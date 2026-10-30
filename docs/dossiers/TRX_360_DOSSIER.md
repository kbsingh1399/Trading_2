# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:22:11 IST` (`2026-10-30 03:52:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3501` | **Live Ask Quote**: `0.3538` | **Mid Price**: `0.3519`
- **Spread Points**: `37.00` | **Spread BPS**: `105.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3534` | VWAP Z-Score: `-1.96` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0048` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.68` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3598` | Lower -3.00σ Band: `0.3471`
  * Upper +2.51σ Band: `0.3587` | Lower -2.51σ Band: `0.3481`
  * Upper +2.01σ Band: `0.3577` | Lower -2.01σ Band: `0.3492`
  * Upper +2.00σ Band: `0.3577` | Lower -2.00σ Band: `0.3492`
  * Upper +1.28σ Band: `0.3561` | Lower -1.28σ Band: `0.3507`
  * Upper +1.00σ Band: `0.3555` | Lower -1.00σ Band: `0.3513`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3518` | EMA-20=`0.3505` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3443` (Slope: `+0.0000`) | EMA-100=`0.3390`
  * Institutional Anchors: EMA-144=`0.3366` | EMA-200=`0.3349` (Slope: `+0.7055`) | EMA-233=`0.3342`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3572` (Distance: `-1.47%`)
  * Point of Control (POC) = `0.3512` (Distance: `+0.19%`)
  * Value Area Low (VAL) = `0.3459` (Distance: `+1.74%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3484` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3534` | Low=`0.3505`
  * New York Session (13:00-21:00 UTC): High=`0.3541` | Low=`0.3498`
  * Initial Balance (First Hour): IB High=`0.3530` | IB Low=`0.3509`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3505` - `0.3534`
  * Optimal Trade Entry (OTE 0.705): `0.3527`
  * Structural Invalidation Anchor (0.786): `0.3548`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3530` | `0.3539` | `0.3521` | `0.3521` | `4,305,470` | 1,518,699.74 USD | 317,780.84 USD | `+20.92%` | 6,277,557.13 USD | `+2.45` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.3521` | `0.3522` | `0.3493` | `0.3508` | `5,611,600` | 1,967,191.48 USD | -140,149.31 USD | `-7.12%` | 6,137,407.82 USD | `-0.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3508` | `0.3540` | `0.3507` | `0.3518` | `3,759,004` | 1,325,683.87 USD | 56,156.72 USD | `+4.24%` | 6,193,564.53 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3515` | `0.3548` | `0.3511` | `0.3534` | `7,272,047` | 2,568,313.45 USD | -81,052.09 USD | `-3.16%` | 5,978,310.16 USD | `-0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3534` | `0.3549` | `0.3493` | `0.3508` | `11,970,269` | 4,212,194.59 USD | 154,320.67 USD | `+3.66%` | 6,132,630.82 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3508` | `0.3540` | `0.3507` | `0.3518` | `3,759,004` | 1,325,683.87 USD | 56,156.72 USD | `+4.24%` | 6,188,787.54 USD | `-0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3579` | `0.3608` | `0.3516` | `0.3565` | `62,320,691` | 22,267,555.61 USD | 1,112,045.02 USD | `+4.99%` | 6,309,309.46 USD | `+0.68` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3565` | `0.3599` | `0.3515` | `0.3526` | `36,953,084` | 13,170,319.10 USD | -246,981.15 USD | `-1.88%` | 6,062,328.31 USD | `-0.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3526` | `0.3549` | `0.3493` | `0.3518` | `36,588,388` | 12,880,450.63 USD | 126,459.23 USD | `+0.98%` | 6,188,787.54 USD | `-0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3493` | `0.3518` | `248,873,392` | 88,408,758.27 USD | 2,794,167.43 USD | `+3.16%` | 6,189,354.00 USD | `+1.67` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 662,939.61 USD | `-1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,032,247.78 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,244,338.66 USD | `-0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 3,395,186.57 USD | `+1.93` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3493` | `0.3518` | `248,873,392` | 88,408,758.27 USD | 2,794,167.43 USD | `+3.16%` | 6,189,354.00 USD | `+1.67` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.3519`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `767` | `0xecb6...2b00` | `LONG` | 2,956,180.65 USD | `8,373,975.00` | `0.3341` | `0.3530` | `0.000000` | 158,066.46 USD | `+5.35%` | `10X Cross` |
| `1522` | `0xeadc...9d55` | `LONG` | 1,412,120.00 USD | `4,000,000.00` | `0.3421` | `0.3530` | `0.000000` | 43,641.91 USD | `+3.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3292` | 6,465.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3292 USD [API] | `2026-10-29 00:34:42` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+4.64%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--7.51%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+4.64%`) | Long MP=`0.3249` (Vol: 801,900.00 USD, Dist: `--7.51%`)
  * 3D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+4.25%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--7.51%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+4.25%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--7.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0705` | 815.54 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 103.26 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 186.07 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 8,260.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 114.87 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 112.50 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 391.44 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 342.82 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 208.12 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 3,270.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 239.53 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 20,240.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 1,140.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 7,740.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 10,500.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,370.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,170.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 256.98 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 175.37 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 208.67 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 1,860.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,870.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 41,450.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 101.59 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1985` | 635.20 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 86,250.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,650.00 USD | 954,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 227.46 USD | 952,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 286.67 USD | 952,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 952,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 237.74 USD | 947,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 2,360.00 USD | 947,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 122.23 USD | 944,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 3,080.00 USD | 944,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,120.00 USD | 941,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 6,120.00 USD | 939,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 3,150.00 USD | 933,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,260.00 USD | 930,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 216.51 USD | 928,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 159.45 USD | 928,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,230.00 USD | 928,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,350.00 USD | 927,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 2,800.00 USD | 926,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 923,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2515` | 263.07 USD | 911,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 911,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 301.79 USD | 909,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 752.06 USD | 909,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 2,210.00 USD | 908,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,210.00 USD | 906,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 27,230.00 USD | 904,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 193.75 USD | 877,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 876,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2695` | 3,170.00 USD | 876,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 3,950.00 USD | 873,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 80,810.00 USD | 869,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 182.04 USD | 788,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,060.00 USD | 788,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 775,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 13,350.00 USD | 769,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 3,700.00 USD | 755,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 5,720.00 USD | 752,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 359.16 USD | 746,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 589.42 USD | 746,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 24,310,000.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 745,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 3,540.00 USD | 744,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 338.67 USD | 740,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 24,230,000.00 USD | 24,230,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 24,170,000.00 USD | 24,170,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2959` | 24,090,000.00 USD | 24,090,000.00 USD | 109,190.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 23,950,000.00 USD | 23,950,000.00 USD | 127,630.00 USD | 38,150.00 USD | 62,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 305.39 USD | 740,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 23,720,000.00 USD | 23,720,000.00 USD | 151,670.00 USD | 40,930.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 23,460,000.00 USD | 23,460,000.00 USD | 69,090.00 USD | 20,520.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 23,350,000.00 USD | 23,350,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 127.46 USD | 740,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2989` | 23,130,000.00 USD | 23,130,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 22,980,000.00 USD | 22,980,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 3,510.00 USD | 740,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3001` | 21,260,000.00 USD | 21,260,000.00 USD | 107.80 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3007` | 21,260,000.00 USD | 21,260,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 22,970,000.00 USD | 22,970,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,980.00 USD | 736,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,130.00 USD | 725,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 21,200,000.00 USD | 21,200,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 485.90 USD | 723,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 267.35 USD | 723,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 21,160,000.00 USD | 21,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 22,930,000.00 USD | 22,930,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 21,080,000.00 USD | 21,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 22,880,000.00 USD | 22,880,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,810.00 USD | 722,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 21,010,000.00 USD | 21,010,000.00 USD | 885.25 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 22,880,000.00 USD | 22,880,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3067` | 20,950,000.00 USD | 20,950,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 22,810,000.00 USD | 22,810,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 20,870,000.00 USD | 20,870,000.00 USD | 23,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 22,800,000.00 USD | 22,800,000.00 USD | 9,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 5,920.00 USD | 708,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3079` | 20,840,000.00 USD | 20,840,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 22,790,000.00 USD | 22,790,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 20,840,000.00 USD | 20,840,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 22,690,000.00 USD | 22,690,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 1,020.00 USD | 702,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3091` | 20,820,000.00 USD | 20,820,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 22,690,000.00 USD | 22,690,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3097` | 20,820,000.00 USD | 20,820,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 22,680,000.00 USD | 22,680,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 20,820,000.00 USD | 20,820,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 22,660,000.00 USD | 22,660,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 193.13 USD | 701,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 22,530,000.00 USD | 22,530,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 22,520,000.00 USD | 22,520,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,740.00 USD | 700,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3121` | 22,520,000.00 USD | 22,520,000.00 USD | 162,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 3,130.00 USD | 687,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 20,710,000.00 USD | 20,710,000.00 USD | 2,260.00 USD | 24,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 22,360,000.00 USD | 22,360,000.00 USD | 12,180.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 20,680,000.00 USD | 20,680,000.00 USD | 164.40 USD | 23,940.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 22,340,000.00 USD | 22,340,000.00 USD | 8,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 18,090.00 USD | 683,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 20,630,000.00 USD | 20,630,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 22,340,000.00 USD | 22,340,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 20,630,000.00 USD | 20,630,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 22,330,000.00 USD | 22,330,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 141.84 USD | 665,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3151` | 20,630,000.00 USD | 20,630,000.00 USD | 215.60 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 22,020,000.00 USD | 22,020,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,490.00 USD | 665,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 21,760,000.00 USD | 21,760,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 20,590,000.00 USD | 20,590,000.00 USD | 69,350.00 USD | 50,600.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 21,220,000.00 USD | 21,220,000.00 USD | 493,400.00 USD | 185,890.00 USD | 203,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 664,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 20,440,000.00 USD | 20,440,000.00 USD | 84,050.00 USD | 16,200.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 20,330,000.00 USD | 20,330,000.00 USD | 585,730.00 USD | 116,810.00 USD | 159,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 20,300,000.00 USD | 20,300,000.00 USD | 21,570.00 USD | 46,950.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 19,470,000.00 USD | 19,470,000.00 USD | 189,350.00 USD | 63,970.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 20,220,000.00 USD | 20,220,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 19,140,000.00 USD | 19,140,000.00 USD | 738,770.00 USD | 76,910.00 USD | 133,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 19,670,000.00 USD | 19,670,000.00 USD | 182,020.00 USD | 53,160.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 18,190,000.00 USD | 18,190,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 17,720,000.00 USD | 17,720,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 19,400,000.00 USD | 19,400,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 19,350,000.00 USD | 19,350,000.00 USD | 265,870.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 17,420,000.00 USD | 17,420,000.00 USD | 34,460.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 19,050,000.00 USD | 19,050,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 17,320,000.00 USD | 17,320,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3215` | 1,790.00 USD | 663,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3217` | 18,890,000.00 USD | 18,890,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 16,460,000.00 USD | 16,460,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 18,800,000.00 USD | 18,800,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 16,010,000.00 USD | 16,010,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 18,510,000.00 USD | 18,510,000.00 USD | 140,560.00 USD | 81,070.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 15,080,000.00 USD | 15,080,000.00 USD | 761,410.00 USD | 281,560.00 USD | 407,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 18,080,000.00 USD | 18,080,000.00 USD | 129,720.00 USD | 77,760.00 USD | 168,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 13,630,000.00 USD | 13,630,000.00 USD | 1,080,000.00 USD | 233,630.00 USD | 407,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 647,000.00 USD | 661,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3241` | 17,710,000.00 USD | 17,710,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 11,910,000.00 USD | 11,910,000.00 USD | 480,120.00 USD | 170,870.00 USD | 157,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3245` | 462.09 USD | 14,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3247` | 17,510,000.00 USD | 17,510,000.00 USD | 570,580.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 11,100,000.00 USD | 11,100,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 16,520,000.00 USD | 16,520,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 9,770,000.00 USD | 9,770,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 2,570.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 15,150,000.00 USD | 15,150,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 8,440,000.00 USD | 8,440,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 8,050,000.00 USD | 8,050,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3265` | 129.62 USD | 11,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3271` | 14,630,000.00 USD | 14,630,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 7,860,000.00 USD | 7,860,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 3,000.00 USD | 11,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 14,170,000.00 USD | 14,170,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 7,660,000.00 USD | 7,660,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3289` | 13,700,000.00 USD | 13,700,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 13,500,000.00 USD | 13,500,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 7,270,000.00 USD | 7,270,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 7,240,000.00 USD | 7,240,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3305` | 1,650.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3307` | 13,420,000.00 USD | 13,420,000.00 USD | 110,810.00 USD | 13,130.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 7,170,000.00 USD | 7,170,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 13,210,000.00 USD | 13,210,000.00 USD | 234,580.00 USD | 143,410.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 6,830,000.00 USD | 6,830,000.00 USD | 138,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 12,500,000.00 USD | 12,500,000.00 USD | 158,550.00 USD | 54,860.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 11,990,000.00 USD | 11,990,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 6,580,000.00 USD | 6,580,000.00 USD | 90,080.00 USD | 35,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3325` | 160.93 USD | 6,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3331` | 11,660,000.00 USD | 11,660,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 6,450,000.00 USD | 6,450,000.00 USD | 549,640.00 USD | 38,470.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3335` | 1,150.00 USD | 6,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3337` | 11,660,000.00 USD | 11,660,000.00 USD | 147,860.00 USD | 164,450.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 11,430.00 USD | 186,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 10,770,000.00 USD | 10,770,000.00 USD | 76,100.00 USD | 91,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 33,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 1,010.00 USD | 5,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Long Liquidation` | `0.3379` | 9,470,000.00 USD | 9,470,000.00 USD | 514,160.00 USD | 67,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 4,290,000.00 USD | 4,290,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 8,890,000.00 USD | 8,890,000.00 USD | 178,310.00 USD | 115,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 3,620,000.00 USD | 3,620,000.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3385` | 2,430.00 USD | 4,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3391` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 27,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3395` | 986.93 USD | 1,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3397` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 75,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,340,000.00 USD | 3,340,000.00 USD | 257,550.00 USD | 172,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 2,910,000.00 USD | 2,910,000.00 USD | 799,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 164,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 95,940.00 USD | 158,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 8,210,000.00 USD | 8,210,000.00 USD | 627,050.00 USD | 119,690.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3415` | 344.23 USD | 985.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3421` | 7,400,000.00 USD | 7,400,000.00 USD | 392,750.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3425` | 641.16 USD | 641.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.3559` | 1,490,000.00 USD | 1,490,000.00 USD | 218,620.00 USD | 151,290.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 2,230,000.00 USD | 2,230,000.00 USD | 3,220.00 USD | 163,630.00 USD | 578,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 2,620,000.00 USD | 2,620,000.00 USD | 389,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 3,100,000.00 USD | 3,100,000.00 USD | 110,810.00 USD | 105,430.00 USD | 268,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 225,550.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `0.3631` | 5,400,000.00 USD | 5,400,000.00 USD | 967,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,410.00 USD | 31,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 5,520,000.00 USD | 5,520,000.00 USD | 98,170.00 USD | 22,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 5,640,000.00 USD | 5,640,000.00 USD | 1,360.00 USD | 119,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 4,890,000.00 USD | 4,890,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 43,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 5,860,000.00 USD | 5,860,000.00 USD | 194,600.00 USD | 24,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,070,000.00 USD | 5,070,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 6,150,000.00 USD | 6,150,000.00 USD | 186,410.00 USD | 99,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 5,470,000.00 USD | 5,470,000.00 USD | 288,200.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 6,430,000.00 USD | 6,430,000.00 USD | 259,500.00 USD | 23,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 6,320,000.00 USD | 6,320,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,060.00 USD | 44,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 6,840,000.00 USD | 6,840,000.00 USD | 341,880.00 USD | 70,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 6,740,000.00 USD | 6,740,000.00 USD | 419,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 6,920,000.00 USD | 6,920,000.00 USD | 5,540.00 USD | 75,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 7,250,000.00 USD | 7,250,000.00 USD | 511,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,300.00 USD | 46,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3679` | 7,670,000.00 USD | 7,670,000.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 7,500,000.00 USD | 7,500,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 8,210,000.00 USD | 8,210,000.00 USD | 326,450.00 USD | 217,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 102,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 2,270.00 USD | 48,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3691` | 8,540,000.00 USD | 8,540,000.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 7,950,000.00 USD | 7,950,000.00 USD | 147,650.00 USD | 193,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 8,720,000.00 USD | 8,720,000.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 95,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 9,470,000.00 USD | 9,470,000.00 USD | 603,020.00 USD | 151,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 10,000,000.00 USD | 10,000,000.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 11,500,000.00 USD | 11,500,000.00 USD | 438,840.00 USD | 92,390.00 USD | 969,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 2,690.00 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3721` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 179.92 USD | 51,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3727` | 12,860,000.00 USD | 12,860,000.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 9,230,000.00 USD | 9,230,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 13,730,000.00 USD | 13,730,000.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 9,420,000.00 USD | 9,420,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 27,130.00 USD | 78,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3739` | 14,220,000.00 USD | 14,220,000.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 9,890,000.00 USD | 9,890,000.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 14,600,000.00 USD | 14,600,000.00 USD | 31,600.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 10,280,000.00 USD | 10,280,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 17,660.00 USD | 96,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 15,440,000.00 USD | 15,440,000.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,960.00 USD | 101,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3757` | 15,710,000.00 USD | 15,710,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 10,580,000.00 USD | 10,580,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 16,960,000.00 USD | 16,960,000.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 10,760,000.00 USD | 10,760,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3765` | 32,390.00 USD | 133,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3769` | 17,010,000.00 USD | 17,010,000.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 10,760,000.00 USD | 10,760,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3775` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3781` | 17,320,000.00 USD | 17,320,000.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 10,790,000.00 USD | 10,790,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,700.00 USD | 690,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 17,830,000.00 USD | 17,830,000.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3787` | 10,830,000.00 USD | 10,830,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 18,030,000.00 USD | 18,030,000.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 11,300,000.00 USD | 11,300,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3799` | 18,030,000.00 USD | 18,030,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 18,360,000.00 USD | 18,360,000.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 11,450,000.00 USD | 11,450,000.00 USD | 156,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3823` | 18,630,000.00 USD | 18,630,000.00 USD | 2,080.00 USD | 24,220.00 USD | 239,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 4,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3829` | 18,660,000.00 USD | 18,660,000.00 USD | 1,720.00 USD | 23,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 34,170.00 USD | 724,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3841` | 18,870,000.00 USD | 18,870,000.00 USD | 850.22 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 11,460,000.00 USD | 11,460,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3847` | 18,870,000.00 USD | 18,870,000.00 USD | 899.18 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3853` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 11,530,000.00 USD | 11,530,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3865` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 11,690,000.00 USD | 11,690,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3865` | 66,200.00 USD | 790,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3871` | 18,970,000.00 USD | 18,970,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3877` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 28,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 11,810,000.00 USD | 11,810,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3883` | 19,000,000.00 USD | 19,000,000.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 11,910,000.00 USD | 11,910,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3895` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 30,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,360.00 USD | 794,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 12,010,000.00 USD | 12,010,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 1,100.00 USD | 795,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 19,080,000.00 USD | 19,080,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3907` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3913` | 19,250,000.00 USD | 19,250,000.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 609.57 USD | 796,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 19,320,000.00 USD | 19,320,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 19,390,000.00 USD | 19,390,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 12,290,000.00 USD | 12,290,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3931` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 12,320,000.00 USD | 12,320,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 798,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3937` | 19,560,000.00 USD | 19,560,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3937` | 12,350,000.00 USD | 12,350,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 19,770,000.00 USD | 19,770,000.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 12,370,000.00 USD | 12,370,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 916,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 19,900,000.00 USD | 19,900,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3949` | 12,510,000.00 USD | 12,510,000.00 USD | 109,790.00 USD | 8,290.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 20,100,000.00 USD | 20,100,000.00 USD | 55,640.00 USD | 47,610.00 USD | 92,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 12,750,000.00 USD | 12,750,000.00 USD | 111,780.00 USD | 10,870.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3961` | 20,200,000.00 USD | 20,200,000.00 USD | 4,020.00 USD | 10,290.00 USD | 86,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 12,960,000.00 USD | 12,960,000.00 USD | 145,900.00 USD | 54,030.00 USD | 9,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 1,580.00 USD | 917,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3967` | 20,290,000.00 USD | 20,290,000.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 12,980,000.00 USD | 12,980,000.00 USD | 12,370.00 USD | 7,000.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 20,460,000.00 USD | 20,460,000.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 13,120,000.00 USD | 13,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3979` | 20,860,000.00 USD | 20,860,000.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 13,230,000.00 USD | 13,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 20,870,000.00 USD | 20,870,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 13,270,000.00 USD | 13,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3991` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3997` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 21,080,000.00 USD | 21,080,000.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4005` | 45,000.00 USD | 962,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.4009` | 21,240,000.00 USD | 21,240,000.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 13,290,000.00 USD | 13,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4027` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4045` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,040.00 USD | 964,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 410.73 USD | 965,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4125` | 194.70 USD | 965,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4175` | 599.53 USD | 966,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 1,000.00 USD | 967,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 11,900.00 USD | 978,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4285` | 10,190.00 USD | 989,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4335` | 70,560.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 378.34 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 1,850.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 23,460.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 758.51 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4485` | 65,760.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 318.76 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 5,560.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4535` | 1,140.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4585` | 596,050.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4695` | 301,500.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4735` | 9,680.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,960.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 289.29 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 235.71 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5045` | 780,810.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5545` | 43,340.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5595` | 8,260.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5705` | 54,680.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5785` | 4,630.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5795` | 752,780.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5885` | 24,420.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 28,550.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6255` | 32,880.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 1,140.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 395,490.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 48,630.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6365` | 7,070.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6465` | 1,060.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6545` | 706.21 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6625` | 2,060.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 2,930.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6645` | 1,210.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6705` | 85,400.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6735` | 83,060.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6765` | 16,750.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6775` | 833.33 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6875` | 262.62 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6925` | 414.12 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6965` | 783,420.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6985` | 27,940.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6995` | 1,010.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7005` | 106.48 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0705` | 1,180,000.00 USD | 0.00 USD | 815.54 USD | `-80.03%` | `11,568.00` |
| `Live` | `Long` | `0.0845` | 1,180,000.00 USD | 0.00 USD | 103.26 USD | `-76.06%` | `1,222.00` |
| `Live` | `Long` | `0.0895` | 1,180,000.00 USD | 0.00 USD | 186.07 USD | `-74.65%` | `2,079.00` |
| `Live` | `Long` | `0.1075` | 1,180,000.00 USD | 0.00 USD | 8,260.00 USD | `-69.55%` | `76,797.00` |
| `Live` | `Long` | `0.1095` | 1,170,000.00 USD | 0.00 USD | 114.87 USD | `-68.98%` | `1,049.00` |
| `Live` | `Long` | `0.1115` | 1,170,000.00 USD | 0.00 USD | 112.50 USD | `-68.41%` | `1,009.00` |
| `Live` | `Long` | `0.1165` | 1,170,000.00 USD | 0.00 USD | 391.44 USD | `-67.00%` | `3,360.00` |
| `Live` | `Long` | `0.1205` | 1,170,000.00 USD | 0.00 USD | 342.82 USD | `-65.86%` | `2,845.00` |
| `Live` | `Long` | `0.1475` | 1,170,000.00 USD | 0.00 USD | 208.12 USD | `-58.22%` | `1,411.00` |
| `Live` | `Long` | `0.1595` | 1,170,000.00 USD | 0.00 USD | 390.46 USD | `-54.82%` | `2,448.00` |
| `Live` | `Long` | `0.1635` | 1,170,000.00 USD | 0.00 USD | 3,270.00 USD | `-53.68%` | `20,000.00` |
| `Live` | `Long` | `0.1675` | 1,170,000.00 USD | 0.00 USD | 239.53 USD | `-52.55%` | `1,430.00` |
| `Live` | `Long` | `0.1695` | 1,170,000.00 USD | 0.00 USD | 20,240.00 USD | `-51.98%` | `119,400.00` |
| `Live` | `Long` | `0.1705` | 1,150,000.00 USD | 0.00 USD | 1,140.00 USD | `-51.70%` | `6,706.00` |
| `Live` | `Long` | `0.1725` | 1,150,000.00 USD | 0.00 USD | 7,740.00 USD | `-51.13%` | `44,884.00` |
| `Live` | `Long` | `0.1735` | 1,140,000.00 USD | 0.00 USD | 10,500.00 USD | `-50.85%` | `60,538.00` |
| `Live` | `Long` | `0.1745` | 1,130,000.00 USD | 0.00 USD | 1,370.00 USD | `-50.57%` | `7,823.00` |
| `Live` | `Long` | `0.1755` | 1,130,000.00 USD | 0.00 USD | 4,170.00 USD | `-50.28%` | `23,777.00` |
| `Live` | `Long` | `0.1765` | 1,120,000.00 USD | 0.00 USD | 256.98 USD | `-50.00%` | `1,456.00` |
| `Live` | `Long` | `0.1775` | 1,120,000.00 USD | 0.00 USD | 175.37 USD | `-49.72%` | `988.00` |
| `Live` | `Long` | `0.1785` | 1,120,000.00 USD | 0.00 USD | 208.67 USD | `-49.43%` | `1,169.00` |
| `Live` | `Long` | `0.1845` | 1,120,000.00 USD | 0.00 USD | 1,860.00 USD | `-47.73%` | `10,084.00` |
| `Live` | `Long` | `0.1875` | 1,120,000.00 USD | 0.00 USD | 36,870.00 USD | `-46.88%` | `196,636.00` |
| `Live` | `Long` | `0.1895` | 1,080,000.00 USD | 0.00 USD | 41,450.00 USD | `-46.32%` | `218,745.00` |
| `Live` | `Long` | `0.1935` | 1,040,000.00 USD | 0.00 USD | 101.59 USD | `-45.18%` | `525.00` |
| `Live` | `Long` | `0.1985` | 1,040,000.00 USD | 0.00 USD | 635.20 USD | `-43.77%` | `3,200.00` |
| `Live` | `Long` | `0.2045` | 1,040,000.00 USD | 0.00 USD | 86,250.00 USD | `-42.07%` | `421,736.00` |
| `Live` | `Long` | `0.2175` | 954,190.00 USD | 0.00 USD | 1,650.00 USD | `-38.39%` | `7,594.00` |
| `Live` | `Long` | `0.2185` | 952,540.00 USD | 0.00 USD | 227.46 USD | `-38.10%` | `1,041.00` |
| `Live` | `Long` | `0.2195` | 952,320.00 USD | 0.00 USD | 286.67 USD | `-37.82%` | `1,306.00` |
| `Live` | `Long` | `0.2255` | 952,030.00 USD | 0.00 USD | 4,590.00 USD | `-36.12%` | `20,360.00` |
| `Live` | `Long` | `0.2275` | 947,440.00 USD | 0.00 USD | 237.74 USD | `-35.55%` | `1,045.00` |
| `Live` | `Long` | `0.2305` | 947,200.00 USD | 0.00 USD | 2,360.00 USD | `-34.70%` | `10,255.00` |
| `Live` | `Long` | `0.2315` | 944,840.00 USD | 0.00 USD | 122.23 USD | `-34.42%` | `528.00` |
| `Live` | `Long` | `0.2325` | 944,710.00 USD | 0.00 USD | 3,080.00 USD | `-34.14%` | `13,262.00` |
| `Live` | `Long` | `0.2335` | 941,630.00 USD | 0.00 USD | 2,120.00 USD | `-33.85%` | `9,077.00` |
| `Live` | `Long` | `0.2345` | 939,510.00 USD | 0.00 USD | 6,120.00 USD | `-33.57%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 933,390.00 USD | 0.00 USD | 3,150.00 USD | `-33.00%` | `13,311.00` |
| `Live` | `Long` | `0.2375` | 930,250.00 USD | 0.00 USD | 1,260.00 USD | `-32.72%` | `5,298.00` |
| `Live` | `Long` | `0.2395` | 928,990.00 USD | 0.00 USD | 216.51 USD | `-32.15%` | `904.00` |
| `Live` | `Long` | `0.2405` | 928,770.00 USD | 0.00 USD | 159.45 USD | `-31.87%` | `663.00` |
| `Live` | `Long` | `0.2425` | 928,610.00 USD | 0.00 USD | 1,230.00 USD | `-31.30%` | `5,071.00` |
| `Live` | `Long` | `0.2445` | 927,380.00 USD | 0.00 USD | 1,350.00 USD | `-30.74%` | `5,539.00` |
| `Live` | `Long` | `0.2465` | 926,030.00 USD | 0.00 USD | 2,800.00 USD | `-30.17%` | `11,365.00` |
| `Live` | `Long` | `0.2485` | 923,230.00 USD | 0.00 USD | 11,890.00 USD | `-29.60%` | `47,833.00` |
| `Live` | `Long` | `0.2515` | 911,340.00 USD | 0.00 USD | 263.07 USD | `-28.75%` | `1,046.00` |
| `Live` | `Long` | `0.2565` | 911,080.00 USD | 0.00 USD | 1,230.00 USD | `-27.34%` | `4,794.00` |
| `Live` | `Long` | `0.2575` | 909,850.00 USD | 0.00 USD | 301.79 USD | `-27.05%` | `1,172.00` |
| `Live` | `Long` | `0.2605` | 909,550.00 USD | 0.00 USD | 752.06 USD | `-26.20%` | `2,887.00` |
| `Live` | `Long` | `0.2625` | 908,790.00 USD | 0.00 USD | 2,210.00 USD | `-25.64%` | `8,427.00` |
| `Live` | `Long` | `0.2645` | 906,580.00 USD | 0.00 USD | 2,210.00 USD | `-25.07%` | `8,340.00` |
| `Live` | `Long` | `0.2655` | 904,380.00 USD | 0.00 USD | 27,230.00 USD | `-24.79%` | `102,572.00` |
| `Live` | `Long` | `0.2665` | 877,140.00 USD | 0.00 USD | 193.75 USD | `-24.50%` | `727.00` |
| `Live` | `Long` | `0.2675` | 876,950.00 USD | 0.00 USD | 321.54 USD | `-24.22%` | `1,202.00` |
| `Live` | `Long` | `0.2695` | 876,630.00 USD | 0.00 USD | 3,170.00 USD | `-23.65%` | `11,746.00` |
| `Live` | `Long` | `0.2745` | 873,460.00 USD | 0.00 USD | 3,950.00 USD | `-22.24%` | `14,395.00` |
| `Live` | `Long` | `0.2755` | 869,510.00 USD | 0.00 USD | 80,810.00 USD | `-21.95%` | `293,333.00` |
| `Live` | `Long` | `0.2775` | 788,700.00 USD | 0.00 USD | 182.04 USD | `-21.39%` | `656.00` |
| `Live` | `Long` | `0.2795` | 788,520.00 USD | 0.00 USD | 13,060.00 USD | `-20.82%` | `46,725.00` |
| `Live` | `Long` | `0.2805` | 775,460.00 USD | 0.00 USD | 6,280.00 USD | `-20.54%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 769,180.00 USD | 0.00 USD | 13,350.00 USD | `-20.25%` | `47,408.00` |
| `Live` | `Long` | `0.2825` | 755,830.00 USD | 0.00 USD | 3,700.00 USD | `-19.97%` | `13,109.00` |
| `Live` | `Long` | `0.2845` | 752,130.00 USD | 0.00 USD | 5,720.00 USD | `-19.41%` | `20,120.00` |
| `Live` | `Long` | `0.2855` | 746,410.00 USD | 0.00 USD | 359.16 USD | `-19.12%` | `1,258.00` |
| `Live` | `Long` | `0.2905` | 746,050.00 USD | 0.00 USD | 589.42 USD | `-17.71%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 745,460.00 USD | 0.00 USD | 957.64 USD | `-17.14%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 744,500.00 USD | 0.00 USD | 3,540.00 USD | `-16.86%` | `12,054.00` |
| `Live` | `Long` | `0.2945` | 740,960.00 USD | 0.00 USD | 338.67 USD | `-16.57%` | `1,150.00` |
| `Live` | `Long` | `0.2965` | 740,620.00 USD | 0.00 USD | 305.39 USD | `-16.01%` | `1,030.00` |
| `Live` | `Long` | `0.2985` | 740,320.00 USD | 0.00 USD | 127.46 USD | `-15.44%` | `427.00` |
| `Live` | `Long` | `0.2995` | 740,190.00 USD | 0.00 USD | 3,510.00 USD | `-15.16%` | `11,720.00` |
| `Live` | `Long` | `0.3015` | 736,680.00 USD | 0.00 USD | 10,980.00 USD | `-14.59%` | `36,421.00` |
| `Live` | `Long` | `0.3025` | 725,700.00 USD | 0.00 USD | 2,130.00 USD | `-14.31%` | `7,054.00` |
| `Live` | `Long` | `0.3035` | 723,560.00 USD | 0.00 USD | 485.90 USD | `-14.02%` | `1,601.00` |
| `Live` | `Long` | `0.3045` | 723,080.00 USD | 0.00 USD | 267.35 USD | `-13.74%` | `878.00` |
| `Live` | `Long` | `0.3055` | 722,810.00 USD | 0.00 USD | 14,810.00 USD | `-13.46%` | `48,480.00` |
| `Live` | `Long` | `0.3075` | 708,000.00 USD | 0.00 USD | 5,920.00 USD | `-12.89%` | `19,262.00` |
| `Live` | `Long` | `0.3085` | 702,080.00 USD | 0.00 USD | 1,020.00 USD | `-12.61%` | `3,295.00` |
| `Live` | `Long` | `0.3105` | 701,060.00 USD | 0.00 USD | 193.13 USD | `-12.04%` | `622.00` |
| `Live` | `Long` | `0.3115` | 700,870.00 USD | 0.00 USD | 13,740.00 USD | `-11.76%` | `44,115.00` |
| `Live` | `Long` | `0.3125` | 687,130.00 USD | 0.00 USD | 3,130.00 USD | `-11.47%` | `10,032.00` |
| `Live` | `Long` | `0.3135` | 683,990.00 USD | 0.00 USD | 18,090.00 USD | `-11.19%` | `57,693.00` |
| `Live` | `Long` | `0.3145` | 665,900.00 USD | 0.00 USD | 141.84 USD | `-10.91%` | `451.00` |
| `Live` | `Long` | `0.3155` | 665,760.00 USD | 0.00 USD | 1,490.00 USD | `-10.62%` | `4,723.00` |
| `Live` | `Long` | `0.3165` | 664,270.00 USD | 0.00 USD | 935.89 USD | `-10.34%` | `2,957.00` |
| `Live` | `Long` | `0.3215` | 663,340.00 USD | 0.00 USD | 1,790.00 USD | `-8.92%` | `5,572.00` |
| `Live` | `Long` | `0.3235` | 661,550.00 USD | 0.00 USD | 647,000.00 USD | `-8.36%` | `1,999,999.00` |
| `Live` | `Long` | `0.3245` | 14,550.00 USD | 0.00 USD | 462.09 USD | `-8.07%` | `1,424.00` |
| `Live` | `Long` | `0.3255` | 14,080.00 USD | 0.00 USD | 2,570.00 USD | `-7.79%` | `7,883.00` |
| `Live` | `Long` | `0.3265` | 11,520.00 USD | 0.00 USD | 129.62 USD | `-7.51%` | `397.00` |
| `Live` | `Long` | `0.3275` | 11,390.00 USD | 0.00 USD | 3,000.00 USD | `-7.22%` | `9,175.00` |
| `Live` | `Long` | `0.3305` | 8,380.00 USD | 0.00 USD | 1,650.00 USD | `-6.37%` | `4,998.00` |
| `Live` | `Long` | `0.3325` | 6,730.00 USD | 0.00 USD | 160.93 USD | `-5.81%` | `484.00` |
| `Live` | `Long` | `0.3335` | 6,570.00 USD | 0.00 USD | 1,150.00 USD | `-5.52%` | `3,460.00` |
| `Live` | `Long` | `0.3345` | 5,420.00 USD | 0.00 USD | 1,010.00 USD | `-5.24%` | `3,030.00` |
| `Live` | `Long` | `0.3385` | 4,400.00 USD | 0.00 USD | 2,430.00 USD | `-4.11%` | `7,181.00` |
| `Live` | `Long` | `0.3395` | 1,970.00 USD | 0.00 USD | 986.93 USD | `-3.82%` | `2,907.00` |
| `Live` | `Long` | `0.3415` | 985.39 USD | 0.00 USD | 344.23 USD | `-3.26%` | `1,008.00` |
| `Live` | `Long` | `0.3425` | 641.16 USD | 0.00 USD | 641.16 USD | `-2.97%` | `1,872.00` |
| `Live` | `Short` | `0.3635` | 31,410.00 USD | 31,410.00 USD | 0.00 USD | `+2.97%` | `86,423.00` |
| `Live` | `Short` | `0.3645` | 43,810.00 USD | 12,390.00 USD | 0.00 USD | `+3.26%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 44,870.00 USD | 1,060.00 USD | 0.00 USD | `+3.82%` | `2,882.00` |
| `Live` | `Short` | `0.3675` | 46,160.00 USD | 1,300.00 USD | 0.00 USD | `+4.11%` | `3,531.00` |
| `Live` | `Short` | `0.3685` | 48,430.00 USD | 2,270.00 USD | 0.00 USD | `+4.39%` | `6,156.00` |
| `Live` | `Short` | `0.3715` | 51,120.00 USD | 2,690.00 USD | 0.00 USD | `+5.24%` | `7,251.00` |
| `Live` | `Short` | `0.3725` | 51,300.00 USD | 179.92 USD | 0.00 USD | `+5.52%` | `483.00` |
| `Live` | `Short` | `0.3735` | 78,440.00 USD | 27,130.00 USD | 0.00 USD | `+5.81%` | `72,645.00` |
| `Live` | `Short` | `0.3745` | 96,100.00 USD | 17,660.00 USD | 0.00 USD | `+6.09%` | `47,166.00` |
| `Live` | `Short` | `0.3755` | 101,060.00 USD | 4,960.00 USD | 0.00 USD | `+6.37%` | `13,214.00` |
| `Live` | `Short` | `0.3765` | 133,450.00 USD | 32,390.00 USD | 0.00 USD | `+6.66%` | `86,025.00` |
| `Live` | `Short` | `0.3785` | 690,150.00 USD | 556,700.00 USD | 0.00 USD | `+7.22%` | `1,470,802.00` |
| `Live` | `Short` | `0.3835` | 724,320.00 USD | 34,170.00 USD | 0.00 USD | `+8.64%` | `89,108.00` |
| `Live` | `Short` | `0.3865` | 790,530.00 USD | 66,200.00 USD | 0.00 USD | `+9.49%` | `171,288.00` |
| `Live` | `Short` | `0.3895` | 794,880.00 USD | 4,360.00 USD | 0.00 USD | `+10.34%` | `11,191.00` |
| `Live` | `Short` | `0.3905` | 795,980.00 USD | 1,100.00 USD | 0.00 USD | `+10.62%` | `2,810.00` |
| `Live` | `Short` | `0.3915` | 796,590.00 USD | 609.57 USD | 0.00 USD | `+10.91%` | `1,557.00` |
| `Live` | `Short` | `0.3935` | 798,080.00 USD | 1,480.00 USD | 0.00 USD | `+11.47%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 916,200.00 USD | 118,130.00 USD | 0.00 USD | `+11.76%` | `299,436.00` |
| `Live` | `Short` | `0.3965` | 917,790.00 USD | 1,580.00 USD | 0.00 USD | `+12.32%` | `3,992.00` |
| `Live` | `Short` | `0.4005` | 962,790.00 USD | 45,000.00 USD | 0.00 USD | `+13.46%` | `112,367.00` |
| `Live` | `Short` | `0.4085` | 964,830.00 USD | 2,040.00 USD | 0.00 USD | `+15.72%` | `4,999.00` |
| `Live` | `Short` | `0.4095` | 965,240.00 USD | 410.73 USD | 0.00 USD | `+16.01%` | `1,003.00` |
| `Live` | `Short` | `0.4125` | 965,440.00 USD | 194.70 USD | 0.00 USD | `+16.86%` | `472.00` |
| `Live` | `Short` | `0.4175` | 966,040.00 USD | 599.53 USD | 0.00 USD | `+18.27%` | `1,436.00` |
| `Live` | `Short` | `0.4195` | 967,040.00 USD | 1,000.00 USD | 0.00 USD | `+18.84%` | `2,387.00` |
| `Live` | `Short` | `0.4235` | 978,930.00 USD | 11,900.00 USD | 0.00 USD | `+19.97%` | `28,092.00` |
| `Live` | `Short` | `0.4285` | 989,120.00 USD | 10,190.00 USD | 0.00 USD | `+21.39%` | `23,779.00` |
| `Live` | `Short` | `0.4335` | 1,060,000.00 USD | 70,560.00 USD | 0.00 USD | `+22.80%` | `162,775.00` |
| `Live` | `Short` | `0.4425` | 1,060,000.00 USD | 378.34 USD | 0.00 USD | `+25.35%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,060,000.00 USD | 1,850.00 USD | 0.00 USD | `+26.20%` | `4,154.00` |
| `Live` | `Short` | `0.4465` | 1,090,000.00 USD | 23,460.00 USD | 0.00 USD | `+26.49%` | `52,539.00` |
| `Live` | `Short` | `0.4475` | 1,090,000.00 USD | 758.51 USD | 0.00 USD | `+26.77%` | `1,695.00` |
| `Live` | `Short` | `0.4485` | 1,150,000.00 USD | 65,760.00 USD | 0.00 USD | `+27.05%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 1,150,000.00 USD | 318.76 USD | 0.00 USD | `+27.90%` | `706.00` |
| `Live` | `Short` | `0.4525` | 1,160,000.00 USD | 5,560.00 USD | 0.00 USD | `+28.19%` | `12,287.00` |
| `Live` | `Short` | `0.4535` | 1,160,000.00 USD | 1,140.00 USD | 0.00 USD | `+28.47%` | `2,519.00` |
| `Live` | `Short` | `0.4585` | 1,750,000.00 USD | 596,050.00 USD | 0.00 USD | `+29.89%` | `1,300,000.00` |
| `Live` | `Short` | `0.4695` | 2,060,000.00 USD | 301,500.00 USD | 0.00 USD | `+33.00%` | `642,167.00` |
| `Live` | `Short` | `0.4735` | 2,070,000.00 USD | 9,680.00 USD | 0.00 USD | `+34.14%` | `20,443.00` |
| `Live` | `Short` | `0.4905` | 2,070,000.00 USD | 5,960.00 USD | 0.00 USD | `+38.95%` | `12,145.00` |
| `Live` | `Short` | `0.4995` | 2,070,000.00 USD | 2,730.00 USD | 0.00 USD | `+41.50%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,080,000.00 USD | 289.29 USD | 0.00 USD | `+41.78%` | `578.00` |
| `Live` | `Short` | `0.5015` | 2,080,000.00 USD | 235.71 USD | 0.00 USD | `+42.07%` | `470.00` |
| `Live` | `Short` | `0.5045` | 2,860,000.00 USD | 780,810.00 USD | 0.00 USD | `+42.92%` | `1,547,681.00` |
| `Live` | `Short` | `0.5335` | 2,860,000.00 USD | 668.48 USD | 0.00 USD | `+51.13%` | `1,253.00` |
| `Live` | `Short` | `0.5545` | 2,900,000.00 USD | 43,340.00 USD | 0.00 USD | `+57.08%` | `78,154.00` |
| `Live` | `Short` | `0.5575` | 2,900,000.00 USD | 740.92 USD | 0.00 USD | `+57.93%` | `1,329.00` |
| `Live` | `Short` | `0.5595` | 2,910,000.00 USD | 8,260.00 USD | 0.00 USD | `+58.50%` | `14,763.00` |
| `Live` | `Short` | `0.5615` | 2,910,000.00 USD | 140.38 USD | 0.00 USD | `+59.07%` | `250.00` |
| `Live` | `Short` | `0.5705` | 2,960,000.00 USD | 54,680.00 USD | 0.00 USD | `+61.61%` | `95,846.00` |
| `Live` | `Short` | `0.5785` | 2,970,000.00 USD | 4,630.00 USD | 0.00 USD | `+63.88%` | `8,009.00` |
| `Live` | `Short` | `0.5795` | 3,720,000.00 USD | 752,780.00 USD | 0.00 USD | `+64.16%` | `1,299,024.00` |
| `Live` | `Short` | `0.5885` | 3,750,000.00 USD | 24,420.00 USD | 0.00 USD | `+66.71%` | `41,497.00` |
| `Live` | `Short` | `0.6155` | 3,770,000.00 USD | 28,550.00 USD | 0.00 USD | `+74.36%` | `46,380.00` |
| `Live` | `Short` | `0.6255` | 3,810,000.00 USD | 32,880.00 USD | 0.00 USD | `+77.20%` | `52,566.00` |
| `Live` | `Short` | `0.6285` | 3,810,000.00 USD | 1,140.00 USD | 0.00 USD | `+78.05%` | `1,808.00` |
| `Live` | `Short` | `0.6335` | 4,200,000.00 USD | 395,490.00 USD | 0.00 USD | `+79.46%` | `624,300.00` |
| `Live` | `Short` | `0.6345` | 4,250,000.00 USD | 48,630.00 USD | 0.00 USD | `+79.75%` | `76,641.00` |
| `Live` | `Short` | `0.6365` | 4,260,000.00 USD | 7,070.00 USD | 0.00 USD | `+80.31%` | `11,103.00` |
| `Live` | `Short` | `0.6465` | 4,260,000.00 USD | 1,060.00 USD | 0.00 USD | `+83.14%` | `1,642.00` |
| `Live` | `Short` | `0.6515` | 4,260,000.00 USD | 951.19 USD | 0.00 USD | `+84.56%` | `1,460.00` |
| `Live` | `Short` | `0.6545` | 4,260,000.00 USD | 706.21 USD | 0.00 USD | `+85.41%` | `1,079.00` |
| `Live` | `Short` | `0.6625` | 4,260,000.00 USD | 2,060.00 USD | 0.00 USD | `+87.68%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 4,270,000.00 USD | 2,930.00 USD | 0.00 USD | `+87.96%` | `4,416.00` |
| `Live` | `Short` | `0.6645` | 4,270,000.00 USD | 1,210.00 USD | 0.00 USD | `+88.24%` | `1,821.00` |
| `Live` | `Short` | `0.6705` | 4,350,000.00 USD | 85,400.00 USD | 0.00 USD | `+89.94%` | `127,370.00` |
| `Live` | `Short` | `0.6735` | 4,440,000.00 USD | 83,060.00 USD | 0.00 USD | `+90.79%` | `123,332.00` |
| `Live` | `Short` | `0.6765` | 4,450,000.00 USD | 16,750.00 USD | 0.00 USD | `+91.64%` | `24,756.00` |
| `Live` | `Short` | `0.6775` | 4,450,000.00 USD | 833.33 USD | 0.00 USD | `+91.93%` | `1,230.00` |
| `Live` | `Short` | `0.6875` | 4,450,000.00 USD | 262.62 USD | 0.00 USD | `+94.76%` | `382.00` |
| `Live` | `Short` | `0.6925` | 4,460,000.00 USD | 414.12 USD | 0.00 USD | `+96.18%` | `598.00` |
| `Live` | `Short` | `0.6965` | 5,240,000.00 USD | 783,420.00 USD | 0.00 USD | `+97.31%` | `1,124,802.00` |
| `Live` | `Short` | `0.6985` | 5,270,000.00 USD | 27,940.00 USD | 0.00 USD | `+97.88%` | `40,000.00` |
| `Live` | `Short` | `0.6995` | 5,270,000.00 USD | 1,010.00 USD | 0.00 USD | `+98.16%` | `1,451.00` |
| `Live` | `Short` | `0.7005` | 5,270,000.00 USD | 106.48 USD | 0.00 USD | `+98.44%` | `152.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 1,160,000.00 USD | 0.00 USD | 198.45 USD | `-73.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 1,160,000.00 USD | 0.00 USD | 330.26 USD | `-59.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 1,160,000.00 USD | 0.00 USD | 6,100.00 USD | `-48.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 1,150,000.00 USD | 0.00 USD | 1,750.00 USD | `-42.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 1,150,000.00 USD | 0.00 USD | 2,220.00 USD | `-40.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 1,150,000.00 USD | 0.00 USD | 121.70 USD | `-34.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 1,150,000.00 USD | 0.00 USD | 705.61 USD | `-33.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 1,150,000.00 USD | 0.00 USD | 159.20 USD | `-33.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 1,150,000.00 USD | 0.00 USD | 1,200.00 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 1,140,000.00 USD | 0.00 USD | 127.51 USD | `-31.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 1,140,000.00 USD | 0.00 USD | 1,850.00 USD | `-29.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 1,140,000.00 USD | 0.00 USD | 41,500.00 USD | `-28.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 1,100,000.00 USD | 0.00 USD | 1,920.00 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 1,100,000.00 USD | 0.00 USD | 664.01 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 1,100,000.00 USD | 0.00 USD | 954.98 USD | `-25.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 1,100,000.00 USD | 0.00 USD | 103.56 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 1,100,000.00 USD | 0.00 USD | 695.50 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 1,100,000.00 USD | 0.00 USD | 1,630.00 USD | `-23.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 1,090,000.00 USD | 0.00 USD | 1,470.00 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 1,090,000.00 USD | 0.00 USD | 101.94 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 1,090,000.00 USD | 0.00 USD | 3,260.00 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 1,090,000.00 USD | 0.00 USD | 2,550.00 USD | `-20.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 1,090,000.00 USD | 0.00 USD | 229.92 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 1,090,000.00 USD | 0.00 USD | 8,010.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 1,080,000.00 USD | 0.00 USD | 11,610.00 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 1,070,000.00 USD | 0.00 USD | 111.19 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 1,070,000.00 USD | 0.00 USD | 326.86 USD | `-15.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 1,070,000.00 USD | 0.00 USD | 2,710.00 USD | `-14.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 1,060,000.00 USD | 0.00 USD | 335.56 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 1,060,000.00 USD | 0.00 USD | 919.50 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 1,060,000.00 USD | 0.00 USD | 193.11 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 1,060,000.00 USD | 0.00 USD | 15,150.00 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 1,050,000.00 USD | 0.00 USD | 147.32 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 1,050,000.00 USD | 0.00 USD | 12,200.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 1,040,000.00 USD | 0.00 USD | 6,530.00 USD | `-11.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 1,030,000.00 USD | 0.00 USD | 524,570.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 504,450.00 USD | 0.00 USD | 1,270.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 503,180.00 USD | 0.00 USD | 53,690.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 449,490.00 USD | 0.00 USD | 1,780.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 447,710.00 USD | 0.00 USD | 6,100.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 441,620.00 USD | 0.00 USD | 850.90 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 440,770.00 USD | 0.00 USD | 1,040.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 439,720.00 USD | 0.00 USD | 6,220.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 433,500.00 USD | 0.00 USD | 10,000.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 423,500.00 USD | 0.00 USD | 43,570.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 379,940.00 USD | 0.00 USD | 131.90 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 379,800.00 USD | 0.00 USD | 4,710.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 375,090.00 USD | 0.00 USD | 3,220.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 371,870.00 USD | 0.00 USD | 63,670.00 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 308,200.00 USD | 0.00 USD | 6,130.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 302,070.00 USD | 0.00 USD | 6,770.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 295,300.00 USD | 0.00 USD | 996.01 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 294,300.00 USD | 0.00 USD | 2,100.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 292,200.00 USD | 0.00 USD | 949.53 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 291,250.00 USD | 0.00 USD | 100.11 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 291,150.00 USD | 0.00 USD | 135.99 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 291,010.00 USD | 0.00 USD | 1,010.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 290,000.00 USD | 0.00 USD | 5,640.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 284,370.00 USD | 0.00 USD | 174,860.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 109,510.00 USD | 0.00 USD | 34,710.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 74,790.00 USD | 0.00 USD | 32,490.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3385` | 42,310.00 USD | 0.00 USD | 157.74 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3395` | 42,150.00 USD | 0.00 USD | 3,380.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3405` | 38,770.00 USD | 0.00 USD | 3,870.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3415` | 34,900.00 USD | 0.00 USD | 486.30 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3425` | 34,410.00 USD | 0.00 USD | 359.28 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3435` | 34,050.00 USD | 0.00 USD | 828.18 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3445` | 33,230.00 USD | 0.00 USD | 1,950.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3455` | 31,280.00 USD | 0.00 USD | 3,980.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3465` | 27,300.00 USD | 0.00 USD | 555.44 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3475` | 26,750.00 USD | 0.00 USD | 1,280.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3485` | 25,470.00 USD | 0.00 USD | 1,160.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3495` | 24,310.00 USD | 0.00 USD | 1,570.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3505` | 22,740.00 USD | 0.00 USD | 2,430.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3515` | 20,300.00 USD | 0.00 USD | 919.52 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3525` | 19,380.00 USD | 0.00 USD | 19,380.00 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 494.90 USD | 494.90 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 1,260.00 USD | 769.97 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 3,840.00 USD | 2,580.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 43,270.00 USD | 39,430.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 83,660.00 USD | 40,390.00 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 86,970.00 USD | 3,310.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 88,000.00 USD | 1,030.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 90,940.00 USD | 2,940.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 91,170.00 USD | 224.49 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 92,330.00 USD | 1,170.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 95,810.00 USD | 3,480.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 138,380.00 USD | 42,570.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 149,550.00 USD | 11,170.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 158,820.00 USD | 9,270.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 159,150.00 USD | 321.70 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 173,480.00 USD | 14,330.00 USD | 0.00 USD | `+4.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 178,550.00 USD | 5,070.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 178,720.00 USD | 174.60 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 178,830.00 USD | 107.28 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 179,270.00 USD | 439.61 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 179,700.00 USD | 437.79 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 181,160.00 USD | 1,460.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 181,350.00 USD | 182.60 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 187,800.00 USD | 6,450.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 188,070.00 USD | 275.17 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 188,640.00 USD | 569.25 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 194,620.00 USD | 5,980.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 194,880.00 USD | 257.89 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 195,840.00 USD | 963.52 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 196,070.00 USD | 224.73 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 197,850.00 USD | 1,790.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 198,560.00 USD | 702.27 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 199,670.00 USD | 1,110.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 199,850.00 USD | 181.04 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 200,200.00 USD | 352.11 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 200,360.00 USD | 155.03 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 200,640.00 USD | 276.40 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 200,760.00 USD | 126.24 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 203,160.00 USD | 2,400.00 USD | 0.00 USD | `+12.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 204,180.00 USD | 1,010.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 206,180.00 USD | 2,010.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 259,060.00 USD | 52,880.00 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 259,930.00 USD | 864.28 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 263,850.00 USD | 3,920.00 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 343,180.00 USD | 79,330.00 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 344,380.00 USD | 1,200.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 345,580.00 USD | 1,200.00 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 345,710.00 USD | 138.07 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 346,980.00 USD | 1,270.00 USD | 0.00 USD | `+16.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 347,320.00 USD | 331.63 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 347,630.00 USD | 313.54 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 347,820.00 USD | 186.70 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 348,140.00 USD | 325.75 USD | 0.00 USD | `+21.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 348,330.00 USD | 183.82 USD | 0.00 USD | `+21.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 348,620.00 USD | 299.19 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 387,200.00 USD | 38,580.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 387,370.00 USD | 170.69 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 387,510.00 USD | 135.59 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 388,900.00 USD | 1,390.00 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 394,230.00 USD | 5,340.00 USD | 0.00 USD | `+28.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 395,710.00 USD | 1,470.00 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 476,480.00 USD | 80,770.00 USD | 0.00 USD | `+38.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 476,650.00 USD | 169.22 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 476,800.00 USD | 153.79 USD | 0.00 USD | `+40.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 477,520.00 USD | 724.89 USD | 0.00 USD | `+40.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 488,680.00 USD | 11,150.00 USD | 0.00 USD | `+41.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 490,600.00 USD | 1,930.00 USD | 0.00 USD | `+43.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 490,740.00 USD | 135.02 USD | 0.00 USD | `+50.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 490,980.00 USD | 240.85 USD | 0.00 USD | `+78.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 492,080.00 USD | 1,100.00 USD | 0.00 USD | `+79.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 505,690.00 USD | 13,610.00 USD | 0.00 USD | `+91.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6795` | 507,530.00 USD | 1,840.00 USD | 0.00 USD | `+92.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6835` | 508,520.00 USD | 991.76 USD | 0.00 USD | `+93.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6855` | 509,650.00 USD | 1,130.00 USD | 0.00 USD | `+94.19%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `420.77M` | Total OI Tokens: `1,193,395,931.0 TRX`
  * 1h OI Change: `+1.74%` | 4h OI Change: `+6.63%` | 24h OI Change: `+46.42%`
  * Exchange Breakdown: Binance=`115.32M` | Bybit=`86.01M` | OKX=`25.20M` | Hyperliquid=`20.11M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-655.09K` | Last 24h: `-591.71K` | Last 3d: `-625.30K` | Last 7d: `-857.35K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.3182%` | **USDT OKX** | `-0.7045%` |
| **USDT Bybit** | `-0.1344%` | **USDT KuCoin** | `-0.0323%` |
| **USDT MEXC** | `-0.3217%` | **USDT BingX** | `-0.5000%` |
| **USDT Gate** | `-0.1980%` | **USDT Bitget** | `-0.3669%` |
| **CoinM Binance** | `-0.5251%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `46.25%` | `53.75%` | `0.86` | 11,940,000.00 USD |
| `15M` | `Binance` | `51.23%` | `48.77%` | `1.05` | 5,390,000.00 USD |
| `15M` | `OKX` | `48.71%` | `51.29%` | `0.95` | 1,360,000.00 USD |
| `15M` | `Bybit` | `41.03%` | `58.97%` | `0.70` | 2,140,000.00 USD |
| `15M` | `KuCoin` | `44.41%` | `55.59%` | `0.80` | 191,920.00 USD |
| `15M` | `Gate` | `32.25%` | `67.75%` | `0.48` | 1,250,000.00 USD |
| `15M` | `Bitget` | `39.21%` | `60.79%` | `0.65` | 907,370.00 USD |
| `15M` | `BingX` | `25.68%` | `74.32%` | `0.35` | 55,250.00 USD |
| `15M` | `MEXC` | `51.23%` | `48.77%` | `1.05` | 186,970.00 USD |
| `15M` | `Bitunix` | `49.58%` | `50.42%` | `0.98` | 154,330.00 USD |
| `15M` | `Hyperliquid` | `60.75%` | `39.25%` | `1.55` | 143,590.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.96%` | `44.04%` | `1.27` | 32,680.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `89.92%` | `10.08%` | `8.92` | 11,900.00 USD |
| `15M` | `HTX` | `42.45%` | `57.55%` | `0.74` | 64,520.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `28.67%` | `71.33%` | `0.40` | 7,600.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `91.34%` | `8.66%` | `10.55` | 52,040.00 USD |
| `15M` | `Whale Positions` | `51.23%` | `48.77%` | `1.05` | 5,390,000.00 USD |
| `15M` | `Global Accounts` | `46.25%` | `53.75%` | `0.86` | 11,940,000.00 USD |
| `1H` | `TRX` | `46.97%` | `53.03%` | `0.89` | 41,730,000.00 USD |
| `1H` | `Binance` | `49.61%` | `50.39%` | `0.98` | 16,260,000.00 USD |
| `1H` | `OKX` | `49.75%` | `50.25%` | `0.99` | 4,200,000.00 USD |
| `1H` | `Bybit` | `49.83%` | `50.17%` | `0.99` | 9,250,000.00 USD |
| `1H` | `KuCoin` | `48.09%` | `51.91%` | `0.93` | 722,430.00 USD |
| `1H` | `Gate` | `35.36%` | `64.64%` | `0.55` | 4,610,000.00 USD |
| `1H` | `Bitget` | `44.31%` | `55.69%` | `0.80` | 2,730,000.00 USD |
| `1H` | `BingX` | `18.92%` | `81.08%` | `0.23` | 529,420.00 USD |
| `1H` | `MEXC` | `48.07%` | `51.93%` | `0.93` | 635,500.00 USD |
| `1H` | `Bitunix` | `39.54%` | `60.46%` | `0.65` | 576,770.00 USD |
| `1H` | `Hyperliquid` | `52.32%` | `47.68%` | `1.10` | 922,880.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.92%` | `57.08%` | `0.75` | 623,010.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `32.09%` | `67.91%` | `0.47` | 133,210.00 USD |
| `1H` | `HTX` | `38.86%` | `61.14%` | `0.64` | 209,840.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.8%` | `45.2%` | `1.21` | 1,880.00 USD |
| `1H` | `Aster` | `38.49%` | `61.51%` | `0.63` | 58,490.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.87%` | `57.13%` | `0.75` | 275,090.00 USD |
| `1H` | `Whale Positions` | `49.61%` | `50.39%` | `0.98` | 16,260,000.00 USD |
| `1H` | `Global Accounts` | `46.97%` | `53.03%` | `0.89` | 41,730,000.00 USD |
| `4H` | `TRX` | `50.77%` | `49.23%` | `1.03` | 223,620,000.00 USD |
| `4H` | `Binance` | `52.08%` | `47.92%` | `1.09` | 80,880,000.00 USD |
| `4H` | `OKX` | `50.25%` | `49.75%` | `1.01` | 20,880,000.00 USD |
| `4H` | `Bybit` | `52.27%` | `47.73%` | `1.10` | 28,940,000.00 USD |
| `4H` | `KuCoin` | `48.51%` | `51.49%` | `0.94` | 1,960,000.00 USD |
| `4H` | `Gate` | `46.07%` | `53.93%` | `0.85` | 8,400,000.00 USD |
| `4H` | `Bitget` | `52.78%` | `47.22%` | `1.12` | 10,170,000.00 USD |
| `4H` | `BingX` | `41.78%` | `58.22%` | `0.72` | 7,980,000.00 USD |
| `4H` | `MEXC` | `49.31%` | `50.69%` | `0.97` | 12,990,000.00 USD |
| `4H` | `Bitunix` | `48.44%` | `51.56%` | `0.94` | 6,200,000.00 USD |
| `4H` | `Hyperliquid` | `54.39%` | `45.61%` | `1.19` | 2,520,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.42%` | `50.58%` | `0.98` | 39,170,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `32.75%` | `67.25%` | `0.49` | 870,660.00 USD |
| `4H` | `HTX` | `49.19%` | `50.81%` | `0.97` | 854,430.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `58.93%` | `41.07%` | `1.43` | 1,110,000.00 USD |
| `4H` | `Aster` | `24.08%` | `75.92%` | `0.32` | 557,690.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.72%` | `47.28%` | `1.12` | 146,460.00 USD |
| `4H` | `Whale Positions` | `52.08%` | `47.92%` | `1.09` | 80,880,000.00 USD |
| `4H` | `Global Accounts` | `50.77%` | `49.23%` | `1.03` | 223,620,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3569` | `0.3560` | `0.3569` | `0.3597` | `0.3516` | 6,905,900.10 USD | 3,419,045.32 USD | 3,486,854.78 USD | -67,809.47 USD | `-0.98%` | `7B / 10S` |
| `5:00 UTC` | `0.3569` | `0.3557` | `0.3569` | `0.3573` | `0.3538` | 3,113,295.36 USD | 1,603,340.17 USD | 1,509,955.19 USD | 93,384.98 USD | `+3.00%` | `23B / 15S` |
| `0:00 UTC` | `0.3561` | `0.3570` | `0.3561` | `0.3589` | `0.3549` | 2,900,250.45 USD | 1,473,071.99 USD | 1,427,178.46 USD | 45,893.52 USD | `+1.58%` | `30B / 17S` |
| `5:00 UTC` | `0.3597` | `0.3579` | `0.3597` | `0.3599` | `0.3549` | 3,146,983.44 USD | 1,605,139.22 USD | 1,541,844.22 USD | 63,295.00 USD | `+2.01%` | `14B / 4S` |
| `0:00 UTC` | `0.3573` | `0.3571` | `0.3573` | `0.3587` | `0.3551` | 3,159,686.58 USD | 1,607,357.36 USD | 1,552,329.22 USD | 55,028.14 USD | `+1.74%` | `11B / 26S` |
| `5:00 UTC` | `0.3551` | `0.3543` | `0.3551` | `0.3561` | `0.3515` | 3,963,398.63 USD | 1,776,100.41 USD | 2,187,298.22 USD | -411,197.81 USD | `-10.37%` | `5B / 21S` |
| `0:00 UTC` | `0.3520` | `0.3514` | `0.3520` | `0.3534` | `0.3499` | 4,774,258.73 USD | 2,385,646.34 USD | 2,388,612.39 USD | -2,966.06 USD | `-0.06%` | `18B / 14S` |
| `5:00 UTC` | `0.3528` | `0.3532` | `0.3528` | `0.3548` | `0.3511` | 2,568,313.45 USD | 1,243,630.68 USD | 1,324,682.77 USD | -81,052.09 USD | `-3.16%` | `19B / 34S` |
| `0:00 UTC` | `0.3524` | `0.3518` | `0.3524` | `0.3549` | `0.3493` | 4,212,194.59 USD | 2,183,257.63 USD | 2,028,936.96 USD | 154,320.67 USD | `+3.66%` | `11B / 11S` |
| `5:00 UTC` | `0.3538` | `0.3526` | `0.3538` | `0.3540` | `0.3507` | 612,635.77 USD | 381,876.13 USD | 230,759.63 USD | 151,116.50 USD | `+24.67%` | `45B / 18S` |

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
| `5m` | 378,660.00 USD | -82,600.00 USD | **`ACCUMULATION`** |
| `15m` | 1,020,000.00 USD | 175,400.00 USD | **`ACCUMULATION`** |
| `30m` | 1,490,000.00 USD | 737,010.00 USD | **`ACCUMULATION`** |
| `1h` | 3,190,000.00 USD | 20,570.00 USD | **`ACCUMULATION`** |
| `2h` | 5,250,000.00 USD | -163,910.00 USD | **`ACCUMULATION`** |
| `4h` | 7,970,000.00 USD | 5,510,000.00 USD | **`ACCUMULATION`** |
| `6h` | 12,480,000.00 USD | 6,560,000.00 USD | **`ACCUMULATION`** |
| `8h` | 10,400,000.00 USD | 12,910,000.00 USD | **`ACCUMULATION`** |
| `12h` | 11,010,000.00 USD | 12,900,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,210,000.00 USD | 14,340,000.00 USD | **`ACCUMULATION`** |
| `1w` | 5,380,000.00 USD | 12,660,000.00 USD | **`ACCUMULATION`** |
| `30d` | -14,230,000.00 USD | 14,890,000.00 USD | **`ACCUMULATION`** |

* Spot Capital Netflows: 5m=`+378.66K` | 15m=`+1.02M` | 1h=`+3.19M` | 24h=`+12.21M`
* Futures Capital Netflows: 5m=`-82.60K` | 15m=`+175.40K` | 1h=`+20.57K` | 24h=`+14.34M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3459` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3345` (Risk Distance: `0.0114` pts)
  * +2.5R Take Profit: `0.3743`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3572` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3686` (Risk Distance: `0.0114` pts)
  * +2.5R Take Profit: `0.3288`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3548`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
