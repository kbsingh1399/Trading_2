# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 00:47:28 IST` (`2026-10-29 19:17:28 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `287.46` | **Live Ask Quote**: `288.04` | **Mid Price**: `287.75`
- **Spread Points**: `580.00` | **Spread BPS**: `20.16 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.72` | VWAP Z-Score: `+1.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.25` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.27` | Lower -3.00σ Band: `270.17`
  * Upper +2.51σ Band: `293.22` | Lower -2.51σ Band: `272.22`
  * Upper +2.01σ Band: `291.13` | Lower -2.01σ Band: `274.32`
  * Upper +2.00σ Band: `291.09` | Lower -2.00σ Band: `274.36`
  * Upper +1.28σ Band: `288.08` | Lower -1.28σ Band: `277.37`
  * Upper +1.00σ Band: `286.91` | Lower -1.00σ Band: `278.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.70` | EMA-20=`286.16` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.92` (Slope: `+0.0000`) | EMA-100=`284.33`
  * Institutional Anchors: EMA-144=`284.76` | EMA-200=`284.67` (Slope: `+0.1721`) | EMA-233=`284.94`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.56` (Distance: `+0.07%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.25%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.06%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `286.60` - `288.90`
  * Optimal Trade Entry (OTE 0.705): `288.33`
  * Structural Invalidation Anchor (0.786): `290.05`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `287.78` | `288.99` | `287.78` | `288.95` | `2,106` | 606,991.25 USD | 21,024.39 USD | `+3.46%` | -2,643,117.77 USD | `+0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `288.96` | `289.13` | `288.13` | `288.17` | `919` | 265,324.44 USD | 5,749.88 USD | `+2.17%` | -2,637,367.90 USD | `-0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `288.16` | `288.53` | `286.82` | `287.42` | `1,204` | 346,155.33 USD | 11,169.59 USD | `+3.23%` | -2,626,198.31 USD | `+0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `287.57` | `287.86` | `285.90` | `287.66` | `4,423` | 1,269,041.85 USD | 9,693.27 USD | `+0.76%` | -2,790,280.58 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `287.65` | `289.13` | `287.21` | `288.17` | `3,756` | 1,082,751.51 USD | 102,018.00 USD | `+9.42%` | -2,688,262.58 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `288.16` | `288.53` | `286.82` | `287.82` | `2,485` | 714,740.62 USD | 106,534.90 USD | `+14.91%` | -2,581,727.67 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.48` | `291.58` | `286.48` | `288.89` | `23,176` | 6,696,574.59 USD | 177,926.21 USD | `+2.66%` | -3,100,524.21 USD | `+0.54` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `288.88` | `289.93` | `285.90` | `288.17` | `14,933` | 4,302,316.36 USD | 354,117.88 USD | `+8.23%` | -2,746,406.33 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.16` | `288.53` | `286.82` | `287.82` | `2,485` | 714,740.62 USD | 106,534.90 USD | `+14.91%` | -2,639,871.43 USD | `+0.39` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `287.81` | `88,426` | 25,585,566.66 USD | -1,651,077.62 USD | `-6.45%` | -2,638,082.02 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `287.81` | `88,426` | 25,585,566.66 USD | -1,651,077.62 USD | `-6.45%` | -2,638,082.02 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`287.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1951` | `0x12d2...f97f` | `LONG` | 1,043,155.19 USD | `3,627,243,000,000.00` | `303.26` | `287.52` | `0.000000` | -56,844.15 USD | `-5.45%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.70` (Vol: 152,600.00 USD, Dist: `+2.58%`) | Long MP=`271.76` (Vol: 166,000.00 USD, Dist: `--5.72%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.13%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--5.69%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+2.13%`) | Long MP=`274.98` (Vol: 169,100.00 USD, Dist: `--4.60%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+2.12%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--8.52%`)
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
| `7D` | `Long Liquidation` | `248.50` | 18,370,000.00 USD | 18,370,000.00 USD | 34,780.00 USD | 11,250.00 USD | 31,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 18,290,000.00 USD | 18,290,000.00 USD | 14,600.00 USD | 15,640.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 18,250,000.00 USD | 18,250,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 8,700.00 USD | 217,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.70` | 18,210,000.00 USD | 18,210,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.10` | 18,120,000.00 USD | 18,120,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.50` | 18,020,000.00 USD | 18,020,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 208,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.90` | 17,940,000.00 USD | 17,940,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 17,890,000.00 USD | 17,890,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 207,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 17,770,000.00 USD | 17,770,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.10` | 17,610,000.00 USD | 17,610,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.50` | 17,500,000.00 USD | 17,500,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 207,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.90` | 17,400,000.00 USD | 17,400,000.00 USD | 13,480.00 USD | 19,580.00 USD | 12.13 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 17,360,000.00 USD | 17,360,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 17,270,000.00 USD | 17,270,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.10` | 17,210,000.00 USD | 17,210,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.50` | 17,120,000.00 USD | 17,120,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 206,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.90` | 17,060,000.00 USD | 17,060,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 17,030,000.00 USD | 17,030,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 16,920,000.00 USD | 16,920,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.10` | 16,840,000.00 USD | 16,840,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.50` | 16,750,000.00 USD | 16,750,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.90` | 16,670,000.00 USD | 16,670,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.10` | 8,100,000.00 USD | 8,100,000.00 USD | 4,210.00 USD | 638.00 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 16,580,000.00 USD | 16,580,000.00 USD | 23,000.00 USD | 1,200.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 8,090,000.00 USD | 8,090,000.00 USD | 32.00 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.70` | 16,530,000.00 USD | 16,530,000.00 USD | 46,990.00 USD | 6,040.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 8,080,000.00 USD | 8,080,000.00 USD | 32.50 USD | 991.50 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.10` | 16,450,000.00 USD | 16,450,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 8,070,000.00 USD | 8,070,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.50` | 16,310,000.00 USD | 16,310,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 8,050,000.00 USD | 8,050,000.00 USD | 7,010.00 USD | 5,060.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 16,170,000.00 USD | 16,170,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 8,020,000.00 USD | 8,020,000.00 USD | 24,070.00 USD | 9,940.00 USD | 14,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 16,110,000.00 USD | 16,110,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 7,970,000.00 USD | 7,970,000.00 USD | 4,620.00 USD | 4,660.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 16,050,000.00 USD | 16,050,000.00 USD | 17,070.00 USD | 13,660.00 USD | 105.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 7,960,000.00 USD | 7,960,000.00 USD | 19,490.00 USD | 17,870.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.10` | 16,020,000.00 USD | 16,020,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 7,890,000.00 USD | 7,890,000.00 USD | 3,100.00 USD | 9,490.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.50` | 15,980,000.00 USD | 15,980,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 7,870,000.00 USD | 7,870,000.00 USD | 5,040.00 USD | 15,080.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 15,920,000.00 USD | 15,920,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 7,830,000.00 USD | 7,830,000.00 USD | 12,720.00 USD | 6,900.00 USD | 6,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 15,840,000.00 USD | 15,840,000.00 USD | 2,490.00 USD | 33,470.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 7,810,000.00 USD | 7,810,000.00 USD | 8,750.00 USD | 14,260.00 USD | 2.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 15,780,000.00 USD | 15,780,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 7,780,000.00 USD | 7,780,000.00 USD | 4,920.00 USD | 4,330.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.10` | 15,690,000.00 USD | 15,690,000.00 USD | 60,340.00 USD | 34,480.00 USD | 32,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 7,760,000.00 USD | 7,760,000.00 USD | 8,640.00 USD | 626.24 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.50` | 15,560,000.00 USD | 15,560,000.00 USD | 36,340.00 USD | 26,590.00 USD | 15.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 7,750,000.00 USD | 7,750,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 15,500,000.00 USD | 15,500,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 7,750,000.00 USD | 7,750,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 15,360,000.00 USD | 15,360,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 7,730,000.00 USD | 7,730,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 15,270,000.00 USD | 15,270,000.00 USD | 265,940.00 USD | 96,750.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 7,700,000.00 USD | 7,700,000.00 USD | 746.44 USD | 825.92 USD | 3.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.10` | 14,880,000.00 USD | 14,880,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 7,700,000.00 USD | 7,700,000.00 USD | 1,860.00 USD | 647.93 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.50` | 14,710,000.00 USD | 14,710,000.00 USD | 49,620.00 USD | 16,400.00 USD | 37,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.70` | 7,700,000.00 USD | 7,700,000.00 USD | 28,300.00 USD | 615.20 USD | 36,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 14,610,000.00 USD | 14,610,000.00 USD | 22,920.00 USD | 75,260.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 7,640,000.00 USD | 7,640,000.00 USD | 20,540.00 USD | 8,870.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 14,490,000.00 USD | 14,490,000.00 USD | 111,680.00 USD | 43,610.00 USD | 103,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 7,590,000.00 USD | 7,590,000.00 USD | 9,760.00 USD | 11,810.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `265.70` | 14,230,000.00 USD | 14,230,000.00 USD | 54,220.00 USD | 77,170.00 USD | 46,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.90` | 7,500,000.00 USD | 7,500,000.00 USD | 14,110.00 USD | 11,850.00 USD | 19.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.10` | 14,060,000.00 USD | 14,060,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 7,480,000.00 USD | 7,480,000.00 USD | 32,850.00 USD | 115.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.50` | 13,700,000.00 USD | 13,700,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.70` | 7,440,000.00 USD | 7,440,000.00 USD | 15,000.00 USD | 3,250.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 13,390,000.00 USD | 13,390,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 7,420,000.00 USD | 7,420,000.00 USD | 28,570.00 USD | 6,640.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 13,030,000.00 USD | 13,030,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 7,370,000.00 USD | 7,370,000.00 USD | 11,820.00 USD | 26,650.00 USD | 22.03 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `267.70` | 12,670,000.00 USD | 12,670,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.90` | 7,330,000.00 USD | 7,330,000.00 USD | 113,380.00 USD | 120,840.00 USD | 45,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.10` | 12,220,000.00 USD | 12,220,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 7,050,000.00 USD | 7,050,000.00 USD | 39,160.00 USD | 98,460.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.50` | 11,730,000.00 USD | 11,730,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.70` | 6,890,000.00 USD | 6,890,000.00 USD | 97,080.00 USD | 85,110.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 11,310,000.00 USD | 11,310,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 6,650,000.00 USD | 6,650,000.00 USD | 50,070.00 USD | 23,000.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 10,910,000.00 USD | 10,910,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 6,560,000.00 USD | 6,560,000.00 USD | 31,770.00 USD | 6,100.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `269.70` | 10,370,000.00 USD | 10,370,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 6,510,000.00 USD | 6,510,000.00 USD | 33,260.00 USD | 43,730.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.10` | 10,210,000.00 USD | 10,210,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 6,420,000.00 USD | 6,420,000.00 USD | 108,170.00 USD | 64,760.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.50` | 9,800,000.00 USD | 9,800,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.70` | 6,120,000.00 USD | 6,120,000.00 USD | 52,010.00 USD | 39,730.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 9,410,000.00 USD | 9,410,000.00 USD | 275,900.00 USD | 144,560.00 USD | 90,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 6,030,000.00 USD | 6,030,000.00 USD | 40,150.00 USD | 33,840.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 8,900,000.00 USD | 8,900,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 5,810,000.00 USD | 5,810,000.00 USD | 28,220.00 USD | 37,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,110.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `271.70` | 8,610,000.00 USD | 8,610,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 5,750,000.00 USD | 5,750,000.00 USD | 93,920.00 USD | 23,950.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.10` | 8,100,000.00 USD | 8,100,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 5,610,000.00 USD | 5,610,000.00 USD | 66,270.00 USD | 9,680.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.50` | 7,620,000.00 USD | 7,620,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 5,520,000.00 USD | 5,520,000.00 USD | 67,730.00 USD | 29,720.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 7,260,000.00 USD | 7,260,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 5,400,000.00 USD | 5,400,000.00 USD | 89,520.00 USD | 82,120.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 6,820,000.00 USD | 6,820,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 5,220,000.00 USD | 5,220,000.00 USD | 225,140.00 USD | 235,170.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 6,140,000.00 USD | 6,140,000.00 USD | 195,450.00 USD | 467,590.00 USD | 205,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 4,670,000.00 USD | 4,670,000.00 USD | 88,320.00 USD | 196,200.00 USD | 53,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.10` | 5,270,000.00 USD | 5,270,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 4,330,000.00 USD | 4,330,000.00 USD | 204,120.00 USD | 170,220.00 USD | 126,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.50` | 4,420,000.00 USD | 4,420,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.70` | 3,830,000.00 USD | 3,830,000.00 USD | 101,740.00 USD | 43,050.00 USD | 53,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 3,810,000.00 USD | 3,810,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 3,630,000.00 USD | 3,630,000.00 USD | 62,250.00 USD | 21,990.00 USD | 44,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 3,290,000.00 USD | 3,290,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 3,500,000.00 USD | 3,500,000.00 USD | 59,520.00 USD | 65,680.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 3,150,000.00 USD | 3,150,000.00 USD | 1,350.00 USD | 51,050.00 USD | 10.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 3,340,000.00 USD | 3,340,000.00 USD | 52,570.00 USD | 51,470.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.10` | 3,100,000.00 USD | 3,100,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 3,210,000.00 USD | 3,210,000.00 USD | 65,640.00 USD | 44,550.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.50` | 3,090,000.00 USD | 3,090,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.70` | 3,100,000.00 USD | 3,100,000.00 USD | 13,620.00 USD | 21,650.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 3,090,000.00 USD | 3,090,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 3,050,000.00 USD | 3,050,000.00 USD | 19,010.00 USD | 64,370.00 USD | 67,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 63,290.00 USD | 116.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 2,900,000.00 USD | 2,900,000.00 USD | 74,620.00 USD | 55,090.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 27,190.00 USD | 84,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 2,750,000.00 USD | 2,750,000.00 USD | 12,650.00 USD | 9,490.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.10` | 2,830,000.00 USD | 2,830,000.00 USD | 24,750.00 USD | 0.00 USD | 59,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 2,710,000.00 USD | 2,710,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.50` | 2,750,000.00 USD | 2,750,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 2,560,000.00 USD | 2,560,000.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.90` | 2,660,000.00 USD | 2,660,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.10` | 2,490,000.00 USD | 2,490,000.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 2,560,000.00 USD | 2,560,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.50` | 2,410,000.00 USD | 2,410,000.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 2,490,000.00 USD | 2,490,000.00 USD | 46,800.00 USD | 0.00 USD | 54,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.90` | 2,340,000.00 USD | 2,340,000.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.30` | 2,300,000.00 USD | 2,300,000.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.50` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.70` | 2,230,000.00 USD | 2,230,000.00 USD | 21,670.00 USD | 4,860.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.10` | 2,140,000.00 USD | 2,140,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.50` | 2,070,000.00 USD | 2,070,000.00 USD | 9,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 2,330,000.00 USD | 2,330,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.90` | 2,060,000.00 USD | 2,060,000.00 USD | 15,000.00 USD | 20,570.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.10` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 133,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.30` | 1,930,000.00 USD | 1,930,000.00 USD | 55,330.00 USD | 22,600.00 USD | 142,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.50` | 2,070,000.00 USD | 2,070,000.00 USD | 32,190.00 USD | 0.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.70` | 1,710,000.00 USD | 1,710,000.00 USD | 5,740.00 USD | 34,190.00 USD | 42,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.90` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 125.24 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.10` | 1,620,000.00 USD | 1,620,000.00 USD | 71,390.00 USD | 44,720.00 USD | 178,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 37,310.00 USD | 89,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.50` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.90` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.10` | 1,630,000.00 USD | 1,630,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.30` | 1,180,000.00 USD | 1,180,000.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.50` | 1,450,000.00 USD | 1,450,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.70` | 1,060,000.00 USD | 1,060,000.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 282,130.00 USD | 65.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.10` | 939,130.00 USD | 939,130.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.30` | 906,700.00 USD | 906,700.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.50` | 835,330.00 USD | 835,330.00 USD | 91,500.00 USD | 95,280.00 USD | 52,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.70` | 616,870.00 USD | 616,870.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.90` | 596,530.00 USD | 596,530.00 USD | 0.00 USD | 42,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.10` | 503,230.00 USD | 503,230.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.30` | 553,690.00 USD | 553,690.00 USD | 20,960.00 USD | 7,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.50` | 428,380.00 USD | 428,380.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.70` | 525,680.00 USD | 525,680.00 USD | 134,800.00 USD | 43,100.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.90` | 308,940.00 USD | 308,940.00 USD | 27,530.00 USD | 141,160.00 USD | 1.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.10` | 266,940.00 USD | 266,940.00 USD | 38,480.00 USD | 136,750.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.30` | 140,260.00 USD | 140,260.00 USD | 53,620.00 USD | 86,570.00 USD | 70.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.50` | 11,010.00 USD | 11,010.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.70` | 154,260.00 USD | 154,260.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.70` | 308,520.00 USD | 308,520.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.10` | 447,810.00 USD | 447,810.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 449,680.00 USD | 449,680.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 0.00 USD | 5.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 458,930.00 USD | 458,930.00 USD | 0.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 33,980.00 USD | 33,980.00 USD | 0.00 USD | 21,970.00 USD | 5.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 553,020.00 USD | 553,020.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 62,020.00 USD | 62,020.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.10` | 671,700.00 USD | 671,700.00 USD | 0.00 USD | 118,660.00 USD | 18.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 124,600.00 USD | 124,600.00 USD | 0.00 USD | 62,570.00 USD | 7.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.50` | 698,420.00 USD | 698,420.00 USD | 0.00 USD | 26,610.00 USD | 118.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 223,220.00 USD | 223,220.00 USD | 606.80 USD | 98,000.00 USD | 9.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 817,010.00 USD | 817,010.00 USD | 0.00 USD | 118,480.00 USD | 117.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 284,740.00 USD | 284,740.00 USD | 10,710.00 USD | 50,810.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 930,110.00 USD | 930,110.00 USD | 534.50 USD | 112,560.00 USD | 6.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 369,610.00 USD | 369,610.00 USD | 14,220.00 USD | 68,500.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 968,630.00 USD | 968,630.00 USD | 37,280.00 USD | 1,170.00 USD | 65.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 559,870.00 USD | 559,870.00 USD | 73,070.00 USD | 31,360.00 USD | 85,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.10` | 1,190,000.00 USD | 1,190,000.00 USD | 85,150.00 USD | 33,590.00 USD | 105,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 742,510.00 USD | 742,510.00 USD | 49,730.00 USD | 74,090.00 USD | 58,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.50` | 1,280,000.00 USD | 1,280,000.00 USD | 69,950.00 USD | 15,030.00 USD | 24.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 1,140,000.00 USD | 1,140,000.00 USD | 133,430.00 USD | 96,720.00 USD | 168,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 1,540,000.00 USD | 1,540,000.00 USD | 63,470.00 USD | 92,770.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 1,310,000.00 USD | 1,310,000.00 USD | 32,330.00 USD | 64,510.00 USD | 73,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 1,900,000.00 USD | 1,900,000.00 USD | 45,590.00 USD | 65,580.00 USD | 252,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 1,590,000.00 USD | 1,590,000.00 USD | 102,280.00 USD | 111,710.00 USD | 68,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 2,210,000.00 USD | 2,210,000.00 USD | 105,410.00 USD | 72,570.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 1,780,000.00 USD | 1,780,000.00 USD | 105,070.00 USD | 43,160.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.10` | 2,500,000.00 USD | 2,500,000.00 USD | 75,740.00 USD | 90,470.00 USD | 119,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 2,010,000.00 USD | 2,010,000.00 USD | 108,090.00 USD | 95,560.00 USD | 27,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.50` | 2,630,000.00 USD | 2,630,000.00 USD | 1,060.00 USD | 77,140.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.70` | 2,140,000.00 USD | 2,140,000.00 USD | 34,010.00 USD | 39,270.00 USD | 62,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 3,030,000.00 USD | 3,030,000.00 USD | 206,840.00 USD | 51,220.00 USD | 134,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 2,240,000.00 USD | 2,240,000.00 USD | 52,650.00 USD | 177.11 USD | 49,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 3,030,000.00 USD | 3,030,000.00 USD | 3,960.00 USD | 2,500.00 USD | 58.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 2,270,000.00 USD | 2,270,000.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 3,130,000.00 USD | 3,130,000.00 USD | 144.38 USD | 56,790.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 2,300,000.00 USD | 2,300,000.00 USD | 1,150.00 USD | 10,040.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.10` | 3,310,000.00 USD | 3,310,000.00 USD | 49,240.00 USD | 80,820.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 2,490,000.00 USD | 2,490,000.00 USD | 44,190.00 USD | 8,520.00 USD | 137,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.50` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 12,660.00 USD | 48,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 2,610,000.00 USD | 2,610,000.00 USD | 29,410.00 USD | 13,250.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 3,480,000.00 USD | 3,480,000.00 USD | 70,090.00 USD | 993.25 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 2,720,000.00 USD | 2,720,000.00 USD | 51,580.00 USD | 24,680.00 USD | 38,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 3,530,000.00 USD | 3,530,000.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 2,820,000.00 USD | 2,820,000.00 USD | 28,240.00 USD | 28,870.00 USD | 38,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 628.05 USD | 628.05 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `299.70` | 3,560,000.00 USD | 3,560,000.00 USD | 5,310.00 USD | 7,720.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 2,890,000.00 USD | 2,890,000.00 USD | 20,860.00 USD | 22,410.00 USD | 27,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.10` | 3,620,000.00 USD | 3,620,000.00 USD | 51,500.00 USD | 2,470.00 USD | 14.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 3,010,000.00 USD | 3,010,000.00 USD | 48,160.00 USD | 32,740.00 USD | 43,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.50` | 3,680,000.00 USD | 3,680,000.00 USD | 866.20 USD | 36,230.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 3,130,000.00 USD | 3,130,000.00 USD | 20,040.00 USD | 37,920.00 USD | 52,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 3,820,000.00 USD | 3,820,000.00 USD | 24,730.00 USD | 34,630.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 3,220,000.00 USD | 3,220,000.00 USD | 35,810.00 USD | 28,690.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 4,040,000.00 USD | 4,040,000.00 USD | 71,140.00 USD | 55,420.00 USD | 94,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 3,320,000.00 USD | 3,320,000.00 USD | 31,870.00 USD | 27,310.00 USD | 44,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 1,980.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `301.70` | 4,210,000.00 USD | 4,210,000.00 USD | 37,640.00 USD | 130,520.00 USD | 37.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 3,420,000.00 USD | 3,420,000.00 USD | 39,870.00 USD | 51,280.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.10` | 4,410,000.00 USD | 4,410,000.00 USD | 53,220.00 USD | 123,390.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 3,450,000.00 USD | 3,450,000.00 USD | 5,320.00 USD | 12,360.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.50` | 4,590,000.00 USD | 4,590,000.00 USD | 31,330.00 USD | 102,200.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 3,510,000.00 USD | 3,510,000.00 USD | 11,520.00 USD | 11,410.00 USD | 41,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 4,690,000.00 USD | 4,690,000.00 USD | 40,380.00 USD | 64,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 3,550,000.00 USD | 3,550,000.00 USD | 20,770.00 USD | 1,360.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 173.09 USD | 220.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 3,570,000.00 USD | 3,570,000.00 USD | 11,460.00 USD | 232.42 USD | 6,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `303.50` | 336.58 USD | 2,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `303.70` | 4,740,000.00 USD | 4,740,000.00 USD | 17,370.00 USD | 8,710.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 3,620,000.00 USD | 3,620,000.00 USD | 29,930.00 USD | 3,900.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.10` | 4,750,000.00 USD | 4,750,000.00 USD | 5,440.00 USD | 1,950.00 USD | 95.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 3,680,000.00 USD | 3,680,000.00 USD | 4,310.00 USD | 5,170.00 USD | 48,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.50` | 4,760,000.00 USD | 4,760,000.00 USD | 3,480.00 USD | 11,110.00 USD | 68.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 3,730,000.00 USD | 3,730,000.00 USD | 9,700.00 USD | 4,920.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 4,830,000.00 USD | 4,830,000.00 USD | 34,680.00 USD | 18,990.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 3,750,000.00 USD | 3,750,000.00 USD | 9,410.00 USD | 236.66 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 5,230,000.00 USD | 5,230,000.00 USD | 162,420.00 USD | 128,450.00 USD | 117,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 3,750,000.00 USD | 3,750,000.00 USD | 4,980.00 USD | 1,820.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 5,350,000.00 USD | 5,350,000.00 USD | 82,270.00 USD | 18,170.00 USD | 17,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 3,770,000.00 USD | 3,770,000.00 USD | 9,360.00 USD | 2,810.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.10` | 5,490,000.00 USD | 5,490,000.00 USD | 22,930.00 USD | 68,220.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 3,780,000.00 USD | 3,780,000.00 USD | 4,260.00 USD | 3,210.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.50` | 5,630,000.00 USD | 5,630,000.00 USD | 30,150.00 USD | 41,830.00 USD | 65,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 3,810,000.00 USD | 3,810,000.00 USD | 4,450.00 USD | 21,850.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 5,790,000.00 USD | 5,790,000.00 USD | 58,810.00 USD | 50,570.00 USD | 57,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 3,900,000.00 USD | 3,900,000.00 USD | 33,050.00 USD | 42,120.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 6,040,000.00 USD | 6,040,000.00 USD | 34,320.00 USD | 123,720.00 USD | 83,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 3,930,000.00 USD | 3,930,000.00 USD | 6,340.00 USD | 22,290.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 6,220,000.00 USD | 6,220,000.00 USD | 84,930.00 USD | 74,370.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 4,020,000.00 USD | 4,020,000.00 USD | 33,320.00 USD | 30,610.00 USD | 21,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.10` | 6,500,000.00 USD | 6,500,000.00 USD | 106,040.00 USD | 63,640.00 USD | 107,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 4,050,000.00 USD | 4,050,000.00 USD | 13,940.00 USD | 7,490.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.50` | 6,740,000.00 USD | 6,740,000.00 USD | 118,090.00 USD | 64,440.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 4,060,000.00 USD | 4,060,000.00 USD | 5,550.00 USD | 387.08 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 6,860,000.00 USD | 6,860,000.00 USD | 60,660.00 USD | 31,940.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 4,080,000.00 USD | 4,080,000.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 6,950,000.00 USD | 6,950,000.00 USD | 27,920.00 USD | 26,240.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 4,120,000.00 USD | 4,120,000.00 USD | 12,390.00 USD | 22,900.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 7,270,000.00 USD | 7,270,000.00 USD | 40,410.00 USD | 132,660.00 USD | 153,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 4,130,000.00 USD | 4,130,000.00 USD | 8,500.00 USD | 2,590.00 USD | 978.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.10` | 7,430,000.00 USD | 7,430,000.00 USD | 34,250.00 USD | 63,360.00 USD | 62,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 4,140,000.00 USD | 4,140,000.00 USD | 232.38 USD | 7,040.00 USD | 2.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.50` | 7,600,000.00 USD | 7,600,000.00 USD | 68,560.00 USD | 73,280.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 3,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.70` | 4,140,000.00 USD | 4,140,000.00 USD | 144.00 USD | 421.81 USD | 2.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 7,670,000.00 USD | 7,670,000.00 USD | 35,670.00 USD | 30,720.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 4,140,000.00 USD | 4,140,000.00 USD | 134.35 USD | 2,050.00 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 7,870,000.00 USD | 7,870,000.00 USD | 84,180.00 USD | 65,480.00 USD | 47,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 4,160,000.00 USD | 4,160,000.00 USD | 7,390.00 USD | 6,590.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `311.50` | 539.21 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `311.70` | 7,940,000.00 USD | 7,940,000.00 USD | 34,040.00 USD | 11,430.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 4,160,000.00 USD | 4,160,000.00 USD | 2,810.00 USD | 0.00 USD | 4.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.10` | 8,010,000.00 USD | 8,010,000.00 USD | 46,850.00 USD | 1,100.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 4,180,000.00 USD | 4,180,000.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.50` | 8,110,000.00 USD | 8,110,000.00 USD | 19,540.00 USD | 22,180.00 USD | 49,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 4,190,000.00 USD | 4,190,000.00 USD | 13,380.00 USD | 2,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 8,180,000.00 USD | 8,180,000.00 USD | 22,600.00 USD | 20,090.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 4,200,000.00 USD | 4,200,000.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 8,300,000.00 USD | 8,300,000.00 USD | 64,910.00 USD | 30,120.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 4,210,000.00 USD | 4,210,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 8,370,000.00 USD | 8,370,000.00 USD | 32,170.00 USD | 15,010.00 USD | 23,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 4,220,000.00 USD | 4,220,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.10` | 8,440,000.00 USD | 8,440,000.00 USD | 26,810.00 USD | 362.37 USD | 47,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.30` | 4,230,000.00 USD | 4,230,000.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.50` | 8,520,000.00 USD | 8,520,000.00 USD | 48,630.00 USD | 307.60 USD | 24,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.70` | 4,240,000.00 USD | 4,240,000.00 USD | 32.00 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 8,560,000.00 USD | 8,560,000.00 USD | 29,590.00 USD | 0.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 4,240,000.00 USD | 4,240,000.00 USD | 32.50 USD | 0.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 8,560,000.00 USD | 8,560,000.00 USD | 5,690.00 USD | 547.95 USD | 4.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 3,270.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 8,670,000.00 USD | 8,670,000.00 USD | 9,200.00 USD | 50,270.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.90` | 4,270,000.00 USD | 4,270,000.00 USD | 3,440.00 USD | 5,260.00 USD | 43.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.10` | 8,770,000.00 USD | 8,770,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.30` | 4,300,000.00 USD | 4,300,000.00 USD | 12,470.00 USD | 5,050.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.50` | 8,830,000.00 USD | 8,830,000.00 USD | 16,120.00 USD | 20,630.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `316.50` | 6,540.00 USD | 10,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `316.70` | 4,340,000.00 USD | 4,340,000.00 USD | 16,490.00 USD | 8,910.00 USD | 14,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 8,840,000.00 USD | 8,840,000.00 USD | 3,030.00 USD | 10,840.00 USD | 42.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.10` | 4,360,000.00 USD | 4,360,000.00 USD | 3,940.00 USD | 4,440.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 8,860,000.00 USD | 8,860,000.00 USD | 14,540.00 USD | 748.91 USD | 125.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.50` | 4,400,000.00 USD | 4,400,000.00 USD | 11,570.00 USD | 14,470.00 USD | 17,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 8,860,000.00 USD | 8,860,000.00 USD | 620.15 USD | 265.17 USD | 118.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.90` | 4,430,000.00 USD | 4,430,000.00 USD | 7,000.00 USD | 9,190.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.10` | 8,890,000.00 USD | 8,890,000.00 USD | 22,250.00 USD | 9,100.00 USD | 183.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.30` | 4,450,000.00 USD | 4,450,000.00 USD | 2,200.00 USD | 8,470.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.50` | 8,950,000.00 USD | 8,950,000.00 USD | 3,010.00 USD | 26,630.00 USD | 36,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 10,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.70` | 4,480,000.00 USD | 4,480,000.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 9,010,000.00 USD | 9,010,000.00 USD | 10,270.00 USD | 17,970.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.10` | 4,500,000.00 USD | 4,500,000.00 USD | 12,470.00 USD | 6,810.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 18,060.00 USD | 36.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.50` | 4,520,000.00 USD | 4,520,000.00 USD | 8,590.00 USD | 10,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 9,040,000.00 USD | 9,040,000.00 USD | 936.82 USD | 12,700.00 USD | 49.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.90` | 4,530,000.00 USD | 4,530,000.00 USD | 4,350.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.10` | 9,110,000.00 USD | 9,110,000.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 4,210.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.50` | 9,140,000.00 USD | 9,140,000.00 USD | 15,190.00 USD | 10,080.00 USD | 18.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 11,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `320.70` | 4,560,000.00 USD | 4,560,000.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.90` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.30` | 9,160,000.00 USD | 9,160,000.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.70` | 9,190,000.00 USD | 9,190,000.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.10` | 9,230,000.00 USD | 9,230,000.00 USD | 22,940.00 USD | 8,290.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.50` | 9,230,000.00 USD | 9,230,000.00 USD | 555.20 USD | 365.55 USD | 0.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 9,250,000.00 USD | 9,250,000.00 USD | 16,590.00 USD | 5,630.00 USD | 53.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.30` | 9,280,000.00 USD | 9,280,000.00 USD | 14,160.00 USD | 5,860.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.70` | 9,290,000.00 USD | 9,290,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.10` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
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
| `7D` | `248.50` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 34,780.00 USD | 11,250.00 USD | 31,990.00 USD |
| `7D` | `248.90` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 14,600.00 USD | 15,640.00 USD | 7,070.00 USD |
| `7D` | `249.30` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD |
| `7D` | `249.70` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD |
| `7D` | `250.10` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,100.00 USD |
| `7D` | `250.50` | 18,020,000.00 USD | 0.00 USD | 18,020,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD |
| `7D` | `250.90` | 17,940,000.00 USD | 0.00 USD | 17,940,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,880.00 USD |
| `7D` | `251.30` | 17,890,000.00 USD | 0.00 USD | 17,890,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,650.00 USD |
| `7D` | `251.70` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD |
| `7D` | `252.10` | 17,610,000.00 USD | 0.00 USD | 17,610,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,660.00 USD |
| `7D` | `252.50` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,710.00 USD |
| `7D` | `252.90` | 17,400,000.00 USD | 0.00 USD | 17,400,000.00 USD | 13,480.00 USD | 19,580.00 USD | 12.13 USD |
| `7D` | `253.30` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,790.00 USD |
| `7D` | `253.70` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,040.00 USD |
| `7D` | `254.10` | 17,210,000.00 USD | 0.00 USD | 17,210,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,950.00 USD |
| `7D` | `254.50` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,430.00 USD |
| `7D` | `254.90` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,620.00 USD |
| `7D` | `255.30` | 17,030,000.00 USD | 0.00 USD | 17,030,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,030.00 USD |
| `7D` | `255.70` | 16,920,000.00 USD | 0.00 USD | 16,920,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,740.00 USD |
| `7D` | `256.10` | 16,840,000.00 USD | 0.00 USD | 16,840,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,190.00 USD |
| `7D` | `256.50` | 16,750,000.00 USD | 0.00 USD | 16,750,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,700.00 USD |
| `7D` | `256.90` | 16,670,000.00 USD | 0.00 USD | 16,670,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,450.00 USD |
| `1D` | `257.10` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 4,210.00 USD | 638.00 USD | 3,430.00 USD |
| `7D` | `257.30` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 23,000.00 USD | 1,200.00 USD | 27,290.00 USD |
| `1D` | `257.50` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 32.00 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `257.70` | 16,530,000.00 USD | 0.00 USD | 16,530,000.00 USD | 46,990.00 USD | 6,040.00 USD | 18,210.00 USD |
| `1D` | `257.90` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 32.50 USD | 991.50 USD | 10,990.00 USD |
| `7D` | `258.10` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,820.00 USD |
| `1D` | `258.30` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `258.50` | 16,310,000.00 USD | 0.00 USD | 16,310,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,960.00 USD |
| `1D` | `258.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 7,010.00 USD | 5,060.00 USD | 11,840.00 USD |
| `7D` | `258.90` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,330.00 USD |
| `1D` | `259.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 24,070.00 USD | 9,940.00 USD | 14,260.00 USD |
| `7D` | `259.30` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,020.00 USD |
| `1D` | `259.50` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 4,620.00 USD | 4,660.00 USD | 8,940.00 USD |
| `7D` | `259.70` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 17,070.00 USD | 13,660.00 USD | 105.03 USD |
| `1D` | `259.90` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 19,490.00 USD | 17,870.00 USD | 26,940.00 USD |
| `7D` | `260.10` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,940.00 USD |
| `1D` | `260.30` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 3,100.00 USD | 9,490.00 USD | 7,690.00 USD |
| `7D` | `260.50` | 15,980,000.00 USD | 0.00 USD | 15,980,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,380.00 USD |
| `1D` | `260.70` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 5,040.00 USD | 15,080.00 USD | 17,340.00 USD |
| `7D` | `260.90` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,880.00 USD |
| `1D` | `261.10` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 12,720.00 USD | 6,900.00 USD | 6,670.00 USD |
| `7D` | `261.30` | 15,840,000.00 USD | 0.00 USD | 15,840,000.00 USD | 2,490.00 USD | 33,470.00 USD | 16,060.00 USD |
| `1D` | `261.50` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 8,750.00 USD | 14,260.00 USD | 2.10 USD |
| `7D` | `261.70` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,910.00 USD |
| `1D` | `261.90` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 4,920.00 USD | 4,330.00 USD | 10,920.00 USD |
| `7D` | `262.10` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 60,340.00 USD | 34,480.00 USD | 32,830.00 USD |
| `1D` | `262.30` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 8,640.00 USD | 626.24 USD | 5,590.00 USD |
| `7D` | `262.50` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 36,340.00 USD | 26,590.00 USD | 15.39 USD |
| `1D` | `262.70` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD |
| `7D` | `262.90` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,730.00 USD |
| `1D` | `263.10` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD |
| `7D` | `263.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,070.00 USD |
| `1D` | `263.50` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD |
| `7D` | `263.70` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 265,940.00 USD | 96,750.00 USD | 27,000.00 USD |
| `1D` | `263.90` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 746.44 USD | 825.92 USD | 3.09 USD |
| `7D` | `264.10` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,900.00 USD |
| `1D` | `264.30` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 1,860.00 USD | 647.93 USD | 9.06 USD |
| `7D` | `264.50` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 49,620.00 USD | 16,400.00 USD | 37,340.00 USD |
| `1D` | `264.70` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 28,300.00 USD | 615.20 USD | 36,610.00 USD |
| `7D` | `264.90` | 14,610,000.00 USD | 0.00 USD | 14,610,000.00 USD | 22,920.00 USD | 75,260.00 USD | 16,070.00 USD |
| `1D` | `265.10` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 20,540.00 USD | 8,870.00 USD | 15,630.00 USD |
| `7D` | `265.30` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 111,680.00 USD | 43,610.00 USD | 103,140.00 USD |
| `1D` | `265.50` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 9,760.00 USD | 11,810.00 USD | 67,100.00 USD |
| `7D` | `265.70` | 14,230,000.00 USD | 0.00 USD | 14,230,000.00 USD | 54,220.00 USD | 77,170.00 USD | 46,130.00 USD |
| `1D` | `265.90` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 14,110.00 USD | 11,850.00 USD | 19.98 USD |
| `7D` | `266.10` | 14,060,000.00 USD | 0.00 USD | 14,060,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,530.00 USD |
| `1D` | `266.30` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 32,850.00 USD | 115.00 USD | 5,010.00 USD |
| `7D` | `266.50` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,150.00 USD |
| `1D` | `266.70` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 15,000.00 USD | 3,250.00 USD | 3,710.00 USD |
| `7D` | `266.90` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,210.00 USD |
| `1D` | `267.10` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 28,570.00 USD | 6,640.00 USD | 10,110.00 USD |
| `7D` | `267.30` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,770.00 USD |
| `1D` | `267.50` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 11,820.00 USD | 26,650.00 USD | 22.03 USD |
| `7D` | `267.70` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,800.00 USD |
| `1D` | `267.90` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 113,380.00 USD | 120,840.00 USD | 45,380.00 USD |
| `7D` | `268.10` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,480.00 USD |
| `1D` | `268.30` | 7,050,000.00 USD | 0.00 USD | 7,050,000.00 USD | 39,160.00 USD | 98,460.00 USD | 26,540.00 USD |
| `7D` | `268.50` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,240.00 USD |
| `1D` | `268.70` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 97,080.00 USD | 85,110.00 USD | 58,760.00 USD |
| `7D` | `268.90` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,100.00 USD |
| `1D` | `269.10` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 50,070.00 USD | 23,000.00 USD | 16,360.00 USD |
| `7D` | `269.30` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,050.00 USD |
| `1D` | `269.50` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 31,770.00 USD | 6,100.00 USD | 8,720.00 USD |
| `7D` | `269.70` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,500.00 USD |
| `1D` | `269.90` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 33,260.00 USD | 43,730.00 USD | 12,980.00 USD |
| `7D` | `270.10` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,580.00 USD |
| `1D` | `270.30` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 108,170.00 USD | 64,760.00 USD | 128,910.00 USD |
| `7D` | `270.50` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,620.00 USD |
| `1D` | `270.70` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 52,010.00 USD | 39,730.00 USD | 1,670.00 USD |
| `7D` | `270.90` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 275,900.00 USD | 144,560.00 USD | 90,090.00 USD |
| `1D` | `271.10` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 40,150.00 USD | 33,840.00 USD | 139,870.00 USD |
| `7D` | `271.30` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD |
| `1D` | `271.50` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 28,220.00 USD | 37,290.00 USD | 0.00 USD |
| `7D` | `271.70` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,220.00 USD |
| `1D` | `271.90` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 93,920.00 USD | 23,950.00 USD | 16,940.00 USD |
| `7D` | `272.10` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,630.00 USD |
| `1D` | `272.30` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 66,270.00 USD | 9,680.00 USD | 17,040.00 USD |
| `7D` | `272.50` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,230.00 USD |
| `1D` | `272.70` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 67,730.00 USD | 29,720.00 USD | 21,910.00 USD |
| `7D` | `272.90` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,520.00 USD |
| `1D` | `273.10` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 89,520.00 USD | 82,120.00 USD | 6,990.00 USD |
| `7D` | `273.30` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD |
| `1D` | `273.50` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 225,140.00 USD | 235,170.00 USD | 90,150.00 USD |
| `7D` | `273.70` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 195,450.00 USD | 467,590.00 USD | 205,880.00 USD |
| `1D` | `273.90` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 88,320.00 USD | 196,200.00 USD | 53,020.00 USD |
| `7D` | `274.10` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,060.00 USD |
| `1D` | `274.30` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 204,120.00 USD | 170,220.00 USD | 126,080.00 USD |
| `7D` | `274.50` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,520.00 USD |
| `1D` | `274.70` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 101,740.00 USD | 43,050.00 USD | 53,520.00 USD |
| `7D` | `274.90` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,910.00 USD |
| `1D` | `275.10` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 62,250.00 USD | 21,990.00 USD | 44,880.00 USD |
| `7D` | `275.30` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,400.00 USD |
| `1D` | `275.50` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 59,520.00 USD | 65,680.00 USD | 39,110.00 USD |
| `7D` | `275.70` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 1,350.00 USD | 51,050.00 USD | 10.44 USD |
| `1D` | `275.90` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 52,570.00 USD | 51,470.00 USD | 22,040.00 USD |
| `7D` | `276.10` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.30` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 65,640.00 USD | 44,550.00 USD | 3,230.00 USD |
| `7D` | `276.50` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.70` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 13,620.00 USD | 21,650.00 USD | 14,660.00 USD |
| `7D` | `276.90` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,880.00 USD |
| `1D` | `277.10` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 19,010.00 USD | 64,370.00 USD | 67,920.00 USD |
| `7D` | `277.30` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 63,290.00 USD | 116.78 USD |
| `1D` | `277.50` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 74,620.00 USD | 55,090.00 USD | 17,160.00 USD |
| `7D` | `277.70` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 27,190.00 USD | 84,320.00 USD |
| `1D` | `277.90` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 12,650.00 USD | 9,490.00 USD | 23,940.00 USD |
| `7D` | `278.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 24,750.00 USD | 0.00 USD | 59,540.00 USD |
| `1D` | `278.30` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD |
| `7D` | `278.50` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD |
| `1D` | `278.70` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD |
| `7D` | `278.90` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,090.00 USD |
| `1D` | `279.10` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD |
| `7D` | `279.30` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD |
| `1D` | `279.50` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD |
| `7D` | `279.70` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 46,800.00 USD | 0.00 USD | 54,420.00 USD |
| `1D` | `279.90` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD |
| `1D` | `280.30` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD |
| `7D` | `280.50` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD |
| `1D` | `280.70` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 21,670.00 USD | 4,860.00 USD | 64,530.00 USD |
| `1D` | `281.10` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.30` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.50` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 9,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `281.70` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `281.90` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 15,000.00 USD | 20,570.00 USD | 94,830.00 USD |
| `7D` | `282.10` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 133,700.00 USD |
| `1D` | `282.30` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 55,330.00 USD | 22,600.00 USD | 142,200.00 USD |
| `7D` | `282.50` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 32,190.00 USD | 0.00 USD | 39,660.00 USD |
| `1D` | `282.70` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 5,740.00 USD | 34,190.00 USD | 42,610.00 USD |
| `7D` | `282.90` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 125.24 USD |
| `1D` | `283.10` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 71,390.00 USD | 44,720.00 USD | 178,950.00 USD |
| `7D` | `283.30` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 37,310.00 USD | 89,360.00 USD |
| `1D` | `283.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 80,840.00 USD |
| `7D` | `283.70` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD |
| `1D` | `283.90` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD |
| `7D` | `284.10` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `284.30` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD |
| `7D` | `284.50` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,160.00 USD |
| `1D` | `284.70` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD |
| `7D` | `284.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 282,130.00 USD | 65.52 USD |
| `1D` | `285.10` | 939,130.00 USD | 0.00 USD | 939,130.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD |
| `7D` | `285.30` | 906,700.00 USD | 0.00 USD | 906,700.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD |
| `1D` | `285.50` | 835,330.00 USD | 0.00 USD | 835,330.00 USD | 91,500.00 USD | 95,280.00 USD | 52,020.00 USD |
| `7D` | `285.70` | 616,870.00 USD | 0.00 USD | 616,870.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD |
| `1D` | `285.90` | 596,530.00 USD | 0.00 USD | 596,530.00 USD | 0.00 USD | 42,840.00 USD | 0.00 USD |
| `7D` | `286.10` | 503,230.00 USD | 0.00 USD | 503,230.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD |
| `1D` | `286.30` | 553,690.00 USD | 0.00 USD | 553,690.00 USD | 20,960.00 USD | 7,060.00 USD | 0.00 USD |
| `7D` | `286.50` | 428,380.00 USD | 0.00 USD | 428,380.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD |
| `1D` | `286.70` | 525,680.00 USD | 0.00 USD | 525,680.00 USD | 134,800.00 USD | 43,100.00 USD | 80,840.00 USD |
| `7D` | `286.90` | 308,940.00 USD | 0.00 USD | 308,940.00 USD | 27,530.00 USD | 141,160.00 USD | 1.44 USD |
| `1D` | `287.10` | 266,940.00 USD | 0.00 USD | 266,940.00 USD | 38,480.00 USD | 136,750.00 USD | 80,690.00 USD |
| `7D` | `287.30` | 140,260.00 USD | 0.00 USD | 140,260.00 USD | 53,620.00 USD | 86,570.00 USD | 70.92 USD |
| `1D` | `287.50` | 11,010.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD |
| `1D` | `287.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `287.70` | 154,260.00 USD | 154,260.00 USD | 0.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD |
| `7D` | `287.70` | 308,520.00 USD | 308,520.00 USD | 0.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD |
| `7D` | `288.10` | 447,810.00 USD | 447,810.00 USD | 0.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD |
| `1D` | `289.10` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.70` | 449,680.00 USD | 449,680.00 USD | 0.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD |
| `1D` | `291.10` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.82 USD |
| `7D` | `291.30` | 458,930.00 USD | 458,930.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `291.50` | 33,980.00 USD | 33,980.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD | 5.34 USD |
| `7D` | `291.70` | 553,020.00 USD | 553,020.00 USD | 0.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD |
| `1D` | `291.90` | 62,020.00 USD | 62,020.00 USD | 0.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD |
| `7D` | `292.10` | 671,700.00 USD | 671,700.00 USD | 0.00 USD | 0.00 USD | 118,660.00 USD | 18.90 USD |
| `1D` | `292.30` | 124,600.00 USD | 124,600.00 USD | 0.00 USD | 0.00 USD | 62,570.00 USD | 7.00 USD |
| `7D` | `292.50` | 698,420.00 USD | 698,420.00 USD | 0.00 USD | 0.00 USD | 26,610.00 USD | 118.54 USD |
| `1D` | `292.70` | 223,220.00 USD | 223,220.00 USD | 0.00 USD | 606.80 USD | 98,000.00 USD | 9.69 USD |
| `7D` | `292.90` | 817,010.00 USD | 817,010.00 USD | 0.00 USD | 0.00 USD | 118,480.00 USD | 117.39 USD |
| `1D` | `293.10` | 284,740.00 USD | 284,740.00 USD | 0.00 USD | 10,710.00 USD | 50,810.00 USD | 0.42 USD |
| `7D` | `293.30` | 930,110.00 USD | 930,110.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 6.64 USD |
| `1D` | `293.50` | 369,610.00 USD | 369,610.00 USD | 0.00 USD | 14,220.00 USD | 68,500.00 USD | 2,150.00 USD |
| `7D` | `293.70` | 968,630.00 USD | 968,630.00 USD | 0.00 USD | 37,280.00 USD | 1,170.00 USD | 65.98 USD |
| `1D` | `293.90` | 559,870.00 USD | 559,870.00 USD | 0.00 USD | 73,070.00 USD | 31,360.00 USD | 85,820.00 USD |
| `7D` | `294.10` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 85,150.00 USD | 33,590.00 USD | 105,650.00 USD |
| `1D` | `294.30` | 742,510.00 USD | 742,510.00 USD | 0.00 USD | 49,730.00 USD | 74,090.00 USD | 58,830.00 USD |
| `7D` | `294.50` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 69,950.00 USD | 15,030.00 USD | 24.48 USD |
| `1D` | `294.70` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 133,430.00 USD | 96,720.00 USD | 168,940.00 USD |
| `7D` | `294.90` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 63,470.00 USD | 92,770.00 USD | 104,870.00 USD |
| `1D` | `295.10` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 32,330.00 USD | 64,510.00 USD | 73,420.00 USD |
| `7D` | `295.30` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 45,590.00 USD | 65,580.00 USD | 252,150.00 USD |
| `1D` | `295.50` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 102,280.00 USD | 111,710.00 USD | 68,310.00 USD |
| `7D` | `295.70` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 105,410.00 USD | 72,570.00 USD | 133,230.00 USD |
| `1D` | `295.90` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 105,070.00 USD | 43,160.00 USD | 33,310.00 USD |
| `7D` | `296.10` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 75,740.00 USD | 90,470.00 USD | 119,120.00 USD |
| `1D` | `296.30` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 108,090.00 USD | 95,560.00 USD | 27,150.00 USD |
| `7D` | `296.50` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 1,060.00 USD | 77,140.00 USD | 57,080.00 USD |
| `1D` | `296.70` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 34,010.00 USD | 39,270.00 USD | 62,260.00 USD |
| `7D` | `296.90` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 206,840.00 USD | 51,220.00 USD | 134,640.00 USD |
| `1D` | `297.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 52,650.00 USD | 177.11 USD | 49,450.00 USD |
| `7D` | `297.30` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 3,960.00 USD | 2,500.00 USD | 58.25 USD |
| `1D` | `297.50` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD |
| `7D` | `297.70` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 144.38 USD | 56,790.00 USD | 34,690.00 USD |
| `1D` | `297.90` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 1,150.00 USD | 10,040.00 USD | 12,060.00 USD |
| `7D` | `298.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 49,240.00 USD | 80,820.00 USD | 54,850.00 USD |
| `1D` | `298.30` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 44,190.00 USD | 8,520.00 USD | 137,660.00 USD |
| `7D` | `298.50` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 12,660.00 USD | 48,100.00 USD |
| `1D` | `298.70` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 29,410.00 USD | 13,250.00 USD | 80,710.00 USD |
| `7D` | `298.90` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 70,090.00 USD | 993.25 USD | 39,930.00 USD |
| `1D` | `299.10` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 51,580.00 USD | 24,680.00 USD | 38,000.00 USD |
| `7D` | `299.30` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD |
| `1D` | `299.50` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 28,240.00 USD | 28,870.00 USD | 38,520.00 USD |
| `7D` | `299.70` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 5,310.00 USD | 7,720.00 USD | 19,830.00 USD |
| `1D` | `299.90` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 20,860.00 USD | 22,410.00 USD | 27,470.00 USD |
| `7D` | `300.10` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 51,500.00 USD | 2,470.00 USD | 14.59 USD |
| `1D` | `300.30` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 48,160.00 USD | 32,740.00 USD | 43,720.00 USD |
| `7D` | `300.50` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 866.20 USD | 36,230.00 USD | 19,740.00 USD |
| `1D` | `300.70` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 20,040.00 USD | 37,920.00 USD | 52,600.00 USD |
| `7D` | `300.90` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 24,730.00 USD | 34,630.00 USD | 84,370.00 USD |
| `1D` | `301.10` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 35,810.00 USD | 28,690.00 USD | 26,010.00 USD |
| `7D` | `301.30` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 71,140.00 USD | 55,420.00 USD | 94,870.00 USD |
| `1D` | `301.50` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 31,870.00 USD | 27,310.00 USD | 44,030.00 USD |
| `7D` | `301.70` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 37,640.00 USD | 130,520.00 USD | 37.85 USD |
| `1D` | `301.90` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 39,870.00 USD | 51,280.00 USD | 11,590.00 USD |
| `7D` | `302.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 53,220.00 USD | 123,390.00 USD | 26,240.00 USD |
| `1D` | `302.30` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 5,320.00 USD | 12,360.00 USD | 10,300.00 USD |
| `7D` | `302.50` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 31,330.00 USD | 102,200.00 USD | 41,630.00 USD |
| `1D` | `302.70` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 11,520.00 USD | 11,410.00 USD | 41,280.00 USD |
| `7D` | `302.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 40,380.00 USD | 64,640.00 USD | 0.00 USD |
| `1D` | `303.10` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 20,770.00 USD | 1,360.00 USD | 14,670.00 USD |
| `7D` | `303.30` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 220.53 USD |
| `1D` | `303.50` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 11,460.00 USD | 232.42 USD | 6,250.00 USD |
| `7D` | `303.70` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 17,370.00 USD | 8,710.00 USD | 24,630.00 USD |
| `1D` | `303.90` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 29,930.00 USD | 3,900.00 USD | 18,760.00 USD |
| `7D` | `304.10` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 5,440.00 USD | 1,950.00 USD | 95.81 USD |
| `1D` | `304.30` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 4,310.00 USD | 5,170.00 USD | 48,560.00 USD |
| `7D` | `304.50` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 3,480.00 USD | 11,110.00 USD | 68.95 USD |
| `1D` | `304.70` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 9,700.00 USD | 4,920.00 USD | 40,350.00 USD |
| `7D` | `304.90` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 34,680.00 USD | 18,990.00 USD | 8,430.00 USD |
| `1D` | `305.10` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 9,410.00 USD | 236.66 USD | 2,010.00 USD |
| `7D` | `305.30` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 162,420.00 USD | 128,450.00 USD | 117,030.00 USD |
| `1D` | `305.50` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 4,980.00 USD | 1,820.00 USD | 1,500.00 USD |
| `7D` | `305.70` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 82,270.00 USD | 18,170.00 USD | 17,450.00 USD |
| `1D` | `305.90` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 9,360.00 USD | 2,810.00 USD | 1,930.00 USD |
| `7D` | `306.10` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 22,930.00 USD | 68,220.00 USD | 46,170.00 USD |
| `1D` | `306.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 4,260.00 USD | 3,210.00 USD | 1,390.00 USD |
| `7D` | `306.50` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 30,150.00 USD | 41,830.00 USD | 65,780.00 USD |
| `1D` | `306.70` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 4,450.00 USD | 21,850.00 USD | 3,850.00 USD |
| `7D` | `306.90` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 58,810.00 USD | 50,570.00 USD | 57,650.00 USD |
| `1D` | `307.10` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 33,050.00 USD | 42,120.00 USD | 13,710.00 USD |
| `7D` | `307.30` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 34,320.00 USD | 123,720.00 USD | 83,200.00 USD |
| `1D` | `307.50` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 6,340.00 USD | 22,290.00 USD | 9,430.00 USD |
| `7D` | `307.70` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 84,930.00 USD | 74,370.00 USD | 23,930.00 USD |
| `1D` | `307.90` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 33,320.00 USD | 30,610.00 USD | 21,640.00 USD |
| `7D` | `308.10` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 106,040.00 USD | 63,640.00 USD | 107,010.00 USD |
| `1D` | `308.30` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 13,940.00 USD | 7,490.00 USD | 5,640.00 USD |
| `7D` | `308.50` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 118,090.00 USD | 64,440.00 USD | 65,570.00 USD |
| `1D` | `308.70` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 5,550.00 USD | 387.08 USD | 3,480.00 USD |
| `7D` | `308.90` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 60,660.00 USD | 31,940.00 USD | 19,680.00 USD |
| `1D` | `309.10` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD |
| `7D` | `309.30` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 27,920.00 USD | 26,240.00 USD | 36,580.00 USD |
| `1D` | `309.50` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 12,390.00 USD | 22,900.00 USD | 8,280.00 USD |
| `7D` | `309.70` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 40,410.00 USD | 132,660.00 USD | 153,350.00 USD |
| `1D` | `309.90` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 8,500.00 USD | 2,590.00 USD | 978.51 USD |
| `7D` | `310.10` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 34,250.00 USD | 63,360.00 USD | 62,840.00 USD |
| `1D` | `310.30` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 232.38 USD | 7,040.00 USD | 2.37 USD |
| `7D` | `310.50` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 68,560.00 USD | 73,280.00 USD | 21,950.00 USD |
| `1D` | `310.70` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 144.00 USD | 421.81 USD | 2.98 USD |
| `7D` | `310.90` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 35,670.00 USD | 30,720.00 USD | 3,870.00 USD |
| `1D` | `311.10` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 134.35 USD | 2,050.00 USD | 0.82 USD |
| `7D` | `311.30` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 84,180.00 USD | 65,480.00 USD | 47,600.00 USD |
| `1D` | `311.50` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 7,390.00 USD | 6,590.00 USD | 2,760.00 USD |
| `7D` | `311.70` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 34,040.00 USD | 11,430.00 USD | 31,770.00 USD |
| `1D` | `311.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 4.14 USD |
| `7D` | `312.10` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 46,850.00 USD | 1,100.00 USD | 24,330.00 USD |
| `1D` | `312.30` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD |
| `7D` | `312.50` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 19,540.00 USD | 22,180.00 USD | 49,740.00 USD |
| `1D` | `312.70` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 13,380.00 USD | 2,180.00 USD | 0.00 USD |
| `7D` | `312.90` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 30,070.00 USD |
| `1D` | `313.10` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD |
| `7D` | `313.30` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 64,910.00 USD | 30,120.00 USD | 22,650.00 USD |
| `1D` | `313.50` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `7D` | `313.70` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 32,170.00 USD | 15,010.00 USD | 23,070.00 USD |
| `1D` | `313.90` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `314.10` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 26,810.00 USD | 362.37 USD | 47,790.00 USD |
| `1D` | `314.30` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.50` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 48,630.00 USD | 307.60 USD | 24,540.00 USD |
| `1D` | `314.70` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 32.00 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `314.90` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 29,590.00 USD | 0.00 USD | 10,360.00 USD |
| `1D` | `315.10` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 32.50 USD | 0.00 USD | 4,820.00 USD |
| `7D` | `315.30` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 5,690.00 USD | 547.95 USD | 4.11 USD |
| `1D` | `315.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 3,270.00 USD | 19,390.00 USD |
| `7D` | `315.70` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 9,200.00 USD | 50,270.00 USD | 48,150.00 USD |
| `1D` | `315.90` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 3,440.00 USD | 5,260.00 USD | 43.23 USD |
| `7D` | `316.10` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,400.00 USD |
| `1D` | `316.30` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 12,470.00 USD | 5,050.00 USD | 11,800.00 USD |
| `7D` | `316.50` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 16,120.00 USD | 20,630.00 USD | 18,360.00 USD |
| `1D` | `316.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 16,490.00 USD | 8,910.00 USD | 14,250.00 USD |
| `7D` | `316.90` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 42.47 USD |
| `1D` | `317.10` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 3,940.00 USD | 4,440.00 USD | 8,940.00 USD |
| `7D` | `317.30` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 14,540.00 USD | 748.91 USD | 125.83 USD |
| `1D` | `317.50` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 11,570.00 USD | 14,470.00 USD | 17,050.00 USD |
| `7D` | `317.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 620.15 USD | 265.17 USD | 118.37 USD |
| `1D` | `317.90` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 7,000.00 USD | 9,190.00 USD | 16,750.00 USD |
| `7D` | `318.10` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 22,250.00 USD | 9,100.00 USD | 183.15 USD |
| `1D` | `318.30` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 2,200.00 USD | 8,470.00 USD | 10,400.00 USD |
| `7D` | `318.50` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 3,010.00 USD | 26,630.00 USD | 36,360.00 USD |
| `1D` | `318.70` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD |
| `7D` | `318.90` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 10,270.00 USD | 17,970.00 USD | 23,770.00 USD |
| `1D` | `319.10` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 12,470.00 USD | 6,810.00 USD | 6,660.00 USD |
| `7D` | `319.30` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 18,060.00 USD | 36.86 USD |
| `1D` | `319.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 8,590.00 USD | 10,950.00 USD | 0.00 USD |
| `7D` | `319.70` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 49.12 USD |
| `1D` | `319.90` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 4,350.00 USD | 2,370.00 USD | 0.00 USD |
| `7D` | `320.10` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD |
| `1D` | `320.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 4,210.00 USD | 16,510.00 USD |
| `7D` | `320.50` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 15,190.00 USD | 10,080.00 USD | 18.28 USD |
| `1D` | `320.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `320.90` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.30` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD |
| `7D` | `321.70` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD |
| `7D` | `322.10` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 22,940.00 USD | 8,290.00 USD | 6,150.00 USD |
| `7D` | `322.50` | 9,230,000.00 USD | 9,230,000.00 USD | 0.00 USD | 555.20 USD | 365.55 USD | 0.48 USD |
| `7D` | `322.90` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 16,590.00 USD | 5,630.00 USD | 53.16 USD |
| `7D` | `323.30` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 14,160.00 USD | 5,860.00 USD | 11,480.00 USD |
| `7D` | `323.70` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.10` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD |
| `7D` | `324.40` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `315.01M` | Total OI Tokens: `1,095,583.0 BCH`
  * 1h OI Change: `-0.71%` | 4h OI Change: `+0.71%` | 24h OI Change: `-2.06%`
  * Exchange Breakdown: Binance=`93.84M` | Bybit=`39.93M` | OKX=`24.56M` | Hyperliquid=`8.17M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.21K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0022%` | **USDT OKX** | `-0.0065%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0024%` |
| **USDT MEXC** | `0.0022%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0001%` | **USDT Bitget** | `0.0067%` |
| **CoinM Binance** | `-0.0017%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `55.99%` | `44.01%` | `1.27` | 1,980,000.00 USD |
| `15M` | `Binance` | `60.5%` | `39.5%` | `1.53` | 452,190.00 USD |
| `15M` | `OKX` | `34.22%` | `65.78%` | `0.52` | 213,550.00 USD |
| `15M` | `Bybit` | `46.97%` | `53.03%` | `0.89` | 185,700.00 USD |
| `15M` | `KuCoin` | `78.26%` | `21.74%` | `3.60` | 132.61 USD |
| `15M` | `Gate` | `60.17%` | `39.83%` | `1.51` | 265,730.00 USD |
| `15M` | `Bitget` | `55.21%` | `44.79%` | `1.23` | 72,090.00 USD |
| `15M` | `BingX` | `49.45%` | `50.55%` | `0.98` | 477,970.00 USD |
| `15M` | `MEXC` | `79.22%` | `20.78%` | `3.81` | 22,920.00 USD |
| `15M` | `Bitunix` | `51.63%` | `48.37%` | `1.07` | 21,130.00 USD |
| `15M` | `Hyperliquid` | `31.1%` | `68.9%` | `0.45` | 3,670.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.59%` | `50.41%` | `0.98` | 88,560.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `96.43%` | `3.57%` | `27.01` | 168,540.00 USD |
| `15M` | `HTX` | `56.3%` | `43.7%` | `1.29` | 686.07 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `21.43%` | `78.57%` | `0.27` | 9,660.00 USD |
| `15M` | `Aster` | `94.51%` | `5.49%` | `17.21` | 2,120.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 5.13 USD |
| `15M` | `Whale Positions` | `60.5%` | `39.5%` | `1.53` | 452,190.00 USD |
| `15M` | `Global Accounts` | `55.99%` | `44.01%` | `1.27` | 1,980,000.00 USD |
| `1H` | `BCH` | `56.16%` | `43.84%` | `1.28` | 10,560,000.00 USD |
| `1H` | `Binance` | `53.21%` | `46.79%` | `1.14` | 2,820,000.00 USD |
| `1H` | `OKX` | `54.57%` | `45.43%` | `1.20` | 948,390.00 USD |
| `1H` | `Bybit` | `48.97%` | `51.03%` | `0.96` | 1,180,000.00 USD |
| `1H` | `KuCoin` | `60.5%` | `39.5%` | `1.53` | 93,220.00 USD |
| `1H` | `Gate` | `54.43%` | `45.57%` | `1.19` | 1,400,000.00 USD |
| `1H` | `Bitget` | `47.94%` | `52.06%` | `0.92` | 201,310.00 USD |
| `1H` | `BingX` | `49.68%` | `50.32%` | `0.99` | 2,040,000.00 USD |
| `1H` | `MEXC` | `51.97%` | `48.03%` | `1.08` | 241,480.00 USD |
| `1H` | `Bitunix` | `52.87%` | `47.13%` | `1.12` | 109,940.00 USD |
| `1H` | `Hyperliquid` | `32.92%` | `67.08%` | `0.49` | 125,520.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.84%` | `50.16%` | `0.99` | 341,170.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.77%` | `2.23%` | `43.84` | 1,020,000.00 USD |
| `1H` | `HTX` | `73.59%` | `26.41%` | `2.79` | 3,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `18.66%` | `81.34%` | `0.23` | 28,090.00 USD |
| `1H` | `Aster` | `41.51%` | `58.49%` | `0.71` | 10,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `72.52%` | `27.48%` | `2.64` | 440.89 USD |
| `1H` | `Whale Positions` | `53.21%` | `46.79%` | `1.14` | 2,820,000.00 USD |
| `1H` | `Global Accounts` | `56.16%` | `43.84%` | `1.28` | 10,560,000.00 USD |
| `4H` | `BCH` | `53.05%` | `46.95%` | `1.13` | 56,510,000.00 USD |
| `4H` | `Binance` | `49.18%` | `50.82%` | `0.97` | 17,020,000.00 USD |
| `4H` | `OKX` | `47.39%` | `52.61%` | `0.90` | 6,250,000.00 USD |
| `4H` | `Bybit` | `51%` | `49%` | `1.04` | 4,670,000.00 USD |
| `4H` | `KuCoin` | `46.57%` | `53.43%` | `0.87` | 528,130.00 USD |
| `4H` | `Gate` | `50.07%` | `49.93%` | `1.00` | 7,480,000.00 USD |
| `4H` | `Bitget` | `59.17%` | `40.83%` | `1.45` | 956,050.00 USD |
| `4H` | `BingX` | `45.19%` | `54.81%` | `0.82` | 9,140,000.00 USD |
| `4H` | `MEXC` | `46.53%` | `53.47%` | `0.87` | 1,510,000.00 USD |
| `4H` | `Bitunix` | `48.32%` | `51.68%` | `0.93` | 824,790.00 USD |
| `4H` | `Hyperliquid` | `45.88%` | `54.12%` | `0.85` | 411,130.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.62%` | `49.38%` | `1.03` | 2,070,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `97.06%` | `2.94%` | `33.01` | 5,200,000.00 USD |
| `4H` | `HTX` | `43.98%` | `56.02%` | `0.79` | 86,510.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.68%` | `64.32%` | `0.55` | 237,540.00 USD |
| `4H` | `Aster` | `69.47%` | `30.53%` | `2.28` | 83,230.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.31%` | `68.69%` | `0.46` | 51,990.00 USD |
| `4H` | `Whale Positions` | `49.18%` | `50.82%` | `0.97` | 17,020,000.00 USD |
| `4H` | `Global Accounts` | `53.05%` | `46.95%` | `1.13` | 56,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `290.00` | `289.14` | `290.00` | `290.24` | `288.04` | 1,415,488.00 USD | 804,419.88 USD | 611,068.12 USD | 193,351.76 USD | `+13.66%` | `22B / 10S` |
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `290.49` | `289.33` | `290.49` | `291.59` | `287.81` | 1,897,766.44 USD | 827,805.59 USD | 1,069,960.85 USD | -242,155.26 USD | `-12.76%` | `25B / 40S` |
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `288.94` | `289.00` | `289.94` | `288.00` | 1,099,157.40 USD | 660,933.72 USD | 438,223.69 USD | 222,710.03 USD | `+20.26%` | `43B / 33S` |
| `5:00 UTC` | `287.91` | `288.60` | `287.91` | `289.87` | `287.51` | 851,365.60 USD | 435,531.09 USD | 415,834.51 USD | 19,696.57 USD | `+2.31%` | `18B / 22S` |
| `0:00 UTC` | `286.33` | `286.94` | `286.33` | `287.87` | `285.90` | 1,269,041.85 USD | 639,367.56 USD | 629,674.29 USD | 9,693.27 USD | `+0.76%` | `32B / 48S` |
| `5:00 UTC` | `288.00` | `288.25` | `288.00` | `289.13` | `287.22` | 1,082,751.51 USD | 592,384.75 USD | 490,366.75 USD | 102,018.00 USD | `+9.42%` | `41B / 33S` |
| `0:00 UTC` | `287.00` | `287.52` | `287.00` | `288.53` | `286.82` | 570,885.33 USD | 311,748.26 USD | 259,137.07 USD | 52,611.19 USD | `+9.22%` | `38B / 34S` |

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
| `5m` | 2,910.00 USD | 91,670.00 USD | **`ACCUMULATION`** |
| `15m` | 14,190.00 USD | 282,870.00 USD | **`ACCUMULATION`** |
| `30m` | -23,270.00 USD | 561,140.00 USD | **`ACCUMULATION`** |
| `1h` | -155,280.00 USD | 698,050.00 USD | **`ACCUMULATION`** |
| `2h` | -130,820.00 USD | 840,990.00 USD | **`ACCUMULATION`** |
| `4h` | -173,820.00 USD | -2,350,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 266,440.00 USD | -963,560.00 USD | **`DISTRIBUTION`** |
| `8h` | 80,590.00 USD | -295,610.00 USD | **`DISTRIBUTION`** |
| `12h` | 338,020.00 USD | -1,430,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -872,640.00 USD | -7,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 91,210.00 USD | -12,210,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,520,000.00 USD | -136,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+2.91K` | 15m=`+14.19K` | 1h=`-155.28K` | 24h=`-872.64K`
* Futures Capital Netflows: 5m=`+91.67K` | 15m=`+282.87K` | 1h=`+698.05K` | 24h=`-7.31M`
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
  * `2026-10-30 00:17:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:38:29 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `272.95` (Risk Distance: `3.57` pts)
  * +2.5R Take Profit: `285.44`
  * Mathematical Lot Sizing: **`2.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.13` (Risk Distance: `3.57` pts)
  * +2.5R Take Profit: `278.64`
  * Mathematical Lot Sizing: **`2.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`290.05`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
