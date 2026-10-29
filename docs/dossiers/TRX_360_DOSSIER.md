# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3275` | **Live Ask Quote**: `0.3303` | **Mid Price**: `0.3289`
- **Spread Points**: `28.00` | **Spread BPS**: `85.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3302` | VWAP Z-Score: `-1.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000473` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `25.13` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3324` | Lower -3.00σ Band: `0.3280`
  * Upper +2.51σ Band: `0.3321` | Lower -2.51σ Band: `0.3284`
  * Upper +2.01σ Band: `0.3317` | Lower -2.01σ Band: `0.3288`
  * Upper +2.00σ Band: `0.3317` | Lower -2.00σ Band: `0.3288`
  * Upper +1.28σ Band: `0.3312` | Lower -1.28σ Band: `0.3293`
  * Upper +1.00σ Band: `0.3310` | Lower -1.00σ Band: `0.3295`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3303` | EMA-20=`0.3305` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3306` (Slope: `+0.0000`) | EMA-100=`0.3304`
  * Institutional Anchors: EMA-144=`0.3302` | EMA-200=`0.3300` (Slope: `+0.0209`) | EMA-233=`0.3299`
- **Range Boundaries**: 24H High=`0.3313` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `-0.68%`)
  * Point of Control (POC) = `0.3307` (Distance: `-0.54%`)
  * Value Area Low (VAL) = `0.3293` (Distance: `-0.13%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3314` | POC=`0.3309` | VAL=`0.3304`
  * Prior Day Extremes: PDH=`0.3319` | PDL=`0.3288` | PDC=`0.3289`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3313` | Weekly POC=`0.3307` | Weekly VAL=`0.3290`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3306` | Low=`0.3285`
  * London Session (08:00-16:00 UTC): High=`0.3311` | Low=`0.3303`
  * New York Session (13:00-21:00 UTC): High=`0.3313` | Low=`0.3301`
  * Initial Balance (First Hour): IB High=`0.3311` | IB Low=`0.3303`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3276` - `0.3302`
  * Optimal Trade Entry (OTE 0.705): `0.3296`
  * Structural Invalidation Anchor (0.786): `0.3315`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3306` | `0.3308` | `0.3285` | `0.3295` | `5,608,819` | 1,848,764.49 USD | -542,293.32 USD | `-29.33%` | 461,119.81 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3295` | `0.3327` | `0.3282` | `0.3308` | `14,512,420` | 4,801,653.77 USD | 1,036,168.74 USD | `+21.58%` | 1,497,288.55 USD | `+2.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3308` | `0.3319` | `0.3307` | `0.3318` | `544,984` | 180,550.12 USD | 68,323.33 USD | `+37.84%` | 1,565,611.88 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3312` | `0.3313` | `0.3295` | `0.3300` | `9,356,663` | 3,091,479.93 USD | -1,727,517.83 USD | `-55.88%` | 716,523.69 USD | `-4.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3300` | `0.3363` | `0.3285` | `0.3295` | `32,071,134` | 10,644,567.03 USD | -267,046.75 USD | `-2.51%` | 449,476.93 USD | `-0.46` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3295` | `0.3327` | `0.3282` | `0.3318` | `15,025,241` | 4,971,531.20 USD | 1,110,825.01 USD | `+22.34%` | 1,560,301.95 USD | `+2.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.3313` | `0.3316` | `0.3312` | `0.3315` | `2,121,059` | 702,996.80 USD | 82,277.88 USD | `+11.70%` | 2,342,614.46 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3315` | `0.3363` | `0.3285` | `0.3295` | `44,626,076` | 14,795,667.86 USD | -1,967,377.84 USD | `-13.30%` | 375,236.63 USD | `-3.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3295` | `0.3327` | `0.3282` | `0.3318` | `14,963,797` | 4,951,142.15 USD | 1,108,971.94 USD | `+22.40%` | 1,484,208.57 USD | `+1.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3363` | `0.3282` | `0.3318` | `59,651,317` | 19,767,199.06 USD | -856,552.82 USD | `-4.33%` | 988,672.90 USD | `-2.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,247,572.49 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 1,263,826.68 USD | `-1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3363` | `0.3282` | `0.3318` | `59,651,317` | 19,767,199.06 USD | -856,552.82 USD | `-4.33%` | 988,672.90 USD | `-2.02` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3289`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `827` | `0xecb6...2b00` | `LONG` | 2,761,057.84 USD | `8,275,560.00` | `0.3311` | `0.3352` | `0.000000` | 20,983.57 USD | `+0.76%` | `10X Cross` |
| `1609` | `0xeadc...9d55` | `LONG` | 1,324,116.00 USD | `4,000,000.00` | `0.3421` | `0.3352` | `0.000000` | -44,362.09 USD | `-3.35%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,473.44 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3316 USD [API] | `2026-10-28 08:12:23` |
| `ANNOUNCEMENT` | `INFO` | `0.3324` | 11,625.32 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 11.63K USD at 0.3324 USD [API] | `2026-10-28 08:23:21` |
| `ANNOUNCEMENT` | `INFO` | `0.3324` | 9,374.78 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 9.37K USD at 0.3324 USD [API] | `2026-10-28 08:42:41` |
| `ANNOUNCEMENT` | `INFO` | `0.3322` | 8,118.55 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 8.12K USD at 0.3322 USD [API] | `2026-10-28 08:42:41` |
| `ANNOUNCEMENT` | `INFO` | `0.3320` | 3,885.51 USD | `-` | `NEWS_INTEL` | `-` | #TRX Liquidated Short: 3.89K USD at 0.3320 USD [API] | `2026-10-18 19:33:08` |
| `ANNOUNCEMENT` | `INFO` | `0.3322` | 4,999.85 USD | `-` | `NEWS_INTEL` | `-` | #TRX Liquidated Short: 5.00K USD at 0.3322 USD [API] | `2026-10-18 19:33:08` |
| `ANNOUNCEMENT` | `INFO` | `0.3320` | 6,300.46 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.30K USD at 0.3320 USD [API] | `2026-10-28 09:20:11` |
| `ANNOUNCEMENT` | `INFO` | `0.3320` | 8,114.15 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.11K USD at 0.3320 USD [API] | `2026-10-28 09:40:39` |
| `ANNOUNCEMENT` | `INFO` | `0.3321` | 6,466.04 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3321 USD [API] | `2026-10-28 09:46:58` |
| `ANNOUNCEMENT` | `INFO` | `0.3321` | 6,466.07 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3321 USD [API] | `2026-10-28 09:55:05` |
| `ANNOUNCEMENT` | `INFO` | `0.3323` | 5,904.31 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.90K USD at 0.3323 USD [API] | `2026-10-28 11:34:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3380` (Vol: 430,600.00 USD, Dist: `+2.04%`) | Long MP=`0.3248` (Vol: 480,000.00 USD, Dist: `--1.96%`)
  * 48H Horizon: Short MP=`0.3381` (Vol: 573,800.00 USD, Dist: `+2.05%`) | Long MP=`0.3250` (Vol: 651,100.00 USD, Dist: `--1.90%`)
  * 3D Horizon: Short MP=`0.3381` (Vol: 529,100.00 USD, Dist: `+2.04%`) | Long MP=`0.3250` (Vol: 624,900.00 USD, Dist: `--1.91%`)
  * 7D Horizon: Short MP=`0.3381` (Vol: 651,800.00 USD, Dist: `+2.04%`) | Long MP=`0.3250` (Vol: 685,700.00 USD, Dist: `--1.91%`)
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
| `1D` | `Long Liquidation` | `0.2957` | 3,740,000.00 USD | 3,740,000.00 USD | 321.75 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2961` | 3,740,000.00 USD | 3,740,000.00 USD | 285.15 USD | 654.45 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2965` | 3,730,000.00 USD | 3,730,000.00 USD | 18,360.00 USD | 7,390.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2969` | 3,690,000.00 USD | 3,690,000.00 USD | 19,670.00 USD | 3,440.00 USD | 12,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2973` | 3,660,000.00 USD | 3,660,000.00 USD | 195.85 USD | 5,040.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2977` | 3,650,000.00 USD | 3,650,000.00 USD | 9,210.00 USD | 4,260.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,830,000.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 3,630,000.00 USD | 3,630,000.00 USD | 21,740.00 USD | 8,970.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,740,000.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2985` | 3,580,000.00 USD | 3,580,000.00 USD | 133,260.00 USD | 15,760.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,580,000.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2989` | 3,410,000.00 USD | 3,410,000.00 USD | 9,970.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,480,000.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2993` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3005` | 3,390,000.00 USD | 3,390,000.00 USD | 4,620.00 USD | 1,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3009` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 111,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 693.50 USD | 111,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,540.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,440,000.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,440,000.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,440,000.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,440,000.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3069` | 3,370,000.00 USD | 3,370,000.00 USD | 864.69 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,440,000.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 3,370,000.00 USD | 3,370,000.00 USD | 1,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,430,000.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3077` | 3,370,000.00 USD | 3,370,000.00 USD | 95.35 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,430,000.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 3,370,000.00 USD | 3,370,000.00 USD | 58.54 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,420,000.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 3,370,000.00 USD | 3,370,000.00 USD | 340.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 84,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,420,000.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3089` | 3,370,000.00 USD | 3,370,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,420,000.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 3,360,000.00 USD | 3,360,000.00 USD | 161.62 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,420,000.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,420,000.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 304.34 USD | 78,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,420,000.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,410,000.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3125` | 3,360,000.00 USD | 3,360,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,680.00 USD | 78,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,410,000.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3129` | 3,360,000.00 USD | 3,360,000.00 USD | 1,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,400,000.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 3,360,000.00 USD | 3,360,000.00 USD | 127.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,390,000.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 3,360,000.00 USD | 3,360,000.00 USD | 78.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,390,000.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 3,360,000.00 USD | 3,360,000.00 USD | 394.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,390,000.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 3,360,000.00 USD | 3,360,000.00 USD | 911.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 1,900.00 USD | 15,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,160,000.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3149` | 3,360,000.00 USD | 3,360,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,030,000.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,820,000.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,610,000.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 3,350,000.00 USD | 3,350,000.00 USD | 37,390.00 USD | 18,800.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,070,000.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3165` | 3,270,000.00 USD | 3,270,000.00 USD | 69,780.00 USD | 12,610.00 USD | 28,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3169` | 3,160,000.00 USD | 3,160,000.00 USD | 23,130.00 USD | 15,490.00 USD | 26,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,090,000.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 3,100,000.00 USD | 3,100,000.00 USD | 7,510.00 USD | 11,000.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,610,000.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3177` | 3,070,000.00 USD | 3,070,000.00 USD | 43,360.00 USD | 11,070.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,530,000.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 3,000,000.00 USD | 3,000,000.00 USD | 316,810.00 USD | 59,050.00 USD | 89,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,210,000.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3185` | 2,530,000.00 USD | 2,530,000.00 USD | 179,880.00 USD | 16,360.00 USD | 12,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,500,000.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3189` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,340,000.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 463.59 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3205` | 2,300,000.00 USD | 2,300,000.00 USD | 11,550.00 USD | 4,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,260,000.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3209` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,050,000.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,550,000.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,260,000.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,840,000.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3225` | 2,240,000.00 USD | 2,240,000.00 USD | 11,490.00 USD | 11,200.00 USD | 54,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 2,160,000.00 USD | 2,160,000.00 USD | 160,620.00 USD | 42,360.00 USD | 35,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,150,000.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 1,920,000.00 USD | 1,920,000.00 USD | 80,770.00 USD | 17,470.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,080,000.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 1,770,000.00 USD | 1,770,000.00 USD | 15,410.00 USD | 34,210.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,200,000.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 1,680,000.00 USD | 1,680,000.00 USD | 32,780.00 USD | 17,820.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,610,000.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3245` | 1,620,000.00 USD | 1,620,000.00 USD | 87,440.00 USD | 47,250.00 USD | 66,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,270,000.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 1,410,000.00 USD | 1,410,000.00 USD | 837,620.00 USD | 100,790.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,380,000.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 315,160.00 USD | 315,160.00 USD | 129,570.00 USD | 17,670.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3257` | 162,750.00 USD | 162,750.00 USD | 0.00 USD | 0.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3261` | 118,790.00 USD | 118,790.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3269` | 112,550.00 USD | 112,550.00 USD | 23,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3273` | 89,450.00 USD | 89,450.00 USD | 0.00 USD | 9,000.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3365` | 46,750.00 USD | 46,750.00 USD | 38,540.00 USD | 8,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3369` | 134,960.00 USD | 134,960.00 USD | 15,410.00 USD | 34,210.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3373` | 202,600.00 USD | 202,600.00 USD | 32,780.00 USD | 17,820.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3377` | 403,850.00 USD | 403,850.00 USD | 87,440.00 USD | 47,250.00 USD | 66,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3381` | 1,500,000.00 USD | 1,500,000.00 USD | 837,620.00 USD | 100,790.00 USD | 160,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3385` | 1,650,000.00 USD | 1,650,000.00 USD | 129,570.00 USD | 17,670.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3389` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3393` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3405` | 1,740,000.00 USD | 1,740,000.00 USD | 23,100.00 USD | 9,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3409` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3421` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3425` | 1,900,000.00 USD | 1,900,000.00 USD | 37,390.00 USD | 18,800.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3429` | 2,020,000.00 USD | 2,020,000.00 USD | 69,780.00 USD | 12,610.00 USD | 28,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 2,080,000.00 USD | 2,080,000.00 USD | 23,130.00 USD | 15,490.00 USD | 26,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3437` | 2,110,000.00 USD | 2,110,000.00 USD | 7,510.00 USD | 11,000.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 2,180,000.00 USD | 2,180,000.00 USD | 43,360.00 USD | 11,070.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 2,310,000.00 USD | 2,310,000.00 USD | 53,060.00 USD | 27,950.00 USD | 42,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3449` | 2,810,000.00 USD | 2,810,000.00 USD | 403,110.00 USD | 41,550.00 USD | 59,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 2,880,000.00 USD | 2,880,000.00 USD | 41,660.00 USD | 5,910.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3457` | 2,880,000.00 USD | 2,880,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 2,880,000.00 USD | 2,880,000.00 USD | 252.10 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3465` | 2,880,000.00 USD | 2,880,000.00 USD | 78.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 2,900,000.00 USD | 2,900,000.00 USD | 11,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 2,900,000.00 USD | 2,900,000.00 USD | 563.70 USD | 4,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 10,210.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3477` | 2,940,000.00 USD | 2,940,000.00 USD | 428.70 USD | 0.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 2,940,000.00 USD | 2,940,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 16,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 194,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3509` | 2,940,000.00 USD | 2,940,000.00 USD | 864.69 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 2,940,000.00 USD | 2,940,000.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 2,940,000.00 USD | 2,940,000.00 USD | 188.98 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 2,940,000.00 USD | 2,940,000.00 USD | 58.54 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3525` | 2,940,000.00 USD | 2,940,000.00 USD | 235.08 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 2,940,000.00 USD | 2,940,000.00 USD | 105.01 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 2,950,000.00 USD | 2,950,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 194,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3537` | 2,950,000.00 USD | 2,950,000.00 USD | 161.62 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3605` | 20,520.00 USD | 215,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3617` | 2,950,000.00 USD | 2,950,000.00 USD | 469.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 2,960,000.00 USD | 2,960,000.00 USD | 4,490.00 USD | 2,520.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 3,000,000.00 USD | 3,000,000.00 USD | 21,350.00 USD | 6,030.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 3,020,000.00 USD | 3,020,000.00 USD | 12,330.00 USD | 2,930.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 3,030,000.00 USD | 3,030,000.00 USD | 195.85 USD | 5,040.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 3,040,000.00 USD | 3,040,000.00 USD | 2,220.00 USD | 2,110.00 USD | 2,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 3,070,000.00 USD | 3,070,000.00 USD | 16,030.00 USD | 5,840.00 USD | 7,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3645` | 3,210,000.00 USD | 3,210,000.00 USD | 100,070.00 USD | 15,170.00 USD | 29,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 215,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 3,270,000.00 USD | 3,270,000.00 USD | 45,890.00 USD | 5,870.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3653` | 3,290,000.00 USD | 3,290,000.00 USD | 9,970.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 215,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3669` | 3,300,000.00 USD | 3,300,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 1,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3677` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 16,090.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0685` | 512,820.00 USD | 0.00 USD | 2,740.00 USD | `-79.22%` | `40,000.00` |
| `Live` | `Long` | `0.0765` | 510,080.00 USD | 0.00 USD | 977.75 USD | `-76.79%` | `12,781.00` |
| `Live` | `Long` | `0.0815` | 509,110.00 USD | 0.00 USD | 3,330.00 USD | `-75.28%` | `40,871.00` |
| `Live` | `Long` | `0.0825` | 505,780.00 USD | 0.00 USD | 171.52 USD | `-74.97%` | `2,079.00` |
| `Live` | `Long` | `0.1095` | 505,600.00 USD | 0.00 USD | 575.31 USD | `-66.78%` | `5,254.00` |
| `Live` | `Long` | `0.1145` | 505,030.00 USD | 0.00 USD | 546.05 USD | `-65.27%` | `4,769.00` |
| `Live` | `Long` | `0.1175` | 504,480.00 USD | 0.00 USD | 394.80 USD | `-64.36%` | `3,360.00` |
| `Live` | `Long` | `0.1195` | 504,090.00 USD | 0.00 USD | 1,360.00 USD | `-63.75%` | `11,352.00` |
| `Live` | `Long` | `0.1355` | 502,730.00 USD | 0.00 USD | 10,410.00 USD | `-58.89%` | `76,797.00` |
| `Live` | `Long` | `0.1395` | 492,330.00 USD | 0.00 USD | 5,520.00 USD | `-57.68%` | `39,551.00` |
| `Live` | `Long` | `0.1405` | 486,810.00 USD | 0.00 USD | 429.65 USD | `-57.38%` | `3,058.00` |
| `Live` | `Long` | `0.1455` | 486,380.00 USD | 0.00 USD | 1,020.00 USD | `-55.86%` | `7,033.00` |
| `Live` | `Long` | `0.1595` | 485,360.00 USD | 0.00 USD | 390.46 USD | `-51.61%` | `2,448.00` |
| `Live` | `Long` | `0.1685` | 484,970.00 USD | 0.00 USD | 505.50 USD | `-48.88%` | `3,000.00` |
| `Live` | `Long` | `0.1705` | 484,460.00 USD | 0.00 USD | 20,360.00 USD | `-48.28%` | `119,400.00` |
| `Live` | `Long` | `0.1735` | 464,100.00 USD | 0.00 USD | 11,160.00 USD | `-47.37%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 452,940.00 USD | 0.00 USD | 954.34 USD | `-47.06%` | `5,469.00` |
| `Live` | `Long` | `0.1755` | 451,990.00 USD | 0.00 USD | 1,030.00 USD | `-46.76%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 450,960.00 USD | 0.00 USD | 42,810.00 USD | `-46.46%` | `242,522.00` |
| `Live` | `Long` | `0.1775` | 408,150.00 USD | 0.00 USD | 433.81 USD | `-46.15%` | `2,444.00` |
| `Live` | `Long` | `0.1785` | 407,720.00 USD | 0.00 USD | 890.18 USD | `-45.85%` | `4,987.00` |
| `Live` | `Long` | `0.1795` | 406,830.00 USD | 0.00 USD | 209.84 USD | `-45.55%` | `1,169.00` |
| `Live` | `Long` | `0.1895` | 406,620.00 USD | 0.00 USD | 1,150.00 USD | `-42.51%` | `6,059.00` |
| `Live` | `Long` | `0.1935` | 405,470.00 USD | 0.00 USD | 4,140.00 USD | `-41.30%` | `21,411.00` |
| `Live` | `Long` | `0.1995` | 401,330.00 USD | 0.00 USD | 638.40 USD | `-39.48%` | `3,200.00` |
| `Live` | `Long` | `0.2045` | 400,690.00 USD | 0.00 USD | 6,130.00 USD | `-37.96%` | `30,000.00` |
| `Live` | `Long` | `0.2105` | 394,550.00 USD | 0.00 USD | 526.67 USD | `-36.14%` | `2,502.00` |
| `Live` | `Long` | `0.2145` | 394,030.00 USD | 0.00 USD | 3,330.00 USD | `-34.93%` | `15,528.00` |
| `Live` | `Long` | `0.2165` | 390,700.00 USD | 0.00 USD | 195.72 USD | `-34.32%` | `904.00` |
| `Live` | `Long` | `0.2185` | 390,500.00 USD | 0.00 USD | 1,530.00 USD | `-33.72%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 388,970.00 USD | 0.00 USD | 515.17 USD | `-33.41%` | `2,347.00` |
| `Live` | `Long` | `0.2225` | 388,460.00 USD | 0.00 USD | 2,580.00 USD | `-32.50%` | `11,605.00` |
| `Live` | `Long` | `0.2245` | 385,870.00 USD | 0.00 USD | 3,350.00 USD | `-31.90%` | `14,921.00` |
| `Live` | `Long` | `0.2255` | 382,520.00 USD | 0.00 USD | 4,590.00 USD | `-31.59%` | `20,360.00` |
| `Live` | `Long` | `0.2305` | 377,930.00 USD | 0.00 USD | 4,180.00 USD | `-30.08%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 373,750.00 USD | 0.00 USD | 2,730.00 USD | `-29.77%` | `11,792.00` |
| `Live` | `Long` | `0.2325` | 371,020.00 USD | 0.00 USD | 308.30 USD | `-29.47%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 370,710.00 USD | 0.00 USD | 2,370.00 USD | `-29.17%` | `10,154.00` |
| `Live` | `Long` | `0.2345` | 368,340.00 USD | 0.00 USD | 729.53 USD | `-28.86%` | `3,111.00` |
| `Live` | `Long` | `0.2355` | 367,610.00 USD | 0.00 USD | 6,140.00 USD | `-28.56%` | `26,082.00` |
| `Live` | `Long` | `0.2375` | 361,470.00 USD | 0.00 USD | 345.56 USD | `-27.95%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 361,120.00 USD | 0.00 USD | 1,260.00 USD | `-27.65%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 359,860.00 USD | 0.00 USD | 181.58 USD | `-27.04%` | `755.00` |
| `Live` | `Long` | `0.2445` | 359,680.00 USD | 0.00 USD | 889.49 USD | `-25.83%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 358,790.00 USD | 0.00 USD | 466.70 USD | `-25.52%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 358,320.00 USD | 0.00 USD | 276.57 USD | `-25.22%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 358,050.00 USD | 0.00 USD | 2,420.00 USD | `-24.92%` | `9,797.00` |
| `Live` | `Long` | `0.2505` | 355,620.00 USD | 0.00 USD | 200.40 USD | `-24.01%` | `800.00` |
| `Live` | `Long` | `0.2565` | 355,420.00 USD | 0.00 USD | 1,230.00 USD | `-22.19%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 354,190.00 USD | 0.00 USD | 1,580.00 USD | `-21.58%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 352,610.00 USD | 0.00 USD | 315.81 USD | `-21.28%` | `1,217.00` |
| `Live` | `Long` | `0.2605` | 352,300.00 USD | 0.00 USD | 8,650.00 USD | `-20.97%` | `33,208.00` |
| `Live` | `Long` | `0.2615` | 343,650.00 USD | 0.00 USD | 466.78 USD | `-20.67%` | `1,785.00` |
| `Live` | `Long` | `0.2635` | 343,180.00 USD | 0.00 USD | 108.56 USD | `-20.06%` | `412.00` |
| `Live` | `Long` | `0.2655` | 343,070.00 USD | 0.00 USD | 7,520.00 USD | `-19.46%` | `28,325.00` |
| `Live` | `Long` | `0.2665` | 335,550.00 USD | 0.00 USD | 450.92 USD | `-19.15%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 335,100.00 USD | 0.00 USD | 495.41 USD | `-18.85%` | `1,852.00` |
| `Live` | `Long` | `0.2685` | 334,610.00 USD | 0.00 USD | 322.74 USD | `-18.55%` | `1,202.00` |
| `Live` | `Long` | `0.2705` | 334,280.00 USD | 0.00 USD | 686.53 USD | `-17.94%` | `2,538.00` |
| `Live` | `Long` | `0.2725` | 333,600.00 USD | 0.00 USD | 412.84 USD | `-17.33%` | `1,515.00` |
| `Live` | `Long` | `0.2755` | 333,180.00 USD | 0.00 USD | 85,120.00 USD | `-16.42%` | `308,954.00` |
| `Live` | `Long` | `0.2775` | 248,070.00 USD | 0.00 USD | 29,880.00 USD | `-15.82%` | `107,693.00` |
| `Live` | `Long` | `0.2785` | 218,180.00 USD | 0.00 USD | 2,310.00 USD | `-15.51%` | `8,290.00` |
| `Live` | `Long` | `0.2795` | 215,870.00 USD | 0.00 USD | 13,590.00 USD | `-15.21%` | `48,633.00` |
| `Live` | `Long` | `0.2805` | 202,280.00 USD | 0.00 USD | 6,280.00 USD | `-14.91%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 196,000.00 USD | 0.00 USD | 1,310.00 USD | `-14.60%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 194,700.00 USD | 0.00 USD | 15,060.00 USD | `-14.30%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 179,630.00 USD | 0.00 USD | 1,430.00 USD | `-14.00%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 178,200.00 USD | 0.00 USD | 360.42 USD | `-13.09%` | `1,258.00` |
| `Live` | `Long` | `0.2875` | 177,840.00 USD | 0.00 USD | 42,200.00 USD | `-12.78%` | `146,785.00` |
| `Live` | `Long` | `0.2915` | 135,640.00 USD | 0.00 USD | 591.45 USD | `-11.57%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 135,050.00 USD | 0.00 USD | 957.64 USD | `-11.27%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 134,090.00 USD | 0.00 USD | 3,760.00 USD | `-10.66%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 130,330.00 USD | 0.00 USD | 125.29 USD | `-10.36%` | `424.00` |
| `Live` | `Long` | `0.2985` | 130,210.00 USD | 0.00 USD | 244.47 USD | `-9.45%` | `819.00` |
| `Live` | `Long` | `0.2995` | 129,960.00 USD | 0.00 USD | 127.89 USD | `-9.14%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,830.00 USD | 0.00 USD | 7,130.00 USD | `-8.84%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,710.00 USD | 0.00 USD | 12,010.00 USD | `-8.54%` | `39,820.00` |
| `Live` | `Long` | `0.3025` | 110,700.00 USD | 0.00 USD | 694.54 USD | `-8.23%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 110,010.00 USD | 0.00 USD | 693.50 USD | `-7.93%` | `2,285.00` |
| `Live` | `Long` | `0.3045` | 109,310.00 USD | 0.00 USD | 5,540.00 USD | `-7.63%` | `18,187.00` |
| `Live` | `Long` | `0.3055` | 103,770.00 USD | 0.00 USD | 5,300.00 USD | `-7.32%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 98,470.00 USD | 0.00 USD | 14,720.00 USD | `-7.02%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 83,750.00 USD | 0.00 USD | 6,670.00 USD | `-6.41%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 77,080.00 USD | 0.00 USD | 304.34 USD | `-5.50%` | `977.00` |
| `Live` | `Long` | `0.3125` | 76,780.00 USD | 0.00 USD | 17,770.00 USD | `-5.20%` | `56,868.00` |
| `Live` | `Long` | `0.3135` | 59,010.00 USD | 0.00 USD | 44,080.00 USD | `-4.90%` | `140,602.00` |
| `Live` | `Long` | `0.3145` | 14,930.00 USD | 0.00 USD | 1,220.00 USD | `-4.59%` | `3,895.00` |
| `Live` | `Long` | `0.3155` | 13,710.00 USD | 0.00 USD | 142.29 USD | `-4.29%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,560.00 USD | 0.00 USD | 1,490.00 USD | `-3.99%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,070.00 USD | 0.00 USD | 938.85 USD | `-3.68%` | `2,957.00` |
| `Live` | `Long` | `0.3235` | 11,130.00 USD | 0.00 USD | 11,000.00 USD | `-1.86%` | `34,003.00` |
| `Live` | `Long` | `0.3265` | 129.62 USD | 0.00 USD | 129.62 USD | `-0.95%` | `397.00` |
| `Live` | `Short` | `0.3405` | 10,680.00 USD | 10,680.00 USD | 0.00 USD | `+3.29%` | `31,368.00` |
| `Live` | `Short` | `0.3435` | 10,830.00 USD | 153.89 USD | 0.00 USD | `+4.20%` | `448.00` |
| `Live` | `Short` | `0.3445` | 11,450.00 USD | 611.49 USD | 0.00 USD | `+4.51%` | `1,775.00` |
| `Live` | `Short` | `0.3475` | 13,150.00 USD | 1,700.00 USD | 0.00 USD | `+5.42%` | `4,901.00` |
| `Live` | `Short` | `0.3505` | 13,360.00 USD | 212.40 USD | 0.00 USD | `+6.33%` | `606.00` |
| `Live` | `Short` | `0.3515` | 17,080.00 USD | 3,720.00 USD | 0.00 USD | `+6.63%` | `10,572.00` |
| `Live` | `Short` | `0.3535` | 17,300.00 USD | 223.06 USD | 0.00 USD | `+7.24%` | `631.00` |
| `Live` | `Short` | `0.3605` | 37,820.00 USD | 20,520.00 USD | 0.00 USD | `+9.36%` | `56,909.00` |
| `Live` | `Short` | `0.3645` | 38,190.00 USD | 376.53 USD | 0.00 USD | `+10.58%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 38,460.00 USD | 262.78 USD | 0.00 USD | `+11.18%` | `717.00` |
| `Live` | `Short` | `0.3745` | 45,150.00 USD | 6,690.00 USD | 0.00 USD | `+13.61%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 45,690.00 USD | 537.85 USD | 0.00 USD | `+14.82%` | `1,421.00` |
| `Live` | `Short` | `0.3795` | 603,580.00 USD | 557,900.00 USD | 0.00 USD | `+15.13%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 603,870.00 USD | 285.74 USD | 0.00 USD | `+15.73%` | `749.00` |
| `Live` | `Short` | `0.3845` | 603,980.00 USD | 115.35 USD | 0.00 USD | `+16.64%` | `300.00` |
| `Live` | `Short` | `0.3895` | 610,270.00 USD | 6,280.00 USD | 0.00 USD | `+18.16%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 615,040.00 USD | 4,770.00 USD | 0.00 USD | `+18.46%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 615,520.00 USD | 487.42 USD | 0.00 USD | `+18.77%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 617,010.00 USD | 1,490.00 USD | 0.00 USD | `+19.68%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 735,440.00 USD | 118,430.00 USD | 0.00 USD | `+19.98%` | `299,436.00` |
| `Live` | `Short` | `0.4105` | 739,810.00 USD | 4,380.00 USD | 0.00 USD | `+24.53%` | `10,665.00` |
| `Live` | `Short` | `0.4145` | 740,090.00 USD | 278.13 USD | 0.00 USD | `+25.74%` | `671.00` |
| `Live` | `Short` | `0.4185` | 740,260.00 USD | 167.40 USD | 0.00 USD | `+26.96%` | `400.00` |
| `Live` | `Short` | `0.4385` | 811,640.00 USD | 71,380.00 USD | 0.00 USD | `+33.02%` | `162,775.00` |
| `Live` | `Short` | `0.4475` | 812,660.00 USD | 1,020.00 USD | 0.00 USD | `+35.75%` | `2,284.00` |
| `Live` | `Short` | `0.4705` | 812,760.00 USD | 103.98 USD | 0.00 USD | `+42.73%` | `221.00` |
| `Live` | `Short` | `0.4905` | 813,600.00 USD | 841.21 USD | 0.00 USD | `+48.80%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 818,730.00 USD | 5,130.00 USD | 0.00 USD | `+49.10%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 819,400.00 USD | 669.73 USD | 0.00 USD | `+62.15%` | `1,253.00` |
| `Live` | `Short` | `0.5455` | 838,160.00 USD | 18,760.00 USD | 0.00 USD | `+65.48%` | `34,396.00` |
| `Live` | `Short` | `0.5585` | 838,910.00 USD | 742.25 USD | 0.00 USD | `+69.43%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,570,000.00 USD | 729,840.00 USD | 0.00 USD | `+70.64%` | `1,297,498.00` |
| `Live` | `Short` | `0.6145` | 1,610,000.00 USD | 36,870.00 USD | 0.00 USD | `+86.42%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,610,000.00 USD | 275.47 USD | 0.00 USD | `+90.36%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,610,000.00 USD | 7,390.00 USD | 0.00 USD | `+90.66%` | `11,753.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 796,920.00 USD | 0.00 USD | 6,100.00 USD | `-45.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 790,830.00 USD | 0.00 USD | 1,750.00 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 789,070.00 USD | 0.00 USD | 579.72 USD | `-36.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 788,490.00 USD | 0.00 USD | 121.70 USD | `-30.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 788,370.00 USD | 0.00 USD | 705.61 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 787,670.00 USD | 0.00 USD | 1,200.00 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 786,460.00 USD | 0.00 USD | 127.51 USD | `-26.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 786,340.00 USD | 0.00 USD | 1,850.00 USD | `-24.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 784,480.00 USD | 0.00 USD | 1,920.00 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 782,560.00 USD | 0.00 USD | 664.01 USD | `-20.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 781,890.00 USD | 0.00 USD | 954.98 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 780,940.00 USD | 0.00 USD | 695.50 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 780,240.00 USD | 0.00 USD | 1,630.00 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 778,620.00 USD | 0.00 USD | 2,550.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 776,060.00 USD | 0.00 USD | 229.92 USD | `-14.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 775,830.00 USD | 0.00 USD | 15,940.00 USD | `-10.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 759,890.00 USD | 0.00 USD | 111.19 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 759,780.00 USD | 0.00 USD | 685.95 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 759,100.00 USD | 0.00 USD | 2,710.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 756,390.00 USD | 0.00 USD | 335.56 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 756,060.00 USD | 0.00 USD | 919.50 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 755,140.00 USD | 0.00 USD | 193.11 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 754,940.00 USD | 0.00 USD | 16,070.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 738,880.00 USD | 0.00 USD | 147.32 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 738,730.00 USD | 0.00 USD | 25,820.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 712,910.00 USD | 0.00 USD | 6,530.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 706,390.00 USD | 0.00 USD | 524,570.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 181,810.00 USD | 0.00 USD | 1,270.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 180,550.00 USD | 0.00 USD | 25,790.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 154,760.00 USD | 0.00 USD | 3,510.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 151,250.00 USD | 0.00 USD | 6,100.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 145,160.00 USD | 0.00 USD | 2,010.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 143,140.00 USD | 0.00 USD | 15,050.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 128,090.00 USD | 0.00 USD | 21,270.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 106,820.00 USD | 0.00 USD | 55,600.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 51,220.00 USD | 0.00 USD | 131.90 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 51,090.00 USD | 0.00 USD | 740.82 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 50,350.00 USD | 0.00 USD | 14,470.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 35,880.00 USD | 0.00 USD | 7,660.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 28,220.00 USD | 0.00 USD | 24,840.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 3,390.00 USD | 0.00 USD | 1,050.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 2,330.00 USD | 0.00 USD | 504.90 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 1,830.00 USD | 0.00 USD | 1,830.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3305` | 1,840.00 USD | 1,840.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3315` | 1,940.00 USD | 100.11 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 2,080.00 USD | 135.99 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 2,190.00 USD | 106.39 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 3,410.00 USD | 1,220.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 178,270.00 USD | 174,860.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 178,390.00 USD | 119.79 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 178,550.00 USD | 162.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 190,200.00 USD | 11,640.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 190,300.00 USD | 102.87 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 193,390.00 USD | 3,090.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 195,900.00 USD | 2,520.00 USD | 0.00 USD | `+3.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 201,430.00 USD | 5,520.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 209,040.00 USD | 7,610.00 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 211,910.00 USD | 2,870.00 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 219,840.00 USD | 7,930.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 222,300.00 USD | 2,450.00 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 223,520.00 USD | 1,220.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 249,270.00 USD | 25,750.00 USD | 0.00 USD | `+6.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 267,850.00 USD | 18,580.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 281,270.00 USD | 13,420.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 282,040.00 USD | 769.97 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 283,230.00 USD | 1,190.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 283,350.00 USD | 122.62 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 289,210.00 USD | 5,860.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 295,390.00 USD | 6,180.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 295,880.00 USD | 485.59 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 296,270.00 USD | 390.40 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 296,700.00 USD | 433.85 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 297,170.00 USD | 463.99 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 297,330.00 USD | 159.62 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 298,250.00 USD | 926.99 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 300,900.00 USD | 2,650.00 USD | 0.00 USD | `+13.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 301,180.00 USD | 275.17 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 301,640.00 USD | 463.37 USD | 0.00 USD | `+15.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 301,980.00 USD | 337.12 USD | 0.00 USD | `+15.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 302,090.00 USD | 114.83 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 302,320.00 USD | 224.73 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 302,830.00 USD | 514.64 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 303,180.00 USD | 352.11 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 305,590.00 USD | 2,400.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 306,160.00 USD | 572.00 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 307,360.00 USD | 1,200.00 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 360,240.00 USD | 52,880.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 362,640.00 USD | 2,400.00 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 363,830.00 USD | 1,200.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 365,040.00 USD | 1,200.00 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 366,230.00 USD | 1,200.00 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 366,420.00 USD | 186.70 USD | 0.00 USD | `+27.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 405,000.00 USD | 38,580.00 USD | 0.00 USD | `+33.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 405,170.00 USD | 170.69 USD | 0.00 USD | `+34.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 406,560.00 USD | 1,390.00 USD | 0.00 USD | `+36.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 417,710.00 USD | 11,150.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.2958` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.2962` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 386.20 USD | 1,050.00 USD | 9,660.00 USD |
| `1D` | `0.2966` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 27,760.00 USD | 8,570.00 USD | 6,610.00 USD |
| `1D` | `0.2970` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 9,760.00 USD | 4,390.00 USD | 14,730.00 USD |
| `1D` | `0.2974` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 156.80 USD | 3,840.00 USD | 4,390.00 USD |
| `1D` | `0.2978` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 23,600.00 USD | 6,620.00 USD | 6,500.00 USD |
| `7D` | `0.2979` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2982` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 41,590.00 USD | 11,830.00 USD | 23,600.00 USD |
| `7D` | `0.2983` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD |
| `1D` | `0.2986` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 117,260.00 USD | 13,490.00 USD | 10,750.00 USD |
| `7D` | `0.2987` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `1D` | `0.2990` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 8,790.00 USD |
| `7D` | `0.2991` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `1D` | `0.2994` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3002` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 4,620.00 USD | 3,220.00 USD | 0.00 USD |
| `1D` | `0.3006` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 0.00 USD | 1,800.00 USD | 16,090.00 USD |
| `1D` | `0.3010` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 13,540.00 USD | 3,410.00 USD | 0.00 USD |
| `7D` | `0.3051` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3066` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3070` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 452.85 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3074` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 562.75 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3078` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 95.35 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3082` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 293.62 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3086` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 422.57 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3090` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 321.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3094` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 161.62 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3122` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 2,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3126` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 883.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3130` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 471.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3134` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 127.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3138` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 391.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3142` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 140.10 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3146` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 852.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD |
| `1D` | `0.3150` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD |
| `1D` | `0.3158` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 0.00 USD | 3,680.00 USD | 14,720.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3162` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 66,530.00 USD | 20,130.00 USD | 23,780.00 USD |
| `7D` | `0.3163` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `1D` | `0.3166` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 49,870.00 USD | 11,700.00 USD | 29,070.00 USD |
| `7D` | `0.3167` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3170` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 17,750.00 USD | 13,740.00 USD | 24,330.00 USD |
| `7D` | `0.3171` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3174` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 9,140.00 USD | 12,730.00 USD | 7,100.00 USD |
| `7D` | `0.3175` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3178` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 78,240.00 USD | 17,000.00 USD | 20,870.00 USD |
| `7D` | `0.3179` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3182` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 424,700.00 USD | 60,650.00 USD | 93,940.00 USD |
| `7D` | `0.3183` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD |
| `1D` | `0.3186` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 64,790.00 USD | 15,380.00 USD | 2,590.00 USD |
| `7D` | `0.3187` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `1D` | `0.3190` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `0.3191` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `1D` | `0.3194` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `1D` | `0.3202` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 24,400.00 USD | 8,050.00 USD | 23,180.00 USD |
| `1D` | `0.3206` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 4,500.00 USD | 40,220.00 USD |
| `7D` | `0.3207` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `1D` | `0.3210` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 33,860.00 USD | 8,530.00 USD | 0.00 USD |
| `7D` | `0.3211` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3219` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `7D` | `0.3223` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3226` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 34,160.00 USD | 19,120.00 USD | 61,130.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3230` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 164,650.00 USD | 39,750.00 USD | 31,990.00 USD |
| `7D` | `0.3231` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3234` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 54,080.00 USD | 24,770.00 USD | 79,050.00 USD |
| `7D` | `0.3235` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3238` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 22,730.00 USD | 28,170.00 USD | 21,930.00 USD |
| `7D` | `0.3239` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3242` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 90,440.00 USD | 24,160.00 USD | 17,610.00 USD |
| `7D` | `0.3243` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3246` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 168,730.00 USD | 66,050.00 USD | 102,480.00 USD |
| `7D` | `0.3247` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `1D` | `0.3250` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 806,230.00 USD | 96,200.00 USD | 118,580.00 USD |
| `7D` | `0.3251` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3254` | 428,510.00 USD | 0.00 USD | 428,510.00 USD | 81,010.00 USD | 11,820.00 USD | 43,960.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3262` | 291,720.00 USD | 0.00 USD | 291,720.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD |
| `1D` | `0.3270` | 285,480.00 USD | 0.00 USD | 285,480.00 USD | 48,790.00 USD | 16,100.00 USD | 46,350.00 USD |
| `1D` | `0.3274` | 174,240.00 USD | 0.00 USD | 174,240.00 USD | 67,720.00 USD | 26,070.00 USD | 80,450.00 USD |
| `7D` | `0.3315` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3354` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `7D` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `7D` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3366` | 86,330.00 USD | 86,330.00 USD | 0.00 USD | 38,540.00 USD | 20,810.00 USD | 26,980.00 USD |
| `7D` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3370` | 159,160.00 USD | 159,160.00 USD | 0.00 USD | 22,730.00 USD | 28,170.00 USD | 21,930.00 USD |
| `7D` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3374` | 291,360.00 USD | 291,360.00 USD | 0.00 USD | 90,440.00 USD | 24,160.00 USD | 17,610.00 USD |
| `7D` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3378` | 628,630.00 USD | 628,630.00 USD | 0.00 USD | 168,730.00 USD | 66,050.00 USD | 102,480.00 USD |
| `7D` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `1D` | `0.3382` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 806,230.00 USD | 96,200.00 USD | 118,580.00 USD |
| `7D` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3386` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 81,010.00 USD | 11,820.00 USD | 43,960.00 USD |
| `7D` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3394` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 0.00 USD |
| `1D` | `0.3402` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 48,790.00 USD | 16,100.00 USD | 46,350.00 USD |
| `7D` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `1D` | `0.3406` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 9,000.00 USD | 0.00 USD |
| `7D` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `1D` | `0.3410` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 67,720.00 USD | 17,070.00 USD | 80,450.00 USD |
| `7D` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `7D` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD |
| `7D` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3422` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 3,680.00 USD | 14,720.00 USD |
| `7D` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3426` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 66,530.00 USD | 20,130.00 USD | 23,780.00 USD |
| `7D` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `1D` | `0.3430` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 49,870.00 USD | 11,700.00 USD | 29,070.00 USD |
| `7D` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3434` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 17,750.00 USD | 13,740.00 USD | 24,330.00 USD |
| `7D` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3438` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 9,140.00 USD | 12,730.00 USD | 7,100.00 USD |
| `7D` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3442` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 78,240.00 USD | 17,000.00 USD | 20,870.00 USD |
| `7D` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3446` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 125,210.00 USD | 37,340.00 USD | 64,590.00 USD |
| `7D` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD |
| `1D` | `0.3450` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 339,490.00 USD | 38,680.00 USD | 31,940.00 USD |
| `7D` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3454` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3458` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 844.80 USD | 3,120.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3462` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 127.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3466` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 78.10 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3470` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 24,720.00 USD | 8,050.00 USD | 23,180.00 USD |
| `7D` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3474` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 899.30 USD | 4,500.00 USD | 40,220.00 USD |
| `7D` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3478` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 33,940.00 USD | 8,530.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3482` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 215.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3506` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3510` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 452.85 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3514` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 562.75 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3518` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 95.35 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3522` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 58.54 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3526` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 243.85 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3530` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 413.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3534` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 321.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3538` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 161.62 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `7D` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `1D` | `0.3618` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 1,160.00 USD | 0.00 USD | 4,050.00 USD |
| `7D` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3622` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 10,540.00 USD | 6,220.00 USD | 6,890.00 USD |
| `7D` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD |
| `1D` | `0.3626` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 17,400.00 USD | 3,400.00 USD | 5,320.00 USD |
| `7D` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3630` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 9,760.00 USD | 4,390.00 USD | 14,730.00 USD |
| `7D` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3634` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 156.80 USD | 3,840.00 USD | 4,390.00 USD |
| `7D` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3638` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 4,270.00 USD | 3,890.00 USD | 1,350.00 USD |
| `7D` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3642` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 23,360.00 USD | 7,120.00 USD | 11,930.00 USD |
| `7D` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD |
| `1D` | `0.3646` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 98,950.00 USD | 12,450.00 USD | 23,630.00 USD |
| `7D` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `1D` | `0.3650` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 55,860.00 USD | 8,480.00 USD | 3,940.00 USD |
| `7D` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |
| `1D` | `0.3654` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,790.00 USD |
| `1D` | `0.3658` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3670` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 4,620.00 USD | 3,220.00 USD | 0.00 USD |
| `1D` | `0.3674` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 1,800.00 USD | 16,090.00 USD |
| `1D` | `0.3678` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 13,540.00 USD | 3,410.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `308.67M` | Total OI Tokens: `923,229,271.0 TRX`
  * 1h OI Change: `+1.01%` | 4h OI Change: `+3.33%` | 24h OI Change: `+5.76%`
  * Exchange Breakdown: Binance=`90.54M` | Bybit=`52.19M` | OKX=`14.22M` | Hyperliquid=`15.51M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.22K` | Last 24h: `9.22K` | Last 3d: `-51.81K` | Last 7d: `-271.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0044%` | **USDT OKX** | `-0.0073%` |
| **USDT Bybit** | `0.0029%` | **USDT KuCoin** | `0.0093%` |
| **USDT MEXC** | `0.0044%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `50.20%` | `49.80%` | `1.01` | 42,150,000.00 USD |
| `15M` | `Binance` | `48.36%` | `51.64%` | `0.94` | 14,160,000.00 USD |
| `15M` | `OKX` | `49.96%` | `50.04%` | `1.00` | 6,380,000.00 USD |
| `15M` | `Bybit` | `49.7%` | `50.3%` | `0.99` | 3,850,000.00 USD |
| `15M` | `KuCoin` | `46.16%` | `53.84%` | `0.86` | 254,410.00 USD |
| `15M` | `Gate` | `59.73%` | `40.27%` | `1.48` | 3,040,000.00 USD |
| `15M` | `Bitget` | `52.5%` | `47.5%` | `1.11` | 3,450,000.00 USD |
| `15M` | `BingX` | `32.69%` | `67.31%` | `0.49` | 1,070,000.00 USD |
| `15M` | `MEXC` | `44.69%` | `55.31%` | `0.81` | 1,780,000.00 USD |
| `15M` | `Bitunix` | `49.81%` | `50.19%` | `0.99` | 898,910.00 USD |
| `15M` | `Hyperliquid` | `48.12%` | `51.88%` | `0.93` | 502,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.45%` | `45.55%` | `1.20` | 6,410,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `9.56%` | `90.44%` | `0.11` | 162,780.00 USD |
| `15M` | `HTX` | `48.17%` | `51.83%` | `0.93` | 24,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `67.64%` | `32.36%` | `2.09` | 144,550.00 USD |
| `15M` | `Aster` | `74.34%` | `25.66%` | `2.90` | 22,830.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `60.51%` | `39.49%` | `1.53` | 4,050.00 USD |
| `15M` | `Whale Positions` | `48.36%` | `51.64%` | `0.94` | 14,160,000.00 USD |
| `15M` | `Global Accounts` | `50.20%` | `49.80%` | `1.01` | 42,150,000.00 USD |
| `1H` | `TRX` | `47.36%` | `52.64%` | `0.90` | 377,240,000.00 USD |
| `1H` | `Binance` | `45.21%` | `54.79%` | `0.83` | 167,250,000.00 USD |
| `1H` | `OKX` | `47.65%` | `52.35%` | `0.91` | 86,570,000.00 USD |
| `1H` | `Bybit` | `47.26%` | `52.74%` | `0.90` | 42,450,000.00 USD |
| `1H` | `KuCoin` | `54.65%` | `45.35%` | `1.21` | 3,800,000.00 USD |
| `1H` | `Gate` | `49.85%` | `50.15%` | `0.99` | 19,350,000.00 USD |
| `1H` | `Bitget` | `46.81%` | `53.19%` | `0.88` | 10,650,000.00 USD |
| `1H` | `BingX` | `44.94%` | `55.06%` | `0.82` | 3,060,000.00 USD |
| `1H` | `MEXC` | `44.66%` | `55.34%` | `0.81` | 15,620,000.00 USD |
| `1H` | `Bitunix` | `46.85%` | `53.15%` | `0.88` | 9,300,000.00 USD |
| `1H` | `Hyperliquid` | `44.31%` | `55.69%` | `0.80` | 4,230,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.75%` | `46.25%` | `1.16` | 1,500,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 413,700.00 USD |
| `1H` | `WhiteBIT` | `6.38%` | `93.62%` | `0.07` | 3,450,000.00 USD |
| `1H` | `HTX` | `47.6%` | `52.4%` | `0.91` | 3,060,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.83%` | `48.17%` | `1.08` | 1,500,000.00 USD |
| `1H` | `Aster` | `37.6%` | `62.4%` | `0.60` | 4,850,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.63%` | `45.37%` | `1.20` | 171,310.00 USD |
| `1H` | `Whale Positions` | `45.21%` | `54.79%` | `0.83` | 167,250,000.00 USD |
| `1H` | `Global Accounts` | `47.36%` | `52.64%` | `0.90` | 377,240,000.00 USD |
| `4H` | `TRX` | `47.21%` | `52.79%` | `0.89` | 292,030,000.00 USD |
| `4H` | `Binance` | `45.64%` | `54.36%` | `0.84` | 100,150,000.00 USD |
| `4H` | `OKX` | `47.57%` | `52.43%` | `0.91` | 34,540,000.00 USD |
| `4H` | `Bybit` | `47.03%` | `52.97%` | `0.89` | 29,260,000.00 USD |
| `4H` | `KuCoin` | `51.29%` | `48.71%` | `1.05` | 2,400,000.00 USD |
| `4H` | `Gate` | `51.89%` | `48.11%` | `1.08` | 13,990,000.00 USD |
| `4H` | `Bitget` | `46.54%` | `53.46%` | `0.87` | 24,190,000.00 USD |
| `4H` | `BingX` | `46.47%` | `53.53%` | `0.87` | 8,590,000.00 USD |
| `4H` | `MEXC` | `44.75%` | `55.25%` | `0.81` | 19,170,000.00 USD |
| `4H` | `Bitunix` | `49.04%` | `50.96%` | `0.96` | 7,150,000.00 USD |
| `4H` | `Hyperliquid` | `41.41%` | `58.59%` | `0.71` | 4,150,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.92%` | `47.08%` | `1.12` | 44,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.95%` | `95.05%` | `0.05` | 2,270,000.00 USD |
| `4H` | `HTX` | `46.71%` | `53.29%` | `0.88` | 540,140.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.66%` | `49.34%` | `1.03` | 1,250,000.00 USD |
| `4H` | `Aster` | `35.78%` | `64.22%` | `0.56` | 224,530.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.8%` | `57.2%` | `0.75` | 99,050.00 USD |
| `4H` | `Whale Positions` | `45.64%` | `54.36%` | `0.84` | 100,150,000.00 USD |
| `4H` | `Global Accounts` | `47.21%` | `52.79%` | `0.89` | 292,030,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 89,593.30 USD | 27,876.48 USD | 61,716.82 USD | -33,840.33 USD | `-37.77%` | `1B / 7S` |
| `0:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 149,813.03 USD | 80,120.40 USD | 69,692.63 USD | 10,427.77 USD | `+6.96%` | `4B / 2S` |
| `5:00 UTC` | `0.3314` | `0.3314` | `0.3314` | `0.3315` | `0.3313` | 181,186.70 USD | 125,777.62 USD | 55,409.08 USD | 70,368.54 USD | `+38.84%` | `7B / 3S` |
| `0:00 UTC` | `0.3316` | `0.3315` | `0.3316` | `0.3316` | `0.3313` | 274,455.87 USD | 151,943.78 USD | 122,512.08 USD | 29,431.70 USD | `+10.72%` | `6B / 8S` |
| `5:00 UTC` | `0.3316` | `0.3315` | `0.3316` | `0.3316` | `0.3315` | 97,541.21 USD | 34,795.54 USD | 62,745.67 USD | -27,950.14 USD | `-28.65%` | `4B / 4S` |
| `0:00 UTC` | `0.3311` | `0.3313` | `0.3311` | `0.3316` | `0.3310` | 747,180.14 USD | 373,024.41 USD | 374,155.73 USD | -1,131.33 USD | `-0.15%` | `16B / 17S` |
| `5:00 UTC` | `0.3313` | `0.3314` | `0.3313` | `0.3315` | `0.3312` | 312,440.76 USD | 170,379.42 USD | 142,061.34 USD | 28,318.07 USD | `+9.06%` | `13B / 7S` |
| `0:00 UTC` | `0.3308` | `0.3304` | `0.3308` | `0.3313` | `0.3295` | 3,091,479.93 USD | 681,981.05 USD | 2,409,498.88 USD | -1,727,517.83 USD | `-55.88%` | `20B / 55S` |
| `5:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3363` | `0.3285` | 10,644,567.03 USD | 5,188,760.14 USD | 5,455,806.89 USD | -267,046.75 USD | `-2.51%` | `23B / 18S` |
| `0:00 UTC` | `0.3310` | `0.3308` | `0.3310` | `0.3327` | `0.3282` | 3,816,992.27 USD | 2,389,119.90 USD | 1,427,872.36 USD | 961,247.54 USD | `+25.18%` | `41B / 28S` |

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
| `5m` | 618,380.00 USD | 1,250,000.00 USD | **`ACCUMULATION`** |
| `15m` | 543,810.00 USD | 2,210,000.00 USD | **`ACCUMULATION`** |
| `30m` | -649,260.00 USD | 238,020.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,510,000.00 USD | 327,150.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,890,000.00 USD | 506,860.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,870,000.00 USD | 788,140.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,320,000.00 USD | 671,120.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,180,000.00 USD | 994,780.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,440,000.00 USD | 839,930.00 USD | **`DISTRIBUTION`** |
| `24h` | 1,850,000.00 USD | 3,830,000.00 USD | **`ACCUMULATION`** |
| `1w` | -5,440,000.00 USD | 1,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -24,780,000.00 USD | 4,270,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+618.38K` | 15m=`+543.81K` | 1h=`-1.51M` | 24h=`+1.85M`
* Futures Capital Netflows: 5m=`+1.25M` | 15m=`+2.21M` | 1h=`+327.15K` | 24h=`+3.83M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3293` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3245` (Risk Distance: `0.0056` pts)
  * +2.5R Take Profit: `0.3433`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3360` (Risk Distance: `0.0056` pts)
  * +2.5R Take Profit: `0.3172`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3315`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
