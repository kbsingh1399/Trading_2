# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:37:50 IST` (`2026-10-30 05:07:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.22` | **Live Ask Quote**: `4.25` | **Mid Price**: `4.24`
- **Spread Points**: `30.00` | **Spread BPS**: `70.82 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.03` | VWAP Z-Score: `+2.50` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0507` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `63.43` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.24` | Lower -3.00σ Band: `3.81`
  * Upper +2.51σ Band: `4.21` | Lower -2.51σ Band: `3.84`
  * Upper +2.01σ Band: `4.17` | Lower -2.01σ Band: `3.88`
  * Upper +2.00σ Band: `4.17` | Lower -2.00σ Band: `3.88`
  * Upper +1.28σ Band: `4.12` | Lower -1.28σ Band: `3.93`
  * Upper +1.00σ Band: `4.10` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.14` | EMA-20=`4.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.18` (Slope: `+0.0000`) | EMA-100=`4.29`
  * Institutional Anchors: EMA-144=`4.34` | EMA-200=`4.39` (Slope: `-0.7912`) | EMA-233=`4.42`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.15` (Distance: `+2.09%`)
  * Point of Control (POC) = `4.09` (Distance: `+3.44%`)
  * Value Area Low (VAL) = `3.97` (Distance: `+6.72%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.69` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.24` | Low=`4.21`
  * New York Session (13:00-21:00 UTC): High=`4.26` | Low=`4.21`
  * Initial Balance (First Hour): IB High=`4.24` | IB Low=`4.21`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.22` - `4.25`
  * Optimal Trade Entry (OTE 0.705): `4.24`
  * Structural Invalidation Anchor (0.786): `4.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.23` | `4.24` | `4.22` | `4.24` | `662,557` | 2,804,867.48 USD | 246,036.83 USD | `+8.77%` | -26,918,850.69 USD | `-0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4.24` | `4.24` | `4.22` | `4.22` | `499,572` | 2,113,847.20 USD | -911,221.20 USD | `-43.11%` | -27,830,071.89 USD | `-1.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.22` | `4.25` | `4.22` | `4.24` | `612,396` | 2,596,034.46 USD | -704,525.85 USD | `-27.14%` | -28,534,597.75 USD | `-1.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.20` | `4.20` | `4.18` | `4.20` | `1,011,226` | 4,237,923.38 USD | -720,370.54 USD | `-17.00%` | -27,474,992.00 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.20` | `4.24` | `4.20` | `4.22` | `1,761,726` | 7,447,660.88 USD | -826,781.65 USD | `-11.10%` | -28,301,773.65 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.22` | `4.25` | `4.22` | `4.24` | `612,396` | 2,596,034.46 USD | -704,525.85 USD | `-27.14%` | -29,006,299.51 USD | `-0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.06` | `4.17` | `4.06` | `4.16` | `6,011,715` | 24,741,893.48 USD | 4,089,779.03 USD | `+16.53%` | -28,096,918.96 USD | `+1.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4.16` | `4.24` | `4.12` | `4.22` | `7,320,214` | 30,649,363.67 USD | 998,131.84 USD | `+3.26%` | -27,098,787.12 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.22` | `4.25` | `4.22` | `4.24` | `611,398` | 2,591,805.93 USD | -708,703.55 USD | `-27.34%` | -27,807,490.67 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.25` | `4.12` | `4.24` | `7,932,610` | 33,245,398.13 USD | 293,605.99 USD | `+0.88%` | -13,015,423.97 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | 3,315,318.08 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -853,625.74 USD | `-1.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.25` | `4.12` | `4.24` | `7,932,610` | 33,245,398.13 USD | 293,605.99 USD | `+0.88%` | -13,015,423.97 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `61` | `0x7737...bf66` | `LONG` | 23,898,838.42 USD | `5,640,376.30` | `2.35` | `4.24` | `0.8570` | 10,626,935.59 USD | `+44.47%` | `10X Cross` |
| `103` | `0xefe4...194b` | `SHORT` | 19,103,581.38 USD | `4,507,262.50` | `4.21` | `4.24` | `6.60` | -128,484.67 USD | `-0.67%` | `5X Cross` |
| `134` | `0xb581...6f4f` | `LONG` | 15,252,840.00 USD | `3,600,000.00` | `5.19` | `4.24` | `0.000000` | -3,440,195.22 USD | `-22.55%` | `4X Cross` |
| `211` | `0xdd53...2b13` | `SHORT` | 10,171,336.02 USD | `2,400,202.00` | `2.31` | `4.24` | `28.89` | -4,625,487.46 USD | `-45.48%` | `3X Cross` |
| `268` | `0x77ee...2902` | `LONG` | 8,741,854.08 USD | `2,063,023.10` | `1.93` | `4.24` | `0.000000` | 4,750,658.15 USD | `+54.34%` | `10X Cross` |
| `360` | `0x9df2...c665` | `SHORT` | 6,416,816.85 USD | `1,514,579.00` | `2.36` | `4.24` | `23.81` | -2,836,827.19 USD | `-44.21%` | `10X Cross` |
| `377` | `0xb83d...6e36` | `SHORT` | 6,125,247.58 USD | `1,445,759.10` | `5.19` | `4.24` | `91.75` | 1,384,201.36 USD | `+22.60%` | `3X Cross` |
| `378` | `0x7fda...17d1` | `SHORT` | 6,120,756.11 USD | `1,443,915.10` | `4.28` | `4.24` | `28.77` | 61,322.41 USD | `+1.00%` | `10X Cross` |
| `396` | `0xb46b...538e` | `SHORT` | 5,661,099.60 USD | `1,336,000.00` | `4.33` | `4.24` | `7.44` | 123,764.46 USD | `+2.19%` | `10X Cross` |
| `467` | `0x60b0...991e` | `LONG` | 4,752,099.49 USD | `1,121,307.10` | `5.00` | `4.24` | `0.000000` | -849,324.94 USD | `-17.87%` | `10X Cross` |
| `494` | `0xcac1...26b3` | `SHORT` | 4,550,741.40 USD | `1,073,743.90` | `2.48` | `4.24` | `12.15` | -1,890,797.93 USD | `-41.55%` | `10X Cross` |
| `514` | `0x781e...96b7` | `SHORT` | 4,400,750.23 USD | `1,039,604.60` | `2.45` | `4.24` | `7.46` | -1,856,413.04 USD | `-42.18%` | `10X Cross` |
| `592` | `0x45d2...4029` | `SHORT` | 3,853,173.27 USD | `909,400.00` | `3.26` | `4.24` | `47.94` | -887,023.37 USD | `-23.02%` | `10X Cross` |
| `598` | `0x4cae...7c34` | `LONG` | 3,816,149.05 USD | `900,587.40` | `3.97` | `4.24` | `2.84` | 237,956.26 USD | `+6.24%` | `10X Cross` |
| `826` | `0x005a...61fe` | `LONG` | 2,762,519.14 USD | `652,414.60` | `2.08` | `4.24` | `2.41` | 1,404,987.90 USD | `+50.86%` | `7X Cross` |
| `832` | `0xba5d...a352` | `SHORT` | 2,743,530.45 USD | `647,532.50` | `2.83` | `4.24` | `13.22` | -910,815.51 USD | `-33.20%` | `10X Cross` |
| `848` | `0xb695...a92d` | `SHORT` | 2,709,319.64 USD | `639,231.70` | `4.57` | `4.24` | `44.56` | 214,039.29 USD | `+7.90%` | `10X Cross` |
| `849` | `0xd1dd...9e85` | `SHORT` | 2,701,600.18 USD | `637,621.00` | `4.96` | `4.24` | `18.07` | 461,872.56 USD | `+17.10%` | `10X Cross` |
| `852` | `0x123d...3bff` | `SHORT` | 2,687,740.25 USD | `634,140.30` | `2.09` | `4.24` | `9.09` | -1,364,404.47 USD | `-50.76%` | `10X Cross` |
| `864` | `0xcf53...ee11` | `SHORT` | 2,633,339.46 USD | `621,598.40` | `5.07` | `4.24` | `25.08` | 518,830.79 USD | `+19.70%` | `10X Cross` |
| `987` | `0xbfc7...80b4` | `SHORT` | 2,249,793.90 USD | `531,000.00` | `2.01` | `4.24` | `7.12` | -1,184,594.51 USD | `-52.65%` | `10X Cross` |
| `1246` | `0x0eec...d4c5` | `LONG` | 1,779,740.90 USD | `419,948.30` | `4.01` | `4.24` | `1.22` | 97,156.05 USD | `+5.46%` | `10X Cross` |
| `1289` | `0xe097...d0fe` | `LONG` | 1,693,240.00 USD | `400,000.00` | `5.29` | `4.24` | `0.000000` | -423,547.30 USD | `-25.01%` | `10X Cross` |
| `1426` | `0x6e8f...4364` | `LONG` | 1,530,340.53 USD | `361,210.50` | `3.28` | `4.24` | `3.51` | 346,280.30 USD | `+22.63%` | `10X Cross` |
| `1446` | `0xef96...9383` | `SHORT` | 1,513,429.18 USD | `357,412.90` | `4.50` | `4.24` | `14.12` | 95,832.54 USD | `+6.33%` | `10X Cross` |
| `1466` | `0xdf95...7d72` | `SHORT` | 1,484,876.78 USD | `350,413.40` | `4.23` | `4.24` | `108.97` | -1,817.26 USD | `-0.12%` | `10X Cross` |
| `1467` | `0xcf67...eb24` | `LONG` | 1,483,335.00 USD | `350,000.00` | `1.98` | `4.24` | `1.46` | 791,717.12 USD | `+53.37%` | `10X Cross` |
| `1581` | `0xfc27...9d9d` | `SHORT` | 1,356,470.25 USD | `319,997.70` | `5.01` | `4.24` | `59.08` | 247,072.37 USD | `+18.21%` | `10X Cross` |
| `1585` | `0x089f...a4f8` | `LONG` | 1,350,925.05 USD | `319,043.30` | `4.06` | `4.24` | `0.000000` | 56,068.34 USD | `+4.15%` | `1X Cross` |
| `1638` | `0x17c3...a868` | `LONG` | 1,297,082.12 USD | `306,103.30` | `4.36` | `4.24` | `0.000000` | -38,470.62 USD | `-2.97%` | `3X Cross` |
| `1660` | `0x9836...457e` | `LONG` | 1,274,402.55 USD | `300,000.60` | `4.57` | `4.24` | `1.85` | -97,670.62 USD | `-7.66%` | `10X Cross` |
| `1675` | `0x9aa5...58af` | `SHORT` | 1,265,932.52 USD | `298,681.70` | `4.78` | `4.24` | `34.11` | 161,362.80 USD | `+12.75%` | `10X Cross` |
| `1721` | `0xe065...0f85` | `SHORT` | 1,220,691.04 USD | `288,027.90` | `2.81` | `4.24` | `5.57` | -410,137.92 USD | `-33.60%` | `10X Cross` |
| `1911` | `0xff43...d924` | `LONG` | 1,056,998.51 USD | `249,474.50` | `4.64` | `4.24` | `3.28` | -101,045.17 USD | `-9.56%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.51` | 2,645.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.65K USD at 4.5123 USD [API] | `2026-10-29 01:49:15` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 3,997.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 4.00K USD at 4.5169 USD [API] | `2026-10-29 01:49:08` |
| `ANNOUNCEMENT` | `INFO` | `4.53` | 9,057.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.06K USD at 4.5288 USD [API] | `2026-10-29 01:50:32` |
| `ANNOUNCEMENT` | `INFO` | `4.53` | 9,830.42 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.83K USD at 4.5314 USD [API] | `2026-10-29 01:50:29` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 4,438.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 4.44K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 33.02 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.03K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 646.63 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.65K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 10.26 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.01K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 94.61 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.09K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 90.59 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.09K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 1,702.48 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.70K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 473.48 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.47K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 167.79 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.17K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.46` | 11.16 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.01K USD at 4.4626 USD [API] | `2026-10-29 02:05:43` |
| `ANNOUNCEMENT` | `INFO` | `4.49` | 1,344.34 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.34K USD at 4.4901 USD [API] | `2026-10-29 01:58:25` |
| `ANNOUNCEMENT` | `INFO` | `4.50` | 1,732.06 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.73K USD at 4.5012 USD [API] | `2026-10-29 01:57:46` |
| `ANNOUNCEMENT` | `INFO` | `4.51` | 47.33 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.05K USD at 4.5072 USD [API] | `2026-10-29 01:57:43` |
| `ANNOUNCEMENT` | `INFO` | `4.45` | 33,410.89 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 33.41K USD at 4.4469 USD [API] | `2026-10-29 02:29:40` |
| `ANNOUNCEMENT` | `INFO` | `4.45` | 6,653.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.65K USD at 4.4469 USD [API] | `2026-10-29 02:29:40` |
| `ANNOUNCEMENT` | `INFO` | `4.43` | 43.89 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.04K USD at 4.4334 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `4.48` | 360.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.36K USD at 4.4765 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `4.49` | 2,137.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.14K USD at 4.4901 USD [API] | `2026-10-29 01:58:25` |
| `ANNOUNCEMENT` | `INFO` | `4.49` | 43.15 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.04K USD at 4.4947 USD [API] | `2026-10-29 01:58:04` |
| `ANNOUNCEMENT` | `INFO` | `4.49` | 70.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.07K USD at 4.4947 USD [API] | `2026-10-29 01:58:04` |
| `ANNOUNCEMENT` | `INFO` | `4.50` | 141.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.14K USD at 4.5005 USD [API] | `2026-10-29 01:57:46` |
| `ANNOUNCEMENT` | `INFO` | `4.50` | 2,000.92 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.00K USD at 4.5005 USD [API] | `2026-10-29 01:57:46` |
| `ANNOUNCEMENT` | `INFO` | `4.51` | 1,444.49 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.44K USD at 4.5070 USD [API] | `2026-10-29 01:57:39` |
| `ANNOUNCEMENT` | `INFO` | `4.43` | 5,489.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.49K USD at 4.4310 USD [API] | `2026-10-29 02:36:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+4.52%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--7.75%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+4.44%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--7.77%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+4.44%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--7.77%`)
  * 7D Horizon: Short MP=`5.01` (Vol: 953,300.00 USD, Dist: `+18.52%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--7.74%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8650` | 912.83 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 40,360.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 3,040.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 935.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 7,800.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 22,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 30,990.00 USD | 22,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 2,740.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 8,590.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 99,270.00 USD | 22,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 22,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 337.44 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 16,190.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 856.24 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 13,510.00 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 40,820.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 144.69 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 1,720.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 3,440.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 7,390.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 56,130.00 USD | 22,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 517,410.00 USD | 22,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 2,190.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 2,260.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,310.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 21,840.00 USD | 21,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 428.16 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 1,010.00 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 22,870.00 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,000.00 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 2,860.00 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 21,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 1,040.00 USD | 21,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 70,820.00 USD | 21,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 112,730.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 1,020.00 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.44` | 15,310.00 USD | 21,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,660.00 USD | 21,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 5,440.00 USD | 21,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 429.83 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 576,020.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 3,420.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 605.42 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 1,220.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 311.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 23,700.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 15,740.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 191.64 USD | 20,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 15,250.00 USD | 20,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 3,780.00 USD | 20,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 2,040.00 USD | 20,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 1,320.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 574.59 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,380.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 12,850.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 169.50 USD | 20,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 2,190.00 USD | 20,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 6,750.00 USD | 20,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 5,310.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 4,230.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,600.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 722.59 USD | 20,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 20,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 453.93 USD | 20,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 471.73 USD | 20,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 1,350.00 USD | 20,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 8,400.00 USD | 20,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 32,440.00 USD | 20,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 553,500.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 13,220.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 34,420.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,250.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 2,030.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 1,870.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 34,520.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 3,710.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 1,740.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 36,170.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 135.38 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 11,410.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 102.86 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 20,080.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 665.62 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 1,390.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 595.33 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 7,870.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 11,100.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 18,930.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,760.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 6,240.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 15,580.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 34,490.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 59,140.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 92,830.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 189,270.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 292.32 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 1,110.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,010.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 251,500.00 USD | 19,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 3,010.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 243.19 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 12,270.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 310,060.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 184,160.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,370.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 382,060.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 463.86 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 2,150.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 9,680.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 9,000.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 697.50 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,670.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 6,680.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 7,490.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 32,450.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 9,230.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,830,000.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 186,030.00 USD | 16,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,060.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,890.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,700.00 USD | 16,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,240.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 17,050.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 12,710.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 4,600.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,910.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 10,310.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 34,060.00 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 7,270.00 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 456,880.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,260.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,340.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 83,350.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 3,820.00 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 25,280.00 USD | 15,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 20,520.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 7,540.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 5,130.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 733.85 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 357,920.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 21,440.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 28,380.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 9,400.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,690.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 26,770.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 352,610.00 USD | 14,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 49,740.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 191,910.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 97,490.00 USD | 14,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 10,010.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 11,350.00 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 24,770.00 USD | 14,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 8,780.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,580,000.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 9,150.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 475,530.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 18,230.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 14,200.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 14,830.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 82,440.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 49,180.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 431,620.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 50,830.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,100.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 5,090.00 USD | 10,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 37,560.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 178,230.00 USD | 10,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 8,090.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 11,020.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 21,490.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 31,230.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 1,020.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 168,030.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 178,920.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 125,140.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 7,660.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 7,660.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 17,000.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 31,130.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 7,930.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 9,280.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,000.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 25,240.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 12,840.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 57,760.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 249,290.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 219.50 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 4,010.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 13,530.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 31,660.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 56,080.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 20,130.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,640.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 51,010.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 874,570.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 19,440.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 133,000.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 131,270.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 17,060.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 20,150.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 73,060.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 27,160.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,780.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 24,580.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 191,940.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,790.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 888.47 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 98,820.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 415,990.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 28,690.00 USD | 6,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 33,630.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 21,620.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 12,040.00 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,380.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.47` | 14,770,000.00 USD | 14,770,000.00 USD | 40,560.00 USD | 26,960.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 197,260.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.48` | 14,710,000.00 USD | 14,710,000.00 USD | 44,910.00 USD | 13,410.00 USD | 33.52 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 29,090.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.49` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 42.93 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 1,320,000.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 14,650,000.00 USD | 14,650,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 35,120.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 14,580,000.00 USD | 14,580,000.00 USD | 3,690.00 USD | 0.00 USD | 114.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 37,770.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 14,580,000.00 USD | 14,580,000.00 USD | 15,180.00 USD | 0.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 195,120.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 14,520,000.00 USD | 14,520,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 120,780.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 14,290,000.00 USD | 14,290,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 167,840.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 14,200,000.00 USD | 14,200,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 374,310.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 13,970,000.00 USD | 13,970,000.00 USD | 61,170.00 USD | 0.00 USD | 158.35 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 9,160.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 13,910,000.00 USD | 13,910,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 61,480.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 13,710,000.00 USD | 13,710,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 33,150.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 13,430,000.00 USD | 13,430,000.00 USD | 535.75 USD | 18,170.00 USD | 37.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 109,830.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 13,410,000.00 USD | 13,410,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 60,200.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 13,310,000.00 USD | 13,310,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 16,360.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 13,170,000.00 USD | 13,170,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 125,710.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 12,950,000.00 USD | 12,950,000.00 USD | 50,840.00 USD | 8,120.00 USD | 156.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 230,840.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 13,070,000.00 USD | 13,070,000.00 USD | 1,300.00 USD | 5,040.00 USD | 303.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 12,890,000.00 USD | 12,890,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 19,580.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 13,060,000.00 USD | 13,060,000.00 USD | 1,410.00 USD | 23,490.00 USD | 14,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 12,730,000.00 USD | 12,730,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 12,700.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 13,020,000.00 USD | 13,020,000.00 USD | 52,660.00 USD | 13,280.00 USD | 70.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 12,640,000.00 USD | 12,640,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 56,050.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 12,960,000.00 USD | 12,960,000.00 USD | 2,720.00 USD | 0.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 12,460,000.00 USD | 12,460,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 99,010.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 12,940,000.00 USD | 12,940,000.00 USD | 680.67 USD | 3,880.00 USD | 31,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.68` | 12,340,000.00 USD | 12,340,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 287,470.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 12,910,000.00 USD | 12,910,000.00 USD | 24,450.00 USD | 0.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 12,340,000.00 USD | 12,340,000.00 USD | 27,750.00 USD | 0.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 94,330.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 12,870,000.00 USD | 12,870,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 12,250,000.00 USD | 12,250,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 212,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 12,770,000.00 USD | 12,770,000.00 USD | 16,480.00 USD | 0.00 USD | 780.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 12,110,000.00 USD | 12,110,000.00 USD | 51,960.00 USD | 0.00 USD | 74,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 72,730.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 12,750,000.00 USD | 12,750,000.00 USD | 18,460.00 USD | 0.00 USD | 228.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 11,990,000.00 USD | 11,990,000.00 USD | 425.03 USD | 0.00 USD | 546.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 224,660.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 12,730,000.00 USD | 12,730,000.00 USD | 405.02 USD | 11,920.00 USD | 25,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 11,990,000.00 USD | 11,990,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 122,190.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 12,700,000.00 USD | 12,700,000.00 USD | 108,320.00 USD | 56,340.00 USD | 82,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 11,880,000.00 USD | 11,880,000.00 USD | 130,620.00 USD | 40,020.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 39,750.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 12,450,000.00 USD | 12,450,000.00 USD | 1,720.00 USD | 0.00 USD | 52,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 11,580,000.00 USD | 11,580,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 201,260.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 12,400,000.00 USD | 12,400,000.00 USD | 1,260.00 USD | 8,310.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 11,400,000.00 USD | 11,400,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 60,660.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 12,390,000.00 USD | 12,390,000.00 USD | 48,010.00 USD | 54,910.00 USD | 1,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 11,330,000.00 USD | 11,330,000.00 USD | 15,340.00 USD | 8,090.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 64,270.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 12,280,000.00 USD | 12,280,000.00 USD | 4,250.00 USD | 0.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 11,290,000.00 USD | 11,290,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 31,540.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 12,260,000.00 USD | 12,260,000.00 USD | 4,270.00 USD | 24,440.00 USD | 68,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 11,130,000.00 USD | 11,130,000.00 USD | 51,640.00 USD | 0.00 USD | 137,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 137,950.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 12,160,000.00 USD | 12,160,000.00 USD | 3,400.00 USD | 0.00 USD | 74,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 10,940,000.00 USD | 10,940,000.00 USD | 6,530.00 USD | 18,170.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 456,920.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 12,080,000.00 USD | 12,080,000.00 USD | 212,830.00 USD | 0.00 USD | 79,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 10,900,000.00 USD | 10,900,000.00 USD | 5,310.00 USD | 0.00 USD | 810.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 100,730.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 11,790,000.00 USD | 11,790,000.00 USD | 3,240.00 USD | 21,590.00 USD | 94,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 10,890,000.00 USD | 10,890,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 161,990.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 11,670,000.00 USD | 11,670,000.00 USD | 93,470.00 USD | 91,390.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 33,630.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 198,060.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 11,370,000.00 USD | 11,370,000.00 USD | 150,080.00 USD | 33,720.00 USD | 33,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 10,800,000.00 USD | 10,800,000.00 USD | 7,940.00 USD | 33,350.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 123,400.00 USD | 961,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 11,160,000.00 USD | 11,160,000.00 USD | 156,570.00 USD | 160,920.00 USD | 408.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 10,760,000.00 USD | 10,760,000.00 USD | 3,390.00 USD | 49,170.00 USD | 252.34 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 81,300.00 USD | 837,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 10,840,000.00 USD | 10,840,000.00 USD | 39,850.00 USD | 46,130.00 USD | 107,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 10,710,000.00 USD | 10,710,000.00 USD | 5,190.00 USD | 156,620.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 33,810.00 USD | 756,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 10,640,000.00 USD | 10,640,000.00 USD | 3,490.00 USD | 70,020.00 USD | 152,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 10,470,000.00 USD | 10,470,000.00 USD | 63,710.00 USD | 0.00 USD | 229,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 29,390.00 USD | 722,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 10,420,000.00 USD | 10,420,000.00 USD | 109,330.00 USD | 24,380.00 USD | 227,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 10,180,000.00 USD | 10,180,000.00 USD | 110,160.00 USD | 77,860.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 238,510.00 USD | 693,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 10,060,000.00 USD | 10,060,000.00 USD | 446,590.00 USD | 91,430.00 USD | 197,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,890,000.00 USD | 9,890,000.00 USD | 4,240.00 USD | 50,710.00 USD | 82,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 99,530.00 USD | 454,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 9,320,000.00 USD | 9,320,000.00 USD | 32,970.00 USD | 59,980.00 USD | 246,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,750,000.00 USD | 9,750,000.00 USD | 274,050.00 USD | 28,250.00 USD | 54,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,110.00 USD | 355,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 8,980,000.00 USD | 8,980,000.00 USD | 337,210.00 USD | 120,100.00 USD | 261,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 9,390,000.00 USD | 9,390,000.00 USD | 121,570.00 USD | 67,260.00 USD | 50,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 161,730.00 USD | 349,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 8,260,000.00 USD | 8,260,000.00 USD | 317,510.00 USD | 8,570.00 USD | 125,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 9,150,000.00 USD | 9,150,000.00 USD | 85,790.00 USD | 66,710.00 USD | 97,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 304.58 USD | 187,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 7,810,000.00 USD | 7,810,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,900,000.00 USD | 8,900,000.00 USD | 30,960.00 USD | 28,720.00 USD | 1,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 6,340.00 USD | 187,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 7,500,000.00 USD | 7,500,000.00 USD | 132,520.00 USD | 53,060.00 USD | 136,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,840,000.00 USD | 8,840,000.00 USD | 75,150.00 USD | 0.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 147,750.00 USD | 180,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 7,170,000.00 USD | 7,170,000.00 USD | 114,710.00 USD | 0.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,770,000.00 USD | 8,770,000.00 USD | 8,490.00 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.96` | 7,030,000.00 USD | 7,030,000.00 USD | 66,520.00 USD | 22,830.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,750,000.00 USD | 8,750,000.00 USD | 165,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.97` | 6,920,000.00 USD | 6,920,000.00 USD | 772.10 USD | 36,470.00 USD | 137,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 8,590,000.00 USD | 8,590,000.00 USD | 235,890.00 USD | 0.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 33,140.00 USD | 33,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 6,750,000.00 USD | 6,750,000.00 USD | 19,950.00 USD | 76,990.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 8,350,000.00 USD | 8,350,000.00 USD | 506,280.00 USD | 0.00 USD | 279,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.99` | 6,550,000.00 USD | 6,550,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 7,570,000.00 USD | 7,570,000.00 USD | 298,270.00 USD | 26,340.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.00` | 6,350,000.00 USD | 6,350,000.00 USD | 39,240.00 USD | 17,140.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 7,160,000.00 USD | 7,160,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.01` | 6,160,000.00 USD | 6,160,000.00 USD | 473.90 USD | 158,450.00 USD | 222,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 6,210,000.00 USD | 6,210,000.00 USD | 368,350.00 USD | 57,440.00 USD | 437,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.02` | 5,770,000.00 USD | 5,770,000.00 USD | 109,790.00 USD | 41,930.00 USD | 72,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 5,350,000.00 USD | 5,350,000.00 USD | 271,690.00 USD | 156,620.00 USD | 253,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.03` | 5,550,000.00 USD | 5,550,000.00 USD | 38,390.00 USD | 48,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,670,000.00 USD | 4,670,000.00 USD | 245,910.00 USD | 0.00 USD | 346,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.04` | 5,460,000.00 USD | 5,460,000.00 USD | 66,450.00 USD | 21,940.00 USD | 183,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 4,070,000.00 USD | 4,070,000.00 USD | 321,230.00 USD | 0.00 USD | 492,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.05` | 5,190,000.00 USD | 5,190,000.00 USD | 347,570.00 USD | 23,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 270.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.06` | 4,820,000.00 USD | 4,820,000.00 USD | 34,760.00 USD | 72,940.00 USD | 386,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 72,410.00 USD | 925.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.07` | 4,330,000.00 USD | 4,330,000.00 USD | 218,800.00 USD | 179,680.00 USD | 188,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 287,180.00 USD | 166,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.08` | 3,740,000.00 USD | 3,740,000.00 USD | 68,020.00 USD | 196,150.00 USD | 79,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 237,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.09` | 3,390,000.00 USD | 3,390,000.00 USD | 163,310.00 USD | 0.00 USD | 151,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 2,500,000.00 USD | 2,500,000.00 USD | 127,170.00 USD | 137,180.00 USD | 432,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.10` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 58,480.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 1,800,000.00 USD | 1,800,000.00 USD | 24,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.11` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 60,170.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 98,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.12` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 379,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 137,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.13` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 310,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 164,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 2,110,000.00 USD | 2,110,000.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 1,370,000.00 USD | 1,370,000.00 USD | 238,150.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.14` | 90,630.00 USD | 90,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 2,050,000.00 USD | 2,050,000.00 USD | 469,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 1,040,000.00 USD | 1,040,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.17` | 1,580,000.00 USD | 1,580,000.00 USD | 58,020.00 USD | 0.00 USD | 293.77 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 10,040.00 USD | 100,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 1,520,000.00 USD | 1,520,000.00 USD | 329,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 1,550.00 USD | 102,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 1,190,000.00 USD | 1,190,000.00 USD | 204,570.00 USD | 0.00 USD | 293.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 808,880.00 USD | 808,880.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 261.35 USD | 102,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 986,390.00 USD | 986,390.00 USD | 66,990.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 806,120.00 USD | 806,120.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 4,100.00 USD | 106,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 846,700.00 USD | 846,700.00 USD | 168,700.00 USD | 98,820.00 USD | 42,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 206,800.00 USD | 206,800.00 USD | 2,900.00 USD | 0.00 USD | 82,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 837.10 USD | 107,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 536,340.00 USD | 536,340.00 USD | 97,990.00 USD | 129,920.00 USD | 308,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 121,900.00 USD | 121,900.00 USD | 121,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.22` | 165.62 USD | 107,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.23` | 651,000.00 USD | 651,000.00 USD | 1,340.00 USD | 427,200.00 USD | 222,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 1,300,000.00 USD | 1,300,000.00 USD | 1,340.00 USD | 427,200.00 USD | 222,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.23` | 284,010.00 USD | 284,010.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.23` | 568,030.00 USD | 568,030.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.24` | 18,110.00 USD | 125,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,320,000.00 USD | 2,320,000.00 USD | 594,350.00 USD | 137,280.00 USD | 285,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.24` | 719,410.00 USD | 719,410.00 USD | 2,900.00 USD | 52,690.00 USD | 95,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.25` | 296.30 USD | 125,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.25` | 2,910,000.00 USD | 2,910,000.00 USD | 4,080.00 USD | 82,610.00 USD | 501,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,380,000.00 USD | 1,380,000.00 USD | 3,390.00 USD | 223,240.00 USD | 433,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,370,000.00 USD | 3,370,000.00 USD | 150,470.00 USD | 221,190.00 USD | 93,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 2,120,000.00 USD | 2,120,000.00 USD | 2,960.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.26` | 59,310.00 USD | 185,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,280,000.00 USD | 4,280,000.00 USD | 699,060.00 USD | 51,930.00 USD | 152,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,910,000.00 USD | 3,910,000.00 USD | 24,810.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,730,000.00 USD | 4,730,000.00 USD | 125,880.00 USD | 41,380.00 USD | 285,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,820,000.00 USD | 5,820,000.00 USD | 119,230.00 USD | 497,680.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 163.69 USD | 185,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,080,000.00 USD | 5,080,000.00 USD | 156,040.00 USD | 32,690.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,880,000.00 USD | 5,880,000.00 USD | 5,150.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 210,730.00 USD | 396,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,360,000.00 USD | 5,360,000.00 USD | 65,250.00 USD | 56,980.00 USD | 163,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,350,000.00 USD | 6,350,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 6,350.00 USD | 402,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,990,000.00 USD | 5,990,000.00 USD | 376,510.00 USD | 50,050.00 USD | 194,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,790,000.00 USD | 6,790,000.00 USD | 215,700.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 37,740.00 USD | 440,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 6,300,000.00 USD | 6,300,000.00 USD | 107,540.00 USD | 106,760.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,530,000.00 USD | 7,530,000.00 USD | 268,260.00 USD | 160,980.00 USD | 309,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 230.52 USD | 440,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,870,000.00 USD | 6,870,000.00 USD | 292,220.00 USD | 158,240.00 USD | 127,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,710,000.00 USD | 7,710,000.00 USD | 8,950.00 USD | 84,830.00 USD | 91,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,480,000.00 USD | 7,480,000.00 USD | 273,450.00 USD | 140,540.00 USD | 189,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 8,170,000.00 USD | 8,170,000.00 USD | 9,550.00 USD | 97,260.00 USD | 351,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 444,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,660,000.00 USD | 7,660,000.00 USD | 2,840.00 USD | 39,020.00 USD | 144,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 8,260,000.00 USD | 8,260,000.00 USD | 2,410.00 USD | 0.00 USD | 85,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 2,290.00 USD | 446,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,830,000.00 USD | 7,830,000.00 USD | 86,330.00 USD | 20,830.00 USD | 60,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 8,410,000.00 USD | 8,410,000.00 USD | 10,460.00 USD | 0.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.37` | 423.84 USD | 447,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 8,140,000.00 USD | 8,140,000.00 USD | 110,040.00 USD | 46,860.00 USD | 156,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 6,940.00 USD | 454,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 9,010,000.00 USD | 9,010,000.00 USD | 250,760.00 USD | 34,500.00 USD | 584,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 203.90 USD | 454,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 9,430,000.00 USD | 9,430,000.00 USD | 37,480.00 USD | 41,380.00 USD | 333,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 9,330,000.00 USD | 9,330,000.00 USD | 252,620.00 USD | 108,260.00 USD | 158,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 192,710.00 USD | 647,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,950,000.00 USD | 9,950,000.00 USD | 385,030.00 USD | 47,530.00 USD | 92,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,940,000.00 USD | 9,940,000.00 USD | 111,810.00 USD | 26,950.00 USD | 466,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 648,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 10,340,000.00 USD | 10,340,000.00 USD | 197,850.00 USD | 130,890.00 USD | 61,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 10,280,000.00 USD | 10,280,000.00 USD | 1,450.00 USD | 65,600.00 USD | 273,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 10,420,000.00 USD | 10,420,000.00 USD | 1,080.00 USD | 60,770.00 USD | 22,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,930,000.00 USD | 10,930,000.00 USD | 404,280.00 USD | 71,590.00 USD | 176,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 671.71 USD | 649,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 10,570,000.00 USD | 10,570,000.00 USD | 6,140.00 USD | 49,400.00 USD | 94,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 11,210,000.00 USD | 11,210,000.00 USD | 163,540.00 USD | 46,230.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 11,360,000.00 USD | 11,360,000.00 USD | 154,690.00 USD | 339,100.00 USD | 295,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 143,990.00 USD | 72,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 11,420,000.00 USD | 11,420,000.00 USD | 1,750.00 USD | 50,720.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 11,450,000.00 USD | 11,450,000.00 USD | 2,300.00 USD | 24,070.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 11,500,000.00 USD | 11,500,000.00 USD | 3,070.00 USD | 62,110.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 649,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 11,500,000.00 USD | 11,500,000.00 USD | 797.71 USD | 25,190.00 USD | 30,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,840,000.00 USD | 11,840,000.00 USD | 204,140.00 USD | 135,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 629.18 USD | 650,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 11,780,000.00 USD | 11,780,000.00 USD | 167,410.00 USD | 86,520.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,840,000.00 USD | 11,840,000.00 USD | 1,870.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 12,350,000.00 USD | 12,350,000.00 USD | 253,770.00 USD | 155,000.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 12,180,000.00 USD | 12,180,000.00 USD | 244,370.00 USD | 93,790.00 USD | 504.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 280.49 USD | 650,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 12,940,000.00 USD | 12,940,000.00 USD | 362,590.00 USD | 69,580.00 USD | 149,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 12,750,000.00 USD | 12,750,000.00 USD | 374,250.00 USD | 200,700.00 USD | 343.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 283.81 USD | 650,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 13,670,000.00 USD | 13,670,000.00 USD | 187,350.00 USD | 223,860.00 USD | 327,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,830,000.00 USD | 12,830,000.00 USD | 77,780.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 389.19 USD | 651,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 14,300,000.00 USD | 14,300,000.00 USD | 287,830.00 USD | 92,260.00 USD | 243,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,970,000.00 USD | 12,970,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,820.00 USD | 670,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 15,080,000.00 USD | 15,080,000.00 USD | 501,550.00 USD | 0.00 USD | 280,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,960,000.00 USD | 13,960,000.00 USD | 439,420.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 15,480,000.00 USD | 15,480,000.00 USD | 12,950.00 USD | 150,600.00 USD | 234,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 394.51 USD | 670,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 34,450.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 713.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 16,020,000.00 USD | 16,020,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 15,680,000.00 USD | 15,680,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 16,370,000.00 USD | 16,370,000.00 USD | 177,440.00 USD | 70,180.00 USD | 98,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 16,230,000.00 USD | 16,230,000.00 USD | 305,830.00 USD | 27,650.00 USD | 210,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 14,690.00 USD | 685,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,660,000.00 USD | 17,660,000.00 USD | 481,120.00 USD | 99,430.00 USD | 717,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 16,360,000.00 USD | 16,360,000.00 USD | 44,380.00 USD | 0.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,410,000.00 USD | 18,410,000.00 USD | 559,590.00 USD | 75,460.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 18,070,000.00 USD | 18,070,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,580,000.00 USD | 18,580,000.00 USD | 54,700.00 USD | 50,860.00 USD | 68,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 18,180,000.00 USD | 18,180,000.00 USD | 3,460.00 USD | 112,080.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 686,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,720,000.00 USD | 18,720,000.00 USD | 66,880.00 USD | 7,560.00 USD | 59,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 18,190,000.00 USD | 18,190,000.00 USD | 3,350.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,860,000.00 USD | 18,860,000.00 USD | 95,090.00 USD | 31,380.00 USD | 19,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 18,320,000.00 USD | 18,320,000.00 USD | 134,680.00 USD | 0.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,870,000.00 USD | 18,870,000.00 USD | 1,180.00 USD | 0.00 USD | 360.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 18,540,000.00 USD | 18,540,000.00 USD | 213,490.00 USD | 0.00 USD | 431.56 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 687,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 19,040,000.00 USD | 19,040,000.00 USD | 118,230.00 USD | 11,270.00 USD | 41,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 19,060,000.00 USD | 19,060,000.00 USD | 501,930.00 USD | 18,170.00 USD | 407.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 143.07 USD | 687,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 19,780,000.00 USD | 19,780,000.00 USD | 201,570.00 USD | 52,020.00 USD | 488,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 19,480,000.00 USD | 19,480,000.00 USD | 420,940.00 USD | 0.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 124.75 USD | 687,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 20,480,000.00 USD | 20,480,000.00 USD | 157,430.00 USD | 299,030.00 USD | 249,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 19,790,000.00 USD | 19,790,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 687,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 20,900,000.00 USD | 20,900,000.00 USD | 118,960.00 USD | 0.00 USD | 301,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 21,160,000.00 USD | 21,160,000.00 USD | 112,140.00 USD | 81,340.00 USD | 61,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 20,750,000.00 USD | 20,750,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 151,470.00 USD | 839,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 21,560,000.00 USD | 21,560,000.00 USD | 133,390.00 USD | 40,000.00 USD | 225,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 20,840,000.00 USD | 20,840,000.00 USD | 2,450.00 USD | 0.00 USD | 88,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 839,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.70` | 21,160,000.00 USD | 21,160,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 846,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.71` | 21,570,000.00 USD | 21,570,000.00 USD | 178,360.00 USD | 232,800.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 250.37 USD | 847,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.72` | 21,760,000.00 USD | 21,760,000.00 USD | 7,140.00 USD | 0.00 USD | 180,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 21,840,000.00 USD | 21,840,000.00 USD | 59,970.00 USD | 15,660.00 USD | 790.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 22,160,000.00 USD | 22,160,000.00 USD | 14,750.00 USD | 173,100.00 USD | 130,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 22,700,000.00 USD | 22,700,000.00 USD | 17,340.00 USD | 185,060.00 USD | 342,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 24,050,000.00 USD | 24,050,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 275,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,950,000.00 USD | 24,950,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 12,840.00 USD | 859,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 26,090,000.00 USD | 26,090,000.00 USD | 499,950.00 USD | 477,230.00 USD | 153,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 860,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 27,120,000.00 USD | 27,120,000.00 USD | 713,060.00 USD | 249,310.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 861,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 28,710,000.00 USD | 28,710,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 29,340,000.00 USD | 29,340,000.00 USD | 400,800.00 USD | 125,900.00 USD | 102,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 32,110,000.00 USD | 32,110,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 863,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,750,000.00 USD | 33,750,000.00 USD | 822,860.00 USD | 85,680.00 USD | 740,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,950.00 USD | 865,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 34,250,000.00 USD | 34,250,000.00 USD | 97,300.00 USD | 71,790.00 USD | 323,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 876,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 36,280,000.00 USD | 36,280,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 37,690,000.00 USD | 37,690,000.00 USD | 444,810.00 USD | 162,380.00 USD | 801,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 876,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,750,000.00 USD | 38,750,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 40,270,000.00 USD | 40,270,000.00 USD | 450,900.00 USD | 266,980.00 USD | 793,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 877,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,850,000.00 USD | 40,850,000.00 USD | 213,960.00 USD | 100,850.00 USD | 271,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,990,000.00 USD | 41,990,000.00 USD | 451,360.00 USD | 145,910.00 USD | 541,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 43,430,000.00 USD | 43,430,000.00 USD | 637,320.00 USD | 208,910.00 USD | 591,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 898,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 45,160,000.00 USD | 45,160,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 900,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,720,000.00 USD | 46,720,000.00 USD | 730,010.00 USD | 78,190.00 USD | 748,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 900,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 48,040,000.00 USD | 48,040,000.00 USD | 339,870.00 USD | 290,290.00 USD | 694,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 900,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 135,500.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 1,190.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.21` | 2,610.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 6,220.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 21,300.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 1,060,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 59,660.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,710.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 3,900.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 5,410.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 419.04 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 296,230.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 1,600,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.55` | 55,550.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,580.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.63` | 63,960.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 405,140.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.76` | 148.16 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.78` | 670.48 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 2,680.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 337,490.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 439.54 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 200.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 378,490.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 345,420.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.20` | 1,890.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 14,150.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 24,830.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 261,360.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 5,760.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 77,220.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.50` | 5,550.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 1,230,000.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 40,450.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 51,310.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 88,290.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 30,000,000.00 USD | 37,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 37,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 37,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.70` | 9,270.00 USD | 37,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 37,370.00 USD | 38,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.74` | 946.94 USD | 38,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.82` | 187.41 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 2,460.00 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 39,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 39,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 39,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 39,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.05` | 559.46 USD | 39,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 39,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 39,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.22` | 3,840,000.00 USD | 43,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 3,500.00 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 773.95 USD | 43,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 106,150.00 USD | 43,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 43,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 9,970,000.00 USD | 53,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 7,800,000.00 USD | 61,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 61,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 3,350.00 USD | 61,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 61,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 61,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 6,100.00 USD | 61,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 259.56 USD | 61,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 61,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 105,820.00 USD | 61,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 498.51 USD | 61,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 74,390.00 USD | 61,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 61,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 325.24 USD | 61,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 61,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 61,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.97` | 95,700.00 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.00` | 167.10 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.04` | 318.19 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 363.86 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.28` | 700,250.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8550` | 27,920,000.00 USD | 0.00 USD | 4,820,000.00 USD | `-79.76%` | `5,641,576.30` |
| `Live` | `Long` | `0.8650` | 23,100,000.00 USD | 0.00 USD | 433.80 USD | `-79.52%` | `501.50` |
| `Live` | `Long` | `0.8750` | 23,100,000.00 USD | 0.00 USD | 484.57 USD | `-79.29%` | `553.80` |
| `Live` | `Long` | `0.8950` | 23,100,000.00 USD | 0.00 USD | 38,570.00 USD | `-78.81%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 23,060,000.00 USD | 0.00 USD | 292.22 USD | `-78.58%` | `322.90` |
| `Live` | `Long` | `0.9150` | 23,060,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.34%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 23,050,000.00 USD | 0.00 USD | 84,010.00 USD | `-78.10%` | `90,819.90` |
| `Live` | `Long` | `0.9350` | 22,970,000.00 USD | 0.00 USD | 100.51 USD | `-77.87%` | `107.50` |
| `Live` | `Long` | `0.9450` | 22,970,000.00 USD | 0.00 USD | 945.00 USD | `-77.63%` | `1,000.00` |
| `Live` | `Long` | `0.9650` | 22,960,000.00 USD | 0.00 USD | 6,750.00 USD | `-77.16%` | `7,000.00` |
| `Live` | `Long` | `0.9850` | 22,960,000.00 USD | 0.00 USD | 707.53 USD | `-76.68%` | `718.30` |
| `Live` | `Long` | `0.9950` | 22,960,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.45%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,800,000.00 USD | 0.00 USD | 110.55 USD | `-76.21%` | `110.00` |
| `Live` | `Long` | `1.01` | 22,800,000.00 USD | 0.00 USD | 31,300.00 USD | `-75.97%` | `30,836.80` |
| `Live` | `Long` | `1.02` | 22,770,000.00 USD | 0.00 USD | 10,250.00 USD | `-75.74%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,760,000.00 USD | 0.00 USD | 5,070.00 USD | `-75.50%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,760,000.00 USD | 0.00 USD | 2,740.00 USD | `-75.26%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 22,750,000.00 USD | 0.00 USD | 4,540.00 USD | `-75.03%` | `4,305.70` |
| `Live` | `Long` | `1.06` | 22,750,000.00 USD | 0.00 USD | 892.90 USD | `-74.79%` | `838.40` |
| `Live` | `Long` | `1.07` | 22,750,000.00 USD | 0.00 USD | 5,310.00 USD | `-74.55%` | `4,939.60` |
| `Live` | `Long` | `1.08` | 22,740,000.00 USD | 0.00 USD | 8,400.00 USD | `-74.32%` | `7,737.80` |
| `Live` | `Long` | `1.10` | 22,730,000.00 USD | 0.00 USD | 16,340.00 USD | `-73.84%` | `14,783.90` |
| `Live` | `Long` | `1.11` | 22,720,000.00 USD | 0.00 USD | 1,500.00 USD | `-73.61%` | `1,347.00` |
| `Live` | `Long` | `1.12` | 22,720,000.00 USD | 0.00 USD | 856.24 USD | `-73.37%` | `761.10` |
| `Live` | `Long` | `1.14` | 22,720,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.13%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 22,710,000.00 USD | 0.00 USD | 26,620.00 USD | `-72.89%` | `23,252.70` |
| `Live` | `Long` | `1.16` | 22,680,000.00 USD | 0.00 USD | 17,320.00 USD | `-72.66%` | `15,000.00` |
| `Live` | `Long` | `1.17` | 22,670,000.00 USD | 0.00 USD | 144.69 USD | `-72.42%` | `124.20` |
| `Live` | `Long` | `1.18` | 22,670,000.00 USD | 0.00 USD | 3,900.00 USD | `-72.18%` | `3,318.50` |
| `Live` | `Long` | `1.19` | 22,660,000.00 USD | 0.00 USD | 238.78 USD | `-71.95%` | `201.50` |
| `Live` | `Long` | `1.20` | 22,660,000.00 USD | 0.00 USD | 1,290.00 USD | `-71.71%` | `1,083.50` |
| `Live` | `Long` | `1.21` | 22,660,000.00 USD | 0.00 USD | 507,290.00 USD | `-71.47%` | `420,990.70` |
| `Live` | `Long` | `1.23` | 22,150,000.00 USD | 0.00 USD | 1,120.00 USD | `-71.00%` | `912.40` |
| `Live` | `Long` | `1.25` | 22,150,000.00 USD | 0.00 USD | 7,130.00 USD | `-70.53%` | `5,727.90` |
| `Live` | `Long` | `1.25` | 22,150,000.00 USD | 0.00 USD | 15,020.00 USD | `-70.29%` | `11,969.60` |
| `Live` | `Long` | `1.26` | 22,130,000.00 USD | 0.00 USD | 104,800.00 USD | `-70.05%` | `82,845.10` |
| `Live` | `Long` | `1.27` | 22,030,000.00 USD | 0.00 USD | 5,090.00 USD | `-69.82%` | `3,991.50` |
| `Live` | `Long` | `1.28` | 22,020,000.00 USD | 0.00 USD | 1,670.00 USD | `-69.58%` | `1,301.80` |
| `Live` | `Long` | `1.29` | 22,020,000.00 USD | 0.00 USD | 258.35 USD | `-69.34%` | `199.50` |
| `Live` | `Long` | `1.30` | 22,020,000.00 USD | 0.00 USD | 471.63 USD | `-69.11%` | `361.40` |
| `Live` | `Long` | `1.31` | 22,020,000.00 USD | 0.00 USD | 2,810.00 USD | `-68.87%` | `2,134.40` |
| `Live` | `Long` | `1.32` | 22,020,000.00 USD | 0.00 USD | 2,830.00 USD | `-68.63%` | `2,132.40` |
| `Live` | `Long` | `1.34` | 22,010,000.00 USD | 0.00 USD | 5,850.00 USD | `-68.16%` | `4,350.00` |
| `Live` | `Long` | `1.35` | 22,010,000.00 USD | 0.00 USD | 73,140.00 USD | `-67.92%` | `53,978.00` |
| `Live` | `Long` | `1.38` | 21,930,000.00 USD | 0.00 USD | 12,380.00 USD | `-67.45%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 21,920,000.00 USD | 0.00 USD | 295.56 USD | `-67.21%` | `213.40` |
| `Live` | `Long` | `1.40` | 21,920,000.00 USD | 0.00 USD | 931.86 USD | `-66.98%` | `668.00` |
| `Live` | `Long` | `1.41` | 21,920,000.00 USD | 0.00 USD | 1,680.00 USD | `-66.74%` | `1,194.90` |
| `Live` | `Long` | `1.42` | 21,920,000.00 USD | 0.00 USD | 4,710.00 USD | `-66.50%` | `3,325.90` |
| `Live` | `Long` | `1.43` | 21,910,000.00 USD | 0.00 USD | 33,990.00 USD | `-66.27%` | `23,853.80` |
| `Live` | `Long` | `1.44` | 21,880,000.00 USD | 0.00 USD | 17,030.00 USD | `-66.03%` | `11,870.40` |
| `Live` | `Long` | `1.45` | 21,860,000.00 USD | 0.00 USD | 1,530.00 USD | `-65.79%` | `1,061.70` |
| `Live` | `Long` | `1.46` | 21,860,000.00 USD | 0.00 USD | 587,440.00 USD | `-65.56%` | `403,738.20` |
| `Live` | `Long` | `1.47` | 21,270,000.00 USD | 0.00 USD | 512.75 USD | `-65.32%` | `350.00` |
| `Live` | `Long` | `1.48` | 21,270,000.00 USD | 0.00 USD | 1,480.00 USD | `-65.08%` | `1,000.00` |
| `Live` | `Long` | `1.49` | 21,270,000.00 USD | 0.00 USD | 742.50 USD | `-64.85%` | `500.00` |
| `Live` | `Long` | `1.50` | 21,270,000.00 USD | 0.00 USD | 602.00 USD | `-64.37%` | `400.00` |
| `Live` | `Long` | `1.51` | 21,270,000.00 USD | 0.00 USD | 3,980.00 USD | `-64.14%` | `2,627.10` |
| `Live` | `Long` | `1.52` | 21,270,000.00 USD | 0.00 USD | 327.72 USD | `-63.90%` | `214.90` |
| `Live` | `Long` | `1.53` | 21,270,000.00 USD | 0.00 USD | 6,040.00 USD | `-63.66%` | `3,937.60` |
| `Live` | `Long` | `1.55` | 21,260,000.00 USD | 0.00 USD | 311.00 USD | `-63.19%` | `200.00` |
| `Live` | `Long` | `1.56` | 21,260,000.00 USD | 0.00 USD | 32,700.00 USD | `-62.95%` | `20,896.60` |
| `Live` | `Long` | `1.57` | 21,230,000.00 USD | 0.00 USD | 589.52 USD | `-62.72%` | `374.30` |
| `Live` | `Long` | `1.58` | 21,230,000.00 USD | 0.00 USD | 1,980.00 USD | `-62.48%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 21,220,000.00 USD | 0.00 USD | 5,300.00 USD | `-62.24%` | `3,322.80` |
| `Live` | `Long` | `1.60` | 21,220,000.00 USD | 0.00 USD | 12,450.00 USD | `-62.01%` | `7,756.60` |
| `Live` | `Long` | `1.61` | 21,210,000.00 USD | 0.00 USD | 2,330.00 USD | `-61.77%` | `1,442.70` |
| `Live` | `Long` | `1.62` | 21,200,000.00 USD | 0.00 USD | 1,220.00 USD | `-61.53%` | `750.00` |
| `Live` | `Long` | `1.64` | 21,200,000.00 USD | 0.00 USD | 7,460.00 USD | `-61.30%` | `4,564.80` |
| `Live` | `Long` | `1.65` | 21,200,000.00 USD | 0.00 USD | 5,190.00 USD | `-61.06%` | `3,155.00` |
| `Live` | `Long` | `1.66` | 21,190,000.00 USD | 0.00 USD | 113.70 USD | `-60.82%` | `68.70` |
| `Live` | `Long` | `1.67` | 21,190,000.00 USD | 0.00 USD | 683.65 USD | `-60.59%` | `410.60` |
| `Live` | `Long` | `1.68` | 21,190,000.00 USD | 0.00 USD | 5,230.00 USD | `-60.35%` | `3,123.70` |
| `Live` | `Long` | `1.69` | 21,180,000.00 USD | 0.00 USD | 12,850.00 USD | `-60.11%` | `7,624.50` |
| `Live` | `Long` | `1.70` | 21,170,000.00 USD | 0.00 USD | 4,110.00 USD | `-59.88%` | `2,422.20` |
| `Live` | `Long` | `1.71` | 21,170,000.00 USD | 0.00 USD | 3,580.00 USD | `-59.64%` | `2,099.10` |
| `Live` | `Long` | `1.72` | 21,160,000.00 USD | 0.00 USD | 169.96 USD | `-59.40%` | `99.10` |
| `Live` | `Long` | `1.73` | 21,160,000.00 USD | 0.00 USD | 5,460.00 USD | `-59.16%` | `3,164.50` |
| `Live` | `Long` | `1.75` | 21,160,000.00 USD | 0.00 USD | 2,790.00 USD | `-58.69%` | `1,600.00` |
| `Live` | `Long` | `1.75` | 21,160,000.00 USD | 0.00 USD | 10,250.00 USD | `-58.45%` | `5,841.90` |
| `Live` | `Long` | `1.77` | 21,150,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.98%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 21,140,000.00 USD | 0.00 USD | 923.02 USD | `-57.74%` | `517.10` |
| `Live` | `Long` | `1.80` | 21,140,000.00 USD | 0.00 USD | 2,360.00 USD | `-57.27%` | `1,305.50` |
| `Live` | `Long` | `1.81` | 21,140,000.00 USD | 0.00 USD | 1,580.00 USD | `-57.03%` | `873.20` |
| `Live` | `Long` | `1.82` | 21,140,000.00 USD | 0.00 USD | 10,190.00 USD | `-56.80%` | `5,583.80` |
| `Live` | `Long` | `1.83` | 21,130,000.00 USD | 0.00 USD | 28,360.00 USD | `-56.56%` | `15,454.80` |
| `Live` | `Long` | `1.85` | 21,100,000.00 USD | 0.00 USD | 984.26 USD | `-56.09%` | `530.60` |
| `Live` | `Long` | `1.86` | 21,100,000.00 USD | 0.00 USD | 76,780.00 USD | `-55.85%` | `41,168.80` |
| `Live` | `Long` | `1.88` | 21,020,000.00 USD | 0.00 USD | 562,500.00 USD | `-55.61%` | `300,000.60` |
| `Live` | `Long` | `1.89` | 20,460,000.00 USD | 0.00 USD | 1,880.00 USD | `-55.38%` | `995.20` |
| `Live` | `Long` | `1.90` | 20,460,000.00 USD | 0.00 USD | 2,080.00 USD | `-55.14%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 20,450,000.00 USD | 0.00 USD | 416.43 USD | `-54.90%` | `218.60` |
| `Live` | `Long` | `1.92` | 20,450,000.00 USD | 0.00 USD | 979.71 USD | `-54.67%` | `511.60` |
| `Live` | `Long` | `1.93` | 20,450,000.00 USD | 0.00 USD | 2,760.00 USD | `-54.43%` | `1,432.70` |
| `Live` | `Long` | `1.95` | 20,450,000.00 USD | 0.00 USD | 4,110.00 USD | `-53.96%` | `2,114.50` |
| `Live` | `Long` | `1.96` | 20,450,000.00 USD | 0.00 USD | 1,090.00 USD | `-53.72%` | `559.40` |
| `Live` | `Long` | `1.97` | 20,440,000.00 USD | 0.00 USD | 1,590.00 USD | `-53.48%` | `810.90` |
| `Live` | `Long` | `1.98` | 20,440,000.00 USD | 0.00 USD | 34,960.00 USD | `-53.25%` | `17,700.10` |
| `Live` | `Long` | `1.99` | 20,410,000.00 USD | 0.00 USD | 456.55 USD | `-53.01%` | `230.00` |
| `Live` | `Long` | `2.00` | 20,410,000.00 USD | 0.00 USD | 2,000.00 USD | `-52.54%` | `1,000.00` |
| `Live` | `Long` | `2.02` | 20,410,000.00 USD | 0.00 USD | 1,820.00 USD | `-52.30%` | `905.70` |
| `Live` | `Long` | `2.02` | 20,400,000.00 USD | 0.00 USD | 926.64 USD | `-52.06%` | `457.60` |
| `Live` | `Long` | `2.04` | 20,400,000.00 USD | 0.00 USD | 27,560.00 USD | `-51.83%` | `13,541.80` |
| `Live` | `Long` | `2.04` | 20,380,000.00 USD | 0.00 USD | 3,460.00 USD | `-51.59%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 20,370,000.00 USD | 0.00 USD | 411.00 USD | `-51.35%` | `200.00` |
| `Live` | `Long` | `2.06` | 20,370,000.00 USD | 0.00 USD | 6,070.00 USD | `-51.12%` | `2,938.70` |
| `Live` | `Long` | `2.08` | 20,370,000.00 USD | 0.00 USD | 39,990.00 USD | `-50.88%` | `19,273.10` |
| `Live` | `Long` | `2.08` | 20,330,000.00 USD | 0.00 USD | 18,600.00 USD | `-50.64%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 20,310,000.00 USD | 0.00 USD | 2,970.00 USD | `-50.41%` | `1,417.00` |
| `Live` | `Long` | `2.10` | 20,300,000.00 USD | 0.00 USD | 9,390.00 USD | `-50.17%` | `4,458.70` |
| `Live` | `Long` | `2.12` | 20,290,000.00 USD | 0.00 USD | 12,650.00 USD | `-49.93%` | `5,979.50` |
| `Live` | `Long` | `2.12` | 20,280,000.00 USD | 0.00 USD | 64,840.00 USD | `-49.70%` | `30,512.30` |
| `Live` | `Long` | `2.13` | 20,220,000.00 USD | 0.00 USD | 1,540.00 USD | `-49.46%` | `723.50` |
| `Live` | `Long` | `2.15` | 20,220,000.00 USD | 0.00 USD | 92,580.00 USD | `-49.22%` | `43,163.00` |
| `Live` | `Long` | `2.15` | 20,120,000.00 USD | 0.00 USD | 65,640.00 USD | `-48.99%` | `30,460.00` |
| `Live` | `Long` | `2.17` | 20,060,000.00 USD | 0.00 USD | 188,590.00 USD | `-48.75%` | `87,108.00` |
| `Live` | `Long` | `2.17` | 19,870,000.00 USD | 0.00 USD | 292.32 USD | `-48.51%` | `134.40` |
| `Live` | `Long` | `2.19` | 19,870,000.00 USD | 0.00 USD | 8,170.00 USD | `-48.28%` | `3,737.10` |
| `Live` | `Long` | `2.19` | 19,860,000.00 USD | 0.00 USD | 217,960.00 USD | `-48.04%` | `99,299.00` |
| `Live` | `Long` | `2.21` | 19,640,000.00 USD | 0.00 USD | 44,900.00 USD | `-47.80%` | `20,363.90` |
| `Live` | `Long` | `2.21` | 19,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-47.57%` | `542.90` |
| `Live` | `Long` | `2.23` | 19,600,000.00 USD | 0.00 USD | 9,420.00 USD | `-47.33%` | `4,233.70` |
| `Live` | `Long` | `2.23` | 19,590,000.00 USD | 0.00 USD | 2,670.00 USD | `-47.09%` | `1,193.70` |
| `Live` | `Long` | `2.25` | 19,580,000.00 USD | 0.00 USD | 307,460.00 USD | `-46.86%` | `136,955.00` |
| `Live` | `Long` | `2.25` | 19,280,000.00 USD | 0.00 USD | 116,500.00 USD | `-46.62%` | `51,660.80` |
| `Live` | `Long` | `2.27` | 19,160,000.00 USD | 0.00 USD | 339.75 USD | `-46.38%` | `150.00` |
| `Live` | `Long` | `2.27` | 19,160,000.00 USD | 0.00 USD | 380,350.00 USD | `-46.14%` | `167,188.50` |
| `Live` | `Long` | `2.29` | 18,780,000.00 USD | 0.00 USD | 4,090.00 USD | `-45.91%` | `1,790.70` |
| `Live` | `Long` | `2.29` | 18,780,000.00 USD | 0.00 USD | 3,030.00 USD | `-45.67%` | `1,319.00` |
| `Live` | `Long` | `2.31` | 18,770,000.00 USD | 0.00 USD | 11,600.00 USD | `-45.43%` | `5,030.60` |
| `Live` | `Long` | `2.31` | 18,760,000.00 USD | 0.00 USD | 1,970.00 USD | `-45.20%` | `849.40` |
| `Live` | `Long` | `2.33` | 18,760,000.00 USD | 0.00 USD | 4,910.00 USD | `-44.72%` | `2,102.30` |
| `Live` | `Long` | `2.35` | 18,750,000.00 USD | 0.00 USD | 30,900.00 USD | `-44.49%` | `13,175.10` |
| `Live` | `Long` | `2.37` | 18,720,000.00 USD | 0.00 USD | 10,510.00 USD | `-44.01%` | `4,442.70` |
| `Live` | `Long` | `2.38` | 18,710,000.00 USD | 0.00 USD | 42,440.00 USD | `-43.78%` | `17,868.70` |
| `Live` | `Long` | `2.38` | 18,670,000.00 USD | 0.00 USD | 10,940.00 USD | `-43.54%` | `4,586.00` |
| `Live` | `Long` | `2.40` | 18,660,000.00 USD | 0.00 USD | 2,520.00 USD | `-43.30%` | `1,052.50` |
| `Live` | `Long` | `2.40` | 18,660,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-43.07%` | `652,414.60` |
| `Live` | `Long` | `2.42` | 17,090,000.00 USD | 0.00 USD | 185,860.00 USD | `-42.83%` | `76,961.80` |
| `Live` | `Long` | `2.42` | 16,900,000.00 USD | 0.00 USD | 273,510.00 USD | `-42.59%` | `112,788.60` |
| `Live` | `Long` | `2.44` | 16,630,000.00 USD | 0.00 USD | 5,750.00 USD | `-42.36%` | `2,360.90` |
| `Live` | `Long` | `2.44` | 16,620,000.00 USD | 0.00 USD | 3,700.00 USD | `-42.12%` | `1,515.10` |
| `Live` | `Long` | `2.46` | 16,620,000.00 USD | 0.00 USD | 3,010.00 USD | `-41.88%` | `1,227.10` |
| `Live` | `Long` | `2.46` | 16,620,000.00 USD | 0.00 USD | 252,240.00 USD | `-41.65%` | `102,329.10` |
| `Live` | `Long` | `2.48` | 16,360,000.00 USD | 0.00 USD | 796.46 USD | `-41.41%` | `321.80` |
| `Live` | `Long` | `2.48` | 16,360,000.00 USD | 0.00 USD | 2,760.00 USD | `-41.17%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 16,360,000.00 USD | 0.00 USD | 1,110.00 USD | `-40.94%` | `443.10` |
| `Live` | `Long` | `2.50` | 16,360,000.00 USD | 0.00 USD | 6,000.00 USD | `-40.70%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 16,350,000.00 USD | 0.00 USD | 15,360.00 USD | `-40.46%` | `6,108.50` |
| `Live` | `Long` | `2.52` | 16,340,000.00 USD | 0.00 USD | 35,080.00 USD | `-40.23%` | `13,891.20` |
| `Live` | `Long` | `2.54` | 16,300,000.00 USD | 0.00 USD | 395.71 USD | `-39.99%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,300,000.00 USD | 0.00 USD | 105.36 USD | `-39.75%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,300,000.00 USD | 0.00 USD | 26,190.00 USD | `-39.52%` | `10,251.60` |
| `Live` | `Long` | `2.56` | 16,280,000.00 USD | 0.00 USD | 437,910.00 USD | `-39.28%` | `170,724.30` |
| `Live` | `Long` | `2.58` | 15,840,000.00 USD | 0.00 USD | 6,410.00 USD | `-39.04%` | `2,490.00` |
| `Live` | `Long` | `2.58` | 15,830,000.00 USD | 0.00 USD | 905.27 USD | `-38.81%` | `350.20` |
| `Live` | `Long` | `2.60` | 15,830,000.00 USD | 0.00 USD | 82,690.00 USD | `-38.57%` | `31,866.60` |
| `Live` | `Long` | `2.62` | 15,750,000.00 USD | 0.00 USD | 1,190.00 USD | `-38.10%` | `454.70` |
| `Live` | `Long` | `2.62` | 15,750,000.00 USD | 0.00 USD | 18,360.00 USD | `-37.86%` | `6,992.80` |
| `Live` | `Long` | `2.63` | 15,730,000.00 USD | 0.00 USD | 28,300.00 USD | `-37.62%` | `10,738.80` |
| `Live` | `Long` | `2.65` | 15,700,000.00 USD | 0.00 USD | 2,650.00 USD | `-37.39%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 15,700,000.00 USD | 0.00 USD | 16,510.00 USD | `-37.15%` | `6,216.80` |
| `Live` | `Long` | `2.67` | 15,680,000.00 USD | 0.00 USD | 1,920.00 USD | `-36.91%` | `721.80` |
| `Live` | `Long` | `2.67` | 15,680,000.00 USD | 0.00 USD | 90,780.00 USD | `-36.68%` | `33,936.10` |
| `Live` | `Long` | `2.69` | 15,590,000.00 USD | 0.00 USD | 5,130.00 USD | `-36.44%` | `1,911.60` |
| `Live` | `Long` | `2.69` | 15,580,000.00 USD | 0.00 USD | 170,500.00 USD | `-36.20%` | `63,264.00` |
| `Live` | `Long` | `2.71` | 15,410,000.00 USD | 0.00 USD | 435,960.00 USD | `-35.97%` | `161,169.20` |
| `Live` | `Long` | `2.71` | 14,980,000.00 USD | 0.00 USD | 32,590.00 USD | `-35.73%` | `12,003.90` |
| `Live` | `Long` | `2.73` | 14,940,000.00 USD | 0.00 USD | 28,380.00 USD | `-35.49%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 14,920,000.00 USD | 0.00 USD | 2,160.00 USD | `-35.26%` | `791.50` |
| `Live` | `Long` | `2.75` | 14,910,000.00 USD | 0.00 USD | 43,670.00 USD | `-35.02%` | `15,908.60` |
| `Live` | `Long` | `2.75` | 14,870,000.00 USD | 0.00 USD | 25,260.00 USD | `-34.78%` | `9,167.40` |
| `Live` | `Long` | `2.77` | 14,840,000.00 USD | 0.00 USD | 349,980.00 USD | `-34.55%` | `126,574.60` |
| `Live` | `Long` | `2.77` | 14,490,000.00 USD | 0.00 USD | 10,760.00 USD | `-34.31%` | `3,879.10` |
| `Live` | `Long` | `2.79` | 14,480,000.00 USD | 0.00 USD | 50,500.00 USD | `-34.07%` | `18,132.90` |
| `Live` | `Long` | `2.79` | 14,430,000.00 USD | 0.00 USD | 15,730.00 USD | `-33.84%` | `5,629.00` |
| `Live` | `Long` | `2.81` | 14,420,000.00 USD | 0.00 USD | 104,120.00 USD | `-33.60%` | `37,117.80` |
| `Live` | `Long` | `2.81` | 14,310,000.00 USD | 0.00 USD | 33,830.00 USD | `-33.36%` | `12,019.20` |
| `Live` | `Long` | `2.83` | 14,280,000.00 USD | 0.00 USD | 11,060.00 USD | `-33.13%` | `3,915.10` |
| `Live` | `Long` | `2.83` | 14,270,000.00 USD | 0.00 USD | 2,560,000.00 USD | `-32.89%` | `902,338.80` |
| `Live` | `Long` | `2.85` | 11,710,000.00 USD | 0.00 USD | 8,780.00 USD | `-32.65%` | `3,084.70` |
| `Live` | `Long` | `2.85` | 11,700,000.00 USD | 0.00 USD | 3,870.00 USD | `-32.41%` | `1,354.50` |
| `Live` | `Long` | `2.87` | 11,700,000.00 USD | 0.00 USD | 13,160.00 USD | `-32.18%` | `4,593.60` |
| `Live` | `Long` | `2.88` | 11,680,000.00 USD | 0.00 USD | 476,330.00 USD | `-31.94%` | `165,678.40` |
| `Live` | `Long` | `2.88` | 11,210,000.00 USD | 0.00 USD | 8,400.00 USD | `-31.70%` | `2,912.80` |
| `Live` | `Long` | `2.90` | 11,200,000.00 USD | 0.00 USD | 225,540.00 USD | `-31.47%` | `77,907.80` |
| `Live` | `Long` | `2.90` | 10,970,000.00 USD | 0.00 USD | 13,880.00 USD | `-31.23%` | `4,779.10` |
| `Live` | `Long` | `2.92` | 10,960,000.00 USD | 0.00 USD | 84,030.00 USD | `-30.99%` | `28,827.70` |
| `Live` | `Long` | `2.92` | 10,880,000.00 USD | 0.00 USD | 49,800.00 USD | `-30.76%` | `17,024.00` |
| `Live` | `Long` | `2.94` | 10,830,000.00 USD | 0.00 USD | 48,480.00 USD | `-30.52%` | `16,518.20` |
| `Live` | `Long` | `2.94` | 10,780,000.00 USD | 0.00 USD | 17,440.00 USD | `-30.28%` | `5,922.20` |
| `Live` | `Long` | `2.96` | 10,760,000.00 USD | 0.00 USD | 1,450.00 USD | `-30.05%` | `491.50` |
| `Live` | `Long` | `2.96` | 10,760,000.00 USD | 0.00 USD | 160,150.00 USD | `-29.81%` | `54,013.00` |
| `Live` | `Long` | `2.98` | 10,600,000.00 USD | 0.00 USD | 43,620.00 USD | `-29.57%` | `14,661.40` |
| `Live` | `Long` | `2.98` | 10,560,000.00 USD | 0.00 USD | 111,490.00 USD | `-29.34%` | `37,350.40` |
| `Live` | `Long` | `3.00` | 10,440,000.00 USD | 0.00 USD | 18,560.00 USD | `-29.10%` | `6,197.60` |
| `Live` | `Long` | `3.00` | 10,430,000.00 USD | 0.00 USD | 11,020.00 USD | `-28.86%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 10,410,000.00 USD | 0.00 USD | 21,610.00 USD | `-28.63%` | `7,167.60` |
| `Live` | `Long` | `3.02` | 10,390,000.00 USD | 0.00 USD | 20,250.00 USD | `-28.39%` | `6,694.10` |
| `Live` | `Long` | `3.04` | 10,370,000.00 USD | 0.00 USD | 2,540.00 USD | `-28.15%` | `836.50` |
| `Live` | `Long` | `3.04` | 10,370,000.00 USD | 0.00 USD | 171,230.00 USD | `-27.92%` | `56,234.20` |
| `Live` | `Long` | `3.06` | 10,200,000.00 USD | 0.00 USD | 65,890.00 USD | `-27.68%` | `21,568.30` |
| `Live` | `Long` | `3.06` | 10,130,000.00 USD | 0.00 USD | 115,880.00 USD | `-27.44%` | `37,808.40` |
| `Live` | `Long` | `3.08` | 10,020,000.00 USD | 0.00 USD | 45,630.00 USD | `-27.21%` | `14,838.80` |
| `Live` | `Long` | `3.08` | 9,970,000.00 USD | 0.00 USD | 8,010.00 USD | `-26.97%` | `2,595.40` |
| `Live` | `Long` | `3.10` | 9,960,000.00 USD | 0.00 USD | 5,110.00 USD | `-26.73%` | `1,650.90` |
| `Live` | `Long` | `3.10` | 9,960,000.00 USD | 0.00 USD | 100,200.00 USD | `-26.50%` | `32,270.30` |
| `Live` | `Long` | `3.12` | 9,860,000.00 USD | 0.00 USD | 31,130.00 USD | `-26.26%` | `9,992.50` |
| `Live` | `Long` | `3.12` | 9,830,000.00 USD | 0.00 USD | 8,180.00 USD | `-26.02%` | `2,618.00` |
| `Live` | `Long` | `3.13` | 9,820,000.00 USD | 0.00 USD | 13,150.00 USD | `-25.79%` | `4,195.80` |
| `Live` | `Long` | `3.15` | 9,810,000.00 USD | 0.00 USD | 23,850.00 USD | `-25.55%` | `7,583.20` |
| `Live` | `Long` | `3.15` | 9,780,000.00 USD | 0.00 USD | 54,840.00 USD | `-25.31%` | `17,382.00` |
| `Live` | `Long` | `3.17` | 9,730,000.00 USD | 0.00 USD | 38,060.00 USD | `-25.08%` | `12,026.80` |
| `Live` | `Long` | `3.17` | 9,690,000.00 USD | 0.00 USD | 3,820.00 USD | `-24.84%` | `1,204.50` |
| `Live` | `Long` | `3.19` | 9,680,000.00 USD | 0.00 USD | 245,320.00 USD | `-24.60%` | `77,025.00` |
| `Live` | `Long` | `3.19` | 9,440,000.00 USD | 0.00 USD | 6,250.00 USD | `-24.37%` | `1,956.90` |
| `Live` | `Long` | `3.21` | 9,430,000.00 USD | 0.00 USD | 2,290.00 USD | `-24.13%` | `714.20` |
| `Live` | `Long` | `3.21` | 9,430,000.00 USD | 0.00 USD | 33,530.00 USD | `-23.89%` | `10,428.10` |
| `Live` | `Long` | `3.23` | 9,400,000.00 USD | 0.00 USD | 146,260.00 USD | `-23.66%` | `45,350.70` |
| `Live` | `Long` | `3.23` | 9,250,000.00 USD | 0.00 USD | 56,130.00 USD | `-23.42%` | `17,352.20` |
| `Live` | `Long` | `3.25` | 9,190,000.00 USD | 0.00 USD | 19,810.00 USD | `-23.18%` | `6,104.10` |
| `Live` | `Long` | `3.25` | 9,180,000.00 USD | 0.00 USD | 5,640.00 USD | `-22.95%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 9,170,000.00 USD | 0.00 USD | 49,440.00 USD | `-22.71%` | `15,142.80` |
| `Live` | `Long` | `3.27` | 9,120,000.00 USD | 0.00 USD | 868,070.00 USD | `-22.47%` | `265,060.40` |
| `Live` | `Long` | `3.29` | 8,250,000.00 USD | 0.00 USD | 14,120.00 USD | `-22.24%` | `4,298.30` |
| `Live` | `Long` | `3.29` | 8,240,000.00 USD | 0.00 USD | 137,180.00 USD | `-22.00%` | `41,634.00` |
| `Live` | `Long` | `3.31` | 8,100,000.00 USD | 0.00 USD | 132,030.00 USD | `-21.76%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 7,970,000.00 USD | 0.00 USD | 17,060.00 USD | `-21.53%` | `5,145.10` |
| `Live` | `Long` | `3.33` | 7,950,000.00 USD | 0.00 USD | 10,720.00 USD | `-21.29%` | `3,223.90` |
| `Live` | `Long` | `3.33` | 7,940,000.00 USD | 0.00 USD | 73,390.00 USD | `-21.05%` | `22,007.00` |
| `Live` | `Long` | `3.35` | 7,870,000.00 USD | 0.00 USD | 27,090.00 USD | `-20.82%` | `8,097.80` |
| `Live` | `Long` | `3.35` | 7,840,000.00 USD | 0.00 USD | 1,780.00 USD | `-20.58%` | `531.00` |
| `Live` | `Long` | `3.37` | 7,840,000.00 USD | 0.00 USD | 169,280.00 USD | `-20.34%` | `50,305.80` |
| `Live` | `Long` | `3.38` | 7,670,000.00 USD | 0.00 USD | 46,700.00 USD | `-20.11%` | `13,838.50` |
| `Live` | `Long` | `3.38` | 7,620,000.00 USD | 0.00 USD | 44,790.00 USD | `-19.87%` | `13,232.00` |
| `Live` | `Long` | `3.40` | 7,580,000.00 USD | 0.00 USD | 1,230.00 USD | `-19.63%` | `361.70` |
| `Live` | `Long` | `3.40` | 7,580,000.00 USD | 0.00 USD | 98,820.00 USD | `-19.39%` | `29,022.40` |
| `Live` | `Long` | `3.42` | 7,480,000.00 USD | 0.00 USD | 415,990.00 USD | `-19.16%` | `121,813.20` |
| `Live` | `Long` | `3.42` | 7,060,000.00 USD | 0.00 USD | 30,850.00 USD | `-18.92%` | `9,006.60` |
| `Live` | `Long` | `3.44` | 7,030,000.00 USD | 0.00 USD | 32,060.00 USD | `-18.68%` | `9,333.30` |
| `Live` | `Long` | `3.44` | 7,000,000.00 USD | 0.00 USD | 48,230.00 USD | `-18.45%` | `14,000.10` |
| `Live` | `Long` | `3.46` | 6,950,000.00 USD | 0.00 USD | 11,010.00 USD | `-18.21%` | `3,186.10` |
| `Live` | `Long` | `3.46` | 6,940,000.00 USD | 0.00 USD | 16,340.00 USD | `-17.97%` | `4,715.80` |
| `Live` | `Long` | `3.48` | 6,920,000.00 USD | 0.00 USD | 91,230.00 USD | `-17.74%` | `26,252.50` |
| `Live` | `Long` | `3.48` | 6,830,000.00 USD | 0.00 USD | 50,130.00 USD | `-17.50%` | `14,385.40` |
| `Live` | `Long` | `3.50` | 6,780,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-17.26%` | `375,490.60` |
| `Live` | `Long` | `3.50` | 5,470,000.00 USD | 0.00 USD | 34,500.00 USD | `-17.03%` | `9,841.90` |
| `Live` | `Long` | `3.52` | 5,440,000.00 USD | 0.00 USD | 42,030.00 USD | `-16.79%` | `11,956.60` |
| `Live` | `Long` | `3.52` | 5,390,000.00 USD | 0.00 USD | 296,250.00 USD | `-16.55%` | `84,041.80` |
| `Live` | `Long` | `3.54` | 5,100,000.00 USD | 0.00 USD | 209,090.00 USD | `-16.32%` | `59,147.60` |
| `Live` | `Long` | `3.54` | 4,890,000.00 USD | 0.00 USD | 167,840.00 USD | `-16.08%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 4,720,000.00 USD | 0.00 USD | 375,150.00 USD | `-15.84%` | `105,526.80` |
| `Live` | `Long` | `3.56` | 4,340,000.00 USD | 0.00 USD | 22,250.00 USD | `-15.61%` | `6,241.40` |
| `Live` | `Long` | `3.58` | 4,320,000.00 USD | 0.00 USD | 61,150.00 USD | `-15.37%` | `17,104.60` |
| `Live` | `Long` | `3.58` | 4,260,000.00 USD | 0.00 USD | 248,010.00 USD | `-15.13%` | `69,179.50` |
| `Live` | `Long` | `3.60` | 4,010,000.00 USD | 0.00 USD | 23,000.00 USD | `-14.90%` | `6,399.10` |
| `Live` | `Long` | `3.60` | 3,990,000.00 USD | 0.00 USD | 60,200.00 USD | `-14.66%` | `16,699.70` |
| `Live` | `Long` | `3.62` | 3,930,000.00 USD | 0.00 USD | 31,960.00 USD | `-14.42%` | `8,841.80` |
| `Live` | `Long` | `3.62` | 3,900,000.00 USD | 0.00 USD | 123,450.00 USD | `-14.19%` | `34,053.90` |
| `Live` | `Long` | `3.63` | 3,770,000.00 USD | 0.00 USD | 3,960.00 USD | `-13.95%` | `1,089.80` |
| `Live` | `Long` | `3.65` | 3,770,000.00 USD | 0.00 USD | 23,090.00 USD | `-13.71%` | `6,334.30` |
| `Live` | `Long` | `3.65` | 3,750,000.00 USD | 0.00 USD | 15,510.00 USD | `-13.48%` | `4,242.50` |
| `Live` | `Long` | `3.67` | 3,730,000.00 USD | 0.00 USD | 40,280.00 USD | `-13.24%` | `10,989.20` |
| `Live` | `Long` | `3.67` | 3,690,000.00 USD | 0.00 USD | 101,410.00 USD | `-13.00%` | `27,593.60` |
| `Live` | `Long` | `3.69` | 3,590,000.00 USD | 0.00 USD | 183,600.00 USD | `-12.77%` | `49,822.70` |
| `Live` | `Long` | `3.69` | 3,410,000.00 USD | 0.00 USD | 93,270.00 USD | `-12.53%` | `25,241.00` |
| `Live` | `Long` | `3.71` | 3,310,000.00 USD | 0.00 USD | 212,700.00 USD | `-12.29%` | `57,408.40` |
| `Live` | `Long` | `3.71` | 3,100,000.00 USD | 0.00 USD | 72,730.00 USD | `-12.06%` | `19,577.00` |
| `Live` | `Long` | `3.73` | 3,030,000.00 USD | 0.00 USD | 213,580.00 USD | `-11.82%` | `57,336.90` |
| `Live` | `Long` | `3.73` | 2,810,000.00 USD | 0.00 USD | 121,750.00 USD | `-11.58%` | `32,597.20` |
| `Live` | `Long` | `3.75` | 2,690,000.00 USD | 0.00 USD | 40,190.00 USD | `-11.35%` | `10,731.70` |
| `Live` | `Long` | `3.75` | 2,650,000.00 USD | 0.00 USD | 191,910.00 USD | `-11.11%` | `51,107.80` |
| `Live` | `Long` | `3.77` | 2,460,000.00 USD | 0.00 USD | 70,180.00 USD | `-10.87%` | `18,639.00` |
| `Live` | `Long` | `3.77` | 2,390,000.00 USD | 0.00 USD | 61,240.00 USD | `-10.64%` | `16,223.70` |
| `Live` | `Long` | `3.79` | 2,330,000.00 USD | 0.00 USD | 32,110.00 USD | `-10.40%` | `8,484.70` |
| `Live` | `Long` | `3.79` | 2,300,000.00 USD | 0.00 USD | 152,480.00 USD | `-10.16%` | `40,178.10` |
| `Live` | `Long` | `3.81` | 2,140,000.00 USD | 0.00 USD | 456,920.00 USD | `-9.93%` | `120,083.60` |
| `Live` | `Long` | `3.81` | 1,690,000.00 USD | 0.00 USD | 96,110.00 USD | `-9.69%` | `25,191.50` |
| `Live` | `Long` | `3.83` | 1,590,000.00 USD | 0.00 USD | 161,990.00 USD | `-9.45%` | `42,351.30` |
| `Live` | `Long` | `3.83` | 1,430,000.00 USD | 0.00 USD | 185,530.00 USD | `-9.22%` | `48,377.60` |
| `Live` | `Long` | `3.85` | 1,240,000.00 USD | 0.00 USD | 122,450.00 USD | `-8.98%` | `31,847.00` |
| `Live` | `Long` | `3.85` | 1,120,000.00 USD | 0.00 USD | 26,550.00 USD | `-8.74%` | `6,888.30` |
| `Live` | `Long` | `3.87` | 1,100,000.00 USD | 0.00 USD | 164,270.00 USD | `-8.51%` | `42,502.30` |
| `Live` | `Long` | `3.88` | 930,860.00 USD | 0.00 USD | 29,160.00 USD | `-8.27%` | `7,524.90` |
| `Live` | `Long` | `3.88` | 901,700.00 USD | 0.00 USD | 211,110.00 USD | `-8.03%` | `54,340.40` |
| `Live` | `Long` | `3.90` | 690,590.00 USD | 0.00 USD | 98,420.00 USD | `-7.80%` | `25,267.90` |
| `Live` | `Long` | `3.90` | 592,170.00 USD | 0.00 USD | 20,880.00 USD | `-7.56%` | `5,346.20` |
| `Live` | `Long` | `3.92` | 571,300.00 USD | 0.00 USD | 14,270.00 USD | `-7.32%` | `3,646.00` |
| `Live` | `Long` | `3.92` | 557,020.00 USD | 0.00 USD | 7,790.00 USD | `-7.09%` | `1,984.50` |
| `Live` | `Long` | `3.94` | 549,230.00 USD | 0.00 USD | 151,080.00 USD | `-6.85%` | `38,393.50` |
| `Live` | `Long` | `3.94` | 398,150.00 USD | 0.00 USD | 164,860.00 USD | `-6.61%` | `41,790.70` |
| `Live` | `Long` | `3.96` | 233,290.00 USD | 0.00 USD | 31,700.00 USD | `-6.38%` | `8,014.30` |
| `Live` | `Long` | `3.96` | 201,590.00 USD | 0.00 USD | 160,690.00 USD | `-6.14%` | `40,526.90` |
| `Live` | `Long` | `3.98` | 40,900.00 USD | 0.00 USD | 28,360.00 USD | `-5.90%` | `7,135.20` |
| `Live` | `Long` | `3.98` | 12,540.00 USD | 0.00 USD | 4,850.00 USD | `-5.66%` | `1,216.90` |
| `Live` | `Long` | `4.00` | 7,690.00 USD | 0.00 USD | 6,980.00 USD | `-5.19%` | `1,743.80` |
| `Live` | `Long` | `4.12` | 709.01 USD | 0.00 USD | 709.01 USD | `-2.59%` | `172.30` |
| `Live` | `Short` | `4.26` | 5,950.00 USD | 5,950.00 USD | 0.00 USD | `+0.96%` | `1,395.50` |
| `Live` | `Short` | `4.29` | 35,410.00 USD | 29,460.00 USD | 0.00 USD | `+1.44%` | `6,875.70` |
| `Live` | `Short` | `4.29` | 325,620.00 USD | 290,210.00 USD | 0.00 USD | `+1.67%` | `67,568.90` |
| `Live` | `Short` | `4.32` | 354,610.00 USD | 28,990.00 USD | 0.00 USD | `+2.15%` | `6,718.30` |
| `Live` | `Short` | `4.33` | 361,210.00 USD | 6,600.00 USD | 0.00 USD | `+2.38%` | `1,526.60` |
| `Live` | `Short` | `4.33` | 361,750.00 USD | 533.64 USD | 0.00 USD | `+2.62%` | `123.10` |
| `Live` | `Short` | `4.34` | 365,870.00 USD | 4,130.00 USD | 0.00 USD | `+2.86%` | `949.40` |
| `Live` | `Short` | `4.36` | 369,080.00 USD | 3,210.00 USD | 0.00 USD | `+3.09%` | `736.90` |
| `Live` | `Short` | `4.38` | 452,640.00 USD | 83,560.00 USD | 0.00 USD | `+3.57%` | `19,099.00` |
| `Live` | `Short` | `4.38` | 458,730.00 USD | 6,090.00 USD | 0.00 USD | `+3.80%` | `1,389.30` |
| `Live` | `Short` | `4.39` | 652,000.00 USD | 193,270.00 USD | 0.00 USD | `+4.04%` | `43,974.60` |
| `Live` | `Short` | `4.41` | 653,410.00 USD | 1,410.00 USD | 0.00 USD | `+4.28%` | `319.80` |
| `Live` | `Short` | `4.42` | 668,090.00 USD | 14,680.00 USD | 0.00 USD | `+4.51%` | `3,326.00` |
| `Live` | `Short` | `4.42` | 686,500.00 USD | 18,410.00 USD | 0.00 USD | `+4.75%` | `4,160.30` |
| `Live` | `Short` | `4.43` | 686,710.00 USD | 210.22 USD | 0.00 USD | `+4.99%` | `47.40` |
| `Live` | `Short` | `4.45` | 774,630.00 USD | 87,920.00 USD | 0.00 USD | `+5.22%` | `19,779.60` |
| `Live` | `Short` | `4.46` | 776,640.00 USD | 2,000.00 USD | 0.00 USD | `+5.46%` | `449.40` |
| `Live` | `Short` | `4.46` | 776,640.00 USD | 6.70 USD | 0.00 USD | `+5.70%` | `1.50` |
| `Live` | `Short` | `4.50` | 797,180.00 USD | 20,540.00 USD | 0.00 USD | `+6.41%` | `4,569.50` |
| `Live` | `Short` | `4.50` | 797,470.00 USD | 283.81 USD | 0.00 USD | `+6.64%` | `63.00` |
| `Live` | `Short` | `4.51` | 797,860.00 USD | 389.19 USD | 0.00 USD | `+6.88%` | `86.20` |
| `Live` | `Short` | `4.53` | 815,960.00 USD | 18,100.00 USD | 0.00 USD | `+7.12%` | `4,000.00` |
| `Live` | `Short` | `4.54` | 816,210.00 USD | 252.70 USD | 0.00 USD | `+7.59%` | `55.60` |
| `Live` | `Short` | `4.63` | 817,200.00 USD | 990.04 USD | 0.00 USD | `+9.72%` | `213.60` |
| `Live` | `Short` | `4.64` | 817,340.00 USD | 143.07 USD | 0.00 USD | `+9.96%` | `30.80` |
| `Live` | `Short` | `4.66` | 818,100.00 USD | 756.44 USD | 0.00 USD | `+10.20%` | `162.50` |
| `Live` | `Short` | `4.67` | 818,200.00 USD | 101.70 USD | 0.00 USD | `+10.43%` | `21.80` |
| `Live` | `Short` | `4.68` | 969,090.00 USD | 150,890.00 USD | 0.00 USD | `+10.91%` | `32,207.40` |
| `Live` | `Short` | `4.70` | 969,320.00 USD | 230.06 USD | 0.00 USD | `+11.14%` | `49.00` |
| `Live` | `Short` | `4.71` | 976,800.00 USD | 7,480.00 USD | 0.00 USD | `+11.38%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 977,050.00 USD | 250.37 USD | 0.00 USD | `+11.62%` | `53.10` |
| `Live` | `Short` | `4.74` | 989,560.00 USD | 12,500.00 USD | 0.00 USD | `+12.09%` | `2,640.70` |
| `Live` | `Short` | `4.78` | 998,340.00 USD | 8,780.00 USD | 0.00 USD | `+13.04%` | `1,839.40` |
| `Live` | `Short` | `4.79` | 998,480.00 USD | 143.55 USD | 0.00 USD | `+13.27%` | `30.00` |
| `Live` | `Short` | `4.79` | 1,000,000.00 USD | 1,920.00 USD | 0.00 USD | `+13.51%` | `401.10` |
| `Live` | `Short` | `4.82` | 1,000,000.00 USD | 4,090.00 USD | 0.00 USD | `+13.98%` | `849.60` |
| `Live` | `Short` | `4.83` | 1,010,000.00 USD | 1,740.00 USD | 0.00 USD | `+14.22%` | `360.90` |
| `Live` | `Short` | `4.83` | 1,010,000.00 USD | 1,540.00 USD | 0.00 USD | `+14.46%` | `317.90` |
| `Live` | `Short` | `4.84` | 1,020,000.00 USD | 11,220.00 USD | 0.00 USD | `+14.69%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 1,020,000.00 USD | 137.68 USD | 0.00 USD | `+15.17%` | `28.30` |
| `Live` | `Short` | `4.88` | 1,020,000.00 USD | 827.03 USD | 0.00 USD | `+15.64%` | `169.30` |
| `Live` | `Short` | `4.92` | 1,040,000.00 USD | 20,720.00 USD | 0.00 USD | `+16.35%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,040,000.00 USD | 2,100.00 USD | 0.00 USD | `+16.59%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,040,000.00 USD | 157.43 USD | 0.00 USD | `+16.82%` | `31.90` |
| `Live` | `Short` | `4.96` | 1,040,000.00 USD | 488.56 USD | 0.00 USD | `+17.30%` | `98.60` |
| `Live` | `Short` | `4.96` | 1,080,000.00 USD | 36,060.00 USD | 0.00 USD | `+17.53%` | `7,262.50` |
| `Live` | `Short` | `4.97` | 1,180,000.00 USD | 99,370.00 USD | 0.00 USD | `+17.77%` | `19,974.00` |
| `Live` | `Short` | `5.05` | 1,210,000.00 USD | 35,380.00 USD | 0.00 USD | `+19.66%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,220,000.00 USD | 3,420.00 USD | 0.00 USD | `+19.90%` | `675.80` |
| `Live` | `Short` | `5.11` | 1,270,000.00 USD | 57,160.00 USD | 0.00 USD | `+20.85%` | `11,196.20` |
| `Live` | `Short` | `5.12` | 1,280,000.00 USD | 2,560.00 USD | 0.00 USD | `+21.32%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,280,000.00 USD | 751.51 USD | 0.00 USD | `+22.27%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,290,000.00 USD | 15,040.00 USD | 0.00 USD | `+22.98%` | `2,895.50` |
| `Live` | `Short` | `5.22` | 1,370,000.00 USD | 72,110.00 USD | 0.00 USD | `+23.69%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 1,370,000.00 USD | 748.46 USD | 0.00 USD | `+24.16%` | `142.70` |
| `Live` | `Short` | `5.25` | 1,380,000.00 USD | 17,380.00 USD | 0.00 USD | `+24.40%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,390,000.00 USD | 5,610.00 USD | 0.00 USD | `+24.64%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 2,440,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+24.87%` | `200,000.00` |
| `Live` | `Short` | `5.29` | 2,470,000.00 USD | 21,390.00 USD | 0.00 USD | `+25.11%` | `4,047.70` |
| `Live` | `Short` | `5.30` | 2,470,000.00 USD | 524.66 USD | 0.00 USD | `+25.58%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,470,000.00 USD | 147.23 USD | 0.00 USD | `+25.82%` | `27.70` |
| `Live` | `Short` | `5.34` | 2,470,000.00 USD | 1,710.00 USD | 0.00 USD | `+26.53%` | `320.50` |
| `Live` | `Short` | `5.36` | 2,470,000.00 USD | 142.44 USD | 0.00 USD | `+26.77%` | `26.60` |
| `Live` | `Short` | `5.41` | 2,470,000.00 USD | 5,410.00 USD | 0.00 USD | `+27.95%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 2,750,000.00 USD | 276,410.00 USD | 0.00 USD | `+28.66%` | `50,857.00` |
| `Live` | `Short` | `5.46` | 2,790,000.00 USD | 42,690.00 USD | 0.00 USD | `+29.37%` | `7,811.90` |
| `Live` | `Short` | `5.47` | 2,790,000.00 USD | 2,000.00 USD | 0.00 USD | `+29.61%` | `364.70` |
| `Live` | `Short` | `5.50` | 2,860,000.00 USD | 66,470.00 USD | 0.00 USD | `+30.08%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,900,000.00 USD | 38,800.00 USD | 0.00 USD | `+30.55%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 4,550,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+31.03%` | `298,065.70` |
| `Live` | `Short` | `5.57` | 4,560,000.00 USD | 8,670.00 USD | 0.00 USD | `+31.74%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,560,000.00 USD | 697.99 USD | 0.00 USD | `+31.97%` | `125.20` |
| `Live` | `Short` | `5.58` | 4,620,000.00 USD | 62,580.00 USD | 0.00 USD | `+32.21%` | `11,205.20` |
| `Live` | `Short` | `5.59` | 4,620,000.00 USD | 686.51 USD | 0.00 USD | `+32.45%` | `122.70` |
| `Live` | `Short` | `5.64` | 5,060,000.00 USD | 440,450.00 USD | 0.00 USD | `+33.63%` | `78,025.60` |
| `Live` | `Short` | `5.67` | 5,060,000.00 USD | 1,630.00 USD | 0.00 USD | `+34.11%` | `287.30` |
| `Live` | `Short` | `5.67` | 5,060,000.00 USD | 228.70 USD | 0.00 USD | `+34.34%` | `40.30` |
| `Live` | `Short` | `5.68` | 5,090,000.00 USD | 26,090.00 USD | 0.00 USD | `+34.58%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 5,090,000.00 USD | 1,520.00 USD | 0.00 USD | `+34.82%` | `267.40` |
| `Live` | `Short` | `5.71` | 5,090,000.00 USD | 1,770.00 USD | 0.00 USD | `+35.05%` | `310.00` |
| `Live` | `Short` | `5.71` | 5,100,000.00 USD | 2,130.00 USD | 0.00 USD | `+35.29%` | `372.40` |
| `Live` | `Short` | `5.74` | 5,100,000.00 USD | 147.39 USD | 0.00 USD | `+35.76%` | `25.70` |
| `Live` | `Short` | `5.75` | 5,100,000.00 USD | 4,580.00 USD | 0.00 USD | `+36.00%` | `796.90` |
| `Live` | `Short` | `5.75` | 5,100,000.00 USD | 286.02 USD | 0.00 USD | `+36.24%` | `49.70` |
| `Live` | `Short` | `5.78` | 5,100,000.00 USD | 2,710.00 USD | 0.00 USD | `+36.71%` | `468.80` |
| `Live` | `Short` | `5.84` | 5,370,000.00 USD | 270,730.00 USD | 0.00 USD | `+38.37%` | `46,318.00` |
| `Live` | `Short` | `5.86` | 5,380,000.00 USD | 848.39 USD | 0.00 USD | `+38.60%` | `144.90` |
| `Live` | `Short` | `5.88` | 5,380,000.00 USD | 7,150.00 USD | 0.00 USD | `+39.31%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,470,000.00 USD | 88,590.00 USD | 0.00 USD | `+39.55%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,470,000.00 USD | 319.41 USD | 0.00 USD | `+40.02%` | `54.00` |
| `Live` | `Short` | `5.95` | 5,580,000.00 USD | 104,080.00 USD | 0.00 USD | `+40.73%` | `17,506.80` |
| `Live` | `Short` | `6.03` | 5,600,000.00 USD | 23,060.00 USD | 0.00 USD | `+42.63%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 5,920,000.00 USD | 325,240.00 USD | 0.00 USD | `+43.57%` | `53,625.50` |
| `Live` | `Short` | `6.08` | 5,930,000.00 USD | 5,920.00 USD | 0.00 USD | `+44.05%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,970,000.00 USD | 37,510.00 USD | 0.00 USD | `+44.28%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 5,980,000.00 USD | 13,680.00 USD | 0.00 USD | `+44.76%` | `2,237.40` |
| `Live` | `Short` | `6.13` | 6,340,000.00 USD | 357,880.00 USD | 0.00 USD | `+45.23%` | `58,334.50` |
| `Live` | `Short` | `6.21` | 6,360,000.00 USD | 24,100.00 USD | 0.00 USD | `+46.89%` | `3,883.80` |
| `Live` | `Short` | `6.21` | 6,360,000.00 USD | 1,900.00 USD | 0.00 USD | `+47.12%` | `305.00` |
| `Live` | `Short` | `6.24` | 6,890,000.00 USD | 526,230.00 USD | 0.00 USD | `+47.60%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 6,900,000.00 USD | 7,300.00 USD | 0.00 USD | `+47.84%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,900,000.00 USD | 439.10 USD | 0.00 USD | `+48.07%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,900,000.00 USD | 397.84 USD | 0.00 USD | `+48.55%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,900,000.00 USD | 310.70 USD | 0.00 USD | `+49.49%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,900,000.00 USD | 382.00 USD | 0.00 USD | `+49.97%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,900,000.00 USD | 214.46 USD | 0.00 USD | `+50.20%` | `33.80` |
| `Live` | `Short` | `6.36` | 7,160,000.00 USD | 259,720.00 USD | 0.00 USD | `+50.44%` | `40,869.30` |
| `Live` | `Short` | `6.37` | 7,160,000.00 USD | 113.93 USD | 0.00 USD | `+50.68%` | `17.90` |
| `Live` | `Short` | `6.38` | 7,160,000.00 USD | 288.15 USD | 0.00 USD | `+50.91%` | `45.20` |
| `Live` | `Short` | `6.39` | 7,160,000.00 USD | 2,000.00 USD | 0.00 USD | `+51.39%` | `312.80` |
| `Live` | `Short` | `6.41` | 7,170,000.00 USD | 5,780.00 USD | 0.00 USD | `+51.62%` | `902.20` |
| `Live` | `Short` | `6.42` | 7,180,000.00 USD | 8,700.00 USD | 0.00 USD | `+51.86%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 7,180,000.00 USD | 173.47 USD | 0.00 USD | `+52.10%` | `27.00` |
| `Live` | `Short` | `6.45` | 8,390,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+52.57%` | `188,818.40` |
| `Live` | `Short` | `6.46` | 8,400,000.00 USD | 7,150.00 USD | 0.00 USD | `+52.81%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 8,400,000.00 USD | 1,940.00 USD | 0.00 USD | `+53.04%` | `300.00` |
| `Live` | `Short` | `6.51` | 8,400,000.00 USD | 380.48 USD | 0.00 USD | `+54.23%` | `58.40` |
| `Live` | `Short` | `6.54` | 8,440,000.00 USD | 40,780.00 USD | 0.00 USD | `+54.94%` | `6,230.50` |
| `Live` | `Short` | `6.57` | 8,500,000.00 USD | 51,390.00 USD | 0.00 USD | `+55.41%` | `7,827.40` |
| `Live` | `Short` | `6.59` | 8,500,000.00 USD | 6,040.00 USD | 0.00 USD | `+56.12%` | `916.30` |
| `Live` | `Short` | `6.62` | 38,360,000.00 USD | 29,860,000.00 USD | 0.00 USD | `+56.83%` | `4,507,262.50` |
| `Live` | `Short` | `6.66` | 38,370,000.00 USD | 7,230.00 USD | 0.00 USD | `+57.54%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 38,370,000.00 USD | 233.94 USD | 0.00 USD | `+57.78%` | `35.10` |
| `Live` | `Short` | `6.67` | 38,460,000.00 USD | 89,430.00 USD | 0.00 USD | `+58.01%` | `13,397.10` |
| `Live` | `Short` | `6.68` | 38,470,000.00 USD | 9,250.00 USD | 0.00 USD | `+58.25%` | `1,384.00` |
| `Live` | `Short` | `6.72` | 38,510,000.00 USD | 37,370.00 USD | 0.00 USD | `+59.20%` | `5,556.90` |
| `Live` | `Short` | `6.75` | 39,750,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+59.91%` | `184,528.50` |
| `Live` | `Short` | `6.80` | 39,750,000.00 USD | 722.01 USD | 0.00 USD | `+61.09%` | `106.10` |
| `Live` | `Short` | `6.82` | 39,750,000.00 USD | 1,700.00 USD | 0.00 USD | `+61.33%` | `250.00` |
| `Live` | `Short` | `6.84` | 39,760,000.00 USD | 753.63 USD | 0.00 USD | `+62.04%` | `110.10` |
| `Live` | `Short` | `6.87` | 39,760,000.00 USD | 2,650.00 USD | 0.00 USD | `+62.51%` | `386.60` |
| `Live` | `Short` | `6.92` | 39,760,000.00 USD | 6,920.00 USD | 0.00 USD | `+63.93%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 39,770,000.00 USD | 664.27 USD | 0.00 USD | `+65.35%` | `95.10` |
| `Live` | `Short` | `7.03` | 39,770,000.00 USD | 665.27 USD | 0.00 USD | `+66.30%` | `94.70` |
| `Live` | `Short` | `7.05` | 39,770,000.00 USD | 559.46 USD | 0.00 USD | `+67.01%` | `79.30` |
| `Live` | `Short` | `7.09` | 39,770,000.00 USD | 699.57 USD | 0.00 USD | `+67.96%` | `98.60` |
| `Live` | `Short` | `7.12` | 43,550,000.00 USD | 3,780,000.00 USD | 0.00 USD | `+68.67%` | `531,000.00` |
| `Live` | `Short` | `7.13` | 43,550,000.00 USD | 1,000.00 USD | 0.00 USD | `+68.90%` | `140.60` |
| `Live` | `Short` | `7.21` | 43,570,000.00 USD | 13,560.00 USD | 0.00 USD | `+70.80%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 43,570,000.00 USD | 4,910.00 USD | 0.00 USD | `+71.27%` | `679.30` |
| `Live` | `Short` | `7.33` | 43,570,000.00 USD | 767.66 USD | 0.00 USD | `+73.40%` | `104.80` |
| `Live` | `Short` | `7.33` | 43,580,000.00 USD | 4,850.00 USD | 0.00 USD | `+73.64%` | `661.50` |
| `Live` | `Short` | `7.43` | 53,510,000.00 USD | 9,930,000.00 USD | 0.00 USD | `+76.01%` | `1,336,000.00` |
| `Live` | `Short` | `7.45` | 53,620,000.00 USD | 106,290.00 USD | 0.00 USD | `+76.24%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 53,620,000.00 USD | 1,420.00 USD | 0.00 USD | `+76.48%` | `191.10` |
| `Live` | `Short` | `7.46` | 61,380,000.00 USD | 7,760,000.00 USD | 0.00 USD | `+76.72%` | `1,039,604.60` |
| `Live` | `Short` | `7.53` | 61,380,000.00 USD | 1,570.00 USD | 0.00 USD | `+78.14%` | `208.40` |
| `Live` | `Short` | `7.57` | 61,380,000.00 USD | 485.67 USD | 0.00 USD | `+79.08%` | `64.20` |
| `Live` | `Short` | `7.62` | 61,380,000.00 USD | 2,640.00 USD | 0.00 USD | `+80.27%` | `347.20` |
| `Live` | `Short` | `7.62` | 61,390,000.00 USD | 11,550.00 USD | 0.00 USD | `+80.50%` | `1,514.20` |
| `Live` | `Short` | `7.63` | 61,410,000.00 USD | 19,210.00 USD | 0.00 USD | `+80.74%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 61,440,000.00 USD | 26,080.00 USD | 0.00 USD | `+81.21%` | `3,407.20` |
| `Live` | `Short` | `7.67` | 61,440,000.00 USD | 676.82 USD | 0.00 USD | `+81.45%` | `88.30` |
| `Live` | `Short` | `7.68` | 61,500,000.00 USD | 61,480.00 USD | 0.00 USD | `+81.92%` | `8,000.00` |
| `Live` | `Short` | `7.72` | 61,510,000.00 USD | 13,780.00 USD | 0.00 USD | `+82.87%` | `1,783.60` |
| `Live` | `Short` | `7.74` | 61,520,000.00 USD | 505.87 USD | 0.00 USD | `+83.11%` | `65.40` |
| `Live` | `Short` | `7.75` | 61,580,000.00 USD | 63,970.00 USD | 0.00 USD | `+83.34%` | `8,259.90` |
| `Live` | `Short` | `7.79` | 61,610,000.00 USD | 33,540.00 USD | 0.00 USD | `+84.29%` | `4,308.50` |
| `Live` | `Short` | `7.82` | 61,710,000.00 USD | 93,780.00 USD | 0.00 USD | `+85.00%` | `12,000.00` |
| `Live` | `Short` | `7.87` | 61,710,000.00 USD | 2,980.00 USD | 0.00 USD | `+86.18%` | `378.70` |
| `Live` | `Short` | `7.89` | 61,710,000.00 USD | 1,670.00 USD | 0.00 USD | `+86.89%` | `211.30` |
| `Live` | `Short` | `7.95` | 61,720,000.00 USD | 6,120.00 USD | 0.00 USD | `+88.08%` | `769.80` |
| `Live` | `Short` | `7.96` | 61,720,000.00 USD | 166.47 USD | 0.00 USD | `+88.55%` | `20.90` |
| `Live` | `Short` | `7.99` | 61,720,000.00 USD | 399.25 USD | 0.00 USD | `+89.03%` | `50.00` |
| `Live` | `Short` | `8.03` | 62,150,000.00 USD | 435,420.00 USD | 0.00 USD | `+89.97%` | `54,257.40` |
| `Live` | `Short` | `8.37` | 63,250,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+98.02%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 63,250,000.00 USD | 191.79 USD | 0.00 USD | `+98.26%` | `22.90` |
| `Live` | `Short` | `8.45` | 63,330,000.00 USD | 76,000.00 USD | 0.00 USD | `+99.91%` | `9,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,440,000.00 USD | 0.00 USD | 585.51 USD | `-76.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,440,000.00 USD | 0.00 USD | 339.82 USD | `-75.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,440,000.00 USD | 0.00 USD | 196.58 USD | `-71.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,430,000.00 USD | 0.00 USD | 331.54 USD | `-68.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,430,000.00 USD | 0.00 USD | 345.25 USD | `-67.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,430,000.00 USD | 0.00 USD | 5,640.00 USD | `-67.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,430,000.00 USD | 0.00 USD | 997.29 USD | `-66.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,430,000.00 USD | 0.00 USD | 741.29 USD | `-64.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,430,000.00 USD | 0.00 USD | 113.28 USD | `-63.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,430,000.00 USD | 0.00 USD | 4,000.00 USD | `-63.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,420,000.00 USD | 0.00 USD | 324.22 USD | `-63.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,420,000.00 USD | 0.00 USD | 4,590.00 USD | `-62.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,420,000.00 USD | 0.00 USD | 739.67 USD | `-61.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,420,000.00 USD | 0.00 USD | 1,740.00 USD | `-61.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,420,000.00 USD | 0.00 USD | 6,260.00 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,410,000.00 USD | 0.00 USD | 345.40 USD | `-60.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,410,000.00 USD | 0.00 USD | 167.50 USD | `-60.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,410,000.00 USD | 0.00 USD | 669.02 USD | `-59.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,410,000.00 USD | 0.00 USD | 105.88 USD | `-59.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,410,000.00 USD | 0.00 USD | 172.50 USD | `-59.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,410,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,400,000.00 USD | 0.00 USD | 722.00 USD | `-57.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,400,000.00 USD | 0.00 USD | 259.00 USD | `-57.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,400,000.00 USD | 0.00 USD | 103.84 USD | `-56.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,400,000.00 USD | 0.00 USD | 109.00 USD | `-56.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,400,000.00 USD | 0.00 USD | 222.19 USD | `-55.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,400,000.00 USD | 0.00 USD | 10,280.00 USD | `-55.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,390,000.00 USD | 0.00 USD | 558.36 USD | `-54.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,380,000.00 USD | 0.00 USD | 1,520.00 USD | `-54.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,380,000.00 USD | 0.00 USD | 222.14 USD | `-54.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,380,000.00 USD | 0.00 USD | 279.50 USD | `-53.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,380,000.00 USD | 0.00 USD | 197.50 USD | `-53.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,380,000.00 USD | 0.00 USD | 935.66 USD | `-52.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,380,000.00 USD | 0.00 USD | 18,860.00 USD | `-52.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,360,000.00 USD | 0.00 USD | 3,020.00 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,360,000.00 USD | 0.00 USD | 214.52 USD | `-51.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,360,000.00 USD | 0.00 USD | 1,200.00 USD | `-51.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,360,000.00 USD | 0.00 USD | 578.41 USD | `-51.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,360,000.00 USD | 0.00 USD | 18,070.00 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,340,000.00 USD | 0.00 USD | 108.62 USD | `-50.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,340,000.00 USD | 0.00 USD | 107.23 USD | `-49.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,340,000.00 USD | 0.00 USD | 1,590.00 USD | `-49.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,340,000.00 USD | 0.00 USD | 5,830.00 USD | `-49.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,330,000.00 USD | 0.00 USD | 310.32 USD | `-48.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,330,000.00 USD | 0.00 USD | 1,170.00 USD | `-48.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,330,000.00 USD | 0.00 USD | 576.18 USD | `-48.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,330,000.00 USD | 0.00 USD | 295.67 USD | `-48.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,330,000.00 USD | 0.00 USD | 1,430.00 USD | `-47.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,330,000.00 USD | 0.00 USD | 812.68 USD | `-47.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,330,000.00 USD | 0.00 USD | 1,440.00 USD | `-47.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,330,000.00 USD | 0.00 USD | 106.16 USD | `-47.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,330,000.00 USD | 0.00 USD | 6,270.00 USD | `-46.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,320,000.00 USD | 0.00 USD | 478.06 USD | `-46.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,320,000.00 USD | 0.00 USD | 540.88 USD | `-46.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,320,000.00 USD | 0.00 USD | 867.46 USD | `-46.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,320,000.00 USD | 0.00 USD | 759.76 USD | `-45.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,320,000.00 USD | 0.00 USD | 11,060.00 USD | `-45.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,310,000.00 USD | 0.00 USD | 3,690.00 USD | `-45.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,300,000.00 USD | 0.00 USD | 722.15 USD | `-44.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,300,000.00 USD | 0.00 USD | 467.00 USD | `-44.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,300,000.00 USD | 0.00 USD | 506.75 USD | `-44.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,300,000.00 USD | 0.00 USD | 214.27 USD | `-44.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,300,000.00 USD | 0.00 USD | 428.69 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,300,000.00 USD | 0.00 USD | 322.45 USD | `-43.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,300,000.00 USD | 0.00 USD | 108.25 USD | `-43.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,300,000.00 USD | 0.00 USD | 3,900.00 USD | `-43.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,300,000.00 USD | 0.00 USD | 799.04 USD | `-42.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,290,000.00 USD | 0.00 USD | 6,830.00 USD | `-42.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,290,000.00 USD | 0.00 USD | 137.16 USD | `-42.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,290,000.00 USD | 0.00 USD | 504.41 USD | `-41.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,290,000.00 USD | 0.00 USD | 963.93 USD | `-41.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,290,000.00 USD | 0.00 USD | 6,690.00 USD | `-40.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,280,000.00 USD | 0.00 USD | 541.98 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,280,000.00 USD | 0.00 USD | 108.75 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,280,000.00 USD | 0.00 USD | 766.55 USD | `-39.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,280,000.00 USD | 0.00 USD | 7,110.00 USD | `-39.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,270,000.00 USD | 0.00 USD | 1,100.00 USD | `-39.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,270,000.00 USD | 0.00 USD | 100.04 USD | `-38.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 3,270,000.00 USD | 0.00 USD | 1,220.00 USD | `-38.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,270,000.00 USD | 0.00 USD | 5,090.00 USD | `-38.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,260,000.00 USD | 0.00 USD | 226.57 USD | `-36.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,260,000.00 USD | 0.00 USD | 104.98 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,260,000.00 USD | 0.00 USD | 889.89 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,260,000.00 USD | 0.00 USD | 7,270.00 USD | `-35.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,260,000.00 USD | 0.00 USD | 107.21 USD | `-35.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,250,000.00 USD | 0.00 USD | 197.37 USD | `-35.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,250,000.00 USD | 0.00 USD | 8,110.00 USD | `-34.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,250,000.00 USD | 0.00 USD | 108.39 USD | `-34.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,250,000.00 USD | 0.00 USD | 435.95 USD | `-34.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,250,000.00 USD | 0.00 USD | 217.23 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,250,000.00 USD | 0.00 USD | 437.98 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,250,000.00 USD | 0.00 USD | 2,720.00 USD | `-33.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,240,000.00 USD | 0.00 USD | 8,380.00 USD | `-33.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,230,000.00 USD | 0.00 USD | 283.50 USD | `-32.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,230,000.00 USD | 0.00 USD | 109.53 USD | `-32.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,230,000.00 USD | 0.00 USD | 1,230.00 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,230,000.00 USD | 0.00 USD | 1,960.00 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,230,000.00 USD | 0.00 USD | 157.81 USD | `-31.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,230,000.00 USD | 0.00 USD | 2,900.00 USD | `-31.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,230,000.00 USD | 0.00 USD | 4,870.00 USD | `-31.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,220,000.00 USD | 0.00 USD | 1,320.00 USD | `-30.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,220,000.00 USD | 0.00 USD | 358.90 USD | `-30.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,220,000.00 USD | 0.00 USD | 15,370.00 USD | `-30.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,210,000.00 USD | 0.00 USD | 738.75 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,210,000.00 USD | 0.00 USD | 523.32 USD | `-29.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,200,000.00 USD | 0.00 USD | 4,470.00 USD | `-29.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,200,000.00 USD | 0.00 USD | 22,950.00 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,180,000.00 USD | 0.00 USD | 1,020.00 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,180,000.00 USD | 0.00 USD | 214.57 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,180,000.00 USD | 0.00 USD | 249.08 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,180,000.00 USD | 0.00 USD | 305.50 USD | `-27.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,180,000.00 USD | 0.00 USD | 109.42 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,180,000.00 USD | 0.00 USD | 9,300.00 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,170,000.00 USD | 0.00 USD | 8,570.00 USD | `-26.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 3,160,000.00 USD | 0.00 USD | 104.69 USD | `-26.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 3,160,000.00 USD | 0.00 USD | 315.69 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,160,000.00 USD | 0.00 USD | 17,510.00 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 3,140,000.00 USD | 0.00 USD | 269,150.00 USD | `-25.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,870,000.00 USD | 0.00 USD | 4,210.00 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,870,000.00 USD | 0.00 USD | 1,030.00 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,860,000.00 USD | 0.00 USD | 218.81 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,860,000.00 USD | 0.00 USD | 24,840.00 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,840,000.00 USD | 0.00 USD | 144.67 USD | `-23.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,840,000.00 USD | 0.00 USD | 27,380.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,810,000.00 USD | 0.00 USD | 1,670.00 USD | `-22.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,810,000.00 USD | 0.00 USD | 104.81 USD | `-22.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,810,000.00 USD | 0.00 USD | 200.10 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,810,000.00 USD | 0.00 USD | 1,480.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,810,000.00 USD | 0.00 USD | 1,870.00 USD | `-22.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,810,000.00 USD | 0.00 USD | 18,240.00 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,790,000.00 USD | 0.00 USD | 240.67 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,790,000.00 USD | 0.00 USD | 306.56 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,790,000.00 USD | 0.00 USD | 6,590.00 USD | `-21.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,780,000.00 USD | 0.00 USD | 505.76 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,780,000.00 USD | 0.00 USD | 73,220.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,710,000.00 USD | 0.00 USD | 19,600.00 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,690,000.00 USD | 0.00 USD | 8,490.00 USD | `-19.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,680,000.00 USD | 0.00 USD | 111,650.00 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,570,000.00 USD | 0.00 USD | 421.41 USD | `-19.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,570,000.00 USD | 0.00 USD | 506.22 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,570,000.00 USD | 0.00 USD | 171.75 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,570,000.00 USD | 0.00 USD | 2,550.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,560,000.00 USD | 0.00 USD | 1,380.00 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,560,000.00 USD | 0.00 USD | 344.07 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,560,000.00 USD | 0.00 USD | 24,320.00 USD | `-17.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,540,000.00 USD | 0.00 USD | 156.83 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,540,000.00 USD | 0.00 USD | 894.72 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,540,000.00 USD | 0.00 USD | 67,780.00 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,470,000.00 USD | 0.00 USD | 21,320.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,450,000.00 USD | 0.00 USD | 3,700.00 USD | `-16.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,440,000.00 USD | 0.00 USD | 17,230.00 USD | `-16.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,430,000.00 USD | 0.00 USD | 5,130.00 USD | `-16.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,420,000.00 USD | 0.00 USD | 17,420.00 USD | `-15.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,400,000.00 USD | 0.00 USD | 18,440.00 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,390,000.00 USD | 0.00 USD | 78,170.00 USD | `-15.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,310,000.00 USD | 0.00 USD | 1,250.00 USD | `-15.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,310,000.00 USD | 0.00 USD | 331.46 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,310,000.00 USD | 0.00 USD | 16,250.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,290,000.00 USD | 0.00 USD | 632.99 USD | `-14.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,290,000.00 USD | 0.00 USD | 172.19 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,290,000.00 USD | 0.00 USD | 1,210.00 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,290,000.00 USD | 0.00 USD | 179.33 USD | `-13.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,290,000.00 USD | 0.00 USD | 4,080.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,280,000.00 USD | 0.00 USD | 4,070.00 USD | `-13.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,280,000.00 USD | 0.00 USD | 367.50 USD | `-13.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,280,000.00 USD | 0.00 USD | 34,850.00 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,240,000.00 USD | 0.00 USD | 4,370.00 USD | `-12.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,240,000.00 USD | 0.00 USD | 234,410.00 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,010,000.00 USD | 0.00 USD | 6,300.00 USD | `-12.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,000,000.00 USD | 0.00 USD | 2,490.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,000,000.00 USD | 0.00 USD | 32,040.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,970,000.00 USD | 0.00 USD | 28,820.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,940,000.00 USD | 0.00 USD | 14,490.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,920,000.00 USD | 0.00 USD | 257,990.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,660,000.00 USD | 0.00 USD | 1,510.00 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,660,000.00 USD | 0.00 USD | 1,660.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,660,000.00 USD | 0.00 USD | 181,010.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,480,000.00 USD | 0.00 USD | 7,500.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,470,000.00 USD | 0.00 USD | 22,340.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,450,000.00 USD | 0.00 USD | 36,060.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,410,000.00 USD | 0.00 USD | 41,340.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,370,000.00 USD | 0.00 USD | 43,060.00 USD | `-8.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,330,000.00 USD | 0.00 USD | 7,710.00 USD | `-8.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,320,000.00 USD | 0.00 USD | 8,620.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,310,000.00 USD | 0.00 USD | 161,080.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,150,000.00 USD | 0.00 USD | 57,280.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,090,000.00 USD | 0.00 USD | 12,210.00 USD | `-7.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,080,000.00 USD | 0.00 USD | 46,290.00 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,040,000.00 USD | 0.00 USD | 2,340.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,030,000.00 USD | 0.00 USD | 5,190.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,030,000.00 USD | 0.00 USD | 934.17 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,030,000.00 USD | 0.00 USD | 3,510.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,020,000.00 USD | 0.00 USD | 5,800.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,020,000.00 USD | 0.00 USD | 37,740.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 980,790.00 USD | 0.00 USD | 317.60 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 980,470.00 USD | 0.00 USD | 3,960.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 976,500.00 USD | 0.00 USD | 993.16 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 975,510.00 USD | 0.00 USD | 201,270.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 774,240.00 USD | 0.00 USD | 20,520.00 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 753,720.00 USD | 0.00 USD | 9,590.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 744,130.00 USD | 0.00 USD | 1,470.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 742,660.00 USD | 0.00 USD | 16,870.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 725,790.00 USD | 0.00 USD | 62,450.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 663,340.00 USD | 0.00 USD | 113.41 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 663,230.00 USD | 0.00 USD | 1,290.00 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 661,940.00 USD | 0.00 USD | 5,360.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 656,570.00 USD | 0.00 USD | 34,290.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 622,280.00 USD | 0.00 USD | 410.91 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 621,870.00 USD | 0.00 USD | 1,710.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 620,160.00 USD | 0.00 USD | 46,570.00 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 573,590.00 USD | 0.00 USD | 1,120.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 572,470.00 USD | 0.00 USD | 3,280.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 569,190.00 USD | 0.00 USD | 1,730.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 567,460.00 USD | 0.00 USD | 84,840.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 482,630.00 USD | 0.00 USD | 2,700.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 479,930.00 USD | 0.00 USD | 92,060.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 387,870.00 USD | 0.00 USD | 371,990.00 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 15,870.00 USD | 0.00 USD | 15,080.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 791.58 USD | 0.00 USD | 791.58 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 1,130.00 USD | 1,130.00 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 175,700.00 USD | 174,570.00 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 180,890.00 USD | 5,190.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 215,340.00 USD | 34,450.00 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 217,740.00 USD | 2,390.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 240,970.00 USD | 23,230.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 279,620.00 USD | 38,650.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 314,070.00 USD | 34,450.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 341,180.00 USD | 27,110.00 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 341,450.00 USD | 269.26 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 343,870.00 USD | 2,420.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 345,410.00 USD | 1,540.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 362,790.00 USD | 17,380.00 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 363,010.00 USD | 222.11 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 519,550.00 USD | 156,540.00 USD | 0.00 USD | `+3.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 561,630.00 USD | 42,080.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 563,250.00 USD | 1,620.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 605,560.00 USD | 42,310.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 1,020,000.00 USD | 411,780.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,030,000.00 USD | 12,210.00 USD | 0.00 USD | `+4.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,030,000.00 USD | 4,090.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 1,030,000.00 USD | 543.29 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 1,030,000.00 USD | 524.07 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,110,000.00 USD | 71,220.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,110,000.00 USD | 2,470.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 1,110,000.00 USD | 1,700.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,110,000.00 USD | 1,310.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,140,000.00 USD | 29,550.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,160,000.00 USD | 20,340.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,170,000.00 USD | 13,100.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,230,000.00 USD | 52,300.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,230,000.00 USD | 200.45 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,230,000.00 USD | 1,990.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,230,000.00 USD | 1,190.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,230,000.00 USD | 227.79 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,230,000.00 USD | 2,030.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,230,000.00 USD | 1,470.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,290,000.00 USD | 52,450.00 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,310,000.00 USD | 27,250.00 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,310,000.00 USD | 289.82 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,330,000.00 USD | 20,960.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,340,000.00 USD | 1,100.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,340,000.00 USD | 7,380.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,390,000.00 USD | 44,520.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,400,000.00 USD | 16,750.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,410,000.00 USD | 617.10 USD | 0.00 USD | `+10.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,420,000.00 USD | 15,710.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,420,000.00 USD | 152.12 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,780,000.00 USD | 357,870.00 USD | 0.00 USD | `+11.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,000,000.00 USD | 218,120.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,000,000.00 USD | 2,650.00 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,080,000.00 USD | 84,180.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,090,000.00 USD | 8,450.00 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,120,000.00 USD | 27,130.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,130,000.00 USD | 13,030.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,140,000.00 USD | 2,640.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,880,000.00 USD | 749,110.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,880,000.00 USD | 559.58 USD | 0.00 USD | `+13.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,060,000.00 USD | 176,880.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,100,000.00 USD | 33,510.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,100,000.00 USD | 8,540.00 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,100,000.00 USD | 283.33 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,120,000.00 USD | 11,760.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,140,000.00 USD | 24,370.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,150,000.00 USD | 10,460.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,160,000.00 USD | 10,400.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,180,000.00 USD | 19,890.00 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,180,000.00 USD | 4,060.00 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,300,000.00 USD | 120,030.00 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,310,000.00 USD | 156.30 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,320,000.00 USD | 13,180.00 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,320,000.00 USD | 4,420.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,320,000.00 USD | 313.51 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,330,000.00 USD | 5,070.00 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,380,000.00 USD | 47,350.00 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,380,000.00 USD | 187.06 USD | 0.00 USD | `+17.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,470,000.00 USD | 92,570.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,470,000.00 USD | 2,540.00 USD | 0.00 USD | `+18.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,510,000.00 USD | 40,150.00 USD | 0.00 USD | `+18.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,540,000.00 USD | 25,080.00 USD | 0.00 USD | `+18.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,540,000.00 USD | 5,030.00 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,560,000.00 USD | 19,640.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,560,000.00 USD | 120.58 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,580,000.00 USD | 14,690.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,580,000.00 USD | 6,090.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,670,000.00 USD | 87,290.00 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,670,000.00 USD | 5,640.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,670,000.00 USD | 178.33 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,740,000.00 USD | 68,210.00 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,760,000.00 USD | 15,350.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,760,000.00 USD | 179.38 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,760,000.00 USD | 179.72 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,760,000.00 USD | 217.63 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,760,000.00 USD | 493.85 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,760,000.00 USD | 575.38 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,760,000.00 USD | 327.58 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,760,000.00 USD | 163.85 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 3,880,000.00 USD | 120,930.00 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,920,000.00 USD | 38,410.00 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,920,000.00 USD | 1,710.00 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 3,920,000.00 USD | 432.63 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 3,920,000.00 USD | 2,620.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 3,920,000.00 USD | 537.61 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,350,000.00 USD | 420,400.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,350,000.00 USD | 278.52 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,350,000.00 USD | 589.22 USD | 0.00 USD | `+24.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,350,000.00 USD | 733.03 USD | 0.00 USD | `+25.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,350,000.00 USD | 423.60 USD | 0.00 USD | `+25.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,360,000.00 USD | 10,930.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,360,000.00 USD | 381.09 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,360,000.00 USD | 961.16 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,360,000.00 USD | 1,570.00 USD | 0.00 USD | `+26.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,370,000.00 USD | 5,650.00 USD | 0.00 USD | `+26.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,370,000.00 USD | 160.11 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,370,000.00 USD | 225.33 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,370,000.00 USD | 438.60 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,370,000.00 USD | 6,800.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,420,000.00 USD | 40,880.00 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,440,000.00 USD | 19,950.00 USD | 0.00 USD | `+27.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,440,000.00 USD | 270.75 USD | 0.00 USD | `+28.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,440,000.00 USD | 639.61 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,440,000.00 USD | 1,710.00 USD | 0.00 USD | `+28.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,450,000.00 USD | 12,600.00 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,450,000.00 USD | 1,020.00 USD | 0.00 USD | `+29.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,640,000.00 USD | 192,640.00 USD | 0.00 USD | `+29.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,670,000.00 USD | 30,110.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,710,000.00 USD | 38,920.00 USD | 0.00 USD | `+29.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,710,000.00 USD | 1,180.00 USD | 0.00 USD | `+30.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,680,000.00 USD | 968,550.00 USD | 0.00 USD | `+30.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,690,000.00 USD | 5,600.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,710,000.00 USD | 19,110.00 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,730,000.00 USD | 18,790.00 USD | 0.00 USD | `+31.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,780,000.00 USD | 58,030.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,830,000.00 USD | 46,110.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,840,000.00 USD | 14,320.00 USD | 0.00 USD | `+31.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,860,000.00 USD | 11,740.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,880,000.00 USD | 20,540.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,880,000.00 USD | 384.94 USD | 0.00 USD | `+32.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,880,000.00 USD | 573.39 USD | 0.00 USD | `+32.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,880,000.00 USD | 347.06 USD | 0.00 USD | `+33.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,880,000.00 USD | 491.11 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,880,000.00 USD | 3,290.00 USD | 0.00 USD | `+33.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,880,000.00 USD | 281.55 USD | 0.00 USD | `+34.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,890,000.00 USD | 6,590.00 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,890,000.00 USD | 586.69 USD | 0.00 USD | `+34.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,900,000.00 USD | 5,860.00 USD | 0.00 USD | `+34.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,000,000.00 USD | 103,470.00 USD | 0.00 USD | `+35.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,000,000.00 USD | 705.23 USD | 0.00 USD | `+35.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,010,000.00 USD | 5,720.00 USD | 0.00 USD | `+35.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,010,000.00 USD | 139.03 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,010,000.00 USD | 2,450.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,010,000.00 USD | 1,850.00 USD | 0.00 USD | `+36.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,010,000.00 USD | 286.94 USD | 0.00 USD | `+36.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,020,000.00 USD | 7,120.00 USD | 0.00 USD | `+37.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,020,000.00 USD | 329.13 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,020,000.00 USD | 1,970.00 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,020,000.00 USD | 1,150.00 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,020,000.00 USD | 1,190.00 USD | 0.00 USD | `+38.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,020,000.00 USD | 1,770.00 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,030,000.00 USD | 3,450.00 USD | 0.00 USD | `+39.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,030,000.00 USD | 345.45 USD | 0.00 USD | `+39.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,110,000.00 USD | 81,630.00 USD | 0.00 USD | `+39.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,110,000.00 USD | 2,510.00 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,110,000.00 USD | 1,020.00 USD | 0.00 USD | `+40.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,270,000.00 USD | 153,150.00 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,290,000.00 USD | 26,180.00 USD | 0.00 USD | `+40.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,300,000.00 USD | 5,440.00 USD | 0.00 USD | `+41.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,310,000.00 USD | 8,940.00 USD | 0.00 USD | `+41.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,430,000.00 USD | 119,340.00 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,430,000.00 USD | 3,000.00 USD | 0.00 USD | `+41.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,630,000.00 USD | 201,800.00 USD | 0.00 USD | `+42.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,650,000.00 USD | 13,710.00 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,740,000.00 USD | 90,380.00 USD | 0.00 USD | `+42.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,740,000.00 USD | 2,170.00 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,740,000.00 USD | 3,300.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,740,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,740,000.00 USD | 425.76 USD | 0.00 USD | `+43.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,740,000.00 USD | 2,030.00 USD | 0.00 USD | `+43.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,750,000.00 USD | 4,120.00 USD | 0.00 USD | `+44.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 6,750,000.00 USD | 2,000.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,810,000.00 USD | 61,050.00 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,810,000.00 USD | 1,610.00 USD | 0.00 USD | `+44.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,810,000.00 USD | 1,200.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,810,000.00 USD | 420.32 USD | 0.00 USD | `+45.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,820,000.00 USD | 1,940.00 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,820,000.00 USD | 4,010.00 USD | 0.00 USD | `+46.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 6,820,000.00 USD | 3,960.00 USD | 0.00 USD | `+46.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,890,000.00 USD | 66,060.00 USD | 0.00 USD | `+46.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,890,000.00 USD | 1,890.00 USD | 0.00 USD | `+47.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,890,000.00 USD | 195.46 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,890,000.00 USD | 289.93 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,890,000.00 USD | 116.16 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,900,000.00 USD | 7,310.00 USD | 0.00 USD | `+49.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,900,000.00 USD | 310.70 USD | 0.00 USD | `+49.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,900,000.00 USD | 325.62 USD | 0.00 USD | `+49.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,900,000.00 USD | 1,760.00 USD | 0.00 USD | `+50.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,910,000.00 USD | 3,230.00 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,910,000.00 USD | 5,120.00 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,910,000.00 USD | 1,310.00 USD | 0.00 USD | `+53.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,940,000.00 USD | 30,990.00 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,940,000.00 USD | 104.24 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,960,000.00 USD | 13,580.00 USD | 0.00 USD | `+54.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,960,000.00 USD | 1,630.00 USD | 0.00 USD | `+55.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+56.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,970,000.00 USD | 5,400.00 USD | 0.00 USD | `+56.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,970,000.00 USD | 1,620.00 USD | 0.00 USD | `+56.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 6,970,000.00 USD | 3,220.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,970,000.00 USD | 450.55 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,970,000.00 USD | 3,060.00 USD | 0.00 USD | `+58.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,980,000.00 USD | 3,070.00 USD | 0.00 USD | `+58.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 6,980,000.00 USD | 3,120.00 USD | 0.00 USD | `+59.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,980,000.00 USD | 1,550.00 USD | 0.00 USD | `+59.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 6,990,000.00 USD | 3,080.00 USD | 0.00 USD | `+60.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,990,000.00 USD | 647.56 USD | 0.00 USD | `+60.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,990,000.00 USD | 1,420.00 USD | 0.00 USD | `+61.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,990,000.00 USD | 2,130.00 USD | 0.00 USD | `+61.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,000,000.00 USD | 6,870.00 USD | 0.00 USD | `+61.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,000,000.00 USD | 342.25 USD | 0.00 USD | `+62.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,000,000.00 USD | 2,990.00 USD | 0.00 USD | `+62.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,000,000.00 USD | 2,970.00 USD | 0.00 USD | `+63.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,000,000.00 USD | 324.54 USD | 0.00 USD | `+63.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,000,000.00 USD | 504.21 USD | 0.00 USD | `+64.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,000,000.00 USD | 166.00 USD | 0.00 USD | `+65.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,010,000.00 USD | 4,190.00 USD | 0.00 USD | `+65.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,020,000.00 USD | 12,970.00 USD | 0.00 USD | `+65.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,020,000.00 USD | 2,860.00 USD | 0.00 USD | `+66.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,020,000.00 USD | 264.31 USD | 0.00 USD | `+68.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,020,000.00 USD | 599.34 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,020,000.00 USD | 193.19 USD | 0.00 USD | `+69.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,030,000.00 USD | 3,950.00 USD | 0.00 USD | `+70.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,030,000.00 USD | 1,940.00 USD | 0.00 USD | `+70.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,190,000.00 USD | 160,550.00 USD | 0.00 USD | `+71.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,190,000.00 USD | 1,290.00 USD | 0.00 USD | `+72.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,190,000.00 USD | 1,180.00 USD | 0.00 USD | `+73.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,190,000.00 USD | 630.05 USD | 0.00 USD | `+75.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,200,000.00 USD | 1,410.00 USD | 0.00 USD | `+75.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,200,000.00 USD | 2,610.00 USD | 0.00 USD | `+75.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,210,000.00 USD | 7,630.00 USD | 0.00 USD | `+77.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,210,000.00 USD | 4,640.00 USD | 0.00 USD | `+79.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,210,000.00 USD | 371.88 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,210,000.00 USD | 2,510.00 USD | 0.00 USD | `+80.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,210,000.00 USD | 380.68 USD | 0.00 USD | `+81.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,220,000.00 USD | 1,470.00 USD | 0.00 USD | `+84.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,230,000.00 USD | 11,170.00 USD | 0.00 USD | `+84.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,260,000.00 USD | 34,360.00 USD | 0.00 USD | `+84.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,260,000.00 USD | 253.21 USD | 0.00 USD | `+85.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,260,000.00 USD | 100.29 USD | 0.00 USD | `+85.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,270,000.00 USD | 10,610.00 USD | 0.00 USD | `+88.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,270,000.00 USD | 309.43 USD | 0.00 USD | `+88.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,310,000.00 USD | 36,740.00 USD | 0.00 USD | `+89.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,390,000.00 USD | 81,310.00 USD | 0.00 USD | `+89.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,390,000.00 USD | 1,390.00 USD | 0.00 USD | `+92.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,390,000.00 USD | 216.90 USD | 0.00 USD | `+93.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,390,000.00 USD | 1,990.00 USD | 0.00 USD | `+94.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,400,000.00 USD | 7,200.00 USD | 0.00 USD | `+94.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,400,000.00 USD | 1,350.00 USD | 0.00 USD | `+97.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,460,000.00 USD | 56,000.00 USD | 0.00 USD | `+98.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,460,000.00 USD | 1,260.00 USD | 0.00 USD | `+98.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,560,000.00 USD | 103,010.00 USD | 0.00 USD | `+98.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 7,560,000.00 USD | 1,330.00 USD | 0.00 USD | `+99.68%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.47` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 40,560.00 USD | 26,960.00 USD | 1,100.00 USD |
| `7D` | `3.48` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 44,910.00 USD | 13,410.00 USD | 33.52 USD |
| `7D` | `3.49` | 14,650,000.00 USD | 0.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 42.93 USD |
| `7D` | `3.50` | 14,650,000.00 USD | 0.00 USD | 14,650,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,410.00 USD |
| `7D` | `3.51` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 3,690.00 USD | 0.00 USD | 114.40 USD |
| `7D` | `3.52` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 15,180.00 USD | 0.00 USD | 40,970.00 USD |
| `7D` | `3.53` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,200.00 USD |
| `7D` | `3.54` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,430.00 USD |
| `7D` | `3.55` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,320.00 USD |
| `7D` | `3.56` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 61,170.00 USD | 0.00 USD | 158.35 USD |
| `7D` | `3.57` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,400.00 USD |
| `7D` | `3.58` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,770.00 USD |
| `7D` | `3.59` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 535.75 USD | 18,170.00 USD | 37.48 USD |
| `7D` | `3.60` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,660.00 USD |
| `7D` | `3.62` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,920.00 USD |
| `7D` | `3.63` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 50,840.00 USD | 8,120.00 USD | 156.86 USD |
| `1D` | `3.64` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 1,300.00 USD | 5,040.00 USD | 303.96 USD |
| `7D` | `3.64` | 12,890,000.00 USD | 0.00 USD | 12,890,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,030.00 USD |
| `1D` | `3.65` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 1,410.00 USD | 23,490.00 USD | 14,090.00 USD |
| `7D` | `3.65` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,210.00 USD |
| `1D` | `3.66` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 52,660.00 USD | 13,280.00 USD | 70.59 USD |
| `7D` | `3.66` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,450.00 USD |
| `1D` | `3.67` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 2,720.00 USD | 0.00 USD | 12,610.00 USD |
| `7D` | `3.67` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,500.00 USD |
| `1D` | `3.68` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 680.67 USD | 3,880.00 USD | 31,300.00 USD |
| `7D` | `3.68` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.69` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 24,450.00 USD | 0.00 USD | 12,800.00 USD |
| `7D` | `3.69` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 27,750.00 USD | 0.00 USD | 59,940.00 USD |
| `1D` | `3.70` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,760.00 USD |
| `7D` | `3.70` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,080.00 USD |
| `1D` | `3.71` | 12,770,000.00 USD | 0.00 USD | 12,770,000.00 USD | 16,480.00 USD | 0.00 USD | 780.13 USD |
| `7D` | `3.71` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 51,960.00 USD | 0.00 USD | 74,510.00 USD |
| `1D` | `3.72` | 12,750,000.00 USD | 0.00 USD | 12,750,000.00 USD | 18,460.00 USD | 0.00 USD | 228.04 USD |
| `7D` | `3.72` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 425.03 USD | 0.00 USD | 546.73 USD |
| `1D` | `3.73` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 405.02 USD | 11,920.00 USD | 25,330.00 USD |
| `7D` | `3.73` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 108,320.00 USD | 56,340.00 USD | 82,410.00 USD |
| `7D` | `3.74` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 130,620.00 USD | 40,020.00 USD | 123,850.00 USD |
| `1D` | `3.75` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 1,720.00 USD | 0.00 USD | 52,350.00 USD |
| `7D` | `3.75` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,300.00 USD |
| `1D` | `3.76` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 1,260.00 USD | 8,310.00 USD | 1,020.00 USD |
| `7D` | `3.76` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,230.00 USD |
| `1D` | `3.77` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 48,010.00 USD | 54,910.00 USD | 1,230.00 USD |
| `7D` | `3.77` | 11,330,000.00 USD | 0.00 USD | 11,330,000.00 USD | 15,340.00 USD | 8,090.00 USD | 22,820.00 USD |
| `1D` | `3.78` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 4,250.00 USD | 0.00 USD | 19,280.00 USD |
| `7D` | `3.78` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,920.00 USD |
| `1D` | `3.79` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 4,270.00 USD | 24,440.00 USD | 68,290.00 USD |
| `7D` | `3.79` | 11,130,000.00 USD | 0.00 USD | 11,130,000.00 USD | 51,640.00 USD | 0.00 USD | 137,820.00 USD |
| `1D` | `3.80` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 3,400.00 USD | 0.00 USD | 74,410.00 USD |
| `7D` | `3.80` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 6,530.00 USD | 18,170.00 USD | 16,860.00 USD |
| `1D` | `3.81` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 212,830.00 USD | 0.00 USD | 79,730.00 USD |
| `7D` | `3.81` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 5,310.00 USD | 0.00 USD | 810.67 USD |
| `1D` | `3.82` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 3,240.00 USD | 21,590.00 USD | 94,470.00 USD |
| `7D` | `3.82` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 93,470.00 USD | 91,390.00 USD | 113,860.00 USD |
| `7D` | `3.83` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 0.00 USD | 33,630.00 USD | 2,870.00 USD |
| `1D` | `3.84` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 150,080.00 USD | 33,720.00 USD | 33,210.00 USD |
| `7D` | `3.84` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 7,940.00 USD | 33,350.00 USD | 2,720.00 USD |
| `1D` | `3.85` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 156,570.00 USD | 160,920.00 USD | 408.30 USD |
| `7D` | `3.85` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 3,390.00 USD | 49,170.00 USD | 252.34 USD |
| `1D` | `3.86` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 39,850.00 USD | 46,130.00 USD | 107,390.00 USD |
| `7D` | `3.86` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 5,190.00 USD | 156,620.00 USD | 72,830.00 USD |
| `1D` | `3.87` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 3,490.00 USD | 70,020.00 USD | 152,620.00 USD |
| `7D` | `3.87` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 63,710.00 USD | 0.00 USD | 229,030.00 USD |
| `1D` | `3.88` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 109,330.00 USD | 24,380.00 USD | 227,830.00 USD |
| `7D` | `3.88` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 110,160.00 USD | 77,860.00 USD | 102,520.00 USD |
| `1D` | `3.89` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 446,590.00 USD | 91,430.00 USD | 197,990.00 USD |
| `7D` | `3.89` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 4,240.00 USD | 50,710.00 USD | 82,770.00 USD |
| `1D` | `3.90` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 32,970.00 USD | 59,980.00 USD | 246,330.00 USD |
| `7D` | `3.90` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 274,050.00 USD | 28,250.00 USD | 54,000.00 USD |
| `1D` | `3.91` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 337,210.00 USD | 120,100.00 USD | 261,900.00 USD |
| `7D` | `3.91` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 121,570.00 USD | 67,260.00 USD | 50,650.00 USD |
| `1D` | `3.92` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 317,510.00 USD | 8,570.00 USD | 125,860.00 USD |
| `7D` | `3.92` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 85,790.00 USD | 66,710.00 USD | 97,980.00 USD |
| `1D` | `3.93` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,820.00 USD |
| `7D` | `3.93` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 30,960.00 USD | 28,720.00 USD | 1,310.00 USD |
| `1D` | `3.94` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 132,520.00 USD | 53,060.00 USD | 136,160.00 USD |
| `7D` | `3.94` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 75,150.00 USD | 0.00 USD | 2,570.00 USD |
| `1D` | `3.95` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 114,710.00 USD | 0.00 USD | 32,990.00 USD |
| `7D` | `3.95` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 8,490.00 USD | 0.00 USD | 2,110.00 USD |
| `1D` | `3.96` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 66,520.00 USD | 22,830.00 USD | 17,230.00 USD |
| `7D` | `3.96` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 165,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.97` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 772.10 USD | 36,470.00 USD | 137,480.00 USD |
| `7D` | `3.97` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 235,890.00 USD | 0.00 USD | 2,270.00 USD |
| `1D` | `3.98` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 19,950.00 USD | 76,990.00 USD | 94,420.00 USD |
| `7D` | `3.98` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 506,280.00 USD | 0.00 USD | 279,430.00 USD |
| `1D` | `3.99` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,190.00 USD |
| `7D` | `3.99` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 298,270.00 USD | 26,340.00 USD | 79,670.00 USD |
| `1D` | `4.00` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 39,240.00 USD | 17,140.00 USD | 137,720.00 USD |
| `7D` | `4.00` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,320.00 USD |
| `1D` | `4.01` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 473.90 USD | 158,450.00 USD | 222,830.00 USD |
| `7D` | `4.01` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 368,350.00 USD | 57,440.00 USD | 437,920.00 USD |
| `1D` | `4.02` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 109,790.00 USD | 41,930.00 USD | 72,300.00 USD |
| `7D` | `4.02` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 271,690.00 USD | 156,620.00 USD | 253,220.00 USD |
| `1D` | `4.03` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 38,390.00 USD | 48,890.00 USD | 0.00 USD |
| `7D` | `4.03` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 245,910.00 USD | 0.00 USD | 346,390.00 USD |
| `1D` | `4.04` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 66,450.00 USD | 21,940.00 USD | 183,110.00 USD |
| `7D` | `4.04` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 321,230.00 USD | 0.00 USD | 492,260.00 USD |
| `1D` | `4.05` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 347,570.00 USD | 23,720.00 USD | 0.00 USD |
| `7D` | `4.05` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 270.82 USD |
| `1D` | `4.06` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 34,760.00 USD | 72,940.00 USD | 386,720.00 USD |
| `7D` | `4.06` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 72,410.00 USD | 925.18 USD |
| `1D` | `4.07` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 218,800.00 USD | 179,680.00 USD | 188,840.00 USD |
| `7D` | `4.07` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 0.00 USD | 287,180.00 USD | 166,480.00 USD |
| `1D` | `4.08` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 68,020.00 USD | 196,150.00 USD | 79,620.00 USD |
| `7D` | `4.08` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 0.00 USD | 237,170.00 USD | 0.00 USD |
| `1D` | `4.09` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 163,310.00 USD | 0.00 USD | 151,720.00 USD |
| `7D` | `4.09` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 127,170.00 USD | 137,180.00 USD | 432,940.00 USD |
| `1D` | `4.10` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 0.00 USD | 58,480.00 USD | 61,820.00 USD |
| `7D` | `4.10` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 24,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.11` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 60,170.00 USD | 100,990.00 USD |
| `7D` | `4.11` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 98,730.00 USD |
| `1D` | `4.12` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 379,460.00 USD |
| `7D` | `4.12` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 137,940.00 USD | 0.00 USD |
| `1D` | `4.13` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 310,560.00 USD |
| `7D` | `4.13` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 164,000.00 USD |
| `1D` | `4.14` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 238,150.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 469,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.17` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 58,020.00 USD | 0.00 USD | 293.77 USD |
| `1D` | `4.18` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 329,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.19` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 204,570.00 USD | 0.00 USD | 293.68 USD |
| `7D` | `4.19` | 808,880.00 USD | 0.00 USD | 808,880.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.20` | 986,390.00 USD | 0.00 USD | 986,390.00 USD | 66,990.00 USD | 0.00 USD | 72,700.00 USD |
| `7D` | `4.20` | 806,120.00 USD | 0.00 USD | 806,120.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 846,700.00 USD | 0.00 USD | 846,700.00 USD | 168,700.00 USD | 98,820.00 USD | 42,830.00 USD |
| `7D` | `4.21` | 206,800.00 USD | 0.00 USD | 206,800.00 USD | 2,900.00 USD | 0.00 USD | 82,000.00 USD |
| `1D` | `4.22` | 536,340.00 USD | 0.00 USD | 536,340.00 USD | 97,990.00 USD | 129,920.00 USD | 308,440.00 USD |
| `7D` | `4.22` | 121,900.00 USD | 0.00 USD | 121,900.00 USD | 121,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.23` | 651,000.00 USD | 651,000.00 USD | 0.00 USD | 1,340.00 USD | 427,200.00 USD | 222,460.00 USD |
| `1D` | `4.23` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,340.00 USD | 427,200.00 USD | 222,460.00 USD |
| `7D` | `4.23` | 284,010.00 USD | 284,010.00 USD | 0.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD |
| `7D` | `4.23` | 568,030.00 USD | 568,030.00 USD | 0.00 USD | 117,530.00 USD | 0.00 USD | 166,480.00 USD |
| `1D` | `4.24` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 594,350.00 USD | 137,280.00 USD | 285,220.00 USD |
| `7D` | `4.24` | 719,410.00 USD | 719,410.00 USD | 0.00 USD | 2,900.00 USD | 52,690.00 USD | 95,800.00 USD |
| `1D` | `4.25` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 4,080.00 USD | 82,610.00 USD | 501,160.00 USD |
| `7D` | `4.25` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 3,390.00 USD | 223,240.00 USD | 433,170.00 USD |
| `1D` | `4.26` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 150,470.00 USD | 221,190.00 USD | 93,880.00 USD |
| `7D` | `4.26` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 2,960.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 699,060.00 USD | 51,930.00 USD | 152,560.00 USD |
| `7D` | `4.27` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 24,810.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 125,880.00 USD | 41,380.00 USD | 285,040.00 USD |
| `7D` | `4.28` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 119,230.00 USD | 497,680.00 USD | 1,290,000.00 USD |
| `1D` | `4.29` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 156,040.00 USD | 32,690.00 USD | 162,030.00 USD |
| `7D` | `4.29` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 5,150.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 65,250.00 USD | 56,980.00 USD | 163,490.00 USD |
| `7D` | `4.30` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 376,510.00 USD | 50,050.00 USD | 194,650.00 USD |
| `7D` | `4.31` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 215,700.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 107,540.00 USD | 106,760.00 USD | 95,610.00 USD |
| `7D` | `4.32` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 268,260.00 USD | 160,980.00 USD | 309,880.00 USD |
| `1D` | `4.33` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 292,220.00 USD | 158,240.00 USD | 127,560.00 USD |
| `7D` | `4.33` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 8,950.00 USD | 84,830.00 USD | 91,620.00 USD |
| `1D` | `4.34` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 273,450.00 USD | 140,540.00 USD | 189,340.00 USD |
| `7D` | `4.34` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 9,550.00 USD | 97,260.00 USD | 351,030.00 USD |
| `1D` | `4.35` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 2,840.00 USD | 39,020.00 USD | 144,480.00 USD |
| `7D` | `4.35` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | 85,890.00 USD |
| `1D` | `4.36` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 86,330.00 USD | 20,830.00 USD | 60,020.00 USD |
| `7D` | `4.36` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 10,460.00 USD | 0.00 USD | 143,250.00 USD |
| `1D` | `4.37` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 110,040.00 USD | 46,860.00 USD | 156,480.00 USD |
| `1D` | `4.38` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 250,760.00 USD | 34,500.00 USD | 584,290.00 USD |
| `7D` | `4.38` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 37,480.00 USD | 41,380.00 USD | 333,410.00 USD |
| `7D` | `4.39` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 252,620.00 USD | 108,260.00 USD | 158,250.00 USD |
| `1D` | `4.40` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 385,030.00 USD | 47,530.00 USD | 92,060.00 USD |
| `7D` | `4.40` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 111,810.00 USD | 26,950.00 USD | 466,710.00 USD |
| `1D` | `4.41` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 197,850.00 USD | 130,890.00 USD | 61,550.00 USD |
| `7D` | `4.41` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 1,450.00 USD | 65,600.00 USD | 273,190.00 USD |
| `1D` | `4.42` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 1,080.00 USD | 60,770.00 USD | 22,260.00 USD |
| `7D` | `4.42` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 176,380.00 USD |
| `1D` | `4.43` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 6,140.00 USD | 49,400.00 USD | 94,610.00 USD |
| `7D` | `4.43` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 70,920.00 USD |
| `1D` | `4.44` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 154,690.00 USD | 339,100.00 USD | 295,010.00 USD |
| `7D` | `4.44` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 143,990.00 USD | 72,560.00 USD |
| `1D` | `4.45` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 1,750.00 USD | 50,720.00 USD | 3,590.00 USD |
| `1D` | `4.46` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 2,300.00 USD | 24,070.00 USD | 1,640.00 USD |
| `7D` | `4.46` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 3,070.00 USD | 62,110.00 USD | 1,510.00 USD |
| `1D` | `4.47` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 797.71 USD | 25,190.00 USD | 30,350.00 USD |
| `7D` | `4.47` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 204,140.00 USD | 135,940.00 USD | 0.00 USD |
| `1D` | `4.48` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 167,410.00 USD | 86,520.00 USD | 23,770.00 USD |
| `7D` | `4.48` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.49` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 253,770.00 USD | 155,000.00 USD | 163,110.00 USD |
| `7D` | `4.49` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 244,370.00 USD | 93,790.00 USD | 504.68 USD |
| `1D` | `4.50` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 362,590.00 USD | 69,580.00 USD | 149,110.00 USD |
| `7D` | `4.50` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 374,250.00 USD | 200,700.00 USD | 343.28 USD |
| `1D` | `4.51` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 187,350.00 USD | 223,860.00 USD | 327,640.00 USD |
| `7D` | `4.51` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `4.52` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 287,830.00 USD | 92,260.00 USD | 243,310.00 USD |
| `7D` | `4.52` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 501,550.00 USD | 0.00 USD | 280,160.00 USD |
| `7D` | `4.53` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 309,560.00 USD |
| `1D` | `4.54` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 12,950.00 USD | 150,600.00 USD | 234,040.00 USD |
| `7D` | `4.54` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 0.00 USD | 34,450.00 USD | 108,040.00 USD |
| `7D` | `4.55` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 713.40 USD |
| `1D` | `4.56` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,520.00 USD |
| `7D` | `4.56` | 15,680,000.00 USD | 15,680,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 98,830.00 USD |
| `7D` | `4.57` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 210,490.00 USD |
| `1D` | `4.58` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 481,120.00 USD | 99,430.00 USD | 717,480.00 USD |
| `7D` | `4.58` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,870.00 USD |
| `1D` | `4.59` | 18,410,000.00 USD | 18,410,000.00 USD | 0.00 USD | 559,590.00 USD | 75,460.00 USD | 111,260.00 USD |
| `7D` | `4.59` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD |
| `1D` | `4.60` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 54,700.00 USD | 50,860.00 USD | 68,530.00 USD |
| `7D` | `4.60` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 1,010.00 USD |
| `1D` | `4.61` | 18,720,000.00 USD | 18,720,000.00 USD | 0.00 USD | 66,880.00 USD | 7,560.00 USD | 59,740.00 USD |
| `7D` | `4.61` | 18,190,000.00 USD | 18,190,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 1,280.00 USD |
| `1D` | `4.62` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,170.00 USD |
| `7D` | `4.62` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 1,970.00 USD |
| `1D` | `4.63` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 360.21 USD |
| `7D` | `4.63` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 431.56 USD |
| `1D` | `4.64` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 118,230.00 USD | 11,270.00 USD | 41,420.00 USD |
| `7D` | `4.64` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 407.00 USD |
| `1D` | `4.65` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 201,570.00 USD | 52,020.00 USD | 488,280.00 USD |
| `7D` | `4.65` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 1,870.00 USD |
| `1D` | `4.66` | 20,480,000.00 USD | 20,480,000.00 USD | 0.00 USD | 157,430.00 USD | 299,030.00 USD | 249,460.00 USD |
| `7D` | `4.66` | 19,790,000.00 USD | 19,790,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,630.00 USD |
| `1D` | `4.67` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 118,960.00 USD | 0.00 USD | 301,380.00 USD |
| `7D` | `4.67` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,580.00 USD |
| `1D` | `4.68` | 21,160,000.00 USD | 21,160,000.00 USD | 0.00 USD | 112,140.00 USD | 81,340.00 USD | 61,000.00 USD |
| `7D` | `4.68` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,110.00 USD |
| `1D` | `4.69` | 21,560,000.00 USD | 21,560,000.00 USD | 0.00 USD | 133,390.00 USD | 40,000.00 USD | 225,560.00 USD |
| `7D` | `4.69` | 20,840,000.00 USD | 20,840,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,430.00 USD |
| `7D` | `4.70` | 21,160,000.00 USD | 21,160,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `7D` | `4.71` | 21,570,000.00 USD | 21,570,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 1,070.00 USD |
| `7D` | `4.72` | 21,760,000.00 USD | 21,760,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,260.00 USD |
| `7D` | `4.73` | 21,840,000.00 USD | 21,840,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 790.73 USD |
| `7D` | `4.74` | 22,160,000.00 USD | 22,160,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 130,720.00 USD |
| `7D` | `4.75` | 22,700,000.00 USD | 22,700,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 342,050.00 USD |
| `7D` | `4.76` | 24,050,000.00 USD | 24,050,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 275,020.00 USD |
| `7D` | `4.77` | 24,950,000.00 USD | 24,950,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 26,090,000.00 USD | 26,090,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 153,740.00 USD |
| `7D` | `4.79` | 27,120,000.00 USD | 27,120,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 71,560.00 USD |
| `7D` | `4.80` | 28,710,000.00 USD | 28,710,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,610.00 USD |
| `7D` | `4.81` | 29,340,000.00 USD | 29,340,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 102,460.00 USD |
| `7D` | `4.82` | 32,110,000.00 USD | 32,110,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 33,750,000.00 USD | 33,750,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 740,680.00 USD |
| `7D` | `4.84` | 34,250,000.00 USD | 34,250,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 323,750.00 USD |
| `7D` | `4.85` | 36,280,000.00 USD | 36,280,000.00 USD | 0.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 37,690,000.00 USD | 37,690,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 801,150.00 USD |
| `7D` | `4.87` | 38,750,000.00 USD | 38,750,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,540.00 USD |
| `7D` | `4.88` | 40,270,000.00 USD | 40,270,000.00 USD | 0.00 USD | 450,900.00 USD | 266,980.00 USD | 793,500.00 USD |
| `7D` | `4.89` | 40,850,000.00 USD | 40,850,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 271,050.00 USD |
| `7D` | `4.90` | 41,990,000.00 USD | 41,990,000.00 USD | 0.00 USD | 451,360.00 USD | 145,910.00 USD | 541,900.00 USD |
| `7D` | `4.91` | 43,430,000.00 USD | 43,430,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 591,540.00 USD |
| `7D` | `4.92` | 45,160,000.00 USD | 45,160,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,600.00 USD |
| `7D` | `4.93` | 46,720,000.00 USD | 46,720,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 748,270.00 USD |
| `7D` | `4.94` | 48,040,000.00 USD | 48,040,000.00 USD | 0.00 USD | 339,870.00 USD | 290,290.00 USD | 694,910.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `265,201,486.7 NEAR`
  * 1h OI Change: `+4.55%` | 4h OI Change: `+4.86%` | 24h OI Change: `-12.24%`
  * Exchange Breakdown: Binance=`207.63M` | Bybit=`149.09M` | OKX=`51.79M` | Hyperliquid=`240.99M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-73.15K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0023%` | **USDT OKX** | `-0.0279%` |
| **USDT Bybit** | `-0.0357%` | **USDT KuCoin** | `0.0091%` |
| **USDT MEXC** | `-0.0022%` | **USDT BingX** | `-0.0017%` |
| **USDT Gate** | `-0.0520%` | **USDT Bitget** | `-0.0198%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `44.48%` | `55.52%` | `0.80` | 11,330,000.00 USD |
| `15M` | `Binance` | `43.36%` | `56.64%` | `0.77` | 5,610,000.00 USD |
| `15M` | `OKX` | `35.99%` | `64.01%` | `0.56` | 1,200,000.00 USD |
| `15M` | `Bybit` | `41.36%` | `58.64%` | `0.71` | 1,590,000.00 USD |
| `15M` | `KuCoin` | `40.37%` | `59.63%` | `0.68` | 84,780.00 USD |
| `15M` | `Gate` | `60.5%` | `39.5%` | `1.53` | 217,800.00 USD |
| `15M` | `Bitget` | `48.57%` | `51.43%` | `0.94` | 750,860.00 USD |
| `15M` | `BingX` | `54.14%` | `45.86%` | `1.18` | 171,230.00 USD |
| `15M` | `MEXC` | `54.52%` | `45.48%` | `1.20` | 682,990.00 USD |
| `15M` | `Bitunix` | `41.85%` | `58.15%` | `0.72` | 587,540.00 USD |
| `15M` | `Hyperliquid` | `59.8%` | `40.2%` | `1.49` | 88,500.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `79.06%` | `20.94%` | `3.78` | 58,210.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `68.3%` | `31.7%` | `2.15` | 217,830.00 USD |
| `15M` | `HTX` | `31.95%` | `68.05%` | `0.47` | 19,130.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `49.11%` | `50.89%` | `0.97` | 32,070.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.71%` | `74.29%` | `0.35` | 13,690.00 USD |
| `15M` | `Whale Positions` | `43.36%` | `56.64%` | `0.77` | 5,610,000.00 USD |
| `15M` | `Global Accounts` | `44.48%` | `55.52%` | `0.80` | 11,330,000.00 USD |
| `1H` | `NEAR` | `52.84%` | `47.16%` | `1.12` | 36,490,000.00 USD |
| `1H` | `Binance` | `51.55%` | `48.45%` | `1.06` | 14,840,000.00 USD |
| `1H` | `OKX` | `57.18%` | `42.82%` | `1.34` | 5,470,000.00 USD |
| `1H` | `Bybit` | `48.42%` | `51.58%` | `0.94` | 5,160,000.00 USD |
| `1H` | `KuCoin` | `39.1%` | `60.9%` | `0.64` | 482,150.00 USD |
| `1H` | `Gate` | `52.31%` | `47.69%` | `1.10` | 755,140.00 USD |
| `1H` | `Bitget` | `48.08%` | `51.92%` | `0.93` | 2,580,000.00 USD |
| `1H` | `BingX` | `43.27%` | `56.73%` | `0.76` | 1,610,000.00 USD |
| `1H` | `MEXC` | `58.56%` | `41.44%` | `1.41` | 2,360,000.00 USD |
| `1H` | `Bitunix` | `47.75%` | `52.25%` | `0.91` | 1,550,000.00 USD |
| `1H` | `Hyperliquid` | `64.63%` | `35.37%` | `1.83` | 465,660.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `90.94%` | `9.06%` | `10.04` | 568,370.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `92.55%` | `7.45%` | `12.42` | 511,550.00 USD |
| `1H` | `HTX` | `47.26%` | `52.74%` | `0.90` | 49,130.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `55.66%` | `44.34%` | `1.26` | 60,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.17%` | `47.83%` | `1.09` | 34,540.00 USD |
| `1H` | `Whale Positions` | `51.55%` | `48.45%` | `1.06` | 14,840,000.00 USD |
| `1H` | `Global Accounts` | `52.84%` | `47.16%` | `1.12` | 36,490,000.00 USD |
| `4H` | `NEAR` | `55.34%` | `44.66%` | `1.24` | 312,690,000.00 USD |
| `4H` | `Binance` | `52.99%` | `47.01%` | `1.13` | 125,860,000.00 USD |
| `4H` | `OKX` | `56.14%` | `43.86%` | `1.28` | 36,900,000.00 USD |
| `4H` | `Bybit` | `55.8%` | `44.2%` | `1.26` | 41,090,000.00 USD |
| `4H` | `KuCoin` | `54.47%` | `45.53%` | `1.20` | 1,910,000.00 USD |
| `4H` | `Gate` | `55.05%` | `44.95%` | `1.22` | 15,280,000.00 USD |
| `4H` | `Bitget` | `54.6%` | `45.4%` | `1.20` | 17,660,000.00 USD |
| `4H` | `BingX` | `57.4%` | `42.6%` | `1.35` | 16,120,000.00 USD |
| `4H` | `MEXC` | `52.65%` | `47.35%` | `1.11` | 10,700,000.00 USD |
| `4H` | `Bitunix` | `53.25%` | `46.75%` | `1.14` | 6,720,000.00 USD |
| `4H` | `Hyperliquid` | `59.64%` | `40.36%` | `1.48` | 29,200,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.8%` | `45.2%` | `1.21` | 1,630,000.00 USD |
| `4H` | `Crypto.com` | `51.85%` | `48.15%` | `1.08` | 19,690.00 USD |
| `4H` | `WhiteBIT` | `88.49%` | `11.51%` | `7.69` | 5,620,000.00 USD |
| `4H` | `HTX` | `48.59%` | `51.41%` | `0.95` | 254,450.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `65.58%` | `34.42%` | `1.91` | 630,140.00 USD |
| `4H` | `Aster` | `33.03%` | `66.97%` | `0.49` | 1,480,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.53%` | `48.47%` | `1.06` | 1,620,000.00 USD |
| `4H` | `Whale Positions` | `52.99%` | `47.01%` | `1.13` | 125,860,000.00 USD |
| `4H` | `Global Accounts` | `55.34%` | `44.66%` | `1.24` | 312,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.06` | `4.07` | `4.06` | `4.10` | `4.05` | 6,914,413.13 USD | 3,114,711.21 USD | 3,799,701.92 USD | -684,990.71 USD | `-9.91%` | `2B / 8S` |
| `0:00 UTC` | `4.08` | `4.08` | `4.08` | `4.09` | `4.06` | 5,392,588.64 USD | 3,075,595.58 USD | 2,316,993.06 USD | 758,602.52 USD | `+14.07%` | `1B / 1S` |
| `5:00 UTC` | `4.07` | `4.08` | `4.07` | `4.11` | `4.07` | 4,324,346.41 USD | 2,642,977.58 USD | 1,681,368.84 USD | 961,608.74 USD | `+22.24%` | `17B / 1S` |
| `0:00 UTC` | `4.14` | `4.13` | `4.14` | `4.16` | `4.10` | 9,990,039.56 USD | 5,818,620.01 USD | 4,171,419.55 USD | 1,647,200.46 USD | `+16.49%` | `10B / 2S` |
| `5:00 UTC` | `4.15` | `4.15` | `4.15` | `4.17` | `4.14` | 5,034,918.87 USD | 2,878,643.09 USD | 2,156,275.78 USD | 722,367.31 USD | `+14.35%` | `2B / 1S` |
| `0:00 UTC` | `4.14` | `4.14` | `4.14` | `4.16` | `4.12` | 6,119,703.21 USD | 2,845,557.53 USD | 3,274,145.68 USD | -428,588.16 USD | `-7.00%` | `1B / 5S` |
| `5:00 UTC` | `4.18` | `4.19` | `4.18` | `4.22` | `4.15` | 12,847,139.28 USD | 7,912,037.28 USD | 4,935,102.00 USD | 2,976,935.28 USD | `+23.17%` | `8B / 2S` |
| `0:00 UTC` | `4.19` | `4.19` | `4.19` | `4.20` | `4.18` | 4,234,860.30 USD | 1,755,713.34 USD | 2,479,146.96 USD | -723,433.62 USD | `-17.08%` | `2B / 1S` |
| `5:00 UTC` | `4.23` | `4.23` | `4.23` | `4.24` | `4.20` | 7,447,660.88 USD | 3,310,439.61 USD | 4,137,221.27 USD | -826,781.65 USD | `-11.10%` | `6B / 7S` |
| `0:00 UTC` | `4.22` | `4.22` | `4.22` | `4.23` | `4.22` | 617,425.10 USD | 220,555.89 USD | 396,869.21 USD | -176,313.31 USD | `-28.56%` | `3B / 4S` |

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
| `5m` | 25,700.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 92,270.00 USD | -2,380,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 405,940.00 USD | -3,310,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,300,000.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,710,000.00 USD | 6,820,000.00 USD | **`ACCUMULATION`** |
| `4h` | 6,120,000.00 USD | 16,090,000.00 USD | **`ACCUMULATION`** |
| `6h` | 4,160,000.00 USD | 2,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | 736,780.00 USD | -17,130,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,170,000.00 USD | -20,090,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,490,000.00 USD | -53,590,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -75,520,000.00 USD | -129,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -243,230,000.00 USD | -677,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+25.70K` | 15m=`+92.27K` | 1h=`+1.30M` | 24h=`-11.49M`
* Futures Capital Netflows: 5m=`-1.18M` | 15m=`-2.38M` | 1h=`+1.21M` | 24h=`-53.59M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3.86` (Risk Distance: `0.1058` pts)
  * +2.5R Take Profit: `4.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.25` (Risk Distance: `0.1058` pts)
  * +2.5R Take Profit: `3.88`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
