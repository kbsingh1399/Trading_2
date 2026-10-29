# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 03:40:27 IST` (`2026-10-29 22:10:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3542` | **Live Ask Quote**: `0.3592` | **Mid Price**: `0.3567`
- **Spread Points**: `50.00` | **Spread BPS**: `140.17 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3567` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3592` | Lower -3.00σ Band: `0.3542`
  * Upper +2.51σ Band: `0.3587` | Lower -2.51σ Band: `0.3547`
  * Upper +2.01σ Band: `0.3582` | Lower -2.01σ Band: `0.3552`
  * Upper +2.00σ Band: `0.3581` | Lower -2.00σ Band: `0.3553`
  * Upper +1.28σ Band: `0.3577` | Lower -1.28σ Band: `0.3557`
  * Upper +1.00σ Band: `0.3574` | Lower -1.00σ Band: `0.3560`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3567` | EMA-20=`0.3567` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3567` (Slope: `+0.0000`) | EMA-100=`0.3567`
  * Institutional Anchors: EMA-144=`0.3567` | EMA-200=`0.3567` (Slope: `+0.0000`) | EMA-233=`0.3567`
- **Range Boundaries**: 24H High=`0.3603` | 24H Low=`0.3531` | Weekly High=`0.3638` | Weekly Low=`0.3496`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3532` (Distance: `+1.15%`)
  * Point of Control (POC) = `0.3441` (Distance: `+3.82%`)
  * Value Area Low (VAL) = `0.3342` (Distance: `+6.90%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3316` | Weekly POC=`0.3306` | Weekly VAL=`0.3282`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3581` | Low=`0.3553`
  * New York Session (13:00-21:00 UTC): High=`0.3588` | Low=`0.3546`
  * Initial Balance (First Hour): IB High=`0.3578` | IB Low=`0.3556`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3553` - `0.3581`
  * Optimal Trade Entry (OTE 0.705): `0.3574`
  * Structural Invalidation Anchor (0.786): `0.3596`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3599` | `0.3620` | `0.3547` | `0.3605` | `37,030,450` | 13,274,879.53 USD | 658,750.78 USD | `+4.96%` | 3,599,898.07 USD | `+0.88` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.3605` | `0.3653` | `0.3569` | `0.3572` | `45,597,517` | 16,499,985.63 USD | 381,161.45 USD | `+2.31%` | 3,981,059.52 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.3572` | `0.3573` | `0.3550` | `0.3572` | `3,817,929` | 1,360,846.10 USD | -26,548.59 USD | `-1.95%` | 3,954,510.94 USD | `-0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3411` | `0.3499` | `0.3360` | `0.3469` | `63,787,992` | 21,787,549.51 USD | 2,150,841.30 USD | `+9.87%` | 3,666,315.17 USD | `+2.93` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3469` | `0.3650` | `0.3466` | `0.3605` | `124,705,981` | 44,541,588.04 USD | -81,226.19 USD | `-0.18%` | 3,585,088.98 USD | `-0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3605` | `0.3653` | `0.3550` | `0.3576` | `49,672,732` | 17,952,782.52 USD | 402,022.24 USD | `+2.24%` | 3,987,111.23 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3315` | `0.3363` | `0.3285` | `0.3295` | `44,626,076` | 14,795,667.86 USD | -1,967,377.84 USD | `-13.30%` | 36,856.06 USD | `-3.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3295` | `0.3650` | `0.3282` | `0.3605` | `269,212,638` | 93,735,194.61 USD | 3,250,400.68 USD | `+3.47%` | 3,287,256.74 USD | `+3.58` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3605` | `0.3653` | `0.3550` | `0.3563` | `48,399,596` | 17,498,544.28 USD | 250,968.07 USD | `+1.43%` | 3,538,224.81 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3572` | `363,254,160` | 126,391,694.20 USD | 1,637,635.71 USD | `+1.30%` | 3,482,861.43 USD | `+2.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,247,572.49 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 1,263,826.68 USD | `-1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 1,633,134.85 USD | `-0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 1,845,225.72 USD | `-0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3572` | `363,254,160` | 126,391,694.20 USD | 1,637,635.71 USD | `+1.30%` | 3,482,861.43 USD | `+2.03` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3567`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `767` | `0xecb6...2b00` | `LONG` | 2,999,532.38 USD | `8,562,753.00` | `0.3330` | `0.3462` | `0.000000` | 148,391.15 USD | `+4.95%` | `10X Cross` |
| `1555` | `0xeadc...9d55` | `LONG` | 1,424,960.00 USD | `4,000,000.00` | `0.3421` | `0.3462` | `0.000000` | 56,481.91 USD | `+3.96%` | `10X Cross` |
| `1793` | `0xf517...c032` | `SHORT` | 1,171,030.28 USD | `3,241,068.00` | `0.3584` | `0.3462` | `2.81` | -9,292.54 USD | `-0.79%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 7,828.12 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 7.83K USD at 0.3317 USD [API] | `2026-10-28 12:48:28` |
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 5,363.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.36K USD at 0.3317 USD [API] | `2026-10-28 13:13:46` |
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
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.3248` (Vol: 494,500.00 USD, Dist: `--10.97%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.3251` (Vol: 581,100.00 USD, Dist: `--10.89%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.3250` (Vol: 826,400.00 USD, Dist: `--10.91%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.3250` (Vol: 887,200.00 USD, Dist: `--10.91%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0765` | 977.75 USD | 510,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 3,330.00 USD | 509,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 171.52 USD | 505,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 575.31 USD | 505,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 546.05 USD | 505,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 504,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,360.00 USD | 504,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 10,410.00 USD | 502,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,520.00 USD | 492,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 429.65 USD | 486,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 1,020.00 USD | 486,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 485,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 505.50 USD | 484,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 484,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,160.00 USD | 464,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 954.34 USD | 452,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 451,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,810.00 USD | 450,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 433.81 USD | 408,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1785` | 890.18 USD | 407,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 406,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,150.00 USD | 406,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 4,140.00 USD | 405,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 638.40 USD | 401,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 6,130.00 USD | 400,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 526.67 USD | 394,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 3,330.00 USD | 394,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 195.72 USD | 390,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 1,530.00 USD | 390,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 388,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 2,580.00 USD | 388,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 3,350.00 USD | 385,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 382,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 4,180.00 USD | 377,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,730.00 USD | 373,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 308.30 USD | 371,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,370.00 USD | 370,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 729.53 USD | 368,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,140.00 USD | 367,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 345.56 USD | 361,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 361,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 181.58 USD | 359,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 359,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 358,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 276.57 USD | 358,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,420.00 USD | 358,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 200.40 USD | 355,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 355,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 1,580.00 USD | 354,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 315.81 USD | 352,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 8,650.00 USD | 352,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 466.78 USD | 343,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 108.56 USD | 343,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,520.00 USD | 343,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 450.92 USD | 335,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 495.41 USD | 335,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 334,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2705` | 686.53 USD | 334,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 333,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 85,120.00 USD | 333,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 29,880.00 USD | 248,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 2,310.00 USD | 218,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 13,590.00 USD | 215,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 202,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,310.00 USD | 196,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 194,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 179,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 178,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2875` | 42,200.00 USD | 177,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 135,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 135,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 134,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 130,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2959` | 18,620,000.00 USD | 18,620,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2965` | 18,620,000.00 USD | 18,620,000.00 USD | 15,620.00 USD | 7,410.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2971` | 18,580,000.00 USD | 18,580,000.00 USD | 19,710.00 USD | 7,550.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2977` | 18,540,000.00 USD | 18,540,000.00 USD | 17,630.00 USD | 6,840.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,830,000.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 18,510,000.00 USD | 18,510,000.00 USD | 109,110.00 USD | 18,870.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,740,000.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 244.47 USD | 130,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,580,000.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2989` | 18,350,000.00 USD | 18,350,000.00 USD | 55,860.00 USD | 8,480.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,480,000.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2995` | 18,270,000.00 USD | 18,270,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 18,270,000.00 USD | 18,270,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 12,010.00 USD | 122,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 110,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3031` | 18,210,000.00 USD | 18,210,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 693.50 USD | 110,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3043` | 18,210,000.00 USD | 18,210,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,540.00 USD | 109,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 18,160,000.00 USD | 18,160,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,440,000.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 18,080,000.00 USD | 18,080,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,440,000.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 103,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 0.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,440,000.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 98,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 17,960,000.00 USD | 17,960,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,440,000.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,440,000.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 17,870,000.00 USD | 17,870,000.00 USD | 23,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,430,000.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 17,850,000.00 USD | 17,850,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,430,000.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,420,000.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 17,850,000.00 USD | 17,850,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 83,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,420,000.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 17,830,000.00 USD | 17,830,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,420,000.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3097` | 17,830,000.00 USD | 17,830,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 17,830,000.00 USD | 17,830,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,420,000.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,420,000.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 304.34 USD | 77,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,420,000.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,410,000.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,770.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 17,710,000.00 USD | 17,710,000.00 USD | 2,360.00 USD | 3,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,410,000.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,400,000.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 17,710,000.00 USD | 17,710,000.00 USD | 252.10 USD | 0.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,390,000.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,080.00 USD | 59,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 17,680,000.00 USD | 17,680,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,390,000.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,390,000.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 17,680,000.00 USD | 17,680,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 1,220.00 USD | 14,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,160,000.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3151` | 17,680,000.00 USD | 17,680,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,030,000.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,820,000.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 13,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 17,680,000.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,610,000.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 17,670,000.00 USD | 17,670,000.00 USD | 78,560.00 USD | 24,840.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,070,000.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3169` | 17,530,000.00 USD | 17,530,000.00 USD | 87,450.00 USD | 20,120.00 USD | 40,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,090,000.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 17,380,000.00 USD | 17,380,000.00 USD | 20,240.00 USD | 18,720.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,610,000.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,530,000.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 17,330,000.00 USD | 17,330,000.00 USD | 380,600.00 USD | 66,490.00 USD | 103,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,210,000.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 16,780,000.00 USD | 16,780,000.00 USD | 180,660.00 USD | 22,910.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,500,000.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,340,000.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 16,540,000.00 USD | 16,540,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 16,490,000.00 USD | 16,490,000.00 USD | 94,420.00 USD | 12,550.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,260,000.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 16,360,000.00 USD | 16,360,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,050,000.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,550,000.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,260,000.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 16,110,000.00 USD | 16,110,000.00 USD | 118,230.00 USD | 13,780.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,840,000.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 15,820,000.00 USD | 15,820,000.00 USD | 157,520.00 USD | 87,110.00 USD | 211,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,150,000.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 15,360,000.00 USD | 15,360,000.00 USD | 136,920.00 USD | 85,600.00 USD | 173,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,080,000.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,200,000.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 14,970,000.00 USD | 14,970,000.00 USD | 40,480.00 USD | 46,100.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,610,000.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 14,770,000.00 USD | 14,770,000.00 USD | 423,530.00 USD | 146,030.00 USD | 274,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,270,000.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,380,000.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 13,930,000.00 USD | 13,930,000.00 USD | 873,130.00 USD | 93,570.00 USD | 268,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3259` | 12,690,000.00 USD | 12,690,000.00 USD | 46,420.00 USD | 42,480.00 USD | 202,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3265` | 129.62 USD | 129.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3271` | 12,260,000.00 USD | 12,260,000.00 USD | 161,520.00 USD | 73,710.00 USD | 135,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3277` | 11,890,000.00 USD | 11,890,000.00 USD | 125,690.00 USD | 23,970.00 USD | 80,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3289` | 11,660,000.00 USD | 11,660,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3307` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 13,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 11,440,000.00 USD | 11,440,000.00 USD | 234,580.00 USD | 121,210.00 USD | 329,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 10,760,000.00 USD | 10,760,000.00 USD | 158,550.00 USD | 32,400.00 USD | 211,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 10,360,000.00 USD | 10,360,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3331` | 10,020,000.00 USD | 10,020,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3337` | 10,020,000.00 USD | 10,020,000.00 USD | 147,860.00 USD | 113,790.00 USD | 573,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3343` | 9,190,000.00 USD | 9,190,000.00 USD | 75,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3349` | 9,110,000.00 USD | 9,110,000.00 USD | 158,400.00 USD | 16,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3355` | 8,880,000.00 USD | 8,880,000.00 USD | 91,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3361` | 8,790,000.00 USD | 8,790,000.00 USD | 77,430.00 USD | 0.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3367` | 8,640,000.00 USD | 8,640,000.00 USD | 46,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3373` | 8,600,000.00 USD | 8,600,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3379` | 8,590,000.00 USD | 8,590,000.00 USD | 292,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3385` | 8,300,000.00 USD | 8,300,000.00 USD | 79,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3391` | 8,220,000.00 USD | 8,220,000.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3403` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 117,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3405` | 10,680.00 USD | 10,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3409` | 8,100,000.00 USD | 8,100,000.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3415` | 8,100,000.00 USD | 8,100,000.00 USD | 198,430.00 USD | 0.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3421` | 7,830,000.00 USD | 7,830,000.00 USD | 174,120.00 USD | 0.00 USD | 119,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3427` | 7,540,000.00 USD | 7,540,000.00 USD | 66,290.00 USD | 18,020.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3433` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 44,190.00 USD | 176,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 10,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3439` | 7,050,000.00 USD | 7,050,000.00 USD | 295,580.00 USD | 48,730.00 USD | 392,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3445` | 6,310,000.00 USD | 6,310,000.00 USD | 291,770.00 USD | 106,440.00 USD | 217,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 611.49 USD | 11,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3451` | 5,700,000.00 USD | 5,700,000.00 USD | 121,080.00 USD | 113,420.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3457` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 21,670.00 USD | 258,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3469` | 4,950,000.00 USD | 4,950,000.00 USD | 163,220.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3475` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 86,040.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 1,700.00 USD | 13,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3481` | 4,290,000.00 USD | 4,290,000.00 USD | 233,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3487` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 125,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3493` | 3,940,000.00 USD | 3,940,000.00 USD | 348,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3499` | 3,590,000.00 USD | 3,590,000.00 USD | 132,580.00 USD | 36,040.00 USD | 375,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3505` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 88,380.00 USD | 352,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 212.40 USD | 13,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3511` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 68,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 3,720.00 USD | 17,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3517` | 2,530,000.00 USD | 2,530,000.00 USD | 151,490.00 USD | 117,900.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3523` | 1,830,000.00 USD | 1,830,000.00 USD | 242,170.00 USD | 226,830.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3529` | 900,730.00 USD | 900,730.00 USD | 0.00 USD | 0.00 USD | 406,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 17,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3541` | 494,430.00 USD | 494,430.00 USD | 0.00 USD | 0.00 USD | 494,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3605` | 20,520.00 USD | 37,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 1,220.00 USD | 1,220.00 USD | 1,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 2,220.00 USD | 2,220.00 USD | 999.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 2,330.00 USD | 2,330.00 USD | 113.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 2,440.00 USD | 2,440.00 USD | 102.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 485,640.00 USD | 485,640.00 USD | 483,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 1,380,000.00 USD | 1,380,000.00 USD | 36,990.00 USD | 124,420.00 USD | 728,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 38,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 1,510,000.00 USD | 1,510,000.00 USD | 134,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 2,680,000.00 USD | 2,680,000.00 USD | 601,120.00 USD | 97,460.00 USD | 476,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 3,570,000.00 USD | 3,570,000.00 USD | 259,500.00 USD | 187,170.00 USD | 434,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 38,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 4,490,000.00 USD | 4,490,000.00 USD | 242,170.00 USD | 226,830.00 USD | 459,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 5,070,000.00 USD | 5,070,000.00 USD | 5,540.00 USD | 48,350.00 USD | 517,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3679` | 5,100,000.00 USD | 5,100,000.00 USD | 13,540.00 USD | 3,410.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 5,920,000.00 USD | 5,920,000.00 USD | 326,450.00 USD | 0.00 USD | 494,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3691` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 49,680.00 USD | 336,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 6,480,000.00 USD | 6,480,000.00 USD | 116,970.00 USD | 0.00 USD | 62,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 6,660,000.00 USD | 6,660,000.00 USD | 174,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3709` | 6,730,000.00 USD | 6,730,000.00 USD | 66,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3715` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 62,210.00 USD | 391,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 52,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3727` | 8,010,000.00 USD | 8,010,000.00 USD | 327,290.00 USD | 20,750.00 USD | 434,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 8,480,000.00 USD | 8,480,000.00 USD | 94,310.00 USD | 116,960.00 USD | 254,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3739` | 8,950,000.00 USD | 8,950,000.00 USD | 122,210.00 USD | 113,420.00 USD | 229,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 9,330,000.00 USD | 9,330,000.00 USD | 30,710.00 USD | 33,910.00 USD | 315,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3745` | 6,690.00 USD | 45,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3751` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 7,200.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3757` | 9,640,000.00 USD | 9,640,000.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3763` | 9,990,000.00 USD | 9,990,000.00 USD | 164,680.00 USD | 24,840.00 USD | 159,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3769` | 10,010,000.00 USD | 10,010,000.00 USD | 19,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 537.85 USD | 45,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3787` | 10,010,000.00 USD | 10,010,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3793` | 10,120,000.00 USD | 10,120,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 603,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3799` | 10,130,000.00 USD | 10,130,000.00 USD | 846.48 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3805` | 10,130,000.00 USD | 10,130,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3815` | 285.74 USD | 603,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3823` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 3,950.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3829` | 10,150,000.00 USD | 10,150,000.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3835` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 6,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 603,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3871` | 10,200,000.00 USD | 10,200,000.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 6,280.00 USD | 610,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 615,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3907` | 10,250,000.00 USD | 10,250,000.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 615,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3919` | 10,320,000.00 USD | 10,320,000.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3925` | 10,400,000.00 USD | 10,400,000.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3931` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3937` | 10,560,000.00 USD | 10,560,000.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3943` | 10,770,000.00 USD | 10,770,000.00 USD | 57,010.00 USD | 0.00 USD | 157,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 1,490.00 USD | 617,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3949` | 10,900,000.00 USD | 10,900,000.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3955` | 11,100,000.00 USD | 11,100,000.00 USD | 56,420.00 USD | 48,220.00 USD | 93,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 735,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3961` | 11,200,000.00 USD | 11,200,000.00 USD | 3,050.00 USD | 10,290.00 USD | 86,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3967` | 11,200,000.00 USD | 11,200,000.00 USD | 84.31 USD | 870.52 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3973` | 11,320,000.00 USD | 11,320,000.00 USD | 7,550.00 USD | 2,200.00 USD | 103,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3979` | 11,520,000.00 USD | 11,520,000.00 USD | 114,110.00 USD | 15,920.00 USD | 75,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3985` | 11,530,000.00 USD | 11,530,000.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4003` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4009` | 11,550,000.00 USD | 11,550,000.00 USD | 6,770.00 USD | 2,610.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.4056` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 4,650.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4105` | 4,380.00 USD | 739,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4145` | 278.13 USD | 740,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 167.40 USD | 740,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4385` | 71,380.00 USD | 811,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 812,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 103.98 USD | 812,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 813,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 818,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 819,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5455` | 18,760.00 USD | 838,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 838,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 729,840.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `1D` | `0.2959` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 955.10 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.2965` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 14,320.00 USD | 6,710.00 USD | 12,310.00 USD |
| `1D` | `0.2971` | 21,670,000.00 USD | 0.00 USD | 21,670,000.00 USD | 19,710.00 USD | 7,550.00 USD | 17,420.00 USD |
| `1D` | `0.2977` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 17,630.00 USD | 6,840.00 USD | 7,910.00 USD |
| `7D` | `0.2979` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 70,110.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 109,110.00 USD | 18,870.00 USD | 33,390.00 USD |
| `7D` | `0.2983` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 117,250.00 USD | 10,950.00 USD | 36,400.00 USD |
| `7D` | `0.2987` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `1D` | `0.2989` | 21,430,000.00 USD | 0.00 USD | 21,430,000.00 USD | 55,860.00 USD | 8,480.00 USD | 12,730.00 USD |
| `7D` | `0.2991` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `1D` | `0.2995` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD |
| `1D` | `0.3007` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 18,160.00 USD | 8,430.00 USD | 16,090.00 USD |
| `1D` | `0.3019` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD |
| `1D` | `0.3031` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 275.03 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3043` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 0.00 USD | 17,840.00 USD | 27,080.00 USD |
| `1D` | `0.3049` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 31,710.00 USD | 6,480.00 USD | 42,260.00 USD |
| `7D` | `0.3051` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3055` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 18,570.00 USD | 10,520.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 21,100,000.00 USD | 0.00 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 56,460.00 USD |
| `7D` | `0.3063` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 21,050,000.00 USD | 0.00 USD | 21,050,000.00 USD | 31,170.00 USD | 19,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3073` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 23,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 20,940,000.00 USD | 0.00 USD | 20,940,000.00 USD | 504.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3085` | 20,940,000.00 USD | 0.00 USD | 20,940,000.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 20,920,000.00 USD | 0.00 USD | 20,920,000.00 USD | 638.93 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 20,920,000.00 USD | 0.00 USD | 20,920,000.00 USD | 771.87 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3103` | 20,920,000.00 USD | 0.00 USD | 20,920,000.00 USD | 54,040.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3107` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 2,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 20,800,000.00 USD | 0.00 USD | 20,800,000.00 USD | 2,360.00 USD | 3,950.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,400,000.00 USD | 0.00 USD | 12,400,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3133` | 20,790,000.00 USD | 0.00 USD | 20,790,000.00 USD | 252.10 USD | 0.00 USD | 21,520.00 USD |
| `7D` | `0.3135` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 20,770,000.00 USD | 0.00 USD | 20,770,000.00 USD | 1,010.00 USD | 6,500.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3145` | 20,770,000.00 USD | 0.00 USD | 20,770,000.00 USD | 992.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 101,940.00 USD | 16,380.00 USD | 10,680.00 USD |
| `1D` | `0.3151` | 20,760,000.00 USD | 0.00 USD | 20,760,000.00 USD | 215.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 149,140.00 USD | 37,570.00 USD | 17,280.00 USD |
| `1D` | `0.3157` | 20,760,000.00 USD | 0.00 USD | 20,760,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 334,950.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 20,750,000.00 USD | 0.00 USD | 20,750,000.00 USD | 74,190.00 USD | 23,090.00 USD | 31,430.00 USD |
| `7D` | `0.3163` | 11,070,000.00 USD | 0.00 USD | 11,070,000.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `7D` | `0.3167` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3169` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 87,450.00 USD | 20,120.00 USD | 40,860.00 USD |
| `7D` | `0.3171` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 20,480,000.00 USD | 0.00 USD | 20,480,000.00 USD | 20,240.00 USD | 18,720.00 USD | 14,330.00 USD |
| `7D` | `0.3175` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `7D` | `0.3179` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3181` | 20,420,000.00 USD | 0.00 USD | 20,420,000.00 USD | 381,030.00 USD | 66,490.00 USD | 103,190.00 USD |
| `7D` | `0.3183` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 574,820.00 USD | 53,700.00 USD | 82,240.00 USD |
| `1D` | `0.3187` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 180,660.00 USD | 22,910.00 USD | 34,760.00 USD |
| `7D` | `0.3187` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `1D` | `0.3193` | 19,630,000.00 USD | 0.00 USD | 19,630,000.00 USD | 0.00 USD | 3,120.00 USD | 0.00 USD |
| `1D` | `0.3199` | 19,630,000.00 USD | 0.00 USD | 19,630,000.00 USD | 47,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3205` | 19,580,000.00 USD | 0.00 USD | 19,580,000.00 USD | 158,590.00 USD | 12,550.00 USD | 23,180.00 USD |
| `7D` | `0.3207` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `1D` | `0.3211` | 19,390,000.00 USD | 0.00 USD | 19,390,000.00 USD | 35,150.00 USD | 11,980.00 USD | 115,350.00 USD |
| `7D` | `0.3211` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `1D` | `0.3217` | 19,230,000.00 USD | 0.00 USD | 19,230,000.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `7D` | `0.3219` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3223` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 118,640.00 USD | 13,780.00 USD | 157,050.00 USD |
| `7D` | `0.3223` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3229` | 18,850,000.00 USD | 0.00 USD | 18,850,000.00 USD | 148,780.00 USD | 83,610.00 USD | 211,400.00 USD |
| `7D` | `0.3231` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 18,410,000.00 USD | 0.00 USD | 18,410,000.00 USD | 136,920.00 USD | 85,600.00 USD | 173,670.00 USD |
| `7D` | `0.3235` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `7D` | `0.3239` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3241` | 18,010,000.00 USD | 0.00 USD | 18,010,000.00 USD | 41,450.00 USD | 46,100.00 USD | 109,920.00 USD |
| `7D` | `0.3243` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 17,810,000.00 USD | 0.00 USD | 17,810,000.00 USD | 568,770.00 USD | 146,030.00 USD | 274,600.00 USD |
| `7D` | `0.3247` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `7D` | `0.3251` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3253` | 16,820,000.00 USD | 0.00 USD | 16,820,000.00 USD | 873,130.00 USD | 121,930.00 USD | 375,230.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `1D` | `0.3259` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 101,780.00 USD | 42,480.00 USD | 202,260.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3265` | 15,110,000.00 USD | 0.00 USD | 15,110,000.00 USD | 0.00 USD | 30,260.00 USD | 141,160.00 USD |
| `1D` | `0.3271` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 161,520.00 USD | 73,710.00 USD | 227,940.00 USD |
| `1D` | `0.3277` | 14,470,000.00 USD | 0.00 USD | 14,470,000.00 USD | 213,460.00 USD | 23,970.00 USD | 196,110.00 USD |
| `1D` | `0.3283` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 32,250.00 USD | 0.00 USD |
| `1D` | `0.3289` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 84,680.00 USD | 0.00 USD | 115,570.00 USD |
| `1D` | `0.3295` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 977.29 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.3307` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 0.00 USD | 13,130.00 USD | 87,100.00 USD |
| `1D` | `0.3313` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 234,580.00 USD | 121,210.00 USD | 329,260.00 USD |
| `7D` | `0.3315` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3319` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 158,550.00 USD | 32,400.00 USD | 295,390.00 USD |
| `1D` | `0.3325` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 93,690.00 USD | 52,610.00 USD | 188,720.00 USD |
| `1D` | `0.3331` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 855.55 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3337` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 147,860.00 USD | 113,790.00 USD | 573,250.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `1D` | `0.3343` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 76,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `1D` | `0.3349` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 158,400.00 USD | 16,250.00 USD | 59,820.00 USD |
| `7D` | `0.3351` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 307,930.00 USD | 61,830.00 USD | 47,940.00 USD |
| `1D` | `0.3355` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 93,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3355` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `7D` | `0.3359` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 600,750.00 USD | 199,800.00 USD | 227,150.00 USD |
| `1D` | `0.3361` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 79,180.00 USD | 0.00 USD | 65,250.00 USD |
| `7D` | `0.3363` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 46,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3367` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `7D` | `0.3371` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3373` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 7,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3375` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 292,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3379` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 594,480.00 USD | 90,270.00 USD | 196,520.00 USD |
| `7D` | `0.3383` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 826,800.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3385` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 79,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `1D` | `0.3391` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 1,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3391` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3397` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 858.77 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3403` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 1,240.00 USD | 0.00 USD | 117,320.00 USD |
| `7D` | `0.3403` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `1D` | `0.3409` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3411` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `1D` | `0.3415` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 358,860.00 USD | 0.00 USD | 62,690.00 USD |
| `7D` | `0.3415` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 23,220.00 USD |
| `7D` | `0.3419` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 154,360.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3421` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 176,460.00 USD | 0.00 USD | 119,640.00 USD |
| `7D` | `0.3423` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 312,710.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 66,290.00 USD | 18,020.00 USD | 187,820.00 USD |
| `7D` | `0.3427` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 225,120.00 USD | 112,010.00 USD | 134,250.00 USD |
| `7D` | `0.3431` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3433` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 0.00 USD | 44,190.00 USD | 176,350.00 USD |
| `7D` | `0.3435` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 388,780.00 USD | 48,730.00 USD | 392,630.00 USD |
| `7D` | `0.3439` | 11,110,000.00 USD | 11,110,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `7D` | `0.3443` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 231,050.00 USD | 40,270.00 USD | 53,150.00 USD |
| `1D` | `0.3445` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 291,770.00 USD | 106,440.00 USD | 217,030.00 USD |
| `7D` | `0.3447` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 378,020.00 USD | 36,640.00 USD | 68,590.00 USD |
| `1D` | `0.3451` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 121,080.00 USD | 139,630.00 USD | 229,860.00 USD |
| `7D` | `0.3451` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `7D` | `0.3455` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3457` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 1,150.00 USD | 21,670.00 USD | 258,740.00 USD |
| `7D` | `0.3459` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 363,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3469` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 163,220.00 USD | 70,910.00 USD | 514,270.00 USD |
| `7D` | `0.3471` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 138,390.00 USD | 86,040.00 USD | 159,850.00 USD |
| `7D` | `0.3475` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 3,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3481` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 233,940.00 USD | 32,810.00 USD | 0.00 USD |
| `1D` | `0.3487` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 320,850.00 USD | 75,650.00 USD | 356,270.00 USD |
| `7D` | `0.3491` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3493` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 567,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3499` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 132,580.00 USD | 116,660.00 USD | 664,810.00 USD |
| `7D` | `0.3503` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 1,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3505` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 88,380.00 USD | 352,700.00 USD |
| `7D` | `0.3507` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 68,910.00 USD | 334,230.00 USD |
| `7D` | `0.3511` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3517` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 0.00 USD | 117,900.00 USD | 434,060.00 USD |
| `7D` | `0.3519` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 279,270.00 USD | 459,710.00 USD |
| `7D` | `0.3523` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3529` | 624,060.00 USD | 0.00 USD | 624,060.00 USD | 0.00 USD | 0.00 USD | 624,060.00 USD |
| `7D` | `0.3531` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3533` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3541` | 846,520.00 USD | 846,520.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 704,710.00 USD |
| `1D` | `0.3547` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 534,120.00 USD |
| `1D` | `0.3553` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 65,630.00 USD | 0.00 USD |
| `1D` | `0.3559` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 151,290.00 USD | 461,790.00 USD |
| `1D` | `0.3571` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 161,260.00 USD | 578,320.00 USD |
| `1D` | `0.3583` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 268,150.00 USD |
| `1D` | `0.3589` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 400,320.00 USD |
| `7D` | `0.3599` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `7D` | `0.3615` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `7D` | `0.3619` | 12,810,000.00 USD | 12,810,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `7D` | `0.3623` | 12,960,000.00 USD | 12,960,000.00 USD | 0.00 USD | 81,760.00 USD | 32,570.00 USD | 36,370.00 USD |
| `7D` | `0.3627` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 320,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3631` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `7D` | `0.3635` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `7D` | `0.3639` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `7D` | `0.3643` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 89,900.00 USD | 9,390.00 USD | 22,010.00 USD |
| `7D` | `0.3647` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `7D` | `0.3651` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |
| `1D` | `0.3655` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 186,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3661` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 259,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3667` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 242,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3673` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 5,540.00 USD | 48,350.00 USD | 0.00 USD |
| `1D` | `0.3679` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 739,750.00 USD | 3,410.00 USD | 0.00 USD |
| `1D` | `0.3685` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 326,450.00 USD | 141,810.00 USD | 0.00 USD |
| `1D` | `0.3691` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 276,770.00 USD | 49,680.00 USD | 0.00 USD |
| `1D` | `0.3697` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 116,970.00 USD | 65,630.00 USD | 0.00 USD |
| `1D` | `0.3703` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 334,820.00 USD | 151,290.00 USD | 0.00 USD |
| `1D` | `0.3709` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 67,590.00 USD | 0.00 USD | 461,790.00 USD |
| `1D` | `0.3715` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 438,840.00 USD | 62,210.00 USD | 969,570.00 USD |
| `1D` | `0.3721` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 213,550.00 USD | 0.00 USD |
| `1D` | `0.3727` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 420,490.00 USD | 20,750.00 USD | 703,030.00 USD |
| `1D` | `0.3733` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 94,310.00 USD | 116,960.00 USD | 655,100.00 USD |
| `1D` | `0.3739` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 122,210.00 USD | 139,630.00 USD | 229,860.00 USD |
| `1D` | `0.3745` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 30,710.00 USD | 33,910.00 USD | 315,200.00 USD |
| `1D` | `0.3751` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 363,100.00 USD | 7,200.00 USD | 471,200.00 USD |
| `1D` | `0.3757` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 23,190.00 USD | 0.00 USD | 247,210.00 USD |
| `1D` | `0.3763` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 304,310.00 USD | 95,750.00 USD | 847,470.00 USD |
| `1D` | `0.3769` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 20,560.00 USD | 32,810.00 USD | 0.00 USD |
| `1D` | `0.3775` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 0.00 USD | 75,650.00 USD | 0.00 USD |
| `1D` | `0.3781` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 2,330.00 USD | 0.00 USD | 230,890.00 USD |
| `1D` | `0.3787` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 220,030.00 USD | 0.00 USD | 289,160.00 USD |
| `1D` | `0.3793` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 54,040.00 USD | 96,440.00 USD | 46,470.00 USD |
| `1D` | `0.3799` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 846.48 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3805` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 855.55 USD | 0.00 USD | 334,230.00 USD |
| `1D` | `0.3823` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 2,080.00 USD | 3,950.00 USD | 239,270.00 USD |
| `1D` | `0.3829` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 1,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3835` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 6,500.00 USD | 210,280.00 USD |
| `1D` | `0.3841` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 850.22 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3847` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 899.18 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3871` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 43,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3883` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 1,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3907` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 46,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3913` | 16,220,000.00 USD | 16,220,000.00 USD | 0.00 USD | 64,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3919` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 70,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3925` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 380.43 USD | 0.00 USD | 75,130.00 USD |
| `1D` | `0.3931` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 17,680.00 USD | 70,540.00 USD |
| `1D` | `0.3937` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 61,560.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.3943` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 57,430.00 USD | 0.00 USD | 157,050.00 USD |
| `1D` | `0.3949` | 16,870,000.00 USD | 16,870,000.00 USD | 0.00 USD | 441.41 USD | 37,760.00 USD | 91,180.00 USD |
| `1D` | `0.3955` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 56,420.00 USD | 47,870.00 USD | 93,620.00 USD |
| `1D` | `0.3961` | 17,170,000.00 USD | 17,170,000.00 USD | 0.00 USD | 4,020.00 USD | 10,290.00 USD | 86,890.00 USD |
| `1D` | `0.3967` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 91,720.00 USD | 870.52 USD | 2,580.00 USD |
| `1D` | `0.3973` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 61,150.00 USD | 2,200.00 USD | 103,990.00 USD |
| `1D` | `0.3979` | 17,830,000.00 USD | 17,830,000.00 USD | 0.00 USD | 169,470.00 USD | 44,290.00 USD | 182,050.00 USD |
| `1D` | `0.3985` | 17,840,000.00 USD | 17,840,000.00 USD | 0.00 USD | 5,260.00 USD | 1,060.00 USD | 4,400.00 USD |
| `1D` | `0.3991` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 0.00 USD | 30,260.00 USD | 0.00 USD |
| `1D` | `0.3997` | 17,960,000.00 USD | 17,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 92,360.00 USD |
| `1D` | `0.4003` | 18,050,000.00 USD | 18,050,000.00 USD | 0.00 USD | 87,770.00 USD | 1,610.00 USD | 0.00 USD |
| `1D` | `0.4009` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 6,770.00 USD | 34,860.00 USD | 123,710.00 USD |
| `1D` | `0.4027` | 18,300,000.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,060.00 USD |
| `1D` | `0.4045` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,100.00 USD |
| `1D` | `0.4057` | 18,490,000.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 8,920.00 USD | 97,650.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `381.48M` | Total OI Tokens: `1,090,122,689.8 TRX`
  * 1h OI Change: `+24.07%` | 4h OI Change: `+28.05%` | 24h OI Change: `+31.20%`
  * Exchange Breakdown: Binance=`111.58M` | Bybit=`81.94M` | OKX=`20.69M` | Hyperliquid=`19.11M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-136.98K` | Last 24h: `9.22K` | Last 3d: `-51.81K` | Last 7d: `-271.17K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0673%` | **USDT OKX** | `-0.1638%` |
| **USDT Bybit** | `-0.0462%` | **USDT KuCoin** | `-0.1084%` |
| **USDT MEXC** | `-0.0619%` | **USDT BingX** | `-0.1256%` |
| **USDT Gate** | `-0.1275%` | **USDT Bitget** | `-0.0594%` |
| **CoinM Binance** | `0.0028%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `47.61%` | `52.39%` | `0.91` | 10,750,000.00 USD |
| `15M` | `Binance` | `44.05%` | `55.95%` | `0.79` | 3,930,000.00 USD |
| `15M` | `OKX` | `44.72%` | `55.28%` | `0.81` | 1,070,000.00 USD |
| `15M` | `Bybit` | `52.77%` | `47.23%` | `1.12` | 1,550,000.00 USD |
| `15M` | `KuCoin` | `36.41%` | `63.59%` | `0.57` | 165,360.00 USD |
| `15M` | `Gate` | `57.75%` | `42.25%` | `1.37` | 358,330.00 USD |
| `15M` | `Bitget` | `37.52%` | `62.48%` | `0.60` | 316,150.00 USD |
| `15M` | `BingX` | `50.66%` | `49.34%` | `1.03` | 138,360.00 USD |
| `15M` | `MEXC` | `36.63%` | `63.37%` | `0.58` | 633,940.00 USD |
| `15M` | `Bitunix` | `35.43%` | `64.57%` | `0.55` | 244,980.00 USD |
| `15M` | `Hyperliquid` | `62.69%` | `37.31%` | `1.68` | 116,720.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.97%` | `48.03%` | `1.08` | 1,850,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `86.2%` | `13.8%` | `6.25` | 260,460.00 USD |
| `15M` | `HTX` | `47.74%` | `52.26%` | `0.91` | 38,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.39%` | `48.61%` | `1.06` | 71,470.00 USD |
| `15M` | `Aster` | `61.3%` | `38.7%` | `1.58` | 1,660.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `24.83%` | `75.17%` | `0.33` | 8,860.00 USD |
| `15M` | `Whale Positions` | `44.05%` | `55.95%` | `0.79` | 3,930,000.00 USD |
| `15M` | `Global Accounts` | `47.61%` | `52.39%` | `0.91` | 10,750,000.00 USD |
| `1H` | `TRX` | `44.64%` | `55.36%` | `0.81` | 65,770,000.00 USD |
| `1H` | `Binance` | `47.92%` | `52.08%` | `0.92` | 20,990,000.00 USD |
| `1H` | `OKX` | `50.54%` | `49.46%` | `1.02` | 5,010,000.00 USD |
| `1H` | `Bybit` | `51.9%` | `48.1%` | `1.08` | 7,610,000.00 USD |
| `1H` | `KuCoin` | `45.33%` | `54.67%` | `0.83` | 483,030.00 USD |
| `1H` | `Gate` | `50.25%` | `49.75%` | `1.01` | 2,760,000.00 USD |
| `1H` | `Bitget` | `51.58%` | `48.42%` | `1.07` | 2,280,000.00 USD |
| `1H` | `BingX` | `12.89%` | `87.11%` | `0.15` | 10,420,000.00 USD |
| `1H` | `MEXC` | `46.48%` | `53.52%` | `0.87` | 3,030,000.00 USD |
| `1H` | `Bitunix` | `55.15%` | `44.85%` | `1.23` | 1,250,000.00 USD |
| `1H` | `Hyperliquid` | `52.52%` | `47.48%` | `1.11` | 578,430.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.02%` | `45.98%` | `1.17` | 9,880,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `75.47%` | `24.53%` | `3.08` | 841,130.00 USD |
| `1H` | `HTX` | `52.26%` | `47.74%` | `1.09` | 116,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `51.3%` | `48.7%` | `1.05` | 475,170.00 USD |
| `1H` | `Aster` | `46.84%` | `53.16%` | `0.88` | 18,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `30.14%` | `69.86%` | `0.43` | 16,750.00 USD |
| `1H` | `Whale Positions` | `47.92%` | `52.08%` | `0.92` | 20,990,000.00 USD |
| `1H` | `Global Accounts` | `44.64%` | `55.36%` | `0.81` | 65,770,000.00 USD |
| `4H` | `TRX` | `46.51%` | `53.49%` | `0.87` | 327,910,000.00 USD |
| `4H` | `Binance` | `46.21%` | `53.79%` | `0.86` | 109,690,000.00 USD |
| `4H` | `OKX` | `48.04%` | `51.96%` | `0.92` | 37,090,000.00 USD |
| `4H` | `Bybit` | `48.14%` | `51.86%` | `0.93` | 34,650,000.00 USD |
| `4H` | `KuCoin` | `50.61%` | `49.39%` | `1.02` | 2,650,000.00 USD |
| `4H` | `Gate` | `50.34%` | `49.66%` | `1.01` | 15,180,000.00 USD |
| `4H` | `Bitget` | `46.75%` | `53.25%` | `0.88` | 24,850,000.00 USD |
| `4H` | `BingX` | `24.06%` | `75.94%` | `0.32` | 17,420,000.00 USD |
| `4H` | `MEXC` | `43.57%` | `56.43%` | `0.77` | 20,190,000.00 USD |
| `4H` | `Bitunix` | `48.54%` | `51.46%` | `0.94` | 7,600,000.00 USD |
| `4H` | `Hyperliquid` | `43.95%` | `56.05%` | `0.78` | 4,510,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.41%` | `46.59%` | `1.15` | 48,880,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `27.72%` | `72.28%` | `0.38` | 2,730,000.00 USD |
| `4H` | `HTX` | `48.11%` | `51.89%` | `0.93` | 539,050.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.26%` | `49.74%` | `1.01` | 1,600,000.00 USD |
| `4H` | `Aster` | `36.54%` | `63.46%` | `0.58` | 237,840.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.31%` | `57.69%` | `0.73` | 112,190.00 USD |
| `4H` | `Whale Positions` | `46.21%` | `53.79%` | `0.86` | 109,690,000.00 USD |
| `4H` | `Global Accounts` | `46.51%` | `53.49%` | `0.87` | 327,910,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3316` | `0.3315` | `0.3316` | `0.3316` | `0.3315` | 97,541.21 USD | 34,795.54 USD | 62,745.67 USD | -27,950.14 USD | `-28.65%` | `4B / 4S` |
| `0:00 UTC` | `0.3311` | `0.3313` | `0.3311` | `0.3316` | `0.3310` | 747,180.14 USD | 373,024.41 USD | 374,155.73 USD | -1,131.33 USD | `-0.15%` | `16B / 17S` |
| `5:00 UTC` | `0.3313` | `0.3314` | `0.3313` | `0.3315` | `0.3312` | 312,440.76 USD | 170,379.42 USD | 142,061.34 USD | 28,318.07 USD | `+9.06%` | `13B / 7S` |
| `0:00 UTC` | `0.3308` | `0.3304` | `0.3308` | `0.3313` | `0.3295` | 3,091,479.93 USD | 681,981.05 USD | 2,409,498.88 USD | -1,727,517.83 USD | `-55.88%` | `20B / 55S` |
| `5:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3363` | `0.3285` | 10,644,567.03 USD | 5,188,760.14 USD | 5,455,806.89 USD | -267,046.75 USD | `-2.51%` | `23B / 18S` |
| `0:00 UTC` | `0.3310` | `0.3345` | `0.3310` | `0.3414` | `0.3283` | 12,234,359.27 USD | 6,873,169.39 USD | 5,361,189.88 USD | 1,511,979.51 USD | `+12.36%` | `29B / 4S` |
| `5:00 UTC` | `0.3410` | `0.3437` | `0.3410` | `0.3496` | `0.3386` | 15,171,697.80 USD | 7,420,251.93 USD | 7,751,445.87 USD | -331,193.94 USD | `-2.18%` | `3B / 6S` |
| `0:00 UTC` | `0.3377` | `0.3416` | `0.3377` | `0.3499` | `0.3361` | 21,787,549.51 USD | 11,969,195.40 USD | 9,818,354.10 USD | 2,150,841.30 USD | `+9.87%` | `13B / 4S` |
| `5:00 UTC` | `0.3600` | `0.3572` | `0.3600` | `0.3651` | `0.3467` | 44,541,588.04 USD | 22,230,180.93 USD | 22,311,407.11 USD | -81,226.19 USD | `-0.18%` | `8B / 6S` |
| `0:00 UTC` | `0.3620` | `0.3613` | `0.3620` | `0.3636` | `0.3595` | 6,344,628.91 USD | 3,286,890.98 USD | 3,057,737.93 USD | 229,153.05 USD | `+3.61%` | `19B / 11S` |

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
| `5m` | -1,510,000.00 USD | 1,890,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,820,000.00 USD | 1,390,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,660,000.00 USD | 4,940,000.00 USD | **`ACCUMULATION`** |
| `1h` | -2,060,000.00 USD | 7,350,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,730,000.00 USD | 7,650,000.00 USD | **`ACCUMULATION`** |
| `4h` | -3,490,000.00 USD | 8,110,000.00 USD | **`ACCUMULATION`** |
| `6h` | -3,250,000.00 USD | 7,990,000.00 USD | **`ACCUMULATION`** |
| `8h` | -3,610,000.00 USD | 8,150,000.00 USD | **`ACCUMULATION`** |
| `12h` | -3,460,000.00 USD | 8,280,000.00 USD | **`ACCUMULATION`** |
| `24h` | -431,710.00 USD | 11,030,000.00 USD | **`ACCUMULATION`** |
| `1w` | -7,700,000.00 USD | 8,690,000.00 USD | **`ACCUMULATION`** |
| `30d` | -26,820,000.00 USD | 11,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.51M` | 15m=`-1.82M` | 1h=`-2.06M` | 24h=`-431.71K`
* Futures Capital Netflows: 5m=`+1.89M` | 15m=`+1.39M` | 1h=`+7.35M` | 24h=`+11.03M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3342` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.8733` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `3.35`
  * Mathematical Lot Sizing: **`8.28 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3532` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.56` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `-2.67`
  * Mathematical Lot Sizing: **`8.28 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3596`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
