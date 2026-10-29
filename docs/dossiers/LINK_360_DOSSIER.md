# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 00:23:15 IST` (`2026-10-29 18:53:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.61` | **Live Ask Quote**: `11.70` | **Mid Price**: `11.65`
- **Spread Points**: `87.00` | **Spread BPS**: `74.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.57` | VWAP Z-Score: `+0.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0744` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.11` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.11` | Lower -3.00σ Band: `11.02`
  * Upper +2.51σ Band: `12.02` | Lower -2.51σ Band: `11.11`
  * Upper +2.01σ Band: `11.93` | Lower -2.01σ Band: `11.20`
  * Upper +2.00σ Band: `11.93` | Lower -2.00σ Band: `11.20`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.33`
  * Upper +1.00σ Band: `11.75` | Lower -1.00σ Band: `11.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.70` | EMA-20=`11.70` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.64` (Slope: `+0.0000`) | EMA-100=`11.59`
  * Institutional Anchors: EMA-144=`11.57` | EMA-200=`11.53` (Slope: `+0.2439`) | EMA-233=`11.51`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`11.23` | Weekly High=`11.96` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.91` (Distance: `-2.10%`)
  * Point of Control (POC) = `11.77` (Distance: `-0.97%`)
  * Value Area Low (VAL) = `11.44` (Distance: `+1.93%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.57` | Weekly POC=`11.41` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.96` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.61` - `11.70`
  * Optimal Trade Entry (OTE 0.705): `11.68`
  * Structural Invalidation Anchor (0.786): `11.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.72` | `11.73` | `11.69` | `11.70` | `34,086` | 398,945.43 USD | -70,093.07 USD | `-17.57%` | -92,576.55 USD | `-0.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.70` | `11.71` | `11.62` | `11.65` | `105,034` | 1,223,772.09 USD | -167,001.69 USD | `-13.65%` | -259,578.24 USD | `-1.42` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `11.65` | `11.65` | `11.64` | `11.64` | `3,629` | 42,263.02 USD | 1,409.54 USD | `+3.34%` | -258,168.70 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.74` | `11.75` | `11.71` | `11.74` | `64,493` | 756,364.68 USD | -134,161.69 USD | `-17.74%` | -247,680.30 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.74` | `11.76` | `11.69` | `11.70` | `88,177` | 1,033,883.46 USD | 44,372.08 USD | `+4.29%` | -203,308.22 USD | `+0.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.70` | `11.71` | `11.62` | `11.64` | `108,654` | 1,265,925.08 USD | -165,702.19 USD | `-13.09%` | -369,010.41 USD | `-0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.96` | `12.01` | `11.82` | `11.86` | `812,884` | 9,680,116.17 USD | -943,322.93 USD | `-9.74%` | 70,235.30 USD | `-1.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.86` | `11.87` | `11.66` | `11.74` | `476,252` | 5,603,289.28 USD | -228,969.33 USD | `-4.09%` | -158,734.04 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.64` | `261,218` | 3,054,951.99 USD | -255,734.22 USD | `-8.37%` | -414,468.26 USD | `-0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.64` | `1,550,459` | 18,339,578.66 USD | -1,427,784.06 USD | `-7.79%` | -881,600.94 USD | `-0.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.66` | `1,659,924` | 19,614,448.04 USD | -1,377,418.36 USD | `-7.02%` | -831,235.25 USD | `-0.93` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.65`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `493` | `0x73ce...8ce9` | `LONG` | 4,661,435.18 USD | `400,011,600.00` | `12.05` | `11.64` | `9.13` | -158,318.53 USD | `-3.40%` | `5X Cross` |
| `640` | `0x5b5d...c060` | `SHORT` | 3,630,386.62 USD | `311,728,200.00` | `13.61` | `11.64` | `497.68` | 611,745.49 USD | `+16.85%` | `3X Cross` |
| `645` | `0xb83d...6e36` | `SHORT` | 3,590,972.29 USD | `308,152,000.00` | `12.93` | `11.64` | `422.77` | 394,281.20 USD | `+10.98%` | `3X Cross` |
| `866` | `0x458d...ab3b` | `LONG` | 2,646,375.56 USD | `227,156,700.00` | `13.13` | `11.64` | `9.34` | -335,854.84 USD | `-12.69%` | `3X Isolated` |
| `950` | `0xdd53...2b13` | `SHORT` | 2,403,991.92 USD | `206,475,300.00` | `11.92` | `11.64` | `274.78` | 57,231.01 USD | `+2.38%` | `3X Cross` |
| `980` | `0x3dc9...54b0` | `SHORT` | 2,331,000.00 USD | `200,000,000.00` | `7.56` | `11.64` | `81.41` | -819,841.58 USD | `-35.17%` | `10X Cross` |
| `1001` | `0x45d2...4029` | `SHORT` | 2,275,815.50 USD | `195,500,000.00` | `11.54` | `11.64` | `191.73` | -19,332.07 USD | `-0.85%` | `10X Cross` |
| `1194` | `0x6540...f7b7` | `LONG` | 1,910,045.79 USD | `164,051,000.00` | `12.48` | `11.64` | `8.01` | -136,770.59 USD | `-7.16%` | `5X Isolated` |
| `1247` | `0xeadc...9d55` | `LONG` | 1,836,476.37 USD | `157,691,600.00` | `9.43` | `11.64` | `0.000000` | 349,821.47 USD | `+19.05%` | `10X Cross` |
| `1610` | `0x9df2...c665` | `SHORT` | 1,374,574.25 USD | `117,956,300.00` | `11.48` | `11.64` | `250.72` | -19,973.74 USD | `-1.45%` | `10X Cross` |
| `1631` | `0xf6f3...47f8` | `SHORT` | 1,339,461.47 USD | `115,024,600.00` | `11.42` | `11.64` | `18.84` | -26,131.28 USD | `-1.95%` | `5X Cross` |
| `1796` | `0xfe7e...11b4` | `LONG` | 1,177,899.73 USD | `101,142,000.00` | `14.47` | `11.64` | `5.33` | -285,213.42 USD | `-24.21%` | `5X Isolated` |
| `1827` | `0x8af7...fa05` | `SHORT` | 1,149,008.34 USD | `98,661,200.00` | `14.08` | `11.64` | `203.28` | 240,174.20 USD | `+20.90%` | `10X Cross` |
| `1882` | `0xb7ec...5166` | `LONG` | 1,100,732.17 USD | `94,515,900.00` | `9.01` | `11.64` | `7.20` | 248,871.59 USD | `+22.61%` | `4X Cross` |

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
  * 24H Horizon: Short MP=`12.05` (Vol: 117,000.00 USD, Dist: `+2.95%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.45%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+2.95%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.63%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.40%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.72%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.41%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.69%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 2,160.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,490.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 220.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 7,380.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,000.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 8,800.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 276.90 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 78,600.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,580.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 375.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 3,100.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 6,090.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 20,120.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 227,000.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 707.27 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,200.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 50,500.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 5,050.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 21,330.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 649,410.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 5,150.00 USD | 12,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 8,850.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 54,130.00 USD | 12,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 34,810.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 18,730.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 790.76 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 11,650.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 167,180.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,590.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 13,370.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 15,810.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 6,940.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 1,080.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 4,200.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 699,300.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 8,460.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 34,640.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 6,140.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 17,510.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 660.96 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 2,890.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 1,510.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 18,640.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,390,000.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 40,530.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 33,520.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,770.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 36,990.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 17,550.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 21,890.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 304,290.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 34,730.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 488,550.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 30,270.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,760,000.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 24,790.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 17,190.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 16,490.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 59,520.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 52,830.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 17,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 812,400.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 648,530.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 249,630.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.22` | 20,660,000.00 USD | 20,660,000.00 USD | 126,280.00 USD | 35,380.00 USD | 126,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 20,370,000.00 USD | 20,370,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 188,780.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 20,180,000.00 USD | 20,180,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 20,040,000.00 USD | 20,040,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 19,910,000.00 USD | 19,910,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 19,810,000.00 USD | 19,810,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 19,670,000.00 USD | 19,670,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 18,480.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 19,540,000.00 USD | 19,540,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 19,510,000.00 USD | 19,510,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 19,450,000.00 USD | 19,450,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 19,300,000.00 USD | 19,300,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 19,220,000.00 USD | 19,220,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 14,500.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 6,270,000.00 USD | 6,270,000.00 USD | 27,560.00 USD | 8,350.00 USD | 22,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 19,170,000.00 USD | 19,170,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 6,210,000.00 USD | 6,210,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 19,060,000.00 USD | 19,060,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 6,180,000.00 USD | 6,180,000.00 USD | 24,480.00 USD | 7,140.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 19,000,000.00 USD | 19,000,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 6,140,000.00 USD | 6,140,000.00 USD | 18,490.00 USD | 3,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 18,930,000.00 USD | 18,930,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 6,110,000.00 USD | 6,110,000.00 USD | 4,350.00 USD | 1,600.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 18,890,000.00 USD | 18,890,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,960.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 6,100,000.00 USD | 6,100,000.00 USD | 22,600.00 USD | 9,260.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 18,840,000.00 USD | 18,840,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 6,060,000.00 USD | 6,060,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 18,750,000.00 USD | 18,750,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,030,000.00 USD | 6,030,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 18,640,000.00 USD | 18,640,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,020,000.00 USD | 6,020,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 18,590,000.00 USD | 18,590,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 5,970,000.00 USD | 5,970,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 18,550,000.00 USD | 18,550,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 5,930,000.00 USD | 5,930,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 18,500,000.00 USD | 18,500,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 5,910,000.00 USD | 5,910,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 18,470,000.00 USD | 18,470,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 5,890,000.00 USD | 5,890,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 18,450,000.00 USD | 18,450,000.00 USD | 14,670.00 USD | 0.00 USD | 188.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 5,880,000.00 USD | 5,880,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 18,430,000.00 USD | 18,430,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 5,860,000.00 USD | 5,860,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 18,390,000.00 USD | 18,390,000.00 USD | 20,210.00 USD | 4,010.00 USD | 318.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 5,830,000.00 USD | 5,830,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 18,360,000.00 USD | 18,360,000.00 USD | 16,310.00 USD | 0.00 USD | 294.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 5,810,000.00 USD | 5,810,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 18,350,000.00 USD | 18,350,000.00 USD | 14,200.00 USD | 4,000.00 USD | 23,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 5,800,000.00 USD | 5,800,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 18,300,000.00 USD | 18,300,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 5,800,000.00 USD | 5,800,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 18,170,000.00 USD | 18,170,000.00 USD | 135,080.00 USD | 28,860.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 5,800,000.00 USD | 5,800,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,990,000.00 USD | 17,990,000.00 USD | 79,220.00 USD | 38,860.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 79,970.00 USD | 797,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 5,800,000.00 USD | 5,800,000.00 USD | 976.86 USD | 4,520.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 17,830,000.00 USD | 17,830,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 5,790,000.00 USD | 5,790,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 17,470,000.00 USD | 17,470,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 5,760,000.00 USD | 5,760,000.00 USD | 3,610.00 USD | 3,770.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 17,010,000.00 USD | 17,010,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 5,720,000.00 USD | 5,720,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 16,580,000.00 USD | 16,580,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 5,570,000.00 USD | 5,570,000.00 USD | 47,590.00 USD | 17,110.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 15,670,000.00 USD | 15,670,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 717,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 5,500,000.00 USD | 5,500,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 15,080,000.00 USD | 15,080,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 5,350,000.00 USD | 5,350,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 14,530,000.00 USD | 14,530,000.00 USD | 96,870.00 USD | 110,950.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 5,300,000.00 USD | 5,300,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 14,160,000.00 USD | 14,160,000.00 USD | 134,000.00 USD | 91,410.00 USD | 160,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 5,250,000.00 USD | 5,250,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 13,770,000.00 USD | 13,770,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,090,000.00 USD | 5,090,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 13,260,000.00 USD | 13,260,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 27,780.00 USD | 159,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,060,000.00 USD | 5,060,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 12,600,000.00 USD | 12,600,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,020,000.00 USD | 5,020,000.00 USD | 30,300.00 USD | 15,060.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 12,200,000.00 USD | 12,200,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 4,950,000.00 USD | 4,950,000.00 USD | 34,720.00 USD | 30,270.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 11,390,000.00 USD | 11,390,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 4,850,000.00 USD | 4,850,000.00 USD | 54,370.00 USD | 33,090.00 USD | 75,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 10,190,000.00 USD | 10,190,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 4,690,000.00 USD | 4,690,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 9,150,000.00 USD | 9,150,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 48,310.00 USD | 131,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 4,300,000.00 USD | 4,300,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 7,670,000.00 USD | 7,670,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 4,010,000.00 USD | 4,010,000.00 USD | 137,180.00 USD | 43,130.00 USD | 55,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 6,360,000.00 USD | 6,360,000.00 USD | 659,190.00 USD | 214,580.00 USD | 541,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 3,770,000.00 USD | 3,770,000.00 USD | 222,000.00 USD | 47,730.00 USD | 96,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,950,000.00 USD | 4,950,000.00 USD | 371,240.00 USD | 240,290.00 USD | 128,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 3,400,000.00 USD | 3,400,000.00 USD | 91,270.00 USD | 34,010.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 4,210,000.00 USD | 4,210,000.00 USD | 208,020.00 USD | 228,180.00 USD | 217,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 3,230,000.00 USD | 3,230,000.00 USD | 116,260.00 USD | 63,910.00 USD | 79,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 3,560,000.00 USD | 3,560,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 72,340.00 USD | 83,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 2,970,000.00 USD | 2,970,000.00 USD | 189,850.00 USD | 53,910.00 USD | 63,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 3,260,000.00 USD | 3,260,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 2,660,000.00 USD | 2,660,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 2,690,000.00 USD | 2,690,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 2,540,000.00 USD | 2,540,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 2,280,000.00 USD | 2,280,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 2,400,000.00 USD | 2,400,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 2,210,000.00 USD | 2,210,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 2,290,000.00 USD | 2,290,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 2,040,000.00 USD | 2,040,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 10,910.00 USD | 10,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 2,020,000.00 USD | 2,020,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 1,680,000.00 USD | 1,680,000.00 USD | 170,150.00 USD | 48,220.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 1,620,000.00 USD | 1,620,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 1,400,000.00 USD | 1,400,000.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 1,490,000.00 USD | 1,490,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 1,310,000.00 USD | 1,310,000.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 1,300,000.00 USD | 1,300,000.00 USD | 106,690.00 USD | 34,500.00 USD | 53,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 1,120,000.00 USD | 1,120,000.00 USD | 61,980.00 USD | 0.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 1,100,000.00 USD | 1,100,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 1,000,000.00 USD | 1,000,000.00 USD | 148,600.00 USD | 44,370.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 857,200.00 USD | 857,200.00 USD | 130,220.00 USD | 30,500.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.46` | 769,190.00 USD | 769,190.00 USD | 0.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 671,620.00 USD | 671,620.00 USD | 16,710.00 USD | 14,820.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 759,150.00 USD | 759,150.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 628,140.00 USD | 628,140.00 USD | 74,140.00 USD | 61,630.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 718,720.00 USD | 718,720.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 478,070.00 USD | 478,070.00 USD | 13,090.00 USD | 34,130.00 USD | 46,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.52` | 630,580.00 USD | 630,580.00 USD | 0.00 USD | 37,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.54` | 384,520.00 USD | 384,520.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.54` | 593,050.00 USD | 593,050.00 USD | 34,770.00 USD | 27,190.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 361,920.00 USD | 361,920.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.56` | 479,570.00 USD | 479,570.00 USD | 0.00 USD | 28,460.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.58` | 202,960.00 USD | 202,960.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.58` | 413,220.00 USD | 413,220.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 121,320.00 USD | 121,320.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.60` | 381,600.00 USD | 381,600.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.62` | 13,920.00 USD | 13,920.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.64` | 358,820.00 USD | 358,820.00 USD | 68,740.00 USD | 79,630.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.66` | 37,590.00 USD | 37,590.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.66` | 75,180.00 USD | 75,180.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.66` | 154,750.00 USD | 154,750.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 121,100.00 USD | 121,100.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.68` | 92,780.00 USD | 92,780.00 USD | 88,140.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 140,560.00 USD | 140,560.00 USD | 0.00 USD | 230.72 USD | 19,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 317,980.00 USD | 317,980.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 195,940.00 USD | 195,940.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 318,310.00 USD | 318,310.00 USD | 0.00 USD | 324.58 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 318,650.00 USD | 318,650.00 USD | 0.00 USD | 342.56 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 244,130.00 USD | 244,130.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 335,680.00 USD | 335,680.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 336,740.00 USD | 336,740.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 384,250.00 USD | 384,250.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 545,000.00 USD | 545,000.00 USD | 158,640.00 USD | 1,970.00 USD | 133.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 420,660.00 USD | 420,660.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 764,330.00 USD | 764,330.00 USD | 178,690.00 USD | 40,640.00 USD | 10.32 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 2,390.00 USD | 2,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 492,810.00 USD | 492,810.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 770,990.00 USD | 770,990.00 USD | 0.00 USD | 6,610.00 USD | 42.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 548,760.00 USD | 548,760.00 USD | 19,640.00 USD | 15,360.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 783,970.00 USD | 783,970.00 USD | 10,340.00 USD | 2,480.00 USD | 165.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 592,970.00 USD | 592,970.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 795,940.00 USD | 795,940.00 USD | 11,220.00 USD | 612.37 USD | 145.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 618,570.00 USD | 618,570.00 USD | 12,480.00 USD | 13,090.00 USD | 20.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 803,120.00 USD | 803,120.00 USD | 7,000.00 USD | 0.00 USD | 169.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 630,270.00 USD | 630,270.00 USD | 1,220.00 USD | 4,890.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 993,220.00 USD | 993,220.00 USD | 17,060.00 USD | 24,600.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 697,020.00 USD | 697,020.00 USD | 12,210.00 USD | 26,690.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 1,150,000.00 USD | 1,150,000.00 USD | 6,640.00 USD | 1,490.00 USD | 151,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 833,980.00 USD | 833,980.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 1,770,000.00 USD | 1,770,000.00 USD | 391,180.00 USD | 34,700.00 USD | 190,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 982,170.00 USD | 982,170.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 2,270,000.00 USD | 2,270,000.00 USD | 304,560.00 USD | 7,460.00 USD | 183,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 1,090,000.00 USD | 1,090,000.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 2,780,000.00 USD | 2,780,000.00 USD | 244,440.00 USD | 47,410.00 USD | 222,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 1,500,000.00 USD | 1,500,000.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 3,390,000.00 USD | 3,390,000.00 USD | 292,690.00 USD | 137,340.00 USD | 179,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 1,960,000.00 USD | 1,960,000.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 3,870,000.00 USD | 3,870,000.00 USD | 234,210.00 USD | 101,560.00 USD | 145,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 2,180,000.00 USD | 2,180,000.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 4,520,000.00 USD | 4,520,000.00 USD | 375,670.00 USD | 106,090.00 USD | 165,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 2,240,000.00 USD | 2,240,000.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 4,650,000.00 USD | 4,650,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 2,480,000.00 USD | 2,480,000.00 USD | 141,930.00 USD | 49,190.00 USD | 50,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 5,010,000.00 USD | 5,010,000.00 USD | 174,090.00 USD | 67,240.00 USD | 119,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 2,680,000.00 USD | 2,680,000.00 USD | 109,520.00 USD | 28,690.00 USD | 53,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 5,290,000.00 USD | 5,290,000.00 USD | 118,920.00 USD | 65,050.00 USD | 93,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,130.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 2,890,000.00 USD | 2,890,000.00 USD | 90,900.00 USD | 61,100.00 USD | 64,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 5,630,000.00 USD | 5,630,000.00 USD | 183,570.00 USD | 86,510.00 USD | 72,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 3,100,000.00 USD | 3,100,000.00 USD | 122,240.00 USD | 44,200.00 USD | 42,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 5,760,000.00 USD | 5,760,000.00 USD | 57,680.00 USD | 42,810.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 3,280,000.00 USD | 3,280,000.00 USD | 94,060.00 USD | 48,470.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 6,090,000.00 USD | 6,090,000.00 USD | 194,760.00 USD | 51,340.00 USD | 78,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 3,400,000.00 USD | 3,400,000.00 USD | 29,450.00 USD | 42,870.00 USD | 52,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 6,500,000.00 USD | 6,500,000.00 USD | 261,490.00 USD | 56,370.00 USD | 93,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 3,460,000.00 USD | 3,460,000.00 USD | 35,430.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 6,740,000.00 USD | 6,740,000.00 USD | 70,650.00 USD | 58,900.00 USD | 114,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,710.00 USD | 5,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 3,570,000.00 USD | 3,570,000.00 USD | 59,230.00 USD | 27,170.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 7,050,000.00 USD | 7,050,000.00 USD | 202,660.00 USD | 56,010.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 3,730,000.00 USD | 3,730,000.00 USD | 99,490.00 USD | 24,800.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 7,540,000.00 USD | 7,540,000.00 USD | 238,210.00 USD | 76,160.00 USD | 170,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 3,860,000.00 USD | 3,860,000.00 USD | 59,030.00 USD | 24,040.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 7,890,000.00 USD | 7,890,000.00 USD | 178,010.00 USD | 79,440.00 USD | 96,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 3,870,000.00 USD | 3,870,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 8,080,000.00 USD | 8,080,000.00 USD | 120,640.00 USD | 46,590.00 USD | 18,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 3,920,000.00 USD | 3,920,000.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 8,330,000.00 USD | 8,330,000.00 USD | 158,050.00 USD | 81,530.00 USD | 13,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 103,300.00 USD | 108,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 3,950,000.00 USD | 3,950,000.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 8,480,000.00 USD | 8,480,000.00 USD | 97,320.00 USD | 30,690.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 4,000,000.00 USD | 4,000,000.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 8,660,000.00 USD | 8,660,000.00 USD | 7,170.00 USD | 7,370.00 USD | 166,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 4,070,000.00 USD | 4,070,000.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 9,150,000.00 USD | 9,150,000.00 USD | 196,150.00 USD | 41,260.00 USD | 258,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 4,150,000.00 USD | 4,150,000.00 USD | 51,980.00 USD | 13,980.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 9,730,000.00 USD | 9,730,000.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 4,180,000.00 USD | 4,180,000.00 USD | 18,760.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 10,210,000.00 USD | 10,210,000.00 USD | 162,080.00 USD | 68,340.00 USD | 247,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,930.00 USD | 113,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 4,210,000.00 USD | 4,210,000.00 USD | 2,900.00 USD | 15,260.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 10,460,000.00 USD | 10,460,000.00 USD | 84,310.00 USD | 78,160.00 USD | 86,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 4,220,000.00 USD | 4,220,000.00 USD | 2,220.00 USD | 2,560.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 10,690,000.00 USD | 10,690,000.00 USD | 31,320.00 USD | 20,570.00 USD | 180,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 4,240,000.00 USD | 4,240,000.00 USD | 1,320.00 USD | 4,320.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 10,940,000.00 USD | 10,940,000.00 USD | 153,430.00 USD | 20,380.00 USD | 74,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 4,280,000.00 USD | 4,280,000.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 11,280,000.00 USD | 11,280,000.00 USD | 165,890.00 USD | 45,040.00 USD | 125,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 4,290,000.00 USD | 4,290,000.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 11,540,000.00 USD | 11,540,000.00 USD | 96,800.00 USD | 59,960.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.56` | 4,340,000.00 USD | 4,340,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 11,730,000.00 USD | 11,730,000.00 USD | 128,070.00 USD | 30,820.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 4,360,000.00 USD | 4,360,000.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 11,930,000.00 USD | 11,930,000.00 USD | 97,670.00 USD | 66,210.00 USD | 41,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 4,370,000.00 USD | 4,370,000.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 12,050,000.00 USD | 12,050,000.00 USD | 56,420.00 USD | 26,450.00 USD | 39,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 4,400,000.00 USD | 4,400,000.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 12,120,000.00 USD | 12,120,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 4,430,000.00 USD | 4,430,000.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 12,420,000.00 USD | 12,420,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 4,380.00 USD | 117,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 4,430,000.00 USD | 4,430,000.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 12,580,000.00 USD | 12,580,000.00 USD | 43,740.00 USD | 9,020.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 4,450,000.00 USD | 4,450,000.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 12,870,000.00 USD | 12,870,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 13,090,000.00 USD | 13,090,000.00 USD | 22,060.00 USD | 50,120.00 USD | 142,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 4,470,000.00 USD | 4,470,000.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 13,270,000.00 USD | 13,270,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 4,500,000.00 USD | 4,500,000.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 13,350,000.00 USD | 13,350,000.00 USD | 38,570.00 USD | 18,330.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 4,570,000.00 USD | 4,570,000.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 13,400,000.00 USD | 13,400,000.00 USD | 15,760.00 USD | 6,360.00 USD | 29,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 4,590,000.00 USD | 4,590,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 13,510,000.00 USD | 13,510,000.00 USD | 78,020.00 USD | 15,750.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 4,610,000.00 USD | 4,610,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 13,570,000.00 USD | 13,570,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 4,620,000.00 USD | 4,620,000.00 USD | 2,680.00 USD | 1,320.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 13,590,000.00 USD | 13,590,000.00 USD | 14,750.00 USD | 132.05 USD | 4,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 4,650,000.00 USD | 4,650,000.00 USD | 21,810.00 USD | 5,820.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 13,640,000.00 USD | 13,640,000.00 USD | 29,710.00 USD | 15,990.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 117,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 4,680,000.00 USD | 4,680,000.00 USD | 18,490.00 USD | 3,790.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 13,690,000.00 USD | 13,690,000.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 4,700,000.00 USD | 4,700,000.00 USD | 3,720.00 USD | 1,600.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 13,730,000.00 USD | 13,730,000.00 USD | 24,580.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 4,730,000.00 USD | 4,730,000.00 USD | 21,720.00 USD | 9,260.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 13,810,000.00 USD | 13,810,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 4,750,000.00 USD | 4,750,000.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 13,880,000.00 USD | 13,880,000.00 USD | 50,620.00 USD | 13,030.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 4,770,000.00 USD | 4,770,000.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 13,910,000.00 USD | 13,910,000.00 USD | 27,900.00 USD | 1,070.00 USD | 123.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 4,770,000.00 USD | 4,770,000.00 USD | 227.00 USD | 5,090.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 13,950,000.00 USD | 13,950,000.00 USD | 14,650.00 USD | 11,970.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 4,820,000.00 USD | 4,820,000.00 USD | 24,650.00 USD | 7,080.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 13,990,000.00 USD | 13,990,000.00 USD | 13,860.00 USD | 6,970.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 4,860,000.00 USD | 4,860,000.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 14,030,000.00 USD | 14,030,000.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.02` | 4,880,000.00 USD | 4,880,000.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 14,040,000.00 USD | 14,040,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.04` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 14,040,000.00 USD | 14,040,000.00 USD | 303.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 118,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `13.06` | 4,900,000.00 USD | 4,900,000.00 USD | 9,530.00 USD | 1,380.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.06` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.08` | 4,910,000.00 USD | 4,910,000.00 USD | 7,160.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.10` | 14,080,000.00 USD | 14,080,000.00 USD | 18,460.00 USD | 5,730.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.12` | 14,090,000.00 USD | 14,090,000.00 USD | 945.50 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.14` | 14,090,000.00 USD | 14,090,000.00 USD | 321.45 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 118,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.16` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 41.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.18` | 14,100,000.00 USD | 14,100,000.00 USD | 193.15 USD | 4,000.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.20` | 14,120,000.00 USD | 14,120,000.00 USD | 972.55 USD | 0.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.22` | 14,150,000.00 USD | 14,150,000.00 USD | 23,980.00 USD | 259.77 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.24` | 14,190,000.00 USD | 14,190,000.00 USD | 23,250.00 USD | 4,640.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.26` | 14,210,000.00 USD | 14,210,000.00 USD | 463.75 USD | 8,520.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.28` | 14,230,000.00 USD | 14,230,000.00 USD | 14,470.00 USD | 5,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 7,740.00 USD | 126,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 127,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 1,170.00 USD | 129,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 37,400.00 USD | 166,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 898.79 USD | 167,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 616.92 USD | 167,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 615.08 USD | 168,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 193,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 16,130.00 USD | 210,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 24,770.00 USD | 234,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 10,000.00 USD | 244,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 504.00 USD | 245,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 301,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 5,070.00 USD | 306,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 26,030.00 USD | 332,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 565.71 USD | 333,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.65` | 64,850.00 USD | 398,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 469.00 USD | 398,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 478,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 479,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 241.50 USD | 480,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 575,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 245,140.00 USD | 820,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 1,720.00 USD | 821,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 822,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 822,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 824,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 2,130,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 574.70 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 452.87 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 759,860.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 73,950.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.05` | 334,610.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.25` | 890.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.45` | 2,990.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 13,860,000.00 USD | 0.00 USD | 2,160.00 USD | `-80.00%` | `920,000.00` |
| `Live` | `Long` | `2.65` | 13,850,000.00 USD | 0.00 USD | 2,490.00 USD | `-77.44%` | `938,700.00` |
| `Live` | `Long` | `2.75` | 13,850,000.00 USD | 0.00 USD | 220.00 USD | `-76.59%` | `80,000.00` |
| `Live` | `Long` | `2.95` | 13,850,000.00 USD | 0.00 USD | 7,380.00 USD | `-74.89%` | `2,500,000.00` |
| `Live` | `Long` | `3.05` | 13,840,000.00 USD | 0.00 USD | 7,000.00 USD | `-74.04%` | `2,296,000.00` |
| `Live` | `Long` | `3.15` | 13,840,000.00 USD | 0.00 USD | 8,800.00 USD | `-73.19%` | `2,793,300.00` |
| `Live` | `Long` | `3.25` | 13,830,000.00 USD | 0.00 USD | 276.90 USD | `-72.34%` | `85,200.00` |
| `Live` | `Long` | `3.35` | 13,830,000.00 USD | 0.00 USD | 78,600.00 USD | `-71.49%` | `23,464,000.00` |
| `Live` | `Long` | `3.65` | 13,750,000.00 USD | 0.00 USD | 2,580.00 USD | `-68.93%` | `707,000.00` |
| `Live` | `Long` | `3.75` | 13,750,000.00 USD | 0.00 USD | 375.00 USD | `-68.08%` | `100,000.00` |
| `Live` | `Long` | `3.85` | 13,750,000.00 USD | 0.00 USD | 3,100.00 USD | `-67.23%` | `805,000.00` |
| `Live` | `Long` | `3.95` | 13,740,000.00 USD | 0.00 USD | 6,090.00 USD | `-66.38%` | `1,540,700.00` |
| `Live` | `Long` | `4.05` | 13,740,000.00 USD | 0.00 USD | 20,120.00 USD | `-65.53%` | `4,966,700.00` |
| `Live` | `Long` | `4.25` | 13,720,000.00 USD | 0.00 USD | 5,090.00 USD | `-63.83%` | `1,198,100.00` |
| `Live` | `Long` | `4.45` | 13,710,000.00 USD | 0.00 USD | 381.37 USD | `-62.12%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 13,710,000.00 USD | 0.00 USD | 227,000.00 USD | `-61.27%` | `49,890,900.00` |
| `Live` | `Long` | `4.65` | 13,480,000.00 USD | 0.00 USD | 383.63 USD | `-60.42%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,480,000.00 USD | 0.00 USD | 707.27 USD | `-59.57%` | `148,900.00` |
| `Live` | `Long` | `4.85` | 13,480,000.00 USD | 0.00 USD | 1,200.00 USD | `-58.72%` | `247,100.00` |
| `Live` | `Long` | `4.95` | 13,480,000.00 USD | 0.00 USD | 50,500.00 USD | `-57.87%` | `10,202,800.00` |
| `Live` | `Long` | `5.05` | 13,430,000.00 USD | 0.00 USD | 5,050.00 USD | `-57.02%` | `1,000,000.00` |
| `Live` | `Long` | `5.25` | 13,430,000.00 USD | 0.00 USD | 21,330.00 USD | `-55.31%` | `4,062,100.00` |
| `Live` | `Long` | `5.35` | 13,400,000.00 USD | 0.00 USD | 649,410.00 USD | `-54.46%` | `121,384,200.00` |
| `Live` | `Long` | `5.45` | 12,760,000.00 USD | 0.00 USD | 5,150.00 USD | `-53.61%` | `945,000.00` |
| `Live` | `Long` | `5.55` | 12,750,000.00 USD | 0.00 USD | 8,850.00 USD | `-52.76%` | `1,593,700.00` |
| `Live` | `Long` | `5.65` | 12,740,000.00 USD | 0.00 USD | 54,130.00 USD | `-51.91%` | `9,581,300.00` |
| `Live` | `Long` | `5.75` | 12,690,000.00 USD | 0.00 USD | 34,810.00 USD | `-51.06%` | `6,053,800.00` |
| `Live` | `Long` | `5.85` | 12,650,000.00 USD | 0.00 USD | 18,730.00 USD | `-50.21%` | `3,202,100.00` |
| `Live` | `Long` | `5.95` | 12,630,000.00 USD | 0.00 USD | 790.76 USD | `-49.36%` | `132,900.00` |
| `Live` | `Long` | `6.05` | 12,630,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.50%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,570,000.00 USD | 0.00 USD | 11,650.00 USD | `-47.65%` | `1,894,700.00` |
| `Live` | `Long` | `6.25` | 12,560,000.00 USD | 0.00 USD | 167,180.00 USD | `-46.80%` | `26,748,700.00` |
| `Live` | `Long` | `6.35` | 12,390,000.00 USD | 0.00 USD | 16,590.00 USD | `-45.95%` | `2,612,900.00` |
| `Live` | `Long` | `6.45` | 12,370,000.00 USD | 0.00 USD | 13,370.00 USD | `-45.10%` | `2,073,400.00` |
| `Live` | `Long` | `6.55` | 12,360,000.00 USD | 0.00 USD | 15,810.00 USD | `-44.25%` | `2,414,300.00` |
| `Live` | `Long` | `6.65` | 12,350,000.00 USD | 0.00 USD | 9,260.00 USD | `-43.40%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 12,340,000.00 USD | 0.00 USD | 4,130.00 USD | `-42.55%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,330,000.00 USD | 0.00 USD | 6,940.00 USD | `-41.69%` | `1,013,400.00` |
| `Live` | `Long` | `6.95` | 12,330,000.00 USD | 0.00 USD | 1,080.00 USD | `-40.84%` | `155,300.00` |
| `Live` | `Long` | `7.05` | 12,320,000.00 USD | 0.00 USD | 4,200.00 USD | `-39.99%` | `595,500.00` |
| `Live` | `Long` | `7.15` | 12,320,000.00 USD | 0.00 USD | 699,300.00 USD | `-39.14%` | `97,803,500.00` |
| `Live` | `Long` | `7.25` | 11,620,000.00 USD | 0.00 USD | 8,460.00 USD | `-38.29%` | `1,167,100.00` |
| `Live` | `Long` | `7.35` | 11,610,000.00 USD | 0.00 USD | 34,640.00 USD | `-37.44%` | `4,712,300.00` |
| `Live` | `Long` | `7.45` | 11,580,000.00 USD | 0.00 USD | 6,140.00 USD | `-36.59%` | `823,900.00` |
| `Live` | `Long` | `7.55` | 11,570,000.00 USD | 0.00 USD | 17,510.00 USD | `-35.74%` | `2,318,800.00` |
| `Live` | `Long` | `7.65` | 11,550,000.00 USD | 0.00 USD | 660.96 USD | `-34.89%` | `86,400.00` |
| `Live` | `Long` | `7.75` | 11,550,000.00 USD | 0.00 USD | 2,890.00 USD | `-34.03%` | `373,100.00` |
| `Live` | `Long` | `7.85` | 11,550,000.00 USD | 0.00 USD | 1,510.00 USD | `-33.18%` | `192,900.00` |
| `Live` | `Long` | `7.95` | 11,550,000.00 USD | 0.00 USD | 18,640.00 USD | `-32.33%` | `2,344,200.00` |
| `Live` | `Long` | `8.05` | 11,530,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-31.48%` | `172,511,800.00` |
| `Live` | `Long` | `8.15` | 10,140,000.00 USD | 0.00 USD | 40,530.00 USD | `-30.63%` | `4,973,400.00` |
| `Live` | `Long` | `8.25` | 10,100,000.00 USD | 0.00 USD | 33,520.00 USD | `-29.78%` | `4,063,200.00` |
| `Live` | `Long` | `8.35` | 10,070,000.00 USD | 0.00 USD | 7,770.00 USD | `-28.93%` | `930,800.00` |
| `Live` | `Long` | `8.45` | 10,060,000.00 USD | 0.00 USD | 36,990.00 USD | `-28.08%` | `4,377,000.00` |
| `Live` | `Long` | `8.55` | 10,020,000.00 USD | 0.00 USD | 17,550.00 USD | `-27.22%` | `2,053,200.00` |
| `Live` | `Long` | `8.65` | 10,010,000.00 USD | 0.00 USD | 21,890.00 USD | `-26.37%` | `2,530,600.00` |
| `Live` | `Long` | `8.75` | 9,980,000.00 USD | 0.00 USD | 304,290.00 USD | `-25.52%` | `34,776,300.00` |
| `Live` | `Long` | `8.85` | 9,680,000.00 USD | 0.00 USD | 34,730.00 USD | `-24.67%` | `3,924,300.00` |
| `Live` | `Long` | `8.95` | 9,640,000.00 USD | 0.00 USD | 488,550.00 USD | `-23.82%` | `54,587,100.00` |
| `Live` | `Long` | `9.05` | 9,160,000.00 USD | 0.00 USD | 30,270.00 USD | `-22.97%` | `3,344,900.00` |
| `Live` | `Long` | `9.15` | 9,130,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-22.12%` | `410,398,600.00` |
| `Live` | `Long` | `9.25` | 5,370,000.00 USD | 0.00 USD | 24,790.00 USD | `-21.27%` | `2,679,800.00` |
| `Live` | `Long` | `9.35` | 5,350,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-20.42%` | `230,268,400.00` |
| `Live` | `Long` | `9.45` | 3,190,000.00 USD | 0.00 USD | 17,190.00 USD | `-19.56%` | `1,819,100.00` |
| `Live` | `Long` | `9.55` | 3,180,000.00 USD | 0.00 USD | 16,490.00 USD | `-18.71%` | `1,726,500.00` |
| `Live` | `Long` | `9.65` | 3,160,000.00 USD | 0.00 USD | 59,520.00 USD | `-17.86%` | `6,167,500.00` |
| `Live` | `Long` | `9.75` | 3,100,000.00 USD | 0.00 USD | 52,830.00 USD | `-17.01%` | `5,418,900.00` |
| `Live` | `Long` | `9.85` | 3,050,000.00 USD | 0.00 USD | 17,700.00 USD | `-16.16%` | `1,796,600.00` |
| `Live` | `Long` | `9.95` | 3,030,000.00 USD | 0.00 USD | 812,400.00 USD | `-15.31%` | `81,648,500.00` |
| `Live` | `Long` | `10.05` | 2,220,000.00 USD | 0.00 USD | 648,530.00 USD | `-14.46%` | `64,530,100.00` |
| `Live` | `Long` | `10.15` | 1,570,000.00 USD | 0.00 USD | 249,630.00 USD | `-13.61%` | `24,594,200.00` |
| `Live` | `Long` | `10.25` | 1,320,000.00 USD | 0.00 USD | 188,780.00 USD | `-12.75%` | `18,418,000.00` |
| `Live` | `Long` | `10.35` | 1,130,000.00 USD | 0.00 USD | 18,480.00 USD | `-11.90%` | `1,785,200.00` |
| `Live` | `Long` | `10.45` | 1,110,000.00 USD | 0.00 USD | 14,500.00 USD | `-11.05%` | `1,387,200.00` |
| `Live` | `Long` | `10.55` | 1,100,000.00 USD | 0.00 USD | 40,960.00 USD | `-10.20%` | `3,882,000.00` |
| `Live` | `Long` | `10.65` | 1,060,000.00 USD | 0.00 USD | 44,080.00 USD | `-9.35%` | `4,138,800.00` |
| `Live` | `Long` | `10.75` | 1,010,000.00 USD | 0.00 USD | 214,040.00 USD | `-8.50%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 797,380.00 USD | 0.00 USD | 79,970.00 USD | `-7.65%` | `7,370,500.00` |
| `Live` | `Long` | `10.95` | 717,420.00 USD | 0.00 USD | 558,090.00 USD | `-6.80%` | `50,966,800.00` |
| `Live` | `Long` | `11.05` | 159,330.00 USD | 0.00 USD | 27,780.00 USD | `-5.95%` | `2,513,600.00` |
| `Live` | `Long` | `11.15` | 131,550.00 USD | 0.00 USD | 48,310.00 USD | `-5.09%` | `4,332,700.00` |
| `Live` | `Long` | `11.25` | 83,240.00 USD | 0.00 USD | 72,340.00 USD | `-4.24%` | `6,429,900.00` |
| `Live` | `Long` | `11.35` | 10,910.00 USD | 0.00 USD | 10,910.00 USD | `-3.39%` | `961,000.00` |
| `Live` | `Short` | `11.85` | 2,390.00 USD | 2,390.00 USD | 0.00 USD | `+0.86%` | `201,300.00` |
| `Live` | `Short` | `12.15` | 3,520.00 USD | 1,130.00 USD | 0.00 USD | `+3.42%` | `93,000.00` |
| `Live` | `Short` | `12.25` | 5,230.00 USD | 1,710.00 USD | 0.00 USD | `+4.27%` | `139,900.00` |
| `Live` | `Short` | `12.35` | 108,530.00 USD | 103,300.00 USD | 0.00 USD | `+5.12%` | `8,364,200.00` |
| `Live` | `Short` | `12.45` | 113,450.00 USD | 4,930.00 USD | 0.00 USD | `+5.97%` | `395,700.00` |
| `Live` | `Short` | `12.65` | 117,830.00 USD | 4,380.00 USD | 0.00 USD | `+7.67%` | `346,000.00` |
| `Live` | `Short` | `12.85` | 117,970.00 USD | 138.78 USD | 0.00 USD | `+9.38%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 118,080.00 USD | 113.53 USD | 0.00 USD | `+11.08%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 118,360.00 USD | 274.84 USD | 0.00 USD | `+11.93%` | `20,900.00` |
| `Live` | `Short` | `13.45` | 126,100.00 USD | 7,740.00 USD | 0.00 USD | `+14.48%` | `575,300.00` |
| `Live` | `Short` | `13.55` | 127,860.00 USD | 1,760.00 USD | 0.00 USD | `+15.33%` | `130,100.00` |
| `Live` | `Short` | `13.85` | 129,030.00 USD | 1,170.00 USD | 0.00 USD | `+17.89%` | `84,500.00` |
| `Live` | `Short` | `14.05` | 166,430.00 USD | 37,400.00 USD | 0.00 USD | `+19.59%` | `2,661,900.00` |
| `Live` | `Short` | `14.45` | 167,330.00 USD | 898.79 USD | 0.00 USD | `+22.99%` | `62,200.00` |
| `Live` | `Short` | `14.55` | 167,940.00 USD | 616.92 USD | 0.00 USD | `+23.85%` | `42,400.00` |
| `Live` | `Short` | `14.75` | 168,560.00 USD | 615.08 USD | 0.00 USD | `+25.55%` | `41,700.00` |
| `Live` | `Short` | `14.95` | 193,890.00 USD | 25,330.00 USD | 0.00 USD | `+27.25%` | `1,694,600.00` |
| `Live` | `Short` | `15.25` | 210,030.00 USD | 16,130.00 USD | 0.00 USD | `+29.80%` | `1,058,000.00` |
| `Live` | `Short` | `15.55` | 234,800.00 USD | 24,770.00 USD | 0.00 USD | `+32.36%` | `1,592,900.00` |
| `Live` | `Short` | `15.65` | 244,800.00 USD | 10,000.00 USD | 0.00 USD | `+33.21%` | `639,000.00` |
| `Live` | `Short` | `15.75` | 245,300.00 USD | 504.00 USD | 0.00 USD | `+34.06%` | `32,000.00` |
| `Live` | `Short` | `15.85` | 301,650.00 USD | 56,350.00 USD | 0.00 USD | `+34.91%` | `3,554,900.00` |
| `Live` | `Short` | `15.95` | 306,710.00 USD | 5,070.00 USD | 0.00 USD | `+35.76%` | `317,700.00` |
| `Live` | `Short` | `16.25` | 332,750.00 USD | 26,030.00 USD | 0.00 USD | `+38.32%` | `1,601,900.00` |
| `Live` | `Short` | `16.35` | 333,310.00 USD | 565.71 USD | 0.00 USD | `+39.17%` | `34,600.00` |
| `Live` | `Short` | `16.65` | 398,160.00 USD | 64,850.00 USD | 0.00 USD | `+41.72%` | `3,895,000.00` |
| `Live` | `Short` | `16.75` | 398,630.00 USD | 469.00 USD | 0.00 USD | `+42.57%` | `28,000.00` |
| `Live` | `Short` | `16.95` | 478,400.00 USD | 79,770.00 USD | 0.00 USD | `+44.27%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 479,770.00 USD | 1,370.00 USD | 0.00 USD | `+45.98%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 480,010.00 USD | 241.50 USD | 0.00 USD | `+46.83%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 575,030.00 USD | 95,020.00 USD | 0.00 USD | `+48.53%` | `5,445,000.00` |
| `Live` | `Short` | `17.55` | 820,170.00 USD | 245,140.00 USD | 0.00 USD | `+49.38%` | `13,968,000.00` |
| `Live` | `Short` | `17.75` | 821,890.00 USD | 1,720.00 USD | 0.00 USD | `+51.08%` | `96,900.00` |
| `Live` | `Short` | `17.85` | 822,140.00 USD | 249.90 USD | 0.00 USD | `+51.93%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 822,760.00 USD | 621.07 USD | 0.00 USD | `+52.79%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 824,730.00 USD | 1,970.00 USD | 0.00 USD | `+53.64%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 2,950,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+57.04%` | `115,235,400.00` |
| `Live` | `Short` | `18.55` | 2,950,000.00 USD | 185.50 USD | 0.00 USD | `+57.89%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,950,000.00 USD | 186.50 USD | 0.00 USD | `+58.74%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 2,950,000.00 USD | 456.17 USD | 0.00 USD | `+60.45%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,970,000.00 USD | 16,250.00 USD | 0.00 USD | `+61.30%` | `857,700.00` |
| `Live` | `Short` | `19.35` | 2,970,000.00 USD | 574.70 USD | 0.00 USD | `+64.70%` | `29,700.00` |
| `Live` | `Short` | `19.65` | 3,010,000.00 USD | 38,790.00 USD | 0.00 USD | `+67.26%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 3,010,000.00 USD | 452.87 USD | 0.00 USD | `+69.81%` | `22,700.00` |
| `Live` | `Short` | `20.15` | 3,770,000.00 USD | 759,860.00 USD | 0.00 USD | `+71.51%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,770,000.00 USD | 7,250.00 USD | 0.00 USD | `+74.92%` | `353,000.00` |
| `Live` | `Short` | `21.75` | 3,850,000.00 USD | 73,950.00 USD | 0.00 USD | `+85.13%` | `3,400,000.00` |
| `Live` | `Short` | `22.05` | 4,180,000.00 USD | 334,610.00 USD | 0.00 USD | `+87.68%` | `15,175,000.00` |
| `Live` | `Short` | `22.25` | 4,180,000.00 USD | 890.00 USD | 0.00 USD | `+89.39%` | `40,000.00` |
| `Live` | `Short` | `22.45` | 4,190,000.00 USD | 2,990.00 USD | 0.00 USD | `+91.09%` | `133,300.00` |
| `Live` | `Short` | `23.35` | 4,190,000.00 USD | 238.17 USD | 0.00 USD | `+98.75%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 1,020,000.00 USD | 0.00 USD | 431.68 USD | `-69.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 1,020,000.00 USD | 0.00 USD | 290.29 USD | `-61.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 1,020,000.00 USD | 0.00 USD | 120.22 USD | `-55.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 1,020,000.00 USD | 0.00 USD | 107.09 USD | `-48.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 1,020,000.00 USD | 0.00 USD | 3,760.00 USD | `-44.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 1,020,000.00 USD | 0.00 USD | 133.00 USD | `-43.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 1,020,000.00 USD | 0.00 USD | 3,770.00 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 1,020,000.00 USD | 0.00 USD | 2,070.00 USD | `-38.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 1,010,000.00 USD | 0.00 USD | 3,740.00 USD | `-36.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 1,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 1,010,000.00 USD | 0.00 USD | 146.80 USD | `-33.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 1,010,000.00 USD | 0.00 USD | 5,000.00 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 1,000,000.00 USD | 0.00 USD | 393.64 USD | `-30.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 1,000,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 993,120.00 USD | 0.00 USD | 1,360.00 USD | `-28.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 991,760.00 USD | 0.00 USD | 30,250.00 USD | `-27.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 961,510.00 USD | 0.00 USD | 186.84 USD | `-26.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 961,320.00 USD | 0.00 USD | 742.88 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 960,580.00 USD | 0.00 USD | 180.54 USD | `-24.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 960,400.00 USD | 0.00 USD | 1,320.00 USD | `-23.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 959,080.00 USD | 0.00 USD | 2,440.00 USD | `-22.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 956,640.00 USD | 0.00 USD | 194.90 USD | `-22.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 956,440.00 USD | 0.00 USD | 4,940.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 951,500.00 USD | 0.00 USD | 9,870.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 941,630.00 USD | 0.00 USD | 3,550.00 USD | `-17.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 938,090.00 USD | 0.00 USD | 25,950.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 912,130.00 USD | 0.00 USD | 19,100.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 893,030.00 USD | 0.00 USD | 299,650.00 USD | `-15.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 593,380.00 USD | 0.00 USD | 2,590.00 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 590,790.00 USD | 0.00 USD | 1,050.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 589,740.00 USD | 0.00 USD | 2,820.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 586,920.00 USD | 0.00 USD | 2,000.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 584,920.00 USD | 0.00 USD | 19,450.00 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 565,470.00 USD | 0.00 USD | 5,160.00 USD | `-10.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 560,310.00 USD | 0.00 USD | 4,590.00 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 555,720.00 USD | 0.00 USD | 5,470.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 550,240.00 USD | 0.00 USD | 4,370.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 545,870.00 USD | 0.00 USD | 6,510.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 539,360.00 USD | 0.00 USD | 16,530.00 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 522,830.00 USD | 0.00 USD | 24,830.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 497,990.00 USD | 0.00 USD | 46,190.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 451,810.00 USD | 0.00 USD | 14,120.00 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 437,690.00 USD | 0.00 USD | 19,680.00 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 418,010.00 USD | 0.00 USD | 7,530.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 410,470.00 USD | 0.00 USD | 410,470.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 15,120.00 USD | 15,120.00 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 15,500.00 USD | 382.75 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 15,660.00 USD | 156.55 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 54,920.00 USD | 39,260.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 89,410.00 USD | 34,500.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 100,250.00 USD | 10,830.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 101,580.00 USD | 1,340.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 101,890.00 USD | 307.52 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 113,000.00 USD | 11,110.00 USD | 0.00 USD | `+6.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 169,530.00 USD | 56,530.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 211,010.00 USD | 41,470.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 231,730.00 USD | 20,730.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 232,520.00 USD | 784.77 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 239,020.00 USD | 6,500.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 240,070.00 USD | 1,050.00 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 243,910.00 USD | 3,840.00 USD | 0.00 USD | `+12.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 248,900.00 USD | 4,990.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 263,420.00 USD | 14,520.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 266,060.00 USD | 2,630.00 USD | 0.00 USD | `+15.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 268,080.00 USD | 2,020.00 USD | 0.00 USD | `+16.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 270,140.00 USD | 2,060.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 270,260.00 USD | 120.50 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 270,520.00 USD | 266.44 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 287,640.00 USD | 17,110.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 288,700.00 USD | 1,060.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 295,690.00 USD | 6,990.00 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 295,910.00 USD | 218.25 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 298,520.00 USD | 2,610.00 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 311,440.00 USD | 12,920.00 USD | 0.00 USD | `+25.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 312,390.00 USD | 950.82 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 323,620.00 USD | 11,220.00 USD | 0.00 USD | `+28.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 325,440.00 USD | 1,830.00 USD | 0.00 USD | `+28.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 558,480.00 USD | 233,040.00 USD | 0.00 USD | `+29.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 571,980.00 USD | 13,500.00 USD | 0.00 USD | `+30.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 572,870.00 USD | 893.01 USD | 0.00 USD | `+31.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 573,260.00 USD | 388.75 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 599,370.00 USD | 26,100.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 601,470.00 USD | 2,110.00 USD | 0.00 USD | `+34.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 606,810.00 USD | 5,340.00 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 612,130.00 USD | 5,320.00 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 621,300.00 USD | 9,170.00 USD | 0.00 USD | `+36.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 628,100.00 USD | 6,800.00 USD | 0.00 USD | `+37.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 646,860.00 USD | 18,760.00 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 653,400.00 USD | 6,540.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 659,980.00 USD | 6,580.00 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 669,910.00 USD | 9,930.00 USD | 0.00 USD | `+40.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 683,230.00 USD | 13,320.00 USD | 0.00 USD | `+41.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 697,470.00 USD | 14,240.00 USD | 0.00 USD | `+42.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 781,830.00 USD | 84,360.00 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 783,520.00 USD | 1,700.00 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 793,030.00 USD | 9,510.00 USD | 0.00 USD | `+45.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 794,740.00 USD | 1,710.00 USD | 0.00 USD | `+45.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 796,990.00 USD | 2,250.00 USD | 0.00 USD | `+46.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 895,330.00 USD | 98,330.00 USD | 0.00 USD | `+47.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 916,990.00 USD | 21,670.00 USD | 0.00 USD | `+48.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 923,430.00 USD | 6,430.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 927,840.00 USD | 4,410.00 USD | 0.00 USD | `+50.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 932,280.00 USD | 4,440.00 USD | 0.00 USD | `+51.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 936,740.00 USD | 4,460.00 USD | 0.00 USD | `+51.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 937,190.00 USD | 448.75 USD | 0.00 USD | `+52.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 972,770.00 USD | 35,590.00 USD | 0.00 USD | `+53.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 973,230.00 USD | 453.75 USD | 0.00 USD | `+54.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 974,060.00 USD | 830.38 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 974,510.00 USD | 458.75 USD | 0.00 USD | `+56.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 974,980.00 USD | 461.25 USD | 0.00 USD | `+57.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 979,520.00 USD | 4,540.00 USD | 0.00 USD | `+57.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 979,990.00 USD | 466.25 USD | 0.00 USD | `+58.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 980,460.00 USD | 468.75 USD | 0.00 USD | `+59.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 980,930.00 USD | 471.25 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 981,400.00 USD | 473.75 USD | 0.00 USD | `+61.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,050,000.00 USD | 67,000.00 USD | 0.00 USD | `+62.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,050,000.00 USD | 574.50 USD | 0.00 USD | `+63.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,050,000.00 USD | 577.50 USD | 0.00 USD | `+63.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,050,000.00 USD | 2,710.00 USD | 0.00 USD | `+64.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,050,000.00 USD | 972.50 USD | 0.00 USD | `+65.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,060,000.00 USD | 7,680.00 USD | 0.00 USD | `+66.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,060,000.00 USD | 1,680.00 USD | 0.00 USD | `+67.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,060,000.00 USD | 1,690.00 USD | 0.00 USD | `+68.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,070,000.00 USD | 992.50 USD | 0.00 USD | `+68.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,070,000.00 USD | 5,170.00 USD | 0.00 USD | `+69.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,680,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+71.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+73.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,690,000.00 USD | 1,030.00 USD | 0.00 USD | `+74.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,690,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,690,000.00 USD | 1,860.00 USD | 0.00 USD | `+76.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,690,000.00 USD | 1,410.00 USD | 0.00 USD | `+77.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,700,000.00 USD | 1,050.00 USD | 0.00 USD | `+78.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,700,000.00 USD | 4,000.00 USD | 0.00 USD | `+79.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,700,000.00 USD | 1,060.00 USD | 0.00 USD | `+80.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,700,000.00 USD | 1,060.00 USD | 0.00 USD | `+80.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,750,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+81.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,750,000.00 USD | 1,070.00 USD | 0.00 USD | `+82.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,750,000.00 USD | 1,080.00 USD | 0.00 USD | `+83.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,750,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,750,000.00 USD | 1,090.00 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,760,000.00 USD | 3,280.00 USD | 0.00 USD | `+85.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+86.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,760,000.00 USD | 1,110.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,760,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,760,000.00 USD | 1,120.00 USD | 0.00 USD | `+90.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,760,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,760,000.00 USD | 1,130.00 USD | 0.00 USD | `+91.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,760,000.00 USD | 1,130.00 USD | 0.00 USD | `+92.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+93.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,770,000.00 USD | 1,150.00 USD | 0.00 USD | `+95.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,900,000.00 USD | 129,920.00 USD | 0.00 USD | `+96.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+97.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+97.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,900,000.00 USD | 1,170.00 USD | 0.00 USD | `+98.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.45` | 3,900,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.60%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.22` | 20,660,000.00 USD | 0.00 USD | 20,660,000.00 USD | 126,280.00 USD | 35,380.00 USD | 126,190.00 USD |
| `7D` | `10.24` | 20,370,000.00 USD | 0.00 USD | 20,370,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,790.00 USD |
| `7D` | `10.26` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,290.00 USD |
| `7D` | `10.28` | 20,040,000.00 USD | 0.00 USD | 20,040,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,010.00 USD |
| `7D` | `10.30` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,940.00 USD |
| `7D` | `10.32` | 19,810,000.00 USD | 0.00 USD | 19,810,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `7D` | `10.34` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,760.00 USD |
| `7D` | `10.36` | 19,540,000.00 USD | 0.00 USD | 19,540,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,710.00 USD |
| `7D` | `10.38` | 19,510,000.00 USD | 0.00 USD | 19,510,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,280.00 USD |
| `7D` | `10.40` | 19,450,000.00 USD | 0.00 USD | 19,450,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,920.00 USD |
| `7D` | `10.42` | 19,300,000.00 USD | 0.00 USD | 19,300,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,860.00 USD |
| `7D` | `10.44` | 19,220,000.00 USD | 0.00 USD | 19,220,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,450.00 USD |
| `1D` | `10.46` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 27,560.00 USD | 8,350.00 USD | 22,290.00 USD |
| `7D` | `10.46` | 19,170,000.00 USD | 0.00 USD | 19,170,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,650.00 USD |
| `1D` | `10.48` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD |
| `7D` | `10.48` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,380.00 USD |
| `1D` | `10.50` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 24,480.00 USD | 7,140.00 USD | 8,180.00 USD |
| `7D` | `10.50` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,660.00 USD |
| `1D` | `10.52` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 18,490.00 USD | 3,790.00 USD | 7,610.00 USD |
| `7D` | `10.52` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD |
| `1D` | `10.54` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 4,350.00 USD | 1,600.00 USD | 8,020.00 USD |
| `7D` | `10.54` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,860.00 USD |
| `1D` | `10.56` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 22,600.00 USD | 9,260.00 USD | 4,770.00 USD |
| `7D` | `10.56` | 18,840,000.00 USD | 0.00 USD | 18,840,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,310.00 USD |
| `1D` | `10.58` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,210.00 USD |
| `7D` | `10.58` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,240.00 USD |
| `1D` | `10.60` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD |
| `7D` | `10.60` | 18,640,000.00 USD | 0.00 USD | 18,640,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,590.00 USD |
| `1D` | `10.62` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD |
| `7D` | `10.62` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,170.00 USD |
| `1D` | `10.64` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD |
| `7D` | `10.64` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,430.00 USD |
| `1D` | `10.66` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD |
| `7D` | `10.66` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,240.00 USD |
| `1D` | `10.68` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,580.00 USD |
| `1D` | `10.70` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `10.70` | 18,450,000.00 USD | 0.00 USD | 18,450,000.00 USD | 14,670.00 USD | 0.00 USD | 188.12 USD |
| `1D` | `10.72` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD |
| `7D` | `10.72` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,810.00 USD |
| `1D` | `10.74` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD |
| `7D` | `10.74` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 20,210.00 USD | 4,010.00 USD | 318.38 USD |
| `1D` | `10.76` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD |
| `7D` | `10.76` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 16,310.00 USD | 0.00 USD | 294.21 USD |
| `1D` | `10.78` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD |
| `7D` | `10.78` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 14,200.00 USD | 4,000.00 USD | 23,690.00 USD |
| `1D` | `10.80` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD |
| `7D` | `10.80` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,490.00 USD |
| `1D` | `10.82` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD |
| `7D` | `10.82` | 18,170,000.00 USD | 0.00 USD | 18,170,000.00 USD | 135,080.00 USD | 28,860.00 USD | 10,980.00 USD |
| `1D` | `10.84` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD |
| `7D` | `10.84` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 79,220.00 USD | 38,860.00 USD | 46,230.00 USD |
| `1D` | `10.86` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 976.86 USD | 4,520.00 USD | 3,770.00 USD |
| `7D` | `10.86` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,270.00 USD |
| `7D` | `10.88` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,540.00 USD |
| `1D` | `10.90` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 3,610.00 USD | 3,770.00 USD | 26,510.00 USD |
| `7D` | `10.90` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,670.00 USD |
| `1D` | `10.92` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,390.00 USD |
| `7D` | `10.92` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,080.00 USD |
| `1D` | `10.94` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 47,590.00 USD | 17,110.00 USD | 5,770.00 USD |
| `7D` | `10.94` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,940.00 USD |
| `1D` | `10.96` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD |
| `7D` | `10.96` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,320.00 USD |
| `1D` | `10.98` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD |
| `7D` | `10.98` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 96,870.00 USD | 110,950.00 USD | 161,880.00 USD |
| `1D` | `11.00` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD |
| `7D` | `11.00` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 134,000.00 USD | 91,410.00 USD | 160,860.00 USD |
| `1D` | `11.02` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD |
| `7D` | `11.02` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,840.00 USD |
| `1D` | `11.04` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD |
| `7D` | `11.04` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,840.00 USD |
| `1D` | `11.06` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,340.00 USD |
| `7D` | `11.06` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,800.00 USD |
| `1D` | `11.08` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 30,300.00 USD | 15,060.00 USD | 29,500.00 USD |
| `7D` | `11.08` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,470.00 USD |
| `1D` | `11.10` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 34,720.00 USD | 30,270.00 USD | 32,470.00 USD |
| `7D` | `11.10` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,360.00 USD |
| `1D` | `11.12` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 54,370.00 USD | 33,090.00 USD | 75,860.00 USD |
| `7D` | `11.12` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,950.00 USD |
| `1D` | `11.14` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD |
| `7D` | `11.14` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,600.00 USD |
| `1D` | `11.16` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD |
| `7D` | `11.16` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,990.00 USD |
| `1D` | `11.18` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 137,180.00 USD | 43,130.00 USD | 55,140.00 USD |
| `7D` | `11.18` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 659,190.00 USD | 214,580.00 USD | 541,440.00 USD |
| `1D` | `11.20` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 222,000.00 USD | 47,730.00 USD | 96,770.00 USD |
| `7D` | `11.20` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 371,240.00 USD | 240,290.00 USD | 128,880.00 USD |
| `1D` | `11.22` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 91,270.00 USD | 34,010.00 USD | 48,500.00 USD |
| `7D` | `11.22` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 208,020.00 USD | 228,180.00 USD | 217,320.00 USD |
| `1D` | `11.24` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 116,260.00 USD | 63,910.00 USD | 79,070.00 USD |
| `7D` | `11.24` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 189,850.00 USD | 53,910.00 USD | 63,320.00 USD |
| `7D` | `11.26` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD |
| `1D` | `11.28` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD |
| `7D` | `11.28` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD |
| `7D` | `11.30` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD |
| `1D` | `11.32` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD |
| `7D` | `11.32` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD |
| `1D` | `11.34` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD |
| `7D` | `11.34` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD |
| `1D` | `11.36` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD |
| `7D` | `11.36` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 170,150.00 USD | 48,220.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD |
| `7D` | `11.38` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD |
| `7D` | `11.40` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 106,690.00 USD | 34,500.00 USD | 53,910.00 USD |
| `7D` | `11.42` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 61,980.00 USD | 0.00 USD | 55,710.00 USD |
| `1D` | `11.44` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD |
| `7D` | `11.44` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 148,600.00 USD | 44,370.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 857,200.00 USD | 0.00 USD | 857,200.00 USD | 130,220.00 USD | 30,500.00 USD | 24,850.00 USD |
| `7D` | `11.46` | 769,190.00 USD | 0.00 USD | 769,190.00 USD | 0.00 USD | 10,040.00 USD | 0.00 USD |
| `1D` | `11.48` | 671,620.00 USD | 0.00 USD | 671,620.00 USD | 16,710.00 USD | 14,820.00 USD | 11,950.00 USD |
| `7D` | `11.48` | 759,150.00 USD | 0.00 USD | 759,150.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `11.50` | 628,140.00 USD | 0.00 USD | 628,140.00 USD | 74,140.00 USD | 61,630.00 USD | 14,300.00 USD |
| `7D` | `11.50` | 718,720.00 USD | 0.00 USD | 718,720.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD |
| `1D` | `11.52` | 478,070.00 USD | 0.00 USD | 478,070.00 USD | 13,090.00 USD | 34,130.00 USD | 46,330.00 USD |
| `7D` | `11.52` | 630,580.00 USD | 0.00 USD | 630,580.00 USD | 0.00 USD | 37,540.00 USD | 0.00 USD |
| `1D` | `11.54` | 384,520.00 USD | 0.00 USD | 384,520.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD |
| `7D` | `11.54` | 593,050.00 USD | 0.00 USD | 593,050.00 USD | 34,770.00 USD | 27,190.00 USD | 51,530.00 USD |
| `1D` | `11.56` | 361,920.00 USD | 0.00 USD | 361,920.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD |
| `7D` | `11.56` | 479,570.00 USD | 0.00 USD | 479,570.00 USD | 0.00 USD | 28,460.00 USD | 37,880.00 USD |
| `1D` | `11.58` | 202,960.00 USD | 0.00 USD | 202,960.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD |
| `7D` | `11.58` | 413,220.00 USD | 0.00 USD | 413,220.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 121,320.00 USD | 0.00 USD | 121,320.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD |
| `7D` | `11.60` | 381,600.00 USD | 0.00 USD | 381,600.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.62` | 13,920.00 USD | 0.00 USD | 13,920.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD |
| `7D` | `11.64` | 358,820.00 USD | 0.00 USD | 358,820.00 USD | 68,740.00 USD | 79,630.00 USD | 55,700.00 USD |
| `1D` | `11.66` | 37,590.00 USD | 37,590.00 USD | 0.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD |
| `1D` | `11.66` | 75,180.00 USD | 75,180.00 USD | 0.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD |
| `7D` | `11.66` | 154,750.00 USD | 0.00 USD | 154,750.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 121,100.00 USD | 121,100.00 USD | 0.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD |
| `7D` | `11.68` | 92,780.00 USD | 0.00 USD | 92,780.00 USD | 88,140.00 USD | 4,650.00 USD | 0.00 USD |
| `1D` | `11.70` | 140,560.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD | 230.72 USD | 19,230.00 USD |
| `7D` | `11.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.72` | 317,980.00 USD | 317,980.00 USD | 0.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD |
| `7D` | `11.72` | 195,940.00 USD | 195,940.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 318,310.00 USD | 318,310.00 USD | 0.00 USD | 0.00 USD | 324.58 USD | 0.00 USD |
| `1D` | `11.76` | 318,650.00 USD | 318,650.00 USD | 0.00 USD | 0.00 USD | 342.56 USD | 0.00 USD |
| `7D` | `11.76` | 244,130.00 USD | 244,130.00 USD | 0.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 335,680.00 USD | 335,680.00 USD | 0.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD |
| `1D` | `11.80` | 336,740.00 USD | 336,740.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `11.80` | 384,250.00 USD | 384,250.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.82` | 545,000.00 USD | 545,000.00 USD | 0.00 USD | 158,640.00 USD | 1,970.00 USD | 133.38 USD |
| `1D` | `11.84` | 420,660.00 USD | 420,660.00 USD | 0.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD |
| `7D` | `11.84` | 764,330.00 USD | 764,330.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 10.32 USD |
| `1D` | `11.86` | 492,810.00 USD | 492,810.00 USD | 0.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD |
| `7D` | `11.86` | 770,990.00 USD | 770,990.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | 42.92 USD |
| `1D` | `11.88` | 548,760.00 USD | 548,760.00 USD | 0.00 USD | 19,640.00 USD | 15,360.00 USD | 20,940.00 USD |
| `7D` | `11.88` | 783,970.00 USD | 783,970.00 USD | 0.00 USD | 10,340.00 USD | 2,480.00 USD | 165.54 USD |
| `1D` | `11.90` | 592,970.00 USD | 592,970.00 USD | 0.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD |
| `7D` | `11.90` | 795,940.00 USD | 795,940.00 USD | 0.00 USD | 11,220.00 USD | 612.37 USD | 145.40 USD |
| `1D` | `11.92` | 618,570.00 USD | 618,570.00 USD | 0.00 USD | 12,480.00 USD | 13,090.00 USD | 20.02 USD |
| `7D` | `11.92` | 803,120.00 USD | 803,120.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | 169.96 USD |
| `1D` | `11.94` | 630,270.00 USD | 630,270.00 USD | 0.00 USD | 1,220.00 USD | 4,890.00 USD | 5,590.00 USD |
| `7D` | `11.94` | 993,220.00 USD | 993,220.00 USD | 0.00 USD | 17,060.00 USD | 24,600.00 USD | 148,450.00 USD |
| `1D` | `11.96` | 697,020.00 USD | 697,020.00 USD | 0.00 USD | 12,210.00 USD | 26,690.00 USD | 27,850.00 USD |
| `7D` | `11.96` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 6,640.00 USD | 1,490.00 USD | 151,660.00 USD |
| `1D` | `11.98` | 833,980.00 USD | 833,980.00 USD | 0.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD |
| `7D` | `11.98` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 391,180.00 USD | 34,700.00 USD | 190,650.00 USD |
| `1D` | `12.00` | 982,170.00 USD | 982,170.00 USD | 0.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD |
| `7D` | `12.00` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 304,560.00 USD | 7,460.00 USD | 183,600.00 USD |
| `1D` | `12.02` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD |
| `7D` | `12.02` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 244,440.00 USD | 47,410.00 USD | 222,490.00 USD |
| `1D` | `12.04` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD |
| `7D` | `12.04` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 292,690.00 USD | 137,340.00 USD | 179,710.00 USD |
| `1D` | `12.06` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD |
| `7D` | `12.06` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 234,210.00 USD | 101,560.00 USD | 145,610.00 USD |
| `1D` | `12.08` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD |
| `7D` | `12.08` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 165,220.00 USD |
| `1D` | `12.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD |
| `7D` | `12.10` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 141,930.00 USD | 49,190.00 USD | 50,370.00 USD |
| `7D` | `12.12` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 174,090.00 USD | 67,240.00 USD | 119,400.00 USD |
| `1D` | `12.14` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 109,520.00 USD | 28,690.00 USD | 53,490.00 USD |
| `7D` | `12.14` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 118,920.00 USD | 65,050.00 USD | 93,050.00 USD |
| `1D` | `12.16` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 90,900.00 USD | 61,100.00 USD | 64,580.00 USD |
| `7D` | `12.16` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 183,570.00 USD | 86,510.00 USD | 72,100.00 USD |
| `1D` | `12.18` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 122,240.00 USD | 44,200.00 USD | 42,030.00 USD |
| `7D` | `12.18` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 57,680.00 USD | 42,810.00 USD | 31,960.00 USD |
| `1D` | `12.20` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 94,060.00 USD | 48,470.00 USD | 32,760.00 USD |
| `7D` | `12.20` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 194,760.00 USD | 51,340.00 USD | 78,380.00 USD |
| `1D` | `12.22` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 29,450.00 USD | 42,870.00 USD | 52,640.00 USD |
| `7D` | `12.22` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 261,490.00 USD | 56,370.00 USD | 93,640.00 USD |
| `1D` | `12.24` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 35,430.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.24` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 70,650.00 USD | 58,900.00 USD | 114,600.00 USD |
| `1D` | `12.26` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 59,230.00 USD | 27,170.00 USD | 21,490.00 USD |
| `7D` | `12.26` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 202,660.00 USD | 56,010.00 USD | 50,570.00 USD |
| `1D` | `12.28` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 99,490.00 USD | 24,800.00 USD | 37,620.00 USD |
| `7D` | `12.28` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 238,210.00 USD | 76,160.00 USD | 170,690.00 USD |
| `1D` | `12.30` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 59,030.00 USD | 24,040.00 USD | 45,440.00 USD |
| `7D` | `12.30` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 178,010.00 USD | 79,440.00 USD | 96,690.00 USD |
| `1D` | `12.32` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.32` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 120,640.00 USD | 46,590.00 USD | 18,010.00 USD |
| `1D` | `12.34` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD |
| `7D` | `12.34` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 158,050.00 USD | 81,530.00 USD | 13,430.00 USD |
| `1D` | `12.36` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD |
| `7D` | `12.36` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 97,320.00 USD | 30,690.00 USD | 18,500.00 USD |
| `1D` | `12.38` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD |
| `7D` | `12.38` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 166,020.00 USD |
| `1D` | `12.40` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD |
| `7D` | `12.40` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 196,150.00 USD | 41,260.00 USD | 258,500.00 USD |
| `1D` | `12.42` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 51,980.00 USD | 13,980.00 USD | 9,680.00 USD |
| `7D` | `12.42` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 18,760.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.44` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 162,080.00 USD | 68,340.00 USD | 247,990.00 USD |
| `1D` | `12.46` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 2,900.00 USD | 15,260.00 USD | 11,590.00 USD |
| `7D` | `12.46` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 84,310.00 USD | 78,160.00 USD | 86,180.00 USD |
| `1D` | `12.48` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 2,220.00 USD | 2,560.00 USD | 8,380.00 USD |
| `7D` | `12.48` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 31,320.00 USD | 20,570.00 USD | 180,460.00 USD |
| `1D` | `12.50` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 1,320.00 USD | 4,320.00 USD | 8,230.00 USD |
| `7D` | `12.50` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 153,430.00 USD | 20,380.00 USD | 74,680.00 USD |
| `1D` | `12.52` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD |
| `7D` | `12.52` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 165,890.00 USD | 45,040.00 USD | 125,090.00 USD |
| `1D` | `12.54` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD |
| `7D` | `12.54` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 96,800.00 USD | 59,960.00 USD | 107,090.00 USD |
| `1D` | `12.56` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.56` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 128,070.00 USD | 30,820.00 USD | 27,480.00 USD |
| `1D` | `12.58` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD |
| `7D` | `12.58` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 97,670.00 USD | 66,210.00 USD | 41,120.00 USD |
| `1D` | `12.60` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD |
| `7D` | `12.60` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 56,420.00 USD | 26,450.00 USD | 39,140.00 USD |
| `1D` | `12.62` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,130.00 USD |
| `1D` | `12.64` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD |
| `7D` | `12.64` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,820.00 USD |
| `1D` | `12.66` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD |
| `7D` | `12.66` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 43,740.00 USD | 9,020.00 USD | 99,100.00 USD |
| `1D` | `12.68` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD |
| `7D` | `12.68` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,470.00 USD |
| `1D` | `12.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD |
| `7D` | `12.70` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 22,060.00 USD | 50,120.00 USD | 142,780.00 USD |
| `1D` | `12.72` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD |
| `7D` | `12.72` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,170.00 USD |
| `1D` | `12.74` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD |
| `7D` | `12.74` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 20,890.00 USD |
| `1D` | `12.76` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD |
| `7D` | `12.76` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 15,760.00 USD | 6,360.00 USD | 29,510.00 USD |
| `1D` | `12.78` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.78` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 78,020.00 USD | 15,750.00 USD | 18,720.00 USD |
| `1D` | `12.80` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD |
| `7D` | `12.80` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,530.00 USD |
| `1D` | `12.82` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 2,680.00 USD | 1,320.00 USD | 1,990.00 USD |
| `7D` | `12.82` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 4,980.00 USD |
| `1D` | `12.84` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 21,810.00 USD | 5,820.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 29,710.00 USD | 15,990.00 USD | 7,980.00 USD |
| `1D` | `12.86` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 18,490.00 USD | 3,790.00 USD | 7,570.00 USD |
| `7D` | `12.86` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD |
| `1D` | `12.88` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 3,720.00 USD | 1,600.00 USD | 8,020.00 USD |
| `7D` | `12.88` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 24,580.00 USD | 4,610.00 USD | 12,750.00 USD |
| `1D` | `12.90` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 21,720.00 USD | 9,260.00 USD | 4,770.00 USD |
| `7D` | `12.90` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,200.00 USD |
| `1D` | `12.92` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD |
| `7D` | `12.92` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 11,060.00 USD |
| `1D` | `12.94` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.94` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 123.98 USD |
| `1D` | `12.96` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,220.00 USD |
| `7D` | `12.96` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 14,650.00 USD | 11,970.00 USD | 10,480.00 USD |
| `1D` | `12.98` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 24,650.00 USD | 7,080.00 USD | 12,040.00 USD |
| `7D` | `12.98` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 19,020.00 USD |
| `1D` | `13.00` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD |
| `7D` | `13.00` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD |
| `1D` | `13.02` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD |
| `7D` | `13.02` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `1D` | `13.04` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `13.04` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 303.50 USD | 0.00 USD | 0.00 USD |
| `1D` | `13.06` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 9,530.00 USD | 1,380.00 USD | 1,550.00 USD |
| `7D` | `13.06` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD |
| `1D` | `13.08` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 7,160.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `13.10` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 18,460.00 USD | 5,730.00 USD | 7,630.00 USD |
| `7D` | `13.12` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 945.50 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.14` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 321.45 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.16` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41.47 USD |
| `7D` | `13.18` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 193.15 USD | 4,000.00 USD | 8,380.00 USD |
| `7D` | `13.20` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 18,640.00 USD |
| `7D` | `13.22` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 23,980.00 USD | 259.77 USD | 22.55 USD |
| `7D` | `13.24` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 23,250.00 USD | 4,640.00 USD | 11,820.00 USD |
| `7D` | `13.26` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 463.75 USD | 8,520.00 USD | 10,920.00 USD |
| `7D` | `13.28` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 14,470.00 USD | 5,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `554.29M` | Total OI Tokens: `47,620,963.7 LINK`
  * 1h OI Change: `-0.65%` | 4h OI Change: `-1.46%` | 24h OI Change: `-2.48%`
  * Exchange Breakdown: Binance=`105.26M` | Bybit=`65.41M` | OKX=`26.43M` | Hyperliquid=`56.42M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.36K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0045%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0078%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `53.97%` | `46.03%` | `1.17` | 896,500.00 USD |
| `15M` | `Binance` | `64.75%` | `35.25%` | `1.84` | 395,080.00 USD |
| `15M` | `OKX` | `46.55%` | `53.45%` | `0.87` | 39,830.00 USD |
| `15M` | `Bybit` | `72.71%` | `27.29%` | `2.66` | 101,820.00 USD |
| `15M` | `KuCoin` | `42.48%` | `57.52%` | `0.74` | 14,970.00 USD |
| `15M` | `Gate` | `41.29%` | `58.71%` | `0.70` | 18,270.00 USD |
| `15M` | `Bitget` | `36.88%` | `63.12%` | `0.58` | 6,400.00 USD |
| `15M` | `BingX` | `52.55%` | `47.45%` | `1.11` | 33,970.00 USD |
| `15M` | `MEXC` | `53.26%` | `46.74%` | `1.14` | 3,300.00 USD |
| `15M` | `Bitunix` | `54.95%` | `45.05%` | `1.22` | 9,680.00 USD |
| `15M` | `Hyperliquid` | `83.02%` | `16.98%` | `4.89` | 31,390.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.86%` | `50.14%` | `0.99` | 99,020.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `8.76%` | `91.24%` | `0.10` | 131,750.00 USD |
| `15M` | `HTX` | `71.83%` | `28.17%` | `2.55` | 10,110.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `8.81%` | `91.19%` | `0.10` | 428.49 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 318.44 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 177.31 USD |
| `15M` | `Whale Positions` | `64.75%` | `35.25%` | `1.84` | 395,080.00 USD |
| `15M` | `Global Accounts` | `53.97%` | `46.03%` | `1.17` | 896,500.00 USD |
| `1H` | `LINK` | `44.67%` | `55.33%` | `0.81` | 2,840,000.00 USD |
| `1H` | `Binance` | `47.4%` | `52.6%` | `0.90` | 1,080,000.00 USD |
| `1H` | `OKX` | `39.55%` | `60.45%` | `0.65` | 161,390.00 USD |
| `1H` | `Bybit` | `41.96%` | `58.04%` | `0.72` | 144,950.00 USD |
| `1H` | `KuCoin` | `49.86%` | `50.14%` | `0.99` | 60,640.00 USD |
| `1H` | `Gate` | `45.68%` | `54.32%` | `0.84` | 64,540.00 USD |
| `1H` | `Bitget` | `44.8%` | `55.2%` | `0.81` | 55,780.00 USD |
| `1H` | `BingX` | `46.69%` | `53.31%` | `0.88` | 127,640.00 USD |
| `1H` | `MEXC` | `49.48%` | `50.52%` | `0.98` | 16,610.00 USD |
| `1H` | `Bitunix` | `49.42%` | `50.58%` | `0.98` | 34,230.00 USD |
| `1H` | `Hyperliquid` | `14.38%` | `85.62%` | `0.17` | 63,340.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.57%` | `45.43%` | `1.20` | 535,590.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 427,650.00 USD |
| `1H` | `HTX` | `30.26%` | `69.74%` | `0.43` | 46,460.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `21.4%` | `78.6%` | `0.27` | 9,420.00 USD |
| `1H` | `Aster` | `2.97%` | `97.03%` | `0.03` | 2,230.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.95%` | `56.05%` | `0.78` | 2,120.00 USD |
| `1H` | `Whale Positions` | `47.4%` | `52.6%` | `0.90` | 1,080,000.00 USD |
| `1H` | `Global Accounts` | `44.67%` | `55.33%` | `0.81` | 2,840,000.00 USD |
| `4H` | `LINK` | `45.19%` | `54.81%` | `0.82` | 12,210,000.00 USD |
| `4H` | `Binance` | `52.04%` | `47.96%` | `1.09` | 4,400,000.00 USD |
| `4H` | `OKX` | `46.56%` | `53.44%` | `0.87` | 785,140.00 USD |
| `4H` | `Bybit` | `51.18%` | `48.82%` | `1.05` | 627,040.00 USD |
| `4H` | `KuCoin` | `48.97%` | `51.03%` | `0.96` | 270,220.00 USD |
| `4H` | `Gate` | `60.61%` | `39.39%` | `1.54` | 304,620.00 USD |
| `4H` | `Bitget` | `57.41%` | `42.59%` | `1.35` | 179,830.00 USD |
| `4H` | `BingX` | `25.03%` | `74.97%` | `0.33` | 1,080,000.00 USD |
| `4H` | `MEXC` | `60.68%` | `39.32%` | `1.54` | 147,200.00 USD |
| `4H` | `Bitunix` | `49.38%` | `50.62%` | `0.98` | 135,090.00 USD |
| `4H` | `Hyperliquid` | `84.32%` | `15.68%` | `5.38` | 423,470.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.09%` | `49.91%` | `1.00` | 1,930,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.63%` | `90.37%` | `0.11` | 1,520,000.00 USD |
| `4H` | `HTX` | `53.57%` | `46.43%` | `1.15` | 197,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `70.8%` | `29.2%` | `2.42` | 134,890.00 USD |
| `4H` | `Aster` | `22.6%` | `77.4%` | `0.29` | 8,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `28.56%` | `71.44%` | `0.40` | 63,880.00 USD |
| `4H` | `Whale Positions` | `52.04%` | `47.96%` | `1.09` | 4,400,000.00 USD |
| `4H` | `Global Accounts` | `45.19%` | `54.81%` | `0.82` | 12,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.86` | `11.86` | `11.86` | `11.91` | `11.82` | 2,416,227.23 USD | 1,033,147.61 USD | 1,383,079.61 USD | -349,932.00 USD | `-14.48%` | `6B / 27S` |
| `5:00 UTC` | `11.84` | `11.85` | `11.84` | `11.87` | `11.83` | 923,896.67 USD | 361,612.35 USD | 562,284.32 USD | -200,671.96 USD | `-21.72%` | `4B / 14S` |
| `0:00 UTC` | `11.83` | `11.83` | `11.83` | `11.87` | `11.79` | 1,261,426.96 USD | 528,120.38 USD | 733,306.58 USD | -205,186.20 USD | `-16.27%` | `8B / 14S` |
| `5:00 UTC` | `11.80` | `11.80` | `11.80` | `11.83` | `11.79` | 889,528.52 USD | 480,169.70 USD | 409,358.82 USD | 70,810.88 USD | `+7.96%` | `8B / 3S` |
| `0:00 UTC` | `11.78` | `11.76` | `11.78` | `11.84` | `11.71` | 1,746,825.55 USD | 823,777.15 USD | 923,048.41 USD | -99,271.26 USD | `-5.68%` | `22B / 37S` |
| `5:00 UTC` | `11.71` | `11.70` | `11.71` | `11.74` | `11.66` | 1,705,508.25 USD | 855,092.75 USD | 850,415.50 USD | 4,677.25 USD | `+0.27%` | `14B / 10S` |
| `0:00 UTC` | `11.73` | `11.73` | `11.73` | `11.75` | `11.71` | 756,364.68 USD | 311,101.50 USD | 445,263.18 USD | -134,161.69 USD | `-17.74%` | `6B / 13S` |
| `5:00 UTC` | `11.74` | `11.73` | `11.74` | `11.76` | `11.69` | 1,033,883.46 USD | 539,127.77 USD | 494,755.69 USD | 44,372.08 USD | `+4.29%` | `15B / 13S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.66` | `11.66` | `11.66` | `11.69` | `11.64` | 383,510.74 USD | 270,187.83 USD | 113,322.91 USD | 156,864.92 USD | `+40.90%` | `19B / 8S` |

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
| `5m` | 3,890.00 USD | -94,050.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,820.00 USD | -605,240.00 USD | **`DISTRIBUTION`** |
| `30m` | 8,040.00 USD | -654,500.00 USD | **`DISTRIBUTION`** |
| `1h` | -197,980.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -988,160.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 376,350.00 USD | -2,210,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 280,860.00 USD | -1,720,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 524,250.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 503,330.00 USD | 110,780.00 USD | **`ACCUMULATION`** |
| `24h` | 664,070.00 USD | -3,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,770,000.00 USD | -23,940,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -68,340,000.00 USD | -187,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.89K` | 15m=`-2.82K` | 1h=`-197.98K` | 24h=`+664.07K`
* Futures Capital Netflows: 5m=`-94.05K` | 15m=`-605.24K` | 1h=`-1.19M` | 24h=`-3.37M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `11.22` (Risk Distance: `0.2198` pts)
  * +2.5R Take Profit: `11.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.13` (Risk Distance: `0.2198` pts)
  * +2.5R Take Profit: `11.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
