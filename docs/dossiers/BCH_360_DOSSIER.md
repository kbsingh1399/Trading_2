# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 01:17:49 IST` (`2026-10-29 19:47:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `286.96` | **Live Ask Quote**: `287.54` | **Mid Price**: `287.25`
- **Spread Points**: `580.00` | **Spread BPS**: `20.19 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.82` | VWAP Z-Score: `+1.18` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.18` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.40` | Lower -3.00σ Band: `270.24`
  * Upper +2.51σ Band: `293.34` | Lower -2.51σ Band: `272.30`
  * Upper +2.01σ Band: `291.25` | Lower -2.01σ Band: `274.39`
  * Upper +2.00σ Band: `291.21` | Lower -2.00σ Band: `274.44`
  * Upper +1.28σ Band: `288.19` | Lower -1.28σ Band: `277.45`
  * Upper +1.00σ Band: `287.01` | Lower -1.00σ Band: `278.63`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.59` | EMA-20=`286.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`284.18` (Slope: `+0.0000`) | EMA-100=`284.44`
  * Institutional Anchors: EMA-144=`284.82` | EMA-200=`284.77` (Slope: `+0.1525`) | EMA-233=`285.06`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.68` (Distance: `-0.13%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.08%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+3.90%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`299.16` | POC=`296.76` | VAL=`289.44`
  * Prior Day Extremes: PDH=`304.16` | PDL=`281.75` | PDC=`288.90`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.02` | Weekly POC=`278.72` | Weekly VAL=`275.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`290.60` | Low=`274.76`
  * London Session (08:00-16:00 UTC): High=`281.86` | Low=`276.86`
  * New York Session (13:00-21:00 UTC): High=`292.96` | Low=`277.16`
  * Initial Balance (First Hour): IB High=`281.86` | IB Low=`279.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `286.10` - `288.40`
  * Optimal Trade Entry (OTE 0.705): `287.82`
  * Structural Invalidation Anchor (0.786): `289.55`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `288.16` | `288.89` | `287.75` | `287.75` | `722` | 208,157.96 USD | -31,760.50 USD | `-15.26%` | -2,441,271.03 USD | `-1.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `287.74` | `287.81` | `287.26` | `287.34` | `560` | 160,948.31 USD | 38,272.89 USD | `+23.78%` | -2,402,998.15 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `287.35` | `287.86` | `287.35` | `287.50` | `344` | 98,968.82 USD | 11,844.17 USD | `+11.97%` | -2,391,153.98 USD | `-0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `288.16` | `288.53` | `286.82` | `287.43` | `2,694` | 774,817.75 USD | 109,914.46 USD | `+14.19%` | -2,550,521.89 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `287.43` | `289.02` | `287.21` | `288.16` | `1,755` | 505,722.48 USD | 141,011.36 USD | `+27.88%` | -2,409,510.53 USD | `+0.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `288.16` | `288.89` | `287.26` | `287.50` | `1,626` | 468,075.09 USD | 18,356.55 USD | `+3.92%` | -2,391,153.98 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.48` | `291.58` | `286.48` | `288.89` | `23,176` | 6,696,574.59 USD | 177,926.21 USD | `+2.66%` | -3,100,524.21 USD | `+0.54` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `288.88` | `289.93` | `285.90` | `288.17` | `14,933` | 4,302,316.36 USD | 354,117.88 USD | `+8.23%` | -2,746,406.33 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.16` | `289.02` | `286.82` | `287.53` | `6,070` | 1,747,304.77 USD | 270,592.92 USD | `+15.49%` | -2,475,813.41 USD | `+0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `287.53` | `92,001` | 26,615,353.07 USD | -1,488,809.02 USD | `-5.59%` | -2,475,813.41 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `287.53` | `92,001` | 26,615,353.07 USD | -1,488,809.02 USD | `-5.59%` | -2,475,813.41 USD | `-0.71` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`287.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1957` | `0x12d2...f97f` | `LONG` | 1,043,122.54 USD | `3,627,243,000,000.00` | `303.26` | `287.34` | `0.000000` | -56,876.80 USD | `-5.45%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.70` (Vol: 152,600.00 USD, Dist: `+2.87%`) | Long MP=`271.76` (Vol: 166,000.00 USD, Dist: `--5.46%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.41%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--5.43%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.41%`) | Long MP=`274.98` (Vol: 169,100.00 USD, Dist: `--4.34%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+2.41%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--8.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 469,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 468,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 461,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 457,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 171.25 USD | 457,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 457,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 52,660.00 USD | 457,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 404,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 404,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `138.50` | 2,080.00 USD | 403,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `146.50` | 7,330.00 USD | 401,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 394,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 393,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 392,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 389,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 389,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 389,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 1,090.00 USD | 388,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 387,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 387,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 387,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `180.50` | 5,690.00 USD | 386,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 191.57 USD | 381,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 380,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `187.50` | 562.50 USD | 380,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 379,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 1,230.00 USD | 379,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 378,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 859.22 USD | 376,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 765.08 USD | 375,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 374,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 583.61 USD | 374,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 39,880.00 USD | 374,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 781.11 USD | 334,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 964.93 USD | 333,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 332,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 347.60 USD | 328,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 6,260.00 USD | 328,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `221.50` | 1,640.00 USD | 322,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 320,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `225.50` | 613.13 USD | 287,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 286,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 285,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 285,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,190.00 USD | 284,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 283,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 429.66 USD | 283,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 282,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 1,490.00 USD | 282,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 281,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `241.50` | 367.32 USD | 280,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 279,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 278,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 6,740.00 USD | 274,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `246.50` | 49,300.00 USD | 267,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 218,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.50` | 18,330,000.00 USD | 18,330,000.00 USD | 34,780.00 USD | 12,870.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 18,250,000.00 USD | 18,250,000.00 USD | 14,600.00 USD | 14,030.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 18,210,000.00 USD | 18,210,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 8,700.00 USD | 217,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.70` | 18,170,000.00 USD | 18,170,000.00 USD | 50,470.00 USD | 27,880.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.10` | 18,070,000.00 USD | 18,070,000.00 USD | 45,440.00 USD | 14,600.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.50` | 17,990,000.00 USD | 17,990,000.00 USD | 9,050.00 USD | 52,190.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 208,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.90` | 17,910,000.00 USD | 17,910,000.00 USD | 25,590.00 USD | 15,360.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 17,860,000.00 USD | 17,860,000.00 USD | 32,380.00 USD | 72,300.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 207,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 17,740,000.00 USD | 17,740,000.00 USD | 57,590.00 USD | 62,360.00 USD | 37,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.10` | 17,580,000.00 USD | 17,580,000.00 USD | 62,800.00 USD | 22,760.00 USD | 29,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.50` | 17,460,000.00 USD | 17,460,000.00 USD | 54,060.00 USD | 28,380.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 207,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.90` | 17,360,000.00 USD | 17,360,000.00 USD | 13,480.00 USD | 20,850.00 USD | 7.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 17,330,000.00 USD | 17,330,000.00 USD | 30,240.00 USD | 36,380.00 USD | 26,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 17,240,000.00 USD | 17,240,000.00 USD | 4,870.00 USD | 29,070.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.10` | 17,170,000.00 USD | 17,170,000.00 USD | 28,730.00 USD | 36,890.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.50` | 17,090,000.00 USD | 17,090,000.00 USD | 32,120.00 USD | 13,170.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 206,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.90` | 17,020,000.00 USD | 17,020,000.00 USD | 14,160.00 USD | 6,220.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 17,000,000.00 USD | 17,000,000.00 USD | 55,960.00 USD | 10,820.00 USD | 42,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 16,890,000.00 USD | 16,890,000.00 USD | 19,690.00 USD | 13,040.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.10` | 16,810,000.00 USD | 16,810,000.00 USD | 53,510.00 USD | 24,220.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.50` | 16,720,000.00 USD | 16,720,000.00 USD | 36,010.00 USD | 15,160.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.90` | 16,640,000.00 USD | 16,640,000.00 USD | 45,670.00 USD | 13,800.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 8,140,000.00 USD | 8,140,000.00 USD | 4,240.00 USD | 638.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 16,550,000.00 USD | 16,550,000.00 USD | 23,000.00 USD | 2,970.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.70` | 16,490,000.00 USD | 16,490,000.00 USD | 46,990.00 USD | 7,280.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 8,120,000.00 USD | 8,120,000.00 USD | 32.50 USD | 4,120.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.10` | 16,420,000.00 USD | 16,420,000.00 USD | 72,040.00 USD | 39,480.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 8,090,000.00 USD | 8,090,000.00 USD | 3,360.00 USD | 5,260.00 USD | 45.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.50` | 16,280,000.00 USD | 16,280,000.00 USD | 109,750.00 USD | 15,650.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.90` | 8,090,000.00 USD | 8,090,000.00 USD | 5,230.00 USD | 10,960.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 16,130,000.00 USD | 16,130,000.00 USD | 20,250.00 USD | 10,000.00 USD | 34,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 8,060,000.00 USD | 8,060,000.00 USD | 15,050.00 USD | 4,190.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 16,070,000.00 USD | 16,070,000.00 USD | 3,650.00 USD | 36,950.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 8,020,000.00 USD | 8,020,000.00 USD | 14,700.00 USD | 19,050.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 16,020,000.00 USD | 16,020,000.00 USD | 17,070.00 USD | 11,440.00 USD | 84.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 7,960,000.00 USD | 7,960,000.00 USD | 8,090.00 USD | 9,630.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.10` | 15,990,000.00 USD | 15,990,000.00 USD | 23,940.00 USD | 8,740.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 7,930,000.00 USD | 7,930,000.00 USD | 2,850.00 USD | 8,760.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.50` | 15,950,000.00 USD | 15,950,000.00 USD | 6,310.00 USD | 31,320.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.90` | 7,900,000.00 USD | 7,900,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 15,890,000.00 USD | 15,890,000.00 USD | 17,580.00 USD | 30,210.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 7,860,000.00 USD | 7,860,000.00 USD | 8,660.00 USD | 16,360.00 USD | 500.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 15,800,000.00 USD | 15,800,000.00 USD | 1,980.00 USD | 33,580.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 7,840,000.00 USD | 7,840,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 15,750,000.00 USD | 15,750,000.00 USD | 24,930.00 USD | 48,920.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 7,830,000.00 USD | 7,830,000.00 USD | 517.32 USD | 4,790.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.10` | 15,660,000.00 USD | 15,660,000.00 USD | 60,340.00 USD | 36,740.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 7,810,000.00 USD | 7,810,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.50` | 15,530,000.00 USD | 15,530,000.00 USD | 36,340.00 USD | 26,170.00 USD | 24.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 7,800,000.00 USD | 7,800,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 15,460,000.00 USD | 15,460,000.00 USD | 66,900.00 USD | 32,740.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 7,800,000.00 USD | 7,800,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 15,330,000.00 USD | 15,330,000.00 USD | 31,720.00 USD | 23,840.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 7,770,000.00 USD | 7,770,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 15,240,000.00 USD | 15,240,000.00 USD | 265,940.00 USD | 104,900.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 7,750,000.00 USD | 7,750,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.10` | 14,840,000.00 USD | 14,840,000.00 USD | 93,540.00 USD | 27,860.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 7,750,000.00 USD | 7,750,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.50` | 14,680,000.00 USD | 14,680,000.00 USD | 49,620.00 USD | 14,050.00 USD | 37,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.90` | 7,710,000.00 USD | 7,710,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 14,580,000.00 USD | 14,580,000.00 USD | 22,920.00 USD | 73,550.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 7,670,000.00 USD | 7,670,000.00 USD | 19,790.00 USD | 8,590.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 14,460,000.00 USD | 14,460,000.00 USD | 111,680.00 USD | 47,310.00 USD | 103,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 7,600,000.00 USD | 7,600,000.00 USD | 23,810.00 USD | 23,390.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.70` | 14,200,000.00 USD | 14,200,000.00 USD | 54,220.00 USD | 73,540.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 7,520,000.00 USD | 7,520,000.00 USD | 10,200.00 USD | 87.00 USD | 7.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.10` | 14,030,000.00 USD | 14,030,000.00 USD | 156,170.00 USD | 143,870.00 USD | 57,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 7,510,000.00 USD | 7,510,000.00 USD | 27,700.00 USD | 3,060.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.50` | 13,670,000.00 USD | 13,670,000.00 USD | 112,390.00 USD | 71,680.00 USD | 105,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.90` | 7,470,000.00 USD | 7,470,000.00 USD | 32,360.00 USD | 6,530.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 13,380,000.00 USD | 13,380,000.00 USD | 138,720.00 USD | 163,270.00 USD | 59,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 7,430,000.00 USD | 7,430,000.00 USD | 17,990.00 USD | 11,130.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 13,020,000.00 USD | 13,020,000.00 USD | 112,800.00 USD | 156,840.00 USD | 88,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 7,400,000.00 USD | 7,400,000.00 USD | 83,350.00 USD | 112,120.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.70` | 12,660,000.00 USD | 12,660,000.00 USD | 171,250.00 USD | 207,730.00 USD | 62,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 7,190,000.00 USD | 7,190,000.00 USD | 55,330.00 USD | 80,220.00 USD | 47,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.10` | 12,220,000.00 USD | 12,220,000.00 USD | 108,270.00 USD | 282,540.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 7,000,000.00 USD | 7,000,000.00 USD | 57,220.00 USD | 101,650.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.50` | 11,730,000.00 USD | 11,730,000.00 USD | 200,320.00 USD | 140,160.00 USD | 76,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.90` | 6,810,000.00 USD | 6,810,000.00 USD | 92,000.00 USD | 36,340.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 11,310,000.00 USD | 11,310,000.00 USD | 199,940.00 USD | 107,670.00 USD | 92,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 6,640,000.00 USD | 6,640,000.00 USD | 28,630.00 USD | 16,320.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 10,910,000.00 USD | 10,910,000.00 USD | 280,160.00 USD | 180,610.00 USD | 85,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.70` | 6,580,000.00 USD | 6,580,000.00 USD | 39,120.00 USD | 24,350.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.70` | 10,370,000.00 USD | 10,370,000.00 USD | 55,620.00 USD | 85,320.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 6,500,000.00 USD | 6,500,000.00 USD | 97,380.00 USD | 77,420.00 USD | 98,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.10` | 10,210,000.00 USD | 10,210,000.00 USD | 143,830.00 USD | 169,870.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 6,230,000.00 USD | 6,230,000.00 USD | 71,720.00 USD | 36,250.00 USD | 36,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.50` | 9,800,000.00 USD | 9,800,000.00 USD | 79,840.00 USD | 97,680.00 USD | 214,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 6,090,000.00 USD | 6,090,000.00 USD | 11,770.00 USD | 23,900.00 USD | 66,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 9,410,000.00 USD | 9,410,000.00 USD | 275,900.00 USD | 146,080.00 USD | 90,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 5,980,000.00 USD | 5,980,000.00 USD | 56,610.00 USD | 46,080.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 8,900,000.00 USD | 8,900,000.00 USD | 128,290.00 USD | 123,510.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,110.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.70` | 5,810,000.00 USD | 5,810,000.00 USD | 20,370.00 USD | 13,810.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.70` | 8,610,000.00 USD | 8,610,000.00 USD | 379,860.00 USD | 48,230.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 5,770,000.00 USD | 5,770,000.00 USD | 109,050.00 USD | 33,030.00 USD | 17,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.10` | 8,100,000.00 USD | 8,100,000.00 USD | 257,880.00 USD | 75,270.00 USD | 148,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 5,610,000.00 USD | 5,610,000.00 USD | 73,010.00 USD | 24,600.00 USD | 24,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.50` | 7,620,000.00 USD | 7,620,000.00 USD | 157,320.00 USD | 167,310.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 5,490,000.00 USD | 5,490,000.00 USD | 79,800.00 USD | 57,910.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 7,260,000.00 USD | 7,260,000.00 USD | 151,480.00 USD | 204,700.00 USD | 83,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 5,340,000.00 USD | 5,340,000.00 USD | 179,910.00 USD | 204,160.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 6,820,000.00 USD | 6,820,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 4,920,000.00 USD | 4,920,000.00 USD | 142,100.00 USD | 172,390.00 USD | 94,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 6,140,000.00 USD | 6,140,000.00 USD | 195,450.00 USD | 467,490.00 USD | 205,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 4,510,000.00 USD | 4,510,000.00 USD | 113,450.00 USD | 203,210.00 USD | 71,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.10` | 5,270,000.00 USD | 5,270,000.00 USD | 455,510.00 USD | 216,600.00 USD | 178,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 4,120,000.00 USD | 4,120,000.00 USD | 195,280.00 USD | 71,370.00 USD | 104,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.50` | 4,420,000.00 USD | 4,420,000.00 USD | 345,450.00 USD | 165,770.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.90` | 3,750,000.00 USD | 3,750,000.00 USD | 57,970.00 USD | 35,940.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 3,810,000.00 USD | 3,810,000.00 USD | 260,340.00 USD | 168,220.00 USD | 90,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 3,610,000.00 USD | 3,610,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 3,290,000.00 USD | 3,290,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 3,440,000.00 USD | 3,440,000.00 USD | 17,100.00 USD | 37,310.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 3,150,000.00 USD | 3,150,000.00 USD | 1,350.00 USD | 51,050.00 USD | 11.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 3,370,000.00 USD | 3,370,000.00 USD | 85,030.00 USD | 50,210.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.10` | 3,100,000.00 USD | 3,100,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 3,220,000.00 USD | 3,220,000.00 USD | 35,490.00 USD | 31,830.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.50` | 3,090,000.00 USD | 3,090,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.90` | 3,130,000.00 USD | 3,130,000.00 USD | 13,620.00 USD | 26,230.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 3,090,000.00 USD | 3,090,000.00 USD | 45,560.00 USD | 22,950.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 3,060,000.00 USD | 3,060,000.00 USD | 36,000.00 USD | 66,900.00 USD | 59,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 2,890,000.00 USD | 2,890,000.00 USD | 57,640.00 USD | 47,660.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 27,190.00 USD | 84,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 2,760,000.00 USD | 2,760,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.10` | 2,830,000.00 USD | 2,830,000.00 USD | 24,750.00 USD | 0.00 USD | 59,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 2,710,000.00 USD | 2,710,000.00 USD | 67,950.00 USD | 33,500.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.50` | 2,750,000.00 USD | 2,750,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 2,580,000.00 USD | 2,580,000.00 USD | 24,100.00 USD | 27,270.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.90` | 2,660,000.00 USD | 2,660,000.00 USD | 42,950.00 USD | 31,760.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 2,520,000.00 USD | 2,520,000.00 USD | 53,390.00 USD | 33,630.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 2,560,000.00 USD | 2,560,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 2,390,000.00 USD | 2,390,000.00 USD | 20,320.00 USD | 0.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 2,490,000.00 USD | 2,490,000.00 USD | 46,800.00 USD | 0.00 USD | 54,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 2,360,000.00 USD | 2,360,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 2,300,000.00 USD | 2,300,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 4,860.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.90` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 2,180,000.00 USD | 2,180,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.70` | 2,100,000.00 USD | 2,100,000.00 USD | 19,210.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 2,330,000.00 USD | 2,330,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 2,050,000.00 USD | 2,050,000.00 USD | 76,000.00 USD | 43,170.00 USD | 226,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.50` | 1,710,000.00 USD | 1,710,000.00 USD | 5,740.00 USD | 24,390.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.50` | 2,070,000.00 USD | 2,070,000.00 USD | 32,190.00 USD | 0.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.90` | 1,640,000.00 USD | 1,640,000.00 USD | 52,960.00 USD | 54,510.00 USD | 98,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.90` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 117.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 1,430,000.00 USD | 1,430,000.00 USD | 18,430.00 USD | 0.00 USD | 112,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 37,310.00 USD | 89,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.70` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 30,480.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 1,220,000.00 USD | 1,220,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.10` | 1,630,000.00 USD | 1,630,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.50` | 1,080,000.00 USD | 1,080,000.00 USD | 39,670.00 USD | 70,600.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.50` | 1,450,000.00 USD | 1,450,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.90` | 947,650.00 USD | 947,650.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.30` | 918,540.00 USD | 918,540.00 USD | 20,960.00 USD | 64,640.00 USD | 93,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.30` | 906,630.00 USD | 906,630.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.70` | 739,260.00 USD | 739,260.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.70` | 616,790.00 USD | 616,790.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.10` | 576,640.00 USD | 576,640.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.10` | 503,160.00 USD | 503,160.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.50` | 546,640.00 USD | 546,640.00 USD | 111,830.00 USD | 0.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.50` | 428,310.00 USD | 428,310.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.90` | 397,290.00 USD | 397,290.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.90` | 308,870.00 USD | 308,870.00 USD | 27,530.00 USD | 141,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.30` | 101,950.00 USD | 101,950.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.30` | 140,180.00 USD | 140,180.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.70` | 154,260.00 USD | 154,260.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.10` | 293,550.00 USD | 293,550.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 294,480.00 USD | 294,480.00 USD | 0.00 USD | 927.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.10` | 295,420.00 USD | 295,420.00 USD | 0.00 USD | 947.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 0.00 USD | 3.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 21,950.00 USD | 21,950.00 USD | 0.00 USD | 9,950.00 USD | 7.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 305,520.00 USD | 305,520.00 USD | 0.00 USD | 10,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.70` | 59,720.00 USD | 59,720.00 USD | 0.00 USD | 15,650.00 USD | 22,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 398,750.00 USD | 398,750.00 USD | 0.00 USD | 93,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 94,550.00 USD | 94,550.00 USD | 0.00 USD | 34,810.00 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.10` | 517,590.00 USD | 517,590.00 USD | 0.00 USD | 118,820.00 USD | 18.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 141,910.00 USD | 141,910.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.50` | 543,470.00 USD | 543,470.00 USD | 0.00 USD | 25,780.00 USD | 103.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 234,030.00 USD | 234,030.00 USD | 10,870.00 USD | 81,240.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 663,560.00 USD | 663,560.00 USD | 0.00 USD | 120,030.00 USD | 68.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 300,730.00 USD | 300,730.00 USD | 6,120.00 USD | 60,590.00 USD | 1.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 777,370.00 USD | 777,370.00 USD | 534.50 USD | 113,250.00 USD | 22.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 562,190.00 USD | 562,190.00 USD | 88,260.00 USD | 73,530.00 USD | 99,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 815,050.00 USD | 815,050.00 USD | 37,280.00 USD | 346.50 USD | 54.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 703,720.00 USD | 703,720.00 USD | 36,530.00 USD | 47,290.00 USD | 57,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.10` | 1,040,000.00 USD | 1,040,000.00 USD | 85,150.00 USD | 32,540.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 1,030,000.00 USD | 1,030,000.00 USD | 129,200.00 USD | 98,900.00 USD | 95,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.50` | 1,120,000.00 USD | 1,120,000.00 USD | 69,950.00 USD | 14,450.00 USD | 30.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 1,270,000.00 USD | 1,270,000.00 USD | 53,910.00 USD | 79,400.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 1,380,000.00 USD | 1,380,000.00 USD | 63,470.00 USD | 88,260.00 USD | 104,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 1,480,000.00 USD | 1,480,000.00 USD | 86,610.00 USD | 69,170.00 USD | 63,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 1,740,000.00 USD | 1,740,000.00 USD | 45,590.00 USD | 65,470.00 USD | 252,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 1,740,000.00 USD | 1,740,000.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 2,050,000.00 USD | 2,050,000.00 USD | 105,410.00 USD | 71,570.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 1,980,000.00 USD | 1,980,000.00 USD | 90,530.00 USD | 115,020.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.10` | 2,340,000.00 USD | 2,340,000.00 USD | 75,740.00 USD | 90,370.00 USD | 119,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 2,080,000.00 USD | 2,080,000.00 USD | 43,030.00 USD | 34,820.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.50` | 2,470,000.00 USD | 2,470,000.00 USD | 1,060.00 USD | 78,480.00 USD | 57,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 2,210,000.00 USD | 2,210,000.00 USD | 22,010.00 USD | 21,080.00 USD | 91,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 2,870,000.00 USD | 2,870,000.00 USD | 206,840.00 USD | 56,070.00 USD | 134,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 2,290,000.00 USD | 2,290,000.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 2,880,000.00 USD | 2,880,000.00 USD | 3,960.00 USD | 443.90 USD | 5.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 2,300,000.00 USD | 2,300,000.00 USD | 807.94 USD | 723.06 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 2,970,000.00 USD | 2,970,000.00 USD | 144.38 USD | 58,490.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 2,410,000.00 USD | 2,410,000.00 USD | 44,470.00 USD | 6,340.00 USD | 52,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.10` | 3,160,000.00 USD | 3,160,000.00 USD | 49,240.00 USD | 82,010.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 2,520,000.00 USD | 2,520,000.00 USD | 7,150.00 USD | 21,100.00 USD | 84,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.50` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 16,080.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 2,700,000.00 USD | 2,700,000.00 USD | 39,590.00 USD | 15,820.00 USD | 118,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 3,330,000.00 USD | 3,330,000.00 USD | 70,090.00 USD | 1,940.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 2,780,000.00 USD | 2,780,000.00 USD | 33,660.00 USD | 21,880.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 3,380,000.00 USD | 3,380,000.00 USD | 2,570.00 USD | 2,980.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 628.05 USD | 628.05 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.70` | 2,850,000.00 USD | 2,850,000.00 USD | 12,530.00 USD | 22,710.00 USD | 34,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 3,420,000.00 USD | 3,420,000.00 USD | 5,310.00 USD | 9,400.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 3,000,000.00 USD | 3,000,000.00 USD | 51,990.00 USD | 44,400.00 USD | 58,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.10` | 3,470,000.00 USD | 3,470,000.00 USD | 51,500.00 USD | 2,420.00 USD | 58.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 3,070,000.00 USD | 3,070,000.00 USD | 18,720.00 USD | 10,730.00 USD | 41,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.50` | 3,530,000.00 USD | 3,530,000.00 USD | 866.20 USD | 36,110.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 3,160,000.00 USD | 3,160,000.00 USD | 12,920.00 USD | 32,430.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 3,670,000.00 USD | 3,670,000.00 USD | 24,730.00 USD | 35,210.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 3,270,000.00 USD | 3,270,000.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 3,900,000.00 USD | 3,900,000.00 USD | 71,140.00 USD | 56,660.00 USD | 94,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 1,980.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.70` | 3,330,000.00 USD | 3,330,000.00 USD | 31,740.00 USD | 20,120.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.70` | 4,070,000.00 USD | 4,070,000.00 USD | 37,640.00 USD | 133,050.00 USD | 106.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 3,430,000.00 USD | 3,430,000.00 USD | 44,760.00 USD | 37,250.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.10` | 4,270,000.00 USD | 4,270,000.00 USD | 53,220.00 USD | 122,660.00 USD | 26,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 3,490,000.00 USD | 3,490,000.00 USD | 10,520.00 USD | 20,620.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.50` | 4,450,000.00 USD | 4,450,000.00 USD | 31,330.00 USD | 103,660.00 USD | 41,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 3,510,000.00 USD | 3,510,000.00 USD | 1,230.00 USD | 1,910.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 4,550,000.00 USD | 4,550,000.00 USD | 40,380.00 USD | 63,830.00 USD | 90.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 3,560,000.00 USD | 3,560,000.00 USD | 31,930.00 USD | 299.52 USD | 14,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 2,170.00 USD | 96.05 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `303.50` | 336.58 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `303.70` | 3,580,000.00 USD | 3,580,000.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 4,610,000.00 USD | 4,610,000.00 USD | 17,370.00 USD | 11,960.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 3,650,000.00 USD | 3,650,000.00 USD | 22,560.00 USD | 981.10 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.10` | 4,610,000.00 USD | 4,610,000.00 USD | 5,440.00 USD | 855.36 USD | 122.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 3,730,000.00 USD | 3,730,000.00 USD | 13,310.00 USD | 9,590.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.50` | 4,630,000.00 USD | 4,630,000.00 USD | 3,480.00 USD | 11,660.00 USD | 111.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 3,730,000.00 USD | 3,730,000.00 USD | 697.80 USD | 146.63 USD | 2.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 4,690,000.00 USD | 4,690,000.00 USD | 34,680.00 USD | 19,830.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 3,740,000.00 USD | 3,740,000.00 USD | 11,260.00 USD | 0.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 5,100,000.00 USD | 5,100,000.00 USD | 162,420.00 USD | 128,830.00 USD | 117,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 3,760,000.00 USD | 3,760,000.00 USD | 7,960.00 USD | 1,830.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 5,210,000.00 USD | 5,210,000.00 USD | 82,270.00 USD | 14,420.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 3,770,000.00 USD | 3,770,000.00 USD | 4,210.00 USD | 2,720.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.10` | 5,350,000.00 USD | 5,350,000.00 USD | 22,930.00 USD | 67,530.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 3,780,000.00 USD | 3,780,000.00 USD | 4,550.00 USD | 9,580.00 USD | 58.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.50` | 5,480,000.00 USD | 5,480,000.00 USD | 30,150.00 USD | 40,640.00 USD | 65,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 3,870,000.00 USD | 3,870,000.00 USD | 32,120.00 USD | 40,320.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 5,650,000.00 USD | 5,650,000.00 USD | 58,810.00 USD | 50,710.00 USD | 57,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 3,920,000.00 USD | 3,920,000.00 USD | 7,930.00 USD | 34,600.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 5,890,000.00 USD | 5,890,000.00 USD | 34,320.00 USD | 124,020.00 USD | 83,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 3,980,000.00 USD | 3,980,000.00 USD | 19,670.00 USD | 28,030.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 6,070,000.00 USD | 6,070,000.00 USD | 84,930.00 USD | 73,620.00 USD | 23,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 4,030,000.00 USD | 4,030,000.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.10` | 6,350,000.00 USD | 6,350,000.00 USD | 105,700.00 USD | 62,570.00 USD | 106,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 4,040,000.00 USD | 4,040,000.00 USD | 5,570.00 USD | 3,510.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.50` | 6,600,000.00 USD | 6,600,000.00 USD | 118,090.00 USD | 65,810.00 USD | 65,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 4,070,000.00 USD | 4,070,000.00 USD | 12,710.00 USD | 6,030.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 6,710,000.00 USD | 6,710,000.00 USD | 60,660.00 USD | 32,520.00 USD | 19,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 4,090,000.00 USD | 4,090,000.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 6,800,000.00 USD | 6,800,000.00 USD | 27,920.00 USD | 25,880.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 4,130,000.00 USD | 4,130,000.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 7,130,000.00 USD | 7,130,000.00 USD | 40,410.00 USD | 132,640.00 USD | 153,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 4,130,000.00 USD | 4,130,000.00 USD | 4,390.00 USD | 4,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.10` | 7,290,000.00 USD | 7,290,000.00 USD | 34,250.00 USD | 63,210.00 USD | 62,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 4,140,000.00 USD | 4,140,000.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.50` | 7,450,000.00 USD | 7,450,000.00 USD | 68,560.00 USD | 73,910.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 3,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.90` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 2.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 7,520,000.00 USD | 7,520,000.00 USD | 35,670.00 USD | 31,060.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 4,140,000.00 USD | 4,140,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 7,720,000.00 USD | 7,720,000.00 USD | 84,180.00 USD | 64,750.00 USD | 47,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `311.50` | 539.21 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `311.70` | 4,160,000.00 USD | 4,160,000.00 USD | 9,900.00 USD | 6,590.00 USD | 4.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 7,800,000.00 USD | 7,800,000.00 USD | 34,040.00 USD | 11,260.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 4,160,000.00 USD | 4,160,000.00 USD | 244.00 USD | 39.75 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.10` | 7,870,000.00 USD | 7,870,000.00 USD | 46,850.00 USD | 246.55 USD | 24,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 4,180,000.00 USD | 4,180,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.50` | 7,960,000.00 USD | 7,960,000.00 USD | 19,540.00 USD | 23,400.00 USD | 49,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 4,190,000.00 USD | 4,190,000.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 8,030,000.00 USD | 8,030,000.00 USD | 22,600.00 USD | 18,280.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 4,210,000.00 USD | 4,210,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 8,150,000.00 USD | 8,150,000.00 USD | 64,910.00 USD | 30,310.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 4,220,000.00 USD | 4,220,000.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 8,220,000.00 USD | 8,220,000.00 USD | 32,170.00 USD | 14,450.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.10` | 8,300,000.00 USD | 8,300,000.00 USD | 26,810.00 USD | 2,090.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 4,230,000.00 USD | 4,230,000.00 USD | 4,240.00 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.50` | 8,370,000.00 USD | 8,370,000.00 USD | 48,630.00 USD | 258.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 8,410,000.00 USD | 8,410,000.00 USD | 29,590.00 USD | 289.95 USD | 10,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 4,240,000.00 USD | 4,240,000.00 USD | 32.50 USD | 144.50 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 8,410,000.00 USD | 8,410,000.00 USD | 5,690.00 USD | 0.00 USD | 52.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 4,270,000.00 USD | 4,270,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 8,520,000.00 USD | 8,520,000.00 USD | 9,200.00 USD | 50,710.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 4,290,000.00 USD | 4,290,000.00 USD | 6,930.00 USD | 5,010.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.10` | 8,630,000.00 USD | 8,630,000.00 USD | 38,840.00 USD | 19,940.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 4,300,000.00 USD | 4,300,000.00 USD | 235.25 USD | 5,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.50` | 8,680,000.00 USD | 8,680,000.00 USD | 16,120.00 USD | 20,380.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `316.50` | 6,540.00 USD | 10,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `316.90` | 4,330,000.00 USD | 4,330,000.00 USD | 14,650.00 USD | 3,700.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 8,690,000.00 USD | 8,690,000.00 USD | 3,030.00 USD | 10,360.00 USD | 101.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.30` | 4,350,000.00 USD | 4,350,000.00 USD | 2,250.00 USD | 6,390.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 8,710,000.00 USD | 8,710,000.00 USD | 14,540.00 USD | 854.23 USD | 102.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.70` | 4,410,000.00 USD | 4,410,000.00 USD | 18,240.00 USD | 15,360.00 USD | 26,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 8,710,000.00 USD | 8,710,000.00 USD | 620.15 USD | 894.23 USD | 88.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.10` | 4,430,000.00 USD | 4,430,000.00 USD | 2,290.00 USD | 9,270.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.10` | 8,740,000.00 USD | 8,740,000.00 USD | 22,250.00 USD | 8,980.00 USD | 142.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.50` | 4,450,000.00 USD | 4,450,000.00 USD | 4,700.00 USD | 7,500.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.50` | 8,810,000.00 USD | 8,810,000.00 USD | 3,010.00 USD | 25,720.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 10,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.90` | 4,490,000.00 USD | 4,490,000.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 8,860,000.00 USD | 8,860,000.00 USD | 10,270.00 USD | 17,970.00 USD | 23,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.30` | 4,510,000.00 USD | 4,510,000.00 USD | 8,310.00 USD | 16,300.00 USD | 488.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 19,140.00 USD | 5.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 8,890,000.00 USD | 8,890,000.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.10` | 8,970,000.00 USD | 8,970,000.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.50` | 8,990,000.00 USD | 8,990,000.00 USD | 15,190.00 USD | 10,420.00 USD | 49.92 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 11,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `321.30` | 9,020,000.00 USD | 9,020,000.00 USD | 9,210.00 USD | 8,300.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.70` | 9,050,000.00 USD | 9,050,000.00 USD | 4,780.00 USD | 9,440.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.10` | 9,080,000.00 USD | 9,080,000.00 USD | 22,940.00 USD | 7,790.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.50` | 9,080,000.00 USD | 9,080,000.00 USD | 555.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 9,100,000.00 USD | 9,100,000.00 USD | 16,590.00 USD | 5,630.00 USD | 0.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.30` | 9,140,000.00 USD | 9,140,000.00 USD | 14,160.00 USD | 6,560.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.70` | 9,140,000.00 USD | 9,140,000.00 USD | 269.10 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.10` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 12,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `339.50` | 1,360.00 USD | 13,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 14,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `361.50` | 39,770.00 USD | 54,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 54,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `395.50` | 3,430.00 USD | 58,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `427.50` | 9,480.00 USD | 67,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 76,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 122,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `493.50` | 143.61 USD | 122,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 1,040.00 USD | 123,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `533.50` | 177.66 USD | 123,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 124,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `565.50` | 1,450.00 USD | 126,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `95.50` | 469,030.00 USD | 0.00 USD | 920.05 USD | `-66.90%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 468,110.00 USD | 0.00 USD | 6,240.00 USD | `-64.82%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 461,870.00 USD | 0.00 USD | 4,080.00 USD | `-64.47%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 457,790.00 USD | 0.00 USD | 212.76 USD | `-62.05%` | `1,943,000,000.00` |
| `Live` | `Long` | `116.50` | 457,580.00 USD | 0.00 USD | 171.25 USD | `-59.62%` | `1,470,000,000.00` |
| `Live` | `Long` | `118.50` | 457,410.00 USD | 0.00 USD | 212.35 USD | `-58.93%` | `1,792,000,000.00` |
| `Live` | `Long` | `119.50` | 457,190.00 USD | 0.00 USD | 52,660.00 USD | `-58.58%` | `440,704,000,000.00` |
| `Live` | `Long` | `122.50` | 404,530.00 USD | 0.00 USD | 124.46 USD | `-57.54%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 404,410.00 USD | 0.00 USD | 658.18 USD | `-56.15%` | `5,203,000,000.00` |
| `Live` | `Long` | `138.50` | 403,750.00 USD | 0.00 USD | 2,080.00 USD | `-51.99%` | `15,000,000,000.00` |
| `Live` | `Long` | `146.50` | 401,670.00 USD | 0.00 USD | 7,330.00 USD | `-49.22%` | `50,000,000,000.00` |
| `Live` | `Long` | `147.50` | 394,350.00 USD | 0.00 USD | 895.47 USD | `-48.88%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 393,450.00 USD | 0.00 USD | 1,270.00 USD | `-48.53%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 392,180.00 USD | 0.00 USD | 2,370.00 USD | `-48.18%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 389,820.00 USD | 0.00 USD | 303.78 USD | `-47.14%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 389,510.00 USD | 0.00 USD | 325.00 USD | `-43.68%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 389,190.00 USD | 0.00 USD | 285.75 USD | `-41.94%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 388,900.00 USD | 0.00 USD | 1,090.00 USD | `-40.90%` | `6,397,000,000.00` |
| `Live` | `Long` | `174.50` | 387,810.00 USD | 0.00 USD | 169.96 USD | `-39.52%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 387,640.00 USD | 0.00 USD | 516.67 USD | `-39.17%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 387,130.00 USD | 0.00 USD | 373.83 USD | `-38.82%` | `2,118,000,000.00` |
| `Live` | `Long` | `180.50` | 386,750.00 USD | 0.00 USD | 5,690.00 USD | `-37.44%` | `31,500,000,000.00` |
| `Live` | `Long` | `183.50` | 381,070.00 USD | 0.00 USD | 191.57 USD | `-36.40%` | `1,044,000,000.00` |
| `Live` | `Long` | `184.50` | 380,870.00 USD | 0.00 USD | 616.05 USD | `-36.05%` | `3,339,000,000.00` |
| `Live` | `Long` | `187.50` | 380,260.00 USD | 0.00 USD | 562.50 USD | `-35.01%` | `3,000,000,000.00` |
| `Live` | `Long` | `188.50` | 379,700.00 USD | 0.00 USD | 418.28 USD | `-34.66%` | `2,219,000,000.00` |
| `Live` | `Long` | `191.50` | 379,280.00 USD | 0.00 USD | 1,230.00 USD | `-33.62%` | `6,413,000,000.00` |
| `Live` | `Long` | `192.50` | 378,050.00 USD | 0.00 USD | 1,490.00 USD | `-33.28%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 376,560.00 USD | 0.00 USD | 859.22 USD | `-32.24%` | `4,395,000,000.00` |
| `Live` | `Long` | `199.50` | 375,710.00 USD | 0.00 USD | 765.08 USD | `-30.85%` | `3,835,000,000.00` |
| `Live` | `Long` | `200.50` | 374,940.00 USD | 0.00 USD | 293.13 USD | `-30.51%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 374,650.00 USD | 0.00 USD | 583.61 USD | `-29.81%` | `2,882,000,000.00` |
| `Live` | `Long` | `204.50` | 374,060.00 USD | 0.00 USD | 39,880.00 USD | `-29.12%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 334,180.00 USD | 0.00 USD | 781.11 USD | `-28.77%` | `3,801,000,000.00` |
| `Live` | `Long` | `210.50` | 333,400.00 USD | 0.00 USD | 964.93 USD | `-27.04%` | `4,584,000,000.00` |
| `Live` | `Long` | `213.50` | 332,430.00 USD | 0.00 USD | 3,800.00 USD | `-26.00%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 328,630.00 USD | 0.00 USD | 347.60 USD | `-25.31%` | `1,613,000,000.00` |
| `Live` | `Long` | `220.50` | 328,280.00 USD | 0.00 USD | 6,260.00 USD | `-23.57%` | `28,395,000,000.00` |
| `Live` | `Long` | `221.50` | 322,020.00 USD | 0.00 USD | 1,640.00 USD | `-23.23%` | `7,388,000,000.00` |
| `Live` | `Long` | `223.50` | 320,390.00 USD | 0.00 USD | 32,860.00 USD | `-22.53%` | `147,023,000,000.00` |
| `Live` | `Long` | `225.50` | 287,530.00 USD | 0.00 USD | 613.13 USD | `-21.84%` | `2,719,000,000.00` |
| `Live` | `Long` | `226.50` | 286,910.00 USD | 0.00 USD | 1,240.00 USD | `-21.49%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 285,680.00 USD | 0.00 USD | 174.49 USD | `-21.15%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 285,500.00 USD | 0.00 USD | 642.77 USD | `-20.80%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 284,860.00 USD | 0.00 USD | 1,190.00 USD | `-20.45%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 283,670.00 USD | 0.00 USD | 295.86 USD | `-19.76%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 283,380.00 USD | 0.00 USD | 429.66 USD | `-19.41%` | `1,848,000,000.00` |
| `Live` | `Long` | `234.50` | 282,950.00 USD | 0.00 USD | 217.85 USD | `-18.72%` | `929,000,000.00` |
| `Live` | `Long` | `237.50` | 282,730.00 USD | 0.00 USD | 1,490.00 USD | `-17.68%` | `6,274,000,000.00` |
| `Live` | `Long` | `239.50` | 281,240.00 USD | 0.00 USD | 1,030.00 USD | `-16.99%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 280,210.00 USD | 0.00 USD | 367.32 USD | `-16.29%` | `1,521,000,000.00` |
| `Live` | `Long` | `243.50` | 279,850.00 USD | 0.00 USD | 1,200.00 USD | `-15.60%` | `4,937,000,000.00` |
| `Live` | `Long` | `244.50` | 278,640.00 USD | 0.00 USD | 4,220.00 USD | `-15.25%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 274,420.00 USD | 0.00 USD | 6,740.00 USD | `-14.91%` | `27,435,000,000.00` |
| `Live` | `Long` | `246.50` | 267,690.00 USD | 0.00 USD | 49,300.00 USD | `-14.56%` | `200,000,000,000.00` |
| `Live` | `Long` | `247.50` | 218,390.00 USD | 0.00 USD | 699.44 USD | `-14.21%` | `2,826,000,000.00` |
| `Live` | `Long` | `249.50` | 217,690.00 USD | 0.00 USD | 8,700.00 USD | `-13.52%` | `34,884,000,000.00` |
| `Live` | `Long` | `250.50` | 208,980.00 USD | 0.00 USD | 1,330.00 USD | `-13.17%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 207,660.00 USD | 0.00 USD | 268.35 USD | `-12.83%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 207,390.00 USD | 0.00 USD | 1,030.00 USD | `-12.48%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 206,360.00 USD | 0.00 USD | 362.92 USD | `-11.79%` | `1,426,000,000.00` |
| `Live` | `Long` | `256.50` | 205,990.00 USD | 0.00 USD | 2,480.00 USD | `-11.09%` | `9,686,000,000.00` |
| `Live` | `Long` | `257.50` | 203,510.00 USD | 0.00 USD | 14,580.00 USD | `-10.75%` | `56,622,000,000.00` |
| `Live` | `Long` | `258.50` | 188,930.00 USD | 0.00 USD | 176.56 USD | `-10.40%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 188,750.00 USD | 0.00 USD | 3,860.00 USD | `-9.71%` | `14,816,000,000.00` |
| `Live` | `Long` | `264.50` | 184,890.00 USD | 0.00 USD | 280.37 USD | `-8.32%` | `1,060,000,000.00` |
| `Live` | `Long` | `265.50` | 184,610.00 USD | 0.00 USD | 121,910.00 USD | `-7.98%` | `459,161,000,000.00` |
| `Live` | `Long` | `266.50` | 62,700.00 USD | 0.00 USD | 15,210.00 USD | `-7.63%` | `57,069,000,000.00` |
| `Live` | `Long` | `267.50` | 47,500.00 USD | 0.00 USD | 684.00 USD | `-7.28%` | `2,557,000,000.00` |
| `Live` | `Long` | `268.50` | 46,810.00 USD | 0.00 USD | 7,020.00 USD | `-6.94%` | `26,129,000,000.00` |
| `Live` | `Long` | `269.50` | 39,800.00 USD | 0.00 USD | 37,920.00 USD | `-6.59%` | `140,689,000,000.00` |
| `Live` | `Long` | `271.50` | 1,880.00 USD | 0.00 USD | 1,110.00 USD | `-5.90%` | `4,078,000,000.00` |
| `Live` | `Long` | `274.50` | 773.38 USD | 0.00 USD | 567.94 USD | `-4.86%` | `2,069,000,000.00` |
| `Live` | `Long` | `276.50` | 205.44 USD | 0.00 USD | 205.44 USD | `-4.16%` | `743,000,000.00` |
| `Live` | `Short` | `299.50` | 628.05 USD | 628.05 USD | 0.00 USD | `+3.81%` | `2,097,000,000.00` |
| `Live` | `Short` | `301.50` | 2,610.00 USD | 1,980.00 USD | 0.00 USD | `+4.50%` | `6,571,000,000.00` |
| `Live` | `Short` | `303.50` | 2,950.00 USD | 336.58 USD | 0.00 USD | `+5.20%` | `1,109,000,000.00` |
| `Live` | `Short` | `310.50` | 3,460.00 USD | 517.91 USD | 0.00 USD | `+7.62%` | `1,668,000,000.00` |
| `Live` | `Short` | `311.50` | 4,000.00 USD | 539.21 USD | 0.00 USD | `+7.97%` | `1,731,000,000.00` |
| `Live` | `Short` | `316.50` | 10,540.00 USD | 6,540.00 USD | 0.00 USD | `+9.70%` | `20,668,000,000.00` |
| `Live` | `Short` | `318.50` | 10,660.00 USD | 114.34 USD | 0.00 USD | `+10.39%` | `359,000,000.00` |
| `Live` | `Short` | `320.50` | 11,770.00 USD | 1,110.00 USD | 0.00 USD | `+11.09%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 12,040.00 USD | 276.63 USD | 0.00 USD | `+14.55%` | `837,000,000.00` |
| `Live` | `Short` | `339.50` | 13,400.00 USD | 1,360.00 USD | 0.00 USD | `+17.67%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 14,410.00 USD | 1,010.00 USD | 0.00 USD | `+24.26%` | `2,812,000,000.00` |
| `Live` | `Short` | `361.50` | 54,170.00 USD | 39,770.00 USD | 0.00 USD | `+25.30%` | `110,000,000,000.00` |
| `Live` | `Short` | `368.50` | 54,620.00 USD | 445.52 USD | 0.00 USD | `+27.73%` | `1,209,000,000.00` |
| `Live` | `Short` | `395.50` | 58,050.00 USD | 3,430.00 USD | 0.00 USD | `+37.08%` | `8,681,000,000.00` |
| `Live` | `Short` | `427.50` | 67,530.00 USD | 9,480.00 USD | 0.00 USD | `+48.18%` | `22,172,000,000.00` |
| `Live` | `Short` | `432.50` | 76,340.00 USD | 8,810.00 USD | 0.00 USD | `+49.91%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 122,590.00 USD | 46,250.00 USD | 0.00 USD | `+59.27%` | `100,662,000,000.00` |
| `Live` | `Short` | `493.50` | 122,740.00 USD | 143.61 USD | 0.00 USD | `+71.05%` | `291,000,000.00` |
| `Live` | `Short` | `498.50` | 123,780.00 USD | 1,040.00 USD | 0.00 USD | `+72.78%` | `2,093,000,000.00` |
| `Live` | `Short` | `533.50` | 123,960.00 USD | 177.66 USD | 0.00 USD | `+84.92%` | `333,000,000.00` |
| `Live` | `Short` | `560.50` | 124,800.00 USD | 842.43 USD | 0.00 USD | `+94.27%` | `1,503,000,000.00` |
| `Live` | `Short` | `565.50` | 126,250.00 USD | 1,450.00 USD | 0.00 USD | `+96.01%` | `2,572,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 334,910.00 USD | 0.00 USD | 210.94 USD | `-50.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 334,690.00 USD | 0.00 USD | 2,070.00 USD | `-49.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 332,630.00 USD | 0.00 USD | 2,530.00 USD | `-38.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 330,100.00 USD | 0.00 USD | 490.59 USD | `-36.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 329,610.00 USD | 0.00 USD | 482.01 USD | `-31.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 329,130.00 USD | 0.00 USD | 189.07 USD | `-30.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 328,940.00 USD | 0.00 USD | 441.60 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 328,500.00 USD | 0.00 USD | 703.49 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 327,790.00 USD | 0.00 USD | 638.36 USD | `-23.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 327,150.00 USD | 0.00 USD | 740.85 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 326,410.00 USD | 0.00 USD | 1,050.00 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 325,360.00 USD | 0.00 USD | 389.48 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 324,970.00 USD | 0.00 USD | 220.64 USD | `-17.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 324,750.00 USD | 0.00 USD | 429.30 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 324,320.00 USD | 0.00 USD | 296.50 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 324,030.00 USD | 0.00 USD | 216.45 USD | `-16.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 323,810.00 USD | 0.00 USD | 101.61 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 323,710.00 USD | 0.00 USD | 366.75 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 323,340.00 USD | 0.00 USD | 1,630.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 321,720.00 USD | 0.00 USD | 2,940.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 318,770.00 USD | 0.00 USD | 4,560.00 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 314,220.00 USD | 0.00 USD | 7,080.00 USD | `-12.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 307,140.00 USD | 0.00 USD | 231.54 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 306,910.00 USD | 0.00 USD | 109.26 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 306,800.00 USD | 0.00 USD | 1,780.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 305,020.00 USD | 0.00 USD | 51,300.00 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 253,720.00 USD | 0.00 USD | 250.81 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 253,470.00 USD | 0.00 USD | 707.78 USD | `-9.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 252,760.00 USD | 0.00 USD | 857.85 USD | `-9.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 251,900.00 USD | 0.00 USD | 7,790.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 244,110.00 USD | 0.00 USD | 122.99 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 243,990.00 USD | 0.00 USD | 455.86 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 243,530.00 USD | 0.00 USD | 10,490.00 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 233,040.00 USD | 0.00 USD | 1,110.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 231,940.00 USD | 0.00 USD | 877.46 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 231,060.00 USD | 0.00 USD | 498.04 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 230,560.00 USD | 0.00 USD | 24,640.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 205,920.00 USD | 0.00 USD | 269.60 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 205,650.00 USD | 0.00 USD | 13,500.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 192,160.00 USD | 0.00 USD | 1,470.00 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 190,690.00 USD | 0.00 USD | 336.54 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 190,350.00 USD | 0.00 USD | 299.74 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 190,050.00 USD | 0.00 USD | 903.60 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 189,150.00 USD | 0.00 USD | 384.34 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 188,760.00 USD | 0.00 USD | 125.88 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 188,640.00 USD | 0.00 USD | 21,990.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 166,650.00 USD | 0.00 USD | 3,370.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 163,280.00 USD | 0.00 USD | 2,880.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 160,400.00 USD | 0.00 USD | 135,500.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 24,900.00 USD | 0.00 USD | 8,040.00 USD | `-1.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 16,860.00 USD | 0.00 USD | 3,690.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 13,170.00 USD | 0.00 USD | 7,690.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,480.00 USD | 0.00 USD | 5,080.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `287.50` | 400.62 USD | 0.00 USD | 280.02 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `288.50` | 120.59 USD | 0.00 USD | 120.59 USD | `-0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 153.44 USD | 153.44 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,470.00 USD | 1,320.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 1,590.00 USD | 115.73 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 2,000.00 USD | 409.21 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 20,250.00 USD | 18,250.00 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 20,650.00 USD | 407.88 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 93,100.00 USD | 72,450.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 93,680.00 USD | 581.14 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 94,070.00 USD | 388.95 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 103,760.00 USD | 9,690.00 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 114,820.00 USD | 11,060.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 117,470.00 USD | 2,650.00 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 118,530.00 USD | 1,060.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 118,630.00 USD | 102.73 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 133,130.00 USD | 14,500.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 133,760.00 USD | 634.04 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `312.50` | 134,080.00 USD | 317.19 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 135,110.00 USD | 1,030.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 140,760.00 USD | 5,650.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 140,880.00 USD | 118.85 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 141,410.00 USD | 534.59 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 141,740.00 USD | 321.50 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 206,660.00 USD | 64,920.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 207,750.00 USD | 1,090.00 USD | 0.00 USD | `+15.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 208,290.00 USD | 547.52 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 208,430.00 USD | 138.20 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 208,690.00 USD | 257.45 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 208,860.00 USD | 174.25 USD | 0.00 USD | `+20.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 209,020.00 USD | 151.50 USD | 0.00 USD | `+21.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 210,470.00 USD | 1,450.00 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 212,240.00 USD | 1,770.00 USD | 0.00 USD | `+24.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 212,570.00 USD | 326.07 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 213,400.00 USD | 826.60 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `364.50` | 217,120.00 USD | 3,730.00 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 224,570.00 USD | 7,440.00 USD | 0.00 USD | `+26.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 225,250.00 USD | 682.84 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 226,350.00 USD | 1,100.00 USD | 0.00 USD | `+32.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 227,030.00 USD | 683.96 USD | 0.00 USD | `+37.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 227,230.00 USD | 199.75 USD | 0.00 USD | `+38.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 230,730.00 USD | 3,500.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 231,770.00 USD | 1,040.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 232,150.00 USD | 376.71 USD | 0.00 USD | `+40.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 420,790.00 USD | 188,640.00 USD | 0.00 USD | `+42.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 426,690.00 USD | 5,900.00 USD | 0.00 USD | `+44.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 427,590.00 USD | 901.21 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 429,300.00 USD | 1,700.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 430,850.00 USD | 1,550.00 USD | 0.00 USD | `+49.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 432,230.00 USD | 1,380.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 432,850.00 USD | 621.14 USD | 0.00 USD | `+51.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 436,230.00 USD | 3,380.00 USD | 0.00 USD | `+52.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 436,450.00 USD | 222.75 USD | 0.00 USD | `+54.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 442,050.00 USD | 5,590.00 USD | 0.00 USD | `+56.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 447,960.00 USD | 5,920.00 USD | 0.00 USD | `+56.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 449,090.00 USD | 1,130.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 456,730.00 USD | 7,630.00 USD | 0.00 USD | `+67.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 555,200.00 USD | 98,470.00 USD | 0.00 USD | `+68.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 556,190.00 USD | 981.00 USD | 0.00 USD | `+70.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 556,680.00 USD | 499.50 USD | 0.00 USD | `+73.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,440,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+73.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,440,000.00 USD | 1,000.00 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,450,000.00 USD | 1,040.00 USD | 0.00 USD | `+79.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,450,000.00 USD | 340.67 USD | 0.00 USD | `+81.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,450,000.00 USD | 638.86 USD | 0.00 USD | `+92.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `575.50` | 2,450,000.00 USD | 2,590.00 USD | 0.00 USD | `+99.47%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `248.50` | 18,330,000.00 USD | 0.00 USD | 18,330,000.00 USD | 34,780.00 USD | 12,870.00 USD | 32,000.00 USD |
| `7D` | `248.90` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 14,600.00 USD | 14,030.00 USD | 7,060.00 USD |
| `7D` | `249.30` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD |
| `7D` | `249.70` | 18,170,000.00 USD | 0.00 USD | 18,170,000.00 USD | 50,470.00 USD | 27,880.00 USD | 14,350.00 USD |
| `7D` | `250.10` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 45,440.00 USD | 14,600.00 USD | 26,320.00 USD |
| `7D` | `250.50` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 9,050.00 USD | 52,190.00 USD | 13,790.00 USD |
| `7D` | `250.90` | 17,910,000.00 USD | 0.00 USD | 17,910,000.00 USD | 25,590.00 USD | 15,360.00 USD | 13,860.00 USD |
| `7D` | `251.30` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 32,380.00 USD | 72,300.00 USD | 14,680.00 USD |
| `7D` | `251.70` | 17,740,000.00 USD | 0.00 USD | 17,740,000.00 USD | 57,590.00 USD | 62,360.00 USD | 37,660.00 USD |
| `7D` | `252.10` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 62,800.00 USD | 22,760.00 USD | 29,620.00 USD |
| `7D` | `252.50` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 54,060.00 USD | 28,380.00 USD | 17,700.00 USD |
| `7D` | `252.90` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 13,480.00 USD | 20,850.00 USD | 7.06 USD |
| `7D` | `253.30` | 17,330,000.00 USD | 0.00 USD | 17,330,000.00 USD | 30,240.00 USD | 36,380.00 USD | 26,800.00 USD |
| `7D` | `253.70` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 4,870.00 USD | 29,070.00 USD | 28,090.00 USD |
| `7D` | `254.10` | 17,170,000.00 USD | 0.00 USD | 17,170,000.00 USD | 28,730.00 USD | 36,890.00 USD | 21,950.00 USD |
| `7D` | `254.50` | 17,090,000.00 USD | 0.00 USD | 17,090,000.00 USD | 32,120.00 USD | 13,170.00 USD | 16,390.00 USD |
| `7D` | `254.90` | 17,020,000.00 USD | 0.00 USD | 17,020,000.00 USD | 14,160.00 USD | 6,220.00 USD | 5,620.00 USD |
| `7D` | `255.30` | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 55,960.00 USD | 10,820.00 USD | 42,030.00 USD |
| `7D` | `255.70` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 19,690.00 USD | 13,040.00 USD | 49,760.00 USD |
| `7D` | `256.10` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 53,510.00 USD | 24,220.00 USD | 14,220.00 USD |
| `7D` | `256.50` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 36,010.00 USD | 15,160.00 USD | 27,710.00 USD |
| `7D` | `256.90` | 16,640,000.00 USD | 0.00 USD | 16,640,000.00 USD | 45,670.00 USD | 13,800.00 USD | 31,440.00 USD |
| `1D` | `257.30` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 4,240.00 USD | 638.00 USD | 11,750.00 USD |
| `7D` | `257.30` | 16,550,000.00 USD | 0.00 USD | 16,550,000.00 USD | 23,000.00 USD | 2,970.00 USD | 27,310.00 USD |
| `1D` | `257.70` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `257.70` | 16,490,000.00 USD | 0.00 USD | 16,490,000.00 USD | 46,990.00 USD | 7,280.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 32.50 USD | 4,120.00 USD | 19,390.00 USD |
| `7D` | `258.10` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 72,040.00 USD | 39,480.00 USD | 30,750.00 USD |
| `1D` | `258.50` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 3,360.00 USD | 5,260.00 USD | 45.78 USD |
| `7D` | `258.50` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 109,750.00 USD | 15,650.00 USD | 21,020.00 USD |
| `1D` | `258.90` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 396.65 USD | 8,890.00 USD | 10,710.00 USD |
| `7D` | `258.90` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 20,250.00 USD | 10,000.00 USD | 34,360.00 USD |
| `1D` | `259.30` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 15,050.00 USD | 4,190.00 USD | 20,140.00 USD |
| `7D` | `259.30` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 3,650.00 USD | 36,950.00 USD | 8,050.00 USD |
| `1D` | `259.70` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 14,700.00 USD | 19,050.00 USD | 24,230.00 USD |
| `7D` | `259.70` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 17,070.00 USD | 11,440.00 USD | 84.33 USD |
| `1D` | `260.10` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 8,090.00 USD | 9,630.00 USD | 16,750.00 USD |
| `7D` | `260.10` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 23,940.00 USD | 8,740.00 USD | 8,910.00 USD |
| `1D` | `260.50` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 2,850.00 USD | 8,760.00 USD | 10,400.00 USD |
| `7D` | `260.50` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 6,310.00 USD | 31,320.00 USD | 22,370.00 USD |
| `1D` | `260.90` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD |
| `7D` | `260.90` | 15,890,000.00 USD | 0.00 USD | 15,890,000.00 USD | 17,580.00 USD | 30,210.00 USD | 37,880.00 USD |
| `1D` | `261.30` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 8,660.00 USD | 16,360.00 USD | 500.69 USD |
| `7D` | `261.30` | 15,800,000.00 USD | 0.00 USD | 15,800,000.00 USD | 1,980.00 USD | 33,580.00 USD | 15,970.00 USD |
| `1D` | `261.70` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD |
| `7D` | `261.70` | 15,750,000.00 USD | 0.00 USD | 15,750,000.00 USD | 24,930.00 USD | 48,920.00 USD | 19,910.00 USD |
| `1D` | `262.10` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 517.32 USD | 4,790.00 USD | 16,510.00 USD |
| `7D` | `262.10` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 60,340.00 USD | 36,740.00 USD | 32,860.00 USD |
| `1D` | `262.50` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD |
| `7D` | `262.50` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 36,340.00 USD | 26,170.00 USD | 24.52 USD |
| `1D` | `262.90` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD |
| `7D` | `262.90` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 66,900.00 USD | 32,740.00 USD | 32,750.00 USD |
| `1D` | `263.30` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD |
| `7D` | `263.30` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 31,720.00 USD | 23,840.00 USD | 39,100.00 USD |
| `1D` | `263.70` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD |
| `7D` | `263.70` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 265,940.00 USD | 104,900.00 USD | 27,030.00 USD |
| `1D` | `264.10` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD |
| `7D` | `264.10` | 14,840,000.00 USD | 0.00 USD | 14,840,000.00 USD | 93,540.00 USD | 27,860.00 USD | 41,920.00 USD |
| `1D` | `264.50` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD |
| `7D` | `264.50` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 49,620.00 USD | 14,050.00 USD | 37,310.00 USD |
| `1D` | `264.90` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,630.00 USD |
| `7D` | `264.90` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 22,920.00 USD | 73,550.00 USD | 16,060.00 USD |
| `1D` | `265.30` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 19,790.00 USD | 8,590.00 USD | 33,450.00 USD |
| `7D` | `265.30` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 111,680.00 USD | 47,310.00 USD | 103,160.00 USD |
| `1D` | `265.70` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 23,810.00 USD | 23,390.00 USD | 33,670.00 USD |
| `7D` | `265.70` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 54,220.00 USD | 73,540.00 USD | 46,110.00 USD |
| `1D` | `266.10` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 10,200.00 USD | 87.00 USD | 7.04 USD |
| `7D` | `266.10` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 156,170.00 USD | 143,870.00 USD | 57,440.00 USD |
| `1D` | `266.50` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 27,700.00 USD | 3,060.00 USD | 8,720.00 USD |
| `7D` | `266.50` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 112,390.00 USD | 71,680.00 USD | 105,340.00 USD |
| `1D` | `266.90` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 32,360.00 USD | 6,530.00 USD | 6,770.00 USD |
| `7D` | `266.90` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 138,720.00 USD | 163,270.00 USD | 59,230.00 USD |
| `1D` | `267.30` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 17,990.00 USD | 11,130.00 USD | 3,350.00 USD |
| `7D` | `267.30` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 112,800.00 USD | 156,840.00 USD | 88,780.00 USD |
| `1D` | `267.70` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 83,350.00 USD | 112,170.00 USD | 14,410.00 USD |
| `7D` | `267.70` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 171,250.00 USD | 207,730.00 USD | 62,750.00 USD |
| `1D` | `268.10` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 55,330.00 USD | 80,080.00 USD | 47,150.00 USD |
| `7D` | `268.10` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 108,270.00 USD | 282,540.00 USD | 99,590.00 USD |
| `1D` | `268.50` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 57,220.00 USD | 101,650.00 USD | 31,670.00 USD |
| `7D` | `268.50` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 200,320.00 USD | 140,160.00 USD | 76,210.00 USD |
| `1D` | `268.90` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 92,000.00 USD | 36,340.00 USD | 41,690.00 USD |
| `7D` | `268.90` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 199,940.00 USD | 107,670.00 USD | 92,150.00 USD |
| `1D` | `269.30` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 28,630.00 USD | 16,320.00 USD | 20,850.00 USD |
| `7D` | `269.30` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 280,160.00 USD | 180,610.00 USD | 85,010.00 USD |
| `1D` | `269.70` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 39,120.00 USD | 24,350.00 USD | 8,620.00 USD |
| `7D` | `269.70` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 55,620.00 USD | 85,320.00 USD | 10,360.00 USD |
| `1D` | `270.10` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 97,380.00 USD | 77,420.00 USD | 98,140.00 USD |
| `7D` | `270.10` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 143,830.00 USD | 169,870.00 USD | 98,670.00 USD |
| `1D` | `270.50` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 71,720.00 USD | 36,250.00 USD | 36,810.00 USD |
| `7D` | `270.50` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 79,840.00 USD | 97,680.00 USD | 214,710.00 USD |
| `1D` | `270.90` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 11,770.00 USD | 23,900.00 USD | 66,890.00 USD |
| `7D` | `270.90` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 275,900.00 USD | 146,080.00 USD | 90,020.00 USD |
| `1D` | `271.30` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 56,610.00 USD | 46,080.00 USD | 72,980.00 USD |
| `7D` | `271.30` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 128,290.00 USD | 123,510.00 USD | 39,340.00 USD |
| `1D` | `271.70` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 20,370.00 USD | 13,810.00 USD | 6,920.00 USD |
| `7D` | `271.70` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 379,860.00 USD | 48,230.00 USD | 77,320.00 USD |
| `1D` | `272.10` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 109,050.00 USD | 33,030.00 USD | 17,450.00 USD |
| `7D` | `272.10` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 257,880.00 USD | 75,270.00 USD | 148,590.00 USD |
| `1D` | `272.50` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 73,010.00 USD | 24,680.00 USD | 24,790.00 USD |
| `7D` | `272.50` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 157,320.00 USD | 167,310.00 USD | 31,120.00 USD |
| `1D` | `272.90` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 79,800.00 USD | 57,810.00 USD | 6,760.00 USD |
| `7D` | `272.90` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 151,480.00 USD | 204,700.00 USD | 83,580.00 USD |
| `1D` | `273.30` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 179,910.00 USD | 204,070.00 USD | 35,220.00 USD |
| `7D` | `273.30` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD |
| `1D` | `273.70` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 142,100.00 USD | 172,390.00 USD | 94,170.00 USD |
| `7D` | `273.70` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 195,450.00 USD | 467,490.00 USD | 205,950.00 USD |
| `1D` | `274.10` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 113,450.00 USD | 203,210.00 USD | 71,890.00 USD |
| `7D` | `274.10` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 455,510.00 USD | 216,600.00 USD | 178,150.00 USD |
| `1D` | `274.50` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 195,280.00 USD | 71,370.00 USD | 104,190.00 USD |
| `7D` | `274.50` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 345,450.00 USD | 165,770.00 USD | 94,420.00 USD |
| `1D` | `274.90` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 57,970.00 USD | 35,940.00 USD | 53,710.00 USD |
| `7D` | `274.90` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 260,340.00 USD | 168,220.00 USD | 90,910.00 USD |
| `1D` | `275.30` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD |
| `7D` | `275.30` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,390.00 USD |
| `1D` | `275.70` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 17,100.00 USD | 37,310.00 USD | 8,730.00 USD |
| `7D` | `275.70` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 1,350.00 USD | 51,050.00 USD | 11.36 USD |
| `1D` | `276.10` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 85,030.00 USD | 50,210.00 USD | 22,040.00 USD |
| `7D` | `276.10` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 35,490.00 USD | 31,830.00 USD | 22,370.00 USD |
| `7D` | `276.50` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 13,620.00 USD | 26,230.00 USD | 31,120.00 USD |
| `7D` | `276.90` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 45,560.00 USD | 22,950.00 USD | 19,830.00 USD |
| `1D` | `277.30` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 36,000.00 USD | 66,900.00 USD | 59,760.00 USD |
| `7D` | `277.30` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD |
| `1D` | `277.70` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 57,640.00 USD | 47,660.00 USD | 23,950.00 USD |
| `7D` | `277.70` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 27,190.00 USD | 84,350.00 USD |
| `1D` | `278.10` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD |
| `7D` | `278.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 24,750.00 USD | 0.00 USD | 59,500.00 USD |
| `1D` | `278.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 67,950.00 USD | 33,500.00 USD | 29,220.00 USD |
| `7D` | `278.50` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD |
| `1D` | `278.90` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 24,100.00 USD | 27,270.00 USD | 10,340.00 USD |
| `7D` | `278.90` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 42,950.00 USD | 31,760.00 USD | 17,140.00 USD |
| `1D` | `279.30` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 53,390.00 USD | 33,630.00 USD | 44,020.00 USD |
| `7D` | `279.30` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD |
| `1D` | `279.70` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 20,320.00 USD | 0.00 USD | 13,960.00 USD |
| `7D` | `279.70` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 46,800.00 USD | 0.00 USD | 54,370.00 USD |
| `1D` | `280.10` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD |
| `1D` | `280.50` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD |
| `1D` | `280.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 4,860.00 USD | 21,660.00 USD |
| `7D` | `280.90` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD |
| `1D` | `281.30` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.30` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.70` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 19,210.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `281.70` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 76,000.00 USD | 43,170.00 USD | 226,010.00 USD |
| `7D` | `282.10` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD |
| `1D` | `282.50` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 5,740.00 USD | 24,390.00 USD | 43,160.00 USD |
| `7D` | `282.50` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 32,190.00 USD | 0.00 USD | 39,740.00 USD |
| `1D` | `282.90` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 52,960.00 USD | 54,510.00 USD | 98,300.00 USD |
| `7D` | `282.90` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 117.84 USD |
| `1D` | `283.30` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 18,430.00 USD | 0.00 USD | 112,590.00 USD |
| `7D` | `283.30` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 37,310.00 USD | 89,370.00 USD |
| `1D` | `283.70` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 30,480.00 USD | 51,990.00 USD |
| `7D` | `283.70` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD |
| `1D` | `284.10` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD |
| `7D` | `284.10` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `284.50` | 976,660.00 USD | 0.00 USD | 976,660.00 USD | 39,670.00 USD | 70,600.00 USD | 20,690.00 USD |
| `7D` | `284.50` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,150.00 USD |
| `1D` | `284.90` | 845,700.00 USD | 0.00 USD | 845,700.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD |
| `7D` | `284.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD |
| `1D` | `285.30` | 816,590.00 USD | 0.00 USD | 816,590.00 USD | 20,960.00 USD | 64,640.00 USD | 93,680.00 USD |
| `7D` | `285.30` | 906,630.00 USD | 0.00 USD | 906,630.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD |
| `1D` | `285.70` | 637,310.00 USD | 0.00 USD | 637,310.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD |
| `7D` | `285.70` | 616,790.00 USD | 0.00 USD | 616,790.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD |
| `1D` | `286.10` | 474,690.00 USD | 0.00 USD | 474,690.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `7D` | `286.10` | 503,160.00 USD | 0.00 USD | 503,160.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD |
| `1D` | `286.50` | 444,680.00 USD | 0.00 USD | 444,680.00 USD | 111,830.00 USD | 0.00 USD | 37,510.00 USD |
| `7D` | `286.50` | 428,310.00 USD | 0.00 USD | 428,310.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 295,340.00 USD | 0.00 USD | 295,340.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD |
| `7D` | `286.90` | 308,870.00 USD | 0.00 USD | 308,870.00 USD | 27,530.00 USD | 141,160.00 USD | 0.00 USD |
| `1D` | `287.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `287.30` | 101,950.00 USD | 101,950.00 USD | 0.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD |
| `7D` | `287.30` | 140,180.00 USD | 0.00 USD | 140,180.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD |
| `7D` | `287.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `287.70` | 154,260.00 USD | 154,260.00 USD | 0.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD |
| `7D` | `288.10` | 293,550.00 USD | 293,550.00 USD | 0.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD |
| `1D` | `289.30` | 113,950.00 USD | 113,950.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.70` | 294,480.00 USD | 294,480.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `7D` | `290.10` | 295,420.00 USD | 295,420.00 USD | 0.00 USD | 0.00 USD | 947.00 USD | 0.00 USD |
| `1D` | `290.90` | 113,950.00 USD | 113,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.40 USD |
| `1D` | `291.30` | 123,900.00 USD | 123,900.00 USD | 0.00 USD | 0.00 USD | 9,950.00 USD | 7.76 USD |
| `7D` | `291.30` | 305,520.00 USD | 305,520.00 USD | 0.00 USD | 0.00 USD | 10,100.00 USD | 0.00 USD |
| `1D` | `291.70` | 161,680.00 USD | 161,680.00 USD | 0.00 USD | 0.00 USD | 15,650.00 USD | 22,120.00 USD |
| `7D` | `291.70` | 398,750.00 USD | 398,750.00 USD | 0.00 USD | 0.00 USD | 93,220.00 USD | 0.00 USD |
| `1D` | `292.10` | 196,500.00 USD | 196,500.00 USD | 0.00 USD | 0.00 USD | 34,810.00 USD | 9.06 USD |
| `7D` | `292.10` | 517,590.00 USD | 517,590.00 USD | 0.00 USD | 0.00 USD | 118,820.00 USD | 18.90 USD |
| `1D` | `292.50` | 243,870.00 USD | 243,870.00 USD | 0.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD |
| `7D` | `292.50` | 543,470.00 USD | 543,470.00 USD | 0.00 USD | 0.00 USD | 25,780.00 USD | 103.56 USD |
| `1D` | `292.90` | 335,980.00 USD | 335,980.00 USD | 0.00 USD | 10,870.00 USD | 81,240.00 USD | 3.04 USD |
| `7D` | `292.90` | 663,560.00 USD | 663,560.00 USD | 0.00 USD | 0.00 USD | 120,030.00 USD | 68.92 USD |
| `1D` | `293.30` | 402,690.00 USD | 402,690.00 USD | 0.00 USD | 6,120.00 USD | 60,590.00 USD | 1.58 USD |
| `7D` | `293.30` | 777,370.00 USD | 777,370.00 USD | 0.00 USD | 534.50 USD | 113,250.00 USD | 22.43 USD |
| `1D` | `293.70` | 653,770.00 USD | 653,770.00 USD | 0.00 USD | 88,260.00 USD | 63,150.00 USD | 99,670.00 USD |
| `7D` | `293.70` | 815,050.00 USD | 815,050.00 USD | 0.00 USD | 37,280.00 USD | 346.50 USD | 54.81 USD |
| `1D` | `294.10` | 795,300.00 USD | 795,300.00 USD | 0.00 USD | 36,530.00 USD | 47,290.00 USD | 57,700.00 USD |
| `7D` | `294.10` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 85,150.00 USD | 32,540.00 USD | 105,680.00 USD |
| `1D` | `294.50` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 129,200.00 USD | 98,900.00 USD | 95,200.00 USD |
| `7D` | `294.50` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 69,950.00 USD | 14,450.00 USD | 30.22 USD |
| `1D` | `294.90` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 53,910.00 USD | 79,400.00 USD | 105,170.00 USD |
| `7D` | `294.90` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 63,470.00 USD | 88,260.00 USD | 104,880.00 USD |
| `1D` | `295.30` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 86,610.00 USD | 69,170.00 USD | 63,240.00 USD |
| `7D` | `295.30` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 45,590.00 USD | 65,470.00 USD | 252,180.00 USD |
| `1D` | `295.70` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD |
| `7D` | `295.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 105,410.00 USD | 71,570.00 USD | 133,250.00 USD |
| `1D` | `296.10` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 90,530.00 USD | 115,020.00 USD | 29,580.00 USD |
| `7D` | `296.10` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 75,740.00 USD | 90,370.00 USD | 119,220.00 USD |
| `1D` | `296.50` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 43,030.00 USD | 34,820.00 USD | 20,610.00 USD |
| `7D` | `296.50` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 1,060.00 USD | 78,480.00 USD | 57,020.00 USD |
| `1D` | `296.90` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 22,010.00 USD | 21,080.00 USD | 91,120.00 USD |
| `7D` | `296.90` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 206,840.00 USD | 56,070.00 USD | 134,620.00 USD |
| `1D` | `297.30` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD |
| `7D` | `297.30` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 3,960.00 USD | 443.90 USD | 5.22 USD |
| `1D` | `297.70` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 807.94 USD | 723.06 USD | 12,060.00 USD |
| `7D` | `297.70` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 144.38 USD | 58,490.00 USD | 34,680.00 USD |
| `1D` | `298.10` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 44,470.00 USD | 6,340.00 USD | 52,940.00 USD |
| `7D` | `298.10` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 49,240.00 USD | 82,010.00 USD | 54,850.00 USD |
| `1D` | `298.50` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 7,150.00 USD | 21,100.00 USD | 84,740.00 USD |
| `7D` | `298.50` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 16,080.00 USD | 48,060.00 USD |
| `1D` | `298.90` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 27,510.00 USD | 15,820.00 USD | 115,940.00 USD |
| `7D` | `298.90` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 70,090.00 USD | 1,940.00 USD | 40,000.00 USD |
| `1D` | `299.30` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 33,660.00 USD | 16,690.00 USD | 27,850.00 USD |
| `7D` | `299.30` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 2,570.00 USD | 2,980.00 USD | 45,900.00 USD |
| `1D` | `299.70` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 12,530.00 USD | 22,710.00 USD | 34,030.00 USD |
| `7D` | `299.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 5,310.00 USD | 9,400.00 USD | 19,850.00 USD |
| `1D` | `300.10` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 51,990.00 USD | 44,400.00 USD | 58,110.00 USD |
| `7D` | `300.10` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 51,500.00 USD | 2,420.00 USD | 58.36 USD |
| `1D` | `300.50` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 18,720.00 USD | 10,730.00 USD | 41,890.00 USD |
| `7D` | `300.50` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 866.20 USD | 36,110.00 USD | 19,760.00 USD |
| `1D` | `300.90` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 12,920.00 USD | 32,430.00 USD | 36,720.00 USD |
| `7D` | `300.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 24,730.00 USD | 35,210.00 USD | 84,450.00 USD |
| `1D` | `301.30` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 34,050.00 USD | 46,940.00 USD | 28,550.00 USD |
| `7D` | `301.30` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 71,140.00 USD | 56,660.00 USD | 94,690.00 USD |
| `1D` | `301.70` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 31,740.00 USD | 20,020.00 USD | 16,730.00 USD |
| `7D` | `301.70` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 37,640.00 USD | 133,050.00 USD | 106.53 USD |
| `1D` | `302.10` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 44,760.00 USD | 37,150.00 USD | 10,340.00 USD |
| `7D` | `302.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 53,220.00 USD | 122,660.00 USD | 26,250.00 USD |
| `1D` | `302.50` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 10,520.00 USD | 20,620.00 USD | 31,130.00 USD |
| `7D` | `302.50` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 31,330.00 USD | 103,660.00 USD | 41,720.00 USD |
| `1D` | `302.90` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,230.00 USD | 1,910.00 USD | 20,480.00 USD |
| `7D` | `302.90` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 40,380.00 USD | 63,830.00 USD | 90.12 USD |
| `1D` | `303.30` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 31,930.00 USD | 299.52 USD | 14,640.00 USD |
| `7D` | `303.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 2,170.00 USD | 96.05 USD |
| `1D` | `303.70` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD |
| `7D` | `303.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 17,370.00 USD | 11,960.00 USD | 24,680.00 USD |
| `1D` | `304.10` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 22,560.00 USD | 981.10 USD | 53,800.00 USD |
| `7D` | `304.10` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 5,440.00 USD | 855.36 USD | 122.16 USD |
| `1D` | `304.50` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 13,310.00 USD | 9,590.00 USD | 53,870.00 USD |
| `7D` | `304.50` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 3,480.00 USD | 11,660.00 USD | 111.47 USD |
| `1D` | `304.90` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 697.80 USD | 146.63 USD | 2.91 USD |
| `7D` | `304.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 34,680.00 USD | 19,830.00 USD | 8,370.00 USD |
| `1D` | `305.30` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 11,260.00 USD | 0.00 USD | 2,010.00 USD |
| `7D` | `305.30` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 162,420.00 USD | 128,830.00 USD | 117,040.00 USD |
| `1D` | `305.70` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 7,960.00 USD | 1,830.00 USD | 3,410.00 USD |
| `7D` | `305.70` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 82,270.00 USD | 14,420.00 USD | 12,700.00 USD |
| `1D` | `306.10` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 4,210.00 USD | 2,780.00 USD | 1,350.00 USD |
| `7D` | `306.10` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 22,930.00 USD | 67,530.00 USD | 46,130.00 USD |
| `1D` | `306.50` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 4,550.00 USD | 9,500.00 USD | 58.13 USD |
| `7D` | `306.50` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 30,150.00 USD | 40,640.00 USD | 65,840.00 USD |
| `1D` | `306.90` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 32,120.00 USD | 40,250.00 USD | 13,060.00 USD |
| `7D` | `306.90` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 58,810.00 USD | 50,710.00 USD | 57,640.00 USD |
| `1D` | `307.30` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 7,930.00 USD | 34,600.00 USD | 10,930.00 USD |
| `7D` | `307.30` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 34,320.00 USD | 124,020.00 USD | 83,200.00 USD |
| `1D` | `307.70` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 19,670.00 USD | 28,030.00 USD | 9,610.00 USD |
| `7D` | `307.70` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 84,930.00 USD | 73,620.00 USD | 23,980.00 USD |
| `1D` | `308.10` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD |
| `7D` | `308.10` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 105,700.00 USD | 62,570.00 USD | 106,890.00 USD |
| `1D` | `308.50` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 5,570.00 USD | 3,510.00 USD | 4,260.00 USD |
| `7D` | `308.50` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 118,090.00 USD | 65,810.00 USD | 65,520.00 USD |
| `1D` | `308.90` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 12,710.00 USD | 6,030.00 USD | 4,140.00 USD |
| `7D` | `308.90` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 60,660.00 USD | 32,520.00 USD | 19,790.00 USD |
| `1D` | `309.30` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD |
| `7D` | `309.30` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 27,920.00 USD | 25,880.00 USD | 36,580.00 USD |
| `1D` | `309.70` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD |
| `7D` | `309.70` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 40,410.00 USD | 132,640.00 USD | 153,310.00 USD |
| `1D` | `310.10` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 4,390.00 USD | 4,770.00 USD | 0.00 USD |
| `7D` | `310.10` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 34,250.00 USD | 63,210.00 USD | 62,830.00 USD |
| `1D` | `310.50` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD |
| `7D` | `310.50` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 68,560.00 USD | 73,910.00 USD | 22,000.00 USD |
| `1D` | `310.90` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.31 USD |
| `7D` | `310.90` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 35,670.00 USD | 31,060.00 USD | 3,900.00 USD |
| `1D` | `311.30` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `311.30` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 84,180.00 USD | 64,750.00 USD | 47,650.00 USD |
| `1D` | `311.70` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 9,900.00 USD | 6,590.00 USD | 4.14 USD |
| `7D` | `311.70` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 34,040.00 USD | 11,260.00 USD | 31,800.00 USD |
| `1D` | `312.10` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 244.00 USD | 39.75 USD | 0.00 USD |
| `7D` | `312.10` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 46,850.00 USD | 246.55 USD | 24,210.00 USD |
| `1D` | `312.50` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD |
| `7D` | `312.50` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 19,540.00 USD | 23,400.00 USD | 49,770.00 USD |
| `1D` | `312.90` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD |
| `7D` | `312.90` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 22,600.00 USD | 18,280.00 USD | 30,100.00 USD |
| `1D` | `313.30` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 64,910.00 USD | 30,310.00 USD | 22,660.00 USD |
| `1D` | `313.70` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `313.70` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 32,170.00 USD | 14,450.00 USD | 23,120.00 USD |
| `1D` | `314.10` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.10` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 26,810.00 USD | 2,090.00 USD | 47,790.00 USD |
| `1D` | `314.50` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 4,240.00 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `314.50` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 48,630.00 USD | 258.00 USD | 24,540.00 USD |
| `1D` | `314.90` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `314.90` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 29,590.00 USD | 289.95 USD | 10,250.00 USD |
| `1D` | `315.30` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 32.50 USD | 144.50 USD | 6,170.00 USD |
| `7D` | `315.30` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | 52.52 USD |
| `1D` | `315.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `315.70` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 9,200.00 USD | 50,710.00 USD | 48,150.00 USD |
| `1D` | `316.10` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 2,100.00 USD | 5,010.00 USD | 10,740.00 USD |
| `7D` | `316.10` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 38,840.00 USD | 19,940.00 USD | 43,420.00 USD |
| `1D` | `316.50` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 235.25 USD | 3,300.00 USD | 0.00 USD |
| `7D` | `316.50` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 16,120.00 USD | 20,380.00 USD | 18,370.00 USD |
| `1D` | `316.90` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 14,650.00 USD | 3,700.00 USD | 20,140.00 USD |
| `7D` | `316.90` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 3,030.00 USD | 10,360.00 USD | 101.25 USD |
| `1D` | `317.30` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 2,250.00 USD | 6,390.00 USD | 7,170.00 USD |
| `7D` | `317.30` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 14,540.00 USD | 854.23 USD | 102.12 USD |
| `1D` | `317.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 18,240.00 USD | 15,360.00 USD | 26,930.00 USD |
| `7D` | `317.70` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 620.15 USD | 894.23 USD | 88.33 USD |
| `1D` | `318.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 2,290.00 USD | 9,270.00 USD | 7,680.00 USD |
| `7D` | `318.10` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 22,250.00 USD | 8,980.00 USD | 142.18 USD |
| `1D` | `318.50` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 4,700.00 USD | 7,500.00 USD | 9,580.00 USD |
| `7D` | `318.50` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 3,010.00 USD | 25,720.00 USD | 36,350.00 USD |
| `1D` | `318.90` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 12,300.00 USD | 8,760.00 USD | 13,930.00 USD |
| `7D` | `318.90` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 10,270.00 USD | 17,970.00 USD | 23,820.00 USD |
| `1D` | `319.30` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 8,310.00 USD | 16,300.00 USD | 488.47 USD |
| `7D` | `319.30` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 19,140.00 USD | 5.68 USD |
| `7D` | `319.70` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `7D` | `320.10` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD |
| `7D` | `320.50` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 15,190.00 USD | 10,420.00 USD | 49.92 USD |
| `7D` | `321.30` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 9,210.00 USD | 8,300.00 USD | 5,950.00 USD |
| `7D` | `321.70` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 4,780.00 USD | 9,440.00 USD | 15,090.00 USD |
| `7D` | `322.10` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 22,940.00 USD | 7,790.00 USD | 6,210.00 USD |
| `7D` | `322.50` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 555.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `322.90` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 16,590.00 USD | 5,630.00 USD | 0.48 USD |
| `7D` | `323.30` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 14,160.00 USD | 6,560.00 USD | 11,480.00 USD |
| `7D` | `323.70` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 269.10 USD | 6,330.00 USD | 0.00 USD |
| `7D` | `324.10` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD |
| `7D` | `324.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `314.91M` | Total OI Tokens: `1,096,449.3 BCH`
  * 1h OI Change: `+0.08%` | 4h OI Change: `+0.90%` | 24h OI Change: `-2.78%`
  * Exchange Breakdown: Binance=`93.73M` | Bybit=`39.94M` | OKX=`24.48M` | Hyperliquid=`8.17M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.14K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0039%` | **USDT OKX** | `-0.0063%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0007%` |
| **USDT MEXC** | `0.0038%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0039%` | **USDT Bitget** | `0.0084%` |
| **CoinM Binance** | `-0.0008%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `41.53%` | `58.47%` | `0.71` | 2,090,000.00 USD |
| `15M` | `Binance` | `48.42%` | `51.58%` | `0.94` | 419,300.00 USD |
| `15M` | `OKX` | `59.61%` | `40.39%` | `1.48` | 220,500.00 USD |
| `15M` | `Bybit` | `50.87%` | `49.13%` | `1.04` | 145,610.00 USD |
| `15M` | `KuCoin` | `50.11%` | `49.89%` | `1.00` | 3,130.00 USD |
| `15M` | `Gate` | `30.24%` | `69.76%` | `0.43` | 390,650.00 USD |
| `15M` | `Bitget` | `45%` | `55%` | `0.82` | 23,990.00 USD |
| `15M` | `BingX` | `41.74%` | `58.26%` | `0.72` | 525,290.00 USD |
| `15M` | `MEXC` | `6.83%` | `93.17%` | `0.07` | 87,050.00 USD |
| `15M` | `Bitunix` | `38.12%` | `61.88%` | `0.62` | 21,540.00 USD |
| `15M` | `Hyperliquid` | `28.54%` | `71.46%` | `0.40` | 30,730.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.09%` | `54.91%` | `0.82` | 25,150.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 178,340.00 USD |
| `15M` | `HTX` | `26.65%` | `73.35%` | `0.36` | 347.90 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 6,700.00 USD |
| `15M` | `Aster` | `20.05%` | `79.95%` | `0.25` | 10,920.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 164.19 USD |
| `15M` | `Whale Positions` | `48.42%` | `51.58%` | `0.94` | 419,300.00 USD |
| `15M` | `Global Accounts` | `41.53%` | `58.47%` | `0.71` | 2,090,000.00 USD |
| `1H` | `BCH` | `50.23%` | `49.77%` | `1.01` | 8,820,000.00 USD |
| `1H` | `Binance` | `55.64%` | `44.36%` | `1.25` | 3,110,000.00 USD |
| `1H` | `OKX` | `60.87%` | `39.13%` | `1.56` | 995,930.00 USD |
| `1H` | `Bybit` | `68.14%` | `31.86%` | `2.14` | 820,640.00 USD |
| `1H` | `KuCoin` | `52.71%` | `47.29%` | `1.11` | 92,410.00 USD |
| `1H` | `Gate` | `44.54%` | `55.46%` | `0.80` | 107,020.00 USD |
| `1H` | `Bitget` | `35.68%` | `64.32%` | `0.55` | 280,930.00 USD |
| `1H` | `BingX` | `47.36%` | `52.64%` | `0.90` | 757,520.00 USD |
| `1H` | `MEXC` | `27.01%` | `72.99%` | `0.37` | 72,200.00 USD |
| `1H` | `Bitunix` | `58.51%` | `41.49%` | `1.41` | 348,680.00 USD |
| `1H` | `Hyperliquid` | `90.06%` | `9.94%` | `9.06` | 49,100.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.6%` | `51.4%` | `0.95` | 1,420,000.00 USD |
| `1H` | `Crypto.com` | `49.98%` | `50.02%` | `1.00` | 23.03 USD |
| `1H` | `WhiteBIT` | `1.39%` | `98.61%` | `0.01` | 747,310.00 USD |
| `1H` | `HTX` | `49.85%` | `50.15%` | `0.99` | 1,840.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `1.9%` | `98.1%` | `0.02` | 8,330.00 USD |
| `1H` | `Aster` | `99.08%` | `0.92%` | `107.70` | 10,780.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `91.22%` | `8.78%` | `10.39` | 926.44 USD |
| `1H` | `Whale Positions` | `55.64%` | `44.36%` | `1.25` | 3,110,000.00 USD |
| `1H` | `Global Accounts` | `50.23%` | `49.77%` | `1.01` | 8,820,000.00 USD |
| `4H` | `BCH` | `46.80%` | `53.20%` | `0.88` | 89,300,000.00 USD |
| `4H` | `Binance` | `47.93%` | `52.07%` | `0.92` | 32,300,000.00 USD |
| `4H` | `OKX` | `49.91%` | `50.09%` | `1.00` | 16,930,000.00 USD |
| `4H` | `Bybit` | `49.76%` | `50.24%` | `0.99` | 8,360,000.00 USD |
| `4H` | `KuCoin` | `49.43%` | `50.57%` | `0.98` | 2,100,000.00 USD |
| `4H` | `Gate` | `48.6%` | `51.4%` | `0.95` | 1,460,000.00 USD |
| `4H` | `Bitget` | `41.09%` | `58.91%` | `0.70` | 2,480,000.00 USD |
| `4H` | `BingX` | `44.8%` | `55.2%` | `0.81` | 2,590,000.00 USD |
| `4H` | `MEXC` | `53.95%` | `46.05%` | `1.17` | 1,530,000.00 USD |
| `4H` | `Bitunix` | `50.28%` | `49.72%` | `1.01` | 2,620,000.00 USD |
| `4H` | `Hyperliquid` | `49.71%` | `50.29%` | `0.99` | 402,770.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.91%` | `50.09%` | `1.00` | 14,510,000.00 USD |
| `4H` | `Crypto.com` | `24.05%` | `75.95%` | `0.32` | 383.65 USD |
| `4H` | `WhiteBIT` | `0.55%` | `99.45%` | `0.01` | 3,470,000.00 USD |
| `4H` | `HTX` | `41.3%` | `58.7%` | `0.70` | 42,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `21.55%` | `78.45%` | `0.27` | 217,570.00 USD |
| `4H` | `Aster` | `30.84%` | `69.16%` | `0.45` | 205,800.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.43%` | `55.57%` | `0.80` | 86,480.00 USD |
| `4H` | `Whale Positions` | `47.93%` | `52.07%` | `0.92` | 32,300,000.00 USD |
| `4H` | `Global Accounts` | `46.80%` | `53.20%` | `0.88` | 89,300,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `290.49` | `289.33` | `290.49` | `291.59` | `287.81` | 1,897,766.44 USD | 827,805.59 USD | 1,069,960.85 USD | -242,155.26 USD | `-12.76%` | `25B / 40S` |
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `288.94` | `289.00` | `289.94` | `288.00` | 1,099,157.40 USD | 660,933.72 USD | 438,223.69 USD | 222,710.03 USD | `+20.26%` | `43B / 33S` |
| `5:00 UTC` | `287.91` | `288.60` | `287.91` | `289.87` | `287.51` | 851,365.60 USD | 435,531.09 USD | 415,834.51 USD | 19,696.57 USD | `+2.31%` | `18B / 22S` |
| `0:00 UTC` | `286.33` | `286.94` | `286.33` | `287.87` | `285.90` | 1,269,041.85 USD | 639,367.56 USD | 629,674.29 USD | 9,693.27 USD | `+0.76%` | `32B / 48S` |
| `5:00 UTC` | `288.00` | `288.25` | `288.00` | `289.13` | `287.22` | 1,082,751.51 USD | 592,384.75 USD | 490,366.75 USD | 102,018.00 USD | `+9.42%` | `41B / 33S` |
| `0:00 UTC` | `288.00` | `287.59` | `288.00` | `288.53` | `286.82` | 774,817.75 USD | 442,366.10 USD | 332,451.65 USD | 109,914.46 USD | `+14.19%` | `38B / 28S` |
| `5:00 UTC` | `289.00` | `288.21` | `289.00` | `289.02` | `287.22` | 505,722.48 USD | 323,366.92 USD | 182,355.56 USD | 141,011.36 USD | `+27.88%` | `60B / 31S` |
| `0:00 UTC` | `288.00` | `287.93` | `288.00` | `288.89` | `287.26` | 386,053.80 USD | 202,478.84 USD | 183,574.96 USD | 18,903.88 USD | `+4.90%` | `41B / 40S` |

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
| `5m` | 2,710.00 USD | 53,380.00 USD | **`ACCUMULATION`** |
| `15m` | -67,110.00 USD | 61,850.00 USD | **`DISTRIBUTION`** |
| `30m` | -53,090.00 USD | 350,140.00 USD | **`ACCUMULATION`** |
| `1h` | -74,620.00 USD | 905,640.00 USD | **`ACCUMULATION`** |
| `2h` | -159,120.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `4h` | -214,570.00 USD | -1,610,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 164,350.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 100,990.00 USD | -7,310.00 USD | **`ACCUMULATION`** |
| `12h` | 345,970.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,010,000.00 USD | -6,870,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 41,240.00 USD | -11,870,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,520,000.00 USD | -136,090,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+2.71K` | 15m=`-67.11K` | 1h=`-74.62K` | 24h=`-1.01M`
* Futures Capital Netflows: 5m=`+53.38K` | 15m=`+61.85K` | 1h=`+905.64K` | 24h=`-6.87M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `273.04` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `285.22`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.68` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.16` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `278.98`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`289.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
