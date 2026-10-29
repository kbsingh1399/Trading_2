# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 23:49:57 IST` (`2026-10-29 18:19:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `288.56` | **Live Ask Quote**: `289.04` | **Mid Price**: `288.80`
- **Spread Points**: `480.00` | **Spread BPS**: `16.62 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.44` | VWAP Z-Score: `+1.48` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `63.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `294.88` | Lower -3.00σ Band: `269.99`
  * Upper +2.51σ Band: `292.85` | Lower -2.51σ Band: `272.02`
  * Upper +2.01σ Band: `290.77` | Lower -2.01σ Band: `274.10`
  * Upper +2.00σ Band: `290.73` | Lower -2.00σ Band: `274.14`
  * Upper +1.28σ Band: `287.75` | Lower -1.28σ Band: `277.13`
  * Upper +1.00σ Band: `286.58` | Lower -1.00σ Band: `278.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.97` | EMA-20=`285.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.48` (Slope: `+0.0000`) | EMA-100=`284.14`
  * Institutional Anchors: EMA-144=`284.66` | EMA-200=`284.51` (Slope: `+0.1497`) | EMA-233=`284.77`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.56` (Distance: `+0.52%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.71%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.53%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `287.64` - `289.96`
  * Optimal Trade Entry (OTE 0.705): `289.38`
  * Structural Invalidation Anchor (0.786): `291.11`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `289.05` | `289.93` | `288.93` | `289.19` | `862` | 249,486.48 USD | 30,986.06 USD | `+12.42%` | -3,314,029.71 USD | `+0.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `289.19` | `289.25` | `288.00` | `289.04` | `1,181` | 340,817.33 USD | 23,589.54 USD | `+6.92%` | -3,290,440.18 USD | `-0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `289.04` | `289.19` | `289.04` | `289.19` | `11` | 3,218.08 USD | 3,160.25 USD | `+98.20%` | -3,287,279.93 USD | `-0.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `288.74` | `289.31` | `286.48` | `288.89` | `6,651` | 1,912,559.47 USD | -50,347.76 USD | `-2.63%` | -3,056,475.79 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `288.88` | `289.93` | `288.00` | `289.04` | `3,804` | 1,099,157.40 USD | 222,710.03 USD | `+20.26%` | -2,833,765.76 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `289.04` | `289.19` | `289.04` | `289.19` | `11` | 3,218.08 USD | 3,160.25 USD | `+98.20%` | -2,830,605.51 USD | `+0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -3,009,893.89 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `291.58` | `286.48` | `288.89` | `23,176` | 6,696,574.59 USD | 177,926.21 USD | `+2.66%` | -2,831,967.68 USD | `+0.54` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `288.88` | `289.93` | `288.00` | `289.08` | `3,812` | 1,101,421.06 USD | 224,973.69 USD | `+20.43%` | -2,606,993.99 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.48` | `289.10` | `74,811` | 21,667,432.85 USD | -1,888,266.28 USD | `-8.71%` | -2,875,270.67 USD | `-0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.48` | `289.10` | `74,811` | 21,667,432.85 USD | -1,888,266.28 USD | `-8.71%` | -2,875,270.67 USD | `-0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`288.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1949` | `0x12d2...f97f` | `LONG` | 1,049,143.77 USD | `3,627,243,000,000.00` | `303.26` | `289.30` | `0.000000` | -50,855.57 USD | `-4.85%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.70` (Vol: 152,600.00 USD, Dist: `+2.32%`) | Long MP=`271.76` (Vol: 159,600.00 USD, Dist: `--5.97%`)
  * 48H Horizon: Short MP=`295.64` (Vol: 196,600.00 USD, Dist: `+2.30%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--5.93%`)
  * 3D Horizon: Short MP=`295.64` (Vol: 196,600.00 USD, Dist: `+2.30%`) | Long MP=`274.36` (Vol: 203,100.00 USD, Dist: `--5.07%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+1.86%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--8.76%`)
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
| `7D` | `Long Liquidation` | `248.50` | 18,750,000.00 USD | 18,750,000.00 USD | 42,680.00 USD | 13,170.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 18,660,000.00 USD | 18,660,000.00 USD | 18,160.00 USD | 22,560.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 18,610,000.00 USD | 18,610,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.70` | 18,560,000.00 USD | 18,560,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.10` | 18,470,000.00 USD | 18,470,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.50` | 18,380,000.00 USD | 18,380,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 212,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.90` | 18,300,000.00 USD | 18,300,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 18,250,000.00 USD | 18,250,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 211,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 18,130,000.00 USD | 18,130,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.10` | 17,970,000.00 USD | 17,970,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.50` | 17,850,000.00 USD | 17,850,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 211,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.90` | 17,760,000.00 USD | 17,760,000.00 USD | 13,480.00 USD | 19,580.00 USD | 7.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 17,720,000.00 USD | 17,720,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 17,630,000.00 USD | 17,630,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.10` | 17,560,000.00 USD | 17,560,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.50` | 17,480,000.00 USD | 17,480,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 210,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.90` | 17,420,000.00 USD | 17,420,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 17,390,000.00 USD | 17,390,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 209,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `255.70` | 17,280,000.00 USD | 17,280,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.10` | 17,200,000.00 USD | 17,200,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.50` | 17,110,000.00 USD | 17,110,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.90` | 17,030,000.00 USD | 17,030,000.00 USD | 45,670.00 USD | 16,630.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 16,930,000.00 USD | 16,930,000.00 USD | 23,000.00 USD | 1,850.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 8,130,000.00 USD | 8,130,000.00 USD | 4,210.00 USD | 5,710.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.70` | 16,880,000.00 USD | 16,880,000.00 USD | 47,180.00 USD | 6,040.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 8,110,000.00 USD | 8,110,000.00 USD | 32.50 USD | 991.50 USD | 10,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.10` | 16,810,000.00 USD | 16,810,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 8,100,000.00 USD | 8,100,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.50` | 16,670,000.00 USD | 16,670,000.00 USD | 109,750.00 USD | 15,580.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 8,080,000.00 USD | 8,080,000.00 USD | 5,020.00 USD | 5,060.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 16,520,000.00 USD | 16,520,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 8,050,000.00 USD | 8,050,000.00 USD | 24,070.00 USD | 9,900.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 16,460,000.00 USD | 16,460,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 8,010,000.00 USD | 8,010,000.00 USD | 4,620.00 USD | 2,470.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 16,410,000.00 USD | 16,410,000.00 USD | 17,070.00 USD | 13,660.00 USD | 84.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 8,000,000.00 USD | 8,000,000.00 USD | 16,510.00 USD | 17,870.00 USD | 23,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.10` | 16,380,000.00 USD | 16,380,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 7,940,000.00 USD | 7,940,000.00 USD | 3,100.00 USD | 9,440.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.50` | 16,340,000.00 USD | 16,340,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 7,920,000.00 USD | 7,920,000.00 USD | 5,040.00 USD | 15,080.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 16,280,000.00 USD | 16,280,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 7,890,000.00 USD | 7,890,000.00 USD | 12,720.00 USD | 6,900.00 USD | 6,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 16,190,000.00 USD | 16,190,000.00 USD | 2,490.00 USD | 34,410.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 7,870,000.00 USD | 7,870,000.00 USD | 8,750.00 USD | 14,260.00 USD | 7.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 16,140,000.00 USD | 16,140,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 7,840,000.00 USD | 7,840,000.00 USD | 4,920.00 USD | 4,330.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.10` | 16,040,000.00 USD | 16,040,000.00 USD | 60,340.00 USD | 35,350.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 7,820,000.00 USD | 7,820,000.00 USD | 8,640.00 USD | 626.24 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.50` | 15,910,000.00 USD | 15,910,000.00 USD | 36,590.00 USD | 26,590.00 USD | 24.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 7,810,000.00 USD | 7,810,000.00 USD | 150.60 USD | 1,190.00 USD | 3.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 15,850,000.00 USD | 15,850,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 7,810,000.00 USD | 7,810,000.00 USD | 8,670.00 USD | 571.81 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 15,720,000.00 USD | 15,720,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 7,790,000.00 USD | 7,790,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 15,620,000.00 USD | 15,620,000.00 USD | 265,940.00 USD | 96,750.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 7,760,000.00 USD | 7,760,000.00 USD | 746.44 USD | 825.92 USD | 10.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.10` | 15,230,000.00 USD | 15,230,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 7,760,000.00 USD | 7,760,000.00 USD | 1,860.00 USD | 647.93 USD | 5.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.50` | 15,060,000.00 USD | 15,060,000.00 USD | 58,720.00 USD | 23,360.00 USD | 37,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.70` | 7,760,000.00 USD | 7,760,000.00 USD | 28,300.00 USD | 615.20 USD | 36,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 14,940,000.00 USD | 14,940,000.00 USD | 34,850.00 USD | 75,260.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 7,690,000.00 USD | 7,690,000.00 USD | 20,980.00 USD | 8,870.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 14,810,000.00 USD | 14,810,000.00 USD | 133,130.00 USD | 59,960.00 USD | 111,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 7,650,000.00 USD | 7,650,000.00 USD | 10,270.00 USD | 11,920.00 USD | 67,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `265.70` | 14,510,000.00 USD | 14,510,000.00 USD | 54,220.00 USD | 81,830.00 USD | 61,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.90` | 7,560,000.00 USD | 7,560,000.00 USD | 14,110.00 USD | 11,970.00 USD | 13.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.10` | 14,310,000.00 USD | 14,310,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 7,530,000.00 USD | 7,530,000.00 USD | 32,850.00 USD | 245.13 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.50` | 13,950,000.00 USD | 13,950,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.70` | 7,490,000.00 USD | 7,490,000.00 USD | 14,960.00 USD | 3,340.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 13,640,000.00 USD | 13,640,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 7,470,000.00 USD | 7,470,000.00 USD | 28,570.00 USD | 6,580.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 13,280,000.00 USD | 13,280,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 7,430,000.00 USD | 7,430,000.00 USD | 11,820.00 USD | 26,590.00 USD | 4.65 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `267.70` | 12,920,000.00 USD | 12,920,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.90` | 7,390,000.00 USD | 7,390,000.00 USD | 113,380.00 USD | 120,840.00 USD | 45,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.10` | 12,470,000.00 USD | 12,470,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 7,110,000.00 USD | 7,110,000.00 USD | 39,130.00 USD | 98,350.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.50` | 11,980,000.00 USD | 11,980,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.70` | 6,950,000.00 USD | 6,950,000.00 USD | 97,080.00 USD | 85,050.00 USD | 58,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 11,560,000.00 USD | 11,560,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 6,700,000.00 USD | 6,700,000.00 USD | 50,070.00 USD | 23,000.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 11,160,000.00 USD | 11,160,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 6,620,000.00 USD | 6,620,000.00 USD | 31,770.00 USD | 6,030.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `269.70` | 10,620,000.00 USD | 10,620,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 6,570,000.00 USD | 6,570,000.00 USD | 33,840.00 USD | 43,730.00 USD | 13,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.10` | 10,460,000.00 USD | 10,460,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 6,480,000.00 USD | 6,480,000.00 USD | 108,850.00 USD | 64,910.00 USD | 128,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.50` | 10,050,000.00 USD | 10,050,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 106.31 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.70` | 6,180,000.00 USD | 6,180,000.00 USD | 52,010.00 USD | 39,890.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 9,660,000.00 USD | 9,660,000.00 USD | 318,780.00 USD | 144,560.00 USD | 90,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 6,080,000.00 USD | 6,080,000.00 USD | 40,150.00 USD | 34,010.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 9,110,000.00 USD | 9,110,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 5,870,000.00 USD | 5,870,000.00 USD | 28,220.00 USD | 37,420.00 USD | 15,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `271.70` | 8,820,000.00 USD | 8,820,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 5,790,000.00 USD | 5,790,000.00 USD | 138,620.00 USD | 37,570.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.10` | 8,310,000.00 USD | 8,310,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 5,550,000.00 USD | 5,550,000.00 USD | 66,270.00 USD | 15,920.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.50` | 7,830,000.00 USD | 7,830,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 5,460,000.00 USD | 5,460,000.00 USD | 76,380.00 USD | 36,390.00 USD | 43,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 7,470,000.00 USD | 7,470,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 5,300,000.00 USD | 5,300,000.00 USD | 89,480.00 USD | 87,000.00 USD | 6,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 7,030,000.00 USD | 7,030,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 5,120,000.00 USD | 5,120,000.00 USD | 225,140.00 USD | 235,020.00 USD | 90,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 6,350,000.00 USD | 6,350,000.00 USD | 195,450.00 USD | 467,590.00 USD | 205,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 4,560,000.00 USD | 4,560,000.00 USD | 95,740.00 USD | 211,090.00 USD | 75,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.10` | 5,480,000.00 USD | 5,480,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 4,180,000.00 USD | 4,180,000.00 USD | 204,120.00 USD | 184,400.00 USD | 133,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.50` | 4,630,000.00 USD | 4,630,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.70` | 3,660,000.00 USD | 3,660,000.00 USD | 101,740.00 USD | 42,950.00 USD | 53,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 4,020,000.00 USD | 4,020,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 3,460,000.00 USD | 3,460,000.00 USD | 62,250.00 USD | 19,560.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 3,500,000.00 USD | 3,500,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 3,340,000.00 USD | 3,340,000.00 USD | 59,520.00 USD | 65,680.00 USD | 39,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 3,360,000.00 USD | 3,360,000.00 USD | 1,350.00 USD | 51,050.00 USD | 11.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 3,170,000.00 USD | 3,170,000.00 USD | 47,640.00 USD | 51,470.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.10` | 3,310,000.00 USD | 3,310,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 3,050,000.00 USD | 3,050,000.00 USD | 62,820.00 USD | 42,520.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.50` | 3,300,000.00 USD | 3,300,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.70` | 2,940,000.00 USD | 2,940,000.00 USD | 10,750.00 USD | 16,180.00 USD | 6.08 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 3,300,000.00 USD | 3,300,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 2,910,000.00 USD | 2,910,000.00 USD | 13,560.00 USD | 64,370.00 USD | 45,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 2,790,000.00 USD | 2,790,000.00 USD | 67,150.00 USD | 63,410.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 27,190.00 USD | 55,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 2,640,000.00 USD | 2,640,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.10` | 3,070,000.00 USD | 3,070,000.00 USD | 24,750.00 USD | 0.00 USD | 59,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 2,620,000.00 USD | 2,620,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.50` | 2,980,000.00 USD | 2,980,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 2,480,000.00 USD | 2,480,000.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.90` | 2,890,000.00 USD | 2,890,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.10` | 2,410,000.00 USD | 2,410,000.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 2,800,000.00 USD | 2,800,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.50` | 2,330,000.00 USD | 2,330,000.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 2,730,000.00 USD | 2,730,000.00 USD | 46,800.00 USD | 0.00 USD | 54,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.90` | 2,260,000.00 USD | 2,260,000.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.30` | 2,220,000.00 USD | 2,220,000.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.70` | 2,150,000.00 USD | 2,150,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.90` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.10` | 2,060,000.00 USD | 2,060,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 2,560,000.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.90` | 1,990,000.00 USD | 1,990,000.00 USD | 9,360.00 USD | 16,510.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.10` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.30` | 1,860,000.00 USD | 1,860,000.00 USD | 55,330.00 USD | 22,600.00 USD | 124,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.50` | 2,310,000.00 USD | 2,310,000.00 USD | 32,190.00 USD | 0.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.70` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 23,250.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.90` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 117.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.10` | 1,640,000.00 USD | 1,640,000.00 USD | 45,550.00 USD | 44,720.00 USD | 161,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 37,310.00 USD | 89,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.50` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 181,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.90` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.10` | 1,930,000.00 USD | 1,930,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.30` | 1,280,000.00 USD | 1,280,000.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.50` | 1,740,000.00 USD | 1,740,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.70` | 1,170,000.00 USD | 1,170,000.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.90` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.10` | 1,040,000.00 USD | 1,040,000.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.30` | 1,200,000.00 USD | 1,200,000.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.50` | 939,560.00 USD | 939,560.00 USD | 91,500.00 USD | 95,280.00 USD | 52,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.70` | 910,340.00 USD | 910,340.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.90` | 700,760.00 USD | 700,760.00 USD | 0.00 USD | 42,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.10` | 796,710.00 USD | 796,710.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.30` | 657,920.00 USD | 657,920.00 USD | 20,960.00 USD | 11,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.50` | 721,860.00 USD | 721,860.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.70` | 625,330.00 USD | 625,330.00 USD | 134,800.00 USD | 85,750.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.90` | 602,420.00 USD | 602,420.00 USD | 27,530.00 USD | 141,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.10` | 323,950.00 USD | 323,950.00 USD | 38,480.00 USD | 136,750.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.30` | 433,730.00 USD | 433,730.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.50` | 68,020.00 USD | 68,020.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.70` | 293,550.00 USD | 293,550.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.90` | 57,010.00 USD | 57,010.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `288.10` | 139,290.00 USD | 139,290.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.30` | 23,360.00 USD | 23,360.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `289.10` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 11,990.00 USD | 6.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.50` | 1.36 USD | 1.36 USD | 0.00 USD | 0.00 USD | 1.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `290.50` | 1,210.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.10` | 6.84 USD | 6.84 USD | 0.00 USD | 0.00 USD | 5.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 11,120.00 USD | 11,120.00 USD | 0.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 50,330.00 USD | 50,330.00 USD | 0.00 USD | 50,320.00 USD | 10.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 105,210.00 USD | 105,210.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 78,380.00 USD | 78,380.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.10` | 223,890.00 USD | 223,890.00 USD | 0.00 USD | 118,660.00 USD | 18.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 136,090.00 USD | 136,090.00 USD | 0.00 USD | 57,710.00 USD | 4.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.50` | 250,600.00 USD | 250,600.00 USD | 0.00 USD | 26,610.00 USD | 103.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 234,700.00 USD | 234,700.00 USD | 606.80 USD | 98,000.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 369,140.00 USD | 369,140.00 USD | 0.00 USD | 118,480.00 USD | 70.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 286,370.00 USD | 286,370.00 USD | 857.50 USD | 50,810.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 482,260.00 USD | 482,260.00 USD | 534.50 USD | 112,560.00 USD | 22.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 361,560.00 USD | 361,560.00 USD | 8,580.00 USD | 64,440.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 520,760.00 USD | 520,760.00 USD | 37,280.00 USD | 1,170.00 USD | 54.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 544,310.00 USD | 544,310.00 USD | 73,070.00 USD | 31,360.00 USD | 78,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.10` | 745,180.00 USD | 745,180.00 USD | 85,150.00 USD | 33,590.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 731,580.00 USD | 731,580.00 USD | 62,310.00 USD | 76,770.00 USD | 48,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.50` | 830,190.00 USD | 830,190.00 USD | 69,950.00 USD | 15,030.00 USD | 30.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 1,140,000.00 USD | 1,140,000.00 USD | 134,020.00 USD | 103,120.00 USD | 166,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 1,090,000.00 USD | 1,090,000.00 USD | 63,470.00 USD | 92,770.00 USD | 104,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 1,260,000.00 USD | 1,260,000.00 USD | 32,330.00 USD | 64,510.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 1,400,000.00 USD | 1,400,000.00 USD | 45,590.00 USD | 65,580.00 USD | 195,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 1,580,000.00 USD | 1,580,000.00 USD | 110,930.00 USD | 118,390.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 1,710,000.00 USD | 1,710,000.00 USD | 105,410.00 USD | 72,570.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 1,760,000.00 USD | 1,760,000.00 USD | 105,070.00 USD | 48,120.00 USD | 33,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.10` | 1,990,000.00 USD | 1,990,000.00 USD | 75,740.00 USD | 90,470.00 USD | 119,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 1,990,000.00 USD | 1,990,000.00 USD | 108,090.00 USD | 95,560.00 USD | 27,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.50` | 2,130,000.00 USD | 2,130,000.00 USD | 1,060.00 USD | 77,140.00 USD | 57,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.70` | 2,180,000.00 USD | 2,180,000.00 USD | 41,440.00 USD | 54,160.00 USD | 85,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 2,520,000.00 USD | 2,520,000.00 USD | 206,840.00 USD | 51,220.00 USD | 134,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 2,300,000.00 USD | 2,300,000.00 USD | 52,650.00 USD | 14,350.00 USD | 56,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 2,530,000.00 USD | 2,530,000.00 USD | 3,960.00 USD | 2,500.00 USD | 5.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 2,330,000.00 USD | 2,330,000.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 2,620,000.00 USD | 2,620,000.00 USD | 144.38 USD | 56,790.00 USD | 34,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 2,350,000.00 USD | 2,350,000.00 USD | 1,150.00 USD | 7,600.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.10` | 2,810,000.00 USD | 2,810,000.00 USD | 49,240.00 USD | 80,820.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 2,540,000.00 USD | 2,540,000.00 USD | 44,780.00 USD | 8,520.00 USD | 137,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.50` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 12,660.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 2,660,000.00 USD | 2,660,000.00 USD | 25,160.00 USD | 13,400.00 USD | 80,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 2,980,000.00 USD | 2,980,000.00 USD | 70,090.00 USD | 993.25 USD | 40,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 2,770,000.00 USD | 2,770,000.00 USD | 48,760.00 USD | 22,810.00 USD | 37,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 3,030,000.00 USD | 3,030,000.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 2,850,000.00 USD | 2,850,000.00 USD | 28,240.00 USD | 29,040.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 3,060,000.00 USD | 3,060,000.00 USD | 5,310.00 USD | 7,720.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 2,900,000.00 USD | 2,900,000.00 USD | 17,990.00 USD | 17,070.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.10` | 3,110,000.00 USD | 3,110,000.00 USD | 51,500.00 USD | 2,470.00 USD | 58.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 3,000,000.00 USD | 3,000,000.00 USD | 35,170.00 USD | 32,740.00 USD | 34,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.50` | 3,170,000.00 USD | 3,170,000.00 USD | 866.20 USD | 36,230.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 3,110,000.00 USD | 3,110,000.00 USD | 20,040.00 USD | 37,840.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 3,290,000.00 USD | 3,290,000.00 USD | 24,730.00 USD | 34,630.00 USD | 55,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 3,180,000.00 USD | 3,180,000.00 USD | 35,810.00 USD | 28,610.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 3,510,000.00 USD | 3,510,000.00 USD | 71,140.00 USD | 55,420.00 USD | 94,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 3,280,000.00 USD | 3,280,000.00 USD | 31,870.00 USD | 27,310.00 USD | 44,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 3,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `301.70` | 3,680,000.00 USD | 3,680,000.00 USD | 37,640.00 USD | 130,520.00 USD | 107.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 3,380,000.00 USD | 3,380,000.00 USD | 39,820.00 USD | 51,210.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.10` | 3,880,000.00 USD | 3,880,000.00 USD | 53,220.00 USD | 123,390.00 USD | 26,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 3,410,000.00 USD | 3,410,000.00 USD | 5,320.00 USD | 12,210.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.50` | 4,050,000.00 USD | 4,050,000.00 USD | 31,330.00 USD | 102,200.00 USD | 41,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 3,480,000.00 USD | 3,480,000.00 USD | 11,520.00 USD | 11,410.00 USD | 41,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 4,160,000.00 USD | 4,160,000.00 USD | 40,380.00 USD | 64,640.00 USD | 90.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 3,510,000.00 USD | 3,510,000.00 USD | 21,200.00 USD | 1,360.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 173.09 USD | 96.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 3,530,000.00 USD | 3,530,000.00 USD | 11,970.00 USD | 248.89 USD | 6,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 4,210,000.00 USD | 4,210,000.00 USD | 17,370.00 USD | 8,710.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 3,580,000.00 USD | 3,580,000.00 USD | 29,930.00 USD | 3,900.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.10` | 4,220,000.00 USD | 4,220,000.00 USD | 5,440.00 USD | 1,950.00 USD | 122.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 3,640,000.00 USD | 3,640,000.00 USD | 4,310.00 USD | 5,410.00 USD | 48,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.50` | 4,230,000.00 USD | 4,230,000.00 USD | 3,480.00 USD | 11,110.00 USD | 112.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `304.50` | 1,040.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `304.70` | 3,700,000.00 USD | 3,700,000.00 USD | 9,700.00 USD | 5,010.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 4,290,000.00 USD | 4,290,000.00 USD | 34,680.00 USD | 18,990.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 3,710,000.00 USD | 3,710,000.00 USD | 9,360.00 USD | 236.66 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 4,700,000.00 USD | 4,700,000.00 USD | 162,420.00 USD | 128,450.00 USD | 117,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 3,720,000.00 USD | 3,720,000.00 USD | 4,980.00 USD | 1,760.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 4,820,000.00 USD | 4,820,000.00 USD | 82,270.00 USD | 18,170.00 USD | 17,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 3,730,000.00 USD | 3,730,000.00 USD | 9,360.00 USD | 2,750.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.10` | 4,960,000.00 USD | 4,960,000.00 USD | 22,930.00 USD | 68,220.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 3,740,000.00 USD | 3,740,000.00 USD | 4,260.00 USD | 3,210.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.50` | 5,090,000.00 USD | 5,090,000.00 USD | 30,150.00 USD | 41,830.00 USD | 65,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 3,770,000.00 USD | 3,770,000.00 USD | 4,420.00 USD | 21,850.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 5,260,000.00 USD | 5,260,000.00 USD | 58,810.00 USD | 50,570.00 USD | 57,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 3,860,000.00 USD | 3,860,000.00 USD | 33,050.00 USD | 42,000.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 5,500,000.00 USD | 5,500,000.00 USD | 34,320.00 USD | 123,720.00 USD | 83,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 3,900,000.00 USD | 3,900,000.00 USD | 6,340.00 USD | 22,230.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 5,690,000.00 USD | 5,690,000.00 USD | 84,930.00 USD | 74,370.00 USD | 23,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 3,980,000.00 USD | 3,980,000.00 USD | 33,320.00 USD | 30,610.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.10` | 5,960,000.00 USD | 5,960,000.00 USD | 106,040.00 USD | 63,640.00 USD | 106,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 4,010,000.00 USD | 4,010,000.00 USD | 13,940.00 USD | 7,420.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.50` | 6,210,000.00 USD | 6,210,000.00 USD | 118,090.00 USD | 64,440.00 USD | 65,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 4,020,000.00 USD | 4,020,000.00 USD | 5,550.00 USD | 387.08 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 6,320,000.00 USD | 6,320,000.00 USD | 60,660.00 USD | 31,940.00 USD | 19,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 4,040,000.00 USD | 4,040,000.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 6,410,000.00 USD | 6,410,000.00 USD | 27,920.00 USD | 26,240.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 4,080,000.00 USD | 4,080,000.00 USD | 12,390.00 USD | 22,900.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 6,740,000.00 USD | 6,740,000.00 USD | 40,410.00 USD | 132,660.00 USD | 153,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 4,100,000.00 USD | 4,100,000.00 USD | 8,500.00 USD | 2,590.00 USD | 974.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.10` | 6,900,000.00 USD | 6,900,000.00 USD | 34,250.00 USD | 63,360.00 USD | 62,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 4,100,000.00 USD | 4,100,000.00 USD | 232.38 USD | 7,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.50` | 7,060,000.00 USD | 7,060,000.00 USD | 68,560.00 USD | 73,280.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 5,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.70` | 4,100,000.00 USD | 4,100,000.00 USD | 144.00 USD | 421.81 USD | 8.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 7,130,000.00 USD | 7,130,000.00 USD | 35,670.00 USD | 30,720.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 4,110,000.00 USD | 4,110,000.00 USD | 134.35 USD | 2,050.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 7,330,000.00 USD | 7,330,000.00 USD | 84,180.00 USD | 65,480.00 USD | 47,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 4,160,000.00 USD | 4,160,000.00 USD | 25,300.00 USD | 6,590.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `311.50` | 539.21 USD | 5,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `311.70` | 7,410,000.00 USD | 7,410,000.00 USD | 34,040.00 USD | 11,430.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 4,160,000.00 USD | 4,160,000.00 USD | 2,810.00 USD | 0.00 USD | 3.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.10` | 7,480,000.00 USD | 7,480,000.00 USD | 46,850.00 USD | 1,100.00 USD | 24,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 4,180,000.00 USD | 4,180,000.00 USD | 6,410.00 USD | 5,330.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.50` | 7,570,000.00 USD | 7,570,000.00 USD | 19,540.00 USD | 22,180.00 USD | 49,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 4,200,000.00 USD | 4,200,000.00 USD | 14,010.00 USD | 2,180.00 USD | 38.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 7,650,000.00 USD | 7,650,000.00 USD | 22,600.00 USD | 20,090.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 4,210,000.00 USD | 4,210,000.00 USD | 5,080.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 7,760,000.00 USD | 7,760,000.00 USD | 64,910.00 USD | 30,120.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 4,220,000.00 USD | 4,220,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 7,830,000.00 USD | 7,830,000.00 USD | 32,170.00 USD | 15,010.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 4,240,000.00 USD | 4,240,000.00 USD | 4,760.00 USD | 6,040.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.10` | 7,910,000.00 USD | 7,910,000.00 USD | 26,810.00 USD | 362.37 USD | 47,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.30` | 4,250,000.00 USD | 4,250,000.00 USD | 4,210.00 USD | 5,710.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.50` | 7,980,000.00 USD | 7,980,000.00 USD | 48,630.00 USD | 307.60 USD | 24,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 8,020,000.00 USD | 8,020,000.00 USD | 29,590.00 USD | 0.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 4,260,000.00 USD | 4,260,000.00 USD | 32.50 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 8,030,000.00 USD | 8,030,000.00 USD | 5,690.00 USD | 547.95 USD | 48.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.50` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 3,270.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `315.50` | 6,520.00 USD | 12,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `315.70` | 8,140,000.00 USD | 8,140,000.00 USD | 9,200.00 USD | 50,270.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.90` | 4,290,000.00 USD | 4,290,000.00 USD | 1,470.00 USD | 5,260.00 USD | 44.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.10` | 8,240,000.00 USD | 8,240,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.30` | 4,320,000.00 USD | 4,320,000.00 USD | 12,450.00 USD | 5,050.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.50` | 8,290,000.00 USD | 8,290,000.00 USD | 16,120.00 USD | 20,630.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.70` | 4,360,000.00 USD | 4,360,000.00 USD | 16,490.00 USD | 8,870.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 8,310,000.00 USD | 8,310,000.00 USD | 3,030.00 USD | 10,840.00 USD | 101.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.10` | 4,370,000.00 USD | 4,370,000.00 USD | 3,940.00 USD | 2,260.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 8,320,000.00 USD | 8,320,000.00 USD | 14,540.00 USD | 748.91 USD | 102.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.50` | 4,410,000.00 USD | 4,410,000.00 USD | 11,570.00 USD | 14,470.00 USD | 13,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 8,320,000.00 USD | 8,320,000.00 USD | 620.15 USD | 265.17 USD | 88.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.90` | 4,440,000.00 USD | 4,440,000.00 USD | 4,010.00 USD | 9,140.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.10` | 8,360,000.00 USD | 8,360,000.00 USD | 22,250.00 USD | 9,100.00 USD | 142.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.30` | 4,450,000.00 USD | 4,450,000.00 USD | 2,200.00 USD | 8,470.00 USD | 820.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.50` | 8,420,000.00 USD | 8,420,000.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 12,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.70` | 4,470,000.00 USD | 4,470,000.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 8,470,000.00 USD | 8,470,000.00 USD | 10,270.00 USD | 17,970.00 USD | 23,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.10` | 4,500,000.00 USD | 4,500,000.00 USD | 12,470.00 USD | 6,810.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 18,060.00 USD | 5.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.50` | 4,520,000.00 USD | 4,520,000.00 USD | 8,590.00 USD | 10,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 8,510,000.00 USD | 8,510,000.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.90` | 4,520,000.00 USD | 4,520,000.00 USD | 4,350.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.10` | 8,580,000.00 USD | 8,580,000.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.30` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 4,210.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.50` | 8,610,000.00 USD | 8,610,000.00 USD | 15,190.00 USD | 10,080.00 USD | 49.92 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 13,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `320.70` | 4,550,000.00 USD | 4,550,000.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.90` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.10` | 4,550,000.00 USD | 4,550,000.00 USD | 150.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.30` | 8,630,000.00 USD | 8,630,000.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.50` | 4,570,000.00 USD | 4,570,000.00 USD | 8,670.00 USD | 0.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.70` | 8,660,000.00 USD | 8,660,000.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.10` | 8,700,000.00 USD | 8,700,000.00 USD | 22,940.00 USD | 8,290.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `322.30` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.50` | 8,700,000.00 USD | 8,700,000.00 USD | 555.20 USD | 365.55 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 8,720,000.00 USD | 8,720,000.00 USD | 16,590.00 USD | 5,630.00 USD | 0.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.30` | 8,750,000.00 USD | 8,750,000.00 USD | 14,160.00 USD | 5,860.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.70` | 8,760,000.00 USD | 8,760,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.10` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
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
| `7D` | `248.50` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 42,680.00 USD | 13,170.00 USD | 32,000.00 USD |
| `7D` | `248.90` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 18,160.00 USD | 22,560.00 USD | 11,550.00 USD |
| `7D` | `249.30` | 18,610,000.00 USD | 0.00 USD | 18,610,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD |
| `7D` | `249.70` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 50,470.00 USD | 27,820.00 USD | 14,350.00 USD |
| `7D` | `250.10` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 45,440.00 USD | 17,650.00 USD | 31,090.00 USD |
| `7D` | `250.50` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 9,050.00 USD | 53,240.00 USD | 13,790.00 USD |
| `7D` | `250.90` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,860.00 USD |
| `7D` | `251.30` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,680.00 USD |
| `7D` | `251.70` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 57,590.00 USD | 63,110.00 USD | 37,660.00 USD |
| `7D` | `252.10` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 63,140.00 USD | 22,650.00 USD | 29,620.00 USD |
| `7D` | `252.50` | 17,850,000.00 USD | 0.00 USD | 17,850,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,700.00 USD |
| `7D` | `252.90` | 17,760,000.00 USD | 0.00 USD | 17,760,000.00 USD | 13,480.00 USD | 19,580.00 USD | 7.06 USD |
| `7D` | `253.30` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 30,240.00 USD | 36,720.00 USD | 26,800.00 USD |
| `7D` | `253.70` | 17,630,000.00 USD | 0.00 USD | 17,630,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,090.00 USD |
| `7D` | `254.10` | 17,560,000.00 USD | 0.00 USD | 17,560,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,950.00 USD |
| `7D` | `254.50` | 17,480,000.00 USD | 0.00 USD | 17,480,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,390.00 USD |
| `7D` | `254.90` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,620.00 USD |
| `7D` | `255.30` | 17,390,000.00 USD | 0.00 USD | 17,390,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,030.00 USD |
| `7D` | `255.70` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 19,690.00 USD | 13,030.00 USD | 49,760.00 USD |
| `7D` | `256.10` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,220.00 USD |
| `7D` | `256.50` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,710.00 USD |
| `7D` | `256.90` | 17,030,000.00 USD | 0.00 USD | 17,030,000.00 USD | 45,670.00 USD | 16,630.00 USD | 31,440.00 USD |
| `7D` | `257.30` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 23,000.00 USD | 1,850.00 USD | 27,310.00 USD |
| `1D` | `257.70` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 0.00 USD | 5,670.00 USD | 4,870.00 USD |
| `7D` | `257.70` | 16,880,000.00 USD | 0.00 USD | 16,880,000.00 USD | 47,180.00 USD | 6,040.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 32.50 USD | 4,120.00 USD | 19,390.00 USD |
| `7D` | `258.10` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,750.00 USD |
| `1D` | `258.50` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 1,470.00 USD | 5,260.00 USD | 45.78 USD |
| `7D` | `258.50` | 16,670,000.00 USD | 0.00 USD | 16,670,000.00 USD | 109,750.00 USD | 15,580.00 USD | 21,020.00 USD |
| `1D` | `258.90` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 17,930.00 USD | 11,000.00 USD | 11,810.00 USD |
| `7D` | `258.90` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,360.00 USD |
| `1D` | `259.30` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 13,160.00 USD | 4,150.00 USD | 12,490.00 USD |
| `7D` | `259.30` | 16,460,000.00 USD | 0.00 USD | 16,460,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,050.00 USD |
| `1D` | `259.70` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 14,700.00 USD | 16,830.00 USD | 15,100.00 USD |
| `7D` | `259.70` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 17,070.00 USD | 13,660.00 USD | 84.33 USD |
| `1D` | `260.10` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 5,100.00 USD | 9,630.00 USD | 16,750.00 USD |
| `7D` | `260.10` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,910.00 USD |
| `1D` | `260.50` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 2,850.00 USD | 8,760.00 USD | 10,400.00 USD |
| `7D` | `260.50` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,370.00 USD |
| `1D` | `260.90` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD |
| `7D` | `260.90` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,880.00 USD |
| `1D` | `261.30` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 8,660.00 USD | 16,360.00 USD | 500.69 USD |
| `7D` | `261.30` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 2,490.00 USD | 34,410.00 USD | 15,970.00 USD |
| `1D` | `261.70` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD |
| `7D` | `261.70` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,910.00 USD |
| `1D` | `262.10` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 517.32 USD | 4,790.00 USD | 16,510.00 USD |
| `7D` | `262.10` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 60,340.00 USD | 35,350.00 USD | 32,860.00 USD |
| `1D` | `262.50` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD |
| `7D` | `262.50` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 36,590.00 USD | 26,590.00 USD | 24.52 USD |
| `1D` | `262.90` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD |
| `7D` | `262.90` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,750.00 USD |
| `1D` | `263.30` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD |
| `7D` | `263.30` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,100.00 USD |
| `1D` | `263.70` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD |
| `7D` | `263.70` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 265,940.00 USD | 96,750.00 USD | 27,030.00 USD |
| `1D` | `264.10` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD |
| `7D` | `264.10` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,920.00 USD |
| `1D` | `264.50` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD |
| `7D` | `264.50` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 58,720.00 USD | 23,360.00 USD | 37,310.00 USD |
| `1D` | `264.90` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,670.00 USD |
| `7D` | `264.90` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 34,850.00 USD | 75,260.00 USD | 25,240.00 USD |
| `1D` | `265.30` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 20,730.00 USD | 8,710.00 USD | 33,520.00 USD |
| `7D` | `265.30` | 14,810,000.00 USD | 0.00 USD | 14,810,000.00 USD | 133,130.00 USD | 59,960.00 USD | 111,210.00 USD |
| `1D` | `265.70` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 23,810.00 USD | 23,390.00 USD | 33,670.00 USD |
| `7D` | `265.70` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 54,220.00 USD | 81,830.00 USD | 61,280.00 USD |
| `1D` | `266.10` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 10,200.00 USD | 335.05 USD | 7.04 USD |
| `7D` | `266.10` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 156,850.00 USD | 142,000.00 USD | 57,440.00 USD |
| `1D` | `266.50` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 27,700.00 USD | 3,150.00 USD | 8,720.00 USD |
| `7D` | `266.50` | 13,950,000.00 USD | 0.00 USD | 13,950,000.00 USD | 112,390.00 USD | 80,270.00 USD | 122,140.00 USD |
| `1D` | `266.90` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 32,310.00 USD | 6,620.00 USD | 6,770.00 USD |
| `7D` | `266.90` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,230.00 USD |
| `1D` | `267.30` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 17,990.00 USD | 11,070.00 USD | 3,350.00 USD |
| `7D` | `267.30` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 112,800.00 USD | 158,320.00 USD | 88,780.00 USD |
| `1D` | `267.70` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 83,350.00 USD | 112,140.00 USD | 14,410.00 USD |
| `7D` | `267.70` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 171,250.00 USD | 212,530.00 USD | 62,740.00 USD |
| `1D` | `268.10` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 55,490.00 USD | 80,400.00 USD | 47,150.00 USD |
| `7D` | `268.10` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,590.00 USD |
| `1D` | `268.50` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 57,190.00 USD | 101,540.00 USD | 31,670.00 USD |
| `7D` | `268.50` | 11,980,000.00 USD | 0.00 USD | 11,980,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,210.00 USD |
| `1D` | `268.90` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 92,000.00 USD | 36,230.00 USD | 41,690.00 USD |
| `7D` | `268.90` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,150.00 USD |
| `1D` | `269.30` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 28,630.00 USD | 16,320.00 USD | 20,850.00 USD |
| `7D` | `269.30` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,010.00 USD |
| `1D` | `269.70` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 39,120.00 USD | 24,350.00 USD | 8,680.00 USD |
| `7D` | `269.70` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 55,620.00 USD | 86,170.00 USD | 10,360.00 USD |
| `1D` | `270.10` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 98,640.00 USD | 77,570.00 USD | 98,230.00 USD |
| `7D` | `270.10` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,670.00 USD |
| `1D` | `270.50` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 71,720.00 USD | 36,250.00 USD | 36,810.00 USD |
| `7D` | `270.50` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,710.00 USD |
| `1D` | `270.90` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 11,770.00 USD | 24,230.00 USD | 66,890.00 USD |
| `7D` | `270.90` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 318,780.00 USD | 144,560.00 USD | 90,020.00 USD |
| `1D` | `271.30` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 56,610.00 USD | 46,210.00 USD | 83,200.00 USD |
| `7D` | `271.30` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,340.00 USD |
| `1D` | `271.70` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 38,640.00 USD | 23,380.00 USD | 21,390.00 USD |
| `7D` | `271.70` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,320.00 USD |
| `1D` | `272.10` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 125,130.00 USD | 32,950.00 USD | 17,450.00 USD |
| `7D` | `272.10` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,590.00 USD |
| `1D` | `272.50` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 81,660.00 USD | 31,310.00 USD | 46,830.00 USD |
| `7D` | `272.50` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,110.00 USD |
| `1D` | `272.90` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 80,060.00 USD | 58,140.00 USD | 6,760.00 USD |
| `7D` | `272.90` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,580.00 USD |
| `1D` | `273.30` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 179,830.00 USD | 208,970.00 USD | 35,220.00 USD |
| `7D` | `273.30` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,350.00 USD |
| `1D` | `273.70` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 142,100.00 USD | 172,310.00 USD | 117,060.00 USD |
| `7D` | `273.70` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 195,450.00 USD | 467,590.00 USD | 205,950.00 USD |
| `1D` | `274.10` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 120,870.00 USD | 232,210.00 USD | 71,890.00 USD |
| `7D` | `274.10` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,150.00 USD |
| `1D` | `274.50` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 195,280.00 USD | 71,370.00 USD | 111,420.00 USD |
| `7D` | `274.50` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,420.00 USD |
| `1D` | `274.90` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 57,970.00 USD | 37,710.00 USD | 53,710.00 USD |
| `7D` | `274.90` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,910.00 USD |
| `1D` | `275.30` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD |
| `7D` | `275.30` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,390.00 USD |
| `1D` | `275.70` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 12,170.00 USD | 37,310.00 USD | 8,730.00 USD |
| `7D` | `275.70` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 1,350.00 USD | 51,050.00 USD | 11.36 USD |
| `1D` | `276.10` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 82,210.00 USD | 48,180.00 USD | 22,040.00 USD |
| `7D` | `276.10` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.50` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 27,970.00 USD | 31,830.00 USD | 3,230.00 USD |
| `7D` | `276.50` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 485.90 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 10,750.00 USD | 20,770.00 USD | 11,360.00 USD |
| `7D` | `276.90` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,830.00 USD |
| `1D` | `277.30` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 28,530.00 USD | 66,900.00 USD | 50,910.00 USD |
| `7D` | `277.30` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD |
| `1D` | `277.70` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 57,640.00 USD | 47,660.00 USD | 23,950.00 USD |
| `7D` | `277.70` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 27,190.00 USD | 55,800.00 USD |
| `1D` | `278.10` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD |
| `7D` | `278.10` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 24,750.00 USD | 0.00 USD | 59,500.00 USD |
| `1D` | `278.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 67,950.00 USD | 33,500.00 USD | 29,220.00 USD |
| `7D` | `278.50` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 17,440.00 USD | 71,230.00 USD | 0.00 USD |
| `1D` | `278.90` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 24,100.00 USD | 27,270.00 USD | 10,340.00 USD |
| `7D` | `278.90` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 42,950.00 USD | 32,690.00 USD | 17,140.00 USD |
| `1D` | `279.30` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 53,390.00 USD | 33,630.00 USD | 44,020.00 USD |
| `7D` | `279.30` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD |
| `1D` | `279.70` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 20,320.00 USD | 0.00 USD | 13,960.00 USD |
| `7D` | `279.70` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 46,800.00 USD | 0.00 USD | 54,370.00 USD |
| `1D` | `280.10` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD |
| `1D` | `280.50` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD |
| `1D` | `280.90` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 21,660.00 USD |
| `7D` | `280.90` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD |
| `1D` | `281.30` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.30` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.70` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 9,360.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `281.70` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 55,330.00 USD | 39,110.00 USD | 187,730.00 USD |
| `7D` | `282.10` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 133,750.00 USD |
| `1D` | `282.50` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 13,450.00 USD | 3,640.00 USD |
| `7D` | `282.50` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 32,190.00 USD | 0.00 USD | 39,740.00 USD |
| `1D` | `282.90` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 38,030.00 USD | 54,510.00 USD | 80,600.00 USD |
| `7D` | `282.90` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 117.84 USD |
| `1D` | `283.30` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 18,430.00 USD | 0.00 USD | 112,590.00 USD |
| `7D` | `283.30` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 37,310.00 USD | 89,370.00 USD |
| `1D` | `283.70` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 30,480.00 USD | 51,990.00 USD |
| `7D` | `283.70` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 181,750.00 USD |
| `1D` | `284.10` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD |
| `7D` | `284.10` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `284.50` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 39,670.00 USD | 70,600.00 USD | 20,690.00 USD |
| `7D` | `284.50` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 26,130.00 USD | 198,780.00 USD | 34,150.00 USD |
| `1D` | `284.90` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD |
| `7D` | `284.90` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD |
| `1D` | `285.30` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 20,960.00 USD | 64,640.00 USD | 93,680.00 USD |
| `7D` | `285.30` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD |
| `1D` | `285.70` | 831,490.00 USD | 0.00 USD | 831,490.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD |
| `7D` | `285.70` | 910,340.00 USD | 0.00 USD | 910,340.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD |
| `1D` | `286.10` | 668,860.00 USD | 0.00 USD | 668,860.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `7D` | `286.10` | 796,710.00 USD | 0.00 USD | 796,710.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD |
| `1D` | `286.50` | 638,860.00 USD | 0.00 USD | 638,860.00 USD | 111,830.00 USD | 47,210.00 USD | 37,510.00 USD |
| `7D` | `286.50` | 721,860.00 USD | 0.00 USD | 721,860.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 442,300.00 USD | 0.00 USD | 442,300.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD |
| `7D` | `286.90` | 602,420.00 USD | 0.00 USD | 602,420.00 USD | 27,530.00 USD | 141,160.00 USD | 0.00 USD |
| `1D` | `287.30` | 146,960.00 USD | 0.00 USD | 146,960.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD |
| `7D` | `287.30` | 433,730.00 USD | 0.00 USD | 433,730.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD |
| `1D` | `287.70` | 45,010.00 USD | 0.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `7D` | `287.70` | 293,550.00 USD | 0.00 USD | 293,550.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD |
| `1D` | `288.10` | 11,360.00 USD | 0.00 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD |
| `7D` | `288.10` | 139,290.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD |
| `7D` | `289.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.30` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `289.30` | 23,990.00 USD | 23,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.70` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD |
| `1D` | `290.90` | 23,990.00 USD | 23,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.40 USD |
| `1D` | `291.30` | 62,290.00 USD | 62,290.00 USD | 0.00 USD | 0.00 USD | 38,290.00 USD | 7.76 USD |
| `7D` | `291.30` | 11,120.00 USD | 11,120.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `291.70` | 100,060.00 USD | 100,060.00 USD | 0.00 USD | 0.00 USD | 15,650.00 USD | 22,120.00 USD |
| `7D` | `291.70` | 105,210.00 USD | 105,210.00 USD | 0.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD |
| `1D` | `292.10` | 138,430.00 USD | 138,430.00 USD | 0.00 USD | 0.00 USD | 38,360.00 USD | 9.06 USD |
| `7D` | `292.10` | 223,890.00 USD | 223,890.00 USD | 0.00 USD | 0.00 USD | 118,660.00 USD | 18.90 USD |
| `1D` | `292.50` | 185,800.00 USD | 185,800.00 USD | 0.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD |
| `7D` | `292.50` | 250,600.00 USD | 250,600.00 USD | 0.00 USD | 0.00 USD | 26,610.00 USD | 103.56 USD |
| `1D` | `292.90` | 268,060.00 USD | 268,060.00 USD | 0.00 USD | 1,020.00 USD | 81,240.00 USD | 3.04 USD |
| `7D` | `292.90` | 369,140.00 USD | 369,140.00 USD | 0.00 USD | 0.00 USD | 118,480.00 USD | 70.68 USD |
| `1D` | `293.30` | 329,130.00 USD | 329,130.00 USD | 0.00 USD | 476.80 USD | 60,590.00 USD | 1.58 USD |
| `7D` | `293.30` | 482,260.00 USD | 482,260.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 22.43 USD |
| `1D` | `293.70` | 540,820.00 USD | 540,820.00 USD | 0.00 USD | 73,230.00 USD | 77,060.00 USD | 61,390.00 USD |
| `7D` | `293.70` | 520,760.00 USD | 520,760.00 USD | 0.00 USD | 37,280.00 USD | 1,170.00 USD | 54.81 USD |
| `1D` | `294.10` | 636,360.00 USD | 636,360.00 USD | 0.00 USD | 30,790.00 USD | 36,360.00 USD | 28,400.00 USD |
| `7D` | `294.10` | 745,180.00 USD | 745,180.00 USD | 0.00 USD | 85,150.00 USD | 33,590.00 USD | 105,680.00 USD |
| `1D` | `294.50` | 985,350.00 USD | 985,350.00 USD | 0.00 USD | 148,680.00 USD | 108,350.00 USD | 91,970.00 USD |
| `7D` | `294.50` | 830,190.00 USD | 830,190.00 USD | 0.00 USD | 69,950.00 USD | 15,030.00 USD | 30.22 USD |
| `1D` | `294.90` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 53,910.00 USD | 79,400.00 USD | 105,170.00 USD |
| `7D` | `294.90` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 63,470.00 USD | 92,770.00 USD | 104,880.00 USD |
| `1D` | `295.30` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 95,260.00 USD | 75,850.00 USD | 85,290.00 USD |
| `7D` | `295.30` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 45,590.00 USD | 65,580.00 USD | 195,070.00 USD |
| `1D` | `295.70` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD |
| `7D` | `295.70` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 105,410.00 USD | 72,570.00 USD | 133,250.00 USD |
| `1D` | `296.10` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 90,530.00 USD | 119,980.00 USD | 29,580.00 USD |
| `7D` | `296.10` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 75,740.00 USD | 90,470.00 USD | 119,220.00 USD |
| `1D` | `296.50` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 43,030.00 USD | 34,820.00 USD | 43,490.00 USD |
| `7D` | `296.50` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 1,060.00 USD | 77,140.00 USD | 57,020.00 USD |
| `1D` | `296.90` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 29,430.00 USD | 50,150.00 USD | 91,120.00 USD |
| `7D` | `296.90` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 206,840.00 USD | 51,220.00 USD | 134,620.00 USD |
| `1D` | `297.30` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 57,730.00 USD | 359.06 USD | 28,050.00 USD |
| `7D` | `297.30` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 3,960.00 USD | 2,500.00 USD | 5.22 USD |
| `1D` | `297.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 807.94 USD | 723.06 USD | 12,060.00 USD |
| `7D` | `297.70` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 144.38 USD | 56,790.00 USD | 34,680.00 USD |
| `1D` | `298.10` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 44,470.00 USD | 8,120.00 USD | 53,000.00 USD |
| `7D` | `298.10` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 49,240.00 USD | 80,820.00 USD | 54,850.00 USD |
| `1D` | `298.50` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 8,410.00 USD | 21,250.00 USD | 84,830.00 USD |
| `7D` | `298.50` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 12,660.00 USD | 48,060.00 USD |
| `1D` | `298.90` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 34,670.00 USD | 15,820.00 USD | 118,690.00 USD |
| `7D` | `298.90` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 70,090.00 USD | 993.25 USD | 40,000.00 USD |
| `1D` | `299.30` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 59,910.00 USD | 23,800.00 USD | 27,850.00 USD |
| `7D` | `299.30` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD |
| `1D` | `299.70` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 4,910.00 USD | 17,410.00 USD | 9,090.00 USD |
| `7D` | `299.70` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 5,310.00 USD | 7,720.00 USD | 19,850.00 USD |
| `1D` | `300.10` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 51,990.00 USD | 44,530.00 USD | 35,300.00 USD |
| `7D` | `300.10` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 51,500.00 USD | 2,470.00 USD | 58.36 USD |
| `1D` | `300.50` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 11,190.00 USD | 10,850.00 USD | 41,890.00 USD |
| `7D` | `300.50` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 866.20 USD | 36,230.00 USD | 19,760.00 USD |
| `1D` | `300.90` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 12,920.00 USD | 32,390.00 USD | 36,710.00 USD |
| `7D` | `300.90` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 24,730.00 USD | 34,630.00 USD | 55,890.00 USD |
| `1D` | `301.30` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD |
| `7D` | `301.30` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 71,140.00 USD | 55,420.00 USD | 94,690.00 USD |
| `1D` | `301.70` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 31,990.00 USD | 20,360.00 USD | 16,730.00 USD |
| `7D` | `301.70` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 37,640.00 USD | 130,520.00 USD | 107.42 USD |
| `1D` | `302.10` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 44,680.00 USD | 37,100.00 USD | 10,340.00 USD |
| `7D` | `302.10` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 53,220.00 USD | 123,390.00 USD | 26,250.00 USD |
| `1D` | `302.50` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 10,520.00 USD | 20,540.00 USD | 31,130.00 USD |
| `7D` | `302.50` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 31,330.00 USD | 102,200.00 USD | 41,720.00 USD |
| `1D` | `302.90` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 1,230.00 USD | 1,850.00 USD | 20,520.00 USD |
| `7D` | `302.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 40,380.00 USD | 64,640.00 USD | 90.12 USD |
| `1D` | `303.30` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 32,880.00 USD | 413.69 USD | 14,710.00 USD |
| `7D` | `303.30` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 96.05 USD |
| `1D` | `303.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD |
| `7D` | `303.70` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 17,370.00 USD | 8,710.00 USD | 24,680.00 USD |
| `1D` | `304.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 22,560.00 USD | 1,100.00 USD | 53,800.00 USD |
| `7D` | `304.10` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 5,440.00 USD | 1,950.00 USD | 122.16 USD |
| `1D` | `304.50` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 13,310.00 USD | 9,720.00 USD | 53,870.00 USD |
| `7D` | `304.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 3,480.00 USD | 11,110.00 USD | 112.34 USD |
| `1D` | `304.90` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 697.80 USD | 240.63 USD | 2.91 USD |
| `7D` | `304.90` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 34,680.00 USD | 18,990.00 USD | 8,370.00 USD |
| `1D` | `305.30` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 11,210.00 USD | 90.03 USD | 2,010.00 USD |
| `7D` | `305.30` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 162,420.00 USD | 128,450.00 USD | 117,040.00 USD |
| `1D` | `305.70` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 7,960.00 USD | 1,770.00 USD | 3,410.00 USD |
| `7D` | `305.70` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 82,270.00 USD | 18,170.00 USD | 17,470.00 USD |
| `1D` | `306.10` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 4,210.00 USD | 2,750.00 USD | 1,350.00 USD |
| `7D` | `306.10` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 22,930.00 USD | 68,220.00 USD | 46,120.00 USD |
| `1D` | `306.50` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 4,740.00 USD | 9,750.00 USD | 58.13 USD |
| `7D` | `306.50` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 30,150.00 USD | 41,830.00 USD | 65,840.00 USD |
| `1D` | `306.90` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 32,060.00 USD | 40,210.00 USD | 13,060.00 USD |
| `7D` | `306.90` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 58,810.00 USD | 50,570.00 USD | 57,640.00 USD |
| `1D` | `307.30` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 7,930.00 USD | 34,540.00 USD | 10,930.00 USD |
| `7D` | `307.30` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 34,320.00 USD | 123,720.00 USD | 83,200.00 USD |
| `1D` | `307.70` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 19,670.00 USD | 27,980.00 USD | 9,610.00 USD |
| `7D` | `307.70` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 84,930.00 USD | 74,370.00 USD | 23,980.00 USD |
| `1D` | `308.10` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD |
| `7D` | `308.10` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 106,040.00 USD | 63,640.00 USD | 106,890.00 USD |
| `1D` | `308.50` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 5,570.00 USD | 3,510.00 USD | 4,260.00 USD |
| `7D` | `308.50` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 118,090.00 USD | 64,440.00 USD | 65,520.00 USD |
| `1D` | `308.90` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 12,710.00 USD | 6,030.00 USD | 4,140.00 USD |
| `7D` | `308.90` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 60,660.00 USD | 31,940.00 USD | 19,790.00 USD |
| `1D` | `309.30` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD |
| `7D` | `309.30` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 27,920.00 USD | 26,240.00 USD | 36,580.00 USD |
| `1D` | `309.70` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD |
| `7D` | `309.70` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 40,410.00 USD | 132,660.00 USD | 153,310.00 USD |
| `1D` | `310.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 4,390.00 USD | 4,770.00 USD | 0.00 USD |
| `7D` | `310.10` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 34,250.00 USD | 63,360.00 USD | 62,830.00 USD |
| `1D` | `310.50` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD |
| `7D` | `310.50` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 68,560.00 USD | 73,280.00 USD | 22,000.00 USD |
| `1D` | `310.90` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,090.00 USD |
| `7D` | `310.90` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 35,670.00 USD | 30,720.00 USD | 3,900.00 USD |
| `1D` | `311.30` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 7,760.00 USD | 2,050.00 USD | 8,550.00 USD |
| `7D` | `311.30` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 84,180.00 USD | 65,480.00 USD | 47,650.00 USD |
| `1D` | `311.70` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 16,340.00 USD | 6,590.00 USD | 4.48 USD |
| `7D` | `311.70` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 34,040.00 USD | 11,430.00 USD | 31,800.00 USD |
| `1D` | `312.10` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 244.00 USD | 39.75 USD | 29.51 USD |
| `7D` | `312.10` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 46,850.00 USD | 1,100.00 USD | 24,210.00 USD |
| `1D` | `312.50` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 8,760.00 USD | 7,440.00 USD | 8,700.00 USD |
| `7D` | `312.50` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 19,540.00 USD | 22,180.00 USD | 49,770.00 USD |
| `1D` | `312.90` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 11,420.00 USD | 23.27 USD | 1.44 USD |
| `7D` | `312.90` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 30,100.00 USD |
| `1D` | `313.30` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 64,910.00 USD | 30,120.00 USD | 22,660.00 USD |
| `1D` | `313.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 8,340.00 USD | 86.80 USD | 6,390.00 USD |
| `7D` | `313.70` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 32,170.00 USD | 15,010.00 USD | 23,120.00 USD |
| `1D` | `314.10` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD | 3,420.00 USD |
| `7D` | `314.10` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 26,810.00 USD | 362.37 USD | 47,790.00 USD |
| `1D` | `314.50` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `314.50` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 48,630.00 USD | 307.60 USD | 24,540.00 USD |
| `1D` | `314.90` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `314.90` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 29,590.00 USD | 0.00 USD | 10,250.00 USD |
| `1D` | `315.30` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 32.50 USD | 144.50 USD | 6,170.00 USD |
| `7D` | `315.30` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 5,690.00 USD | 547.95 USD | 48.58 USD |
| `1D` | `315.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `315.70` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 9,200.00 USD | 50,270.00 USD | 48,150.00 USD |
| `1D` | `316.10` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 5,020.00 USD | 5,050.00 USD | 11,840.00 USD |
| `7D` | `316.10` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD |
| `1D` | `316.50` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 12,950.00 USD | 5,380.00 USD | 0.00 USD |
| `7D` | `316.50` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 16,120.00 USD | 20,630.00 USD | 18,370.00 USD |
| `1D` | `316.90` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 12,760.00 USD | 3,660.00 USD | 12,480.00 USD |
| `7D` | `316.90` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 101.25 USD |
| `1D` | `317.30` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 2,250.00 USD | 4,170.00 USD | 1,590.00 USD |
| `7D` | `317.30` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 14,540.00 USD | 748.91 USD | 102.12 USD |
| `1D` | `317.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 15,260.00 USD | 15,360.00 USD | 23,390.00 USD |
| `7D` | `317.70` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 620.15 USD | 265.17 USD | 88.33 USD |
| `1D` | `318.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 2,290.00 USD | 9,270.00 USD | 7,680.00 USD |
| `7D` | `318.10` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 22,250.00 USD | 9,100.00 USD | 142.18 USD |
| `1D` | `318.50` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 4,700.00 USD | 7,500.00 USD | 9,580.00 USD |
| `7D` | `318.50` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD |
| `1D` | `318.90` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD |
| `7D` | `318.90` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 10,270.00 USD | 17,970.00 USD | 23,820.00 USD |
| `1D` | `319.30` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 8,590.00 USD | 16,300.00 USD | 488.47 USD |
| `7D` | `319.30` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 18,060.00 USD | 5.68 USD |
| `1D` | `319.70` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `7D` | `319.70` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `1D` | `320.10` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 4,350.00 USD | 4,210.00 USD | 10,920.00 USD |
| `7D` | `320.10` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD |
| `1D` | `320.50` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `320.50` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 15,190.00 USD | 10,080.00 USD | 49.92 USD |
| `7D` | `320.90` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.30` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD |
| `7D` | `321.70` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD |
| `7D` | `322.10` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 22,940.00 USD | 8,290.00 USD | 6,210.00 USD |
| `7D` | `322.50` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 555.20 USD | 365.55 USD | 0.00 USD |
| `7D` | `322.90` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 16,590.00 USD | 5,630.00 USD | 0.48 USD |
| `7D` | `323.30` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 14,160.00 USD | 5,860.00 USD | 11,480.00 USD |
| `7D` | `323.70` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.10` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD |
| `7D` | `324.40` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `316.85M` | Total OI Tokens: `1,095,339.3 BCH`
  * 1h OI Change: `-0.11%` | 4h OI Change: `+2.77%` | 24h OI Change: `-1.23%`
  * Exchange Breakdown: Binance=`94.35M` | Bybit=`40.44M` | OKX=`24.88M` | Hyperliquid=`8.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.56K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0012%` | **USDT OKX** | `-0.0045%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0046%` |
| **USDT MEXC** | `0.0010%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0015%` | **USDT Bitget** | `0.0060%` |
| **CoinM Binance** | `0.0004%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `52.42%` | `47.58%` | `1.10` | 2,680,000.00 USD |
| `15M` | `Binance` | `59.5%` | `40.5%` | `1.47` | 724,030.00 USD |
| `15M` | `OKX` | `53.24%` | `46.76%` | `1.14` | 145,380.00 USD |
| `15M` | `Bybit` | `52.16%` | `47.84%` | `1.09` | 250,510.00 USD |
| `15M` | `KuCoin` | `47.01%` | `52.99%` | `0.89` | 17,300.00 USD |
| `15M` | `Gate` | `57.7%` | `42.3%` | `1.36` | 548,930.00 USD |
| `15M` | `Bitget` | `53.87%` | `46.13%` | `1.17` | 47,730.00 USD |
| `15M` | `BingX` | `64.67%` | `35.33%` | `1.83` | 477,190.00 USD |
| `15M` | `MEXC` | `66.94%` | `33.06%` | `2.02` | 96,020.00 USD |
| `15M` | `Bitunix` | `58.98%` | `41.02%` | `1.44` | 36,620.00 USD |
| `15M` | `Hyperliquid` | `25.84%` | `74.16%` | `0.35` | 6,630.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.65%` | `48.35%` | `1.07` | 28,640.00 USD |
| `15M` | `Crypto.com` | `50%` | `50%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 278,320.00 USD |
| `15M` | `HTX` | `38.82%` | `61.18%` | `0.63` | 641.82 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.14%` | `53.86%` | `0.86` | 6,380.00 USD |
| `15M` | `Aster` | `91.69%` | `8.31%` | `11.03` | 143.71 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `76.28%` | `23.72%` | `3.22` | 14,300.00 USD |
| `15M` | `Whale Positions` | `59.5%` | `40.5%` | `1.47` | 724,030.00 USD |
| `15M` | `Global Accounts` | `52.42%` | `47.58%` | `1.10` | 2,680,000.00 USD |
| `1H` | `BCH` | `52.14%` | `47.86%` | `1.09` | 12,570,000.00 USD |
| `1H` | `Binance` | `47.82%` | `52.18%` | `0.92` | 3,370,000.00 USD |
| `1H` | `OKX` | `49.75%` | `50.25%` | `0.99` | 1,240,000.00 USD |
| `1H` | `Bybit` | `46.9%` | `53.1%` | `0.88` | 945,150.00 USD |
| `1H` | `KuCoin` | `41.73%` | `58.27%` | `0.72` | 133,680.00 USD |
| `1H` | `Gate` | `47.41%` | `52.59%` | `0.90` | 1,770,000.00 USD |
| `1H` | `Bitget` | `61.13%` | `38.87%` | `1.57` | 257,290.00 USD |
| `1H` | `BingX` | `44.42%` | `55.58%` | `0.80` | 2,340,000.00 USD |
| `1H` | `MEXC` | `45.22%` | `54.78%` | `0.83` | 603,960.00 USD |
| `1H` | `Bitunix` | `51.43%` | `48.57%` | `1.06` | 167,110.00 USD |
| `1H` | `Hyperliquid` | `50.28%` | `49.72%` | `1.01` | 70,850.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.29%` | `50.71%` | `0.97` | 354,150.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.26%` | `0.74%` | `134.14` | 1,190,000.00 USD |
| `1H` | `HTX` | `33.51%` | `66.49%` | `0.50` | 53,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.15%` | `50.85%` | `0.97` | 30,340.00 USD |
| `1H` | `Aster` | `59.62%` | `40.38%` | `1.48` | 7,680.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0.39%` | `99.61%` | `0.00` | 29,080.00 USD |
| `1H` | `Whale Positions` | `47.82%` | `52.18%` | `0.92` | 3,370,000.00 USD |
| `1H` | `Global Accounts` | `52.14%` | `47.86%` | `1.09` | 12,570,000.00 USD |
| `4H` | `BCH` | `53.16%` | `46.84%` | `1.13` | 63,430,000.00 USD |
| `4H` | `Binance` | `48.51%` | `51.49%` | `0.94` | 19,660,000.00 USD |
| `4H` | `OKX` | `49.3%` | `50.7%` | `0.97` | 7,380,000.00 USD |
| `4H` | `Bybit` | `53.73%` | `46.27%` | `1.16` | 5,010,000.00 USD |
| `4H` | `KuCoin` | `45.28%` | `54.72%` | `0.83` | 523,350.00 USD |
| `4H` | `Gate` | `49.32%` | `50.68%` | `0.97` | 8,470,000.00 USD |
| `4H` | `Bitget` | `43.98%` | `56.02%` | `0.79` | 1,310,000.00 USD |
| `4H` | `BingX` | `46.47%` | `53.53%` | `0.87` | 9,360,000.00 USD |
| `4H` | `MEXC` | `50.94%` | `49.06%` | `1.04` | 1,640,000.00 USD |
| `4H` | `Bitunix` | `48.72%` | `51.28%` | `0.95` | 1,030,000.00 USD |
| `4H` | `Hyperliquid` | `55.35%` | `44.65%` | `1.24` | 405,480.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.4%` | `49.6%` | `1.02` | 2,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.35%` | `3.65%` | `26.40` | 5,690,000.00 USD |
| `4H` | `HTX` | `45.53%` | `54.47%` | `0.84` | 130,130.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.82%` | `57.18%` | `0.75` | 260,590.00 USD |
| `4H` | `Aster` | `66.62%` | `33.38%` | `2.00` | 117,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.1%` | `68.9%` | `0.45` | 52,230.00 USD |
| `4H` | `Whale Positions` | `48.51%` | `51.49%` | `0.94` | 19,660,000.00 USD |
| `4H` | `Global Accounts` | `53.16%` | `46.84%` | `1.13` | 63,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `287.25` | `286.10` | `287.25` | `288.25` | `284.09` | 2,685,023.61 USD | 1,441,619.22 USD | 1,243,404.38 USD | 198,214.84 USD | `+7.38%` | `22B / 9S` |
| `0:00 UTC` | `290.18` | `290.75` | `290.18` | `293.42` | `286.94` | 7,434,288.46 USD | 2,860,219.97 USD | 4,574,068.49 USD | -1,713,848.52 USD | `-23.05%` | `22B / 26S` |
| `5:00 UTC` | `290.33` | `290.07` | `290.33` | `290.97` | `289.12` | 2,596,782.25 USD | 1,062,961.61 USD | 1,533,820.64 USD | -470,859.04 USD | `-18.13%` | `12B / 36S` |
| `0:00 UTC` | `287.31` | `288.38` | `287.31` | `290.09` | `287.09` | 2,309,907.78 USD | 1,171,627.08 USD | 1,138,280.70 USD | 33,346.39 USD | `+1.44%` | `26B / 14S` |
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `290.00` | `289.14` | `290.00` | `290.24` | `288.04` | 1,415,488.00 USD | 804,419.88 USD | 611,068.12 USD | 193,351.76 USD | `+13.66%` | `22B / 10S` |
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `290.49` | `289.33` | `290.49` | `291.59` | `287.81` | 1,897,766.44 USD | 827,805.59 USD | 1,069,960.85 USD | -242,155.26 USD | `-12.76%` | `25B / 40S` |
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `289.06` | `289.00` | `289.94` | `288.28` | 870,309.17 USD | 536,785.18 USD | 333,523.99 USD | 203,261.19 USD | `+23.36%` | `41B / 29S` |

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
| `5m` | -20,610.00 USD | -202,530.00 USD | **`DISTRIBUTION`** |
| `15m` | 22,620.00 USD | 194,020.00 USD | **`ACCUMULATION`** |
| `30m` | 28,000.00 USD | -21,160.00 USD | **`ACCUMULATION`** |
| `1h` | -14,570.00 USD | 139,760.00 USD | **`ACCUMULATION`** |
| `2h` | -77,220.00 USD | -1,810,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 294,490.00 USD | -2,620,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 329,100.00 USD | -905,550.00 USD | **`DISTRIBUTION`** |
| `8h` | 202,280.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 232,690.00 USD | -3,030,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -874,420.00 USD | -8,720,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 206,120.00 USD | -12,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,160,000.00 USD | -136,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-20.61K` | 15m=`+22.62K` | 1h=`-14.57K` | 24h=`-874.42K`
* Futures Capital Netflows: 5m=`-202.53K` | 15m=`+194.02K` | 1h=`+139.76K` | 24h=`-8.72M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `273.03` (Risk Distance: `3.49` pts)
  * +2.5R Take Profit: `285.25`
  * Mathematical Lot Sizing: **`2.86 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.05` (Risk Distance: `3.49` pts)
  * +2.5R Take Profit: `278.83`
  * Mathematical Lot Sizing: **`2.86 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`291.11`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
