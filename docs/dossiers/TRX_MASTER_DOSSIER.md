# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:45:52 IST` (`2026-10-30 11:15:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3380` | **Live Ask Quote**: `0.3406` | **Mid Price**: `0.3393`
- **Spread Points**: `26.00` | **Spread BPS**: `76.63 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3393` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3417` | Lower -3.00σ Band: `0.3369`
  * Upper +2.51σ Band: `0.3412` | Lower -2.51σ Band: `0.3374`
  * Upper +2.01σ Band: `0.3407` | Lower -2.01σ Band: `0.3379`
  * Upper +2.00σ Band: `0.3407` | Lower -2.00σ Band: `0.3379`
  * Upper +1.28σ Band: `0.3403` | Lower -1.28σ Band: `0.3383`
  * Upper +1.00σ Band: `0.3400` | Lower -1.00σ Band: `0.3386`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3393` | EMA-20=`0.3393` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3393` (Slope: `+0.0000`) | EMA-100=`0.3393`
  * Institutional Anchors: EMA-144=`0.3393` | EMA-200=`0.3393` (Slope: `+0.0000`) | EMA-233=`0.3393`
- **Range Boundaries**: 24H High=`0.3427` | 24H Low=`0.3359` | Weekly High=`0.3461` | Weekly Low=`0.3325`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-5.13%`)
  * Point of Control (POC) = `0.3513` (Distance: `-3.39%`)
  * Value Area Low (VAL) = `0.3387` (Distance: `+0.22%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3458` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3418` | Low=`0.3319`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3379` - `0.3407`
  * Optimal Trade Entry (OTE 0.705): `0.3400`
  * Structural Invalidation Anchor (0.786): `0.3420`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3421` | `0.3424` | `0.3409` | `0.3418` | `2,933,803` | 1,002,010.76 USD | -177,283.15 USD | `-17.69%` | -4,914,905.74 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3418` | `0.3426` | `0.3400` | `0.3401` | `5,596,755` | 1,913,323.34 USD | -390,396.57 USD | `-20.40%` | -5,305,302.32 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3401` | `0.3404` | `0.3393` | `0.3395` | `621,484` | 211,116.65 USD | -63,513.30 USD | `-30.08%` | -5,368,815.62 USD | `+0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3391` | `0.3409` | `0.3377` | `0.3406` | `18,974,049` | 6,444,023.59 USD | -1,597,593.95 USD | `-24.79%` | -4,130,361.55 USD | `-1.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3406` | `0.3423` | `0.3377` | `0.3421` | `11,488,452` | 3,912,907.38 USD | -607,261.04 USD | `-15.52%` | -4,737,622.59 USD | `-0.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3421` | `0.3426` | `0.3393` | `0.3397` | `9,185,835` | 3,137,925.92 USD | -623,803.22 USD | `-19.88%` | -5,361,425.81 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3324` | `0.3367` | `0.3318` | `0.3346` | `29,287,422` | 9,766,957.28 USD | -468,481.97 USD | `-4.80%` | -2,562,480.69 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3346` | `0.3423` | `0.3335` | `0.3421` | `46,813,628` | 15,856,959.71 USD | -2,110,863.32 USD | `-13.31%` | -4,673,344.01 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3421` | `0.3426` | `0.3393` | `0.3397` | `9,185,835` | 3,137,925.92 USD | -623,803.22 USD | `-19.88%` | -5,297,147.23 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3426` | `0.3307` | `0.3397` | `124,708,304` | 41,884,928.79 USD | -2,893,020.29 USD | `-6.91%` | -5,299,074.17 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3426` | `0.3307` | `0.3397` | `124,708,304` | 41,884,928.79 USD | -2,893,020.29 USD | `-6.91%` | -5,299,074.17 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3393`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1085` | `0xecb6...2b00` | `LONG` | 2,003,155.21 USD | `5,879,390.00` | `0.3344` | `0.3411` | `0.000000` | 37,166.62 USD | `+1.86%` | `10X Cross` |
| `1275` | `0x8dd7...fa30` | `SHORT` | 1,702,800.00 USD | `5,000,000.00` | `0.3334` | `0.3411` | `0.3729` | -35,999.93 USD | `-2.11%` | `6X Cross` |
| `1576` | `0xeadc...9d55` | `LONG` | 1,363,360.00 USD | `4,000,000.00` | `0.3421` | `0.3411` | `0.000000` | -5,118.09 USD | `-0.38%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,464.28 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3312 USD [API] | `2026-10-29 18:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.3314` | 5,738.36 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 5.74K USD at 0.3314 USD [API] | `2026-10-29 18:33:20` |
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 9,348.50 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 9.35K USD at 0.3312 USD [API] | `2026-10-29 20:08:06` |
| `ANNOUNCEMENT` | `INFO` | `0.3309` | 6,863.03 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.86K USD at 0.3309 USD [API] | `2026-10-29 20:34:22` |


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
| `Live` | `Long Liquidation` | `0.0865` | 179.83 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 878.45 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 7,990.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 143.51 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 27,380.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,290.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 265.88 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 123.26 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 11,500.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 863.51 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 35,330.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,760.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 23,490.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 648.96 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 10,440.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 2,520.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 4,150.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 255.53 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 174.38 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 207.50 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 100.37 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 628.80 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 1,200.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 14,200.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 223.11 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,520.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 710.34 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 493.04 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 156.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,420.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 807.21 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 568.81 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 3,100.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 464.79 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 11,840.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 292.41 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 999,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 107.74 USD | 999,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 4,550.00 USD | 998,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 994,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 991,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 241.18 USD | 991,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 991,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,150.00 USD | 991,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 4,160.00 USD | 987,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 80,520.00 USD | 983,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 15,180.00 USD | 903,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 887,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 13,300.00 USD | 881,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 3,690.00 USD | 868,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 838.74 USD | 864,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 6,250.00 USD | 863,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 552.44 USD | 857,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,150.00 USD | 857,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2895` | 297.90 USD | 852,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 522.90 USD | 852,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 852,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 851,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 850,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 23,430,000.00 USD | 23,430,000.00 USD | 82,070.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 850,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 23,340,000.00 USD | 23,340,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,200,000.00 USD | 23,200,000.00 USD | 122,540.00 USD | 36,820.00 USD | 59,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,010.00 USD | 850,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 22,980,000.00 USD | 22,980,000.00 USD | 89,290.00 USD | 34,680.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 22,800,000.00 USD | 22,800,000.00 USD | 54,000.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 17,570,000.00 USD | 17,570,000.00 USD | 25,600.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 22,710,000.00 USD | 22,710,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 849,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2986` | 17,540,000.00 USD | 17,540,000.00 USD | 111,780.00 USD | 10,860.00 USD | 11,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 22,490,000.00 USD | 22,490,000.00 USD | 117,420.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2991` | 17,400,000.00 USD | 17,400,000.00 USD | 57,070.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,330,000.00 USD | 22,330,000.00 USD | 6,450.00 USD | 69,130.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 848,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2996` | 17,340,000.00 USD | 17,340,000.00 USD | 13,470.00 USD | 62,620.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3001` | 17,170,000.00 USD | 17,170,000.00 USD | 8,760.00 USD | 14,600.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 34,510.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 848,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3006` | 17,120,000.00 USD | 17,120,000.00 USD | 16,450.00 USD | 7,870.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,050,000.00 USD | 22,050,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3011` | 17,060,000.00 USD | 17,060,000.00 USD | 51,610.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 22,010,000.00 USD | 22,010,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 838,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3016` | 17,000,000.00 USD | 17,000,000.00 USD | 1,010.00 USD | 9,650.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3021` | 16,970,000.00 USD | 16,970,000.00 USD | 14,850.00 USD | 6,560.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 22,000,000.00 USD | 22,000,000.00 USD | 4,850.00 USD | 22,200.00 USD | 55,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 838,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3026` | 16,930,000.00 USD | 16,930,000.00 USD | 2,880.00 USD | 2,050.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3031` | 16,910,000.00 USD | 16,910,000.00 USD | 24,620.00 USD | 8,320.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 21,910,000.00 USD | 21,910,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 835,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3036` | 16,870,000.00 USD | 16,870,000.00 USD | 1,260.00 USD | 3,230.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3037` | 21,860,000.00 USD | 21,860,000.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3041` | 16,850,000.00 USD | 16,850,000.00 USD | 1,130.00 USD | 9,300.00 USD | 75,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 831,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3046` | 16,770,000.00 USD | 16,770,000.00 USD | 41,400.00 USD | 18,130.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 21,860,000.00 USD | 21,860,000.00 USD | 18,020.00 USD | 0.00 USD | 106,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3051` | 16,700,000.00 USD | 16,700,000.00 USD | 24,960.00 USD | 13,680.00 USD | 73,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 21,730,000.00 USD | 21,730,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 831,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3056` | 16,590,000.00 USD | 16,590,000.00 USD | 48,690.00 USD | 13,380.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3061` | 16,490,000.00 USD | 16,490,000.00 USD | 19,420.00 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 21,730,000.00 USD | 21,730,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 816,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3066` | 16,410,000.00 USD | 16,410,000.00 USD | 38,030.00 USD | 29,620.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 21,650,000.00 USD | 21,650,000.00 USD | 6,430.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 16,310,000.00 USD | 16,310,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 21,640,000.00 USD | 21,640,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 810,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3076` | 16,290,000.00 USD | 16,290,000.00 USD | 23,570.00 USD | 8,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 21,630,000.00 USD | 21,630,000.00 USD | 38,480.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 16,260,000.00 USD | 16,260,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 21,530,000.00 USD | 21,530,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 810,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3086` | 16,230,000.00 USD | 16,230,000.00 USD | 598.72 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 16,220,000.00 USD | 16,220,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 21,530,000.00 USD | 21,530,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 809,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3096` | 16,220,000.00 USD | 16,220,000.00 USD | 21,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 21,530,000.00 USD | 21,530,000.00 USD | 83,770.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3101` | 16,190,000.00 USD | 16,190,000.00 USD | 42,020.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 21,380,000.00 USD | 21,380,000.00 USD | 72,010.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 14,140.00 USD | 809,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3106` | 16,090,000.00 USD | 16,090,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 21,250,000.00 USD | 21,250,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 21,240,000.00 USD | 21,240,000.00 USD | 5,160.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 245.77 USD | 795,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3116` | 16,070,000.00 USD | 16,070,000.00 USD | 2,250.00 USD | 17,210.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3121` | 16,030,000.00 USD | 16,030,000.00 USD | 24,790.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 21,200,000.00 USD | 21,200,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 18,110.00 USD | 795,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3126` | 15,970,000.00 USD | 15,970,000.00 USD | 15,000.00 USD | 13,530.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 21,020,000.00 USD | 21,020,000.00 USD | 16,080.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 15,930,000.00 USD | 15,930,000.00 USD | 3,900.00 USD | 28,470.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 20,890,000.00 USD | 20,890,000.00 USD | 10,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 141.39 USD | 777,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3136` | 15,880,000.00 USD | 15,880,000.00 USD | 5,830.00 USD | 34,540.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 20,880,000.00 USD | 20,880,000.00 USD | 12,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 15,830,000.00 USD | 15,830,000.00 USD | 7,520.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 20,870,000.00 USD | 20,870,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 1,490.00 USD | 776,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3146` | 15,810,000.00 USD | 15,810,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3151` | 15,810,000.00 USD | 15,810,000.00 USD | 6,830.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 20,550,000.00 USD | 20,550,000.00 USD | 197,800.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,150.00 USD | 775,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3156` | 15,770,000.00 USD | 15,770,000.00 USD | 35,910.00 USD | 3,680.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 20,280,000.00 USD | 20,280,000.00 USD | 403,130.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 15,720,000.00 USD | 15,720,000.00 USD | 7,880.00 USD | 2,990.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 19,720,000.00 USD | 19,720,000.00 USD | 478,060.00 USD | 174,600.00 USD | 189,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3166` | 15,710,000.00 USD | 15,710,000.00 USD | 46,600.00 USD | 37,250.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 18,880,000.00 USD | 18,880,000.00 USD | 414,720.00 USD | 104,590.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 15,610,000.00 USD | 15,610,000.00 USD | 9,020.00 USD | 35,130.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 18,220,000.00 USD | 18,220,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 3,440.00 USD | 774,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3176` | 15,530,000.00 USD | 15,530,000.00 USD | 52,670.00 USD | 9,730.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 15,430,000.00 USD | 15,430,000.00 USD | 259,620.00 USD | 43,420.00 USD | 72,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 17,960,000.00 USD | 17,960,000.00 USD | 744,820.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 17,020.00 USD | 770,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3186` | 15,060,000.00 USD | 15,060,000.00 USD | 149,850.00 USD | 58,500.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 16,960,000.00 USD | 16,960,000.00 USD | 409,740.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3191` | 14,790,000.00 USD | 14,790,000.00 USD | 251,300.00 USD | 13,910.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 16,420,000.00 USD | 16,420,000.00 USD | 192,420.00 USD | 123,840.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 285.31 USD | 753,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3196` | 14,440,000.00 USD | 14,440,000.00 USD | 95,570.00 USD | 187,520.00 USD | 252,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 15,860,000.00 USD | 15,860,000.00 USD | 5,810.00 USD | 191,160.00 USD | 267,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3201` | 13,900,000.00 USD | 13,900,000.00 USD | 263,400.00 USD | 72,570.00 USD | 153,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 15,400,000.00 USD | 15,400,000.00 USD | 172,060.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 455.75 USD | 753,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3206` | 13,410,000.00 USD | 13,410,000.00 USD | 164,150.00 USD | 31,270.00 USD | 142,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 13,080,000.00 USD | 13,080,000.00 USD | 143,990.00 USD | 48,000.00 USD | 113,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 15,040,000.00 USD | 15,040,000.00 USD | 561,850.00 USD | 135,070.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3215` | 127.64 USD | 753,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3216` | 12,770,000.00 USD | 12,770,000.00 USD | 8,430.00 USD | 33,650.00 USD | 155,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 14,090,000.00 USD | 14,090,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3221` | 12,570,000.00 USD | 12,570,000.00 USD | 98,860.00 USD | 45,010.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 13,640,000.00 USD | 13,640,000.00 USD | 649,350.00 USD | 265,170.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3225` | 3,930.00 USD | 752,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3226` | 12,360,000.00 USD | 12,360,000.00 USD | 73,350.00 USD | 33,350.00 USD | 245,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 12,570,000.00 USD | 12,570,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 12,010,000.00 USD | 12,010,000.00 USD | 92,790.00 USD | 55,060.00 USD | 120,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 10,910,000.00 USD | 10,910,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3236` | 11,740,000.00 USD | 11,740,000.00 USD | 61,120.00 USD | 106,740.00 USD | 175,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 11,390,000.00 USD | 11,390,000.00 USD | 966.93 USD | 40,210.00 USD | 132,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 9,620,000.00 USD | 9,620,000.00 USD | 434,620.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3246` | 11,220,000.00 USD | 11,220,000.00 USD | 383,940.00 USD | 95,040.00 USD | 339,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 8,890,000.00 USD | 8,890,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 10,400,000.00 USD | 10,400,000.00 USD | 744,360.00 USD | 100,090.00 USD | 387,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 7,560,000.00 USD | 7,560,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 339,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3256` | 9,170,000.00 USD | 9,170,000.00 USD | 662,530.00 USD | 100,910.00 USD | 365,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 5,870,000.00 USD | 5,870,000.00 USD | 432,530.00 USD | 308,400.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3261` | 8,040,000.00 USD | 8,040,000.00 USD | 206,710.00 USD | 375,900.00 USD | 555,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 4,620,000.00 USD | 4,620,000.00 USD | 78,960.00 USD | 324,810.00 USD | 500,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3265` | 190.35 USD | 190.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3266` | 6,900,000.00 USD | 6,900,000.00 USD | 91,040.00 USD | 193,200.00 USD | 374,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3271` | 6,250,000.00 USD | 6,250,000.00 USD | 255,030.00 USD | 131,960.00 USD | 412,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 3,720,000.00 USD | 3,720,000.00 USD | 318,340.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 745,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3276` | 5,450,000.00 USD | 5,450,000.00 USD | 269,510.00 USD | 70,470.00 USD | 255,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3277` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3281` | 4,850,000.00 USD | 4,850,000.00 USD | 164,690.00 USD | 78,800.00 USD | 138,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 2,880,000.00 USD | 2,880,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 745,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3286` | 4,470,000.00 USD | 4,470,000.00 USD | 45,960.00 USD | 48,460.00 USD | 162,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3291` | 4,210,000.00 USD | 4,210,000.00 USD | 109,890.00 USD | 66,400.00 USD | 152,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 2,170,000.00 USD | 2,170,000.00 USD | 255,900.00 USD | 83,080.00 USD | 279,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3296` | 3,880,000.00 USD | 3,880,000.00 USD | 167,290.00 USD | 15,860.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3301` | 3,610,000.00 USD | 3,610,000.00 USD | 36,460.00 USD | 76,790.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 1,550,000.00 USD | 1,550,000.00 USD | 184,120.00 USD | 47,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3306` | 3,470,000.00 USD | 3,470,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 1,320,000.00 USD | 1,320,000.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3311` | 3,250,000.00 USD | 3,250,000.00 USD | 28,510.00 USD | 122,460.00 USD | 599,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 850,120.00 USD | 850,120.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3316` | 2,500,000.00 USD | 2,500,000.00 USD | 44,750.00 USD | 113,100.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 799,470.00 USD | 799,470.00 USD | 0.00 USD | 57,890.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3321` | 2,310,000.00 USD | 2,310,000.00 USD | 45,760.00 USD | 23,430.00 USD | 100,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 545,470.00 USD | 545,470.00 USD | 251,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3326` | 2,140,000.00 USD | 2,140,000.00 USD | 69,290.00 USD | 9,670.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3331` | 2,020,000.00 USD | 2,020,000.00 USD | 139,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 294,230.00 USD | 294,230.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3336` | 1,880,000.00 USD | 1,880,000.00 USD | 34,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3346` | 1,850,000.00 USD | 1,850,000.00 USD | 20,610.00 USD | 8,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3351` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3371` | 1,790,000.00 USD | 1,790,000.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3376` | 1,720,000.00 USD | 1,720,000.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 254,160.00 USD | 254,160.00 USD | 0.00 USD | 0.00 USD | 254,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3401` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 376,470.00 USD | 376,470.00 USD | 0.00 USD | 0.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3406` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 852,850.00 USD | 852,850.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3411` | 832,870.00 USD | 832,870.00 USD | 112,120.00 USD | 0.00 USD | 45,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 974,140.00 USD | 974,140.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3416` | 674,910.00 USD | 674,910.00 USD | 343,500.00 USD | 0.00 USD | 211,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3421` | 119,990.00 USD | 119,990.00 USD | 71,180.00 USD | 0.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 229,350.00 USD | 384,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 490,220.00 USD | 490,220.00 USD | 166,310.00 USD | 238,840.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 1,920,000.00 USD | 1,920,000.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3436` | 725,790.00 USD | 725,790.00 USD | 0.00 USD | 141,640.00 USD | 93,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 770,860.00 USD | 770,860.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 2,030,000.00 USD | 2,030,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3446` | 952,130.00 USD | 952,130.00 USD | 0.00 USD | 75,030.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 1,420,000.00 USD | 1,420,000.00 USD | 154,220.00 USD | 63,000.00 USD | 254,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 2,320,000.00 USD | 2,320,000.00 USD | 62,830.00 USD | 28,550.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3456` | 1,970,000.00 USD | 1,970,000.00 USD | 231,820.00 USD | 37,860.00 USD | 281,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 2,740,000.00 USD | 2,740,000.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 3,010,000.00 USD | 3,010,000.00 USD | 263,140.00 USD | 240,590.00 USD | 528,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 3,490,000.00 USD | 3,490,000.00 USD | 251,240.00 USD | 290,920.00 USD | 205,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3466` | 3,380,000.00 USD | 3,380,000.00 USD | 135,220.00 USD | 83,230.00 USD | 156,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 3,820,000.00 USD | 3,820,000.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 3,570,000.00 USD | 3,570,000.00 USD | 81,330.00 USD | 45,970.00 USD | 61,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3476` | 3,770,000.00 USD | 3,770,000.00 USD | 86,450.00 USD | 64,310.00 USD | 45,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 4,010,000.00 USD | 4,010,000.00 USD | 73,970.00 USD | 38,390.00 USD | 128,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 32,530.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3486` | 4,160,000.00 USD | 4,160,000.00 USD | 10,620.00 USD | 62,880.00 USD | 76,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 3,970,000.00 USD | 3,970,000.00 USD | 19,250.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3491` | 4,290,000.00 USD | 4,290,000.00 USD | 42,120.00 USD | 28,080.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 93,150.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3496` | 4,460,000.00 USD | 4,460,000.00 USD | 34,020.00 USD | 13,050.00 USD | 121,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 4,390,000.00 USD | 4,390,000.00 USD | 133,330.00 USD | 0.00 USD | 139,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3501` | 4,950,000.00 USD | 4,950,000.00 USD | 52,670.00 USD | 9,040.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 4,420,000.00 USD | 4,420,000.00 USD | 6,140.00 USD | 19,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3506` | 5,080,000.00 USD | 5,080,000.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 5,140,000.00 USD | 5,140,000.00 USD | 2,790.00 USD | 16,810.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 5,380,000.00 USD | 5,380,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 592.63 USD | 782.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3516` | 5,330,000.00 USD | 5,330,000.00 USD | 52,740.00 USD | 5,720.00 USD | 135,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3517` | 5,380,000.00 USD | 5,380,000.00 USD | 6,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 5,480,000.00 USD | 5,480,000.00 USD | 47,300.00 USD | 21,980.00 USD | 78,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 5,900,000.00 USD | 5,900,000.00 USD | 277,410.00 USD | 28,950.00 USD | 205,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3526` | 5,540,000.00 USD | 5,540,000.00 USD | 14,390.00 USD | 17,990.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3529` | 6,030,000.00 USD | 6,030,000.00 USD | 137,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 5,890,000.00 USD | 5,890,000.00 USD | 139,090.00 USD | 98,020.00 USD | 108,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 6,330,000.00 USD | 6,330,000.00 USD | 5,810.00 USD | 98,000.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3536` | 6,290,000.00 USD | 6,290,000.00 USD | 194,810.00 USD | 16,340.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3541` | 6,490,000.00 USD | 6,490,000.00 USD | 101,070.00 USD | 96,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 7,250,000.00 USD | 7,250,000.00 USD | 808,620.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3546` | 6,630,000.00 USD | 6,630,000.00 USD | 8,680.00 USD | 60,460.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 7,560,000.00 USD | 7,560,000.00 USD | 15,040.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3551` | 6,740,000.00 USD | 6,740,000.00 USD | 16,020.00 USD | 46,910.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3556` | 6,840,000.00 USD | 6,840,000.00 USD | 23,440.00 USD | 73,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 7,680,000.00 USD | 7,680,000.00 USD | 9,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3561` | 6,970,000.00 USD | 6,970,000.00 USD | 859.20 USD | 25,000.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 7,730,000.00 USD | 7,730,000.00 USD | 4,730.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3566` | 7,030,000.00 USD | 7,030,000.00 USD | 5,680.00 USD | 11,630.00 USD | 39,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 7,040,000.00 USD | 7,040,000.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 7,730,000.00 USD | 7,730,000.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3576` | 7,220,000.00 USD | 7,220,000.00 USD | 161,860.00 USD | 18,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 7,860,000.00 USD | 7,860,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3581` | 7,260,000.00 USD | 7,260,000.00 USD | 3,860.00 USD | 0.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 8,000,000.00 USD | 8,000,000.00 USD | 4,040.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3585` | 433.78 USD | 1,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3586` | 7,290,000.00 USD | 7,290,000.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 8,380,000.00 USD | 8,380,000.00 USD | 10,970.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3591` | 7,360,000.00 USD | 7,360,000.00 USD | 22,510.00 USD | 15,750.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3596` | 7,620,000.00 USD | 7,620,000.00 USD | 139,210.00 USD | 12,460.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 7,820,000.00 USD | 7,820,000.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 9,030,000.00 USD | 9,030,000.00 USD | 7,660.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3605` | 282.63 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3606` | 8,110,000.00 USD | 8,110,000.00 USD | 62,630.00 USD | 32,860.00 USD | 195,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 9,430,000.00 USD | 9,430,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3611` | 8,440,000.00 USD | 8,440,000.00 USD | 86,800.00 USD | 60,060.00 USD | 190,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 10,120,000.00 USD | 10,120,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3616` | 8,860,000.00 USD | 8,860,000.00 USD | 228,030.00 USD | 38,210.00 USD | 150,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 10,330,000.00 USD | 10,330,000.00 USD | 3,550.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 9,190,000.00 USD | 9,190,000.00 USD | 144,510.00 USD | 113,560.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3626` | 9,340,000.00 USD | 9,340,000.00 USD | 100,410.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 10,800,000.00 USD | 10,800,000.00 USD | 1,260,000.00 USD | 102,260.00 USD | 93,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 12,360.00 USD | 13,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3636` | 11,220,000.00 USD | 11,220,000.00 USD | 183,690.00 USD | 48,500.00 USD | 185,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 11,610,000.00 USD | 11,610,000.00 USD | 85,150.00 USD | 229,250.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 11,450,000.00 USD | 11,450,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3646` | 12,040,000.00 USD | 12,040,000.00 USD | 351,270.00 USD | 21,220.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 11,630,000.00 USD | 11,630,000.00 USD | 180,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3651` | 12,320,000.00 USD | 12,320,000.00 USD | 2,860.00 USD | 67,160.00 USD | 207,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 12,430,000.00 USD | 12,430,000.00 USD | 681,380.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3656` | 13,260,000.00 USD | 13,260,000.00 USD | 519,740.00 USD | 133,520.00 USD | 290,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 13,750,000.00 USD | 13,750,000.00 USD | 277,650.00 USD | 111,580.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 13,420,000.00 USD | 13,420,000.00 USD | 685,520.00 USD | 66,940.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,010.00 USD | 16,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3666` | 14,420,000.00 USD | 14,420,000.00 USD | 484,790.00 USD | 124,300.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 14,040,000.00 USD | 14,040,000.00 USD | 419,350.00 USD | 34,510.00 USD | 166,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3671` | 15,030,000.00 USD | 15,030,000.00 USD | 94,630.00 USD | 93,830.00 USD | 412,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 14,730,000.00 USD | 14,730,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3676` | 15,370,000.00 USD | 15,370,000.00 USD | 76,720.00 USD | 53,460.00 USD | 218,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 14,980,000.00 USD | 14,980,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3681` | 16,350,000.00 USD | 16,350,000.00 USD | 769,010.00 USD | 104,570.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 15,160,000.00 USD | 15,160,000.00 USD | 2,020.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3686` | 16,980,000.00 USD | 16,980,000.00 USD | 327,450.00 USD | 157,020.00 USD | 145,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3691` | 17,530,000.00 USD | 17,530,000.00 USD | 475,810.00 USD | 51,700.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 15,570,000.00 USD | 15,570,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3696` | 17,800,000.00 USD | 17,800,000.00 USD | 163,960.00 USD | 88,200.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 15,810,000.00 USD | 15,810,000.00 USD | 4,850.00 USD | 175,510.00 USD | 55,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3701` | 18,550,000.00 USD | 18,550,000.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 15,860,000.00 USD | 15,860,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 17,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3706` | 19,380,000.00 USD | 19,380,000.00 USD | 249,050.00 USD | 8,320.00 USD | 573,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 15,860,000.00 USD | 15,860,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3711` | 20,260,000.00 USD | 20,260,000.00 USD | 549,150.00 USD | 105,970.00 USD | 225,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 16,260,000.00 USD | 16,260,000.00 USD | 3,410.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3716` | 21,390,000.00 USD | 21,390,000.00 USD | 76,250.00 USD | 229,370.00 USD | 817,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 21,590,000.00 USD | 21,590,000.00 USD | 20,850.00 USD | 62,750.00 USD | 116,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 786,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 26,260.00 USD | 43,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3726` | 22,720,000.00 USD | 22,720,000.00 USD | 512,200.00 USD | 31,730.00 USD | 587,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 17,320,000.00 USD | 17,320,000.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3731` | 23,900,000.00 USD | 23,900,000.00 USD | 72,270.00 USD | 152,050.00 USD | 954,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 17,510,000.00 USD | 17,510,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 1,870,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3736` | 24,120,000.00 USD | 24,120,000.00 USD | 224,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 17,990,000.00 USD | 17,990,000.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3741` | 24,760,000.00 USD | 24,760,000.00 USD | 68,340.00 USD | 166,120.00 USD | 403,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 18,390,000.00 USD | 18,390,000.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3746` | 25,190,000.00 USD | 25,190,000.00 USD | 37,630.00 USD | 50,320.00 USD | 341,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3751` | 26,060,000.00 USD | 26,060,000.00 USD | 363,100.00 USD | 6,290.00 USD | 497,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3756` | 26,350,000.00 USD | 26,350,000.00 USD | 23,190.00 USD | 1,940.00 USD | 265,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 18,690,000.00 USD | 18,690,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3761` | 27,580,000.00 USD | 27,580,000.00 USD | 303,200.00 USD | 77,030.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 18,870,000.00 USD | 18,870,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3766` | 27,630,000.00 USD | 27,630,000.00 USD | 21,660.00 USD | 24,840.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 18,870,000.00 USD | 18,870,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3771` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 32,810.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3776` | 27,760,000.00 USD | 27,760,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3780` | 27,770,000.00 USD | 27,770,000.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 18,890,000.00 USD | 18,890,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 19,040,000.00 USD | 19,040,000.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 19,510,000.00 USD | 19,510,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 773.04 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3805` | 19,510,000.00 USD | 19,510,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3805` | 2,320.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3811` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 19,720,000.00 USD | 19,720,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3825` | 114.75 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3841` | 19,840,000.00 USD | 19,840,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 264.84 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3859` | 19,910,000.00 USD | 19,910,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 20,070,000.00 USD | 20,070,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 20,190,000.00 USD | 20,190,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 20,340,000.00 USD | 20,340,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 20,440,000.00 USD | 20,440,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3919` | 20,560,000.00 USD | 20,560,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 20,720,000.00 USD | 20,720,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 20,750,000.00 USD | 20,750,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 20,780,000.00 USD | 20,780,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 20,810,000.00 USD | 20,810,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 20,940,000.00 USD | 20,940,000.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 21,170,000.00 USD | 21,170,000.00 USD | 107,420.00 USD | 8,610.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 21,350,000.00 USD | 21,350,000.00 USD | 123,320.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 21,380,000.00 USD | 21,380,000.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 21,520,000.00 USD | 21,520,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 21,630,000.00 USD | 21,630,000.00 USD | 57,460.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 21,660,000.00 USD | 21,660,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3985` | 145,580.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3991` | 21,700,000.00 USD | 21,700,000.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3997` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 27,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4015` | 327.62 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4065` | 128.86 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4145` | 13,090.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 998.96 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 3,930.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4265` | 322.01 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4305` | 1,490.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 72,540.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 5,780.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 8,970.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4495` | 259.81 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4625` | 20,210.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4805` | 4,710.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 23,320.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 667.22 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5435` | 2,260.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5475` | 40,520.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 140.12 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5745` | 745,270.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 24,580.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 6,810.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6395` | 168.19 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6505` | 102,710.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 395.37 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6625` | 2,520.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 1,210.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6765` | 83,430.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0865` | 1,230,000.00 USD | 0.00 USD | 179.83 USD | `-74.77%` | `2,079.00` |
| `Live` | `Long` | `0.0885` | 1,230,000.00 USD | 0.00 USD | 878.45 USD | `-74.19%` | `9,926.00` |
| `Live` | `Long` | `0.0905` | 1,230,000.00 USD | 0.00 USD | 7,990.00 USD | `-73.60%` | `88,233.00` |
| `Live` | `Long` | `0.1005` | 1,220,000.00 USD | 0.00 USD | 143.51 USD | `-70.69%` | `1,428.00` |
| `Live` | `Long` | `0.1075` | 1,220,000.00 USD | 0.00 USD | 27,380.00 USD | `-68.64%` | `254,687.00` |
| `Live` | `Long` | `0.1145` | 1,190,000.00 USD | 0.00 USD | 2,290.00 USD | `-66.60%` | `20,000.00` |
| `Live` | `Long` | `0.1155` | 1,190,000.00 USD | 0.00 USD | 265.88 USD | `-66.31%` | `2,302.00` |
| `Live` | `Long` | `0.1165` | 1,190,000.00 USD | 0.00 USD | 123.26 USD | `-66.02%` | `1,058.00` |
| `Live` | `Long` | `0.1395` | 1,190,000.00 USD | 0.00 USD | 11,500.00 USD | `-59.31%` | `82,417.00` |
| `Live` | `Long` | `0.1585` | 1,180,000.00 USD | 0.00 USD | 863.51 USD | `-53.77%` | `5,448.00` |
| `Live` | `Long` | `0.1615` | 1,180,000.00 USD | 0.00 USD | 35,330.00 USD | `-52.89%` | `218,745.00` |
| `Live` | `Long` | `0.1645` | 1,140,000.00 USD | 0.00 USD | 6,760.00 USD | `-52.02%` | `41,100.00` |
| `Live` | `Long` | `0.1685` | 1,130,000.00 USD | 0.00 USD | 23,490.00 USD | `-50.85%` | `139,400.00` |
| `Live` | `Long` | `0.1715` | 1,110,000.00 USD | 0.00 USD | 648.96 USD | `-49.98%` | `3,784.00` |
| `Live` | `Long` | `0.1725` | 1,110,000.00 USD | 0.00 USD | 10,440.00 USD | `-49.68%` | `60,538.00` |
| `Live` | `Long` | `0.1735` | 1,100,000.00 USD | 0.00 USD | 2,520.00 USD | `-49.39%` | `14,529.00` |
| `Live` | `Long` | `0.1745` | 1,100,000.00 USD | 0.00 USD | 4,150.00 USD | `-49.10%` | `23,777.00` |
| `Live` | `Long` | `0.1755` | 1,090,000.00 USD | 0.00 USD | 255.53 USD | `-48.81%` | `1,456.00` |
| `Live` | `Long` | `0.1765` | 1,090,000.00 USD | 0.00 USD | 174.38 USD | `-48.52%` | `988.00` |
| `Live` | `Long` | `0.1775` | 1,090,000.00 USD | 0.00 USD | 207.50 USD | `-48.23%` | `1,169.00` |
| `Live` | `Long` | `0.1815` | 1,090,000.00 USD | 0.00 USD | 100.37 USD | `-47.06%` | `553.00` |
| `Live` | `Long` | `0.1875` | 1,090,000.00 USD | 0.00 USD | 36,310.00 USD | `-45.31%` | `193,636.00` |
| `Live` | `Long` | `0.1965` | 1,060,000.00 USD | 0.00 USD | 628.80 USD | `-42.68%` | `3,200.00` |
| `Live` | `Long` | `0.2025` | 1,060,000.00 USD | 0.00 USD | 1,200.00 USD | `-40.93%` | `5,912.00` |
| `Live` | `Long` | `0.2105` | 1,050,000.00 USD | 0.00 USD | 14,200.00 USD | `-38.60%` | `67,468.00` |
| `Live` | `Long` | `0.2135` | 1,040,000.00 USD | 0.00 USD | 223.11 USD | `-37.73%` | `1,045.00` |
| `Live` | `Long` | `0.2165` | 1,040,000.00 USD | 0.00 USD | 1,520.00 USD | `-36.85%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,040,000.00 USD | 0.00 USD | 710.34 USD | `-36.27%` | `3,251.00` |
| `Live` | `Long` | `0.2205` | 1,040,000.00 USD | 0.00 USD | 493.04 USD | `-35.68%` | `2,236.00` |
| `Live` | `Long` | `0.2245` | 1,040,000.00 USD | 0.00 USD | 4,570.00 USD | `-34.52%` | `20,360.00` |
| `Live` | `Long` | `0.2275` | 1,030,000.00 USD | 0.00 USD | 156.06 USD | `-33.64%` | `686.00` |
| `Live` | `Long` | `0.2295` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-33.06%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-32.77%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,030,000.00 USD | 0.00 USD | 2,420.00 USD | `-32.18%` | `10,412.00` |
| `Live` | `Long` | `0.2335` | 1,030,000.00 USD | 0.00 USD | 807.21 USD | `-31.89%` | `3,457.00` |
| `Live` | `Long` | `0.2345` | 1,030,000.00 USD | 0.00 USD | 5,700.00 USD | `-31.60%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 3,130.00 USD | `-31.31%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 1,020,000.00 USD | 0.00 USD | 686.56 USD | `-31.02%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 1,020,000.00 USD | 0.00 USD | 568.81 USD | `-30.73%` | `2,395.00` |
| `Live` | `Long` | `0.2385` | 1,020,000.00 USD | 0.00 USD | 3,100.00 USD | `-30.43%` | `12,978.00` |
| `Live` | `Long` | `0.2395` | 1,010,000.00 USD | 0.00 USD | 151.36 USD | `-30.14%` | `632.00` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 885.85 USD | `-28.98%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 1,010,000.00 USD | 0.00 USD | 464.79 USD | `-28.68%` | `1,901.00` |
| `Live` | `Long` | `0.2455` | 1,010,000.00 USD | 0.00 USD | 384.94 USD | `-28.39%` | `1,568.00` |
| `Live` | `Long` | `0.2475` | 1,010,000.00 USD | 0.00 USD | 11,840.00 USD | `-27.81%` | `47,833.00` |
| `Live` | `Long` | `0.2495` | 1,000,000.00 USD | 0.00 USD | 292.41 USD | `-27.23%` | `1,172.00` |
| `Live` | `Long` | `0.2505` | 1,000,000.00 USD | 0.00 USD | 262.02 USD | `-26.93%` | `1,046.00` |
| `Live` | `Long` | `0.2595` | 999,820.00 USD | 0.00 USD | 749.18 USD | `-24.31%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 999,070.00 USD | 0.00 USD | 107.74 USD | `-23.73%` | `412.00` |
| `Live` | `Long` | `0.2635` | 998,970.00 USD | 0.00 USD | 4,550.00 USD | `-23.14%` | `17,283.00` |
| `Live` | `Long` | `0.2645` | 994,410.00 USD | 0.00 USD | 2,650.00 USD | `-22.85%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 991,760.00 USD | 0.00 USD | 193.02 USD | `-22.56%` | `727.00` |
| `Live` | `Long` | `0.2665` | 991,570.00 USD | 0.00 USD | 241.18 USD | `-22.27%` | `905.00` |
| `Live` | `Long` | `0.2675` | 991,320.00 USD | 0.00 USD | 321.54 USD | `-21.98%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 991,000.00 USD | 0.00 USD | 3,150.00 USD | `-21.68%` | `11,746.00` |
| `Live` | `Long` | `0.2735` | 987,850.00 USD | 0.00 USD | 4,160.00 USD | `-20.23%` | `15,203.00` |
| `Live` | `Long` | `0.2745` | 983,690.00 USD | 0.00 USD | 80,520.00 USD | `-19.93%` | `293,333.00` |
| `Live` | `Long` | `0.2785` | 903,170.00 USD | 0.00 USD | 15,180.00 USD | `-18.77%` | `54,497.00` |
| `Live` | `Long` | `0.2795` | 887,990.00 USD | 0.00 USD | 6,260.00 USD | `-18.48%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 881,740.00 USD | 0.00 USD | 13,300.00 USD | `-18.18%` | `47,408.00` |
| `Live` | `Long` | `0.2815` | 868,440.00 USD | 0.00 USD | 3,690.00 USD | `-17.89%` | `13,109.00` |
| `Live` | `Long` | `0.2825` | 864,750.00 USD | 0.00 USD | 838.74 USD | `-17.60%` | `2,969.00` |
| `Live` | `Long` | `0.2845` | 863,910.00 USD | 0.00 USD | 6,250.00 USD | `-17.02%` | `21,954.00` |
| `Live` | `Long` | `0.2855` | 857,670.00 USD | 0.00 USD | 552.44 USD | `-16.73%` | `1,935.00` |
| `Live` | `Long` | `0.2865` | 857,110.00 USD | 0.00 USD | 4,150.00 USD | `-16.43%` | `14,481.00` |
| `Live` | `Long` | `0.2895` | 852,960.00 USD | 0.00 USD | 297.90 USD | `-15.56%` | `1,029.00` |
| `Live` | `Long` | `0.2905` | 852,670.00 USD | 0.00 USD | 522.90 USD | `-15.27%` | `1,800.00` |
| `Live` | `Long` | `0.2915` | 852,140.00 USD | 0.00 USD | 954.37 USD | `-14.97%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 851,190.00 USD | 0.00 USD | 213.08 USD | `-14.39%` | `726.00` |
| `Live` | `Long` | `0.2945` | 850,980.00 USD | 0.00 USD | 124.87 USD | `-14.10%` | `424.00` |
| `Live` | `Long` | `0.2955` | 850,850.00 USD | 0.00 USD | 156.61 USD | `-13.81%` | `530.00` |
| `Live` | `Long` | `0.2965` | 850,690.00 USD | 0.00 USD | 1,010.00 USD | `-13.52%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 849,690.00 USD | 0.00 USD | 759.68 USD | `-12.93%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 848,930.00 USD | 0.00 USD | 197.37 USD | `-12.64%` | `659.00` |
| `Live` | `Long` | `0.3005` | 848,730.00 USD | 0.00 USD | 10,620.00 USD | `-12.35%` | `35,336.00` |
| `Live` | `Long` | `0.3015` | 838,110.00 USD | 0.00 USD | 102.81 USD | `-12.06%` | `341.00` |
| `Live` | `Long` | `0.3025` | 838,010.00 USD | 0.00 USD | 2,510.00 USD | `-11.77%` | `8,314.00` |
| `Live` | `Long` | `0.3035` | 835,490.00 USD | 0.00 USD | 4,040.00 USD | `-11.47%` | `13,300.00` |
| `Live` | `Long` | `0.3045` | 831,460.00 USD | 0.00 USD | 138.24 USD | `-11.18%` | `454.00` |
| `Live` | `Long` | `0.3055` | 831,320.00 USD | 0.00 USD | 14,670.00 USD | `-10.89%` | `48,026.00` |
| `Live` | `Long` | `0.3065` | 816,650.00 USD | 0.00 USD | 5,900.00 USD | `-10.60%` | `19,262.00` |
| `Live` | `Long` | `0.3075` | 810,740.00 USD | 0.00 USD | 722.62 USD | `-10.31%` | `2,350.00` |
| `Live` | `Long` | `0.3085` | 810,020.00 USD | 0.00 USD | 291.53 USD | `-10.02%` | `945.00` |
| `Live` | `Long` | `0.3095` | 809,730.00 USD | 0.00 USD | 192.51 USD | `-9.72%` | `622.00` |
| `Live` | `Long` | `0.3105` | 809,540.00 USD | 0.00 USD | 14,140.00 USD | `-9.43%` | `45,526.00` |
| `Live` | `Long` | `0.3115` | 795,400.00 USD | 0.00 USD | 245.77 USD | `-9.14%` | `789.00` |
| `Live` | `Long` | `0.3125` | 795,150.00 USD | 0.00 USD | 18,110.00 USD | `-8.85%` | `57,949.00` |
| `Live` | `Long` | `0.3135` | 777,050.00 USD | 0.00 USD | 141.39 USD | `-8.56%` | `451.00` |
| `Live` | `Long` | `0.3145` | 776,900.00 USD | 0.00 USD | 1,490.00 USD | `-8.27%` | `4,723.00` |
| `Live` | `Long` | `0.3155` | 775,420.00 USD | 0.00 USD | 1,150.00 USD | `-7.97%` | `3,657.00` |
| `Live` | `Long` | `0.3175` | 774,270.00 USD | 0.00 USD | 3,440.00 USD | `-7.39%` | `10,836.00` |
| `Live` | `Long` | `0.3185` | 770,820.00 USD | 0.00 USD | 17,020.00 USD | `-7.10%` | `53,426.00` |
| `Live` | `Long` | `0.3195` | 753,810.00 USD | 0.00 USD | 285.31 USD | `-6.81%` | `893.00` |
| `Live` | `Long` | `0.3205` | 753,520.00 USD | 0.00 USD | 455.75 USD | `-6.52%` | `1,422.00` |
| `Live` | `Long` | `0.3215` | 753,070.00 USD | 0.00 USD | 127.64 USD | `-6.22%` | `397.00` |
| `Live` | `Long` | `0.3225` | 752,940.00 USD | 0.00 USD | 3,930.00 USD | `-5.93%` | `12,194.00` |
| `Live` | `Long` | `0.3255` | 749,010.00 USD | 0.00 USD | 3,580.00 USD | `-5.06%` | `11,000.00` |
| `Live` | `Short` | `0.3265` | 190.35 USD | 190.35 USD | 0.00 USD | `-4.77%` | `583.00` |
| `Live` | `Long` | `0.3275` | 745,430.00 USD | 0.00 USD | 163.42 USD | `-4.47%` | `499.00` |
| `Live` | `Long` | `0.3285` | 745,260.00 USD | 0.00 USD | 745,260.00 USD | `-4.18%` | `2,268,686.00` |
| `Live` | `Short` | `0.3515` | 782.98 USD | 592.63 USD | 0.00 USD | `+2.53%` | `1,686.00` |
| `Live` | `Short` | `0.3585` | 1,220.00 USD | 433.78 USD | 0.00 USD | `+4.57%` | `1,210.00` |
| `Live` | `Short` | `0.3605` | 1,500.00 USD | 282.63 USD | 0.00 USD | `+5.15%` | `784.00` |
| `Live` | `Short` | `0.3635` | 13,860.00 USD | 12,360.00 USD | 0.00 USD | `+6.03%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 16,870.00 USD | 3,010.00 USD | 0.00 USD | `+6.90%` | `8,215.00` |
| `Live` | `Short` | `0.3705` | 17,150.00 USD | 278.99 USD | 0.00 USD | `+8.07%` | `753.00` |
| `Live` | `Short` | `0.3725` | 43,410.00 USD | 26,260.00 USD | 0.00 USD | `+8.65%` | `70,500.00` |
| `Live` | `Short` | `0.3735` | 1,920,000.00 USD | 1,870,000.00 USD | 0.00 USD | `+8.94%` | `5,018,211.00` |
| `Live` | `Short` | `0.3755` | 1,920,000.00 USD | 4,030.00 USD | 0.00 USD | `+9.53%` | `10,732.00` |
| `Live` | `Short` | `0.3775` | 1,920,000.00 USD | 104.19 USD | 0.00 USD | `+10.11%` | `276.00` |
| `Live` | `Short` | `0.3785` | 2,480,000.00 USD | 556,430.00 USD | 0.00 USD | `+10.40%` | `1,470,083.00` |
| `Live` | `Short` | `0.3795` | 2,480,000.00 USD | 773.04 USD | 0.00 USD | `+10.69%` | `2,037.00` |
| `Live` | `Short` | `0.3805` | 2,480,000.00 USD | 2,320.00 USD | 0.00 USD | `+10.98%` | `6,090.00` |
| `Live` | `Short` | `0.3825` | 2,480,000.00 USD | 114.75 USD | 0.00 USD | `+11.57%` | `300.00` |
| `Live` | `Short` | `0.3855` | 2,480,000.00 USD | 264.84 USD | 0.00 USD | `+12.44%` | `687.00` |
| `Live` | `Short` | `0.3895` | 2,490,000.00 USD | 4,760.00 USD | 0.00 USD | `+13.61%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 2,490,000.00 USD | 6,000.00 USD | 0.00 USD | `+13.90%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 2,490,000.00 USD | 1,480.00 USD | 0.00 USD | `+14.78%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 2,610,000.00 USD | 118,130.00 USD | 0.00 USD | `+15.07%` | `299,436.00` |
| `Live` | `Short` | `0.3985` | 2,760,000.00 USD | 145,580.00 USD | 0.00 USD | `+16.23%` | `365,311.00` |
| `Live` | `Short` | `0.4015` | 2,760,000.00 USD | 327.62 USD | 0.00 USD | `+17.11%` | `816.00` |
| `Live` | `Short` | `0.4065` | 2,760,000.00 USD | 128.86 USD | 0.00 USD | `+18.57%` | `317.00` |
| `Live` | `Short` | `0.4085` | 2,760,000.00 USD | 170.75 USD | 0.00 USD | `+19.15%` | `418.00` |
| `Live` | `Short` | `0.4095` | 2,760,000.00 USD | 239.56 USD | 0.00 USD | `+19.44%` | `585.00` |
| `Live` | `Short` | `0.4145` | 2,770,000.00 USD | 13,090.00 USD | 0.00 USD | `+20.90%` | `31,569.00` |
| `Live` | `Short` | `0.4185` | 2,770,000.00 USD | 998.96 USD | 0.00 USD | `+22.07%` | `2,387.00` |
| `Live` | `Short` | `0.4245` | 2,780,000.00 USD | 3,930.00 USD | 0.00 USD | `+23.82%` | `9,259.00` |
| `Live` | `Short` | `0.4265` | 2,780,000.00 USD | 322.01 USD | 0.00 USD | `+24.40%` | `755.00` |
| `Live` | `Short` | `0.4305` | 2,780,000.00 USD | 1,490.00 USD | 0.00 USD | `+25.57%` | `3,464.00` |
| `Live` | `Short` | `0.4365` | 2,850,000.00 USD | 72,540.00 USD | 0.00 USD | `+27.32%` | `166,191.00` |
| `Live` | `Short` | `0.4415` | 2,850,000.00 USD | 377.48 USD | 0.00 USD | `+28.78%` | `855.00` |
| `Live` | `Short` | `0.4425` | 2,860,000.00 USD | 5,780.00 USD | 0.00 USD | `+29.07%` | `13,056.00` |
| `Live` | `Short` | `0.4455` | 2,870,000.00 USD | 8,970.00 USD | 0.00 USD | `+29.94%` | `20,134.00` |
| `Live` | `Short` | `0.4475` | 2,930,000.00 USD | 65,610.00 USD | 0.00 USD | `+30.53%` | `146,614.00` |
| `Live` | `Short` | `0.4495` | 2,930,000.00 USD | 259.81 USD | 0.00 USD | `+31.11%` | `578.00` |
| `Live` | `Short` | `0.4625` | 2,950,000.00 USD | 20,210.00 USD | 0.00 USD | `+34.90%` | `43,700.00` |
| `Live` | `Short` | `0.4805` | 2,960,000.00 USD | 4,710.00 USD | 0.00 USD | `+40.15%` | `9,800.00` |
| `Live` | `Short` | `0.4895` | 2,960,000.00 USD | 839.49 USD | 0.00 USD | `+42.78%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,960,000.00 USD | 5,120.00 USD | 0.00 USD | `+43.07%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,970,000.00 USD | 2,730.00 USD | 0.00 USD | `+45.69%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,990,000.00 USD | 23,320.00 USD | 0.00 USD | `+45.99%` | `46,591.00` |
| `Live` | `Short` | `0.5325` | 2,990,000.00 USD | 667.22 USD | 0.00 USD | `+55.32%` | `1,253.00` |
| `Live` | `Short` | `0.5435` | 2,990,000.00 USD | 2,260.00 USD | 0.00 USD | `+58.53%` | `4,154.00` |
| `Live` | `Short` | `0.5475` | 3,030,000.00 USD | 40,520.00 USD | 0.00 USD | `+59.70%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 3,030,000.00 USD | 740.92 USD | 0.00 USD | `+62.61%` | `1,329.00` |
| `Live` | `Short` | `0.5605` | 3,030,000.00 USD | 140.12 USD | 0.00 USD | `+63.49%` | `250.00` |
| `Live` | `Short` | `0.5745` | 3,780,000.00 USD | 745,270.00 USD | 0.00 USD | `+67.57%` | `1,297,248.00` |
| `Live` | `Short` | `0.6145` | 3,800,000.00 USD | 24,580.00 USD | 0.00 USD | `+79.24%` | `40,000.00` |
| `Live` | `Short` | `0.6335` | 3,810,000.00 USD | 6,810.00 USD | 0.00 USD | `+84.78%` | `10,756.00` |
| `Live` | `Short` | `0.6395` | 3,810,000.00 USD | 168.19 USD | 0.00 USD | `+86.53%` | `263.00` |
| `Live` | `Short` | `0.6505` | 3,910,000.00 USD | 102,710.00 USD | 0.00 USD | `+89.74%` | `157,888.00` |
| `Live` | `Short` | `0.6515` | 3,910,000.00 USD | 951.19 USD | 0.00 USD | `+90.03%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 3,910,000.00 USD | 395.37 USD | 0.00 USD | `+90.61%` | `605.00` |
| `Live` | `Short` | `0.6615` | 3,920,000.00 USD | 2,060.00 USD | 0.00 USD | `+92.95%` | `3,114.00` |
| `Live` | `Short` | `0.6625` | 3,920,000.00 USD | 2,520.00 USD | 0.00 USD | `+93.24%` | `3,811.00` |
| `Live` | `Short` | `0.6635` | 3,920,000.00 USD | 1,210.00 USD | 0.00 USD | `+93.53%` | `1,821.00` |
| `Live` | `Short` | `0.6765` | 4,000,000.00 USD | 83,430.00 USD | 0.00 USD | `+97.32%` | `123,332.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0925` | 825,650.00 USD | 0.00 USD | 407.56 USD | `-73.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 825,240.00 USD | 0.00 USD | 198.45 USD | `-72.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 825,040.00 USD | 0.00 USD | 330.26 USD | `-58.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 824,710.00 USD | 0.00 USD | 1,750.00 USD | `-40.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 822,960.00 USD | 0.00 USD | 579.72 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2155` | 822,380.00 USD | 0.00 USD | 2,040.00 USD | `-37.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2165` | 820,340.00 USD | 0.00 USD | 1,030.00 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 819,310.00 USD | 0.00 USD | 515.61 USD | `-35.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 818,800.00 USD | 0.00 USD | 121.70 USD | `-32.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 818,680.00 USD | 0.00 USD | 705.61 USD | `-31.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 817,970.00 USD | 0.00 USD | 159.20 USD | `-31.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 817,810.00 USD | 0.00 USD | 1,200.00 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 816,610.00 USD | 0.00 USD | 127.51 USD | `-29.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 816,480.00 USD | 0.00 USD | 1,850.00 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 814,630.00 USD | 0.00 USD | 41,500.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 773,130.00 USD | 0.00 USD | 1,920.00 USD | `-25.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 771,210.00 USD | 0.00 USD | 664.01 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 770,540.00 USD | 0.00 USD | 954.98 USD | `-23.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 769,590.00 USD | 0.00 USD | 103.56 USD | `-23.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2655` | 769,480.00 USD | 0.00 USD | 195.14 USD | `-22.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 769,290.00 USD | 0.00 USD | 695.50 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 768,590.00 USD | 0.00 USD | 1,630.00 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 766,970.00 USD | 0.00 USD | 1,470.00 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 765,490.00 USD | 0.00 USD | 101.94 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 765,390.00 USD | 0.00 USD | 3,260.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 762,130.00 USD | 0.00 USD | 2,550.00 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 759,580.00 USD | 0.00 USD | 229.92 USD | `-17.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 759,350.00 USD | 0.00 USD | 8,010.00 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 751,340.00 USD | 0.00 USD | 11,610.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 739,730.00 USD | 0.00 USD | 111.19 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 739,620.00 USD | 0.00 USD | 433.42 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 739,190.00 USD | 0.00 USD | 2,710.00 USD | `-12.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 736,480.00 USD | 0.00 USD | 503.95 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 735,980.00 USD | 0.00 USD | 1,400.00 USD | `-10.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 734,580.00 USD | 0.00 USD | 193.11 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 734,380.00 USD | 0.00 USD | 15,150.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 719,230.00 USD | 0.00 USD | 156.30 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 719,070.00 USD | 0.00 USD | 12,200.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 706,870.00 USD | 0.00 USD | 6,530.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 700,340.00 USD | 0.00 USD | 524,570.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 175,770.00 USD | 0.00 USD | 1,270.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 174,500.00 USD | 0.00 USD | 53,690.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 120,820.00 USD | 0.00 USD | 644.88 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 120,170.00 USD | 0.00 USD | 7,160.00 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 113,010.00 USD | 0.00 USD | 850.90 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 112,160.00 USD | 0.00 USD | 1,610.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 110,550.00 USD | 0.00 USD | 5,610.00 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 104,940.00 USD | 0.00 USD | 10,160.00 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 94,780.00 USD | 0.00 USD | 43,760.00 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 51,010.00 USD | 0.00 USD | 191.56 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 50,820.00 USD | 0.00 USD | 7,040.00 USD | `-5.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 43,780.00 USD | 0.00 USD | 3,970.00 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 39,810.00 USD | 0.00 USD | 2,040.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 37,770.00 USD | 0.00 USD | 6,130.00 USD | `-4.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 31,630.00 USD | 0.00 USD | 7,400.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 24,240.00 USD | 0.00 USD | 4,730.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 19,510.00 USD | 0.00 USD | 1,770.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 17,740.00 USD | 0.00 USD | 330.50 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 17,410.00 USD | 0.00 USD | 984.22 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 16,420.00 USD | 0.00 USD | 199.83 USD | `-3.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 16,220.00 USD | 0.00 USD | 4,880.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 11,350.00 USD | 0.00 USD | 229.47 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 11,120.00 USD | 0.00 USD | 4,040.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 7,070.00 USD | 0.00 USD | 265.50 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 6,810.00 USD | 0.00 USD | 2,020.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 4,790.00 USD | 0.00 USD | 1,450.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 3,340.00 USD | 0.00 USD | 960.45 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 2,380.00 USD | 0.00 USD | 1,460.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 917.85 USD | 0.00 USD | 486.30 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 431.55 USD | 0.00 USD | 431.55 USD | `-0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 828.18 USD | 828.18 USD | 0.00 USD | `+0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 1,880.00 USD | 1,050.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 2,100.00 USD | 225.27 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 2,330.00 USD | 225.57 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 2,740.00 USD | 412.83 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 2,980.00 USD | 239.07 USD | 0.00 USD | `+1.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 4,930.00 USD | 1,950.00 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 5,600.00 USD | 665.60 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 6,430.00 USD | 835.16 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 6,850.00 USD | 423.70 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 7,170.00 USD | 312.14 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 7,520.00 USD | 354.50 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 7,650.00 USD | 132.96 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 47,080.00 USD | 39,430.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 87,470.00 USD | 40,390.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 90,780.00 USD | 3,310.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 91,810.00 USD | 1,030.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 92,170.00 USD | 360.50 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 111,070.00 USD | 18,900.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 111,170.00 USD | 103.23 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 113,870.00 USD | 2,700.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 124,180.00 USD | 10,310.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 124,440.00 USD | 256.55 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 1,960,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 1,960,000.00 USD | 218.89 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 1,980,000.00 USD | 14,610.00 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 1,980,000.00 USD | 870.30 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 1,980,000.00 USD | 174.60 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 1,980,000.00 USD | 107.28 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 1,980,000.00 USD | 439.61 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 1,980,000.00 USD | 437.79 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 1,980,000.00 USD | 2,040.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 1,980,000.00 USD | 182.60 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 1,990,000.00 USD | 6,450.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 1,990,000.00 USD | 275.17 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 1,990,000.00 USD | 569.25 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 1,990,000.00 USD | 6,080.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 1,990,000.00 USD | 257.89 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 1,990,000.00 USD | 262.78 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 2,000,000.00 USD | 224.73 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 2,000,000.00 USD | 621.04 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 2,000,000.00 USD | 742.08 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 2,000,000.00 USD | 1,110.00 USD | 0.00 USD | `+13.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 2,000,000.00 USD | 181.04 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 2,000,000.00 USD | 490.38 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 2,000,000.00 USD | 138.63 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 2,000,000.00 USD | 276.40 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 2,000,000.00 USD | 126.24 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 2,000,000.00 USD | 2,400.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 2,000,000.00 USD | 647.13 USD | 0.00 USD | `+15.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 2,000,000.00 USD | 1,200.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 2,070,000.00 USD | 71,490.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 2,080,000.00 USD | 562.30 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 2,080,000.00 USD | 3,920.00 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 2,160,000.00 USD | 79,330.00 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 2,160,000.00 USD | 1,200.00 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 2,160,000.00 USD | 1,200.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 2,160,000.00 USD | 138.07 USD | 0.00 USD | `+19.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 2,160,000.00 USD | 1,270.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 2,160,000.00 USD | 331.63 USD | 0.00 USD | `+20.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 2,160,000.00 USD | 313.54 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 2,160,000.00 USD | 186.70 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 2,160,000.00 USD | 325.75 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 2,160,000.00 USD | 183.82 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 2,160,000.00 USD | 299.19 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 2,200,000.00 USD | 38,580.00 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 2,200,000.00 USD | 170.69 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 2,200,000.00 USD | 135.59 USD | 0.00 USD | `+30.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 2,200,000.00 USD | 1,520.00 USD | 0.00 USD | `+31.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 2,200,000.00 USD | 320.31 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 2,210,000.00 USD | 5,340.00 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 2,210,000.00 USD | 1,470.00 USD | 0.00 USD | `+34.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 2,290,000.00 USD | 80,770.00 USD | 0.00 USD | `+42.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 2,290,000.00 USD | 169.22 USD | 0.00 USD | `+43.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 2,290,000.00 USD | 153.79 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 2,290,000.00 USD | 724.89 USD | 0.00 USD | `+44.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 2,300,000.00 USD | 11,150.00 USD | 0.00 USD | `+45.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 2,310,000.00 USD | 1,930.00 USD | 0.00 USD | `+47.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5175` | 2,310,000.00 USD | 2,280.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 2,310,000.00 USD | 135.02 USD | 0.00 USD | `+54.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6255` | 2,310,000.00 USD | 1,160.00 USD | 0.00 USD | `+82.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 2,310,000.00 USD | 240.85 USD | 0.00 USD | `+83.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 2,310,000.00 USD | 1,100.00 USD | 0.00 USD | `+84.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 2,310,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 2,330,000.00 USD | 13,610.00 USD | 0.00 USD | `+97.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6775` | 2,330,000.00 USD | 1,060.00 USD | 0.00 USD | `+97.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 2,330,000.00 USD | 1,840.00 USD | 0.00 USD | `+98.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 2,330,000.00 USD | 991.76 USD | 0.00 USD | `+99.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 2,330,000.00 USD | 1,130.00 USD | 0.00 USD | `+99.95%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2953` | 23,430,000.00 USD | 0.00 USD | 23,430,000.00 USD | 82,070.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 23,340,000.00 USD | 0.00 USD | 23,340,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 23,200,000.00 USD | 0.00 USD | 23,200,000.00 USD | 122,540.00 USD | 36,820.00 USD | 59,640.00 USD |
| `7D` | `0.2971` | 22,980,000.00 USD | 0.00 USD | 22,980,000.00 USD | 89,290.00 USD | 34,680.00 USD | 52,660.00 USD |
| `7D` | `0.2977` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 54,000.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2981` | 17,570,000.00 USD | 0.00 USD | 17,570,000.00 USD | 25,600.00 USD | 3,620.00 USD | 0.00 USD |
| `7D` | `0.2983` | 22,710,000.00 USD | 0.00 USD | 22,710,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2986` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 111,780.00 USD | 10,860.00 USD | 11,740.00 USD |
| `7D` | `0.2989` | 22,490,000.00 USD | 0.00 USD | 22,490,000.00 USD | 117,420.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2991` | 17,400,000.00 USD | 0.00 USD | 17,400,000.00 USD | 57,070.00 USD | 0.00 USD | 8,790.00 USD |
| `7D` | `0.2995` | 22,330,000.00 USD | 0.00 USD | 22,330,000.00 USD | 6,450.00 USD | 69,130.00 USD | 80,320.00 USD |
| `1D` | `0.2996` | 17,340,000.00 USD | 0.00 USD | 17,340,000.00 USD | 13,470.00 USD | 62,620.00 USD | 85,870.00 USD |
| `1D` | `0.3001` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 8,760.00 USD | 14,600.00 USD | 31,550.00 USD |
| `7D` | `0.3001` | 22,170,000.00 USD | 0.00 USD | 22,170,000.00 USD | 0.00 USD | 34,510.00 USD | 93,100.00 USD |
| `1D` | `0.3006` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 16,450.00 USD | 7,870.00 USD | 34,530.00 USD |
| `7D` | `0.3007` | 22,050,000.00 USD | 0.00 USD | 22,050,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3011` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 51,610.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.3013` | 22,010,000.00 USD | 0.00 USD | 22,010,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3016` | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 1,010.00 USD | 9,650.00 USD | 18,990.00 USD |
| `7D` | `0.3019` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3021` | 16,970,000.00 USD | 0.00 USD | 16,970,000.00 USD | 14,850.00 USD | 6,560.00 USD | 16,590.00 USD |
| `7D` | `0.3025` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 4,850.00 USD | 22,200.00 USD | 55,840.00 USD |
| `1D` | `0.3026` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 2,880.00 USD | 2,050.00 USD | 17,010.00 USD |
| `1D` | `0.3031` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 24,620.00 USD | 8,320.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 21,910,000.00 USD | 0.00 USD | 21,910,000.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3036` | 16,870,000.00 USD | 0.00 USD | 16,870,000.00 USD | 1,260.00 USD | 3,230.00 USD | 12,600.00 USD |
| `7D` | `0.3037` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 3,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3041` | 16,850,000.00 USD | 0.00 USD | 16,850,000.00 USD | 1,130.00 USD | 9,300.00 USD | 75,700.00 USD |
| `1D` | `0.3046` | 16,770,000.00 USD | 0.00 USD | 16,770,000.00 USD | 41,400.00 USD | 18,130.00 USD | 7,480.00 USD |
| `7D` | `0.3049` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 18,020.00 USD | 0.00 USD | 106,090.00 USD |
| `1D` | `0.3051` | 16,700,000.00 USD | 0.00 USD | 16,700,000.00 USD | 24,960.00 USD | 13,680.00 USD | 73,970.00 USD |
| `7D` | `0.3055` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3056` | 16,590,000.00 USD | 0.00 USD | 16,590,000.00 USD | 48,690.00 USD | 13,380.00 USD | 37,740.00 USD |
| `1D` | `0.3061` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 19,420.00 USD | 2,350.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 21,730,000.00 USD | 0.00 USD | 21,730,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3066` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 38,030.00 USD | 29,620.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 21,650,000.00 USD | 0.00 USD | 21,650,000.00 USD | 6,430.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3071` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD |
| `7D` | `0.3073` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3076` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 23,570.00 USD | 8,060.00 USD | 0.00 USD |
| `7D` | `0.3079` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 38,480.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3081` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD |
| `7D` | `0.3085` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3086` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 598.72 USD | 0.00 USD | 15,810.00 USD |
| `1D` | `0.3091` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3096` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 21,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 83,770.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3101` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 42,020.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 21,380,000.00 USD | 0.00 USD | 21,380,000.00 USD | 72,010.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3106` | 16,090,000.00 USD | 0.00 USD | 16,090,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 21,240,000.00 USD | 0.00 USD | 21,240,000.00 USD | 5,160.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3116` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 2,250.00 USD | 17,210.00 USD | 17,620.00 USD |
| `1D` | `0.3121` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 24,790.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3121` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3126` | 15,970,000.00 USD | 0.00 USD | 15,970,000.00 USD | 15,000.00 USD | 13,530.00 USD | 7,580.00 USD |
| `7D` | `0.3127` | 21,020,000.00 USD | 0.00 USD | 21,020,000.00 USD | 16,080.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3131` | 15,930,000.00 USD | 0.00 USD | 15,930,000.00 USD | 3,900.00 USD | 28,470.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 20,890,000.00 USD | 0.00 USD | 20,890,000.00 USD | 10,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3136` | 15,880,000.00 USD | 0.00 USD | 15,880,000.00 USD | 5,830.00 USD | 34,540.00 USD | 9,590.00 USD |
| `7D` | `0.3139` | 20,880,000.00 USD | 0.00 USD | 20,880,000.00 USD | 12,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3141` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 7,520.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3146` | 15,810,000.00 USD | 0.00 USD | 15,810,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD |
| `1D` | `0.3151` | 15,810,000.00 USD | 0.00 USD | 15,810,000.00 USD | 6,830.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 197,800.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3156` | 15,770,000.00 USD | 0.00 USD | 15,770,000.00 USD | 35,910.00 USD | 3,680.00 USD | 10,790.00 USD |
| `7D` | `0.3157` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 403,130.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3161` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 7,880.00 USD | 2,990.00 USD | 5,450.00 USD |
| `7D` | `0.3163` | 19,720,000.00 USD | 0.00 USD | 19,720,000.00 USD | 478,060.00 USD | 174,600.00 USD | 189,520.00 USD |
| `1D` | `0.3166` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 46,600.00 USD | 37,250.00 USD | 17,210.00 USD |
| `7D` | `0.3169` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 414,720.00 USD | 104,590.00 USD | 135,950.00 USD |
| `1D` | `0.3171` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 9,020.00 USD | 35,130.00 USD | 35,030.00 USD |
| `7D` | `0.3175` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3176` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 52,670.00 USD | 9,730.00 USD | 30,850.00 USD |
| `1D` | `0.3181` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 259,620.00 USD | 43,420.00 USD | 72,180.00 USD |
| `7D` | `0.3181` | 17,960,000.00 USD | 0.00 USD | 17,960,000.00 USD | 744,820.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3186` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 149,850.00 USD | 58,500.00 USD | 64,330.00 USD |
| `7D` | `0.3187` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 409,740.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3191` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 251,300.00 USD | 13,910.00 USD | 81,230.00 USD |
| `7D` | `0.3193` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 192,420.00 USD | 123,840.00 USD | 247,300.00 USD |
| `1D` | `0.3196` | 14,440,000.00 USD | 0.00 USD | 14,440,000.00 USD | 95,570.00 USD | 187,520.00 USD | 252,980.00 USD |
| `7D` | `0.3199` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 5,810.00 USD | 191,160.00 USD | 267,030.00 USD |
| `1D` | `0.3201` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 263,400.00 USD | 72,570.00 USD | 153,860.00 USD |
| `7D` | `0.3205` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 172,060.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3206` | 13,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 164,150.00 USD | 31,270.00 USD | 142,380.00 USD |
| `1D` | `0.3211` | 13,080,000.00 USD | 0.00 USD | 13,080,000.00 USD | 143,990.00 USD | 48,000.00 USD | 113,300.00 USD |
| `7D` | `0.3211` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 561,850.00 USD | 135,070.00 USD | 244,340.00 USD |
| `1D` | `0.3216` | 12,770,000.00 USD | 0.00 USD | 12,770,000.00 USD | 8,430.00 USD | 33,650.00 USD | 155,370.00 USD |
| `7D` | `0.3217` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3221` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 98,860.00 USD | 45,010.00 USD | 72,520.00 USD |
| `7D` | `0.3223` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 649,350.00 USD | 265,170.00 USD | 156,030.00 USD |
| `1D` | `0.3226` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 73,350.00 USD | 33,350.00 USD | 245,020.00 USD |
| `7D` | `0.3229` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,650.00 USD |
| `1D` | `0.3231` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 92,790.00 USD | 55,060.00 USD | 120,280.00 USD |
| `7D` | `0.3235` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD |
| `1D` | `0.3236` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 61,120.00 USD | 106,740.00 USD | 175,040.00 USD |
| `1D` | `0.3241` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 966.93 USD | 40,210.00 USD | 132,060.00 USD |
| `7D` | `0.3241` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 434,620.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3246` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 383,940.00 USD | 95,040.00 USD | 339,620.00 USD |
| `7D` | `0.3247` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3251` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 744,360.00 USD | 100,090.00 USD | 387,350.00 USD |
| `7D` | `0.3253` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 339,740.00 USD |
| `1D` | `0.3256` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 662,530.00 USD | 100,910.00 USD | 365,380.00 USD |
| `7D` | `0.3259` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 432,530.00 USD | 308,400.00 USD | 503,650.00 USD |
| `1D` | `0.3261` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 206,710.00 USD | 375,900.00 USD | 555,160.00 USD |
| `7D` | `0.3265` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 78,960.00 USD | 324,810.00 USD | 500,270.00 USD |
| `1D` | `0.3266` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 91,040.00 USD | 193,200.00 USD | 374,210.00 USD |
| `1D` | `0.3271` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 255,030.00 USD | 131,960.00 USD | 412,860.00 USD |
| `7D` | `0.3271` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 318,340.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3276` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 269,510.00 USD | 70,470.00 USD | 255,720.00 USD |
| `7D` | `0.3277` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3281` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 164,690.00 USD | 78,800.00 USD | 138,990.00 USD |
| `7D` | `0.3283` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD |
| `1D` | `0.3286` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 45,960.00 USD | 48,460.00 USD | 162,370.00 USD |
| `7D` | `0.3289` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD |
| `1D` | `0.3291` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 109,890.00 USD | 66,400.00 USD | 152,210.00 USD |
| `7D` | `0.3295` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 255,900.00 USD | 83,080.00 USD | 279,220.00 USD |
| `1D` | `0.3296` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 167,290.00 USD | 15,860.00 USD | 85,070.00 USD |
| `1D` | `0.3301` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 36,460.00 USD | 76,790.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 184,120.00 USD | 47,610.00 USD | 0.00 USD |
| `1D` | `0.3306` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD |
| `7D` | `0.3307` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3311` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 28,510.00 USD | 122,460.00 USD | 599,930.00 USD |
| `7D` | `0.3313` | 850,120.00 USD | 0.00 USD | 850,120.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3316` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 44,750.00 USD | 113,100.00 USD | 28,340.00 USD |
| `7D` | `0.3319` | 799,470.00 USD | 0.00 USD | 799,470.00 USD | 0.00 USD | 57,890.00 USD | 196,110.00 USD |
| `1D` | `0.3321` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 45,760.00 USD | 23,430.00 USD | 100,730.00 USD |
| `7D` | `0.3325` | 545,470.00 USD | 0.00 USD | 545,470.00 USD | 251,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3326` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 69,290.00 USD | 9,670.00 USD | 39,970.00 USD |
| `1D` | `0.3331` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 139,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3331` | 294,230.00 USD | 0.00 USD | 294,230.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD |
| `1D` | `0.3336` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 34,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3346` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 20,610.00 USD | 8,820.00 USD | 0.00 USD |
| `1D` | `0.3351` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD |
| `1D` | `0.3371` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3376` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3397` | 254,160.00 USD | 0.00 USD | 254,160.00 USD | 0.00 USD | 0.00 USD | 254,160.00 USD |
| `1D` | `0.3401` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD |
| `7D` | `0.3402` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3403` | 376,470.00 USD | 376,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 376,470.00 USD |
| `1D` | `0.3406` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD |
| `7D` | `0.3409` | 852,850.00 USD | 852,850.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3411` | 832,870.00 USD | 0.00 USD | 832,870.00 USD | 112,120.00 USD | 0.00 USD | 45,840.00 USD |
| `7D` | `0.3415` | 974,140.00 USD | 974,140.00 USD | 0.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD |
| `1D` | `0.3416` | 674,910.00 USD | 0.00 USD | 674,910.00 USD | 343,500.00 USD | 0.00 USD | 211,420.00 USD |
| `1D` | `0.3421` | 119,990.00 USD | 0.00 USD | 119,990.00 USD | 71,180.00 USD | 0.00 USD | 48,810.00 USD |
| `7D` | `0.3421` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3422` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3427` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 229,350.00 USD | 384,540.00 USD |
| `1D` | `0.3431` | 490,220.00 USD | 490,220.00 USD | 0.00 USD | 166,310.00 USD | 238,840.00 USD | 85,070.00 USD |
| `7D` | `0.3433` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD |
| `1D` | `0.3436` | 725,790.00 USD | 725,790.00 USD | 0.00 USD | 0.00 USD | 141,640.00 USD | 93,930.00 USD |
| `1D` | `0.3441` | 770,860.00 USD | 770,860.00 USD | 0.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD |
| `7D` | `0.3445` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3446` | 952,130.00 USD | 952,130.00 USD | 0.00 USD | 0.00 USD | 75,030.00 USD | 106,240.00 USD |
| `1D` | `0.3451` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 154,220.00 USD | 63,000.00 USD | 254,020.00 USD |
| `7D` | `0.3451` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 196,110.00 USD |
| `1D` | `0.3456` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 231,820.00 USD | 37,860.00 USD | 281,350.00 USD |
| `7D` | `0.3457` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3461` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 263,140.00 USD | 240,590.00 USD | 528,570.00 USD |
| `7D` | `0.3463` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 251,240.00 USD | 290,920.00 USD | 205,410.00 USD |
| `1D` | `0.3466` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 135,220.00 USD | 83,230.00 USD | 156,500.00 USD |
| `7D` | `0.3469` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD |
| `1D` | `0.3471` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 81,330.00 USD | 45,970.00 USD | 61,300.00 USD |
| `7D` | `0.3475` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3476` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 86,450.00 USD | 64,310.00 USD | 45,010.00 USD |
| `1D` | `0.3481` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 73,970.00 USD | 38,390.00 USD | 128,800.00 USD |
| `7D` | `0.3481` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 32,530.00 USD | 42,810.00 USD |
| `1D` | `0.3486` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 10,620.00 USD | 62,880.00 USD | 76,450.00 USD |
| `7D` | `0.3487` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 19,250.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3491` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 42,120.00 USD | 28,080.00 USD | 61,240.00 USD |
| `7D` | `0.3493` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 93,150.00 USD | 52,660.00 USD |
| `1D` | `0.3496` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 34,020.00 USD | 13,050.00 USD | 121,570.00 USD |
| `7D` | `0.3499` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 133,330.00 USD | 0.00 USD | 139,610.00 USD |
| `1D` | `0.3501` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 52,670.00 USD | 9,040.00 USD | 426,410.00 USD |
| `7D` | `0.3505` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 6,140.00 USD | 19,280.00 USD | 0.00 USD |
| `1D` | `0.3506` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD |
| `1D` | `0.3511` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 2,790.00 USD | 16,810.00 USD | 32,490.00 USD |
| `7D` | `0.3511` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3516` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 52,740.00 USD | 5,720.00 USD | 135,720.00 USD |
| `7D` | `0.3517` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 6,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3521` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 47,300.00 USD | 21,980.00 USD | 78,700.00 USD |
| `7D` | `0.3523` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 205,490.00 USD |
| `1D` | `0.3526` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 14,390.00 USD | 17,990.00 USD | 28,910.00 USD |
| `7D` | `0.3529` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 137,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 139,090.00 USD | 98,020.00 USD | 108,090.00 USD |
| `7D` | `0.3535` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 5,810.00 USD | 98,000.00 USD | 187,450.00 USD |
| `1D` | `0.3536` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 194,810.00 USD | 16,340.00 USD | 195,270.00 USD |
| `1D` | `0.3541` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 101,070.00 USD | 96,770.00 USD | 0.00 USD |
| `7D` | `0.3541` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 808,620.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3546` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 8,680.00 USD | 60,460.00 USD | 69,820.00 USD |
| `7D` | `0.3547` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 15,040.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3551` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 16,020.00 USD | 46,910.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3556` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 23,440.00 USD | 73,670.00 USD | 0.00 USD |
| `7D` | `0.3559` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 9,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3561` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 859.20 USD | 25,000.00 USD | 106,140.00 USD |
| `7D` | `0.3565` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 4,730.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3566` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 5,680.00 USD | 11,630.00 USD | 39,520.00 USD |
| `1D` | `0.3571` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `0.3571` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3576` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 161,860.00 USD | 18,380.00 USD | 0.00 USD |
| `7D` | `0.3577` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3581` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 3,860.00 USD | 0.00 USD | 38,950.00 USD |
| `7D` | `0.3583` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 4,040.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3586` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD |
| `7D` | `0.3589` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 10,970.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3591` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 22,510.00 USD | 15,750.00 USD | 33,590.00 USD |
| `7D` | `0.3595` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3596` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 139,210.00 USD | 12,460.00 USD | 99,590.00 USD |
| `1D` | `0.3601` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD |
| `7D` | `0.3601` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 7,660.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3606` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 62,630.00 USD | 32,860.00 USD | 195,380.00 USD |
| `7D` | `0.3607` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3611` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 86,800.00 USD | 60,060.00 USD | 190,770.00 USD |
| `7D` | `0.3613` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3616` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 228,030.00 USD | 38,210.00 USD | 150,170.00 USD |
| `7D` | `0.3619` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 3,550.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3621` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 144,510.00 USD | 113,560.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3626` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 100,410.00 USD | 49,330.00 USD | 0.00 USD |
| `1D` | `0.3631` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 1,260,000.00 USD | 102,260.00 USD | 93,510.00 USD |
| `7D` | `0.3631` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3636` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 183,690.00 USD | 48,500.00 USD | 185,880.00 USD |
| `7D` | `0.3637` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3641` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 85,150.00 USD | 229,250.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3646` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 351,270.00 USD | 21,220.00 USD | 62,250.00 USD |
| `7D` | `0.3649` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 180,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3651` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 2,860.00 USD | 67,160.00 USD | 207,000.00 USD |
| `7D` | `0.3655` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 681,380.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3656` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 519,740.00 USD | 133,520.00 USD | 290,540.00 USD |
| `1D` | `0.3661` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 277,650.00 USD | 111,580.00 USD | 96,250.00 USD |
| `7D` | `0.3661` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 685,520.00 USD | 66,940.00 USD | 238,480.00 USD |
| `1D` | `0.3666` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 484,790.00 USD | 124,300.00 USD | 66,840.00 USD |
| `7D` | `0.3667` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 419,350.00 USD | 34,510.00 USD | 166,250.00 USD |
| `1D` | `0.3671` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,630.00 USD | 93,830.00 USD | 412,340.00 USD |
| `7D` | `0.3673` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3676` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 76,720.00 USD | 53,460.00 USD | 218,560.00 USD |
| `7D` | `0.3679` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3681` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 769,010.00 USD | 104,570.00 USD | 103,470.00 USD |
| `7D` | `0.3685` | 15,160,000.00 USD | 15,160,000.00 USD | 0.00 USD | 2,020.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3686` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 327,450.00 USD | 157,020.00 USD | 145,380.00 USD |
| `1D` | `0.3691` | 17,530,000.00 USD | 17,530,000.00 USD | 0.00 USD | 475,810.00 USD | 51,700.00 USD | 23,760.00 USD |
| `7D` | `0.3691` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3696` | 17,800,000.00 USD | 17,800,000.00 USD | 0.00 USD | 163,960.00 USD | 88,200.00 USD | 17,010.00 USD |
| `7D` | `0.3697` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 4,850.00 USD | 175,510.00 USD | 55,840.00 USD |
| `1D` | `0.3701` | 18,550,000.00 USD | 18,550,000.00 USD | 0.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD |
| `7D` | `0.3703` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 52,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3706` | 19,380,000.00 USD | 19,380,000.00 USD | 0.00 USD | 249,050.00 USD | 8,320.00 USD | 573,510.00 USD |
| `7D` | `0.3709` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3711` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 549,150.00 USD | 105,970.00 USD | 225,950.00 USD |
| `7D` | `0.3715` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 3,410.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3716` | 21,390,000.00 USD | 21,390,000.00 USD | 0.00 USD | 76,250.00 USD | 229,370.00 USD | 817,010.00 USD |
| `1D` | `0.3721` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 20,850.00 USD | 62,750.00 USD | 116,090.00 USD |
| `7D` | `0.3721` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 786,960.00 USD |
| `1D` | `0.3726` | 22,720,000.00 USD | 22,720,000.00 USD | 0.00 USD | 512,200.00 USD | 31,730.00 USD | 587,700.00 USD |
| `7D` | `0.3727` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3731` | 23,900,000.00 USD | 23,900,000.00 USD | 0.00 USD | 72,270.00 USD | 152,050.00 USD | 954,660.00 USD |
| `7D` | `0.3733` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3736` | 24,120,000.00 USD | 24,120,000.00 USD | 0.00 USD | 224,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3741` | 24,760,000.00 USD | 24,760,000.00 USD | 0.00 USD | 68,340.00 USD | 166,120.00 USD | 403,580.00 USD |
| `7D` | `0.3745` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD |
| `1D` | `0.3746` | 25,190,000.00 USD | 25,190,000.00 USD | 0.00 USD | 37,630.00 USD | 50,320.00 USD | 341,310.00 USD |
| `1D` | `0.3751` | 26,060,000.00 USD | 26,060,000.00 USD | 0.00 USD | 363,100.00 USD | 6,290.00 USD | 497,990.00 USD |
| `1D` | `0.3756` | 26,350,000.00 USD | 26,350,000.00 USD | 0.00 USD | 23,190.00 USD | 1,940.00 USD | 265,460.00 USD |
| `7D` | `0.3757` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3761` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 303,200.00 USD | 77,030.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3766` | 27,630,000.00 USD | 27,630,000.00 USD | 0.00 USD | 21,660.00 USD | 24,840.00 USD | 12,250.00 USD |
| `7D` | `0.3769` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3771` | 27,680,000.00 USD | 27,680,000.00 USD | 0.00 USD | 0.00 USD | 32,810.00 USD | 15,810.00 USD |
| `1D` | `0.3776` | 27,760,000.00 USD | 27,760,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3780` | 27,770,000.00 USD | 27,770,000.00 USD | 0.00 USD | 14,580.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `438.72M` | Total OI Tokens: `1,286,870,269.2 TRX`
  * 1h OI Change: `+3.88%` | 4h OI Change: `+8.48%` | 24h OI Change: `+53.23%`
  * Exchange Breakdown: Binance=`109.68M` | Bybit=`86.50M` | OKX=`27.94M` | Hyperliquid=`19.48M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-181.49K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0778%` | **USDT OKX** | `-0.3811%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0128%` |
| **USDT MEXC** | `-0.0778%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.1824%` | **USDT Bitget** | `-0.1954%` |
| **CoinM Binance** | `-0.1433%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `51.06%` | `48.94%` | `1.04` | 55,450,000.00 USD |
| `15M` | `Binance` | `50.69%` | `49.31%` | `1.03` | 17,360,000.00 USD |
| `15M` | `OKX` | `50.19%` | `49.81%` | `1.01` | 9,160,000.00 USD |
| `15M` | `Bybit` | `56.23%` | `43.77%` | `1.28` | 5,430,000.00 USD |
| `15M` | `KuCoin` | `47.24%` | `52.76%` | `0.90` | 41,130.00 USD |
| `15M` | `Gate` | `53.65%` | `46.35%` | `1.16` | 5,420,000.00 USD |
| `15M` | `Bitget` | `41.03%` | `58.97%` | `0.70` | 1,400,000.00 USD |
| `15M` | `BingX` | `46.02%` | `53.98%` | `0.85` | 4,350,000.00 USD |
| `15M` | `MEXC` | `46.12%` | `53.88%` | `0.86` | 3,010,000.00 USD |
| `15M` | `Bitunix` | `58.91%` | `41.09%` | `1.43` | 1,920,000.00 USD |
| `15M` | `Hyperliquid` | `54.9%` | `45.1%` | `1.22` | 487,790.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `42.01%` | `57.99%` | `0.72` | 2,500,000.00 USD |
| `15M` | `Crypto.com` | `41.29%` | `58.71%` | `0.70` | 78,620.00 USD |
| `15M` | `WhiteBIT` | `5.09%` | `94.91%` | `0.05` | 1,350,000.00 USD |
| `15M` | `HTX` | `38.81%` | `61.19%` | `0.63` | 49,840.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.2%` | `9.8%` | `9.20` | 2,410,000.00 USD |
| `15M` | `Aster` | `50.26%` | `49.74%` | `1.01` | 216,640.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.83%` | `55.17%` | `0.81` | 272,280.00 USD |
| `15M` | `Whale Positions` | `50.69%` | `49.31%` | `1.03` | 17,360,000.00 USD |
| `15M` | `Global Accounts` | `51.06%` | `48.94%` | `1.04` | 55,450,000.00 USD |
| `1H` | `TRX` | `45.32%` | `54.68%` | `0.83` | 58,070,000.00 USD |
| `1H` | `Binance` | `41.79%` | `58.21%` | `0.72` | 33,910,000.00 USD |
| `1H` | `OKX` | `52%` | `48%` | `1.08` | 6,280,000.00 USD |
| `1H` | `Bybit` | `47.55%` | `52.45%` | `0.91` | 5,470,000.00 USD |
| `1H` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 528,120.00 USD |
| `1H` | `Gate` | `54.2%` | `45.8%` | `1.18` | 2,840,000.00 USD |
| `1H` | `Bitget` | `53.38%` | `46.62%` | `1.15` | 849,910.00 USD |
| `1H` | `BingX` | `58.19%` | `41.81%` | `1.39` | 1,070,000.00 USD |
| `1H` | `MEXC` | `65.92%` | `34.08%` | `1.93` | 791,070.00 USD |
| `1H` | `Bitunix` | `49.26%` | `50.74%` | `0.97` | 1,780,000.00 USD |
| `1H` | `Hyperliquid` | `40.6%` | `59.4%` | `0.68` | 1,850,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.81%` | `49.19%` | `1.03` | 621,830.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `25.91%` | `74.09%` | `0.35` | 411,770.00 USD |
| `1H` | `HTX` | `40.66%` | `59.34%` | `0.69` | 444,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.59%` | `51.41%` | `0.95` | 62,430.00 USD |
| `1H` | `Aster` | `52.63%` | `47.37%` | `1.11` | 852,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.92%` | `47.08%` | `1.12` | 315,110.00 USD |
| `1H` | `Whale Positions` | `41.79%` | `58.21%` | `0.72` | 33,910,000.00 USD |
| `1H` | `Global Accounts` | `45.32%` | `54.68%` | `0.83` | 58,070,000.00 USD |
| `4H` | `TRX` | `47.65%` | `52.35%` | `0.91` | 1,010,000,000.00 USD |
| `4H` | `Binance` | `47.98%` | `52.02%` | `0.92` | 311,220,000.00 USD |
| `4H` | `OKX` | `44.82%` | `55.18%` | `0.81` | 215,500,000.00 USD |
| `4H` | `Bybit` | `48.45%` | `51.55%` | `0.94` | 83,710,000.00 USD |
| `4H` | `KuCoin` | `47.37%` | `52.63%` | `0.90` | 4,180,000.00 USD |
| `4H` | `Gate` | `51.35%` | `48.65%` | `1.06` | 78,460,000.00 USD |
| `4H` | `Bitget` | `43.11%` | `56.89%` | `0.76` | 44,370,000.00 USD |
| `4H` | `BingX` | `46.73%` | `53.27%` | `0.88` | 47,530,000.00 USD |
| `4H` | `MEXC` | `50.28%` | `49.72%` | `1.01` | 85,350,000.00 USD |
| `4H` | `Bitunix` | `47.5%` | `52.5%` | `0.90` | 40,610,000.00 USD |
| `4H` | `Hyperliquid` | `51.62%` | `48.38%` | `1.07` | 33,590,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.67%` | `49.33%` | `1.03` | 25,440,000.00 USD |
| `4H` | `Crypto.com` | `43.78%` | `56.22%` | `0.78` | 3,010,000.00 USD |
| `4H` | `WhiteBIT` | `48.55%` | `51.45%` | `0.94` | 14,610,000.00 USD |
| `4H` | `HTX` | `57.74%` | `42.26%` | `1.37` | 1,360,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.25%` | `50.75%` | `0.97` | 9,280,000.00 USD |
| `4H` | `Aster` | `37.29%` | `62.71%` | `0.59` | 7,260,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.89%` | `51.11%` | `0.96` | 9,120,000.00 USD |
| `4H` | `Whale Positions` | `47.98%` | `52.02%` | `0.92` | 311,220,000.00 USD |
| `4H` | `Global Accounts` | `47.65%` | `52.35%` | `0.91` | 1,010,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3360` | `0.3335` | 1,833,198.85 USD | 904,870.52 USD | 928,328.33 USD | -23,457.81 USD | `-1.28%` | `23B / 24S` |
| `5:00 UTC` | `0.3348` | `0.3371` | `0.3348` | `0.3399` | `0.3343` | 3,666,829.89 USD | 1,892,139.69 USD | 1,774,690.20 USD | 117,449.48 USD | `+3.20%` | `16B / 11S` |
| `0:00 UTC` | `0.3400` | `0.3396` | `0.3400` | `0.3409` | `0.3377` | 6,444,023.59 USD | 2,423,214.82 USD | 4,020,808.77 USD | -1,597,593.95 USD | `-24.79%` | `17B / 14S` |
| `5:00 UTC` | `0.3416` | `0.3406` | `0.3416` | `0.3423` | `0.3377` | 3,912,907.38 USD | 1,652,823.17 USD | 2,260,084.21 USD | -607,261.04 USD | `-15.52%` | `9B / 17S` |
| `0:00 UTC` | `0.3421` | `0.3418` | `0.3421` | `0.3426` | `0.3408` | 2,715,323.02 USD | 1,103,827.83 USD | 1,611,495.19 USD | -507,667.36 USD | `-18.70%` | `47B / 36S` |

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
| `5m` | 81,470.00 USD | -420,300.00 USD | **`DISTRIBUTION`** |
| `15m` | 117,770.00 USD | -948,220.00 USD | **`DISTRIBUTION`** |
| `30m` | 581,790.00 USD | -923,510.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,150,000.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,860,000.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 419,750.00 USD | 2,330,000.00 USD | **`ACCUMULATION`** |
| `6h` | 7,100,000.00 USD | -6,450,000.00 USD | **`ACCUMULATION`** |
| `8h` | 9,790,000.00 USD | -9,470,000.00 USD | **`ACCUMULATION`** |
| `12h` | 15,470,000.00 USD | 2,480,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,850,000.00 USD | 3,740,000.00 USD | **`ACCUMULATION`** |
| `1w` | 11,060,000.00 USD | 2,800,000.00 USD | **`ACCUMULATION`** |
| `30d` | -12,320,000.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+81.47K` | 15m=`+117.77K` | 1h=`-1.15M` | 24h=`+18.85M`
* Futures Capital Netflows: 5m=`-420.30K` | 15m=`-948.22K` | 1h=`-1.84M` | 24h=`+3.74M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `-0.8652` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.35`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.56` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.65`
  * Mathematical Lot Sizing: **`8.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3420`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
