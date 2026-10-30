# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:30:44 IST` (`2026-10-30 11:00:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3395` | **Live Ask Quote**: `0.3431` | **Mid Price**: `0.3413`
- **Spread Points**: `36.00` | **Spread BPS**: `105.48 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3442` | VWAP Z-Score: `-0.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0028` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.90` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3723` | Lower -3.00σ Band: `0.3161`
  * Upper +2.51σ Band: `0.3677` | Lower -2.51σ Band: `0.3207`
  * Upper +2.01σ Band: `0.3631` | Lower -2.01σ Band: `0.3254`
  * Upper +2.00σ Band: `0.3630` | Lower -2.00σ Band: `0.3255`
  * Upper +1.28σ Band: `0.3562` | Lower -1.28σ Band: `0.3322`
  * Upper +1.00σ Band: `0.3536` | Lower -1.00σ Band: `0.3349`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3347` | EMA-20=`0.3356` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3384` (Slope: `+0.0000`) | EMA-100=`0.3377`
  * Institutional Anchors: EMA-144=`0.3365` | EMA-200=`0.3353` (Slope: `-0.0746`) | EMA-233=`0.3347`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-4.59%`)
  * Point of Control (POC) = `0.3513` (Distance: `-2.84%`)
  * Value Area Low (VAL) = `0.3387` (Distance: `+0.79%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3460` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3397` | Low=`0.3319`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3399` - `0.3427`
  * Optimal Trade Entry (OTE 0.705): `0.3420`
  * Structural Invalidation Anchor (0.786): `0.3440`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3393` | `0.3409` | `0.3385` | `0.3406` | `3,261,694` | 1,107,688.92 USD | 55,574.62 USD | `+5.02%` | -4,194,368.54 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.3406` | `0.3410` | `0.3377` | `0.3404` | `4,967,645` | 1,687,429.09 USD | -208,994.69 USD | `-12.39%` | -4,403,363.24 USD | `-0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3404` | `0.3416` | `0.3394` | `0.3416` | `1,455,541` | 495,748.86 USD | 99,731.95 USD | `+20.12%` | -4,303,631.29 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3359` | `0.3400` | `0.3343` | `0.3391` | `10,876,835` | 3,666,829.89 USD | 117,449.48 USD | `+3.20%` | -2,594,157.02 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3391` | `0.3409` | `0.3377` | `0.3406` | `18,974,049` | 6,444,023.59 USD | -1,597,593.95 USD | `-24.79%` | -4,191,750.97 USD | `-1.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3406` | `0.3416` | `0.3377` | `0.3416` | `6,422,421` | 2,182,916.61 USD | -109,524.08 USD | `-5.02%` | -4,301,275.05 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3324` | `39,413,287` | 13,120,323.22 USD | 312,055.16 USD | `+2.38%` | -2,219,666.72 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3324` | `0.3367` | `0.3318` | `0.3346` | `29,287,422` | 9,766,957.28 USD | -468,481.97 USD | `-4.80%` | -2,688,148.69 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3346` | `0.3416` | `0.3335` | `0.3416` | `41,747,597` | 14,126,968.95 USD | -1,613,126.36 USD | `-11.42%` | -4,301,275.05 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3416` | `0.3307` | `0.3416` | `110,449,071` | 37,014,510.79 USD | -1,769,291.84 USD | `-4.78%` | -4,175,345.72 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3416` | `0.3307` | `0.3416` | `110,449,071` | 37,014,510.79 USD | -1,769,291.84 USD | `-4.78%` | -4,175,345.72 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3413`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1079` | `0xecb6...2b00` | `LONG` | 2,009,928.27 USD | `5,879,390.00` | `0.3344` | `0.3417` | `0.000000` | 43,939.68 USD | `+2.19%` | `10X Cross` |
| `1269` | `0x8dd7...fa30` | `SHORT` | 1,709,250.00 USD | `5,000,000.00` | `0.3334` | `0.3417` | `0.3731` | -42,449.93 USD | `-2.48%` | `6X Cross` |
| `1566` | `0xeadc...9d55` | `LONG` | 1,367,440.00 USD | `4,000,000.00` | `0.3421` | `0.3417` | `0.000000` | -1,038.09 USD | `-0.08%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,464.28 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3312 USD [API] | `2026-10-29 18:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.3314` | 5,738.36 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 5.74K USD at 0.3314 USD [API] | `2026-10-29 18:33:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.69%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--2.46%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.69%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--3.93%`)
  * 3D Horizon: Short MP=`0.3662` (Vol: 1,100,000.00 USD, Dist: `+8.29%`) | Long MP=`0.3250` (Vol: 996,100.00 USD, Dist: `--3.89%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+8.29%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--3.93%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0785` | 6,930.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 226.18 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 868.52 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 188.15 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,450.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 265.88 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 123.26 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 11,410.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 44,010.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 10,230.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 20,120.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 511.50 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 4,470.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 10,440.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 5,170.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 38,650.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 174.38 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,400.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 100.37 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 165.87 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1855` | 109.63 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 14,200.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,520.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 512.82 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 493.04 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 232.51 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 204.76 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,420.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 553.86 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 826.50 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 6,760.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 464.79 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 11,840.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 555.61 USD | 993,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,520.00 USD | 993,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 991,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 107.74 USD | 990,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 4,550.00 USD | 990,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 986,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 983,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 983,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,390.00 USD | 983,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 220.99 USD | 979,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,470.00 USD | 979,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 15,180.00 USD | 895,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 879,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 13,300.00 USD | 873,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 3,690.00 USD | 860,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 838.74 USD | 856,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 357.90 USD | 855,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 6,300.00 USD | 855,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,310.00 USD | 849,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 821.82 USD | 844,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 843,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 843,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 842,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 23,430,000.00 USD | 23,430,000.00 USD | 82,070.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 842,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 23,340,000.00 USD | 23,340,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,200,000.00 USD | 23,200,000.00 USD | 122,540.00 USD | 36,820.00 USD | 59,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,010.00 USD | 842,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 22,980,000.00 USD | 22,980,000.00 USD | 89,290.00 USD | 34,680.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 22,800,000.00 USD | 22,800,000.00 USD | 54,000.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 16,770,000.00 USD | 16,770,000.00 USD | 25,600.00 USD | 3,620.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 22,710,000.00 USD | 22,710,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2985` | 16,730,000.00 USD | 16,730,000.00 USD | 101,850.00 USD | 10,860.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 841,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2989` | 16,600,000.00 USD | 16,600,000.00 USD | 26,190.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 22,490,000.00 USD | 22,490,000.00 USD | 117,420.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2993` | 16,570,000.00 USD | 16,570,000.00 USD | 55,190.00 USD | 33,830.00 USD | 56,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,330,000.00 USD | 22,330,000.00 USD | 6,450.00 USD | 69,130.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 840,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2997` | 16,420,000.00 USD | 16,420,000.00 USD | 600.83 USD | 28,790.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3001` | 16,340,000.00 USD | 16,340,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 34,510.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3005` | 16,310,000.00 USD | 16,310,000.00 USD | 15,600.00 USD | 7,870.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 840,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,050,000.00 USD | 22,050,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3009` | 16,270,000.00 USD | 16,270,000.00 USD | 35,140.00 USD | 8,400.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3013` | 16,210,000.00 USD | 16,210,000.00 USD | 17,320.00 USD | 3,170.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 22,010,000.00 USD | 22,010,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 829,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3017` | 16,180,000.00 USD | 16,180,000.00 USD | 1,010.00 USD | 8,490.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3021` | 16,160,000.00 USD | 16,160,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3025` | 16,120,000.00 USD | 16,120,000.00 USD | 2,600.00 USD | 2,050.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 22,000,000.00 USD | 22,000,000.00 USD | 4,850.00 USD | 22,200.00 USD | 55,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 829,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3029` | 16,100,000.00 USD | 16,100,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 21,910,000.00 USD | 21,910,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3033` | 16,070,000.00 USD | 16,070,000.00 USD | 1,070.00 USD | 8,320.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 827,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3037` | 16,050,000.00 USD | 16,050,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3037` | 21,860,000.00 USD | 21,860,000.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3041` | 16,040,000.00 USD | 16,040,000.00 USD | 1,130.00 USD | 9,300.00 USD | 75,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3045` | 15,960,000.00 USD | 15,960,000.00 USD | 9,410.00 USD | 13,170.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 823,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 15,930,000.00 USD | 15,930,000.00 USD | 38,210.00 USD | 11,440.00 USD | 62,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 21,860,000.00 USD | 21,860,000.00 USD | 18,020.00 USD | 0.00 USD | 106,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3053` | 15,810,000.00 USD | 15,810,000.00 USD | 57,250.00 USD | 20,580.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 21,730,000.00 USD | 21,730,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 823,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3057` | 15,690,000.00 USD | 15,690,000.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3061` | 15,680,000.00 USD | 15,680,000.00 USD | 19,420.00 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 21,730,000.00 USD | 21,730,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3065` | 15,600,000.00 USD | 15,600,000.00 USD | 36,490.00 USD | 26,740.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 808,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3067` | 21,650,000.00 USD | 21,650,000.00 USD | 6,430.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3069` | 15,500,000.00 USD | 15,500,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 15,480,000.00 USD | 15,480,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 21,640,000.00 USD | 21,640,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 802,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3077` | 15,460,000.00 USD | 15,460,000.00 USD | 350.20 USD | 6,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 21,630,000.00 USD | 21,630,000.00 USD | 38,480.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 15,450,000.00 USD | 15,450,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 15,420,000.00 USD | 15,420,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 21,530,000.00 USD | 21,530,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 801,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3089` | 15,400,000.00 USD | 15,400,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 21,530,000.00 USD | 21,530,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 15,400,000.00 USD | 15,400,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 801,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 15,390,000.00 USD | 15,390,000.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 21,530,000.00 USD | 21,530,000.00 USD | 83,770.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3101` | 15,380,000.00 USD | 15,380,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 21,380,000.00 USD | 21,380,000.00 USD | 72,010.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3105` | 15,280,000.00 USD | 15,280,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 801,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 21,250,000.00 USD | 21,250,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3113` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 21,240,000.00 USD | 21,240,000.00 USD | 5,160.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 800,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3117` | 15,250,000.00 USD | 15,250,000.00 USD | 15,480.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3121` | 15,210,000.00 USD | 15,210,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 21,200,000.00 USD | 21,200,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3125` | 15,160,000.00 USD | 15,160,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,810.00 USD | 786,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 21,020,000.00 USD | 21,020,000.00 USD | 16,080.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3129` | 15,130,000.00 USD | 15,130,000.00 USD | 3,990.00 USD | 28,470.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 15,070,000.00 USD | 15,070,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 20,890,000.00 USD | 20,890,000.00 USD | 10,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 446.11 USD | 769,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 15,030,000.00 USD | 15,030,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 20,880,000.00 USD | 20,880,000.00 USD | 12,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 15,020,000.00 USD | 15,020,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 15,000,000.00 USD | 15,000,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 20,870,000.00 USD | 20,870,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 577.11 USD | 768,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3149` | 14,990,000.00 USD | 14,990,000.00 USD | 1,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 20,550,000.00 USD | 20,550,000.00 USD | 197,800.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3153` | 14,990,000.00 USD | 14,990,000.00 USD | 30,120.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 11,510.00 USD | 768,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 14,940,000.00 USD | 14,940,000.00 USD | 13,270.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 20,280,000.00 USD | 20,280,000.00 USD | 403,130.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 14,900,000.00 USD | 14,900,000.00 USD | 5,650.00 USD | 2,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 19,720,000.00 USD | 19,720,000.00 USD | 478,060.00 USD | 174,600.00 USD | 189,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3165` | 14,900,000.00 USD | 14,900,000.00 USD | 46,090.00 USD | 30,980.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 756,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 14,810,000.00 USD | 14,810,000.00 USD | 2,610.00 USD | 10,820.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 18,880,000.00 USD | 18,880,000.00 USD | 414,720.00 USD | 104,590.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 14,780,000.00 USD | 14,780,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 18,220,000.00 USD | 18,220,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,290.00 USD | 755,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3177` | 14,690,000.00 USD | 14,690,000.00 USD | 47,770.00 USD | 8,980.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 14,600,000.00 USD | 14,600,000.00 USD | 251,300.00 USD | 40,890.00 USD | 68,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 17,960,000.00 USD | 17,960,000.00 USD | 744,820.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3185` | 14,240,000.00 USD | 14,240,000.00 USD | 149,850.00 USD | 52,920.00 USD | 51,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 1,300.00 USD | 753,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3187` | 16,960,000.00 USD | 16,960,000.00 USD | 409,740.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3189` | 13,990,000.00 USD | 13,990,000.00 USD | 172,980.00 USD | 5,580.00 USD | 48,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 13,760,000.00 USD | 13,760,000.00 USD | 154,490.00 USD | 107,560.00 USD | 180,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 16,420,000.00 USD | 16,420,000.00 USD | 192,420.00 USD | 123,840.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3197` | 13,320,000.00 USD | 13,320,000.00 USD | 74,370.00 USD | 118,340.00 USD | 160,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 15,860,000.00 USD | 15,860,000.00 USD | 5,810.00 USD | 191,160.00 USD | 267,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3201` | 12,960,000.00 USD | 12,960,000.00 USD | 208,440.00 USD | 48,100.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 12,600,000.00 USD | 12,600,000.00 USD | 163,900.00 USD | 31,270.00 USD | 102,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 15,400,000.00 USD | 15,400,000.00 USD | 172,060.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 2,930.00 USD | 752,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3209` | 12,300,000.00 USD | 12,300,000.00 USD | 89,060.00 USD | 29,040.00 USD | 54,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 15,040,000.00 USD | 15,040,000.00 USD | 561,850.00 USD | 135,070.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3213` | 12,130,000.00 USD | 12,130,000.00 USD | 55,660.00 USD | 30,340.00 USD | 107,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 11,930,000.00 USD | 11,930,000.00 USD | 8,400.00 USD | 33,860.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 14,090,000.00 USD | 14,090,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3221` | 11,740,000.00 USD | 11,740,000.00 USD | 98,430.00 USD | 33,430.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 13,640,000.00 USD | 13,640,000.00 USD | 649,350.00 USD | 265,170.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3225` | 11,540,000.00 USD | 11,540,000.00 USD | 72,740.00 USD | 33,350.00 USD | 202,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 11,230,000.00 USD | 11,230,000.00 USD | 91,630.00 USD | 55,060.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 12,570,000.00 USD | 12,570,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 10,950,000.00 USD | 10,950,000.00 USD | 56,470.00 USD | 35,600.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 10,910,000.00 USD | 10,910,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 749,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 10,810,000.00 USD | 10,810,000.00 USD | 6,420.00 USD | 83,630.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 10,550,000.00 USD | 10,550,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 9,620,000.00 USD | 9,620,000.00 USD | 434,620.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3245` | 10,400,000.00 USD | 10,400,000.00 USD | 256,740.00 USD | 54,650.00 USD | 265,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 8,890,000.00 USD | 8,890,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 9,830,000.00 USD | 9,830,000.00 USD | 792,700.00 USD | 90,860.00 USD | 176,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 8,770,000.00 USD | 8,770,000.00 USD | 217,740.00 USD | 107,140.00 USD | 423,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 7,560,000.00 USD | 7,560,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 339,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3257` | 8,020,000.00 USD | 8,020,000.00 USD | 567,900.00 USD | 48,220.00 USD | 229,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 5,870,000.00 USD | 5,870,000.00 USD | 432,530.00 USD | 308,400.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3261` | 7,170,000.00 USD | 7,170,000.00 USD | 173,320.00 USD | 371,060.00 USD | 555,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 6,070,000.00 USD | 6,070,000.00 USD | 90,110.00 USD | 156,570.00 USD | 345,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 4,620,000.00 USD | 4,620,000.00 USD | 78,960.00 USD | 324,810.00 USD | 500,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3269` | 5,480,000.00 USD | 5,480,000.00 USD | 217,410.00 USD | 143,860.00 USD | 378,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 3,720,000.00 USD | 3,720,000.00 USD | 318,340.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3273` | 4,740,000.00 USD | 4,740,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 745,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 4,500,000.00 USD | 4,500,000.00 USD | 327,480.00 USD | 76,150.00 USD | 161,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3277` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3281` | 3,940,000.00 USD | 3,940,000.00 USD | 106,720.00 USD | 73,120.00 USD | 120,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 2,880,000.00 USD | 2,880,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3285` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 48,460.00 USD | 79,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 745,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 3,510,000.00 USD | 3,510,000.00 USD | 155,850.00 USD | 21,810.00 USD | 155,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3293` | 3,170,000.00 USD | 3,170,000.00 USD | 977.29 USD | 60,450.00 USD | 165,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 2,170,000.00 USD | 2,170,000.00 USD | 255,900.00 USD | 83,080.00 USD | 279,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3297` | 2,950,000.00 USD | 2,950,000.00 USD | 166,310.00 USD | 18,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3301` | 2,760,000.00 USD | 2,760,000.00 USD | 36,460.00 USD | 58,700.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 1,550,000.00 USD | 1,550,000.00 USD | 184,120.00 USD | 47,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3305` | 2,640,000.00 USD | 2,640,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 1,320,000.00 USD | 1,320,000.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3309` | 2,420,000.00 USD | 2,420,000.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 1,910,000.00 USD | 1,910,000.00 USD | 61,660.00 USD | 128,440.00 USD | 183,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 850,120.00 USD | 850,120.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3317` | 1,540,000.00 USD | 1,540,000.00 USD | 27,700.00 USD | 58,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 799,470.00 USD | 799,470.00 USD | 0.00 USD | 57,890.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3321` | 1,450,000.00 USD | 1,450,000.00 USD | 18,060.00 USD | 23,430.00 USD | 100,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 1,310,000.00 USD | 1,310,000.00 USD | 51,310.00 USD | 9,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 545,470.00 USD | 545,470.00 USD | 251,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3329` | 1,250,000.00 USD | 1,250,000.00 USD | 64,380.00 USD | 0.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 294,230.00 USD | 294,230.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3333` | 1,140,000.00 USD | 1,140,000.00 USD | 92,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3337` | 1,050,000.00 USD | 1,050,000.00 USD | 34,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3345` | 1,020,000.00 USD | 1,020,000.00 USD | 20,610.00 USD | 8,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3349` | 987,790.00 USD | 987,790.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3369` | 957,160.00 USD | 957,160.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3377` | 884,240.00 USD | 884,240.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 254,160.00 USD | 254,160.00 USD | 0.00 USD | 0.00 USD | 254,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3401` | 554,610.00 USD | 554,610.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 376,470.00 USD | 376,470.00 USD | 0.00 USD | 0.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3405` | 334,040.00 USD | 334,040.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3409` | 139,820.00 USD | 139,820.00 USD | 112,120.00 USD | 0.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3409` | 279,630.00 USD | 279,630.00 USD | 112,120.00 USD | 0.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 852,850.00 USD | 852,850.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3413` | 360,460.00 USD | 360,460.00 USD | 0.00 USD | 0.00 USD | 80,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 974,140.00 USD | 974,140.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3417` | 901,510.00 USD | 901,510.00 USD | 343,500.00 USD | 0.00 USD | 197,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3421` | 972,680.00 USD | 972,680.00 USD | 71,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 229,350.00 USD | 384,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3429` | 1,210,000.00 USD | 1,210,000.00 USD | 60,980.00 USD | 95,980.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 1,520,000.00 USD | 1,520,000.00 USD | 105,330.00 USD | 167,240.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 1,920,000.00 USD | 1,920,000.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3437` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 117,260.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 2,030,000.00 USD | 2,030,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3449` | 2,250,000.00 USD | 2,250,000.00 USD | 97,620.00 USD | 92,440.00 USD | 183,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 2,320,000.00 USD | 2,320,000.00 USD | 62,830.00 USD | 28,550.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 2,510,000.00 USD | 2,510,000.00 USD | 130,670.00 USD | 47,460.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3457` | 3,300,000.00 USD | 3,300,000.00 USD | 170,670.00 USD | 57,370.00 USD | 553,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 2,740,000.00 USD | 2,740,000.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 3,980,000.00 USD | 3,980,000.00 USD | 250,210.00 USD | 190,690.00 USD | 242,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 3,490,000.00 USD | 3,490,000.00 USD | 251,240.00 USD | 290,920.00 USD | 205,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3465` | 4,280,000.00 USD | 4,280,000.00 USD | 86,270.00 USD | 67,330.00 USD | 142,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 4,520,000.00 USD | 4,520,000.00 USD | 130,280.00 USD | 42,550.00 USD | 75,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 3,820,000.00 USD | 3,820,000.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 4,620,000.00 USD | 4,620,000.00 USD | 34,590.00 USD | 35,130.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3477` | 4,800,000.00 USD | 4,800,000.00 USD | 51,860.00 USD | 48,500.00 USD | 77,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 4,980,000.00 USD | 4,980,000.00 USD | 73,970.00 USD | 38,390.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 32,530.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3485` | 5,110,000.00 USD | 5,110,000.00 USD | 9,350.00 USD | 46,810.00 USD | 76,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 3,970,000.00 USD | 3,970,000.00 USD | 19,250.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3489` | 5,240,000.00 USD | 5,240,000.00 USD | 41,500.00 USD | 23,850.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3493` | 5,280,000.00 USD | 5,280,000.00 USD | 3,620.00 USD | 33,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 93,150.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3497` | 5,810,000.00 USD | 5,810,000.00 USD | 32,290.00 USD | 0.00 USD | 497,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 4,390,000.00 USD | 4,390,000.00 USD | 133,330.00 USD | 0.00 USD | 139,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3501` | 5,920,000.00 USD | 5,920,000.00 USD | 52,670.00 USD | 9,040.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3505` | 6,060,000.00 USD | 6,060,000.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 4,420,000.00 USD | 4,420,000.00 USD | 6,140.00 USD | 19,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 8,650.00 USD | 10,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3509` | 6,080,000.00 USD | 6,080,000.00 USD | 2,790.00 USD | 16,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 5,380,000.00 USD | 5,380,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 175.05 USD | 11,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3517` | 6,310,000.00 USD | 6,310,000.00 USD | 52,740.00 USD | 5,720.00 USD | 101,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3517` | 5,380,000.00 USD | 5,380,000.00 USD | 6,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 6,450,000.00 USD | 6,450,000.00 USD | 47,300.00 USD | 21,980.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 5,900,000.00 USD | 5,900,000.00 USD | 277,410.00 USD | 28,950.00 USD | 205,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3525` | 6,510,000.00 USD | 6,510,000.00 USD | 13,010.00 USD | 17,990.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3525` | 112.45 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3529` | 6,700,000.00 USD | 6,700,000.00 USD | 128,260.00 USD | 57,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3529` | 6,030,000.00 USD | 6,030,000.00 USD | 137,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 6,950,000.00 USD | 6,950,000.00 USD | 99,280.00 USD | 44,040.00 USD | 108,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 6,330,000.00 USD | 6,330,000.00 USD | 5,810.00 USD | 98,000.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3537` | 7,280,000.00 USD | 7,280,000.00 USD | 107,750.00 USD | 29,120.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3541` | 7,460,000.00 USD | 7,460,000.00 USD | 101,070.00 USD | 80,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 7,250,000.00 USD | 7,250,000.00 USD | 808,620.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3545` | 7,580,000.00 USD | 7,580,000.00 USD | 5,220.00 USD | 44,140.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3545` | 29,460.00 USD | 40,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3547` | 7,560,000.00 USD | 7,560,000.00 USD | 15,040.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3549` | 7,660,000.00 USD | 7,660,000.00 USD | 17,670.00 USD | 58,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 7,770,000.00 USD | 7,770,000.00 USD | 22,550.00 USD | 39,740.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3557` | 7,810,000.00 USD | 7,810,000.00 USD | 2,710.00 USD | 38,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 7,680,000.00 USD | 7,680,000.00 USD | 9,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3561` | 7,940,000.00 USD | 7,940,000.00 USD | 859.20 USD | 25,000.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3565` | 8,000,000.00 USD | 8,000,000.00 USD | 5,060.00 USD | 11,630.00 USD | 39,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 7,730,000.00 USD | 7,730,000.00 USD | 4,730.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3569` | 8,010,000.00 USD | 8,010,000.00 USD | 2,060.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 7,730,000.00 USD | 7,730,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3573` | 8,150,000.00 USD | 8,150,000.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 8,190,000.00 USD | 8,190,000.00 USD | 31,960.00 USD | 9,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 7,860,000.00 USD | 7,860,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3581` | 8,230,000.00 USD | 8,230,000.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 8,000,000.00 USD | 8,000,000.00 USD | 4,040.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3585` | 8,270,000.00 USD | 8,270,000.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 8,280,000.00 USD | 8,280,000.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 8,380,000.00 USD | 8,380,000.00 USD | 10,970.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3593` | 8,480,000.00 USD | 8,480,000.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3597` | 8,590,000.00 USD | 8,590,000.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 8,790,000.00 USD | 8,790,000.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 9,030,000.00 USD | 9,030,000.00 USD | 7,660.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3605` | 8,980,000.00 USD | 8,980,000.00 USD | 61,950.00 USD | 32,860.00 USD | 94,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 9,430,000.00 USD | 9,430,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3609` | 9,210,000.00 USD | 9,210,000.00 USD | 76,130.00 USD | 25,740.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 9,490,000.00 USD | 9,490,000.00 USD | 13,080.00 USD | 59,640.00 USD | 203,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 10,120,000.00 USD | 10,120,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3617` | 9,870,000.00 USD | 9,870,000.00 USD | 226,310.00 USD | 50,630.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 10,330,000.00 USD | 10,330,000.00 USD | 3,550.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 10,160,000.00 USD | 10,160,000.00 USD | 144,510.00 USD | 75,820.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 10,310,000.00 USD | 10,310,000.00 USD | 100,410.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 11,550,000.00 USD | 11,550,000.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 11,960,000.00 USD | 11,960,000.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 12,360.00 USD | 53,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 12,210,000.00 USD | 12,210,000.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 12,580,000.00 USD | 12,580,000.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 11,450,000.00 USD | 11,450,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3645` | 12,890,000.00 USD | 12,890,000.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 13,240,000.00 USD | 13,240,000.00 USD | 96,700.00 USD | 59,680.00 USD | 195,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 11,630,000.00 USD | 11,630,000.00 USD | 180,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3653` | 13,730,000.00 USD | 13,730,000.00 USD | 303,010.00 USD | 19,500.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 12,430,000.00 USD | 12,430,000.00 USD | 681,380.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3657` | 14,260,000.00 USD | 14,260,000.00 USD | 218,660.00 USD | 149,310.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 14,720,000.00 USD | 14,720,000.00 USD | 277,650.00 USD | 88,330.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 13,420,000.00 USD | 13,420,000.00 USD | 685,520.00 USD | 66,940.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3665` | 15,370,000.00 USD | 15,370,000.00 USD | 468,570.00 USD | 117,940.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,110.00 USD | 56,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 14,040,000.00 USD | 14,040,000.00 USD | 419,350.00 USD | 34,510.00 USD | 166,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3669` | 15,780,000.00 USD | 15,780,000.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 16,090,000.00 USD | 16,090,000.00 USD | 52,240.00 USD | 102,840.00 USD | 158,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 14,730,000.00 USD | 14,730,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3677` | 16,820,000.00 USD | 16,820,000.00 USD | 494,570.00 USD | 41,730.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 14,980,000.00 USD | 14,980,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3681` | 17,320,000.00 USD | 17,320,000.00 USD | 310,830.00 USD | 87,330.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 17,900,000.00 USD | 17,900,000.00 USD | 327,450.00 USD | 152,380.00 USD | 93,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 15,160,000.00 USD | 15,160,000.00 USD | 2,020.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3689` | 18,410,000.00 USD | 18,410,000.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 15,570,000.00 USD | 15,570,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3693` | 18,520,000.00 USD | 18,520,000.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 18,770,000.00 USD | 18,770,000.00 USD | 155,550.00 USD | 83,650.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 15,810,000.00 USD | 15,810,000.00 USD | 4,850.00 USD | 175,510.00 USD | 55,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3701` | 19,530,000.00 USD | 19,530,000.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 15,860,000.00 USD | 15,860,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3705` | 20,340,000.00 USD | 20,340,000.00 USD | 249,050.00 USD | 8,320.00 USD | 560,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 56,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3709` | 20,490,000.00 USD | 20,490,000.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 15,860,000.00 USD | 15,860,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3713` | 21,870,000.00 USD | 21,870,000.00 USD | 482,060.00 USD | 90,010.00 USD | 804,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 16,260,000.00 USD | 16,260,000.00 USD | 3,410.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3717` | 22,400,000.00 USD | 22,400,000.00 USD | 44,980.00 USD | 220,760.00 USD | 269,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 22,560,000.00 USD | 22,560,000.00 USD | 9,410.00 USD | 62,750.00 USD | 85,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 786,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3725` | 23,640,000.00 USD | 23,640,000.00 USD | 512,060.00 USD | 31,730.00 USD | 537,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 56,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 17,320,000.00 USD | 17,320,000.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3729` | 24,150,000.00 USD | 24,150,000.00 USD | 33,900.00 USD | 128,180.00 USD | 349,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 24,950,000.00 USD | 24,950,000.00 USD | 115,910.00 USD | 23,870.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 17,510,000.00 USD | 17,510,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,070.00 USD | 63,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3737` | 25,210,000.00 USD | 25,210,000.00 USD | 164,450.00 USD | 94,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 17,990,000.00 USD | 17,990,000.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3741` | 25,730,000.00 USD | 25,730,000.00 USD | 51,150.00 USD | 71,420.00 USD | 403,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 26,110,000.00 USD | 26,110,000.00 USD | 37,630.00 USD | 35,840.00 USD | 305,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 18,390,000.00 USD | 18,390,000.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3749` | 26,880,000.00 USD | 26,880,000.00 USD | 229,090.00 USD | 20,770.00 USD | 520,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3753` | 27,050,000.00 USD | 27,050,000.00 USD | 134,010.00 USD | 0.00 USD | 31,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 67,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 27,320,000.00 USD | 27,320,000.00 USD | 23,190.00 USD | 5,790.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 18,690,000.00 USD | 18,690,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3761` | 28,550,000.00 USD | 28,550,000.00 USD | 303,200.00 USD | 73,190.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 18,870,000.00 USD | 18,870,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3765` | 28,600,000.00 USD | 28,600,000.00 USD | 18,380.00 USD | 24,840.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3769` | 28,640,000.00 USD | 28,640,000.00 USD | 0.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 18,870,000.00 USD | 18,870,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 67,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3781` | 18,890,000.00 USD | 18,890,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 624,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 19,040,000.00 USD | 19,040,000.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 19,510,000.00 USD | 19,510,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 773.04 USD | 625,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3805` | 19,510,000.00 USD | 19,510,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3805` | 3,390.00 USD | 628,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3811` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 19,720,000.00 USD | 19,720,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 628,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3841` | 19,840,000.00 USD | 19,840,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 264.84 USD | 628,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3859` | 19,910,000.00 USD | 19,910,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 20,070,000.00 USD | 20,070,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3865` | 1,550,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3877` | 20,190,000.00 USD | 20,190,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 20,340,000.00 USD | 20,340,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 20,440,000.00 USD | 20,440,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3919` | 20,560,000.00 USD | 20,560,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 20,720,000.00 USD | 20,720,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 20,750,000.00 USD | 20,750,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 20,780,000.00 USD | 20,780,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 20,810,000.00 USD | 20,810,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 20,940,000.00 USD | 20,940,000.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 21,170,000.00 USD | 21,170,000.00 USD | 107,420.00 USD | 8,610.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 21,350,000.00 USD | 21,350,000.00 USD | 123,320.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 21,380,000.00 USD | 21,380,000.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 21,520,000.00 USD | 21,520,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 21,630,000.00 USD | 21,630,000.00 USD | 57,460.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 21,660,000.00 USD | 21,660,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 21,700,000.00 USD | 21,700,000.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3997` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 27,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4015` | 327.62 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4145` | 12,440.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 94,510.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 998.96 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 134.25 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 3,930.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4335` | 1,500.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4355` | 70,890.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 1,490.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 13,280.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4435` | 3,460.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 22,200.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 1,020.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 5,520.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4675` | 270.22 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 23,320.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 667.22 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5355` | 1,170.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5475` | 40,520.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 3,060.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 140.12 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5765` | 747,860.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5855` | 115.93 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5935` | 4,900.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 24,620.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6265` | 379.03 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 6,810.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6505` | 102,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6545` | 706.21 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0785` | 1,250,000.00 USD | 0.00 USD | 6,930.00 USD | `-76.58%` | `88,233.00` |
| `Live` | `Long` | `0.0795` | 1,240,000.00 USD | 0.00 USD | 226.18 USD | `-76.28%` | `2,845.00` |
| `Live` | `Long` | `0.0875` | 1,240,000.00 USD | 0.00 USD | 868.52 USD | `-73.89%` | `9,926.00` |
| `Live` | `Long` | `0.0905` | 1,240,000.00 USD | 0.00 USD | 188.15 USD | `-73.00%` | `2,079.00` |
| `Live` | `Long` | `0.1145` | 1,240,000.00 USD | 0.00 USD | 2,450.00 USD | `-65.84%` | `21,428.00` |
| `Live` | `Long` | `0.1155` | 1,240,000.00 USD | 0.00 USD | 265.88 USD | `-65.54%` | `2,302.00` |
| `Live` | `Long` | `0.1165` | 1,240,000.00 USD | 0.00 USD | 123.26 USD | `-65.24%` | `1,058.00` |
| `Live` | `Long` | `0.1385` | 1,240,000.00 USD | 0.00 USD | 11,410.00 USD | `-58.68%` | `82,417.00` |
| `Live` | `Long` | `0.1475` | 1,220,000.00 USD | 0.00 USD | 44,010.00 USD | `-55.99%` | `298,397.00` |
| `Live` | `Long` | `0.1585` | 1,180,000.00 USD | 0.00 USD | 388.01 USD | `-52.71%` | `2,448.00` |
| `Live` | `Long` | `0.1675` | 1,180,000.00 USD | 0.00 USD | 10,230.00 USD | `-50.02%` | `61,100.00` |
| `Live` | `Long` | `0.1685` | 1,170,000.00 USD | 0.00 USD | 20,120.00 USD | `-49.72%` | `119,400.00` |
| `Live` | `Long` | `0.1705` | 1,150,000.00 USD | 0.00 USD | 511.50 USD | `-49.13%` | `3,000.00` |
| `Live` | `Long` | `0.1715` | 1,150,000.00 USD | 0.00 USD | 4,470.00 USD | `-48.83%` | `26,050.00` |
| `Live` | `Long` | `0.1725` | 1,150,000.00 USD | 0.00 USD | 10,440.00 USD | `-48.53%` | `60,538.00` |
| `Live` | `Long` | `0.1735` | 1,130,000.00 USD | 0.00 USD | 339.71 USD | `-48.23%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,130,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.93%` | `29,642.00` |
| `Live` | `Long` | `0.1755` | 1,130,000.00 USD | 0.00 USD | 38,650.00 USD | `-47.64%` | `220,201.00` |
| `Live` | `Long` | `0.1765` | 1,090,000.00 USD | 0.00 USD | 174.38 USD | `-47.34%` | `988.00` |
| `Live` | `Long` | `0.1775` | 1,090,000.00 USD | 0.00 USD | 1,400.00 USD | `-47.04%` | `7,875.00` |
| `Live` | `Long` | `0.1815` | 1,090,000.00 USD | 0.00 USD | 100.37 USD | `-45.85%` | `553.00` |
| `Live` | `Long` | `0.1845` | 1,090,000.00 USD | 0.00 USD | 165.87 USD | `-44.95%` | `899.00` |
| `Live` | `Long` | `0.1855` | 1,090,000.00 USD | 0.00 USD | 109.63 USD | `-44.65%` | `591.00` |
| `Live` | `Long` | `0.1875` | 1,090,000.00 USD | 0.00 USD | 36,310.00 USD | `-44.05%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,050,000.00 USD | 0.00 USD | 632.00 USD | `-41.07%` | `3,200.00` |
| `Live` | `Long` | `0.2105` | 1,050,000.00 USD | 0.00 USD | 14,200.00 USD | `-37.19%` | `67,468.00` |
| `Live` | `Long` | `0.2165` | 1,040,000.00 USD | 0.00 USD | 1,520.00 USD | `-35.40%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,040,000.00 USD | 0.00 USD | 512.82 USD | `-34.81%` | `2,347.00` |
| `Live` | `Long` | `0.2205` | 1,040,000.00 USD | 0.00 USD | 493.04 USD | `-34.21%` | `2,236.00` |
| `Live` | `Long` | `0.2225` | 1,040,000.00 USD | 0.00 USD | 232.51 USD | `-33.61%` | `1,045.00` |
| `Live` | `Long` | `0.2245` | 1,030,000.00 USD | 0.00 USD | 4,570.00 USD | `-33.02%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 1,030,000.00 USD | 0.00 USD | 204.76 USD | `-32.42%` | `904.00` |
| `Live` | `Long` | `0.2295` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.52%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-31.22%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,030,000.00 USD | 0.00 USD | 2,420.00 USD | `-30.63%` | `10,412.00` |
| `Live` | `Long` | `0.2335` | 1,030,000.00 USD | 0.00 USD | 553.86 USD | `-30.33%` | `2,372.00` |
| `Live` | `Long` | `0.2345` | 1,020,000.00 USD | 0.00 USD | 5,700.00 USD | `-30.03%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 3,130.00 USD | `-29.73%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 1,020,000.00 USD | 0.00 USD | 686.56 USD | `-29.43%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 1,020,000.00 USD | 0.00 USD | 826.50 USD | `-29.14%` | `3,480.00` |
| `Live` | `Long` | `0.2395` | 1,010,000.00 USD | 0.00 USD | 151.36 USD | `-28.54%` | `632.00` |
| `Live` | `Long` | `0.2425` | 1,010,000.00 USD | 0.00 USD | 6,760.00 USD | `-27.64%` | `27,881.00` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 885.85 USD | `-27.35%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 1,010,000.00 USD | 0.00 USD | 464.79 USD | `-27.05%` | `1,901.00` |
| `Live` | `Long` | `0.2455` | 1,010,000.00 USD | 0.00 USD | 384.94 USD | `-26.75%` | `1,568.00` |
| `Live` | `Long` | `0.2475` | 1,010,000.00 USD | 0.00 USD | 11,840.00 USD | `-26.15%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 993,750.00 USD | 0.00 USD | 555.61 USD | `-25.26%` | `2,218.00` |
| `Live` | `Long` | `0.2565` | 993,190.00 USD | 0.00 USD | 1,520.00 USD | `-23.47%` | `5,912.00` |
| `Live` | `Long` | `0.2595` | 991,670.00 USD | 0.00 USD | 749.18 USD | `-22.57%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 990,920.00 USD | 0.00 USD | 107.74 USD | `-21.98%` | `412.00` |
| `Live` | `Long` | `0.2635` | 990,820.00 USD | 0.00 USD | 4,550.00 USD | `-21.38%` | `17,283.00` |
| `Live` | `Long` | `0.2645` | 986,260.00 USD | 0.00 USD | 2,650.00 USD | `-21.08%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 983,610.00 USD | 0.00 USD | 193.02 USD | `-20.78%` | `727.00` |
| `Live` | `Long` | `0.2675` | 983,420.00 USD | 0.00 USD | 321.54 USD | `-20.18%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 983,090.00 USD | 0.00 USD | 3,390.00 USD | `-19.89%` | `12,636.00` |
| `Live` | `Long` | `0.2735` | 979,700.00 USD | 0.00 USD | 220.99 USD | `-18.39%` | `808.00` |
| `Live` | `Long` | `0.2745` | 979,480.00 USD | 0.00 USD | 84,470.00 USD | `-18.10%` | `307,728.00` |
| `Live` | `Long` | `0.2785` | 895,010.00 USD | 0.00 USD | 15,180.00 USD | `-16.90%` | `54,497.00` |
| `Live` | `Long` | `0.2795` | 879,830.00 USD | 0.00 USD | 6,260.00 USD | `-16.60%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 873,580.00 USD | 0.00 USD | 13,300.00 USD | `-16.31%` | `47,408.00` |
| `Live` | `Long` | `0.2815` | 860,280.00 USD | 0.00 USD | 3,690.00 USD | `-16.01%` | `13,109.00` |
| `Live` | `Long` | `0.2825` | 856,590.00 USD | 0.00 USD | 838.74 USD | `-15.71%` | `2,969.00` |
| `Live` | `Long` | `0.2845` | 855,750.00 USD | 0.00 USD | 357.90 USD | `-15.11%` | `1,258.00` |
| `Live` | `Long` | `0.2855` | 855,390.00 USD | 0.00 USD | 6,300.00 USD | `-14.81%` | `22,055.00` |
| `Live` | `Long` | `0.2865` | 849,100.00 USD | 0.00 USD | 4,310.00 USD | `-14.52%` | `15,057.00` |
| `Live` | `Long` | `0.2905` | 844,780.00 USD | 0.00 USD | 821.82 USD | `-13.32%` | `2,829.00` |
| `Live` | `Long` | `0.2915` | 843,960.00 USD | 0.00 USD | 954.37 USD | `-13.02%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 843,010.00 USD | 0.00 USD | 213.08 USD | `-12.43%` | `726.00` |
| `Live` | `Long` | `0.2945` | 842,790.00 USD | 0.00 USD | 124.87 USD | `-12.13%` | `424.00` |
| `Live` | `Long` | `0.2955` | 842,670.00 USD | 0.00 USD | 156.61 USD | `-11.83%` | `530.00` |
| `Live` | `Long` | `0.2965` | 842,510.00 USD | 0.00 USD | 1,010.00 USD | `-11.53%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 841,500.00 USD | 0.00 USD | 759.68 USD | `-10.94%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 840,740.00 USD | 0.00 USD | 197.37 USD | `-10.64%` | `659.00` |
| `Live` | `Long` | `0.3005` | 840,550.00 USD | 0.00 USD | 10,620.00 USD | `-10.34%` | `35,336.00` |
| `Live` | `Long` | `0.3015` | 829,930.00 USD | 0.00 USD | 102.81 USD | `-10.04%` | `341.00` |
| `Live` | `Long` | `0.3025` | 829,820.00 USD | 0.00 USD | 2,510.00 USD | `-9.74%` | `8,314.00` |
| `Live` | `Long` | `0.3035` | 827,310.00 USD | 0.00 USD | 4,040.00 USD | `-9.44%` | `13,300.00` |
| `Live` | `Long` | `0.3045` | 823,270.00 USD | 0.00 USD | 138.24 USD | `-9.15%` | `454.00` |
| `Live` | `Long` | `0.3055` | 823,130.00 USD | 0.00 USD | 14,670.00 USD | `-8.85%` | `48,026.00` |
| `Live` | `Long` | `0.3065` | 808,460.00 USD | 0.00 USD | 5,900.00 USD | `-8.55%` | `19,262.00` |
| `Live` | `Long` | `0.3075` | 802,560.00 USD | 0.00 USD | 722.62 USD | `-8.25%` | `2,350.00` |
| `Live` | `Long` | `0.3085` | 801,840.00 USD | 0.00 USD | 291.53 USD | `-7.95%` | `945.00` |
| `Live` | `Long` | `0.3095` | 801,540.00 USD | 0.00 USD | 192.51 USD | `-7.65%` | `622.00` |
| `Live` | `Long` | `0.3105` | 801,350.00 USD | 0.00 USD | 820.96 USD | `-7.35%` | `2,644.00` |
| `Live` | `Long` | `0.3115` | 800,530.00 USD | 0.00 USD | 13,600.00 USD | `-7.06%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 786,930.00 USD | 0.00 USD | 17,810.00 USD | `-6.76%` | `56,977.00` |
| `Live` | `Long` | `0.3135` | 769,120.00 USD | 0.00 USD | 446.11 USD | `-6.46%` | `1,423.00` |
| `Live` | `Long` | `0.3145` | 768,680.00 USD | 0.00 USD | 577.11 USD | `-6.16%` | `1,835.00` |
| `Live` | `Long` | `0.3155` | 768,100.00 USD | 0.00 USD | 11,510.00 USD | `-5.86%` | `36,472.00` |
| `Live` | `Long` | `0.3165` | 756,590.00 USD | 0.00 USD | 935.89 USD | `-5.56%` | `2,957.00` |
| `Live` | `Long` | `0.3175` | 755,660.00 USD | 0.00 USD | 2,290.00 USD | `-5.27%` | `7,205.00` |
| `Live` | `Long` | `0.3185` | 753,370.00 USD | 0.00 USD | 1,300.00 USD | `-4.97%` | `4,080.00` |
| `Live` | `Long` | `0.3205` | 752,070.00 USD | 0.00 USD | 2,930.00 USD | `-4.37%` | `9,154.00` |
| `Live` | `Long` | `0.3235` | 749,140.00 USD | 0.00 USD | 128.43 USD | `-3.48%` | `397.00` |
| `Live` | `Long` | `0.3255` | 749,010.00 USD | 0.00 USD | 3,580.00 USD | `-2.88%` | `11,000.00` |
| `Live` | `Long` | `0.3275` | 745,430.00 USD | 0.00 USD | 163.42 USD | `-2.28%` | `499.00` |
| `Live` | `Long` | `0.3285` | 745,260.00 USD | 0.00 USD | 745,260.00 USD | `-1.98%` | `2,268,686.00` |
| `Live` | `Short` | `0.3445` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | `+2.79%` | `6,622.00` |
| `Live` | `Short` | `0.3505` | 10,930.00 USD | 8,650.00 USD | 0.00 USD | `+4.58%` | `24,688.00` |
| `Live` | `Short` | `0.3515` | 11,110.00 USD | 175.05 USD | 0.00 USD | `+4.88%` | `498.00` |
| `Live` | `Short` | `0.3525` | 11,220.00 USD | 112.45 USD | 0.00 USD | `+5.18%` | `319.00` |
| `Live` | `Short` | `0.3545` | 40,690.00 USD | 29,460.00 USD | 0.00 USD | `+5.77%` | `83,113.00` |
| `Live` | `Short` | `0.3635` | 53,050.00 USD | 12,360.00 USD | 0.00 USD | `+8.46%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 56,160.00 USD | 3,110.00 USD | 0.00 USD | `+9.35%` | `8,498.00` |
| `Live` | `Short` | `0.3705` | 56,440.00 USD | 278.99 USD | 0.00 USD | `+10.55%` | `753.00` |
| `Live` | `Short` | `0.3725` | 56,630.00 USD | 186.25 USD | 0.00 USD | `+11.14%` | `500.00` |
| `Live` | `Short` | `0.3735` | 63,690.00 USD | 7,070.00 USD | 0.00 USD | `+11.44%` | `18,920.00` |
| `Live` | `Short` | `0.3755` | 67,720.00 USD | 4,030.00 USD | 0.00 USD | `+12.04%` | `10,732.00` |
| `Live` | `Short` | `0.3775` | 67,830.00 USD | 104.19 USD | 0.00 USD | `+12.64%` | `276.00` |
| `Live` | `Short` | `0.3785` | 624,250.00 USD | 556,430.00 USD | 0.00 USD | `+12.93%` | `1,470,083.00` |
| `Live` | `Short` | `0.3795` | 625,030.00 USD | 773.04 USD | 0.00 USD | `+13.23%` | `2,037.00` |
| `Live` | `Short` | `0.3805` | 628,420.00 USD | 3,390.00 USD | 0.00 USD | `+13.53%` | `8,919.00` |
| `Live` | `Short` | `0.3835` | 628,530.00 USD | 115.05 USD | 0.00 USD | `+14.43%` | `300.00` |
| `Live` | `Short` | `0.3855` | 628,800.00 USD | 264.84 USD | 0.00 USD | `+15.02%` | `687.00` |
| `Live` | `Short` | `0.3865` | 2,170,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+15.32%` | `4,000,000.00` |
| `Live` | `Short` | `0.3895` | 2,180,000.00 USD | 4,760.00 USD | 0.00 USD | `+16.22%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 2,190,000.00 USD | 6,000.00 USD | 0.00 USD | `+16.51%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 2,190,000.00 USD | 1,480.00 USD | 0.00 USD | `+17.41%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 2,310,000.00 USD | 118,130.00 USD | 0.00 USD | `+17.71%` | `299,436.00` |
| `Live` | `Short` | `0.4015` | 2,310,000.00 USD | 327.62 USD | 0.00 USD | `+19.80%` | `816.00` |
| `Live` | `Short` | `0.4085` | 2,310,000.00 USD | 170.75 USD | 0.00 USD | `+21.89%` | `418.00` |
| `Live` | `Short` | `0.4095` | 2,310,000.00 USD | 239.56 USD | 0.00 USD | `+22.18%` | `585.00` |
| `Live` | `Short` | `0.4145` | 2,320,000.00 USD | 12,440.00 USD | 0.00 USD | `+23.68%` | `30,000.00` |
| `Live` | `Short` | `0.4165` | 2,410,000.00 USD | 94,510.00 USD | 0.00 USD | `+24.27%` | `226,922.00` |
| `Live` | `Short` | `0.4185` | 2,410,000.00 USD | 998.96 USD | 0.00 USD | `+24.87%` | `2,387.00` |
| `Live` | `Short` | `0.4235` | 2,410,000.00 USD | 134.25 USD | 0.00 USD | `+26.36%` | `317.00` |
| `Live` | `Short` | `0.4245` | 2,420,000.00 USD | 3,930.00 USD | 0.00 USD | `+26.66%` | `9,259.00` |
| `Live` | `Short` | `0.4335` | 2,420,000.00 USD | 1,500.00 USD | 0.00 USD | `+29.35%` | `3,464.00` |
| `Live` | `Short` | `0.4355` | 2,490,000.00 USD | 70,890.00 USD | 0.00 USD | `+29.94%` | `162,775.00` |
| `Live` | `Short` | `0.4365` | 2,490,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.24%` | `3,416.00` |
| `Live` | `Short` | `0.4415` | 2,490,000.00 USD | 377.48 USD | 0.00 USD | `+31.73%` | `855.00` |
| `Live` | `Short` | `0.4425` | 2,510,000.00 USD | 13,280.00 USD | 0.00 USD | `+32.03%` | `30,000.00` |
| `Live` | `Short` | `0.4435` | 2,510,000.00 USD | 3,460.00 USD | 0.00 USD | `+32.33%` | `7,800.00` |
| `Live` | `Short` | `0.4445` | 2,530,000.00 USD | 22,200.00 USD | 0.00 USD | `+32.63%` | `49,950.00` |
| `Live` | `Short` | `0.4455` | 2,530,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.93%` | `2,284.00` |
| `Live` | `Short` | `0.4465` | 2,540,000.00 USD | 5,520.00 USD | 0.00 USD | `+33.22%` | `12,352.00` |
| `Live` | `Short` | `0.4475` | 2,600,000.00 USD | 65,610.00 USD | 0.00 USD | `+33.52%` | `146,614.00` |
| `Live` | `Short` | `0.4675` | 2,600,000.00 USD | 270.22 USD | 0.00 USD | `+39.49%` | `578.00` |
| `Live` | `Short` | `0.4895` | 2,600,000.00 USD | 839.49 USD | 0.00 USD | `+46.05%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,610,000.00 USD | 5,120.00 USD | 0.00 USD | `+46.35%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,610,000.00 USD | 2,730.00 USD | 0.00 USD | `+49.04%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,640,000.00 USD | 23,320.00 USD | 0.00 USD | `+49.34%` | `46,591.00` |
| `Live` | `Short` | `0.5325` | 2,640,000.00 USD | 667.22 USD | 0.00 USD | `+58.88%` | `1,253.00` |
| `Live` | `Short` | `0.5355` | 2,640,000.00 USD | 1,170.00 USD | 0.00 USD | `+59.78%` | `2,193.00` |
| `Live` | `Short` | `0.5475` | 2,680,000.00 USD | 40,520.00 USD | 0.00 USD | `+63.36%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,680,000.00 USD | 3,060.00 USD | 0.00 USD | `+66.34%` | `5,483.00` |
| `Live` | `Short` | `0.5605` | 2,680,000.00 USD | 140.12 USD | 0.00 USD | `+67.24%` | `250.00` |
| `Live` | `Short` | `0.5765` | 3,430,000.00 USD | 747,860.00 USD | 0.00 USD | `+72.01%` | `1,297,248.00` |
| `Live` | `Short` | `0.5855` | 3,430,000.00 USD | 115.93 USD | 0.00 USD | `+74.70%` | `198.00` |
| `Live` | `Short` | `0.5935` | 3,430,000.00 USD | 4,900.00 USD | 0.00 USD | `+77.08%` | `8,250.00` |
| `Live` | `Short` | `0.6155` | 3,460,000.00 USD | 24,620.00 USD | 0.00 USD | `+83.65%` | `40,000.00` |
| `Live` | `Short` | `0.6265` | 3,460,000.00 USD | 379.03 USD | 0.00 USD | `+86.93%` | `605.00` |
| `Live` | `Short` | `0.6335` | 3,470,000.00 USD | 6,810.00 USD | 0.00 USD | `+89.02%` | `10,756.00` |
| `Live` | `Short` | `0.6505` | 3,570,000.00 USD | 102,000.00 USD | 0.00 USD | `+94.09%` | `156,809.00` |
| `Live` | `Short` | `0.6515` | 3,570,000.00 USD | 951.19 USD | 0.00 USD | `+94.39%` | `1,460.00` |
| `Live` | `Short` | `0.6545` | 3,570,000.00 USD | 706.21 USD | 0.00 USD | `+95.29%` | `1,079.00` |
| `Live` | `Short` | `0.6615` | 3,570,000.00 USD | 2,060.00 USD | 0.00 USD | `+97.37%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,580,000.00 USD | 3,740.00 USD | 0.00 USD | `+97.97%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0925` | 2,140,000.00 USD | 0.00 USD | 407.56 USD | `-72.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 2,140,000.00 USD | 0.00 USD | 198.45 USD | `-71.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 2,140,000.00 USD | 0.00 USD | 330.26 USD | `-57.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 2,140,000.00 USD | 0.00 USD | 1,750.00 USD | `-39.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 2,140,000.00 USD | 0.00 USD | 579.72 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2165` | 2,140,000.00 USD | 0.00 USD | 1,030.00 USD | `-35.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 2,140,000.00 USD | 0.00 USD | 515.61 USD | `-34.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 2,140,000.00 USD | 0.00 USD | 121.70 USD | `-31.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 2,140,000.00 USD | 0.00 USD | 705.61 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 2,140,000.00 USD | 0.00 USD | 159.20 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 2,140,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 2,140,000.00 USD | 0.00 USD | 127.51 USD | `-27.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 2,140,000.00 USD | 0.00 USD | 1,850.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 2,130,000.00 USD | 0.00 USD | 41,500.00 USD | `-24.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 2,090,000.00 USD | 0.00 USD | 1,920.00 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 2,090,000.00 USD | 0.00 USD | 664.01 USD | `-22.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 2,090,000.00 USD | 0.00 USD | 954.98 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 2,090,000.00 USD | 0.00 USD | 103.56 USD | `-21.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 2,090,000.00 USD | 0.00 USD | 695.50 USD | `-20.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 2,090,000.00 USD | 0.00 USD | 1,630.00 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 2,090,000.00 USD | 0.00 USD | 1,470.00 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 2,080,000.00 USD | 0.00 USD | 101.94 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 2,080,000.00 USD | 0.00 USD | 3,260.00 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 2,080,000.00 USD | 0.00 USD | 2,550.00 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 2,080,000.00 USD | 0.00 USD | 229.92 USD | `-15.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 2,080,000.00 USD | 0.00 USD | 8,010.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 2,070,000.00 USD | 0.00 USD | 11,610.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 2,060,000.00 USD | 0.00 USD | 111.19 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 2,060,000.00 USD | 0.00 USD | 433.42 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 2,060,000.00 USD | 0.00 USD | 2,710.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 2,060,000.00 USD | 0.00 USD | 503.95 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 2,050,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 2,050,000.00 USD | 0.00 USD | 193.11 USD | `-8.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 2,050,000.00 USD | 0.00 USD | 15,150.00 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 2,040,000.00 USD | 0.00 USD | 156.30 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 2,040,000.00 USD | 0.00 USD | 12,200.00 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 2,030,000.00 USD | 0.00 USD | 6,530.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 2,020,000.00 USD | 0.00 USD | 524,570.00 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 1,490,000.00 USD | 0.00 USD | 1,270.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 1,490,000.00 USD | 0.00 USD | 53,690.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 1,440,000.00 USD | 0.00 USD | 644.88 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 1,440,000.00 USD | 0.00 USD | 7,400.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 1,430,000.00 USD | 0.00 USD | 850.90 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 1,430,000.00 USD | 0.00 USD | 1,730.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 1,430,000.00 USD | 0.00 USD | 5,610.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 1,420,000.00 USD | 0.00 USD | 10,160.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 1,410,000.00 USD | 0.00 USD | 43,760.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 1,370,000.00 USD | 0.00 USD | 5,520.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 1,360,000.00 USD | 0.00 USD | 7,040.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 1,360,000.00 USD | 0.00 USD | 3,970.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 1,350,000.00 USD | 0.00 USD | 2,240.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 1,350,000.00 USD | 0.00 USD | 6,130.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 1,340,000.00 USD | 0.00 USD | 7,620.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 1,340,000.00 USD | 0.00 USD | 4,270.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 1,330,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 13,100.00 USD | 0.00 USD | 949.53 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 12,150.00 USD | 0.00 USD | 984.22 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 11,160.00 USD | 0.00 USD | 5,730.00 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 5,440.00 USD | 0.00 USD | 4,880.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 560.96 USD | 0.00 USD | 560.96 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 8,260.00 USD | 8,260.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 8,520.00 USD | 265.50 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 10,550.00 USD | 2,020.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 12,000.00 USD | 1,450.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 12,960.00 USD | 960.45 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 14,410.00 USD | 1,460.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 14,900.00 USD | 486.30 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 15,330.00 USD | 431.55 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 16,160.00 USD | 828.18 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 16,650.00 USD | 488.16 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 17,080.00 USD | 435.33 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 17,640.00 USD | 555.44 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 17,910.00 USD | 274.18 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 18,350.00 USD | 439.11 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 20,300.00 USD | 1,950.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 20,970.00 USD | 665.60 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 21,570.00 USD | 605.63 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 22,000.00 USD | 423.70 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 22,310.00 USD | 312.14 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 22,660.00 USD | 354.50 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 22,800.00 USD | 132.96 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 62,230.00 USD | 39,430.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 102,620.00 USD | 40,390.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 105,920.00 USD | 3,310.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 106,960.00 USD | 1,030.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 109,900.00 USD | 2,940.00 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 110,120.00 USD | 224.49 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 110,220.00 USD | 103.23 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 112,920.00 USD | 2,700.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 123,230.00 USD | 10,310.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 123,490.00 USD | 256.55 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 123,660.00 USD | 172.72 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 123,880.00 USD | 218.89 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 138,490.00 USD | 14,610.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 139,090.00 USD | 597.99 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 139,270.00 USD | 174.60 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 139,370.00 USD | 107.28 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 139,810.00 USD | 439.61 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 140,250.00 USD | 437.79 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 142,720.00 USD | 2,470.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 142,900.00 USD | 182.60 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 149,350.00 USD | 6,450.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 149,630.00 USD | 275.17 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 150,200.00 USD | 569.25 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 156,280.00 USD | 6,080.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 156,540.00 USD | 257.89 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 156,800.00 USD | 262.78 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 157,030.00 USD | 224.73 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 157,650.00 USD | 621.04 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 158,390.00 USD | 742.08 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 159,500.00 USD | 1,110.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 159,690.00 USD | 181.04 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 1,720,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 1,720,000.00 USD | 138.63 USD | 0.00 USD | `+16.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 1,720,000.00 USD | 276.40 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 1,720,000.00 USD | 126.24 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 1,720,000.00 USD | 2,400.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 1,720,000.00 USD | 647.13 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 1,720,000.00 USD | 1,200.00 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 1,790,000.00 USD | 71,490.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 1,800,000.00 USD | 864.28 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 1,800,000.00 USD | 3,920.00 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 1,880,000.00 USD | 79,330.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 1,880,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 1,880,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 1,880,000.00 USD | 138.07 USD | 0.00 USD | `+21.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 1,880,000.00 USD | 1,270.00 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 1,880,000.00 USD | 331.63 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 1,880,000.00 USD | 313.54 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 1,880,000.00 USD | 186.70 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 1,880,000.00 USD | 325.75 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 1,880,000.00 USD | 183.82 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 1,880,000.00 USD | 299.19 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 1,920,000.00 USD | 38,580.00 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 1,920,000.00 USD | 170.69 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 1,920,000.00 USD | 135.59 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 1,920,000.00 USD | 1,520.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 1,920,000.00 USD | 320.31 USD | 0.00 USD | `+34.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 1,930,000.00 USD | 5,340.00 USD | 0.00 USD | `+35.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 1,930,000.00 USD | 1,470.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 2,010,000.00 USD | 80,770.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 2,010,000.00 USD | 169.22 USD | 0.00 USD | `+46.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 2,010,000.00 USD | 153.79 USD | 0.00 USD | `+47.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 2,010,000.00 USD | 724.89 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 2,020,000.00 USD | 11,150.00 USD | 0.00 USD | `+49.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 2,030,000.00 USD | 1,930.00 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5175` | 2,030,000.00 USD | 2,280.00 USD | 0.00 USD | `+54.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 2,030,000.00 USD | 135.02 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6255` | 2,030,000.00 USD | 1,160.00 USD | 0.00 USD | `+86.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 2,030,000.00 USD | 240.85 USD | 0.00 USD | `+88.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 2,030,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 2,030,000.00 USD | 1,050.00 USD | 0.00 USD | `+99.76%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2953` | 23,430,000.00 USD | 0.00 USD | 23,430,000.00 USD | 82,070.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 23,340,000.00 USD | 0.00 USD | 23,340,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 23,200,000.00 USD | 0.00 USD | 23,200,000.00 USD | 122,540.00 USD | 36,820.00 USD | 59,640.00 USD |
| `7D` | `0.2971` | 22,980,000.00 USD | 0.00 USD | 22,980,000.00 USD | 89,290.00 USD | 34,680.00 USD | 52,660.00 USD |
| `7D` | `0.2977` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 54,000.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2981` | 16,770,000.00 USD | 0.00 USD | 16,770,000.00 USD | 25,600.00 USD | 3,620.00 USD | 10,710.00 USD |
| `7D` | `0.2983` | 22,710,000.00 USD | 0.00 USD | 22,710,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2985` | 16,730,000.00 USD | 0.00 USD | 16,730,000.00 USD | 101,850.00 USD | 10,860.00 USD | 12,310.00 USD |
| `1D` | `0.2989` | 16,600,000.00 USD | 0.00 USD | 16,600,000.00 USD | 26,190.00 USD | 0.00 USD | 8,790.00 USD |
| `7D` | `0.2989` | 22,490,000.00 USD | 0.00 USD | 22,490,000.00 USD | 117,420.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2993` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 55,190.00 USD | 33,830.00 USD | 56,800.00 USD |
| `7D` | `0.2995` | 22,330,000.00 USD | 0.00 USD | 22,330,000.00 USD | 6,450.00 USD | 69,130.00 USD | 80,320.00 USD |
| `1D` | `0.2997` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 600.83 USD | 28,790.00 USD | 46,110.00 USD |
| `1D` | `0.3001` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD |
| `7D` | `0.3001` | 22,170,000.00 USD | 0.00 USD | 22,170,000.00 USD | 0.00 USD | 34,510.00 USD | 93,100.00 USD |
| `1D` | `0.3005` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 15,600.00 USD | 7,870.00 USD | 18,440.00 USD |
| `7D` | `0.3007` | 22,050,000.00 USD | 0.00 USD | 22,050,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3009` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 35,140.00 USD | 8,400.00 USD | 16,090.00 USD |
| `1D` | `0.3013` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 17,320.00 USD | 3,170.00 USD | 9,220.00 USD |
| `7D` | `0.3013` | 22,010,000.00 USD | 0.00 USD | 22,010,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3017` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 1,010.00 USD | 8,490.00 USD | 9,760.00 USD |
| `7D` | `0.3019` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3021` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD |
| `1D` | `0.3025` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 2,600.00 USD | 2,050.00 USD | 17,010.00 USD |
| `7D` | `0.3025` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 4,850.00 USD | 22,200.00 USD | 55,840.00 USD |
| `1D` | `0.3029` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 21,910,000.00 USD | 0.00 USD | 21,910,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3033` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 1,070.00 USD | 8,320.00 USD | 12,600.00 USD |
| `1D` | `0.3037` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD |
| `7D` | `0.3037` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3041` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 1,130.00 USD | 9,300.00 USD | 75,700.00 USD |
| `1D` | `0.3045` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 9,410.00 USD | 13,170.00 USD | 7,480.00 USD |
| `1D` | `0.3049` | 15,930,000.00 USD | 0.00 USD | 15,930,000.00 USD | 38,210.00 USD | 11,440.00 USD | 62,400.00 USD |
| `7D` | `0.3049` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 18,020.00 USD | 0.00 USD | 106,090.00 USD |
| `1D` | `0.3053` | 15,810,000.00 USD | 0.00 USD | 15,810,000.00 USD | 57,250.00 USD | 20,580.00 USD | 49,310.00 USD |
| `7D` | `0.3055` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3057` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 19,420.00 USD | 2,350.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3065` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 36,490.00 USD | 26,740.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 21,650,000.00 USD | 0.00 USD | 21,650,000.00 USD | 6,430.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3069` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD |
| `1D` | `0.3073` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3073` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3077` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 350.20 USD | 6,130.00 USD | 0.00 USD |
| `7D` | `0.3079` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 38,480.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3081` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD |
| `1D` | `0.3085` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD |
| `7D` | `0.3085` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3089` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3093` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 83,770.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3101` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 21,380,000.00 USD | 0.00 USD | 21,380,000.00 USD | 72,010.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3105` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3113` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD |
| `7D` | `0.3115` | 21,240,000.00 USD | 0.00 USD | 21,240,000.00 USD | 5,160.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3117` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 15,480.00 USD | 12,220.00 USD | 17,620.00 USD |
| `1D` | `0.3121` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3121` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3125` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD |
| `7D` | `0.3127` | 21,020,000.00 USD | 0.00 USD | 21,020,000.00 USD | 16,080.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3129` | 15,130,000.00 USD | 0.00 USD | 15,130,000.00 USD | 3,990.00 USD | 28,470.00 USD | 29,100.00 USD |
| `1D` | `0.3133` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD |
| `7D` | `0.3133` | 20,890,000.00 USD | 0.00 USD | 20,890,000.00 USD | 10,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3137` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 20,880,000.00 USD | 0.00 USD | 20,880,000.00 USD | 12,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3141` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.3145` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD |
| `7D` | `0.3145` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3149` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 1,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 197,800.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3153` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 30,120.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.3157` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 13,270.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3157` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 403,130.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3161` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 5,650.00 USD | 2,990.00 USD | 0.00 USD |
| `7D` | `0.3163` | 19,720,000.00 USD | 0.00 USD | 19,720,000.00 USD | 478,060.00 USD | 174,600.00 USD | 189,520.00 USD |
| `1D` | `0.3165` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 46,090.00 USD | 30,980.00 USD | 9,000.00 USD |
| `1D` | `0.3169` | 14,810,000.00 USD | 0.00 USD | 14,810,000.00 USD | 2,610.00 USD | 10,820.00 USD | 20,780.00 USD |
| `7D` | `0.3169` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 414,720.00 USD | 104,590.00 USD | 135,950.00 USD |
| `1D` | `0.3173` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD |
| `7D` | `0.3175` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3177` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 47,770.00 USD | 8,980.00 USD | 30,890.00 USD |
| `1D` | `0.3181` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 251,300.00 USD | 40,890.00 USD | 68,400.00 USD |
| `7D` | `0.3181` | 17,960,000.00 USD | 0.00 USD | 17,960,000.00 USD | 744,820.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3185` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 149,850.00 USD | 52,920.00 USD | 51,330.00 USD |
| `7D` | `0.3187` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 409,740.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3189` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 172,980.00 USD | 5,580.00 USD | 48,660.00 USD |
| `1D` | `0.3193` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 154,490.00 USD | 107,560.00 USD | 180,830.00 USD |
| `7D` | `0.3193` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 192,420.00 USD | 123,840.00 USD | 247,300.00 USD |
| `1D` | `0.3197` | 13,320,000.00 USD | 0.00 USD | 13,320,000.00 USD | 74,370.00 USD | 118,340.00 USD | 160,310.00 USD |
| `7D` | `0.3199` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 5,810.00 USD | 191,160.00 USD | 267,030.00 USD |
| `1D` | `0.3201` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 208,440.00 USD | 48,100.00 USD | 111,260.00 USD |
| `1D` | `0.3205` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 163,900.00 USD | 31,270.00 USD | 102,160.00 USD |
| `7D` | `0.3205` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 172,060.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3209` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 89,060.00 USD | 29,040.00 USD | 54,070.00 USD |
| `7D` | `0.3211` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 561,850.00 USD | 135,070.00 USD | 244,340.00 USD |
| `1D` | `0.3213` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 55,660.00 USD | 30,340.00 USD | 107,830.00 USD |
| `1D` | `0.3217` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 8,400.00 USD | 33,860.00 USD | 146,990.00 USD |
| `7D` | `0.3217` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3221` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 98,430.00 USD | 33,430.00 USD | 72,520.00 USD |
| `7D` | `0.3223` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 649,350.00 USD | 265,170.00 USD | 156,030.00 USD |
| `1D` | `0.3225` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 72,740.00 USD | 33,350.00 USD | 202,490.00 USD |
| `1D` | `0.3229` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 91,630.00 USD | 55,060.00 USD | 129,350.00 USD |
| `7D` | `0.3229` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,650.00 USD |
| `1D` | `0.3233` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 56,470.00 USD | 35,600.00 USD | 49,900.00 USD |
| `7D` | `0.3235` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD |
| `1D` | `0.3237` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 6,420.00 USD | 83,630.00 USD | 171,270.00 USD |
| `1D` | `0.3241` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD |
| `7D` | `0.3241` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 434,620.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3245` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 256,740.00 USD | 54,650.00 USD | 265,030.00 USD |
| `7D` | `0.3247` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3249` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 792,700.00 USD | 90,860.00 USD | 176,670.00 USD |
| `1D` | `0.3253` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 217,740.00 USD | 107,140.00 USD | 423,830.00 USD |
| `7D` | `0.3253` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 339,740.00 USD |
| `1D` | `0.3257` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 567,900.00 USD | 48,220.00 USD | 229,640.00 USD |
| `7D` | `0.3259` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 432,530.00 USD | 308,400.00 USD | 503,650.00 USD |
| `1D` | `0.3261` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 173,320.00 USD | 371,060.00 USD | 555,160.00 USD |
| `1D` | `0.3265` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 90,110.00 USD | 156,570.00 USD | 345,910.00 USD |
| `7D` | `0.3265` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 78,960.00 USD | 324,810.00 USD | 500,270.00 USD |
| `1D` | `0.3269` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 217,410.00 USD | 143,860.00 USD | 378,850.00 USD |
| `7D` | `0.3271` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 318,340.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3273` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD |
| `1D` | `0.3277` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 327,480.00 USD | 76,150.00 USD | 161,500.00 USD |
| `7D` | `0.3277` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3281` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 106,720.00 USD | 73,120.00 USD | 120,850.00 USD |
| `7D` | `0.3283` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD |
| `1D` | `0.3285` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 0.00 USD | 48,460.00 USD | 79,430.00 USD |
| `1D` | `0.3289` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 155,850.00 USD | 21,810.00 USD | 155,080.00 USD |
| `7D` | `0.3289` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD |
| `1D` | `0.3293` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 977.29 USD | 60,450.00 USD | 165,140.00 USD |
| `7D` | `0.3295` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 255,900.00 USD | 83,080.00 USD | 279,220.00 USD |
| `1D` | `0.3297` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 166,310.00 USD | 18,090.00 USD | 0.00 USD |
| `1D` | `0.3301` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 36,460.00 USD | 58,700.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 184,120.00 USD | 47,610.00 USD | 0.00 USD |
| `1D` | `0.3305` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD |
| `7D` | `0.3307` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3309` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD |
| `1D` | `0.3313` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 61,660.00 USD | 128,440.00 USD | 183,340.00 USD |
| `7D` | `0.3313` | 850,120.00 USD | 0.00 USD | 850,120.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3317` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 27,700.00 USD | 58,950.00 USD | 0.00 USD |
| `7D` | `0.3319` | 799,470.00 USD | 0.00 USD | 799,470.00 USD | 0.00 USD | 57,890.00 USD | 196,110.00 USD |
| `1D` | `0.3321` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 18,060.00 USD | 23,430.00 USD | 100,730.00 USD |
| `1D` | `0.3325` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 51,310.00 USD | 9,670.00 USD | 0.00 USD |
| `7D` | `0.3325` | 545,470.00 USD | 0.00 USD | 545,470.00 USD | 251,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3329` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 64,380.00 USD | 0.00 USD | 39,970.00 USD |
| `7D` | `0.3331` | 294,230.00 USD | 0.00 USD | 294,230.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD |
| `1D` | `0.3333` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 92,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3337` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 34,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3345` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 20,610.00 USD | 8,820.00 USD | 0.00 USD |
| `1D` | `0.3349` | 987,790.00 USD | 0.00 USD | 987,790.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD |
| `1D` | `0.3369` | 957,160.00 USD | 0.00 USD | 957,160.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3377` | 884,240.00 USD | 0.00 USD | 884,240.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3397` | 254,160.00 USD | 0.00 USD | 254,160.00 USD | 0.00 USD | 0.00 USD | 254,160.00 USD |
| `1D` | `0.3401` | 554,610.00 USD | 0.00 USD | 554,610.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD |
| `7D` | `0.3402` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3403` | 376,470.00 USD | 376,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 376,470.00 USD |
| `1D` | `0.3405` | 334,040.00 USD | 0.00 USD | 334,040.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD |
| `1D` | `0.3409` | 139,820.00 USD | 139,820.00 USD | 0.00 USD | 112,120.00 USD | 0.00 USD | 27,700.00 USD |
| `1D` | `0.3409` | 279,630.00 USD | 279,630.00 USD | 0.00 USD | 112,120.00 USD | 0.00 USD | 27,700.00 USD |
| `7D` | `0.3409` | 852,850.00 USD | 852,850.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3413` | 360,460.00 USD | 360,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,830.00 USD |
| `7D` | `0.3415` | 974,140.00 USD | 974,140.00 USD | 0.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD |
| `1D` | `0.3417` | 901,510.00 USD | 901,510.00 USD | 0.00 USD | 343,500.00 USD | 0.00 USD | 197,540.00 USD |
| `1D` | `0.3421` | 972,680.00 USD | 972,680.00 USD | 0.00 USD | 71,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3421` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `7D` | `0.3427` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 229,350.00 USD | 384,540.00 USD |
| `1D` | `0.3429` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 60,980.00 USD | 95,980.00 USD | 85,070.00 USD |
| `1D` | `0.3433` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 105,330.00 USD | 167,240.00 USD | 30,950.00 USD |
| `7D` | `0.3433` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD |
| `1D` | `0.3437` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 117,260.00 USD | 62,980.00 USD |
| `1D` | `0.3441` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD |
| `1D` | `0.3445` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD |
| `7D` | `0.3445` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3449` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 97,620.00 USD | 92,440.00 USD | 183,340.00 USD |
| `7D` | `0.3451` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 196,110.00 USD |
| `1D` | `0.3453` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 130,670.00 USD | 47,460.00 USD | 84,370.00 USD |
| `1D` | `0.3457` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 170,670.00 USD | 57,370.00 USD | 553,330.00 USD |
| `7D` | `0.3457` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3461` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 250,210.00 USD | 190,690.00 USD | 242,890.00 USD |
| `7D` | `0.3463` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 251,240.00 USD | 290,920.00 USD | 205,410.00 USD |
| `1D` | `0.3465` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 86,270.00 USD | 67,330.00 USD | 142,350.00 USD |
| `1D` | `0.3469` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 130,280.00 USD | 42,550.00 USD | 75,450.00 USD |
| `7D` | `0.3469` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD |
| `1D` | `0.3473` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 34,590.00 USD | 35,130.00 USD | 31,160.00 USD |
| `7D` | `0.3475` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3477` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 51,860.00 USD | 48,500.00 USD | 77,670.00 USD |
| `1D` | `0.3481` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 73,970.00 USD | 38,390.00 USD | 64,980.00 USD |
| `7D` | `0.3481` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 32,530.00 USD | 42,810.00 USD |
| `1D` | `0.3485` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 9,350.00 USD | 46,810.00 USD | 76,450.00 USD |
| `7D` | `0.3487` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 19,250.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3489` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 41,500.00 USD | 23,850.00 USD | 61,240.00 USD |
| `1D` | `0.3493` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 3,620.00 USD | 33,350.00 USD | 0.00 USD |
| `7D` | `0.3493` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 93,150.00 USD | 52,660.00 USD |
| `1D` | `0.3497` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | 497,210.00 USD |
| `7D` | `0.3499` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 133,330.00 USD | 0.00 USD | 139,610.00 USD |
| `1D` | `0.3501` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 52,670.00 USD | 9,040.00 USD | 50,760.00 USD |
| `1D` | `0.3505` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD |
| `7D` | `0.3505` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 6,140.00 USD | 19,280.00 USD | 0.00 USD |
| `1D` | `0.3509` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 2,790.00 USD | 16,810.00 USD | 0.00 USD |
| `7D` | `0.3511` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3513` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD |
| `1D` | `0.3517` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 52,740.00 USD | 5,720.00 USD | 101,300.00 USD |
| `7D` | `0.3517` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 6,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3521` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 47,300.00 USD | 21,980.00 USD | 69,070.00 USD |
| `7D` | `0.3523` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 205,490.00 USD |
| `1D` | `0.3525` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 13,010.00 USD | 17,990.00 USD | 28,910.00 USD |
| `1D` | `0.3529` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 128,260.00 USD | 57,540.00 USD | 0.00 USD |
| `7D` | `0.3529` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 137,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3533` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 99,280.00 USD | 44,040.00 USD | 108,090.00 USD |
| `7D` | `0.3535` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 5,810.00 USD | 98,000.00 USD | 187,450.00 USD |
| `1D` | `0.3537` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 107,750.00 USD | 29,120.00 USD | 195,270.00 USD |
| `1D` | `0.3541` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 101,070.00 USD | 80,430.00 USD | 0.00 USD |
| `7D` | `0.3541` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 808,620.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3545` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 5,220.00 USD | 44,140.00 USD | 69,820.00 USD |
| `7D` | `0.3547` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3549` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 17,670.00 USD | 58,390.00 USD | 0.00 USD |
| `1D` | `0.3553` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 22,550.00 USD | 39,740.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3557` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 2,710.00 USD | 38,770.00 USD | 0.00 USD |
| `7D` | `0.3559` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 9,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3561` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 859.20 USD | 25,000.00 USD | 106,140.00 USD |
| `1D` | `0.3565` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 5,060.00 USD | 11,630.00 USD | 39,520.00 USD |
| `7D` | `0.3565` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 4,730.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3569` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 2,060.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `0.3571` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3573` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `0.3577` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 31,960.00 USD | 9,130.00 USD | 0.00 USD |
| `7D` | `0.3577` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3581` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD |
| `7D` | `0.3583` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 4,040.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3585` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD |
| `1D` | `0.3589` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `0.3589` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 10,970.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3593` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD |
| `7D` | `0.3595` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3597` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD |
| `1D` | `0.3601` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD |
| `7D` | `0.3601` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 7,660.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3605` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 61,950.00 USD | 32,860.00 USD | 94,650.00 USD |
| `7D` | `0.3607` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3609` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 76,130.00 USD | 25,740.00 USD | 133,760.00 USD |
| `1D` | `0.3613` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 13,080.00 USD | 59,640.00 USD | 203,600.00 USD |
| `7D` | `0.3613` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3617` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 226,310.00 USD | 50,630.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 3,550.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3621` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 144,510.00 USD | 75,820.00 USD | 71,510.00 USD |
| `1D` | `0.3625` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 100,410.00 USD | 49,330.00 USD | 0.00 USD |
| `7D` | `0.3625` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3629` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD |
| `7D` | `0.3631` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3633` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD |
| `1D` | `0.3637` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD |
| `7D` | `0.3637` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3641` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3645` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD |
| `1D` | `0.3649` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 96,700.00 USD | 59,680.00 USD | 195,820.00 USD |
| `7D` | `0.3649` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 180,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3653` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 303,010.00 USD | 19,500.00 USD | 165,330.00 USD |
| `7D` | `0.3655` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 681,380.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3657` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 218,660.00 USD | 149,310.00 USD | 163,370.00 USD |
| `1D` | `0.3661` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 277,650.00 USD | 88,330.00 USD | 96,250.00 USD |
| `7D` | `0.3661` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 685,520.00 USD | 66,940.00 USD | 238,480.00 USD |
| `1D` | `0.3665` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 468,570.00 USD | 117,940.00 USD | 66,840.00 USD |
| `7D` | `0.3667` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 419,350.00 USD | 34,510.00 USD | 166,250.00 USD |
| `1D` | `0.3669` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD |
| `1D` | `0.3673` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 52,240.00 USD | 102,840.00 USD | 158,510.00 USD |
| `7D` | `0.3673` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3677` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 494,570.00 USD | 41,730.00 USD | 191,130.00 USD |
| `7D` | `0.3679` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3681` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 310,830.00 USD | 87,330.00 USD | 103,470.00 USD |
| `1D` | `0.3685` | 17,900,000.00 USD | 17,900,000.00 USD | 0.00 USD | 327,450.00 USD | 152,380.00 USD | 93,220.00 USD |
| `7D` | `0.3685` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 2,020.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3689` | 18,410,000.00 USD | 18,410,000.00 USD | 0.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD |
| `7D` | `0.3691` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3693` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD |
| `1D` | `0.3697` | 18,770,000.00 USD | 18,770,000.00 USD | 0.00 USD | 155,550.00 USD | 83,650.00 USD | 17,010.00 USD |
| `7D` | `0.3697` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 4,850.00 USD | 175,510.00 USD | 55,840.00 USD |
| `1D` | `0.3701` | 19,530,000.00 USD | 19,530,000.00 USD | 0.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD |
| `7D` | `0.3703` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3705` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 249,050.00 USD | 8,320.00 USD | 560,920.00 USD |
| `1D` | `0.3709` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD |
| `7D` | `0.3709` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3713` | 21,870,000.00 USD | 21,870,000.00 USD | 0.00 USD | 482,060.00 USD | 90,010.00 USD | 804,260.00 USD |
| `7D` | `0.3715` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 3,410.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3717` | 22,400,000.00 USD | 22,400,000.00 USD | 0.00 USD | 44,980.00 USD | 220,760.00 USD | 269,700.00 USD |
| `1D` | `0.3721` | 22,560,000.00 USD | 22,560,000.00 USD | 0.00 USD | 9,410.00 USD | 62,750.00 USD | 85,090.00 USD |
| `7D` | `0.3721` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 786,960.00 USD |
| `1D` | `0.3725` | 23,640,000.00 USD | 23,640,000.00 USD | 0.00 USD | 512,060.00 USD | 31,730.00 USD | 537,700.00 USD |
| `7D` | `0.3727` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3729` | 24,150,000.00 USD | 24,150,000.00 USD | 0.00 USD | 33,900.00 USD | 128,180.00 USD | 349,570.00 USD |
| `1D` | `0.3733` | 24,950,000.00 USD | 24,950,000.00 USD | 0.00 USD | 115,910.00 USD | 23,870.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3737` | 25,210,000.00 USD | 25,210,000.00 USD | 0.00 USD | 164,450.00 USD | 94,700.00 USD | 0.00 USD |
| `7D` | `0.3739` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3741` | 25,730,000.00 USD | 25,730,000.00 USD | 0.00 USD | 51,150.00 USD | 71,420.00 USD | 403,580.00 USD |
| `1D` | `0.3745` | 26,110,000.00 USD | 26,110,000.00 USD | 0.00 USD | 37,630.00 USD | 35,840.00 USD | 305,620.00 USD |
| `7D` | `0.3745` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD |
| `1D` | `0.3749` | 26,880,000.00 USD | 26,880,000.00 USD | 0.00 USD | 229,090.00 USD | 20,770.00 USD | 520,920.00 USD |
| `1D` | `0.3753` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 134,010.00 USD | 0.00 USD | 31,010.00 USD |
| `1D` | `0.3757` | 27,320,000.00 USD | 27,320,000.00 USD | 0.00 USD | 23,190.00 USD | 5,790.00 USD | 247,210.00 USD |
| `7D` | `0.3757` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3761` | 28,550,000.00 USD | 28,550,000.00 USD | 0.00 USD | 303,200.00 USD | 73,190.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3765` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 18,380.00 USD | 24,840.00 USD | 12,250.00 USD |
| `1D` | `0.3769` | 28,640,000.00 USD | 28,640,000.00 USD | 0.00 USD | 0.00 USD | 32,810.00 USD | 0.00 USD |
| `7D` | `0.3769` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 18,890,000.00 USD | 18,890,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD |
| `7D` | `0.3793` | 19,510,000.00 USD | 19,510,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `7D` | `0.3805` | 19,510,000.00 USD | 19,510,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3811` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `0.3817` | 19,720,000.00 USD | 19,720,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `7D` | `0.3823` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `7D` | `0.3841` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3859` | 19,910,000.00 USD | 19,910,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 20,190,000.00 USD | 20,190,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 20,440,000.00 USD | 20,440,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3919` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3925` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 20,810,000.00 USD | 20,810,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 107,420.00 USD | 8,610.00 USD | 110,780.00 USD |
| `7D` | `0.3961` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 123,320.00 USD | 54,030.00 USD | 7,040.00 USD |
| `7D` | `0.3967` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 21,520,000.00 USD | 21,520,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 21,630,000.00 USD | 21,630,000.00 USD | 0.00 USD | 57,460.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 21,660,000.00 USD | 21,660,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 21,700,000.00 USD | 21,700,000.00 USD | 0.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD |
| `7D` | `0.3997` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 0.00 USD | 27,240.00 USD | 0.00 USD |
| `7D` | `0.4001` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `438.20M` | Total OI Tokens: `1,284,469,004.8 TRX`
  * 1h OI Change: `+4.18%` | 4h OI Change: `+7.13%` | 24h OI Change: `+53.02%`
  * Exchange Breakdown: Binance=`109.59M` | Bybit=`86.90M` | OKX=`28.04M` | Hyperliquid=`19.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-140.59K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0759%` | **USDT OKX** | `-0.3858%` |
| **USDT Bybit** | `0.0228%` | **USDT KuCoin** | `-0.0363%` |
| **USDT MEXC** | `-0.0754%` | **USDT BingX** | `0.0402%` |
| **USDT Gate** | `-0.1976%` | **USDT Bitget** | `-0.2060%` |
| **CoinM Binance** | `-0.1425%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `47.42%` | `52.58%` | `0.90` | 3,700,000.00 USD |
| `15M` | `Binance` | `52.09%` | `47.91%` | `1.09` | 1,170,000.00 USD |
| `15M` | `OKX` | `54%` | `46%` | `1.17` | 343,030.00 USD |
| `15M` | `Bybit` | `53.02%` | `46.98%` | `1.13` | 490,380.00 USD |
| `15M` | `KuCoin` | `50.28%` | `49.72%` | `1.01` | 18,560.00 USD |
| `15M` | `Gate` | `77.78%` | `22.22%` | `3.50` | 119,050.00 USD |
| `15M` | `Bitget` | `62.24%` | `37.76%` | `1.65` | 44,490.00 USD |
| `15M` | `BingX` | `47.83%` | `52.17%` | `0.92` | 111,840.00 USD |
| `15M` | `MEXC` | `29.01%` | `70.99%` | `0.41` | 315,060.00 USD |
| `15M` | `Bitunix` | `61.97%` | `38.03%` | `1.63` | 71,130.00 USD |
| `15M` | `Hyperliquid` | `76.06%` | `23.94%` | `3.18` | 49,700.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `40.7%` | `59.3%` | `0.69` | 646,700.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 229,450.00 USD |
| `15M` | `HTX` | `68.31%` | `31.69%` | `2.16` | 10,150.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.71%` | `9.29%` | `9.76` | 78,070.00 USD |
| `15M` | `Aster` | `68.38%` | `31.62%` | `2.16` | 1,030.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `71.82%` | `28.18%` | `2.55` | 5,400.00 USD |
| `15M` | `Whale Positions` | `52.09%` | `47.91%` | `1.09` | 1,170,000.00 USD |
| `15M` | `Global Accounts` | `47.42%` | `52.58%` | `0.90` | 3,700,000.00 USD |
| `1H` | `TRX` | `43.70%` | `56.30%` | `0.78` | 18,130,000.00 USD |
| `1H` | `Binance` | `44.61%` | `55.39%` | `0.81` | 5,440,000.00 USD |
| `1H` | `OKX` | `46.27%` | `53.73%` | `0.86` | 1,850,000.00 USD |
| `1H` | `Bybit` | `54.75%` | `45.25%` | `1.21` | 2,190,000.00 USD |
| `1H` | `KuCoin` | `45.1%` | `54.9%` | `0.82` | 291,980.00 USD |
| `1H` | `Gate` | `49.59%` | `50.41%` | `0.98` | 449,020.00 USD |
| `1H` | `Bitget` | `56.89%` | `43.11%` | `1.32` | 632,920.00 USD |
| `1H` | `BingX` | `28.82%` | `71.18%` | `0.40` | 877,880.00 USD |
| `1H` | `MEXC` | `57.12%` | `42.88%` | `1.33` | 1,580,000.00 USD |
| `1H` | `Bitunix` | `43.8%` | `56.2%` | `0.78` | 355,630.00 USD |
| `1H` | `Hyperliquid` | `55.08%` | `44.92%` | `1.23` | 337,880.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.2%` | `53.8%` | `0.86` | 2,700,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `13.28%` | `86.72%` | `0.15` | 1,130,000.00 USD |
| `1H` | `HTX` | `49.84%` | `50.16%` | `0.99` | 51,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `80.17%` | `19.83%` | `4.04` | 235,810.00 USD |
| `1H` | `Aster` | `21.16%` | `78.84%` | `0.27` | 10,280.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `58.92%` | `41.08%` | `1.43` | 5,010.00 USD |
| `1H` | `Whale Positions` | `44.61%` | `55.39%` | `0.81` | 5,440,000.00 USD |
| `1H` | `Global Accounts` | `43.70%` | `56.30%` | `0.78` | 18,130,000.00 USD |
| `4H` | `TRX` | `49.30%` | `50.70%` | `0.97` | 157,710,000.00 USD |
| `4H` | `Binance` | `50.29%` | `49.71%` | `1.01` | 63,100,000.00 USD |
| `4H` | `OKX` | `46.82%` | `53.18%` | `0.88` | 19,300,000.00 USD |
| `4H` | `Bybit` | `57.15%` | `42.85%` | `1.33` | 25,820,000.00 USD |
| `4H` | `KuCoin` | `49.13%` | `50.87%` | `0.97` | 3,160,000.00 USD |
| `4H` | `Gate` | `44.1%` | `55.9%` | `0.79` | 6,780,000.00 USD |
| `4H` | `Bitget` | `56.33%` | `43.67%` | `1.29` | 6,110,000.00 USD |
| `4H` | `BingX` | `27.52%` | `72.48%` | `0.38` | 2,960,000.00 USD |
| `4H` | `MEXC` | `53.58%` | `46.42%` | `1.15` | 1,430,000.00 USD |
| `4H` | `Bitunix` | `51.82%` | `48.18%` | `1.08` | 2,180,000.00 USD |
| `4H` | `Hyperliquid` | `52.29%` | `47.71%` | `1.10` | 13,810,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.54%` | `50.46%` | `0.98` | 1,990,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.7%` | `81.3%` | `0.23` | 7,750,000.00 USD |
| `4H` | `HTX` | `50.13%` | `49.87%` | `1.01` | 396,440.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `77.47%` | `22.53%` | `3.44` | 964,640.00 USD |
| `4H` | `Aster` | `38.06%` | `61.94%` | `0.61` | 1,000,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.99%` | `43.01%` | `1.33` | 978,520.00 USD |
| `4H` | `Whale Positions` | `50.29%` | `49.71%` | `1.01` | 63,100,000.00 USD |
| `4H` | `Global Accounts` | `49.30%` | `50.70%` | `0.97` | 157,710,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3360` | `0.3335` | 1,833,198.85 USD | 904,870.52 USD | 928,328.33 USD | -23,457.81 USD | `-1.28%` | `23B / 24S` |
| `5:00 UTC` | `0.3348` | `0.3371` | `0.3348` | `0.3399` | `0.3343` | 3,666,829.89 USD | 1,892,139.69 USD | 1,774,690.20 USD | 117,449.48 USD | `+3.20%` | `16B / 11S` |
| `0:00 UTC` | `0.3400` | `0.3396` | `0.3400` | `0.3409` | `0.3377` | 6,444,023.59 USD | 2,423,214.82 USD | 4,020,808.77 USD | -1,597,593.95 USD | `-24.79%` | `17B / 14S` |
| `5:00 UTC` | `0.3414` | `0.3405` | `0.3414` | `0.3423` | `0.3377` | 3,655,789.47 USD | 1,570,218.83 USD | 2,085,570.64 USD | -515,351.81 USD | `-14.10%` | `8B / 17S` |

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
| `5m` | 244,060.00 USD | -174,250.00 USD | **`ACCUMULATION`** |
| `15m` | 399,240.00 USD | 556,340.00 USD | **`ACCUMULATION`** |
| `30m` | -1,340,000.00 USD | -553,980.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,610,000.00 USD | -828,480.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,310,000.00 USD | 253,380.00 USD | **`DISTRIBUTION`** |
| `4h` | -110,380.00 USD | 3,540,000.00 USD | **`ACCUMULATION`** |
| `6h` | 6,040,000.00 USD | -6,830,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 11,020,000.00 USD | -8,060,000.00 USD | **`ACCUMULATION`** |
| `12h` | 16,310,000.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,780,000.00 USD | 5,040,000.00 USD | **`ACCUMULATION`** |
| `1w` | 10,570,000.00 USD | 3,480,000.00 USD | **`ACCUMULATION`** |
| `30d` | -11,590,000.00 USD | 4,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+244.06K` | 15m=`+399.24K` | 1h=`-2.61M` | 24h=`+18.78M`
* Futures Capital Netflows: 5m=`-174.25K` | 15m=`+556.34K` | 1h=`-828.48K` | 24h=`+5.04M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3387` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3299` (Risk Distance: `0.0088` pts)
  * +2.5R Take Profit: `0.3607`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3666` (Risk Distance: `0.0088` pts)
  * +2.5R Take Profit: `0.3358`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3440`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
