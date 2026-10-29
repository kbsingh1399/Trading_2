# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:10:46 IST` (`2026-10-29 22:40:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3404` | **Live Ask Quote**: `0.3447` | **Mid Price**: `0.3426`
- **Spread Points**: `43.00` | **Spread BPS**: `125.53 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3426` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3449` | Lower -3.00σ Band: `0.3402`
  * Upper +2.51σ Band: `0.3444` | Lower -2.51σ Band: `0.3407`
  * Upper +2.01σ Band: `0.3440` | Lower -2.01σ Band: `0.3411`
  * Upper +2.00σ Band: `0.3439` | Lower -2.00σ Band: `0.3412`
  * Upper +1.28σ Band: `0.3435` | Lower -1.28σ Band: `0.3416`
  * Upper +1.00σ Band: `0.3432` | Lower -1.00σ Band: `0.3419`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3426` | EMA-20=`0.3426` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3426` (Slope: `+0.0000`) | EMA-100=`0.3426`
  * Institutional Anchors: EMA-144=`0.3426` | EMA-200=`0.3426` (Slope: `+0.0000`) | EMA-233=`0.3426`
- **Range Boundaries**: 24H High=`0.3460` | 24H Low=`0.3391` | Weekly High=`0.3494` | Weekly Low=`0.3357`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3566` (Distance: `-3.96%`)
  * Point of Control (POC) = `0.3441` (Distance: `-0.48%`)
  * Value Area Low (VAL) = `0.3395` (Distance: `+0.86%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3316` | Weekly POC=`0.3306` | Weekly VAL=`0.3272`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3439` | Low=`0.3412`
  * New York Session (13:00-21:00 UTC): High=`0.3446` | Low=`0.3405`
  * Initial Balance (First Hour): IB High=`0.3436` | IB Low=`0.3415`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3412` - `0.3439`
  * Optimal Trade Entry (OTE 0.705): `0.3432`
  * Structural Invalidation Anchor (0.786): `0.3453`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3520` | `0.3575` | `0.3488` | `0.3497` | `32,239,324` | 11,433,377.47 USD | -1,226,107.29 USD | `-10.72%` | 4,329,871.91 USD | `-2.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3497` | `0.3516` | `0.3423` | `0.3431` | `27,936,990` | 9,677,954.97 USD | -1,464,347.34 USD | `-15.13%` | 2,865,524.57 USD | `-1.98` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3431` | `0.3446` | `0.3367` | `0.3425` | `34,179,625` | 11,665,788.02 USD | -1,727,135.84 USD | `-14.81%` | 1,138,388.73 USD | `-2.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3605` | `0.3653` | `0.3449` | `0.3530` | `133,186,039` | 47,319,855.69 USD | 2,137,266.99 USD | `+4.52%` | 5,430,763.65 USD | `+2.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3530` | `0.3575` | `0.3423` | `0.3431` | `84,180,944` | 29,513,228.46 USD | -2,580,728.73 USD | `-8.74%` | 2,850,034.92 USD | `-2.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3431` | `0.3446` | `0.3367` | `0.3425` | `34,179,625` | 11,665,788.02 USD | -1,727,135.84 USD | `-14.81%` | 1,122,899.08 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3315` | `0.3363` | `0.3285` | `0.3295` | `44,626,076` | 14,795,667.86 USD | -1,967,377.84 USD | `-13.30%` | 36,856.06 USD | `-3.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3295` | `0.3650` | `0.3282` | `0.3605` | `269,212,638` | 93,735,194.61 USD | 3,250,400.68 USD | `+3.47%` | 3,287,256.74 USD | `+3.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3605` | `0.3653` | `0.3367` | `0.3425` | `251,546,608` | 88,498,872.17 USD | -2,170,597.58 USD | `-2.45%` | 1,116,659.16 USD | `-2.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3428` | `565,189,047` | 196,962,509.91 USD | -859,432.33 USD | `-0.44%` | 985,793.39 USD | `-2.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,247,572.49 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 1,263,826.68 USD | `-1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3428` | `565,189,047` | 196,962,509.91 USD | -859,432.33 USD | `-0.44%` | 985,793.39 USD | `-2.02` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3426`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `763` | `0xecb6...2b00` | `LONG` | 2,984,633.19 USD | `8,562,753.00` | `0.3330` | `0.3471` | `0.000000` | 133,491.96 USD | `+4.47%` | `10X Cross` |
| `1588` | `0xeadc...9d55` | `LONG` | 1,374,200.00 USD | `4,000,000.00` | `0.3421` | `0.3471` | `0.000000` | 5,721.91 USD | `+0.42%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3323` | 5,265.80 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 5.27K USD at 0.3323 USD [API] | `2026-10-28 14:05:34` |
| `ANNOUNCEMENT` | `INFO` | `0.3320` | 5,900.17 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.90K USD at 0.3320 USD [API] | `2026-10-28 14:11:55` |
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 6,000.27 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.00K USD at 0.3317 USD [API] | `2026-10-28 14:24:57` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 8,102.66 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3316 USD [API] | `2026-10-28 14:28:34` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 8,102.66 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3316 USD [API] | `2026-10-28 14:38:49` |
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 5,015.61 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.02K USD at 0.3317 USD [API] | `2026-10-28 14:55:42` |
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 8,106.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.11K USD at 0.3317 USD [API] | `2026-10-28 15:07:33` |
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 8,104.86 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3317 USD [API] | `2026-10-28 15:12:03` |
| `ANNOUNCEMENT` | `INFO` | `0.3313` | 5,229.92 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.23K USD at 0.3313 USD [API] | `2026-10-28 15:27:25` |
| `ANNOUNCEMENT` | `INFO` | `0.3315` | 8,101.20 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3315 USD [API] | `2026-10-28 15:39:12` |
| `ANNOUNCEMENT` | `INFO` | `0.3311` | 8,091.18 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.09K USD at 0.3311 USD [API] | `2026-10-28 15:53:17` |
| `ANNOUNCEMENT` | `INFO` | `0.3301` | 7,523.39 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.52K USD at 0.3301 USD [API] | `2026-10-28 17:28:38` |
| `ANNOUNCEMENT` | `INFO` | `0.3299` | 6,042.81 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.04K USD at 0.3299 USD [API] | `2026-10-28 17:35:01` |
| `ANNOUNCEMENT` | `INFO` | `0.3302` | 8,091.87 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.09K USD at 0.3302 USD [API] | `2026-10-28 18:00:01` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3653` (Vol: 750,600.00 USD, Dist: `+2.98%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.3660` (Vol: 716,000.00 USD, Dist: `+3.20%`) | Long MP=`0.3251` (Vol: 834,600.00 USD, Dist: `--8.34%`)
  * 3D Horizon: Short MP=`0.3662` (Vol: 754,300.00 USD, Dist: `+3.24%`) | Long MP=`0.3251` (Vol: 826,400.00 USD, Dist: `--8.34%`)
  * 7D Horizon: Short MP=`0.3665` (Vol: 807,400.00 USD, Dist: `+3.35%`) | Long MP=`0.3251` (Vol: 887,200.00 USD, Dist: `--8.34%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0815` | 169.44 USD | 451,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 3,490.00 USD | 451,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 538.54 USD | 447,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 447,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,480.00 USD | 446,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 10,710.00 USD | 441,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 430,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 484.50 USD | 430,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 429,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 49,110.00 USD | 409,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 471.50 USD | 360,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 359,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,200.00 USD | 358,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 433.81 USD | 354,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 354,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 3,810.00 USD | 353,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1955` | 275.85 USD | 350,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 638.40 USD | 349,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2005` | 1,210.00 USD | 349,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2055` | 185.77 USD | 348,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 221.02 USD | 347,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,740.00 USD | 347,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 1,530.00 USD | 345,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 344,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 2,350.00 USD | 343,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 341,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,080.00 USD | 336,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,380.00 USD | 334,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 308.30 USD | 332,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,980.00 USD | 332,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 729.53 USD | 330,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,140.00 USD | 329,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 8,970.00 USD | 323,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 345.56 USD | 314,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,480.00 USD | 313,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 174.12 USD | 312,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 139.92 USD | 312,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 312,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 6,400.00 USD | 311,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 276.57 USD | 304,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,590.00 USD | 304,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 302,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 2,330.00 USD | 300,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 108.56 USD | 298,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,830.00 USD | 298,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 450.92 USD | 290,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 194.47 USD | 290,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 289,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 289,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 108,910.00 USD | 289,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 5,580.00 USD | 180,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 182.70 USD | 174,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 12,870.00 USD | 174,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 161,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,120.00 USD | 155,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 154,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 139,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 445.95 USD | 137,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 137,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 35,560.00 USD | 136,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 101,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 100,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 99,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 96,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2959` | 14,080,000.00 USD | 14,080,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2965` | 14,080,000.00 USD | 14,080,000.00 USD | 14,230.00 USD | 6,710.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,710.00 USD | 95,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2971` | 14,050,000.00 USD | 14,050,000.00 USD | 18,240.00 USD | 7,550.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2977` | 14,010,000.00 USD | 14,010,000.00 USD | 17,630.00 USD | 6,840.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,830,000.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 13,980,000.00 USD | 13,980,000.00 USD | 109,110.00 USD | 18,870.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,740,000.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,580,000.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2989` | 13,810,000.00 USD | 13,810,000.00 USD | 55,860.00 USD | 8,480.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,480,000.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2995` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 94,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 5,200.00 USD | 94,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 13,740,000.00 USD | 13,740,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 78,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 13,680,000.00 USD | 13,680,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 589.40 USD | 77,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3049` | 13,630,000.00 USD | 13,630,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,440,000.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 13,550,000.00 USD | 13,550,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,440,000.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 138.70 USD | 77,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,440,000.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 15,050.00 USD | 77,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 13,430,000.00 USD | 13,430,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,440,000.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,440,000.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 13,340,000.00 USD | 13,340,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,430,000.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 13,320,000.00 USD | 13,320,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,430,000.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,420,000.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 13,320,000.00 USD | 13,320,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 62,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,420,000.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 13,300,000.00 USD | 13,300,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,420,000.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 292.48 USD | 55,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 13,300,000.00 USD | 13,300,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 13,300,000.00 USD | 13,300,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 668.82 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,420,000.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,420,000.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 138.31 USD | 54,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,420,000.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,410,000.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 14,170.00 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 13,180,000.00 USD | 13,180,000.00 USD | 2,260.00 USD | 3,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,410,000.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,400,000.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 13,180,000.00 USD | 13,180,000.00 USD | 164.40 USD | 0.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,390,000.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 25,410.00 USD | 40,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 13,150,000.00 USD | 13,150,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,390,000.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,390,000.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 13,150,000.00 USD | 13,150,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 541.88 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,160,000.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3151` | 13,140,000.00 USD | 13,140,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,030,000.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,820,000.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,610,000.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 13,130,000.00 USD | 13,130,000.00 USD | 69,350.00 USD | 22,290.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,070,000.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3169` | 13,010,000.00 USD | 13,010,000.00 USD | 87,450.00 USD | 19,720.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,090,000.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 12,870,000.00 USD | 12,870,000.00 USD | 20,240.00 USD | 18,720.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,610,000.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,530,000.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 12,810,000.00 USD | 12,810,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,210,000.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 12,260,000.00 USD | 12,260,000.00 USD | 180,660.00 USD | 22,910.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,500,000.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,340,000.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 12,020,000.00 USD | 12,020,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 11,980,000.00 USD | 11,980,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,260,000.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 11,670,000.00 USD | 11,670,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,050,000.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,550,000.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,260,000.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 11,420,000.00 USD | 11,420,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,840,000.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 11,130,000.00 USD | 11,130,000.00 USD | 139,110.00 USD | 82,020.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,150,000.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 10,710,000.00 USD | 10,710,000.00 USD | 136,920.00 USD | 84,820.00 USD | 170,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,080,000.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,200,000.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 10,310,000.00 USD | 10,310,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,610,000.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 10,120,000.00 USD | 10,120,000.00 USD | 568,770.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,270,000.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,380,000.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 9,130,000.00 USD | 9,130,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 129.22 USD | 594.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 7,760,000.00 USD | 7,760,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3265` | 464.94 USD | 464.94 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3271` | 7,240,000.00 USD | 7,240,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3277` | 6,780,000.00 USD | 6,780,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3289` | 6,310,000.00 USD | 6,310,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 6,110,000.00 USD | 6,110,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3307` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 13,130.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 5,930,000.00 USD | 5,930,000.00 USD | 234,580.00 USD | 121,210.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 5,240,000.00 USD | 5,240,000.00 USD | 158,550.00 USD | 32,400.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 4,760,000.00 USD | 4,760,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3331` | 4,420,000.00 USD | 4,420,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3337` | 4,420,000.00 USD | 4,420,000.00 USD | 147,860.00 USD | 113,790.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 3,590,000.00 USD | 3,590,000.00 USD | 76,100.00 USD | 31,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3349` | 3,480,000.00 USD | 3,480,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3355` | 3,140,000.00 USD | 3,140,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3361` | 3,040,000.00 USD | 3,040,000.00 USD | 177,350.00 USD | 0.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 2,800,000.00 USD | 2,800,000.00 USD | 240,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3373` | 2,560,000.00 USD | 2,560,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3379` | 2,550,000.00 USD | 2,550,000.00 USD | 292,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 2,260,000.00 USD | 2,260,000.00 USD | 179,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3385` | 511.81 USD | 511.81 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3391` | 2,080,000.00 USD | 2,080,000.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3395` | 12,820.00 USD | 13,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3397` | 2,080,000.00 USD | 2,080,000.00 USD | 858.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 2,080,000.00 USD | 2,080,000.00 USD | 1,240.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 1,960,000.00 USD | 1,960,000.00 USD | 2,300.00 USD | 62,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 1,890,000.00 USD | 1,890,000.00 USD | 627,050.00 USD | 0.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3415` | 86.06 USD | 13,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3421` | 1,200,000.00 USD | 1,200,000.00 USD | 395,080.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3427` | 689,020.00 USD | 689,020.00 USD | 262,640.00 USD | 18,020.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3433` | 220,540.00 USD | 220,540.00 USD | 0.00 USD | 44,190.00 USD | 176,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3439` | 1,220,000.00 USD | 1,220,000.00 USD | 777,990.00 USD | 48,730.00 USD | 392,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 1,830,000.00 USD | 1,830,000.00 USD | 291,770.00 USD | 106,440.00 USD | 217,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 2,330,000.00 USD | 2,330,000.00 USD | 121,080.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3457` | 2,610,000.00 USD | 2,610,000.00 USD | 1,150.00 USD | 21,670.00 USD | 258,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3487` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3499` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3505` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 68,910.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 117,900.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 279,270.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 1,930.00 USD | 15,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3541` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 141,810.00 USD | 704,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3547` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 128,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3559` | 9,310,000.00 USD | 9,310,000.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 161,260.00 USD | 578,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 10,440,000.00 USD | 10,440,000.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 400,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3595` | 11,310,000.00 USD | 11,310,000.00 USD | 199,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 31,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 12,310,000.00 USD | 12,310,000.00 USD | 966,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 12,410,000.00 USD | 12,410,000.00 USD | 98,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 12,600,000.00 USD | 12,600,000.00 USD | 194,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 12,790,000.00 USD | 12,790,000.00 USD | 186,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 13,050,000.00 USD | 13,050,000.00 USD | 259,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 68.54 USD | 15,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 13,390,000.00 USD | 13,390,000.00 USD | 341,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 13,440,000.00 USD | 13,440,000.00 USD | 5,540.00 USD | 48,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3679` | 14,190,000.00 USD | 14,190,000.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 14,650,000.00 USD | 14,650,000.00 USD | 326,450.00 USD | 141,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3691` | 14,980,000.00 USD | 14,980,000.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 15,160,000.00 USD | 15,160,000.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 15,920,000.00 USD | 15,920,000.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 16,450,000.00 USD | 16,450,000.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 17,920,000.00 USD | 17,920,000.00 USD | 438,840.00 USD | 62,210.00 USD | 969,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 289.77 USD | 15,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3721` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3727` | 19,280,000.00 USD | 19,280,000.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 20,140,000.00 USD | 20,140,000.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3739` | 20,630,000.00 USD | 20,630,000.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 21,010,000.00 USD | 21,010,000.00 USD | 30,710.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 15,630.00 USD | 31,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 21,850,000.00 USD | 21,850,000.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 55,050.00 USD | 86,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 22,130,000.00 USD | 22,130,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 23,370,000.00 USD | 23,370,000.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3765` | 34,780.00 USD | 121,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3769` | 23,430,000.00 USD | 23,430,000.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3775` | 23,500,000.00 USD | 23,500,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3781` | 23,730,000.00 USD | 23,730,000.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 685.46 USD | 121,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 24,240,000.00 USD | 24,240,000.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 24,440,000.00 USD | 24,440,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 679,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3799` | 24,440,000.00 USD | 24,440,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 24,780,000.00 USD | 24,780,000.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3805` | 323.43 USD | 680,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3823` | 25,020,000.00 USD | 25,020,000.00 USD | 2,080.00 USD | 3,950.00 USD | 239,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3829` | 25,020,000.00 USD | 25,020,000.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 25,240,000.00 USD | 25,240,000.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 665.37 USD | 680,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3841` | 25,240,000.00 USD | 25,240,000.00 USD | 850.22 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 680,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3847` | 25,240,000.00 USD | 25,240,000.00 USD | 899.18 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3871` | 25,290,000.00 USD | 25,290,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3883` | 25,290,000.00 USD | 25,290,000.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 685,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 25,330,000.00 USD | 25,330,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3913` | 25,510,000.00 USD | 25,510,000.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 686,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 25,580,000.00 USD | 25,580,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 25,650,000.00 USD | 25,650,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3925` | 21,850.00 USD | 707,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3931` | 25,740,000.00 USD | 25,740,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3937` | 25,810,000.00 USD | 25,810,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 26,030,000.00 USD | 26,030,000.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 776,680.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 26,160,000.00 USD | 26,160,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 26,350,000.00 USD | 26,350,000.00 USD | 55,640.00 USD | 47,870.00 USD | 92,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3961` | 26,460,000.00 USD | 26,460,000.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 111.42 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3967` | 26,550,000.00 USD | 26,550,000.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 26,720,000.00 USD | 26,720,000.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3975` | 502.84 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3979` | 27,110,000.00 USD | 27,110,000.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 27,120,000.00 USD | 27,120,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3991` | 27,150,000.00 USD | 27,150,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3997` | 27,250,000.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 27,340,000.00 USD | 27,340,000.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4009` | 27,500,000.00 USD | 27,500,000.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4027` | 27,580,000.00 USD | 27,580,000.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4045` | 27,670,000.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4057` | 27,780,000.00 USD | 27,780,000.00 USD | 0.00 USD | 8,920.00 USD | 97,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4095` | 5,150.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4115` | 6,020.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,010.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 2,950.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4305` | 203.20 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 67,500.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4375` | 183.31 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 29,420.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4395` | 71,540.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4435` | 635,130.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4495` | 272,040.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 103.98 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5215` | 1,720.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5295` | 12,150.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5305` | 644,210.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 8,270.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 728,400.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6165` | 24,660.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6355` | 6,350.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6525` | 242.08 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 27,950.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6745` | 83,190.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6935` | 414.71 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7015` | 106.63 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0815` | 451,440.00 USD | 0.00 USD | 169.44 USD | `-77.41%` | `2,079.00` |
| `Live` | `Long` | `0.0855` | 451,270.00 USD | 0.00 USD | 3,490.00 USD | `-76.30%` | `40,871.00` |
| `Live` | `Long` | `0.1025` | 447,780.00 USD | 0.00 USD | 538.54 USD | `-71.59%` | `5,254.00` |
| `Live` | `Long` | `0.1175` | 447,240.00 USD | 0.00 USD | 394.80 USD | `-67.43%` | `3,360.00` |
| `Live` | `Long` | `0.1385` | 446,840.00 USD | 0.00 USD | 5,480.00 USD | `-61.61%` | `39,551.00` |
| `Live` | `Long` | `0.1395` | 441,370.00 USD | 0.00 USD | 10,710.00 USD | `-61.33%` | `76,797.00` |
| `Live` | `Long` | `0.1595` | 430,650.00 USD | 0.00 USD | 390.46 USD | `-55.79%` | `2,448.00` |
| `Live` | `Long` | `0.1615` | 430,260.00 USD | 0.00 USD | 484.50 USD | `-55.23%` | `3,000.00` |
| `Live` | `Long` | `0.1705` | 429,780.00 USD | 0.00 USD | 20,360.00 USD | `-52.74%` | `119,400.00` |
| `Live` | `Long` | `0.1735` | 409,420.00 USD | 0.00 USD | 49,110.00 USD | `-51.90%` | `283,067.00` |
| `Live` | `Long` | `0.1745` | 360,310.00 USD | 0.00 USD | 471.50 USD | `-51.63%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 359,840.00 USD | 0.00 USD | 1,030.00 USD | `-51.35%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 358,810.00 USD | 0.00 USD | 4,200.00 USD | `-51.07%` | `23,777.00` |
| `Live` | `Long` | `0.1775` | 354,610.00 USD | 0.00 USD | 433.81 USD | `-50.80%` | `2,444.00` |
| `Live` | `Long` | `0.1795` | 354,180.00 USD | 0.00 USD | 209.84 USD | `-50.24%` | `1,169.00` |
| `Live` | `Long` | `0.1905` | 353,970.00 USD | 0.00 USD | 3,810.00 USD | `-47.19%` | `20,000.00` |
| `Live` | `Long` | `0.1955` | 350,160.00 USD | 0.00 USD | 275.85 USD | `-45.81%` | `1,411.00` |
| `Live` | `Long` | `0.1995` | 349,880.00 USD | 0.00 USD | 638.40 USD | `-44.70%` | `3,200.00` |
| `Live` | `Long` | `0.2005` | 349,240.00 USD | 0.00 USD | 1,210.00 USD | `-44.42%` | `6,059.00` |
| `Live` | `Long` | `0.2055` | 348,030.00 USD | 0.00 USD | 185.77 USD | `-43.03%` | `904.00` |
| `Live` | `Long` | `0.2115` | 347,840.00 USD | 0.00 USD | 221.02 USD | `-41.37%` | `1,045.00` |
| `Live` | `Long` | `0.2175` | 347,620.00 USD | 0.00 USD | 1,740.00 USD | `-39.71%` | `8,005.00` |
| `Live` | `Long` | `0.2185` | 345,880.00 USD | 0.00 USD | 1,530.00 USD | `-39.43%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 344,350.00 USD | 0.00 USD | 515.17 USD | `-39.15%` | `2,347.00` |
| `Live` | `Long` | `0.2225` | 343,830.00 USD | 0.00 USD | 2,350.00 USD | `-38.32%` | `10,560.00` |
| `Live` | `Long` | `0.2255` | 341,480.00 USD | 0.00 USD | 4,590.00 USD | `-37.49%` | `20,360.00` |
| `Live` | `Long` | `0.2305` | 336,890.00 USD | 0.00 USD | 2,080.00 USD | `-36.10%` | `9,004.00` |
| `Live` | `Long` | `0.2315` | 334,820.00 USD | 0.00 USD | 2,380.00 USD | `-35.83%` | `10,282.00` |
| `Live` | `Long` | `0.2325` | 332,440.00 USD | 0.00 USD | 308.30 USD | `-35.55%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 332,130.00 USD | 0.00 USD | 1,980.00 USD | `-35.27%` | `8,488.00` |
| `Live` | `Long` | `0.2345` | 330,150.00 USD | 0.00 USD | 729.53 USD | `-34.99%` | `3,111.00` |
| `Live` | `Long` | `0.2355` | 329,420.00 USD | 0.00 USD | 6,140.00 USD | `-34.72%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 323,280.00 USD | 0.00 USD | 8,970.00 USD | `-34.44%` | `37,937.00` |
| `Live` | `Long` | `0.2375` | 314,300.00 USD | 0.00 USD | 345.56 USD | `-34.16%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 313,960.00 USD | 0.00 USD | 1,480.00 USD | `-33.89%` | `6,215.00` |
| `Live` | `Long` | `0.2405` | 312,480.00 USD | 0.00 USD | 174.12 USD | `-33.33%` | `724.00` |
| `Live` | `Long` | `0.2425` | 312,300.00 USD | 0.00 USD | 139.92 USD | `-32.78%` | `577.00` |
| `Live` | `Long` | `0.2445` | 312,160.00 USD | 0.00 USD | 889.49 USD | `-32.22%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 311,270.00 USD | 0.00 USD | 6,400.00 USD | `-31.95%` | `26,056.00` |
| `Live` | `Long` | `0.2465` | 304,880.00 USD | 0.00 USD | 276.57 USD | `-31.67%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 304,600.00 USD | 0.00 USD | 2,590.00 USD | `-31.39%` | `10,478.00` |
| `Live` | `Long` | `0.2565` | 302,010.00 USD | 0.00 USD | 1,230.00 USD | `-28.90%` | `4,794.00` |
| `Live` | `Long` | `0.2605` | 300,780.00 USD | 0.00 USD | 2,330.00 USD | `-27.79%` | `8,947.00` |
| `Live` | `Long` | `0.2635` | 298,450.00 USD | 0.00 USD | 108.56 USD | `-26.96%` | `412.00` |
| `Live` | `Long` | `0.2655` | 298,340.00 USD | 0.00 USD | 7,830.00 USD | `-26.40%` | `29,497.00` |
| `Live` | `Long` | `0.2665` | 290,510.00 USD | 0.00 USD | 450.92 USD | `-26.12%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 290,050.00 USD | 0.00 USD | 194.47 USD | `-25.85%` | `727.00` |
| `Live` | `Long` | `0.2685` | 289,860.00 USD | 0.00 USD | 322.74 USD | `-25.57%` | `1,202.00` |
| `Live` | `Long` | `0.2725` | 289,540.00 USD | 0.00 USD | 412.84 USD | `-24.46%` | `1,515.00` |
| `Live` | `Long` | `0.2755` | 289,120.00 USD | 0.00 USD | 108,910.00 USD | `-23.63%` | `395,301.00` |
| `Live` | `Long` | `0.2775` | 180,220.00 USD | 0.00 USD | 5,580.00 USD | `-23.07%` | `20,120.00` |
| `Live` | `Long` | `0.2785` | 174,640.00 USD | 0.00 USD | 182.70 USD | `-22.80%` | `656.00` |
| `Live` | `Long` | `0.2795` | 174,450.00 USD | 0.00 USD | 12,870.00 USD | `-22.52%` | `46,044.00` |
| `Live` | `Long` | `0.2805` | 161,580.00 USD | 0.00 USD | 6,280.00 USD | `-22.24%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 155,310.00 USD | 0.00 USD | 1,120.00 USD | `-21.97%` | `3,982.00` |
| `Live` | `Long` | `0.2825` | 154,190.00 USD | 0.00 USD | 15,060.00 USD | `-21.69%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 139,120.00 USD | 0.00 USD | 1,430.00 USD | `-21.41%` | `5,038.00` |
| `Live` | `Long` | `0.2855` | 137,690.00 USD | 0.00 USD | 445.95 USD | `-20.86%` | `1,562.00` |
| `Live` | `Long` | `0.2865` | 137,250.00 USD | 0.00 USD | 360.42 USD | `-20.58%` | `1,258.00` |
| `Live` | `Long` | `0.2875` | 136,890.00 USD | 0.00 USD | 35,560.00 USD | `-20.30%` | `123,681.00` |
| `Live` | `Long` | `0.2915` | 101,330.00 USD | 0.00 USD | 591.45 USD | `-19.19%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 100,740.00 USD | 0.00 USD | 957.64 USD | `-18.92%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 99,780.00 USD | 0.00 USD | 3,760.00 USD | `-18.36%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 96,020.00 USD | 0.00 USD | 125.29 USD | `-18.09%` | `424.00` |
| `Live` | `Long` | `0.2965` | 95,890.00 USD | 0.00 USD | 1,710.00 USD | `-17.81%` | `5,767.00` |
| `Live` | `Long` | `0.2995` | 94,180.00 USD | 0.00 USD | 127.89 USD | `-16.98%` | `427.00` |
| `Live` | `Long` | `0.3005` | 94,050.00 USD | 0.00 USD | 5,200.00 USD | `-16.70%` | `17,292.00` |
| `Live` | `Long` | `0.3015` | 88,860.00 USD | 0.00 USD | 10,330.00 USD | `-16.42%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 78,530.00 USD | 0.00 USD | 694.54 USD | `-16.14%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 77,840.00 USD | 0.00 USD | 589.40 USD | `-15.87%` | `1,942.00` |
| `Live` | `Long` | `0.3055` | 77,250.00 USD | 0.00 USD | 138.70 USD | `-15.31%` | `454.00` |
| `Live` | `Long` | `0.3065` | 77,110.00 USD | 0.00 USD | 15,050.00 USD | `-15.04%` | `49,111.00` |
| `Live` | `Long` | `0.3085` | 62,060.00 USD | 0.00 USD | 6,670.00 USD | `-14.48%` | `21,612.00` |
| `Live` | `Long` | `0.3095` | 55,390.00 USD | 0.00 USD | 292.48 USD | `-14.20%` | `945.00` |
| `Live` | `Long` | `0.3105` | 55,100.00 USD | 0.00 USD | 668.82 USD | `-13.93%` | `2,154.00` |
| `Live` | `Long` | `0.3115` | 54,430.00 USD | 0.00 USD | 138.31 USD | `-13.65%` | `444.00` |
| `Live` | `Long` | `0.3125` | 54,290.00 USD | 0.00 USD | 14,170.00 USD | `-13.37%` | `45,342.00` |
| `Live` | `Long` | `0.3135` | 40,120.00 USD | 0.00 USD | 25,410.00 USD | `-13.10%` | `81,045.00` |
| `Live` | `Long` | `0.3145` | 14,710.00 USD | 0.00 USD | 541.88 USD | `-12.82%` | `1,723.00` |
| `Live` | `Long` | `0.3155` | 14,170.00 USD | 0.00 USD | 142.29 USD | `-12.54%` | `451.00` |
| `Live` | `Long` | `0.3165` | 14,030.00 USD | 0.00 USD | 1,490.00 USD | `-12.26%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,530.00 USD | 0.00 USD | 938.85 USD | `-11.99%` | `2,957.00` |
| `Live` | `Long` | `0.3235` | 11,590.00 USD | 0.00 USD | 11,000.00 USD | `-10.32%` | `34,003.00` |
| `Live` | `Long` | `0.3255` | 594.16 USD | 0.00 USD | 129.22 USD | `-9.77%` | `397.00` |
| `Live` | `Long` | `0.3265` | 464.94 USD | 0.00 USD | 464.94 USD | `-9.49%` | `1,424.00` |
| `Live` | `Short` | `0.3385` | 511.81 USD | 511.81 USD | 0.00 USD | `-6.17%` | `1,512.00` |
| `Live` | `Short` | `0.3395` | 13,340.00 USD | 12,820.00 USD | 0.00 USD | `-5.89%` | `37,776.00` |
| `Live` | `Short` | `0.3415` | 13,420.00 USD | 86.06 USD | 0.00 USD | `-5.33%` | `252.00` |
| `Live` | `Short` | `0.3535` | 15,350.00 USD | 1,930.00 USD | 0.00 USD | `-2.01%` | `5,455.00` |
| `Live` | `Short` | `0.3665` | 15,420.00 USD | 68.54 USD | 0.00 USD | `+1.60%` | `187.00` |
| `Live` | `Short` | `0.3715` | 15,710.00 USD | 289.77 USD | 0.00 USD | `+2.98%` | `780.00` |
| `Live` | `Short` | `0.3745` | 31,340.00 USD | 15,630.00 USD | 0.00 USD | `+3.81%` | `41,741.00` |
| `Live` | `Short` | `0.3755` | 86,400.00 USD | 55,050.00 USD | 0.00 USD | `+4.09%` | `146,614.00` |
| `Live` | `Short` | `0.3765` | 121,170.00 USD | 34,780.00 USD | 0.00 USD | `+4.37%` | `92,368.00` |
| `Live` | `Short` | `0.3785` | 121,860.00 USD | 685.46 USD | 0.00 USD | `+4.92%` | `1,811.00` |
| `Live` | `Short` | `0.3795` | 679,750.00 USD | 557,900.00 USD | 0.00 USD | `+5.20%` | `1,470,083.00` |
| `Live` | `Short` | `0.3805` | 680,080.00 USD | 323.43 USD | 0.00 USD | `+5.48%` | `850.00` |
| `Live` | `Short` | `0.3835` | 680,740.00 USD | 665.37 USD | 0.00 USD | `+6.31%` | `1,735.00` |
| `Live` | `Short` | `0.3845` | 680,860.00 USD | 115.35 USD | 0.00 USD | `+6.59%` | `300.00` |
| `Live` | `Short` | `0.3905` | 685,630.00 USD | 4,770.00 USD | 0.00 USD | `+8.25%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 686,110.00 USD | 487.42 USD | 0.00 USD | `+8.53%` | `1,245.00` |
| `Live` | `Short` | `0.3925` | 707,970.00 USD | 21,850.00 USD | 0.00 USD | `+8.80%` | `55,678.00` |
| `Live` | `Short` | `0.3945` | 1,480,000.00 USD | 776,680.00 USD | 0.00 USD | `+9.36%` | `1,968,770.00` |
| `Live` | `Short` | `0.3955` | 1,600,000.00 USD | 118,430.00 USD | 0.00 USD | `+9.64%` | `299,436.00` |
| `Live` | `Short` | `0.3965` | 1,600,000.00 USD | 111.42 USD | 0.00 USD | `+9.91%` | `281.00` |
| `Live` | `Short` | `0.3975` | 1,600,000.00 USD | 502.84 USD | 0.00 USD | `+10.19%` | `1,265.00` |
| `Live` | `Short` | `0.4095` | 1,610,000.00 USD | 5,150.00 USD | 0.00 USD | `+13.52%` | `12,580.00` |
| `Live` | `Short` | `0.4115` | 1,610,000.00 USD | 6,020.00 USD | 0.00 USD | `+14.07%` | `14,632.00` |
| `Live` | `Short` | `0.4205` | 1,620,000.00 USD | 1,010.00 USD | 0.00 USD | `+16.57%` | `2,408.00` |
| `Live` | `Short` | `0.4245` | 1,620,000.00 USD | 2,950.00 USD | 0.00 USD | `+17.67%` | `6,956.00` |
| `Live` | `Short` | `0.4305` | 1,620,000.00 USD | 203.20 USD | 0.00 USD | `+19.34%` | `472.00` |
| `Live` | `Short` | `0.4365` | 1,690,000.00 USD | 67,500.00 USD | 0.00 USD | `+21.00%` | `154,638.00` |
| `Live` | `Short` | `0.4375` | 1,690,000.00 USD | 183.31 USD | 0.00 USD | `+21.28%` | `419.00` |
| `Live` | `Short` | `0.4385` | 1,720,000.00 USD | 29,420.00 USD | 0.00 USD | `+21.56%` | `67,091.00` |
| `Live` | `Short` | `0.4395` | 1,790,000.00 USD | 71,540.00 USD | 0.00 USD | `+21.83%` | `162,775.00` |
| `Live` | `Short` | `0.4435` | 2,420,000.00 USD | 635,130.00 USD | 0.00 USD | `+22.94%` | `1,432,082.00` |
| `Live` | `Short` | `0.4475` | 2,420,000.00 USD | 1,020.00 USD | 0.00 USD | `+24.05%` | `2,284.00` |
| `Live` | `Short` | `0.4495` | 2,700,000.00 USD | 272,040.00 USD | 0.00 USD | `+24.60%` | `605,203.00` |
| `Live` | `Short` | `0.4705` | 2,700,000.00 USD | 103.98 USD | 0.00 USD | `+30.43%` | `221.00` |
| `Live` | `Short` | `0.4905` | 2,700,000.00 USD | 841.21 USD | 0.00 USD | `+35.97%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 2,700,000.00 USD | 5,130.00 USD | 0.00 USD | `+36.25%` | `10,430.00` |
| `Live` | `Short` | `0.5215` | 2,700,000.00 USD | 1,720.00 USD | 0.00 USD | `+44.56%` | `3,303.00` |
| `Live` | `Short` | `0.5295` | 2,720,000.00 USD | 12,150.00 USD | 0.00 USD | `+46.78%` | `22,943.00` |
| `Live` | `Short` | `0.5305` | 3,360,000.00 USD | 644,210.00 USD | 0.00 USD | `+47.06%` | `1,214,339.00` |
| `Live` | `Short` | `0.5345` | 3,360,000.00 USD | 669.73 USD | 0.00 USD | `+48.17%` | `1,253.00` |
| `Live` | `Short` | `0.5585` | 3,360,000.00 USD | 742.25 USD | 0.00 USD | `+54.82%` | `1,329.00` |
| `Live` | `Short` | `0.5605` | 3,370,000.00 USD | 8,270.00 USD | 0.00 USD | `+55.38%` | `14,763.00` |
| `Live` | `Short` | `0.5615` | 4,100,000.00 USD | 728,400.00 USD | 0.00 USD | `+55.65%` | `1,297,248.00` |
| `Live` | `Short` | `0.5625` | 4,100,000.00 USD | 140.62 USD | 0.00 USD | `+55.93%` | `250.00` |
| `Live` | `Short` | `0.6145` | 4,140,000.00 USD | 36,870.00 USD | 0.00 USD | `+70.34%` | `60,000.00` |
| `Live` | `Short` | `0.6165` | 4,160,000.00 USD | 24,660.00 USD | 0.00 USD | `+70.90%` | `40,000.00` |
| `Live` | `Short` | `0.6275` | 4,160,000.00 USD | 275.47 USD | 0.00 USD | `+73.95%` | `439.00` |
| `Live` | `Short` | `0.6285` | 4,170,000.00 USD | 7,390.00 USD | 0.00 USD | `+74.23%` | `11,753.00` |
| `Live` | `Short` | `0.6355` | 4,170,000.00 USD | 6,350.00 USD | 0.00 USD | `+76.17%` | `10,000.00` |
| `Live` | `Short` | `0.6525` | 4,170,000.00 USD | 242.08 USD | 0.00 USD | `+80.88%` | `371.00` |
| `Live` | `Short` | `0.6645` | 4,200,000.00 USD | 27,950.00 USD | 0.00 USD | `+84.20%` | `42,059.00` |
| `Live` | `Short` | `0.6745` | 4,290,000.00 USD | 83,190.00 USD | 0.00 USD | `+86.98%` | `123,332.00` |
| `Live` | `Short` | `0.6935` | 4,290,000.00 USD | 414.71 USD | 0.00 USD | `+92.24%` | `598.00` |
| `Live` | `Short` | `0.7015` | 4,290,000.00 USD | 106.63 USD | 0.00 USD | `+94.46%` | `152.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 1,200,000.00 USD | 0.00 USD | 6,100.00 USD | `-49.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,200,000.00 USD | 0.00 USD | 1,750.00 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,190,000.00 USD | 0.00 USD | 579.72 USD | `-41.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,190,000.00 USD | 0.00 USD | 121.70 USD | `-36.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,190,000.00 USD | 0.00 USD | 705.61 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,190,000.00 USD | 0.00 USD | 1,200.00 USD | `-33.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,190,000.00 USD | 0.00 USD | 127.51 USD | `-33.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,190,000.00 USD | 0.00 USD | 1,850.00 USD | `-30.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 1,190,000.00 USD | 0.00 USD | 1,920.00 USD | `-28.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 1,190,000.00 USD | 0.00 USD | 664.01 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 1,190,000.00 USD | 0.00 USD | 954.98 USD | `-27.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 1,190,000.00 USD | 0.00 USD | 695.50 USD | `-25.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 1,190,000.00 USD | 0.00 USD | 1,630.00 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 1,180,000.00 USD | 0.00 USD | 2,550.00 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 1,180,000.00 USD | 0.00 USD | 229.92 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 1,180,000.00 USD | 0.00 USD | 11,610.00 USD | `-18.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 1,170,000.00 USD | 0.00 USD | 111.19 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 1,170,000.00 USD | 0.00 USD | 326.86 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 1,170,000.00 USD | 0.00 USD | 2,710.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 1,170,000.00 USD | 0.00 USD | 335.56 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 1,170,000.00 USD | 0.00 USD | 919.50 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 1,170,000.00 USD | 0.00 USD | 193.11 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 1,160,000.00 USD | 0.00 USD | 15,150.00 USD | `-14.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 1,150,000.00 USD | 0.00 USD | 147.32 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 1,150,000.00 USD | 0.00 USD | 20,580.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 1,130,000.00 USD | 0.00 USD | 6,530.00 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 1,120,000.00 USD | 0.00 USD | 524,570.00 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 597,860.00 USD | 0.00 USD | 1,270.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 596,590.00 USD | 0.00 USD | 25,720.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 570,880.00 USD | 0.00 USD | 1,250.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 569,630.00 USD | 0.00 USD | 6,100.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 563,530.00 USD | 0.00 USD | 1,040.00 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 562,490.00 USD | 0.00 USD | 9,160.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 553,330.00 USD | 0.00 USD | 9,980.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 543,350.00 USD | 0.00 USD | 55,430.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 487,920.00 USD | 0.00 USD | 131.90 USD | `-10.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 487,790.00 USD | 0.00 USD | 166.60 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 487,620.00 USD | 0.00 USD | 3,680.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 483,940.00 USD | 0.00 USD | 5,440.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 478,500.00 USD | 0.00 USD | 23,220.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 455,280.00 USD | 0.00 USD | 2,670.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 452,610.00 USD | 0.00 USD | 1,320.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 451,290.00 USD | 0.00 USD | 51,610.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 399,680.00 USD | 0.00 USD | 3,270.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 396,410.00 USD | 0.00 USD | 100.11 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 396,310.00 USD | 0.00 USD | 135.99 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 396,180.00 USD | 0.00 USD | 106.39 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 396,070.00 USD | 0.00 USD | 5,030.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 391,050.00 USD | 0.00 USD | 174,860.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 216,180.00 USD | 0.00 USD | 49,750.00 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 166,440.00 USD | 0.00 USD | 139.73 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 166,300.00 USD | 0.00 USD | 11,640.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 154,650.00 USD | 0.00 USD | 102.87 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 154,550.00 USD | 0.00 USD | 3,090.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 151,460.00 USD | 0.00 USD | 2,520.00 USD | `-5.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 148,950.00 USD | 0.00 USD | 5,520.00 USD | `-5.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 143,420.00 USD | 0.00 USD | 7,610.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 135,810.00 USD | 0.00 USD | 18,620.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 117,190.00 USD | 0.00 USD | 2,870.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 114,320.00 USD | 0.00 USD | 7,930.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 106,390.00 USD | 0.00 USD | 2,450.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3485` | 103,930.00 USD | 0.00 USD | 4,380.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3495` | 99,550.00 USD | 0.00 USD | 7,750.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 91,790.00 USD | 0.00 USD | 18,580.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3525` | 73,220.00 USD | 0.00 USD | 19,380.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3535` | 53,830.00 USD | 0.00 USD | 1,350.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3545` | 52,480.00 USD | 0.00 USD | 769.97 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3555` | 51,710.00 USD | 0.00 USD | 1,190.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3565` | 50,530.00 USD | 0.00 USD | 13,990.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3575` | 36,540.00 USD | 0.00 USD | 122.62 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3585` | 36,410.00 USD | 0.00 USD | 29,750.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3595` | 6,670.00 USD | 0.00 USD | 6,180.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3605` | 485.59 USD | 0.00 USD | 485.59 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 390.40 USD | 390.40 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 824.25 USD | 433.85 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 1,150.00 USD | 326.19 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 5,770.00 USD | 4,620.00 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 6,260.00 USD | 481.83 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 6,570.00 USD | 310.11 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 6,670.00 USD | 107.28 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 7,390.00 USD | 720.96 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 23,420.00 USD | 16,020.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 23,690.00 USD | 275.17 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 24,150.00 USD | 463.37 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 24,380.00 USD | 222.21 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 24,490.00 USD | 114.83 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 24,720.00 USD | 224.73 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 25,340.00 USD | 621.04 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 26,490.00 USD | 1,150.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 26,840.00 USD | 352.11 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 29,250.00 USD | 2,400.00 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 30,090.00 USD | 847.87 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 31,290.00 USD | 1,200.00 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 84,170.00 USD | 52,880.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 86,570.00 USD | 2,400.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 87,770.00 USD | 1,200.00 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 88,970.00 USD | 1,200.00 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 90,170.00 USD | 1,200.00 USD | 0.00 USD | `+12.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 90,310.00 USD | 138.07 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 90,870.00 USD | 564.43 USD | 0.00 USD | `+14.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 91,060.00 USD | 186.70 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 91,380.00 USD | 325.75 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 91,680.00 USD | 299.19 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 130,260.00 USD | 38,580.00 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 130,430.00 USD | 170.69 USD | 0.00 USD | `+23.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 131,820.00 USD | 1,390.00 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 142,970.00 USD | 11,150.00 USD | 0.00 USD | `+38.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 143,210.00 USD | 240.85 USD | 0.00 USD | `+74.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 156,820.00 USD | 13,610.00 USD | 0.00 USD | `+87.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.2959` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.2965` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 14,230.00 USD | 6,710.00 USD | 11,630.00 USD |
| `1D` | `0.2971` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 18,240.00 USD | 7,030.00 USD | 16,250.00 USD |
| `1D` | `0.2977` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 17,630.00 USD | 6,840.00 USD | 7,910.00 USD |
| `7D` | `0.2979` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 109,110.00 USD | 18,870.00 USD | 33,390.00 USD |
| `7D` | `0.2983` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD |
| `7D` | `0.2987` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `1D` | `0.2989` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 55,860.00 USD | 8,480.00 USD | 12,730.00 USD |
| `7D` | `0.2991` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `1D` | `0.2995` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3007` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD |
| `1D` | `0.3019` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3031` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD |
| `1D` | `0.3049` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3051` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3055` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD |
| `7D` | `0.3063` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 14,650,000.00 USD | 0.00 USD | 14,650,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3073` | 14,560,000.00 USD | 0.00 USD | 14,560,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3085` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3103` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3107` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3133` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 164.40 USD | 0.00 USD | 21,520.00 USD |
| `7D` | `0.3135` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3145` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD |
| `1D` | `0.3151` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD |
| `1D` | `0.3157` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 69,350.00 USD | 21,820.00 USD | 28,250.00 USD |
| `7D` | `0.3163` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `7D` | `0.3167` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3169` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 85,970.00 USD | 18,430.00 USD | 39,440.00 USD |
| `7D` | `0.3171` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 21,570.00 USD | 18,720.00 USD | 14,330.00 USD |
| `7D` | `0.3175` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `7D` | `0.3179` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3181` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD |
| `7D` | `0.3183` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD |
| `1D` | `0.3187` | 13,470,000.00 USD | 0.00 USD | 13,470,000.00 USD | 182,020.00 USD | 22,910.00 USD | 34,760.00 USD |
| `7D` | `0.3187` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `1D` | `0.3193` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `1D` | `0.3199` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3205` | 13,180,000.00 USD | 0.00 USD | 13,180,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD |
| `7D` | `0.3207` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `1D` | `0.3211` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD |
| `7D` | `0.3211` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `1D` | `0.3217` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3219` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3223` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD |
| `7D` | `0.3223` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3229` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 139,110.00 USD | 81,070.00 USD | 205,050.00 USD |
| `7D` | `0.3231` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 135,730.00 USD | 82,220.00 USD | 170,820.00 USD |
| `7D` | `0.3235` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `7D` | `0.3239` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3241` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD |
| `7D` | `0.3243` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 11,320,000.00 USD | 0.00 USD | 11,320,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD |
| `7D` | `0.3247` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `7D` | `0.3251` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3253` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `1D` | `0.3259` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3265` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD |
| `1D` | `0.3271` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD |
| `1D` | `0.3277` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3283` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD |
| `1D` | `0.3289` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3295` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.3307` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD |
| `1D` | `0.3313` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 234,580.00 USD | 121,210.00 USD | 329,260.00 USD |
| `7D` | `0.3315` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3319` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 158,550.00 USD | 32,400.00 USD | 295,390.00 USD |
| `1D` | `0.3325` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD |
| `1D` | `0.3331` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3337` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `1D` | `0.3343` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 76,100.00 USD | 31,390.00 USD | 0.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `1D` | `0.3349` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD |
| `7D` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3355` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `7D` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3361` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 177,350.00 USD | 0.00 USD | 65,250.00 USD |
| `7D` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 240,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `7D` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3373` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 514,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `7D` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3385` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 178,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3403` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD |
| `7D` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `1D` | `0.3409` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD |
| `7D` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `1D` | `0.3415` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 627,050.00 USD | 0.00 USD | 62,690.00 USD |
| `7D` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD |
| `7D` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3421` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD |
| `7D` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 262,640.00 USD | 18,020.00 USD | 187,820.00 USD |
| `7D` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `7D` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3433` | 950,750.00 USD | 0.00 USD | 950,750.00 USD | 0.00 USD | 44,190.00 USD | 176,350.00 USD |
| `7D` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 730,200.00 USD | 0.00 USD | 730,200.00 USD | 0.00 USD | 48,730.00 USD | 392,630.00 USD |
| `7D` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `7D` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3445` | 288,840.00 USD | 0.00 USD | 288,840.00 USD | 0.00 USD | 71,810.00 USD | 217,030.00 USD |
| `7D` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD |
| `1D` | `0.3448` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3451` | 229,860.00 USD | 229,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 229,860.00 USD |
| `7D` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `7D` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3457` | 489,740.00 USD | 489,740.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD |
| `7D` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3469` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD |
| `7D` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD |
| `7D` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3487` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD |
| `7D` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3499` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD |
| `7D` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3505` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD |
| `7D` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD |
| `7D` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3517` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 221,620.00 USD | 117,900.00 USD | 434,060.00 USD |
| `7D` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 279,270.00 USD | 459,710.00 USD |
| `7D` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD |
| `7D` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3541` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 704,710.00 USD |
| `1D` | `0.3547` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 101,320.00 USD | 534,120.00 USD |
| `1D` | `0.3553` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 128,410.00 USD | 0.00 USD |
| `1D` | `0.3559` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD |
| `1D` | `0.3571` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 1,770.00 USD | 161,260.00 USD | 578,320.00 USD |
| `1D` | `0.3577` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3583` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 110,810.00 USD | 0.00 USD | 268,150.00 USD |
| `1D` | `0.3589` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 1,810.00 USD | 0.00 USD | 400,320.00 USD |
| `1D` | `0.3595` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 199,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `1D` | `0.3613` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 50,660.00 USD | 0.00 USD |
| `7D` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 31,390.00 USD | 0.00 USD |
| `7D` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `7D` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD |
| `7D` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `7D` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3637` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 98,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 1,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD |
| `7D` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `1D` | `0.3649` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 194,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |
| `1D` | `0.3655` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 186,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3661` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 259,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3667` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 341,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3673` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 5,540.00 USD | 48,350.00 USD | 0.00 USD |
| `1D` | `0.3679` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD |
| `1D` | `0.3685` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 326,450.00 USD | 141,810.00 USD | 0.00 USD |
| `1D` | `0.3691` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD |
| `1D` | `0.3697` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD |
| `1D` | `0.3703` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD |
| `1D` | `0.3709` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD |
| `1D` | `0.3715` | 16,220,000.00 USD | 16,220,000.00 USD | 0.00 USD | 438,840.00 USD | 62,210.00 USD | 969,570.00 USD |
| `1D` | `0.3721` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD |
| `1D` | `0.3727` | 17,580,000.00 USD | 17,580,000.00 USD | 0.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD |
| `1D` | `0.3733` | 18,450,000.00 USD | 18,450,000.00 USD | 0.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD |
| `1D` | `0.3739` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD |
| `1D` | `0.3745` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD |
| `1D` | `0.3751` | 20,160,000.00 USD | 20,160,000.00 USD | 0.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD |
| `1D` | `0.3757` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD |
| `1D` | `0.3763` | 21,680,000.00 USD | 21,680,000.00 USD | 0.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD |
| `1D` | `0.3769` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD |
| `1D` | `0.3775` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3781` | 22,040,000.00 USD | 22,040,000.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD |
| `1D` | `0.3787` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD |
| `1D` | `0.3793` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD |
| `1D` | `0.3799` | 22,750,000.00 USD | 22,750,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3805` | 23,080,000.00 USD | 23,080,000.00 USD | 0.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD |
| `1D` | `0.3823` | 23,350,000.00 USD | 23,350,000.00 USD | 0.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD |
| `1D` | `0.3829` | 23,350,000.00 USD | 23,350,000.00 USD | 0.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3835` | 23,570,000.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 23,570,000.00 USD | 23,570,000.00 USD | 0.00 USD | 850.22 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3847` | 23,570,000.00 USD | 23,570,000.00 USD | 0.00 USD | 899.18 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3871` | 23,610,000.00 USD | 23,610,000.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3883` | 23,610,000.00 USD | 23,610,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3907` | 23,660,000.00 USD | 23,660,000.00 USD | 0.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3913` | 23,830,000.00 USD | 23,830,000.00 USD | 0.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3919` | 23,900,000.00 USD | 23,900,000.00 USD | 0.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3925` | 23,980,000.00 USD | 23,980,000.00 USD | 0.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD |
| `1D` | `0.3931` | 24,060,000.00 USD | 24,060,000.00 USD | 0.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `1D` | `0.3937` | 24,140,000.00 USD | 24,140,000.00 USD | 0.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.3943` | 24,350,000.00 USD | 24,350,000.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD |
| `1D` | `0.3949` | 24,480,000.00 USD | 24,480,000.00 USD | 0.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD |
| `1D` | `0.3955` | 24,680,000.00 USD | 24,680,000.00 USD | 0.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD |
| `1D` | `0.3961` | 24,780,000.00 USD | 24,780,000.00 USD | 0.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD |
| `1D` | `0.3967` | 24,880,000.00 USD | 24,880,000.00 USD | 0.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD |
| `1D` | `0.3973` | 25,040,000.00 USD | 25,040,000.00 USD | 0.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD |
| `1D` | `0.3979` | 25,440,000.00 USD | 25,440,000.00 USD | 0.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD |
| `1D` | `0.3985` | 25,450,000.00 USD | 25,450,000.00 USD | 0.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD |
| `1D` | `0.3991` | 25,480,000.00 USD | 25,480,000.00 USD | 0.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `1D` | `0.3997` | 25,570,000.00 USD | 25,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD |
| `1D` | `0.4003` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD |
| `1D` | `0.4009` | 25,830,000.00 USD | 25,830,000.00 USD | 0.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD |
| `1D` | `0.4027` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.4045` | 25,990,000.00 USD | 25,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD |
| `1D` | `0.4057` | 26,100,000.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 8,920.00 USD | 97,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `393.06M` | Total OI Tokens: `1,131,596,864.7 TRX`
  * 1h OI Change: `+20.66%` | 4h OI Change: `+31.86%` | 24h OI Change: `+35.10%`
  * Exchange Breakdown: Binance=`116.46M` | Bybit=`84.01M` | OKX=`21.34M` | Hyperliquid=`16.88M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-433.94K` | Last 24h: `9.22K` | Last 3d: `-51.81K` | Last 7d: `-271.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.1615%` | **USDT OKX** | `-0.6327%` |
| **USDT Bybit** | `-0.1300%` | **USDT KuCoin** | `-0.3460%` |
| **USDT MEXC** | `-0.1585%` | **USDT BingX** | `-0.4892%` |
| **USDT Gate** | `-0.3449%` | **USDT Bitget** | `-0.2136%` |
| **CoinM Binance** | `-0.0828%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `53.70%` | `46.30%` | `1.16` | 25,810,000.00 USD |
| `15M` | `Binance` | `47.7%` | `52.3%` | `0.91` | 9,600,000.00 USD |
| `15M` | `OKX` | `64.1%` | `35.9%` | `1.79` | 5,270,000.00 USD |
| `15M` | `Bybit` | `50.59%` | `49.41%` | `1.02` | 2,070,000.00 USD |
| `15M` | `KuCoin` | `56.64%` | `43.36%` | `1.31` | 395,690.00 USD |
| `15M` | `Gate` | `48.76%` | `51.24%` | `0.95` | 3,670,000.00 USD |
| `15M` | `Bitget` | `47.48%` | `52.52%` | `0.90` | 610,660.00 USD |
| `15M` | `BingX` | `51.78%` | `48.22%` | `1.07` | 116,100.00 USD |
| `15M` | `MEXC` | `65.14%` | `34.86%` | `1.87` | 2,360,000.00 USD |
| `15M` | `Bitunix` | `52.47%` | `47.53%` | `1.10` | 556,460.00 USD |
| `15M` | `Hyperliquid` | `45.32%` | `54.68%` | `0.83` | 128,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `67.53%` | `32.47%` | `2.08` | 91,300.00 USD |
| `15M` | `Crypto.com` | `44.7%` | `55.3%` | `0.81` | 15,550.00 USD |
| `15M` | `WhiteBIT` | `34.52%` | `65.48%` | `0.53` | 379,780.00 USD |
| `15M` | `HTX` | `83.8%` | `16.2%` | `5.17` | 155,940.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.12%` | `57.88%` | `0.73` | 147,180.00 USD |
| `15M` | `Aster` | `91.2%` | `8.8%` | `10.36` | 216,430.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `33.18%` | `66.82%` | `0.50` | 4,290.00 USD |
| `15M` | `Whale Positions` | `47.7%` | `52.3%` | `0.91` | 9,600,000.00 USD |
| `15M` | `Global Accounts` | `53.70%` | `46.30%` | `1.16` | 25,810,000.00 USD |
| `1H` | `TRX` | `44.68%` | `55.32%` | `0.81` | 53,720,000.00 USD |
| `1H` | `Binance` | `50.28%` | `49.72%` | `1.01` | 15,570,000.00 USD |
| `1H` | `OKX` | `49.66%` | `50.34%` | `0.99` | 3,680,000.00 USD |
| `1H` | `Bybit` | `53.44%` | `46.56%` | `1.15` | 4,790,000.00 USD |
| `1H` | `KuCoin` | `42.27%` | `57.73%` | `0.73` | 498,740.00 USD |
| `1H` | `Gate` | `51.97%` | `48.03%` | `1.08` | 2,060,000.00 USD |
| `1H` | `Bitget` | `47.12%` | `52.88%` | `0.89` | 1,400,000.00 USD |
| `1H` | `BingX` | `17.38%` | `82.62%` | `0.21` | 11,970,000.00 USD |
| `1H` | `MEXC` | `54.83%` | `45.17%` | `1.21` | 3,380,000.00 USD |
| `1H` | `Bitunix` | `48.53%` | `51.47%` | `0.94` | 875,060.00 USD |
| `1H` | `Hyperliquid` | `55.59%` | `44.41%` | `1.25` | 415,380.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.91%` | `45.09%` | `1.22` | 7,630,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `83.78%` | `16.22%` | `5.17` | 941,860.00 USD |
| `1H` | `HTX` | `52.26%` | `47.74%` | `1.09` | 109,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `56.12%` | `43.88%` | `1.28` | 379,640.00 USD |
| `1H` | `Aster` | `76.74%` | `23.26%` | `3.30` | 5,170.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `21.67%` | `78.33%` | `0.28` | 20,020.00 USD |
| `1H` | `Whale Positions` | `50.28%` | `49.72%` | `1.01` | 15,570,000.00 USD |
| `1H` | `Global Accounts` | `44.68%` | `55.32%` | `0.81` | 53,720,000.00 USD |
| `4H` | `TRX` | `47.61%` | `52.39%` | `0.91` | 662,930,000.00 USD |
| `4H` | `Binance` | `47.34%` | `52.66%` | `0.90` | 284,140,000.00 USD |
| `4H` | `OKX` | `48.76%` | `51.24%` | `0.95` | 144,740,000.00 USD |
| `4H` | `Bybit` | `45.52%` | `54.48%` | `0.84` | 62,870,000.00 USD |
| `4H` | `KuCoin` | `43.54%` | `56.46%` | `0.77` | 5,440,000.00 USD |
| `4H` | `Gate` | `48.77%` | `51.23%` | `0.95` | 52,330,000.00 USD |
| `4H` | `Bitget` | `39.63%` | `60.37%` | `0.66` | 18,940,000.00 USD |
| `4H` | `BingX` | `50.45%` | `49.55%` | `1.02` | 6,740,000.00 USD |
| `4H` | `MEXC` | `54.71%` | `45.29%` | `1.21` | 34,880,000.00 USD |
| `4H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 18,300,000.00 USD |
| `4H` | `Hyperliquid` | `48.6%` | `51.4%` | `0.95` | 6,440,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.77%` | `43.23%` | `1.31` | 2,630,000.00 USD |
| `4H` | `Crypto.com` | `50.79%` | `49.21%` | `1.03` | 820,230.00 USD |
| `4H` | `WhiteBIT` | `32.51%` | `67.49%` | `0.48` | 7,380,000.00 USD |
| `4H` | `HTX` | `45.9%` | `54.1%` | `0.85` | 5,540,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.18%` | `54.82%` | `0.82` | 2,920,000.00 USD |
| `4H` | `Aster` | `48.37%` | `51.63%` | `0.94` | 8,560,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.22%` | `48.78%` | `1.05` | 256,480.00 USD |
| `4H` | `Whale Positions` | `47.34%` | `52.66%` | `0.90` | 284,140,000.00 USD |
| `4H` | `Global Accounts` | `47.61%` | `52.39%` | `0.91` | 662,930,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3313` | `0.3314` | `0.3313` | `0.3315` | `0.3312` | 312,440.76 USD | 170,379.42 USD | 142,061.34 USD | 28,318.07 USD | `+9.06%` | `13B / 7S` |
| `0:00 UTC` | `0.3308` | `0.3304` | `0.3308` | `0.3313` | `0.3295` | 3,091,479.93 USD | 681,981.05 USD | 2,409,498.88 USD | -1,727,517.83 USD | `-55.88%` | `20B / 55S` |
| `5:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3363` | `0.3285` | 10,644,567.03 USD | 5,188,760.14 USD | 5,455,806.89 USD | -267,046.75 USD | `-2.51%` | `23B / 18S` |
| `0:00 UTC` | `0.3310` | `0.3345` | `0.3310` | `0.3414` | `0.3283` | 12,234,359.27 USD | 6,873,169.39 USD | 5,361,189.88 USD | 1,511,979.51 USD | `+12.36%` | `29B / 4S` |
| `5:00 UTC` | `0.3410` | `0.3437` | `0.3410` | `0.3496` | `0.3386` | 15,171,697.80 USD | 7,420,251.93 USD | 7,751,445.87 USD | -331,193.94 USD | `-2.18%` | `3B / 6S` |
| `0:00 UTC` | `0.3377` | `0.3416` | `0.3377` | `0.3499` | `0.3361` | 21,787,549.51 USD | 11,969,195.40 USD | 9,818,354.10 USD | 2,150,841.30 USD | `+9.87%` | `13B / 4S` |
| `5:00 UTC` | `0.3600` | `0.3572` | `0.3600` | `0.3651` | `0.3467` | 44,541,588.04 USD | 22,230,180.93 USD | 22,311,407.11 USD | -81,226.19 USD | `-0.18%` | `8B / 6S` |
| `0:00 UTC` | `0.3597` | `0.3554` | `0.3597` | `0.3654` | `0.3450` | 47,319,855.69 USD | 24,728,561.34 USD | 22,591,294.35 USD | 2,137,266.99 USD | `+4.52%` | `7B / 1S` |
| `5:00 UTC` | `0.3490` | `0.3506` | `0.3490` | `0.3575` | `0.3423` | 29,514,058.42 USD | 13,466,249.86 USD | 16,047,808.55 USD | -2,581,558.69 USD | `-8.75%` | `3B / 18S` |
| `0:00 UTC` | `0.3440` | `0.3430` | `0.3440` | `0.3446` | `0.3413` | 3,442,790.85 USD | 1,513,731.28 USD | 1,929,059.57 USD | -415,328.29 USD | `-12.06%` | `36B / 26S` |

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
| `5m` | 722,210.00 USD | -1,710,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 3,250,000.00 USD | -5,030,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 4,000,000.00 USD | -4,470,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 893,290.00 USD | -141,480.00 USD | **`ACCUMULATION`** |
| `2h` | -20,380.00 USD | 1,830,000.00 USD | **`ACCUMULATION`** |
| `4h` | -623,970.00 USD | 2,250,000.00 USD | **`ACCUMULATION`** |
| `6h` | -561,130.00 USD | 2,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | 753,840.00 USD | 2,360,000.00 USD | **`ACCUMULATION`** |
| `12h` | 489,410.00 USD | 2,670,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,850,000.00 USD | 5,070,000.00 USD | **`ACCUMULATION`** |
| `1w` | -3,980,000.00 USD | 3,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -22,930,000.00 USD | 5,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+722.21K` | 15m=`+3.25M` | 1h=`+893.29K` | 24h=`+2.85M`
* Futures Capital Netflows: 5m=`-1.71M` | 15m=`-5.03M` | 1h=`-141.48K` | 24h=`+5.07M`
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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3395` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.8669` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `3.36`
  * Mathematical Lot Sizing: **`8.28 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3566` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.56` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `-2.66`
  * Mathematical Lot Sizing: **`8.28 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3453`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
