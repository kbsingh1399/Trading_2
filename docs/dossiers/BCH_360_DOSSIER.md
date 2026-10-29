# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 00:08:07 IST` (`2026-10-29 18:38:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `286.26` | **Live Ask Quote**: `286.84` | **Mid Price**: `286.55`
- **Spread Points**: `581.00` | **Spread BPS**: `20.28 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.54` | VWAP Z-Score: `+1.11` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.30` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `57.62` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.07` | Lower -3.00σ Band: `270.01`
  * Upper +2.51σ Band: `293.02` | Lower -2.51σ Band: `272.06`
  * Upper +2.01σ Band: `290.93` | Lower -2.01σ Band: `274.15`
  * Upper +2.00σ Band: `290.89` | Lower -2.00σ Band: `274.19`
  * Upper +1.28σ Band: `287.89` | Lower -1.28σ Band: `277.19`
  * Upper +1.00σ Band: `286.72` | Lower -1.00σ Band: `278.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.81` | EMA-20=`285.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.62` (Slope: `+0.0000`) | EMA-100=`284.20`
  * Institutional Anchors: EMA-144=`284.69` | EMA-200=`284.57` (Slope: `+0.1656`) | EMA-233=`284.82`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.56` (Distance: `-0.33%`)
  * Point of Control (POC) = `278.70` (Distance: `+2.83%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+3.65%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`299.16` | POC=`296.76` | VAL=`289.44`
  * Prior Day Extremes: PDH=`304.16` | PDL=`281.75` | PDC=`288.90`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.22` | Weekly POC=`278.72` | Weekly VAL=`275.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`290.60` | Low=`274.76`
  * London Session (08:00-16:00 UTC): High=`281.86` | Low=`276.86`
  * New York Session (13:00-21:00 UTC): High=`292.96` | Low=`277.16`
  * Initial Balance (First Hour): IB High=`281.86` | IB Low=`279.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `285.40` - `287.70`
  * Optimal Trade Entry (OTE 0.705): `287.12`
  * Structural Invalidation Anchor (0.786): `288.84`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `287.87` | `288.14` | `287.50` | `287.58` | `896` | 257,871.91 USD | -35,064.83 USD | `-13.60%` | -3,078,384.53 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `287.57` | `287.80` | `285.90` | `286.86` | `2,405` | 689,416.81 USD | -117,254.36 USD | `-17.01%` | -3,195,638.88 USD | `-1.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `286.86` | `286.93` | `286.69` | `286.80` | `92` | 26,307.35 USD | 4,354.61 USD | `+16.55%` | -3,191,284.28 USD | `-0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `288.88` | `289.93` | `288.00` | `289.04` | `3,804` | 1,099,157.40 USD | 222,710.03 USD | `+20.26%` | -2,491,049.37 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `289.04` | `289.87` | `287.50` | `287.58` | `2,950` | 851,365.60 USD | 19,696.57 USD | `+2.31%` | -2,471,352.80 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `287.57` | `287.80` | `285.90` | `286.80` | `2,508` | 719,022.07 USD | -116,197.67 USD | `-16.16%` | -2,587,550.46 USD | `-0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -3,009,893.89 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `291.58` | `286.48` | `288.89` | `23,176` | 6,696,574.59 USD | 177,926.21 USD | `+2.66%` | -2,831,967.68 USD | `+0.54` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `288.88` | `289.93` | `285.90` | `286.80` | `9,263` | 2,669,545.07 USD | 126,208.94 USD | `+4.73%` | -2,705,758.74 USD | `+0.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.80` | `80,249` | 23,231,979.10 USD | -1,984,012.96 USD | `-8.54%` | -2,971,017.36 USD | `-0.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.80` | `80,249` | 23,231,979.10 USD | -1,984,012.96 USD | `-8.54%` | -2,971,017.36 USD | `-0.94` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`286.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:05:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1959` | `0x12d2...f97f` | `LONG` | 1,040,953.45 USD | `3,627,243,000,000.00` | `303.26` | `287.62` | `0.000000` | -59,045.89 USD | `-5.67%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.70` (Vol: 152,600.00 USD, Dist: `+2.76%`) | Long MP=`271.76` (Vol: 159,600.00 USD, Dist: `--5.56%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.31%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--5.53%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.31%`) | Long MP=`274.36` (Vol: 203,100.00 USD, Dist: `--4.66%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+2.30%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--8.37%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 469,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 468,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 461,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 457,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 50,900.00 USD | 457,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 171.25 USD | 406,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 406,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 406,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 406,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `141.50` | 2,120.00 USD | 405,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 7,170.00 USD | 403,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 2,070.00 USD | 396,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 394,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 393,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 392,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 389,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 958.26 USD | 389,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 388,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 388,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 387,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 387,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 387,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 742.07 USD | 386,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 385,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `185.50` | 5,840.00 USD | 385,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 782.09 USD | 379,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 1,340.00 USD | 378,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 377,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `193.50` | 786.96 USD | 375,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 375,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 765.08 USD | 374,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 373,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 373,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 39,880.00 USD | 373,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 333,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 333,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `211.50` | 1,110.00 USD | 333,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `212.50` | 106.25 USD | 331,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 4,420.00 USD | 331,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 327,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 5,690.00 USD | 327,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 1,010.00 USD | 321,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 320,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 610.42 USD | 287,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 287,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 285,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 285,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 47,090.00 USD | 284,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 237,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 429.66 USD | 237,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 237,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `235.50` | 1,480.00 USD | 236,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 235,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `241.50` | 367.32 USD | 234,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 9,700.00 USD | 234,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 224,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 220,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 6,480.00 USD | 219,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.50` | 18,650,000.00 USD | 18,650,000.00 USD | 37,900.00 USD | 13,170.00 USD | 32,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 18,570,000.00 USD | 18,570,000.00 USD | 18,160.00 USD | 22,560.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 18,520,000.00 USD | 18,520,000.00 USD | 16,540.00 USD | 28,020.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.70` | 18,470,000.00 USD | 18,470,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.10` | 18,380,000.00 USD | 18,380,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.50` | 18,290,000.00 USD | 18,290,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 212,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.90` | 18,210,000.00 USD | 18,210,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 18,160,000.00 USD | 18,160,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 211,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 18,040,000.00 USD | 18,040,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.10` | 17,880,000.00 USD | 17,880,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.50` | 17,760,000.00 USD | 17,760,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 211,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.90` | 17,660,000.00 USD | 17,660,000.00 USD | 13,480.00 USD | 19,580.00 USD | 14.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 17,630,000.00 USD | 17,630,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 17,540,000.00 USD | 17,540,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.10` | 17,470,000.00 USD | 17,470,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.50` | 17,390,000.00 USD | 17,390,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 210,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.90` | 17,320,000.00 USD | 17,320,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 17,300,000.00 USD | 17,300,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 209,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `255.70` | 17,190,000.00 USD | 17,190,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.10` | 17,110,000.00 USD | 17,110,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.50` | 17,010,000.00 USD | 17,010,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.90` | 16,940,000.00 USD | 16,940,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 16,840,000.00 USD | 16,840,000.00 USD | 23,000.00 USD | 1,850.00 USD | 27,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 5,670.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.70` | 16,790,000.00 USD | 16,790,000.00 USD | 47,180.00 USD | 6,040.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 8,020,000.00 USD | 8,020,000.00 USD | 32.50 USD | 4,120.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.10` | 16,720,000.00 USD | 16,720,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 8,000,000.00 USD | 8,000,000.00 USD | 1,470.00 USD | 5,260.00 USD | 45.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.50` | 16,580,000.00 USD | 16,580,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.90` | 7,990,000.00 USD | 7,990,000.00 USD | 17,930.00 USD | 11,000.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 16,430,000.00 USD | 16,430,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 7,950,000.00 USD | 7,950,000.00 USD | 13,160.00 USD | 4,150.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 16,370,000.00 USD | 16,370,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 7,920,000.00 USD | 7,920,000.00 USD | 14,700.00 USD | 16,830.00 USD | 15,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 16,320,000.00 USD | 16,320,000.00 USD | 17,070.00 USD | 13,660.00 USD | 250.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 7,870,000.00 USD | 7,870,000.00 USD | 5,100.00 USD | 9,630.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.10` | 16,290,000.00 USD | 16,290,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 7,840,000.00 USD | 7,840,000.00 USD | 2,850.00 USD | 8,760.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.50` | 16,250,000.00 USD | 16,250,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.90` | 7,820,000.00 USD | 7,820,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 16,190,000.00 USD | 16,190,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 7,780,000.00 USD | 7,780,000.00 USD | 8,660.00 USD | 16,360.00 USD | 500.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 16,100,000.00 USD | 16,100,000.00 USD | 2,490.00 USD | 33,470.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 7,750,000.00 USD | 7,750,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 16,050,000.00 USD | 16,050,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 7,740,000.00 USD | 7,740,000.00 USD | 517.32 USD | 4,790.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.10` | 15,950,000.00 USD | 15,950,000.00 USD | 60,340.00 USD | 35,350.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 7,720,000.00 USD | 7,720,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.50` | 15,820,000.00 USD | 15,820,000.00 USD | 36,590.00 USD | 26,590.00 USD | 50.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 7,710,000.00 USD | 7,710,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 15,760,000.00 USD | 15,760,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 7,710,000.00 USD | 7,710,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 15,630,000.00 USD | 15,630,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 7,680,000.00 USD | 7,680,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 15,530,000.00 USD | 15,530,000.00 USD | 265,940.00 USD | 96,750.00 USD | 26,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 7,670,000.00 USD | 7,670,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.10` | 15,140,000.00 USD | 15,140,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 7,660,000.00 USD | 7,660,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.50` | 14,970,000.00 USD | 14,970,000.00 USD | 49,620.00 USD | 16,400.00 USD | 37,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.90` | 7,630,000.00 USD | 7,630,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 14,870,000.00 USD | 14,870,000.00 USD | 22,920.00 USD | 75,260.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 7,580,000.00 USD | 7,580,000.00 USD | 20,730.00 USD | 8,710.00 USD | 33,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 14,760,000.00 USD | 14,760,000.00 USD | 133,130.00 USD | 59,960.00 USD | 111,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 7,520,000.00 USD | 7,520,000.00 USD | 23,810.00 USD | 23,390.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.70` | 14,450,000.00 USD | 14,450,000.00 USD | 54,220.00 USD | 81,830.00 USD | 61,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 7,440,000.00 USD | 7,440,000.00 USD | 10,200.00 USD | 335.05 USD | 7.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.10` | 14,250,000.00 USD | 14,250,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 7,430,000.00 USD | 7,430,000.00 USD | 27,700.00 USD | 3,150.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.50` | 13,900,000.00 USD | 13,900,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.90` | 7,390,000.00 USD | 7,390,000.00 USD | 32,310.00 USD | 6,620.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 13,580,000.00 USD | 13,580,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 7,340,000.00 USD | 7,340,000.00 USD | 17,990.00 USD | 11,070.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 13,220,000.00 USD | 13,220,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 7,310,000.00 USD | 7,310,000.00 USD | 83,350.00 USD | 112,140.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.70` | 12,860,000.00 USD | 12,860,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 7,100,000.00 USD | 7,100,000.00 USD | 55,490.00 USD | 80,400.00 USD | 47,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.10` | 12,420,000.00 USD | 12,420,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 6,920,000.00 USD | 6,920,000.00 USD | 57,190.00 USD | 101,540.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.50` | 11,930,000.00 USD | 11,930,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.90` | 6,730,000.00 USD | 6,730,000.00 USD | 92,000.00 USD | 36,230.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 11,510,000.00 USD | 11,510,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 6,560,000.00 USD | 6,560,000.00 USD | 28,630.00 USD | 16,320.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 11,110,000.00 USD | 11,110,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.70` | 6,490,000.00 USD | 6,490,000.00 USD | 39,120.00 USD | 24,350.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.70` | 10,560,000.00 USD | 10,560,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 6,420,000.00 USD | 6,420,000.00 USD | 98,640.00 USD | 77,570.00 USD | 98,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.10` | 10,410,000.00 USD | 10,410,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 6,140,000.00 USD | 6,140,000.00 USD | 71,720.00 USD | 36,250.00 USD | 36,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.50` | 10,000,000.00 USD | 10,000,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 106.31 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.90` | 6,000,000.00 USD | 6,000,000.00 USD | 11,770.00 USD | 24,230.00 USD | 66,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 9,610,000.00 USD | 9,610,000.00 USD | 318,780.00 USD | 144,560.00 USD | 90,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 5,900,000.00 USD | 5,900,000.00 USD | 56,610.00 USD | 46,210.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 9,050,000.00 USD | 9,050,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.70` | 5,720,000.00 USD | 5,720,000.00 USD | 20,310.00 USD | 13,930.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.70` | 8,760,000.00 USD | 8,760,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 5,680,000.00 USD | 5,680,000.00 USD | 109,050.00 USD | 32,950.00 USD | 17,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.10` | 8,260,000.00 USD | 8,260,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 5,520,000.00 USD | 5,520,000.00 USD | 81,660.00 USD | 31,310.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.50` | 7,780,000.00 USD | 7,780,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 5,360,000.00 USD | 5,360,000.00 USD | 80,060.00 USD | 58,140.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 7,420,000.00 USD | 7,420,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 5,210,000.00 USD | 5,210,000.00 USD | 179,830.00 USD | 208,970.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 6,980,000.00 USD | 6,980,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 4,790,000.00 USD | 4,790,000.00 USD | 142,100.00 USD | 172,310.00 USD | 117,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 6,290,000.00 USD | 6,290,000.00 USD | 195,450.00 USD | 467,590.00 USD | 206,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 4,360,000.00 USD | 4,360,000.00 USD | 120,870.00 USD | 232,210.00 USD | 71,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.10` | 5,420,000.00 USD | 5,420,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 3,930,000.00 USD | 3,930,000.00 USD | 195,280.00 USD | 71,370.00 USD | 111,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.50` | 4,570,000.00 USD | 4,570,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.90` | 3,560,000.00 USD | 3,560,000.00 USD | 57,970.00 USD | 37,710.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 3,970,000.00 USD | 3,970,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 3,410,000.00 USD | 3,410,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 3,450,000.00 USD | 3,450,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 3,240,000.00 USD | 3,240,000.00 USD | 12,170.00 USD | 37,310.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 3,310,000.00 USD | 3,310,000.00 USD | 1,350.00 USD | 51,050.00 USD | 51.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 3,180,000.00 USD | 3,180,000.00 USD | 82,210.00 USD | 48,180.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.10` | 3,250,000.00 USD | 3,250,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 3,030,000.00 USD | 3,030,000.00 USD | 27,970.00 USD | 31,830.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.50` | 3,250,000.00 USD | 3,250,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.90` | 2,960,000.00 USD | 2,960,000.00 USD | 10,750.00 USD | 20,770.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 3,250,000.00 USD | 3,250,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 2,920,000.00 USD | 2,920,000.00 USD | 28,530.00 USD | 66,900.00 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 63,290.00 USD | 36.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 2,770,000.00 USD | 2,770,000.00 USD | 57,640.00 USD | 47,660.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 27,190.00 USD | 84,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 2,650,000.00 USD | 2,650,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.10` | 2,980,000.00 USD | 2,980,000.00 USD | 24,750.00 USD | 0.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 2,600,000.00 USD | 2,600,000.00 USD | 67,950.00 USD | 33,500.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.50` | 2,900,000.00 USD | 2,900,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 2,460,000.00 USD | 2,460,000.00 USD | 24,100.00 USD | 27,270.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.90` | 2,810,000.00 USD | 2,810,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 2,400,000.00 USD | 2,400,000.00 USD | 53,390.00 USD | 33,630.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 2,720,000.00 USD | 2,720,000.00 USD | 31,330.00 USD | 0.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 2,270,000.00 USD | 2,270,000.00 USD | 20,320.00 USD | 0.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 2,650,000.00 USD | 2,650,000.00 USD | 46,800.00 USD | 0.00 USD | 54,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 2,240,000.00 USD | 2,240,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 2,180,000.00 USD | 2,180,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.50` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 36.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.90` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 69.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 2,060,000.00 USD | 2,060,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.70` | 1,990,000.00 USD | 1,990,000.00 USD | 9,360.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 2,480,000.00 USD | 2,480,000.00 USD | 565.82 USD | 0.00 USD | 122,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 1,950,000.00 USD | 1,950,000.00 USD | 55,330.00 USD | 39,110.00 USD | 187,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.10` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.50` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 13,450.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.50` | 2,230,000.00 USD | 2,230,000.00 USD | 32,190.00 USD | 0.00 USD | 39,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.90` | 1,650,000.00 USD | 1,650,000.00 USD | 38,030.00 USD | 54,510.00 USD | 80,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 97.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 1,480,000.00 USD | 1,480,000.00 USD | 18,430.00 USD | 0.00 USD | 112,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 37,310.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.70` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 30,480.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 238,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 1,260,000.00 USD | 1,260,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.10` | 1,790,000.00 USD | 1,790,000.00 USD | 49,500.00 USD | 0.00 USD | 135,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.50` | 1,130,000.00 USD | 1,130,000.00 USD | 39,670.00 USD | 70,600.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.50` | 1,600,000.00 USD | 1,600,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.90` | 994,860.00 USD | 994,860.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.90` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.30` | 965,760.00 USD | 965,760.00 USD | 20,960.00 USD | 64,640.00 USD | 93,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.30` | 1,060,000.00 USD | 1,060,000.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.70` | 786,470.00 USD | 786,470.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.70` | 771,160.00 USD | 771,160.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.10` | 623,850.00 USD | 623,850.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.10` | 657,530.00 USD | 657,530.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.50` | 593,850.00 USD | 593,850.00 USD | 111,830.00 USD | 47,210.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.50` | 582,680.00 USD | 582,680.00 USD | 23,860.00 USD | 95,580.00 USD | 31.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.90` | 397,290.00 USD | 397,290.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.90` | 463,210.00 USD | 463,210.00 USD | 27,530.00 USD | 141,160.00 USD | 2.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.30` | 101,950.00 USD | 101,950.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.30` | 294,520.00 USD | 294,520.00 USD | 53,620.00 USD | 86,570.00 USD | 0.99 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.70` | 33,650.00 USD | 33,650.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.70` | 67,300.00 USD | 67,300.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.70` | 154,340.00 USD | 154,340.00 USD | 0.00 USD | 154,260.00 USD | 77.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 78,660.00 USD | 78,660.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.10` | 139,310.00 USD | 139,310.00 USD | 0.00 USD | 139,290.00 USD | 15.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 139,310.00 USD | 139,310.00 USD | 0.00 USD | 0.00 USD | 6.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 90,660.00 USD | 90,660.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 139,340.00 USD | 139,340.00 USD | 0.00 USD | 0.00 USD | 22.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 141,210.00 USD | 141,210.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.10` | 141,240.00 USD | 141,240.00 USD | 0.00 USD | 0.00 USD | 33.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.50` | 141,260.00 USD | 141,260.00 USD | 0.00 USD | 0.00 USD | 16.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `290.50` | 1,210.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `290.90` | 90,660.00 USD | 90,660.00 USD | 0.00 USD | 0.00 USD | 3.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 128,960.00 USD | 128,960.00 USD | 0.00 USD | 38,290.00 USD | 7.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 150,520.00 USD | 150,520.00 USD | 0.00 USD | 9,250.00 USD | 11.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.70` | 166,730.00 USD | 166,730.00 USD | 0.00 USD | 15,650.00 USD | 22,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 244,620.00 USD | 244,620.00 USD | 0.00 USD | 94,090.00 USD | 14.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 205,100.00 USD | 205,100.00 USD | 0.00 USD | 38,360.00 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.10` | 363,320.00 USD | 363,320.00 USD | 0.00 USD | 118,660.00 USD | 38.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 252,470.00 USD | 252,470.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.50` | 390,020.00 USD | 390,020.00 USD | 0.00 USD | 26,610.00 USD | 96.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 334,730.00 USD | 334,730.00 USD | 1,020.00 USD | 81,240.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 508,540.00 USD | 508,540.00 USD | 0.00 USD | 118,480.00 USD | 41.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 395,800.00 USD | 395,800.00 USD | 476.80 USD | 60,590.00 USD | 1.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 621,650.00 USD | 621,650.00 USD | 534.50 USD | 112,560.00 USD | 21.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 607,490.00 USD | 607,490.00 USD | 73,230.00 USD | 77,060.00 USD | 61,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 660,160.00 USD | 660,160.00 USD | 37,280.00 USD | 1,170.00 USD | 64.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 692,810.00 USD | 692,810.00 USD | 30,790.00 USD | 36,360.00 USD | 18,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.10` | 884,710.00 USD | 884,710.00 USD | 85,150.00 USD | 33,590.00 USD | 105,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 983,470.00 USD | 983,470.00 USD | 114,260.00 USD | 98,900.00 USD | 77,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.50` | 969,700.00 USD | 969,700.00 USD | 69,950.00 USD | 15,030.00 USD | 8.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 1,220,000.00 USD | 1,220,000.00 USD | 53,910.00 USD | 79,400.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 1,230,000.00 USD | 1,230,000.00 USD | 63,470.00 USD | 92,770.00 USD | 104,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 1,480,000.00 USD | 1,480,000.00 USD | 95,260.00 USD | 75,850.00 USD | 85,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 1,590,000.00 USD | 1,590,000.00 USD | 45,590.00 USD | 65,580.00 USD | 252,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 1,740,000.00 USD | 1,740,000.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 1,910,000.00 USD | 1,910,000.00 USD | 105,410.00 USD | 72,570.00 USD | 133,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 1,980,000.00 USD | 1,980,000.00 USD | 90,530.00 USD | 119,980.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.10` | 2,190,000.00 USD | 2,190,000.00 USD | 75,740.00 USD | 90,470.00 USD | 119,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 2,100,000.00 USD | 2,100,000.00 USD | 43,030.00 USD | 34,820.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.50` | 2,330,000.00 USD | 2,330,000.00 USD | 1,060.00 USD | 77,140.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 2,270,000.00 USD | 2,270,000.00 USD | 29,430.00 USD | 50,150.00 USD | 91,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 2,720,000.00 USD | 2,720,000.00 USD | 206,840.00 USD | 51,220.00 USD | 134,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 2,360,000.00 USD | 2,360,000.00 USD | 57,730.00 USD | 359.06 USD | 28,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 2,730,000.00 USD | 2,730,000.00 USD | 3,960.00 USD | 2,500.00 USD | 68.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 2,370,000.00 USD | 2,370,000.00 USD | 807.94 USD | 723.06 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 2,820,000.00 USD | 2,820,000.00 USD | 144.38 USD | 56,790.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 2,480,000.00 USD | 2,480,000.00 USD | 44,470.00 USD | 8,120.00 USD | 53,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.10` | 3,000,000.00 USD | 3,000,000.00 USD | 49,240.00 USD | 80,820.00 USD | 54,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 2,590,000.00 USD | 2,590,000.00 USD | 8,410.00 USD | 21,250.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.50` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 12,660.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 2,760,000.00 USD | 2,760,000.00 USD | 34,670.00 USD | 15,820.00 USD | 118,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 3,170,000.00 USD | 3,170,000.00 USD | 70,090.00 USD | 993.25 USD | 40,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 2,870,000.00 USD | 2,870,000.00 USD | 59,910.00 USD | 23,800.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 3,220,000.00 USD | 3,220,000.00 USD | 2,570.00 USD | 1,380.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 2,900,000.00 USD | 2,900,000.00 USD | 4,910.00 USD | 17,410.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 3,260,000.00 USD | 3,260,000.00 USD | 5,310.00 USD | 7,720.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 3,030,000.00 USD | 3,030,000.00 USD | 51,990.00 USD | 44,530.00 USD | 35,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.10` | 3,310,000.00 USD | 3,310,000.00 USD | 51,500.00 USD | 2,470.00 USD | 41.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 3,100,000.00 USD | 3,100,000.00 USD | 11,190.00 USD | 10,850.00 USD | 41,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.50` | 3,370,000.00 USD | 3,370,000.00 USD | 866.20 USD | 36,230.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 3,180,000.00 USD | 3,180,000.00 USD | 12,920.00 USD | 32,390.00 USD | 36,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 3,510,000.00 USD | 3,510,000.00 USD | 24,730.00 USD | 34,630.00 USD | 84,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 3,290,000.00 USD | 3,290,000.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 3,730,000.00 USD | 3,730,000.00 USD | 71,140.00 USD | 55,420.00 USD | 94,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.70` | 3,360,000.00 USD | 3,360,000.00 USD | 31,990.00 USD | 20,360.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.70` | 3,900,000.00 USD | 3,900,000.00 USD | 37,640.00 USD | 130,520.00 USD | 14.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 3,450,000.00 USD | 3,450,000.00 USD | 44,680.00 USD | 37,100.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.10` | 4,100,000.00 USD | 4,100,000.00 USD | 53,220.00 USD | 123,390.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 3,510,000.00 USD | 3,510,000.00 USD | 10,520.00 USD | 20,540.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.50` | 4,280,000.00 USD | 4,280,000.00 USD | 31,330.00 USD | 102,200.00 USD | 41,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 3,540,000.00 USD | 3,540,000.00 USD | 1,230.00 USD | 1,850.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 4,380,000.00 USD | 4,380,000.00 USD | 40,380.00 USD | 64,640.00 USD | 150.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 3,580,000.00 USD | 3,580,000.00 USD | 32,880.00 USD | 413.69 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 173.09 USD | 6.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 3,600,000.00 USD | 3,600,000.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 4,430,000.00 USD | 4,430,000.00 USD | 17,370.00 USD | 8,710.00 USD | 24,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 3,680,000.00 USD | 3,680,000.00 USD | 22,560.00 USD | 1,100.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.10` | 4,440,000.00 USD | 4,440,000.00 USD | 5,440.00 USD | 1,950.00 USD | 154.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 3,760,000.00 USD | 3,760,000.00 USD | 13,310.00 USD | 9,720.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.50` | 4,460,000.00 USD | 4,460,000.00 USD | 3,480.00 USD | 11,110.00 USD | 92.29 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `304.50` | 1,040.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `304.90` | 3,760,000.00 USD | 3,760,000.00 USD | 697.80 USD | 240.63 USD | 2.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 4,520,000.00 USD | 4,520,000.00 USD | 34,680.00 USD | 18,990.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 3,770,000.00 USD | 3,770,000.00 USD | 11,210.00 USD | 90.03 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 4,930,000.00 USD | 4,930,000.00 USD | 162,420.00 USD | 128,450.00 USD | 117,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 3,780,000.00 USD | 3,780,000.00 USD | 7,960.00 USD | 1,770.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 5,040,000.00 USD | 5,040,000.00 USD | 82,270.00 USD | 18,170.00 USD | 17,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 3,790,000.00 USD | 3,790,000.00 USD | 4,210.00 USD | 2,750.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.10` | 5,180,000.00 USD | 5,180,000.00 USD | 22,930.00 USD | 68,220.00 USD | 45,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 3,810,000.00 USD | 3,810,000.00 USD | 4,740.00 USD | 9,750.00 USD | 58.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.50` | 5,320,000.00 USD | 5,320,000.00 USD | 30,150.00 USD | 41,830.00 USD | 65,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 3,890,000.00 USD | 3,890,000.00 USD | 32,060.00 USD | 40,210.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 5,490,000.00 USD | 5,490,000.00 USD | 58,810.00 USD | 50,570.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 3,950,000.00 USD | 3,950,000.00 USD | 7,930.00 USD | 34,540.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 5,730,000.00 USD | 5,730,000.00 USD | 34,320.00 USD | 123,720.00 USD | 83,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 4,000,000.00 USD | 4,000,000.00 USD | 19,670.00 USD | 27,980.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 5,910,000.00 USD | 5,910,000.00 USD | 84,930.00 USD | 74,370.00 USD | 24,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 4,060,000.00 USD | 4,060,000.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.10` | 6,190,000.00 USD | 6,190,000.00 USD | 106,040.00 USD | 63,640.00 USD | 106,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 4,070,000.00 USD | 4,070,000.00 USD | 5,570.00 USD | 3,510.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.50` | 6,440,000.00 USD | 6,440,000.00 USD | 118,090.00 USD | 64,440.00 USD | 65,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 4,090,000.00 USD | 4,090,000.00 USD | 12,710.00 USD | 6,030.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 6,550,000.00 USD | 6,550,000.00 USD | 60,660.00 USD | 31,940.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 4,120,000.00 USD | 4,120,000.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 6,640,000.00 USD | 6,640,000.00 USD | 27,920.00 USD | 26,240.00 USD | 36,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 4,150,000.00 USD | 4,150,000.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 6,970,000.00 USD | 6,970,000.00 USD | 40,410.00 USD | 132,660.00 USD | 153,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 4,160,000.00 USD | 4,160,000.00 USD | 4,390.00 USD | 4,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.10` | 7,130,000.00 USD | 7,130,000.00 USD | 34,250.00 USD | 63,360.00 USD | 62,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 4,160,000.00 USD | 4,160,000.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.50` | 7,290,000.00 USD | 7,290,000.00 USD | 68,560.00 USD | 73,280.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 5,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 2.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 7,360,000.00 USD | 7,360,000.00 USD | 35,670.00 USD | 30,720.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 4,170,000.00 USD | 4,170,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 7,560,000.00 USD | 7,560,000.00 USD | 84,180.00 USD | 65,480.00 USD | 47,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `311.50` | 539.21 USD | 5,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `311.70` | 4,190,000.00 USD | 4,190,000.00 USD | 9,900.00 USD | 6,590.00 USD | 4.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 7,630,000.00 USD | 7,630,000.00 USD | 34,040.00 USD | 11,430.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 4,190,000.00 USD | 4,190,000.00 USD | 244.00 USD | 39.75 USD | 29.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.10` | 7,710,000.00 USD | 7,710,000.00 USD | 46,850.00 USD | 1,100.00 USD | 24,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 4,210,000.00 USD | 4,210,000.00 USD | 8,760.00 USD | 7,440.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.50` | 7,800,000.00 USD | 7,800,000.00 USD | 19,540.00 USD | 22,180.00 USD | 49,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 4,220,000.00 USD | 4,220,000.00 USD | 11,420.00 USD | 23.27 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 7,870,000.00 USD | 7,870,000.00 USD | 22,600.00 USD | 20,090.00 USD | 30,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 4,240,000.00 USD | 4,240,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 7,990,000.00 USD | 7,990,000.00 USD | 64,910.00 USD | 30,120.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 4,250,000.00 USD | 4,250,000.00 USD | 8,340.00 USD | 86.80 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 8,060,000.00 USD | 8,060,000.00 USD | 32,170.00 USD | 15,010.00 USD | 23,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 11,670.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.10` | 8,130,000.00 USD | 8,130,000.00 USD | 26,810.00 USD | 362.37 USD | 47,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 4,280,000.00 USD | 4,280,000.00 USD | 4,210.00 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.50` | 8,210,000.00 USD | 8,210,000.00 USD | 48,630.00 USD | 307.60 USD | 24,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 8,250,000.00 USD | 8,250,000.00 USD | 29,590.00 USD | 0.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 4,290,000.00 USD | 4,290,000.00 USD | 32.50 USD | 144.50 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 8,250,000.00 USD | 8,250,000.00 USD | 5,690.00 USD | 547.95 USD | 51.95 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `315.50` | 6,520.00 USD | 12,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `315.70` | 4,320,000.00 USD | 4,320,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 8,360,000.00 USD | 8,360,000.00 USD | 9,200.00 USD | 50,270.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 4,340,000.00 USD | 4,340,000.00 USD | 5,020.00 USD | 5,050.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.10` | 8,460,000.00 USD | 8,460,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 4,360,000.00 USD | 4,360,000.00 USD | 12,950.00 USD | 5,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.50` | 8,520,000.00 USD | 8,520,000.00 USD | 16,120.00 USD | 20,630.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.90` | 4,390,000.00 USD | 4,390,000.00 USD | 12,760.00 USD | 3,660.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 8,530,000.00 USD | 8,530,000.00 USD | 3,030.00 USD | 10,840.00 USD | 41.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.30` | 4,390,000.00 USD | 4,390,000.00 USD | 2,250.00 USD | 4,170.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 8,550,000.00 USD | 8,550,000.00 USD | 14,540.00 USD | 748.91 USD | 196.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.70` | 4,450,000.00 USD | 4,450,000.00 USD | 15,260.00 USD | 15,360.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 8,550,000.00 USD | 8,550,000.00 USD | 620.15 USD | 265.17 USD | 37.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.10` | 4,470,000.00 USD | 4,470,000.00 USD | 2,290.00 USD | 9,270.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.10` | 8,580,000.00 USD | 8,580,000.00 USD | 22,250.00 USD | 9,100.00 USD | 148.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.50` | 4,490,000.00 USD | 4,490,000.00 USD | 4,700.00 USD | 7,500.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.50` | 8,650,000.00 USD | 8,650,000.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.90` | 4,520,000.00 USD | 4,520,000.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 8,700,000.00 USD | 8,700,000.00 USD | 10,270.00 USD | 17,970.00 USD | 23,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.30` | 4,550,000.00 USD | 4,550,000.00 USD | 8,590.00 USD | 16,300.00 USD | 488.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 18,060.00 USD | 49.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.70` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 8,730,000.00 USD | 8,730,000.00 USD | 936.82 USD | 12,700.00 USD | 2.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.10` | 4,570,000.00 USD | 4,570,000.00 USD | 4,350.00 USD | 4,210.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.10` | 8,800,000.00 USD | 8,800,000.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.50` | 4,580,000.00 USD | 4,580,000.00 USD | 8,130.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.50` | 8,830,000.00 USD | 8,830,000.00 USD | 15,190.00 USD | 10,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 13,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.30` | 8,850,000.00 USD | 8,850,000.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.70` | 8,880,000.00 USD | 8,880,000.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.10` | 8,920,000.00 USD | 8,920,000.00 USD | 22,940.00 USD | 8,290.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.50` | 8,920,000.00 USD | 8,920,000.00 USD | 555.20 USD | 365.55 USD | 0.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 8,940,000.00 USD | 8,940,000.00 USD | 16,590.00 USD | 5,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.30` | 8,980,000.00 USD | 8,980,000.00 USD | 14,160.00 USD | 5,860.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.70` | 8,980,000.00 USD | 8,980,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.10` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 13,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `340.50` | 1,360.00 USD | 15,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `356.50` | 39,220.00 USD | 54,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 55,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 55,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `395.50` | 3,430.00 USD | 59,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `427.50` | 9,480.00 USD | 68,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 77,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 123,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 1,040.00 USD | 124,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `533.50` | 177.66 USD | 124,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 125,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `565.50` | 1,450.00 USD | 127,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `95.50` | 469,140.00 USD | 0.00 USD | 920.05 USD | `-66.96%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 468,220.00 USD | 0.00 USD | 6,240.00 USD | `-64.88%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 461,980.00 USD | 0.00 USD | 4,080.00 USD | `-64.54%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 457,910.00 USD | 0.00 USD | 212.76 USD | `-62.11%` | `1,943,000,000.00` |
| `Live` | `Long` | `115.50` | 457,690.00 USD | 0.00 USD | 50,900.00 USD | `-60.04%` | `440,704,000,000.00` |
| `Live` | `Long` | `116.50` | 406,790.00 USD | 0.00 USD | 171.25 USD | `-59.69%` | `1,470,000,000.00` |
| `Live` | `Long` | `118.50` | 406,620.00 USD | 0.00 USD | 212.35 USD | `-59.00%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 406,410.00 USD | 0.00 USD | 124.46 USD | `-57.62%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 406,280.00 USD | 0.00 USD | 658.18 USD | `-56.23%` | `5,203,000,000.00` |
| `Live` | `Long` | `141.50` | 405,620.00 USD | 0.00 USD | 2,120.00 USD | `-51.04%` | `15,000,000,000.00` |
| `Live` | `Long` | `143.50` | 403,500.00 USD | 0.00 USD | 7,170.00 USD | `-50.35%` | `50,000,000,000.00` |
| `Live` | `Long` | `145.50` | 396,330.00 USD | 0.00 USD | 2,070.00 USD | `-49.66%` | `14,200,000,000.00` |
| `Live` | `Long` | `147.50` | 394,260.00 USD | 0.00 USD | 895.47 USD | `-48.97%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 393,370.00 USD | 0.00 USD | 1,270.00 USD | `-48.62%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 392,100.00 USD | 0.00 USD | 2,370.00 USD | `-48.27%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 389,730.00 USD | 0.00 USD | 303.78 USD | `-47.24%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 389,430.00 USD | 0.00 USD | 958.26 USD | `-43.78%` | `5,897,000,000.00` |
| `Live` | `Long` | `167.50` | 388,470.00 USD | 0.00 USD | 285.75 USD | `-42.05%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 388,190.00 USD | 0.00 USD | 426.25 USD | `-41.01%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 387,760.00 USD | 0.00 USD | 169.96 USD | `-39.62%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 387,590.00 USD | 0.00 USD | 516.67 USD | `-39.28%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 387,070.00 USD | 0.00 USD | 373.83 USD | `-38.93%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 386,700.00 USD | 0.00 USD | 742.07 USD | `-36.51%` | `4,044,000,000.00` |
| `Live` | `Long` | `184.50` | 385,960.00 USD | 0.00 USD | 616.05 USD | `-36.16%` | `3,339,000,000.00` |
| `Live` | `Long` | `185.50` | 385,340.00 USD | 0.00 USD | 5,840.00 USD | `-35.82%` | `31,500,000,000.00` |
| `Live` | `Long` | `188.50` | 379,500.00 USD | 0.00 USD | 782.09 USD | `-34.78%` | `4,149,000,000.00` |
| `Live` | `Long` | `191.50` | 378,720.00 USD | 0.00 USD | 1,340.00 USD | `-33.74%` | `6,983,000,000.00` |
| `Live` | `Long` | `192.50` | 377,380.00 USD | 0.00 USD | 1,490.00 USD | `-33.40%` | `7,715,000,000.00` |
| `Live` | `Long` | `193.50` | 375,890.00 USD | 0.00 USD | 786.96 USD | `-33.05%` | `4,067,000,000.00` |
| `Live` | `Long` | `195.50` | 375,110.00 USD | 0.00 USD | 370.47 USD | `-32.36%` | `1,895,000,000.00` |
| `Live` | `Long` | `199.50` | 374,740.00 USD | 0.00 USD | 765.08 USD | `-30.97%` | `3,835,000,000.00` |
| `Live` | `Long` | `200.50` | 373,970.00 USD | 0.00 USD | 293.13 USD | `-30.63%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 373,680.00 USD | 0.00 USD | 420.39 USD | `-29.94%` | `2,076,000,000.00` |
| `Live` | `Long` | `204.50` | 373,260.00 USD | 0.00 USD | 39,880.00 USD | `-29.24%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 333,370.00 USD | 0.00 USD | 191.53 USD | `-28.90%` | `932,000,000.00` |
| `Live` | `Long` | `210.50` | 333,180.00 USD | 0.00 USD | 108.83 USD | `-27.17%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 333,070.00 USD | 0.00 USD | 1,110.00 USD | `-26.82%` | `5,260,000,000.00` |
| `Live` | `Long` | `212.50` | 331,960.00 USD | 0.00 USD | 106.25 USD | `-26.48%` | `500,000,000.00` |
| `Live` | `Long` | `213.50` | 331,860.00 USD | 0.00 USD | 4,420.00 USD | `-26.13%` | `20,686,000,000.00` |
| `Live` | `Long` | `215.50` | 327,440.00 USD | 0.00 USD | 239.85 USD | `-25.44%` | `1,113,000,000.00` |
| `Live` | `Long` | `219.50` | 327,200.00 USD | 0.00 USD | 5,690.00 USD | `-24.05%` | `25,931,000,000.00` |
| `Live` | `Long` | `220.50` | 321,510.00 USD | 0.00 USD | 1,010.00 USD | `-23.71%` | `4,592,000,000.00` |
| `Live` | `Long` | `223.50` | 320,490.00 USD | 0.00 USD | 32,860.00 USD | `-22.67%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 287,630.00 USD | 0.00 USD | 610.42 USD | `-22.32%` | `2,719,000,000.00` |
| `Live` | `Long` | `226.50` | 287,020.00 USD | 0.00 USD | 1,240.00 USD | `-21.63%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 285,790.00 USD | 0.00 USD | 174.49 USD | `-21.29%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 285,610.00 USD | 0.00 USD | 642.77 USD | `-20.94%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 284,970.00 USD | 0.00 USD | 47,090.00 USD | `-20.59%` | `205,171,000,000.00` |
| `Live` | `Long` | `231.50` | 237,880.00 USD | 0.00 USD | 295.86 USD | `-19.90%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 237,590.00 USD | 0.00 USD | 429.66 USD | `-19.56%` | `1,848,000,000.00` |
| `Live` | `Long` | `234.50` | 237,160.00 USD | 0.00 USD | 217.85 USD | `-18.86%` | `929,000,000.00` |
| `Live` | `Long` | `235.50` | 236,940.00 USD | 0.00 USD | 1,480.00 USD | `-18.52%` | `6,274,000,000.00` |
| `Live` | `Long` | `239.50` | 235,460.00 USD | 0.00 USD | 1,030.00 USD | `-17.13%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 234,440.00 USD | 0.00 USD | 367.32 USD | `-16.44%` | `1,521,000,000.00` |
| `Live` | `Long` | `243.50` | 234,070.00 USD | 0.00 USD | 9,700.00 USD | `-15.75%` | `39,821,000,000.00` |
| `Live` | `Long` | `244.50` | 224,370.00 USD | 0.00 USD | 4,220.00 USD | `-15.40%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 220,150.00 USD | 0.00 USD | 1,030.00 USD | `-15.06%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 219,120.00 USD | 0.00 USD | 6,480.00 USD | `-14.37%` | `26,178,000,000.00` |
| `Live` | `Long` | `250.50` | 212,640.00 USD | 0.00 USD | 1,330.00 USD | `-13.33%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 211,320.00 USD | 0.00 USD | 268.35 USD | `-12.98%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 211,050.00 USD | 0.00 USD | 1,030.00 USD | `-12.64%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 210,020.00 USD | 0.00 USD | 362.92 USD | `-11.94%` | `1,426,000,000.00` |
| `Live` | `Long` | `255.50` | 209,660.00 USD | 0.00 USD | 3,660.00 USD | `-11.60%` | `14,337,000,000.00` |
| `Live` | `Long` | `256.50` | 205,990.00 USD | 0.00 USD | 2,480.00 USD | `-11.25%` | `9,686,000,000.00` |
| `Live` | `Long` | `257.50` | 203,510.00 USD | 0.00 USD | 14,580.00 USD | `-10.91%` | `56,622,000,000.00` |
| `Live` | `Long` | `258.50` | 188,930.00 USD | 0.00 USD | 176.56 USD | `-10.56%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 188,750.00 USD | 0.00 USD | 3,860.00 USD | `-9.87%` | `14,816,000,000.00` |
| `Live` | `Long` | `264.50` | 184,890.00 USD | 0.00 USD | 280.37 USD | `-8.48%` | `1,060,000,000.00` |
| `Live` | `Long` | `265.50` | 184,610.00 USD | 0.00 USD | 121,910.00 USD | `-8.14%` | `459,161,000,000.00` |
| `Live` | `Long` | `266.50` | 62,700.00 USD | 0.00 USD | 15,210.00 USD | `-7.79%` | `57,069,000,000.00` |
| `Live` | `Long` | `267.50` | 47,500.00 USD | 0.00 USD | 684.00 USD | `-7.45%` | `2,557,000,000.00` |
| `Live` | `Long` | `268.50` | 46,810.00 USD | 0.00 USD | 7,020.00 USD | `-7.10%` | `26,129,000,000.00` |
| `Live` | `Long` | `269.50` | 39,800.00 USD | 0.00 USD | 37,920.00 USD | `-6.75%` | `140,689,000,000.00` |
| `Live` | `Long` | `270.50` | 1,880.00 USD | 0.00 USD | 106.31 USD | `-6.41%` | `393,000,000.00` |
| `Live` | `Long` | `271.50` | 1,770.00 USD | 0.00 USD | 1,000.00 USD | `-6.06%` | `3,685,000,000.00` |
| `Live` | `Long` | `274.50` | 773.38 USD | 0.00 USD | 567.94 USD | `-5.02%` | `2,069,000,000.00` |
| `Live` | `Long` | `276.50` | 205.44 USD | 0.00 USD | 205.44 USD | `-4.33%` | `743,000,000.00` |
| `Live` | `Short` | `290.50` | 1,210.00 USD | 1,210.00 USD | 0.00 USD | `+0.51%` | `4,156,000,000.00` |
| `Live` | `Short` | `301.50` | 3,580.00 USD | 2,380.00 USD | 0.00 USD | `+4.32%` | `7,885,000,000.00` |
| `Live` | `Short` | `304.50` | 4,620.00 USD | 1,040.00 USD | 0.00 USD | `+5.36%` | `3,411,000,000.00` |
| `Live` | `Short` | `310.50` | 5,140.00 USD | 517.91 USD | 0.00 USD | `+7.43%` | `1,668,000,000.00` |
| `Live` | `Short` | `311.50` | 5,680.00 USD | 539.21 USD | 0.00 USD | `+7.78%` | `1,731,000,000.00` |
| `Live` | `Short` | `315.50` | 12,200.00 USD | 6,520.00 USD | 0.00 USD | `+9.16%` | `20,668,000,000.00` |
| `Live` | `Short` | `318.50` | 12,320.00 USD | 114.34 USD | 0.00 USD | `+10.20%` | `359,000,000.00` |
| `Live` | `Short` | `320.50` | 13,420.00 USD | 1,110.00 USD | 0.00 USD | `+10.89%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 13,700.00 USD | 276.63 USD | 0.00 USD | `+14.35%` | `837,000,000.00` |
| `Live` | `Short` | `340.50` | 15,060.00 USD | 1,360.00 USD | 0.00 USD | `+17.81%` | `4,000,000,000.00` |
| `Live` | `Short` | `356.50` | 54,280.00 USD | 39,220.00 USD | 0.00 USD | `+23.35%` | `110,000,000,000.00` |
| `Live` | `Short` | `358.50` | 55,280.00 USD | 1,010.00 USD | 0.00 USD | `+24.04%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 55,730.00 USD | 445.52 USD | 0.00 USD | `+27.50%` | `1,209,000,000.00` |
| `Live` | `Short` | `395.50` | 59,160.00 USD | 3,430.00 USD | 0.00 USD | `+36.84%` | `8,681,000,000.00` |
| `Live` | `Short` | `427.50` | 68,640.00 USD | 9,480.00 USD | 0.00 USD | `+47.91%` | `22,172,000,000.00` |
| `Live` | `Short` | `432.50` | 77,450.00 USD | 8,810.00 USD | 0.00 USD | `+49.64%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 123,700.00 USD | 46,250.00 USD | 0.00 USD | `+58.99%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 124,750.00 USD | 1,040.00 USD | 0.00 USD | `+72.48%` | `2,093,000,000.00` |
| `Live` | `Short` | `533.50` | 124,920.00 USD | 177.66 USD | 0.00 USD | `+84.59%` | `333,000,000.00` |
| `Live` | `Short` | `560.50` | 125,770.00 USD | 842.43 USD | 0.00 USD | `+93.93%` | `1,503,000,000.00` |
| `Live` | `Short` | `565.50` | 127,220.00 USD | 1,450.00 USD | 0.00 USD | `+95.66%` | `2,572,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 209,970.00 USD | 0.00 USD | 210.94 USD | `-50.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 209,760.00 USD | 0.00 USD | 2,070.00 USD | `-49.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 207,690.00 USD | 0.00 USD | 2,530.00 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 205,160.00 USD | 0.00 USD | 490.59 USD | `-36.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 204,670.00 USD | 0.00 USD | 482.01 USD | `-32.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 204,190.00 USD | 0.00 USD | 189.07 USD | `-30.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 204,000.00 USD | 0.00 USD | 441.60 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 203,560.00 USD | 0.00 USD | 703.49 USD | `-27.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 202,850.00 USD | 0.00 USD | 638.36 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 202,220.00 USD | 0.00 USD | 740.85 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 201,480.00 USD | 0.00 USD | 1,050.00 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 200,430.00 USD | 0.00 USD | 389.48 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 200,040.00 USD | 0.00 USD | 220.64 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 199,820.00 USD | 0.00 USD | 429.30 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 199,390.00 USD | 0.00 USD | 296.50 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 199,090.00 USD | 0.00 USD | 216.45 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 198,870.00 USD | 0.00 USD | 101.61 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 198,770.00 USD | 0.00 USD | 366.75 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 198,400.00 USD | 0.00 USD | 1,630.00 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 196,780.00 USD | 0.00 USD | 2,940.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 193,840.00 USD | 0.00 USD | 4,560.00 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 189,280.00 USD | 0.00 USD | 7,080.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 182,200.00 USD | 0.00 USD | 231.54 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 181,970.00 USD | 0.00 USD | 109.26 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 181,860.00 USD | 0.00 USD | 1,780.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 180,080.00 USD | 0.00 USD | 51,300.00 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 128,780.00 USD | 0.00 USD | 250.81 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `259.50` | 128,530.00 USD | 0.00 USD | 386.14 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 128,140.00 USD | 0.00 USD | 707.78 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 127,430.00 USD | 0.00 USD | 857.85 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 126,580.00 USD | 0.00 USD | 7,790.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 118,780.00 USD | 0.00 USD | 122.99 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 118,660.00 USD | 0.00 USD | 455.86 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 118,200.00 USD | 0.00 USD | 10,490.00 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 107,720.00 USD | 0.00 USD | 1,110.00 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 106,610.00 USD | 0.00 USD | 877.46 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 105,730.00 USD | 0.00 USD | 498.04 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 105,240.00 USD | 0.00 USD | 1,180.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 104,060.00 USD | 0.00 USD | 269.60 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 103,790.00 USD | 0.00 USD | 13,500.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 90,290.00 USD | 0.00 USD | 1,470.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 88,820.00 USD | 0.00 USD | 336.54 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 88,490.00 USD | 0.00 USD | 681.31 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 87,810.00 USD | 0.00 USD | 105.35 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 87,700.00 USD | 0.00 USD | 14,500.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 73,200.00 USD | 0.00 USD | 125.88 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 73,070.00 USD | 0.00 USD | 25,690.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 47,380.00 USD | 0.00 USD | 20,810.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 26,570.00 USD | 0.00 USD | 2,880.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 23,690.00 USD | 0.00 USD | 290.13 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 23,400.00 USD | 0.00 USD | 11,620.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 11,780.00 USD | 0.00 USD | 3,690.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 8,090.00 USD | 0.00 USD | 2,600.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,480.00 USD | 0.00 USD | 5,080.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `287.50` | 400.62 USD | 0.00 USD | 280.02 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `288.50` | 120.59 USD | 0.00 USD | 120.59 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 153.44 USD | 153.44 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,470.00 USD | 1,320.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 1,590.00 USD | 115.73 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 2,000.00 USD | 409.21 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 20,250.00 USD | 18,250.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 20,650.00 USD | 407.88 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 25,380.00 USD | 4,730.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 25,960.00 USD | 581.14 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 26,500.00 USD | 535.51 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 36,190.00 USD | 9,690.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 46,910.00 USD | 10,730.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 49,560.00 USD | 2,650.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 50,620.00 USD | 1,060.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 50,720.00 USD | 102.73 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 65,220.00 USD | 14,500.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 65,850.00 USD | 634.04 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `312.50` | 66,170.00 USD | 317.19 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 67,210.00 USD | 1,030.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 72,850.00 USD | 5,650.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 72,970.00 USD | 118.85 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 73,510.00 USD | 534.59 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 73,830.00 USD | 321.50 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 138,750.00 USD | 64,920.00 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 139,300.00 USD | 547.52 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 139,440.00 USD | 138.20 USD | 0.00 USD | `+19.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 139,700.00 USD | 257.45 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 139,870.00 USD | 174.25 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 140,020.00 USD | 151.50 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 141,480.00 USD | 1,450.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 143,250.00 USD | 1,770.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 143,580.00 USD | 326.07 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 144,400.00 USD | 826.60 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `364.50` | 148,130.00 USD | 3,730.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 155,580.00 USD | 7,440.00 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 156,260.00 USD | 682.84 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 157,360.00 USD | 1,100.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 158,040.00 USD | 683.96 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 158,240.00 USD | 199.75 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 161,740.00 USD | 3,500.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 162,780.00 USD | 1,040.00 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 163,160.00 USD | 376.71 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 351,800.00 USD | 188,640.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 357,700.00 USD | 5,900.00 USD | 0.00 USD | `+43.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 358,600.00 USD | 901.21 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 366,400.00 USD | 7,800.00 USD | 0.00 USD | `+47.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 367,960.00 USD | 1,550.00 USD | 0.00 USD | `+48.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 369,340.00 USD | 1,380.00 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 369,960.00 USD | 621.14 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 373,340.00 USD | 3,380.00 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 373,560.00 USD | 222.75 USD | 0.00 USD | `+54.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 379,160.00 USD | 5,590.00 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 385,070.00 USD | 5,920.00 USD | 0.00 USD | `+56.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 386,200.00 USD | 1,130.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 393,840.00 USD | 7,630.00 USD | 0.00 USD | `+66.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 492,310.00 USD | 98,470.00 USD | 0.00 USD | `+68.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 493,290.00 USD | 981.00 USD | 0.00 USD | `+69.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 493,790.00 USD | 499.50 USD | 0.00 USD | `+72.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,380,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+73.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,380,000.00 USD | 1,000.00 USD | 0.00 USD | `+73.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,380,000.00 USD | 1,040.00 USD | 0.00 USD | `+79.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,380,000.00 USD | 340.67 USD | 0.00 USD | `+80.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,380,000.00 USD | 638.86 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `575.50` | 2,390,000.00 USD | 2,590.00 USD | 0.00 USD | `+99.12%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `248.50` | 18,650,000.00 USD | 0.00 USD | 18,650,000.00 USD | 37,900.00 USD | 13,170.00 USD | 32,010.00 USD |
| `7D` | `248.90` | 18,570,000.00 USD | 0.00 USD | 18,570,000.00 USD | 18,160.00 USD | 22,560.00 USD | 11,560.00 USD |
| `7D` | `249.30` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 16,540.00 USD | 28,020.00 USD | 2,020.00 USD |
| `7D` | `249.70` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD |
| `7D` | `250.10` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,050.00 USD |
| `7D` | `250.50` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD |
| `7D` | `250.90` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,850.00 USD |
| `7D` | `251.30` | 18,160,000.00 USD | 0.00 USD | 18,160,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,650.00 USD |
| `7D` | `251.70` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD |
| `7D` | `252.10` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,670.00 USD |
| `7D` | `252.50` | 17,760,000.00 USD | 0.00 USD | 17,760,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,710.00 USD |
| `7D` | `252.90` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 13,480.00 USD | 19,580.00 USD | 14.44 USD |
| `7D` | `253.30` | 17,630,000.00 USD | 0.00 USD | 17,630,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,810.00 USD |
| `7D` | `253.70` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,070.00 USD |
| `7D` | `254.10` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,940.00 USD |
| `7D` | `254.50` | 17,390,000.00 USD | 0.00 USD | 17,390,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,380.00 USD |
| `7D` | `254.90` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,630.00 USD |
| `7D` | `255.30` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,040.00 USD |
| `7D` | `255.70` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,680.00 USD |
| `7D` | `256.10` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,210.00 USD |
| `7D` | `256.50` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,750.00 USD |
| `7D` | `256.90` | 16,940,000.00 USD | 0.00 USD | 16,940,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,470.00 USD |
| `7D` | `257.30` | 16,840,000.00 USD | 0.00 USD | 16,840,000.00 USD | 23,000.00 USD | 1,850.00 USD | 27,280.00 USD |
| `1D` | `257.70` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 0.00 USD | 5,670.00 USD | 4,870.00 USD |
| `7D` | `257.70` | 16,790,000.00 USD | 0.00 USD | 16,790,000.00 USD | 47,180.00 USD | 6,040.00 USD | 18,210.00 USD |
| `1D` | `258.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 32.50 USD | 4,120.00 USD | 19,390.00 USD |
| `7D` | `258.10` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,750.00 USD |
| `1D` | `258.50` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 1,470.00 USD | 5,260.00 USD | 45.78 USD |
| `7D` | `258.50` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,940.00 USD |
| `1D` | `258.90` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 17,930.00 USD | 11,000.00 USD | 11,810.00 USD |
| `7D` | `258.90` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,380.00 USD |
| `1D` | `259.30` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 13,160.00 USD | 4,150.00 USD | 12,490.00 USD |
| `7D` | `259.30` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,050.00 USD |
| `1D` | `259.70` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 14,700.00 USD | 16,830.00 USD | 15,100.00 USD |
| `7D` | `259.70` | 16,320,000.00 USD | 0.00 USD | 16,320,000.00 USD | 17,070.00 USD | 13,660.00 USD | 250.38 USD |
| `1D` | `260.10` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 5,100.00 USD | 9,630.00 USD | 16,750.00 USD |
| `7D` | `260.10` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,820.00 USD |
| `1D` | `260.50` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 2,850.00 USD | 8,760.00 USD | 10,400.00 USD |
| `7D` | `260.50` | 16,250,000.00 USD | 0.00 USD | 16,250,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,340.00 USD |
| `1D` | `260.90` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD |
| `7D` | `260.90` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,890.00 USD |
| `1D` | `261.30` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 8,660.00 USD | 16,360.00 USD | 500.69 USD |
| `7D` | `261.30` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 2,490.00 USD | 33,470.00 USD | 16,070.00 USD |
| `1D` | `261.70` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD |
| `7D` | `261.70` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,940.00 USD |
| `1D` | `262.10` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 517.32 USD | 4,790.00 USD | 16,510.00 USD |
| `7D` | `262.10` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 60,340.00 USD | 35,350.00 USD | 32,810.00 USD |
| `1D` | `262.50` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD |
| `7D` | `262.50` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 36,590.00 USD | 26,590.00 USD | 50.84 USD |
| `1D` | `262.90` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD |
| `7D` | `262.90` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,700.00 USD |
| `1D` | `263.30` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD |
| `7D` | `263.30` | 15,630,000.00 USD | 0.00 USD | 15,630,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,090.00 USD |
| `1D` | `263.70` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD |
| `7D` | `263.70` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 265,940.00 USD | 96,750.00 USD | 26,980.00 USD |
| `1D` | `264.10` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD |
| `7D` | `264.10` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,880.00 USD |
| `1D` | `264.50` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD |
| `7D` | `264.50` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 49,620.00 USD | 16,400.00 USD | 37,350.00 USD |
| `1D` | `264.90` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,670.00 USD |
| `7D` | `264.90` | 14,870,000.00 USD | 0.00 USD | 14,870,000.00 USD | 22,920.00 USD | 75,260.00 USD | 16,040.00 USD |
| `1D` | `265.30` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 20,730.00 USD | 8,710.00 USD | 33,520.00 USD |
| `7D` | `265.30` | 14,760,000.00 USD | 0.00 USD | 14,760,000.00 USD | 133,130.00 USD | 59,960.00 USD | 111,080.00 USD |
| `1D` | `265.70` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 23,810.00 USD | 23,390.00 USD | 33,670.00 USD |
| `7D` | `265.70` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 54,220.00 USD | 81,830.00 USD | 61,300.00 USD |
| `1D` | `266.10` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 10,200.00 USD | 335.05 USD | 7.04 USD |
| `7D` | `266.10` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,640.00 USD |
| `1D` | `266.50` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 27,700.00 USD | 3,150.00 USD | 8,720.00 USD |
| `7D` | `266.50` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,120.00 USD |
| `1D` | `266.90` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 32,310.00 USD | 6,620.00 USD | 6,770.00 USD |
| `7D` | `266.90` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,300.00 USD |
| `1D` | `267.30` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 17,990.00 USD | 11,070.00 USD | 3,350.00 USD |
| `7D` | `267.30` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,780.00 USD |
| `1D` | `267.70` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 83,350.00 USD | 112,140.00 USD | 14,410.00 USD |
| `7D` | `267.70` | 12,860,000.00 USD | 0.00 USD | 12,860,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,540.00 USD |
| `1D` | `268.10` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 55,490.00 USD | 80,400.00 USD | 47,150.00 USD |
| `7D` | `268.10` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,490.00 USD |
| `1D` | `268.50` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 57,190.00 USD | 101,540.00 USD | 31,670.00 USD |
| `7D` | `268.50` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,220.00 USD |
| `1D` | `268.90` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 92,000.00 USD | 36,230.00 USD | 41,690.00 USD |
| `7D` | `268.90` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,390.00 USD |
| `1D` | `269.30` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 28,630.00 USD | 16,320.00 USD | 20,850.00 USD |
| `7D` | `269.30` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,030.00 USD |
| `1D` | `269.70` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 39,120.00 USD | 24,350.00 USD | 8,680.00 USD |
| `7D` | `269.70` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,350.00 USD |
| `1D` | `270.10` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 98,640.00 USD | 77,570.00 USD | 98,230.00 USD |
| `7D` | `270.10` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,490.00 USD |
| `1D` | `270.50` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 71,720.00 USD | 36,250.00 USD | 36,810.00 USD |
| `7D` | `270.50` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,730.00 USD |
| `1D` | `270.90` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 11,770.00 USD | 24,230.00 USD | 66,890.00 USD |
| `7D` | `270.90` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 318,780.00 USD | 144,560.00 USD | 90,090.00 USD |
| `1D` | `271.30` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 56,610.00 USD | 46,210.00 USD | 72,980.00 USD |
| `7D` | `271.30` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD |
| `1D` | `271.70` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 20,310.00 USD | 13,930.00 USD | 6,920.00 USD |
| `7D` | `271.70` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,250.00 USD |
| `1D` | `272.10` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 109,050.00 USD | 32,950.00 USD | 17,450.00 USD |
| `7D` | `272.10` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,620.00 USD |
| `1D` | `272.50` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 81,660.00 USD | 31,310.00 USD | 46,830.00 USD |
| `7D` | `272.50` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,080.00 USD |
| `1D` | `272.90` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 80,060.00 USD | 58,140.00 USD | 6,760.00 USD |
| `7D` | `272.90` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,390.00 USD |
| `1D` | `273.30` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 179,830.00 USD | 208,970.00 USD | 35,220.00 USD |
| `7D` | `273.30` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,430.00 USD |
| `1D` | `273.70` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 142,100.00 USD | 172,310.00 USD | 117,060.00 USD |
| `7D` | `273.70` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 195,450.00 USD | 467,590.00 USD | 206,000.00 USD |
| `1D` | `274.10` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 120,870.00 USD | 232,210.00 USD | 71,890.00 USD |
| `7D` | `274.10` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,410.00 USD |
| `1D` | `274.50` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 195,280.00 USD | 71,370.00 USD | 111,420.00 USD |
| `7D` | `274.50` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,420.00 USD |
| `1D` | `274.90` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 57,970.00 USD | 37,710.00 USD | 53,710.00 USD |
| `7D` | `274.90` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,760.00 USD |
| `1D` | `275.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD |
| `7D` | `275.30` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,420.00 USD |
| `1D` | `275.70` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 12,170.00 USD | 37,310.00 USD | 8,730.00 USD |
| `7D` | `275.70` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 1,350.00 USD | 51,050.00 USD | 51.95 USD |
| `1D` | `276.10` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 82,210.00 USD | 48,180.00 USD | 22,040.00 USD |
| `7D` | `276.10` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 27,970.00 USD | 31,830.00 USD | 3,230.00 USD |
| `7D` | `276.50` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 10,750.00 USD | 20,770.00 USD | 11,360.00 USD |
| `7D` | `276.90` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,950.00 USD |
| `1D` | `277.30` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 28,530.00 USD | 66,900.00 USD | 50,910.00 USD |
| `7D` | `277.30` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 0.00 USD | 63,290.00 USD | 36.46 USD |
| `1D` | `277.70` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 57,640.00 USD | 47,660.00 USD | 23,950.00 USD |
| `7D` | `277.70` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 0.00 USD | 27,190.00 USD | 84,360.00 USD |
| `1D` | `278.10` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD |
| `7D` | `278.10` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 24,750.00 USD | 0.00 USD | 59,520.00 USD |
| `1D` | `278.50` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 67,950.00 USD | 33,500.00 USD | 29,220.00 USD |
| `7D` | `278.50` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD |
| `1D` | `278.90` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 24,100.00 USD | 27,270.00 USD | 10,340.00 USD |
| `7D` | `278.90` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,120.00 USD |
| `1D` | `279.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 53,390.00 USD | 33,630.00 USD | 44,020.00 USD |
| `7D` | `279.30` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 31,330.00 USD | 0.00 USD | 41,670.00 USD |
| `1D` | `279.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 20,320.00 USD | 0.00 USD | 13,960.00 USD |
| `7D` | `279.70` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 46,800.00 USD | 0.00 USD | 54,390.00 USD |
| `1D` | `280.10` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD |
| `1D` | `280.50` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD |
| `7D` | `280.50` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 36.62 USD |
| `1D` | `280.90` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 21,660.00 USD |
| `7D` | `280.90` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 69.30 USD |
| `1D` | `281.30` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.30` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.70` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 9,360.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `281.70` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 565.82 USD | 0.00 USD | 122,430.00 USD |
| `1D` | `282.10` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 55,330.00 USD | 39,110.00 USD | 187,730.00 USD |
| `7D` | `282.10` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD |
| `1D` | `282.50` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 13,450.00 USD | 3,640.00 USD |
| `7D` | `282.50` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 32,190.00 USD | 0.00 USD | 39,760.00 USD |
| `1D` | `282.90` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 38,030.00 USD | 54,510.00 USD | 80,600.00 USD |
| `7D` | `282.90` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 97.92 USD |
| `1D` | `283.30` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 18,430.00 USD | 0.00 USD | 112,590.00 USD |
| `7D` | `283.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 0.00 USD | 37,310.00 USD | 89,310.00 USD |
| `1D` | `283.70` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 30,480.00 USD | 51,990.00 USD |
| `7D` | `283.70` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 238,930.00 USD |
| `1D` | `284.10` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD |
| `7D` | `284.10` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 49,500.00 USD | 0.00 USD | 135,980.00 USD |
| `1D` | `284.50` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 39,670.00 USD | 70,600.00 USD | 20,690.00 USD |
| `7D` | `284.50` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,170.00 USD |
| `1D` | `284.90` | 994,860.00 USD | 0.00 USD | 994,860.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD |
| `7D` | `284.90` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD |
| `1D` | `285.30` | 965,760.00 USD | 0.00 USD | 965,760.00 USD | 20,960.00 USD | 64,640.00 USD | 93,680.00 USD |
| `7D` | `285.30` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD |
| `1D` | `285.70` | 786,470.00 USD | 0.00 USD | 786,470.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD |
| `7D` | `285.70` | 771,160.00 USD | 0.00 USD | 771,160.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD |
| `1D` | `286.10` | 623,850.00 USD | 0.00 USD | 623,850.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `7D` | `286.10` | 657,530.00 USD | 0.00 USD | 657,530.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD |
| `1D` | `286.50` | 593,850.00 USD | 0.00 USD | 593,850.00 USD | 111,830.00 USD | 47,210.00 USD | 37,510.00 USD |
| `7D` | `286.50` | 582,680.00 USD | 0.00 USD | 582,680.00 USD | 23,860.00 USD | 95,580.00 USD | 31.50 USD |
| `1D` | `286.90` | 397,290.00 USD | 0.00 USD | 397,290.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD |
| `7D` | `286.90` | 463,210.00 USD | 0.00 USD | 463,210.00 USD | 27,530.00 USD | 141,160.00 USD | 2.46 USD |
| `1D` | `287.30` | 101,950.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD |
| `7D` | `287.30` | 294,520.00 USD | 0.00 USD | 294,520.00 USD | 53,620.00 USD | 86,570.00 USD | 0.99 USD |
| `1D` | `287.70` | 33,650.00 USD | 33,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `287.70` | 67,300.00 USD | 67,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `7D` | `287.70` | 154,340.00 USD | 0.00 USD | 154,340.00 USD | 0.00 USD | 154,260.00 USD | 77.98 USD |
| `7D` | `287.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `288.10` | 78,660.00 USD | 78,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD |
| `7D` | `288.10` | 139,310.00 USD | 139,310.00 USD | 0.00 USD | 0.00 USD | 139,290.00 USD | 15.00 USD |
| `7D` | `288.90` | 139,310.00 USD | 139,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6.30 USD |
| `1D` | `289.30` | 90,660.00 USD | 90,660.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.30` | 139,340.00 USD | 139,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22.44 USD |
| `7D` | `289.70` | 141,210.00 USD | 141,210.00 USD | 0.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD |
| `7D` | `290.10` | 141,240.00 USD | 141,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.96 USD |
| `7D` | `290.50` | 141,260.00 USD | 141,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16.74 USD |
| `1D` | `290.90` | 90,660.00 USD | 90,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.40 USD |
| `1D` | `291.30` | 128,960.00 USD | 128,960.00 USD | 0.00 USD | 0.00 USD | 38,290.00 USD | 7.76 USD |
| `7D` | `291.30` | 150,520.00 USD | 150,520.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD | 11.00 USD |
| `1D` | `291.70` | 166,730.00 USD | 166,730.00 USD | 0.00 USD | 0.00 USD | 15,650.00 USD | 22,120.00 USD |
| `7D` | `291.70` | 244,620.00 USD | 244,620.00 USD | 0.00 USD | 0.00 USD | 94,090.00 USD | 14.24 USD |
| `1D` | `292.10` | 205,100.00 USD | 205,100.00 USD | 0.00 USD | 0.00 USD | 38,360.00 USD | 9.06 USD |
| `7D` | `292.10` | 363,320.00 USD | 363,320.00 USD | 0.00 USD | 0.00 USD | 118,660.00 USD | 38.04 USD |
| `1D` | `292.50` | 252,470.00 USD | 252,470.00 USD | 0.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD |
| `7D` | `292.50` | 390,020.00 USD | 390,020.00 USD | 0.00 USD | 0.00 USD | 26,610.00 USD | 96.06 USD |
| `1D` | `292.90` | 334,730.00 USD | 334,730.00 USD | 0.00 USD | 1,020.00 USD | 81,240.00 USD | 3.04 USD |
| `7D` | `292.90` | 508,540.00 USD | 508,540.00 USD | 0.00 USD | 0.00 USD | 118,480.00 USD | 41.87 USD |
| `1D` | `293.30` | 395,800.00 USD | 395,800.00 USD | 0.00 USD | 476.80 USD | 60,590.00 USD | 1.58 USD |
| `7D` | `293.30` | 621,650.00 USD | 621,650.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 21.06 USD |
| `1D` | `293.70` | 607,490.00 USD | 607,490.00 USD | 0.00 USD | 73,230.00 USD | 77,060.00 USD | 61,390.00 USD |
| `7D` | `293.70` | 660,160.00 USD | 660,160.00 USD | 0.00 USD | 37,280.00 USD | 1,170.00 USD | 64.24 USD |
| `1D` | `294.10` | 692,810.00 USD | 692,810.00 USD | 0.00 USD | 30,790.00 USD | 36,360.00 USD | 18,180.00 USD |
| `7D` | `294.10` | 884,710.00 USD | 884,710.00 USD | 0.00 USD | 85,150.00 USD | 33,590.00 USD | 105,810.00 USD |
| `1D` | `294.50` | 983,470.00 USD | 983,470.00 USD | 0.00 USD | 114,260.00 USD | 98,900.00 USD | 77,500.00 USD |
| `7D` | `294.50` | 969,700.00 USD | 969,700.00 USD | 0.00 USD | 69,950.00 USD | 15,030.00 USD | 8.50 USD |
| `1D` | `294.90` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 53,910.00 USD | 79,400.00 USD | 105,170.00 USD |
| `7D` | `294.90` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 63,470.00 USD | 92,770.00 USD | 104,880.00 USD |
| `1D` | `295.30` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 95,260.00 USD | 75,850.00 USD | 85,290.00 USD |
| `7D` | `295.30` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 45,590.00 USD | 65,580.00 USD | 252,160.00 USD |
| `1D` | `295.70` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD |
| `7D` | `295.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 105,410.00 USD | 72,570.00 USD | 133,220.00 USD |
| `1D` | `296.10` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 90,530.00 USD | 119,980.00 USD | 29,580.00 USD |
| `7D` | `296.10` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 75,740.00 USD | 90,470.00 USD | 119,120.00 USD |
| `1D` | `296.50` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 43,030.00 USD | 34,820.00 USD | 43,490.00 USD |
| `7D` | `296.50` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 1,060.00 USD | 77,140.00 USD | 57,060.00 USD |
| `1D` | `296.90` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 29,430.00 USD | 50,150.00 USD | 91,120.00 USD |
| `7D` | `296.90` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 206,840.00 USD | 51,220.00 USD | 134,610.00 USD |
| `1D` | `297.30` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 57,730.00 USD | 359.06 USD | 28,050.00 USD |
| `7D` | `297.30` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 3,960.00 USD | 2,500.00 USD | 68.02 USD |
| `1D` | `297.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 807.94 USD | 723.06 USD | 12,060.00 USD |
| `7D` | `297.70` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 144.38 USD | 56,790.00 USD | 34,680.00 USD |
| `1D` | `298.10` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 44,470.00 USD | 8,120.00 USD | 53,000.00 USD |
| `7D` | `298.10` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 49,240.00 USD | 80,820.00 USD | 54,890.00 USD |
| `1D` | `298.50` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 8,410.00 USD | 21,250.00 USD | 84,830.00 USD |
| `7D` | `298.50` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 12,660.00 USD | 47,950.00 USD |
| `1D` | `298.90` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 34,670.00 USD | 15,820.00 USD | 118,690.00 USD |
| `7D` | `298.90` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 70,090.00 USD | 993.25 USD | 40,010.00 USD |
| `1D` | `299.30` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 59,910.00 USD | 23,800.00 USD | 27,850.00 USD |
| `7D` | `299.30` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 2,570.00 USD | 1,380.00 USD | 45,960.00 USD |
| `1D` | `299.70` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 4,910.00 USD | 17,410.00 USD | 9,090.00 USD |
| `7D` | `299.70` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 5,310.00 USD | 7,720.00 USD | 19,910.00 USD |
| `1D` | `300.10` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 51,990.00 USD | 44,530.00 USD | 35,300.00 USD |
| `7D` | `300.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 51,500.00 USD | 2,470.00 USD | 41.48 USD |
| `1D` | `300.50` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 11,190.00 USD | 10,850.00 USD | 41,890.00 USD |
| `7D` | `300.50` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 866.20 USD | 36,230.00 USD | 19,830.00 USD |
| `1D` | `300.90` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 12,920.00 USD | 32,390.00 USD | 36,710.00 USD |
| `7D` | `300.90` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 24,730.00 USD | 34,630.00 USD | 84,340.00 USD |
| `1D` | `301.30` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD |
| `7D` | `301.30` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 71,140.00 USD | 55,420.00 USD | 94,560.00 USD |
| `1D` | `301.70` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 31,990.00 USD | 20,360.00 USD | 16,730.00 USD |
| `7D` | `301.70` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 37,640.00 USD | 130,520.00 USD | 14.22 USD |
| `1D` | `302.10` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 44,680.00 USD | 37,100.00 USD | 10,340.00 USD |
| `7D` | `302.10` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 53,220.00 USD | 123,390.00 USD | 26,310.00 USD |
| `1D` | `302.50` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 10,520.00 USD | 20,540.00 USD | 31,130.00 USD |
| `7D` | `302.50` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 31,330.00 USD | 102,200.00 USD | 41,750.00 USD |
| `1D` | `302.90` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 1,230.00 USD | 1,850.00 USD | 20,520.00 USD |
| `7D` | `302.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 40,380.00 USD | 64,640.00 USD | 150.66 USD |
| `1D` | `303.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 32,880.00 USD | 413.69 USD | 14,710.00 USD |
| `7D` | `303.30` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 6.76 USD |
| `1D` | `303.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD |
| `7D` | `303.70` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 17,370.00 USD | 8,710.00 USD | 24,600.00 USD |
| `1D` | `304.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 22,560.00 USD | 1,100.00 USD | 53,800.00 USD |
| `7D` | `304.10` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 5,440.00 USD | 1,950.00 USD | 154.23 USD |
| `1D` | `304.50` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 13,310.00 USD | 9,720.00 USD | 53,870.00 USD |
| `7D` | `304.50` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 3,480.00 USD | 11,110.00 USD | 92.29 USD |
| `1D` | `304.90` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 697.80 USD | 240.63 USD | 2.91 USD |
| `7D` | `304.90` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 34,680.00 USD | 18,990.00 USD | 8,350.00 USD |
| `1D` | `305.30` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 11,210.00 USD | 90.03 USD | 2,010.00 USD |
| `7D` | `305.30` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 162,420.00 USD | 128,450.00 USD | 117,090.00 USD |
| `1D` | `305.70` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 7,960.00 USD | 1,770.00 USD | 3,410.00 USD |
| `7D` | `305.70` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 82,270.00 USD | 18,170.00 USD | 17,450.00 USD |
| `1D` | `306.10` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 4,210.00 USD | 2,750.00 USD | 1,350.00 USD |
| `7D` | `306.10` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 22,930.00 USD | 68,220.00 USD | 45,940.00 USD |
| `1D` | `306.50` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 4,740.00 USD | 9,750.00 USD | 58.13 USD |
| `7D` | `306.50` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 30,150.00 USD | 41,830.00 USD | 65,770.00 USD |
| `1D` | `306.90` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 32,060.00 USD | 40,210.00 USD | 13,060.00 USD |
| `7D` | `306.90` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 58,810.00 USD | 50,570.00 USD | 57,740.00 USD |
| `1D` | `307.30` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 7,930.00 USD | 34,540.00 USD | 10,930.00 USD |
| `7D` | `307.30` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 34,320.00 USD | 123,720.00 USD | 83,230.00 USD |
| `1D` | `307.70` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 19,670.00 USD | 27,980.00 USD | 9,610.00 USD |
| `7D` | `307.70` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 84,930.00 USD | 74,370.00 USD | 24,120.00 USD |
| `1D` | `308.10` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD |
| `7D` | `308.10` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 106,040.00 USD | 63,640.00 USD | 106,970.00 USD |
| `1D` | `308.50` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 5,570.00 USD | 3,510.00 USD | 4,260.00 USD |
| `7D` | `308.50` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 118,090.00 USD | 64,440.00 USD | 65,440.00 USD |
| `1D` | `308.90` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 12,710.00 USD | 6,030.00 USD | 4,140.00 USD |
| `7D` | `308.90` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 60,660.00 USD | 31,940.00 USD | 19,740.00 USD |
| `1D` | `309.30` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD |
| `7D` | `309.30` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 27,920.00 USD | 26,240.00 USD | 36,610.00 USD |
| `1D` | `309.70` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD |
| `7D` | `309.70` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 40,410.00 USD | 132,660.00 USD | 153,330.00 USD |
| `1D` | `310.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 4,390.00 USD | 4,770.00 USD | 0.00 USD |
| `7D` | `310.10` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 34,250.00 USD | 63,360.00 USD | 62,780.00 USD |
| `1D` | `310.50` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD |
| `7D` | `310.50` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 68,560.00 USD | 73,280.00 USD | 22,010.00 USD |
| `1D` | `310.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.31 USD |
| `7D` | `310.90` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 35,670.00 USD | 30,720.00 USD | 3,860.00 USD |
| `1D` | `311.30` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `311.30` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 84,180.00 USD | 65,480.00 USD | 47,640.00 USD |
| `1D` | `311.70` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 9,900.00 USD | 6,590.00 USD | 4.48 USD |
| `7D` | `311.70` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 34,040.00 USD | 11,430.00 USD | 31,800.00 USD |
| `1D` | `312.10` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 244.00 USD | 39.75 USD | 29.51 USD |
| `7D` | `312.10` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 46,850.00 USD | 1,100.00 USD | 24,240.00 USD |
| `1D` | `312.50` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 8,760.00 USD | 7,440.00 USD | 8,700.00 USD |
| `7D` | `312.50` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 19,540.00 USD | 22,180.00 USD | 49,680.00 USD |
| `1D` | `312.90` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 11,420.00 USD | 23.27 USD | 1.44 USD |
| `7D` | `312.90` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 30,000.00 USD |
| `1D` | `313.30` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 64,910.00 USD | 30,120.00 USD | 22,690.00 USD |
| `1D` | `313.70` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 8,340.00 USD | 86.80 USD | 6,390.00 USD |
| `7D` | `313.70` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 32,170.00 USD | 15,010.00 USD | 23,160.00 USD |
| `1D` | `314.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD | 3,420.00 USD |
| `7D` | `314.10` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 26,810.00 USD | 362.37 USD | 47,870.00 USD |
| `1D` | `314.50` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `314.50` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 48,630.00 USD | 307.60 USD | 24,530.00 USD |
| `1D` | `314.90` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `314.90` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 29,590.00 USD | 0.00 USD | 10,270.00 USD |
| `1D` | `315.30` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 32.50 USD | 144.50 USD | 6,170.00 USD |
| `7D` | `315.30` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 5,690.00 USD | 547.95 USD | 51.95 USD |
| `1D` | `315.70` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `315.70` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 9,200.00 USD | 50,270.00 USD | 48,060.00 USD |
| `1D` | `316.10` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,020.00 USD | 5,050.00 USD | 11,840.00 USD |
| `7D` | `316.10` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,440.00 USD |
| `1D` | `316.50` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 12,950.00 USD | 5,380.00 USD | 0.00 USD |
| `7D` | `316.50` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 16,120.00 USD | 20,630.00 USD | 18,390.00 USD |
| `1D` | `316.90` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 12,760.00 USD | 3,660.00 USD | 12,480.00 USD |
| `7D` | `316.90` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 41.88 USD |
| `1D` | `317.30` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 2,250.00 USD | 4,170.00 USD | 1,590.00 USD |
| `7D` | `317.30` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 14,540.00 USD | 748.91 USD | 196.09 USD |
| `1D` | `317.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 15,260.00 USD | 15,360.00 USD | 23,390.00 USD |
| `7D` | `317.70` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 620.15 USD | 265.17 USD | 37.00 USD |
| `1D` | `318.10` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 2,290.00 USD | 9,270.00 USD | 7,680.00 USD |
| `7D` | `318.10` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 22,250.00 USD | 9,100.00 USD | 148.70 USD |
| `1D` | `318.50` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 4,700.00 USD | 7,500.00 USD | 9,580.00 USD |
| `7D` | `318.50` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD |
| `1D` | `318.90` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD |
| `7D` | `318.90` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 10,270.00 USD | 17,970.00 USD | 23,860.00 USD |
| `1D` | `319.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 8,590.00 USD | 16,300.00 USD | 488.47 USD |
| `7D` | `319.30` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 18,060.00 USD | 49.12 USD |
| `1D` | `319.70` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `7D` | `319.70` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 2.45 USD |
| `1D` | `320.10` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 4,350.00 USD | 4,210.00 USD | 10,920.00 USD |
| `7D` | `320.10` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD |
| `1D` | `320.50` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `320.50` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 15,190.00 USD | 10,080.00 USD | 0.00 USD |
| `7D` | `320.90` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.30` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD |
| `7D` | `321.70` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD |
| `7D` | `322.10` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 22,940.00 USD | 8,290.00 USD | 6,150.00 USD |
| `7D` | `322.50` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 555.20 USD | 365.55 USD | 0.48 USD |
| `7D` | `322.90` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 16,590.00 USD | 5,630.00 USD | 0.00 USD |
| `7D` | `323.30` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 14,160.00 USD | 5,860.00 USD | 11,530.00 USD |
| `7D` | `323.70` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.10` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD |
| `7D` | `324.40` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `315.37M` | Total OI Tokens: `1,095,570.3 BCH`
  * 1h OI Change: `-1.27%` | 4h OI Change: `+2.42%` | 24h OI Change: `-1.39%`
  * Exchange Breakdown: Binance=`93.93M` | Bybit=`40.27M` | OKX=`24.73M` | Hyperliquid=`8.14M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.50K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0010%` | **USDT OKX** | `-0.0049%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0048%` |
| **USDT MEXC** | `0.0009%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0008%` | **USDT Bitget** | `0.0058%` |
| **CoinM Binance** | `-0.0011%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `40.26%` | `59.74%` | `0.67` | 20,910,000.00 USD |
| `15M` | `Binance` | `47.48%` | `52.52%` | `0.90` | 7,780,000.00 USD |
| `15M` | `OKX` | `47.91%` | `52.09%` | `0.92` | 1,740,000.00 USD |
| `15M` | `Bybit` | `39%` | `61%` | `0.64` | 2,820,000.00 USD |
| `15M` | `KuCoin` | `34.65%` | `65.35%` | `0.53` | 168,620.00 USD |
| `15M` | `Gate` | `33.04%` | `66.96%` | `0.49` | 424,270.00 USD |
| `15M` | `Bitget` | `34.56%` | `65.44%` | `0.53` | 544,660.00 USD |
| `15M` | `BingX` | `23.72%` | `76.28%` | `0.31` | 2,080,000.00 USD |
| `15M` | `MEXC` | `52.13%` | `47.87%` | `1.09` | 717,540.00 USD |
| `15M` | `Bitunix` | `31.81%` | `68.19%` | `0.47` | 910,030.00 USD |
| `15M` | `Hyperliquid` | `32.97%` | `67.03%` | `0.49` | 1,460,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `34.2%` | `65.8%` | `0.52` | 160,860.00 USD |
| `15M` | `Crypto.com` | `59.19%` | `40.81%` | `1.45` | 119.71 USD |
| `15M` | `WhiteBIT` | `78.2%` | `21.8%` | `3.59` | 668,080.00 USD |
| `15M` | `HTX` | `70.2%` | `29.8%` | `2.36` | 51,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `5.21%` | `94.79%` | `0.05` | 1,240,000.00 USD |
| `15M` | `Aster` | `81.43%` | `18.57%` | `4.39` | 11,400.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.6%` | `41.4%` | `1.42` | 138,430.00 USD |
| `15M` | `Whale Positions` | `47.48%` | `52.52%` | `0.90` | 7,780,000.00 USD |
| `15M` | `Global Accounts` | `40.26%` | `59.74%` | `0.67` | 20,910,000.00 USD |
| `1H` | `BCH` | `52.14%` | `47.86%` | `1.09` | 13,960,000.00 USD |
| `1H` | `Binance` | `45.41%` | `54.59%` | `0.83` | 4,130,000.00 USD |
| `1H` | `OKX` | `50.45%` | `49.55%` | `1.02` | 1,320,000.00 USD |
| `1H` | `Bybit` | `44.92%` | `55.08%` | `0.82` | 1,250,000.00 USD |
| `1H` | `KuCoin` | `60.94%` | `39.06%` | `1.56` | 99,610.00 USD |
| `1H` | `Gate` | `53.15%` | `46.85%` | `1.13` | 1,860,000.00 USD |
| `1H` | `Bitget` | `47.19%` | `52.81%` | `0.89` | 284,460.00 USD |
| `1H` | `BingX` | `47.31%` | `52.69%` | `0.90` | 2,220,000.00 USD |
| `1H` | `MEXC` | `44.17%` | `55.83%` | `0.79` | 673,910.00 USD |
| `1H` | `Bitunix` | `51.67%` | `48.33%` | `1.07` | 185,710.00 USD |
| `1H` | `Hyperliquid` | `31.21%` | `68.79%` | `0.45` | 139,290.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.77%` | `51.23%` | `0.95` | 374,880.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.92%` | `1.08%` | `91.59` | 1,300,000.00 USD |
| `1H` | `HTX` | `32.77%` | `67.23%` | `0.49` | 52,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `31.49%` | `68.51%` | `0.46` | 26,650.00 USD |
| `1H` | `Aster` | `42.48%` | `57.52%` | `0.74` | 10,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0.39%` | `99.61%` | `0.00` | 28,880.00 USD |
| `1H` | `Whale Positions` | `45.41%` | `54.59%` | `0.83` | 4,130,000.00 USD |
| `1H` | `Global Accounts` | `52.14%` | `47.86%` | `1.09` | 13,960,000.00 USD |
| `4H` | `BCH` | `52.66%` | `47.34%` | `1.11` | 62,420,000.00 USD |
| `4H` | `Binance` | `47.68%` | `52.32%` | `0.91` | 19,340,000.00 USD |
| `4H` | `OKX` | `48.73%` | `51.27%` | `0.95` | 7,200,000.00 USD |
| `4H` | `Bybit` | `51.84%` | `48.16%` | `1.08` | 5,400,000.00 USD |
| `4H` | `KuCoin` | `46.21%` | `53.79%` | `0.86` | 526,040.00 USD |
| `4H` | `Gate` | `49.7%` | `50.3%` | `0.99` | 8,310,000.00 USD |
| `4H` | `Bitget` | `56.32%` | `43.68%` | `1.29` | 1,020,000.00 USD |
| `4H` | `BingX` | `46.32%` | `53.68%` | `0.86` | 9,290,000.00 USD |
| `4H` | `MEXC` | `48.57%` | `51.43%` | `0.94` | 1,610,000.00 USD |
| `4H` | `Bitunix` | `47.71%` | `52.29%` | `0.91` | 966,340.00 USD |
| `4H` | `Hyperliquid` | `49.71%` | `50.29%` | `0.99` | 484,760.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.36%` | `49.64%` | `1.01` | 2,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.67%` | `3.33%` | `29.03` | 5,320,000.00 USD |
| `4H` | `HTX` | `45.99%` | `54.01%` | `0.85` | 123,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.78%` | `59.22%` | `0.69` | 258,670.00 USD |
| `4H` | `Aster` | `64.59%` | `35.41%` | `1.82` | 117,570.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.17%` | `68.83%` | `0.45` | 52,110.00 USD |
| `4H` | `Whale Positions` | `47.68%` | `52.32%` | `0.91` | 19,340,000.00 USD |
| `4H` | `Global Accounts` | `52.66%` | `47.34%` | `1.11` | 62,420,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `290.33` | `290.07` | `290.33` | `290.97` | `289.12` | 2,596,782.25 USD | 1,062,961.61 USD | 1,533,820.64 USD | -470,859.04 USD | `-18.13%` | `12B / 36S` |
| `0:00 UTC` | `287.31` | `288.38` | `287.31` | `290.09` | `287.09` | 2,309,907.78 USD | 1,171,627.08 USD | 1,138,280.70 USD | 33,346.39 USD | `+1.44%` | `26B / 14S` |
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `290.00` | `289.14` | `290.00` | `290.24` | `288.04` | 1,415,488.00 USD | 804,419.88 USD | 611,068.12 USD | 193,351.76 USD | `+13.66%` | `22B / 10S` |
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `290.49` | `289.33` | `290.49` | `291.59` | `287.81` | 1,897,766.44 USD | 827,805.59 USD | 1,069,960.85 USD | -242,155.26 USD | `-12.76%` | `25B / 40S` |
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `288.94` | `289.00` | `289.94` | `288.00` | 1,099,157.40 USD | 660,933.72 USD | 438,223.69 USD | 222,710.03 USD | `+20.26%` | `43B / 33S` |
| `5:00 UTC` | `287.91` | `288.60` | `287.91` | `289.87` | `287.51` | 851,365.60 USD | 435,531.09 USD | 415,834.51 USD | 19,696.57 USD | `+2.31%` | `18B / 22S` |
| `0:00 UTC` | `287.14` | `286.73` | `287.14` | `287.81` | `286.01` | 435,317.35 USD | 155,241.58 USD | 280,075.78 USD | -124,834.20 USD | `-28.68%` | `29B / 40S` |

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
| `5m` | -90,080.00 USD | -264,820.00 USD | **`DISTRIBUTION`** |
| `15m` | -103,610.00 USD | -306,510.00 USD | **`DISTRIBUTION`** |
| `30m` | -123,560.00 USD | 24,970.00 USD | **`DISTRIBUTION`** |
| `1h` | -146,250.00 USD | -615,550.00 USD | **`DISTRIBUTION`** |
| `2h` | 35,380.00 USD | 82,800.00 USD | **`ACCUMULATION`** |
| `4h` | 282,790.00 USD | -3,250,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 311,740.00 USD | -1,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 133,490.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 279,370.00 USD | -2,270,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -941,060.00 USD | -8,300,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 133,230.00 USD | -12,520,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,250,000.00 USD | -137,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-90.08K` | 15m=`-103.61K` | 1h=`-146.25K` | 24h=`-941.06K`
* Futures Capital Netflows: 5m=`-264.82K` | 15m=`-306.51K` | 1h=`-615.55K` | 24h=`-8.30M`
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
  * `2026-10-29 23:31:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:27 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:27 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `276.52` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `272.89` (Risk Distance: `3.63` pts)
  * +2.5R Take Profit: `285.61`
  * Mathematical Lot Sizing: **`2.75 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.19` (Risk Distance: `3.63` pts)
  * +2.5R Take Profit: `278.47`
  * Mathematical Lot Sizing: **`2.75 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`288.84`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
