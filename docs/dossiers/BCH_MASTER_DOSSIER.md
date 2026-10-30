# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 10:52:59 IST` (`2026-10-30 05:22:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `283.46` | **Live Ask Quote**: `284.04` | **Mid Price**: `283.75`
- **Spread Points**: `580.00` | **Spread BPS**: `20.44 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `274.46` | VWAP Z-Score: `+1.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.97` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `61.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `292.46` | Lower -3.00σ Band: `256.47`
  * Upper +2.51σ Band: `289.52` | Lower -2.51σ Band: `259.41`
  * Upper +2.01σ Band: `286.52` | Lower -2.01σ Band: `262.40`
  * Upper +2.00σ Band: `286.46` | Lower -2.00σ Band: `262.46`
  * Upper +1.28σ Band: `282.14` | Lower -1.28σ Band: `266.78`
  * Upper +1.00σ Band: `280.46` | Lower -1.00σ Band: `268.46`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`281.69` | EMA-20=`279.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`278.81` (Slope: `+0.0000`) | EMA-100=`280.38`
  * Institutional Anchors: EMA-144=`281.45` | EMA-200=`282.93` (Slope: `-0.0933`) | EMA-233=`284.03`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.75` (Distance: `+1.83%`)
  * Point of Control (POC) = `276.23` (Distance: `+2.76%`)
  * Value Area Low (VAL) = `268.96` (Distance: `+5.54%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.76` | Low=`282.66`
  * New York Session (13:00-21:00 UTC): High=`285.45` | Low=`282.05`
  * Initial Balance (First Hour): IB High=`284.76` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `282.62` - `284.88`
  * Optimal Trade Entry (OTE 0.705): `284.32`
  * Structural Invalidation Anchor (0.786): `286.02`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.52` | `285.59` | `283.92` | `283.92` | `1,002` | 285,551.06 USD | 81,255.77 USD | `+28.46%` | -2,226,425.70 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `283.93` | `284.39` | `283.91` | `284.39` | `638` | 181,209.70 USD | 33,521.26 USD | `+18.50%` | -2,192,904.43 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `284.40` | `284.58` | `283.93` | `284.24` | `204` | 57,994.86 USD | 6,645.09 USD | `+11.46%` | -2,186,259.35 USD | `+0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `284.59` | `284.96` | `283.35` | `283.51` | `4,651` | 1,321,321.21 USD | -29,957.81 USD | `-2.27%` | -2,452,463.50 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `283.51` | `285.59` | `283.46` | `283.92` | `3,278` | 932,067.73 USD | 167,554.77 USD | `+17.98%` | -2,284,908.73 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `283.93` | `284.58` | `283.91` | `284.24` | `842` | 239,204.56 USD | 40,166.35 USD | `+16.79%` | -2,244,742.38 USD | `-0.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `276.08` | `284.75` | `276.00` | `283.99` | `21,838` | 6,138,674.85 USD | -75,926.04 USD | `-1.24%` | -2,486,653.51 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `283.99` | `287.12` | `282.33` | `283.51` | `23,256` | 6,620,902.65 USD | -28,395.05 USD | `-0.43%` | -2,515,048.57 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `283.51` | `285.59` | `283.46` | `284.26` | `4,118` | 1,170,847.90 USD | 207,999.40 USD | `+17.76%` | -2,307,049.17 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.24` | `27,376` | 7,792,174.93 USD | 179,326.07 USD | `+2.30%` | -1,695,056.93 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | 1,085,885.17 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -386,016.76 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.24` | `27,376` | 7,792,174.93 USD | 179,326.07 USD | `+2.30%` | -1,695,056.93 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`283.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1966` | `0x12d2...f97f` | `LONG` | 1,030,282.10 USD | `3,627,243,000,000.00` | `303.26` | `283.87` | `0.000000` | -69,717.24 USD | `-6.77%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `282.54` | 6,657.21 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.66K USD at 282.5400 USD [API] | `2026-10-29 02:19:03` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+1.80%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.45%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `66.50` | 2,730.00 USD | 201,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 277.83 USD | 198,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 541.71 USD | 198,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 1,110.00 USD | 198,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 146.70 USD | 196,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 196,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 195,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 189,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 185,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 185,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 3,190.00 USD | 185,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 125.50 USD | 181,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 181,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `133.50` | 2,000.00 USD | 181,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 179,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 178,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 177,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 174,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 174,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 8,280.00 USD | 174,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 165,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 165,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 165,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 164,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 164,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 2,310.00 USD | 163,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 161,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 160,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 160,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 159,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 158,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `193.50` | 1,050.00 USD | 157,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 156,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 2,290.00 USD | 155,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 153,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 153,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 152,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 152,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 42,410.00 USD | 152,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 109,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `211.50` | 6,660.00 USD | 109,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 103,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 2,610.00 USD | 99,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 96,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 5,340.00 USD | 63,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 58,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 57,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 1,320.00 USD | 57,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,300.00 USD | 55,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 54,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 632.17 USD | 54,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `234.70` | 10,050,000.00 USD | 10,050,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.20` | 10,040,000.00 USD | 10,040,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.70` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.20` | 10,030,000.00 USD | 10,030,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.70` | 10,010,000.00 USD | 10,010,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.20` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 30,780.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.70` | 9,970,000.00 USD | 9,970,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.20` | 9,970,000.00 USD | 9,970,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.70` | 9,950,000.00 USD | 9,950,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.20` | 9,920,000.00 USD | 9,920,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.70` | 9,900,000.00 USD | 9,900,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.70` | 9,900,000.00 USD | 9,900,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.20` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.70` | 9,890,000.00 USD | 9,890,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.20` | 9,880,000.00 USD | 9,880,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 21,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.70` | 9,810,000.00 USD | 9,810,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.20` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 19,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.70` | 9,770,000.00 USD | 9,770,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.20` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 18,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.70` | 9,710,000.00 USD | 9,710,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.20` | 9,710,000.00 USD | 9,710,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.70` | 9,670,000.00 USD | 9,670,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.20` | 9,650,000.00 USD | 9,650,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.70` | 9,610,000.00 USD | 9,610,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 9,600,000.00 USD | 9,600,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 12,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.70` | 9,560,000.00 USD | 9,560,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.20` | 9,550,000.00 USD | 9,550,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 12,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.70` | 9,540,000.00 USD | 9,540,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 9,440,000.00 USD | 9,440,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 12,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.70` | 9,370,000.00 USD | 9,370,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.20` | 4,630,000.00 USD | 4,630,000.00 USD | 19,400.00 USD | 7,530.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.20` | 9,260,000.00 USD | 9,260,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 10,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.60` | 4,600,000.00 USD | 4,600,000.00 USD | 8,330.00 USD | 2,460.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.70` | 9,150,000.00 USD | 9,150,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.00` | 4,580,000.00 USD | 4,580,000.00 USD | 28,550.00 USD | 38,930.00 USD | 11,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 9,010,000.00 USD | 9,010,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.40` | 4,500,000.00 USD | 4,500,000.00 USD | 11,230.00 USD | 36,660.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 9,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 8,890,000.00 USD | 8,890,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.80` | 4,420,000.00 USD | 4,420,000.00 USD | 34,810.00 USD | 54,770.00 USD | 11,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.20` | 4,320,000.00 USD | 4,320,000.00 USD | 25,960.00 USD | 8,130.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.20` | 8,710,000.00 USD | 8,710,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,170.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.60` | 4,270,000.00 USD | 4,270,000.00 USD | 12,330.00 USD | 1,550.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.70` | 8,580,000.00 USD | 8,580,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.00` | 4,260,000.00 USD | 4,260,000.00 USD | 8,050.00 USD | 11,430.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 8,480,000.00 USD | 8,480,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.40` | 4,230,000.00 USD | 4,230,000.00 USD | 15,470.00 USD | 16,560.00 USD | 15,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 8,410,000.00 USD | 8,410,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.80` | 4,180,000.00 USD | 4,180,000.00 USD | 6,930.00 USD | 7,470.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.20` | 4,160,000.00 USD | 4,160,000.00 USD | 1,590.00 USD | 3,710.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.20` | 8,300,000.00 USD | 8,300,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.60` | 4,150,000.00 USD | 4,150,000.00 USD | 9,130.00 USD | 11,220.00 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.70` | 8,190,000.00 USD | 8,190,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.00` | 4,130,000.00 USD | 4,130,000.00 USD | 14,600.00 USD | 8,110.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 8,020,000.00 USD | 8,020,000.00 USD | 32,100.00 USD | 13,440.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.40` | 4,100,000.00 USD | 4,100,000.00 USD | 2,600.00 USD | 16,230.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 7,940,000.00 USD | 7,940,000.00 USD | 33,430.00 USD | 16,550.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.80` | 4,060,000.00 USD | 4,060,000.00 USD | 19,840.00 USD | 11,010.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.20` | 4,020,000.00 USD | 4,020,000.00 USD | 884.48 USD | 30,930.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.20` | 7,850,000.00 USD | 7,850,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 4,490.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.60` | 3,970,000.00 USD | 3,970,000.00 USD | 7,420.00 USD | 4,010.00 USD | 4.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.70` | 7,710,000.00 USD | 7,710,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.00` | 3,960,000.00 USD | 3,960,000.00 USD | 9,580.00 USD | 1,470.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 7,600,000.00 USD | 7,600,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.40` | 3,940,000.00 USD | 3,940,000.00 USD | 6,290.00 USD | 4,650.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 467.62 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.70` | 7,560,000.00 USD | 7,560,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.80` | 3,920,000.00 USD | 3,920,000.00 USD | 1,500.00 USD | 2,430.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.20` | 3,910,000.00 USD | 3,910,000.00 USD | 21,220.00 USD | 15,910.00 USD | 56,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.20` | 7,490,000.00 USD | 7,490,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.60` | 3,820,000.00 USD | 3,820,000.00 USD | 25,120.00 USD | 8,910.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.70` | 7,290,000.00 USD | 7,290,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.00` | 3,750,000.00 USD | 3,750,000.00 USD | 12,700.00 USD | 34,640.00 USD | 7.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 7,130,000.00 USD | 7,130,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.40` | 3,700,000.00 USD | 3,700,000.00 USD | 14,770.00 USD | 3,600.00 USD | 17,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 7,040,000.00 USD | 7,040,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.80` | 3,660,000.00 USD | 3,660,000.00 USD | 41,920.00 USD | 32,160.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.20` | 3,550,000.00 USD | 3,550,000.00 USD | 4,720.00 USD | 8,150.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.20` | 6,880,000.00 USD | 6,880,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.60` | 3,530,000.00 USD | 3,530,000.00 USD | 20,220.00 USD | 6,120.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.70` | 6,660,000.00 USD | 6,660,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.00` | 3,480,000.00 USD | 3,480,000.00 USD | 8,310.00 USD | 48,880.00 USD | 44,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 6,540,000.00 USD | 6,540,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.40` | 3,370,000.00 USD | 3,370,000.00 USD | 7,780.00 USD | 43,600.00 USD | 2,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 6,410,000.00 USD | 6,410,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.80` | 3,320,000.00 USD | 3,320,000.00 USD | 15,410.00 USD | 47,140.00 USD | 62,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.20` | 3,200,000.00 USD | 3,200,000.00 USD | 34,470.00 USD | 27,340.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.20` | 6,240,000.00 USD | 6,240,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.60` | 3,110,000.00 USD | 3,110,000.00 USD | 366.04 USD | 539.35 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.70` | 6,050,000.00 USD | 6,050,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.00` | 3,100,000.00 USD | 3,100,000.00 USD | 8,670.00 USD | 12,480.00 USD | 6,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 5,870,000.00 USD | 5,870,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.40` | 3,070,000.00 USD | 3,070,000.00 USD | 30,700.00 USD | 4,190.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 5,810,000.00 USD | 5,810,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.80` | 2,960,000.00 USD | 2,960,000.00 USD | 32,740.00 USD | 29,870.00 USD | 28,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.20` | 2,870,000.00 USD | 2,870,000.00 USD | 25,990.00 USD | 15,290.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.20` | 5,410,000.00 USD | 5,410,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.60` | 2,810,000.00 USD | 2,810,000.00 USD | 1,370.00 USD | 19,610.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.70` | 5,240,000.00 USD | 5,240,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.00` | 2,770,000.00 USD | 2,770,000.00 USD | 32,870.00 USD | 1,190.00 USD | 33,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 5,180,000.00 USD | 5,180,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.40` | 2,700,000.00 USD | 2,700,000.00 USD | 64,290.00 USD | 1,260.00 USD | 3.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.70` | 5,040,000.00 USD | 5,040,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.80` | 2,640,000.00 USD | 2,640,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.20` | 2,630,000.00 USD | 2,630,000.00 USD | 3,880.00 USD | 13,250.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.20` | 4,840,000.00 USD | 4,840,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.60` | 2,600,000.00 USD | 2,600,000.00 USD | 28,430.00 USD | 8,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 4,650,000.00 USD | 4,650,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.00` | 2,570,000.00 USD | 2,570,000.00 USD | 47,770.00 USD | 22,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 4,450,000.00 USD | 4,450,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.40` | 2,500,000.00 USD | 2,500,000.00 USD | 7,660.00 USD | 68,160.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.70` | 4,270,000.00 USD | 4,270,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.80` | 2,400,000.00 USD | 2,400,000.00 USD | 4,660.00 USD | 36,050.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.20` | 2,350,000.00 USD | 2,350,000.00 USD | 4,570.00 USD | 35,070.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.20` | 3,940,000.00 USD | 3,940,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.70` | 3,610,000.00 USD | 3,610,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.00` | 2,250,000.00 USD | 2,250,000.00 USD | 8,580.00 USD | 321.80 USD | 20.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 3,550,000.00 USD | 3,550,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.40` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 16,500.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.70` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.80` | 2,210,000.00 USD | 2,210,000.00 USD | 378.60 USD | 618.10 USD | 3,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.20` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.20` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.60` | 2,210,000.00 USD | 2,210,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.70` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.00` | 2,200,000.00 USD | 2,200,000.00 USD | 323.80 USD | 7,970.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.40` | 2,180,000.00 USD | 2,180,000.00 USD | 12,710.00 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.70` | 3,520,000.00 USD | 3,520,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.80` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 25,790.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.20` | 2,130,000.00 USD | 2,130,000.00 USD | 15,100.00 USD | 15,900.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.20` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.60` | 2,090,000.00 USD | 2,090,000.00 USD | 27,370.00 USD | 16,330.00 USD | 53,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 3,390,000.00 USD | 3,390,000.00 USD | 25,660.00 USD | 17,630.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.00` | 1,990,000.00 USD | 1,990,000.00 USD | 33,780.00 USD | 21,290.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.40` | 1,910,000.00 USD | 1,910,000.00 USD | 9,330.00 USD | 82,780.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 3,000,000.00 USD | 3,000,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.80` | 1,810,000.00 USD | 1,810,000.00 USD | 37,900.00 USD | 70,140.00 USD | 49,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.20` | 1,650,000.00 USD | 1,650,000.00 USD | 224,890.00 USD | 0.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.20` | 2,870,000.00 USD | 2,870,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.60` | 1,410,000.00 USD | 1,410,000.00 USD | 215,540.00 USD | 19,960.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.70` | 2,370,000.00 USD | 2,370,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.00` | 1,130,000.00 USD | 1,130,000.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 1,740,000.00 USD | 1,740,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.40` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 1,580,000.00 USD | 1,580,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.80` | 1,090,000.00 USD | 1,090,000.00 USD | 20,900.00 USD | 10,450.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.20` | 1,010,000.00 USD | 1,010,000.00 USD | 89,570.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.20` | 1,500,000.00 USD | 1,500,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.60` | 921,220.00 USD | 921,220.00 USD | 11,880.00 USD | 9,200.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.70` | 1,320,000.00 USD | 1,320,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.00` | 894,550.00 USD | 894,550.00 USD | 25,410.00 USD | 4,330.00 USD | 16,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 1,220,000.00 USD | 1,220,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.40` | 848,700.00 USD | 848,700.00 USD | 301.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 1,060,000.00 USD | 1,060,000.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.80` | 848,400.00 USD | 848,400.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.20` | 828,100.00 USD | 828,100.00 USD | 12,120.00 USD | 65,540.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.20` | 669,540.00 USD | 669,540.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.60` | 694,220.00 USD | 694,220.00 USD | 79,560.00 USD | 55,720.00 USD | 61,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 512,260.00 USD | 512,260.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.00` | 497,130.00 USD | 497,130.00 USD | 1,710.00 USD | 53,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 460,020.00 USD | 460,020.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 457,350.00 USD | 457,350.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.80` | 442,310.00 USD | 442,310.00 USD | 14,720.00 USD | 14,930.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.20` | 381,310.00 USD | 381,310.00 USD | 14,910.00 USD | 26,680.00 USD | 50,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.20` | 455,590.00 USD | 455,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.60` | 289,110.00 USD | 289,110.00 USD | 28,040.00 USD | 49,180.00 USD | 46,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.70` | 438,230.00 USD | 438,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.00` | 165,460.00 USD | 165,460.00 USD | 10,450.00 USD | 8,090.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 422,680.00 USD | 422,680.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.40` | 146,910.00 USD | 146,910.00 USD | 2,280.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 325,280.00 USD | 325,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.80` | 137,680.00 USD | 137,680.00 USD | 0.00 USD | 12,900.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.20` | 120,630.00 USD | 120,630.00 USD | 10,310.00 USD | 8,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.20` | 127,860.00 USD | 127,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.60` | 101,830.00 USD | 101,830.00 USD | 0.00 USD | 34,420.00 USD | 19.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.00` | 67,380.00 USD | 67,380.00 USD | 14,930.00 USD | 36,060.00 USD | 26.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 103,640.00 USD | 103,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.40` | 16,370.00 USD | 16,370.00 USD | 1,280.00 USD | 15,060.00 USD | 21.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 2,000.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.20` | 3,800.00 USD | 3,800.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.20` | 74,590.00 USD | 74,590.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.60` | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.70` | 431,170.00 USD | 431,170.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.00` | 55,810.00 USD | 55,810.00 USD | 29,420.00 USD | 21,230.00 USD | 9.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.20` | 843,250.00 USD | 843,250.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.40` | 361,600.00 USD | 361,600.00 USD | 99,300.00 USD | 125,760.00 USD | 80,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.70` | 1,030,000.00 USD | 1,030,000.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.80` | 446,640.00 USD | 446,640.00 USD | 59,140.00 USD | 7,790.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.20` | 465,230.00 USD | 465,230.00 USD | 13,210.00 USD | 284.90 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.20` | 1,110,000.00 USD | 1,110,000.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.60` | 499,590.00 USD | 499,590.00 USD | 2,290.00 USD | 1,930.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.70` | 1,290,000.00 USD | 1,290,000.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.00` | 657,480.00 USD | 657,480.00 USD | 32,920.00 USD | 37,170.00 USD | 87,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 1,560,000.00 USD | 1,560,000.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.40` | 732,720.00 USD | 732,720.00 USD | 24,060.00 USD | 22,520.00 USD | 28,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `287.70` | 1,780,000.00 USD | 1,780,000.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.80` | 817,630.00 USD | 817,630.00 USD | 13,160.00 USD | 13,520.00 USD | 58,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.20` | 921,110.00 USD | 921,110.00 USD | 69,440.00 USD | 19,850.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.20` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.60` | 966,890.00 USD | 966,890.00 USD | 6,190.00 USD | 19,100.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.70` | 2,130,000.00 USD | 2,130,000.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.00` | 1,010,000.00 USD | 1,010,000.00 USD | 16,170.00 USD | 16,460.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 2,190,000.00 USD | 2,190,000.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.40` | 1,150,000.00 USD | 1,150,000.00 USD | 21,350.00 USD | 29,380.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 99,990.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.80` | 1,280,000.00 USD | 1,280,000.00 USD | 48,610.00 USD | 43,130.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.20` | 1,390,000.00 USD | 1,390,000.00 USD | 38,050.00 USD | 29,720.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.20` | 2,510,000.00 USD | 2,510,000.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.60` | 1,520,000.00 USD | 1,520,000.00 USD | 4,230.00 USD | 82,920.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.70` | 2,510,000.00 USD | 2,510,000.00 USD | 898.13 USD | 861.99 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.00` | 1,570,000.00 USD | 1,570,000.00 USD | 34,600.00 USD | 7,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 2,540,000.00 USD | 2,540,000.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.40` | 1,600,000.00 USD | 1,600,000.00 USD | 10,310.00 USD | 22,770.00 USD | 19.25 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `291.70` | 2,680,000.00 USD | 2,680,000.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.80` | 1,650,000.00 USD | 1,650,000.00 USD | 684.64 USD | 29,680.00 USD | 22,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.20` | 1,710,000.00 USD | 1,710,000.00 USD | 11,300.00 USD | 35,410.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.20` | 2,810,000.00 USD | 2,810,000.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.60` | 1,750,000.00 USD | 1,750,000.00 USD | 22,800.00 USD | 15,930.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 2,910,000.00 USD | 2,910,000.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.00` | 1,810,000.00 USD | 1,810,000.00 USD | 21,400.00 USD | 25,600.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 3,060,000.00 USD | 3,060,000.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.40` | 1,870,000.00 USD | 1,870,000.00 USD | 10,870.00 USD | 25,220.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 3,100,000.00 USD | 3,100,000.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.80` | 2,050,000.00 USD | 2,050,000.00 USD | 91,520.00 USD | 33,690.00 USD | 50,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.20` | 2,120,000.00 USD | 2,120,000.00 USD | 6,580.00 USD | 22,130.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.20` | 3,430,000.00 USD | 3,430,000.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.60` | 2,380,000.00 USD | 2,380,000.00 USD | 101,910.00 USD | 69,320.00 USD | 85,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 3,690,000.00 USD | 3,690,000.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.00` | 2,480,000.00 USD | 2,480,000.00 USD | 12,710.00 USD | 10,340.00 USD | 72,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 4,040,000.00 USD | 4,040,000.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.40` | 2,620,000.00 USD | 2,620,000.00 USD | 43,160.00 USD | 39,530.00 USD | 59,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 4,570,000.00 USD | 4,570,000.00 USD | 176,660.00 USD | 91,790.00 USD | 264,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.80` | 2,820,000.00 USD | 2,820,000.00 USD | 66,570.00 USD | 22,770.00 USD | 112,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.20` | 3,020,000.00 USD | 3,020,000.00 USD | 65,430.00 USD | 99,010.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.20` | 4,870,000.00 USD | 4,870,000.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `296.60` | 3,070,000.00 USD | 3,070,000.00 USD | 30,750.00 USD | 211.38 USD | 20,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.70` | 5,240,000.00 USD | 5,240,000.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.00` | 3,170,000.00 USD | 3,170,000.00 USD | 1,080.00 USD | 21,880.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,410,000.00 USD | 5,410,000.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.40` | 3,270,000.00 USD | 3,270,000.00 USD | 61,300.00 USD | 9,700.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 5,510,000.00 USD | 5,510,000.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.80` | 3,300,000.00 USD | 3,300,000.00 USD | 16,070.00 USD | 4,170.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.20` | 3,450,000.00 USD | 3,450,000.00 USD | 55,370.00 USD | 5,280.00 USD | 84,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.20` | 5,760,000.00 USD | 5,760,000.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `298.50` | 442.08 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `298.60` | 3,530,000.00 USD | 3,530,000.00 USD | 18,490.00 USD | 920.82 USD | 61,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.70` | 5,870,000.00 USD | 5,870,000.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.00` | 3,600,000.00 USD | 3,600,000.00 USD | 13,520.00 USD | 5,530.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 5,980,000.00 USD | 5,980,000.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.40` | 3,680,000.00 USD | 3,680,000.00 USD | 35,710.00 USD | 15,230.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 6,020,000.00 USD | 6,020,000.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.80` | 3,720,000.00 USD | 3,720,000.00 USD | 3,330.00 USD | 6,420.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.20` | 3,830,000.00 USD | 3,830,000.00 USD | 32,520.00 USD | 36,610.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.20` | 6,080,000.00 USD | 6,080,000.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 14,550.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `300.60` | 3,860,000.00 USD | 3,860,000.00 USD | 10,120.00 USD | 940.65 USD | 17,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.70` | 6,200,000.00 USD | 6,200,000.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.00` | 3,890,000.00 USD | 3,890,000.00 USD | 521.60 USD | 6,330.00 USD | 29,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 6,410,000.00 USD | 6,410,000.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.40` | 3,940,000.00 USD | 3,940,000.00 USD | 582.35 USD | 9,670.00 USD | 36,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.70` | 6,680,000.00 USD | 6,680,000.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.80` | 4,000,000.00 USD | 4,000,000.00 USD | 19,640.00 USD | 31,100.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.20` | 4,040,000.00 USD | 4,040,000.00 USD | 25,460.00 USD | 8,900.00 USD | 20.89 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.20` | 6,910,000.00 USD | 6,910,000.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.60` | 4,100,000.00 USD | 4,100,000.00 USD | 14,410.00 USD | 11,620.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 7,120,000.00 USD | 7,120,000.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.00` | 4,140,000.00 USD | 4,140,000.00 USD | 20,600.00 USD | 1,490.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.40` | 4,150,000.00 USD | 4,150,000.00 USD | 336.16 USD | 2,630.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 7,210,000.00 USD | 7,210,000.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 315.07 USD | 1.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.20` | 4,220,000.00 USD | 4,220,000.00 USD | 21,920.00 USD | 3,360.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.20` | 7,250,000.00 USD | 7,250,000.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.60` | 4,270,000.00 USD | 4,270,000.00 USD | 9,710.00 USD | 1,990.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 7,260,000.00 USD | 7,260,000.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.00` | 4,290,000.00 USD | 4,290,000.00 USD | 9,740.00 USD | 7,030.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 7,630,000.00 USD | 7,630,000.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.40` | 4,300,000.00 USD | 4,300,000.00 USD | 4,950.00 USD | 1,710.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 7,840,000.00 USD | 7,840,000.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.80` | 4,320,000.00 USD | 4,320,000.00 USD | 11,730.00 USD | 5,750.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.20` | 4,340,000.00 USD | 4,340,000.00 USD | 6,970.00 USD | 321.71 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.20` | 8,010,000.00 USD | 8,010,000.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.60` | 4,360,000.00 USD | 4,360,000.00 USD | 4,420.00 USD | 13,560.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 8,170,000.00 USD | 8,170,000.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.00` | 4,440,000.00 USD | 4,440,000.00 USD | 31,700.00 USD | 33,620.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 8,480,000.00 USD | 8,480,000.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.40` | 4,510,000.00 USD | 4,510,000.00 USD | 4,260.00 USD | 45,320.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 8,750,000.00 USD | 8,750,000.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.80` | 4,600,000.00 USD | 4,600,000.00 USD | 34,800.00 USD | 37,350.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.20` | 4,640,000.00 USD | 4,640,000.00 USD | 24,360.00 USD | 7,380.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.20` | 9,180,000.00 USD | 9,180,000.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.60` | 4,650,000.00 USD | 4,650,000.00 USD | 5,200.00 USD | 185.69 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 9,310,000.00 USD | 9,310,000.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.00` | 4,670,000.00 USD | 4,670,000.00 USD | 8,460.00 USD | 6,010.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 9,450,000.00 USD | 9,450,000.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.40` | 4,680,000.00 USD | 4,680,000.00 USD | 6,810.00 USD | 4,770.00 USD | 796.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 9,790,000.00 USD | 9,790,000.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.80` | 4,700,000.00 USD | 4,700,000.00 USD | 10,880.00 USD | 5,410.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.20` | 4,720,000.00 USD | 4,720,000.00 USD | 1,670.00 USD | 6,500.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.20` | 9,950,000.00 USD | 9,950,000.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.60` | 4,730,000.00 USD | 4,730,000.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.70` | 10,180,000.00 USD | 10,180,000.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.00` | 4,730,000.00 USD | 4,730,000.00 USD | 5,080.00 USD | 0.00 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,380,000.00 USD | 10,380,000.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.40` | 4,730,000.00 USD | 4,730,000.00 USD | 901.19 USD | 160.90 USD | 6.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 10,480,000.00 USD | 10,480,000.00 USD | 65,050.00 USD | 11,430.00 USD | 25,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.80` | 4,750,000.00 USD | 4,750,000.00 USD | 6,450.00 USD | 6,700.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.20` | 4,770,000.00 USD | 4,770,000.00 USD | 244.00 USD | 4,260.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.20` | 10,560,000.00 USD | 10,560,000.00 USD | 43,780.00 USD | 11,410.00 USD | 24,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.60` | 4,800,000.00 USD | 4,800,000.00 USD | 19,840.00 USD | 5,440.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 10,620,000.00 USD | 10,620,000.00 USD | 8,290.00 USD | 19,350.00 USD | 29,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.00` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 10,760,000.00 USD | 10,760,000.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.40` | 4,830,000.00 USD | 4,830,000.00 USD | 7,160.00 USD | 11,520.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 10,830,000.00 USD | 10,830,000.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.80` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 239.05 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.20` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.20` | 10,890,000.00 USD | 10,890,000.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.60` | 4,840,000.00 USD | 4,840,000.00 USD | 4,240.00 USD | 3,720.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 10,940,000.00 USD | 10,940,000.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 1,400.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 10,970,000.00 USD | 10,970,000.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.40` | 4,860,000.00 USD | 4,860,000.00 USD | 3,750.00 USD | 144.50 USD | 2.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 11,050,000.00 USD | 11,050,000.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.80` | 4,860,000.00 USD | 4,860,000.00 USD | 118.95 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.20` | 4,870,000.00 USD | 4,870,000.00 USD | 2,100.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.20` | 11,150,000.00 USD | 11,150,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.60` | 4,880,000.00 USD | 4,880,000.00 USD | 11,090.00 USD | 3,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.70` | 4,890,000.00 USD | 4,890,000.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 11,210,000.00 USD | 11,210,000.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 11,220,000.00 USD | 11,220,000.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 11,230,000.00 USD | 11,230,000.00 USD | 620.15 USD | 721.55 USD | 67.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.20` | 11,300,000.00 USD | 11,300,000.00 USD | 23,930.00 USD | 13,700.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.70` | 11,390,000.00 USD | 11,390,000.00 USD | 11,230.00 USD | 44,600.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.20` | 11,410,000.00 USD | 11,410,000.00 USD | 366.90 USD | 18,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 11,420,000.00 USD | 11,420,000.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.20` | 11,520,000.00 USD | 11,520,000.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 23,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `323.50` | 2,220.00 USD | 25,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 51,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `339.50` | 1,360.00 USD | 52,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 53,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 53,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `374.50` | 41,200.00 USD | 95,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 141,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `477.50` | 8,200.00 USD | 149,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 150,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 151,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `66.50` | 201,600.00 USD | 0.00 USD | 2,730.00 USD | `-76.56%` | `41,012,000,000.00` |
| `Live` | `Long` | `73.50` | 198,870.00 USD | 0.00 USD | 277.83 USD | `-74.09%` | `3,780,000,000.00` |
| `Live` | `Long` | `75.50` | 198,590.00 USD | 0.00 USD | 541.71 USD | `-73.38%` | `7,175,000,000.00` |
| `Live` | `Long` | `84.50` | 198,050.00 USD | 0.00 USD | 1,110.00 USD | `-70.21%` | `13,105,000,000.00` |
| `Live` | `Long` | `93.50` | 196,950.00 USD | 0.00 USD | 146.70 USD | `-67.04%` | `1,569,000,000.00` |
| `Live` | `Long` | `95.50` | 196,800.00 USD | 0.00 USD | 920.05 USD | `-66.33%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 195,880.00 USD | 0.00 USD | 6,240.00 USD | `-64.22%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 189,640.00 USD | 0.00 USD | 4,080.00 USD | `-63.87%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 185,560.00 USD | 0.00 USD | 212.76 USD | `-61.40%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 185,350.00 USD | 0.00 USD | 212.35 USD | `-58.23%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 185,140.00 USD | 0.00 USD | 3,190.00 USD | `-56.82%` | `26,016,000,000.00` |
| `Live` | `Long` | `125.50` | 181,950.00 USD | 0.00 USD | 125.50 USD | `-55.76%` | `1,000,000,000.00` |
| `Live` | `Long` | `126.50` | 181,830.00 USD | 0.00 USD | 658.18 USD | `-55.41%` | `5,203,000,000.00` |
| `Live` | `Long` | `133.50` | 181,170.00 USD | 0.00 USD | 2,000.00 USD | `-52.94%` | `15,000,000,000.00` |
| `Live` | `Long` | `147.50` | 179,170.00 USD | 0.00 USD | 895.47 USD | `-48.00%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 178,270.00 USD | 0.00 USD | 1,270.00 USD | `-47.65%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 177,000.00 USD | 0.00 USD | 2,370.00 USD | `-47.30%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 174,640.00 USD | 0.00 USD | 303.78 USD | `-46.24%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 174,330.00 USD | 0.00 USD | 325.00 USD | `-42.72%` | `2,000,000,000.00` |
| `Live` | `Long` | `165.50` | 174,010.00 USD | 0.00 USD | 8,280.00 USD | `-41.66%` | `50,000,000,000.00` |
| `Live` | `Long` | `167.50` | 165,730.00 USD | 0.00 USD | 285.75 USD | `-40.95%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 165,450.00 USD | 0.00 USD | 426.25 USD | `-39.89%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 165,020.00 USD | 0.00 USD | 169.96 USD | `-38.48%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 164,850.00 USD | 0.00 USD | 516.67 USD | `-38.13%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 164,340.00 USD | 0.00 USD | 373.83 USD | `-37.78%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 163,960.00 USD | 0.00 USD | 2,310.00 USD | `-35.31%` | `12,599,000,000.00` |
| `Live` | `Long` | `184.50` | 161,650.00 USD | 0.00 USD | 808.66 USD | `-34.96%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 160,840.00 USD | 0.00 USD | 418.28 USD | `-33.55%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 160,420.00 USD | 0.00 USD | 694.75 USD | `-32.84%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 159,730.00 USD | 0.00 USD | 858.49 USD | `-32.49%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 158,870.00 USD | 0.00 USD | 1,490.00 USD | `-32.14%` | `7,715,000,000.00` |
| `Live` | `Long` | `193.50` | 157,380.00 USD | 0.00 USD | 1,050.00 USD | `-31.79%` | `5,434,000,000.00` |
| `Live` | `Long` | `195.50` | 156,330.00 USD | 0.00 USD | 370.47 USD | `-31.08%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 155,960.00 USD | 0.00 USD | 2,290.00 USD | `-30.73%` | `11,644,000,000.00` |
| `Live` | `Long` | `199.50` | 153,670.00 USD | 0.00 USD | 548.03 USD | `-29.67%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 153,130.00 USD | 0.00 USD | 293.13 USD | `-29.32%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 152,830.00 USD | 0.00 USD | 420.39 USD | `-28.61%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 152,410.00 USD | 0.00 USD | 191.53 USD | `-27.56%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 152,220.00 USD | 0.00 USD | 42,410.00 USD | `-27.20%` | `205,387,000,000.00` |
| `Live` | `Long` | `210.50` | 109,810.00 USD | 0.00 USD | 108.83 USD | `-25.79%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 109,700.00 USD | 0.00 USD | 6,660.00 USD | `-25.44%` | `31,500,000,000.00` |
| `Live` | `Long` | `213.50` | 103,040.00 USD | 0.00 USD | 3,800.00 USD | `-24.74%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 99,230.00 USD | 0.00 USD | 2,610.00 USD | `-24.03%` | `12,132,000,000.00` |
| `Live` | `Long` | `223.50` | 96,620.00 USD | 0.00 USD | 32,860.00 USD | `-21.21%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 63,760.00 USD | 0.00 USD | 5,340.00 USD | `-20.86%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 58,420.00 USD | 0.00 USD | 1,240.00 USD | `-20.15%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 57,180.00 USD | 0.00 USD | 174.49 USD | `-19.80%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 57,010.00 USD | 0.00 USD | 1,320.00 USD | `-19.45%` | `5,783,000,000.00` |
| `Live` | `Long` | `229.50` | 55,680.00 USD | 0.00 USD | 1,300.00 USD | `-19.10%` | `5,671,000,000.00` |
| `Live` | `Long` | `231.50` | 54,380.00 USD | 0.00 USD | 295.86 USD | `-18.39%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 54,090.00 USD | 0.00 USD | 632.17 USD | `-18.04%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 53,460.00 USD | 0.00 USD | 30,780.00 USD | `-16.28%` | `129,590,000,000.00` |
| `Live` | `Long` | `239.50` | 22,680.00 USD | 0.00 USD | 1,030.00 USD | `-15.57%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 21,650.00 USD | 0.00 USD | 251.88 USD | `-14.87%` | `1,043,000,000.00` |
| `Live` | `Long` | `242.50` | 21,400.00 USD | 0.00 USD | 1,520.00 USD | `-14.51%` | `6,274,000,000.00` |
| `Live` | `Long` | `243.50` | 19,880.00 USD | 0.00 USD | 1,850.00 USD | `-14.16%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 18,030.00 USD | 0.00 USD | 4,220.00 USD | `-13.81%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 13,810.00 USD | 0.00 USD | 1,030.00 USD | `-13.46%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 12,780.00 USD | 0.00 USD | 106.67 USD | `-12.75%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 12,670.00 USD | 0.00 USD | 595.16 USD | `-12.40%` | `2,395,000,000.00` |
| `Live` | `Long` | `249.50` | 12,080.00 USD | 0.00 USD | 1,590.00 USD | `-12.05%` | `6,354,000,000.00` |
| `Live` | `Long` | `250.50` | 10,490.00 USD | 0.00 USD | 1,330.00 USD | `-11.69%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 9,170.00 USD | 0.00 USD | 268.35 USD | `-11.34%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 8,900.00 USD | 0.00 USD | 1,170.00 USD | `-10.99%` | `4,639,000,000.00` |
| `Live` | `Long` | `254.50` | 7,730.00 USD | 0.00 USD | 548.45 USD | `-10.28%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 7,180.00 USD | 0.00 USD | 4,490.00 USD | `-9.58%` | `17,514,000,000.00` |
| `Live` | `Long` | `257.50` | 2,690.00 USD | 0.00 USD | 467.62 USD | `-9.23%` | `1,816,000,000.00` |
| `Live` | `Long` | `258.50` | 2,220.00 USD | 0.00 USD | 176.56 USD | `-8.87%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 2,040.00 USD | 0.00 USD | 2,040.00 USD | `-8.17%` | `7,839,000,000.00` |
| `Live` | `Short` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | `+1.35%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 1,070.00 USD | 954.95 USD | 0.00 USD | `+2.76%` | `3,276,000,000.00` |
| `Live` | `Short` | `296.50` | 7,200.00 USD | 6,130.00 USD | 0.00 USD | `+4.52%` | `20,668,000,000.00` |
| `Live` | `Short` | `298.50` | 7,640.00 USD | 442.08 USD | 0.00 USD | `+5.23%` | `1,481,000,000.00` |
| `Live` | `Short` | `300.50` | 22,180.00 USD | 14,550.00 USD | 0.00 USD | `+5.93%` | `48,404,000,000.00` |
| `Live` | `Short` | `320.50` | 23,290.00 USD | 1,110.00 USD | 0.00 USD | `+12.98%` | `3,452,000,000.00` |
| `Live` | `Short` | `323.50` | 25,510.00 USD | 2,220.00 USD | 0.00 USD | `+14.04%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 51,040.00 USD | 25,530.00 USD | 0.00 USD | `+15.10%` | `78,189,000,000.00` |
| `Live` | `Short` | `339.50` | 52,390.00 USD | 1,360.00 USD | 0.00 USD | `+19.68%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 53,400.00 USD | 1,010.00 USD | 0.00 USD | `+26.38%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 53,850.00 USD | 445.52 USD | 0.00 USD | `+29.90%` | `1,209,000,000.00` |
| `Live` | `Short` | `374.50` | 95,040.00 USD | 41,200.00 USD | 0.00 USD | `+32.02%` | `110,000,000,000.00` |
| `Live` | `Short` | `459.50` | 141,300.00 USD | 46,250.00 USD | 0.00 USD | `+61.98%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 149,500.00 USD | 8,200.00 USD | 0.00 USD | `+68.33%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 150,210.00 USD | 718.34 USD | 0.00 USD | `+75.73%` | `1,441,000,000.00` |
| `Live` | `Short` | `560.50` | 151,060.00 USD | 842.43 USD | 0.00 USD | `+97.59%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 449,470.00 USD | 0.00 USD | 210.94 USD | `-49.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 449,260.00 USD | 0.00 USD | 2,070.00 USD | `-48.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 447,190.00 USD | 0.00 USD | 489.38 USD | `-41.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 446,700.00 USD | 0.00 USD | 2,530.00 USD | `-37.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 444,170.00 USD | 0.00 USD | 490.59 USD | `-34.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 443,680.00 USD | 0.00 USD | 482.01 USD | `-30.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 443,200.00 USD | 0.00 USD | 189.07 USD | `-29.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 443,010.00 USD | 0.00 USD | 441.60 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 442,570.00 USD | 0.00 USD | 299.96 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 442,270.00 USD | 0.00 USD | 715.29 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 441,550.00 USD | 0.00 USD | 638.36 USD | `-21.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 440,920.00 USD | 0.00 USD | 740.85 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 440,170.00 USD | 0.00 USD | 478.48 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 439,700.00 USD | 0.00 USD | 389.48 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 439,310.00 USD | 0.00 USD | 812.38 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 438,490.00 USD | 0.00 USD | 220.64 USD | `-16.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 438,270.00 USD | 0.00 USD | 429.30 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 437,840.00 USD | 0.00 USD | 296.50 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 437,550.00 USD | 0.00 USD | 216.45 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 437,330.00 USD | 0.00 USD | 387.76 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 436,940.00 USD | 0.00 USD | 9,420.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 427,530.00 USD | 0.00 USD | 1,630.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 425,900.00 USD | 0.00 USD | 2,700.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 423,200.00 USD | 0.00 USD | 2,940.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 420,260.00 USD | 0.00 USD | 4,560.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 415,700.00 USD | 0.00 USD | 1,850.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 413,850.00 USD | 0.00 USD | 231.54 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 413,620.00 USD | 0.00 USD | 109.26 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 413,510.00 USD | 0.00 USD | 1,780.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 411,730.00 USD | 0.00 USD | 51,300.00 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 360,430.00 USD | 0.00 USD | 250.81 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 360,180.00 USD | 0.00 USD | 2,370.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 357,810.00 USD | 0.00 USD | 269,800.00 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 88,020.00 USD | 0.00 USD | 857.85 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 87,160.00 USD | 0.00 USD | 320.15 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 86,840.00 USD | 0.00 USD | 199.17 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 86,640.00 USD | 0.00 USD | 2,180.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 84,460.00 USD | 0.00 USD | 241.98 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 84,220.00 USD | 0.00 USD | 219.35 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 84,000.00 USD | 0.00 USD | 107.40 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 83,890.00 USD | 0.00 USD | 29,530.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 54,370.00 USD | 0.00 USD | 3,340.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 51,020.00 USD | 0.00 USD | 620.38 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 50,400.00 USD | 0.00 USD | 13,500.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 36,910.00 USD | 0.00 USD | 1,010.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 35,890.00 USD | 0.00 USD | 667.86 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 35,220.00 USD | 0.00 USD | 299.74 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 34,920.00 USD | 0.00 USD | 903.60 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 34,020.00 USD | 0.00 USD | 326.34 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 33,690.00 USD | 0.00 USD | 125.88 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 33,570.00 USD | 0.00 USD | 21,990.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 11,580.00 USD | 0.00 USD | 3,080.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 8,500.00 USD | 0.00 USD | 104.72 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 8,400.00 USD | 0.00 USD | 355.67 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 8,040.00 USD | 0.00 USD | 8,040.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 2,010.00 USD | 2,010.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 3,060.00 USD | 1,050.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 3,340.00 USD | 280.77 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 8,500.00 USD | 5,160.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 8,760.00 USD | 261.96 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 9,290.00 USD | 530.36 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 11,440.00 USD | 2,150.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 36,720.00 USD | 25,280.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 36,820.00 USD | 107.05 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 37,820.00 USD | 992.62 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 39,840.00 USD | 2,020.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 44,560.00 USD | 4,730.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 44,670.00 USD | 110.37 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 45,060.00 USD | 388.95 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 45,220.00 USD | 153.94 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 55,990.00 USD | 10,780.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 66,720.00 USD | 10,730.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 69,370.00 USD | 2,650.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 69,470.00 USD | 102.73 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 83,970.00 USD | 14,500.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 84,600.00 USD | 634.04 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 85,640.00 USD | 1,030.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 91,290.00 USD | 5,650.00 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 91,820.00 USD | 534.59 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 92,140.00 USD | 321.50 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 158,860.00 USD | 66,720.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 159,950.00 USD | 1,090.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 171,940.00 USD | 12,000.00 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 172,490.00 USD | 547.52 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 172,600.00 USD | 110.91 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 172,860.00 USD | 257.45 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 173,030.00 USD | 174.25 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 173,190.00 USD | 151.50 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 174,640.00 USD | 1,450.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 176,410.00 USD | 1,770.00 USD | 0.00 USD | `+26.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 176,740.00 USD | 326.07 USD | 0.00 USD | `+27.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 177,570.00 USD | 826.60 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 185,010.00 USD | 7,440.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 185,690.00 USD | 682.84 USD | 0.00 USD | `+30.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 186,790.00 USD | 1,100.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 187,480.00 USD | 683.96 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 187,680.00 USD | 199.75 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 188,970.00 USD | 1,290.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 190,010.00 USD | 1,040.00 USD | 0.00 USD | `+42.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 190,380.00 USD | 376.71 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 190,540.00 USD | 158.86 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 196,440.00 USD | 5,900.00 USD | 0.00 USD | `+46.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 197,520.00 USD | 1,080.00 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 199,220.00 USD | 1,700.00 USD | 0.00 USD | `+50.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 200,770.00 USD | 1,550.00 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 202,160.00 USD | 1,380.00 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 202,780.00 USD | 621.14 USD | 0.00 USD | `+53.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 205,060.00 USD | 2,280.00 USD | 0.00 USD | `+55.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 205,280.00 USD | 222.75 USD | 0.00 USD | `+57.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 212,200.00 USD | 6,920.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 218,120.00 USD | 5,920.00 USD | 0.00 USD | `+59.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 219,250.00 USD | 1,130.00 USD | 0.00 USD | `+62.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 226,880.00 USD | 7,630.00 USD | 0.00 USD | `+70.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 227,860.00 USD | 975.00 USD | 0.00 USD | `+71.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 228,840.00 USD | 981.00 USD | 0.00 USD | `+72.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 229,340.00 USD | 499.50 USD | 0.00 USD | `+76.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,120,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+76.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,120,000.00 USD | 1,000.00 USD | 0.00 USD | `+76.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,120,000.00 USD | 1,040.00 USD | 0.00 USD | `+82.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,120,000.00 USD | 340.67 USD | 0.00 USD | `+84.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,120,000.00 USD | 638.86 USD | 0.00 USD | `+96.18%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.70` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD |
| `7D` | `235.20` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD |
| `7D` | `235.70` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD |
| `7D` | `236.20` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD |
| `7D` | `236.70` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD |
| `7D` | `237.20` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD |
| `7D` | `237.70` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `238.20` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD |
| `7D` | `238.70` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD |
| `7D` | `239.20` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.70` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.70` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `241.20` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.70` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.20` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD |
| `7D` | `242.70` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `243.20` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD |
| `7D` | `243.70` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `244.20` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.70` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD |
| `7D` | `245.20` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD |
| `7D` | `245.70` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD |
| `7D` | `246.20` | 9,650,000.00 USD | 0.00 USD | 9,650,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD |
| `7D` | `246.70` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD |
| `7D` | `247.20` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD |
| `7D` | `247.70` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD |
| `7D` | `248.20` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD |
| `7D` | `248.70` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD |
| `7D` | `249.20` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD |
| `7D` | `249.70` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD |
| `1D` | `250.20` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 19,400.00 USD | 7,530.00 USD | 7,410.00 USD |
| `7D` | `250.20` | 9,260,000.00 USD | 0.00 USD | 9,260,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD |
| `1D` | `250.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 8,330.00 USD | 2,460.00 USD | 6,370.00 USD |
| `7D` | `250.70` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD |
| `1D` | `251.00` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 28,550.00 USD | 38,930.00 USD | 11,150.00 USD |
| `7D` | `251.20` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD |
| `1D` | `251.40` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 11,230.00 USD | 36,660.00 USD | 32,730.00 USD |
| `7D` | `251.70` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD |
| `1D` | `251.80` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 34,810.00 USD | 54,770.00 USD | 11,290.00 USD |
| `1D` | `252.20` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 25,960.00 USD | 8,130.00 USD | 14,660.00 USD |
| `7D` | `252.20` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD |
| `1D` | `252.60` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 12,330.00 USD | 1,550.00 USD | 3,490.00 USD |
| `7D` | `252.70` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD |
| `1D` | `253.00` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 8,050.00 USD | 11,430.00 USD | 4,350.00 USD |
| `7D` | `253.20` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD |
| `1D` | `253.40` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 15,470.00 USD | 16,560.00 USD | 15,760.00 USD |
| `7D` | `253.70` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD |
| `1D` | `253.80` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 6,930.00 USD | 7,470.00 USD | 11,030.00 USD |
| `1D` | `254.20` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 1,590.00 USD | 3,710.00 USD | 3,940.00 USD |
| `7D` | `254.20` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD |
| `1D` | `254.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 9,130.00 USD | 11,220.00 USD | 0.82 USD |
| `7D` | `254.70` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD |
| `1D` | `255.00` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 14,600.00 USD | 8,110.00 USD | 3,240.00 USD |
| `7D` | `255.20` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 32,100.00 USD | 13,440.00 USD | 35,520.00 USD |
| `1D` | `255.40` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 2,600.00 USD | 16,230.00 USD | 19,220.00 USD |
| `7D` | `255.70` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 33,430.00 USD | 16,550.00 USD | 35,380.00 USD |
| `1D` | `255.80` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 19,840.00 USD | 11,010.00 USD | 12,610.00 USD |
| `1D` | `256.20` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 884.48 USD | 30,930.00 USD | 15,090.00 USD |
| `7D` | `256.20` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD |
| `1D` | `256.60` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 7,420.00 USD | 4,010.00 USD | 4.12 USD |
| `7D` | `256.70` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD |
| `1D` | `257.00` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 9,580.00 USD | 1,470.00 USD | 8,870.00 USD |
| `7D` | `257.20` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD |
| `1D` | `257.40` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 6,290.00 USD | 4,650.00 USD | 8,330.00 USD |
| `7D` | `257.70` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD |
| `1D` | `257.80` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 1,500.00 USD | 2,430.00 USD | 6,450.00 USD |
| `1D` | `258.20` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 21,220.00 USD | 15,910.00 USD | 56,550.00 USD |
| `7D` | `258.20` | 7,490,000.00 USD | 0.00 USD | 7,490,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD |
| `1D` | `258.60` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 25,120.00 USD | 8,910.00 USD | 40,000.00 USD |
| `7D` | `258.70` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD |
| `1D` | `259.00` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 12,700.00 USD | 34,640.00 USD | 7.60 USD |
| `7D` | `259.20` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD |
| `1D` | `259.40` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 14,770.00 USD | 3,600.00 USD | 17,640.00 USD |
| `7D` | `259.70` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD |
| `1D` | `259.80` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 41,920.00 USD | 32,160.00 USD | 39,290.00 USD |
| `1D` | `260.20` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 4,720.00 USD | 8,150.00 USD | 6,870.00 USD |
| `7D` | `260.20` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD |
| `1D` | `260.60` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 20,220.00 USD | 6,120.00 USD | 27,210.00 USD |
| `7D` | `260.70` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD |
| `1D` | `261.00` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 8,310.00 USD | 48,880.00 USD | 44,770.00 USD |
| `7D` | `261.20` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD |
| `1D` | `261.40` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 7,780.00 USD | 43,600.00 USD | 2,570.00 USD |
| `7D` | `261.70` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD |
| `1D` | `261.80` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 15,410.00 USD | 47,140.00 USD | 62,120.00 USD |
| `1D` | `262.20` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 34,470.00 USD | 27,340.00 USD | 21,320.00 USD |
| `7D` | `262.20` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD |
| `1D` | `262.60` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 366.04 USD | 539.35 USD | 13,400.00 USD |
| `7D` | `262.70` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD |
| `1D` | `263.00` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 8,670.00 USD | 12,480.00 USD | 6,180.00 USD |
| `7D` | `263.20` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD |
| `1D` | `263.40` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 30,700.00 USD | 4,190.00 USD | 74,200.00 USD |
| `7D` | `263.70` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD |
| `1D` | `263.80` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 32,740.00 USD | 29,870.00 USD | 28,460.00 USD |
| `1D` | `264.20` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 25,990.00 USD | 15,290.00 USD | 17,150.00 USD |
| `7D` | `264.20` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD |
| `1D` | `264.60` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 1,370.00 USD | 19,610.00 USD | 19,930.00 USD |
| `7D` | `264.70` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD |
| `1D` | `265.00` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 32,870.00 USD | 1,190.00 USD | 33,270.00 USD |
| `7D` | `265.20` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD |
| `1D` | `265.40` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 64,290.00 USD | 1,260.00 USD | 3.40 USD |
| `7D` | `265.70` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD |
| `1D` | `265.80` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `266.20` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 3,880.00 USD | 13,250.00 USD | 4,800.00 USD |
| `7D` | `266.20` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD |
| `1D` | `266.60` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 28,430.00 USD | 8,190.00 USD | 0.00 USD |
| `7D` | `266.70` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD |
| `1D` | `267.00` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 47,770.00 USD | 22,400.00 USD | 0.00 USD |
| `7D` | `267.20` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD |
| `1D` | `267.40` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 7,660.00 USD | 68,160.00 USD | 22,320.00 USD |
| `7D` | `267.70` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD |
| `1D` | `267.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 4,660.00 USD | 36,050.00 USD | 5,280.00 USD |
| `1D` | `268.20` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 4,570.00 USD | 35,070.00 USD | 63,430.00 USD |
| `7D` | `268.20` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD |
| `7D` | `268.70` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD |
| `1D` | `269.00` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 8,580.00 USD | 321.80 USD | 20.82 USD |
| `7D` | `269.20` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD |
| `1D` | `269.40` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 16,500.00 USD | 10,200.00 USD |
| `7D` | `269.70` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD |
| `1D` | `269.80` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 378.60 USD | 618.10 USD | 3,380.00 USD |
| `1D` | `270.20` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD |
| `7D` | `270.20` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD |
| `1D` | `270.60` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `270.70` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD |
| `1D` | `271.00` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 323.80 USD | 7,970.00 USD | 2,750.00 USD |
| `1D` | `271.40` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 12,710.00 USD | 0.00 USD | 5,300.00 USD |
| `7D` | `271.70` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD |
| `1D` | `271.80` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 25,790.00 USD | 9,610.00 USD |
| `1D` | `272.20` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 15,100.00 USD | 15,900.00 USD | 10,160.00 USD |
| `7D` | `272.20` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.60` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 27,370.00 USD | 16,330.00 USD | 53,230.00 USD |
| `7D` | `272.70` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 25,660.00 USD | 17,630.00 USD | 47,720.00 USD |
| `1D` | `273.00` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 33,780.00 USD | 21,290.00 USD | 30,900.00 USD |
| `7D` | `273.20` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD |
| `1D` | `273.40` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 9,330.00 USD | 82,780.00 USD | 10,240.00 USD |
| `7D` | `273.70` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD |
| `1D` | `273.80` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 37,900.00 USD | 70,140.00 USD | 49,200.00 USD |
| `1D` | `274.20` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 224,890.00 USD | 0.00 USD | 12,870.00 USD |
| `7D` | `274.20` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.60` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 215,540.00 USD | 19,960.00 USD | 41,170.00 USD |
| `7D` | `274.70` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD |
| `1D` | `275.00` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.20` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.40` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD |
| `7D` | `275.70` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD |
| `1D` | `275.80` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 20,900.00 USD | 10,450.00 USD | 40,360.00 USD |
| `1D` | `276.20` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 89,570.00 USD | 0.00 USD | 3,220.00 USD |
| `7D` | `276.20` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD |
| `1D` | `276.60` | 921,220.00 USD | 0.00 USD | 921,220.00 USD | 11,880.00 USD | 9,200.00 USD | 5,600.00 USD |
| `7D` | `276.70` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `277.00` | 894,550.00 USD | 0.00 USD | 894,550.00 USD | 25,410.00 USD | 4,330.00 USD | 16,100.00 USD |
| `7D` | `277.20` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD |
| `1D` | `277.40` | 848,700.00 USD | 0.00 USD | 848,700.00 USD | 301.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.70` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD |
| `1D` | `277.80` | 848,400.00 USD | 0.00 USD | 848,400.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD |
| `1D` | `278.20` | 828,100.00 USD | 0.00 USD | 828,100.00 USD | 12,120.00 USD | 65,540.00 USD | 56,220.00 USD |
| `7D` | `278.20` | 669,540.00 USD | 0.00 USD | 669,540.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD |
| `1D` | `278.60` | 694,220.00 USD | 0.00 USD | 694,220.00 USD | 79,560.00 USD | 55,720.00 USD | 61,800.00 USD |
| `7D` | `278.70` | 512,260.00 USD | 0.00 USD | 512,260.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD |
| `1D` | `279.00` | 497,130.00 USD | 0.00 USD | 497,130.00 USD | 1,710.00 USD | 53,110.00 USD | 0.00 USD |
| `7D` | `279.20` | 460,020.00 USD | 0.00 USD | 460,020.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.70` | 457,350.00 USD | 0.00 USD | 457,350.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `279.80` | 442,310.00 USD | 0.00 USD | 442,310.00 USD | 14,720.00 USD | 14,930.00 USD | 31,350.00 USD |
| `1D` | `280.20` | 381,310.00 USD | 0.00 USD | 381,310.00 USD | 14,910.00 USD | 26,680.00 USD | 50,610.00 USD |
| `7D` | `280.20` | 455,590.00 USD | 0.00 USD | 455,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD |
| `1D` | `280.60` | 289,110.00 USD | 0.00 USD | 289,110.00 USD | 28,040.00 USD | 49,180.00 USD | 46,430.00 USD |
| `7D` | `280.70` | 438,230.00 USD | 0.00 USD | 438,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `281.00` | 165,460.00 USD | 0.00 USD | 165,460.00 USD | 10,450.00 USD | 8,090.00 USD | 12.68 USD |
| `7D` | `281.20` | 422,680.00 USD | 0.00 USD | 422,680.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `1D` | `281.40` | 146,910.00 USD | 0.00 USD | 146,910.00 USD | 2,280.00 USD | 6,950.00 USD | 0.00 USD |
| `7D` | `281.70` | 325,280.00 USD | 0.00 USD | 325,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `281.80` | 137,680.00 USD | 0.00 USD | 137,680.00 USD | 0.00 USD | 12,900.00 USD | 4,140.00 USD |
| `1D` | `282.20` | 120,630.00 USD | 0.00 USD | 120,630.00 USD | 10,310.00 USD | 8,490.00 USD | 0.00 USD |
| `7D` | `282.20` | 127,860.00 USD | 0.00 USD | 127,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.60` | 101,830.00 USD | 0.00 USD | 101,830.00 USD | 0.00 USD | 34,420.00 USD | 19.90 USD |
| `1D` | `283.00` | 67,380.00 USD | 0.00 USD | 67,380.00 USD | 14,930.00 USD | 36,060.00 USD | 26.04 USD |
| `7D` | `283.20` | 103,640.00 USD | 0.00 USD | 103,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD |
| `1D` | `283.40` | 16,370.00 USD | 0.00 USD | 16,370.00 USD | 1,280.00 USD | 15,060.00 USD | 21.32 USD |
| `7D` | `283.70` | 2,000.00 USD | 0.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.20` | 3,800.00 USD | 3,800.00 USD | 0.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD |
| `7D` | `284.20` | 74,590.00 USD | 74,590.00 USD | 0.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD |
| `1D` | `284.60` | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | 0.00 USD |
| `7D` | `284.70` | 431,170.00 USD | 431,170.00 USD | 0.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD |
| `1D` | `285.00` | 55,810.00 USD | 55,810.00 USD | 0.00 USD | 29,420.00 USD | 21,230.00 USD | 9.04 USD |
| `7D` | `285.20` | 843,250.00 USD | 843,250.00 USD | 0.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD |
| `1D` | `285.40` | 361,600.00 USD | 361,600.00 USD | 0.00 USD | 99,300.00 USD | 125,760.00 USD | 80,730.00 USD |
| `7D` | `285.70` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD |
| `1D` | `285.80` | 446,640.00 USD | 446,640.00 USD | 0.00 USD | 59,140.00 USD | 7,790.00 USD | 18,110.00 USD |
| `1D` | `286.20` | 465,230.00 USD | 465,230.00 USD | 0.00 USD | 13,210.00 USD | 284.90 USD | 5,100.00 USD |
| `7D` | `286.20` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD |
| `1D` | `286.60` | 499,590.00 USD | 499,590.00 USD | 0.00 USD | 2,290.00 USD | 1,930.00 USD | 30,140.00 USD |
| `7D` | `286.70` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD |
| `1D` | `287.00` | 657,480.00 USD | 657,480.00 USD | 0.00 USD | 32,920.00 USD | 37,170.00 USD | 87,790.00 USD |
| `7D` | `287.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD |
| `1D` | `287.40` | 732,720.00 USD | 732,720.00 USD | 0.00 USD | 24,060.00 USD | 22,520.00 USD | 28,650.00 USD |
| `7D` | `287.70` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD |
| `1D` | `287.80` | 817,630.00 USD | 817,630.00 USD | 0.00 USD | 13,160.00 USD | 13,520.00 USD | 58,230.00 USD |
| `1D` | `288.20` | 921,110.00 USD | 921,110.00 USD | 0.00 USD | 69,440.00 USD | 19,850.00 USD | 14,180.00 USD |
| `7D` | `288.20` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD |
| `1D` | `288.60` | 966,890.00 USD | 966,890.00 USD | 0.00 USD | 6,190.00 USD | 19,100.00 USD | 20,490.00 USD |
| `7D` | `288.70` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD |
| `1D` | `289.00` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 16,170.00 USD | 16,460.00 USD | 9,870.00 USD |
| `7D` | `289.20` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 21,350.00 USD | 29,380.00 USD | 89,090.00 USD |
| `7D` | `289.70` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 99,990.00 USD | 134,010.00 USD |
| `1D` | `289.80` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 48,610.00 USD | 43,130.00 USD | 41,520.00 USD |
| `1D` | `290.20` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 38,050.00 USD | 29,720.00 USD | 39,570.00 USD |
| `7D` | `290.20` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD |
| `1D` | `290.60` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 4,230.00 USD | 82,920.00 USD | 46,650.00 USD |
| `7D` | `290.70` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 0.00 USD |
| `1D` | `291.00` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 34,600.00 USD | 7,260.00 USD | 0.00 USD |
| `7D` | `291.20` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD |
| `1D` | `291.40` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 10,310.00 USD | 22,770.00 USD | 19.25 USD |
| `7D` | `291.70` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD |
| `1D` | `291.80` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 684.64 USD | 29,680.00 USD | 22,160.00 USD |
| `1D` | `292.20` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 11,300.00 USD | 35,410.00 USD | 11,500.00 USD |
| `7D` | `292.20` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD |
| `1D` | `292.60` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 22,800.00 USD | 15,930.00 USD | 2,250.00 USD |
| `7D` | `292.70` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD |
| `1D` | `293.00` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 21,400.00 USD | 25,600.00 USD | 16,840.00 USD |
| `7D` | `293.20` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD |
| `1D` | `293.40` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 10,870.00 USD | 25,220.00 USD | 23,900.00 USD |
| `7D` | `293.70` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD |
| `1D` | `293.80` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 91,520.00 USD | 33,690.00 USD | 50,500.00 USD |
| `1D` | `294.20` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 6,580.00 USD | 22,130.00 USD | 44,850.00 USD |
| `7D` | `294.20` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD |
| `1D` | `294.60` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 101,910.00 USD | 69,320.00 USD | 85,210.00 USD |
| `7D` | `294.70` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD |
| `1D` | `295.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 12,710.00 USD | 10,340.00 USD | 72,570.00 USD |
| `7D` | `295.20` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD |
| `1D` | `295.40` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 43,160.00 USD | 39,530.00 USD | 59,140.00 USD |
| `7D` | `295.70` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 176,660.00 USD | 91,790.00 USD | 264,470.00 USD |
| `1D` | `295.80` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 66,570.00 USD | 22,770.00 USD | 112,830.00 USD |
| `1D` | `296.20` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 65,430.00 USD | 99,010.00 USD | 32,990.00 USD |
| `7D` | `296.20` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD |
| `1D` | `296.60` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 30,750.00 USD | 211.38 USD | 20,610.00 USD |
| `7D` | `296.70` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD |
| `1D` | `297.00` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,080.00 USD | 21,880.00 USD | 82,140.00 USD |
| `7D` | `297.20` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD |
| `1D` | `297.40` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 61,300.00 USD | 9,700.00 USD | 27,500.00 USD |
| `7D` | `297.70` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD |
| `1D` | `297.80` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 16,070.00 USD | 4,170.00 USD | 12,070.00 USD |
| `1D` | `298.20` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 55,370.00 USD | 5,280.00 USD | 84,890.00 USD |
| `7D` | `298.20` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD |
| `1D` | `298.60` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 18,490.00 USD | 920.82 USD | 61,070.00 USD |
| `7D` | `298.70` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD |
| `1D` | `299.00` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 13,520.00 USD | 5,530.00 USD | 46,700.00 USD |
| `7D` | `299.20` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD |
| `1D` | `299.40` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 35,710.00 USD | 15,230.00 USD | 31,470.00 USD |
| `7D` | `299.70` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD |
| `1D` | `299.80` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 3,330.00 USD | 6,420.00 USD | 30,240.00 USD |
| `1D` | `300.20` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 32,520.00 USD | 36,610.00 USD | 42,600.00 USD |
| `7D` | `300.20` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD |
| `1D` | `300.60` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 10,120.00 USD | 940.65 USD | 17,180.00 USD |
| `7D` | `300.70` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD |
| `1D` | `301.00` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 521.60 USD | 6,330.00 USD | 29,430.00 USD |
| `7D` | `301.20` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD |
| `1D` | `301.40` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 582.35 USD | 9,670.00 USD | 36,290.00 USD |
| `7D` | `301.70` | 6,680,000.00 USD | 6,680,000.00 USD | 0.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD |
| `1D` | `301.80` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 19,640.00 USD | 31,100.00 USD | 10,350.00 USD |
| `1D` | `302.20` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 25,460.00 USD | 8,900.00 USD | 20.89 USD |
| `7D` | `302.20` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD |
| `1D` | `302.60` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 14,410.00 USD | 11,620.00 USD | 38,380.00 USD |
| `7D` | `302.70` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD |
| `1D` | `303.00` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 20,600.00 USD | 1,490.00 USD | 13,980.00 USD |
| `7D` | `303.20` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD |
| `1D` | `303.40` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 336.16 USD | 2,630.00 USD | 9,360.00 USD |
| `7D` | `303.70` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD |
| `1D` | `303.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 315.07 USD | 1.44 USD |
| `1D` | `304.20` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 21,920.00 USD | 3,360.00 USD | 40,420.00 USD |
| `7D` | `304.20` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD |
| `1D` | `304.60` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 9,710.00 USD | 1,990.00 USD | 44,520.00 USD |
| `7D` | `304.70` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD |
| `1D` | `305.00` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 9,740.00 USD | 7,030.00 USD | 3,310.00 USD |
| `7D` | `305.20` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD |
| `1D` | `305.40` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 4,950.00 USD | 1,710.00 USD | 2,210.00 USD |
| `7D` | `305.70` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD |
| `1D` | `305.80` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 11,730.00 USD | 5,750.00 USD | 5,870.00 USD |
| `1D` | `306.20` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 6,970.00 USD | 321.71 USD | 6,370.00 USD |
| `7D` | `306.20` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD |
| `1D` | `306.60` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 4,420.00 USD | 13,560.00 USD | 7,060.00 USD |
| `7D` | `306.70` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD |
| `1D` | `307.00` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 31,700.00 USD | 33,620.00 USD | 16,140.00 USD |
| `7D` | `307.20` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD |
| `1D` | `307.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 4,260.00 USD | 45,320.00 USD | 21,030.00 USD |
| `7D` | `307.70` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD |
| `1D` | `307.80` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 34,800.00 USD | 37,350.00 USD | 10,910.00 USD |
| `1D` | `308.20` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 24,360.00 USD | 7,380.00 USD | 14,620.00 USD |
| `7D` | `308.20` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD |
| `1D` | `308.60` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 5,200.00 USD | 185.69 USD | 3,480.00 USD |
| `7D` | `308.70` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD |
| `1D` | `309.00` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 8,460.00 USD | 6,010.00 USD | 3,530.00 USD |
| `7D` | `309.20` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD |
| `1D` | `309.40` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 6,810.00 USD | 4,770.00 USD | 796.24 USD |
| `7D` | `309.70` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD |
| `1D` | `309.80` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 10,880.00 USD | 5,410.00 USD | 3,030.00 USD |
| `1D` | `310.20` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 1,670.00 USD | 6,500.00 USD | 11,020.00 USD |
| `7D` | `310.20` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD |
| `1D` | `310.60` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD |
| `7D` | `310.70` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD |
| `1D` | `311.00` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 0.82 USD |
| `7D` | `311.20` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD |
| `1D` | `311.40` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 901.19 USD | 160.90 USD | 6.94 USD |
| `7D` | `311.70` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 65,050.00 USD | 11,430.00 USD | 25,590.00 USD |
| `1D` | `311.80` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 6,450.00 USD | 6,700.00 USD | 4,060.00 USD |
| `1D` | `312.20` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 244.00 USD | 4,260.00 USD | 9,550.00 USD |
| `7D` | `312.20` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 24,190.00 USD |
| `1D` | `312.60` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 19,840.00 USD | 5,440.00 USD | 12,590.00 USD |
| `7D` | `312.70` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 8,290.00 USD | 19,350.00 USD | 29,640.00 USD |
| `1D` | `313.00` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.96 USD |
| `7D` | `313.20` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD |
| `1D` | `313.40` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 7,160.00 USD | 11,520.00 USD | 2,580.00 USD |
| `7D` | `313.70` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD |
| `1D` | `313.80` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 239.05 USD | 0.00 USD |
| `1D` | `314.20` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.20` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD |
| `1D` | `314.60` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 4,240.00 USD | 3,720.00 USD | 8,330.00 USD |
| `7D` | `314.70` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `315.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 6,450.00 USD |
| `7D` | `315.20` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD |
| `1D` | `315.40` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 3,750.00 USD | 144.50 USD | 2.46 USD |
| `7D` | `315.70` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD |
| `1D` | `315.80` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 118.95 USD | 0.00 USD | 5,230.00 USD |
| `1D` | `316.20` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `316.20` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD |
| `1D` | `316.60` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 11,090.00 USD | 3,570.00 USD | 0.00 USD |
| `1D` | `316.70` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `316.70` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD |
| `7D` | `317.20` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD |
| `7D` | `317.70` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 620.15 USD | 721.55 USD | 67.28 USD |
| `7D` | `318.20` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 23,930.00 USD | 13,700.00 USD | 32,180.00 USD |
| `7D` | `318.70` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 11,230.00 USD | 44,600.00 USD | 37,810.00 USD |
| `7D` | `319.20` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 366.90 USD | 18,060.00 USD | 0.00 USD |
| `7D` | `319.70` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `7D` | `320.20` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.47M` | Total OI Tokens: `1,082,726.4 BCH`
  * 1h OI Change: `-0.37%` | 4h OI Change: `+5.36%` | 24h OI Change: `-1.61%`
  * Exchange Breakdown: Binance=`89.97M` | Bybit=`38.50M` | OKX=`23.99M` | Hyperliquid=`7.25M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.41K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0074%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0061%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `58.62%` | `41.38%` | `1.42` | 2,460,000.00 USD |
| `15M` | `Binance` | `54.21%` | `45.79%` | `1.18` | 759,780.00 USD |
| `15M` | `OKX` | `60.28%` | `39.72%` | `1.52` | 311,120.00 USD |
| `15M` | `Bybit` | `59.34%` | `40.66%` | `1.46` | 252,060.00 USD |
| `15M` | `KuCoin` | `46.13%` | `53.87%` | `0.86` | 24,650.00 USD |
| `15M` | `Gate` | `64.44%` | `35.56%` | `1.81` | 177,320.00 USD |
| `15M` | `Bitget` | `94.09%` | `5.91%` | `15.92` | 109,720.00 USD |
| `15M` | `BingX` | `42.27%` | `57.73%` | `0.73` | 514,100.00 USD |
| `15M` | `MEXC` | `62.55%` | `37.45%` | `1.67` | 37,610.00 USD |
| `15M` | `Bitunix` | `79.54%` | `20.46%` | `3.89` | 70,960.00 USD |
| `15M` | `Hyperliquid` | `75.47%` | `24.53%` | `3.08` | 13,010.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `70.11%` | `29.89%` | `2.35` | 96,780.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.81%` | `1.19%` | `83.03` | 88,910.00 USD |
| `15M` | `HTX` | `19.53%` | `80.47%` | `0.24` | 4,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 609.70 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `93.93%` | `6.07%` | `15.47` | 1,200.00 USD |
| `15M` | `Whale Positions` | `54.21%` | `45.79%` | `1.18` | 759,780.00 USD |
| `15M` | `Global Accounts` | `58.62%` | `41.38%` | `1.42` | 2,460,000.00 USD |
| `1H` | `BCH` | `45.65%` | `54.35%` | `0.84` | 14,970,000.00 USD |
| `1H` | `Binance` | `47.63%` | `52.37%` | `0.91` | 5,170,000.00 USD |
| `1H` | `OKX` | `47.65%` | `52.35%` | `0.91` | 3,380,000.00 USD |
| `1H` | `Bybit` | `57.83%` | `42.17%` | `1.37` | 1,240,000.00 USD |
| `1H` | `KuCoin` | `51.34%` | `48.66%` | `1.06` | 623,890.00 USD |
| `1H` | `Gate` | `50.6%` | `49.4%` | `1.02` | 257,360.00 USD |
| `1H` | `Bitget` | `33.12%` | `66.88%` | `0.50` | 306,860.00 USD |
| `1H` | `BingX` | `16.69%` | `83.31%` | `0.20` | 596,480.00 USD |
| `1H` | `MEXC` | `59.54%` | `40.46%` | `1.47` | 260,180.00 USD |
| `1H` | `Bitunix` | `28.99%` | `71.01%` | `0.41` | 357,550.00 USD |
| `1H` | `Hyperliquid` | `59.56%` | `40.44%` | `1.47` | 68,860.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `45.49%` | `54.51%` | `0.83` | 2,250,000.00 USD |
| `1H` | `Crypto.com` | `96.54%` | `3.46%` | `27.90` | 984.82 USD |
| `1H` | `WhiteBIT` | `11.5%` | `88.5%` | `0.13` | 409,480.00 USD |
| `1H` | `HTX` | `8.16%` | `91.84%` | `0.09` | 26,980.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `85.63%` | `14.37%` | `5.96` | 21,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `24.03%` | `75.97%` | `0.32` | 1,680.00 USD |
| `1H` | `Whale Positions` | `47.63%` | `52.37%` | `0.91` | 5,170,000.00 USD |
| `1H` | `Global Accounts` | `45.65%` | `54.35%` | `0.84` | 14,970,000.00 USD |
| `4H` | `BCH` | `48.89%` | `51.11%` | `0.96` | 57,080,000.00 USD |
| `4H` | `Binance` | `46.43%` | `53.57%` | `0.87` | 18,550,000.00 USD |
| `4H` | `OKX` | `47.72%` | `52.28%` | `0.91` | 7,590,000.00 USD |
| `4H` | `Bybit` | `53.69%` | `46.31%` | `1.16` | 4,640,000.00 USD |
| `4H` | `KuCoin` | `46.93%` | `53.07%` | `0.88` | 490,470.00 USD |
| `4H` | `Gate` | `48.14%` | `51.86%` | `0.93` | 4,760,000.00 USD |
| `4H` | `Bitget` | `56.52%` | `43.48%` | `1.30` | 1,970,000.00 USD |
| `4H` | `BingX` | `40.86%` | `59.14%` | `0.69` | 9,820,000.00 USD |
| `4H` | `MEXC` | `52.57%` | `47.43%` | `1.11` | 2,620,000.00 USD |
| `4H` | `Bitunix` | `54.71%` | `45.29%` | `1.21` | 1,710,000.00 USD |
| `4H` | `Hyperliquid` | `49.13%` | `50.87%` | `0.97` | 1,210,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.89%` | `49.11%` | `1.04` | 1,800,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.15%` | `3.85%` | `24.97` | 1,570,000.00 USD |
| `4H` | `HTX` | `52.45%` | `47.55%` | `1.10` | 109,960.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.78%` | `49.22%` | `1.03` | 51,540.00 USD |
| `4H` | `Aster` | `64.24%` | `35.76%` | `1.80` | 142,700.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `71.47%` | `28.53%` | `2.51` | 22,710.00 USD |
| `4H` | `Whale Positions` | `46.43%` | `53.57%` | `0.87` | 18,550,000.00 USD |
| `4H` | `Global Accounts` | `48.89%` | `51.11%` | `0.96` | 57,080,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `278.95` | `278.11` | `278.95` | `279.11` | `276.01` | 1,117,022.83 USD | 460,337.30 USD | 656,685.53 USD | -196,348.23 USD | `-17.58%` | `14B / 26S` |
| `5:00 UTC` | `278.75` | `278.95` | `278.75` | `279.99` | `277.87` | 899,043.00 USD | 507,720.36 USD | 391,322.65 USD | 116,397.71 USD | `+12.95%` | `23B / 14S` |
| `0:00 UTC` | `281.80` | `281.23` | `281.80` | `282.56` | `279.38` | 1,860,973.61 USD | 1,019,031.48 USD | 841,942.13 USD | 177,089.35 USD | `+9.52%` | `29B / 17S` |
| `5:00 UTC` | `282.40` | `283.39` | `282.40` | `284.76` | `281.82` | 2,261,635.40 USD | 1,044,285.27 USD | 1,217,350.14 USD | -173,064.87 USD | `-7.65%` | `26B / 23S` |
| `0:00 UTC` | `287.03` | `284.86` | `287.03` | `287.15` | `282.35` | 3,497,591.91 USD | 1,841,198.98 USD | 1,656,392.94 USD | 184,806.04 USD | `+5.28%` | `24B / 10S` |
| `5:00 UTC` | `284.49` | `285.18` | `284.49` | `286.67` | `284.13` | 976,529.89 USD | 414,772.25 USD | 561,757.64 USD | -146,985.38 USD | `-15.05%` | `8B / 33S` |
| `0:00 UTC` | `284.00` | `284.42` | `284.00` | `285.15` | `283.77` | 825,459.63 USD | 394,600.86 USD | 430,858.77 USD | -36,257.91 USD | `-4.39%` | `20B / 24S` |
| `5:00 UTC` | `284.75` | `284.10` | `284.75` | `284.97` | `283.36` | 1,321,321.21 USD | 645,681.70 USD | 675,639.51 USD | -29,957.81 USD | `-2.27%` | `33B / 48S` |
| `0:00 UTC` | `284.87` | `284.37` | `284.87` | `285.61` | `283.47` | 932,067.73 USD | 549,811.25 USD | 382,256.48 USD | 167,554.77 USD | `+17.98%` | `21B / 18S` |
| `5:00 UTC` | `284.12` | `284.11` | `284.12` | `284.32` | `283.92` | 177,649.14 USD | 103,804.92 USD | 73,844.22 USD | 29,960.70 USD | `+16.87%` | `7B / 7S` |

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
| `5m` | 31,360.00 USD | -95,180.00 USD | **`DISTRIBUTION`** |
| `15m` | 98,090.00 USD | 367,680.00 USD | **`ACCUMULATION`** |
| `30m` | 47,070.00 USD | 371,310.00 USD | **`ACCUMULATION`** |
| `1h` | 306,590.00 USD | -25,340.00 USD | **`ACCUMULATION`** |
| `2h` | 672,740.00 USD | 158,260.00 USD | **`ACCUMULATION`** |
| `4h` | 1,210,000.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `6h` | 262,260.00 USD | -307,140.00 USD | **`DISTRIBUTION`** |
| `8h` | 759,180.00 USD | -2,190,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -217,110.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 47,300.00 USD | -4,870,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -1,080,000.00 USD | -14,860,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,300,000.00 USD | -137,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+31.36K` | 15m=`+98.09K` | 1h=`+306.59K` | 24h=`+47.30K`
* Futures Capital Netflows: 5m=`-95.18K` | 15m=`+367.68K` | 1h=`-25.34K` | 24h=`-4.87M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `268.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `264.53` (Risk Distance: `4.43` pts)
  * +2.5R Take Profit: `280.05`
  * Mathematical Lot Sizing: **`2.25 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `283.18` (Risk Distance: `4.43` pts)
  * +2.5R Take Profit: `267.66`
  * Mathematical Lot Sizing: **`2.25 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`286.02`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
