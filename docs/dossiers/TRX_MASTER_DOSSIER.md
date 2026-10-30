# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3341` | **Live Ask Quote**: `0.3374` | **Mid Price**: `0.3357`
- **Spread Points**: `33.00` | **Spread BPS**: `98.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3516` | VWAP Z-Score: `-3.23` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0035` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.06` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3642` | Lower -3.00σ Band: `0.3389`
  * Upper +2.51σ Band: `0.3622` | Lower -2.51σ Band: `0.3410`
  * Upper +2.01σ Band: `0.3601` | Lower -2.01σ Band: `0.3431`
  * Upper +2.00σ Band: `0.3600` | Lower -2.00σ Band: `0.3431`
  * Upper +1.28σ Band: `0.3570` | Lower -1.28σ Band: `0.3462`
  * Upper +1.00σ Band: `0.3558` | Lower -1.00σ Band: `0.3473`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3425` | EMA-20=`0.3454` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3437` (Slope: `+0.0000`) | EMA-100=`0.3395`
  * Institutional Anchors: EMA-144=`0.3373` | EMA-200=`0.3356` (Slope: `+0.3356`) | EMA-233=`0.3348`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3571` (Distance: `-5.36%`)
  * Point of Control (POC) = `0.3513` (Distance: `-3.79%`)
  * Value Area Low (VAL) = `0.3448` (Distance: `-2.00%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3477` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3331`
  * New York Session (13:00-21:00 UTC): High=`0.3378` | Low=`0.3337`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3344` - `0.3371`
  * Optimal Trade Entry (OTE 0.705): `0.3364`
  * Structural Invalidation Anchor (0.786): `0.3384`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3381` | `0.3382` | `0.3366` | `0.3366` | `8,358,962` | 2,820,554.99 USD | -1,299,979.90 USD | `-46.09%` | -1,125,951.55 USD | `-1.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3366` | `0.3366` | `0.3342` | `0.3355` | `12,243,586` | 4,102,564.29 USD | -1,050,948.56 USD | `-25.62%` | -2,176,900.11 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3355` | `0.3378` | `0.3338` | `0.3373` | `12,285,907` | 4,117,731.58 USD | 13,275.81 USD | `+0.32%` | -2,163,624.30 USD | `+0.60` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3407` | `0.3411` | `0.3393` | `0.3405` | `15,500,455` | 5,271,834.49 USD | -1,312,014.12 USD | `-24.89%` | 2,025,386.08 USD | `-1.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3404` | `0.3406` | `0.3381` | `0.3381` | `13,819,873` | 4,684,490.06 USD | -1,851,357.72 USD | `-39.52%` | 174,028.36 USD | `-2.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3381` | `0.3382` | `0.3338` | `0.3375` | `32,919,150` | 11,051,207.20 USD | -2,328,609.84 USD | `-21.07%` | -2,154,581.48 USD | `-2.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3495` | `0.3497` | `0.3444` | `0.3458` | `45,347,497` | 15,724,010.32 USD | -13,807.83 USD | `-0.09%` | 4,647,136.13 USD | `-0.19` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3458` | `0.3460` | `0.3381` | `0.3381` | `54,065,624` | 18,425,452.39 USD | -4,585,214.81 USD | `-24.89%` | 61,921.32 USD | `-2.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3381` | `0.3382` | `0.3338` | `0.3375` | `32,919,150` | 11,051,207.20 USD | -2,328,609.84 USD | `-21.07%` | -2,266,688.52 USD | `-1.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3338` | `0.3373` | `132,351,021` | 45,206,994.18 USD | -6,933,956.75 USD | `-15.34%` | -2,077,270.00 USD | `-2.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 385,562.36 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 597,653.23 USD | `+0.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,748,501.15 USD | `+1.71` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,856,686.75 USD | `+1.19` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3338` | `0.3373` | `132,351,021` | 45,206,994.18 USD | -6,933,956.75 USD | `-15.34%` | -2,077,270.00 USD | `-2.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.3357`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `965` | `0xecb6...2b00` | `LONG` | 2,306,035.47 USD | `6,838,371.00` | `0.3343` | `0.3371` | `0.000000` | 19,643.36 USD | `+0.85%` | `10X Cross` |
| `1577` | `0xeadc...9d55` | `LONG` | 1,351,440.00 USD | `4,000,000.00` | `0.3421` | `0.3371` | `0.000000` | -17,038.09 USD | `-1.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3305` | 5,355.08 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.36K USD at 0.3305 USD [API] | `2026-10-29 03:26:26` |
| `ANNOUNCEMENT` | `INFO` | `0.3313` | 6,465.71 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3313 USD [API] | `2026-10-29 07:47:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.20%`) | Long MP=`0.3328` (Vol: 651,900.00 USD, Dist: `--2.01%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.20%`) | Long MP=`0.3249` (Vol: 801,900.00 USD, Dist: `--4.36%`)
  * 3D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+7.79%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--4.36%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+7.79%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--4.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0795` | 3,250.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 7,900.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 967.79 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 391.44 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 10,330.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 208.12 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 6,230.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 34,700.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 20,240.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 3,410.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 1,150.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 11,100.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,020.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,170.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 431.37 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 208.67 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1925` | 79,260.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 183.06 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2095` | 218.93 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 512.82 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 1,700.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 726.42 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 6,120.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 2,790.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 1,260.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 139.35 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 2,890.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 464.79 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 101.06 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,520.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 2,100.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 108.15 USD | 999,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,210.00 USD | 998,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 449.23 USD | 996,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 193.75 USD | 996,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 27,310.00 USD | 996,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,510.00 USD | 968,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,690.00 USD | 965,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 301.09 USD | 880,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 13,010.00 USD | 880,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 867,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 605.32 USD | 861,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 15,010.00 USD | 860,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 1,420.00 USD | 845,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 911.60 USD | 843,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 5,780.00 USD | 843,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 2,220.00 USD | 837,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 835,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2923` | 25,780,000.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 834,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 833,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2947` | 25,710,000.00 USD | 25,710,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2953` | 25,650,000.00 USD | 25,650,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 147.75 USD | 833,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 25,560,000.00 USD | 25,560,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 25,420,000.00 USD | 25,420,000.00 USD | 122,540.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 157.14 USD | 833,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 25,200,000.00 USD | 25,200,000.00 USD | 137,530.00 USD | 37,780.00 USD | 57,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2975` | 1,010.00 USD | 833,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2977` | 24,970,000.00 USD | 24,970,000.00 USD | 69,090.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 24,860,000.00 USD | 24,860,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 127.46 USD | 832,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2989` | 24,640,000.00 USD | 24,640,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 24,480,000.00 USD | 24,480,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 831.71 USD | 832,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,290.00 USD | 831,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 24,470,000.00 USD | 24,470,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3008` | 11,680,000.00 USD | 11,680,000.00 USD | 13,540.00 USD | 0.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 328.03 USD | 821,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3018` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,620.00 USD | 820,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3028` | 11,640,000.00 USD | 11,640,000.00 USD | 454.78 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3033` | 11,640,000.00 USD | 11,640,000.00 USD | 332.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3043` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 17,840.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 405.59 USD | 818,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3048` | 11,580,000.00 USD | 11,580,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 24,440,000.00 USD | 24,440,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3053` | 11,500,000.00 USD | 11,500,000.00 USD | 18,730.00 USD | 13,030.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 24,390,000.00 USD | 24,390,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 817,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 24,390,000.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3063` | 11,430,000.00 USD | 11,430,000.00 USD | 885.25 USD | 16,530.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 24,310,000.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3068` | 11,360,000.00 USD | 11,360,000.00 USD | 31,110.00 USD | 15,440.00 USD | 48,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 11,260,000.00 USD | 11,260,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 24,310,000.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 6,650.00 USD | 803,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3078` | 11,240,000.00 USD | 11,240,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 24,300,000.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 11,230,000.00 USD | 11,230,000.00 USD | 18,640.00 USD | 0.00 USD | 28,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 24,200,000.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 2,010.00 USD | 796,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3088` | 11,190,000.00 USD | 11,190,000.00 USD | 707.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 24,200,000.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 11,190,000.00 USD | 11,190,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 794,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3097` | 24,190,000.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3098` | 11,170,000.00 USD | 11,170,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 11,170,000.00 USD | 11,170,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 24,170,000.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 137.86 USD | 794,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 24,030,000.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3113` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 24,030,000.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 794,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3118` | 11,050,000.00 USD | 11,050,000.00 USD | 12,410.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 23,990,000.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 11,010,000.00 USD | 11,010,000.00 USD | 24,290.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,630.00 USD | 780,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 23,810,000.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3128` | 10,950,000.00 USD | 10,950,000.00 USD | 424.13 USD | 39,470.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 26,460.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 23,690,000.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 540.16 USD | 762,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3138` | 10,840,000.00 USD | 10,840,000.00 USD | 952.52 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 23,680,000.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 10,830,000.00 USD | 10,830,000.00 USD | 1,280.00 USD | 3,580.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 23,680,000.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 141.84 USD | 762,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3148` | 10,820,000.00 USD | 10,820,000.00 USD | 644.30 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 23,360,000.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3153` | 10,810,000.00 USD | 10,810,000.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,490.00 USD | 762,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3157` | 23,110,000.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3158` | 10,770,000.00 USD | 10,770,000.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 10,750,000.00 USD | 10,750,000.00 USD | 248.58 USD | 33,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 22,560,000.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 760,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3168` | 10,710,000.00 USD | 10,710,000.00 USD | 43,210.00 USD | 10,820.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 21,710,000.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 10,630,000.00 USD | 10,630,000.00 USD | 23,670.00 USD | 33,870.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 20,910,000.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3178` | 10,540,000.00 USD | 10,540,000.00 USD | 64,070.00 USD | 13,580.00 USD | 44,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 20,590,000.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 10,420,000.00 USD | 10,420,000.00 USD | 376,020.00 USD | 71,770.00 USD | 97,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 19,600,000.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3188` | 9,880,000.00 USD | 9,880,000.00 USD | 43,050.00 USD | 36,160.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 9,750,000.00 USD | 9,750,000.00 USD | 74,100.00 USD | 3,120.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 19,130,000.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3198` | 9,650,000.00 USD | 9,650,000.00 USD | 56,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3203` | 9,590,000.00 USD | 9,590,000.00 USD | 208,350.00 USD | 26,000.00 USD | 34,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 18,830,000.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3208` | 9,320,000.00 USD | 9,320,000.00 USD | 132,330.00 USD | 13,040.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 18,730,000.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3213` | 9,120,000.00 USD | 9,120,000.00 USD | 1,300.00 USD | 20,180.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 17,860,000.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3218` | 9,000,000.00 USD | 9,000,000.00 USD | 5,550.00 USD | 21,490.00 USD | 87,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 8,890,000.00 USD | 8,890,000.00 USD | 118,980.00 USD | 13,780.00 USD | 176,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 17,410,000.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3225` | 128.03 USD | 759,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3228` | 8,580,000.00 USD | 8,580,000.00 USD | 21,530.00 USD | 46,020.00 USD | 168,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 16,490,000.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 8,340,000.00 USD | 8,340,000.00 USD | 56,470.00 USD | 6,250.00 USD | 34,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 15,100,000.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3238` | 8,250,000.00 USD | 8,250,000.00 USD | 6,420.00 USD | 81,890.00 USD | 150,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 13,520,000.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 8,010,000.00 USD | 8,010,000.00 USD | 125,350.00 USD | 41,210.00 USD | 191,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 12,730,000.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3248` | 7,650,000.00 USD | 7,650,000.00 USD | 714,450.00 USD | 114,830.00 USD | 235,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 6,580,000.00 USD | 6,580,000.00 USD | 424,900.00 USD | 91,650.00 USD | 334,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 11,400,000.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3258` | 5,730,000.00 USD | 5,730,000.00 USD | 101,780.00 USD | 36,240.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 10,060,000.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3263` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 9,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 9,680,000.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3268` | 5,380,000.00 USD | 5,380,000.00 USD | 124,870.00 USD | 87,680.00 USD | 279,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 9,490,000.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3273` | 4,890,000.00 USD | 4,890,000.00 USD | 38,550.00 USD | 50,640.00 USD | 201,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 6,260.00 USD | 759,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3278` | 4,600,000.00 USD | 4,600,000.00 USD | 213,460.00 USD | 31,950.00 USD | 115,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 36,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 9,290,000.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 753,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3288` | 4,200,000.00 USD | 4,200,000.00 USD | 84,680.00 USD | 0.00 USD | 185,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3293` | 3,930,000.00 USD | 3,930,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 8,900,000.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 2,030.00 USD | 8,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3301` | 8,870,000.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3303` | 3,850,000.00 USD | 3,850,000.00 USD | 37,670.00 USD | 0.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 8,800,000.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3308` | 3,800,000.00 USD | 3,800,000.00 USD | 214,030.00 USD | 39,540.00 USD | 203,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 3,350,000.00 USD | 3,350,000.00 USD | 142,970.00 USD | 117,000.00 USD | 271,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 8,460,000.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3315` | 5,420.00 USD | 6,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3318` | 2,810,000.00 USD | 2,810,000.00 USD | 159,340.00 USD | 54,860.00 USD | 295,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3323` | 2,300,000.00 USD | 2,300,000.00 USD | 106,340.00 USD | 87,940.00 USD | 44,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3325` | 8,150,000.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3325` | 634.08 USD | 749.48 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3328` | 2,070,000.00 USD | 2,070,000.00 USD | 62,020.00 USD | 33,750.00 USD | 286,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3331` | 7,890,000.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3333` | 1,680,000.00 USD | 1,680,000.00 USD | 38,930.00 USD | 58,300.00 USD | 340,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3337` | 7,230,000.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3338` | 1,250,000.00 USD | 1,250,000.00 USD | 223,020.00 USD | 224,220.00 USD | 251,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 547,620.00 USD | 547,620.00 USD | 932.61 USD | 134,220.00 USD | 87,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3343` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3345` | 115.40 USD | 115.40 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3348` | 324,670.00 USD | 324,670.00 USD | 277,800.00 USD | 46,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3349` | 6,610,000.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3353` | 181,600.00 USD | 181,600.00 USD | 0.00 USD | 22,780.00 USD | 158,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3355` | 6,380,000.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3358` | 615,830.00 USD | 615,830.00 USD | 267,520.00 USD | 22,430.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 6,110,000.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3363` | 730,170.00 USD | 730,170.00 USD | 46,870.00 USD | 67,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3367` | 6,110,000.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3368` | 1,080,000.00 USD | 1,080,000.00 USD | 282,270.00 USD | 29,430.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3373` | 1,210,000.00 USD | 1,210,000.00 USD | 859.70 USD | 107,280.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3373` | 5,860,000.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3378` | 1,880,000.00 USD | 1,880,000.00 USD | 619,770.00 USD | 31,130.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3379` | 5,270,000.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 2,280,000.00 USD | 2,280,000.00 USD | 232,810.00 USD | 114,980.00 USD | 49,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3385` | 4,610,000.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3388` | 2,420,000.00 USD | 2,420,000.00 USD | 32,800.00 USD | 44,920.00 USD | 59,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3391` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3393` | 2,700,000.00 USD | 2,700,000.00 USD | 65,650.00 USD | 45,920.00 USD | 168,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3397` | 3,970,000.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3398` | 3,180,000.00 USD | 3,180,000.00 USD | 144,030.00 USD | 0.00 USD | 337,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3403` | 3,570,000.00 USD | 3,570,000.00 USD | 187,960.00 USD | 0.00 USD | 198,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3403` | 3,280,000.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3408` | 3,670,000.00 USD | 3,670,000.00 USD | 71,510.00 USD | 0.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3409` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3413` | 3,920,000.00 USD | 3,920,000.00 USD | 181,530.00 USD | 0.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3415` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3418` | 4,530,000.00 USD | 4,530,000.00 USD | 585,390.00 USD | 0.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 11,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3427` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3428` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 179,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 156,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3438` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 49,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3439` | 733,270.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 29,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3448` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 72,750.00 USD | 58,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3451` | 538,440.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 24,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3458` | 5,500,000.00 USD | 5,500,000.00 USD | 1,150.00 USD | 12,550.00 USD | 370,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3468` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 7,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 37,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3478` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 37,720.00 USD | 111,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3483` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 9,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3488` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 8,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3493` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3498` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 454,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3503` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3508` | 6,330,000.00 USD | 6,330,000.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3518` | 6,410,000.00 USD | 6,410,000.00 USD | 21,910.00 USD | 0.00 USD | 29,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 6,410,000.00 USD | 6,410,000.00 USD | 396.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3528` | 6,460,000.00 USD | 6,460,000.00 USD | 25,310.00 USD | 31,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 6,680,000.00 USD | 6,680,000.00 USD | 62,410.00 USD | 64,680.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3538` | 6,960,000.00 USD | 6,960,000.00 USD | 58,450.00 USD | 29,120.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3543` | 7,190,000.00 USD | 7,190,000.00 USD | 75,280.00 USD | 119,750.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3548` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 41,620.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 7,370,000.00 USD | 7,370,000.00 USD | 20,180.00 USD | 36,790.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3558` | 7,450,000.00 USD | 7,450,000.00 USD | 331.60 USD | 45,890.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3563` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 29,510.00 USD | 115,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3568` | 7,600,000.00 USD | 7,600,000.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3573` | 7,740,000.00 USD | 7,740,000.00 USD | 131,970.00 USD | 16,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3578` | 7,810,000.00 USD | 7,810,000.00 USD | 29,800.00 USD | 9,130.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 7,850,000.00 USD | 7,850,000.00 USD | 10,960.00 USD | 14,930.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3588` | 7,870,000.00 USD | 7,870,000.00 USD | 1,810.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3593` | 8,060,000.00 USD | 8,060,000.00 USD | 64,080.00 USD | 0.00 USD | 133,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3598` | 8,240,000.00 USD | 8,240,000.00 USD | 90,790.00 USD | 22,780.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3603` | 8,450,000.00 USD | 8,450,000.00 USD | 31,030.00 USD | 41,780.00 USD | 136,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3608` | 8,720,000.00 USD | 8,720,000.00 USD | 77,290.00 USD | 39,250.00 USD | 157,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 9,060,000.00 USD | 9,060,000.00 USD | 37,640.00 USD | 63,400.00 USD | 236,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3618` | 9,450,000.00 USD | 9,450,000.00 USD | 225,600.00 USD | 56,810.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 9,830,000.00 USD | 9,830,000.00 USD | 226,400.00 USD | 79,900.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3625` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3628` | 11,010,000.00 USD | 11,010,000.00 USD | 1,060,000.00 USD | 74,470.00 USD | 55,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 11,530,000.00 USD | 11,530,000.00 USD | 223,360.00 USD | 72,670.00 USD | 223,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,560.00 USD | 33,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3638` | 11,860,000.00 USD | 11,860,000.00 USD | 183,690.00 USD | 65,110.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 12,270,000.00 USD | 12,270,000.00 USD | 167,490.00 USD | 211,440.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 45,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3648` | 12,730,000.00 USD | 12,730,000.00 USD | 259,960.00 USD | 71,710.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3653` | 13,270,000.00 USD | 13,270,000.00 USD | 286,780.00 USD | 19,500.00 USD | 236,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3658` | 13,870,000.00 USD | 13,870,000.00 USD | 289,040.00 USD | 152,150.00 USD | 156,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3663` | 14,430,000.00 USD | 14,430,000.00 USD | 448,400.00 USD | 99,430.00 USD | 16,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,160.00 USD | 46,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3668` | 14,990,000.00 USD | 14,990,000.00 USD | 257,230.00 USD | 48,270.00 USD | 253,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 15,350,000.00 USD | 15,350,000.00 USD | 45,880.00 USD | 106,060.00 USD | 203,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,960.00 USD | 48,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3678` | 16,080,000.00 USD | 16,080,000.00 USD | 497,170.00 USD | 45,130.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3683` | 16,590,000.00 USD | 16,590,000.00 USD | 269,310.00 USD | 81,750.00 USD | 161,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3685` | 220.73 USD | 48,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3688` | 17,520,000.00 USD | 17,520,000.00 USD | 715,890.00 USD | 144,580.00 USD | 68,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3693` | 17,680,000.00 USD | 17,680,000.00 USD | 79,910.00 USD | 49,680.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3698` | 18,070,000.00 USD | 18,070,000.00 USD | 313,650.00 USD | 81,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 18,940,000.00 USD | 18,940,000.00 USD | 589,850.00 USD | 196,170.00 USD | 84,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 49,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3708` | 19,570,000.00 USD | 19,570,000.00 USD | 110,690.00 USD | 21,340.00 USD | 497,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3713` | 20,950,000.00 USD | 20,950,000.00 USD | 481,410.00 USD | 90,010.00 USD | 804,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 2,040.00 USD | 51,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3718` | 21,490,000.00 USD | 21,490,000.00 USD | 43,980.00 USD | 226,350.00 USD | 274,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3723` | 21,970,000.00 USD | 21,970,000.00 USD | 327,290.00 USD | 58,560.00 USD | 89,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 366.17 USD | 51,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3728` | 23,050,000.00 USD | 23,050,000.00 USD | 178,580.00 USD | 106,520.00 USD | 802,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 23,880,000.00 USD | 23,880,000.00 USD | 110,390.00 USD | 58,740.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 44,580.00 USD | 96,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3738` | 24,420,000.00 USD | 24,420,000.00 USD | 154,860.00 USD | 158,380.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3743` | 24,770,000.00 USD | 24,770,000.00 USD | 32,620.00 USD | 43,590.00 USD | 276,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 140.06 USD | 96,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3748` | 25,550,000.00 USD | 25,550,000.00 USD | 30,710.00 USD | 20,770.00 USD | 724,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3753` | 25,940,000.00 USD | 25,940,000.00 USD | 363,100.00 USD | 0.00 USD | 31,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 6,120.00 USD | 102,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3758` | 26,450,000.00 USD | 26,450,000.00 USD | 186,760.00 USD | 72,840.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 27,480,000.00 USD | 27,480,000.00 USD | 140,730.00 USD | 24,840.00 USD | 859,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3768` | 27,540,000.00 USD | 27,540,000.00 USD | 20,560.00 USD | 32,810.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3773` | 27,620,000.00 USD | 27,620,000.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 32,300.00 USD | 134,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3778` | 27,850,000.00 USD | 27,850,000.00 USD | 1,210.00 USD | 0.00 USD | 230,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3783` | 27,870,000.00 USD | 27,870,000.00 USD | 16,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,530.00 USD | 691,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3788` | 28,380,000.00 USD | 28,380,000.00 USD | 220,670.00 USD | 0.00 USD | 289,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 28,580,000.00 USD | 28,580,000.00 USD | 54,830.00 USD | 96,440.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3798` | 28,580,000.00 USD | 28,580,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3803` | 28,910,000.00 USD | 28,910,000.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3808` | 28,950,000.00 USD | 28,950,000.00 USD | 855.55 USD | 17,210.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3813` | 28,990,000.00 USD | 28,990,000.00 USD | 23,970.00 USD | 2,560.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3818` | 29,020,000.00 USD | 29,020,000.00 USD | 11,830.00 USD | 3,560.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3823` | 29,310,000.00 USD | 29,310,000.00 USD | 932.61 USD | 35,920.00 USD | 246,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3828` | 29,340,000.00 USD | 29,340,000.00 USD | 1,720.00 USD | 26,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3833` | 29,570,000.00 USD | 29,570,000.00 USD | 0.00 USD | 10,610.00 USD | 219,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 691,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3838` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3843` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3850` | 29,600,000.00 USD | 29,600,000.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3865` | 265.53 USD | 691,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 9,310.00 USD | 700,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 1,440.00 USD | 702,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3919` | 14,140,000.00 USD | 14,140,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 14,300,000.00 USD | 14,300,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 14,330,000.00 USD | 14,330,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 703,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 14,360,000.00 USD | 14,360,000.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 14,390,000.00 USD | 14,390,000.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 166,720.00 USD | 870,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 14,520,000.00 USD | 14,520,000.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 14,750,000.00 USD | 14,750,000.00 USD | 107,420.00 USD | 10,160.00 USD | 112,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 14,960,000.00 USD | 14,960,000.00 USD | 143,850.00 USD | 54,030.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3965` | 69,500.00 USD | 940,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3967` | 14,980,000.00 USD | 14,980,000.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 15,120,000.00 USD | 15,120,000.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 15,230,000.00 USD | 15,230,000.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 15,270,000.00 USD | 15,270,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4003` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4009` | 15,290,000.00 USD | 15,290,000.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4015` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,210.00 USD | 942,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 942,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 730.12 USD | 943,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 1,000.00 USD | 944,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4255` | 1,470.00 USD | 945,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4295` | 10,210.00 USD | 956,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 206.03 USD | 956,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 71,380.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 378.34 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 22,270.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 1,020.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 5,400.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 1,140.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4545` | 1,550.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4715` | 282,990.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4935` | 285.24 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4945` | 20,750.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 23,600.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5195` | 1,100.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5445` | 4,360.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5545` | 41,030.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5635` | 2,340.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5645` | 732,300.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5665` | 54,300.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6105` | 8,060.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 28,550.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6185` | 374.19 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6225` | 32,720.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 1,130.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 6,820.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 705.13 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6575` | 91,960.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6605` | 87,360.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6735` | 1,800.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6765` | 83,430.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0795` | 1,270,000.00 USD | 0.00 USD | 3,250.00 USD | `-76.34%` | `40,871.00` |
| `Live` | `Long` | `0.0875` | 1,260,000.00 USD | 0.00 USD | 7,900.00 USD | `-73.96%` | `90,312.00` |
| `Live` | `Long` | `0.0975` | 1,250,000.00 USD | 0.00 USD | 967.79 USD | `-70.99%` | `9,926.00` |
| `Live` | `Long` | `0.1165` | 1,250,000.00 USD | 0.00 USD | 391.44 USD | `-65.33%` | `3,360.00` |
| `Live` | `Long` | `0.1345` | 1,250,000.00 USD | 0.00 USD | 10,330.00 USD | `-59.98%` | `76,797.00` |
| `Live` | `Long` | `0.1475` | 1,240,000.00 USD | 0.00 USD | 208.12 USD | `-56.11%` | `1,411.00` |
| `Live` | `Long` | `0.1515` | 1,240,000.00 USD | 0.00 USD | 6,230.00 USD | `-54.92%` | `41,100.00` |
| `Live` | `Long` | `0.1565` | 1,240,000.00 USD | 0.00 USD | 34,700.00 USD | `-53.43%` | `221,745.00` |
| `Live` | `Long` | `0.1585` | 1,200,000.00 USD | 0.00 USD | 388.01 USD | `-52.83%` | `2,448.00` |
| `Live` | `Long` | `0.1695` | 1,200,000.00 USD | 0.00 USD | 20,240.00 USD | `-49.56%` | `119,400.00` |
| `Live` | `Long` | `0.1705` | 1,180,000.00 USD | 0.00 USD | 3,410.00 USD | `-49.26%` | `20,000.00` |
| `Live` | `Long` | `0.1715` | 1,180,000.00 USD | 0.00 USD | 1,150.00 USD | `-48.97%` | `6,706.00` |
| `Live` | `Long` | `0.1725` | 1,180,000.00 USD | 0.00 USD | 11,100.00 USD | `-48.67%` | `64,322.00` |
| `Live` | `Long` | `0.1735` | 1,170,000.00 USD | 0.00 USD | 339.71 USD | `-48.37%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,170,000.00 USD | 0.00 USD | 1,020.00 USD | `-48.07%` | `5,865.00` |
| `Live` | `Long` | `0.1755` | 1,160,000.00 USD | 0.00 USD | 4,170.00 USD | `-47.78%` | `23,777.00` |
| `Live` | `Long` | `0.1765` | 1,160,000.00 USD | 0.00 USD | 431.37 USD | `-47.48%` | `2,444.00` |
| `Live` | `Long` | `0.1785` | 1,160,000.00 USD | 0.00 USD | 208.67 USD | `-46.88%` | `1,169.00` |
| `Live` | `Long` | `0.1875` | 1,160,000.00 USD | 0.00 USD | 36,310.00 USD | `-44.20%` | `193,636.00` |
| `Live` | `Long` | `0.1925` | 1,120,000.00 USD | 0.00 USD | 79,260.00 USD | `-42.72%` | `411,722.00` |
| `Live` | `Long` | `0.1975` | 1,040,000.00 USD | 0.00 USD | 632.00 USD | `-41.23%` | `3,200.00` |
| `Live` | `Long` | `0.2025` | 1,040,000.00 USD | 0.00 USD | 183.06 USD | `-39.74%` | `904.00` |
| `Live` | `Long` | `0.2095` | 1,040,000.00 USD | 0.00 USD | 218.93 USD | `-37.66%` | `1,045.00` |
| `Live` | `Long` | `0.2175` | 1,040,000.00 USD | 0.00 USD | 1,520.00 USD | `-35.28%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,040,000.00 USD | 0.00 USD | 512.82 USD | `-34.98%` | `2,347.00` |
| `Live` | `Long` | `0.2245` | 1,040,000.00 USD | 0.00 USD | 4,570.00 USD | `-33.19%` | `20,360.00` |
| `Live` | `Long` | `0.2295` | 1,040,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.71%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-31.41%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,030,000.00 USD | 0.00 USD | 1,700.00 USD | `-30.81%` | `7,301.00` |
| `Live` | `Long` | `0.2335` | 1,030,000.00 USD | 0.00 USD | 726.42 USD | `-30.52%` | `3,111.00` |
| `Live` | `Long` | `0.2345` | 1,030,000.00 USD | 0.00 USD | 6,120.00 USD | `-30.22%` | `26,082.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 2,790.00 USD | `-29.92%` | `11,856.00` |
| `Live` | `Long` | `0.2365` | 1,020,000.00 USD | 0.00 USD | 344.11 USD | `-29.62%` | `1,455.00` |
| `Live` | `Long` | `0.2375` | 1,020,000.00 USD | 0.00 USD | 1,260.00 USD | `-29.33%` | `5,298.00` |
| `Live` | `Long` | `0.2395` | 1,020,000.00 USD | 0.00 USD | 151.36 USD | `-28.73%` | `632.00` |
| `Live` | `Long` | `0.2415` | 1,020,000.00 USD | 0.00 USD | 139.35 USD | `-28.14%` | `577.00` |
| `Live` | `Long` | `0.2425` | 1,020,000.00 USD | 0.00 USD | 2,890.00 USD | `-27.84%` | `11,927.00` |
| `Live` | `Long` | `0.2435` | 1,020,000.00 USD | 0.00 USD | 885.85 USD | `-27.54%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 1,020,000.00 USD | 0.00 USD | 464.79 USD | `-27.24%` | `1,901.00` |
| `Live` | `Long` | `0.2455` | 1,020,000.00 USD | 0.00 USD | 384.94 USD | `-26.95%` | `1,568.00` |
| `Live` | `Long` | `0.2465` | 1,020,000.00 USD | 0.00 USD | 101.06 USD | `-26.65%` | `410.00` |
| `Live` | `Long` | `0.2485` | 1,020,000.00 USD | 0.00 USD | 11,890.00 USD | `-26.05%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 1,000,000.00 USD | 0.00 USD | 262.02 USD | `-25.46%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 1,000,000.00 USD | 0.00 USD | 1,520.00 USD | `-23.97%` | `5,966.00` |
| `Live` | `Long` | `0.2595` | 1,000,000.00 USD | 0.00 USD | 749.18 USD | `-22.78%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 1,000,000.00 USD | 0.00 USD | 2,100.00 USD | `-22.18%` | `8,015.00` |
| `Live` | `Long` | `0.2625` | 999,040.00 USD | 0.00 USD | 108.15 USD | `-21.89%` | `412.00` |
| `Live` | `Long` | `0.2645` | 998,930.00 USD | 0.00 USD | 2,210.00 USD | `-21.29%` | `8,340.00` |
| `Live` | `Long` | `0.2655` | 996,730.00 USD | 0.00 USD | 449.23 USD | `-20.99%` | `1,692.00` |
| `Live` | `Long` | `0.2665` | 996,280.00 USD | 0.00 USD | 193.75 USD | `-20.70%` | `727.00` |
| `Live` | `Long` | `0.2675` | 996,080.00 USD | 0.00 USD | 27,310.00 USD | `-20.40%` | `102,082.00` |
| `Live` | `Long` | `0.2685` | 968,780.00 USD | 0.00 USD | 3,510.00 USD | `-20.10%` | `13,060.00` |
| `Live` | `Long` | `0.2745` | 965,270.00 USD | 0.00 USD | 84,690.00 USD | `-18.32%` | `308,536.00` |
| `Live` | `Long` | `0.2775` | 880,580.00 USD | 0.00 USD | 301.09 USD | `-17.42%` | `1,085.00` |
| `Live` | `Long` | `0.2785` | 880,270.00 USD | 0.00 USD | 13,010.00 USD | `-17.13%` | `46,725.00` |
| `Live` | `Long` | `0.2795` | 867,260.00 USD | 0.00 USD | 6,260.00 USD | `-16.83%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 861,010.00 USD | 0.00 USD | 605.32 USD | `-16.53%` | `2,158.00` |
| `Live` | `Long` | `0.2815` | 860,400.00 USD | 0.00 USD | 15,010.00 USD | `-16.23%` | `53,321.00` |
| `Live` | `Long` | `0.2825` | 845,390.00 USD | 0.00 USD | 1,420.00 USD | `-15.94%` | `5,038.00` |
| `Live` | `Long` | `0.2855` | 843,970.00 USD | 0.00 USD | 911.60 USD | `-15.04%` | `3,193.00` |
| `Live` | `Long` | `0.2875` | 843,060.00 USD | 0.00 USD | 5,780.00 USD | `-14.45%` | `20,120.00` |
| `Live` | `Long` | `0.2905` | 837,270.00 USD | 0.00 USD | 2,220.00 USD | `-13.55%` | `7,635.00` |
| `Live` | `Long` | `0.2915` | 835,050.00 USD | 0.00 USD | 954.37 USD | `-13.26%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 834,100.00 USD | 0.00 USD | 213.08 USD | `-12.66%` | `726.00` |
| `Live` | `Long` | `0.2945` | 833,890.00 USD | 0.00 USD | 124.87 USD | `-12.36%` | `424.00` |
| `Live` | `Long` | `0.2955` | 833,760.00 USD | 0.00 USD | 147.75 USD | `-12.07%` | `500.00` |
| `Live` | `Long` | `0.2965` | 833,610.00 USD | 0.00 USD | 157.14 USD | `-11.77%` | `530.00` |
| `Live` | `Long` | `0.2975` | 833,460.00 USD | 0.00 USD | 1,010.00 USD | `-11.47%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 832,450.00 USD | 0.00 USD | 127.46 USD | `-11.17%` | `427.00` |
| `Live` | `Long` | `0.2995` | 832,320.00 USD | 0.00 USD | 831.71 USD | `-10.88%` | `2,777.00` |
| `Live` | `Long` | `0.3005` | 831,490.00 USD | 0.00 USD | 10,290.00 USD | `-10.58%` | `34,248.00` |
| `Live` | `Long` | `0.3015` | 821,200.00 USD | 0.00 USD | 328.03 USD | `-10.28%` | `1,088.00` |
| `Live` | `Long` | `0.3025` | 820,870.00 USD | 0.00 USD | 2,620.00 USD | `-9.98%` | `8,655.00` |
| `Live` | `Long` | `0.3045` | 818,250.00 USD | 0.00 USD | 405.59 USD | `-9.39%` | `1,332.00` |
| `Live` | `Long` | `0.3055` | 817,840.00 USD | 0.00 USD | 14,670.00 USD | `-9.09%` | `48,026.00` |
| `Live` | `Long` | `0.3075` | 803,170.00 USD | 0.00 USD | 6,650.00 USD | `-8.50%` | `21,612.00` |
| `Live` | `Long` | `0.3085` | 796,530.00 USD | 0.00 USD | 2,010.00 USD | `-8.20%` | `6,517.00` |
| `Live` | `Long` | `0.3095` | 794,520.00 USD | 0.00 USD | 192.51 USD | `-7.90%` | `622.00` |
| `Live` | `Long` | `0.3105` | 794,320.00 USD | 0.00 USD | 137.86 USD | `-7.60%` | `444.00` |
| `Live` | `Long` | `0.3115` | 794,190.00 USD | 0.00 USD | 13,600.00 USD | `-7.31%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 780,580.00 USD | 0.00 USD | 17,630.00 USD | `-7.01%` | `56,426.00` |
| `Live` | `Long` | `0.3135` | 762,950.00 USD | 0.00 USD | 540.16 USD | `-6.71%` | `1,723.00` |
| `Live` | `Long` | `0.3145` | 762,410.00 USD | 0.00 USD | 141.84 USD | `-6.41%` | `451.00` |
| `Live` | `Long` | `0.3155` | 762,270.00 USD | 0.00 USD | 1,490.00 USD | `-6.12%` | `4,723.00` |
| `Live` | `Long` | `0.3165` | 760,780.00 USD | 0.00 USD | 935.89 USD | `-5.82%` | `2,957.00` |
| `Live` | `Long` | `0.3225` | 759,840.00 USD | 0.00 USD | 128.03 USD | `-4.03%` | `397.00` |
| `Live` | `Long` | `0.3275` | 759,710.00 USD | 0.00 USD | 6,260.00 USD | `-2.54%` | `19,105.00` |
| `Live` | `Long` | `0.3285` | 753,460.00 USD | 0.00 USD | 745,260.00 USD | `-2.25%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 8,190.00 USD | 0.00 USD | 2,030.00 USD | `-1.95%` | `6,149.00` |
| `Live` | `Long` | `0.3315` | 6,170.00 USD | 0.00 USD | 5,420.00 USD | `-1.35%` | `16,340.00` |
| `Live` | `Long` | `0.3325` | 749.48 USD | 0.00 USD | 634.08 USD | `-1.06%` | `1,907.00` |
| `Live` | `Long` | `0.3345` | 115.40 USD | 0.00 USD | 115.40 USD | `-0.46%` | `345.00` |
| `Live` | `Short` | `0.3625` | 1,650.00 USD | 1,650.00 USD | 0.00 USD | `+7.87%` | `4,554.00` |
| `Live` | `Short` | `0.3635` | 33,210.00 USD | 31,560.00 USD | 0.00 USD | `+8.17%` | `86,811.00` |
| `Live` | `Short` | `0.3645` | 45,600.00 USD | 12,390.00 USD | 0.00 USD | `+8.47%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 46,760.00 USD | 1,160.00 USD | 0.00 USD | `+9.06%` | `3,165.00` |
| `Live` | `Short` | `0.3675` | 48,720.00 USD | 1,960.00 USD | 0.00 USD | `+9.36%` | `5,333.00` |
| `Live` | `Short` | `0.3685` | 48,940.00 USD | 220.73 USD | 0.00 USD | `+9.66%` | `599.00` |
| `Live` | `Short` | `0.3705` | 49,220.00 USD | 278.99 USD | 0.00 USD | `+10.25%` | `753.00` |
| `Live` | `Short` | `0.3715` | 51,260.00 USD | 2,040.00 USD | 0.00 USD | `+10.55%` | `5,485.00` |
| `Live` | `Short` | `0.3725` | 51,620.00 USD | 366.17 USD | 0.00 USD | `+10.85%` | `983.00` |
| `Live` | `Short` | `0.3735` | 96,210.00 USD | 44,580.00 USD | 0.00 USD | `+11.14%` | `119,364.00` |
| `Live` | `Short` | `0.3745` | 96,350.00 USD | 140.06 USD | 0.00 USD | `+11.44%` | `374.00` |
| `Live` | `Short` | `0.3755` | 102,460.00 USD | 6,120.00 USD | 0.00 USD | `+11.74%` | `16,287.00` |
| `Live` | `Short` | `0.3775` | 134,760.00 USD | 32,300.00 USD | 0.00 USD | `+12.33%` | `85,568.00` |
| `Live` | `Short` | `0.3785` | 691,300.00 USD | 556,530.00 USD | 0.00 USD | `+12.63%` | `1,470,359.00` |
| `Live` | `Short` | `0.3835` | 691,410.00 USD | 115.05 USD | 0.00 USD | `+14.12%` | `300.00` |
| `Live` | `Short` | `0.3865` | 691,680.00 USD | 265.53 USD | 0.00 USD | `+15.01%` | `687.00` |
| `Live` | `Short` | `0.3895` | 700,980.00 USD | 9,310.00 USD | 0.00 USD | `+15.91%` | `23,896.00` |
| `Live` | `Short` | `0.3905` | 702,420.00 USD | 1,440.00 USD | 0.00 USD | `+16.20%` | `3,688.00` |
| `Live` | `Short` | `0.3935` | 703,910.00 USD | 1,480.00 USD | 0.00 USD | `+17.10%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 870,630.00 USD | 166,720.00 USD | 0.00 USD | `+17.39%` | `422,615.00` |
| `Live` | `Short` | `0.3965` | 940,130.00 USD | 69,500.00 USD | 0.00 USD | `+17.99%` | `175,280.00` |
| `Live` | `Short` | `0.4085` | 942,340.00 USD | 2,210.00 USD | 0.00 USD | `+21.56%` | `5,417.00` |
| `Live` | `Short` | `0.4095` | 942,580.00 USD | 239.56 USD | 0.00 USD | `+21.86%` | `585.00` |
| `Live` | `Short` | `0.4165` | 943,310.00 USD | 730.12 USD | 0.00 USD | `+23.94%` | `1,753.00` |
| `Live` | `Short` | `0.4195` | 944,310.00 USD | 1,000.00 USD | 0.00 USD | `+24.83%` | `2,387.00` |
| `Live` | `Short` | `0.4255` | 945,780.00 USD | 1,470.00 USD | 0.00 USD | `+26.62%` | `3,464.00` |
| `Live` | `Short` | `0.4295` | 956,000.00 USD | 10,210.00 USD | 0.00 USD | `+27.81%` | `23,779.00` |
| `Live` | `Short` | `0.4365` | 956,200.00 USD | 206.03 USD | 0.00 USD | `+29.89%` | `472.00` |
| `Live` | `Short` | `0.4385` | 1,030,000.00 USD | 71,380.00 USD | 0.00 USD | `+30.49%` | `162,775.00` |
| `Live` | `Short` | `0.4425` | 1,030,000.00 USD | 378.34 USD | 0.00 USD | `+31.68%` | `855.00` |
| `Live` | `Short` | `0.4455` | 1,050,000.00 USD | 22,270.00 USD | 0.00 USD | `+32.57%` | `50,000.00` |
| `Live` | `Short` | `0.4465` | 1,050,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.87%` | `2,284.00` |
| `Live` | `Short` | `0.4475` | 1,120,000.00 USD | 65,610.00 USD | 0.00 USD | `+33.16%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 1,120,000.00 USD | 5,400.00 USD | 0.00 USD | `+34.36%` | `11,950.00` |
| `Live` | `Short` | `0.4525` | 1,120,000.00 USD | 1,140.00 USD | 0.00 USD | `+34.65%` | `2,519.00` |
| `Live` | `Short` | `0.4545` | 1,120,000.00 USD | 1,550.00 USD | 0.00 USD | `+35.25%` | `3,416.00` |
| `Live` | `Short` | `0.4715` | 1,410,000.00 USD | 282,990.00 USD | 0.00 USD | `+40.31%` | `600,198.00` |
| `Live` | `Short` | `0.4895` | 1,410,000.00 USD | 839.49 USD | 0.00 USD | `+45.66%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 1,410,000.00 USD | 5,120.00 USD | 0.00 USD | `+45.96%` | `10,430.00` |
| `Live` | `Short` | `0.4935` | 1,410,000.00 USD | 285.24 USD | 0.00 USD | `+46.85%` | `578.00` |
| `Live` | `Short` | `0.4945` | 1,430,000.00 USD | 20,750.00 USD | 0.00 USD | `+47.15%` | `41,969.00` |
| `Live` | `Short` | `0.4995` | 1,440,000.00 USD | 2,730.00 USD | 0.00 USD | `+48.64%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 1,460,000.00 USD | 23,600.00 USD | 0.00 USD | `+49.23%` | `47,061.00` |
| `Live` | `Short` | `0.5195` | 1,460,000.00 USD | 1,100.00 USD | 0.00 USD | `+54.59%` | `2,120.00` |
| `Live` | `Short` | `0.5335` | 1,460,000.00 USD | 668.48 USD | 0.00 USD | `+58.76%` | `1,253.00` |
| `Live` | `Short` | `0.5445` | 1,470,000.00 USD | 4,360.00 USD | 0.00 USD | `+62.03%` | `8,009.00` |
| `Live` | `Short` | `0.5545` | 1,510,000.00 USD | 41,030.00 USD | 0.00 USD | `+65.01%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 1,510,000.00 USD | 740.92 USD | 0.00 USD | `+65.90%` | `1,329.00` |
| `Live` | `Short` | `0.5615` | 1,510,000.00 USD | 140.38 USD | 0.00 USD | `+67.09%` | `250.00` |
| `Live` | `Short` | `0.5635` | 1,510,000.00 USD | 2,340.00 USD | 0.00 USD | `+67.68%` | `4,154.00` |
| `Live` | `Short` | `0.5645` | 2,240,000.00 USD | 732,300.00 USD | 0.00 USD | `+67.98%` | `1,297,248.00` |
| `Live` | `Short` | `0.5665` | 2,300,000.00 USD | 54,300.00 USD | 0.00 USD | `+68.58%` | `95,846.00` |
| `Live` | `Short` | `0.6105` | 2,310,000.00 USD | 8,060.00 USD | 0.00 USD | `+81.67%` | `13,210.00` |
| `Live` | `Short` | `0.6155` | 2,330,000.00 USD | 28,550.00 USD | 0.00 USD | `+83.16%` | `46,380.00` |
| `Live` | `Short` | `0.6185` | 2,340,000.00 USD | 374.19 USD | 0.00 USD | `+84.05%` | `605.00` |
| `Live` | `Short` | `0.6225` | 2,370,000.00 USD | 32,720.00 USD | 0.00 USD | `+85.24%` | `52,566.00` |
| `Live` | `Short` | `0.6275` | 2,370,000.00 USD | 1,130.00 USD | 0.00 USD | `+86.73%` | `1,808.00` |
| `Live` | `Short` | `0.6345` | 2,380,000.00 USD | 6,820.00 USD | 0.00 USD | `+88.81%` | `10,756.00` |
| `Live` | `Short` | `0.6515` | 2,380,000.00 USD | 951.19 USD | 0.00 USD | `+93.87%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 2,380,000.00 USD | 705.13 USD | 0.00 USD | `+94.47%` | `1,079.00` |
| `Live` | `Short` | `0.6575` | 2,470,000.00 USD | 91,960.00 USD | 0.00 USD | `+95.66%` | `139,864.00` |
| `Live` | `Short` | `0.6605` | 2,560,000.00 USD | 87,360.00 USD | 0.00 USD | `+96.55%` | `132,260.00` |
| `Live` | `Short` | `0.6615` | 2,560,000.00 USD | 2,060.00 USD | 0.00 USD | `+96.85%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 2,560,000.00 USD | 3,740.00 USD | 0.00 USD | `+97.44%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0945` | 872,760.00 USD | 0.00 USD | 198.45 USD | `-71.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 872,560.00 USD | 0.00 USD | 330.26 USD | `-57.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 872,230.00 USD | 0.00 USD | 1,750.00 USD | `-39.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 870,480.00 USD | 0.00 USD | 2,220.00 USD | `-37.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 868,260.00 USD | 0.00 USD | 121.70 USD | `-31.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 868,140.00 USD | 0.00 USD | 705.61 USD | `-30.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 867,430.00 USD | 0.00 USD | 159.20 USD | `-29.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 867,270.00 USD | 0.00 USD | 1,200.00 USD | `-28.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 866,070.00 USD | 0.00 USD | 127.51 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 865,940.00 USD | 0.00 USD | 1,850.00 USD | `-25.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 864,090.00 USD | 0.00 USD | 41,500.00 USD | `-25.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 822,590.00 USD | 0.00 USD | 1,920.00 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 820,670.00 USD | 0.00 USD | 664.01 USD | `-22.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 820,000.00 USD | 0.00 USD | 954.98 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 819,050.00 USD | 0.00 USD | 103.56 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 818,950.00 USD | 0.00 USD | 695.50 USD | `-20.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 818,250.00 USD | 0.00 USD | 1,630.00 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 816,620.00 USD | 0.00 USD | 1,470.00 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 815,150.00 USD | 0.00 USD | 101.94 USD | `-18.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 815,050.00 USD | 0.00 USD | 3,260.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 811,790.00 USD | 0.00 USD | 2,550.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 809,240.00 USD | 0.00 USD | 229.92 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 809,010.00 USD | 0.00 USD | 8,010.00 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 801,000.00 USD | 0.00 USD | 11,610.00 USD | `-12.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 789,390.00 USD | 0.00 USD | 111.19 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 789,280.00 USD | 0.00 USD | 433.42 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 788,840.00 USD | 0.00 USD | 2,710.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 786,140.00 USD | 0.00 USD | 335.56 USD | `-9.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 785,800.00 USD | 0.00 USD | 1,040.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 784,760.00 USD | 0.00 USD | 193.11 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 784,570.00 USD | 0.00 USD | 15,150.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 769,410.00 USD | 0.00 USD | 147.32 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 769,270.00 USD | 0.00 USD | 12,200.00 USD | `-7.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 757,060.00 USD | 0.00 USD | 6,530.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 750,540.00 USD | 0.00 USD | 524,570.00 USD | `-7.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 225,960.00 USD | 0.00 USD | 1,270.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 224,700.00 USD | 0.00 USD | 53,690.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 171,010.00 USD | 0.00 USD | 2,480.00 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 168,530.00 USD | 0.00 USD | 6,100.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 162,440.00 USD | 0.00 USD | 850.90 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 161,590.00 USD | 0.00 USD | 1,160.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 160,420.00 USD | 0.00 USD | 6,220.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 154,200.00 USD | 0.00 USD | 10,000.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 144,200.00 USD | 0.00 USD | 43,570.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 100,640.00 USD | 0.00 USD | 131.90 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 100,500.00 USD | 0.00 USD | 4,710.00 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 95,790.00 USD | 0.00 USD | 3,220.00 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 92,570.00 USD | 0.00 USD | 64,780.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 27,800.00 USD | 0.00 USD | 6,130.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 21,660.00 USD | 0.00 USD | 6,770.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 14,890.00 USD | 0.00 USD | 3,800.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 11,090.00 USD | 0.00 USD | 1,960.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 9,130.00 USD | 0.00 USD | 949.53 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 8,180.00 USD | 0.00 USD | 100.11 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 8,080.00 USD | 0.00 USD | 135.99 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 7,950.00 USD | 0.00 USD | 1,010.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 6,940.00 USD | 0.00 USD | 5,930.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 1,010.00 USD | 0.00 USD | 1,010.00 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 56,310.00 USD | 56,310.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 88,790.00 USD | 32,490.00 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 88,950.00 USD | 157.74 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 92,330.00 USD | 3,380.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 93,730.00 USD | 1,400.00 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 94,220.00 USD | 486.30 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 94,580.00 USD | 359.28 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 95,410.00 USD | 828.18 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 97,350.00 USD | 1,950.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 101,330.00 USD | 3,980.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 101,890.00 USD | 555.44 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 102,020.00 USD | 134.83 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 102,460.00 USD | 439.11 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 104,030.00 USD | 1,570.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 106,460.00 USD | 2,430.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 107,380.00 USD | 919.52 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 116,080.00 USD | 8,690.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 116,390.00 USD | 312.14 USD | 0.00 USD | `+5.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 116,550.00 USD | 157.04 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 116,680.00 USD | 132.96 USD | 0.00 USD | `+5.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 156,110.00 USD | 39,430.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 196,500.00 USD | 40,390.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 199,810.00 USD | 3,310.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 200,840.00 USD | 1,030.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 203,780.00 USD | 2,940.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 204,000.00 USD | 224.49 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 204,110.00 USD | 103.23 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 206,900.00 USD | 2,800.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 248,510.00 USD | 41,610.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 259,690.00 USD | 11,170.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 259,860.00 USD | 172.72 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 260,080.00 USD | 218.89 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 274,410.00 USD | 14,330.00 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 277,290.00 USD | 2,880.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 277,470.00 USD | 174.60 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 277,570.00 USD | 107.28 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 278,010.00 USD | 439.61 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 278,450.00 USD | 437.79 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 280,740.00 USD | 2,290.00 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 280,920.00 USD | 182.60 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 287,380.00 USD | 6,450.00 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 287,650.00 USD | 275.17 USD | 0.00 USD | `+12.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 288,220.00 USD | 569.25 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 294,200.00 USD | 5,980.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 294,450.00 USD | 257.89 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 294,720.00 USD | 262.78 USD | 0.00 USD | `+13.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 294,940.00 USD | 224.73 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 295,560.00 USD | 621.04 USD | 0.00 USD | `+14.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 296,260.00 USD | 702.27 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 297,380.00 USD | 1,110.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 297,560.00 USD | 181.04 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 297,910.00 USD | 352.11 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 298,070.00 USD | 155.03 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 298,340.00 USD | 276.40 USD | 0.00 USD | `+16.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 298,470.00 USD | 126.24 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 300,870.00 USD | 2,400.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 301,880.00 USD | 1,010.00 USD | 0.00 USD | `+18.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 303,240.00 USD | 1,350.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 374,730.00 USD | 71,490.00 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 375,590.00 USD | 864.28 USD | 0.00 USD | `+19.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 379,510.00 USD | 3,920.00 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 458,840.00 USD | 79,330.00 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 460,040.00 USD | 1,200.00 USD | 0.00 USD | `+20.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 461,240.00 USD | 1,200.00 USD | 0.00 USD | `+20.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 461,380.00 USD | 138.07 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 462,650.00 USD | 1,270.00 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 462,980.00 USD | 331.63 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 463,290.00 USD | 313.54 USD | 0.00 USD | `+24.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 463,480.00 USD | 186.70 USD | 0.00 USD | `+25.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 463,810.00 USD | 325.75 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 463,990.00 USD | 183.82 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 464,290.00 USD | 299.19 USD | 0.00 USD | `+29.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 502,870.00 USD | 38,580.00 USD | 0.00 USD | `+31.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 503,040.00 USD | 170.69 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 503,170.00 USD | 135.59 USD | 0.00 USD | `+33.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 504,370.00 USD | 1,200.00 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 509,710.00 USD | 5,340.00 USD | 0.00 USD | `+35.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 511,190.00 USD | 1,470.00 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 591,960.00 USD | 80,770.00 USD | 0.00 USD | `+45.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 592,120.00 USD | 169.22 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 592,280.00 USD | 153.79 USD | 0.00 USD | `+47.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 593,000.00 USD | 724.89 USD | 0.00 USD | `+47.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 604,160.00 USD | 11,150.00 USD | 0.00 USD | `+48.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 606,080.00 USD | 1,930.00 USD | 0.00 USD | `+50.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 606,220.00 USD | 135.02 USD | 0.00 USD | `+57.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 606,460.00 USD | 240.85 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 607,560.00 USD | 1,100.00 USD | 0.00 USD | `+88.22%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2923` | 25,780,000.00 USD | 0.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 74,770.00 USD |
| `7D` | `0.2947` | 25,710,000.00 USD | 0.00 USD | 25,710,000.00 USD | 45,870.00 USD | 8,790.00 USD | 2,910.00 USD |
| `7D` | `0.2953` | 25,650,000.00 USD | 0.00 USD | 25,650,000.00 USD | 65,070.00 USD | 8,220.00 USD | 13,500.00 USD |
| `7D` | `0.2959` | 25,560,000.00 USD | 0.00 USD | 25,560,000.00 USD | 108,940.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 25,420,000.00 USD | 0.00 USD | 25,420,000.00 USD | 122,540.00 USD | 38,150.00 USD | 60,970.00 USD |
| `7D` | `0.2971` | 25,200,000.00 USD | 0.00 USD | 25,200,000.00 USD | 137,530.00 USD | 37,780.00 USD | 57,710.00 USD |
| `7D` | `0.2977` | 24,970,000.00 USD | 0.00 USD | 24,970,000.00 USD | 69,090.00 USD | 18,540.00 USD | 17,670.00 USD |
| `7D` | `0.2983` | 24,860,000.00 USD | 0.00 USD | 24,860,000.00 USD | 167,680.00 USD | 15,470.00 USD | 39,660.00 USD |
| `7D` | `0.2989` | 24,640,000.00 USD | 0.00 USD | 24,640,000.00 USD | 110,250.00 USD | 18,720.00 USD | 23,920.00 USD |
| `7D` | `0.2995` | 24,480,000.00 USD | 0.00 USD | 24,480,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD |
| `7D` | `0.3007` | 24,470,000.00 USD | 0.00 USD | 24,470,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3008` | 11,680,000.00 USD | 0.00 USD | 11,680,000.00 USD | 13,540.00 USD | 0.00 USD | 16,090.00 USD |
| `1D` | `0.3018` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3028` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 454.78 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3033` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 332.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 0.00 USD | 17,840.00 USD | 38,730.00 USD |
| `1D` | `0.3048` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3049` | 24,440,000.00 USD | 0.00 USD | 24,440,000.00 USD | 18,020.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3053` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 18,730.00 USD | 13,030.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 24,390,000.00 USD | 0.00 USD | 24,390,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3061` | 24,390,000.00 USD | 0.00 USD | 24,390,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3063` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 885.25 USD | 16,530.00 USD | 56,460.00 USD |
| `7D` | `0.3067` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 6,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3068` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 31,110.00 USD | 15,440.00 USD | 48,460.00 USD |
| `1D` | `0.3073` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3073` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 8,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3078` | 11,240,000.00 USD | 0.00 USD | 11,240,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 24,300,000.00 USD | 0.00 USD | 24,300,000.00 USD | 39,410.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3083` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 18,640.00 USD | 0.00 USD | 28,050.00 USD |
| `7D` | `0.3085` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3088` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 707.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 24,200,000.00 USD | 0.00 USD | 24,200,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3093` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 24,190,000.00 USD | 0.00 USD | 24,190,000.00 USD | 24,310.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3098` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3103` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 24,170,000.00 USD | 0.00 USD | 24,170,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `7D` | `0.3109` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3113` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD |
| `7D` | `0.3115` | 24,030,000.00 USD | 0.00 USD | 24,030,000.00 USD | 554.30 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3118` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 12,410.00 USD | 12,220.00 USD | 17,620.00 USD |
| `7D` | `0.3121` | 23,990,000.00 USD | 0.00 USD | 23,990,000.00 USD | 162,610.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3123` | 11,010,000.00 USD | 0.00 USD | 11,010,000.00 USD | 24,290.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3127` | 23,810,000.00 USD | 0.00 USD | 23,810,000.00 USD | 11,540.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3128` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 424.13 USD | 39,470.00 USD | 29,100.00 USD |
| `1D` | `0.3133` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 0.00 USD | 26,460.00 USD | 9,590.00 USD |
| `7D` | `0.3133` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 7,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3138` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 952.52 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,280.00 USD | 3,580.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 23,680,000.00 USD | 0.00 USD | 23,680,000.00 USD | 247,520.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3148` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 644.30 USD | 2,330.00 USD | 0.00 USD |
| `7D` | `0.3151` | 23,360,000.00 USD | 0.00 USD | 23,360,000.00 USD | 181,440.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3153` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 18,750.00 USD | 25,600.00 USD | 0.00 USD |
| `7D` | `0.3157` | 23,110,000.00 USD | 0.00 USD | 23,110,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3158` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 5,900.00 USD | 1,830.00 USD | 16,240.00 USD |
| `1D` | `0.3163` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 248.58 USD | 33,960.00 USD | 0.00 USD |
| `7D` | `0.3163` | 22,560,000.00 USD | 0.00 USD | 22,560,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3168` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 43,210.00 USD | 10,820.00 USD | 29,770.00 USD |
| `7D` | `0.3169` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 531,940.00 USD | 109,980.00 USD | 150,970.00 USD |
| `1D` | `0.3173` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 23,670.00 USD | 33,870.00 USD | 27,630.00 USD |
| `7D` | `0.3175` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 189,350.00 USD | 59,040.00 USD | 71,670.00 USD |
| `1D` | `0.3178` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 64,070.00 USD | 13,580.00 USD | 44,000.00 USD |
| `7D` | `0.3181` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 738,770.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3183` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 376,020.00 USD | 71,770.00 USD | 97,130.00 USD |
| `7D` | `0.3187` | 19,600,000.00 USD | 0.00 USD | 19,600,000.00 USD | 346,920.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3188` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 43,050.00 USD | 36,160.00 USD | 49,850.00 USD |
| `1D` | `0.3193` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 74,100.00 USD | 3,120.00 USD | 20,860.00 USD |
| `7D` | `0.3193` | 19,130,000.00 USD | 0.00 USD | 19,130,000.00 USD | 118,210.00 USD | 25,780.00 USD | 51,630.00 USD |
| `1D` | `0.3198` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 56,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3203` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 208,350.00 USD | 26,000.00 USD | 34,330.00 USD |
| `7D` | `0.3205` | 18,830,000.00 USD | 0.00 USD | 18,830,000.00 USD | 37,120.00 USD | 7,390.00 USD | 55,250.00 USD |
| `1D` | `0.3208` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 132,330.00 USD | 13,040.00 USD | 63,020.00 USD |
| `7D` | `0.3211` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 561,850.00 USD | 102,530.00 USD | 201,530.00 USD |
| `1D` | `0.3213` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 1,300.00 USD | 20,180.00 USD | 90,380.00 USD |
| `7D` | `0.3217` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 284,170.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3218` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 5,550.00 USD | 21,490.00 USD | 87,330.00 USD |
| `1D` | `0.3223` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 118,980.00 USD | 13,780.00 USD | 176,480.00 USD |
| `7D` | `0.3223` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 644,620.00 USD | 175,040.00 USD | 103,370.00 USD |
| `1D` | `0.3228` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 21,530.00 USD | 46,020.00 USD | 168,550.00 USD |
| `7D` | `0.3229` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 730,720.00 USD | 274,530.00 USD | 385,680.00 USD |
| `1D` | `0.3233` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 56,470.00 USD | 6,250.00 USD | 34,420.00 USD |
| `7D` | `0.3235` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 974,940.00 USD | 219,960.00 USD | 389,140.00 USD |
| `1D` | `0.3238` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 6,420.00 USD | 81,890.00 USD | 150,090.00 USD |
| `7D` | `0.3241` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 480,120.00 USD | 161,000.00 USD | 143,340.00 USD |
| `1D` | `0.3243` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 125,350.00 USD | 41,210.00 USD | 191,760.00 USD |
| `7D` | `0.3247` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 847,940.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3248` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 714,450.00 USD | 114,830.00 USD | 235,780.00 USD |
| `1D` | `0.3253` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 424,900.00 USD | 91,650.00 USD | 334,570.00 USD |
| `7D` | `0.3253` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 1,090,000.00 USD | 108,500.00 USD | 134,260.00 USD |
| `1D` | `0.3258` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 101,780.00 USD | 36,240.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 182,240.00 USD | 92,250.00 USD | 112,320.00 USD |
| `1D` | `0.3263` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 0.00 USD | 9,800.00 USD | 0.00 USD |
| `7D` | `0.3265` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 78,960.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3268` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 124,870.00 USD | 87,680.00 USD | 279,870.00 USD |
| `7D` | `0.3271` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 68,910.00 USD | 14,780.00 USD | 110,490.00 USD |
| `1D` | `0.3273` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 38,550.00 USD | 50,640.00 USD | 201,590.00 USD |
| `1D` | `0.3278` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 213,460.00 USD | 31,950.00 USD | 115,660.00 USD |
| `1D` | `0.3283` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 0.00 USD | 36,260.00 USD | 0.00 USD |
| `7D` | `0.3283` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3288` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 84,680.00 USD | 0.00 USD | 185,700.00 USD |
| `1D` | `0.3293` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 1,210.00 USD | 33,750.00 USD | 0.00 USD |
| `7D` | `0.3301` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 59,490.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3303` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 37,670.00 USD | 0.00 USD | 11,710.00 USD |
| `7D` | `0.3307` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 167,950.00 USD | 10,690.00 USD | 158,260.00 USD |
| `1D` | `0.3308` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 214,030.00 USD | 39,540.00 USD | 203,280.00 USD |
| `1D` | `0.3313` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 142,970.00 USD | 117,000.00 USD | 271,320.00 USD |
| `7D` | `0.3313` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 138,700.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3318` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 159,340.00 USD | 54,860.00 USD | 295,390.00 USD |
| `7D` | `0.3319` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 119,480.00 USD |
| `1D` | `0.3323` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 106,340.00 USD | 87,940.00 USD | 44,050.00 USD |
| `7D` | `0.3325` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 94,080.00 USD | 74,110.00 USD | 93,720.00 USD |
| `1D` | `0.3328` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 62,020.00 USD | 33,750.00 USD | 286,350.00 USD |
| `7D` | `0.3331` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 549,640.00 USD | 87,530.00 USD | 26,320.00 USD |
| `1D` | `0.3333` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 38,930.00 USD | 58,300.00 USD | 340,980.00 USD |
| `7D` | `0.3337` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 73,540.00 USD | 136,160.00 USD | 330,300.00 USD |
| `1D` | `0.3338` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 223,020.00 USD | 224,220.00 USD | 251,220.00 USD |
| `1D` | `0.3343` | 547,620.00 USD | 0.00 USD | 547,620.00 USD | 932.61 USD | 134,220.00 USD | 87,800.00 USD |
| `7D` | `0.3343` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 0.00 USD | 74,100.00 USD | 0.00 USD |
| `1D` | `0.3348` | 324,670.00 USD | 0.00 USD | 324,670.00 USD | 277,800.00 USD | 46,870.00 USD | 0.00 USD |
| `7D` | `0.3349` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 178,050.00 USD | 51,330.00 USD | 0.00 USD |
| `1D` | `0.3352` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3353` | 181,600.00 USD | 181,600.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | 158,820.00 USD |
| `7D` | `0.3355` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 1,610.00 USD | 21,530.00 USD | 251,000.00 USD |
| `1D` | `0.3358` | 615,830.00 USD | 615,830.00 USD | 0.00 USD | 267,520.00 USD | 22,430.00 USD | 144,280.00 USD |
| `7D` | `0.3361` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3363` | 730,170.00 USD | 730,170.00 USD | 0.00 USD | 46,870.00 USD | 67,470.00 USD | 0.00 USD |
| `7D` | `0.3367` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 177,120.00 USD | 67,510.00 USD | 0.00 USD |
| `1D` | `0.3368` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 282,270.00 USD | 29,430.00 USD | 40,590.00 USD |
| `1D` | `0.3373` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 859.70 USD | 107,280.00 USD | 23,420.00 USD |
| `7D` | `0.3373` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 478,820.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3378` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 619,770.00 USD | 31,130.00 USD | 17,230.00 USD |
| `7D` | `0.3379` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 308,170.00 USD | 21,390.00 USD | 336,650.00 USD |
| `1D` | `0.3383` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 232,810.00 USD | 114,980.00 USD | 49,800.00 USD |
| `7D` | `0.3385` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 282,740.00 USD | 101,310.00 USD | 73,150.00 USD |
| `1D` | `0.3388` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 32,800.00 USD | 44,920.00 USD | 59,530.00 USD |
| `7D` | `0.3391` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3393` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 65,650.00 USD | 45,920.00 USD | 168,910.00 USD |
| `7D` | `0.3397` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 257,550.00 USD | 250,860.00 USD | 187,450.00 USD |
| `1D` | `0.3398` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 144,030.00 USD | 0.00 USD | 337,050.00 USD |
| `1D` | `0.3403` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 187,960.00 USD | 0.00 USD | 198,780.00 USD |
| `7D` | `0.3403` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 946,670.00 USD | 406,630.00 USD | 72,350.00 USD |
| `1D` | `0.3408` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 71,510.00 USD | 0.00 USD | 37,920.00 USD |
| `7D` | `0.3409` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 177,540.00 USD | 446,990.00 USD |
| `1D` | `0.3413` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 181,530.00 USD | 0.00 USD | 62,690.00 USD |
| `7D` | `0.3415` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 57,370.00 USD | 0.00 USD |
| `1D` | `0.3418` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 585,390.00 USD | 0.00 USD | 27,870.00 USD |
| `1D` | `0.3423` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 11,630.00 USD | 0.00 USD |
| `7D` | `0.3427` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | 394,570.00 USD |
| `1D` | `0.3428` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 179,060.00 USD | 0.00 USD |
| `1D` | `0.3433` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 156,070.00 USD | 0.00 USD |
| `1D` | `0.3438` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 49,600.00 USD | 0.00 USD |
| `7D` | `0.3439` | 733,270.00 USD | 0.00 USD | 733,270.00 USD | 194,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3443` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 29,480.00 USD | 0.00 USD |
| `1D` | `0.3448` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 72,750.00 USD | 58,230.00 USD |
| `7D` | `0.3451` | 538,440.00 USD | 0.00 USD | 538,440.00 USD | 0.00 USD | 0.00 USD | 538,440.00 USD |
| `1D` | `0.3453` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 24,140.00 USD | 0.00 USD |
| `1D` | `0.3458` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 1,150.00 USD | 12,550.00 USD | 370,070.00 USD |
| `1D` | `0.3468` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | 0.00 USD |
| `7D` | `0.3472` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3473` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 37,260.00 USD | 0.00 USD |
| `1D` | `0.3478` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 37,720.00 USD | 111,350.00 USD |
| `1D` | `0.3483` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 0.00 USD | 9,680.00 USD | 0.00 USD |
| `1D` | `0.3488` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 8,020.00 USD | 0.00 USD |
| `1D` | `0.3493` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61,240.00 USD |
| `1D` | `0.3498` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 454,680.00 USD |
| `1D` | `0.3503` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 35,280.00 USD |
| `1D` | `0.3508` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 389,660.00 USD | 389,660.00 USD | 0.00 USD | 389,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3513` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 23,420.00 USD |
| `1D` | `0.3518` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 21,910.00 USD | 0.00 USD | 29,120.00 USD |
| `1D` | `0.3523` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 396.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 667,070.00 USD | 667,070.00 USD | 0.00 USD | 277,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3528` | 6,460,000.00 USD | 6,460,000.00 USD | 0.00 USD | 25,310.00 USD | 31,190.00 USD | 0.00 USD |
| `1D` | `0.3533` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 62,410.00 USD | 64,680.00 USD | 88,110.00 USD |
| `7D` | `0.3535` | 932,480.00 USD | 932,480.00 USD | 0.00 USD | 0.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3538` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 58,450.00 USD | 29,120.00 USD | 195,270.00 USD |
| `7D` | `0.3541` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 799,020.00 USD | 98,110.00 USD | 0.00 USD |
| `1D` | `0.3543` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 75,280.00 USD | 119,750.00 USD | 37,920.00 USD |
| `7D` | `0.3547` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3548` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 41,620.00 USD | 31,910.00 USD |
| `1D` | `0.3553` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 20,180.00 USD | 36,790.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 81,600.00 USD | 0.00 USD |
| `1D` | `0.3558` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 331.60 USD | 45,890.00 USD | 30,620.00 USD |
| `1D` | `0.3563` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 29,510.00 USD | 115,040.00 USD |
| `7D` | `0.3565` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3568` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3573` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 131,970.00 USD | 16,170.00 USD | 0.00 USD |
| `1D` | `0.3578` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 29,800.00 USD | 9,130.00 USD | 27,240.00 USD |
| `1D` | `0.3583` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 10,960.00 USD | 14,930.00 USD | 11,710.00 USD |
| `1D` | `0.3588` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 1,810.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `0.3589` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 1,760.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3593` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 64,080.00 USD | 0.00 USD | 133,180.00 USD |
| `7D` | `0.3595` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3598` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 90,790.00 USD | 22,780.00 USD | 64,450.00 USD |
| `7D` | `0.3601` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3603` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 31,030.00 USD | 41,780.00 USD | 136,650.00 USD |
| `7D` | `0.3607` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3608` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 77,290.00 USD | 39,250.00 USD | 157,390.00 USD |
| `1D` | `0.3613` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 37,640.00 USD | 63,400.00 USD | 236,630.00 USD |
| `7D` | `0.3613` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3618` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 225,600.00 USD | 56,810.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 192,210.00 USD | 0.00 USD |
| `1D` | `0.3623` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 226,400.00 USD | 79,900.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3628` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 1,060,000.00 USD | 74,470.00 USD | 55,750.00 USD |
| `7D` | `0.3631` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3633` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 223,360.00 USD | 72,670.00 USD | 223,640.00 USD |
| `7D` | `0.3637` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3638` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 183,690.00 USD | 65,110.00 USD | 76,240.00 USD |
| `1D` | `0.3643` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 167,490.00 USD | 211,440.00 USD | 35,280.00 USD |
| `7D` | `0.3643` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3648` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 259,960.00 USD | 71,710.00 USD | 124,520.00 USD |
| `7D` | `0.3649` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 177,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3653` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 286,780.00 USD | 19,500.00 USD | 236,620.00 USD |
| `7D` | `0.3655` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3658` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 289,040.00 USD | 152,150.00 USD | 156,950.00 USD |
| `7D` | `0.3661` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 685,520.00 USD | 0.00 USD | 160,210.00 USD |
| `1D` | `0.3663` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 448,400.00 USD | 99,430.00 USD | 16,800.00 USD |
| `7D` | `0.3667` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 419,350.00 USD | 0.00 USD | 73,150.00 USD |
| `1D` | `0.3668` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 257,230.00 USD | 48,270.00 USD | 253,250.00 USD |
| `1D` | `0.3673` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 45,880.00 USD | 106,060.00 USD | 203,360.00 USD |
| `7D` | `0.3673` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3678` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 497,170.00 USD | 45,130.00 USD | 191,130.00 USD |
| `7D` | `0.3679` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3683` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 269,310.00 USD | 81,750.00 USD | 161,850.00 USD |
| `7D` | `0.3685` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3688` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 715,890.00 USD | 144,580.00 USD | 68,010.00 USD |
| `7D` | `0.3691` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 147,650.00 USD | 252,870.00 USD | 0.00 USD |
| `1D` | `0.3693` | 17,680,000.00 USD | 17,680,000.00 USD | 0.00 USD | 79,910.00 USD | 49,680.00 USD | 23,760.00 USD |
| `7D` | `0.3697` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 153,310.00 USD | 0.00 USD |
| `1D` | `0.3698` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 313,650.00 USD | 81,600.00 USD | 0.00 USD |
| `1D` | `0.3703` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 589,850.00 USD | 196,170.00 USD | 84,860.00 USD |
| `1D` | `0.3708` | 19,570,000.00 USD | 19,570,000.00 USD | 0.00 USD | 110,690.00 USD | 21,340.00 USD | 497,740.00 USD |
| `7D` | `0.3709` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3713` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 481,410.00 USD | 90,010.00 USD | 804,260.00 USD |
| `7D` | `0.3715` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3718` | 21,490,000.00 USD | 21,490,000.00 USD | 0.00 USD | 43,980.00 USD | 226,350.00 USD | 274,680.00 USD |
| `7D` | `0.3721` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3723` | 21,970,000.00 USD | 21,970,000.00 USD | 0.00 USD | 327,290.00 USD | 58,560.00 USD | 89,100.00 USD |
| `7D` | `0.3727` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 23,900.00 USD |
| `1D` | `0.3728` | 23,050,000.00 USD | 23,050,000.00 USD | 0.00 USD | 178,580.00 USD | 106,520.00 USD | 802,100.00 USD |
| `1D` | `0.3733` | 23,880,000.00 USD | 23,880,000.00 USD | 0.00 USD | 110,390.00 USD | 58,740.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3738` | 24,420,000.00 USD | 24,420,000.00 USD | 0.00 USD | 154,860.00 USD | 158,380.00 USD | 229,860.00 USD |
| `7D` | `0.3739` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 246,590.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3743` | 24,770,000.00 USD | 24,770,000.00 USD | 0.00 USD | 32,620.00 USD | 43,590.00 USD | 276,190.00 USD |
| `7D` | `0.3745` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 248,660.00 USD | 107,330.00 USD | 37,210.00 USD |
| `1D` | `0.3748` | 25,550,000.00 USD | 25,550,000.00 USD | 0.00 USD | 30,710.00 USD | 20,770.00 USD | 724,070.00 USD |
| `1D` | `0.3753` | 25,940,000.00 USD | 25,940,000.00 USD | 0.00 USD | 363,100.00 USD | 0.00 USD | 31,010.00 USD |
| `7D` | `0.3757` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 302,240.00 USD |
| `1D` | `0.3758` | 26,450,000.00 USD | 26,450,000.00 USD | 0.00 USD | 186,760.00 USD | 72,840.00 USD | 247,210.00 USD |
| `1D` | `0.3763` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 140,730.00 USD | 24,840.00 USD | 859,720.00 USD |
| `7D` | `0.3763` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `1D` | `0.3768` | 27,540,000.00 USD | 27,540,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 15,810.00 USD |
| `7D` | `0.3769` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3773` | 27,620,000.00 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3778` | 27,850,000.00 USD | 27,850,000.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 230,890.00 USD |
| `7D` | `0.3781` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 25,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3783` | 27,870,000.00 USD | 27,870,000.00 USD | 0.00 USD | 16,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 39,410.00 USD | 3,620.00 USD | 0.00 USD |
| `1D` | `0.3788` | 28,380,000.00 USD | 28,380,000.00 USD | 0.00 USD | 220,670.00 USD | 0.00 USD | 289,160.00 USD |
| `1D` | `0.3793` | 28,580,000.00 USD | 28,580,000.00 USD | 0.00 USD | 54,830.00 USD | 96,440.00 USD | 46,470.00 USD |
| `7D` | `0.3793` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `1D` | `0.3798` | 28,580,000.00 USD | 28,580,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3803` | 28,910,000.00 USD | 28,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 334,230.00 USD |
| `7D` | `0.3805` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3808` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 855.55 USD | 17,210.00 USD | 17,620.00 USD |
| `7D` | `0.3811` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3813` | 28,990,000.00 USD | 28,990,000.00 USD | 0.00 USD | 23,970.00 USD | 2,560.00 USD | 17,440.00 USD |
| `7D` | `0.3817` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3818` | 29,020,000.00 USD | 29,020,000.00 USD | 0.00 USD | 11,830.00 USD | 3,560.00 USD | 16,390.00 USD |
| `1D` | `0.3823` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 932.61 USD | 35,920.00 USD | 246,850.00 USD |
| `7D` | `0.3823` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3828` | 29,340,000.00 USD | 29,340,000.00 USD | 0.00 USD | 1,720.00 USD | 26,460.00 USD | 0.00 USD |
| `1D` | `0.3833` | 29,570,000.00 USD | 29,570,000.00 USD | 0.00 USD | 0.00 USD | 10,610.00 USD | 219,870.00 USD |
| `1D` | `0.3838` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,540.00 USD |
| `7D` | `0.3841` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3843` | 29,580,000.00 USD | 29,580,000.00 USD | 0.00 USD | 0.00 USD | 5,900.00 USD | 0.00 USD |
| `1D` | `0.3850` | 29,600,000.00 USD | 29,600,000.00 USD | 0.00 USD | 0.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3859` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3919` | 14,140,000.00 USD | 14,140,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3925` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 14,330,000.00 USD | 14,330,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 21,960.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 14,390,000.00 USD | 14,390,000.00 USD | 0.00 USD | 24,610.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 109,660.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 107,420.00 USD | 10,160.00 USD | 112,040.00 USD |
| `7D` | `0.3961` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 143,850.00 USD | 54,030.00 USD | 8,320.00 USD |
| `7D` | `0.3967` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 12,370.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 16,650.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 57,630.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 1,030.00 USD |
| `7D` | `0.4003` | 15,280,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,050.00 USD |
| `7D` | `0.4009` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 6,890.00 USD | 1,480.00 USD | 0.00 USD |
| `7D` | `0.4015` | 15,440,000.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 149,550.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `406.86M` | Total OI Tokens: `1,210,210,064.0 TRX`
  * 1h OI Change: `-3.39%` | 4h OI Change: `-1.34%` | 24h OI Change: `+41.48%`
  * Exchange Breakdown: Binance=`106.71M` | Bybit=`82.27M` | OKX=`25.21M` | Hyperliquid=`17.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-129.61K` | Last 24h: `-591.57K` | Last 3d: `-625.17K` | Last 7d: `-857.29K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0618%` | **USDT OKX** | `-0.2989%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0268%` |
| **USDT MEXC** | `-0.0648%` | **USDT BingX** | `-0.2951%` |
| **USDT Gate** | `-0.0638%` | **USDT Bitget** | `-0.2033%` |
| **CoinM Binance** | `-0.2160%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `41.83%` | `58.17%` | `0.72` | 11,310,000.00 USD |
| `15M` | `Binance` | `44.05%` | `55.95%` | `0.79` | 4,260,000.00 USD |
| `15M` | `OKX` | `39%` | `61%` | `0.64` | 2,520,000.00 USD |
| `15M` | `Bybit` | `43.11%` | `56.89%` | `0.76` | 527,290.00 USD |
| `15M` | `KuCoin` | `69.95%` | `30.05%` | `2.33` | 41,730.00 USD |
| `15M` | `Gate` | `39.92%` | `60.08%` | `0.66` | 1,480,000.00 USD |
| `15M` | `Bitget` | `14.59%` | `85.41%` | `0.17` | 485,380.00 USD |
| `15M` | `BingX` | `47.08%` | `52.92%` | `0.89` | 147,570.00 USD |
| `15M` | `MEXC` | `51.29%` | `48.71%` | `1.05` | 1,280,000.00 USD |
| `15M` | `Bitunix` | `39.38%` | `60.62%` | `0.65` | 238,570.00 USD |
| `15M` | `Hyperliquid` | `4.46%` | `95.54%` | `0.05` | 37,140.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.6%` | `52.4%` | `0.91` | 50,850.00 USD |
| `15M` | `Crypto.com` | `24.57%` | `75.43%` | `0.33` | 6,180.00 USD |
| `15M` | `WhiteBIT` | `50.95%` | `49.05%` | `1.04` | 103,180.00 USD |
| `15M` | `HTX` | `33.84%` | `66.16%` | `0.51` | 43,950.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `43.12%` | `56.88%` | `0.76` | 89,110.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `87.89%` | `12.11%` | `7.26` | 281.17 USD |
| `15M` | `Whale Positions` | `44.05%` | `55.95%` | `0.79` | 4,260,000.00 USD |
| `15M` | `Global Accounts` | `41.83%` | `58.17%` | `0.72` | 11,310,000.00 USD |
| `1H` | `TRX` | `49.00%` | `51.00%` | `0.96` | 38,620,000.00 USD |
| `1H` | `Binance` | `47.67%` | `52.33%` | `0.91` | 14,090,000.00 USD |
| `1H` | `OKX` | `47.18%` | `52.82%` | `0.89` | 7,610,000.00 USD |
| `1H` | `Bybit` | `49.4%` | `50.6%` | `0.98` | 2,310,000.00 USD |
| `1H` | `KuCoin` | `44.18%` | `55.82%` | `0.79` | 216,290.00 USD |
| `1H` | `Gate` | `45.47%` | `54.53%` | `0.83` | 6,370,000.00 USD |
| `1H` | `Bitget` | `24.39%` | `75.61%` | `0.32` | 983,270.00 USD |
| `1H` | `BingX` | `44.09%` | `55.91%` | `0.79` | 545,460.00 USD |
| `1H` | `MEXC` | `66.71%` | `33.29%` | `2.00` | 3,960,000.00 USD |
| `1H` | `Bitunix` | `57.97%` | `42.03%` | `1.38` | 1,270,000.00 USD |
| `1H` | `Hyperliquid` | `29.05%` | `70.95%` | `0.41` | 92,250.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.22%` | `46.78%` | `1.14` | 221,930.00 USD |
| `1H` | `Crypto.com` | `47.02%` | `52.98%` | `0.89` | 29,620.00 USD |
| `1H` | `WhiteBIT` | `30.88%` | `69.12%` | `0.45` | 342,460.00 USD |
| `1H` | `HTX` | `68.94%` | `31.06%` | `2.22` | 429,100.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `44.78%` | `55.22%` | `0.81` | 160,680.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.82%` | `45.18%` | `1.21` | 3,470.00 USD |
| `1H` | `Whale Positions` | `47.67%` | `52.33%` | `0.91` | 14,090,000.00 USD |
| `1H` | `Global Accounts` | `49.00%` | `51.00%` | `0.96` | 38,620,000.00 USD |
| `4H` | `TRX` | `50.71%` | `49.29%` | `1.03` | 206,810,000.00 USD |
| `4H` | `Binance` | `50.92%` | `49.08%` | `1.04` | 82,790,000.00 USD |
| `4H` | `OKX` | `51.4%` | `48.6%` | `1.06` | 43,270,000.00 USD |
| `4H` | `Bybit` | `54.87%` | `45.13%` | `1.22` | 15,840,000.00 USD |
| `4H` | `KuCoin` | `41.27%` | `58.73%` | `0.70` | 1,320,000.00 USD |
| `4H` | `Gate` | `50.31%` | `49.69%` | `1.01` | 29,220,000.00 USD |
| `4H` | `Bitget` | `51.27%` | `48.73%` | `1.05` | 4,150,000.00 USD |
| `4H` | `BingX` | `39.25%` | `60.75%` | `0.65` | 2,980,000.00 USD |
| `4H` | `MEXC` | `53.57%` | `46.43%` | `1.15` | 9,280,000.00 USD |
| `4H` | `Bitunix` | `50.1%` | `49.9%` | `1.00` | 6,730,000.00 USD |
| `4H` | `Hyperliquid` | `50.07%` | `49.93%` | `1.00` | 2,820,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.04%` | `47.96%` | `1.09` | 1,010,000.00 USD |
| `4H` | `Crypto.com` | `49.89%` | `50.11%` | `1.00` | 232,320.00 USD |
| `4H` | `WhiteBIT` | `22.66%` | `77.34%` | `0.29` | 1,880,000.00 USD |
| `4H` | `HTX` | `44.86%` | `55.14%` | `0.81` | 3,840,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `37.71%` | `62.29%` | `0.61` | 92,220.00 USD |
| `4H` | `Aster` | `48.46%` | `51.54%` | `0.94` | 1,300,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.88%` | `54.12%` | `0.85` | 69,680.00 USD |
| `4H` | `Whale Positions` | `50.92%` | `49.08%` | `1.04` | 82,790,000.00 USD |
| `4H` | `Global Accounts` | `50.71%` | `49.29%` | `1.03` | 206,810,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3505` | `0.3505` | `0.3505` | `0.3539` | `0.3475` | 4,325,285.35 USD | 1,848,013.35 USD | 2,477,272.00 USD | -629,258.65 USD | `-14.55%` | `8B / 22S` |
| `0:00 UTC` | `0.3460` | `0.3471` | `0.3460` | `0.3497` | `0.3450` | 7,401,583.91 USD | 3,367,813.41 USD | 4,033,770.49 USD | -665,957.08 USD | `-9.00%` | `10B / 13S` |
| `5:00 UTC` | `0.3454` | `0.3452` | `0.3454` | `0.3460` | `0.3444` | 2,735,847.92 USD | 1,369,518.79 USD | 1,366,329.13 USD | 3,189.66 USD | `+0.12%` | `29B / 17S` |
| `0:00 UTC` | `0.3463` | `0.3466` | `0.3463` | `0.3482` | `0.3449` | 2,895,955.74 USD | 1,679,080.86 USD | 1,216,874.88 USD | 462,205.98 USD | `+15.96%` | `37B / 15S` |
| `5:00 UTC` | `0.3476` | `0.3475` | `0.3476` | `0.3487` | `0.3457` | 2,690,622.76 USD | 1,438,688.18 USD | 1,251,934.57 USD | 186,753.61 USD | `+6.94%` | `22B / 33S` |
| `0:00 UTC` | `0.3417` | `0.3427` | `0.3417` | `0.3460` | `0.3412` | 5,553,627.27 USD | 1,962,224.93 USD | 3,591,402.33 USD | -1,629,177.40 USD | `-29.34%` | `2B / 39S` |
| `5:00 UTC` | `0.3411` | `0.3414` | `0.3411` | `0.3425` | `0.3406` | 2,915,500.58 USD | 1,561,417.51 USD | 1,354,083.07 USD | 207,334.44 USD | `+7.11%` | `58B / 24S` |
| `0:00 UTC` | `0.3400` | `0.3401` | `0.3400` | `0.3411` | `0.3393` | 5,271,834.49 USD | 1,979,910.19 USD | 3,291,924.30 USD | -1,312,014.12 USD | `-24.89%` | `28B / 23S` |
| `5:00 UTC` | `0.3384` | `0.3390` | `0.3384` | `0.3406` | `0.3381` | 4,684,490.06 USD | 1,416,566.17 USD | 3,267,923.89 USD | -1,851,357.72 USD | `-39.52%` | `25B / 25S` |
| `0:00 UTC` | `0.3381` | `0.3361` | `0.3381` | `0.3382` | `0.3342` | 6,831,727.34 USD | 2,245,195.74 USD | 4,586,531.60 USD | -2,341,335.86 USD | `-34.27%` | `1B / 32S` |

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
| `5m` | 836,560.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,490,000.00 USD | -3,610,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 2,890,000.00 USD | -5,300,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 5,000,000.00 USD | -5,120,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 4,970,000.00 USD | -7,760,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 10,780,000.00 USD | -8,450,000.00 USD | **`ACCUMULATION`** |
| `6h` | 14,430,000.00 USD | -4,710,000.00 USD | **`ACCUMULATION`** |
| `8h` | 21,470,000.00 USD | 5,890,000.00 USD | **`ACCUMULATION`** |
| `12h` | 17,100,000.00 USD | 4,570,000.00 USD | **`ACCUMULATION`** |
| `24h` | 17,300,000.00 USD | 5,070,000.00 USD | **`ACCUMULATION`** |
| `1w` | 11,060,000.00 USD | 3,890,000.00 USD | **`ACCUMULATION`** |
| `30d` | -9,590,000.00 USD | 5,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+836.56K` | 15m=`+1.49M` | 1h=`+5.00M` | 24h=`+17.30M`
* Futures Capital Netflows: 5m=`-1.11M` | 15m=`-3.61M` | 1h=`-5.12M` | 24h=`+5.07M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3448` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3356` (Risk Distance: `0.0092` pts)
  * +2.5R Take Profit: `0.3678`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3571` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3663` (Risk Distance: `0.0092` pts)
  * +2.5R Take Profit: `0.3341`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3384`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
