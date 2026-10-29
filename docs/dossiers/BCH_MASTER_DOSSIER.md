# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 04:41:04 IST` (`2026-10-29 23:11:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `275.76` | **Live Ask Quote**: `276.24` | **Mid Price**: `276.00`
- **Spread Points**: `481.00` | **Spread BPS**: `17.43 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `280.93` | VWAP Z-Score: `-0.71` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.02` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `42.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.92` | Lower -3.00σ Band: `265.93`
  * Upper +2.51σ Band: `293.47` | Lower -2.51σ Band: `268.38`
  * Upper +2.01σ Band: `290.97` | Lower -2.01σ Band: `270.88`
  * Upper +2.00σ Band: `290.92` | Lower -2.00σ Band: `270.93`
  * Upper +1.28σ Band: `287.32` | Lower -1.28σ Band: `274.53`
  * Upper +1.00σ Band: `285.92` | Lower -1.00σ Band: `275.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`277.28` | EMA-20=`279.45` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`281.35` (Slope: `+0.0000`) | EMA-100=`282.80`
  * Institutional Anchors: EMA-144=`283.53` | EMA-200=`284.09` (Slope: `-0.3399`) | EMA-233=`284.77`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`269.53` | Weekly High=`304.16` | Weekly Low=`269.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.58` (Distance: `-0.87%`)
  * Point of Control (POC) = `276.81` (Distance: `-0.24%`)
  * Value Area Low (VAL) = `275.10` (Distance: `+0.38%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.04` | Weekly POC=`278.88` | Weekly VAL=`274.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`279.40` | Low=`270.25`
  * London Session (08:00-16:00 UTC): High=`277.10` | Low=`274.90`
  * New York Session (13:00-21:00 UTC): High=`277.66` | Low=`274.34`
  * Initial Balance (First Hour): IB High=`276.83` | IB Low=`275.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `274.90` - `277.10`
  * Optimal Trade Entry (OTE 0.705): `276.55`
  * Structural Invalidation Anchor (0.786): `278.21`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `277.62` | `278.32` | `277.48` | `277.89` | `1,002` | 278,559.28 USD | -12,019.89 USD | `-4.32%` | -3,778,645.91 USD | `-0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `277.86` | `278.42` | `276.46` | `276.55` | `2,390` | 662,715.83 USD | -253,519.14 USD | `-38.25%` | -4,032,165.05 USD | `-0.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `276.54` | `276.70` | `276.30` | `276.31` | `688` | 190,269.52 USD | -54,938.22 USD | `-28.87%` | -4,087,103.27 USD | `-0.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `277.44` | `279.46` | `277.00` | `277.36` | `4,049` | 1,126,883.43 USD | -162,716.03 USD | `-14.44%` | -3,611,210.18 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `277.34` | `278.32` | `276.60` | `277.89` | `4,058` | 1,125,978.55 USD | -175,712.36 USD | `-15.61%` | -3,786,922.54 USD | `-0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `277.86` | `278.42` | `276.30` | `276.31` | `3,078` | 852,985.35 USD | -308,457.37 USD | `-36.16%` | -4,095,379.91 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `270.43` | `280.00` | `269.74` | `276.50` | `41,918` | 11,558,813.69 USD | 153,675.96 USD | `+1.33%` | -3,649,872.10 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `276.48` | `279.46` | `273.98` | `277.89` | `29,021` | 8,047,324.82 USD | 57,900.23 USD | `+0.72%` | -3,591,971.87 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `277.86` | `278.42` | `276.30` | `276.38` | `3,086` | 855,124.15 USD | -309,194.47 USD | `-36.16%` | -3,901,166.35 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `276.36` | `152,773` | 42,308,531.99 USD | -489,595.52 USD | `-1.16%` | -3,899,853.32 USD | `+0.12` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `276.36` | `152,773` | 42,308,531.99 USD | -489,595.52 USD | `-1.16%` | -3,899,853.32 USD | `+0.12` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`276.00`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1997` | `0x12d2...f97f` | `LONG` | 1,002,170.97 USD | `3,627,243,000,000.00` | `303.26` | `276.49` | `0.000000` | -97,828.37 USD | `-9.76%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `283.81` | 394.50 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Short: 0.39K USD at 283.8100 USD [API] | `2026-10-28 17:26:15` |
| `ANNOUNCEMENT` | `INFO` | `284.26` | 6,655.10 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 6.66K USD at 284.2600 USD [API] | `2026-10-28 18:08:29` |
| `ANNOUNCEMENT` | `INFO` | `285.30` | 6,679.16 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.68K USD at 285.3000 USD [API] | `2026-10-28 18:36:16` |
| `ANNOUNCEMENT` | `INFO` | `301.89` | 1,148.69 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Long: 1.15K USD at 301.8900 USD [API] | `2026-10-28 09:30:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`284.69` (Vol: 134,100.00 USD, Dist: `+2.41%`) | Long MP=`273.57` (Vol: 134,100.00 USD, Dist: `--1.59%`)
  * 48H Horizon: Short MP=`294.42` (Vol: 176,100.00 USD, Dist: `+5.91%`) | Long MP=`273.65` (Vol: 134,100.00 USD, Dist: `--1.56%`)
  * 3D Horizon: Short MP=`294.42` (Vol: 176,100.00 USD, Dist: `+5.91%`) | Long MP=`273.65` (Vol: 134,100.00 USD, Dist: `--1.56%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+5.89%`) | Long MP=`263.68` (Vol: 277,800.00 USD, Dist: `--5.15%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `66.50` | 251.37 USD | 434,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 541.71 USD | 433,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 433,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 432,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 426,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 422,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 1,450.00 USD | 421,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 420,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 175.66 USD | 420,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 420,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 856.66 USD | 419,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `131.50` | 1,970.00 USD | 419,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `141.50` | 157.49 USD | 417,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 417,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 416,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 414,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 2,130.00 USD | 412,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `154.50` | 1,540.00 USD | 410,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 408,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 8,660.00 USD | 408,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `169.50` | 367.31 USD | 399,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 399,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 399,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 904.53 USD | 398,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 397,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `181.50` | 1,990.00 USD | 397,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 191.57 USD | 395,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 395,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 394,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 394,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 393,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 392,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 391,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 391,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 390,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `203.50` | 610.50 USD | 390,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 39,880.00 USD | 389,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 349,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `207.50` | 188,820.00 USD | 349,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 6,740.00 USD | 160,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 9,340.00 USD | 154,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 2,610.00 USD | 144,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 528.56 USD | 142,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 1,650.00 USD | 141,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 140,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 561.25 USD | 107,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `225.50` | 5,370.00 USD | 106,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 101,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 288.24 USD | 99,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 1,260.00 USD | 99,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,190.00 USD | 98,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 506.06 USD | 97,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 429.66 USD | 96,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `233.50` | 6,090.00 USD | 96,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 90,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,640.00 USD | 90,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.90` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.40` | 12,350,000.00 USD | 12,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 88,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 12,340,000.00 USD | 12,340,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 12,320,000.00 USD | 12,320,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 88,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.90` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.40` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `243.50` | 4,740,000.00 USD | 4,740,000.00 USD | 583.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 86,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `243.90` | 4,730,000.00 USD | 4,730,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.90` | 12,240,000.00 USD | 12,240,000.00 USD | 781.30 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 28,760.00 USD | 85,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `244.70` | 4,730,000.00 USD | 4,730,000.00 USD | 638.70 USD | 5,270.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.90` | 12,220,000.00 USD | 12,220,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.40` | 12,200,000.00 USD | 12,200,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `245.50` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 56,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `245.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 6.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.90` | 12,180,000.00 USD | 12,180,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.30` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 5,540.00 USD | 6.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 12,160,000.00 USD | 12,160,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.70` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.90` | 12,130,000.00 USD | 12,130,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.10` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.40` | 12,120,000.00 USD | 12,120,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.50` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 1,330.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.90` | 4,690,000.00 USD | 4,690,000.00 USD | 528.00 USD | 619.60 USD | 5.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.90` | 12,080,000.00 USD | 12,080,000.00 USD | 789.37 USD | 4,610.00 USD | 3.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.30` | 4,690,000.00 USD | 4,690,000.00 USD | 10,640.00 USD | 1,390.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 12,070,000.00 USD | 12,070,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.70` | 4,650,000.00 USD | 4,650,000.00 USD | 7,480.00 USD | 3,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 12,030,000.00 USD | 12,030,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.10` | 4,640,000.00 USD | 4,640,000.00 USD | 3,780.00 USD | 9,520.00 USD | 31,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.40` | 11,930,000.00 USD | 11,930,000.00 USD | 49,060.00 USD | 28,020.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.50` | 4,590,000.00 USD | 4,590,000.00 USD | 5,170.00 USD | 1,450.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.90` | 4,580,000.00 USD | 4,580,000.00 USD | 13,540.00 USD | 1,330.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 11,850,000.00 USD | 11,850,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.30` | 4,570,000.00 USD | 4,570,000.00 USD | 9,170.00 USD | 5,500.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 11,740,000.00 USD | 11,740,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 54,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.70` | 4,550,000.00 USD | 4,550,000.00 USD | 3,680.00 USD | 9,520.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.90` | 11,670,000.00 USD | 11,670,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.10` | 4,530,000.00 USD | 4,530,000.00 USD | 31,920.00 USD | 39,990.00 USD | 13,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 11,580,000.00 USD | 11,580,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.50` | 4,440,000.00 USD | 4,440,000.00 USD | 7,900.00 USD | 34,360.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 53,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.90` | 4,380,000.00 USD | 4,380,000.00 USD | 49,120.00 USD | 36,870.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 11,410,000.00 USD | 11,410,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.30` | 4,270,000.00 USD | 4,270,000.00 USD | 13,370.00 USD | 7,400.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 11,240,000.00 USD | 11,240,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 53,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.70` | 4,240,000.00 USD | 4,240,000.00 USD | 14,040.00 USD | 5,720.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 11,100,000.00 USD | 11,100,000.00 USD | 29,220.00 USD | 19,580.00 USD | 22.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.10` | 4,220,000.00 USD | 4,220,000.00 USD | 9,570.00 USD | 12,280.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 11,050,000.00 USD | 11,050,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.50` | 4,200,000.00 USD | 4,200,000.00 USD | 19,980.00 USD | 13,820.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.90` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 8,890.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 10,930,000.00 USD | 10,930,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.30` | 4,130,000.00 USD | 4,130,000.00 USD | 144.00 USD | 2,130.00 USD | 3.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 10,860,000.00 USD | 10,860,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 52,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.70` | 4,130,000.00 USD | 4,130,000.00 USD | 994.06 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 10,780,000.00 USD | 10,780,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.10` | 4,120,000.00 USD | 4,120,000.00 USD | 9,680.00 USD | 6,590.00 USD | 19.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 10,730,000.00 USD | 10,730,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.50` | 4,100,000.00 USD | 4,100,000.00 USD | 6,410.00 USD | 6,180.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.90` | 4,090,000.00 USD | 4,090,000.00 USD | 13,380.00 USD | 2,480.00 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 10,650,000.00 USD | 10,650,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.30` | 4,070,000.00 USD | 4,070,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 10,580,000.00 USD | 10,580,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 453.49 USD | 51,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.70` | 4,060,000.00 USD | 4,060,000.00 USD | 9,140.00 USD | 0.00 USD | 8.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 10,450,000.00 USD | 10,450,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.10` | 4,050,000.00 USD | 4,050,000.00 USD | 5,380.00 USD | 928.93 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 10,360,000.00 USD | 10,360,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 4,040,000.00 USD | 4,040,000.00 USD | 918.80 USD | 600.15 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.90` | 4,030,000.00 USD | 4,030,000.00 USD | 3,330.00 USD | 2,390.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 10,280,000.00 USD | 10,280,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 4,010,000.00 USD | 4,010,000.00 USD | 3,380.00 USD | 3,270.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 10,220,000.00 USD | 10,220,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 51,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 4,000,000.00 USD | 4,000,000.00 USD | 2,360.00 USD | 3,080.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 10,000,000.00 USD | 10,000,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 3,990,000.00 USD | 3,990,000.00 USD | 13,030.00 USD | 4,500.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 9,900,000.00 USD | 9,900,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 3,970,000.00 USD | 3,970,000.00 USD | 5,110.00 USD | 2,610.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `259.50` | 5,190.00 USD | 50,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `259.90` | 3,950,000.00 USD | 3,950,000.00 USD | 15,160.00 USD | 15,630.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 9,840,000.00 USD | 9,840,000.00 USD | 19,140.00 USD | 12,520.00 USD | 119.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 3,900,000.00 USD | 3,900,000.00 USD | 3,050.00 USD | 12,260.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 9,810,000.00 USD | 9,810,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 7,590.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 3,880,000.00 USD | 3,880,000.00 USD | 338.15 USD | 5,500.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 9,690,000.00 USD | 9,690,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 3,860,000.00 USD | 3,860,000.00 USD | 8,020.00 USD | 16,510.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 9,570,000.00 USD | 9,570,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 3,800,000.00 USD | 3,800,000.00 USD | 7,870.00 USD | 16,090.00 USD | 18.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 3,770,000.00 USD | 3,770,000.00 USD | 4,770.00 USD | 4,240.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 9,470,000.00 USD | 9,470,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 3,730,000.00 USD | 3,730,000.00 USD | 8,640.00 USD | 4,380.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 9,310,000.00 USD | 9,310,000.00 USD | 44,640.00 USD | 52,560.00 USD | 24.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 3,720,000.00 USD | 3,720,000.00 USD | 366.04 USD | 13,770.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 9,210,000.00 USD | 9,210,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 3,700,000.00 USD | 3,700,000.00 USD | 9,030.00 USD | 4,720.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 9,070,000.00 USD | 9,070,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 3,680,000.00 USD | 3,680,000.00 USD | 913.24 USD | 979.31 USD | 24,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 3,650,000.00 USD | 3,650,000.00 USD | 746.44 USD | 10,060.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 8,890,000.00 USD | 8,890,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 3,620,000.00 USD | 3,620,000.00 USD | 1,860.00 USD | 843.43 USD | 16.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 8,450,000.00 USD | 8,450,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 9,770.00 USD | 38,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.70` | 3,620,000.00 USD | 3,620,000.00 USD | 28,300.00 USD | 4,090.00 USD | 59,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 8,330,000.00 USD | 8,330,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 3,530,000.00 USD | 3,530,000.00 USD | 31,390.00 USD | 9,550.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 8,190,000.00 USD | 8,190,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 3,470,000.00 USD | 3,470,000.00 USD | 9,760.00 USD | 22,630.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 390.02 USD | 28,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.90` | 3,370,000.00 USD | 3,370,000.00 USD | 30,220.00 USD | 15,460.00 USD | 19,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 7,830,000.00 USD | 7,830,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 3,310,000.00 USD | 3,310,000.00 USD | 45,330.00 USD | 26,490.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 7,500,000.00 USD | 7,500,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.70` | 3,230,000.00 USD | 3,230,000.00 USD | 21,690.00 USD | 16,380.00 USD | 65,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 7,020,000.00 USD | 7,020,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 3,120,000.00 USD | 3,120,000.00 USD | 28,570.00 USD | 14,480.00 USD | 58,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 6,540,000.00 USD | 6,540,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 3,020,000.00 USD | 3,020,000.00 USD | 12,110.00 USD | 30,400.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 195.01 USD | 27,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.90` | 2,960,000.00 USD | 2,960,000.00 USD | 113,020.00 USD | 128,050.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 6,110,000.00 USD | 6,110,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 2,680,000.00 USD | 2,680,000.00 USD | 71,550.00 USD | 129,780.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 5,500,000.00 USD | 5,500,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 26,720.00 USD | 27,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.70` | 2,430,000.00 USD | 2,430,000.00 USD | 97,080.00 USD | 92,740.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 4,900,000.00 USD | 4,900,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 2,190,000.00 USD | 2,190,000.00 USD | 49,680.00 USD | 34,630.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 4,400,000.00 USD | 4,400,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 2,080,000.00 USD | 2,080,000.00 USD | 30,680.00 USD | 12,730.00 USD | 44,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 971.55 USD | 971.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.90` | 2,000,000.00 USD | 2,000,000.00 USD | 32,430.00 USD | 42,870.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 3,830,000.00 USD | 3,830,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 1,910,000.00 USD | 1,910,000.00 USD | 117,910.00 USD | 6,950.00 USD | 175,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 3,610,000.00 USD | 3,610,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.70` | 1,610,000.00 USD | 1,610,000.00 USD | 76,780.00 USD | 0.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 3,480,000.00 USD | 3,480,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 1,500,000.00 USD | 1,500,000.00 USD | 39,410.00 USD | 0.00 USD | 149,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 3,150,000.00 USD | 3,150,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 1,310,000.00 USD | 1,310,000.00 USD | 60,220.00 USD | 7,210.00 USD | 20,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 1,220,000.00 USD | 1,220,000.00 USD | 118,720.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 3,000,000.00 USD | 3,000,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 1,100,000.00 USD | 1,100,000.00 USD | 79,160.00 USD | 4,430.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 2,540,000.00 USD | 2,540,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 991,990.00 USD | 991,990.00 USD | 66,860.00 USD | 3,620.00 USD | 8.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 2,260,000.00 USD | 2,260,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 921,500.00 USD | 921,500.00 USD | 89,210.00 USD | 3,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 2,090,000.00 USD | 2,090,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 828,500.00 USD | 828,500.00 USD | 224,710.00 USD | 0.00 USD | 78,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 525,790.00 USD | 525,790.00 USD | 152,940.00 USD | 0.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 1,550,000.00 USD | 1,550,000.00 USD | 375,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 338,920.00 USD | 338,920.00 USD | 204,080.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 1,170,000.00 USD | 1,170,000.00 USD | 496,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.70` | 134,840.00 USD | 134,840.00 USD | 100,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 677,870.00 USD | 677,870.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 34,230.00 USD | 34,230.00 USD | 33,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.40` | 329,400.00 USD | 329,400.00 USD | 3,530.00 USD | 0.00 USD | 110.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `275.50` | 5,990.00 USD | 5,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `275.90` | 325,760.00 USD | 325,760.00 USD | 2,560.00 USD | 0.00 USD | 99.71 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 323,100.00 USD | 323,100.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `276.50` | 333.46 USD | 6,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `276.90` | 216,870.00 USD | 216,870.00 USD | 44,670.00 USD | 22,950.00 USD | 10.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.40` | 149,240.00 USD | 149,240.00 USD | 0.00 USD | 63,290.00 USD | 90.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 301.20 USD | 301.20 USD | 301.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 85,860.00 USD | 85,860.00 USD | 0.00 USD | 85,690.00 USD | 163.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.40` | 51,190.00 USD | 51,190.00 USD | 24,750.00 USD | 26,370.00 USD | 73.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.70` | 24,120.00 USD | 24,120.00 USD | 19,830.00 USD | 4,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 128,750.00 USD | 128,750.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.10` | 78,250.00 USD | 78,250.00 USD | 29,260.00 USD | 24,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.40` | 224,730.00 USD | 224,730.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.50` | 106,630.00 USD | 106,630.00 USD | 28,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.90` | 131,430.00 USD | 131,430.00 USD | 0.00 USD | 7,690.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.30` | 257,500.00 USD | 257,500.00 USD | 29,750.00 USD | 18,470.00 USD | 77,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.70` | 342,010.00 USD | 342,010.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.10` | 388,770.00 USD | 388,770.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 301,680.00 USD | 301,680.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.50` | 416,300.00 USD | 416,300.00 USD | 20,590.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.90` | 421,710.00 USD | 421,710.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.90` | 699,710.00 USD | 699,710.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.30` | 459,970.00 USD | 459,970.00 USD | 0.00 USD | 0.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 755,930.00 USD | 755,930.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.70` | 547,670.00 USD | 547,670.00 USD | 57,180.00 USD | 20,400.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.90` | 788,130.00 USD | 788,130.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.10` | 788,970.00 USD | 788,970.00 USD | 71,390.00 USD | 9,540.00 USD | 160,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 66,560.00 USD | 146,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.50` | 917,440.00 USD | 917,440.00 USD | 13,380.00 USD | 15,300.00 USD | 99,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.90` | 990,250.00 USD | 990,250.00 USD | 0.00 USD | 34,020.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.90` | 1,360,000.00 USD | 1,360,000.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.30` | 1,140,000.00 USD | 1,140,000.00 USD | 38,980.00 USD | 54,150.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 1,520,000.00 USD | 1,520,000.00 USD | 27,700.00 USD | 89,730.00 USD | 42,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.70` | 1,280,000.00 USD | 1,280,000.00 USD | 49,080.00 USD | 67,500.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 1,980,000.00 USD | 1,980,000.00 USD | 67,050.00 USD | 391,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.10` | 1,500,000.00 USD | 1,500,000.00 USD | 87,540.00 USD | 37,830.00 USD | 96,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 2,320,000.00 USD | 2,320,000.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.50` | 1,730,000.00 USD | 1,730,000.00 USD | 91,500.00 USD | 95,280.00 USD | 39,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.90` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 29,130.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 2,420,000.00 USD | 2,420,000.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 137,400.00 USD | 11.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.70` | 1,800,000.00 USD | 1,800,000.00 USD | 750.70 USD | 3,470.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 51,390.00 USD | 148,230.00 USD | 2.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.10` | 2,030,000.00 USD | 2,030,000.00 USD | 31,110.00 USD | 117,540.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 53,620.00 USD | 103,430.00 USD | 53,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 21,390.00 USD | 54,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.90` | 2,170,000.00 USD | 2,170,000.00 USD | 9,030.00 USD | 10,410.00 USD | 38,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 277,850.00 USD | 23.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.30` | 2,200,000.00 USD | 2,200,000.00 USD | 28,590.00 USD | 4,000.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 2,140.00 USD | 8,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.70` | 2,220,000.00 USD | 2,220,000.00 USD | 7,560.00 USD | 5,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 3,240,000.00 USD | 3,240,000.00 USD | 1,170.00 USD | 0.00 USD | 9.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 2,250,000.00 USD | 2,250,000.00 USD | 1,720.00 USD | 20,030.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 927.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.50` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 4,030.00 USD | 14.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.90` | 2,270,000.00 USD | 2,270,000.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 3,280,000.00 USD | 3,280,000.00 USD | 34,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.70` | 2,320,000.00 USD | 2,320,000.00 USD | 33,020.00 USD | 7,010.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 3,280,000.00 USD | 3,280,000.00 USD | 898.13 USD | 861.99 USD | 5.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 2,320,000.00 USD | 2,320,000.00 USD | 352.90 USD | 0.00 USD | 5.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 3,340,000.00 USD | 3,340,000.00 USD | 1,340.00 USD | 55,720.00 USD | 19.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 2,350,000.00 USD | 2,350,000.00 USD | 562.74 USD | 22,110.00 USD | 22.17 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 6,770.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 120,730.00 USD | 9.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 2,460,000.00 USD | 2,460,000.00 USD | 13,260.00 USD | 61,370.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 71,940.00 USD | 32.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 763.13 USD | 9,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `292.70` | 2,550,000.00 USD | 2,550,000.00 USD | 20,240.00 USD | 71,800.00 USD | 9.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 119,560.00 USD | 23.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 2,610,000.00 USD | 2,610,000.00 USD | 10,710.00 USD | 35,470.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 534.50 USD | 112,560.00 USD | 43.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 2,710,000.00 USD | 2,710,000.00 USD | 19,530.00 USD | 55,160.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 2,860,000.00 USD | 2,860,000.00 USD | 88,090.00 USD | 19,500.00 USD | 43,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 3,880,000.00 USD | 3,880,000.00 USD | 51,570.00 USD | 20,910.00 USD | 45,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 2,990,000.00 USD | 2,990,000.00 USD | 28,410.00 USD | 48,550.00 USD | 56,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 139,780.00 USD | 14,550.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 3,320,000.00 USD | 3,320,000.00 USD | 111,760.00 USD | 96,720.00 USD | 119,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 64,510.00 USD | 107,870.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 3,440,000.00 USD | 3,440,000.00 USD | 23,770.00 USD | 41,270.00 USD | 53,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 3,590,000.00 USD | 3,590,000.00 USD | 39,490.00 USD | 63,880.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 3,730,000.00 USD | 3,730,000.00 USD | 82,120.00 USD | 19,540.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 108,830.00 USD | 133,090.00 USD | 150,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 3,910,000.00 USD | 3,910,000.00 USD | 69,980.00 USD | 82,640.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 27,680.00 USD | 77,570.00 USD | 120,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 102.59 USD | 9,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `296.70` | 4,030,000.00 USD | 4,030,000.00 USD | 34,010.00 USD | 21,030.00 USD | 62,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 207,350.00 USD | 50,930.00 USD | 172,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 4,120,000.00 USD | 4,120,000.00 USD | 52,650.00 USD | 323.66 USD | 36,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 5,960,000.00 USD | 5,960,000.00 USD | 4,100.00 USD | 59,290.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 4,140,000.00 USD | 4,140,000.00 USD | 6,700.00 USD | 1,120.00 USD | 20,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 4,170,000.00 USD | 4,170,000.00 USD | 1,730.00 USD | 9,670.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 17,770.00 USD | 39,840.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 4,320,000.00 USD | 4,320,000.00 USD | 55,610.00 USD | 974.79 USD | 93,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 32,250.00 USD | 42,710.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 4,440,000.00 USD | 4,440,000.00 USD | 30,040.00 USD | 7,690.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 6,340,000.00 USD | 6,340,000.00 USD | 70,090.00 USD | 12,780.00 USD | 40,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 4,490,000.00 USD | 4,490,000.00 USD | 7,660.00 USD | 18,270.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 4,470.00 USD | 13,080.00 USD | 45,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 4,560,000.00 USD | 4,560,000.00 USD | 35,750.00 USD | 15,000.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 883.53 USD | 10,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.90` | 4,630,000.00 USD | 4,630,000.00 USD | 14,520.00 USD | 17,340.00 USD | 32,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 6,490,000.00 USD | 6,490,000.00 USD | 56,210.00 USD | 10,220.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 4,730,000.00 USD | 4,730,000.00 USD | 33,000.00 USD | 24,420.00 USD | 42,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 866.20 USD | 1,190.00 USD | 121.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 4,790,000.00 USD | 4,790,000.00 USD | 15,970.00 USD | 30,870.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 6,690,000.00 USD | 6,690,000.00 USD | 24,730.00 USD | 70,210.00 USD | 104,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 4,840,000.00 USD | 4,840,000.00 USD | 4,280.00 USD | 20,930.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 71,890.00 USD | 56,010.00 USD | 94,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 4,910,000.00 USD | 4,910,000.00 USD | 19,640.00 USD | 8,100.00 USD | 34,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 4,980,000.00 USD | 4,980,000.00 USD | 20,900.00 USD | 38,380.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 89,300.00 USD | 185,430.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 5,000,000.00 USD | 5,000,000.00 USD | 4,890.00 USD | 4,690.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 7,340,000.00 USD | 7,340,000.00 USD | 1,560.00 USD | 125,480.00 USD | 50.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 5,060,000.00 USD | 5,060,000.00 USD | 11,530.00 USD | 11,670.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 71,700.00 USD | 110,480.00 USD | 41,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 5,110,000.00 USD | 5,110,000.00 USD | 20,770.00 USD | 1,020.00 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 173.09 USD | 47.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 5,130,000.00 USD | 5,130,000.00 USD | 10,860.00 USD | 1,620.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 5,180,000.00 USD | 5,180,000.00 USD | 29,150.00 USD | 3,670.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 21,140.00 USD | 11,010.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 5,240,000.00 USD | 5,240,000.00 USD | 3,890.00 USD | 5,160.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 7,660,000.00 USD | 7,660,000.00 USD | 3,670.00 USD | 11,280.00 USD | 259.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 5,300,000.00 USD | 5,300,000.00 USD | 9,880.00 USD | 6,170.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 36,160.00 USD | 18,990.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 5,310,000.00 USD | 5,310,000.00 USD | 14,400.00 USD | 178.95 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 163,730.00 USD | 127,450.00 USD | 119,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 5,320,000.00 USD | 5,320,000.00 USD | 4,670.00 USD | 1,640.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 5,340,000.00 USD | 5,340,000.00 USD | 9,360.00 USD | 5,780.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 8,280,000.00 USD | 8,280,000.00 USD | 82,000.00 USD | 55,480.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 5,350,000.00 USD | 5,350,000.00 USD | 3,900.00 USD | 3,200.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 39,250.00 USD | 55,740.00 USD | 66,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 5,390,000.00 USD | 5,390,000.00 USD | 4,670.00 USD | 21,680.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 84,850.00 USD | 64,520.00 USD | 102,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 5,480,000.00 USD | 5,480,000.00 USD | 32,760.00 USD | 42,120.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 8,980,000.00 USD | 8,980,000.00 USD | 46,230.00 USD | 154,680.00 USD | 83,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 5,540,000.00 USD | 5,540,000.00 USD | 19,010.00 USD | 24,960.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 6,360.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `307.90` | 5,620,000.00 USD | 5,620,000.00 USD | 33,320.00 USD | 30,350.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 136,380.00 USD | 101,120.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 5,650,000.00 USD | 5,650,000.00 USD | 13,480.00 USD | 7,490.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 9,610,000.00 USD | 9,610,000.00 USD | 152,590.00 USD | 50,070.00 USD | 124,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 5,660,000.00 USD | 5,660,000.00 USD | 5,270.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 61,600.00 USD | 52,230.00 USD | 19,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.00` | 5,670,000.00 USD | 5,670,000.00 USD | 11,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 9,860,000.00 USD | 9,860,000.00 USD | 28,000.00 USD | 35,530.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 10,190,000.00 USD | 10,190,000.00 USD | 59,490.00 USD | 131,460.00 USD | 144,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 10,470,000.00 USD | 10,470,000.00 USD | 78,770.00 USD | 123,340.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 17,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `310.90` | 10,550,000.00 USD | 10,550,000.00 USD | 35,670.00 USD | 35,930.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.40` | 10,750,000.00 USD | 10,750,000.00 USD | 89,390.00 USD | 65,750.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 10,810,000.00 USD | 10,810,000.00 USD | 40,320.00 USD | 11,160.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 10,920,000.00 USD | 10,920,000.00 USD | 38,320.00 USD | 22,970.00 USD | 43,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 10,990,000.00 USD | 10,990,000.00 USD | 22,600.00 USD | 8,800.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.40` | 11,100,000.00 USD | 11,100,000.00 USD | 55,570.00 USD | 24,730.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 11,200,000.00 USD | 11,200,000.00 USD | 44,540.00 USD | 15,370.00 USD | 35,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 11,300,000.00 USD | 11,300,000.00 USD | 51,980.00 USD | 307.60 USD | 51,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 11,350,000.00 USD | 11,350,000.00 USD | 39,410.00 USD | 0.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.40` | 11,370,000.00 USD | 11,370,000.00 USD | 6,160.00 USD | 9,920.00 USD | 50.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 11,480,000.00 USD | 11,480,000.00 USD | 47,110.00 USD | 41,400.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 11,600,000.00 USD | 11,600,000.00 USD | 16,580.00 USD | 40,320.00 USD | 61,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 11,620,000.00 USD | 11,620,000.00 USD | 3,030.00 USD | 10,840.00 USD | 9.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.40` | 11,630,000.00 USD | 11,630,000.00 USD | 14,540.00 USD | 1,010.00 USD | 247.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 11,660,000.00 USD | 11,660,000.00 USD | 21,640.00 USD | 8,200.00 USD | 143.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 11,720,000.00 USD | 11,720,000.00 USD | 3,320.00 USD | 27,530.00 USD | 22,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 11,780,000.00 USD | 11,780,000.00 USD | 11,180.00 USD | 17,970.00 USD | 37,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.40` | 11,800,000.00 USD | 11,800,000.00 USD | 733.55 USD | 18,060.00 USD | 3.21 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 11,830,000.00 USD | 11,830,000.00 USD | 446.22 USD | 22,230.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 11,910,000.00 USD | 11,910,000.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 18,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 166.45 USD | 2.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.40` | 11,960,000.00 USD | 11,960,000.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 11,970,000.00 USD | 11,970,000.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 12,010,000.00 USD | 12,010,000.00 USD | 22,930.00 USD | 7,950.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 12,030,000.00 USD | 12,030,000.00 USD | 16,590.00 USD | 5,830.00 USD | 53.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.40` | 12,070,000.00 USD | 12,070,000.00 USD | 14,160.00 USD | 11,950.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.90` | 12,070,000.00 USD | 12,070,000.00 USD | 269.10 USD | 692.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.90` | 12,120,000.00 USD | 12,120,000.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `325.40` | 12,170,000.00 USD | 12,170,000.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `340.50` | 1,360.00 USD | 19,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 20,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 21,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `373.50` | 41,090.00 USD | 62,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `387.50` | 487.86 USD | 62,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 71,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 117,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `477.50` | 8,200.00 USD | 126,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 126,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `538.50` | 351.10 USD | 127,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `70.50` | 439,430.00 USD | 0.00 USD | 266.49 USD | `-74.61%` | `3,780,000,000.00` |
| `Live` | `Long` | `80.50` | 439,160.00 USD | 0.00 USD | 577.59 USD | `-71.01%` | `7,175,000,000.00` |
| `Live` | `Long` | `95.50` | 438,580.00 USD | 0.00 USD | 920.05 USD | `-65.61%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 437,660.00 USD | 0.00 USD | 6,240.00 USD | `-63.45%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 431,420.00 USD | 0.00 USD | 4,080.00 USD | `-63.09%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 427,350.00 USD | 0.00 USD | 212.76 USD | `-60.57%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 427,130.00 USD | 0.00 USD | 212.35 USD | `-57.33%` | `1,792,000,000.00` |
| `Live` | `Long` | `119.50` | 426,920.00 USD | 0.00 USD | 175.66 USD | `-56.97%` | `1,470,000,000.00` |
| `Live` | `Long` | `122.50` | 426,740.00 USD | 0.00 USD | 124.46 USD | `-55.89%` | `1,016,000,000.00` |
| `Live` | `Long` | `125.50` | 426,620.00 USD | 0.00 USD | 1,640.00 USD | `-54.81%` | `13,105,000,000.00` |
| `Live` | `Long` | `126.50` | 424,980.00 USD | 0.00 USD | 658.18 USD | `-54.45%` | `5,203,000,000.00` |
| `Live` | `Long` | `127.50` | 424,320.00 USD | 0.00 USD | 1,910.00 USD | `-54.09%` | `15,000,000,000.00` |
| `Live` | `Long` | `141.50` | 422,410.00 USD | 0.00 USD | 157.49 USD | `-49.04%` | `1,113,000,000.00` |
| `Live` | `Long` | `147.50` | 422,250.00 USD | 0.00 USD | 895.47 USD | `-46.88%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 421,350.00 USD | 0.00 USD | 1,270.00 USD | `-46.52%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 420,090.00 USD | 0.00 USD | 2,370.00 USD | `-46.16%` | `15,823,000,000.00` |
| `Live` | `Long` | `150.50` | 417,720.00 USD | 0.00 USD | 236.13 USD | `-45.80%` | `1,569,000,000.00` |
| `Live` | `Long` | `152.50` | 417,480.00 USD | 0.00 USD | 303.78 USD | `-45.08%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 417,180.00 USD | 0.00 USD | 325.00 USD | `-41.48%` | `2,000,000,000.00` |
| `Live` | `Long` | `164.50` | 416,860.00 USD | 0.00 USD | 1,650.00 USD | `-40.76%` | `10,000,000,000.00` |
| `Live` | `Long` | `167.50` | 415,210.00 USD | 0.00 USD | 8,660.00 USD | `-39.68%` | `51,706,000,000.00` |
| `Live` | `Long` | `170.50` | 406,550.00 USD | 0.00 USD | 426.25 USD | `-38.60%` | `2,500,000,000.00` |
| `Live` | `Long` | `172.50` | 406,120.00 USD | 0.00 USD | 2,090.00 USD | `-37.88%` | `12,135,000,000.00` |
| `Live` | `Long` | `174.50` | 404,030.00 USD | 0.00 USD | 169.96 USD | `-37.16%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 403,860.00 USD | 0.00 USD | 516.67 USD | `-36.80%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 403,340.00 USD | 0.00 USD | 373.83 USD | `-36.44%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 402,970.00 USD | 0.00 USD | 191.57 USD | `-33.92%` | `1,044,000,000.00` |
| `Live` | `Long` | `184.50` | 402,780.00 USD | 0.00 USD | 616.05 USD | `-33.56%` | `3,339,000,000.00` |
| `Live` | `Long` | `186.50` | 402,160.00 USD | 0.00 USD | 412.17 USD | `-32.84%` | `2,210,000,000.00` |
| `Live` | `Long` | `188.50` | 401,750.00 USD | 0.00 USD | 418.28 USD | `-32.12%` | `2,219,000,000.00` |
| `Live` | `Long` | `191.50` | 401,330.00 USD | 0.00 USD | 858.49 USD | `-31.04%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 400,470.00 USD | 0.00 USD | 1,490.00 USD | `-30.68%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 398,990.00 USD | 0.00 USD | 370.47 USD | `-29.60%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 398,620.00 USD | 0.00 USD | 210.65 USD | `-29.24%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 398,410.00 USD | 0.00 USD | 548.03 USD | `-28.16%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 397,860.00 USD | 0.00 USD | 293.13 USD | `-27.80%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 397,570.00 USD | 0.00 USD | 420.39 USD | `-27.08%` | `2,076,000,000.00` |
| `Live` | `Long` | `203.50` | 397,150.00 USD | 0.00 USD | 1,050.00 USD | `-26.72%` | `5,167,000,000.00` |
| `Live` | `Long` | `204.50` | 396,090.00 USD | 0.00 USD | 39,880.00 USD | `-26.36%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 356,210.00 USD | 0.00 USD | 191.53 USD | `-26.00%` | `932,000,000.00` |
| `Live` | `Long` | `207.50` | 356,020.00 USD | 0.00 USD | 188,820.00 USD | `-25.28%` | `909,952,000,000.00` |
| `Live` | `Long` | `210.50` | 167,200.00 USD | 0.00 USD | 108.83 USD | `-24.20%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 167,100.00 USD | 0.00 USD | 9,340.00 USD | `-23.12%` | `43,743,000,000.00` |
| `Live` | `Long` | `214.50` | 157,760.00 USD | 0.00 USD | 2,940.00 USD | `-22.76%` | `13,703,000,000.00` |
| `Live` | `Long` | `215.50` | 154,820.00 USD | 0.00 USD | 2,610.00 USD | `-22.40%` | `12,132,000,000.00` |
| `Live` | `Long` | `219.50` | 152,200.00 USD | 0.00 USD | 104.92 USD | `-20.96%` | `478,000,000.00` |
| `Live` | `Long` | `220.50` | 152,100.00 USD | 0.00 USD | 1,010.00 USD | `-20.59%` | `4,592,000,000.00` |
| `Live` | `Long` | `222.50` | 151,080.00 USD | 0.00 USD | 5,800.00 USD | `-19.87%` | `26,061,000,000.00` |
| `Live` | `Long` | `223.50` | 145,290.00 USD | 0.00 USD | 32,860.00 USD | `-19.51%` | `147,023,000,000.00` |
| `Live` | `Long` | `225.50` | 112,430.00 USD | 0.00 USD | 5,370.00 USD | `-18.79%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 107,060.00 USD | 0.00 USD | 1,890.00 USD | `-18.43%` | `8,324,000,000.00` |
| `Live` | `Long` | `227.50` | 105,170.00 USD | 0.00 USD | 174.49 USD | `-18.07%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 105,000.00 USD | 0.00 USD | 7,840.00 USD | `-17.71%` | `34,313,000,000.00` |
| `Live` | `Long` | `229.50` | 97,160.00 USD | 0.00 USD | 1,880.00 USD | `-17.35%` | `8,171,000,000.00` |
| `Live` | `Long` | `230.50` | 95,280.00 USD | 0.00 USD | 626.73 USD | `-16.99%` | `2,719,000,000.00` |
| `Live` | `Long` | `231.50` | 94,660.00 USD | 0.00 USD | 506.06 USD | `-16.63%` | `2,186,000,000.00` |
| `Live` | `Long` | `232.50` | 94,150.00 USD | 0.00 USD | 429.66 USD | `-16.27%` | `1,848,000,000.00` |
| `Live` | `Long` | `234.50` | 93,720.00 USD | 0.00 USD | 217.85 USD | `-15.55%` | `929,000,000.00` |
| `Live` | `Long` | `235.50` | 93,500.00 USD | 0.00 USD | 454.52 USD | `-15.19%` | `1,930,000,000.00` |
| `Live` | `Long` | `239.50` | 93,050.00 USD | 0.00 USD | 1,030.00 USD | `-13.75%` | `4,281,000,000.00` |
| `Live` | `Long` | `240.50` | 92,020.00 USD | 0.00 USD | 612.79 USD | `-13.39%` | `2,548,000,000.00` |
| `Live` | `Long` | `241.50` | 91,410.00 USD | 0.00 USD | 251.88 USD | `-13.03%` | `1,043,000,000.00` |
| `Live` | `Long` | `243.50` | 91,160.00 USD | 0.00 USD | 1,200.00 USD | `-12.31%` | `4,937,000,000.00` |
| `Live` | `Long` | `244.50` | 89,960.00 USD | 0.00 USD | 30,300.00 USD | `-11.95%` | `123,916,000,000.00` |
| `Live` | `Long` | `245.50` | 59,660.00 USD | 0.00 USD | 1,030.00 USD | `-11.59%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 58,630.00 USD | 0.00 USD | 699.44 USD | `-10.87%` | `2,826,000,000.00` |
| `Live` | `Long` | `250.50` | 57,930.00 USD | 0.00 USD | 1,330.00 USD | `-9.79%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 56,610.00 USD | 0.00 USD | 268.35 USD | `-9.43%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 56,340.00 USD | 0.00 USD | 1,030.00 USD | `-9.07%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 55,310.00 USD | 0.00 USD | 362.92 USD | `-8.35%` | `1,426,000,000.00` |
| `Live` | `Long` | `256.50` | 54,940.00 USD | 0.00 USD | 453.49 USD | `-7.63%` | `1,768,000,000.00` |
| `Live` | `Long` | `257.50` | 54,490.00 USD | 0.00 USD | 366.42 USD | `-7.27%` | `1,423,000,000.00` |
| `Live` | `Long` | `258.50` | 54,120.00 USD | 0.00 USD | 278.15 USD | `-6.91%` | `1,076,000,000.00` |
| `Live` | `Long` | `259.50` | 53,850.00 USD | 0.00 USD | 5,190.00 USD | `-6.55%` | `20,000,000,000.00` |
| `Live` | `Long` | `260.50` | 48,660.00 USD | 0.00 USD | 8,620.00 USD | `-6.19%` | `33,107,000,000.00` |
| `Live` | `Long` | `261.50` | 40,030.00 USD | 0.00 USD | 1,990.00 USD | `-5.83%` | `7,603,000,000.00` |
| `Live` | `Long` | `264.50` | 38,040.00 USD | 0.00 USD | 9,770.00 USD | `-4.75%` | `36,922,000,000.00` |
| `Live` | `Long` | `265.50` | 28,280.00 USD | 0.00 USD | 390.02 USD | `-4.39%` | `1,469,000,000.00` |
| `Live` | `Long` | `267.50` | 27,890.00 USD | 0.00 USD | 195.01 USD | `-3.67%` | `729,000,000.00` |
| `Live` | `Long` | `268.50` | 27,690.00 USD | 0.00 USD | 26,720.00 USD | `-3.31%` | `99,518,000,000.00` |
| `Live` | `Long` | `269.50` | 971.55 USD | 0.00 USD | 971.55 USD | `-2.95%` | `3,605,000,000.00` |
| `Live` | `Short` | `280.50` | 3,080.00 USD | 3,080.00 USD | 0.00 USD | `+1.01%` | `10,970,000,000.00` |
| `Live` | `Short` | `288.50` | 9,350.00 USD | 6,280.00 USD | 0.00 USD | `+3.89%` | `21,758,000,000.00` |
| `Live` | `Short` | `296.50` | 9,460.00 USD | 102.59 USD | 0.00 USD | `+6.77%` | `346,000,000.00` |
| `Live` | `Short` | `305.50` | 15,770.00 USD | 6,310.00 USD | 0.00 USD | `+10.01%` | `20,668,000,000.00` |
| `Live` | `Short` | `310.50` | 16,290.00 USD | 517.91 USD | 0.00 USD | `+11.82%` | `1,668,000,000.00` |
| `Live` | `Short` | `320.50` | 17,400.00 USD | 1,110.00 USD | 0.00 USD | `+15.42%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 17,670.00 USD | 276.63 USD | 0.00 USD | `+19.02%` | `837,000,000.00` |
| `Live` | `Short` | `341.50` | 19,040.00 USD | 1,370.00 USD | 0.00 USD | `+22.98%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 20,050.00 USD | 1,010.00 USD | 0.00 USD | `+29.10%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 20,490.00 USD | 445.52 USD | 0.00 USD | `+32.70%` | `1,209,000,000.00` |
| `Live` | `Short` | `371.50` | 61,360.00 USD | 40,870.00 USD | 0.00 USD | `+33.78%` | `110,000,000,000.00` |
| `Live` | `Short` | `387.50` | 61,840.00 USD | 487.86 USD | 0.00 USD | `+39.54%` | `1,259,000,000.00` |
| `Live` | `Short` | `432.50` | 70,650.00 USD | 8,810.00 USD | 0.00 USD | `+55.75%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 116,910.00 USD | 46,250.00 USD | 0.00 USD | `+65.47%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 125,110.00 USD | 8,200.00 USD | 0.00 USD | `+71.95%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 125,820.00 USD | 718.34 USD | 0.00 USD | `+79.52%` | `1,441,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 158,440.00 USD | 0.00 USD | 210.94 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 158,230.00 USD | 0.00 USD | 2,070.00 USD | `-47.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 156,160.00 USD | 0.00 USD | 2,530.00 USD | `-35.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 153,630.00 USD | 0.00 USD | 490.59 USD | `-33.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 153,140.00 USD | 0.00 USD | 482.01 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 152,660.00 USD | 0.00 USD | 189.07 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 152,470.00 USD | 0.00 USD | 441.60 USD | `-24.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 152,030.00 USD | 0.00 USD | 703.49 USD | `-24.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 151,330.00 USD | 0.00 USD | 715.29 USD | `-23.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 150,610.00 USD | 0.00 USD | 638.36 USD | `-20.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 149,970.00 USD | 0.00 USD | 740.85 USD | `-19.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 149,230.00 USD | 0.00 USD | 1,050.00 USD | `-17.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 148,180.00 USD | 0.00 USD | 389.48 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 147,790.00 USD | 0.00 USD | 812.38 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 146,980.00 USD | 0.00 USD | 220.64 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 146,760.00 USD | 0.00 USD | 429.30 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 146,330.00 USD | 0.00 USD | 296.50 USD | `-13.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 146,040.00 USD | 0.00 USD | 216.45 USD | `-13.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 145,820.00 USD | 0.00 USD | 387.76 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 145,430.00 USD | 0.00 USD | 366.75 USD | `-11.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 145,060.00 USD | 0.00 USD | 1,630.00 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 143,440.00 USD | 0.00 USD | 2,700.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 140,740.00 USD | 0.00 USD | 2,940.00 USD | `-10.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 137,790.00 USD | 0.00 USD | 4,680.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 133,110.00 USD | 0.00 USD | 3,590.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 129,520.00 USD | 0.00 USD | 231.54 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 129,290.00 USD | 0.00 USD | 109.26 USD | `-8.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 129,180.00 USD | 0.00 USD | 1,780.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 127,400.00 USD | 0.00 USD | 51,300.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 76,100.00 USD | 0.00 USD | 250.81 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 75,850.00 USD | 0.00 USD | 468.90 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 75,380.00 USD | 0.00 USD | 857.85 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 74,530.00 USD | 0.00 USD | 7,790.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 66,730.00 USD | 0.00 USD | 122.99 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 66,610.00 USD | 0.00 USD | 2,180.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 64,430.00 USD | 0.00 USD | 241.98 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 64,190.00 USD | 0.00 USD | 2,850.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 61,340.00 USD | 0.00 USD | 6,540.00 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 54,800.00 USD | 0.00 USD | 27,320.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 27,480.00 USD | 0.00 USD | 1,140.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 26,340.00 USD | 0.00 USD | 269.60 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 26,070.00 USD | 0.00 USD | 13,500.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 12,570.00 USD | 0.00 USD | 1,140.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 11,430.00 USD | 0.00 USD | 9,840.00 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 1,590.00 USD | 0.00 USD | 299.74 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 1,290.00 USD | 0.00 USD | 903.60 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 384.34 USD | 0.00 USD | 384.34 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `278.50` | 125.88 USD | 125.88 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `279.50` | 22,120.00 USD | 21,990.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 25,480.00 USD | 3,370.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 25,620.00 USD | 133.43 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 26,920.00 USD | 1,300.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 34,960.00 USD | 8,040.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 36,970.00 USD | 2,010.00 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 44,660.00 USD | 7,690.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 49,740.00 USD | 5,080.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 56,030.00 USD | 6,290.00 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 56,290.00 USD | 261.96 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 56,450.00 USD | 153.44 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 85,460.00 USD | 29,020.00 USD | 0.00 USD | `+4.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 110,750.00 USD | 25,280.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 111,740.00 USD | 992.62 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 112,150.00 USD | 407.88 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 184,590.00 USD | 72,450.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 185,170.00 USD | 581.14 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 185,560.00 USD | 388.95 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 196,340.00 USD | 10,780.00 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 207,070.00 USD | 10,730.00 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 209,720.00 USD | 2,650.00 USD | 0.00 USD | `+10.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 210,770.00 USD | 1,060.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 210,880.00 USD | 102.73 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 225,370.00 USD | 14,500.00 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 226,010.00 USD | 634.04 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 227,040.00 USD | 1,030.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 232,690.00 USD | 5,650.00 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 232,810.00 USD | 118.85 USD | 0.00 USD | `+15.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 233,340.00 USD | 534.59 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 233,670.00 USD | 321.50 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 298,590.00 USD | 64,920.00 USD | 0.00 USD | `+17.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 299,680.00 USD | 1,090.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 311,670.00 USD | 12,000.00 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 312,220.00 USD | 547.52 USD | 0.00 USD | `+22.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 312,360.00 USD | 138.20 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 312,620.00 USD | 257.45 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 312,790.00 USD | 174.25 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 312,940.00 USD | 151.50 USD | 0.00 USD | `+26.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 314,390.00 USD | 1,450.00 USD | 0.00 USD | `+28.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 316,170.00 USD | 1,770.00 USD | 0.00 USD | `+29.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 316,500.00 USD | 326.07 USD | 0.00 USD | `+30.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 317,320.00 USD | 826.60 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 324,770.00 USD | 7,440.00 USD | 0.00 USD | `+31.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 325,450.00 USD | 682.84 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 326,550.00 USD | 1,100.00 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 327,230.00 USD | 683.96 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 327,430.00 USD | 199.75 USD | 0.00 USD | `+43.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 329,900.00 USD | 2,470.00 USD | 0.00 USD | `+44.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 330,940.00 USD | 1,040.00 USD | 0.00 USD | `+45.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 331,320.00 USD | 376.71 USD | 0.00 USD | `+46.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 331,480.00 USD | 158.86 USD | 0.00 USD | `+47.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 337,380.00 USD | 5,900.00 USD | 0.00 USD | `+49.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 338,460.00 USD | 1,080.00 USD | 0.00 USD | `+52.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 340,160.00 USD | 1,700.00 USD | 0.00 USD | `+53.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 341,710.00 USD | 1,550.00 USD | 0.00 USD | `+55.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 343,090.00 USD | 1,380.00 USD | 0.00 USD | `+56.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 343,710.00 USD | 621.14 USD | 0.00 USD | `+57.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 347,090.00 USD | 3,380.00 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 347,320.00 USD | 222.75 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 352,910.00 USD | 5,590.00 USD | 0.00 USD | `+62.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 358,830.00 USD | 5,920.00 USD | 0.00 USD | `+62.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 359,960.00 USD | 1,130.00 USD | 0.00 USD | `+65.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 367,590.00 USD | 7,630.00 USD | 0.00 USD | `+73.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 368,570.00 USD | 975.00 USD | 0.00 USD | `+75.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 369,550.00 USD | 981.00 USD | 0.00 USD | `+76.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 370,050.00 USD | 499.50 USD | 0.00 USD | `+79.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,260,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+80.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,260,000.00 USD | 1,000.00 USD | 0.00 USD | `+80.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,260,000.00 USD | 1,040.00 USD | 0.00 USD | `+86.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,260,000.00 USD | 340.67 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `240.90` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD |
| `7D` | `241.40` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `241.90` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.40` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD |
| `7D` | `242.90` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.40` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD |
| `7D` | `243.90` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 781.30 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.90` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD |
| `7D` | `245.40` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD |
| `1D` | `245.70` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `245.90` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD |
| `1D` | `246.10` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 13.11 USD |
| `7D` | `246.40` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD |
| `1D` | `246.50` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `1D` | `246.90` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `7D` | `246.90` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,740.00 USD |
| `1D` | `247.30` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 3,690.00 USD | 7,240.00 USD |
| `7D` | `247.40` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,700.00 USD |
| `1D` | `247.70` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 528.00 USD | 619.60 USD | 5.98 USD |
| `7D` | `247.90` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 789.37 USD | 4,610.00 USD | 3.04 USD |
| `1D` | `248.10` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 10,640.00 USD | 1,390.00 USD | 24,000.00 USD |
| `7D` | `248.40` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,880.00 USD |
| `1D` | `248.50` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 7,480.00 USD | 3,300.00 USD | 6,250.00 USD |
| `1D` | `248.90` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 3,780.00 USD | 7,980.00 USD | 26,840.00 USD |
| `7D` | `248.90` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD |
| `1D` | `249.30` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 182.40 USD | 6,170.00 USD | 4,180.00 USD |
| `7D` | `249.40` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 49,060.00 USD | 28,020.00 USD | 4,010.00 USD |
| `1D` | `249.70` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 17,990.00 USD | 76.18 USD | 4,030.00 USD |
| `7D` | `249.90` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,200.00 USD |
| `1D` | `250.10` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 9,650.00 USD | 4,330.00 USD | 7,360.00 USD |
| `7D` | `250.40` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,470.00 USD |
| `1D` | `250.50` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 4,210.00 USD | 2,450.00 USD | 1,340.00 USD |
| `1D` | `250.90` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 7,630.00 USD | 24,810.00 USD | 9,490.00 USD |
| `7D` | `250.90` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD |
| `1D` | `251.30` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 32,730.00 USD | 41,780.00 USD | 20,490.00 USD |
| `7D` | `251.40` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,200.00 USD |
| `1D` | `251.70` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 35,310.00 USD | 46,850.00 USD | 16,060.00 USD |
| `7D` | `251.90` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD |
| `1D` | `252.10` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 25,540.00 USD | 11,300.00 USD | 16,370.00 USD |
| `7D` | `252.40` | 11,240,000.00 USD | 0.00 USD | 11,240,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,130.00 USD |
| `1D` | `252.50` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 10,840.00 USD | 3,450.00 USD | 7,750.00 USD |
| `1D` | `252.90` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 12,160.00 USD | 6,450.00 USD | 2,980.00 USD |
| `7D` | `252.90` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 29,220.00 USD | 19,580.00 USD | 22.93 USD |
| `1D` | `253.30` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 17,170.00 USD | 22,810.00 USD | 8,230.00 USD |
| `7D` | `253.40` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD |
| `1D` | `253.70` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 8,120.00 USD | 8,990.00 USD | 11,920.00 USD |
| `7D` | `253.90` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,940.00 USD |
| `1D` | `254.10` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 144.00 USD | 4,520.00 USD | 3,930.00 USD |
| `7D` | `254.40` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,860.00 USD |
| `1D` | `254.50` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 134.35 USD | 2,050.00 USD | 2.31 USD |
| `1D` | `254.90` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 7,730.00 USD | 6,590.00 USD | 2,770.00 USD |
| `7D` | `254.90` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD |
| `1D` | `255.30` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 3,050.00 USD | 890.20 USD | 11.05 USD |
| `7D` | `255.40` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,820.00 USD |
| `1D` | `255.70` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD |
| `7D` | `255.90` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,120.00 USD |
| `1D` | `256.10` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 16,160.00 USD | 2,260.00 USD | 0.96 USD |
| `7D` | `256.40` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,420.00 USD |
| `1D` | `256.50` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `1D` | `256.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 5,560.00 USD | 928.93 USD | 8.97 USD |
| `7D` | `256.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,960.00 USD |
| `1D` | `257.30` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 5,410.00 USD | 130.77 USD | 11,760.00 USD |
| `7D` | `257.40` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,290.00 USD |
| `1D` | `257.70` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 886.80 USD | 611.06 USD | 4,830.00 USD |
| `7D` | `257.90` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,230.00 USD |
| `1D` | `258.10` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 5,060.00 USD | 2,620.00 USD | 6,860.00 USD |
| `7D` | `258.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,530.00 USD |
| `1D` | `258.50` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 3,900.00 USD | 3,110.00 USD | 2.55 USD |
| `1D` | `258.90` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 463.18 USD | 7,050.00 USD | 5,600.00 USD |
| `7D` | `258.90` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,410.00 USD |
| `1D` | `259.30` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 15,810.00 USD | 713.90 USD | 7,660.00 USD |
| `7D` | `259.40` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,100.00 USD |
| `1D` | `259.70` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 10,100.00 USD | 13,590.00 USD | 24,250.00 USD |
| `7D` | `259.90` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 19,140.00 USD | 12,520.00 USD | 119.41 USD |
| `1D` | `260.10` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 8,200.00 USD | 14,680.00 USD | 6,870.00 USD |
| `7D` | `260.40` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,170.00 USD |
| `1D` | `260.50` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 2,460.00 USD | 2,810.00 USD | 10,400.00 USD |
| `1D` | `260.90` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 8,070.00 USD | 16,070.00 USD | 13,930.00 USD |
| `7D` | `260.90` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,920.00 USD |
| `1D` | `261.30` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 7,780.00 USD | 18,050.00 USD | 31,350.00 USD |
| `7D` | `261.40` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,490.00 USD |
| `1D` | `261.70` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 4,600.00 USD | 1,290.00 USD | 19,370.00 USD |
| `7D` | `261.90` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,280.00 USD |
| `1D` | `262.10` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 517.32 USD | 4,780.00 USD | 13,920.00 USD |
| `7D` | `262.40` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 44,640.00 USD | 52,560.00 USD | 24.61 USD |
| `1D` | `262.50` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 8,380.00 USD | 4,860.00 USD | 5.26 USD |
| `1D` | `262.90` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 366.04 USD | 13,810.00 USD | 6.97 USD |
| `7D` | `262.90` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,780.00 USD |
| `1D` | `263.30` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 9,600.00 USD | 3,960.00 USD | 16,180.00 USD |
| `7D` | `263.40` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,020.00 USD |
| `1D` | `263.70` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 790.65 USD | 10,850.00 USD | 16,160.00 USD |
| `7D` | `263.90` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,860.00 USD |
| `1D` | `264.10` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 2,210.00 USD | 184.09 USD | 18,120.00 USD |
| `7D` | `264.40` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,190.00 USD |
| `1D` | `264.50` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 800.20 USD | 928.53 USD | 60,000.00 USD |
| `1D` | `264.90` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 39,490.00 USD | 4,750.00 USD | 15,630.00 USD |
| `7D` | `264.90` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,220.00 USD |
| `1D` | `265.30` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 23,930.00 USD | 12,790.00 USD | 35,520.00 USD |
| `7D` | `265.40` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,820.00 USD |
| `1D` | `265.70` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 27,950.00 USD | 38,080.00 USD | 52,790.00 USD |
| `7D` | `265.90` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,740.00 USD |
| `1D` | `266.10` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 53,050.00 USD | 3,690.00 USD | 5,080.00 USD |
| `7D` | `266.40` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,690.00 USD |
| `1D` | `266.50` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 34,380.00 USD | 31,420.00 USD | 70,400.00 USD |
| `1D` | `266.90` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 32,360.00 USD | 25,410.00 USD | 16,630.00 USD |
| `7D` | `266.90` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,370.00 USD |
| `1D` | `267.30` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 17,990.00 USD | 15,140.00 USD | 42,060.00 USD |
| `7D` | `267.40` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,460.00 USD |
| `1D` | `267.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 83,640.00 USD | 119,390.00 USD | 28,560.00 USD |
| `7D` | `267.90` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,230.00 USD |
| `1D` | `268.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 55,190.00 USD | 104,940.00 USD | 64,060.00 USD |
| `7D` | `268.40` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,620.00 USD |
| `1D` | `268.50` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 89,550.00 USD | 108,360.00 USD | 31,670.00 USD |
| `1D` | `268.90` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 91,610.00 USD | 43,970.00 USD | 41,690.00 USD |
| `7D` | `268.90` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,100.00 USD |
| `1D` | `269.30` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 28,610.00 USD | 34,530.00 USD | 57,060.00 USD |
| `7D` | `269.40` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,060.00 USD |
| `1D` | `269.70` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 37,480.00 USD | 23,780.00 USD | 8,620.00 USD |
| `7D` | `269.90` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD |
| `1D` | `270.10` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 107,180.00 USD | 21,550.00 USD | 144,890.00 USD |
| `7D` | `270.40` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD |
| `1D` | `270.50` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 91,660.00 USD | 6,950.00 USD | 50,040.00 USD |
| `1D` | `270.90` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 24,050.00 USD | 7,500.00 USD | 94,920.00 USD |
| `7D` | `270.90` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.30` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 64,420.00 USD | 7,760.00 USD | 93,860.00 USD |
| `7D` | `271.40` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.70` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 105,910.00 USD | 7,210.00 USD | 10,130.00 USD |
| `7D` | `271.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 122,330.00 USD | 4,060.00 USD | 12.62 USD |
| `7D` | `272.40` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.50` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 72,620.00 USD | 447.70 USD | 19,730.00 USD |
| `1D` | `272.90` | 949,360.00 USD | 0.00 USD | 949,360.00 USD | 78,920.00 USD | 7,260.00 USD | 0.00 USD |
| `7D` | `272.90` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD |
| `1D` | `273.30` | 863,180.00 USD | 0.00 USD | 863,180.00 USD | 179,400.00 USD | 73.70 USD | 16,110.00 USD |
| `7D` | `273.40` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD |
| `1D` | `273.70` | 667,600.00 USD | 0.00 USD | 667,600.00 USD | 142,060.00 USD | 0.00 USD | 95,820.00 USD |
| `7D` | `273.90` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 375,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.10` | 429,720.00 USD | 0.00 USD | 429,720.00 USD | 178,110.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `274.40` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 496,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.50` | 251,600.00 USD | 0.00 USD | 251,600.00 USD | 194,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.90` | 57,120.00 USD | 0.00 USD | 57,120.00 USD | 57,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 677,870.00 USD | 0.00 USD | 677,870.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.40` | 329,400.00 USD | 0.00 USD | 329,400.00 USD | 3,530.00 USD | 0.00 USD | 110.28 USD |
| `7D` | `275.90` | 325,760.00 USD | 0.00 USD | 325,760.00 USD | 2,560.00 USD | 0.00 USD | 99.71 USD |
| `1D` | `276.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `276.40` | 323,100.00 USD | 0.00 USD | 323,100.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD |
| `7D` | `276.90` | 216,870.00 USD | 0.00 USD | 216,870.00 USD | 44,670.00 USD | 22,950.00 USD | 10.77 USD |
| `1D` | `277.30` | 301.20 USD | 301.20 USD | 0.00 USD | 301.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.40` | 149,240.00 USD | 0.00 USD | 149,240.00 USD | 0.00 USD | 63,290.00 USD | 90.83 USD |
| `7D` | `277.90` | 85,860.00 USD | 0.00 USD | 85,860.00 USD | 0.00 USD | 85,690.00 USD | 163.45 USD |
| `7D` | `278.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `278.40` | 51,190.00 USD | 51,190.00 USD | 0.00 USD | 24,750.00 USD | 26,370.00 USD | 73.93 USD |
| `1D` | `278.90` | 28,680.00 USD | 28,680.00 USD | 0.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD |
| `7D` | `278.90` | 128,750.00 USD | 128,750.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD |
| `1D` | `279.30` | 106,930.00 USD | 106,930.00 USD | 0.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD |
| `7D` | `279.40` | 224,730.00 USD | 224,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD |
| `1D` | `279.70` | 114,620.00 USD | 114,620.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |
| `1D` | `280.10` | 184,120.00 USD | 184,120.00 USD | 0.00 USD | 21,040.00 USD | 11,840.00 USD | 36,620.00 USD |
| `1D` | `280.50` | 300,680.00 USD | 300,680.00 USD | 0.00 USD | 8,720.00 USD | 6,630.00 USD | 101,210.00 USD |
| `1D` | `280.90` | 342,310.00 USD | 342,310.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 29,760.00 USD |
| `1D` | `281.30` | 396,010.00 USD | 396,010.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | 46,760.00 USD |
| `7D` | `281.40` | 301,680.00 USD | 301,680.00 USD | 0.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD |
| `1D` | `281.70` | 422,010.00 USD | 422,010.00 USD | 0.00 USD | 20,590.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.90` | 699,710.00 USD | 699,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD |
| `1D` | `282.10` | 457,960.00 USD | 457,960.00 USD | 0.00 USD | 16,550.00 USD | 15,250.00 USD | 4,140.00 USD |
| `7D` | `282.40` | 755,930.00 USD | 755,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD |
| `1D` | `282.50` | 543,900.00 USD | 543,900.00 USD | 0.00 USD | 40,480.00 USD | 7,210.00 USD | 38,250.00 USD |
| `1D` | `282.90` | 791,450.00 USD | 791,450.00 USD | 0.00 USD | 98,180.00 USD | 13,190.00 USD | 136,180.00 USD |
| `7D` | `282.90` | 788,130.00 USD | 788,130.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.30` | 875,840.00 USD | 875,840.00 USD | 0.00 USD | 31,810.00 USD | 9,540.00 USD | 43,040.00 USD |
| `7D` | `283.40` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 146,510.00 USD |
| `1D` | `283.70` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 45,780.00 USD | 91,060.00 USD |
| `7D` | `283.90` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD |
| `1D` | `284.10` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 38,980.00 USD | 41,630.00 USD | 97,960.00 USD |
| `7D` | `284.40` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 27,700.00 USD | 89,730.00 USD | 42,840.00 USD |
| `1D` | `284.50` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 40,560.00 USD | 83,030.00 USD | 20,690.00 USD |
| `1D` | `284.90` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 8,520.00 USD | 531.60 USD | 54,520.00 USD |
| `7D` | `284.90` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 67,050.00 USD | 391,180.00 USD | 0.00 USD |
| `1D` | `285.30` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 87,540.00 USD | 81,890.00 USD | 80,720.00 USD |
| `7D` | `285.40` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD |
| `1D` | `285.70` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 91,500.00 USD | 80,350.00 USD | 0.00 USD |
| `7D` | `285.90` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD |
| `1D` | `286.10` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,110.00 USD |
| `7D` | `286.40` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 137,400.00 USD | 11.42 USD |
| `1D` | `286.50` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD |
| `1D` | `286.90` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 31,110.00 USD | 30,070.00 USD | 80,710.00 USD |
| `7D` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 51,390.00 USD | 148,230.00 USD | 2.56 USD |
| `1D` | `287.30` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 103,090.00 USD | 26,570.00 USD |
| `7D` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 53,620.00 USD | 103,430.00 USD | 53,370.00 USD |
| `1D` | `287.70` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 17,310.00 USD | 16,870.00 USD | 49,860.00 USD |
| `7D` | `287.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 277,850.00 USD | 23.40 USD |
| `1D` | `288.10` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 20,240.00 USD | 14,410.00 USD | 19,130.00 USD |
| `1D` | `288.50` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 22,610.00 USD | 3,710.00 USD | 5,060.00 USD |
| `1D` | `288.90` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 8,620.00 USD | 1,990.00 USD | 11.96 USD |
| `7D` | `288.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 9.00 USD |
| `1D` | `289.30` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 664.77 USD | 20,430.00 USD | 9,870.00 USD |
| `7D` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `1D` | `289.70` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 957.57 USD | 3,710.00 USD | 14,160.00 USD |
| `7D` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD |
| `1D` | `290.10` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 106.00 USD | 0.00 USD |
| `7D` | `290.40` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 34,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.50` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 403.50 USD | 16,960.00 USD |
| `1D` | `290.90` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 33,370.00 USD | 6,700.00 USD | 3.40 USD |
| `7D` | `290.90` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 5.10 USD |
| `1D` | `291.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 562.74 USD | 10,090.00 USD | 7.76 USD |
| `7D` | `291.40` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 1,340.00 USD | 55,720.00 USD | 19.10 USD |
| `1D` | `291.70` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 375.70 USD | 15,650.00 USD | 22,150.00 USD |
| `7D` | `291.90` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 9.60 USD |
| `1D` | `292.10` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 42,870.00 USD | 8,120.00 USD |
| `7D` | `292.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 71,940.00 USD | 32.44 USD |
| `1D` | `292.50` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 21,960.00 USD | 31,710.00 USD | 10.29 USD |
| `1D` | `292.90` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 21,830.00 USD | 70,670.00 USD | 3.04 USD |
| `7D` | `292.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 119,560.00 USD | 23.76 USD |
| `1D` | `293.30` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 10,630.00 USD | 49,870.00 USD | 27,360.00 USD |
| `7D` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 43.05 USD |
| `1D` | `293.70` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 89,050.00 USD | 51,280.00 USD | 53,800.00 USD |
| `7D` | `293.90` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,030.00 USD |
| `1D` | `294.10` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 23,860.00 USD | 38,720.00 USD | 48,850.00 USD |
| `7D` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 139,780.00 USD | 14,550.00 USD | 60,670.00 USD |
| `1D` | `294.50` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 98,880.00 USD | 82,070.00 USD | 93,000.00 USD |
| `1D` | `294.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 45,360.00 USD | 55,700.00 USD | 35,620.00 USD |
| `7D` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 64,510.00 USD | 107,870.00 USD | 104,920.00 USD |
| `1D` | `295.30` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,550.00 USD | 43,120.00 USD | 63,240.00 USD |
| `7D` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD |
| `1D` | `295.70` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 89,560.00 USD | 21,530.00 USD | 69,660.00 USD |
| `7D` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 108,830.00 USD | 133,090.00 USD | 150,850.00 USD |
| `1D` | `296.10` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 52,710.00 USD | 89,980.00 USD | 29,590.00 USD |
| `7D` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 27,680.00 USD | 77,570.00 USD | 120,810.00 USD |
| `1D` | `296.50` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 43,030.00 USD | 12,250.00 USD | 20,610.00 USD |
| `1D` | `296.90` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 22,010.00 USD | 21,230.00 USD | 78,160.00 USD |
| `7D` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 207,350.00 USD | 50,930.00 USD | 172,360.00 USD |
| `1D` | `297.30` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD |
| `7D` | `297.40` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 4,100.00 USD | 59,290.00 USD | 34,770.00 USD |
| `1D` | `297.70` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 1,810.00 USD | 902.60 USD | 12,060.00 USD |
| `7D` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 17,770.00 USD | 39,840.00 USD | 54,850.00 USD |
| `1D` | `298.10` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 51,550.00 USD | 10,450.00 USD | 41,570.00 USD |
| `7D` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 32,250.00 USD | 42,710.00 USD | 68,810.00 USD |
| `1D` | `298.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 11,480.00 USD | 7,730.00 USD | 56,420.00 USD |
| `1D` | `298.90` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 28,150.00 USD | 13,200.00 USD | 94,670.00 USD |
| `7D` | `298.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 70,090.00 USD | 12,780.00 USD | 40,080.00 USD |
| `1D` | `299.30` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 33,660.00 USD | 16,690.00 USD | 12,340.00 USD |
| `7D` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 4,470.00 USD | 13,080.00 USD | 45,970.00 USD |
| `1D` | `299.70` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 12,530.00 USD | 14,020.00 USD | 29,600.00 USD |
| `7D` | `299.90` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 56,210.00 USD | 10,220.00 USD | 19,830.00 USD |
| `1D` | `300.10` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 30,490.00 USD | 30,850.00 USD | 64,750.00 USD |
| `7D` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 121.42 USD |
| `1D` | `300.50` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 18,940.00 USD | 11,020.00 USD | 17,180.00 USD |
| `1D` | `300.90` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 8,640.00 USD | 15,810.00 USD | 26,660.00 USD |
| `7D` | `300.90` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 24,730.00 USD | 70,210.00 USD | 104,110.00 USD |
| `1D` | `301.30` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 2,520.00 USD | 28,460.00 USD | 19,410.00 USD |
| `7D` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 71,890.00 USD | 56,010.00 USD | 94,620.00 USD |
| `1D` | `301.70` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 19,800.00 USD | 8,210.00 USD | 16,650.00 USD |
| `7D` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 89,300.00 USD | 185,430.00 USD | 26,360.00 USD |
| `1D` | `302.10` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 25,280.00 USD | 33,010.00 USD | 10,340.00 USD |
| `7D` | `302.40` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 50.20 USD |
| `1D` | `302.50` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 10,520.00 USD | 12,750.00 USD | 38,380.00 USD |
| `1D` | `302.90` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 1,230.00 USD | 1,760.00 USD | 13,980.00 USD |
| `7D` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 71,700.00 USD | 110,480.00 USD | 41,930.00 USD |
| `1D` | `303.30` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 31,330.00 USD | 1,690.00 USD | 24,000.00 USD |
| `7D` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 47.58 USD |
| `1D` | `303.70` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 7,540.00 USD | 3,530.00 USD | 6,250.00 USD |
| `7D` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 21,140.00 USD | 11,010.00 USD | 45,900.00 USD |
| `1D` | `304.10` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 21,670.00 USD | 2,210.00 USD | 53,800.00 USD |
| `7D` | `304.40` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 3,670.00 USD | 11,280.00 USD | 259.62 USD |
| `1D` | `304.50` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 13,310.00 USD | 10,980.00 USD | 57,980.00 USD |
| `1D` | `304.90` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 9,920.00 USD | 1,450.00 USD | 2,030.00 USD |
| `7D` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 36,160.00 USD | 18,990.00 USD | 8,410.00 USD |
| `1D` | `305.30` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 10,950.00 USD | 172.52 USD | 2,010.00 USD |
| `7D` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 163,730.00 USD | 127,450.00 USD | 119,210.00 USD |
| `1D` | `305.70` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 7,960.00 USD | 4,710.00 USD | 7,360.00 USD |
| `7D` | `305.90` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 82,000.00 USD | 55,480.00 USD | 10,570.00 USD |
| `1D` | `306.10` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 4,210.00 USD | 2,780.00 USD | 1,340.00 USD |
| `7D` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 39,250.00 USD | 55,740.00 USD | 66,770.00 USD |
| `1D` | `306.50` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 4,410.00 USD | 9,500.00 USD | 5,660.00 USD |
| `1D` | `306.90` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 31,980.00 USD | 40,330.00 USD | 13,050.00 USD |
| `7D` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 84,850.00 USD | 64,520.00 USD | 102,670.00 USD |
| `1D` | `307.30` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 7,930.00 USD | 34,540.00 USD | 17,710.00 USD |
| `7D` | `307.40` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 46,230.00 USD | 154,680.00 USD | 83,290.00 USD |
| `1D` | `307.70` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 32,340.00 USD | 30,450.00 USD | 9,600.00 USD |
| `7D` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 136,380.00 USD | 101,120.00 USD | 65,350.00 USD |
| `1D` | `308.10` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 25,680.00 USD | 11,410.00 USD | 16,370.00 USD |
| `7D` | `308.40` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 152,590.00 USD | 50,070.00 USD | 124,960.00 USD |
| `1D` | `308.50` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 4,640.00 USD | 3,360.00 USD | 4,260.00 USD |
| `1D` | `308.70` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 61,600.00 USD | 52,230.00 USD | 19,690.00 USD |
| `7D` | `309.40` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 28,000.00 USD | 35,530.00 USD | 46,590.00 USD |
| `7D` | `309.90` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 59,490.00 USD | 131,460.00 USD | 144,770.00 USD |
| `7D` | `310.40` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 78,770.00 USD | 123,340.00 USD | 76,870.00 USD |
| `7D` | `310.90` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 35,670.00 USD | 35,930.00 USD | 3,820.00 USD |
| `7D` | `311.40` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 89,390.00 USD | 65,750.00 USD | 47,610.00 USD |
| `7D` | `311.90` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 40,320.00 USD | 11,160.00 USD | 13,520.00 USD |
| `7D` | `312.40` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 38,320.00 USD | 22,970.00 USD | 43,740.00 USD |
| `7D` | `312.90` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 22,600.00 USD | 8,800.00 USD | 38,770.00 USD |
| `7D` | `313.40` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 55,570.00 USD | 24,730.00 USD | 30,370.00 USD |
| `7D` | `313.90` | 11,200,000.00 USD | 11,200,000.00 USD | 0.00 USD | 44,540.00 USD | 15,370.00 USD | 35,930.00 USD |
| `7D` | `314.40` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,850.00 USD |
| `7D` | `314.90` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 39,410.00 USD | 0.00 USD | 10,250.00 USD |
| `7D` | `315.40` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 6,160.00 USD | 9,920.00 USD | 50.67 USD |
| `7D` | `315.90` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 47,110.00 USD | 41,400.00 USD | 29,940.00 USD |
| `7D` | `316.40` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 16,580.00 USD | 40,320.00 USD | 61,810.00 USD |
| `7D` | `316.90` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 9.33 USD |
| `7D` | `317.40` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 14,540.00 USD | 1,010.00 USD | 247.83 USD |
| `7D` | `317.90` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 21,640.00 USD | 8,200.00 USD | 143.05 USD |
| `7D` | `318.40` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 3,320.00 USD | 27,530.00 USD | 22,380.00 USD |
| `7D` | `318.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 11,180.00 USD | 17,970.00 USD | 37,870.00 USD |
| `7D` | `319.40` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 733.55 USD | 18,060.00 USD | 3.21 USD |
| `7D` | `319.90` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 446.22 USD | 22,230.00 USD | 5,370.00 USD |
| `7D` | `320.40` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD |
| `7D` | `320.90` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 2.45 USD |
| `7D` | `321.40` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD |
| `7D` | `321.90` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD |
| `7D` | `322.40` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 22,930.00 USD | 7,950.00 USD | 6,150.00 USD |
| `7D` | `322.90` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 16,590.00 USD | 5,830.00 USD | 53.16 USD |
| `7D` | `323.40` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 14,160.00 USD | 11,950.00 USD | 11,480.00 USD |
| `7D` | `323.90` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 269.10 USD | 692.00 USD | 0.00 USD |
| `7D` | `324.40` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.90` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD |
| `7D` | `325.40` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `296.59M` | Total OI Tokens: `1,074,733.9 BCH`
  * 1h OI Change: `-0.44%` | 4h OI Change: `-5.84%` | 24h OI Change: `-7.91%`
  * Exchange Breakdown: Binance=`87.02M` | Bybit=`37.11M` | OKX=`23.32M` | Hyperliquid=`7.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.03K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0080%` | **USDT OKX** | `-0.0014%` |
| **USDT Bybit** | `-0.0036%` | **USDT KuCoin** | `0.0020%` |
| **USDT MEXC** | `0.0079%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0094%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0044%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `52.42%` | `47.58%` | `1.10` | 2,900,000.00 USD |
| `15M` | `Binance` | `48.31%` | `51.69%` | `0.93` | 925,240.00 USD |
| `15M` | `OKX` | `55.96%` | `44.04%` | `1.27` | 315,950.00 USD |
| `15M` | `Bybit` | `55.68%` | `44.32%` | `1.26` | 228,220.00 USD |
| `15M` | `KuCoin` | `52.79%` | `47.21%` | `1.12` | 168,050.00 USD |
| `15M` | `Gate` | `47.96%` | `52.04%` | `0.92` | 29,500.00 USD |
| `15M` | `Bitget` | `37.05%` | `62.95%` | `0.59` | 34,010.00 USD |
| `15M` | `BingX` | `45.98%` | `54.02%` | `0.85` | 128,310.00 USD |
| `15M` | `MEXC` | `46.61%` | `53.39%` | `0.87` | 266,110.00 USD |
| `15M` | `Bitunix` | `50.36%` | `49.64%` | `1.01` | 58,090.00 USD |
| `15M` | `Hyperliquid` | `14.01%` | `85.99%` | `0.16` | 208,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.33%` | `49.67%` | `1.01` | 246,720.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.06%` | `0.94%` | `105.38` | 292,820.00 USD |
| `15M` | `HTX` | `47.01%` | `52.99%` | `0.89` | 520.89 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.05%` | `93.95%` | `0.06` | 510.96 USD |
| `15M` | `Aster` | `6.4%` | `93.6%` | `0.07` | 2,450.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `48.31%` | `51.69%` | `0.93` | 925,240.00 USD |
| `15M` | `Global Accounts` | `52.42%` | `47.58%` | `1.10` | 2,900,000.00 USD |
| `1H` | `BCH` | `52.12%` | `47.88%` | `1.09` | 16,200,000.00 USD |
| `1H` | `Binance` | `52.19%` | `47.81%` | `1.09` | 5,330,000.00 USD |
| `1H` | `OKX` | `51.74%` | `48.26%` | `1.07` | 1,740,000.00 USD |
| `1H` | `Bybit` | `59.83%` | `40.17%` | `1.49` | 1,250,000.00 USD |
| `1H` | `KuCoin` | `44.26%` | `55.74%` | `0.79` | 267,620.00 USD |
| `1H` | `Gate` | `54.35%` | `45.65%` | `1.19` | 746,900.00 USD |
| `1H` | `Bitget` | `57.07%` | `42.93%` | `1.33` | 277,320.00 USD |
| `1H` | `BingX` | `37.16%` | `62.84%` | `0.59` | 2,790,000.00 USD |
| `1H` | `MEXC` | `48.07%` | `51.93%` | `0.93` | 618,440.00 USD |
| `1H` | `Bitunix` | `60.03%` | `39.97%` | `1.50` | 368,600.00 USD |
| `1H` | `Hyperliquid` | `68.86%` | `31.14%` | `2.21` | 322,870.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.05%` | `50.95%` | `0.96` | 342,640.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `68.15%` | `31.85%` | `2.14` | 1,960,000.00 USD |
| `1H` | `HTX` | `47.64%` | `52.36%` | `0.91` | 19,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.32%` | `59.68%` | `0.68` | 40,870.00 USD |
| `1H` | `Aster` | `11.98%` | `88.02%` | `0.14` | 121,200.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `99.68%` | `0.32%` | `311.50` | 10,470.00 USD |
| `1H` | `Whale Positions` | `52.19%` | `47.81%` | `1.09` | 5,330,000.00 USD |
| `1H` | `Global Accounts` | `52.12%` | `47.88%` | `1.09` | 16,200,000.00 USD |
| `4H` | `BCH` | `48.00%` | `52.00%` | `0.92` | 130,360,000.00 USD |
| `4H` | `Binance` | `45.95%` | `54.05%` | `0.85` | 46,720,000.00 USD |
| `4H` | `OKX` | `48.33%` | `51.67%` | `0.94` | 15,990,000.00 USD |
| `4H` | `Bybit` | `53.72%` | `46.28%` | `1.16` | 15,580,000.00 USD |
| `4H` | `KuCoin` | `44.44%` | `55.56%` | `0.80` | 1,100,000.00 USD |
| `4H` | `Gate` | `47.39%` | `52.61%` | `0.90` | 8,500,000.00 USD |
| `4H` | `Bitget` | `35.94%` | `64.06%` | `0.56` | 4,750,000.00 USD |
| `4H` | `BingX` | `45.05%` | `54.95%` | `0.82` | 10,100,000.00 USD |
| `4H` | `MEXC` | `30.06%` | `69.94%` | `0.43` | 6,170,000.00 USD |
| `4H` | `Bitunix` | `49.25%` | `50.75%` | `0.97` | 2,660,000.00 USD |
| `4H` | `Hyperliquid` | `47.16%` | `52.84%` | `0.89` | 1,850,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.8%` | `52.2%` | `0.92` | 3,140,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `64.91%` | `35.09%` | `1.85` | 11,800,000.00 USD |
| `4H` | `HTX` | `45.45%` | `54.55%` | `0.83` | 637,630.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `66.34%` | `33.66%` | `1.97` | 684,510.00 USD |
| `4H` | `Aster` | `45.43%` | `54.57%` | `0.83` | 541,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `32.23%` | `67.77%` | `0.48` | 155,050.00 USD |
| `4H` | `Whale Positions` | `45.95%` | `54.05%` | `0.85` | 46,720,000.00 USD |
| `4H` | `Global Accounts` | `48.00%` | `52.00%` | `0.92` | 130,360,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `273.26` | `272.72` | `273.26` | `275.70` | `269.30` | 7,511,252.05 USD | 3,875,803.21 USD | 3,635,448.84 USD | 240,354.37 USD | `+3.20%` | `12B / 10S` |
| `0:00 UTC` | `273.80` | `272.56` | `273.80` | `274.68` | `269.76` | 3,951,157.31 USD | 2,047,269.47 USD | 1,903,887.84 USD | 143,381.63 USD | `+3.63%` | `9B / 4S` |
| `5:00 UTC` | `276.40` | `276.70` | `276.40` | `278.76` | `273.60` | 2,981,088.00 USD | 1,514,309.73 USD | 1,466,778.26 USD | 47,531.47 USD | `+1.59%` | `19B / 11S` |
| `0:00 UTC` | `279.50` | `278.78` | `279.50` | `280.00` | `277.16` | 1,923,752.33 USD | 667,499.40 USD | 1,256,252.93 USD | -588,753.54 USD | `-30.60%` | `8B / 42S` |
| `5:00 UTC` | `276.86` | `277.31` | `276.86` | `278.92` | `275.98` | 2,702,816.05 USD | 1,627,166.23 USD | 1,075,649.82 USD | 551,516.40 USD | `+20.41%` | `18B / 30S` |
| `0:00 UTC` | `277.76` | `276.89` | `277.76` | `279.16` | `274.00` | 4,286,596.03 USD | 2,451,355.63 USD | 1,835,240.40 USD | 616,115.23 USD | `+14.37%` | `33B / 11S` |
| `5:00 UTC` | `277.49` | `277.51` | `277.49` | `278.59` | `275.93` | 1,507,866.81 USD | 644,040.10 USD | 863,826.71 USD | -219,786.61 USD | `-14.58%` | `11B / 24S` |
| `0:00 UTC` | `278.41` | `278.31` | `278.41` | `279.47` | `277.01` | 1,126,883.43 USD | 482,083.70 USD | 644,799.73 USD | -162,716.03 USD | `-14.44%` | `11B / 24S` |
| `5:00 UTC` | `276.72` | `277.50` | `276.72` | `278.32` | `276.61` | 1,125,978.55 USD | 475,133.10 USD | 650,845.45 USD | -175,712.36 USD | `-15.61%` | `24B / 42S` |
| `0:00 UTC` | `277.39` | `277.55` | `277.39` | `278.43` | `277.00` | 381,448.88 USD | 120,890.26 USD | 260,558.62 USD | -139,668.35 USD | `-36.62%` | `24B / 42S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 1` | `Divergence` | **`BEARISH`** | Rally without taker buying | `294.56` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.50` | 3,900.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `295.29` | 0.00 USD | 0.00 USD |
| `10-28 16:40` | `Range 1` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `296.45` | 2,100.00 USD | 0.00 USD |
| `10-28 16:31` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.73` | 1,000.00 USD | 0.00 USD |
| `10-28 15:58` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `300.99` | 0.00 USD | 0.00 USD |
| `10-28 15:25` | `Volume 10K BCH` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `304.75` | 0.00 USD | 0.00 USD |
| `10-28 12:36` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.11` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Volume 10K BCH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,500.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `298.39` | 0.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,100.00 USD | 0.00 USD |
| `10-28 11:32` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `298.10` | 0.00 USD | 0.00 USD |
| `10-28 11:24` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.42` | 0.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.64` | 1,000.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `299.34` | 1,200.00 USD | 0.00 USD |
| `10-28 09:12` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.13` | 0.00 USD | 0.00 USD |
| `10-28 08:27` | `Range 1` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `297.20` | 0.00 USD | 0.00 USD |
| `10-28 07:51` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.25` | 2,500.00 USD | 0.00 USD |
| `10-28 07:41` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `295.18` | 0.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 10K BCH` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `293.94` | 2,400.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.42` | 0.00 USD | 0.00 USD |
| `10-28 06:21` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.97` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 15,550.00 USD | -303,820.00 USD | **`DISTRIBUTION`** |
| `15m` | 31,020.00 USD | -349,500.00 USD | **`DISTRIBUTION`** |
| `30m` | 5,000.00 USD | -629,380.00 USD | **`DISTRIBUTION`** |
| `1h` | 125,640.00 USD | -1,060,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 467,210.00 USD | -91,100.00 USD | **`ACCUMULATION`** |
| `4h` | -428,020.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -501,110.00 USD | 215,540.00 USD | **`DISTRIBUTION`** |
| `8h` | -583,410.00 USD | -2,810,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -391,200.00 USD | -1,350,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,370,000.00 USD | -9,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -439,290.00 USD | -13,130,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,340,000.00 USD | -137,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+15.55K` | 15m=`+31.02K` | 1h=`+125.64K` | 24h=`-1.37M`
* Futures Capital Netflows: 5m=`-303.82K` | 15m=`-349.50K` | 1h=`-1.06M` | 24h=`-9.37M`
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
  * Execution Entry: `275.10` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `270.75` (Risk Distance: `4.35` pts)
  * +2.5R Take Profit: `285.97`
  * Mathematical Lot Sizing: **`2.29 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.58` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `282.93` (Risk Distance: `4.35` pts)
  * +2.5R Take Profit: `267.71`
  * Mathematical Lot Sizing: **`2.29 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`278.21`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
