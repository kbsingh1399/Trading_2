# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 04:31:59 IST` (`2026-10-29 23:01:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `276.96` | **Live Ask Quote**: `277.54` | **Mid Price**: `277.25`
- **Spread Points**: `580.00` | **Spread BPS**: `20.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `277.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `279.19` | Lower -3.00σ Band: `275.31`
  * Upper +2.51σ Band: `278.77` | Lower -2.51σ Band: `275.73`
  * Upper +2.01σ Band: `278.41` | Lower -2.01σ Band: `276.09`
  * Upper +2.00σ Band: `278.36` | Lower -2.00σ Band: `276.14`
  * Upper +1.28σ Band: `278.03` | Lower -1.28σ Band: `276.47`
  * Upper +1.00σ Band: `277.80` | Lower -1.00σ Band: `276.70`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`277.25` | EMA-20=`277.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`277.25` (Slope: `+0.0000`) | EMA-100=`277.25`
  * Institutional Anchors: EMA-144=`277.25` | EMA-200=`277.25` (Slope: `+0.0000`) | EMA-233=`277.25`
- **Range Boundaries**: 24H High=`280.02` | 24H Low=`274.48` | Weekly High=`282.80` | Weekly Low=`271.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.58` (Distance: `-0.44%`)
  * Point of Control (POC) = `276.81` (Distance: `+0.20%`)
  * Value Area Low (VAL) = `274.73` (Distance: `+0.95%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.04` | Weekly POC=`278.88` | Weekly VAL=`274.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`279.40` | Low=`270.25`
  * London Session (08:00-16:00 UTC): High=`278.36` | Low=`276.14`
  * New York Session (13:00-21:00 UTC): High=`278.91` | Low=`275.59`
  * Initial Balance (First Hour): IB High=`278.08` | IB Low=`276.42`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `276.14` - `278.36`
  * Optimal Trade Entry (OTE 0.705): `277.80`
  * Structural Invalidation Anchor (0.786): `279.47`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `277.69` | `278.31` | `277.02` | `278.04` | `1,723` | 478,449.33 USD | -126,048.90 USD | `-26.35%` | -3,348,414.73 USD | `-0.57` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `278.07` | `278.45` | `277.43` | `277.44` | `1,424` | 396,075.51 USD | -323.64 USD | `-0.08%` | -3,348,738.37 USD | `-0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `277.44` | `278.65` | `277.00` | `278.60` | `1,619` | 450,041.99 USD | -42,514.84 USD | `-9.45%` | -3,391,253.20 USD | `-0.28` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `276.48` | `279.16` | `273.98` | `277.23` | `15,481` | 4,286,596.03 USD | 616,115.23 USD | `+14.37%` | -3,221,955.11 USD | `+1.87` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `277.21` | `278.57` | `275.92` | `277.44` | `5,434` | 1,507,866.81 USD | -219,786.61 USD | `-14.58%` | -3,441,741.72 USD | `-0.81` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `277.44` | `278.65` | `277.00` | `278.60` | `1,619` | 450,041.99 USD | -42,514.84 USD | `-9.45%` | -3,484,256.56 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `286.78` | `286.91` | `269.28` | `270.43` | `78,753` | 21,848,832.22 USD | -393,290.27 USD | `-1.80%` | -3,940,771.41 USD | `-0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `270.43` | `280.00` | `269.74` | `276.50` | `41,918` | 11,558,813.69 USD | 153,675.96 USD | `+1.33%` | -3,787,095.44 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `276.48` | `279.16` | `273.98` | `278.60` | `22,533` | 6,244,504.83 USD | 353,813.78 USD | `+5.67%` | -3,433,281.66 USD | `+0.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `278.53` | `143,202` | 39,651,365.75 USD | 113,414.49 USD | `+0.29%` | -3,296,843.30 USD | `+0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `278.53` | `143,202` | 39,651,365.75 USD | 113,414.49 USD | `+0.29%` | -3,296,843.30 USD | `+0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`277.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1982` | `0x12d2...f97f` | `LONG` | 1,008,228.46 USD | `3,627,243,000,000.00` | `303.26` | `277.77` | `0.000000` | -91,770.87 USD | `-9.10%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `293.56` | 7,191.63 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 7.19K USD at 293.5600 USD [API] | `2026-10-28 14:18:38` |
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
| `7D` | `Long Liquidation` | `240.40` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 20.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.90` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 330.05 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.40` | 12,350,000.00 USD | 12,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 88,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 12,340,000.00 USD | 12,340,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 12,320,000.00 USD | 12,320,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 88,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.90` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.40` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 86,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `243.70` | 4,730,000.00 USD | 4,730,000.00 USD | 583.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.90` | 12,240,000.00 USD | 12,240,000.00 USD | 781.30 USD | 0.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `244.10` | 4,730,000.00 USD | 4,730,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.40` | 12,220,000.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 4.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `244.50` | 4,730,000.00 USD | 4,730,000.00 USD | 638.70 USD | 5,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 28,760.00 USD | 85,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `244.90` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.90` | 12,220,000.00 USD | 12,220,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `245.30` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.40` | 12,200,000.00 USD | 12,200,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 56,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.90` | 12,180,000.00 USD | 12,180,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.10` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 13.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 12,160,000.00 USD | 12,160,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.50` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.90` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.90` | 12,130,000.00 USD | 12,130,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.30` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 3,690.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.40` | 12,120,000.00 USD | 12,120,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 55,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.70` | 4,690,000.00 USD | 4,690,000.00 USD | 528.00 USD | 619.60 USD | 5.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.90` | 12,080,000.00 USD | 12,080,000.00 USD | 789.37 USD | 4,610.00 USD | 33.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.10` | 4,690,000.00 USD | 4,690,000.00 USD | 10,640.00 USD | 1,390.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 12,070,000.00 USD | 12,070,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.50` | 4,650,000.00 USD | 4,650,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.90` | 4,640,000.00 USD | 4,640,000.00 USD | 3,780.00 USD | 4,920.00 USD | 26,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 12,030,000.00 USD | 12,030,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.30` | 4,600,000.00 USD | 4,600,000.00 USD | 182.40 USD | 6,140.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.40` | 11,930,000.00 USD | 11,930,000.00 USD | 49,060.00 USD | 28,020.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.70` | 4,590,000.00 USD | 4,590,000.00 USD | 13,940.00 USD | 6.43 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 11,850,000.00 USD | 11,850,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.10` | 4,570,000.00 USD | 4,570,000.00 USD | 9,650.00 USD | 4,330.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 11,740,000.00 USD | 11,740,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.50` | 4,550,000.00 USD | 4,550,000.00 USD | 4,210.00 USD | 2,450.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 54,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.90` | 4,540,000.00 USD | 4,540,000.00 USD | 7,630.00 USD | 24,810.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.90` | 11,670,000.00 USD | 11,670,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,500,000.00 USD | 4,500,000.00 USD | 32,730.00 USD | 41,780.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 11,580,000.00 USD | 11,580,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 53,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,410,000.00 USD | 4,410,000.00 USD | 35,310.00 USD | 46,850.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 11,410,000.00 USD | 11,410,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,310,000.00 USD | 4,310,000.00 USD | 25,540.00 USD | 11,300.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 11,240,000.00 USD | 11,240,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,250,000.00 USD | 4,250,000.00 USD | 10,840.00 USD | 3,450.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 53,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,230,000.00 USD | 4,230,000.00 USD | 12,160.00 USD | 6,450.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 11,100,000.00 USD | 11,100,000.00 USD | 29,220.00 USD | 19,580.00 USD | 45.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,210,000.00 USD | 4,210,000.00 USD | 17,170.00 USD | 22,810.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 11,050,000.00 USD | 11,050,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,160,000.00 USD | 4,160,000.00 USD | 8,120.00 USD | 8,990.00 USD | 11,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 10,930,000.00 USD | 10,930,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,130,000.00 USD | 4,130,000.00 USD | 144.00 USD | 4,520.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 10,860,000.00 USD | 10,860,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,130,000.00 USD | 4,130,000.00 USD | 134.35 USD | 2,050.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 52,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,120,000.00 USD | 4,120,000.00 USD | 7,730.00 USD | 6,590.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 10,780,000.00 USD | 10,780,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,110,000.00 USD | 4,110,000.00 USD | 3,050.00 USD | 890.20 USD | 11.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 10,730,000.00 USD | 10,730,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,100,000.00 USD | 4,100,000.00 USD | 8,470.00 USD | 7,440.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 10,650,000.00 USD | 10,650,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,080,000.00 USD | 4,080,000.00 USD | 16,160.00 USD | 2,260.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 10,580,000.00 USD | 10,580,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,070,000.00 USD | 4,070,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 453.49 USD | 51,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,050,000.00 USD | 4,050,000.00 USD | 5,560.00 USD | 928.93 USD | 8.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 10,450,000.00 USD | 10,450,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,040,000.00 USD | 4,040,000.00 USD | 5,410.00 USD | 68.55 USD | 11,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 10,360,000.00 USD | 10,360,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 51,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,030,000.00 USD | 4,030,000.00 USD | 886.80 USD | 531.60 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 10,280,000.00 USD | 10,280,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,020,000.00 USD | 4,020,000.00 USD | 5,060.00 USD | 2,620.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 10,220,000.00 USD | 10,220,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,010,000.00 USD | 4,010,000.00 USD | 3,640.00 USD | 3,040.00 USD | 2.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 51,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,000,000.00 USD | 4,000,000.00 USD | 181.55 USD | 6,940.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 10,000,000.00 USD | 10,000,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 3,990,000.00 USD | 3,990,000.00 USD | 15,810.00 USD | 713.90 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 9,900,000.00 USD | 9,900,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `259.50` | 5,190.00 USD | 50,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `259.70` | 3,960,000.00 USD | 3,960,000.00 USD | 10,100.00 USD | 13,590.00 USD | 24,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 9,840,000.00 USD | 9,840,000.00 USD | 19,140.00 USD | 12,520.00 USD | 113.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 3,910,000.00 USD | 3,910,000.00 USD | 8,200.00 USD | 14,680.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 9,810,000.00 USD | 9,810,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,880,000.00 USD | 3,880,000.00 USD | 2,460.00 USD | 4,730.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 7,590.00 USD | 45,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,870,000.00 USD | 3,870,000.00 USD | 8,070.00 USD | 16,080.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 9,690,000.00 USD | 9,690,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,830,000.00 USD | 3,830,000.00 USD | 7,780.00 USD | 18,050.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 9,570,000.00 USD | 9,570,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,770,000.00 USD | 3,770,000.00 USD | 4,600.00 USD | 1,290.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 9,470,000.00 USD | 9,470,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,750,000.00 USD | 3,750,000.00 USD | 517.32 USD | 4,700.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 9,310,000.00 USD | 9,310,000.00 USD | 44,640.00 USD | 52,560.00 USD | 42.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,730,000.00 USD | 3,730,000.00 USD | 8,380.00 USD | 4,750.00 USD | 5.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,710,000.00 USD | 3,710,000.00 USD | 366.04 USD | 13,720.00 USD | 6.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 9,210,000.00 USD | 9,210,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,700,000.00 USD | 3,700,000.00 USD | 9,250.00 USD | 3,960.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 9,070,000.00 USD | 9,070,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,670,000.00 USD | 3,670,000.00 USD | 414.95 USD | 10,710.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 8,890,000.00 USD | 8,890,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,640,000.00 USD | 3,640,000.00 USD | 2,210.00 USD | 184.09 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 8,450,000.00 USD | 8,450,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,620,000.00 USD | 3,620,000.00 USD | 800.20 USD | 928.53 USD | 60,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 9,770.00 USD | 38,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,560,000.00 USD | 3,560,000.00 USD | 39,490.00 USD | 4,750.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 8,330,000.00 USD | 8,330,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,500,000.00 USD | 3,500,000.00 USD | 19,790.00 USD | 9,040.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 8,190,000.00 USD | 8,190,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 390.02 USD | 28,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 3,440,000.00 USD | 3,440,000.00 USD | 23,810.00 USD | 34,200.00 USD | 52,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 7,830,000.00 USD | 7,830,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 3,330,000.00 USD | 3,330,000.00 USD | 38,800.00 USD | 3,690.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 7,500,000.00 USD | 7,500,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 3,280,000.00 USD | 3,280,000.00 USD | 34,380.00 USD | 31,420.00 USD | 70,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 3,140,000.00 USD | 3,140,000.00 USD | 32,360.00 USD | 25,410.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 7,020,000.00 USD | 7,020,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 3,070,000.00 USD | 3,070,000.00 USD | 17,990.00 USD | 15,140.00 USD | 42,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 6,540,000.00 USD | 6,540,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 195.01 USD | 27,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 3,000,000.00 USD | 3,000,000.00 USD | 83,640.00 USD | 119,390.00 USD | 28,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 6,110,000.00 USD | 6,110,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,760,000.00 USD | 2,760,000.00 USD | 55,190.00 USD | 104,940.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 5,500,000.00 USD | 5,500,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,540,000.00 USD | 2,540,000.00 USD | 89,550.00 USD | 108,360.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 26,720.00 USD | 27,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,310,000.00 USD | 2,310,000.00 USD | 91,610.00 USD | 43,970.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 4,900,000.00 USD | 4,900,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,130,000.00 USD | 2,130,000.00 USD | 28,610.00 USD | 34,530.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 4,400,000.00 USD | 4,400,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 971.55 USD | 971.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,010,000.00 USD | 2,010,000.00 USD | 37,480.00 USD | 23,780.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 3,830,000.00 USD | 3,830,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 1,940,000.00 USD | 1,940,000.00 USD | 107,180.00 USD | 21,550.00 USD | 144,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 3,610,000.00 USD | 3,610,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 1,670,000.00 USD | 1,670,000.00 USD | 91,660.00 USD | 6,950.00 USD | 50,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 1,520,000.00 USD | 1,520,000.00 USD | 15,760.00 USD | 0.00 USD | 90,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 3,480,000.00 USD | 3,480,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 1,410,000.00 USD | 1,410,000.00 USD | 56,160.00 USD | 0.00 USD | 93,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 3,150,000.00 USD | 3,150,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 1,260,000.00 USD | 1,260,000.00 USD | 77,400.00 USD | 7,210.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 3,000,000.00 USD | 3,000,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 1,170,000.00 USD | 1,170,000.00 USD | 122,330.00 USD | 4,060.00 USD | 12.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 2,540,000.00 USD | 2,540,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 1,040,000.00 USD | 1,040,000.00 USD | 72,620.00 USD | 447.70 USD | 19,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 949,660.00 USD | 949,660.00 USD | 78,920.00 USD | 7,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 2,260,000.00 USD | 2,260,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 863,480.00 USD | 863,480.00 USD | 179,400.00 USD | 73.70 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 2,090,000.00 USD | 2,090,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 667,900.00 USD | 667,900.00 USD | 142,060.00 USD | 0.00 USD | 95,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 1,550,000.00 USD | 1,550,000.00 USD | 375,450.00 USD | 0.00 USD | 459.34 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 430,020.00 USD | 430,020.00 USD | 178,110.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 1,170,000.00 USD | 1,170,000.00 USD | 496,740.00 USD | 0.00 USD | 9.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 251,900.00 USD | 251,900.00 USD | 194,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 57,420.00 USD | 57,420.00 USD | 57,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 677,690.00 USD | 677,690.00 USD | 348,470.00 USD | 0.00 USD | 73.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.40` | 329,150.00 USD | 329,150.00 USD | 3,530.00 USD | 0.00 USD | 168.04 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `275.50` | 5,990.00 USD | 5,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `275.90` | 325,450.00 USD | 325,450.00 USD | 2,560.00 USD | 0.00 USD | 46.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 322,840.00 USD | 322,840.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `276.50` | 333.46 USD | 6,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `276.90` | 216,620.00 USD | 216,620.00 USD | 44,670.00 USD | 22,950.00 USD | 11.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 301.20 USD | 301.20 USD | 301.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.40` | 148,980.00 USD | 148,980.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 85,690.00 USD | 85,690.00 USD | 0.00 USD | 85,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.40` | 51,120.00 USD | 51,120.00 USD | 24,750.00 USD | 26,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.90` | 28,380.00 USD | 28,380.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 128,670.00 USD | 128,670.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.30` | 106,630.00 USD | 106,630.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.40` | 224,660.00 USD | 224,660.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.70` | 114,320.00 USD | 114,320.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.90` | 224,680.00 USD | 224,680.00 USD | 0.00 USD | 0.00 USD | 19.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.10` | 183,820.00 USD | 183,820.00 USD | 21,040.00 USD | 11,840.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.40` | 224,760.00 USD | 224,760.00 USD | 0.00 USD | 0.00 USD | 82.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.50` | 300,380.00 USD | 300,380.00 USD | 8,720.00 USD | 6,630.00 USD | 101,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.90` | 342,010.00 USD | 342,010.00 USD | 0.00 USD | 11,870.00 USD | 29,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.30` | 395,710.00 USD | 395,710.00 USD | 0.00 USD | 6,950.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 301,710.00 USD | 301,710.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.70` | 421,710.00 USD | 421,710.00 USD | 20,590.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.90` | 699,740.00 USD | 699,740.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 755,960.00 USD | 755,960.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.50` | 499,410.00 USD | 499,410.00 USD | 32,230.00 USD | 7,210.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.90` | 726,690.00 USD | 726,690.00 USD | 77,910.00 USD | 13,190.00 USD | 136,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.90` | 788,160.00 USD | 788,160.00 USD | 32,190.00 USD | 0.00 USD | 7.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.30` | 811,080.00 USD | 811,080.00 USD | 31,810.00 USD | 9,540.00 USD | 43,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 66,560.00 USD | 146,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.70` | 947,920.00 USD | 947,920.00 USD | 0.00 USD | 45,780.00 USD | 91,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.90` | 1,360,000.00 USD | 1,360,000.00 USD | 49,500.00 USD | 0.00 USD | 309,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.10` | 1,130,000.00 USD | 1,130,000.00 USD | 38,980.00 USD | 41,630.00 USD | 97,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 1,520,000.00 USD | 1,520,000.00 USD | 27,700.00 USD | 89,730.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.50` | 1,270,000.00 USD | 1,270,000.00 USD | 40,560.00 USD | 83,030.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 1,330,000.00 USD | 1,330,000.00 USD | 8,520.00 USD | 531.60 USD | 54,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 1,980,000.00 USD | 1,980,000.00 USD | 67,050.00 USD | 391,180.00 USD | 13.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 1,580,000.00 USD | 1,580,000.00 USD | 87,540.00 USD | 81,890.00 USD | 80,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 2,320,000.00 USD | 2,320,000.00 USD | 64,060.00 USD | 193,790.00 USD | 83,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 1,760,000.00 USD | 1,760,000.00 USD | 91,500.00 USD | 80,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 2,420,000.00 USD | 2,420,000.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 137,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 1,800,000.00 USD | 1,800,000.00 USD | 750.70 USD | 0.00 USD | 23,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 1,940,000.00 USD | 1,940,000.00 USD | 31,110.00 USD | 30,070.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 51,390.00 USD | 148,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 103,090.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 53,620.00 USD | 103,430.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.70` | 2,140,000.00 USD | 2,140,000.00 USD | 9,030.00 USD | 9,240.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 277,850.00 USD | 8.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 2,190,000.00 USD | 2,190,000.00 USD | 16,120.00 USD | 14,410.00 USD | 19,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.40` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 8.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 2,210,000.00 USD | 2,210,000.00 USD | 12,480.00 USD | 3,710.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 2,140.00 USD | 8,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.90` | 2,220,000.00 USD | 2,220,000.00 USD | 8,620.00 USD | 1,990.00 USD | 11.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 3,240,000.00 USD | 3,240,000.00 USD | 1,170.00 USD | 0.00 USD | 10.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 2,250,000.00 USD | 2,250,000.00 USD | 664.77 USD | 20,430.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 927.80 USD | 80.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 2,270,000.00 USD | 2,270,000.00 USD | 957.57 USD | 3,630.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 1,990.00 USD | 32.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 3,280,000.00 USD | 3,280,000.00 USD | 34,580.00 USD | 0.00 USD | 58.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 305.70 USD | 16,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 2,320,000.00 USD | 2,320,000.00 USD | 33,020.00 USD | 6,700.00 USD | 3.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 3,280,000.00 USD | 3,280,000.00 USD | 898.13 USD | 861.99 USD | 0.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 2,330,000.00 USD | 2,330,000.00 USD | 562.74 USD | 9,950.00 USD | 7.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 3,340,000.00 USD | 3,340,000.00 USD | 1,340.00 USD | 55,720.00 USD | 64.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 15,650.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 120,730.00 USD | 36.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 42,870.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 71,940.00 USD | 140.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 2,480,000.00 USD | 2,480,000.00 USD | 21,960.00 USD | 31,710.00 USD | 10.29 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 763.13 USD | 9,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,570,000.00 USD | 2,570,000.00 USD | 21,830.00 USD | 70,670.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 119,560.00 USD | 24.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,660,000.00 USD | 2,660,000.00 USD | 10,630.00 USD | 49,870.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 534.50 USD | 112,560.00 USD | 15.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,850,000.00 USD | 2,850,000.00 USD | 89,050.00 USD | 51,280.00 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 3,880,000.00 USD | 3,880,000.00 USD | 51,570.00 USD | 20,910.00 USD | 45,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,960,000.00 USD | 2,960,000.00 USD | 23,860.00 USD | 38,720.00 USD | 48,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 139,780.00 USD | 14,550.00 USD | 60,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 3,240,000.00 USD | 3,240,000.00 USD | 98,880.00 USD | 81,930.00 USD | 93,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 3,380,000.00 USD | 3,380,000.00 USD | 45,360.00 USD | 65,300.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 64,510.00 USD | 107,870.00 USD | 104,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 3,510,000.00 USD | 3,510,000.00 USD | 23,550.00 USD | 43,050.00 USD | 63,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 92,780.00 USD | 94,780.00 USD | 252,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,690,000.00 USD | 3,690,000.00 USD | 89,300.00 USD | 21,530.00 USD | 69,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 108,830.00 USD | 133,090.00 USD | 150,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,870,000.00 USD | 3,870,000.00 USD | 52,430.00 USD | 89,880.00 USD | 29,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 27,680.00 USD | 77,570.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,940,000.00 USD | 3,940,000.00 USD | 43,030.00 USD | 12,250.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 102.59 USD | 9,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `296.90` | 4,060,000.00 USD | 4,060,000.00 USD | 22,010.00 USD | 21,230.00 USD | 78,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 207,350.00 USD | 50,930.00 USD | 172,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 4,140,000.00 USD | 4,140,000.00 USD | 57,730.00 USD | 359.06 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 5,960,000.00 USD | 5,960,000.00 USD | 4,100.00 USD | 59,290.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 4,160,000.00 USD | 4,160,000.00 USD | 1,810.00 USD | 902.60 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 17,770.00 USD | 39,840.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 4,260,000.00 USD | 4,260,000.00 USD | 51,550.00 USD | 10,450.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 32,250.00 USD | 42,710.00 USD | 68,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,340,000.00 USD | 4,340,000.00 USD | 11,480.00 USD | 7,730.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,470,000.00 USD | 4,470,000.00 USD | 28,150.00 USD | 13,200.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 6,340,000.00 USD | 6,340,000.00 USD | 70,090.00 USD | 12,780.00 USD | 40,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,530,000.00 USD | 4,530,000.00 USD | 33,660.00 USD | 16,690.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 4,470.00 USD | 13,080.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 883.53 USD | 10,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,590,000.00 USD | 4,590,000.00 USD | 12,530.00 USD | 14,020.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 6,490,000.00 USD | 6,490,000.00 USD | 56,210.00 USD | 10,220.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,720,000.00 USD | 4,720,000.00 USD | 30,490.00 USD | 30,850.00 USD | 64,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 866.20 USD | 1,190.00 USD | 81.62 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,760,000.00 USD | 4,760,000.00 USD | 18,940.00 USD | 11,020.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,820,000.00 USD | 4,820,000.00 USD | 8,640.00 USD | 20,610.00 USD | 26,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 6,690,000.00 USD | 6,690,000.00 USD | 24,730.00 USD | 70,210.00 USD | 104,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,870,000.00 USD | 4,870,000.00 USD | 2,520.00 USD | 28,460.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 71,890.00 USD | 56,010.00 USD | 94,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,910,000.00 USD | 4,910,000.00 USD | 19,800.00 USD | 8,210.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 89,300.00 USD | 185,430.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,980,000.00 USD | 4,980,000.00 USD | 25,280.00 USD | 33,010.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 7,340,000.00 USD | 7,340,000.00 USD | 1,560.00 USD | 125,480.00 USD | 128.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 5,050,000.00 USD | 5,050,000.00 USD | 10,520.00 USD | 12,750.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 5,060,000.00 USD | 5,060,000.00 USD | 1,230.00 USD | 1,760.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 71,700.00 USD | 110,480.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 5,120,000.00 USD | 5,120,000.00 USD | 31,330.00 USD | 1,690.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 173.09 USD | 5.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 5,140,000.00 USD | 5,140,000.00 USD | 7,540.00 USD | 3,470.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 21,140.00 USD | 11,010.00 USD | 45,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 5,210,000.00 USD | 5,210,000.00 USD | 21,670.00 USD | 710.90 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 7,660,000.00 USD | 7,660,000.00 USD | 3,670.00 USD | 11,280.00 USD | 169.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 5,290,000.00 USD | 5,290,000.00 USD | 13,310.00 USD | 9,420.00 USD | 57,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 5,300,000.00 USD | 5,300,000.00 USD | 5,870.00 USD | 1,450.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 36,160.00 USD | 18,990.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 5,320,000.00 USD | 5,320,000.00 USD | 10,950.00 USD | 102.77 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 163,730.00 USD | 127,450.00 USD | 119,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 5,340,000.00 USD | 5,340,000.00 USD | 7,960.00 USD | 4,710.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 8,280,000.00 USD | 8,280,000.00 USD | 82,000.00 USD | 55,480.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 5,340,000.00 USD | 5,340,000.00 USD | 4,210.00 USD | 2,780.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 39,250.00 USD | 55,740.00 USD | 66,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 5,360,000.00 USD | 5,360,000.00 USD | 4,410.00 USD | 9,500.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,450,000.00 USD | 5,450,000.00 USD | 31,980.00 USD | 40,330.00 USD | 13,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 84,850.00 USD | 64,520.00 USD | 102,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,510,000.00 USD | 5,510,000.00 USD | 7,930.00 USD | 34,540.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 8,980,000.00 USD | 8,980,000.00 USD | 46,230.00 USD | 154,680.00 USD | 83,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 6,360.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,580,000.00 USD | 5,580,000.00 USD | 32,340.00 USD | 30,450.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 136,380.00 USD | 101,120.00 USD | 65,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,640,000.00 USD | 5,640,000.00 USD | 25,680.00 USD | 11,430.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 9,610,000.00 USD | 9,610,000.00 USD | 152,590.00 USD | 50,070.00 USD | 124,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,650,000.00 USD | 5,650,000.00 USD | 4,890.00 USD | 3,510.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,670,000.00 USD | 5,670,000.00 USD | 12,310.00 USD | 5,660.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 61,600.00 USD | 52,230.00 USD | 19,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 5,670,000.00 USD | 5,670,000.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 9,860,000.00 USD | 9,860,000.00 USD | 28,000.00 USD | 35,530.00 USD | 46,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 10,190,000.00 USD | 10,190,000.00 USD | 59,490.00 USD | 131,460.00 USD | 144,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 10,470,000.00 USD | 10,470,000.00 USD | 78,770.00 USD | 123,340.00 USD | 76,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 17,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `310.90` | 10,550,000.00 USD | 10,550,000.00 USD | 35,670.00 USD | 35,930.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.40` | 10,750,000.00 USD | 10,750,000.00 USD | 89,390.00 USD | 65,750.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 10,810,000.00 USD | 10,810,000.00 USD | 40,320.00 USD | 11,160.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 10,920,000.00 USD | 10,920,000.00 USD | 38,320.00 USD | 22,970.00 USD | 43,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 10,990,000.00 USD | 10,990,000.00 USD | 22,600.00 USD | 8,800.00 USD | 38,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.40` | 11,100,000.00 USD | 11,100,000.00 USD | 55,570.00 USD | 24,730.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 11,200,000.00 USD | 11,200,000.00 USD | 44,540.00 USD | 15,370.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 11,300,000.00 USD | 11,300,000.00 USD | 51,980.00 USD | 307.60 USD | 51,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 11,350,000.00 USD | 11,350,000.00 USD | 39,410.00 USD | 0.00 USD | 10,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.40` | 11,370,000.00 USD | 11,370,000.00 USD | 6,160.00 USD | 9,920.00 USD | 121.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 11,480,000.00 USD | 11,480,000.00 USD | 47,110.00 USD | 41,400.00 USD | 29,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 11,600,000.00 USD | 11,600,000.00 USD | 16,580.00 USD | 40,320.00 USD | 61,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 11,620,000.00 USD | 11,620,000.00 USD | 3,030.00 USD | 10,840.00 USD | 107.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.40` | 11,630,000.00 USD | 11,630,000.00 USD | 14,540.00 USD | 1,010.00 USD | 270.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 11,660,000.00 USD | 11,660,000.00 USD | 21,640.00 USD | 8,200.00 USD | 31.78 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 11,720,000.00 USD | 11,720,000.00 USD | 3,320.00 USD | 27,530.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 11,780,000.00 USD | 11,780,000.00 USD | 11,180.00 USD | 17,970.00 USD | 37,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.40` | 11,800,000.00 USD | 11,800,000.00 USD | 733.55 USD | 18,060.00 USD | 2.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 11,830,000.00 USD | 11,830,000.00 USD | 446.22 USD | 22,230.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 11,910,000.00 USD | 11,910,000.00 USD | 49,620.00 USD | 10,080.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 18,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 166.45 USD | 49.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.40` | 11,960,000.00 USD | 11,960,000.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 11,970,000.00 USD | 11,970,000.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 12,010,000.00 USD | 12,010,000.00 USD | 22,930.00 USD | 7,950.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 12,030,000.00 USD | 12,030,000.00 USD | 16,590.00 USD | 5,830.00 USD | 0.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.40` | 12,070,000.00 USD | 12,070,000.00 USD | 14,160.00 USD | 11,950.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.90` | 12,070,000.00 USD | 12,070,000.00 USD | 269.10 USD | 692.00 USD | 3.32 USD | `Tier 1 CEX` |
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
| `7D` | `240.90` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 0.00 USD | 330.05 USD | 4,570.00 USD |
| `7D` | `241.40` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `241.90` | 12,340,000.00 USD | 0.00 USD | 12,340,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.40` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD |
| `7D` | `242.90` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 0.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.40` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD |
| `1D` | `243.50` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 583.95 USD | 0.00 USD | 0.00 USD |
| `1D` | `243.90` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD |
| `7D` | `243.90` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 781.30 USD | 0.00 USD | 20,790.00 USD |
| `1D` | `244.70` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 638.70 USD | 5,270.00 USD | 12,330.00 USD |
| `7D` | `244.90` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD |
| `7D` | `245.40` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,880.00 USD |
| `1D` | `245.50` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 7,740.00 USD |
| `1D` | `245.90` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 6.81 USD |
| `7D` | `245.90` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD |
| `1D` | `246.30` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 5,540.00 USD | 6.30 USD |
| `7D` | `246.40` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD |
| `1D` | `246.70` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `7D` | `246.90` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,740.00 USD |
| `1D` | `247.10` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD |
| `7D` | `247.40` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,700.00 USD |
| `1D` | `247.50` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 1,330.00 USD | 7,240.00 USD |
| `1D` | `247.90` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 528.00 USD | 619.60 USD | 5.98 USD |
| `7D` | `247.90` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 789.37 USD | 4,610.00 USD | 3.04 USD |
| `1D` | `248.30` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 10,640.00 USD | 1,390.00 USD | 30,250.00 USD |
| `7D` | `248.40` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,880.00 USD |
| `1D` | `248.70` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 7,480.00 USD | 3,350.00 USD | 0.00 USD |
| `7D` | `248.90` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 37,420.00 USD | 24,350.00 USD | 32,250.00 USD |
| `1D` | `249.10` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 3,780.00 USD | 9,520.00 USD | 31,010.00 USD |
| `7D` | `249.40` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 49,060.00 USD | 28,020.00 USD | 4,010.00 USD |
| `1D` | `249.50` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 5,170.00 USD | 1,450.00 USD | 2,030.00 USD |
| `1D` | `249.90` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 13,540.00 USD | 1,330.00 USD | 3,490.00 USD |
| `7D` | `249.90` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,200.00 USD |
| `1D` | `250.30` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 9,170.00 USD | 5,500.00 USD | 5,870.00 USD |
| `7D` | `250.40` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,470.00 USD |
| `1D` | `250.70` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 3,680.00 USD | 9,520.00 USD | 7,010.00 USD |
| `7D` | `250.90` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD |
| `1D` | `251.10` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 31,920.00 USD | 39,990.00 USD | 13,050.00 USD |
| `7D` | `251.40` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,200.00 USD |
| `1D` | `251.50` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 7,900.00 USD | 34,360.00 USD | 17,710.00 USD |
| `1D` | `251.90` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 49,120.00 USD | 36,870.00 USD | 24,600.00 USD |
| `7D` | `251.90` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD |
| `1D` | `252.30` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 13,370.00 USD | 7,400.00 USD | 5,650.00 USD |
| `7D` | `252.40` | 11,240,000.00 USD | 0.00 USD | 11,240,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,130.00 USD |
| `1D` | `252.70` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 14,040.00 USD | 5,720.00 USD | 4,140.00 USD |
| `7D` | `252.90` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 29,220.00 USD | 19,580.00 USD | 22.93 USD |
| `1D` | `253.10` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 9,570.00 USD | 12,280.00 USD | 2,320.00 USD |
| `7D` | `253.40` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD |
| `1D` | `253.50` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 19,980.00 USD | 13,820.00 USD | 14,520.00 USD |
| `1D` | `253.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 8,890.00 USD | 9,560.00 USD |
| `7D` | `253.90` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,940.00 USD |
| `1D` | `254.30` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 144.00 USD | 2,130.00 USD | 3.80 USD |
| `7D` | `254.40` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,860.00 USD |
| `1D` | `254.70` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 994.06 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `254.90` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD |
| `1D` | `255.10` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 9,680.00 USD | 6,590.00 USD | 19.66 USD |
| `7D` | `255.40` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,820.00 USD |
| `1D` | `255.50` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 6,410.00 USD | 6,180.00 USD | 2,760.00 USD |
| `1D` | `255.90` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 13,380.00 USD | 2,480.00 USD | 3.61 USD |
| `7D` | `255.90` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,120.00 USD |
| `1D` | `256.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `256.40` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,420.00 USD |
| `1D` | `256.70` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 9,140.00 USD | 0.00 USD | 8.97 USD |
| `7D` | `256.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,960.00 USD |
| `1D` | `257.10` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 5,380.00 USD | 928.93 USD | 3,430.00 USD |
| `7D` | `257.40` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,290.00 USD |
| `1D` | `257.50` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 918.80 USD | 600.15 USD | 8,330.00 USD |
| `1D` | `257.90` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 3,330.00 USD | 2,390.00 USD | 6,450.00 USD |
| `7D` | `257.90` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,230.00 USD |
| `1D` | `258.30` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 3,380.00 USD | 3,270.00 USD | 5,230.00 USD |
| `7D` | `258.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,530.00 USD |
| `1D` | `258.70` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 2,360.00 USD | 3,080.00 USD | 5,590.00 USD |
| `7D` | `258.90` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,410.00 USD |
| `1D` | `259.10` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 13,030.00 USD | 4,500.00 USD | 7,670.00 USD |
| `7D` | `259.40` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,100.00 USD |
| `1D` | `259.50` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 5,110.00 USD | 2,610.00 USD | 7,180.00 USD |
| `1D` | `259.90` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 15,160.00 USD | 15,630.00 USD | 17,070.00 USD |
| `7D` | `259.90` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 19,140.00 USD | 12,520.00 USD | 119.41 USD |
| `1D` | `260.30` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 3,050.00 USD | 12,260.00 USD | 7,690.00 USD |
| `7D` | `260.40` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,170.00 USD |
| `1D` | `260.70` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 338.15 USD | 5,500.00 USD | 17,340.00 USD |
| `7D` | `260.90` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,920.00 USD |
| `1D` | `261.10` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 8,020.00 USD | 16,510.00 USD | 37,510.00 USD |
| `7D` | `261.40` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,490.00 USD |
| `1D` | `261.50` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 7,870.00 USD | 16,090.00 USD | 18.60 USD |
| `1D` | `261.90` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 4,770.00 USD | 4,240.00 USD | 27,700.00 USD |
| `7D` | `261.90` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,280.00 USD |
| `1D` | `262.30` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 8,640.00 USD | 4,380.00 USD | 5,590.00 USD |
| `7D` | `262.40` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 44,640.00 USD | 52,560.00 USD | 24.61 USD |
| `1D` | `262.70` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 366.04 USD | 13,770.00 USD | 12.23 USD |
| `7D` | `262.90` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,780.00 USD |
| `1D` | `263.10` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 9,030.00 USD | 4,720.00 USD | 7,500.00 USD |
| `7D` | `263.40` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,020.00 USD |
| `1D` | `263.50` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 913.24 USD | 979.31 USD | 24,820.00 USD |
| `1D` | `263.90` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 746.44 USD | 10,060.00 USD | 18,120.00 USD |
| `7D` | `263.90` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,860.00 USD |
| `1D` | `264.30` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 1,860.00 USD | 843.43 USD | 16.64 USD |
| `7D` | `264.40` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,190.00 USD |
| `1D` | `264.70` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 28,300.00 USD | 4,090.00 USD | 59,990.00 USD |
| `7D` | `264.90` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,220.00 USD |
| `1D` | `265.10` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 31,390.00 USD | 9,550.00 USD | 15,630.00 USD |
| `7D` | `265.40` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 134,720.00 USD | 49,150.00 USD | 182,820.00 USD |
| `1D` | `265.50` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 9,760.00 USD | 22,630.00 USD | 67,100.00 USD |
| `1D` | `265.90` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 30,220.00 USD | 15,460.00 USD | 19,150.00 USD |
| `7D` | `265.90` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,740.00 USD |
| `1D` | `266.30` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 45,330.00 USD | 26,490.00 USD | 10,080.00 USD |
| `7D` | `266.40` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,690.00 USD |
| `1D` | `266.70` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 21,690.00 USD | 16,380.00 USD | 65,380.00 USD |
| `7D` | `266.90` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,370.00 USD |
| `1D` | `267.10` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 28,570.00 USD | 14,480.00 USD | 58,670.00 USD |
| `7D` | `267.40` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,460.00 USD |
| `1D` | `267.50` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 12,110.00 USD | 30,400.00 USD | 14,180.00 USD |
| `1D` | `267.90` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 113,020.00 USD | 128,050.00 USD | 45,340.00 USD |
| `7D` | `267.90` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,230.00 USD |
| `1D` | `268.30` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 71,550.00 USD | 129,780.00 USD | 43,490.00 USD |
| `7D` | `268.40` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,620.00 USD |
| `1D` | `268.70` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 97,080.00 USD | 92,740.00 USD | 58,760.00 USD |
| `7D` | `268.90` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 261,830.00 USD | 135,480.00 USD | 104,100.00 USD |
| `1D` | `269.10` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 49,680.00 USD | 34,630.00 USD | 16,360.00 USD |
| `7D` | `269.40` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,060.00 USD |
| `1D` | `269.50` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 30,680.00 USD | 12,730.00 USD | 44,920.00 USD |
| `1D` | `269.90` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 32,430.00 USD | 42,870.00 USD | 12,980.00 USD |
| `7D` | `269.90` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD |
| `1D` | `270.30` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 117,910.00 USD | 6,950.00 USD | 175,670.00 USD |
| `7D` | `270.40` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD |
| `1D` | `270.70` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 76,780.00 USD | 0.00 USD | 28,980.00 USD |
| `7D` | `270.90` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 328,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.10` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 39,410.00 USD | 0.00 USD | 149,680.00 USD |
| `7D` | `271.40` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.50` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 60,220.00 USD | 7,210.00 USD | 20,880.00 USD |
| `1D` | `271.90` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 118,720.00 USD | 0.00 USD | 10,140.00 USD |
| `7D` | `271.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.30` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 79,160.00 USD | 4,430.00 USD | 19,720.00 USD |
| `7D` | `272.40` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.70` | 991,990.00 USD | 0.00 USD | 991,990.00 USD | 66,860.00 USD | 3,620.00 USD | 8.40 USD |
| `7D` | `272.90` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD |
| `1D` | `273.10` | 921,500.00 USD | 0.00 USD | 921,500.00 USD | 89,210.00 USD | 3,790.00 USD | 0.00 USD |
| `7D` | `273.40` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD |
| `1D` | `273.50` | 828,500.00 USD | 0.00 USD | 828,500.00 USD | 224,710.00 USD | 0.00 USD | 78,000.00 USD |
| `1D` | `273.90` | 525,790.00 USD | 0.00 USD | 525,790.00 USD | 152,940.00 USD | 0.00 USD | 33,930.00 USD |
| `7D` | `273.90` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 375,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.30` | 338,920.00 USD | 0.00 USD | 338,920.00 USD | 204,080.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `274.40` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 496,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.70` | 134,840.00 USD | 0.00 USD | 134,840.00 USD | 100,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 677,870.00 USD | 0.00 USD | 677,870.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `275.10` | 34,230.00 USD | 0.00 USD | 34,230.00 USD | 33,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.40` | 329,400.00 USD | 0.00 USD | 329,400.00 USD | 3,530.00 USD | 0.00 USD | 110.28 USD |
| `7D` | `275.90` | 325,760.00 USD | 0.00 USD | 325,760.00 USD | 2,560.00 USD | 0.00 USD | 99.71 USD |
| `7D` | `276.40` | 323,100.00 USD | 0.00 USD | 323,100.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD |
| `7D` | `276.90` | 216,870.00 USD | 0.00 USD | 216,870.00 USD | 44,670.00 USD | 22,950.00 USD | 10.77 USD |
| `7D` | `277.40` | 149,240.00 USD | 0.00 USD | 149,240.00 USD | 0.00 USD | 63,290.00 USD | 90.83 USD |
| `1D` | `277.50` | 301.20 USD | 0.00 USD | 301.20 USD | 301.20 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.90` | 85,860.00 USD | 0.00 USD | 85,860.00 USD | 0.00 USD | 85,690.00 USD | 163.45 USD |
| `7D` | `278.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `278.40` | 51,190.00 USD | 51,190.00 USD | 0.00 USD | 24,750.00 USD | 26,370.00 USD | 73.93 USD |
| `1D` | `278.70` | 24,120.00 USD | 24,120.00 USD | 0.00 USD | 19,830.00 USD | 4,280.00 USD | 0.00 USD |
| `7D` | `278.90` | 128,750.00 USD | 128,750.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 0.00 USD |
| `1D` | `279.10` | 78,250.00 USD | 78,250.00 USD | 0.00 USD | 29,260.00 USD | 24,870.00 USD | 0.00 USD |
| `7D` | `279.40` | 224,730.00 USD | 224,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD |
| `1D` | `279.50` | 106,630.00 USD | 106,630.00 USD | 0.00 USD | 28,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.90` | 131,430.00 USD | 131,430.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 17,110.00 USD |
| `1D` | `280.30` | 257,500.00 USD | 257,500.00 USD | 0.00 USD | 29,750.00 USD | 18,470.00 USD | 77,850.00 USD |
| `1D` | `280.70` | 342,010.00 USD | 342,010.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD |
| `1D` | `281.10` | 388,770.00 USD | 388,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD |
| `7D` | `281.40` | 301,680.00 USD | 301,680.00 USD | 0.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD |
| `1D` | `281.50` | 416,300.00 USD | 416,300.00 USD | 0.00 USD | 20,590.00 USD | 6,950.00 USD | 0.00 USD |
| `1D` | `281.90` | 421,710.00 USD | 421,710.00 USD | 0.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.90` | 699,710.00 USD | 699,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 398,030.00 USD |
| `1D` | `282.30` | 459,970.00 USD | 459,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,250.00 USD |
| `7D` | `282.40` | 755,930.00 USD | 755,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD |
| `1D` | `282.70` | 547,670.00 USD | 547,670.00 USD | 0.00 USD | 57,180.00 USD | 20,400.00 USD | 10,130.00 USD |
| `7D` | `282.90` | 788,130.00 USD | 788,130.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.10` | 788,970.00 USD | 788,970.00 USD | 0.00 USD | 71,390.00 USD | 9,540.00 USD | 160,370.00 USD |
| `7D` | `283.40` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 146,510.00 USD |
| `1D` | `283.50` | 917,440.00 USD | 917,440.00 USD | 0.00 USD | 13,380.00 USD | 15,300.00 USD | 99,790.00 USD |
| `1D` | `283.90` | 990,250.00 USD | 990,250.00 USD | 0.00 USD | 0.00 USD | 34,020.00 USD | 38,790.00 USD |
| `7D` | `283.90` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD |
| `1D` | `284.30` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 38,980.00 USD | 54,150.00 USD | 59,180.00 USD |
| `7D` | `284.40` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 27,700.00 USD | 89,730.00 USD | 42,840.00 USD |
| `1D` | `284.70` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 49,080.00 USD | 67,500.00 USD | 20,690.00 USD |
| `7D` | `284.90` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 67,050.00 USD | 391,180.00 USD | 0.00 USD |
| `1D` | `285.10` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 87,540.00 USD | 37,830.00 USD | 96,180.00 USD |
| `7D` | `285.40` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD |
| `1D` | `285.50` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 91,500.00 USD | 95,280.00 USD | 39,050.00 USD |
| `1D` | `285.90` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 29,130.00 USD | 18,110.00 USD |
| `7D` | `285.90` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD |
| `7D` | `286.40` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 137,400.00 USD | 11.42 USD |
| `1D` | `286.70` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 750.70 USD | 3,470.00 USD | 23,380.00 USD |
| `7D` | `286.90` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 51,390.00 USD | 148,230.00 USD | 2.56 USD |
| `1D` | `287.10` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 31,110.00 USD | 117,540.00 USD | 80,720.00 USD |
| `7D` | `287.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 53,620.00 USD | 103,430.00 USD | 53,370.00 USD |
| `1D` | `287.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 21,390.00 USD | 54,720.00 USD |
| `1D` | `287.90` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 9,030.00 USD | 10,410.00 USD | 38,750.00 USD |
| `7D` | `287.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 277,850.00 USD | 23.40 USD |
| `1D` | `288.30` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 28,590.00 USD | 4,000.00 USD | 5,060.00 USD |
| `1D` | `288.70` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 7,560.00 USD | 5,700.00 USD | 0.00 USD |
| `7D` | `288.90` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 9.00 USD |
| `1D` | `289.10` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 1,720.00 USD | 20,030.00 USD | 9,870.00 USD |
| `7D` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `1D` | `289.50` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 4,030.00 USD | 14.24 USD |
| `1D` | `289.90` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 957.57 USD | 0.00 USD | 14,160.00 USD |
| `7D` | `289.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD |
| `7D` | `290.40` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 34,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.70` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 33,020.00 USD | 7,010.00 USD | 16,960.00 USD |
| `7D` | `290.90` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 5.10 USD |
| `1D` | `291.10` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 352.90 USD | 0.00 USD | 5.82 USD |
| `7D` | `291.40` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 1,340.00 USD | 55,720.00 USD | 19.10 USD |
| `1D` | `291.50` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 562.74 USD | 22,110.00 USD | 22.17 USD |
| `1D` | `291.90` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 22,140.00 USD |
| `7D` | `291.90` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 9.60 USD |
| `1D` | `292.30` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 13,260.00 USD | 61,370.00 USD | 8,120.00 USD |
| `7D` | `292.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 71,940.00 USD | 32.44 USD |
| `1D` | `292.70` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 20,240.00 USD | 71,800.00 USD | 9.69 USD |
| `7D` | `292.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 119,560.00 USD | 23.76 USD |
| `1D` | `293.10` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 10,710.00 USD | 35,470.00 USD | 13,280.00 USD |
| `7D` | `293.40` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 43.05 USD |
| `1D` | `293.50` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 19,530.00 USD | 55,160.00 USD | 23,910.00 USD |
| `1D` | `293.90` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 88,090.00 USD | 19,500.00 USD | 43,980.00 USD |
| `7D` | `293.90` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,030.00 USD |
| `1D` | `294.30` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 28,410.00 USD | 48,550.00 USD | 56,640.00 USD |
| `7D` | `294.40` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 139,780.00 USD | 14,550.00 USD | 60,670.00 USD |
| `1D` | `294.70` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 111,760.00 USD | 96,720.00 USD | 119,520.00 USD |
| `7D` | `294.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 64,510.00 USD | 107,870.00 USD | 104,920.00 USD |
| `1D` | `295.10` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 23,770.00 USD | 41,270.00 USD | 53,300.00 USD |
| `7D` | `295.40` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD |
| `1D` | `295.50` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 39,490.00 USD | 63,880.00 USD | 50,050.00 USD |
| `1D` | `295.90` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 82,120.00 USD | 19,540.00 USD | 33,310.00 USD |
| `7D` | `295.90` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 108,830.00 USD | 133,090.00 USD | 150,850.00 USD |
| `1D` | `296.30` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 69,980.00 USD | 82,640.00 USD | 27,160.00 USD |
| `7D` | `296.40` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 27,680.00 USD | 77,570.00 USD | 120,810.00 USD |
| `1D` | `296.70` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 34,010.00 USD | 21,030.00 USD | 62,260.00 USD |
| `7D` | `296.90` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 207,350.00 USD | 50,930.00 USD | 172,360.00 USD |
| `1D` | `297.10` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 52,650.00 USD | 323.66 USD | 36,490.00 USD |
| `7D` | `297.40` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 4,100.00 USD | 59,290.00 USD | 34,770.00 USD |
| `1D` | `297.50` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 6,700.00 USD | 1,120.00 USD | 20,820.00 USD |
| `1D` | `297.90` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 1,730.00 USD | 9,670.00 USD | 16,110.00 USD |
| `7D` | `297.90` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 17,770.00 USD | 39,840.00 USD | 54,850.00 USD |
| `1D` | `298.30` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 55,610.00 USD | 974.79 USD | 93,920.00 USD |
| `7D` | `298.40` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 32,250.00 USD | 42,710.00 USD | 68,810.00 USD |
| `1D` | `298.70` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 30,040.00 USD | 7,690.00 USD | 80,710.00 USD |
| `7D` | `298.90` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 70,090.00 USD | 12,780.00 USD | 40,080.00 USD |
| `1D` | `299.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 7,660.00 USD | 18,270.00 USD | 26,320.00 USD |
| `7D` | `299.40` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 4,470.00 USD | 13,080.00 USD | 45,970.00 USD |
| `1D` | `299.50` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 35,750.00 USD | 15,000.00 USD | 19,140.00 USD |
| `1D` | `299.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 14,520.00 USD | 17,340.00 USD | 32,600.00 USD |
| `7D` | `299.90` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 56,210.00 USD | 10,220.00 USD | 19,830.00 USD |
| `1D` | `300.30` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 33,000.00 USD | 24,420.00 USD | 42,610.00 USD |
| `7D` | `300.40` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 121.42 USD |
| `1D` | `300.70` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 15,970.00 USD | 30,870.00 USD | 17,840.00 USD |
| `7D` | `300.90` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 24,730.00 USD | 70,210.00 USD | 104,110.00 USD |
| `1D` | `301.10` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 4,280.00 USD | 20,930.00 USD | 26,010.00 USD |
| `7D` | `301.40` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 71,890.00 USD | 56,010.00 USD | 94,620.00 USD |
| `1D` | `301.50` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 19,640.00 USD | 8,100.00 USD | 34,830.00 USD |
| `1D` | `301.90` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 20,900.00 USD | 38,380.00 USD | 11,570.00 USD |
| `7D` | `301.90` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 89,300.00 USD | 185,430.00 USD | 26,360.00 USD |
| `1D` | `302.30` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 4,890.00 USD | 4,690.00 USD | 17,540.00 USD |
| `7D` | `302.40` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 50.20 USD |
| `1D` | `302.70` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 11,530.00 USD | 11,670.00 USD | 34,800.00 USD |
| `7D` | `302.90` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 71,700.00 USD | 110,480.00 USD | 41,930.00 USD |
| `1D` | `303.10` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 20,770.00 USD | 1,020.00 USD | 24,010.00 USD |
| `7D` | `303.40` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 47.58 USD |
| `1D` | `303.50` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 10,860.00 USD | 1,620.00 USD | 6,250.00 USD |
| `1D` | `303.90` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 29,150.00 USD | 3,670.00 USD | 18,760.00 USD |
| `7D` | `303.90` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 21,140.00 USD | 11,010.00 USD | 45,900.00 USD |
| `1D` | `304.30` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 3,890.00 USD | 5,160.00 USD | 48,500.00 USD |
| `7D` | `304.40` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 3,670.00 USD | 11,280.00 USD | 259.62 USD |
| `1D` | `304.70` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 9,880.00 USD | 6,170.00 USD | 44,520.00 USD |
| `7D` | `304.90` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 36,160.00 USD | 18,990.00 USD | 8,410.00 USD |
| `1D` | `305.10` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 14,400.00 USD | 178.95 USD | 4,030.00 USD |
| `7D` | `305.40` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 163,730.00 USD | 127,450.00 USD | 119,210.00 USD |
| `1D` | `305.50` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 4,670.00 USD | 1,640.00 USD | 1,490.00 USD |
| `1D` | `305.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 9,360.00 USD | 5,780.00 USD | 5,880.00 USD |
| `7D` | `305.90` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 82,000.00 USD | 55,480.00 USD | 10,570.00 USD |
| `1D` | `306.30` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 3,900.00 USD | 3,200.00 USD | 1,340.00 USD |
| `7D` | `306.40` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 39,250.00 USD | 55,740.00 USD | 66,770.00 USD |
| `1D` | `306.70` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 4,670.00 USD | 21,680.00 USD | 9,490.00 USD |
| `7D` | `306.90` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 84,850.00 USD | 64,520.00 USD | 102,670.00 USD |
| `1D` | `307.10` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 32,760.00 USD | 42,120.00 USD | 20,490.00 USD |
| `7D` | `307.40` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 46,230.00 USD | 154,680.00 USD | 83,290.00 USD |
| `1D` | `307.50` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 19,010.00 USD | 24,960.00 USD | 9,430.00 USD |
| `1D` | `307.90` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 33,320.00 USD | 30,350.00 USD | 21,610.00 USD |
| `7D` | `307.90` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 136,380.00 USD | 101,120.00 USD | 65,350.00 USD |
| `1D` | `308.30` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 13,480.00 USD | 7,490.00 USD | 5,640.00 USD |
| `7D` | `308.40` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 152,590.00 USD | 50,070.00 USD | 124,960.00 USD |
| `1D` | `308.70` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 5,270.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `308.90` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 61,600.00 USD | 52,230.00 USD | 19,690.00 USD |
| `1D` | `309.00` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 11,380.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `298.53M` | Total OI Tokens: `1,074,699.8 BCH`
  * 1h OI Change: `-0.26%` | 4h OI Change: `-5.42%` | 24h OI Change: `-7.57%`
  * Exchange Breakdown: Binance=`87.50M` | Bybit=`37.38M` | OKX=`23.39M` | Hyperliquid=`7.58M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.73K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0076%` | **USDT OKX** | `-0.0023%` |
| **USDT Bybit** | `-0.0026%` | **USDT KuCoin** | `0.0025%` |
| **USDT MEXC** | `0.0074%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0039%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `48.22%` | `51.78%` | `0.93` | 3,240,000.00 USD |
| `15M` | `Binance` | `41.37%` | `58.63%` | `0.71` | 1,100,000.00 USD |
| `15M` | `OKX` | `40.52%` | `59.48%` | `0.68` | 469,170.00 USD |
| `15M` | `Bybit` | `50.77%` | `49.23%` | `1.03` | 240,290.00 USD |
| `15M` | `KuCoin` | `39.77%` | `60.23%` | `0.66` | 51,630.00 USD |
| `15M` | `Gate` | `46.61%` | `53.39%` | `0.87` | 185,020.00 USD |
| `15M` | `Bitget` | `45.8%` | `54.2%` | `0.85` | 37,290.00 USD |
| `15M` | `BingX` | `47.7%` | `52.3%` | `0.91` | 487,420.00 USD |
| `15M` | `MEXC` | `54.6%` | `45.4%` | `1.20` | 136,330.00 USD |
| `15M` | `Bitunix` | `29.59%` | `70.41%` | `0.42` | 41,980.00 USD |
| `15M` | `Hyperliquid` | `53.26%` | `46.74%` | `1.14` | 16,710.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.29%` | `53.71%` | `0.86` | 106,730.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `85.77%` | `14.23%` | `6.03` | 334,590.00 USD |
| `15M` | `HTX` | `12.29%` | `87.71%` | `0.14` | 3,580.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `43.42%` | `56.58%` | `0.77` | 12,780.00 USD |
| `15M` | `Aster` | `0.69%` | `99.31%` | `0.01` | 15,050.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `41.37%` | `58.63%` | `0.71` | 1,100,000.00 USD |
| `15M` | `Global Accounts` | `48.22%` | `51.78%` | `0.93` | 3,240,000.00 USD |
| `1H` | `BCH` | `50.07%` | `49.93%` | `1.00` | 17,310,000.00 USD |
| `1H` | `Binance` | `51.26%` | `48.74%` | `1.05` | 5,660,000.00 USD |
| `1H` | `OKX` | `48.4%` | `51.6%` | `0.94` | 1,980,000.00 USD |
| `1H` | `Bybit` | `53.37%` | `46.63%` | `1.14` | 1,620,000.00 USD |
| `1H` | `KuCoin` | `46.51%` | `53.49%` | `0.87` | 290,370.00 USD |
| `1H` | `Gate` | `49.51%` | `50.49%` | `0.98` | 758,900.00 USD |
| `1H` | `Bitget` | `55.35%` | `44.65%` | `1.24` | 297,350.00 USD |
| `1H` | `BingX` | `37.1%` | `62.9%` | `0.59` | 2,810,000.00 USD |
| `1H` | `MEXC` | `44.37%` | `55.63%` | `0.80` | 606,960.00 USD |
| `1H` | `Bitunix` | `45.69%` | `54.31%` | `0.84` | 283,920.00 USD |
| `1H` | `Hyperliquid` | `53.61%` | `46.39%` | `1.16` | 327,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.12%` | `50.88%` | `0.97` | 354,620.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `64.85%` | `35.15%` | `1.84` | 2,200,000.00 USD |
| `1H` | `HTX` | `44.02%` | `55.98%` | `0.79` | 31,350.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.95%` | `57.05%` | `0.75` | 49,380.00 USD |
| `1H` | `Aster` | `17.56%` | `82.44%` | `0.21` | 32,420.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `99.92%` | `0.08%` | `1249.00` | 9,670.00 USD |
| `1H` | `Whale Positions` | `51.26%` | `48.74%` | `1.05` | 5,660,000.00 USD |
| `1H` | `Global Accounts` | `50.07%` | `49.93%` | `1.00` | 17,310,000.00 USD |
| `4H` | `BCH` | `47.91%` | `52.09%` | `0.92` | 129,650,000.00 USD |
| `4H` | `Binance` | `46.08%` | `53.92%` | `0.85` | 46,380,000.00 USD |
| `4H` | `OKX` | `47.88%` | `52.12%` | `0.92` | 16,000,000.00 USD |
| `4H` | `Bybit` | `53.56%` | `46.44%` | `1.15` | 15,570,000.00 USD |
| `4H` | `KuCoin` | `45.31%` | `54.69%` | `0.83` | 1,030,000.00 USD |
| `4H` | `Gate` | `47.11%` | `52.89%` | `0.89` | 8,600,000.00 USD |
| `4H` | `Bitget` | `36.17%` | `63.83%` | `0.57` | 4,810,000.00 USD |
| `4H` | `BingX` | `44.84%` | `55.16%` | `0.81` | 10,080,000.00 USD |
| `4H` | `MEXC` | `29.78%` | `70.22%` | `0.42` | 6,100,000.00 USD |
| `4H` | `Bitunix` | `47.24%` | `52.76%` | `0.90` | 2,540,000.00 USD |
| `4H` | `Hyperliquid` | `45.64%` | `54.36%` | `0.84` | 1,780,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.75%` | `52.25%` | `0.91` | 3,100,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `64.83%` | `35.17%` | `1.84` | 11,750,000.00 USD |
| `4H` | `HTX` | `45.57%` | `54.43%` | `0.84` | 629,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `65.93%` | `34.07%` | `1.94` | 692,110.00 USD |
| `4H` | `Aster` | `55.32%` | `44.68%` | `1.24` | 431,140.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.89%` | `68.11%` | `0.47` | 154,230.00 USD |
| `4H` | `Whale Positions` | `46.08%` | `53.92%` | `0.85` | 46,380,000.00 USD |
| `4H` | `Global Accounts` | `47.91%` | `52.09%` | `0.92` | 129,650,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `275.52` | `277.16` | `275.52` | `282.40` | `273.60` | 7,176,408.30 USD | 3,429,549.36 USD | 3,746,858.94 USD | -317,309.59 USD | `-4.42%` | `7B / 13S` |
| `5:00 UTC` | `273.26` | `272.72` | `273.26` | `275.70` | `269.30` | 7,511,252.05 USD | 3,875,803.21 USD | 3,635,448.84 USD | 240,354.37 USD | `+3.20%` | `12B / 10S` |
| `0:00 UTC` | `273.80` | `272.56` | `273.80` | `274.68` | `269.76` | 3,951,157.31 USD | 2,047,269.47 USD | 1,903,887.84 USD | 143,381.63 USD | `+3.63%` | `9B / 4S` |
| `5:00 UTC` | `276.40` | `276.70` | `276.40` | `278.76` | `273.60` | 2,981,088.00 USD | 1,514,309.73 USD | 1,466,778.26 USD | 47,531.47 USD | `+1.59%` | `19B / 11S` |
| `0:00 UTC` | `279.50` | `278.78` | `279.50` | `280.00` | `277.16` | 1,923,752.33 USD | 667,499.40 USD | 1,256,252.93 USD | -588,753.54 USD | `-30.60%` | `8B / 42S` |
| `5:00 UTC` | `276.86` | `277.31` | `276.86` | `278.92` | `275.98` | 2,702,816.05 USD | 1,627,166.23 USD | 1,075,649.82 USD | 551,516.40 USD | `+20.41%` | `18B / 30S` |
| `0:00 UTC` | `277.76` | `276.89` | `277.76` | `279.16` | `274.00` | 4,286,596.03 USD | 2,451,355.63 USD | 1,835,240.40 USD | 616,115.23 USD | `+14.37%` | `33B / 11S` |
| `5:00 UTC` | `277.49` | `277.51` | `277.49` | `278.59` | `275.93` | 1,507,866.81 USD | 644,040.10 USD | 863,826.71 USD | -219,786.61 USD | `-14.58%` | `11B / 24S` |
| `0:00 UTC` | `278.41` | `278.31` | `278.41` | `279.47` | `277.01` | 1,126,883.43 USD | 482,083.70 USD | 644,799.73 USD | -162,716.03 USD | `-14.44%` | `11B / 24S` |
| `5:00 UTC` | `276.72` | `277.32` | `276.72` | `278.25` | `276.61` | 713,187.72 USD | 284,325.85 USD | 428,861.87 USD | -144,536.02 USD | `-20.27%` | `38B / 54S` |

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
| `5m` | 896.92 USD | -124,990.00 USD | **`DISTRIBUTION`** |
| `15m` | -53,370.00 USD | -243,120.00 USD | **`DISTRIBUTION`** |
| `30m` | -28,450.00 USD | -360,130.00 USD | **`DISTRIBUTION`** |
| `1h` | 237,770.00 USD | -229,550.00 USD | **`ACCUMULATION`** |
| `2h` | 418,360.00 USD | 1,000,000.00 USD | **`ACCUMULATION`** |
| `4h` | -519,100.00 USD | -267,140.00 USD | **`DISTRIBUTION`** |
| `6h` | -504,180.00 USD | 585,670.00 USD | **`ACCUMULATION`** |
| `8h` | -546,720.00 USD | -2,050,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -484,470.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,440,000.00 USD | -9,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -457,370.00 USD | -12,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,410,000.00 USD | -137,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+896.92` | 15m=`-53.37K` | 1h=`+237.77K` | 24h=`-1.44M`
* Futures Capital Netflows: 5m=`-124.99K` | 15m=`-243.12K` | 1h=`-229.55K` | 24h=`-9.07M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `274.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `272.66` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `279.91`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.58` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `280.65` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `273.40`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`279.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
