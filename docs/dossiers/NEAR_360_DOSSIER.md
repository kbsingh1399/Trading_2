# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.43` | **Live Ask Quote**: `4.46` | **Mid Price**: `4.45`
- **Spread Points**: `30.00` | **Spread BPS**: `67.45 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.43` | VWAP Z-Score: `+0.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0386` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.26` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.71` | Lower -3.00σ Band: `4.15`
  * Upper +2.51σ Band: `4.66` | Lower -2.51σ Band: `4.20`
  * Upper +2.01σ Band: `4.62` | Lower -2.01σ Band: `4.25`
  * Upper +2.00σ Band: `4.62` | Lower -2.00σ Band: `4.25`
  * Upper +1.28σ Band: `4.55` | Lower -1.28σ Band: `4.31`
  * Upper +1.00σ Band: `4.52` | Lower -1.00σ Band: `4.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.43` | EMA-20=`4.41` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.43` (Slope: `+0.0000`) | EMA-100=`4.49`
  * Institutional Anchors: EMA-144=`4.51` | EMA-200=`4.52` (Slope: `-0.2740`) | EMA-233=`4.52`
- **Range Boundaries**: 24H High=`4.80` | 24H Low=`4.27` | Weekly High=`4.80` | Weekly Low=`4.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.50` (Distance: `-1.14%`)
  * Point of Control (POC) = `4.41` (Distance: `+0.89%`)
  * Value Area Low (VAL) = `4.31` (Distance: `+3.15%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.73` | POC=`4.68` | VAL=`4.61`
  * Prior Day Extremes: PDH=`4.80` | PDL=`4.53` | PDC=`4.71`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.62` | Weekly POC=`4.44` | Weekly VAL=`4.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.75` | Low=`4.39`
  * London Session (08:00-16:00 UTC): High=`4.50` | Low=`4.27`
  * New York Session (13:00-21:00 UTC): High=`4.50` | Low=`4.34`
  * Initial Balance (First Hour): IB High=`4.50` | IB Low=`4.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.43` - `4.47`
  * Optimal Trade Entry (OTE 0.705): `4.46`
  * Structural Invalidation Anchor (0.786): `4.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.45` | `4.46` | `4.44` | `4.45` | `292,094` | 1,298,568.54 USD | -54,196.17 USD | `-4.17%` | -27,829,127.24 USD | `-0.06` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4.45` | `4.46` | `4.43` | `4.43` | `257,890` | 1,145,789.28 USD | 162,993.73 USD | `+14.23%` | -27,666,133.52 USD | `+0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4.44` | `4.45` | `4.42` | `4.45` | `240,157` | 1,064,541.26 USD | -87,113.07 USD | `-8.18%` | -27,753,246.59 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.48` | `4.49` | `4.41` | `4.43` | `2,534,544` | 11,253,305.16 USD | -1,977,930.95 USD | `-17.58%` | -28,124,412.03 USD | `-2.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.43` | `4.47` | `4.42` | `4.45` | `1,912,461` | 8,493,651.28 USD | 349,480.96 USD | `+4.11%` | -27,774,931.08 USD | `+0.63` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `4.45` | `4.46` | `4.42` | `4.45` | `790,141` | 3,508,899.09 USD | 21,684.49 USD | `+0.62%` | -27,753,246.59 USD | `+0.25` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.42` | `4.45` | `4.38` | `4.45` | `4,814,312` | 21,260,483.42 USD | -625,963.85 USD | `-2.94%` | -27,253,179.00 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.45` | `4.51` | `4.41` | `4.45` | `11,330,540` | 50,614,765.09 USD | -1,170,566.12 USD | `-2.31%` | -28,423,745.12 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.45` | `4.46` | `4.42` | `4.45` | `790,141` | 3,508,899.09 USD | 21,684.49 USD | `+0.62%` | -28,402,060.64 USD | `+0.43` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -24,290,560.14 USD | `-1.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -25,384,269.17 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.51` | `4.38` | `4.45` | `16,934,993` | 75,384,147.60 USD | -1,774,845.48 USD | `-2.35%` | -27,159,114.66 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.75` | `4.82` | `4.66` | `4.73` | `16,593,267` | 78,638,657.86 USD | -4,068,826.21 USD | `-5.17%` | 3,183,079.42 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.73` | `4.73` | `4.40` | `4.42` | `25,745,501` | 116,497,184.49 USD | -11,801,514.25 USD | `-10.13%` | -8,618,434.83 USD | `-1.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.42` | `4.51` | `4.28` | `4.32` | `30,541,980` | 133,934,580.88 USD | -15,672,125.31 USD | `-11.70%` | -24,290,560.14 USD | `-1.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -25,384,269.17 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.51` | `4.38` | `4.45` | `16,934,993` | 75,384,147.60 USD | -1,774,845.48 USD | `-2.35%` | -27,159,114.66 USD | `+0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`4.45`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

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
| `ANNOUNCEMENT` | `INFO` | `4.64` | 8,708.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.71K USD at 4.6358 USD [API] | `2026-10-27 18:54:01` |
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
| `Live` | `Long Liquidation` | `0.8950` | 45,150.00 USD | 36,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 11,240.00 USD | 36,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 1,880.00 USD | 36,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 5,280,000.00 USD | 36,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 1,160.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 40,780.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 128.55 USD | 31,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 32,220.00 USD | 31,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 7,890.00 USD | 31,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 1,850.00 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,730.00 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 2,360.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 73,400.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 58,550.00 USD | 31,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 31,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 875.70 USD | 31,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 31,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 52,110.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 161.82 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 238.19 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 25,760.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 568.22 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 558.38 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 653.98 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 449,810.00 USD | 30,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 464.78 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 825.82 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 1,340.00 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 130.32 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 42,510.00 USD | 30,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 1,710.00 USD | 30,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 100,010.00 USD | 30,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 16,870.00 USD | 30,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 461.64 USD | 30,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 30,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 1,510.00 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 157.50 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 67,700.00 USD | 30,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 40,330.00 USD | 30,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 226.29 USD | 30,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 688.80 USD | 30,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,480.00 USD | 30,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 4,900.00 USD | 30,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 9,270.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.54` | 12,200.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 13,300.00 USD | 30,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 30,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 4,620.00 USD | 30,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,380.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 191.64 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 3,390.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,310.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 3,210.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 13,020.00 USD | 30,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 2,850.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,060.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 16,920.00 USD | 30,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 10,000.00 USD | 30,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 1,200.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 21,990.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 211.80 USD | 30,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 11,470.00 USD | 30,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 1,570.00 USD | 30,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 30,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 25,090.00 USD | 30,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 59,460.00 USD | 30,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 65,820.00 USD | 29,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 4,830.00 USD | 29,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 4,130.00 USD | 29,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 937.50 USD | 29,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 909.51 USD | 29,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 25,520.00 USD | 29,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 4,280.00 USD | 29,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 8,970.00 USD | 29,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 5,080.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 23,990.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 41,640.00 USD | 29,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 189,050.00 USD | 29,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 127,520.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,580.00 USD | 29,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 124,870.00 USD | 29,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 29,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 41,550.00 USD | 29,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,810.00 USD | 29,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 369.90 USD | 29,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 2,910.00 USD | 29,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 299,800.00 USD | 29,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 20,990.00 USD | 28,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 2,060.00 USD | 28,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 19,450.00 USD | 28,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 37,350.00 USD | 28,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 30,920.00 USD | 28,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 26,150.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 894.04 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 1,090.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 575.02 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 21,610.00 USD | 28,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 1,950,000.00 USD | 28,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 35,390.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,610.00 USD | 26,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 30,830.00 USD | 26,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 115,680.00 USD | 26,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 122,830.00 USD | 26,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 5,560.00 USD | 26,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 3,300.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 4,930.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 70,680.00 USD | 26,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 5,180.00 USD | 26,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 440.31 USD | 26,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 12,050.00 USD | 26,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 12,820.00 USD | 26,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 70,960.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 8,720.00 USD | 26,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 1,610,000.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 422,220.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 652.30 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 143.70 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 11,910.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 342,760.00 USD | 24,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 242.50 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,690.00 USD | 23,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,240.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 11,980.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 654,860.00 USD | 23,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 3,610.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,040.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 7,490.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 9,500.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 23,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 23,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 1,730.00 USD | 23,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 16,100.00 USD | 23,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,810.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,310.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 4,030.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 2,910.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 158,280.00 USD | 23,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 3,350.00 USD | 23,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 30,530.00 USD | 23,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 57,850.00 USD | 23,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 7,240.00 USD | 23,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 18,980.00 USD | 23,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 191,610.00 USD | 22,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 189,890.00 USD | 22,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,750.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 35,600.00 USD | 22,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 2,880.00 USD | 22,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 41,410.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 2,150.00 USD | 22,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 4,980.00 USD | 22,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 776,080.00 USD | 22,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 30,290.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 19,380.00 USD | 21,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 11,050.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 207,820.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 9,140.00 USD | 21,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,140.00 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 410.82 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,560.00 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 13,400.00 USD | 21,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 1,330.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 19,050.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 13,910.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 21,740.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 3,230.00 USD | 21,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 7,310.00 USD | 21,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 64,080.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 171.08 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 12,440.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 35,190.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 45,300.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 494,090.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 15,460.00 USD | 20,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 73,850.00 USD | 20,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 125,310.00 USD | 20,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 44,940.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 123,540.00 USD | 20,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 22,270.00 USD | 20,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,530.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 7,450.00 USD | 20,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 27,240.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 151,660.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 8,940.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 37,360.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 56,990.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 2,390.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 28,660.00 USD | 19,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 99,120.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 168,550.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 6,880.00 USD | 19,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 102,670.00 USD | 19,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 23,460.00 USD | 19,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,780.00 USD | 19,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 26,750.00 USD | 19,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 868,920.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 476.53 USD | 18,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 48,150.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 848,500.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 163,060.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 1,390,000.00 USD | 17,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 57,870.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 21,100.00 USD | 16,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 7,330.00 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 53,610.00 USD | 16,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 45,290.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 8,630.00 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 4,760.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 14,490.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 45,780.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 3,830.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 99,440.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 187,750.00 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 6,630.00 USD | 15,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 33,900.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 43,330.00 USD | 15,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 158,380.00 USD | 15,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 11,280.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 105,730.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 13,960.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 70,420.00 USD | 15,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 19,680.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 22,360.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 227,660.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 13,230.00 USD | 14,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 338,000.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 371,970.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 15,990.00 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 116,620.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 17,180.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 47,790.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.60` | 10,850.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 845.19 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 76,190.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.63` | 53,270.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 67,270.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 52,620.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 510,060.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 191,730.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 226,010.00 USD | 13,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.69` | 6,200.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 33,200.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.71` | 77,580.00 USD | 12,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 22,200.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.73` | 8,970.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 139,060.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 162,760.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 92,970.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.77` | 23,300.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 46,690.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.79` | 136,080.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 16,990.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.81` | 68,990.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 20,520.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.83` | 174,170.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.84` | 31,230,000.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 301.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 27,390.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 32,230.00 USD | 11,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.86` | 31,230,000.00 USD | 31,230,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 20,990.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.87` | 31,150,000.00 USD | 31,150,000.00 USD | 54,110.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 4,040.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.88` | 31,070,000.00 USD | 31,070,000.00 USD | 107,410.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 29,390.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.89` | 30,850,000.00 USD | 30,850,000.00 USD | 25,070.00 USD | 50,710.00 USD | 1,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 95,980.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.90` | 30,770,000.00 USD | 30,770,000.00 USD | 93,000.00 USD | 28,250.00 USD | 49,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 567,610.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.91` | 30,600,000.00 USD | 30,600,000.00 USD | 1,280.00 USD | 25,680.00 USD | 46,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 3,920,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.92` | 30,530,000.00 USD | 30,530,000.00 USD | 91,730.00 USD | 41,330.00 USD | 80,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 198,930.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.93` | 30,310,000.00 USD | 30,310,000.00 USD | 51,660.00 USD | 26,290.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 17,860.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 24,580.00 USD | 28,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 30,190,000.00 USD | 30,190,000.00 USD | 75,150.00 USD | 36,920.00 USD | 126,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 551,430.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 15,550,000.00 USD | 15,550,000.00 USD | 12,850.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 29,950,000.00 USD | 29,950,000.00 USD | 8,490.00 USD | 26,060.00 USD | 552.68 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 170,710.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 15,530,000.00 USD | 15,530,000.00 USD | 23,250.00 USD | 16,000.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 29,910,000.00 USD | 29,910,000.00 USD | 52,720.00 USD | 15,590.00 USD | 151,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 126,910.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 15,470,000.00 USD | 15,470,000.00 USD | 93,920.00 USD | 47,530.00 USD | 53,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 29,690,000.00 USD | 29,690,000.00 USD | 231,790.00 USD | 102,960.00 USD | 268,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 43,490.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 15,280,000.00 USD | 15,280,000.00 USD | 46,710.00 USD | 30,290.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 29,090,000.00 USD | 29,090,000.00 USD | 31,450.00 USD | 84,480.00 USD | 85,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 67,030.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 15,190,000.00 USD | 15,190,000.00 USD | 68,470.00 USD | 12,310.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 28,890,000.00 USD | 28,890,000.00 USD | 62,170.00 USD | 82,870.00 USD | 101,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 36,180.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 15,070,000.00 USD | 15,070,000.00 USD | 8,110.00 USD | 7,330.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 28,640,000.00 USD | 28,640,000.00 USD | 261,860.00 USD | 105,220.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 57,060.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 15,040,000.00 USD | 15,040,000.00 USD | 109,160.00 USD | 56,050.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 28,110,000.00 USD | 28,110,000.00 USD | 384,840.00 USD | 94,720.00 USD | 437,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 62,150.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 14,830,000.00 USD | 14,830,000.00 USD | 60,540.00 USD | 20,960.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 27,190,000.00 USD | 27,190,000.00 USD | 279,800.00 USD | 88,330.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 141,530.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 14,720,000.00 USD | 14,720,000.00 USD | 23,320.00 USD | 32,030.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 26,630,000.00 USD | 26,630,000.00 USD | 250,870.00 USD | 45,290.00 USD | 149,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 15,430.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 14,650,000.00 USD | 14,650,000.00 USD | 14,780.00 USD | 32,610.00 USD | 100,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 26,180,000.00 USD | 26,180,000.00 USD | 98,660.00 USD | 65,670.00 USD | 121,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 64,110.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 14,500,000.00 USD | 14,500,000.00 USD | 53,740.00 USD | 0.00 USD | 14,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 25,900,000.00 USD | 25,900,000.00 USD | 184,470.00 USD | 72,110.00 USD | 85,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 223,930.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 14,430,000.00 USD | 14,430,000.00 USD | 30,920.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 25,550,000.00 USD | 25,550,000.00 USD | 197,400.00 USD | 45,470.00 USD | 89,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 362,220.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 14,370,000.00 USD | 14,370,000.00 USD | 1,720.00 USD | 7,520.00 USD | 332.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 25,220,000.00 USD | 25,220,000.00 USD | 180,120.00 USD | 35,750.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 359,690.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 14,360,000.00 USD | 14,360,000.00 USD | 2,500.00 USD | 0.00 USD | 16.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 24,960,000.00 USD | 24,960,000.00 USD | 9,180.00 USD | 63,440.00 USD | 230,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 740,450.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 14,360,000.00 USD | 14,360,000.00 USD | 9,420.00 USD | 0.00 USD | 150.55 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 24,660,000.00 USD | 24,660,000.00 USD | 132,550.00 USD | 26,560.00 USD | 43,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 45,110.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 14,350,000.00 USD | 14,350,000.00 USD | 7,820.00 USD | 14,180.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 24,460,000.00 USD | 24,460,000.00 USD | 158,760.00 USD | 98,760.00 USD | 347,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 482,190.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 14,290,000.00 USD | 14,290,000.00 USD | 17,790.00 USD | 0.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 23,850,000.00 USD | 23,850,000.00 USD | 110,780.00 USD | 0.00 USD | 85,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 368,940.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 14,250,000.00 USD | 14,250,000.00 USD | 39,380.00 USD | 45,090.00 USD | 148,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 23,660,000.00 USD | 23,660,000.00 USD | 97,300.00 USD | 30,180.00 USD | 341,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 54,610.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 14,020,000.00 USD | 14,020,000.00 USD | 35,390.00 USD | 55,880.00 USD | 37,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 23,190,000.00 USD | 23,190,000.00 USD | 286,870.00 USD | 79,100.00 USD | 107,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.13` | 84,130.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.14` | 13,890,000.00 USD | 13,890,000.00 USD | 215,610.00 USD | 38,360.00 USD | 181,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 22,710,000.00 USD | 22,710,000.00 USD | 372,080.00 USD | 57,440.00 USD | 218,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 133,280.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 13,450,000.00 USD | 13,450,000.00 USD | 253,600.00 USD | 126,760.00 USD | 135,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 22,070,000.00 USD | 22,070,000.00 USD | 254,890.00 USD | 134,230.00 USD | 261,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.16` | 61,340.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.16` | 12,940,000.00 USD | 12,940,000.00 USD | 24,940.00 USD | 58,100.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.16` | 21,420,000.00 USD | 21,420,000.00 USD | 310,530.00 USD | 146,010.00 USD | 174,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 220,090.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 12,780,000.00 USD | 12,780,000.00 USD | 55,780.00 USD | 91,390.00 USD | 98,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 20,780,000.00 USD | 20,780,000.00 USD | 124,760.00 USD | 114,530.00 USD | 446,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.17` | 23,690.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.18` | 12,530,000.00 USD | 12,530,000.00 USD | 118,210.00 USD | 43,080.00 USD | 63,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 20,100,000.00 USD | 20,100,000.00 USD | 360,840.00 USD | 103,320.00 USD | 59,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.18` | 71,370.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.19` | 12,310,000.00 USD | 12,310,000.00 USD | 287,670.00 USD | 60,530.00 USD | 169,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 19,580,000.00 USD | 19,580,000.00 USD | 215,210.00 USD | 89,120.00 USD | 671,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.20` | 359,880.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.20` | 11,790,000.00 USD | 11,790,000.00 USD | 109,420.00 USD | 162,810.00 USD | 486,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 18,600,000.00 USD | 18,600,000.00 USD | 337,660.00 USD | 122,960.00 USD | 882,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 207,470.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.21` | 11,030,000.00 USD | 11,030,000.00 USD | 66,630.00 USD | 118,560.00 USD | 778.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 17,260,000.00 USD | 17,260,000.00 USD | 312,160.00 USD | 149,940.00 USD | 118,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.21` | 159,020.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 10,840,000.00 USD | 10,840,000.00 USD | 497,250.00 USD | 97,910.00 USD | 375,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 16,680,000.00 USD | 16,680,000.00 USD | 843,820.00 USD | 161,970.00 USD | 785,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.22` | 46,270.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.23` | 9,870,000.00 USD | 9,870,000.00 USD | 710,180.00 USD | 324,910.00 USD | 375,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 14,880,000.00 USD | 14,880,000.00 USD | 1,080,000.00 USD | 593,230.00 USD | 739,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.24` | 70,770.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.24` | 8,460,000.00 USD | 8,460,000.00 USD | 232,690.00 USD | 220,350.00 USD | 236,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.24` | 12,470,000.00 USD | 12,470,000.00 USD | 657,830.00 USD | 485,260.00 USD | 567,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 27,920.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.25` | 7,770,000.00 USD | 7,770,000.00 USD | 366,020.00 USD | 239,130.00 USD | 386,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 10,760,000.00 USD | 10,760,000.00 USD | 350,470.00 USD | 433,770.00 USD | 647,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.25` | 1,260,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.26` | 6,780,000.00 USD | 6,780,000.00 USD | 334,900.00 USD | 95,760.00 USD | 281,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 9,330,000.00 USD | 9,330,000.00 USD | 1,530,000.00 USD | 358,870.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.26` | 167,200.00 USD | 179,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.27` | 6,070,000.00 USD | 6,070,000.00 USD | 607,790.00 USD | 199,830.00 USD | 432,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 7,080,000.00 USD | 7,080,000.00 USD | 750,150.00 USD | 213,760.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.28` | 4,960.00 USD | 12,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 4,830,000.00 USD | 4,830,000.00 USD | 315,460.00 USD | 283,680.00 USD | 173,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 4,650,000.00 USD | 4,650,000.00 USD | 834,930.00 USD | 497,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.29` | 7,200.00 USD | 7,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.29` | 4,060,000.00 USD | 4,060,000.00 USD | 246,310.00 USD | 24,960.00 USD | 103,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.30` | 3,680,000.00 USD | 3,680,000.00 USD | 223,190.00 USD | 139,890.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.30` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.31` | 3,300,000.00 USD | 3,300,000.00 USD | 195,160.00 USD | 136,150.00 USD | 314,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.31` | 2,070,000.00 USD | 2,070,000.00 USD | 88,750.00 USD | 0.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.32` | 286.52 USD | 286.52 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 2,650,000.00 USD | 2,650,000.00 USD | 243,570.00 USD | 69,840.00 USD | 193,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 77,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.33` | 2,140,000.00 USD | 2,140,000.00 USD | 214,670.00 USD | 85,110.00 USD | 105,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.33` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 112,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.34` | 1,740,000.00 USD | 1,740,000.00 USD | 147,730.00 USD | 82,560.00 USD | 210,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 137,930.00 USD | 134,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.35` | 1,300,000.00 USD | 1,300,000.00 USD | 64,860.00 USD | 0.00 USD | 105,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 1,480,000.00 USD | 1,480,000.00 USD | 93,250.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.36` | 1,130,000.00 USD | 1,130,000.00 USD | 36,420.00 USD | 34,190.00 USD | 54,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.36` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 39,100.00 USD | 86,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.37` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 18,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.38` | 984,430.00 USD | 984,430.00 USD | 60,040.00 USD | 19,120.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.38` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 93,060.00 USD | 197,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.39` | 856,290.00 USD | 856,290.00 USD | 40,390.00 USD | 151,010.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.39` | 884,480.00 USD | 884,480.00 USD | 0.00 USD | 62,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.40` | 618,760.00 USD | 618,760.00 USD | 65,980.00 USD | 170,160.00 USD | 311,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.40` | 821,630.00 USD | 821,630.00 USD | 0.00 USD | 0.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.41` | 70,760.00 USD | 70,760.00 USD | 0.00 USD | 0.00 USD | 70,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.41` | 421,440.00 USD | 421,440.00 USD | 308,040.00 USD | 0.00 USD | 113,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.42` | 127.47 USD | 127.47 USD | 0.00 USD | 0.00 USD | 59.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.44` | 67.83 USD | 67.83 USD | 0.00 USD | 0.00 USD | 67.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 76,550.00 USD | 76,550.00 USD | 76,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 146,190.00 USD | 146,190.00 USD | 146,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.47` | 110,770.00 USD | 110,770.00 USD | 34,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 280,880.00 USD | 280,880.00 USD | 132,630.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 281,830.00 USD | 281,830.00 USD | 0.00 USD | 0.00 USD | 949.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 113,100.00 USD | 113,100.00 USD | 2,050.00 USD | 0.00 USD | 283.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 525,050.00 USD | 525,050.00 USD | 242,770.00 USD | 0.00 USD | 451.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.50` | 578,570.00 USD | 578,570.00 USD | 316,670.00 USD | 148,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 1,990,000.00 USD | 1,990,000.00 USD | 828,400.00 USD | 640,730.00 USD | 504.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.51` | 1,280,000.00 USD | 1,280,000.00 USD | 457,360.00 USD | 242,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 186,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 2,390,000.00 USD | 2,390,000.00 USD | 552,290.00 USD | 187,770.00 USD | 373,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 3,050,000.00 USD | 3,050,000.00 USD | 361,140.00 USD | 316,520.00 USD | 191,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 933.51 USD | 933.51 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 4,030,000.00 USD | 4,030,000.00 USD | 815,730.00 USD | 85,170.00 USD | 735,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 3,560,000.00 USD | 3,560,000.00 USD | 214,030.00 USD | 60,150.00 USD | 236,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 5,360,000.00 USD | 5,360,000.00 USD | 376,850.00 USD | 262,370.00 USD | 691,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 5,610,000.00 USD | 5,610,000.00 USD | 581,730.00 USD | 367,580.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 269.97 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 6,580,000.00 USD | 6,580,000.00 USD | 653,340.00 USD | 254,800.00 USD | 312,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 6,850,000.00 USD | 6,850,000.00 USD | 989,010.00 USD | 174,120.00 USD | 80,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 4,640.00 USD | 5,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 7,420,000.00 USD | 7,420,000.00 USD | 435,050.00 USD | 148,170.00 USD | 254,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 7,780,000.00 USD | 7,780,000.00 USD | 361,350.00 USD | 307,230.00 USD | 261,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 56,710.00 USD | 62,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 8,300,000.00 USD | 8,300,000.00 USD | 314,580.00 USD | 312,090.00 USD | 253,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 8,150,000.00 USD | 8,150,000.00 USD | 198,050.00 USD | 167,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 9,420,000.00 USD | 9,420,000.00 USD | 249,850.00 USD | 222,910.00 USD | 649,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 8,300,000.00 USD | 8,300,000.00 USD | 47,710.00 USD | 22,490.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 205.41 USD | 62,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 10,460,000.00 USD | 10,460,000.00 USD | 530,370.00 USD | 191,380.00 USD | 319,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 9,830,000.00 USD | 9,830,000.00 USD | 674,410.00 USD | 214,810.00 USD | 637,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 660.76 USD | 63,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 11,160,000.00 USD | 11,160,000.00 USD | 363,790.00 USD | 84,420.00 USD | 247,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 9,950,000.00 USD | 9,950,000.00 USD | 3,460.00 USD | 112,080.00 USD | 968.18 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 12,450.00 USD | 75,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 12,200,000.00 USD | 12,200,000.00 USD | 504,130.00 USD | 131,410.00 USD | 403,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 10,360,000.00 USD | 10,360,000.00 USD | 76,670.00 USD | 181,090.00 USD | 153,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 1,720.00 USD | 77,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 13,100,000.00 USD | 13,100,000.00 USD | 188,210.00 USD | 204,510.00 USD | 516,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 11,190,000.00 USD | 11,190,000.00 USD | 307,400.00 USD | 63,780.00 USD | 459,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 6,710.00 USD | 84,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 14,230,000.00 USD | 14,230,000.00 USD | 483,130.00 USD | 208,050.00 USD | 439,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 11,750,000.00 USD | 11,750,000.00 USD | 226,350.00 USD | 63,200.00 USD | 272,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 7,950.00 USD | 92,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 14,750,000.00 USD | 14,750,000.00 USD | 234,120.00 USD | 263,860.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 12,610,000.00 USD | 12,610,000.00 USD | 513,660.00 USD | 254,400.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 464.50 USD | 92,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 15,270,000.00 USD | 15,270,000.00 USD | 270,310.00 USD | 84,330.00 USD | 164,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 13,460,000.00 USD | 13,460,000.00 USD | 422,980.00 USD | 134,210.00 USD | 288,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 1,510.00 USD | 94,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 15,690,000.00 USD | 15,690,000.00 USD | 147,450.00 USD | 92,980.00 USD | 172,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 13,720,000.00 USD | 13,720,000.00 USD | 156,990.00 USD | 31,420.00 USD | 75,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 6,220.00 USD | 100,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 16,190,000.00 USD | 16,190,000.00 USD | 129,030.00 USD | 103,830.00 USD | 274,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 13,770,000.00 USD | 13,770,000.00 USD | 7,760.00 USD | 0.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 5,690.00 USD | 106,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 16,710,000.00 USD | 16,710,000.00 USD | 287,250.00 USD | 50,360.00 USD | 175,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 14,520,000.00 USD | 14,520,000.00 USD | 381,910.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 153,850.00 USD | 259,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 16,870,000.00 USD | 16,870,000.00 USD | 79,980.00 USD | 0.00 USD | 85,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 14,530,000.00 USD | 14,530,000.00 USD | 2,450.00 USD | 0.00 USD | 339.33 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 104.70 USD | 260,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 16,920,000.00 USD | 16,920,000.00 USD | 5,620.00 USD | 38,510.00 USD | 233.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 14,610,000.00 USD | 14,610,000.00 USD | 2,860.00 USD | 37,250.00 USD | 42,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 26,920.00 USD | 287,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 16,920,000.00 USD | 16,920,000.00 USD | 5,150.00 USD | 0.00 USD | 354.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 14,620,000.00 USD | 14,620,000.00 USD | 9,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 117.40 USD | 287,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.72` | 17,000,000.00 USD | 17,000,000.00 USD | 4,880.00 USD | 19,440.00 USD | 53,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 14,670,000.00 USD | 14,670,000.00 USD | 7,140.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 17,380.00 USD | 304,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 17,080,000.00 USD | 17,080,000.00 USD | 4,080.00 USD | 11,800.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 14,720,000.00 USD | 14,720,000.00 USD | 54,580.00 USD | 0.00 USD | 160.93 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 2,020.00 USD | 306,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 17,480,000.00 USD | 17,480,000.00 USD | 208,070.00 USD | 39,720.00 USD | 154,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 14,790,000.00 USD | 14,790,000.00 USD | 9,090.00 USD | 0.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 124,230.00 USD | 430,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 17,920,000.00 USD | 17,920,000.00 USD | 165,010.00 USD | 93,530.00 USD | 183,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 15,250,000.00 USD | 15,250,000.00 USD | 8,240.00 USD | 108,690.00 USD | 342,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 1,720.00 USD | 432,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.76` | 18,210,000.00 USD | 18,210,000.00 USD | 32,150.00 USD | 27,300.00 USD | 228,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 16,470,000.00 USD | 16,470,000.00 USD | 942,680.00 USD | 0.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 1,180.00 USD | 433,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 18,530,000.00 USD | 18,530,000.00 USD | 109,820.00 USD | 102,010.00 USD | 105,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 17,330,000.00 USD | 17,330,000.00 USD | 731,680.00 USD | 31,590.00 USD | 101,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.78` | 18,760,000.00 USD | 18,760,000.00 USD | 117,090.00 USD | 78,770.00 USD | 38,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 19,010,000.00 USD | 19,010,000.00 USD | 922,010.00 USD | 605,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 475.15 USD | 434,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 19,570,000.00 USD | 19,570,000.00 USD | 473,790.00 USD | 231,110.00 USD | 100,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 19,980,000.00 USD | 19,980,000.00 USD | 713,060.00 USD | 249,310.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 435,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 20,130,000.00 USD | 20,130,000.00 USD | 306,250.00 USD | 220,680.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 21,370,000.00 USD | 21,370,000.00 USD | 1,070,000.00 USD | 315,940.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.80` | 130.22 USD | 435,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.81` | 20,790,000.00 USD | 20,790,000.00 USD | 408,590.00 USD | 120,180.00 USD | 127,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 21,990,000.00 USD | 21,990,000.00 USD | 397,490.00 USD | 125,900.00 USD | 101,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 1,090.00 USD | 436,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 21,710,000.00 USD | 21,710,000.00 USD | 295,730.00 USD | 191,140.00 USD | 433,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 24,680,000.00 USD | 24,680,000.00 USD | 998,780.00 USD | 369,430.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 2,230.00 USD | 438,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 22,400,000.00 USD | 22,400,000.00 USD | 260,840.00 USD | 100,910.00 USD | 330,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 26,320,000.00 USD | 26,320,000.00 USD | 820,240.00 USD | 85,680.00 USD | 739,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 2,820.00 USD | 441,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 22,630,000.00 USD | 22,630,000.00 USD | 76,430.00 USD | 28,910.00 USD | 122,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 26,750,000.00 USD | 26,750,000.00 USD | 97,300.00 USD | 9,680.00 USD | 322,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.85` | 23,180,000.00 USD | 23,180,000.00 USD | 182,320.00 USD | 157,810.00 USD | 210,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 28,740,000.00 USD | 28,740,000.00 USD | 487,940.00 USD | 328,780.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.86` | 23,760,000.00 USD | 23,760,000.00 USD | 214,210.00 USD | 43,740.00 USD | 328,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 30,150,000.00 USD | 30,150,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 9,540.00 USD | 451,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.87` | 24,100,000.00 USD | 24,100,000.00 USD | 202,820.00 USD | 86,180.00 USD | 46,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.87` | 31,210,000.00 USD | 31,210,000.00 USD | 263,700.00 USD | 136,820.00 USD | 663,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 6,700.00 USD | 457,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.88` | 24,410,000.00 USD | 24,410,000.00 USD | 10,810.00 USD | 30,820.00 USD | 265,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 32,870,000.00 USD | 32,870,000.00 USD | 388,550.00 USD | 480,980.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 203,870.00 USD | 661,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.89` | 24,670,000.00 USD | 24,670,000.00 USD | 143,940.00 USD | 46,470.00 USD | 77,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.89` | 33,460,000.00 USD | 33,460,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.90` | 25,260,000.00 USD | 25,260,000.00 USD | 79,980.00 USD | 112,960.00 USD | 391,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 34,590,000.00 USD | 34,590,000.00 USD | 446,650.00 USD | 145,910.00 USD | 541,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.91` | 212,190.00 USD | 874,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.91` | 25,770,000.00 USD | 25,770,000.00 USD | 292,500.00 USD | 85,510.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 36,030,000.00 USD | 36,030,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 894,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.92` | 26,260,000.00 USD | 26,260,000.00 USD | 190,700.00 USD | 89,190.00 USD | 207,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.92` | 37,760,000.00 USD | 37,760,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 15,530.00 USD | 910,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.93` | 26,590,000.00 USD | 26,590,000.00 USD | 118,690.00 USD | 64,250.00 USD | 151,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.93` | 39,320,000.00 USD | 39,320,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 575.42 USD | 910,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.94` | 26,840,000.00 USD | 26,840,000.00 USD | 36,860.00 USD | 65,310.00 USD | 144,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.94` | 40,620,000.00 USD | 40,620,000.00 USD | 351,940.00 USD | 290,290.00 USD | 659,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.95` | 26,970,000.00 USD | 26,970,000.00 USD | 79,890.00 USD | 4,170.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 41,920,000.00 USD | 41,920,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 905.77 USD | 911,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.96` | 27,080,000.00 USD | 27,080,000.00 USD | 69,140.00 USD | 21,750.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.96` | 43,110,000.00 USD | 43,110,000.00 USD | 602,080.00 USD | 214,910.00 USD | 375,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.97` | 27,170,000.00 USD | 27,170,000.00 USD | 5,050.00 USD | 7,520.00 USD | 77,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 43,490,000.00 USD | 43,490,000.00 USD | 194,450.00 USD | 72,330.00 USD | 113,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 118,580.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 44,290,000.00 USD | 44,290,000.00 USD | 436,230.00 USD | 88,580.00 USD | 270,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 1,710.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 44,640,000.00 USD | 44,640,000.00 USD | 127,170.00 USD | 103,060.00 USD | 116,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 1,410.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.00` | 7,110.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.04` | 3,340.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.04` | 2,130.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 182,290.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,710.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 5,620.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 3,760.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.11` | 2,460.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 1,020.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 648.31 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,240.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 317.65 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 28,960.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,810.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 245.29 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 228.84 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 37,450.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 61,910.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 24,290.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.37` | 58,080.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 1,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 113.29 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 5,890.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 179.03 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 3,500.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 3,220.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 334.52 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 88,450.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 39,430.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 2,060.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.55` | 868.25 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 53,380.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 63,790.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 17,680.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 65,640.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.64` | 2,400.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 11,350.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 659,170.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 12,410.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.76` | 199,500.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.78` | 196.93 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 125,810.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 5,470.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 370.62 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 295.43 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 1,240,000.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 23,790.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.93` | 2,850.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 209.86 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.99` | 1,130,000.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.01` | 6,080.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 23,410.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 14,040.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 1,610,000.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 1,540.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,680.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.26` | 352.72 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.29` | 5,060.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 4,100.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 584,470.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.47` | 346,540.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.50` | 146.14 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.53` | 17,950.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 461,930.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 836.25 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.62` | 88,560.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 16,280.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 614.35 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 184,710.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 39,750.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.78` | 8,620.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 538.05 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.83` | 1,920.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 3,410.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 1,870.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 7,400.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.93` | 61,190.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 978.60 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 2,180.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.05` | 1,670.00 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 1,370.00 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 96,610.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 7,510.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 9,680,000.00 USD | 20,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 1,530.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 20,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 7,810,000.00 USD | 28,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 104.09 USD | 28,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 477.97 USD | 28,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 107,860.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 272.47 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 122,230.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 1,500.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,610.00 USD | 29,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.61` | 17,850.00 USD | 29,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 26,630.00 USD | 29,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 112.85 USD | 29,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 29,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.64` | 336.38 USD | 29,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 29,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 868.81 USD | 29,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 807.48 USD | 29,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.78` | 26,740.00 USD | 29,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 3,330.00 USD | 29,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 332,360.00 USD | 29,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.89` | 34,770.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 3,130.00 USD | 29,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 29,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 29,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.13` | 938,520.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.15` | 9,200.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 737,550.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.22` | 103.64 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.23` | 1,220.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.24` | 415,110.00 USD | 32,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.26` | 3,810.00 USD | 32,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.28` | 8,150.00 USD | 32,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 33,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 577.04 USD | 33,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 17,980.00 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.41` | 953.42 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 182.84 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 3,390.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 777.29 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 578.85 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 127.17 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 2,760.00 USD | 33,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.55` | 25,660.00 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.57` | 583.96 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.62` | 2,830.00 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.64` | 1,430.00 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.66` | 949.68 USD | 33,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.68` | 6,260.00 USD | 33,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.72` | 1,880,000.00 USD | 35,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.74` | 451,500.00 USD | 35,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.76` | 16,580.00 USD | 35,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.78` | 1,270.00 USD | 35,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.82` | 2,650.00 USD | 35,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.84` | 19,980.00 USD | 35,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.85` | 6,380.00 USD | 35,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.86` | 4,030.00 USD | 35,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.87` | 5,000.00 USD | 35,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.88` | 1,490,000.00 USD | 37,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8950` | 36,580,000.00 USD | 0.00 USD | 45,150.00 USD | `-79.91%` | `50,448.40` |
| `Live` | `Long` | `0.9050` | 36,530,000.00 USD | 0.00 USD | 11,240.00 USD | `-79.68%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 36,520,000.00 USD | 0.00 USD | 1,880.00 USD | `-79.24%` | `2,031.10` |
| `Live` | `Long` | `0.9350` | 36,520,000.00 USD | 0.00 USD | 5,280,000.00 USD | `-79.01%` | `5,651,256.90` |
| `Live` | `Long` | `1.01` | 31,230,000.00 USD | 0.00 USD | 1,160.00 USD | `-77.22%` | `1,145.20` |
| `Live` | `Long` | `1.02` | 31,230,000.00 USD | 0.00 USD | 40,780.00 USD | `-76.99%` | `39,788.40` |
| `Live` | `Long` | `1.03` | 31,190,000.00 USD | 0.00 USD | 128.55 USD | `-76.77%` | `124.20` |
| `Live` | `Long` | `1.04` | 31,190,000.00 USD | 0.00 USD | 32,220.00 USD | `-76.54%` | `30,836.80` |
| `Live` | `Long` | `1.05` | 31,160,000.00 USD | 0.00 USD | 7,890.00 USD | `-76.32%` | `7,479.20` |
| `Live` | `Long` | `1.06` | 31,150,000.00 USD | 0.00 USD | 1,850.00 USD | `-76.09%` | `1,741.60` |
| `Live` | `Long` | `1.07` | 31,150,000.00 USD | 0.00 USD | 7,730.00 USD | `-75.87%` | `7,189.60` |
| `Live` | `Long` | `1.08` | 31,140,000.00 USD | 0.00 USD | 2,360.00 USD | `-75.64%` | `2,174.60` |
| `Live` | `Long` | `1.09` | 31,140,000.00 USD | 0.00 USD | 73,400.00 USD | `-75.42%` | `67,034.60` |
| `Live` | `Long` | `1.10` | 31,070,000.00 USD | 0.00 USD | 58,550.00 USD | `-75.20%` | `52,985.50` |
| `Live` | `Long` | `1.11` | 31,010,000.00 USD | 0.00 USD | 557.50 USD | `-74.97%` | `500.00` |
| `Live` | `Long` | `1.12` | 31,010,000.00 USD | 0.00 USD | 875.70 USD | `-74.75%` | `778.40` |
| `Live` | `Long` | `1.14` | 31,010,000.00 USD | 0.00 USD | 4,960.00 USD | `-74.52%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 31,000,000.00 USD | 0.00 USD | 52,110.00 USD | `-74.30%` | `45,509.60` |
| `Live` | `Long` | `1.16` | 30,950,000.00 USD | 0.00 USD | 161.82 USD | `-74.07%` | `140.10` |
| `Live` | `Long` | `1.18` | 30,950,000.00 USD | 0.00 USD | 184.59 USD | `-73.62%` | `157.10` |
| `Live` | `Long` | `1.19` | 30,950,000.00 USD | 0.00 USD | 238.19 USD | `-73.40%` | `201.00` |
| `Live` | `Long` | `1.23` | 30,950,000.00 USD | 0.00 USD | 25,760.00 USD | `-72.50%` | `21,030.60` |
| `Live` | `Long` | `1.24` | 30,920,000.00 USD | 0.00 USD | 568.22 USD | `-72.28%` | `460.10` |
| `Live` | `Long` | `1.25` | 30,920,000.00 USD | 0.00 USD | 558.38 USD | `-72.05%` | `448.50` |
| `Live` | `Long` | `1.25` | 30,920,000.00 USD | 0.00 USD | 653.98 USD | `-71.83%` | `521.10` |
| `Live` | `Long` | `1.26` | 30,920,000.00 USD | 0.00 USD | 2,060.00 USD | `-71.60%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 30,920,000.00 USD | 0.00 USD | 449,810.00 USD | `-71.38%` | `352,789.20` |
| `Live` | `Long` | `1.28` | 30,470,000.00 USD | 0.00 USD | 464.78 USD | `-71.15%` | `361.70` |
| `Live` | `Long` | `1.29` | 30,470,000.00 USD | 0.00 USD | 825.82 USD | `-70.93%` | `637.70` |
| `Live` | `Long` | `1.30` | 30,470,000.00 USD | 0.00 USD | 1,340.00 USD | `-70.71%` | `1,024.40` |
| `Live` | `Long` | `1.31` | 30,470,000.00 USD | 0.00 USD | 130.32 USD | `-70.48%` | `99.10` |
| `Live` | `Long` | `1.32` | 30,470,000.00 USD | 0.00 USD | 42,510.00 USD | `-70.26%` | `32,082.40` |
| `Live` | `Long` | `1.33` | 30,420,000.00 USD | 0.00 USD | 1,710.00 USD | `-70.03%` | `1,280.00` |
| `Live` | `Long` | `1.34` | 30,420,000.00 USD | 0.00 USD | 100,010.00 USD | `-69.81%` | `74,358.70` |
| `Live` | `Long` | `1.35` | 30,320,000.00 USD | 0.00 USD | 16,870.00 USD | `-69.58%` | `12,452.40` |
| `Live` | `Long` | `1.36` | 30,300,000.00 USD | 0.00 USD | 461.64 USD | `-69.36%` | `338.20` |
| `Live` | `Long` | `1.38` | 30,300,000.00 USD | 0.00 USD | 12,380.00 USD | `-69.13%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 30,290,000.00 USD | 0.00 USD | 1,510.00 USD | `-68.91%` | `1,093.60` |
| `Live` | `Long` | `1.40` | 30,290,000.00 USD | 0.00 USD | 157.50 USD | `-68.69%` | `112.90` |
| `Live` | `Long` | `1.41` | 30,290,000.00 USD | 0.00 USD | 67,700.00 USD | `-68.46%` | `48,187.70` |
| `Live` | `Long` | `1.43` | 30,220,000.00 USD | 0.00 USD | 40,330.00 USD | `-68.01%` | `28,299.30` |
| `Live` | `Long` | `1.45` | 30,180,000.00 USD | 0.00 USD | 226.29 USD | `-67.56%` | `156.60` |
| `Live` | `Long` | `1.46` | 30,180,000.00 USD | 0.00 USD | 688.80 USD | `-67.34%` | `473.40` |
| `Live` | `Long` | `1.48` | 30,180,000.00 USD | 0.00 USD | 1,480.00 USD | `-66.89%` | `1,000.00` |
| `Live` | `Long` | `1.50` | 30,180,000.00 USD | 0.00 USD | 4,900.00 USD | `-66.22%` | `3,258.80` |
| `Live` | `Long` | `1.51` | 30,170,000.00 USD | 0.00 USD | 9,270.00 USD | `-65.99%` | `6,118.70` |
| `Live` | `Long` | `1.53` | 30,170,000.00 USD | 0.00 USD | 279.37 USD | `-65.54%` | `182.00` |
| `Live` | `Long` | `1.54` | 30,170,000.00 USD | 0.00 USD | 12,200.00 USD | `-65.32%` | `7,895.30` |
| `Live` | `Long` | `1.56` | 30,150,000.00 USD | 0.00 USD | 13,300.00 USD | `-64.87%` | `8,501.00` |
| `Live` | `Long` | `1.57` | 30,140,000.00 USD | 0.00 USD | 589.52 USD | `-64.64%` | `374.30` |
| `Live` | `Long` | `1.58` | 30,140,000.00 USD | 0.00 USD | 4,620.00 USD | `-64.42%` | `2,914.40` |
| `Live` | `Long` | `1.59` | 30,130,000.00 USD | 0.00 USD | 3,380.00 USD | `-64.20%` | `2,119.70` |
| `Live` | `Long` | `1.60` | 30,130,000.00 USD | 0.00 USD | 191.64 USD | `-63.97%` | `119.40` |
| `Live` | `Long` | `1.61` | 30,130,000.00 USD | 0.00 USD | 3,390.00 USD | `-63.75%` | `2,096.20` |
| `Live` | `Long` | `1.64` | 30,130,000.00 USD | 0.00 USD | 2,310.00 USD | `-63.30%` | `1,414.90` |
| `Live` | `Long` | `1.65` | 30,130,000.00 USD | 0.00 USD | 3,210.00 USD | `-63.07%` | `1,950.40` |
| `Live` | `Long` | `1.66` | 30,120,000.00 USD | 0.00 USD | 13,020.00 USD | `-62.85%` | `7,869.30` |
| `Live` | `Long` | `1.67` | 30,110,000.00 USD | 0.00 USD | 2,850.00 USD | `-62.62%` | `1,712.10` |
| `Live` | `Long` | `1.68` | 30,110,000.00 USD | 0.00 USD | 1,060.00 USD | `-62.40%` | `630.10` |
| `Live` | `Long` | `1.69` | 30,100,000.00 USD | 0.00 USD | 16,920.00 USD | `-62.18%` | `10,039.90` |
| `Live` | `Long` | `1.73` | 30,090,000.00 USD | 0.00 USD | 10,000.00 USD | `-61.28%` | `5,797.20` |
| `Live` | `Long` | `1.75` | 30,080,000.00 USD | 0.00 USD | 1,200.00 USD | `-60.83%` | `685.20` |
| `Live` | `Long` | `1.75` | 30,080,000.00 USD | 0.00 USD | 21,990.00 USD | `-60.60%` | `12,531.00` |
| `Live` | `Long` | `1.76` | 30,050,000.00 USD | 0.00 USD | 211.80 USD | `-60.38%` | `120.00` |
| `Live` | `Long` | `1.77` | 30,050,000.00 USD | 0.00 USD | 11,470.00 USD | `-60.16%` | `6,459.40` |
| `Live` | `Long` | `1.78` | 30,040,000.00 USD | 0.00 USD | 1,570.00 USD | `-59.93%` | `878.60` |
| `Live` | `Long` | `1.80` | 30,040,000.00 USD | 0.00 USD | 529.05 USD | `-59.48%` | `293.10` |
| `Live` | `Long` | `1.81` | 30,040,000.00 USD | 0.00 USD | 25,090.00 USD | `-59.26%` | `13,825.00` |
| `Live` | `Long` | `1.82` | 30,020,000.00 USD | 0.00 USD | 59,460.00 USD | `-59.03%` | `32,583.20` |
| `Live` | `Long` | `1.83` | 29,960,000.00 USD | 0.00 USD | 65,820.00 USD | `-58.81%` | `35,867.00` |
| `Live` | `Long` | `1.84` | 29,890,000.00 USD | 0.00 USD | 4,830.00 USD | `-58.58%` | `2,616.60` |
| `Live` | `Long` | `1.85` | 29,890,000.00 USD | 0.00 USD | 4,130.00 USD | `-58.36%` | `2,227.40` |
| `Live` | `Long` | `1.88` | 29,880,000.00 USD | 0.00 USD | 937.50 USD | `-57.91%` | `500.00` |
| `Live` | `Long` | `1.89` | 29,880,000.00 USD | 0.00 USD | 909.51 USD | `-57.69%` | `482.50` |
| `Live` | `Long` | `1.90` | 29,880,000.00 USD | 0.00 USD | 25,520.00 USD | `-57.46%` | `13,465.30` |
| `Live` | `Long` | `1.91` | 29,850,000.00 USD | 0.00 USD | 4,280.00 USD | `-57.24%` | `2,248.00` |
| `Live` | `Long` | `1.92` | 29,850,000.00 USD | 0.00 USD | 8,970.00 USD | `-57.01%` | `4,682.20` |
| `Live` | `Long` | `1.93` | 29,840,000.00 USD | 0.00 USD | 5,080.00 USD | `-56.79%` | `2,637.80` |
| `Live` | `Long` | `1.94` | 29,840,000.00 USD | 0.00 USD | 23,990.00 USD | `-56.56%` | `12,396.70` |
| `Live` | `Long` | `1.95` | 29,810,000.00 USD | 0.00 USD | 41,640.00 USD | `-56.34%` | `21,407.10` |
| `Live` | `Long` | `1.97` | 29,770,000.00 USD | 0.00 USD | 189,050.00 USD | `-55.89%` | `96,209.90` |
| `Live` | `Long` | `1.98` | 29,580,000.00 USD | 0.00 USD | 127,520.00 USD | `-55.67%` | `64,567.50` |
| `Live` | `Long` | `2.00` | 29,450,000.00 USD | 0.00 USD | 1,580.00 USD | `-55.22%` | `790.10` |
| `Live` | `Long` | `2.00` | 29,450,000.00 USD | 0.00 USD | 124,870.00 USD | `-54.99%` | `62,280.10` |
| `Live` | `Long` | `2.02` | 29,330,000.00 USD | 0.00 USD | 260.62 USD | `-54.54%` | `128.70` |
| `Live` | `Long` | `2.04` | 29,330,000.00 USD | 0.00 USD | 41,550.00 USD | `-54.32%` | `20,415.60` |
| `Live` | `Long` | `2.04` | 29,290,000.00 USD | 0.00 USD | 3,810.00 USD | `-54.09%` | `1,863.20` |
| `Live` | `Long` | `2.06` | 29,280,000.00 USD | 0.00 USD | 369.90 USD | `-53.87%` | `180.00` |
| `Live` | `Long` | `2.06` | 29,280,000.00 USD | 0.00 USD | 2,910.00 USD | `-53.65%` | `1,407.20` |
| `Live` | `Long` | `2.08` | 29,280,000.00 USD | 0.00 USD | 299,800.00 USD | `-53.42%` | `144,484.30` |
| `Live` | `Long` | `2.08` | 28,980,000.00 USD | 0.00 USD | 20,990.00 USD | `-53.20%` | `10,065.20` |
| `Live` | `Long` | `2.10` | 28,960,000.00 USD | 0.00 USD | 2,060.00 USD | `-52.97%` | `983.60` |
| `Live` | `Long` | `2.10` | 28,960,000.00 USD | 0.00 USD | 19,450.00 USD | `-52.75%` | `9,241.40` |
| `Live` | `Long` | `2.12` | 28,940,000.00 USD | 0.00 USD | 37,350.00 USD | `-52.52%` | `17,660.70` |
| `Live` | `Long` | `2.12` | 28,900,000.00 USD | 0.00 USD | 30,920.00 USD | `-52.30%` | `14,552.90` |
| `Live` | `Long` | `2.13` | 28,870,000.00 USD | 0.00 USD | 26,150.00 USD | `-52.07%` | `12,250.50` |
| `Live` | `Long` | `2.15` | 28,840,000.00 USD | 0.00 USD | 894.04 USD | `-51.85%` | `416.80` |
| `Live` | `Long` | `2.15` | 28,840,000.00 USD | 0.00 USD | 1,090.00 USD | `-51.63%` | `503.70` |
| `Live` | `Long` | `2.17` | 28,840,000.00 USD | 0.00 USD | 575.02 USD | `-51.40%` | `265.60` |
| `Live` | `Long` | `2.19` | 28,840,000.00 USD | 0.00 USD | 21,610.00 USD | `-50.95%` | `9,889.40` |
| `Live` | `Long` | `2.19` | 28,820,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-50.73%` | `890,412.10` |
| `Live` | `Long` | `2.21` | 26,860,000.00 USD | 0.00 USD | 35,390.00 USD | `-50.50%` | `16,049.50` |
| `Live` | `Long` | `2.23` | 26,830,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.05%` | `722.20` |
| `Live` | `Long` | `2.23` | 26,830,000.00 USD | 0.00 USD | 30,830.00 USD | `-49.83%` | `13,795.80` |
| `Live` | `Long` | `2.25` | 26,800,000.00 USD | 0.00 USD | 115,680.00 USD | `-49.60%` | `51,526.00` |
| `Live` | `Long` | `2.25` | 26,680,000.00 USD | 0.00 USD | 122,830.00 USD | `-49.38%` | `54,468.00` |
| `Live` | `Long` | `2.27` | 26,560,000.00 USD | 0.00 USD | 5,560.00 USD | `-49.16%` | `2,453.00` |
| `Live` | `Long` | `2.27` | 26,550,000.00 USD | 0.00 USD | 3,300.00 USD | `-48.93%` | `1,451.70` |
| `Live` | `Long` | `2.29` | 26,550,000.00 USD | 0.00 USD | 4,930.00 USD | `-48.71%` | `2,159.60` |
| `Live` | `Long` | `2.29` | 26,540,000.00 USD | 0.00 USD | 70,680.00 USD | `-48.48%` | `30,795.70` |
| `Live` | `Long` | `2.31` | 26,470,000.00 USD | 0.00 USD | 5,180.00 USD | `-48.26%` | `2,247.50` |
| `Live` | `Long` | `2.31` | 26,470,000.00 USD | 0.00 USD | 440.31 USD | `-48.03%` | `190.20` |
| `Live` | `Long` | `2.33` | 26,470,000.00 USD | 0.00 USD | 12,050.00 USD | `-47.81%` | `5,181.10` |
| `Live` | `Long` | `2.33` | 26,450,000.00 USD | 0.00 USD | 12,820.00 USD | `-47.58%` | `5,489.00` |
| `Live` | `Long` | `2.35` | 26,440,000.00 USD | 0.00 USD | 70,960.00 USD | `-47.36%` | `30,259.50` |
| `Live` | `Long` | `2.35` | 26,370,000.00 USD | 0.00 USD | 8,720.00 USD | `-47.14%` | `3,700.80` |
| `Live` | `Long` | `2.37` | 26,360,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-46.91%` | `678,989.50` |
| `Live` | `Long` | `2.38` | 24,760,000.00 USD | 0.00 USD | 422,220.00 USD | `-46.69%` | `177,778.50` |
| `Live` | `Long` | `2.38` | 24,330,000.00 USD | 0.00 USD | 652.30 USD | `-46.46%` | `273.50` |
| `Live` | `Long` | `2.40` | 24,330,000.00 USD | 0.00 USD | 143.70 USD | `-46.24%` | `60.00` |
| `Live` | `Long` | `2.40` | 24,330,000.00 USD | 0.00 USD | 11,910.00 USD | `-46.01%` | `4,952.60` |
| `Live` | `Long` | `2.42` | 24,320,000.00 USD | 0.00 USD | 342,760.00 USD | `-45.79%` | `141,929.30` |
| `Live` | `Long` | `2.42` | 23,980,000.00 USD | 0.00 USD | 242.50 USD | `-45.56%` | `100.00` |
| `Live` | `Long` | `2.44` | 23,980,000.00 USD | 0.00 USD | 4,690.00 USD | `-45.34%` | `1,925.50` |
| `Live` | `Long` | `2.46` | 23,970,000.00 USD | 0.00 USD | 1,240.00 USD | `-44.89%` | `504.90` |
| `Live` | `Long` | `2.46` | 23,970,000.00 USD | 0.00 USD | 11,980.00 USD | `-44.67%` | `4,860.50` |
| `Live` | `Long` | `2.48` | 23,960,000.00 USD | 0.00 USD | 654,860.00 USD | `-44.44%` | `264,589.10` |
| `Live` | `Long` | `2.48` | 23,310,000.00 USD | 0.00 USD | 3,610.00 USD | `-44.22%` | `1,452.90` |
| `Live` | `Long` | `2.50` | 23,300,000.00 USD | 0.00 USD | 2,040.00 USD | `-43.99%` | `818.30` |
| `Live` | `Long` | `2.50` | 23,300,000.00 USD | 0.00 USD | 7,490.00 USD | `-43.77%` | `2,989.20` |
| `Live` | `Long` | `2.52` | 23,290,000.00 USD | 0.00 USD | 9,500.00 USD | `-43.32%` | `3,763.10` |
| `Live` | `Long` | `2.54` | 23,280,000.00 USD | 0.00 USD | 395.71 USD | `-43.10%` | `156.10` |
| `Live` | `Long` | `2.54` | 23,280,000.00 USD | 0.00 USD | 105.36 USD | `-42.87%` | `41.40` |
| `Live` | `Long` | `2.56` | 23,280,000.00 USD | 0.00 USD | 1,730.00 USD | `-42.65%` | `678.10` |
| `Live` | `Long` | `2.56` | 23,280,000.00 USD | 0.00 USD | 16,100.00 USD | `-42.42%` | `6,277.60` |
| `Live` | `Long` | `2.58` | 23,260,000.00 USD | 0.00 USD | 1,810.00 USD | `-42.20%` | `701.80` |
| `Live` | `Long` | `2.58` | 23,260,000.00 USD | 0.00 USD | 2,310.00 USD | `-41.97%` | `893.00` |
| `Live` | `Long` | `2.60` | 23,260,000.00 USD | 0.00 USD | 4,030.00 USD | `-41.75%` | `1,553.00` |
| `Live` | `Long` | `2.62` | 23,260,000.00 USD | 0.00 USD | 1,190.00 USD | `-41.30%` | `454.70` |
| `Live` | `Long` | `2.62` | 23,260,000.00 USD | 0.00 USD | 2,910.00 USD | `-41.07%` | `1,106.70` |
| `Live` | `Long` | `2.63` | 23,250,000.00 USD | 0.00 USD | 158,280.00 USD | `-40.85%` | `60,067.60` |
| `Live` | `Long` | `2.65` | 23,090,000.00 USD | 0.00 USD | 3,350.00 USD | `-40.63%` | `1,268.00` |
| `Live` | `Long` | `2.65` | 23,090,000.00 USD | 0.00 USD | 30,530.00 USD | `-40.40%` | `11,499.10` |
| `Live` | `Long` | `2.67` | 23,060,000.00 USD | 0.00 USD | 57,850.00 USD | `-40.18%` | `21,706.70` |
| `Live` | `Long` | `2.67` | 23,000,000.00 USD | 0.00 USD | 7,240.00 USD | `-39.95%` | `2,705.60` |
| `Live` | `Long` | `2.69` | 23,000,000.00 USD | 0.00 USD | 18,980.00 USD | `-39.73%` | `7,068.70` |
| `Live` | `Long` | `2.69` | 22,980,000.00 USD | 0.00 USD | 191,610.00 USD | `-39.50%` | `71,100.00` |
| `Live` | `Long` | `2.71` | 22,780,000.00 USD | 0.00 USD | 189,890.00 USD | `-39.28%` | `70,198.30` |
| `Live` | `Long` | `2.71` | 22,590,000.00 USD | 0.00 USD | 11,750.00 USD | `-39.05%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 22,580,000.00 USD | 0.00 USD | 35,600.00 USD | `-38.83%` | `13,064.00` |
| `Live` | `Long` | `2.73` | 22,550,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.61%` | `1,052.10` |
| `Live` | `Long` | `2.75` | 22,540,000.00 USD | 0.00 USD | 41,410.00 USD | `-38.38%` | `15,084.40` |
| `Live` | `Long` | `2.75` | 22,500,000.00 USD | 0.00 USD | 2,150.00 USD | `-38.16%` | `779.70` |
| `Live` | `Long` | `2.77` | 22,500,000.00 USD | 0.00 USD | 4,980.00 USD | `-37.93%` | `1,800.90` |
| `Live` | `Long` | `2.77` | 22,500,000.00 USD | 0.00 USD | 776,080.00 USD | `-37.71%` | `279,668.70` |
| `Live` | `Long` | `2.79` | 21,720,000.00 USD | 0.00 USD | 30,290.00 USD | `-37.48%` | `10,877.80` |
| `Live` | `Long` | `2.79` | 21,690,000.00 USD | 0.00 USD | 19,380.00 USD | `-37.26%` | `6,933.50` |
| `Live` | `Long` | `2.81` | 21,670,000.00 USD | 0.00 USD | 11,050.00 USD | `-37.03%` | `3,939.40` |
| `Live` | `Long` | `2.81` | 21,660,000.00 USD | 0.00 USD | 207,820.00 USD | `-36.81%` | `73,826.50` |
| `Live` | `Long` | `2.83` | 21,450,000.00 USD | 0.00 USD | 9,140.00 USD | `-36.59%` | `3,234.40` |
| `Live` | `Long` | `2.83` | 21,440,000.00 USD | 0.00 USD | 1,140.00 USD | `-36.36%` | `402.50` |
| `Live` | `Long` | `2.85` | 21,440,000.00 USD | 0.00 USD | 410.82 USD | `-36.14%` | `144.40` |
| `Live` | `Long` | `2.85` | 21,440,000.00 USD | 0.00 USD | 2,560.00 USD | `-35.91%` | `895.00` |
| `Live` | `Long` | `2.87` | 21,440,000.00 USD | 0.00 USD | 13,400.00 USD | `-35.69%` | `4,678.40` |
| `Live` | `Long` | `2.88` | 21,420,000.00 USD | 0.00 USD | 1,330.00 USD | `-35.46%` | `463.30` |
| `Live` | `Long` | `2.88` | 21,420,000.00 USD | 0.00 USD | 19,050.00 USD | `-35.24%` | `6,602.70` |
| `Live` | `Long` | `2.90` | 21,400,000.00 USD | 0.00 USD | 13,910.00 USD | `-35.01%` | `4,804.60` |
| `Live` | `Long` | `2.90` | 21,390,000.00 USD | 0.00 USD | 21,740.00 USD | `-34.79%` | `7,482.10` |
| `Live` | `Long` | `2.92` | 21,370,000.00 USD | 0.00 USD | 3,230.00 USD | `-34.56%` | `1,109.50` |
| `Live` | `Long` | `2.92` | 21,370,000.00 USD | 0.00 USD | 7,310.00 USD | `-34.34%` | `2,500.00` |
| `Live` | `Long` | `2.94` | 21,360,000.00 USD | 0.00 USD | 64,080.00 USD | `-34.12%` | `21,831.40` |
| `Live` | `Long` | `2.96` | 21,290,000.00 USD | 0.00 USD | 171.08 USD | `-33.44%` | `57.70` |
| `Live` | `Long` | `2.98` | 21,290,000.00 USD | 0.00 USD | 12,440.00 USD | `-33.22%` | `4,181.50` |
| `Live` | `Long` | `2.98` | 21,280,000.00 USD | 0.00 USD | 35,190.00 USD | `-32.99%` | `11,787.90` |
| `Live` | `Long` | `3.00` | 21,250,000.00 USD | 0.00 USD | 2,000.00 USD | `-32.77%` | `666.40` |
| `Live` | `Long` | `3.00` | 21,240,000.00 USD | 0.00 USD | 45,300.00 USD | `-32.54%` | `15,074.20` |
| `Live` | `Long` | `3.02` | 21,200,000.00 USD | 0.00 USD | 494,090.00 USD | `-32.32%` | `163,876.30` |
| `Live` | `Long` | `3.02` | 20,700,000.00 USD | 0.00 USD | 15,460.00 USD | `-32.10%` | `5,111.70` |
| `Live` | `Long` | `3.04` | 20,690,000.00 USD | 0.00 USD | 73,850.00 USD | `-31.87%` | `24,332.40` |
| `Live` | `Long` | `3.04` | 20,620,000.00 USD | 0.00 USD | 125,310.00 USD | `-31.65%` | `41,154.00` |
| `Live` | `Long` | `3.06` | 20,490,000.00 USD | 0.00 USD | 44,940.00 USD | `-31.42%` | `14,711.90` |
| `Live` | `Long` | `3.06` | 20,450,000.00 USD | 0.00 USD | 123,540.00 USD | `-31.20%` | `40,305.10` |
| `Live` | `Long` | `3.08` | 20,320,000.00 USD | 0.00 USD | 22,270.00 USD | `-30.97%` | `7,242.60` |
| `Live` | `Long` | `3.08` | 20,300,000.00 USD | 0.00 USD | 13,530.00 USD | `-30.75%` | `4,386.50` |
| `Live` | `Long` | `3.10` | 20,290,000.00 USD | 0.00 USD | 7,450.00 USD | `-30.52%` | `2,408.60` |
| `Live` | `Long` | `3.10` | 20,280,000.00 USD | 0.00 USD | 27,240.00 USD | `-30.30%` | `8,773.40` |
| `Live` | `Long` | `3.12` | 20,250,000.00 USD | 0.00 USD | 151,660.00 USD | `-30.08%` | `48,686.60` |
| `Live` | `Long` | `3.12` | 20,100,000.00 USD | 0.00 USD | 8,940.00 USD | `-29.85%` | `2,861.40` |
| `Live` | `Long` | `3.13` | 20,090,000.00 USD | 0.00 USD | 37,360.00 USD | `-29.63%` | `11,917.80` |
| `Live` | `Long` | `3.15` | 20,050,000.00 USD | 0.00 USD | 56,990.00 USD | `-29.40%` | `18,121.80` |
| `Live` | `Long` | `3.15` | 20,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-29.18%` | `756.80` |
| `Live` | `Long` | `3.17` | 19,990,000.00 USD | 0.00 USD | 28,660.00 USD | `-28.95%` | `9,054.10` |
| `Live` | `Long` | `3.17` | 19,970,000.00 USD | 0.00 USD | 99,120.00 USD | `-28.73%` | `31,220.10` |
| `Live` | `Long` | `3.19` | 19,870,000.00 USD | 0.00 USD | 168,550.00 USD | `-28.50%` | `52,919.30` |
| `Live` | `Long` | `3.19` | 19,700,000.00 USD | 0.00 USD | 6,880.00 USD | `-28.28%` | `2,153.90` |
| `Live` | `Long` | `3.21` | 19,690,000.00 USD | 0.00 USD | 102,670.00 USD | `-28.06%` | `32,035.00` |
| `Live` | `Long` | `3.21` | 19,590,000.00 USD | 0.00 USD | 23,460.00 USD | `-27.83%` | `7,298.50` |
| `Live` | `Long` | `3.23` | 19,560,000.00 USD | 0.00 USD | 23,780.00 USD | `-27.61%` | `7,374.20` |
| `Live` | `Long` | `3.23` | 19,540,000.00 USD | 0.00 USD | 26,750.00 USD | `-27.38%` | `8,270.40` |
| `Live` | `Long` | `3.25` | 19,510,000.00 USD | 0.00 USD | 868,920.00 USD | `-27.16%` | `267,771.30` |
| `Live` | `Long` | `3.25` | 18,650,000.00 USD | 0.00 USD | 476.53 USD | `-26.93%` | `146.40` |
| `Live` | `Long` | `3.27` | 18,640,000.00 USD | 0.00 USD | 48,150.00 USD | `-26.71%` | `14,747.10` |
| `Live` | `Long` | `3.27` | 18,600,000.00 USD | 0.00 USD | 848,500.00 USD | `-26.48%` | `259,082.70` |
| `Live` | `Long` | `3.29` | 17,750,000.00 USD | 0.00 USD | 163,060.00 USD | `-26.26%` | `49,638.80` |
| `Live` | `Long` | `3.29` | 17,580,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-26.03%` | `421,243.60` |
| `Live` | `Long` | `3.31` | 16,200,000.00 USD | 0.00 USD | 57,870.00 USD | `-25.81%` | `17,508.90` |
| `Live` | `Long` | `3.31` | 16,140,000.00 USD | 0.00 USD | 21,100.00 USD | `-25.59%` | `6,365.70` |
| `Live` | `Long` | `3.33` | 16,120,000.00 USD | 0.00 USD | 7,330.00 USD | `-25.36%` | `2,205.10` |
| `Live` | `Long` | `3.33` | 16,110,000.00 USD | 0.00 USD | 53,610.00 USD | `-25.14%` | `16,075.10` |
| `Live` | `Long` | `3.35` | 16,060,000.00 USD | 0.00 USD | 45,290.00 USD | `-24.91%` | `13,540.80` |
| `Live` | `Long` | `3.35` | 16,010,000.00 USD | 0.00 USD | 8,630.00 USD | `-24.69%` | `2,571.00` |
| `Live` | `Long` | `3.37` | 16,000,000.00 USD | 0.00 USD | 4,760.00 USD | `-24.46%` | `1,415.50` |
| `Live` | `Long` | `3.38` | 16,000,000.00 USD | 0.00 USD | 14,490.00 USD | `-24.24%` | `4,293.30` |
| `Live` | `Long` | `3.38` | 15,980,000.00 USD | 0.00 USD | 45,780.00 USD | `-24.01%` | `13,523.20` |
| `Live` | `Long` | `3.40` | 15,940,000.00 USD | 0.00 USD | 3,830.00 USD | `-23.79%` | `1,129.60` |
| `Live` | `Long` | `3.40` | 15,930,000.00 USD | 0.00 USD | 99,440.00 USD | `-23.57%` | `29,205.40` |
| `Live` | `Long` | `3.42` | 15,830,000.00 USD | 0.00 USD | 187,750.00 USD | `-23.34%` | `54,978.40` |
| `Live` | `Long` | `3.42` | 15,650,000.00 USD | 0.00 USD | 6,630.00 USD | `-23.12%` | `1,935.30` |
| `Live` | `Long` | `3.44` | 15,640,000.00 USD | 0.00 USD | 33,900.00 USD | `-22.89%` | `9,868.30` |
| `Live` | `Long` | `3.44` | 15,610,000.00 USD | 0.00 USD | 43,330.00 USD | `-22.67%` | `12,578.40` |
| `Live` | `Long` | `3.46` | 15,560,000.00 USD | 0.00 USD | 158,380.00 USD | `-22.44%` | `45,841.50` |
| `Live` | `Long` | `3.46` | 15,400,000.00 USD | 0.00 USD | 11,280.00 USD | `-22.22%` | `3,255.00` |
| `Live` | `Long` | `3.48` | 15,390,000.00 USD | 0.00 USD | 105,730.00 USD | `-21.99%` | `30,425.30` |
| `Live` | `Long` | `3.48` | 15,290,000.00 USD | 0.00 USD | 13,960.00 USD | `-21.77%` | `4,006.90` |
| `Live` | `Long` | `3.50` | 15,270,000.00 USD | 0.00 USD | 70,420.00 USD | `-21.55%` | `20,148.60` |
| `Live` | `Long` | `3.50` | 15,200,000.00 USD | 0.00 USD | 19,680.00 USD | `-21.32%` | `5,615.80` |
| `Live` | `Long` | `3.52` | 15,180,000.00 USD | 0.00 USD | 22,360.00 USD | `-21.10%` | `6,362.30` |
| `Live` | `Long` | `3.52` | 15,160,000.00 USD | 0.00 USD | 227,660.00 USD | `-20.87%` | `64,583.40` |
| `Live` | `Long` | `3.54` | 14,930,000.00 USD | 0.00 USD | 13,230.00 USD | `-20.65%` | `3,742.70` |
| `Live` | `Long` | `3.54` | 14,920,000.00 USD | 0.00 USD | 338,000.00 USD | `-20.42%` | `95,344.20` |
| `Live` | `Long` | `3.56` | 14,580,000.00 USD | 0.00 USD | 371,970.00 USD | `-20.20%` | `104,631.70` |
| `Live` | `Long` | `3.56` | 14,210,000.00 USD | 0.00 USD | 15,990.00 USD | `-19.97%` | `4,484.00` |
| `Live` | `Long` | `3.58` | 14,190,000.00 USD | 0.00 USD | 116,620.00 USD | `-19.75%` | `32,621.90` |
| `Live` | `Long` | `3.58` | 14,080,000.00 USD | 0.00 USD | 17,180.00 USD | `-19.53%` | `4,792.00` |
| `Live` | `Long` | `3.60` | 14,060,000.00 USD | 0.00 USD | 47,790.00 USD | `-19.30%` | `13,294.10` |
| `Live` | `Long` | `3.60` | 14,010,000.00 USD | 0.00 USD | 10,850.00 USD | `-19.08%` | `3,009.20` |
| `Live` | `Long` | `3.62` | 14,000,000.00 USD | 0.00 USD | 845.19 USD | `-18.85%` | `233.80` |
| `Live` | `Long` | `3.62` | 14,000,000.00 USD | 0.00 USD | 76,190.00 USD | `-18.63%` | `21,017.70` |
| `Live` | `Long` | `3.63` | 13,930,000.00 USD | 0.00 USD | 53,270.00 USD | `-18.40%` | `14,653.90` |
| `Live` | `Long` | `3.65` | 13,870,000.00 USD | 0.00 USD | 67,270.00 USD | `-18.18%` | `18,454.90` |
| `Live` | `Long` | `3.65` | 13,800,000.00 USD | 0.00 USD | 52,620.00 USD | `-17.95%` | `14,396.60` |
| `Live` | `Long` | `3.67` | 13,750,000.00 USD | 0.00 USD | 510,060.00 USD | `-17.73%` | `139,170.50` |
| `Live` | `Long` | `3.67` | 13,240,000.00 USD | 0.00 USD | 191,730.00 USD | `-17.50%` | `52,170.70` |
| `Live` | `Long` | `3.69` | 13,050,000.00 USD | 0.00 USD | 226,010.00 USD | `-17.28%` | `61,332.30` |
| `Live` | `Long` | `3.69` | 12,820,000.00 USD | 0.00 USD | 6,200.00 USD | `-17.06%` | `1,678.70` |
| `Live` | `Long` | `3.71` | 12,820,000.00 USD | 0.00 USD | 33,200.00 USD | `-16.83%` | `8,961.90` |
| `Live` | `Long` | `3.71` | 12,780,000.00 USD | 0.00 USD | 77,580.00 USD | `-16.61%` | `20,881.70` |
| `Live` | `Long` | `3.73` | 12,710,000.00 USD | 0.00 USD | 22,200.00 USD | `-16.38%` | `5,959.40` |
| `Live` | `Long` | `3.73` | 12,680,000.00 USD | 0.00 USD | 8,970.00 USD | `-16.16%` | `2,401.70` |
| `Live` | `Long` | `3.75` | 12,680,000.00 USD | 0.00 USD | 139,060.00 USD | `-15.93%` | `37,131.80` |
| `Live` | `Long` | `3.75` | 12,540,000.00 USD | 0.00 USD | 162,760.00 USD | `-15.71%` | `43,345.70` |
| `Live` | `Long` | `3.77` | 12,370,000.00 USD | 0.00 USD | 92,970.00 USD | `-15.48%` | `24,694.20` |
| `Live` | `Long` | `3.77` | 12,280,000.00 USD | 0.00 USD | 23,300.00 USD | `-15.26%` | `6,171.00` |
| `Live` | `Long` | `3.79` | 12,260,000.00 USD | 0.00 USD | 46,690.00 USD | `-15.04%` | `12,335.70` |
| `Live` | `Long` | `3.79` | 12,210,000.00 USD | 0.00 USD | 136,080.00 USD | `-14.81%` | `35,858.80` |
| `Live` | `Long` | `3.81` | 12,080,000.00 USD | 0.00 USD | 16,990.00 USD | `-14.59%` | `4,464.60` |
| `Live` | `Long` | `3.81` | 12,060,000.00 USD | 0.00 USD | 68,990.00 USD | `-14.36%` | `18,084.30` |
| `Live` | `Long` | `3.83` | 11,990,000.00 USD | 0.00 USD | 20,520.00 USD | `-14.14%` | `5,365.10` |
| `Live` | `Long` | `3.83` | 11,970,000.00 USD | 0.00 USD | 174,170.00 USD | `-13.91%` | `45,416.60` |
| `Live` | `Long` | `3.85` | 11,790,000.00 USD | 0.00 USD | 27,390.00 USD | `-13.69%` | `7,122.90` |
| `Live` | `Long` | `3.85` | 11,770,000.00 USD | 0.00 USD | 32,230.00 USD | `-13.46%` | `8,360.60` |
| `Live` | `Long` | `3.87` | 11,730,000.00 USD | 0.00 USD | 20,990.00 USD | `-13.24%` | `5,430.40` |
| `Live` | `Long` | `3.88` | 11,710,000.00 USD | 0.00 USD | 4,040.00 USD | `-13.02%` | `1,042.30` |
| `Live` | `Long` | `3.88` | 11,710,000.00 USD | 0.00 USD | 29,390.00 USD | `-12.79%` | `7,564.70` |
| `Live` | `Long` | `3.90` | 11,680,000.00 USD | 0.00 USD | 95,980.00 USD | `-12.57%` | `24,641.30` |
| `Live` | `Long` | `3.90` | 11,580,000.00 USD | 0.00 USD | 567,610.00 USD | `-12.34%` | `145,355.40` |
| `Live` | `Long` | `3.92` | 11,020,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-12.12%` | `1,000,937.40` |
| `Live` | `Long` | `3.92` | 7,100,000.00 USD | 0.00 USD | 198,930.00 USD | `-11.89%` | `50,683.20` |
| `Live` | `Long` | `3.94` | 6,900,000.00 USD | 0.00 USD | 17,860.00 USD | `-11.67%` | `4,538.90` |
| `Live` | `Long` | `3.94` | 6,880,000.00 USD | 0.00 USD | 551,430.00 USD | `-11.44%` | `139,779.70` |
| `Live` | `Long` | `3.96` | 6,330,000.00 USD | 0.00 USD | 170,710.00 USD | `-11.22%` | `43,162.10` |
| `Live` | `Long` | `3.96` | 6,160,000.00 USD | 0.00 USD | 126,910.00 USD | `-10.99%` | `32,007.10` |
| `Live` | `Long` | `3.98` | 6,030,000.00 USD | 0.00 USD | 43,490.00 USD | `-10.77%` | `10,940.90` |
| `Live` | `Long` | `3.98` | 5,990,000.00 USD | 0.00 USD | 67,030.00 USD | `-10.55%` | `16,821.00` |
| `Live` | `Long` | `4.00` | 5,920,000.00 USD | 0.00 USD | 36,180.00 USD | `-10.32%` | `9,055.90` |
| `Live` | `Long` | `4.00` | 5,890,000.00 USD | 0.00 USD | 57,060.00 USD | `-10.10%` | `14,248.10` |
| `Live` | `Long` | `4.01` | 5,830,000.00 USD | 0.00 USD | 62,150.00 USD | `-9.87%` | `15,479.80` |
| `Live` | `Long` | `4.03` | 5,770,000.00 USD | 0.00 USD | 141,530.00 USD | `-9.65%` | `35,162.90` |
| `Live` | `Long` | `4.04` | 5,620,000.00 USD | 0.00 USD | 15,430.00 USD | `-9.42%` | `3,824.20` |
| `Live` | `Long` | `4.04` | 5,610,000.00 USD | 0.00 USD | 64,110.00 USD | `-9.20%` | `15,848.10` |
| `Live` | `Long` | `4.05` | 5,550,000.00 USD | 0.00 USD | 223,930.00 USD | `-8.97%` | `55,223.90` |
| `Live` | `Long` | `4.07` | 5,320,000.00 USD | 0.00 USD | 362,220.00 USD | `-8.75%` | `89,106.90` |
| `Live` | `Long` | `4.08` | 4,960,000.00 USD | 0.00 USD | 359,690.00 USD | `-8.53%` | `88,267.50` |
| `Live` | `Long` | `4.08` | 4,600,000.00 USD | 0.00 USD | 740,450.00 USD | `-8.30%` | `181,260.70` |
| `Live` | `Long` | `4.09` | 3,860,000.00 USD | 0.00 USD | 45,110.00 USD | `-8.08%` | `11,016.80` |
| `Live` | `Long` | `4.11` | 3,810,000.00 USD | 0.00 USD | 482,190.00 USD | `-7.85%` | `117,463.90` |
| `Live` | `Long` | `4.12` | 3,330,000.00 USD | 0.00 USD | 368,940.00 USD | `-7.63%` | `89,657.30` |
| `Live` | `Long` | `4.12` | 2,960,000.00 USD | 0.00 USD | 54,610.00 USD | `-7.40%` | `13,238.50` |
| `Live` | `Long` | `4.13` | 2,910,000.00 USD | 0.00 USD | 84,130.00 USD | `-7.18%` | `20,346.70` |
| `Live` | `Long` | `4.14` | 2,820,000.00 USD | 0.00 USD | 133,280.00 USD | `-6.95%` | `32,154.50` |
| `Live` | `Long` | `4.16` | 2,690,000.00 USD | 0.00 USD | 61,340.00 USD | `-6.73%` | `14,762.40` |
| `Live` | `Long` | `4.17` | 2,630,000.00 USD | 0.00 USD | 220,090.00 USD | `-6.51%` | `52,843.60` |
| `Live` | `Long` | `4.17` | 2,410,000.00 USD | 0.00 USD | 23,690.00 USD | `-6.28%` | `5,674.60` |
| `Live` | `Long` | `4.18` | 2,390,000.00 USD | 0.00 USD | 71,370.00 USD | `-6.06%` | `17,053.20` |
| `Live` | `Long` | `4.20` | 2,310,000.00 USD | 0.00 USD | 359,880.00 USD | `-5.83%` | `85,787.10` |
| `Live` | `Long` | `4.21` | 1,950,000.00 USD | 0.00 USD | 207,470.00 USD | `-5.61%` | `49,338.50` |
| `Live` | `Long` | `4.21` | 1,750,000.00 USD | 0.00 USD | 159,020.00 USD | `-5.38%` | `37,727.50` |
| `Live` | `Long` | `4.22` | 1,590,000.00 USD | 0.00 USD | 46,270.00 USD | `-5.16%` | `10,950.40` |
| `Live` | `Long` | `4.24` | 1,540,000.00 USD | 0.00 USD | 70,770.00 USD | `-4.93%` | `16,710.20` |
| `Live` | `Long` | `4.25` | 1,470,000.00 USD | 0.00 USD | 27,920.00 USD | `-4.71%` | `6,576.60` |
| `Live` | `Long` | `4.25` | 1,440,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-4.49%` | `296,887.50` |
| `Live` | `Long` | `4.26` | 179,650.00 USD | 0.00 USD | 167,200.00 USD | `-4.26%` | `39,203.00` |
| `Live` | `Long` | `4.28` | 12,450.00 USD | 0.00 USD | 4,960.00 USD | `-4.04%` | `1,160.60` |
| `Live` | `Long` | `4.29` | 7,490.00 USD | 0.00 USD | 7,200.00 USD | `-3.81%` | `1,681.30` |
| `Live` | `Long` | `4.32` | 286.52 USD | 0.00 USD | 286.52 USD | `-3.14%` | `66.40` |
| `Live` | `Short` | `4.53` | 933.51 USD | 933.51 USD | 0.00 USD | `+1.58%` | `206.30` |
| `Live` | `Short` | `4.54` | 1,200.00 USD | 269.97 USD | 0.00 USD | `+2.02%` | `59.40` |
| `Live` | `Short` | `4.55` | 5,850.00 USD | 4,640.00 USD | 0.00 USD | `+2.25%` | `1,019.70` |
| `Live` | `Short` | `4.57` | 62,560.00 USD | 56,710.00 USD | 0.00 USD | `+2.47%` | `12,423.20` |
| `Live` | `Short` | `4.58` | 62,770.00 USD | 205.41 USD | 0.00 USD | `+2.92%` | `44.80` |
| `Live` | `Short` | `4.59` | 63,430.00 USD | 660.76 USD | 0.00 USD | `+3.15%` | `143.80` |
| `Live` | `Short` | `4.61` | 75,870.00 USD | 12,450.00 USD | 0.00 USD | `+3.37%` | `2,702.90` |
| `Live` | `Short` | `4.62` | 77,600.00 USD | 1,720.00 USD | 0.00 USD | `+3.60%` | `373.60` |
| `Live` | `Short` | `4.62` | 84,310.00 USD | 6,710.00 USD | 0.00 USD | `+3.82%` | `1,451.40` |
| `Live` | `Short` | `4.63` | 92,260.00 USD | 7,950.00 USD | 0.00 USD | `+4.05%` | `1,714.60` |
| `Live` | `Short` | `4.64` | 92,720.00 USD | 464.50 USD | 0.00 USD | `+4.27%` | `100.00` |
| `Live` | `Short` | `4.66` | 94,240.00 USD | 1,510.00 USD | 0.00 USD | `+4.49%` | `325.20` |
| `Live` | `Short` | `4.67` | 100,460.00 USD | 6,220.00 USD | 0.00 USD | `+4.72%` | `1,333.40` |
| `Live` | `Short` | `4.67` | 106,150.00 USD | 5,690.00 USD | 0.00 USD | `+4.94%` | `1,217.40` |
| `Live` | `Short` | `4.68` | 259,990.00 USD | 153,850.00 USD | 0.00 USD | `+5.17%` | `32,838.00` |
| `Live` | `Short` | `4.70` | 260,100.00 USD | 104.70 USD | 0.00 USD | `+5.39%` | `22.30` |
| `Live` | `Short` | `4.71` | 287,020.00 USD | 26,920.00 USD | 0.00 USD | `+5.62%` | `5,721.60` |
| `Live` | `Short` | `4.71` | 287,140.00 USD | 117.40 USD | 0.00 USD | `+5.84%` | `24.90` |
| `Live` | `Short` | `4.72` | 304,510.00 USD | 17,380.00 USD | 0.00 USD | `+6.07%` | `3,677.90` |
| `Live` | `Short` | `4.74` | 306,530.00 USD | 2,020.00 USD | 0.00 USD | `+6.29%` | `426.40` |
| `Live` | `Short` | `4.75` | 430,760.00 USD | 124,230.00 USD | 0.00 USD | `+6.51%` | `26,181.70` |
| `Live` | `Short` | `4.75` | 432,490.00 USD | 1,720.00 USD | 0.00 USD | `+6.74%` | `362.40` |
| `Live` | `Short` | `4.76` | 433,670.00 USD | 1,180.00 USD | 0.00 USD | `+6.96%` | `248.30` |
| `Live` | `Short` | `4.79` | 434,150.00 USD | 475.15 USD | 0.00 USD | `+7.41%` | `99.30` |
| `Live` | `Short` | `4.79` | 435,480.00 USD | 1,330.00 USD | 0.00 USD | `+7.64%` | `277.70` |
| `Live` | `Short` | `4.80` | 435,610.00 USD | 130.22 USD | 0.00 USD | `+7.86%` | `27.10` |
| `Live` | `Short` | `4.82` | 436,700.00 USD | 1,090.00 USD | 0.00 USD | `+8.09%` | `226.10` |
| `Live` | `Short` | `4.83` | 438,920.00 USD | 2,230.00 USD | 0.00 USD | `+8.31%` | `461.60` |
| `Live` | `Short` | `4.83` | 441,740.00 USD | 2,820.00 USD | 0.00 USD | `+8.53%` | `582.60` |
| `Live` | `Short` | `4.87` | 451,280.00 USD | 9,540.00 USD | 0.00 USD | `+9.21%` | `1,960.70` |
| `Live` | `Short` | `4.88` | 457,980.00 USD | 6,700.00 USD | 0.00 USD | `+9.43%` | `1,374.60` |
| `Live` | `Short` | `4.88` | 661,860.00 USD | 203,870.00 USD | 0.00 USD | `+9.66%` | `41,734.90` |
| `Live` | `Short` | `4.91` | 874,040.00 USD | 212,190.00 USD | 0.00 USD | `+10.11%` | `43,259.10` |
| `Live` | `Short` | `4.92` | 894,760.00 USD | 20,720.00 USD | 0.00 USD | `+10.33%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 910,290.00 USD | 15,530.00 USD | 0.00 USD | `+10.55%` | `3,153.50` |
| `Live` | `Short` | `4.93` | 910,860.00 USD | 575.42 USD | 0.00 USD | `+10.78%` | `116.60` |
| `Live` | `Short` | `4.96` | 911,770.00 USD | 905.77 USD | 0.00 USD | `+11.23%` | `182.80` |
| `Live` | `Short` | `4.97` | 1,030,000.00 USD | 118,580.00 USD | 0.00 USD | `+11.68%` | `23,834.70` |
| `Live` | `Short` | `4.99` | 1,030,000.00 USD | 1,710.00 USD | 0.00 USD | `+11.90%` | `343.70` |
| `Live` | `Short` | `5.00` | 1,030,000.00 USD | 1,410.00 USD | 0.00 USD | `+12.13%` | `282.50` |
| `Live` | `Short` | `5.00` | 1,040,000.00 USD | 7,110.00 USD | 0.00 USD | `+12.35%` | `1,421.50` |
| `Live` | `Short` | `5.04` | 1,040,000.00 USD | 3,340.00 USD | 0.00 USD | `+13.02%` | `663.30` |
| `Live` | `Short` | `5.04` | 1,050,000.00 USD | 2,130.00 USD | 0.00 USD | `+13.25%` | `422.00` |
| `Live` | `Short` | `5.05` | 1,230,000.00 USD | 182,290.00 USD | 0.00 USD | `+13.47%` | `36,061.50` |
| `Live` | `Short` | `5.07` | 1,230,000.00 USD | 3,710.00 USD | 0.00 USD | `+13.70%` | `732.20` |
| `Live` | `Short` | `5.08` | 1,240,000.00 USD | 5,620.00 USD | 0.00 USD | `+13.92%` | `1,108.10` |
| `Live` | `Short` | `5.08` | 1,240,000.00 USD | 3,760.00 USD | 0.00 USD | `+14.15%` | `740.30` |
| `Live` | `Short` | `5.11` | 1,240,000.00 USD | 2,460.00 USD | 0.00 USD | `+14.60%` | `481.40` |
| `Live` | `Short` | `5.12` | 1,240,000.00 USD | 1,020.00 USD | 0.00 USD | `+14.82%` | `200.00` |
| `Live` | `Short` | `5.12` | 1,250,000.00 USD | 648.31 USD | 0.00 USD | `+15.04%` | `126.50` |
| `Live` | `Short` | `5.13` | 1,250,000.00 USD | 1,240.00 USD | 0.00 USD | `+15.27%` | `241.30` |
| `Live` | `Short` | `5.17` | 1,250,000.00 USD | 317.65 USD | 0.00 USD | `+15.94%` | `61.50` |
| `Live` | `Short` | `5.21` | 2,150,000.00 USD | 898,120.00 USD | 0.00 USD | `+16.84%` | `172,549.20` |
| `Live` | `Short` | `5.22` | 2,220,000.00 USD | 72,110.00 USD | 0.00 USD | `+17.29%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 2,250,000.00 USD | 28,960.00 USD | 0.00 USD | `+17.74%` | `5,520.80` |
| `Live` | `Short` | `5.25` | 2,250,000.00 USD | 288.50 USD | 0.00 USD | `+17.96%` | `54.90` |
| `Live` | `Short` | `5.26` | 2,250,000.00 USD | 5,810.00 USD | 0.00 USD | `+18.19%` | `1,103.40` |
| `Live` | `Short` | `5.28` | 2,250,000.00 USD | 245.29 USD | 0.00 USD | `+18.41%` | `46.50` |
| `Live` | `Short` | `5.29` | 2,250,000.00 USD | 228.84 USD | 0.00 USD | `+18.64%` | `43.30` |
| `Live` | `Short` | `5.29` | 2,290,000.00 USD | 37,450.00 USD | 0.00 USD | `+18.86%` | `7,072.30` |
| `Live` | `Short` | `5.30` | 2,290,000.00 USD | 524.66 USD | 0.00 USD | `+19.09%` | `98.90` |
| `Live` | `Short` | `5.34` | 2,350,000.00 USD | 61,910.00 USD | 0.00 USD | `+19.98%` | `11,582.30` |
| `Live` | `Short` | `5.36` | 2,380,000.00 USD | 24,290.00 USD | 0.00 USD | `+20.21%` | `4,536.10` |
| `Live` | `Short` | `5.37` | 2,440,000.00 USD | 58,080.00 USD | 0.00 USD | `+20.43%` | `10,826.30` |
| `Live` | `Short` | `5.38` | 2,440,000.00 USD | 1,000.00 USD | 0.00 USD | `+20.66%` | `186.60` |
| `Live` | `Short` | `5.39` | 2,440,000.00 USD | 113.29 USD | 0.00 USD | `+21.11%` | `21.00` |
| `Live` | `Short` | `5.42` | 2,440,000.00 USD | 5,890.00 USD | 0.00 USD | `+21.55%` | `1,087.60` |
| `Live` | `Short` | `5.42` | 2,440,000.00 USD | 179.03 USD | 0.00 USD | `+21.78%` | `33.00` |
| `Live` | `Short` | `5.43` | 2,440,000.00 USD | 962.54 USD | 0.00 USD | `+22.00%` | `177.10` |
| `Live` | `Short` | `5.46` | 2,450,000.00 USD | 3,500.00 USD | 0.00 USD | `+22.45%` | `641.20` |
| `Live` | `Short` | `5.46` | 2,450,000.00 USD | 3,220.00 USD | 0.00 USD | `+22.68%` | `588.70` |
| `Live` | `Short` | `5.47` | 2,450,000.00 USD | 334.52 USD | 0.00 USD | `+22.90%` | `61.10` |
| `Live` | `Short` | `5.50` | 2,540,000.00 USD | 88,450.00 USD | 0.00 USD | `+23.35%` | `16,097.30` |
| `Live` | `Short` | `5.51` | 2,580,000.00 USD | 39,430.00 USD | 0.00 USD | `+23.80%` | `7,150.20` |
| `Live` | `Short` | `5.53` | 2,580,000.00 USD | 2,060.00 USD | 0.00 USD | `+24.02%` | `372.40` |
| `Live` | `Short` | `5.54` | 2,580,000.00 USD | 209.22 USD | 0.00 USD | `+24.25%` | `37.80` |
| `Live` | `Short` | `5.55` | 2,580,000.00 USD | 868.25 USD | 0.00 USD | `+24.70%` | `156.30` |
| `Live` | `Short` | `5.57` | 2,590,000.00 USD | 8,670.00 USD | 0.00 USD | `+24.92%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 2,640,000.00 USD | 53,380.00 USD | 0.00 USD | `+25.15%` | `9,574.70` |
| `Live` | `Short` | `5.58` | 2,710,000.00 USD | 63,790.00 USD | 0.00 USD | `+25.37%` | `11,421.90` |
| `Live` | `Short` | `5.59` | 2,710,000.00 USD | 686.51 USD | 0.00 USD | `+25.59%` | `122.70` |
| `Live` | `Short` | `5.61` | 2,730,000.00 USD | 17,680.00 USD | 0.00 USD | `+25.82%` | `3,153.90` |
| `Live` | `Short` | `5.62` | 2,790,000.00 USD | 65,640.00 USD | 0.00 USD | `+26.27%` | `11,670.20` |
| `Live` | `Short` | `5.64` | 2,790,000.00 USD | 2,400.00 USD | 0.00 USD | `+26.72%` | `425.90` |
| `Live` | `Short` | `5.67` | 2,800,000.00 USD | 11,350.00 USD | 0.00 USD | `+27.17%` | `2,002.70` |
| `Live` | `Short` | `5.67` | 2,810,000.00 USD | 228.70 USD | 0.00 USD | `+27.39%` | `40.30` |
| `Live` | `Short` | `5.68` | 3,460,000.00 USD | 659,170.00 USD | 0.00 USD | `+27.62%` | `115,949.40` |
| `Live` | `Short` | `5.70` | 3,480,000.00 USD | 12,410.00 USD | 0.00 USD | `+27.84%` | `2,179.00` |
| `Live` | `Short` | `5.71` | 3,480,000.00 USD | 2,130.00 USD | 0.00 USD | `+28.29%` | `372.40` |
| `Live` | `Short` | `5.75` | 3,480,000.00 USD | 4,580.00 USD | 0.00 USD | `+28.96%` | `796.90` |
| `Live` | `Short` | `5.75` | 3,480,000.00 USD | 286.02 USD | 0.00 USD | `+29.19%` | `49.70` |
| `Live` | `Short` | `5.76` | 3,680,000.00 USD | 199,500.00 USD | 0.00 USD | `+29.41%` | `34,605.30` |
| `Live` | `Short` | `5.78` | 3,680,000.00 USD | 196.93 USD | 0.00 USD | `+29.64%` | `34.10` |
| `Live` | `Short` | `5.83` | 3,810,000.00 USD | 125,810.00 USD | 0.00 USD | `+30.98%` | `21,560.70` |
| `Live` | `Short` | `5.84` | 3,810,000.00 USD | 5,470.00 USD | 0.00 USD | `+31.21%` | `935.10` |
| `Live` | `Short` | `5.86` | 3,820,000.00 USD | 370.62 USD | 0.00 USD | `+31.43%` | `63.30` |
| `Live` | `Short` | `5.88` | 3,820,000.00 USD | 295.43 USD | 0.00 USD | `+32.10%` | `50.20` |
| `Live` | `Short` | `5.89` | 5,050,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+32.33%` | `210,027.60` |
| `Live` | `Short` | `5.91` | 5,080,000.00 USD | 23,790.00 USD | 0.00 USD | `+32.55%` | `4,028.30` |
| `Live` | `Short` | `5.92` | 5,080,000.00 USD | 189.28 USD | 0.00 USD | `+32.78%` | `32.00` |
| `Live` | `Short` | `5.93` | 5,080,000.00 USD | 2,850.00 USD | 0.00 USD | `+33.23%` | `479.70` |
| `Live` | `Short` | `5.95` | 5,080,000.00 USD | 209.86 USD | 0.00 USD | `+33.45%` | `35.30` |
| `Live` | `Short` | `5.99` | 6,210,000.00 USD | 1,130,000.00 USD | 0.00 USD | `+34.35%` | `188,022.00` |
| `Live` | `Short` | `6.01` | 6,210,000.00 USD | 6,080.00 USD | 0.00 USD | `+35.02%` | `1,010.60` |
| `Live` | `Short` | `6.04` | 6,240,000.00 USD | 23,410.00 USD | 0.00 USD | `+35.47%` | `3,878.40` |
| `Live` | `Short` | `6.07` | 6,240,000.00 USD | 740.54 USD | 0.00 USD | `+36.15%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,240,000.00 USD | 5,920.00 USD | 0.00 USD | `+36.59%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,280,000.00 USD | 37,510.00 USD | 0.00 USD | `+36.82%` | `6,154.10` |
| `Live` | `Short` | `6.11` | 6,290,000.00 USD | 14,040.00 USD | 0.00 USD | `+37.04%` | `2,300.10` |
| `Live` | `Short` | `6.13` | 6,300,000.00 USD | 2,430.00 USD | 0.00 USD | `+37.72%` | `396.10` |
| `Live` | `Short` | `6.18` | 7,910,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+38.84%` | `260,227.90` |
| `Live` | `Short` | `6.24` | 7,910,000.00 USD | 1,540.00 USD | 0.00 USD | `+39.96%` | `247.30` |
| `Live` | `Short` | `6.25` | 7,910,000.00 USD | 7,680.00 USD | 0.00 USD | `+40.19%` | `1,230.10` |
| `Live` | `Short` | `6.25` | 7,920,000.00 USD | 439.10 USD | 0.00 USD | `+40.41%` | `70.20` |
| `Live` | `Short` | `6.26` | 7,920,000.00 USD | 352.72 USD | 0.00 USD | `+40.63%` | `56.30` |
| `Live` | `Short` | `6.29` | 7,920,000.00 USD | 5,060.00 USD | 0.00 USD | `+41.31%` | `803.80` |
| `Live` | `Short` | `6.32` | 7,920,000.00 USD | 310.70 USD | 0.00 USD | `+41.76%` | `49.20` |
| `Live` | `Short` | `6.33` | 7,920,000.00 USD | 382.00 USD | 0.00 USD | `+42.21%` | `60.30` |
| `Live` | `Short` | `6.34` | 7,920,000.00 USD | 214.46 USD | 0.00 USD | `+42.43%` | `33.80` |
| `Live` | `Short` | `6.37` | 7,920,000.00 USD | 113.93 USD | 0.00 USD | `+42.88%` | `17.90` |
| `Live` | `Short` | `6.38` | 7,920,000.00 USD | 288.15 USD | 0.00 USD | `+43.10%` | `45.20` |
| `Live` | `Short` | `6.38` | 7,920,000.00 USD | 2,000.00 USD | 0.00 USD | `+43.33%` | `312.80` |
| `Live` | `Short` | `6.41` | 7,930,000.00 USD | 4,100.00 USD | 0.00 USD | `+43.78%` | `640.10` |
| `Live` | `Short` | `6.42` | 7,930,000.00 USD | 943.65 USD | 0.00 USD | `+44.00%` | `147.10` |
| `Live` | `Short` | `6.42` | 7,930,000.00 USD | 346.95 USD | 0.00 USD | `+44.23%` | `54.00` |
| `Live` | `Short` | `6.43` | 8,510,000.00 USD | 584,470.00 USD | 0.00 USD | `+44.45%` | `90,827.50` |
| `Live` | `Short` | `6.45` | 8,520,000.00 USD | 5,270.00 USD | 0.00 USD | `+44.68%` | `818.40` |
| `Live` | `Short` | `6.46` | 8,530,000.00 USD | 7,150.00 USD | 0.00 USD | `+44.90%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 8,530,000.00 USD | 1,940.00 USD | 0.00 USD | `+45.12%` | `300.00` |
| `Live` | `Short` | `6.47` | 8,870,000.00 USD | 346,540.00 USD | 0.00 USD | `+45.35%` | `53,520.30` |
| `Live` | `Short` | `6.50` | 8,870,000.00 USD | 146.14 USD | 0.00 USD | `+45.80%` | `22.50` |
| `Live` | `Short` | `6.51` | 8,880,000.00 USD | 380.48 USD | 0.00 USD | `+46.25%` | `58.40` |
| `Live` | `Short` | `6.53` | 8,890,000.00 USD | 17,950.00 USD | 0.00 USD | `+46.47%` | `2,751.50` |
| `Live` | `Short` | `6.54` | 8,890,000.00 USD | 265.07 USD | 0.00 USD | `+46.92%` | `40.50` |
| `Live` | `Short` | `6.58` | 9,360,000.00 USD | 461,930.00 USD | 0.00 USD | `+47.82%` | `70,149.50` |
| `Live` | `Short` | `6.59` | 9,360,000.00 USD | 836.25 USD | 0.00 USD | `+48.04%` | `126.80` |
| `Live` | `Short` | `6.62` | 9,440,000.00 USD | 88,560.00 USD | 0.00 USD | `+48.72%` | `13,367.10` |
| `Live` | `Short` | `6.66` | 9,450,000.00 USD | 7,230.00 USD | 0.00 USD | `+49.39%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 9,470,000.00 USD | 16,280.00 USD | 0.00 USD | `+49.61%` | `2,443.30` |
| `Live` | `Short` | `6.67` | 9,470,000.00 USD | 200.25 USD | 0.00 USD | `+49.84%` | `30.00` |
| `Live` | `Short` | `6.68` | 9,470,000.00 USD | 614.35 USD | 0.00 USD | `+50.06%` | `91.90` |
| `Live` | `Short` | `6.71` | 9,650,000.00 USD | 184,710.00 USD | 0.00 USD | `+50.51%` | `27,548.10` |
| `Live` | `Short` | `6.71` | 9,690,000.00 USD | 39,750.00 USD | 0.00 USD | `+50.74%` | `5,920.00` |
| `Live` | `Short` | `6.72` | 9,810,000.00 USD | 115,670.00 USD | 0.00 USD | `+50.96%` | `17,200.00` |
| `Live` | `Short` | `6.75` | 11,060,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+51.63%` | `184,501.00` |
| `Live` | `Short` | `6.78` | 11,060,000.00 USD | 8,620.00 USD | 0.00 USD | `+52.08%` | `1,272.00` |
| `Live` | `Short` | `6.79` | 11,060,000.00 USD | 538.05 USD | 0.00 USD | `+52.31%` | `79.30` |
| `Live` | `Short` | `6.83` | 11,070,000.00 USD | 1,920.00 USD | 0.00 USD | `+53.43%` | `280.50` |
| `Live` | `Short` | `6.87` | 11,070,000.00 USD | 3,410.00 USD | 0.00 USD | `+54.10%` | `496.20` |
| `Live` | `Short` | `6.92` | 11,070,000.00 USD | 1,870.00 USD | 0.00 USD | `+55.23%` | `270.60` |
| `Live` | `Short` | `6.92` | 11,080,000.00 USD | 7,400.00 USD | 0.00 USD | `+55.45%` | `1,069.30` |
| `Live` | `Short` | `6.93` | 11,140,000.00 USD | 61,190.00 USD | 0.00 USD | `+55.67%` | `8,823.60` |
| `Live` | `Short` | `6.99` | 11,140,000.00 USD | 978.60 USD | 0.00 USD | `+56.80%` | `140.10` |
| `Live` | `Short` | `7.03` | 11,140,000.00 USD | 2,180.00 USD | 0.00 USD | `+57.70%` | `310.00` |
| `Live` | `Short` | `7.05` | 11,150,000.00 USD | 1,670.00 USD | 0.00 USD | `+58.37%` | `237.00` |
| `Live` | `Short` | `7.08` | 11,150,000.00 USD | 1,370.00 USD | 0.00 USD | `+59.04%` | `193.30` |
| `Live` | `Short` | `7.12` | 11,240,000.00 USD | 96,610.00 USD | 0.00 USD | `+59.72%` | `13,578.50` |
| `Live` | `Short` | `7.21` | 11,260,000.00 USD | 13,560.00 USD | 0.00 USD | `+61.96%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 11,260,000.00 USD | 7,510.00 USD | 0.00 USD | `+62.41%` | `1,038.50` |
| `Live` | `Short` | `7.25` | 20,940,000.00 USD | 9,680,000.00 USD | 0.00 USD | `+62.63%` | `1,336,000.00` |
| `Live` | `Short` | `7.32` | 20,950,000.00 USD | 1,530.00 USD | 0.00 USD | `+64.20%` | `209.70` |
| `Live` | `Short` | `7.33` | 20,950,000.00 USD | 1,320.00 USD | 0.00 USD | `+64.65%` | `180.00` |
| `Live` | `Short` | `7.38` | 28,760,000.00 USD | 7,810,000.00 USD | 0.00 USD | `+65.78%` | `1,058,172.40` |
| `Live` | `Short` | `7.43` | 28,760,000.00 USD | 104.09 USD | 0.00 USD | `+66.90%` | `14.00` |
| `Live` | `Short` | `7.45` | 28,760,000.00 USD | 477.97 USD | 0.00 USD | `+67.12%` | `64.20` |
| `Live` | `Short` | `7.46` | 28,870,000.00 USD | 107,860.00 USD | 0.00 USD | `+67.35%` | `14,467.60` |
| `Live` | `Short` | `7.46` | 28,870,000.00 USD | 272.47 USD | 0.00 USD | `+67.57%` | `36.50` |
| `Live` | `Short` | `7.47` | 28,990,000.00 USD | 122,230.00 USD | 0.00 USD | `+67.80%` | `16,351.90` |
| `Live` | `Short` | `7.50` | 28,990,000.00 USD | 1,500.00 USD | 0.00 USD | `+68.47%` | `200.00` |
| `Live` | `Short` | `7.53` | 29,000,000.00 USD | 1,610.00 USD | 0.00 USD | `+68.92%` | `214.00` |
| `Live` | `Short` | `7.61` | 29,010,000.00 USD | 17,850.00 USD | 0.00 USD | `+70.71%` | `2,347.20` |
| `Live` | `Short` | `7.62` | 29,040,000.00 USD | 26,630.00 USD | 0.00 USD | `+70.94%` | `3,496.50` |
| `Live` | `Short` | `7.62` | 29,040,000.00 USD | 112.85 USD | 0.00 USD | `+71.16%` | `14.80` |
| `Live` | `Short` | `7.63` | 29,060,000.00 USD | 19,210.00 USD | 0.00 USD | `+71.39%` | `2,516.10` |
| `Live` | `Short` | `7.64` | 29,060,000.00 USD | 336.38 USD | 0.00 USD | `+71.61%` | `44.00` |
| `Live` | `Short` | `7.67` | 29,060,000.00 USD | 360.25 USD | 0.00 USD | `+72.06%` | `47.00` |
| `Live` | `Short` | `7.67` | 29,060,000.00 USD | 868.81 USD | 0.00 USD | `+72.29%` | `113.20` |
| `Live` | `Short` | `7.71` | 29,060,000.00 USD | 807.48 USD | 0.00 USD | `+72.96%` | `104.80` |
| `Live` | `Short` | `7.78` | 29,090,000.00 USD | 26,740.00 USD | 0.00 USD | `+74.53%` | `3,438.80` |
| `Live` | `Short` | `7.87` | 29,090,000.00 USD | 3,330.00 USD | 0.00 USD | `+76.55%` | `423.10` |
| `Live` | `Short` | `7.88` | 29,420,000.00 USD | 332,360.00 USD | 0.00 USD | `+77.00%` | `42,151.20` |
| `Live` | `Short` | `7.89` | 29,460,000.00 USD | 34,770.00 USD | 0.00 USD | `+77.22%` | `4,404.40` |
| `Live` | `Short` | `7.92` | 29,460,000.00 USD | 3,130.00 USD | 0.00 USD | `+77.90%` | `394.70` |
| `Live` | `Short` | `7.95` | 29,470,000.00 USD | 6,120.00 USD | 0.00 USD | `+78.35%` | `769.80` |
| `Live` | `Short` | `7.96` | 29,600,000.00 USD | 134,240.00 USD | 0.00 USD | `+78.80%` | `16,854.30` |
| `Live` | `Short` | `8.03` | 30,040,000.00 USD | 435,420.00 USD | 0.00 USD | `+80.14%` | `54,257.40` |
| `Live` | `Short` | `8.06` | 30,040,000.00 USD | 797.63 USD | 0.00 USD | `+81.04%` | `98.90` |
| `Live` | `Short` | `8.13` | 30,980,000.00 USD | 938,520.00 USD | 0.00 USD | `+82.61%` | `115,368.10` |
| `Live` | `Short` | `8.15` | 30,990,000.00 USD | 9,200.00 USD | 0.00 USD | `+83.06%` | `1,128.40` |
| `Live` | `Short` | `8.20` | 31,720,000.00 USD | 737,550.00 USD | 0.00 USD | `+83.96%` | `90,000.00` |
| `Live` | `Short` | `8.22` | 31,720,000.00 USD | 103.64 USD | 0.00 USD | `+84.63%` | `12.60` |
| `Live` | `Short` | `8.23` | 31,720,000.00 USD | 1,220.00 USD | 0.00 USD | `+84.86%` | `148.00` |
| `Live` | `Short` | `8.24` | 32,140,000.00 USD | 415,110.00 USD | 0.00 USD | `+85.08%` | `50,346.40` |
| `Live` | `Short` | `8.26` | 32,140,000.00 USD | 3,810.00 USD | 0.00 USD | `+85.31%` | `461.40` |
| `Live` | `Short` | `8.28` | 32,150,000.00 USD | 8,150.00 USD | 0.00 USD | `+85.75%` | `984.60` |
| `Live` | `Short` | `8.37` | 33,250,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+87.77%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 33,250,000.00 USD | 577.04 USD | 0.00 USD | `+88.00%` | `68.90` |
| `Live` | `Short` | `8.38` | 33,270,000.00 USD | 17,980.00 USD | 0.00 USD | `+88.22%` | `2,144.60` |
| `Live` | `Short` | `8.41` | 33,270,000.00 USD | 953.42 USD | 0.00 USD | `+88.90%` | `113.30` |
| `Live` | `Short` | `8.46` | 33,270,000.00 USD | 182.84 USD | 0.00 USD | `+90.02%` | `21.60` |
| `Live` | `Short` | `8.48` | 33,280,000.00 USD | 3,390.00 USD | 0.00 USD | `+90.47%` | `400.00` |
| `Live` | `Short` | `8.49` | 33,280,000.00 USD | 777.29 USD | 0.00 USD | `+90.69%` | `91.50` |
| `Live` | `Short` | `8.53` | 33,280,000.00 USD | 578.85 USD | 0.00 USD | `+91.37%` | `67.90` |
| `Live` | `Short` | `8.54` | 33,280,000.00 USD | 127.17 USD | 0.00 USD | `+91.59%` | `14.90` |
| `Live` | `Short` | `8.54` | 33,280,000.00 USD | 2,760.00 USD | 0.00 USD | `+91.82%` | `323.50` |
| `Live` | `Short` | `8.55` | 33,310,000.00 USD | 25,660.00 USD | 0.00 USD | `+92.04%` | `3,000.00` |
| `Live` | `Short` | `8.57` | 33,310,000.00 USD | 583.96 USD | 0.00 USD | `+92.49%` | `68.10` |
| `Live` | `Short` | `8.62` | 33,310,000.00 USD | 2,830.00 USD | 0.00 USD | `+93.61%` | `328.40` |
| `Live` | `Short` | `8.64` | 33,310,000.00 USD | 1,430.00 USD | 0.00 USD | `+94.06%` | `165.80` |
| `Live` | `Short` | `8.66` | 33,310,000.00 USD | 949.68 USD | 0.00 USD | `+94.51%` | `109.60` |
| `Live` | `Short` | `8.68` | 33,320,000.00 USD | 6,260.00 USD | 0.00 USD | `+94.73%` | `721.10` |
| `Live` | `Short` | `8.72` | 35,200,000.00 USD | 1,880,000.00 USD | 0.00 USD | `+95.86%` | `215,956.10` |
| `Live` | `Short` | `8.74` | 35,650,000.00 USD | 451,500.00 USD | 0.00 USD | `+96.31%` | `51,630.00` |
| `Live` | `Short` | `8.76` | 35,670,000.00 USD | 16,580.00 USD | 0.00 USD | `+96.53%` | `1,894.30` |
| `Live` | `Short` | `8.78` | 35,670,000.00 USD | 1,270.00 USD | 0.00 USD | `+96.98%` | `145.00` |
| `Live` | `Short` | `8.82` | 35,670,000.00 USD | 2,650.00 USD | 0.00 USD | `+98.10%` | `300.00` |
| `Live` | `Short` | `8.84` | 35,690,000.00 USD | 19,980.00 USD | 0.00 USD | `+98.33%` | `2,261.80` |
| `Live` | `Short` | `8.85` | 35,700,000.00 USD | 6,380.00 USD | 0.00 USD | `+98.55%` | `721.60` |
| `Live` | `Short` | `8.86` | 35,700,000.00 USD | 4,030.00 USD | 0.00 USD | `+98.77%` | `454.60` |
| `Live` | `Short` | `8.87` | 35,710,000.00 USD | 5,000.00 USD | 0.00 USD | `+99.00%` | `564.00` |
| `Live` | `Short` | `8.88` | 37,200,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+99.45%` | `168,122.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 4,670,000.00 USD | 0.00 USD | 717.17 USD | `-77.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 4,660,000.00 USD | 0.00 USD | 345.25 USD | `-69.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 4,660,000.00 USD | 0.00 USD | 5,640.00 USD | `-69.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 4,660,000.00 USD | 0.00 USD | 997.29 USD | `-68.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 4,660,000.00 USD | 0.00 USD | 139.83 USD | `-65.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 4,660,000.00 USD | 0.00 USD | 113.28 USD | `-65.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 4,660,000.00 USD | 0.00 USD | 4,000.00 USD | `-65.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 4,650,000.00 USD | 0.00 USD | 324.22 USD | `-65.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 4,650,000.00 USD | 0.00 USD | 4,590.00 USD | `-64.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 4,650,000.00 USD | 0.00 USD | 739.67 USD | `-63.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 4,650,000.00 USD | 0.00 USD | 1,740.00 USD | `-63.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 4,650,000.00 USD | 0.00 USD | 669.02 USD | `-61.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 4,650,000.00 USD | 0.00 USD | 105.88 USD | `-61.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 4,650,000.00 USD | 0.00 USD | 172.50 USD | `-61.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 4,640,000.00 USD | 0.00 USD | 10,650.00 USD | `-60.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 4,630,000.00 USD | 0.00 USD | 722.00 USD | `-59.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 4,630,000.00 USD | 0.00 USD | 259.00 USD | `-59.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 4,630,000.00 USD | 0.00 USD | 103.84 USD | `-59.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 4,630,000.00 USD | 0.00 USD | 109.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 4,630,000.00 USD | 0.00 USD | 222.19 USD | `-57.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 4,630,000.00 USD | 0.00 USD | 10,280.00 USD | `-57.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 4,620,000.00 USD | 0.00 USD | 558.36 USD | `-57.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 4,620,000.00 USD | 0.00 USD | 1,520.00 USD | `-56.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 4,620,000.00 USD | 0.00 USD | 222.14 USD | `-56.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 4,620,000.00 USD | 0.00 USD | 279.50 USD | `-56.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 4,620,000.00 USD | 0.00 USD | 197.50 USD | `-55.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,620,000.00 USD | 0.00 USD | 935.66 USD | `-55.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 4,620,000.00 USD | 0.00 USD | 18,860.00 USD | `-54.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 4,600,000.00 USD | 0.00 USD | 3,020.00 USD | `-54.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 4,600,000.00 USD | 0.00 USD | 214.52 USD | `-54.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-53.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 4,600,000.00 USD | 0.00 USD | 578.41 USD | `-53.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,590,000.00 USD | 0.00 USD | 18,070.00 USD | `-52.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 4,580,000.00 USD | 0.00 USD | 13,980.00 USD | `-52.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,560,000.00 USD | 0.00 USD | 107.23 USD | `-52.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 4,560,000.00 USD | 0.00 USD | 1,590.00 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,560,000.00 USD | 0.00 USD | 6,970.00 USD | `-51.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 4,550,000.00 USD | 0.00 USD | 310.32 USD | `-51.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 4,550,000.00 USD | 0.00 USD | 1,170.00 USD | `-51.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,550,000.00 USD | 0.00 USD | 576.18 USD | `-50.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 4,550,000.00 USD | 0.00 USD | 295.67 USD | `-50.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,550,000.00 USD | 0.00 USD | 2,940.00 USD | `-50.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 4,550,000.00 USD | 0.00 USD | 812.68 USD | `-50.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,550,000.00 USD | 0.00 USD | 1,440.00 USD | `-50.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 4,550,000.00 USD | 0.00 USD | 490.14 USD | `-49.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,550,000.00 USD | 0.00 USD | 13,490.00 USD | `-49.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 4,530,000.00 USD | 0.00 USD | 478.06 USD | `-49.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,530,000.00 USD | 0.00 USD | 540.88 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 4,530,000.00 USD | 0.00 USD | 1,210.00 USD | `-48.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,530,000.00 USD | 0.00 USD | 759.76 USD | `-48.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 4,530,000.00 USD | 0.00 USD | 15,550.00 USD | `-48.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 4,510,000.00 USD | 0.00 USD | 12,970.00 USD | `-48.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,500,000.00 USD | 0.00 USD | 3,050.00 USD | `-47.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 4,500,000.00 USD | 0.00 USD | 467.00 USD | `-47.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 4,500,000.00 USD | 0.00 USD | 506.75 USD | `-47.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 4,500,000.00 USD | 0.00 USD | 214.27 USD | `-46.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,500,000.00 USD | 0.00 USD | 428.69 USD | `-46.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 4,500,000.00 USD | 0.00 USD | 322.45 USD | `-46.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,500,000.00 USD | 0.00 USD | 108.25 USD | `-46.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 4,500,000.00 USD | 0.00 USD | 3,850.00 USD | `-46.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 4,490,000.00 USD | 0.00 USD | 799.04 USD | `-45.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,490,000.00 USD | 0.00 USD | 6,830.00 USD | `-45.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 4,480,000.00 USD | 0.00 USD | 137.16 USD | `-45.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,480,000.00 USD | 0.00 USD | 504.41 USD | `-44.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 4,480,000.00 USD | 0.00 USD | 963.93 USD | `-44.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 4,480,000.00 USD | 0.00 USD | 13,880.00 USD | `-43.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 4,470,000.00 USD | 0.00 USD | 541.98 USD | `-43.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,470,000.00 USD | 0.00 USD | 108.75 USD | `-43.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 4,470,000.00 USD | 0.00 USD | 766.55 USD | `-42.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 4,470,000.00 USD | 0.00 USD | 1,010.00 USD | `-42.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,470,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 4,470,000.00 USD | 0.00 USD | 100.04 USD | `-41.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 4,470,000.00 USD | 0.00 USD | 5,090.00 USD | `-41.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 4,460,000.00 USD | 0.00 USD | 226.57 USD | `-39.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,460,000.00 USD | 0.00 USD | 104.98 USD | `-39.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 4,460,000.00 USD | 0.00 USD | 329.33 USD | `-39.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 4,460,000.00 USD | 0.00 USD | 7,160.00 USD | `-39.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 4,450,000.00 USD | 0.00 USD | 107.21 USD | `-38.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,450,000.00 USD | 0.00 USD | 197.37 USD | `-38.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 4,450,000.00 USD | 0.00 USD | 8,390.00 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,440,000.00 USD | 0.00 USD | 108.39 USD | `-37.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 4,440,000.00 USD | 0.00 USD | 1,270.00 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,440,000.00 USD | 0.00 USD | 14,140.00 USD | `-37.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 4,430,000.00 USD | 0.00 USD | 437.98 USD | `-37.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 4,430,000.00 USD | 0.00 USD | 2,000.00 USD | `-37.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 4,430,000.00 USD | 0.00 USD | 9,790.00 USD | `-36.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 4,420,000.00 USD | 0.00 USD | 109.53 USD | `-36.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.87` | 4,420,000.00 USD | 0.00 USD | 1,810.00 USD | `-35.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,410,000.00 USD | 0.00 USD | 437.00 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 4,410,000.00 USD | 0.00 USD | 746.06 USD | `-35.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 4,410,000.00 USD | 0.00 USD | 4,870.00 USD | `-34.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,410,000.00 USD | 0.00 USD | 696.98 USD | `-34.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 4,410,000.00 USD | 0.00 USD | 358.90 USD | `-34.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 4,410,000.00 USD | 0.00 USD | 15,370.00 USD | `-33.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 4,390,000.00 USD | 0.00 USD | 523.32 USD | `-33.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 4,390,000.00 USD | 0.00 USD | 2,330.00 USD | `-33.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 4,390,000.00 USD | 0.00 USD | 16,110.00 USD | `-32.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,370,000.00 USD | 0.00 USD | 1,020.00 USD | `-32.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 4,370,000.00 USD | 0.00 USD | 345.76 USD | `-32.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 4,370,000.00 USD | 0.00 USD | 214.57 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 4,370,000.00 USD | 0.00 USD | 109.42 USD | `-31.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 4,370,000.00 USD | 0.00 USD | 721.58 USD | `-30.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 4,370,000.00 USD | 0.00 USD | 9,300.00 USD | `-30.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 4,360,000.00 USD | 0.00 USD | 8,700.00 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 4,350,000.00 USD | 0.00 USD | 315.69 USD | `-29.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,350,000.00 USD | 0.00 USD | 214.17 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 4,350,000.00 USD | 0.00 USD | 641.10 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,350,000.00 USD | 0.00 USD | 212.06 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 4,350,000.00 USD | 0.00 USD | 1,030.00 USD | `-28.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 4,350,000.00 USD | 0.00 USD | 218.81 USD | `-28.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,350,000.00 USD | 0.00 USD | 31,570.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 4,320,000.00 USD | 0.00 USD | 144.67 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 4,320,000.00 USD | 0.00 USD | 21,850.00 USD | `-27.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 4,300,000.00 USD | 0.00 USD | 1,990.00 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 4,290,000.00 USD | 0.00 USD | 642.55 USD | `-26.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,290,000.00 USD | 0.00 USD | 1,150.00 USD | `-26.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 4,290,000.00 USD | 0.00 USD | 1,070.00 USD | `-26.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,290,000.00 USD | 0.00 USD | 17,330.00 USD | `-25.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 4,270,000.00 USD | 0.00 USD | 240.67 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,270,000.00 USD | 0.00 USD | 306.56 USD | `-25.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 4,270,000.00 USD | 0.00 USD | 1,670.00 USD | `-25.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 4,270,000.00 USD | 0.00 USD | 505.76 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 4,270,000.00 USD | 0.00 USD | 73,220.00 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 4,200,000.00 USD | 0.00 USD | 129,640.00 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,070,000.00 USD | 0.00 USD | 8,490.00 USD | `-23.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 4,060,000.00 USD | 0.00 USD | 3,320.00 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 4,060,000.00 USD | 0.00 USD | 25,250.00 USD | `-23.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 4,030,000.00 USD | 0.00 USD | 506.22 USD | `-23.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 4,030,000.00 USD | 0.00 USD | 103.05 USD | `-22.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 4,030,000.00 USD | 0.00 USD | 2,550.00 USD | `-22.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 4,030,000.00 USD | 0.00 USD | 1,380.00 USD | `-22.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 4,030,000.00 USD | 0.00 USD | 77,350.00 USD | `-22.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 3,950,000.00 USD | 0.00 USD | 112,400.00 USD | `-21.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 3,840,000.00 USD | 0.00 USD | 17,360.00 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,820,000.00 USD | 0.00 USD | 2,030.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 3,820,000.00 USD | 0.00 USD | 12,040.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,810,000.00 USD | 0.00 USD | 633.50 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 3,800,000.00 USD | 0.00 USD | 333.68 USD | `-19.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,800,000.00 USD | 0.00 USD | 72,860.00 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 3,730,000.00 USD | 0.00 USD | 179.25 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,730,000.00 USD | 0.00 USD | 643.50 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 3,730,000.00 USD | 0.00 USD | 4,330.00 USD | `-19.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,730,000.00 USD | 0.00 USD | 632.99 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 3,730,000.00 USD | 0.00 USD | 172.19 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 3,730,000.00 USD | 0.00 USD | 13,400.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,710,000.00 USD | 0.00 USD | 1,260.00 USD | `-18.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 3,710,000.00 USD | 0.00 USD | 3,900.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,710,000.00 USD | 0.00 USD | 174.09 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 3,710,000.00 USD | 0.00 USD | 367.50 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,710,000.00 USD | 0.00 USD | 9,210.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 3,700,000.00 USD | 0.00 USD | 6,080.00 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,690,000.00 USD | 0.00 USD | 17,930.00 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 3,670,000.00 USD | 0.00 USD | 1,440.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,670,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 3,670,000.00 USD | 0.00 USD | 48,440.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 3,620,000.00 USD | 0.00 USD | 18,790.00 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,600,000.00 USD | 0.00 USD | 7,640.00 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 3,600,000.00 USD | 0.00 USD | 3,940.00 USD | `-15.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,590,000.00 USD | 0.00 USD | 189,250.00 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 3,400,000.00 USD | 0.00 USD | 1,900.00 USD | `-14.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,400,000.00 USD | 0.00 USD | 5,270.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 3,400,000.00 USD | 0.00 USD | 18,070.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,380,000.00 USD | 0.00 USD | 23,770.00 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 3,350,000.00 USD | 0.00 USD | 2,240.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,350,000.00 USD | 0.00 USD | 537.92 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 3,350,000.00 USD | 0.00 USD | 3,070.00 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 3,350,000.00 USD | 0.00 USD | 2,460.00 USD | `-13.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,350,000.00 USD | 0.00 USD | 5,550.00 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 3,340,000.00 USD | 0.00 USD | 7,320.00 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,330,000.00 USD | 0.00 USD | 1,310.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 3,330,000.00 USD | 0.00 USD | 38,930.00 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,290,000.00 USD | 0.00 USD | 2,950.00 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 3,290,000.00 USD | 0.00 USD | 1,120.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,290,000.00 USD | 0.00 USD | 1,420.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 3,290,000.00 USD | 0.00 USD | 358.60 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,290,000.00 USD | 0.00 USD | 13,970.00 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 3,270,000.00 USD | 0.00 USD | 301,690.00 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,970,000.00 USD | 0.00 USD | 4,980.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 2,970,000.00 USD | 0.00 USD | 3,950.00 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,960,000.00 USD | 0.00 USD | 513.36 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 2,960,000.00 USD | 0.00 USD | 288,590.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 2,670,000.00 USD | 0.00 USD | 6,140.00 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 2,670,000.00 USD | 0.00 USD | 4,510.00 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,660,000.00 USD | 0.00 USD | 2,350.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 2,660,000.00 USD | 0.00 USD | 6,050.00 USD | `-9.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 2,650,000.00 USD | 0.00 USD | 93,640.00 USD | `-8.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 2,560,000.00 USD | 0.00 USD | 1,140.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,560,000.00 USD | 0.00 USD | 504,780.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 2,050,000.00 USD | 0.00 USD | 74,690.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 1,980,000.00 USD | 0.00 USD | 1,250.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 1,980,000.00 USD | 0.00 USD | 29,060.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,950,000.00 USD | 0.00 USD | 11,340.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 1,940,000.00 USD | 0.00 USD | 10,440.00 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 1,930,000.00 USD | 0.00 USD | 352,210.00 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 1,580,000.00 USD | 0.00 USD | 1,910.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,570,000.00 USD | 0.00 USD | 57,670.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,520,000.00 USD | 0.00 USD | 4,330.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 1,510,000.00 USD | 0.00 USD | 28,150.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 1,480,000.00 USD | 0.00 USD | 45,890.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 1,440,000.00 USD | 0.00 USD | 32,130.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,410,000.00 USD | 0.00 USD | 151,190.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 1,250,000.00 USD | 0.00 USD | 104,510.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 1,150,000.00 USD | 0.00 USD | 131,520.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 1,020,000.00 USD | 0.00 USD | 84,770.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 933,300.00 USD | 0.00 USD | 30,740.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 902,560.00 USD | 0.00 USD | 60,800.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 841,760.00 USD | 0.00 USD | 8,270.00 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 833,490.00 USD | 0.00 USD | 278,330.00 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 555,160.00 USD | 0.00 USD | 62,800.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 492,350.00 USD | 0.00 USD | 26,550.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 465,800.00 USD | 0.00 USD | 5,230.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 460,570.00 USD | 0.00 USD | 2,910.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 457,660.00 USD | 0.00 USD | 5,730.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 451,930.00 USD | 0.00 USD | 58,330.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 393,600.00 USD | 0.00 USD | 112,970.00 USD | `-2.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.36` | 280,620.00 USD | 0.00 USD | 23,920.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.37` | 256,700.00 USD | 0.00 USD | 49,650.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 207,060.00 USD | 0.00 USD | 46,980.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.38` | 160,070.00 USD | 0.00 USD | 15,030.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.39` | 145,050.00 USD | 0.00 USD | 36,050.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.41` | 109,000.00 USD | 0.00 USD | 92,860.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 16,140.00 USD | 0.00 USD | 2,540.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.42` | 13,600.00 USD | 0.00 USD | 8,050.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.43` | 5,550.00 USD | 0.00 USD | 102.45 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.45` | 5,450.00 USD | 0.00 USD | 5,450.00 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 91,430.00 USD | 91,430.00 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 94,850.00 USD | 3,410.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 98,140.00 USD | 3,300.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 98,480.00 USD | 334.13 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 99,910.00 USD | 1,440.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 100,260.00 USD | 347.79 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 106,770.00 USD | 6,510.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 108,020.00 USD | 1,250.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 108,880.00 USD | 854.85 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 112,670.00 USD | 3,790.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 128,900.00 USD | 16,230.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 299,350.00 USD | 170,450.00 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 305,990.00 USD | 6,640.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 457,680.00 USD | 151,690.00 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 460,420.00 USD | 2,740.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 527,150.00 USD | 66,730.00 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 527,570.00 USD | 419.04 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 598,180.00 USD | 70,600.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 598,620.00 USD | 447.28 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 605,730.00 USD | 7,100.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 718,470.00 USD | 112,740.00 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 723,470.00 USD | 5,010.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 726,110.00 USD | 2,640.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 734,320.00 USD | 8,200.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 734,610.00 USD | 294.85 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,200,000.00 USD | 469,830.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,210,000.00 USD | 3,750.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,220,000.00 USD | 7,550.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,320,000.00 USD | 100,820.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,350,000.00 USD | 34,400.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,390,000.00 USD | 40,230.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,430,000.00 USD | 38,000.00 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,440,000.00 USD | 10,110.00 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 1,440,000.00 USD | 1,700.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 1,500,000.00 USD | 55,300.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 1,520,000.00 USD | 25,900.00 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,310,000.00 USD | 790,860.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,320,000.00 USD | 11,840.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,330,000.00 USD | 1,790.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 2,330,000.00 USD | 927.82 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 2,370,000.00 USD | 38,860.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 2,380,000.00 USD | 11,620.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,410,000.00 USD | 32,370.00 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 2,590,000.00 USD | 181,440.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 2,600,000.00 USD | 4,060.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 2,720,000.00 USD | 126,730.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,730,000.00 USD | 5,460.00 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 2,770,000.00 USD | 41,100.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 2,780,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 2,780,000.00 USD | 114.72 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 2,780,000.00 USD | 6,580.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 2,790,000.00 USD | 2,350.00 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 2,790,000.00 USD | 562.17 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 2,880,000.00 USD | 93,310.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 2,900,000.00 USD | 18,960.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,030,000.00 USD | 134,660.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,060,000.00 USD | 26,480.00 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,070,000.00 USD | 5,250.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,160,000.00 USD | 89,940.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,160,000.00 USD | 104.94 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,210,000.00 USD | 50,710.00 USD | 0.00 USD | `+13.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,210,000.00 USD | 114.98 USD | 0.00 USD | `+13.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,300,000.00 USD | 90,150.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,170,000.00 USD | 877,410.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,180,000.00 USD | 547.20 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,230,000.00 USD | 49,770.00 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,240,000.00 USD | 15,450.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,240,000.00 USD | 113.26 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,250,000.00 USD | 11,300.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,260,000.00 USD | 3,670.00 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,260,000.00 USD | 3,770.00 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,260,000.00 USD | 1,200.00 USD | 0.00 USD | `+15.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,260,000.00 USD | 327.58 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,260,000.00 USD | 270.66 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,260,000.00 USD | 164.68 USD | 0.00 USD | `+16.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,310,000.00 USD | 44,400.00 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,310,000.00 USD | 1,710.00 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,430,000.00 USD | 120,710.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,440,000.00 USD | 9,820.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,440,000.00 USD | 537.61 USD | 0.00 USD | `+17.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,970,000.00 USD | 532,880.00 USD | 0.00 USD | `+17.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,980,000.00 USD | 5,540.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,980,000.00 USD | 589.22 USD | 0.00 USD | `+18.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,980,000.00 USD | 733.03 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,980,000.00 USD | 693.64 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 5,030,000.00 USD | 50,110.00 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 5,030,000.00 USD | 2,980.00 USD | 0.00 USD | `+19.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,030,000.00 USD | 961.16 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 5,040,000.00 USD | 2,020.00 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 5,040,000.00 USD | 6,220.00 USD | 0.00 USD | `+19.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 5,150,000.00 USD | 107,860.00 USD | 0.00 USD | `+20.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 5,160,000.00 USD | 9,950.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,160,000.00 USD | 438.60 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 5,170,000.00 USD | 6,560.00 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 5,210,000.00 USD | 43,730.00 USD | 0.00 USD | `+21.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 5,340,000.00 USD | 130,550.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,340,000.00 USD | 425.62 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 5,360,000.00 USD | 15,090.00 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 5,360,000.00 USD | 4,750.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 5,370,000.00 USD | 13,190.00 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,390,000.00 USD | 19,720.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,610,000.00 USD | 219,900.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,660,000.00 USD | 45,700.00 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,710,000.00 USD | 45,900.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,710,000.00 USD | 4,610.00 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,870,000.00 USD | 157,540.00 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,870,000.00 USD | 5,600.00 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,920,000.00 USD | 45,680.00 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,940,000.00 USD | 18,790.00 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,010,000.00 USD | 74,260.00 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,060,000.00 USD | 50,010.00 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,080,000.00 USD | 14,320.00 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,130,000.00 USD | 55,670.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,150,000.00 USD | 20,540.00 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,150,000.00 USD | 384.94 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,160,000.00 USD | 6,020.00 USD | 0.00 USD | `+25.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,160,000.00 USD | 5,510.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 6,160,000.00 USD | 581.53 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,160,000.00 USD | 295.23 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,170,000.00 USD | 4,950.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,170,000.00 USD | 281.55 USD | 0.00 USD | `+27.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,180,000.00 USD | 9,380.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,180,000.00 USD | 2,840.00 USD | 0.00 USD | `+27.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,190,000.00 USD | 5,860.00 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,300,000.00 USD | 116,400.00 USD | 0.00 USD | `+28.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,310,000.00 USD | 2,210.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,310,000.00 USD | 5,720.00 USD | 0.00 USD | `+28.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,340,000.00 USD | 24,700.00 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 6,340,000.00 USD | 2,430.00 USD | 0.00 USD | `+29.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,340,000.00 USD | 286.94 USD | 0.00 USD | `+29.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,340,000.00 USD | 2,900.00 USD | 0.00 USD | `+30.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,350,000.00 USD | 5,800.00 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,350,000.00 USD | 329.13 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,350,000.00 USD | 1,970.00 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,350,000.00 USD | 1,120.00 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,350,000.00 USD | 1,150.00 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,360,000.00 USD | 8,210.00 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,360,000.00 USD | 3,450.00 USD | 0.00 USD | `+31.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,370,000.00 USD | 345.45 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.89` | 6,370,000.00 USD | 2,950.00 USD | 0.00 USD | `+32.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,430,000.00 USD | 65,020.00 USD | 0.00 USD | `+32.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,440,000.00 USD | 1,790.00 USD | 0.00 USD | `+32.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,440,000.00 USD | 1,400.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,570,000.00 USD | 133,540.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,040,000.00 USD | 469,530.00 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,050,000.00 USD | 5,620.00 USD | 0.00 USD | `+33.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,050,000.00 USD | 9,410.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,170,000.00 USD | 119,340.00 USD | 0.00 USD | `+34.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,180,000.00 USD | 3,000.00 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,330,000.00 USD | 155,620.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,350,000.00 USD | 13,610.00 USD | 0.00 USD | `+35.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,410,000.00 USD | 60,250.00 USD | 0.00 USD | `+35.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,410,000.00 USD | 2,080.00 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,410,000.00 USD | 3,300.00 USD | 0.00 USD | `+35.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,410,000.00 USD | 2,550.00 USD | 0.00 USD | `+35.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,410,000.00 USD | 425.76 USD | 0.00 USD | `+36.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,420,000.00 USD | 2,030.00 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,420,000.00 USD | 4,120.00 USD | 0.00 USD | `+36.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,420,000.00 USD | 2,000.00 USD | 0.00 USD | `+36.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,480,000.00 USD | 61,050.00 USD | 0.00 USD | `+37.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,490,000.00 USD | 6,870.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,490,000.00 USD | 1,200.00 USD | 0.00 USD | `+37.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,500,000.00 USD | 11,620.00 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,510,000.00 USD | 1,940.00 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,510,000.00 USD | 1,410.00 USD | 0.00 USD | `+38.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,510,000.00 USD | 4,010.00 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,510,000.00 USD | 3,960.00 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.20` | 7,520,000.00 USD | 3,830.00 USD | 0.00 USD | `+39.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,590,000.00 USD | 66,850.00 USD | 0.00 USD | `+39.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,590,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,590,000.00 USD | 195.46 USD | 0.00 USD | `+39.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,600,000.00 USD | 7,480.00 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 7,600,000.00 USD | 3,670.00 USD | 0.00 USD | `+40.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 7,600,000.00 USD | 3,680.00 USD | 0.00 USD | `+41.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,610,000.00 USD | 7,370.00 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,610,000.00 USD | 310.70 USD | 0.00 USD | `+41.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,610,000.00 USD | 602.77 USD | 0.00 USD | `+41.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,610,000.00 USD | 449.79 USD | 0.00 USD | `+42.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,610,000.00 USD | 2,810.00 USD | 0.00 USD | `+42.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 7,620,000.00 USD | 3,560.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,620,000.00 USD | 3,230.00 USD | 0.00 USD | `+43.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,630,000.00 USD | 5,120.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.42` | 7,630,000.00 USD | 2,120.00 USD | 0.00 USD | `+44.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 7,630,000.00 USD | 613.26 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.49` | 7,630,000.00 USD | 2,080.00 USD | 0.00 USD | `+45.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,630,000.00 USD | 1,310.00 USD | 0.00 USD | `+45.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,680,000.00 USD | 43,090.00 USD | 0.00 USD | `+46.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,680,000.00 USD | 234.54 USD | 0.00 USD | `+46.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,690,000.00 USD | 14,070.00 USD | 0.00 USD | `+46.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,690,000.00 USD | 1,630.00 USD | 0.00 USD | `+47.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,690,000.00 USD | 2,390.00 USD | 0.00 USD | `+48.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,700,000.00 USD | 1,970.00 USD | 0.00 USD | `+48.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,700,000.00 USD | 3,220.00 USD | 0.00 USD | `+49.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.66` | 7,700,000.00 USD | 1,950.00 USD | 0.00 USD | `+49.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,700,000.00 USD | 1,250.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,700,000.00 USD | 3,060.00 USD | 0.00 USD | `+49.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.68` | 7,710,000.00 USD | 1,930.00 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,710,000.00 USD | 3,070.00 USD | 0.00 USD | `+50.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,710,000.00 USD | 1,920.00 USD | 0.00 USD | `+50.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,720,000.00 USD | 3,120.00 USD | 0.00 USD | `+51.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,720,000.00 USD | 3,080.00 USD | 0.00 USD | `+52.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,720,000.00 USD | 1,990.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,720,000.00 USD | 647.56 USD | 0.00 USD | `+52.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,720,000.00 USD | 1,420.00 USD | 0.00 USD | `+52.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,720,000.00 USD | 2,130.00 USD | 0.00 USD | `+52.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,730,000.00 USD | 3,140.00 USD | 0.00 USD | `+53.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,730,000.00 USD | 342.25 USD | 0.00 USD | `+53.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 7,730,000.00 USD | 1,830.00 USD | 0.00 USD | `+53.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,730,000.00 USD | 2,990.00 USD | 0.00 USD | `+54.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,740,000.00 USD | 2,970.00 USD | 0.00 USD | `+54.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,740,000.00 USD | 391.51 USD | 0.00 USD | `+55.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,740,000.00 USD | 504.21 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.96` | 7,740,000.00 USD | 1,900.00 USD | 0.00 USD | `+56.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,740,000.00 USD | 166.00 USD | 0.00 USD | `+56.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,740,000.00 USD | 4,190.00 USD | 0.00 USD | `+56.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,760,000.00 USD | 17,380.00 USD | 0.00 USD | `+57.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 7,760,000.00 USD | 1,750.00 USD | 0.00 USD | `+57.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,760,000.00 USD | 236.31 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.08` | 7,760,000.00 USD | 1,840.00 USD | 0.00 USD | `+59.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,760,000.00 USD | 264.31 USD | 0.00 USD | `+59.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,760,000.00 USD | 599.34 USD | 0.00 USD | `+60.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,760,000.00 USD | 193.19 USD | 0.00 USD | `+60.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,770,000.00 USD | 3,950.00 USD | 0.00 USD | `+61.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,770,000.00 USD | 1,940.00 USD | 0.00 USD | `+61.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.22` | 7,770,000.00 USD | 1,770.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,930,000.00 USD | 160,550.00 USD | 0.00 USD | `+62.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,930,000.00 USD | 1,750.00 USD | 0.00 USD | `+63.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,940,000.00 USD | 731.50 USD | 0.00 USD | `+64.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.33` | 7,940,000.00 USD | 1,730.00 USD | 0.00 USD | `+64.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,940,000.00 USD | 1,710.00 USD | 0.00 USD | `+65.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 7,950,000.00 USD | 7,870.00 USD | 0.00 USD | `+65.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,950,000.00 USD | 3,250.00 USD | 0.00 USD | `+66.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,960,000.00 USD | 7,770.00 USD | 0.00 USD | `+68.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 7,960,000.00 USD | 1,620.00 USD | 0.00 USD | `+69.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,960,000.00 USD | 4,640.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,960,000.00 USD | 371.88 USD | 0.00 USD | `+70.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,970,000.00 USD | 380.68 USD | 0.00 USD | `+72.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.70` | 7,970,000.00 USD | 133.12 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 7,970,000.00 USD | 1,490.00 USD | 0.00 USD | `+74.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,970,000.00 USD | 1,470.00 USD | 0.00 USD | `+74.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,980,000.00 USD | 11,170.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 8,010,000.00 USD | 34,360.00 USD | 0.00 USD | `+75.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 8,010,000.00 USD | 399.35 USD | 0.00 USD | `+75.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 8,020,000.00 USD | 1,470.00 USD | 0.00 USD | `+75.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 8,020,000.00 USD | 1,550.00 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 8,030,000.00 USD | 10,610.00 USD | 0.00 USD | `+78.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 8,030,000.00 USD | 309.43 USD | 0.00 USD | `+79.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 8,070,000.00 USD | 42,490.00 USD | 0.00 USD | `+79.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 8,150,000.00 USD | 81,310.00 USD | 0.00 USD | `+80.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 8,150,000.00 USD | 1,390.00 USD | 0.00 USD | `+82.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 8,150,000.00 USD | 216.90 USD | 0.00 USD | `+83.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 8,150,000.00 USD | 738.45 USD | 0.00 USD | `+84.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 8,160,000.00 USD | 1,350.00 USD | 0.00 USD | `+86.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 8,210,000.00 USD | 56,000.00 USD | 0.00 USD | `+88.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 8,210,000.00 USD | 1,260.00 USD | 0.00 USD | `+88.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 8,320,000.00 USD | 103,010.00 USD | 0.00 USD | `+88.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 8,320,000.00 USD | 1,330.00 USD | 0.00 USD | `+89.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 8,320,000.00 USD | 721.22 USD | 0.00 USD | `+90.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 8,320,000.00 USD | 2,010.00 USD | 0.00 USD | `+93.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 8,320,000.00 USD | 596.33 USD | 0.00 USD | `+94.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 8,320,000.00 USD | 3,670.00 USD | 0.00 USD | `+94.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 8,320,000.00 USD | 384.34 USD | 0.00 USD | `+96.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 8,330,000.00 USD | 1,600.00 USD | 0.00 USD | `+97.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 8,330,000.00 USD | 1,820.00 USD | 0.00 USD | `+97.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 8,330,000.00 USD | 1,950.00 USD | 0.00 USD | `+99.45%` | `TACTICAL (Retail Cluster)` |

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
  * Execution Entry: `4.31` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4.22` (Risk Distance: `0.0914` pts)
  * +2.5R Take Profit: `4.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.59` (Risk Distance: `0.0914` pts)
  * +2.5R Take Profit: `4.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
