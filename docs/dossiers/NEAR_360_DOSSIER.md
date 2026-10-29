# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.57` | **Live Ask Quote**: `4.60` | **Mid Price**: `4.59`
- **Spread Points**: `29.00` | **Spread BPS**: `63.20 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.43` | VWAP Z-Score: `+1.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0442` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `68.03` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.70` | Lower -3.00σ Band: `4.17`
  * Upper +2.51σ Band: `4.66` | Lower -2.51σ Band: `4.21`
  * Upper +2.01σ Band: `4.61` | Lower -2.01σ Band: `4.26`
  * Upper +2.00σ Band: `4.61` | Lower -2.00σ Band: `4.26`
  * Upper +1.28σ Band: `4.55` | Lower -1.28σ Band: `4.32`
  * Upper +1.00σ Band: `4.52` | Lower -1.00σ Band: `4.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.45` | EMA-20=`4.42` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.44` (Slope: `+0.0000`) | EMA-100=`4.49`
  * Institutional Anchors: EMA-144=`4.51` | EMA-200=`4.51` (Slope: `-0.2265`) | EMA-233=`4.52`
- **Range Boundaries**: 24H High=`4.80` | 24H Low=`4.27` | Weekly High=`4.80` | Weekly Low=`4.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.64` (Distance: `-1.24%`)
  * Point of Control (POC) = `4.41` (Distance: `+4.04%`)
  * Value Area Low (VAL) = `4.37` (Distance: `+4.88%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.73` | POC=`4.68` | VAL=`4.61`
  * Prior Day Extremes: PDH=`4.80` | PDL=`4.53` | PDC=`4.71`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.62` | Weekly POC=`4.44` | Weekly VAL=`4.41`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.75` | Low=`4.39`
  * London Session (08:00-16:00 UTC): High=`4.50` | Low=`4.27`
  * New York Session (13:00-21:00 UTC): High=`4.67` | Low=`4.34`
  * Initial Balance (First Hour): IB High=`4.50` | IB Low=`4.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.57` - `4.61`
  * Optimal Trade Entry (OTE 0.705): `4.60`
  * Structural Invalidation Anchor (0.786): `4.63`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.58` | `4.59` | `4.58` | `4.58` | `638,741` | 2,925,919.92 USD | -573,390.34 USD | `-19.60%` | -23,311,428.95 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.58` | `4.60` | `4.58` | `4.60` | `250,726` | 1,151,311.60 USD | 217,531.09 USD | `+18.89%` | -23,093,897.86 USD | `+0.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.60` | `4.60` | `4.59` | `4.59` | `194,442` | 893,296.48 USD | -579,339.77 USD | `-64.85%` | -23,673,237.64 USD | `-0.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.62` | `4.63` | `4.59` | `4.60` | `2,339,101` | 10,770,688.98 USD | 318,397.72 USD | `+2.96%` | -22,490,552.06 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.60` | `4.61` | `4.58` | `4.60` | `1,453,442` | 6,667,677.12 USD | -726,421.72 USD | `-10.89%` | -23,216,973.79 USD | `-0.57` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.60` | `4.60` | `4.59` | `4.59` | `194,468` | 893,415.77 USD | -579,459.06 USD | `-64.86%` | -23,796,432.85 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4.52` | `4.66` | `4.51` | `4.65` | `12,649,887` | 58,190,012.91 USD | 5,991,812.39 USD | `+10.30%` | -22,042,925.80 USD | `+2.01` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.65` | `4.69` | `4.58` | `4.60` | `10,150,684` | 46,941,765.94 USD | -4,168,368.77 USD | `-8.88%` | -26,211,294.57 USD | `-0.73` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.60` | `4.60` | `4.59` | `4.59` | `194,442` | 893,296.48 USD | -579,339.77 USD | `-64.85%` | -26,790,634.34 USD | `+0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.58` | `4.59` | `10,345,155` | 47,835,195.48 USD | -4,747,841.60 USD | `-9.93%` | -32,974,989.30 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.73` | `4.73` | `4.40` | `4.42` | `25,745,501` | 116,497,184.49 USD | -11,801,514.25 USD | `-10.13%` | -15,870,340.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -31,542,465.78 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -32,636,174.80 USD | `+1.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -28,227,147.70 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.58` | `4.59` | `10,345,155` | 47,835,195.48 USD | -4,747,841.60 USD | `-9.93%` | -32,974,989.30 USD | `+0.11` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`4.59`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `60` | `0x7737...bf66` | `LONG` | 25,043,383.58 USD | `5,640,376.30` | `2.35` | `4.44` | `0.9344` | 11,771,480.75 USD | `+47.00%` | `10X Cross` |
| `130` | `0xb581...6f4f` | `LONG` | 15,980,400.00 USD | `3,600,000.00` | `5.19` | `4.44` | `0.000000` | -2,712,635.22 USD | `-16.97%` | `4X Cross` |
| `211` | `0xdd53...2b13` | `SHORT` | 10,675,258.87 USD | `2,400,202.10` | `2.31` | `4.44` | `27.16` | -5,129,854.99 USD | `-48.05%` | `3X Cross` |
| `262` | `0x77ee...2902` | `LONG` | 9,179,008.68 USD | `2,063,023.10` | `1.93` | `4.44` | `0.2642` | 5,187,812.75 USD | `+56.52%` | `10X Cross` |
| `273` | `0xefe4...194b` | `SHORT` | 8,983,729.51 USD | `2,019,882.30` | `4.44` | `4.44` | `11.55` | -8,644.36 USD | `-0.10%` | `5X Cross` |
| `380` | `0xb83d...6e36` | `SHORT` | 6,429,001.57 USD | `1,445,759.10` | `5.19` | `4.44` | `81.32` | 1,080,447.38 USD | `+16.81%` | `3X Cross` |
| `406` | `0xb46b...538e` | `SHORT` | 5,936,248.80 USD | `1,336,000.00` | `4.33` | `4.44` | `7.24` | -151,384.74 USD | `-2.55%` | `10X Cross` |
| `425` | `0x9df2...c665` | `SHORT` | 5,625,202.00 USD | `1,265,000.00` | `2.03` | `4.44` | `27.04` | -3,058,519.66 USD | `-54.37%` | `10X Cross` |
| `435` | `0xb695...a92d` | `SHORT` | 5,480,467.97 USD | `1,233,422.90` | `4.57` | `4.44` | `26.59` | 160,268.94 USD | `+2.92%` | `10X Cross` |
| `469` | `0x60b0...991e` | `LONG` | 4,982,595.38 USD | `1,121,307.10` | `5.00` | `4.44` | `0.000000` | -618,829.05 USD | `-12.42%` | `10X Cross` |
| `490` | `0xcac1...26b3` | `SHORT` | 4,775,690.74 USD | `1,073,743.90` | `2.48` | `4.44` | `11.70` | -2,115,747.28 USD | `-44.30%` | `10X Cross` |
| `496` | `0x781e...96b7` | `SHORT` | 4,704,964.83 USD | `1,058,151.50` | `2.45` | `4.44` | `7.38` | -2,115,235.80 USD | `-44.96%` | `10X Cross` |
| `520` | `0xdf60...d3c7` | `LONG` | 4,444,100.00 USD | `1,000,000.00` | `4.70` | `4.44` | `3.91` | -255,177.29 USD | `-5.74%` | `8X Isolated` |
| `572` | `0x45d2...4029` | `SHORT` | 4,040,100.44 USD | `909,400.00` | `3.26` | `4.44` | `40.99` | -1,073,950.54 USD | `-26.58%` | `10X Cross` |
| `587` | `0x4cae...7c34` | `LONG` | 3,960,263.20 USD | `890,086.80` | `3.51` | `4.44` | `2.20` | 833,257.07 USD | `+21.04%` | `10X Cross` |
| `723` | `0x9aa5...58af` | `SHORT` | 3,213,734.35 USD | `723,977.10` | `4.78` | `4.44` | `15.00` | 245,898.84 USD | `+7.65%` | `10X Cross` |
| `808` | `0x005a...61fe` | `LONG` | 2,899,330.48 USD | `652,414.60` | `2.08` | `4.44` | `2.37` | 1,541,799.25 USD | `+53.18%` | `7X Cross` |
| `817` | `0xba5d...a352` | `SHORT` | 2,876,339.37 USD | `647,532.50` | `2.83` | `4.44` | `12.65` | -1,043,624.42 USD | `-36.28%` | `10X Cross` |
| `830` | `0xd1dd...9e85` | `SHORT` | 2,835,819.40 USD | `637,621.00` | `4.96` | `4.44` | `16.39` | 327,653.34 USD | `+11.55%` | `10X Cross` |
| `831` | `0x123d...3bff` | `SHORT` | 2,825,580.33 USD | `635,890.70` | `2.09` | `4.44` | `9.16` | -1,499,069.60 USD | `-53.05%` | `10X Cross` |
| `845` | `0xcf53...ee11` | `SHORT` | 2,760,021.22 USD | `621,598.40` | `5.07` | `4.44` | `24.18` | 392,149.04 USD | `+14.21%` | `10X Cross` |
| `940` | `0x5647...e7de` | `SHORT` | 2,422,000.79 USD | `545,864.50` | `4.69` | `4.44` | `12.50` | 136,590.66 USD | `+5.64%` | `10X Cross` |
| `966` | `0xbfc7...80b4` | `SHORT` | 2,362,578.30 USD | `531,000.00` | `2.01` | `4.44` | `12.78` | -1,297,378.91 USD | `-54.91%` | `10X Cross` |
| `977` | `0xfc66...ca06` | `SHORT` | 2,344,281.59 USD | `527,083.20` | `4.58` | `4.44` | `59.39` | 70,894.63 USD | `+3.02%` | `10X Cross` |
| `1025` | `0x7fda...17d1` | `SHORT` | 2,229,968.37 USD | `501,477.10` | `4.83` | `4.44` | `69.18` | 190,154.48 USD | `+8.53%` | `10X Cross` |
| `1065` | `0xef96...9383` | `SHORT` | 2,122,975.92 USD | `477,459.50` | `4.50` | `4.44` | `12.48` | 26,922.28 USD | `+1.27%` | `10X Cross` |
| `1296` | `0xe097...d0fe` | `LONG` | 1,776,920.00 USD | `400,000.00` | `5.29` | `4.44` | `0.000000` | -339,867.30 USD | `-19.13%` | `10X Cross` |
| `1410` | `0xdf95...7d72` | `SHORT` | 1,611,132.30 USD | `362,243.50` | `4.23` | `4.44` | `99.51` | -78,054.10 USD | `-4.84%` | `10X Cross` |
| `1429` | `0x6e8f...4364` | `LONG` | 1,606,537.88 USD | `361,210.50` | `3.28` | `4.44` | `3.29` | 422,477.65 USD | `+26.30%` | `10X Cross` |
| `1465` | `0xcf67...eb24` | `LONG` | 1,557,220.00 USD | `350,000.00` | `1.98` | `4.44` | `1.27` | 865,602.12 USD | `+55.59%` | `10X Cross` |
| `1575` | `0xfc27...9d9d` | `SHORT` | 1,421,621.78 USD | `319,997.70` | `5.01` | `4.44` | `49.85` | 181,920.84 USD | `+12.80%` | `10X Cross` |
| `1651` | `0x023a...2355` | `SHORT` | 1,329,104.59 USD | `298,833.00` | `4.60` | `4.44` | `29.85` | 46,263.14 USD | `+3.48%` | `10X Cross` |
| `1837` | `0xe065...0f85` | `SHORT` | 1,156,218.58 USD | `260,227.90` | `2.60` | `4.44` | `6.17` | -478,507.84 USD | `-41.39%` | `10X Cross` |
| `1850` | `0xb69e...033a` | `LONG` | 1,140,670.17 USD | `257,081.40` | `4.61` | `4.44` | `2.70` | -43,384.70 USD | `-3.80%` | `10X Cross` |
| `1888` | `0xff43...d924` | `LONG` | 1,109,986.89 USD | `249,474.50` | `4.64` | `4.44` | `3.28` | -48,056.78 USD | `-4.33%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.65` | 5,862.40 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.86K USD at 4.6479 USD [API] | `2026-10-27 19:06:26` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 5,887.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.89K USD at 4.6337 USD [API] | `2026-10-27 19:29:16` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 7,199.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.20K USD at 4.6624 USD [API] | `2026-10-27 19:45:07` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 5,953.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.95K USD at 4.6236 USD [API] | `2026-10-27 20:39:38` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 5,532.85 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.53K USD at 4.6331 USD [API] | `2026-10-27 20:47:56` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 19.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.6336 USD [API] | `2026-10-27 16:31:27` |
| `ANNOUNCEMENT` | `INFO` | `4.63` | 470.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.47K USD at 4.6336 USD [API] | `2026-10-27 16:31:27` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 8,803.46 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.80K USD at 4.7333 USD [API] | `2026-10-27 21:35:14` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 1,192.73 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.19K USD at 4.7901 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 1,045.02 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.05K USD at 4.8025 USD [API] | `2026-10-27 21:38:12` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 3,789.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.79K USD at 4.7956 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 1,043.39 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.04K USD at 4.7950 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 1,042.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 1.04K USD at 4.7930 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.80` | 5,147.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 5.15K USD at 4.7954 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.72` | 790.30 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.79K USD at 4.7154 USD [API] | `2026-10-27 21:34:13` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 52.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 4.6960 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 12.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.6960 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 12.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.6960 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 12.63 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.6771 USD [API] | `2026-10-27 21:32:35` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 10,238.18 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.24K USD at 4.7945 USD [API] | `2026-10-27 21:36:32` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 7,460.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.46K USD at 4.6855 USD [API] | `2026-10-27 21:45:16` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 6,073.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.07K USD at 4.6855 USD [API] | `2026-10-27 21:45:16` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 2,061.57 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 2.06K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 52.69 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.05K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |
| `ANNOUNCEMENT` | `INFO` | `4.79` | 17.72 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.02K USD at 4.7899 USD [API] | `2026-10-27 21:36:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.55` (Vol: 717,200.00 USD, Dist: `+2.36%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--4.18%`)
  * 48H Horizon: Short MP=`4.55` (Vol: 717,200.00 USD, Dist: `+2.36%`) | Long MP=`4.26` (Vol: 591,700.00 USD, Dist: `--4.18%`)
  * 3D Horizon: Short MP=`4.55` (Vol: 717,200.00 USD, Dist: `+2.36%`) | Long MP=`4.26` (Vol: 618,400.00 USD, Dist: `--4.18%`)
  * 7D Horizon: Short MP=`5.03` (Vol: 914,000.00 USD, Dist: `+12.98%`) | Long MP=`4.23` (Vol: 1,200,000.00 USD, Dist: `--4.99%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.9350` | 10,170.00 USD | 36,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 29,450.00 USD | 36,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 5,440,000.00 USD | 36,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 17,330.00 USD | 30,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 122.34 USD | 30,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 159,280.00 USD | 30,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 28,030.00 USD | 30,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 30,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 15,420.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 5,690.00 USD | 30,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 7,890.00 USD | 30,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 4,460.00 USD | 30,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 30,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 8,500.00 USD | 30,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 75,160.00 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 26,680.00 USD | 30,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,120.00 USD | 30,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 650.70 USD | 30,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 30,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 52,310.00 USD | 30,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 589.28 USD | 30,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 2,820.00 USD | 30,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 9,290.00 USD | 30,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,900.00 USD | 30,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 9,080.00 USD | 30,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 1,120.00 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,520.00 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 408.12 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 447.94 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 2,830.00 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 2,490.00 USD | 30,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 28,060.00 USD | 30,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 236.85 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 795.11 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 3,410.00 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 37,460.00 USD | 30,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 20,260.00 USD | 30,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 3,000.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 7,080.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 3,330.00 USD | 30,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,420.00 USD | 30,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 30,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 610.00 USD | 30,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 2,360.00 USD | 30,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 146,570.00 USD | 30,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 32,200.00 USD | 30,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 1,420,000.00 USD | 29,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 7,540.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 7,660.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 191.64 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 807.50 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 1,620.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 16,800.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 92,960.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 1,110.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,560.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 15,740.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 7,770.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 6,660.00 USD | 28,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 28,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 1,560.00 USD | 28,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 32,210.00 USD | 28,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 68,650.00 USD | 28,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 211.80 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 78,220.00 USD | 28,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 303.45 USD | 28,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 179,870.00 USD | 28,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 5,410.00 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 100.55 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 28,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 1,290.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 5,790.00 USD | 27,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 239,650.00 USD | 27,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 937.50 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 5,830.00 USD | 27,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,340.00 USD | 27,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 4,280.00 USD | 27,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 918.42 USD | 27,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 27,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 6,970.00 USD | 27,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 41,390.00 USD | 27,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 124,790.00 USD | 27,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 506.37 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 104,370.00 USD | 27,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 85,840.00 USD | 27,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 4,560.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 1,960.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 17,190.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 28,510.00 USD | 27,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 5,880.00 USD | 27,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 12,760.00 USD | 27,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 4,700.00 USD | 27,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 2,230.00 USD | 27,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 161,930.00 USD | 27,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 543.75 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 24,920.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 11,120.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 600,160.00 USD | 27,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 11,120.00 USD | 26,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 27,790.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 58,480.00 USD | 26,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 124,730.00 USD | 26,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 152,580.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 2,030.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 804.32 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 5,250.00 USD | 26,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,510,000.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 440.31 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 3,460.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 1,270.00 USD | 24,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 50,580.00 USD | 24,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,650.00 USD | 24,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 65,220.00 USD | 24,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 430,380.00 USD | 24,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 534.24 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 386,250.00 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 2,430.00 USD | 23,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 185,860.00 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 485.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 29,790.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 2,760.00 USD | 23,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 10,580.00 USD | 23,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 259,350.00 USD | 23,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 23,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,040.00 USD | 23,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 24,490.00 USD | 23,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 10,690.00 USD | 23,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 22,690.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 23,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 186,320.00 USD | 23,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 694.96 USD | 22,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 10,460.00 USD | 22,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 67,580.00 USD | 22,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 5,890.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 301.40 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 6,420.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,760.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 55,020.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 186,060.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,620.00 USD | 22,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 19,240.00 USD | 22,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 3,050.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 10,340.00 USD | 22,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 121,210.00 USD | 22,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,970.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 40,930.00 USD | 22,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 1,850.00 USD | 22,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 22,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,960.00 USD | 22,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 3,850.00 USD | 22,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 1,800.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,840.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 10,720.00 USD | 22,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 200,600.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 694.18 USD | 22,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 6,480.00 USD | 22,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 539,720.00 USD | 22,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 6,970.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,050.00 USD | 21,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 5,190.00 USD | 21,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 5,990.00 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,600.00 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 18,250.00 USD | 21,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 22,220.00 USD | 21,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 6,000.00 USD | 21,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 116.12 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 63,540.00 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 2,170.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 7,160.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 12,620.00 USD | 21,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 26,040.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 119,700.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 29,380.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 15,760.00 USD | 21,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 358,170.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 119,150.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 22,550.00 USD | 20,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,720.00 USD | 20,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 3,090.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,030.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 4,930.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 36,570.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 80,900.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 10,480.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 38,530.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 30,120.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 2,220.00 USD | 20,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 52,770.00 USD | 20,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 111,270.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 10,060.00 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 5,820.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 103,170.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 28,430.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 21,640.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 19,880.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 276,210.00 USD | 19,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 59,690.00 USD | 19,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 37,050.00 USD | 19,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 835,690.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 5,600.00 USD | 18,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,400,000.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 58,360.00 USD | 17,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 64,720.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 6,800.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 54,740.00 USD | 17,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 32,850.00 USD | 17,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 5,110.00 USD | 17,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 5,240.00 USD | 17,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 14,490.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 45,540.00 USD | 17,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 8,730.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 97,200.00 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 187,920.00 USD | 16,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 6,530.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 25,060.00 USD | 16,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 40,920.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 21,600.00 USD | 16,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 11,390.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 77,730.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 23,730.00 USD | 16,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 21,380.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,460.00 USD | 16,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 15,060.00 USD | 16,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 2,700.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 536,780.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 335,270.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 367,390.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 3,340.00 USD | 15,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 113,320.00 USD | 15,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 296,360.00 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 28,190.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 94,590.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 13,600.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 13,580.00 USD | 14,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 25,260.00 USD | 14,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 523,780.00 USD | 14,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 31,510.00 USD | 14,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 44,710.00 USD | 14,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 189,790.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 216,110.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 3,030.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 140,650.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 58,950.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 24,930.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 135,410.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,460.00 USD | 13,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 91,600.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 56,130.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 19,920.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 37,770.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 143,780.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 14,720.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 82,000.00 USD | 12,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 5,180.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 162,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.84` | 31,230,000.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 301.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 23,860.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 13,750.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.86` | 31,230,000.00 USD | 31,230,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 23,070.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.87` | 31,160,000.00 USD | 31,160,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 4,660.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.88` | 31,070,000.00 USD | 31,070,000.00 USD | 107,410.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 37,160.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.89` | 30,850,000.00 USD | 30,850,000.00 USD | 25,070.00 USD | 50,710.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 103,080.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.90` | 30,780,000.00 USD | 30,780,000.00 USD | 93,000.00 USD | 28,250.00 USD | 49,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 8,840.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.91` | 30,610,000.00 USD | 30,610,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.92` | 30,530,000.00 USD | 30,530,000.00 USD | 91,730.00 USD | 41,330.00 USD | 80,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 199,590.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.93` | 30,320,000.00 USD | 30,320,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 20,840.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.94` | 30,190,000.00 USD | 30,190,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 533,900.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 15,560,000.00 USD | 15,560,000.00 USD | 12,850.00 USD | 8,690.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 29,950,000.00 USD | 29,950,000.00 USD | 8,490.00 USD | 26,060.00 USD | 552.68 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 51,840.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 15,520,000.00 USD | 15,520,000.00 USD | 23,250.00 USD | 16,000.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 29,920,000.00 USD | 29,920,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 108,170.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 15,460,000.00 USD | 15,460,000.00 USD | 93,920.00 USD | 47,530.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 29,700,000.00 USD | 29,700,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 40,980.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 15,270,000.00 USD | 15,270,000.00 USD | 46,710.00 USD | 30,290.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 29,090,000.00 USD | 29,090,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 161,330.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 15,180,000.00 USD | 15,180,000.00 USD | 68,470.00 USD | 12,310.00 USD | 34,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 28,890,000.00 USD | 28,890,000.00 USD | 62,170.00 USD | 82,870.00 USD | 101,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 35,370.00 USD | 7,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 15,060,000.00 USD | 15,060,000.00 USD | 8,650.00 USD | 7,330.00 USD | 19,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 28,650,000.00 USD | 28,650,000.00 USD | 261,860.00 USD | 105,220.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 56,650.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 15,030,000.00 USD | 15,030,000.00 USD | 109,160.00 USD | 56,050.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 28,110,000.00 USD | 28,110,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 21,970.00 USD | 7,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 14,820,000.00 USD | 14,820,000.00 USD | 60,540.00 USD | 20,960.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 27,200,000.00 USD | 27,200,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 97,150.00 USD | 7,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 14,710,000.00 USD | 14,710,000.00 USD | 23,320.00 USD | 32,030.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 26,630,000.00 USD | 26,630,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 30,290.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 14,630,000.00 USD | 14,630,000.00 USD | 14,780.00 USD | 32,610.00 USD | 100,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 26,190,000.00 USD | 26,190,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 67,670.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 14,490,000.00 USD | 14,490,000.00 USD | 53,740.00 USD | 0.00 USD | 14,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 25,900,000.00 USD | 25,900,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 88,740.00 USD | 7,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 14,420,000.00 USD | 14,420,000.00 USD | 30,920.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 25,560,000.00 USD | 25,560,000.00 USD | 197,400.00 USD | 45,470.00 USD | 89,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 341,320.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 14,360,000.00 USD | 14,360,000.00 USD | 1,720.00 USD | 7,520.00 USD | 308.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 25,230,000.00 USD | 25,230,000.00 USD | 180,120.00 USD | 35,750.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 254,230.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 14,360,000.00 USD | 14,360,000.00 USD | 2,500.00 USD | 0.00 USD | 194.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 24,970,000.00 USD | 24,970,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 316,900.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 14,350,000.00 USD | 14,350,000.00 USD | 9,420.00 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 24,670,000.00 USD | 24,670,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 721,900.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 14,340,000.00 USD | 14,340,000.00 USD | 7,140.00 USD | 7,360.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 24,460,000.00 USD | 24,460,000.00 USD | 158,760.00 USD | 98,760.00 USD | 347,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 267,100.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 14,290,000.00 USD | 14,290,000.00 USD | 17,790.00 USD | 0.00 USD | 459.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 23,860,000.00 USD | 23,860,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 190,830.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 14,270,000.00 USD | 14,270,000.00 USD | 39,100.00 USD | 45,090.00 USD | 135,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 23,660,000.00 USD | 23,660,000.00 USD | 97,300.00 USD | 30,180.00 USD | 341,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 57,070.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 14,050,000.00 USD | 14,050,000.00 USD | 35,390.00 USD | 55,880.00 USD | 37,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 23,190,000.00 USD | 23,190,000.00 USD | 286,870.00 USD | 79,100.00 USD | 107,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 78,280.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 13,920,000.00 USD | 13,920,000.00 USD | 216,420.00 USD | 38,360.00 USD | 181,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 22,720,000.00 USD | 22,720,000.00 USD | 374,140.00 USD | 57,440.00 USD | 218,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 101,240.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 13,480,000.00 USD | 13,480,000.00 USD | 253,600.00 USD | 126,760.00 USD | 134,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 22,070,000.00 USD | 22,070,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 55,880.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 12,970,000.00 USD | 12,970,000.00 USD | 24,940.00 USD | 58,100.00 USD | 78,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 21,420,000.00 USD | 21,420,000.00 USD | 310,530.00 USD | 146,010.00 USD | 174,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 306,880.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 12,810,000.00 USD | 12,810,000.00 USD | 55,780.00 USD | 91,390.00 USD | 98,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 20,790,000.00 USD | 20,790,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 19,800.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 12,560,000.00 USD | 12,560,000.00 USD | 118,210.00 USD | 43,080.00 USD | 63,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 20,100,000.00 USD | 20,100,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 372,630.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 12,340,000.00 USD | 12,340,000.00 USD | 287,670.00 USD | 60,530.00 USD | 170,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 19,580,000.00 USD | 19,580,000.00 USD | 215,210.00 USD | 89,120.00 USD | 671,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 678,960.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 11,820,000.00 USD | 11,820,000.00 USD | 109,420.00 USD | 162,810.00 USD | 486,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 18,600,000.00 USD | 18,600,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 163,230.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 11,060,000.00 USD | 11,060,000.00 USD | 66,630.00 USD | 118,560.00 USD | 315.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 17,260,000.00 USD | 17,260,000.00 USD | 312,160.00 USD | 149,940.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 107,780.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 10,870,000.00 USD | 10,870,000.00 USD | 498,330.00 USD | 97,910.00 USD | 375,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 16,680,000.00 USD | 16,680,000.00 USD | 846,580.00 USD | 161,970.00 USD | 785,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 148,660.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.23` | 9,900,000.00 USD | 9,900,000.00 USD | 710,180.00 USD | 324,910.00 USD | 375,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 14,880,000.00 USD | 14,880,000.00 USD | 1,080,000.00 USD | 593,230.00 USD | 739,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 76,430.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 8,490,000.00 USD | 8,490,000.00 USD | 232,690.00 USD | 220,350.00 USD | 236,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 12,470,000.00 USD | 12,470,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 13,830.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.25` | 7,800,000.00 USD | 7,800,000.00 USD | 365,010.00 USD | 239,130.00 USD | 385,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 10,760,000.00 USD | 10,760,000.00 USD | 350,470.00 USD | 433,770.00 USD | 647,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 551,090.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.26` | 6,810,000.00 USD | 6,810,000.00 USD | 334,900.00 USD | 106,500.00 USD | 280,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 9,330,000.00 USD | 9,330,000.00 USD | 1,530,000.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 47,330.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.27` | 6,090,000.00 USD | 6,090,000.00 USD | 607,160.00 USD | 199,830.00 USD | 432,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 7,070,000.00 USD | 7,070,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.28` | 14,010.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 4,850,000.00 USD | 4,850,000.00 USD | 315,460.00 USD | 283,680.00 USD | 173,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 4,650,000.00 USD | 4,650,000.00 USD | 834,930.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 22,440.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.29` | 4,080,000.00 USD | 4,080,000.00 USD | 246,310.00 USD | 24,960.00 USD | 103,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 13,840.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.30` | 3,700,000.00 USD | 3,700,000.00 USD | 223,190.00 USD | 139,890.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.30` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.30` | 15,940.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.31` | 3,320,000.00 USD | 3,320,000.00 USD | 195,160.00 USD | 136,150.00 USD | 314,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 2,070,000.00 USD | 2,070,000.00 USD | 88,750.00 USD | 0.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.32` | 97,460.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 2,670,000.00 USD | 2,670,000.00 USD | 243,570.00 USD | 69,840.00 USD | 193,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 77,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.33` | 4,790.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.33` | 2,170,000.00 USD | 2,170,000.00 USD | 214,670.00 USD | 85,110.00 USD | 105,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.33` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 112,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.34` | 1,760,000.00 USD | 1,760,000.00 USD | 147,730.00 USD | 82,560.00 USD | 210,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 137,930.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.34` | 30,420.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.35` | 1,320,000.00 USD | 1,320,000.00 USD | 64,860.00 USD | 21,470.00 USD | 105,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 1,480,000.00 USD | 1,480,000.00 USD | 93,250.00 USD | 39,140.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.36` | 1,090.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.36` | 1,130,000.00 USD | 1,130,000.00 USD | 36,420.00 USD | 34,190.00 USD | 54,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.36` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 86,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.37` | 67,460.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.37` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 18,760.00 USD | 177.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 81,030.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.38` | 984,410.00 USD | 984,410.00 USD | 60,040.00 USD | 19,120.00 USD | 49,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.38` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 93,060.00 USD | 197,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.38` | 662,490.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.39` | 856,200.00 USD | 856,200.00 USD | 40,390.00 USD | 151,010.00 USD | 46,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.39` | 884,480.00 USD | 884,480.00 USD | 0.00 USD | 62,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.39` | 36,850.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.40` | 618,720.00 USD | 618,720.00 USD | 65,980.00 USD | 170,160.00 USD | 311,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.40` | 821,630.00 USD | 821,630.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.41` | 1,090,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.41` | 70,650.00 USD | 70,650.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.41` | 421,440.00 USD | 421,440.00 USD | 308,040.00 USD | 0.00 USD | 113,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.42` | 3,340.00 USD | 14,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.42` | 222.88 USD | 222.88 USD | 0.00 USD | 0.00 USD | 39.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.42` | 9,760.00 USD | 10,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.43` | 183.82 USD | 183.82 USD | 0.00 USD | 0.00 USD | 138.68 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.43` | 970.38 USD | 970.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.44` | 45.14 USD | 45.14 USD | 0.00 USD | 0.00 USD | 45.14 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 232.47 USD | 3,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 76,550.00 USD | 76,550.00 USD | 76,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 153,090.00 USD | 153,090.00 USD | 76,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 146,190.00 USD | 146,190.00 USD | 146,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.47` | 187,320.00 USD | 187,320.00 USD | 34,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 280,880.00 USD | 280,880.00 USD | 132,630.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.48` | 187,500.00 USD | 187,500.00 USD | 0.00 USD | 0.00 USD | 184.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 281,830.00 USD | 281,830.00 USD | 0.00 USD | 0.00 USD | 949.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 189,930.00 USD | 189,930.00 USD | 2,050.00 USD | 0.00 USD | 380.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 525,050.00 USD | 525,050.00 USD | 242,770.00 USD | 0.00 USD | 451.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 655,610.00 USD | 655,610.00 USD | 316,670.00 USD | 148,800.00 USD | 210.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 1,990,000.00 USD | 1,990,000.00 USD | 828,400.00 USD | 640,730.00 USD | 504.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.51` | 1,360,000.00 USD | 1,360,000.00 USD | 457,360.00 USD | 242,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 186,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 2,470,000.00 USD | 2,470,000.00 USD | 552,290.00 USD | 187,770.00 USD | 373,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 3,050,000.00 USD | 3,050,000.00 USD | 361,140.00 USD | 316,520.00 USD | 191,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.53` | 4,130,000.00 USD | 4,130,000.00 USD | 815,730.00 USD | 106,640.00 USD | 737,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 3,600,000.00 USD | 3,600,000.00 USD | 214,030.00 USD | 99,290.00 USD | 236,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 5,460,000.00 USD | 5,460,000.00 USD | 376,850.00 USD | 262,370.00 USD | 690,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 5,610,000.00 USD | 5,610,000.00 USD | 581,730.00 USD | 328,480.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.55` | 6,680,000.00 USD | 6,680,000.00 USD | 653,340.00 USD | 254,800.00 USD | 312,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 6,850,000.00 USD | 6,850,000.00 USD | 989,010.00 USD | 174,120.00 USD | 80,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 7,520,000.00 USD | 7,520,000.00 USD | 435,050.00 USD | 148,170.00 USD | 253,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 7,780,000.00 USD | 7,780,000.00 USD | 361,350.00 USD | 307,230.00 USD | 261,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 8,400,000.00 USD | 8,400,000.00 USD | 314,580.00 USD | 312,090.00 USD | 253,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 8,150,000.00 USD | 8,150,000.00 USD | 198,050.00 USD | 167,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 9,520,000.00 USD | 9,520,000.00 USD | 249,850.00 USD | 222,910.00 USD | 649,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 8,300,000.00 USD | 8,300,000.00 USD | 47,710.00 USD | 22,490.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 10,560,000.00 USD | 10,560,000.00 USD | 530,370.00 USD | 191,380.00 USD | 319,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 9,830,000.00 USD | 9,830,000.00 USD | 674,410.00 USD | 214,810.00 USD | 637,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 11,260,000.00 USD | 11,260,000.00 USD | 363,790.00 USD | 84,420.00 USD | 249,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 9,950,000.00 USD | 9,950,000.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 12,290,000.00 USD | 12,290,000.00 USD | 504,130.00 USD | 131,410.00 USD | 402,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 10,360,000.00 USD | 10,360,000.00 USD | 76,670.00 USD | 181,090.00 USD | 153,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 13,210,000.00 USD | 13,210,000.00 USD | 188,210.00 USD | 215,240.00 USD | 516,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 11,210,000.00 USD | 11,210,000.00 USD | 307,400.00 USD | 83,350.00 USD | 459,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 14,340,000.00 USD | 14,340,000.00 USD | 483,130.00 USD | 208,050.00 USD | 438,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 11,750,000.00 USD | 11,750,000.00 USD | 226,350.00 USD | 43,650.00 USD | 272,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.64` | 14,860,000.00 USD | 14,860,000.00 USD | 234,120.00 USD | 263,860.00 USD | 20,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 12,610,000.00 USD | 12,610,000.00 USD | 513,660.00 USD | 254,400.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.65` | 15,380,000.00 USD | 15,380,000.00 USD | 270,310.00 USD | 84,330.00 USD | 163,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 13,460,000.00 USD | 13,460,000.00 USD | 422,980.00 USD | 134,210.00 USD | 288,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 15,800,000.00 USD | 15,800,000.00 USD | 148,530.00 USD | 92,980.00 USD | 172,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 13,720,000.00 USD | 13,720,000.00 USD | 159,750.00 USD | 31,420.00 USD | 75,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.67` | 16,300,000.00 USD | 16,300,000.00 USD | 129,030.00 USD | 103,830.00 USD | 274,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 13,770,000.00 USD | 13,770,000.00 USD | 7,760.00 USD | 0.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 16,820,000.00 USD | 16,820,000.00 USD | 287,250.00 USD | 50,360.00 USD | 175,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 14,530,000.00 USD | 14,530,000.00 USD | 381,910.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 16,980,000.00 USD | 16,980,000.00 USD | 79,980.00 USD | 0.00 USD | 85,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 14,530,000.00 USD | 14,530,000.00 USD | 2,450.00 USD | 0.00 USD | 339.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 17,030,000.00 USD | 17,030,000.00 USD | 5,620.00 USD | 38,510.00 USD | 28.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 14,610,000.00 USD | 14,610,000.00 USD | 2,860.00 USD | 37,250.00 USD | 42,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.71` | 17,030,000.00 USD | 17,030,000.00 USD | 5,150.00 USD | 0.00 USD | 471.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 14,620,000.00 USD | 14,620,000.00 USD | 9,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 17,110,000.00 USD | 17,110,000.00 USD | 4,880.00 USD | 19,440.00 USD | 54,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 14,670,000.00 USD | 14,670,000.00 USD | 7,140.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 3,920.00 USD | 7,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 17,190,000.00 USD | 17,190,000.00 USD | 4,080.00 USD | 11,800.00 USD | 60,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 14,720,000.00 USD | 14,720,000.00 USD | 54,580.00 USD | 0.00 USD | 160.93 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 4,530.00 USD | 12,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 17,590,000.00 USD | 17,590,000.00 USD | 208,880.00 USD | 39,720.00 USD | 155,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 14,800,000.00 USD | 14,800,000.00 USD | 11,160.00 USD | 0.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 2,000.00 USD | 14,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 18,030,000.00 USD | 18,030,000.00 USD | 165,010.00 USD | 93,530.00 USD | 183,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 15,260,000.00 USD | 15,260,000.00 USD | 8,240.00 USD | 108,690.00 USD | 342,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 1,720.00 USD | 16,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 18,320,000.00 USD | 18,320,000.00 USD | 32,150.00 USD | 27,300.00 USD | 228,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 16,470,000.00 USD | 16,470,000.00 USD | 942,680.00 USD | 0.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.77` | 18,640,000.00 USD | 18,640,000.00 USD | 109,820.00 USD | 102,010.00 USD | 105,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 17,340,000.00 USD | 17,340,000.00 USD | 731,680.00 USD | 31,590.00 USD | 101,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 2,620.00 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 18,870,000.00 USD | 18,870,000.00 USD | 117,090.00 USD | 78,770.00 USD | 38,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 19,020,000.00 USD | 19,020,000.00 USD | 922,010.00 USD | 605,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,750.00 USD | 23,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 19,680,000.00 USD | 19,680,000.00 USD | 472,440.00 USD | 231,110.00 USD | 100,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 19,980,000.00 USD | 19,980,000.00 USD | 713,060.00 USD | 249,310.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 63,970.00 USD | 87,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 20,240,000.00 USD | 20,240,000.00 USD | 306,250.00 USD | 220,680.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 21,370,000.00 USD | 21,370,000.00 USD | 1,070,000.00 USD | 315,940.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.80` | 1,770.00 USD | 89,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.81` | 20,890,000.00 USD | 20,890,000.00 USD | 407,750.00 USD | 120,180.00 USD | 127,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 22,000,000.00 USD | 22,000,000.00 USD | 397,490.00 USD | 125,900.00 USD | 101,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 76,590.00 USD | 165,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 21,810,000.00 USD | 21,810,000.00 USD | 295,730.00 USD | 191,140.00 USD | 433,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 24,680,000.00 USD | 24,680,000.00 USD | 998,780.00 USD | 369,430.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 167,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 22,510,000.00 USD | 22,510,000.00 USD | 260,840.00 USD | 100,910.00 USD | 330,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 26,330,000.00 USD | 26,330,000.00 USD | 820,240.00 USD | 85,680.00 USD | 739,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 22,890.00 USD | 190,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 22,730,000.00 USD | 22,730,000.00 USD | 76,430.00 USD | 28,910.00 USD | 122,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 26,760,000.00 USD | 26,760,000.00 USD | 97,300.00 USD | 9,680.00 USD | 322,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 4,440.00 USD | 194,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.85` | 23,290,000.00 USD | 23,290,000.00 USD | 182,320.00 USD | 157,810.00 USD | 210,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 28,740,000.00 USD | 28,740,000.00 USD | 487,940.00 USD | 328,780.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.86` | 99,700.00 USD | 294,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.86` | 23,870,000.00 USD | 23,870,000.00 USD | 214,210.00 USD | 43,740.00 USD | 328,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 30,150,000.00 USD | 30,150,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 83,880.00 USD | 378,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 24,210,000.00 USD | 24,210,000.00 USD | 201,810.00 USD | 86,180.00 USD | 46,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 31,210,000.00 USD | 31,210,000.00 USD | 263,700.00 USD | 136,820.00 USD | 663,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 55,260.00 USD | 433,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 24,510,000.00 USD | 24,510,000.00 USD | 11,350.00 USD | 30,820.00 USD | 265,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 32,880,000.00 USD | 32,880,000.00 USD | 388,550.00 USD | 480,980.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 114,450.00 USD | 548,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 24,780,000.00 USD | 24,780,000.00 USD | 143,310.00 USD | 46,470.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 33,460,000.00 USD | 33,460,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.89` | 104.26 USD | 548,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.90` | 25,370,000.00 USD | 25,370,000.00 USD | 79,980.00 USD | 112,960.00 USD | 391,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 34,600,000.00 USD | 34,600,000.00 USD | 446,650.00 USD | 145,910.00 USD | 541,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.91` | 25,880,000.00 USD | 25,880,000.00 USD | 292,500.00 USD | 85,510.00 USD | 134,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 36,030,000.00 USD | 36,030,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 569,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.92` | 26,360,000.00 USD | 26,360,000.00 USD | 190,700.00 USD | 89,190.00 USD | 207,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.92` | 37,770,000.00 USD | 37,770,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 12,930.00 USD | 581,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.93` | 26,700,000.00 USD | 26,700,000.00 USD | 118,690.00 USD | 64,250.00 USD | 151,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.93` | 39,320,000.00 USD | 39,320,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 582,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.94` | 26,950,000.00 USD | 26,950,000.00 USD | 36,860.00 USD | 65,310.00 USD | 144,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.94` | 40,630,000.00 USD | 40,630,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.95` | 2,180.00 USD | 584,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.95` | 27,080,000.00 USD | 27,080,000.00 USD | 79,890.00 USD | 4,170.00 USD | 46,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 41,930,000.00 USD | 41,930,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 4,170.00 USD | 588,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.96` | 27,190,000.00 USD | 27,190,000.00 USD | 69,140.00 USD | 21,750.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.96` | 43,120,000.00 USD | 43,120,000.00 USD | 602,080.00 USD | 214,910.00 USD | 375,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 7,990.00 USD | 596,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.97` | 27,280,000.00 USD | 27,280,000.00 USD | 5,050.00 USD | 7,520.00 USD | 77,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 43,500,000.00 USD | 43,500,000.00 USD | 194,450.00 USD | 72,330.00 USD | 113,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 254,030.00 USD | 850,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 44,290,000.00 USD | 44,290,000.00 USD | 436,230.00 USD | 88,580.00 USD | 270,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,710.00 USD | 852,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 44,640,000.00 USD | 44,640,000.00 USD | 127,170.00 USD | 103,060.00 USD | 116,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 267.27 USD | 852,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.01` | 30,430.00 USD | 882,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.03` | 11,040.00 USD | 893,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.04` | 1,160.00 USD | 895,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 5,020.00 USD | 900,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 903,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 212,580.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,190.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.09` | 4,170.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.13` | 167,390.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.16` | 36,460.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 11,180.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 346.72 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.18` | 12,270.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 1,040.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.21` | 28,650.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.24` | 454.40 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 7,440.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 878.04 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,630.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 39,950.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 35,920.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 40,130.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 431.61 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 42,070.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 179.03 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 2,180.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 2,270.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.49` | 52,520.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 9,490.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 256,100.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 639.34 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.64` | 754,650.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 301.98 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 11,350.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 2,410.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 32,270.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 2,730,000.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.76` | 385.10 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 6,670.00 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 6,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 68,870.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 92,430.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.93` | 40,670.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 3,860.00 USD | 6,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.96` | 127,350.00 USD | 6,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 71,940.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,210.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 6,460.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 7,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 94,120.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.14` | 487.30 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 45,700.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,610.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 1,550.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 109.43 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 536.84 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 748.53 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 540.60 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 17,930.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 1,370.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 357,670.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.82` | 40,950.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.83` | 2,200.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,410.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.93` | 61,000.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.95` | 17,480.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 9,030.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 9,930,000.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.18` | 2,920.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 38,360.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 19,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.29` | 152.47 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.39` | 474.76 USD | 19,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 7,850,000.00 USD | 27,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 27,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 106,720.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 6,880.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 27,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.64` | 1,140.00 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 2,690.00 USD | 27,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 15,530.00 USD | 27,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.78` | 33,500.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.91` | 1,250,000.00 USD | 29,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 712,350.00 USD | 29,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 32,750.00 USD | 29,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 29,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 354.53 USD | 29,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 463,480.00 USD | 30,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.04` | 404,530.00 USD | 30,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 2,130.00 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 30,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.24` | 625,070.00 USD | 31,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.29` | 3,760.00 USD | 31,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.36` | 8,460.00 USD | 31,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 32,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.39` | 25,180.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 2,350.00 USD | 32,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 18,200.00 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 594.65 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 32,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 440,790.00 USD | 32,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 2,760.00 USD | 32,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 583.96 USD | 32,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.62` | 1,910,000.00 USD | 34,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.64` | 1,880,000.00 USD | 36,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 2,320.00 USD | 36,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.70` | 16,520.00 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.71` | 31,930.00 USD | 36,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.77` | 2,630.00 USD | 36,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.78` | 4,390.00 USD | 36,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.81` | 1,280.00 USD | 36,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 19,980.00 USD | 36,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.85` | 6,380.00 USD | 36,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,500,000.00 USD | 38,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.88` | 1,800,000.00 USD | 40,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.91` | 867.43 USD | 40,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.95` | 223.62 USD | 40,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.96` | 17,370.00 USD | 40,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.96` | 19,880.00 USD | 40,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.99` | 5,720,000.00 USD | 45,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.01` | 60,030.00 USD | 45,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.05` | 814.95 USD | 45,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.14` | 11,460.00 USD | 45,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.16` | 486,070.00 USD | 46,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.9350` | 36,220,000.00 USD | 0.00 USD | 10,170.00 USD | `-79.66%` | `10,880.60` |
| `Live` | `Long` | `0.9550` | 36,210,000.00 USD | 0.00 USD | 29,450.00 USD | `-79.23%` | `30,836.80` |
| `Live` | `Long` | `0.9650` | 36,180,000.00 USD | 0.00 USD | 5,440,000.00 USD | `-79.01%` | `5,642,472.50` |
| `Live` | `Long` | `0.9750` | 30,740,000.00 USD | 0.00 USD | 17,330.00 USD | `-78.79%` | `17,777.30` |
| `Live` | `Long` | `0.9850` | 30,720,000.00 USD | 0.00 USD | 122.34 USD | `-78.57%` | `124.20` |
| `Live` | `Long` | `0.9950` | 30,720,000.00 USD | 0.00 USD | 159,280.00 USD | `-78.35%` | `160,075.90` |
| `Live` | `Long` | `1.01` | 30,560,000.00 USD | 0.00 USD | 28,030.00 USD | `-77.92%` | `27,618.30` |
| `Live` | `Long` | `1.02` | 30,530,000.00 USD | 0.00 USD | 10,250.00 USD | `-77.70%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 30,520,000.00 USD | 0.00 USD | 15,420.00 USD | `-77.48%` | `14,897.40` |
| `Live` | `Long` | `1.04` | 30,510,000.00 USD | 0.00 USD | 5,690.00 USD | `-77.27%` | `5,446.30` |
| `Live` | `Long` | `1.05` | 30,500,000.00 USD | 0.00 USD | 7,890.00 USD | `-77.05%` | `7,479.20` |
| `Live` | `Long` | `1.06` | 30,490,000.00 USD | 0.00 USD | 4,460.00 USD | `-76.83%` | `4,186.70` |
| `Live` | `Long` | `1.07` | 30,490,000.00 USD | 0.00 USD | 7,510.00 USD | `-76.61%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 30,480,000.00 USD | 0.00 USD | 8,500.00 USD | `-76.40%` | `7,837.10` |
| `Live` | `Long` | `1.09` | 30,470,000.00 USD | 0.00 USD | 75,160.00 USD | `-76.18%` | `68,637.40` |
| `Live` | `Long` | `1.10` | 30,400,000.00 USD | 0.00 USD | 26,680.00 USD | `-75.96%` | `24,148.50` |
| `Live` | `Long` | `1.11` | 30,370,000.00 USD | 0.00 USD | 1,120.00 USD | `-75.74%` | `1,006.60` |
| `Live` | `Long` | `1.12` | 30,370,000.00 USD | 0.00 USD | 650.70 USD | `-75.53%` | `578.40` |
| `Live` | `Long` | `1.14` | 30,370,000.00 USD | 0.00 USD | 4,960.00 USD | `-75.31%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 30,360,000.00 USD | 0.00 USD | 52,310.00 USD | `-75.09%` | `45,683.90` |
| `Live` | `Long` | `1.16` | 30,310,000.00 USD | 0.00 USD | 589.28 USD | `-74.87%` | `510.20` |
| `Live` | `Long` | `1.17` | 30,310,000.00 USD | 0.00 USD | 2,820.00 USD | `-74.66%` | `2,422.20` |
| `Live` | `Long` | `1.18` | 30,310,000.00 USD | 0.00 USD | 9,290.00 USD | `-74.44%` | `7,907.40` |
| `Live` | `Long` | `1.19` | 30,300,000.00 USD | 0.00 USD | 1,900.00 USD | `-74.22%` | `1,601.00` |
| `Live` | `Long` | `1.21` | 30,300,000.00 USD | 0.00 USD | 9,080.00 USD | `-73.79%` | `7,537.90` |
| `Live` | `Long` | `1.24` | 30,290,000.00 USD | 0.00 USD | 1,120.00 USD | `-73.13%` | `908.60` |
| `Live` | `Long` | `1.25` | 30,290,000.00 USD | 0.00 USD | 653.98 USD | `-72.70%` | `521.10` |
| `Live` | `Long` | `1.26` | 30,280,000.00 USD | 0.00 USD | 2,060.00 USD | `-72.48%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 30,280,000.00 USD | 0.00 USD | 2,520.00 USD | `-72.26%` | `1,975.90` |
| `Live` | `Long` | `1.28` | 30,280,000.00 USD | 0.00 USD | 408.12 USD | `-72.05%` | `317.60` |
| `Live` | `Long` | `1.29` | 30,280,000.00 USD | 0.00 USD | 447.94 USD | `-71.83%` | `345.90` |
| `Live` | `Long` | `1.30` | 30,280,000.00 USD | 0.00 USD | 116.80 USD | `-71.61%` | `89.50` |
| `Live` | `Long` | `1.32` | 30,280,000.00 USD | 0.00 USD | 2,830.00 USD | `-71.18%` | `2,132.40` |
| `Live` | `Long` | `1.33` | 30,280,000.00 USD | 0.00 USD | 2,490.00 USD | `-70.96%` | `1,867.20` |
| `Live` | `Long` | `1.34` | 30,270,000.00 USD | 0.00 USD | 28,060.00 USD | `-70.74%` | `20,864.60` |
| `Live` | `Long` | `1.35` | 30,250,000.00 USD | 0.00 USD | 236.85 USD | `-70.52%` | `174.80` |
| `Live` | `Long` | `1.36` | 30,250,000.00 USD | 0.00 USD | 795.11 USD | `-70.31%` | `582.50` |
| `Live` | `Long` | `1.38` | 30,240,000.00 USD | 0.00 USD | 12,380.00 USD | `-70.09%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 30,230,000.00 USD | 0.00 USD | 3,410.00 USD | `-69.87%` | `2,459.80` |
| `Live` | `Long` | `1.40` | 30,230,000.00 USD | 0.00 USD | 157.50 USD | `-69.65%` | `112.90` |
| `Live` | `Long` | `1.42` | 30,230,000.00 USD | 0.00 USD | 37,460.00 USD | `-69.22%` | `26,470.40` |
| `Live` | `Long` | `1.43` | 30,190,000.00 USD | 0.00 USD | 20,260.00 USD | `-69.00%` | `14,219.60` |
| `Live` | `Long` | `1.45` | 30,170,000.00 USD | 0.00 USD | 3,000.00 USD | `-68.57%` | `2,077.30` |
| `Live` | `Long` | `1.46` | 30,170,000.00 USD | 0.00 USD | 7,080.00 USD | `-68.35%` | `4,867.40` |
| `Live` | `Long` | `1.48` | 30,160,000.00 USD | 0.00 USD | 3,330.00 USD | `-67.91%` | `2,254.90` |
| `Live` | `Long` | `1.50` | 30,160,000.00 USD | 0.00 USD | 4,420.00 USD | `-67.26%` | `2,938.80` |
| `Live` | `Long` | `1.51` | 30,150,000.00 USD | 0.00 USD | 454.50 USD | `-67.04%` | `300.00` |
| `Live` | `Long` | `1.52` | 30,150,000.00 USD | 0.00 USD | 610.00 USD | `-66.83%` | `400.00` |
| `Live` | `Long` | `1.53` | 30,150,000.00 USD | 0.00 USD | 2,360.00 USD | `-66.61%` | `1,536.00` |
| `Live` | `Long` | `1.55` | 30,150,000.00 USD | 0.00 USD | 146,570.00 USD | `-66.17%` | `94,258.00` |
| `Live` | `Long` | `1.56` | 30,000,000.00 USD | 0.00 USD | 32,200.00 USD | `-65.96%` | `20,574.30` |
| `Live` | `Long` | `1.57` | 29,970,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-65.74%` | `900,675.60` |
| `Live` | `Long` | `1.58` | 28,550,000.00 USD | 0.00 USD | 7,540.00 USD | `-65.52%` | `4,758.20` |
| `Live` | `Long` | `1.59` | 28,550,000.00 USD | 0.00 USD | 7,660.00 USD | `-65.30%` | `4,801.70` |
| `Live` | `Long` | `1.60` | 28,540,000.00 USD | 0.00 USD | 191.64 USD | `-65.09%` | `119.40` |
| `Live` | `Long` | `1.61` | 28,540,000.00 USD | 0.00 USD | 807.50 USD | `-64.87%` | `500.00` |
| `Live` | `Long` | `1.62` | 28,540,000.00 USD | 0.00 USD | 1,620.00 USD | `-64.65%` | `1,000.00` |
| `Live` | `Long` | `1.64` | 28,530,000.00 USD | 0.00 USD | 16,800.00 USD | `-64.43%` | `10,275.40` |
| `Live` | `Long` | `1.65` | 28,520,000.00 USD | 0.00 USD | 981.08 USD | `-64.22%` | `596.40` |
| `Live` | `Long` | `1.66` | 28,520,000.00 USD | 0.00 USD | 92,960.00 USD | `-64.00%` | `56,172.10` |
| `Live` | `Long` | `1.67` | 28,420,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.78%` | `664.10` |
| `Live` | `Long` | `1.68` | 28,420,000.00 USD | 0.00 USD | 1,560.00 USD | `-63.56%` | `933.30` |
| `Live` | `Long` | `1.69` | 28,420,000.00 USD | 0.00 USD | 15,740.00 USD | `-63.34%` | `9,338.80` |
| `Live` | `Long` | `1.70` | 28,410,000.00 USD | 0.00 USD | 7,770.00 USD | `-63.13%` | `4,586.00` |
| `Live` | `Long` | `1.72` | 28,400,000.00 USD | 0.00 USD | 6,660.00 USD | `-62.69%` | `3,883.20` |
| `Live` | `Long` | `1.73` | 28,390,000.00 USD | 0.00 USD | 5,460.00 USD | `-62.47%` | `3,164.50` |
| `Live` | `Long` | `1.74` | 28,390,000.00 USD | 0.00 USD | 1,560.00 USD | `-62.26%` | `900.00` |
| `Live` | `Long` | `1.75` | 28,380,000.00 USD | 0.00 USD | 32,210.00 USD | `-62.04%` | `18,455.90` |
| `Live` | `Long` | `1.75` | 28,350,000.00 USD | 0.00 USD | 68,650.00 USD | `-61.82%` | `39,114.20` |
| `Live` | `Long` | `1.76` | 28,280,000.00 USD | 0.00 USD | 211.80 USD | `-61.60%` | `120.00` |
| `Live` | `Long` | `1.77` | 28,280,000.00 USD | 0.00 USD | 78,220.00 USD | `-61.39%` | `44,069.00` |
| `Live` | `Long` | `1.78` | 28,200,000.00 USD | 0.00 USD | 303.45 USD | `-61.17%` | `170.00` |
| `Live` | `Long` | `1.79` | 28,200,000.00 USD | 0.00 USD | 179,870.00 USD | `-60.95%` | `100,207.20` |
| `Live` | `Long` | `1.80` | 28,020,000.00 USD | 0.00 USD | 5,410.00 USD | `-60.73%` | `2,997.90` |
| `Live` | `Long` | `1.81` | 28,020,000.00 USD | 0.00 USD | 100.55 USD | `-60.52%` | `55.40` |
| `Live` | `Long` | `1.83` | 28,020,000.00 USD | 0.00 USD | 27,520.00 USD | `-60.08%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 27,990,000.00 USD | 0.00 USD | 1,290.00 USD | `-59.86%` | `700.20` |
| `Live` | `Long` | `1.85` | 27,990,000.00 USD | 0.00 USD | 5,790.00 USD | `-59.65%` | `3,120.40` |
| `Live` | `Long` | `1.86` | 27,980,000.00 USD | 0.00 USD | 239,650.00 USD | `-59.43%` | `128,500.70` |
| `Live` | `Long` | `1.88` | 27,750,000.00 USD | 0.00 USD | 937.50 USD | `-59.21%` | `500.00` |
| `Live` | `Long` | `1.89` | 27,740,000.00 USD | 0.00 USD | 5,830.00 USD | `-58.99%` | `3,091.50` |
| `Live` | `Long` | `1.90` | 27,740,000.00 USD | 0.00 USD | 2,340.00 USD | `-58.78%` | `1,233.80` |
| `Live` | `Long` | `1.91` | 27,740,000.00 USD | 0.00 USD | 4,280.00 USD | `-58.56%` | `2,248.00` |
| `Live` | `Long` | `1.93` | 27,730,000.00 USD | 0.00 USD | 918.42 USD | `-58.12%` | `477.10` |
| `Live` | `Long` | `1.95` | 27,730,000.00 USD | 0.00 USD | 2,740.00 USD | `-57.69%` | `1,410.10` |
| `Live` | `Long` | `1.97` | 27,730,000.00 USD | 0.00 USD | 6,970.00 USD | `-57.25%` | `3,546.60` |
| `Live` | `Long` | `1.98` | 27,720,000.00 USD | 0.00 USD | 41,390.00 USD | `-57.04%` | `20,957.80` |
| `Live` | `Long` | `2.00` | 27,680,000.00 USD | 0.00 USD | 124,790.00 USD | `-56.38%` | `62,238.70` |
| `Live` | `Long` | `2.02` | 27,550,000.00 USD | 0.00 USD | 506.37 USD | `-56.17%` | `251.30` |
| `Live` | `Long` | `2.02` | 27,550,000.00 USD | 0.00 USD | 104,370.00 USD | `-55.95%` | `51,540.50` |
| `Live` | `Long` | `2.04` | 27,450,000.00 USD | 0.00 USD | 85,840.00 USD | `-55.73%` | `42,179.40` |
| `Live` | `Long` | `2.04` | 27,360,000.00 USD | 0.00 USD | 4,560.00 USD | `-55.51%` | `2,230.40` |
| `Live` | `Long` | `2.08` | 27,360,000.00 USD | 0.00 USD | 1,960.00 USD | `-54.86%` | `942.60` |
| `Live` | `Long` | `2.08` | 27,360,000.00 USD | 0.00 USD | 17,190.00 USD | `-54.64%` | `8,245.00` |
| `Live` | `Long` | `2.10` | 27,340,000.00 USD | 0.00 USD | 28,510.00 USD | `-54.43%` | `13,607.20` |
| `Live` | `Long` | `2.10` | 27,310,000.00 USD | 0.00 USD | 5,880.00 USD | `-54.21%` | `2,794.70` |
| `Live` | `Long` | `2.12` | 27,310,000.00 USD | 0.00 USD | 12,760.00 USD | `-53.99%` | `6,032.50` |
| `Live` | `Long` | `2.12` | 27,290,000.00 USD | 0.00 USD | 4,700.00 USD | `-53.77%` | `2,211.00` |
| `Live` | `Long` | `2.13` | 27,290,000.00 USD | 0.00 USD | 2,230.00 USD | `-53.56%` | `1,045.80` |
| `Live` | `Long` | `2.15` | 27,290,000.00 USD | 0.00 USD | 161,930.00 USD | `-53.12%` | `75,141.50` |
| `Live` | `Long` | `2.17` | 27,120,000.00 USD | 0.00 USD | 543.75 USD | `-52.69%` | `250.00` |
| `Live` | `Long` | `2.19` | 27,120,000.00 USD | 0.00 USD | 24,920.00 USD | `-52.47%` | `11,403.20` |
| `Live` | `Long` | `2.19` | 27,100,000.00 USD | 0.00 USD | 11,120.00 USD | `-52.25%` | `5,064.00` |
| `Live` | `Long` | `2.21` | 27,090,000.00 USD | 0.00 USD | 600,160.00 USD | `-52.03%` | `272,183.20` |
| `Live` | `Long` | `2.23` | 26,490,000.00 USD | 0.00 USD | 11,120.00 USD | `-51.60%` | `5,000.00` |
| `Live` | `Long` | `2.23` | 26,480,000.00 USD | 0.00 USD | 27,790.00 USD | `-51.38%` | `12,434.60` |
| `Live` | `Long` | `2.25` | 26,450,000.00 USD | 0.00 USD | 58,480.00 USD | `-51.16%` | `26,050.00` |
| `Live` | `Long` | `2.25` | 26,390,000.00 USD | 0.00 USD | 124,730.00 USD | `-50.95%` | `55,313.30` |
| `Live` | `Long` | `2.27` | 26,270,000.00 USD | 0.00 USD | 152,580.00 USD | `-50.73%` | `67,362.10` |
| `Live` | `Long` | `2.27` | 26,110,000.00 USD | 0.00 USD | 2,030.00 USD | `-50.51%` | `891.50` |
| `Live` | `Long` | `2.29` | 26,110,000.00 USD | 0.00 USD | 804.32 USD | `-50.29%` | `352.00` |
| `Live` | `Long` | `2.29` | 26,110,000.00 USD | 0.00 USD | 5,250.00 USD | `-50.08%` | `2,286.90` |
| `Live` | `Long` | `2.31` | 26,100,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-49.86%` | `653,387.20` |
| `Live` | `Long` | `2.31` | 24,600,000.00 USD | 0.00 USD | 440.31 USD | `-49.64%` | `190.20` |
| `Live` | `Long` | `2.33` | 24,600,000.00 USD | 0.00 USD | 3,460.00 USD | `-49.42%` | `1,489.70` |
| `Live` | `Long` | `2.33` | 24,590,000.00 USD | 0.00 USD | 1,270.00 USD | `-49.20%` | `543.20` |
| `Live` | `Long` | `2.35` | 24,590,000.00 USD | 0.00 USD | 50,580.00 USD | `-48.99%` | `21,570.00` |
| `Live` | `Long` | `2.35` | 24,540,000.00 USD | 0.00 USD | 5,650.00 USD | `-48.77%` | `2,399.90` |
| `Live` | `Long` | `2.37` | 24,540,000.00 USD | 0.00 USD | 65,220.00 USD | `-48.55%` | `27,576.50` |
| `Live` | `Long` | `2.38` | 24,470,000.00 USD | 0.00 USD | 430,380.00 USD | `-48.33%` | `181,213.40` |
| `Live` | `Long` | `2.38` | 24,040,000.00 USD | 0.00 USD | 534.24 USD | `-48.12%` | `224.00` |
| `Live` | `Long` | `2.40` | 24,040,000.00 USD | 0.00 USD | 386,250.00 USD | `-47.90%` | `161,275.30` |
| `Live` | `Long` | `2.40` | 23,660,000.00 USD | 0.00 USD | 2,430.00 USD | `-47.68%` | `1,011.10` |
| `Live` | `Long` | `2.42` | 23,650,000.00 USD | 0.00 USD | 185,860.00 USD | `-47.46%` | `76,961.80` |
| `Live` | `Long` | `2.42` | 23,470,000.00 USD | 0.00 USD | 485.00 USD | `-47.25%` | `200.00` |
| `Live` | `Long` | `2.44` | 23,470,000.00 USD | 0.00 USD | 29,790.00 USD | `-47.03%` | `12,233.60` |
| `Live` | `Long` | `2.46` | 23,440,000.00 USD | 0.00 USD | 2,760.00 USD | `-46.59%` | `1,124.60` |
| `Live` | `Long` | `2.46` | 23,430,000.00 USD | 0.00 USD | 10,580.00 USD | `-46.38%` | `4,293.90` |
| `Live` | `Long` | `2.48` | 23,420,000.00 USD | 0.00 USD | 259,350.00 USD | `-46.16%` | `104,789.00` |
| `Live` | `Long` | `2.48` | 23,160,000.00 USD | 0.00 USD | 2,760.00 USD | `-45.94%` | `1,112.50` |
| `Live` | `Long` | `2.50` | 23,160,000.00 USD | 0.00 USD | 2,040.00 USD | `-45.72%` | `818.30` |
| `Live` | `Long` | `2.50` | 23,160,000.00 USD | 0.00 USD | 24,490.00 USD | `-45.51%` | `9,777.80` |
| `Live` | `Long` | `2.52` | 23,130,000.00 USD | 0.00 USD | 10,690.00 USD | `-45.29%` | `4,250.30` |
| `Live` | `Long` | `2.52` | 23,120,000.00 USD | 0.00 USD | 22,690.00 USD | `-45.07%` | `8,987.90` |
| `Live` | `Long` | `2.54` | 23,100,000.00 USD | 0.00 USD | 395.71 USD | `-44.85%` | `156.10` |
| `Live` | `Long` | `2.54` | 23,100,000.00 USD | 0.00 USD | 186,320.00 USD | `-44.64%` | `73,209.80` |
| `Live` | `Long` | `2.56` | 22,910,000.00 USD | 0.00 USD | 694.96 USD | `-44.42%` | `272.00` |
| `Live` | `Long` | `2.56` | 22,910,000.00 USD | 0.00 USD | 10,460.00 USD | `-44.20%` | `4,077.60` |
| `Live` | `Long` | `2.58` | 22,900,000.00 USD | 0.00 USD | 67,580.00 USD | `-43.77%` | `26,142.70` |
| `Live` | `Long` | `2.60` | 22,840,000.00 USD | 0.00 USD | 5,890.00 USD | `-43.55%` | `2,268.00` |
| `Live` | `Long` | `2.60` | 22,830,000.00 USD | 0.00 USD | 301.40 USD | `-43.33%` | `115.70` |
| `Live` | `Long` | `2.62` | 22,830,000.00 USD | 0.00 USD | 6,420.00 USD | `-43.11%` | `2,454.70` |
| `Live` | `Long` | `2.62` | 22,820,000.00 USD | 0.00 USD | 1,760.00 USD | `-42.90%` | `670.50` |
| `Live` | `Long` | `2.63` | 22,820,000.00 USD | 0.00 USD | 55,020.00 USD | `-42.68%` | `20,879.50` |
| `Live` | `Long` | `2.65` | 22,770,000.00 USD | 0.00 USD | 186,060.00 USD | `-42.46%` | `70,342.80` |
| `Live` | `Long` | `2.65` | 22,580,000.00 USD | 0.00 USD | 18,620.00 USD | `-42.24%` | `7,012.60` |
| `Live` | `Long` | `2.67` | 22,560,000.00 USD | 0.00 USD | 19,240.00 USD | `-42.03%` | `7,219.00` |
| `Live` | `Long` | `2.67` | 22,540,000.00 USD | 0.00 USD | 3,050.00 USD | `-41.81%` | `1,140.50` |
| `Live` | `Long` | `2.69` | 22,540,000.00 USD | 0.00 USD | 4,860.00 USD | `-41.59%` | `1,809.60` |
| `Live` | `Long` | `2.69` | 22,530,000.00 USD | 0.00 USD | 10,340.00 USD | `-41.37%` | `3,837.50` |
| `Live` | `Long` | `2.71` | 22,520,000.00 USD | 0.00 USD | 121,210.00 USD | `-41.16%` | `44,809.80` |
| `Live` | `Long` | `2.71` | 22,400,000.00 USD | 0.00 USD | 11,970.00 USD | `-40.94%` | `4,408.30` |
| `Live` | `Long` | `2.73` | 22,390,000.00 USD | 0.00 USD | 40,930.00 USD | `-40.72%` | `15,020.90` |
| `Live` | `Long` | `2.73` | 22,350,000.00 USD | 0.00 USD | 1,850.00 USD | `-40.50%` | `675.80` |
| `Live` | `Long` | `2.75` | 22,350,000.00 USD | 0.00 USD | 39,550.00 USD | `-40.29%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 22,310,000.00 USD | 0.00 USD | 1,960.00 USD | `-40.07%` | `711.70` |
| `Live` | `Long` | `2.77` | 22,310,000.00 USD | 0.00 USD | 3,850.00 USD | `-39.85%` | `1,391.40` |
| `Live` | `Long` | `2.77` | 22,300,000.00 USD | 0.00 USD | 1,800.00 USD | `-39.63%` | `649.90` |
| `Live` | `Long` | `2.79` | 22,300,000.00 USD | 0.00 USD | 24,840.00 USD | `-39.42%` | `8,920.90` |
| `Live` | `Long` | `2.79` | 22,280,000.00 USD | 0.00 USD | 10,720.00 USD | `-39.20%` | `3,836.20` |
| `Live` | `Long` | `2.81` | 22,270,000.00 USD | 0.00 USD | 200,600.00 USD | `-38.98%` | `71,515.00` |
| `Live` | `Long` | `2.81` | 22,060,000.00 USD | 0.00 USD | 694.18 USD | `-38.76%` | `246.60` |
| `Live` | `Long` | `2.83` | 22,060,000.00 USD | 0.00 USD | 6,480.00 USD | `-38.55%` | `2,292.20` |
| `Live` | `Long` | `2.83` | 22,060,000.00 USD | 0.00 USD | 539,720.00 USD | `-38.33%` | `190,377.40` |
| `Live` | `Long` | `2.85` | 21,520,000.00 USD | 0.00 USD | 6,970.00 USD | `-38.11%` | `2,449.80` |
| `Live` | `Long` | `2.85` | 21,510,000.00 USD | 0.00 USD | 3,050.00 USD | `-37.89%` | `1,069.60` |
| `Live` | `Long` | `2.87` | 21,510,000.00 USD | 0.00 USD | 5,190.00 USD | `-37.68%` | `1,810.40` |
| `Live` | `Long` | `2.88` | 21,500,000.00 USD | 0.00 USD | 5,990.00 USD | `-37.46%` | `2,081.80` |
| `Live` | `Long` | `2.88` | 21,500,000.00 USD | 0.00 USD | 6,600.00 USD | `-37.24%` | `2,286.30` |
| `Live` | `Long` | `2.90` | 21,490,000.00 USD | 0.00 USD | 18,250.00 USD | `-37.02%` | `6,304.60` |
| `Live` | `Long` | `2.90` | 21,470,000.00 USD | 0.00 USD | 22,220.00 USD | `-36.81%` | `7,649.70` |
| `Live` | `Long` | `2.92` | 21,450,000.00 USD | 0.00 USD | 6,000.00 USD | `-36.59%` | `2,056.80` |
| `Live` | `Long` | `2.92` | 21,440,000.00 USD | 0.00 USD | 116.12 USD | `-36.37%` | `39.70` |
| `Live` | `Long` | `2.94` | 21,440,000.00 USD | 0.00 USD | 63,540.00 USD | `-36.15%` | `21,647.60` |
| `Live` | `Long` | `2.96` | 21,380,000.00 USD | 0.00 USD | 2,170.00 USD | `-35.72%` | `735.00` |
| `Live` | `Long` | `2.96` | 21,380,000.00 USD | 0.00 USD | 7,160.00 USD | `-35.50%` | `2,413.80` |
| `Live` | `Long` | `2.98` | 21,370,000.00 USD | 0.00 USD | 12,620.00 USD | `-35.28%` | `4,243.30` |
| `Live` | `Long` | `2.98` | 21,360,000.00 USD | 0.00 USD | 26,040.00 USD | `-35.06%` | `8,723.50` |
| `Live` | `Long` | `3.00` | 21,330,000.00 USD | 0.00 USD | 2,000.00 USD | `-34.85%` | `666.40` |
| `Live` | `Long` | `3.00` | 21,330,000.00 USD | 0.00 USD | 119,700.00 USD | `-34.63%` | `39,834.30` |
| `Live` | `Long` | `3.02` | 21,210,000.00 USD | 0.00 USD | 29,380.00 USD | `-34.41%` | `9,743.00` |
| `Live` | `Long` | `3.02` | 21,180,000.00 USD | 0.00 USD | 15,760.00 USD | `-34.19%` | `5,210.70` |
| `Live` | `Long` | `3.04` | 21,170,000.00 USD | 0.00 USD | 358,170.00 USD | `-33.98%` | `118,012.40` |
| `Live` | `Long` | `3.04` | 20,810,000.00 USD | 0.00 USD | 119,150.00 USD | `-33.76%` | `39,129.30` |
| `Live` | `Long` | `3.06` | 20,690,000.00 USD | 0.00 USD | 22,550.00 USD | `-33.54%` | `7,381.60` |
| `Live` | `Long` | `3.06` | 20,670,000.00 USD | 0.00 USD | 115,720.00 USD | `-33.32%` | `37,754.10` |
| `Live` | `Long` | `3.08` | 20,550,000.00 USD | 0.00 USD | 3,090.00 USD | `-33.11%` | `1,004.70` |
| `Live` | `Long` | `3.08` | 20,550,000.00 USD | 0.00 USD | 13,030.00 USD | `-32.89%` | `4,223.20` |
| `Live` | `Long` | `3.10` | 20,530,000.00 USD | 0.00 USD | 4,930.00 USD | `-32.67%` | `1,594.30` |
| `Live` | `Long` | `3.10` | 20,530,000.00 USD | 0.00 USD | 36,570.00 USD | `-32.45%` | `11,777.50` |
| `Live` | `Long` | `3.12` | 20,490,000.00 USD | 0.00 USD | 80,900.00 USD | `-32.24%` | `25,970.90` |
| `Live` | `Long` | `3.12` | 20,410,000.00 USD | 0.00 USD | 10,480.00 USD | `-32.02%` | `3,352.80` |
| `Live` | `Long` | `3.13` | 20,400,000.00 USD | 0.00 USD | 38,530.00 USD | `-31.80%` | `12,290.90` |
| `Live` | `Long` | `3.15` | 20,360,000.00 USD | 0.00 USD | 30,120.00 USD | `-31.58%` | `9,578.30` |
| `Live` | `Long` | `3.15` | 20,330,000.00 USD | 0.00 USD | 2,220.00 USD | `-31.37%` | `703.30` |
| `Live` | `Long` | `3.17` | 20,330,000.00 USD | 0.00 USD | 52,770.00 USD | `-31.15%` | `16,673.20` |
| `Live` | `Long` | `3.17` | 20,280,000.00 USD | 0.00 USD | 111,270.00 USD | `-30.93%` | `35,046.40` |
| `Live` | `Long` | `3.19` | 20,170,000.00 USD | 0.00 USD | 10,060.00 USD | `-30.71%` | `3,157.90` |
| `Live` | `Long` | `3.19` | 20,160,000.00 USD | 0.00 USD | 5,820.00 USD | `-30.50%` | `1,822.60` |
| `Live` | `Long` | `3.21` | 20,150,000.00 USD | 0.00 USD | 103,170.00 USD | `-30.28%` | `32,189.70` |
| `Live` | `Long` | `3.21` | 20,050,000.00 USD | 0.00 USD | 28,430.00 USD | `-30.06%` | `8,844.20` |
| `Live` | `Long` | `3.23` | 20,020,000.00 USD | 0.00 USD | 21,640.00 USD | `-29.84%` | `6,709.70` |
| `Live` | `Long` | `3.23` | 20,000,000.00 USD | 0.00 USD | 19,880.00 USD | `-29.63%` | `6,144.90` |
| `Live` | `Long` | `3.25` | 19,980,000.00 USD | 0.00 USD | 276,210.00 USD | `-29.41%` | `85,119.60` |
| `Live` | `Long` | `3.25` | 19,700,000.00 USD | 0.00 USD | 59,690.00 USD | `-29.19%` | `18,338.20` |
| `Live` | `Long` | `3.27` | 19,640,000.00 USD | 0.00 USD | 37,050.00 USD | `-28.97%` | `11,346.20` |
| `Live` | `Long` | `3.27` | 19,600,000.00 USD | 0.00 USD | 835,690.00 USD | `-28.76%` | `255,173.10` |
| `Live` | `Long` | `3.29` | 18,770,000.00 USD | 0.00 USD | 5,600.00 USD | `-28.54%` | `1,704.30` |
| `Live` | `Long` | `3.29` | 18,760,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-28.32%` | `425,278.00` |
| `Live` | `Long` | `3.31` | 17,360,000.00 USD | 0.00 USD | 58,360.00 USD | `-28.10%` | `17,658.90` |
| `Live` | `Long` | `3.31` | 17,300,000.00 USD | 0.00 USD | 64,720.00 USD | `-27.89%` | `19,521.90` |
| `Live` | `Long` | `3.33` | 17,240,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.67%` | `2,043.90` |
| `Live` | `Long` | `3.33` | 17,230,000.00 USD | 0.00 USD | 54,740.00 USD | `-27.45%` | `16,414.80` |
| `Live` | `Long` | `3.35` | 17,180,000.00 USD | 0.00 USD | 32,850.00 USD | `-27.23%` | `9,822.10` |
| `Live` | `Long` | `3.35` | 17,140,000.00 USD | 0.00 USD | 5,110.00 USD | `-27.02%` | `1,523.20` |
| `Live` | `Long` | `3.37` | 17,140,000.00 USD | 0.00 USD | 5,240.00 USD | `-26.80%` | `1,558.40` |
| `Live` | `Long` | `3.38` | 17,130,000.00 USD | 0.00 USD | 14,490.00 USD | `-26.58%` | `4,293.30` |
| `Live` | `Long` | `3.38` | 17,120,000.00 USD | 0.00 USD | 45,540.00 USD | `-26.36%` | `13,452.60` |
| `Live` | `Long` | `3.40` | 17,070,000.00 USD | 0.00 USD | 8,730.00 USD | `-26.15%` | `2,570.90` |
| `Live` | `Long` | `3.40` | 17,060,000.00 USD | 0.00 USD | 97,200.00 USD | `-25.93%` | `28,546.80` |
| `Live` | `Long` | `3.42` | 16,970,000.00 USD | 0.00 USD | 187,920.00 USD | `-25.71%` | `55,029.00` |
| `Live` | `Long` | `3.42` | 16,780,000.00 USD | 0.00 USD | 6,530.00 USD | `-25.49%` | `1,905.40` |
| `Live` | `Long` | `3.44` | 16,770,000.00 USD | 0.00 USD | 25,060.00 USD | `-25.28%` | `7,295.20` |
| `Live` | `Long` | `3.44` | 16,750,000.00 USD | 0.00 USD | 40,920.00 USD | `-25.06%` | `11,879.50` |
| `Live` | `Long` | `3.46` | 16,710,000.00 USD | 0.00 USD | 21,600.00 USD | `-24.84%` | `6,253.20` |
| `Live` | `Long` | `3.46` | 16,690,000.00 USD | 0.00 USD | 11,390.00 USD | `-24.62%` | `3,286.70` |
| `Live` | `Long` | `3.48` | 16,670,000.00 USD | 0.00 USD | 77,730.00 USD | `-24.41%` | `22,369.60` |
| `Live` | `Long` | `3.48` | 16,600,000.00 USD | 0.00 USD | 23,730.00 USD | `-24.19%` | `6,809.20` |
| `Live` | `Long` | `3.50` | 16,570,000.00 USD | 0.00 USD | 21,380.00 USD | `-23.97%` | `6,116.20` |
| `Live` | `Long` | `3.50` | 16,550,000.00 USD | 0.00 USD | 24,460.00 USD | `-23.75%` | `6,979.30` |
| `Live` | `Long` | `3.52` | 16,530,000.00 USD | 0.00 USD | 15,060.00 USD | `-23.54%` | `4,285.50` |
| `Live` | `Long` | `3.52` | 16,510,000.00 USD | 0.00 USD | 2,700.00 USD | `-23.32%` | `765.80` |
| `Live` | `Long` | `3.54` | 16,510,000.00 USD | 0.00 USD | 536,780.00 USD | `-23.10%` | `151,846.00` |
| `Live` | `Long` | `3.54` | 15,970,000.00 USD | 0.00 USD | 335,270.00 USD | `-22.88%` | `94,575.00` |
| `Live` | `Long` | `3.56` | 15,640,000.00 USD | 0.00 USD | 367,390.00 USD | `-22.67%` | `103,345.40` |
| `Live` | `Long` | `3.56` | 15,270,000.00 USD | 0.00 USD | 3,340.00 USD | `-22.45%` | `936.80` |
| `Live` | `Long` | `3.58` | 15,270,000.00 USD | 0.00 USD | 113,320.00 USD | `-22.23%` | `31,698.00` |
| `Live` | `Long` | `3.58` | 15,150,000.00 USD | 0.00 USD | 296,360.00 USD | `-22.01%` | `82,667.50` |
| `Live` | `Long` | `3.60` | 14,860,000.00 USD | 0.00 USD | 28,190.00 USD | `-21.80%` | `7,841.00` |
| `Live` | `Long` | `3.60` | 14,830,000.00 USD | 0.00 USD | 94,590.00 USD | `-21.58%` | `26,237.30` |
| `Live` | `Long` | `3.62` | 14,730,000.00 USD | 0.00 USD | 13,600.00 USD | `-21.36%` | `3,762.20` |
| `Live` | `Long` | `3.62` | 14,720,000.00 USD | 0.00 USD | 13,580.00 USD | `-21.14%` | `3,746.80` |
| `Live` | `Long` | `3.63` | 14,710,000.00 USD | 0.00 USD | 25,260.00 USD | `-20.92%` | `6,949.40` |
| `Live` | `Long` | `3.65` | 14,680,000.00 USD | 0.00 USD | 523,780.00 USD | `-20.71%` | `143,697.10` |
| `Live` | `Long` | `3.65` | 14,160,000.00 USD | 0.00 USD | 31,510.00 USD | `-20.49%` | `8,622.00` |
| `Live` | `Long` | `3.67` | 14,130,000.00 USD | 0.00 USD | 44,710.00 USD | `-20.27%` | `12,199.40` |
| `Live` | `Long` | `3.67` | 14,080,000.00 USD | 0.00 USD | 189,790.00 USD | `-20.05%` | `51,642.30` |
| `Live` | `Long` | `3.69` | 13,890,000.00 USD | 0.00 USD | 216,110.00 USD | `-19.84%` | `58,645.00` |
| `Live` | `Long` | `3.69` | 13,680,000.00 USD | 0.00 USD | 3,030.00 USD | `-19.62%` | `819.40` |
| `Live` | `Long` | `3.71` | 13,670,000.00 USD | 0.00 USD | 140,650.00 USD | `-19.40%` | `37,963.20` |
| `Live` | `Long` | `3.71` | 13,530,000.00 USD | 0.00 USD | 58,950.00 USD | `-19.18%` | `15,868.20` |
| `Live` | `Long` | `3.73` | 13,470,000.00 USD | 0.00 USD | 24,930.00 USD | `-18.97%` | `6,691.90` |
| `Live` | `Long` | `3.73` | 13,450,000.00 USD | 0.00 USD | 135,410.00 USD | `-18.75%` | `36,253.40` |
| `Live` | `Long` | `3.75` | 13,310,000.00 USD | 0.00 USD | 24,460.00 USD | `-18.53%` | `6,531.10` |
| `Live` | `Long` | `3.75` | 13,290,000.00 USD | 0.00 USD | 91,600.00 USD | `-18.31%` | `24,394.50` |
| `Live` | `Long` | `3.77` | 13,200,000.00 USD | 0.00 USD | 56,130.00 USD | `-18.10%` | `14,909.60` |
| `Live` | `Long` | `3.77` | 13,140,000.00 USD | 0.00 USD | 19,920.00 USD | `-17.88%` | `5,275.70` |
| `Live` | `Long` | `3.79` | 13,120,000.00 USD | 0.00 USD | 37,770.00 USD | `-17.66%` | `9,979.90` |
| `Live` | `Long` | `3.79` | 13,080,000.00 USD | 0.00 USD | 143,780.00 USD | `-17.44%` | `37,887.90` |
| `Live` | `Long` | `3.81` | 12,940,000.00 USD | 0.00 USD | 14,720.00 USD | `-17.23%` | `3,868.60` |
| `Live` | `Long` | `3.81` | 12,920,000.00 USD | 0.00 USD | 82,000.00 USD | `-17.01%` | `21,495.10` |
| `Live` | `Long` | `3.83` | 12,840,000.00 USD | 0.00 USD | 5,180.00 USD | `-16.79%` | `1,354.50` |
| `Live` | `Long` | `3.83` | 12,840,000.00 USD | 0.00 USD | 162,000.00 USD | `-16.57%` | `42,242.20` |
| `Live` | `Long` | `3.85` | 12,670,000.00 USD | 0.00 USD | 23,860.00 USD | `-16.36%` | `6,206.40` |
| `Live` | `Long` | `3.85` | 12,650,000.00 USD | 0.00 USD | 13,750.00 USD | `-16.14%` | `3,567.80` |
| `Live` | `Long` | `3.87` | 12,640,000.00 USD | 0.00 USD | 23,070.00 USD | `-15.92%` | `5,969.30` |
| `Live` | `Long` | `3.88` | 12,610,000.00 USD | 0.00 USD | 4,660.00 USD | `-15.70%` | `1,203.10` |
| `Live` | `Long` | `3.88` | 12,610,000.00 USD | 0.00 USD | 37,160.00 USD | `-15.49%` | `9,565.70` |
| `Live` | `Long` | `3.90` | 12,570,000.00 USD | 0.00 USD | 103,080.00 USD | `-15.27%` | `26,464.90` |
| `Live` | `Long` | `3.90` | 12,470,000.00 USD | 0.00 USD | 8,840.00 USD | `-15.05%` | `2,264.40` |
| `Live` | `Long` | `3.92` | 12,460,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-14.83%` | `1,002,004.60` |
| `Live` | `Long` | `3.92` | 8,540,000.00 USD | 0.00 USD | 199,590.00 USD | `-14.62%` | `50,851.20` |
| `Live` | `Long` | `3.94` | 8,340,000.00 USD | 0.00 USD | 20,840.00 USD | `-14.40%` | `5,295.30` |
| `Live` | `Long` | `3.94` | 8,320,000.00 USD | 0.00 USD | 533,900.00 USD | `-14.18%` | `135,336.70` |
| `Live` | `Long` | `3.96` | 7,780,000.00 USD | 0.00 USD | 51,840.00 USD | `-13.96%` | `13,106.90` |
| `Live` | `Long` | `3.96` | 7,730,000.00 USD | 0.00 USD | 108,170.00 USD | `-13.75%` | `27,281.60` |
| `Live` | `Long` | `3.98` | 7,620,000.00 USD | 0.00 USD | 40,980.00 USD | `-13.53%` | `10,308.90` |
| `Live` | `Long` | `3.98` | 7,580,000.00 USD | 0.00 USD | 161,330.00 USD | `-13.31%` | `40,484.10` |
| `Live` | `Long` | `4.00` | 7,420,000.00 USD | 0.00 USD | 35,370.00 USD | `-13.09%` | `8,853.70` |
| `Live` | `Long` | `4.00` | 7,390,000.00 USD | 0.00 USD | 56,650.00 USD | `-12.88%` | `14,144.50` |
| `Live` | `Long` | `4.01` | 7,330,000.00 USD | 0.00 USD | 21,970.00 USD | `-12.66%` | `5,471.70` |
| `Live` | `Long` | `4.03` | 7,310,000.00 USD | 0.00 USD | 97,150.00 USD | `-12.44%` | `24,136.50` |
| `Live` | `Long` | `4.04` | 7,210,000.00 USD | 0.00 USD | 30,290.00 USD | `-12.22%` | `7,506.00` |
| `Live` | `Long` | `4.04` | 7,180,000.00 USD | 0.00 USD | 67,670.00 USD | `-12.01%` | `16,729.30` |
| `Live` | `Long` | `4.05` | 7,110,000.00 USD | 0.00 USD | 88,740.00 USD | `-11.79%` | `21,883.20` |
| `Live` | `Long` | `4.07` | 7,020,000.00 USD | 0.00 USD | 341,320.00 USD | `-11.57%` | `83,965.10` |
| `Live` | `Long` | `4.08` | 6,680,000.00 USD | 0.00 USD | 254,230.00 USD | `-11.35%` | `62,387.20` |
| `Live` | `Long` | `4.08` | 6,430,000.00 USD | 0.00 USD | 316,900.00 USD | `-11.14%` | `77,575.30` |
| `Live` | `Long` | `4.09` | 6,110,000.00 USD | 0.00 USD | 721,900.00 USD | `-10.92%` | `176,287.80` |
| `Live` | `Long` | `4.11` | 5,390,000.00 USD | 0.00 USD | 267,100.00 USD | `-10.70%` | `65,065.90` |
| `Live` | `Long` | `4.12` | 5,120,000.00 USD | 0.00 USD | 190,830.00 USD | `-10.48%` | `46,373.70` |
| `Live` | `Long` | `4.12` | 4,930,000.00 USD | 0.00 USD | 57,070.00 USD | `-10.27%` | `13,834.20` |
| `Live` | `Long` | `4.13` | 4,870,000.00 USD | 0.00 USD | 78,280.00 USD | `-10.05%` | `18,931.20` |
| `Live` | `Long` | `4.14` | 4,800,000.00 USD | 0.00 USD | 101,240.00 USD | `-9.83%` | `24,425.80` |
| `Live` | `Long` | `4.16` | 4,690,000.00 USD | 0.00 USD | 55,880.00 USD | `-9.61%` | `13,449.10` |
| `Live` | `Long` | `4.17` | 4,640,000.00 USD | 0.00 USD | 306,880.00 USD | `-9.40%` | `73,681.20` |
| `Live` | `Long` | `4.17` | 4,330,000.00 USD | 0.00 USD | 19,800.00 USD | `-9.18%` | `4,741.80` |
| `Live` | `Long` | `4.18` | 4,310,000.00 USD | 0.00 USD | 372,630.00 USD | `-8.96%` | `89,039.10` |
| `Live` | `Long` | `4.20` | 3,940,000.00 USD | 0.00 USD | 678,960.00 USD | `-8.74%` | `161,848.90` |
| `Live` | `Long` | `4.21` | 3,260,000.00 USD | 0.00 USD | 163,230.00 USD | `-8.53%` | `38,818.50` |
| `Live` | `Long` | `4.21` | 3,100,000.00 USD | 0.00 USD | 107,780.00 USD | `-8.31%` | `25,570.30` |
| `Live` | `Long` | `4.22` | 2,990,000.00 USD | 0.00 USD | 148,660.00 USD | `-8.09%` | `35,185.70` |
| `Live` | `Long` | `4.24` | 2,840,000.00 USD | 0.00 USD | 76,430.00 USD | `-7.87%` | `18,048.40` |
| `Live` | `Long` | `4.25` | 2,760,000.00 USD | 0.00 USD | 13,830.00 USD | `-7.66%` | `3,256.80` |
| `Live` | `Long` | `4.25` | 2,750,000.00 USD | 0.00 USD | 551,090.00 USD | `-7.44%` | `129,516.70` |
| `Live` | `Long` | `4.26` | 2,200,000.00 USD | 0.00 USD | 47,330.00 USD | `-7.22%` | `11,097.10` |
| `Live` | `Long` | `4.28` | 2,150,000.00 USD | 0.00 USD | 14,010.00 USD | `-7.00%` | `3,276.80` |
| `Live` | `Long` | `4.29` | 2,140,000.00 USD | 0.00 USD | 22,440.00 USD | `-6.79%` | `5,236.20` |
| `Live` | `Long` | `4.29` | 2,120,000.00 USD | 0.00 USD | 13,840.00 USD | `-6.57%` | `3,222.20` |
| `Live` | `Long` | `4.30` | 2,100,000.00 USD | 0.00 USD | 15,940.00 USD | `-6.35%` | `3,703.80` |
| `Live` | `Long` | `4.32` | 2,090,000.00 USD | 0.00 USD | 97,460.00 USD | `-6.13%` | `22,585.30` |
| `Live` | `Long` | `4.33` | 1,990,000.00 USD | 0.00 USD | 4,790.00 USD | `-5.91%` | `1,106.40` |
| `Live` | `Short` | `4.33` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | `-5.70%` | `864.70` |
| `Live` | `Long` | `4.34` | 1,980,000.00 USD | 0.00 USD | 30,420.00 USD | `-5.48%` | `7,000.00` |
| `Live` | `Long` | `4.36` | 1,950,000.00 USD | 0.00 USD | 1,090.00 USD | `-5.26%` | `251.00` |
| `Live` | `Long` | `4.37` | 1,950,000.00 USD | 0.00 USD | 67,460.00 USD | `-5.04%` | `15,455.00` |
| `Live` | `Long` | `4.38` | 1,880,000.00 USD | 0.00 USD | 81,030.00 USD | `-4.83%` | `18,521.80` |
| `Live` | `Long` | `4.38` | 1,800,000.00 USD | 0.00 USD | 662,490.00 USD | `-4.61%` | `151,081.80` |
| `Live` | `Long` | `4.39` | 1,140,000.00 USD | 0.00 USD | 36,850.00 USD | `-4.39%` | `8,384.70` |
| `Live` | `Long` | `4.41` | 1,100,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-4.17%` | `247,384.60` |
| `Live` | `Long` | `4.42` | 14,070.00 USD | 0.00 USD | 3,340.00 USD | `-3.96%` | `756.30` |
| `Live` | `Long` | `4.42` | 10,730.00 USD | 0.00 USD | 9,760.00 USD | `-3.74%` | `2,205.10` |
| `Live` | `Long` | `4.43` | 970.38 USD | 0.00 USD | 970.38 USD | `-3.52%` | `218.80` |
| `Live` | `Short` | `4.45` | 3,980.00 USD | 232.47 USD | 0.00 USD | `-3.30%` | `52.30` |
| `Live` | `Short` | `4.72` | 7,900.00 USD | 3,920.00 USD | 0.00 USD | `+2.79%` | `830.00` |
| `Live` | `Short` | `4.74` | 12,430.00 USD | 4,530.00 USD | 0.00 USD | `+3.00%` | `956.30` |
| `Live` | `Short` | `4.75` | 14,430.00 USD | 2,000.00 USD | 0.00 USD | `+3.22%` | `420.80` |
| `Live` | `Short` | `4.75` | 16,150.00 USD | 1,720.00 USD | 0.00 USD | `+3.44%` | `362.40` |
| `Live` | `Short` | `4.78` | 18,770.00 USD | 2,620.00 USD | 0.00 USD | `+3.87%` | `548.40` |
| `Live` | `Short` | `4.79` | 23,520.00 USD | 4,750.00 USD | 0.00 USD | `+4.09%` | `993.50` |
| `Live` | `Short` | `4.79` | 87,490.00 USD | 63,970.00 USD | 0.00 USD | `+4.31%` | `13,341.10` |
| `Live` | `Short` | `4.80` | 89,260.00 USD | 1,770.00 USD | 0.00 USD | `+4.53%` | `367.90` |
| `Live` | `Short` | `4.82` | 165,850.00 USD | 76,590.00 USD | 0.00 USD | `+4.74%` | `15,906.20` |
| `Live` | `Short` | `4.83` | 167,590.00 USD | 1,740.00 USD | 0.00 USD | `+4.96%` | `360.90` |
| `Live` | `Short` | `4.83` | 190,480.00 USD | 22,890.00 USD | 0.00 USD | `+5.18%` | `4,733.70` |
| `Live` | `Short` | `4.84` | 194,920.00 USD | 4,440.00 USD | 0.00 USD | `+5.40%` | `916.00` |
| `Live` | `Short` | `4.86` | 294,620.00 USD | 99,700.00 USD | 0.00 USD | `+5.61%` | `20,536.20` |
| `Live` | `Short` | `4.87` | 378,500.00 USD | 83,880.00 USD | 0.00 USD | `+5.83%` | `17,242.30` |
| `Live` | `Short` | `4.88` | 433,760.00 USD | 55,260.00 USD | 0.00 USD | `+6.05%` | `11,335.60` |
| `Live` | `Short` | `4.88` | 548,220.00 USD | 114,450.00 USD | 0.00 USD | `+6.27%` | `23,429.70` |
| `Live` | `Short` | `4.89` | 548,320.00 USD | 104.26 USD | 0.00 USD | `+6.48%` | `21.30` |
| `Live` | `Short` | `4.92` | 569,040.00 USD | 20,720.00 USD | 0.00 USD | `+6.92%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 581,970.00 USD | 12,930.00 USD | 0.00 USD | `+7.14%` | `2,625.70` |
| `Live` | `Short` | `4.93` | 582,130.00 USD | 157.43 USD | 0.00 USD | `+7.35%` | `31.90` |
| `Live` | `Short` | `4.95` | 584,300.00 USD | 2,180.00 USD | 0.00 USD | `+7.57%` | `440.00` |
| `Live` | `Short` | `4.96` | 588,480.00 USD | 4,170.00 USD | 0.00 USD | `+7.79%` | `842.00` |
| `Live` | `Short` | `4.96` | 596,460.00 USD | 7,990.00 USD | 0.00 USD | `+8.01%` | `1,608.30` |
| `Live` | `Short` | `4.97` | 850,490.00 USD | 254,030.00 USD | 0.00 USD | `+8.23%` | `51,061.00` |
| `Live` | `Short` | `4.99` | 852,200.00 USD | 1,710.00 USD | 0.00 USD | `+8.44%` | `343.70` |
| `Live` | `Short` | `5.00` | 852,470.00 USD | 267.27 USD | 0.00 USD | `+8.88%` | `53.40` |
| `Live` | `Short` | `5.01` | 882,900.00 USD | 30,430.00 USD | 0.00 USD | `+9.10%` | `6,067.50` |
| `Live` | `Short` | `5.03` | 893,940.00 USD | 11,040.00 USD | 0.00 USD | `+9.31%` | `2,198.00` |
| `Live` | `Short` | `5.04` | 895,110.00 USD | 1,160.00 USD | 0.00 USD | `+9.75%` | `230.50` |
| `Live` | `Short` | `5.05` | 900,130.00 USD | 5,020.00 USD | 0.00 USD | `+9.97%` | `993.80` |
| `Live` | `Short` | `5.07` | 903,550.00 USD | 3,420.00 USD | 0.00 USD | `+10.18%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,120,000.00 USD | 212,580.00 USD | 0.00 USD | `+10.40%` | `41,888.20` |
| `Live` | `Short` | `5.08` | 1,120,000.00 USD | 3,190.00 USD | 0.00 USD | `+10.62%` | `627.90` |
| `Live` | `Short` | `5.09` | 1,120,000.00 USD | 4,170.00 USD | 0.00 USD | `+10.84%` | `819.40` |
| `Live` | `Short` | `5.12` | 1,130,000.00 USD | 2,560.00 USD | 0.00 USD | `+11.49%` | `500.00` |
| `Live` | `Short` | `5.13` | 1,290,000.00 USD | 167,390.00 USD | 0.00 USD | `+11.71%` | `32,598.30` |
| `Live` | `Short` | `5.16` | 1,330,000.00 USD | 36,460.00 USD | 0.00 USD | `+12.14%` | `7,072.30` |
| `Live` | `Short` | `5.17` | 1,340,000.00 USD | 11,180.00 USD | 0.00 USD | `+12.36%` | `2,164.00` |
| `Live` | `Short` | `5.17` | 1,340,000.00 USD | 346.72 USD | 0.00 USD | `+12.58%` | `67.00` |
| `Live` | `Short` | `5.18` | 1,350,000.00 USD | 12,270.00 USD | 0.00 USD | `+12.79%` | `2,366.00` |
| `Live` | `Short` | `5.20` | 1,350,000.00 USD | 1,040.00 USD | 0.00 USD | `+13.01%` | `200.00` |
| `Live` | `Short` | `5.21` | 2,250,000.00 USD | 898,120.00 USD | 0.00 USD | `+13.23%` | `172,549.20` |
| `Live` | `Short` | `5.21` | 2,280,000.00 USD | 28,650.00 USD | 0.00 USD | `+13.45%` | `5,493.40` |
| `Live` | `Short` | `5.22` | 2,350,000.00 USD | 72,110.00 USD | 0.00 USD | `+13.66%` | `13,800.00` |
| `Live` | `Short` | `5.24` | 2,350,000.00 USD | 454.40 USD | 0.00 USD | `+13.88%` | `86.80` |
| `Live` | `Short` | `5.25` | 2,360,000.00 USD | 7,440.00 USD | 0.00 USD | `+14.10%` | `1,419.40` |
| `Live` | `Short` | `5.25` | 2,360,000.00 USD | 288.50 USD | 0.00 USD | `+14.32%` | `54.90` |
| `Live` | `Short` | `5.26` | 2,370,000.00 USD | 5,610.00 USD | 0.00 USD | `+14.53%` | `1,066.10` |
| `Live` | `Short` | `5.28` | 2,370,000.00 USD | 245.29 USD | 0.00 USD | `+14.75%` | `46.50` |
| `Live` | `Short` | `5.29` | 2,370,000.00 USD | 228.84 USD | 0.00 USD | `+14.97%` | `43.30` |
| `Live` | `Short` | `5.30` | 2,370,000.00 USD | 524.66 USD | 0.00 USD | `+15.40%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,370,000.00 USD | 878.04 USD | 0.00 USD | `+15.62%` | `165.20` |
| `Live` | `Short` | `5.33` | 2,370,000.00 USD | 1,630.00 USD | 0.00 USD | `+16.06%` | `305.00` |
| `Live` | `Short` | `5.34` | 2,410,000.00 USD | 39,950.00 USD | 0.00 USD | `+16.27%` | `7,474.80` |
| `Live` | `Short` | `5.36` | 2,450,000.00 USD | 35,920.00 USD | 0.00 USD | `+16.49%` | `6,707.60` |
| `Live` | `Short` | `5.37` | 2,490,000.00 USD | 40,130.00 USD | 0.00 USD | `+16.71%` | `7,479.70` |
| `Live` | `Short` | `5.38` | 2,490,000.00 USD | 431.61 USD | 0.00 USD | `+16.93%` | `80.30` |
| `Live` | `Short` | `5.38` | 2,530,000.00 USD | 42,070.00 USD | 0.00 USD | `+17.14%` | `7,811.90` |
| `Live` | `Short` | `5.42` | 2,530,000.00 USD | 179.03 USD | 0.00 USD | `+18.01%` | `33.00` |
| `Live` | `Short` | `5.43` | 2,530,000.00 USD | 962.54 USD | 0.00 USD | `+18.23%` | `177.10` |
| `Live` | `Short` | `5.45` | 2,530,000.00 USD | 2,180.00 USD | 0.00 USD | `+18.45%` | `400.00` |
| `Live` | `Short` | `5.46` | 2,540,000.00 USD | 2,270.00 USD | 0.00 USD | `+18.88%` | `415.20` |
| `Live` | `Short` | `5.49` | 2,590,000.00 USD | 52,520.00 USD | 0.00 USD | `+19.32%` | `9,574.70` |
| `Live` | `Short` | `5.50` | 2,680,000.00 USD | 88,450.00 USD | 0.00 USD | `+19.54%` | `16,097.30` |
| `Live` | `Short` | `5.50` | 2,690,000.00 USD | 9,490.00 USD | 0.00 USD | `+19.75%` | `1,723.30` |
| `Live` | `Short` | `5.51` | 2,720,000.00 USD | 38,800.00 USD | 0.00 USD | `+19.97%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 2,980,000.00 USD | 256,100.00 USD | 0.00 USD | `+20.41%` | `46,268.50` |
| `Live` | `Short` | `5.54` | 2,980,000.00 USD | 639.34 USD | 0.00 USD | `+20.62%` | `115.30` |
| `Live` | `Short` | `5.57` | 2,990,000.00 USD | 8,670.00 USD | 0.00 USD | `+21.06%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 3,050,000.00 USD | 62,420.00 USD | 0.00 USD | `+21.49%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 3,050,000.00 USD | 686.51 USD | 0.00 USD | `+21.71%` | `122.70` |
| `Live` | `Short` | `5.61` | 3,070,000.00 USD | 17,680.00 USD | 0.00 USD | `+21.93%` | `3,153.90` |
| `Live` | `Short` | `5.64` | 3,830,000.00 USD | 754,650.00 USD | 0.00 USD | `+22.80%` | `133,684.90` |
| `Live` | `Short` | `5.66` | 3,830,000.00 USD | 301.98 USD | 0.00 USD | `+23.02%` | `53.40` |
| `Live` | `Short` | `5.67` | 3,840,000.00 USD | 11,350.00 USD | 0.00 USD | `+23.24%` | `2,002.70` |
| `Live` | `Short` | `5.67` | 3,840,000.00 USD | 2,410.00 USD | 0.00 USD | `+23.45%` | `423.80` |
| `Live` | `Short` | `5.68` | 3,870,000.00 USD | 32,270.00 USD | 0.00 USD | `+23.67%` | `5,676.90` |
| `Live` | `Short` | `5.70` | 6,600,000.00 USD | 2,730,000.00 USD | 0.00 USD | `+23.89%` | `479,125.30` |
| `Live` | `Short` | `5.71` | 6,600,000.00 USD | 2,130.00 USD | 0.00 USD | `+24.32%` | `372.40` |
| `Live` | `Short` | `5.75` | 6,610,000.00 USD | 4,580.00 USD | 0.00 USD | `+24.98%` | `796.90` |
| `Live` | `Short` | `5.75` | 6,610,000.00 USD | 286.02 USD | 0.00 USD | `+25.19%` | `49.70` |
| `Live` | `Short` | `5.76` | 6,610,000.00 USD | 385.10 USD | 0.00 USD | `+25.41%` | `66.80` |
| `Live` | `Short` | `5.84` | 6,610,000.00 USD | 6,670.00 USD | 0.00 USD | `+27.15%` | `1,141.30` |
| `Live` | `Short` | `5.86` | 6,610,000.00 USD | 370.62 USD | 0.00 USD | `+27.37%` | `63.30` |
| `Live` | `Short` | `5.88` | 6,680,000.00 USD | 68,870.00 USD | 0.00 USD | `+28.02%` | `11,702.60` |
| `Live` | `Short` | `5.89` | 6,780,000.00 USD | 92,430.00 USD | 0.00 USD | `+28.24%` | `15,679.30` |
| `Live` | `Short` | `5.92` | 6,780,000.00 USD | 189.28 USD | 0.00 USD | `+28.67%` | `32.00` |
| `Live` | `Short` | `5.93` | 6,820,000.00 USD | 40,670.00 USD | 0.00 USD | `+29.11%` | `6,852.00` |
| `Live` | `Short` | `5.95` | 6,820,000.00 USD | 3,860.00 USD | 0.00 USD | `+29.33%` | `650.00` |
| `Live` | `Short` | `5.96` | 6,950,000.00 USD | 127,350.00 USD | 0.00 USD | `+29.54%` | `21,385.70` |
| `Live` | `Short` | `6.00` | 7,020,000.00 USD | 71,940.00 USD | 0.00 USD | `+30.41%` | `12,000.00` |
| `Live` | `Short` | `6.01` | 7,030,000.00 USD | 6,210.00 USD | 0.00 USD | `+30.85%` | `1,032.60` |
| `Live` | `Short` | `6.07` | 7,030,000.00 USD | 740.54 USD | 0.00 USD | `+31.94%` | `122.10` |
| `Live` | `Short` | `6.08` | 7,030,000.00 USD | 6,460.00 USD | 0.00 USD | `+32.37%` | `1,062.10` |
| `Live` | `Short` | `6.09` | 7,070,000.00 USD | 37,510.00 USD | 0.00 USD | `+32.59%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 7,160,000.00 USD | 94,120.00 USD | 0.00 USD | `+32.81%` | `15,417.20` |
| `Live` | `Short` | `6.13` | 7,170,000.00 USD | 2,430.00 USD | 0.00 USD | `+33.46%` | `396.10` |
| `Live` | `Short` | `6.14` | 7,170,000.00 USD | 487.30 USD | 0.00 USD | `+33.68%` | `79.30` |
| `Live` | `Short` | `6.18` | 7,210,000.00 USD | 45,700.00 USD | 0.00 USD | `+34.55%` | `7,388.60` |
| `Live` | `Short` | `6.25` | 7,220,000.00 USD | 7,610.00 USD | 0.00 USD | `+35.85%` | `1,218.90` |
| `Live` | `Short` | `6.25` | 7,220,000.00 USD | 439.10 USD | 0.00 USD | `+36.07%` | `70.20` |
| `Live` | `Short` | `6.32` | 7,220,000.00 USD | 310.70 USD | 0.00 USD | `+37.38%` | `49.20` |
| `Live` | `Short` | `6.33` | 7,220,000.00 USD | 382.00 USD | 0.00 USD | `+37.81%` | `60.30` |
| `Live` | `Short` | `6.34` | 7,220,000.00 USD | 1,550.00 USD | 0.00 USD | `+38.03%` | `244.90` |
| `Live` | `Short` | `6.37` | 7,220,000.00 USD | 113.93 USD | 0.00 USD | `+38.46%` | `17.90` |
| `Live` | `Short` | `6.38` | 7,220,000.00 USD | 288.15 USD | 0.00 USD | `+38.68%` | `45.20` |
| `Live` | `Short` | `6.38` | 7,230,000.00 USD | 2,000.00 USD | 0.00 USD | `+38.90%` | `312.80` |
| `Live` | `Short` | `6.41` | 7,230,000.00 USD | 3,780.00 USD | 0.00 USD | `+39.33%` | `590.10` |
| `Live` | `Short` | `6.42` | 7,230,000.00 USD | 943.65 USD | 0.00 USD | `+39.55%` | `147.10` |
| `Live` | `Short` | `6.42` | 7,230,000.00 USD | 346.95 USD | 0.00 USD | `+39.77%` | `54.00` |
| `Live` | `Short` | `6.43` | 7,820,000.00 USD | 584,470.00 USD | 0.00 USD | `+39.99%` | `90,827.50` |
| `Live` | `Short` | `6.45` | 7,820,000.00 USD | 5,270.00 USD | 0.00 USD | `+40.20%` | `818.40` |
| `Live` | `Short` | `6.46` | 7,830,000.00 USD | 7,150.00 USD | 0.00 USD | `+40.42%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 7,830,000.00 USD | 1,940.00 USD | 0.00 USD | `+40.64%` | `300.00` |
| `Live` | `Short` | `6.47` | 7,830,000.00 USD | 109.43 USD | 0.00 USD | `+40.86%` | `16.90` |
| `Live` | `Short` | `6.51` | 7,830,000.00 USD | 536.84 USD | 0.00 USD | `+41.73%` | `82.40` |
| `Live` | `Short` | `6.54` | 7,830,000.00 USD | 265.07 USD | 0.00 USD | `+42.38%` | `40.50` |
| `Live` | `Short` | `6.59` | 7,830,000.00 USD | 748.53 USD | 0.00 USD | `+43.47%` | `113.50` |
| `Live` | `Short` | `6.62` | 7,830,000.00 USD | 540.60 USD | 0.00 USD | `+44.12%` | `81.60` |
| `Live` | `Short` | `6.66` | 7,850,000.00 USD | 17,930.00 USD | 0.00 USD | `+44.77%` | `2,693.80` |
| `Live` | `Short` | `6.67` | 7,850,000.00 USD | 1,370.00 USD | 0.00 USD | `+44.99%` | `205.90` |
| `Live` | `Short` | `6.67` | 7,850,000.00 USD | 200.25 USD | 0.00 USD | `+45.21%` | `30.00` |
| `Live` | `Short` | `6.68` | 8,210,000.00 USD | 357,670.00 USD | 0.00 USD | `+45.42%` | `53,503.40` |
| `Live` | `Short` | `6.72` | 8,330,000.00 USD | 115,670.00 USD | 0.00 USD | `+46.29%` | `17,200.00` |
| `Live` | `Short` | `6.75` | 9,570,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+46.95%` | `184,501.00` |
| `Live` | `Short` | `6.82` | 9,610,000.00 USD | 40,950.00 USD | 0.00 USD | `+48.25%` | `6,008.30` |
| `Live` | `Short` | `6.83` | 9,610,000.00 USD | 2,200.00 USD | 0.00 USD | `+48.47%` | `322.50` |
| `Live` | `Short` | `6.87` | 9,620,000.00 USD | 3,410.00 USD | 0.00 USD | `+49.34%` | `496.20` |
| `Live` | `Short` | `6.92` | 9,620,000.00 USD | 6,920.00 USD | 0.00 USD | `+50.64%` | `1,000.00` |
| `Live` | `Short` | `6.93` | 9,690,000.00 USD | 61,000.00 USD | 0.00 USD | `+50.86%` | `8,796.10` |
| `Live` | `Short` | `6.95` | 9,700,000.00 USD | 17,480.00 USD | 0.00 USD | `+51.08%` | `2,517.30` |
| `Live` | `Short` | `6.99` | 9,700,000.00 USD | 664.27 USD | 0.00 USD | `+51.95%` | `95.10` |
| `Live` | `Short` | `7.03` | 9,710,000.00 USD | 9,030.00 USD | 0.00 USD | `+52.82%` | `1,285.90` |
| `Live` | `Short` | `7.08` | 9,710,000.00 USD | 1,370.00 USD | 0.00 USD | `+54.13%` | `193.30` |
| `Live` | `Short` | `7.12` | 19,650,000.00 USD | 9,930,000.00 USD | 0.00 USD | `+55.00%` | `1,393,938.40` |
| `Live` | `Short` | `7.18` | 19,650,000.00 USD | 2,920.00 USD | 0.00 USD | `+56.30%` | `406.50` |
| `Live` | `Short` | `7.21` | 19,690,000.00 USD | 38,360.00 USD | 0.00 USD | `+56.74%` | `5,323.40` |
| `Live` | `Short` | `7.21` | 19,700,000.00 USD | 13,560.00 USD | 0.00 USD | `+56.95%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 19,710,000.00 USD | 4,910.00 USD | 0.00 USD | `+57.39%` | `679.30` |
| `Live` | `Short` | `7.29` | 19,710,000.00 USD | 152.47 USD | 0.00 USD | `+58.69%` | `20.90` |
| `Live` | `Short` | `7.33` | 19,710,000.00 USD | 1,320.00 USD | 0.00 USD | `+59.56%` | `180.00` |
| `Live` | `Short` | `7.39` | 19,710,000.00 USD | 474.76 USD | 0.00 USD | `+60.87%` | `64.20` |
| `Live` | `Short` | `7.42` | 27,560,000.00 USD | 7,850,000.00 USD | 0.00 USD | `+61.52%` | `1,057,278.40` |
| `Live` | `Short` | `7.46` | 27,560,000.00 USD | 1,420.00 USD | 0.00 USD | `+62.17%` | `191.10` |
| `Live` | `Short` | `7.47` | 27,670,000.00 USD | 106,720.00 USD | 0.00 USD | `+62.61%` | `14,276.50` |
| `Live` | `Short` | `7.50` | 27,670,000.00 USD | 6,880.00 USD | 0.00 USD | `+63.26%` | `917.00` |
| `Live` | `Short` | `7.53` | 27,670,000.00 USD | 1,610.00 USD | 0.00 USD | `+63.70%` | `214.00` |
| `Live` | `Short` | `7.63` | 27,690,000.00 USD | 19,210.00 USD | 0.00 USD | `+66.09%` | `2,516.10` |
| `Live` | `Short` | `7.64` | 27,700,000.00 USD | 1,140.00 USD | 0.00 USD | `+66.31%` | `148.80` |
| `Live` | `Short` | `7.67` | 27,700,000.00 USD | 360.25 USD | 0.00 USD | `+66.74%` | `47.00` |
| `Live` | `Short` | `7.75` | 27,700,000.00 USD | 629.67 USD | 0.00 USD | `+68.48%` | `81.30` |
| `Live` | `Short` | `7.75` | 27,700,000.00 USD | 2,690.00 USD | 0.00 USD | `+68.70%` | `347.20` |
| `Live` | `Short` | `7.76` | 27,710,000.00 USD | 15,530.00 USD | 0.00 USD | `+68.92%` | `2,000.00` |
| `Live` | `Short` | `7.78` | 27,750,000.00 USD | 33,500.00 USD | 0.00 USD | `+69.14%` | `4,308.50` |
| `Live` | `Short` | `7.87` | 27,750,000.00 USD | 2,980.00 USD | 0.00 USD | `+71.09%` | `378.70` |
| `Live` | `Short` | `7.91` | 29,000,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+71.96%` | `157,519.30` |
| `Live` | `Short` | `7.92` | 29,710,000.00 USD | 712,350.00 USD | 0.00 USD | `+72.18%` | `90,000.00` |
| `Live` | `Short` | `7.95` | 29,740,000.00 USD | 32,750.00 USD | 0.00 USD | `+72.83%` | `4,122.10` |
| `Live` | `Short` | `7.96` | 29,880,000.00 USD | 134,240.00 USD | 0.00 USD | `+73.27%` | `16,854.30` |
| `Live` | `Short` | `7.99` | 29,880,000.00 USD | 354.53 USD | 0.00 USD | `+73.70%` | `44.40` |
| `Live` | `Short` | `8.03` | 30,340,000.00 USD | 463,480.00 USD | 0.00 USD | `+74.57%` | `57,753.90` |
| `Live` | `Short` | `8.04` | 30,740,000.00 USD | 404,530.00 USD | 0.00 USD | `+74.79%` | `50,346.40` |
| `Live` | `Short` | `8.06` | 30,750,000.00 USD | 2,130.00 USD | 0.00 USD | `+75.44%` | `264.70` |
| `Live` | `Short` | `8.22` | 30,750,000.00 USD | 103.64 USD | 0.00 USD | `+78.92%` | `12.60` |
| `Live` | `Short` | `8.24` | 31,370,000.00 USD | 625,070.00 USD | 0.00 USD | `+79.36%` | `75,812.40` |
| `Live` | `Short` | `8.29` | 31,370,000.00 USD | 3,760.00 USD | 0.00 USD | `+80.23%` | `454.00` |
| `Live` | `Short` | `8.36` | 31,380,000.00 USD | 8,460.00 USD | 0.00 USD | `+81.75%` | `1,012.60` |
| `Live` | `Short` | `8.37` | 32,480,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+81.97%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 32,480,000.00 USD | 577.04 USD | 0.00 USD | `+82.19%` | `68.90` |
| `Live` | `Short` | `8.39` | 32,510,000.00 USD | 25,180.00 USD | 0.00 USD | `+82.62%` | `3,000.00` |
| `Live` | `Short` | `8.46` | 32,510,000.00 USD | 2,350.00 USD | 0.00 USD | `+84.15%` | `277.70` |
| `Live` | `Short` | `8.48` | 32,530,000.00 USD | 18,200.00 USD | 0.00 USD | `+84.58%` | `2,144.60` |
| `Live` | `Short` | `8.49` | 32,530,000.00 USD | 594.65 USD | 0.00 USD | `+84.80%` | `70.00` |
| `Live` | `Short` | `8.53` | 32,530,000.00 USD | 578.85 USD | 0.00 USD | `+85.45%` | `67.90` |
| `Live` | `Short` | `8.54` | 32,970,000.00 USD | 440,790.00 USD | 0.00 USD | `+85.67%` | `51,644.90` |
| `Live` | `Short` | `8.54` | 32,970,000.00 USD | 2,760.00 USD | 0.00 USD | `+85.89%` | `323.50` |
| `Live` | `Short` | `8.57` | 32,980,000.00 USD | 583.96 USD | 0.00 USD | `+86.54%` | `68.10` |
| `Live` | `Short` | `8.62` | 34,890,000.00 USD | 1,910,000.00 USD | 0.00 USD | `+87.63%` | `221,939.70` |
| `Live` | `Short` | `8.64` | 36,770,000.00 USD | 1,880,000.00 USD | 0.00 USD | `+88.06%` | `217,796.20` |
| `Live` | `Short` | `8.68` | 36,770,000.00 USD | 2,320.00 USD | 0.00 USD | `+88.71%` | `267.10` |
| `Live` | `Short` | `8.70` | 36,790,000.00 USD | 16,520.00 USD | 0.00 USD | `+89.15%` | `1,900.00` |
| `Live` | `Short` | `8.71` | 36,820,000.00 USD | 31,930.00 USD | 0.00 USD | `+89.58%` | `3,664.20` |
| `Live` | `Short` | `8.77` | 36,830,000.00 USD | 2,630.00 USD | 0.00 USD | `+90.67%` | `300.00` |
| `Live` | `Short` | `8.78` | 36,830,000.00 USD | 4,390.00 USD | 0.00 USD | `+90.89%` | `500.00` |
| `Live` | `Short` | `8.81` | 36,830,000.00 USD | 1,280.00 USD | 0.00 USD | `+91.76%` | `145.00` |
| `Live` | `Short` | `8.84` | 36,850,000.00 USD | 19,980.00 USD | 0.00 USD | `+92.19%` | `2,261.80` |
| `Live` | `Short` | `8.85` | 36,860,000.00 USD | 6,380.00 USD | 0.00 USD | `+92.41%` | `721.60` |
| `Live` | `Short` | `8.87` | 38,350,000.00 USD | 1,500,000.00 USD | 0.00 USD | `+92.85%` | `168,686.00` |
| `Live` | `Short` | `8.88` | 40,160,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+93.28%` | `203,058.40` |
| `Live` | `Short` | `8.91` | 40,160,000.00 USD | 867.43 USD | 0.00 USD | `+93.94%` | `97.30` |
| `Live` | `Short` | `8.95` | 40,160,000.00 USD | 223.62 USD | 0.00 USD | `+94.59%` | `25.00` |
| `Live` | `Short` | `8.96` | 40,180,000.00 USD | 17,370.00 USD | 0.00 USD | `+94.81%` | `1,940.10` |
| `Live` | `Short` | `8.96` | 40,200,000.00 USD | 19,880.00 USD | 0.00 USD | `+95.02%` | `2,217.40` |
| `Live` | `Short` | `8.99` | 45,920,000.00 USD | 5,720,000.00 USD | 0.00 USD | `+95.68%` | `636,076.70` |
| `Live` | `Short` | `9.01` | 45,980,000.00 USD | 60,030.00 USD | 0.00 USD | `+95.89%` | `6,665.80` |
| `Live` | `Short` | `9.05` | 45,980,000.00 USD | 814.95 USD | 0.00 USD | `+96.98%` | `90.00` |
| `Live` | `Short` | `9.14` | 45,990,000.00 USD | 11,460.00 USD | 0.00 USD | `+98.94%` | `1,252.60` |
| `Live` | `Short` | `9.16` | 46,480,000.00 USD | 486,070.00 USD | 0.00 USD | `+99.37%` | `53,035.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 4,820,000.00 USD | 0.00 USD | 585.51 USD | `-78.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 4,820,000.00 USD | 0.00 USD | 345.25 USD | `-70.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 4,820,000.00 USD | 0.00 USD | 5,640.00 USD | `-70.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 4,820,000.00 USD | 0.00 USD | 997.29 USD | `-69.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 4,810,000.00 USD | 0.00 USD | 139.83 USD | `-67.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 4,810,000.00 USD | 0.00 USD | 113.28 USD | `-66.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 4,810,000.00 USD | 0.00 USD | 4,000.00 USD | `-66.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 4,810,000.00 USD | 0.00 USD | 324.22 USD | `-66.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 4,810,000.00 USD | 0.00 USD | 4,590.00 USD | `-65.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 4,810,000.00 USD | 0.00 USD | 739.67 USD | `-64.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 4,800,000.00 USD | 0.00 USD | 1,740.00 USD | `-64.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 4,800,000.00 USD | 0.00 USD | 669.02 USD | `-63.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 4,800,000.00 USD | 0.00 USD | 105.88 USD | `-62.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 4,800,000.00 USD | 0.00 USD | 172.50 USD | `-62.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 4,800,000.00 USD | 0.00 USD | 10,650.00 USD | `-61.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 4,790,000.00 USD | 0.00 USD | 722.00 USD | `-60.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 4,790,000.00 USD | 0.00 USD | 259.00 USD | `-60.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 4,790,000.00 USD | 0.00 USD | 103.84 USD | `-60.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 4,790,000.00 USD | 0.00 USD | 109.00 USD | `-60.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 4,790,000.00 USD | 0.00 USD | 222.19 USD | `-59.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 4,790,000.00 USD | 0.00 USD | 10,280.00 USD | `-58.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 4,780,000.00 USD | 0.00 USD | 558.36 USD | `-58.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 4,780,000.00 USD | 0.00 USD | 1,520.00 USD | `-58.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 4,780,000.00 USD | 0.00 USD | 222.14 USD | `-57.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 4,780,000.00 USD | 0.00 USD | 279.50 USD | `-57.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 4,780,000.00 USD | 0.00 USD | 197.50 USD | `-57.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,780,000.00 USD | 0.00 USD | 935.66 USD | `-56.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,780,000.00 USD | 0.00 USD | 18,860.00 USD | `-56.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 4,760,000.00 USD | 0.00 USD | 3,020.00 USD | `-56.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 4,750,000.00 USD | 0.00 USD | 214.52 USD | `-55.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,750,000.00 USD | 0.00 USD | 1,200.00 USD | `-55.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,750,000.00 USD | 0.00 USD | 578.41 USD | `-55.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,750,000.00 USD | 0.00 USD | 18,070.00 USD | `-54.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,730,000.00 USD | 0.00 USD | 13,980.00 USD | `-54.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,720,000.00 USD | 0.00 USD | 107.23 USD | `-53.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,720,000.00 USD | 0.00 USD | 1,590.00 USD | `-53.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,720,000.00 USD | 0.00 USD | 6,970.00 USD | `-53.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,710,000.00 USD | 0.00 USD | 310.32 USD | `-53.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 4,710,000.00 USD | 0.00 USD | 1,170.00 USD | `-52.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,710,000.00 USD | 0.00 USD | 576.18 USD | `-52.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,710,000.00 USD | 0.00 USD | 295.67 USD | `-52.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,710,000.00 USD | 0.00 USD | 2,940.00 USD | `-52.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,710,000.00 USD | 0.00 USD | 812.68 USD | `-51.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,710,000.00 USD | 0.00 USD | 1,440.00 USD | `-51.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,700,000.00 USD | 0.00 USD | 490.14 USD | `-51.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,700,000.00 USD | 0.00 USD | 13,490.00 USD | `-51.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,690,000.00 USD | 0.00 USD | 478.06 USD | `-50.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,690,000.00 USD | 0.00 USD | 540.88 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,690,000.00 USD | 0.00 USD | 1,210.00 USD | `-50.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,690,000.00 USD | 0.00 USD | 759.76 USD | `-50.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,690,000.00 USD | 0.00 USD | 15,550.00 USD | `-50.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 4,670,000.00 USD | 0.00 USD | 3,690.00 USD | `-49.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,670,000.00 USD | 0.00 USD | 3,050.00 USD | `-49.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,660,000.00 USD | 0.00 USD | 467.00 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 4,660,000.00 USD | 0.00 USD | 506.75 USD | `-48.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 4,660,000.00 USD | 0.00 USD | 214.27 USD | `-48.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,660,000.00 USD | 0.00 USD | 428.69 USD | `-48.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,660,000.00 USD | 0.00 USD | 322.45 USD | `-48.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,660,000.00 USD | 0.00 USD | 108.25 USD | `-47.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,660,000.00 USD | 0.00 USD | 3,850.00 USD | `-47.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 4,660,000.00 USD | 0.00 USD | 799.04 USD | `-47.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,660,000.00 USD | 0.00 USD | 6,830.00 USD | `-47.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,650,000.00 USD | 0.00 USD | 137.16 USD | `-46.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,650,000.00 USD | 0.00 USD | 504.41 USD | `-46.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,650,000.00 USD | 0.00 USD | 963.93 USD | `-45.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 4,650,000.00 USD | 0.00 USD | 13,880.00 USD | `-45.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 4,640,000.00 USD | 0.00 USD | 541.98 USD | `-45.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,640,000.00 USD | 0.00 USD | 108.75 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,640,000.00 USD | 0.00 USD | 766.55 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 4,630,000.00 USD | 0.00 USD | 1,010.00 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,630,000.00 USD | 0.00 USD | 1,100.00 USD | `-43.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,630,000.00 USD | 0.00 USD | 100.04 USD | `-43.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 4,630,000.00 USD | 0.00 USD | 5,090.00 USD | `-43.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 4,630,000.00 USD | 0.00 USD | 226.57 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,630,000.00 USD | 0.00 USD | 104.98 USD | `-41.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,630,000.00 USD | 0.00 USD | 329.33 USD | `-41.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 4,630,000.00 USD | 0.00 USD | 7,160.00 USD | `-41.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 4,620,000.00 USD | 0.00 USD | 107.21 USD | `-40.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,620,000.00 USD | 0.00 USD | 197.37 USD | `-40.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,620,000.00 USD | 0.00 USD | 8,390.00 USD | `-40.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,610,000.00 USD | 0.00 USD | 108.39 USD | `-39.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,610,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,610,000.00 USD | 0.00 USD | 14,140.00 USD | `-39.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,590,000.00 USD | 0.00 USD | 437.98 USD | `-39.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 4,590,000.00 USD | 0.00 USD | 2,000.00 USD | `-38.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 4,590,000.00 USD | 0.00 USD | 8,250.00 USD | `-38.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 4,580,000.00 USD | 0.00 USD | 109.53 USD | `-38.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 4,580,000.00 USD | 0.00 USD | 1,810.00 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,580,000.00 USD | 0.00 USD | 437.00 USD | `-37.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,580,000.00 USD | 0.00 USD | 746.06 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 4,580,000.00 USD | 0.00 USD | 4,870.00 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,580,000.00 USD | 0.00 USD | 696.98 USD | `-36.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,580,000.00 USD | 0.00 USD | 358.90 USD | `-36.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 4,580,000.00 USD | 0.00 USD | 15,370.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 4,560,000.00 USD | 0.00 USD | 523.32 USD | `-35.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 4,560,000.00 USD | 0.00 USD | 2,330.00 USD | `-35.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 4,560,000.00 USD | 0.00 USD | 16,080.00 USD | `-34.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,540,000.00 USD | 0.00 USD | 1,020.00 USD | `-34.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,540,000.00 USD | 0.00 USD | 345.76 USD | `-34.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 4,540,000.00 USD | 0.00 USD | 214.57 USD | `-33.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 4,540,000.00 USD | 0.00 USD | 109.42 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 4,540,000.00 USD | 0.00 USD | 721.58 USD | `-32.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 4,540,000.00 USD | 0.00 USD | 9,300.00 USD | `-32.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 4,530,000.00 USD | 0.00 USD | 104.69 USD | `-32.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 4,530,000.00 USD | 0.00 USD | 315.69 USD | `-31.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,530,000.00 USD | 0.00 USD | 214.17 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,530,000.00 USD | 0.00 USD | 641.10 USD | `-31.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,530,000.00 USD | 0.00 USD | 212.06 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,530,000.00 USD | 0.00 USD | 1,030.00 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 4,530,000.00 USD | 0.00 USD | 218.81 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,530,000.00 USD | 0.00 USD | 31,570.00 USD | `-30.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,490,000.00 USD | 0.00 USD | 144.67 USD | `-30.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 4,490,000.00 USD | 0.00 USD | 21,850.00 USD | `-29.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 4,470,000.00 USD | 0.00 USD | 1,880.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 4,470,000.00 USD | 0.00 USD | 104.81 USD | `-28.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,470,000.00 USD | 0.00 USD | 1,150.00 USD | `-28.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,470,000.00 USD | 0.00 USD | 1,070.00 USD | `-28.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,470,000.00 USD | 0.00 USD | 15,820.00 USD | `-28.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,450,000.00 USD | 0.00 USD | 240.67 USD | `-27.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,450,000.00 USD | 0.00 USD | 306.56 USD | `-27.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,450,000.00 USD | 0.00 USD | 1,670.00 USD | `-27.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 4,450,000.00 USD | 0.00 USD | 505.76 USD | `-27.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 4,450,000.00 USD | 0.00 USD | 73,220.00 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 4,380,000.00 USD | 0.00 USD | 129,640.00 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,250,000.00 USD | 0.00 USD | 8,490.00 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,240,000.00 USD | 0.00 USD | 3,320.00 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 4,240,000.00 USD | 0.00 USD | 25,250.00 USD | `-25.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 4,210,000.00 USD | 0.00 USD | 506.22 USD | `-25.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 4,210,000.00 USD | 0.00 USD | 103.05 USD | `-25.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 4,210,000.00 USD | 0.00 USD | 2,550.00 USD | `-25.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 4,210,000.00 USD | 0.00 USD | 1,380.00 USD | `-24.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 4,210,000.00 USD | 0.00 USD | 344.07 USD | `-24.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 4,210,000.00 USD | 0.00 USD | 117,360.00 USD | `-23.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 4,090,000.00 USD | 0.00 USD | 17,360.00 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 4,070,000.00 USD | 0.00 USD | 2,030.00 USD | `-23.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 4,070,000.00 USD | 0.00 USD | 12,040.00 USD | `-22.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 4,060,000.00 USD | 0.00 USD | 633.50 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 4,060,000.00 USD | 0.00 USD | 333.68 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 4,060,000.00 USD | 0.00 USD | 72,860.00 USD | `-22.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,980,000.00 USD | 0.00 USD | 179.25 USD | `-22.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,980,000.00 USD | 0.00 USD | 643.50 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,980,000.00 USD | 0.00 USD | 3,540.00 USD | `-21.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,980,000.00 USD | 0.00 USD | 632.99 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,980,000.00 USD | 0.00 USD | 172.19 USD | `-21.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 3,980,000.00 USD | 0.00 USD | 13,400.00 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,960,000.00 USD | 0.00 USD | 1,260.00 USD | `-20.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,960,000.00 USD | 0.00 USD | 3,900.00 USD | `-20.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,960,000.00 USD | 0.00 USD | 174.09 USD | `-20.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,960,000.00 USD | 0.00 USD | 367.50 USD | `-20.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,960,000.00 USD | 0.00 USD | 9,210.00 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,950,000.00 USD | 0.00 USD | 4,370.00 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,940,000.00 USD | 0.00 USD | 17,930.00 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,930,000.00 USD | 0.00 USD | 1,440.00 USD | `-19.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,930,000.00 USD | 0.00 USD | 1,030.00 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,920,000.00 USD | 0.00 USD | 48,440.00 USD | `-18.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 3,880,000.00 USD | 0.00 USD | 18,440.00 USD | `-18.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,860,000.00 USD | 0.00 USD | 6,850.00 USD | `-18.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,850,000.00 USD | 0.00 USD | 5,550.00 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,850,000.00 USD | 0.00 USD | 189,250.00 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,660,000.00 USD | 0.00 USD | 1,900.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,650,000.00 USD | 0.00 USD | 1,420.00 USD | `-17.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,650,000.00 USD | 0.00 USD | 18,070.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,630,000.00 USD | 0.00 USD | 23,060.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,610,000.00 USD | 0.00 USD | 2,240.00 USD | `-16.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,610,000.00 USD | 0.00 USD | 301.45 USD | `-16.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,610,000.00 USD | 0.00 USD | 3,070.00 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 3,610,000.00 USD | 0.00 USD | 2,460.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,600,000.00 USD | 0.00 USD | 5,550.00 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,600,000.00 USD | 0.00 USD | 4,990.00 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,590,000.00 USD | 0.00 USD | 1,310.00 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,590,000.00 USD | 0.00 USD | 38,930.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,550,000.00 USD | 0.00 USD | 2,070.00 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,550,000.00 USD | 0.00 USD | 1,120.00 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,550,000.00 USD | 0.00 USD | 1,420.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,550,000.00 USD | 0.00 USD | 187.78 USD | `-14.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,550,000.00 USD | 0.00 USD | 13,970.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,530,000.00 USD | 0.00 USD | 301,690.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 3,230,000.00 USD | 0.00 USD | 4,980.00 USD | `-13.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 3,230,000.00 USD | 0.00 USD | 3,950.00 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 3,220,000.00 USD | 0.00 USD | 513.36 USD | `-13.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 3,220,000.00 USD | 0.00 USD | 249,600.00 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 2,970,000.00 USD | 0.00 USD | 5,440.00 USD | `-12.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 2,970,000.00 USD | 0.00 USD | 4,510.00 USD | `-12.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,960,000.00 USD | 0.00 USD | 3,210.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,960,000.00 USD | 0.00 USD | 6,050.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 2,950,000.00 USD | 0.00 USD | 2,530.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 2,950,000.00 USD | 0.00 USD | 860.56 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,950,000.00 USD | 0.00 USD | 504,780.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,450,000.00 USD | 0.00 USD | 74,690.00 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 2,370,000.00 USD | 0.00 USD | 1,250.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 2,370,000.00 USD | 0.00 USD | 29,060.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 2,340,000.00 USD | 0.00 USD | 3,430.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 2,340,000.00 USD | 0.00 USD | 10,440.00 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 2,330,000.00 USD | 0.00 USD | 352,210.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 1,970,000.00 USD | 0.00 USD | 1,910.00 USD | `-9.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,970,000.00 USD | 0.00 USD | 38,450.00 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,930,000.00 USD | 0.00 USD | 4,080.00 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,930,000.00 USD | 0.00 USD | 30,410.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 1,900,000.00 USD | 0.00 USD | 44,430.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 1,860,000.00 USD | 0.00 USD | 34,460.00 USD | `-8.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,820,000.00 USD | 0.00 USD | 139,740.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,680,000.00 USD | 0.00 USD | 7,270.00 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 1,670,000.00 USD | 0.00 USD | 92,660.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 1,580,000.00 USD | 0.00 USD | 30,510.00 USD | `-7.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 1,550,000.00 USD | 0.00 USD | 45,410.00 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 1,510,000.00 USD | 0.00 USD | 34,140.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 1,470,000.00 USD | 0.00 USD | 7,980.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 1,460,000.00 USD | 0.00 USD | 276,540.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 1,190,000.00 USD | 0.00 USD | 11,740.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 1,170,000.00 USD | 0.00 USD | 59,510.00 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 1,120,000.00 USD | 0.00 USD | 3,290.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 1,110,000.00 USD | 0.00 USD | 53,330.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 1,060,000.00 USD | 0.00 USD | 61,100.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 997,660.00 USD | 0.00 USD | 11,230.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 986,430.00 USD | 0.00 USD | 107,700.00 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 878,730.00 USD | 0.00 USD | 29,330.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 849,390.00 USD | 0.00 USD | 62,500.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 786,890.00 USD | 0.00 USD | 6,260.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 780,630.00 USD | 0.00 USD | 24,740.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.39` | 755,890.00 USD | 0.00 USD | 34,820.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.41` | 721,070.00 USD | 0.00 USD | 87,730.00 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 633,340.00 USD | 0.00 USD | 79,630.00 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 553,710.00 USD | 0.00 USD | 157,600.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.43` | 396,110.00 USD | 0.00 USD | 45,940.00 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.45` | 350,180.00 USD | 0.00 USD | 3,050.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.46` | 347,120.00 USD | 0.00 USD | 5,260.00 USD | `-3.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.46` | 341,860.00 USD | 0.00 USD | 9,320.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.47` | 332,540.00 USD | 0.00 USD | 3,720.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.49` | 328,820.00 USD | 0.00 USD | 5,240.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.50` | 323,590.00 USD | 0.00 USD | 624.81 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.50` | 322,960.00 USD | 0.00 USD | 263,790.00 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.51` | 59,170.00 USD | 0.00 USD | 6,430.00 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.53` | 52,750.00 USD | 0.00 USD | 9,480.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.54` | 43,270.00 USD | 0.00 USD | 616.76 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.54` | 42,650.00 USD | 0.00 USD | 15,640.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 27,010.00 USD | 0.00 USD | 2,280.00 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.57` | 24,730.00 USD | 0.00 USD | 881.96 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.58` | 23,840.00 USD | 0.00 USD | 10,990.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.58` | 12,850.00 USD | 0.00 USD | 8,520.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.59` | 4,330.00 USD | 0.00 USD | 4,330.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 10,070.00 USD | 7,100.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 10,710.00 USD | 641.49 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 13,060.00 USD | 2,350.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 14,510.00 USD | 1,450.00 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 129,730.00 USD | 115,210.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 132,550.00 USD | 2,830.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 275,000.00 USD | 142,450.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 288,080.00 USD | 13,080.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 306,300.00 USD | 18,220.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 782,420.00 USD | 476,110.00 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 891,430.00 USD | 109,010.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 896,570.00 USD | 5,140.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,040,000.00 USD | 139,370.00 USD | 0.00 USD | `+3.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,080,000.00 USD | 43,320.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,110,000.00 USD | 30,510.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,160,000.00 USD | 45,280.00 USD | 0.00 USD | `+3.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,170,000.00 USD | 10,630.00 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 1,170,000.00 USD | 1,720.00 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 1,190,000.00 USD | 19,200.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 1,220,000.00 USD | 34,290.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,010,000.00 USD | 793,320.00 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,030,000.00 USD | 13,450.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,030,000.00 USD | 1,790.00 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 2,050,000.00 USD | 17,440.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 2,110,000.00 USD | 66,670.00 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 2,150,000.00 USD | 35,940.00 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,160,000.00 USD | 10,850.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,340,000.00 USD | 178,970.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 2,340,000.00 USD | 4,060.00 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 2,460,000.00 USD | 111,870.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,460,000.00 USD | 639.44 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,470,000.00 USD | 11,020.00 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 2,480,000.00 USD | 9,400.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 2,480,000.00 USD | 114.72 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 2,480,000.00 USD | 3,180.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 2,530,000.00 USD | 47,350.00 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 2,530,000.00 USD | 562.17 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 2,620,000.00 USD | 94,170.00 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 2,640,000.00 USD | 18,960.00 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 2,780,000.00 USD | 141,610.00 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 2,810,000.00 USD | 26,480.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 2,810,000.00 USD | 5,140.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 2,900,000.00 USD | 90,010.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 2,900,000.00 USD | 219.46 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 2,950,000.00 USD | 50,820.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 2,960,000.00 USD | 3,550.00 USD | 0.00 USD | `+10.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,050,000.00 USD | 90,150.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,930,000.00 USD | 882,870.00 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,930,000.00 USD | 547.20 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,980,000.00 USD | 49,770.00 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,000,000.00 USD | 15,350.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,000,000.00 USD | 113.26 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,010,000.00 USD | 8,600.00 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,010,000.00 USD | 3,670.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,010,000.00 USD | 3,770.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,010,000.00 USD | 1,200.00 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,010,000.00 USD | 327.58 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,020,000.00 USD | 270.66 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,020,000.00 USD | 5,960.00 USD | 0.00 USD | `+13.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,060,000.00 USD | 41,900.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,060,000.00 USD | 1,710.00 USD | 0.00 USD | `+13.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,190,000.00 USD | 120,710.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,200,000.00 USD | 9,820.00 USD | 0.00 USD | `+13.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,200,000.00 USD | 537.61 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,670,000.00 USD | 477,520.00 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,680,000.00 USD | 5,540.00 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,680,000.00 USD | 589.22 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,680,000.00 USD | 733.03 USD | 0.00 USD | `+14.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,680,000.00 USD | 693.64 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,730,000.00 USD | 52,560.00 USD | 0.00 USD | `+15.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,740,000.00 USD | 3,090.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,740,000.00 USD | 961.16 USD | 0.00 USD | `+15.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,740,000.00 USD | 2,020.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,750,000.00 USD | 6,220.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,850,000.00 USD | 107,860.00 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,860,000.00 USD | 9,950.00 USD | 0.00 USD | `+16.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,860,000.00 USD | 438.60 USD | 0.00 USD | `+16.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,870,000.00 USD | 6,080.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,910,000.00 USD | 43,730.00 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,020,000.00 USD | 106,450.00 USD | 0.00 USD | `+17.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,020,000.00 USD | 425.62 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,060,000.00 USD | 36,790.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 5,060,000.00 USD | 4,750.00 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,080,000.00 USD | 13,190.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,090,000.00 USD | 18,360.00 USD | 0.00 USD | `+18.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,310,000.00 USD | 219,590.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,350,000.00 USD | 35,450.00 USD | 0.00 USD | `+19.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,390,000.00 USD | 45,900.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,400,000.00 USD | 1,180.00 USD | 0.00 USD | `+19.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,560,000.00 USD | 160,420.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,560,000.00 USD | 5,600.00 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,610,000.00 USD | 45,680.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,630,000.00 USD | 18,790.00 USD | 0.00 USD | `+20.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,700,000.00 USD | 74,260.00 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,750,000.00 USD | 50,010.00 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,760,000.00 USD | 14,320.00 USD | 0.00 USD | `+21.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,770,000.00 USD | 5,560.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,790,000.00 USD | 20,540.00 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,790,000.00 USD | 384.94 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,800,000.00 USD | 6,020.00 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,800,000.00 USD | 5,510.00 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,800,000.00 USD | 581.53 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,800,000.00 USD | 295.23 USD | 0.00 USD | `+22.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,810,000.00 USD | 3,290.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,810,000.00 USD | 281.55 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,820,000.00 USD | 9,380.00 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,820,000.00 USD | 2,840.00 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,830,000.00 USD | 5,860.00 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,940,000.00 USD | 116,400.00 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,940,000.00 USD | 2,210.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 5,950,000.00 USD | 5,720.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,970,000.00 USD | 24,700.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 5,980,000.00 USD | 2,430.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,980,000.00 USD | 286.94 USD | 0.00 USD | `+25.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,980,000.00 USD | 2,900.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 5,990,000.00 USD | 5,800.00 USD | 0.00 USD | `+26.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 5,990,000.00 USD | 6,030.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,990,000.00 USD | 1,970.00 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,000,000.00 USD | 3,100.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,000,000.00 USD | 1,150.00 USD | 0.00 USD | `+27.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,000,000.00 USD | 2,960.00 USD | 0.00 USD | `+27.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,000,000.00 USD | 3,450.00 USD | 0.00 USD | `+27.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,000,000.00 USD | 345.45 USD | 0.00 USD | `+28.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.89` | 6,010,000.00 USD | 2,950.00 USD | 0.00 USD | `+28.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,060,000.00 USD | 51,850.00 USD | 0.00 USD | `+28.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,060,000.00 USD | 1,790.00 USD | 0.00 USD | `+28.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,060,000.00 USD | 1,400.00 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,200,000.00 USD | 133,540.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,670,000.00 USD | 469,530.00 USD | 0.00 USD | `+29.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,670,000.00 USD | 5,620.00 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,680,000.00 USD | 9,410.00 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,800,000.00 USD | 119,340.00 USD | 0.00 USD | `+30.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,800,000.00 USD | 3,000.00 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,940,000.00 USD | 138,290.00 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,960,000.00 USD | 13,610.00 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,020,000.00 USD | 60,620.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,020,000.00 USD | 2,030.00 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,020,000.00 USD | 3,300.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,020,000.00 USD | 2,550.00 USD | 0.00 USD | `+31.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,020,000.00 USD | 425.76 USD | 0.00 USD | `+31.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,030,000.00 USD | 2,030.00 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,030,000.00 USD | 4,120.00 USD | 0.00 USD | `+32.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,030,000.00 USD | 2,000.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,090,000.00 USD | 61,050.00 USD | 0.00 USD | `+32.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,100,000.00 USD | 6,870.00 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,100,000.00 USD | 1,200.00 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,110,000.00 USD | 11,620.00 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,110,000.00 USD | 1,940.00 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,120,000.00 USD | 1,410.00 USD | 0.00 USD | `+34.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,120,000.00 USD | 4,010.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,120,000.00 USD | 3,960.00 USD | 0.00 USD | `+34.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,130,000.00 USD | 3,830.00 USD | 0.00 USD | `+34.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,200,000.00 USD | 66,850.00 USD | 0.00 USD | `+34.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,200,000.00 USD | 1,890.00 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,200,000.00 USD | 195.46 USD | 0.00 USD | `+35.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,200,000.00 USD | 7,480.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,210,000.00 USD | 3,670.00 USD | 0.00 USD | `+36.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,210,000.00 USD | 3,680.00 USD | 0.00 USD | `+36.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,220,000.00 USD | 9,890.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,220,000.00 USD | 310.70 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,220,000.00 USD | 602.77 USD | 0.00 USD | `+37.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,220,000.00 USD | 449.79 USD | 0.00 USD | `+37.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,230,000.00 USD | 2,810.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,230,000.00 USD | 3,560.00 USD | 0.00 USD | `+38.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,230,000.00 USD | 3,230.00 USD | 0.00 USD | `+39.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,240,000.00 USD | 5,120.00 USD | 0.00 USD | `+39.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.42` | 7,240,000.00 USD | 2,120.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,240,000.00 USD | 613.26 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.49` | 7,240,000.00 USD | 2,080.00 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,250,000.00 USD | 10,590.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,300,000.00 USD | 43,090.00 USD | 0.00 USD | `+41.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,300,000.00 USD | 234.54 USD | 0.00 USD | `+41.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,310,000.00 USD | 14,070.00 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,310,000.00 USD | 1,630.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,310,000.00 USD | 2,390.00 USD | 0.00 USD | `+43.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,320,000.00 USD | 1,620.00 USD | 0.00 USD | `+43.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,320,000.00 USD | 1,970.00 USD | 0.00 USD | `+44.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,320,000.00 USD | 3,220.00 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 7,320,000.00 USD | 1,950.00 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,320,000.00 USD | 1,250.00 USD | 0.00 USD | `+44.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,330,000.00 USD | 3,060.00 USD | 0.00 USD | `+45.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,330,000.00 USD | 1,930.00 USD | 0.00 USD | `+45.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,330,000.00 USD | 3,070.00 USD | 0.00 USD | `+45.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,330,000.00 USD | 1,920.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,340,000.00 USD | 3,120.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,340,000.00 USD | 1,550.00 USD | 0.00 USD | `+46.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,340,000.00 USD | 3,080.00 USD | 0.00 USD | `+47.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,340,000.00 USD | 647.56 USD | 0.00 USD | `+47.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,340,000.00 USD | 1,420.00 USD | 0.00 USD | `+48.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,350,000.00 USD | 2,370.00 USD | 0.00 USD | `+48.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,350,000.00 USD | 3,140.00 USD | 0.00 USD | `+48.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,350,000.00 USD | 342.25 USD | 0.00 USD | `+48.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,350,000.00 USD | 1,830.00 USD | 0.00 USD | `+49.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,360,000.00 USD | 2,990.00 USD | 0.00 USD | `+49.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,360,000.00 USD | 2,970.00 USD | 0.00 USD | `+49.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,360,000.00 USD | 391.51 USD | 0.00 USD | `+50.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,360,000.00 USD | 504.21 USD | 0.00 USD | `+51.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.96` | 7,360,000.00 USD | 1,900.00 USD | 0.00 USD | `+51.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,360,000.00 USD | 166.00 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,370,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,380,000.00 USD | 17,380.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,380,000.00 USD | 1,750.00 USD | 0.00 USD | `+52.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,380,000.00 USD | 236.31 USD | 0.00 USD | `+53.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,390,000.00 USD | 1,840.00 USD | 0.00 USD | `+54.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,390,000.00 USD | 264.31 USD | 0.00 USD | `+54.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,390,000.00 USD | 599.34 USD | 0.00 USD | `+55.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,390,000.00 USD | 193.19 USD | 0.00 USD | `+55.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,390,000.00 USD | 3,950.00 USD | 0.00 USD | `+56.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,390,000.00 USD | 1,830.00 USD | 0.00 USD | `+56.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.22` | 7,400,000.00 USD | 1,770.00 USD | 0.00 USD | `+57.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,560,000.00 USD | 160,550.00 USD | 0.00 USD | `+57.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,560,000.00 USD | 1,750.00 USD | 0.00 USD | `+58.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,560,000.00 USD | 731.50 USD | 0.00 USD | `+59.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,560,000.00 USD | 1,730.00 USD | 0.00 USD | `+59.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,560,000.00 USD | 1,710.00 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,570,000.00 USD | 7,870.00 USD | 0.00 USD | `+60.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,570,000.00 USD | 630.05 USD | 0.00 USD | `+60.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,570,000.00 USD | 2,610.00 USD | 0.00 USD | `+61.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,580,000.00 USD | 7,900.00 USD | 0.00 USD | `+63.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,580,000.00 USD | 1,620.00 USD | 0.00 USD | `+64.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,590,000.00 USD | 4,640.00 USD | 0.00 USD | `+64.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,590,000.00 USD | 371.88 USD | 0.00 USD | `+65.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,590,000.00 USD | 2,510.00 USD | 0.00 USD | `+65.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,590,000.00 USD | 380.68 USD | 0.00 USD | `+66.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,590,000.00 USD | 133.12 USD | 0.00 USD | `+67.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,590,000.00 USD | 1,490.00 USD | 0.00 USD | `+68.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,590,000.00 USD | 1,470.00 USD | 0.00 USD | `+69.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,600,000.00 USD | 11,170.00 USD | 0.00 USD | `+69.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,640,000.00 USD | 34,360.00 USD | 0.00 USD | `+69.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,640,000.00 USD | 399.35 USD | 0.00 USD | `+70.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,640,000.00 USD | 100.29 USD | 0.00 USD | `+70.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 7,640,000.00 USD | 1,550.00 USD | 0.00 USD | `+71.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,650,000.00 USD | 10,610.00 USD | 0.00 USD | `+73.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,650,000.00 USD | 309.43 USD | 0.00 USD | `+73.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,790,000.00 USD | 134,220.00 USD | 0.00 USD | `+74.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,870,000.00 USD | 81,310.00 USD | 0.00 USD | `+74.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,870,000.00 USD | 1,390.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,870,000.00 USD | 216.90 USD | 0.00 USD | `+78.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,870,000.00 USD | 738.45 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,870,000.00 USD | 1,350.00 USD | 0.00 USD | `+81.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,930,000.00 USD | 56,000.00 USD | 0.00 USD | `+82.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,930,000.00 USD | 1,260.00 USD | 0.00 USD | `+82.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 8,030,000.00 USD | 103,010.00 USD | 0.00 USD | `+82.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 8,030,000.00 USD | 1,330.00 USD | 0.00 USD | `+83.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 8,030,000.00 USD | 721.22 USD | 0.00 USD | `+84.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,040,000.00 USD | 2,010.00 USD | 0.00 USD | `+87.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 8,040,000.00 USD | 596.33 USD | 0.00 USD | `+88.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 8,040,000.00 USD | 3,670.00 USD | 0.00 USD | `+88.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 8,040,000.00 USD | 1,600.00 USD | 0.00 USD | `+91.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 8,040,000.00 USD | 1,820.00 USD | 0.00 USD | `+91.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,040,000.00 USD | 1,950.00 USD | 0.00 USD | `+93.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 8,120,000.00 USD | 78,870.00 USD | 0.00 USD | `+95.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 8,120,000.00 USD | 773.07 USD | 0.00 USD | `+97.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 8,130,000.00 USD | 1,300.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 8,130,000.00 USD | 236.20 USD | 0.00 USD | `+99.16%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.84` | 31,230,000.00 USD | 0.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 301.36 USD |
| `7D` | `3.86` | 31,230,000.00 USD | 0.00 USD | 31,230,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `7D` | `3.87` | 31,160,000.00 USD | 0.00 USD | 31,160,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD |
| `7D` | `3.88` | 31,070,000.00 USD | 0.00 USD | 31,070,000.00 USD | 107,410.00 USD | 8,890.00 USD | 101,810.00 USD |
| `7D` | `3.89` | 30,850,000.00 USD | 0.00 USD | 30,850,000.00 USD | 25,070.00 USD | 50,710.00 USD | 1,220.00 USD |
| `7D` | `3.90` | 30,780,000.00 USD | 0.00 USD | 30,780,000.00 USD | 93,000.00 USD | 28,250.00 USD | 49,490.00 USD |
| `7D` | `3.91` | 30,610,000.00 USD | 0.00 USD | 30,610,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,950.00 USD |
| `7D` | `3.92` | 30,530,000.00 USD | 0.00 USD | 30,530,000.00 USD | 91,730.00 USD | 41,330.00 USD | 80,170.00 USD |
| `7D` | `3.93` | 30,320,000.00 USD | 0.00 USD | 30,320,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,110.00 USD |
| `7D` | `3.94` | 30,190,000.00 USD | 0.00 USD | 30,190,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,320.00 USD |
| `1D` | `3.95` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 12,850.00 USD | 8,690.00 USD | 16,980.00 USD |
| `7D` | `3.95` | 29,950,000.00 USD | 0.00 USD | 29,950,000.00 USD | 8,490.00 USD | 26,060.00 USD | 552.68 USD |
| `1D` | `3.96` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 23,250.00 USD | 16,000.00 USD | 17,870.00 USD |
| `7D` | `3.96` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,370.00 USD |
| `1D` | `3.97` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 93,920.00 USD | 47,530.00 USD | 53,070.00 USD |
| `7D` | `3.97` | 29,700,000.00 USD | 0.00 USD | 29,700,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD |
| `1D` | `3.98` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 46,710.00 USD | 30,290.00 USD | 10,250.00 USD |
| `7D` | `3.98` | 29,090,000.00 USD | 0.00 USD | 29,090,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,710.00 USD |
| `1D` | `3.99` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 68,470.00 USD | 12,310.00 USD | 34,480.00 USD |
| `7D` | `3.99` | 28,890,000.00 USD | 0.00 USD | 28,890,000.00 USD | 62,170.00 USD | 82,870.00 USD | 101,140.00 USD |
| `1D` | `4.00` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 8,650.00 USD | 7,330.00 USD | 19,210.00 USD |
| `7D` | `4.00` | 28,650,000.00 USD | 0.00 USD | 28,650,000.00 USD | 261,860.00 USD | 105,220.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 109,160.00 USD | 56,050.00 USD | 44,520.00 USD |
| `7D` | `4.01` | 28,110,000.00 USD | 0.00 USD | 28,110,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,410.00 USD |
| `1D` | `4.02` | 14,820,000.00 USD | 0.00 USD | 14,820,000.00 USD | 60,540.00 USD | 20,960.00 USD | 26,150.00 USD |
| `7D` | `4.02` | 27,200,000.00 USD | 0.00 USD | 27,200,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD |
| `1D` | `4.03` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 23,320.00 USD | 32,030.00 USD | 21,210.00 USD |
| `7D` | `4.03` | 26,630,000.00 USD | 0.00 USD | 26,630,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD |
| `1D` | `4.04` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 14,780.00 USD | 32,610.00 USD | 100,740.00 USD |
| `7D` | `4.04` | 26,190,000.00 USD | 0.00 USD | 26,190,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD |
| `1D` | `4.05` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 53,740.00 USD | 0.00 USD | 14,110.00 USD |
| `7D` | `4.05` | 25,900,000.00 USD | 0.00 USD | 25,900,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,710.00 USD |
| `1D` | `4.06` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 30,920.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `4.06` | 25,560,000.00 USD | 0.00 USD | 25,560,000.00 USD | 197,400.00 USD | 45,470.00 USD | 89,780.00 USD |
| `1D` | `4.07` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 1,720.00 USD | 7,520.00 USD | 308.86 USD |
| `7D` | `4.07` | 25,230,000.00 USD | 0.00 USD | 25,230,000.00 USD | 180,120.00 USD | 35,750.00 USD | 41,460.00 USD |
| `1D` | `4.08` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 2,500.00 USD | 0.00 USD | 194.60 USD |
| `7D` | `4.08` | 24,970,000.00 USD | 0.00 USD | 24,970,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD |
| `1D` | `4.09` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 9,420.00 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `4.09` | 24,670,000.00 USD | 0.00 USD | 24,670,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,020.00 USD |
| `1D` | `4.10` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 7,140.00 USD | 7,360.00 USD | 39,590.00 USD |
| `7D` | `4.10` | 24,460,000.00 USD | 0.00 USD | 24,460,000.00 USD | 158,760.00 USD | 98,760.00 USD | 347,120.00 USD |
| `1D` | `4.11` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 17,790.00 USD | 0.00 USD | 459.73 USD |
| `7D` | `4.11` | 23,860,000.00 USD | 0.00 USD | 23,860,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD |
| `1D` | `4.12` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 39,100.00 USD | 45,090.00 USD | 135,010.00 USD |
| `7D` | `4.12` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 97,300.00 USD | 30,180.00 USD | 341,850.00 USD |
| `1D` | `4.13` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 35,390.00 USD | 55,880.00 USD | 37,390.00 USD |
| `7D` | `4.13` | 23,190,000.00 USD | 0.00 USD | 23,190,000.00 USD | 286,870.00 USD | 79,100.00 USD | 107,680.00 USD |
| `1D` | `4.14` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 216,420.00 USD | 38,360.00 USD | 181,900.00 USD |
| `7D` | `4.14` | 22,720,000.00 USD | 0.00 USD | 22,720,000.00 USD | 374,140.00 USD | 57,440.00 USD | 218,300.00 USD |
| `1D` | `4.15` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 253,600.00 USD | 126,760.00 USD | 134,950.00 USD |
| `7D` | `4.15` | 22,070,000.00 USD | 0.00 USD | 22,070,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,600.00 USD |
| `1D` | `4.16` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 24,940.00 USD | 58,100.00 USD | 78,830.00 USD |
| `7D` | `4.16` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 310,530.00 USD | 146,010.00 USD | 174,580.00 USD |
| `1D` | `4.17` | 12,810,000.00 USD | 0.00 USD | 12,810,000.00 USD | 55,780.00 USD | 91,390.00 USD | 98,500.00 USD |
| `7D` | `4.17` | 20,790,000.00 USD | 0.00 USD | 20,790,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,510.00 USD |
| `1D` | `4.18` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 118,210.00 USD | 43,080.00 USD | 63,220.00 USD |
| `7D` | `4.18` | 20,100,000.00 USD | 0.00 USD | 20,100,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD |
| `1D` | `4.19` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 287,670.00 USD | 60,530.00 USD | 170,100.00 USD |
| `7D` | `4.19` | 19,580,000.00 USD | 0.00 USD | 19,580,000.00 USD | 215,210.00 USD | 89,120.00 USD | 671,560.00 USD |
| `1D` | `4.20` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 109,420.00 USD | 162,810.00 USD | 486,450.00 USD |
| `7D` | `4.20` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,260.00 USD |
| `1D` | `4.21` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 66,630.00 USD | 118,560.00 USD | 315.51 USD |
| `7D` | `4.21` | 17,260,000.00 USD | 0.00 USD | 17,260,000.00 USD | 312,160.00 USD | 149,940.00 USD | 118,920.00 USD |
| `1D` | `4.22` | 10,870,000.00 USD | 0.00 USD | 10,870,000.00 USD | 498,330.00 USD | 97,910.00 USD | 375,220.00 USD |
| `7D` | `4.22` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 846,580.00 USD | 161,970.00 USD | 785,900.00 USD |
| `1D` | `4.23` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 710,180.00 USD | 324,910.00 USD | 375,250.00 USD |
| `7D` | `4.23` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 1,080,000.00 USD | 593,230.00 USD | 739,200.00 USD |
| `1D` | `4.24` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 232,690.00 USD | 220,350.00 USD | 236,300.00 USD |
| `7D` | `4.24` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,410.00 USD |
| `1D` | `4.25` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 365,010.00 USD | 239,130.00 USD | 385,920.00 USD |
| `7D` | `4.25` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 350,470.00 USD | 433,770.00 USD | 647,490.00 USD |
| `1D` | `4.26` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 334,900.00 USD | 106,500.00 USD | 280,980.00 USD |
| `7D` | `4.26` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 1,530,000.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 6,090,000.00 USD | 0.00 USD | 6,090,000.00 USD | 607,160.00 USD | 199,830.00 USD | 432,330.00 USD |
| `7D` | `4.27` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 750,150.00 USD | 194,220.00 USD | 1,470,000.00 USD |
| `1D` | `4.28` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 315,460.00 USD | 283,680.00 USD | 173,100.00 USD |
| `7D` | `4.28` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 834,930.00 USD | 497,680.00 USD | 1,110,000.00 USD |
| `1D` | `4.29` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 246,310.00 USD | 24,960.00 USD | 103,000.00 USD |
| `7D` | `4.29` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 223,190.00 USD | 139,890.00 USD | 23,040.00 USD |
| `7D` | `4.30` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD |
| `1D` | `4.31` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 195,160.00 USD | 136,150.00 USD | 314,410.00 USD |
| `7D` | `4.31` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 88,750.00 USD | 0.00 USD | 42,810.00 USD |
| `1D` | `4.32` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 243,570.00 USD | 69,840.00 USD | 193,150.00 USD |
| `7D` | `4.32` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 77,290.00 USD | 0.00 USD |
| `1D` | `4.33` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 214,670.00 USD | 85,110.00 USD | 105,710.00 USD |
| `7D` | `4.33` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 112,660.00 USD | 0.00 USD |
| `1D` | `4.34` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 147,730.00 USD | 82,560.00 USD | 210,610.00 USD |
| `7D` | `4.34` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 137,930.00 USD | 134,560.00 USD |
| `1D` | `4.35` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 64,860.00 USD | 21,470.00 USD | 105,240.00 USD |
| `7D` | `4.35` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 93,250.00 USD | 39,140.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 36,420.00 USD | 34,190.00 USD | 54,350.00 USD |
| `7D` | `4.36` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 86,450.00 USD |
| `1D` | `4.37` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 0.00 USD | 18,760.00 USD | 177.29 USD |
| `1D` | `4.38` | 984,410.00 USD | 0.00 USD | 984,410.00 USD | 60,040.00 USD | 19,120.00 USD | 49,050.00 USD |
| `7D` | `4.38` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 93,060.00 USD | 197,660.00 USD |
| `1D` | `4.39` | 856,200.00 USD | 0.00 USD | 856,200.00 USD | 40,390.00 USD | 151,010.00 USD | 46,080.00 USD |
| `7D` | `4.39` | 884,480.00 USD | 0.00 USD | 884,480.00 USD | 0.00 USD | 62,850.00 USD | 0.00 USD |
| `1D` | `4.40` | 618,720.00 USD | 0.00 USD | 618,720.00 USD | 65,980.00 USD | 170,160.00 USD | 311,940.00 USD |
| `7D` | `4.40` | 821,630.00 USD | 0.00 USD | 821,630.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD |
| `1D` | `4.41` | 70,650.00 USD | 0.00 USD | 70,650.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD |
| `7D` | `4.41` | 421,440.00 USD | 0.00 USD | 421,440.00 USD | 308,040.00 USD | 0.00 USD | 113,410.00 USD |
| `1D` | `4.42` | 222.88 USD | 0.00 USD | 222.88 USD | 0.00 USD | 0.00 USD | 39.06 USD |
| `1D` | `4.43` | 183.82 USD | 0.00 USD | 183.82 USD | 0.00 USD | 0.00 USD | 138.68 USD |
| `1D` | `4.44` | 45.14 USD | 0.00 USD | 45.14 USD | 0.00 USD | 0.00 USD | 45.14 USD |
| `7D` | `4.45` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.46` | 76,550.00 USD | 76,550.00 USD | 0.00 USD | 76,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.46` | 153,090.00 USD | 153,090.00 USD | 0.00 USD | 76,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.46` | 146,190.00 USD | 146,190.00 USD | 0.00 USD | 146,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.47` | 187,320.00 USD | 187,320.00 USD | 0.00 USD | 34,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.47` | 280,880.00 USD | 280,880.00 USD | 0.00 USD | 132,630.00 USD | 0.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 187,500.00 USD | 187,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 184.66 USD |
| `7D` | `4.48` | 281,830.00 USD | 281,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 949.26 USD |
| `1D` | `4.49` | 189,930.00 USD | 189,930.00 USD | 0.00 USD | 2,050.00 USD | 0.00 USD | 380.82 USD |
| `7D` | `4.49` | 525,050.00 USD | 525,050.00 USD | 0.00 USD | 242,770.00 USD | 0.00 USD | 451.28 USD |
| `1D` | `4.50` | 655,610.00 USD | 655,610.00 USD | 0.00 USD | 316,670.00 USD | 148,800.00 USD | 210.22 USD |
| `7D` | `4.50` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 828,400.00 USD | 640,730.00 USD | 504.68 USD |
| `1D` | `4.51` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 457,360.00 USD | 242,880.00 USD | 0.00 USD |
| `7D` | `4.51` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 186,490.00 USD | 0.00 USD |
| `1D` | `4.52` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 552,290.00 USD | 187,770.00 USD | 373,190.00 USD |
| `7D` | `4.52` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 361,140.00 USD | 316,520.00 USD | 191,370.00 USD |
| `1D` | `4.53` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 815,730.00 USD | 106,640.00 USD | 737,830.00 USD |
| `7D` | `4.53` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 214,030.00 USD | 99,290.00 USD | 236,530.00 USD |
| `1D` | `4.54` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 376,850.00 USD | 262,370.00 USD | 690,280.00 USD |
| `7D` | `4.54` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 581,730.00 USD | 328,480.00 USD | 1,100,000.00 USD |
| `1D` | `4.55` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 653,340.00 USD | 254,800.00 USD | 312,540.00 USD |
| `7D` | `4.55` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 989,010.00 USD | 174,120.00 USD | 80,580.00 USD |
| `1D` | `4.56` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 435,050.00 USD | 148,170.00 USD | 253,180.00 USD |
| `7D` | `4.56` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 361,350.00 USD | 307,230.00 USD | 261,960.00 USD |
| `1D` | `4.57` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 314,580.00 USD | 312,090.00 USD | 253,140.00 USD |
| `7D` | `4.57` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 198,050.00 USD | 167,110.00 USD | 0.00 USD |
| `1D` | `4.58` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 249,850.00 USD | 222,910.00 USD | 649,210.00 USD |
| `7D` | `4.58` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 47,710.00 USD | 22,490.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 530,370.00 USD | 191,380.00 USD | 319,300.00 USD |
| `7D` | `4.59` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 674,410.00 USD | 214,810.00 USD | 637,850.00 USD |
| `1D` | `4.60` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 363,790.00 USD | 84,420.00 USD | 249,460.00 USD |
| `7D` | `4.60` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD |
| `1D` | `4.61` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 504,130.00 USD | 131,410.00 USD | 402,590.00 USD |
| `7D` | `4.61` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 76,670.00 USD | 181,090.00 USD | 153,060.00 USD |
| `1D` | `4.62` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 188,210.00 USD | 215,240.00 USD | 516,060.00 USD |
| `7D` | `4.62` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 307,400.00 USD | 83,350.00 USD | 459,250.00 USD |
| `1D` | `4.63` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 483,130.00 USD | 208,050.00 USD | 438,360.00 USD |
| `7D` | `4.63` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 226,350.00 USD | 43,650.00 USD | 272,750.00 USD |
| `1D` | `4.64` | 14,860,000.00 USD | 14,860,000.00 USD | 0.00 USD | 234,120.00 USD | 263,860.00 USD | 20,980.00 USD |
| `7D` | `4.64` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 513,660.00 USD | 254,400.00 USD | 91,570.00 USD |
| `1D` | `4.65` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 270,310.00 USD | 84,330.00 USD | 163,970.00 USD |
| `7D` | `4.65` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 422,980.00 USD | 134,210.00 USD | 288,990.00 USD |
| `1D` | `4.66` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 148,530.00 USD | 92,980.00 USD | 172,630.00 USD |
| `7D` | `4.66` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 159,750.00 USD | 31,420.00 USD | 75,320.00 USD |
| `1D` | `4.67` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 129,030.00 USD | 103,830.00 USD | 274,380.00 USD |
| `7D` | `4.67` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 42,810.00 USD |
| `1D` | `4.68` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 287,250.00 USD | 50,360.00 USD | 175,810.00 USD |
| `7D` | `4.68` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 381,910.00 USD | 0.00 USD | 371,840.00 USD |
| `1D` | `4.69` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 79,980.00 USD | 0.00 USD | 85,890.00 USD |
| `7D` | `4.69` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 339.33 USD |
| `1D` | `4.70` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 5,620.00 USD | 38,510.00 USD | 28.82 USD |
| `7D` | `4.70` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 2,860.00 USD | 37,250.00 USD | 42,750.00 USD |
| `1D` | `4.71` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 5,150.00 USD | 0.00 USD | 471.86 USD |
| `7D` | `4.71` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 9,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.72` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 4,880.00 USD | 19,440.00 USD | 54,280.00 USD |
| `7D` | `4.72` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `4.73` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 4,080.00 USD | 11,800.00 USD | 60,880.00 USD |
| `7D` | `4.73` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 54,580.00 USD | 0.00 USD | 160.93 USD |
| `1D` | `4.74` | 17,590,000.00 USD | 17,590,000.00 USD | 0.00 USD | 208,880.00 USD | 39,720.00 USD | 155,460.00 USD |
| `7D` | `4.74` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 11,160.00 USD | 0.00 USD | 63,790.00 USD |
| `1D` | `4.75` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 165,010.00 USD | 93,530.00 USD | 183,400.00 USD |
| `7D` | `4.75` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 8,240.00 USD | 108,690.00 USD | 342,950.00 USD |
| `1D` | `4.76` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 32,150.00 USD | 27,300.00 USD | 228,550.00 USD |
| `7D` | `4.76` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 942,680.00 USD | 0.00 USD | 272,560.00 USD |
| `1D` | `4.77` | 18,640,000.00 USD | 18,640,000.00 USD | 0.00 USD | 109,820.00 USD | 102,010.00 USD | 105,190.00 USD |
| `7D` | `4.77` | 17,340,000.00 USD | 17,340,000.00 USD | 0.00 USD | 731,680.00 USD | 31,590.00 USD | 101,190.00 USD |
| `1D` | `4.78` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 117,090.00 USD | 78,770.00 USD | 38,100.00 USD |
| `7D` | `4.78` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 922,010.00 USD | 605,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 19,680,000.00 USD | 19,680,000.00 USD | 0.00 USD | 472,440.00 USD | 231,110.00 USD | 100,480.00 USD |
| `7D` | `4.79` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 2,730.00 USD |
| `1D` | `4.80` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 306,250.00 USD | 220,680.00 USD | 35,420.00 USD |
| `7D` | `4.80` | 21,370,000.00 USD | 21,370,000.00 USD | 0.00 USD | 1,070,000.00 USD | 315,940.00 USD | 2,170.00 USD |
| `1D` | `4.81` | 20,890,000.00 USD | 20,890,000.00 USD | 0.00 USD | 407,750.00 USD | 120,180.00 USD | 127,520.00 USD |
| `7D` | `4.81` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 397,490.00 USD | 125,900.00 USD | 101,480.00 USD |
| `1D` | `4.82` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 295,730.00 USD | 191,140.00 USD | 433,180.00 USD |
| `7D` | `4.82` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 998,780.00 USD | 369,430.00 USD | 1,320,000.00 USD |
| `1D` | `4.83` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 260,840.00 USD | 100,910.00 USD | 330,690.00 USD |
| `7D` | `4.83` | 26,330,000.00 USD | 26,330,000.00 USD | 0.00 USD | 820,240.00 USD | 85,680.00 USD | 739,490.00 USD |
| `1D` | `4.84` | 22,730,000.00 USD | 22,730,000.00 USD | 0.00 USD | 76,430.00 USD | 28,910.00 USD | 122,570.00 USD |
| `7D` | `4.84` | 26,760,000.00 USD | 26,760,000.00 USD | 0.00 USD | 97,300.00 USD | 9,680.00 USD | 322,510.00 USD |
| `1D` | `4.85` | 23,290,000.00 USD | 23,290,000.00 USD | 0.00 USD | 182,320.00 USD | 157,810.00 USD | 210,800.00 USD |
| `7D` | `4.85` | 28,740,000.00 USD | 28,740,000.00 USD | 0.00 USD | 487,940.00 USD | 328,780.00 USD | 1,160,000.00 USD |
| `1D` | `4.86` | 23,870,000.00 USD | 23,870,000.00 USD | 0.00 USD | 214,210.00 USD | 43,740.00 USD | 328,820.00 USD |
| `7D` | `4.86` | 30,150,000.00 USD | 30,150,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,240.00 USD |
| `1D` | `4.87` | 24,210,000.00 USD | 24,210,000.00 USD | 0.00 USD | 201,810.00 USD | 86,180.00 USD | 46,210.00 USD |
| `7D` | `4.87` | 31,210,000.00 USD | 31,210,000.00 USD | 0.00 USD | 263,700.00 USD | 136,820.00 USD | 663,310.00 USD |
| `1D` | `4.88` | 24,510,000.00 USD | 24,510,000.00 USD | 0.00 USD | 11,350.00 USD | 30,820.00 USD | 265,360.00 USD |
| `7D` | `4.88` | 32,880,000.00 USD | 32,880,000.00 USD | 0.00 USD | 388,550.00 USD | 480,980.00 USD | 792,630.00 USD |
| `1D` | `4.89` | 24,780,000.00 USD | 24,780,000.00 USD | 0.00 USD | 143,310.00 USD | 46,470.00 USD | 77,340.00 USD |
| `7D` | `4.89` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `1D` | `4.90` | 25,370,000.00 USD | 25,370,000.00 USD | 0.00 USD | 79,980.00 USD | 112,960.00 USD | 391,590.00 USD |
| `7D` | `4.90` | 34,600,000.00 USD | 34,600,000.00 USD | 0.00 USD | 446,650.00 USD | 145,910.00 USD | 541,190.00 USD |
| `1D` | `4.91` | 25,880,000.00 USD | 25,880,000.00 USD | 0.00 USD | 292,500.00 USD | 85,510.00 USD | 134,540.00 USD |
| `7D` | `4.91` | 36,030,000.00 USD | 36,030,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `1D` | `4.92` | 26,360,000.00 USD | 26,360,000.00 USD | 0.00 USD | 190,700.00 USD | 89,190.00 USD | 207,340.00 USD |
| `7D` | `4.92` | 37,770,000.00 USD | 37,770,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `1D` | `4.93` | 26,700,000.00 USD | 26,700,000.00 USD | 0.00 USD | 118,690.00 USD | 64,250.00 USD | 151,050.00 USD |
| `7D` | `4.93` | 39,320,000.00 USD | 39,320,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `1D` | `4.94` | 26,950,000.00 USD | 26,950,000.00 USD | 0.00 USD | 36,860.00 USD | 65,310.00 USD | 144,840.00 USD |
| `7D` | `4.94` | 40,630,000.00 USD | 40,630,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD |
| `1D` | `4.95` | 27,080,000.00 USD | 27,080,000.00 USD | 0.00 USD | 79,890.00 USD | 4,170.00 USD | 46,560.00 USD |
| `7D` | `4.95` | 41,930,000.00 USD | 41,930,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,070.00 USD |
| `1D` | `4.96` | 27,190,000.00 USD | 27,190,000.00 USD | 0.00 USD | 69,140.00 USD | 21,750.00 USD | 23,010.00 USD |
| `7D` | `4.96` | 43,120,000.00 USD | 43,120,000.00 USD | 0.00 USD | 602,080.00 USD | 214,910.00 USD | 375,480.00 USD |
| `1D` | `4.97` | 27,280,000.00 USD | 27,280,000.00 USD | 0.00 USD | 5,050.00 USD | 7,520.00 USD | 77,900.00 USD |
| `7D` | `4.97` | 43,500,000.00 USD | 43,500,000.00 USD | 0.00 USD | 194,450.00 USD | 72,330.00 USD | 113,140.00 USD |
| `7D` | `4.98` | 44,290,000.00 USD | 44,290,000.00 USD | 0.00 USD | 436,230.00 USD | 88,580.00 USD | 270,990.00 USD |
| `7D` | `4.99` | 44,640,000.00 USD | 44,640,000.00 USD | 0.00 USD | 127,170.00 USD | 103,060.00 USD | 116,440.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.28B` | Total OI Tokens: `289,882,977.4 NEAR`
  * 1h OI Change: `-1.50%` | 4h OI Change: `+1.16%` | 24h OI Change: `-1.78%`
  * Exchange Breakdown: Binance=`249.32M` | Bybit=`172.78M` | OKX=`54.38M` | Hyperliquid=`258.57M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `41.23K` | Last 24h: `106.01K` | Last 3d: `314.39K` | Last 7d: `172.37K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0079%` | **USDT OKX** | `0.0078%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0079%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0081%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `45.41%` | `54.59%` | `0.83` | 5,590,000.00 USD |
| `15M` | `Binance` | `52.53%` | `47.47%` | `1.11` | 1,270,000.00 USD |
| `15M` | `OKX` | `24.41%` | `75.59%` | `0.32` | 472,020.00 USD |
| `15M` | `Bybit` | `60.07%` | `39.93%` | `1.50` | 382,000.00 USD |
| `15M` | `KuCoin` | `30.36%` | `69.64%` | `0.44` | 37,810.00 USD |
| `15M` | `Gate` | `32.82%` | `67.18%` | `0.49` | 49,540.00 USD |
| `15M` | `Bitget` | `38.08%` | `61.92%` | `0.61` | 71,640.00 USD |
| `15M` | `BingX` | `14.2%` | `85.8%` | `0.17` | 406,520.00 USD |
| `15M` | `MEXC` | `52.01%` | `47.99%` | `1.08` | 2,420,000.00 USD |
| `15M` | `Bitunix` | `49.42%` | `50.58%` | `0.98` | 88,590.00 USD |
| `15M` | `Hyperliquid` | `56.74%` | `43.26%` | `1.31` | 14,010.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.34%` | `44.66%` | `1.24` | 103,770.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.45%` | `99.55%` | `0.00` | 218,350.00 USD |
| `15M` | `HTX` | `93.91%` | `6.09%` | `15.42` | 95.56 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `81.88%` | `18.12%` | `4.52` | 39,330.00 USD |
| `15M` | `Aster` | `99.82%` | `0.18%` | `554.56` | 9,490.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `62.71%` | `37.29%` | `1.68` | 2,700.00 USD |
| `15M` | `Whale Positions` | `52.53%` | `47.47%` | `1.11` | 1,270,000.00 USD |
| `15M` | `Global Accounts` | `45.41%` | `54.59%` | `0.83` | 5,590,000.00 USD |
| `1H` | `NEAR` | `55.12%` | `44.88%` | `1.23` | 55,280,000.00 USD |
| `1H` | `Binance` | `57.03%` | `42.97%` | `1.33` | 36,960,000.00 USD |
| `1H` | `OKX` | `46.07%` | `53.93%` | `0.85` | 3,270,000.00 USD |
| `1H` | `Bybit` | `56.46%` | `43.54%` | `1.30` | 1,510,000.00 USD |
| `1H` | `KuCoin` | `43.58%` | `56.42%` | `0.77` | 257,510.00 USD |
| `1H` | `Gate` | `48.84%` | `51.16%` | `0.95` | 4,870,000.00 USD |
| `1H` | `Bitget` | `59.32%` | `40.68%` | `1.46` | 1,170,000.00 USD |
| `1H` | `BingX` | `50.88%` | `49.12%` | `1.04` | 1,630,000.00 USD |
| `1H` | `MEXC` | `58.67%` | `41.33%` | `1.42` | 680,730.00 USD |
| `1H` | `Bitunix` | `51.88%` | `48.12%` | `1.08` | 1,370,000.00 USD |
| `1H` | `Hyperliquid` | `51.15%` | `48.85%` | `1.05` | 641,210.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.07%` | `53.93%` | `0.85` | 1,340,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `95.13%` | `4.87%` | `19.53` | 262,360.00 USD |
| `1H` | `HTX` | `78.45%` | `21.55%` | `3.64` | 194,530.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.66%` | `57.34%` | `0.74` | 237,590.00 USD |
| `1H` | `Aster` | `56.79%` | `43.21%` | `1.31` | 618,840.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `39.39%` | `60.61%` | `0.65` | 265,570.00 USD |
| `1H` | `Whale Positions` | `57.03%` | `42.97%` | `1.33` | 36,960,000.00 USD |
| `1H` | `Global Accounts` | `55.12%` | `44.88%` | `1.23` | 55,280,000.00 USD |
| `4H` | `NEAR` | `46.68%` | `53.32%` | `0.88` | 82,360,000.00 USD |
| `4H` | `Binance` | `49.94%` | `50.06%` | `1.00` | 22,810,000.00 USD |
| `4H` | `OKX` | `46.43%` | `53.57%` | `0.87` | 6,070,000.00 USD |
| `4H` | `Bybit` | `53.27%` | `46.73%` | `1.14` | 4,110,000.00 USD |
| `4H` | `KuCoin` | `49.4%` | `50.6%` | `0.98` | 666,650.00 USD |
| `4H` | `Gate` | `41.59%` | `58.41%` | `0.71` | 1,070,000.00 USD |
| `4H` | `Bitget` | `44.66%` | `55.34%` | `0.81` | 2,240,000.00 USD |
| `4H` | `BingX` | `32.29%` | `67.71%` | `0.48` | 4,310,000.00 USD |
| `4H` | `MEXC` | `49.61%` | `50.39%` | `0.98` | 31,910,000.00 USD |
| `4H` | `Bitunix` | `41.71%` | `58.29%` | `0.72` | 2,760,000.00 USD |
| `4H` | `Hyperliquid` | `51.62%` | `48.38%` | `1.07` | 885,240.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `45.33%` | `54.67%` | `0.83` | 1,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.87%` | `90.13%` | `0.11` | 3,100,000.00 USD |
| `4H` | `HTX` | `43.82%` | `56.18%` | `0.78` | 24,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `69.38%` | `30.62%` | `2.27` | 213,050.00 USD |
| `4H` | `Aster` | `59.26%` | `40.74%` | `1.45` | 59,070.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `29.76%` | `70.24%` | `0.42` | 177,690.00 USD |
| `4H` | `Whale Positions` | `49.94%` | `50.06%` | `1.00` | 22,810,000.00 USD |
| `4H` | `Global Accounts` | `46.68%` | `53.32%` | `0.88` | 82,360,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.42` | `4.42` | `4.42` | `4.43` | `4.41` | 2,349,084.35 USD | 1,299,933.14 USD | 1,049,151.21 USD | 250,781.93 USD | `+10.68%` | `3B / 1S` |
| `0:00 UTC` | `4.40` | `4.40` | `4.40` | `4.42` | `4.38` | 4,910,877.38 USD | 1,659,091.84 USD | 3,251,785.54 USD | -1,592,693.71 USD | `-32.43%` | `0B / 10S` |
| `5:00 UTC` | `4.40` | `4.40` | `4.40` | `4.41` | `4.39` | 3,908,851.94 USD | 1,991,153.28 USD | 1,917,698.65 USD | 73,454.63 USD | `+1.88%` | `3B / 1S` |
| `0:00 UTC` | `4.43` | `4.42` | `4.43` | `4.45` | `4.40` | 7,532,142.79 USD | 4,259,193.05 USD | 3,272,949.73 USD | 986,243.32 USD | `+13.09%` | `8B / 4S` |
| `5:00 UTC` | `4.44` | `4.44` | `4.44` | `4.45` | `4.42` | 4,908,611.32 USD | 2,407,821.61 USD | 2,500,789.71 USD | -92,968.10 USD | `-1.89%` | `5B / 2S` |
| `0:00 UTC` | `4.48` | `4.48` | `4.48` | `4.50` | `4.45` | 13,239,385.49 USD | 6,890,699.76 USD | 6,348,685.73 USD | 542,014.04 USD | `+4.09%` | `7B / 0S` |
| `5:00 UTC` | `4.49` | `4.49` | `4.49` | `4.52` | `4.46` | 17,628,423.17 USD | 8,772,146.50 USD | 8,856,276.67 USD | -84,130.16 USD | `-0.48%` | `4B / 3S` |
| `0:00 UTC` | `4.44` | `4.44` | `4.44` | `4.49` | `4.41` | 11,253,305.16 USD | 4,637,687.11 USD | 6,615,618.05 USD | -1,977,930.94 USD | `-17.58%` | `3B / 17S` |
| `5:00 UTC` | `4.45` | `4.44` | `4.45` | `4.47` | `4.42` | 8,493,651.28 USD | 4,421,566.12 USD | 4,072,085.16 USD | 349,480.96 USD | `+4.11%` | `4B / 2S` |
| `0:00 UTC` | `4.44` | `4.44` | `4.44` | `4.46` | `4.42` | 2,728,868.42 USD | 1,311,393.58 USD | 1,417,474.85 USD | -106,081.27 USD | `-3.89%` | `6B / 10S` |

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
| `5m` | 4,120.00 USD | -293,940.00 USD | **`DISTRIBUTION`** |
| `15m` | 115,250.00 USD | 491,340.00 USD | **`ACCUMULATION`** |
| `30m` | 211,080.00 USD | 1,510,000.00 USD | **`ACCUMULATION`** |
| `1h` | -411,460.00 USD | -2,760,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -408,520.00 USD | 223,300.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,830,000.00 USD | -1,370,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,470,000.00 USD | 1,590,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,010,000.00 USD | -27,420,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,330,000.00 USD | -26,340,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,940,000.00 USD | -52,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -70,130,000.00 USD | -100,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -234,990,000.00 USD | -689,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.12K` | 15m=`+115.25K` | 1h=`-411.46K` | 24h=`-7.94M`
* Futures Capital Netflows: 5m=`-293.94K` | 15m=`+491.34K` | 1h=`-2.76M` | 24h=`-52.17M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4.37` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.28` (Risk Distance: `0.0966` pts)
  * +2.5R Take Profit: `4.62`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.64` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.74` (Risk Distance: `0.0966` pts)
  * +2.5R Take Profit: `4.40`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
