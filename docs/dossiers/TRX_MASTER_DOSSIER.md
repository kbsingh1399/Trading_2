# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 00:23:15 IST` (`2026-10-29 18:53:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3307` | **Live Ask Quote**: `0.3319` | **Mid Price**: `0.3313`
- **Spread Points**: `12.00` | **Spread BPS**: `36.22 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3302` | VWAP Z-Score: `+0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000363` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3325` | Lower -3.00σ Band: `0.3280`
  * Upper +2.51σ Band: `0.3321` | Lower -2.51σ Band: `0.3283`
  * Upper +2.01σ Band: `0.3318` | Lower -2.01σ Band: `0.3287`
  * Upper +2.00σ Band: `0.3317` | Lower -2.00σ Band: `0.3287`
  * Upper +1.28σ Band: `0.3312` | Lower -1.28σ Band: `0.3293`
  * Upper +1.00σ Band: `0.3310` | Lower -1.00σ Band: `0.3295`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3307` | EMA-20=`0.3307` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3306` (Slope: `+0.0000`) | EMA-100=`0.3304`
  * Institutional Anchors: EMA-144=`0.3302` | EMA-200=`0.3300` (Slope: `+0.0261`) | EMA-233=`0.3299`
- **Range Boundaries**: 24H High=`0.3313` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `+0.03%`)
  * Point of Control (POC) = `0.3307` (Distance: `+0.18%`)
  * Value Area Low (VAL) = `0.3294` (Distance: `+0.58%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `0.3300` - `0.3326`
  * Optimal Trade Entry (OTE 0.705): `0.3320`
  * Structural Invalidation Anchor (0.786): `0.3340`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3313` | `0.3313` | `0.3313` | `0.3313` | `53,738` | 17,803.10 USD | -8,480.85 USD | `-47.64%` | 2,111,616.52 USD | `-0.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3313` | `0.3314` | `0.3312` | `0.3313` | `652,092` | 216,068.43 USD | 107,124.03 USD | `+49.58%` | 2,218,740.55 USD | `+2.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3313` | `0.3313` | `0.3312` | `0.3312` | `29,641` | 9,819.36 USD | -7,099.41 USD | `-72.30%` | 2,211,641.14 USD | `-0.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3312` | `0.3312` | `0.3311` | `0.3312` | `461,221` | 152,723.77 USD | -24,794.54 USD | `-16.23%` | 1,952,324.44 USD | `-0.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3312` | `0.3314` | `0.3312` | `0.3313` | `729,696` | 241,719.94 USD | 97,373.89 USD | `+40.28%` | 2,049,698.33 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3313` | `0.3314` | `0.3312` | `0.3312` | `681,733` | 225,887.79 USD | 100,024.62 USD | `+44.28%` | 2,149,722.95 USD | `+0.83` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3314` | `0.3316` | `0.3311` | `0.3311` | `3,106,966` | 1,029,390.94 USD | -31,067.74 USD | `-3.02%` | 2,031,724.83 USD | `-0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3311` | `0.3313` | `0.3310` | `0.3312` | `3,301,362` | 1,093,342.85 USD | -39,208.85 USD | `-3.59%` | 1,992,515.98 USD | `-0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3312` | `0.3314` | `0.3311` | `0.3312` | `1,872,650` | 620,331.50 USD | 172,603.97 USD | `+27.82%` | 2,165,119.95 USD | `+0.35` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3312` | `8,280,875` | 2,743,031.17 USD | 102,361.50 USD | `+3.73%` | 2,482,260.68 USD | `-1.13` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3296` | `0.3308` | `0.3290` | `0.3307` | `23,140,787` | 7,631,473.08 USD | 600,887.06 USD | `+7.87%` | 1,347,651.40 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,994,336.82 USD | `-0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3314` | `8,863,440` | 2,936,046.78 USD | 162,714.26 USD | `+5.54%` | 2,542,613.45 USD | `-0.98` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`0.3313`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1649` | `0xeadc...9d55` | `LONG` | 1,325,640.00 USD | `4,000,000.00` | `0.3421` | `0.3314` | `0.000000` | -42,838.09 USD | `-3.23%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,465.75 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3312 USD [API] | `2026-10-27 22:40:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3380` (Vol: 384,800.00 USD, Dist: `+2.00%`) | Long MP=`0.3248` (Vol: 434,200.00 USD, Dist: `--1.99%`)
  * 48H Horizon: Short MP=`0.3382` (Vol: 574,000.00 USD, Dist: `+2.04%`) | Long MP=`0.3250` (Vol: 648,500.00 USD, Dist: `--1.95%`)
  * 3D Horizon: Short MP=`0.3383` (Vol: 512,000.00 USD, Dist: `+2.08%`) | Long MP=`0.3250` (Vol: 602,700.00 USD, Dist: `--1.94%`)
  * 7D Horizon: Short MP=`0.3381` (Vol: 627,400.00 USD, Dist: `+2.01%`) | Long MP=`0.3250` (Vol: 663,500.00 USD, Dist: `--1.94%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0685` | 2,740.00 USD | 500,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 331.31 USD | 497,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 150.73 USD | 497,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 1,050.00 USD | 497,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 4,230.00 USD | 495,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 4,370.00 USD | 491,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 803.93 USD | 487,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 113.50 USD | 486,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 486,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 643.62 USD | 486,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 27,020.00 USD | 485,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 1,560.00 USD | 458,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 429.65 USD | 456,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 130.63 USD | 456,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 371.55 USD | 456,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 469.77 USD | 455,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 455,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 12,400.00 USD | 455,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 442,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 3,930.00 USD | 422,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,160.00 USD | 418,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 471.50 USD | 407,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 406,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 5,080.00 USD | 405,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 433.81 USD | 400,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 400,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,150.00 USD | 399,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 838.39 USD | 398,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2025` | 3,020.00 USD | 397,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 6,130.00 USD | 394,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 3,330.00 USD | 388,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 385,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 383,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2235` | 2,360.00 USD | 383,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 381,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 319.59 USD | 376,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 4,180.00 USD | 376,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 3,010.00 USD | 372,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 308.30 USD | 368,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,370.00 USD | 368,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 1,000.00 USD | 366,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,140.00 USD | 365,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 359,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 358,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 510.10 USD | 357,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 357,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 356,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 276.57 USD | 355,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,420.00 USD | 355,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 352,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 1,580.00 USD | 351,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 315.81 USD | 350,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 8,650.00 USD | 349,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 466.78 USD | 341,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 22,990.00 USD | 340,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 405.00 USD | 317,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,520.00 USD | 317,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 450.92 USD | 309,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 194.47 USD | 309,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 309,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 308,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 5,500.00 USD | 308,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 84,780.00 USD | 302,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 41,220.00 USD | 218,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 2,130.00 USD | 176,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,720.00 USD | 174,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 161,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,310.00 USD | 154,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 153,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 138,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 482.75 USD | 137,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 1,600.00 USD | 136,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 134,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 134,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 133,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 129,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,850,000.00 USD | 12,850,000.00 USD | 69,830.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 3,030,000.00 USD | 3,030,000.00 USD | 91,050.00 USD | 16,880.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,760,000.00 USD | 12,760,000.00 USD | 117,250.00 USD | 9,990.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2987` | 2,890,000.00 USD | 2,890,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,600,000.00 USD | 12,600,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,500,000.00 USD | 12,500,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 111,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 693.50 USD | 111,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,540.00 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,460,000.00 USD | 12,460,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,460,000.00 USD | 12,460,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,460,000.00 USD | 12,460,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 2,840,000.00 USD | 2,840,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,460,000.00 USD | 12,460,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 2,840,000.00 USD | 2,840,000.00 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,450,000.00 USD | 12,450,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3075` | 2,840,000.00 USD | 2,840,000.00 USD | 1,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,450,000.00 USD | 12,450,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 2,830,000.00 USD | 2,830,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,450,000.00 USD | 12,450,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 2,830,000.00 USD | 2,830,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,440,000.00 USD | 12,440,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 84,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 2,830,000.00 USD | 2,830,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,440,000.00 USD | 12,440,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 2,830,000.00 USD | 2,830,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,440,000.00 USD | 12,440,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,440,000.00 USD | 12,440,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 304.34 USD | 78,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,440,000.00 USD | 12,440,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 2,830,000.00 USD | 2,830,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,430,000.00 USD | 12,430,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,680.00 USD | 78,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 2,830,000.00 USD | 2,830,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,430,000.00 USD | 12,430,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 2,830,000.00 USD | 2,830,000.00 USD | 1,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,420,000.00 USD | 12,420,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3135` | 2,830,000.00 USD | 2,830,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,410,000.00 USD | 12,410,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 2,830,000.00 USD | 2,830,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,410,000.00 USD | 12,410,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 2,830,000.00 USD | 2,830,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,410,000.00 USD | 12,410,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 1,900.00 USD | 15,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 2,830,000.00 USD | 2,830,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,180,000.00 USD | 12,180,000.00 USD | 101,370.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,050,000.00 USD | 12,050,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,840,000.00 USD | 11,840,000.00 USD | 157,220.00 USD | 37,570.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3159` | 2,830,000.00 USD | 2,830,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,620,000.00 USD | 11,620,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 2,790,000.00 USD | 2,790,000.00 USD | 98,530.00 USD | 30,960.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,060,000.00 USD | 11,060,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 2,630,000.00 USD | 2,630,000.00 USD | 46,570.00 USD | 11,520.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,580,000.00 USD | 10,580,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 2,560,000.00 USD | 2,560,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,080,000.00 USD | 10,080,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 2,530,000.00 USD | 2,530,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,600,000.00 USD | 9,600,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3179` | 2,510,000.00 USD | 2,510,000.00 USD | 39,170.00 USD | 22,020.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,520,000.00 USD | 9,520,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 2,420,000.00 USD | 2,420,000.00 USD | 391,660.00 USD | 47,640.00 USD | 68,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,200,000.00 USD | 9,200,000.00 USD | 551,920.00 USD | 51,290.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 335.70 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3187` | 1,910,000.00 USD | 1,910,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,510,000.00 USD | 8,510,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,350,000.00 USD | 8,350,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 126.84 USD | 11,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,270,000.00 USD | 8,270,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,070,000.00 USD | 8,070,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,560,000.00 USD | 7,560,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,270,000.00 USD | 7,270,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,830,000.00 USD | 6,830,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 1,860,000.00 USD | 1,860,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 1,670,000.00 USD | 1,670,000.00 USD | 161,500.00 USD | 45,670.00 USD | 55,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,090,000.00 USD | 5,090,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 1,400,000.00 USD | 1,400,000.00 USD | 46,250.00 USD | 20,320.00 USD | 28,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,030,000.00 USD | 4,030,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 1,310,000.00 USD | 1,310,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,150,000.00 USD | 3,150,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 1,280,000.00 USD | 1,280,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,560,000.00 USD | 2,560,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 1,160,000.00 USD | 1,160,000.00 USD | 232,030.00 USD | 77,350.00 USD | 123,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,210,000.00 USD | 2,210,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 725,950.00 USD | 725,950.00 USD | 601,650.00 USD | 52,790.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,370,000.00 USD | 1,370,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3255` | 20,070.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,440,000.00 USD | 1,440,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,100,000.00 USD | 2,100,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,180,000.00 USD | 3,180,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3363` | 480,390.00 USD | 480,390.00 USD | 161,500.00 USD | 45,670.00 USD | 55,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,240,000.00 USD | 4,240,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3367` | 575,220.00 USD | 575,220.00 USD | 46,250.00 USD | 20,320.00 USD | 28,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3371` | 604,850.00 USD | 604,850.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,710,000.00 USD | 5,710,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3375` | 725,790.00 USD | 725,790.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 6,060,000.00 USD | 6,060,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3379` | 1,160,000.00 USD | 1,160,000.00 USD | 232,030.00 USD | 77,350.00 USD | 123,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,900,000.00 USD | 6,900,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 1,860,000.00 USD | 1,860,000.00 USD | 601,650.00 USD | 52,790.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,840,000.00 USD | 7,840,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3387` | 1,880,000.00 USD | 1,880,000.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,190,000.00 USD | 8,190,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,270,000.00 USD | 8,270,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,370,000.00 USD | 8,370,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,580,000.00 USD | 8,580,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,760,000.00 USD | 8,760,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,870,000.00 USD | 8,870,000.00 USD | 75,860.00 USD | 17,240.00 USD | 26,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,100,000.00 USD | 9,100,000.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 1,920,000.00 USD | 1,920,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,620,000.00 USD | 9,620,000.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3427` | 2,080,000.00 USD | 2,080,000.00 USD | 98,530.00 USD | 30,960.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,090,000.00 USD | 10,090,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 2,150,000.00 USD | 2,150,000.00 USD | 46,570.00 USD | 11,520.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3435` | 2,180,000.00 USD | 2,180,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,070,000.00 USD | 11,070,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3439` | 2,200,000.00 USD | 2,200,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,150,000.00 USD | 11,150,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 2,290,000.00 USD | 2,290,000.00 USD | 39,170.00 USD | 22,020.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,480,000.00 USD | 11,480,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3447` | 2,650,000.00 USD | 2,650,000.00 USD | 265,380.00 USD | 37,630.00 USD | 57,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,930,000.00 USD | 11,930,000.00 USD | 355,170.00 USD | 34,230.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 2,830,000.00 USD | 2,830,000.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,260,000.00 USD | 12,260,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3455` | 2,830,000.00 USD | 2,830,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,400,000.00 USD | 12,400,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3459` | 2,830,000.00 USD | 2,830,000.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,430,000.00 USD | 12,430,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3463` | 2,830,000.00 USD | 2,830,000.00 USD | 186.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,430,000.00 USD | 12,430,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3467` | 2,830,000.00 USD | 2,830,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,430,000.00 USD | 12,430,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 2,830,000.00 USD | 2,830,000.00 USD | 307.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,430,000.00 USD | 12,430,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 2,830,000.00 USD | 2,830,000.00 USD | 663.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,440,000.00 USD | 12,440,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 10,210.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3479` | 2,830,000.00 USD | 2,830,000.00 USD | 81.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,440,000.00 USD | 12,440,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 16,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,440,000.00 USD | 12,440,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,440,000.00 USD | 12,440,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,440,000.00 USD | 12,440,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 194,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3507` | 2,830,000.00 USD | 2,830,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,450,000.00 USD | 12,450,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 2,840,000.00 USD | 2,840,000.00 USD | 1,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,450,000.00 USD | 12,450,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3515` | 2,840,000.00 USD | 2,840,000.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,460,000.00 USD | 12,460,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3519` | 2,840,000.00 USD | 2,840,000.00 USD | 140.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,460,000.00 USD | 12,460,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 2,840,000.00 USD | 2,840,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,460,000.00 USD | 12,460,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3527` | 2,840,000.00 USD | 2,840,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,460,000.00 USD | 12,460,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 2,840,000.00 USD | 2,840,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,460,000.00 USD | 12,460,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3535` | 2,840,000.00 USD | 2,840,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,460,000.00 USD | 12,460,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 194,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,490,000.00 USD | 12,490,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,550,000.00 USD | 12,550,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,590,000.00 USD | 12,590,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,620,000.00 USD | 12,620,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,700,000.00 USD | 12,700,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 2,850,000.00 USD | 2,850,000.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,830,000.00 USD | 12,830,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 2,890,000.00 USD | 2,890,000.00 USD | 24,740.00 USD | 8,270.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,990,000.00 USD | 12,990,000.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3627` | 2,910,000.00 USD | 2,910,000.00 USD | 15,050.00 USD | 5,060.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,120,000.00 USD | 13,120,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 2,930,000.00 USD | 2,930,000.00 USD | 7,150.00 USD | 3,380.00 USD | 4,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,250,000.00 USD | 13,250,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3635` | 2,930,000.00 USD | 2,930,000.00 USD | 147.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,320,000.00 USD | 13,320,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 2,940,000.00 USD | 2,940,000.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,360,000.00 USD | 13,360,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 2,990,000.00 USD | 2,990,000.00 USD | 21,720.00 USD | 7,740.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,480,000.00 USD | 13,480,000.00 USD | 89,610.00 USD | 8,430.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 194,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3646` | 3,090,000.00 USD | 3,090,000.00 USD | 73,690.00 USD | 9,140.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,600,000.00 USD | 13,600,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,670,000.00 USD | 13,670,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 195,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 6,690.00 USD | 201,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3785` | 652.16 USD | 202,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 760,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3815` | 285.74 USD | 760,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 760,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3895` | 6,280.00 USD | 767,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 771,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 772,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 1,490.00 USD | 773,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 892,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 4,630.00 USD | 896,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4255` | 51,950.00 USD | 948,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 72,520.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 203.26 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5375` | 194.58 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5405` | 18,590.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5415` | 702,460.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0685` | 500,240.00 USD | 0.00 USD | 2,740.00 USD | `-79.33%` | `40,000.00` |
| `Live` | `Long` | `0.0695` | 497,500.00 USD | 0.00 USD | 331.31 USD | `-79.03%` | `4,767.00` |
| `Live` | `Long` | `0.0725` | 497,170.00 USD | 0.00 USD | 150.73 USD | `-78.13%` | `2,079.00` |
| `Live` | `Long` | `0.0825` | 497,020.00 USD | 0.00 USD | 1,050.00 USD | `-75.11%` | `12,781.00` |
| `Live` | `Long` | `0.1035` | 495,970.00 USD | 0.00 USD | 4,230.00 USD | `-68.77%` | `40,871.00` |
| `Live` | `Long` | `0.1105` | 491,740.00 USD | 0.00 USD | 4,370.00 USD | `-66.66%` | `39,551.00` |
| `Live` | `Long` | `0.1125` | 487,370.00 USD | 0.00 USD | 803.93 USD | `-66.06%` | `7,146.00` |
| `Live` | `Long` | `0.1135` | 486,560.00 USD | 0.00 USD | 113.50 USD | `-65.75%` | `1,000.00` |
| `Live` | `Long` | `0.1175` | 486,450.00 USD | 0.00 USD | 394.80 USD | `-64.55%` | `3,360.00` |
| `Live` | `Long` | `0.1225` | 486,060.00 USD | 0.00 USD | 643.62 USD | `-63.04%` | `5,254.00` |
| `Live` | `Long` | `0.1235` | 485,410.00 USD | 0.00 USD | 27,020.00 USD | `-62.74%` | `218,745.00` |
| `Live` | `Long` | `0.1375` | 458,400.00 USD | 0.00 USD | 1,560.00 USD | `-58.51%` | `11,352.00` |
| `Live` | `Long` | `0.1405` | 456,840.00 USD | 0.00 USD | 429.65 USD | `-57.61%` | `3,058.00` |
| `Live` | `Long` | `0.1445` | 456,410.00 USD | 0.00 USD | 130.63 USD | `-56.40%` | `904.00` |
| `Live` | `Long` | `0.1485` | 456,280.00 USD | 0.00 USD | 371.55 USD | `-55.19%` | `2,502.00` |
| `Live` | `Long` | `0.1555` | 455,900.00 USD | 0.00 USD | 469.77 USD | `-53.08%` | `3,021.00` |
| `Live` | `Long` | `0.1595` | 455,430.00 USD | 0.00 USD | 390.46 USD | `-51.88%` | `2,448.00` |
| `Live` | `Long` | `0.1615` | 455,040.00 USD | 0.00 USD | 12,400.00 USD | `-51.27%` | `76,797.00` |
| `Live` | `Long` | `0.1705` | 442,640.00 USD | 0.00 USD | 20,360.00 USD | `-48.56%` | `119,400.00` |
| `Live` | `Long` | `0.1725` | 422,280.00 USD | 0.00 USD | 3,930.00 USD | `-47.95%` | `22,767.00` |
| `Live` | `Long` | `0.1735` | 418,360.00 USD | 0.00 USD | 11,160.00 USD | `-47.65%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 407,200.00 USD | 0.00 USD | 471.50 USD | `-47.35%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 406,720.00 USD | 0.00 USD | 1,030.00 USD | `-47.05%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 405,700.00 USD | 0.00 USD | 5,080.00 USD | `-46.75%` | `28,764.00` |
| `Live` | `Long` | `0.1775` | 400,620.00 USD | 0.00 USD | 433.81 USD | `-46.44%` | `2,444.00` |
| `Live` | `Long` | `0.1795` | 400,180.00 USD | 0.00 USD | 209.84 USD | `-45.84%` | `1,169.00` |
| `Live` | `Long` | `0.1895` | 399,970.00 USD | 0.00 USD | 1,150.00 USD | `-42.82%` | `6,059.00` |
| `Live` | `Long` | `0.1975` | 398,830.00 USD | 0.00 USD | 838.39 USD | `-40.41%` | `4,245.00` |
| `Live` | `Long` | `0.2025` | 397,990.00 USD | 0.00 USD | 3,020.00 USD | `-38.90%` | `14,921.00` |
| `Live` | `Long` | `0.2045` | 394,970.00 USD | 0.00 USD | 6,130.00 USD | `-38.30%` | `30,000.00` |
| `Live` | `Long` | `0.2145` | 388,830.00 USD | 0.00 USD | 3,330.00 USD | `-35.28%` | `15,528.00` |
| `Live` | `Long` | `0.2175` | 385,500.00 USD | 0.00 USD | 1,520.00 USD | `-34.38%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 383,980.00 USD | 0.00 USD | 515.17 USD | `-33.77%` | `2,347.00` |
| `Live` | `Long` | `0.2235` | 383,460.00 USD | 0.00 USD | 2,360.00 USD | `-32.56%` | `10,560.00` |
| `Live` | `Long` | `0.2255` | 381,100.00 USD | 0.00 USD | 4,590.00 USD | `-31.96%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 376,510.00 USD | 0.00 USD | 319.59 USD | `-31.66%` | `1,411.00` |
| `Live` | `Long` | `0.2305` | 376,190.00 USD | 0.00 USD | 4,180.00 USD | `-30.45%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 372,010.00 USD | 0.00 USD | 3,010.00 USD | `-30.15%` | `13,018.00` |
| `Live` | `Long` | `0.2325` | 368,990.00 USD | 0.00 USD | 308.30 USD | `-29.85%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 368,690.00 USD | 0.00 USD | 2,370.00 USD | `-29.55%` | `10,154.00` |
| `Live` | `Long` | `0.2345` | 366,320.00 USD | 0.00 USD | 1,000.00 USD | `-29.25%` | `4,283.00` |
| `Live` | `Long` | `0.2355` | 365,310.00 USD | 0.00 USD | 6,140.00 USD | `-28.94%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 359,170.00 USD | 0.00 USD | 344.11 USD | `-28.64%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 358,820.00 USD | 0.00 USD | 1,260.00 USD | `-28.04%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 357,560.00 USD | 0.00 USD | 510.10 USD | `-27.44%` | `2,121.00` |
| `Live` | `Long` | `0.2445` | 357,050.00 USD | 0.00 USD | 889.49 USD | `-26.23%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 356,160.00 USD | 0.00 USD | 466.70 USD | `-25.93%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 355,690.00 USD | 0.00 USD | 276.57 USD | `-25.63%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 355,420.00 USD | 0.00 USD | 2,420.00 USD | `-25.32%` | `9,797.00` |
| `Live` | `Long` | `0.2565` | 352,990.00 USD | 0.00 USD | 1,230.00 USD | `-22.61%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 351,760.00 USD | 0.00 USD | 1,580.00 USD | `-22.00%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 350,190.00 USD | 0.00 USD | 315.81 USD | `-21.70%` | `1,217.00` |
| `Live` | `Long` | `0.2605` | 349,870.00 USD | 0.00 USD | 8,650.00 USD | `-21.40%` | `33,208.00` |
| `Live` | `Long` | `0.2615` | 341,220.00 USD | 0.00 USD | 466.78 USD | `-21.10%` | `1,785.00` |
| `Live` | `Long` | `0.2625` | 340,750.00 USD | 0.00 USD | 22,990.00 USD | `-20.80%` | `87,573.00` |
| `Live` | `Long` | `0.2635` | 317,770.00 USD | 0.00 USD | 405.00 USD | `-20.50%` | `1,537.00` |
| `Live` | `Long` | `0.2655` | 317,360.00 USD | 0.00 USD | 7,520.00 USD | `-19.89%` | `28,325.00` |
| `Live` | `Long` | `0.2665` | 309,840.00 USD | 0.00 USD | 450.92 USD | `-19.59%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 309,390.00 USD | 0.00 USD | 194.47 USD | `-19.29%` | `727.00` |
| `Live` | `Long` | `0.2685` | 309,200.00 USD | 0.00 USD | 322.74 USD | `-18.99%` | `1,202.00` |
| `Live` | `Long` | `0.2725` | 308,870.00 USD | 0.00 USD | 412.84 USD | `-17.78%` | `1,515.00` |
| `Live` | `Long` | `0.2735` | 308,460.00 USD | 0.00 USD | 5,500.00 USD | `-17.48%` | `20,120.00` |
| `Live` | `Long` | `0.2755` | 302,960.00 USD | 0.00 USD | 84,780.00 USD | `-16.88%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 218,180.00 USD | 0.00 USD | 41,220.00 USD | `-16.27%` | `148,541.00` |
| `Live` | `Long` | `0.2785` | 176,960.00 USD | 0.00 USD | 2,130.00 USD | `-15.97%` | `7,634.00` |
| `Live` | `Long` | `0.2795` | 174,830.00 USD | 0.00 USD | 13,720.00 USD | `-15.67%` | `49,085.00` |
| `Live` | `Long` | `0.2805` | 161,110.00 USD | 0.00 USD | 6,280.00 USD | `-15.37%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 154,830.00 USD | 0.00 USD | 1,310.00 USD | `-15.07%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 153,530.00 USD | 0.00 USD | 15,060.00 USD | `-14.76%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 138,470.00 USD | 0.00 USD | 1,430.00 USD | `-14.46%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 137,040.00 USD | 0.00 USD | 482.75 USD | `-13.56%` | `1,685.00` |
| `Live` | `Long` | `0.2875` | 136,550.00 USD | 0.00 USD | 1,600.00 USD | `-13.25%` | `5,572.00` |
| `Live` | `Long` | `0.2915` | 134,950.00 USD | 0.00 USD | 591.45 USD | `-12.05%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 134,360.00 USD | 0.00 USD | 957.64 USD | `-11.75%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 133,400.00 USD | 0.00 USD | 3,760.00 USD | `-11.14%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 129,640.00 USD | 0.00 USD | 125.29 USD | `-10.84%` | `424.00` |
| `Live` | `Long` | `0.2995` | 129,510.00 USD | 0.00 USD | 127.89 USD | `-9.63%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,390.00 USD | 0.00 USD | 7,130.00 USD | `-9.33%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,260.00 USD | 0.00 USD | 10,330.00 USD | `-9.03%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 111,930.00 USD | 0.00 USD | 694.54 USD | `-8.73%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 111,240.00 USD | 0.00 USD | 693.50 USD | `-8.43%` | `2,285.00` |
| `Live` | `Long` | `0.3045` | 110,540.00 USD | 0.00 USD | 5,540.00 USD | `-8.13%` | `18,206.00` |
| `Live` | `Long` | `0.3055` | 105,000.00 USD | 0.00 USD | 5,300.00 USD | `-7.82%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 99,700.00 USD | 0.00 USD | 14,720.00 USD | `-7.52%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 84,980.00 USD | 0.00 USD | 6,670.00 USD | `-6.92%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 78,310.00 USD | 0.00 USD | 304.34 USD | `-6.01%` | `977.00` |
| `Live` | `Long` | `0.3125` | 78,010.00 USD | 0.00 USD | 17,680.00 USD | `-5.71%` | `56,580.00` |
| `Live` | `Long` | `0.3135` | 60,330.00 USD | 0.00 USD | 44,390.00 USD | `-5.41%` | `141,602.00` |
| `Live` | `Long` | `0.3145` | 15,930.00 USD | 0.00 USD | 1,900.00 USD | `-5.11%` | `6,027.00` |
| `Live` | `Long` | `0.3155` | 14,040.00 USD | 0.00 USD | 142.29 USD | `-4.81%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,900.00 USD | 0.00 USD | 1,490.00 USD | `-4.50%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,400.00 USD | 0.00 USD | 938.85 USD | `-4.20%` | `2,957.00` |
| `Live` | `Long` | `0.3185` | 11,460.00 USD | 0.00 USD | 335.70 USD | `-3.90%` | `1,054.00` |
| `Live` | `Long` | `0.3195` | 11,130.00 USD | 0.00 USD | 126.84 USD | `-3.60%` | `397.00` |
| `Live` | `Long` | `0.3235` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-2.39%` | `34,003.00` |
| `Live` | `Short` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | `+3.34%` | `1,333.00` |
| `Live` | `Short` | `0.3435` | 610.44 USD | 153.89 USD | 0.00 USD | `+3.64%` | `448.00` |
| `Live` | `Short` | `0.3445` | 5,900.00 USD | 5,290.00 USD | 0.00 USD | `+3.94%` | `15,355.00` |
| `Live` | `Short` | `0.3455` | 6,390.00 USD | 486.46 USD | 0.00 USD | `+4.25%` | `1,408.00` |
| `Live` | `Short` | `0.3475` | 16,590.00 USD | 10,210.00 USD | 0.00 USD | `+4.85%` | `29,369.00` |
| `Live` | `Short` | `0.3485` | 16,820.00 USD | 223.04 USD | 0.00 USD | `+5.15%` | `640.00` |
| `Live` | `Short` | `0.3505` | 194,350.00 USD | 177,540.00 USD | 0.00 USD | `+5.75%` | `506,529.00` |
| `Live` | `Short` | `0.3535` | 194,580.00 USD | 223.06 USD | 0.00 USD | `+6.66%` | `631.00` |
| `Live` | `Short` | `0.3645` | 194,950.00 USD | 376.53 USD | 0.00 USD | `+9.98%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 195,220.00 USD | 262.78 USD | 0.00 USD | `+10.58%` | `717.00` |
| `Live` | `Short` | `0.3745` | 201,910.00 USD | 6,690.00 USD | 0.00 USD | `+13.00%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 202,560.00 USD | 652.16 USD | 0.00 USD | `+14.20%` | `1,723.00` |
| `Live` | `Short` | `0.3795` | 760,460.00 USD | 557,900.00 USD | 0.00 USD | `+14.50%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 760,740.00 USD | 285.74 USD | 0.00 USD | `+15.11%` | `749.00` |
| `Live` | `Short` | `0.3845` | 760,860.00 USD | 115.35 USD | 0.00 USD | `+16.01%` | `300.00` |
| `Live` | `Short` | `0.3895` | 767,140.00 USD | 6,280.00 USD | 0.00 USD | `+17.52%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 771,910.00 USD | 4,770.00 USD | 0.00 USD | `+17.82%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 772,400.00 USD | 487.42 USD | 0.00 USD | `+18.12%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 773,880.00 USD | 1,490.00 USD | 0.00 USD | `+19.03%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 892,310.00 USD | 118,430.00 USD | 0.00 USD | `+19.33%` | `299,436.00` |
| `Live` | `Short` | `0.4185` | 896,940.00 USD | 4,630.00 USD | 0.00 USD | `+26.27%` | `11,065.00` |
| `Live` | `Short` | `0.4255` | 948,890.00 USD | 51,950.00 USD | 0.00 USD | `+28.38%` | `122,096.00` |
| `Live` | `Short` | `0.4455` | 1,020,000.00 USD | 72,520.00 USD | 0.00 USD | `+34.42%` | `162,775.00` |
| `Live` | `Short` | `0.4475` | 1,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+35.02%` | `2,284.00` |
| `Live` | `Short` | `0.4705` | 1,020,000.00 USD | 203.26 USD | 0.00 USD | `+41.96%` | `432.00` |
| `Live` | `Short` | `0.4905` | 1,020,000.00 USD | 841.21 USD | 0.00 USD | `+48.00%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,030,000.00 USD | 5,130.00 USD | 0.00 USD | `+48.30%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 1,030,000.00 USD | 669.73 USD | 0.00 USD | `+61.27%` | `1,253.00` |
| `Live` | `Short` | `0.5375` | 1,030,000.00 USD | 194.58 USD | 0.00 USD | `+62.18%` | `362.00` |
| `Live` | `Short` | `0.5405` | 1,050,000.00 USD | 18,590.00 USD | 0.00 USD | `+63.08%` | `34,396.00` |
| `Live` | `Short` | `0.5415` | 1,750,000.00 USD | 702,460.00 USD | 0.00 USD | `+63.38%` | `1,297,248.00` |
| `Live` | `Short` | `0.5585` | 1,750,000.00 USD | 742.25 USD | 0.00 USD | `+68.51%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,750,000.00 USD | 140.62 USD | 0.00 USD | `+69.72%` | `250.00` |
| `Live` | `Short` | `0.6145` | 1,790,000.00 USD | 36,870.00 USD | 0.00 USD | `+85.41%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,790,000.00 USD | 275.47 USD | 0.00 USD | `+89.33%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,800,000.00 USD | 7,390.00 USD | 0.00 USD | `+89.63%` | `11,753.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 819,350.00 USD | 0.00 USD | 6,100.00 USD | `-45.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 813,260.00 USD | 0.00 USD | 1,750.00 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 811,500.00 USD | 0.00 USD | 579.72 USD | `-36.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 810,920.00 USD | 0.00 USD | 705.61 USD | `-29.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 810,220.00 USD | 0.00 USD | 1,200.00 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 809,020.00 USD | 0.00 USD | 127.51 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 808,890.00 USD | 0.00 USD | 1,850.00 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 807,030.00 USD | 0.00 USD | 1,920.00 USD | `-22.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 805,110.00 USD | 0.00 USD | 4,200.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 800,910.00 USD | 0.00 USD | 954.98 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 799,950.00 USD | 0.00 USD | 695.50 USD | `-19.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 799,260.00 USD | 0.00 USD | 1,630.00 USD | `-18.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 797,630.00 USD | 0.00 USD | 2,550.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 795,080.00 USD | 0.00 USD | 229.92 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 794,850.00 USD | 0.00 USD | 15,940.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 778,910.00 USD | 0.00 USD | 111.19 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 778,800.00 USD | 0.00 USD | 685.95 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 778,110.00 USD | 0.00 USD | 2,710.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 775,410.00 USD | 0.00 USD | 919.50 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 774,490.00 USD | 0.00 USD | 193.11 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 774,290.00 USD | 0.00 USD | 16,070.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 758,230.00 USD | 0.00 USD | 147.32 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 758,080.00 USD | 0.00 USD | 25,820.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 732,260.00 USD | 0.00 USD | 6,530.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 725,740.00 USD | 0.00 USD | 524,570.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 201,160.00 USD | 0.00 USD | 1,270.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 199,900.00 USD | 0.00 USD | 25,790.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 174,110.00 USD | 0.00 USD | 3,600.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 170,510.00 USD | 0.00 USD | 6,100.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 164,410.00 USD | 0.00 USD | 2,010.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 162,400.00 USD | 0.00 USD | 15,160.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 147,240.00 USD | 0.00 USD | 21,270.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 125,970.00 USD | 0.00 USD | 55,600.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 70,370.00 USD | 0.00 USD | 174.47 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 70,190.00 USD | 0.00 USD | 845.95 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 69,350.00 USD | 0.00 USD | 14,470.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 54,880.00 USD | 0.00 USD | 8,410.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 46,460.00 USD | 0.00 USD | 25,740.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 20,720.00 USD | 0.00 USD | 13,320.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 7,400.00 USD | 0.00 USD | 3,730.00 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 3,670.00 USD | 0.00 USD | 1,830.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 1,840.00 USD | 0.00 USD | 1,840.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3315` | 496.92 USD | 496.92 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 41,090.00 USD | 40,600.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 42,580.00 USD | 1,480.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 43,800.00 USD | 1,220.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 218,660.00 USD | 174,860.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 219,040.00 USD | 379.57 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 219,200.00 USD | 162.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 230,850.00 USD | 11,640.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 230,950.00 USD | 102.87 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 234,040.00 USD | 3,090.00 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 234,940.00 USD | 904.63 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 240,460.00 USD | 5,520.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 248,080.00 USD | 7,610.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 250,960.00 USD | 2,880.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 258,890.00 USD | 7,930.00 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 262,040.00 USD | 3,150.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 263,100.00 USD | 1,060.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 288,850.00 USD | 25,750.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 307,430.00 USD | 18,580.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 320,850.00 USD | 13,420.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 321,620.00 USD | 769.97 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 321,850.00 USD | 226.10 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 326,030.00 USD | 4,180.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 332,010.00 USD | 5,990.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 338,200.00 USD | 6,180.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 338,680.00 USD | 485.59 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 339,070.00 USD | 390.40 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 339,510.00 USD | 433.85 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 339,970.00 USD | 463.99 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 340,130.00 USD | 159.62 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 341,060.00 USD | 926.99 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 343,820.00 USD | 2,760.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 344,090.00 USD | 275.17 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 344,550.00 USD | 463.37 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 344,890.00 USD | 337.12 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 345,010.00 USD | 114.83 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 345,230.00 USD | 224.73 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 345,750.00 USD | 514.64 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 346,100.00 USD | 352.11 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 348,500.00 USD | 2,400.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 349,070.00 USD | 572.00 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 350,270.00 USD | 1,200.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 403,150.00 USD | 52,880.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 405,550.00 USD | 2,400.00 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 406,750.00 USD | 1,200.00 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 407,950.00 USD | 1,200.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 409,150.00 USD | 1,200.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 409,330.00 USD | 186.70 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 447,910.00 USD | 38,580.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 448,080.00 USD | 170.69 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 449,470.00 USD | 1,390.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 460,620.00 USD | 11,150.00 USD | 0.00 USD | `+51.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2979` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 69,830.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 91,050.00 USD | 16,880.00 USD | 28,570.00 USD |
| `7D` | `0.2983` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 117,250.00 USD | 9,990.00 USD | 36,400.00 USD |
| `1D` | `0.2987` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD |
| `7D` | `0.2987` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `7D` | `0.2991` | 12,500,000.00 USD | 0.00 USD | 12,500,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `7D` | `0.3051` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 2,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 1,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3083` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3123` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3131` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,740.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3147` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 101,370.00 USD | 16,380.00 USD | 10,680.00 USD |
| `7D` | `0.3151` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 157,220.00 USD | 37,570.00 USD | 20,330.00 USD |
| `1D` | `0.3159` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3159` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 98,530.00 USD | 30,960.00 USD | 27,920.00 USD |
| `7D` | `0.3163` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3167` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 46,570.00 USD | 11,520.00 USD | 15,080.00 USD |
| `7D` | `0.3167` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3171` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3171` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3175` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3179` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 39,170.00 USD | 22,020.00 USD | 27,720.00 USD |
| `7D` | `0.3179` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD |
| `1D` | `0.3183` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 391,660.00 USD | 47,640.00 USD | 68,030.00 USD |
| `7D` | `0.3183` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 551,920.00 USD | 51,290.00 USD | 82,240.00 USD |
| `1D` | `0.3187` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD |
| `7D` | `0.3187` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `7D` | `0.3207` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `7D` | `0.3211` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3219` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD |
| `1D` | `0.3223` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3223` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3227` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3231` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 161,500.00 USD | 45,670.00 USD | 55,680.00 USD |
| `7D` | `0.3231` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 46,250.00 USD | 20,320.00 USD | 28,270.00 USD |
| `7D` | `0.3235` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3239` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3239` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3243` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3243` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 232,030.00 USD | 77,350.00 USD | 123,620.00 USD |
| `7D` | `0.3247` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD |
| `1D` | `0.3251` | 725,950.00 USD | 0.00 USD | 725,950.00 USD | 601,650.00 USD | 52,790.00 USD | 51,440.00 USD |
| `7D` | `0.3251` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3255` | 20,070.00 USD | 0.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3312` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3313` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3351` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD |
| `1D` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3355` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 0.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3359` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3363` | 480,390.00 USD | 480,390.00 USD | 0.00 USD | 161,500.00 USD | 45,670.00 USD | 55,680.00 USD |
| `7D` | `0.3363` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 575,220.00 USD | 575,220.00 USD | 0.00 USD | 46,250.00 USD | 20,320.00 USD | 28,270.00 USD |
| `7D` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3371` | 604,850.00 USD | 604,850.00 USD | 0.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3371` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3375` | 725,790.00 USD | 725,790.00 USD | 0.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3375` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 232,030.00 USD | 77,350.00 USD | 123,620.00 USD |
| `7D` | `0.3379` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD |
| `1D` | `0.3383` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 601,650.00 USD | 52,790.00 USD | 51,440.00 USD |
| `7D` | `0.3383` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3387` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3403` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `7D` | `0.3411` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `7D` | `0.3415` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 26,270.00 USD |
| `7D` | `0.3419` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3423` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3423` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 98,530.00 USD | 30,960.00 USD | 27,920.00 USD |
| `7D` | `0.3427` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3431` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 46,570.00 USD | 11,520.00 USD | 15,080.00 USD |
| `7D` | `0.3431` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3435` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3435` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3439` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3443` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 39,170.00 USD | 22,020.00 USD | 27,720.00 USD |
| `7D` | `0.3443` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD |
| `1D` | `0.3447` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 265,380.00 USD | 37,630.00 USD | 57,890.00 USD |
| `7D` | `0.3447` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 355,170.00 USD | 34,230.00 USD | 68,590.00 USD |
| `1D` | `0.3451` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD |
| `7D` | `0.3451` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3455` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3455` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3459` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 186.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3467` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3471` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 307.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3471` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 663.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3475` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 81.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 1,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3515` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 140.03 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3527` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3535` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `7D` | `0.3615` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD |
| `7D` | `0.3619` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3623` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 24,740.00 USD | 8,270.00 USD | 8,880.00 USD |
| `7D` | `0.3623` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD |
| `1D` | `0.3627` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 15,050.00 USD | 5,060.00 USD | 6,220.00 USD |
| `7D` | `0.3627` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 7,150.00 USD | 3,380.00 USD | 4,520.00 USD |
| `7D` | `0.3631` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3635` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 147.65 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3635` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3639` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD |
| `7D` | `0.3639` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 21,720.00 USD | 7,740.00 USD | 16,150.00 USD |
| `7D` | `0.3643` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 89,610.00 USD | 8,430.00 USD | 22,010.00 USD |
| `1D` | `0.3646` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 73,690.00 USD | 9,140.00 USD | 12,420.00 USD |
| `7D` | `0.3647` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `7D` | `0.3651` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `298.09M` | Total OI Tokens: `899,912,290.3 TRX`
  * 1h OI Change: `-0.03%` | 4h OI Change: `-0.60%` | 24h OI Change: `+1.54%`
  * Exchange Breakdown: Binance=`90.45M` | Bybit=`49.75M` | OKX=`13.77M` | Hyperliquid=`11.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.30K` | Last 24h: `9.21K` | Last 3d: `-51.81K` | Last 7d: `-271.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0083%` | **USDT OKX** | `-0.0028%` |
| **USDT Bybit** | `0.0020%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0083%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0013%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `46.34%` | `53.66%` | `0.86` | 10,430,000.00 USD |
| `15M` | `Binance` | `50.99%` | `49.01%` | `1.04` | 3,730,000.00 USD |
| `15M` | `OKX` | `47.36%` | `52.64%` | `0.90` | 777,110.00 USD |
| `15M` | `Bybit` | `41.89%` | `58.11%` | `0.72` | 851,320.00 USD |
| `15M` | `KuCoin` | `34.09%` | `65.91%` | `0.52` | 63,770.00 USD |
| `15M` | `Gate` | `59.63%` | `40.37%` | `1.48` | 827,780.00 USD |
| `15M` | `Bitget` | `54.55%` | `45.45%` | `1.20` | 489,470.00 USD |
| `15M` | `BingX` | `53.64%` | `46.36%` | `1.16` | 187,330.00 USD |
| `15M` | `MEXC` | `34.83%` | `65.17%` | `0.53` | 960,710.00 USD |
| `15M` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 288,020.00 USD |
| `15M` | `Hyperliquid` | `23.86%` | `76.14%` | `0.31` | 245,590.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.87%` | `58.13%` | `0.72` | 1,790,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `10.05%` | `89.95%` | `0.11` | 167,230.00 USD |
| `15M` | `HTX` | `61.51%` | `38.49%` | `1.60` | 15,020.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `42.81%` | `57.19%` | `0.75` | 49,870.00 USD |
| `15M` | `Aster` | `44.04%` | `55.96%` | `0.79` | 141.64 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 763.16 USD |
| `15M` | `Whale Positions` | `50.99%` | `49.01%` | `1.04` | 3,730,000.00 USD |
| `15M` | `Global Accounts` | `46.34%` | `53.66%` | `0.86` | 10,430,000.00 USD |
| `1H` | `TRX` | `48.89%` | `51.11%` | `0.96` | 2,840,000.00 USD |
| `1H` | `Binance` | `59.67%` | `40.33%` | `1.48` | 1,080,000.00 USD |
| `1H` | `OKX` | `49.83%` | `50.17%` | `0.99` | 161,390.00 USD |
| `1H` | `Bybit` | `73.52%` | `26.48%` | `2.78` | 144,950.00 USD |
| `1H` | `KuCoin` | `49.59%` | `50.41%` | `0.98` | 60,640.00 USD |
| `1H` | `Gate` | `48.27%` | `51.73%` | `0.93` | 64,540.00 USD |
| `1H` | `Bitget` | `54.82%` | `45.18%` | `1.21` | 55,780.00 USD |
| `1H` | `BingX` | `51.5%` | `48.5%` | `1.06` | 127,640.00 USD |
| `1H` | `MEXC` | `46.72%` | `53.28%` | `0.88` | 16,610.00 USD |
| `1H` | `Bitunix` | `56.44%` | `43.56%` | `1.30` | 34,230.00 USD |
| `1H` | `Hyperliquid` | `44.92%` | `55.08%` | `0.82` | 63,340.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.07%` | `49.93%` | `1.00` | 535,590.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.25%` | `91.75%` | `0.09` | 427,650.00 USD |
| `1H` | `HTX` | `59.83%` | `40.17%` | `1.49` | 46,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `74.63%` | `25.37%` | `2.94` | 9,420.00 USD |
| `1H` | `Aster` | `21.48%` | `78.52%` | `0.27` | 2,230.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.52%` | `52.48%` | `0.91` | 2,120.00 USD |
| `1H` | `Whale Positions` | `59.67%` | `40.33%` | `1.48` | 1,080,000.00 USD |
| `1H` | `Global Accounts` | `48.89%` | `51.11%` | `0.96` | 2,840,000.00 USD |
| `4H` | `TRX` | `45.19%` | `54.81%` | `0.82` | 12,210,000.00 USD |
| `4H` | `Binance` | `52.04%` | `47.96%` | `1.09` | 4,400,000.00 USD |
| `4H` | `OKX` | `46.56%` | `53.44%` | `0.87` | 785,140.00 USD |
| `4H` | `Bybit` | `51.18%` | `48.82%` | `1.05` | 627,040.00 USD |
| `4H` | `KuCoin` | `48.97%` | `51.03%` | `0.96` | 270,220.00 USD |
| `4H` | `Gate` | `60.61%` | `39.39%` | `1.54` | 304,620.00 USD |
| `4H` | `Bitget` | `57.41%` | `42.59%` | `1.35` | 179,830.00 USD |
| `4H` | `BingX` | `25.03%` | `74.97%` | `0.33` | 1,080,000.00 USD |
| `4H` | `MEXC` | `60.68%` | `39.32%` | `1.54` | 147,200.00 USD |
| `4H` | `Bitunix` | `49.38%` | `50.62%` | `0.98` | 135,090.00 USD |
| `4H` | `Hyperliquid` | `84.32%` | `15.68%` | `5.38` | 423,470.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.09%` | `49.91%` | `1.00` | 1,930,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.63%` | `90.37%` | `0.11` | 1,520,000.00 USD |
| `4H` | `HTX` | `53.57%` | `46.43%` | `1.15` | 197,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `70.8%` | `29.2%` | `2.42` | 134,890.00 USD |
| `4H` | `Aster` | `22.6%` | `77.4%` | `0.29` | 8,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `28.56%` | `71.44%` | `0.40` | 63,880.00 USD |
| `4H` | `Whale Positions` | `52.04%` | `47.96%` | `1.09` | 4,400,000.00 USD |
| `4H` | `Global Accounts` | `45.19%` | `54.81%` | `0.82` | 12,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3313` | `0.3312` | 179,833.13 USD | 50,346.37 USD | 129,486.77 USD | -79,140.40 USD | `-44.01%` | `3B / 3S` |
| `5:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `0.3311` | 145,155.84 USD | 46,671.46 USD | 98,484.38 USD | -51,812.92 USD | `-35.69%` | `2B / 3S` |
| `0:00 UTC` | `0.3312` | `0.3311` | `0.3312` | `0.3312` | `0.3310` | 301,237.68 USD | 114,043.04 USD | 187,194.64 USD | -73,151.60 USD | `-24.28%` | `3B / 9S` |
| `5:00 UTC` | `0.3312` | `0.3311` | `0.3312` | `0.3312` | `0.3311` | 209,738.14 USD | 96,085.33 USD | 113,652.81 USD | -17,567.48 USD | `-8.38%` | `4B / 10S` |
| `0:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3313` | `0.3311` | 324,753.86 USD | 187,135.24 USD | 137,618.62 USD | 49,516.62 USD | `+15.25%` | `5B / 7S` |
| `5:00 UTC` | `0.3313` | `0.3312` | `0.3313` | `0.3313` | `0.3311` | 257,613.17 USD | 129,803.39 USD | 127,809.78 USD | 1,993.62 USD | `+0.77%` | `7B / 11S` |
| `0:00 UTC` | `0.3311` | `0.3311` | `0.3311` | `0.3312` | `0.3311` | 152,723.77 USD | 63,964.61 USD | 88,759.15 USD | -24,794.54 USD | `-16.23%` | `3B / 5S` |
| `5:00 UTC` | `0.3312` | `0.3313` | `0.3312` | `0.3314` | `0.3312` | 241,719.94 USD | 169,546.92 USD | 72,173.03 USD | 97,373.89 USD | `+40.28%` | `9B / 3S` |
| `0:00 UTC` | `0.3314` | `0.3313` | `0.3314` | `0.3315` | `0.3312` | 417,486.18 USD | 289,418.38 USD | 128,067.80 USD | 161,350.58 USD | `+38.65%` | `12B / 5S` |
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 57,224.66 USD | 12,773.74 USD | 44,450.92 USD | -31,677.18 USD | `-55.36%` | `2B / 7S` |

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
| `5m` | 29,880.00 USD | 34,460.00 USD | **`ACCUMULATION`** |
| `15m` | 95,130.00 USD | 209,150.00 USD | **`ACCUMULATION`** |
| `30m` | 179,930.00 USD | 386,430.00 USD | **`ACCUMULATION`** |
| `1h` | 63,370.00 USD | 328,420.00 USD | **`ACCUMULATION`** |
| `2h` | 104,450.00 USD | 246,690.00 USD | **`ACCUMULATION`** |
| `4h` | 366,460.00 USD | 173,290.00 USD | **`ACCUMULATION`** |
| `6h` | 89,130.00 USD | 378,000.00 USD | **`ACCUMULATION`** |
| `8h` | 320,350.00 USD | 471,730.00 USD | **`ACCUMULATION`** |
| `12h` | 541,900.00 USD | 948,630.00 USD | **`ACCUMULATION`** |
| `24h` | 4,030,000.00 USD | 3,320,000.00 USD | **`ACCUMULATION`** |
| `1w` | -4,750,000.00 USD | 2,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,040,000.00 USD | 3,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+29.88K` | 15m=`+95.13K` | 1h=`+63.37K` | 24h=`+4.03M`
* Futures Capital Netflows: 5m=`+34.46K` | 15m=`+209.15K` | 1h=`+328.42K` | 24h=`+3.32M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3294` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3272` (Risk Distance: `0.0024` pts)
  * +2.5R Take Profit: `0.3354`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3334` (Risk Distance: `0.0024` pts)
  * +2.5R Take Profit: `0.3252`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3340`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
