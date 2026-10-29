# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 04:41:04 IST` (`2026-10-29 23:11:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3428` | **Live Ask Quote**: `0.3467` | **Mid Price**: `0.3448`
- **Spread Points**: `39.00` | **Spread BPS**: `113.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3403` | VWAP Z-Score: `+0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0067` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `59.38` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3685` | Lower -3.00σ Band: `0.3121`
  * Upper +2.51σ Band: `0.3639` | Lower -2.51σ Band: `0.3167`
  * Upper +2.01σ Band: `0.3592` | Lower -2.01σ Band: `0.3214`
  * Upper +2.00σ Band: `0.3591` | Lower -2.00σ Band: `0.3215`
  * Upper +1.28σ Band: `0.3523` | Lower -1.28σ Band: `0.3283`
  * Upper +1.00σ Band: `0.3497` | Lower -1.00σ Band: `0.3309`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3442` | EMA-20=`0.3393` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3348` (Slope: `+0.0000`) | EMA-100=`0.3327`
  * Institutional Anchors: EMA-144=`0.3319` | EMA-200=`0.3312` (Slope: `+0.3751`) | EMA-233=`0.3310`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3534` (Distance: `-2.49%`)
  * Point of Control (POC) = `0.3461` (Distance: `-0.43%`)
  * Value Area Low (VAL) = `0.3384` (Distance: `+1.85%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3336` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3461` | Low=`0.3434`
  * New York Session (13:00-21:00 UTC): High=`0.3468` | Low=`0.3427`
  * Initial Balance (First Hour): IB High=`0.3458` | IB Low=`0.3437`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3434` - `0.3461`
  * Optimal Trade Entry (OTE 0.705): `0.3454`
  * Structural Invalidation Anchor (0.786): `0.3475`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3490` | `0.3537` | `0.3477` | `0.3478` | `13,576,955` | 4,745,833.47 USD | -555,819.26 USD | `-11.71%` | 1,199,967.95 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3478` | `0.3506` | `0.3413` | `0.3426` | `20,214,044` | 6,977,489.78 USD | -479,222.28 USD | `-6.87%` | 720,745.67 USD | `-0.50` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3426` | `0.3447` | `0.3418` | `0.3446` | `3,086,420` | 1,057,965.49 USD | 74,160.10 USD | `+7.01%` | 794,905.77 USD | `+0.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3431` | `0.3537` | `0.3367` | `0.3530` | `71,878,276` | 24,778,361.80 USD | -1,078,098.11 USD | `-4.35%` | 1,677,378.88 USD | `-1.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3530` | `0.3565` | `0.3477` | `0.3478` | `50,798,827` | 17,864,049.59 USD | -501,690.24 USD | `-2.81%` | 1,175,688.65 USD | `-0.45` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3478` | `0.3506` | `0.3413` | `0.3446` | `23,300,464` | 8,035,455.28 USD | -405,062.18 USD | `-5.04%` | 770,626.47 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3295` | `0.3650` | `0.3282` | `0.3605` | `269,212,638` | 93,735,194.61 USD | 3,250,400.68 USD | `+3.47%` | 3,128,248.56 USD | `+3.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3605` | `0.3653` | `0.3367` | `0.3478` | `340,044,086` | 119,475,495.53 USD | -2,023,250.09 USD | `-1.69%` | 1,104,998.47 USD | `-2.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3478` | `0.3506` | `0.3413` | `0.3442` | `23,178,914` | 7,993,589.97 USD | -416,918.74 USD | `-5.22%` | 688,079.73 USD | `-0.43` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3443` | `677,056,540` | 235,998,166.69 USD | -1,155,761.31 USD | `-0.49%` | 689,464.41 USD | `-2.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,247,572.49 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 1,263,826.68 USD | `-1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3443` | `677,056,540` | 235,998,166.69 USD | -1,155,761.31 USD | `-0.49%` | 689,464.41 USD | `-2.09` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3448`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `776` | `0xecb6...2b00` | `LONG` | 2,928,290.27 USD | `8,562,753.00` | `0.3330` | `0.3433` | `0.000000` | 77,149.05 USD | `+2.63%` | `10X Cross` |
| `1558` | `0xeadc...9d55` | `LONG` | 1,396,600.00 USD | `4,000,000.00` | `0.3421` | `0.3433` | `0.000000` | 28,121.91 USD | `+2.01%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3301` | 7,523.39 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.52K USD at 0.3301 USD [API] | `2026-10-28 17:28:38` |
| `ANNOUNCEMENT` | `INFO` | `0.3299` | 6,042.81 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.04K USD at 0.3299 USD [API] | `2026-10-28 17:35:01` |
| `ANNOUNCEMENT` | `INFO` | `0.3302` | 8,091.87 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.09K USD at 0.3302 USD [API] | `2026-10-28 18:00:01` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3591` (Vol: 1,400,000.00 USD, Dist: `+1.30%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--8.37%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+3.66%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.3607` (Vol: 1,200,000.00 USD, Dist: `+1.75%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.3665` (Vol: 1,100,000.00 USD, Dist: `+3.39%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
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
| `7D` | `Long Liquidation` | `0.2923` | 24,310,000.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 100,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 99,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 24,230,000.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 24,170,000.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 96,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2959` | 17,480,000.00 USD | 17,480,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2959` | 24,090,000.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2965` | 17,480,000.00 USD | 17,480,000.00 USD | 14,230.00 USD | 6,710.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,950,000.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,710.00 USD | 95,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2971` | 17,440,000.00 USD | 17,440,000.00 USD | 18,240.00 USD | 6,720.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2971` | 23,720,000.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2977` | 17,400,000.00 USD | 17,400,000.00 USD | 17,630.00 USD | 6,840.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 23,460,000.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 17,370,000.00 USD | 17,370,000.00 USD | 109,110.00 USD | 18,870.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 23,350,000.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2989` | 17,210,000.00 USD | 17,210,000.00 USD | 55,860.00 USD | 8,480.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 23,130,000.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2995` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,980,000.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 94,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 5,200.00 USD | 94,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 17,130,000.00 USD | 17,130,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,970,000.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 88,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 78,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 17,070,000.00 USD | 17,070,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 589.40 USD | 77,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3049` | 17,030,000.00 USD | 17,030,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 22,930,000.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 16,950,000.00 USD | 16,950,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 22,880,000.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 138.70 USD | 77,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 16,880,000.00 USD | 16,880,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 22,880,000.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 15,050.00 USD | 77,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 16,820,000.00 USD | 16,820,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 22,810,000.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 16,730,000.00 USD | 16,730,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 22,800,000.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 16,710,000.00 USD | 16,710,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 22,790,000.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 16,710,000.00 USD | 16,710,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 22,690,000.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 62,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3091` | 16,690,000.00 USD | 16,690,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 22,690,000.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 292.48 USD | 55,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 16,690,000.00 USD | 16,690,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 22,680,000.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 16,690,000.00 USD | 16,690,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 22,660,000.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 668.82 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 22,530,000.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 22,520,000.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 138.31 USD | 54,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3121` | 22,520,000.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 14,170.00 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 16,570,000.00 USD | 16,570,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 22,360,000.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 16,550,000.00 USD | 16,550,000.00 USD | 164.40 USD | 0.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 22,340,000.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 25,410.00 USD | 40,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 16,530,000.00 USD | 16,530,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 22,340,000.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 16,520,000.00 USD | 16,520,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 22,330,000.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 541.88 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3151` | 16,520,000.00 USD | 16,520,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 22,020,000.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 21,760,000.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 16,510,000.00 USD | 16,510,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 21,220,000.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 14,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 16,360,000.00 USD | 16,360,000.00 USD | 84,720.00 USD | 17,660.00 USD | 39,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 20,330,000.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 16,220,000.00 USD | 16,220,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 19,470,000.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3181` | 16,130,000.00 USD | 16,130,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 19,140,000.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 15,580,000.00 USD | 15,580,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 18,190,000.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 17,720,000.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 15,310,000.00 USD | 15,310,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 15,260,000.00 USD | 15,260,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 17,420,000.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 14,960,000.00 USD | 14,960,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 17,320,000.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 16,460,000.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 14,710,000.00 USD | 14,710,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 16,010,000.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 14,420,000.00 USD | 14,420,000.00 USD | 139,110.00 USD | 81,070.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 15,080,000.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 14,000,000.00 USD | 14,000,000.00 USD | 133,230.00 USD | 80,680.00 USD | 170,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 13,630,000.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3241` | 13,610,000.00 USD | 13,610,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 11,910,000.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 13,410,000.00 USD | 13,410,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 11,100,000.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 12,420,000.00 USD | 12,420,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 9,770,000.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 129.22 USD | 594.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 11,050,000.00 USD | 11,050,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 8,440,000.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 8,050,000.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3265` | 464.94 USD | 464.94 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3271` | 10,530,000.00 USD | 10,530,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 7,860,000.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3277` | 10,070,000.00 USD | 10,070,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 7,660,000.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3289` | 9,610,000.00 USD | 9,610,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 9,410,000.00 USD | 9,410,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 7,270,000.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 7,240,000.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3307` | 9,320,000.00 USD | 9,320,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 7,170,000.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 9,110,000.00 USD | 9,110,000.00 USD | 234,580.00 USD | 121,210.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 6,830,000.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 8,430,000.00 USD | 8,430,000.00 USD | 158,550.00 USD | 32,400.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 7,940,000.00 USD | 7,940,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 6,580,000.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3331` | 7,610,000.00 USD | 7,610,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 6,450,000.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3337` | 7,610,000.00 USD | 7,610,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 6,720,000.00 USD | 6,720,000.00 USD | 76,100.00 USD | 31,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3349` | 6,610,000.00 USD | 6,610,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 5,610,000.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3355` | 6,270,000.00 USD | 6,270,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 5,380,000.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3361` | 6,180,000.00 USD | 6,180,000.00 USD | 177,350.00 USD | 0.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 5,120,000.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 5,930,000.00 USD | 5,930,000.00 USD | 240,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3373` | 5,690,000.00 USD | 5,690,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 4,880,000.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3379` | 5,560,000.00 USD | 5,560,000.00 USD | 514,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 4,290,000.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 5,050,000.00 USD | 5,050,000.00 USD | 178,310.00 USD | 70,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 3,620,000.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3385` | 511.81 USD | 511.81 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3391` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3395` | 12,820.00 USD | 13,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3397` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,340,000.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 2,910,000.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 4,410,000.00 USD | 4,410,000.00 USD | 627,050.00 USD | 0.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3415` | 86.06 USD | 13,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3421` | 3,720,000.00 USD | 3,720,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3427` | 3,210,000.00 USD | 3,210,000.00 USD | 262,640.00 USD | 48,190.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3433` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 44,190.00 USD | 176,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3439` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 98,460.00 USD | 392,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3445` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 271,430.00 USD | 217,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3445` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3451` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3457` | 1,280,000.00 USD | 1,280,000.00 USD | 1,150.00 USD | 141,160.00 USD | 258,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3463` | 880,490.00 USD | 880,490.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3469` | 825,390.00 USD | 825,390.00 USD | 0.00 USD | 151,270.00 USD | 514,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3469` | 699,440.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3475` | 159,850.00 USD | 159,850.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3481` | 191,880.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3487` | 356,270.00 USD | 356,270.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3499` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3505` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 2,360,000.00 USD | 2,360,000.00 USD | 221,620.00 USD | 0.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 1,930.00 USD | 15,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3541` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3547` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3559` | 5,520,000.00 USD | 5,520,000.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 6,100,000.00 USD | 6,100,000.00 USD | 1,770.00 USD | 0.00 USD | 578,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 6,490,000.00 USD | 6,490,000.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 6,970,000.00 USD | 6,970,000.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 7,520,000.00 USD | 7,520,000.00 USD | 1,810.00 USD | 143,920.00 USD | 400,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3595` | 7,860,000.00 USD | 7,860,000.00 USD | 199,420.00 USD | 141,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 31,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 9,110,000.00 USD | 9,110,000.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 9,210,000.00 USD | 9,210,000.00 USD | 98,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 9,270,000.00 USD | 9,270,000.00 USD | 1,360.00 USD | 60,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 9,490,000.00 USD | 9,490,000.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 9,780,000.00 USD | 9,780,000.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 10,040,000.00 USD | 10,040,000.00 USD | 259,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 68.54 USD | 15,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 10,450,000.00 USD | 10,450,000.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 10,530,000.00 USD | 10,530,000.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3679` | 11,280,000.00 USD | 11,280,000.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 11,820,000.00 USD | 11,820,000.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3691` | 12,150,000.00 USD | 12,150,000.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 12,330,000.00 USD | 12,330,000.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 13,080,000.00 USD | 13,080,000.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 13,610,000.00 USD | 13,610,000.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 15,110,000.00 USD | 15,110,000.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 289.77 USD | 15,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3721` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3727` | 16,470,000.00 USD | 16,470,000.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 17,340,000.00 USD | 17,340,000.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3739` | 17,830,000.00 USD | 17,830,000.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 18,210,000.00 USD | 18,210,000.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 15,630.00 USD | 31,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 19,050,000.00 USD | 19,050,000.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 55,050.00 USD | 86,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 19,320,000.00 USD | 19,320,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 20,570,000.00 USD | 20,570,000.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3765` | 34,780.00 USD | 121,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3769` | 20,620,000.00 USD | 20,620,000.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3775` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3781` | 20,930,000.00 USD | 20,930,000.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 685.46 USD | 121,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 21,440,000.00 USD | 21,440,000.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 21,640,000.00 USD | 21,640,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 679,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3799` | 21,640,000.00 USD | 21,640,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 21,970,000.00 USD | 21,970,000.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3805` | 323.43 USD | 680,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3823` | 22,240,000.00 USD | 22,240,000.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3829` | 22,240,000.00 USD | 22,240,000.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 665.37 USD | 680,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3841` | 22,460,000.00 USD | 22,460,000.00 USD | 850.22 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 680,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3847` | 22,460,000.00 USD | 22,460,000.00 USD | 899.18 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3865` | 22,490,000.00 USD | 22,490,000.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3871` | 22,530,000.00 USD | 22,530,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3877` | 22,560,000.00 USD | 22,560,000.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3883` | 22,560,000.00 USD | 22,560,000.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3895` | 22,590,000.00 USD | 22,590,000.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 685,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 22,640,000.00 USD | 22,640,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3913` | 22,810,000.00 USD | 22,810,000.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 686,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 22,880,000.00 USD | 22,880,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 22,960,000.00 USD | 22,960,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3925` | 21,850.00 USD | 707,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3931` | 23,040,000.00 USD | 23,040,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3937` | 23,120,000.00 USD | 23,120,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 23,330,000.00 USD | 23,330,000.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 776,680.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 23,460,000.00 USD | 23,460,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 23,660,000.00 USD | 23,660,000.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3961` | 23,760,000.00 USD | 23,760,000.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 111.42 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3967` | 23,860,000.00 USD | 23,860,000.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 24,020,000.00 USD | 24,020,000.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3975` | 502.84 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3979` | 24,420,000.00 USD | 24,420,000.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 24,430,000.00 USD | 24,430,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3991` | 24,460,000.00 USD | 24,460,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3997` | 24,550,000.00 USD | 24,550,000.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 24,640,000.00 USD | 24,640,000.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4009` | 24,810,000.00 USD | 24,810,000.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4027` | 24,890,000.00 USD | 24,890,000.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4045` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4057` | 25,080,000.00 USD | 25,080,000.00 USD | 0.00 USD | 8,920.00 USD | 97,650.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0835` | 437,640.00 USD | 0.00 USD | 173.60 USD | `-76.03%` | `2,079.00` |
| `Live` | `Long` | `0.0845` | 437,470.00 USD | 0.00 USD | 3,450.00 USD | `-75.75%` | `40,871.00` |
| `Live` | `Long` | `0.0965` | 434,010.00 USD | 0.00 USD | 137.80 USD | `-72.30%` | `1,428.00` |
| `Live` | `Long` | `0.1045` | 433,870.00 USD | 0.00 USD | 549.04 USD | `-70.01%` | `5,254.00` |
| `Live` | `Long` | `0.1175` | 433,330.00 USD | 0.00 USD | 394.80 USD | `-66.27%` | `3,360.00` |
| `Live` | `Long` | `0.1195` | 432,930.00 USD | 0.00 USD | 174.83 USD | `-65.70%` | `1,463.00` |
| `Live` | `Long` | `0.1375` | 432,760.00 USD | 0.00 USD | 1,250.00 USD | `-60.53%` | `9,085.00` |
| `Live` | `Long` | `0.1385` | 431,510.00 USD | 0.00 USD | 5,480.00 USD | `-60.25%` | `39,551.00` |
| `Live` | `Long` | `0.1395` | 426,030.00 USD | 0.00 USD | 10,710.00 USD | `-59.96%` | `76,797.00` |
| `Live` | `Long` | `0.1595` | 415,320.00 USD | 0.00 USD | 390.46 USD | `-54.22%` | `2,448.00` |
| `Live` | `Long` | `0.1705` | 414,920.00 USD | 0.00 USD | 20,360.00 USD | `-51.06%` | `119,400.00` |
| `Live` | `Long` | `0.1725` | 394,570.00 USD | 0.00 USD | 3,450.00 USD | `-50.49%` | `20,000.00` |
| `Live` | `Long` | `0.1735` | 391,120.00 USD | 0.00 USD | 11,680.00 USD | `-50.20%` | `67,322.00` |
| `Live` | `Long` | `0.1745` | 379,440.00 USD | 0.00 USD | 471.50 USD | `-49.91%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 378,970.00 USD | 0.00 USD | 1,030.00 USD | `-49.63%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 377,940.00 USD | 0.00 USD | 4,450.00 USD | `-49.34%` | `25,233.00` |
| `Live` | `Long` | `0.1775` | 373,480.00 USD | 0.00 USD | 175.37 USD | `-49.05%` | `988.00` |
| `Live` | `Long` | `0.1795` | 373,310.00 USD | 0.00 USD | 209.84 USD | `-48.48%` | `1,169.00` |
| `Live` | `Long` | `0.1855` | 373,100.00 USD | 0.00 USD | 40,580.00 USD | `-46.76%` | `218,745.00` |
| `Live` | `Long` | `0.1905` | 332,520.00 USD | 0.00 USD | 112.59 USD | `-45.32%` | `591.00` |
| `Live` | `Long` | `0.1945` | 332,410.00 USD | 0.00 USD | 274.44 USD | `-44.17%` | `1,411.00` |
| `Live` | `Long` | `0.1985` | 332,130.00 USD | 0.00 USD | 635.20 USD | `-43.03%` | `3,200.00` |
| `Live` | `Long` | `0.2075` | 331,500.00 USD | 0.00 USD | 187.58 USD | `-40.44%` | `904.00` |
| `Live` | `Long` | `0.2175` | 331,310.00 USD | 0.00 USD | 1,520.00 USD | `-37.57%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 329,790.00 USD | 0.00 USD | 744.54 USD | `-37.00%` | `3,392.00` |
| `Live` | `Long` | `0.2255` | 329,040.00 USD | 0.00 USD | 4,590.00 USD | `-35.28%` | `20,360.00` |
| `Live` | `Long` | `0.2305` | 324,450.00 USD | 0.00 USD | 2,080.00 USD | `-33.84%` | `9,004.00` |
| `Live` | `Long` | `0.2315` | 322,380.00 USD | 0.00 USD | 2,380.00 USD | `-33.55%` | `10,282.00` |
| `Live` | `Long` | `0.2325` | 320,000.00 USD | 0.00 USD | 188.56 USD | `-33.27%` | `811.00` |
| `Live` | `Long` | `0.2335` | 319,810.00 USD | 0.00 USD | 1,700.00 USD | `-32.98%` | `7,301.00` |
| `Live` | `Long` | `0.2345` | 318,100.00 USD | 0.00 USD | 1,140.00 USD | `-32.69%` | `4,882.00` |
| `Live` | `Long` | `0.2355` | 316,960.00 USD | 0.00 USD | 5,730.00 USD | `-32.41%` | `24,311.00` |
| `Live` | `Long` | `0.2365` | 311,230.00 USD | 0.00 USD | 344.11 USD | `-32.12%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 310,890.00 USD | 0.00 USD | 1,260.00 USD | `-31.54%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 309,620.00 USD | 0.00 USD | 174.12 USD | `-30.97%` | `724.00` |
| `Live` | `Long` | `0.2425` | 309,450.00 USD | 0.00 USD | 139.92 USD | `-30.40%` | `577.00` |
| `Live` | `Long` | `0.2445` | 309,310.00 USD | 0.00 USD | 889.49 USD | `-29.82%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 308,420.00 USD | 0.00 USD | 466.70 USD | `-29.54%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 307,950.00 USD | 0.00 USD | 2,690.00 USD | `-29.25%` | `10,919.00` |
| `Live` | `Long` | `0.2495` | 305,260.00 USD | 0.00 USD | 2,980.00 USD | `-28.39%` | `11,927.00` |
| `Live` | `Long` | `0.2555` | 302,290.00 USD | 0.00 USD | 1,220.00 USD | `-26.66%` | `4,769.00` |
| `Live` | `Long` | `0.2565` | 301,070.00 USD | 0.00 USD | 1,230.00 USD | `-26.38%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 299,840.00 USD | 0.00 USD | 302.96 USD | `-25.80%` | `1,172.00` |
| `Live` | `Long` | `0.2605` | 299,540.00 USD | 0.00 USD | 14,000.00 USD | `-25.23%` | `53,741.00` |
| `Live` | `Long` | `0.2635` | 285,540.00 USD | 0.00 USD | 108.56 USD | `-24.37%` | `412.00` |
| `Live` | `Long` | `0.2655` | 285,430.00 USD | 0.00 USD | 7,970.00 USD | `-23.79%` | `30,017.00` |
| `Live` | `Long` | `0.2665` | 277,460.00 USD | 0.00 USD | 193.75 USD | `-23.51%` | `727.00` |
| `Live` | `Long` | `0.2685` | 277,260.00 USD | 0.00 USD | 27,410.00 USD | `-22.93%` | `102,082.00` |
| `Live` | `Long` | `0.2695` | 249,860.00 USD | 0.00 USD | 3,170.00 USD | `-22.65%` | `11,746.00` |
| `Live` | `Long` | `0.2725` | 246,690.00 USD | 0.00 USD | 412.84 USD | `-21.79%` | `1,515.00` |
| `Live` | `Long` | `0.2755` | 246,280.00 USD | 0.00 USD | 84,780.00 USD | `-20.92%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 161,500.00 USD | 0.00 USD | 5,770.00 USD | `-20.35%` | `20,776.00` |
| `Live` | `Long` | `0.2785` | 155,730.00 USD | 0.00 USD | 516.34 USD | `-20.06%` | `1,854.00` |
| `Live` | `Long` | `0.2795` | 155,220.00 USD | 0.00 USD | 13,060.00 USD | `-19.78%` | `46,725.00` |
| `Live` | `Long` | `0.2805` | 142,160.00 USD | 0.00 USD | 6,280.00 USD | `-19.49%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 135,880.00 USD | 0.00 USD | 748.23 USD | `-19.20%` | `2,658.00` |
| `Live` | `Long` | `0.2825` | 135,130.00 USD | 0.00 USD | 15,060.00 USD | `-18.92%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 120,070.00 USD | 0.00 USD | 1,430.00 USD | `-18.63%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 118,640.00 USD | 0.00 USD | 360.42 USD | `-17.77%` | `1,258.00` |
| `Live` | `Long` | `0.2915` | 118,280.00 USD | 0.00 USD | 591.45 USD | `-16.33%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 117,690.00 USD | 0.00 USD | 957.64 USD | `-16.04%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 116,730.00 USD | 0.00 USD | 3,540.00 USD | `-15.76%` | `12,054.00` |
| `Live` | `Long` | `0.2945` | 113,190.00 USD | 0.00 USD | 213.81 USD | `-15.47%` | `726.00` |
| `Live` | `Long` | `0.2955` | 112,980.00 USD | 0.00 USD | 125.29 USD | `-15.18%` | `424.00` |
| `Live` | `Long` | `0.2995` | 112,850.00 USD | 0.00 USD | 1,800.00 USD | `-14.04%` | `5,999.00` |
| `Live` | `Long` | `0.3005` | 111,060.00 USD | 0.00 USD | 3,520.00 USD | `-13.75%` | `11,720.00` |
| `Live` | `Long` | `0.3015` | 107,530.00 USD | 0.00 USD | 10,530.00 USD | `-13.46%` | `34,910.00` |
| `Live` | `Long` | `0.3025` | 97,010.00 USD | 0.00 USD | 494.28 USD | `-13.17%` | `1,634.00` |
| `Live` | `Long` | `0.3035` | 96,510.00 USD | 0.00 USD | 589.40 USD | `-12.89%` | `1,942.00` |
| `Live` | `Long` | `0.3045` | 95,930.00 USD | 0.00 USD | 267.35 USD | `-12.60%` | `878.00` |
| `Live` | `Long` | `0.3055` | 95,660.00 USD | 0.00 USD | 138.70 USD | `-12.31%` | `454.00` |
| `Live` | `Long` | `0.3065` | 95,520.00 USD | 0.00 USD | 14,890.00 USD | `-12.03%` | `48,597.00` |
| `Live` | `Long` | `0.3085` | 80,620.00 USD | 0.00 USD | 6,670.00 USD | `-11.45%` | `21,612.00` |
| `Live` | `Long` | `0.3095` | 73,960.00 USD | 0.00 USD | 292.48 USD | `-11.17%` | `945.00` |
| `Live` | `Long` | `0.3115` | 73,660.00 USD | 0.00 USD | 658.82 USD | `-10.59%` | `2,115.00` |
| `Live` | `Long` | `0.3125` | 73,010.00 USD | 0.00 USD | 13,990.00 USD | `-10.30%` | `44,756.00` |
| `Live` | `Long` | `0.3135` | 59,020.00 USD | 0.00 USD | 20,690.00 USD | `-10.02%` | `66,002.00` |
| `Live` | `Long` | `0.3145` | 38,330.00 USD | 0.00 USD | 7,370.00 USD | `-9.73%` | `23,431.00` |
| `Live` | `Long` | `0.3155` | 30,960.00 USD | 0.00 USD | 142.29 USD | `-9.44%` | `451.00` |
| `Live` | `Long` | `0.3165` | 30,820.00 USD | 0.00 USD | 1,490.00 USD | `-9.16%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 29,320.00 USD | 0.00 USD | 938.85 USD | `-8.87%` | `2,957.00` |
| `Live` | `Long` | `0.3195` | 28,380.00 USD | 0.00 USD | 109.59 USD | `-8.30%` | `343.00` |
| `Live` | `Long` | `0.3235` | 28,270.00 USD | 0.00 USD | 11,000.00 USD | `-7.15%` | `34,003.00` |
| `Live` | `Long` | `0.3255` | 17,270.00 USD | 0.00 USD | 129.22 USD | `-6.57%` | `397.00` |
| `Live` | `Long` | `0.3265` | 17,140.00 USD | 0.00 USD | 464.94 USD | `-6.29%` | `1,424.00` |
| `Live` | `Long` | `0.3285` | 16,680.00 USD | 0.00 USD | 10,240.00 USD | `-5.71%` | `31,169.00` |
| `Live` | `Long` | `0.3305` | 6,440.00 USD | 0.00 USD | 3,420.00 USD | `-5.14%` | `10,341.00` |
| `Live` | `Long` | `0.3335` | 3,020.00 USD | 0.00 USD | 1,300.00 USD | `-4.28%` | `3,888.00` |
| `Live` | `Long` | `0.3345` | 1,730.00 USD | 0.00 USD | 1,730.00 USD | `-3.99%` | `5,159.00` |
| `Live` | `Short` | `0.3375` | 2,110.00 USD | 2,110.00 USD | 0.00 USD | `-3.13%` | `6,256.00` |
| `Live` | `Short` | `0.3385` | 3,030.00 USD | 923.09 USD | 0.00 USD | `-2.84%` | `2,727.00` |
| `Live` | `Short` | `0.3555` | 4,880.00 USD | 1,840.00 USD | 0.00 USD | `+2.04%` | `5,185.00` |
| `Live` | `Short` | `0.3575` | 6,490.00 USD | 1,610.00 USD | 0.00 USD | `+2.61%` | `4,500.00` |
| `Live` | `Short` | `0.3585` | 6,710.00 USD | 228.01 USD | 0.00 USD | `+2.90%` | `636.00` |
| `Live` | `Short` | `0.3625` | 40,900.00 USD | 34,180.00 USD | 0.00 USD | `+4.05%` | `94,302.00` |
| `Live` | `Short` | `0.3635` | 52,590.00 USD | 11,690.00 USD | 0.00 USD | `+4.33%` | `32,150.00` |
| `Live` | `Short` | `0.3645` | 53,330.00 USD | 742.12 USD | 0.00 USD | `+4.62%` | `2,036.00` |
| `Live` | `Short` | `0.3655` | 84,760.00 USD | 31,440.00 USD | 0.00 USD | `+4.91%` | `86,010.00` |
| `Live` | `Short` | `0.3685` | 87,560.00 USD | 2,800.00 USD | 0.00 USD | `+5.77%` | `7,600.00` |
| `Live` | `Short` | `0.3735` | 87,860.00 USD | 291.33 USD | 0.00 USD | `+7.20%` | `780.00` |
| `Live` | `Short` | `0.3745` | 95,020.00 USD | 7,170.00 USD | 0.00 USD | `+7.49%` | `19,140.00` |
| `Live` | `Short` | `0.3765` | 95,710.00 USD | 681.84 USD | 0.00 USD | `+8.07%` | `1,811.00` |
| `Live` | `Short` | `0.3785` | 111,710.00 USD | 16,000.00 USD | 0.00 USD | `+8.64%` | `42,278.00` |
| `Live` | `Short` | `0.3795` | 669,600.00 USD | 557,900.00 USD | 0.00 USD | `+8.93%` | `1,470,083.00` |
| `Live` | `Short` | `0.3825` | 685,550.00 USD | 15,940.00 USD | 0.00 USD | `+9.79%` | `41,685.00` |
| `Live` | `Short` | `0.3845` | 685,660.00 USD | 115.35 USD | 0.00 USD | `+10.36%` | `300.00` |
| `Live` | `Short` | `0.3885` | 688,560.00 USD | 2,890.00 USD | 0.00 USD | `+11.51%` | `7,444.00` |
| `Live` | `Short` | `0.3905` | 693,320.00 USD | 4,770.00 USD | 0.00 USD | `+12.08%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 693,810.00 USD | 487.42 USD | 0.00 USD | `+12.37%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 707,720.00 USD | 13,910.00 USD | 0.00 USD | `+13.23%` | `35,254.00` |
| `Live` | `Short` | `0.3955` | 826,150.00 USD | 118,430.00 USD | 0.00 USD | `+13.52%` | `299,436.00` |
| `Live` | `Short` | `0.3975` | 827,290.00 USD | 1,140.00 USD | 0.00 USD | `+14.09%` | `2,873.00` |
| `Live` | `Short` | `0.4035` | 831,840.00 USD | 4,560.00 USD | 0.00 USD | `+15.82%` | `11,292.00` |
| `Live` | `Short` | `0.4045` | 831,960.00 USD | 115.69 USD | 0.00 USD | `+16.10%` | `286.00` |
| `Live` | `Short` | `0.4065` | 833,970.00 USD | 2,010.00 USD | 0.00 USD | `+16.68%` | `4,939.00` |
| `Live` | `Short` | `0.4085` | 835,760.00 USD | 1,790.00 USD | 0.00 USD | `+17.25%` | `4,378.00` |
| `Live` | `Short` | `0.4115` | 836,850.00 USD | 1,100.00 USD | 0.00 USD | `+18.11%` | `2,668.00` |
| `Live` | `Short` | `0.4165` | 870,650.00 USD | 33,800.00 USD | 0.00 USD | `+19.55%` | `81,141.00` |
| `Live` | `Short` | `0.4175` | 871,250.00 USD | 599.53 USD | 0.00 USD | `+19.83%` | `1,436.00` |
| `Live` | `Short` | `0.4205` | 872,260.00 USD | 1,010.00 USD | 0.00 USD | `+20.69%` | `2,408.00` |
| `Live` | `Short` | `0.4215` | 1,090,000.00 USD | 222,080.00 USD | 0.00 USD | `+20.98%` | `526,888.00` |
| `Live` | `Short` | `0.4245` | 1,120,000.00 USD | 24,200.00 USD | 0.00 USD | `+21.84%` | `57,000.00` |
| `Live` | `Short` | `0.4265` | 1,120,000.00 USD | 201.31 USD | 0.00 USD | `+22.42%` | `472.00` |
| `Live` | `Short` | `0.4285` | 1,430,000.00 USD | 313,010.00 USD | 0.00 USD | `+22.99%` | `730,477.00` |
| `Live` | `Short` | `0.4305` | 1,510,000.00 USD | 82,110.00 USD | 0.00 USD | `+23.56%` | `190,735.00` |
| `Live` | `Short` | `0.4315` | 1,520,000.00 USD | 4,170.00 USD | 0.00 USD | `+23.85%` | `9,658.00` |
| `Live` | `Short` | `0.4385` | 1,610,000.00 USD | 91,950.00 USD | 0.00 USD | `+25.86%` | `209,683.00` |
| `Live` | `Short` | `0.4395` | 1,680,000.00 USD | 71,540.00 USD | 0.00 USD | `+26.15%` | `162,775.00` |
| `Live` | `Short` | `0.4455` | 1,690,000.00 USD | 3,820.00 USD | 0.00 USD | `+27.87%` | `8,564.00` |
| `Live` | `Short` | `0.4475` | 1,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+28.44%` | `2,284.00` |
| `Live` | `Short` | `0.4485` | 1,750,000.00 USD | 66,060.00 USD | 0.00 USD | `+28.73%` | `147,290.00` |
| `Live` | `Short` | `0.4505` | 1,750,000.00 USD | 175.24 USD | 0.00 USD | `+29.31%` | `389.00` |
| `Live` | `Short` | `0.4525` | 1,760,000.00 USD | 5,570.00 USD | 0.00 USD | `+29.88%` | `12,303.00` |
| `Live` | `Short` | `0.4535` | 2,230,000.00 USD | 467,070.00 USD | 0.00 USD | `+30.17%` | `1,029,919.00` |
| `Live` | `Short` | `0.4595` | 2,230,000.00 USD | 318.89 USD | 0.00 USD | `+31.89%` | `694.00` |
| `Live` | `Short` | `0.4705` | 2,230,000.00 USD | 103.98 USD | 0.00 USD | `+35.05%` | `221.00` |
| `Live` | `Short` | `0.4905` | 2,230,000.00 USD | 841.21 USD | 0.00 USD | `+40.79%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 2,230,000.00 USD | 5,130.00 USD | 0.00 USD | `+41.07%` | `10,430.00` |
| `Live` | `Short` | `0.4965` | 2,250,000.00 USD | 20,840.00 USD | 0.00 USD | `+42.51%` | `41,969.00` |
| `Live` | `Short` | `0.5025` | 2,250,000.00 USD | 236.17 USD | 0.00 USD | `+44.23%` | `470.00` |
| `Live` | `Short` | `0.5145` | 2,250,000.00 USD | 297.38 USD | 0.00 USD | `+47.68%` | `578.00` |
| `Live` | `Short` | `0.5185` | 2,330,000.00 USD | 72,070.00 USD | 0.00 USD | `+48.82%` | `139,000.00` |
| `Live` | `Short` | `0.5345` | 2,330,000.00 USD | 669.73 USD | 0.00 USD | `+53.42%` | `1,253.00` |
| `Live` | `Short` | `0.5435` | 2,960,000.00 USD | 637,800.00 USD | 0.00 USD | `+56.00%` | `1,173,513.00` |
| `Live` | `Short` | `0.5505` | 2,970,000.00 USD | 2,290.00 USD | 0.00 USD | `+58.01%` | `4,154.00` |
| `Live` | `Short` | `0.5585` | 2,970,000.00 USD | 6,360.00 USD | 0.00 USD | `+60.30%` | `11,386.00` |
| `Live` | `Short` | `0.5605` | 2,980,000.00 USD | 8,270.00 USD | 0.00 USD | `+60.88%` | `14,763.00` |
| `Live` | `Short` | `0.5615` | 3,710,000.00 USD | 728,400.00 USD | 0.00 USD | `+61.17%` | `1,297,248.00` |
| `Live` | `Short` | `0.5625` | 3,710,000.00 USD | 140.62 USD | 0.00 USD | `+61.45%` | `250.00` |
| `Live` | `Short` | `0.5745` | 3,710,000.00 USD | 213.14 USD | 0.00 USD | `+64.90%` | `371.00` |
| `Live` | `Short` | `0.5765` | 3,770,000.00 USD | 56,240.00 USD | 0.00 USD | `+65.47%` | `97,553.00` |
| `Live` | `Short` | `0.5945` | 3,770,000.00 USD | 7,370.00 USD | 0.00 USD | `+70.64%` | `12,403.00` |
| `Live` | `Short` | `0.5995` | 3,830,000.00 USD | 53,170.00 USD | 0.00 USD | `+72.07%` | `88,696.00` |
| `Live` | `Short` | `0.6145` | 3,860,000.00 USD | 36,870.00 USD | 0.00 USD | `+76.38%` | `60,000.00` |
| `Live` | `Short` | `0.6155` | 3,890,000.00 USD | 29,540.00 USD | 0.00 USD | `+76.66%` | `47,992.00` |
| `Live` | `Short` | `0.6165` | 3,920,000.00 USD | 24,660.00 USD | 0.00 USD | `+76.95%` | `40,000.00` |
| `Live` | `Short` | `0.6275` | 3,920,000.00 USD | 275.47 USD | 0.00 USD | `+80.11%` | `439.00` |
| `Live` | `Short` | `0.6285` | 3,920,000.00 USD | 7,390.00 USD | 0.00 USD | `+80.40%` | `11,753.00` |
| `Live` | `Short` | `0.6305` | 3,930,000.00 USD | 281.83 USD | 0.00 USD | `+80.97%` | `447.00` |
| `Live` | `Short` | `0.6555` | 3,940,000.00 USD | 16,230.00 USD | 0.00 USD | `+88.15%` | `24,756.00` |
| `Live` | `Short` | `0.6615` | 3,940,000.00 USD | 565.58 USD | 0.00 USD | `+89.87%` | `855.00` |
| `Live` | `Short` | `0.6645` | 3,940,000.00 USD | 1,210.00 USD | 0.00 USD | `+90.73%` | `1,821.00` |
| `Live` | `Short` | `0.6745` | 4,030,000.00 USD | 83,190.00 USD | 0.00 USD | `+93.60%` | `123,332.00` |
| `Live` | `Short` | `0.6805` | 4,030,000.00 USD | 2,770.00 USD | 0.00 USD | `+95.32%` | `4,068.00` |
| `Live` | `Short` | `0.6885` | 4,030,000.00 USD | 263.01 USD | 0.00 USD | `+97.62%` | `382.00` |
| `Live` | `Short` | `0.6935` | 4,030,000.00 USD | 414.71 USD | 0.00 USD | `+99.05%` | `598.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 1,050,000.00 USD | 0.00 USD | 6,100.00 USD | `-48.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,040,000.00 USD | 0.00 USD | 1,750.00 USD | `-41.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,040,000.00 USD | 0.00 USD | 579.72 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,040,000.00 USD | 0.00 USD | 121.70 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,040,000.00 USD | 0.00 USD | 705.61 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 1,040,000.00 USD | 0.00 USD | 159.20 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,040,000.00 USD | 0.00 USD | 1,200.00 USD | `-30.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,040,000.00 USD | 0.00 USD | 127.51 USD | `-30.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,040,000.00 USD | 0.00 USD | 1,850.00 USD | `-28.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 1,040,000.00 USD | 0.00 USD | 41,500.00 USD | `-27.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 994,480.00 USD | 0.00 USD | 1,920.00 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 992,560.00 USD | 0.00 USD | 664.01 USD | `-25.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 991,890.00 USD | 0.00 USD | 954.98 USD | `-24.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 990,940.00 USD | 0.00 USD | 695.50 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 990,240.00 USD | 0.00 USD | 1,630.00 USD | `-22.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 988,620.00 USD | 0.00 USD | 101.94 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 988,520.00 USD | 0.00 USD | 3,260.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 985,260.00 USD | 0.00 USD | 2,550.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 982,700.00 USD | 0.00 USD | 229.92 USD | `-18.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 982,470.00 USD | 0.00 USD | 11,610.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 970,860.00 USD | 0.00 USD | 111.19 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 970,750.00 USD | 0.00 USD | 326.86 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 970,430.00 USD | 0.00 USD | 2,710.00 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 967,720.00 USD | 0.00 USD | 335.56 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 967,390.00 USD | 0.00 USD | 919.50 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 966,470.00 USD | 0.00 USD | 193.11 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 966,270.00 USD | 0.00 USD | 15,150.00 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 951,120.00 USD | 0.00 USD | 147.32 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 950,970.00 USD | 0.00 USD | 11,410.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 939,570.00 USD | 0.00 USD | 6,530.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 933,040.00 USD | 0.00 USD | 524,570.00 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 408,460.00 USD | 0.00 USD | 1,270.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 407,200.00 USD | 0.00 USD | 25,720.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 381,480.00 USD | 0.00 USD | 1,950.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 379,530.00 USD | 0.00 USD | 6,100.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 373,440.00 USD | 0.00 USD | 1,040.00 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 372,400.00 USD | 0.00 USD | 5,610.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 366,790.00 USD | 0.00 USD | 9,840.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 356,940.00 USD | 0.00 USD | 43,570.00 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 313,380.00 USD | 0.00 USD | 131.90 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 313,240.00 USD | 0.00 USD | 166.60 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 313,080.00 USD | 0.00 USD | 3,680.00 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 309,400.00 USD | 0.00 USD | 537.73 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 308,860.00 USD | 0.00 USD | 6,130.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 302,730.00 USD | 0.00 USD | 6,110.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 296,620.00 USD | 0.00 USD | 1,320.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 295,310.00 USD | 0.00 USD | 5,890.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 289,420.00 USD | 0.00 USD | 949.53 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 288,470.00 USD | 0.00 USD | 100.11 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 288,370.00 USD | 0.00 USD | 135.99 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 288,240.00 USD | 0.00 USD | 1,010.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 287,230.00 USD | 0.00 USD | 7,100.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 280,130.00 USD | 0.00 USD | 174,860.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 105,260.00 USD | 0.00 USD | 34,240.00 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 71,030.00 USD | 0.00 USD | 536.96 USD | `-3.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 70,490.00 USD | 0.00 USD | 30,020.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 40,470.00 USD | 0.00 USD | 1,940.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 38,530.00 USD | 0.00 USD | 3,090.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 35,440.00 USD | 0.00 USD | 118.16 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 35,320.00 USD | 0.00 USD | 5,520.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 29,800.00 USD | 0.00 USD | 7,610.00 USD | `-1.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 22,190.00 USD | 0.00 USD | 18,620.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 3,570.00 USD | 0.00 USD | 1,060.00 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 2,510.00 USD | 0.00 USD | 101.52 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 2,410.00 USD | 0.00 USD | 2,410.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 4,380.00 USD | 4,380.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 12,140.00 USD | 7,750.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 30,720.00 USD | 18,580.00 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 50,100.00 USD | 19,380.00 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 51,450.00 USD | 1,350.00 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 52,220.00 USD | 769.97 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 53,190.00 USD | 969.45 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 57,210.00 USD | 4,030.00 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 58,140.00 USD | 924.85 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 61,220.00 USD | 3,080.00 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 62,250.00 USD | 1,030.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 63,350.00 USD | 1,100.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 63,460.00 USD | 103.23 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 63,590.00 USD | 136.69 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 64,030.00 USD | 433.85 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 64,350.00 USD | 326.19 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 64,530.00 USD | 172.72 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 78,860.00 USD | 14,330.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 79,170.00 USD | 310.11 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 79,350.00 USD | 174.60 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 79,450.00 USD | 107.28 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 79,890.00 USD | 439.61 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 80,170.00 USD | 281.25 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 81,720.00 USD | 1,550.00 USD | 0.00 USD | `+7.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 81,910.00 USD | 182.60 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 88,360.00 USD | 6,450.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 88,630.00 USD | 275.17 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 89,100.00 USD | 463.37 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 91,710.00 USD | 2,610.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 91,970.00 USD | 257.89 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 92,190.00 USD | 224.73 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 92,810.00 USD | 621.04 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 92,960.00 USD | 152.28 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 94,080.00 USD | 1,110.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 94,430.00 USD | 352.11 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 96,830.00 USD | 2,400.00 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 97,680.00 USD | 847.87 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 99,030.00 USD | 1,350.00 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 151,910.00 USD | 52,880.00 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 152,780.00 USD | 864.28 USD | 0.00 USD | `+14.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 155,180.00 USD | 2,400.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 156,380.00 USD | 1,200.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 157,580.00 USD | 1,200.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 158,770.00 USD | 1,200.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 158,910.00 USD | 138.07 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 159,480.00 USD | 564.43 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 159,790.00 USD | 313.54 USD | 0.00 USD | `+19.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 159,980.00 USD | 186.70 USD | 0.00 USD | `+20.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 160,300.00 USD | 325.75 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 160,600.00 USD | 299.19 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 199,180.00 USD | 38,580.00 USD | 0.00 USD | `+26.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 199,350.00 USD | 170.69 USD | 0.00 USD | `+27.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 200,740.00 USD | 1,390.00 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 206,080.00 USD | 5,340.00 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 286,840.00 USD | 80,770.00 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 298,000.00 USD | 11,150.00 USD | 0.00 USD | `+43.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 299,920.00 USD | 1,930.00 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 300,160.00 USD | 240.85 USD | 0.00 USD | `+80.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 313,780.00 USD | 13,610.00 USD | 0.00 USD | `+94.17%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2923` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD |
| `7D` | `0.2947` | 24,230,000.00 USD | 0.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD |
| `7D` | `0.2953` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD |
| `7D` | `0.2959` | 24,090,000.00 USD | 0.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 23,950,000.00 USD | 0.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD |
| `7D` | `0.2971` | 23,720,000.00 USD | 0.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD |
| `7D` | `0.2977` | 23,460,000.00 USD | 0.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD |
| `7D` | `0.2983` | 23,350,000.00 USD | 0.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `7D` | `0.2989` | 23,130,000.00 USD | 0.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD |
| `7D` | `0.2995` | 22,980,000.00 USD | 0.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD |
| `1D` | `0.3001` | 13,840,000.00 USD | 0.00 USD | 13,840,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3007` | 13,840,000.00 USD | 0.00 USD | 13,840,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD |
| `7D` | `0.3007` | 22,970,000.00 USD | 0.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3019` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3031` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD |
| `1D` | `0.3049` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3049` | 22,930,000.00 USD | 0.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3055` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3067` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 22,810,000.00 USD | 0.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3073` | 13,440,000.00 USD | 0.00 USD | 13,440,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3073` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 22,790,000.00 USD | 0.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3085` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3085` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3103` | 13,400,000.00 USD | 0.00 USD | 13,400,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 22,660,000.00 USD | 0.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `7D` | `0.3109` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3121` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD |
| `7D` | `0.3127` | 22,360,000.00 USD | 0.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3133` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD |
| `7D` | `0.3139` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3145` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3145` | 22,330,000.00 USD | 0.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3151` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 22,020,000.00 USD | 0.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3157` | 13,180,000.00 USD | 0.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD |
| `7D` | `0.3157` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3163` | 13,160,000.00 USD | 0.00 USD | 13,160,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD |
| `7D` | `0.3163` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD |
| `1D` | `0.3169` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 82,960.00 USD | 16,570.00 USD | 38,410.00 USD |
| `7D` | `0.3169` | 20,330,000.00 USD | 0.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD |
| `1D` | `0.3175` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD |
| `7D` | `0.3175` | 19,470,000.00 USD | 0.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD |
| `1D` | `0.3181` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD |
| `7D` | `0.3181` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD |
| `1D` | `0.3187` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD |
| `7D` | `0.3187` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3193` | 11,980,000.00 USD | 0.00 USD | 11,980,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `7D` | `0.3193` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3199` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 17,520,000.00 USD | 0.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3205` | 11,920,000.00 USD | 0.00 USD | 11,920,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD |
| `7D` | `0.3205` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3211` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD |
| `7D` | `0.3211` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3217` | 11,460,000.00 USD | 0.00 USD | 11,460,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3217` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3223` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD |
| `7D` | `0.3223` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3229` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 139,110.00 USD | 81,070.00 USD | 205,050.00 USD |
| `7D` | `0.3229` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD |
| `1D` | `0.3235` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 129,720.00 USD | 78,500.00 USD | 168,760.00 USD |
| `7D` | `0.3235` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD |
| `1D` | `0.3241` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD |
| `7D` | `0.3241` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD |
| `1D` | `0.3247` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD |
| `7D` | `0.3247` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3253` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD |
| `7D` | `0.3253` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3259` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3265` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD |
| `7D` | `0.3265` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3271` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD |
| `7D` | `0.3271` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3277` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3283` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD |
| `7D` | `0.3283` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3289` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3295` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `7D` | `0.3301` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3307` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD |
| `7D` | `0.3307` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3313` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD |
| `7D` | `0.3313` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3319` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD |
| `7D` | `0.3319` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3325` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD |
| `7D` | `0.3325` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD |
| `1D` | `0.3331` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3331` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD |
| `1D` | `0.3337` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD |
| `7D` | `0.3337` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD |
| `1D` | `0.3343` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3343` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `1D` | `0.3349` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD |
| `7D` | `0.3349` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3355` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD |
| `1D` | `0.3361` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 177,350.00 USD | 81,810.00 USD | 65,250.00 USD |
| `7D` | `0.3361` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3367` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 237,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3367` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3373` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD |
| `7D` | `0.3373` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3379` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 514,160.00 USD | 44,400.00 USD | 0.00 USD |
| `7D` | `0.3379` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3385` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD |
| `7D` | `0.3385` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3391` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD |
| `1D` | `0.3397` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD |
| `7D` | `0.3397` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD |
| `1D` | `0.3403` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD |
| `7D` | `0.3403` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3409` | 973,540.00 USD | 0.00 USD | 973,540.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD |
| `7D` | `0.3409` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD |
| `1D` | `0.3415` | 809,430.00 USD | 0.00 USD | 809,430.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD |
| `1D` | `0.3421` | 512,390.00 USD | 512,390.00 USD | 0.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD |
| `1D` | `0.3421` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD |
| `1D` | `0.3427` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 262,640.00 USD | 93,060.00 USD | 187,820.00 USD |
| `7D` | `0.3427` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3433` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 162,950.00 USD | 176,350.00 USD |
| `1D` | `0.3439` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 34,460.00 USD | 392,630.00 USD |
| `1D` | `0.3445` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 217,030.00 USD |
| `7D` | `0.3445` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3451` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 229,860.00 USD |
| `7D` | `0.3451` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3457` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD |
| `1D` | `0.3469` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD |
| `7D` | `0.3469` | 699,440.00 USD | 0.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD |
| `1D` | `0.3475` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD |
| `7D` | `0.3481` | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `7D` | `0.3485` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3487` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD |
| `1D` | `0.3499` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD |
| `1D` | `0.3505` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD |
| `1D` | `0.3511` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD |
| `1D` | `0.3517` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 221,620.00 USD | 44,400.00 USD | 434,060.00 USD |
| `1D` | `0.3523` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 0.00 USD | 44,920.00 USD | 459,710.00 USD |
| `7D` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD |
| `1D` | `0.3541` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD |
| `7D` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 0.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3547` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD |
| `1D` | `0.3553` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 119,690.00 USD | 0.00 USD |
| `1D` | `0.3559` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD |
| `1D` | `0.3571` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 1,770.00 USD | 163,630.00 USD | 578,320.00 USD |
| `1D` | `0.3577` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3583` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD |
| `7D` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3589` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 1,810.00 USD | 166,120.00 USD | 400,320.00 USD |
| `7D` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD |
| `1D` | `0.3595` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 199,420.00 USD | 163,620.00 USD | 0.00 USD |
| `7D` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3601` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD |
| `7D` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD |
| `7D` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3613` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD |
| `7D` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD |
| `1D` | `0.3619` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `7D` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3631` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3637` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD |
| `1D` | `0.3643` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD |
| `7D` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3649` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD |
| `7D` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3655` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD |
| `7D` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3661` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 259,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3667` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD |
| `7D` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3673` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD |
| `7D` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3679` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD |
| `7D` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3685` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD |
| `7D` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD |
| `1D` | `0.3691` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD |
| `7D` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD |
| `1D` | `0.3697` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD |
| `7D` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD |
| `1D` | `0.3703` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD |
| `1D` | `0.3709` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD |
| `7D` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3715` | 19,390,000.00 USD | 19,390,000.00 USD | 0.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD |
| `7D` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3721` | 19,600,000.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD |
| `7D` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3727` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD |
| `7D` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3733` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3739` | 22,100,000.00 USD | 22,100,000.00 USD | 0.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD |
| `7D` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3745` | 22,490,000.00 USD | 22,490,000.00 USD | 0.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD |
| `7D` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3751` | 23,330,000.00 USD | 23,330,000.00 USD | 0.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD |
| `1D` | `0.3757` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD |
| `7D` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3763` | 24,840,000.00 USD | 24,840,000.00 USD | 0.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3769` | 24,900,000.00 USD | 24,900,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD |
| `7D` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3775` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3781` | 25,210,000.00 USD | 25,210,000.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD |
| `7D` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3787` | 25,720,000.00 USD | 25,720,000.00 USD | 0.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD |
| `7D` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3793` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD |
| `7D` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3799` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3805` | 26,250,000.00 USD | 26,250,000.00 USD | 0.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD |
| `7D` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3823` | 26,510,000.00 USD | 26,510,000.00 USD | 0.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD |
| `7D` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3829` | 26,540,000.00 USD | 26,540,000.00 USD | 0.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD |
| `1D` | `0.3835` | 26,760,000.00 USD | 26,760,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 26,760,000.00 USD | 26,760,000.00 USD | 0.00 USD | 850.22 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3847` | 26,760,000.00 USD | 26,760,000.00 USD | 0.00 USD | 899.18 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3853` | 26,780,000.00 USD | 26,780,000.00 USD | 0.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3865` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD |
| `7D` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `1D` | `0.3871` | 26,850,000.00 USD | 26,850,000.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3877` | 26,880,000.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD |
| `7D` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3883` | 26,880,000.00 USD | 26,880,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3895` | 26,910,000.00 USD | 26,910,000.00 USD | 0.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD |
| `7D` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3907` | 26,960,000.00 USD | 26,960,000.00 USD | 0.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `1D` | `0.3913` | 27,130,000.00 USD | 27,130,000.00 USD | 0.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3919` | 27,200,000.00 USD | 27,200,000.00 USD | 0.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3925` | 27,280,000.00 USD | 27,280,000.00 USD | 0.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD |
| `7D` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `1D` | `0.3931` | 27,370,000.00 USD | 27,370,000.00 USD | 0.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `1D` | `0.3937` | 27,440,000.00 USD | 27,440,000.00 USD | 0.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD |
| `7D` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `1D` | `0.3943` | 27,660,000.00 USD | 27,660,000.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD |
| `7D` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `1D` | `0.3949` | 27,790,000.00 USD | 27,790,000.00 USD | 0.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD |
| `7D` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD |
| `1D` | `0.3955` | 27,980,000.00 USD | 27,980,000.00 USD | 0.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD |
| `7D` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD |
| `1D` | `0.3961` | 28,080,000.00 USD | 28,080,000.00 USD | 0.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD |
| `7D` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD |
| `1D` | `0.3967` | 28,180,000.00 USD | 28,180,000.00 USD | 0.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD |
| `7D` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD |
| `1D` | `0.3973` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD |
| `7D` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `1D` | `0.3979` | 28,740,000.00 USD | 28,740,000.00 USD | 0.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD |
| `7D` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD |
| `1D` | `0.3985` | 28,750,000.00 USD | 28,750,000.00 USD | 0.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD |
| `7D` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `1D` | `0.3991` | 28,780,000.00 USD | 28,780,000.00 USD | 0.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `7D` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD |
| `1D` | `0.3997` | 28,870,000.00 USD | 28,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD |
| `1D` | `0.4003` | 28,960,000.00 USD | 28,960,000.00 USD | 0.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD |
| `7D` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `1D` | `0.4009` | 29,130,000.00 USD | 29,130,000.00 USD | 0.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD |
| `7D` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD |
| `1D` | `0.4027` | 29,210,000.00 USD | 29,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.4045` | 29,300,000.00 USD | 29,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `386.36M` | Total OI Tokens: `1,126,099,068.3 TRX`
  * 1h OI Change: `+0.78%` | 4h OI Change: `+29.61%` | 24h OI Change: `+32.83%`
  * Exchange Breakdown: Binance=`115.09M` | Bybit=`80.09M` | OKX=`24.23M` | Hyperliquid=`16.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-632.68K` | Last 24h: `9.22K` | Last 3d: `-51.81K` | Last 7d: `-271.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.2213%` | **USDT OKX** | `-0.8797%` |
| **USDT Bybit** | `-0.2183%` | **USDT KuCoin** | `-0.5250%` |
| **USDT MEXC** | `-0.2195%` | **USDT BingX** | `-0.5000%` |
| **USDT Gate** | `-0.5027%` | **USDT Bitget** | `-0.3249%` |
| **CoinM Binance** | `-0.1997%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `47.87%` | `52.13%` | `0.92` | 13,620,000.00 USD |
| `15M` | `Binance` | `44.82%` | `55.18%` | `0.81` | 4,020,000.00 USD |
| `15M` | `OKX` | `48.48%` | `51.52%` | `0.94` | 1,230,000.00 USD |
| `15M` | `Bybit` | `55.36%` | `44.64%` | `1.24` | 1,610,000.00 USD |
| `15M` | `KuCoin` | `45.84%` | `54.16%` | `0.85` | 98,140.00 USD |
| `15M` | `Gate` | `55.68%` | `44.32%` | `1.26` | 676,530.00 USD |
| `15M` | `Bitget` | `49.32%` | `50.68%` | `0.97` | 858,140.00 USD |
| `15M` | `BingX` | `41.27%` | `58.73%` | `0.70` | 116,390.00 USD |
| `15M` | `MEXC` | `53.33%` | `46.67%` | `1.14` | 1,950,000.00 USD |
| `15M` | `Bitunix` | `38.24%` | `61.76%` | `0.62` | 186,140.00 USD |
| `15M` | `Hyperliquid` | `4.81%` | `95.19%` | `0.05` | 536,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.15%` | `52.85%` | `0.89` | 1,970,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `87.92%` | `12.08%` | `7.28` | 230,180.00 USD |
| `15M` | `HTX` | `64.48%` | `35.52%` | `1.82` | 30,850.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.92%` | `53.08%` | `0.88` | 94,010.00 USD |
| `15M` | `Aster` | `23.96%` | `76.04%` | `0.32` | 967.89 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `36.92%` | `63.08%` | `0.59` | 6,280.00 USD |
| `15M` | `Whale Positions` | `44.82%` | `55.18%` | `0.81` | 4,020,000.00 USD |
| `15M` | `Global Accounts` | `47.87%` | `52.13%` | `0.92` | 13,620,000.00 USD |
| `1H` | `TRX` | `51.27%` | `48.73%` | `1.05` | 45,760,000.00 USD |
| `1H` | `Binance` | `49.56%` | `50.44%` | `0.98` | 15,040,000.00 USD |
| `1H` | `OKX` | `49.51%` | `50.49%` | `0.98` | 3,700,000.00 USD |
| `1H` | `Bybit` | `54.61%` | `45.39%` | `1.20` | 4,470,000.00 USD |
| `1H` | `KuCoin` | `47.2%` | `52.8%` | `0.89` | 390,980.00 USD |
| `1H` | `Gate` | `51.83%` | `48.17%` | `1.08` | 2,050,000.00 USD |
| `1H` | `Bitget` | `44.39%` | `55.61%` | `0.80` | 1,920,000.00 USD |
| `1H` | `BingX` | `49.68%` | `50.32%` | `0.99` | 2,570,000.00 USD |
| `1H` | `MEXC` | `56.24%` | `43.76%` | `1.29` | 4,720,000.00 USD |
| `1H` | `Bitunix` | `55.16%` | `44.84%` | `1.23` | 950,190.00 USD |
| `1H` | `Hyperliquid` | `36.73%` | `63.27%` | `0.58` | 1,310,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.23%` | `48.77%` | `1.05` | 7,360,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `82.27%` | `17.73%` | `4.64` | 880,620.00 USD |
| `1H` | `HTX` | `50.56%` | `49.44%` | `1.02` | 76,980.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.56%` | `47.44%` | `1.11` | 311,380.00 USD |
| `1H` | `Aster` | `18.37%` | `81.63%` | `0.23` | 2,770.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.19%` | `67.81%` | `0.47` | 15,410.00 USD |
| `1H` | `Whale Positions` | `49.56%` | `50.44%` | `0.98` | 15,040,000.00 USD |
| `1H` | `Global Accounts` | `51.27%` | `48.73%` | `1.05` | 45,760,000.00 USD |
| `4H` | `TRX` | `47.08%` | `52.92%` | `0.89` | 353,080,000.00 USD |
| `4H` | `Binance` | `46.32%` | `53.68%` | `0.86` | 117,600,000.00 USD |
| `4H` | `OKX` | `48.06%` | `51.94%` | `0.93` | 39,200,000.00 USD |
| `4H` | `Bybit` | `48.75%` | `51.25%` | `0.95` | 37,720,000.00 USD |
| `4H` | `KuCoin` | `50.84%` | `49.16%` | `1.03` | 2,890,000.00 USD |
| `4H` | `Gate` | `50.43%` | `49.57%` | `1.02` | 16,380,000.00 USD |
| `4H` | `Bitget` | `46.57%` | `53.43%` | `0.87` | 25,840,000.00 USD |
| `4H` | `BingX` | `27.26%` | `72.74%` | `0.37` | 18,970,000.00 USD |
| `4H` | `MEXC` | `46.07%` | `53.93%` | `0.85` | 22,120,000.00 USD |
| `4H` | `Bitunix` | `49.16%` | `50.84%` | `0.97` | 8,080,000.00 USD |
| `4H` | `Hyperliquid` | `42.99%` | `57.01%` | `0.75` | 5,520,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.51%` | `46.49%` | `1.15` | 53,020,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.89%` | `53.11%` | `0.88` | 3,070,000.00 USD |
| `4H` | `HTX` | `48.23%` | `51.77%` | `0.93` | 559,250.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.51%` | `51.49%` | `0.94` | 1,740,000.00 USD |
| `4H` | `Aster` | `36.07%` | `63.93%` | `0.56` | 239,300.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.79%` | `59.21%` | `0.69` | 124,220.00 USD |
| `4H` | `Whale Positions` | `46.32%` | `53.68%` | `0.86` | 117,600,000.00 USD |
| `4H` | `Global Accounts` | `47.08%` | `52.92%` | `0.89` | 353,080,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3363` | `0.3285` | 10,644,567.03 USD | 5,188,760.14 USD | 5,455,806.89 USD | -267,046.75 USD | `-2.51%` | `23B / 18S` |
| `0:00 UTC` | `0.3310` | `0.3345` | `0.3310` | `0.3414` | `0.3283` | 12,234,359.27 USD | 6,873,169.39 USD | 5,361,189.88 USD | 1,511,979.51 USD | `+12.36%` | `29B / 4S` |
| `5:00 UTC` | `0.3410` | `0.3437` | `0.3410` | `0.3496` | `0.3386` | 15,171,697.80 USD | 7,420,251.93 USD | 7,751,445.87 USD | -331,193.94 USD | `-2.18%` | `3B / 6S` |
| `0:00 UTC` | `0.3377` | `0.3416` | `0.3377` | `0.3499` | `0.3361` | 21,787,549.51 USD | 11,969,195.40 USD | 9,818,354.10 USD | 2,150,841.30 USD | `+9.87%` | `13B / 4S` |
| `5:00 UTC` | `0.3600` | `0.3572` | `0.3600` | `0.3651` | `0.3467` | 44,541,588.04 USD | 22,230,180.93 USD | 22,311,407.11 USD | -81,226.19 USD | `-0.18%` | `8B / 6S` |
| `0:00 UTC` | `0.3597` | `0.3554` | `0.3597` | `0.3654` | `0.3450` | 47,319,855.69 USD | 24,728,561.34 USD | 22,591,294.35 USD | 2,137,266.99 USD | `+4.52%` | `7B / 1S` |
| `5:00 UTC` | `0.3490` | `0.3506` | `0.3490` | `0.3575` | `0.3423` | 29,514,058.42 USD | 13,466,249.86 USD | 16,047,808.55 USD | -2,581,558.69 USD | `-8.75%` | `3B / 18S` |
| `0:00 UTC` | `0.3460` | `0.3448` | `0.3460` | `0.3537` | `0.3368` | 24,777,531.84 USD | 11,850,131.84 USD | 12,927,400.00 USD | -1,077,268.15 USD | `-4.35%` | `10B / 8S` |
| `5:00 UTC` | `0.3549` | `0.3516` | `0.3549` | `0.3564` | `0.3478` | 17,864,049.59 USD | 8,681,179.68 USD | 9,182,869.91 USD | -501,690.24 USD | `-2.81%` | `5B / 7S` |
| `0:00 UTC` | `0.3480` | `0.3472` | `0.3480` | `0.3506` | `0.3441` | 3,449,211.75 USD | 1,686,837.33 USD | 1,762,374.42 USD | -75,537.08 USD | `-2.19%` | `9B / 14S` |

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
| `5m` | 1,070,000.00 USD | -1,100,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,770,000.00 USD | -1,700,000.00 USD | **`ACCUMULATION`** |
| `30m` | 3,430,000.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `1h` | 7,230,000.00 USD | -6,630,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,320,000.00 USD | 550,270.00 USD | **`ACCUMULATION`** |
| `4h` | 3,750,000.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `6h` | 3,760,000.00 USD | 1,520,000.00 USD | **`ACCUMULATION`** |
| `8h` | 4,160,000.00 USD | 1,090,000.00 USD | **`ACCUMULATION`** |
| `12h` | 3,680,000.00 USD | 1,560,000.00 USD | **`ACCUMULATION`** |
| `24h` | 6,220,000.00 USD | 3,960,000.00 USD | **`ACCUMULATION`** |
| `1w` | -569,350.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `30d` | -19,410,000.00 USD | 5,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.07M` | 15m=`+1.77M` | 1h=`+7.23M` | 24h=`+6.22M`
* Futures Capital Netflows: 5m=`-1.10M` | 15m=`-1.70M` | 1h=`-6.63M` | 24h=`+3.96M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3384` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3246` (Risk Distance: `0.0138` pts)
  * +2.5R Take Profit: `0.3730`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3534` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3672` (Risk Distance: `0.0138` pts)
  * +2.5R Take Profit: `0.3188`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3475`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
