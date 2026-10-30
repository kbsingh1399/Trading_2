# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:31:46 IST` (`2026-10-30 05:01:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.22` | **Live Ask Quote**: `4.25` | **Mid Price**: `4.24`
- **Spread Points**: `29.00` | **Spread BPS**: `68.47 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.02` | VWAP Z-Score: `+2.44` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0512` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `60.74` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.22` | Lower -3.00σ Band: `3.82`
  * Upper +2.51σ Band: `4.19` | Lower -2.51σ Band: `3.85`
  * Upper +2.01σ Band: `4.16` | Lower -2.01σ Band: `3.88`
  * Upper +2.00σ Band: `4.16` | Lower -2.00σ Band: `3.89`
  * Upper +1.28σ Band: `4.11` | Lower -1.28σ Band: `3.93`
  * Upper +1.00σ Band: `4.09` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.13` | EMA-20=`4.11` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.18` (Slope: `+0.0000`) | EMA-100=`4.29`
  * Institutional Anchors: EMA-144=`4.35` | EMA-200=`4.39` (Slope: `-0.8477`) | EMA-233=`4.42`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.15` (Distance: `+2.08%`)
  * Point of Control (POC) = `4.09` (Distance: `+3.43%`)
  * Value Area Low (VAL) = `3.97` (Distance: `+6.64%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.69` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.25` | Low=`4.22`
  * New York Session (13:00-21:00 UTC): High=`4.26` | Low=`4.21`
  * Initial Balance (First Hour): IB High=`4.25` | IB Low=`4.22`
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
| `5m` | `4.20` | `4.20` | `4.19` | `4.19` | `402,032` | 1,686,595.95 USD | -296.78 USD | `-0.02%` | -25,943,015.84 USD | `-0.44` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4.19` | `4.19` | `4.18` | `4.19` | `353,051` | 1,478,619.83 USD | -455,232.99 USD | `-30.79%` | -26,398,248.84 USD | `-1.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.19` | `4.19` | `4.18` | `4.19` | `206,204` | 863,220.17 USD | -248,433.68 USD | `-28.78%` | -26,646,682.52 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.16` | `4.22` | `4.15` | `4.20` | `3,068,734` | 12,844,076.20 USD | 2,973,872.20 USD | `+23.15%` | -25,611,693.78 USD | `+1.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.20` | `4.20` | `4.18` | `4.20` | `1,011,226` | 4,237,923.38 USD | -720,370.54 USD | `-17.00%` | -26,332,064.33 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.20` | `4.24` | `4.20` | `4.24` | `1,159,700` | 4,899,628.84 USD | -128,966.59 USD | `-2.63%` | -26,461,030.92 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.00` | `4.11` | `3.97` | `4.06` | `7,535,910` | 30,558,990.03 USD | 3,476,842.65 USD | `+11.38%` | -32,246,756.85 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.06` | `4.17` | `4.06` | `4.16` | `6,011,715` | 24,741,893.48 USD | 4,089,779.03 USD | `+16.53%` | -28,156,977.82 USD | `+1.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4.16` | `4.24` | `4.12` | `4.24` | `6,718,078` | 28,100,865.67 USD | 1,696,412.86 USD | `+6.04%` | -26,460,564.96 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.22` | `4.12` | `4.19` | `5,508,549` | 22,992,215.36 USD | 1,841,320.58 USD | `+8.01%` | -11,467,709.38 USD | `+0.72` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | 3,315,318.08 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -853,625.74 USD | `-1.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -12,896,665.02 USD | `-1.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -13,309,029.96 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.24` | `4.12` | `4.24` | `6,718,188` | 28,101,331.63 USD | 1,695,946.90 USD | `+6.04%` | -11,613,083.06 USD | `+0.70` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `61` | `0x7737...bf66` | `LONG` | 23,866,124.24 USD | `5,640,376.30` | `2.35` | `4.23` | `0.8492` | 10,594,221.41 USD | `+44.39%` | `10X Cross` |
| `103` | `0xefe4...194b` | `SHORT` | 19,099,975.57 USD | `4,507,262.50` | `4.21` | `4.23` | `6.61` | -124,878.86 USD | `-0.65%` | `5X Cross` |
| `133` | `0xb581...6f4f` | `LONG` | 15,232,572.00 USD | `3,600,000.00` | `5.19` | `4.23` | `0.000000` | -3,460,463.22 USD | `-22.72%` | `4X Cross` |
| `210` | `0xdd53...2b13` | `SHORT` | 10,161,735.21 USD | `2,400,202.00` | `2.31` | `4.23` | `28.91` | -4,615,886.65 USD | `-45.42%` | `3X Cross` |
| `268` | `0x77ee...2902` | `LONG` | 8,729,207.75 USD | `2,063,023.10` | `1.93` | `4.23` | `0.000000` | 4,738,011.82 USD | `+54.28%` | `10X Cross` |
| `362` | `0x9df2...c665` | `SHORT` | 6,416,816.85 USD | `1,514,579.00` | `2.36` | `4.23` | `23.87` | -2,836,827.19 USD | `-44.21%` | `10X Cross` |
| `378` | `0xb83d...6e36` | `SHORT` | 6,124,380.12 USD | `1,445,759.10` | `5.19` | `4.23` | `92.49` | 1,385,068.82 USD | `+22.62%` | `3X Cross` |
| `379` | `0x7fda...17d1` | `SHORT` | 6,121,218.16 USD | `1,443,915.10` | `4.28` | `4.23` | `28.87` | 60,860.36 USD | `+0.99%` | `10X Cross` |
| `396` | `0xb46b...538e` | `SHORT` | 5,665,174.40 USD | `1,336,000.00` | `4.33` | `4.23` | `7.43` | 119,689.66 USD | `+2.11%` | `10X Cross` |
| `465` | `0x60b0...991e` | `LONG` | 4,747,277.87 USD | `1,121,307.10` | `5.00` | `4.23` | `0.000000` | -854,146.56 USD | `-17.99%` | `10X Cross` |
| `491` | `0xcac1...26b3` | `SHORT` | 4,550,634.02 USD | `1,073,743.90` | `2.48` | `4.23` | `12.15` | -1,890,690.56 USD | `-41.55%` | `10X Cross` |
| `510` | `0x781e...96b7` | `SHORT` | 4,406,675.98 USD | `1,039,604.60` | `2.45` | `4.23` | `7.47` | -1,862,338.79 USD | `-42.26%` | `10X Cross` |
| `591` | `0x45d2...4029` | `SHORT` | 3,854,764.72 USD | `909,400.00` | `3.26` | `4.23` | `48.19` | -888,614.82 USD | `-23.05%` | `10X Cross` |
| `598` | `0x4cae...7c34` | `LONG` | 3,810,628.45 USD | `900,587.40` | `3.97` | `4.23` | `2.86` | 232,435.66 USD | `+6.10%` | `10X Cross` |
| `824` | `0x005a...61fe` | `LONG` | 2,766,629.35 USD | `652,414.60` | `2.08` | `4.23` | `2.40` | 1,409,098.12 USD | `+50.93%` | `7X Cross` |
| `830` | `0xba5d...a352` | `SHORT` | 2,739,884.84 USD | `647,532.50` | `2.83` | `4.23` | `13.30` | -907,169.90 USD | `-33.11%` | `10X Cross` |
| `846` | `0xb695...a92d` | `SHORT` | 2,709,255.71 USD | `639,231.70` | `4.57` | `4.23` | `44.71` | 214,103.21 USD | `+7.90%` | `10X Cross` |
| `848` | `0xd1dd...9e85` | `SHORT` | 2,697,946.61 USD | `637,621.00` | `4.96` | `4.23` | `18.05` | 465,526.13 USD | `+17.25%` | `10X Cross` |
| `850` | `0x123d...3bff` | `SHORT` | 2,690,843.37 USD | `634,992.30` | `2.09` | `4.23` | `9.07` | -1,365,729.63 USD | `-50.75%` | `10X Cross` |
| `864` | `0xcf53...ee11` | `SHORT` | 2,635,390.74 USD | `621,598.40` | `5.07` | `4.23` | `25.06` | 516,779.51 USD | `+19.61%` | `10X Cross` |
| `987` | `0xbfc7...80b4` | `SHORT` | 2,250,165.60 USD | `531,000.00` | `2.01` | `4.23` | `7.12` | -1,184,966.21 USD | `-52.66%` | `10X Cross` |
| `1247` | `0x0eec...d4c5` | `LONG` | 1,781,524.62 USD | `420,905.50` | `4.01` | `4.23` | `1.21` | 95,104.61 USD | `+5.34%` | `10X Cross` |
| `1290` | `0xe097...d0fe` | `LONG` | 1,695,560.00 USD | `400,000.00` | `5.29` | `4.23` | `0.000000` | -421,227.30 USD | `-24.84%` | `10X Cross` |
| `1433` | `0x6e8f...4364` | `LONG` | 1,530,340.53 USD | `361,210.50` | `3.28` | `4.23` | `3.50` | 346,280.30 USD | `+22.63%` | `10X Cross` |
| `1450` | `0xef96...9383` | `SHORT` | 1,512,785.84 USD | `357,412.90` | `4.50` | `4.23` | `14.15` | 96,475.89 USD | `+6.38%` | `10X Cross` |
| `1468` | `0xdf95...7d72` | `SHORT` | 1,485,370.47 USD | `350,422.40` | `4.23` | `4.23` | `109.38` | -2,272.86 USD | `-0.15%` | `10X Cross` |
| `1472` | `0xcf67...eb24` | `LONG` | 1,481,410.00 USD | `350,000.00` | `1.98` | `4.23` | `1.47` | 789,792.12 USD | `+53.31%` | `10X Cross` |
| `1586` | `0xfc27...9d9d` | `SHORT` | 1,354,422.26 USD | `319,997.70` | `5.01` | `4.23` | `59.93` | 249,120.36 USD | `+18.39%` | `10X Cross` |
| `1587` | `0x089f...a4f8` | `LONG` | 1,352,935.02 USD | `319,043.30` | `4.06` | `4.23` | `0.000000` | 58,078.31 USD | `+4.29%` | `1X Cross` |
| `1644` | `0x17c3...a868` | `LONG` | 1,294,759.69 USD | `305,454.30` | `4.36` | `4.23` | `0.000000` | -38,048.64 USD | `-2.94%` | `3X Cross` |
| `1653` | `0x9aa5...58af` | `SHORT` | 1,283,870.76 USD | `302,971.20` | `4.78` | `4.23` | `33.71` | 163,922.58 USD | `+12.77%` | `10X Cross` |
| `1667` | `0x9836...457e` | `LONG` | 1,271,642.54 USD | `300,000.60` | `4.57` | `4.23` | `1.86` | -100,430.63 USD | `-7.90%` | `10X Cross` |
| `1726` | `0xe065...0f85` | `SHORT` | 1,219,106.89 USD | `288,027.90` | `2.81` | `4.23` | `5.56` | -408,553.77 USD | `-33.51%` | `10X Cross` |
| `1920` | `0xff43...d924` | `LONG` | 1,055,593.97 USD | `249,474.50` | `4.64` | `4.23` | `3.28` | -102,449.71 USD | `-9.71%` | `10X Isolated` |

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
| `Live` | `Long` | `0.8650` | 22,850,000.00 USD | 0.00 USD | 912.83 USD | `-79.11%` | `1,055.30` |
| `Live` | `Long` | `0.8950` | 22,850,000.00 USD | 0.00 USD | 40,360.00 USD | `-78.38%` | `45,091.40` |
| `Live` | `Long` | `0.9050` | 22,810,000.00 USD | 0.00 USD | 3,040.00 USD | `-78.14%` | `3,354.30` |
| `Live` | `Long` | `0.9150` | 22,810,000.00 USD | 0.00 USD | 11,370.00 USD | `-77.90%` | `12,425.00` |
| `Live` | `Long` | `0.9350` | 22,800,000.00 USD | 0.00 USD | 935.00 USD | `-77.42%` | `1,000.00` |
| `Live` | `Long` | `0.9650` | 22,800,000.00 USD | 0.00 USD | 965.00 USD | `-76.69%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,800,000.00 USD | 0.00 USD | 7,800.00 USD | `-76.21%` | `7,918.30` |
| `Live` | `Long` | `0.9950` | 22,790,000.00 USD | 0.00 USD | 154,200.00 USD | `-75.97%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,630,000.00 USD | 0.00 USD | 30,990.00 USD | `-75.73%` | `30,836.80` |
| `Live` | `Long` | `1.02` | 22,600,000.00 USD | 0.00 USD | 10,250.00 USD | `-75.24%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,590,000.00 USD | 0.00 USD | 5,070.00 USD | `-75.00%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,590,000.00 USD | 0.00 USD | 2,740.00 USD | `-74.76%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 22,590,000.00 USD | 0.00 USD | 8,590.00 USD | `-74.52%` | `8,146.90` |
| `Live` | `Long` | `1.06` | 22,580,000.00 USD | 0.00 USD | 99,270.00 USD | `-74.28%` | `93,214.70` |
| `Live` | `Long` | `1.07` | 22,480,000.00 USD | 0.00 USD | 7,510.00 USD | `-74.04%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 22,470,000.00 USD | 0.00 USD | 337.44 USD | `-73.80%` | `311.00` |
| `Live` | `Long` | `1.09` | 22,470,000.00 USD | 0.00 USD | 16,190.00 USD | `-73.55%` | `14,783.90` |
| `Live` | `Long` | `1.11` | 22,450,000.00 USD | 0.00 USD | 557.50 USD | `-73.07%` | `500.00` |
| `Live` | `Long` | `1.12` | 22,450,000.00 USD | 0.00 USD | 856.24 USD | `-72.83%` | `761.10` |
| `Live` | `Long` | `1.14` | 22,450,000.00 USD | 0.00 USD | 13,510.00 USD | `-72.59%` | `11,906.50` |
| `Live` | `Long` | `1.15` | 22,440,000.00 USD | 0.00 USD | 40,820.00 USD | `-72.35%` | `35,649.30` |
| `Live` | `Long` | `1.17` | 22,400,000.00 USD | 0.00 USD | 144.69 USD | `-71.86%` | `124.20` |
| `Live` | `Long` | `1.18` | 22,400,000.00 USD | 0.00 USD | 1,720.00 USD | `-71.62%` | `1,463.50` |
| `Live` | `Long` | `1.19` | 22,400,000.00 USD | 0.00 USD | 3,440.00 USD | `-71.38%` | `2,906.40` |
| `Live` | `Long` | `1.20` | 22,390,000.00 USD | 0.00 USD | 7,390.00 USD | `-71.14%` | `6,187.90` |
| `Live` | `Long` | `1.21` | 22,380,000.00 USD | 0.00 USD | 56,130.00 USD | `-70.90%` | `46,584.90` |
| `Live` | `Long` | `1.23` | 22,330,000.00 USD | 0.00 USD | 517,410.00 USD | `-70.41%` | `422,373.40` |
| `Live` | `Long` | `1.25` | 21,810,000.00 USD | 0.00 USD | 2,190.00 USD | `-69.93%` | `1,756.00` |
| `Live` | `Long` | `1.25` | 21,810,000.00 USD | 0.00 USD | 2,260.00 USD | `-69.69%` | `1,803.00` |
| `Live` | `Long` | `1.26` | 21,810,000.00 USD | 0.00 USD | 2,310.00 USD | `-69.45%` | `1,827.40` |
| `Live` | `Long` | `1.27` | 21,800,000.00 USD | 0.00 USD | 21,840.00 USD | `-69.21%` | `17,125.90` |
| `Live` | `Long` | `1.28` | 21,780,000.00 USD | 0.00 USD | 428.16 USD | `-68.97%` | `333.20` |
| `Live` | `Long` | `1.30` | 21,780,000.00 USD | 0.00 USD | 116.80 USD | `-68.48%` | `89.50` |
| `Live` | `Long` | `1.31` | 21,780,000.00 USD | 0.00 USD | 1,010.00 USD | `-68.24%` | `770.10` |
| `Live` | `Long` | `1.32` | 21,780,000.00 USD | 0.00 USD | 22,870.00 USD | `-68.00%` | `17,259.90` |
| `Live` | `Long` | `1.34` | 21,760,000.00 USD | 0.00 USD | 603.91 USD | `-67.52%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,760,000.00 USD | 0.00 USD | 2,000.00 USD | `-67.27%` | `1,474.80` |
| `Live` | `Long` | `1.36` | 21,760,000.00 USD | 0.00 USD | 2,860.00 USD | `-67.03%` | `2,096.20` |
| `Live` | `Long` | `1.38` | 21,750,000.00 USD | 0.00 USD | 12,380.00 USD | `-66.79%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 21,740,000.00 USD | 0.00 USD | 295.56 USD | `-66.55%` | `213.40` |
| `Live` | `Long` | `1.40` | 21,740,000.00 USD | 0.00 USD | 1,040.00 USD | `-66.31%` | `743.00` |
| `Live` | `Long` | `1.41` | 21,740,000.00 USD | 0.00 USD | 70,820.00 USD | `-66.07%` | `50,407.00` |
| `Live` | `Long` | `1.42` | 21,670,000.00 USD | 0.00 USD | 112,730.00 USD | `-65.83%` | `79,669.00` |
| `Live` | `Long` | `1.43` | 21,560,000.00 USD | 0.00 USD | 1,020.00 USD | `-65.58%` | `714.90` |
| `Live` | `Long` | `1.44` | 21,550,000.00 USD | 0.00 USD | 15,310.00 USD | `-65.34%` | `10,668.30` |
| `Live` | `Long` | `1.45` | 21,540,000.00 USD | 0.00 USD | 1,660.00 USD | `-65.10%` | `1,146.90` |
| `Live` | `Long` | `1.46` | 21,540,000.00 USD | 0.00 USD | 5,440.00 USD | `-64.86%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 21,530,000.00 USD | 0.00 USD | 429.83 USD | `-64.62%` | `293.40` |
| `Live` | `Long` | `1.48` | 21,530,000.00 USD | 0.00 USD | 1,480.00 USD | `-64.38%` | `1,000.00` |
| `Live` | `Long` | `1.50` | 21,530,000.00 USD | 0.00 USD | 576,020.00 USD | `-63.89%` | `385,297.90` |
| `Live` | `Long` | `1.50` | 20,950,000.00 USD | 0.00 USD | 3,420.00 USD | `-63.65%` | `2,271.90` |
| `Live` | `Long` | `1.51` | 20,950,000.00 USD | 0.00 USD | 454.50 USD | `-63.41%` | `300.00` |
| `Live` | `Long` | `1.52` | 20,950,000.00 USD | 0.00 USD | 605.42 USD | `-63.17%` | `397.00` |
| `Live` | `Long` | `1.53` | 20,950,000.00 USD | 0.00 USD | 1,220.00 USD | `-62.93%` | `797.50` |
| `Live` | `Long` | `1.55` | 20,950,000.00 USD | 0.00 USD | 311.00 USD | `-62.44%` | `200.00` |
| `Live` | `Long` | `1.56` | 20,950,000.00 USD | 0.00 USD | 23,700.00 USD | `-62.20%` | `15,146.30` |
| `Live` | `Long` | `1.57` | 20,920,000.00 USD | 0.00 USD | 589.52 USD | `-61.96%` | `374.30` |
| `Live` | `Long` | `1.58` | 20,920,000.00 USD | 0.00 USD | 1,980.00 USD | `-61.72%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 20,920,000.00 USD | 0.00 USD | 15,740.00 USD | `-61.48%` | `9,870.00` |
| `Live` | `Long` | `1.60` | 20,910,000.00 USD | 0.00 USD | 191.64 USD | `-61.24%` | `119.40` |
| `Live` | `Long` | `1.62` | 20,910,000.00 USD | 0.00 USD | 15,250.00 USD | `-60.75%` | `9,387.20` |
| `Live` | `Long` | `1.64` | 20,890,000.00 USD | 0.00 USD | 3,780.00 USD | `-60.51%` | `2,309.30` |
| `Live` | `Long` | `1.65` | 20,890,000.00 USD | 0.00 USD | 2,040.00 USD | `-60.27%` | `1,240.20` |
| `Live` | `Long` | `1.66` | 20,880,000.00 USD | 0.00 USD | 1,320.00 USD | `-60.03%` | `794.90` |
| `Live` | `Long` | `1.67` | 20,880,000.00 USD | 0.00 USD | 574.59 USD | `-59.79%` | `345.10` |
| `Live` | `Long` | `1.68` | 20,880,000.00 USD | 0.00 USD | 1,380.00 USD | `-59.55%` | `823.50` |
| `Live` | `Long` | `1.69` | 20,880,000.00 USD | 0.00 USD | 12,850.00 USD | `-59.30%` | `7,624.50` |
| `Live` | `Long` | `1.70` | 20,870,000.00 USD | 0.00 USD | 169.50 USD | `-59.06%` | `100.00` |
| `Live` | `Long` | `1.71` | 20,870,000.00 USD | 0.00 USD | 2,190.00 USD | `-58.82%` | `1,286.10` |
| `Live` | `Long` | `1.73` | 20,870,000.00 USD | 0.00 USD | 6,750.00 USD | `-58.34%` | `3,914.50` |
| `Live` | `Long` | `1.74` | 20,860,000.00 USD | 0.00 USD | 5,310.00 USD | `-58.10%` | `3,058.80` |
| `Live` | `Long` | `1.75` | 20,850,000.00 USD | 0.00 USD | 4,230.00 USD | `-57.86%` | `2,422.20` |
| `Live` | `Long` | `1.75` | 20,850,000.00 USD | 0.00 USD | 10,600.00 USD | `-57.61%` | `6,041.40` |
| `Live` | `Long` | `1.76` | 20,840,000.00 USD | 0.00 USD | 722.59 USD | `-57.37%` | `409.40` |
| `Live` | `Long` | `1.77` | 20,840,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.13%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 20,840,000.00 USD | 0.00 USD | 453.93 USD | `-56.89%` | `254.30` |
| `Live` | `Long` | `1.79` | 20,830,000.00 USD | 0.00 USD | 471.73 USD | `-56.65%` | `262.80` |
| `Live` | `Long` | `1.80` | 20,830,000.00 USD | 0.00 USD | 1,350.00 USD | `-56.41%` | `747.90` |
| `Live` | `Long` | `1.81` | 20,830,000.00 USD | 0.00 USD | 8,400.00 USD | `-56.16%` | `4,628.80` |
| `Live` | `Long` | `1.83` | 20,820,000.00 USD | 0.00 USD | 32,440.00 USD | `-55.68%` | `17,680.00` |
| `Live` | `Long` | `1.84` | 20,790,000.00 USD | 0.00 USD | 553,500.00 USD | `-55.44%` | `300,000.60` |
| `Live` | `Long` | `1.85` | 20,240,000.00 USD | 0.00 USD | 13,220.00 USD | `-55.20%` | `7,126.80` |
| `Live` | `Long` | `1.86` | 20,230,000.00 USD | 0.00 USD | 34,420.00 USD | `-54.96%` | `18,455.90` |
| `Live` | `Long` | `1.90` | 20,190,000.00 USD | 0.00 USD | 2,250.00 USD | `-54.23%` | `1,189.40` |
| `Live` | `Long` | `1.91` | 20,190,000.00 USD | 0.00 USD | 2,030.00 USD | `-53.99%` | `1,066.70` |
| `Live` | `Long` | `1.93` | 20,190,000.00 USD | 0.00 USD | 1,870.00 USD | `-53.51%` | `971.20` |
| `Live` | `Long` | `1.94` | 20,180,000.00 USD | 0.00 USD | 34,520.00 USD | `-53.27%` | `17,837.90` |
| `Live` | `Long` | `1.95` | 20,150,000.00 USD | 0.00 USD | 3,710.00 USD | `-53.02%` | `1,909.40` |
| `Live` | `Long` | `1.96` | 20,150,000.00 USD | 0.00 USD | 775.55 USD | `-52.78%` | `396.70` |
| `Live` | `Long` | `1.97` | 20,150,000.00 USD | 0.00 USD | 1,740.00 USD | `-52.54%` | `884.20` |
| `Live` | `Long` | `1.98` | 20,140,000.00 USD | 0.00 USD | 36,170.00 USD | `-52.30%` | `18,315.70` |
| `Live` | `Long` | `1.99` | 20,110,000.00 USD | 0.00 USD | 135.38 USD | `-52.06%` | `68.20` |
| `Live` | `Long` | `2.00` | 20,110,000.00 USD | 0.00 USD | 11,410.00 USD | `-51.82%` | `5,720.40` |
| `Live` | `Long` | `2.00` | 20,100,000.00 USD | 0.00 USD | 102.86 USD | `-51.58%` | `51.30` |
| `Live` | `Long` | `2.02` | 20,100,000.00 USD | 0.00 USD | 20,080.00 USD | `-51.33%` | `9,963.70` |
| `Live` | `Long` | `2.02` | 20,080,000.00 USD | 0.00 USD | 665.62 USD | `-51.09%` | `328.70` |
| `Live` | `Long` | `2.04` | 20,080,000.00 USD | 0.00 USD | 1,390.00 USD | `-50.85%` | `681.60` |
| `Live` | `Long` | `2.04` | 20,070,000.00 USD | 0.00 USD | 3,460.00 USD | `-50.61%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 20,070,000.00 USD | 0.00 USD | 595.33 USD | `-50.37%` | `289.70` |
| `Live` | `Long` | `2.06` | 20,070,000.00 USD | 0.00 USD | 7,870.00 USD | `-50.13%` | `3,809.30` |
| `Live` | `Long` | `2.08` | 20,060,000.00 USD | 0.00 USD | 11,100.00 USD | `-49.89%` | `5,347.70` |
| `Live` | `Long` | `2.08` | 20,050,000.00 USD | 0.00 USD | 18,930.00 USD | `-49.64%` | `9,079.00` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 2,760.00 USD | `-49.40%` | `1,317.50` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 6,240.00 USD | `-49.16%` | `2,964.60` |
| `Live` | `Long` | `2.12` | 20,020,000.00 USD | 0.00 USD | 15,580.00 USD | `-48.92%` | `7,365.20` |
| `Live` | `Long` | `2.12` | 20,010,000.00 USD | 0.00 USD | 34,490.00 USD | `-48.68%` | `16,232.50` |
| `Live` | `Long` | `2.15` | 19,970,000.00 USD | 0.00 USD | 59,140.00 USD | `-48.19%` | `27,573.10` |
| `Live` | `Long` | `2.15` | 19,910,000.00 USD | 0.00 USD | 92,830.00 USD | `-47.95%` | `43,074.40` |
| `Live` | `Long` | `2.17` | 19,820,000.00 USD | 0.00 USD | 189,270.00 USD | `-47.71%` | `87,423.20` |
| `Live` | `Long` | `2.17` | 19,630,000.00 USD | 0.00 USD | 292.32 USD | `-47.47%` | `134.40` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 1,110.00 USD | `-47.23%` | `505.90` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 10,010.00 USD | `-46.99%` | `4,560.10` |
| `Live` | `Long` | `2.21` | 19,620,000.00 USD | 0.00 USD | 251,500.00 USD | `-46.75%` | `114,059.40` |
| `Live` | `Long` | `2.21` | 19,370,000.00 USD | 0.00 USD | 3,010.00 USD | `-46.50%` | `1,357.10` |
| `Live` | `Long` | `2.23` | 19,370,000.00 USD | 0.00 USD | 243.19 USD | `-46.26%` | `109.30` |
| `Live` | `Long` | `2.23` | 19,370,000.00 USD | 0.00 USD | 12,270.00 USD | `-46.02%` | `5,491.60` |
| `Live` | `Long` | `2.25` | 19,350,000.00 USD | 0.00 USD | 310,060.00 USD | `-45.78%` | `138,111.20` |
| `Live` | `Long` | `2.25` | 19,040,000.00 USD | 0.00 USD | 184,160.00 USD | `-45.54%` | `81,669.00` |
| `Live` | `Long` | `2.27` | 18,860,000.00 USD | 0.00 USD | 2,370.00 USD | `-45.30%` | `1,045.80` |
| `Live` | `Long` | `2.27` | 18,860,000.00 USD | 0.00 USD | 382,060.00 USD | `-45.05%` | `167,937.60` |
| `Live` | `Long` | `2.29` | 18,470,000.00 USD | 0.00 USD | 463.86 USD | `-44.81%` | `203.00` |
| `Live` | `Long` | `2.29` | 18,470,000.00 USD | 0.00 USD | 2,150.00 USD | `-44.57%` | `936.90` |
| `Live` | `Long` | `2.31` | 18,470,000.00 USD | 0.00 USD | 9,680.00 USD | `-44.33%` | `4,197.70` |
| `Live` | `Long` | `2.31` | 18,460,000.00 USD | 0.00 USD | 9,000.00 USD | `-44.09%` | `3,889.70` |
| `Live` | `Long` | `2.33` | 18,450,000.00 USD | 0.00 USD | 697.50 USD | `-43.85%` | `300.00` |
| `Live` | `Long` | `2.33` | 18,450,000.00 USD | 0.00 USD | 2,670.00 USD | `-43.61%` | `1,145.40` |
| `Live` | `Long` | `2.35` | 18,450,000.00 USD | 0.00 USD | 6,680.00 USD | `-43.36%` | `2,848.60` |
| `Live` | `Long` | `2.37` | 18,440,000.00 USD | 0.00 USD | 7,490.00 USD | `-42.88%` | `3,167.80` |
| `Live` | `Long` | `2.38` | 18,440,000.00 USD | 0.00 USD | 32,450.00 USD | `-42.64%` | `13,661.50` |
| `Live` | `Long` | `2.38` | 18,400,000.00 USD | 0.00 USD | 9,230.00 USD | `-42.40%` | `3,870.50` |
| `Live` | `Long` | `2.40` | 18,390,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-42.16%` | `766,069.90` |
| `Live` | `Long` | `2.42` | 16,560,000.00 USD | 0.00 USD | 186,030.00 USD | `-41.67%` | `77,030.20` |
| `Live` | `Long` | `2.42` | 16,370,000.00 USD | 0.00 USD | 273,060.00 USD | `-41.43%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 16,100,000.00 USD | 0.00 USD | 4,890.00 USD | `-41.19%` | `2,007.40` |
| `Live` | `Long` | `2.44` | 16,100,000.00 USD | 0.00 USD | 3,700.00 USD | `-40.95%` | `1,515.10` |
| `Live` | `Long` | `2.46` | 16,090,000.00 USD | 0.00 USD | 1,240.00 USD | `-40.71%` | `504.90` |
| `Live` | `Long` | `2.46` | 16,090,000.00 USD | 0.00 USD | 17,050.00 USD | `-40.47%` | `6,915.10` |
| `Live` | `Long` | `2.48` | 16,070,000.00 USD | 0.00 USD | 12,710.00 USD | `-40.22%` | `5,135.90` |
| `Live` | `Long` | `2.48` | 16,060,000.00 USD | 0.00 USD | 4,600.00 USD | `-39.98%` | `1,852.60` |
| `Live` | `Long` | `2.50` | 16,060,000.00 USD | 0.00 USD | 2,910.00 USD | `-39.74%` | `1,165.30` |
| `Live` | `Long` | `2.50` | 16,050,000.00 USD | 0.00 USD | 10,310.00 USD | `-39.50%` | `4,116.50` |
| `Live` | `Long` | `2.52` | 16,040,000.00 USD | 0.00 USD | 34,060.00 USD | `-39.02%` | `13,489.80` |
| `Live` | `Long` | `2.54` | 16,010,000.00 USD | 0.00 USD | 395.71 USD | `-38.78%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,010,000.00 USD | 0.00 USD | 105.36 USD | `-38.53%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,010,000.00 USD | 0.00 USD | 7,270.00 USD | `-38.29%` | `2,847.00` |
| `Live` | `Long` | `2.56` | 16,000,000.00 USD | 0.00 USD | 456,880.00 USD | `-38.05%` | `178,122.40` |
| `Live` | `Long` | `2.58` | 15,540,000.00 USD | 0.00 USD | 1,260.00 USD | `-37.81%` | `490.00` |
| `Live` | `Long` | `2.58` | 15,540,000.00 USD | 0.00 USD | 1,340.00 USD | `-37.57%` | `519.60` |
| `Live` | `Long` | `2.60` | 15,540,000.00 USD | 0.00 USD | 83,350.00 USD | `-37.33%` | `32,118.60` |
| `Live` | `Long` | `2.62` | 15,460,000.00 USD | 0.00 USD | 3,820.00 USD | `-36.84%` | `1,459.80` |
| `Live` | `Long` | `2.63` | 15,450,000.00 USD | 0.00 USD | 25,280.00 USD | `-36.36%` | `9,594.00` |
| `Live` | `Long` | `2.65` | 15,430,000.00 USD | 0.00 USD | 2,650.00 USD | `-36.12%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 15,430,000.00 USD | 0.00 USD | 20,520.00 USD | `-35.88%` | `7,730.60` |
| `Live` | `Long` | `2.67` | 15,410,000.00 USD | 0.00 USD | 7,540.00 USD | `-35.39%` | `2,819.10` |
| `Live` | `Long` | `2.69` | 15,400,000.00 USD | 0.00 USD | 5,130.00 USD | `-35.15%` | `1,911.60` |
| `Live` | `Long` | `2.69` | 15,390,000.00 USD | 0.00 USD | 733.85 USD | `-34.91%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,390,000.00 USD | 0.00 USD | 357,920.00 USD | `-34.67%` | `132,319.00` |
| `Live` | `Long` | `2.71` | 15,030,000.00 USD | 0.00 USD | 21,440.00 USD | `-34.43%` | `7,897.20` |
| `Live` | `Long` | `2.73` | 15,010,000.00 USD | 0.00 USD | 28,380.00 USD | `-34.19%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 14,980,000.00 USD | 0.00 USD | 9,400.00 USD | `-33.95%` | `3,435.70` |
| `Live` | `Long` | `2.75` | 14,980,000.00 USD | 0.00 USD | 39,690.00 USD | `-33.70%` | `14,458.30` |
| `Live` | `Long` | `2.75` | 14,940,000.00 USD | 0.00 USD | 26,770.00 USD | `-33.46%` | `9,717.40` |
| `Live` | `Long` | `2.77` | 14,910,000.00 USD | 0.00 USD | 352,610.00 USD | `-33.22%` | `127,526.20` |
| `Live` | `Long` | `2.77` | 14,560,000.00 USD | 0.00 USD | 398.77 USD | `-32.98%` | `143.70` |
| `Live` | `Long` | `2.79` | 14,560,000.00 USD | 0.00 USD | 49,740.00 USD | `-32.74%` | `17,859.80` |
| `Live` | `Long` | `2.79` | 14,510,000.00 USD | 0.00 USD | 191,910.00 USD | `-32.50%` | `68,661.50` |
| `Live` | `Long` | `2.81` | 14,310,000.00 USD | 0.00 USD | 97,490.00 USD | `-32.25%` | `34,757.40` |
| `Live` | `Long` | `2.81` | 14,220,000.00 USD | 0.00 USD | 10,010.00 USD | `-32.01%` | `3,555.20` |
| `Live` | `Long` | `2.83` | 14,210,000.00 USD | 0.00 USD | 11,350.00 USD | `-31.77%` | `4,017.50` |
| `Live` | `Long` | `2.83` | 14,200,000.00 USD | 0.00 USD | 24,770.00 USD | `-31.53%` | `8,736.40` |
| `Live` | `Long` | `2.85` | 14,170,000.00 USD | 0.00 USD | 8,780.00 USD | `-31.29%` | `3,084.70` |
| `Live` | `Long` | `2.85` | 14,160,000.00 USD | 0.00 USD | 2,580,000.00 USD | `-31.05%` | `902,328.30` |
| `Live` | `Long` | `2.87` | 11,590,000.00 USD | 0.00 USD | 9,150.00 USD | `-30.81%` | `3,193.80` |
| `Live` | `Long` | `2.88` | 11,580,000.00 USD | 0.00 USD | 475,530.00 USD | `-30.56%` | `165,401.50` |
| `Live` | `Long` | `2.88` | 11,100,000.00 USD | 0.00 USD | 18,230.00 USD | `-30.32%` | `6,320.30` |
| `Live` | `Long` | `2.90` | 11,080,000.00 USD | 0.00 USD | 14,200.00 USD | `-30.08%` | `4,904.40` |
| `Live` | `Long` | `2.90` | 11,070,000.00 USD | 0.00 USD | 14,830.00 USD | `-29.84%` | `5,103.40` |
| `Live` | `Long` | `2.92` | 11,050,000.00 USD | 0.00 USD | 82,440.00 USD | `-29.60%` | `28,282.50` |
| `Live` | `Long` | `2.92` | 10,970,000.00 USD | 0.00 USD | 49,180.00 USD | `-29.36%` | `16,814.40` |
| `Live` | `Long` | `2.94` | 10,920,000.00 USD | 0.00 USD | 431,620.00 USD | `-29.11%` | `147,058.90` |
| `Live` | `Long` | `2.94` | 10,490,000.00 USD | 0.00 USD | 50,830.00 USD | `-28.87%` | `17,261.00` |
| `Live` | `Long` | `2.96` | 10,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-28.63%` | `372.30` |
| `Live` | `Long` | `2.96` | 10,440,000.00 USD | 0.00 USD | 5,090.00 USD | `-28.39%` | `1,717.90` |
| `Live` | `Long` | `2.98` | 10,430,000.00 USD | 0.00 USD | 37,560.00 USD | `-28.15%` | `12,626.10` |
| `Live` | `Long` | `2.98` | 10,400,000.00 USD | 0.00 USD | 178,230.00 USD | `-27.91%` | `59,709.80` |
| `Live` | `Long` | `3.00` | 10,220,000.00 USD | 0.00 USD | 8,090.00 USD | `-27.67%` | `2,701.70` |
| `Live` | `Long` | `3.00` | 10,210,000.00 USD | 0.00 USD | 11,020.00 USD | `-27.42%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 10,200,000.00 USD | 0.00 USD | 21,490.00 USD | `-27.18%` | `7,128.10` |
| `Live` | `Long` | `3.02` | 10,180,000.00 USD | 0.00 USD | 31,230.00 USD | `-26.94%` | `10,322.50` |
| `Live` | `Long` | `3.04` | 10,150,000.00 USD | 0.00 USD | 1,020.00 USD | `-26.70%` | `335.50` |
| `Live` | `Long` | `3.04` | 10,150,000.00 USD | 0.00 USD | 168,030.00 USD | `-26.46%` | `55,183.00` |
| `Live` | `Long` | `3.06` | 9,980,000.00 USD | 0.00 USD | 178,920.00 USD | `-26.22%` | `58,567.00` |
| `Live` | `Long` | `3.06` | 9,800,000.00 USD | 0.00 USD | 115,550.00 USD | `-25.98%` | `37,700.70` |
| `Live` | `Long` | `3.08` | 9,680,000.00 USD | 0.00 USD | 125,140.00 USD | `-25.73%` | `40,695.80` |
| `Live` | `Long` | `3.08` | 9,560,000.00 USD | 0.00 USD | 7,660.00 USD | `-25.49%` | `2,484.40` |
| `Live` | `Long` | `3.10` | 9,550,000.00 USD | 0.00 USD | 7,660.00 USD | `-25.25%` | `2,473.60` |
| `Live` | `Long` | `3.10` | 9,540,000.00 USD | 0.00 USD | 17,000.00 USD | `-25.01%` | `5,476.00` |
| `Live` | `Long` | `3.12` | 9,530,000.00 USD | 0.00 USD | 31,130.00 USD | `-24.77%` | `9,992.50` |
| `Live` | `Long` | `3.12` | 9,490,000.00 USD | 0.00 USD | 7,930.00 USD | `-24.53%` | `2,537.20` |
| `Live` | `Long` | `3.13` | 9,490,000.00 USD | 0.00 USD | 9,280.00 USD | `-24.28%` | `2,961.00` |
| `Live` | `Long` | `3.15` | 9,480,000.00 USD | 0.00 USD | 23,000.00 USD | `-24.04%` | `7,314.70` |
| `Live` | `Long` | `3.15` | 9,450,000.00 USD | 0.00 USD | 25,240.00 USD | `-23.80%` | `8,000.00` |
| `Live` | `Long` | `3.17` | 9,430,000.00 USD | 0.00 USD | 12,840.00 USD | `-23.56%` | `4,056.10` |
| `Live` | `Long` | `3.17` | 9,420,000.00 USD | 0.00 USD | 57,760.00 USD | `-23.32%` | `18,191.20` |
| `Live` | `Long` | `3.19` | 9,360,000.00 USD | 0.00 USD | 249,290.00 USD | `-23.08%` | `78,269.80` |
| `Live` | `Long` | `3.19` | 9,110,000.00 USD | 0.00 USD | 219.50 USD | `-22.84%` | `68.70` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 4,010.00 USD | `-22.59%` | `1,251.10` |
| `Live` | `Long` | `3.21` | 9,100,000.00 USD | 0.00 USD | 13,530.00 USD | `-22.35%` | `4,208.60` |
| `Live` | `Long` | `3.23` | 9,090,000.00 USD | 0.00 USD | 31,660.00 USD | `-22.11%` | `9,815.60` |
| `Live` | `Long` | `3.23` | 9,060,000.00 USD | 0.00 USD | 56,080.00 USD | `-21.87%` | `17,335.30` |
| `Live` | `Long` | `3.25` | 9,000,000.00 USD | 0.00 USD | 20,130.00 USD | `-21.63%` | `6,204.10` |
| `Live` | `Long` | `3.25` | 8,980,000.00 USD | 0.00 USD | 5,640.00 USD | `-21.39%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 8,980,000.00 USD | 0.00 USD | 51,010.00 USD | `-21.14%` | `15,622.30` |
| `Live` | `Long` | `3.27` | 8,930,000.00 USD | 0.00 USD | 874,570.00 USD | `-20.90%` | `267,044.10` |
| `Live` | `Long` | `3.29` | 8,050,000.00 USD | 0.00 USD | 19,440.00 USD | `-20.66%` | `5,916.40` |
| `Live` | `Long` | `3.29` | 8,030,000.00 USD | 0.00 USD | 133,000.00 USD | `-20.42%` | `40,362.70` |
| `Live` | `Long` | `3.31` | 7,900,000.00 USD | 0.00 USD | 131,270.00 USD | `-20.18%` | `39,719.70` |
| `Live` | `Long` | `3.31` | 7,770,000.00 USD | 0.00 USD | 17,060.00 USD | `-19.94%` | `5,145.10` |
| `Live` | `Long` | `3.33` | 7,750,000.00 USD | 0.00 USD | 20,150.00 USD | `-19.70%` | `6,061.00` |
| `Live` | `Long` | `3.33` | 7,730,000.00 USD | 0.00 USD | 73,060.00 USD | `-19.45%` | `21,908.00` |
| `Live` | `Long` | `3.35` | 7,660,000.00 USD | 0.00 USD | 27,160.00 USD | `-19.21%` | `8,119.40` |
| `Live` | `Long` | `3.35` | 7,630,000.00 USD | 0.00 USD | 1,780.00 USD | `-18.97%` | `531.00` |
| `Live` | `Long` | `3.37` | 7,630,000.00 USD | 0.00 USD | 24,580.00 USD | `-18.73%` | `7,305.80` |
| `Live` | `Long` | `3.38` | 7,600,000.00 USD | 0.00 USD | 191,940.00 USD | `-18.49%` | `56,870.10` |
| `Live` | `Long` | `3.38` | 7,410,000.00 USD | 0.00 USD | 44,790.00 USD | `-18.25%` | `13,232.00` |
| `Live` | `Long` | `3.40` | 7,370,000.00 USD | 0.00 USD | 888.47 USD | `-18.01%` | `261.70` |
| `Live` | `Long` | `3.40` | 7,370,000.00 USD | 0.00 USD | 98,820.00 USD | `-17.76%` | `29,022.40` |
| `Live` | `Long` | `3.42` | 7,270,000.00 USD | 0.00 USD | 415,990.00 USD | `-17.52%` | `121,813.20` |
| `Live` | `Long` | `3.42` | 6,850,000.00 USD | 0.00 USD | 28,690.00 USD | `-17.28%` | `8,375.70` |
| `Live` | `Long` | `3.44` | 6,820,000.00 USD | 0.00 USD | 33,630.00 USD | `-17.04%` | `9,789.70` |
| `Live` | `Long` | `3.44` | 6,790,000.00 USD | 0.00 USD | 21,620.00 USD | `-16.80%` | `6,275.80` |
| `Live` | `Long` | `3.46` | 6,770,000.00 USD | 0.00 USD | 12,040.00 USD | `-16.56%` | `3,485.50` |
| `Live` | `Long` | `3.46` | 6,760,000.00 USD | 0.00 USD | 14,380.00 USD | `-16.31%` | `4,150.10` |
| `Live` | `Long` | `3.48` | 6,740,000.00 USD | 0.00 USD | 197,260.00 USD | `-16.07%` | `56,765.10` |
| `Live` | `Long` | `3.48` | 6,540,000.00 USD | 0.00 USD | 29,090.00 USD | `-15.83%` | `8,347.40` |
| `Live` | `Long` | `3.50` | 6,520,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-15.59%` | `378,131.30` |
| `Live` | `Long` | `3.50` | 5,190,000.00 USD | 0.00 USD | 35,120.00 USD | `-15.35%` | `10,019.80` |
| `Live` | `Long` | `3.52` | 5,160,000.00 USD | 0.00 USD | 37,770.00 USD | `-15.11%` | `10,746.00` |
| `Live` | `Long` | `3.52` | 5,120,000.00 USD | 0.00 USD | 195,120.00 USD | `-14.87%` | `55,353.30` |
| `Live` | `Long` | `3.54` | 4,930,000.00 USD | 0.00 USD | 120,780.00 USD | `-14.62%` | `34,168.00` |
| `Live` | `Long` | `3.54` | 4,800,000.00 USD | 0.00 USD | 167,840.00 USD | `-14.38%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 4,640,000.00 USD | 0.00 USD | 374,310.00 USD | `-14.14%` | `105,290.00` |
| `Live` | `Long` | `3.56` | 4,260,000.00 USD | 0.00 USD | 9,160.00 USD | `-13.90%` | `2,569.10` |
| `Live` | `Long` | `3.58` | 4,250,000.00 USD | 0.00 USD | 61,480.00 USD | `-13.66%` | `17,196.70` |
| `Live` | `Long` | `3.58` | 4,190,000.00 USD | 0.00 USD | 33,150.00 USD | `-13.42%` | `9,246.50` |
| `Live` | `Long` | `3.60` | 4,160,000.00 USD | 0.00 USD | 109,830.00 USD | `-13.17%` | `30,549.80` |
| `Live` | `Long` | `3.60` | 4,050,000.00 USD | 0.00 USD | 60,200.00 USD | `-12.93%` | `16,699.70` |
| `Live` | `Long` | `3.62` | 3,990,000.00 USD | 0.00 USD | 16,360.00 USD | `-12.69%` | `4,526.20` |
| `Live` | `Long` | `3.62` | 3,970,000.00 USD | 0.00 USD | 125,710.00 USD | `-12.45%` | `34,678.60` |
| `Live` | `Long` | `3.63` | 3,850,000.00 USD | 0.00 USD | 230,840.00 USD | `-12.21%` | `63,504.80` |
| `Live` | `Long` | `3.65` | 3,620,000.00 USD | 0.00 USD | 19,580.00 USD | `-11.97%` | `5,371.80` |
| `Live` | `Long` | `3.65` | 3,600,000.00 USD | 0.00 USD | 12,700.00 USD | `-11.73%` | `3,474.60` |
| `Live` | `Long` | `3.67` | 3,580,000.00 USD | 0.00 USD | 56,050.00 USD | `-11.48%` | `15,293.30` |
| `Live` | `Long` | `3.67` | 3,530,000.00 USD | 0.00 USD | 99,010.00 USD | `-11.24%` | `26,942.70` |
| `Live` | `Long` | `3.69` | 3,430,000.00 USD | 0.00 USD | 287,470.00 USD | `-11.00%` | `78,011.80` |
| `Live` | `Long` | `3.69` | 3,140,000.00 USD | 0.00 USD | 94,330.00 USD | `-10.76%` | `25,529.50` |
| `Live` | `Long` | `3.71` | 3,050,000.00 USD | 0.00 USD | 212,700.00 USD | `-10.52%` | `57,408.40` |
| `Live` | `Long` | `3.71` | 2,830,000.00 USD | 0.00 USD | 72,730.00 USD | `-10.28%` | `19,577.00` |
| `Live` | `Long` | `3.73` | 2,760,000.00 USD | 0.00 USD | 224,660.00 USD | `-10.04%` | `60,310.30` |
| `Live` | `Long` | `3.73` | 2,540,000.00 USD | 0.00 USD | 122,190.00 USD | `-9.79%` | `32,714.50` |
| `Live` | `Long` | `3.75` | 2,410,000.00 USD | 0.00 USD | 39,750.00 USD | `-9.55%` | `10,614.40` |
| `Live` | `Long` | `3.75` | 2,370,000.00 USD | 0.00 USD | 201,260.00 USD | `-9.31%` | `53,596.90` |
| `Live` | `Long` | `3.77` | 2,170,000.00 USD | 0.00 USD | 60,660.00 USD | `-9.07%` | `16,112.30` |
| `Live` | `Long` | `3.77` | 2,110,000.00 USD | 0.00 USD | 64,270.00 USD | `-8.83%` | `17,024.00` |
| `Live` | `Long` | `3.79` | 2,050,000.00 USD | 0.00 USD | 31,540.00 USD | `-8.59%` | `8,334.20` |
| `Live` | `Long` | `3.79` | 2,020,000.00 USD | 0.00 USD | 137,950.00 USD | `-8.34%` | `36,351.50` |
| `Live` | `Long` | `3.81` | 1,880,000.00 USD | 0.00 USD | 456,920.00 USD | `-8.10%` | `120,083.60` |
| `Live` | `Long` | `3.81` | 1,420,000.00 USD | 0.00 USD | 100,730.00 USD | `-7.86%` | `26,403.80` |
| `Live` | `Long` | `3.83` | 1,320,000.00 USD | 0.00 USD | 161,990.00 USD | `-7.62%` | `42,351.30` |
| `Live` | `Long` | `3.83` | 1,160,000.00 USD | 0.00 USD | 198,060.00 USD | `-7.38%` | `51,646.10` |
| `Live` | `Long` | `3.85` | 961,300.00 USD | 0.00 USD | 123,400.00 USD | `-7.14%` | `32,093.40` |
| `Live` | `Long` | `3.85` | 837,910.00 USD | 0.00 USD | 81,300.00 USD | `-6.90%` | `21,090.60` |
| `Live` | `Long` | `3.87` | 756,600.00 USD | 0.00 USD | 33,810.00 USD | `-6.65%` | `8,747.40` |
| `Live` | `Long` | `3.88` | 722,790.00 USD | 0.00 USD | 29,390.00 USD | `-6.41%` | `7,584.20` |
| `Live` | `Long` | `3.88` | 693,400.00 USD | 0.00 USD | 238,510.00 USD | `-6.17%` | `61,393.20` |
| `Live` | `Long` | `3.90` | 454,890.00 USD | 0.00 USD | 99,530.00 USD | `-5.93%` | `25,552.90` |
| `Live` | `Long` | `3.90` | 355,360.00 USD | 0.00 USD | 6,110.00 USD | `-5.69%` | `1,563.70` |
| `Live` | `Long` | `3.92` | 349,260.00 USD | 0.00 USD | 161,730.00 USD | `-5.45%` | `41,309.30` |
| `Live` | `Long` | `3.92` | 187,530.00 USD | 0.00 USD | 304.58 USD | `-5.20%` | `77.60` |
| `Live` | `Long` | `3.94` | 187,230.00 USD | 0.00 USD | 6,340.00 USD | `-4.96%` | `1,611.10` |
| `Live` | `Long` | `3.94` | 180,890.00 USD | 0.00 USD | 147,750.00 USD | `-4.72%` | `37,452.60` |
| `Live` | `Long` | `3.98` | 33,140.00 USD | 0.00 USD | 33,140.00 USD | `-4.00%` | `8,336.10` |
| `Live` | `Short` | `4.14` | 90,630.00 USD | 90,630.00 USD | 0.00 USD | `+0.11%` | `21,865.20` |
| `Live` | `Short` | `4.17` | 100,670.00 USD | 10,040.00 USD | 0.00 USD | `+0.83%` | `2,404.60` |
| `Live` | `Short` | `4.18` | 102,220.00 USD | 1,550.00 USD | 0.00 USD | `+1.07%` | `370.20` |
| `Live` | `Short` | `4.20` | 102,480.00 USD | 261.35 USD | 0.00 USD | `+1.32%` | `62.30` |
| `Live` | `Short` | `4.21` | 106,580.00 USD | 4,100.00 USD | 0.00 USD | `+1.56%` | `975.40` |
| `Live` | `Short` | `4.21` | 107,420.00 USD | 837.10 USD | 0.00 USD | `+1.80%` | `198.60` |
| `Live` | `Short` | `4.22` | 107,590.00 USD | 165.62 USD | 0.00 USD | `+2.04%` | `39.20` |
| `Live` | `Short` | `4.24` | 125,690.00 USD | 18,110.00 USD | 0.00 USD | `+2.28%` | `4,275.50` |
| `Live` | `Short` | `4.25` | 125,990.00 USD | 296.30 USD | 0.00 USD | `+2.52%` | `69.80` |
| `Live` | `Short` | `4.26` | 185,300.00 USD | 59,310.00 USD | 0.00 USD | `+3.01%` | `13,906.10` |
| `Live` | `Short` | `4.29` | 185,460.00 USD | 163.69 USD | 0.00 USD | `+3.49%` | `38.20` |
| `Live` | `Short` | `4.29` | 396,190.00 USD | 210,730.00 USD | 0.00 USD | `+3.73%` | `49,064.30` |
| `Live` | `Short` | `4.30` | 402,540.00 USD | 6,350.00 USD | 0.00 USD | `+3.97%` | `1,475.50` |
| `Live` | `Short` | `4.32` | 440,290.00 USD | 37,740.00 USD | 0.00 USD | `+4.21%` | `8,746.80` |
| `Live` | `Short` | `4.33` | 440,520.00 USD | 230.52 USD | 0.00 USD | `+4.46%` | `53.30` |
| `Live` | `Short` | `4.34` | 444,640.00 USD | 4,130.00 USD | 0.00 USD | `+4.94%` | `949.40` |
| `Live` | `Short` | `4.36` | 446,940.00 USD | 2,290.00 USD | 0.00 USD | `+5.18%` | `526.70` |
| `Live` | `Short` | `4.37` | 447,360.00 USD | 423.84 USD | 0.00 USD | `+5.42%` | `97.10` |
| `Live` | `Short` | `4.38` | 454,300.00 USD | 6,940.00 USD | 0.00 USD | `+5.66%` | `1,586.30` |
| `Live` | `Short` | `4.38` | 454,500.00 USD | 203.90 USD | 0.00 USD | `+5.91%` | `46.50` |
| `Live` | `Short` | `4.39` | 647,210.00 USD | 192,710.00 USD | 0.00 USD | `+6.15%` | `43,846.50` |
| `Live` | `Short` | `4.41` | 648,620.00 USD | 1,410.00 USD | 0.00 USD | `+6.39%` | `319.80` |
| `Live` | `Short` | `4.42` | 649,290.00 USD | 671.71 USD | 0.00 USD | `+6.87%` | `151.80` |
| `Live` | `Short` | `4.46` | 649,760.00 USD | 468.38 USD | 0.00 USD | `+7.84%` | `104.90` |
| `Live` | `Short` | `4.47` | 650,390.00 USD | 629.18 USD | 0.00 USD | `+8.08%` | `140.60` |
| `Live` | `Short` | `4.50` | 650,670.00 USD | 280.49 USD | 0.00 USD | `+8.56%` | `62.40` |
| `Live` | `Short` | `4.50` | 650,950.00 USD | 283.81 USD | 0.00 USD | `+8.80%` | `63.00` |
| `Live` | `Short` | `4.51` | 651,340.00 USD | 389.19 USD | 0.00 USD | `+9.04%` | `86.20` |
| `Live` | `Short` | `4.53` | 670,170.00 USD | 18,820.00 USD | 0.00 USD | `+9.29%` | `4,160.10` |
| `Live` | `Short` | `4.54` | 670,560.00 USD | 394.51 USD | 0.00 USD | `+9.77%` | `86.80` |
| `Live` | `Short` | `4.58` | 685,250.00 USD | 14,690.00 USD | 0.00 USD | `+10.49%` | `3,211.90` |
| `Live` | `Short` | `4.61` | 686,300.00 USD | 1,050.00 USD | 0.00 USD | `+11.22%` | `227.10` |
| `Live` | `Short` | `4.63` | 687,290.00 USD | 990.04 USD | 0.00 USD | `+11.94%` | `213.60` |
| `Live` | `Short` | `4.64` | 687,430.00 USD | 143.07 USD | 0.00 USD | `+12.18%` | `30.80` |
| `Live` | `Short` | `4.66` | 687,560.00 USD | 124.75 USD | 0.00 USD | `+12.43%` | `26.80` |
| `Live` | `Short` | `4.67` | 687,660.00 USD | 101.70 USD | 0.00 USD | `+12.67%` | `21.80` |
| `Live` | `Short` | `4.68` | 839,130.00 USD | 151,470.00 USD | 0.00 USD | `+13.15%` | `32,330.80` |
| `Live` | `Short` | `4.70` | 839,360.00 USD | 230.06 USD | 0.00 USD | `+13.39%` | `49.00` |
| `Live` | `Short` | `4.71` | 846,840.00 USD | 7,480.00 USD | 0.00 USD | `+13.63%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 847,090.00 USD | 250.37 USD | 0.00 USD | `+13.88%` | `53.10` |
| `Live` | `Short` | `4.78` | 859,930.00 USD | 12,840.00 USD | 0.00 USD | `+15.32%` | `2,689.00` |
| `Live` | `Short` | `4.79` | 860,080.00 USD | 143.55 USD | 0.00 USD | `+15.57%` | `30.00` |
| `Live` | `Short` | `4.79` | 861,410.00 USD | 1,330.00 USD | 0.00 USD | `+15.81%` | `277.70` |
| `Live` | `Short` | `4.83` | 863,150.00 USD | 1,740.00 USD | 0.00 USD | `+16.53%` | `360.90` |
| `Live` | `Short` | `4.83` | 865,100.00 USD | 1,950.00 USD | 0.00 USD | `+16.77%` | `403.60` |
| `Live` | `Short` | `4.84` | 876,320.00 USD | 11,220.00 USD | 0.00 USD | `+17.01%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 876,460.00 USD | 137.68 USD | 0.00 USD | `+17.50%` | `28.30` |
| `Live` | `Short` | `4.88` | 877,290.00 USD | 827.03 USD | 0.00 USD | `+17.98%` | `169.30` |
| `Live` | `Short` | `4.92` | 898,000.00 USD | 20,720.00 USD | 0.00 USD | `+18.71%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 900,100.00 USD | 2,100.00 USD | 0.00 USD | `+18.95%` | `425.70` |
| `Live` | `Short` | `4.93` | 900,260.00 USD | 157.43 USD | 0.00 USD | `+19.19%` | `31.90` |
| `Live` | `Short` | `4.96` | 900,600.00 USD | 342.89 USD | 0.00 USD | `+19.67%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,040,000.00 USD | 135,500.00 USD | 0.00 USD | `+20.15%` | `27,236.50` |
| `Live` | `Short` | `5.00` | 1,040,000.00 USD | 339.66 USD | 0.00 USD | `+20.64%` | `68.00` |
| `Live` | `Short` | `5.05` | 1,070,000.00 USD | 35,380.00 USD | 0.00 USD | `+22.09%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,080,000.00 USD | 3,420.00 USD | 0.00 USD | `+22.33%` | `675.80` |
| `Live` | `Short` | `5.12` | 1,080,000.00 USD | 2,560.00 USD | 0.00 USD | `+23.78%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,080,000.00 USD | 751.51 USD | 0.00 USD | `+24.74%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,080,000.00 USD | 1,190.00 USD | 0.00 USD | `+25.47%` | `229.00` |
| `Live` | `Short` | `5.21` | 1,080,000.00 USD | 2,610.00 USD | 0.00 USD | `+25.95%` | `500.00` |
| `Live` | `Short` | `5.22` | 1,150,000.00 USD | 72,110.00 USD | 0.00 USD | `+26.19%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 1,150,000.00 USD | 143.71 USD | 0.00 USD | `+26.68%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,150,000.00 USD | 288.50 USD | 0.00 USD | `+26.92%` | `54.90` |
| `Live` | `Short` | `5.26` | 1,160,000.00 USD | 6,220.00 USD | 0.00 USD | `+27.16%` | `1,181.40` |
| `Live` | `Short` | `5.29` | 1,160,000.00 USD | 134.77 USD | 0.00 USD | `+27.64%` | `25.50` |
| `Live` | `Short` | `5.29` | 1,180,000.00 USD | 21,300.00 USD | 0.00 USD | `+27.88%` | `4,022.20` |
| `Live` | `Short` | `5.30` | 2,240,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+28.12%` | `200,098.90` |
| `Live` | `Short` | `5.32` | 2,300,000.00 USD | 59,660.00 USD | 0.00 USD | `+28.37%` | `11,223.90` |
| `Live` | `Short` | `5.33` | 2,310,000.00 USD | 1,710.00 USD | 0.00 USD | `+28.85%` | `320.50` |
| `Live` | `Short` | `5.36` | 2,310,000.00 USD | 142.44 USD | 0.00 USD | `+29.33%` | `26.60` |
| `Live` | `Short` | `5.39` | 2,310,000.00 USD | 3,900.00 USD | 0.00 USD | `+30.30%` | `722.10` |
| `Live` | `Short` | `5.41` | 2,310,000.00 USD | 5,410.00 USD | 0.00 USD | `+30.54%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 2,320,000.00 USD | 419.04 USD | 0.00 USD | `+31.26%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,610,000.00 USD | 296,230.00 USD | 0.00 USD | `+32.23%` | `54,106.20` |
| `Live` | `Short` | `5.50` | 2,680,000.00 USD | 66,470.00 USD | 0.00 USD | `+32.71%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,720,000.00 USD | 38,800.00 USD | 0.00 USD | `+33.20%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 2,720,000.00 USD | 209.22 USD | 0.00 USD | `+33.68%` | `37.80` |
| `Live` | `Short` | `5.54` | 4,310,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+33.92%` | `288,027.90` |
| `Live` | `Short` | `5.55` | 4,370,000.00 USD | 55,550.00 USD | 0.00 USD | `+34.16%` | `10,000.00` |
| `Live` | `Short` | `5.57` | 4,380,000.00 USD | 8,670.00 USD | 0.00 USD | `+34.40%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,440,000.00 USD | 62,580.00 USD | 0.00 USD | `+34.89%` | `11,205.20` |
| `Live` | `Short` | `5.59` | 4,440,000.00 USD | 686.51 USD | 0.00 USD | `+35.13%` | `122.70` |
| `Live` | `Short` | `5.63` | 4,510,000.00 USD | 63,960.00 USD | 0.00 USD | `+36.09%` | `11,349.70` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 211.30 USD | 0.00 USD | `+36.82%` | `37.30` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 228.70 USD | 0.00 USD | `+37.06%` | `40.30` |
| `Live` | `Short` | `5.68` | 4,910,000.00 USD | 405,140.00 USD | 0.00 USD | `+37.30%` | `71,265.40` |
| `Live` | `Short` | `5.70` | 4,910,000.00 USD | 1,520.00 USD | 0.00 USD | `+37.54%` | `267.40` |
| `Live` | `Short` | `5.71` | 4,910,000.00 USD | 2,130.00 USD | 0.00 USD | `+38.03%` | `372.40` |
| `Live` | `Short` | `5.75` | 4,920,000.00 USD | 4,580.00 USD | 0.00 USD | `+38.75%` | `796.90` |
| `Live` | `Short` | `5.75` | 4,920,000.00 USD | 286.02 USD | 0.00 USD | `+38.99%` | `49.70` |
| `Live` | `Short` | `5.76` | 4,920,000.00 USD | 148.16 USD | 0.00 USD | `+39.23%` | `25.70` |
| `Live` | `Short` | `5.78` | 4,920,000.00 USD | 670.48 USD | 0.00 USD | `+39.48%` | `116.10` |
| `Live` | `Short` | `5.79` | 4,920,000.00 USD | 2,680.00 USD | 0.00 USD | `+39.96%` | `463.10` |
| `Live` | `Short` | `5.83` | 5,260,000.00 USD | 337,490.00 USD | 0.00 USD | `+40.68%` | `57,938.40` |
| `Live` | `Short` | `5.84` | 5,260,000.00 USD | 439.54 USD | 0.00 USD | `+41.17%` | `75.20` |
| `Live` | `Short` | `5.86` | 5,260,000.00 USD | 848.39 USD | 0.00 USD | `+41.41%` | `144.90` |
| `Live` | `Short` | `5.87` | 5,260,000.00 USD | 200.00 USD | 0.00 USD | `+41.65%` | `34.10` |
| `Live` | `Short` | `5.88` | 5,270,000.00 USD | 7,150.00 USD | 0.00 USD | `+42.13%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,360,000.00 USD | 88,590.00 USD | 0.00 USD | `+42.37%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,360,000.00 USD | 189.28 USD | 0.00 USD | `+42.86%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,740,000.00 USD | 378,490.00 USD | 0.00 USD | `+43.58%` | `63,665.50` |
| `Live` | `Short` | `6.03` | 6,080,000.00 USD | 345,420.00 USD | 0.00 USD | `+45.51%` | `57,330.80` |
| `Live` | `Short` | `6.07` | 6,080,000.00 USD | 740.54 USD | 0.00 USD | `+46.48%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,090,000.00 USD | 5,920.00 USD | 0.00 USD | `+46.96%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,130,000.00 USD | 37,510.00 USD | 0.00 USD | `+47.20%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 6,130,000.00 USD | 2,430.00 USD | 0.00 USD | `+48.17%` | `396.10` |
| `Live` | `Short` | `6.20` | 6,130,000.00 USD | 1,890.00 USD | 0.00 USD | `+49.62%` | `305.00` |
| `Live` | `Short` | `6.25` | 6,140,000.00 USD | 7,300.00 USD | 0.00 USD | `+50.83%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,140,000.00 USD | 439.10 USD | 0.00 USD | `+51.07%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,140,000.00 USD | 397.84 USD | 0.00 USD | `+51.55%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,140,000.00 USD | 310.70 USD | 0.00 USD | `+52.52%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,150,000.00 USD | 14,150.00 USD | 0.00 USD | `+52.76%` | `2,237.40` |
| `Live` | `Short` | `6.33` | 6,150,000.00 USD | 382.00 USD | 0.00 USD | `+53.00%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,150,000.00 USD | 214.46 USD | 0.00 USD | `+53.24%` | `33.80` |
| `Live` | `Short` | `6.37` | 6,180,000.00 USD | 24,830.00 USD | 0.00 USD | `+53.73%` | `3,901.70` |
| `Live` | `Short` | `6.38` | 6,180,000.00 USD | 288.15 USD | 0.00 USD | `+53.97%` | `45.20` |
| `Live` | `Short` | `6.38` | 6,180,000.00 USD | 2,000.00 USD | 0.00 USD | `+54.21%` | `312.80` |
| `Live` | `Short` | `6.39` | 6,440,000.00 USD | 261,360.00 USD | 0.00 USD | `+54.45%` | `40,869.30` |
| `Live` | `Short` | `6.41` | 6,450,000.00 USD | 5,760.00 USD | 0.00 USD | `+54.69%` | `899.50` |
| `Live` | `Short` | `6.42` | 6,460,000.00 USD | 8,700.00 USD | 0.00 USD | `+54.93%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,460,000.00 USD | 173.47 USD | 0.00 USD | `+55.17%` | `27.00` |
| `Live` | `Short` | `6.43` | 6,530,000.00 USD | 77,220.00 USD | 0.00 USD | `+55.42%` | `12,000.00` |
| `Live` | `Short` | `6.45` | 6,540,000.00 USD | 5,270.00 USD | 0.00 USD | `+55.66%` | `818.40` |
| `Live` | `Short` | `6.46` | 6,550,000.00 USD | 7,150.00 USD | 0.00 USD | `+55.90%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 6,550,000.00 USD | 1,940.00 USD | 0.00 USD | `+56.14%` | `300.00` |
| `Live` | `Short` | `6.50` | 6,550,000.00 USD | 5,550.00 USD | 0.00 USD | `+57.11%` | `852.80` |
| `Live` | `Short` | `6.51` | 7,780,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+57.35%` | `188,058.40` |
| `Live` | `Short` | `6.54` | 7,820,000.00 USD | 40,450.00 USD | 0.00 USD | `+57.83%` | `6,190.00` |
| `Live` | `Short` | `6.54` | 7,820,000.00 USD | 265.07 USD | 0.00 USD | `+58.07%` | `40.50` |
| `Live` | `Short` | `6.55` | 7,870,000.00 USD | 51,310.00 USD | 0.00 USD | `+58.31%` | `7,827.40` |
| `Live` | `Short` | `6.59` | 7,870,000.00 USD | 418.78 USD | 0.00 USD | `+59.28%` | `63.50` |
| `Live` | `Short` | `6.61` | 7,960,000.00 USD | 88,290.00 USD | 0.00 USD | `+59.52%` | `13,367.10` |
| `Live` | `Short` | `6.66` | 37,960,000.00 USD | 30,000,000.00 USD | 0.00 USD | `+60.73%` | `4,508,349.40` |
| `Live` | `Short` | `6.67` | 37,960,000.00 USD | 233.94 USD | 0.00 USD | `+60.97%` | `35.10` |
| `Live` | `Short` | `6.67` | 37,960,000.00 USD | 200.25 USD | 0.00 USD | `+61.21%` | `30.00` |
| `Live` | `Short` | `6.70` | 37,970,000.00 USD | 9,270.00 USD | 0.00 USD | `+61.70%` | `1,384.00` |
| `Live` | `Short` | `6.72` | 38,010,000.00 USD | 37,370.00 USD | 0.00 USD | `+62.42%` | `5,556.90` |
| `Live` | `Short` | `6.74` | 38,010,000.00 USD | 946.94 USD | 0.00 USD | `+62.66%` | `140.60` |
| `Live` | `Short` | `6.75` | 39,260,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+63.14%` | `184,607.10` |
| `Live` | `Short` | `6.82` | 39,260,000.00 USD | 187.41 USD | 0.00 USD | `+64.59%` | `27.50` |
| `Live` | `Short` | `6.84` | 39,260,000.00 USD | 2,460.00 USD | 0.00 USD | `+65.32%` | `360.10` |
| `Live` | `Short` | `6.87` | 39,260,000.00 USD | 2,650.00 USD | 0.00 USD | `+65.80%` | `386.60` |
| `Live` | `Short` | `6.92` | 39,270,000.00 USD | 6,920.00 USD | 0.00 USD | `+67.25%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 39,270,000.00 USD | 664.27 USD | 0.00 USD | `+68.70%` | `95.10` |
| `Live` | `Short` | `7.03` | 39,270,000.00 USD | 665.27 USD | 0.00 USD | `+69.67%` | `94.70` |
| `Live` | `Short` | `7.05` | 39,270,000.00 USD | 559.46 USD | 0.00 USD | `+70.39%` | `79.30` |
| `Live` | `Short` | `7.09` | 39,270,000.00 USD | 699.57 USD | 0.00 USD | `+71.36%` | `98.60` |
| `Live` | `Short` | `7.21` | 39,290,000.00 USD | 13,560.00 USD | 0.00 USD | `+74.25%` | `1,879.60` |
| `Live` | `Short` | `7.22` | 43,120,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+74.50%` | `531,000.00` |
| `Live` | `Short` | `7.24` | 43,130,000.00 USD | 4,910.00 USD | 0.00 USD | `+74.74%` | `679.30` |
| `Live` | `Short` | `7.28` | 43,130,000.00 USD | 3,500.00 USD | 0.00 USD | `+75.70%` | `481.50` |
| `Live` | `Short` | `7.33` | 43,130,000.00 USD | 1,320.00 USD | 0.00 USD | `+77.15%` | `180.00` |
| `Live` | `Short` | `7.38` | 43,130,000.00 USD | 773.95 USD | 0.00 USD | `+78.36%` | `104.80` |
| `Live` | `Short` | `7.43` | 43,240,000.00 USD | 106,150.00 USD | 0.00 USD | `+79.57%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 43,240,000.00 USD | 1,420.00 USD | 0.00 USD | `+80.05%` | `191.10` |
| `Live` | `Short` | `7.46` | 53,220,000.00 USD | 9,970,000.00 USD | 0.00 USD | `+80.29%` | `1,336,211.30` |
| `Live` | `Short` | `7.49` | 61,010,000.00 USD | 7,800,000.00 USD | 0.00 USD | `+80.78%` | `1,041,428.80` |
| `Live` | `Short` | `7.53` | 61,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+81.74%` | `208.40` |
| `Live` | `Short` | `7.62` | 61,020,000.00 USD | 3,350.00 USD | 0.00 USD | `+83.91%` | `439.40` |
| `Live` | `Short` | `7.63` | 61,030,000.00 USD | 19,210.00 USD | 0.00 USD | `+84.40%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 61,040,000.00 USD | 360.25 USD | 0.00 USD | `+85.12%` | `47.00` |
| `Live` | `Short` | `7.67` | 61,040,000.00 USD | 6,100.00 USD | 0.00 USD | `+85.36%` | `794.40` |
| `Live` | `Short` | `7.72` | 61,040,000.00 USD | 259.56 USD | 0.00 USD | `+86.57%` | `33.60` |
| `Live` | `Short` | `7.74` | 61,040,000.00 USD | 505.87 USD | 0.00 USD | `+86.81%` | `65.40` |
| `Live` | `Short` | `7.75` | 61,150,000.00 USD | 105,820.00 USD | 0.00 USD | `+87.05%` | `13,662.50` |
| `Live` | `Short` | `7.76` | 61,150,000.00 USD | 498.51 USD | 0.00 USD | `+87.54%` | `64.20` |
| `Live` | `Short` | `7.79` | 61,220,000.00 USD | 74,390.00 USD | 0.00 USD | `+88.02%` | `9,555.00` |
| `Live` | `Short` | `7.87` | 61,230,000.00 USD | 2,980.00 USD | 0.00 USD | `+89.95%` | `378.70` |
| `Live` | `Short` | `7.88` | 61,230,000.00 USD | 325.24 USD | 0.00 USD | `+90.19%` | `41.30` |
| `Live` | `Short` | `7.95` | 61,230,000.00 USD | 6,120.00 USD | 0.00 USD | `+91.89%` | `769.80` |
| `Live` | `Short` | `7.96` | 61,370,000.00 USD | 134,240.00 USD | 0.00 USD | `+92.37%` | `16,854.30` |
| `Live` | `Short` | `7.97` | 61,460,000.00 USD | 95,700.00 USD | 0.00 USD | `+92.61%` | `12,000.00` |
| `Live` | `Short` | `7.99` | 61,460,000.00 USD | 399.25 USD | 0.00 USD | `+92.85%` | `50.00` |
| `Live` | `Short` | `8.00` | 61,460,000.00 USD | 167.10 USD | 0.00 USD | `+93.09%` | `20.90` |
| `Live` | `Short` | `8.03` | 61,900,000.00 USD | 435,420.00 USD | 0.00 USD | `+93.82%` | `54,257.40` |
| `Live` | `Short` | `8.04` | 61,900,000.00 USD | 318.19 USD | 0.00 USD | `+94.06%` | `39.60` |
| `Live` | `Short` | `8.20` | 61,900,000.00 USD | 363.86 USD | 0.00 USD | `+97.92%` | `44.40` |
| `Live` | `Short` | `8.22` | 61,900,000.00 USD | 103.64 USD | 0.00 USD | `+98.65%` | `12.60` |
| `Live` | `Short` | `8.28` | 62,600,000.00 USD | 700,250.00 USD | 0.00 USD | `+99.86%` | `84,621.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 2,860,000.00 USD | 0.00 USD | 585.51 USD | `-75.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,860,000.00 USD | 0.00 USD | 339.82 USD | `-75.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,860,000.00 USD | 0.00 USD | 196.58 USD | `-71.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,860,000.00 USD | 0.00 USD | 331.54 USD | `-67.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,860,000.00 USD | 0.00 USD | 345.25 USD | `-67.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,860,000.00 USD | 0.00 USD | 5,640.00 USD | `-66.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,860,000.00 USD | 0.00 USD | 997.29 USD | `-66.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,860,000.00 USD | 0.00 USD | 741.29 USD | `-63.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,850,000.00 USD | 0.00 USD | 113.28 USD | `-62.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,850,000.00 USD | 0.00 USD | 4,000.00 USD | `-62.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,850,000.00 USD | 0.00 USD | 324.22 USD | `-62.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,850,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,850,000.00 USD | 0.00 USD | 739.67 USD | `-61.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,840,000.00 USD | 0.00 USD | 1,740.00 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,840,000.00 USD | 0.00 USD | 6,260.00 USD | `-60.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 2,840,000.00 USD | 0.00 USD | 345.40 USD | `-60.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,840,000.00 USD | 0.00 USD | 167.50 USD | `-59.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,840,000.00 USD | 0.00 USD | 669.02 USD | `-59.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,840,000.00 USD | 0.00 USD | 105.88 USD | `-58.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,840,000.00 USD | 0.00 USD | 172.50 USD | `-58.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,840,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,820,000.00 USD | 0.00 USD | 722.00 USD | `-56.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,820,000.00 USD | 0.00 USD | 259.00 USD | `-56.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,820,000.00 USD | 0.00 USD | 103.84 USD | `-55.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,820,000.00 USD | 0.00 USD | 109.00 USD | `-55.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,820,000.00 USD | 0.00 USD | 222.19 USD | `-54.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,820,000.00 USD | 0.00 USD | 10,280.00 USD | `-54.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,810,000.00 USD | 0.00 USD | 558.36 USD | `-53.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,810,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,810,000.00 USD | 0.00 USD | 222.14 USD | `-53.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,810,000.00 USD | 0.00 USD | 279.50 USD | `-53.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,810,000.00 USD | 0.00 USD | 197.50 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,810,000.00 USD | 0.00 USD | 935.66 USD | `-51.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,810,000.00 USD | 0.00 USD | 18,860.00 USD | `-51.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,790,000.00 USD | 0.00 USD | 3,020.00 USD | `-51.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,790,000.00 USD | 0.00 USD | 214.52 USD | `-50.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,790,000.00 USD | 0.00 USD | 1,200.00 USD | `-50.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,790,000.00 USD | 0.00 USD | 578.41 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,790,000.00 USD | 0.00 USD | 18,070.00 USD | `-49.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,770,000.00 USD | 0.00 USD | 108.62 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,770,000.00 USD | 0.00 USD | 107.23 USD | `-48.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,770,000.00 USD | 0.00 USD | 1,590.00 USD | `-48.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,770,000.00 USD | 0.00 USD | 5,830.00 USD | `-48.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,760,000.00 USD | 0.00 USD | 310.32 USD | `-47.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,760,000.00 USD | 0.00 USD | 1,170.00 USD | `-47.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,760,000.00 USD | 0.00 USD | 576.18 USD | `-47.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,760,000.00 USD | 0.00 USD | 295.67 USD | `-46.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,760,000.00 USD | 0.00 USD | 1,430.00 USD | `-46.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,760,000.00 USD | 0.00 USD | 812.68 USD | `-46.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,760,000.00 USD | 0.00 USD | 1,440.00 USD | `-46.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,750,000.00 USD | 0.00 USD | 106.16 USD | `-46.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,750,000.00 USD | 0.00 USD | 6,270.00 USD | `-45.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,750,000.00 USD | 0.00 USD | 478.06 USD | `-45.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,750,000.00 USD | 0.00 USD | 540.88 USD | `-45.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,750,000.00 USD | 0.00 USD | 867.46 USD | `-45.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,750,000.00 USD | 0.00 USD | 759.76 USD | `-44.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,740,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,730,000.00 USD | 0.00 USD | 3,690.00 USD | `-44.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,730,000.00 USD | 0.00 USD | 722.15 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,730,000.00 USD | 0.00 USD | 467.00 USD | `-43.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,730,000.00 USD | 0.00 USD | 506.75 USD | `-43.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,730,000.00 USD | 0.00 USD | 214.27 USD | `-42.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,730,000.00 USD | 0.00 USD | 428.69 USD | `-42.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,730,000.00 USD | 0.00 USD | 322.45 USD | `-42.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,730,000.00 USD | 0.00 USD | 108.25 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,730,000.00 USD | 0.00 USD | 3,900.00 USD | `-41.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,720,000.00 USD | 0.00 USD | 799.04 USD | `-41.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,720,000.00 USD | 0.00 USD | 6,830.00 USD | `-41.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,720,000.00 USD | 0.00 USD | 137.16 USD | `-40.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,720,000.00 USD | 0.00 USD | 504.41 USD | `-40.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,720,000.00 USD | 0.00 USD | 963.93 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,710,000.00 USD | 0.00 USD | 6,690.00 USD | `-39.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,710,000.00 USD | 0.00 USD | 541.98 USD | `-39.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,710,000.00 USD | 0.00 USD | 108.75 USD | `-38.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,710,000.00 USD | 0.00 USD | 766.55 USD | `-38.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,710,000.00 USD | 0.00 USD | 7,110.00 USD | `-38.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,700,000.00 USD | 0.00 USD | 1,100.00 USD | `-37.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,700,000.00 USD | 0.00 USD | 100.04 USD | `-37.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,700,000.00 USD | 0.00 USD | 1,220.00 USD | `-37.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,700,000.00 USD | 0.00 USD | 5,090.00 USD | `-36.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,690,000.00 USD | 0.00 USD | 226.57 USD | `-35.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,690,000.00 USD | 0.00 USD | 104.98 USD | `-35.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,690,000.00 USD | 0.00 USD | 889.89 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,690,000.00 USD | 0.00 USD | 7,270.00 USD | `-34.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,680,000.00 USD | 0.00 USD | 107.21 USD | `-33.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,680,000.00 USD | 0.00 USD | 197.37 USD | `-33.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,680,000.00 USD | 0.00 USD | 8,110.00 USD | `-33.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,670,000.00 USD | 0.00 USD | 108.39 USD | `-33.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,670,000.00 USD | 0.00 USD | 435.95 USD | `-32.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,670,000.00 USD | 0.00 USD | 217.23 USD | `-32.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,670,000.00 USD | 0.00 USD | 437.98 USD | `-32.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,670,000.00 USD | 0.00 USD | 2,720.00 USD | `-32.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,670,000.00 USD | 0.00 USD | 8,380.00 USD | `-31.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,660,000.00 USD | 0.00 USD | 283.50 USD | `-31.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,660,000.00 USD | 0.00 USD | 109.53 USD | `-31.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,660,000.00 USD | 0.00 USD | 1,230.00 USD | `-31.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,660,000.00 USD | 0.00 USD | 1,960.00 USD | `-30.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,660,000.00 USD | 0.00 USD | 157.81 USD | `-30.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,660,000.00 USD | 0.00 USD | 2,900.00 USD | `-30.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,660,000.00 USD | 0.00 USD | 4,870.00 USD | `-29.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,650,000.00 USD | 0.00 USD | 1,320.00 USD | `-29.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,650,000.00 USD | 0.00 USD | 358.90 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,650,000.00 USD | 0.00 USD | 15,370.00 USD | `-28.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,630,000.00 USD | 0.00 USD | 738.75 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,630,000.00 USD | 0.00 USD | 523.32 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,630,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,630,000.00 USD | 0.00 USD | 22,950.00 USD | `-27.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,600,000.00 USD | 0.00 USD | 1,020.00 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,600,000.00 USD | 0.00 USD | 345.76 USD | `-26.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,600,000.00 USD | 0.00 USD | 214.57 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,600,000.00 USD | 0.00 USD | 249.08 USD | `-26.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,600,000.00 USD | 0.00 USD | 305.50 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,600,000.00 USD | 0.00 USD | 109.42 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,600,000.00 USD | 0.00 USD | 9,300.00 USD | `-25.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,590,000.00 USD | 0.00 USD | 8,570.00 USD | `-24.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,580,000.00 USD | 0.00 USD | 104.69 USD | `-24.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,580,000.00 USD | 0.00 USD | 315.69 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,580,000.00 USD | 0.00 USD | 17,510.00 USD | `-24.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,570,000.00 USD | 0.00 USD | 269,150.00 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,300,000.00 USD | 0.00 USD | 4,210.00 USD | `-23.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,290,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,290,000.00 USD | 0.00 USD | 218.81 USD | `-23.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,290,000.00 USD | 0.00 USD | 24,840.00 USD | `-22.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,270,000.00 USD | 0.00 USD | 144.67 USD | `-22.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,270,000.00 USD | 0.00 USD | 27,380.00 USD | `-21.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,240,000.00 USD | 0.00 USD | 104.81 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,240,000.00 USD | 0.00 USD | 200.10 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,240,000.00 USD | 0.00 USD | 1,480.00 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,240,000.00 USD | 0.00 USD | 1,870.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,230,000.00 USD | 0.00 USD | 18,240.00 USD | `-20.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,220,000.00 USD | 0.00 USD | 240.67 USD | `-19.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,220,000.00 USD | 0.00 USD | 306.56 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,220,000.00 USD | 0.00 USD | 6,590.00 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,210,000.00 USD | 0.00 USD | 505.76 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,210,000.00 USD | 0.00 USD | 73,220.00 USD | `-18.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,140,000.00 USD | 0.00 USD | 19,600.00 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,120,000.00 USD | 0.00 USD | 8,490.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,110,000.00 USD | 0.00 USD | 111,650.00 USD | `-17.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,000,000.00 USD | 0.00 USD | 421.41 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,000,000.00 USD | 0.00 USD | 506.22 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,990,000.00 USD | 0.00 USD | 171.75 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,990,000.00 USD | 0.00 USD | 2,550.00 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,990,000.00 USD | 0.00 USD | 1,380.00 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,990,000.00 USD | 0.00 USD | 344.07 USD | `-16.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,990,000.00 USD | 0.00 USD | 24,320.00 USD | `-16.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,970,000.00 USD | 0.00 USD | 156.83 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,970,000.00 USD | 0.00 USD | 894.72 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,970,000.00 USD | 0.00 USD | 67,780.00 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,900,000.00 USD | 0.00 USD | 21,320.00 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,880,000.00 USD | 0.00 USD | 3,700.00 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,870,000.00 USD | 0.00 USD | 17,230.00 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,850,000.00 USD | 0.00 USD | 5,130.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,850,000.00 USD | 0.00 USD | 17,420.00 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,830,000.00 USD | 0.00 USD | 18,440.00 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,810,000.00 USD | 0.00 USD | 78,170.00 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,740,000.00 USD | 0.00 USD | 1,250.00 USD | `-13.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,730,000.00 USD | 0.00 USD | 331.46 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,730,000.00 USD | 0.00 USD | 16,250.00 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,720,000.00 USD | 0.00 USD | 632.99 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,720,000.00 USD | 0.00 USD | 172.19 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,720,000.00 USD | 0.00 USD | 1,210.00 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,720,000.00 USD | 0.00 USD | 179.33 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,720,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,710,000.00 USD | 0.00 USD | 4,070.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,710,000.00 USD | 0.00 USD | 367.50 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,710,000.00 USD | 0.00 USD | 34,850.00 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,670,000.00 USD | 0.00 USD | 4,370.00 USD | `-10.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,670,000.00 USD | 0.00 USD | 234,410.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,430,000.00 USD | 0.00 USD | 6,300.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,430,000.00 USD | 0.00 USD | 2,490.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,420,000.00 USD | 0.00 USD | 32,040.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,390,000.00 USD | 0.00 USD | 28,820.00 USD | `-9.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,360,000.00 USD | 0.00 USD | 14,490.00 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,350,000.00 USD | 0.00 USD | 257,990.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,090,000.00 USD | 0.00 USD | 1,510.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,090,000.00 USD | 0.00 USD | 1,660.00 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,090,000.00 USD | 0.00 USD | 181,010.00 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 907,320.00 USD | 0.00 USD | 7,500.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 899,820.00 USD | 0.00 USD | 22,340.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 877,480.00 USD | 0.00 USD | 36,060.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 841,420.00 USD | 0.00 USD | 41,340.00 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 800,080.00 USD | 0.00 USD | 43,060.00 USD | `-7.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 757,030.00 USD | 0.00 USD | 7,710.00 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 749,320.00 USD | 0.00 USD | 8,620.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 740,700.00 USD | 0.00 USD | 161,080.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 579,620.00 USD | 0.00 USD | 57,280.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 522,340.00 USD | 0.00 USD | 12,210.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 510,130.00 USD | 0.00 USD | 46,290.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 463,840.00 USD | 0.00 USD | 2,340.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 461,500.00 USD | 0.00 USD | 5,190.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 456,310.00 USD | 0.00 USD | 934.17 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 455,370.00 USD | 0.00 USD | 3,510.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 451,860.00 USD | 0.00 USD | 5,800.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 446,060.00 USD | 0.00 USD | 37,740.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 408,320.00 USD | 0.00 USD | 317.60 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 408,000.00 USD | 0.00 USD | 3,960.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 404,040.00 USD | 0.00 USD | 993.16 USD | `-3.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 403,040.00 USD | 0.00 USD | 201,270.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 201,770.00 USD | 0.00 USD | 20,520.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 181,250.00 USD | 0.00 USD | 9,590.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 171,660.00 USD | 0.00 USD | 1,470.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 170,200.00 USD | 0.00 USD | 16,870.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 153,320.00 USD | 0.00 USD | 62,450.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 90,870.00 USD | 0.00 USD | 113.41 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 90,760.00 USD | 0.00 USD | 1,290.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 89,470.00 USD | 0.00 USD | 5,360.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 84,110.00 USD | 0.00 USD | 34,290.00 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 49,810.00 USD | 0.00 USD | 410.91 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 49,400.00 USD | 0.00 USD | 1,710.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 47,690.00 USD | 0.00 USD | 46,570.00 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 1,120.00 USD | 0.00 USD | 1,120.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.14` | 3,280.00 USD | 3,280.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 5,000.00 USD | 1,730.00 USD | 0.00 USD | `+0.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 89,840.00 USD | 84,840.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 92,540.00 USD | 2,700.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 184,600.00 USD | 92,060.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 556,590.00 USD | 371,990.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 571,670.00 USD | 15,080.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 572,470.00 USD | 791.58 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 573,600.00 USD | 1,130.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 748,170.00 USD | 174,570.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 753,360.00 USD | 5,190.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 787,810.00 USD | 34,450.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 790,200.00 USD | 2,390.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 813,440.00 USD | 23,230.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 852,090.00 USD | 38,650.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 886,540.00 USD | 34,450.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 913,650.00 USD | 27,110.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 913,920.00 USD | 269.26 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 916,340.00 USD | 2,420.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 917,870.00 USD | 1,540.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 935,250.00 USD | 17,380.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 935,480.00 USD | 222.11 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 1,090,000.00 USD | 156,540.00 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 1,130,000.00 USD | 42,080.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 1,140,000.00 USD | 1,620.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 1,180,000.00 USD | 42,310.00 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 1,590,000.00 USD | 411,780.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,600,000.00 USD | 12,210.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,610,000.00 USD | 4,090.00 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 1,610,000.00 USD | 543.29 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 1,610,000.00 USD | 524.07 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,680,000.00 USD | 71,220.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,680,000.00 USD | 2,470.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 1,680,000.00 USD | 1,700.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,680,000.00 USD | 1,310.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,710,000.00 USD | 29,550.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,730,000.00 USD | 20,340.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,750,000.00 USD | 13,100.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,800,000.00 USD | 52,300.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,800,000.00 USD | 200.45 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,800,000.00 USD | 1,990.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,800,000.00 USD | 1,190.00 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,800,000.00 USD | 227.79 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,800,000.00 USD | 2,030.00 USD | 0.00 USD | `+10.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,810,000.00 USD | 1,470.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,860,000.00 USD | 52,450.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,890,000.00 USD | 27,250.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,890,000.00 USD | 289.82 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,910,000.00 USD | 20,960.00 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,910,000.00 USD | 1,100.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,920,000.00 USD | 7,380.00 USD | 0.00 USD | `+12.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,960,000.00 USD | 44,520.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,980,000.00 USD | 16,750.00 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,980,000.00 USD | 617.10 USD | 0.00 USD | `+12.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,990,000.00 USD | 15,710.00 USD | 0.00 USD | `+13.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,990,000.00 USD | 152.12 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,350,000.00 USD | 357,870.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,570,000.00 USD | 218,120.00 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,570,000.00 USD | 2,650.00 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,660,000.00 USD | 84,180.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,660,000.00 USD | 8,450.00 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,690,000.00 USD | 27,130.00 USD | 0.00 USD | `+14.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,700,000.00 USD | 13,030.00 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,710,000.00 USD | 2,640.00 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,460,000.00 USD | 749,110.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,460,000.00 USD | 559.58 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,630,000.00 USD | 176,880.00 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,670,000.00 USD | 33,510.00 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,680,000.00 USD | 8,540.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,680,000.00 USD | 283.33 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,690,000.00 USD | 11,760.00 USD | 0.00 USD | `+17.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,710,000.00 USD | 24,370.00 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,720,000.00 USD | 10,460.00 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,730,000.00 USD | 10,400.00 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,750,000.00 USD | 19,890.00 USD | 0.00 USD | `+17.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,760,000.00 USD | 4,060.00 USD | 0.00 USD | `+18.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,880,000.00 USD | 120,030.00 USD | 0.00 USD | `+18.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,880,000.00 USD | 156.30 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,890,000.00 USD | 13,180.00 USD | 0.00 USD | `+18.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,900,000.00 USD | 4,420.00 USD | 0.00 USD | `+19.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,900,000.00 USD | 313.51 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,900,000.00 USD | 5,070.00 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,950,000.00 USD | 47,350.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,950,000.00 USD | 187.06 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 4,040,000.00 USD | 92,570.00 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 4,040,000.00 USD | 2,540.00 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 4,080,000.00 USD | 40,150.00 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 4,110,000.00 USD | 25,080.00 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 4,110,000.00 USD | 5,030.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 4,130,000.00 USD | 19,640.00 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 4,130,000.00 USD | 120.58 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 4,150,000.00 USD | 14,690.00 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 4,150,000.00 USD | 6,090.00 USD | 0.00 USD | `+22.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,240,000.00 USD | 87,290.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,250,000.00 USD | 5,640.00 USD | 0.00 USD | `+22.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,250,000.00 USD | 178.33 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,320,000.00 USD | 68,210.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,330,000.00 USD | 15,350.00 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,330,000.00 USD | 179.38 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,330,000.00 USD | 179.72 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,330,000.00 USD | 217.63 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,330,000.00 USD | 493.85 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,330,000.00 USD | 575.38 USD | 0.00 USD | `+24.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,330,000.00 USD | 327.58 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,330,000.00 USD | 163.85 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,450,000.00 USD | 120,930.00 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,490,000.00 USD | 38,410.00 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,490,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,490,000.00 USD | 432.63 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,500,000.00 USD | 2,620.00 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,500,000.00 USD | 537.61 USD | 0.00 USD | `+26.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,920,000.00 USD | 420,400.00 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,920,000.00 USD | 278.52 USD | 0.00 USD | `+27.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,920,000.00 USD | 589.22 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,920,000.00 USD | 733.03 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,920,000.00 USD | 423.60 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,930,000.00 USD | 10,930.00 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,930,000.00 USD | 381.09 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,930,000.00 USD | 961.16 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,930,000.00 USD | 1,570.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,940,000.00 USD | 5,650.00 USD | 0.00 USD | `+29.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,940,000.00 USD | 160.11 USD | 0.00 USD | `+29.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,940,000.00 USD | 225.33 USD | 0.00 USD | `+29.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,940,000.00 USD | 438.60 USD | 0.00 USD | `+29.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,950,000.00 USD | 6,800.00 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,990,000.00 USD | 40,880.00 USD | 0.00 USD | `+30.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,010,000.00 USD | 19,950.00 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,010,000.00 USD | 270.75 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,010,000.00 USD | 639.61 USD | 0.00 USD | `+31.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 5,010,000.00 USD | 1,710.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,020,000.00 USD | 12,600.00 USD | 0.00 USD | `+31.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+31.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,220,000.00 USD | 192,640.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,250,000.00 USD | 30,110.00 USD | 0.00 USD | `+32.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,290,000.00 USD | 38,920.00 USD | 0.00 USD | `+32.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,290,000.00 USD | 1,180.00 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,260,000.00 USD | 968,550.00 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,260,000.00 USD | 5,600.00 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,280,000.00 USD | 19,110.00 USD | 0.00 USD | `+33.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,300,000.00 USD | 18,790.00 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,360,000.00 USD | 58,030.00 USD | 0.00 USD | `+33.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,400,000.00 USD | 46,110.00 USD | 0.00 USD | `+34.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,420,000.00 USD | 14,320.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,430,000.00 USD | 11,740.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,450,000.00 USD | 20,540.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,450,000.00 USD | 384.94 USD | 0.00 USD | `+35.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,450,000.00 USD | 573.39 USD | 0.00 USD | `+35.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,450,000.00 USD | 347.06 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,450,000.00 USD | 491.11 USD | 0.00 USD | `+36.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,450,000.00 USD | 3,290.00 USD | 0.00 USD | `+36.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,450,000.00 USD | 281.55 USD | 0.00 USD | `+36.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,460,000.00 USD | 6,590.00 USD | 0.00 USD | `+37.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,460,000.00 USD | 586.69 USD | 0.00 USD | `+37.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,470,000.00 USD | 5,860.00 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,570,000.00 USD | 103,470.00 USD | 0.00 USD | `+37.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,570,000.00 USD | 705.23 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,580,000.00 USD | 5,720.00 USD | 0.00 USD | `+38.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,580,000.00 USD | 139.03 USD | 0.00 USD | `+38.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,580,000.00 USD | 2,450.00 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,580,000.00 USD | 1,850.00 USD | 0.00 USD | `+39.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,580,000.00 USD | 286.94 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,590,000.00 USD | 7,120.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,590,000.00 USD | 329.13 USD | 0.00 USD | `+40.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,590,000.00 USD | 1,970.00 USD | 0.00 USD | `+40.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,590,000.00 USD | 1,020.00 USD | 0.00 USD | `+40.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,590,000.00 USD | 1,150.00 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,600,000.00 USD | 1,190.00 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,600,000.00 USD | 1,770.00 USD | 0.00 USD | `+41.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,600,000.00 USD | 3,450.00 USD | 0.00 USD | `+41.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,600,000.00 USD | 345.45 USD | 0.00 USD | `+42.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,680,000.00 USD | 81,630.00 USD | 0.00 USD | `+42.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,690,000.00 USD | 2,510.00 USD | 0.00 USD | `+42.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,840,000.00 USD | 153,150.00 USD | 0.00 USD | `+43.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,870,000.00 USD | 26,180.00 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,870,000.00 USD | 5,440.00 USD | 0.00 USD | `+44.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,880,000.00 USD | 8,940.00 USD | 0.00 USD | `+44.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,000,000.00 USD | 119,340.00 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,000,000.00 USD | 3,000.00 USD | 0.00 USD | `+44.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,200,000.00 USD | 201,800.00 USD | 0.00 USD | `+45.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,220,000.00 USD | 13,710.00 USD | 0.00 USD | `+45.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,310,000.00 USD | 90,380.00 USD | 0.00 USD | `+45.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,310,000.00 USD | 2,170.00 USD | 0.00 USD | `+45.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,310,000.00 USD | 3,300.00 USD | 0.00 USD | `+46.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,310,000.00 USD | 1,040.00 USD | 0.00 USD | `+46.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,320,000.00 USD | 425.76 USD | 0.00 USD | `+46.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,320,000.00 USD | 2,030.00 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,320,000.00 USD | 4,120.00 USD | 0.00 USD | `+46.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,320,000.00 USD | 2,000.00 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,380,000.00 USD | 61,050.00 USD | 0.00 USD | `+47.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,390,000.00 USD | 1,610.00 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,390,000.00 USD | 1,200.00 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,390,000.00 USD | 420.32 USD | 0.00 USD | `+48.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,390,000.00 USD | 1,940.00 USD | 0.00 USD | `+48.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,390,000.00 USD | 4,010.00 USD | 0.00 USD | `+49.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,400,000.00 USD | 3,960.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,460,000.00 USD | 66,060.00 USD | 0.00 USD | `+49.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,470,000.00 USD | 1,890.00 USD | 0.00 USD | `+50.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,470,000.00 USD | 195.46 USD | 0.00 USD | `+50.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,470,000.00 USD | 289.93 USD | 0.00 USD | `+50.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 7,470,000.00 USD | 116.16 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,470,000.00 USD | 7,310.00 USD | 0.00 USD | `+52.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,470,000.00 USD | 310.70 USD | 0.00 USD | `+52.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,470,000.00 USD | 325.62 USD | 0.00 USD | `+53.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,480,000.00 USD | 1,760.00 USD | 0.00 USD | `+53.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,480,000.00 USD | 3,230.00 USD | 0.00 USD | `+54.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,480,000.00 USD | 5,120.00 USD | 0.00 USD | `+54.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,490,000.00 USD | 1,310.00 USD | 0.00 USD | `+56.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,520,000.00 USD | 30,990.00 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,520,000.00 USD | 104.24 USD | 0.00 USD | `+57.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,530,000.00 USD | 13,580.00 USD | 0.00 USD | `+58.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,530,000.00 USD | 1,630.00 USD | 0.00 USD | `+59.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 7,530,000.00 USD | 1,370.00 USD | 0.00 USD | `+59.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,540,000.00 USD | 5,400.00 USD | 0.00 USD | `+59.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,540,000.00 USD | 1,620.00 USD | 0.00 USD | `+59.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,540,000.00 USD | 3,220.00 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,540,000.00 USD | 450.55 USD | 0.00 USD | `+60.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,550,000.00 USD | 3,060.00 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,550,000.00 USD | 3,070.00 USD | 0.00 USD | `+61.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,550,000.00 USD | 3,120.00 USD | 0.00 USD | `+62.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,550,000.00 USD | 1,550.00 USD | 0.00 USD | `+62.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,560,000.00 USD | 3,080.00 USD | 0.00 USD | `+63.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,560,000.00 USD | 647.56 USD | 0.00 USD | `+64.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,560,000.00 USD | 1,420.00 USD | 0.00 USD | `+64.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,560,000.00 USD | 2,130.00 USD | 0.00 USD | `+64.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,570,000.00 USD | 6,870.00 USD | 0.00 USD | `+64.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,570,000.00 USD | 342.25 USD | 0.00 USD | `+65.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,570,000.00 USD | 2,990.00 USD | 0.00 USD | `+65.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,570,000.00 USD | 2,970.00 USD | 0.00 USD | `+66.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,580,000.00 USD | 324.54 USD | 0.00 USD | `+66.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,580,000.00 USD | 504.21 USD | 0.00 USD | `+67.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,580,000.00 USD | 166.00 USD | 0.00 USD | `+68.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,580,000.00 USD | 4,190.00 USD | 0.00 USD | `+68.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,590,000.00 USD | 12,970.00 USD | 0.00 USD | `+69.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,600,000.00 USD | 2,860.00 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,600,000.00 USD | 264.31 USD | 0.00 USD | `+71.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,600,000.00 USD | 599.34 USD | 0.00 USD | `+72.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,600,000.00 USD | 193.19 USD | 0.00 USD | `+72.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,600,000.00 USD | 3,950.00 USD | 0.00 USD | `+73.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,600,000.00 USD | 1,940.00 USD | 0.00 USD | `+74.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,760,000.00 USD | 160,550.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,760,000.00 USD | 1,290.00 USD | 0.00 USD | `+75.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,770,000.00 USD | 1,180.00 USD | 0.00 USD | `+76.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,770,000.00 USD | 630.05 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,770,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,770,000.00 USD | 2,610.00 USD | 0.00 USD | `+79.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,780,000.00 USD | 7,630.00 USD | 0.00 USD | `+81.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,780,000.00 USD | 4,640.00 USD | 0.00 USD | `+82.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,780,000.00 USD | 371.88 USD | 0.00 USD | `+83.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,790,000.00 USD | 2,510.00 USD | 0.00 USD | `+83.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,790,000.00 USD | 380.68 USD | 0.00 USD | `+85.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,790,000.00 USD | 1,470.00 USD | 0.00 USD | `+87.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,800,000.00 USD | 11,170.00 USD | 0.00 USD | `+88.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,830,000.00 USD | 34,360.00 USD | 0.00 USD | `+88.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,830,000.00 USD | 253.21 USD | 0.00 USD | `+88.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,830,000.00 USD | 100.29 USD | 0.00 USD | `+89.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,840,000.00 USD | 10,610.00 USD | 0.00 USD | `+92.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,840,000.00 USD | 309.43 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,880,000.00 USD | 36,740.00 USD | 0.00 USD | `+93.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,960,000.00 USD | 81,310.00 USD | 0.00 USD | `+93.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,960,000.00 USD | 1,390.00 USD | 0.00 USD | `+96.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,960,000.00 USD | 216.90 USD | 0.00 USD | `+97.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,970,000.00 USD | 1,990.00 USD | 0.00 USD | `+97.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,970,000.00 USD | 7,200.00 USD | 0.00 USD | `+98.16%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `1.12B` | Total OI Tokens: `265,366,542.0 NEAR`
  * 1h OI Change: `+3.54%` | 4h OI Change: `+4.44%` | 24h OI Change: `-11.80%`
  * Exchange Breakdown: Binance=`208.03M` | Bybit=`148.97M` | OKX=`51.85M` | Hyperliquid=`240.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-70.24K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
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
| `15M` | `NEAR` | `48.99%` | `51.01%` | `0.96` | 5,430,000.00 USD |
| `15M` | `Binance` | `46.9%` | `53.1%` | `0.88` | 2,150,000.00 USD |
| `15M` | `OKX` | `39.14%` | `60.86%` | `0.64` | 342,460.00 USD |
| `15M` | `Bybit` | `47.49%` | `52.51%` | `0.90` | 386,210.00 USD |
| `15M` | `KuCoin` | `48.43%` | `51.57%` | `0.94` | 14,950.00 USD |
| `15M` | `Gate` | `49.81%` | `50.19%` | `0.99` | 131,700.00 USD |
| `15M` | `Bitget` | `35.13%` | `64.87%` | `0.54` | 79,400.00 USD |
| `15M` | `BingX` | `48.88%` | `51.12%` | `0.96` | 768,910.00 USD |
| `15M` | `MEXC` | `59.85%` | `40.15%` | `1.49` | 313,490.00 USD |
| `15M` | `Bitunix` | `57.04%` | `42.96%` | `1.33` | 101,850.00 USD |
| `15M` | `Hyperliquid` | `59.02%` | `40.98%` | `1.44` | 20,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.73%` | `48.27%` | `1.07` | 1,070,000.00 USD |
| `15M` | `Crypto.com` | `41.16%` | `58.84%` | `0.70` | 14.46 USD |
| `15M` | `WhiteBIT` | `88.95%` | `11.05%` | `8.05` | 15,280.00 USD |
| `15M` | `HTX` | `46.52%` | `53.48%` | `0.87` | 2,820.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `95.4%` | `4.6%` | `20.74` | 30,230.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `66.64%` | `33.36%` | `2.00` | 10,340.00 USD |
| `15M` | `Whale Positions` | `46.9%` | `53.1%` | `0.88` | 2,150,000.00 USD |
| `15M` | `Global Accounts` | `48.99%` | `51.01%` | `0.96` | 5,430,000.00 USD |
| `1H` | `NEAR` | `50.94%` | `49.06%` | `1.04` | 35,240,000.00 USD |
| `1H` | `Binance` | `48.97%` | `51.03%` | `0.96` | 13,740,000.00 USD |
| `1H` | `OKX` | `56.43%` | `43.57%` | `1.30` | 5,470,000.00 USD |
| `1H` | `Bybit` | `49.31%` | `50.69%` | `0.97` | 5,580,000.00 USD |
| `1H` | `KuCoin` | `38.79%` | `61.21%` | `0.63` | 476,070.00 USD |
| `1H` | `Gate` | `48.67%` | `51.33%` | `0.95` | 704,510.00 USD |
| `1H` | `Bitget` | `44.12%` | `55.88%` | `0.79` | 2,240,000.00 USD |
| `1H` | `BingX` | `38.21%` | `61.79%` | `0.62` | 1,680,000.00 USD |
| `1H` | `MEXC` | `55.42%` | `44.58%` | `1.24` | 2,240,000.00 USD |
| `1H` | `Bitunix` | `43.62%` | `56.38%` | `0.77` | 1,430,000.00 USD |
| `1H` | `Hyperliquid` | `59.82%` | `40.18%` | `1.49` | 468,100.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `89.65%` | `10.35%` | `8.66` | 659,910.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.61%` | `0.39%` | `255.41` | 429,410.00 USD |
| `1H` | `HTX` | `57.81%` | `42.19%` | `1.37` | 39,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `43.07%` | `56.93%` | `0.76` | 55,740.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.88%` | `43.12%` | `1.32` | 31,960.00 USD |
| `1H` | `Whale Positions` | `48.97%` | `51.03%` | `0.96` | 13,740,000.00 USD |
| `1H` | `Global Accounts` | `50.94%` | `49.06%` | `1.04` | 35,240,000.00 USD |
| `4H` | `NEAR` | `51.68%` | `48.32%` | `1.07` | 137,560,000.00 USD |
| `4H` | `Binance` | `51.91%` | `48.09%` | `1.08` | 54,420,000.00 USD |
| `4H` | `OKX` | `54.51%` | `45.49%` | `1.20` | 19,370,000.00 USD |
| `4H` | `Bybit` | `52.49%` | `47.51%` | `1.10` | 18,230,000.00 USD |
| `4H` | `KuCoin` | `52.05%` | `47.95%` | `1.09` | 1,670,000.00 USD |
| `4H` | `Gate` | `53.32%` | `46.68%` | `1.14` | 4,050,000.00 USD |
| `4H` | `Bitget` | `48.43%` | `51.57%` | `0.94` | 7,160,000.00 USD |
| `4H` | `BingX` | `30.22%` | `69.78%` | `0.43` | 7,210,000.00 USD |
| `4H` | `MEXC` | `55.34%` | `44.66%` | `1.24` | 12,000,000.00 USD |
| `4H` | `Bitunix` | `46.98%` | `53.02%` | `0.89` | 4,660,000.00 USD |
| `4H` | `Hyperliquid` | `38.48%` | `61.52%` | `0.63` | 4,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `70.8%` | `29.2%` | `2.42` | 1,340,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.43%` | `1.57%` | `62.69` | 2,030,000.00 USD |
| `4H` | `HTX` | `49.25%` | `50.75%` | `0.97` | 225,060.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.62%` | `53.38%` | `0.87` | 334,280.00 USD |
| `4H` | `Aster` | `65.79%` | `34.21%` | `1.92` | 369,800.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.7%` | `43.3%` | `1.31` | 116,970.00 USD |
| `4H` | `Whale Positions` | `51.91%` | `48.09%` | `1.08` | 54,420,000.00 USD |
| `4H` | `Global Accounts` | `51.68%` | `48.32%` | `1.07` | 137,560,000.00 USD |


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
| `5m` | 167,410.00 USD | -79,380.00 USD | **`ACCUMULATION`** |
| `15m` | 691,000.00 USD | -575,190.00 USD | **`ACCUMULATION`** |
| `30m` | 866,460.00 USD | -728,530.00 USD | **`ACCUMULATION`** |
| `1h` | 1,650,000.00 USD | 3,200,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,990,000.00 USD | 9,800,000.00 USD | **`ACCUMULATION`** |
| `4h` | 8,400,000.00 USD | 18,810,000.00 USD | **`ACCUMULATION`** |
| `6h` | 3,500,000.00 USD | 1,780,000.00 USD | **`ACCUMULATION`** |
| `8h` | 52,400.00 USD | -14,420,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,410,000.00 USD | -19,600,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,500,000.00 USD | -50,300,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -75,260,000.00 USD | -124,090,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -242,800,000.00 USD | -673,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+167.41K` | 15m=`+691.00K` | 1h=`+1.65M` | 24h=`-10.50M`
* Futures Capital Netflows: 5m=`-79.38K` | 15m=`-575.19K` | 1h=`+3.20M` | 24h=`-50.30M`
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
  * Spread-Padded Stop Loss: `3.87` (Risk Distance: `0.1049` pts)
  * +2.5R Take Profit: `4.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.25` (Risk Distance: `0.1049` pts)
  * +2.5R Take Profit: `3.89`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
