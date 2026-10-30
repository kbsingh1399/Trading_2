# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3542` | **Live Ask Quote**: `0.3572` | **Mid Price**: `0.3557`
- **Spread Points**: `30.00` | **Spread BPS**: `84.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3539` | VWAP Z-Score: `+1.07` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0059` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `60.38` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3723` | Lower -3.00σ Band: `0.3160`
  * Upper +2.51σ Band: `0.3677` | Lower -2.51σ Band: `0.3206`
  * Upper +2.01σ Band: `0.3630` | Lower -2.01σ Band: `0.3253`
  * Upper +2.00σ Band: `0.3629` | Lower -2.00σ Band: `0.3254`
  * Upper +1.28σ Band: `0.3562` | Lower -1.28σ Band: `0.3321`
  * Upper +1.00σ Band: `0.3535` | Lower -1.00σ Band: `0.3348`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3527` | EMA-20=`0.3484` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3412` (Slope: `+0.0000`) | EMA-100=`0.3366`
  * Institutional Anchors: EMA-144=`0.3348` | EMA-200=`0.3334` (Slope: `+0.7134`) | EMA-233=`0.3329`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3572` (Distance: `-0.40%`)
  * Point of Control (POC) = `0.3512` (Distance: `+1.29%`)
  * Value Area Low (VAL) = `0.3447` (Distance: `+3.21%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3460` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3571` | Low=`0.3543`
  * New York Session (13:00-21:00 UTC): High=`0.3578` | Low=`0.3536`
  * Initial Balance (First Hour): IB High=`0.3568` | IB Low=`0.3546`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3543` - `0.3571`
  * Optimal Trade Entry (OTE 0.705): `0.3564`
  * Structural Invalidation Anchor (0.786): `0.3585`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3559` | `0.3568` | `0.3538` | `0.3566` | `3,301,616` | 1,172,941.29 USD | -4,242.27 USD | `-0.36%` | 6,799,977.28 USD | `-0.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.3567` | `0.3573` | `0.3545` | `0.3551` | `3,018,175` | 1,074,525.47 USD | 55,599.43 USD | `+5.17%` | 6,855,576.71 USD | `-0.39` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.3551` | `0.3568` | `0.3550` | `0.3557` | `1,090,994` | 388,361.27 USD | 47,098.81 USD | `+12.13%` | 6,902,675.52 USD | `-0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3590` | `0.3608` | `0.3547` | `0.3557` | `16,678,989` | 5,984,969.75 USD | 872,836.23 USD | `+14.58%` | 6,872,029.02 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3557` | `0.3597` | `0.3516` | `0.3559` | `19,401,131` | 6,905,900.10 USD | -67,809.47 USD | `-0.98%` | 6,804,219.56 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3559` | `0.3573` | `0.3538` | `0.3556` | `7,414,757` | 2,637,240.58 USD | 98,551.25 USD | `+3.74%` | 6,902,770.80 USD | `-0.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3478` | `0.3565` | `0.3413` | `0.3533` | `139,891,995` | 48,962,803.05 USD | 2,891,075.17 USD | `+5.90%` | 3,983,481.65 USD | `+2.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3533` | `0.3604` | `0.3498` | `0.3579` | `113,009,587` | 40,089,855.22 USD | 1,802,077.87 USD | `+4.50%` | 5,785,559.52 USD | `+1.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3579` | `0.3608` | `0.3516` | `0.3557` | `60,978,003` | 21,790,088.27 USD | 1,117,116.00 USD | `+5.13%` | 6,902,675.52 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3498` | `0.3557` | `173,987,590` | 61,879,943.48 USD | 2,919,193.87 USD | `+4.72%` | 6,314,380.44 USD | `+1.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 662,939.61 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,032,247.78 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3498` | `0.3557` | `173,987,590` | 61,879,943.48 USD | 2,919,193.87 USD | `+4.72%` | 6,314,380.44 USD | `+1.72` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3557`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `746` | `0xecb6...2b00` | `LONG` | 2,998,903.86 USD | `8,430,755.00` | `0.3340` | `0.3560` | `0.000000` | 183,124.76 USD | `+6.11%` | `10X Cross` |
| `1484` | `0xeadc...9d55` | `LONG` | 1,421,600.00 USD | `4,000,000.00` | `0.3421` | `0.3560` | `0.000000` | 53,121.91 USD | `+3.74%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3296` | 8,035.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.04K USD at 0.3296 USD [API] | `2026-10-28 21:03:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3591` (Vol: 1,400,000.00 USD, Dist: `+1.28%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--8.39%`)
  * 48H Horizon: Short MP=`0.3591` (Vol: 1,400,000.00 USD, Dist: `+1.28%`) | Long MP=`0.3249` (Vol: 801,900.00 USD, Dist: `--8.39%`)
  * 3D Horizon: Short MP=`0.3588` (Vol: 1,300,000.00 USD, Dist: `+1.18%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--8.39%`)
  * 7D Horizon: Short MP=`0.3588` (Vol: 1,300,000.00 USD, Dist: `+1.18%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--8.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0835` | 173.60 USD | 437,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 3,450.00 USD | 437,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 137.80 USD | 434,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 549.04 USD | 433,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 433,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 174.83 USD | 432,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,250.00 USD | 432,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,480.00 USD | 431,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 10,710.00 USD | 426,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 415,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 414,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 3,450.00 USD | 394,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,680.00 USD | 391,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 471.50 USD | 379,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 378,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,450.00 USD | 377,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 175.37 USD | 373,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 373,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1855` | 40,580.00 USD | 373,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 112.59 USD | 332,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1945` | 274.44 USD | 332,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 635.20 USD | 332,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2075` | 187.58 USD | 331,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 331,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 744.54 USD | 329,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 329,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,080.00 USD | 324,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,380.00 USD | 322,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 188.56 USD | 320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 1,700.00 USD | 319,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 1,140.00 USD | 318,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 5,730.00 USD | 316,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 311,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 310,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 174.12 USD | 309,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 139.92 USD | 309,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 309,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 308,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 2,690.00 USD | 307,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2495` | 2,980.00 USD | 305,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,220.00 USD | 302,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 301,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 302.96 USD | 299,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 14,000.00 USD | 299,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 108.56 USD | 285,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,970.00 USD | 285,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 193.75 USD | 277,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 27,410.00 USD | 277,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 3,170.00 USD | 249,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 246,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 84,780.00 USD | 246,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 5,770.00 USD | 161,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 516.34 USD | 155,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,060.00 USD | 155,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 142,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 748.23 USD | 135,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 135,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 120,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 118,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 118,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 24,310,000.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 117,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 3,540.00 USD | 116,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 213.81 USD | 113,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 24,230,000.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 24,170,000.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 112,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 24,090,000.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,950,000.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2971` | 23,720,000.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 23,460,000.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 23,350,000.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 23,130,000.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,980,000.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 1,800.00 USD | 112,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3001` | 21,260,000.00 USD | 21,260,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 3,520.00 USD | 111,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 21,260,000.00 USD | 21,260,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,970,000.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,530.00 USD | 107,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 494.28 USD | 97,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 21,200,000.00 USD | 21,200,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 589.40 USD | 96,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 267.35 USD | 95,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 21,160,000.00 USD | 21,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 22,930,000.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 21,080,000.00 USD | 21,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 22,880,000.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 138.70 USD | 95,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 21,010,000.00 USD | 21,010,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 22,880,000.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,890.00 USD | 95,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 20,950,000.00 USD | 20,950,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 22,810,000.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 20,870,000.00 USD | 20,870,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 22,800,000.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 20,840,000.00 USD | 20,840,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 22,790,000.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 20,840,000.00 USD | 20,840,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 22,690,000.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 80,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3091` | 20,820,000.00 USD | 20,820,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 22,690,000.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 292.48 USD | 73,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 20,820,000.00 USD | 20,820,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 22,680,000.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 20,820,000.00 USD | 20,820,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 22,660,000.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 22,530,000.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 22,520,000.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 658.82 USD | 73,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3121` | 22,520,000.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 13,990.00 USD | 73,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 20,710,000.00 USD | 20,710,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 22,360,000.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 20,680,000.00 USD | 20,680,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 22,340,000.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 20,690.00 USD | 59,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 20,630,000.00 USD | 20,630,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 22,340,000.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 20,630,000.00 USD | 20,630,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 22,330,000.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 7,370.00 USD | 38,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3151` | 20,630,000.00 USD | 20,630,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 22,020,000.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 30,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 21,760,000.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 20,590,000.00 USD | 20,590,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 21,220,000.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 30,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 20,440,000.00 USD | 20,440,000.00 USD | 84,050.00 USD | 16,200.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 20,330,000.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 20,300,000.00 USD | 20,300,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 19,470,000.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 29,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3181` | 20,220,000.00 USD | 20,220,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 19,140,000.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 19,670,000.00 USD | 19,670,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 18,190,000.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 17,720,000.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 109.59 USD | 28,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3199` | 19,400,000.00 USD | 19,400,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 19,350,000.00 USD | 19,350,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 17,420,000.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 19,050,000.00 USD | 19,050,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 17,320,000.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 18,890,000.00 USD | 18,890,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 16,460,000.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 18,800,000.00 USD | 18,800,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 16,010,000.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 18,510,000.00 USD | 18,510,000.00 USD | 140,560.00 USD | 81,070.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 15,080,000.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 18,080,000.00 USD | 18,080,000.00 USD | 129,720.00 USD | 77,760.00 USD | 168,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 13,630,000.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 28,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3241` | 17,710,000.00 USD | 17,710,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 11,910,000.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 17,510,000.00 USD | 17,510,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 11,100,000.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 16,520,000.00 USD | 16,520,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 9,770,000.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 129.22 USD | 17,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 15,150,000.00 USD | 15,150,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 8,440,000.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 8,050,000.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3265` | 464.94 USD | 17,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3271` | 14,630,000.00 USD | 14,630,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 7,860,000.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3277` | 14,170,000.00 USD | 14,170,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 7,660,000.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 10,240.00 USD | 16,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 13,700,000.00 USD | 13,700,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 13,500,000.00 USD | 13,500,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 7,270,000.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 7,240,000.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3305` | 3,420.00 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3307` | 13,420,000.00 USD | 13,420,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 7,170,000.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 13,210,000.00 USD | 13,210,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 6,830,000.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 12,500,000.00 USD | 12,500,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 11,990,000.00 USD | 11,990,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 6,580,000.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3331` | 11,660,000.00 USD | 11,660,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 6,450,000.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3335` | 1,300.00 USD | 3,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3337` | 11,660,000.00 USD | 11,660,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 10,770,000.00 USD | 10,770,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 1,730.00 USD | 1,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3349` | 10,600,000.00 USD | 10,600,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 5,610,000.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3355` | 10,260,000.00 USD | 10,260,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 5,380,000.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3361` | 10,170,000.00 USD | 10,170,000.00 USD | 177,350.00 USD | 81,810.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 5,120,000.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 9,840,000.00 USD | 9,840,000.00 USD | 237,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3373` | 9,600,000.00 USD | 9,600,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 4,880,000.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3375` | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3379` | 9,470,000.00 USD | 9,470,000.00 USD | 514,160.00 USD | 67,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 4,290,000.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 8,890,000.00 USD | 8,890,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 3,620,000.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3385` | 923.09 USD | 3,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3391` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3397` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,340,000.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 2,910,000.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 8,210,000.00 USD | 8,210,000.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3421` | 7,400,000.00 USD | 7,400,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3427` | 6,890,000.00 USD | 6,890,000.00 USD | 262,640.00 USD | 93,060.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3433` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 162,950.00 USD | 176,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3439` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 34,460.00 USD | 392,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3445` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 217,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3445` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3451` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 46,510.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3457` | 5,090,000.00 USD | 5,090,000.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3469` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3469` | 699,440.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3475` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3481` | 191,880.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3487` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3499` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3505` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3517` | 2,440,000.00 USD | 2,440,000.00 USD | 221,620.00 USD | 0.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3523` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3529` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3541` | 704,710.00 USD | 704,710.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3547` | 534,120.00 USD | 534,120.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 653,810.00 USD | 653,810.00 USD | 0.00 USD | 119,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3555` | 1,840.00 USD | 4,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3559` | 1,490,000.00 USD | 1,490,000.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 2,230,000.00 USD | 2,230,000.00 USD | 3,220.00 USD | 163,630.00 USD | 578,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3575` | 1,610.00 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3577` | 2,620,000.00 USD | 2,620,000.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 3,100,000.00 USD | 3,100,000.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3585` | 228.01 USD | 6,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3589` | 3,720,000.00 USD | 3,720,000.00 USD | 1,810.00 USD | 212,630.00 USD | 400,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3595` | 4,080,000.00 USD | 4,080,000.00 USD | 199,420.00 USD | 163,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 91,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 4,430,000.00 USD | 4,430,000.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3625` | 34,180.00 USD | 40,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3631` | 5,400,000.00 USD | 5,400,000.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 11,690.00 USD | 52,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 5,520,000.00 USD | 5,520,000.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 5,640,000.00 USD | 5,640,000.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 742.12 USD | 53,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 5,860,000.00 USD | 5,860,000.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 6,150,000.00 USD | 6,150,000.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3655` | 31,440.00 USD | 84,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3661` | 6,430,000.00 USD | 6,430,000.00 USD | 259,500.00 USD | 23,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3667` | 6,840,000.00 USD | 6,840,000.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 6,920,000.00 USD | 6,920,000.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3679` | 7,670,000.00 USD | 7,670,000.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 8,210,000.00 USD | 8,210,000.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 2,800.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3691` | 8,540,000.00 USD | 8,540,000.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 8,720,000.00 USD | 8,720,000.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 9,470,000.00 USD | 9,470,000.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 10,000,000.00 USD | 10,000,000.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 11,500,000.00 USD | 11,500,000.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3727` | 12,860,000.00 USD | 12,860,000.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 13,730,000.00 USD | 13,730,000.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 291.33 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3739` | 14,220,000.00 USD | 14,220,000.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 14,600,000.00 USD | 14,600,000.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 7,170.00 USD | 95,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 15,440,000.00 USD | 15,440,000.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3757` | 15,710,000.00 USD | 15,710,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 16,960,000.00 USD | 16,960,000.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3765` | 681.84 USD | 95,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3769` | 17,010,000.00 USD | 17,010,000.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3775` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3781` | 17,320,000.00 USD | 17,320,000.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 16,000.00 USD | 111,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 17,830,000.00 USD | 17,830,000.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 18,030,000.00 USD | 18,030,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 669,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3799` | 18,030,000.00 USD | 18,030,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 18,360,000.00 USD | 18,360,000.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3823` | 18,630,000.00 USD | 18,630,000.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3825` | 15,940.00 USD | 685,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3829` | 18,660,000.00 USD | 18,660,000.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3841` | 18,870,000.00 USD | 18,870,000.00 USD | 850.22 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 685,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3847` | 18,870,000.00 USD | 18,870,000.00 USD | 899.18 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3853` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3865` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3871` | 18,970,000.00 USD | 18,970,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3877` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3883` | 19,000,000.00 USD | 19,000,000.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3885` | 2,890.00 USD | 688,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3895` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 693,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 19,080,000.00 USD | 19,080,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3913` | 19,250,000.00 USD | 19,250,000.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 693,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 19,320,000.00 USD | 19,320,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 19,390,000.00 USD | 19,390,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3931` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3937` | 19,560,000.00 USD | 19,560,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 19,770,000.00 USD | 19,770,000.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 13,910.00 USD | 707,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 19,900,000.00 USD | 19,900,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 20,100,000.00 USD | 20,100,000.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 826,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3961` | 20,200,000.00 USD | 20,200,000.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3967` | 20,290,000.00 USD | 20,290,000.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 20,460,000.00 USD | 20,460,000.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3975` | 1,140.00 USD | 827,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3979` | 20,860,000.00 USD | 20,860,000.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 20,870,000.00 USD | 20,870,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3991` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3997` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 21,080,000.00 USD | 21,080,000.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4009` | 21,240,000.00 USD | 21,240,000.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4027` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4035` | 4,560.00 USD | 831,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.4045` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4045` | 115.69 USD | 831,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4065` | 2,010.00 USD | 833,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 1,790.00 USD | 835,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4115` | 1,100.00 USD | 836,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 33,800.00 USD | 870,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4175` | 599.53 USD | 871,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 1,010.00 USD | 872,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4215` | 222,080.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 24,200.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4265` | 201.31 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4285` | 313,010.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4305` | 82,110.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4315` | 4,170.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 91,950.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4395` | 71,540.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 3,820.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4485` | 66,060.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4505` | 175.24 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 5,570.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4535` | 467,070.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4595` | 318.89 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 103.98 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4965` | 20,840.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5025` | 236.17 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5145` | 297.38 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5185` | 72,070.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5435` | 637,800.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5505` | 2,290.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 6,360.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 8,270.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 728,400.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5745` | 213.14 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5765` | 56,240.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5945` | 7,370.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5995` | 53,170.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 29,540.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6165` | 24,660.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6305` | 281.83 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6555` | 16,230.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 565.58 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 1,210.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6745` | 83,190.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6805` | 2,770.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6885` | 263.01 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6935` | 414.71 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0715` | 577,690.00 USD | 0.00 USD | 117.40 USD | `-80.04%` | `1,642.00` |
| `Live` | `Long` | `0.0825` | 577,570.00 USD | 0.00 USD | 100.81 USD | `-76.96%` | `1,222.00` |
| `Live` | `Long` | `0.0885` | 577,470.00 USD | 0.00 USD | 183.99 USD | `-75.29%` | `2,079.00` |
| `Live` | `Long` | `0.0895` | 577,280.00 USD | 0.00 USD | 127.81 USD | `-75.01%` | `1,428.00` |
| `Live` | `Long` | `0.0965` | 577,160.00 USD | 0.00 USD | 928.04 USD | `-73.06%` | `9,617.00` |
| `Live` | `Long` | `0.1095` | 576,230.00 USD | 0.00 USD | 114.87 USD | `-69.43%` | `1,049.00` |
| `Live` | `Long` | `0.1145` | 576,110.00 USD | 0.00 USD | 8,790.00 USD | `-68.03%` | `76,797.00` |
| `Live` | `Long` | `0.1165` | 567,320.00 USD | 0.00 USD | 268.18 USD | `-67.47%` | `2,302.00` |
| `Live` | `Long` | `0.1175` | 567,050.00 USD | 0.00 USD | 124.32 USD | `-67.19%` | `1,058.00` |
| `Live` | `Long` | `0.1205` | 566,930.00 USD | 0.00 USD | 667.33 USD | `-66.35%` | `5,538.00` |
| `Live` | `Long` | `0.1295` | 566,260.00 USD | 0.00 USD | 130.67 USD | `-63.84%` | `1,009.00` |
| `Live` | `Long` | `0.1335` | 566,130.00 USD | 0.00 USD | 379.81 USD | `-62.72%` | `2,845.00` |
| `Live` | `Long` | `0.1485` | 565,750.00 USD | 0.00 USD | 209.53 USD | `-58.54%` | `1,411.00` |
| `Live` | `Long` | `0.1595` | 565,540.00 USD | 0.00 USD | 390.46 USD | `-55.46%` | `2,448.00` |
| `Live` | `Long` | `0.1655` | 565,150.00 USD | 0.00 USD | 3,310.00 USD | `-53.79%` | `20,000.00` |
| `Live` | `Long` | `0.1695` | 561,840.00 USD | 0.00 USD | 20,240.00 USD | `-52.67%` | `119,400.00` |
| `Live` | `Long` | `0.1725` | 541,600.00 USD | 0.00 USD | 652.74 USD | `-51.83%` | `3,784.00` |
| `Live` | `Long` | `0.1735` | 540,950.00 USD | 0.00 USD | 10,500.00 USD | `-51.56%` | `60,538.00` |
| `Live` | `Long` | `0.1745` | 530,450.00 USD | 0.00 USD | 7,640.00 USD | `-51.28%` | `43,802.00` |
| `Live` | `Long` | `0.1755` | 522,800.00 USD | 0.00 USD | 5,200.00 USD | `-51.00%` | `29,642.00` |
| `Live` | `Long` | `0.1765` | 517,600.00 USD | 0.00 USD | 256.98 USD | `-50.72%` | `1,456.00` |
| `Live` | `Long` | `0.1775` | 517,340.00 USD | 0.00 USD | 175.37 USD | `-50.44%` | `988.00` |
| `Live` | `Long` | `0.1785` | 517,170.00 USD | 0.00 USD | 208.67 USD | `-50.16%` | `1,169.00` |
| `Live` | `Long` | `0.1845` | 516,960.00 USD | 0.00 USD | 2,410.00 USD | `-48.48%` | `13,084.00` |
| `Live` | `Long` | `0.1885` | 514,550.00 USD | 0.00 USD | 36,500.00 USD | `-47.37%` | `193,636.00` |
| `Live` | `Long` | `0.1925` | 478,040.00 USD | 0.00 USD | 275.28 USD | `-46.25%` | `1,430.00` |
| `Live` | `Long` | `0.1945` | 477,770.00 USD | 0.00 USD | 42,550.00 USD | `-45.69%` | `218,745.00` |
| `Live` | `Long` | `0.1985` | 435,220.00 USD | 0.00 USD | 1,680.00 USD | `-44.57%` | `8,480.00` |
| `Live` | `Long` | `0.2175` | 433,540.00 USD | 0.00 USD | 1,520.00 USD | `-39.27%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 432,020.00 USD | 0.00 USD | 515.17 USD | `-38.71%` | `2,347.00` |
| `Live` | `Long` | `0.2255` | 431,500.00 USD | 0.00 USD | 4,590.00 USD | `-37.04%` | `20,360.00` |
| `Live` | `Long` | `0.2275` | 426,910.00 USD | 0.00 USD | 237.74 USD | `-36.48%` | `1,045.00` |
| `Live` | `Long` | `0.2285` | 426,670.00 USD | 0.00 USD | 107,530.00 USD | `-36.20%` | `470,586.00` |
| `Live` | `Long` | `0.2305` | 319,140.00 USD | 0.00 USD | 2,080.00 USD | `-35.64%` | `9,004.00` |
| `Live` | `Long` | `0.2315` | 317,070.00 USD | 0.00 USD | 411.84 USD | `-35.36%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 316,660.00 USD | 0.00 USD | 188.56 USD | `-35.08%` | `811.00` |
| `Live` | `Long` | `0.2335` | 316,470.00 USD | 0.00 USD | 2,430.00 USD | `-34.80%` | `10,412.00` |
| `Live` | `Long` | `0.2345` | 314,040.00 USD | 0.00 USD | 415.30 USD | `-34.52%` | `1,771.00` |
| `Live` | `Long` | `0.2355` | 313,620.00 USD | 0.00 USD | 5,730.00 USD | `-34.24%` | `24,311.00` |
| `Live` | `Long` | `0.2365` | 307,900.00 USD | 0.00 USD | 3,150.00 USD | `-33.96%` | `13,311.00` |
| `Live` | `Long` | `0.2375` | 304,750.00 USD | 0.00 USD | 1,030.00 USD | `-33.69%` | `4,347.00` |
| `Live` | `Long` | `0.2385` | 303,720.00 USD | 0.00 USD | 571.21 USD | `-33.41%` | `2,395.00` |
| `Live` | `Long` | `0.2395` | 303,140.00 USD | 0.00 USD | 2,860.00 USD | `-33.13%` | `11,927.00` |
| `Live` | `Long` | `0.2405` | 300,290.00 USD | 0.00 USD | 166.67 USD | `-32.85%` | `693.00` |
| `Live` | `Long` | `0.2425` | 300,120.00 USD | 0.00 USD | 139.92 USD | `-32.29%` | `577.00` |
| `Live` | `Long` | `0.2445` | 299,980.00 USD | 0.00 USD | 1,110.00 USD | `-31.73%` | `4,542.00` |
| `Live` | `Long` | `0.2455` | 298,870.00 USD | 0.00 USD | 466.70 USD | `-31.45%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 298,400.00 USD | 0.00 USD | 2,800.00 USD | `-31.17%` | `11,365.00` |
| `Live` | `Long` | `0.2495` | 295,600.00 USD | 0.00 USD | 11,930.00 USD | `-30.33%` | `47,833.00` |
| `Live` | `Long` | `0.2565` | 283,670.00 USD | 0.00 USD | 1,230.00 USD | `-28.38%` | `4,794.00` |
| `Live` | `Long` | `0.2605` | 282,440.00 USD | 0.00 USD | 14,000.00 USD | `-27.26%` | `53,741.00` |
| `Live` | `Long` | `0.2625` | 268,440.00 USD | 0.00 USD | 108.15 USD | `-26.70%` | `412.00` |
| `Live` | `Long` | `0.2655` | 268,330.00 USD | 0.00 USD | 2,970.00 USD | `-25.87%` | `11,204.00` |
| `Live` | `Long` | `0.2665` | 265,360.00 USD | 0.00 USD | 27,080.00 USD | `-25.59%` | `101,607.00` |
| `Live` | `Long` | `0.2685` | 238,280.00 USD | 0.00 USD | 322.74 USD | `-25.03%` | `1,202.00` |
| `Live` | `Long` | `0.2695` | 237,960.00 USD | 0.00 USD | 3,170.00 USD | `-24.75%` | `11,746.00` |
| `Live` | `Long` | `0.2715` | 234,790.00 USD | 0.00 USD | 411.32 USD | `-24.19%` | `1,515.00` |
| `Live` | `Long` | `0.2755` | 234,380.00 USD | 0.00 USD | 84,780.00 USD | `-23.07%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 149,600.00 USD | 0.00 USD | 182.04 USD | `-22.52%` | `656.00` |
| `Live` | `Long` | `0.2795` | 149,420.00 USD | 0.00 USD | 18,680.00 USD | `-21.96%` | `66,845.00` |
| `Live` | `Long` | `0.2805` | 130,730.00 USD | 0.00 USD | 6,860.00 USD | `-21.68%` | `24,441.00` |
| `Live` | `Long` | `0.2815` | 123,880.00 USD | 0.00 USD | 13,350.00 USD | `-21.40%` | `47,408.00` |
| `Live` | `Long` | `0.2825` | 110,530.00 USD | 0.00 USD | 3,700.00 USD | `-21.12%` | `13,109.00` |
| `Live` | `Long` | `0.2865` | 106,830.00 USD | 0.00 USD | 360.42 USD | `-20.00%` | `1,258.00` |
| `Live` | `Long` | `0.2915` | 106,470.00 USD | 0.00 USD | 591.45 USD | `-18.61%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 105,880.00 USD | 0.00 USD | 957.64 USD | `-18.33%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 104,920.00 USD | 0.00 USD | 3,540.00 USD | `-18.05%` | `12,054.00` |
| `Live` | `Long` | `0.2945` | 101,380.00 USD | 0.00 USD | 213.81 USD | `-17.77%` | `726.00` |
| `Live` | `Long` | `0.2955` | 101,170.00 USD | 0.00 USD | 125.29 USD | `-17.49%` | `424.00` |
| `Live` | `Long` | `0.2965` | 101,040.00 USD | 0.00 USD | 305.39 USD | `-17.21%` | `1,030.00` |
| `Live` | `Long` | `0.2995` | 100,740.00 USD | 0.00 USD | 762.23 USD | `-16.37%` | `2,545.00` |
| `Live` | `Long` | `0.3005` | 99,980.00 USD | 0.00 USD | 2,890.00 USD | `-16.09%` | `9,602.00` |
| `Live` | `Long` | `0.3015` | 97,090.00 USD | 0.00 USD | 10,650.00 USD | `-15.82%` | `35,336.00` |
| `Live` | `Long` | `0.3025` | 86,440.00 USD | 0.00 USD | 103.15 USD | `-15.54%` | `341.00` |
| `Live` | `Long` | `0.3035` | 86,330.00 USD | 0.00 USD | 485.90 USD | `-15.26%` | `1,601.00` |
| `Live` | `Long` | `0.3045` | 85,850.00 USD | 0.00 USD | 597.73 USD | `-14.98%` | `1,963.00` |
| `Live` | `Long` | `0.3055` | 85,250.00 USD | 0.00 USD | 138.70 USD | `-14.70%` | `454.00` |
| `Live` | `Long` | `0.3065` | 85,110.00 USD | 0.00 USD | 14,720.00 USD | `-14.42%` | `48,026.00` |
| `Live` | `Long` | `0.3075` | 70,390.00 USD | 0.00 USD | 5,920.00 USD | `-14.14%` | `19,262.00` |
| `Live` | `Long` | `0.3085` | 64,470.00 USD | 0.00 USD | 724.98 USD | `-13.86%` | `2,350.00` |
| `Live` | `Long` | `0.3095` | 63,740.00 USD | 0.00 USD | 292.48 USD | `-13.58%` | `945.00` |
| `Live` | `Long` | `0.3105` | 63,450.00 USD | 0.00 USD | 193.13 USD | `-13.30%` | `622.00` |
| `Live` | `Long` | `0.3115` | 63,260.00 USD | 0.00 USD | 658.82 USD | `-13.02%` | `2,115.00` |
| `Live` | `Long` | `0.3125` | 62,600.00 USD | 0.00 USD | 13,650.00 USD | `-12.74%` | `43,671.00` |
| `Live` | `Long` | `0.3135` | 48,950.00 USD | 0.00 USD | 20,930.00 USD | `-12.46%` | `66,753.00` |
| `Live` | `Long` | `0.3145` | 28,020.00 USD | 0.00 USD | 447.53 USD | `-12.19%` | `1,423.00` |
| `Live` | `Long` | `0.3155` | 27,580.00 USD | 0.00 USD | 578.94 USD | `-11.91%` | `1,835.00` |
| `Live` | `Long` | `0.3165` | 27,000.00 USD | 0.00 USD | 914.05 USD | `-11.63%` | `2,888.00` |
| `Live` | `Long` | `0.3175` | 26,080.00 USD | 0.00 USD | 938.85 USD | `-11.35%` | `2,957.00` |
| `Live` | `Long` | `0.3185` | 25,150.00 USD | 0.00 USD | 109.25 USD | `-11.07%` | `343.00` |
| `Live` | `Long` | `0.3195` | 25,040.00 USD | 0.00 USD | 1,780.00 USD | `-10.79%` | `5,572.00` |
| `Live` | `Long` | `0.3245` | 23,260.00 USD | 0.00 USD | 576.31 USD | `-9.39%` | `1,776.00` |
| `Live` | `Long` | `0.3255` | 22,680.00 USD | 0.00 USD | 312.48 USD | `-9.11%` | `960.00` |
| `Live` | `Long` | `0.3265` | 22,370.00 USD | 0.00 USD | 464.94 USD | `-8.83%` | `1,424.00` |
| `Live` | `Long` | `0.3275` | 21,900.00 USD | 0.00 USD | 130.02 USD | `-8.56%` | `397.00` |
| `Live` | `Long` | `0.3285` | 21,770.00 USD | 0.00 USD | 3,010.00 USD | `-8.28%` | `9,175.00` |
| `Live` | `Long` | `0.3305` | 18,760.00 USD | 0.00 USD | 3,300.00 USD | `-7.72%` | `9,995.00` |
| `Live` | `Long` | `0.3335` | 15,450.00 USD | 0.00 USD | 6,080.00 USD | `-6.88%` | `18,236.00` |
| `Live` | `Long` | `0.3345` | 9,370.00 USD | 0.00 USD | 7,050.00 USD | `-6.60%` | `21,090.00` |
| `Live` | `Long` | `0.3365` | 2,320.00 USD | 0.00 USD | 575.08 USD | `-6.04%` | `1,709.00` |
| `Live` | `Long` | `0.3375` | 1,740.00 USD | 0.00 USD | 784.69 USD | `-5.76%` | `2,325.00` |
| `Live` | `Long` | `0.3385` | 958.74 USD | 0.00 USD | 116.78 USD | `-5.48%` | `345.00` |
| `Live` | `Long` | `0.3395` | 841.96 USD | 0.00 USD | 841.96 USD | `-5.20%` | `2,480.00` |
| `Live` | `Short` | `0.3645` | 44,110.00 USD | 44,110.00 USD | 0.00 USD | `+1.78%` | `121,025.00` |
| `Live` | `Short` | `0.3675` | 46,470.00 USD | 2,360.00 USD | 0.00 USD | `+2.61%` | `6,413.00` |
| `Live` | `Short` | `0.3685` | 50,210.00 USD | 3,740.00 USD | 0.00 USD | `+2.89%` | `10,160.00` |
| `Live` | `Short` | `0.3715` | 52,910.00 USD | 2,690.00 USD | 0.00 USD | `+3.73%` | `7,251.00` |
| `Live` | `Short` | `0.3725` | 53,880.00 USD | 973.34 USD | 0.00 USD | `+4.01%` | `2,613.00` |
| `Live` | `Short` | `0.3735` | 61,540.00 USD | 7,660.00 USD | 0.00 USD | `+4.29%` | `20,500.00` |
| `Live` | `Short` | `0.3745` | 85,360.00 USD | 23,830.00 USD | 0.00 USD | `+4.57%` | `63,619.00` |
| `Live` | `Short` | `0.3755` | 94,900.00 USD | 9,540.00 USD | 0.00 USD | `+4.85%` | `25,396.00` |
| `Live` | `Short` | `0.3765` | 100,860.00 USD | 5,960.00 USD | 0.00 USD | `+5.13%` | `15,830.00` |
| `Live` | `Short` | `0.3775` | 133,160.00 USD | 32,300.00 USD | 0.00 USD | `+5.41%` | `85,568.00` |
| `Live` | `Short` | `0.3785` | 133,270.00 USD | 104.47 USD | 0.00 USD | `+5.68%` | `276.00` |
| `Live` | `Short` | `0.3795` | 691,160.00 USD | 557,900.00 USD | 0.00 USD | `+5.96%` | `1,470,083.00` |
| `Live` | `Short` | `0.3835` | 725,220.00 USD | 34,060.00 USD | 0.00 USD | `+7.08%` | `88,808.00` |
| `Live` | `Short` | `0.3845` | 725,340.00 USD | 115.35 USD | 0.00 USD | `+7.36%` | `300.00` |
| `Live` | `Short` | `0.3905` | 730,100.00 USD | 4,770.00 USD | 0.00 USD | `+9.04%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 731,410.00 USD | 1,310.00 USD | 0.00 USD | `+9.31%` | `3,348.00` |
| `Live` | `Short` | `0.3935` | 732,180.00 USD | 766.93 USD | 0.00 USD | `+9.87%` | `1,949.00` |
| `Live` | `Short` | `0.3945` | 733,670.00 USD | 1,490.00 USD | 0.00 USD | `+10.15%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 852,100.00 USD | 118,430.00 USD | 0.00 USD | `+10.43%` | `299,436.00` |
| `Live` | `Short` | `0.3965` | 853,680.00 USD | 1,580.00 USD | 0.00 USD | `+10.71%` | `3,992.00` |
| `Live` | `Short` | `0.4005` | 898,680.00 USD | 45,000.00 USD | 0.00 USD | `+11.83%` | `112,367.00` |
| `Live` | `Short` | `0.4065` | 900,130.00 USD | 1,440.00 USD | 0.00 USD | `+13.50%` | `3,552.00` |
| `Live` | `Short` | `0.4095` | 901,100.00 USD | 973.79 USD | 0.00 USD | `+14.34%` | `2,378.00` |
| `Live` | `Short` | `0.4105` | 901,290.00 USD | 193.76 USD | 0.00 USD | `+14.62%` | `472.00` |
| `Live` | `Short` | `0.4145` | 902,110.00 USD | 812.42 USD | 0.00 USD | `+15.74%` | `1,960.00` |
| `Live` | `Short` | `0.4175` | 902,700.00 USD | 599.53 USD | 0.00 USD | `+16.57%` | `1,436.00` |
| `Live` | `Short` | `0.4185` | 907,470.00 USD | 4,760.00 USD | 0.00 USD | `+16.85%` | `11,384.00` |
| `Live` | `Short` | `0.4265` | 908,210.00 USD | 740.40 USD | 0.00 USD | `+19.09%` | `1,736.00` |
| `Live` | `Short` | `0.4295` | 908,640.00 USD | 432.94 USD | 0.00 USD | `+19.93%` | `1,008.00` |
| `Live` | `Short` | `0.4305` | 990,750.00 USD | 82,110.00 USD | 0.00 USD | `+20.20%` | `190,735.00` |
| `Live` | `Short` | `0.4345` | 1,060,000.00 USD | 70,730.00 USD | 0.00 USD | `+21.32%` | `162,775.00` |
| `Live` | `Short` | `0.4385` | 1,060,000.00 USD | 442.01 USD | 0.00 USD | `+22.44%` | `1,008.00` |
| `Live` | `Short` | `0.4425` | 1,060,000.00 USD | 378.34 USD | 0.00 USD | `+23.56%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,060,000.00 USD | 307.39 USD | 0.00 USD | `+24.39%` | `690.00` |
| `Live` | `Short` | `0.4465` | 1,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+24.67%` | `2,284.00` |
| `Live` | `Short` | `0.4475` | 1,070,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.95%` | `4,163.00` |
| `Live` | `Short` | `0.4485` | 1,130,000.00 USD | 65,760.00 USD | 0.00 USD | `+25.23%` | `146,614.00` |
| `Live` | `Short` | `0.4495` | 1,130,000.00 USD | 1,560.00 USD | 0.00 USD | `+25.51%` | `3,464.00` |
| `Live` | `Short` | `0.4525` | 1,140,000.00 USD | 5,560.00 USD | 0.00 USD | `+26.35%` | `12,290.00` |
| `Live` | `Short` | `0.4535` | 1,140,000.00 USD | 1,140.00 USD | 0.00 USD | `+26.63%` | `2,519.00` |
| `Live` | `Short` | `0.4585` | 1,150,000.00 USD | 8,340.00 USD | 0.00 USD | `+28.02%` | `18,187.00` |
| `Live` | `Short` | `0.4595` | 1,170,000.00 USD | 19,280.00 USD | 0.00 USD | `+28.30%` | `41,969.00` |
| `Live` | `Short` | `0.4665` | 1,450,000.00 USD | 279,990.00 USD | 0.00 USD | `+30.26%` | `600,198.00` |
| `Live` | `Short` | `0.4735` | 1,460,000.00 USD | 8,060.00 USD | 0.00 USD | `+32.21%` | `17,027.00` |
| `Live` | `Short` | `0.4795` | 1,460,000.00 USD | 483.34 USD | 0.00 USD | `+33.89%` | `1,008.00` |
| `Live` | `Short` | `0.4895` | 1,460,000.00 USD | 103.28 USD | 0.00 USD | `+36.68%` | `211.00` |
| `Live` | `Short` | `0.4905` | 1,460,000.00 USD | 841.21 USD | 0.00 USD | `+36.96%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,460,000.00 USD | 5,130.00 USD | 0.00 USD | `+37.24%` | `10,430.00` |
| `Live` | `Short` | `0.5005` | 1,460,000.00 USD | 2,740.00 USD | 0.00 USD | `+39.75%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 1,460,000.00 USD | 235.71 USD | 0.00 USD | `+40.03%` | `470.00` |
| `Live` | `Short` | `0.5115` | 1,470,000.00 USD | 295.65 USD | 0.00 USD | `+42.82%` | `578.00` |
| `Live` | `Short` | `0.5295` | 1,940,000.00 USD | 476,550.00 USD | 0.00 USD | `+47.85%` | `900,000.00` |
| `Live` | `Short` | `0.5305` | 2,670,000.00 USD | 729,000.00 USD | 0.00 USD | `+48.13%` | `1,374,173.00` |
| `Live` | `Short` | `0.5335` | 2,670,000.00 USD | 668.48 USD | 0.00 USD | `+48.96%` | `1,253.00` |
| `Live` | `Short` | `0.5445` | 2,670,000.00 USD | 2,260.00 USD | 0.00 USD | `+52.04%` | `4,154.00` |
| `Live` | `Short` | `0.5485` | 2,680,000.00 USD | 1,600.00 USD | 0.00 USD | `+53.15%` | `2,912.00` |
| `Live` | `Short` | `0.5555` | 2,720,000.00 USD | 41,110.00 USD | 0.00 USD | `+55.11%` | `74,000.00` |
| `Live` | `Short` | `0.5585` | 2,720,000.00 USD | 742.25 USD | 0.00 USD | `+55.94%` | `1,329.00` |
| `Live` | `Short` | `0.5605` | 2,730,000.00 USD | 8,270.00 USD | 0.00 USD | `+56.50%` | `14,763.00` |
| `Live` | `Short` | `0.5615` | 2,730,000.00 USD | 140.38 USD | 0.00 USD | `+56.78%` | `250.00` |
| `Live` | `Short` | `0.5665` | 2,780,000.00 USD | 54,960.00 USD | 0.00 USD | `+58.18%` | `97,008.00` |
| `Live` | `Short` | `0.5815` | 3,530,000.00 USD | 754,350.00 USD | 0.00 USD | `+62.37%` | `1,297,248.00` |
| `Live` | `Short` | `0.6075` | 3,540,000.00 USD | 1,080.00 USD | 0.00 USD | `+69.63%` | `1,776.00` |
| `Live` | `Short` | `0.6155` | 3,540,000.00 USD | 3,930.00 USD | 0.00 USD | `+71.86%` | `6,380.00` |
| `Live` | `Short` | `0.6165` | 3,560,000.00 USD | 24,660.00 USD | 0.00 USD | `+72.14%` | `40,000.00` |
| `Live` | `Short` | `0.6275` | 3,570,000.00 USD | 5,910.00 USD | 0.00 USD | `+75.21%` | `9,411.00` |
| `Live` | `Short` | `0.6285` | 3,570,000.00 USD | 1,140.00 USD | 0.00 USD | `+75.49%` | `1,808.00` |
| `Live` | `Short` | `0.6305` | 3,600,000.00 USD | 33,140.00 USD | 0.00 USD | `+76.05%` | `52,566.00` |
| `Live` | `Short` | `0.6325` | 4,000,000.00 USD | 391,910.00 USD | 0.00 USD | `+76.61%` | `619,615.00` |
| `Live` | `Short` | `0.6335` | 4,000,000.00 USD | 1,040.00 USD | 0.00 USD | `+76.89%` | `1,642.00` |
| `Live` | `Short` | `0.6475` | 4,000,000.00 USD | 391.74 USD | 0.00 USD | `+80.80%` | `605.00` |
| `Live` | `Short` | `0.6525` | 4,000,000.00 USD | 952.65 USD | 0.00 USD | `+82.19%` | `1,460.00` |
| `Live` | `Short` | `0.6545` | 4,000,000.00 USD | 706.21 USD | 0.00 USD | `+82.75%` | `1,079.00` |
| `Live` | `Short` | `0.6625` | 4,000,000.00 USD | 2,060.00 USD | 0.00 USD | `+84.98%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 4,000,000.00 USD | 2,530.00 USD | 0.00 USD | `+85.26%` | `3,811.00` |
| `Live` | `Short` | `0.6645` | 4,010,000.00 USD | 1,210.00 USD | 0.00 USD | `+85.54%` | `1,821.00` |
| `Live` | `Short` | `0.6665` | 4,010,000.00 USD | 819.80 USD | 0.00 USD | `+86.10%` | `1,230.00` |
| `Live` | `Short` | `0.6695` | 4,080,000.00 USD | 78,850.00 USD | 0.00 USD | `+86.94%` | `117,778.00` |
| `Live` | `Short` | `0.6715` | 4,100,000.00 USD | 10,810.00 USD | 0.00 USD | `+87.50%` | `16,100.00` |
| `Live` | `Short` | `0.6725` | 4,110,000.00 USD | 16,650.00 USD | 0.00 USD | `+87.78%` | `24,756.00` |
| `Live` | `Short` | `0.6735` | 4,200,000.00 USD | 83,060.00 USD | 0.00 USD | `+88.05%` | `123,332.00` |
| `Live` | `Short` | `0.6855` | 4,970,000.00 USD | 776,470.00 USD | 0.00 USD | `+91.41%` | `1,132,705.00` |
| `Live` | `Short` | `0.6875` | 4,970,000.00 USD | 262.62 USD | 0.00 USD | `+91.96%` | `382.00` |
| `Live` | `Short` | `0.6935` | 4,970,000.00 USD | 1,420.00 USD | 0.00 USD | `+93.64%` | `2,049.00` |
| `Live` | `Short` | `0.6985` | 5,000,000.00 USD | 27,940.00 USD | 0.00 USD | `+95.04%` | `40,000.00` |
| `Live` | `Short` | `0.7015` | 5,000,000.00 USD | 106.63 USD | 0.00 USD | `+95.87%` | `152.00` |
| `Live` | `Short` | `0.7095` | 5,010,000.00 USD | 4,190.00 USD | 0.00 USD | `+98.11%` | `5,899.00` |
| `Live` | `Short` | `0.7165` | 5,010,000.00 USD | 8,890.00 USD | 0.00 USD | `+100.06%` | `12,403.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 1,220,000.00 USD | 0.00 USD | 198.45 USD | `-73.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 1,220,000.00 USD | 0.00 USD | 330.26 USD | `-60.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 1,220,000.00 USD | 0.00 USD | 6,100.00 USD | `-49.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,210,000.00 USD | 0.00 USD | 1,750.00 USD | `-43.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,210,000.00 USD | 0.00 USD | 2,220.00 USD | `-41.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,210,000.00 USD | 0.00 USD | 121.70 USD | `-35.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,210,000.00 USD | 0.00 USD | 705.61 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 1,210,000.00 USD | 0.00 USD | 159.20 USD | `-34.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,210,000.00 USD | 0.00 USD | 1,200.00 USD | `-32.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,210,000.00 USD | 0.00 USD | 127.51 USD | `-32.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,210,000.00 USD | 0.00 USD | 1,850.00 USD | `-30.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 1,210,000.00 USD | 0.00 USD | 41,500.00 USD | `-29.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 1,170,000.00 USD | 0.00 USD | 1,920.00 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 1,160,000.00 USD | 0.00 USD | 664.01 USD | `-27.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 1,160,000.00 USD | 0.00 USD | 954.98 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 1,160,000.00 USD | 0.00 USD | 103.56 USD | `-26.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 1,160,000.00 USD | 0.00 USD | 695.50 USD | `-25.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 1,160,000.00 USD | 0.00 USD | 1,630.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 1,160,000.00 USD | 0.00 USD | 1,470.00 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 1,160,000.00 USD | 0.00 USD | 101.94 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 1,160,000.00 USD | 0.00 USD | 3,260.00 USD | `-22.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 1,150,000.00 USD | 0.00 USD | 2,550.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 1,150,000.00 USD | 0.00 USD | 229.92 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 1,150,000.00 USD | 0.00 USD | 8,010.00 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 1,140,000.00 USD | 0.00 USD | 11,610.00 USD | `-18.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 1,130,000.00 USD | 0.00 USD | 111.19 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 1,130,000.00 USD | 0.00 USD | 326.86 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 1,130,000.00 USD | 0.00 USD | 2,710.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 1,130,000.00 USD | 0.00 USD | 335.56 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 1,130,000.00 USD | 0.00 USD | 919.50 USD | `-14.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 1,130,000.00 USD | 0.00 USD | 193.11 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 1,130,000.00 USD | 0.00 USD | 15,150.00 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 1,110,000.00 USD | 0.00 USD | 147.32 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 1,110,000.00 USD | 0.00 USD | 12,200.00 USD | `-13.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 1,100,000.00 USD | 0.00 USD | 6,530.00 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 1,090,000.00 USD | 0.00 USD | 524,570.00 USD | `-12.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 568,690.00 USD | 0.00 USD | 1,270.00 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 567,420.00 USD | 0.00 USD | 53,690.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 513,730.00 USD | 0.00 USD | 1,370.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 512,360.00 USD | 0.00 USD | 6,100.00 USD | `-11.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 506,270.00 USD | 0.00 USD | 850.90 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 505,420.00 USD | 0.00 USD | 1,040.00 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 504,370.00 USD | 0.00 USD | 6,220.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 498,150.00 USD | 0.00 USD | 9,840.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 488,310.00 USD | 0.00 USD | 43,570.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 444,740.00 USD | 0.00 USD | 131.90 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 444,610.00 USD | 0.00 USD | 4,710.00 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 439,890.00 USD | 0.00 USD | 3,220.00 USD | `-9.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 436,680.00 USD | 0.00 USD | 63,670.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 373,010.00 USD | 0.00 USD | 6,130.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 366,870.00 USD | 0.00 USD | 6,770.00 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 360,100.00 USD | 0.00 USD | 996.01 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 359,110.00 USD | 0.00 USD | 2,430.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 356,680.00 USD | 0.00 USD | 949.53 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 355,730.00 USD | 0.00 USD | 100.11 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 355,630.00 USD | 0.00 USD | 135.99 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 355,490.00 USD | 0.00 USD | 1,010.00 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 354,490.00 USD | 0.00 USD | 5,640.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 348,850.00 USD | 0.00 USD | 174,860.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 173,990.00 USD | 0.00 USD | 34,710.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 139,280.00 USD | 0.00 USD | 32,490.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 106,790.00 USD | 0.00 USD | 157.74 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 106,630.00 USD | 0.00 USD | 3,380.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 103,250.00 USD | 0.00 USD | 5,290.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 97,970.00 USD | 0.00 USD | 13,710.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 84,250.00 USD | 0.00 USD | 359.28 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 83,890.00 USD | 0.00 USD | 828.18 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 83,070.00 USD | 0.00 USD | 1,950.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 81,120.00 USD | 0.00 USD | 3,980.00 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 77,140.00 USD | 0.00 USD | 2,460.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 74,680.00 USD | 0.00 USD | 323.87 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3485` | 74,360.00 USD | 0.00 USD | 305.29 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3495` | 74,050.00 USD | 0.00 USD | 8,090.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 65,960.00 USD | 0.00 USD | 314.75 USD | `-2.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3515` | 65,650.00 USD | 0.00 USD | 3,810.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3525` | 61,840.00 USD | 0.00 USD | 19,380.00 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3535` | 42,450.00 USD | 0.00 USD | 494.90 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3545` | 41,960.00 USD | 0.00 USD | 769.97 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3555` | 41,190.00 USD | 0.00 USD | 969.45 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3565` | 40,220.00 USD | 0.00 USD | 39,430.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3575` | 791.15 USD | 0.00 USD | 791.15 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 1,920.00 USD | 1,920.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 2,960.00 USD | 1,030.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 5,900.00 USD | 2,940.00 USD | 0.00 USD | `+0.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 6,110.00 USD | 216.65 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 7,460.00 USD | 1,350.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 25,070.00 USD | 17,610.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 36,070.00 USD | 10,990.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 45,340.00 USD | 9,270.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 45,440.00 USD | 104.65 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 59,780.00 USD | 14,330.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 65,970.00 USD | 6,190.00 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 66,140.00 USD | 174.60 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 66,250.00 USD | 107.28 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 66,690.00 USD | 439.61 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 67,130.00 USD | 437.79 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 68,100.00 USD | 973.30 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 68,280.00 USD | 182.60 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 74,730.00 USD | 6,450.00 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 75,010.00 USD | 275.17 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 75,470.00 USD | 463.37 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 81,450.00 USD | 5,980.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 81,710.00 USD | 257.89 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 82,670.00 USD | 963.52 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 83,640.00 USD | 972.17 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 84,260.00 USD | 621.04 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 84,970.00 USD | 702.27 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 86,080.00 USD | 1,110.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 86,260.00 USD | 181.04 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 86,610.00 USD | 352.11 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 86,770.00 USD | 155.03 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 86,890.00 USD | 126.24 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 89,300.00 USD | 2,400.00 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 90,630.00 USD | 1,340.00 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 92,640.00 USD | 2,010.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 146,200.00 USD | 53,560.00 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 147,060.00 USD | 864.28 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 150,980.00 USD | 3,920.00 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 230,310.00 USD | 79,330.00 USD | 0.00 USD | `+12.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 231,510.00 USD | 1,200.00 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 232,710.00 USD | 1,200.00 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 232,850.00 USD | 138.07 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 234,120.00 USD | 1,270.00 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 234,450.00 USD | 331.63 USD | 0.00 USD | `+15.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 234,770.00 USD | 313.54 USD | 0.00 USD | `+16.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 234,950.00 USD | 186.70 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 235,280.00 USD | 325.75 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 235,580.00 USD | 299.19 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 274,150.00 USD | 38,580.00 USD | 0.00 USD | `+23.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 274,320.00 USD | 170.69 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 274,460.00 USD | 135.59 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 275,850.00 USD | 1,390.00 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 281,190.00 USD | 5,340.00 USD | 0.00 USD | `+26.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 361,950.00 USD | 80,770.00 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 362,120.00 USD | 169.22 USD | 0.00 USD | `+36.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 362,850.00 USD | 724.89 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 374,000.00 USD | 11,150.00 USD | 0.00 USD | `+39.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 375,930.00 USD | 1,930.00 USD | 0.00 USD | `+41.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 376,060.00 USD | 135.02 USD | 0.00 USD | `+47.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 376,300.00 USD | 240.85 USD | 0.00 USD | `+76.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 377,400.00 USD | 1,100.00 USD | 0.00 USD | `+76.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 391,010.00 USD | 13,610.00 USD | 0.00 USD | `+88.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 392,850.00 USD | 1,840.00 USD | 0.00 USD | `+89.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 393,840.00 USD | 991.76 USD | 0.00 USD | `+90.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 394,970.00 USD | 1,130.00 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7155` | 395,780.00 USD | 807.08 USD | 0.00 USD | `+99.78%` | `TACTICAL (Retail Cluster)` |

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
| `1D` | `0.3001` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3007` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD |
| `7D` | `0.3007` | 22,970,000.00 USD | 0.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3019` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3031` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 21,200,000.00 USD | 0.00 USD | 21,200,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD |
| `1D` | `0.3049` | 21,160,000.00 USD | 0.00 USD | 21,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3049` | 22,930,000.00 USD | 0.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3055` | 21,080,000.00 USD | 0.00 USD | 21,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 21,010,000.00 USD | 0.00 USD | 21,010,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 22,880,000.00 USD | 0.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3067` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 22,810,000.00 USD | 0.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3073` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3073` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 22,790,000.00 USD | 0.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3085` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3085` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3103` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 22,660,000.00 USD | 0.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `7D` | `0.3109` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3121` | 22,520,000.00 USD | 0.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 20,710,000.00 USD | 0.00 USD | 20,710,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD |
| `7D` | `0.3127` | 22,360,000.00 USD | 0.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3133` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD |
| `7D` | `0.3139` | 22,340,000.00 USD | 0.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3145` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3145` | 22,330,000.00 USD | 0.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3151` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 22,020,000.00 USD | 0.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3157` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD |
| `7D` | `0.3157` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3163` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD |
| `7D` | `0.3163` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD |
| `1D` | `0.3169` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 84,050.00 USD | 16,200.00 USD | 38,410.00 USD |
| `7D` | `0.3169` | 20,330,000.00 USD | 0.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD |
| `1D` | `0.3175` | 20,300,000.00 USD | 0.00 USD | 20,300,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD |
| `7D` | `0.3175` | 19,470,000.00 USD | 0.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD |
| `1D` | `0.3181` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD |
| `7D` | `0.3181` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD |
| `1D` | `0.3187` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD |
| `7D` | `0.3187` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3193` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `7D` | `0.3193` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3199` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 17,520,000.00 USD | 0.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3205` | 19,350,000.00 USD | 0.00 USD | 19,350,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD |
| `7D` | `0.3205` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3211` | 19,050,000.00 USD | 0.00 USD | 19,050,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD |
| `7D` | `0.3211` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3217` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3217` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3223` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD |
| `7D` | `0.3223` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3229` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 140,560.00 USD | 81,070.00 USD | 205,050.00 USD |
| `7D` | `0.3229` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD |
| `1D` | `0.3235` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 129,720.00 USD | 77,760.00 USD | 168,760.00 USD |
| `7D` | `0.3235` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD |
| `1D` | `0.3241` | 17,710,000.00 USD | 0.00 USD | 17,710,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD |
| `7D` | `0.3241` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD |
| `1D` | `0.3247` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD |
| `7D` | `0.3247` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3253` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD |
| `7D` | `0.3253` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3259` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3265` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD |
| `7D` | `0.3265` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3271` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD |
| `7D` | `0.3271` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3277` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3283` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD |
| `7D` | `0.3283` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3289` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3295` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `7D` | `0.3301` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3307` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD |
| `7D` | `0.3307` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3313` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD |
| `7D` | `0.3313` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3319` | 12,500,000.00 USD | 0.00 USD | 12,500,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD |
| `7D` | `0.3319` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3325` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD |
| `7D` | `0.3325` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD |
| `1D` | `0.3331` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3331` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD |
| `1D` | `0.3337` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD |
| `7D` | `0.3337` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD |
| `1D` | `0.3343` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3343` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `1D` | `0.3349` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 267,710.00 USD | 16,250.00 USD | 59,820.00 USD |
| `7D` | `0.3349` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3355` | 10,260,000.00 USD | 0.00 USD | 10,260,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 1,610.00 USD | 0.00 USD | 251,000.00 USD |
| `1D` | `0.3361` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 177,350.00 USD | 81,810.00 USD | 65,250.00 USD |
| `7D` | `0.3361` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3367` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 237,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3367` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3373` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 7,700.00 USD | 124,670.00 USD | 0.00 USD |
| `7D` | `0.3373` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3379` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 514,160.00 USD | 67,660.00 USD | 0.00 USD |
| `7D` | `0.3379` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3385` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD |
| `7D` | `0.3385` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3391` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD |
| `1D` | `0.3397` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD |
| `7D` | `0.3397` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD |
| `1D` | `0.3403` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD |
| `7D` | `0.3403` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3409` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD |
| `7D` | `0.3409` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD |
| `1D` | `0.3415` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD |
| `1D` | `0.3421` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD |
| `1D` | `0.3427` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 262,640.00 USD | 93,060.00 USD | 187,820.00 USD |
| `7D` | `0.3427` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3433` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 0.00 USD | 162,950.00 USD | 176,350.00 USD |
| `1D` | `0.3439` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 0.00 USD | 34,460.00 USD | 392,630.00 USD |
| `1D` | `0.3445` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 0.00 USD | 0.00 USD | 217,030.00 USD |
| `7D` | `0.3445` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3451` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 0.00 USD | 46,510.00 USD | 229,860.00 USD |
| `7D` | `0.3451` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3457` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 1,150.00 USD | 0.00 USD | 258,740.00 USD |
| `1D` | `0.3469` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 514,270.00 USD |
| `7D` | `0.3469` | 699,440.00 USD | 0.00 USD | 699,440.00 USD | 0.00 USD | 205,310.00 USD | 302,240.00 USD |
| `1D` | `0.3475` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 159,850.00 USD |
| `7D` | `0.3481` | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `7D` | `0.3485` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3487` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 356,270.00 USD |
| `1D` | `0.3499` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 664,810.00 USD |
| `1D` | `0.3505` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 352,700.00 USD |
| `1D` | `0.3511` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD |
| `1D` | `0.3517` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 221,620.00 USD | 0.00 USD | 434,060.00 USD |
| `1D` | `0.3523` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 459,710.00 USD |
| `7D` | `0.3523` | 277,410.00 USD | 277,410.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD |
| `1D` | `0.3541` | 704,710.00 USD | 0.00 USD | 704,710.00 USD | 0.00 USD | 0.00 USD | 704,710.00 USD |
| `7D` | `0.3541` | 929,350.00 USD | 929,350.00 USD | 0.00 USD | 651,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3544` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3547` | 534,120.00 USD | 534,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD |
| `1D` | `0.3553` | 653,810.00 USD | 653,810.00 USD | 0.00 USD | 0.00 USD | 119,690.00 USD | 0.00 USD |
| `1D` | `0.3559` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD |
| `1D` | `0.3571` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 3,220.00 USD | 163,630.00 USD | 578,320.00 USD |
| `1D` | `0.3577` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3583` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD |
| `7D` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD |
| `1D` | `0.3589` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 1,810.00 USD | 212,630.00 USD | 400,320.00 USD |
| `7D` | `0.3589` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 703,970.00 USD | 0.00 USD | 320,430.00 USD |
| `1D` | `0.3595` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 199,420.00 USD | 163,620.00 USD | 0.00 USD |
| `7D` | `0.3595` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 616,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3601` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD |
| `7D` | `0.3601` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 35,120.00 USD | 0.00 USD |
| `7D` | `0.3607` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 841,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3613` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 201,930.00 USD | 0.00 USD |
| `7D` | `0.3613` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 205,310.00 USD | 0.00 USD |
| `1D` | `0.3619` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 91,240.00 USD | 0.00 USD |
| `7D` | `0.3619` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD |
| `1D` | `0.3625` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3625` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3631` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3637` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD |
| `1D` | `0.3643` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD |
| `7D` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3649` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD |
| `7D` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3655` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD |
| `7D` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3661` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 259,500.00 USD | 23,260.00 USD | 0.00 USD |
| `7D` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3667` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD |
| `7D` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3673` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD |
| `7D` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3679` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD |
| `7D` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3685` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD |
| `7D` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD |
| `1D` | `0.3691` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD |
| `7D` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD |
| `1D` | `0.3697` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD |
| `7D` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD |
| `1D` | `0.3703` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD |
| `1D` | `0.3709` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD |
| `7D` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3715` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD |
| `7D` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3721` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD |
| `7D` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3727` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD |
| `7D` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3733` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3739` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD |
| `7D` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3745` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD |
| `7D` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3751` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD |
| `1D` | `0.3757` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD |
| `7D` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3763` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD |
| `7D` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3769` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD |
| `7D` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3775` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3781` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD |
| `7D` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3787` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD |
| `7D` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3793` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD |
| `7D` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3799` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3805` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD |
| `7D` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3823` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD |
| `7D` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD |
| `1D` | `0.3829` | 18,660,000.00 USD | 18,660,000.00 USD | 0.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD |
| `1D` | `0.3835` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 850.22 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3847` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 899.18 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3853` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3865` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD |
| `7D` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `1D` | `0.3871` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3877` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD |
| `7D` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3883` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3895` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD |
| `7D` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3907` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `1D` | `0.3913` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3919` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3925` | 19,390,000.00 USD | 19,390,000.00 USD | 0.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD |
| `7D` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `1D` | `0.3931` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `1D` | `0.3937` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD |
| `7D` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `1D` | `0.3943` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD |
| `7D` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `1D` | `0.3949` | 19,900,000.00 USD | 19,900,000.00 USD | 0.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD |
| `7D` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD |
| `1D` | `0.3955` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD |
| `7D` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD |
| `1D` | `0.3961` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD |
| `7D` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD |
| `1D` | `0.3967` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD |
| `7D` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD |
| `1D` | `0.3973` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD |
| `7D` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `1D` | `0.3979` | 20,860,000.00 USD | 20,860,000.00 USD | 0.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD |
| `7D` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD |
| `1D` | `0.3985` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD |
| `7D` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `1D` | `0.3991` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `7D` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD |
| `1D` | `0.3997` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD |
| `1D` | `0.4003` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD |
| `7D` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `1D` | `0.4009` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD |
| `7D` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD |
| `1D` | `0.4027` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.4045` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `410.27M` | Total OI Tokens: `1,151,852,411.8 TRX`
  * 1h OI Change: `+1.32%` | 4h OI Change: `+9.49%` | 24h OI Change: `+41.72%`
  * Exchange Breakdown: Binance=`115.39M` | Bybit=`86.31M` | OKX=`25.31M` | Hyperliquid=`19.12M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-857.87K` | Last 24h: `-591.71K` | Last 3d: `-625.30K` | Last 7d: `-857.35K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.3900%` | **USDT OKX** | `-0.8747%` |
| **USDT Bybit** | `-0.2302%` | **USDT KuCoin** | `-0.0406%` |
| **USDT MEXC** | `-0.3901%` | **USDT BingX** | `-0.5000%` |
| **USDT Gate** | `-0.2396%` | **USDT Bitget** | `-0.4081%` |
| **CoinM Binance** | `-0.6349%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `45.26%` | `54.74%` | `0.83` | 83,940,000.00 USD |
| `15M` | `Binance` | `43.34%` | `56.66%` | `0.76` | 31,400,000.00 USD |
| `15M` | `OKX` | `47.17%` | `52.83%` | `0.89` | 15,860,000.00 USD |
| `15M` | `Bybit` | `49.69%` | `50.31%` | `0.99` | 6,200,000.00 USD |
| `15M` | `KuCoin` | `49.22%` | `50.78%` | `0.97` | 4,040,000.00 USD |
| `15M` | `Gate` | `51.16%` | `48.84%` | `1.05` | 4,750,000.00 USD |
| `15M` | `Bitget` | `51.96%` | `48.04%` | `1.08` | 3,500,000.00 USD |
| `15M` | `BingX` | `51.89%` | `48.11%` | `1.08` | 2,720,000.00 USD |
| `15M` | `MEXC` | `39.75%` | `60.25%` | `0.66` | 6,840,000.00 USD |
| `15M` | `Bitunix` | `29.46%` | `70.54%` | `0.42` | 3,430,000.00 USD |
| `15M` | `Hyperliquid` | `52.76%` | `47.24%` | `1.12` | 2,120,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.63%` | `43.37%` | `1.31` | 511,920.00 USD |
| `15M` | `Crypto.com` | `48.08%` | `51.92%` | `0.93` | 212,030.00 USD |
| `15M` | `WhiteBIT` | `22.38%` | `77.62%` | `0.29` | 1,020,000.00 USD |
| `15M` | `HTX` | `48.54%` | `51.46%` | `0.94` | 83,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `72.27%` | `27.73%` | `2.61` | 359,990.00 USD |
| `15M` | `Aster` | `40.54%` | `59.46%` | `0.68` | 473,800.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `51.03%` | `48.97%` | `1.04` | 413,470.00 USD |
| `15M` | `Whale Positions` | `43.34%` | `56.66%` | `0.76` | 31,400,000.00 USD |
| `15M` | `Global Accounts` | `45.26%` | `54.74%` | `0.83` | 83,940,000.00 USD |
| `1H` | `TRX` | `45.05%` | `54.95%` | `0.82` | 257,730,000.00 USD |
| `1H` | `Binance` | `47.32%` | `52.68%` | `0.90` | 93,900,000.00 USD |
| `1H` | `OKX` | `45.81%` | `54.19%` | `0.85` | 33,750,000.00 USD |
| `1H` | `Bybit` | `42.23%` | `57.77%` | `0.73` | 39,600,000.00 USD |
| `1H` | `KuCoin` | `48.86%` | `51.14%` | `0.96` | 3,970,000.00 USD |
| `1H` | `Gate` | `40.45%` | `59.55%` | `0.68` | 6,040,000.00 USD |
| `1H` | `Bitget` | `48.25%` | `51.75%` | `0.93` | 20,410,000.00 USD |
| `1H` | `BingX` | `50.12%` | `49.88%` | `1.00` | 2,230,000.00 USD |
| `1H` | `MEXC` | `43.64%` | `56.36%` | `0.77` | 27,830,000.00 USD |
| `1H` | `Bitunix` | `50.27%` | `49.73%` | `1.01` | 7,360,000.00 USD |
| `1H` | `Hyperliquid` | `23.82%` | `76.18%` | `0.31` | 13,860,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `57.11%` | `42.89%` | `1.33` | 1,410,000.00 USD |
| `1H` | `Crypto.com` | `50.15%` | `49.85%` | `1.01` | 367,080.00 USD |
| `1H` | `WhiteBIT` | `90.49%` | `9.51%` | `9.52` | 2,490,000.00 USD |
| `1H` | `HTX` | `55.07%` | `44.93%` | `1.23` | 328,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `39.74%` | `60.26%` | `0.66` | 1,320,000.00 USD |
| `1H` | `Aster` | `40.12%` | `59.88%` | `0.67` | 1,920,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `29.9%` | `70.1%` | `0.43` | 979,720.00 USD |
| `1H` | `Whale Positions` | `47.32%` | `52.68%` | `0.90` | 93,900,000.00 USD |
| `1H` | `Global Accounts` | `45.05%` | `54.95%` | `0.82` | 257,730,000.00 USD |
| `4H` | `TRX` | `47.28%` | `52.72%` | `0.90` | 2,960,000,000.00 USD |
| `4H` | `Binance` | `49.43%` | `50.57%` | `0.98` | 1,160,000,000.00 USD |
| `4H` | `OKX` | `45.78%` | `54.22%` | `0.84` | 501,890,000.00 USD |
| `4H` | `Bybit` | `44.12%` | `55.88%` | `0.79` | 253,570,000.00 USD |
| `4H` | `KuCoin` | `47.98%` | `52.02%` | `0.92` | 37,900,000.00 USD |
| `4H` | `Gate` | `46.26%` | `53.74%` | `0.86` | 131,450,000.00 USD |
| `4H` | `Bitget` | `46.45%` | `53.55%` | `0.87` | 121,670,000.00 USD |
| `4H` | `BingX` | `42.58%` | `57.42%` | `0.74` | 129,700,000.00 USD |
| `4H` | `MEXC` | `44.33%` | `55.67%` | `0.80` | 221,090,000.00 USD |
| `4H` | `Bitunix` | `48.22%` | `51.78%` | `0.93` | 110,560,000.00 USD |
| `4H` | `Hyperliquid` | `34.69%` | `65.31%` | `0.53` | 147,460,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.88%` | `42.12%` | `1.37` | 40,050,000.00 USD |
| `4H` | `Crypto.com` | `47.76%` | `52.24%` | `0.91` | 7,100,000.00 USD |
| `4H` | `WhiteBIT` | `88.49%` | `11.51%` | `7.69` | 18,870,000.00 USD |
| `4H` | `HTX` | `47.6%` | `52.4%` | `0.91` | 5,310,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.77%` | `57.23%` | `0.75` | 21,570,000.00 USD |
| `4H` | `Aster` | `54.74%` | `45.26%` | `1.21` | 29,360,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.18%` | `49.82%` | `1.01` | 25,410,000.00 USD |
| `4H` | `Whale Positions` | `49.43%` | `50.57%` | `0.98` | 1,160,000,000.00 USD |
| `4H` | `Global Accounts` | `47.28%` | `52.72%` | `0.90` | 2,960,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

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
| `5m` | 209,070.00 USD | -140,940.00 USD | **`ACCUMULATION`** |
| `15m` | -38,460.00 USD | -584,360.00 USD | **`DISTRIBUTION`** |
| `30m` | 577,230.00 USD | -543,770.00 USD | **`ACCUMULATION`** |
| `1h` | 4,190,000.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `2h` | 3,550,000.00 USD | 4,330,000.00 USD | **`ACCUMULATION`** |
| `4h` | 8,530,000.00 USD | 8,440,000.00 USD | **`ACCUMULATION`** |
| `6h` | 5,500,000.00 USD | 12,500,000.00 USD | **`ACCUMULATION`** |
| `8h` | 5,830,000.00 USD | 12,820,000.00 USD | **`ACCUMULATION`** |
| `12h` | 5,800,000.00 USD | 12,620,000.00 USD | **`ACCUMULATION`** |
| `24h` | 8,510,000.00 USD | 15,080,000.00 USD | **`ACCUMULATION`** |
| `1w` | 689,550.00 USD | 12,390,000.00 USD | **`ACCUMULATION`** |
| `30d` | -17,190,000.00 USD | 16,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+209.07K` | 15m=`-38.46K` | 1h=`+4.19M` | 24h=`+8.51M`
* Futures Capital Netflows: 5m=`-140.94K` | 15m=`-584.36K` | 1h=`+1.53M` | 24h=`+15.08M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3447` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3331` (Risk Distance: `0.0116` pts)
  * +2.5R Take Profit: `0.3737`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3572` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3688` (Risk Distance: `0.0116` pts)
  * +2.5R Take Profit: `0.3282`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3585`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
