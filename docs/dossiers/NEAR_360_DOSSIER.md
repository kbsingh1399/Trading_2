# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:36:44 IST` (`2026-10-29 21:06:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.15` | **Live Ask Quote**: `4.18` | **Mid Price**: `4.17`
- **Spread Points**: `29.00` | **Spread BPS**: `69.60 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.45` | VWAP Z-Score: `-2.58` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0628` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `23.03` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.77` | Lower -3.00σ Band: `4.13`
  * Upper +2.51σ Band: `4.72` | Lower -2.51σ Band: `4.18`
  * Upper +2.01σ Band: `4.66` | Lower -2.01σ Band: `4.23`
  * Upper +2.00σ Band: `4.66` | Lower -2.00σ Band: `4.23`
  * Upper +1.28σ Band: `4.59` | Lower -1.28σ Band: `4.31`
  * Upper +1.00σ Band: `4.56` | Lower -1.00σ Band: `4.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.35` | EMA-20=`4.41` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.44` (Slope: `+0.0000`) | EMA-100=`4.48`
  * Institutional Anchors: EMA-144=`4.49` | EMA-200=`4.50` (Slope: `-0.3503`) | EMA-233=`4.51`
- **Range Boundaries**: 24H High=`4.75` | 24H Low=`4.13` | Weekly High=`4.80` | Weekly Low=`4.13`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.57` (Distance: `-8.87%`)
  * Point of Control (POC) = `4.41` (Distance: `-5.55%`)
  * Value Area Low (VAL) = `4.29` (Distance: `-2.89%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.73` | POC=`4.68` | VAL=`4.61`
  * Prior Day Extremes: PDH=`4.80` | PDL=`4.53` | PDC=`4.71`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.63` | Weekly POC=`4.45` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.75` | Low=`4.39`
  * London Session (08:00-16:00 UTC): High=`4.50` | Low=`4.27`
  * New York Session (13:00-21:00 UTC): High=`4.67` | Low=`4.34`
  * Initial Balance (First Hour): IB High=`4.50` | IB Low=`4.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.15` - `4.18`
  * Optimal Trade Entry (OTE 0.705): `4.17`
  * Structural Invalidation Anchor (0.786): `4.20`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.20` | `4.21` | `4.16` | `4.17` | `1,316,370` | 5,510,248.80 USD | 743,594.78 USD | `+13.49%` | -40,492,239.82 USD | `+0.77` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4.17` | `4.19` | `4.12` | `4.13` | `5,321,532` | 22,090,592.99 USD | -2,713,402.01 USD | `-12.28%` | -43,205,641.83 USD | `-1.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4.13` | `4.13` | `4.12` | `4.13` | `174,877` | 721,131.13 USD | 265,924.37 USD | `+36.88%` | -42,939,717.46 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.36` | `4.37` | `4.14` | `4.18` | `9,697,980` | 41,106,447.75 USD | -5,829,110.65 USD | `-14.18%` | -34,348,399.02 USD | `-3.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.18` | `4.26` | `4.10` | `4.17` | `12,607,156` | 52,737,895.99 USD | -6,401,449.26 USD | `-12.14%` | -40,749,848.28 USD | `-2.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.17` | `4.19` | `4.12` | `4.13` | `5,494,022` | 22,801,870.49 USD | -2,452,031.05 USD | `-10.75%` | -43,201,879.33 USD | `-0.81` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.42` | `4.43` | `4.38` | `4.40` | `4,517,639` | 19,883,976.65 USD | 1,294,805.24 USD | `+6.51%` | -28,218,858.01 USD | `+0.73` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.40` | `4.41` | `4.10` | `4.17` | `27,824,304` | 117,811,919.82 USD | -11,296,164.64 USD | `-9.59%` | -39,515,022.65 USD | `-2.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.17` | `4.19` | `4.12` | `4.13` | `5,496,409` | 22,811,724.12 USD | -2,447,477.64 USD | `-10.73%` | -41,962,500.29 USD | `-0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.10` | `4.13` | `33,318,326` | 140,613,790.30 USD | -13,748,195.69 USD | `-9.78%` | -42,075,461.00 USD | `-0.93` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -27,473,639.56 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -28,567,348.59 USD | `+1.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.10` | `4.13` | `33,318,326` | 140,613,790.30 USD | -13,748,195.69 USD | `-9.78%` | -42,075,461.00 USD | `-0.93` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `58` | `0x7737...bf66` | `LONG` | 24,581,887.99 USD | `5,640,376.30` | `2.35` | `4.19` | `0.9075` | 11,309,985.16 USD | `+46.01%` | `10X Cross` |
| `128` | `0xb581...6f4f` | `LONG` | 15,707,160.00 USD | `3,600,000.00` | `5.19` | `4.19` | `0.000000` | -2,985,875.22 USD | `-19.01%` | `4X Cross` |
| `219` | `0xdd53...2b13` | `SHORT` | 10,105,330.88 USD | `2,400,202.10` | `2.31` | `4.19` | `28.89` | -4,559,927.00 USD | `-45.12%` | `3X Cross` |
| `262` | `0x77ee...2902` | `LONG` | 8,978,689.14 USD | `2,063,023.10` | `1.93` | `4.19` | `0.2508` | 4,987,493.20 USD | `+55.55%` | `10X Cross` |
| `284` | `0xefe4...194b` | `SHORT` | 8,470,719.80 USD | `2,019,882.30` | `4.44` | `4.19` | `11.18` | 504,365.35 USD | `+5.95%` | `5X Cross` |
| `383` | `0xb83d...6e36` | `SHORT` | 6,219,655.65 USD | `1,445,759.10` | `5.19` | `4.19` | `98.85` | 1,289,793.29 USD | `+20.74%` | `3X Cross` |
| `408` | `0xb46b...538e` | `SHORT` | 5,599,176.00 USD | `1,336,000.00` | `4.33` | `4.19` | `7.49` | 185,688.06 USD | `+3.32%` | `10X Cross` |
| `426` | `0x9df2...c665` | `SHORT` | 5,304,992.55 USD | `1,265,000.00` | `2.03` | `4.19` | `28.14` | -2,738,310.21 USD | `-51.62%` | `10X Cross` |
| `459` | `0x60b0...991e` | `LONG` | 4,872,191.48 USD | `1,121,307.10` | `5.00` | `4.19` | `0.000000` | -729,232.95 USD | `-14.97%` | `10X Cross` |
| `492` | `0xcac1...26b3` | `SHORT` | 4,505,966.28 USD | `1,073,743.90` | `2.48` | `4.19` | `11.91` | -1,846,022.81 USD | `-40.97%` | `10X Cross` |
| `510` | `0x781e...96b7` | `SHORT` | 4,362,076.94 USD | `1,039,604.60` | `2.45` | `4.19` | `7.61` | -1,817,739.75 USD | `-41.67%` | `10X Cross` |
| `513` | `0xdf60...d3c7` | `LONG` | 4,302,600.00 USD | `1,000,000.00` | `4.70` | `4.19` | `3.91` | -396,677.29 USD | `-9.22%` | `8X Isolated` |
| `576` | `0x4cae...7c34` | `LONG` | 3,917,357.77 USD | `900,086.80` | `3.52` | `4.19` | `2.16` | 744,956.79 USD | `+19.02%` | `10X Cross` |
| `588` | `0xb695...a92d` | `SHORT` | 3,849,464.93 USD | `919,780.40` | `4.57` | `4.19` | `36.83` | 356,910.07 USD | `+9.27%` | `10X Cross` |
| `594` | `0x45d2...4029` | `SHORT` | 3,813,723.50 USD | `909,400.00` | `3.26` | `4.19` | `47.61` | -847,573.60 USD | `-22.22%` | `10X Cross` |
| `718` | `0x9aa5...58af` | `SHORT` | 3,154,295.83 USD | `723,977.10` | `4.78` | `4.19` | `15.12` | 305,337.36 USD | `+9.68%` | `10X Cross` |
| `807` | `0xba5d...a352` | `SHORT` | 2,821,234.35 USD | `647,532.50` | `2.83` | `4.19` | `12.83` | -988,519.41 USD | `-35.04%` | `10X Cross` |
| `819` | `0xd1dd...9e85` | `SHORT` | 2,781,366.56 USD | `637,621.00` | `4.96` | `4.19` | `16.96` | 382,106.17 USD | `+13.74%` | `10X Cross` |
| `834` | `0x005a...61fe` | `LONG` | 2,730,485.58 USD | `652,414.60` | `2.08` | `4.19` | `2.40` | 1,372,954.35 USD | `+50.28%` | `7X Cross` |
| `840` | `0x123d...3bff` | `SHORT` | 2,706,188.32 USD | `636,076.70` | `2.09` | `4.19` | `9.05` | -1,378,811.63 USD | `-50.95%` | `10X Cross` |
| `859` | `0xcf53...ee11` | `SHORT` | 2,613,019.41 USD | `621,598.40` | `5.07` | `4.19` | `24.97` | 539,150.84 USD | `+20.63%` | `10X Cross` |
| `936` | `0x5647...e7de` | `SHORT` | 2,381,115.54 USD | `545,864.50` | `4.69` | `4.19` | `12.82` | 177,475.91 USD | `+7.45%` | `10X Cross` |
| `967` | `0xbfc7...80b4` | `SHORT` | 2,307,141.90 USD | `531,000.00` | `2.01` | `4.19` | `13.16` | -1,241,942.51 USD | `-53.83%` | `10X Cross` |
| `1140` | `0xef96...9383` | `SHORT` | 1,971,350.78 USD | `468,443.50` | `4.50` | `4.19` | `13.13` | 137,950.29 USD | `+7.00%` | `10X Cross` |
| `1304` | `0x7fda...17d1` | `SHORT` | 1,711,523.97 USD | `407,903.90` | `4.83` | `4.19` | `101.62` | 257,015.66 USD | `+15.02%` | `10X Cross` |
| `1318` | `0xe097...d0fe` | `LONG` | 1,678,280.00 USD | `400,000.00` | `5.29` | `4.19` | `0.000000` | -438,507.30 USD | `-26.13%` | `10X Cross` |
| `1338` | `0xfc66...ca06` | `SHORT` | 1,651,238.95 USD | `396,313.20` | `4.59` | `4.19` | `92.12` | 167,811.05 USD | `+10.16%` | `10X Cross` |
| `1468` | `0x6e8f...4364` | `LONG` | 1,516,614.53 USD | `361,210.50` | `3.28` | `4.19` | `3.29` | 332,554.30 USD | `+21.93%` | `10X Cross` |
| `1469` | `0xdf95...7d72` | `SHORT` | 1,516,403.01 USD | `362,325.10` | `4.23` | `4.19` | `111.04` | 17,093.02 USD | `+1.13%` | `10X Cross` |
| `1504` | `0xcf67...eb24` | `LONG` | 1,469,790.00 USD | `350,000.00` | `1.98` | `4.19` | `1.68` | 778,172.12 USD | `+52.94%` | `10X Cross` |
| `1617` | `0xfc27...9d9d` | `SHORT` | 1,339,254.37 USD | `319,997.70` | `5.01` | `4.19` | `57.43` | 264,288.25 USD | `+19.73%` | `10X Cross` |
| `1690` | `0xe065...0f85` | `SHORT` | 1,261,234.68 USD | `290,227.90` | `2.81` | `4.19` | `6.39` | -444,490.43 USD | `-35.24%` | `10X Cross` |
| `1811` | `0x023a...2355` | `SHORT` | 1,138,219.55 USD | `271,963.00` | `4.57` | `4.19` | `33.18` | 103,524.60 USD | `+9.10%` | `10X Cross` |
| `1830` | `0xb69e...033a` | `LONG` | 1,121,414.77 USD | `257,081.40` | `4.61` | `4.19` | `2.84` | -62,640.09 USD | `-5.59%` | `10X Cross` |
| `1877` | `0xff43...d924` | `LONG` | 1,083,839.47 USD | `249,474.50` | `4.64` | `4.19` | `3.28` | -74,204.21 USD | `-6.85%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.68` | 5,496.08 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.50K USD at 4.6819 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 5,335.85 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.34K USD at 4.6818 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `5.20` | 16,539.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 16.54K USD at 5.1980 USD [API] | `2026-10-10 05:20:14` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 46,290.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 46.29K USD at 4.6831 USD [API] | `2026-10-28 04:36:12` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 7,062.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.06K USD at 4.6896 USD [API] | `2026-10-28 04:46:22` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 6,772.75 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.77K USD at 4.6854 USD [API] | `2026-10-28 05:41:34` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 78,582.01 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 78.58K USD at 4.6996 USD [API] | `2026-10-28 05:48:58` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 10,035.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.04K USD at 4.6996 USD [API] | `2026-10-28 05:48:58` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 10,035.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.04K USD at 4.6996 USD [API] | `2026-10-28 05:48:58` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 10,035.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.04K USD at 4.6996 USD [API] | `2026-10-28 07:45:25` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 80,112.67 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 80.11K USD at 4.6996 USD [API] | `2026-10-28 07:45:25` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 10,035.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.04K USD at 4.6996 USD [API] | `2026-10-28 07:45:25` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 6,499.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.50K USD at 4.6994 USD [API] | `2026-10-28 07:45:25` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 11,349.13 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 11.35K USD at 4.7006 USD [API] | `2026-10-28 07:46:54` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 3,648.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.65K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 149.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.15K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 248.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.25K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 12.90 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 263.16 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.26K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 41,159.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 41.16K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 436.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.44K USD at 4.3000 USD [API] | `2026-10-24 14:16:49` |
| `ANNOUNCEMENT` | `INFO` | `4.75` | 5,298.99 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.30K USD at 4.7465 USD [API] | `2026-10-28 08:06:38` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 10,239.88 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.24K USD at 4.7953 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 8,849.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.85K USD at 4.7707 USD [API] | `2026-10-28 08:28:06` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,210.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.21K USD at 4.7817 USD [API] | `2026-10-28 08:29:22` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 6,599.33 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.60K USD at 4.7752 USD [API] | `2026-10-28 08:32:34` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,197.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.20K USD at 4.7755 USD [API] | `2026-10-28 08:32:34` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,197.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.20K USD at 4.7755 USD [API] | `2026-10-28 08:32:34` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 8,216.76 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.22K USD at 4.7758 USD [API] | `2026-10-28 08:32:34` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 5,444.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.44K USD at 4.7759 USD [API] | `2026-10-28 08:32:34` |
| `ANNOUNCEMENT` | `INFO` | `4.76` | 7,748.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.75K USD at 4.7590 USD [API] | `2026-10-28 08:38:09` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 9,006.76 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.01K USD at 4.7404 USD [API] | `2026-10-28 08:58:47` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 6,080.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.08K USD at 4.7301 USD [API] | `2026-10-28 09:39:48` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 7,763.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.76K USD at 4.7077 USD [API] | `2026-10-28 10:21:41` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 2.04 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.00K USD at 5.0906 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 71.78 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.07K USD at 5.0907 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 34.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.03K USD at 5.0908 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 166.47 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.17K USD at 5.0909 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 77.38 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.08K USD at 5.0909 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 1,662.21 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.66K USD at 5.0910 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 999.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.00K USD at 5.0910 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 58.04 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.06K USD at 5.0910 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 3,938.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.94K USD at 5.0910 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 46.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 5.0911 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 56.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.06K USD at 5.0912 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 16.80 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 5.0912 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 13.24 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 5.0912 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 15.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 5.0913 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `5.09` | 78.41 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.08K USD at 5.0914 USD [API] | `2026-10-22 04:33:48` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 7,741.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.74K USD at 4.7011 USD [API] | `2026-10-28 10:56:53` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 10,021.01 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.02K USD at 4.6928 USD [API] | `2026-10-28 11:02:15` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 5,574.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.57K USD at 4.6583 USD [API] | `2026-10-28 11:11:49` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 5,610.46 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.61K USD at 4.6676 USD [API] | `2026-10-28 11:30:45` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 9,012.59 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.01K USD at 4.6678 USD [API] | `2026-10-28 11:30:45` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.54` (Vol: 539,200.00 USD, Dist: `+4.25%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--1.95%`)
  * 48H Horizon: Short MP=`4.53` (Vol: 539,200.00 USD, Dist: `+4.23%`) | Long MP=`4.24` (Vol: 596,900.00 USD, Dist: `--2.58%`)
  * 3D Horizon: Short MP=`4.83` (Vol: 541,200.00 USD, Dist: `+11.05%`) | Long MP=`4.24` (Vol: 689,000.00 USD, Dist: `--2.58%`)
  * 7D Horizon: Short MP=`4.41` (Vol: 793,100.00 USD, Dist: `+1.37%`) | Long MP=`4.23` (Vol: 1,400,000.00 USD, Dist: `--2.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8450` | 2,030.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 3,350.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 43,750.00 USD | 33,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 512.24 USD | 33,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,380.00 USD | 33,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 19,280.00 USD | 33,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 5,280,000.00 USD | 33,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 286.50 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 6,610.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 30,370.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 1,000.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 126.06 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 11,320.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 27,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 8,040.00 USD | 27,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 383,760.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 53,650.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 73,400.00 USD | 27,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 27,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 41,270.00 USD | 27,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 57,020.00 USD | 27,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 13,350.00 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 2,670.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 35,290.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 21,600.00 USD | 27,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 2,300.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 558.38 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 11,870.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 13,810.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 2,830.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 2,760.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 11,330.00 USD | 27,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 236.85 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 1,330.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 27,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 23,470.00 USD | 27,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 669.86 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 18,780.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 226.29 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 1,320.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,200.00 USD | 27,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 674.18 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 31,130.00 USD | 27,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 1,170.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 16,150.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 4,620.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 5,680.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 308.32 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 2,440.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,510.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 10,850.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 27,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 4,740.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,190.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 17,420.00 USD | 27,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 569.64 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 6,790.00 USD | 27,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 1,370.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 5,750.00 USD | 27,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 11,460.00 USD | 27,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 211.80 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 265,490.00 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 15,250.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 2,440.00 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 2,870.00 USD | 26,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 26,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,080.00 USD | 26,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 13,270.00 USD | 26,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 12,910.00 USD | 26,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 1,310.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,250.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 24,990.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 1,720,000.00 USD | 26,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 2,010.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 263.92 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 6,770.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 3,010.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 3,960.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 41,570.00 USD | 24,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 643.54 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 199,500.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 214,480.00 USD | 24,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 81,810.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 6,020.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 86,680.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 6,810.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 12,830.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,950.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,510.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 10,310.00 USD | 24,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 3,210.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 5,590.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 6,120.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 248.38 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 45,940.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,880.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 24,600.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 239.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 6,340.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 26,180.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 4,680.00 USD | 24,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 120,330.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 3,440.00 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 804.32 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 4,150.00 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,810.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 9,840.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 1,520,000.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 3,120.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 48,780.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,800.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 63,060.00 USD | 22,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 420,020.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 534.24 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 63,350.00 USD | 21,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 2,310.00 USD | 21,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,860.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 60,620.00 USD | 21,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 391,530.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 158,860.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 636,570.00 USD | 21,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 15,480.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 259,390.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 20,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,690.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,490.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 37,790.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 10,330.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 1,160.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 9,730.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 8,920.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 368.88 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 71,500.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 560.34 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 14,260.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 224.44 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 65,400.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 10,090.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 103,320.00 USD | 19,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,300.00 USD | 19,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,930.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 20,370.00 USD | 19,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 130,140.00 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 17,980.00 USD | 19,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 249,070.00 USD | 19,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 8,440.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 19,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 154.83 USD | 19,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 3,740.00 USD | 19,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 2,140.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,840.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,470.00 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 6,190.00 USD | 19,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 572.29 USD | 19,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 199,090.00 USD | 19,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,140.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 28,270.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,860.00 USD | 18,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 5,190.00 USD | 18,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 4,150.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,800.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,910.00 USD | 18,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 22,330.00 USD | 18,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 3,480.00 USD | 18,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 37,660.00 USD | 18,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 942.11 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 6,210.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 15,260.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 9,740.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 12,330.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 22,800.00 USD | 18,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 355,760.00 USD | 18,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 103,780.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 25,110.00 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 701,010.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 9,970.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 12,360.00 USD | 17,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,510.00 USD | 17,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 92,110.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 107,620.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 9,270.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 39,110.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 19,990.00 USD | 17,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,110.00 USD | 17,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 8,100.00 USD | 17,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 122,100.00 USD | 17,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 8,320.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 354.65 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 218,340.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 29,190.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 18,920.00 USD | 16,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 35,590.00 USD | 16,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 35,080.00 USD | 16,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 64,310.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 47,960.00 USD | 16,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 836,280.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 8,590.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,400,000.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 69,500.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 15,580.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 29,530.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 51,870.00 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 31,120.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 2,090.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 14,490.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 53,610.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 12,370.00 USD | 14,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 158,490.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 187,750.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 50,040.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 25,570.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 5,860.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 10,250.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 55,000.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 70,570.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 26,990.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 25,280.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 12,480.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 17,140.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 21,970.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 7,690.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 325,560.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 379,650.00 USD | 13,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 8,330.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 135,550.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 22,500.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 79,940.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 165,030.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 845.19 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 11,540.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 29,880.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 10,840,000.00 USD | 10,840,000.00 USD | 57,840.00 USD | 22,500.00 USD | 121,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 513,760.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 10,640,000.00 USD | 10,640,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 49,270.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 10,550,000.00 USD | 10,550,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 574,480.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,300,000.00 USD | 5,300,000.00 USD | 16,740.00 USD | 3,070.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 10,380,000.00 USD | 10,380,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 189,590.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 178,360.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 9.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,260,000.00 USD | 10,260,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 1,930.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,270,000.00 USD | 5,270,000.00 USD | 17,670.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,170,000.00 USD | 10,170,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 43,110.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,230,000.00 USD | 5,230,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,030,000.00 USD | 10,030,000.00 USD | 50,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 157,110.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,230,000.00 USD | 5,230,000.00 USD | 186.40 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 9,980,000.00 USD | 9,980,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 27,950.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,230,000.00 USD | 5,230,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 9,980,000.00 USD | 9,980,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 30,770.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 15,960.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 9,880,000.00 USD | 9,880,000.00 USD | 20,660.00 USD | 12,370.00 USD | 64,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 33,470.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 9,780,000.00 USD | 9,780,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 99,550.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 9,710,000.00 USD | 9,710,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 56,700.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,150,000.00 USD | 5,150,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 9,640,000.00 USD | 9,640,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 14,890.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,150,000.00 USD | 5,150,000.00 USD | 7,570.00 USD | 9,280.00 USD | 29,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,600,000.00 USD | 9,600,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 38,620.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,100,000.00 USD | 5,100,000.00 USD | 225.52 USD | 3,860.00 USD | 9,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,520,000.00 USD | 9,520,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 146,150.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,090,000.00 USD | 5,090,000.00 USD | 3,170.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,430,000.00 USD | 9,430,000.00 USD | 582.53 USD | 0.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 14,720.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,080,000.00 USD | 5,080,000.00 USD | 53,440.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 77,060.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,410,000.00 USD | 9,410,000.00 USD | 527.85 USD | 0.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 6,620.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,020,000.00 USD | 5,020,000.00 USD | 352.15 USD | 0.00 USD | 16,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 147,910.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 24,250.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,000,000.00 USD | 5,000,000.00 USD | 138.23 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 154,310.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 4,990,000.00 USD | 4,990,000.00 USD | 1,450.00 USD | 12,320.00 USD | 53,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,390,000.00 USD | 9,390,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 24,820.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,310,000.00 USD | 9,310,000.00 USD | 54,800.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 4,710.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 4,910,000.00 USD | 4,910,000.00 USD | 105,540.00 USD | 6,860.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,230,000.00 USD | 9,230,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 52,710.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 4,760,000.00 USD | 4,760,000.00 USD | 112,190.00 USD | 37,150.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,010,000.00 USD | 9,010,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 96,500.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,590,000.00 USD | 4,590,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 8,960,000.00 USD | 8,960,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,040.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 35,760.00 USD | 38,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 8,710,000.00 USD | 8,710,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,480,000.00 USD | 4,480,000.00 USD | 145,280.00 USD | 26,030.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,630,000.00 USD | 8,630,000.00 USD | 90,780.00 USD | 41,330.00 USD | 81,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 331,990.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 21,500.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,420,000.00 USD | 8,420,000.00 USD | 51,660.00 USD | 20,780.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 21,330.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 4,240,000.00 USD | 4,240,000.00 USD | 576.76 USD | 6,420.00 USD | 16,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,300,000.00 USD | 8,300,000.00 USD | 75,150.00 USD | 31,050.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 533,900.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 4,220,000.00 USD | 4,220,000.00 USD | 12,850.00 USD | 5,610.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,060,000.00 USD | 8,060,000.00 USD | 8,490.00 USD | 19,870.00 USD | 696.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 13,470.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,200,000.00 USD | 4,200,000.00 USD | 35,990.00 USD | 29,270.00 USD | 35,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,030,000.00 USD | 8,030,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 108,840.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,100,000.00 USD | 4,100,000.00 USD | 156,730.00 USD | 52,430.00 USD | 65,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,840,000.00 USD | 7,840,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 67,350.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,820,000.00 USD | 3,820,000.00 USD | 46,870.00 USD | 30,290.00 USD | 14,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,230,000.00 USD | 7,230,000.00 USD | 30,630.00 USD | 77,970.00 USD | 85,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 61,830.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 3,730,000.00 USD | 3,730,000.00 USD | 94,130.00 USD | 45,940.00 USD | 49,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 7,040,000.00 USD | 7,040,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 33,890.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 3,540,000.00 USD | 3,540,000.00 USD | 35,730.00 USD | 21,130.00 USD | 95,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,790,000.00 USD | 6,790,000.00 USD | 317,210.00 USD | 98,320.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 57,440.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 3,390,000.00 USD | 3,390,000.00 USD | 109,930.00 USD | 56,050.00 USD | 73,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 6,210,000.00 USD | 6,210,000.00 USD | 386,400.00 USD | 94,720.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 11,310.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 3,150,000.00 USD | 3,150,000.00 USD | 60,540.00 USD | 33,270.00 USD | 105,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 5,300,000.00 USD | 5,300,000.00 USD | 279,800.00 USD | 88,330.00 USD | 248,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 84,020.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 2,950,000.00 USD | 2,950,000.00 USD | 23,550.00 USD | 55,650.00 USD | 82,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,680,000.00 USD | 4,680,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 12,740.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 2,790,000.00 USD | 2,790,000.00 USD | 29,430.00 USD | 32,610.00 USD | 127,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 4,240,000.00 USD | 4,240,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 33,550.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 2,600,000.00 USD | 2,600,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 3,950,000.00 USD | 3,950,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 82,940.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 2,500,000.00 USD | 2,500,000.00 USD | 190,260.00 USD | 0.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 3,610,000.00 USD | 3,610,000.00 USD | 198,550.00 USD | 45,470.00 USD | 124,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 349,630.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 2,260,000.00 USD | 2,260,000.00 USD | 3,630.00 USD | 15,020.00 USD | 22,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 3,240,000.00 USD | 3,240,000.00 USD | 183,890.00 USD | 35,750.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 302,020.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 2,220,000.00 USD | 2,220,000.00 USD | 4,280.00 USD | 85,320.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 2,980,000.00 USD | 2,980,000.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 60,670.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 2,110,000.00 USD | 2,110,000.00 USD | 10,540.00 USD | 34,570.00 USD | 194,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 2,620,000.00 USD | 2,620,000.00 USD | 134,630.00 USD | 26,560.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 723,030.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 1,870,000.00 USD | 1,870,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 2,420,000.00 USD | 2,420,000.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 124,860.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 1,770,000.00 USD | 1,770,000.00 USD | 22,930.00 USD | 59,250.00 USD | 73,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 1,800,000.00 USD | 1,800,000.00 USD | 110,780.00 USD | 0.00 USD | 190,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 253,880.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 1,610,000.00 USD | 1,610,000.00 USD | 4,430.00 USD | 80,980.00 USD | 228,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 1,500,000.00 USD | 1,500,000.00 USD | 97,300.00 USD | 0.00 USD | 341,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 44,090.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 1,300,000.00 USD | 1,300,000.00 USD | 39,650.00 USD | 55,060.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 1,060,000.00 USD | 1,060,000.00 USD | 363,830.00 USD | 0.00 USD | 106,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 101,080.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 1,170,000.00 USD | 1,170,000.00 USD | 272,540.00 USD | 53,970.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 592,140.00 USD | 592,140.00 USD | 374,290.00 USD | 0.00 USD | 217,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 236,880.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 672,440.00 USD | 672,440.00 USD | 564,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 514,600.00 USD | 514,600.00 USD | 254,890.00 USD | 0.00 USD | 259,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 1,030,000.00 USD | 1,030,000.00 USD | 254,890.00 USD | 0.00 USD | 259,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 122,430.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 107,680.00 USD | 107,680.00 USD | 63,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.16` | 1,710,000.00 USD | 1,710,000.00 USD | 509,640.00 USD | 0.00 USD | 171,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 466,520.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 44,430.00 USD | 44,430.00 USD | 44,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.17` | 1,910,000.00 USD | 1,910,000.00 USD | 202,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 45,840.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.18` | 197,650.00 USD | 197,650.00 USD | 197,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.18` | 395,310.00 USD | 395,310.00 USD | 197,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.18` | 2,270,000.00 USD | 2,270,000.00 USD | 360,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 30,300.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 683,590.00 USD | 683,590.00 USD | 288,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.19` | 2,490,000.00 USD | 2,490,000.00 USD | 215,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 101,900.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.20` | 738,980.00 USD | 738,980.00 USD | 55,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.20` | 2,950,000.00 USD | 2,950,000.00 USD | 337,660.00 USD | 122,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 134,680.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.21` | 802,520.00 USD | 802,520.00 USD | 63,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.21` | 3,560,000.00 USD | 3,560,000.00 USD | 462,060.00 USD | 149,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 19,220.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.22` | 977,550.00 USD | 977,550.00 USD | 0.00 USD | 175,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.22` | 5,360,000.00 USD | 5,360,000.00 USD | 853,600.00 USD | 161,970.00 USD | 783,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 49,240.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.23` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 440,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.23` | 7,900,000.00 USD | 7,900,000.00 USD | 1,170,000.00 USD | 633,870.00 USD | 736,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 601,150.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.24` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 268,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.24` | 10,130,000.00 USD | 10,130,000.00 USD | 1,060,000.00 USD | 611,180.00 USD | 563,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 12,700.00 USD | 472,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.25` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 323,700.00 USD | 150,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 11,720,000.00 USD | 11,720,000.00 USD | 506,030.00 USD | 433,770.00 USD | 647,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 288,490.00 USD | 459,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.26` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 171,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 14,120,000.00 USD | 14,120,000.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 41,020.00 USD | 171,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 3,010,000.00 USD | 3,010,000.00 USD | 594,570.00 USD | 24,620.00 USD | 59,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 16,640,000.00 USD | 16,640,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.28` | 6,760.00 USD | 130,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.28` | 3,660,000.00 USD | 3,660,000.00 USD | 313,130.00 USD | 30,410.00 USD | 308,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 18,240,000.00 USD | 18,240,000.00 USD | 0.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 14,670.00 USD | 123,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.29` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 858.14 USD | 109,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 3,670,000.00 USD | 3,670,000.00 USD | 3,320.00 USD | 0.00 USD | 53.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 90,090.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.31` | 4,000,000.00 USD | 4,000,000.00 USD | 270,390.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 0.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.32` | 122.98 USD | 108,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 4,000,000.00 USD | 4,000,000.00 USD | 611.20 USD | 0.00 USD | 19.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 78,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 5,860.00 USD | 108,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 4,030,000.00 USD | 4,030,000.00 USD | 1,990.00 USD | 33,630.00 USD | 301.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 13,310.00 USD | 102,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.34` | 4,390,000.00 USD | 4,390,000.00 USD | 269,670.00 USD | 13,800.00 USD | 75,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 18,830,000.00 USD | 18,830,000.00 USD | 4,550.00 USD | 0.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.34` | 30,420.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.36` | 1,090.00 USD | 58,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 4,600,000.00 USD | 4,600,000.00 USD | 82,150.00 USD | 12,310.00 USD | 29,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 19,060,000.00 USD | 19,060,000.00 USD | 5,210.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.37` | 56,750.00 USD | 57,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 4,830,000.00 USD | 4,830,000.00 USD | 52,120.00 USD | 46,860.00 USD | 131,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 600.25 USD | 600.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 5,500,000.00 USD | 5,500,000.00 USD | 171,480.00 USD | 18,150.00 USD | 476,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 229,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 19,820,000.00 USD | 19,820,000.00 USD | 141,060.00 USD | 62,850.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 3,660.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 6,130,000.00 USD | 6,130,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 6,470,000.00 USD | 6,470,000.00 USD | 193,630.00 USD | 83,080.00 USD | 63,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 272,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 537.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 21,150,000.00 USD | 21,150,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.43` | 6,610,000.00 USD | 6,610,000.00 USD | 769.40 USD | 49,400.00 USD | 94,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 21,420,000.00 USD | 21,420,000.00 USD | 155,560.00 USD | 46,230.00 USD | 69,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 7,400,000.00 USD | 7,400,000.00 USD | 154,480.00 USD | 339,100.00 USD | 289,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 50,720.00 USD | 359.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 7,460,000.00 USD | 7,460,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.47` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 16,700.00 USD | 18,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 22,010,000.00 USD | 22,010,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.48` | 7,710,000.00 USD | 7,710,000.00 USD | 115,670.00 USD | 73,240.00 USD | 25,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 22,010,000.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 8,270,000.00 USD | 8,270,000.00 USD | 252,980.00 USD | 155,000.00 USD | 150,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 22,350,000.00 USD | 22,350,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 8,810,000.00 USD | 8,810,000.00 USD | 359,570.00 USD | 65,710.00 USD | 117,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 22,920,000.00 USD | 22,920,000.00 USD | 368,940.00 USD | 200,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.51` | 9,590,000.00 USD | 9,590,000.00 USD | 162,900.00 USD | 307,580.00 USD | 309,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 23,000,000.00 USD | 23,000,000.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 10,150,000.00 USD | 10,150,000.00 USD | 266,310.00 USD | 88,150.00 USD | 205,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 23,140,000.00 USD | 23,140,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.53` | 10,920,000.00 USD | 10,920,000.00 USD | 487,540.00 USD | 0.00 USD | 278,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 24,040,000.00 USD | 24,040,000.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 150,600.00 USD | 598,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 25,280,000.00 USD | 25,280,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.55` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 22,540.00 USD | 239,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 12,330,000.00 USD | 12,330,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 25,770,000.00 USD | 25,770,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 12,620,000.00 USD | 12,620,000.00 USD | 155,250.00 USD | 70,180.00 USD | 67,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 26,120,000.00 USD | 26,120,000.00 USD | 198,050.00 USD | 0.00 USD | 151,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 13,950,000.00 USD | 13,950,000.00 USD | 434,730.00 USD | 56,540.00 USD | 841,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 26,250,000.00 USD | 26,250,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 14,940,000.00 USD | 14,940,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 27,840,000.00 USD | 27,840,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 444.34 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 15,140,000.00 USD | 15,140,000.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 27,960,000.00 USD | 27,960,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 484.91 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 15,280,000.00 USD | 15,280,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 27,970,000.00 USD | 27,970,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 34,060.00 USD | 38,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 15,420,000.00 USD | 15,420,000.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 28,100,000.00 USD | 28,100,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 15,420,000.00 USD | 15,420,000.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 28,320,000.00 USD | 28,320,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 2,400.00 USD | 41,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 15,830,000.00 USD | 15,830,000.00 USD | 333,310.00 USD | 11,270.00 USD | 61,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 28,820,000.00 USD | 28,820,000.00 USD | 500,990.00 USD | 0.00 USD | 857.07 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 7,990.00 USD | 49,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 16,900,000.00 USD | 16,900,000.00 USD | 423,550.00 USD | 52,020.00 USD | 598,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 29,240,000.00 USD | 29,240,000.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 38,330.00 USD | 87,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 17,870,000.00 USD | 17,870,000.00 USD | 281,290.00 USD | 304,540.00 USD | 379,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 29,540,000.00 USD | 29,540,000.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,700.00 USD | 212,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 18,430,000.00 USD | 18,430,000.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 154.74 USD | 212,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 19,020,000.00 USD | 19,020,000.00 USD | 345,840.00 USD | 62,440.00 USD | 175,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 30,500,000.00 USD | 30,500,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 14,780.00 USD | 227,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 19,520,000.00 USD | 19,520,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 30,590,000.00 USD | 30,590,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 1,050.00 USD | 228,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 19,870,000.00 USD | 19,870,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 30,900,000.00 USD | 30,900,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 11,230.00 USD | 239,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 20,830,000.00 USD | 20,830,000.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 31,310,000.00 USD | 31,310,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 29,520.00 USD | 268,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 21,130,000.00 USD | 21,130,000.00 USD | 5,440.00 USD | 187,480.00 USD | 103,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 31,500,000.00 USD | 31,500,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 3,920.00 USD | 272,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 21,290,000.00 USD | 21,290,000.00 USD | 61,330.00 USD | 37,010.00 USD | 61,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 31,560,000.00 USD | 31,560,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 4,700.00 USD | 277,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 22,040,000.00 USD | 22,040,000.00 USD | 273,860.00 USD | 172,000.00 USD | 304,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 31,880,000.00 USD | 31,880,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 12,960.00 USD | 290,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 22,750,000.00 USD | 22,750,000.00 USD | 240,860.00 USD | 202,760.00 USD | 270,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 32,420,000.00 USD | 32,420,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 1,720.00 USD | 292,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 23,110,000.00 USD | 23,110,000.00 USD | 35,470.00 USD | 78,750.00 USD | 247,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 33,770,000.00 USD | 33,770,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.77` | 23,490,000.00 USD | 23,490,000.00 USD | 113,030.00 USD | 151,370.00 USD | 115,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 34,680,000.00 USD | 34,680,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 299,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 23,670,000.00 USD | 23,670,000.00 USD | 40,580.00 USD | 20,000.00 USD | 114,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 36,030,000.00 USD | 36,030,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 20,410.00 USD | 319,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 24,020,000.00 USD | 24,020,000.00 USD | 112,300.00 USD | 92,850.00 USD | 142,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 37,060,000.00 USD | 37,060,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 553,480.00 USD | 873,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 24,640,000.00 USD | 24,640,000.00 USD | 244,480.00 USD | 200,920.00 USD | 174,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 38,650,000.00 USD | 38,650,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 24,940,000.00 USD | 24,940,000.00 USD | 55,660.00 USD | 120,180.00 USD | 127,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 39,280,000.00 USD | 39,280,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 50,910.00 USD | 923,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 25,500,000.00 USD | 25,500,000.00 USD | 140,640.00 USD | 218,170.00 USD | 201,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 42,050,000.00 USD | 42,050,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 925,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 25,770,000.00 USD | 25,770,000.00 USD | 61,110.00 USD | 70,050.00 USD | 140,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 43,700,000.00 USD | 43,700,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 21,070.00 USD | 946,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 26,020,000.00 USD | 26,020,000.00 USD | 85,920.00 USD | 89,230.00 USD | 77,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 44,190,000.00 USD | 44,190,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.85` | 26,600,000.00 USD | 26,600,000.00 USD | 243,020.00 USD | 110,540.00 USD | 223,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 46,210,000.00 USD | 46,210,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.86` | 22,180.00 USD | 968,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.86` | 26,950,000.00 USD | 26,950,000.00 USD | 94,860.00 USD | 69,470.00 USD | 178,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 47,620,000.00 USD | 47,620,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 974,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 27,170,000.00 USD | 27,170,000.00 USD | 111,250.00 USD | 52,140.00 USD | 59,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 48,680,000.00 USD | 48,680,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 18,250.00 USD | 992,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 27,250,000.00 USD | 27,250,000.00 USD | 36,680.00 USD | 7,330.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 50,270,000.00 USD | 50,270,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 993,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 27,340,000.00 USD | 27,340,000.00 USD | 10,630.00 USD | 25,940.00 USD | 50,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 50,850,000.00 USD | 50,850,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.90` | 27,480,000.00 USD | 27,480,000.00 USD | 24,860.00 USD | 55,440.00 USD | 64,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 51,990,000.00 USD | 51,990,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.91` | 1,630.00 USD | 995,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.91` | 27,760,000.00 USD | 27,760,000.00 USD | 114,310.00 USD | 85,510.00 USD | 74,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 53,430,000.00 USD | 53,430,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 55,160,000.00 USD | 55,160,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 12,930.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 56,720,000.00 USD | 56,720,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 58,020,000.00 USD | 58,020,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 59,320,000.00 USD | 59,320,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 1,350,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 60,550,000.00 USD | 60,550,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 60,940,000.00 USD | 60,940,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 61,490,000.00 USD | 61,490,000.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,710.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 61,850,000.00 USD | 61,850,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 62,550,000.00 USD | 62,550,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 260.76 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.01` | 64,700,000.00 USD | 64,700,000.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.01` | 371,590.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.02` | 66,190,000.00 USD | 66,190,000.00 USD | 821,860.00 USD | 337,720.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 67,630,000.00 USD | 67,630,000.00 USD | 385,330.00 USD | 172,880.00 USD | 886,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 13,130.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.04` | 68,750,000.00 USD | 68,750,000.00 USD | 305,260.00 USD | 191,790.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.05` | 70,300,000.00 USD | 70,300,000.00 USD | 799,820.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 55,570.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 71,010,000.00 USD | 71,010,000.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 72,210,000.00 USD | 72,210,000.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 56,820.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.08` | 72,730,000.00 USD | 72,730,000.00 USD | 204,140.00 USD | 167,810.00 USD | 149,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,190.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 73,270,000.00 USD | 73,270,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 73,650,000.00 USD | 73,650,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 74,410,000.00 USD | 74,410,000.00 USD | 369,260.00 USD | 92,720.00 USD | 291,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 74,990,000.00 USD | 74,990,000.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,680.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 75,720,000.00 USD | 75,720,000.00 USD | 173,190.00 USD | 71,310.00 USD | 484,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 2,110.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 76,180,000.00 USD | 76,180,000.00 USD | 140,950.00 USD | 73,940.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 76,790,000.00 USD | 76,790,000.00 USD | 258,430.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 77,310,000.00 USD | 77,310,000.00 USD | 51,850.00 USD | 126,880.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 317.65 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 78,000,000.00 USD | 78,000,000.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 346.72 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 78,260,000.00 USD | 78,260,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 78,480,000.00 USD | 78,480,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 7,610.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 78,730,000.00 USD | 78,730,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.21` | 78,970,000.00 USD | 78,970,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 79,040,000.00 USD | 79,040,000.00 USD | 55,630.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,250.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 79,090,000.00 USD | 79,090,000.00 USD | 0.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.24` | 29,050.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 59,130.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 878.04 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 37,730.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,840.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 79,090.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 41,910.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 310.68 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 2,320.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 2,300.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 2,270.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 255,740.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 39,430.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 54,260.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 301.98 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 1,730.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 32,270.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 6,050.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.72` | 738.52 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 9,160.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 197.27 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 82,870.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 6,670.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 604.10 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 855.09 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 89,540.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.99` | 131.67 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 1,860.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,080.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 129,280.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 12,520.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.16` | 1,160,000.00 USD | 6,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 330,920.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 1,370.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,610.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 1,820,000.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.30` | 829.74 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 4,110.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 91,940.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 109.43 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.49` | 77,820.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.50` | 325.25 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 536.84 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 697.04 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 29,440.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 392,810.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 12,080.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 15,540.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 40,180.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 474.36 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,410.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 60,560.00 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.91` | 189.89 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 37,400.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.07` | 257.87 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.22` | 9,650,000.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 772.94 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.36` | 6,740.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 154.35 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 3,220.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 121,410.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 107,200.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,790,000.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 29,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 319,720.00 USD | 29,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 29,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.70` | 31,690.00 USD | 29,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 15,410.00 USD | 29,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 2,680.00 USD | 29,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 25,930.00 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,580.00 USD | 29,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.82` | 819.01 USD | 29,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 4,280.00 USD | 29,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 27,570.00 USD | 29,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 29,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 29,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.10` | 359.42 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.12` | 937,370.00 USD | 31,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.13` | 409,570.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.14` | 733,050.00 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 32,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 17,700.00 USD | 32,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.45` | 3,830.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 35,260.00 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 594.65 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.52` | 172,480.00 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 33,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 26,620.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 2,760.00 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 774.32 USD | 33,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.64` | 24,890.00 USD | 33,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,480.00 USD | 33,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.71` | 449,960.00 USD | 34,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.78` | 3,420,000.00 USD | 37,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8450` | 27,170,000.00 USD | 0.00 USD | 2,030.00 USD | `-79.74%` | `2,406.30` |
| `Live` | `Long` | `0.8650` | 27,160,000.00 USD | 0.00 USD | 433.80 USD | `-79.26%` | `501.50` |
| `Live` | `Long` | `0.8750` | 27,160,000.00 USD | 0.00 USD | 2,120.00 USD | `-79.02%` | `2,427.10` |
| `Live` | `Long` | `0.8850` | 27,160,000.00 USD | 0.00 USD | 4,090.00 USD | `-78.78%` | `4,625.30` |
| `Live` | `Long` | `0.8950` | 27,160,000.00 USD | 0.00 USD | 38,570.00 USD | `-78.54%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 27,120,000.00 USD | 0.00 USD | 292.22 USD | `-78.30%` | `322.90` |
| `Live` | `Long` | `0.9150` | 27,120,000.00 USD | 0.00 USD | 12,770.00 USD | `-78.06%` | `13,956.60` |
| `Live` | `Long` | `0.9550` | 27,100,000.00 USD | 0.00 USD | 3,540.00 USD | `-77.10%` | `3,711.10` |
| `Live` | `Long` | `0.9950` | 27,100,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.15%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 26,950,000.00 USD | 0.00 USD | 31,200.00 USD | `-75.91%` | `31,041.00` |
| `Live` | `Long` | `1.01` | 26,920,000.00 USD | 0.00 USD | 3,110.00 USD | `-75.67%` | `3,067.80` |
| `Live` | `Long` | `1.02` | 26,910,000.00 USD | 0.00 USD | 10,880.00 USD | `-75.43%` | `10,616.70` |
| `Live` | `Long` | `1.03` | 26,900,000.00 USD | 0.00 USD | 6,060.00 USD | `-75.19%` | `5,852.20` |
| `Live` | `Long` | `1.05` | 26,900,000.00 USD | 0.00 USD | 8,780.00 USD | `-74.71%` | `8,326.20` |
| `Live` | `Long` | `1.06` | 26,890,000.00 USD | 0.00 USD | 1,010.00 USD | `-74.47%` | `949.50` |
| `Live` | `Long` | `1.07` | 26,890,000.00 USD | 0.00 USD | 7,510.00 USD | `-74.23%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 26,880,000.00 USD | 0.00 USD | 762.97 USD | `-73.99%` | `703.20` |
| `Live` | `Long` | `1.10` | 26,880,000.00 USD | 0.00 USD | 1,030.00 USD | `-73.51%` | `932.00` |
| `Live` | `Long` | `1.11` | 26,880,000.00 USD | 0.00 USD | 929.58 USD | `-73.27%` | `833.70` |
| `Live` | `Long` | `1.12` | 26,880,000.00 USD | 0.00 USD | 9,180.00 USD | `-73.03%` | `8,158.40` |
| `Live` | `Long` | `1.14` | 26,870,000.00 USD | 0.00 USD | 5,990.00 USD | `-72.79%` | `5,281.00` |
| `Live` | `Long` | `1.15` | 26,860,000.00 USD | 0.00 USD | 52,270.00 USD | `-72.55%` | `45,654.80` |
| `Live` | `Long` | `1.18` | 26,810,000.00 USD | 0.00 USD | 1,610.00 USD | `-71.83%` | `1,368.90` |
| `Live` | `Long` | `1.20` | 26,810,000.00 USD | 0.00 USD | 55,670.00 USD | `-71.35%` | `46,584.90` |
| `Live` | `Long` | `1.22` | 26,750,000.00 USD | 0.00 USD | 150.90 USD | `-70.87%` | `124.20` |
| `Live` | `Long` | `1.24` | 26,750,000.00 USD | 0.00 USD | 5,930.00 USD | `-70.39%` | `4,800.50` |
| `Live` | `Long` | `1.25` | 26,750,000.00 USD | 0.00 USD | 18,680.00 USD | `-70.15%` | `15,000.00` |
| `Live` | `Long` | `1.25` | 26,730,000.00 USD | 0.00 USD | 139,310.00 USD | `-69.91%` | `111,002.80` |
| `Live` | `Long` | `1.26` | 26,590,000.00 USD | 0.00 USD | 3,830.00 USD | `-69.67%` | `3,030.60` |
| `Live` | `Long` | `1.27` | 26,580,000.00 USD | 0.00 USD | 4,440.00 USD | `-69.43%` | `3,479.60` |
| `Live` | `Long` | `1.28` | 26,580,000.00 USD | 0.00 USD | 1,880.00 USD | `-69.19%` | `1,463.40` |
| `Live` | `Long` | `1.30` | 26,580,000.00 USD | 0.00 USD | 116.80 USD | `-68.71%` | `89.50` |
| `Live` | `Long` | `1.32` | 26,580,000.00 USD | 0.00 USD | 2,830.00 USD | `-68.23%` | `2,132.40` |
| `Live` | `Long` | `1.33` | 26,570,000.00 USD | 0.00 USD | 2,470.00 USD | `-67.99%` | `1,849.90` |
| `Live` | `Long` | `1.34` | 26,570,000.00 USD | 0.00 USD | 603.91 USD | `-67.76%` | `449.00` |
| `Live` | `Long` | `1.35` | 26,570,000.00 USD | 0.00 USD | 236.85 USD | `-67.52%` | `174.80` |
| `Live` | `Long` | `1.36` | 26,570,000.00 USD | 0.00 USD | 795.11 USD | `-67.28%` | `582.50` |
| `Live` | `Long` | `1.38` | 26,570,000.00 USD | 0.00 USD | 20,050.00 USD | `-67.04%` | `14,581.00` |
| `Live` | `Long` | `1.39` | 26,550,000.00 USD | 0.00 USD | 295.56 USD | `-66.80%` | `213.40` |
| `Live` | `Long` | `1.40` | 26,550,000.00 USD | 0.00 USD | 931.86 USD | `-66.56%` | `668.00` |
| `Live` | `Long` | `1.41` | 26,550,000.00 USD | 0.00 USD | 442.43 USD | `-66.32%` | `314.90` |
| `Live` | `Long` | `1.42` | 26,550,000.00 USD | 0.00 USD | 1,790.00 USD | `-66.08%` | `1,264.50` |
| `Live` | `Long` | `1.43` | 26,550,000.00 USD | 0.00 USD | 15,180.00 USD | `-65.84%` | `10,649.80` |
| `Live` | `Long` | `1.45` | 26,530,000.00 USD | 0.00 USD | 1,800.00 USD | `-65.36%` | `1,245.80` |
| `Live` | `Long` | `1.46` | 26,530,000.00 USD | 0.00 USD | 229.89 USD | `-65.12%` | `158.00` |
| `Live` | `Long` | `1.47` | 26,530,000.00 USD | 0.00 USD | 1,480.00 USD | `-64.88%` | `1,011.70` |
| `Live` | `Long` | `1.48` | 26,530,000.00 USD | 0.00 USD | 11,130.00 USD | `-64.64%` | `7,542.50` |
| `Live` | `Long` | `1.50` | 26,520,000.00 USD | 0.00 USD | 216.78 USD | `-64.16%` | `145.00` |
| `Live` | `Long` | `1.51` | 26,520,000.00 USD | 0.00 USD | 454.50 USD | `-63.68%` | `300.00` |
| `Live` | `Long` | `1.52` | 26,520,000.00 USD | 0.00 USD | 305.00 USD | `-63.44%` | `200.00` |
| `Live` | `Long` | `1.53` | 26,520,000.00 USD | 0.00 USD | 279.37 USD | `-63.20%` | `182.00` |
| `Live` | `Long` | `1.56` | 26,520,000.00 USD | 0.00 USD | 13,300.00 USD | `-62.48%` | `8,501.00` |
| `Live` | `Long` | `1.57` | 26,500,000.00 USD | 0.00 USD | 589.52 USD | `-62.24%` | `374.30` |
| `Live` | `Long` | `1.58` | 26,500,000.00 USD | 0.00 USD | 747.96 USD | `-62.00%` | `471.90` |
| `Live` | `Long` | `1.59` | 26,500,000.00 USD | 0.00 USD | 8,090.00 USD | `-61.76%` | `5,073.30` |
| `Live` | `Long` | `1.60` | 26,490,000.00 USD | 0.00 USD | 511.83 USD | `-61.52%` | `318.90` |
| `Live` | `Long` | `1.61` | 26,490,000.00 USD | 0.00 USD | 565,250.00 USD | `-61.28%` | `350,000.00` |
| `Live` | `Long` | `1.62` | 25,930,000.00 USD | 0.00 USD | 3,250.00 USD | `-61.04%` | `2,000.00` |
| `Live` | `Long` | `1.64` | 25,920,000.00 USD | 0.00 USD | 2,030.00 USD | `-60.80%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 25,920,000.00 USD | 0.00 USD | 2,460.00 USD | `-60.56%` | `1,496.60` |
| `Live` | `Long` | `1.66` | 25,920,000.00 USD | 0.00 USD | 384.13 USD | `-60.32%` | `232.10` |
| `Live` | `Long` | `1.67` | 25,920,000.00 USD | 0.00 USD | 5,340.00 USD | `-60.08%` | `3,206.70` |
| `Live` | `Long` | `1.68` | 25,910,000.00 USD | 0.00 USD | 1,190.00 USD | `-59.84%` | `708.70` |
| `Live` | `Long` | `1.69` | 25,910,000.00 USD | 0.00 USD | 26,390.00 USD | `-59.60%` | `15,664.40` |
| `Live` | `Long` | `1.70` | 25,890,000.00 USD | 0.00 USD | 294.76 USD | `-59.36%` | `173.90` |
| `Live` | `Long` | `1.71` | 25,890,000.00 USD | 0.00 USD | 4,640.00 USD | `-59.12%` | `2,722.80` |
| `Live` | `Long` | `1.72` | 25,880,000.00 USD | 0.00 USD | 12,930.00 USD | `-58.88%` | `7,537.90` |
| `Live` | `Long` | `1.73` | 25,870,000.00 USD | 0.00 USD | 8,020.00 USD | `-58.64%` | `4,648.10` |
| `Live` | `Long` | `1.74` | 25,860,000.00 USD | 0.00 USD | 3,870.00 USD | `-58.41%` | `2,229.40` |
| `Live` | `Long` | `1.75` | 25,860,000.00 USD | 0.00 USD | 391.58 USD | `-58.17%` | `224.40` |
| `Live` | `Long` | `1.75` | 25,860,000.00 USD | 0.00 USD | 11,460.00 USD | `-57.93%` | `6,531.00` |
| `Live` | `Long` | `1.77` | 25,840,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.45%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 25,840,000.00 USD | 0.00 USD | 4,700.00 USD | `-57.21%` | `2,632.70` |
| `Live` | `Long` | `1.80` | 25,840,000.00 USD | 0.00 USD | 730.66 USD | `-56.73%` | `404.80` |
| `Live` | `Long` | `1.81` | 25,840,000.00 USD | 0.00 USD | 100.55 USD | `-56.49%` | `55.40` |
| `Live` | `Long` | `1.83` | 25,840,000.00 USD | 0.00 USD | 28,390.00 USD | `-56.01%` | `15,470.20` |
| `Live` | `Long` | `1.84` | 25,810,000.00 USD | 0.00 USD | 15,170.00 USD | `-55.77%` | `8,223.20` |
| `Live` | `Long` | `1.85` | 25,790,000.00 USD | 0.00 USD | 4,130.00 USD | `-55.53%` | `2,227.40` |
| `Live` | `Long` | `1.88` | 25,790,000.00 USD | 0.00 USD | 937.50 USD | `-55.05%` | `500.00` |
| `Live` | `Long` | `1.89` | 25,790,000.00 USD | 0.00 USD | 10,530.00 USD | `-54.81%` | `5,583.80` |
| `Live` | `Long` | `1.90` | 25,780,000.00 USD | 0.00 USD | 40,000.00 USD | `-54.57%` | `21,105.90` |
| `Live` | `Long` | `1.91` | 25,740,000.00 USD | 0.00 USD | 2,070.00 USD | `-54.33%` | `1,084.50` |
| `Live` | `Long` | `1.93` | 25,730,000.00 USD | 0.00 USD | 2,850.00 USD | `-53.85%` | `1,482.80` |
| `Live` | `Long` | `1.95` | 25,730,000.00 USD | 0.00 USD | 3,710.00 USD | `-53.37%` | `1,909.40` |
| `Live` | `Long` | `1.96` | 25,730,000.00 USD | 0.00 USD | 775.55 USD | `-53.13%` | `396.70` |
| `Live` | `Long` | `1.97` | 25,730,000.00 USD | 0.00 USD | 10,180.00 USD | `-52.89%` | `5,182.20` |
| `Live` | `Long` | `1.98` | 25,720,000.00 USD | 0.00 USD | 46,180.00 USD | `-52.65%` | `23,380.00` |
| `Live` | `Long` | `1.99` | 25,670,000.00 USD | 0.00 USD | 36,830.00 USD | `-52.41%` | `18,554.80` |
| `Live` | `Long` | `2.00` | 25,630,000.00 USD | 0.00 USD | 122,770.00 USD | `-51.93%` | `61,234.30` |
| `Live` | `Long` | `2.02` | 25,510,000.00 USD | 0.00 USD | 23,610.00 USD | `-51.69%` | `11,718.70` |
| `Live` | `Long` | `2.02` | 25,490,000.00 USD | 0.00 USD | 409.05 USD | `-51.45%` | `202.00` |
| `Live` | `Long` | `2.04` | 25,490,000.00 USD | 0.00 USD | 112,690.00 USD | `-51.21%` | `55,377.10` |
| `Live` | `Long` | `2.04` | 25,370,000.00 USD | 0.00 USD | 4,820.00 USD | `-50.97%` | `2,357.30` |
| `Live` | `Long` | `2.06` | 25,370,000.00 USD | 0.00 USD | 1,850.00 USD | `-50.73%` | `900.00` |
| `Live` | `Long` | `2.06` | 25,370,000.00 USD | 0.00 USD | 548.46 USD | `-50.49%` | `265.60` |
| `Live` | `Long` | `2.08` | 25,370,000.00 USD | 0.00 USD | 28,940.00 USD | `-50.25%` | `13,945.80` |
| `Live` | `Long` | `2.08` | 25,340,000.00 USD | 0.00 USD | 27,630.00 USD | `-50.01%` | `13,253.00` |
| `Live` | `Long` | `2.10` | 25,310,000.00 USD | 0.00 USD | 8,570.00 USD | `-49.53%` | `4,070.00` |
| `Live` | `Long` | `2.12` | 25,300,000.00 USD | 0.00 USD | 30,880.00 USD | `-49.30%` | `14,602.60` |
| `Live` | `Long` | `2.12` | 25,270,000.00 USD | 0.00 USD | 169,050.00 USD | `-49.06%` | `79,552.30` |
| `Live` | `Long` | `2.15` | 25,100,000.00 USD | 0.00 USD | 214,010.00 USD | `-48.58%` | `99,769.80` |
| `Live` | `Long` | `2.15` | 24,890,000.00 USD | 0.00 USD | 1,270.00 USD | `-48.34%` | `590.90` |
| `Live` | `Long` | `2.17` | 24,890,000.00 USD | 0.00 USD | 216,500.00 USD | `-48.10%` | `100,000.00` |
| `Live` | `Long` | `2.19` | 24,670,000.00 USD | 0.00 USD | 13,820.00 USD | `-47.62%` | `6,325.30` |
| `Live` | `Long` | `2.19` | 24,660,000.00 USD | 0.00 USD | 714.03 USD | `-47.38%` | `325.30` |
| `Live` | `Long` | `2.21` | 24,660,000.00 USD | 0.00 USD | 37,530.00 USD | `-47.14%` | `17,018.40` |
| `Live` | `Long` | `2.21` | 24,620,000.00 USD | 0.00 USD | 639.47 USD | `-46.90%` | `288.70` |
| `Live` | `Long` | `2.23` | 24,620,000.00 USD | 0.00 USD | 2,310.00 USD | `-46.66%` | `1,040.10` |
| `Live` | `Long` | `2.23` | 24,610,000.00 USD | 0.00 USD | 34,210.00 USD | `-46.42%` | `15,308.60` |
| `Live` | `Long` | `2.25` | 24,580,000.00 USD | 0.00 USD | 4,910.00 USD | `-46.18%` | `2,185.10` |
| `Live` | `Long` | `2.25` | 24,580,000.00 USD | 0.00 USD | 115,820.00 USD | `-45.94%` | `51,360.80` |
| `Live` | `Long` | `2.29` | 24,460,000.00 USD | 0.00 USD | 804.32 USD | `-45.22%` | `352.00` |
| `Live` | `Long` | `2.29` | 24,460,000.00 USD | 0.00 USD | 2,150.00 USD | `-44.98%` | `936.90` |
| `Live` | `Long` | `2.31` | 24,460,000.00 USD | 0.00 USD | 8,710.00 USD | `-44.74%` | `3,779.50` |
| `Live` | `Long` | `2.31` | 24,450,000.00 USD | 0.00 USD | 2,880.00 USD | `-44.50%` | `1,242.10` |
| `Live` | `Long` | `2.33` | 24,450,000.00 USD | 0.00 USD | 2,190.00 USD | `-44.26%` | `942.60` |
| `Live` | `Long` | `2.33` | 24,440,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.02%` | `4,734.90` |
| `Live` | `Long` | `2.35` | 24,430,000.00 USD | 0.00 USD | 49,760.00 USD | `-43.78%` | `21,221.20` |
| `Live` | `Long` | `2.35` | 24,380,000.00 USD | 0.00 USD | 5,530.00 USD | `-43.54%` | `2,348.10` |
| `Live` | `Long` | `2.37` | 24,380,000.00 USD | 0.00 USD | 50,910.00 USD | `-43.30%` | `21,526.50` |
| `Live` | `Long` | `2.38` | 24,330,000.00 USD | 0.00 USD | 422,330.00 USD | `-43.06%` | `177,821.90` |
| `Live` | `Long` | `2.38` | 23,900,000.00 USD | 0.00 USD | 534.24 USD | `-42.82%` | `224.00` |
| `Live` | `Long` | `2.40` | 23,900,000.00 USD | 0.00 USD | 11,360.00 USD | `-42.58%` | `4,743.60` |
| `Live` | `Long` | `2.40` | 23,890,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-42.34%` | `664,872.90` |
| `Live` | `Long` | `2.42` | 22,290,000.00 USD | 0.00 USD | 224,000.00 USD | `-42.10%` | `92,753.80` |
| `Live` | `Long` | `2.42` | 22,070,000.00 USD | 0.00 USD | 274,270.00 USD | `-41.86%` | `113,101.40` |
| `Live` | `Long` | `2.44` | 21,790,000.00 USD | 0.00 USD | 5,350.00 USD | `-41.62%` | `2,196.80` |
| `Live` | `Long` | `2.44` | 21,790,000.00 USD | 0.00 USD | 8,210.00 USD | `-41.38%` | `3,356.60` |
| `Live` | `Long` | `2.46` | 21,780,000.00 USD | 0.00 USD | 15,800.00 USD | `-41.14%` | `6,436.10` |
| `Live` | `Long` | `2.46` | 21,760,000.00 USD | 0.00 USD | 17,800.00 USD | `-40.90%` | `7,222.10` |
| `Live` | `Long` | `2.48` | 21,750,000.00 USD | 0.00 USD | 1,620.00 USD | `-40.66%` | `654.00` |
| `Live` | `Long` | `2.48` | 21,750,000.00 USD | 0.00 USD | 5,870.00 USD | `-40.42%` | `2,363.00` |
| `Live` | `Long` | `2.50` | 21,740,000.00 USD | 0.00 USD | 1,110.00 USD | `-40.19%` | `443.10` |
| `Live` | `Long` | `2.50` | 21,740,000.00 USD | 0.00 USD | 7,810.00 USD | `-39.95%` | `3,117.70` |
| `Live` | `Long` | `2.52` | 21,730,000.00 USD | 0.00 USD | 121.98 USD | `-39.71%` | `48.50` |
| `Live` | `Long` | `2.52` | 21,730,000.00 USD | 0.00 USD | 414,260.00 USD | `-39.47%` | `164,065.30` |
| `Live` | `Long` | `2.54` | 21,320,000.00 USD | 0.00 USD | 395.71 USD | `-39.23%` | `156.10` |
| `Live` | `Long` | `2.54` | 21,320,000.00 USD | 0.00 USD | 10,920.00 USD | `-38.99%` | `4,291.70` |
| `Live` | `Long` | `2.56` | 21,310,000.00 USD | 0.00 USD | 7,430.00 USD | `-38.75%` | `2,908.50` |
| `Live` | `Long` | `2.56` | 21,300,000.00 USD | 0.00 USD | 7,890.00 USD | `-38.51%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 21,290,000.00 USD | 0.00 USD | 839.97 USD | `-38.27%` | `326.20` |
| `Live` | `Long` | `2.58` | 21,290,000.00 USD | 0.00 USD | 1,570.00 USD | `-38.03%` | `607.20` |
| `Live` | `Long` | `2.60` | 21,290,000.00 USD | 0.00 USD | 71,490.00 USD | `-37.79%` | `27,547.60` |
| `Live` | `Long` | `2.62` | 21,220,000.00 USD | 0.00 USD | 1,820.00 USD | `-37.31%` | `694.70` |
| `Live` | `Long` | `2.62` | 21,210,000.00 USD | 0.00 USD | 359.10 USD | `-37.07%` | `136.80` |
| `Live` | `Long` | `2.63` | 21,210,000.00 USD | 0.00 USD | 48,970.00 USD | `-36.83%` | `18,584.90` |
| `Live` | `Long` | `2.65` | 21,160,000.00 USD | 0.00 USD | 6,920.00 USD | `-36.59%` | `2,614.70` |
| `Live` | `Long` | `2.65` | 21,160,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-36.35%` | `907,059.40` |
| `Live` | `Long` | `2.67` | 18,750,000.00 USD | 0.00 USD | 11,010.00 USD | `-36.11%` | `4,131.60` |
| `Live` | `Long` | `2.67` | 18,740,000.00 USD | 0.00 USD | 375.84 USD | `-35.87%` | `140.50` |
| `Live` | `Long` | `2.69` | 18,740,000.00 USD | 0.00 USD | 4,990.00 USD | `-35.63%` | `1,859.30` |
| `Live` | `Long` | `2.69` | 18,730,000.00 USD | 0.00 USD | 3,150.00 USD | `-35.39%` | `1,167.70` |
| `Live` | `Long` | `2.71` | 18,730,000.00 USD | 0.00 USD | 119,930.00 USD | `-35.15%` | `44,335.90` |
| `Live` | `Long` | `2.71` | 18,610,000.00 USD | 0.00 USD | 19,910.00 USD | `-34.91%` | `7,332.60` |
| `Live` | `Long` | `2.73` | 18,590,000.00 USD | 0.00 USD | 27,130.00 USD | `-34.67%` | `9,955.90` |
| `Live` | `Long` | `2.73` | 18,560,000.00 USD | 0.00 USD | 1,850.00 USD | `-34.43%` | `675.80` |
| `Live` | `Long` | `2.75` | 18,560,000.00 USD | 0.00 USD | 41,060.00 USD | `-34.19%` | `14,958.60` |
| `Live` | `Long` | `2.75` | 18,520,000.00 USD | 0.00 USD | 154.83 USD | `-33.95%` | `56.20` |
| `Live` | `Long` | `2.77` | 18,520,000.00 USD | 0.00 USD | 6,500.00 USD | `-33.71%` | `2,350.90` |
| `Live` | `Long` | `2.77` | 18,510,000.00 USD | 0.00 USD | 12,800.00 USD | `-33.47%` | `4,613.30` |
| `Live` | `Long` | `2.79` | 18,500,000.00 USD | 0.00 USD | 36,670.00 USD | `-33.23%` | `13,165.70` |
| `Live` | `Long` | `2.79` | 18,460,000.00 USD | 0.00 USD | 15,020.00 USD | `-32.99%` | `5,373.70` |
| `Live` | `Long` | `2.81` | 18,450,000.00 USD | 0.00 USD | 6,310.00 USD | `-32.75%` | `2,248.90` |
| `Live` | `Long` | `2.81` | 18,440,000.00 USD | 0.00 USD | 572.29 USD | `-32.51%` | `203.30` |
| `Live` | `Long` | `2.83` | 18,440,000.00 USD | 0.00 USD | 180,080.00 USD | `-32.27%` | `63,743.90` |
| `Live` | `Long` | `2.83` | 18,260,000.00 USD | 0.00 USD | 11,980.00 USD | `-32.03%` | `4,225.10` |
| `Live` | `Long` | `2.85` | 18,250,000.00 USD | 0.00 USD | 367,060.00 USD | `-31.79%` | `129,020.70` |
| `Live` | `Long` | `2.85` | 17,880,000.00 USD | 0.00 USD | 8,640.00 USD | `-31.55%` | `3,027.70` |
| `Live` | `Long` | `2.87` | 17,870,000.00 USD | 0.00 USD | 7,750.00 USD | `-31.31%` | `2,706.40` |
| `Live` | `Long` | `2.88` | 17,870,000.00 USD | 0.00 USD | 420.61 USD | `-31.07%` | `146.30` |
| `Live` | `Long` | `2.88` | 17,870,000.00 USD | 0.00 USD | 5,930.00 USD | `-30.84%` | `2,054.60` |
| `Live` | `Long` | `2.90` | 17,860,000.00 USD | 0.00 USD | 19,800.00 USD | `-30.60%` | `6,839.90` |
| `Live` | `Long` | `2.90` | 17,840,000.00 USD | 0.00 USD | 215,820.00 USD | `-30.36%` | `74,293.50` |
| `Live` | `Long` | `2.92` | 17,620,000.00 USD | 0.00 USD | 11,600.00 USD | `-30.12%` | `3,978.60` |
| `Live` | `Long` | `2.92` | 17,610,000.00 USD | 0.00 USD | 1,460.00 USD | `-29.88%` | `500.80` |
| `Live` | `Long` | `2.94` | 17,610,000.00 USD | 0.00 USD | 66,720.00 USD | `-29.64%` | `22,731.40` |
| `Live` | `Long` | `2.94` | 17,540,000.00 USD | 0.00 USD | 1,680.00 USD | `-29.40%` | `569.20` |
| `Live` | `Long` | `2.96` | 17,540,000.00 USD | 0.00 USD | 45,080.00 USD | `-29.16%` | `15,255.20` |
| `Live` | `Long` | `2.96` | 17,500,000.00 USD | 0.00 USD | 9,080.00 USD | `-28.92%` | `3,061.00` |
| `Live` | `Long` | `2.98` | 17,490,000.00 USD | 0.00 USD | 12,440.00 USD | `-28.68%` | `4,181.50` |
| `Live` | `Long` | `2.98` | 17,480,000.00 USD | 0.00 USD | 1,240.00 USD | `-28.44%` | `416.10` |
| `Live` | `Long` | `3.00` | 17,480,000.00 USD | 0.00 USD | 2,000.00 USD | `-28.20%` | `666.40` |
| `Live` | `Long` | `3.00` | 17,470,000.00 USD | 0.00 USD | 169,060.00 USD | `-27.96%` | `56,260.80` |
| `Live` | `Long` | `3.02` | 17,300,000.00 USD | 0.00 USD | 11,290.00 USD | `-27.72%` | `3,743.00` |
| `Live` | `Long` | `3.02` | 17,290,000.00 USD | 0.00 USD | 13,310.00 USD | `-27.48%` | `4,401.60` |
| `Live` | `Long` | `3.04` | 17,280,000.00 USD | 0.00 USD | 842.82 USD | `-27.24%` | `277.70` |
| `Live` | `Long` | `3.04` | 17,280,000.00 USD | 0.00 USD | 131,300.00 USD | `-27.00%` | `43,120.40` |
| `Live` | `Long` | `3.06` | 17,150,000.00 USD | 0.00 USD | 165,040.00 USD | `-26.76%` | `54,021.50` |
| `Live` | `Long` | `3.06` | 16,980,000.00 USD | 0.00 USD | 477,830.00 USD | `-26.52%` | `155,899.60` |
| `Live` | `Long` | `3.08` | 16,500,000.00 USD | 0.00 USD | 411.44 USD | `-26.28%` | `133.80` |
| `Live` | `Long` | `3.08` | 16,500,000.00 USD | 0.00 USD | 30,170.00 USD | `-26.04%` | `9,781.10` |
| `Live` | `Long` | `3.10` | 16,470,000.00 USD | 0.00 USD | 7,550.00 USD | `-25.80%` | `2,439.30` |
| `Live` | `Long` | `3.10` | 16,470,000.00 USD | 0.00 USD | 21,960.00 USD | `-25.56%` | `7,073.60` |
| `Live` | `Long` | `3.12` | 16,440,000.00 USD | 0.00 USD | 104,690.00 USD | `-25.32%` | `33,608.90` |
| `Live` | `Long` | `3.12` | 16,340,000.00 USD | 0.00 USD | 13,260.00 USD | `-25.08%` | `4,244.50` |
| `Live` | `Long` | `3.13` | 16,330,000.00 USD | 0.00 USD | 165,620.00 USD | `-24.84%` | `52,830.30` |
| `Live` | `Long` | `3.15` | 16,160,000.00 USD | 0.00 USD | 741.91 USD | `-24.60%` | `235.90` |
| `Live` | `Long` | `3.15` | 16,160,000.00 USD | 0.00 USD | 97,170.00 USD | `-24.36%` | `30,799.70` |
| `Live` | `Long` | `3.17` | 16,060,000.00 USD | 0.00 USD | 222,700.00 USD | `-24.12%` | `70,364.40` |
| `Live` | `Long` | `3.17` | 15,840,000.00 USD | 0.00 USD | 10,200.00 USD | `-23.88%` | `3,211.10` |
| `Live` | `Long` | `3.19` | 15,830,000.00 USD | 0.00 USD | 6,870.00 USD | `-23.64%` | `2,157.90` |
| `Live` | `Long` | `3.21` | 15,820,000.00 USD | 0.00 USD | 105,270.00 USD | `-23.16%` | `32,844.70` |
| `Live` | `Long` | `3.21` | 15,720,000.00 USD | 0.00 USD | 13,860.00 USD | `-22.92%` | `4,311.80` |
| `Live` | `Long` | `3.23` | 15,700,000.00 USD | 0.00 USD | 27,650.00 USD | `-22.68%` | `8,574.70` |
| `Live` | `Long` | `3.23` | 15,680,000.00 USD | 0.00 USD | 19,880.00 USD | `-22.44%` | `6,144.90` |
| `Live` | `Long` | `3.25` | 15,660,000.00 USD | 0.00 USD | 17,300.00 USD | `-22.20%` | `5,331.80` |
| `Live` | `Long` | `3.25` | 15,640,000.00 USD | 0.00 USD | 62,120.00 USD | `-21.96%` | `19,085.00` |
| `Live` | `Long` | `3.27` | 15,580,000.00 USD | 0.00 USD | 37,970.00 USD | `-21.73%` | `11,629.90` |
| `Live` | `Long` | `3.27` | 15,540,000.00 USD | 0.00 USD | 838,480.00 USD | `-21.49%` | `256,024.70` |
| `Live` | `Long` | `3.29` | 14,700,000.00 USD | 0.00 USD | 5,780.00 USD | `-21.25%` | `1,758.60` |
| `Live` | `Long` | `3.29` | 14,690,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-21.01%` | `403,073.20` |
| `Live` | `Long` | `3.31` | 13,370,000.00 USD | 0.00 USD | 69,450.00 USD | `-20.77%` | `21,014.70` |
| `Live` | `Long` | `3.31` | 13,300,000.00 USD | 0.00 USD | 20,450.00 USD | `-20.53%` | `6,169.70` |
| `Live` | `Long` | `3.33` | 13,280,000.00 USD | 0.00 USD | 19,420.00 USD | `-20.29%` | `5,839.60` |
| `Live` | `Long` | `3.33` | 13,260,000.00 USD | 0.00 USD | 63,210.00 USD | `-20.05%` | `18,952.80` |
| `Live` | `Long` | `3.35` | 13,190,000.00 USD | 0.00 USD | 26,150.00 USD | `-19.81%` | `7,819.00` |
| `Live` | `Long` | `3.35` | 13,170,000.00 USD | 0.00 USD | 2,120.00 USD | `-19.57%` | `631.30` |
| `Live` | `Long` | `3.37` | 13,170,000.00 USD | 0.00 USD | 1,930.00 USD | `-19.33%` | `573.60` |
| `Live` | `Long` | `3.38` | 13,160,000.00 USD | 0.00 USD | 15,580.00 USD | `-19.09%` | `4,617.00` |
| `Live` | `Long` | `3.38` | 13,150,000.00 USD | 0.00 USD | 43,640.00 USD | `-18.85%` | `12,892.50` |
| `Live` | `Long` | `3.40` | 13,100,000.00 USD | 0.00 USD | 6,790.00 USD | `-18.61%` | `2,000.00` |
| `Live` | `Long` | `3.40` | 13,100,000.00 USD | 0.00 USD | 76,440.00 USD | `-18.37%` | `22,450.30` |
| `Live` | `Long` | `3.42` | 13,020,000.00 USD | 0.00 USD | 188,400.00 USD | `-18.13%` | `55,167.30` |
| `Live` | `Long` | `3.42` | 12,830,000.00 USD | 0.00 USD | 7,040.00 USD | `-17.89%` | `2,056.10` |
| `Live` | `Long` | `3.44` | 12,830,000.00 USD | 0.00 USD | 33,260.00 USD | `-17.65%` | `9,682.90` |
| `Live` | `Long` | `3.44` | 12,790,000.00 USD | 0.00 USD | 42,880.00 USD | `-17.41%` | `12,448.40` |
| `Live` | `Long` | `3.46` | 12,750,000.00 USD | 0.00 USD | 110,800.00 USD | `-17.17%` | `32,069.30` |
| `Live` | `Long` | `3.46` | 12,640,000.00 USD | 0.00 USD | 6,020.00 USD | `-16.93%` | `1,738.80` |
| `Live` | `Long` | `3.48` | 12,630,000.00 USD | 0.00 USD | 47,740.00 USD | `-16.69%` | `13,737.40` |
| `Live` | `Long` | `3.48` | 12,590,000.00 USD | 0.00 USD | 666,400.00 USD | `-16.45%` | `191,220.90` |
| `Live` | `Long` | `3.50` | 11,920,000.00 USD | 0.00 USD | 36,570.00 USD | `-16.21%` | `10,462.20` |
| `Live` | `Long` | `3.50` | 11,880,000.00 USD | 0.00 USD | 20,210.00 USD | `-15.97%` | `5,767.10` |
| `Live` | `Long` | `3.52` | 11,860,000.00 USD | 0.00 USD | 8,990.00 USD | `-15.73%` | `2,558.60` |
| `Live` | `Long` | `3.52` | 11,850,000.00 USD | 0.00 USD | 12,290.00 USD | `-15.49%` | `3,487.30` |
| `Live` | `Long` | `3.54` | 11,840,000.00 USD | 0.00 USD | 18,420.00 USD | `-15.25%` | `5,210.30` |
| `Live` | `Long` | `3.54` | 11,820,000.00 USD | 0.00 USD | 345,290.00 USD | `-15.01%` | `97,402.40` |
| `Live` | `Long` | `3.56` | 11,480,000.00 USD | 0.00 USD | 414,820.00 USD | `-14.77%` | `116,687.20` |
| `Live` | `Long` | `3.56` | 11,060,000.00 USD | 0.00 USD | 6,600.00 USD | `-14.53%` | `1,851.50` |
| `Live` | `Long` | `3.58` | 11,060,000.00 USD | 0.00 USD | 799,940.00 USD | `-14.29%` | `223,759.20` |
| `Live` | `Long` | `3.58` | 10,260,000.00 USD | 0.00 USD | 138,890.00 USD | `-14.05%` | `38,741.50` |
| `Live` | `Long` | `3.60` | 10,120,000.00 USD | 0.00 USD | 23,250.00 USD | `-13.81%` | `6,467.90` |
| `Live` | `Long` | `3.60` | 10,090,000.00 USD | 0.00 USD | 144,000.00 USD | `-13.57%` | `39,945.30` |
| `Live` | `Long` | `3.62` | 9,950,000.00 USD | 0.00 USD | 7,850.00 USD | `-13.33%` | `2,172.00` |
| `Live` | `Long` | `3.62` | 9,940,000.00 USD | 0.00 USD | 24,880.00 USD | `-13.09%` | `6,863.40` |
| `Live` | `Long` | `3.63` | 9,920,000.00 USD | 0.00 USD | 23,390.00 USD | `-12.85%` | `6,433.90` |
| `Live` | `Long` | `3.65` | 9,890,000.00 USD | 0.00 USD | 63,230.00 USD | `-12.62%` | `17,345.90` |
| `Live` | `Long` | `3.65` | 9,830,000.00 USD | 0.00 USD | 40,820.00 USD | `-12.38%` | `11,167.40` |
| `Live` | `Long` | `3.67` | 9,790,000.00 USD | 0.00 USD | 214,400.00 USD | `-12.14%` | `58,498.00` |
| `Live` | `Long` | `3.67` | 9,580,000.00 USD | 0.00 USD | 576,550.00 USD | `-11.90%` | `156,885.60` |
| `Live` | `Long` | `3.69` | 9,000,000.00 USD | 0.00 USD | 168,120.00 USD | `-11.66%` | `45,622.80` |
| `Live` | `Long` | `3.69` | 8,830,000.00 USD | 0.00 USD | 111,220.00 USD | `-11.42%` | `30,100.60` |
| `Live` | `Long` | `3.71` | 8,720,000.00 USD | 0.00 USD | 31,300.00 USD | `-11.18%` | `8,449.00` |
| `Live` | `Long` | `3.71` | 8,690,000.00 USD | 0.00 USD | 41,960.00 USD | `-10.94%` | `11,294.60` |
| `Live` | `Long` | `3.73` | 8,650,000.00 USD | 0.00 USD | 55,240.00 USD | `-10.70%` | `14,830.40` |
| `Live` | `Long` | `3.73` | 8,590,000.00 USD | 0.00 USD | 30,700.00 USD | `-10.46%` | `8,219.20` |
| `Live` | `Long` | `3.75` | 8,560,000.00 USD | 0.00 USD | 31,700.00 USD | `-10.22%` | `8,464.70` |
| `Live` | `Long` | `3.75` | 8,530,000.00 USD | 0.00 USD | 107,800.00 USD | `-9.98%` | `28,709.10` |
| `Live` | `Long` | `3.77` | 8,420,000.00 USD | 0.00 USD | 207,410.00 USD | `-9.74%` | `55,088.30` |
| `Live` | `Long` | `3.77` | 8,210,000.00 USD | 0.00 USD | 11,560.00 USD | `-9.50%` | `3,061.20` |
| `Live` | `Long` | `3.79` | 8,200,000.00 USD | 0.00 USD | 40,070.00 USD | `-9.26%` | `10,585.90` |
| `Live` | `Long` | `3.79` | 8,160,000.00 USD | 0.00 USD | 260,160.00 USD | `-9.02%` | `68,552.50` |
| `Live` | `Long` | `3.81` | 7,900,000.00 USD | 0.00 USD | 17,470.00 USD | `-8.78%` | `4,591.60` |
| `Live` | `Long` | `3.81` | 7,880,000.00 USD | 0.00 USD | 36,220.00 USD | `-8.54%` | `9,494.20` |
| `Live` | `Long` | `3.83` | 7,850,000.00 USD | 0.00 USD | 36,270.00 USD | `-8.30%` | `9,481.20` |
| `Live` | `Long` | `3.83` | 7,810,000.00 USD | 0.00 USD | 151,710.00 USD | `-8.06%` | `39,560.60` |
| `Live` | `Long` | `3.85` | 7,660,000.00 USD | 0.00 USD | 26,070.00 USD | `-7.82%` | `6,779.60` |
| `Live` | `Long` | `3.85` | 7,630,000.00 USD | 0.00 USD | 10,450.00 USD | `-7.58%` | `2,712.00` |
| `Live` | `Long` | `3.87` | 7,620,000.00 USD | 0.00 USD | 20,220.00 USD | `-7.34%` | `5,231.10` |
| `Live` | `Long` | `3.88` | 7,600,000.00 USD | 0.00 USD | 42,080.00 USD | `-7.10%` | `10,859.90` |
| `Live` | `Long` | `3.88` | 7,560,000.00 USD | 0.00 USD | 33,300.00 USD | `-6.86%` | `8,572.00` |
| `Live` | `Long` | `3.90` | 7,530,000.00 USD | 0.00 USD | 216,450.00 USD | `-6.62%` | `55,571.20` |
| `Live` | `Long` | `3.90` | 7,310,000.00 USD | 0.00 USD | 17,140.00 USD | `-6.38%` | `4,388.90` |
| `Live` | `Long` | `3.92` | 7,290,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-6.14%` | `1,001,780.80` |
| `Live` | `Long` | `3.92` | 3,370,000.00 USD | 0.00 USD | 338,920.00 USD | `-5.90%` | `86,347.90` |
| `Live` | `Short` | `3.94` | 222,790.00 USD | 222,790.00 USD | 0.00 USD | `-5.66%` | `56,618.80` |
| `Live` | `Long` | `3.94` | 3,030,000.00 USD | 0.00 USD | 129,280.00 USD | `-5.42%` | `32,771.20` |
| `Live` | `Long` | `3.96` | 2,900,000.00 USD | 0.00 USD | 210,040.00 USD | `-5.18%` | `53,106.60` |
| `Live` | `Long` | `3.96` | 2,690,000.00 USD | 0.00 USD | 686,500.00 USD | `-4.94%` | `173,141.00` |
| `Live` | `Long` | `3.98` | 2,010,000.00 USD | 0.00 USD | 2,510.00 USD | `-4.70%` | `631.50` |
| `Live` | `Long` | `3.98` | 2,000,000.00 USD | 0.00 USD | 88,360.00 USD | `-4.46%` | `22,173.10` |
| `Live` | `Long` | `4.00` | 1,920,000.00 USD | 0.00 USD | 16,100.00 USD | `-4.22%` | `4,031.10` |
| `Live` | `Long` | `4.00` | 1,900,000.00 USD | 0.00 USD | 48,460.00 USD | `-3.98%` | `12,101.00` |
| `Live` | `Long` | `4.01` | 1,850,000.00 USD | 0.00 USD | 13,580.00 USD | `-3.74%` | `3,382.70` |
| `Live` | `Long` | `4.03` | 1,840,000.00 USD | 0.00 USD | 72,480.00 USD | `-3.50%` | `18,007.30` |
| `Live` | `Long` | `4.04` | 1,770,000.00 USD | 0.00 USD | 30,730.00 USD | `-3.27%` | `7,616.50` |
| `Live` | `Long` | `4.04` | 1,740,000.00 USD | 0.00 USD | 38,860.00 USD | `-3.03%` | `9,606.20` |
| `Live` | `Long` | `4.05` | 1,700,000.00 USD | 0.00 USD | 88,020.00 USD | `-2.79%` | `21,707.50` |
| `Live` | `Long` | `4.07` | 1,610,000.00 USD | 0.00 USD | 352,920.00 USD | `-2.55%` | `86,818.50` |
| `Live` | `Long` | `4.08` | 1,260,000.00 USD | 0.00 USD | 156,040.00 USD | `-2.31%` | `38,293.20` |
| `Live` | `Long` | `4.08` | 1,100,000.00 USD | 0.00 USD | 61,840.00 USD | `-2.07%` | `15,138.00` |
| `Live` | `Long` | `4.09` | 1,040,000.00 USD | 0.00 USD | 709,180.00 USD | `-1.83%` | `173,181.80` |
| `Live` | `Long` | `4.11` | 328,310.00 USD | 0.00 USD | 133,830.00 USD | `-1.59%` | `32,601.80` |
| `Live` | `Long` | `4.12` | 194,480.00 USD | 0.00 USD | 473.96 USD | `-1.11%` | `114.90` |
| `Live` | `Long` | `4.13` | 194,000.00 USD | 0.00 USD | 185,670.00 USD | `-0.87%` | `44,901.20` |
| `Live` | `Long` | `4.14` | 8,340.00 USD | 0.00 USD | 7,670.00 USD | `-0.63%` | `1,850.10` |
| `Live` | `Long` | `4.17` | 669.32 USD | 0.00 USD | 669.32 USD | `-0.15%` | `160.70` |
| `Live` | `Short` | `4.21` | 227,130.00 USD | 4,340.00 USD | 0.00 USD | `+0.81%` | `1,031.80` |
| `Live` | `Short` | `4.21` | 227,360.00 USD | 229.72 USD | 0.00 USD | `+1.05%` | `54.50` |
| `Live` | `Short` | `4.26` | 236,580.00 USD | 9,210.00 USD | 0.00 USD | `+2.25%` | `2,160.10` |
| `Live` | `Short` | `4.28` | 236,920.00 USD | 344.14 USD | 0.00 USD | `+2.49%` | `80.50` |
| `Live` | `Short` | `4.32` | 241,870.00 USD | 4,940.00 USD | 0.00 USD | `+3.45%` | `1,146.00` |
| `Live` | `Short` | `4.33` | 242,670.00 USD | 807.48 USD | 0.00 USD | `+3.69%` | `186.70` |
| `Live` | `Short` | `4.33` | 242,900.00 USD | 224.99 USD | 0.00 USD | `+3.93%` | `51.90` |
| `Live` | `Short` | `4.36` | 243,210.00 USD | 310.51 USD | 0.00 USD | `+4.41%` | `71.30` |
| `Live` | `Short` | `4.37` | 251,120.00 USD | 7,910.00 USD | 0.00 USD | `+4.65%` | `1,813.00` |
| `Live` | `Short` | `4.38` | 371,080.00 USD | 119,960.00 USD | 0.00 USD | `+4.89%` | `27,419.60` |
| `Live` | `Short` | `4.38` | 383,140.00 USD | 12,050.00 USD | 0.00 USD | `+5.13%` | `2,748.90` |
| `Live` | `Short` | `4.39` | 413,040.00 USD | 29,910.00 USD | 0.00 USD | `+5.37%` | `6,804.40` |
| `Live` | `Short` | `4.41` | 434,300.00 USD | 21,260.00 USD | 0.00 USD | `+5.61%` | `4,826.60` |
| `Live` | `Short` | `4.42` | 564,050.00 USD | 129,750.00 USD | 0.00 USD | `+5.84%` | `29,388.00` |
| `Live` | `Short` | `4.42` | 587,080.00 USD | 23,030.00 USD | 0.00 USD | `+6.08%` | `5,203.40` |
| `Live` | `Short` | `4.43` | 680,180.00 USD | 93,100.00 USD | 0.00 USD | `+6.32%` | `20,991.90` |
| `Live` | `Short` | `4.45` | 685,250.00 USD | 5,070.00 USD | 0.00 USD | `+6.56%` | `1,141.20` |
| `Live` | `Short` | `4.46` | 688,840.00 USD | 3,590.00 USD | 0.00 USD | `+7.04%` | `804.40` |
| `Live` | `Short` | `4.47` | 723,060.00 USD | 34,220.00 USD | 0.00 USD | `+7.28%` | `7,645.90` |
| `Live` | `Short` | `4.49` | 729,500.00 USD | 6,450.00 USD | 0.00 USD | `+7.52%` | `1,437.20` |
| `Live` | `Short` | `4.50` | 753,060.00 USD | 23,560.00 USD | 0.00 USD | `+7.76%` | `5,241.00` |
| `Live` | `Short` | `4.50` | 753,850.00 USD | 790.18 USD | 0.00 USD | `+8.00%` | `175.40` |
| `Live` | `Short` | `4.53` | 771,950.00 USD | 18,100.00 USD | 0.00 USD | `+8.48%` | `4,000.00` |
| `Live` | `Short` | `4.54` | 772,750.00 USD | 798.10 USD | 0.00 USD | `+8.96%` | `175.60` |
| `Live` | `Short` | `4.55` | 836,280.00 USD | 63,530.00 USD | 0.00 USD | `+9.20%` | `13,948.00` |
| `Live` | `Short` | `4.57` | 837,220.00 USD | 934.46 USD | 0.00 USD | `+9.44%` | `204.70` |
| `Live` | `Short` | `4.61` | 875,840.00 USD | 38,620.00 USD | 0.00 USD | `+10.40%` | `8,386.70` |
| `Live` | `Short` | `4.63` | 880,170.00 USD | 4,330.00 USD | 0.00 USD | `+11.12%` | `934.90` |
| `Live` | `Short` | `4.64` | 991,060.00 USD | 110,890.00 USD | 0.00 USD | `+11.36%` | `23,872.90` |
| `Live` | `Short` | `4.66` | 1,040,000.00 USD | 47,590.00 USD | 0.00 USD | `+11.60%` | `10,222.60` |
| `Live` | `Short` | `4.67` | 1,160,000.00 USD | 124,390.00 USD | 0.00 USD | `+11.84%` | `26,664.20` |
| `Live` | `Short` | `4.67` | 1,160,000.00 USD | 154.74 USD | 0.00 USD | `+12.08%` | `33.10` |
| `Live` | `Short` | `4.70` | 1,160,000.00 USD | 1,050.00 USD | 0.00 USD | `+12.56%` | `224.00` |
| `Live` | `Short` | `4.71` | 1,170,000.00 USD | 5,290.00 USD | 0.00 USD | `+12.80%` | `1,125.20` |
| `Live` | `Short` | `4.75` | 1,740,000.00 USD | 573,930.00 USD | 0.00 USD | `+13.76%` | `120,953.70` |
| `Live` | `Short` | `4.75` | 1,750,000.00 USD | 1,720.00 USD | 0.00 USD | `+14.00%` | `362.40` |
| `Live` | `Short` | `4.76` | 1,750,000.00 USD | 1,580.00 USD | 0.00 USD | `+14.24%` | `332.30` |
| `Live` | `Short` | `4.78` | 1,760,000.00 USD | 9,440.00 USD | 0.00 USD | `+14.48%` | `1,977.00` |
| `Live` | `Short` | `4.79` | 1,780,000.00 USD | 25,940.00 USD | 0.00 USD | `+14.72%` | `5,420.50` |
| `Live` | `Short` | `4.79` | 1,780,000.00 USD | 2,460.00 USD | 0.00 USD | `+14.95%` | `513.30` |
| `Live` | `Short` | `4.80` | 1,790,000.00 USD | 5,140.00 USD | 0.00 USD | `+15.19%` | `1,069.00` |
| `Live` | `Short` | `4.82` | 1,840,000.00 USD | 54,380.00 USD | 0.00 USD | `+15.43%` | `11,294.50` |
| `Live` | `Short` | `4.83` | 1,850,000.00 USD | 1,740.00 USD | 0.00 USD | `+15.67%` | `360.90` |
| `Live` | `Short` | `4.83` | 1,860,000.00 USD | 15,700.00 USD | 0.00 USD | `+15.91%` | `3,247.80` |
| `Live` | `Short` | `4.86` | 1,860,000.00 USD | 453.46 USD | 0.00 USD | `+16.39%` | `93.40` |
| `Live` | `Short` | `4.87` | 1,870,000.00 USD | 5,460.00 USD | 0.00 USD | `+16.63%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 1,880,000.00 USD | 14,550.00 USD | 0.00 USD | `+16.87%` | `2,984.20` |
| `Live` | `Short` | `4.88` | 1,900,000.00 USD | 15,160.00 USD | 0.00 USD | `+17.11%` | `3,103.20` |
| `Live` | `Short` | `4.92` | 1,920,000.00 USD | 20,720.00 USD | 0.00 USD | `+17.83%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,920,000.00 USD | 2,100.00 USD | 0.00 USD | `+18.07%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,920,000.00 USD | 556.67 USD | 0.00 USD | `+18.31%` | `112.80` |
| `Live` | `Short` | `4.96` | 1,920,000.00 USD | 452.89 USD | 0.00 USD | `+18.79%` | `91.40` |
| `Live` | `Short` | `4.97` | 2,230,000.00 USD | 308,200.00 USD | 0.00 USD | `+19.27%` | `61,950.20` |
| `Live` | `Short` | `4.99` | 2,230,000.00 USD | 1,710.00 USD | 0.00 USD | `+19.51%` | `343.70` |
| `Live` | `Short` | `5.00` | 2,230,000.00 USD | 339.66 USD | 0.00 USD | `+19.75%` | `68.00` |
| `Live` | `Short` | `5.01` | 2,230,000.00 USD | 1,350.00 USD | 0.00 USD | `+20.23%` | `268.20` |
| `Live` | `Short` | `5.04` | 2,230,000.00 USD | 1,160.00 USD | 0.00 USD | `+20.95%` | `230.50` |
| `Live` | `Short` | `5.05` | 2,290,000.00 USD | 55,570.00 USD | 0.00 USD | `+21.19%` | `10,993.80` |
| `Live` | `Short` | `5.07` | 2,290,000.00 USD | 3,420.00 USD | 0.00 USD | `+21.43%` | `675.80` |
| `Live` | `Short` | `5.08` | 2,300,000.00 USD | 3,190.00 USD | 0.00 USD | `+21.91%` | `627.90` |
| `Live` | `Short` | `5.12` | 2,300,000.00 USD | 2,560.00 USD | 0.00 USD | `+22.87%` | `500.00` |
| `Live` | `Short` | `5.13` | 2,300,000.00 USD | 1,080.00 USD | 0.00 USD | `+23.11%` | `210.70` |
| `Live` | `Short` | `5.17` | 2,320,000.00 USD | 21,090.00 USD | 0.00 USD | `+23.83%` | `4,083.70` |
| `Live` | `Short` | `5.20` | 2,500,000.00 USD | 175,590.00 USD | 0.00 USD | `+24.54%` | `33,800.00` |
| `Live` | `Short` | `5.21` | 3,390,000.00 USD | 898,120.00 USD | 0.00 USD | `+24.78%` | `172,549.20` |
| `Live` | `Short` | `5.21` | 3,920,000.00 USD | 527,490.00 USD | 0.00 USD | `+25.02%` | `101,148.30` |
| `Live` | `Short` | `5.22` | 3,990,000.00 USD | 72,110.00 USD | 0.00 USD | `+25.26%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 3,990,000.00 USD | 143.71 USD | 0.00 USD | `+25.74%` | `27.40` |
| `Live` | `Short` | `5.25` | 4,000,000.00 USD | 1,340.00 USD | 0.00 USD | `+25.98%` | `254.90` |
| `Live` | `Short` | `5.26` | 4,090,000.00 USD | 90,330.00 USD | 0.00 USD | `+26.22%` | `17,157.60` |
| `Live` | `Short` | `5.28` | 4,090,000.00 USD | 1,940.00 USD | 0.00 USD | `+26.46%` | `367.00` |
| `Live` | `Short` | `5.29` | 4,090,000.00 USD | 228.84 USD | 0.00 USD | `+26.70%` | `43.30` |
| `Live` | `Short` | `5.30` | 4,090,000.00 USD | 524.66 USD | 0.00 USD | `+27.18%` | `98.90` |
| `Live` | `Short` | `5.32` | 5,200,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+27.42%` | `209,675.30` |
| `Live` | `Short` | `5.33` | 5,230,000.00 USD | 29,310.00 USD | 0.00 USD | `+27.90%` | `5,493.40` |
| `Live` | `Short` | `5.34` | 5,250,000.00 USD | 19,710.00 USD | 0.00 USD | `+28.14%` | `3,686.80` |
| `Live` | `Short` | `5.36` | 5,320,000.00 USD | 65,430.00 USD | 0.00 USD | `+28.38%` | `12,218.10` |
| `Live` | `Short` | `5.37` | 5,320,000.00 USD | 437.78 USD | 0.00 USD | `+28.62%` | `81.60` |
| `Live` | `Short` | `5.38` | 5,320,000.00 USD | 6,050.00 USD | 0.00 USD | `+29.10%` | `1,124.10` |
| `Live` | `Short` | `5.39` | 5,380,000.00 USD | 55,910.00 USD | 0.00 USD | `+29.34%` | `10,364.10` |
| `Live` | `Short` | `5.43` | 5,380,000.00 USD | 962.54 USD | 0.00 USD | `+30.30%` | `177.10` |
| `Live` | `Short` | `5.45` | 5,380,000.00 USD | 1,170.00 USD | 0.00 USD | `+30.54%` | `214.40` |
| `Live` | `Short` | `5.46` | 5,440,000.00 USD | 55,070.00 USD | 0.00 USD | `+30.78%` | `10,094.50` |
| `Live` | `Short` | `5.46` | 5,440,000.00 USD | 1,760.00 USD | 0.00 USD | `+31.02%` | `322.90` |
| `Live` | `Short` | `5.47` | 5,440,000.00 USD | 505.34 USD | 0.00 USD | `+31.26%` | `92.30` |
| `Live` | `Short` | `5.51` | 5,540,000.00 USD | 101,390.00 USD | 0.00 USD | `+32.22%` | `18,384.60` |
| `Live` | `Short` | `5.54` | 5,540,000.00 USD | 209.22 USD | 0.00 USD | `+32.70%` | `37.80` |
| `Live` | `Short` | `5.57` | 5,550,000.00 USD | 8,670.00 USD | 0.00 USD | `+33.41%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 5,610,000.00 USD | 62,420.00 USD | 0.00 USD | `+33.89%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 5,610,000.00 USD | 686.51 USD | 0.00 USD | `+34.13%` | `122.70` |
| `Live` | `Short` | `5.61` | 5,930,000.00 USD | 317,560.00 USD | 0.00 USD | `+34.37%` | `56,657.30` |
| `Live` | `Short` | `5.62` | 5,990,000.00 USD | 62,870.00 USD | 0.00 USD | `+34.61%` | `11,196.20` |
| `Live` | `Short` | `5.64` | 5,990,000.00 USD | 887.39 USD | 0.00 USD | `+35.33%` | `157.20` |
| `Live` | `Short` | `5.66` | 5,990,000.00 USD | 729.50 USD | 0.00 USD | `+35.57%` | `129.00` |
| `Live` | `Short` | `5.67` | 6,000,000.00 USD | 1,070.00 USD | 0.00 USD | `+35.81%` | `189.10` |
| `Live` | `Short` | `5.67` | 6,000,000.00 USD | 1,730.00 USD | 0.00 USD | `+36.05%` | `305.00` |
| `Live` | `Short` | `5.68` | 6,030,000.00 USD | 31,310.00 USD | 0.00 USD | `+36.29%` | `5,508.20` |
| `Live` | `Short` | `5.70` | 6,030,000.00 USD | 4,190.00 USD | 0.00 USD | `+36.53%` | `735.50` |
| `Live` | `Short` | `5.71` | 6,110,000.00 USD | 80,430.00 USD | 0.00 USD | `+36.77%` | `14,097.30` |
| `Live` | `Short` | `5.71` | 6,120,000.00 USD | 2,130.00 USD | 0.00 USD | `+37.01%` | `372.40` |
| `Live` | `Short` | `5.75` | 6,120,000.00 USD | 4,580.00 USD | 0.00 USD | `+37.73%` | `796.90` |
| `Live` | `Short` | `5.75` | 6,120,000.00 USD | 286.02 USD | 0.00 USD | `+37.97%` | `49.70` |
| `Live` | `Short` | `5.79` | 6,160,000.00 USD | 43,610.00 USD | 0.00 USD | `+38.69%` | `7,538.30` |
| `Live` | `Short` | `5.80` | 6,160,000.00 USD | 127.71 USD | 0.00 USD | `+39.17%` | `22.00` |
| `Live` | `Short` | `5.82` | 6,170,000.00 USD | 1,770.00 USD | 0.00 USD | `+39.41%` | `305.00` |
| `Live` | `Short` | `5.83` | 6,170,000.00 USD | 126.04 USD | 0.00 USD | `+39.89%` | `21.60` |
| `Live` | `Short` | `5.84` | 6,170,000.00 USD | 199.31 USD | 0.00 USD | `+40.13%` | `34.10` |
| `Live` | `Short` | `5.86` | 6,170,000.00 USD | 370.62 USD | 0.00 USD | `+40.37%` | `63.30` |
| `Live` | `Short` | `5.87` | 6,220,000.00 USD | 56,160.00 USD | 0.00 USD | `+40.61%` | `9,574.70` |
| `Live` | `Short` | `5.88` | 6,220,000.00 USD | 190.67 USD | 0.00 USD | `+41.09%` | `32.40` |
| `Live` | `Short` | `5.89` | 6,310,000.00 USD | 89,540.00 USD | 0.00 USD | `+41.33%` | `15,189.10` |
| `Live` | `Short` | `5.91` | 6,310,000.00 USD | 2,370.00 USD | 0.00 USD | `+41.57%` | `402.10` |
| `Live` | `Short` | `5.92` | 6,320,000.00 USD | 189.28 USD | 0.00 USD | `+41.81%` | `32.00` |
| `Live` | `Short` | `5.95` | 6,320,000.00 USD | 1,400.00 USD | 0.00 USD | `+42.52%` | `234.80` |
| `Live` | `Short` | `6.00` | 6,320,000.00 USD | 859.68 USD | 0.00 USD | `+43.72%` | `143.40` |
| `Live` | `Short` | `6.00` | 6,590,000.00 USD | 277,620.00 USD | 0.00 USD | `+43.96%` | `46,230.70` |
| `Live` | `Short` | `6.01` | 6,600,000.00 USD | 6,080.00 USD | 0.00 USD | `+44.20%` | `1,010.60` |
| `Live` | `Short` | `6.03` | 6,620,000.00 USD | 23,060.00 USD | 0.00 USD | `+44.44%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 6,620,000.00 USD | 740.54 USD | 0.00 USD | `+45.40%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,630,000.00 USD | 5,920.00 USD | 0.00 USD | `+45.88%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,670,000.00 USD | 37,510.00 USD | 0.00 USD | `+46.12%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 6,680,000.00 USD | 12,520.00 USD | 0.00 USD | `+46.36%` | `2,050.10` |
| `Live` | `Short` | `6.13` | 6,700,000.00 USD | 24,160.00 USD | 0.00 USD | `+47.08%` | `3,938.70` |
| `Live` | `Short` | `6.16` | 6,710,000.00 USD | 307.75 USD | 0.00 USD | `+47.56%` | `50.00` |
| `Live` | `Short` | `6.24` | 6,710,000.00 USD | 1,930.00 USD | 0.00 USD | `+49.48%` | `310.00` |
| `Live` | `Short` | `6.25` | 6,710,000.00 USD | 7,300.00 USD | 0.00 USD | `+49.72%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,710,000.00 USD | 439.10 USD | 0.00 USD | `+49.96%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,720,000.00 USD | 397.84 USD | 0.00 USD | `+50.44%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,800,000.00 USD | 84,720.00 USD | 0.00 USD | `+51.40%` | `13,416.30` |
| `Live` | `Short` | `6.33` | 6,800,000.00 USD | 382.00 USD | 0.00 USD | `+51.87%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,800,000.00 USD | 214.46 USD | 0.00 USD | `+52.11%` | `33.80` |
| `Live` | `Short` | `6.37` | 6,800,000.00 USD | 113.93 USD | 0.00 USD | `+52.59%` | `17.90` |
| `Live` | `Short` | `6.38` | 6,800,000.00 USD | 288.15 USD | 0.00 USD | `+52.83%` | `45.20` |
| `Live` | `Short` | `6.38` | 6,800,000.00 USD | 2,000.00 USD | 0.00 USD | `+53.07%` | `312.80` |
| `Live` | `Short` | `6.41` | 6,810,000.00 USD | 3,780.00 USD | 0.00 USD | `+53.55%` | `590.10` |
| `Live` | `Short` | `6.42` | 6,820,000.00 USD | 8,700.00 USD | 0.00 USD | `+53.79%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,820,000.00 USD | 346.95 USD | 0.00 USD | `+54.03%` | `54.00` |
| `Live` | `Short` | `6.43` | 6,860,000.00 USD | 41,340.00 USD | 0.00 USD | `+54.27%` | `6,424.10` |
| `Live` | `Short` | `6.45` | 6,860,000.00 USD | 5,270.00 USD | 0.00 USD | `+54.51%` | `818.40` |
| `Live` | `Short` | `6.46` | 6,870,000.00 USD | 7,150.00 USD | 0.00 USD | `+54.75%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 6,870,000.00 USD | 1,940.00 USD | 0.00 USD | `+54.99%` | `300.00` |
| `Live` | `Short` | `6.47` | 6,870,000.00 USD | 109.43 USD | 0.00 USD | `+55.23%` | `16.90` |
| `Live` | `Short` | `6.50` | 6,870,000.00 USD | 450.10 USD | 0.00 USD | `+55.71%` | `69.30` |
| `Live` | `Short` | `6.51` | 6,870,000.00 USD | 380.48 USD | 0.00 USD | `+56.19%` | `58.40` |
| `Live` | `Short` | `6.54` | 6,870,000.00 USD | 1,630.00 USD | 0.00 USD | `+56.67%` | `250.00` |
| `Live` | `Short` | `6.54` | 6,870,000.00 USD | 265.07 USD | 0.00 USD | `+56.91%` | `40.50` |
| `Live` | `Short` | `6.58` | 6,930,000.00 USD | 53,480.00 USD | 0.00 USD | `+57.87%` | `8,122.10` |
| `Live` | `Short` | `6.59` | 6,930,000.00 USD | 418.78 USD | 0.00 USD | `+58.11%` | `63.50` |
| `Live` | `Short` | `6.62` | 6,930,000.00 USD | 6,070.00 USD | 0.00 USD | `+58.59%` | `917.00` |
| `Live` | `Short` | `6.63` | 8,860,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+59.07%` | `290,227.90` |
| `Live` | `Short` | `6.66` | 8,870,000.00 USD | 7,230.00 USD | 0.00 USD | `+59.55%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 8,870,000.00 USD | 803.13 USD | 0.00 USD | `+59.79%` | `120.50` |
| `Live` | `Short` | `6.67` | 8,870,000.00 USD | 200.25 USD | 0.00 USD | `+60.03%` | `30.00` |
| `Live` | `Short` | `6.71` | 8,890,000.00 USD | 26,330.00 USD | 0.00 USD | `+60.98%` | `3,921.40` |
| `Live` | `Short` | `6.72` | 9,010,000.00 USD | 115,670.00 USD | 0.00 USD | `+61.22%` | `17,200.00` |
| `Live` | `Short` | `6.75` | 9,400,000.00 USD | 390,790.00 USD | 0.00 USD | `+61.70%` | `57,938.40` |
| `Live` | `Short` | `6.75` | 10,680,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+61.94%` | `189,824.40` |
| `Live` | `Short` | `6.79` | 10,820,000.00 USD | 135,700.00 USD | 0.00 USD | `+62.66%` | `20,000.00` |
| `Live` | `Short` | `6.84` | 10,820,000.00 USD | 753.63 USD | 0.00 USD | `+64.10%` | `110.10` |
| `Live` | `Short` | `6.87` | 10,820,000.00 USD | 2,650.00 USD | 0.00 USD | `+64.58%` | `386.60` |
| `Live` | `Short` | `6.89` | 10,850,000.00 USD | 30,970.00 USD | 0.00 USD | `+65.30%` | `4,491.40` |
| `Live` | `Short` | `6.92` | 10,850,000.00 USD | 733.68 USD | 0.00 USD | `+65.78%` | `106.10` |
| `Live` | `Short` | `6.92` | 10,860,000.00 USD | 8,260.00 USD | 0.00 USD | `+66.02%` | `1,193.30` |
| `Live` | `Short` | `6.93` | 10,900,000.00 USD | 38,320.00 USD | 0.00 USD | `+66.26%` | `5,525.30` |
| `Live` | `Short` | `6.99` | 10,900,000.00 USD | 664.27 USD | 0.00 USD | `+67.46%` | `95.10` |
| `Live` | `Short` | `7.08` | 10,900,000.00 USD | 1,370.00 USD | 0.00 USD | `+69.86%` | `193.30` |
| `Live` | `Short` | `7.09` | 10,900,000.00 USD | 1,770.00 USD | 0.00 USD | `+70.09%` | `250.00` |
| `Live` | `Short` | `7.16` | 10,970,000.00 USD | 63,500.00 USD | 0.00 USD | `+71.53%` | `8,875.40` |
| `Live` | `Short` | `7.20` | 10,990,000.00 USD | 24,120.00 USD | 0.00 USD | `+72.49%` | `3,352.30` |
| `Live` | `Short` | `7.21` | 11,010,000.00 USD | 13,560.00 USD | 0.00 USD | `+72.97%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 11,010,000.00 USD | 4,910.00 USD | 0.00 USD | `+73.45%` | `679.30` |
| `Live` | `Short` | `7.26` | 12,380,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+74.17%` | `188,000.00` |
| `Live` | `Short` | `7.32` | 12,390,000.00 USD | 17,450.00 USD | 0.00 USD | `+75.37%` | `2,385.40` |
| `Live` | `Short` | `7.33` | 12,400,000.00 USD | 1,320.00 USD | 0.00 USD | `+75.85%` | `180.00` |
| `Live` | `Short` | `7.34` | 12,480,000.00 USD | 88,140.00 USD | 0.00 USD | `+76.09%` | `12,000.00` |
| `Live` | `Short` | `7.39` | 12,480,000.00 USD | 1,630.00 USD | 0.00 USD | `+77.29%` | `220.40` |
| `Live` | `Short` | `7.43` | 12,590,000.00 USD | 106,150.00 USD | 0.00 USD | `+78.25%` | `14,276.50` |
| `Live` | `Short` | `7.45` | 12,610,000.00 USD | 14,890.00 USD | 0.00 USD | `+78.49%` | `2,000.00` |
| `Live` | `Short` | `7.46` | 12,610,000.00 USD | 1,420.00 USD | 0.00 USD | `+78.73%` | `191.10` |
| `Live` | `Short` | `7.49` | 22,610,000.00 USD | 10,000,000.00 USD | 0.00 USD | `+79.44%` | `1,336,000.00` |
| `Live` | `Short` | `7.53` | 22,610,000.00 USD | 1,610.00 USD | 0.00 USD | `+80.40%` | `214.00` |
| `Live` | `Short` | `7.54` | 22,630,000.00 USD | 25,590.00 USD | 0.00 USD | `+80.64%` | `3,396.50` |
| `Live` | `Short` | `7.54` | 22,640,000.00 USD | 2,620.00 USD | 0.00 USD | `+80.88%` | `347.20` |
| `Live` | `Short` | `7.63` | 22,660,000.00 USD | 19,210.00 USD | 0.00 USD | `+83.04%` | `2,516.10` |
| `Live` | `Short` | `7.64` | 30,600,000.00 USD | 7,950,000.00 USD | 0.00 USD | `+83.28%` | `1,039,604.60` |
| `Live` | `Short` | `7.67` | 30,600,000.00 USD | 360.25 USD | 0.00 USD | `+83.76%` | `47.00` |
| `Live` | `Short` | `7.67` | 30,620,000.00 USD | 15,000.00 USD | 0.00 USD | `+84.00%` | `1,954.70` |
| `Live` | `Short` | `7.70` | 30,940,000.00 USD | 324,350.00 USD | 0.00 USD | `+84.48%` | `42,151.20` |
| `Live` | `Short` | `7.71` | 30,940,000.00 USD | 655.70 USD | 0.00 USD | `+84.72%` | `85.10` |
| `Live` | `Short` | `7.74` | 31,070,000.00 USD | 126,480.00 USD | 0.00 USD | `+85.44%` | `16,351.90` |
| `Live` | `Short` | `7.75` | 31,070,000.00 USD | 629.67 USD | 0.00 USD | `+85.68%` | `81.30` |
| `Live` | `Short` | `7.78` | 31,110,000.00 USD | 33,500.00 USD | 0.00 USD | `+86.40%` | `4,308.50` |
| `Live` | `Short` | `7.79` | 31,130,000.00 USD | 27,220.00 USD | 0.00 USD | `+86.64%` | `3,496.50` |
| `Live` | `Short` | `7.87` | 31,140,000.00 USD | 2,980.00 USD | 0.00 USD | `+88.55%` | `378.70` |
| `Live` | `Short` | `7.88` | 32,290,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+88.79%` | `146,026.20` |
| `Live` | `Short` | `7.95` | 32,290,000.00 USD | 6,120.00 USD | 0.00 USD | `+90.47%` | `769.80` |
| `Live` | `Short` | `7.96` | 32,430,000.00 USD | 134,240.00 USD | 0.00 USD | `+90.95%` | `16,854.30` |
| `Live` | `Short` | `8.03` | 32,860,000.00 USD | 435,420.00 USD | 0.00 USD | `+92.39%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 32,860,000.00 USD | 797.63 USD | 0.00 USD | `+93.35%` | `98.90` |
| `Live` | `Short` | `8.15` | 32,860,000.00 USD | 362.08 USD | 0.00 USD | `+95.51%` | `44.40` |
| `Live` | `Short` | `8.22` | 32,880,000.00 USD | 21,500.00 USD | 0.00 USD | `+97.19%` | `2,613.60` |
| `Live` | `Short` | `8.29` | 32,880,000.00 USD | 869.32 USD | 0.00 USD | `+98.86%` | `104.80` |
| `Live` | `Short` | `8.34` | 33,310,000.00 USD | 430,340.00 USD | 0.00 USD | `+99.82%` | `51,630.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,050,000.00 USD | 0.00 USD | 585.51 USD | `-75.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,050,000.00 USD | 0.00 USD | 331.54 USD | `-67.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,050,000.00 USD | 0.00 USD | 345.25 USD | `-67.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,050,000.00 USD | 0.00 USD | 5,640.00 USD | `-67.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,040,000.00 USD | 0.00 USD | 997.29 USD | `-66.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,040,000.00 USD | 0.00 USD | 139.83 USD | `-63.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,040,000.00 USD | 0.00 USD | 113.28 USD | `-63.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,040,000.00 USD | 0.00 USD | 4,000.00 USD | `-62.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,040,000.00 USD | 0.00 USD | 324.22 USD | `-62.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,040,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,030,000.00 USD | 0.00 USD | 739.67 USD | `-61.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,030,000.00 USD | 0.00 USD | 1,740.00 USD | `-61.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,030,000.00 USD | 0.00 USD | 6,260.00 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,030,000.00 USD | 0.00 USD | 167.50 USD | `-59.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,030,000.00 USD | 0.00 USD | 669.02 USD | `-59.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,020,000.00 USD | 0.00 USD | 105.88 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,020,000.00 USD | 0.00 USD | 172.50 USD | `-58.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,020,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,010,000.00 USD | 0.00 USD | 722.00 USD | `-56.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,010,000.00 USD | 0.00 USD | 259.00 USD | `-56.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,010,000.00 USD | 0.00 USD | 103.84 USD | `-56.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,010,000.00 USD | 0.00 USD | 109.00 USD | `-56.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,010,000.00 USD | 0.00 USD | 222.19 USD | `-55.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,010,000.00 USD | 0.00 USD | 10,280.00 USD | `-54.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,000,000.00 USD | 0.00 USD | 558.36 USD | `-54.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,000,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,000,000.00 USD | 0.00 USD | 222.14 USD | `-53.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,000,000.00 USD | 0.00 USD | 279.50 USD | `-53.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,000,000.00 USD | 0.00 USD | 197.50 USD | `-52.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,000,000.00 USD | 0.00 USD | 935.66 USD | `-52.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,000,000.00 USD | 0.00 USD | 19,170.00 USD | `-51.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,980,000.00 USD | 0.00 USD | 3,020.00 USD | `-51.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,980,000.00 USD | 0.00 USD | 214.52 USD | `-50.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,980,000.00 USD | 0.00 USD | 1,200.00 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,970,000.00 USD | 0.00 USD | 578.41 USD | `-50.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,970,000.00 USD | 0.00 USD | 18,190.00 USD | `-49.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,960,000.00 USD | 0.00 USD | 13,980.00 USD | `-49.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,940,000.00 USD | 0.00 USD | 107.23 USD | `-49.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,940,000.00 USD | 0.00 USD | 1,590.00 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,940,000.00 USD | 0.00 USD | 6,970.00 USD | `-48.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,930,000.00 USD | 0.00 USD | 310.32 USD | `-48.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,930,000.00 USD | 0.00 USD | 1,170.00 USD | `-48.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,930,000.00 USD | 0.00 USD | 576.18 USD | `-47.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,930,000.00 USD | 0.00 USD | 295.67 USD | `-47.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,930,000.00 USD | 0.00 USD | 2,940.00 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,930,000.00 USD | 0.00 USD | 812.68 USD | `-46.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,930,000.00 USD | 0.00 USD | 1,440.00 USD | `-46.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,930,000.00 USD | 0.00 USD | 490.14 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,930,000.00 USD | 0.00 USD | 6,270.00 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,920,000.00 USD | 0.00 USD | 478.06 USD | `-45.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,920,000.00 USD | 0.00 USD | 540.88 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,920,000.00 USD | 0.00 USD | 1,210.00 USD | `-45.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,920,000.00 USD | 0.00 USD | 759.76 USD | `-45.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,920,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,900,000.00 USD | 0.00 USD | 3,690.00 USD | `-44.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,900,000.00 USD | 0.00 USD | 3,050.00 USD | `-44.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,900,000.00 USD | 0.00 USD | 467.00 USD | `-44.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,900,000.00 USD | 0.00 USD | 506.75 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,900,000.00 USD | 0.00 USD | 214.27 USD | `-43.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,900,000.00 USD | 0.00 USD | 428.69 USD | `-43.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,900,000.00 USD | 0.00 USD | 322.45 USD | `-42.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,900,000.00 USD | 0.00 USD | 108.25 USD | `-42.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,900,000.00 USD | 0.00 USD | 3,850.00 USD | `-42.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,890,000.00 USD | 0.00 USD | 799.04 USD | `-41.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,890,000.00 USD | 0.00 USD | 6,830.00 USD | `-41.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,880,000.00 USD | 0.00 USD | 137.16 USD | `-41.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,880,000.00 USD | 0.00 USD | 504.41 USD | `-40.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,880,000.00 USD | 0.00 USD | 963.93 USD | `-40.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,880,000.00 USD | 0.00 USD | 13,880.00 USD | `-39.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,870,000.00 USD | 0.00 USD | 541.98 USD | `-39.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,870,000.00 USD | 0.00 USD | 108.75 USD | `-39.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,870,000.00 USD | 0.00 USD | 766.55 USD | `-38.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,870,000.00 USD | 0.00 USD | 1,010.00 USD | `-38.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,870,000.00 USD | 0.00 USD | 1,100.00 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,870,000.00 USD | 0.00 USD | 100.04 USD | `-38.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,870,000.00 USD | 0.00 USD | 5,090.00 USD | `-37.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,860,000.00 USD | 0.00 USD | 226.57 USD | `-35.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,860,000.00 USD | 0.00 USD | 104.98 USD | `-35.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,860,000.00 USD | 0.00 USD | 7,160.00 USD | `-35.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,850,000.00 USD | 0.00 USD | 107.21 USD | `-34.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,850,000.00 USD | 0.00 USD | 197.37 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,850,000.00 USD | 0.00 USD | 8,390.00 USD | `-33.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,840,000.00 USD | 0.00 USD | 108.39 USD | `-33.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,840,000.00 USD | 0.00 USD | 1,270.00 USD | `-33.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,840,000.00 USD | 0.00 USD | 217.23 USD | `-33.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,840,000.00 USD | 0.00 USD | 437.98 USD | `-32.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,840,000.00 USD | 0.00 USD | 2,000.00 USD | `-32.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,840,000.00 USD | 0.00 USD | 8,250.00 USD | `-32.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,830,000.00 USD | 0.00 USD | 109.53 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 2,830,000.00 USD | 0.00 USD | 1,810.00 USD | `-31.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,830,000.00 USD | 0.00 USD | 437.00 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,830,000.00 USD | 0.00 USD | 746.06 USD | `-30.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,830,000.00 USD | 0.00 USD | 4,870.00 USD | `-30.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,820,000.00 USD | 0.00 USD | 696.98 USD | `-30.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,820,000.00 USD | 0.00 USD | 358.90 USD | `-29.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,820,000.00 USD | 0.00 USD | 15,370.00 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,810,000.00 USD | 0.00 USD | 523.32 USD | `-28.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,810,000.00 USD | 0.00 USD | 2,330.00 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,800,000.00 USD | 0.00 USD | 15,810.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,790,000.00 USD | 0.00 USD | 1,020.00 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,790,000.00 USD | 0.00 USD | 345.76 USD | `-27.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,790,000.00 USD | 0.00 USD | 214.57 USD | `-27.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,790,000.00 USD | 0.00 USD | 109.42 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 2,790,000.00 USD | 0.00 USD | 721.58 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,790,000.00 USD | 0.00 USD | 9,300.00 USD | `-25.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,780,000.00 USD | 0.00 USD | 8,530.00 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,770,000.00 USD | 0.00 USD | 104.69 USD | `-25.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,770,000.00 USD | 0.00 USD | 315.69 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,770,000.00 USD | 0.00 USD | 214.17 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,770,000.00 USD | 0.00 USD | 641.10 USD | `-24.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,770,000.00 USD | 0.00 USD | 212.06 USD | `-24.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,770,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,770,000.00 USD | 0.00 USD | 218.81 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,770,000.00 USD | 0.00 USD | 25,410.00 USD | `-23.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,740,000.00 USD | 0.00 USD | 144.67 USD | `-22.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,740,000.00 USD | 0.00 USD | 2,170.00 USD | `-21.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,740,000.00 USD | 0.00 USD | 104.81 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,740,000.00 USD | 0.00 USD | 1,150.00 USD | `-21.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,740,000.00 USD | 0.00 USD | 1,070.00 USD | `-21.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,740,000.00 USD | 0.00 USD | 15,820.00 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,720,000.00 USD | 0.00 USD | 240.67 USD | `-20.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,720,000.00 USD | 0.00 USD | 465.50 USD | `-20.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,720,000.00 USD | 0.00 USD | 1,670.00 USD | `-20.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,720,000.00 USD | 0.00 USD | 505.76 USD | `-19.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,720,000.00 USD | 0.00 USD | 73,220.00 USD | `-19.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,640,000.00 USD | 0.00 USD | 12,850.00 USD | `-19.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,630,000.00 USD | 0.00 USD | 8,490.00 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,620,000.00 USD | 0.00 USD | 208,010.00 USD | `-18.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,410,000.00 USD | 0.00 USD | 28,130.00 USD | `-18.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,390,000.00 USD | 0.00 USD | 506.22 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,390,000.00 USD | 0.00 USD | 171.75 USD | `-17.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,390,000.00 USD | 0.00 USD | 2,550.00 USD | `-17.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,380,000.00 USD | 0.00 USD | 2,710.00 USD | `-17.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,380,000.00 USD | 0.00 USD | 344.07 USD | `-16.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,380,000.00 USD | 0.00 USD | 1,950.00 USD | `-16.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,380,000.00 USD | 0.00 USD | 123,320.00 USD | `-15.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,250,000.00 USD | 0.00 USD | 17,360.00 USD | `-15.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,240,000.00 USD | 0.00 USD | 2,030.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,240,000.00 USD | 0.00 USD | 5,000.00 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,230,000.00 USD | 0.00 USD | 633.50 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,230,000.00 USD | 0.00 USD | 333.68 USD | `-14.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,230,000.00 USD | 0.00 USD | 72,860.00 USD | `-14.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,160,000.00 USD | 0.00 USD | 179.25 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,160,000.00 USD | 0.00 USD | 643.50 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,160,000.00 USD | 0.00 USD | 4,370.00 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,150,000.00 USD | 0.00 USD | 632.99 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,150,000.00 USD | 0.00 USD | 172.19 USD | `-13.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,150,000.00 USD | 0.00 USD | 14,000.00 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,140,000.00 USD | 0.00 USD | 179.33 USD | `-12.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,140,000.00 USD | 0.00 USD | 3,900.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,130,000.00 USD | 0.00 USD | 174.09 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,130,000.00 USD | 0.00 USD | 367.50 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,130,000.00 USD | 0.00 USD | 4,490.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,130,000.00 USD | 0.00 USD | 4,370.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,120,000.00 USD | 0.00 USD | 18,110.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,110,000.00 USD | 0.00 USD | 2,620.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,100,000.00 USD | 0.00 USD | 1,030.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,100,000.00 USD | 0.00 USD | 45,640.00 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,060,000.00 USD | 0.00 USD | 28,820.00 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,030,000.00 USD | 0.00 USD | 114,290.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,910,000.00 USD | 0.00 USD | 7,500.00 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,910,000.00 USD | 0.00 USD | 3,940.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,900,000.00 USD | 0.00 USD | 359.57 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,900,000.00 USD | 0.00 USD | 1,900.00 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,900,000.00 USD | 0.00 USD | 1,560.00 USD | `-8.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,900,000.00 USD | 0.00 USD | 18,070.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,880,000.00 USD | 0.00 USD | 24,620.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,850,000.00 USD | 0.00 USD | 2,990.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,850,000.00 USD | 0.00 USD | 2,100.00 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,850,000.00 USD | 0.00 USD | 3,990.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,850,000.00 USD | 0.00 USD | 2,640.00 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,840,000.00 USD | 0.00 USD | 14,700.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,830,000.00 USD | 0.00 USD | 6,260.00 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,820,000.00 USD | 0.00 USD | 16,050.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,810,000.00 USD | 0.00 USD | 30,060.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,780,000.00 USD | 0.00 USD | 1,060.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,770,000.00 USD | 0.00 USD | 1,690.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,770,000.00 USD | 0.00 USD | 1,420.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,770,000.00 USD | 0.00 USD | 1,060.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,770,000.00 USD | 0.00 USD | 16,710.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,750,000.00 USD | 0.00 USD | 1,960.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,750,000.00 USD | 0.00 USD | 5,680.00 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,750,000.00 USD | 0.00 USD | 99,370.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,650,000.00 USD | 0.00 USD | 14,550.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,630,000.00 USD | 0.00 USD | 194,890.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 1,440,000.00 USD | 0.00 USD | 5,440.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 1,430,000.00 USD | 0.00 USD | 4,400.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,430,000.00 USD | 0.00 USD | 3,040.00 USD | `-3.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,420,000.00 USD | 0.00 USD | 6,720.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 1,420,000.00 USD | 0.00 USD | 360,700.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 1,060,000.00 USD | 0.00 USD | 485.36 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,060,000.00 USD | 0.00 USD | 26,510.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,030,000.00 USD | 0.00 USD | 192,000.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 838,270.00 USD | 0.00 USD | 42,690.00 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 795,580.00 USD | 0.00 USD | 718,270.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 77,300.00 USD | 0.00 USD | 2,080.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 75,220.00 USD | 0.00 USD | 3,350.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 71,880.00 USD | 0.00 USD | 30,470.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 41,410.00 USD | 0.00 USD | 1,910.00 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 39,490.00 USD | 0.00 USD | 36,660.00 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 2,830.00 USD | 0.00 USD | 2,830.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 31,360.00 USD | 31,360.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 57,050.00 USD | 25,690.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 91,260.00 USD | 34,210.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 91,360.00 USD | 100.08 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 142,650.00 USD | 51,290.00 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 143,000.00 USD | 351.94 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 190,950.00 USD | 47,940.00 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 194,640.00 USD | 3,700.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 195,310.00 USD | 668.89 USD | 0.00 USD | `+2.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 199,580.00 USD | 4,270.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 222,270.00 USD | 22,700.00 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 223,420.00 USD | 1,150.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 225,300.00 USD | 1,880.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 255,280.00 USD | 29,980.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 653,180.00 USD | 397,900.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 655,600.00 USD | 2,420.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 656,110.00 USD | 509.80 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 658,540.00 USD | 2,430.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 659,400.00 USD | 860.11 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 665,600.00 USD | 6,200.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 690,950.00 USD | 25,350.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 701,730.00 USD | 10,780.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 701,990.00 USD | 261.50 USD | 0.00 USD | `+5.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 765,080.00 USD | 63,090.00 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 766,480.00 USD | 1,400.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 768,000.00 USD | 1,520.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 768,430.00 USD | 428.86 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 769,320.00 USD | 889.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 770,480.00 USD | 1,170.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 776,790.00 USD | 6,300.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 776,940.00 USD | 151.70 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 821,790.00 USD | 44,850.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 832,640.00 USD | 10,850.00 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 848,340.00 USD | 15,700.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 861,440.00 USD | 13,100.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 912,100.00 USD | 50,660.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,030,000.00 USD | 121,950.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,040,000.00 USD | 1,610.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,050,000.00 USD | 15,770.00 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,050,000.00 USD | 702.55 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,100,000.00 USD | 45,750.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,100,000.00 USD | 1,150.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,120,000.00 USD | 18,440.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,150,000.00 USD | 29,400.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,160,000.00 USD | 10,970.00 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,160,000.00 USD | 255.30 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,200,000.00 USD | 43,960.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,200,000.00 USD | 750.17 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,220,000.00 USD | 21,240.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,240,000.00 USD | 11,660.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,240,000.00 USD | 104.25 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,240,000.00 USD | 7,930.00 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,240,000.00 USD | 152.12 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,810,000.00 USD | 570,840.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,030,000.00 USD | 217,980.00 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,040,000.00 USD | 2,650.00 USD | 0.00 USD | `+13.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,140,000.00 USD | 105,630.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,150,000.00 USD | 6,160.00 USD | 0.00 USD | `+13.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,170,000.00 USD | 27,130.00 USD | 0.00 USD | `+14.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,190,000.00 USD | 13,030.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,200,000.00 USD | 15,480.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,070,000.00 USD | 869,380.00 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,070,000.00 USD | 559.58 USD | 0.00 USD | `+14.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,250,000.00 USD | 173,550.00 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,250,000.00 USD | 6,530.00 USD | 0.00 USD | `+15.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,270,000.00 USD | 13,730.00 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,270,000.00 USD | 1,080.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,280,000.00 USD | 11,760.00 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,300,000.00 USD | 24,490.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,330,000.00 USD | 22,380.00 USD | 0.00 USD | `+16.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,340,000.00 USD | 10,610.00 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,350,000.00 USD | 9,690.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,350,000.00 USD | 4,060.00 USD | 0.00 USD | `+17.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,470,000.00 USD | 120,040.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,470,000.00 USD | 287.53 USD | 0.00 USD | `+17.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,480,000.00 USD | 13,180.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,490,000.00 USD | 8,600.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,490,000.00 USD | 313.51 USD | 0.00 USD | `+18.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,500,000.00 USD | 5,070.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,550,000.00 USD | 47,350.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,550,000.00 USD | 187.06 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,640,000.00 USD | 95,210.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,650,000.00 USD | 11,390.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,690,000.00 USD | 38,240.00 USD | 0.00 USD | `+19.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,720,000.00 USD | 25,080.00 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,720,000.00 USD | 5,030.00 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,890,000.00 USD | 172,540.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,890,000.00 USD | 104.94 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,940,000.00 USD | 51,080.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,950,000.00 USD | 4,730.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,040,000.00 USD | 87,490.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,920,000.00 USD | 882,870.00 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,920,000.00 USD | 547.20 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,970,000.00 USD | 51,790.00 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,990,000.00 USD | 15,350.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,990,000.00 USD | 113.26 USD | 0.00 USD | `+22.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 5,000,000.00 USD | 15,400.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 5,010,000.00 USD | 3,670.00 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 5,010,000.00 USD | 3,770.00 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,010,000.00 USD | 575.38 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,010,000.00 USD | 327.58 USD | 0.00 USD | `+24.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 5,010,000.00 USD | 163.85 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 5,130,000.00 USD | 120,080.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,160,000.00 USD | 33,260.00 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,170,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 5,290,000.00 USD | 120,450.00 USD | 0.00 USD | `+25.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 5,290,000.00 USD | 2,620.00 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,290,000.00 USD | 537.61 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,740,000.00 USD | 449,510.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,740,000.00 USD | 5,540.00 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,750,000.00 USD | 589.22 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,750,000.00 USD | 733.03 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,750,000.00 USD | 423.60 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,760,000.00 USD | 10,930.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,760,000.00 USD | 381.09 USD | 0.00 USD | `+27.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,760,000.00 USD | 961.16 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,760,000.00 USD | 1,570.00 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,770,000.00 USD | 6,220.00 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,770,000.00 USD | 1,170.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,770,000.00 USD | 225.33 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,770,000.00 USD | 438.60 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,770,000.00 USD | 5,000.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,810,000.00 USD | 41,030.00 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,940,000.00 USD | 127,430.00 USD | 0.00 USD | `+29.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,940,000.00 USD | 604.86 USD | 0.00 USD | `+29.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,940,000.00 USD | 2,370.00 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,960,000.00 USD | 12,920.00 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,970,000.00 USD | 12,220.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,190,000.00 USD | 219,220.00 USD | 0.00 USD | `+31.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,220,000.00 USD | 35,450.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,270,000.00 USD | 44,780.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,270,000.00 USD | 1,180.00 USD | 0.00 USD | `+31.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,370,000.00 USD | 95,100.00 USD | 0.00 USD | `+31.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,370,000.00 USD | 5,600.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,420,000.00 USD | 45,680.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,440,000.00 USD | 18,790.00 USD | 0.00 USD | `+32.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,510,000.00 USD | 74,260.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,560,000.00 USD | 49,440.00 USD | 0.00 USD | `+33.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,570,000.00 USD | 14,320.00 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,580,000.00 USD | 5,560.00 USD | 0.00 USD | `+33.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,600,000.00 USD | 20,540.00 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,600,000.00 USD | 384.94 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,600,000.00 USD | 4,170.00 USD | 0.00 USD | `+34.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,610,000.00 USD | 2,190.00 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,610,000.00 USD | 581.53 USD | 0.00 USD | `+35.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,610,000.00 USD | 295.23 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,610,000.00 USD | 3,290.00 USD | 0.00 USD | `+35.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,610,000.00 USD | 281.55 USD | 0.00 USD | `+35.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,620,000.00 USD | 6,590.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,620,000.00 USD | 5,860.00 USD | 0.00 USD | `+36.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,740,000.00 USD | 116,610.00 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,740,000.00 USD | 2,210.00 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,750,000.00 USD | 5,720.00 USD | 0.00 USD | `+37.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,770,000.00 USD | 24,820.00 USD | 0.00 USD | `+37.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,780,000.00 USD | 2,430.00 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,780,000.00 USD | 286.94 USD | 0.00 USD | `+38.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,780,000.00 USD | 7,120.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,780,000.00 USD | 329.13 USD | 0.00 USD | `+39.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,790,000.00 USD | 1,970.00 USD | 0.00 USD | `+39.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,790,000.00 USD | 1,120.00 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,790,000.00 USD | 1,150.00 USD | 0.00 USD | `+40.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,790,000.00 USD | 1,190.00 USD | 0.00 USD | `+40.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,790,000.00 USD | 3,450.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,790,000.00 USD | 345.45 USD | 0.00 USD | `+41.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,850,000.00 USD | 55,870.00 USD | 0.00 USD | `+41.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,850,000.00 USD | 1,670.00 USD | 0.00 USD | `+41.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,850,000.00 USD | 1,400.00 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,990,000.00 USD | 136,500.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,020,000.00 USD | 32,530.00 USD | 0.00 USD | `+42.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,030,000.00 USD | 5,440.00 USD | 0.00 USD | `+43.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,030,000.00 USD | 8,940.00 USD | 0.00 USD | `+43.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,150,000.00 USD | 119,340.00 USD | 0.00 USD | `+43.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,160,000.00 USD | 3,000.00 USD | 0.00 USD | `+43.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,280,000.00 USD | 118,630.00 USD | 0.00 USD | `+43.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,290,000.00 USD | 13,610.00 USD | 0.00 USD | `+44.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,380,000.00 USD | 90,380.00 USD | 0.00 USD | `+44.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,380,000.00 USD | 2,120.00 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,390,000.00 USD | 3,300.00 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,390,000.00 USD | 2,550.00 USD | 0.00 USD | `+45.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,390,000.00 USD | 425.76 USD | 0.00 USD | `+45.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,390,000.00 USD | 2,030.00 USD | 0.00 USD | `+45.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,390,000.00 USD | 4,120.00 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,400,000.00 USD | 2,000.00 USD | 0.00 USD | `+46.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,460,000.00 USD | 61,050.00 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,460,000.00 USD | 1,610.00 USD | 0.00 USD | `+46.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,460,000.00 USD | 1,200.00 USD | 0.00 USD | `+47.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,470,000.00 USD | 11,620.00 USD | 0.00 USD | `+47.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,470,000.00 USD | 1,940.00 USD | 0.00 USD | `+47.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,470,000.00 USD | 1,410.00 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,480,000.00 USD | 4,010.00 USD | 0.00 USD | `+48.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,480,000.00 USD | 3,960.00 USD | 0.00 USD | `+48.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,490,000.00 USD | 3,830.00 USD | 0.00 USD | `+48.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,550,000.00 USD | 66,120.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,550,000.00 USD | 1,890.00 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,550,000.00 USD | 195.46 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,560,000.00 USD | 7,480.00 USD | 0.00 USD | `+49.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,570,000.00 USD | 3,670.00 USD | 0.00 USD | `+50.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,570,000.00 USD | 3,680.00 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,580,000.00 USD | 7,370.00 USD | 0.00 USD | `+51.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,580,000.00 USD | 412.37 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,580,000.00 USD | 602.77 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,580,000.00 USD | 449.79 USD | 0.00 USD | `+51.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,580,000.00 USD | 1,760.00 USD | 0.00 USD | `+52.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,580,000.00 USD | 3,560.00 USD | 0.00 USD | `+52.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,590,000.00 USD | 3,230.00 USD | 0.00 USD | `+53.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,590,000.00 USD | 5,120.00 USD | 0.00 USD | `+53.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,590,000.00 USD | 613.26 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,590,000.00 USD | 1,310.00 USD | 0.00 USD | `+55.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,630,000.00 USD | 31,270.00 USD | 0.00 USD | `+55.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,630,000.00 USD | 234.54 USD | 0.00 USD | `+56.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,640,000.00 USD | 14,070.00 USD | 0.00 USD | `+56.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,640,000.00 USD | 1,630.00 USD | 0.00 USD | `+57.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,640,000.00 USD | 2,390.00 USD | 0.00 USD | `+58.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,650,000.00 USD | 1,620.00 USD | 0.00 USD | `+58.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,650,000.00 USD | 3,220.00 USD | 0.00 USD | `+59.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 7,650,000.00 USD | 1,950.00 USD | 0.00 USD | `+59.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,650,000.00 USD | 450.55 USD | 0.00 USD | `+59.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,650,000.00 USD | 3,060.00 USD | 0.00 USD | `+60.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,660,000.00 USD | 1,930.00 USD | 0.00 USD | `+60.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,660,000.00 USD | 3,070.00 USD | 0.00 USD | `+60.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,660,000.00 USD | 1,920.00 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,660,000.00 USD | 3,120.00 USD | 0.00 USD | `+61.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,670,000.00 USD | 1,550.00 USD | 0.00 USD | `+61.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,670,000.00 USD | 3,080.00 USD | 0.00 USD | `+62.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,670,000.00 USD | 647.56 USD | 0.00 USD | `+62.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,670,000.00 USD | 1,420.00 USD | 0.00 USD | `+63.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,670,000.00 USD | 2,130.00 USD | 0.00 USD | `+63.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,680,000.00 USD | 3,140.00 USD | 0.00 USD | `+63.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,680,000.00 USD | 342.25 USD | 0.00 USD | `+64.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,680,000.00 USD | 1,830.00 USD | 0.00 USD | `+64.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,680,000.00 USD | 2,990.00 USD | 0.00 USD | `+64.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,680,000.00 USD | 2,970.00 USD | 0.00 USD | `+65.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,680,000.00 USD | 324.54 USD | 0.00 USD | `+65.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,690,000.00 USD | 504.21 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,690,000.00 USD | 166.00 USD | 0.00 USD | `+67.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,690,000.00 USD | 4,190.00 USD | 0.00 USD | `+67.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,710,000.00 USD | 15,610.00 USD | 0.00 USD | `+67.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,710,000.00 USD | 1,750.00 USD | 0.00 USD | `+68.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,710,000.00 USD | 2,860.00 USD | 0.00 USD | `+68.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,710,000.00 USD | 264.31 USD | 0.00 USD | `+70.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,710,000.00 USD | 599.34 USD | 0.00 USD | `+71.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,710,000.00 USD | 193.19 USD | 0.00 USD | `+71.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,710,000.00 USD | 3,950.00 USD | 0.00 USD | `+72.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,720,000.00 USD | 1,940.00 USD | 0.00 USD | `+72.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,880,000.00 USD | 160,550.00 USD | 0.00 USD | `+73.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,880,000.00 USD | 1,290.00 USD | 0.00 USD | `+74.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,880,000.00 USD | 905.60 USD | 0.00 USD | `+75.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,880,000.00 USD | 1,730.00 USD | 0.00 USD | `+75.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,880,000.00 USD | 1,710.00 USD | 0.00 USD | `+76.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,890,000.00 USD | 7,870.00 USD | 0.00 USD | `+77.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,890,000.00 USD | 630.05 USD | 0.00 USD | `+77.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,890,000.00 USD | 2,610.00 USD | 0.00 USD | `+77.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,900,000.00 USD | 6,000.00 USD | 0.00 USD | `+79.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,900,000.00 USD | 1,620.00 USD | 0.00 USD | `+80.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,910,000.00 USD | 4,640.00 USD | 0.00 USD | `+81.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,910,000.00 USD | 371.88 USD | 0.00 USD | `+82.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,910,000.00 USD | 2,510.00 USD | 0.00 USD | `+82.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,910,000.00 USD | 380.68 USD | 0.00 USD | `+84.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,910,000.00 USD | 133.12 USD | 0.00 USD | `+84.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,910,000.00 USD | 1,490.00 USD | 0.00 USD | `+86.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,910,000.00 USD | 1,470.00 USD | 0.00 USD | `+86.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,920,000.00 USD | 11,170.00 USD | 0.00 USD | `+86.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,960,000.00 USD | 34,360.00 USD | 0.00 USD | `+87.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,960,000.00 USD | 399.35 USD | 0.00 USD | `+87.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,960,000.00 USD | 100.29 USD | 0.00 USD | `+87.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 7,960,000.00 USD | 1,550.00 USD | 0.00 USD | `+88.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,970,000.00 USD | 10,610.00 USD | 0.00 USD | `+90.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,970,000.00 USD | 309.43 USD | 0.00 USD | `+91.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 8,030,000.00 USD | 56,170.00 USD | 0.00 USD | `+91.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,110,000.00 USD | 81,310.00 USD | 0.00 USD | `+92.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,110,000.00 USD | 1,390.00 USD | 0.00 USD | `+94.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,110,000.00 USD | 216.90 USD | 0.00 USD | `+96.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,110,000.00 USD | 738.45 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 8,110,000.00 USD | 1,350.00 USD | 0.00 USD | `+99.58%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.64` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 57,840.00 USD | 22,500.00 USD | 121,880.00 USD |
| `7D` | `3.65` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD |
| `1D` | `3.67` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 16,740.00 USD | 3,070.00 USD | 11,810.00 USD |
| `7D` | `3.67` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD |
| `1D` | `3.69` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 9.86 USD |
| `7D` | `3.69` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `1D` | `3.70` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 17,670.00 USD | 0.00 USD | 17,970.00 USD |
| `7D` | `3.70` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD |
| `7D` | `3.71` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 50,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.72` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 186.40 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,130.00 USD |
| `7D` | `3.73` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 15,960.00 USD | 7,860.00 USD |
| `7D` | `3.74` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 20,660.00 USD | 12,370.00 USD | 64,720.00 USD |
| `1D` | `3.75` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD |
| `1D` | `3.76` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD |
| `7D` | `3.77` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 7,570.00 USD | 9,280.00 USD | 29,190.00 USD |
| `7D` | `3.78` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 225.52 USD | 3,860.00 USD | 9,110.00 USD |
| `7D` | `3.79` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD |
| `1D` | `3.80` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 3,170.00 USD | 0.00 USD | 3,610.00 USD |
| `7D` | `3.80` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 582.53 USD | 0.00 USD | 16,970.00 USD |
| `1D` | `3.81` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 53,440.00 USD | 0.00 USD | 11,530.00 USD |
| `1D` | `3.82` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 176.51 USD |
| `7D` | `3.82` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 527.85 USD | 0.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 352.15 USD | 0.00 USD | 16,870.00 USD |
| `7D` | `3.83` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `1D` | `3.85` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 138.23 USD | 6,330.00 USD | 141.64 USD |
| `1D` | `3.86` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 1,450.00 USD | 12,320.00 USD | 53,950.00 USD |
| `7D` | `3.86` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 0.00 USD | 11,800.00 USD | 0.00 USD |
| `7D` | `3.87` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 54,800.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 105,540.00 USD | 6,860.00 USD | 41,580.00 USD |
| `7D` | `3.88` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 112,190.00 USD | 37,150.00 USD | 21,950.00 USD |
| `7D` | `3.89` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD |
| `1D` | `3.90` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD |
| `7D` | `3.90` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD |
| `1D` | `3.91` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 35,760.00 USD | 38,020.00 USD |
| `7D` | `3.91` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 145,280.00 USD | 26,030.00 USD | 31,900.00 USD |
| `7D` | `3.92` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 90,780.00 USD | 41,330.00 USD | 81,820.00 USD |
| `1D` | `3.93` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 21,500.00 USD | 11,960.00 USD |
| `7D` | `3.93` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 51,660.00 USD | 20,780.00 USD | 50,110.00 USD |
| `1D` | `3.94` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 576.76 USD | 6,420.00 USD | 16,990.00 USD |
| `7D` | `3.94` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 75,150.00 USD | 31,050.00 USD | 126,320.00 USD |
| `1D` | `3.95` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 12,850.00 USD | 5,610.00 USD | 2,150.00 USD |
| `7D` | `3.95` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 8,490.00 USD | 19,870.00 USD | 696.53 USD |
| `1D` | `3.96` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 35,990.00 USD | 29,270.00 USD | 35,080.00 USD |
| `7D` | `3.96` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,470.00 USD |
| `1D` | `3.97` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 156,730.00 USD | 52,430.00 USD | 65,880.00 USD |
| `7D` | `3.97` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,380.00 USD |
| `1D` | `3.98` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 46,870.00 USD | 30,290.00 USD | 14,820.00 USD |
| `7D` | `3.98` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 30,630.00 USD | 77,970.00 USD | 85,840.00 USD |
| `1D` | `3.99` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 94,130.00 USD | 45,940.00 USD | 49,790.00 USD |
| `7D` | `3.99` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 35,730.00 USD | 21,130.00 USD | 95,030.00 USD |
| `7D` | `4.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 317,210.00 USD | 98,320.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 109,930.00 USD | 56,050.00 USD | 73,690.00 USD |
| `7D` | `4.01` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 386,400.00 USD | 94,720.00 USD | 436,220.00 USD |
| `1D` | `4.02` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 60,540.00 USD | 33,270.00 USD | 105,290.00 USD |
| `7D` | `4.02` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 279,800.00 USD | 88,330.00 USD | 248,240.00 USD |
| `1D` | `4.03` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 23,550.00 USD | 55,650.00 USD | 82,060.00 USD |
| `7D` | `4.03` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD |
| `1D` | `4.04` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 29,430.00 USD | 32,610.00 USD | 127,520.00 USD |
| `7D` | `4.04` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,210.00 USD |
| `1D` | `4.05` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 78,330.00 USD | 8,520.00 USD | 14,170.00 USD |
| `7D` | `4.05` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,640.00 USD |
| `1D` | `4.06` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 190,260.00 USD | 0.00 USD | 51,860.00 USD |
| `7D` | `4.06` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 198,550.00 USD | 45,470.00 USD | 124,020.00 USD |
| `1D` | `4.07` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 3,630.00 USD | 15,020.00 USD | 22,900.00 USD |
| `7D` | `4.07` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 183,890.00 USD | 35,750.00 USD | 40,370.00 USD |
| `1D` | `4.08` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 4,280.00 USD | 85,320.00 USD | 15,970.00 USD |
| `7D` | `4.08` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `1D` | `4.09` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 10,540.00 USD | 34,570.00 USD | 194,190.00 USD |
| `7D` | `4.09` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 134,630.00 USD | 26,560.00 USD | 40,790.00 USD |
| `1D` | `4.10` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 33,810.00 USD | 10,080.00 USD | 59,350.00 USD |
| `7D` | `4.10` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD |
| `1D` | `4.11` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 22,930.00 USD | 59,250.00 USD | 73,200.00 USD |
| `7D` | `4.11` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 110,780.00 USD | 0.00 USD | 190,950.00 USD |
| `1D` | `4.12` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 4,430.00 USD | 80,980.00 USD | 228,820.00 USD |
| `7D` | `4.12` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 97,300.00 USD | 0.00 USD | 341,440.00 USD |
| `1D` | `4.13` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 39,650.00 USD | 55,060.00 USD | 38,380.00 USD |
| `7D` | `4.13` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 363,830.00 USD | 0.00 USD | 106,790.00 USD |
| `1D` | `4.14` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 272,540.00 USD | 53,970.00 USD | 166,640.00 USD |
| `7D` | `4.14` | 592,140.00 USD | 0.00 USD | 592,140.00 USD | 374,290.00 USD | 0.00 USD | 217,840.00 USD |
| `1D` | `4.15` | 672,440.00 USD | 0.00 USD | 672,440.00 USD | 564,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 514,600.00 USD | 514,600.00 USD | 0.00 USD | 254,890.00 USD | 0.00 USD | 259,700.00 USD |
| `7D` | `4.15` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 254,890.00 USD | 0.00 USD | 259,700.00 USD |
| `1D` | `4.16` | 107,680.00 USD | 0.00 USD | 107,680.00 USD | 63,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.16` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 509,640.00 USD | 0.00 USD | 171,380.00 USD |
| `1D` | `4.17` | 44,430.00 USD | 0.00 USD | 44,430.00 USD | 44,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.17` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 202,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.18` | 197,650.00 USD | 197,650.00 USD | 0.00 USD | 197,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.18` | 395,310.00 USD | 395,310.00 USD | 0.00 USD | 197,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.18` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 360,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.19` | 683,590.00 USD | 683,590.00 USD | 0.00 USD | 288,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.19` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 215,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.20` | 738,980.00 USD | 738,980.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.20` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 337,660.00 USD | 122,960.00 USD | 0.00 USD |
| `1D` | `4.21` | 802,520.00 USD | 802,520.00 USD | 0.00 USD | 63,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.21` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 462,060.00 USD | 149,940.00 USD | 0.00 USD |
| `1D` | `4.22` | 977,550.00 USD | 977,550.00 USD | 0.00 USD | 0.00 USD | 175,040.00 USD | 0.00 USD |
| `7D` | `4.22` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 853,600.00 USD | 161,970.00 USD | 783,110.00 USD |
| `1D` | `4.23` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 440,840.00 USD | 0.00 USD |
| `7D` | `4.23` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 1,170,000.00 USD | 633,870.00 USD | 736,840.00 USD |
| `1D` | `4.24` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 268,340.00 USD | 0.00 USD |
| `7D` | `4.24` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 1,060,000.00 USD | 611,180.00 USD | 563,980.00 USD |
| `1D` | `4.25` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 323,700.00 USD | 150,500.00 USD |
| `7D` | `4.25` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 506,030.00 USD | 433,770.00 USD | 647,490.00 USD |
| `1D` | `4.26` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 171,790.00 USD | 0.00 USD |
| `7D` | `4.26` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,660,000.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 594,570.00 USD | 24,620.00 USD | 59,600.00 USD |
| `7D` | `4.27` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 750,150.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 313,130.00 USD | 30,410.00 USD | 308,720.00 USD |
| `7D` | `4.28` | 18,240,000.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `7D` | `4.29` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 3,320.00 USD | 0.00 USD | 53.99 USD |
| `7D` | `4.30` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 90,090.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 270,390.00 USD | 0.00 USD | 57,740.00 USD |
| `7D` | `4.31` | 18,500,000.00 USD | 18,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42,810.00 USD |
| `1D` | `4.32` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 611.20 USD | 0.00 USD | 19.74 USD |
| `7D` | `4.32` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,540.00 USD |
| `1D` | `4.33` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 1,990.00 USD | 33,630.00 USD | 301.03 USD |
| `7D` | `4.33` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 269,670.00 USD | 13,800.00 USD | 75,330.00 USD |
| `7D` | `4.34` | 18,830,000.00 USD | 18,830,000.00 USD | 0.00 USD | 4,550.00 USD | 0.00 USD | 134,560.00 USD |
| `1D` | `4.35` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,370.00 USD |
| `7D` | `4.35` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 82,150.00 USD | 12,310.00 USD | 29,780.00 USD |
| `7D` | `4.36` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 5,210.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 52,120.00 USD | 46,860.00 USD | 131,580.00 USD |
| `1D` | `4.38` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 171,480.00 USD | 18,150.00 USD | 476,590.00 USD |
| `7D` | `4.38` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 229,170.00 USD |
| `7D` | `4.39` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 141,060.00 USD | 62,850.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD |
| `7D` | `4.40` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD |
| `1D` | `4.41` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 193,630.00 USD | 83,080.00 USD | 63,590.00 USD |
| `7D` | `4.41` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 272,500.00 USD |
| `1D` | `4.42` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 537.46 USD |
| `7D` | `4.42` | 21,150,000.00 USD | 21,150,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 769.40 USD | 49,400.00 USD | 94,480.00 USD |
| `7D` | `4.43` | 21,420,000.00 USD | 21,420,000.00 USD | 0.00 USD | 155,560.00 USD | 46,230.00 USD | 69,230.00 USD |
| `1D` | `4.44` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 289,290.00 USD |
| `7D` | `4.44` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 70,120.00 USD |
| `1D` | `4.45` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 50,720.00 USD | 359.05 USD |
| `1D` | `4.46` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD |
| `7D` | `4.46` | 21,670,000.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD |
| `1D` | `4.47` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 16,700.00 USD | 18,240.00 USD |
| `7D` | `4.47` | 22,010,000.00 USD | 22,010,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 115,670.00 USD | 73,240.00 USD | 25,450.00 USD |
| `7D` | `4.48` | 22,010,000.00 USD | 22,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 252,980.00 USD | 155,000.00 USD | 150,370.00 USD |
| `7D` | `4.49` | 22,350,000.00 USD | 22,350,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 359,570.00 USD | 65,710.00 USD | 117,840.00 USD |
| `7D` | `4.50` | 22,920,000.00 USD | 22,920,000.00 USD | 0.00 USD | 368,940.00 USD | 200,700.00 USD | 0.00 USD |
| `1D` | `4.51` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 162,900.00 USD | 307,580.00 USD | 309,910.00 USD |
| `7D` | `4.51` | 23,000,000.00 USD | 23,000,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.52` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 266,310.00 USD | 88,150.00 USD | 205,900.00 USD |
| `7D` | `4.52` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 278,740.00 USD |
| `7D` | `4.53` | 24,040,000.00 USD | 24,040,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD |
| `1D` | `4.54` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 150,600.00 USD | 598,910.00 USD |
| `7D` | `4.54` | 25,280,000.00 USD | 25,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 239,970.00 USD |
| `1D` | `4.56` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 25,770,000.00 USD | 25,770,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 155,250.00 USD | 70,180.00 USD | 67,410.00 USD |
| `7D` | `4.57` | 26,120,000.00 USD | 26,120,000.00 USD | 0.00 USD | 198,050.00 USD | 0.00 USD | 151,550.00 USD |
| `1D` | `4.58` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 434,730.00 USD | 56,540.00 USD | 841,400.00 USD |
| `7D` | `4.58` | 26,250,000.00 USD | 26,250,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD |
| `7D` | `4.59` | 27,840,000.00 USD | 27,840,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD |
| `7D` | `4.60` | 27,960,000.00 USD | 27,960,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD |
| `7D` | `4.61` | 27,970,000.00 USD | 27,970,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD |
| `7D` | `4.62` | 28,100,000.00 USD | 28,100,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 28,320,000.00 USD | 28,320,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 333,310.00 USD | 11,270.00 USD | 61,860.00 USD |
| `7D` | `4.64` | 28,820,000.00 USD | 28,820,000.00 USD | 0.00 USD | 500,990.00 USD | 0.00 USD | 857.07 USD |
| `1D` | `4.65` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 598,910.00 USD |
| `7D` | `4.65` | 29,240,000.00 USD | 29,240,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 649.48 USD |
| `1D` | `4.66` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 281,290.00 USD | 304,540.00 USD | 379,970.00 USD |
| `7D` | `4.66` | 29,540,000.00 USD | 29,540,000.00 USD | 0.00 USD | 144,860.00 USD | 0.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 18,430,000.00 USD | 18,430,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD |
| `7D` | `4.67` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 345,840.00 USD | 62,440.00 USD | 175,640.00 USD |
| `7D` | `4.68` | 30,500,000.00 USD | 30,500,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD |
| `7D` | `4.69` | 30,590,000.00 USD | 30,590,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 19,870,000.00 USD | 19,870,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD |
| `7D` | `4.70` | 30,900,000.00 USD | 30,900,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 20,830,000.00 USD | 20,830,000.00 USD | 0.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD |
| `7D` | `4.71` | 31,310,000.00 USD | 31,310,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `1D` | `4.72` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 5,440.00 USD | 187,480.00 USD | 103,790.00 USD |
| `7D` | `4.72` | 31,500,000.00 USD | 31,500,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 21,290,000.00 USD | 21,290,000.00 USD | 0.00 USD | 61,330.00 USD | 37,010.00 USD | 61,550.00 USD |
| `7D` | `4.73` | 31,560,000.00 USD | 31,560,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD |
| `1D` | `4.74` | 22,040,000.00 USD | 22,040,000.00 USD | 0.00 USD | 273,860.00 USD | 172,000.00 USD | 304,220.00 USD |
| `7D` | `4.74` | 31,880,000.00 USD | 31,880,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `1D` | `4.75` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 240,860.00 USD | 202,760.00 USD | 270,190.00 USD |
| `7D` | `4.75` | 32,420,000.00 USD | 32,420,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 23,110,000.00 USD | 23,110,000.00 USD | 0.00 USD | 35,470.00 USD | 78,750.00 USD | 247,600.00 USD |
| `7D` | `4.76` | 33,770,000.00 USD | 33,770,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `1D` | `4.77` | 23,490,000.00 USD | 23,490,000.00 USD | 0.00 USD | 113,030.00 USD | 151,370.00 USD | 115,600.00 USD |
| `7D` | `4.77` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 23,670,000.00 USD | 23,670,000.00 USD | 0.00 USD | 40,580.00 USD | 20,000.00 USD | 114,020.00 USD |
| `7D` | `4.78` | 36,030,000.00 USD | 36,030,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 24,020,000.00 USD | 24,020,000.00 USD | 0.00 USD | 112,300.00 USD | 92,850.00 USD | 142,450.00 USD |
| `7D` | `4.79` | 37,060,000.00 USD | 37,060,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `1D` | `4.80` | 24,640,000.00 USD | 24,640,000.00 USD | 0.00 USD | 244,480.00 USD | 200,920.00 USD | 174,320.00 USD |
| `7D` | `4.80` | 38,650,000.00 USD | 38,650,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 24,940,000.00 USD | 24,940,000.00 USD | 0.00 USD | 55,660.00 USD | 120,180.00 USD | 127,800.00 USD |
| `7D` | `4.81` | 39,280,000.00 USD | 39,280,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 25,500,000.00 USD | 25,500,000.00 USD | 0.00 USD | 140,640.00 USD | 218,170.00 USD | 201,100.00 USD |
| `7D` | `4.82` | 42,050,000.00 USD | 42,050,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 25,770,000.00 USD | 25,770,000.00 USD | 0.00 USD | 61,110.00 USD | 70,050.00 USD | 140,260.00 USD |
| `7D` | `4.83` | 43,700,000.00 USD | 43,700,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `1D` | `4.84` | 26,020,000.00 USD | 26,020,000.00 USD | 0.00 USD | 85,920.00 USD | 89,230.00 USD | 77,670.00 USD |
| `7D` | `4.84` | 44,190,000.00 USD | 44,190,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `1D` | `4.85` | 26,600,000.00 USD | 26,600,000.00 USD | 0.00 USD | 243,020.00 USD | 110,540.00 USD | 223,650.00 USD |
| `7D` | `4.85` | 46,210,000.00 USD | 46,210,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `1D` | `4.86` | 26,950,000.00 USD | 26,950,000.00 USD | 0.00 USD | 94,860.00 USD | 69,470.00 USD | 178,940.00 USD |
| `7D` | `4.86` | 47,620,000.00 USD | 47,620,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `1D` | `4.87` | 27,170,000.00 USD | 27,170,000.00 USD | 0.00 USD | 111,250.00 USD | 52,140.00 USD | 59,530.00 USD |
| `7D` | `4.87` | 48,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `1D` | `4.88` | 27,250,000.00 USD | 27,250,000.00 USD | 0.00 USD | 36,680.00 USD | 7,330.00 USD | 38,250.00 USD |
| `7D` | `4.88` | 50,270,000.00 USD | 50,270,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD |
| `1D` | `4.89` | 27,340,000.00 USD | 27,340,000.00 USD | 0.00 USD | 10,630.00 USD | 25,940.00 USD | 50,150.00 USD |
| `7D` | `4.89` | 50,850,000.00 USD | 50,850,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `1D` | `4.90` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 24,860.00 USD | 55,440.00 USD | 64,500.00 USD |
| `7D` | `4.90` | 51,990,000.00 USD | 51,990,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `1D` | `4.91` | 27,760,000.00 USD | 27,760,000.00 USD | 0.00 USD | 114,310.00 USD | 85,510.00 USD | 74,620.00 USD |
| `7D` | `4.91` | 53,430,000.00 USD | 53,430,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `7D` | `4.92` | 55,160,000.00 USD | 55,160,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 56,720,000.00 USD | 56,720,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 58,020,000.00 USD | 58,020,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD |
| `7D` | `4.95` | 59,320,000.00 USD | 59,320,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 60,550,000.00 USD | 60,550,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 60,940,000.00 USD | 60,940,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 61,490,000.00 USD | 61,490,000.00 USD | 0.00 USD | 197,950.00 USD | 88,580.00 USD | 270,990.00 USD |
| `7D` | `4.99` | 61,850,000.00 USD | 61,850,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 62,550,000.00 USD | 62,550,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 64,700,000.00 USD | 64,700,000.00 USD | 0.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD |
| `7D` | `5.02` | 66,190,000.00 USD | 66,190,000.00 USD | 0.00 USD | 821,860.00 USD | 337,720.00 USD | 321,920.00 USD |
| `7D` | `5.03` | 67,630,000.00 USD | 67,630,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 886,200.00 USD |
| `7D` | `5.04` | 68,750,000.00 USD | 68,750,000.00 USD | 0.00 USD | 305,260.00 USD | 191,790.00 USD | 619,980.00 USD |
| `7D` | `5.05` | 70,300,000.00 USD | 70,300,000.00 USD | 0.00 USD | 799,820.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 71,010,000.00 USD | 71,010,000.00 USD | 0.00 USD | 92,480.00 USD | 193,330.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 72,210,000.00 USD | 72,210,000.00 USD | 0.00 USD | 358,750.00 USD | 166,480.00 USD | 673,800.00 USD |
| `7D` | `5.08` | 72,730,000.00 USD | 72,730,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 149,330.00 USD |
| `7D` | `5.09` | 73,270,000.00 USD | 73,270,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD |
| `7D` | `5.10` | 73,650,000.00 USD | 73,650,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 74,410,000.00 USD | 74,410,000.00 USD | 0.00 USD | 369,260.00 USD | 92,720.00 USD | 291,780.00 USD |
| `7D` | `5.12` | 74,990,000.00 USD | 74,990,000.00 USD | 0.00 USD | 303,840.00 USD | 166,880.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 75,720,000.00 USD | 75,720,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 484,250.00 USD |
| `7D` | `5.14` | 76,180,000.00 USD | 76,180,000.00 USD | 0.00 USD | 140,950.00 USD | 73,940.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 76,790,000.00 USD | 76,790,000.00 USD | 0.00 USD | 258,430.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 77,310,000.00 USD | 77,310,000.00 USD | 0.00 USD | 51,850.00 USD | 126,880.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 78,000,000.00 USD | 78,000,000.00 USD | 0.00 USD | 280,710.00 USD | 99,740.00 USD | 309,950.00 USD |
| `7D` | `5.18` | 78,260,000.00 USD | 78,260,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 124,380.00 USD |
| `7D` | `5.19` | 78,480,000.00 USD | 78,480,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 138,970.00 USD |
| `7D` | `5.20` | 78,730,000.00 USD | 78,730,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD |
| `7D` | `5.21` | 78,970,000.00 USD | 78,970,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,630.00 USD |
| `7D` | `5.22` | 79,040,000.00 USD | 79,040,000.00 USD | 0.00 USD | 55,630.00 USD | 13,410.00 USD | 398.26 USD |
| `7D` | `5.23` | 79,090,000.00 USD | 79,090,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 34,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.16B` | Total OI Tokens: `276,902,904.8 NEAR`
  * 1h OI Change: `-7.57%` | 4h OI Change: `-11.10%` | 24h OI Change: `-13.49%`
  * Exchange Breakdown: Binance=`224.15M` | Bybit=`157.53M` | OKX=`49.65M` | Hyperliquid=`235.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `41.28K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0093%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0093%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0017%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `43.58%` | `56.42%` | `0.77` | 94,990,000.00 USD |
| `15M` | `Binance` | `44.15%` | `55.85%` | `0.79` | 38,770,000.00 USD |
| `15M` | `OKX` | `47.91%` | `52.09%` | `0.92` | 14,030,000.00 USD |
| `15M` | `Bybit` | `41.15%` | `58.85%` | `0.70` | 14,310,000.00 USD |
| `15M` | `KuCoin` | `42.72%` | `57.28%` | `0.75` | 976,530.00 USD |
| `15M` | `Gate` | `44.99%` | `55.01%` | `0.82` | 1,290,000.00 USD |
| `15M` | `Bitget` | `44.64%` | `55.36%` | `0.81` | 6,480,000.00 USD |
| `15M` | `BingX` | `32.42%` | `67.58%` | `0.48` | 2,100,000.00 USD |
| `15M` | `MEXC` | `42.38%` | `57.62%` | `0.74` | 7,620,000.00 USD |
| `15M` | `Bitunix` | `47.41%` | `52.59%` | `0.90` | 3,670,000.00 USD |
| `15M` | `Hyperliquid` | `38.18%` | `61.82%` | `0.62` | 3,220,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.31%` | `45.69%` | `1.19` | 232,110.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `10.21%` | `89.79%` | `0.11` | 597,410.00 USD |
| `15M` | `HTX` | `49.73%` | `50.27%` | `0.99` | 336,590.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `40.73%` | `59.27%` | `0.69` | 454,770.00 USD |
| `15M` | `Aster` | `35.22%` | `64.78%` | `0.54` | 719,620.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.3%` | `43.7%` | `1.29` | 182,930.00 USD |
| `15M` | `Whale Positions` | `44.15%` | `55.85%` | `0.79` | 38,770,000.00 USD |
| `15M` | `Global Accounts` | `43.58%` | `56.42%` | `0.77` | 94,990,000.00 USD |
| `1H` | `NEAR` | `42.50%` | `57.50%` | `0.74` | 165,150,000.00 USD |
| `1H` | `Binance` | `44.2%` | `55.8%` | `0.79` | 67,310,000.00 USD |
| `1H` | `OKX` | `45.46%` | `54.54%` | `0.83` | 23,000,000.00 USD |
| `1H` | `Bybit` | `41.01%` | `58.99%` | `0.70` | 25,040,000.00 USD |
| `1H` | `KuCoin` | `37.37%` | `62.63%` | `0.60` | 1,930,000.00 USD |
| `1H` | `Gate` | `44.42%` | `55.58%` | `0.80` | 2,570,000.00 USD |
| `1H` | `Bitget` | `40.72%` | `59.28%` | `0.69` | 10,460,000.00 USD |
| `1H` | `BingX` | `36.64%` | `63.36%` | `0.58` | 4,130,000.00 USD |
| `1H` | `MEXC` | `39.2%` | `60.8%` | `0.64` | 13,720,000.00 USD |
| `1H` | `Bitunix` | `44.14%` | `55.86%` | `0.79` | 6,930,000.00 USD |
| `1H` | `Hyperliquid` | `36.39%` | `63.61%` | `0.57` | 5,440,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.79%` | `47.21%` | `1.12` | 504,680.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `25.02%` | `74.98%` | `0.33` | 1,440,000.00 USD |
| `1H` | `HTX` | `50.38%` | `49.62%` | `1.02` | 479,550.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.58%` | `64.42%` | `0.55` | 1,040,000.00 USD |
| `1H` | `Aster` | `32.72%` | `67.28%` | `0.49` | 929,410.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.96%` | `48.04%` | `1.08` | 231,920.00 USD |
| `1H` | `Whale Positions` | `44.2%` | `55.8%` | `0.79` | 67,310,000.00 USD |
| `1H` | `Global Accounts` | `42.50%` | `57.50%` | `0.74` | 165,150,000.00 USD |
| `4H` | `NEAR` | `45.04%` | `54.96%` | `0.82` | 250,070,000.00 USD |
| `4H` | `Binance` | `45.26%` | `54.74%` | `0.83` | 98,680,000.00 USD |
| `4H` | `OKX` | `46.72%` | `53.28%` | `0.88` | 33,730,000.00 USD |
| `4H` | `Bybit` | `43.87%` | `56.13%` | `0.78` | 37,240,000.00 USD |
| `4H` | `KuCoin` | `44.04%` | `55.96%` | `0.79` | 3,120,000.00 USD |
| `4H` | `Gate` | `49.63%` | `50.37%` | `0.99` | 4,690,000.00 USD |
| `4H` | `Bitget` | `43.62%` | `56.38%` | `0.77` | 13,960,000.00 USD |
| `4H` | `BingX` | `44.5%` | `55.5%` | `0.80` | 8,270,000.00 USD |
| `4H` | `MEXC` | `42.49%` | `57.51%` | `0.74` | 21,710,000.00 USD |
| `4H` | `Bitunix` | `47.48%` | `52.52%` | `0.90` | 10,090,000.00 USD |
| `4H` | `Hyperliquid` | `40.87%` | `59.13%` | `0.69` | 8,210,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `38.07%` | `61.93%` | `0.61` | 1,680,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `56.32%` | `43.68%` | `1.29` | 5,020,000.00 USD |
| `4H` | `HTX` | `50.54%` | `49.46%` | `1.02` | 565,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.41%` | `53.59%` | `0.87` | 1,700,000.00 USD |
| `4H` | `Aster` | `29.85%` | `70.15%` | `0.43` | 1,130,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.23%` | `47.77%` | `1.09` | 275,060.00 USD |
| `4H` | `Whale Positions` | `45.26%` | `54.74%` | `0.83` | 98,680,000.00 USD |
| `4H` | `Global Accounts` | `45.04%` | `54.96%` | `0.82` | 250,070,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.44` | `4.42` | `4.44` | `4.45` | `4.39` | 7,755,029.11 USD | 3,981,690.96 USD | 3,773,338.14 USD | 208,352.82 USD | `+2.69%` | `13B / 5S` |
| `0:00 UTC` | `4.39` | `4.40` | `4.39` | `4.43` | `4.38` | 7,242,328.79 USD | 3,238,308.88 USD | 4,004,019.90 USD | -765,711.02 USD | `-10.57%` | `3B / 12S` |
| `5:00 UTC` | `4.41` | `4.41` | `4.41` | `4.43` | `4.39` | 3,825,249.23 USD | 2,351,169.85 USD | 1,474,079.38 USD | 877,090.47 USD | `+22.93%` | `9B / 0S` |
| `0:00 UTC` | `4.40` | `4.41` | `4.40` | `4.42` | `4.38` | 4,175,868.12 USD | 2,209,978.23 USD | 1,965,889.90 USD | 244,088.33 USD | `+5.85%` | `6B / 6S` |
| `5:00 UTC` | `4.38` | `4.40` | `4.38` | `4.42` | `4.38` | 4,640,530.52 USD | 2,789,933.99 USD | 1,850,596.53 USD | 939,337.46 USD | `+20.24%` | `7B / 6S` |
| `0:00 UTC` | `4.33` | `4.34` | `4.33` | `4.41` | `4.31` | 19,326,312.32 USD | 9,601,663.40 USD | 9,724,648.92 USD | -122,985.52 USD | `-0.64%` | `6B / 20S` |
| `5:00 UTC` | `4.36` | `4.35` | `4.36` | `4.37` | `4.34` | 4,641,250.70 USD | 2,849,322.27 USD | 1,791,928.43 USD | 1,057,393.84 USD | `+22.78%` | `8B / 0S` |
| `0:00 UTC` | `4.21` | `4.24` | `4.21` | `4.37` | `4.15` | 41,106,447.75 USD | 17,638,668.55 USD | 23,467,779.20 USD | -5,829,110.65 USD | `-14.18%` | `4B / 19S` |
| `5:00 UTC` | `4.16` | `4.18` | `4.16` | `4.26` | `4.10` | 52,737,896.00 USD | 23,168,223.37 USD | 29,569,672.63 USD | -6,401,449.26 USD | `-12.14%` | `7B / 20S` |
| `0:00 UTC` | `4.15` | `4.15` | `4.15` | `4.19` | `4.13` | 16,718,669.99 USD | 7,274,302.04 USD | 9,444,367.94 USD | -2,170,065.90 USD | `-12.98%` | `10B / 4S` |

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
| `5m` | -236,400.00 USD | -4,600,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,090,000.00 USD | -10,430,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,530,000.00 USD | -23,030,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -5,290,000.00 USD | -19,310,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -5,750,000.00 USD | -15,550,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,760,000.00 USD | -22,540,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -11,920,000.00 USD | -27,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -12,100,000.00 USD | -29,350,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -14,640,000.00 USD | -26,760,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -24,270,000.00 USD | -79,060,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,080,000.00 USD | -120,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -243,510,000.00 USD | -685,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-236.40K` | 15m=`-1.09M` | 1h=`-5.29M` | 24h=`-24.27M`
* Futures Capital Netflows: 5m=`-4.60M` | 15m=`-10.43M` | 1h=`-19.31M` | 24h=`-79.06M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.17` (Risk Distance: `0.1189` pts)
  * +2.5R Take Profit: `4.59`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.57` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.69` (Risk Distance: `0.1189` pts)
  * +2.5R Take Profit: `4.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
