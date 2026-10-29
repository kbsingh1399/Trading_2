# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 01:08:42 IST` (`2026-10-29 19:38:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.68` | **Live Ask Quote**: `11.76` | **Mid Price**: `11.72`
- **Spread Points**: `85.00` | **Spread BPS**: `72.54 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.57` | VWAP Z-Score: `+0.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0720` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.16` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.11` | Lower -3.00σ Band: `11.03`
  * Upper +2.51σ Band: `12.02` | Lower -2.51σ Band: `11.12`
  * Upper +2.01σ Band: `11.93` | Lower -2.01σ Band: `11.21`
  * Upper +2.00σ Band: `11.93` | Lower -2.00σ Band: `11.21`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.34`
  * Upper +1.00σ Band: `11.75` | Lower -1.00σ Band: `11.39`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.66` | EMA-20=`11.68` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.63` (Slope: `+0.0000`) | EMA-100=`11.59`
  * Institutional Anchors: EMA-144=`11.57` | EMA-200=`11.54` (Slope: `+0.1669`) | EMA-233=`11.51`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`11.23` | Weekly High=`11.96` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.91` (Distance: `-1.54%`)
  * Point of Control (POC) = `11.77` (Distance: `-0.40%`)
  * Value Area Low (VAL) = `11.44` (Distance: `+2.47%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.58` | Weekly POC=`11.41` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.96` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.67` - `11.76`
  * Optimal Trade Entry (OTE 0.705): `11.74`
  * Structural Invalidation Anchor (0.786): `11.81`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.65` | `11.68` | `11.64` | `11.68` | `11,843` | 138,198.09 USD | 1,916.36 USD | `+1.39%` | -392,726.73 USD | `+0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `11.68` | `11.68` | `11.66` | `11.68` | `39,484` | 460,847.60 USD | -140,192.35 USD | `-30.42%` | -532,919.09 USD | `-0.94` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.68` | `11.73` | `11.68` | `11.73` | `43,103` | 504,594.39 USD | 119,440.57 USD | `+23.67%` | -413,478.52 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.68` | `11.69` | `11.64` | `11.64` | `73,796` | 859,560.77 USD | -257,858.72 USD | `-30.00%` | -339,762.56 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.64` | `11.68` | `11.63` | `11.68` | `85,534` | 997,243.09 USD | -276,964.43 USD | `-27.77%` | -616,726.99 USD | `-0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.68` | `11.73` | `11.68` | `11.73` | `42,981` | 503,169.85 USD | 118,016.04 USD | `+23.45%` | -498,710.95 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `11.86` | `11.87` | `11.66` | `11.74` | `476,252` | 5,603,289.28 USD | -228,969.33 USD | `-4.09%` | -626,109.15 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.68` | `461,460` | 5,390,854.94 USD | 388,230.26 USD | `+7.20%` | -237,878.89 USD | `+0.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.73` | `11.63` | `11.73` | `202,325` | 2,360,125.75 USD | -416,655.08 USD | `-17.65%` | -654,533.98 USD | `-0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.73` | `1,951,653` | 23,019,514.01 USD | -1,215,589.22 USD | `-5.28%` | -669,406.10 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.73` | `1,951,653` | 23,019,514.01 USD | -1,215,589.22 USD | `-5.28%` | -669,406.10 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.72`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:03:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `487` | `0x73ce...8ce9` | `LONG` | 4,688,535.96 USD | `400,011,600.00` | `12.05` | `11.72` | `9.13` | -131,217.74 USD | `-2.80%` | `5X Cross` |
| `637` | `0x5b5d...c060` | `SHORT` | 3,654,311.76 USD | `311,728,200.00` | `13.61` | `11.72` | `492.89` | 587,820.35 USD | `+16.09%` | `3X Cross` |
| `643` | `0xb83d...6e36` | `SHORT` | 3,611,849.59 USD | `308,152,000.00` | `12.93` | `11.72` | `420.18` | 373,403.90 USD | `+10.34%` | `3X Cross` |
| `859` | `0x458d...ab3b` | `LONG` | 2,662,794.44 USD | `227,156,700.00` | `13.13` | `11.72` | `9.34` | -319,435.96 USD | `-12.00%` | `3X Isolated` |
| `945` | `0xdd53...2b13` | `SHORT` | 2,420,303.47 USD | `206,475,300.00` | `11.92` | `11.72` | `274.59` | 40,919.46 USD | `+1.69%` | `3X Cross` |
| `977` | `0x3dc9...54b0` | `SHORT` | 2,344,400.00 USD | `200,000,000.00` | `7.56` | `11.72` | `81.83` | -833,241.58 USD | `-35.54%` | `10X Cross` |
| `999` | `0x45d2...4029` | `SHORT` | 2,291,846.50 USD | `195,500,000.00` | `11.54` | `11.72` | `192.03` | -35,363.07 USD | `-1.54%` | `10X Cross` |
| `1197` | `0x6540...f7b7` | `LONG` | 1,919,750.27 USD | `163,759,300.00` | `12.48` | `11.72` | `8.01` | -123,426.66 USD | `-6.43%` | `5X Isolated` |
| `1255` | `0xeadc...9d55` | `LONG` | 1,848,382.09 USD | `157,691,600.00` | `9.43` | `11.72` | `0.000000` | 361,727.19 USD | `+19.57%` | `10X Cross` |
| `1608` | `0x9df2...c665` | `SHORT` | 1,381,971.54 USD | `117,905,600.00` | `11.48` | `11.72` | `253.07` | -27,953.26 USD | `-2.02%` | `10X Cross` |
| `1638` | `0xf6f3...47f8` | `SHORT` | 1,348,433.39 USD | `115,024,600.00` | `11.42` | `11.72` | `18.72` | -35,103.20 USD | `-2.60%` | `5X Cross` |
| `1798` | `0xfe7e...11b4` | `LONG` | 1,185,608.78 USD | `101,142,000.00` | `14.47` | `11.72` | `5.33` | -277,504.37 USD | `-23.41%` | `5X Isolated` |
| `1829` | `0x8af7...fa05` | `SHORT` | 1,156,506.59 USD | `98,661,200.00` | `14.08` | `11.72` | `204.40` | 232,675.95 USD | `+20.12%` | `10X Cross` |
| `1884` | `0xb7ec...5166` | `LONG` | 1,107,941.84 USD | `94,515,900.00` | `9.01` | `11.72` | `7.20` | 256,081.27 USD | `+23.11%` | `4X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.53` | 5,184.59 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.18K USD at 11.5290 USD [API] | `2026-10-27 22:22:38` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,130.50 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.13K USD at 11.5370 USD [API] | `2026-10-27 23:02:34` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 6,217.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.22K USD at 11.5370 USD [API] | `2026-10-27 23:02:31` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,831.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.83K USD at 11.5370 USD [API] | `2026-10-27 23:01:48` |
| `ANNOUNCEMENT` | `INFO` | `12.10` | 421.08 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.42K USD at 12.1000 USD [API] | `2026-10-08 17:26:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`12.16` (Vol: 178,200.00 USD, Dist: `+3.82%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.50%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+2.90%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.68%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.35%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.77%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.36%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.73%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 2,500.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 2,250.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 442.68 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 34,400.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 632.50 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 269.90 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 8,210.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 951.40 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 345.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,300.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,340.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 4,160.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 15,960.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 19,980.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,940.00 USD | 13,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 745.59 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 651.48 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 222,950.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 5,810.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 55,670.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 15,450.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 90,620.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 542,530.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 27,350.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 8,390.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 18,730.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 20,310.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 11,220.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,180.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,910.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 141,810.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,840.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 22,560.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 6,770.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 810.37 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 3,760.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 730,260.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,080.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 45,460.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 6,940.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 21,000.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 660.96 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 244.12 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 726.91 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 15,130.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,420,000.00 USD | 11,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,010.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 33,960.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,770.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 10,670.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 23,380.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 33,160.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 304,290.00 USD | 10,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 34,730.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,940.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 35,420.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,760,000.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 25,310.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 25,230.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 16,760.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 8,830.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 103,770.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 17,500.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 773,910.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 645,910.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 60,410.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.25` | 271,590.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.27` | 20,210,000.00 USD | 20,210,000.00 USD | 92,330.00 USD | 32,960.00 USD | 72,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 20,010,000.00 USD | 20,010,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 19,930,000.00 USD | 19,930,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 19,740,000.00 USD | 19,740,000.00 USD | 57,270.00 USD | 28,270.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 19,630,000.00 USD | 19,630,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 9,660.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.37` | 19,570,000.00 USD | 19,570,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 19,520,000.00 USD | 19,520,000.00 USD | 4,240.00 USD | 648.05 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 19,470,000.00 USD | 19,470,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 19,320,000.00 USD | 19,320,000.00 USD | 32,710.00 USD | 14,710.00 USD | 14,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 19,260,000.00 USD | 19,260,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 14,500.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 6,280,000.00 USD | 6,280,000.00 USD | 27,560.00 USD | 8,350.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 19,170,000.00 USD | 19,170,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 6,230,000.00 USD | 6,230,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 19,090,000.00 USD | 19,090,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 6,200,000.00 USD | 6,200,000.00 USD | 23,170.00 USD | 9,270.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 19,040,000.00 USD | 19,040,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 6,160,000.00 USD | 6,160,000.00 USD | 22,700.00 USD | 3,770.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 18,950,000.00 USD | 18,950,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 6,130,000.00 USD | 6,130,000.00 USD | 715.66 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 18,910,000.00 USD | 18,910,000.00 USD | 55,490.00 USD | 18,800.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 198,380.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 6,120,000.00 USD | 6,120,000.00 USD | 22,600.00 USD | 4,320.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 18,820,000.00 USD | 18,820,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 6,100,000.00 USD | 6,100,000.00 USD | 16,870.00 USD | 5,420.00 USD | 8,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 18,710,000.00 USD | 18,710,000.00 USD | 33,510.00 USD | 9,440.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,070,000.00 USD | 6,070,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 18,660,000.00 USD | 18,660,000.00 USD | 26,680.00 USD | 10,560.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,060,000.00 USD | 6,060,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 18,620,000.00 USD | 18,620,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 6,010,000.00 USD | 6,010,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 18,540,000.00 USD | 18,540,000.00 USD | 6,380.00 USD | 2,920.00 USD | 168.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 48,560.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 5,970,000.00 USD | 5,970,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 18,530,000.00 USD | 18,530,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 5,940,000.00 USD | 5,940,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 18,500,000.00 USD | 18,500,000.00 USD | 18,290.00 USD | 0.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 5,930,000.00 USD | 5,930,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 18,480,000.00 USD | 18,480,000.00 USD | 14,600.00 USD | 0.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 5,920,000.00 USD | 5,920,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 18,450,000.00 USD | 18,450,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 5,900,000.00 USD | 5,900,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 18,420,000.00 USD | 18,420,000.00 USD | 17,290.00 USD | 4,010.00 USD | 318.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 5,870,000.00 USD | 5,870,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 18,400,000.00 USD | 18,400,000.00 USD | 16,290.00 USD | 3,960.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 5,850,000.00 USD | 5,850,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 18,370,000.00 USD | 18,370,000.00 USD | 57,970.00 USD | 1,400.00 USD | 24,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 5,840,000.00 USD | 5,840,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 18,280,000.00 USD | 18,280,000.00 USD | 86,860.00 USD | 28,970.00 USD | 60,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 5,840,000.00 USD | 5,840,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 18,110,000.00 USD | 18,110,000.00 USD | 123,460.00 USD | 23,810.00 USD | 45,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 5,840,000.00 USD | 5,840,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 17,910,000.00 USD | 17,910,000.00 USD | 231,910.00 USD | 23,820.00 USD | 83,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 85,390.00 USD | 843,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 5,830,000.00 USD | 5,830,000.00 USD | 976.86 USD | 4,520.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 17,580,000.00 USD | 17,580,000.00 USD | 86,700.00 USD | 41,310.00 USD | 100,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 5,820,000.00 USD | 5,820,000.00 USD | 1,820.00 USD | 10,400.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 17,350,000.00 USD | 17,350,000.00 USD | 235,210.00 USD | 62,890.00 USD | 175,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 5,800,000.00 USD | 5,800,000.00 USD | 1,120.00 USD | 3,770.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 16,870,000.00 USD | 16,870,000.00 USD | 271,580.00 USD | 48,930.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 5,760,000.00 USD | 5,760,000.00 USD | 66,100.00 USD | 28,790.00 USD | 58,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 16,340,000.00 USD | 16,340,000.00 USD | 395,920.00 USD | 107,040.00 USD | 316,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 5,610,000.00 USD | 5,610,000.00 USD | 46,880.00 USD | 17,110.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 15,520,000.00 USD | 15,520,000.00 USD | 308,350.00 USD | 107,220.00 USD | 305,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 757,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 5,540,000.00 USD | 5,540,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 14,800,000.00 USD | 14,800,000.00 USD | 165,580.00 USD | 96,900.00 USD | 114,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 5,390,000.00 USD | 5,390,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 14,420,000.00 USD | 14,420,000.00 USD | 94,430.00 USD | 117,780.00 USD | 249,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 5,340,000.00 USD | 5,340,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 13,960,000.00 USD | 13,960,000.00 USD | 141,200.00 USD | 39,420.00 USD | 103,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 5,290,000.00 USD | 5,290,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.03` | 13,680,000.00 USD | 13,680,000.00 USD | 423,180.00 USD | 178,040.00 USD | 207,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,140,000.00 USD | 5,140,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.05` | 12,870,000.00 USD | 12,870,000.00 USD | 260,170.00 USD | 70,790.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 122,470.00 USD | 199,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,110,000.00 USD | 5,110,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.07` | 12,380,000.00 USD | 12,380,000.00 USD | 437,450.00 USD | 53,630.00 USD | 224,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,060,000.00 USD | 5,060,000.00 USD | 28,900.00 USD | 15,060.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.09` | 11,670,000.00 USD | 11,670,000.00 USD | 170,080.00 USD | 126,860.00 USD | 397,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 4,990,000.00 USD | 4,990,000.00 USD | 31,390.00 USD | 30,270.00 USD | 32,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.11` | 10,970,000.00 USD | 10,970,000.00 USD | 575,850.00 USD | 145,120.00 USD | 441,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 4,900,000.00 USD | 4,900,000.00 USD | 52,470.00 USD | 33,090.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.13` | 9,810,000.00 USD | 9,810,000.00 USD | 618,260.00 USD | 148,900.00 USD | 476,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 4,730,000.00 USD | 4,730,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.15` | 8,570,000.00 USD | 8,570,000.00 USD | 809,230.00 USD | 195,340.00 USD | 593,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 26,420.00 USD | 77,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 4,350,000.00 USD | 4,350,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.17` | 6,970,000.00 USD | 6,970,000.00 USD | 527,700.00 USD | 265,230.00 USD | 520,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 4,060,000.00 USD | 4,060,000.00 USD | 137,180.00 USD | 48,450.00 USD | 63,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.19` | 5,660,000.00 USD | 5,660,000.00 USD | 597,320.00 USD | 155,670.00 USD | 279,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 3,810,000.00 USD | 3,810,000.00 USD | 222,000.00 USD | 49,900.00 USD | 95,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.21` | 4,620,000.00 USD | 4,620,000.00 USD | 319,760.00 USD | 249,060.00 USD | 282,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 3,440,000.00 USD | 3,440,000.00 USD | 97,140.00 USD | 31,640.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.23` | 3,770,000.00 USD | 3,770,000.00 USD | 201,470.00 USD | 197,890.00 USD | 58,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 3,270,000.00 USD | 3,270,000.00 USD | 102,960.00 USD | 56,970.00 USD | 70,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.25` | 3,310,000.00 USD | 3,310,000.00 USD | 332,220.00 USD | 106,830.00 USD | 101,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 41,990.00 USD | 50,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 3,040,000.00 USD | 3,040,000.00 USD | 185,010.00 USD | 39,170.00 USD | 55,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.27` | 2,770,000.00 USD | 2,770,000.00 USD | 181,530.00 USD | 128,400.00 USD | 101,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 2,760,000.00 USD | 2,760,000.00 USD | 44,920.00 USD | 15,750.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.29` | 2,360,000.00 USD | 2,360,000.00 USD | 104,970.00 USD | 43,570.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 2,650,000.00 USD | 2,650,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.31` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,590.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 2,510,000.00 USD | 2,510,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.33` | 2,050,000.00 USD | 2,050,000.00 USD | 190,980.00 USD | 11,560.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 2,400,000.00 USD | 2,400,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.35` | 1,830,000.00 USD | 1,830,000.00 USD | 310,190.00 USD | 58,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 8,900.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 2,130,000.00 USD | 2,130,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.37` | 1,460,000.00 USD | 1,460,000.00 USD | 44,290.00 USD | 10,650.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 1,730,000.00 USD | 1,730,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.39` | 1,300,000.00 USD | 1,300,000.00 USD | 142,620.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 1,600,000.00 USD | 1,600,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.41` | 1,120,000.00 USD | 1,120,000.00 USD | 34,370.00 USD | 14,250.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 1,410,000.00 USD | 1,410,000.00 USD | 106,690.00 USD | 45,130.00 USD | 70,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.43` | 1,040,000.00 USD | 1,040,000.00 USD | 133,220.00 USD | 29,480.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 1,180,000.00 USD | 1,180,000.00 USD | 130,750.00 USD | 48,050.00 USD | 77,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.45` | 822,540.00 USD | 822,540.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 928,060.00 USD | 928,060.00 USD | 177,600.00 USD | 30,500.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.47` | 568,010.00 USD | 568,010.00 USD | 17,370.00 USD | 14,370.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 695,110.00 USD | 695,110.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.49` | 497,510.00 USD | 497,510.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 617,750.00 USD | 617,750.00 USD | 74,140.00 USD | 32,160.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.51` | 464,390.00 USD | 464,390.00 USD | 40,840.00 USD | 33,270.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 497,160.00 USD | 497,160.00 USD | 13,090.00 USD | 28,340.00 USD | 46,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.53` | 353,030.00 USD | 353,030.00 USD | 34,770.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.54` | 409,400.00 USD | 409,400.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.55` | 313,990.00 USD | 313,990.00 USD | 0.00 USD | 55,650.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 386,800.00 USD | 386,800.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.57` | 206,820.00 USD | 206,820.00 USD | 0.00 USD | 0.00 USD | 69,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.58` | 227,840.00 USD | 227,840.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.59` | 137,320.00 USD | 137,320.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 146,200.00 USD | 146,200.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.62` | 38,810.00 USD | 38,810.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.63` | 114,540.00 USD | 114,540.00 USD | 34,910.00 USD | 57,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.65` | 22,350.00 USD | 22,350.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.66` | 24,880.00 USD | 24,880.00 USD | 0.00 USD | 0.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 66,230.00 USD | 66,230.00 USD | 0.00 USD | 4,270.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 27,920.00 USD | 27,920.00 USD | 0.00 USD | 294.87 USD | 27,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 66,610.00 USD | 66,610.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 28,150.00 USD | 28,150.00 USD | 0.00 USD | 230.72 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 262,560.00 USD | 262,560.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 205,560.00 USD | 205,560.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 205,890.00 USD | 205,890.00 USD | 0.00 USD | 324.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 279,940.00 USD | 279,940.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 206,230.00 USD | 206,230.00 USD | 0.00 USD | 342.56 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 310,750.00 USD | 310,750.00 USD | 30,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 223,270.00 USD | 223,270.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 386,150.00 USD | 386,150.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 224,320.00 USD | 224,320.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 550,660.00 USD | 550,660.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 614,840.00 USD | 614,840.00 USD | 58,850.00 USD | 5,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 308,240.00 USD | 308,240.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 832,860.00 USD | 832,860.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 380,400.00 USD | 380,400.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 861,910.00 USD | 861,910.00 USD | 438.10 USD | 5,400.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 463,860.00 USD | 463,860.00 USD | 19,640.00 USD | 25,990.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 918,370.00 USD | 918,370.00 USD | 40,020.00 USD | 16,380.00 USD | 71.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 519,050.00 USD | 519,050.00 USD | 44,160.00 USD | 4,400.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 1,000,000.00 USD | 1,000,000.00 USD | 82,030.00 USD | 0.00 USD | 165.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 591,880.00 USD | 591,880.00 USD | 59,860.00 USD | 12,940.00 USD | 20.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 1,070,000.00 USD | 1,070,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 637,460.00 USD | 637,460.00 USD | 1,220.00 USD | 15,870.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 1,310,000.00 USD | 1,310,000.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 704,210.00 USD | 704,210.00 USD | 12,210.00 USD | 26,690.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 1,920,000.00 USD | 1,920,000.00 USD | 354,730.00 USD | 35,140.00 USD | 213,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 823,200.00 USD | 823,200.00 USD | 43,720.00 USD | 7,680.00 USD | 67,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 2,280,000.00 USD | 2,280,000.00 USD | 242,400.00 USD | 3,330.00 USD | 119,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 971,390.00 USD | 971,390.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 2,670,000.00 USD | 2,670,000.00 USD | 164,140.00 USD | 5,360.00 USD | 219,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 1,080,000.00 USD | 1,080,000.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 3,320,000.00 USD | 3,320,000.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 1,480,000.00 USD | 1,480,000.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 3,950,000.00 USD | 3,950,000.00 USD | 330,170.00 USD | 106,020.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 1,950,000.00 USD | 1,950,000.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 4,520,000.00 USD | 4,520,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 2,170,000.00 USD | 2,170,000.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 4,810,000.00 USD | 4,810,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 2,230,000.00 USD | 2,230,000.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 5,090,000.00 USD | 5,090,000.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 2,490,000.00 USD | 2,490,000.00 USD | 141,930.00 USD | 54,500.00 USD | 58,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 5,330,000.00 USD | 5,330,000.00 USD | 148,530.00 USD | 63,030.00 USD | 36,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 2,680,000.00 USD | 2,680,000.00 USD | 109,520.00 USD | 30,860.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 5,890,000.00 USD | 5,890,000.00 USD | 310,620.00 USD | 114,540.00 USD | 131,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 2,890,000.00 USD | 2,890,000.00 USD | 96,770.00 USD | 58,720.00 USD | 53,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 6,030,000.00 USD | 6,030,000.00 USD | 26,820.00 USD | 61,400.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 3,070,000.00 USD | 3,070,000.00 USD | 108,930.00 USD | 37,270.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 6,360,000.00 USD | 6,360,000.00 USD | 196,200.00 USD | 58,210.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 3,220,000.00 USD | 3,220,000.00 USD | 89,220.00 USD | 33,730.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 6,740,000.00 USD | 6,740,000.00 USD | 200,760.00 USD | 62,900.00 USD | 115,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 3,330,000.00 USD | 3,330,000.00 USD | 20,470.00 USD | 39,970.00 USD | 52,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 6,960,000.00 USD | 6,960,000.00 USD | 140,270.00 USD | 19,410.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 3,390,000.00 USD | 3,390,000.00 USD | 34,030.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 7,260,000.00 USD | 7,260,000.00 USD | 134,500.00 USD | 56,330.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 5,040.00 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 3,490,000.00 USD | 3,490,000.00 USD | 55,900.00 USD | 27,170.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 7,510,000.00 USD | 7,510,000.00 USD | 141,400.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 3,650,000.00 USD | 3,650,000.00 USD | 99,490.00 USD | 24,800.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 8,030,000.00 USD | 8,030,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 3,780,000.00 USD | 3,780,000.00 USD | 57,120.00 USD | 24,040.00 USD | 45,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 8,290,000.00 USD | 8,290,000.00 USD | 157,240.00 USD | 53,480.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 3,790,000.00 USD | 3,790,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 8,580,000.00 USD | 8,580,000.00 USD | 191,980.00 USD | 89,700.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 3,840,000.00 USD | 3,840,000.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 8,730,000.00 USD | 8,730,000.00 USD | 116,830.00 USD | 15,980.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 7,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 3,880,000.00 USD | 3,880,000.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 8,800,000.00 USD | 8,800,000.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 3,930,000.00 USD | 3,930,000.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 9,340,000.00 USD | 9,340,000.00 USD | 160,660.00 USD | 42,540.00 USD | 338,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 3,990,000.00 USD | 3,990,000.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 9,650,000.00 USD | 9,650,000.00 USD | 80,100.00 USD | 32,410.00 USD | 195,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 4,070,000.00 USD | 4,070,000.00 USD | 51,980.00 USD | 13,980.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 10,250,000.00 USD | 10,250,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 4,100,000.00 USD | 4,100,000.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 10,680,000.00 USD | 10,680,000.00 USD | 57,130.00 USD | 118,850.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,930.00 USD | 12,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 4,130,000.00 USD | 4,130,000.00 USD | 411.51 USD | 15,260.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 10,970,000.00 USD | 10,970,000.00 USD | 66,870.00 USD | 29,080.00 USD | 192,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 4,140,000.00 USD | 4,140,000.00 USD | 1,500.00 USD | 2,560.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 11,140,000.00 USD | 11,140,000.00 USD | 91,900.00 USD | 17,840.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 4,150,000.00 USD | 4,150,000.00 USD | 620.31 USD | 4,320.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 11,390,000.00 USD | 11,390,000.00 USD | 136,260.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 4,190,000.00 USD | 4,190,000.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 11,700,000.00 USD | 11,700,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 4,210,000.00 USD | 4,210,000.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 11,950,000.00 USD | 11,950,000.00 USD | 126,130.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.56` | 4,260,000.00 USD | 4,260,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.57` | 12,160,000.00 USD | 12,160,000.00 USD | 131,970.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 4,280,000.00 USD | 4,280,000.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 12,280,000.00 USD | 12,280,000.00 USD | 65,910.00 USD | 17,430.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 4,280,000.00 USD | 4,280,000.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 12,410,000.00 USD | 12,410,000.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 4,310,000.00 USD | 4,310,000.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 12,580,000.00 USD | 12,580,000.00 USD | 62,580.00 USD | 28,520.00 USD | 81,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 4,350,000.00 USD | 4,350,000.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 12,810,000.00 USD | 12,810,000.00 USD | 76,240.00 USD | 26,110.00 USD | 131,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.66` | 4,350,000.00 USD | 4,350,000.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 13,120,000.00 USD | 13,120,000.00 USD | 66,110.00 USD | 19,940.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 4,360,000.00 USD | 4,360,000.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 13,360,000.00 USD | 13,360,000.00 USD | 44,600.00 USD | 34,670.00 USD | 154,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 13,460,000.00 USD | 13,460,000.00 USD | 31,960.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 4,380,000.00 USD | 4,380,000.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 13,610,000.00 USD | 13,610,000.00 USD | 54,040.00 USD | 11,090.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 4,420,000.00 USD | 4,420,000.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 13,670,000.00 USD | 13,670,000.00 USD | 33,680.00 USD | 14,710.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 4,480,000.00 USD | 4,480,000.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 13,760,000.00 USD | 13,760,000.00 USD | 36,060.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 4,500,000.00 USD | 4,500,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 13,850,000.00 USD | 13,850,000.00 USD | 56,200.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 4,530,000.00 USD | 4,530,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 13,880,000.00 USD | 13,880,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 4,540,000.00 USD | 4,540,000.00 USD | 2,680.00 USD | 3,450.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 13,900,000.00 USD | 13,900,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 4,570,000.00 USD | 4,570,000.00 USD | 20,500.00 USD | 5,820.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 13,990,000.00 USD | 13,990,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 12,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 4,600,000.00 USD | 4,600,000.00 USD | 22,700.00 USD | 3,770.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.87` | 14,020,000.00 USD | 14,020,000.00 USD | 10,160.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 4,610,000.00 USD | 4,610,000.00 USD | 91.75 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 14,110,000.00 USD | 14,110,000.00 USD | 48,720.00 USD | 18,800.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 4,640,000.00 USD | 4,640,000.00 USD | 21,720.00 USD | 4,320.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 14,210,000.00 USD | 14,210,000.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 4,650,000.00 USD | 4,650,000.00 USD | 3,090.00 USD | 4,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 14,240,000.00 USD | 14,240,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 4,670,000.00 USD | 4,670,000.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 14,250,000.00 USD | 14,250,000.00 USD | 2,290.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 4,680,000.00 USD | 4,680,000.00 USD | 227.00 USD | 5,090.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 14,290,000.00 USD | 14,290,000.00 USD | 15,020.00 USD | 10,560.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 4,720,000.00 USD | 4,720,000.00 USD | 24,650.00 USD | 7,080.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 14,360,000.00 USD | 14,360,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 4,760,000.00 USD | 4,760,000.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 14,360,000.00 USD | 14,360,000.00 USD | 2,070.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.02` | 4,790,000.00 USD | 4,790,000.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 14,370,000.00 USD | 14,370,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.04` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 14,380,000.00 USD | 14,380,000.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 12,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.07` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 14,390,000.00 USD | 14,390,000.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 14,410,000.00 USD | 14,410,000.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 14,420,000.00 USD | 14,420,000.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 12,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.17` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 14,440,000.00 USD | 14,440,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 14,460,000.00 USD | 14,460,000.00 USD | 13,890.00 USD | 259.77 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 14,480,000.00 USD | 14,480,000.00 USD | 15,330.00 USD | 0.00 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 14,510,000.00 USD | 14,510,000.00 USD | 18,020.00 USD | 4,640.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 14,540,000.00 USD | 14,540,000.00 USD | 10,290.00 USD | 8,420.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.35` | 113.48 USD | 12,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 7,500.00 USD | 20,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 22,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 1,170.00 USD | 23,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 37,130.00 USD | 60,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 598.40 USD | 60,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 898.79 USD | 61,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 621.16 USD | 62,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 87,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 16,240.00 USD | 104,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 1,180.00 USD | 105,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 10,220.00 USD | 115,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 80,740.00 USD | 196,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 196,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 455.43 USD | 196,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 5,020.00 USD | 201,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 203,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 25,210.00 USD | 228,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 469.00 USD | 228,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 145,790.00 USD | 374,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 375,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 241.50 USD | 376,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 471,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 246,540.00 USD | 717,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 718,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 718,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 720,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 724,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 724,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 724,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 2,170,000.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 319.55 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 1,880.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 39,370.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 422.65 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 756,090.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.75` | 168.07 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 2,900.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 74,290.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.15` | 336,130.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.25` | 890.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 13,900,000.00 USD | 0.00 USD | 2,500.00 USD | `-79.88%` | `1,065,000.00` |
| `Live` | `Long` | `2.45` | 13,900,000.00 USD | 0.00 USD | 2,250.00 USD | `-79.03%` | `920,000.00` |
| `Live` | `Long` | `2.55` | 13,900,000.00 USD | 0.00 USD | 442.68 USD | `-78.17%` | `173,600.00` |
| `Live` | `Long` | `2.65` | 13,900,000.00 USD | 0.00 USD | 34,400.00 USD | `-77.31%` | `12,980,800.00` |
| `Live` | `Long` | `2.75` | 13,860,000.00 USD | 0.00 USD | 632.50 USD | `-76.46%` | `230,000.00` |
| `Live` | `Long` | `2.85` | 13,860,000.00 USD | 0.00 USD | 269.90 USD | `-75.60%` | `94,700.00` |
| `Live` | `Long` | `3.05` | 13,860,000.00 USD | 0.00 USD | 6,390.00 USD | `-73.89%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 13,860,000.00 USD | 0.00 USD | 297.99 USD | `-73.03%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 13,860,000.00 USD | 0.00 USD | 8,210.00 USD | `-72.18%` | `2,527,300.00` |
| `Live` | `Long` | `3.35` | 13,850,000.00 USD | 0.00 USD | 951.40 USD | `-71.32%` | `284,000.00` |
| `Live` | `Long` | `3.45` | 13,850,000.00 USD | 0.00 USD | 345.00 USD | `-70.47%` | `100,000.00` |
| `Live` | `Long` | `3.65` | 13,850,000.00 USD | 0.00 USD | 2,300.00 USD | `-68.75%` | `631,400.00` |
| `Live` | `Long` | `3.75` | 13,840,000.00 USD | 0.00 USD | 3,340.00 USD | `-67.90%` | `890,200.00` |
| `Live` | `Long` | `3.85` | 13,840,000.00 USD | 0.00 USD | 4,160.00 USD | `-67.04%` | `1,080,500.00` |
| `Live` | `Long` | `3.95` | 13,840,000.00 USD | 0.00 USD | 15,960.00 USD | `-66.19%` | `4,040,700.00` |
| `Live` | `Long` | `4.05` | 13,820,000.00 USD | 0.00 USD | 950.54 USD | `-65.33%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 13,820,000.00 USD | 0.00 USD | 19,980.00 USD | `-64.47%` | `4,813,700.00` |
| `Live` | `Long` | `4.25` | 13,800,000.00 USD | 0.00 USD | 5,940.00 USD | `-63.62%` | `1,398,100.00` |
| `Live` | `Long` | `4.35` | 13,790,000.00 USD | 0.00 USD | 745.59 USD | `-62.76%` | `171,400.00` |
| `Live` | `Long` | `4.45` | 13,790,000.00 USD | 0.00 USD | 651.48 USD | `-61.91%` | `146,400.00` |
| `Live` | `Long` | `4.55` | 13,790,000.00 USD | 0.00 USD | 222,950.00 USD | `-61.05%` | `49,000,000.00` |
| `Live` | `Long` | `4.65` | 13,570,000.00 USD | 0.00 USD | 383.63 USD | `-60.19%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,570,000.00 USD | 0.00 USD | 418.95 USD | `-59.34%` | `88,200.00` |
| `Live` | `Long` | `4.85` | 13,570,000.00 USD | 0.00 USD | 5,810.00 USD | `-58.48%` | `1,198,700.00` |
| `Live` | `Long` | `4.95` | 13,560,000.00 USD | 0.00 USD | 883.08 USD | `-57.62%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 13,560,000.00 USD | 0.00 USD | 55,670.00 USD | `-56.77%` | `11,024,400.00` |
| `Live` | `Long` | `5.15` | 13,510,000.00 USD | 0.00 USD | 15,450.00 USD | `-55.91%` | `3,000,000.00` |
| `Live` | `Long` | `5.25` | 13,490,000.00 USD | 0.00 USD | 90,620.00 USD | `-55.06%` | `17,260,600.00` |
| `Live` | `Long` | `5.35` | 13,400,000.00 USD | 0.00 USD | 542,530.00 USD | `-54.20%` | `101,407,400.00` |
| `Live` | `Long` | `5.45` | 12,860,000.00 USD | 0.00 USD | 138.97 USD | `-53.34%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 12,860,000.00 USD | 0.00 USD | 27,350.00 USD | `-52.49%` | `4,927,500.00` |
| `Live` | `Long` | `5.65` | 12,830,000.00 USD | 0.00 USD | 35,600.00 USD | `-51.63%` | `6,300,800.00` |
| `Live` | `Long` | `5.75` | 12,790,000.00 USD | 0.00 USD | 8,390.00 USD | `-50.78%` | `1,458,900.00` |
| `Live` | `Long` | `5.85` | 12,790,000.00 USD | 0.00 USD | 18,730.00 USD | `-49.92%` | `3,202,100.00` |
| `Live` | `Long` | `5.95` | 12,770,000.00 USD | 0.00 USD | 20,310.00 USD | `-49.06%` | `3,413,400.00` |
| `Live` | `Long` | `6.05` | 12,750,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.21%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,680,000.00 USD | 0.00 USD | 11,220.00 USD | `-47.35%` | `1,825,000.00` |
| `Live` | `Long` | `6.25` | 12,670,000.00 USD | 0.00 USD | 42,180.00 USD | `-46.50%` | `6,748,700.00` |
| `Live` | `Long` | `6.35` | 12,630,000.00 USD | 0.00 USD | 16,910.00 USD | `-45.64%` | `2,663,400.00` |
| `Live` | `Long` | `6.45` | 12,610,000.00 USD | 0.00 USD | 141,810.00 USD | `-44.78%` | `21,986,200.00` |
| `Live` | `Long` | `6.55` | 12,470,000.00 USD | 0.00 USD | 2,840.00 USD | `-43.93%` | `433,500.00` |
| `Live` | `Long` | `6.65` | 12,470,000.00 USD | 0.00 USD | 22,560.00 USD | `-43.07%` | `3,391,800.00` |
| `Live` | `Long` | `6.75` | 12,450,000.00 USD | 0.00 USD | 4,130.00 USD | `-42.22%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,440,000.00 USD | 0.00 USD | 6,770.00 USD | `-41.36%` | `987,800.00` |
| `Live` | `Long` | `6.95` | 12,440,000.00 USD | 0.00 USD | 810.37 USD | `-40.50%` | `116,600.00` |
| `Live` | `Long` | `7.05` | 12,430,000.00 USD | 0.00 USD | 3,760.00 USD | `-39.65%` | `533,400.00` |
| `Live` | `Long` | `7.15` | 12,430,000.00 USD | 0.00 USD | 730,260.00 USD | `-38.79%` | `102,134,200.00` |
| `Live` | `Long` | `7.25` | 11,700,000.00 USD | 0.00 USD | 21,080.00 USD | `-37.94%` | `2,906,900.00` |
| `Live` | `Long` | `7.35` | 11,680,000.00 USD | 0.00 USD | 45,460.00 USD | `-37.08%` | `6,185,500.00` |
| `Live` | `Long` | `7.45` | 11,630,000.00 USD | 0.00 USD | 6,940.00 USD | `-36.22%` | `931,100.00` |
| `Live` | `Long` | `7.55` | 11,630,000.00 USD | 0.00 USD | 21,000.00 USD | `-35.37%` | `2,782,100.00` |
| `Live` | `Long` | `7.65` | 11,610,000.00 USD | 0.00 USD | 660.96 USD | `-34.51%` | `86,400.00` |
| `Live` | `Long` | `7.75` | 11,610,000.00 USD | 0.00 USD | 244.12 USD | `-33.66%` | `31,500.00` |
| `Live` | `Long` | `7.85` | 11,610,000.00 USD | 0.00 USD | 726.91 USD | `-32.80%` | `92,600.00` |
| `Live` | `Long` | `7.95` | 11,600,000.00 USD | 0.00 USD | 15,130.00 USD | `-31.94%` | `1,903,400.00` |
| `Live` | `Long` | `8.05` | 11,590,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-31.09%` | `175,847,600.00` |
| `Live` | `Long` | `8.15` | 10,170,000.00 USD | 0.00 USD | 16,010.00 USD | `-30.23%` | `1,964,500.00` |
| `Live` | `Long` | `8.25` | 10,160,000.00 USD | 0.00 USD | 33,960.00 USD | `-29.37%` | `4,116,000.00` |
| `Live` | `Long` | `8.35` | 10,120,000.00 USD | 0.00 USD | 7,770.00 USD | `-28.52%` | `930,800.00` |
| `Live` | `Long` | `8.45` | 10,120,000.00 USD | 0.00 USD | 10,670.00 USD | `-27.66%` | `1,263,100.00` |
| `Live` | `Long` | `8.55` | 10,110,000.00 USD | 0.00 USD | 23,380.00 USD | `-26.81%` | `2,734,400.00` |
| `Live` | `Long` | `8.65` | 10,080,000.00 USD | 0.00 USD | 33,160.00 USD | `-25.95%` | `3,833,800.00` |
| `Live` | `Long` | `8.75` | 10,050,000.00 USD | 0.00 USD | 304,290.00 USD | `-25.09%` | `34,776,300.00` |
| `Live` | `Long` | `8.85` | 9,740,000.00 USD | 0.00 USD | 34,730.00 USD | `-24.24%` | `3,924,300.00` |
| `Live` | `Long` | `8.95` | 9,710,000.00 USD | 0.00 USD | 486,940.00 USD | `-23.38%` | `54,406,700.00` |
| `Live` | `Long` | `9.05` | 9,220,000.00 USD | 0.00 USD | 35,420.00 USD | `-22.53%` | `3,913,700.00` |
| `Live` | `Long` | `9.15` | 9,190,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-21.67%` | `410,576,400.00` |
| `Live` | `Long` | `9.25` | 5,430,000.00 USD | 0.00 USD | 25,310.00 USD | `-20.81%` | `2,736,500.00` |
| `Live` | `Long` | `9.35` | 5,410,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-19.96%` | `230,268,400.00` |
| `Live` | `Long` | `9.45` | 3,250,000.00 USD | 0.00 USD | 25,230.00 USD | `-19.10%` | `2,669,400.00` |
| `Live` | `Long` | `9.55` | 3,230,000.00 USD | 0.00 USD | 16,760.00 USD | `-18.25%` | `1,755,400.00` |
| `Live` | `Long` | `9.65` | 3,210,000.00 USD | 0.00 USD | 8,830.00 USD | `-17.39%` | `914,600.00` |
| `Live` | `Long` | `9.75` | 3,200,000.00 USD | 0.00 USD | 103,770.00 USD | `-16.53%` | `10,642,900.00` |
| `Live` | `Long` | `9.85` | 3,100,000.00 USD | 0.00 USD | 17,500.00 USD | `-15.68%` | `1,777,000.00` |
| `Live` | `Long` | `9.95` | 3,080,000.00 USD | 0.00 USD | 773,910.00 USD | `-14.82%` | `77,780,400.00` |
| `Live` | `Long` | `10.05` | 2,310,000.00 USD | 0.00 USD | 645,910.00 USD | `-13.97%` | `64,270,100.00` |
| `Live` | `Long` | `10.15` | 1,660,000.00 USD | 0.00 USD | 60,410.00 USD | `-13.11%` | `5,952,000.00` |
| `Live` | `Long` | `10.25` | 1,600,000.00 USD | 0.00 USD | 271,590.00 USD | `-12.25%` | `26,497,000.00` |
| `Live` | `Long` | `10.35` | 1,330,000.00 USD | 0.00 USD | 9,660.00 USD | `-11.40%` | `933,500.00` |
| `Live` | `Long` | `10.45` | 1,320,000.00 USD | 0.00 USD | 14,500.00 USD | `-10.54%` | `1,387,200.00` |
| `Live` | `Long` | `10.55` | 1,300,000.00 USD | 0.00 USD | 198,380.00 USD | `-9.69%` | `18,803,600.00` |
| `Live` | `Long` | `10.65` | 1,110,000.00 USD | 0.00 USD | 48,560.00 USD | `-8.83%` | `4,560,000.00` |
| `Live` | `Long` | `10.75` | 1,060,000.00 USD | 0.00 USD | 214,040.00 USD | `-7.97%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 843,260.00 USD | 0.00 USD | 85,390.00 USD | `-7.12%` | `7,870,500.00` |
| `Live` | `Long` | `10.95` | 757,870.00 USD | 0.00 USD | 558,090.00 USD | `-6.26%` | `50,966,800.00` |
| `Live` | `Long` | `11.05` | 199,780.00 USD | 0.00 USD | 122,470.00 USD | `-5.41%` | `11,083,400.00` |
| `Live` | `Long` | `11.15` | 77,310.00 USD | 0.00 USD | 26,420.00 USD | `-4.55%` | `2,369,500.00` |
| `Live` | `Long` | `11.25` | 50,890.00 USD | 0.00 USD | 41,990.00 USD | `-3.69%` | `3,732,700.00` |
| `Live` | `Long` | `11.35` | 8,900.00 USD | 0.00 USD | 8,900.00 USD | `-2.84%` | `784,000.00` |
| `Live` | `Short` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | `+4.01%` | `114,600.00` |
| `Live` | `Short` | `12.25` | 6,440.00 USD | 5,040.00 USD | 0.00 USD | `+4.87%` | `411,700.00` |
| `Live` | `Short` | `12.35` | 7,170.00 USD | 736.06 USD | 0.00 USD | `+5.72%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 12,100.00 USD | 4,930.00 USD | 0.00 USD | `+6.58%` | `395,700.00` |
| `Live` | `Short` | `12.85` | 12,240.00 USD | 138.78 USD | 0.00 USD | `+10.00%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 12,350.00 USD | 113.53 USD | 0.00 USD | `+11.72%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 12,630.00 USD | 274.84 USD | 0.00 USD | `+12.57%` | `20,900.00` |
| `Live` | `Short` | `13.35` | 12,740.00 USD | 113.48 USD | 0.00 USD | `+14.28%` | `8,500.00` |
| `Live` | `Short` | `13.45` | 20,240.00 USD | 7,500.00 USD | 0.00 USD | `+15.14%` | `557,600.00` |
| `Live` | `Short` | `13.55` | 22,000.00 USD | 1,760.00 USD | 0.00 USD | `+16.00%` | `130,100.00` |
| `Live` | `Short` | `13.85` | 23,170.00 USD | 1,170.00 USD | 0.00 USD | `+18.56%` | `84,500.00` |
| `Live` | `Short` | `13.95` | 60,310.00 USD | 37,130.00 USD | 0.00 USD | `+19.42%` | `2,661,900.00` |
| `Live` | `Short` | `14.35` | 60,900.00 USD | 598.40 USD | 0.00 USD | `+22.84%` | `41,700.00` |
| `Live` | `Short` | `14.45` | 61,800.00 USD | 898.79 USD | 0.00 USD | `+23.70%` | `62,200.00` |
| `Live` | `Short` | `14.65` | 62,420.00 USD | 621.16 USD | 0.00 USD | `+25.41%` | `42,400.00` |
| `Live` | `Short` | `14.95` | 87,760.00 USD | 25,330.00 USD | 0.00 USD | `+27.98%` | `1,694,600.00` |
| `Live` | `Short` | `15.35` | 104,000.00 USD | 16,240.00 USD | 0.00 USD | `+31.41%` | `1,058,000.00` |
| `Live` | `Short` | `15.55` | 105,180.00 USD | 1,180.00 USD | 0.00 USD | `+33.12%` | `75,700.00` |
| `Live` | `Short` | `15.75` | 115,400.00 USD | 10,220.00 USD | 0.00 USD | `+34.83%` | `649,200.00` |
| `Live` | `Short` | `15.85` | 196,140.00 USD | 80,740.00 USD | 0.00 USD | `+35.69%` | `5,093,900.00` |
| `Live` | `Short` | `15.95` | 196,280.00 USD | 138.76 USD | 0.00 USD | `+36.54%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 196,730.00 USD | 455.43 USD | 0.00 USD | `+38.25%` | `28,200.00` |
| `Live` | `Short` | `16.25` | 201,750.00 USD | 5,020.00 USD | 0.00 USD | `+39.11%` | `309,000.00` |
| `Live` | `Short` | `16.35` | 203,150.00 USD | 1,390.00 USD | 0.00 USD | `+39.97%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 228,350.00 USD | 25,210.00 USD | 0.00 USD | `+41.68%` | `1,523,000.00` |
| `Live` | `Short` | `16.75` | 228,820.00 USD | 469.00 USD | 0.00 USD | `+43.39%` | `28,000.00` |
| `Live` | `Short` | `16.95` | 374,620.00 USD | 145,790.00 USD | 0.00 USD | `+45.10%` | `8,601,300.00` |
| `Live` | `Short` | `17.15` | 375,980.00 USD | 1,370.00 USD | 0.00 USD | `+46.81%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 376,220.00 USD | 241.50 USD | 0.00 USD | `+47.67%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 471,240.00 USD | 95,020.00 USD | 0.00 USD | `+49.38%` | `5,445,000.00` |
| `Live` | `Short` | `17.65` | 717,770.00 USD | 246,540.00 USD | 0.00 USD | `+51.10%` | `13,968,000.00` |
| `Live` | `Short` | `17.85` | 718,020.00 USD | 249.90 USD | 0.00 USD | `+52.81%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 718,650.00 USD | 621.07 USD | 0.00 USD | `+53.66%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 720,620.00 USD | 1,970.00 USD | 0.00 USD | `+54.52%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 724,510.00 USD | 3,890.00 USD | 0.00 USD | `+57.94%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 724,690.00 USD | 185.50 USD | 0.00 USD | `+58.80%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 724,880.00 USD | 186.50 USD | 0.00 USD | `+59.66%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 2,890,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+61.37%` | `115,048,800.00` |
| `Live` | `Short` | `18.95` | 2,910,000.00 USD | 16,250.00 USD | 0.00 USD | `+62.22%` | `857,700.00` |
| `Live` | `Short` | `19.25` | 2,910,000.00 USD | 319.55 USD | 0.00 USD | `+64.79%` | `16,600.00` |
| `Live` | `Short` | `19.35` | 2,910,000.00 USD | 1,880.00 USD | 0.00 USD | `+65.65%` | `96,900.00` |
| `Live` | `Short` | `19.65` | 2,950,000.00 USD | 39,370.00 USD | 0.00 USD | `+68.22%` | `2,003,700.00` |
| `Live` | `Short` | `19.75` | 2,950,000.00 USD | 422.65 USD | 0.00 USD | `+69.07%` | `21,400.00` |
| `Live` | `Short` | `19.95` | 2,950,000.00 USD | 291.27 USD | 0.00 USD | `+70.78%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,710,000.00 USD | 756,090.00 USD | 0.00 USD | `+71.64%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+75.92%` | `353,000.00` |
| `Live` | `Short` | `20.75` | 3,720,000.00 USD | 168.07 USD | 0.00 USD | `+77.63%` | `8,100.00` |
| `Live` | `Short` | `21.75` | 3,720,000.00 USD | 2,900.00 USD | 0.00 USD | `+86.19%` | `133,300.00` |
| `Live` | `Short` | `21.85` | 3,790,000.00 USD | 74,290.00 USD | 0.00 USD | `+87.05%` | `3,400,000.00` |
| `Live` | `Short` | `22.15` | 4,130,000.00 USD | 336,130.00 USD | 0.00 USD | `+89.62%` | `15,175,000.00` |
| `Live` | `Short` | `22.25` | 4,130,000.00 USD | 890.00 USD | 0.00 USD | `+90.47%` | `40,000.00` |
| `Live` | `Short` | `23.35` | 4,130,000.00 USD | 238.17 USD | 0.00 USD | `+99.89%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 771,010.00 USD | 0.00 USD | 431.68 USD | `-69.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 770,580.00 USD | 0.00 USD | 290.29 USD | `-61.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 770,290.00 USD | 0.00 USD | 120.22 USD | `-55.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 770,170.00 USD | 0.00 USD | 107.09 USD | `-48.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 770,060.00 USD | 0.00 USD | 3,760.00 USD | `-43.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 766,300.00 USD | 0.00 USD | 133.00 USD | `-43.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 766,170.00 USD | 0.00 USD | 3,770.00 USD | `-39.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 762,400.00 USD | 0.00 USD | 2,070.00 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 760,330.00 USD | 0.00 USD | 3,740.00 USD | `-36.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 756,580.00 USD | 0.00 USD | 1,050.00 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 755,530.00 USD | 0.00 USD | 146.80 USD | `-32.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 755,390.00 USD | 0.00 USD | 5,000.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 750,380.00 USD | 0.00 USD | 393.64 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 749,990.00 USD | 0.00 USD | 10,660.00 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 739,320.00 USD | 0.00 USD | 1,360.00 USD | `-27.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 737,970.00 USD | 0.00 USD | 30,250.00 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 707,720.00 USD | 0.00 USD | 186.84 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 707,530.00 USD | 0.00 USD | 742.88 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 706,790.00 USD | 0.00 USD | 196.47 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 706,590.00 USD | 0.00 USD | 1,320.00 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 705,280.00 USD | 0.00 USD | 2,240.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 703,030.00 USD | 0.00 USD | 194.90 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 702,840.00 USD | 0.00 USD | 4,940.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 697,890.00 USD | 0.00 USD | 9,870.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 688,030.00 USD | 0.00 USD | 3,550.00 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 684,480.00 USD | 0.00 USD | 25,950.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 658,530.00 USD | 0.00 USD | 19,100.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 639,430.00 USD | 0.00 USD | 299,650.00 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 339,770.00 USD | 0.00 USD | 2,590.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 337,180.00 USD | 0.00 USD | 1,050.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 336,130.00 USD | 0.00 USD | 2,820.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 333,310.00 USD | 0.00 USD | 6,330.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 326,990.00 USD | 0.00 USD | 19,650.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 307,330.00 USD | 0.00 USD | 5,160.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 302,170.00 USD | 0.00 USD | 4,590.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 297,580.00 USD | 0.00 USD | 5,470.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 292,100.00 USD | 0.00 USD | 3,780.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 288,320.00 USD | 0.00 USD | 3,270.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 285,050.00 USD | 0.00 USD | 18,860.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 266,180.00 USD | 0.00 USD | 26,990.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 239,190.00 USD | 0.00 USD | 47,110.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 192,080.00 USD | 0.00 USD | 12,810.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 179,280.00 USD | 0.00 USD | 48,420.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 130,860.00 USD | 0.00 USD | 11,000.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 119,870.00 USD | 0.00 USD | 119,870.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 10,530.00 USD | 6,070.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 10,690.00 USD | 156.55 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 66,960.00 USD | 56,270.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 68,920.00 USD | 1,960.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 79,340.00 USD | 10,420.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 80,680.00 USD | 1,340.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 80,780.00 USD | 100.84 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 91,890.00 USD | 11,110.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 148,420.00 USD | 56,530.00 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 189,900.00 USD | 41,470.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 210,630.00 USD | 20,730.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 211,090.00 USD | 461.02 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 217,590.00 USD | 6,500.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 218,630.00 USD | 1,050.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 222,480.00 USD | 3,840.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 227,470.00 USD | 4,990.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 241,870.00 USD | 14,400.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 244,500.00 USD | 2,630.00 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 246,520.00 USD | 2,020.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 248,580.00 USD | 2,060.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 248,700.00 USD | 120.50 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 248,970.00 USD | 266.44 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 274,430.00 USD | 25,460.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 275,220.00 USD | 798.06 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 282,210.00 USD | 6,990.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 282,430.00 USD | 218.25 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 285,040.00 USD | 2,610.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 297,970.00 USD | 12,920.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 298,920.00 USD | 950.82 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 310,420.00 USD | 11,500.00 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 314,600.00 USD | 4,180.00 USD | 0.00 USD | `+29.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 547,640.00 USD | 233,040.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 552,030.00 USD | 4,380.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 552,920.00 USD | 893.01 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 553,310.00 USD | 388.75 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 580,360.00 USD | 27,050.00 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 582,700.00 USD | 2,330.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 588,040.00 USD | 5,340.00 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 593,350.00 USD | 5,320.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 602,520.00 USD | 9,170.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 609,320.00 USD | 6,800.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 628,090.00 USD | 18,760.00 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 634,630.00 USD | 6,540.00 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 641,210.00 USD | 6,580.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 651,140.00 USD | 9,930.00 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 664,460.00 USD | 13,320.00 USD | 0.00 USD | `+42.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 678,690.00 USD | 14,240.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 763,050.00 USD | 84,360.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 764,740.00 USD | 1,700.00 USD | 0.00 USD | `+45.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 774,250.00 USD | 9,510.00 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 775,970.00 USD | 1,710.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 778,220.00 USD | 2,250.00 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 876,550.00 USD | 98,330.00 USD | 0.00 USD | `+48.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 898,220.00 USD | 21,670.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 904,650.00 USD | 6,430.00 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 909,060.00 USD | 4,410.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 913,500.00 USD | 4,440.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 917,960.00 USD | 4,460.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 918,410.00 USD | 448.75 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 954,000.00 USD | 35,590.00 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 954,450.00 USD | 453.75 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 955,280.00 USD | 830.38 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 955,740.00 USD | 458.75 USD | 0.00 USD | `+57.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 956,200.00 USD | 461.25 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 960,740.00 USD | 4,540.00 USD | 0.00 USD | `+58.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 961,210.00 USD | 466.25 USD | 0.00 USD | `+59.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 961,680.00 USD | 468.75 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 962,150.00 USD | 471.25 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 962,620.00 USD | 473.75 USD | 0.00 USD | `+62.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,030,000.00 USD | 67,000.00 USD | 0.00 USD | `+63.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,030,000.00 USD | 574.50 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,030,000.00 USD | 577.50 USD | 0.00 USD | `+64.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,030,000.00 USD | 2,710.00 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,030,000.00 USD | 972.50 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,040,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,040,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,050,000.00 USD | 1,690.00 USD | 0.00 USD | `+69.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,050,000.00 USD | 992.50 USD | 0.00 USD | `+69.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,050,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,670,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,670,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+75.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,670,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,670,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,670,000.00 USD | 1,860.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,680,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,680,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,680,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,680,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,680,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,730,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,730,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,730,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,730,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,740,000.00 USD | 3,280.00 USD | 0.00 USD | `+87.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,740,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,740,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,740,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,740,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,740,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,750,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,750,000.00 USD | 1,150.00 USD | 0.00 USD | `+96.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,880,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,880,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,880,000.00 USD | 1,160.00 USD | 0.00 USD | `+99.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,880,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.89%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.29` | 20,160,000.00 USD | 0.00 USD | 20,160,000.00 USD | 93,250.00 USD | 40,640.00 USD | 31,660.00 USD |
| `7D` | `10.31` | 20,000,000.00 USD | 0.00 USD | 20,000,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD |
| `7D` | `10.33` | 19,810,000.00 USD | 0.00 USD | 19,810,000.00 USD | 57,270.00 USD | 28,270.00 USD | 25,780.00 USD |
| `7D` | `10.35` | 19,700,000.00 USD | 0.00 USD | 19,700,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,640.00 USD |
| `7D` | `10.37` | 19,630,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,020.00 USD |
| `7D` | `10.39` | 19,590,000.00 USD | 0.00 USD | 19,590,000.00 USD | 4,240.00 USD | 648.05 USD | 52,550.00 USD |
| `7D` | `10.41` | 19,530,000.00 USD | 0.00 USD | 19,530,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,590.00 USD |
| `7D` | `10.43` | 19,390,000.00 USD | 0.00 USD | 19,390,000.00 USD | 32,710.00 USD | 14,710.00 USD | 14,800.00 USD |
| `7D` | `10.45` | 19,320,000.00 USD | 0.00 USD | 19,320,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,270.00 USD |
| `1D` | `10.46` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 27,560.00 USD | 3,350.00 USD | 16,510.00 USD |
| `7D` | `10.47` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,630.00 USD |
| `1D` | `10.48` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 12,430.00 USD | 4,740.00 USD | 12,890.00 USD |
| `7D` | `10.49` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 22,510.00 USD | 183.20 USD | 24,780.00 USD |
| `1D` | `10.50` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 23,170.00 USD | 9,270.00 USD | 8,180.00 USD |
| `7D` | `10.51` | 19,110,000.00 USD | 0.00 USD | 19,110,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,780.00 USD |
| `1D` | `10.52` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 22,760.00 USD | 3,770.00 USD | 3,080.00 USD |
| `7D` | `10.53` | 19,020,000.00 USD | 0.00 USD | 19,020,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,100.00 USD |
| `1D` | `10.54` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 715.66 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `10.55` | 18,980,000.00 USD | 0.00 USD | 18,980,000.00 USD | 55,490.00 USD | 18,800.00 USD | 20,820.00 USD |
| `1D` | `10.56` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 22,600.00 USD | 5,790.00 USD | 1,810.00 USD |
| `7D` | `10.57` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,400.00 USD |
| `1D` | `10.58` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 16,870.00 USD | 5,420.00 USD | 8,210.00 USD |
| `7D` | `10.59` | 18,770,000.00 USD | 0.00 USD | 18,770,000.00 USD | 33,510.00 USD | 9,440.00 USD | 4,330.00 USD |
| `1D` | `10.60` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD |
| `7D` | `10.61` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 26,680.00 USD | 10,560.00 USD | 10,060.00 USD |
| `1D` | `10.62` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD |
| `7D` | `10.63` | 18,680,000.00 USD | 0.00 USD | 18,680,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,810.00 USD |
| `1D` | `10.64` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD |
| `7D` | `10.65` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 6,380.00 USD | 2,920.00 USD | 189.57 USD |
| `1D` | `10.66` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD |
| `7D` | `10.67` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,280.00 USD |
| `1D` | `10.68` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.69` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 18,290.00 USD | 0.00 USD | 5,520.00 USD |
| `1D` | `10.70` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `10.71` | 18,540,000.00 USD | 0.00 USD | 18,540,000.00 USD | 14,600.00 USD | 0.00 USD | 7,890.00 USD |
| `1D` | `10.72` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD |
| `7D` | `10.73` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 28,700.00 USD | 5,730.00 USD | 147.96 USD |
| `1D` | `10.74` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD |
| `7D` | `10.75` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 17,290.00 USD | 4,010.00 USD | 332.91 USD |
| `1D` | `10.76` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD |
| `7D` | `10.77` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 16,290.00 USD | 3,960.00 USD | 8,940.00 USD |
| `1D` | `10.78` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD |
| `7D` | `10.79` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 57,970.00 USD | 1,400.00 USD | 24,960.00 USD |
| `1D` | `10.80` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD |
| `7D` | `10.81` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 86,860.00 USD | 28,970.00 USD | 60,610.00 USD |
| `1D` | `10.82` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD |
| `7D` | `10.83` | 18,170,000.00 USD | 0.00 USD | 18,170,000.00 USD | 123,460.00 USD | 23,810.00 USD | 45,240.00 USD |
| `1D` | `10.84` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD |
| `7D` | `10.85` | 17,980,000.00 USD | 0.00 USD | 17,980,000.00 USD | 231,910.00 USD | 23,820.00 USD | 83,070.00 USD |
| `1D` | `10.86` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 976.86 USD | 4,520.00 USD | 3,820.00 USD |
| `7D` | `10.87` | 17,640,000.00 USD | 0.00 USD | 17,640,000.00 USD | 82,290.00 USD | 41,310.00 USD | 99,600.00 USD |
| `1D` | `10.88` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 1,820.00 USD | 10,400.00 USD | 16,270.00 USD |
| `7D` | `10.89` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 235,210.00 USD | 62,890.00 USD | 175,540.00 USD |
| `1D` | `10.90` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 1,120.00 USD | 3,770.00 USD | 26,480.00 USD |
| `7D` | `10.91` | 16,940,000.00 USD | 0.00 USD | 16,940,000.00 USD | 271,580.00 USD | 48,930.00 USD | 212,370.00 USD |
| `1D` | `10.92` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 66,180.00 USD | 28,790.00 USD | 58,360.00 USD |
| `7D` | `10.93` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 395,920.00 USD | 107,040.00 USD | 316,190.00 USD |
| `1D` | `10.94` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 46,880.00 USD | 17,110.00 USD | 5,770.00 USD |
| `7D` | `10.95` | 15,590,000.00 USD | 0.00 USD | 15,590,000.00 USD | 308,350.00 USD | 107,220.00 USD | 304,990.00 USD |
| `1D` | `10.96` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD |
| `7D` | `10.97` | 14,870,000.00 USD | 0.00 USD | 14,870,000.00 USD | 165,580.00 USD | 96,900.00 USD | 115,040.00 USD |
| `1D` | `10.98` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD |
| `7D` | `10.99` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 94,430.00 USD | 117,780.00 USD | 249,060.00 USD |
| `1D` | `11.00` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD |
| `7D` | `11.01` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 141,200.00 USD | 39,420.00 USD | 103,810.00 USD |
| `1D` | `11.02` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD |
| `7D` | `11.03` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 423,180.00 USD | 178,040.00 USD | 208,020.00 USD |
| `1D` | `11.04` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD |
| `7D` | `11.05` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 260,170.00 USD | 70,790.00 USD | 155,560.00 USD |
| `1D` | `11.06` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,400.00 USD |
| `7D` | `11.07` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 437,450.00 USD | 53,630.00 USD | 223,610.00 USD |
| `1D` | `11.08` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 28,900.00 USD | 15,060.00 USD | 29,500.00 USD |
| `7D` | `11.09` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 170,080.00 USD | 126,860.00 USD | 397,860.00 USD |
| `1D` | `11.10` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 31,390.00 USD | 30,270.00 USD | 32,430.00 USD |
| `7D` | `11.11` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 575,850.00 USD | 145,120.00 USD | 441,990.00 USD |
| `1D` | `11.12` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 52,580.00 USD | 33,090.00 USD | 75,810.00 USD |
| `7D` | `11.13` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 618,260.00 USD | 148,900.00 USD | 476,300.00 USD |
| `1D` | `11.14` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD |
| `7D` | `11.15` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 809,230.00 USD | 195,340.00 USD | 593,040.00 USD |
| `1D` | `11.16` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD |
| `7D` | `11.17` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 527,700.00 USD | 265,230.00 USD | 520,640.00 USD |
| `1D` | `11.18` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 137,180.00 USD | 48,450.00 USD | 63,580.00 USD |
| `7D` | `11.19` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 597,320.00 USD | 155,670.00 USD | 279,220.00 USD |
| `1D` | `11.20` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 222,000.00 USD | 52,070.00 USD | 99,010.00 USD |
| `7D` | `11.21` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 319,760.00 USD | 249,060.00 USD | 282,700.00 USD |
| `1D` | `11.22` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 97,140.00 USD | 33,850.00 USD | 37,230.00 USD |
| `7D` | `11.23` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 201,470.00 USD | 197,890.00 USD | 58,370.00 USD |
| `1D` | `11.24` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 102,960.00 USD | 56,970.00 USD | 70,490.00 USD |
| `7D` | `11.25` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 332,220.00 USD | 106,830.00 USD | 101,020.00 USD |
| `1D` | `11.26` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 189,710.00 USD | 42,840.00 USD | 55,920.00 USD |
| `7D` | `11.27` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 181,530.00 USD | 128,400.00 USD | 101,750.00 USD |
| `1D` | `11.28` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 44,920.00 USD | 13,050.00 USD | 49,880.00 USD |
| `7D` | `11.29` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 104,970.00 USD | 43,570.00 USD | 55,980.00 USD |
| `1D` | `11.30` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD |
| `7D` | `11.31` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 13,590.00 USD | 95,360.00 USD |
| `1D` | `11.32` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD |
| `7D` | `11.33` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 190,980.00 USD | 11,560.00 USD | 18,940.00 USD |
| `1D` | `11.34` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD |
| `7D` | `11.35` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 310,190.00 USD | 58,690.00 USD | 0.00 USD |
| `1D` | `11.36` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD |
| `7D` | `11.37` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 44,290.00 USD | 10,650.00 USD | 99,100.00 USD |
| `1D` | `11.38` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD |
| `7D` | `11.39` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 142,620.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD |
| `7D` | `11.41` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 34,370.00 USD | 14,250.00 USD | 34,700.00 USD |
| `1D` | `11.42` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 106,690.00 USD | 45,130.00 USD | 70,800.00 USD |
| `7D` | `11.43` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 133,220.00 USD | 29,480.00 USD | 55,710.00 USD |
| `1D` | `11.44` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 130,750.00 USD | 52,380.00 USD | 84,430.00 USD |
| `7D` | `11.45` | 889,150.00 USD | 0.00 USD | 889,150.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 952,480.00 USD | 0.00 USD | 952,480.00 USD | 177,600.00 USD | 34,920.00 USD | 24,850.00 USD |
| `7D` | `11.47` | 634,620.00 USD | 0.00 USD | 634,620.00 USD | 17,370.00 USD | 14,370.00 USD | 38,770.00 USD |
| `1D` | `11.48` | 715,100.00 USD | 0.00 USD | 715,100.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD |
| `7D` | `11.49` | 564,120.00 USD | 0.00 USD | 564,120.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD |
| `1D` | `11.50` | 637,750.00 USD | 0.00 USD | 637,750.00 USD | 83,540.00 USD | 39,490.00 USD | 14,300.00 USD |
| `7D` | `11.51` | 531,000.00 USD | 0.00 USD | 531,000.00 USD | 40,840.00 USD | 33,270.00 USD | 37,240.00 USD |
| `1D` | `11.52` | 500,420.00 USD | 0.00 USD | 500,420.00 USD | 13,090.00 USD | 28,340.00 USD | 46,330.00 USD |
| `7D` | `11.53` | 419,650.00 USD | 0.00 USD | 419,650.00 USD | 34,770.00 USD | 4,270.00 USD | 0.00 USD |
| `1D` | `11.54` | 412,660.00 USD | 0.00 USD | 412,660.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD |
| `7D` | `11.55` | 380,610.00 USD | 0.00 USD | 380,610.00 USD | 0.00 USD | 55,650.00 USD | 51,530.00 USD |
| `1D` | `11.56` | 390,070.00 USD | 0.00 USD | 390,070.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD |
| `7D` | `11.57` | 273,430.00 USD | 0.00 USD | 273,430.00 USD | 0.00 USD | 0.00 USD | 69,500.00 USD |
| `1D` | `11.58` | 231,100.00 USD | 0.00 USD | 231,100.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD |
| `7D` | `11.59` | 203,930.00 USD | 0.00 USD | 203,930.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.60` | 149,470.00 USD | 0.00 USD | 149,470.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD |
| `1D` | `11.62` | 42,070.00 USD | 0.00 USD | 42,070.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD |
| `7D` | `11.63` | 181,160.00 USD | 0.00 USD | 181,160.00 USD | 34,910.00 USD | 57,280.00 USD | 0.00 USD |
| `7D` | `11.65` | 88,970.00 USD | 0.00 USD | 88,970.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD |
| `7D` | `11.67` | 66,610.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 4,270.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 28,150.00 USD | 0.00 USD | 28,150.00 USD | 0.00 USD | 294.87 USD | 27,620.00 USD |
| `7D` | `11.69` | 381.10 USD | 0.00 USD | 381.10 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.70` | 230.72 USD | 0.00 USD | 230.72 USD | 0.00 USD | 230.72 USD | 0.00 USD |
| `7D` | `11.71` | 195,940.00 USD | 195,940.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `7D` | `11.71` | 391,880.00 USD | 391,880.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.72` | 177,420.00 USD | 177,420.00 USD | 0.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD |
| `1D` | `11.72` | 354,830.00 USD | 354,830.00 USD | 0.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD |
| `1D` | `11.74` | 355,160.00 USD | 355,160.00 USD | 0.00 USD | 0.00 USD | 324.58 USD | 0.00 USD |
| `7D` | `11.75` | 409,270.00 USD | 409,270.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.76` | 355,500.00 USD | 355,500.00 USD | 0.00 USD | 0.00 USD | 342.56 USD | 0.00 USD |
| `7D` | `11.77` | 440,070.00 USD | 440,070.00 USD | 0.00 USD | 30,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 372,530.00 USD | 372,530.00 USD | 0.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD |
| `7D` | `11.79` | 515,480.00 USD | 515,480.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.80` | 373,590.00 USD | 373,590.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `11.81` | 679,990.00 USD | 679,990.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.83` | 744,310.00 USD | 744,310.00 USD | 0.00 USD | 58,850.00 USD | 5,340.00 USD | 136.58 USD |
| `1D` | `11.84` | 457,510.00 USD | 457,510.00 USD | 0.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD |
| `7D` | `11.85` | 962,280.00 USD | 962,280.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 50.04 USD |
| `1D` | `11.86` | 529,670.00 USD | 529,670.00 USD | 0.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD |
| `7D` | `11.87` | 991,260.00 USD | 991,260.00 USD | 0.00 USD | 438.10 USD | 5,400.00 USD | 23,140.00 USD |
| `1D` | `11.88` | 613,130.00 USD | 613,130.00 USD | 0.00 USD | 19,640.00 USD | 25,990.00 USD | 37,840.00 USD |
| `7D` | `11.89` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 40,020.00 USD | 16,380.00 USD | 140.80 USD |
| `1D` | `11.90` | 679,130.00 USD | 679,130.00 USD | 0.00 USD | 44,160.00 USD | 8,730.00 USD | 13,110.00 USD |
| `7D` | `11.91` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | 135.84 USD |
| `1D` | `11.92` | 756,380.00 USD | 756,380.00 USD | 0.00 USD | 59,860.00 USD | 17,360.00 USD | 20.02 USD |
| `7D` | `11.93` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,910.00 USD |
| `1D` | `11.94` | 801,960.00 USD | 801,960.00 USD | 0.00 USD | 1,220.00 USD | 15,870.00 USD | 28,480.00 USD |
| `7D` | `11.95` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 885,440.00 USD | 885,440.00 USD | 0.00 USD | 21,600.00 USD | 34,030.00 USD | 27,850.00 USD |
| `7D` | `11.97` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 354,730.00 USD | 35,140.00 USD | 213,110.00 USD |
| `1D` | `11.98` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 43,720.00 USD | 7,680.00 USD | 67,590.00 USD |
| `7D` | `11.99` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 242,400.00 USD | 3,330.00 USD | 119,860.00 USD |
| `1D` | `12.00` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD |
| `7D` | `12.01` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 164,140.00 USD | 5,360.00 USD | 219,520.00 USD |
| `1D` | `12.02` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD |
| `7D` | `12.03` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 321,170.00 USD | 140,540.00 USD | 192,590.00 USD |
| `1D` | `12.04` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD |
| `7D` | `12.05` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 330,170.00 USD | 106,020.00 USD | 188,410.00 USD |
| `1D` | `12.06` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD |
| `7D` | `12.07` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,230.00 USD |
| `1D` | `12.08` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD |
| `7D` | `12.09` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,410.00 USD |
| `1D` | `12.10` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD |
| `7D` | `12.11` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 84,910.00 USD | 74,760.00 USD | 111,140.00 USD |
| `1D` | `12.12` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 141,930.00 USD | 54,500.00 USD | 58,820.00 USD |
| `7D` | `12.13` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 148,530.00 USD | 63,030.00 USD | 36,210.00 USD |
| `1D` | `12.14` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 109,520.00 USD | 33,030.00 USD | 55,720.00 USD |
| `7D` | `12.15` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 310,620.00 USD | 114,540.00 USD | 131,290.00 USD |
| `1D` | `12.16` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 96,770.00 USD | 60,930.00 USD | 53,300.00 USD |
| `7D` | `12.17` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 26,820.00 USD | 61,400.00 USD | 53,190.00 USD |
| `1D` | `12.18` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 108,930.00 USD | 37,270.00 USD | 33,450.00 USD |
| `7D` | `12.19` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 196,200.00 USD | 58,210.00 USD | 79,590.00 USD |
| `1D` | `12.20` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 93,920.00 USD | 37,400.00 USD | 25,360.00 USD |
| `7D` | `12.21` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 115,750.00 USD |
| `1D` | `12.22` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 20,470.00 USD | 37,270.00 USD | 48,330.00 USD |
| `7D` | `12.23` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 140,270.00 USD | 19,410.00 USD | 56,930.00 USD |
| `1D` | `12.24` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 34,030.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.25` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 134,500.00 USD | 56,330.00 USD | 103,140.00 USD |
| `1D` | `12.26` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 55,900.00 USD | 27,170.00 USD | 21,450.00 USD |
| `7D` | `12.27` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 141,400.00 USD | 49,260.00 USD | 64,040.00 USD |
| `1D` | `12.28` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 99,610.00 USD | 24,800.00 USD | 37,620.00 USD |
| `7D` | `12.29` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,260.00 USD |
| `1D` | `12.30` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 57,120.00 USD | 24,040.00 USD | 45,400.00 USD |
| `7D` | `12.31` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 135,150.00 USD | 53,480.00 USD | 55,160.00 USD |
| `1D` | `12.32` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.33` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 179,300.00 USD | 89,700.00 USD | 5,080.00 USD |
| `1D` | `12.34` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD |
| `7D` | `12.35` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 116,830.00 USD | 15,980.00 USD | 19,350.00 USD |
| `1D` | `12.36` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD |
| `7D` | `12.37` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 32,750.00 USD | 24,960.00 USD | 12,470.00 USD |
| `1D` | `12.38` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD |
| `7D` | `12.39` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 160,660.00 USD | 42,540.00 USD | 338,640.00 USD |
| `1D` | `12.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD |
| `7D` | `12.41` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 80,100.00 USD | 32,410.00 USD | 195,410.00 USD |
| `1D` | `12.42` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 51,980.00 USD | 13,980.00 USD | 9,730.00 USD |
| `7D` | `12.43` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 333,860.00 USD |
| `1D` | `12.44` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.45` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 57,130.00 USD | 118,850.00 USD | 259,000.00 USD |
| `1D` | `12.46` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 411.51 USD | 15,260.00 USD | 11,560.00 USD |
| `7D` | `12.47` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 66,870.00 USD | 29,080.00 USD | 192,390.00 USD |
| `1D` | `12.48` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 1,590.00 USD | 2,560.00 USD | 8,350.00 USD |
| `7D` | `12.49` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 91,900.00 USD | 17,840.00 USD | 60,440.00 USD |
| `1D` | `12.50` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 620.31 USD | 4,320.00 USD | 8,230.00 USD |
| `7D` | `12.51` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 136,260.00 USD | 26,650.00 USD | 85,940.00 USD |
| `1D` | `12.52` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD |
| `7D` | `12.53` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,100.00 USD |
| `1D` | `12.54` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD |
| `7D` | `12.55` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,070.00 USD |
| `1D` | `12.56` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.57` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 125,630.00 USD | 65,650.00 USD | 10,590.00 USD |
| `1D` | `12.58` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD |
| `7D` | `12.59` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 65,910.00 USD | 17,430.00 USD | 36,710.00 USD |
| `1D` | `12.60` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD |
| `7D` | `12.61` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 41,220.00 USD | 29,650.00 USD | 58,910.00 USD |
| `1D` | `12.62` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.63` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 62,580.00 USD | 28,520.00 USD | 81,350.00 USD |
| `1D` | `12.64` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD |
| `7D` | `12.65` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 76,240.00 USD | 26,110.00 USD | 131,410.00 USD |
| `1D` | `12.66` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD |
| `7D` | `12.67` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 66,110.00 USD | 19,940.00 USD | 223,870.00 USD |
| `1D` | `12.68` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD |
| `7D` | `12.69` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 44,600.00 USD | 34,670.00 USD | 154,100.00 USD |
| `1D` | `12.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD |
| `7D` | `12.71` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 31,960.00 USD | 43,220.00 USD | 24,420.00 USD |
| `1D` | `12.72` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD |
| `7D` | `12.73` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 86,650.00 USD |
| `1D` | `12.74` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD |
| `7D` | `12.75` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 33,680.00 USD | 14,710.00 USD | 14,830.00 USD |
| `1D` | `12.76` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD |
| `7D` | `12.77` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 36,060.00 USD | 11,060.00 USD | 42,380.00 USD |
| `1D` | `12.78` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.79` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 56,200.00 USD | 22,760.00 USD | 6,720.00 USD |
| `1D` | `12.80` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 12,430.00 USD | 4,740.00 USD | 12,890.00 USD |
| `7D` | `12.81` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `12.82` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 2,680.00 USD | 3,450.00 USD | 1,990.00 USD |
| `7D` | `12.83` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 4,950.00 USD |
| `1D` | `12.84` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 20,500.00 USD | 5,820.00 USD | 6,190.00 USD |
| `7D` | `12.85` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,700.00 USD |
| `1D` | `12.86` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 22,760.00 USD | 3,770.00 USD | 3,050.00 USD |
| `7D` | `12.87` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 10,160.00 USD | 6,560.00 USD | 21,060.00 USD |
| `1D` | `12.88` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 91.75 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `12.89` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD |
| `1D` | `12.90` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 21,720.00 USD | 5,790.00 USD | 1,810.00 USD |
| `7D` | `12.91` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 23,290.00 USD |
| `1D` | `12.92` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 3,090.00 USD | 4,130.00 USD | 8,200.00 USD |
| `7D` | `12.93` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 76.10 USD |
| `1D` | `12.94` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.95` | 14,330,000.00 USD | 14,330,000.00 USD | 0.00 USD | 2,290.00 USD | 9,210.00 USD | 4,180.00 USD |
| `1D` | `12.96` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,100.00 USD |
| `7D` | `12.97` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 15,020.00 USD | 10,560.00 USD | 9,910.00 USD |
| `1D` | `12.98` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 24,650.00 USD | 6,900.00 USD | 11,950.00 USD |
| `7D` | `12.99` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,720.00 USD |
| `1D` | `13.00` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 16,930.00 USD | 7,680.00 USD | 16,490.00 USD |
| `7D` | `13.01` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 2,070.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `13.03` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD |
| `7D` | `13.07` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `13.09` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `13.11` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD |
| `7D` | `13.13` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,410.00 USD |
| `7D` | `13.19` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 14,540,000.00 USD | 14,540,000.00 USD | 0.00 USD | 13,890.00 USD | 259.77 USD | 8,970.00 USD |
| `7D` | `13.23` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 15,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.25` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 18,020.00 USD | 4,640.00 USD | 11,590.00 USD |
| `7D` | `13.27` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 10,290.00 USD | 8,420.00 USD | 10,920.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `559.24M` | Total OI Tokens: `47,697,770.3 LINK`
  * 1h OI Change: `+0.72%` | 4h OI Change: `-1.72%` | 24h OI Change: `-1.96%`
  * Exchange Breakdown: Binance=`105.99M` | Bybit=`65.90M` | OKX=`26.52M` | Hyperliquid=`56.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.45K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0031%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0050%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `56.11%` | `43.89%` | `1.28` | 5,880,000.00 USD |
| `15M` | `Binance` | `50.79%` | `49.21%` | `1.03` | 1,410,000.00 USD |
| `15M` | `OKX` | `80.53%` | `19.47%` | `4.14` | 993,070.00 USD |
| `15M` | `Bybit` | `68.86%` | `31.14%` | `2.21` | 316,900.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `39.77%` | `60.23%` | `0.66` | 121,070.00 USD |
| `15M` | `Bitget` | `57.4%` | `42.6%` | `1.35` | 261,990.00 USD |
| `15M` | `BingX` | `62.56%` | `37.44%` | `1.67` | 121,170.00 USD |
| `15M` | `MEXC` | `50.78%` | `49.22%` | `1.03` | 2,090,000.00 USD |
| `15M` | `Bitunix` | `63.46%` | `36.54%` | `1.74` | 84,090.00 USD |
| `15M` | `Hyperliquid` | `64.34%` | `35.66%` | `1.80` | 109,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.96%` | `46.04%` | `1.17` | 101,790.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.35%` | `99.65%` | `0.00` | 208,610.00 USD |
| `15M` | `HTX` | `90.34%` | `9.66%` | `9.35` | 5,260.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.51%` | `26.49%` | `2.78` | 22,580.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 7,500.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `92.64%` | `7.36%` | `12.59` | 17,390.00 USD |
| `15M` | `Whale Positions` | `50.79%` | `49.21%` | `1.03` | 1,410,000.00 USD |
| `15M` | `Global Accounts` | `56.11%` | `43.89%` | `1.28` | 5,880,000.00 USD |
| `1H` | `LINK` | `51.72%` | `48.28%` | `1.07` | 20,110,000.00 USD |
| `1H` | `Binance` | `53.07%` | `46.93%` | `1.13` | 5,240,000.00 USD |
| `1H` | `OKX` | `63.69%` | `36.31%` | `1.75` | 1,930,000.00 USD |
| `1H` | `Bybit` | `50.2%` | `49.8%` | `1.01` | 1,180,000.00 USD |
| `1H` | `KuCoin` | `53.61%` | `46.39%` | `1.16` | 37,120.00 USD |
| `1H` | `Gate` | `43.5%` | `56.5%` | `0.77` | 190,110.00 USD |
| `1H` | `Bitget` | `57.69%` | `42.31%` | `1.36` | 543,540.00 USD |
| `1H` | `BingX` | `43.31%` | `56.69%` | `0.76` | 1,040,000.00 USD |
| `1H` | `MEXC` | `51.52%` | `48.48%` | `1.06` | 8,000,000.00 USD |
| `1H` | `Bitunix` | `68.31%` | `31.69%` | `2.16` | 438,230.00 USD |
| `1H` | `Hyperliquid` | `58.06%` | `41.94%` | `1.38` | 173,670.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.62%` | `48.38%` | `1.07` | 395,570.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.92%` | `84.08%` | `0.19` | 762,720.00 USD |
| `1H` | `HTX` | `84.8%` | `15.2%` | `5.58` | 5,930.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `36.07%` | `63.93%` | `0.56` | 132,130.00 USD |
| `1H` | `Aster` | `95.92%` | `4.08%` | `23.51` | 9,110.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.63%` | `31.37%` | `2.19` | 34,270.00 USD |
| `1H` | `Whale Positions` | `53.07%` | `46.93%` | `1.13` | 5,240,000.00 USD |
| `1H` | `Global Accounts` | `51.72%` | `48.28%` | `1.07` | 20,110,000.00 USD |
| `4H` | `LINK` | `46.22%` | `53.78%` | `0.86` | 99,640,000.00 USD |
| `4H` | `Binance` | `47.57%` | `52.43%` | `0.91` | 28,550,000.00 USD |
| `4H` | `OKX` | `42.33%` | `57.67%` | `0.73` | 8,100,000.00 USD |
| `4H` | `Bybit` | `46.71%` | `53.29%` | `0.88` | 6,340,000.00 USD |
| `4H` | `KuCoin` | `51.14%` | `48.86%` | `1.05` | 841,390.00 USD |
| `4H` | `Gate` | `48.21%` | `51.79%` | `0.93` | 1,180,000.00 USD |
| `4H` | `Bitget` | `44.3%` | `55.7%` | `0.80` | 2,470,000.00 USD |
| `4H` | `BingX` | `45.48%` | `54.52%` | `0.83` | 3,960,000.00 USD |
| `4H` | `MEXC` | `49.32%` | `50.68%` | `0.97` | 35,580,000.00 USD |
| `4H` | `Bitunix` | `49.94%` | `50.06%` | `1.00` | 3,930,000.00 USD |
| `4H` | `Hyperliquid` | `38.46%` | `61.54%` | `0.62` | 2,490,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.09%` | `50.91%` | `0.96` | 2,260,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `6.79%` | `93.21%` | `0.07` | 2,910,000.00 USD |
| `4H` | `HTX` | `66.14%` | `33.86%` | `1.95` | 46,120.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.27%` | `58.73%` | `0.70` | 574,900.00 USD |
| `4H` | `Aster` | `34.4%` | `65.6%` | `0.52` | 311,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.7%` | `57.3%` | `0.75` | 97,140.00 USD |
| `4H` | `Whale Positions` | `47.57%` | `52.43%` | `0.91` | 28,550,000.00 USD |
| `4H` | `Global Accounts` | `46.22%` | `53.78%` | `0.86` | 99,640,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.80` | `11.80` | `11.80` | `11.83` | `11.79` | 889,528.52 USD | 480,169.70 USD | 409,358.82 USD | 70,810.88 USD | `+7.96%` | `8B / 3S` |
| `0:00 UTC` | `11.78` | `11.76` | `11.78` | `11.84` | `11.71` | 1,746,825.55 USD | 823,777.15 USD | 923,048.41 USD | -99,271.26 USD | `-5.68%` | `22B / 37S` |
| `5:00 UTC` | `11.71` | `11.70` | `11.71` | `11.74` | `11.66` | 1,705,508.25 USD | 855,092.75 USD | 850,415.50 USD | 4,677.25 USD | `+0.27%` | `14B / 10S` |
| `0:00 UTC` | `11.73` | `11.73` | `11.73` | `11.75` | `11.71` | 756,364.68 USD | 311,101.50 USD | 445,263.18 USD | -134,161.69 USD | `-17.74%` | `6B / 13S` |
| `5:00 UTC` | `11.74` | `11.73` | `11.74` | `11.76` | `11.69` | 1,033,883.46 USD | 539,127.77 USD | 494,755.69 USD | 44,372.08 USD | `+4.29%` | `15B / 13S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.68` | `11.66` | `11.68` | `11.68` | `11.63` | 997,243.09 USD | 360,139.33 USD | 637,103.76 USD | -276,964.43 USD | `-27.77%` | `11B / 15S` |
| `0:00 UTC` | `11.68` | `11.68` | `11.68` | `11.68` | `11.68` | 1,132.85 USD | 1,132.85 USD | 0.00 USD | 1,132.85 USD | `+100.00%` | `0B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -12,680.00 USD | 639,530.00 USD | **`ACCUMULATION`** |
| `15m` | -30,530.00 USD | 723,440.00 USD | **`ACCUMULATION`** |
| `30m` | -78,670.00 USD | 242,270.00 USD | **`ACCUMULATION`** |
| `1h` | -92,560.00 USD | 903,560.00 USD | **`ACCUMULATION`** |
| `2h` | -543,720.00 USD | -815,930.00 USD | **`DISTRIBUTION`** |
| `4h` | -461,740.00 USD | -2,470,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 263,400.00 USD | -382,270.00 USD | **`DISTRIBUTION`** |
| `8h` | 315,460.00 USD | -69,370.00 USD | **`ACCUMULATION`** |
| `12h` | 110,800.00 USD | 513,570.00 USD | **`ACCUMULATION`** |
| `24h` | 543,260.00 USD | -3,270,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,070,000.00 USD | -23,460,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -69,010,000.00 USD | -187,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.68K` | 15m=`-30.53K` | 1h=`-92.56K` | 24h=`+543.26K`
* Futures Capital Netflows: 5m=`+639.53K` | 15m=`+723.44K` | 1h=`+903.56K` | 24h=`-3.27M`
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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.44` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `11.23` (Risk Distance: `0.2140` pts)
  * +2.5R Take Profit: `11.98`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.12` (Risk Distance: `0.2140` pts)
  * +2.5R Take Profit: `11.37`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.81`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
