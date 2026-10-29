# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:49:32 IST` (`2026-10-29 22:19:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.11` | **Live Ask Quote**: `4.14` | **Mid Price**: `4.12`
- **Spread Points**: `30.00` | **Spread BPS**: `72.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.41` | VWAP Z-Score: `-2.04` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0703` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `24.46` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.83` | Lower -3.00σ Band: `3.98`
  * Upper +2.51σ Band: `4.76` | Lower -2.51σ Band: `4.05`
  * Upper +2.01σ Band: `4.69` | Lower -2.01σ Band: `4.12`
  * Upper +2.00σ Band: `4.69` | Lower -2.00σ Band: `4.12`
  * Upper +1.28σ Band: `4.59` | Lower -1.28σ Band: `4.22`
  * Upper +1.00σ Band: `4.55` | Lower -1.00σ Band: `4.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.20` | EMA-20=`4.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.38` (Slope: `+0.0000`) | EMA-100=`4.44`
  * Institutional Anchors: EMA-144=`4.47` | EMA-200=`4.48` (Slope: `-0.6818`) | EMA-233=`4.49`
- **Range Boundaries**: 24H High=`4.74` | 24H Low=`4.06` | Weekly High=`4.80` | Weekly Low=`4.06`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.26` (Distance: `-3.23%`)
  * Point of Control (POC) = `4.17` (Distance: `-1.12%`)
  * Value Area Low (VAL) = `4.14` (Distance: `-0.39%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.64` | Weekly POC=`4.45` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`4.06`
  * London Session (08:00-16:00 UTC): High=`4.14` | Low=`4.11`
  * New York Session (13:00-21:00 UTC): High=`4.15` | Low=`4.10`
  * Initial Balance (First Hour): IB High=`4.13` | IB Low=`4.11`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.11` - `4.14`
  * Optimal Trade Entry (OTE 0.705): `4.13`
  * Structural Invalidation Anchor (0.786): `4.15`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.12` | `4.13` | `4.08` | `4.11` | `2,753,130` | 11,296,014.75 USD | -1,207,202.40 USD | `-10.69%` | -40,346,812.00 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4.11` | `4.16` | `4.09` | `4.13` | `1,657,377` | 6,839,450.78 USD | 844,324.90 USD | `+12.34%` | -39,502,487.10 USD | `+0.83` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4.13` | `4.13` | `4.12` | `4.12` | `32,432` | 133,741.86 USD | -5,754.09 USD | `-4.30%` | -39,508,241.18 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.18` | `4.20` | `4.14` | `4.15` | `2,773,782` | 11,567,070.53 USD | 723,484.51 USD | `+6.25%` | -38,831,419.35 USD | `+0.59` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.15` | `4.17` | `4.08` | `4.13` | `6,026,544` | 24,831,193.99 USD | -409,829.11 USD | `-1.65%` | -39,241,248.46 USD | `+0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.13` | `4.13` | `4.12` | `4.12` | `35,970` | 148,332.20 USD | 4,663.52 USD | `+3.14%` | -39,236,584.94 USD | `+0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.40` | `4.41` | `4.10` | `4.17` | `27,824,304` | 117,811,919.82 USD | -11,296,164.64 USD | `-9.59%` | -39,911,269.20 USD | `-2.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.17` | `4.28` | `4.12` | `4.15` | `18,917,752` | 79,175,981.42 USD | 886,549.86 USD | `+1.12%` | -39,024,719.35 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4.15` | `4.17` | `4.08` | `4.12` | `6,058,976` | 24,964,935.85 USD | -415,583.19 USD | `-1.66%` | -39,440,302.54 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.08` | `4.12` | `52,801,032` | 221,952,837.09 USD | -10,825,197.97 USD | `-4.88%` | -39,152,463.28 USD | `-0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -27,473,639.56 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -28,567,348.59 USD | `+1.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -24,158,321.49 USD | `+1.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -28,327,265.31 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.08` | `4.12` | `52,801,032` | 221,952,837.09 USD | -10,825,197.97 USD | `-4.88%` | -39,152,463.28 USD | `-0.62` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`4.12`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `68` | `0x7737...bf66` | `LONG` | 23,585,233.50 USD | `5,640,376.30` | `2.35` | `4.11` | `0.8539` | 10,313,330.67 USD | `+43.73%` | `10X Cross` |
| `138` | `0xb581...6f4f` | `LONG` | 14,704,920.00 USD | `3,600,000.00` | `5.19` | `4.11` | `0.000000` | -3,988,115.22 USD | `-27.12%` | `4X Cross` |
| `226` | `0xdd53...2b13` | `SHORT` | 9,857,390.00 USD | `2,400,202.10` | `2.31` | `4.11` | `29.41` | -4,311,986.12 USD | `-43.74%` | `3X Cross` |
| `279` | `0x77ee...2902` | `LONG` | 8,496,560.64 USD | `2,063,023.10` | `1.93` | `4.11` | `0.000000` | 4,505,364.70 USD | `+53.03%` | `10X Cross` |
| `285` | `0xefe4...194b` | `SHORT` | 8,294,646.67 USD | `2,019,882.30` | `4.44` | `4.11` | `10.93` | 680,438.49 USD | `+8.20%` | `5X Cross` |
| `394` | `0xb83d...6e36` | `SHORT` | 5,941,347.02 USD | `1,445,759.10` | `5.19` | `4.11` | `105.22` | 1,568,101.92 USD | `+26.39%` | `3X Cross` |
| `412` | `0xb46b...538e` | `SHORT` | 5,492,696.80 USD | `1,336,000.00` | `4.33` | `4.11` | `7.55` | 292,167.26 USD | `+5.32%` | `10X Cross` |
| `424` | `0x9df2...c665` | `SHORT` | 5,194,722.50 USD | `1,265,000.00` | `2.03` | `4.11` | `28.60` | -2,628,040.16 USD | `-50.59%` | `10X Cross` |
| `477` | `0x60b0...991e` | `LONG` | 4,605,096.13 USD | `1,121,307.10` | `5.00` | `4.11` | `0.000000` | -996,328.30 USD | `-21.64%` | `10X Cross` |
| `502` | `0xcac1...26b3` | `SHORT` | 4,416,093.91 USD | `1,073,743.90` | `2.48` | `4.11` | `12.07` | -1,756,150.45 USD | `-39.77%` | `10X Cross` |
| `512` | `0x781e...96b7` | `SHORT` | 4,278,700.65 USD | `1,039,604.60` | `2.45` | `4.11` | `7.51` | -1,734,363.46 USD | `-40.53%` | `10X Cross` |
| `604` | `0x45d2...4029` | `SHORT` | 3,738,816.22 USD | `909,400.00` | `3.26` | `4.11` | `48.61` | -772,666.32 USD | `-20.67%` | `10X Cross` |
| `607` | `0x4cae...7c34` | `LONG` | 3,733,470.04 USD | `900,086.80` | `3.52` | `4.11` | `2.66` | 561,069.05 USD | `+15.03%` | `10X Cross` |
| `617` | `0xdf60...d3c7` | `LONG` | 3,698,730.00 USD | `900,000.00` | `4.70` | `4.11` | `3.92` | -530,619.56 USD | `-14.35%` | `8X Isolated` |
| `755` | `0x9aa5...58af` | `SHORT` | 3,015,147.43 USD | `723,977.10` | `4.78` | `4.11` | `16.31` | 444,485.76 USD | `+14.74%` | `10X Cross` |
| `841` | `0xba5d...a352` | `SHORT` | 2,687,000.86 USD | `647,532.50` | `2.83` | `4.11` | `13.07` | -854,285.92 USD | `-31.79%` | `10X Cross` |
| `843` | `0x005a...61fe` | `LONG` | 2,683,576.97 USD | `652,414.60` | `2.08` | `4.11` | `2.42` | 1,326,045.74 USD | `+49.41%` | `7X Cross` |
| `853` | `0xb695...a92d` | `SHORT` | 2,628,073.29 USD | `639,231.70` | `4.57` | `4.11` | `43.95` | 295,285.64 USD | `+11.24%` | `10X Cross` |
| `854` | `0xd1dd...9e85` | `SHORT` | 2,626,042.09 USD | `637,621.00` | `4.96` | `4.11` | `17.89` | 537,430.65 USD | `+20.47%` | `10X Cross` |
| `862` | `0x123d...3bff` | `SHORT` | 2,612,239.79 USD | `636,076.70` | `2.09` | `4.11` | `9.25` | -1,284,863.10 USD | `-49.19%` | `10X Cross` |
| `881` | `0xcf53...ee11` | `SHORT` | 2,560,177.33 USD | `621,598.40` | `5.07` | `4.11` | `24.97` | 591,992.92 USD | `+23.12%` | `10X Cross` |
| `1013` | `0xbfc7...80b4` | `SHORT` | 2,203,543.80 USD | `531,000.00` | `2.01` | `4.11` | `12.39` | -1,138,344.41 USD | `-51.66%` | `10X Cross` |
| `1162` | `0xef96...9383` | `SHORT` | 1,923,616.39 USD | `468,443.50` | `4.50` | `4.11` | `13.15` | 185,684.68 USD | `+9.65%` | `10X Cross` |
| `1266` | `0x5647...e7de` | `SHORT` | 1,778,887.97 USD | `432,682.60` | `4.69` | `4.11` | `15.17` | 249,194.09 USD | `+14.01%` | `10X Cross` |
| `1345` | `0xe097...d0fe` | `LONG` | 1,644,640.00 USD | `400,000.00` | `5.29` | `4.11` | `0.000000` | -472,147.30 USD | `-28.71%` | `10X Cross` |
| `1351` | `0x7fda...17d1` | `SHORT` | 1,640,552.38 USD | `399,511.10` | `4.83` | `4.11` | `105.97` | 287,483.69 USD | `+17.52%` | `10X Cross` |
| `1366` | `0xfc66...ca06` | `SHORT` | 1,627,460.16 USD | `396,313.20` | `4.59` | `4.11` | `44.03` | 191,589.84 USD | `+11.77%` | `10X Cross` |
| `1483` | `0x6e8f...4364` | `LONG` | 1,484,069.46 USD | `361,210.50` | `3.28` | `4.11` | `3.40` | 300,009.23 USD | `+20.22%` | `10X Cross` |
| `1495` | `0xdf95...7d72` | `SHORT` | 1,471,478.34 USD | `358,337.80` | `4.23` | `4.11` | `112.07` | 45,124.50 USD | `+3.07%` | `10X Cross` |
| `1531` | `0xcf67...eb24` | `LONG` | 1,430,520.00 USD | `350,000.00` | `1.98` | `4.11` | `1.67` | 738,902.12 USD | `+51.65%` | `10X Cross` |
| `1627` | `0xfc27...9d9d` | `SHORT` | 1,321,526.50 USD | `319,997.70` | `5.01` | `4.11` | `57.56` | 282,016.12 USD | `+21.34%` | `10X Cross` |
| `1743` | `0xe065...0f85` | `SHORT` | 1,194,316.83 USD | `290,227.90` | `2.81` | `4.11` | `6.65` | -377,572.58 USD | `-31.61%` | `10X Cross` |
| `1756` | `0x023a...2355` | `SHORT` | 1,183,772.30 USD | `288,120.60` | `4.53` | `4.11` | `27.37` | 121,268.28 USD | `+10.24%` | `10X Cross` |
| `1828` | `0xa33a...1ff8` | `SHORT` | 1,123,678.84 USD | `273,634.20` | `4.18` | `4.11` | `7.83` | 20,052.92 USD | `+1.78%` | `10X Cross` |
| `1864` | `0x2577...4897` | `LONG` | 1,099,047.16 USD | `267,642.50` | `4.24` | `4.11` | `0.000000` | -34,553.04 USD | `-3.14%` | `10X Cross` |
| `1938` | `0x9836...457e` | `LONG` | 1,027,902.47 USD | `250,000.60` | `4.67` | `4.11` | `1.43` | -138,890.77 USD | `-13.51%` | `10X Cross` |
| `1940` | `0xff43...d924` | `LONG` | 1,027,460.73 USD | `249,474.50` | `4.64` | `4.11` | `3.28` | -130,582.95 USD | `-12.71%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.63` | 5,952.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.95K USD at 4.6260 USD [API] | `2026-10-28 13:35:01` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 6,333.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.33K USD at 4.6346 USD [API] | `2026-10-28 13:45:09` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 3,211.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.21K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 14,280.13 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 14.28K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 15,704.99 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 15.70K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 1,066.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.07K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 351.22 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.35K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 15.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 18.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.4402 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 11.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.4403 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 18.65 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.4404 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 2,976.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.98K USD at 4.4404 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 6,240.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 6.24K USD at 4.4404 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 47.51 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 4.4404 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 177.62 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.18K USD at 4.4405 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 31,804.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 31.80K USD at 4.4405 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 59.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.06K USD at 4.4405 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 4,749.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 4.75K USD at 4.4405 USD [API] | `2026-10-08 17:49:49` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 7,819.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.82K USD at 4.5900 USD [API] | `2026-10-28 14:56:47` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 5,803.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.80K USD at 4.5900 USD [API] | `2026-10-28 14:56:47` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 9,012.71 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.01K USD at 4.6376 USD [API] | `2026-10-28 15:23:48` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 9,012.42 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.01K USD at 4.6439 USD [API] | `2026-10-28 15:25:24` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 8,090.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.09K USD at 4.6377 USD [API] | `2026-10-28 15:26:03` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 8,486.92 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.49K USD at 4.6278 USD [API] | `2026-10-28 15:33:35` |
| `ANNOUNCEMENT` | `INFO` | `4.65` | 7,649.23 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.65K USD at 4.6466 USD [API] | `2026-10-28 15:41:35` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 5,527.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.53K USD at 4.6380 USD [API] | `2026-10-28 15:46:28` |
| `ANNOUNCEMENT` | `INFO` | `4.64` | 5,803.90 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.80K USD at 4.6383 USD [API] | `2026-10-28 15:46:28` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 5,779.88 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.78K USD at 4.6239 USD [API] | `2026-10-28 15:54:27` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 6,378.78 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.38K USD at 4.6213 USD [API] | `2026-10-28 16:03:43` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 6,021.80 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.02K USD at 4.6183 USD [API] | `2026-10-28 16:08:33` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 6,060.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.06K USD at 4.6109 USD [API] | `2026-10-28 16:10:55` |
| `ANNOUNCEMENT` | `INFO` | `4.60` | 5,801.72 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.80K USD at 4.5987 USD [API] | `2026-10-28 16:21:46` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 9,005.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.01K USD at 4.6084 USD [API] | `2026-10-28 16:28:27` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 11,348.45 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 11.35K USD at 4.5934 USD [API] | `2026-10-28 16:38:51` |
| `ANNOUNCEMENT` | `INFO` | `4.60` | 9,832.24 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.83K USD at 4.6044 USD [API] | `2026-10-28 17:44:33` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 9,273.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.27K USD at 4.6100 USD [API] | `2026-10-28 17:54:59` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 5,803.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.80K USD at 4.5936 USD [API] | `2026-10-28 17:59:18` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 29,008.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 29.01K USD at 4.5936 USD [API] | `2026-10-28 17:59:18` |
| `ANNOUNCEMENT` | `INFO` | `4.65` | 5,635.55 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.64K USD at 4.6521 USD [API] | `2026-10-28 18:04:35` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 5,935.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.94K USD at 4.6055 USD [API] | `2026-10-28 18:11:25` |
| `ANNOUNCEMENT` | `INFO` | `4.61` | 9,990.95 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.99K USD at 4.6054 USD [API] | `2026-10-28 18:11:25` |
| `ANNOUNCEMENT` | `INFO` | `4.60` | 5,273.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.27K USD at 4.6043 USD [API] | `2026-10-28 18:22:01` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 5,885.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.89K USD at 4.7081 USD [API] | `2026-10-28 18:44:24` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 6,803.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.80K USD at 4.6850 USD [API] | `2026-10-28 18:52:00` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 8,107.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.11K USD at 4.6978 USD [API] | `2026-10-28 18:59:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+5.73%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--2.46%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+5.71%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--2.48%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+5.71%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--2.48%`)
  * 7D Horizon: Short MP=`5.03` (Vol: 905,600.00 USD, Dist: `+20.36%`) | Long MP=`4.07` (Vol: 1,100,000.00 USD, Dist: `--2.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8450` | 4,770,000.00 USD | 33,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 4,230.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 470.47 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,650.00 USD | 28,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 28,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 28,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 2,570.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,050.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 2,910.00 USD | 28,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 28,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 31,200.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,360.00 USD | 28,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,950.00 USD | 28,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 11,860.00 USD | 28,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 1,160.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 28,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 1,210.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 1,330.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 8,840.00 USD | 28,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 17,280.00 USD | 28,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,150.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 30,060.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 227.30 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 55,360.00 USD | 28,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 238.78 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 23,160.00 USD | 28,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 38,720.00 USD | 28,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 110,450.00 USD | 28,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 3,370.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 4,410.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 170.21 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,640.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 795.11 USD | 28,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 28,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 6,450.00 USD | 28,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 3,330.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 669.86 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 85,140.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,890.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 14,650.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 4,420.00 USD | 28,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 814.78 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 300.25 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 530,700.00 USD | 28,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 311.00 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 13,300.00 USD | 27,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 5,240.00 USD | 27,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,380.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 12,630.00 USD | 27,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,460.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 19,600.00 USD | 27,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 2,440.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 1,450.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 681.98 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 108.71 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 14,290.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 12,950.00 USD | 27,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 8,670.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 11,320.00 USD | 27,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 4,810.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 42,700.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 40,550.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,290.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 4,130.00 USD | 27,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 35,540.00 USD | 27,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,890.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 3,130.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 2,070.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 5,740.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 23,920.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 11,560.00 USD | 27,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,010.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 10,180.00 USD | 27,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 42,930.00 USD | 27,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,320.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 122,770.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,220.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 582.39 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 17,030.00 USD | 27,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 15,730.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,230.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 10,540.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 6,820.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 1,880.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 229,560.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,640.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 94,190.00 USD | 26,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 30,070.00 USD | 26,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 594.13 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 77,890.00 USD | 26,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 225,110.00 USD | 26,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 13,820.00 USD | 26,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 968.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 74,790.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 8,330.00 USD | 26,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,310.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,060.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 42,920.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 116,500.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,270.00 USD | 26,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 748.70 USD | 26,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 13,570.00 USD | 26,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 3,530.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 6,600.00 USD | 26,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,310.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,650.00 USD | 26,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,670.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 74,090.00 USD | 26,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,680.00 USD | 26,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 35,930.00 USD | 26,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 422,720.00 USD | 26,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 1,970.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570,000.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,110.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 203,420.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 282,760.00 USD | 23,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,540.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,990.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 13,230.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 5,740.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 19,070.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 140,910.00 USD | 23,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 4,450.00 USD | 23,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,780.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 1,550.00 USD | 23,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 18,360.00 USD | 23,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 6,380.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 412,400.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 8,730.00 USD | 22,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 860.82 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,330,000.00 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 69,910.00 USD | 20,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 3,950.00 USD | 20,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 4,200.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 20,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 9,840.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 20,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,680.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 375.84 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,300.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 132,990.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 19,350.00 USD | 20,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 38,030.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 3,350.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 42,880.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 154.83 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 3,880.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 1,360.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 214,990.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,470.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 14,230.00 USD | 19,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 7,890.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,760.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 367,060.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,550.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,140.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 929.20 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,370.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,780.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 213,920.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 85,170.00 USD | 19,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 3,960.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 155,560.00 USD | 19,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 1,010.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 166,480.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 15,880.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 180,710.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 387.15 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 375,800.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,840.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 8,140.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 106,550.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 28,140.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,160.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 4,930.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 45,890.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,050.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,330.00 USD | 17,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 38,380.00 USD | 17,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 5,540.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 214,120.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 83,740.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 7,320.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 7,310.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 134,880.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 20,150.00 USD | 17,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 27,070.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 71,220.00 USD | 17,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 17,490.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 58,930.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 37,970.00 USD | 17,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 836,670.00 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 2,680.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 134,710.00 USD | 16,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 138,120.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 22,780.00 USD | 16,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 32,280.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 63,800.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 577,220.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 3,860.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 2,020.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 36,990.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,450.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 5,390.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 76,100.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 190,450.00 USD | 15,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 93,990.00 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 28,770.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 2,340.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,550.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 6,650.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 112,700.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 687,230.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 1,280,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,560.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 37,050.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 251,330.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 79,900.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 460,870.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 368,760.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 5,440.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 37,650.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 39,740.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 25,250.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 154,780.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 42,940.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 10,950,000.00 USD | 10,950,000.00 USD | 147,810.00 USD | 44,040.00 USD | 165,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 13,470.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 10,600,000.00 USD | 10,600,000.00 USD | 50,840.00 USD | 8,120.00 USD | 156.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 20,820.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 10,540,000.00 USD | 10,540,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 72,880.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,580,000.00 USD | 5,580,000.00 USD | 710.37 USD | 5,040.00 USD | 258.71 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 10,400,000.00 USD | 10,400,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 45,600.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,570,000.00 USD | 5,570,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 10,310,000.00 USD | 10,310,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 218,940.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,570,000.00 USD | 5,570,000.00 USD | 16,270.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 10,140,000.00 USD | 10,140,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 622,270.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 130,530.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 9.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,020,000.00 USD | 10,020,000.00 USD | 27,750.00 USD | 0.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 188,240.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,540,000.00 USD | 5,540,000.00 USD | 17,670.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 9,940,000.00 USD | 9,940,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 47,380.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,500,000.00 USD | 5,500,000.00 USD | 430.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 9,800,000.00 USD | 9,800,000.00 USD | 50,620.00 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 40,480.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,500,000.00 USD | 5,500,000.00 USD | 186.40 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 9,740,000.00 USD | 9,740,000.00 USD | 425.03 USD | 0.00 USD | 546.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 37,230.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,500,000.00 USD | 5,500,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 9,740,000.00 USD | 9,740,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 21,540.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,480,000.00 USD | 5,480,000.00 USD | 73,140.00 USD | 33,110.00 USD | 41,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 9,640,000.00 USD | 9,640,000.00 USD | 128,440.00 USD | 40,020.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 58,120.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 9,350,000.00 USD | 9,350,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 78,040.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 9,280,000.00 USD | 9,280,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 54,900.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,300,000.00 USD | 5,300,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 9,210,000.00 USD | 9,210,000.00 USD | 13,170.00 USD | 8,090.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 11,510.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,290,000.00 USD | 5,290,000.00 USD | 7,430.00 USD | 6,570.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,170,000.00 USD | 9,170,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 81,910.00 USD | 9,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,250,000.00 USD | 5,250,000.00 USD | 76.30 USD | 2,230.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,090,000.00 USD | 9,090,000.00 USD | 49,420.00 USD | 0.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 129,010.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,240,000.00 USD | 5,240,000.00 USD | 4,050.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,000,000.00 USD | 9,000,000.00 USD | 1,530.00 USD | 18,170.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 136,040.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,230,000.00 USD | 5,230,000.00 USD | 53,440.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 810.67 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 18,470.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 8,960,000.00 USD | 8,960,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 35,730.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,150,000.00 USD | 5,150,000.00 USD | 352.15 USD | 18,900.00 USD | 16,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 163,840.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 67,130.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,120,000.00 USD | 5,120,000.00 USD | 138.23 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 252.34 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 16,580.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,110,000.00 USD | 5,110,000.00 USD | 1,450.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 8,920,000.00 USD | 8,920,000.00 USD | 2,220.00 USD | 0.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 160,010.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,040,000.00 USD | 5,040,000.00 USD | 1,690.00 USD | 11,800.00 USD | 102.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 8,840,000.00 USD | 8,840,000.00 USD | 57,040.00 USD | 0.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 19,300.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,030,000.00 USD | 5,030,000.00 USD | 105,540.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 8,750,000.00 USD | 8,750,000.00 USD | 106,950.00 USD | 8,890.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 173,540.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 4,880,000.00 USD | 4,880,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 8,540,000.00 USD | 8,540,000.00 USD | 1,210.00 USD | 50,710.00 USD | 869.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 96,380.00 USD | 8,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,700,000.00 USD | 4,700,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 8,480,000.00 USD | 8,480,000.00 USD | 171,750.00 USD | 28,250.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 2,130.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 35,760.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 8,230,000.00 USD | 8,230,000.00 USD | 1,280.00 USD | 25,680.00 USD | 47,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,950,000.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,600,000.00 USD | 4,600,000.00 USD | 147,080.00 USD | 26,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,160,000.00 USD | 8,160,000.00 USD | 90,780.00 USD | 41,330.00 USD | 82,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 372,020.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 21,500.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 7,940,000.00 USD | 7,940,000.00 USD | 51,660.00 USD | 20,780.00 USD | 51,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 127,720.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 4,360,000.00 USD | 4,360,000.00 USD | 4,810.00 USD | 6,420.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 7,820,000.00 USD | 7,820,000.00 USD | 82,440.00 USD | 31,050.00 USD | 128,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 687,490.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 4,330,000.00 USD | 4,330,000.00 USD | 12,850.00 USD | 5,610.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 7,580,000.00 USD | 7,580,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 38,270.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,310,000.00 USD | 4,310,000.00 USD | 36,860.00 USD | 29,270.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 7,550,000.00 USD | 7,550,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 246,650.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,200,000.00 USD | 4,200,000.00 USD | 156,730.00 USD | 52,430.00 USD | 65,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,350,000.00 USD | 7,350,000.00 USD | 231,790.00 USD | 102,960.00 USD | 270,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 505,940.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,930,000.00 USD | 3,930,000.00 USD | 79,930.00 USD | 30,290.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 6,750,000.00 USD | 6,750,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 152,750.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 3,800,000.00 USD | 3,800,000.00 USD | 349,680.00 USD | 106,190.00 USD | 138,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,070,000.00 USD | 6,070,000.00 USD | 63,200.00 USD | 103,210.00 USD | 79,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 234,780.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 3,210,000.00 USD | 3,210,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 5,830,000.00 USD | 5,830,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 61,540.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 2,980,000.00 USD | 2,980,000.00 USD | 112,570.00 USD | 56,050.00 USD | 77,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,220,000.00 USD | 5,220,000.00 USD | 392,150.00 USD | 94,720.00 USD | 437,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 39,230.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 2,740,000.00 USD | 2,740,000.00 USD | 60,540.00 USD | 33,270.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,290,000.00 USD | 4,290,000.00 USD | 279,800.00 USD | 88,330.00 USD | 253,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 375,020.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 2,540,000.00 USD | 2,540,000.00 USD | 23,550.00 USD | 55,650.00 USD | 81,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 3,670,000.00 USD | 3,670,000.00 USD | 250,870.00 USD | 45,290.00 USD | 148,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 23,890.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 2,380,000.00 USD | 2,380,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,230,000.00 USD | 3,230,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 107,490.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 2,020,000.00 USD | 2,020,000.00 USD | 78,330.00 USD | 25,880.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,940,000.00 USD | 2,940,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 91,310.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 1,820,000.00 USD | 1,820,000.00 USD | 190,260.00 USD | 0.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,450,000.00 USD | 2,450,000.00 USD | 305,310.00 USD | 72,410.00 USD | 188,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 549,980.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 1,570,000.00 USD | 1,570,000.00 USD | 69,760.00 USD | 44,930.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,880,000.00 USD | 1,880,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 138,060.00 USD | 938,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 1,440,000.00 USD | 1,440,000.00 USD | 510,570.00 USD | 253,070.00 USD | 188,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 615,940.00 USD | 615,940.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 17,870.00 USD | 800,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 483,930.00 USD | 483,930.00 USD | 10,540.00 USD | 99,090.00 USD | 271,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 259,310.00 USD | 259,310.00 USD | 134,630.00 USD | 83,890.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 692,300.00 USD | 782,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 102,730.00 USD | 102,730.00 USD | 33,810.00 USD | 10,080.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 618,690.00 USD | 618,690.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 1,240,000.00 USD | 1,240,000.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 55,720.00 USD | 89,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.11` | 154,110.00 USD | 154,110.00 USD | 22,930.00 USD | 59,250.00 USD | 71,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.11` | 308,220.00 USD | 308,220.00 USD | 22,930.00 USD | 59,250.00 USD | 71,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.11` | 1,540,000.00 USD | 1,540,000.00 USD | 110,780.00 USD | 0.00 USD | 190,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 231.67 USD | 34,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.12` | 617,880.00 USD | 617,880.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.12` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 341,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.13` | 1,050,000.00 USD | 1,050,000.00 USD | 183,190.00 USD | 87,750.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 33,970.00 USD | 33,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.14` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 34,720.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 2,190,000.00 USD | 2,190,000.00 USD | 214,920.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 2,580,000.00 USD | 2,580,000.00 USD | 213,530.00 USD | 53,890.00 USD | 127,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.18` | 1,260,000.00 USD | 1,260,000.00 USD | 9,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 2,010.00 USD | 2,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,270,000.00 USD | 1,270,000.00 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 1,770,000.00 USD | 1,770,000.00 USD | 66,130.00 USD | 440,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,450,000.00 USD | 2,450,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.25` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 64,520.00 USD | 229,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 57,340.00 USD | 229.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 171,790.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.27` | 3,600,000.00 USD | 3,600,000.00 USD | 594,570.00 USD | 24,620.00 USD | 59,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 5,160,000.00 USD | 5,160,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,240,000.00 USD | 4,240,000.00 USD | 313,130.00 USD | 30,410.00 USD | 296,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.29` | 4,580,000.00 USD | 4,580,000.00 USD | 152,480.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.30` | 4,780,000.00 USD | 4,780,000.00 USD | 3,320.00 USD | 34,720.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 7,290,000.00 USD | 7,290,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,110,000.00 USD | 5,110,000.00 USD | 270,390.00 USD | 0.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 7,730,000.00 USD | 7,730,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.32` | 5,210,000.00 USD | 5,210,000.00 USD | 33,680.00 USD | 59,810.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 8,380,000.00 USD | 8,380,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.33` | 5,640,000.00 USD | 5,640,000.00 USD | 255,140.00 USD | 93,880.00 USD | 86,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 6,170,000.00 USD | 6,170,000.00 USD | 269,670.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 8,660,000.00 USD | 8,660,000.00 USD | 4,550.00 USD | 28,670.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.35` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 85,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,360.00 USD | 5,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 6,380,000.00 USD | 6,380,000.00 USD | 84,400.00 USD | 12,310.00 USD | 30,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 8,900,000.00 USD | 8,900,000.00 USD | 8,190.00 USD | 0.00 USD | 143,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.37` | 47,330.00 USD | 52,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 6,610,000.00 USD | 6,610,000.00 USD | 52,120.00 USD | 46,860.00 USD | 129,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 367.06 USD | 53,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 7,450,000.00 USD | 7,450,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 3,610.00 USD | 56,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 9,810,000.00 USD | 9,810,000.00 USD | 248,520.00 USD | 108,260.00 USD | 155,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 905.81 USD | 57,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 8,180,000.00 USD | 8,180,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 10,410,000.00 USD | 10,410,000.00 USD | 106,760.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,790.00 USD | 59,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 8,560,000.00 USD | 8,560,000.00 USD | 196,030.00 USD | 112,990.00 USD | 65,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 45,930.00 USD | 273,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 309,400.00 USD | 368,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 11,380,000.00 USD | 11,380,000.00 USD | 404,280.00 USD | 71,590.00 USD | 176,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 9,730.00 USD | 378,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 8,760,000.00 USD | 8,760,000.00 USD | 5,100.00 USD | 49,400.00 USD | 97,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 11,660,000.00 USD | 11,660,000.00 USD | 163,540.00 USD | 46,230.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 799.63 USD | 379,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 9,540,000.00 USD | 9,540,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 116,400.00 USD | 72,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 6,320.00 USD | 385,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 9,590,000.00 USD | 9,590,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 9,600,000.00 USD | 9,600,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 62,110.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 386,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 12,250,000.00 USD | 12,250,000.00 USD | 203,160.00 USD | 135,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 8,430.00 USD | 394,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 9,860,000.00 USD | 9,860,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 10,410,000.00 USD | 10,410,000.00 USD | 252,130.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 12,590,000.00 USD | 12,590,000.00 USD | 242,770.00 USD | 93,790.00 USD | 504.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 17,170.00 USD | 411,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 10,960,000.00 USD | 10,960,000.00 USD | 361,560.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 13,170,000.00 USD | 13,170,000.00 USD | 373,240.00 USD | 200,700.00 USD | 343.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 18,080.00 USD | 429,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 11,740,000.00 USD | 11,740,000.00 USD | 162,900.00 USD | 307,580.00 USD | 312,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 13,250,000.00 USD | 13,250,000.00 USD | 77,780.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 47,410.00 USD | 477,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 12,300,000.00 USD | 12,300,000.00 USD | 266,310.00 USD | 88,150.00 USD | 205,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 13,390,000.00 USD | 13,390,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,100.00 USD | 495,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 13,070,000.00 USD | 13,070,000.00 USD | 487,540.00 USD | 0.00 USD | 278,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 14,290,000.00 USD | 14,290,000.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 150,600.00 USD | 584,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 495,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 22,540.00 USD | 214,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 713.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 14,440,000.00 USD | 14,440,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 16,020,000.00 USD | 16,020,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 14,740,000.00 USD | 14,740,000.00 USD | 156,380.00 USD | 70,180.00 USD | 67,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 16,560,000.00 USD | 16,560,000.00 USD | 305,830.00 USD | 27,650.00 USD | 210,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 16,190,000.00 USD | 16,190,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 16,690,000.00 USD | 16,690,000.00 USD | 44,380.00 USD | 0.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 17,170,000.00 USD | 17,170,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 18,290,000.00 USD | 18,290,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 17,380,000.00 USD | 17,380,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 18,400,000.00 USD | 18,400,000.00 USD | 3,460.00 USD | 112,080.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 496,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 17,510,000.00 USD | 17,510,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 18,410,000.00 USD | 18,410,000.00 USD | 3,350.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 17,660,000.00 USD | 17,660,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 18,550,000.00 USD | 18,550,000.00 USD | 134,680.00 USD | 0.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 41,900.00 USD | 538,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 17,660,000.00 USD | 17,660,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 18,760,000.00 USD | 18,760,000.00 USD | 213,490.00 USD | 0.00 USD | 431.56 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 493.16 USD | 538,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 18,070,000.00 USD | 18,070,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 19,280,000.00 USD | 19,280,000.00 USD | 501,930.00 USD | 18,170.00 USD | 407.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 116.59 USD | 539,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 19,150,000.00 USD | 19,150,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 19,700,000.00 USD | 19,700,000.00 USD | 420,940.00 USD | 0.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 20,130,000.00 USD | 20,130,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 20,020,000.00 USD | 20,020,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,390.00 USD | 663,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 20,690,000.00 USD | 20,690,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 21,290,000.00 USD | 21,290,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 20,980,000.00 USD | 20,980,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 21,800,000.00 USD | 21,800,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 21,070,000.00 USD | 21,070,000.00 USD | 2,450.00 USD | 0.00 USD | 88,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 22,140,000.00 USD | 22,140,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 21,380,000.00 USD | 21,380,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 1,940.00 USD | 665,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 23,110,000.00 USD | 23,110,000.00 USD | 365,580.00 USD | 284,360.00 USD | 316,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 21,790,000.00 USD | 21,790,000.00 USD | 178,360.00 USD | 232,800.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 23,400,000.00 USD | 23,400,000.00 USD | 5,440.00 USD | 187,480.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 21,980,000.00 USD | 21,980,000.00 USD | 7,140.00 USD | 0.00 USD | 180,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 23,560,000.00 USD | 23,560,000.00 USD | 61,330.00 USD | 37,010.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 22,040,000.00 USD | 22,040,000.00 USD | 59,970.00 USD | 0.00 USD | 790.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.74` | 24,310,000.00 USD | 24,310,000.00 USD | 273,860.00 USD | 172,000.00 USD | 304,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 22,360,000.00 USD | 22,360,000.00 USD | 14,750.00 USD | 173,100.00 USD | 130,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 335.95 USD | 665,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 25,030,000.00 USD | 25,030,000.00 USD | 240,860.00 USD | 202,760.00 USD | 270,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 22,910,000.00 USD | 22,910,000.00 USD | 17,340.00 USD | 185,060.00 USD | 342,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 154,870.00 USD | 820,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 25,390,000.00 USD | 25,390,000.00 USD | 35,470.00 USD | 78,750.00 USD | 247,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 24,250,000.00 USD | 24,250,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 275,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 85,580.00 USD | 906,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 25,770,000.00 USD | 25,770,000.00 USD | 113,030.00 USD | 151,370.00 USD | 115,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 25,160,000.00 USD | 25,160,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 913,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 25,940,000.00 USD | 25,940,000.00 USD | 40,580.00 USD | 20,000.00 USD | 114,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 26,510,000.00 USD | 26,510,000.00 USD | 683,730.00 USD | 513,870.00 USD | 153,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,530.00 USD | 917,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 26,290,000.00 USD | 26,290,000.00 USD | 112,300.00 USD | 92,850.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 27,550,000.00 USD | 27,550,000.00 USD | 713,060.00 USD | 249,310.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 6,460.00 USD | 924,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 26,910,000.00 USD | 26,910,000.00 USD | 244,480.00 USD | 200,920.00 USD | 174,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 29,140,000.00 USD | 29,140,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 27,120,000.00 USD | 27,120,000.00 USD | 31,770.00 USD | 53,140.00 USD | 127,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 29,760,000.00 USD | 29,760,000.00 USD | 400,070.00 USD | 125,900.00 USD | 102,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 473,730.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 27,640,000.00 USD | 27,640,000.00 USD | 140,640.00 USD | 201,340.00 USD | 172,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 32,530,000.00 USD | 32,530,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 27,840,000.00 USD | 27,840,000.00 USD | 61,110.00 USD | 53,720.00 USD | 88,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 34,180,000.00 USD | 34,180,000.00 USD | 822,860.00 USD | 85,680.00 USD | 740,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 4,530.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 28,090,000.00 USD | 28,090,000.00 USD | 82,160.00 USD | 89,230.00 USD | 77,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 34,670,000.00 USD | 34,670,000.00 USD | 97,300.00 USD | 71,790.00 USD | 323,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 36,690,000.00 USD | 36,690,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 38,100,000.00 USD | 38,100,000.00 USD | 444,810.00 USD | 162,380.00 USD | 801,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 39,170,000.00 USD | 39,170,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 16,630.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.88` | 40,750,000.00 USD | 40,750,000.00 USD | 449,970.00 USD | 340,260.00 USD | 793,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 15,160.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 41,340,000.00 USD | 41,340,000.00 USD | 213,960.00 USD | 100,850.00 USD | 271,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 42,470,000.00 USD | 42,470,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 43,910,000.00 USD | 43,910,000.00 USD | 637,320.00 USD | 208,910.00 USD | 591,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 140,840.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 45,640,000.00 USD | 45,640,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 47,200,000.00 USD | 47,200,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 556.67 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 48,500,000.00 USD | 48,500,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 49,800,000.00 USD | 49,800,000.00 USD | 468,360.00 USD | 161,040.00 USD | 669,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 51,040,000.00 USD | 51,040,000.00 USD | 607,770.00 USD | 214,910.00 USD | 411,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 51,420,000.00 USD | 51,420,000.00 USD | 198,220.00 USD | 72,330.00 USD | 112,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 52,080,000.00 USD | 52,080,000.00 USD | 251,840.00 USD | 102,410.00 USD | 302,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 210,290.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 52,430,000.00 USD | 52,430,000.00 USD | 133,330.00 USD | 103,060.00 USD | 118,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 53,130,000.00 USD | 53,130,000.00 USD | 210,680.00 USD | 36,180.00 USD | 453,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 55,290,000.00 USD | 55,290,000.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 56,770,000.00 USD | 56,770,000.00 USD | 821,860.00 USD | 337,720.00 USD | 321,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 58,210,000.00 USD | 58,210,000.00 USD | 385,330.00 USD | 172,880.00 USD | 886,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 59,300,000.00 USD | 59,300,000.00 USD | 305,260.00 USD | 163,190.00 USD | 620,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.05` | 60,750,000.00 USD | 60,750,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 55,570.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 61,430,000.00 USD | 61,430,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 62,600,000.00 USD | 62,600,000.00 USD | 358,750.00 USD | 137,080.00 USD | 673,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 63,120,000.00 USD | 63,120,000.00 USD | 204,140.00 USD | 167,810.00 USD | 148,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 4,130.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 63,660,000.00 USD | 63,660,000.00 USD | 105,390.00 USD | 52,790.00 USD | 384,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 64,040,000.00 USD | 64,040,000.00 USD | 182,200.00 USD | 0.00 USD | 202,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 64,800,000.00 USD | 64,800,000.00 USD | 369,260.00 USD | 92,720.00 USD | 291,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 65,380,000.00 USD | 65,380,000.00 USD | 303,840.00 USD | 166,880.00 USD | 116,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 66,110,000.00 USD | 66,110,000.00 USD | 173,190.00 USD | 71,310.00 USD | 483,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 66,550,000.00 USD | 66,550,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.14` | 82,200.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.15` | 67,110,000.00 USD | 67,110,000.00 USD | 205,680.00 USD | 82,350.00 USD | 268,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 67,620,000.00 USD | 67,620,000.00 USD | 51,850.00 USD | 112,830.00 USD | 346,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 317.65 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 68,300,000.00 USD | 68,300,000.00 USD | 280,710.00 USD | 85,040.00 USD | 310,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 3,620.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.18` | 68,550,000.00 USD | 68,550,000.00 USD | 67,600.00 USD | 63,250.00 USD | 123,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 68,770,000.00 USD | 68,770,000.00 USD | 69,310.00 USD | 13,680.00 USD | 139,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.20` | 69,020,000.00 USD | 69,020,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.21` | 69,260,000.00 USD | 69,260,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 69,330,000.00 USD | 69,330,000.00 USD | 52,130.00 USD | 13,410.00 USD | 300.69 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 69,380,000.00 USD | 69,380,000.00 USD | 0.00 USD | 15,520.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.24` | 21,060.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 544.38 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 257.38 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 114.37 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 1,140.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 29,250.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 19,710.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 25,310.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 41,910.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 60,180.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 20,300.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 35,680.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 1,050.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 627.98 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 77,760.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 1,380.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 64,190.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 6,190.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 300,420.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.64` | 56,450.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 942.09 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 334.26 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 66,300.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 2,010.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 2,700.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 55,580.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 128.37 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 199.31 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 271,610.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 486.74 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 1,830.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 24,380.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.17` | 1,910.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.17` | 308.75 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 1,540.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 1,270.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 369,650.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 41,340.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 47,710.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 2,560.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 831.97 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 1,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 1,930.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 87,890.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 51,780.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 13,340.00 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 803.13 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 35,590.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 10,770.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 15,540.00 USD | 7,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 789,370.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.74` | 5,130.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,690.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,960.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.89` | 68,950.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.91` | 189.89 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 2,420,000.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.95` | 38,370.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.00` | 1,160.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.04` | 558.67 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 670.95 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.22` | 63,550.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 1,370,000.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 90,250.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 16,640.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 14,890.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 107,860.00 USD | 13,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 10,030,000.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 23,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 7,860,000.00 USD | 31,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 2,630.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 491.45 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 161.45 USD | 31,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 327,090.00 USD | 31,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.78` | 72,540.00 USD | 31,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 2,920.00 USD | 31,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 32,560.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 31,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.14` | 983.92 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.15` | 190.01 USD | 32,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.18` | 362.97 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 32,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.23` | 24,700.00 USD | 32,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 21,470.00 USD | 32,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.27` | 87,280.00 USD | 32,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8450` | 33,640,000.00 USD | 0.00 USD | 4,770,000.00 USD | `-79.65%` | `5,642,782.60` |
| `Live` | `Long` | `0.8550` | 28,870,000.00 USD | 0.00 USD | 4,230.00 USD | `-79.41%` | `4,949.80` |
| `Live` | `Long` | `0.8650` | 28,860,000.00 USD | 0.00 USD | 433.80 USD | `-79.17%` | `501.50` |
| `Live` | `Long` | `0.8850` | 28,860,000.00 USD | 0.00 USD | 470.47 USD | `-78.69%` | `531.60` |
| `Live` | `Long` | `0.8950` | 28,860,000.00 USD | 0.00 USD | 39,650.00 USD | `-78.45%` | `44,298.30` |
| `Live` | `Long` | `0.9050` | 28,820,000.00 USD | 0.00 USD | 292.22 USD | `-78.21%` | `322.90` |
| `Live` | `Long` | `0.9150` | 28,820,000.00 USD | 0.00 USD | 11,370.00 USD | `-77.97%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 28,810,000.00 USD | 0.00 USD | 2,570.00 USD | `-77.73%` | `2,773.30` |
| `Live` | `Long` | `0.9550` | 28,810,000.00 USD | 0.00 USD | 1,050.00 USD | `-77.00%` | `1,102.20` |
| `Live` | `Long` | `0.9650` | 28,810,000.00 USD | 0.00 USD | 965.00 USD | `-76.76%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 28,810,000.00 USD | 0.00 USD | 2,910.00 USD | `-76.28%` | `2,950.80` |
| `Live` | `Long` | `0.9950` | 28,800,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.04%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 28,650,000.00 USD | 0.00 USD | 31,200.00 USD | `-75.80%` | `31,041.00` |
| `Live` | `Long` | `1.02` | 28,620,000.00 USD | 0.00 USD | 10,360.00 USD | `-75.32%` | `10,111.10` |
| `Live` | `Long` | `1.03` | 28,610,000.00 USD | 0.00 USD | 5,950.00 USD | `-75.08%` | `5,744.40` |
| `Live` | `Long` | `1.05` | 28,600,000.00 USD | 0.00 USD | 11,860.00 USD | `-74.60%` | `11,237.90` |
| `Live` | `Long` | `1.06` | 28,590,000.00 USD | 0.00 USD | 1,160.00 USD | `-74.35%` | `1,093.60` |
| `Live` | `Long` | `1.07` | 28,590,000.00 USD | 0.00 USD | 7,510.00 USD | `-74.11%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 28,580,000.00 USD | 0.00 USD | 1,210.00 USD | `-73.87%` | `1,112.30` |
| `Live` | `Long` | `1.09` | 28,580,000.00 USD | 0.00 USD | 1,330.00 USD | `-73.63%` | `1,211.80` |
| `Live` | `Long` | `1.10` | 28,580,000.00 USD | 0.00 USD | 8,840.00 USD | `-73.39%` | `8,000.00` |
| `Live` | `Long` | `1.11` | 28,570,000.00 USD | 0.00 USD | 17,280.00 USD | `-73.15%` | `15,500.00` |
| `Live` | `Long` | `1.12` | 28,550,000.00 USD | 0.00 USD | 2,150.00 USD | `-72.91%` | `1,914.40` |
| `Live` | `Long` | `1.14` | 28,550,000.00 USD | 0.00 USD | 4,960.00 USD | `-72.67%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 28,540,000.00 USD | 0.00 USD | 30,060.00 USD | `-72.43%` | `26,252.70` |
| `Live` | `Long` | `1.16` | 28,510,000.00 USD | 0.00 USD | 227.30 USD | `-72.19%` | `196.80` |
| `Live` | `Long` | `1.17` | 28,510,000.00 USD | 0.00 USD | 55,360.00 USD | `-71.95%` | `47,516.90` |
| `Live` | `Long` | `1.18` | 28,460,000.00 USD | 0.00 USD | 184.59 USD | `-71.71%` | `157.10` |
| `Live` | `Long` | `1.19` | 28,460,000.00 USD | 0.00 USD | 238.78 USD | `-71.47%` | `201.50` |
| `Live` | `Long` | `1.20` | 28,460,000.00 USD | 0.00 USD | 23,160.00 USD | `-71.22%` | `19,381.10` |
| `Live` | `Long` | `1.24` | 28,440,000.00 USD | 0.00 USD | 38,720.00 USD | `-70.26%` | `31,349.00` |
| `Live` | `Long` | `1.25` | 28,400,000.00 USD | 0.00 USD | 110,450.00 USD | `-69.78%` | `88,005.60` |
| `Live` | `Long` | `1.26` | 28,290,000.00 USD | 0.00 USD | 2,060.00 USD | `-69.54%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 28,280,000.00 USD | 0.00 USD | 3,370.00 USD | `-69.30%` | `2,646.90` |
| `Live` | `Long` | `1.28` | 28,280,000.00 USD | 0.00 USD | 169.23 USD | `-69.06%` | `131.70` |
| `Live` | `Long` | `1.30` | 28,280,000.00 USD | 0.00 USD | 116.80 USD | `-68.58%` | `89.50` |
| `Live` | `Long` | `1.32` | 28,280,000.00 USD | 0.00 USD | 4,410.00 USD | `-68.09%` | `3,327.30` |
| `Live` | `Long` | `1.33` | 28,280,000.00 USD | 0.00 USD | 170.21 USD | `-67.85%` | `127.50` |
| `Live` | `Long` | `1.34` | 28,280,000.00 USD | 0.00 USD | 603.91 USD | `-67.61%` | `449.00` |
| `Live` | `Long` | `1.35` | 28,280,000.00 USD | 0.00 USD | 2,640.00 USD | `-67.37%` | `1,947.70` |
| `Live` | `Long` | `1.36` | 28,270,000.00 USD | 0.00 USD | 795.11 USD | `-67.13%` | `582.50` |
| `Live` | `Long` | `1.38` | 28,270,000.00 USD | 0.00 USD | 12,380.00 USD | `-66.89%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 28,260,000.00 USD | 0.00 USD | 6,450.00 USD | `-66.65%` | `4,659.70` |
| `Live` | `Long` | `1.40` | 28,250,000.00 USD | 0.00 USD | 931.86 USD | `-66.41%` | `668.00` |
| `Live` | `Long` | `1.41` | 28,250,000.00 USD | 0.00 USD | 3,330.00 USD | `-66.17%` | `2,368.10` |
| `Live` | `Long` | `1.42` | 28,250,000.00 USD | 0.00 USD | 669.86 USD | `-65.93%` | `473.40` |
| `Live` | `Long` | `1.43` | 28,250,000.00 USD | 0.00 USD | 85,140.00 USD | `-65.69%` | `59,746.30` |
| `Live` | `Long` | `1.45` | 28,160,000.00 USD | 0.00 USD | 1,890.00 USD | `-65.20%` | `1,304.90` |
| `Live` | `Long` | `1.47` | 28,160,000.00 USD | 0.00 USD | 14,650.00 USD | `-64.72%` | `10,000.00` |
| `Live` | `Long` | `1.48` | 28,150,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.48%` | `3,000.00` |
| `Live` | `Long` | `1.50` | 28,140,000.00 USD | 0.00 USD | 814.78 USD | `-64.00%` | `545.00` |
| `Live` | `Long` | `1.50` | 28,140,000.00 USD | 0.00 USD | 300.25 USD | `-63.76%` | `199.50` |
| `Live` | `Long` | `1.51` | 28,140,000.00 USD | 0.00 USD | 530,700.00 USD | `-63.52%` | `350,300.00` |
| `Live` | `Long` | `1.53` | 27,610,000.00 USD | 0.00 USD | 279.37 USD | `-63.04%` | `182.00` |
| `Live` | `Long` | `1.55` | 27,610,000.00 USD | 0.00 USD | 311.00 USD | `-62.56%` | `200.00` |
| `Live` | `Long` | `1.56` | 27,610,000.00 USD | 0.00 USD | 13,300.00 USD | `-62.31%` | `8,501.00` |
| `Live` | `Long` | `1.57` | 27,600,000.00 USD | 0.00 USD | 5,240.00 USD | `-62.07%` | `3,327.90` |
| `Live` | `Long` | `1.59` | 27,590,000.00 USD | 0.00 USD | 3,380.00 USD | `-61.59%` | `2,119.70` |
| `Live` | `Long` | `1.60` | 27,590,000.00 USD | 0.00 USD | 12,630.00 USD | `-61.35%` | `7,869.70` |
| `Live` | `Long` | `1.62` | 27,580,000.00 USD | 0.00 USD | 1,460.00 USD | `-60.87%` | `900.20` |
| `Live` | `Long` | `1.64` | 27,570,000.00 USD | 0.00 USD | 19,600.00 USD | `-60.63%` | `11,985.60` |
| `Live` | `Long` | `1.65` | 27,550,000.00 USD | 0.00 USD | 2,440.00 USD | `-60.39%` | `1,484.60` |
| `Live` | `Long` | `1.66` | 27,550,000.00 USD | 0.00 USD | 1,450.00 USD | `-60.15%` | `875.90` |
| `Live` | `Long` | `1.67` | 27,550,000.00 USD | 0.00 USD | 681.98 USD | `-59.91%` | `409.60` |
| `Live` | `Long` | `1.68` | 27,550,000.00 USD | 0.00 USD | 108.71 USD | `-59.67%` | `64.90` |
| `Live` | `Long` | `1.69` | 27,550,000.00 USD | 0.00 USD | 14,290.00 USD | `-59.42%` | `8,482.20` |
| `Live` | `Long` | `1.70` | 27,540,000.00 USD | 0.00 USD | 12,950.00 USD | `-59.18%` | `7,637.20` |
| `Live` | `Long` | `1.73` | 27,520,000.00 USD | 0.00 USD | 8,670.00 USD | `-58.46%` | `5,027.10` |
| `Live` | `Long` | `1.75` | 27,510,000.00 USD | 0.00 USD | 11,320.00 USD | `-57.74%` | `6,449.40` |
| `Live` | `Long` | `1.77` | 27,500,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.26%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 27,500,000.00 USD | 0.00 USD | 4,810.00 USD | `-57.02%` | `2,693.30` |
| `Live` | `Long` | `1.80` | 27,490,000.00 USD | 0.00 USD | 42,700.00 USD | `-56.54%` | `23,654.20` |
| `Live` | `Long` | `1.81` | 27,450,000.00 USD | 0.00 USD | 1,580.00 USD | `-56.29%` | `873.20` |
| `Live` | `Long` | `1.83` | 27,450,000.00 USD | 0.00 USD | 40,550.00 USD | `-55.81%` | `22,096.80` |
| `Live` | `Long` | `1.84` | 27,410,000.00 USD | 0.00 USD | 1,290.00 USD | `-55.57%` | `697.70` |
| `Live` | `Long` | `1.85` | 27,410,000.00 USD | 0.00 USD | 4,130.00 USD | `-55.33%` | `2,227.40` |
| `Live` | `Long` | `1.88` | 27,400,000.00 USD | 0.00 USD | 35,540.00 USD | `-54.85%` | `18,955.90` |
| `Live` | `Long` | `1.89` | 27,370,000.00 USD | 0.00 USD | 1,890.00 USD | `-54.61%` | `1,004.90` |
| `Live` | `Long` | `1.90` | 27,370,000.00 USD | 0.00 USD | 3,130.00 USD | `-54.37%` | `1,650.00` |
| `Live` | `Long` | `1.91` | 27,360,000.00 USD | 0.00 USD | 2,070.00 USD | `-54.13%` | `1,084.50` |
| `Live` | `Long` | `1.92` | 27,360,000.00 USD | 0.00 USD | 5,740.00 USD | `-53.89%` | `2,995.20` |
| `Live` | `Long` | `1.93` | 27,360,000.00 USD | 0.00 USD | 23,920.00 USD | `-53.65%` | `12,426.30` |
| `Live` | `Long` | `1.95` | 27,330,000.00 USD | 0.00 USD | 11,560.00 USD | `-53.16%` | `5,941.10` |
| `Live` | `Long` | `1.96` | 27,320,000.00 USD | 0.00 USD | 2,010.00 USD | `-52.92%` | `1,025.60` |
| `Live` | `Long` | `1.97` | 27,320,000.00 USD | 0.00 USD | 10,180.00 USD | `-52.68%` | `5,182.20` |
| `Live` | `Long` | `1.98` | 27,310,000.00 USD | 0.00 USD | 42,930.00 USD | `-52.44%` | `21,735.30` |
| `Live` | `Long` | `2.00` | 27,260,000.00 USD | 0.00 USD | 1,320.00 USD | `-51.96%` | `664.10` |
| `Live` | `Long` | `2.00` | 27,260,000.00 USD | 0.00 USD | 122,770.00 USD | `-51.72%` | `61,234.30` |
| `Live` | `Long` | `2.02` | 27,140,000.00 USD | 0.00 USD | 1,220.00 USD | `-51.48%` | `604.30` |
| `Live` | `Long` | `2.02` | 27,140,000.00 USD | 0.00 USD | 582.39 USD | `-51.24%` | `287.60` |
| `Live` | `Long` | `2.04` | 27,140,000.00 USD | 0.00 USD | 17,030.00 USD | `-51.00%` | `8,370.20` |
| `Live` | `Long` | `2.04` | 27,120,000.00 USD | 0.00 USD | 15,730.00 USD | `-50.76%` | `7,693.20` |
| `Live` | `Long` | `2.06` | 27,110,000.00 USD | 0.00 USD | 1,230.00 USD | `-50.52%` | `598.30` |
| `Live` | `Long` | `2.06` | 27,110,000.00 USD | 0.00 USD | 10,540.00 USD | `-50.27%` | `5,102.90` |
| `Live` | `Long` | `2.08` | 27,090,000.00 USD | 0.00 USD | 6,820.00 USD | `-50.03%` | `3,288.40` |
| `Live` | `Long` | `2.08` | 27,090,000.00 USD | 0.00 USD | 1,880.00 USD | `-49.79%` | `900.00` |
| `Live` | `Long` | `2.10` | 27,090,000.00 USD | 0.00 USD | 229,560.00 USD | `-49.31%` | `109,052.70` |
| `Live` | `Long` | `2.12` | 26,860,000.00 USD | 0.00 USD | 11,640.00 USD | `-49.07%` | `5,503.50` |
| `Live` | `Long` | `2.12` | 26,840,000.00 USD | 0.00 USD | 94,190.00 USD | `-48.83%` | `44,324.90` |
| `Live` | `Long` | `2.13` | 26,750,000.00 USD | 0.00 USD | 30,070.00 USD | `-48.59%` | `14,082.70` |
| `Live` | `Long` | `2.15` | 26,720,000.00 USD | 0.00 USD | 594.13 USD | `-48.11%` | `275.70` |
| `Live` | `Long` | `2.17` | 26,720,000.00 USD | 0.00 USD | 77,890.00 USD | `-47.87%` | `35,977.40` |
| `Live` | `Long` | `2.17` | 26,640,000.00 USD | 0.00 USD | 225,110.00 USD | `-47.63%` | `103,500.00` |
| `Live` | `Long` | `2.19` | 26,420,000.00 USD | 0.00 USD | 13,820.00 USD | `-47.38%` | `6,325.30` |
| `Live` | `Long` | `2.19` | 26,400,000.00 USD | 0.00 USD | 968.00 USD | `-47.14%` | `441.00` |
| `Live` | `Long` | `2.21` | 26,400,000.00 USD | 0.00 USD | 74,790.00 USD | `-46.90%` | `33,919.90` |
| `Live` | `Long` | `2.21` | 26,330,000.00 USD | 0.00 USD | 8,330.00 USD | `-46.66%` | `3,761.20` |
| `Live` | `Long` | `2.23` | 26,320,000.00 USD | 0.00 USD | 2,310.00 USD | `-46.42%` | `1,040.10` |
| `Live` | `Long` | `2.23` | 26,320,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.18%` | `473.60` |
| `Live` | `Long` | `2.25` | 26,320,000.00 USD | 0.00 USD | 42,920.00 USD | `-45.94%` | `19,117.30` |
| `Live` | `Long` | `2.25` | 26,270,000.00 USD | 0.00 USD | 116,500.00 USD | `-45.70%` | `51,661.60` |
| `Live` | `Long` | `2.27` | 26,160,000.00 USD | 0.00 USD | 2,270.00 USD | `-45.46%` | `1,000.00` |
| `Live` | `Long` | `2.27` | 26,150,000.00 USD | 0.00 USD | 748.70 USD | `-45.22%` | `329.10` |
| `Live` | `Long` | `2.29` | 26,150,000.00 USD | 0.00 USD | 13,570.00 USD | `-44.98%` | `5,939.00` |
| `Live` | `Long` | `2.29` | 26,140,000.00 USD | 0.00 USD | 3,530.00 USD | `-44.74%` | `1,536.90` |
| `Live` | `Long` | `2.31` | 26,140,000.00 USD | 0.00 USD | 6,600.00 USD | `-44.50%` | `2,864.70` |
| `Live` | `Long` | `2.31` | 26,130,000.00 USD | 0.00 USD | 2,310.00 USD | `-44.25%` | `999.40` |
| `Live` | `Long` | `2.33` | 26,130,000.00 USD | 0.00 USD | 2,650.00 USD | `-44.01%` | `1,140.30` |
| `Live` | `Long` | `2.33` | 26,120,000.00 USD | 0.00 USD | 2,670.00 USD | `-43.77%` | `1,145.40` |
| `Live` | `Long` | `2.35` | 26,120,000.00 USD | 0.00 USD | 74,090.00 USD | `-43.53%` | `31,593.90` |
| `Live` | `Long` | `2.35` | 26,050,000.00 USD | 0.00 USD | 5,680.00 USD | `-43.29%` | `2,412.80` |
| `Live` | `Long` | `2.37` | 26,040,000.00 USD | 0.00 USD | 35,930.00 USD | `-43.05%` | `15,194.10` |
| `Live` | `Long` | `2.38` | 26,010,000.00 USD | 0.00 USD | 422,720.00 USD | `-42.81%` | `177,988.30` |
| `Live` | `Long` | `2.38` | 25,580,000.00 USD | 0.00 USD | 1,970.00 USD | `-42.57%` | `827.70` |
| `Live` | `Long` | `2.40` | 25,580,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-42.33%` | `655,768.40` |
| `Live` | `Long` | `2.40` | 24,010,000.00 USD | 0.00 USD | 1,110.00 USD | `-42.09%` | `463.40` |
| `Live` | `Long` | `2.42` | 24,010,000.00 USD | 0.00 USD | 203,420.00 USD | `-41.85%` | `84,232.60` |
| `Live` | `Long` | `2.42` | 23,810,000.00 USD | 0.00 USD | 282,760.00 USD | `-41.61%` | `116,601.40` |
| `Live` | `Long` | `2.44` | 23,520,000.00 USD | 0.00 USD | 2,540.00 USD | `-41.36%` | `1,042.90` |
| `Live` | `Long` | `2.44` | 23,520,000.00 USD | 0.00 USD | 3,990.00 USD | `-41.12%` | `1,629.90` |
| `Live` | `Long` | `2.46` | 23,520,000.00 USD | 0.00 USD | 13,230.00 USD | `-40.88%` | `5,390.30` |
| `Live` | `Long` | `2.46` | 23,500,000.00 USD | 0.00 USD | 5,740.00 USD | `-40.64%` | `2,329.10` |
| `Live` | `Long` | `2.48` | 23,500,000.00 USD | 0.00 USD | 19,070.00 USD | `-40.40%` | `7,706.70` |
| `Live` | `Long` | `2.48` | 23,480,000.00 USD | 0.00 USD | 140,910.00 USD | `-40.16%` | `56,703.00` |
| `Live` | `Long` | `2.50` | 23,340,000.00 USD | 0.00 USD | 4,450.00 USD | `-39.92%` | `1,785.00` |
| `Live` | `Long` | `2.50` | 23,330,000.00 USD | 0.00 USD | 7,780.00 USD | `-39.68%` | `3,104.60` |
| `Live` | `Long` | `2.52` | 23,330,000.00 USD | 0.00 USD | 1,550.00 USD | `-39.44%` | `618.10` |
| `Live` | `Long` | `2.52` | 23,320,000.00 USD | 0.00 USD | 18,360.00 USD | `-39.20%` | `7,271.60` |
| `Live` | `Long` | `2.54` | 23,310,000.00 USD | 0.00 USD | 6,380.00 USD | `-38.96%` | `2,515.10` |
| `Live` | `Long` | `2.54` | 23,300,000.00 USD | 0.00 USD | 10,920.00 USD | `-38.72%` | `4,291.70` |
| `Live` | `Long` | `2.56` | 23,290,000.00 USD | 0.00 USD | 412,400.00 USD | `-38.48%` | `161,410.80` |
| `Live` | `Long` | `2.56` | 22,880,000.00 USD | 0.00 USD | 8,730.00 USD | `-38.23%` | `3,403.80` |
| `Live` | `Long` | `2.58` | 22,870,000.00 USD | 0.00 USD | 860.82 USD | `-37.99%` | `334.30` |
| `Live` | `Long` | `2.58` | 22,870,000.00 USD | 0.00 USD | 2,330,000.00 USD | `-37.75%` | `900,693.60` |
| `Live` | `Long` | `2.60` | 20,540,000.00 USD | 0.00 USD | 69,910.00 USD | `-37.51%` | `26,940.80` |
| `Live` | `Long` | `2.60` | 20,470,000.00 USD | 0.00 USD | 3,950.00 USD | `-37.27%` | `1,514.80` |
| `Live` | `Long` | `2.62` | 20,460,000.00 USD | 0.00 USD | 1,190.00 USD | `-37.03%` | `454.70` |
| `Live` | `Long` | `2.62` | 20,460,000.00 USD | 0.00 USD | 4,200.00 USD | `-36.79%` | `1,599.30` |
| `Live` | `Long` | `2.63` | 20,460,000.00 USD | 0.00 USD | 24,310.00 USD | `-36.55%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 20,430,000.00 USD | 0.00 USD | 9,840.00 USD | `-36.31%` | `3,718.80` |
| `Live` | `Long` | `2.65` | 20,420,000.00 USD | 0.00 USD | 18,510.00 USD | `-36.07%` | `6,972.60` |
| `Live` | `Long` | `2.67` | 20,410,000.00 USD | 0.00 USD | 4,680.00 USD | `-35.83%` | `1,757.80` |
| `Live` | `Long` | `2.67` | 20,400,000.00 USD | 0.00 USD | 375.84 USD | `-35.59%` | `140.50` |
| `Live` | `Long` | `2.69` | 20,400,000.00 USD | 0.00 USD | 4,860.00 USD | `-35.34%` | `1,809.60` |
| `Live` | `Long` | `2.69` | 20,400,000.00 USD | 0.00 USD | 4,300.00 USD | `-35.10%` | `1,594.60` |
| `Live` | `Long` | `2.71` | 20,390,000.00 USD | 0.00 USD | 132,990.00 USD | `-34.86%` | `49,165.10` |
| `Live` | `Long` | `2.71` | 20,260,000.00 USD | 0.00 USD | 19,350.00 USD | `-34.62%` | `7,127.50` |
| `Live` | `Long` | `2.73` | 20,240,000.00 USD | 0.00 USD | 38,030.00 USD | `-34.38%` | `13,955.90` |
| `Live` | `Long` | `2.73` | 20,200,000.00 USD | 0.00 USD | 3,350.00 USD | `-34.14%` | `1,225.80` |
| `Live` | `Long` | `2.75` | 20,200,000.00 USD | 0.00 USD | 42,880.00 USD | `-33.90%` | `15,621.60` |
| `Live` | `Long` | `2.75` | 20,160,000.00 USD | 0.00 USD | 154.83 USD | `-33.66%` | `56.20` |
| `Live` | `Long` | `2.77` | 20,160,000.00 USD | 0.00 USD | 3,880.00 USD | `-33.42%` | `1,402.20` |
| `Live` | `Long` | `2.77` | 20,150,000.00 USD | 0.00 USD | 1,360.00 USD | `-33.18%` | `491.60` |
| `Live` | `Long` | `2.79` | 20,150,000.00 USD | 0.00 USD | 214,990.00 USD | `-32.94%` | `77,195.60` |
| `Live` | `Long` | `2.79` | 19,940,000.00 USD | 0.00 USD | 10,470.00 USD | `-32.70%` | `3,746.80` |
| `Live` | `Long` | `2.81` | 19,920,000.00 USD | 0.00 USD | 14,230.00 USD | `-32.46%` | `5,074.80` |
| `Live` | `Long` | `2.83` | 19,910,000.00 USD | 0.00 USD | 7,890.00 USD | `-31.97%` | `2,793.40` |
| `Live` | `Long` | `2.83` | 19,900,000.00 USD | 0.00 USD | 2,760.00 USD | `-31.73%` | `972.50` |
| `Live` | `Long` | `2.85` | 19,900,000.00 USD | 0.00 USD | 367,060.00 USD | `-31.49%` | `129,020.70` |
| `Live` | `Long` | `2.85` | 19,530,000.00 USD | 0.00 USD | 3,550.00 USD | `-31.25%` | `1,241.90` |
| `Live` | `Long` | `2.87` | 19,530,000.00 USD | 0.00 USD | 8,140.00 USD | `-31.01%` | `2,842.80` |
| `Live` | `Long` | `2.88` | 19,520,000.00 USD | 0.00 USD | 929.20 USD | `-30.77%` | `323.20` |
| `Live` | `Long` | `2.88` | 19,520,000.00 USD | 0.00 USD | 7,370.00 USD | `-30.53%` | `2,554.60` |
| `Live` | `Long` | `2.90` | 19,510,000.00 USD | 0.00 USD | 13,780.00 USD | `-30.29%` | `4,759.90` |
| `Live` | `Long` | `2.90` | 19,500,000.00 USD | 0.00 USD | 213,920.00 USD | `-30.05%` | `73,636.90` |
| `Live` | `Long` | `2.92` | 19,280,000.00 USD | 0.00 USD | 85,170.00 USD | `-29.81%` | `29,216.30` |
| `Live` | `Long` | `2.92` | 19,200,000.00 USD | 0.00 USD | 3,960.00 USD | `-29.57%` | `1,353.70` |
| `Live` | `Long` | `2.94` | 19,200,000.00 USD | 0.00 USD | 155,560.00 USD | `-29.32%` | `53,001.10` |
| `Live` | `Long` | `2.94` | 19,040,000.00 USD | 0.00 USD | 1,010.00 USD | `-29.08%` | `341.80` |
| `Live` | `Long` | `2.96` | 19,040,000.00 USD | 0.00 USD | 166,480.00 USD | `-28.84%` | `56,338.50` |
| `Live` | `Long` | `2.96` | 18,870,000.00 USD | 0.00 USD | 15,880.00 USD | `-28.60%` | `5,354.20` |
| `Live` | `Long` | `2.98` | 18,860,000.00 USD | 0.00 USD | 180,710.00 USD | `-28.36%` | `60,743.30` |
| `Live` | `Long` | `2.98` | 18,680,000.00 USD | 0.00 USD | 387.15 USD | `-28.12%` | `129.70` |
| `Live` | `Long` | `3.00` | 18,680,000.00 USD | 0.00 USD | 2,000.00 USD | `-27.88%` | `666.40` |
| `Live` | `Long` | `3.00` | 18,670,000.00 USD | 0.00 USD | 375,800.00 USD | `-27.64%` | `125,059.60` |
| `Live` | `Long` | `3.02` | 18,300,000.00 USD | 0.00 USD | 11,290.00 USD | `-27.40%` | `3,743.00` |
| `Live` | `Long` | `3.02` | 18,290,000.00 USD | 0.00 USD | 20,840.00 USD | `-27.16%` | `6,890.30` |
| `Live` | `Long` | `3.04` | 18,270,000.00 USD | 0.00 USD | 8,140.00 USD | `-26.92%` | `2,681.80` |
| `Live` | `Long` | `3.04` | 18,260,000.00 USD | 0.00 USD | 106,550.00 USD | `-26.68%` | `34,993.20` |
| `Live` | `Long` | `3.06` | 18,150,000.00 USD | 0.00 USD | 28,140.00 USD | `-26.44%` | `9,212.20` |
| `Live` | `Long` | `3.06` | 18,120,000.00 USD | 0.00 USD | 115,550.00 USD | `-26.19%` | `37,700.70` |
| `Live` | `Long` | `3.08` | 18,010,000.00 USD | 0.00 USD | 13,160.00 USD | `-25.71%` | `4,267.00` |
| `Live` | `Long` | `3.10` | 17,990,000.00 USD | 0.00 USD | 4,930.00 USD | `-25.47%` | `1,594.30` |
| `Live` | `Long` | `3.10` | 17,990,000.00 USD | 0.00 USD | 45,890.00 USD | `-25.23%` | `14,778.70` |
| `Live` | `Long` | `3.12` | 17,940,000.00 USD | 0.00 USD | 22,050.00 USD | `-24.99%` | `7,077.10` |
| `Live` | `Long` | `3.12` | 17,920,000.00 USD | 0.00 USD | 8,330.00 USD | `-24.75%` | `2,665.50` |
| `Live` | `Long` | `3.13` | 17,910,000.00 USD | 0.00 USD | 38,380.00 USD | `-24.51%` | `12,243.80` |
| `Live` | `Long` | `3.15` | 17,870,000.00 USD | 0.00 USD | 5,540.00 USD | `-24.27%` | `1,761.70` |
| `Live` | `Long` | `3.15` | 17,870,000.00 USD | 0.00 USD | 214,120.00 USD | `-24.03%` | `67,868.10` |
| `Live` | `Long` | `3.17` | 17,660,000.00 USD | 0.00 USD | 83,740.00 USD | `-23.79%` | `26,458.10` |
| `Live` | `Long` | `3.17` | 17,570,000.00 USD | 0.00 USD | 7,320.00 USD | `-23.55%` | `2,307.00` |
| `Live` | `Long` | `3.19` | 17,560,000.00 USD | 0.00 USD | 7,310.00 USD | `-23.30%` | `2,296.40` |
| `Live` | `Long` | `3.21` | 17,560,000.00 USD | 0.00 USD | 134,880.00 USD | `-22.82%` | `42,085.30` |
| `Live` | `Long` | `3.21` | 17,420,000.00 USD | 0.00 USD | 20,150.00 USD | `-22.58%` | `6,268.70` |
| `Live` | `Long` | `3.23` | 17,400,000.00 USD | 0.00 USD | 27,070.00 USD | `-22.34%` | `8,394.40` |
| `Live` | `Long` | `3.23` | 17,370,000.00 USD | 0.00 USD | 71,220.00 USD | `-22.10%` | `22,015.80` |
| `Live` | `Long` | `3.25` | 17,300,000.00 USD | 0.00 USD | 17,490.00 USD | `-21.86%` | `5,389.70` |
| `Live` | `Long` | `3.25` | 17,290,000.00 USD | 0.00 USD | 58,930.00 USD | `-21.62%` | `18,104.60` |
| `Live` | `Long` | `3.27` | 17,230,000.00 USD | 0.00 USD | 37,970.00 USD | `-21.38%` | `11,629.90` |
| `Live` | `Long` | `3.27` | 17,190,000.00 USD | 0.00 USD | 836,670.00 USD | `-21.14%` | `255,472.50` |
| `Live` | `Long` | `3.29` | 16,350,000.00 USD | 0.00 USD | 2,680.00 USD | `-20.90%` | `815.20` |
| `Live` | `Long` | `3.29` | 16,350,000.00 USD | 0.00 USD | 134,710.00 USD | `-20.66%` | `40,883.70` |
| `Live` | `Long` | `3.31` | 16,210,000.00 USD | 0.00 USD | 138,120.00 USD | `-20.42%` | `41,792.30` |
| `Live` | `Long` | `3.31` | 16,080,000.00 USD | 0.00 USD | 22,780.00 USD | `-20.17%` | `6,872.70` |
| `Live` | `Long` | `3.33` | 16,050,000.00 USD | 0.00 USD | 32,280.00 USD | `-19.93%` | `9,709.60` |
| `Live` | `Long` | `3.33` | 16,020,000.00 USD | 0.00 USD | 63,800.00 USD | `-19.69%` | `19,130.90` |
| `Live` | `Long` | `3.35` | 15,960,000.00 USD | 0.00 USD | 577,220.00 USD | `-19.45%` | `172,561.70` |
| `Live` | `Long` | `3.35` | 15,380,000.00 USD | 0.00 USD | 3,860.00 USD | `-19.21%` | `1,151.10` |
| `Live` | `Long` | `3.37` | 15,380,000.00 USD | 0.00 USD | 2,020.00 USD | `-18.97%` | `600.20` |
| `Live` | `Long` | `3.38` | 15,370,000.00 USD | 0.00 USD | 36,990.00 USD | `-18.73%` | `10,961.20` |
| `Live` | `Long` | `3.38` | 15,340,000.00 USD | 0.00 USD | 44,450.00 USD | `-18.49%` | `13,131.00` |
| `Live` | `Long` | `3.40` | 15,290,000.00 USD | 0.00 USD | 5,390.00 USD | `-18.25%` | `1,586.80` |
| `Live` | `Long` | `3.40` | 15,290,000.00 USD | 0.00 USD | 76,100.00 USD | `-18.01%` | `22,350.30` |
| `Live` | `Long` | `3.42` | 15,210,000.00 USD | 0.00 USD | 190,450.00 USD | `-17.77%` | `55,769.20` |
| `Live` | `Long` | `3.42` | 15,020,000.00 USD | 0.00 USD | 93,990.00 USD | `-17.53%` | `27,442.60` |
| `Live` | `Long` | `3.44` | 14,930,000.00 USD | 0.00 USD | 28,770.00 USD | `-17.28%` | `8,375.20` |
| `Live` | `Long` | `3.44` | 14,900,000.00 USD | 0.00 USD | 2,340.00 USD | `-17.04%` | `678.40` |
| `Live` | `Long` | `3.46` | 14,900,000.00 USD | 0.00 USD | 14,550.00 USD | `-16.80%` | `4,212.00` |
| `Live` | `Long` | `3.46` | 14,880,000.00 USD | 0.00 USD | 6,650.00 USD | `-16.56%` | `1,919.90` |
| `Live` | `Long` | `3.48` | 14,880,000.00 USD | 0.00 USD | 112,700.00 USD | `-16.32%` | `32,431.60` |
| `Live` | `Long` | `3.48` | 14,760,000.00 USD | 0.00 USD | 687,230.00 USD | `-16.08%` | `197,197.60` |
| `Live` | `Long` | `3.50` | 14,080,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-15.84%` | `367,401.60` |
| `Live` | `Long` | `3.50` | 12,790,000.00 USD | 0.00 USD | 24,560.00 USD | `-15.60%` | `7,008.10` |
| `Live` | `Long` | `3.52` | 12,770,000.00 USD | 0.00 USD | 37,050.00 USD | `-15.36%` | `10,541.30` |
| `Live` | `Long` | `3.52` | 12,730,000.00 USD | 0.00 USD | 251,330.00 USD | `-15.12%` | `71,299.90` |
| `Live` | `Long` | `3.54` | 12,480,000.00 USD | 0.00 USD | 79,900.00 USD | `-14.88%` | `22,603.20` |
| `Live` | `Long` | `3.54` | 12,400,000.00 USD | 0.00 USD | 460,870.00 USD | `-14.64%` | `130,006.40` |
| `Live` | `Long` | `3.56` | 11,940,000.00 USD | 0.00 USD | 368,760.00 USD | `-14.40%` | `103,729.40` |
| `Live` | `Long` | `3.56` | 11,570,000.00 USD | 0.00 USD | 5,440.00 USD | `-14.15%` | `1,527.30` |
| `Live` | `Long` | `3.58` | 11,560,000.00 USD | 0.00 USD | 37,650.00 USD | `-13.91%` | `10,531.50` |
| `Live` | `Long` | `3.58` | 11,530,000.00 USD | 0.00 USD | 39,740.00 USD | `-13.67%` | `11,086.20` |
| `Live` | `Long` | `3.60` | 11,490,000.00 USD | 0.00 USD | 25,250.00 USD | `-13.43%` | `7,022.90` |
| `Live` | `Long` | `3.60` | 11,460,000.00 USD | 0.00 USD | 154,780.00 USD | `-13.19%` | `42,935.30` |
| `Live` | `Long` | `3.62` | 11,310,000.00 USD | 0.00 USD | 42,940.00 USD | `-12.95%` | `11,877.40` |
| `Live` | `Long` | `3.62` | 11,260,000.00 USD | 0.00 USD | 13,470.00 USD | `-12.71%` | `3,716.10` |
| `Live` | `Long` | `3.63` | 11,250,000.00 USD | 0.00 USD | 20,820.00 USD | `-12.47%` | `5,728.40` |
| `Live` | `Long` | `3.65` | 11,230,000.00 USD | 0.00 USD | 72,880.00 USD | `-12.23%` | `19,995.40` |
| `Live` | `Long` | `3.65` | 11,160,000.00 USD | 0.00 USD | 45,600.00 USD | `-11.99%` | `12,476.00` |
| `Live` | `Long` | `3.67` | 11,110,000.00 USD | 0.00 USD | 218,940.00 USD | `-11.75%` | `59,738.50` |
| `Live` | `Long` | `3.67` | 10,890,000.00 USD | 0.00 USD | 622,270.00 USD | `-11.51%` | `169,324.20` |
| `Live` | `Long` | `3.69` | 10,270,000.00 USD | 0.00 USD | 130,530.00 USD | `-11.26%` | `35,421.90` |
| `Live` | `Long` | `3.69` | 10,140,000.00 USD | 0.00 USD | 188,240.00 USD | `-11.02%` | `50,945.00` |
| `Live` | `Long` | `3.71` | 9,950,000.00 USD | 0.00 USD | 47,380.00 USD | `-10.78%` | `12,788.20` |
| `Live` | `Long` | `3.71` | 9,900,000.00 USD | 0.00 USD | 40,480.00 USD | `-10.54%` | `10,896.00` |
| `Live` | `Long` | `3.73` | 9,860,000.00 USD | 0.00 USD | 37,230.00 USD | `-10.30%` | `9,994.30` |
| `Live` | `Long` | `3.73` | 9,830,000.00 USD | 0.00 USD | 21,540.00 USD | `-10.06%` | `5,766.80` |
| `Live` | `Long` | `3.75` | 9,800,000.00 USD | 0.00 USD | 58,120.00 USD | `-9.82%` | `15,519.10` |
| `Live` | `Long` | `3.75` | 9,750,000.00 USD | 0.00 USD | 78,040.00 USD | `-9.58%` | `20,781.80` |
| `Live` | `Long` | `3.77` | 9,670,000.00 USD | 0.00 USD | 54,900.00 USD | `-9.34%` | `14,581.50` |
| `Live` | `Long` | `3.77` | 9,610,000.00 USD | 0.00 USD | 11,510.00 USD | `-9.10%` | `3,048.50` |
| `Live` | `Long` | `3.79` | 9,600,000.00 USD | 0.00 USD | 81,910.00 USD | `-8.86%` | `21,641.70` |
| `Live` | `Long` | `3.79` | 9,520,000.00 USD | 0.00 USD | 129,010.00 USD | `-8.62%` | `33,995.00` |
| `Live` | `Long` | `3.81` | 9,390,000.00 USD | 0.00 USD | 136,040.00 USD | `-8.38%` | `35,752.90` |
| `Live` | `Long` | `3.81` | 9,250,000.00 USD | 0.00 USD | 18,470.00 USD | `-8.13%` | `4,841.10` |
| `Live` | `Long` | `3.83` | 9,240,000.00 USD | 0.00 USD | 35,730.00 USD | `-7.89%` | `9,340.30` |
| `Live` | `Long` | `3.83` | 9,200,000.00 USD | 0.00 USD | 163,840.00 USD | `-7.65%` | `42,723.20` |
| `Live` | `Long` | `3.85` | 9,040,000.00 USD | 0.00 USD | 67,130.00 USD | `-7.41%` | `17,458.00` |
| `Live` | `Long` | `3.85` | 8,970,000.00 USD | 0.00 USD | 16,580.00 USD | `-7.17%` | `4,301.30` |
| `Live` | `Long` | `3.87` | 8,950,000.00 USD | 0.00 USD | 160,010.00 USD | `-6.93%` | `41,400.90` |
| `Live` | `Long` | `3.88` | 8,790,000.00 USD | 0.00 USD | 19,300.00 USD | `-6.69%` | `4,979.80` |
| `Live` | `Long` | `3.88` | 8,770,000.00 USD | 0.00 USD | 173,540.00 USD | `-6.45%` | `44,668.30` |
| `Live` | `Long` | `3.90` | 8,600,000.00 USD | 0.00 USD | 96,380.00 USD | `-6.21%` | `24,744.30` |
| `Live` | `Long` | `3.90` | 8,500,000.00 USD | 0.00 USD | 2,130.00 USD | `-5.97%` | `546.20` |
| `Live` | `Long` | `3.92` | 8,500,000.00 USD | 0.00 USD | 3,950,000.00 USD | `-5.73%` | `1,008,594.60` |
| `Live` | `Long` | `3.92` | 4,550,000.00 USD | 0.00 USD | 372,020.00 USD | `-5.49%` | `94,782.60` |
| `Live` | `Long` | `3.94` | 4,180,000.00 USD | 0.00 USD | 127,720.00 USD | `-5.24%` | `32,458.20` |
| `Live` | `Long` | `3.94` | 4,050,000.00 USD | 0.00 USD | 687,490.00 USD | `-5.00%` | `174,267.50` |
| `Live` | `Long` | `3.96` | 3,360,000.00 USD | 0.00 USD | 38,270.00 USD | `-4.76%` | `9,676.80` |
| `Live` | `Long` | `3.96` | 3,330,000.00 USD | 0.00 USD | 246,650.00 USD | `-4.52%` | `62,206.20` |
| `Live` | `Long` | `3.98` | 3,080,000.00 USD | 0.00 USD | 505,940.00 USD | `-4.28%` | `127,281.30` |
| `Live` | `Long` | `3.98` | 2,570,000.00 USD | 0.00 USD | 152,750.00 USD | `-4.04%` | `38,330.70` |
| `Live` | `Long` | `4.00` | 2,420,000.00 USD | 0.00 USD | 234,780.00 USD | `-3.80%` | `58,768.90` |
| `Live` | `Long` | `4.00` | 2,190,000.00 USD | 0.00 USD | 61,540.00 USD | `-3.56%` | `15,365.10` |
| `Live` | `Long` | `4.01` | 2,130,000.00 USD | 0.00 USD | 39,230.00 USD | `-3.32%` | `9,770.10` |
| `Live` | `Long` | `4.03` | 2,090,000.00 USD | 0.00 USD | 375,020.00 USD | `-3.08%` | `93,173.40` |
| `Live` | `Long` | `4.04` | 1,710,000.00 USD | 0.00 USD | 23,890.00 USD | `-2.84%` | `5,921.40` |
| `Live` | `Long` | `4.04` | 1,690,000.00 USD | 0.00 USD | 107,490.00 USD | `-2.60%` | `26,573.50` |
| `Live` | `Long` | `4.05` | 1,580,000.00 USD | 0.00 USD | 91,310.00 USD | `-2.36%` | `22,517.30` |
| `Live` | `Long` | `4.07` | 1,490,000.00 USD | 0.00 USD | 549,980.00 USD | `-2.11%` | `135,295.50` |
| `Live` | `Long` | `4.08` | 938,150.00 USD | 0.00 USD | 138,060.00 USD | `-1.87%` | `33,880.20` |
| `Live` | `Long` | `4.08` | 800,080.00 USD | 0.00 USD | 17,870.00 USD | `-1.63%` | `4,373.50` |
| `Live` | `Long` | `4.09` | 782,220.00 USD | 0.00 USD | 692,300.00 USD | `-1.39%` | `169,060.10` |
| `Live` | `Long` | `4.11` | 89,920.00 USD | 0.00 USD | 55,720.00 USD | `-1.15%` | `13,573.30` |
| `Live` | `Long` | `4.12` | 34,200.00 USD | 0.00 USD | 231.67 USD | `-0.91%` | `56.30` |
| `Live` | `Long` | `4.13` | 33,970.00 USD | 0.00 USD | 33,970.00 USD | `-0.43%` | `8,214.60` |
| `Live` | `Short` | `4.18` | 2,010.00 USD | 2,010.00 USD | 0.00 USD | `+0.78%` | `480.20` |
| `Live` | `Short` | `4.36` | 5,370.00 USD | 3,360.00 USD | 0.00 USD | `+4.87%` | `772.30` |
| `Live` | `Short` | `4.37` | 52,700.00 USD | 47,330.00 USD | 0.00 USD | `+5.11%` | `10,842.30` |
| `Live` | `Short` | `4.38` | 53,070.00 USD | 367.06 USD | 0.00 USD | `+5.35%` | `83.90` |
| `Live` | `Short` | `4.38` | 56,670.00 USD | 3,610.00 USD | 0.00 USD | `+5.59%` | `822.80` |
| `Live` | `Short` | `4.39` | 57,580.00 USD | 905.81 USD | 0.00 USD | `+5.83%` | `206.10` |
| `Live` | `Short` | `4.41` | 59,370.00 USD | 1,790.00 USD | 0.00 USD | `+6.07%` | `405.90` |
| `Live` | `Short` | `4.42` | 368,770.00 USD | 309,400.00 USD | 0.00 USD | `+6.31%` | `70,079.00` |
| `Live` | `Short` | `4.42` | 378,500.00 USD | 9,730.00 USD | 0.00 USD | `+6.55%` | `2,199.10` |
| `Live` | `Short` | `4.43` | 379,300.00 USD | 799.63 USD | 0.00 USD | `+6.80%` | `180.30` |
| `Live` | `Short` | `4.45` | 385,610.00 USD | 6,320.00 USD | 0.00 USD | `+7.04%` | `1,420.70` |
| `Live` | `Short` | `4.46` | 386,080.00 USD | 468.38 USD | 0.00 USD | `+7.52%` | `104.90` |
| `Live` | `Short` | `4.47` | 394,510.00 USD | 8,430.00 USD | 0.00 USD | `+7.76%` | `1,884.20` |
| `Live` | `Short` | `4.50` | 411,690.00 USD | 17,170.00 USD | 0.00 USD | `+8.24%` | `3,820.30` |
| `Live` | `Short` | `4.50` | 429,770.00 USD | 18,080.00 USD | 0.00 USD | `+8.48%` | `4,014.30` |
| `Live` | `Short` | `4.51` | 477,180.00 USD | 47,410.00 USD | 0.00 USD | `+8.72%` | `10,500.80` |
| `Live` | `Short` | `4.53` | 495,280.00 USD | 18,100.00 USD | 0.00 USD | `+8.96%` | `4,000.00` |
| `Live` | `Short` | `4.54` | 495,530.00 USD | 252.70 USD | 0.00 USD | `+9.44%` | `55.60` |
| `Live` | `Short` | `4.61` | 496,580.00 USD | 1,050.00 USD | 0.00 USD | `+10.89%` | `227.10` |
| `Live` | `Short` | `4.62` | 538,480.00 USD | 41,900.00 USD | 0.00 USD | `+11.37%` | `9,059.60` |
| `Live` | `Short` | `4.63` | 538,970.00 USD | 493.16 USD | 0.00 USD | `+11.61%` | `106.40` |
| `Live` | `Short` | `4.64` | 539,090.00 USD | 116.59 USD | 0.00 USD | `+11.85%` | `25.10` |
| `Live` | `Short` | `4.67` | 663,480.00 USD | 124,390.00 USD | 0.00 USD | `+12.33%` | `26,664.20` |
| `Live` | `Short` | `4.71` | 665,420.00 USD | 1,940.00 USD | 0.00 USD | `+13.30%` | `412.30` |
| `Live` | `Short` | `4.75` | 665,750.00 USD | 335.95 USD | 0.00 USD | `+14.26%` | `70.80` |
| `Live` | `Short` | `4.75` | 820,620.00 USD | 154,870.00 USD | 0.00 USD | `+14.50%` | `32,569.80` |
| `Live` | `Short` | `4.76` | 906,200.00 USD | 85,580.00 USD | 0.00 USD | `+14.74%` | `17,960.10` |
| `Live` | `Short` | `4.78` | 913,260.00 USD | 7,050.00 USD | 0.00 USD | `+14.98%` | `1,477.00` |
| `Live` | `Short` | `4.79` | 917,780.00 USD | 4,530.00 USD | 0.00 USD | `+15.22%` | `946.20` |
| `Live` | `Short` | `4.79` | 924,240.00 USD | 6,460.00 USD | 0.00 USD | `+15.46%` | `1,346.70` |
| `Live` | `Short` | `4.82` | 1,400,000.00 USD | 473,730.00 USD | 0.00 USD | `+15.95%` | `98,386.10` |
| `Live` | `Short` | `4.83` | 1,400,000.00 USD | 1,740.00 USD | 0.00 USD | `+16.19%` | `360.90` |
| `Live` | `Short` | `4.83` | 1,400,000.00 USD | 4,530.00 USD | 0.00 USD | `+16.43%` | `936.20` |
| `Live` | `Short` | `4.87` | 1,410,000.00 USD | 5,460.00 USD | 0.00 USD | `+17.15%` | `1,121.90` |
| `Live` | `Short` | `4.88` | 1,430,000.00 USD | 16,630.00 USD | 0.00 USD | `+17.39%` | `3,412.10` |
| `Live` | `Short` | `4.88` | 1,440,000.00 USD | 15,160.00 USD | 0.00 USD | `+17.63%` | `3,103.20` |
| `Live` | `Short` | `4.92` | 1,580,000.00 USD | 140,840.00 USD | 0.00 USD | `+18.35%` | `28,655.30` |
| `Live` | `Short` | `4.92` | 1,580,000.00 USD | 2,100.00 USD | 0.00 USD | `+18.59%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,580,000.00 USD | 556.67 USD | 0.00 USD | `+18.84%` | `112.80` |
| `Live` | `Short` | `4.96` | 1,590,000.00 USD | 342.89 USD | 0.00 USD | `+19.32%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,690,000.00 USD | 99,810.00 USD | 0.00 USD | `+19.80%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 1,900,000.00 USD | 210,290.00 USD | 0.00 USD | `+20.04%` | `42,183.80` |
| `Live` | `Short` | `5.00` | 1,900,000.00 USD | 339.66 USD | 0.00 USD | `+20.28%` | `68.00` |
| `Live` | `Short` | `5.04` | 1,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+21.48%` | `230.50` |
| `Live` | `Short` | `5.05` | 1,950,000.00 USD | 55,570.00 USD | 0.00 USD | `+21.73%` | `10,993.80` |
| `Live` | `Short` | `5.07` | 1,960,000.00 USD | 3,420.00 USD | 0.00 USD | `+21.97%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,960,000.00 USD | 4,130.00 USD | 0.00 USD | `+22.45%` | `812.00` |
| `Live` | `Short` | `5.12` | 1,960,000.00 USD | 2,560.00 USD | 0.00 USD | `+23.41%` | `500.00` |
| `Live` | `Short` | `5.13` | 1,960,000.00 USD | 1,080.00 USD | 0.00 USD | `+23.65%` | `210.70` |
| `Live` | `Short` | `5.14` | 2,050,000.00 USD | 82,200.00 USD | 0.00 USD | `+23.89%` | `15,976.20` |
| `Live` | `Short` | `5.17` | 2,050,000.00 USD | 317.65 USD | 0.00 USD | `+24.37%` | `61.50` |
| `Live` | `Short` | `5.17` | 2,050,000.00 USD | 3,620.00 USD | 0.00 USD | `+24.61%` | `700.00` |
| `Live` | `Short` | `5.21` | 2,950,000.00 USD | 898,120.00 USD | 0.00 USD | `+25.34%` | `172,549.20` |
| `Live` | `Short` | `5.22` | 3,020,000.00 USD | 72,110.00 USD | 0.00 USD | `+25.82%` | `13,800.00` |
| `Live` | `Short` | `5.24` | 3,040,000.00 USD | 21,060.00 USD | 0.00 USD | `+26.06%` | `4,022.20` |
| `Live` | `Short` | `5.25` | 3,040,000.00 USD | 143.71 USD | 0.00 USD | `+26.30%` | `27.40` |
| `Live` | `Short` | `5.25` | 3,040,000.00 USD | 288.50 USD | 0.00 USD | `+26.54%` | `54.90` |
| `Live` | `Short` | `5.26` | 3,050,000.00 USD | 5,610.00 USD | 0.00 USD | `+26.78%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 3,050,000.00 USD | 544.38 USD | 0.00 USD | `+27.02%` | `103.20` |
| `Live` | `Short` | `5.29` | 3,050,000.00 USD | 257.38 USD | 0.00 USD | `+27.26%` | `48.70` |
| `Live` | `Short` | `5.29` | 3,050,000.00 USD | 114.37 USD | 0.00 USD | `+27.50%` | `21.60` |
| `Live` | `Short` | `5.30` | 3,050,000.00 USD | 1,140.00 USD | 0.00 USD | `+27.75%` | `214.20` |
| `Live` | `Short` | `5.32` | 3,050,000.00 USD | 718.59 USD | 0.00 USD | `+27.99%` | `135.20` |
| `Live` | `Short` | `5.33` | 3,080,000.00 USD | 29,250.00 USD | 0.00 USD | `+28.23%` | `5,493.40` |
| `Live` | `Short` | `5.34` | 3,100,000.00 USD | 19,710.00 USD | 0.00 USD | `+28.71%` | `3,686.80` |
| `Live` | `Short` | `5.36` | 3,120,000.00 USD | 25,310.00 USD | 0.00 USD | `+28.95%` | `4,726.70` |
| `Live` | `Short` | `5.37` | 3,170,000.00 USD | 41,910.00 USD | 0.00 USD | `+29.19%` | `7,811.90` |
| `Live` | `Short` | `5.38` | 3,230,000.00 USD | 60,180.00 USD | 0.00 USD | `+29.43%` | `11,196.20` |
| `Live` | `Short` | `5.39` | 3,250,000.00 USD | 20,300.00 USD | 0.00 USD | `+29.91%` | `3,762.90` |
| `Live` | `Short` | `5.41` | 3,280,000.00 USD | 35,680.00 USD | 0.00 USD | `+30.15%` | `6,601.20` |
| `Live` | `Short` | `5.43` | 3,280,000.00 USD | 962.54 USD | 0.00 USD | `+30.88%` | `177.10` |
| `Live` | `Short` | `5.45` | 3,280,000.00 USD | 1,050.00 USD | 0.00 USD | `+31.12%` | `192.10` |
| `Live` | `Short` | `5.47` | 3,280,000.00 USD | 627.98 USD | 0.00 USD | `+31.84%` | `114.70` |
| `Live` | `Short` | `5.50` | 3,360,000.00 USD | 77,760.00 USD | 0.00 USD | `+32.32%` | `14,151.00` |
| `Live` | `Short` | `5.50` | 3,360,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.56%` | `250.00` |
| `Live` | `Short` | `5.51` | 3,400,000.00 USD | 38,800.00 USD | 0.00 USD | `+32.80%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 3,400,000.00 USD | 209.22 USD | 0.00 USD | `+33.28%` | `37.80` |
| `Live` | `Short` | `5.57` | 3,410,000.00 USD | 8,670.00 USD | 0.00 USD | `+34.01%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 3,470,000.00 USD | 62,420.00 USD | 0.00 USD | `+34.49%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 3,540,000.00 USD | 64,190.00 USD | 0.00 USD | `+34.73%` | `11,472.40` |
| `Live` | `Short` | `5.61` | 3,540,000.00 USD | 6,190.00 USD | 0.00 USD | `+34.97%` | `1,103.80` |
| `Live` | `Short` | `5.62` | 3,840,000.00 USD | 300,420.00 USD | 0.00 USD | `+35.21%` | `53,503.40` |
| `Live` | `Short` | `5.64` | 3,900,000.00 USD | 56,450.00 USD | 0.00 USD | `+35.93%` | `10,000.00` |
| `Live` | `Short` | `5.67` | 3,900,000.00 USD | 942.09 USD | 0.00 USD | `+36.41%` | `166.30` |
| `Live` | `Short` | `5.67` | 3,900,000.00 USD | 334.26 USD | 0.00 USD | `+36.65%` | `58.90` |
| `Live` | `Short` | `5.68` | 3,970,000.00 USD | 66,300.00 USD | 0.00 USD | `+36.90%` | `11,661.80` |
| `Live` | `Short` | `5.70` | 3,970,000.00 USD | 2,010.00 USD | 0.00 USD | `+37.14%` | `353.10` |
| `Live` | `Short` | `5.71` | 3,970,000.00 USD | 2,130.00 USD | 0.00 USD | `+37.62%` | `372.40` |
| `Live` | `Short` | `5.75` | 3,980,000.00 USD | 4,580.00 USD | 0.00 USD | `+38.34%` | `796.90` |
| `Live` | `Short` | `5.75` | 3,980,000.00 USD | 286.02 USD | 0.00 USD | `+38.58%` | `49.70` |
| `Live` | `Short` | `5.79` | 3,980,000.00 USD | 2,700.00 USD | 0.00 USD | `+39.30%` | `466.00` |
| `Live` | `Short` | `5.80` | 4,040,000.00 USD | 55,580.00 USD | 0.00 USD | `+39.79%` | `9,574.70` |
| `Live` | `Short` | `5.83` | 4,040,000.00 USD | 128.37 USD | 0.00 USD | `+40.51%` | `22.00` |
| `Live` | `Short` | `5.84` | 4,040,000.00 USD | 199.31 USD | 0.00 USD | `+40.75%` | `34.10` |
| `Live` | `Short` | `5.86` | 4,040,000.00 USD | 370.62 USD | 0.00 USD | `+40.99%` | `63.30` |
| `Live` | `Short` | `5.88` | 4,310,000.00 USD | 271,610.00 USD | 0.00 USD | `+41.47%` | `46,230.70` |
| `Live` | `Short` | `5.88` | 4,310,000.00 USD | 190.67 USD | 0.00 USD | `+41.71%` | `32.40` |
| `Live` | `Short` | `5.89` | 4,400,000.00 USD | 88,590.00 USD | 0.00 USD | `+41.95%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 4,400,000.00 USD | 189.28 USD | 0.00 USD | `+42.43%` | `32.00` |
| `Live` | `Short` | `5.95` | 4,400,000.00 USD | 1,400.00 USD | 0.00 USD | `+43.16%` | `234.80` |
| `Live` | `Short` | `5.96` | 4,400,000.00 USD | 486.74 USD | 0.00 USD | `+43.64%` | `81.60` |
| `Live` | `Short` | `6.00` | 4,400,000.00 USD | 1,830.00 USD | 0.00 USD | `+44.36%` | `305.00` |
| `Live` | `Short` | `6.03` | 4,430,000.00 USD | 24,380.00 USD | 0.00 USD | `+45.08%` | `4,046.90` |
| `Live` | `Short` | `6.07` | 4,430,000.00 USD | 740.54 USD | 0.00 USD | `+46.05%` | `122.10` |
| `Live` | `Short` | `6.08` | 4,430,000.00 USD | 5,920.00 USD | 0.00 USD | `+46.53%` | `973.10` |
| `Live` | `Short` | `6.09` | 4,470,000.00 USD | 37,510.00 USD | 0.00 USD | `+46.77%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 4,490,000.00 USD | 24,160.00 USD | 0.00 USD | `+47.73%` | `3,938.70` |
| `Live` | `Short` | `6.17` | 4,500,000.00 USD | 1,910.00 USD | 0.00 USD | `+48.45%` | `310.00` |
| `Live` | `Short` | `6.17` | 4,500,000.00 USD | 308.75 USD | 0.00 USD | `+48.69%` | `50.00` |
| `Live` | `Short` | `6.21` | 4,500,000.00 USD | 1,540.00 USD | 0.00 USD | `+49.42%` | `247.70` |
| `Live` | `Short` | `6.25` | 4,500,000.00 USD | 7,300.00 USD | 0.00 USD | `+50.38%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 4,510,000.00 USD | 439.10 USD | 0.00 USD | `+50.62%` | `70.20` |
| `Live` | `Short` | `6.28` | 4,510,000.00 USD | 397.84 USD | 0.00 USD | `+51.10%` | `63.40` |
| `Live` | `Short` | `6.32` | 4,510,000.00 USD | 310.70 USD | 0.00 USD | `+52.07%` | `49.20` |
| `Live` | `Short` | `6.33` | 4,510,000.00 USD | 1,270.00 USD | 0.00 USD | `+52.55%` | `200.90` |
| `Live` | `Short` | `6.34` | 4,510,000.00 USD | 214.46 USD | 0.00 USD | `+52.79%` | `33.80` |
| `Live` | `Short` | `6.37` | 4,510,000.00 USD | 113.93 USD | 0.00 USD | `+53.27%` | `17.90` |
| `Live` | `Short` | `6.38` | 4,880,000.00 USD | 369,650.00 USD | 0.00 USD | `+53.51%` | `57,983.60` |
| `Live` | `Short` | `6.38` | 4,880,000.00 USD | 2,000.00 USD | 0.00 USD | `+53.75%` | `312.80` |
| `Live` | `Short` | `6.41` | 4,880,000.00 USD | 3,780.00 USD | 0.00 USD | `+54.23%` | `590.10` |
| `Live` | `Short` | `6.42` | 4,890,000.00 USD | 8,700.00 USD | 0.00 USD | `+54.47%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 4,890,000.00 USD | 346.95 USD | 0.00 USD | `+54.71%` | `54.00` |
| `Live` | `Short` | `6.43` | 4,930,000.00 USD | 41,340.00 USD | 0.00 USD | `+54.96%` | `6,424.10` |
| `Live` | `Short` | `6.45` | 4,940,000.00 USD | 5,270.00 USD | 0.00 USD | `+55.20%` | `818.40` |
| `Live` | `Short` | `6.46` | 4,950,000.00 USD | 7,150.00 USD | 0.00 USD | `+55.44%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 4,990,000.00 USD | 47,710.00 USD | 0.00 USD | `+55.68%` | `7,379.60` |
| `Live` | `Short` | `6.47` | 5,000,000.00 USD | 2,560.00 USD | 0.00 USD | `+55.92%` | `394.70` |
| `Live` | `Short` | `6.51` | 5,000,000.00 USD | 831.97 USD | 0.00 USD | `+56.88%` | `127.70` |
| `Live` | `Short` | `6.54` | 6,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+57.60%` | `290,268.40` |
| `Live` | `Short` | `6.55` | 6,900,000.00 USD | 1,930.00 USD | 0.00 USD | `+57.85%` | `294.70` |
| `Live` | `Short` | `6.58` | 6,990,000.00 USD | 87,890.00 USD | 0.00 USD | `+58.33%` | `13,367.10` |
| `Live` | `Short` | `6.59` | 6,990,000.00 USD | 418.78 USD | 0.00 USD | `+58.81%` | `63.50` |
| `Live` | `Short` | `6.62` | 7,040,000.00 USD | 51,780.00 USD | 0.00 USD | `+59.29%` | `7,827.40` |
| `Live` | `Short` | `6.66` | 7,050,000.00 USD | 13,340.00 USD | 0.00 USD | `+60.25%` | `2,003.90` |
| `Live` | `Short` | `6.67` | 7,050,000.00 USD | 803.13 USD | 0.00 USD | `+60.49%` | `120.50` |
| `Live` | `Short` | `6.67` | 7,050,000.00 USD | 200.25 USD | 0.00 USD | `+60.73%` | `30.00` |
| `Live` | `Short` | `6.68` | 7,090,000.00 USD | 35,590.00 USD | 0.00 USD | `+60.98%` | `5,323.40` |
| `Live` | `Short` | `6.71` | 7,100,000.00 USD | 10,770.00 USD | 0.00 USD | `+61.46%` | `1,606.90` |
| `Live` | `Short` | `6.71` | 7,120,000.00 USD | 15,540.00 USD | 0.00 USD | `+61.70%` | `2,314.50` |
| `Live` | `Short` | `6.72` | 7,900,000.00 USD | 789,370.00 USD | 0.00 USD | `+61.94%` | `117,377.80` |
| `Live` | `Short` | `6.74` | 7,910,000.00 USD | 5,130.00 USD | 0.00 USD | `+62.18%` | `761.90` |
| `Live` | `Short` | `6.75` | 7,910,000.00 USD | 1,690.00 USD | 0.00 USD | `+62.42%` | `250.00` |
| `Live` | `Short` | `6.75` | 9,160,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+62.66%` | `184,501.00` |
| `Live` | `Short` | `6.84` | 9,160,000.00 USD | 753.63 USD | 0.00 USD | `+64.83%` | `110.10` |
| `Live` | `Short` | `6.87` | 9,160,000.00 USD | 3,960.00 USD | 0.00 USD | `+65.31%` | `577.50` |
| `Live` | `Short` | `6.89` | 9,230,000.00 USD | 68,950.00 USD | 0.00 USD | `+66.03%` | `10,000.00` |
| `Live` | `Short` | `6.91` | 9,230,000.00 USD | 189.89 USD | 0.00 USD | `+66.27%` | `27.50` |
| `Live` | `Short` | `6.92` | 11,660,000.00 USD | 2,420,000.00 USD | 0.00 USD | `+66.75%` | `350,156.10` |
| `Live` | `Short` | `6.95` | 11,690,000.00 USD | 38,370.00 USD | 0.00 USD | `+67.24%` | `5,525.30` |
| `Live` | `Short` | `6.99` | 11,700,000.00 USD | 664.27 USD | 0.00 USD | `+68.20%` | `95.10` |
| `Live` | `Short` | `7.00` | 11,700,000.00 USD | 1,160.00 USD | 0.00 USD | `+68.68%` | `165.80` |
| `Live` | `Short` | `7.04` | 11,700,000.00 USD | 558.67 USD | 0.00 USD | `+69.64%` | `79.30` |
| `Live` | `Short` | `7.08` | 11,700,000.00 USD | 670.95 USD | 0.00 USD | `+70.61%` | `94.70` |
| `Live` | `Short` | `7.09` | 11,700,000.00 USD | 699.57 USD | 0.00 USD | `+70.85%` | `98.60` |
| `Live` | `Short` | `7.21` | 11,710,000.00 USD | 13,560.00 USD | 0.00 USD | `+73.74%` | `1,879.60` |
| `Live` | `Short` | `7.22` | 11,780,000.00 USD | 63,550.00 USD | 0.00 USD | `+73.98%` | `8,796.10` |
| `Live` | `Short` | `7.24` | 11,780,000.00 USD | 4,910.00 USD | 0.00 USD | `+74.22%` | `679.30` |
| `Live` | `Short` | `7.29` | 13,150,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+75.42%` | `188,000.00` |
| `Live` | `Short` | `7.33` | 13,150,000.00 USD | 1,320.00 USD | 0.00 USD | `+76.63%` | `180.00` |
| `Live` | `Short` | `7.38` | 13,240,000.00 USD | 90,250.00 USD | 0.00 USD | `+77.83%` | `12,220.40` |
| `Live` | `Short` | `7.43` | 13,260,000.00 USD | 16,640.00 USD | 0.00 USD | `+79.04%` | `2,237.40` |
| `Live` | `Short` | `7.45` | 13,270,000.00 USD | 14,890.00 USD | 0.00 USD | `+79.28%` | `2,000.00` |
| `Live` | `Short` | `7.46` | 13,380,000.00 USD | 107,860.00 USD | 0.00 USD | `+79.52%` | `14,467.60` |
| `Live` | `Short` | `7.50` | 23,410,000.00 USD | 10,030,000.00 USD | 0.00 USD | `+80.72%` | `1,336,000.00` |
| `Live` | `Short` | `7.53` | 23,410,000.00 USD | 1,610.00 USD | 0.00 USD | `+81.20%` | `214.00` |
| `Live` | `Short` | `7.57` | 31,270,000.00 USD | 7,860,000.00 USD | 0.00 USD | `+82.17%` | `1,039,604.60` |
| `Live` | `Short` | `7.58` | 31,280,000.00 USD | 2,630.00 USD | 0.00 USD | `+82.65%` | `347.20` |
| `Live` | `Short` | `7.63` | 31,300,000.00 USD | 19,210.00 USD | 0.00 USD | `+83.85%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 31,300,000.00 USD | 491.45 USD | 0.00 USD | `+84.33%` | `64.20` |
| `Live` | `Short` | `7.67` | 31,300,000.00 USD | 360.25 USD | 0.00 USD | `+84.57%` | `47.00` |
| `Live` | `Short` | `7.72` | 31,300,000.00 USD | 161.45 USD | 0.00 USD | `+86.02%` | `20.90` |
| `Live` | `Short` | `7.75` | 31,620,000.00 USD | 327,090.00 USD | 0.00 USD | `+86.50%` | `42,232.50` |
| `Live` | `Short` | `7.78` | 31,700,000.00 USD | 72,540.00 USD | 0.00 USD | `+87.22%` | `9,330.00` |
| `Live` | `Short` | `7.79` | 31,700,000.00 USD | 2,920.00 USD | 0.00 USD | `+87.46%` | `375.00` |
| `Live` | `Short` | `7.80` | 31,730,000.00 USD | 32,560.00 USD | 0.00 USD | `+87.95%` | `4,171.50` |
| `Live` | `Short` | `7.87` | 31,730,000.00 USD | 2,980.00 USD | 0.00 USD | `+89.39%` | `378.70` |
| `Live` | `Short` | `7.92` | 31,740,000.00 USD | 1,800.00 USD | 0.00 USD | `+90.84%` | `226.70` |
| `Live` | `Short` | `7.95` | 31,740,000.00 USD | 6,120.00 USD | 0.00 USD | `+91.32%` | `769.80` |
| `Live` | `Short` | `7.96` | 31,880,000.00 USD | 134,240.00 USD | 0.00 USD | `+91.80%` | `16,854.30` |
| `Live` | `Short` | `7.99` | 31,880,000.00 USD | 399.25 USD | 0.00 USD | `+92.28%` | `50.00` |
| `Live` | `Short` | `8.03` | 32,310,000.00 USD | 435,420.00 USD | 0.00 USD | `+93.24%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 32,310,000.00 USD | 797.63 USD | 0.00 USD | `+94.21%` | `98.90` |
| `Live` | `Short` | `8.14` | 32,310,000.00 USD | 983.92 USD | 0.00 USD | `+96.13%` | `120.80` |
| `Live` | `Short` | `8.15` | 32,310,000.00 USD | 190.01 USD | 0.00 USD | `+96.37%` | `23.30` |
| `Live` | `Short` | `8.18` | 32,320,000.00 USD | 362.97 USD | 0.00 USD | `+96.86%` | `44.40` |
| `Live` | `Short` | `8.22` | 32,320,000.00 USD | 103.64 USD | 0.00 USD | `+98.06%` | `12.60` |
| `Live` | `Short` | `8.23` | 32,340,000.00 USD | 24,700.00 USD | 0.00 USD | `+98.30%` | `3,000.00` |
| `Live` | `Short` | `8.26` | 32,360,000.00 USD | 21,470.00 USD | 0.00 USD | `+98.78%` | `2,601.00` |
| `Live` | `Short` | `8.27` | 32,450,000.00 USD | 87,280.00 USD | 0.00 USD | `+99.02%` | `10,560.20` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.8250` | 2,970,000.00 USD | 0.00 USD | 209.80 USD | `-80.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,970,000.00 USD | 0.00 USD | 585.51 USD | `-75.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,960,000.00 USD | 0.00 USD | 331.54 USD | `-67.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,960,000.00 USD | 0.00 USD | 345.25 USD | `-67.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,960,000.00 USD | 0.00 USD | 5,640.00 USD | `-66.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,960,000.00 USD | 0.00 USD | 997.29 USD | `-66.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,960,000.00 USD | 0.00 USD | 139.83 USD | `-63.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,960,000.00 USD | 0.00 USD | 113.28 USD | `-63.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,960,000.00 USD | 0.00 USD | 4,000.00 USD | `-62.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,950,000.00 USD | 0.00 USD | 324.22 USD | `-62.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,950,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,950,000.00 USD | 0.00 USD | 739.67 USD | `-61.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,950,000.00 USD | 0.00 USD | 1,740.00 USD | `-60.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,950,000.00 USD | 0.00 USD | 6,260.00 USD | `-60.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,940,000.00 USD | 0.00 USD | 167.50 USD | `-59.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,940,000.00 USD | 0.00 USD | 669.02 USD | `-59.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,940,000.00 USD | 0.00 USD | 105.88 USD | `-58.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,940,000.00 USD | 0.00 USD | 172.50 USD | `-58.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,940,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,930,000.00 USD | 0.00 USD | 722.00 USD | `-56.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,930,000.00 USD | 0.00 USD | 259.00 USD | `-56.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,930,000.00 USD | 0.00 USD | 103.84 USD | `-56.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,930,000.00 USD | 0.00 USD | 109.00 USD | `-55.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,930,000.00 USD | 0.00 USD | 222.19 USD | `-54.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,930,000.00 USD | 0.00 USD | 10,280.00 USD | `-54.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,920,000.00 USD | 0.00 USD | 558.36 USD | `-54.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,920,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,910,000.00 USD | 0.00 USD | 222.14 USD | `-53.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,910,000.00 USD | 0.00 USD | 279.50 USD | `-53.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,910,000.00 USD | 0.00 USD | 197.50 USD | `-52.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,910,000.00 USD | 0.00 USD | 935.66 USD | `-51.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,910,000.00 USD | 0.00 USD | 19,170.00 USD | `-51.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,890,000.00 USD | 0.00 USD | 3,020.00 USD | `-51.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,890,000.00 USD | 0.00 USD | 214.52 USD | `-50.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,890,000.00 USD | 0.00 USD | 1,200.00 USD | `-50.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,890,000.00 USD | 0.00 USD | 578.41 USD | `-50.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,890,000.00 USD | 0.00 USD | 18,070.00 USD | `-49.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,870,000.00 USD | 0.00 USD | 13,980.00 USD | `-49.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,860,000.00 USD | 0.00 USD | 107.23 USD | `-49.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,860,000.00 USD | 0.00 USD | 1,590.00 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,850,000.00 USD | 0.00 USD | 6,970.00 USD | `-48.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,850,000.00 USD | 0.00 USD | 310.32 USD | `-48.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,850,000.00 USD | 0.00 USD | 1,170.00 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,850,000.00 USD | 0.00 USD | 576.18 USD | `-47.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,850,000.00 USD | 0.00 USD | 295.67 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,850,000.00 USD | 0.00 USD | 2,940.00 USD | `-46.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,840,000.00 USD | 0.00 USD | 812.68 USD | `-46.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,840,000.00 USD | 0.00 USD | 1,440.00 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,840,000.00 USD | 0.00 USD | 490.14 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,840,000.00 USD | 0.00 USD | 6,270.00 USD | `-45.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,830,000.00 USD | 0.00 USD | 478.06 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,830,000.00 USD | 0.00 USD | 540.88 USD | `-45.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,830,000.00 USD | 0.00 USD | 1,210.00 USD | `-45.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,830,000.00 USD | 0.00 USD | 759.76 USD | `-44.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,830,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,820,000.00 USD | 0.00 USD | 3,690.00 USD | `-44.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,820,000.00 USD | 0.00 USD | 3,050.00 USD | `-44.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,810,000.00 USD | 0.00 USD | 467.00 USD | `-43.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,810,000.00 USD | 0.00 USD | 506.75 USD | `-43.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,810,000.00 USD | 0.00 USD | 214.27 USD | `-43.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,810,000.00 USD | 0.00 USD | 428.69 USD | `-42.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,810,000.00 USD | 0.00 USD | 322.45 USD | `-42.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,810,000.00 USD | 0.00 USD | 108.25 USD | `-42.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,810,000.00 USD | 0.00 USD | 3,900.00 USD | `-42.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,810,000.00 USD | 0.00 USD | 799.04 USD | `-41.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,810,000.00 USD | 0.00 USD | 6,830.00 USD | `-41.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,800,000.00 USD | 0.00 USD | 137.16 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,800,000.00 USD | 0.00 USD | 504.41 USD | `-40.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,800,000.00 USD | 0.00 USD | 963.93 USD | `-40.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,800,000.00 USD | 0.00 USD | 3,690.00 USD | `-39.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,790,000.00 USD | 0.00 USD | 541.98 USD | `-39.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,790,000.00 USD | 0.00 USD | 108.75 USD | `-38.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,790,000.00 USD | 0.00 USD | 766.55 USD | `-38.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,790,000.00 USD | 0.00 USD | 1,010.00 USD | `-38.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,790,000.00 USD | 0.00 USD | 1,100.00 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,790,000.00 USD | 0.00 USD | 100.04 USD | `-37.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,790,000.00 USD | 0.00 USD | 178,060.00 USD | `-37.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,610,000.00 USD | 0.00 USD | 5,090.00 USD | `-37.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,610,000.00 USD | 0.00 USD | 226.57 USD | `-35.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,610,000.00 USD | 0.00 USD | 104.98 USD | `-35.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,610,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,600,000.00 USD | 0.00 USD | 107.21 USD | `-34.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,600,000.00 USD | 0.00 USD | 197.37 USD | `-33.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,600,000.00 USD | 0.00 USD | 8,390.00 USD | `-33.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,590,000.00 USD | 0.00 USD | 108.39 USD | `-33.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,590,000.00 USD | 0.00 USD | 435.95 USD | `-33.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,590,000.00 USD | 0.00 USD | 217.23 USD | `-32.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,590,000.00 USD | 0.00 USD | 437.98 USD | `-32.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,590,000.00 USD | 0.00 USD | 2,000.00 USD | `-32.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,590,000.00 USD | 0.00 USD | 8,250.00 USD | `-31.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,580,000.00 USD | 0.00 USD | 109.53 USD | `-31.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,580,000.00 USD | 0.00 USD | 437.00 USD | `-30.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,580,000.00 USD | 0.00 USD | 746.06 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,580,000.00 USD | 0.00 USD | 2,900.00 USD | `-30.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,570,000.00 USD | 0.00 USD | 4,870.00 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,570,000.00 USD | 0.00 USD | 696.98 USD | `-29.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,570,000.00 USD | 0.00 USD | 358.90 USD | `-29.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,570,000.00 USD | 0.00 USD | 15,370.00 USD | `-29.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,550,000.00 USD | 0.00 USD | 523.32 USD | `-28.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,550,000.00 USD | 0.00 USD | 2,330.00 USD | `-28.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,550,000.00 USD | 0.00 USD | 14,600.00 USD | `-27.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,540,000.00 USD | 0.00 USD | 1,020.00 USD | `-27.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,540,000.00 USD | 0.00 USD | 345.76 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,530,000.00 USD | 0.00 USD | 214.57 USD | `-26.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,530,000.00 USD | 0.00 USD | 109.42 USD | `-26.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 2,530,000.00 USD | 0.00 USD | 721.58 USD | `-25.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,530,000.00 USD | 0.00 USD | 9,300.00 USD | `-25.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,520,000.00 USD | 0.00 USD | 8,530.00 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,520,000.00 USD | 0.00 USD | 104.69 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,520,000.00 USD | 0.00 USD | 315.69 USD | `-24.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,520,000.00 USD | 0.00 USD | 214.17 USD | `-24.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,520,000.00 USD | 0.00 USD | 641.10 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,510,000.00 USD | 0.00 USD | 212.06 USD | `-23.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,510,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,510,000.00 USD | 0.00 USD | 218.81 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,510,000.00 USD | 0.00 USD | 25,410.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,490,000.00 USD | 0.00 USD | 144.67 USD | `-22.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,490,000.00 USD | 0.00 USD | 27,380.00 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,460,000.00 USD | 0.00 USD | 2,170.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,460,000.00 USD | 0.00 USD | 104.81 USD | `-21.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,460,000.00 USD | 0.00 USD | 1,150.00 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,460,000.00 USD | 0.00 USD | 1,070.00 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,460,000.00 USD | 0.00 USD | 20,120.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,440,000.00 USD | 0.00 USD | 240.67 USD | `-20.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,440,000.00 USD | 0.00 USD | 465.50 USD | `-19.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,430,000.00 USD | 0.00 USD | 6,590.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,430,000.00 USD | 0.00 USD | 505.76 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,430,000.00 USD | 0.00 USD | 73,220.00 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,350,000.00 USD | 0.00 USD | 12,850.00 USD | `-18.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,340,000.00 USD | 0.00 USD | 8,490.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,330,000.00 USD | 0.00 USD | 12,580.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,320,000.00 USD | 0.00 USD | 675.83 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,320,000.00 USD | 0.00 USD | 506.22 USD | `-17.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 171.75 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 2,550.00 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,320,000.00 USD | 0.00 USD | 3,760.00 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,310,000.00 USD | 0.00 USD | 344.07 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,310,000.00 USD | 0.00 USD | 1,950.00 USD | `-15.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,310,000.00 USD | 0.00 USD | 84,110.00 USD | `-15.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,230,000.00 USD | 0.00 USD | 10,750.00 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,220,000.00 USD | 0.00 USD | 2,150.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,210,000.00 USD | 0.00 USD | 5,980.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,210,000.00 USD | 0.00 USD | 173.48 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,210,000.00 USD | 0.00 USD | 333.68 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,210,000.00 USD | 0.00 USD | 72,860.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,130,000.00 USD | 0.00 USD | 179.25 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,130,000.00 USD | 0.00 USD | 643.50 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,130,000.00 USD | 0.00 USD | 3,370.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,130,000.00 USD | 0.00 USD | 632.99 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,130,000.00 USD | 0.00 USD | 172.19 USD | `-12.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,130,000.00 USD | 0.00 USD | 14,620.00 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,110,000.00 USD | 0.00 USD | 179.33 USD | `-12.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,110,000.00 USD | 0.00 USD | 3,900.00 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,110,000.00 USD | 0.00 USD | 174.09 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,110,000.00 USD | 0.00 USD | 367.50 USD | `-11.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,110,000.00 USD | 0.00 USD | 4,490.00 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,110,000.00 USD | 0.00 USD | 4,370.00 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,100,000.00 USD | 0.00 USD | 17,740.00 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 2,080,000.00 USD | 0.00 USD | 9,600.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,070,000.00 USD | 0.00 USD | 1,470.00 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 2,070,000.00 USD | 0.00 USD | 45,640.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,030,000.00 USD | 0.00 USD | 28,820.00 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 2,000,000.00 USD | 0.00 USD | 18,660.00 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,980,000.00 USD | 0.00 USD | 7,500.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,970,000.00 USD | 0.00 USD | 3,940.00 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,970,000.00 USD | 0.00 USD | 359.57 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,970,000.00 USD | 0.00 USD | 1,900.00 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,970,000.00 USD | 0.00 USD | 17,490.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,950,000.00 USD | 0.00 USD | 18,470.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,930,000.00 USD | 0.00 USD | 1,560.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,930,000.00 USD | 0.00 USD | 2,990.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,930,000.00 USD | 0.00 USD | 2,770.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,920,000.00 USD | 0.00 USD | 3,990.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,920,000.00 USD | 0.00 USD | 2,640.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,920,000.00 USD | 0.00 USD | 14,700.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,900,000.00 USD | 0.00 USD | 7,170.00 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,890,000.00 USD | 0.00 USD | 1,310.00 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,890,000.00 USD | 0.00 USD | 29,660.00 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,860,000.00 USD | 0.00 USD | 187.53 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 1,860,000.00 USD | 0.00 USD | 1,690.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,860,000.00 USD | 0.00 USD | 1,420.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 1,860,000.00 USD | 0.00 USD | 1,060.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,860,000.00 USD | 0.00 USD | 16,710.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 1,840,000.00 USD | 0.00 USD | 1,960.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,840,000.00 USD | 0.00 USD | 11,240.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 1,830,000.00 USD | 0.00 USD | 99,380.00 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,730,000.00 USD | 0.00 USD | 13,060.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 1,720,000.00 USD | 0.00 USD | 540,720.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 1,180,000.00 USD | 0.00 USD | 5,440.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 1,170,000.00 USD | 0.00 USD | 4,400.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,170,000.00 USD | 0.00 USD | 3,870.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 1,160,000.00 USD | 0.00 USD | 9,120.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 1,150,000.00 USD | 0.00 USD | 3,020.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 1,150,000.00 USD | 0.00 USD | 30,340.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,120,000.00 USD | 0.00 USD | 31,150.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 1,090,000.00 USD | 0.00 USD | 164,220.00 USD | `-1.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 923,900.00 USD | 0.00 USD | 131,300.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 792,610.00 USD | 0.00 USD | 719,590.00 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 73,020.00 USD | 0.00 USD | 56,080.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 16,940.00 USD | 0.00 USD | 4,570.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 12,370.00 USD | 0.00 USD | 1,320.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 11,050.00 USD | 0.00 USD | 11,050.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 36,660.00 USD | 36,660.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 39,490.00 USD | 2,830.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 70,850.00 USD | 31,360.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 75,860.00 USD | 5,010.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 483,820.00 USD | 407,970.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 615,640.00 USD | 131,820.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 666,930.00 USD | 51,290.00 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 671,070.00 USD | 4,140.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 671,260.00 USD | 186.34 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 671,490.00 USD | 230.93 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 678,080.00 USD | 6,590.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 678,920.00 USD | 842.34 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 712,660.00 USD | 33,740.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 721,440.00 USD | 8,770.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 723,840.00 USD | 2,400.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 735,540.00 USD | 11,700.00 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 752,100.00 USD | 16,560.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 754,520.00 USD | 2,420.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 756,250.00 USD | 1,730.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 758,680.00 USD | 2,430.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 759,460.00 USD | 785.21 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 790,570.00 USD | 31,110.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 836,060.00 USD | 45,490.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 837,500.00 USD | 1,440.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 849,760.00 USD | 12,260.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 901,120.00 USD | 51,360.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 903,640.00 USD | 2,520.00 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 905,600.00 USD | 1,960.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 905,910.00 USD | 301.58 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 906,790.00 USD | 889.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 951,340.00 USD | 44,550.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 951,470.00 USD | 125.02 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 955,550.00 USD | 4,080.00 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,020,000.00 USD | 62,510.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,030,000.00 USD | 10,850.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,080,000.00 USD | 50,840.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,090,000.00 USD | 13,100.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,140,000.00 USD | 50,660.00 USD | 0.00 USD | `+8.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,270,000.00 USD | 122,520.00 USD | 0.00 USD | `+9.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,270,000.00 USD | 1,610.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,270,000.00 USD | 1,190.00 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,270,000.00 USD | 702.55 USD | 0.00 USD | `+9.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,320,000.00 USD | 45,750.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,320,000.00 USD | 1,860.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,330,000.00 USD | 17,590.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,340,000.00 USD | 8,450.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,350,000.00 USD | 10,970.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,360,000.00 USD | 1,830.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,360,000.00 USD | 1,100.00 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,360,000.00 USD | 750.17 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,380,000.00 USD | 21,240.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,390,000.00 USD | 11,660.00 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,390,000.00 USD | 104.25 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,420,000.00 USD | 25,760.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,420,000.00 USD | 152.12 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,860,000.00 USD | 442,040.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,080,000.00 USD | 217,980.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,080,000.00 USD | 2,650.00 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,190,000.00 USD | 106,750.00 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,190,000.00 USD | 6,160.00 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,220,000.00 USD | 28,480.00 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,230,000.00 USD | 13,030.00 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,240,000.00 USD | 2,640.00 USD | 0.00 USD | `+14.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,070,000.00 USD | 832,330.00 USD | 0.00 USD | `+15.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,070,000.00 USD | 559.58 USD | 0.00 USD | `+15.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,240,000.00 USD | 174,240.00 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,260,000.00 USD | 20,970.00 USD | 0.00 USD | `+15.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,280,000.00 USD | 13,730.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,280,000.00 USD | 1,080.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,290,000.00 USD | 11,760.00 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,320,000.00 USD | 24,760.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,340,000.00 USD | 22,380.00 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,350,000.00 USD | 10,610.00 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,360,000.00 USD | 10,730.00 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,360,000.00 USD | 4,060.00 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,480,000.00 USD | 119,930.00 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,480,000.00 USD | 287.53 USD | 0.00 USD | `+18.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,500,000.00 USD | 13,180.00 USD | 0.00 USD | `+18.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,510,000.00 USD | 8,600.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,510,000.00 USD | 313.51 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,510,000.00 USD | 5,070.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,560,000.00 USD | 47,350.00 USD | 0.00 USD | `+19.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,560,000.00 USD | 187.06 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,650,000.00 USD | 95,460.00 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,670,000.00 USD | 11,390.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,700,000.00 USD | 37,080.00 USD | 0.00 USD | `+20.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,730,000.00 USD | 25,080.00 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,730,000.00 USD | 5,030.00 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,910,000.00 USD | 172,540.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,910,000.00 USD | 104.94 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,960,000.00 USD | 55,790.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,970,000.00 USD | 4,730.00 USD | 0.00 USD | `+21.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,050,000.00 USD | 88,030.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,940,000.00 USD | 882,870.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,940,000.00 USD | 547.20 USD | 0.00 USD | `+22.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,990,000.00 USD | 53,320.00 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 5,000,000.00 USD | 12,790.00 USD | 0.00 USD | `+23.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 5,000,000.00 USD | 113.26 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 5,020,000.00 USD | 15,400.00 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 5,020,000.00 USD | 3,670.00 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 5,020,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,030,000.00 USD | 575.38 USD | 0.00 USD | `+24.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,030,000.00 USD | 327.58 USD | 0.00 USD | `+24.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 5,030,000.00 USD | 163.85 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 5,150,000.00 USD | 120,080.00 USD | 0.00 USD | `+25.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,180,000.00 USD | 33,260.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 5,180,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 5,310,000.00 USD | 125,620.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 5,310,000.00 USD | 2,620.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,310,000.00 USD | 537.61 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 5,760,000.00 USD | 449,510.00 USD | 0.00 USD | `+26.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 5,760,000.00 USD | 5,540.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 5,770,000.00 USD | 589.22 USD | 0.00 USD | `+27.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,770,000.00 USD | 733.03 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 5,770,000.00 USD | 423.60 USD | 0.00 USD | `+27.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,780,000.00 USD | 10,930.00 USD | 0.00 USD | `+27.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,780,000.00 USD | 381.09 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,780,000.00 USD | 961.16 USD | 0.00 USD | `+28.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,780,000.00 USD | 1,570.00 USD | 0.00 USD | `+28.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,790,000.00 USD | 6,220.00 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,790,000.00 USD | 759.87 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,790,000.00 USD | 225.33 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,790,000.00 USD | 438.60 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,790,000.00 USD | 4,990.00 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,830,000.00 USD | 41,030.00 USD | 0.00 USD | `+29.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,960,000.00 USD | 127,430.00 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,960,000.00 USD | 270.75 USD | 0.00 USD | `+30.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,960,000.00 USD | 935.27 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,980,000.00 USD | 12,920.00 USD | 0.00 USD | `+31.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,990,000.00 USD | 12,220.00 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,210,000.00 USD | 219,220.00 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,240,000.00 USD | 35,450.00 USD | 0.00 USD | `+31.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,290,000.00 USD | 44,780.00 USD | 0.00 USD | `+32.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,290,000.00 USD | 1,180.00 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,370,000.00 USD | 82,470.00 USD | 0.00 USD | `+32.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,380,000.00 USD | 5,600.00 USD | 0.00 USD | `+32.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,420,000.00 USD | 45,680.00 USD | 0.00 USD | `+33.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,440,000.00 USD | 18,790.00 USD | 0.00 USD | `+33.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,520,000.00 USD | 74,260.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,560,000.00 USD | 46,110.00 USD | 0.00 USD | `+33.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,580,000.00 USD | 16,410.00 USD | 0.00 USD | `+34.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,580,000.00 USD | 5,560.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,600,000.00 USD | 20,540.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,600,000.00 USD | 384.94 USD | 0.00 USD | `+34.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,610,000.00 USD | 811.60 USD | 0.00 USD | `+34.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,610,000.00 USD | 2,190.00 USD | 0.00 USD | `+35.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,610,000.00 USD | 581.53 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,610,000.00 USD | 491.11 USD | 0.00 USD | `+35.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,610,000.00 USD | 3,290.00 USD | 0.00 USD | `+36.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,610,000.00 USD | 281.55 USD | 0.00 USD | `+36.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,620,000.00 USD | 6,590.00 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,620,000.00 USD | 5,860.00 USD | 0.00 USD | `+37.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,740,000.00 USD | 116,610.00 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,740,000.00 USD | 2,210.00 USD | 0.00 USD | `+37.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,750,000.00 USD | 5,720.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,770,000.00 USD | 24,820.00 USD | 0.00 USD | `+38.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,780,000.00 USD | 2,430.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,780,000.00 USD | 286.94 USD | 0.00 USD | `+39.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,780,000.00 USD | 7,120.00 USD | 0.00 USD | `+39.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,780,000.00 USD | 687.91 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,790,000.00 USD | 1,970.00 USD | 0.00 USD | `+40.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,790,000.00 USD | 1,020.00 USD | 0.00 USD | `+40.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,790,000.00 USD | 1,150.00 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,790,000.00 USD | 1,190.00 USD | 0.00 USD | `+40.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,790,000.00 USD | 1,770.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,790,000.00 USD | 3,450.00 USD | 0.00 USD | `+41.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,800,000.00 USD | 345.45 USD | 0.00 USD | `+41.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,850,000.00 USD | 58,220.00 USD | 0.00 USD | `+42.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,860,000.00 USD | 1,670.00 USD | 0.00 USD | `+42.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,860,000.00 USD | 1,400.00 USD | 0.00 USD | `+42.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,990,000.00 USD | 138,320.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,030,000.00 USD | 32,530.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,030,000.00 USD | 5,440.00 USD | 0.00 USD | `+43.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,040,000.00 USD | 8,940.00 USD | 0.00 USD | `+43.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,160,000.00 USD | 119,340.00 USD | 0.00 USD | `+44.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,160,000.00 USD | 3,000.00 USD | 0.00 USD | `+44.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,360,000.00 USD | 194,290.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,370,000.00 USD | 13,610.00 USD | 0.00 USD | `+44.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,460,000.00 USD | 90,380.00 USD | 0.00 USD | `+45.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,460,000.00 USD | 2,100.00 USD | 0.00 USD | `+45.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,470,000.00 USD | 3,300.00 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,470,000.00 USD | 2,550.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,470,000.00 USD | 425.76 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,470,000.00 USD | 2,030.00 USD | 0.00 USD | `+46.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,480,000.00 USD | 4,120.00 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,480,000.00 USD | 2,000.00 USD | 0.00 USD | `+46.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,540,000.00 USD | 61,050.00 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,540,000.00 USD | 1,610.00 USD | 0.00 USD | `+47.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,540,000.00 USD | 1,200.00 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,550,000.00 USD | 11,620.00 USD | 0.00 USD | `+47.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,560,000.00 USD | 1,940.00 USD | 0.00 USD | `+48.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,560,000.00 USD | 1,410.00 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,560,000.00 USD | 4,010.00 USD | 0.00 USD | `+48.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,570,000.00 USD | 3,960.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,570,000.00 USD | 3,830.00 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,640,000.00 USD | 66,120.00 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,640,000.00 USD | 1,890.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,640,000.00 USD | 195.46 USD | 0.00 USD | `+49.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,640,000.00 USD | 1,540.00 USD | 0.00 USD | `+50.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,640,000.00 USD | 3,670.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,650,000.00 USD | 3,680.00 USD | 0.00 USD | `+51.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,650,000.00 USD | 7,370.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,650,000.00 USD | 412.37 USD | 0.00 USD | `+52.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,650,000.00 USD | 602.77 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,660,000.00 USD | 449.79 USD | 0.00 USD | `+52.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,660,000.00 USD | 1,760.00 USD | 0.00 USD | `+53.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,660,000.00 USD | 3,560.00 USD | 0.00 USD | `+53.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,660,000.00 USD | 3,230.00 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,670,000.00 USD | 5,120.00 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,670,000.00 USD | 613.26 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,670,000.00 USD | 1,310.00 USD | 0.00 USD | `+56.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,700,000.00 USD | 31,270.00 USD | 0.00 USD | `+56.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,700,000.00 USD | 234.54 USD | 0.00 USD | `+56.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,720,000.00 USD | 14,070.00 USD | 0.00 USD | `+57.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,720,000.00 USD | 1,630.00 USD | 0.00 USD | `+58.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,720,000.00 USD | 2,390.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,720,000.00 USD | 1,620.00 USD | 0.00 USD | `+59.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,730,000.00 USD | 3,220.00 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,730,000.00 USD | 450.55 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,730,000.00 USD | 3,060.00 USD | 0.00 USD | `+60.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,730,000.00 USD | 1,930.00 USD | 0.00 USD | `+60.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,730,000.00 USD | 3,070.00 USD | 0.00 USD | `+61.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,740,000.00 USD | 1,920.00 USD | 0.00 USD | `+61.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,740,000.00 USD | 3,120.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,740,000.00 USD | 1,550.00 USD | 0.00 USD | `+62.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,740,000.00 USD | 3,080.00 USD | 0.00 USD | `+63.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,740,000.00 USD | 647.56 USD | 0.00 USD | `+63.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,750,000.00 USD | 1,420.00 USD | 0.00 USD | `+63.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,750,000.00 USD | 2,130.00 USD | 0.00 USD | `+64.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,750,000.00 USD | 3,140.00 USD | 0.00 USD | `+64.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,750,000.00 USD | 342.25 USD | 0.00 USD | `+64.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,750,000.00 USD | 1,830.00 USD | 0.00 USD | `+65.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,760,000.00 USD | 2,990.00 USD | 0.00 USD | `+65.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,760,000.00 USD | 2,970.00 USD | 0.00 USD | `+66.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,760,000.00 USD | 324.54 USD | 0.00 USD | `+66.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,760,000.00 USD | 504.21 USD | 0.00 USD | `+67.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,760,000.00 USD | 166.00 USD | 0.00 USD | `+67.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,760,000.00 USD | 4,190.00 USD | 0.00 USD | `+68.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,780,000.00 USD | 15,610.00 USD | 0.00 USD | `+68.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,780,000.00 USD | 1,750.00 USD | 0.00 USD | `+68.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,780,000.00 USD | 2,860.00 USD | 0.00 USD | `+69.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,780,000.00 USD | 264.31 USD | 0.00 USD | `+71.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,790,000.00 USD | 599.34 USD | 0.00 USD | `+71.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,790,000.00 USD | 193.19 USD | 0.00 USD | `+72.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,790,000.00 USD | 3,950.00 USD | 0.00 USD | `+73.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,790,000.00 USD | 1,940.00 USD | 0.00 USD | `+73.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,950,000.00 USD | 160,550.00 USD | 0.00 USD | `+74.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,950,000.00 USD | 1,290.00 USD | 0.00 USD | `+75.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,950,000.00 USD | 905.60 USD | 0.00 USD | `+76.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,960,000.00 USD | 1,730.00 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,960,000.00 USD | 1,710.00 USD | 0.00 USD | `+77.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,970,000.00 USD | 7,870.00 USD | 0.00 USD | `+77.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,970,000.00 USD | 630.05 USD | 0.00 USD | `+78.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,970,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,970,000.00 USD | 2,610.00 USD | 0.00 USD | `+78.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,980,000.00 USD | 6,000.00 USD | 0.00 USD | `+80.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,980,000.00 USD | 1,620.00 USD | 0.00 USD | `+81.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,980,000.00 USD | 4,640.00 USD | 0.00 USD | `+82.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,980,000.00 USD | 371.88 USD | 0.00 USD | `+83.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,990,000.00 USD | 2,510.00 USD | 0.00 USD | `+83.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,990,000.00 USD | 380.68 USD | 0.00 USD | `+84.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,990,000.00 USD | 133.12 USD | 0.00 USD | `+85.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,990,000.00 USD | 1,490.00 USD | 0.00 USD | `+86.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,990,000.00 USD | 1,470.00 USD | 0.00 USD | `+87.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 8,000,000.00 USD | 11,170.00 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 8,030,000.00 USD | 34,360.00 USD | 0.00 USD | `+87.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 8,030,000.00 USD | 399.35 USD | 0.00 USD | `+88.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 8,030,000.00 USD | 100.29 USD | 0.00 USD | `+88.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 8,040,000.00 USD | 1,550.00 USD | 0.00 USD | `+89.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 8,050,000.00 USD | 10,610.00 USD | 0.00 USD | `+91.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 8,050,000.00 USD | 309.43 USD | 0.00 USD | `+92.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 8,110,000.00 USD | 59,860.00 USD | 0.00 USD | `+92.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,190,000.00 USD | 81,310.00 USD | 0.00 USD | `+93.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,190,000.00 USD | 1,390.00 USD | 0.00 USD | `+95.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,190,000.00 USD | 216.90 USD | 0.00 USD | `+97.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,190,000.00 USD | 738.45 USD | 0.00 USD | `+97.58%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.62` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 147,810.00 USD | 44,040.00 USD | 165,960.00 USD |
| `7D` | `3.63` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 50,840.00 USD | 8,120.00 USD | 156.86 USD |
| `7D` | `3.64` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,030.00 USD |
| `1D` | `3.65` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 710.37 USD | 5,040.00 USD | 331.49 USD |
| `7D` | `3.65` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,210.00 USD |
| `1D` | `3.66` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 291.38 USD | 0.00 USD | 6.38 USD |
| `7D` | `3.66` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,450.00 USD |
| `1D` | `3.67` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 16,270.00 USD | 3,070.00 USD | 11,440.00 USD |
| `7D` | `3.67` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,500.00 USD |
| `1D` | `3.69` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 9.86 USD |
| `7D` | `3.69` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 27,750.00 USD | 0.00 USD | 59,940.00 USD |
| `1D` | `3.70` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 38,920.00 USD | 0.00 USD | 55,000.00 USD |
| `7D` | `3.70` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,080.00 USD |
| `1D` | `3.71` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 430.40 USD | 0.00 USD | 6.22 USD |
| `7D` | `3.71` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 50,620.00 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.72` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 186.40 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 425.03 USD | 0.00 USD | 546.73 USD |
| `1D` | `3.73` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,130.00 USD |
| `7D` | `3.73` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,540.00 USD |
| `7D` | `3.74` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 128,440.00 USD | 40,020.00 USD | 123,850.00 USD |
| `1D` | `3.75` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,710.00 USD |
| `1D` | `3.76` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,230.00 USD |
| `1D` | `3.77` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 187.12 USD | 5,330.00 USD | 1,990.00 USD |
| `7D` | `3.77` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 13,170.00 USD | 8,090.00 USD | 22,820.00 USD |
| `1D` | `3.78` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 106.91 USD | 6,570.00 USD | 29,170.00 USD |
| `7D` | `3.78` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,920.00 USD |
| `1D` | `3.79` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 3,890.00 USD |
| `7D` | `3.79` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 49,420.00 USD | 0.00 USD | 39,090.00 USD |
| `1D` | `3.80` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 4,050.00 USD | 0.00 USD | 3,610.00 USD |
| `7D` | `3.80` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 1,530.00 USD | 18,170.00 USD | 16,860.00 USD |
| `1D` | `3.81` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 53,440.00 USD | 0.00 USD | 13,250.00 USD |
| `7D` | `3.81` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 810.67 USD |
| `1D` | `3.82` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 0.00 USD | 11,960.00 USD | 176.51 USD |
| `7D` | `3.82` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 352.15 USD | 18,900.00 USD | 18,440.00 USD |
| `7D` | `3.83` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `1D` | `3.85` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 604.20 USD | 6,330.00 USD | 141.64 USD |
| `7D` | `3.85` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 252.34 USD |
| `1D` | `3.86` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 1,450.00 USD | 12,320.00 USD | 53,950.00 USD |
| `7D` | `3.86` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 2,220.00 USD | 0.00 USD | 72,830.00 USD |
| `1D` | `3.87` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 1,690.00 USD | 11,800.00 USD | 0.00 USD |
| `7D` | `3.87` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 57,040.00 USD | 0.00 USD | 31,570.00 USD |
| `1D` | `3.88` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 105,540.00 USD | 6,860.00 USD | 41,580.00 USD |
| `7D` | `3.88` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 106,950.00 USD | 8,890.00 USD | 102,520.00 USD |
| `1D` | `3.89` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 112,840.00 USD | 37,150.00 USD | 23,350.00 USD |
| `7D` | `3.89` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 1,210.00 USD | 50,710.00 USD | 869.98 USD |
| `1D` | `3.90` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 335.10 USD | 10,910.00 USD | 20,820.00 USD |
| `7D` | `3.90` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 171,750.00 USD | 28,250.00 USD | 50,280.00 USD |
| `1D` | `3.91` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | 35,760.00 USD | 38,020.00 USD |
| `7D` | `3.91` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 1,280.00 USD | 25,680.00 USD | 47,020.00 USD |
| `1D` | `3.92` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 147,700.00 USD | 26,030.00 USD | 31,900.00 USD |
| `7D` | `3.92` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 90,780.00 USD | 41,330.00 USD | 82,250.00 USD |
| `1D` | `3.93` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 0.00 USD | 21,500.00 USD | 11,960.00 USD |
| `7D` | `3.93` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 51,660.00 USD | 20,780.00 USD | 51,350.00 USD |
| `1D` | `3.94` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 4,810.00 USD | 6,420.00 USD | 16,990.00 USD |
| `7D` | `3.94` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 82,440.00 USD | 31,050.00 USD | 128,560.00 USD |
| `1D` | `3.95` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 95,940.00 USD | 5,610.00 USD | 97,310.00 USD |
| `7D` | `3.95` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,170.00 USD |
| `1D` | `3.96` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 36,860.00 USD | 29,270.00 USD | 36,950.00 USD |
| `7D` | `3.96` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 52,720.00 USD | 15,590.00 USD | 126,240.00 USD |
| `1D` | `3.97` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 156,730.00 USD | 52,430.00 USD | 105,360.00 USD |
| `7D` | `3.97` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 231,790.00 USD | 102,960.00 USD | 270,770.00 USD |
| `1D` | `3.98` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 132,570.00 USD | 30,290.00 USD | 14,820.00 USD |
| `7D` | `3.98` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,130.00 USD |
| `1D` | `3.99` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 349,680.00 USD | 106,190.00 USD | 136,510.00 USD |
| `7D` | `3.99` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 63,200.00 USD | 103,210.00 USD | 79,740.00 USD |
| `1D` | `4.00` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,480.00 USD |
| `7D` | `4.00` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,250.00 USD |
| `1D` | `4.01` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 112,570.00 USD | 56,050.00 USD | 73,690.00 USD |
| `7D` | `4.01` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 392,150.00 USD | 94,720.00 USD | 437,920.00 USD |
| `1D` | `4.02` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 60,540.00 USD | 33,270.00 USD | 108,730.00 USD |
| `7D` | `4.02` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 279,800.00 USD | 88,330.00 USD | 253,220.00 USD |
| `1D` | `4.03` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 189,730.00 USD | 55,650.00 USD | 267,230.00 USD |
| `7D` | `4.03` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 250,870.00 USD | 45,290.00 USD | 148,940.00 USD |
| `1D` | `4.04` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 105,670.00 USD | 48,960.00 USD | 211,380.00 USD |
| `7D` | `4.04` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 98,660.00 USD | 65,670.00 USD | 120,630.00 USD |
| `1D` | `4.05` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 78,330.00 USD | 25,880.00 USD | 95,770.00 USD |
| `7D` | `4.05` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,910.00 USD |
| `1D` | `4.06` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 190,260.00 USD | 0.00 USD | 126,130.00 USD |
| `7D` | `4.06` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 305,310.00 USD | 72,410.00 USD | 188,740.00 USD |
| `1D` | `4.07` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 175,040.00 USD | 44,930.00 USD | 22,900.00 USD |
| `7D` | `4.07` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD |
| `1D` | `4.08` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 510,570.00 USD | 253,070.00 USD | 189,410.00 USD |
| `7D` | `4.08` | 615,940.00 USD | 0.00 USD | 615,940.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `1D` | `4.09` | 509,850.00 USD | 0.00 USD | 509,850.00 USD | 10,540.00 USD | 99,090.00 USD | 1,500.00 USD |
| `7D` | `4.09` | 259,310.00 USD | 0.00 USD | 259,310.00 USD | 134,630.00 USD | 83,890.00 USD | 40,790.00 USD |
| `1D` | `4.10` | 398,710.00 USD | 0.00 USD | 398,710.00 USD | 7,600.00 USD | 10,080.00 USD | 509.39 USD |
| `7D` | `4.10` | 618,690.00 USD | 618,690.00 USD | 0.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD |
| `7D` | `4.10` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 158,760.00 USD | 118,310.00 USD | 341,620.00 USD |
| `1D` | `4.11` | 380,520.00 USD | 0.00 USD | 380,520.00 USD | 10,200.00 USD | 59,250.00 USD | 1,270.00 USD |
| `7D` | `4.11` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 110,780.00 USD | 0.00 USD | 190,950.00 USD |
| `1D` | `4.12` | 309,810.00 USD | 0.00 USD | 309,810.00 USD | 0.00 USD | 80,980.00 USD | 228,820.00 USD |
| `7D` | `4.12` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 341,440.00 USD |
| `1D` | `4.13` | 433,180.00 USD | 433,180.00 USD | 0.00 USD | 183,190.00 USD | 87,750.00 USD | 162,240.00 USD |
| `1D` | `4.13` | 866,360.00 USD | 866,360.00 USD | 0.00 USD | 183,190.00 USD | 87,750.00 USD | 162,240.00 USD |
| `1D` | `4.14` | 901,400.00 USD | 901,400.00 USD | 0.00 USD | 0.00 USD | 34,720.00 USD | 330.30 USD |
| `7D` | `4.14` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 214,920.00 USD | 90,830.00 USD | 0.00 USD |
| `7D` | `4.15` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 127,600.00 USD |
| `1D` | `4.18` | 911,070.00 USD | 911,070.00 USD | 0.00 USD | 9,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.19` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 174,270.00 USD | 0.00 USD | 185,170.00 USD |
| `1D` | `4.22` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,260.00 USD |
| `1D` | `4.23` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 171,410.00 USD | 440,840.00 USD | 0.00 USD |
| `1D` | `4.24` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD |
| `1D` | `4.25` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 64,520.00 USD | 229,390.00 USD |
| `7D` | `4.25` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 57,340.00 USD | 229.24 USD |
| `1D` | `4.26` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 168,980.00 USD | 0.00 USD |
| `7D` | `4.26` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 677,660.00 USD | 24,620.00 USD | 152,190.00 USD |
| `7D` | `4.27` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 313,130.00 USD | 30,410.00 USD | 295,750.00 USD |
| `7D` | `4.28` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `1D` | `4.29` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 152,480.00 USD | 32,690.00 USD | 161,450.00 USD |
| `7D` | `4.29` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 3,320.00 USD | 34,720.00 USD | 163,260.00 USD |
| `7D` | `4.30` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 270,390.00 USD | 0.00 USD | 94,870.00 USD |
| `7D` | `4.31` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 86,320.00 USD | 59,810.00 USD | 19.74 USD |
| `7D` | `4.32` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD |
| `1D` | `4.33` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 255,140.00 USD | 93,880.00 USD | 87,020.00 USD |
| `7D` | `4.33` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 270,290.00 USD | 140,540.00 USD | 114,780.00 USD |
| `7D` | `4.34` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 4,550.00 USD | 28,670.00 USD | 134,560.00 USD |
| `1D` | `4.35` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,370.00 USD |
| `7D` | `4.35` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,890.00 USD |
| `1D` | `4.36` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 84,400.00 USD | 12,310.00 USD | 29,780.00 USD |
| `7D` | `4.36` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 143,250.00 USD |
| `1D` | `4.37` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 52,120.00 USD | 46,860.00 USD | 131,580.00 USD |
| `1D` | `4.38` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 248,590.00 USD | 34,500.00 USD | 559,190.00 USD |
| `7D` | `4.38` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | 310,770.00 USD |
| `7D` | `4.39` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 248,520.00 USD | 108,260.00 USD | 155,470.00 USD |
| `1D` | `4.40` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,080.00 USD |
| `7D` | `4.40` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 106,760.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 196,500.00 USD | 112,990.00 USD | 63,590.00 USD |
| `7D` | `4.41` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 45,930.00 USD | 273,190.00 USD |
| `1D` | `4.42` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 47,240.00 USD | 537.46 USD |
| `7D` | `4.42` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 176,380.00 USD |
| `1D` | `4.43` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 5,100.00 USD | 49,400.00 USD | 94,480.00 USD |
| `7D` | `4.43` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 70,920.00 USD |
| `1D` | `4.44` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 292,720.00 USD |
| `7D` | `4.44` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,560.00 USD |
| `1D` | `4.45` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 649.63 USD | 50,720.00 USD | 1,760.00 USD |
| `1D` | `4.46` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 3,140.00 USD |
| `7D` | `4.46` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 1,510.00 USD |
| `1D` | `4.47` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 16,700.00 USD | 18,240.00 USD |
| `7D` | `4.47` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 0.00 USD |
| `1D` | `4.48` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 117,480.00 USD | 73,240.00 USD | 25,450.00 USD |
| `7D` | `4.48` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.49` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 252,130.00 USD | 155,000.00 USD | 150,370.00 USD |
| `7D` | `4.49` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 504.68 USD |
| `1D` | `4.50` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 361,560.00 USD | 65,710.00 USD | 117,840.00 USD |
| `7D` | `4.50` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 373,240.00 USD | 200,700.00 USD | 343.28 USD |
| `1D` | `4.51` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 162,900.00 USD | 307,580.00 USD | 312,490.00 USD |
| `7D` | `4.51` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 1,820.00 USD |
| `1D` | `4.52` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 287,560.00 USD | 88,150.00 USD | 242,940.00 USD |
| `7D` | `4.52` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 281,090.00 USD |
| `7D` | `4.53` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 235,230.00 USD |
| `1D` | `4.54` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 150,600.00 USD | 570,880.00 USD |
| `7D` | `4.54` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 213,870.00 USD |
| `7D` | `4.55` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 713.40 USD |
| `1D` | `4.56` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,390.00 USD |
| `7D` | `4.56` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 67,410.00 USD |
| `7D` | `4.57` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 210,490.00 USD |
| `1D` | `4.58` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 506,750.00 USD | 73,690.00 USD | 876,090.00 USD |
| `7D` | `4.58` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,870.00 USD |
| `1D` | `4.59` | 17,690,000.00 USD | 17,690,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,670.00 USD |
| `7D` | `4.59` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 67,260.00 USD |
| `7D` | `4.60` | 18,400,000.00 USD | 18,400,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 1,010.00 USD |
| `1D` | `4.61` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,890.00 USD |
| `7D` | `4.61` | 18,410,000.00 USD | 18,410,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 1,280.00 USD |
| `1D` | `4.62` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 19,660.00 USD |
| `7D` | `4.62` | 18,550,000.00 USD | 18,550,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 1,970.00 USD |
| `1D` | `4.63` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 18,760,000.00 USD | 18,760,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 431.56 USD |
| `1D` | `4.64` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 334,190.00 USD | 11,270.00 USD | 61,860.00 USD |
| `7D` | `4.64` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 407.00 USD |
| `1D` | `4.65` | 19,660,000.00 USD | 19,660,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 600,630.00 USD |
| `7D` | `4.65` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 1,870.00 USD |
| `1D` | `4.66` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 281,290.00 USD | 316,500.00 USD | 379,970.00 USD |
| `7D` | `4.66` | 20,020,000.00 USD | 20,020,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,630.00 USD |
| `1D` | `4.67` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 377,750.00 USD |
| `7D` | `4.67` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,580.00 USD |
| `1D` | `4.68` | 21,800,000.00 USD | 21,800,000.00 USD | 0.00 USD | 345,840.00 USD | 81,340.00 USD | 177,210.00 USD |
| `7D` | `4.68` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,110.00 USD |
| `1D` | `4.69` | 22,310,000.00 USD | 22,310,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,450.00 USD |
| `7D` | `4.69` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,430.00 USD |
| `1D` | `4.70` | 22,650,000.00 USD | 22,650,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,590.00 USD |
| `7D` | `4.70` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 23,620,000.00 USD | 23,620,000.00 USD | 0.00 USD | 365,580.00 USD | 284,360.00 USD | 316,400.00 USD |
| `7D` | `4.71` | 21,790,000.00 USD | 21,790,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 1,320.00 USD |
| `1D` | `4.72` | 23,920,000.00 USD | 23,920,000.00 USD | 0.00 USD | 5,440.00 USD | 187,480.00 USD | 103,790.00 USD |
| `7D` | `4.72` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,260.00 USD |
| `1D` | `4.73` | 24,080,000.00 USD | 24,080,000.00 USD | 0.00 USD | 61,330.00 USD | 37,010.00 USD | 61,550.00 USD |
| `7D` | `4.73` | 22,040,000.00 USD | 22,040,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 790.73 USD |
| `1D` | `4.74` | 24,830,000.00 USD | 24,830,000.00 USD | 0.00 USD | 273,860.00 USD | 172,000.00 USD | 304,220.00 USD |
| `7D` | `4.74` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 130,720.00 USD |
| `1D` | `4.75` | 25,540,000.00 USD | 25,540,000.00 USD | 0.00 USD | 240,860.00 USD | 202,760.00 USD | 270,190.00 USD |
| `7D` | `4.75` | 22,910,000.00 USD | 22,910,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 342,050.00 USD |
| `1D` | `4.76` | 25,900,000.00 USD | 25,900,000.00 USD | 0.00 USD | 35,470.00 USD | 78,750.00 USD | 247,600.00 USD |
| `7D` | `4.76` | 24,250,000.00 USD | 24,250,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 275,020.00 USD |
| `1D` | `4.77` | 26,280,000.00 USD | 26,280,000.00 USD | 0.00 USD | 113,030.00 USD | 151,370.00 USD | 115,600.00 USD |
| `7D` | `4.77` | 25,160,000.00 USD | 25,160,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 26,460,000.00 USD | 26,460,000.00 USD | 0.00 USD | 40,580.00 USD | 20,000.00 USD | 114,020.00 USD |
| `7D` | `4.78` | 26,510,000.00 USD | 26,510,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 153,740.00 USD |
| `1D` | `4.79` | 26,800,000.00 USD | 26,800,000.00 USD | 0.00 USD | 112,300.00 USD | 92,850.00 USD | 142,450.00 USD |
| `7D` | `4.79` | 27,550,000.00 USD | 27,550,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 71,560.00 USD |
| `1D` | `4.80` | 27,420,000.00 USD | 27,420,000.00 USD | 0.00 USD | 244,480.00 USD | 200,920.00 USD | 174,320.00 USD |
| `7D` | `4.80` | 29,140,000.00 USD | 29,140,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,610.00 USD |
| `1D` | `4.81` | 27,640,000.00 USD | 27,640,000.00 USD | 0.00 USD | 31,770.00 USD | 53,140.00 USD | 127,800.00 USD |
| `7D` | `4.81` | 29,760,000.00 USD | 29,760,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 102,460.00 USD |
| `1D` | `4.82` | 28,040,000.00 USD | 28,040,000.00 USD | 0.00 USD | 67,360.00 USD | 187,290.00 USD | 145,050.00 USD |
| `7D` | `4.82` | 32,530,000.00 USD | 32,530,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 28,220,000.00 USD | 28,220,000.00 USD | 0.00 USD | 61,110.00 USD | 31,430.00 USD | 88,060.00 USD |
| `7D` | `4.83` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 740,680.00 USD |
| `1D` | `4.84` | 28,470,000.00 USD | 28,470,000.00 USD | 0.00 USD | 82,160.00 USD | 89,230.00 USD | 77,570.00 USD |
| `7D` | `4.84` | 34,670,000.00 USD | 34,670,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 323,750.00 USD |
| `7D` | `4.85` | 36,690,000.00 USD | 36,690,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 38,100,000.00 USD | 38,100,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 801,150.00 USD |
| `7D` | `4.87` | 39,170,000.00 USD | 39,170,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,540.00 USD |
| `7D` | `4.88` | 40,750,000.00 USD | 40,750,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 793,500.00 USD |
| `7D` | `4.89` | 41,340,000.00 USD | 41,340,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 271,050.00 USD |
| `7D` | `4.90` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,900.00 USD |
| `7D` | `4.91` | 43,910,000.00 USD | 43,910,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 591,540.00 USD |
| `7D` | `4.92` | 45,640,000.00 USD | 45,640,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,600.00 USD |
| `7D` | `4.93` | 47,200,000.00 USD | 47,200,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,560.00 USD |
| `7D` | `4.94` | 48,500,000.00 USD | 48,500,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,000.00 USD |
| `7D` | `4.95` | 49,800,000.00 USD | 49,800,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 669,830.00 USD |
| `7D` | `4.96` | 51,040,000.00 USD | 51,040,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 411,160.00 USD |
| `7D` | `4.97` | 51,420,000.00 USD | 51,420,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 112,930.00 USD |
| `7D` | `4.98` | 52,080,000.00 USD | 52,080,000.00 USD | 0.00 USD | 251,840.00 USD | 102,410.00 USD | 302,650.00 USD |
| `7D` | `4.99` | 52,430,000.00 USD | 52,430,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 118,020.00 USD |
| `7D` | `5.00` | 53,130,000.00 USD | 53,130,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 453,280.00 USD |
| `7D` | `5.01` | 55,290,000.00 USD | 55,290,000.00 USD | 0.00 USD | 781,840.00 USD | 285,000.00 USD | 1,090,000.00 USD |
| `7D` | `5.02` | 56,770,000.00 USD | 56,770,000.00 USD | 0.00 USD | 821,860.00 USD | 337,720.00 USD | 321,630.00 USD |
| `7D` | `5.03` | 58,210,000.00 USD | 58,210,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 886,110.00 USD |
| `7D` | `5.04` | 59,300,000.00 USD | 59,300,000.00 USD | 0.00 USD | 305,260.00 USD | 163,190.00 USD | 620,470.00 USD |
| `7D` | `5.05` | 60,750,000.00 USD | 60,750,000.00 USD | 0.00 USD | 694,310.00 USD | 267,140.00 USD | 486,840.00 USD |
| `7D` | `5.06` | 61,430,000.00 USD | 61,430,000.00 USD | 0.00 USD | 92,480.00 USD | 165,230.00 USD | 420,550.00 USD |
| `7D` | `5.07` | 62,600,000.00 USD | 62,600,000.00 USD | 0.00 USD | 358,750.00 USD | 137,080.00 USD | 673,490.00 USD |
| `7D` | `5.08` | 63,120,000.00 USD | 63,120,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 148,470.00 USD |
| `7D` | `5.09` | 63,660,000.00 USD | 63,660,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 384,500.00 USD |
| `7D` | `5.10` | 64,040,000.00 USD | 64,040,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 202,060.00 USD |
| `7D` | `5.11` | 64,800,000.00 USD | 64,800,000.00 USD | 0.00 USD | 369,260.00 USD | 92,720.00 USD | 291,590.00 USD |
| `7D` | `5.12` | 65,380,000.00 USD | 65,380,000.00 USD | 0.00 USD | 303,840.00 USD | 166,880.00 USD | 116,730.00 USD |
| `7D` | `5.13` | 66,110,000.00 USD | 66,110,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 483,710.00 USD |
| `7D` | `5.14` | 66,550,000.00 USD | 66,550,000.00 USD | 0.00 USD | 140,950.00 USD | 59,640.00 USD | 239,690.00 USD |
| `7D` | `5.15` | 67,110,000.00 USD | 67,110,000.00 USD | 0.00 USD | 205,680.00 USD | 82,350.00 USD | 268,050.00 USD |
| `7D` | `5.16` | 67,620,000.00 USD | 67,620,000.00 USD | 0.00 USD | 51,850.00 USD | 112,830.00 USD | 346,930.00 USD |
| `7D` | `5.17` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 280,710.00 USD | 85,040.00 USD | 310,010.00 USD |
| `7D` | `5.18` | 68,550,000.00 USD | 68,550,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 123,890.00 USD |
| `7D` | `5.19` | 68,770,000.00 USD | 68,770,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 139,500.00 USD |
| `7D` | `5.20` | 69,020,000.00 USD | 69,020,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,780.00 USD |
| `7D` | `5.21` | 69,260,000.00 USD | 69,260,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,270.00 USD |
| `7D` | `5.22` | 69,330,000.00 USD | 69,330,000.00 USD | 0.00 USD | 52,130.00 USD | 13,410.00 USD | 300.69 USD |
| `7D` | `5.23` | 69,380,000.00 USD | 69,380,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 34,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.15B` | Total OI Tokens: `279,200,695.7 NEAR`
  * 1h OI Change: `-3.10%` | 4h OI Change: `-9.07%` | 24h OI Change: `-13.91%`
  * Exchange Breakdown: Binance=`219.05M` | Bybit=`153.19M` | OKX=`49.03M` | Hyperliquid=`231.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `22.06K` | Last 24h: `115.52K` | Last 3d: `331.47K` | Last 7d: `238.32K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0005%` | **USDT OKX** | `0.0094%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0005%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0079%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `46.90%` | `53.10%` | `0.88` | 20,510,000.00 USD |
| `15M` | `Binance` | `50.75%` | `49.25%` | `1.03` | 7,710,000.00 USD |
| `15M` | `OKX` | `62.39%` | `37.61%` | `1.66` | 2,900,000.00 USD |
| `15M` | `Bybit` | `46.46%` | `53.54%` | `0.87` | 2,640,000.00 USD |
| `15M` | `KuCoin` | `54.2%` | `45.8%` | `1.18` | 195,540.00 USD |
| `15M` | `Gate` | `55.42%` | `44.58%` | `1.24` | 534,680.00 USD |
| `15M` | `Bitget` | `45.08%` | `54.92%` | `0.82` | 1,610,000.00 USD |
| `15M` | `BingX` | `41.05%` | `58.95%` | `0.70` | 558,050.00 USD |
| `15M` | `MEXC` | `25.1%` | `74.9%` | `0.34` | 2,060,000.00 USD |
| `15M` | `Bitunix` | `45.93%` | `54.07%` | `0.85` | 552,340.00 USD |
| `15M` | `Hyperliquid` | `41.33%` | `58.67%` | `0.70` | 404,850.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `38.25%` | `61.75%` | `0.62` | 541,950.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `6.89%` | `93.11%` | `0.07` | 444,600.00 USD |
| `15M` | `HTX` | `35.33%` | `64.67%` | `0.55` | 29,920.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `35.38%` | `64.62%` | `0.55` | 210,420.00 USD |
| `15M` | `Aster` | `45.37%` | `54.63%` | `0.83` | 113,020.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `34.51%` | `65.49%` | `0.53` | 7,070.00 USD |
| `15M` | `Whale Positions` | `50.75%` | `49.25%` | `1.03` | 7,710,000.00 USD |
| `15M` | `Global Accounts` | `46.90%` | `53.10%` | `0.88` | 20,510,000.00 USD |
| `1H` | `NEAR` | `48.72%` | `51.28%` | `0.95` | 184,050,000.00 USD |
| `1H` | `Binance` | `49.56%` | `50.44%` | `0.98` | 68,130,000.00 USD |
| `1H` | `OKX` | `46.53%` | `53.47%` | `0.87` | 20,610,000.00 USD |
| `1H` | `Bybit` | `49.56%` | `50.44%` | `0.98` | 28,710,000.00 USD |
| `1H` | `KuCoin` | `51.71%` | `48.29%` | `1.07` | 1,400,000.00 USD |
| `1H` | `Gate` | `39.08%` | `60.92%` | `0.64` | 2,280,000.00 USD |
| `1H` | `Bitget` | `46.61%` | `53.39%` | `0.87` | 8,490,000.00 USD |
| `1H` | `BingX` | `46.18%` | `53.82%` | `0.86` | 6,310,000.00 USD |
| `1H` | `MEXC` | `53.68%` | `46.32%` | `1.16` | 13,140,000.00 USD |
| `1H` | `Bitunix` | `44.71%` | `55.29%` | `0.81` | 4,420,000.00 USD |
| `1H` | `Hyperliquid` | `42.37%` | `57.63%` | `0.74` | 20,350,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.3%` | `45.7%` | `1.19` | 1,110,000.00 USD |
| `1H` | `Crypto.com` | `43.88%` | `56.12%` | `0.78` | 8,500.00 USD |
| `1H` | `WhiteBIT` | `72.28%` | `27.72%` | `2.61` | 3,820,000.00 USD |
| `1H` | `HTX` | `39.58%` | `60.42%` | `0.66` | 173,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.12%` | `48.88%` | `1.05` | 3,540,000.00 USD |
| `1H` | `Aster` | `32.12%` | `67.88%` | `0.47` | 418,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.59%` | `50.41%` | `0.98` | 1,150,000.00 USD |
| `1H` | `Whale Positions` | `49.56%` | `50.44%` | `0.98` | 68,130,000.00 USD |
| `1H` | `Global Accounts` | `48.72%` | `51.28%` | `0.95` | 184,050,000.00 USD |
| `4H` | `NEAR` | `46.39%` | `53.61%` | `0.87` | 319,320,000.00 USD |
| `4H` | `Binance` | `47.41%` | `52.59%` | `0.90` | 130,470,000.00 USD |
| `4H` | `OKX` | `50.5%` | `49.5%` | `1.02` | 43,520,000.00 USD |
| `4H` | `Bybit` | `46.3%` | `53.7%` | `0.86` | 43,720,000.00 USD |
| `4H` | `KuCoin` | `45.73%` | `54.27%` | `0.84` | 3,670,000.00 USD |
| `4H` | `Gate` | `48.75%` | `51.25%` | `0.95` | 6,650,000.00 USD |
| `4H` | `Bitget` | `45.22%` | `54.78%` | `0.83` | 18,000,000.00 USD |
| `4H` | `BingX` | `43.24%` | `56.76%` | `0.76` | 9,990,000.00 USD |
| `4H` | `MEXC` | `42.29%` | `57.71%` | `0.73` | 27,530,000.00 USD |
| `4H` | `Bitunix` | `44.6%` | `55.4%` | `0.81` | 12,960,000.00 USD |
| `4H` | `Hyperliquid` | `40.58%` | `59.42%` | `0.68` | 10,400,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `41.71%` | `58.29%` | `0.72` | 2,620,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `37.06%` | `62.94%` | `0.59` | 5,040,000.00 USD |
| `4H` | `HTX` | `49.48%` | `50.52%` | `0.98` | 686,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.26%` | `57.74%` | `0.73` | 2,170,000.00 USD |
| `4H` | `Aster` | `41.14%` | `58.86%` | `0.70` | 1,500,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.84%` | `52.16%` | `0.92` | 384,920.00 USD |
| `4H` | `Whale Positions` | `47.41%` | `52.59%` | `0.90` | 130,470,000.00 USD |
| `4H` | `Global Accounts` | `46.39%` | `53.61%` | `0.87` | 319,320,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.38` | `4.40` | `4.38` | `4.42` | `4.38` | 4,640,530.52 USD | 2,789,933.99 USD | 1,850,596.53 USD | 939,337.46 USD | `+20.24%` | `7B / 6S` |
| `0:00 UTC` | `4.33` | `4.34` | `4.33` | `4.41` | `4.31` | 19,326,312.32 USD | 9,601,663.40 USD | 9,724,648.92 USD | -122,985.52 USD | `-0.64%` | `6B / 20S` |
| `5:00 UTC` | `4.36` | `4.35` | `4.36` | `4.37` | `4.34` | 4,641,250.70 USD | 2,849,322.27 USD | 1,791,928.43 USD | 1,057,393.84 USD | `+22.78%` | `8B / 0S` |
| `0:00 UTC` | `4.21` | `4.24` | `4.21` | `4.37` | `4.15` | 41,106,447.75 USD | 17,638,668.55 USD | 23,467,779.20 USD | -5,829,110.65 USD | `-14.18%` | `4B / 19S` |
| `5:00 UTC` | `4.16` | `4.18` | `4.16` | `4.26` | `4.10` | 52,737,896.00 USD | 23,168,223.37 USD | 29,569,672.63 USD | -6,401,449.26 USD | `-12.14%` | `7B / 20S` |
| `0:00 UTC` | `4.15` | `4.16` | `4.15` | `4.21` | `4.12` | 38,451,702.31 USD | 19,031,443.49 USD | 19,420,258.82 USD | -388,815.33 USD | `-1.01%` | `3B / 6S` |
| `5:00 UTC` | `4.23` | `4.22` | `4.23` | `4.28` | `4.18` | 19,231,459.24 USD | 9,485,975.24 USD | 9,745,484.00 USD | -259,508.77 USD | `-1.35%` | `5B / 4S` |
| `0:00 UTC` | `4.24` | `4.23` | `4.24` | `4.26` | `4.18` | 9,925,749.34 USD | 5,368,569.39 USD | 4,557,179.95 USD | 811,389.45 USD | `+8.17%` | `5B / 13S` |
| `5:00 UTC` | `4.17` | `4.17` | `4.17` | `4.20` | `4.14` | 11,567,070.53 USD | 6,145,277.52 USD | 5,421,793.01 USD | 723,484.51 USD | `+6.25%` | `3B / 3S` |
| `0:00 UTC` | `4.10` | `4.12` | `4.10` | `4.17` | `4.08` | 21,897,897.42 USD | 10,536,446.41 USD | 11,361,451.02 USD | -825,004.61 USD | `-3.77%` | `7B / 10S` |

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
| `5m` | 247,110.00 USD | 283,090.00 USD | **`ACCUMULATION`** |
| `15m` | -2,100,000.00 USD | -3,000,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,650,000.00 USD | -3,590,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,270,000.00 USD | -2,120,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -8,070,000.00 USD | -17,040,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,750,000.00 USD | -14,270,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -16,410,000.00 USD | -24,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,300,000.00 USD | -23,570,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -16,170,000.00 USD | -25,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -25,300,000.00 USD | -72,030,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -78,650,000.00 USD | -115,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -245,750,000.00 USD | -682,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+247.11K` | 15m=`-2.10M` | 1h=`-3.27M` | 24h=`-25.30M`
* Futures Capital Netflows: 5m=`+283.09K` | 15m=`-3.00M` | 1h=`-2.12M` | 24h=`-72.03M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.14` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.01` (Risk Distance: `0.1294` pts)
  * +2.5R Take Profit: `4.46`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.39` (Risk Distance: `0.1294` pts)
  * +2.5R Take Profit: `3.93`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.15`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
