# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:39:17 IST` (`2026-10-30 10:09:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3329` | **Live Ask Quote**: `0.3367` | **Mid Price**: `0.3348`
- **Spread Points**: `38.00` | **Spread BPS**: `113.50 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3456` | VWAP Z-Score: `-1.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0029` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.73` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3734` | Lower -3.00σ Band: `0.3177`
  * Upper +2.51σ Band: `0.3689` | Lower -2.51σ Band: `0.3223`
  * Upper +2.01σ Band: `0.3642` | Lower -2.01σ Band: `0.3269`
  * Upper +2.00σ Band: `0.3641` | Lower -2.00σ Band: `0.3270`
  * Upper +1.28σ Band: `0.3575` | Lower -1.28σ Band: `0.3337`
  * Upper +1.00σ Band: `0.3549` | Lower -1.00σ Band: `0.3363`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3326` | EMA-20=`0.3355` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3389` (Slope: `+0.0000`) | EMA-100=`0.3379`
  * Institutional Anchors: EMA-144=`0.3366` | EMA-200=`0.3353` (Slope: `-0.1087`) | EMA-233=`0.3346`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-6.40%`)
  * Point of Control (POC) = `0.3513` (Distance: `-4.69%`)
  * Value Area Low (VAL) = `0.3409` (Distance: `-1.77%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3465` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3368` | Low=`0.3328`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3335` - `0.3361`
  * Optimal Trade Entry (OTE 0.705): `0.3355`
  * Structural Invalidation Anchor (0.786): `0.3375`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3361` | `0.3364` | `0.3344` | `0.3344` | `2,073,971` | 695,683.29 USD | -102,327.09 USD | `-14.71%` | -2,713,698.64 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3344` | `0.3356` | `0.3343` | `0.3346` | `1,962,872` | 657,038.77 USD | -135,568.90 USD | `-20.63%` | -2,849,267.54 USD | `-0.86` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.3347` | `0.3353` | `0.3341` | `0.3347` | `1,721,049` | 575,854.96 USD | 90,701.83 USD | `+15.75%` | -2,758,565.71 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3322` | `0.3328` | `0.3319` | `0.3319` | `6,054,646` | 2,011,271.26 USD | -343,369.33 USD | `-17.07%` | -2,755,986.06 USD | `-0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3319` | `0.3367` | `0.3319` | `0.3361` | `11,450,681` | 3,824,910.39 USD | 144,614.51 USD | `+3.78%` | -2,611,371.55 USD | `+0.55` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3361` | `0.3364` | `0.3341` | `0.3347` | `5,778,981` | 1,935,634.56 USD | -148,823.39 USD | `-7.69%` | -2,760,194.94 USD | `+0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3379` | `0.3380` | `0.3310` | `0.3371` | `71,304,583` | 23,823,772.16 USD | 1,991,288.68 USD | `+8.36%` | -2,620,853.21 USD | `+1.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3324` | `39,413,287` | 13,120,323.22 USD | 312,055.16 USD | `+2.38%` | -2,308,798.06 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3324` | `0.3367` | `0.3318` | `0.3347` | `29,170,195` | 9,727,730.27 USD | -448,889.99 USD | `-4.61%` | -2,757,688.05 USD | `-0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3347` | `68,583,482` | 22,848,053.49 USD | -136,834.83 USD | `-0.60%` | -2,542,888.71 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3347` | `68,583,482` | 22,848,053.49 USD | -136,834.83 USD | `-0.60%` | -2,542,888.71 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3348`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1148` | `0xecb6...2b00` | `LONG` | 1,913,926.83 USD | `5,694,516.00` | `0.3343` | `0.3356` | `0.000000` | 9,979.88 USD | `+0.52%` | `10X Cross` |
| `1585` | `0x8dd7...fa30` | `SHORT` | 1,343,200.00 USD | `4,000,000.00` | `0.3329` | `0.3356` | `0.3866` | -11,711.31 USD | `-0.87%` | `6X Cross` |
| `1586` | `0xeadc...9d55` | `LONG` | 1,340,480.00 USD | `4,000,000.00` | `0.3421` | `0.3356` | `0.000000` | -27,998.09 USD | `-2.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 8,138.69 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 8.14K USD at 0.3317 USD [API] | `2026-10-29 09:27:20` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 7,871.14 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.87K USD at 0.3316 USD [API] | `2026-10-29 10:14:22` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,469.10 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 9,999.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 10.00K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--1.74%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--3.22%`)
  * 3D Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3252` (Vol: 817,700.00 USD, Dist: `--3.12%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+9.09%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--3.22%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0735` | 3,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 6,660.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 858.60 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 181.91 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 964.61 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 152.08 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,290.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 265.88 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 123.26 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,870.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 6,680.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 57,490.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 23,990.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 648.96 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 48,180.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 5,170.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 255.53 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 278.69 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,400.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 263.54 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,520.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 1,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 230.42 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 201.14 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,420.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 413.53 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 568.81 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 3,790.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,910.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 993,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,220.00 USD | 993,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 302.96 USD | 992,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 991,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 107.74 USD | 991,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 11,370.00 USD | 990,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 979,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 976,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 976,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,390.00 USD | 976,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 220.99 USD | 973,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,470.00 USD | 972,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 13,170.00 USD | 888,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 875,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 13,300.00 USD | 868,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 3,690.00 USD | 855,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 838.74 USD | 851,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 1,090.00 USD | 851,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 5,880.00 USD | 850,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,150.00 USD | 844,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 4,940.00 USD | 840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 821.82 USD | 835,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 834,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 833,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 833,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 20,530,000.00 USD | 20,530,000.00 USD | 82,110.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 832,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 20,440,000.00 USD | 20,440,000.00 USD | 109,100.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 20,300,000.00 USD | 20,300,000.00 USD | 122,490.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,010.00 USD | 832,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 20,070,000.00 USD | 20,070,000.00 USD | 88,760.00 USD | 36,460.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2974` | 14,300,000.00 USD | 14,300,000.00 USD | 167.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 19,900,000.00 USD | 19,900,000.00 USD | 53,840.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2978` | 14,300,000.00 USD | 14,300,000.00 USD | 17,600.00 USD | 3,340.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2982` | 14,280,000.00 USD | 14,280,000.00 USD | 26,560.00 USD | 7,720.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 19,810,000.00 USD | 19,810,000.00 USD | 170,390.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 831,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2986` | 14,220,000.00 USD | 14,220,000.00 USD | 102,450.00 USD | 9,300.00 USD | 7,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 19,580,000.00 USD | 19,580,000.00 USD | 109,910.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2990` | 14,110,000.00 USD | 14,110,000.00 USD | 50,390.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2994` | 14,050,000.00 USD | 14,050,000.00 USD | 19,550.00 USD | 37,800.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 19,430,000.00 USD | 19,430,000.00 USD | 6,450.00 USD | 62,740.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 831,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2998` | 13,900,000.00 USD | 13,900,000.00 USD | 9,360.00 USD | 24,820.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 19,280,000.00 USD | 19,280,000.00 USD | 2,360.00 USD | 15,390.00 USD | 62,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3002` | 13,850,000.00 USD | 13,850,000.00 USD | 15,600.00 USD | 20,670.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 830,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3006` | 13,790,000.00 USD | 13,790,000.00 USD | 848.70 USD | 1,800.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 19,200,000.00 USD | 19,200,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3010` | 13,760,000.00 USD | 13,760,000.00 USD | 34,290.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 19,160,000.00 USD | 19,160,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3014` | 13,720,000.00 USD | 13,720,000.00 USD | 17,320.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 820,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3018` | 13,700,000.00 USD | 13,700,000.00 USD | 1,630.00 USD | 6,650.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3022` | 13,670,000.00 USD | 13,670,000.00 USD | 14,930.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 820,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3026` | 13,650,000.00 USD | 13,650,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3030` | 13,650,000.00 USD | 13,650,000.00 USD | 24,620.00 USD | 8,320.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 19,140,000.00 USD | 19,140,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3034` | 13,610,000.00 USD | 13,610,000.00 USD | 742.30 USD | 0.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 817,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3037` | 19,090,000.00 USD | 19,090,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3038` | 13,600,000.00 USD | 13,600,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3042` | 13,590,000.00 USD | 13,590,000.00 USD | 537.63 USD | 9,300.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3043` | 19,080,000.00 USD | 19,080,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 813,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3046` | 13,530,000.00 USD | 13,530,000.00 USD | 31,710.00 USD | 18,130.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 19,080,000.00 USD | 19,080,000.00 USD | 18,020.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3050` | 13,470,000.00 USD | 13,470,000.00 USD | 165.80 USD | 8,990.00 USD | 53,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3054` | 13,410,000.00 USD | 13,410,000.00 USD | 46,820.00 USD | 13,380.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 19,000,000.00 USD | 19,000,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 813,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 19,000,000.00 USD | 19,000,000.00 USD | 32,680.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3062` | 13,310,000.00 USD | 13,310,000.00 USD | 885.25 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 798,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3066` | 13,250,000.00 USD | 13,250,000.00 USD | 31,110.00 USD | 29,620.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 18,920,000.00 USD | 18,920,000.00 USD | 6,500.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3070` | 13,150,000.00 USD | 13,150,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 18,900,000.00 USD | 18,900,000.00 USD | 7,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3074` | 13,140,000.00 USD | 13,140,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 792,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3079` | 18,900,000.00 USD | 18,900,000.00 USD | 38,320.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3082` | 13,120,000.00 USD | 13,120,000.00 USD | 18,640.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 18,800,000.00 USD | 18,800,000.00 USD | 2,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 792,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3086` | 13,080,000.00 USD | 13,080,000.00 USD | 363.64 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3090` | 13,070,000.00 USD | 13,070,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 18,790,000.00 USD | 18,790,000.00 USD | 8,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3094` | 13,070,000.00 USD | 13,070,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 791,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3097` | 18,790,000.00 USD | 18,790,000.00 USD | 75,040.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3098` | 13,050,000.00 USD | 13,050,000.00 USD | 7,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3102` | 13,040,000.00 USD | 13,040,000.00 USD | 57,870.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 18,650,000.00 USD | 18,650,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 791,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3106` | 12,920,000.00 USD | 12,920,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 18,520,000.00 USD | 18,520,000.00 USD | 6,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3114` | 12,920,000.00 USD | 12,920,000.00 USD | 977.81 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 18,520,000.00 USD | 18,520,000.00 USD | 10,340.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 790,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3118` | 12,910,000.00 USD | 12,910,000.00 USD | 14,500.00 USD | 8,100.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 18,470,000.00 USD | 18,470,000.00 USD | 162,580.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3122` | 12,870,000.00 USD | 12,870,000.00 USD | 13,610.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,810.00 USD | 777,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3126` | 12,820,000.00 USD | 12,820,000.00 USD | 12,430.00 USD | 13,530.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 18,290,000.00 USD | 18,290,000.00 USD | 21,180.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3130` | 12,790,000.00 USD | 12,790,000.00 USD | 2,430.00 USD | 28,470.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 18,150,000.00 USD | 18,150,000.00 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3134` | 12,730,000.00 USD | 12,730,000.00 USD | 5,000.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 446.11 USD | 759,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3138` | 12,700,000.00 USD | 12,700,000.00 USD | 5,650.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 18,150,000.00 USD | 18,150,000.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3142` | 12,680,000.00 USD | 12,680,000.00 USD | 4,220.00 USD | 3,580.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 18,150,000.00 USD | 18,150,000.00 USD | 247,810.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 577.11 USD | 758,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3146` | 12,660,000.00 USD | 12,660,000.00 USD | 1,850.00 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3150` | 12,660,000.00 USD | 12,660,000.00 USD | 4,810.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 17,830,000.00 USD | 17,830,000.00 USD | 196,920.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3154` | 12,630,000.00 USD | 12,630,000.00 USD | 27,150.00 USD | 1,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 2,960.00 USD | 758,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3157` | 17,560,000.00 USD | 17,560,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3158` | 12,600,000.00 USD | 12,600,000.00 USD | 10,540.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3162` | 12,570,000.00 USD | 12,570,000.00 USD | 5,670.00 USD | 5,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 17,010,000.00 USD | 17,010,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 512.73 USD | 755,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3166` | 12,560,000.00 USD | 12,560,000.00 USD | 43,210.00 USD | 35,060.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 16,160,000.00 USD | 16,160,000.00 USD | 417,380.00 USD | 106,680.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3170` | 12,470,000.00 USD | 12,470,000.00 USD | 6,720.00 USD | 35,130.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3174` | 12,410,000.00 USD | 12,410,000.00 USD | 21,050.00 USD | 7,370.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 15,500,000.00 USD | 15,500,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,290.00 USD | 754,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3178` | 12,350,000.00 USD | 12,350,000.00 USD | 59,190.00 USD | 9,500.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 15,240,000.00 USD | 15,240,000.00 USD | 751,290.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3182` | 12,240,000.00 USD | 12,240,000.00 USD | 329,920.00 USD | 43,320.00 USD | 82,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3186` | 11,790,000.00 USD | 11,790,000.00 USD | 80,290.00 USD | 54,030.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 14,230,000.00 USD | 14,230,000.00 USD | 408,400.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3190` | 11,610,000.00 USD | 11,610,000.00 USD | 191,070.00 USD | 0.00 USD | 56,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 13,690,000.00 USD | 13,690,000.00 USD | 118,210.00 USD | 104,710.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3194` | 11,360,000.00 USD | 11,360,000.00 USD | 150,770.00 USD | 117,490.00 USD | 267,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 1,430.00 USD | 752,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3198` | 10,830,000.00 USD | 10,830,000.00 USD | 84,870.00 USD | 108,400.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 127,390.00 USD | 190,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3202` | 10,570,000.00 USD | 10,570,000.00 USD | 219,620.00 USD | 63,290.00 USD | 122,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 12,910,000.00 USD | 12,910,000.00 USD | 100,160.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 455.75 USD | 751,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3206` | 10,160,000.00 USD | 10,160,000.00 USD | 127,850.00 USD | 16,080.00 USD | 119,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3210` | 9,900,000.00 USD | 9,900,000.00 USD | 88,620.00 USD | 31,880.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 12,620,000.00 USD | 12,620,000.00 USD | 569,720.00 USD | 117,230.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3214` | 9,740,000.00 USD | 9,740,000.00 USD | 53,360.00 USD | 45,170.00 USD | 83,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3215` | 756.17 USD | 750,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3217` | 11,690,000.00 USD | 11,690,000.00 USD | 286,830.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3218` | 9,560,000.00 USD | 9,560,000.00 USD | 5,550.00 USD | 28,050.00 USD | 87,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3222` | 9,440,000.00 USD | 9,440,000.00 USD | 154,560.00 USD | 24,690.00 USD | 69,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 11,230,000.00 USD | 11,230,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3226` | 9,190,000.00 USD | 9,190,000.00 USD | 13,670.00 USD | 24,400.00 USD | 188,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 10,290,000.00 USD | 10,290,000.00 USD | 858,070.00 USD | 299,190.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3230` | 8,960,000.00 USD | 8,960,000.00 USD | 92,790.00 USD | 46,020.00 USD | 86,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3234` | 8,740,000.00 USD | 8,740,000.00 USD | 61,120.00 USD | 72,090.00 USD | 93,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 8,750,000.00 USD | 8,750,000.00 USD | 709,160.00 USD | 213,370.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 749,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3238` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 53,490.00 USD | 138,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 7,460,000.00 USD | 7,460,000.00 USD | 433,820.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3242` | 8,320,000.00 USD | 8,320,000.00 USD | 97,850.00 USD | 17,220.00 USD | 231,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3246` | 7,970,000.00 USD | 7,970,000.00 USD | 256,230.00 USD | 90,310.00 USD | 171,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 6,740,000.00 USD | 6,740,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3250` | 7,450,000.00 USD | 7,450,000.00 USD | 758,560.00 USD | 89,640.00 USD | 318,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 5,410,000.00 USD | 5,410,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3254` | 6,290,000.00 USD | 6,290,000.00 USD | 340,830.00 USD | 61,360.00 USD | 299,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3258` | 5,590,000.00 USD | 5,590,000.00 USD | 373,570.00 USD | 71,210.00 USD | 143,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 3,810,000.00 USD | 3,810,000.00 USD | 182,240.00 USD | 250,110.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3262` | 5,000,000.00 USD | 5,000,000.00 USD | 115,280.00 USD | 378,600.00 USD | 505,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 2,880,000.00 USD | 2,880,000.00 USD | 80,160.00 USD | 197,270.00 USD | 347,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3266` | 4,000,000.00 USD | 4,000,000.00 USD | 44,720.00 USD | 157,840.00 USD | 354,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3270` | 3,440,000.00 USD | 3,440,000.00 USD | 237,730.00 USD | 115,770.00 USD | 350,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,250,000.00 USD | 2,250,000.00 USD | 192,500.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3274` | 2,740,000.00 USD | 2,740,000.00 USD | 155,490.00 USD | 61,310.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 746,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3277` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3278` | 2,320,000.00 USD | 2,320,000.00 USD | 268,410.00 USD | 32,310.00 USD | 133,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3282` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 61,320.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 1,550,000.00 USD | 1,550,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 746,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3286` | 1,810,000.00 USD | 1,810,000.00 USD | 45,960.00 USD | 39,260.00 USD | 113,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3290` | 1,610,000.00 USD | 1,610,000.00 USD | 109,890.00 USD | 44,530.00 USD | 72,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3294` | 1,380,000.00 USD | 1,380,000.00 USD | 61,960.00 USD | 26,090.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,110,000.00 USD | 1,110,000.00 USD | 255,850.00 USD | 83,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 839.90 USD | 839.90 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3298` | 1,210,000.00 USD | 1,210,000.00 USD | 105,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 774,520.00 USD | 774,520.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3302` | 1,110,000.00 USD | 1,110,000.00 USD | 37,670.00 USD | 58,700.00 USD | 93,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3305` | 7,080.00 USD | 7,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3306` | 917,340.00 USD | 917,340.00 USD | 110,810.00 USD | 16,160.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 581,350.00 USD | 581,350.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3310` | 778,660.00 USD | 778,660.00 USD | 11,600.00 USD | 122,460.00 USD | 444,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 108,550.00 USD | 108,550.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3314` | 199,680.00 USD | 199,680.00 USD | 0.00 USD | 54,160.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3318` | 58,950.00 USD | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 57,890.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3358` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3370` | 217,200.00 USD | 217,200.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3374` | 546,840.00 USD | 546,840.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 21,390.00 USD | 21,390.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3382` | 618,740.00 USD | 618,740.00 USD | 71,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 147,040.00 USD | 147,040.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3386` | 778,070.00 USD | 778,070.00 USD | 92,750.00 USD | 11,160.00 USD | 55,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3390` | 1,160,000.00 USD | 1,160,000.00 USD | 302,930.00 USD | 27,820.00 USD | 49,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 381,700.00 USD | 381,700.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3394` | 1,960,000.00 USD | 1,960,000.00 USD | 115,280.00 USD | 200,920.00 USD | 485,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 1,640,000.00 USD | 1,640,000.00 USD | 262,880.00 USD | 586,760.00 USD | 410,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3398` | 2,350,000.00 USD | 2,350,000.00 USD | 43,780.00 USD | 216,810.00 USD | 129,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3402` | 2,840,000.00 USD | 2,840,000.00 USD | 20,340.00 USD | 97,740.00 USD | 374,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 3,040,000.00 USD | 3,040,000.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3406` | 3,250,000.00 USD | 3,250,000.00 USD | 260,970.00 USD | 0.00 USD | 150,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3410` | 3,570,000.00 USD | 3,570,000.00 USD | 257,330.00 USD | 34,110.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3414` | 4,070,000.00 USD | 4,070,000.00 USD | 376,520.00 USD | 27,220.00 USD | 97,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3418` | 4,480,000.00 USD | 4,480,000.00 USD | 343,500.00 USD | 32,360.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3422` | 4,580,000.00 USD | 4,580,000.00 USD | 71,180.00 USD | 31,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3426` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 156,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3430` | 5,130,000.00 USD | 5,130,000.00 USD | 166,310.00 USD | 220,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 3,990,000.00 USD | 3,990,000.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3434` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 83,080.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3438` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 49,600.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3442` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 51,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 4,090,000.00 USD | 4,090,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3446` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 60,100.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3450` | 5,770,000.00 USD | 5,770,000.00 USD | 35,950.00 USD | 45,930.00 USD | 119,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 4,180,000.00 USD | 4,180,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3454` | 6,060,000.00 USD | 6,060,000.00 USD | 126,310.00 USD | 54,930.00 USD | 106,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3458` | 6,830,000.00 USD | 6,830,000.00 USD | 159,870.00 USD | 100,770.00 USD | 507,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3462` | 7,260,000.00 USD | 7,260,000.00 USD | 168,310.00 USD | 124,400.00 USD | 142,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 167,950.00 USD | 205,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3466` | 7,460,000.00 USD | 7,460,000.00 USD | 21,890.00 USD | 65,550.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 5,110,000.00 USD | 5,110,000.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3470` | 7,590,000.00 USD | 7,590,000.00 USD | 37,620.00 USD | 36,280.00 USD | 61,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3474` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 42,560.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3478` | 7,890,000.00 USD | 7,890,000.00 USD | 51,860.00 USD | 40,550.00 USD | 134,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 5,210,000.00 USD | 5,210,000.00 USD | 6,440.00 USD | 14,700.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3482` | 7,980,000.00 USD | 7,980,000.00 USD | 56,790.00 USD | 20,460.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3486` | 8,020,000.00 USD | 8,020,000.00 USD | 7,190.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3490` | 8,130,000.00 USD | 8,130,000.00 USD | 40,230.00 USD | 10,900.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3494` | 8,240,000.00 USD | 8,240,000.00 USD | 5,420.00 USD | 24,400.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3498` | 8,700,000.00 USD | 8,700,000.00 USD | 83,150.00 USD | 0.00 USD | 375,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 5,390,000.00 USD | 5,390,000.00 USD | 133,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3502` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 5,400,000.00 USD | 5,400,000.00 USD | 12,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 9,630.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3506` | 8,880,000.00 USD | 8,880,000.00 USD | 74,220.00 USD | 0.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3510` | 8,930,000.00 USD | 8,930,000.00 USD | 2,790.00 USD | 12,400.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 6,360,000.00 USD | 6,360,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3514` | 9,030,000.00 USD | 9,030,000.00 USD | 21,910.00 USD | 0.00 USD | 73,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 175.05 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3517` | 6,380,000.00 USD | 6,380,000.00 USD | 12,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3518` | 9,110,000.00 USD | 9,110,000.00 USD | 30,510.00 USD | 11,560.00 USD | 42,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3522` | 9,130,000.00 USD | 9,130,000.00 USD | 2,260.00 USD | 16,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 6,790,000.00 USD | 6,790,000.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3526` | 9,170,000.00 USD | 9,170,000.00 USD | 5,360.00 USD | 6,280.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3530` | 9,410,000.00 USD | 9,410,000.00 USD | 101,220.00 USD | 52,710.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3534` | 9,680,000.00 USD | 9,680,000.00 USD | 127,850.00 USD | 56,820.00 USD | 87,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 7,060,000.00 USD | 7,060,000.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3538` | 9,820,000.00 USD | 9,820,000.00 USD | 3,230.00 USD | 21,150.00 USD | 108,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 7,980,000.00 USD | 7,980,000.00 USD | 799,020.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3542` | 10,020,000.00 USD | 10,020,000.00 USD | 83,710.00 USD | 84,150.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3546` | 10,110,000.00 USD | 10,110,000.00 USD | 5,090.00 USD | 51,930.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 8,280,000.00 USD | 8,280,000.00 USD | 11,040.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3550` | 10,160,000.00 USD | 10,160,000.00 USD | 2,710.00 USD | 42,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3554` | 10,260,000.00 USD | 10,260,000.00 USD | 21,530.00 USD | 40,120.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3558` | 10,320,000.00 USD | 10,320,000.00 USD | 331.60 USD | 25,350.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 8,410,000.00 USD | 8,410,000.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3562` | 10,460,000.00 USD | 10,460,000.00 USD | 977.81 USD | 17,880.00 USD | 115,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3566` | 10,470,000.00 USD | 10,470,000.00 USD | 2,090.00 USD | 11,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3570` | 10,480,000.00 USD | 10,480,000.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 8,460,000.00 USD | 8,460,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3574` | 10,620,000.00 USD | 10,620,000.00 USD | 131,860.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 8,590,000.00 USD | 8,590,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3578` | 10,690,000.00 USD | 10,690,000.00 USD | 31,190.00 USD | 9,130.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3582` | 10,720,000.00 USD | 10,720,000.00 USD | 2,980.00 USD | 14,930.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3586` | 10,740,000.00 USD | 10,740,000.00 USD | 17,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3590` | 10,790,000.00 USD | 10,790,000.00 USD | 3,780.00 USD | 15,750.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3594` | 11,000,000.00 USD | 11,000,000.00 USD | 111,740.00 USD | 0.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3598` | 11,130,000.00 USD | 11,130,000.00 USD | 46,200.00 USD | 22,780.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 9,740,000.00 USD | 9,740,000.00 USD | 4,040.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3602` | 11,330,000.00 USD | 11,330,000.00 USD | 32,190.00 USD | 32,480.00 USD | 136,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3606` | 11,550,000.00 USD | 11,550,000.00 USD | 30,100.00 USD | 26,580.00 USD | 157,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 10,140,000.00 USD | 10,140,000.00 USD | 330,200.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3610` | 11,770,000.00 USD | 11,770,000.00 USD | 75,090.00 USD | 45,020.00 USD | 100,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 10,840,000.00 USD | 10,840,000.00 USD | 77,710.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3614` | 11,960,000.00 USD | 11,960,000.00 USD | 10,940.00 USD | 40,360.00 USD | 135,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3618` | 12,340,000.00 USD | 12,340,000.00 USD | 225,600.00 USD | 56,810.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 11,050,000.00 USD | 11,050,000.00 USD | 3,500.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3622` | 12,650,000.00 USD | 12,650,000.00 USD | 169,910.00 USD | 69,640.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 2,410.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3626` | 12,780,000.00 USD | 12,780,000.00 USD | 73,050.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3630` | 14,070,000.00 USD | 14,070,000.00 USD | 1,120,000.00 USD | 93,320.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 11,360,000.00 USD | 11,360,000.00 USD | 678.26 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3634` | 14,430,000.00 USD | 14,430,000.00 USD | 144,090.00 USD | 14,760.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,260.00 USD | 48,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3637` | 11,380,000.00 USD | 11,380,000.00 USD | 937.01 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3638` | 14,750,000.00 USD | 14,750,000.00 USD | 183,690.00 USD | 65,110.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3642` | 15,100,000.00 USD | 15,100,000.00 USD | 103,140.00 USD | 206,820.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 12,180,000.00 USD | 12,180,000.00 USD | 4,830.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 60,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3646` | 15,480,000.00 USD | 15,480,000.00 USD | 333,280.00 USD | 21,220.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 12,350,000.00 USD | 12,350,000.00 USD | 177,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3650` | 15,700,000.00 USD | 15,700,000.00 USD | 2,410.00 USD | 55,120.00 USD | 168,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3654` | 16,320,000.00 USD | 16,320,000.00 USD | 405,500.00 USD | 47,350.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 13,140,000.00 USD | 13,140,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3658` | 16,920,000.00 USD | 16,920,000.00 USD | 240,260.00 USD | 152,790.00 USD | 203,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 14,130,000.00 USD | 14,130,000.00 USD | 685,520.00 USD | 60,550.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3662` | 17,200,000.00 USD | 17,200,000.00 USD | 161,450.00 USD | 61,740.00 USD | 55,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,110.00 USD | 63,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3666` | 17,860,000.00 USD | 17,860,000.00 USD | 475,420.00 USD | 119,560.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 14,700,000.00 USD | 14,700,000.00 USD | 422,610.00 USD | 15,390.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3670` | 18,340,000.00 USD | 18,340,000.00 USD | 94,630.00 USD | 66,280.00 USD | 318,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 15,390,000.00 USD | 15,390,000.00 USD | 512,420.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3674` | 18,600,000.00 USD | 18,600,000.00 USD | 41,190.00 USD | 72,620.00 USD | 148,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3678` | 19,320,000.00 USD | 19,320,000.00 USD | 517,910.00 USD | 34,010.00 USD | 164,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 15,650,000.00 USD | 15,650,000.00 USD | 259,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3682` | 19,840,000.00 USD | 19,840,000.00 USD | 286,630.00 USD | 82,130.00 USD | 148,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 15,830,000.00 USD | 15,830,000.00 USD | 4,100.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3686` | 20,400,000.00 USD | 20,400,000.00 USD | 327,450.00 USD | 153,840.00 USD | 81,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3690` | 20,930,000.00 USD | 20,930,000.00 USD | 475,810.00 USD | 51,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 16,240,000.00 USD | 16,240,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3694` | 21,180,000.00 USD | 21,180,000.00 USD | 154,310.00 USD | 72,220.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 163,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3698` | 21,360,000.00 USD | 21,360,000.00 USD | 170,350.00 USD | 15,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3702` | 22,020,000.00 USD | 22,020,000.00 USD | 438,600.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 16,450,000.00 USD | 16,450,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 63,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3706` | 22,780,000.00 USD | 22,780,000.00 USD | 177,000.00 USD | 8,320.00 USD | 573,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 16,450,000.00 USD | 16,450,000.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3710` | 22,970,000.00 USD | 22,970,000.00 USD | 110,310.00 USD | 42,590.00 USD | 38,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3714` | 24,360,000.00 USD | 24,360,000.00 USD | 489,730.00 USD | 116,180.00 USD | 783,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 16,850,000.00 USD | 16,850,000.00 USD | 4,580.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3718` | 24,860,000.00 USD | 24,860,000.00 USD | 36,200.00 USD | 182,160.00 USD | 274,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3722` | 25,170,000.00 USD | 25,170,000.00 USD | 185,610.00 USD | 68,140.00 USD | 62,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 64,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 17,880,000.00 USD | 17,880,000.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 18,070,000.00 USD | 18,070,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,210.00 USD | 71,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3739` | 18,540,000.00 USD | 18,540,000.00 USD | 242,460.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 18,940,000.00 USD | 18,940,000.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3751` | 18,940,000.00 USD | 18,940,000.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 75,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3757` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 19,420,000.00 USD | 19,420,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 19,430,000.00 USD | 19,430,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 75,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3781` | 19,450,000.00 USD | 19,450,000.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 631,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 19,600,000.00 USD | 19,600,000.00 USD | 90,150.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 20,060,000.00 USD | 20,060,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 20,100,000.00 USD | 20,100,000.00 USD | 4,000.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 20,280,000.00 USD | 20,280,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 632,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3853` | 20,390,000.00 USD | 20,390,000.00 USD | 535.97 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 264.84 USD | 632,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3859` | 20,460,000.00 USD | 20,460,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 20,620,000.00 USD | 20,620,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 20,750,000.00 USD | 20,750,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 20,900,000.00 USD | 20,900,000.00 USD | 103,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 637,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 21,000,000.00 USD | 21,000,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 643,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 21,270,000.00 USD | 21,270,000.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 21,300,000.00 USD | 21,300,000.00 USD | 27,520.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 644,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 21,330,000.00 USD | 21,330,000.00 USD | 21,970.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 21,360,000.00 USD | 21,360,000.00 USD | 24,790.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 762,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 21,500,000.00 USD | 21,500,000.00 USD | 109,810.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 21,730,000.00 USD | 21,730,000.00 USD | 107,070.00 USD | 10,160.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 1,390,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3961` | 21,910,000.00 USD | 21,910,000.00 USD | 122,550.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 21,930,000.00 USD | 21,930,000.00 USD | 12,300.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 22,070,000.00 USD | 22,070,000.00 USD | 16,660.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 22,180,000.00 USD | 22,180,000.00 USD | 57,690.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 22,220,000.00 USD | 22,220,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3997` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4025` | 328.44 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 998.96 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 134.57 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4255` | 3,940.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4295` | 10,210.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4325` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4355` | 70,890.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 1,490.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 22,230.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 1,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 5,520.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 318.76 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4715` | 272.53 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4805` | 2,880.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 23,320.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 667.22 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5465` | 40,440.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 3,060.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 140.12 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5725` | 742,670.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 24,620.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6205` | 375.40 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 1,130.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 6,810.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6505` | 102,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 705.13 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0735` | 1,240,000.00 USD | 0.00 USD | 3,000.00 USD | `-77.94%` | `40,871.00` |
| `Live` | `Long` | `0.0755` | 1,240,000.00 USD | 0.00 USD | 6,660.00 USD | `-77.34%` | `88,233.00` |
| `Live` | `Long` | `0.0865` | 1,230,000.00 USD | 0.00 USD | 858.60 USD | `-74.04%` | `9,926.00` |
| `Live` | `Long` | `0.0875` | 1,230,000.00 USD | 0.00 USD | 181.91 USD | `-73.74%` | `2,079.00` |
| `Live` | `Long` | `0.0985` | 1,230,000.00 USD | 0.00 USD | 964.61 USD | `-70.44%` | `9,793.00` |
| `Live` | `Long` | `0.1065` | 1,230,000.00 USD | 0.00 USD | 152.08 USD | `-68.04%` | `1,428.00` |
| `Live` | `Long` | `0.1145` | 1,230,000.00 USD | 0.00 USD | 2,290.00 USD | `-65.64%` | `20,000.00` |
| `Live` | `Long` | `0.1155` | 1,230,000.00 USD | 0.00 USD | 265.88 USD | `-65.34%` | `2,302.00` |
| `Live` | `Long` | `0.1165` | 1,230,000.00 USD | 0.00 USD | 123.26 USD | `-65.04%` | `1,058.00` |
| `Live` | `Long` | `0.1285` | 1,230,000.00 USD | 0.00 USD | 9,870.00 USD | `-61.44%` | `76,797.00` |
| `Live` | `Long` | `0.1585` | 1,220,000.00 USD | 0.00 USD | 388.01 USD | `-52.43%` | `2,448.00` |
| `Live` | `Long` | `0.1625` | 1,220,000.00 USD | 0.00 USD | 6,680.00 USD | `-51.23%` | `41,100.00` |
| `Live` | `Long` | `0.1675` | 1,210,000.00 USD | 0.00 USD | 57,490.00 USD | `-49.73%` | `343,214.00` |
| `Live` | `Long` | `0.1685` | 1,150,000.00 USD | 0.00 USD | 23,990.00 USD | `-49.43%` | `142,400.00` |
| `Live` | `Long` | `0.1715` | 1,130,000.00 USD | 0.00 USD | 648.96 USD | `-48.53%` | `3,784.00` |
| `Live` | `Long` | `0.1725` | 1,130,000.00 USD | 0.00 USD | 48,180.00 USD | `-48.23%` | `279,283.00` |
| `Live` | `Long` | `0.1735` | 1,080,000.00 USD | 0.00 USD | 339.71 USD | `-47.93%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,080,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.63%` | `29,642.00` |
| `Live` | `Long` | `0.1755` | 1,070,000.00 USD | 0.00 USD | 255.53 USD | `-47.33%` | `1,456.00` |
| `Live` | `Long` | `0.1765` | 1,070,000.00 USD | 0.00 USD | 278.69 USD | `-47.03%` | `1,579.00` |
| `Live` | `Long` | `0.1775` | 1,070,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.73%` | `7,875.00` |
| `Live` | `Long` | `0.1815` | 1,070,000.00 USD | 0.00 USD | 263.54 USD | `-45.53%` | `1,452.00` |
| `Live` | `Long` | `0.1875` | 1,070,000.00 USD | 0.00 USD | 36,310.00 USD | `-43.73%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,040,000.00 USD | 0.00 USD | 632.00 USD | `-40.73%` | `3,200.00` |
| `Live` | `Long` | `0.2165` | 1,030,000.00 USD | 0.00 USD | 1,520.00 USD | `-35.03%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,030,000.00 USD | 0.00 USD | 1,000.00 USD | `-34.43%` | `4,583.00` |
| `Live` | `Long` | `0.2205` | 1,030,000.00 USD | 0.00 USD | 230.42 USD | `-33.83%` | `1,045.00` |
| `Live` | `Long` | `0.2225` | 1,030,000.00 USD | 0.00 USD | 201.14 USD | `-33.23%` | `904.00` |
| `Live` | `Long` | `0.2245` | 1,030,000.00 USD | 0.00 USD | 4,570.00 USD | `-32.63%` | `20,360.00` |
| `Live` | `Long` | `0.2295` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.13%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-30.83%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,020,000.00 USD | 0.00 USD | 2,420.00 USD | `-30.23%` | `10,412.00` |
| `Live` | `Long` | `0.2335` | 1,020,000.00 USD | 0.00 USD | 413.53 USD | `-29.93%` | `1,771.00` |
| `Live` | `Long` | `0.2345` | 1,020,000.00 USD | 0.00 USD | 5,700.00 USD | `-29.63%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 3,130.00 USD | `-29.33%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 1,010,000.00 USD | 0.00 USD | 686.56 USD | `-29.03%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 1,010,000.00 USD | 0.00 USD | 568.81 USD | `-28.73%` | `2,395.00` |
| `Live` | `Long` | `0.2395` | 1,010,000.00 USD | 0.00 USD | 151.36 USD | `-28.13%` | `632.00` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 3,790.00 USD | `-26.93%` | `15,565.00` |
| `Live` | `Long` | `0.2445` | 1,010,000.00 USD | 0.00 USD | 1,910.00 USD | `-26.63%` | `7,813.00` |
| `Live` | `Long` | `0.2455` | 1,010,000.00 USD | 0.00 USD | 384.94 USD | `-26.32%` | `1,568.00` |
| `Live` | `Long` | `0.2485` | 1,010,000.00 USD | 0.00 USD | 11,890.00 USD | `-25.42%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 993,640.00 USD | 0.00 USD | 262.02 USD | `-24.82%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 993,380.00 USD | 0.00 USD | 1,220.00 USD | `-23.32%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 992,150.00 USD | 0.00 USD | 302.96 USD | `-22.42%` | `1,172.00` |
| `Live` | `Long` | `0.2595` | 991,850.00 USD | 0.00 USD | 749.18 USD | `-22.12%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 991,100.00 USD | 0.00 USD | 107.74 USD | `-21.52%` | `412.00` |
| `Live` | `Long` | `0.2625` | 990,990.00 USD | 0.00 USD | 11,370.00 USD | `-21.22%` | `43,325.00` |
| `Live` | `Long` | `0.2645` | 979,620.00 USD | 0.00 USD | 2,650.00 USD | `-20.62%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 976,970.00 USD | 0.00 USD | 193.02 USD | `-20.32%` | `727.00` |
| `Live` | `Long` | `0.2675` | 976,770.00 USD | 0.00 USD | 321.54 USD | `-19.72%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 976,450.00 USD | 0.00 USD | 3,390.00 USD | `-19.42%` | `12,636.00` |
| `Live` | `Long` | `0.2735` | 973,060.00 USD | 0.00 USD | 220.99 USD | `-17.92%` | `808.00` |
| `Live` | `Long` | `0.2745` | 972,840.00 USD | 0.00 USD | 84,470.00 USD | `-17.62%` | `307,728.00` |
| `Live` | `Long` | `0.2785` | 888,370.00 USD | 0.00 USD | 13,170.00 USD | `-16.42%` | `47,301.00` |
| `Live` | `Long` | `0.2795` | 875,190.00 USD | 0.00 USD | 6,260.00 USD | `-16.12%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 868,940.00 USD | 0.00 USD | 13,300.00 USD | `-15.82%` | `47,408.00` |
| `Live` | `Long` | `0.2815` | 855,640.00 USD | 0.00 USD | 3,690.00 USD | `-15.52%` | `13,109.00` |
| `Live` | `Long` | `0.2825` | 851,950.00 USD | 0.00 USD | 838.74 USD | `-15.22%` | `2,969.00` |
| `Live` | `Long` | `0.2845` | 851,110.00 USD | 0.00 USD | 1,090.00 USD | `-14.62%` | `3,820.00` |
| `Live` | `Long` | `0.2855` | 850,020.00 USD | 0.00 USD | 5,880.00 USD | `-14.32%` | `20,578.00` |
| `Live` | `Long` | `0.2865` | 844,150.00 USD | 0.00 USD | 4,150.00 USD | `-14.02%` | `14,481.00` |
| `Live` | `Long` | `0.2885` | 840,000.00 USD | 0.00 USD | 4,940.00 USD | `-13.42%` | `17,126.00` |
| `Live` | `Long` | `0.2905` | 835,060.00 USD | 0.00 USD | 821.82 USD | `-12.82%` | `2,829.00` |
| `Live` | `Long` | `0.2915` | 834,240.00 USD | 0.00 USD | 954.37 USD | `-12.52%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 833,280.00 USD | 0.00 USD | 213.08 USD | `-11.92%` | `726.00` |
| `Live` | `Long` | `0.2945` | 833,070.00 USD | 0.00 USD | 124.87 USD | `-11.62%` | `424.00` |
| `Live` | `Long` | `0.2955` | 832,950.00 USD | 0.00 USD | 156.61 USD | `-11.32%` | `530.00` |
| `Live` | `Long` | `0.2965` | 832,790.00 USD | 0.00 USD | 1,010.00 USD | `-11.02%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 831,780.00 USD | 0.00 USD | 759.68 USD | `-10.42%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 831,020.00 USD | 0.00 USD | 197.37 USD | `-10.12%` | `659.00` |
| `Live` | `Long` | `0.3005` | 830,820.00 USD | 0.00 USD | 10,620.00 USD | `-9.82%` | `35,336.00` |
| `Live` | `Long` | `0.3015` | 820,210.00 USD | 0.00 USD | 102.81 USD | `-9.52%` | `341.00` |
| `Live` | `Long` | `0.3025` | 820,100.00 USD | 0.00 USD | 2,510.00 USD | `-9.22%` | `8,314.00` |
| `Live` | `Long` | `0.3035` | 817,590.00 USD | 0.00 USD | 4,040.00 USD | `-8.92%` | `13,300.00` |
| `Live` | `Long` | `0.3045` | 813,550.00 USD | 0.00 USD | 138.24 USD | `-8.62%` | `454.00` |
| `Live` | `Long` | `0.3055` | 813,410.00 USD | 0.00 USD | 14,670.00 USD | `-8.32%` | `48,026.00` |
| `Live` | `Long` | `0.3065` | 798,740.00 USD | 0.00 USD | 5,900.00 USD | `-8.02%` | `19,262.00` |
| `Live` | `Long` | `0.3075` | 792,840.00 USD | 0.00 USD | 722.62 USD | `-7.72%` | `2,350.00` |
| `Live` | `Long` | `0.3085` | 792,120.00 USD | 0.00 USD | 291.53 USD | `-7.42%` | `945.00` |
| `Live` | `Long` | `0.3095` | 791,820.00 USD | 0.00 USD | 192.51 USD | `-7.12%` | `622.00` |
| `Live` | `Long` | `0.3105` | 791,630.00 USD | 0.00 USD | 820.96 USD | `-6.82%` | `2,644.00` |
| `Live` | `Long` | `0.3115` | 790,810.00 USD | 0.00 USD | 13,600.00 USD | `-6.52%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 777,210.00 USD | 0.00 USD | 17,810.00 USD | `-6.22%` | `56,977.00` |
| `Live` | `Long` | `0.3135` | 759,400.00 USD | 0.00 USD | 446.11 USD | `-5.92%` | `1,423.00` |
| `Live` | `Long` | `0.3145` | 758,960.00 USD | 0.00 USD | 577.11 USD | `-5.62%` | `1,835.00` |
| `Live` | `Long` | `0.3155` | 758,380.00 USD | 0.00 USD | 2,960.00 USD | `-5.32%` | `9,396.00` |
| `Live` | `Long` | `0.3165` | 755,410.00 USD | 0.00 USD | 512.73 USD | `-5.02%` | `1,620.00` |
| `Live` | `Long` | `0.3175` | 754,900.00 USD | 0.00 USD | 2,290.00 USD | `-4.72%` | `7,205.00` |
| `Live` | `Long` | `0.3195` | 752,610.00 USD | 0.00 USD | 1,430.00 USD | `-4.12%` | `4,464.00` |
| `Live` | `Long` | `0.3205` | 751,190.00 USD | 0.00 USD | 455.75 USD | `-3.82%` | `1,422.00` |
| `Live` | `Long` | `0.3215` | 750,730.00 USD | 0.00 USD | 756.17 USD | `-3.52%` | `2,352.00` |
| `Live` | `Long` | `0.3235` | 749,980.00 USD | 0.00 USD | 128.43 USD | `-2.92%` | `397.00` |
| `Live` | `Long` | `0.3255` | 749,850.00 USD | 0.00 USD | 3,580.00 USD | `-2.32%` | `11,000.00` |
| `Live` | `Long` | `0.3275` | 746,270.00 USD | 0.00 USD | 163.42 USD | `-1.72%` | `499.00` |
| `Live` | `Long` | `0.3285` | 746,100.00 USD | 0.00 USD | 745,260.00 USD | `-1.42%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 839.90 USD | 0.00 USD | 839.90 USD | `-1.12%` | `2,549.00` |
| `Live` | `Short` | `0.3305` | 7,080.00 USD | 7,080.00 USD | 0.00 USD | `-0.82%` | `21,413.00` |
| `Live` | `Short` | `0.3505` | 16,710.00 USD | 9,630.00 USD | 0.00 USD | `+5.19%` | `27,477.00` |
| `Live` | `Short` | `0.3515` | 16,880.00 USD | 175.05 USD | 0.00 USD | `+5.49%` | `498.00` |
| `Live` | `Short` | `0.3635` | 48,140.00 USD | 31,260.00 USD | 0.00 USD | `+9.09%` | `85,992.00` |
| `Live` | `Short` | `0.3645` | 60,530.00 USD | 12,390.00 USD | 0.00 USD | `+9.39%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 63,650.00 USD | 3,110.00 USD | 0.00 USD | `+9.99%` | `8,498.00` |
| `Live` | `Short` | `0.3705` | 63,930.00 USD | 278.99 USD | 0.00 USD | `+11.19%` | `753.00` |
| `Live` | `Short` | `0.3725` | 64,110.00 USD | 186.25 USD | 0.00 USD | `+11.79%` | `500.00` |
| `Live` | `Short` | `0.3735` | 71,320.00 USD | 7,210.00 USD | 0.00 USD | `+12.09%` | `19,294.00` |
| `Live` | `Short` | `0.3755` | 75,350.00 USD | 4,030.00 USD | 0.00 USD | `+12.69%` | `10,732.00` |
| `Live` | `Short` | `0.3775` | 75,460.00 USD | 104.19 USD | 0.00 USD | `+13.29%` | `276.00` |
| `Live` | `Short` | `0.3785` | 631,880.00 USD | 556,430.00 USD | 0.00 USD | `+13.59%` | `1,470,083.00` |
| `Live` | `Short` | `0.3835` | 632,000.00 USD | 115.05 USD | 0.00 USD | `+15.09%` | `300.00` |
| `Live` | `Short` | `0.3855` | 632,260.00 USD | 264.84 USD | 0.00 USD | `+15.69%` | `687.00` |
| `Live` | `Short` | `0.3895` | 637,020.00 USD | 4,760.00 USD | 0.00 USD | `+16.89%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 643,020.00 USD | 6,000.00 USD | 0.00 USD | `+17.19%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 644,500.00 USD | 1,480.00 USD | 0.00 USD | `+18.09%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 762,630.00 USD | 118,130.00 USD | 0.00 USD | `+18.39%` | `299,436.00` |
| `Live` | `Short` | `0.3955` | 2,160,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+18.69%` | `3,526,740.00` |
| `Live` | `Short` | `0.4025` | 2,160,000.00 USD | 328.44 USD | 0.00 USD | `+20.79%` | `816.00` |
| `Live` | `Short` | `0.4085` | 2,160,000.00 USD | 170.75 USD | 0.00 USD | `+22.59%` | `418.00` |
| `Live` | `Short` | `0.4095` | 2,160,000.00 USD | 239.56 USD | 0.00 USD | `+22.89%` | `585.00` |
| `Live` | `Short` | `0.4185` | 2,160,000.00 USD | 998.96 USD | 0.00 USD | `+25.59%` | `2,387.00` |
| `Live` | `Short` | `0.4245` | 2,160,000.00 USD | 134.57 USD | 0.00 USD | `+27.39%` | `317.00` |
| `Live` | `Short` | `0.4255` | 2,160,000.00 USD | 3,940.00 USD | 0.00 USD | `+27.69%` | `9,259.00` |
| `Live` | `Short` | `0.4295` | 2,170,000.00 USD | 10,210.00 USD | 0.00 USD | `+28.89%` | `23,779.00` |
| `Live` | `Short` | `0.4325` | 2,170,000.00 USD | 1,500.00 USD | 0.00 USD | `+29.79%` | `3,464.00` |
| `Live` | `Short` | `0.4355` | 2,250,000.00 USD | 70,890.00 USD | 0.00 USD | `+30.69%` | `162,775.00` |
| `Live` | `Short` | `0.4365` | 2,250,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.99%` | `3,416.00` |
| `Live` | `Short` | `0.4415` | 2,250,000.00 USD | 377.48 USD | 0.00 USD | `+32.50%` | `855.00` |
| `Live` | `Short` | `0.4445` | 2,270,000.00 USD | 22,230.00 USD | 0.00 USD | `+33.40%` | `50,000.00` |
| `Live` | `Short` | `0.4455` | 2,270,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.70%` | `2,284.00` |
| `Live` | `Short` | `0.4465` | 2,280,000.00 USD | 5,520.00 USD | 0.00 USD | `+34.00%` | `12,352.00` |
| `Live` | `Short` | `0.4475` | 2,340,000.00 USD | 65,610.00 USD | 0.00 USD | `+34.30%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 2,340,000.00 USD | 318.76 USD | 0.00 USD | `+35.50%` | `706.00` |
| `Live` | `Short` | `0.4715` | 2,340,000.00 USD | 272.53 USD | 0.00 USD | `+41.50%` | `578.00` |
| `Live` | `Short` | `0.4805` | 2,350,000.00 USD | 2,880.00 USD | 0.00 USD | `+44.20%` | `6,000.00` |
| `Live` | `Short` | `0.4895` | 2,350,000.00 USD | 839.49 USD | 0.00 USD | `+46.90%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,350,000.00 USD | 5,120.00 USD | 0.00 USD | `+47.20%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,350,000.00 USD | 2,730.00 USD | 0.00 USD | `+49.90%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,380,000.00 USD | 23,320.00 USD | 0.00 USD | `+50.20%` | `46,591.00` |
| `Live` | `Short` | `0.5325` | 2,380,000.00 USD | 667.22 USD | 0.00 USD | `+59.80%` | `1,253.00` |
| `Live` | `Short` | `0.5465` | 2,420,000.00 USD | 40,440.00 USD | 0.00 USD | `+64.01%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,420,000.00 USD | 3,060.00 USD | 0.00 USD | `+67.31%` | `5,483.00` |
| `Live` | `Short` | `0.5605` | 2,420,000.00 USD | 140.12 USD | 0.00 USD | `+68.21%` | `250.00` |
| `Live` | `Short` | `0.5725` | 3,160,000.00 USD | 742,670.00 USD | 0.00 USD | `+71.81%` | `1,297,248.00` |
| `Live` | `Short` | `0.6155` | 3,190,000.00 USD | 24,620.00 USD | 0.00 USD | `+84.71%` | `40,000.00` |
| `Live` | `Short` | `0.6205` | 3,190,000.00 USD | 375.40 USD | 0.00 USD | `+86.21%` | `605.00` |
| `Live` | `Short` | `0.6275` | 3,190,000.00 USD | 1,130.00 USD | 0.00 USD | `+88.31%` | `1,808.00` |
| `Live` | `Short` | `0.6335` | 3,200,000.00 USD | 6,810.00 USD | 0.00 USD | `+90.11%` | `10,756.00` |
| `Live` | `Short` | `0.6505` | 3,300,000.00 USD | 102,000.00 USD | 0.00 USD | `+95.22%` | `156,809.00` |
| `Live` | `Short` | `0.6515` | 3,300,000.00 USD | 951.19 USD | 0.00 USD | `+95.52%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 3,300,000.00 USD | 705.13 USD | 0.00 USD | `+96.12%` | `1,079.00` |
| `Live` | `Short` | `0.6615` | 3,300,000.00 USD | 2,060.00 USD | 0.00 USD | `+98.52%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,310,000.00 USD | 3,740.00 USD | 0.00 USD | `+99.12%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0925` | 1,990,000.00 USD | 0.00 USD | 407.56 USD | `-72.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 1,990,000.00 USD | 0.00 USD | 198.45 USD | `-71.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 1,990,000.00 USD | 0.00 USD | 330.26 USD | `-57.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,990,000.00 USD | 0.00 USD | 1,750.00 USD | `-38.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,990,000.00 USD | 0.00 USD | 579.72 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 1,990,000.00 USD | 0.00 USD | 515.61 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,990,000.00 USD | 0.00 USD | 121.70 USD | `-30.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,990,000.00 USD | 0.00 USD | 705.61 USD | `-29.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 1,990,000.00 USD | 0.00 USD | 159.20 USD | `-29.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,990,000.00 USD | 0.00 USD | 1,200.00 USD | `-27.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,990,000.00 USD | 0.00 USD | 127.51 USD | `-27.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,990,000.00 USD | 0.00 USD | 1,850.00 USD | `-24.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 1,990,000.00 USD | 0.00 USD | 41,500.00 USD | `-24.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 1,950,000.00 USD | 0.00 USD | 1,920.00 USD | `-23.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 1,940,000.00 USD | 0.00 USD | 664.01 USD | `-21.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 1,940,000.00 USD | 0.00 USD | 954.98 USD | `-21.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 1,940,000.00 USD | 0.00 USD | 103.56 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 1,940,000.00 USD | 0.00 USD | 695.50 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 1,940,000.00 USD | 0.00 USD | 1,630.00 USD | `-19.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 1,940,000.00 USD | 0.00 USD | 1,470.00 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 1,940,000.00 USD | 0.00 USD | 101.94 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 1,940,000.00 USD | 0.00 USD | 3,260.00 USD | `-16.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 1,930,000.00 USD | 0.00 USD | 2,550.00 USD | `-15.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 1,930,000.00 USD | 0.00 USD | 229.92 USD | `-14.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 1,930,000.00 USD | 0.00 USD | 8,010.00 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 1,920,000.00 USD | 0.00 USD | 11,610.00 USD | `-11.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 1,910,000.00 USD | 0.00 USD | 111.19 USD | `-11.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 1,910,000.00 USD | 0.00 USD | 433.42 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 1,910,000.00 USD | 0.00 USD | 2,710.00 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 1,910,000.00 USD | 0.00 USD | 503.95 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 1,910,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 1,910,000.00 USD | 0.00 USD | 193.11 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 1,910,000.00 USD | 0.00 USD | 15,150.00 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 1,890,000.00 USD | 0.00 USD | 156.30 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 1,890,000.00 USD | 0.00 USD | 12,200.00 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 1,880,000.00 USD | 0.00 USD | 6,530.00 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 1,870,000.00 USD | 0.00 USD | 524,570.00 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 1,350,000.00 USD | 0.00 USD | 1,270.00 USD | `-5.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 1,350,000.00 USD | 0.00 USD | 53,690.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 1,290,000.00 USD | 0.00 USD | 2,770.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 1,290,000.00 USD | 0.00 USD | 6,100.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 1,280,000.00 USD | 0.00 USD | 850.90 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 1,280,000.00 USD | 0.00 USD | 1,160.00 USD | `-4.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 1,280,000.00 USD | 0.00 USD | 6,220.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 1,280,000.00 USD | 0.00 USD | 10,160.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 1,270,000.00 USD | 0.00 USD | 43,760.00 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 1,220,000.00 USD | 0.00 USD | 5,520.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 1,220,000.00 USD | 0.00 USD | 7,040.00 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 1,210,000.00 USD | 0.00 USD | 3,870.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 1,210,000.00 USD | 0.00 USD | 2,240.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 1,200,000.00 USD | 0.00 USD | 6,130.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 1,200,000.00 USD | 0.00 USD | 7,620.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 1,190,000.00 USD | 0.00 USD | 4,270.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 1,190,000.00 USD | 0.00 USD | 1,770.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 1,180,000.00 USD | 0.00 USD | 949.53 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 5,730.00 USD | 0.00 USD | 5,730.00 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 4,880.00 USD | 4,880.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 5,440.00 USD | 560.96 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 13,700.00 USD | 8,260.00 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 13,960.00 USD | 265.50 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 15,990.00 USD | 2,020.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 17,430.00 USD | 1,450.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 24,350.00 USD | 6,910.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 25,800.00 USD | 1,460.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 26,290.00 USD | 486.30 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 26,720.00 USD | 431.55 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 27,550.00 USD | 828.18 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 28,040.00 USD | 488.16 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 28,470.00 USD | 435.33 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 29,030.00 USD | 555.44 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 29,300.00 USD | 274.18 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 29,740.00 USD | 439.11 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 31,690.00 USD | 1,950.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 32,360.00 USD | 665.60 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 32,960.00 USD | 605.63 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 41,660.00 USD | 8,690.00 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 41,970.00 USD | 312.14 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 42,320.00 USD | 354.50 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 42,460.00 USD | 132.96 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 81,890.00 USD | 39,430.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 122,280.00 USD | 40,390.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 125,580.00 USD | 3,310.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 126,620.00 USD | 1,030.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 129,560.00 USD | 2,940.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 129,780.00 USD | 224.49 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 129,880.00 USD | 103.23 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 132,580.00 USD | 2,700.00 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 174,320.00 USD | 41,740.00 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 174,580.00 USD | 256.55 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 174,750.00 USD | 172.72 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 174,970.00 USD | 218.89 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 189,300.00 USD | 14,330.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 189,900.00 USD | 597.99 USD | 0.00 USD | `+11.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 190,080.00 USD | 174.60 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 190,180.00 USD | 107.28 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 190,620.00 USD | 439.61 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 191,060.00 USD | 437.79 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 193,690.00 USD | 2,630.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 193,880.00 USD | 182.60 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 200,330.00 USD | 6,450.00 USD | 0.00 USD | `+13.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 200,600.00 USD | 275.17 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 201,170.00 USD | 569.25 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 207,150.00 USD | 5,980.00 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 207,410.00 USD | 257.89 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 207,670.00 USD | 262.78 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 207,890.00 USD | 224.73 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 208,510.00 USD | 621.04 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 209,260.00 USD | 742.08 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 210,370.00 USD | 1,110.00 USD | 0.00 USD | `+16.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 210,550.00 USD | 181.04 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 1,580,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 1,580,000.00 USD | 138.63 USD | 0.00 USD | `+17.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 1,590,000.00 USD | 276.40 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 1,590,000.00 USD | 126.24 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 1,590,000.00 USD | 2,400.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 1,590,000.00 USD | 1,410.00 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 1,590,000.00 USD | 1,200.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 1,660,000.00 USD | 71,490.00 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 1,660,000.00 USD | 864.28 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 1,670,000.00 USD | 3,920.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 1,750,000.00 USD | 79,330.00 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 1,750,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 1,750,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 1,750,000.00 USD | 138.07 USD | 0.00 USD | `+22.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 1,750,000.00 USD | 1,270.00 USD | 0.00 USD | `+22.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 1,750,000.00 USD | 331.63 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 1,750,000.00 USD | 313.54 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 1,750,000.00 USD | 186.70 USD | 0.00 USD | `+26.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 1,750,000.00 USD | 325.75 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 1,750,000.00 USD | 183.82 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 1,750,000.00 USD | 299.19 USD | 0.00 USD | `+30.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 1,790,000.00 USD | 38,580.00 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 1,790,000.00 USD | 170.69 USD | 0.00 USD | `+33.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 1,790,000.00 USD | 135.59 USD | 0.00 USD | `+34.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 1,790,000.00 USD | 1,520.00 USD | 0.00 USD | `+34.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 1,790,000.00 USD | 320.31 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 1,800,000.00 USD | 5,340.00 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 1,800,000.00 USD | 1,470.00 USD | 0.00 USD | `+38.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 1,880,000.00 USD | 80,770.00 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 1,880,000.00 USD | 169.22 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 1,880,000.00 USD | 153.79 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 1,880,000.00 USD | 724.89 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 1,890,000.00 USD | 11,150.00 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 1,890,000.00 USD | 1,930.00 USD | 0.00 USD | `+51.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5175` | 1,900,000.00 USD | 2,280.00 USD | 0.00 USD | `+55.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 1,900,000.00 USD | 135.02 USD | 0.00 USD | `+58.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6255` | 1,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 1,900,000.00 USD | 240.85 USD | 0.00 USD | `+89.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 1,900,000.00 USD | 1,100.00 USD | 0.00 USD | `+89.81%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2953` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 82,110.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 109,100.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 20,300,000.00 USD | 0.00 USD | 20,300,000.00 USD | 122,490.00 USD | 38,150.00 USD | 60,970.00 USD |
| `7D` | `0.2971` | 20,070,000.00 USD | 0.00 USD | 20,070,000.00 USD | 88,760.00 USD | 36,460.00 USD | 52,660.00 USD |
| `1D` | `0.2974` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 167.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `0.2977` | 19,900,000.00 USD | 0.00 USD | 19,900,000.00 USD | 53,840.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2978` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 17,600.00 USD | 3,340.00 USD | 4,250.00 USD |
| `1D` | `0.2982` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 26,560.00 USD | 7,720.00 USD | 17,280.00 USD |
| `7D` | `0.2983` | 19,810,000.00 USD | 0.00 USD | 19,810,000.00 USD | 170,390.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2986` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 102,450.00 USD | 9,300.00 USD | 7,900.00 USD |
| `7D` | `0.2989` | 19,580,000.00 USD | 0.00 USD | 19,580,000.00 USD | 109,910.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2990` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 50,390.00 USD | 0.00 USD | 8,790.00 USD |
| `1D` | `0.2994` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 19,550.00 USD | 37,800.00 USD | 85,870.00 USD |
| `7D` | `0.2995` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 6,450.00 USD | 62,740.00 USD | 80,320.00 USD |
| `1D` | `0.2998` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 9,360.00 USD | 24,820.00 USD | 17,040.00 USD |
| `7D` | `0.3001` | 19,280,000.00 USD | 0.00 USD | 19,280,000.00 USD | 2,360.00 USD | 15,390.00 USD | 62,490.00 USD |
| `1D` | `0.3002` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 15,600.00 USD | 20,670.00 USD | 24,520.00 USD |
| `1D` | `0.3006` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 848.70 USD | 1,800.00 USD | 24,520.00 USD |
| `7D` | `0.3007` | 19,200,000.00 USD | 0.00 USD | 19,200,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3010` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 34,290.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.3013` | 19,160,000.00 USD | 0.00 USD | 19,160,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3014` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 17,320.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.3018` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 1,630.00 USD | 6,650.00 USD | 16,590.00 USD |
| `7D` | `0.3019` | 19,160,000.00 USD | 0.00 USD | 19,160,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3022` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 14,930.00 USD | 6,590.00 USD | 0.00 USD |
| `7D` | `0.3025` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD |
| `1D` | `0.3026` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3030` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 24,620.00 USD | 8,320.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3034` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 742.30 USD | 0.00 USD | 12,600.00 USD |
| `7D` | `0.3037` | 19,090,000.00 USD | 0.00 USD | 19,090,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3038` | 13,600,000.00 USD | 0.00 USD | 13,600,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD |
| `1D` | `0.3042` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 537.63 USD | 9,300.00 USD | 56,350.00 USD |
| `7D` | `0.3043` | 19,080,000.00 USD | 0.00 USD | 19,080,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3046` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 31,710.00 USD | 18,130.00 USD | 7,480.00 USD |
| `7D` | `0.3049` | 19,080,000.00 USD | 0.00 USD | 19,080,000.00 USD | 18,020.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3050` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 165.80 USD | 8,990.00 USD | 53,820.00 USD |
| `1D` | `0.3054` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 46,820.00 USD | 13,380.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3061` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 32,680.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3062` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 885.25 USD | 2,350.00 USD | 56,460.00 USD |
| `1D` | `0.3066` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 31,110.00 USD | 29,620.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 6,500.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3070` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD |
| `7D` | `0.3073` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 7,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3074` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3079` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 38,320.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3082` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 18,640.00 USD | 0.00 USD | 12,250.00 USD |
| `7D` | `0.3085` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 2,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3086` | 13,080,000.00 USD | 0.00 USD | 13,080,000.00 USD | 363.64 USD | 0.00 USD | 15,810.00 USD |
| `1D` | `0.3090` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 8,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3094` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 75,040.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3098` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 7,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3102` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 57,870.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 18,650,000.00 USD | 0.00 USD | 18,650,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3106` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 6,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3114` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 977.81 USD | 9,110.00 USD | 0.00 USD |
| `7D` | `0.3115` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 10,340.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3118` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 14,500.00 USD | 8,100.00 USD | 17,620.00 USD |
| `7D` | `0.3121` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 162,580.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3122` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 13,610.00 USD | 2,560.00 USD | 33,830.00 USD |
| `1D` | `0.3126` | 12,820,000.00 USD | 0.00 USD | 12,820,000.00 USD | 12,430.00 USD | 13,530.00 USD | 7,580.00 USD |
| `7D` | `0.3127` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 21,180.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3130` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 2,430.00 USD | 28,470.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 5,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3134` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 5,000.00 USD | 23,940.00 USD | 9,590.00 USD |
| `1D` | `0.3138` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 5,650.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3142` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 4,220.00 USD | 3,580.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 247,810.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3146` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 1,850.00 USD | 2,330.00 USD | 0.00 USD |
| `1D` | `0.3150` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 4,810.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 196,920.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3154` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 27,150.00 USD | 1,850.00 USD | 0.00 USD |
| `7D` | `0.3157` | 17,560,000.00 USD | 0.00 USD | 17,560,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3158` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 10,540.00 USD | 1,830.00 USD | 16,240.00 USD |
| `1D` | `0.3162` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 5,670.00 USD | 5,180.00 USD | 0.00 USD |
| `7D` | `0.3163` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3166` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 43,210.00 USD | 35,060.00 USD | 17,210.00 USD |
| `7D` | `0.3169` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 417,380.00 USD | 106,680.00 USD | 135,950.00 USD |
| `1D` | `0.3170` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 6,720.00 USD | 35,130.00 USD | 18,370.00 USD |
| `1D` | `0.3174` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 21,050.00 USD | 7,370.00 USD | 31,150.00 USD |
| `7D` | `0.3175` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3178` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 59,190.00 USD | 9,500.00 USD | 32,130.00 USD |
| `7D` | `0.3181` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 751,290.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3182` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 329,920.00 USD | 43,320.00 USD | 82,320.00 USD |
| `1D` | `0.3186` | 11,790,000.00 USD | 0.00 USD | 11,790,000.00 USD | 80,290.00 USD | 54,030.00 USD | 44,470.00 USD |
| `7D` | `0.3187` | 14,230,000.00 USD | 0.00 USD | 14,230,000.00 USD | 408,400.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3190` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 191,070.00 USD | 0.00 USD | 56,530.00 USD |
| `7D` | `0.3193` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 118,210.00 USD | 104,710.00 USD | 247,300.00 USD |
| `1D` | `0.3194` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 150,770.00 USD | 117,490.00 USD | 267,590.00 USD |
| `1D` | `0.3198` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 84,870.00 USD | 108,400.00 USD | 64,920.00 USD |
| `7D` | `0.3199` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 0.00 USD | 127,390.00 USD | 190,470.00 USD |
| `1D` | `0.3202` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 219,620.00 USD | 63,290.00 USD | 122,200.00 USD |
| `7D` | `0.3205` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 100,160.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3206` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 127,850.00 USD | 16,080.00 USD | 119,210.00 USD |
| `1D` | `0.3210` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 88,620.00 USD | 31,880.00 USD | 38,170.00 USD |
| `7D` | `0.3211` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 569,720.00 USD | 117,230.00 USD | 244,340.00 USD |
| `1D` | `0.3214` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 53,360.00 USD | 45,170.00 USD | 83,510.00 USD |
| `7D` | `0.3217` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 286,830.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3218` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 5,550.00 USD | 28,050.00 USD | 87,330.00 USD |
| `1D` | `0.3222` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 154,560.00 USD | 24,690.00 USD | 69,480.00 USD |
| `7D` | `0.3223` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD |
| `1D` | `0.3226` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 13,670.00 USD | 24,400.00 USD | 188,740.00 USD |
| `7D` | `0.3229` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 858,070.00 USD | 299,190.00 USD | 385,680.00 USD |
| `1D` | `0.3230` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 92,790.00 USD | 46,020.00 USD | 86,810.00 USD |
| `1D` | `0.3234` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 61,120.00 USD | 72,090.00 USD | 93,070.00 USD |
| `7D` | `0.3235` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 709,160.00 USD | 213,370.00 USD | 359,100.00 USD |
| `1D` | `0.3238` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 0.00 USD | 53,490.00 USD | 138,410.00 USD |
| `7D` | `0.3241` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 433,820.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3242` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 97,850.00 USD | 17,220.00 USD | 231,720.00 USD |
| `1D` | `0.3246` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 256,230.00 USD | 90,310.00 USD | 171,640.00 USD |
| `7D` | `0.3247` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3250` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 758,560.00 USD | 89,640.00 USD | 318,030.00 USD |
| `7D` | `0.3253` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD |
| `1D` | `0.3254` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 340,830.00 USD | 61,360.00 USD | 299,050.00 USD |
| `1D` | `0.3258` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 373,570.00 USD | 71,210.00 USD | 143,750.00 USD |
| `7D` | `0.3259` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 182,240.00 USD | 250,110.00 USD | 503,650.00 USD |
| `1D` | `0.3262` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 115,280.00 USD | 378,600.00 USD | 505,960.00 USD |
| `7D` | `0.3265` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 80,160.00 USD | 197,270.00 USD | 347,150.00 USD |
| `1D` | `0.3266` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 44,720.00 USD | 157,840.00 USD | 354,040.00 USD |
| `1D` | `0.3270` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 237,730.00 USD | 115,770.00 USD | 350,550.00 USD |
| `7D` | `0.3271` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 192,500.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3274` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 155,490.00 USD | 61,310.00 USD | 202,370.00 USD |
| `7D` | `0.3277` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3278` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 268,410.00 USD | 32,310.00 USD | 133,800.00 USD |
| `1D` | `0.3282` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 61,320.00 USD | 16,760.00 USD |
| `7D` | `0.3283` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3286` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 45,960.00 USD | 39,260.00 USD | 113,560.00 USD |
| `7D` | `0.3289` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3290` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 109,890.00 USD | 44,530.00 USD | 72,140.00 USD |
| `1D` | `0.3294` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 61,960.00 USD | 26,090.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 255,850.00 USD | 83,080.00 USD | 0.00 USD |
| `1D` | `0.3298` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 105,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3301` | 774,520.00 USD | 0.00 USD | 774,520.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3302` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 37,670.00 USD | 58,700.00 USD | 93,930.00 USD |
| `1D` | `0.3306` | 917,340.00 USD | 0.00 USD | 917,340.00 USD | 110,810.00 USD | 16,160.00 USD | 11,710.00 USD |
| `7D` | `0.3307` | 581,350.00 USD | 0.00 USD | 581,350.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3310` | 778,660.00 USD | 0.00 USD | 778,660.00 USD | 11,600.00 USD | 122,460.00 USD | 444,920.00 USD |
| `7D` | `0.3313` | 108,550.00 USD | 0.00 USD | 108,550.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3314` | 199,680.00 USD | 0.00 USD | 199,680.00 USD | 0.00 USD | 54,160.00 USD | 86,570.00 USD |
| `1D` | `0.3318` | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD |
| `7D` | `0.3319` | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD |
| `7D` | `0.3323` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3339` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3358` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD |
| `1D` | `0.3370` | 217,200.00 USD | 217,200.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3374` | 546,840.00 USD | 546,840.00 USD | 0.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3379` | 21,390.00 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD |
| `1D` | `0.3382` | 618,740.00 USD | 618,740.00 USD | 0.00 USD | 71,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3385` | 147,040.00 USD | 147,040.00 USD | 0.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3386` | 778,070.00 USD | 778,070.00 USD | 0.00 USD | 92,750.00 USD | 11,160.00 USD | 55,410.00 USD |
| `1D` | `0.3390` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 302,930.00 USD | 27,820.00 USD | 49,390.00 USD |
| `7D` | `0.3391` | 381,700.00 USD | 381,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD |
| `1D` | `0.3394` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 115,280.00 USD | 200,920.00 USD | 485,780.00 USD |
| `7D` | `0.3397` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 262,880.00 USD | 586,760.00 USD | 410,790.00 USD |
| `1D` | `0.3398` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 43,780.00 USD | 216,810.00 USD | 129,840.00 USD |
| `1D` | `0.3402` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 20,340.00 USD | 97,740.00 USD | 374,530.00 USD |
| `7D` | `0.3403` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD |
| `1D` | `0.3406` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 260,970.00 USD | 0.00 USD | 150,300.00 USD |
| `7D` | `0.3409` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3410` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 257,330.00 USD | 34,110.00 USD | 27,700.00 USD |
| `1D` | `0.3414` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 376,520.00 USD | 27,220.00 USD | 97,590.00 USD |
| `7D` | `0.3415` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD |
| `1D` | `0.3418` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 343,500.00 USD | 32,360.00 USD | 27,870.00 USD |
| `7D` | `0.3421` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3422` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 71,180.00 USD | 31,660.00 USD | 0.00 USD |
| `1D` | `0.3426` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 156,700.00 USD | 0.00 USD |
| `7D` | `0.3427` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD |
| `1D` | `0.3430` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 166,310.00 USD | 220,760.00 USD | 0.00 USD |
| `7D` | `0.3433` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3434` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 83,080.00 USD | 30,950.00 USD |
| `1D` | `0.3438` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 49,600.00 USD | 62,980.00 USD |
| `1D` | `0.3442` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 51,170.00 USD | 0.00 USD |
| `7D` | `0.3445` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3446` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 60,100.00 USD | 106,240.00 USD |
| `1D` | `0.3450` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 35,950.00 USD | 45,930.00 USD | 119,850.00 USD |
| `7D` | `0.3451` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD |
| `1D` | `0.3454` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 126,310.00 USD | 54,930.00 USD | 106,680.00 USD |
| `7D` | `0.3457` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3458` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 159,870.00 USD | 100,770.00 USD | 507,890.00 USD |
| `1D` | `0.3462` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 168,310.00 USD | 124,400.00 USD | 142,100.00 USD |
| `7D` | `0.3463` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 167,950.00 USD | 205,390.00 USD |
| `1D` | `0.3466` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 21,890.00 USD | 65,550.00 USD | 106,440.00 USD |
| `7D` | `0.3469` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD |
| `1D` | `0.3470` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 37,620.00 USD | 36,280.00 USD | 61,300.00 USD |
| `1D` | `0.3474` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 42,560.00 USD | 31,160.00 USD |
| `7D` | `0.3475` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3478` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 51,860.00 USD | 40,550.00 USD | 134,270.00 USD |
| `7D` | `0.3481` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 6,440.00 USD | 14,700.00 USD | 42,810.00 USD |
| `1D` | `0.3482` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 56,790.00 USD | 20,460.00 USD | 8,380.00 USD |
| `1D` | `0.3486` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 7,190.00 USD | 32,250.00 USD | 0.00 USD |
| `7D` | `0.3487` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3490` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 40,230.00 USD | 10,900.00 USD | 61,240.00 USD |
| `7D` | `0.3493` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD |
| `1D` | `0.3494` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 5,420.00 USD | 24,400.00 USD | 79,030.00 USD |
| `1D` | `0.3498` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 83,150.00 USD | 0.00 USD | 375,650.00 USD |
| `7D` | `0.3499` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 133,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3502` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD |
| `7D` | `0.3505` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 12,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3506` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 74,220.00 USD | 0.00 USD | 31,490.00 USD |
| `1D` | `0.3510` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 2,790.00 USD | 12,400.00 USD | 32,490.00 USD |
| `7D` | `0.3511` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3514` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 21,910.00 USD | 0.00 USD | 73,170.00 USD |
| `7D` | `0.3517` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3518` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 30,510.00 USD | 11,560.00 USD | 42,500.00 USD |
| `1D` | `0.3522` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 2,260.00 USD | 16,140.00 USD | 0.00 USD |
| `7D` | `0.3523` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD |
| `1D` | `0.3526` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 5,360.00 USD | 6,280.00 USD | 28,910.00 USD |
| `1D` | `0.3530` | 9,410,000.00 USD | 9,410,000.00 USD | 0.00 USD | 101,220.00 USD | 52,710.00 USD | 88,110.00 USD |
| `1D` | `0.3534` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 127,850.00 USD | 56,820.00 USD | 87,200.00 USD |
| `7D` | `0.3535` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3538` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 3,230.00 USD | 21,150.00 USD | 108,070.00 USD |
| `7D` | `0.3541` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 799,020.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3542` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 83,710.00 USD | 84,150.00 USD | 37,920.00 USD |
| `1D` | `0.3546` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 5,090.00 USD | 51,930.00 USD | 31,910.00 USD |
| `7D` | `0.3547` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3550` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 2,710.00 USD | 42,500.00 USD | 0.00 USD |
| `7D` | `0.3553` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3554` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 21,530.00 USD | 40,120.00 USD | 47,950.00 USD |
| `1D` | `0.3558` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 331.60 USD | 25,350.00 USD | 30,620.00 USD |
| `7D` | `0.3559` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3562` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 977.81 USD | 17,880.00 USD | 115,040.00 USD |
| `7D` | `0.3565` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3566` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 2,090.00 USD | 11,630.00 USD | 0.00 USD |
| `1D` | `0.3570` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `0.3571` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3574` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 131,860.00 USD | 9,250.00 USD | 0.00 USD |
| `7D` | `0.3577` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3578` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 31,190.00 USD | 9,130.00 USD | 27,240.00 USD |
| `1D` | `0.3582` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 2,980.00 USD | 14,930.00 USD | 11,710.00 USD |
| `7D` | `0.3583` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3586` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 17,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3589` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3590` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 3,780.00 USD | 15,750.00 USD | 33,590.00 USD |
| `1D` | `0.3594` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 111,740.00 USD | 0.00 USD | 99,590.00 USD |
| `7D` | `0.3595` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3598` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 46,200.00 USD | 22,780.00 USD | 64,450.00 USD |
| `7D` | `0.3601` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 4,040.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3602` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 32,190.00 USD | 32,480.00 USD | 136,650.00 USD |
| `1D` | `0.3606` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 30,100.00 USD | 26,580.00 USD | 157,390.00 USD |
| `7D` | `0.3607` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 330,200.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3610` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 75,090.00 USD | 45,020.00 USD | 100,930.00 USD |
| `7D` | `0.3613` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 77,710.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3614` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 10,940.00 USD | 40,360.00 USD | 135,700.00 USD |
| `1D` | `0.3618` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 225,600.00 USD | 56,810.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 3,500.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3622` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 169,910.00 USD | 69,640.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 2,410.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3626` | 12,780,000.00 USD | 12,780,000.00 USD | 0.00 USD | 73,050.00 USD | 49,330.00 USD | 0.00 USD |
| `1D` | `0.3630` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 1,120,000.00 USD | 93,320.00 USD | 79,610.00 USD |
| `7D` | `0.3631` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 678.26 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3634` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 144,090.00 USD | 14,760.00 USD | 199,780.00 USD |
| `7D` | `0.3637` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 937.01 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3638` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 183,690.00 USD | 65,110.00 USD | 76,240.00 USD |
| `1D` | `0.3642` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 103,140.00 USD | 206,820.00 USD | 35,280.00 USD |
| `7D` | `0.3643` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3646` | 15,480,000.00 USD | 15,480,000.00 USD | 0.00 USD | 333,280.00 USD | 21,220.00 USD | 26,970.00 USD |
| `7D` | `0.3649` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 177,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3650` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 2,410.00 USD | 55,120.00 USD | 168,850.00 USD |
| `1D` | `0.3654` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 405,500.00 USD | 47,350.00 USD | 165,330.00 USD |
| `7D` | `0.3655` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3658` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 240,260.00 USD | 152,790.00 USD | 203,990.00 USD |
| `7D` | `0.3661` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 685,520.00 USD | 60,550.00 USD | 238,480.00 USD |
| `1D` | `0.3662` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 161,450.00 USD | 61,740.00 USD | 55,630.00 USD |
| `1D` | `0.3666` | 17,860,000.00 USD | 17,860,000.00 USD | 0.00 USD | 475,420.00 USD | 119,560.00 USD | 66,840.00 USD |
| `7D` | `0.3667` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 422,610.00 USD | 15,390.00 USD | 135,630.00 USD |
| `1D` | `0.3670` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 94,630.00 USD | 66,280.00 USD | 318,570.00 USD |
| `7D` | `0.3673` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 512,420.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3674` | 18,600,000.00 USD | 18,600,000.00 USD | 0.00 USD | 41,190.00 USD | 72,620.00 USD | 148,060.00 USD |
| `1D` | `0.3678` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 517,910.00 USD | 34,010.00 USD | 164,260.00 USD |
| `7D` | `0.3679` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 259,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3682` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 286,630.00 USD | 82,130.00 USD | 148,400.00 USD |
| `7D` | `0.3685` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 4,100.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3686` | 20,400,000.00 USD | 20,400,000.00 USD | 0.00 USD | 327,450.00 USD | 153,840.00 USD | 81,460.00 USD |
| `1D` | `0.3690` | 20,930,000.00 USD | 20,930,000.00 USD | 0.00 USD | 475,810.00 USD | 51,700.00 USD | 0.00 USD |
| `7D` | `0.3691` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3694` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 154,310.00 USD | 72,220.00 USD | 23,760.00 USD |
| `7D` | `0.3697` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 163,180.00 USD | 0.00 USD |
| `1D` | `0.3698` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 170,350.00 USD | 15,980.00 USD | 0.00 USD |
| `1D` | `0.3702` | 22,020,000.00 USD | 22,020,000.00 USD | 0.00 USD | 438,600.00 USD | 196,170.00 USD | 27,870.00 USD |
| `7D` | `0.3703` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3706` | 22,780,000.00 USD | 22,780,000.00 USD | 0.00 USD | 177,000.00 USD | 8,320.00 USD | 573,510.00 USD |
| `7D` | `0.3709` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3710` | 22,970,000.00 USD | 22,970,000.00 USD | 0.00 USD | 110,310.00 USD | 42,590.00 USD | 38,120.00 USD |
| `1D` | `0.3714` | 24,360,000.00 USD | 24,360,000.00 USD | 0.00 USD | 489,730.00 USD | 116,180.00 USD | 783,780.00 USD |
| `7D` | `0.3715` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 4,580.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3718` | 24,860,000.00 USD | 24,860,000.00 USD | 0.00 USD | 36,200.00 USD | 182,160.00 USD | 274,660.00 USD |
| `7D` | `0.3721` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3722` | 25,170,000.00 USD | 25,170,000.00 USD | 0.00 USD | 185,610.00 USD | 68,140.00 USD | 62,210.00 USD |
| `7D` | `0.3727` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD |
| `7D` | `0.3733` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 242,460.00 USD | 7,690.00 USD | 218,010.00 USD |
| `7D` | `0.3745` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD |
| `7D` | `0.3751` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3757` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD |
| `7D` | `0.3763` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `7D` | `0.3769` | 19,430,000.00 USD | 19,430,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 19,450,000.00 USD | 19,450,000.00 USD | 0.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 19,600,000.00 USD | 19,600,000.00 USD | 0.00 USD | 90,150.00 USD | 3,620.00 USD | 54,360.00 USD |
| `7D` | `0.3793` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `7D` | `0.3811` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `0.3817` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `7D` | `0.3823` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `7D` | `0.3853` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 535.97 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3859` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 103,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3925` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 27,520.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 21,970.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 24,790.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 109,810.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 107,070.00 USD | 10,160.00 USD | 110,780.00 USD |
| `7D` | `0.3961` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 122,550.00 USD | 54,030.00 USD | 7,040.00 USD |
| `7D` | `0.3967` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 12,300.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 22,070,000.00 USD | 22,070,000.00 USD | 0.00 USD | 16,660.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 22,180,000.00 USD | 22,180,000.00 USD | 0.00 USD | 57,690.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 22,220,000.00 USD | 22,220,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD |
| `7D` | `0.3997` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD |
| `7D` | `0.4001` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `421.56M` | Total OI Tokens: `1,258,031,235.6 TRX`
  * 1h OI Change: `+3.57%` | 4h OI Change: `+2.76%` | 24h OI Change: `+47.33%`
  * Exchange Breakdown: Binance=`106.72M` | Bybit=`84.30M` | OKX=`27.09M` | Hyperliquid=`18.64M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-5.57K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0243%` | **USDT OKX** | `-0.3327%` |
| **USDT Bybit** | `0.1191%` | **USDT KuCoin** | `-0.0618%` |
| **USDT MEXC** | `-0.0226%` | **USDT BingX** | `0.1130%` |
| **USDT Gate** | `-0.1381%` | **USDT Bitget** | `-0.1989%` |
| **CoinM Binance** | `-0.0776%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `43.21%` | `56.79%` | `0.76` | 17,130,000.00 USD |
| `15M` | `Binance` | `46.4%` | `53.6%` | `0.87` | 9,200,000.00 USD |
| `15M` | `OKX` | `42.16%` | `57.84%` | `0.73` | 1,970,000.00 USD |
| `15M` | `Bybit` | `34.77%` | `65.23%` | `0.53` | 2,120,000.00 USD |
| `15M` | `KuCoin` | `50.71%` | `49.29%` | `1.03` | 187,030.00 USD |
| `15M` | `Gate` | `41.98%` | `58.02%` | `0.72` | 1,020,000.00 USD |
| `15M` | `Bitget` | `29.65%` | `70.35%` | `0.42` | 491,350.00 USD |
| `15M` | `BingX` | `59.24%` | `40.76%` | `1.45` | 259,270.00 USD |
| `15M` | `MEXC` | `36.57%` | `63.43%` | `0.58` | 246,710.00 USD |
| `15M` | `Bitunix` | `46.83%` | `53.17%` | `0.88` | 343,140.00 USD |
| `15M` | `Hyperliquid` | `49.47%` | `50.53%` | `0.98` | 557,380.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `59.65%` | `40.35%` | `1.48` | 50,700.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `8.44%` | `91.56%` | `0.09` | 279,360.00 USD |
| `15M` | `HTX` | `51.37%` | `48.63%` | `1.06` | 64,530.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.7%` | `48.3%` | `1.07` | 77,400.00 USD |
| `15M` | `Aster` | `19.97%` | `80.03%` | `0.25` | 167,050.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `59.65%` | `40.35%` | `1.48` | 89,940.00 USD |
| `15M` | `Whale Positions` | `46.4%` | `53.6%` | `0.87` | 9,200,000.00 USD |
| `15M` | `Global Accounts` | `43.21%` | `56.79%` | `0.76` | 17,130,000.00 USD |
| `1H` | `TRX` | `42.60%` | `57.40%` | `0.74` | 57,710,000.00 USD |
| `1H` | `Binance` | `43.91%` | `56.09%` | `0.78` | 34,140,000.00 USD |
| `1H` | `OKX` | `47.47%` | `52.53%` | `0.90` | 4,570,000.00 USD |
| `1H` | `Bybit` | `29.29%` | `70.71%` | `0.41` | 6,420,000.00 USD |
| `1H` | `KuCoin` | `51.16%` | `48.84%` | `1.05` | 778,150.00 USD |
| `1H` | `Gate` | `45.91%` | `54.09%` | `0.85` | 2,920,000.00 USD |
| `1H` | `Bitget` | `38.35%` | `61.65%` | `0.62` | 1,320,000.00 USD |
| `1H` | `BingX` | `45.5%` | `54.5%` | `0.83` | 995,420.00 USD |
| `1H` | `MEXC` | `42.46%` | `57.54%` | `0.74` | 678,290.00 USD |
| `1H` | `Bitunix` | `47.38%` | `52.62%` | `0.90` | 1,390,000.00 USD |
| `1H` | `Hyperliquid` | `56.22%` | `43.78%` | `1.28` | 1,340,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.66%` | `51.34%` | `0.95` | 430,690.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `4.07%` | `95.93%` | `0.04` | 1,000,000.00 USD |
| `1H` | `HTX` | `57.92%` | `42.08%` | `1.38` | 326,360.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.07%` | `52.93%` | `0.89` | 301,560.00 USD |
| `1H` | `Aster` | `45.81%` | `54.19%` | `0.85` | 788,950.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `65.24%` | `34.76%` | `1.88` | 319,720.00 USD |
| `1H` | `Whale Positions` | `43.91%` | `56.09%` | `0.78` | 34,140,000.00 USD |
| `1H` | `Global Accounts` | `42.60%` | `57.40%` | `0.74` | 57,710,000.00 USD |
| `4H` | `TRX` | `47.82%` | `52.18%` | `0.92` | 966,510,000.00 USD |
| `4H` | `Binance` | `47.15%` | `52.85%` | `0.89` | 293,710,000.00 USD |
| `4H` | `OKX` | `45.72%` | `54.28%` | `0.84` | 196,900,000.00 USD |
| `4H` | `Bybit` | `51.52%` | `48.48%` | `1.06` | 90,560,000.00 USD |
| `4H` | `KuCoin` | `49.96%` | `50.04%` | `1.00` | 4,280,000.00 USD |
| `4H` | `Gate` | `51.18%` | `48.82%` | `1.05` | 76,140,000.00 USD |
| `4H` | `Bitget` | `43.34%` | `56.66%` | `0.76` | 44,370,000.00 USD |
| `4H` | `BingX` | `44.14%` | `55.86%` | `0.79` | 44,610,000.00 USD |
| `4H` | `MEXC` | `47.44%` | `52.56%` | `0.90` | 82,400,000.00 USD |
| `4H` | `Bitunix` | `47.99%` | `52.01%` | `0.92` | 44,050,000.00 USD |
| `4H` | `Hyperliquid` | `48.76%` | `51.24%` | `0.95` | 34,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.51%` | `48.49%` | `1.06` | 16,330,000.00 USD |
| `4H` | `Crypto.com` | `45.55%` | `54.45%` | `0.84` | 2,860,000.00 USD |
| `4H` | `WhiteBIT` | `85.63%` | `14.37%` | `5.96` | 13,360,000.00 USD |
| `4H` | `HTX` | `48.18%` | `51.82%` | `0.93` | 1,120,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.08%` | `70.92%` | `0.41` | 3,230,000.00 USD |
| `4H` | `Aster` | `41.47%` | `58.53%` | `0.71` | 6,250,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.29%` | `60.71%` | `0.65` | 11,450,000.00 USD |
| `4H` | `Whale Positions` | `47.15%` | `52.85%` | `0.89` | 293,710,000.00 USD |
| `4H` | `Global Accounts` | `47.82%` | `52.18%` | `0.92` | 966,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3370` | `0.3359` | `0.3370` | `0.3378` | `0.3316` | 5,309,391.96 USD | 3,078,017.12 USD | 2,231,374.84 USD | 846,642.29 USD | `+15.95%` | `35B / 9S` |
| `0:00 UTC` | `0.3368` | `0.3360` | `0.3368` | `0.3377` | `0.3336` | 2,717,916.28 USD | 1,271,599.87 USD | 1,446,316.41 USD | -174,716.54 USD | `-6.43%` | `5B / 15S` |
| `5:00 UTC` | `0.3312` | `0.3323` | `0.3312` | `0.3350` | `0.3309` | 3,615,541.77 USD | 1,824,507.31 USD | 1,791,034.46 USD | 33,472.85 USD | `+0.93%` | `10B / 13S` |
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3347` | `0.3348` | `0.3347` | `0.3359` | `0.3335` | 994,672.60 USD | 513,864.23 USD | 480,808.37 USD | 33,055.85 USD | `+3.32%` | `26B / 28S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 14:33` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3320` | 2,500,000.00 USD | 0.00 USD |
| `10-28 14:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3319` | 0.00 USD | 0.00 USD |
| `10-28 14:18` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3318` | 0.00 USD | 0.00 USD |
| `10-28 14:13` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3317` | 438,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:48` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 13:43` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3318` | 192,000.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3315` | 266,000.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3315` | 493,000.00 USD | 0.00 USD |
| `10-28 09:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3313` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3309` | 205,000.00 USD | 0.00 USD |
| `10-28 05:53` | `Volume 1.0M TRX` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:51` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:44` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3318` | 198,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -165,200.00 USD | 164,470.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,680,000.00 USD | 30,840.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,540,000.00 USD | 601,520.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,230,000.00 USD | 1,260,000.00 USD | **`ACCUMULATION`** |
| `2h` | 914,540.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `4h` | 4,710,000.00 USD | -61,910.00 USD | **`ACCUMULATION`** |
| `6h` | 8,920,000.00 USD | -6,420,000.00 USD | **`ACCUMULATION`** |
| `8h` | 14,520,000.00 USD | -3,330,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,500,000.00 USD | -595,770.00 USD | **`ACCUMULATION`** |
| `24h` | 20,390,000.00 USD | 5,790,000.00 USD | **`ACCUMULATION`** |
| `1w` | 14,010,000.00 USD | 4,550,000.00 USD | **`ACCUMULATION`** |
| `30d` | -9,440,000.00 USD | 5,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-165.20K` | 15m=`-1.68M` | 1h=`-1.23M` | 24h=`+20.39M`
* Futures Capital Netflows: 5m=`+164.47K` | 15m=`+30.84K` | 1h=`+1.26M` | 24h=`+5.79M`
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
  * Execution Entry: `0.3409` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3318` (Risk Distance: `0.0091` pts)
  * +2.5R Take Profit: `0.3637`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3669` (Risk Distance: `0.0091` pts)
  * +2.5R Take Profit: `0.3350`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3375`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
