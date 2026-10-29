# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 03:19:13 IST` (`2026-10-29 21:49:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `277.10` | **Live Ask Quote**: `277.60` | **Mid Price**: `277.35`
- **Spread Points**: `501.00` | **Spread BPS**: `18.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `281.37` | VWAP Z-Score: `-0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.20` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `40.15` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `296.55` | Lower -3.00σ Band: `266.19`
  * Upper +2.51σ Band: `294.07` | Lower -2.51σ Band: `268.67`
  * Upper +2.01σ Band: `291.54` | Lower -2.01σ Band: `271.20`
  * Upper +2.00σ Band: `291.49` | Lower -2.00σ Band: `271.25`
  * Upper +1.28σ Band: `287.85` | Lower -1.28σ Band: `274.89`
  * Upper +1.00σ Band: `286.43` | Lower -1.00σ Band: `276.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`278.58` | EMA-20=`281.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`282.61` (Slope: `+0.0000`) | EMA-100=`283.58`
  * Institutional Anchors: EMA-144=`284.13` | EMA-200=`284.44` (Slope: `-0.1303`) | EMA-233=`284.96`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`269.53` | Weekly High=`304.16` | Weekly Low=`269.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.58` (Distance: `-0.44%`)
  * Point of Control (POC) = `276.99` (Distance: `+0.13%`)
  * Value Area Low (VAL) = `273.27` (Distance: `+1.49%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.27` | Weekly POC=`278.88` | Weekly VAL=`274.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`279.40` | Low=`270.25`
  * London Session (08:00-16:00 UTC): High=`278.46` | Low=`276.24`
  * New York Session (13:00-21:00 UTC): High=`279.01` | Low=`275.69`
  * Initial Balance (First Hour): IB High=`278.18` | IB Low=`276.52`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `276.24` - `278.46`
  * Optimal Trade Entry (OTE 0.705): `277.90`
  * Structural Invalidation Anchor (0.786): `279.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `277.64` | `279.25` | `277.64` | `278.54` | `2,280` | 634,852.79 USD | -147,772.14 USD | `-23.28%` | -3,799,666.41 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `278.52` | `280.00` | `278.30` | `278.92` | `3,135` | 875,881.64 USD | -274,145.25 USD | `-31.30%` | -4,073,811.66 USD | `-0.67` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `278.91` | `278.91` | `277.52` | `277.61` | `1,217` | 338,668.95 USD | -110,315.78 USD | `-32.57%` | -4,184,127.44 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `270.43` | `274.69` | `269.74` | `273.70` | `14,497` | 3,951,157.31 USD | 143,381.63 USD | `+3.63%` | -3,699,425.74 USD | `+0.61` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `273.69` | `278.76` | `273.58` | `277.63` | `10,774` | 2,981,088.00 USD | 47,531.47 USD | `+1.59%` | -3,651,894.27 USD | `+0.10` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `277.64` | `280.00` | `277.52` | `277.55` | `6,675` | 1,861,099.05 USD | -543,876.11 USD | `-29.22%` | -4,195,770.37 USD | `-2.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `288.16` | `289.02` | `286.45` | `286.78` | `7,901` | 2,272,698.56 USD | 287,500.01 USD | `+12.65%` | -3,481,237.48 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `286.78` | `286.91` | `269.28` | `270.43` | `78,753` | 21,848,832.22 USD | -393,290.27 USD | `-1.80%` | -3,874,527.75 USD | `-0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `270.43` | `280.00` | `269.74` | `277.55` | `31,946` | 8,793,344.37 USD | -352,963.01 USD | `-4.01%` | -4,227,490.76 USD | `-0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `277.61` | `110,657` | 30,630,480.91 USD | -734,610.34 USD | `-2.40%` | -4,144,868.14 USD | `-0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `277.61` | `110,657` | 30,630,480.91 USD | -734,610.34 USD | `-2.40%` | -4,144,868.14 USD | `-0.03` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`277.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `2000` | `0x12d2...f97f` | `LONG` | 1,007,104.02 USD | `3,627,243,000,000.00` | `303.26` | `277.22` | `0.000000` | -92,895.32 USD | `-9.22%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `296.54` | 18,029.34 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 18.03K USD at 296.5400 USD [API] | `2026-10-28 13:04:31` |
| `ANNOUNCEMENT` | `INFO` | `296.49` | 10,023.14 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 10.02K USD at 296.4900 USD [API] | `2026-10-28 13:04:31` |
| `ANNOUNCEMENT` | `INFO` | `293.56` | 7,191.63 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 7.19K USD at 293.5600 USD [API] | `2026-10-28 14:18:38` |
| `ANNOUNCEMENT` | `INFO` | `283.81` | 394.50 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Short: 0.39K USD at 283.8100 USD [API] | `2026-10-28 17:26:15` |
| `ANNOUNCEMENT` | `INFO` | `284.26` | 6,655.10 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 6.66K USD at 284.2600 USD [API] | `2026-10-28 18:08:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.47` (Vol: 187,900.00 USD, Dist: `+4.78%`) | Long MP=`271.80` (Vol: 166,000.00 USD, Dist: `--3.62%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--3.60%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`274.98` (Vol: 169,100.00 USD, Dist: `--2.49%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`263.68` (Vol: 277,800.00 USD, Dist: `--6.50%`)
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
| `7D` | `Long Liquidation` | `240.40` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 0.00 USD | 15.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `240.50` | 612.79 USD | 75,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.90` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.40` | 13,060,000.00 USD | 13,060,000.00 USD | 7,150.00 USD | 0.00 USD | 6.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 367.32 USD | 74,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 13,050,000.00 USD | 13,050,000.00 USD | 19,010.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 13,030,000.00 USD | 13,030,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 74,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.90` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.40` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 9,910.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 72,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `243.70` | 5,010,000.00 USD | 5,010,000.00 USD | 583.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.90` | 12,950,000.00 USD | 12,950,000.00 USD | 781.30 USD | 0.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `244.10` | 5,010,000.00 USD | 5,010,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.40` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 7.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `244.50` | 5,010,000.00 USD | 5,010,000.00 USD | 638.70 USD | 5,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 71,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `244.90` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.90` | 12,930,000.00 USD | 12,930,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `245.30` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.40` | 12,910,000.00 USD | 12,910,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 67,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.90` | 12,890,000.00 USD | 12,890,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.10` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 12,860,000.00 USD | 12,860,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.50` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.90` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.90` | 12,840,000.00 USD | 12,840,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.30` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 2,370.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.40` | 12,830,000.00 USD | 12,830,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 66,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.70` | 4,960,000.00 USD | 4,960,000.00 USD | 330.05 USD | 619.60 USD | 5.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.90` | 12,790,000.00 USD | 12,790,000.00 USD | 789.37 USD | 4,610.00 USD | 1.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.10` | 4,960,000.00 USD | 4,960,000.00 USD | 10,640.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 12,780,000.00 USD | 12,780,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.50` | 4,930,000.00 USD | 4,930,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.90` | 4,910,000.00 USD | 4,910,000.00 USD | 3,780.00 USD | 4,920.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 12,740,000.00 USD | 12,740,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.30` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 4,700.00 USD | 1.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.40` | 12,640,000.00 USD | 12,640,000.00 USD | 49,060.00 USD | 28,020.00 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.70` | 4,870,000.00 USD | 4,870,000.00 USD | 8,950.00 USD | 6.43 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 12,560,000.00 USD | 12,560,000.00 USD | 44,990.00 USD | 28,830.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.10` | 4,860,000.00 USD | 4,860,000.00 USD | 9,650.00 USD | 4,330.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 12,450,000.00 USD | 12,450,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.50` | 4,840,000.00 USD | 4,840,000.00 USD | 4,210.00 USD | 2,450.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 65,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.90` | 4,840,000.00 USD | 4,840,000.00 USD | 7,630.00 USD | 24,810.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.90` | 12,380,000.00 USD | 12,380,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,790,000.00 USD | 4,790,000.00 USD | 32,730.00 USD | 41,780.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 12,290,000.00 USD | 12,290,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 64,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,700,000.00 USD | 4,700,000.00 USD | 35,310.00 USD | 46,850.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 12,110,000.00 USD | 12,110,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,600,000.00 USD | 4,600,000.00 USD | 25,540.00 USD | 11,300.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 11,940,000.00 USD | 11,940,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,550,000.00 USD | 4,550,000.00 USD | 10,840.00 USD | 3,450.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 26,370.00 USD | 64,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,520,000.00 USD | 4,520,000.00 USD | 12,160.00 USD | 6,450.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 11,810,000.00 USD | 11,810,000.00 USD | 29,220.00 USD | 19,580.00 USD | 65.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,500,000.00 USD | 4,500,000.00 USD | 17,170.00 USD | 22,810.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 11,760,000.00 USD | 11,760,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,450,000.00 USD | 4,450,000.00 USD | 8,120.00 USD | 8,990.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 11,640,000.00 USD | 11,640,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,430,000.00 USD | 4,430,000.00 USD | 144.00 USD | 4,520.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 11,570,000.00 USD | 11,570,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,420,000.00 USD | 4,420,000.00 USD | 134.35 USD | 2,050.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 37,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,420,000.00 USD | 4,420,000.00 USD | 7,730.00 USD | 6,590.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 11,490,000.00 USD | 11,490,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,400,000.00 USD | 4,400,000.00 USD | 3,050.00 USD | 890.20 USD | 11.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 11,440,000.00 USD | 11,440,000.00 USD | 51,710.00 USD | 12,420.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,390,000.00 USD | 4,390,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 11,350,000.00 USD | 11,350,000.00 USD | 16,050.00 USD | 30,780.00 USD | 37,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,380,000.00 USD | 4,380,000.00 USD | 16,160.00 USD | 2,260.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 11,270,000.00 USD | 11,270,000.00 USD | 88,910.00 USD | 20,980.00 USD | 37,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,360,000.00 USD | 4,360,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 453.49 USD | 37,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,340,000.00 USD | 4,340,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 11,120,000.00 USD | 11,120,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,340,000.00 USD | 4,340,000.00 USD | 5,410.00 USD | 68.55 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 11,020,000.00 USD | 11,020,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 36,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,320,000.00 USD | 4,320,000.00 USD | 886.80 USD | 531.60 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 10,950,000.00 USD | 10,950,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,310,000.00 USD | 4,310,000.00 USD | 5,060.00 USD | 2,620.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 10,890,000.00 USD | 10,890,000.00 USD | 137,820.00 USD | 54,900.00 USD | 51,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,300,000.00 USD | 4,300,000.00 USD | 3,360.00 USD | 3,040.00 USD | 2.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 36,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,290,000.00 USD | 4,290,000.00 USD | 181.55 USD | 6,940.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 10,640,000.00 USD | 10,640,000.00 USD | 60,610.00 USD | 3,500.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 4,280,000.00 USD | 4,280,000.00 USD | 15,810.00 USD | 713.90 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 10,550,000.00 USD | 10,550,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 4,250,000.00 USD | 4,250,000.00 USD | 10,100.00 USD | 13,440.00 USD | 24,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 10,490,000.00 USD | 10,490,000.00 USD | 19,140.00 USD | 12,520.00 USD | 131.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 4,210,000.00 USD | 4,210,000.00 USD | 8,200.00 USD | 16,350.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 10,460,000.00 USD | 10,460,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 4,180,000.00 USD | 4,180,000.00 USD | 2,620.00 USD | 9,090.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 36,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.90` | 4,150,000.00 USD | 4,150,000.00 USD | 8,070.00 USD | 22,400.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 10,340,000.00 USD | 10,340,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 4,110,000.00 USD | 4,110,000.00 USD | 9,330.00 USD | 19,790.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 10,220,000.00 USD | 10,220,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `261.50` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `261.70` | 4,050,000.00 USD | 4,050,000.00 USD | 4,600.00 USD | 3,670.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 10,110,000.00 USD | 10,110,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 4,020,000.00 USD | 4,020,000.00 USD | 517.32 USD | 4,700.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 9,960,000.00 USD | 9,960,000.00 USD | 44,640.00 USD | 52,560.00 USD | 31.43 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 4,000,000.00 USD | 4,000,000.00 USD | 8,380.00 USD | 4,750.00 USD | 5.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,270.00 USD | 32,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,990,000.00 USD | 3,990,000.00 USD | 366.04 USD | 13,720.00 USD | 6.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 9,860,000.00 USD | 9,860,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,970,000.00 USD | 3,970,000.00 USD | 8,890.00 USD | 3,960.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 9,720,000.00 USD | 9,720,000.00 USD | 100,770.00 USD | 30,720.00 USD | 50,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `263.50` | 2,900.00 USD | 31,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,950,000.00 USD | 3,950,000.00 USD | 414.95 USD | 7,390.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 9,540,000.00 USD | 9,540,000.00 USD | 287,090.00 USD | 98,240.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,920,000.00 USD | 3,920,000.00 USD | 2,210.00 USD | 184.09 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 9,090,000.00 USD | 9,090,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,900,000.00 USD | 3,900,000.00 USD | 800.20 USD | 733.03 USD | 60,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 28,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,840,000.00 USD | 3,840,000.00 USD | 39,490.00 USD | 1,280.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 8,980,000.00 USD | 8,980,000.00 USD | 28,050.00 USD | 75,900.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,780,000.00 USD | 3,780,000.00 USD | 19,790.00 USD | 9,040.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 8,850,000.00 USD | 8,850,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.70` | 3,720,000.00 USD | 3,720,000.00 USD | 23,810.00 USD | 34,200.00 USD | 42,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 8,480,000.00 USD | 8,480,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 3,620,000.00 USD | 3,620,000.00 USD | 10,200.00 USD | 87.00 USD | 11.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 8,150,000.00 USD | 8,150,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 3,610,000.00 USD | 3,610,000.00 USD | 27,700.00 USD | 29,430.00 USD | 70,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 3,480,000.00 USD | 3,480,000.00 USD | 32,360.00 USD | 25,410.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 7,670,000.00 USD | 7,670,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 3,420,000.00 USD | 3,420,000.00 USD | 17,990.00 USD | 11,510.00 USD | 42,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 7,190,000.00 USD | 7,190,000.00 USD | 119,030.00 USD | 209,120.00 USD | 96,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 195.01 USD | 27,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 3,350,000.00 USD | 3,350,000.00 USD | 83,640.00 USD | 119,390.00 USD | 28,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 6,770,000.00 USD | 6,770,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 3,120,000.00 USD | 3,120,000.00 USD | 55,190.00 USD | 104,940.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 6,150,000.00 USD | 6,150,000.00 USD | 176,940.00 USD | 325,150.00 USD | 99,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,890,000.00 USD | 2,890,000.00 USD | 89,550.00 USD | 108,360.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,660,000.00 USD | 2,660,000.00 USD | 91,610.00 USD | 43,970.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 5,550,000.00 USD | 5,550,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,480,000.00 USD | 2,480,000.00 USD | 28,610.00 USD | 27,910.00 USD | 57,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 5,050,000.00 USD | 5,050,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 27,790.00 USD | 27,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,370,000.00 USD | 2,370,000.00 USD | 37,480.00 USD | 23,780.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 4,480,000.00 USD | 4,480,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,300,000.00 USD | 2,300,000.00 USD | 107,180.00 USD | 21,550.00 USD | 144,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 4,270,000.00 USD | 4,270,000.00 USD | 118,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,030,000.00 USD | 2,030,000.00 USD | 91,660.00 USD | 0.00 USD | 50,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `270.50` | 592.94 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.90` | 1,890,000.00 USD | 1,890,000.00 USD | 15,760.00 USD | 0.00 USD | 90,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 4,150,000.00 USD | 4,150,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 1,780,000.00 USD | 1,780,000.00 USD | 56,160.00 USD | 0.00 USD | 72,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 3,820,000.00 USD | 3,820,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 1,650,000.00 USD | 1,650,000.00 USD | 20,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 3,670,000.00 USD | 3,670,000.00 USD | 475,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 1,630,000.00 USD | 1,630,000.00 USD | 108,950.00 USD | 81.40 USD | 12.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 3,190,000.00 USD | 3,190,000.00 USD | 277,000.00 USD | 0.00 USD | 72.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 1,520,000.00 USD | 1,520,000.00 USD | 72,620.00 USD | 447.70 USD | 10.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 1,450,000.00 USD | 1,450,000.00 USD | 78,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 2,910,000.00 USD | 2,910,000.00 USD | 150,960.00 USD | 0.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 1,370,000.00 USD | 1,370,000.00 USD | 179,400.00 USD | 73.70 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 2,750,000.00 USD | 2,750,000.00 USD | 379,270.00 USD | 0.00 USD | 163,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 1,170,000.00 USD | 1,170,000.00 USD | 142,060.00 USD | 0.00 USD | 95,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 2,200,000.00 USD | 2,200,000.00 USD | 375,450.00 USD | 0.00 USD | 553.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 934,960.00 USD | 934,960.00 USD | 178,110.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 1,830,000.00 USD | 1,830,000.00 USD | 496,740.00 USD | 248,170.00 USD | 9.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 756,840.00 USD | 756,840.00 USD | 194,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 562,360.00 USD | 562,360.00 USD | 57,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 1,080,000.00 USD | 1,080,000.00 USD | 348,470.00 USD | 202,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.40` | 533,270.00 USD | 533,270.00 USD | 3,530.00 USD | 126,890.00 USD | 18.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.90` | 402,820.00 USD | 402,820.00 USD | 2,560.00 USD | 25,250.00 USD | 51.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 505,240.00 USD | 505,240.00 USD | 0.00 USD | 50,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 374,960.00 USD | 374,960.00 USD | 2,290.00 USD | 0.00 USD | 103,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 455,030.00 USD | 455,030.00 USD | 0.00 USD | 51,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 403,460.00 USD | 403,460.00 USD | 0.00 USD | 36,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 268,690.00 USD | 268,690.00 USD | 45,560.00 USD | 22,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 366,810.00 USD | 366,810.00 USD | 36,000.00 USD | 81,070.00 USD | 61,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.40` | 200,190.00 USD | 200,190.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `277.50` | 1,380.00 USD | 4,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `277.70` | 188,080.00 USD | 188,080.00 USD | 57,640.00 USD | 11,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 136,900.00 USD | 136,900.00 USD | 0.00 USD | 85,690.00 USD | 5.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 119,310.00 USD | 119,310.00 USD | 12,650.00 USD | 0.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.40` | 51,200.00 USD | 51,200.00 USD | 24,750.00 USD | 26,370.00 USD | 84.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 67,950.00 USD | 67,950.00 USD | 67,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.90` | 58,580.00 USD | 58,580.00 USD | 24,100.00 USD | 34,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 77,560.00 USD | 77,560.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 155,110.00 USD | 155,110.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.30` | 136,840.00 USD | 136,840.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.40` | 251,160.00 USD | 251,160.00 USD | 0.00 USD | 0.00 USD | 96,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.70` | 144,530.00 USD | 144,530.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.90` | 251,350.00 USD | 251,350.00 USD | 0.00 USD | 0.00 USD | 190.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.10` | 214,030.00 USD | 214,030.00 USD | 21,040.00 USD | 11,840.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.50` | 323,960.00 USD | 323,960.00 USD | 8,720.00 USD | 0.00 USD | 101,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.90` | 365,590.00 USD | 365,590.00 USD | 0.00 USD | 11,870.00 USD | 29,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.30` | 412,350.00 USD | 412,350.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 314,160.00 USD | 314,160.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.70` | 438,350.00 USD | 438,350.00 USD | 20,590.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.90` | 712,200.00 USD | 712,200.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 768,430.00 USD | 768,430.00 USD | 0.00 USD | 0.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.50` | 455,720.00 USD | 455,720.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.90` | 647,920.00 USD | 647,920.00 USD | 52,960.00 USD | 13,190.00 USD | 126,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.90` | 800,620.00 USD | 800,620.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.30` | 714,960.00 USD | 714,960.00 USD | 18,430.00 USD | 5,570.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 66,560.00 USD | 146,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.70` | 832,090.00 USD | 832,090.00 USD | 0.00 USD | 45,780.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.90` | 1,370,000.00 USD | 1,370,000.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.10` | 1,000,000.00 USD | 1,000,000.00 USD | 38,980.00 USD | 34,370.00 USD | 97,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 1,530,000.00 USD | 1,530,000.00 USD | 27,700.00 USD | 89,730.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.50` | 1,150,000.00 USD | 1,150,000.00 USD | 40,560.00 USD | 83,030.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `284.50` | 8,520.00 USD | 13,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `284.90` | 1,210,000.00 USD | 1,210,000.00 USD | 8,520.00 USD | 531.60 USD | 54,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 1,990,000.00 USD | 1,990,000.00 USD | 67,040.00 USD | 391,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 1,460,000.00 USD | 1,460,000.00 USD | 87,540.00 USD | 81,890.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 2,330,000.00 USD | 2,330,000.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 1,630,000.00 USD | 1,630,000.00 USD | 91,500.00 USD | 77,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 2,430,000.00 USD | 2,430,000.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 137,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 1,670,000.00 USD | 1,670,000.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 1,810,000.00 USD | 1,810,000.00 USD | 31,110.00 USD | 26,600.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 51,390.00 USD | 141,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 103,090.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 53,620.00 USD | 103,430.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 152.66 USD | 13,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 2,010,000.00 USD | 2,010,000.00 USD | 9,030.00 USD | 9,240.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 10,810.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 15.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 5,770.00 USD | 19,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.90` | 2,030,000.00 USD | 2,030,000.00 USD | 1,540.00 USD | 0.00 USD | 11.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 3,250,000.00 USD | 3,250,000.00 USD | 1,170.00 USD | 0.00 USD | 20.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 2,050,000.00 USD | 2,050,000.00 USD | 664.77 USD | 20,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 927.80 USD | 64.16 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `289.50` | 2,250.00 USD | 21,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `289.70` | 2,070,000.00 USD | 2,070,000.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,990.00 USD | 9.79 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 3,290,000.00 USD | 3,290,000.00 USD | 34,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 305.70 USD | 16,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 2,120,000.00 USD | 2,120,000.00 USD | 32,650.00 USD | 6,700.00 USD | 3.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 3,290,000.00 USD | 3,290,000.00 USD | 898.13 USD | 861.99 USD | 39.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 2,130,000.00 USD | 2,130,000.00 USD | 562.74 USD | 9,950.00 USD | 7.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 55,720.00 USD | 9.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.70` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 15,650.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 120,730.00 USD | 18.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 42,670.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 71,940.00 USD | 29.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 2,280,000.00 USD | 2,280,000.00 USD | 21,960.00 USD | 31,710.00 USD | 10.29 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,370,000.00 USD | 2,370,000.00 USD | 21,830.00 USD | 70,670.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 119,560.00 USD | 157.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,460,000.00 USD | 2,460,000.00 USD | 10,630.00 USD | 49,870.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 534.50 USD | 112,560.00 USD | 118.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,650,000.00 USD | 2,650,000.00 USD | 88,760.00 USD | 51,280.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 3,890,000.00 USD | 3,890,000.00 USD | 51,570.00 USD | 20,910.00 USD | 45,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,760,000.00 USD | 2,760,000.00 USD | 23,860.00 USD | 38,720.00 USD | 48,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 139,780.00 USD | 14,550.00 USD | 60,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 3,040,000.00 USD | 3,040,000.00 USD | 98,880.00 USD | 81,930.00 USD | 93,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 3,200,000.00 USD | 3,200,000.00 USD | 45,360.00 USD | 79,400.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 64,510.00 USD | 107,870.00 USD | 104,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 3,350,000.00 USD | 3,350,000.00 USD | 23,550.00 USD | 69,590.00 USD | 63,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 92,780.00 USD | 94,780.00 USD | 252,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,550,000.00 USD | 3,550,000.00 USD | 89,030.00 USD | 42,590.00 USD | 69,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 107,830.00 USD | 133,090.00 USD | 150,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,740,000.00 USD | 3,740,000.00 USD | 62,130.00 USD | 98,570.00 USD | 29,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 27,680.00 USD | 77,570.00 USD | 120,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,840,000.00 USD | 3,840,000.00 USD | 43,030.00 USD | 30,490.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,960,000.00 USD | 3,960,000.00 USD | 22,010.00 USD | 21,080.00 USD | 78,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 207,350.00 USD | 50,930.00 USD | 172,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 4,040,000.00 USD | 4,040,000.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 5,970,000.00 USD | 5,970,000.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 4,050,000.00 USD | 4,050,000.00 USD | 1,810.00 USD | 902.60 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 17,770.00 USD | 39,840.00 USD | 54,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 4,160,000.00 USD | 4,160,000.00 USD | 51,550.00 USD | 10,450.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 32,250.00 USD | 42,710.00 USD | 68,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,230,000.00 USD | 4,230,000.00 USD | 11,480.00 USD | 7,730.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,370,000.00 USD | 4,370,000.00 USD | 28,150.00 USD | 13,200.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 6,350,000.00 USD | 6,350,000.00 USD | 70,090.00 USD | 12,780.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,430,000.00 USD | 4,430,000.00 USD | 33,660.00 USD | 16,690.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 4,470.00 USD | 13,080.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,490,000.00 USD | 4,490,000.00 USD | 12,530.00 USD | 14,020.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 6,500,000.00 USD | 6,500,000.00 USD | 56,210.00 USD | 10,220.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,610,000.00 USD | 4,610,000.00 USD | 30,490.00 USD | 30,850.00 USD | 64,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 866.20 USD | 1,190.00 USD | 34.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,660,000.00 USD | 4,660,000.00 USD | 18,940.00 USD | 11,020.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,730,000.00 USD | 4,730,000.00 USD | 8,640.00 USD | 32,430.00 USD | 26,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 6,700,000.00 USD | 6,700,000.00 USD | 24,730.00 USD | 70,210.00 USD | 104,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,790,000.00 USD | 4,790,000.00 USD | 2,520.00 USD | 43,910.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 71,890.00 USD | 56,010.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,840,000.00 USD | 4,840,000.00 USD | 19,800.00 USD | 11,800.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 89,300.00 USD | 185,430.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,920,000.00 USD | 4,920,000.00 USD | 30,130.00 USD | 37,350.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 7,350,000.00 USD | 7,350,000.00 USD | 1,560.00 USD | 125,480.00 USD | 448.27 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,990,000.00 USD | 4,990,000.00 USD | 10,520.00 USD | 20,540.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 5,010,000.00 USD | 5,010,000.00 USD | 1,030.00 USD | 1,760.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 71,700.00 USD | 110,480.00 USD | 41,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 5,060,000.00 USD | 5,060,000.00 USD | 31,330.00 USD | 299.52 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 173.09 USD | 66.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 5,080,000.00 USD | 5,080,000.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 21,140.00 USD | 11,010.00 USD | 45,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 5,160,000.00 USD | 5,160,000.00 USD | 21,670.00 USD | 747.60 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 7,670,000.00 USD | 7,670,000.00 USD | 3,670.00 USD | 11,280.00 USD | 35.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 5,230,000.00 USD | 5,230,000.00 USD | 13,310.00 USD | 9,420.00 USD | 53,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 5,230,000.00 USD | 5,230,000.00 USD | 697.80 USD | 146.63 USD | 2.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 36,160.00 USD | 18,990.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 5,250,000.00 USD | 5,250,000.00 USD | 10,950.00 USD | 102.77 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 163,900.00 USD | 127,450.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 5,260,000.00 USD | 5,260,000.00 USD | 7,960.00 USD | 4,710.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 8,290,000.00 USD | 8,290,000.00 USD | 82,000.00 USD | 55,480.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 5,270,000.00 USD | 5,270,000.00 USD | 4,210.00 USD | 2,780.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 39,250.00 USD | 55,740.00 USD | 66,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 5,290,000.00 USD | 5,290,000.00 USD | 4,410.00 USD | 9,500.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,380,000.00 USD | 5,380,000.00 USD | 31,980.00 USD | 40,330.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 84,850.00 USD | 64,520.00 USD | 102,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,440,000.00 USD | 5,440,000.00 USD | 7,930.00 USD | 34,540.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 8,990,000.00 USD | 8,990,000.00 USD | 46,230.00 USD | 154,680.00 USD | 83,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 6,360.00 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,510,000.00 USD | 5,510,000.00 USD | 32,340.00 USD | 30,450.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 136,380.00 USD | 101,120.00 USD | 65,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,560,000.00 USD | 5,560,000.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 9,620,000.00 USD | 9,620,000.00 USD | 152,590.00 USD | 50,070.00 USD | 124,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,570,000.00 USD | 5,570,000.00 USD | 5,120.00 USD | 3,510.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,600,000.00 USD | 5,600,000.00 USD | 12,360.00 USD | 5,850.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 61,600.00 USD | 52,230.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 5,620,000.00 USD | 5,620,000.00 USD | 9,910.00 USD | 12,160.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 9,860,000.00 USD | 9,860,000.00 USD | 28,000.00 USD | 35,530.00 USD | 46,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 5,660,000.00 USD | 5,660,000.00 USD | 15,160.00 USD | 13,820.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 10,200,000.00 USD | 10,200,000.00 USD | 59,490.00 USD | 131,460.00 USD | 144,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 5,680,000.00 USD | 5,680,000.00 USD | 4,390.00 USD | 6,620.00 USD | 10,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 10,470,000.00 USD | 10,470,000.00 USD | 78,770.00 USD | 123,340.00 USD | 76,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 5,690,000.00 USD | 5,690,000.00 USD | 144.00 USD | 4,760.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 28,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.90` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 2.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 10,550,000.00 USD | 10,550,000.00 USD | 35,670.00 USD | 35,930.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 5,700,000.00 USD | 5,700,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.40` | 10,750,000.00 USD | 10,750,000.00 USD | 89,390.00 USD | 65,750.00 USD | 47,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 5,710,000.00 USD | 5,710,000.00 USD | 9,900.00 USD | 6,590.00 USD | 4.14 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 10,820,000.00 USD | 10,820,000.00 USD | 40,320.00 USD | 11,160.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 5,710,000.00 USD | 5,710,000.00 USD | 244.00 USD | 39.75 USD | 1.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 10,930,000.00 USD | 10,930,000.00 USD | 45,640.00 USD | 23,560.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,730,000.00 USD | 5,730,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 5,740,000.00 USD | 5,740,000.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 11,020,000.00 USD | 11,020,000.00 USD | 22,600.00 USD | 20,090.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 5,760,000.00 USD | 5,760,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.40` | 11,150,000.00 USD | 11,150,000.00 USD | 66,180.00 USD | 30,120.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 5,770,000.00 USD | 5,770,000.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 11,240,000.00 USD | 11,240,000.00 USD | 44,540.00 USD | 15,370.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 11,350,000.00 USD | 11,350,000.00 USD | 51,980.00 USD | 307.60 USD | 51,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 5,780,000.00 USD | 5,780,000.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 11,400,000.00 USD | 11,400,000.00 USD | 39,410.00 USD | 0.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 5,790,000.00 USD | 5,790,000.00 USD | 2,050.00 USD | 1,550.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.40` | 11,430,000.00 USD | 11,430,000.00 USD | 6,160.00 USD | 9,920.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 5,810,000.00 USD | 5,810,000.00 USD | 3,110.00 USD | 3,040.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 11,550,000.00 USD | 11,550,000.00 USD | 47,110.00 USD | 41,400.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 5,820,000.00 USD | 5,820,000.00 USD | 2,100.00 USD | 3,070.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 11,670,000.00 USD | 11,670,000.00 USD | 16,580.00 USD | 40,320.00 USD | 61,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 5,820,000.00 USD | 5,820,000.00 USD | 20.15 USD | 3,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.90` | 5,840,000.00 USD | 5,840,000.00 USD | 14,650.00 USD | 228.97 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 11,680,000.00 USD | 11,680,000.00 USD | 3,030.00 USD | 10,840.00 USD | 234.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.30` | 5,860,000.00 USD | 5,860,000.00 USD | 1,990.00 USD | 4,180.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.40` | 11,700,000.00 USD | 11,700,000.00 USD | 14,540.00 USD | 1,010.00 USD | 10.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.70` | 5,900,000.00 USD | 5,900,000.00 USD | 13,910.00 USD | 11,970.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 11,730,000.00 USD | 11,730,000.00 USD | 21,640.00 USD | 8,200.00 USD | 5.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.10` | 5,920,000.00 USD | 5,920,000.00 USD | 1,830.00 USD | 9,210.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 11,780,000.00 USD | 11,780,000.00 USD | 3,320.00 USD | 27,530.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.50` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 7,450.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 28,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `318.90` | 11,850,000.00 USD | 11,850,000.00 USD | 11,180.00 USD | 17,970.00 USD | 37,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.40` | 11,870,000.00 USD | 11,870,000.00 USD | 733.55 USD | 18,060.00 USD | 4.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 11,900,000.00 USD | 11,900,000.00 USD | 446.22 USD | 22,230.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 11,980,000.00 USD | 11,980,000.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 29,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.40` | 12,030,000.00 USD | 12,030,000.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 12,040,000.00 USD | 12,040,000.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 12,070,000.00 USD | 12,070,000.00 USD | 22,930.00 USD | 7,950.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 12,090,000.00 USD | 12,090,000.00 USD | 16,590.00 USD | 5,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.40` | 12,130,000.00 USD | 12,130,000.00 USD | 14,160.00 USD | 11,950.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.90` | 12,130,000.00 USD | 12,130,000.00 USD | 269.10 USD | 692.00 USD | 18.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.90` | 12,190,000.00 USD | 12,190,000.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `325.40` | 12,230,000.00 USD | 12,230,000.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `81.50` | 418,770.00 USD | 0.00 USD | 584.76 USD | `-69.86%` | `7,175,000,000.00` |
| `Live` | `Long` | `86.50` | 418,180.00 USD | 0.00 USD | 1,130.00 USD | `-68.01%` | `13,105,000,000.00` |
| `Live` | `Long` | `95.50` | 417,050.00 USD | 0.00 USD | 920.05 USD | `-64.69%` | `9,634,000,000.00` |
| `Live` | `Long` | `96.50` | 416,130.00 USD | 0.00 USD | 151.41 USD | `-64.32%` | `1,569,000,000.00` |
| `Live` | `Long` | `97.50` | 415,980.00 USD | 0.00 USD | 972.47 USD | `-63.95%` | `9,974,000,000.00` |
| `Live` | `Long` | `101.50` | 415,000.00 USD | 0.00 USD | 6,240.00 USD | `-62.47%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 408,770.00 USD | 0.00 USD | 4,080.00 USD | `-62.10%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 404,690.00 USD | 0.00 USD | 212.76 USD | `-59.51%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 404,480.00 USD | 0.00 USD | 212.35 USD | `-56.18%` | `1,792,000,000.00` |
| `Live` | `Long` | `119.50` | 404,260.00 USD | 0.00 USD | 175.66 USD | `-55.81%` | `1,470,000,000.00` |
| `Live` | `Long` | `122.50` | 404,090.00 USD | 0.00 USD | 124.46 USD | `-54.70%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 403,960.00 USD | 0.00 USD | 1,790.00 USD | `-53.22%` | `14,177,000,000.00` |
| `Live` | `Long` | `128.50` | 402,170.00 USD | 0.00 USD | 1,930.00 USD | `-52.48%` | `15,000,000,000.00` |
| `Live` | `Long` | `147.50` | 400,240.00 USD | 0.00 USD | 895.47 USD | `-45.46%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 399,350.00 USD | 0.00 USD | 1,270.00 USD | `-45.09%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 398,080.00 USD | 0.00 USD | 2,370.00 USD | `-44.72%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 395,720.00 USD | 0.00 USD | 303.78 USD | `-43.61%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 395,410.00 USD | 0.00 USD | 325.00 USD | `-39.91%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 395,090.00 USD | 0.00 USD | 648.73 USD | `-38.06%` | `3,873,000,000.00` |
| `Live` | `Long` | `169.50` | 394,440.00 USD | 0.00 USD | 8,470.00 USD | `-37.32%` | `50,000,000,000.00` |
| `Live` | `Long` | `170.50` | 385,960.00 USD | 0.00 USD | 426.25 USD | `-36.95%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 385,540.00 USD | 0.00 USD | 169.96 USD | `-35.47%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 385,370.00 USD | 0.00 USD | 516.67 USD | `-35.10%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 384,850.00 USD | 0.00 USD | 373.83 USD | `-34.73%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 384,480.00 USD | 0.00 USD | 2,030.00 USD | `-32.15%` | `11,044,000,000.00` |
| `Live` | `Long` | `184.50` | 382,450.00 USD | 0.00 USD | 616.05 USD | `-31.78%` | `3,339,000,000.00` |
| `Live` | `Long` | `188.50` | 381,830.00 USD | 0.00 USD | 418.28 USD | `-30.30%` | `2,219,000,000.00` |
| `Live` | `Long` | `191.50` | 381,420.00 USD | 0.00 USD | 858.49 USD | `-29.19%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 380,560.00 USD | 0.00 USD | 1,490.00 USD | `-28.82%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 379,070.00 USD | 0.00 USD | 7,540.00 USD | `-27.71%` | `38,561,000,000.00` |
| `Live` | `Long` | `199.50` | 371,530.00 USD | 0.00 USD | 548.03 USD | `-26.23%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 370,990.00 USD | 0.00 USD | 293.13 USD | `-25.86%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 370,690.00 USD | 0.00 USD | 420.39 USD | `-25.12%` | `2,076,000,000.00` |
| `Live` | `Long` | `204.50` | 370,270.00 USD | 0.00 USD | 39,880.00 USD | `-24.38%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 330,390.00 USD | 0.00 USD | 191.53 USD | `-24.01%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 330,200.00 USD | 0.00 USD | 619.50 USD | `-23.64%` | `3,000,000,000.00` |
| `Live` | `Long` | `207.50` | 329,580.00 USD | 0.00 USD | 188,820.00 USD | `-23.27%` | `909,952,000,000.00` |
| `Live` | `Long` | `210.50` | 140,760.00 USD | 0.00 USD | 6,740.00 USD | `-22.16%` | `32,017,000,000.00` |
| `Live` | `Long` | `213.50` | 134,020.00 USD | 0.00 USD | 3,800.00 USD | `-21.05%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 130,220.00 USD | 0.00 USD | 239.85 USD | `-20.31%` | `1,113,000,000.00` |
| `Live` | `Long` | `218.50` | 129,980.00 USD | 0.00 USD | 626.88 USD | `-19.20%` | `2,869,000,000.00` |
| `Live` | `Long` | `220.50` | 129,350.00 USD | 0.00 USD | 2,300.00 USD | `-18.46%` | `10,419,000,000.00` |
| `Live` | `Long` | `223.50` | 127,050.00 USD | 0.00 USD | 32,860.00 USD | `-17.35%` | `147,023,000,000.00` |
| `Live` | `Long` | `225.50` | 94,200.00 USD | 0.00 USD | 5,370.00 USD | `-16.61%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 88,830.00 USD | 0.00 USD | 1,240.00 USD | `-16.24%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 87,590.00 USD | 0.00 USD | 174.49 USD | `-15.87%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 87,420.00 USD | 0.00 USD | 2,050.00 USD | `-15.50%` | `8,967,000,000.00` |
| `Live` | `Long` | `229.50` | 85,370.00 USD | 0.00 USD | 1,300.00 USD | `-15.14%` | `5,671,000,000.00` |
| `Live` | `Long` | `231.50` | 84,070.00 USD | 0.00 USD | 295.86 USD | `-14.40%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 83,770.00 USD | 0.00 USD | 1,010.00 USD | `-14.03%` | `4,348,000,000.00` |
| `Live` | `Long` | `234.50` | 82,760.00 USD | 0.00 USD | 217.85 USD | `-13.29%` | `929,000,000.00` |
| `Live` | `Long` | `235.50` | 82,540.00 USD | 0.00 USD | 6,140.00 USD | `-12.92%` | `26,061,000,000.00` |
| `Live` | `Long` | `239.50` | 76,410.00 USD | 0.00 USD | 1,030.00 USD | `-11.44%` | `4,281,000,000.00` |
| `Live` | `Long` | `240.50` | 75,380.00 USD | 0.00 USD | 612.79 USD | `-11.07%` | `2,548,000,000.00` |
| `Live` | `Long` | `241.50` | 74,770.00 USD | 0.00 USD | 367.32 USD | `-10.70%` | `1,521,000,000.00` |
| `Live` | `Long` | `242.50` | 74,400.00 USD | 0.00 USD | 1,520.00 USD | `-10.33%` | `6,274,000,000.00` |
| `Live` | `Long` | `243.50` | 72,880.00 USD | 0.00 USD | 1,200.00 USD | `-9.96%` | `4,937,000,000.00` |
| `Live` | `Long` | `244.50` | 71,680.00 USD | 0.00 USD | 4,220.00 USD | `-9.59%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 67,450.00 USD | 0.00 USD | 1,030.00 USD | `-9.22%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 66,430.00 USD | 0.00 USD | 699.44 USD | `-8.48%` | `2,826,000,000.00` |
| `Live` | `Long` | `250.50` | 65,730.00 USD | 0.00 USD | 1,330.00 USD | `-7.37%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 64,400.00 USD | 0.00 USD | 268.35 USD | `-7.00%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 64,130.00 USD | 0.00 USD | 26,370.00 USD | `-6.63%` | `104,453,000,000.00` |
| `Live` | `Long` | `254.50` | 37,760.00 USD | 0.00 USD | 362.92 USD | `-5.89%` | `1,426,000,000.00` |
| `Live` | `Long` | `256.50` | 37,390.00 USD | 0.00 USD | 453.49 USD | `-5.15%` | `1,768,000,000.00` |
| `Live` | `Long` | `257.50` | 36,940.00 USD | 0.00 USD | 366.42 USD | `-4.78%` | `1,423,000,000.00` |
| `Live` | `Long` | `258.50` | 36,570.00 USD | 0.00 USD | 278.15 USD | `-4.41%` | `1,076,000,000.00` |
| `Live` | `Long` | `260.50` | 36,300.00 USD | 0.00 USD | 3,860.00 USD | `-3.67%` | `14,816,000,000.00` |
| `Live` | `Short` | `261.50` | 2,850.00 USD | 2,850.00 USD | 0.00 USD | `-3.30%` | `10,912,000,000.00` |
| `Live` | `Long` | `262.50` | 32,440.00 USD | 0.00 USD | 1,270.00 USD | `-2.93%` | `4,824,000,000.00` |
| `Live` | `Long` | `263.50` | 31,170.00 USD | 0.00 USD | 2,900.00 USD | `-2.56%` | `11,019,000,000.00` |
| `Live` | `Long` | `264.50` | 28,270.00 USD | 0.00 USD | 280.37 USD | `-2.19%` | `1,060,000,000.00` |
| `Live` | `Long` | `267.50` | 27,990.00 USD | 0.00 USD | 195.01 USD | `-1.08%` | `729,000,000.00` |
| `Live` | `Long` | `269.50` | 27,790.00 USD | 0.00 USD | 27,790.00 USD | `-0.34%` | `103,123,000,000.00` |
| `Live` | `Short` | `270.50` | 3,450.00 USD | 592.94 USD | 0.00 USD | `+0.03%` | `2,192,000,000.00` |
| `Live` | `Short` | `277.50` | 4,830.00 USD | 1,380.00 USD | 0.00 USD | `+2.61%` | `4,973,000,000.00` |
| `Live` | `Short` | `284.50` | 13,350.00 USD | 8,520.00 USD | 0.00 USD | `+5.20%` | `29,945,000,000.00` |
| `Live` | `Short` | `287.50` | 13,500.00 USD | 152.66 USD | 0.00 USD | `+6.31%` | `531,000,000.00` |
| `Live` | `Short` | `288.50` | 19,270.00 USD | 5,770.00 USD | 0.00 USD | `+6.68%` | `20,000,000,000.00` |
| `Live` | `Short` | `289.50` | 21,520.00 USD | 2,250.00 USD | 0.00 USD | `+7.05%` | `7,783,000,000.00` |
| `Live` | `Short` | `307.50` | 27,880.00 USD | 6,360.00 USD | 0.00 USD | `+13.71%` | `20,668,000,000.00` |
| `Live` | `Short` | `310.50` | 28,390.00 USD | 517.91 USD | 0.00 USD | `+14.82%` | `1,668,000,000.00` |
| `Live` | `Short` | `318.50` | 28,510.00 USD | 114.34 USD | 0.00 USD | `+17.78%` | `359,000,000.00` |
| `Live` | `Short` | `320.50` | 29,620.00 USD | 1,110.00 USD | 0.00 USD | `+18.51%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 29,890.00 USD | 276.63 USD | 0.00 USD | `+22.21%` | `837,000,000.00` |
| `Live` | `Short` | `337.50` | 31,240.00 USD | 1,350.00 USD | 0.00 USD | `+24.80%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 32,250.00 USD | 1,010.00 USD | 0.00 USD | `+32.57%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 32,700.00 USD | 445.52 USD | 0.00 USD | `+36.26%` | `1,209,000,000.00` |
| `Live` | `Short` | `379.50` | 74,440.00 USD | 41,740.00 USD | 0.00 USD | `+40.33%` | `110,000,000,000.00` |
| `Live` | `Short` | `432.50` | 83,250.00 USD | 8,810.00 USD | 0.00 USD | `+59.93%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 129,500.00 USD | 46,250.00 USD | 0.00 USD | `+69.91%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 137,700.00 USD | 8,200.00 USD | 0.00 USD | `+76.57%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 138,420.00 USD | 718.34 USD | 0.00 USD | `+84.34%` | `1,441,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 138,170.00 USD | 0.00 USD | 210.94 USD | `-46.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 137,960.00 USD | 0.00 USD | 2,070.00 USD | `-46.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 135,890.00 USD | 0.00 USD | 2,530.00 USD | `-33.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 133,360.00 USD | 0.00 USD | 490.59 USD | `-31.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 132,870.00 USD | 0.00 USD | 482.01 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 132,390.00 USD | 0.00 USD | 189.07 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 132,200.00 USD | 0.00 USD | 441.60 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 131,760.00 USD | 0.00 USD | 703.49 USD | `-22.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 131,060.00 USD | 0.00 USD | 638.36 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 130,420.00 USD | 0.00 USD | 740.85 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 129,680.00 USD | 0.00 USD | 1,050.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 128,630.00 USD | 0.00 USD | 389.48 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 128,240.00 USD | 0.00 USD | 812.38 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 127,430.00 USD | 0.00 USD | 220.64 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 127,210.00 USD | 0.00 USD | 429.30 USD | `-11.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 126,780.00 USD | 0.00 USD | 296.50 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 126,480.00 USD | 0.00 USD | 216.45 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 126,260.00 USD | 0.00 USD | 387.76 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 125,880.00 USD | 0.00 USD | 366.75 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 125,510.00 USD | 0.00 USD | 1,630.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 123,880.00 USD | 0.00 USD | 2,700.00 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 121,180.00 USD | 0.00 USD | 2,940.00 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 118,240.00 USD | 0.00 USD | 4,680.00 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 113,560.00 USD | 0.00 USD | 3,590.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 109,970.00 USD | 0.00 USD | 231.54 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 109,730.00 USD | 0.00 USD | 109.26 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 109,630.00 USD | 0.00 USD | 1,780.00 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 107,850.00 USD | 0.00 USD | 51,300.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 56,550.00 USD | 0.00 USD | 250.81 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 56,300.00 USD | 0.00 USD | 707.78 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 55,590.00 USD | 0.00 USD | 857.85 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 54,730.00 USD | 0.00 USD | 7,790.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 46,940.00 USD | 0.00 USD | 122.99 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 46,810.00 USD | 0.00 USD | 455.86 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 46,360.00 USD | 0.00 USD | 10,490.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 35,870.00 USD | 0.00 USD | 2,120.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 33,760.00 USD | 0.00 USD | 6,440.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 27,320.00 USD | 0.00 USD | 27,320.00 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `270.50` | 331.63 USD | 331.63 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `271.50` | 601.23 USD | 269.60 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `272.50` | 14,100.00 USD | 13,500.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `273.50` | 15,570.00 USD | 1,470.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `274.50` | 15,900.00 USD | 336.54 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `275.50` | 16,200.00 USD | 299.74 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `276.50` | 17,110.00 USD | 903.60 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `277.50` | 17,490.00 USD | 384.34 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `278.50` | 17,620.00 USD | 125.88 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `279.50` | 39,610.00 USD | 21,990.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 42,970.00 USD | 3,370.00 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 43,110.00 USD | 133.43 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 44,410.00 USD | 1,300.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 52,450.00 USD | 8,040.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 54,460.00 USD | 2,010.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 62,150.00 USD | 7,690.00 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 67,230.00 USD | 5,080.00 USD | 0.00 USD | `+5.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 70,370.00 USD | 3,140.00 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 70,510.00 USD | 139.92 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 70,660.00 USD | 153.44 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 99,680.00 USD | 29,020.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 124,960.00 USD | 25,280.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 143,210.00 USD | 18,250.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 143,620.00 USD | 407.88 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 216,060.00 USD | 72,450.00 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 216,640.00 USD | 581.14 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 217,030.00 USD | 388.95 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 226,720.00 USD | 9,690.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 237,450.00 USD | 10,730.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 240,100.00 USD | 2,650.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 241,160.00 USD | 1,060.00 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 241,260.00 USD | 102.73 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 255,750.00 USD | 14,500.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 256,390.00 USD | 634.04 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 257,420.00 USD | 1,030.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 263,070.00 USD | 5,650.00 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 263,190.00 USD | 118.85 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 263,730.00 USD | 534.59 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 264,050.00 USD | 321.50 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 328,970.00 USD | 64,920.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 330,060.00 USD | 1,090.00 USD | 0.00 USD | `+22.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 330,610.00 USD | 547.52 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 330,740.00 USD | 138.20 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 331,000.00 USD | 257.45 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 331,180.00 USD | 174.25 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 331,330.00 USD | 151.50 USD | 0.00 USD | `+29.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 332,780.00 USD | 1,450.00 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 334,550.00 USD | 1,770.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 334,880.00 USD | 326.07 USD | 0.00 USD | `+33.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 335,710.00 USD | 826.60 USD | 0.00 USD | `+34.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 343,150.00 USD | 7,440.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 343,830.00 USD | 682.84 USD | 0.00 USD | `+36.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 344,930.00 USD | 1,100.00 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 345,620.00 USD | 683.96 USD | 0.00 USD | `+46.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 345,820.00 USD | 199.75 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 348,490.00 USD | 2,670.00 USD | 0.00 USD | `+48.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 349,530.00 USD | 1,040.00 USD | 0.00 USD | `+49.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 349,900.00 USD | 376.71 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 350,060.00 USD | 158.86 USD | 0.00 USD | `+51.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 355,960.00 USD | 5,900.00 USD | 0.00 USD | `+53.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 357,040.00 USD | 1,080.00 USD | 0.00 USD | `+56.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 358,740.00 USD | 1,700.00 USD | 0.00 USD | `+57.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 360,300.00 USD | 1,550.00 USD | 0.00 USD | `+59.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 361,680.00 USD | 1,380.00 USD | 0.00 USD | `+61.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 362,300.00 USD | 621.14 USD | 0.00 USD | `+61.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 365,680.00 USD | 3,380.00 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 365,900.00 USD | 222.75 USD | 0.00 USD | `+64.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 371,490.00 USD | 5,590.00 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 377,410.00 USD | 5,920.00 USD | 0.00 USD | `+66.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 378,540.00 USD | 1,130.00 USD | 0.00 USD | `+70.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 386,180.00 USD | 7,630.00 USD | 0.00 USD | `+78.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 387,150.00 USD | 975.00 USD | 0.00 USD | `+80.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 388,130.00 USD | 981.00 USD | 0.00 USD | `+81.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 388,630.00 USD | 499.50 USD | 0.00 USD | `+84.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,280,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+85.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,280,000.00 USD | 1,000.00 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,280,000.00 USD | 1,040.00 USD | 0.00 USD | `+91.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,280,000.00 USD | 340.67 USD | 0.00 USD | `+93.21%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `240.40` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 0.00 USD | 0.00 USD | 15.48 USD |
| `7D` | `240.90` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD |
| `7D` | `241.40` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 7,150.00 USD | 0.00 USD | 6.98 USD |
| `7D` | `241.90` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 19,010.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.40` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD |
| `7D` | `242.90` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.40` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 0.00 USD | 9,910.00 USD | 5,480.00 USD |
| `1D` | `243.70` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 583.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `243.90` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 781.30 USD | 0.00 USD | 20,800.00 USD |
| `1D` | `244.10` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD |
| `7D` | `244.40` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 7.19 USD |
| `1D` | `244.50` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 638.70 USD | 5,270.00 USD | 0.00 USD |
| `1D` | `244.90` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 12,330.00 USD |
| `7D` | `244.90` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD |
| `1D` | `245.30` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `245.40` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD |
| `7D` | `245.90` | 12,890,000.00 USD | 0.00 USD | 12,890,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD |
| `1D` | `246.10` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD |
| `7D` | `246.40` | 12,860,000.00 USD | 0.00 USD | 12,860,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,700.00 USD |
| `1D` | `246.50` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `1D` | `246.90` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `7D` | `246.90` | 12,840,000.00 USD | 0.00 USD | 12,840,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,730.00 USD |
| `1D` | `247.30` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 0.00 USD | 2,370.00 USD | 7,240.00 USD |
| `7D` | `247.40` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,710.00 USD |
| `1D` | `247.70` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 330.05 USD | 619.60 USD | 5.98 USD |
| `7D` | `247.90` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 789.37 USD | 4,610.00 USD | 1.59 USD |
| `1D` | `248.10` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 10,640.00 USD | 0.00 USD | 23,990.00 USD |
| `7D` | `248.40` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,890.00 USD |
| `1D` | `248.50` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD |
| `1D` | `248.90` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 3,780.00 USD | 4,920.00 USD | 26,840.00 USD |
| `7D` | `248.90` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD |
| `1D` | `249.30` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 0.00 USD | 4,700.00 USD | 1.70 USD |
| `7D` | `249.40` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 49,060.00 USD | 28,020.00 USD | 3,990.00 USD |
| `1D` | `249.70` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 8,950.00 USD | 6.43 USD | 2,010.00 USD |
| `7D` | `249.90` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 44,990.00 USD | 28,830.00 USD | 35,180.00 USD |
| `1D` | `250.10` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 9,650.00 USD | 4,330.00 USD | 3,410.00 USD |
| `7D` | `250.40` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,480.00 USD |
| `1D` | `250.50` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 4,210.00 USD | 2,450.00 USD | 1,340.00 USD |
| `1D` | `250.90` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 7,630.00 USD | 24,810.00 USD | 9,490.00 USD |
| `7D` | `250.90` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,650.00 USD |
| `1D` | `251.30` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 32,730.00 USD | 41,780.00 USD | 20,490.00 USD |
| `7D` | `251.40` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,230.00 USD |
| `1D` | `251.70` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 35,310.00 USD | 46,850.00 USD | 16,060.00 USD |
| `7D` | `251.90` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,240.00 USD |
| `1D` | `252.10` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 25,540.00 USD | 11,300.00 USD | 16,370.00 USD |
| `7D` | `252.40` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,050.00 USD |
| `1D` | `252.50` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 10,840.00 USD | 3,450.00 USD | 7,750.00 USD |
| `1D` | `252.90` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 12,160.00 USD | 6,450.00 USD | 2,980.00 USD |
| `7D` | `252.90` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 29,220.00 USD | 19,580.00 USD | 65.75 USD |
| `1D` | `253.30` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 17,170.00 USD | 22,810.00 USD | 8,230.00 USD |
| `7D` | `253.40` | 11,760,000.00 USD | 0.00 USD | 11,760,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD |
| `1D` | `253.70` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 8,120.00 USD | 8,990.00 USD | 11,920.00 USD |
| `7D` | `253.90` | 11,640,000.00 USD | 0.00 USD | 11,640,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,900.00 USD |
| `1D` | `254.10` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 144.00 USD | 4,520.00 USD | 3,930.00 USD |
| `7D` | `254.40` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,870.00 USD |
| `1D` | `254.50` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 134.35 USD | 2,050.00 USD | 2.31 USD |
| `1D` | `254.90` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 7,730.00 USD | 6,590.00 USD | 2,760.00 USD |
| `7D` | `254.90` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,170.00 USD |
| `1D` | `255.30` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 3,050.00 USD | 890.20 USD | 11.05 USD |
| `7D` | `255.40` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 51,710.00 USD | 12,420.00 USD | 23,800.00 USD |
| `1D` | `255.70` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD |
| `7D` | `255.90` | 11,350,000.00 USD | 0.00 USD | 11,350,000.00 USD | 16,050.00 USD | 30,780.00 USD | 37,410.00 USD |
| `1D` | `256.10` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 16,160.00 USD | 2,260.00 USD | 0.96 USD |
| `7D` | `256.40` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 88,910.00 USD | 20,980.00 USD | 37,410.00 USD |
| `1D` | `256.50` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `1D` | `256.90` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD |
| `7D` | `256.90` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,910.00 USD |
| `1D` | `257.30` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 5,410.00 USD | 68.55 USD | 11,750.00 USD |
| `7D` | `257.40` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,320.00 USD |
| `1D` | `257.70` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 886.80 USD | 531.60 USD | 4,830.00 USD |
| `7D` | `257.90` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,280.00 USD |
| `1D` | `258.10` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 5,060.00 USD | 2,620.00 USD | 6,860.00 USD |
| `7D` | `258.40` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 137,820.00 USD | 54,900.00 USD | 51,750.00 USD |
| `1D` | `258.50` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 3,360.00 USD | 3,040.00 USD | 2.55 USD |
| `1D` | `258.90` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 181.55 USD | 6,940.00 USD | 5,600.00 USD |
| `7D` | `258.90` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 60,610.00 USD | 3,500.00 USD | 34,370.00 USD |
| `1D` | `259.30` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 15,810.00 USD | 713.90 USD | 7,660.00 USD |
| `7D` | `259.40` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,230.00 USD |
| `1D` | `259.70` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 10,100.00 USD | 13,440.00 USD | 24,240.00 USD |
| `7D` | `259.90` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 19,140.00 USD | 12,520.00 USD | 131.11 USD |
| `1D` | `260.10` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 8,200.00 USD | 16,350.00 USD | 6,870.00 USD |
| `7D` | `260.40` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,090.00 USD |
| `1D` | `260.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 2,620.00 USD | 9,090.00 USD | 10,400.00 USD |
| `1D` | `260.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 8,070.00 USD | 22,400.00 USD | 13,930.00 USD |
| `7D` | `260.90` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,900.00 USD |
| `1D` | `261.30` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 9,330.00 USD | 19,790.00 USD | 31,350.00 USD |
| `7D` | `261.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,430.00 USD |
| `1D` | `261.70` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 4,600.00 USD | 3,670.00 USD | 19,360.00 USD |
| `7D` | `261.90` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,290.00 USD |
| `1D` | `262.10` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 517.32 USD | 4,700.00 USD | 13,920.00 USD |
| `7D` | `262.40` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 44,640.00 USD | 52,560.00 USD | 31.43 USD |
| `1D` | `262.50` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 8,380.00 USD | 4,750.00 USD | 5.26 USD |
| `1D` | `262.90` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 366.04 USD | 13,720.00 USD | 6.97 USD |
| `7D` | `262.90` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,750.00 USD |
| `1D` | `263.30` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 8,890.00 USD | 3,960.00 USD | 16,180.00 USD |
| `7D` | `263.40` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 100,770.00 USD | 30,720.00 USD | 50,090.00 USD |
| `1D` | `263.70` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 414.95 USD | 7,390.00 USD | 16,160.00 USD |
| `7D` | `263.90` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 287,090.00 USD | 98,240.00 USD | 57,810.00 USD |
| `1D` | `264.10` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 2,210.00 USD | 184.09 USD | 18,120.00 USD |
| `7D` | `264.40` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,190.00 USD |
| `1D` | `264.50` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 800.20 USD | 733.03 USD | 60,000.00 USD |
| `1D` | `264.90` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 39,490.00 USD | 1,280.00 USD | 15,630.00 USD |
| `7D` | `264.90` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 28,050.00 USD | 75,900.00 USD | 27,300.00 USD |
| `1D` | `265.30` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 19,790.00 USD | 9,040.00 USD | 33,450.00 USD |
| `7D` | `265.40` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,820.00 USD |
| `1D` | `265.70` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 23,810.00 USD | 34,200.00 USD | 42,350.00 USD |
| `7D` | `265.90` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,690.00 USD |
| `1D` | `266.10` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 10,200.00 USD | 87.00 USD | 11.92 USD |
| `7D` | `266.40` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,540.00 USD |
| `1D` | `266.50` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 27,700.00 USD | 29,430.00 USD | 70,400.00 USD |
| `1D` | `266.90` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 32,360.00 USD | 25,410.00 USD | 6,770.00 USD |
| `7D` | `266.90` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,390.00 USD |
| `1D` | `267.30` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 17,990.00 USD | 11,510.00 USD | 42,060.00 USD |
| `7D` | `267.40` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 119,030.00 USD | 209,120.00 USD | 96,460.00 USD |
| `1D` | `267.70` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 83,640.00 USD | 119,390.00 USD | 28,560.00 USD |
| `7D` | `267.90` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,270.00 USD |
| `1D` | `268.10` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 55,190.00 USD | 104,940.00 USD | 64,060.00 USD |
| `7D` | `268.40` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 176,940.00 USD | 325,150.00 USD | 99,630.00 USD |
| `1D` | `268.50` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 89,550.00 USD | 108,360.00 USD | 31,670.00 USD |
| `1D` | `268.90` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 91,610.00 USD | 43,970.00 USD | 41,690.00 USD |
| `7D` | `268.90` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,300.00 USD |
| `1D` | `269.30` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 28,610.00 USD | 27,910.00 USD | 57,070.00 USD |
| `7D` | `269.40` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,070.00 USD |
| `1D` | `269.70` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 37,480.00 USD | 23,780.00 USD | 8,620.00 USD |
| `7D` | `269.90` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD |
| `1D` | `270.10` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 107,180.00 USD | 21,550.00 USD | 144,890.00 USD |
| `7D` | `270.40` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 118,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `270.50` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 91,660.00 USD | 0.00 USD | 50,040.00 USD |
| `1D` | `270.90` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 15,760.00 USD | 0.00 USD | 90,780.00 USD |
| `7D` | `270.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.30` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 56,160.00 USD | 0.00 USD | 72,980.00 USD |
| `7D` | `271.40` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.70` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 20,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `271.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 475,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.10` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 108,950.00 USD | 81.40 USD | 12.62 USD |
| `7D` | `272.40` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 277,000.00 USD | 0.00 USD | 72.74 USD |
| `1D` | `272.50` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 72,620.00 USD | 447.70 USD | 10.02 USD |
| `1D` | `272.90` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 78,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `272.90` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 150,960.00 USD | 0.00 USD | 15,490.00 USD |
| `1D` | `273.30` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 179,400.00 USD | 73.70 USD | 16,110.00 USD |
| `7D` | `273.40` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 379,270.00 USD | 0.00 USD | 163,470.00 USD |
| `1D` | `273.70` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 142,060.00 USD | 0.00 USD | 95,820.00 USD |
| `7D` | `273.90` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 375,450.00 USD | 0.00 USD | 553.39 USD |
| `1D` | `274.10` | 934,960.00 USD | 0.00 USD | 934,960.00 USD | 178,110.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `274.40` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 496,740.00 USD | 248,170.00 USD | 9.16 USD |
| `1D` | `274.50` | 756,840.00 USD | 0.00 USD | 756,840.00 USD | 194,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.90` | 562,360.00 USD | 0.00 USD | 562,360.00 USD | 57,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 348,470.00 USD | 202,210.00 USD | 0.00 USD |
| `7D` | `275.40` | 533,270.00 USD | 0.00 USD | 533,270.00 USD | 3,530.00 USD | 126,890.00 USD | 18.34 USD |
| `7D` | `275.90` | 402,820.00 USD | 0.00 USD | 402,820.00 USD | 2,560.00 USD | 25,250.00 USD | 51.84 USD |
| `1D` | `276.10` | 505,240.00 USD | 0.00 USD | 505,240.00 USD | 0.00 USD | 50,210.00 USD | 0.00 USD |
| `7D` | `276.40` | 374,960.00 USD | 0.00 USD | 374,960.00 USD | 2,290.00 USD | 0.00 USD | 103,970.00 USD |
| `1D` | `276.50` | 455,030.00 USD | 0.00 USD | 455,030.00 USD | 0.00 USD | 51,570.00 USD | 0.00 USD |
| `1D` | `276.90` | 403,460.00 USD | 0.00 USD | 403,460.00 USD | 0.00 USD | 36,650.00 USD | 0.00 USD |
| `7D` | `276.90` | 268,690.00 USD | 0.00 USD | 268,690.00 USD | 45,560.00 USD | 22,950.00 USD | 0.00 USD |
| `1D` | `277.30` | 366,810.00 USD | 0.00 USD | 366,810.00 USD | 36,000.00 USD | 81,070.00 USD | 61,670.00 USD |
| `7D` | `277.40` | 200,190.00 USD | 0.00 USD | 200,190.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD |
| `1D` | `277.70` | 188,080.00 USD | 0.00 USD | 188,080.00 USD | 57,640.00 USD | 11,130.00 USD | 0.00 USD |
| `7D` | `277.90` | 136,900.00 USD | 0.00 USD | 136,900.00 USD | 0.00 USD | 85,690.00 USD | 5.83 USD |
| `1D` | `278.10` | 119,310.00 USD | 0.00 USD | 119,310.00 USD | 12,650.00 USD | 0.00 USD | 38,710.00 USD |
| `7D` | `278.40` | 51,200.00 USD | 0.00 USD | 51,200.00 USD | 24,750.00 USD | 26,370.00 USD | 84.37 USD |
| `1D` | `278.50` | 67,950.00 USD | 0.00 USD | 67,950.00 USD | 67,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `278.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `278.90` | 58,580.00 USD | 58,580.00 USD | 0.00 USD | 24,100.00 USD | 34,490.00 USD | 0.00 USD |
| `7D` | `278.90` | 77,560.00 USD | 77,560.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD |
| `7D` | `278.90` | 155,110.00 USD | 155,110.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD |
| `1D` | `279.30` | 136,840.00 USD | 136,840.00 USD | 0.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD |
| `7D` | `279.40` | 251,160.00 USD | 251,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 96,050.00 USD |
| `1D` | `279.70` | 144,530.00 USD | 144,530.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |
| `7D` | `279.90` | 251,350.00 USD | 251,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 190.97 USD |
| `1D` | `280.10` | 214,030.00 USD | 214,030.00 USD | 0.00 USD | 21,040.00 USD | 11,840.00 USD | 36,620.00 USD |
| `1D` | `280.50` | 323,960.00 USD | 323,960.00 USD | 0.00 USD | 8,720.00 USD | 0.00 USD | 101,210.00 USD |
| `1D` | `280.90` | 365,590.00 USD | 365,590.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 29,760.00 USD |
| `1D` | `281.30` | 412,350.00 USD | 412,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD |
| `7D` | `281.40` | 314,160.00 USD | 314,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.70` | 438,350.00 USD | 438,350.00 USD | 0.00 USD | 20,590.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.90` | 712,200.00 USD | 712,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD |
| `7D` | `282.40` | 768,430.00 USD | 768,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,240.00 USD |
| `1D` | `282.50` | 455,720.00 USD | 455,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD |
| `1D` | `282.90` | 647,920.00 USD | 647,920.00 USD | 0.00 USD | 52,960.00 USD | 13,190.00 USD | 126,060.00 USD |
| `7D` | `282.90` | 800,620.00 USD | 800,620.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.30` | 714,960.00 USD | 714,960.00 USD | 0.00 USD | 18,430.00 USD | 5,570.00 USD | 43,040.00 USD |
| `7D` | `283.40` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 146,490.00 USD |
| `1D` | `283.70` | 832,090.00 USD | 832,090.00 USD | 0.00 USD | 0.00 USD | 45,780.00 USD | 71,340.00 USD |
| `7D` | `283.90` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD |
| `1D` | `284.10` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 38,980.00 USD | 34,370.00 USD | 97,960.00 USD |
| `7D` | `284.40` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 27,700.00 USD | 89,730.00 USD | 42,790.00 USD |
| `1D` | `284.50` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 40,560.00 USD | 83,030.00 USD | 20,690.00 USD |
| `1D` | `284.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 8,520.00 USD | 531.60 USD | 54,520.00 USD |
| `7D` | `284.90` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 67,040.00 USD | 391,180.00 USD | 0.00 USD |
| `1D` | `285.30` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 87,540.00 USD | 81,890.00 USD | 80,720.00 USD |
| `7D` | `285.40` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD |
| `1D` | `285.70` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 91,500.00 USD | 77,040.00 USD | 0.00 USD |
| `7D` | `285.90` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD |
| `1D` | `286.10` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,110.00 USD |
| `7D` | `286.40` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 137,400.00 USD | 0.00 USD |
| `1D` | `286.50` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD |
| `1D` | `286.90` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 31,110.00 USD | 26,600.00 USD | 80,690.00 USD |
| `7D` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 51,390.00 USD | 141,160.00 USD | 0.00 USD |
| `1D` | `287.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 103,090.00 USD | 26,570.00 USD |
| `7D` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 53,620.00 USD | 103,430.00 USD | 53,270.00 USD |
| `1D` | `287.70` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 9,030.00 USD | 9,240.00 USD | 47,790.00 USD |
| `7D` | `287.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD |
| `1D` | `288.10` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 10,810.00 USD | 8,690.00 USD |
| `7D` | `288.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.48 USD |
| `1D` | `288.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD |
| `1D` | `288.90` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | 11.96 USD |
| `7D` | `288.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 20.83 USD |
| `1D` | `289.30` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 664.77 USD | 20,430.00 USD | 0.00 USD |
| `7D` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 64.16 USD |
| `1D` | `289.70` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD |
| `7D` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | 9.79 USD |
| `7D` | `290.40` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 34,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.50` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 305.70 USD | 16,960.00 USD |
| `1D` | `290.90` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 32,650.00 USD | 6,700.00 USD | 3.40 USD |
| `7D` | `290.90` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 39.31 USD |
| `1D` | `291.30` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 562.74 USD | 9,950.00 USD | 7.76 USD |
| `7D` | `291.40` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 55,720.00 USD | 9.50 USD |
| `1D` | `291.70` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 15,650.00 USD | 22,140.00 USD |
| `7D` | `291.90` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 18.74 USD |
| `1D` | `292.10` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 42,670.00 USD | 8,120.00 USD |
| `7D` | `292.40` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 71,940.00 USD | 29.00 USD |
| `1D` | `292.50` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 21,960.00 USD | 31,710.00 USD | 10.29 USD |
| `1D` | `292.90` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 21,830.00 USD | 70,670.00 USD | 3.04 USD |
| `7D` | `292.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 119,560.00 USD | 157.62 USD |
| `1D` | `293.30` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 10,630.00 USD | 49,870.00 USD | 27,360.00 USD |
| `7D` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 118.35 USD |
| `1D` | `293.70` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 88,760.00 USD | 51,280.00 USD | 53,800.00 USD |
| `7D` | `293.90` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,070.00 USD |
| `1D` | `294.10` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 23,860.00 USD | 38,720.00 USD | 48,840.00 USD |
| `7D` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 139,780.00 USD | 14,550.00 USD | 60,690.00 USD |
| `1D` | `294.50` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 98,880.00 USD | 81,930.00 USD | 93,000.00 USD |
| `1D` | `294.90` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 45,360.00 USD | 79,400.00 USD | 35,620.00 USD |
| `7D` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 64,510.00 USD | 107,870.00 USD | 104,950.00 USD |
| `1D` | `295.30` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 23,550.00 USD | 69,590.00 USD | 63,240.00 USD |
| `7D` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 252,160.00 USD |
| `1D` | `295.70` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 89,030.00 USD | 42,590.00 USD | 69,660.00 USD |
| `7D` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 107,830.00 USD | 133,090.00 USD | 150,810.00 USD |
| `1D` | `296.10` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 62,130.00 USD | 98,570.00 USD | 29,590.00 USD |
| `7D` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 27,680.00 USD | 77,570.00 USD | 120,850.00 USD |
| `1D` | `296.50` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 43,030.00 USD | 30,490.00 USD | 20,610.00 USD |
| `1D` | `296.90` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 22,010.00 USD | 21,080.00 USD | 78,160.00 USD |
| `7D` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 207,350.00 USD | 50,930.00 USD | 172,330.00 USD |
| `1D` | `297.30` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD |
| `7D` | `297.40` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD |
| `1D` | `297.70` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 1,810.00 USD | 902.60 USD | 12,060.00 USD |
| `7D` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 17,770.00 USD | 39,840.00 USD | 54,910.00 USD |
| `1D` | `298.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 51,550.00 USD | 10,450.00 USD | 41,570.00 USD |
| `7D` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 32,250.00 USD | 42,710.00 USD | 68,790.00 USD |
| `1D` | `298.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 11,480.00 USD | 7,730.00 USD | 56,420.00 USD |
| `1D` | `298.90` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 28,150.00 USD | 13,200.00 USD | 94,670.00 USD |
| `7D` | `298.90` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 70,090.00 USD | 12,780.00 USD | 39,970.00 USD |
| `1D` | `299.30` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 33,660.00 USD | 16,690.00 USD | 12,340.00 USD |
| `7D` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 4,470.00 USD | 13,080.00 USD | 45,920.00 USD |
| `1D` | `299.70` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 12,530.00 USD | 14,020.00 USD | 29,600.00 USD |
| `7D` | `299.90` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 56,210.00 USD | 10,220.00 USD | 19,850.00 USD |
| `1D` | `300.10` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 30,490.00 USD | 30,850.00 USD | 64,750.00 USD |
| `7D` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 34.10 USD |
| `1D` | `300.50` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 18,940.00 USD | 11,020.00 USD | 17,170.00 USD |
| `1D` | `300.90` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 8,640.00 USD | 32,430.00 USD | 26,660.00 USD |
| `7D` | `300.90` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 24,730.00 USD | 70,210.00 USD | 104,120.00 USD |
| `1D` | `301.30` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 2,520.00 USD | 43,910.00 USD | 19,410.00 USD |
| `7D` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 71,890.00 USD | 56,010.00 USD | 94,780.00 USD |
| `1D` | `301.70` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 19,800.00 USD | 11,800.00 USD | 16,650.00 USD |
| `7D` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 89,300.00 USD | 185,430.00 USD | 26,240.00 USD |
| `1D` | `302.10` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 30,130.00 USD | 37,350.00 USD | 10,340.00 USD |
| `7D` | `302.40` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 448.27 USD |
| `1D` | `302.50` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 10,520.00 USD | 20,540.00 USD | 38,380.00 USD |
| `1D` | `302.90` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 1,030.00 USD | 1,760.00 USD | 14,000.00 USD |
| `7D` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 71,700.00 USD | 110,480.00 USD | 41,910.00 USD |
| `1D` | `303.30` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 31,330.00 USD | 299.52 USD | 23,990.00 USD |
| `7D` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 66.92 USD |
| `1D` | `303.70` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 7,850.00 USD | 3,470.00 USD | 6,250.00 USD |
| `7D` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 21,140.00 USD | 11,010.00 USD | 45,820.00 USD |
| `1D` | `304.10` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 21,670.00 USD | 747.60 USD | 53,800.00 USD |
| `7D` | `304.40` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 3,670.00 USD | 11,280.00 USD | 35.31 USD |
| `1D` | `304.50` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 13,310.00 USD | 9,420.00 USD | 53,810.00 USD |
| `1D` | `304.90` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 697.80 USD | 146.63 USD | 2.91 USD |
| `7D` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 36,160.00 USD | 18,990.00 USD | 8,410.00 USD |
| `1D` | `305.30` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 10,950.00 USD | 102.77 USD | 2,010.00 USD |
| `7D` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 163,900.00 USD | 127,450.00 USD | 119,140.00 USD |
| `1D` | `305.70` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 7,960.00 USD | 4,710.00 USD | 3,410.00 USD |
| `7D` | `305.90` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 82,000.00 USD | 55,480.00 USD | 10,620.00 USD |
| `1D` | `306.10` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 4,210.00 USD | 2,780.00 USD | 1,350.00 USD |
| `7D` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 39,250.00 USD | 55,740.00 USD | 66,820.00 USD |
| `1D` | `306.50` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 4,410.00 USD | 9,500.00 USD | 5,670.00 USD |
| `1D` | `306.90` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 31,980.00 USD | 40,330.00 USD | 13,060.00 USD |
| `7D` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 84,850.00 USD | 64,520.00 USD | 102,660.00 USD |
| `1D` | `307.30` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 7,930.00 USD | 34,540.00 USD | 17,710.00 USD |
| `7D` | `307.40` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 46,230.00 USD | 154,680.00 USD | 83,700.00 USD |
| `1D` | `307.70` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 32,340.00 USD | 30,450.00 USD | 9,610.00 USD |
| `7D` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 136,380.00 USD | 101,120.00 USD | 65,240.00 USD |
| `1D` | `308.10` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 25,680.00 USD | 11,430.00 USD | 16,390.00 USD |
| `7D` | `308.40` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 152,590.00 USD | 50,070.00 USD | 124,880.00 USD |
| `1D` | `308.50` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 5,120.00 USD | 3,510.00 USD | 4,270.00 USD |
| `1D` | `308.90` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 12,360.00 USD | 5,850.00 USD | 4,140.00 USD |
| `7D` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 61,600.00 USD | 52,230.00 USD | 19,740.00 USD |
| `1D` | `309.30` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 9,910.00 USD | 12,160.00 USD | 2,320.00 USD |
| `7D` | `309.40` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 28,000.00 USD | 35,530.00 USD | 46,570.00 USD |
| `1D` | `309.70` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 15,160.00 USD | 13,820.00 USD | 9,210.00 USD |
| `7D` | `309.90` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 59,490.00 USD | 131,460.00 USD | 144,770.00 USD |
| `1D` | `310.10` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 4,390.00 USD | 6,620.00 USD | 10,940.00 USD |
| `7D` | `310.40` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 78,770.00 USD | 123,340.00 USD | 76,810.00 USD |
| `1D` | `310.50` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 144.00 USD | 4,760.00 USD | 3,930.00 USD |
| `1D` | `310.90` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.31 USD |
| `7D` | `310.90` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 35,670.00 USD | 35,930.00 USD | 3,870.00 USD |
| `1D` | `311.30` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `311.40` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 89,390.00 USD | 65,750.00 USD | 47,760.00 USD |
| `1D` | `311.70` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 9,900.00 USD | 6,590.00 USD | 4.14 USD |
| `7D` | `311.90` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 40,320.00 USD | 11,160.00 USD | 13,530.00 USD |
| `1D` | `312.10` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 244.00 USD | 39.75 USD | 1.60 USD |
| `7D` | `312.40` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 45,640.00 USD | 23,560.00 USD | 43,600.00 USD |
| `1D` | `312.50` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD |
| `1D` | `312.90` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD |
| `7D` | `312.90` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 47,880.00 USD |
| `1D` | `313.30` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.40` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 66,180.00 USD | 30,120.00 USD | 30,420.00 USD |
| `1D` | `313.70` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `313.90` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 44,540.00 USD | 15,370.00 USD | 35,920.00 USD |
| `1D` | `314.10` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.40` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,860.00 USD |
| `1D` | `314.50` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD |
| `1D` | `314.90` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `314.90` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 39,410.00 USD | 0.00 USD | 10,370.00 USD |
| `1D` | `315.30` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 2,050.00 USD | 1,550.00 USD | 1,620.00 USD |
| `7D` | `315.40` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 6,160.00 USD | 9,920.00 USD | 18,160.00 USD |
| `1D` | `315.70` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 3,110.00 USD | 3,040.00 USD | 5,230.00 USD |
| `7D` | `315.90` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 47,110.00 USD | 41,400.00 USD | 30,030.00 USD |
| `1D` | `316.10` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 2,100.00 USD | 3,070.00 USD | 5,590.00 USD |
| `7D` | `316.40` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 16,580.00 USD | 40,320.00 USD | 61,880.00 USD |
| `1D` | `316.50` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 20.15 USD | 3,300.00 USD | 0.00 USD |
| `1D` | `316.90` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 14,650.00 USD | 228.97 USD | 7,660.00 USD |
| `7D` | `316.90` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 234.48 USD |
| `1D` | `317.30` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 1,990.00 USD | 4,180.00 USD | 7,170.00 USD |
| `7D` | `317.40` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 14,540.00 USD | 1,010.00 USD | 10.69 USD |
| `1D` | `317.70` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 13,910.00 USD | 11,970.00 USD | 17,040.00 USD |
| `7D` | `317.90` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 21,640.00 USD | 8,200.00 USD | 5.83 USD |
| `1D` | `318.10` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 1,830.00 USD | 9,210.00 USD | 7,680.00 USD |
| `7D` | `318.40` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 3,320.00 USD | 27,530.00 USD | 22,390.00 USD |
| `1D` | `318.50` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 7,450.00 USD | 9,580.00 USD |
| `7D` | `318.90` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 11,180.00 USD | 17,970.00 USD | 37,820.00 USD |
| `7D` | `319.40` | 11,870,000.00 USD | 11,870,000.00 USD | 0.00 USD | 733.55 USD | 18,060.00 USD | 4.25 USD |
| `7D` | `319.90` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 446.22 USD | 22,230.00 USD | 5,410.00 USD |
| `7D` | `320.40` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD |
| `7D` | `320.90` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.40` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD |
| `7D` | `321.90` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD |
| `7D` | `322.40` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 22,930.00 USD | 7,950.00 USD | 6,150.00 USD |
| `7D` | `322.90` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 16,590.00 USD | 5,830.00 USD | 0.00 USD |
| `7D` | `323.40` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 14,160.00 USD | 11,950.00 USD | 11,510.00 USD |
| `7D` | `323.90` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 269.10 USD | 692.00 USD | 18.28 USD |
| `7D` | `324.40` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.90` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD |
| `7D` | `325.40` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `298.58M` | Total OI Tokens: `1,078,996.1 BCH`
  * 1h OI Change: `+0.98%` | 4h OI Change: `-5.46%` | 24h OI Change: `-7.70%`
  * Exchange Breakdown: Binance=`87.84M` | Bybit=`37.43M` | OKX=`23.34M` | Hyperliquid=`7.55M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.90K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `-0.0052%` |
| **USDT Bybit** | `0.0039%` | **USDT KuCoin** | `-0.0002%` |
| **USDT MEXC** | `0.0018%` | **USDT BingX** | `0.0095%` |
| **USDT Gate** | `0.0024%` | **USDT Bitget** | `0.0097%` |
| **CoinM Binance** | `-0.0010%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `50.74%` | `49.26%` | `1.03` | 34,330,000.00 USD |
| `15M` | `Binance` | `49.98%` | `50.02%` | `1.00` | 11,870,000.00 USD |
| `15M` | `OKX` | `44.31%` | `55.69%` | `0.80` | 4,620,000.00 USD |
| `15M` | `Bybit` | `59.39%` | `40.61%` | `1.46` | 6,110,000.00 USD |
| `15M` | `KuCoin` | `42.87%` | `57.13%` | `0.75` | 210,130.00 USD |
| `15M` | `Gate` | `33.09%` | `66.91%` | `0.49` | 609,130.00 USD |
| `15M` | `Bitget` | `38.79%` | `61.21%` | `0.63` | 1,600,000.00 USD |
| `15M` | `BingX` | `44.81%` | `55.19%` | `0.81` | 919,750.00 USD |
| `15M` | `MEXC` | `54.62%` | `45.38%` | `1.20` | 2,220,000.00 USD |
| `15M` | `Bitunix` | `48.65%` | `51.35%` | `0.95` | 1,170,000.00 USD |
| `15M` | `Hyperliquid` | `51.9%` | `48.1%` | `1.08` | 2,660,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.07%` | `49.93%` | `1.00` | 115,550.00 USD |
| `15M` | `Crypto.com` | `19.32%` | `80.68%` | `0.24` | 962.50 USD |
| `15M` | `WhiteBIT` | `70.59%` | `29.41%` | `2.40` | 944,430.00 USD |
| `15M` | `HTX` | `34.36%` | `65.64%` | `0.52` | 68,570.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `52.23%` | `47.77%` | `1.09` | 838,800.00 USD |
| `15M` | `Aster` | `19.09%` | `80.91%` | `0.24` | 50,530.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.53%` | `60.47%` | `0.65` | 311,100.00 USD |
| `15M` | `Whale Positions` | `49.98%` | `50.02%` | `1.00` | 11,870,000.00 USD |
| `15M` | `Global Accounts` | `50.74%` | `49.26%` | `1.03` | 34,330,000.00 USD |
| `1H` | `BCH` | `50.29%` | `49.71%` | `1.01` | 45,100,000.00 USD |
| `1H` | `Binance` | `44.77%` | `55.23%` | `0.81` | 16,210,000.00 USD |
| `1H` | `OKX` | `53.41%` | `46.59%` | `1.15` | 5,010,000.00 USD |
| `1H` | `Bybit` | `50.74%` | `49.26%` | `1.03` | 4,950,000.00 USD |
| `1H` | `KuCoin` | `52.69%` | `47.31%` | `1.11` | 898,100.00 USD |
| `1H` | `Gate` | `58.01%` | `41.99%` | `1.38` | 5,070,000.00 USD |
| `1H` | `Bitget` | `49.16%` | `50.84%` | `0.97` | 2,770,000.00 USD |
| `1H` | `BingX` | `53.5%` | `46.5%` | `1.15` | 1,100,000.00 USD |
| `1H` | `MEXC` | `52.01%` | `47.99%` | `1.08` | 2,330,000.00 USD |
| `1H` | `Bitunix` | `46.92%` | `53.08%` | `0.88` | 1,170,000.00 USD |
| `1H` | `Hyperliquid` | `64.75%` | `35.25%` | `1.84` | 852,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.37%` | `49.63%` | `1.01` | 3,730,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `74.89%` | `25.11%` | `2.98` | 670,570.00 USD |
| `1H` | `HTX` | `66.45%` | `33.55%` | `1.98` | 50,510.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.48%` | `50.52%` | `0.98` | 277,050.00 USD |
| `1H` | `Aster` | `53.38%` | `46.62%` | `1.15` | 36,720.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `44.77%` | `55.23%` | `0.81` | 16,210,000.00 USD |
| `1H` | `Global Accounts` | `50.29%` | `49.71%` | `1.01` | 45,100,000.00 USD |
| `4H` | `BCH` | `48.46%` | `51.54%` | `0.94` | 654,660,000.00 USD |
| `4H` | `Binance` | `47.99%` | `52.01%` | `0.92` | 263,610,000.00 USD |
| `4H` | `OKX` | `49.32%` | `50.68%` | `0.97` | 79,910,000.00 USD |
| `4H` | `Bybit` | `51.85%` | `48.15%` | `1.08` | 84,680,000.00 USD |
| `4H` | `KuCoin` | `49.61%` | `50.39%` | `0.98` | 5,080,000.00 USD |
| `4H` | `Gate` | `48.43%` | `51.57%` | `0.94` | 9,540,000.00 USD |
| `4H` | `Bitget` | `46.24%` | `53.76%` | `0.86` | 26,470,000.00 USD |
| `4H` | `BingX` | `43.19%` | `56.81%` | `0.76` | 31,680,000.00 USD |
| `4H` | `MEXC` | `48.36%` | `51.64%` | `0.94` | 34,820,000.00 USD |
| `4H` | `Bitunix` | `49.69%` | `50.31%` | `0.99` | 17,510,000.00 USD |
| `4H` | `Hyperliquid` | `45.24%` | `54.76%` | `0.83` | 61,810,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.29%` | `50.71%` | `0.97` | 4,280,000.00 USD |
| `4H` | `Crypto.com` | `52.05%` | `47.95%` | `1.09` | 45,530.00 USD |
| `4H` | `WhiteBIT` | `61.6%` | `38.4%` | `1.60` | 12,730,000.00 USD |
| `4H` | `HTX` | `48.9%` | `51.1%` | `0.96` | 1,010,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.54%` | `52.46%` | `0.91` | 14,770,000.00 USD |
| `4H` | `Aster` | `55.44%` | `44.56%` | `1.24` | 2,090,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.75%` | `52.25%` | `0.91` | 4,620,000.00 USD |
| `4H` | `Whale Positions` | `47.99%` | `52.01%` | `0.92` | 263,610,000.00 USD |
| `4H` | `Global Accounts` | `48.46%` | `51.54%` | `0.94` | 654,660,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `289.00` | `288.21` | `289.00` | `289.02` | `287.22` | 505,722.48 USD | 323,366.92 USD | 182,355.56 USD | 141,011.36 USD | `+27.88%` | `60B / 31S` |
| `0:00 UTC` | `288.00` | `287.86` | `288.00` | `288.89` | `287.26` | 500,104.64 USD | 252,267.65 USD | 247,836.98 USD | 4,430.67 USD | `+0.89%` | `39B / 37S` |
| `5:00 UTC` | `287.00` | `286.98` | `287.00` | `287.64` | `286.45` | 492,053.69 USD | 262,098.60 USD | 229,955.08 USD | 32,143.52 USD | `+6.53%` | `24B / 25S` |
| `0:00 UTC` | `282.00` | `283.04` | `282.00` | `286.92` | `280.48` | 5,571,232.46 USD | 2,485,967.17 USD | 3,085,265.29 USD | -599,298.12 USD | `-10.76%` | `4B / 29S` |
| `5:00 UTC` | `282.43` | `282.21` | `282.43` | `283.00` | `281.49` | 1,589,754.90 USD | 936,266.72 USD | 653,488.17 USD | 282,778.55 USD | `+17.79%` | `31B / 14S` |
| `0:00 UTC` | `275.52` | `277.16` | `275.52` | `282.40` | `273.60` | 7,176,408.30 USD | 3,429,549.36 USD | 3,746,858.94 USD | -317,309.59 USD | `-4.42%` | `7B / 13S` |
| `5:00 UTC` | `273.26` | `272.72` | `273.26` | `275.70` | `269.30` | 7,511,252.05 USD | 3,875,803.21 USD | 3,635,448.84 USD | 240,354.37 USD | `+3.20%` | `12B / 10S` |
| `0:00 UTC` | `273.80` | `272.56` | `273.80` | `274.68` | `269.76` | 3,951,157.31 USD | 2,047,269.47 USD | 1,903,887.84 USD | 143,381.63 USD | `+3.63%` | `9B / 4S` |
| `5:00 UTC` | `276.40` | `276.70` | `276.40` | `278.76` | `273.60` | 2,981,088.00 USD | 1,514,309.73 USD | 1,466,778.26 USD | 47,531.47 USD | `+1.59%` | `19B / 11S` |
| `0:00 UTC` | `279.51` | `278.96` | `279.51` | `280.01` | `277.65` | 1,651,633.47 USD | 593,491.69 USD | 1,058,141.78 USD | -464,650.08 USD | `-28.13%` | `11B / 24S` |

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
| `5m` | -85,610.00 USD | -134,190.00 USD | **`DISTRIBUTION`** |
| `15m` | 14,200.00 USD | -464,010.00 USD | **`DISTRIBUTION`** |
| `30m` | 14,550.00 USD | -207,350.00 USD | **`DISTRIBUTION`** |
| `1h` | -194,270.00 USD | -78,160.00 USD | **`DISTRIBUTION`** |
| `2h` | -736,860.00 USD | -1,510,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -891,120.00 USD | -641,430.00 USD | **`DISTRIBUTION`** |
| `6h` | -920,650.00 USD | -3,140,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -637,320.00 USD | -1,760,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -694,410.00 USD | -1,490,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,660,000.00 USD | -9,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -802,160.00 USD | -13,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,310,000.00 USD | -139,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-85.61K` | 15m=`+14.20K` | 1h=`-194.27K` | 24h=`-1.66M`
* Futures Capital Netflows: 5m=`-134.19K` | 15m=`-464.01K` | 1h=`-78.16K` | 24h=`-9.48M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `273.27` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `268.68` (Risk Distance: `4.59` pts)
  * +2.5R Take Profit: `284.75`
  * Mathematical Lot Sizing: **`2.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.58` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `283.17` (Risk Distance: `4.59` pts)
  * +2.5R Take Profit: `267.10`
  * Mathematical Lot Sizing: **`2.17 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`279.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
