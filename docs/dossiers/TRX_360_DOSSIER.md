# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 01:48:12 IST` (`2026-10-29 20:18:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3306` | **Live Ask Quote**: `0.3319` | **Mid Price**: `0.3312`
- **Spread Points**: `13.00` | **Spread BPS**: `39.25 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3303` | VWAP Z-Score: `+0.87` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000344` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3325` | Lower -3.00σ Band: `0.3280`
  * Upper +2.51σ Band: `0.3321` | Lower -2.51σ Band: `0.3284`
  * Upper +2.01σ Band: `0.3318` | Lower -2.01σ Band: `0.3287`
  * Upper +2.00σ Band: `0.3317` | Lower -2.00σ Band: `0.3288`
  * Upper +1.28σ Band: `0.3312` | Lower -1.28σ Band: `0.3293`
  * Upper +1.00σ Band: `0.3310` | Lower -1.00σ Band: `0.3295`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3307` | EMA-20=`0.3307` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3306` (Slope: `+0.0000`) | EMA-100=`0.3304`
  * Institutional Anchors: EMA-144=`0.3302` | EMA-200=`0.3300` (Slope: `+0.0255`) | EMA-233=`0.3299`
- **Range Boundaries**: 24H High=`0.3313` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `+0.01%`)
  * Point of Control (POC) = `0.3307` (Distance: `+0.17%`)
  * Value Area Low (VAL) = `0.3296` (Distance: `+0.50%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3314` | POC=`0.3309` | VAL=`0.3304`
  * Prior Day Extremes: PDH=`0.3319` | PDL=`0.3288` | PDC=`0.3289`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3312` | Weekly POC=`0.3307` | Weekly VAL=`0.3290`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3306` | Low=`0.3285`
  * London Session (08:00-16:00 UTC): High=`0.3311` | Low=`0.3303`
  * New York Session (13:00-21:00 UTC): High=`0.3313` | Low=`0.3301`
  * Initial Balance (First Hour): IB High=`0.3311` | IB Low=`0.3303`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3299` - `0.3326`
  * Optimal Trade Entry (OTE 0.705): `0.3319`
  * Structural Invalidation Anchor (0.786): `0.3339`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3315` | `0.3316` | `0.3311` | `0.3311` | `1,039,529` | 344,470.69 USD | -20,061.96 USD | `-5.82%` | 2,558,445.67 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3311` | `0.3314` | `0.3310` | `0.3313` | `794,926` | 263,227.85 USD | 12,754.48 USD | `+4.85%` | 2,571,200.15 USD | `+0.07` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.3313` | `0.3315` | `0.3312` | `0.3313` | `416,809` | 138,121.83 USD | 4,947.58 USD | `+3.58%` | 2,576,147.72 USD | `-0.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3313` | `0.3316` | `0.3313` | `0.3315` | `827,864` | 274,455.87 USD | 29,431.70 USD | `+10.72%` | 2,606,457.76 USD | `+0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3315` | `0.3316` | `0.3315` | `0.3315` | `294,203` | 97,541.21 USD | -27,950.14 USD | `-28.65%` | 2,578,507.62 USD | `-0.63` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3315` | `0.3316` | `0.3310` | `0.3313` | `2,251,264` | 745,820.37 USD | -2,359.90 USD | `-0.32%` | 2,576,147.72 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3312` | `0.3315` | `0.3311` | `0.3313` | `2,721,355` | 901,523.18 USD | 200,089.59 USD | `+22.19%` | 2,384,160.29 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.3313` | `0.3316` | `0.3312` | `0.3315` | `2,121,059` | 702,996.80 USD | 82,277.88 USD | `+11.70%` | 2,466,438.17 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3315` | `0.3316` | `0.3310` | `0.3313` | `2,251,264` | 745,820.37 USD | -2,359.90 USD | `-0.32%` | 2,464,078.27 USD | `-0.51` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3316` | `0.3310` | `0.3313` | `2,251,264` | 745,820.37 USD | -2,359.90 USD | `-0.32%` | 1,842,865.82 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,247,572.49 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 1,263,826.68 USD | `-1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3316` | `0.3310` | `0.3313` | `2,251,264` | 745,820.37 USD | -2,359.90 USD | `-0.32%` | 1,842,865.82 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3312`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1639` | `0xeadc...9d55` | `LONG` | 1,325,880.00 USD | `4,000,000.00` | `0.3421` | `0.3316` | `0.000000` | -42,598.09 USD | `-3.21%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,465.75 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3312 USD [API] | `2026-10-27 22:40:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3380` (Vol: 430,600.00 USD, Dist: `+1.97%`) | Long MP=`0.3248` (Vol: 480,000.00 USD, Dist: `--2.02%`)
  * 48H Horizon: Short MP=`0.3381` (Vol: 573,800.00 USD, Dist: `+1.99%`) | Long MP=`0.3250` (Vol: 640,100.00 USD, Dist: `--1.96%`)
  * 3D Horizon: Short MP=`0.3383` (Vol: 512,000.00 USD, Dist: `+2.05%`) | Long MP=`0.3250` (Vol: 602,700.00 USD, Dist: `--1.97%`)
  * 7D Horizon: Short MP=`0.3381` (Vol: 627,300.00 USD, Dist: `+1.97%`) | Long MP=`0.3250` (Vol: 663,500.00 USD, Dist: `--1.97%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0685` | 3,070.00 USD | 501,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 152.81 USD | 497,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 1,050.00 USD | 497,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 4,070.00 USD | 496,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 4,330.00 USD | 492,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 267.41 USD | 488,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 512.30 USD | 488,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 622.60 USD | 487,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 608.05 USD | 486,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 28,110.00 USD | 486,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,540.00 USD | 458,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 429.65 USD | 456,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 134.24 USD | 456,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 472.79 USD | 456,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 12,100.00 USD | 455,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 443,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 443,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 4,330.00 USD | 422,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,160.00 USD | 418,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 471.50 USD | 407,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 406,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 5,080.00 USD | 405,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 433.81 USD | 400,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 400,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,150.00 USD | 400,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 398,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 211.61 USD | 398,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 9,190.00 USD | 398,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 3,330.00 USD | 388,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 1,530.00 USD | 385,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 384,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 2,350.00 USD | 383,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 381,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 321.00 USD | 376,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 4,180.00 USD | 376,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,730.00 USD | 372,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 308.30 USD | 369,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,370.00 USD | 369,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 729.53 USD | 366,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,140.00 USD | 365,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 911.23 USD | 359,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 358,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 181.58 USD | 357,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,220.00 USD | 357,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 356,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 276.57 USD | 355,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,420.00 USD | 355,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 353,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 1,580.00 USD | 351,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 607.75 USD | 350,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 8,650.00 USD | 349,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 466.78 USD | 341,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 23,180.00 USD | 340,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,520.00 USD | 317,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 450.92 USD | 309,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 194.47 USD | 309,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 309,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 308,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 5,500.00 USD | 308,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 84,780.00 USD | 302,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 305.25 USD | 218,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 43,190.00 USD | 217,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,720.00 USD | 174,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 160,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,310.00 USD | 154,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 153,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 138,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 1,590.00 USD | 136,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 135,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 134,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 134,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 133,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 129,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,830,000.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 3,070,000.00 USD | 3,070,000.00 USD | 94,320.00 USD | 18,870.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,740,000.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2987` | 2,920,000.00 USD | 2,920,000.00 USD | 49,130.00 USD | 4,400.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,580,000.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,480,000.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 111,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 693.50 USD | 111,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,540.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,440,000.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,440,000.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,440,000.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 2,870,000.00 USD | 2,870,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,440,000.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 2,870,000.00 USD | 2,870,000.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,440,000.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3075` | 2,860,000.00 USD | 2,860,000.00 USD | 761.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,430,000.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 2,860,000.00 USD | 2,860,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,430,000.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 2,860,000.00 USD | 2,860,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,420,000.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 84,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 2,860,000.00 USD | 2,860,000.00 USD | 674.15 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,420,000.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 2,860,000.00 USD | 2,860,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,420,000.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,420,000.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,420,000.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 304.34 USD | 78,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,420,000.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 2,860,000.00 USD | 2,860,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,410,000.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,680.00 USD | 78,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 2,860,000.00 USD | 2,860,000.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,410,000.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 2,860,000.00 USD | 2,860,000.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,400,000.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3135` | 2,860,000.00 USD | 2,860,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,390,000.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 2,860,000.00 USD | 2,860,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,390,000.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 2,860,000.00 USD | 2,860,000.00 USD | 552.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,390,000.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 1,900.00 USD | 15,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 2,860,000.00 USD | 2,860,000.00 USD | 428.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,160,000.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,030,000.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,820,000.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3159` | 2,860,000.00 USD | 2,860,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,610,000.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 2,820,000.00 USD | 2,820,000.00 USD | 93,740.00 USD | 23,410.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,070,000.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 2,680,000.00 USD | 2,680,000.00 USD | 40,390.00 USD | 5,610.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 2,620,000.00 USD | 2,620,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,090,000.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 2,600,000.00 USD | 2,600,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,610,000.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3179` | 2,570,000.00 USD | 2,570,000.00 USD | 40,730.00 USD | 23,010.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,530,000.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 2,480,000.00 USD | 2,480,000.00 USD | 419,130.00 USD | 52,750.00 USD | 77,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,210,000.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 1,930,000.00 USD | 1,930,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,500,000.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,340,000.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 463.59 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,260,000.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,050,000.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,550,000.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,260,000.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,840,000.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 1,880,000.00 USD | 1,880,000.00 USD | 101,660.00 USD | 43,840.00 USD | 50,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 1,690,000.00 USD | 1,690,000.00 USD | 139,560.00 USD | 23,440.00 USD | 39,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,150,000.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 1,490,000.00 USD | 1,490,000.00 USD | 46,250.00 USD | 15,630.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,080,000.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 1,400,000.00 USD | 1,400,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,200,000.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 1,370,000.00 USD | 1,370,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,610,000.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 1,250,000.00 USD | 1,250,000.00 USD | 250,210.00 USD | 85,400.00 USD | 132,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,270,000.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 778,930.00 USD | 778,930.00 USD | 641,530.00 USD | 56,940.00 USD | 60,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,380,000.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3255` | 20,070.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3359` | 215,750.00 USD | 215,750.00 USD | 101,660.00 USD | 43,840.00 USD | 50,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3363` | 418,600.00 USD | 418,600.00 USD | 139,560.00 USD | 23,440.00 USD | 39,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3367` | 505,840.00 USD | 505,840.00 USD | 46,250.00 USD | 15,630.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3371` | 535,470.00 USD | 535,470.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3375` | 656,410.00 USD | 656,410.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3379` | 1,120,000.00 USD | 1,120,000.00 USD | 250,210.00 USD | 85,400.00 USD | 132,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 1,880,000.00 USD | 1,880,000.00 USD | 641,530.00 USD | 56,940.00 USD | 60,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3387` | 1,900,000.00 USD | 1,900,000.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 1,940,000.00 USD | 1,940,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3427` | 2,080,000.00 USD | 2,080,000.00 USD | 93,740.00 USD | 23,410.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 2,140,000.00 USD | 2,140,000.00 USD | 40,390.00 USD | 5,610.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3435` | 2,160,000.00 USD | 2,160,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3439` | 2,190,000.00 USD | 2,190,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 2,280,000.00 USD | 2,280,000.00 USD | 40,730.00 USD | 23,010.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3447` | 2,670,000.00 USD | 2,670,000.00 USD | 279,760.00 USD | 42,300.00 USD | 64,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 2,860,000.00 USD | 2,860,000.00 USD | 163,140.00 USD | 12,690.00 USD | 12,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3455` | 2,860,000.00 USD | 2,860,000.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3459` | 2,860,000.00 USD | 2,860,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3463` | 2,860,000.00 USD | 2,860,000.00 USD | 127.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3467` | 2,860,000.00 USD | 2,860,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 2,860,000.00 USD | 2,860,000.00 USD | 364.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 2,860,000.00 USD | 2,860,000.00 USD | 830.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 10,210.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3479` | 2,860,000.00 USD | 2,860,000.00 USD | 81.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 16,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 194,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3507` | 2,860,000.00 USD | 2,860,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 2,860,000.00 USD | 2,860,000.00 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3515` | 2,860,000.00 USD | 2,860,000.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3519` | 2,860,000.00 USD | 2,860,000.00 USD | 95.35 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 2,860,000.00 USD | 2,860,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3527` | 2,860,000.00 USD | 2,860,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 2,870,000.00 USD | 2,870,000.00 USD | 674.15 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3535` | 2,870,000.00 USD | 2,870,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 194,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3605` | 20,520.00 USD | 215,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 2,870,000.00 USD | 2,870,000.00 USD | 410.30 USD | 654.45 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 2,910,000.00 USD | 2,910,000.00 USD | 24,150.00 USD | 7,760.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3627` | 2,930,000.00 USD | 2,930,000.00 USD | 12,550.00 USD | 2,040.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 2,950,000.00 USD | 2,950,000.00 USD | 7,150.00 USD | 2,440.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3635` | 2,950,000.00 USD | 2,950,000.00 USD | 147.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 2,960,000.00 USD | 2,960,000.00 USD | 9,210.00 USD | 2,950.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 3,010,000.00 USD | 3,010,000.00 USD | 21,740.00 USD | 8,970.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 215,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3647` | 3,150,000.00 USD | 3,150,000.00 USD | 113,540.00 USD | 12,500.00 USD | 16,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 3,160,000.00 USD | 3,160,000.00 USD | 10,720.00 USD | 901.82 USD | 889.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 215,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 6,690.00 USD | 222,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3785` | 652.16 USD | 223,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 780,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3815` | 285.74 USD | 781,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 781,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3895` | 6,280.00 USD | 787,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 792,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 792,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 1,490.00 USD | 794,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 912,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 167.40 USD | 912,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4195` | 4,470.00 USD | 917,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 51,830.00 USD | 969,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 72,520.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 103.98 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5415` | 702,460.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5425` | 18,660.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5925` | 219.82 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0685` | 501,040.00 USD | 0.00 USD | 3,070.00 USD | `-79.34%` | `44,767.00` |
| `Live` | `Long` | `0.0735` | 497,970.00 USD | 0.00 USD | 152.81 USD | `-77.84%` | `2,079.00` |
| `Live` | `Long` | `0.0825` | 497,820.00 USD | 0.00 USD | 1,050.00 USD | `-75.12%` | `12,781.00` |
| `Live` | `Long` | `0.0995` | 496,760.00 USD | 0.00 USD | 4,070.00 USD | `-70.00%` | `40,871.00` |
| `Live` | `Long` | `0.1095` | 492,700.00 USD | 0.00 USD | 4,330.00 USD | `-66.98%` | `39,551.00` |
| `Live` | `Long` | `0.1125` | 488,370.00 USD | 0.00 USD | 267.41 USD | `-66.08%` | `2,377.00` |
| `Live` | `Long` | `0.1175` | 488,100.00 USD | 0.00 USD | 512.30 USD | `-64.57%` | `4,360.00` |
| `Live` | `Long` | `0.1185` | 487,590.00 USD | 0.00 USD | 622.60 USD | `-64.27%` | `5,254.00` |
| `Live` | `Long` | `0.1275` | 486,960.00 USD | 0.00 USD | 608.05 USD | `-61.55%` | `4,769.00` |
| `Live` | `Long` | `0.1285` | 486,360.00 USD | 0.00 USD | 28,110.00 USD | `-61.25%` | `218,745.00` |
| `Live` | `Long` | `0.1355` | 458,250.00 USD | 0.00 USD | 1,540.00 USD | `-59.14%` | `11,352.00` |
| `Live` | `Long` | `0.1405` | 456,710.00 USD | 0.00 USD | 429.65 USD | `-57.63%` | `3,058.00` |
| `Live` | `Long` | `0.1485` | 456,280.00 USD | 0.00 USD | 134.24 USD | `-55.22%` | `904.00` |
| `Live` | `Long` | `0.1565` | 456,150.00 USD | 0.00 USD | 472.79 USD | `-52.81%` | `3,021.00` |
| `Live` | `Long` | `0.1575` | 455,670.00 USD | 0.00 USD | 12,100.00 USD | `-52.51%` | `76,797.00` |
| `Live` | `Long` | `0.1595` | 443,580.00 USD | 0.00 USD | 390.46 USD | `-51.90%` | `2,448.00` |
| `Live` | `Long` | `0.1705` | 443,190.00 USD | 0.00 USD | 20,360.00 USD | `-48.59%` | `119,400.00` |
| `Live` | `Long` | `0.1715` | 422,830.00 USD | 0.00 USD | 4,330.00 USD | `-48.29%` | `25,269.00` |
| `Live` | `Long` | `0.1735` | 418,500.00 USD | 0.00 USD | 11,160.00 USD | `-47.68%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 407,340.00 USD | 0.00 USD | 471.50 USD | `-47.38%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 406,860.00 USD | 0.00 USD | 1,030.00 USD | `-47.08%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 405,830.00 USD | 0.00 USD | 5,080.00 USD | `-46.78%` | `28,764.00` |
| `Live` | `Long` | `0.1775` | 400,760.00 USD | 0.00 USD | 433.81 USD | `-46.48%` | `2,444.00` |
| `Live` | `Long` | `0.1795` | 400,320.00 USD | 0.00 USD | 209.84 USD | `-45.87%` | `1,169.00` |
| `Live` | `Long` | `0.1895` | 400,110.00 USD | 0.00 USD | 1,150.00 USD | `-42.86%` | `6,059.00` |
| `Live` | `Long` | `0.1975` | 398,970.00 USD | 0.00 USD | 632.00 USD | `-40.45%` | `3,200.00` |
| `Live` | `Long` | `0.2025` | 398,330.00 USD | 0.00 USD | 211.61 USD | `-38.94%` | `1,045.00` |
| `Live` | `Long` | `0.2045` | 398,120.00 USD | 0.00 USD | 9,190.00 USD | `-38.33%` | `44,921.00` |
| `Live` | `Long` | `0.2145` | 388,940.00 USD | 0.00 USD | 3,330.00 USD | `-35.32%` | `15,528.00` |
| `Live` | `Long` | `0.2185` | 385,610.00 USD | 0.00 USD | 1,530.00 USD | `-34.11%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 384,070.00 USD | 0.00 USD | 515.17 USD | `-33.81%` | `2,347.00` |
| `Live` | `Long` | `0.2225` | 383,560.00 USD | 0.00 USD | 2,350.00 USD | `-32.91%` | `10,560.00` |
| `Live` | `Long` | `0.2255` | 381,210.00 USD | 0.00 USD | 4,590.00 USD | `-32.00%` | `20,360.00` |
| `Live` | `Long` | `0.2275` | 376,620.00 USD | 0.00 USD | 321.00 USD | `-31.40%` | `1,411.00` |
| `Live` | `Long` | `0.2305` | 376,300.00 USD | 0.00 USD | 4,180.00 USD | `-30.49%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 372,110.00 USD | 0.00 USD | 2,730.00 USD | `-30.19%` | `11,792.00` |
| `Live` | `Long` | `0.2325` | 369,380.00 USD | 0.00 USD | 308.30 USD | `-29.89%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 369,080.00 USD | 0.00 USD | 2,370.00 USD | `-29.59%` | `10,154.00` |
| `Live` | `Long` | `0.2345` | 366,710.00 USD | 0.00 USD | 729.53 USD | `-29.29%` | `3,111.00` |
| `Live` | `Long` | `0.2355` | 365,980.00 USD | 0.00 USD | 6,140.00 USD | `-28.99%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 359,830.00 USD | 0.00 USD | 911.23 USD | `-28.69%` | `3,853.00` |
| `Live` | `Long` | `0.2385` | 358,920.00 USD | 0.00 USD | 1,260.00 USD | `-28.08%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 357,660.00 USD | 0.00 USD | 181.58 USD | `-27.48%` | `755.00` |
| `Live` | `Long` | `0.2445` | 357,480.00 USD | 0.00 USD | 1,220.00 USD | `-26.27%` | `5,004.00` |
| `Live` | `Long` | `0.2455` | 356,250.00 USD | 0.00 USD | 466.70 USD | `-25.97%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 355,790.00 USD | 0.00 USD | 276.57 USD | `-25.67%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 355,510.00 USD | 0.00 USD | 2,420.00 USD | `-25.37%` | `9,797.00` |
| `Live` | `Long` | `0.2565` | 353,090.00 USD | 0.00 USD | 1,230.00 USD | `-22.65%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 351,860.00 USD | 0.00 USD | 1,580.00 USD | `-22.05%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 350,280.00 USD | 0.00 USD | 607.75 USD | `-21.75%` | `2,342.00` |
| `Live` | `Long` | `0.2605` | 349,670.00 USD | 0.00 USD | 8,650.00 USD | `-21.45%` | `33,208.00` |
| `Live` | `Long` | `0.2615` | 341,020.00 USD | 0.00 USD | 466.78 USD | `-21.15%` | `1,785.00` |
| `Live` | `Long` | `0.2635` | 340,550.00 USD | 0.00 USD | 23,180.00 USD | `-20.54%` | `87,985.00` |
| `Live` | `Long` | `0.2655` | 317,370.00 USD | 0.00 USD | 7,520.00 USD | `-19.94%` | `28,325.00` |
| `Live` | `Long` | `0.2665` | 309,850.00 USD | 0.00 USD | 450.92 USD | `-19.64%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 309,400.00 USD | 0.00 USD | 194.47 USD | `-19.34%` | `727.00` |
| `Live` | `Long` | `0.2685` | 309,200.00 USD | 0.00 USD | 322.74 USD | `-19.04%` | `1,202.00` |
| `Live` | `Long` | `0.2725` | 308,880.00 USD | 0.00 USD | 412.84 USD | `-17.83%` | `1,515.00` |
| `Live` | `Long` | `0.2735` | 308,470.00 USD | 0.00 USD | 5,500.00 USD | `-17.53%` | `20,120.00` |
| `Live` | `Long` | `0.2755` | 302,970.00 USD | 0.00 USD | 84,780.00 USD | `-16.93%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 218,190.00 USD | 0.00 USD | 305.25 USD | `-16.32%` | `1,100.00` |
| `Live` | `Long` | `0.2785` | 217,880.00 USD | 0.00 USD | 43,190.00 USD | `-16.02%` | `155,075.00` |
| `Live` | `Long` | `0.2795` | 174,690.00 USD | 0.00 USD | 13,720.00 USD | `-15.72%` | `49,085.00` |
| `Live` | `Long` | `0.2805` | 160,970.00 USD | 0.00 USD | 6,280.00 USD | `-15.42%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 154,700.00 USD | 0.00 USD | 1,310.00 USD | `-15.12%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 153,390.00 USD | 0.00 USD | 15,060.00 USD | `-14.81%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 138,330.00 USD | 0.00 USD | 1,430.00 USD | `-14.51%` | `5,038.00` |
| `Live` | `Long` | `0.2845` | 136,900.00 USD | 0.00 USD | 1,590.00 USD | `-14.21%` | `5,572.00` |
| `Live` | `Long` | `0.2865` | 135,310.00 USD | 0.00 USD | 360.42 USD | `-13.61%` | `1,258.00` |
| `Live` | `Long` | `0.2915` | 134,950.00 USD | 0.00 USD | 591.45 USD | `-12.10%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 134,360.00 USD | 0.00 USD | 957.64 USD | `-11.80%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 133,400.00 USD | 0.00 USD | 3,760.00 USD | `-11.20%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 129,640.00 USD | 0.00 USD | 125.29 USD | `-10.89%` | `424.00` |
| `Live` | `Long` | `0.2995` | 129,520.00 USD | 0.00 USD | 127.89 USD | `-9.69%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,390.00 USD | 0.00 USD | 7,130.00 USD | `-9.39%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,260.00 USD | 0.00 USD | 10,330.00 USD | `-9.09%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 111,930.00 USD | 0.00 USD | 694.54 USD | `-8.78%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 111,240.00 USD | 0.00 USD | 693.50 USD | `-8.48%` | `2,285.00` |
| `Live` | `Long` | `0.3045` | 110,550.00 USD | 0.00 USD | 5,540.00 USD | `-8.18%` | `18,206.00` |
| `Live` | `Long` | `0.3055` | 105,000.00 USD | 0.00 USD | 5,300.00 USD | `-7.88%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 99,700.00 USD | 0.00 USD | 14,720.00 USD | `-7.58%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 84,980.00 USD | 0.00 USD | 6,670.00 USD | `-6.97%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 78,310.00 USD | 0.00 USD | 304.34 USD | `-6.07%` | `977.00` |
| `Live` | `Long` | `0.3125` | 78,010.00 USD | 0.00 USD | 17,680.00 USD | `-5.77%` | `56,580.00` |
| `Live` | `Long` | `0.3135` | 60,330.00 USD | 0.00 USD | 44,390.00 USD | `-5.47%` | `141,602.00` |
| `Live` | `Long` | `0.3145` | 15,940.00 USD | 0.00 USD | 1,900.00 USD | `-5.17%` | `6,027.00` |
| `Live` | `Long` | `0.3155` | 14,040.00 USD | 0.00 USD | 142.29 USD | `-4.86%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,900.00 USD | 0.00 USD | 1,490.00 USD | `-4.56%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,400.00 USD | 0.00 USD | 938.85 USD | `-4.26%` | `2,957.00` |
| `Live` | `Long` | `0.3195` | 11,460.00 USD | 0.00 USD | 463.59 USD | `-3.66%` | `1,451.00` |
| `Live` | `Long` | `0.3235` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-2.45%` | `34,003.00` |
| `Live` | `Short` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | `+3.28%` | `1,333.00` |
| `Live` | `Short` | `0.3435` | 610.44 USD | 153.89 USD | 0.00 USD | `+3.58%` | `448.00` |
| `Live` | `Short` | `0.3445` | 5,900.00 USD | 5,290.00 USD | 0.00 USD | `+3.88%` | `15,355.00` |
| `Live` | `Short` | `0.3455` | 6,390.00 USD | 486.46 USD | 0.00 USD | `+4.18%` | `1,408.00` |
| `Live` | `Short` | `0.3475` | 16,590.00 USD | 10,210.00 USD | 0.00 USD | `+4.79%` | `29,369.00` |
| `Live` | `Short` | `0.3485` | 16,820.00 USD | 223.04 USD | 0.00 USD | `+5.09%` | `640.00` |
| `Live` | `Short` | `0.3505` | 194,350.00 USD | 177,540.00 USD | 0.00 USD | `+5.69%` | `506,529.00` |
| `Live` | `Short` | `0.3535` | 194,580.00 USD | 223.06 USD | 0.00 USD | `+6.59%` | `631.00` |
| `Live` | `Short` | `0.3605` | 215,090.00 USD | 20,520.00 USD | 0.00 USD | `+8.71%` | `56,909.00` |
| `Live` | `Short` | `0.3645` | 215,470.00 USD | 376.53 USD | 0.00 USD | `+9.91%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 215,730.00 USD | 262.78 USD | 0.00 USD | `+10.51%` | `717.00` |
| `Live` | `Short` | `0.3745` | 222,420.00 USD | 6,690.00 USD | 0.00 USD | `+12.93%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 223,080.00 USD | 652.16 USD | 0.00 USD | `+14.13%` | `1,723.00` |
| `Live` | `Short` | `0.3795` | 780,970.00 USD | 557,900.00 USD | 0.00 USD | `+14.43%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 781,260.00 USD | 285.74 USD | 0.00 USD | `+15.04%` | `749.00` |
| `Live` | `Short` | `0.3845` | 781,370.00 USD | 115.35 USD | 0.00 USD | `+15.94%` | `300.00` |
| `Live` | `Short` | `0.3895` | 787,660.00 USD | 6,280.00 USD | 0.00 USD | `+17.45%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 792,430.00 USD | 4,770.00 USD | 0.00 USD | `+17.75%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 792,910.00 USD | 487.42 USD | 0.00 USD | `+18.05%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 794,400.00 USD | 1,490.00 USD | 0.00 USD | `+18.96%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 912,830.00 USD | 118,430.00 USD | 0.00 USD | `+19.26%` | `299,436.00` |
| `Live` | `Short` | `0.4185` | 912,990.00 USD | 167.40 USD | 0.00 USD | `+26.19%` | `400.00` |
| `Live` | `Short` | `0.4195` | 917,470.00 USD | 4,470.00 USD | 0.00 USD | `+26.50%` | `10,665.00` |
| `Live` | `Short` | `0.4245` | 969,300.00 USD | 51,830.00 USD | 0.00 USD | `+28.00%` | `122,096.00` |
| `Live` | `Short` | `0.4455` | 1,040,000.00 USD | 72,520.00 USD | 0.00 USD | `+34.34%` | `162,775.00` |
| `Live` | `Short` | `0.4475` | 1,040,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.94%` | `2,284.00` |
| `Live` | `Short` | `0.4705` | 1,040,000.00 USD | 103.98 USD | 0.00 USD | `+41.87%` | `221.00` |
| `Live` | `Short` | `0.4905` | 1,040,000.00 USD | 841.21 USD | 0.00 USD | `+47.91%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,050,000.00 USD | 5,130.00 USD | 0.00 USD | `+48.21%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 1,050,000.00 USD | 669.73 USD | 0.00 USD | `+61.17%` | `1,253.00` |
| `Live` | `Short` | `0.5415` | 1,750,000.00 USD | 702,460.00 USD | 0.00 USD | `+63.28%` | `1,297,248.00` |
| `Live` | `Short` | `0.5425` | 1,770,000.00 USD | 18,660.00 USD | 0.00 USD | `+63.59%` | `34,396.00` |
| `Live` | `Short` | `0.5585` | 1,770,000.00 USD | 742.25 USD | 0.00 USD | `+68.41%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,770,000.00 USD | 140.62 USD | 0.00 USD | `+69.62%` | `250.00` |
| `Live` | `Short` | `0.5925` | 1,770,000.00 USD | 219.82 USD | 0.00 USD | `+78.66%` | `371.00` |
| `Live` | `Short` | `0.6145` | 1,810,000.00 USD | 36,870.00 USD | 0.00 USD | `+85.30%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,810,000.00 USD | 275.47 USD | 0.00 USD | `+89.22%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,820,000.00 USD | 7,390.00 USD | 0.00 USD | `+89.52%` | `11,753.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 819,410.00 USD | 0.00 USD | 6,100.00 USD | `-45.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 813,310.00 USD | 0.00 USD | 1,750.00 USD | `-38.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 811,550.00 USD | 0.00 USD | 579.72 USD | `-36.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 810,980.00 USD | 0.00 USD | 705.61 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 810,270.00 USD | 0.00 USD | 1,200.00 USD | `-27.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 809,070.00 USD | 0.00 USD | 127.51 USD | `-27.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 808,940.00 USD | 0.00 USD | 1,850.00 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 807,090.00 USD | 0.00 USD | 1,920.00 USD | `-22.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 805,160.00 USD | 0.00 USD | 4,200.00 USD | `-21.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 800,960.00 USD | 0.00 USD | 954.98 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 800,010.00 USD | 0.00 USD | 695.50 USD | `-19.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 799,310.00 USD | 0.00 USD | 1,630.00 USD | `-19.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 797,680.00 USD | 0.00 USD | 2,550.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 795,130.00 USD | 0.00 USD | 229.92 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 794,900.00 USD | 0.00 USD | 15,940.00 USD | `-11.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 778,960.00 USD | 0.00 USD | 111.19 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 778,850.00 USD | 0.00 USD | 685.95 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 778,160.00 USD | 0.00 USD | 2,710.00 USD | `-9.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 775,460.00 USD | 0.00 USD | 335.56 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 775,120.00 USD | 0.00 USD | 919.50 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 774,200.00 USD | 0.00 USD | 193.11 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 774,010.00 USD | 0.00 USD | 16,070.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 757,940.00 USD | 0.00 USD | 147.32 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 757,800.00 USD | 0.00 USD | 25,820.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 731,980.00 USD | 0.00 USD | 6,530.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 725,450.00 USD | 0.00 USD | 524,570.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 200,880.00 USD | 0.00 USD | 1,270.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 199,610.00 USD | 0.00 USD | 25,790.00 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 173,820.00 USD | 0.00 USD | 3,610.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 170,210.00 USD | 0.00 USD | 6,100.00 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 164,120.00 USD | 0.00 USD | 2,010.00 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 162,100.00 USD | 0.00 USD | 15,160.00 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 146,940.00 USD | 0.00 USD | 21,270.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 125,670.00 USD | 0.00 USD | 55,600.00 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 70,070.00 USD | 0.00 USD | 174.47 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 69,900.00 USD | 0.00 USD | 845.95 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 69,050.00 USD | 0.00 USD | 14,470.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 54,580.00 USD | 0.00 USD | 8,270.00 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 46,310.00 USD | 0.00 USD | 25,490.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 20,820.00 USD | 0.00 USD | 13,320.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 7,500.00 USD | 0.00 USD | 3,730.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 3,770.00 USD | 0.00 USD | 1,830.00 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 1,940.00 USD | 0.00 USD | 1,840.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 100.11 USD | 0.00 USD | 100.11 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 40,600.00 USD | 40,600.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 42,080.00 USD | 1,480.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 43,300.00 USD | 1,220.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 218,160.00 USD | 174,860.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 218,280.00 USD | 119.79 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 218,450.00 USD | 162.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 230,090.00 USD | 11,640.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 230,190.00 USD | 102.87 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 233,280.00 USD | 3,090.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 234,180.00 USD | 904.63 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 239,710.00 USD | 5,520.00 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 247,320.00 USD | 7,610.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 250,200.00 USD | 2,880.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 258,130.00 USD | 7,930.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 261,280.00 USD | 3,150.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 262,340.00 USD | 1,060.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 288,090.00 USD | 25,750.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 306,670.00 USD | 18,580.00 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 320,090.00 USD | 13,420.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 320,860.00 USD | 769.97 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 321,090.00 USD | 226.10 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 325,270.00 USD | 4,180.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 331,260.00 USD | 5,990.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 337,440.00 USD | 6,180.00 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 337,930.00 USD | 485.59 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 338,320.00 USD | 390.40 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 338,750.00 USD | 433.85 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 339,210.00 USD | 463.99 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 339,370.00 USD | 159.62 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 340,300.00 USD | 926.99 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 343,080.00 USD | 2,780.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 343,350.00 USD | 275.17 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 343,820.00 USD | 463.37 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 344,150.00 USD | 337.12 USD | 0.00 USD | `+14.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 344,270.00 USD | 114.83 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 344,490.00 USD | 224.73 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 345,010.00 USD | 514.64 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 345,360.00 USD | 352.11 USD | 0.00 USD | `+17.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 347,760.00 USD | 2,400.00 USD | 0.00 USD | `+19.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 348,330.00 USD | 572.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 349,530.00 USD | 1,200.00 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 402,410.00 USD | 52,880.00 USD | 0.00 USD | `+20.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 404,810.00 USD | 2,400.00 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 406,010.00 USD | 1,200.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 407,210.00 USD | 1,200.00 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 408,410.00 USD | 1,200.00 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 408,600.00 USD | 186.70 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 447,170.00 USD | 38,580.00 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 447,340.00 USD | 170.69 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 448,730.00 USD | 1,390.00 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 459,880.00 USD | 11,150.00 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2979` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 94,320.00 USD | 18,870.00 USD | 31,110.00 USD |
| `7D` | `0.2983` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD |
| `1D` | `0.2987` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 49,130.00 USD | 4,400.00 USD | 3,940.00 USD |
| `7D` | `0.2987` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `7D` | `0.2991` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `7D` | `0.3051` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 761.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3083` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 674.15 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3123` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 3,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3131` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 552.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3147` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 428.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD |
| `7D` | `0.3151` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD |
| `1D` | `0.3159` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 93,740.00 USD | 23,410.00 USD | 22,560.00 USD |
| `7D` | `0.3163` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `1D` | `0.3167` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 40,390.00 USD | 5,610.00 USD | 10,160.00 USD |
| `7D` | `0.3167` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3171` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3171` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3175` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3179` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 40,730.00 USD | 23,010.00 USD | 27,720.00 USD |
| `7D` | `0.3179` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3183` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 419,130.00 USD | 52,750.00 USD | 77,130.00 USD |
| `7D` | `0.3183` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD |
| `1D` | `0.3187` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD |
| `7D` | `0.3187` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `7D` | `0.3207` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `7D` | `0.3211` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3219` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3223` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3223` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3227` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 101,660.00 USD | 43,840.00 USD | 50,000.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3231` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 139,560.00 USD | 23,440.00 USD | 39,840.00 USD |
| `7D` | `0.3231` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 46,250.00 USD | 15,630.00 USD | 25,360.00 USD |
| `7D` | `0.3235` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3239` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3239` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3243` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3243` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 250,210.00 USD | 85,400.00 USD | 132,860.00 USD |
| `7D` | `0.3247` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `1D` | `0.3251` | 778,930.00 USD | 0.00 USD | 778,930.00 USD | 641,530.00 USD | 56,940.00 USD | 60,390.00 USD |
| `7D` | `0.3251` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3255` | 20,070.00 USD | 0.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3312` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3315` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3359` | 215,750.00 USD | 215,750.00 USD | 0.00 USD | 101,660.00 USD | 43,840.00 USD | 50,000.00 USD |
| `7D` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3363` | 418,600.00 USD | 418,600.00 USD | 0.00 USD | 139,560.00 USD | 23,440.00 USD | 39,840.00 USD |
| `7D` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 505,840.00 USD | 505,840.00 USD | 0.00 USD | 46,250.00 USD | 15,630.00 USD | 25,360.00 USD |
| `7D` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3371` | 535,470.00 USD | 535,470.00 USD | 0.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3375` | 656,410.00 USD | 656,410.00 USD | 0.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 250,210.00 USD | 85,400.00 USD | 132,860.00 USD |
| `7D` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `1D` | `0.3383` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 641,530.00 USD | 56,940.00 USD | 60,390.00 USD |
| `7D` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3387` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `7D` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `7D` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD |
| `7D` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3423` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 93,740.00 USD | 23,410.00 USD | 22,560.00 USD |
| `7D` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `1D` | `0.3431` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 40,390.00 USD | 5,610.00 USD | 10,160.00 USD |
| `7D` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3435` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3443` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 40,730.00 USD | 23,010.00 USD | 27,720.00 USD |
| `7D` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3447` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 279,760.00 USD | 42,300.00 USD | 64,350.00 USD |
| `7D` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD |
| `1D` | `0.3451` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 163,140.00 USD | 12,690.00 USD | 12,780.00 USD |
| `7D` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3455` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3459` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 127.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3467` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3471` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 364.10 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 830.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 81.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3515` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 95.35 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3527` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 674.15 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3535` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `7D` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 410.30 USD | 654.45 USD | 5,890.00 USD |
| `7D` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3623` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 24,150.00 USD | 7,760.00 USD | 8,880.00 USD |
| `7D` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD |
| `1D` | `0.3627` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 12,550.00 USD | 2,040.00 USD | 3,680.00 USD |
| `7D` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 7,150.00 USD | 2,440.00 USD | 4,520.00 USD |
| `7D` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3635` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 147.65 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3639` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 9,210.00 USD | 2,950.00 USD | 2,470.00 USD |
| `7D` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 21,740.00 USD | 8,970.00 USD | 16,150.00 USD |
| `7D` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD |
| `1D` | `0.3647` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 113,540.00 USD | 12,500.00 USD | 16,890.00 USD |
| `7D` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `1D` | `0.3649` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 10,720.00 USD | 901.82 USD | 889.69 USD |
| `7D` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `305.90M` | Total OI Tokens: `923,057,899.8 TRX`
  * 1h OI Change: `+2.59%` | 4h OI Change: `+2.25%` | 24h OI Change: `+4.73%`
  * Exchange Breakdown: Binance=`90.65M` | Bybit=`49.78M` | OKX=`13.76M` | Hyperliquid=`11.67M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.59K` | Last 24h: `9.22K` | Last 3d: `-51.81K` | Last 7d: `-271.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0085%` | **USDT OKX** | `-0.0051%` |
| **USDT Bybit** | `0.0061%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0085%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0096%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `56.44%` | `43.56%` | `1.30` | 2,410,000.00 USD |
| `15M` | `Binance` | `48.36%` | `51.64%` | `0.94` | 787,450.00 USD |
| `15M` | `OKX` | `56.09%` | `43.91%` | `1.28` | 215,430.00 USD |
| `15M` | `Bybit` | `52.32%` | `47.68%` | `1.10` | 138,110.00 USD |
| `15M` | `KuCoin` | `64.17%` | `35.83%` | `1.79` | 12,390.00 USD |
| `15M` | `Gate` | `88.49%` | `11.51%` | `7.69` | 488,590.00 USD |
| `15M` | `Bitget` | `58.45%` | `41.55%` | `1.41` | 37,400.00 USD |
| `15M` | `BingX` | `31.8%` | `68.2%` | `0.47` | 56,250.00 USD |
| `15M` | `MEXC` | `45.27%` | `54.73%` | `0.83` | 27,220.00 USD |
| `15M` | `Bitunix` | `61.74%` | `38.26%` | `1.61` | 30,210.00 USD |
| `15M` | `Hyperliquid` | `66.17%` | `33.83%` | `1.96` | 20,580.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.05%` | `49.95%` | `1.00` | 399,080.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `23.17%` | `76.83%` | `0.30` | 164,870.00 USD |
| `15M` | `HTX` | `65.41%` | `34.59%` | `1.89` | 17,540.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `86.91%` | `13.09%` | `6.64` | 8,580.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 591.41 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.88%` | `2.12%` | `46.17` | 3,770.00 USD |
| `15M` | `Whale Positions` | `48.36%` | `51.64%` | `0.94` | 787,450.00 USD |
| `15M` | `Global Accounts` | `56.44%` | `43.56%` | `1.30` | 2,410,000.00 USD |
| `1H` | `TRX` | `50.03%` | `49.97%` | `1.00` | 4,410,000.00 USD |
| `1H` | `Binance` | `52.67%` | `47.33%` | `1.11` | 1,350,000.00 USD |
| `1H` | `OKX` | `54.61%` | `45.39%` | `1.20` | 320,950.00 USD |
| `1H` | `Bybit` | `71.19%` | `28.81%` | `2.47` | 264,820.00 USD |
| `1H` | `KuCoin` | `57.69%` | `42.31%` | `1.36` | 55,140.00 USD |
| `1H` | `Gate` | `84.69%` | `15.31%` | `5.53` | 563,110.00 USD |
| `1H` | `Bitget` | `60.11%` | `39.89%` | `1.51` | 47,050.00 USD |
| `1H` | `BingX` | `16.13%` | `83.87%` | `0.19` | 396,520.00 USD |
| `1H` | `MEXC` | `56.59%` | `43.41%` | `1.30` | 33,980.00 USD |
| `1H` | `Bitunix` | `60.58%` | `39.42%` | `1.54` | 45,210.00 USD |
| `1H` | `Hyperliquid` | `74.09%` | `25.91%` | `2.86` | 34,850.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.07%` | `50.93%` | `0.96` | 678,510.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.01%` | `84.99%` | `0.18` | 496,310.00 USD |
| `1H` | `HTX` | `59.87%` | `40.13%` | `1.49` | 52,360.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.43%` | `32.57%` | `2.07` | 15,050.00 USD |
| `1H` | `Aster` | `4.2%` | `95.8%` | `0.04` | 1,150.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.66%` | `84.34%` | `0.19` | 53,450.00 USD |
| `1H` | `Whale Positions` | `52.67%` | `47.33%` | `1.11` | 1,350,000.00 USD |
| `1H` | `Global Accounts` | `50.03%` | `49.97%` | `1.00` | 4,410,000.00 USD |
| `4H` | `TRX` | `45.83%` | `54.17%` | `0.85` | 12,270,000.00 USD |
| `4H` | `Binance` | `51.04%` | `48.96%` | `1.04` | 4,160,000.00 USD |
| `4H` | `OKX` | `48.69%` | `51.31%` | `0.95` | 764,100.00 USD |
| `4H` | `Bybit` | `65.13%` | `34.87%` | `1.87` | 620,920.00 USD |
| `4H` | `KuCoin` | `50.78%` | `49.22%` | `1.03` | 251,060.00 USD |
| `4H` | `Gate` | `76.87%` | `23.13%` | `3.32` | 765,310.00 USD |
| `4H` | `Bitget` | `57.76%` | `42.24%` | `1.37` | 152,320.00 USD |
| `4H` | `BingX` | `24.38%` | `75.62%` | `0.32` | 1,080,000.00 USD |
| `4H` | `MEXC` | `49.7%` | `50.3%` | `0.99` | 122,070.00 USD |
| `4H` | `Bitunix` | `53.35%` | `46.65%` | `1.14` | 130,130.00 USD |
| `4H` | `Hyperliquid` | `72.12%` | `27.88%` | `2.59` | 237,780.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.85%` | `50.15%` | `0.99` | 1,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.39%` | `88.61%` | `0.13` | 1,670,000.00 USD |
| `4H` | `HTX` | `56.43%` | `43.57%` | `1.30` | 200,540.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.72%` | `23.28%` | `3.30` | 58,550.00 USD |
| `4H` | `Aster` | `7.13%` | `92.87%` | `0.08` | 8,600.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `29.83%` | `70.17%` | `0.43` | 86,610.00 USD |
| `4H` | `Whale Positions` | `51.04%` | `48.96%` | `1.04` | 4,160,000.00 USD |
| `4H` | `Global Accounts` | `45.83%` | `54.17%` | `0.85` | 12,270,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3313` | `0.3312` | `0.3313` | `0.3313` | `0.3311` | 257,613.17 USD | 129,803.39 USD | 127,809.78 USD | 1,993.62 USD | `+0.77%` | `7B / 11S` |
| `0:00 UTC` | `0.3311` | `0.3311` | `0.3311` | `0.3312` | `0.3311` | 152,723.77 USD | 63,964.61 USD | 88,759.15 USD | -24,794.54 USD | `-16.23%` | `3B / 5S` |
| `5:00 UTC` | `0.3312` | `0.3313` | `0.3312` | `0.3314` | `0.3312` | 241,719.94 USD | 169,546.92 USD | 72,173.03 USD | 97,373.89 USD | `+40.28%` | `9B / 3S` |
| `0:00 UTC` | `0.3314` | `0.3313` | `0.3314` | `0.3315` | `0.3312` | 417,486.18 USD | 289,418.38 USD | 128,067.80 USD | 161,350.58 USD | `+38.65%` | `12B / 5S` |
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 89,593.30 USD | 27,876.48 USD | 61,716.82 USD | -33,840.33 USD | `-37.77%` | `1B / 7S` |
| `0:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 149,813.03 USD | 80,120.40 USD | 69,692.63 USD | 10,427.77 USD | `+6.96%` | `4B / 2S` |
| `5:00 UTC` | `0.3314` | `0.3314` | `0.3314` | `0.3315` | `0.3313` | 181,186.70 USD | 125,777.62 USD | 55,409.08 USD | 70,368.54 USD | `+38.84%` | `7B / 3S` |
| `0:00 UTC` | `0.3316` | `0.3315` | `0.3316` | `0.3316` | `0.3313` | 274,455.87 USD | 151,943.78 USD | 122,512.08 USD | 29,431.70 USD | `+10.72%` | `6B / 8S` |
| `5:00 UTC` | `0.3316` | `0.3315` | `0.3316` | `0.3316` | `0.3315` | 97,541.21 USD | 34,795.54 USD | 62,745.67 USD | -27,950.14 USD | `-28.65%` | `4B / 4S` |
| `0:00 UTC` | `0.3311` | `0.3313` | `0.3311` | `0.3316` | `0.3310` | 636,565.29 USD | 315,121.04 USD | 321,444.24 USD | -6,323.20 USD | `-0.99%` | `19B / 21S` |

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
| `5m` | -14,690.00 USD | 172,190.00 USD | **`ACCUMULATION`** |
| `15m` | -182,010.00 USD | 43,090.00 USD | **`DISTRIBUTION`** |
| `30m` | -295,220.00 USD | 1,260.00 USD | **`DISTRIBUTION`** |
| `1h` | 107,100.00 USD | 232,430.00 USD | **`ACCUMULATION`** |
| `2h` | 241,820.00 USD | 592,240.00 USD | **`ACCUMULATION`** |
| `4h` | 169,350.00 USD | 294,250.00 USD | **`ACCUMULATION`** |
| `6h` | 1,070,000.00 USD | 852,450.00 USD | **`ACCUMULATION`** |
| `8h` | 200,060.00 USD | 505,120.00 USD | **`ACCUMULATION`** |
| `12h` | 231,790.00 USD | 828,160.00 USD | **`ACCUMULATION`** |
| `24h` | 3,160,000.00 USD | 3,810,000.00 USD | **`ACCUMULATION`** |
| `1w` | -4,220,000.00 USD | 1,830,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,370,000.00 USD | 3,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-14.69K` | 15m=`-182.01K` | 1h=`+107.10K` | 24h=`+3.16M`
* Futures Capital Netflows: 5m=`+172.19K` | 15m=`+43.09K` | 1h=`+232.43K` | 24h=`+3.81M`
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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3296` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3272` (Risk Distance: `0.0026` pts)
  * +2.5R Take Profit: `0.3361`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3336` (Risk Distance: `0.0026` pts)
  * +2.5R Take Profit: `0.3247`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3339`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
