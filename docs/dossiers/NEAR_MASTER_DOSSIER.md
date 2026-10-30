# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:14:31 IST` (`2026-10-30 08:44:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.31` | **Live Ask Quote**: `4.34` | **Mid Price**: `4.32`
- **Spread Points**: `29.00` | **Spread BPS**: `67.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.32` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.35` | Lower -3.00σ Band: `4.29`
  * Upper +2.51σ Band: `4.35` | Lower -2.51σ Band: `4.30`
  * Upper +2.01σ Band: `4.34` | Lower -2.01σ Band: `4.31`
  * Upper +2.00σ Band: `4.34` | Lower -2.00σ Band: `4.31`
  * Upper +1.28σ Band: `4.34` | Lower -1.28σ Band: `4.31`
  * Upper +1.00σ Band: `4.33` | Lower -1.00σ Band: `4.32`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.32` | EMA-20=`4.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.32` (Slope: `+0.0000`) | EMA-100=`4.32`
  * Institutional Anchors: EMA-144=`4.32` | EMA-200=`4.32` (Slope: `+0.0000`) | EMA-233=`4.32`
- **Range Boundaries**: 24H High=`4.37` | 24H Low=`4.28` | Weekly High=`4.41` | Weekly Low=`4.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.20` (Distance: `+3.09%`)
  * Point of Control (POC) = `4.07` (Distance: `+6.34%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+9.80%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.70` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.35` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.35` | Low=`4.30`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.31` - `4.34`
  * Optimal Trade Entry (OTE 0.705): `4.33`
  * Structural Invalidation Anchor (0.786): `4.36`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.34` | `4.35` | `4.33` | `4.33` | `482,907` | 2,094,629.01 USD | 136,310.40 USD | `+6.51%` | -7,171,945.20 USD | `-0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4.33` | `4.34` | `4.32` | `4.33` | `632,545` | 2,739,820.64 USD | -728,329.09 USD | `-26.58%` | -7,900,274.29 USD | `-0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4.34` | `4.34` | `4.32` | `4.32` | `65,971` | 285,562.29 USD | -153,517.22 USD | `-53.76%` | -8,053,791.51 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.25` | `4.36` | `4.24` | `4.35` | `7,085,842` | 30,489,684.47 USD | 8,104,829.62 USD | `+26.58%` | -8,161,927.65 USD | `+3.12` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.35` | `4.36` | `4.33` | `4.34` | `3,506,343` | 15,245,662.84 USD | 853,672.05 USD | `+5.60%` | -7,308,255.60 USD | `+0.17` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.34` | `4.35` | `4.32` | `4.33` | `1,231,044` | 5,334,670.06 USD | -703,177.64 USD | `-13.18%` | -8,011,433.24 USD | `-0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.19` | `4.36` | `4.17` | `4.34` | `11,137,123` | 47,569,677.94 USD | 4,662,002.59 USD | `+9.80%` | -11,821,402.63 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.34` | `4.34` | `4.21` | `4.25` | `9,473,664` | 40,439,071.22 USD | -3,673,419.57 USD | `-9.08%` | -15,494,822.20 USD | `-0.74` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.25` | `4.36` | `4.24` | `4.33` | `11,823,229` | 51,070,017.38 USD | 8,255,324.02 USD | `+16.16%` | -7,239,498.18 USD | `+1.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.36` | `4.24` | `4.32` | `11,773,608` | 50,855,359.24 USD | 8,212,965.76 USD | `+16.15%` | -6,838,083.17 USD | `+1.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.36` | `4.24` | `4.32` | `11,773,608` | 50,855,359.24 USD | 8,212,965.76 USD | `+16.15%` | -6,838,083.17 USD | `+1.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| --- | **`4.32`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `57` | `0x7737...bf66` | `LONG` | 24,456,671.64 USD | `5,640,376.30` | `2.35` | `4.33` | `0.8370` | 11,184,768.81 USD | `+45.73%` | `10X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,498,417.57 USD | `4,507,262.50` | `4.21` | `4.33` | `6.58` | -523,320.86 USD | `-2.68%` | `5X Cross` |
| `128` | `0xb581...6f4f` | `LONG` | 15,576,840.00 USD | `3,600,000.00` | `5.19` | `4.33` | `0.000000` | -3,116,195.22 USD | `-20.01%` | `4X Cross` |
| `206` | `0xdd53...2b13` | `SHORT` | 10,382,313.77 USD | `2,400,202.00` | `2.31` | `4.33` | `28.93` | -4,836,465.21 USD | `-46.58%` | `3X Cross` |
| `252` | `0x77ee...2902` | `LONG` | 8,935,365.65 USD | `2,063,023.10` | `1.93` | `4.33` | `0.000000` | 4,944,169.72 USD | `+55.33%` | `10X Cross` |
| `357` | `0x9df2...c665` | `SHORT` | 6,551,008.55 USD | `1,514,579.00` | `2.36` | `4.33` | `24.17` | -2,971,018.89 USD | `-45.35%` | `10X Cross` |
| `371` | `0xb83d...6e36` | `SHORT` | 6,253,341.84 USD | `1,445,759.10` | `5.19` | `4.33` | `89.65` | 1,256,107.11 USD | `+20.09%` | `3X Cross` |
| `373` | `0x7fda...17d1` | `SHORT` | 6,246,376.72 USD | `1,443,915.10` | `4.28` | `4.33` | `29.69` | -64,298.20 USD | `-1.03%` | `10X Cross` |
| `395` | `0xb46b...538e` | `SHORT` | 5,779,536.00 USD | `1,336,000.00` | `4.33` | `4.33` | `7.47` | 5,328.06 USD | `+0.09%` | `10X Cross` |
| `459` | `0x60b0...991e` | `LONG` | 4,849,182.26 USD | `1,121,307.10` | `5.00` | `4.33` | `0.000000` | -752,242.17 USD | `-15.51%` | `10X Cross` |
| `485` | `0xcac1...26b3` | `SHORT` | 4,643,491.40 USD | `1,073,743.90` | `2.48` | `4.33` | `12.20` | -1,983,547.93 USD | `-42.72%` | `10X Cross` |
| `503` | `0x781e...96b7` | `SHORT` | 4,495,666.13 USD | `1,039,604.60` | `2.45` | `4.33` | `7.53` | -1,951,328.94 USD | `-43.40%` | `10X Cross` |
| `579` | `0x45d2...4029` | `SHORT` | 3,935,064.74 USD | `909,400.00` | `3.26` | `4.33` | `49.36` | -968,914.84 USD | `-24.62%` | `10X Cross` |
| `591` | `0x4cae...7c34` | `LONG` | 3,894,410.09 USD | `900,587.40` | `3.97` | `4.33` | `3.10` | 316,217.31 USD | `+8.12%` | `10X Cross` |
| `758` | `0xf382...578c` | `SHORT` | 3,057,257.18 USD | `706,994.70` | `4.27` | `4.33` | `5.63` | -36,543.05 USD | `-1.20%` | `10X Cross` |
| `818` | `0x005a...61fe` | `LONG` | 2,818,953.00 USD | `652,414.60` | `2.08` | `4.33` | `2.42` | 1,461,421.77 USD | `+51.84%` | `7X Cross` |
| `822` | `0xba5d...a352` | `SHORT` | 2,805,499.31 USD | `647,532.50` | `2.83` | `4.33` | `11.65` | -972,784.37 USD | `-34.67%` | `10X Cross` |
| `828` | `0xb695...a92d` | `SHORT` | 2,765,316.33 USD | `639,231.70` | `4.57` | `4.33` | `38.36` | 158,042.59 USD | `+5.72%` | `10X Cross` |
| `829` | `0xd1dd...9e85` | `SHORT` | 2,757,264.49 USD | `637,621.00` | `4.96` | `4.33` | `18.41` | 406,208.25 USD | `+14.73%` | `10X Cross` |
| `849` | `0x123d...3bff` | `SHORT` | 2,700,944.75 USD | `624,568.10` | `2.09` | `4.33` | `9.12` | -1,395,520.57 USD | `-51.67%` | `10X Cross` |
| `854` | `0xcf53...ee11` | `SHORT` | 2,686,859.08 USD | `621,598.40` | `5.07` | `4.33` | `25.28` | 465,311.17 USD | `+17.32%` | `10X Cross` |
| `977` | `0xbfc7...80b4` | `SHORT` | 2,297,583.90 USD | `531,000.00` | `2.01` | `4.33` | `7.20` | -1,232,384.51 USD | `-53.64%` | `10X Cross` |
| `1235` | `0x0eec...d4c5` | `LONG` | 1,806,024.08 USD | `417,519.90` | `4.01` | `4.33` | `1.09` | 133,168.98 USD | `+7.37%` | `10X Cross` |
| `1282` | `0xe097...d0fe` | `LONG` | 1,729,640.00 USD | `400,000.00` | `5.29` | `4.33` | `0.000000` | -387,147.30 USD | `-22.38%` | `10X Cross` |
| `1383` | `0x6e8f...4364` | `LONG` | 1,562,343.78 USD | `361,210.50` | `3.28` | `4.33` | `3.56` | 378,283.55 USD | `+24.21%` | `10X Cross` |
| `1388` | `0xef96...9383` | `SHORT` | 1,559,969.51 USD | `360,644.90` | `4.50` | `4.33` | `13.86` | 63,137.83 USD | `+4.05%` | `10X Cross` |
| `1447` | `0xdf95...7d72` | `SHORT` | 1,515,172.90 USD | `350,280.40` | `4.23` | `4.33` | `110.83` | -32,676.27 USD | `-2.16%` | `10X Cross` |
| `1451` | `0xcf67...eb24` | `LONG` | 1,513,925.00 USD | `350,000.00` | `1.98` | `4.33` | `1.64` | 822,307.12 USD | `+54.32%` | `10X Cross` |
| `1559` | `0xfc27...9d9d` | `SHORT` | 1,384,182.05 USD | `319,997.70` | `5.01` | `4.33` | `60.93` | 219,360.57 USD | `+15.85%` | `10X Cross` |
| `1565` | `0x089f...a4f8` | `LONG` | 1,380,053.70 USD | `319,043.30` | `4.06` | `4.33` | `0.000000` | 85,196.99 USD | `+6.17%` | `1X Cross` |
| `1599` | `0x2577...4897` | `LONG` | 1,345,775.77 USD | `311,090.10` | `4.26` | `4.33` | `0.000000` | 21,837.69 USD | `+1.62%` | `10X Cross` |
| `1620` | `0x17c3...a868` | `LONG` | 1,325,847.24 USD | `306,405.50` | `4.36` | `4.33` | `0.000000` | -10,911.22 USD | `-0.82%` | `3X Cross` |
| `1712` | `0xe065...0f85` | `SHORT` | 1,245,864.68 USD | `288,027.90` | `2.81` | `4.33` | `5.65` | -435,311.56 USD | `-34.94%` | `10X Cross` |
| `1896` | `0xff43...d924` | `LONG` | 1,080,474.06 USD | `249,474.50` | `4.64` | `4.33` | `3.28` | -77,569.62 USD | `-7.18%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.36` | 2,755.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.76K USD at 4.3571 USD [API] | `2026-10-29 06:43:15` |
| `ANNOUNCEMENT` | `INFO` | `4.36` | 2,925.79 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.93K USD at 4.3571 USD [API] | `2026-10-29 06:43:15` |
| `ANNOUNCEMENT` | `INFO` | `4.32` | 9,868.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.87K USD at 4.3216 USD [API] | `2026-10-29 08:06:09` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 34,044.89 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 34.04K USD at 4.3024 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,999.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 4.00K USD at 4.3024 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 2,573.70 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.57K USD at 4.3024 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,186.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.19K USD at 4.3025 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 430.26 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.43K USD at 4.3026 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 13,684.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 13.68K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,825.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.83K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 1,634.17 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.63K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 651.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.65K USD at 4.3027 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 20,080.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 20.08K USD at 4.3028 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 249.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.25K USD at 4.3029 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 37.44 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.04K USD at 4.3029 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 515.06 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.52K USD at 4.3029 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 11,347.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 11.35K USD at 4.3030 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 4,999.66 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 5.00K USD at 4.3030 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 1,789.19 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.79K USD at 4.3030 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 8,020.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 8.02K USD at 4.3031 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 199.66 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.20K USD at 4.3031 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 348.56 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.35K USD at 4.3032 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 2,240.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.24K USD at 4.3032 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 1,104.20 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.10K USD at 4.3032 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 166.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.17K USD at 4.3035 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,188.03 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.19K USD at 4.3035 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 18,691.40 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 18.69K USD at 4.3037 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,188.26 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.19K USD at 4.3038 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,010.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.01K USD at 4.3039 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,188.70 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.19K USD at 4.3044 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 4,999.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 5.00K USD at 4.3047 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 2,466.22 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.47K USD at 4.3048 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 8,954.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 8.95K USD at 4.3048 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 18,696.61 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 18.70K USD at 4.3049 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 99.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.10K USD at 4.3049 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 1,291.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.29K USD at 4.3050 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3060 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3061 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 111.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.11K USD at 4.3061 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.95 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3062 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 430.62 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.43K USD at 4.3062 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 236.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.24K USD at 4.3062 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3065 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3067 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.61 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3070 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 499.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 4.3073 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 99.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.10K USD at 4.3073 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.31` | 1,258.71 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.26K USD at 4.3077 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 13,001.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 13.00K USD at 4.3034 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 166.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.17K USD at 4.3035 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,827.70 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.83K USD at 4.3036 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,120.18 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.12K USD at 4.3037 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 20,085.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 20.09K USD at 4.3039 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,936.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.94K USD at 4.3040 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,828.61 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3040 USD [API] | `2026-10-29 06:47:16` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.38%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--4.08%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.30%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--4.08%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.30%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--4.08%`)
  * 7D Horizon: Short MP=`5.03` (Vol: 833,800.00 USD, Dist: `+15.34%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--4.02%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 22,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Long Liquidation` | `3.48` | 18,480,000.00 USD | 18,480,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 30,100.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 49,910.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 18,400,000.00 USD | 18,400,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 47,110.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 18,340,000.00 USD | 18,340,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 69,940.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 18,340,000.00 USD | 18,340,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 114,740.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 18,280,000.00 USD | 18,280,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 94,440.00 USD | 6,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 18,050,000.00 USD | 18,050,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 167,840.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 17,960,000.00 USD | 17,960,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 556,540.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 17,730,000.00 USD | 17,730,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 1,380,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 17,670,000.00 USD | 17,670,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 67,180.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 17,470,000.00 USD | 17,470,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 42,530.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 17,190,000.00 USD | 17,190,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 22,620.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 17,170,000.00 USD | 17,170,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 276,290.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 17,060,000.00 USD | 17,060,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 16,360.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 16,920,000.00 USD | 16,920,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 132,530.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 16,710,000.00 USD | 16,710,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 95,160.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 16,650,000.00 USD | 16,650,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 15,050.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 16,480,000.00 USD | 16,480,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,880.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 16,390,000.00 USD | 16,390,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 40,010.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 16,220,000.00 USD | 16,220,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 106,380.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 16,100,000.00 USD | 16,100,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 217,880.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 16,100,000.00 USD | 16,100,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 93,270.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 16,010,000.00 USD | 16,010,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 79,410.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 15,870,000.00 USD | 15,870,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 68,990.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 15,740,000.00 USD | 15,740,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 163,920.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 15,740,000.00 USD | 15,740,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 123,490.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 15,630,000.00 USD | 15,630,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,210.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 15,340,000.00 USD | 15,340,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 150,270.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 15,150,000.00 USD | 15,150,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 201,540.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 15,090,000.00 USD | 15,090,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 29,280.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 15,040,000.00 USD | 15,040,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 34,900.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 17,720,000.00 USD | 17,720,000.00 USD | 9,260.00 USD | 24,440.00 USD | 91,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 14,880,000.00 USD | 14,880,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 36,690.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 17,600,000.00 USD | 17,600,000.00 USD | 3,400.00 USD | 0.00 USD | 76,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 14,690,000.00 USD | 14,690,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 585,850.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 17,520,000.00 USD | 17,520,000.00 USD | 213,700.00 USD | 0.00 USD | 101,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 14,630,000.00 USD | 14,630,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 10,380.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 17,200,000.00 USD | 17,200,000.00 USD | 49,390.00 USD | 31,910.00 USD | 141,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 14,630,000.00 USD | 14,630,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 181,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 16,980,000.00 USD | 16,980,000.00 USD | 125,840.00 USD | 125,330.00 USD | 113,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 14,580,000.00 USD | 14,580,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 177,970.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 16,620,000.00 USD | 16,620,000.00 USD | 150,080.00 USD | 46,190.00 USD | 65,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 14,480,000.00 USD | 14,480,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 119,980.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 16,350,000.00 USD | 16,350,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 14,430,000.00 USD | 14,430,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 37,650.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 15,950,000.00 USD | 15,950,000.00 USD | 39,130.00 USD | 39,050.00 USD | 53,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 14,300,000.00 USD | 14,300,000.00 USD | 5,190.00 USD | 173,980.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 75,620.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 15,820,000.00 USD | 15,820,000.00 USD | 52,700.00 USD | 58,230.00 USD | 189,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 14,050,000.00 USD | 14,050,000.00 USD | 63,710.00 USD | 0.00 USD | 227,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 8,180.00 USD | 938,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 15,520,000.00 USD | 15,520,000.00 USD | 35,520.00 USD | 17,520.00 USD | 223,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 13,760,000.00 USD | 13,760,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 177,470.00 USD | 929,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 15,250,000.00 USD | 15,250,000.00 USD | 373,610.00 USD | 91,480.00 USD | 236,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 13,400,000.00 USD | 13,400,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 97,100.00 USD | 752,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 14,540,000.00 USD | 14,540,000.00 USD | 33,360.00 USD | 49,080.00 USD | 226,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 13,260,000.00 USD | 13,260,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,520.00 USD | 655,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 14,240,000.00 USD | 14,240,000.00 USD | 337,710.00 USD | 120,100.00 USD | 286,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 12,910,000.00 USD | 12,910,000.00 USD | 121,570.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,310.00 USD | 648,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 13,490,000.00 USD | 13,490,000.00 USD | 317,510.00 USD | 8,570.00 USD | 125,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 12,670,000.00 USD | 12,670,000.00 USD | 85,790.00 USD | 66,710.00 USD | 104,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,480.00 USD | 611,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 13,040,000.00 USD | 13,040,000.00 USD | 116,350.00 USD | 99,220.00 USD | 99,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 3,320.00 USD | 609,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 12,720,000.00 USD | 12,720,000.00 USD | 132,520.00 USD | 53,060.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 12,390,000.00 USD | 12,390,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 149,880.00 USD | 605,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 12,400,000.00 USD | 12,400,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 12,330,000.00 USD | 12,330,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 56,160.00 USD | 455,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 12,250,000.00 USD | 12,250,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 12,320,000.00 USD | 12,320,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 10,220.00 USD | 399,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 12,140,000.00 USD | 12,140,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 12,150,000.00 USD | 12,150,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 71,610.00 USD | 389,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 11,960,000.00 USD | 11,960,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 11,910,000.00 USD | 11,910,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 5,650.00 USD | 317,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 11,770,000.00 USD | 11,770,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 11,130,000.00 USD | 11,130,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,840.00 USD | 312,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 11,570,000.00 USD | 11,570,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 10,720,000.00 USD | 10,720,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 11,990.00 USD | 151,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 11,370,000.00 USD | 11,370,000.00 USD | 473.90 USD | 158,450.00 USD | 222,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 9,770,000.00 USD | 9,770,000.00 USD | 371,710.00 USD | 57,440.00 USD | 438,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.01` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 10,990,000.00 USD | 10,990,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 8,910,000.00 USD | 8,910,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 856.12 USD | 139,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 10,680,000.00 USD | 10,680,000.00 USD | 64,700.00 USD | 59,350.00 USD | 269.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 8,230,000.00 USD | 8,230,000.00 USD | 247,960.00 USD | 0.00 USD | 344,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 21,260.00 USD | 138,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 10,550,000.00 USD | 10,550,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 7,630,000.00 USD | 7,630,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 19,300.00 USD | 117,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 10,280,000.00 USD | 10,280,000.00 USD | 348,930.00 USD | 23,720.00 USD | 119.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 1,080.00 USD | 97,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 9,900,000.00 USD | 9,900,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 72,410.00 USD | 292.74 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 6,800.00 USD | 96,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 9,330,000.00 USD | 9,330,000.00 USD | 357,260.00 USD | 205,460.00 USD | 334,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 553.79 USD | 90,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 8,440,000.00 USD | 8,440,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 21,030.00 USD | 89,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 7,960,000.00 USD | 7,960,000.00 USD | 243,890.00 USD | 60,230.00 USD | 168,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 5,950,000.00 USD | 5,950,000.00 USD | 253,510.00 USD | 179,350.00 USD | 432,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 17,640.00 USD | 68,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 7,480,000.00 USD | 7,480,000.00 USD | 2,770.00 USD | 89,650.00 USD | 140,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 5,080,000.00 USD | 5,080,000.00 USD | 27,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 16,940.00 USD | 50,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 7,250,000.00 USD | 7,250,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 24,080.00 USD | 33,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 6,650,000.00 USD | 6,650,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.13` | 6,290,000.00 USD | 6,290,000.00 USD | 159,720.00 USD | 0.00 USD | 398,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 4,550,000.00 USD | 4,550,000.00 USD | 154,140.00 USD | 0.00 USD | 237,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 5,730,000.00 USD | 5,730,000.00 USD | 96,750.00 USD | 0.00 USD | 97,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 4,160,000.00 USD | 4,160,000.00 USD | 238,150.00 USD | 217,700.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 9,830.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 5,540,000.00 USD | 5,540,000.00 USD | 469,190.00 USD | 79,810.00 USD | 318,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 3,360,000.00 USD | 3,360,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 4,670,000.00 USD | 4,670,000.00 USD | 276,920.00 USD | 51,570.00 USD | 316,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 9,290.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 4,030,000.00 USD | 4,030,000.00 USD | 215,050.00 USD | 283,430.00 USD | 238,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 3,120,000.00 USD | 3,120,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 3,290,000.00 USD | 3,290,000.00 USD | 329,080.00 USD | 62,340.00 USD | 158,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 2,740,000.00 USD | 2,740,000.00 USD | 148,260.00 USD | 115,850.00 USD | 245,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 2,700,000.00 USD | 2,700,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 2,230,000.00 USD | 2,230,000.00 USD | 540.30 USD | 26,180.00 USD | 132,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,250,000.00 USD | 2,250,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 2,070,000.00 USD | 2,070,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 1,570,000.00 USD | 1,570,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,110,000.00 USD | 1,110,000.00 USD | 119,070.00 USD | 89,680.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 70,340.00 USD | 177,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.24` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 419.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 186,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 485,290.00 USD | 485,290.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.26` | 832,540.00 USD | 832,540.00 USD | 0.00 USD | 0.00 USD | 736.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 481,900.00 USD | 481,900.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 305,790.00 USD | 305,790.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 395.44 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 831,810.00 USD | 831,810.00 USD | 4,310.00 USD | 0.00 USD | 316.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 280,970.00 USD | 280,970.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 827,180.00 USD | 827,180.00 USD | 156,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 275,590.00 USD | 275,590.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.31` | 671,130.00 USD | 671,130.00 USD | 0.00 USD | 0.00 USD | 865.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 270,440.00 USD | 270,440.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.32` | 670,270.00 USD | 670,270.00 USD | 381,790.00 USD | 0.00 USD | 151.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 268,260.00 USD | 268,260.00 USD | 268,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.33` | 288,330.00 USD | 288,330.00 USD | 287,160.00 USD | 0.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 8,950.00 USD | 8,950.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 17,900.00 USD | 17,900.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 269,670.00 USD | 269,670.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 539,330.00 USD | 539,330.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 34,780.00 USD | 34,780.00 USD | 9,550.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 17,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 697,990.00 USD | 697,990.00 USD | 157,030.00 USD | 0.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 289,880.00 USD | 289,880.00 USD | 255,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 20,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 1,180,000.00 USD | 1,180,000.00 USD | 108,840.00 USD | 93,400.00 USD | 281,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 300,340.00 USD | 300,340.00 USD | 10,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 2,040,000.00 USD | 2,040,000.00 USD | 281,560.00 USD | 173,170.00 USD | 400,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 744,200.00 USD | 744,200.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 76,420.00 USD | 97,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 2,990,000.00 USD | 2,990,000.00 USD | 250,760.00 USD | 60,680.00 USD | 638,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 3,890,000.00 USD | 3,890,000.00 USD | 356,920.00 USD | 41,380.00 USD | 508,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 2,310,000.00 USD | 2,310,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 278,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 4,760,000.00 USD | 4,760,000.00 USD | 458,500.00 USD | 58,380.00 USD | 353,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,420,000.00 USD | 3,420,000.00 USD | 111,810.00 USD | 116,620.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 5,960,000.00 USD | 5,960,000.00 USD | 336,310.00 USD | 272,870.00 USD | 589,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 3,770,000.00 USD | 3,770,000.00 USD | 1,450.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 3,410.00 USD | 281,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 6,240,000.00 USD | 6,240,000.00 USD | 1,080.00 USD | 142,250.00 USD | 130,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,420,000.00 USD | 4,420,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 283,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 6,740,000.00 USD | 6,740,000.00 USD | 84,650.00 USD | 109,630.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 4,870,000.00 USD | 4,870,000.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 5,610.00 USD | 289,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 7,630,000.00 USD | 7,630,000.00 USD | 156,430.00 USD | 370,280.00 USD | 367,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 33,190.00 USD | 322,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 7,940,000.00 USD | 7,940,000.00 USD | 76,860.00 USD | 108,640.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 2,160.00 USD | 324,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 8,010,000.00 USD | 8,010,000.00 USD | 4,580.00 USD | 37,160.00 USD | 31,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 5,600,000.00 USD | 5,600,000.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 325,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 8,320,000.00 USD | 8,320,000.00 USD | 160,740.00 USD | 25,190.00 USD | 120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 6,170,000.00 USD | 6,170,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 19,880.00 USD | 345,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 8,730,000.00 USD | 8,730,000.00 USD | 205,250.00 USD | 86,520.00 USD | 121,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 6,420,000.00 USD | 6,420,000.00 USD | 1,870.00 USD | 44,840.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 5,000.00 USD | 350,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 9,560,000.00 USD | 9,560,000.00 USD | 253,770.00 USD | 213,100.00 USD | 357,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 6,760,000.00 USD | 6,760,000.00 USD | 244,370.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 20,580.00 USD | 371,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 10,170,000.00 USD | 10,170,000.00 USD | 363,660.00 USD | 69,580.00 USD | 178,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 7,340,000.00 USD | 7,340,000.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 1,330.00 USD | 372,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 10,920,000.00 USD | 10,920,000.00 USD | 188,660.00 USD | 149,810.00 USD | 416,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 7,420,000.00 USD | 7,420,000.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 5,220.00 USD | 377,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 11,550,000.00 USD | 11,550,000.00 USD | 288,560.00 USD | 92,260.00 USD | 243,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 7,650,000.00 USD | 7,650,000.00 USD | 2,080.00 USD | 0.00 USD | 225,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 819.48 USD | 378,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 12,330,000.00 USD | 12,330,000.00 USD | 505,320.00 USD | 0.00 USD | 278,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 8,630,000.00 USD | 8,630,000.00 USD | 439,420.00 USD | 232,800.00 USD | 309,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 3,060.00 USD | 381,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 12,730,000.00 USD | 12,730,000.00 USD | 15,720.00 USD | 150,600.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 9,870,000.00 USD | 9,870,000.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 381,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 12,880,000.00 USD | 12,880,000.00 USD | 1,620.00 USD | 34,450.00 USD | 109,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 237.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 13,280,000.00 USD | 13,280,000.00 USD | 81,450.00 USD | 32,800.00 USD | 288,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 10,360,000.00 USD | 10,360,000.00 USD | 361,350.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 13,620,000.00 USD | 13,620,000.00 USD | 176,460.00 USD | 70,180.00 USD | 98,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 10,900,000.00 USD | 10,900,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 14,780,000.00 USD | 14,780,000.00 USD | 421,530.00 USD | 99,430.00 USD | 633,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 11,030,000.00 USD | 11,030,000.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 2,140.00 USD | 384,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 15,380,000.00 USD | 15,380,000.00 USD | 418,290.00 USD | 75,460.00 USD | 109,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 12,740,000.00 USD | 12,740,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 15,550,000.00 USD | 15,550,000.00 USD | 49,460.00 USD | 50,860.00 USD | 67,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 12,860,000.00 USD | 12,860,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 15,700,000.00 USD | 15,700,000.00 USD | 64,340.00 USD | 7,560.00 USD | 76,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 12,870,000.00 USD | 12,870,000.00 USD | 5,400.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 15,840,000.00 USD | 15,840,000.00 USD | 94,450.00 USD | 31,380.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 13,000,000.00 USD | 13,000,000.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 51,690.00 USD | 435,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 15,850,000.00 USD | 15,850,000.00 USD | 2,310.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 13,220,000.00 USD | 13,220,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 1,500.00 USD | 437,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 16,010,000.00 USD | 16,010,000.00 USD | 106,430.00 USD | 11,270.00 USD | 43,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 13,760,000.00 USD | 13,760,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 713.47 USD | 437,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 16,750,000.00 USD | 16,750,000.00 USD | 202,440.00 USD | 52,020.00 USD | 484,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 14,180,000.00 USD | 14,180,000.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 756.44 USD | 438,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 17,540,000.00 USD | 17,540,000.00 USD | 202,480.00 USD | 309,340.00 USD | 276,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 14,490,000.00 USD | 14,490,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 150,350.00 USD | 589,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 17,880,000.00 USD | 17,880,000.00 USD | 88,770.00 USD | 0.00 USD | 259,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,290.00 USD | 643,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 18,090,000.00 USD | 18,090,000.00 USD | 60,330.00 USD | 106,120.00 USD | 35,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 15,450,000.00 USD | 15,450,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 1,030.00 USD | 644,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 18,470,000.00 USD | 18,470,000.00 USD | 168,690.00 USD | 49,160.00 USD | 168,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 15,610,000.00 USD | 15,610,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 644,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 18,820,000.00 USD | 18,820,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 15,930,000.00 USD | 15,930,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 652,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 19,860,000.00 USD | 19,860,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 16,420,000.00 USD | 16,420,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 20,090,000.00 USD | 20,090,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 16,620,000.00 USD | 16,620,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 20,260,000.00 USD | 20,260,000.00 USD | 109,760.00 USD | 25,210.00 USD | 35,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 16,700,000.00 USD | 16,700,000.00 USD | 59,970.00 USD | 15,660.00 USD | 894.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 8,880.00 USD | 661,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 20,640,000.00 USD | 20,640,000.00 USD | 68,200.00 USD | 132,280.00 USD | 176,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 17,090,000.00 USD | 17,090,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.75` | 21,000,000.00 USD | 21,000,000.00 USD | 76,690.00 USD | 132,460.00 USD | 151,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 17,630,000.00 USD | 17,630,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.76` | 21,120,000.00 USD | 21,120,000.00 USD | 32,430.00 USD | 51,460.00 USD | 32,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 18,980,000.00 USD | 18,980,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 205.37 USD | 661,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 21,260,000.00 USD | 21,260,000.00 USD | 4,870.00 USD | 85,030.00 USD | 57,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 19,890,000.00 USD | 19,890,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 15,680.00 USD | 676,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 21,410,000.00 USD | 21,410,000.00 USD | 37,290.00 USD | 20,000.00 USD | 86,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 21,020,000.00 USD | 21,020,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 677,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 21,610,000.00 USD | 21,610,000.00 USD | 112,300.00 USD | 44,330.00 USD | 41,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 22,050,000.00 USD | 22,050,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,950.00 USD | 678,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 22,130,000.00 USD | 22,130,000.00 USD | 225,790.00 USD | 136,530.00 USD | 159,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 23,640,000.00 USD | 23,640,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 30,450.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 24,270,000.00 USD | 24,270,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 4,090.00 USD | 683,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 27,040,000.00 USD | 27,040,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 684,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 28,690,000.00 USD | 28,690,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 686,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 29,180,000.00 USD | 29,180,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 697,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 31,190,000.00 USD | 31,190,000.00 USD | 466,560.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 697,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long` | `0.8650` | 22,980,000.00 USD | 0.00 USD | 433.80 USD | `-79.66%` | `501.50` |
| `Live` | `Long` | `0.8950` | 22,980,000.00 USD | 0.00 USD | 38,570.00 USD | `-78.95%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 22,940,000.00 USD | 0.00 USD | 2,100.00 USD | `-78.72%` | `2,324.50` |
| `Live` | `Long` | `0.9150` | 22,940,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.48%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 22,930,000.00 USD | 0.00 USD | 2,440.00 USD | `-78.25%` | `2,636.80` |
| `Live` | `Long` | `0.9350` | 22,930,000.00 USD | 0.00 USD | 935.00 USD | `-78.01%` | `1,000.00` |
| `Live` | `Long` | `0.9650` | 22,930,000.00 USD | 0.00 USD | 3,890.00 USD | `-77.31%` | `4,031.40` |
| `Live` | `Long` | `0.9850` | 22,920,000.00 USD | 0.00 USD | 3,450.00 USD | `-76.83%` | `3,506.20` |
| `Live` | `Long` | `0.9950` | 22,920,000.00 USD | 0.00 USD | 155,480.00 USD | `-76.60%` | `156,265.50` |
| `Live` | `Long` | `1.00` | 22,760,000.00 USD | 0.00 USD | 108.04 USD | `-76.36%` | `107.50` |
| `Live` | `Long` | `1.02` | 22,760,000.00 USD | 0.00 USD | 41,860.00 USD | `-75.89%` | `40,836.80` |
| `Live` | `Long` | `1.03` | 22,720,000.00 USD | 0.00 USD | 5,070.00 USD | `-75.66%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,720,000.00 USD | 0.00 USD | 9,010.00 USD | `-75.42%` | `8,617.40` |
| `Live` | `Long` | `1.05` | 22,710,000.00 USD | 0.00 USD | 19,930.00 USD | `-75.19%` | `18,892.80` |
| `Live` | `Long` | `1.06` | 22,690,000.00 USD | 0.00 USD | 2,550.00 USD | `-74.95%` | `2,391.60` |
| `Live` | `Long` | `1.07` | 22,690,000.00 USD | 0.00 USD | 5,310.00 USD | `-74.72%` | `4,939.60` |
| `Live` | `Long` | `1.08` | 22,680,000.00 USD | 0.00 USD | 216.89 USD | `-74.48%` | `199.90` |
| `Live` | `Long` | `1.11` | 22,680,000.00 USD | 0.00 USD | 557.50 USD | `-73.78%` | `500.00` |
| `Live` | `Long` | `1.12` | 22,680,000.00 USD | 0.00 USD | 479,050.00 USD | `-73.54%` | `425,818.90` |
| `Live` | `Long` | `1.14` | 22,200,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.31%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 22,200,000.00 USD | 0.00 USD | 27,770.00 USD | `-73.07%` | `24,249.70` |
| `Live` | `Long` | `1.16` | 22,170,000.00 USD | 0.00 USD | 3,070.00 USD | `-72.84%` | `2,656.30` |
| `Live` | `Long` | `1.17` | 22,160,000.00 USD | 0.00 USD | 144.69 USD | `-72.60%` | `124.20` |
| `Live` | `Long` | `1.18` | 22,160,000.00 USD | 0.00 USD | 647.54 USD | `-72.37%` | `551.10` |
| `Live` | `Long` | `1.19` | 22,160,000.00 USD | 0.00 USD | 37,440.00 USD | `-72.13%` | `31,597.00` |
| `Live` | `Long` | `1.22` | 22,130,000.00 USD | 0.00 USD | 363.28 USD | `-71.43%` | `299.00` |
| `Live` | `Long` | `1.23` | 22,130,000.00 USD | 0.00 USD | 274,360.00 USD | `-71.19%` | `223,964.70` |
| `Live` | `Long` | `1.25` | 21,850,000.00 USD | 0.00 USD | 138.32 USD | `-70.72%` | `111.10` |
| `Live` | `Long` | `1.25` | 21,850,000.00 USD | 0.00 USD | 16,280.00 USD | `-70.49%` | `12,969.60` |
| `Live` | `Long` | `1.26` | 21,830,000.00 USD | 0.00 USD | 7,400.00 USD | `-70.25%` | `5,853.70` |
| `Live` | `Long` | `1.27` | 21,830,000.00 USD | 0.00 USD | 2,390.00 USD | `-70.01%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 21,830,000.00 USD | 0.00 USD | 1,340.00 USD | `-69.78%` | `1,044.10` |
| `Live` | `Long` | `1.29` | 21,820,000.00 USD | 0.00 USD | 997.28 USD | `-69.54%` | `770.10` |
| `Live` | `Long` | `1.30` | 21,820,000.00 USD | 0.00 USD | 60,910.00 USD | `-69.31%` | `46,674.40` |
| `Live` | `Long` | `1.31` | 21,760,000.00 USD | 0.00 USD | 65,900.00 USD | `-69.07%` | `50,117.80` |
| `Live` | `Long` | `1.32` | 21,700,000.00 USD | 0.00 USD | 11,520.00 USD | `-68.84%` | `8,693.70` |
| `Live` | `Long` | `1.33` | 21,680,000.00 USD | 0.00 USD | 794.59 USD | `-68.60%` | `595.20` |
| `Live` | `Long` | `1.34` | 21,680,000.00 USD | 0.00 USD | 3,470.00 USD | `-68.37%` | `2,583.40` |
| `Live` | `Long` | `1.35` | 21,680,000.00 USD | 0.00 USD | 2,120.00 USD | `-68.13%` | `1,565.00` |
| `Live` | `Long` | `1.39` | 21,680,000.00 USD | 0.00 USD | 39,430.00 USD | `-67.43%` | `28,470.30` |
| `Live` | `Long` | `1.40` | 21,640,000.00 USD | 0.00 USD | 931.86 USD | `-67.19%` | `668.00` |
| `Live` | `Long` | `1.41` | 21,640,000.00 USD | 0.00 USD | 665.13 USD | `-66.96%` | `473.40` |
| `Live` | `Long` | `1.42` | 21,640,000.00 USD | 0.00 USD | 5,120.00 USD | `-66.72%` | `3,619.30` |
| `Live` | `Long` | `1.43` | 21,630,000.00 USD | 0.00 USD | 2,420.00 USD | `-66.49%` | `1,694.90` |
| `Live` | `Long` | `1.44` | 21,630,000.00 USD | 0.00 USD | 810.20 USD | `-66.25%` | `564.60` |
| `Live` | `Long` | `1.45` | 21,630,000.00 USD | 0.00 USD | 1,640.00 USD | `-66.02%` | `1,136.70` |
| `Live` | `Long` | `1.46` | 21,630,000.00 USD | 0.00 USD | 81,340.00 USD | `-65.78%` | `55,901.20` |
| `Live` | `Long` | `1.47` | 21,550,000.00 USD | 0.00 USD | 13,180.00 USD | `-65.55%` | `9,000.00` |
| `Live` | `Long` | `1.48` | 21,530,000.00 USD | 0.00 USD | 4,570.00 USD | `-65.31%` | `3,096.20` |
| `Live` | `Long` | `1.50` | 21,530,000.00 USD | 0.00 USD | 788.61 USD | `-64.84%` | `527.50` |
| `Live` | `Long` | `1.50` | 21,530,000.00 USD | 0.00 USD | 1,810.00 USD | `-64.61%` | `1,203.90` |
| `Live` | `Long` | `1.51` | 21,530,000.00 USD | 0.00 USD | 454.50 USD | `-64.37%` | `300.00` |
| `Live` | `Long` | `1.52` | 21,520,000.00 USD | 0.00 USD | 3,050.00 USD | `-64.14%` | `2,000.00` |
| `Live` | `Long` | `1.53` | 21,520,000.00 USD | 0.00 USD | 4,750.00 USD | `-63.90%` | `3,094.70` |
| `Live` | `Long` | `1.56` | 21,520,000.00 USD | 0.00 USD | 20,570.00 USD | `-63.19%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 21,500,000.00 USD | 0.00 USD | 589.52 USD | `-62.96%` | `374.30` |
| `Live` | `Long` | `1.58` | 21,500,000.00 USD | 0.00 USD | 5,150.00 USD | `-62.72%` | `3,246.60` |
| `Live` | `Long` | `1.59` | 21,490,000.00 USD | 0.00 USD | 3,700.00 USD | `-62.49%` | `2,319.70` |
| `Live` | `Long` | `1.60` | 21,490,000.00 USD | 0.00 USD | 562,450.00 USD | `-62.25%` | `350,434.30` |
| `Live` | `Long` | `1.61` | 20,920,000.00 USD | 0.00 USD | 242.25 USD | `-62.02%` | `150.00` |
| `Live` | `Long` | `1.64` | 20,920,000.00 USD | 0.00 USD | 2,030.00 USD | `-61.55%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 20,920,000.00 USD | 0.00 USD | 2,390.00 USD | `-61.31%` | `1,454.10` |
| `Live` | `Long` | `1.66` | 20,920,000.00 USD | 0.00 USD | 2,860.00 USD | `-61.08%` | `1,729.30` |
| `Live` | `Long` | `1.67` | 20,920,000.00 USD | 0.00 USD | 6,840.00 USD | `-60.84%` | `4,105.60` |
| `Live` | `Long` | `1.68` | 20,910,000.00 USD | 0.00 USD | 2,440.00 USD | `-60.61%` | `1,458.70` |
| `Live` | `Long` | `1.69` | 20,910,000.00 USD | 0.00 USD | 12,850.00 USD | `-60.37%` | `7,624.50` |
| `Live` | `Long` | `1.71` | 20,900,000.00 USD | 0.00 USD | 7,410.00 USD | `-59.90%` | `4,344.90` |
| `Live` | `Long` | `1.73` | 20,890,000.00 USD | 0.00 USD | 5,850.00 USD | `-59.43%` | `3,388.90` |
| `Live` | `Long` | `1.74` | 20,880,000.00 USD | 0.00 USD | 347.00 USD | `-59.20%` | `200.00` |
| `Live` | `Long` | `1.75` | 20,880,000.00 USD | 0.00 USD | 13,520.00 USD | `-58.96%` | `7,750.30` |
| `Live` | `Long` | `1.75` | 20,870,000.00 USD | 0.00 USD | 10,250.00 USD | `-58.73%` | `5,841.90` |
| `Live` | `Long` | `1.77` | 20,860,000.00 USD | 0.00 USD | 3,920.00 USD | `-58.26%` | `2,207.40` |
| `Live` | `Long` | `1.79` | 20,850,000.00 USD | 0.00 USD | 1,970.00 USD | `-57.79%` | `1,095.10` |
| `Live` | `Long` | `1.80` | 20,850,000.00 USD | 0.00 USD | 529.05 USD | `-57.55%` | `293.10` |
| `Live` | `Long` | `1.81` | 20,850,000.00 USD | 0.00 USD | 1,580.00 USD | `-57.32%` | `873.20` |
| `Live` | `Long` | `1.83` | 20,850,000.00 USD | 0.00 USD | 42,180.00 USD | `-56.84%` | `22,987.20` |
| `Live` | `Long` | `1.85` | 20,810,000.00 USD | 0.00 USD | 984.26 USD | `-56.37%` | `530.60` |
| `Live` | `Long` | `1.89` | 20,810,000.00 USD | 0.00 USD | 567,380.00 USD | `-55.67%` | `300,995.80` |
| `Live` | `Long` | `1.90` | 20,240,000.00 USD | 0.00 USD | 37,060.00 USD | `-55.43%` | `19,555.90` |
| `Live` | `Long` | `1.91` | 20,200,000.00 USD | 0.00 USD | 288.61 USD | `-55.20%` | `151.50` |
| `Live` | `Long` | `1.92` | 20,200,000.00 USD | 0.00 USD | 3,000.00 USD | `-54.96%` | `1,567.60` |
| `Live` | `Long` | `1.93` | 20,200,000.00 USD | 0.00 USD | 34,510.00 USD | `-54.73%` | `17,925.90` |
| `Live` | `Long` | `1.95` | 20,160,000.00 USD | 0.00 USD | 2,740.00 USD | `-54.26%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 20,160,000.00 USD | 0.00 USD | 775.55 USD | `-54.02%` | `396.70` |
| `Live` | `Long` | `1.97` | 20,160,000.00 USD | 0.00 USD | 15,710.00 USD | `-53.79%` | `7,994.70` |
| `Live` | `Long` | `1.98` | 20,150,000.00 USD | 0.00 USD | 35,130.00 USD | `-53.55%` | `17,789.80` |
| `Live` | `Long` | `1.99` | 20,110,000.00 USD | 0.00 USD | 177.46 USD | `-53.32%` | `89.40` |
| `Live` | `Long` | `2.00` | 20,110,000.00 USD | 0.00 USD | 102.34 USD | `-53.08%` | `51.30` |
| `Live` | `Long` | `2.02` | 20,110,000.00 USD | 0.00 USD | 2,680.00 USD | `-52.61%` | `1,327.60` |
| `Live` | `Long` | `2.02` | 20,110,000.00 USD | 0.00 USD | 2,700.00 USD | `-52.38%` | `1,333.40` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 2,400.00 USD | `-52.14%` | `1,179.40` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 5,960.00 USD | `-51.91%` | `2,913.70` |
| `Live` | `Long` | `2.06` | 20,100,000.00 USD | 0.00 USD | 8,290.00 USD | `-51.67%` | `4,035.70` |
| `Live` | `Long` | `2.08` | 20,090,000.00 USD | 0.00 USD | 21,830.00 USD | `-51.20%` | `10,519.30` |
| `Live` | `Long` | `2.08` | 20,070,000.00 USD | 0.00 USD | 33,800.00 USD | `-50.97%` | `16,209.70` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 1,100.00 USD | `-50.73%` | `527.40` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 7,620.00 USD | `-50.49%` | `3,618.10` |
| `Live` | `Long` | `2.12` | 20,020,000.00 USD | 0.00 USD | 11,690.00 USD | `-50.26%` | `5,528.20` |
| `Live` | `Long` | `2.12` | 20,010,000.00 USD | 0.00 USD | 5,370.00 USD | `-50.02%` | `2,527.30` |
| `Live` | `Long` | `2.13` | 20,010,000.00 USD | 0.00 USD | 7,480.00 USD | `-49.79%` | `3,501.50` |
| `Live` | `Long` | `2.15` | 20,000,000.00 USD | 0.00 USD | 92,530.00 USD | `-49.55%` | `43,139.50` |
| `Live` | `Long` | `2.15` | 19,910,000.00 USD | 0.00 USD | 857.04 USD | `-49.32%` | `397.70` |
| `Live` | `Long` | `2.17` | 19,910,000.00 USD | 0.00 USD | 271,220.00 USD | `-49.08%` | `125,276.30` |
| `Live` | `Long` | `2.17` | 19,630,000.00 USD | 0.00 USD | 439.57 USD | `-48.85%` | `202.10` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 3,570.00 USD | `-48.61%` | `1,635.90` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 12,830.00 USD | `-48.38%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,620,000.00 USD | 0.00 USD | 251,430.00 USD | `-48.14%` | `114,026.60` |
| `Live` | `Long` | `2.21` | 19,370,000.00 USD | 0.00 USD | 2,790.00 USD | `-47.91%` | `1,258.80` |
| `Live` | `Long` | `2.23` | 19,360,000.00 USD | 0.00 USD | 2,710.00 USD | `-47.67%` | `1,217.80` |
| `Live` | `Long` | `2.23` | 19,360,000.00 USD | 0.00 USD | 2,450.00 USD | `-47.44%` | `1,097.50` |
| `Live` | `Long` | `2.25` | 19,360,000.00 USD | 0.00 USD | 65,420.00 USD | `-47.20%` | `29,142.40` |
| `Live` | `Long` | `2.25` | 19,290,000.00 USD | 0.00 USD | 116,480.00 USD | `-46.97%` | `51,655.20` |
| `Live` | `Long` | `2.27` | 19,180,000.00 USD | 0.00 USD | 1,390.00 USD | `-46.73%` | `615.70` |
| `Live` | `Long` | `2.27` | 19,170,000.00 USD | 0.00 USD | 379,690.00 USD | `-46.50%` | `166,896.10` |
| `Live` | `Long` | `2.29` | 18,790,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.26%` | `1,359.20` |
| `Live` | `Long` | `2.29` | 18,790,000.00 USD | 0.00 USD | 2,150.00 USD | `-46.03%` | `936.90` |
| `Live` | `Long` | `2.31` | 18,790,000.00 USD | 0.00 USD | 11,600.00 USD | `-45.79%` | `5,030.60` |
| `Live` | `Long` | `2.31` | 18,780,000.00 USD | 0.00 USD | 2,640.00 USD | `-45.56%` | `1,141.80` |
| `Live` | `Long` | `2.33` | 18,780,000.00 USD | 0.00 USD | 2,260.00 USD | `-45.32%` | `972.60` |
| `Live` | `Long` | `2.33` | 18,770,000.00 USD | 0.00 USD | 4,910.00 USD | `-45.09%` | `2,102.30` |
| `Live` | `Long` | `2.35` | 18,770,000.00 USD | 0.00 USD | 5,100.00 USD | `-44.85%` | `2,175.10` |
| `Live` | `Long` | `2.35` | 18,760,000.00 USD | 0.00 USD | 25,910.00 USD | `-44.62%` | `11,000.00` |
| `Live` | `Long` | `2.37` | 18,740,000.00 USD | 0.00 USD | 1,580.00 USD | `-44.38%` | `667.80` |
| `Live` | `Long` | `2.38` | 18,740,000.00 USD | 0.00 USD | 153,930.00 USD | `-44.15%` | `64,811.50` |
| `Live` | `Long` | `2.38` | 18,580,000.00 USD | 0.00 USD | 16,980.00 USD | `-43.91%` | `7,121.00` |
| `Live` | `Long` | `2.40` | 18,560,000.00 USD | 0.00 USD | 570.49 USD | `-43.67%` | `238.20` |
| `Live` | `Long` | `2.40` | 18,560,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-43.44%` | `652,414.60` |
| `Live` | `Long` | `2.42` | 17,000,000.00 USD | 0.00 USD | 429,790.00 USD | `-43.20%` | `177,966.20` |
| `Live` | `Long` | `2.42` | 16,570,000.00 USD | 0.00 USD | 279,710.00 USD | `-42.97%` | `115,346.30` |
| `Live` | `Long` | `2.44` | 16,290,000.00 USD | 0.00 USD | 42,870.00 USD | `-42.73%` | `17,603.70` |
| `Live` | `Long` | `2.44` | 16,240,000.00 USD | 0.00 USD | 3,830.00 USD | `-42.50%` | `1,564.60` |
| `Live` | `Long` | `2.46` | 16,240,000.00 USD | 0.00 USD | 1,700.00 USD | `-42.26%` | `690.80` |
| `Live` | `Long` | `2.46` | 16,240,000.00 USD | 0.00 USD | 5,740.00 USD | `-42.03%` | `2,329.10` |
| `Live` | `Long` | `2.48` | 16,230,000.00 USD | 0.00 USD | 3,760.00 USD | `-41.79%` | `1,518.40` |
| `Live` | `Long` | `2.48` | 16,230,000.00 USD | 0.00 USD | 2,760.00 USD | `-41.56%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 16,220,000.00 USD | 0.00 USD | 13,290.00 USD | `-41.32%` | `5,328.50` |
| `Live` | `Long` | `2.50` | 16,210,000.00 USD | 0.00 USD | 6,000.00 USD | `-41.09%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 16,210,000.00 USD | 0.00 USD | 752.99 USD | `-40.85%` | `299.40` |
| `Live` | `Long` | `2.52` | 16,200,000.00 USD | 0.00 USD | 39,960.00 USD | `-40.62%` | `15,824.10` |
| `Live` | `Long` | `2.54` | 16,160,000.00 USD | 0.00 USD | 395.71 USD | `-40.38%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,160,000.00 USD | 0.00 USD | 105.36 USD | `-40.15%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,160,000.00 USD | 0.00 USD | 1,080.00 USD | `-39.91%` | `422.50` |
| `Live` | `Long` | `2.56` | 16,160,000.00 USD | 0.00 USD | 7,890.00 USD | `-39.68%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,160,000.00 USD | 0.00 USD | 1,570.00 USD | `-39.44%` | `610.60` |
| `Live` | `Long` | `2.58` | 16,150,000.00 USD | 0.00 USD | 4,330.00 USD | `-39.21%` | `1,673.90` |
| `Live` | `Long` | `2.60` | 16,150,000.00 USD | 0.00 USD | 82,690.00 USD | `-38.97%` | `31,866.60` |
| `Live` | `Long` | `2.60` | 16,070,000.00 USD | 0.00 USD | 2,330.00 USD | `-38.74%` | `893.00` |
| `Live` | `Long` | `2.62` | 16,060,000.00 USD | 0.00 USD | 5,150.00 USD | `-38.50%` | `1,968.50` |
| `Live` | `Long` | `2.63` | 16,060,000.00 USD | 0.00 USD | 24,310.00 USD | `-38.03%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 16,040,000.00 USD | 0.00 USD | 2,650.00 USD | `-37.80%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 16,030,000.00 USD | 0.00 USD | 183,640.00 USD | `-37.56%` | `69,168.50` |
| `Live` | `Long` | `2.67` | 15,850,000.00 USD | 0.00 USD | 1,920.00 USD | `-37.32%` | `721.80` |
| `Live` | `Long` | `2.67` | 15,850,000.00 USD | 0.00 USD | 4,470.00 USD | `-37.09%` | `1,670.60` |
| `Live` | `Long` | `2.69` | 15,840,000.00 USD | 0.00 USD | 4,860.00 USD | `-36.85%` | `1,809.60` |
| `Live` | `Long` | `2.69` | 15,840,000.00 USD | 0.00 USD | 733.85 USD | `-36.62%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,840,000.00 USD | 0.00 USD | 164,840.00 USD | `-36.38%` | `60,938.90` |
| `Live` | `Long` | `2.71` | 15,670,000.00 USD | 0.00 USD | 11,750.00 USD | `-36.15%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 15,660,000.00 USD | 0.00 USD | 28,380.00 USD | `-35.91%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 15,630,000.00 USD | 0.00 USD | 3,760.00 USD | `-35.68%` | `1,375.80` |
| `Live` | `Long` | `2.75` | 15,630,000.00 USD | 0.00 USD | 45,290.00 USD | `-35.44%` | `16,498.30` |
| `Live` | `Long` | `2.75` | 15,580,000.00 USD | 0.00 USD | 33,840.00 USD | `-35.21%` | `12,283.10` |
| `Live` | `Long` | `2.77` | 15,550,000.00 USD | 0.00 USD | 353,860.00 USD | `-34.97%` | `127,978.90` |
| `Live` | `Long` | `2.77` | 15,200,000.00 USD | 0.00 USD | 398.77 USD | `-34.74%` | `143.70` |
| `Live` | `Long` | `2.79` | 15,190,000.00 USD | 0.00 USD | 57,290.00 USD | `-34.50%` | `20,570.30` |
| `Live` | `Long` | `2.79` | 15,140,000.00 USD | 0.00 USD | 12,340.00 USD | `-34.27%` | `4,416.00` |
| `Live` | `Long` | `2.81` | 15,130,000.00 USD | 0.00 USD | 95,500.00 USD | `-34.03%` | `34,044.80` |
| `Live` | `Long` | `2.81` | 15,030,000.00 USD | 0.00 USD | 14,950.00 USD | `-33.80%` | `5,309.40` |
| `Live` | `Long` | `2.83` | 15,010,000.00 USD | 0.00 USD | 5,660.00 USD | `-33.56%` | `2,005.20` |
| `Live` | `Long` | `2.83` | 15,010,000.00 USD | 0.00 USD | 11,620.00 USD | `-33.33%` | `4,098.80` |
| `Live` | `Long` | `2.85` | 15,000,000.00 USD | 0.00 USD | 8,780.00 USD | `-33.09%` | `3,084.70` |
| `Live` | `Long` | `2.85` | 14,990,000.00 USD | 0.00 USD | 1,970.00 USD | `-32.86%` | `690.70` |
| `Live` | `Long` | `2.87` | 14,990,000.00 USD | 0.00 USD | 10,780.00 USD | `-32.62%` | `3,764.00` |
| `Live` | `Long` | `2.88` | 14,980,000.00 USD | 0.00 USD | 871,990.00 USD | `-32.39%` | `303,301.50` |
| `Live` | `Long` | `2.88` | 14,100,000.00 USD | 0.00 USD | 6,540.00 USD | `-32.15%` | `2,268.60` |
| `Live` | `Long` | `2.90` | 14,100,000.00 USD | 0.00 USD | 126,700.00 USD | `-31.92%` | `43,765.30` |
| `Live` | `Long` | `2.90` | 13,970,000.00 USD | 0.00 USD | 230,110.00 USD | `-31.68%` | `79,211.60` |
| `Live` | `Long` | `2.92` | 13,740,000.00 USD | 0.00 USD | 4,900.00 USD | `-31.45%` | `1,681.40` |
| `Live` | `Long` | `2.92` | 13,740,000.00 USD | 0.00 USD | 51,300.00 USD | `-31.21%` | `17,540.10` |
| `Live` | `Long` | `2.94` | 13,680,000.00 USD | 0.00 USD | 152,910.00 USD | `-30.98%` | `52,099.10` |
| `Live` | `Long` | `2.94` | 13,530,000.00 USD | 0.00 USD | 18,680.00 USD | `-30.74%` | `6,344.50` |
| `Live` | `Long` | `2.96` | 13,510,000.00 USD | 0.00 USD | 14,060.00 USD | `-30.50%` | `4,758.60` |
| `Live` | `Long` | `2.96` | 13,500,000.00 USD | 0.00 USD | 1,380.00 USD | `-30.27%` | `465.60` |
| `Live` | `Long` | `2.98` | 13,500,000.00 USD | 0.00 USD | 173,220.00 USD | `-30.03%` | `58,224.20` |
| `Live` | `Long` | `2.98` | 13,320,000.00 USD | 0.00 USD | 7,400.00 USD | `-29.80%` | `2,477.70` |
| `Live` | `Long` | `3.00` | 13,320,000.00 USD | 0.00 USD | 9,500.00 USD | `-29.56%` | `3,173.10` |
| `Live` | `Long` | `3.00` | 13,310,000.00 USD | 0.00 USD | 11,020.00 USD | `-29.33%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 13,300,000.00 USD | 0.00 USD | 26,540.00 USD | `-29.09%` | `8,801.10` |
| `Live` | `Long` | `3.02` | 13,270,000.00 USD | 0.00 USD | 33,130.00 USD | `-28.86%` | `10,950.60` |
| `Live` | `Long` | `3.04` | 13,240,000.00 USD | 0.00 USD | 99,420.00 USD | `-28.62%` | `32,758.50` |
| `Live` | `Long` | `3.04` | 13,140,000.00 USD | 0.00 USD | 167,580.00 USD | `-28.39%` | `55,034.20` |
| `Live` | `Long` | `3.06` | 12,970,000.00 USD | 0.00 USD | 132,270.00 USD | `-28.15%` | `43,297.80` |
| `Live` | `Long` | `3.06` | 12,840,000.00 USD | 0.00 USD | 2,890,000.00 USD | `-27.92%` | `943,663.70` |
| `Live` | `Long` | `3.08` | 9,940,000.00 USD | 0.00 USD | 40,840.00 USD | `-27.68%` | `13,281.70` |
| `Live` | `Long` | `3.08` | 9,900,000.00 USD | 0.00 USD | 11,370.00 USD | `-27.45%` | `3,684.40` |
| `Live` | `Long` | `3.10` | 9,890,000.00 USD | 0.00 USD | 6,300.00 USD | `-27.21%` | `2,034.90` |
| `Live` | `Long` | `3.10` | 9,890,000.00 USD | 0.00 USD | 186,200.00 USD | `-26.98%` | `59,966.30` |
| `Live` | `Long` | `3.12` | 9,700,000.00 USD | 0.00 USD | 111,930.00 USD | `-26.74%` | `35,932.70` |
| `Live` | `Long` | `3.12` | 9,590,000.00 USD | 0.00 USD | 7,810.00 USD | `-26.51%` | `2,500.50` |
| `Live` | `Long` | `3.13` | 9,580,000.00 USD | 0.00 USD | 7,780.00 USD | `-26.27%` | `2,481.00` |
| `Live` | `Long` | `3.15` | 9,570,000.00 USD | 0.00 USD | 22,850.00 USD | `-26.04%` | `7,264.70` |
| `Live` | `Long` | `3.15` | 9,550,000.00 USD | 0.00 USD | 2,060.00 USD | `-25.80%` | `654.10` |
| `Live` | `Long` | `3.17` | 9,550,000.00 USD | 0.00 USD | 11,930.00 USD | `-25.57%` | `3,768.60` |
| `Live` | `Long` | `3.17` | 9,540,000.00 USD | 0.00 USD | 1,200.00 USD | `-25.33%` | `376.60` |
| `Live` | `Long` | `3.19` | 9,530,000.00 USD | 0.00 USD | 300,690.00 USD | `-25.10%` | `94,407.00` |
| `Live` | `Long` | `3.19` | 9,230,000.00 USD | 0.00 USD | 8,280.00 USD | `-24.86%` | `2,591.50` |
| `Live` | `Long` | `3.21` | 9,230,000.00 USD | 0.00 USD | 27,760.00 USD | `-24.63%` | `8,662.60` |
| `Live` | `Long` | `3.21` | 9,200,000.00 USD | 0.00 USD | 13,040.00 USD | `-24.39%` | `4,056.00` |
| `Live` | `Long` | `3.23` | 9,180,000.00 USD | 0.00 USD | 23,110.00 USD | `-24.15%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 9,160,000.00 USD | 0.00 USD | 39,310.00 USD | `-23.92%` | `12,152.80` |
| `Live` | `Long` | `3.25` | 9,120,000.00 USD | 0.00 USD | 19,810.00 USD | `-23.68%` | `6,104.10` |
| `Live` | `Long` | `3.25` | 9,100,000.00 USD | 0.00 USD | 5,290.00 USD | `-23.45%` | `1,626.20` |
| `Live` | `Long` | `3.27` | 9,100,000.00 USD | 0.00 USD | 51,360.00 USD | `-23.21%` | `15,731.80` |
| `Live` | `Long` | `3.27` | 9,050,000.00 USD | 0.00 USD | 868,730.00 USD | `-22.98%` | `265,260.40` |
| `Live` | `Long` | `3.29` | 8,180,000.00 USD | 0.00 USD | 4,080.00 USD | `-22.74%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,170,000.00 USD | 0.00 USD | 133,000.00 USD | `-22.51%` | `40,362.70` |
| `Live` | `Long` | `3.31` | 8,040,000.00 USD | 0.00 USD | 136,230.00 USD | `-22.27%` | `41,219.90` |
| `Live` | `Long` | `3.31` | 7,900,000.00 USD | 0.00 USD | 24,860.00 USD | `-22.04%` | `7,500.60` |
| `Live` | `Long` | `3.33` | 7,880,000.00 USD | 0.00 USD | 9,110.00 USD | `-21.80%` | `2,740.50` |
| `Live` | `Long` | `3.33` | 7,870,000.00 USD | 0.00 USD | 73,460.00 USD | `-21.57%` | `22,026.40` |
| `Live` | `Long` | `3.35` | 7,800,000.00 USD | 0.00 USD | 18,900.00 USD | `-21.33%` | `5,650.40` |
| `Live` | `Long` | `3.35` | 7,780,000.00 USD | 0.00 USD | 1,210.00 USD | `-21.10%` | `360.80` |
| `Live` | `Long` | `3.37` | 7,780,000.00 USD | 0.00 USD | 41,170.00 USD | `-20.86%` | `12,233.50` |
| `Live` | `Long` | `3.38` | 7,740,000.00 USD | 0.00 USD | 64,430.00 USD | `-20.63%` | `19,089.60` |
| `Live` | `Long` | `3.38` | 7,670,000.00 USD | 0.00 USD | 46,170.00 USD | `-20.39%` | `13,638.50` |
| `Live` | `Long` | `3.40` | 7,620,000.00 USD | 0.00 USD | 36,770.00 USD | `-20.16%` | `10,830.00` |
| `Live` | `Long` | `3.40` | 7,590,000.00 USD | 0.00 USD | 103,060.00 USD | `-19.92%` | `30,267.20` |
| `Live` | `Long` | `3.42` | 7,480,000.00 USD | 0.00 USD | 391,020.00 USD | `-19.69%` | `114,499.80` |
| `Live` | `Long` | `3.42` | 7,090,000.00 USD | 0.00 USD | 5,400.00 USD | `-19.45%` | `1,575.70` |
| `Live` | `Long` | `3.44` | 7,090,000.00 USD | 0.00 USD | 29,660.00 USD | `-19.22%` | `8,633.80` |
| `Live` | `Long` | `3.44` | 7,060,000.00 USD | 0.00 USD | 164,130.00 USD | `-18.98%` | `47,642.20` |
| `Live` | `Long` | `3.46` | 6,890,000.00 USD | 0.00 USD | 12,040.00 USD | `-18.75%` | `3,486.10` |
| `Live` | `Long` | `3.46` | 6,880,000.00 USD | 0.00 USD | 16,780.00 USD | `-18.51%` | `4,842.00` |
| `Live` | `Long` | `3.48` | 6,870,000.00 USD | 0.00 USD | 164,470.00 USD | `-18.28%` | `47,328.80` |
| `Live` | `Long` | `3.48` | 6,700,000.00 USD | 0.00 USD | 30,100.00 USD | `-18.04%` | `8,635.80` |
| `Live` | `Long` | `3.50` | 6,670,000.00 USD | 0.00 USD | 49,910.00 USD | `-17.81%` | `14,279.50` |
| `Live` | `Long` | `3.50` | 6,620,000.00 USD | 0.00 USD | 47,110.00 USD | `-17.57%` | `13,440.20` |
| `Live` | `Long` | `3.52` | 6,570,000.00 USD | 0.00 USD | 69,940.00 USD | `-17.33%` | `19,896.70` |
| `Live` | `Long` | `3.52` | 6,500,000.00 USD | 0.00 USD | 114,740.00 USD | `-17.10%` | `32,551.20` |
| `Live` | `Long` | `3.54` | 6,390,000.00 USD | 0.00 USD | 94,440.00 USD | `-16.86%` | `26,716.40` |
| `Live` | `Long` | `3.54` | 6,300,000.00 USD | 0.00 USD | 167,840.00 USD | `-16.63%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 6,130,000.00 USD | 0.00 USD | 556,540.00 USD | `-16.39%` | `156,552.30` |
| `Live` | `Long` | `3.56` | 5,570,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-16.16%` | `388,325.00` |
| `Live` | `Long` | `3.58` | 4,190,000.00 USD | 0.00 USD | 67,180.00 USD | `-15.92%` | `18,792.90` |
| `Live` | `Long` | `3.58` | 4,120,000.00 USD | 0.00 USD | 42,530.00 USD | `-15.69%` | `11,864.30` |
| `Live` | `Long` | `3.60` | 4,080,000.00 USD | 0.00 USD | 22,620.00 USD | `-15.45%` | `6,291.10` |
| `Live` | `Long` | `3.60` | 4,050,000.00 USD | 0.00 USD | 276,290.00 USD | `-15.22%` | `76,641.90` |
| `Live` | `Long` | `3.62` | 3,780,000.00 USD | 0.00 USD | 16,360.00 USD | `-14.98%` | `4,526.20` |
| `Live` | `Long` | `3.62` | 3,760,000.00 USD | 0.00 USD | 132,530.00 USD | `-14.75%` | `36,558.80` |
| `Live` | `Long` | `3.63` | 3,630,000.00 USD | 0.00 USD | 95,160.00 USD | `-14.51%` | `26,179.80` |
| `Live` | `Long` | `3.65` | 3,530,000.00 USD | 0.00 USD | 15,050.00 USD | `-14.28%` | `4,128.20` |
| `Live` | `Long` | `3.65` | 3,520,000.00 USD | 0.00 USD | 20,880.00 USD | `-14.04%` | `5,713.20` |
| `Live` | `Long` | `3.67` | 3,500,000.00 USD | 0.00 USD | 40,010.00 USD | `-13.81%` | `10,916.30` |
| `Live` | `Long` | `3.67` | 3,460,000.00 USD | 0.00 USD | 106,380.00 USD | `-13.57%` | `28,948.20` |
| `Live` | `Long` | `3.69` | 3,350,000.00 USD | 0.00 USD | 217,880.00 USD | `-13.34%` | `59,126.00` |
| `Live` | `Long` | `3.69` | 3,130,000.00 USD | 0.00 USD | 93,270.00 USD | `-13.10%` | `25,241.00` |
| `Live` | `Long` | `3.71` | 3,040,000.00 USD | 0.00 USD | 79,410.00 USD | `-12.87%` | `21,432.60` |
| `Live` | `Long` | `3.71` | 2,960,000.00 USD | 0.00 USD | 68,990.00 USD | `-12.63%` | `18,570.70` |
| `Live` | `Long` | `3.73` | 2,890,000.00 USD | 0.00 USD | 163,920.00 USD | `-12.40%` | `44,006.60` |
| `Live` | `Long` | `3.73` | 2,730,000.00 USD | 0.00 USD | 123,490.00 USD | `-12.16%` | `33,063.10` |
| `Live` | `Long` | `3.75` | 2,600,000.00 USD | 0.00 USD | 24,210.00 USD | `-11.93%` | `6,464.40` |
| `Live` | `Long` | `3.75` | 2,580,000.00 USD | 0.00 USD | 150,270.00 USD | `-11.69%` | `40,017.50` |
| `Live` | `Long` | `3.77` | 2,430,000.00 USD | 0.00 USD | 201,540.00 USD | `-11.46%` | `53,530.70` |
| `Live` | `Long` | `3.77` | 2,230,000.00 USD | 0.00 USD | 29,280.00 USD | `-11.22%` | `7,757.30` |
| `Live` | `Long` | `3.79` | 2,200,000.00 USD | 0.00 USD | 34,900.00 USD | `-10.98%` | `9,221.10` |
| `Live` | `Long` | `3.79` | 2,160,000.00 USD | 0.00 USD | 36,690.00 USD | `-10.75%` | `9,668.50` |
| `Live` | `Long` | `3.81` | 2,130,000.00 USD | 0.00 USD | 585,850.00 USD | `-10.51%` | `153,967.50` |
| `Live` | `Long` | `3.81` | 1,540,000.00 USD | 0.00 USD | 10,380.00 USD | `-10.28%` | `2,721.70` |
| `Live` | `Long` | `3.83` | 1,530,000.00 USD | 0.00 USD | 181,850.00 USD | `-10.04%` | `47,542.20` |
| `Live` | `Long` | `3.83` | 1,350,000.00 USD | 0.00 USD | 177,970.00 USD | `-9.81%` | `46,406.60` |
| `Live` | `Long` | `3.85` | 1,170,000.00 USD | 0.00 USD | 119,980.00 USD | `-9.57%` | `31,204.60` |
| `Live` | `Long` | `3.85` | 1,050,000.00 USD | 0.00 USD | 37,650.00 USD | `-9.34%` | `9,767.50` |
| `Live` | `Long` | `3.87` | 1,010,000.00 USD | 0.00 USD | 75,620.00 USD | `-9.10%` | `19,565.70` |
| `Live` | `Long` | `3.88` | 938,080.00 USD | 0.00 USD | 8,180.00 USD | `-8.87%` | `2,109.90` |
| `Live` | `Long` | `3.88` | 929,910.00 USD | 0.00 USD | 177,470.00 USD | `-8.63%` | `45,680.40` |
| `Live` | `Long` | `3.90` | 752,440.00 USD | 0.00 USD | 97,100.00 USD | `-8.40%` | `24,930.40` |
| `Live` | `Long` | `3.90` | 655,340.00 USD | 0.00 USD | 6,520.00 USD | `-8.16%` | `1,669.10` |
| `Live` | `Long` | `3.92` | 648,820.00 USD | 0.00 USD | 37,310.00 USD | `-7.93%` | `9,529.10` |
| `Live` | `Long` | `3.92` | 611,510.00 USD | 0.00 USD | 2,480.00 USD | `-7.69%` | `631.90` |
| `Live` | `Long` | `3.94` | 609,030.00 USD | 0.00 USD | 3,320.00 USD | `-7.46%` | `844.50` |
| `Live` | `Long` | `3.94` | 605,710.00 USD | 0.00 USD | 149,880.00 USD | `-7.22%` | `37,992.30` |
| `Live` | `Long` | `3.96` | 455,830.00 USD | 0.00 USD | 56,160.00 USD | `-6.99%` | `14,200.30` |
| `Live` | `Long` | `3.96` | 399,670.00 USD | 0.00 USD | 10,220.00 USD | `-6.75%` | `2,576.60` |
| `Live` | `Long` | `3.98` | 389,450.00 USD | 0.00 USD | 71,610.00 USD | `-6.52%` | `18,015.60` |
| `Live` | `Long` | `3.98` | 317,840.00 USD | 0.00 USD | 5,650.00 USD | `-6.28%` | `1,417.40` |
| `Live` | `Long` | `4.00` | 312,190.00 USD | 0.00 USD | 160,840.00 USD | `-6.05%` | `40,260.30` |
| `Live` | `Long` | `4.00` | 151,350.00 USD | 0.00 USD | 11,990.00 USD | `-5.81%` | `2,993.80` |
| `Live` | `Short` | `4.01` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | `-5.58%` | `1,013.20` |
| `Live` | `Long` | `4.03` | 139,360.00 USD | 0.00 USD | 856.12 USD | `-5.34%` | `212.70` |
| `Live` | `Long` | `4.04` | 138,500.00 USD | 0.00 USD | 21,260.00 USD | `-5.11%` | `5,268.00` |
| `Live` | `Long` | `4.04` | 117,250.00 USD | 0.00 USD | 19,300.00 USD | `-4.87%` | `4,771.90` |
| `Live` | `Long` | `4.05` | 97,950.00 USD | 0.00 USD | 1,080.00 USD | `-4.64%` | `265.30` |
| `Live` | `Long` | `4.07` | 96,870.00 USD | 0.00 USD | 6,800.00 USD | `-4.40%` | `1,672.70` |
| `Live` | `Long` | `4.08` | 90,070.00 USD | 0.00 USD | 553.79 USD | `-4.16%` | `135.90` |
| `Live` | `Long` | `4.08` | 89,520.00 USD | 0.00 USD | 21,030.00 USD | `-3.93%` | `5,149.30` |
| `Live` | `Long` | `4.09` | 68,480.00 USD | 0.00 USD | 17,640.00 USD | `-3.69%` | `4,307.40` |
| `Live` | `Long` | `4.11` | 50,840.00 USD | 0.00 USD | 16,940.00 USD | `-3.46%` | `4,127.10` |
| `Live` | `Long` | `4.12` | 33,900.00 USD | 0.00 USD | 24,080.00 USD | `-3.22%` | `5,850.70` |
| `Live` | `Long` | `4.14` | 9,830.00 USD | 0.00 USD | 9,830.00 USD | `-2.52%` | `2,370.50` |
| `Live` | `Short` | `4.17` | 13,360.00 USD | 9,290.00 USD | 0.00 USD | `-2.05%` | `2,230.50` |
| `Live` | `Short` | `4.28` | 13,750.00 USD | 395.44 USD | 0.00 USD | `+0.54%` | `92.50` |
| `Live` | `Short` | `4.34` | 17,880.00 USD | 4,130.00 USD | 0.00 USD | `+2.19%` | `949.40` |
| `Live` | `Short` | `4.36` | 20,930.00 USD | 3,050.00 USD | 0.00 USD | `+2.42%` | `701.00` |
| `Live` | `Short` | `4.38` | 97,350.00 USD | 76,420.00 USD | 0.00 USD | `+2.89%` | `17,467.60` |
| `Live` | `Short` | `4.39` | 278,110.00 USD | 180,760.00 USD | 0.00 USD | `+3.36%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 281,530.00 USD | 3,410.00 USD | 0.00 USD | `+3.83%` | `773.00` |
| `Live` | `Short` | `4.42` | 283,460.00 USD | 1,930.00 USD | 0.00 USD | `+4.07%` | `436.00` |
| `Live` | `Short` | `4.43` | 289,060.00 USD | 5,610.00 USD | 0.00 USD | `+4.30%` | `1,264.80` |
| `Live` | `Short` | `4.45` | 322,260.00 USD | 33,190.00 USD | 0.00 USD | `+4.54%` | `7,467.70` |
| `Live` | `Short` | `4.46` | 324,420.00 USD | 2,160.00 USD | 0.00 USD | `+4.77%` | `485.30` |
| `Live` | `Short` | `4.46` | 325,790.00 USD | 1,370.00 USD | 0.00 USD | `+5.01%` | `306.90` |
| `Live` | `Short` | `4.47` | 345,670.00 USD | 19,880.00 USD | 0.00 USD | `+5.24%` | `4,441.60` |
| `Live` | `Short` | `4.49` | 350,660.00 USD | 5,000.00 USD | 0.00 USD | `+5.48%` | `1,114.10` |
| `Live` | `Short` | `4.50` | 371,240.00 USD | 20,580.00 USD | 0.00 USD | `+5.71%` | `4,578.30` |
| `Live` | `Short` | `4.50` | 372,580.00 USD | 1,330.00 USD | 0.00 USD | `+5.95%` | `296.10` |
| `Live` | `Short` | `4.51` | 377,800.00 USD | 5,220.00 USD | 0.00 USD | `+6.18%` | `1,156.80` |
| `Live` | `Short` | `4.53` | 378,620.00 USD | 819.48 USD | 0.00 USD | `+6.42%` | `181.10` |
| `Live` | `Short` | `4.54` | 381,680.00 USD | 3,060.00 USD | 0.00 USD | `+6.65%` | `675.30` |
| `Live` | `Short` | `4.54` | 381,930.00 USD | 252.70 USD | 0.00 USD | `+6.89%` | `55.60` |
| `Live` | `Short` | `4.58` | 384,080.00 USD | 2,140.00 USD | 0.00 USD | `+7.83%` | `467.20` |
| `Live` | `Short` | `4.62` | 435,770.00 USD | 51,690.00 USD | 0.00 USD | `+8.77%` | `11,176.20` |
| `Live` | `Short` | `4.63` | 437,270.00 USD | 1,500.00 USD | 0.00 USD | `+9.01%` | `324.00` |
| `Live` | `Short` | `4.64` | 437,980.00 USD | 713.47 USD | 0.00 USD | `+9.24%` | `153.60` |
| `Live` | `Short` | `4.66` | 438,740.00 USD | 756.44 USD | 0.00 USD | `+9.48%` | `162.50` |
| `Live` | `Short` | `4.67` | 589,090.00 USD | 150,350.00 USD | 0.00 USD | `+9.71%` | `32,229.20` |
| `Live` | `Short` | `4.67` | 643,380.00 USD | 54,290.00 USD | 0.00 USD | `+9.95%` | `11,612.70` |
| `Live` | `Short` | `4.68` | 644,410.00 USD | 1,030.00 USD | 0.00 USD | `+10.18%` | `220.50` |
| `Live` | `Short` | `4.70` | 644,640.00 USD | 230.06 USD | 0.00 USD | `+10.42%` | `49.00` |
| `Live` | `Short` | `4.71` | 652,120.00 USD | 7,480.00 USD | 0.00 USD | `+10.65%` | `1,590.30` |
| `Live` | `Short` | `4.74` | 661,000.00 USD | 8,880.00 USD | 0.00 USD | `+11.36%` | `1,874.70` |
| `Live` | `Short` | `4.76` | 661,200.00 USD | 205.37 USD | 0.00 USD | `+12.06%` | `43.10` |
| `Live` | `Short` | `4.78` | 676,880.00 USD | 15,680.00 USD | 0.00 USD | `+12.30%` | `3,282.90` |
| `Live` | `Short` | `4.79` | 677,020.00 USD | 143.55 USD | 0.00 USD | `+12.53%` | `30.00` |
| `Live` | `Short` | `4.79` | 678,970.00 USD | 1,950.00 USD | 0.00 USD | `+12.77%` | `405.80` |
| `Live` | `Short` | `4.82` | 683,060.00 USD | 4,090.00 USD | 0.00 USD | `+13.24%` | `849.60` |
| `Live` | `Short` | `4.83` | 684,800.00 USD | 1,740.00 USD | 0.00 USD | `+13.47%` | `360.90` |
| `Live` | `Short` | `4.83` | 686,340.00 USD | 1,540.00 USD | 0.00 USD | `+13.71%` | `317.90` |
| `Live` | `Short` | `4.84` | 697,560.00 USD | 11,220.00 USD | 0.00 USD | `+13.94%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 697,700.00 USD | 137.68 USD | 0.00 USD | `+14.41%` | `28.30` |
| `Live` | `Short` | `4.88` | 700,900.00 USD | 3,200.00 USD | 0.00 USD | `+14.88%` | `654.10` |
| `Live` | `Short` | `4.91` | 701,570.00 USD | 674.44 USD | 0.00 USD | `+15.36%` | `137.50` |
| `Live` | `Short` | `4.92` | 722,290.00 USD | 20,720.00 USD | 0.00 USD | `+15.59%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 803,290.00 USD | 81,000.00 USD | 0.00 USD | `+15.83%` | `16,447.70` |
| `Live` | `Short` | `4.93` | 803,450.00 USD | 157.43 USD | 0.00 USD | `+16.06%` | `31.90` |
| `Live` | `Short` | `4.96` | 803,940.00 USD | 488.56 USD | 0.00 USD | `+16.53%` | `98.60` |
| `Live` | `Short` | `4.97` | 903,310.00 USD | 99,370.00 USD | 0.00 USD | `+17.00%` | `19,974.00` |
| `Live` | `Short` | `5.05` | 938,690.00 USD | 35,380.00 USD | 0.00 USD | `+18.88%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 942,110.00 USD | 3,420.00 USD | 0.00 USD | `+19.12%` | `675.80` |
| `Live` | `Short` | `5.08` | 943,310.00 USD | 1,200.00 USD | 0.00 USD | `+19.59%` | `235.80` |
| `Live` | `Short` | `5.12` | 997,120.00 USD | 53,810.00 USD | 0.00 USD | `+20.53%` | `10,500.00` |
| `Live` | `Short` | `5.14` | 999,690.00 USD | 2,570.00 USD | 0.00 USD | `+21.00%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,000,000.00 USD | 751.51 USD | 0.00 USD | `+21.47%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,010,000.00 USD | 11,250.00 USD | 0.00 USD | `+22.18%` | `2,166.50` |
| `Live` | `Short` | `5.22` | 1,080,000.00 USD | 72,290.00 USD | 0.00 USD | `+22.88%` | `13,834.70` |
| `Live` | `Short` | `5.25` | 1,080,000.00 USD | 143.71 USD | 0.00 USD | `+23.35%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,100,000.00 USD | 17,990.00 USD | 0.00 USD | `+23.59%` | `3,423.20` |
| `Live` | `Short` | `5.26` | 1,110,000.00 USD | 5,610.00 USD | 0.00 USD | `+23.82%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 1,110,000.00 USD | 1,690.00 USD | 0.00 USD | `+24.06%` | `320.50` |
| `Live` | `Short` | `5.29` | 1,110,000.00 USD | 134.77 USD | 0.00 USD | `+24.29%` | `25.50` |
| `Live` | `Short` | `5.29` | 2,210,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+24.53%` | `207,820.30` |
| `Live` | `Short` | `5.30` | 2,250,000.00 USD | 41,660.00 USD | 0.00 USD | `+24.76%` | `7,853.80` |
| `Live` | `Short` | `5.32` | 2,270,000.00 USD | 15,970.00 USD | 0.00 USD | `+25.00%` | `3,004.20` |
| `Live` | `Short` | `5.34` | 2,570,000.00 USD | 298,680.00 USD | 0.00 USD | `+25.70%` | `55,879.90` |
| `Live` | `Short` | `5.36` | 2,570,000.00 USD | 142.44 USD | 0.00 USD | `+25.94%` | `26.60` |
| `Live` | `Short` | `5.38` | 2,570,000.00 USD | 182.21 USD | 0.00 USD | `+26.41%` | `33.90` |
| `Live` | `Short` | `5.42` | 2,570,000.00 USD | 1,030.00 USD | 0.00 USD | `+27.35%` | `189.60` |
| `Live` | `Short` | `5.42` | 2,630,000.00 USD | 60,740.00 USD | 0.00 USD | `+27.58%` | `11,196.20` |
| `Live` | `Short` | `5.43` | 2,640,000.00 USD | 13,040.00 USD | 0.00 USD | `+27.82%` | `2,399.40` |
| `Live` | `Short` | `5.47` | 2,650,000.00 USD | 7,840.00 USD | 0.00 USD | `+28.76%` | `1,432.70` |
| `Live` | `Short` | `5.50` | 2,720,000.00 USD | 66,470.00 USD | 0.00 USD | `+29.23%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,750,000.00 USD | 38,800.00 USD | 0.00 USD | `+29.70%` | `7,034.90` |
| `Live` | `Short` | `5.53` | 2,820,000.00 USD | 62,710.00 USD | 0.00 USD | `+29.94%` | `11,349.70` |
| `Live` | `Short` | `5.54` | 2,820,000.00 USD | 209.22 USD | 0.00 USD | `+30.17%` | `37.80` |
| `Live` | `Short` | `5.57` | 2,830,000.00 USD | 8,670.00 USD | 0.00 USD | `+30.88%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 2,890,000.00 USD | 62,420.00 USD | 0.00 USD | `+31.35%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 2,890,000.00 USD | 686.51 USD | 0.00 USD | `+31.58%` | `122.70` |
| `Live` | `Short` | `5.61` | 2,890,000.00 USD | 701.75 USD | 0.00 USD | `+31.82%` | `125.20` |
| `Live` | `Short` | `5.63` | 4,510,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+32.52%` | `288,027.90` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 1,630.00 USD | 0.00 USD | `+33.23%` | `287.30` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 228.70 USD | 0.00 USD | `+33.46%` | `40.30` |
| `Live` | `Short` | `5.68` | 8,420,000.00 USD | 3,900,000.00 USD | 0.00 USD | `+33.70%` | `686,106.80` |
| `Live` | `Short` | `5.70` | 8,890,000.00 USD | 471,680.00 USD | 0.00 USD | `+33.93%` | `82,823.50` |
| `Live` | `Short` | `5.71` | 8,890,000.00 USD | 3,900.00 USD | 0.00 USD | `+34.40%` | `682.40` |
| `Live` | `Short` | `5.75` | 8,900,000.00 USD | 4,580.00 USD | 0.00 USD | `+35.11%` | `796.90` |
| `Live` | `Short` | `5.75` | 8,900,000.00 USD | 286.02 USD | 0.00 USD | `+35.35%` | `49.70` |
| `Live` | `Short` | `5.78` | 8,900,000.00 USD | 2,710.00 USD | 0.00 USD | `+35.82%` | `468.80` |
| `Live` | `Short` | `5.83` | 9,170,000.00 USD | 269,960.00 USD | 0.00 USD | `+37.23%` | `46,264.80` |
| `Live` | `Short` | `5.84` | 9,170,000.00 USD | 310.95 USD | 0.00 USD | `+37.46%` | `53.20` |
| `Live` | `Short` | `5.86` | 9,170,000.00 USD | 848.39 USD | 0.00 USD | `+37.70%` | `144.90` |
| `Live` | `Short` | `5.88` | 9,180,000.00 USD | 7,150.00 USD | 0.00 USD | `+38.40%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 9,270,000.00 USD | 88,420.00 USD | 0.00 USD | `+38.64%` | `15,000.00` |
| `Live` | `Short` | `5.91` | 9,270,000.00 USD | 162.98 USD | 0.00 USD | `+38.87%` | `27.60` |
| `Live` | `Short` | `5.92` | 9,270,000.00 USD | 189.28 USD | 0.00 USD | `+39.11%` | `32.00` |
| `Live` | `Short` | `5.95` | 9,370,000.00 USD | 103,780.00 USD | 0.00 USD | `+39.81%` | `17,456.80` |
| `Live` | `Short` | `6.03` | 9,390,000.00 USD | 23,060.00 USD | 0.00 USD | `+41.70%` | `3,827.40` |
| `Live` | `Short` | `6.05` | 9,720,000.00 USD | 323,960.00 USD | 0.00 USD | `+42.40%` | `53,503.40` |
| `Live` | `Short` | `6.07` | 9,720,000.00 USD | 740.54 USD | 0.00 USD | `+42.64%` | `122.10` |
| `Live` | `Short` | `6.08` | 9,730,000.00 USD | 17,160.00 USD | 0.00 USD | `+43.11%` | `2,820.70` |
| `Live` | `Short` | `6.09` | 9,770,000.00 USD | 37,510.00 USD | 0.00 USD | `+43.34%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 9,770,000.00 USD | 2,430.00 USD | 0.00 USD | `+44.28%` | `396.10` |
| `Live` | `Short` | `6.14` | 9,800,000.00 USD | 23,870.00 USD | 0.00 USD | `+44.52%` | `3,883.80` |
| `Live` | `Short` | `6.16` | 9,800,000.00 USD | 1,880.00 USD | 0.00 USD | `+44.75%` | `305.00` |
| `Live` | `Short` | `6.18` | 9,840,000.00 USD | 35,350.00 USD | 0.00 USD | `+45.46%` | `5,715.90` |
| `Live` | `Short` | `6.24` | 10,360,000.00 USD | 527,010.00 USD | 0.00 USD | `+46.63%` | `84,525.00` |
| `Live` | `Short` | `6.25` | 10,370,000.00 USD | 7,300.00 USD | 0.00 USD | `+46.87%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 10,370,000.00 USD | 439.10 USD | 0.00 USD | `+47.10%` | `70.20` |
| `Live` | `Short` | `6.26` | 10,630,000.00 USD | 256,050.00 USD | 0.00 USD | `+47.34%` | `40,869.30` |
| `Live` | `Short` | `6.32` | 10,630,000.00 USD | 310.70 USD | 0.00 USD | `+48.52%` | `49.20` |
| `Live` | `Short` | `6.33` | 10,630,000.00 USD | 2,010.00 USD | 0.00 USD | `+48.75%` | `317.70` |
| `Live` | `Short` | `6.33` | 10,630,000.00 USD | 382.00 USD | 0.00 USD | `+48.99%` | `60.30` |
| `Live` | `Short` | `6.34` | 10,630,000.00 USD | 214.46 USD | 0.00 USD | `+49.22%` | `33.80` |
| `Live` | `Short` | `6.37` | 10,630,000.00 USD | 113.93 USD | 0.00 USD | `+49.69%` | `17.90` |
| `Live` | `Short` | `6.38` | 10,630,000.00 USD | 288.15 USD | 0.00 USD | `+49.93%` | `45.20` |
| `Live` | `Short` | `6.39` | 10,630,000.00 USD | 2,750.00 USD | 0.00 USD | `+50.40%` | `430.30` |
| `Live` | `Short` | `6.41` | 10,640,000.00 USD | 3,780.00 USD | 0.00 USD | `+50.63%` | `590.10` |
| `Live` | `Short` | `6.42` | 10,640,000.00 USD | 943.65 USD | 0.00 USD | `+50.87%` | `147.10` |
| `Live` | `Short` | `6.42` | 10,640,000.00 USD | 173.47 USD | 0.00 USD | `+51.10%` | `27.00` |
| `Live` | `Short` | `6.45` | 11,850,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+51.57%` | `188,818.40` |
| `Live` | `Short` | `6.46` | 11,860,000.00 USD | 7,150.00 USD | 0.00 USD | `+51.81%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 11,860,000.00 USD | 1,940.00 USD | 0.00 USD | `+52.04%` | `300.00` |
| `Live` | `Short` | `6.51` | 11,860,000.00 USD | 380.48 USD | 0.00 USD | `+53.22%` | `58.40` |
| `Live` | `Short` | `6.54` | 11,860,000.00 USD | 376.34 USD | 0.00 USD | `+53.92%` | `57.50` |
| `Live` | `Short` | `6.55` | 11,870,000.00 USD | 5,590.00 USD | 0.00 USD | `+54.16%` | `852.80` |
| `Live` | `Short` | `6.57` | 12,250,000.00 USD | 380,370.00 USD | 0.00 USD | `+54.39%` | `57,938.40` |
| `Live` | `Short` | `6.58` | 41,930,000.00 USD | 29,680,000.00 USD | 0.00 USD | `+54.87%` | `4,507,262.50` |
| `Live` | `Short` | `6.59` | 41,930,000.00 USD | 418.78 USD | 0.00 USD | `+55.10%` | `63.50` |
| `Live` | `Short` | `6.61` | 41,970,000.00 USD | 40,880.00 USD | 0.00 USD | `+55.34%` | `6,190.00` |
| `Live` | `Short` | `6.66` | 41,980,000.00 USD | 7,230.00 USD | 0.00 USD | `+56.51%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 41,980,000.00 USD | 233.94 USD | 0.00 USD | `+56.75%` | `35.10` |
| `Live` | `Short` | `6.67` | 41,980,000.00 USD | 200.25 USD | 0.00 USD | `+56.98%` | `30.00` |
| `Live` | `Short` | `6.72` | 42,020,000.00 USD | 37,370.00 USD | 0.00 USD | `+58.16%` | `5,556.90` |
| `Live` | `Short` | `6.75` | 43,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+58.86%` | `188,024.00` |
| `Live` | `Short` | `6.78` | 43,290,000.00 USD | 186.31 USD | 0.00 USD | `+59.33%` | `27.50` |
| `Live` | `Short` | `6.79` | 43,290,000.00 USD | 719.89 USD | 0.00 USD | `+59.57%` | `106.10` |
| `Live` | `Short` | `6.82` | 43,290,000.00 USD | 156.75 USD | 0.00 USD | `+60.27%` | `23.00` |
| `Live` | `Short` | `6.84` | 43,290,000.00 USD | 753.63 USD | 0.00 USD | `+60.98%` | `110.10` |
| `Live` | `Short` | `6.87` | 43,290,000.00 USD | 2,650.00 USD | 0.00 USD | `+61.45%` | `386.60` |
| `Live` | `Short` | `6.92` | 43,300,000.00 USD | 6,920.00 USD | 0.00 USD | `+62.86%` | `1,000.00` |
| `Live` | `Short` | `6.96` | 43,390,000.00 USD | 93,100.00 USD | 0.00 USD | `+63.80%` | `13,367.10` |
| `Live` | `Short` | `6.99` | 43,390,000.00 USD | 664.27 USD | 0.00 USD | `+64.27%` | `95.10` |
| `Live` | `Short` | `7.03` | 43,390,000.00 USD | 665.27 USD | 0.00 USD | `+65.21%` | `94.70` |
| `Live` | `Short` | `7.04` | 43,410,000.00 USD | 15,740.00 USD | 0.00 USD | `+65.45%` | `2,237.40` |
| `Live` | `Short` | `7.09` | 43,410,000.00 USD | 699.57 USD | 0.00 USD | `+66.86%` | `98.60` |
| `Live` | `Short` | `7.14` | 47,200,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+68.04%` | `531,000.00` |
| `Live` | `Short` | `7.17` | 47,200,000.00 USD | 1,010.00 USD | 0.00 USD | `+68.51%` | `140.60` |
| `Live` | `Short` | `7.20` | 47,200,000.00 USD | 570.56 USD | 0.00 USD | `+69.21%` | `79.30` |
| `Live` | `Short` | `7.21` | 47,220,000.00 USD | 13,560.00 USD | 0.00 USD | `+69.68%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 47,220,000.00 USD | 4,910.00 USD | 0.00 USD | `+70.15%` | `679.30` |
| `Live` | `Short` | `7.33` | 47,280,000.00 USD | 54,940.00 USD | 0.00 USD | `+72.27%` | `7,500.00` |
| `Live` | `Short` | `7.33` | 47,280,000.00 USD | 4,850.00 USD | 0.00 USD | `+72.50%` | `661.50` |
| `Live` | `Short` | `7.39` | 47,340,000.00 USD | 59,980.00 USD | 0.00 USD | `+73.91%` | `8,111.20` |
| `Live` | `Short` | `7.41` | 47,340,000.00 USD | 776.04 USD | 0.00 USD | `+74.15%` | `104.80` |
| `Live` | `Short` | `7.45` | 47,450,000.00 USD | 106,290.00 USD | 0.00 USD | `+75.09%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 47,450,000.00 USD | 1,420.00 USD | 0.00 USD | `+75.33%` | `191.10` |
| `Live` | `Short` | `7.46` | 57,420,000.00 USD | 9,970,000.00 USD | 0.00 USD | `+75.56%` | `1,336,000.00` |
| `Live` | `Short` | `7.50` | 65,230,000.00 USD | 7,800,000.00 USD | 0.00 USD | `+76.50%` | `1,039,604.60` |
| `Live` | `Short` | `7.53` | 65,230,000.00 USD | 1,570.00 USD | 0.00 USD | `+76.97%` | `208.40` |
| `Live` | `Short` | `7.54` | 65,240,000.00 USD | 13,670.00 USD | 0.00 USD | `+77.21%` | `1,814.20` |
| `Live` | `Short` | `7.54` | 65,240,000.00 USD | 2,620.00 USD | 0.00 USD | `+77.44%` | `347.20` |
| `Live` | `Short` | `7.55` | 65,260,000.00 USD | 11,440.00 USD | 0.00 USD | `+77.68%` | `1,514.20` |
| `Live` | `Short` | `7.59` | 65,270,000.00 USD | 17,700.00 USD | 0.00 USD | `+78.62%` | `2,330.50` |
| `Live` | `Short` | `7.62` | 65,280,000.00 USD | 3,050.00 USD | 0.00 USD | `+79.32%` | `400.00` |
| `Live` | `Short` | `7.63` | 65,300,000.00 USD | 19,210.00 USD | 0.00 USD | `+79.56%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 65,320,000.00 USD | 20,000.00 USD | 0.00 USD | `+80.03%` | `2,612.80` |
| `Live` | `Short` | `7.67` | 65,320,000.00 USD | 360.25 USD | 0.00 USD | `+80.26%` | `47.00` |
| `Live` | `Short` | `7.67` | 65,350,000.00 USD | 33,070.00 USD | 0.00 USD | `+80.50%` | `4,308.50` |
| `Live` | `Short` | `7.70` | 65,350,000.00 USD | 317.80 USD | 0.00 USD | `+80.97%` | `41.30` |
| `Live` | `Short` | `7.71` | 65,380,000.00 USD | 26,980.00 USD | 0.00 USD | `+81.44%` | `3,496.50` |
| `Live` | `Short` | `7.72` | 65,380,000.00 USD | 6,400.00 USD | 0.00 USD | `+81.68%` | `828.00` |
| `Live` | `Short` | `7.74` | 65,380,000.00 USD | 505.87 USD | 0.00 USD | `+81.91%` | `65.40` |
| `Live` | `Short` | `7.75` | 65,380,000.00 USD | 629.67 USD | 0.00 USD | `+82.15%` | `81.30` |
| `Live` | `Short` | `7.80` | 65,390,000.00 USD | 1,690.00 USD | 0.00 USD | `+83.56%` | `216.50` |
| `Live` | `Short` | `7.83` | 65,390,000.00 USD | 109.69 USD | 0.00 USD | `+84.26%` | `14.00` |
| `Live` | `Short` | `7.86` | 65,480,000.00 USD | 94,260.00 USD | 0.00 USD | `+84.73%` | `12,000.00` |
| `Live` | `Short` | `7.87` | 65,480,000.00 USD | 2,980.00 USD | 0.00 USD | `+84.97%` | `378.70` |
| `Live` | `Short` | `7.93` | 65,480,000.00 USD | 165.84 USD | 0.00 USD | `+86.61%` | `20.90` |
| `Live` | `Short` | `7.95` | 65,490,000.00 USD | 6,120.00 USD | 0.00 USD | `+86.85%` | `769.80` |
| `Live` | `Short` | `7.99` | 65,490,000.00 USD | 399.25 USD | 0.00 USD | `+87.79%` | `50.00` |
| `Live` | `Short` | `8.00` | 65,490,000.00 USD | 257.44 USD | 0.00 USD | `+88.03%` | `32.20` |
| `Live` | `Short` | `8.03` | 65,930,000.00 USD | 435,420.00 USD | 0.00 USD | `+88.73%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 65,930,000.00 USD | 6,450.00 USD | 0.00 USD | `+89.67%` | `800.00` |
| `Live` | `Short` | `8.19` | 66,000,000.00 USD | 63,470.00 USD | 0.00 USD | `+92.49%` | `7,754.90` |
| `Live` | `Short` | `8.20` | 66,000,000.00 USD | 951.44 USD | 0.00 USD | `+92.73%` | `116.10` |
| `Live` | `Short` | `8.21` | 66,050,000.00 USD | 51,690.00 USD | 0.00 USD | `+92.96%` | `6,300.00` |
| `Live` | `Short` | `8.35` | 66,070,000.00 USD | 25,310.00 USD | 0.00 USD | `+96.26%` | `3,032.60` |
| `Live` | `Short` | `8.37` | 67,170,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+96.73%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 67,180,000.00 USD | 8,900.00 USD | 0.00 USD | `+96.96%` | `1,062.50` |
| `Live` | `Short` | `8.46` | 67,180,000.00 USD | 1,230.00 USD | 0.00 USD | `+98.84%` | `145.00` |
| `Live` | `Short` | `8.47` | 67,180,000.00 USD | 816.99 USD | 0.00 USD | `+99.31%` | `96.40` |
| `Live` | `Short` | `8.48` | 67,190,000.00 USD | 6,640.00 USD | 0.00 USD | `+99.55%` | `782.50` |
| `Live` | `Short` | `8.51` | 67,620,000.00 USD | 428,200.00 USD | 0.00 USD | `+100.02%` | `50,346.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,130,000.00 USD | 0.00 USD | 585.51 USD | `-76.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,130,000.00 USD | 0.00 USD | 339.82 USD | `-76.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,130,000.00 USD | 0.00 USD | 196.58 USD | `-71.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,130,000.00 USD | 0.00 USD | 331.54 USD | `-68.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,130,000.00 USD | 0.00 USD | 345.25 USD | `-68.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,130,000.00 USD | 0.00 USD | 5,640.00 USD | `-67.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,120,000.00 USD | 0.00 USD | 997.29 USD | `-67.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,120,000.00 USD | 0.00 USD | 582.71 USD | `-65.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,120,000.00 USD | 0.00 USD | 139.83 USD | `-64.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,120,000.00 USD | 0.00 USD | 113.28 USD | `-63.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,120,000.00 USD | 0.00 USD | 4,000.00 USD | `-63.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,120,000.00 USD | 0.00 USD | 324.22 USD | `-63.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,120,000.00 USD | 0.00 USD | 4,590.00 USD | `-62.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,110,000.00 USD | 0.00 USD | 739.67 USD | `-62.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,110,000.00 USD | 0.00 USD | 1,740.00 USD | `-61.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,110,000.00 USD | 0.00 USD | 6,260.00 USD | `-61.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,100,000.00 USD | 0.00 USD | 345.40 USD | `-61.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,100,000.00 USD | 0.00 USD | 167.50 USD | `-60.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,100,000.00 USD | 0.00 USD | 669.02 USD | `-60.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,100,000.00 USD | 0.00 USD | 105.88 USD | `-59.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,100,000.00 USD | 0.00 USD | 172.50 USD | `-59.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,100,000.00 USD | 0.00 USD | 10,650.00 USD | `-58.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,090,000.00 USD | 0.00 USD | 722.00 USD | `-57.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,090,000.00 USD | 0.00 USD | 259.00 USD | `-57.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,090,000.00 USD | 0.00 USD | 103.84 USD | `-57.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,090,000.00 USD | 0.00 USD | 109.00 USD | `-56.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,090,000.00 USD | 0.00 USD | 222.19 USD | `-55.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,090,000.00 USD | 0.00 USD | 10,280.00 USD | `-55.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,080,000.00 USD | 0.00 USD | 558.36 USD | `-55.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,080,000.00 USD | 0.00 USD | 1,520.00 USD | `-54.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,080,000.00 USD | 0.00 USD | 222.14 USD | `-54.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,080,000.00 USD | 0.00 USD | 279.50 USD | `-54.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,080,000.00 USD | 0.00 USD | 197.50 USD | `-53.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,080,000.00 USD | 0.00 USD | 935.66 USD | `-53.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,080,000.00 USD | 0.00 USD | 18,860.00 USD | `-52.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,060,000.00 USD | 0.00 USD | 3,020.00 USD | `-52.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,050,000.00 USD | 0.00 USD | 214.52 USD | `-51.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,050,000.00 USD | 0.00 USD | 1,200.00 USD | `-51.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,050,000.00 USD | 0.00 USD | 578.41 USD | `-51.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,050,000.00 USD | 0.00 USD | 18,070.00 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,030,000.00 USD | 0.00 USD | 108.62 USD | `-50.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,030,000.00 USD | 0.00 USD | 107.23 USD | `-50.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,030,000.00 USD | 0.00 USD | 1,590.00 USD | `-50.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,030,000.00 USD | 0.00 USD | 5,830.00 USD | `-49.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,030,000.00 USD | 0.00 USD | 310.32 USD | `-49.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,030,000.00 USD | 0.00 USD | 1,170.00 USD | `-49.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,030,000.00 USD | 0.00 USD | 576.18 USD | `-48.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,020,000.00 USD | 0.00 USD | 295.67 USD | `-48.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,020,000.00 USD | 0.00 USD | 1,430.00 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,020,000.00 USD | 0.00 USD | 812.68 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,020,000.00 USD | 0.00 USD | 1,440.00 USD | `-47.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,020,000.00 USD | 0.00 USD | 106.16 USD | `-47.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,020,000.00 USD | 0.00 USD | 6,270.00 USD | `-47.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,010,000.00 USD | 0.00 USD | 478.06 USD | `-46.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,010,000.00 USD | 0.00 USD | 540.88 USD | `-46.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,010,000.00 USD | 0.00 USD | 867.46 USD | `-46.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,010,000.00 USD | 0.00 USD | 759.76 USD | `-46.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,010,000.00 USD | 0.00 USD | 11,060.00 USD | `-46.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,000,000.00 USD | 0.00 USD | 3,690.00 USD | `-45.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,000,000.00 USD | 0.00 USD | 722.15 USD | `-45.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,000,000.00 USD | 0.00 USD | 467.00 USD | `-45.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,000,000.00 USD | 0.00 USD | 506.75 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,000,000.00 USD | 0.00 USD | 214.27 USD | `-44.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,000,000.00 USD | 0.00 USD | 428.69 USD | `-44.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,990,000.00 USD | 0.00 USD | 322.45 USD | `-43.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,990,000.00 USD | 0.00 USD | 108.25 USD | `-43.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,990,000.00 USD | 0.00 USD | 3,900.00 USD | `-43.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,990,000.00 USD | 0.00 USD | 799.04 USD | `-42.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,990,000.00 USD | 0.00 USD | 6,830.00 USD | `-42.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,980,000.00 USD | 0.00 USD | 137.16 USD | `-42.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,980,000.00 USD | 0.00 USD | 504.41 USD | `-41.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,980,000.00 USD | 0.00 USD | 963.93 USD | `-41.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,980,000.00 USD | 0.00 USD | 6,690.00 USD | `-41.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,970,000.00 USD | 0.00 USD | 541.98 USD | `-40.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,970,000.00 USD | 0.00 USD | 108.75 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,970,000.00 USD | 0.00 USD | 766.55 USD | `-40.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,970,000.00 USD | 0.00 USD | 7,110.00 USD | `-39.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,970,000.00 USD | 0.00 USD | 1,100.00 USD | `-39.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,960,000.00 USD | 0.00 USD | 100.04 USD | `-39.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,960,000.00 USD | 0.00 USD | 390.75 USD | `-38.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,960,000.00 USD | 0.00 USD | 5,090.00 USD | `-38.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,960,000.00 USD | 0.00 USD | 226.57 USD | `-37.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,960,000.00 USD | 0.00 USD | 104.98 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,960,000.00 USD | 0.00 USD | 889.89 USD | `-36.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,960,000.00 USD | 0.00 USD | 7,270.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,950,000.00 USD | 0.00 USD | 107.21 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,950,000.00 USD | 0.00 USD | 197.37 USD | `-35.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,950,000.00 USD | 0.00 USD | 8,110.00 USD | `-35.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,940,000.00 USD | 0.00 USD | 108.39 USD | `-34.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,940,000.00 USD | 0.00 USD | 435.95 USD | `-34.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,940,000.00 USD | 0.00 USD | 217.23 USD | `-34.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,940,000.00 USD | 0.00 USD | 437.98 USD | `-34.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,940,000.00 USD | 0.00 USD | 1,230.00 USD | `-34.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,940,000.00 USD | 0.00 USD | 8,380.00 USD | `-33.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,930,000.00 USD | 0.00 USD | 283.50 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,930,000.00 USD | 0.00 USD | 109.53 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,930,000.00 USD | 0.00 USD | 1,230.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,930,000.00 USD | 0.00 USD | 1,960.00 USD | `-32.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,930,000.00 USD | 0.00 USD | 157.81 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,930,000.00 USD | 0.00 USD | 4,190.00 USD | `-31.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,920,000.00 USD | 0.00 USD | 4,870.00 USD | `-31.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,920,000.00 USD | 0.00 USD | 1,320.00 USD | `-31.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,920,000.00 USD | 0.00 USD | 1,090.00 USD | `-31.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,920,000.00 USD | 0.00 USD | 1,560.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,910,000.00 USD | 0.00 USD | 24,200.00 USD | `-30.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,890,000.00 USD | 0.00 USD | 738.75 USD | `-30.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,890,000.00 USD | 0.00 USD | 523.32 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,890,000.00 USD | 0.00 USD | 4,470.00 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,880,000.00 USD | 0.00 USD | 24,210.00 USD | `-29.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,860,000.00 USD | 0.00 USD | 1,020.00 USD | `-29.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,860,000.00 USD | 0.00 USD | 214.57 USD | `-28.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,860,000.00 USD | 0.00 USD | 249.08 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,860,000.00 USD | 0.00 USD | 305.50 USD | `-28.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,860,000.00 USD | 0.00 USD | 109.42 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,860,000.00 USD | 0.00 USD | 9,300.00 USD | `-26.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,850,000.00 USD | 0.00 USD | 8,570.00 USD | `-26.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,840,000.00 USD | 0.00 USD | 104.69 USD | `-26.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,840,000.00 USD | 0.00 USD | 315.69 USD | `-26.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,840,000.00 USD | 0.00 USD | 214.17 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,840,000.00 USD | 0.00 USD | 329.07 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,840,000.00 USD | 0.00 USD | 4,210.00 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,840,000.00 USD | 0.00 USD | 1,030.00 USD | `-25.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,830,000.00 USD | 0.00 USD | 218.81 USD | `-25.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,830,000.00 USD | 0.00 USD | 24,840.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,810,000.00 USD | 0.00 USD | 144.67 USD | `-24.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 2,810,000.00 USD | 0.00 USD | 273,030.00 USD | `-23.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,540,000.00 USD | 0.00 USD | 27,380.00 USD | `-23.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,510,000.00 USD | 0.00 USD | 1,560.00 USD | `-23.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,510,000.00 USD | 0.00 USD | 104.81 USD | `-23.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,510,000.00 USD | 0.00 USD | 200.10 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,510,000.00 USD | 0.00 USD | 1,480.00 USD | `-22.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,510,000.00 USD | 0.00 USD | 1,870.00 USD | `-22.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,500,000.00 USD | 0.00 USD | 18,240.00 USD | `-22.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,490,000.00 USD | 0.00 USD | 240.67 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,490,000.00 USD | 0.00 USD | 306.56 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,490,000.00 USD | 0.00 USD | 1,670.00 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,480,000.00 USD | 0.00 USD | 73,220.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,410,000.00 USD | 0.00 USD | 19,600.00 USD | `-20.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,390,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,380,000.00 USD | 0.00 USD | 102,530.00 USD | `-19.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,280,000.00 USD | 0.00 USD | 421.41 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,280,000.00 USD | 0.00 USD | 4,350.00 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,270,000.00 USD | 0.00 USD | 444.49 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,270,000.00 USD | 0.00 USD | 2,550.00 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,270,000.00 USD | 0.00 USD | 1,380.00 USD | `-18.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,270,000.00 USD | 0.00 USD | 344.07 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,270,000.00 USD | 0.00 USD | 24,320.00 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,250,000.00 USD | 0.00 USD | 17,430.00 USD | `-18.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,230,000.00 USD | 0.00 USD | 894.72 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,230,000.00 USD | 0.00 USD | 70,280.00 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,160,000.00 USD | 0.00 USD | 21,320.00 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,140,000.00 USD | 0.00 USD | 3,700.00 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,130,000.00 USD | 0.00 USD | 16,250.00 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,120,000.00 USD | 0.00 USD | 5,130.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,110,000.00 USD | 0.00 USD | 1,800.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,110,000.00 USD | 0.00 USD | 18,440.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,090,000.00 USD | 0.00 USD | 78,170.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,010,000.00 USD | 0.00 USD | 1,610.00 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,010,000.00 USD | 0.00 USD | 331.46 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,010,000.00 USD | 0.00 USD | 56,250.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,950,000.00 USD | 0.00 USD | 632.99 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,950,000.00 USD | 0.00 USD | 1,000.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,950,000.00 USD | 0.00 USD | 1,210.00 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,950,000.00 USD | 0.00 USD | 54,670.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,900,000.00 USD | 0.00 USD | 8,030.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,890,000.00 USD | 0.00 USD | 4,070.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,880,000.00 USD | 0.00 USD | 367.50 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,880,000.00 USD | 0.00 USD | 32,620.00 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,850,000.00 USD | 0.00 USD | 4,370.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,850,000.00 USD | 0.00 USD | 391,610.00 USD | `-12.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,460,000.00 USD | 0.00 USD | 6,300.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,450,000.00 USD | 0.00 USD | 821.36 USD | `-12.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,450,000.00 USD | 0.00 USD | 32,040.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,420,000.00 USD | 0.00 USD | 28,820.00 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,390,000.00 USD | 0.00 USD | 14,490.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,370,000.00 USD | 0.00 USD | 6,850.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,370,000.00 USD | 0.00 USD | 1,190.00 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,360,000.00 USD | 0.00 USD | 1,660.00 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,360,000.00 USD | 0.00 USD | 166,450.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,200,000.00 USD | 0.00 USD | 4,530.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,190,000.00 USD | 0.00 USD | 22,340.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,170,000.00 USD | 0.00 USD | 7,350.00 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,160,000.00 USD | 0.00 USD | 41,340.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,120,000.00 USD | 0.00 USD | 43,060.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,080,000.00 USD | 0.00 USD | 16,170.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,060,000.00 USD | 0.00 USD | 8,380.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,050,000.00 USD | 0.00 USD | 161,230.00 USD | `-8.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 892,470.00 USD | 0.00 USD | 27,360.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 865,110.00 USD | 0.00 USD | 10,330.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 854,780.00 USD | 0.00 USD | 46,610.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 808,170.00 USD | 0.00 USD | 2,340.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 805,840.00 USD | 0.00 USD | 6,910.00 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 798,930.00 USD | 0.00 USD | 934.17 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 797,990.00 USD | 0.00 USD | 3,940.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 794,060.00 USD | 0.00 USD | 2,780.00 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 791,280.00 USD | 0.00 USD | 22,700.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 768,580.00 USD | 0.00 USD | 791.02 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 767,790.00 USD | 0.00 USD | 42,280.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 725,500.00 USD | 0.00 USD | 667.16 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 724,840.00 USD | 0.00 USD | 179,460.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 545,380.00 USD | 0.00 USD | 9,720.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 535,660.00 USD | 0.00 USD | 58,180.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 477,480.00 USD | 0.00 USD | 428.11 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 477,050.00 USD | 0.00 USD | 919.83 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 476,130.00 USD | 0.00 USD | 71,120.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 405,010.00 USD | 0.00 USD | 113.41 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 404,900.00 USD | 0.00 USD | 3,880.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 401,020.00 USD | 0.00 USD | 6,340.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 394,680.00 USD | 0.00 USD | 11,540.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 383,150.00 USD | 0.00 USD | 30,490.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 352,660.00 USD | 0.00 USD | 89,870.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 262,790.00 USD | 0.00 USD | 11,940.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 250,850.00 USD | 0.00 USD | 54,000.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 196,850.00 USD | 0.00 USD | 16,900.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 179,950.00 USD | 0.00 USD | 56,810.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 123,140.00 USD | 0.00 USD | 20,560.00 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 102,590.00 USD | 0.00 USD | 1,220.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 101,360.00 USD | 0.00 USD | 13,390.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 87,980.00 USD | 0.00 USD | 126.69 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 87,850.00 USD | 0.00 USD | 62,370.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 25,490.00 USD | 0.00 USD | 982.52 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 24,500.00 USD | 0.00 USD | 1,130.00 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 23,370.00 USD | 0.00 USD | 18,180.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 5,190.00 USD | 0.00 USD | 5,190.00 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 23,900.00 USD | 23,900.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 26,290.00 USD | 2,390.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 27,500.00 USD | 1,200.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 27,640.00 USD | 143.98 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 62,210.00 USD | 34,570.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 81,520.00 USD | 19,320.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 121,290.00 USD | 39,760.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 121,470.00 USD | 182.52 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 122,660.00 USD | 1,190.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 140,040.00 USD | 17,380.00 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 155,460.00 USD | 15,410.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 316,470.00 USD | 161,010.00 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 406,100.00 USD | 89,630.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 474,210.00 USD | 68,110.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 655,170.00 USD | 180,960.00 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 677,220.00 USD | 22,050.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 680,930.00 USD | 3,710.00 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 683,900.00 USD | 2,970.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 691,540.00 USD | 7,640.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 692,650.00 USD | 1,110.00 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 761,320.00 USD | 68,670.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 768,150.00 USD | 6,830.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 768,530.00 USD | 375.90 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 769,840.00 USD | 1,310.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 777,300.00 USD | 7,460.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 788,650.00 USD | 11,350.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 807,590.00 USD | 18,940.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 914,370.00 USD | 106,780.00 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 915,070.00 USD | 699.75 USD | 0.00 USD | `+6.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 915,980.00 USD | 909.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 917,170.00 USD | 1,190.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 917,560.00 USD | 388.48 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 918,630.00 USD | 1,060.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 919,390.00 USD | 759.73 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 947,740.00 USD | 28,360.00 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,070,000.00 USD | 120,610.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,070,000.00 USD | 742.55 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,090,000.00 USD | 21,450.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,090,000.00 USD | 1,100.00 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,100,000.00 USD | 4,070.00 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,100,000.00 USD | 1,240.00 USD | 0.00 USD | `+9.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,170,000.00 USD | 77,690.00 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,180,000.00 USD | 617.10 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,190,000.00 USD | 15,710.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,190,000.00 USD | 152.12 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,620,000.00 USD | 429,960.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,860,000.00 USD | 234,370.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,860,000.00 USD | 2,650.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,940,000.00 USD | 84,180.00 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,950,000.00 USD | 6,160.00 USD | 0.00 USD | `+11.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,980,000.00 USD | 29,420.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,990,000.00 USD | 13,030.00 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,990,000.00 USD | 2,640.00 USD | 0.00 USD | `+12.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,810,000.00 USD | 818,540.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,810,000.00 USD | 559.58 USD | 0.00 USD | `+12.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,990,000.00 USD | 175,870.00 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,020,000.00 USD | 33,510.00 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,030,000.00 USD | 8,540.00 USD | 0.00 USD | `+13.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,120,000.00 USD | 93,100.00 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,180,000.00 USD | 59,460.00 USD | 0.00 USD | `+13.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,210,000.00 USD | 24,370.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,230,000.00 USD | 23,180.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,240,000.00 USD | 10,400.00 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,260,000.00 USD | 19,890.00 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,270,000.00 USD | 4,060.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,390,000.00 USD | 120,030.00 USD | 0.00 USD | `+15.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,390,000.00 USD | 156.30 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,400,000.00 USD | 13,180.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,400,000.00 USD | 4,420.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,400,000.00 USD | 313.51 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,410,000.00 USD | 7,900.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,460,000.00 USD | 47,350.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,460,000.00 USD | 187.06 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,550,000.00 USD | 92,570.00 USD | 0.00 USD | `+17.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,550,000.00 USD | 2,540.00 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,610,000.00 USD | 60,150.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,640,000.00 USD | 25,080.00 USD | 0.00 USD | `+17.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,640,000.00 USD | 5,030.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,660,000.00 USD | 19,640.00 USD | 0.00 USD | `+18.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,660,000.00 USD | 120.58 USD | 0.00 USD | `+18.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,680,000.00 USD | 14,690.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,680,000.00 USD | 5,860.00 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,770,000.00 USD | 87,450.00 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,780,000.00 USD | 5,460.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,780,000.00 USD | 178.33 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,850,000.00 USD | 70,250.00 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,860,000.00 USD | 15,350.00 USD | 0.00 USD | `+20.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,860,000.00 USD | 179.38 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,860,000.00 USD | 179.72 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,860,000.00 USD | 217.63 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,860,000.00 USD | 493.85 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,860,000.00 USD | 575.38 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,860,000.00 USD | 327.58 USD | 0.00 USD | `+21.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,870,000.00 USD | 163.85 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 3,990,000.00 USD | 120,930.00 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,020,000.00 USD | 38,230.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,030,000.00 USD | 1,710.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,030,000.00 USD | 432.63 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,030,000.00 USD | 2,620.00 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,030,000.00 USD | 537.61 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,450,000.00 USD | 420,400.00 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,450,000.00 USD | 278.52 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,450,000.00 USD | 589.22 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,450,000.00 USD | 733.03 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,450,000.00 USD | 423.60 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,460,000.00 USD | 12,620.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,460,000.00 USD | 381.09 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,470,000.00 USD | 961.16 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,470,000.00 USD | 1,570.00 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,470,000.00 USD | 5,650.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,470,000.00 USD | 160.11 USD | 0.00 USD | `+25.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,470,000.00 USD | 225.33 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,470,000.00 USD | 438.60 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,480,000.00 USD | 6,610.00 USD | 0.00 USD | `+26.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,520,000.00 USD | 40,880.00 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,540,000.00 USD | 19,950.00 USD | 0.00 USD | `+27.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,550,000.00 USD | 4,330.00 USD | 0.00 USD | `+27.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,550,000.00 USD | 639.61 USD | 0.00 USD | `+27.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,550,000.00 USD | 1,710.00 USD | 0.00 USD | `+27.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,560,000.00 USD | 12,600.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,560,000.00 USD | 1,020.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,650,000.00 USD | 87,720.00 USD | 0.00 USD | `+28.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,680,000.00 USD | 30,110.00 USD | 0.00 USD | `+28.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,680,000.00 USD | 863.89 USD | 0.00 USD | `+29.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,680,000.00 USD | 1,040.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,650,000.00 USD | 972,470.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,660,000.00 USD | 5,600.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,680,000.00 USD | 19,110.00 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,700,000.00 USD | 18,790.00 USD | 0.00 USD | `+30.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,760,000.00 USD | 58,030.00 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,800,000.00 USD | 46,110.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,820,000.00 USD | 14,320.00 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,830,000.00 USD | 11,740.00 USD | 0.00 USD | `+31.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,850,000.00 USD | 20,540.00 USD | 0.00 USD | `+31.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,850,000.00 USD | 384.94 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,850,000.00 USD | 1,300.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,850,000.00 USD | 347.06 USD | 0.00 USD | `+32.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,850,000.00 USD | 347.68 USD | 0.00 USD | `+32.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,850,000.00 USD | 839.41 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,850,000.00 USD | 3,290.00 USD | 0.00 USD | `+32.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,850,000.00 USD | 281.55 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,860,000.00 USD | 6,590.00 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,860,000.00 USD | 235.93 USD | 0.00 USD | `+33.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,870,000.00 USD | 5,860.00 USD | 0.00 USD | `+33.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,970,000.00 USD | 103,470.00 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,970,000.00 USD | 705.23 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 5,980,000.00 USD | 5,720.00 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,980,000.00 USD | 139.03 USD | 0.00 USD | `+35.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,980,000.00 USD | 2,480.00 USD | 0.00 USD | `+35.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 5,980,000.00 USD | 1,850.00 USD | 0.00 USD | `+35.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,980,000.00 USD | 286.94 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 5,990,000.00 USD | 7,120.00 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 5,990,000.00 USD | 329.13 USD | 0.00 USD | `+36.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,990,000.00 USD | 1,970.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,990,000.00 USD | 1,020.00 USD | 0.00 USD | `+37.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 5,990,000.00 USD | 1,150.00 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,000,000.00 USD | 1,190.00 USD | 0.00 USD | `+37.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,000,000.00 USD | 1,770.00 USD | 0.00 USD | `+37.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,000,000.00 USD | 3,450.00 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,000,000.00 USD | 345.45 USD | 0.00 USD | `+38.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,080,000.00 USD | 81,590.00 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,080,000.00 USD | 1,670.00 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,080,000.00 USD | 1,020.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,240,000.00 USD | 153,150.00 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,260,000.00 USD | 26,180.00 USD | 0.00 USD | `+40.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,270,000.00 USD | 5,440.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,280,000.00 USD | 8,940.00 USD | 0.00 USD | `+40.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,400,000.00 USD | 119,340.00 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,410,000.00 USD | 7,340.00 USD | 0.00 USD | `+40.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,610,000.00 USD | 205,320.00 USD | 0.00 USD | `+41.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,620,000.00 USD | 13,710.00 USD | 0.00 USD | `+41.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,710,000.00 USD | 90,380.00 USD | 0.00 USD | `+41.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,720,000.00 USD | 2,080.00 USD | 0.00 USD | `+41.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,720,000.00 USD | 3,300.00 USD | 0.00 USD | `+42.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,720,000.00 USD | 1,040.00 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,720,000.00 USD | 425.76 USD | 0.00 USD | `+42.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,720,000.00 USD | 2,030.00 USD | 0.00 USD | `+42.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,730,000.00 USD | 4,120.00 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 6,730,000.00 USD | 2,000.00 USD | 0.00 USD | `+43.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,790,000.00 USD | 61,050.00 USD | 0.00 USD | `+43.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,790,000.00 USD | 1,610.00 USD | 0.00 USD | `+43.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,790,000.00 USD | 1,200.00 USD | 0.00 USD | `+44.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,790,000.00 USD | 420.32 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,800,000.00 USD | 1,940.00 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,800,000.00 USD | 4,010.00 USD | 0.00 USD | `+45.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,870,000.00 USD | 66,060.00 USD | 0.00 USD | `+45.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,870,000.00 USD | 1,890.00 USD | 0.00 USD | `+46.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,870,000.00 USD | 195.46 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,870,000.00 USD | 289.93 USD | 0.00 USD | `+46.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,870,000.00 USD | 116.16 USD | 0.00 USD | `+46.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,880,000.00 USD | 7,310.00 USD | 0.00 USD | `+48.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,880,000.00 USD | 310.70 USD | 0.00 USD | `+48.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,880,000.00 USD | 325.62 USD | 0.00 USD | `+48.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,880,000.00 USD | 1,760.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,880,000.00 USD | 3,230.00 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,890,000.00 USD | 5,120.00 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,890,000.00 USD | 1,310.00 USD | 0.00 USD | `+52.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,920,000.00 USD | 30,990.00 USD | 0.00 USD | `+52.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,920,000.00 USD | 104.24 USD | 0.00 USD | `+53.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,930,000.00 USD | 13,580.00 USD | 0.00 USD | `+53.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,930,000.00 USD | 1,630.00 USD | 0.00 USD | `+54.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,940,000.00 USD | 1,370.00 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,940,000.00 USD | 5,400.00 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,940,000.00 USD | 1,620.00 USD | 0.00 USD | `+55.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,940,000.00 USD | 450.55 USD | 0.00 USD | `+56.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,950,000.00 USD | 3,060.00 USD | 0.00 USD | `+56.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,950,000.00 USD | 3,070.00 USD | 0.00 USD | `+57.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,950,000.00 USD | 1,550.00 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 6,950,000.00 USD | 3,080.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,950,000.00 USD | 647.56 USD | 0.00 USD | `+59.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,960,000.00 USD | 1,420.00 USD | 0.00 USD | `+60.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,960,000.00 USD | 2,130.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 6,960,000.00 USD | 6,870.00 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 6,970,000.00 USD | 342.25 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 6,970,000.00 USD | 2,990.00 USD | 0.00 USD | `+61.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 6,970,000.00 USD | 2,970.00 USD | 0.00 USD | `+62.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 6,970,000.00 USD | 324.54 USD | 0.00 USD | `+62.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 6,970,000.00 USD | 504.21 USD | 0.00 USD | `+63.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 6,970,000.00 USD | 166.00 USD | 0.00 USD | `+64.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 6,980,000.00 USD | 4,190.00 USD | 0.00 USD | `+64.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 6,990,000.00 USD | 13,480.00 USD | 0.00 USD | `+64.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 6,990,000.00 USD | 2,860.00 USD | 0.00 USD | `+65.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 6,990,000.00 USD | 264.31 USD | 0.00 USD | `+67.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 6,990,000.00 USD | 599.34 USD | 0.00 USD | `+67.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 6,990,000.00 USD | 193.19 USD | 0.00 USD | `+68.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,000,000.00 USD | 3,950.00 USD | 0.00 USD | `+68.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,000,000.00 USD | 1,940.00 USD | 0.00 USD | `+69.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,160,000.00 USD | 160,550.00 USD | 0.00 USD | `+70.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,160,000.00 USD | 1,290.00 USD | 0.00 USD | `+71.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,160,000.00 USD | 1,180.00 USD | 0.00 USD | `+72.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,160,000.00 USD | 630.05 USD | 0.00 USD | `+73.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,160,000.00 USD | 1,410.00 USD | 0.00 USD | `+74.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,170,000.00 USD | 2,610.00 USD | 0.00 USD | `+74.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,170,000.00 USD | 7,630.00 USD | 0.00 USD | `+76.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,180,000.00 USD | 4,640.00 USD | 0.00 USD | `+78.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,180,000.00 USD | 371.88 USD | 0.00 USD | `+78.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,180,000.00 USD | 2,510.00 USD | 0.00 USD | `+79.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,180,000.00 USD | 380.68 USD | 0.00 USD | `+80.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,190,000.00 USD | 11,170.00 USD | 0.00 USD | `+83.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,230,000.00 USD | 34,360.00 USD | 0.00 USD | `+83.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,230,000.00 USD | 253.21 USD | 0.00 USD | `+83.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,230,000.00 USD | 100.29 USD | 0.00 USD | `+84.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,240,000.00 USD | 10,610.00 USD | 0.00 USD | `+87.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,240,000.00 USD | 309.43 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 7,240,000.00 USD | 4,640.00 USD | 0.00 USD | `+87.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,280,000.00 USD | 36,740.00 USD | 0.00 USD | `+88.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,360,000.00 USD | 81,310.00 USD | 0.00 USD | `+88.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,360,000.00 USD | 216.90 USD | 0.00 USD | `+92.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,360,000.00 USD | 1,990.00 USD | 0.00 USD | `+92.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,370,000.00 USD | 7,200.00 USD | 0.00 USD | `+92.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,370,000.00 USD | 1,350.00 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,370,000.00 USD | 998.65 USD | 0.00 USD | `+97.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,380,000.00 USD | 1,260.00 USD | 0.00 USD | `+97.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,480,000.00 USD | 103,010.00 USD | 0.00 USD | `+97.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 7,480,000.00 USD | 1,330.00 USD | 0.00 USD | `+98.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 7,480,000.00 USD | 721.22 USD | 0.00 USD | `+99.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 7,490,000.00 USD | 5,130.00 USD | 0.00 USD | `+100.02%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.48` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,180.00 USD |
| `7D` | `3.50` | 18,400,000.00 USD | 0.00 USD | 18,400,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD |
| `7D` | `3.51` | 18,340,000.00 USD | 0.00 USD | 18,340,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD |
| `7D` | `3.52` | 18,340,000.00 USD | 0.00 USD | 18,340,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `3.53` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 17,960,000.00 USD | 0.00 USD | 17,960,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 17,730,000.00 USD | 0.00 USD | 17,730,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 17,670,000.00 USD | 0.00 USD | 17,670,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 16,920,000.00 USD | 0.00 USD | 16,920,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 16,710,000.00 USD | 0.00 USD | 16,710,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 16,650,000.00 USD | 0.00 USD | 16,650,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 16,390,000.00 USD | 0.00 USD | 16,390,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `7D` | `3.71` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `7D` | `3.72` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `7D` | `3.73` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `7D` | `3.74` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `7D` | `3.75` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `7D` | `3.76` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `7D` | `3.77` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `7D` | `3.78` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 9,260.00 USD | 24,440.00 USD | 91,470.00 USD |
| `7D` | `3.79` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `1D` | `3.80` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 3,400.00 USD | 0.00 USD | 76,900.00 USD |
| `7D` | `3.80` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD |
| `1D` | `3.81` | 17,520,000.00 USD | 0.00 USD | 17,520,000.00 USD | 213,700.00 USD | 0.00 USD | 101,930.00 USD |
| `7D` | `3.81` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD |
| `1D` | `3.82` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 49,390.00 USD | 31,910.00 USD | 141,180.00 USD |
| `7D` | `3.82` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 125,840.00 USD | 125,330.00 USD | 113,210.00 USD |
| `7D` | `3.83` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD |
| `1D` | `3.84` | 16,620,000.00 USD | 0.00 USD | 16,620,000.00 USD | 150,080.00 USD | 46,190.00 USD | 65,110.00 USD |
| `7D` | `3.84` | 14,480,000.00 USD | 0.00 USD | 14,480,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD |
| `1D` | `3.85` | 16,350,000.00 USD | 0.00 USD | 16,350,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,540.00 USD |
| `7D` | `3.85` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD |
| `1D` | `3.86` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 39,130.00 USD | 39,050.00 USD | 53,300.00 USD |
| `7D` | `3.86` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 5,190.00 USD | 173,980.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 52,700.00 USD | 58,230.00 USD | 189,120.00 USD |
| `7D` | `3.87` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 63,710.00 USD | 0.00 USD | 227,340.00 USD |
| `1D` | `3.88` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 35,520.00 USD | 17,520.00 USD | 223,290.00 USD |
| `7D` | `3.88` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD |
| `1D` | `3.89` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 373,610.00 USD | 91,480.00 USD | 236,910.00 USD |
| `7D` | `3.89` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 33,360.00 USD | 49,080.00 USD | 226,180.00 USD |
| `7D` | `3.90` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD |
| `1D` | `3.91` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 337,710.00 USD | 120,100.00 USD | 286,760.00 USD |
| `7D` | `3.91` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 121,570.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 317,510.00 USD | 8,570.00 USD | 125,890.00 USD |
| `7D` | `3.92` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 85,790.00 USD | 66,710.00 USD | 104,900.00 USD |
| `1D` | `3.93` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 116,350.00 USD | 99,220.00 USD | 99,870.00 USD |
| `7D` | `3.93` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 12,720,000.00 USD | 0.00 USD | 12,720,000.00 USD | 132,520.00 USD | 53,060.00 USD | 141,980.00 USD |
| `7D` | `3.94` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3.95` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD |
| `7D` | `3.95` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `3.96` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,440.00 USD |
| `7D` | `3.96` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD |
| `1D` | `3.97` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,570.00 USD |
| `7D` | `3.97` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `3.98` | 11,960,000.00 USD | 0.00 USD | 11,960,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,570.00 USD |
| `7D` | `3.98` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD |
| `1D` | `3.99` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,320.00 USD |
| `7D` | `3.99` | 11,130,000.00 USD | 0.00 USD | 11,130,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD |
| `1D` | `4.00` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,740.00 USD |
| `7D` | `4.00` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD |
| `1D` | `4.01` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 473.90 USD | 158,450.00 USD | 222,870.00 USD |
| `7D` | `4.01` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 371,710.00 USD | 57,440.00 USD | 438,780.00 USD |
| `1D` | `4.02` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,210.00 USD |
| `7D` | `4.02` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,090.00 USD |
| `1D` | `4.03` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 64,700.00 USD | 59,350.00 USD | 269.89 USD |
| `7D` | `4.03` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 247,960.00 USD | 0.00 USD | 344,750.00 USD |
| `1D` | `4.04` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,230.00 USD |
| `7D` | `4.04` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD |
| `1D` | `4.05` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 348,930.00 USD | 23,720.00 USD | 119.81 USD |
| `7D` | `4.05` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 0.00 USD | 41,020.00 USD | 68,490.00 USD |
| `1D` | `4.06` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,570.00 USD |
| `7D` | `4.06` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 0.00 USD | 72,410.00 USD | 292.74 USD |
| `1D` | `4.07` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 357,260.00 USD | 205,460.00 USD | 334,270.00 USD |
| `7D` | `4.07` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD |
| `1D` | `4.08` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,620.00 USD |
| `7D` | `4.08` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD |
| `1D` | `4.09` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 243,890.00 USD | 60,230.00 USD | 168,320.00 USD |
| `7D` | `4.09` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 253,510.00 USD | 179,350.00 USD | 432,940.00 USD |
| `1D` | `4.10` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 2,770.00 USD | 89,650.00 USD | 140,980.00 USD |
| `7D` | `4.10` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 27,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.11` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,420.00 USD |
| `7D` | `4.11` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD |
| `1D` | `4.12` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,240.00 USD |
| `7D` | `4.12` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 181,330.00 USD | 0.00 USD |
| `1D` | `4.13` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 159,720.00 USD | 0.00 USD | 398,110.00 USD |
| `7D` | `4.13` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 154,140.00 USD | 0.00 USD | 237,490.00 USD |
| `1D` | `4.14` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 96,750.00 USD | 0.00 USD | 97,160.00 USD |
| `7D` | `4.14` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 238,150.00 USD | 217,700.00 USD | 345,750.00 USD |
| `1D` | `4.15` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 469,190.00 USD | 79,810.00 USD | 318,980.00 USD |
| `7D` | `4.15` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 276,920.00 USD | 51,570.00 USD | 316,310.00 USD |
| `1D` | `4.17` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 215,050.00 USD | 283,430.00 USD | 238,980.00 USD |
| `7D` | `4.17` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD |
| `1D` | `4.18` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 329,080.00 USD | 62,340.00 USD | 158,690.00 USD |
| `7D` | `4.18` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD |
| `1D` | `4.19` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 148,260.00 USD | 115,850.00 USD | 245,080.00 USD |
| `7D` | `4.19` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.20` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 540.30 USD | 26,180.00 USD | 132,050.00 USD |
| `7D` | `4.20` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,300.00 USD |
| `7D` | `4.21` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD |
| `7D` | `4.22` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 119,070.00 USD | 89,680.00 USD | 417,550.00 USD |
| `1D` | `4.23` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 70,340.00 USD | 177,020.00 USD |
| `1D` | `4.24` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 419.33 USD |
| `1D` | `4.25` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 186,610.00 USD |
| `7D` | `4.25` | 485,290.00 USD | 0.00 USD | 485,290.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.26` | 832,540.00 USD | 0.00 USD | 832,540.00 USD | 0.00 USD | 0.00 USD | 736.24 USD |
| `7D` | `4.26` | 481,900.00 USD | 0.00 USD | 481,900.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD |
| `7D` | `4.27` | 305,790.00 USD | 0.00 USD | 305,790.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.28` | 831,810.00 USD | 0.00 USD | 831,810.00 USD | 4,310.00 USD | 0.00 USD | 316.62 USD |
| `7D` | `4.28` | 280,970.00 USD | 0.00 USD | 280,970.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.29` | 827,180.00 USD | 0.00 USD | 827,180.00 USD | 156,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.29` | 275,590.00 USD | 0.00 USD | 275,590.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.31` | 671,130.00 USD | 0.00 USD | 671,130.00 USD | 0.00 USD | 0.00 USD | 865.89 USD |
| `7D` | `4.31` | 270,440.00 USD | 0.00 USD | 270,440.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.32` | 670,270.00 USD | 0.00 USD | 670,270.00 USD | 381,790.00 USD | 0.00 USD | 151.98 USD |
| `7D` | `4.32` | 268,260.00 USD | 0.00 USD | 268,260.00 USD | 268,260.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.33` | 288,330.00 USD | 0.00 USD | 288,330.00 USD | 287,160.00 USD | 0.00 USD | 1,170.00 USD |
| `7D` | `4.33` | 8,950.00 USD | 8,950.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.33` | 17,900.00 USD | 17,900.00 USD | 0.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.34` | 269,670.00 USD | 269,670.00 USD | 0.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.34` | 539,330.00 USD | 539,330.00 USD | 0.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.34` | 34,780.00 USD | 34,780.00 USD | 0.00 USD | 9,550.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `4.35` | 697,990.00 USD | 697,990.00 USD | 0.00 USD | 157,030.00 USD | 0.00 USD | 1,630.00 USD |
| `7D` | `4.35` | 289,880.00 USD | 289,880.00 USD | 0.00 USD | 255,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.36` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 108,840.00 USD | 93,400.00 USD | 281,130.00 USD |
| `7D` | `4.36` | 300,340.00 USD | 300,340.00 USD | 0.00 USD | 10,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.37` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 281,560.00 USD | 173,170.00 USD | 400,530.00 USD |
| `7D` | `4.37` | 744,200.00 USD | 744,200.00 USD | 0.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.38` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 250,760.00 USD | 60,680.00 USD | 638,650.00 USD |
| `7D` | `4.38` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 356,920.00 USD | 41,380.00 USD | 508,210.00 USD |
| `7D` | `4.39` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD |
| `1D` | `4.40` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 458,500.00 USD | 58,380.00 USD | 353,100.00 USD |
| `7D` | `4.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 111,810.00 USD | 116,620.00 USD | 881,540.00 USD |
| `1D` | `4.41` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 336,310.00 USD | 272,870.00 USD | 589,990.00 USD |
| `7D` | `4.41` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 1,450.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 1,080.00 USD | 142,250.00 USD | 130,960.00 USD |
| `7D` | `4.42` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 84,650.00 USD | 109,630.00 USD | 306,410.00 USD |
| `7D` | `4.43` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD |
| `1D` | `4.44` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 156,430.00 USD | 370,280.00 USD | 367,190.00 USD |
| `7D` | `4.44` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD |
| `1D` | `4.45` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 76,860.00 USD | 108,640.00 USD | 122,400.00 USD |
| `7D` | `4.45` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD |
| `1D` | `4.46` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 4,580.00 USD | 37,160.00 USD | 31,690.00 USD |
| `7D` | `4.46` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD |
| `1D` | `4.47` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 160,740.00 USD | 25,190.00 USD | 120,000.00 USD |
| `7D` | `4.47` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD |
| `1D` | `4.48` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 205,250.00 USD | 86,520.00 USD | 121,140.00 USD |
| `7D` | `4.48` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 1,870.00 USD | 44,840.00 USD | 210,580.00 USD |
| `1D` | `4.49` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 253,770.00 USD | 213,100.00 USD | 357,060.00 USD |
| `7D` | `4.49` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 244,370.00 USD | 93,790.00 USD | 162.91 USD |
| `1D` | `4.50` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 363,660.00 USD | 69,580.00 USD | 178,610.00 USD |
| `7D` | `4.50` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD |
| `1D` | `4.51` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 188,660.00 USD | 149,810.00 USD | 416,190.00 USD |
| `7D` | `4.51` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `4.52` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 288,560.00 USD | 92,260.00 USD | 243,290.00 USD |
| `7D` | `4.52` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 225,130.00 USD |
| `1D` | `4.53` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 505,320.00 USD | 0.00 USD | 278,060.00 USD |
| `7D` | `4.53` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 309,760.00 USD |
| `1D` | `4.54` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 15,720.00 USD | 150,600.00 USD | 234,280.00 USD |
| `7D` | `4.54` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 1,620.00 USD | 34,450.00 USD | 109,370.00 USD |
| `7D` | `4.55` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 237.10 USD |
| `1D` | `4.56` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 81,450.00 USD | 32,800.00 USD | 288,710.00 USD |
| `7D` | `4.56` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 219.44 USD |
| `1D` | `4.57` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 176,460.00 USD | 70,180.00 USD | 98,660.00 USD |
| `7D` | `4.57` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,430.00 USD |
| `1D` | `4.58` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 421,530.00 USD | 99,430.00 USD | 633,120.00 USD |
| `7D` | `4.58` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD |
| `1D` | `4.59` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 418,290.00 USD | 75,460.00 USD | 109,530.00 USD |
| `7D` | `4.59` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD |
| `1D` | `4.60` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 49,460.00 USD | 50,860.00 USD | 67,520.00 USD |
| `7D` | `4.60` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 64,340.00 USD | 7,560.00 USD | 76,020.00 USD |
| `7D` | `4.61` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 5,400.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 94,450.00 USD | 31,380.00 USD | 19,760.00 USD |
| `7D` | `4.62` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD |
| `1D` | `4.63` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4.63` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 16,010,000.00 USD | 16,010,000.00 USD | 0.00 USD | 106,430.00 USD | 11,270.00 USD | 43,760.00 USD |
| `7D` | `4.64` | 13,760,000.00 USD | 13,760,000.00 USD | 0.00 USD | 503,610.00 USD | 34,570.00 USD | 1,730.00 USD |
| `1D` | `4.65` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 202,440.00 USD | 52,020.00 USD | 484,770.00 USD |
| `7D` | `4.65` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `4.66` | 17,540,000.00 USD | 17,540,000.00 USD | 0.00 USD | 202,480.00 USD | 309,340.00 USD | 276,860.00 USD |
| `7D` | `4.66` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 88,770.00 USD | 0.00 USD | 259,390.00 USD |
| `7D` | `4.67` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 18,090,000.00 USD | 18,090,000.00 USD | 0.00 USD | 60,330.00 USD | 106,120.00 USD | 35,360.00 USD |
| `7D` | `4.68` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD |
| `1D` | `4.69` | 18,470,000.00 USD | 18,470,000.00 USD | 0.00 USD | 168,690.00 USD | 49,160.00 USD | 168,740.00 USD |
| `7D` | `4.69` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 69,690.00 USD | 97,490.00 USD | 175,300.00 USD |
| `7D` | `4.70` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD |
| `1D` | `4.71` | 19,860,000.00 USD | 19,860,000.00 USD | 0.00 USD | 390,710.00 USD | 298,900.00 USD | 353,560.00 USD |
| `7D` | `4.71` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD |
| `1D` | `4.72` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 2,370.00 USD | 181,280.00 USD | 49,910.00 USD |
| `7D` | `4.72` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 109,760.00 USD | 25,210.00 USD | 35,630.00 USD |
| `7D` | `4.73` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 894.74 USD |
| `1D` | `4.74` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 68,200.00 USD | 132,280.00 USD | 176,160.00 USD |
| `7D` | `4.74` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD |
| `1D` | `4.75` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 76,690.00 USD | 132,460.00 USD | 151,890.00 USD |
| `7D` | `4.75` | 17,630,000.00 USD | 17,630,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 32,430.00 USD | 51,460.00 USD | 32,220.00 USD |
| `7D` | `4.76` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD |
| `1D` | `4.77` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 4,870.00 USD | 85,030.00 USD | 57,260.00 USD |
| `7D` | `4.77` | 19,890,000.00 USD | 19,890,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 37,290.00 USD | 20,000.00 USD | 86,970.00 USD |
| `7D` | `4.78` | 21,020,000.00 USD | 21,020,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 112,300.00 USD | 44,330.00 USD | 41,930.00 USD |
| `7D` | `4.79` | 22,050,000.00 USD | 22,050,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `1D` | `4.80` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 225,790.00 USD | 136,530.00 USD | 159,460.00 USD |
| `7D` | `4.80` | 23,640,000.00 USD | 23,640,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | 11,890.00 USD |
| `7D` | `4.81` | 24,270,000.00 USD | 24,270,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 27,040,000.00 USD | 27,040,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 28,690,000.00 USD | 28,690,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 29,180,000.00 USD | 29,180,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 466,560.00 USD | 380,760.00 USD | 1,160,000.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `259,150,648.2 NEAR`
  * 1h OI Change: `+1.69%` | 4h OI Change: `+2.76%` | 24h OI Change: `-11.63%`
  * Exchange Breakdown: Binance=`199.81M` | Bybit=`150.51M` | OKX=`52.23M` | Hyperliquid=`248.27M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-157.01K` | Last 24h: `-22.13K` | Last 3d: `231.31K` | Last 7d: `198.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0004%` | **USDT OKX** | `-0.0297%` |
| **USDT Bybit** | `-0.0950%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0004%` | **USDT BingX** | `0.0008%` |
| **USDT Gate** | `-0.0350%` | **USDT Bitget** | `-0.0472%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `41.24%` | `58.76%` | `0.70` | 5,380,000.00 USD |
| `15M` | `Binance` | `48.77%` | `51.23%` | `0.95` | 1,370,000.00 USD |
| `15M` | `OKX` | `38.97%` | `61.03%` | `0.64` | 276,400.00 USD |
| `15M` | `Bybit` | `44.11%` | `55.89%` | `0.79` | 280,050.00 USD |
| `15M` | `KuCoin` | `47.77%` | `52.23%` | `0.91` | 14,910.00 USD |
| `15M` | `Gate` | `66.53%` | `33.47%` | `1.99` | 55,310.00 USD |
| `15M` | `Bitget` | `44.7%` | `55.3%` | `0.81` | 95,050.00 USD |
| `15M` | `BingX` | `9.22%` | `90.78%` | `0.10` | 619,130.00 USD |
| `15M` | `MEXC` | `49.86%` | `50.14%` | `0.99` | 1,360,000.00 USD |
| `15M` | `Bitunix` | `67.85%` | `32.15%` | `2.11` | 147,990.00 USD |
| `15M` | `Hyperliquid` | `67.39%` | `32.61%` | `2.07` | 126,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.74%` | `50.26%` | `0.99` | 570,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.09%` | `99.91%` | `0.00` | 423,910.00 USD |
| `15M` | `HTX` | `72.71%` | `27.29%` | `2.66` | 22,060.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.05%` | `26.95%` | `2.71` | 7,240.00 USD |
| `15M` | `Aster` | `49.43%` | `50.57%` | `0.98` | 4,560.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.93%` | `2.07%` | `47.31` | 4,250.00 USD |
| `15M` | `Whale Positions` | `48.77%` | `51.23%` | `0.95` | 1,370,000.00 USD |
| `15M` | `Global Accounts` | `41.24%` | `58.76%` | `0.70` | 5,380,000.00 USD |
| `1H` | `NEAR` | `45.60%` | `54.40%` | `0.84` | 16,730,000.00 USD |
| `1H` | `Binance` | `47.97%` | `52.03%` | `0.92` | 5,400,000.00 USD |
| `1H` | `OKX` | `39.35%` | `60.65%` | `0.65` | 1,190,000.00 USD |
| `1H` | `Bybit` | `42.8%` | `57.2%` | `0.75` | 902,510.00 USD |
| `1H` | `KuCoin` | `48.51%` | `51.49%` | `0.94` | 126,080.00 USD |
| `1H` | `Gate` | `61.13%` | `38.87%` | `1.57` | 303,930.00 USD |
| `1H` | `Bitget` | `45.49%` | `54.51%` | `0.83` | 237,270.00 USD |
| `1H` | `BingX` | `19.34%` | `80.66%` | `0.24` | 4,000,000.00 USD |
| `1H` | `MEXC` | `44.47%` | `55.53%` | `0.80` | 613,360.00 USD |
| `1H` | `Bitunix` | `42.84%` | `57.16%` | `0.75` | 348,590.00 USD |
| `1H` | `Hyperliquid` | `22.06%` | `77.94%` | `0.28` | 251,490.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.24%` | `38.76%` | `1.58` | 2,620,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 4,020.00 USD |
| `1H` | `WhiteBIT` | `94.22%` | `5.78%` | `16.30` | 627,720.00 USD |
| `1H` | `HTX` | `39.18%` | `60.82%` | `0.64` | 34,010.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.96%` | `46.04%` | `1.17` | 16,040.00 USD |
| `1H` | `Aster` | `32.98%` | `67.02%` | `0.49` | 10,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `19.8%` | `80.2%` | `0.25` | 43,510.00 USD |
| `1H` | `Whale Positions` | `47.97%` | `52.03%` | `0.92` | 5,400,000.00 USD |
| `1H` | `Global Accounts` | `45.60%` | `54.40%` | `0.84` | 16,730,000.00 USD |
| `4H` | `NEAR` | `48.34%` | `51.66%` | `0.94` | 73,560,000.00 USD |
| `4H` | `Binance` | `46.3%` | `53.7%` | `0.86` | 24,340,000.00 USD |
| `4H` | `OKX` | `46.57%` | `53.43%` | `0.87` | 4,290,000.00 USD |
| `4H` | `Bybit` | `51.18%` | `48.82%` | `1.05` | 4,990,000.00 USD |
| `4H` | `KuCoin` | `49.04%` | `50.96%` | `0.96` | 413,450.00 USD |
| `4H` | `Gate` | `46.73%` | `53.27%` | `0.88` | 1,710,000.00 USD |
| `4H` | `Bitget` | `51.07%` | `48.93%` | `1.04` | 1,300,000.00 USD |
| `4H` | `BingX` | `37.82%` | `62.18%` | `0.61` | 17,210,000.00 USD |
| `4H` | `MEXC` | `51.84%` | `48.16%` | `1.08` | 3,760,000.00 USD |
| `4H` | `Bitunix` | `49.41%` | `50.59%` | `0.98` | 1,290,000.00 USD |
| `4H` | `Hyperliquid` | `58.65%` | `41.35%` | `1.42` | 562,950.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.22%` | `49.78%` | `1.01` | 12,150,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 5,250.00 USD |
| `4H` | `WhiteBIT` | `51.38%` | `48.62%` | `1.06` | 1,260,000.00 USD |
| `4H` | `HTX` | `42.66%` | `57.34%` | `0.74` | 60,970.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.58%` | `37.42%` | `1.67` | 16,800.00 USD |
| `4H` | `Aster` | `40.78%` | `59.22%` | `0.69` | 86,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.82%` | `45.18%` | `1.21` | 128,740.00 USD |
| `4H` | `Whale Positions` | `46.3%` | `53.7%` | `0.86` | 24,340,000.00 USD |
| `4H` | `Global Accounts` | `48.34%` | `51.66%` | `0.94` | 73,560,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.28` | `4.28` | `4.28` | `4.32` | `4.23` | 16,362,042.19 USD | 9,388,667.85 USD | 6,973,374.34 USD | 2,415,293.52 USD | `+14.76%` | `21B / 0S` |
| `0:00 UTC` | `4.31` | `4.31` | `4.31` | `4.33` | `4.29` | 8,450,528.91 USD | 3,282,248.80 USD | 5,168,280.11 USD | -1,886,031.31 USD | `-22.32%` | `1B / 7S` |
| `5:00 UTC` | `4.34` | `4.31` | `4.34` | `4.36` | `4.27` | 7,427,881.94 USD | 3,957,867.39 USD | 3,470,014.55 USD | 487,852.84 USD | `+6.57%` | `16B / 5S` |
| `0:00 UTC` | `4.31` | `4.31` | `4.31` | `4.34` | `4.28` | 9,663,695.00 USD | 3,248,414.35 USD | 6,415,280.65 USD | -3,166,866.30 USD | `-32.77%` | `1B / 19S` |
| `5:00 UTC` | `4.28` | `4.29` | `4.28` | `4.30` | `4.28` | 4,754,194.91 USD | 2,441,201.28 USD | 2,312,993.62 USD | 128,207.66 USD | `+2.70%` | `1B / 2S` |
| `0:00 UTC` | `4.25` | `4.26` | `4.25` | `4.30` | `4.21` | 16,835,236.87 USD | 7,874,403.92 USD | 8,960,832.95 USD | -1,086,429.03 USD | `-6.45%` | `8B / 9S` |
| `5:00 UTC` | `4.25` | `4.25` | `4.25` | `4.26` | `4.23` | 9,185,944.44 USD | 4,818,806.27 USD | 4,367,138.17 USD | 451,668.11 USD | `+4.92%` | `4B / 5S` |
| `0:00 UTC` | `4.30` | `4.30` | `4.30` | `4.36` | `4.24` | 30,489,684.47 USD | 19,297,257.05 USD | 11,192,427.43 USD | 8,104,829.62 USD | `+26.58%` | `32B / 2S` |
| `5:00 UTC` | `4.35` | `4.35` | `4.35` | `4.36` | `4.33` | 15,245,662.84 USD | 8,049,667.44 USD | 7,195,995.40 USD | 853,672.05 USD | `+5.60%` | `0B / 3S` |
| `0:00 UTC` | `4.33` | `4.33` | `4.33` | `4.35` | `4.32` | 4,221,837.40 USD | 1,828,351.48 USD | 2,393,485.91 USD | -565,134.43 USD | `-13.39%` | `1B / 4S` |

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
| `5m` | -136,050.00 USD | -830,040.00 USD | **`DISTRIBUTION`** |
| `15m` | -315,470.00 USD | -1,500,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 4,010,000.00 USD | 4,680,000.00 USD | **`ACCUMULATION`** |
| `1h` | 9,130,000.00 USD | 11,200,000.00 USD | **`ACCUMULATION`** |
| `2h` | 8,600,000.00 USD | 2,230,000.00 USD | **`ACCUMULATION`** |
| `4h` | 14,990,000.00 USD | -557,700.00 USD | **`ACCUMULATION`** |
| `6h` | 19,370,000.00 USD | 10,020,000.00 USD | **`ACCUMULATION`** |
| `8h` | 23,130,000.00 USD | 4,060,000.00 USD | **`ACCUMULATION`** |
| `12h` | 11,500,000.00 USD | -15,580,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 893,980.00 USD | -22,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,430,000.00 USD | -131,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -228,000,000.00 USD | -664,850,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-136.05K` | 15m=`-315.47K` | 1h=`+9.13M` | 24h=`+893.98K`
* Futures Capital Netflows: 5m=`-830.04K` | 15m=`-1.50M` | 1h=`+11.20M` | 24h=`-22.83M`
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
  * `2026-10-30 13:52:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:16 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2.70` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `7.05`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `5.44` (Risk Distance: `1.24` pts)
  * +2.5R Take Profit: `1.09`
  * Mathematical Lot Sizing: **`8.04 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.36`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
