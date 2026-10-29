# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `275.10` | **Live Ask Quote**: `275.70` | **Mid Price**: `275.40`
- **Spread Points**: `600.00` | **Spread BPS**: `21.79 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `281.24` | VWAP Z-Score: `-1.04` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.08` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `38.44` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `296.34` | Lower -3.00σ Band: `266.13`
  * Upper +2.51σ Band: `293.88` | Lower -2.51σ Band: `268.60`
  * Upper +2.01σ Band: `291.36` | Lower -2.01σ Band: `271.12`
  * Upper +2.00σ Band: `291.31` | Lower -2.00σ Band: `271.17`
  * Upper +1.28σ Band: `287.68` | Lower -1.28σ Band: `274.79`
  * Upper +1.00σ Band: `286.27` | Lower -1.00σ Band: `276.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`277.78` | EMA-20=`280.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`282.13` (Slope: `+0.0000`) | EMA-100=`283.30`
  * Institutional Anchors: EMA-144=`283.92` | EMA-200=`284.32` (Slope: `-0.2061`) | EMA-233=`284.89`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`269.53` | Weekly High=`304.16` | Weekly Low=`269.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.33` (Distance: `-1.02%`)
  * Point of Control (POC) = `276.81` (Distance: `-0.47%`)
  * Value Area Low (VAL) = `273.70` (Distance: `+0.66%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.04` | Weekly POC=`278.88` | Weekly VAL=`274.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`279.40` | Low=`270.25`
  * London Session (08:00-16:00 UTC): High=`276.50` | Low=`274.30`
  * New York Session (13:00-21:00 UTC): High=`277.05` | Low=`273.75`
  * Initial Balance (First Hour): IB High=`276.23` | IB Low=`274.57`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `274.30` - `276.50`
  * Optimal Trade Entry (OTE 0.705): `275.95`
  * Structural Invalidation Anchor (0.786): `277.60`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `277.24` | `278.17` | `276.43` | `276.50` | `1,438` | 398,740.88 USD | -106,616.35 USD | `-26.74%` | -3,669,757.84 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `276.48` | `279.05` | `275.47` | `275.71` | `8,998` | 2,494,196.00 USD | 646,411.44 USD | `+25.92%` | -3,023,346.39 USD | `+1.92` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `275.70` | `275.70` | `275.34` | `275.40` | `77` | 21,171.57 USD | -7,978.23 USD | `-37.68%` | -3,031,324.63 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `277.64` | `280.00` | `277.15` | `277.18` | `6,900` | 1,923,752.33 USD | -588,753.54 USD | `-30.60%` | -4,195,976.13 USD | `-2.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `277.17` | `278.91` | `275.97` | `276.50` | `9,747` | 2,702,816.05 USD | 551,516.40 USD | `+20.41%` | -3,644,459.73 USD | `+1.89` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `276.48` | `279.05` | `275.34` | `275.40` | `9,075` | 2,515,387.67 USD | 638,413.11 USD | `+25.38%` | -3,006,046.62 USD | `+1.93` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `286.78` | `286.91` | `269.28` | `270.43` | `78,753` | 21,848,832.22 USD | -393,290.27 USD | `-1.80%` | -3,940,771.41 USD | `-0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `270.43` | `280.00` | `269.74` | `276.50` | `41,918` | 11,558,813.69 USD | 153,675.96 USD | `+1.33%` | -3,787,095.44 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `276.48` | `279.05` | `275.34` | `275.67` | `9,103` | 2,523,016.74 USD | 645,304.99 USD | `+25.58%` | -3,141,790.45 USD | `+1.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `275.67` | `129,774` | 35,930,662.65 USD | 405,690.69 USD | `+1.13%` | -3,004,567.11 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `275.67` | `129,774` | 35,930,662.65 USD | 405,690.69 USD | `+1.13%` | -3,004,567.11 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`275.40`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `2008` | `0x12d2...f97f` | `LONG` | 1,005,653.12 USD | `3,627,243,000,000.00` | `303.26` | `277.41` | `0.000000` | -94,346.22 USD | `-9.38%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `296.54` | 18,029.34 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 18.03K USD at 296.5400 USD [API] | `2026-10-28 13:04:31` |
| `ANNOUNCEMENT` | `INFO` | `296.49` | 10,023.14 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 10.02K USD at 296.4900 USD [API] | `2026-10-28 13:04:31` |
| `ANNOUNCEMENT` | `INFO` | `293.56` | 7,191.63 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 7.19K USD at 293.5600 USD [API] | `2026-10-28 14:18:38` |
| `ANNOUNCEMENT` | `INFO` | `283.81` | 394.50 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Short: 0.39K USD at 283.8100 USD [API] | `2026-10-28 17:26:15` |
| `ANNOUNCEMENT` | `INFO` | `284.26` | 6,655.10 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 6.66K USD at 284.2600 USD [API] | `2026-10-28 18:08:29` |
| `ANNOUNCEMENT` | `INFO` | `285.30` | 6,679.16 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.68K USD at 285.3000 USD [API] | `2026-10-28 18:36:16` |
| `ANNOUNCEMENT` | `INFO` | `301.89` | 1,148.69 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Long: 1.15K USD at 301.8900 USD [API] | `2026-10-28 09:30:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`296.94` (Vol: 125,300.00 USD, Dist: `+6.83%`) | Long MP=`265.31` (Vol: 91,700.00 USD, Dist: `--4.55%`)
  * 48H Horizon: Short MP=`294.42` (Vol: 176,100.00 USD, Dist: `+5.92%`) | Long MP=`265.28` (Vol: 91,700.00 USD, Dist: `--4.56%`)
  * 3D Horizon: Short MP=`294.42` (Vol: 176,100.00 USD, Dist: `+5.92%`) | Long MP=`268.96` (Vol: 98,600.00 USD, Dist: `--3.24%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+5.90%`) | Long MP=`263.68` (Vol: 277,800.00 USD, Dist: `--5.14%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `81.50` | 584.76 USD | 418,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,130.00 USD | 418,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 417,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 151.41 USD | 416,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 972.47 USD | 415,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 415,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 408,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 404,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 404,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 175.66 USD | 404,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 404,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 1,790.00 USD | 403,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 1,930.00 USD | 402,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 400,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 399,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 398,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 395,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 395,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 648.73 USD | 395,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `169.50` | 8,470.00 USD | 394,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 385,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 385,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 385,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 384,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 2,030.00 USD | 384,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 382,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 381,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 381,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 380,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 7,540.00 USD | 379,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 371,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 370,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 370,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 39,880.00 USD | 370,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 330,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 619.50 USD | 330,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `207.50` | 188,820.00 USD | 329,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 6,740.00 USD | 140,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 134,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 130,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `218.50` | 626.88 USD | 129,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 2,300.00 USD | 129,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 127,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `225.50` | 5,370.00 USD | 94,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 88,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 87,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 2,050.00 USD | 87,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,300.00 USD | 85,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 84,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 1,010.00 USD | 83,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 82,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `235.50` | 6,140.00 USD | 82,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 76,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.40` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 7.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `240.50` | 612.79 USD | 75,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.90` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.40` | 12,680,000.00 USD | 12,680,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 367.32 USD | 74,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 12,670,000.00 USD | 12,670,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 12,650,000.00 USD | 12,650,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 74,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.90` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.40` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 9,910.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 72,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `243.80` | 4,690,000.00 USD | 4,690,000.00 USD | 1,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.90` | 12,570,000.00 USD | 12,570,000.00 USD | 781.30 USD | 0.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `244.20` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 71,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `244.60` | 4,680,000.00 USD | 4,680,000.00 USD | 638.70 USD | 5,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.90` | 12,550,000.00 USD | 12,550,000.00 USD | 836.88 USD | 17,320.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `245.00` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `245.40` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.40` | 12,530,000.00 USD | 12,530,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 67,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.90` | 12,510,000.00 USD | 12,510,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.20` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 5,540.00 USD | 6.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 12,490,000.00 USD | 12,490,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.90` | 12,460,000.00 USD | 12,460,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.00` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.40` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 2,370.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.40` | 12,450,000.00 USD | 12,450,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 66,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.80` | 4,640,000.00 USD | 4,640,000.00 USD | 330.05 USD | 619.60 USD | 5.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.90` | 12,410,000.00 USD | 12,410,000.00 USD | 789.37 USD | 4,610.00 USD | 30.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.20` | 4,640,000.00 USD | 4,640,000.00 USD | 10,640.00 USD | 0.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 12,410,000.00 USD | 12,410,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.60` | 4,600,000.00 USD | 4,600,000.00 USD | 7,480.00 USD | 3,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 12,360,000.00 USD | 12,360,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.00` | 4,590,000.00 USD | 4,590,000.00 USD | 3,780.00 USD | 9,620.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.40` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 1.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.40` | 12,270,000.00 USD | 12,270,000.00 USD | 49,060.00 USD | 28,020.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.80` | 4,550,000.00 USD | 4,550,000.00 USD | 10,830.00 USD | 1,230.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 12,190,000.00 USD | 12,190,000.00 USD | 44,990.00 USD | 28,830.00 USD | 35,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.20` | 4,530,000.00 USD | 4,530,000.00 USD | 11,880.00 USD | 5,410.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 12,080,000.00 USD | 12,080,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 65,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.60` | 4,520,000.00 USD | 4,520,000.00 USD | 3,610.00 USD | 3,270.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.90` | 12,000,000.00 USD | 12,000,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.00` | 4,510,000.00 USD | 4,510,000.00 USD | 28,660.00 USD | 41,480.00 USD | 11,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.40` | 4,430,000.00 USD | 4,430,000.00 USD | 11,230.00 USD | 26,760.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 11,910,000.00 USD | 11,910,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 64,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.80` | 4,360,000.00 USD | 4,360,000.00 USD | 41,550.00 USD | 49,340.00 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 11,740,000.00 USD | 11,740,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.20` | 4,260,000.00 USD | 4,260,000.00 USD | 20,950.00 USD | 7,380.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 11,570,000.00 USD | 11,570,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 26,370.00 USD | 64,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.60` | 4,210,000.00 USD | 4,210,000.00 USD | 10,340.00 USD | 92.40 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 11,430,000.00 USD | 11,430,000.00 USD | 29,220.00 USD | 19,580.00 USD | 64.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.00` | 4,200,000.00 USD | 4,200,000.00 USD | 10,280.00 USD | 15,070.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.40` | 4,170,000.00 USD | 4,170,000.00 USD | 21,310.00 USD | 16,680.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 11,380,000.00 USD | 11,380,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.80` | 4,120,000.00 USD | 4,120,000.00 USD | 1,670.00 USD | 8,890.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 11,260,000.00 USD | 11,260,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.20` | 4,100,000.00 USD | 4,100,000.00 USD | 144.00 USD | 2,130.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 11,200,000.00 USD | 11,200,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 37,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.60` | 4,100,000.00 USD | 4,100,000.00 USD | 994.06 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 11,110,000.00 USD | 11,110,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.00` | 4,090,000.00 USD | 4,090,000.00 USD | 9,680.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.40` | 4,070,000.00 USD | 4,070,000.00 USD | 244.00 USD | 1,090.00 USD | 11.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 11,060,000.00 USD | 11,060,000.00 USD | 51,710.00 USD | 11,830.00 USD | 23,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.80` | 4,070,000.00 USD | 4,070,000.00 USD | 13,410.00 USD | 7,270.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 10,970,000.00 USD | 10,970,000.00 USD | 16,050.00 USD | 30,780.00 USD | 37,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.20` | 4,050,000.00 USD | 4,050,000.00 USD | 11,210.00 USD | 4,120.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 10,890,000.00 USD | 10,890,000.00 USD | 88,910.00 USD | 20,980.00 USD | 37,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 453.49 USD | 37,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.60` | 4,030,000.00 USD | 4,030,000.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 10,740,000.00 USD | 10,740,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.00` | 4,020,000.00 USD | 4,020,000.00 USD | 494.83 USD | 928.93 USD | 3,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.40` | 4,010,000.00 USD | 4,010,000.00 USD | 6,290.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 10,640,000.00 USD | 10,640,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 36,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.80` | 4,000,000.00 USD | 4,000,000.00 USD | 32.50 USD | 2,440.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 10,570,000.00 USD | 10,570,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.20` | 3,990,000.00 USD | 3,990,000.00 USD | 5,030.00 USD | 3,750.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 10,510,000.00 USD | 10,510,000.00 USD | 137,820.00 USD | 54,900.00 USD | 51,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 36,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.60` | 3,970,000.00 USD | 3,970,000.00 USD | 3,450.00 USD | 14.47 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 10,270,000.00 USD | 10,270,000.00 USD | 60,610.00 USD | 3,500.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.00` | 3,960,000.00 USD | 3,960,000.00 USD | 11,160.00 USD | 7,340.00 USD | 11.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.40` | 3,950,000.00 USD | 3,950,000.00 USD | 5,040.00 USD | 2,530.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 10,170,000.00 USD | 10,170,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.80` | 3,930,000.00 USD | 3,930,000.00 USD | 13,420.00 USD | 11,230.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 10,110,000.00 USD | 10,110,000.00 USD | 19,140.00 USD | 12,520.00 USD | 98.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.20` | 3,880,000.00 USD | 3,880,000.00 USD | 6,870.00 USD | 16,660.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 10,080,000.00 USD | 10,080,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 36,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.60` | 3,850,000.00 USD | 3,850,000.00 USD | 357.42 USD | 13,560.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 9,960,000.00 USD | 9,960,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.00` | 3,830,000.00 USD | 3,830,000.00 USD | 8,050.00 USD | 18,010.00 USD | 44,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.40` | 3,760,000.00 USD | 3,760,000.00 USD | 9,410.00 USD | 16,080.00 USD | 514.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 9,840,000.00 USD | 9,840,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `261.50` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `261.80` | 3,730,000.00 USD | 3,730,000.00 USD | 4,510.00 USD | 6,650.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 9,740,000.00 USD | 9,740,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.20` | 3,690,000.00 USD | 3,690,000.00 USD | 8,900.00 USD | 4,380.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 9,580,000.00 USD | 9,580,000.00 USD | 44,640.00 USD | 52,560.00 USD | 32.59 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,270.00 USD | 32,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.60` | 3,670,000.00 USD | 3,670,000.00 USD | 366.04 USD | 1,300.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 9,490,000.00 USD | 9,490,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.00` | 3,670,000.00 USD | 3,670,000.00 USD | 8,670.00 USD | 13,360.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.40` | 3,640,000.00 USD | 3,640,000.00 USD | 215.89 USD | 3,940.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 9,340,000.00 USD | 9,340,000.00 USD | 100,770.00 USD | 30,720.00 USD | 50,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `263.50` | 2,900.00 USD | 31,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `263.80` | 3,620,000.00 USD | 3,620,000.00 USD | 616.37 USD | 7,480.00 USD | 24,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 9,160,000.00 USD | 9,160,000.00 USD | 287,090.00 USD | 98,240.00 USD | 57,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.20` | 3,590,000.00 USD | 3,590,000.00 USD | 2,010.00 USD | 666.33 USD | 7.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 8,720,000.00 USD | 8,720,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 28,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.60` | 3,580,000.00 USD | 3,580,000.00 USD | 28,600.00 USD | 110.80 USD | 60,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 8,600,000.00 USD | 8,600,000.00 USD | 28,050.00 USD | 75,010.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.00` | 3,490,000.00 USD | 3,490,000.00 USD | 30,810.00 USD | 9,490.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.40` | 3,440,000.00 USD | 3,440,000.00 USD | 694.46 USD | 12,230.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 8,470,000.00 USD | 8,470,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.80` | 3,390,000.00 USD | 3,390,000.00 USD | 23,780.00 USD | 22,790.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 8,110,000.00 USD | 8,110,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.20` | 3,300,000.00 USD | 3,300,000.00 USD | 21,580.00 USD | 87.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 7,780,000.00 USD | 7,780,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.60` | 3,280,000.00 USD | 3,280,000.00 USD | 36,980.00 USD | 29,590.00 USD | 67,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 7,300,000.00 USD | 7,300,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.00` | 3,150,000.00 USD | 3,150,000.00 USD | 26,590.00 USD | 25,650.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.40` | 3,090,000.00 USD | 3,090,000.00 USD | 14,480.00 USD | 26,770.00 USD | 56,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 6,820,000.00 USD | 6,820,000.00 USD | 119,030.00 USD | 209,120.00 USD | 96,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 195.01 USD | 27,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.80` | 2,990,000.00 USD | 2,990,000.00 USD | 96,650.00 USD | 116,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 6,390,000.00 USD | 6,390,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.20` | 2,740,000.00 USD | 2,740,000.00 USD | 41,920.00 USD | 123,890.00 USD | 47,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 5,780,000.00 USD | 5,780,000.00 USD | 176,940.00 USD | 325,150.00 USD | 99,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.60` | 2,530,000.00 USD | 2,530,000.00 USD | 115,220.00 USD | 107,040.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 5,180,000.00 USD | 5,180,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.00` | 2,270,000.00 USD | 2,270,000.00 USD | 77,550.00 USD | 26,120.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.40` | 2,120,000.00 USD | 2,120,000.00 USD | 20,200.00 USD | 18,120.00 USD | 44,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 4,670,000.00 USD | 4,670,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 27,790.00 USD | 27,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.80` | 2,040,000.00 USD | 2,040,000.00 USD | 34,240.00 USD | 21,490.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 4,110,000.00 USD | 4,110,000.00 USD | 74,250.00 USD | 141,330.00 USD | 145.08 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.20` | 1,970,000.00 USD | 1,970,000.00 USD | 120,570.00 USD | 21,550.00 USD | 144,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 3,890,000.00 USD | 3,890,000.00 USD | 118,110.00 USD | 0.00 USD | 95.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `270.50` | 592.94 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.60` | 1,680,000.00 USD | 1,680,000.00 USD | 78,270.00 USD | 0.00 USD | 61,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 3,770,000.00 USD | 3,770,000.00 USD | 328,250.00 USD | 0.00 USD | 36.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.00` | 1,540,000.00 USD | 1,540,000.00 USD | 25,020.00 USD | 0.00 USD | 76,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.40` | 1,440,000.00 USD | 1,440,000.00 USD | 46,900.00 USD | 0.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 3,440,000.00 USD | 3,440,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.80` | 1,320,000.00 USD | 1,320,000.00 USD | 55,090.00 USD | 0.00 USD | 7.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 3,290,000.00 USD | 3,290,000.00 USD | 475,090.00 USD | 0.00 USD | 158.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.20` | 1,270,000.00 USD | 1,270,000.00 USD | 102,590.00 USD | 81.40 USD | 5.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 2,820,000.00 USD | 2,820,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.60` | 1,160,000.00 USD | 1,160,000.00 USD | 76,790.00 USD | 447.70 USD | 9.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 2,540,000.00 USD | 2,540,000.00 USD | 150,960.00 USD | 0.00 USD | 15,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.00` | 1,090,000.00 USD | 1,090,000.00 USD | 68,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.40` | 1,020,000.00 USD | 1,020,000.00 USD | 217,920.00 USD | 73.70 USD | 53,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 2,370,000.00 USD | 2,370,000.00 USD | 379,280.00 USD | 0.00 USD | 163,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.80` | 746,260.00 USD | 746,260.00 USD | 103,540.00 USD | 0.00 USD | 57,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 1,830,000.00 USD | 1,830,000.00 USD | 375,450.00 USD | 0.00 USD | 257.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.20` | 584,770.00 USD | 584,770.00 USD | 228,980.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 1,450,000.00 USD | 1,450,000.00 USD | 496,740.00 USD | 248,170.00 USD | 132.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.60` | 355,780.00 USD | 355,780.00 USD | 166,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 709,080.00 USD | 709,080.00 USD | 348,470.00 USD | 202,210.00 USD | 159.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.00` | 188,980.00 USD | 188,980.00 USD | 33,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.40` | 158,240.00 USD | 158,240.00 USD | 3,530.00 USD | 126,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.80` | 155,050.00 USD | 155,050.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.90` | 27,810.00 USD | 27,810.00 USD | 2,560.00 USD | 25,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.20` | 123,170.00 USD | 123,170.00 USD | 0.00 USD | 36,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.40` | 106,230.00 USD | 106,230.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.40` | 212,450.00 USD | 212,450.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.60` | 86,350.00 USD | 86,350.00 USD | 0.00 USD | 48,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.90` | 281,040.00 USD | 281,040.00 USD | 45,560.00 USD | 22,950.00 USD | 79.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.00` | 37,400.00 USD | 37,400.00 USD | 0.00 USD | 37,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `277.40` | 168,480.00 USD | 168,480.00 USD | 42,360.00 USD | 64,450.00 USD | 61,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.40` | 344,330.00 USD | 344,330.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `277.50` | 1,380.00 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `277.80` | 224,520.00 USD | 224,520.00 USD | 44,920.00 USD | 11,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.90` | 430,020.00 USD | 430,020.00 USD | 0.00 USD | 85,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.20` | 294,060.00 USD | 294,060.00 USD | 30,830.00 USD | 0.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.40` | 481,140.00 USD | 481,140.00 USD | 24,750.00 USD | 26,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.60` | 361,380.00 USD | 361,380.00 USD | 37,120.00 USD | 30,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 558,690.00 USD | 558,690.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.00` | 389,760.00 USD | 389,760.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.40` | 468,020.00 USD | 468,020.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.40` | 654,680.00 USD | 654,680.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.80` | 492,820.00 USD | 492,820.00 USD | 0.00 USD | 7,690.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.90` | 654,820.00 USD | 654,820.00 USD | 0.00 USD | 0.00 USD | 146.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.20` | 576,050.00 USD | 576,050.00 USD | 29,750.00 USD | 11,840.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.40` | 654,830.00 USD | 654,830.00 USD | 0.00 USD | 0.00 USD | 9.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.60` | 660,000.00 USD | 660,000.00 USD | 0.00 USD | 4,860.00 USD | 79,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.90` | 654,870.00 USD | 654,870.00 USD | 0.00 USD | 0.00 USD | 41.07 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.00` | 743,530.00 USD | 743,530.00 USD | 0.00 USD | 7,010.00 USD | 76,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.40` | 764,120.00 USD | 764,120.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 717,690.00 USD | 717,690.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.80` | 769,530.00 USD | 769,530.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.90` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 398,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.60` | 822,270.00 USD | 822,270.00 USD | 22,180.00 USD | 13,190.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.90` | 1,200,000.00 USD | 1,200,000.00 USD | 32,190.00 USD | 0.00 USD | 7.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.00` | 1,030,000.00 USD | 1,030,000.00 USD | 71,390.00 USD | 5,570.00 USD | 126,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.40` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 66,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 66,560.00 USD | 146,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.80` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 45,780.00 USD | 47,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.90` | 1,780,000.00 USD | 1,780,000.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.20` | 1,370,000.00 USD | 1,370,000.00 USD | 38,980.00 USD | 50,430.00 USD | 97,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 1,940,000.00 USD | 1,940,000.00 USD | 27,700.00 USD | 89,730.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `284.50` | 8,520.00 USD | 13,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `284.60` | 1,510,000.00 USD | 1,510,000.00 USD | 49,080.00 USD | 67,500.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 2,390,000.00 USD | 2,390,000.00 USD | 67,050.00 USD | 391,180.00 USD | 114.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.00` | 1,590,000.00 USD | 1,590,000.00 USD | 20,960.00 USD | 0.00 USD | 54,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.40` | 1,910,000.00 USD | 1,910,000.00 USD | 117,450.00 USD | 125,760.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 2,740,000.00 USD | 2,740,000.00 USD | 64,060.00 USD | 193,790.00 USD | 83,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.80` | 2,000,000.00 USD | 2,000,000.00 USD | 40,630.00 USD | 33,170.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 2,830,000.00 USD | 2,830,000.00 USD | 1,200.00 USD | 97,960.00 USD | 7.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 137,400.00 USD | 32.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.60` | 2,030,000.00 USD | 2,030,000.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 3,160,000.00 USD | 3,160,000.00 USD | 51,390.00 USD | 141,160.00 USD | 61.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.00` | 2,240,000.00 USD | 2,240,000.00 USD | 31,110.00 USD | 99,880.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.40` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 29,800.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 3,380,000.00 USD | 3,380,000.00 USD | 53,620.00 USD | 103,430.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 152.66 USD | 13,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.80` | 2,360,000.00 USD | 2,360,000.00 USD | 9,030.00 USD | 9,240.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.20` | 2,390,000.00 USD | 2,390,000.00 USD | 11,090.00 USD | 10,810.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.40` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 3.86 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 5,770.00 USD | 19,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 3,650,000.00 USD | 3,650,000.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.00` | 2,410,000.00 USD | 2,410,000.00 USD | 1,540.00 USD | 14,290.00 USD | 11.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.40` | 2,420,000.00 USD | 2,420,000.00 USD | 664.77 USD | 6,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 927.80 USD | 52.62 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `289.50` | 2,250.00 USD | 21,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `289.80` | 2,430,000.00 USD | 2,430,000.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 1,990.00 USD | 14.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 3,690,000.00 USD | 3,690,000.00 USD | 34,580.00 USD | 0.00 USD | 34.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 305.70 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 3,690,000.00 USD | 3,690,000.00 USD | 898.13 USD | 861.99 USD | 55.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.00` | 2,490,000.00 USD | 2,490,000.00 USD | 32,650.00 USD | 6,700.00 USD | 3.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.40` | 2,510,000.00 USD | 2,510,000.00 USD | 562.74 USD | 21,420.00 USD | 14.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 55,720.00 USD | 55.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.80` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 6,460.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 120,730.00 USD | 52.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.20` | 2,600,000.00 USD | 2,600,000.00 USD | 10,080.00 USD | 40,470.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 71,940.00 USD | 43.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.60` | 2,680,000.00 USD | 2,680,000.00 USD | 22,800.00 USD | 60,150.00 USD | 10.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 119,560.00 USD | 13.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.00` | 2,750,000.00 USD | 2,750,000.00 USD | 10,970.00 USD | 47,730.00 USD | 13,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.40` | 2,840,000.00 USD | 2,840,000.00 USD | 10,610.00 USD | 51,670.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 4,170,000.00 USD | 4,170,000.00 USD | 534.50 USD | 112,560.00 USD | 198.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.80` | 3,020,000.00 USD | 3,020,000.00 USD | 88,720.00 USD | 43,910.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 4,290,000.00 USD | 4,290,000.00 USD | 51,570.00 USD | 20,910.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.20` | 3,150,000.00 USD | 3,150,000.00 USD | 27,810.00 USD | 48,520.00 USD | 56,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 4,510,000.00 USD | 4,510,000.00 USD | 139,780.00 USD | 14,550.00 USD | 60,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.60` | 3,440,000.00 USD | 3,440,000.00 USD | 120,380.00 USD | 90,270.00 USD | 85,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 4,780,000.00 USD | 4,780,000.00 USD | 64,510.00 USD | 107,870.00 USD | 104,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.00` | 3,550,000.00 USD | 3,550,000.00 USD | 19,910.00 USD | 47,160.00 USD | 39,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.40` | 3,740,000.00 USD | 3,740,000.00 USD | 29,300.00 USD | 104,750.00 USD | 59,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 5,220,000.00 USD | 5,220,000.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.80` | 3,920,000.00 USD | 3,920,000.00 USD | 83,280.00 USD | 26,280.00 USD | 69,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 5,620,000.00 USD | 5,620,000.00 USD | 107,830.00 USD | 133,090.00 USD | 150,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.20` | 4,120,000.00 USD | 4,120,000.00 USD | 83,160.00 USD | 83,110.00 USD | 29,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 5,840,000.00 USD | 5,840,000.00 USD | 27,680.00 USD | 77,570.00 USD | 120,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.60` | 4,200,000.00 USD | 4,200,000.00 USD | 43,250.00 USD | 12,140.00 USD | 20,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 6,270,000.00 USD | 6,270,000.00 USD | 207,350.00 USD | 50,930.00 USD | 172,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.00` | 4,300,000.00 USD | 4,300,000.00 USD | 1,400.00 USD | 20,940.00 USD | 78,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.40` | 4,370,000.00 USD | 4,370,000.00 USD | 57,480.00 USD | 879.58 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 6,370,000.00 USD | 6,370,000.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.80` | 4,400,000.00 USD | 4,400,000.00 USD | 2,180.00 USD | 6,230.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 6,480,000.00 USD | 6,480,000.00 USD | 17,770.00 USD | 39,840.00 USD | 55,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.20` | 4,540,000.00 USD | 4,540,000.00 USD | 55,290.00 USD | 4,610.00 USD | 84,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 6,630,000.00 USD | 6,630,000.00 USD | 32,250.00 USD | 42,710.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.60` | 4,630,000.00 USD | 4,630,000.00 USD | 24,810.00 USD | 7,720.00 USD | 61,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 6,750,000.00 USD | 6,750,000.00 USD | 70,090.00 USD | 12,780.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.00` | 4,710,000.00 USD | 4,710,000.00 USD | 13,220.00 USD | 16,220.00 USD | 46,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.40` | 4,790,000.00 USD | 4,790,000.00 USD | 35,490.00 USD | 17,080.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 6,810,000.00 USD | 6,810,000.00 USD | 4,470.00 USD | 13,080.00 USD | 45,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.80` | 4,850,000.00 USD | 4,850,000.00 USD | 12,870.00 USD | 12,440.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 6,900,000.00 USD | 6,900,000.00 USD | 56,210.00 USD | 10,220.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.20` | 4,960,000.00 USD | 4,960,000.00 USD | 34,830.00 USD | 29,170.00 USD | 43,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 6,900,000.00 USD | 6,900,000.00 USD | 866.20 USD | 1,190.00 USD | 147.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.60` | 5,010,000.00 USD | 5,010,000.00 USD | 11,460.00 USD | 22,740.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 7,100,000.00 USD | 7,100,000.00 USD | 24,730.00 USD | 70,210.00 USD | 104,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.00` | 5,070,000.00 USD | 5,070,000.00 USD | 8,670.00 USD | 27,670.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.40` | 5,140,000.00 USD | 5,140,000.00 USD | 950.24 USD | 33,440.00 USD | 34,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 7,320,000.00 USD | 7,320,000.00 USD | 71,890.00 USD | 56,010.00 USD | 94,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.80` | 5,200,000.00 USD | 5,200,000.00 USD | 19,450.00 USD | 31,100.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 7,620,000.00 USD | 7,620,000.00 USD | 89,300.00 USD | 185,430.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.20` | 5,250,000.00 USD | 5,250,000.00 USD | 30,090.00 USD | 16,310.00 USD | 5.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 7,750,000.00 USD | 7,750,000.00 USD | 1,560.00 USD | 125,480.00 USD | 152.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.60` | 5,310,000.00 USD | 5,310,000.00 USD | 11,270.00 USD | 11,110.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 7,980,000.00 USD | 7,980,000.00 USD | 71,700.00 USD | 110,480.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.00` | 5,350,000.00 USD | 5,350,000.00 USD | 20,640.00 USD | 1,820.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.40` | 5,390,000.00 USD | 5,390,000.00 USD | 10,970.00 USD | 176.02 USD | 30,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 173.09 USD | 154.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.80` | 5,400,000.00 USD | 5,400,000.00 USD | 7,850.00 USD | 3,590.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 8,050,000.00 USD | 8,050,000.00 USD | 21,140.00 USD | 11,010.00 USD | 45,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.20` | 5,480,000.00 USD | 5,480,000.00 USD | 21,670.00 USD | 5,150.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 8,070,000.00 USD | 8,070,000.00 USD | 3,670.00 USD | 11,280.00 USD | 154.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.60` | 5,550,000.00 USD | 5,550,000.00 USD | 13,310.00 USD | 4,900.00 USD | 53,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 8,130,000.00 USD | 8,130,000.00 USD | 36,160.00 USD | 18,990.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.00` | 5,560,000.00 USD | 5,560,000.00 USD | 697.80 USD | 43.93 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.40` | 5,570,000.00 USD | 5,570,000.00 USD | 10,950.00 USD | 1,640.00 USD | 2,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 8,540,000.00 USD | 8,540,000.00 USD | 163,900.00 USD | 127,450.00 USD | 119,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.80` | 5,590,000.00 USD | 5,590,000.00 USD | 12,080.00 USD | 5,750.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 8,690,000.00 USD | 8,690,000.00 USD | 82,000.00 USD | 55,480.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.20` | 5,600,000.00 USD | 5,600,000.00 USD | 3,900.00 USD | 3,330.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 8,850,000.00 USD | 8,850,000.00 USD | 39,250.00 USD | 55,740.00 USD | 66,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.60` | 5,620,000.00 USD | 5,620,000.00 USD | 4,420.00 USD | 11,690.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 9,110,000.00 USD | 9,110,000.00 USD | 84,850.00 USD | 64,520.00 USD | 102,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.00` | 5,710,000.00 USD | 5,710,000.00 USD | 31,810.00 USD | 38,740.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.40` | 5,760,000.00 USD | 5,760,000.00 USD | 4,290.00 USD | 31,200.00 USD | 13,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 9,390,000.00 USD | 9,390,000.00 USD | 46,230.00 USD | 154,680.00 USD | 83,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 6,360.00 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `307.80` | 5,850,000.00 USD | 5,850,000.00 USD | 41,630.00 USD | 37,370.00 USD | 14,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 9,690,000.00 USD | 9,690,000.00 USD | 136,380.00 USD | 101,120.00 USD | 65,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.20` | 5,890,000.00 USD | 5,890,000.00 USD | 21,090.00 USD | 7,500.00 USD | 15,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 10,020,000.00 USD | 10,020,000.00 USD | 152,590.00 USD | 50,070.00 USD | 125,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.60` | 5,900,000.00 USD | 5,900,000.00 USD | 5,550.00 USD | 167.90 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 10,150,000.00 USD | 10,150,000.00 USD | 61,600.00 USD | 52,230.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.00` | 5,920,000.00 USD | 5,920,000.00 USD | 11,380.00 USD | 6,400.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.40` | 5,950,000.00 USD | 5,950,000.00 USD | 9,920.00 USD | 14,000.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 10,260,000.00 USD | 10,260,000.00 USD | 28,000.00 USD | 35,530.00 USD | 46,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.80` | 5,980,000.00 USD | 5,980,000.00 USD | 13,710.00 USD | 11,430.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 10,600,000.00 USD | 10,600,000.00 USD | 59,490.00 USD | 131,460.00 USD | 144,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.20` | 6,000,000.00 USD | 6,000,000.00 USD | 1,670.00 USD | 8,920.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 10,880,000.00 USD | 10,880,000.00 USD | 78,770.00 USD | 123,340.00 USD | 76,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 28,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.60` | 6,010,000.00 USD | 6,010,000.00 USD | 144.00 USD | 2,370.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 10,950,000.00 USD | 10,950,000.00 USD | 35,670.00 USD | 35,930.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.00` | 6,010,000.00 USD | 6,010,000.00 USD | 134.35 USD | 0.00 USD | 0.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.40` | 6,020,000.00 USD | 6,020,000.00 USD | 940.26 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.40` | 11,160,000.00 USD | 11,160,000.00 USD | 89,390.00 USD | 65,750.00 USD | 47,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.80` | 6,030,000.00 USD | 6,030,000.00 USD | 9,260.00 USD | 6,590.00 USD | 4.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 11,220,000.00 USD | 11,220,000.00 USD | 40,320.00 USD | 11,160.00 USD | 13,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.20` | 6,030,000.00 USD | 6,030,000.00 USD | 244.00 USD | 234.60 USD | 1.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 11,330,000.00 USD | 11,330,000.00 USD | 45,640.00 USD | 22,970.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.60` | 6,060,000.00 USD | 6,060,000.00 USD | 13,410.00 USD | 7,270.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 11,420,000.00 USD | 11,420,000.00 USD | 22,600.00 USD | 20,090.00 USD | 47,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.00` | 6,070,000.00 USD | 6,070,000.00 USD | 11,210.00 USD | 0.00 USD | 0.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.40` | 6,080,000.00 USD | 6,080,000.00 USD | 7,160.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.40` | 11,550,000.00 USD | 11,550,000.00 USD | 66,180.00 USD | 30,120.00 USD | 30,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.80` | 6,090,000.00 USD | 6,090,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 11,650,000.00 USD | 11,650,000.00 USD | 44,540.00 USD | 15,370.00 USD | 35,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.20` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 11,750,000.00 USD | 11,750,000.00 USD | 51,980.00 USD | 307.60 USD | 51,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.60` | 6,110,000.00 USD | 6,110,000.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 11,800,000.00 USD | 11,800,000.00 USD | 39,410.00 USD | 0.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.00` | 6,110,000.00 USD | 6,110,000.00 USD | 32.50 USD | 1,400.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.40` | 6,120,000.00 USD | 6,120,000.00 USD | 3,750.00 USD | 144.50 USD | 0.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.40` | 11,840,000.00 USD | 11,840,000.00 USD | 6,160.00 USD | 9,920.00 USD | 18,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.80` | 6,130,000.00 USD | 6,130,000.00 USD | 1,370.00 USD | 3,040.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 11,950,000.00 USD | 11,950,000.00 USD | 47,110.00 USD | 41,400.00 USD | 29,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.20` | 6,140,000.00 USD | 6,140,000.00 USD | 2,100.00 USD | 3,070.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 12,070,000.00 USD | 12,070,000.00 USD | 16,580.00 USD | 40,320.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.60` | 6,150,000.00 USD | 6,150,000.00 USD | 11,090.00 USD | 3,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 12,090,000.00 USD | 12,090,000.00 USD | 3,030.00 USD | 10,840.00 USD | 107.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.00` | 6,170,000.00 USD | 6,170,000.00 USD | 3,590.00 USD | 2,190.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.40` | 6,180,000.00 USD | 6,180,000.00 USD | 3,720.00 USD | 1,960.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.40` | 12,100,000.00 USD | 12,100,000.00 USD | 14,540.00 USD | 1,010.00 USD | 118.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.50` | 6,180,000.00 USD | 6,180,000.00 USD | 5,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 12,130,000.00 USD | 12,130,000.00 USD | 21,640.00 USD | 8,200.00 USD | 111.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 12,190,000.00 USD | 12,190,000.00 USD | 3,320.00 USD | 27,530.00 USD | 22,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 28,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `318.90` | 12,250,000.00 USD | 12,250,000.00 USD | 11,180.00 USD | 17,970.00 USD | 37,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.40` | 12,270,000.00 USD | 12,270,000.00 USD | 733.55 USD | 18,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 12,300,000.00 USD | 12,300,000.00 USD | 446.22 USD | 22,230.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 12,380,000.00 USD | 12,380,000.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 29,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 166.45 USD | 1.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.40` | 12,430,000.00 USD | 12,430,000.00 USD | 13,640.00 USD | 17,870.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 12,440,000.00 USD | 12,440,000.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 12,480,000.00 USD | 12,480,000.00 USD | 22,930.00 USD | 7,950.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 12,500,000.00 USD | 12,500,000.00 USD | 16,590.00 USD | 5,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.40` | 12,540,000.00 USD | 12,540,000.00 USD | 14,160.00 USD | 11,950.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.90` | 12,540,000.00 USD | 12,540,000.00 USD | 269.10 USD | 692.00 USD | 27.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.90` | 12,590,000.00 USD | 12,590,000.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `325.40` | 12,640,000.00 USD | 12,640,000.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 29,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `337.50` | 1,350.00 USD | 31,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 32,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 32,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `379.50` | 41,740.00 USD | 74,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 83,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 129,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `477.50` | 8,200.00 USD | 137,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 138,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `66.50` | 434,190.00 USD | 0.00 USD | 251.37 USD | `-75.96%` | `3,780,000,000.00` |
| `Live` | `Long` | `75.50` | 433,940.00 USD | 0.00 USD | 541.71 USD | `-72.70%` | `7,175,000,000.00` |
| `Live` | `Long` | `95.50` | 433,400.00 USD | 0.00 USD | 920.05 USD | `-65.47%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 432,480.00 USD | 0.00 USD | 6,240.00 USD | `-63.30%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 426,240.00 USD | 0.00 USD | 4,080.00 USD | `-62.94%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 422,160.00 USD | 0.00 USD | 212.76 USD | `-60.41%` | `1,943,000,000.00` |
| `Live` | `Long` | `110.50` | 421,950.00 USD | 0.00 USD | 1,450.00 USD | `-60.05%` | `13,105,000,000.00` |
| `Live` | `Long` | `118.50` | 420,500.00 USD | 0.00 USD | 212.35 USD | `-57.15%` | `1,792,000,000.00` |
| `Live` | `Long` | `119.50` | 420,290.00 USD | 0.00 USD | 175.66 USD | `-56.79%` | `1,470,000,000.00` |
| `Live` | `Long` | `122.50` | 420,110.00 USD | 0.00 USD | 124.46 USD | `-55.71%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 419,990.00 USD | 0.00 USD | 856.66 USD | `-54.26%` | `6,772,000,000.00` |
| `Live` | `Long` | `131.50` | 419,130.00 USD | 0.00 USD | 1,970.00 USD | `-52.45%` | `15,000,000,000.00` |
| `Live` | `Long` | `141.50` | 417,160.00 USD | 0.00 USD | 157.49 USD | `-48.84%` | `1,113,000,000.00` |
| `Live` | `Long` | `147.50` | 417,000.00 USD | 0.00 USD | 895.47 USD | `-46.67%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 416,110.00 USD | 0.00 USD | 1,270.00 USD | `-46.31%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 414,840.00 USD | 0.00 USD | 2,370.00 USD | `-45.94%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 412,480.00 USD | 0.00 USD | 2,130.00 USD | `-44.86%` | `13,966,000,000.00` |
| `Live` | `Long` | `154.50` | 410,350.00 USD | 0.00 USD | 1,540.00 USD | `-44.14%` | `10,000,000,000.00` |
| `Live` | `Long` | `162.50` | 408,800.00 USD | 0.00 USD | 325.00 USD | `-41.24%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 408,480.00 USD | 0.00 USD | 8,660.00 USD | `-39.44%` | `51,706,000,000.00` |
| `Live` | `Long` | `169.50` | 399,820.00 USD | 0.00 USD | 367.31 USD | `-38.71%` | `2,167,000,000.00` |
| `Live` | `Long` | `170.50` | 399,450.00 USD | 0.00 USD | 426.25 USD | `-38.35%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 399,020.00 USD | 0.00 USD | 169.96 USD | `-36.91%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 398,850.00 USD | 0.00 USD | 904.53 USD | `-36.54%` | `5,154,000,000.00` |
| `Live` | `Long` | `176.50` | 397,950.00 USD | 0.00 USD | 373.83 USD | `-36.18%` | `2,118,000,000.00` |
| `Live` | `Long` | `181.50` | 397,570.00 USD | 0.00 USD | 1,990.00 USD | `-34.37%` | `10,974,000,000.00` |
| `Live` | `Long` | `183.50` | 395,580.00 USD | 0.00 USD | 191.57 USD | `-33.65%` | `1,044,000,000.00` |
| `Live` | `Long` | `184.50` | 395,390.00 USD | 0.00 USD | 616.05 USD | `-33.29%` | `3,339,000,000.00` |
| `Live` | `Long` | `188.50` | 394,770.00 USD | 0.00 USD | 418.28 USD | `-31.84%` | `2,219,000,000.00` |
| `Live` | `Long` | `191.50` | 394,360.00 USD | 0.00 USD | 858.49 USD | `-30.76%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 393,500.00 USD | 0.00 USD | 1,490.00 USD | `-30.40%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 392,010.00 USD | 0.00 USD | 370.47 USD | `-29.31%` | `1,895,000,000.00` |
| `Live` | `Long` | `199.50` | 391,640.00 USD | 0.00 USD | 548.03 USD | `-27.87%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 391,090.00 USD | 0.00 USD | 293.13 USD | `-27.50%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 390,800.00 USD | 0.00 USD | 420.39 USD | `-26.78%` | `2,076,000,000.00` |
| `Live` | `Long` | `203.50` | 390,380.00 USD | 0.00 USD | 610.50 USD | `-26.42%` | `3,000,000,000.00` |
| `Live` | `Long` | `204.50` | 389,770.00 USD | 0.00 USD | 39,880.00 USD | `-26.06%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 349,890.00 USD | 0.00 USD | 191.53 USD | `-25.70%` | `932,000,000.00` |
| `Live` | `Long` | `207.50` | 349,700.00 USD | 0.00 USD | 188,820.00 USD | `-24.97%` | `909,952,000,000.00` |
| `Live` | `Long` | `210.50` | 160,880.00 USD | 0.00 USD | 6,740.00 USD | `-23.89%` | `32,017,000,000.00` |
| `Live` | `Long` | `213.50` | 154,140.00 USD | 0.00 USD | 9,340.00 USD | `-22.80%` | `43,743,000,000.00` |
| `Live` | `Long` | `215.50` | 144,800.00 USD | 0.00 USD | 2,610.00 USD | `-22.08%` | `12,132,000,000.00` |
| `Live` | `Long` | `219.50` | 142,190.00 USD | 0.00 USD | 528.56 USD | `-20.63%` | `2,408,000,000.00` |
| `Live` | `Long` | `220.50` | 141,660.00 USD | 0.00 USD | 1,650.00 USD | `-20.27%` | `7,461,000,000.00` |
| `Live` | `Long` | `223.50` | 140,010.00 USD | 0.00 USD | 32,860.00 USD | `-19.19%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 107,150.00 USD | 0.00 USD | 561.25 USD | `-18.83%` | `2,500,000,000.00` |
| `Live` | `Long` | `225.50` | 106,590.00 USD | 0.00 USD | 5,370.00 USD | `-18.47%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 101,220.00 USD | 0.00 USD | 1,240.00 USD | `-18.10%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 99,990.00 USD | 0.00 USD | 288.24 USD | `-17.74%` | `1,267,000,000.00` |
| `Live` | `Long` | `228.50` | 99,700.00 USD | 0.00 USD | 1,260.00 USD | `-17.38%` | `5,532,000,000.00` |
| `Live` | `Long` | `229.50` | 98,440.00 USD | 0.00 USD | 1,190.00 USD | `-17.02%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 97,250.00 USD | 0.00 USD | 506.06 USD | `-16.30%` | `2,186,000,000.00` |
| `Live` | `Long` | `232.50` | 96,740.00 USD | 0.00 USD | 429.66 USD | `-15.93%` | `1,848,000,000.00` |
| `Live` | `Long` | `233.50` | 96,310.00 USD | 0.00 USD | 6,090.00 USD | `-15.57%` | `26,061,000,000.00` |
| `Live` | `Long` | `234.50` | 90,230.00 USD | 0.00 USD | 217.85 USD | `-15.21%` | `929,000,000.00` |
| `Live` | `Long` | `239.50` | 90,010.00 USD | 0.00 USD | 1,640.00 USD | `-13.40%` | `6,829,000,000.00` |
| `Live` | `Long` | `241.50` | 88,380.00 USD | 0.00 USD | 251.88 USD | `-12.68%` | `1,043,000,000.00` |
| `Live` | `Long` | `242.50` | 88,120.00 USD | 0.00 USD | 1,520.00 USD | `-12.32%` | `6,274,000,000.00` |
| `Live` | `Long` | `243.50` | 86,600.00 USD | 0.00 USD | 1,200.00 USD | `-11.96%` | `4,937,000,000.00` |
| `Live` | `Long` | `244.50` | 85,400.00 USD | 0.00 USD | 28,760.00 USD | `-11.60%` | `117,642,000,000.00` |
| `Live` | `Long` | `245.50` | 56,640.00 USD | 0.00 USD | 1,030.00 USD | `-11.23%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 55,610.00 USD | 0.00 USD | 699.44 USD | `-10.51%` | `2,826,000,000.00` |
| `Live` | `Long` | `250.50` | 54,910.00 USD | 0.00 USD | 1,330.00 USD | `-9.43%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 53,590.00 USD | 0.00 USD | 268.35 USD | `-9.06%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 53,320.00 USD | 0.00 USD | 1,030.00 USD | `-8.70%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 52,280.00 USD | 0.00 USD | 362.92 USD | `-7.98%` | `1,426,000,000.00` |
| `Live` | `Long` | `256.50` | 51,920.00 USD | 0.00 USD | 453.49 USD | `-7.26%` | `1,768,000,000.00` |
| `Live` | `Long` | `257.50` | 51,470.00 USD | 0.00 USD | 366.42 USD | `-6.90%` | `1,423,000,000.00` |
| `Live` | `Long` | `258.50` | 51,100.00 USD | 0.00 USD | 278.15 USD | `-6.53%` | `1,076,000,000.00` |
| `Live` | `Long` | `259.50` | 50,820.00 USD | 0.00 USD | 5,190.00 USD | `-6.17%` | `20,000,000,000.00` |
| `Live` | `Long` | `260.50` | 45,630.00 USD | 0.00 USD | 7,590.00 USD | `-5.81%` | `29,138,000,000.00` |
| `Live` | `Long` | `264.50` | 38,040.00 USD | 0.00 USD | 9,770.00 USD | `-4.36%` | `36,922,000,000.00` |
| `Live` | `Long` | `265.50` | 28,280.00 USD | 0.00 USD | 390.02 USD | `-4.00%` | `1,469,000,000.00` |
| `Live` | `Long` | `267.50` | 27,890.00 USD | 0.00 USD | 195.01 USD | `-3.28%` | `729,000,000.00` |
| `Live` | `Long` | `268.50` | 27,690.00 USD | 0.00 USD | 26,720.00 USD | `-2.92%` | `99,518,000,000.00` |
| `Live` | `Long` | `269.50` | 971.55 USD | 0.00 USD | 971.55 USD | `-2.56%` | `3,605,000,000.00` |
| `Live` | `Short` | `275.50` | 5,990.00 USD | 5,990.00 USD | 0.00 USD | `-0.39%` | `21,758,000,000.00` |
| `Live` | `Short` | `276.50` | 6,330.00 USD | 333.46 USD | 0.00 USD | `-0.03%` | `1,206,000,000.00` |
| `Live` | `Short` | `288.50` | 8,470.00 USD | 2,140.00 USD | 0.00 USD | `+4.31%` | `7,418,000,000.00` |
| `Live` | `Short` | `292.50` | 9,230.00 USD | 763.13 USD | 0.00 USD | `+5.76%` | `2,609,000,000.00` |
| `Live` | `Short` | `296.50` | 9,330.00 USD | 102.59 USD | 0.00 USD | `+7.21%` | `346,000,000.00` |
| `Live` | `Short` | `299.50` | 10,220.00 USD | 883.53 USD | 0.00 USD | `+8.29%` | `2,950,000,000.00` |
| `Live` | `Short` | `307.50` | 16,570.00 USD | 6,360.00 USD | 0.00 USD | `+11.18%` | `20,668,000,000.00` |
| `Live` | `Short` | `310.50` | 17,090.00 USD | 517.91 USD | 0.00 USD | `+12.27%` | `1,668,000,000.00` |
| `Live` | `Short` | `320.50` | 18,200.00 USD | 1,110.00 USD | 0.00 USD | `+15.88%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 18,470.00 USD | 276.63 USD | 0.00 USD | `+19.50%` | `837,000,000.00` |
| `Live` | `Short` | `340.50` | 19,840.00 USD | 1,360.00 USD | 0.00 USD | `+23.12%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 20,840.00 USD | 1,010.00 USD | 0.00 USD | `+29.62%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 21,290.00 USD | 445.52 USD | 0.00 USD | `+33.24%` | `1,209,000,000.00` |
| `Live` | `Short` | `373.50` | 62,370.00 USD | 41,090.00 USD | 0.00 USD | `+35.05%` | `110,000,000,000.00` |
| `Live` | `Short` | `387.50` | 62,860.00 USD | 487.86 USD | 0.00 USD | `+40.11%` | `1,259,000,000.00` |
| `Live` | `Short` | `432.50` | 71,670.00 USD | 8,810.00 USD | 0.00 USD | `+56.38%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 117,920.00 USD | 46,250.00 USD | 0.00 USD | `+66.14%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 126,120.00 USD | 8,200.00 USD | 0.00 USD | `+72.65%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 126,840.00 USD | 718.34 USD | 0.00 USD | `+80.24%` | `1,441,000,000.00` |
| `Live` | `Short` | `538.50` | 127,190.00 USD | 351.10 USD | 0.00 USD | `+94.71%` | `652,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 159,930.00 USD | 0.00 USD | 210.94 USD | `-48.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 159,710.00 USD | 0.00 USD | 2,070.00 USD | `-47.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 157,650.00 USD | 0.00 USD | 2,530.00 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 155,120.00 USD | 0.00 USD | 490.59 USD | `-33.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 154,630.00 USD | 0.00 USD | 482.01 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 154,150.00 USD | 0.00 USD | 189.07 USD | `-27.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 153,960.00 USD | 0.00 USD | 441.60 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 153,520.00 USD | 0.00 USD | 703.49 USD | `-23.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 152,810.00 USD | 0.00 USD | 715.29 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 152,100.00 USD | 0.00 USD | 638.36 USD | `-19.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 151,460.00 USD | 0.00 USD | 740.85 USD | `-18.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 150,720.00 USD | 0.00 USD | 1,050.00 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 149,670.00 USD | 0.00 USD | 389.48 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 149,280.00 USD | 0.00 USD | 812.38 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 148,470.00 USD | 0.00 USD | 220.64 USD | `-14.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 148,250.00 USD | 0.00 USD | 429.30 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 147,820.00 USD | 0.00 USD | 296.50 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 147,520.00 USD | 0.00 USD | 216.45 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 147,300.00 USD | 0.00 USD | 387.76 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 146,920.00 USD | 0.00 USD | 366.75 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 146,550.00 USD | 0.00 USD | 1,630.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 144,920.00 USD | 0.00 USD | 2,700.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 142,220.00 USD | 0.00 USD | 2,940.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 139,280.00 USD | 0.00 USD | 4,680.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 134,600.00 USD | 0.00 USD | 3,590.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 131,010.00 USD | 0.00 USD | 231.54 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 130,780.00 USD | 0.00 USD | 109.26 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 130,670.00 USD | 0.00 USD | 1,780.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 128,890.00 USD | 0.00 USD | 51,300.00 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 77,590.00 USD | 0.00 USD | 250.81 USD | `-6.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 77,340.00 USD | 0.00 USD | 468.90 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 76,870.00 USD | 0.00 USD | 857.85 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 76,010.00 USD | 0.00 USD | 7,790.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 68,220.00 USD | 0.00 USD | 122.99 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 68,090.00 USD | 0.00 USD | 2,180.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 65,920.00 USD | 0.00 USD | 241.98 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 65,670.00 USD | 0.00 USD | 4,490.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 61,180.00 USD | 0.00 USD | 6,440.00 USD | `-2.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 54,740.00 USD | 0.00 USD | 27,320.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 27,420.00 USD | 0.00 USD | 1,140.00 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 26,280.00 USD | 0.00 USD | 269.60 USD | `-1.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 26,010.00 USD | 0.00 USD | 13,500.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 12,510.00 USD | 0.00 USD | 1,470.00 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 11,050.00 USD | 0.00 USD | 9,840.00 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 1,200.00 USD | 0.00 USD | 299.74 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 903.60 USD | 0.00 USD | 903.60 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `277.50` | 384.34 USD | 384.34 USD | 0.00 USD | `+0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `278.50` | 510.22 USD | 125.88 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `279.50` | 22,500.00 USD | 21,990.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 25,870.00 USD | 3,370.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 26,000.00 USD | 133.43 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 27,300.00 USD | 1,300.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 35,340.00 USD | 8,040.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 37,350.00 USD | 2,010.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 45,040.00 USD | 7,690.00 USD | 0.00 USD | `+3.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 50,130.00 USD | 5,080.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 55,400.00 USD | 5,270.00 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 55,660.00 USD | 261.96 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 55,810.00 USD | 153.44 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 84,830.00 USD | 29,020.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 110,110.00 USD | 25,280.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 111,100.00 USD | 992.62 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 111,510.00 USD | 407.88 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 183,960.00 USD | 72,450.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 184,540.00 USD | 581.14 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 184,930.00 USD | 388.95 USD | 0.00 USD | `+7.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 194,610.00 USD | 9,690.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 205,340.00 USD | 10,730.00 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 207,990.00 USD | 2,650.00 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 209,050.00 USD | 1,060.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 209,150.00 USD | 102.73 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 223,650.00 USD | 14,500.00 USD | 0.00 USD | `+11.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 224,280.00 USD | 634.04 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 225,310.00 USD | 1,030.00 USD | 0.00 USD | `+14.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 230,960.00 USD | 5,650.00 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 231,080.00 USD | 118.85 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 231,620.00 USD | 534.59 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 231,940.00 USD | 321.50 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 296,860.00 USD | 64,920.00 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 297,950.00 USD | 1,090.00 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 309,950.00 USD | 12,000.00 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 310,490.00 USD | 547.52 USD | 0.00 USD | `+23.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 310,630.00 USD | 138.20 USD | 0.00 USD | `+24.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 310,890.00 USD | 257.45 USD | 0.00 USD | `+25.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 311,060.00 USD | 174.25 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 311,220.00 USD | 151.50 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 312,670.00 USD | 1,450.00 USD | 0.00 USD | `+29.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 314,440.00 USD | 1,770.00 USD | 0.00 USD | `+29.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 314,770.00 USD | 326.07 USD | 0.00 USD | `+30.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 315,600.00 USD | 826.60 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 323,040.00 USD | 7,440.00 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 323,720.00 USD | 682.84 USD | 0.00 USD | `+33.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 324,820.00 USD | 1,100.00 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 325,510.00 USD | 683.96 USD | 0.00 USD | `+43.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 325,710.00 USD | 199.75 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 328,170.00 USD | 2,470.00 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 329,210.00 USD | 1,040.00 USD | 0.00 USD | `+46.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 329,590.00 USD | 376.71 USD | 0.00 USD | `+46.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 329,750.00 USD | 158.86 USD | 0.00 USD | `+48.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 335,650.00 USD | 5,900.00 USD | 0.00 USD | `+50.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 336,730.00 USD | 1,080.00 USD | 0.00 USD | `+53.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 338,430.00 USD | 1,700.00 USD | 0.00 USD | `+53.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 339,980.00 USD | 1,550.00 USD | 0.00 USD | `+55.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 341,370.00 USD | 1,380.00 USD | 0.00 USD | `+57.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 341,990.00 USD | 621.14 USD | 0.00 USD | `+57.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 345,370.00 USD | 3,380.00 USD | 0.00 USD | `+59.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 345,590.00 USD | 222.75 USD | 0.00 USD | `+61.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 351,180.00 USD | 5,590.00 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 357,100.00 USD | 5,920.00 USD | 0.00 USD | `+63.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 358,230.00 USD | 1,130.00 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 365,860.00 USD | 7,630.00 USD | 0.00 USD | `+74.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 366,840.00 USD | 975.00 USD | 0.00 USD | `+76.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 367,820.00 USD | 981.00 USD | 0.00 USD | `+77.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 368,320.00 USD | 499.50 USD | 0.00 USD | `+80.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,250,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+80.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,260,000.00 USD | 1,000.00 USD | 0.00 USD | `+81.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,260,000.00 USD | 1,040.00 USD | 0.00 USD | `+87.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,260,000.00 USD | 340.67 USD | 0.00 USD | `+88.92%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `240.40` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 7.90 USD |
| `7D` | `240.90` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD |
| `7D` | `241.40` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `241.90` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.40` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD |
| `7D` | `242.90` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.40` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 0.00 USD | 9,910.00 USD | 5,480.00 USD |
| `1D` | `243.80` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 1,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `243.90` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 781.30 USD | 0.00 USD | 20,800.00 USD |
| `1D` | `244.20` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 0.00 USD | 265.80 USD | 0.00 USD |
| `1D` | `244.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 638.70 USD | 5,270.00 USD | 0.00 USD |
| `7D` | `244.90` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 836.88 USD | 17,320.00 USD | 2,640.00 USD |
| `1D` | `245.00` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `245.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `245.40` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD |
| `7D` | `245.90` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD |
| `1D` | `246.20` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 0.00 USD | 5,540.00 USD | 6.30 USD |
| `7D` | `246.40` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD |
| `7D` | `246.90` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,720.00 USD |
| `1D` | `247.00` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `1D` | `247.40` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 2,370.00 USD | 7,240.00 USD |
| `7D` | `247.40` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,690.00 USD |
| `1D` | `247.80` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 330.05 USD | 619.60 USD | 5.98 USD |
| `7D` | `247.90` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 789.37 USD | 4,610.00 USD | 30.29 USD |
| `1D` | `248.20` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 10,640.00 USD | 0.00 USD | 30,240.00 USD |
| `7D` | `248.40` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,890.00 USD |
| `1D` | `248.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 7,480.00 USD | 3,250.00 USD | 0.00 USD |
| `7D` | `248.90` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,240.00 USD |
| `1D` | `249.00` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 3,780.00 USD | 9,620.00 USD | 26,840.00 USD |
| `1D` | `249.40` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 1.70 USD |
| `7D` | `249.40` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 49,060.00 USD | 28,020.00 USD | 4,010.00 USD |
| `1D` | `249.80` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 10,830.00 USD | 1,230.00 USD | 3,490.00 USD |
| `7D` | `249.90` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 44,990.00 USD | 28,830.00 USD | 35,200.00 USD |
| `1D` | `250.20` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 11,880.00 USD | 5,410.00 USD | 1,930.00 USD |
| `7D` | `250.40` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,490.00 USD |
| `1D` | `250.60` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,610.00 USD | 3,270.00 USD | 1,340.00 USD |
| `7D` | `250.90` | 12,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,590.00 USD |
| `1D` | `251.00` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 28,660.00 USD | 41,480.00 USD | 11,150.00 USD |
| `1D` | `251.40` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 11,230.00 USD | 26,760.00 USD | 24,920.00 USD |
| `7D` | `251.40` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,280.00 USD |
| `1D` | `251.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 41,550.00 USD | 49,340.00 USD | 14,720.00 USD |
| `7D` | `251.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,210.00 USD |
| `1D` | `252.20` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 20,950.00 USD | 7,380.00 USD | 15,880.00 USD |
| `7D` | `252.40` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,070.00 USD |
| `1D` | `252.60` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 10,340.00 USD | 92.40 USD | 3,480.00 USD |
| `7D` | `252.90` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 29,220.00 USD | 19,580.00 USD | 64.06 USD |
| `1D` | `253.00` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 10,280.00 USD | 15,070.00 USD | 2,980.00 USD |
| `1D` | `253.40` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 21,310.00 USD | 16,680.00 USD | 9,210.00 USD |
| `7D` | `253.40` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,320.00 USD |
| `1D` | `253.80` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 1,670.00 USD | 8,890.00 USD | 10,940.00 USD |
| `7D` | `253.90` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,910.00 USD |
| `1D` | `254.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 144.00 USD | 2,130.00 USD | 3,930.00 USD |
| `7D` | `254.40` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,860.00 USD |
| `1D` | `254.60` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 994.06 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `254.90` | 11,110,000.00 USD | 0.00 USD | 11,110,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD |
| `1D` | `255.00` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 9,680.00 USD | 6,590.00 USD | 0.00 USD |
| `1D` | `255.40` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 244.00 USD | 1,090.00 USD | 11.05 USD |
| `7D` | `255.40` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 51,710.00 USD | 11,830.00 USD | 23,830.00 USD |
| `1D` | `255.80` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 13,410.00 USD | 7,270.00 USD | 2,760.00 USD |
| `7D` | `255.90` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 16,050.00 USD | 30,780.00 USD | 37,400.00 USD |
| `1D` | `256.20` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 11,210.00 USD | 4,120.00 USD | 2,580.00 USD |
| `7D` | `256.40` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 88,910.00 USD | 20,980.00 USD | 37,400.00 USD |
| `1D` | `256.60` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD |
| `7D` | `256.90` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,930.00 USD |
| `1D` | `257.00` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 494.83 USD | 928.93 USD | 3,430.00 USD |
| `1D` | `257.40` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 6,290.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `257.40` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,360.00 USD |
| `1D` | `257.80` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 32.50 USD | 2,440.00 USD | 6,450.00 USD |
| `7D` | `257.90` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,250.00 USD |
| `1D` | `258.20` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 5,030.00 USD | 3,750.00 USD | 5,230.00 USD |
| `7D` | `258.40` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 137,820.00 USD | 54,900.00 USD | 51,740.00 USD |
| `1D` | `258.60` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 3,450.00 USD | 14.47 USD | 5,590.00 USD |
| `7D` | `258.90` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 60,610.00 USD | 3,500.00 USD | 34,410.00 USD |
| `1D` | `259.00` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 11,160.00 USD | 7,340.00 USD | 11.60 USD |
| `1D` | `259.40` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 5,040.00 USD | 2,530.00 USD | 9,240.00 USD |
| `7D` | `259.40` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,090.00 USD |
| `1D` | `259.80` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 13,420.00 USD | 11,230.00 USD | 22,660.00 USD |
| `7D` | `259.90` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 19,140.00 USD | 12,520.00 USD | 98.56 USD |
| `1D` | `260.20` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 6,870.00 USD | 16,660.00 USD | 6,860.00 USD |
| `7D` | `260.40` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,100.00 USD |
| `1D` | `260.60` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 357.42 USD | 13,560.00 USD | 10,400.00 USD |
| `7D` | `260.90` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,990.00 USD |
| `1D` | `261.00` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 8,050.00 USD | 18,010.00 USD | 44,780.00 USD |
| `1D` | `261.40` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 9,410.00 USD | 16,080.00 USD | 514.69 USD |
| `7D` | `261.40` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,410.00 USD |
| `1D` | `261.80` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 4,510.00 USD | 6,650.00 USD | 27,690.00 USD |
| `7D` | `261.90` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,320.00 USD |
| `1D` | `262.20` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 8,900.00 USD | 4,380.00 USD | 5,590.00 USD |
| `7D` | `262.40` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 44,640.00 USD | 52,560.00 USD | 32.59 USD |
| `1D` | `262.60` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 366.04 USD | 1,300.00 USD | 12.23 USD |
| `7D` | `262.90` | 9,490,000.00 USD | 0.00 USD | 9,490,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,760.00 USD |
| `1D` | `263.00` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 8,670.00 USD | 13,360.00 USD | 7,500.00 USD |
| `1D` | `263.40` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 215.89 USD | 3,940.00 USD | 18,270.00 USD |
| `7D` | `263.40` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 100,770.00 USD | 30,720.00 USD | 50,060.00 USD |
| `1D` | `263.80` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 616.37 USD | 7,480.00 USD | 24,670.00 USD |
| `7D` | `263.90` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 287,090.00 USD | 98,240.00 USD | 57,860.00 USD |
| `1D` | `264.20` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,010.00 USD | 666.33 USD | 7.32 USD |
| `7D` | `264.40` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,240.00 USD |
| `1D` | `264.60` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 28,600.00 USD | 110.80 USD | 60,000.00 USD |
| `7D` | `264.90` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 28,050.00 USD | 75,010.00 USD | 27,180.00 USD |
| `1D` | `265.00` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 30,810.00 USD | 9,490.00 USD | 15,630.00 USD |
| `1D` | `265.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 694.46 USD | 12,230.00 USD | 33,450.00 USD |
| `7D` | `265.40` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,920.00 USD |
| `1D` | `265.80` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 23,780.00 USD | 22,790.00 USD | 42,360.00 USD |
| `7D` | `265.90` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,670.00 USD |
| `1D` | `266.20` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 21,580.00 USD | 87.00 USD | 3,210.00 USD |
| `7D` | `266.40` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,530.00 USD |
| `1D` | `266.60` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 36,980.00 USD | 29,590.00 USD | 67,190.00 USD |
| `7D` | `266.90` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,440.00 USD |
| `1D` | `267.00` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 26,590.00 USD | 25,650.00 USD | 6,770.00 USD |
| `1D` | `267.40` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 14,480.00 USD | 26,770.00 USD | 56,230.00 USD |
| `7D` | `267.40` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 119,030.00 USD | 209,120.00 USD | 96,420.00 USD |
| `1D` | `267.80` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 96,650.00 USD | 116,030.00 USD | 33,330.00 USD |
| `7D` | `267.90` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,260.00 USD |
| `1D` | `268.20` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 41,920.00 USD | 123,890.00 USD | 47,050.00 USD |
| `7D` | `268.40` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 176,940.00 USD | 325,150.00 USD | 99,570.00 USD |
| `1D` | `268.60` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 115,220.00 USD | 107,040.00 USD | 41,620.00 USD |
| `7D` | `268.90` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,100.00 USD |
| `1D` | `269.00` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 77,550.00 USD | 26,120.00 USD | 41,940.00 USD |
| `1D` | `269.40` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 20,200.00 USD | 18,120.00 USD | 44,940.00 USD |
| `7D` | `269.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,230.00 USD |
| `1D` | `269.80` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 34,240.00 USD | 21,490.00 USD | 11,570.00 USD |
| `7D` | `269.90` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 74,250.00 USD | 141,330.00 USD | 145.08 USD |
| `1D` | `270.20` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 120,570.00 USD | 21,550.00 USD | 144,370.00 USD |
| `7D` | `270.40` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 118,110.00 USD | 0.00 USD | 95.19 USD |
| `1D` | `270.60` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 78,270.00 USD | 0.00 USD | 61,680.00 USD |
| `7D` | `270.90` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 328,250.00 USD | 0.00 USD | 36.41 USD |
| `1D` | `271.00` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 25,020.00 USD | 0.00 USD | 76,700.00 USD |
| `1D` | `271.40` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 46,900.00 USD | 0.00 USD | 72,980.00 USD |
| `7D` | `271.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.80` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 55,090.00 USD | 0.00 USD | 7.04 USD |
| `7D` | `271.90` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 475,090.00 USD | 0.00 USD | 158.69 USD |
| `1D` | `272.20` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 102,590.00 USD | 81.40 USD | 5.86 USD |
| `7D` | `272.40` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.60` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 76,790.00 USD | 447.70 USD | 9.74 USD |
| `7D` | `272.90` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 150,960.00 USD | 0.00 USD | 15,580.00 USD |
| `1D` | `273.00` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 68,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `273.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 217,920.00 USD | 73.70 USD | 53,980.00 USD |
| `7D` | `273.40` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 379,280.00 USD | 0.00 USD | 163,360.00 USD |
| `1D` | `273.80` | 746,260.00 USD | 0.00 USD | 746,260.00 USD | 103,540.00 USD | 0.00 USD | 57,950.00 USD |
| `7D` | `273.90` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 375,450.00 USD | 0.00 USD | 257.86 USD |
| `1D` | `274.20` | 584,770.00 USD | 0.00 USD | 584,770.00 USD | 228,980.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `274.40` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 496,740.00 USD | 248,170.00 USD | 132.10 USD |
| `1D` | `274.60` | 355,780.00 USD | 0.00 USD | 355,780.00 USD | 166,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 709,080.00 USD | 0.00 USD | 709,080.00 USD | 348,470.00 USD | 202,210.00 USD | 159.64 USD |
| `1D` | `275.00` | 188,980.00 USD | 0.00 USD | 188,980.00 USD | 33,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.40` | 158,240.00 USD | 0.00 USD | 158,240.00 USD | 3,530.00 USD | 126,890.00 USD | 0.00 USD |
| `1D` | `275.80` | 155,050.00 USD | 0.00 USD | 155,050.00 USD | 0.00 USD | 31,880.00 USD | 0.00 USD |
| `7D` | `275.90` | 27,810.00 USD | 0.00 USD | 27,810.00 USD | 2,560.00 USD | 25,250.00 USD | 0.00 USD |
| `1D` | `276.20` | 123,170.00 USD | 0.00 USD | 123,170.00 USD | 0.00 USD | 36,820.00 USD | 0.00 USD |
| `7D` | `276.40` | 106,230.00 USD | 106,230.00 USD | 0.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD |
| `7D` | `276.40` | 212,450.00 USD | 212,450.00 USD | 0.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.60` | 86,350.00 USD | 0.00 USD | 86,350.00 USD | 0.00 USD | 48,940.00 USD | 0.00 USD |
| `7D` | `276.90` | 281,040.00 USD | 281,040.00 USD | 0.00 USD | 45,560.00 USD | 22,950.00 USD | 79.15 USD |
| `1D` | `277.00` | 37,400.00 USD | 0.00 USD | 37,400.00 USD | 0.00 USD | 37,400.00 USD | 0.00 USD |
| `1D` | `277.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.40` | 168,480.00 USD | 168,480.00 USD | 0.00 USD | 42,360.00 USD | 64,450.00 USD | 61,670.00 USD |
| `7D` | `277.40` | 344,330.00 USD | 344,330.00 USD | 0.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD |
| `1D` | `277.80` | 224,520.00 USD | 224,520.00 USD | 0.00 USD | 44,920.00 USD | 11,130.00 USD | 0.00 USD |
| `7D` | `277.90` | 430,020.00 USD | 430,020.00 USD | 0.00 USD | 0.00 USD | 85,690.00 USD | 0.00 USD |
| `1D` | `278.20` | 294,060.00 USD | 294,060.00 USD | 0.00 USD | 30,830.00 USD | 0.00 USD | 38,710.00 USD |
| `7D` | `278.40` | 481,140.00 USD | 481,140.00 USD | 0.00 USD | 24,750.00 USD | 26,370.00 USD | 0.00 USD |
| `1D` | `278.60` | 361,380.00 USD | 361,380.00 USD | 0.00 USD | 37,120.00 USD | 30,210.00 USD | 0.00 USD |
| `7D` | `278.90` | 558,690.00 USD | 558,690.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD |
| `1D` | `279.00` | 389,760.00 USD | 389,760.00 USD | 0.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD |
| `1D` | `279.40` | 468,020.00 USD | 468,020.00 USD | 0.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD |
| `7D` | `279.40` | 654,680.00 USD | 654,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD |
| `1D` | `279.80` | 492,820.00 USD | 492,820.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 17,110.00 USD |
| `7D` | `279.90` | 654,820.00 USD | 654,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146.32 USD |
| `1D` | `280.20` | 576,050.00 USD | 576,050.00 USD | 0.00 USD | 29,750.00 USD | 11,840.00 USD | 41,630.00 USD |
| `7D` | `280.40` | 654,830.00 USD | 654,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9.80 USD |
| `1D` | `280.60` | 660,000.00 USD | 660,000.00 USD | 0.00 USD | 0.00 USD | 4,860.00 USD | 79,090.00 USD |
| `7D` | `280.90` | 654,870.00 USD | 654,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.07 USD |
| `1D` | `281.00` | 743,530.00 USD | 743,530.00 USD | 0.00 USD | 0.00 USD | 7,010.00 USD | 76,520.00 USD |
| `1D` | `281.40` | 764,120.00 USD | 764,120.00 USD | 0.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `281.40` | 717,690.00 USD | 717,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD |
| `1D` | `281.80` | 769,530.00 USD | 769,530.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.90` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 398,240.00 USD |
| `7D` | `282.40` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,310.00 USD |
| `1D` | `282.60` | 822,270.00 USD | 822,270.00 USD | 0.00 USD | 22,180.00 USD | 13,190.00 USD | 17,380.00 USD |
| `7D` | `282.90` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 7.66 USD |
| `1D` | `283.00` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 71,390.00 USD | 5,570.00 USD | 126,060.00 USD |
| `1D` | `283.40` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66,490.00 USD |
| `7D` | `283.40` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 146,380.00 USD |
| `1D` | `283.80` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 45,780.00 USD | 47,890.00 USD |
| `7D` | `283.90` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD |
| `1D` | `284.20` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 38,980.00 USD | 50,430.00 USD | 97,960.00 USD |
| `7D` | `284.40` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 27,700.00 USD | 89,730.00 USD | 42,770.00 USD |
| `1D` | `284.60` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 49,080.00 USD | 67,500.00 USD | 20,690.00 USD |
| `7D` | `284.90` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 67,050.00 USD | 391,180.00 USD | 114.09 USD |
| `1D` | `285.00` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 20,960.00 USD | 0.00 USD | 54,520.00 USD |
| `1D` | `285.40` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 117,450.00 USD | 125,760.00 USD | 80,720.00 USD |
| `7D` | `285.40` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 64,060.00 USD | 193,790.00 USD | 83,250.00 USD |
| `1D` | `285.80` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 40,630.00 USD | 33,170.00 USD | 18,110.00 USD |
| `7D` | `285.90` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 1,200.00 USD | 97,960.00 USD | 7.06 USD |
| `7D` | `286.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 137,400.00 USD | 32.62 USD |
| `1D` | `286.60` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD |
| `7D` | `286.90` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 51,390.00 USD | 141,160.00 USD | 61.94 USD |
| `1D` | `287.00` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 31,110.00 USD | 99,880.00 USD | 80,690.00 USD |
| `1D` | `287.40` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 29,800.00 USD | 26,570.00 USD |
| `7D` | `287.40` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 53,620.00 USD | 103,430.00 USD | 53,270.00 USD |
| `1D` | `287.80` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 9,030.00 USD | 9,240.00 USD | 47,790.00 USD |
| `7D` | `287.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD |
| `1D` | `288.20` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 11,090.00 USD | 10,810.00 USD | 8,690.00 USD |
| `7D` | `288.40` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.86 USD |
| `1D` | `288.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD |
| `7D` | `288.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.00` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 1,540.00 USD | 14,290.00 USD | 11.96 USD |
| `1D` | `289.40` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 664.77 USD | 6,150.00 USD | 0.00 USD |
| `7D` | `289.40` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 52.62 USD |
| `1D` | `289.80` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD |
| `7D` | `289.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | 14.14 USD |
| `7D` | `290.40` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 34,580.00 USD | 0.00 USD | 34.34 USD |
| `1D` | `290.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 305.70 USD | 16,960.00 USD |
| `7D` | `290.90` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 55.15 USD |
| `1D` | `291.00` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 32,650.00 USD | 6,700.00 USD | 3.40 USD |
| `1D` | `291.40` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 562.74 USD | 21,420.00 USD | 14.38 USD |
| `7D` | `291.40` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 55,720.00 USD | 55.26 USD |
| `1D` | `291.80` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 6,460.00 USD | 22,140.00 USD |
| `7D` | `291.90` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 52.30 USD |
| `1D` | `292.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 10,080.00 USD | 40,470.00 USD | 8,120.00 USD |
| `7D` | `292.40` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 71,940.00 USD | 43.94 USD |
| `1D` | `292.60` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 22,800.00 USD | 60,150.00 USD | 10.63 USD |
| `7D` | `292.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 119,560.00 USD | 13.37 USD |
| `1D` | `293.00` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 10,970.00 USD | 47,730.00 USD | 13,280.00 USD |
| `1D` | `293.40` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 10,610.00 USD | 51,670.00 USD | 23,900.00 USD |
| `7D` | `293.40` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 198.85 USD |
| `1D` | `293.80` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 88,720.00 USD | 43,910.00 USD | 43,990.00 USD |
| `7D` | `293.90` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,070.00 USD |
| `1D` | `294.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 27,810.00 USD | 48,520.00 USD | 56,630.00 USD |
| `7D` | `294.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 139,780.00 USD | 14,550.00 USD | 60,710.00 USD |
| `1D` | `294.60` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 120,380.00 USD | 90,270.00 USD | 85,210.00 USD |
| `7D` | `294.90` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 64,510.00 USD | 107,870.00 USD | 104,910.00 USD |
| `1D` | `295.00` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 19,910.00 USD | 47,160.00 USD | 39,720.00 USD |
| `1D` | `295.40` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 29,300.00 USD | 104,750.00 USD | 59,150.00 USD |
| `7D` | `295.40` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD |
| `1D` | `295.80` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 83,280.00 USD | 26,280.00 USD | 69,660.00 USD |
| `7D` | `295.90` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 107,830.00 USD | 133,090.00 USD | 150,820.00 USD |
| `1D` | `296.20` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 83,160.00 USD | 83,110.00 USD | 29,590.00 USD |
| `7D` | `296.40` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 27,680.00 USD | 77,570.00 USD | 120,840.00 USD |
| `1D` | `296.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 43,250.00 USD | 12,140.00 USD | 20,600.00 USD |
| `7D` | `296.90` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 207,350.00 USD | 50,930.00 USD | 172,350.00 USD |
| `1D` | `297.00` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 1,400.00 USD | 20,940.00 USD | 78,160.00 USD |
| `1D` | `297.40` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 57,480.00 USD | 879.58 USD | 20,820.00 USD |
| `7D` | `297.40` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD |
| `1D` | `297.80` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 2,180.00 USD | 6,230.00 USD | 12,060.00 USD |
| `7D` | `297.90` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 17,770.00 USD | 39,840.00 USD | 55,060.00 USD |
| `1D` | `298.20` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 55,290.00 USD | 4,610.00 USD | 84,890.00 USD |
| `7D` | `298.40` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 32,250.00 USD | 42,710.00 USD | 68,760.00 USD |
| `1D` | `298.60` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 24,810.00 USD | 7,720.00 USD | 61,080.00 USD |
| `7D` | `298.90` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 70,090.00 USD | 12,780.00 USD | 39,990.00 USD |
| `1D` | `299.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 13,220.00 USD | 16,220.00 USD | 46,690.00 USD |
| `1D` | `299.40` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 35,490.00 USD | 17,080.00 USD | 31,470.00 USD |
| `7D` | `299.40` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 4,470.00 USD | 13,080.00 USD | 45,940.00 USD |
| `1D` | `299.80` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 12,870.00 USD | 12,440.00 USD | 32,160.00 USD |
| `7D` | `299.90` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 56,210.00 USD | 10,220.00 USD | 19,840.00 USD |
| `1D` | `300.20` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 34,830.00 USD | 29,170.00 USD | 43,050.00 USD |
| `7D` | `300.40` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 147.03 USD |
| `1D` | `300.60` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 11,460.00 USD | 22,740.00 USD | 17,830.00 USD |
| `7D` | `300.90` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 24,730.00 USD | 70,210.00 USD | 104,060.00 USD |
| `1D` | `301.00` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 8,670.00 USD | 27,670.00 USD | 26,010.00 USD |
| `1D` | `301.40` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 950.24 USD | 33,440.00 USD | 34,830.00 USD |
| `7D` | `301.40` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 71,890.00 USD | 56,010.00 USD | 94,710.00 USD |
| `1D` | `301.80` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 19,450.00 USD | 31,100.00 USD | 11,570.00 USD |
| `7D` | `301.90` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 89,300.00 USD | 185,430.00 USD | 26,280.00 USD |
| `1D` | `302.20` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 30,090.00 USD | 16,310.00 USD | 5.28 USD |
| `7D` | `302.40` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 152.98 USD |
| `1D` | `302.60` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 11,270.00 USD | 11,110.00 USD | 38,380.00 USD |
| `7D` | `302.90` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 71,700.00 USD | 110,480.00 USD | 41,670.00 USD |
| `1D` | `303.00` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 20,640.00 USD | 1,820.00 USD | 13,990.00 USD |
| `1D` | `303.40` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 10,970.00 USD | 176.02 USD | 30,240.00 USD |
| `7D` | `303.40` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 154.86 USD |
| `1D` | `303.80` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 7,850.00 USD | 3,590.00 USD | 1.44 USD |
| `7D` | `303.90` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 21,140.00 USD | 11,010.00 USD | 45,890.00 USD |
| `1D` | `304.20` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 21,670.00 USD | 5,150.00 USD | 53,800.00 USD |
| `7D` | `304.40` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 3,670.00 USD | 11,280.00 USD | 154.04 USD |
| `1D` | `304.60` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 13,310.00 USD | 4,900.00 USD | 53,810.00 USD |
| `7D` | `304.90` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 36,160.00 USD | 18,990.00 USD | 8,350.00 USD |
| `1D` | `305.00` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 697.80 USD | 43.93 USD | 1,280.00 USD |
| `1D` | `305.40` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 10,950.00 USD | 1,640.00 USD | 2,220.00 USD |
| `7D` | `305.40` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 163,900.00 USD | 127,450.00 USD | 119,240.00 USD |
| `1D` | `305.80` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 12,080.00 USD | 5,750.00 USD | 1,930.00 USD |
| `7D` | `305.90` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 82,000.00 USD | 55,480.00 USD | 10,600.00 USD |
| `1D` | `306.20` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 3,900.00 USD | 3,330.00 USD | 1,350.00 USD |
| `7D` | `306.40` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 39,250.00 USD | 55,740.00 USD | 66,810.00 USD |
| `1D` | `306.60` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 4,420.00 USD | 11,690.00 USD | 7,060.00 USD |
| `7D` | `306.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 84,850.00 USD | 64,520.00 USD | 102,680.00 USD |
| `1D` | `307.00` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 31,810.00 USD | 38,740.00 USD | 16,140.00 USD |
| `1D` | `307.40` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 4,290.00 USD | 31,200.00 USD | 13,240.00 USD |
| `7D` | `307.40` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 46,230.00 USD | 154,680.00 USD | 83,400.00 USD |
| `1D` | `307.80` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 41,630.00 USD | 37,370.00 USD | 14,380.00 USD |
| `7D` | `307.90` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 136,380.00 USD | 101,120.00 USD | 65,290.00 USD |
| `1D` | `308.20` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 21,090.00 USD | 7,500.00 USD | 15,880.00 USD |
| `7D` | `308.40` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 152,590.00 USD | 50,070.00 USD | 125,020.00 USD |
| `1D` | `308.60` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 5,550.00 USD | 167.90 USD | 3,480.00 USD |
| `7D` | `308.90` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 61,600.00 USD | 52,230.00 USD | 19,730.00 USD |
| `1D` | `309.00` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 11,380.00 USD | 6,400.00 USD | 2,180.00 USD |
| `1D` | `309.40` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 9,920.00 USD | 14,000.00 USD | 4,720.00 USD |
| `7D` | `309.40` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 28,000.00 USD | 35,530.00 USD | 46,570.00 USD |
| `1D` | `309.80` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 13,710.00 USD | 11,430.00 USD | 5,280.00 USD |
| `7D` | `309.90` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 59,490.00 USD | 131,460.00 USD | 144,740.00 USD |
| `1D` | `310.20` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 1,670.00 USD | 8,920.00 USD | 10,940.00 USD |
| `7D` | `310.40` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 78,770.00 USD | 123,340.00 USD | 76,830.00 USD |
| `1D` | `310.60` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 144.00 USD | 2,370.00 USD | 3,930.00 USD |
| `7D` | `310.90` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 35,670.00 USD | 35,930.00 USD | 3,820.00 USD |
| `1D` | `311.00` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 134.35 USD | 0.00 USD | 0.82 USD |
| `1D` | `311.40` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 940.26 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `311.40` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 89,390.00 USD | 65,750.00 USD | 47,700.00 USD |
| `1D` | `311.80` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 9,260.00 USD | 6,590.00 USD | 4.14 USD |
| `7D` | `311.90` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 40,320.00 USD | 11,160.00 USD | 13,650.00 USD |
| `1D` | `312.20` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 244.00 USD | 234.60 USD | 1.60 USD |
| `7D` | `312.40` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 45,640.00 USD | 22,970.00 USD | 43,620.00 USD |
| `1D` | `312.60` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 13,410.00 USD | 7,270.00 USD | 2,760.00 USD |
| `7D` | `312.90` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 47,820.00 USD |
| `1D` | `313.00` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 11,210.00 USD | 0.00 USD | 0.96 USD |
| `1D` | `313.40` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 7,160.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.40` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 66,180.00 USD | 30,120.00 USD | 30,440.00 USD |
| `1D` | `313.80` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `313.90` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 44,540.00 USD | 15,370.00 USD | 35,870.00 USD |
| `1D` | `314.20` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.40` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,850.00 USD |
| `1D` | `314.60` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `314.90` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 39,410.00 USD | 0.00 USD | 10,380.00 USD |
| `1D` | `315.00` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 32.50 USD | 1,400.00 USD | 6,450.00 USD |
| `1D` | `315.40` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 3,750.00 USD | 144.50 USD | 0.81 USD |
| `7D` | `315.40` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 6,160.00 USD | 9,920.00 USD | 18,180.00 USD |
| `1D` | `315.80` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 1,370.00 USD | 3,040.00 USD | 5,230.00 USD |
| `7D` | `315.90` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 47,110.00 USD | 41,400.00 USD | 29,980.00 USD |
| `1D` | `316.20` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 2,100.00 USD | 3,070.00 USD | 5,590.00 USD |
| `7D` | `316.40` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 16,580.00 USD | 40,320.00 USD | 61,840.00 USD |
| `1D` | `316.60` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 11,090.00 USD | 3,300.00 USD | 0.00 USD |
| `7D` | `316.90` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 107.59 USD |
| `1D` | `317.00` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 3,590.00 USD | 2,190.00 USD | 9,240.00 USD |
| `1D` | `317.40` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 3,720.00 USD | 1,960.00 USD | 5,580.00 USD |
| `7D` | `317.40` | 12,100,000.00 USD | 12,100,000.00 USD | 0.00 USD | 14,540.00 USD | 1,010.00 USD | 118.98 USD |
| `1D` | `317.50` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 5,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `317.90` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 21,640.00 USD | 8,200.00 USD | 111.68 USD |
| `7D` | `318.40` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 3,320.00 USD | 27,530.00 USD | 22,360.00 USD |
| `7D` | `318.90` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 11,180.00 USD | 17,970.00 USD | 37,850.00 USD |
| `7D` | `319.40` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 733.55 USD | 18,060.00 USD | 0.00 USD |
| `7D` | `319.90` | 12,300,000.00 USD | 12,300,000.00 USD | 0.00 USD | 446.22 USD | 22,230.00 USD | 5,370.00 USD |
| `7D` | `320.40` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD |
| `7D` | `320.90` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 1.97 USD |
| `7D` | `321.40` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 13,640.00 USD | 17,870.00 USD | 15,810.00 USD |
| `7D` | `321.90` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD |
| `7D` | `322.40` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 22,930.00 USD | 7,950.00 USD | 6,200.00 USD |
| `7D` | `322.90` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 16,590.00 USD | 5,830.00 USD | 0.00 USD |
| `7D` | `323.40` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 14,160.00 USD | 11,950.00 USD | 11,520.00 USD |
| `7D` | `323.90` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 269.10 USD | 692.00 USD | 27.52 USD |
| `7D` | `324.40` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.90` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD |
| `7D` | `325.40` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `299.36M` | Total OI Tokens: `1,077,505.2 BCH`
  * 1h OI Change: `+1.53%` | 4h OI Change: `-5.18%` | 24h OI Change: `-7.80%`
  * Exchange Breakdown: Binance=`88.10M` | Bybit=`37.59M` | OKX=`23.42M` | Hyperliquid=`7.57M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.52K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0022%` | **USDT OKX** | `-0.0049%` |
| **USDT Bybit** | `0.0022%` | **USDT KuCoin** | `-0.0003%` |
| **USDT MEXC** | `0.0021%` | **USDT BingX** | `0.0097%` |
| **USDT Gate** | `0.0025%` | **USDT Bitget** | `0.0095%` |
| **CoinM Binance** | `-0.0033%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `50.89%` | `49.11%` | `1.04` | 5,180,000.00 USD |
| `15M` | `Binance` | `47.52%` | `52.48%` | `0.91` | 2,040,000.00 USD |
| `15M` | `OKX` | `48.99%` | `51.01%` | `0.96` | 574,650.00 USD |
| `15M` | `Bybit` | `47.36%` | `52.64%` | `0.90` | 455,170.00 USD |
| `15M` | `KuCoin` | `46.7%` | `53.3%` | `0.88` | 171,530.00 USD |
| `15M` | `Gate` | `54.08%` | `45.92%` | `1.18` | 330,820.00 USD |
| `15M` | `Bitget` | `27.61%` | `72.39%` | `0.38` | 121,760.00 USD |
| `15M` | `BingX` | `56.12%` | `43.88%` | `1.28` | 159,790.00 USD |
| `15M` | `MEXC` | `45.47%` | `54.53%` | `0.83` | 258,670.00 USD |
| `15M` | `Bitunix` | `42.88%` | `57.12%` | `0.75` | 100,290.00 USD |
| `15M` | `Hyperliquid` | `41.51%` | `58.49%` | `0.71` | 76,430.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.98%` | `50.02%` | `1.00` | 437,110.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `95.19%` | `4.81%` | `19.79` | 374,430.00 USD |
| `15M` | `HTX` | `64.19%` | `35.81%` | `1.79` | 3,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `25.27%` | `74.73%` | `0.34` | 60,510.00 USD |
| `15M` | `Aster` | `4.94%` | `95.06%` | `0.05` | 11,490.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `47.52%` | `52.48%` | `0.91` | 2,040,000.00 USD |
| `15M` | `Global Accounts` | `50.89%` | `49.11%` | `1.04` | 5,180,000.00 USD |
| `1H` | `BCH` | `50.99%` | `49.01%` | `1.04` | 31,140,000.00 USD |
| `1H` | `Binance` | `46.4%` | `53.6%` | `0.87` | 11,270,000.00 USD |
| `1H` | `OKX` | `58.84%` | `41.16%` | `1.43` | 2,820,000.00 USD |
| `1H` | `Bybit` | `64.8%` | `35.2%` | `1.84` | 4,590,000.00 USD |
| `1H` | `KuCoin` | `48.14%` | `51.86%` | `0.93` | 256,360.00 USD |
| `1H` | `Gate` | `48.39%` | `51.61%` | `0.94` | 2,070,000.00 USD |
| `1H` | `Bitget` | `23.03%` | `76.97%` | `0.30` | 1,120,000.00 USD |
| `1H` | `BingX` | `49.71%` | `50.29%` | `0.99` | 2,310,000.00 USD |
| `1H` | `MEXC` | `34.44%` | `65.56%` | `0.53` | 1,160,000.00 USD |
| `1H` | `Bitunix` | `50.45%` | `49.55%` | `1.02` | 825,260.00 USD |
| `1H` | `Hyperliquid` | `44.23%` | `55.77%` | `0.79` | 270,170.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.96%` | `50.04%` | `1.00` | 1,060,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `56.08%` | `43.92%` | `1.28` | 2,830,000.00 USD |
| `1H` | `HTX` | `43.68%` | `56.32%` | `0.78` | 89,910.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `85.65%` | `14.35%` | `5.97` | 307,880.00 USD |
| `1H` | `Aster` | `85.83%` | `14.17%` | `6.06` | 144,420.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `23.46%` | `76.54%` | `0.31` | 4,980.00 USD |
| `1H` | `Whale Positions` | `46.4%` | `53.6%` | `0.87` | 11,270,000.00 USD |
| `1H` | `Global Accounts` | `50.99%` | `49.01%` | `1.04` | 31,140,000.00 USD |
| `4H` | `BCH` | `48.81%` | `51.19%` | `0.95` | 123,570,000.00 USD |
| `4H` | `Binance` | `50.51%` | `49.49%` | `1.02` | 43,780,000.00 USD |
| `4H` | `OKX` | `49.49%` | `50.51%` | `0.98` | 14,860,000.00 USD |
| `4H` | `Bybit` | `50.71%` | `49.29%` | `1.03` | 15,240,000.00 USD |
| `4H` | `KuCoin` | `49.34%` | `50.66%` | `0.97` | 854,380.00 USD |
| `4H` | `Gate` | `54.01%` | `45.99%` | `1.17` | 9,480,000.00 USD |
| `4H` | `Bitget` | `51.72%` | `48.28%` | `1.07` | 4,740,000.00 USD |
| `4H` | `BingX` | `40.69%` | `59.31%` | `0.69` | 9,250,000.00 USD |
| `4H` | `MEXC` | `44.24%` | `55.76%` | `0.79` | 5,790,000.00 USD |
| `4H` | `Bitunix` | `53.08%` | `46.92%` | `1.13` | 2,390,000.00 USD |
| `4H` | `Hyperliquid` | `33.09%` | `66.91%` | `0.49` | 1,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.61%` | `50.39%` | `0.98` | 3,010,000.00 USD |
| `4H` | `Crypto.com` | `75.54%` | `24.46%` | `3.09` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.7%` | `88.3%` | `0.13` | 10,760,000.00 USD |
| `4H` | `HTX` | `44.62%` | `55.38%` | `0.81` | 601,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.51%` | `55.49%` | `0.80` | 666,330.00 USD |
| `4H` | `Aster` | `54.4%` | `45.6%` | `1.19` | 407,190.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `34.7%` | `65.3%` | `0.53` | 159,300.00 USD |
| `4H` | `Whale Positions` | `50.51%` | `49.49%` | `1.02` | 43,780,000.00 USD |
| `4H` | `Global Accounts` | `48.81%` | `51.19%` | `0.95` | 123,570,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `287.00` | `286.98` | `287.00` | `287.64` | `286.45` | 492,053.69 USD | 262,098.60 USD | 229,955.08 USD | 32,143.52 USD | `+6.53%` | `24B / 25S` |
| `0:00 UTC` | `282.00` | `283.04` | `282.00` | `286.92` | `280.48` | 5,571,232.46 USD | 2,485,967.17 USD | 3,085,265.29 USD | -599,298.12 USD | `-10.76%` | `4B / 29S` |
| `5:00 UTC` | `282.43` | `282.21` | `282.43` | `283.00` | `281.49` | 1,589,754.90 USD | 936,266.72 USD | 653,488.17 USD | 282,778.55 USD | `+17.79%` | `31B / 14S` |
| `0:00 UTC` | `275.52` | `277.16` | `275.52` | `282.40` | `273.60` | 7,176,408.30 USD | 3,429,549.36 USD | 3,746,858.94 USD | -317,309.59 USD | `-4.42%` | `7B / 13S` |
| `5:00 UTC` | `273.26` | `272.72` | `273.26` | `275.70` | `269.30` | 7,511,252.05 USD | 3,875,803.21 USD | 3,635,448.84 USD | 240,354.37 USD | `+3.20%` | `12B / 10S` |
| `0:00 UTC` | `273.80` | `272.56` | `273.80` | `274.68` | `269.76` | 3,951,157.31 USD | 2,047,269.47 USD | 1,903,887.84 USD | 143,381.63 USD | `+3.63%` | `9B / 4S` |
| `5:00 UTC` | `276.40` | `276.70` | `276.40` | `278.76` | `273.60` | 2,981,088.00 USD | 1,514,309.73 USD | 1,466,778.26 USD | 47,531.47 USD | `+1.59%` | `19B / 11S` |
| `0:00 UTC` | `279.50` | `278.78` | `279.50` | `280.00` | `277.16` | 1,923,752.33 USD | 667,499.40 USD | 1,256,252.93 USD | -588,753.54 USD | `-30.60%` | `8B / 42S` |
| `5:00 UTC` | `276.86` | `277.31` | `276.86` | `278.92` | `275.98` | 2,702,816.05 USD | 1,627,166.23 USD | 1,075,649.82 USD | 551,516.40 USD | `+20.41%` | `18B / 30S` |
| `0:00 UTC` | `276.00` | `276.19` | `276.00` | `277.03` | `275.69` | 472,438.70 USD | 143,988.90 USD | 328,449.80 USD | -184,460.91 USD | `-39.04%` | `11B / 57S` |

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
| `5m` | 185,980.00 USD | 682,570.00 USD | **`ACCUMULATION`** |
| `15m` | 217,740.00 USD | 466,160.00 USD | **`ACCUMULATION`** |
| `30m` | 184,590.00 USD | 928,970.00 USD | **`ACCUMULATION`** |
| `1h` | 400,740.00 USD | 1,090,000.00 USD | **`ACCUMULATION`** |
| `2h` | -235,340.00 USD | 2,160,000.00 USD | **`ACCUMULATION`** |
| `4h` | -852,820.00 USD | 537,470.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,110,000.00 USD | -3,190,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -378,700.00 USD | -602,530.00 USD | **`DISTRIBUTION`** |
| `12h` | -434,200.00 USD | -273,800.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,510,000.00 USD | -8,200,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -475,230.00 USD | -11,950,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,680,000.00 USD | -136,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+185.98K` | 15m=`+217.74K` | 1h=`+400.74K` | 24h=`-1.51M`
* Futures Capital Netflows: 5m=`+682.57K` | 15m=`+466.16K` | 1h=`+1.09M` | 24h=`-8.20M`
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
  * Execution Entry: `273.70` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `269.10` (Risk Distance: `4.60` pts)
  * +2.5R Take Profit: `285.19`
  * Mathematical Lot Sizing: **`2.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `282.93` (Risk Distance: `4.60` pts)
  * +2.5R Take Profit: `266.84`
  * Mathematical Lot Sizing: **`2.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`277.60`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
