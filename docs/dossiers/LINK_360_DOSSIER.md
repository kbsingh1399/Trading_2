# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 01:45:08 IST` (`2026-10-29 20:15:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.46` | **Live Ask Quote**: `11.55` | **Mid Price**: `11.50`
- **Spread Points**: `88.00` | **Spread BPS**: `76.49 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.57` | VWAP Z-Score: `+0.38` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0684` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.10` | Lower -3.00σ Band: `11.04`
  * Upper +2.51σ Band: `12.02` | Lower -2.51σ Band: `11.12`
  * Upper +2.01σ Band: `11.93` | Lower -2.01σ Band: `11.21`
  * Upper +2.00σ Band: `11.92` | Lower -2.00σ Band: `11.21`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.34`
  * Upper +1.00σ Band: `11.75` | Lower -1.00σ Band: `11.39`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.65` | EMA-20=`11.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.63` (Slope: `+0.0000`) | EMA-100=`11.60`
  * Institutional Anchors: EMA-144=`11.57` | EMA-200=`11.54` (Slope: `+0.1365`) | EMA-233=`11.52`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`11.23` | Weekly High=`11.96` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.89` (Distance: `-3.25%`)
  * Point of Control (POC) = `11.77` (Distance: `-2.26%`)
  * Value Area Low (VAL) = `11.44` (Distance: `+0.56%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `11.46` - `11.55`
  * Optimal Trade Entry (OTE 0.705): `11.53`
  * Structural Invalidation Anchor (0.786): `11.60`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.69` | `11.69` | `11.49` | `11.49` | `246,331` | 2,851,673.47 USD | -868,106.04 USD | `-30.44%` | -3,092,969.50 USD | `-3.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.49` | `11.54` | `11.42` | `11.49` | `268,355` | 3,078,532.41 USD | 334,573.87 USD | `+10.87%` | -2,758,395.63 USD | `+1.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.49` | `11.53` | `11.45` | `11.52` | `77,131` | 886,435.31 USD | 334,683.46 USD | `+37.76%` | -2,423,712.17 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.68` | `11.73` | `11.68` | `11.70` | `104,962` | 1,229,457.09 USD | 216,436.63 USD | `+17.60%` | -2,297,926.82 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.70` | `11.72` | `11.68` | `11.69` | `54,635` | 638,959.31 USD | 73,063.35 USD | `+11.43%` | -2,224,863.46 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.69` | `11.69` | `11.42` | `11.52` | `591,817` | 6,816,641.20 USD | -198,848.71 USD | `-2.92%` | -2,423,712.17 USD | `-0.51` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.68` | `461,460` | 5,390,854.94 USD | 388,230.26 USD | `+7.20%` | -2,106,527.93 USD | `+0.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.73` | `11.63` | `11.69` | `318,927` | 3,725,220.26 USD | -245,323.17 USD | `-6.59%` | -2,351,851.10 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.69` | `11.69` | `11.42` | `11.52` | `591,817` | 6,816,641.20 USD | -198,848.71 USD | `-2.92%` | -2,550,699.81 USD | `-0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `11.42` | `11.52` | `592,363` | 6,822,935.15 USD | -204,897.71 USD | `-3.00%` | -1,923,395.31 USD | `+0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `11.42` | `11.52` | `592,363` | 6,822,935.15 USD | -204,897.71 USD | `-3.00%` | -1,923,395.31 USD | `+0.10` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`11.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `493` | `0x73ce...8ce9` | `LONG` | 4,582,932.90 USD | `400,011,600.00` | `12.05` | `11.44` | `9.13` | -236,820.80 USD | `-5.17%` | `5X Cross` |
| `638` | `0xb83d...6e36` | `SHORT` | 3,600,010.39 USD | `308,152,000.00` | `12.93` | `11.44` | `421.29` | 385,243.10 USD | `+10.70%` | `3X Cross` |
| `644` | `0x5b5d...c060` | `SHORT` | 3,564,923.70 USD | `311,728,200.00` | `13.61` | `11.44` | `522.37` | 677,208.41 USD | `+19.00%` | `3X Cross` |
| `859` | `0x458d...ab3b` | `LONG` | 2,657,051.92 USD | `227,156,700.00` | `13.13` | `11.44` | `9.34` | -325,178.48 USD | `-12.24%` | `3X Isolated` |
| `949` | `0xdd53...2b13` | `SHORT` | 2,379,834.31 USD | `206,475,300.00` | `11.92` | `11.44` | `282.03` | 81,388.62 USD | `+3.42%` | `3X Cross` |
| `968` | `0x3dc9...54b0` | `SHORT` | 2,336,300.00 USD | `200,000,000.00` | `7.56` | `11.44` | `82.52` | -825,141.58 USD | `-35.32%` | `10X Cross` |
| `1003` | `0x45d2...4029` | `SHORT` | 2,244,340.00 USD | `195,500,000.00` | `11.54` | `11.44` | `200.96` | 12,143.43 USD | `+0.54%` | `10X Cross` |
| `1212` | `0x6540...f7b7` | `LONG` | 1,878,810.45 USD | `163,759,300.00` | `12.48` | `11.43` | `8.01` | -164,366.48 USD | `-8.75%` | `5X Isolated` |
| `1249` | `0xeadc...9d55` | `LONG` | 1,842,468.65 USD | `157,691,600.00` | `9.43` | `11.43` | `0.000000` | 355,813.75 USD | `+19.31%` | `10X Cross` |
| `1632` | `0x9df2...c665` | `SHORT` | 1,353,585.76 USD | `117,905,600.00` | `11.48` | `11.43` | `259.82` | 432.52 USD | `+0.03%` | `10X Cross` |
| `1649` | `0xf6f3...47f8` | `SHORT` | 1,323,127.97 USD | `115,024,600.00` | `11.42` | `11.43` | `19.20` | -9,797.79 USD | `-0.74%` | `5X Cross` |
| `1803` | `0xfe7e...11b4` | `LONG` | 1,171,123.22 USD | `101,142,000.00` | `14.47` | `11.43` | `5.33` | -291,989.93 USD | `-24.93%` | `5X Isolated` |
| `1844` | `0x8af7...fa05` | `SHORT` | 1,137,119.66 USD | `98,661,200.00` | `14.08` | `11.43` | `204.32` | 252,062.88 USD | `+22.17%` | `10X Cross` |
| `1883` | `0xb7ec...5166` | `LONG` | 1,104,701.84 USD | `94,515,900.00` | `9.01` | `11.43` | `7.20` | 252,841.26 USD | `+22.89%` | `4X Cross` |

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
| `Live` | `Long Liquidation` | `2.35` | 4,510.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 30,100.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,240.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 220.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 7,930.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 650.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 927.95 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 369.15 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 302.46 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 379.88 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 9,940.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 2,090.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 2,150.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 264.05 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 222,950.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,200.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 22,190.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 55,550.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 31,030.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,210.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 633,510.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 499.77 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 10,170.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 43,840.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 5,120.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 32,070.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 909.76 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 48,450.00 USD | 12,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,490.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,590.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 141,680.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 15,940.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,820.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,700.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 2,740.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 687,520.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 20,150.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 30,960.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 10,880.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 17,030.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,150.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 2,890.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 726.91 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 41,640.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,390,000.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,320.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 34,670.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,770.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 10,670.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 43,900.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 11,540.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 304,290.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 35,020.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,640.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 42,820.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,760,000.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 25,310.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,170,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 19,500.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 14,380.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 8,830.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 103,770.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 17,700.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 782,600.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 645,720.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 44,810.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.24` | 20,290,000.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 278,400.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 19,910,000.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.27` | 5,840,000.00 USD | 5,840,000.00 USD | 25,950.00 USD | 5,810.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 19,770,000.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 5,800,000.00 USD | 5,800,000.00 USD | 14,970.00 USD | 6,380.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 19,650,000.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 5,770,000.00 USD | 5,770,000.00 USD | 20,160.00 USD | 4,360.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 19,540,000.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 5,730,000.00 USD | 5,730,000.00 USD | 25,720.00 USD | 9,500.00 USD | 11,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 19,400,000.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 5,680,000.00 USD | 5,680,000.00 USD | 3,750.00 USD | 4,250.00 USD | 4.92 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 9,660.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 19,270,000.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.37` | 5,680,000.00 USD | 5,680,000.00 USD | 156.89 USD | 3,710.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 19,240,000.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 5,670,000.00 USD | 5,670,000.00 USD | 2,580.00 USD | 1,810.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 19,180,000.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 5,650,000.00 USD | 5,650,000.00 USD | 21,850.00 USD | 9,160.00 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 19,030,000.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 5,620,000.00 USD | 5,620,000.00 USD | 32,610.00 USD | 11,330.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 18,950,000.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 5,570,000.00 USD | 5,570,000.00 USD | 22,830.00 USD | 9,270.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 175,650.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.46` | 18,890,000.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.47` | 5,530,000.00 USD | 5,530,000.00 USD | 9,880.00 USD | 2,060.00 USD | 11,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 18,780,000.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 5,500,000.00 USD | 5,500,000.00 USD | 24,450.00 USD | 9,610.00 USD | 17,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 18,730,000.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 5,450,000.00 USD | 5,450,000.00 USD | 25,860.00 USD | 4,270.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 18,660,000.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 5,410,000.00 USD | 5,410,000.00 USD | 8,070.00 USD | 5,270.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 18,590,000.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 5,400,000.00 USD | 5,400,000.00 USD | 7,160.00 USD | 2,730.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,130.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.56` | 18,550,000.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.57` | 5,390,000.00 USD | 5,390,000.00 USD | 16,060.00 USD | 4,520.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 18,460,000.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 5,360,000.00 USD | 5,360,000.00 USD | 14,080.00 USD | 2,760.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 18,350,000.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 5,340,000.00 USD | 5,340,000.00 USD | 12,640.00 USD | 7,830.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 18,300,000.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 5,310,000.00 USD | 5,310,000.00 USD | 22,390.00 USD | 5,060.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 18,250,000.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 5,270,000.00 USD | 5,270,000.00 USD | 18,690.00 USD | 3,770.00 USD | 14,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.66` | 18,200,000.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.67` | 5,230,000.00 USD | 5,230,000.00 USD | 442.43 USD | 1,480.00 USD | 10.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 18,180,000.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 5,230,000.00 USD | 5,230,000.00 USD | 11,810.00 USD | 3,650.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 18,150,000.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 5,210,000.00 USD | 5,210,000.00 USD | 3,410.00 USD | 1,570.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 18,130,000.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 5,210,000.00 USD | 5,210,000.00 USD | 6,610.00 USD | 3,000.00 USD | 6,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 18,090,000.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 5,190,000.00 USD | 5,190,000.00 USD | 20,270.00 USD | 4,650.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.76` | 18,070,000.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.77` | 5,160,000.00 USD | 5,160,000.00 USD | 5,310.00 USD | 4,090.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 18,050,000.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 5,150,000.00 USD | 5,150,000.00 USD | 2,790.00 USD | 2,540.00 USD | 30.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 18,010,000.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 5,140,000.00 USD | 5,140,000.00 USD | 1,970.00 USD | 0.00 USD | 22.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 17,870,000.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.83` | 5,140,000.00 USD | 5,140,000.00 USD | 2,830.00 USD | 160.15 USD | 76.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,690,000.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.85` | 5,140,000.00 USD | 5,140,000.00 USD | 1,690.00 USD | 4,450.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 85,390.00 USD | 866,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.86` | 17,540,000.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.87` | 5,130,000.00 USD | 5,130,000.00 USD | 576.29 USD | 2,760.00 USD | 209.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 17,190,000.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.89` | 5,120,000.00 USD | 5,120,000.00 USD | 1,860.00 USD | 11,320.00 USD | 36,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 16,720,000.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.91` | 5,070,000.00 USD | 5,070,000.00 USD | 685.29 USD | 10,840.00 USD | 25,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 16,290,000.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.93` | 5,040,000.00 USD | 5,040,000.00 USD | 96,860.00 USD | 28,100.00 USD | 41,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 15,390,000.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.95` | 4,870,000.00 USD | 4,870,000.00 USD | 45,000.00 USD | 14,550.00 USD | 17,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,110.00 USD | 781,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.96` | 14,800,000.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.97` | 4,790,000.00 USD | 4,790,000.00 USD | 80,360.00 USD | 15,940.00 USD | 33,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 14,240,000.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.99` | 4,660,000.00 USD | 4,660,000.00 USD | 48,940.00 USD | 15,200.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 13,870,000.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.01` | 4,580,000.00 USD | 4,580,000.00 USD | 53,360.00 USD | 23,840.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 13,480,000.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.03` | 4,480,000.00 USD | 4,480,000.00 USD | 68,450.00 USD | 12,950.00 USD | 21,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,970,000.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.05` | 4,380,000.00 USD | 4,380,000.00 USD | 14,150.00 USD | 402.52 USD | 8,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 147,130.00 USD | 223,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.06` | 12,320,000.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.07` | 4,350,000.00 USD | 4,350,000.00 USD | 25,280.00 USD | 21,300.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 11,910,000.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.09` | 4,280,000.00 USD | 4,280,000.00 USD | 9,540.00 USD | 9,350.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 11,100,000.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.11` | 4,250,000.00 USD | 4,250,000.00 USD | 52,180.00 USD | 45,500.00 USD | 79,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 9,910,000.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.13` | 4,070,000.00 USD | 4,070,000.00 USD | 89,330.00 USD | 55,180.00 USD | 89,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 8,860,000.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.15` | 3,830,000.00 USD | 3,830,000.00 USD | 188,500.00 USD | 67,260.00 USD | 112,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 25,090.00 USD | 75,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.16` | 7,370,000.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.17` | 3,470,000.00 USD | 3,470,000.00 USD | 153,150.00 USD | 52,240.00 USD | 66,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 6,060,000.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.19` | 3,190,000.00 USD | 3,190,000.00 USD | 257,350.00 USD | 63,490.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,630,000.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.21` | 2,780,000.00 USD | 2,780,000.00 USD | 113,460.00 USD | 22,410.00 USD | 77,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,870,000.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.23` | 2,570,000.00 USD | 2,570,000.00 USD | 131,420.00 USD | 43,780.00 USD | 58,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 3,160,000.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.25` | 2,330,000.00 USD | 2,330,000.00 USD | 205,010.00 USD | 55,560.00 USD | 73,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 41,990.00 USD | 50,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,860,000.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.27` | 2,000,000.00 USD | 2,000,000.00 USD | 72,930.00 USD | 38,810.00 USD | 31,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 2,290,000.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.29` | 1,860,000.00 USD | 1,860,000.00 USD | 77,300.00 USD | 26,000.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,880,000.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.31` | 1,720,000.00 USD | 1,720,000.00 USD | 67,970.00 USD | 15,830.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,810,000.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.33` | 1,600,000.00 USD | 1,600,000.00 USD | 140,030.00 USD | 27,960.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,640,000.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.35` | 1,410,000.00 USD | 1,410,000.00 USD | 146,250.00 USD | 85,790.00 USD | 54,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 8,900.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.36` | 1,280,000.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.37` | 1,120,000.00 USD | 1,120,000.00 USD | 160,130.00 USD | 58,390.00 USD | 93,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 962,530.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.39` | 809,070.00 USD | 809,070.00 USD | 54,830.00 USD | 37,490.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 871,150.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.41` | 665,870.00 USD | 665,870.00 USD | 114,970.00 USD | 34,560.00 USD | 83,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 677,690.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.43` | 432,640.00 USD | 432,640.00 USD | 50,600.00 USD | 26,360.00 USD | 88,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 536,960.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.45` | 267,410.00 USD | 267,410.00 USD | 0.00 USD | 83.92 USD | 68,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.46` | 264,830.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.47` | 199,020.00 USD | 199,020.00 USD | 0.00 USD | 30.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 128,570.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.49` | 170,550.00 USD | 170,550.00 USD | 10,420.00 USD | 18,420.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 88,130.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.51` | 126,250.00 USD | 126,250.00 USD | 83,540.00 USD | 0.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 37,210.00 USD | 37,210.00 USD | 13,090.00 USD | 0.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 94,830.00 USD | 94,830.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 83,270.00 USD | 83,270.00 USD | 21,770.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.57` | 233,550.00 USD | 233,550.00 USD | 77,390.00 USD | 0.00 USD | 72,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 273,530.00 USD | 273,530.00 USD | 11,470.00 USD | 75.80 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 340,430.00 USD | 340,430.00 USD | 66,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 222,010.00 USD | 222,010.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 410,070.00 USD | 410,070.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 541,040.00 USD | 541,040.00 USD | 118,160.00 USD | 12,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 484,570.00 USD | 484,570.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 587,780.00 USD | 587,780.00 USD | 46,440.00 USD | 300.68 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 602,310.00 USD | 602,310.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 532,760.00 USD | 532,760.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 619,270.00 USD | 619,270.00 USD | 16,180.00 USD | 777.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 620,030.00 USD | 620,030.00 USD | 0.00 USD | 755.20 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 672,880.00 USD | 672,880.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 633,970.00 USD | 633,970.00 USD | 0.00 USD | 13,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 873,430.00 USD | 873,430.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 645,470.00 USD | 645,470.00 USD | 0.00 USD | 11,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 789,050.00 USD | 789,050.00 USD | 55,600.00 USD | 22,590.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 872,890.00 USD | 872,890.00 USD | 19,640.00 USD | 26,360.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 942,980.00 USD | 942,980.00 USD | 44,160.00 USD | 11,410.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 1,040,000.00 USD | 1,040,000.00 USD | 62,930.00 USD | 18,340.00 USD | 18,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 1,180,000.00 USD | 1,180,000.00 USD | 78,080.00 USD | 27,850.00 USD | 28,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 1,220,000.00 USD | 1,220,000.00 USD | 1,220.00 USD | 14,280.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 1,350,000.00 USD | 1,350,000.00 USD | 44,480.00 USD | 27,610.00 USD | 60,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 1,440,000.00 USD | 1,440,000.00 USD | 38,440.00 USD | 7,350.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 1,540,000.00 USD | 1,540,000.00 USD | 73,670.00 USD | 467.98 USD | 26,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 1,810,000.00 USD | 1,810,000.00 USD | 155,160.00 USD | 72,030.00 USD | 49,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 2,230,000.00 USD | 2,230,000.00 USD | 234,920.00 USD | 68,310.00 USD | 113,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 2,590,000.00 USD | 2,590,000.00 USD | 169,050.00 USD | 63,630.00 USD | 125,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 2,640,000.00 USD | 2,640,000.00 USD | 17,390.00 USD | 20,350.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 2,830,000.00 USD | 2,830,000.00 USD | 85,570.00 USD | 28,990.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 3,030,000.00 USD | 3,030,000.00 USD | 116,600.00 USD | 34,960.00 USD | 44,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 3,250,000.00 USD | 3,250,000.00 USD | 114,260.00 USD | 42,360.00 USD | 65,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 3,480,000.00 USD | 3,480,000.00 USD | 115,340.00 USD | 58,030.00 USD | 61,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 3,580,000.00 USD | 3,580,000.00 USD | 64,080.00 USD | 18,960.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 3,710,000.00 USD | 3,710,000.00 USD | 68,990.00 USD | 22,360.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 3,780,000.00 USD | 3,780,000.00 USD | 40,830.00 USD | 23,750.00 USD | 10,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 3,820,000.00 USD | 3,820,000.00 USD | 14,490.00 USD | 12,760.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 4,720.00 USD | 6,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.27` | 3,950,000.00 USD | 3,950,000.00 USD | 77,420.00 USD | 19,410.00 USD | 37,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 4,070,000.00 USD | 4,070,000.00 USD | 42,500.00 USD | 27,440.00 USD | 52,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 4,140,000.00 USD | 4,140,000.00 USD | 49,170.00 USD | 5,800.00 USD | 14,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 4,160,000.00 USD | 4,160,000.00 USD | 1,880.00 USD | 3,700.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 4,190,000.00 USD | 4,190,000.00 USD | 20,340.00 USD | 8,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 6,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.37` | 4,240,000.00 USD | 4,240,000.00 USD | 27,200.00 USD | 9,040.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 4,300,000.00 USD | 4,300,000.00 USD | 29,120.00 USD | 12,560.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 4,380,000.00 USD | 4,380,000.00 USD | 37,330.00 USD | 19,880.00 USD | 23,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 4,410,000.00 USD | 4,410,000.00 USD | 23,540.00 USD | 5,940.00 USD | 196.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 4,430,000.00 USD | 4,430,000.00 USD | 11,170.00 USD | 4,330.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,240.00 USD | 11,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 4,460,000.00 USD | 4,460,000.00 USD | 1,620.00 USD | 12,000.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.49` | 4,460,000.00 USD | 4,460,000.00 USD | 317.79 USD | 63.95 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.51` | 4,490,000.00 USD | 4,490,000.00 USD | 11,820.00 USD | 7,590.00 USD | 14,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.53` | 4,520,000.00 USD | 4,520,000.00 USD | 19,320.00 USD | 1,680.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.55` | 4,550,000.00 USD | 4,550,000.00 USD | 17,070.00 USD | 5,800.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.57` | 4,580,000.00 USD | 4,580,000.00 USD | 15,700.00 USD | 6,380.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.59` | 4,590,000.00 USD | 4,590,000.00 USD | 6,640.00 USD | 1,010.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.61` | 4,620,000.00 USD | 4,620,000.00 USD | 17,820.00 USD | 3,350.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.63` | 4,670,000.00 USD | 4,670,000.00 USD | 26,060.00 USD | 9,500.00 USD | 11,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.65` | 4,680,000.00 USD | 4,680,000.00 USD | 4,110.00 USD | 4,250.00 USD | 4.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.67` | 4,690,000.00 USD | 4,690,000.00 USD | 156.89 USD | 3,710.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.69` | 4,700,000.00 USD | 4,700,000.00 USD | 3,670.00 USD | 1,810.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.71` | 4,700,000.00 USD | 4,700,000.00 USD | 242.20 USD | 31.80 USD | 1.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.73` | 4,730,000.00 USD | 4,730,000.00 USD | 22,130.00 USD | 9,120.00 USD | 1.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.75` | 4,790,000.00 USD | 4,790,000.00 USD | 32,610.00 USD | 11,330.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.77` | 4,830,000.00 USD | 4,830,000.00 USD | 22,830.00 USD | 9,270.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.79` | 4,850,000.00 USD | 4,850,000.00 USD | 9,880.00 USD | 2,060.00 USD | 11,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.81` | 4,870,000.00 USD | 4,870,000.00 USD | 7,290.00 USD | 3,830.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.83` | 4,900,000.00 USD | 4,900,000.00 USD | 17,160.00 USD | 5,780.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.85` | 4,940,000.00 USD | 4,940,000.00 USD | 25,860.00 USD | 4,270.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 11,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.87` | 4,960,000.00 USD | 4,960,000.00 USD | 7,900.00 USD | 5,270.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.89` | 4,970,000.00 USD | 4,970,000.00 USD | 6,710.00 USD | 2,730.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.91` | 5,000,000.00 USD | 5,000,000.00 USD | 15,190.00 USD | 4,520.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.93` | 5,000,000.00 USD | 5,000,000.00 USD | 212.28 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.95` | 5,010,000.00 USD | 5,010,000.00 USD | 13,070.00 USD | 2,760.00 USD | 3,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.97` | 5,040,000.00 USD | 5,040,000.00 USD | 10,200.00 USD | 7,720.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 14,560,000.00 USD | 14,560,000.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 14,580,000.00 USD | 14,580,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 14,580,000.00 USD | 14,580,000.00 USD | 303.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 11,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.06` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.10` | 14,620,000.00 USD | 14,620,000.00 USD | 18,460.00 USD | 5,730.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.12` | 14,620,000.00 USD | 14,620,000.00 USD | 945.50 USD | 4,010.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.14` | 14,620,000.00 USD | 14,620,000.00 USD | 321.45 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.16` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 57.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.18` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 3,960.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.20` | 14,650,000.00 USD | 14,650,000.00 USD | 972.55 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.22` | 14,680,000.00 USD | 14,680,000.00 USD | 23,980.00 USD | 213.60 USD | 37.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.24` | 14,710,000.00 USD | 14,710,000.00 USD | 18,770.00 USD | 4,640.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.26` | 14,730,000.00 USD | 14,730,000.00 USD | 463.75 USD | 5,860.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 14,740,000.00 USD | 14,740,000.00 USD | 9,830.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.35` | 113.48 USD | 11,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 7,500.00 USD | 19,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 20,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 37,130.00 USD | 58,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 952.84 USD | 59,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 59,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 621.16 USD | 60,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 85,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 16,240.00 USD | 101,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 102,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 34,810.00 USD | 137,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 193,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 193,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.05` | 452.61 USD | 194,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 4,990.00 USD | 199,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 26,300.00 USD | 225,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.65` | 466.20 USD | 226,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 65,630.00 USD | 291,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 371,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 372,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 242.90 USD | 373,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 468,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 246,540.00 USD | 714,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 714,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 715,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 717,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 721,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 1,980.00 USD | 723,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 723,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 2,160,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 316.23 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 571.73 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 418.37 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 767,400.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.65` | 167.27 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.55` | 66,030.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 2,900.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.25` | 413,290.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.35` | 894.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.15` | 236.13 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 13,900,000.00 USD | 0.00 USD | 4,510.00 USD | `-79.90%` | `1,920,000.00` |
| `Live` | `Long` | `2.45` | 13,900,000.00 USD | 0.00 USD | 30,100.00 USD | `-79.05%` | `12,286,800.00` |
| `Live` | `Long` | `2.65` | 13,870,000.00 USD | 0.00 USD | 2,240.00 USD | `-77.34%` | `844,000.00` |
| `Live` | `Long` | `2.75` | 13,870,000.00 USD | 0.00 USD | 220.00 USD | `-76.48%` | `80,000.00` |
| `Live` | `Long` | `3.05` | 13,870,000.00 USD | 0.00 USD | 6,390.00 USD | `-73.91%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 13,860,000.00 USD | 0.00 USD | 7,930.00 USD | `-73.06%` | `2,516,600.00` |
| `Live` | `Long` | `3.25` | 13,850,000.00 USD | 0.00 USD | 650.00 USD | `-72.20%` | `200,000.00` |
| `Live` | `Long` | `3.35` | 13,850,000.00 USD | 0.00 USD | 927.95 USD | `-71.35%` | `277,000.00` |
| `Live` | `Long` | `3.45` | 13,850,000.00 USD | 0.00 USD | 369.15 USD | `-70.49%` | `107,000.00` |
| `Live` | `Long` | `3.55` | 13,850,000.00 USD | 0.00 USD | 302.46 USD | `-69.64%` | `85,200.00` |
| `Live` | `Long` | `3.65` | 13,850,000.00 USD | 0.00 USD | 2,190.00 USD | `-68.78%` | `600,000.00` |
| `Live` | `Long` | `3.75` | 13,850,000.00 USD | 0.00 USD | 379.88 USD | `-67.93%` | `101,300.00` |
| `Live` | `Long` | `3.95` | 13,850,000.00 USD | 0.00 USD | 9,940.00 USD | `-66.22%` | `2,517,100.00` |
| `Live` | `Long` | `4.05` | 13,840,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.36%` | `516,400.00` |
| `Live` | `Long` | `4.15` | 13,840,000.00 USD | 0.00 USD | 2,150.00 USD | `-64.51%` | `517,600.00` |
| `Live` | `Long` | `4.25` | 13,830,000.00 USD | 0.00 USD | 5,090.00 USD | `-63.65%` | `1,198,100.00` |
| `Live` | `Long` | `4.35` | 13,830,000.00 USD | 0.00 USD | 264.05 USD | `-62.80%` | `60,700.00` |
| `Live` | `Long` | `4.45` | 13,830,000.00 USD | 0.00 USD | 381.37 USD | `-61.94%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 13,830,000.00 USD | 0.00 USD | 222,950.00 USD | `-61.09%` | `49,000,000.00` |
| `Live` | `Long` | `4.65` | 13,600,000.00 USD | 0.00 USD | 383.63 USD | `-60.23%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,600,000.00 USD | 0.00 USD | 418.95 USD | `-59.38%` | `88,200.00` |
| `Live` | `Long` | `4.85` | 13,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-58.52%` | `247,100.00` |
| `Live` | `Long` | `4.95` | 13,600,000.00 USD | 0.00 USD | 22,190.00 USD | `-57.67%` | `4,483,600.00` |
| `Live` | `Long` | `5.05` | 13,580,000.00 USD | 0.00 USD | 55,550.00 USD | `-56.81%` | `11,000,000.00` |
| `Live` | `Long` | `5.15` | 13,520,000.00 USD | 0.00 USD | 31,030.00 USD | `-55.95%` | `6,024,400.00` |
| `Live` | `Long` | `5.25` | 13,490,000.00 USD | 0.00 USD | 1,210.00 USD | `-55.10%` | `229,600.00` |
| `Live` | `Long` | `5.35` | 13,490,000.00 USD | 0.00 USD | 633,510.00 USD | `-54.24%` | `118,413,600.00` |
| `Live` | `Long` | `5.45` | 12,860,000.00 USD | 0.00 USD | 499.77 USD | `-53.39%` | `91,700.00` |
| `Live` | `Long` | `5.55` | 12,860,000.00 USD | 0.00 USD | 10,170.00 USD | `-52.53%` | `1,831,900.00` |
| `Live` | `Long` | `5.65` | 12,850,000.00 USD | 0.00 USD | 43,840.00 USD | `-51.68%` | `7,759,700.00` |
| `Live` | `Long` | `5.75` | 12,800,000.00 USD | 0.00 USD | 5,120.00 USD | `-50.82%` | `890,900.00` |
| `Live` | `Long` | `5.85` | 12,800,000.00 USD | 0.00 USD | 32,070.00 USD | `-49.97%` | `5,482,600.00` |
| `Live` | `Long` | `5.95` | 12,770,000.00 USD | 0.00 USD | 909.76 USD | `-49.11%` | `152,900.00` |
| `Live` | `Long` | `6.05` | 12,770,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.26%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,700,000.00 USD | 0.00 USD | 48,450.00 USD | `-47.40%` | `7,878,800.00` |
| `Live` | `Long` | `6.25` | 12,660,000.00 USD | 0.00 USD | 42,490.00 USD | `-46.55%` | `6,799,200.00` |
| `Live` | `Long` | `6.35` | 12,610,000.00 USD | 0.00 USD | 16,590.00 USD | `-45.69%` | `2,612,900.00` |
| `Live` | `Long` | `6.45` | 12,600,000.00 USD | 0.00 USD | 141,680.00 USD | `-44.84%` | `21,966,200.00` |
| `Live` | `Long` | `6.55` | 12,450,000.00 USD | 0.00 USD | 15,940.00 USD | `-43.98%` | `2,433,500.00` |
| `Live` | `Long` | `6.65` | 12,440,000.00 USD | 0.00 USD | 9,260.00 USD | `-43.13%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 12,430,000.00 USD | 0.00 USD | 4,130.00 USD | `-42.27%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,430,000.00 USD | 0.00 USD | 5,820.00 USD | `-41.42%` | `849,200.00` |
| `Live` | `Long` | `6.95` | 12,420,000.00 USD | 0.00 USD | 3,700.00 USD | `-40.56%` | `532,400.00` |
| `Live` | `Long` | `7.05` | 12,420,000.00 USD | 0.00 USD | 2,740.00 USD | `-39.70%` | `388,400.00` |
| `Live` | `Long` | `7.15` | 12,410,000.00 USD | 0.00 USD | 687,520.00 USD | `-38.85%` | `96,156,800.00` |
| `Live` | `Long` | `7.25` | 11,730,000.00 USD | 0.00 USD | 20,150.00 USD | `-37.99%` | `2,778,700.00` |
| `Live` | `Long` | `7.35` | 11,710,000.00 USD | 0.00 USD | 30,960.00 USD | `-37.14%` | `4,211,800.00` |
| `Live` | `Long` | `7.45` | 11,670,000.00 USD | 0.00 USD | 10,880.00 USD | `-36.28%` | `1,460,900.00` |
| `Live` | `Long` | `7.55` | 11,660,000.00 USD | 0.00 USD | 17,030.00 USD | `-35.43%` | `2,255,200.00` |
| `Live` | `Long` | `7.65` | 11,650,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.57%` | `150,000.00` |
| `Live` | `Long` | `7.75` | 11,650,000.00 USD | 0.00 USD | 2,890.00 USD | `-33.72%` | `373,100.00` |
| `Live` | `Long` | `7.85` | 11,640,000.00 USD | 0.00 USD | 726.91 USD | `-32.86%` | `92,600.00` |
| `Live` | `Long` | `7.95` | 11,640,000.00 USD | 0.00 USD | 41,640.00 USD | `-32.01%` | `5,238,200.00` |
| `Live` | `Long` | `8.05` | 11,600,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-31.15%` | `172,206,300.00` |
| `Live` | `Long` | `8.15` | 10,210,000.00 USD | 0.00 USD | 16,320.00 USD | `-30.30%` | `2,002,500.00` |
| `Live` | `Long` | `8.25` | 10,200,000.00 USD | 0.00 USD | 34,670.00 USD | `-29.44%` | `4,202,500.00` |
| `Live` | `Long` | `8.35` | 10,160,000.00 USD | 0.00 USD | 7,770.00 USD | `-28.59%` | `930,800.00` |
| `Live` | `Long` | `8.45` | 10,150,000.00 USD | 0.00 USD | 10,670.00 USD | `-27.73%` | `1,263,100.00` |
| `Live` | `Long` | `8.55` | 10,140,000.00 USD | 0.00 USD | 43,900.00 USD | `-26.88%` | `5,134,100.00` |
| `Live` | `Long` | `8.65` | 10,100,000.00 USD | 0.00 USD | 11,540.00 USD | `-26.02%` | `1,333,800.00` |
| `Live` | `Long` | `8.75` | 10,090,000.00 USD | 0.00 USD | 304,290.00 USD | `-25.17%` | `34,776,300.00` |
| `Live` | `Long` | `8.85` | 9,780,000.00 USD | 0.00 USD | 35,020.00 USD | `-24.31%` | `3,957,300.00` |
| `Live` | `Long` | `8.95` | 9,750,000.00 USD | 0.00 USD | 486,640.00 USD | `-23.46%` | `54,373,700.00` |
| `Live` | `Long` | `9.05` | 9,260,000.00 USD | 0.00 USD | 42,820.00 USD | `-22.60%` | `4,731,900.00` |
| `Live` | `Long` | `9.15` | 9,220,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-21.74%` | `410,561,400.00` |
| `Live` | `Long` | `9.25` | 5,460,000.00 USD | 0.00 USD | 25,310.00 USD | `-20.89%` | `2,736,500.00` |
| `Live` | `Long` | `9.35` | 5,440,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-20.03%` | `232,320,500.00` |
| `Live` | `Long` | `9.45` | 3,270,000.00 USD | 0.00 USD | 19,500.00 USD | `-19.18%` | `2,064,000.00` |
| `Live` | `Long` | `9.55` | 3,250,000.00 USD | 0.00 USD | 14,380.00 USD | `-18.32%` | `1,505,500.00` |
| `Live` | `Long` | `9.65` | 3,230,000.00 USD | 0.00 USD | 8,830.00 USD | `-17.47%` | `914,600.00` |
| `Live` | `Long` | `9.75` | 3,220,000.00 USD | 0.00 USD | 103,770.00 USD | `-16.61%` | `10,642,900.00` |
| `Live` | `Long` | `9.85` | 3,120,000.00 USD | 0.00 USD | 17,700.00 USD | `-15.76%` | `1,796,600.00` |
| `Live` | `Long` | `9.95` | 3,100,000.00 USD | 0.00 USD | 782,600.00 USD | `-14.90%` | `78,653,300.00` |
| `Live` | `Long` | `10.05` | 2,320,000.00 USD | 0.00 USD | 645,720.00 USD | `-14.05%` | `64,250,500.00` |
| `Live` | `Long` | `10.15` | 1,670,000.00 USD | 0.00 USD | 44,810.00 USD | `-13.19%` | `4,415,000.00` |
| `Live` | `Long` | `10.25` | 1,630,000.00 USD | 0.00 USD | 278,400.00 USD | `-12.34%` | `27,161,100.00` |
| `Live` | `Long` | `10.35` | 1,350,000.00 USD | 0.00 USD | 9,660.00 USD | `-11.48%` | `933,500.00` |
| `Live` | `Long` | `10.45` | 1,340,000.00 USD | 0.00 USD | 175,650.00 USD | `-10.63%` | `16,808,400.00` |
| `Live` | `Long` | `10.55` | 1,160,000.00 USD | 0.00 USD | 40,130.00 USD | `-9.77%` | `3,803,600.00` |
| `Live` | `Long` | `10.65` | 1,120,000.00 USD | 0.00 USD | 44,080.00 USD | `-8.92%` | `4,138,800.00` |
| `Live` | `Long` | `10.75` | 1,080,000.00 USD | 0.00 USD | 214,040.00 USD | `-8.06%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 866,620.00 USD | 0.00 USD | 85,390.00 USD | `-7.21%` | `7,870,500.00` |
| `Live` | `Long` | `10.95` | 781,230.00 USD | 0.00 USD | 558,110.00 USD | `-6.35%` | `50,969,000.00` |
| `Live` | `Long` | `11.05` | 223,120.00 USD | 0.00 USD | 147,130.00 USD | `-5.49%` | `13,314,900.00` |
| `Live` | `Long` | `11.15` | 75,990.00 USD | 0.00 USD | 25,090.00 USD | `-4.64%` | `2,250,600.00` |
| `Live` | `Long` | `11.25` | 50,890.00 USD | 0.00 USD | 41,990.00 USD | `-3.78%` | `3,732,700.00` |
| `Live` | `Long` | `11.35` | 8,900.00 USD | 0.00 USD | 8,900.00 USD | `-2.93%` | `784,000.00` |
| `Live` | `Short` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | `+3.91%` | `114,600.00` |
| `Live` | `Short` | `12.25` | 6,120.00 USD | 4,720.00 USD | 0.00 USD | `+4.77%` | `385,600.00` |
| `Live` | `Short` | `12.35` | 6,850.00 USD | 736.06 USD | 0.00 USD | `+5.62%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 11,090.00 USD | 4,240.00 USD | 0.00 USD | `+6.48%` | `340,500.00` |
| `Live` | `Short` | `12.85` | 11,230.00 USD | 138.78 USD | 0.00 USD | `+9.90%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 11,340.00 USD | 113.53 USD | 0.00 USD | `+11.61%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 11,620.00 USD | 274.84 USD | 0.00 USD | `+12.47%` | `20,900.00` |
| `Live` | `Short` | `13.35` | 11,730.00 USD | 113.48 USD | 0.00 USD | `+14.18%` | `8,500.00` |
| `Live` | `Short` | `13.45` | 19,230.00 USD | 7,500.00 USD | 0.00 USD | `+15.03%` | `557,600.00` |
| `Live` | `Short` | `13.55` | 20,990.00 USD | 1,760.00 USD | 0.00 USD | `+15.89%` | `130,100.00` |
| `Live` | `Short` | `13.95` | 58,130.00 USD | 37,130.00 USD | 0.00 USD | `+19.31%` | `2,661,900.00` |
| `Live` | `Short` | `14.35` | 59,080.00 USD | 952.84 USD | 0.00 USD | `+22.73%` | `66,400.00` |
| `Live` | `Short` | `14.45` | 59,620.00 USD | 541.88 USD | 0.00 USD | `+23.58%` | `37,500.00` |
| `Live` | `Short` | `14.65` | 60,240.00 USD | 621.16 USD | 0.00 USD | `+25.29%` | `42,400.00` |
| `Live` | `Short` | `14.95` | 85,580.00 USD | 25,330.00 USD | 0.00 USD | `+27.86%` | `1,694,600.00` |
| `Live` | `Short` | `15.35` | 101,820.00 USD | 16,240.00 USD | 0.00 USD | `+31.28%` | `1,058,000.00` |
| `Live` | `Short` | `15.55` | 102,660.00 USD | 838.14 USD | 0.00 USD | `+32.99%` | `53,900.00` |
| `Live` | `Short` | `15.75` | 137,460.00 USD | 34,810.00 USD | 0.00 USD | `+34.70%` | `2,210,000.00` |
| `Live` | `Short` | `15.85` | 193,810.00 USD | 56,350.00 USD | 0.00 USD | `+35.56%` | `3,554,900.00` |
| `Live` | `Short` | `15.95` | 193,950.00 USD | 138.76 USD | 0.00 USD | `+36.41%` | `8,700.00` |
| `Live` | `Short` | `16.05` | 194,400.00 USD | 452.61 USD | 0.00 USD | `+37.27%` | `28,200.00` |
| `Live` | `Short` | `16.15` | 199,390.00 USD | 4,990.00 USD | 0.00 USD | `+38.12%` | `309,000.00` |
| `Live` | `Short` | `16.35` | 225,690.00 USD | 26,300.00 USD | 0.00 USD | `+39.83%` | `1,608,300.00` |
| `Live` | `Short` | `16.65` | 226,150.00 USD | 466.20 USD | 0.00 USD | `+42.40%` | `28,000.00` |
| `Live` | `Short` | `16.85` | 291,780.00 USD | 65,630.00 USD | 0.00 USD | `+44.11%` | `3,895,000.00` |
| `Live` | `Short` | `16.95` | 371,560.00 USD | 79,770.00 USD | 0.00 USD | `+44.96%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 372,920.00 USD | 1,370.00 USD | 0.00 USD | `+46.68%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 373,170.00 USD | 242.90 USD | 0.00 USD | `+48.39%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 468,180.00 USD | 95,020.00 USD | 0.00 USD | `+49.24%` | `5,445,000.00` |
| `Live` | `Short` | `17.65` | 714,720.00 USD | 246,540.00 USD | 0.00 USD | `+50.95%` | `13,968,000.00` |
| `Live` | `Short` | `17.85` | 714,970.00 USD | 249.90 USD | 0.00 USD | `+52.66%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 715,590.00 USD | 621.07 USD | 0.00 USD | `+53.52%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 717,560.00 USD | 1,970.00 USD | 0.00 USD | `+54.37%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 721,450.00 USD | 3,890.00 USD | 0.00 USD | `+57.79%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 723,430.00 USD | 1,980.00 USD | 0.00 USD | `+58.65%` | `106,900.00` |
| `Live` | `Short` | `18.65` | 723,620.00 USD | 186.50 USD | 0.00 USD | `+59.50%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 2,880,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+60.36%` | `115,024,600.00` |
| `Live` | `Short` | `18.85` | 2,880,000.00 USD | 456.17 USD | 0.00 USD | `+61.21%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,900,000.00 USD | 16,250.00 USD | 0.00 USD | `+62.07%` | `857,700.00` |
| `Live` | `Short` | `19.05` | 2,900,000.00 USD | 316.23 USD | 0.00 USD | `+62.92%` | `16,600.00` |
| `Live` | `Short` | `19.25` | 2,900,000.00 USD | 571.73 USD | 0.00 USD | `+64.64%` | `29,700.00` |
| `Live` | `Short` | `19.55` | 2,900,000.00 USD | 418.37 USD | 0.00 USD | `+67.20%` | `21,400.00` |
| `Live` | `Short` | `19.65` | 2,940,000.00 USD | 38,790.00 USD | 0.00 USD | `+68.06%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,940,000.00 USD | 291.27 USD | 0.00 USD | `+70.62%` | `14,600.00` |
| `Live` | `Short` | `20.35` | 3,700,000.00 USD | 767,400.00 USD | 0.00 USD | `+74.04%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,710,000.00 USD | 7,250.00 USD | 0.00 USD | `+75.75%` | `353,000.00` |
| `Live` | `Short` | `20.65` | 3,710,000.00 USD | 167.27 USD | 0.00 USD | `+76.61%` | `8,100.00` |
| `Live` | `Short` | `21.55` | 3,780,000.00 USD | 66,030.00 USD | 0.00 USD | `+84.31%` | `3,064,200.00` |
| `Live` | `Short` | `21.75` | 3,780,000.00 USD | 2,900.00 USD | 0.00 USD | `+86.02%` | `133,300.00` |
| `Live` | `Short` | `22.25` | 4,190,000.00 USD | 413,290.00 USD | 0.00 USD | `+90.29%` | `18,575,000.00` |
| `Live` | `Short` | `22.35` | 4,200,000.00 USD | 894.00 USD | 0.00 USD | `+91.15%` | `40,000.00` |
| `Live` | `Short` | `23.15` | 4,200,000.00 USD | 236.13 USD | 0.00 USD | `+97.99%` | `10,200.00` |
| `Live` | `Short` | `23.35` | 4,200,000.00 USD | 238.17 USD | 0.00 USD | `+99.70%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 837,910.00 USD | 0.00 USD | 431.68 USD | `-69.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 837,470.00 USD | 0.00 USD | 290.29 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 837,180.00 USD | 0.00 USD | 120.22 USD | `-55.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 837,060.00 USD | 0.00 USD | 107.09 USD | `-48.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 836,960.00 USD | 0.00 USD | 3,760.00 USD | `-43.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 833,190.00 USD | 0.00 USD | 133.00 USD | `-43.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 833,060.00 USD | 0.00 USD | 3,770.00 USD | `-39.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 829,290.00 USD | 0.00 USD | 2,070.00 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 827,220.00 USD | 0.00 USD | 3,740.00 USD | `-36.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 823,480.00 USD | 0.00 USD | 1,050.00 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 822,420.00 USD | 0.00 USD | 146.80 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 822,280.00 USD | 0.00 USD | 5,000.00 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 817,280.00 USD | 0.00 USD | 393.64 USD | `-30.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 816,880.00 USD | 0.00 USD | 10,660.00 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 806,220.00 USD | 0.00 USD | 1,360.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 804,860.00 USD | 0.00 USD | 30,250.00 USD | `-26.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 774,610.00 USD | 0.00 USD | 186.84 USD | `-26.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 774,430.00 USD | 0.00 USD | 742.88 USD | `-25.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 773,680.00 USD | 0.00 USD | 196.47 USD | `-24.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 773,490.00 USD | 0.00 USD | 1,520.00 USD | `-23.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 771,970.00 USD | 0.00 USD | 2,240.00 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 769,730.00 USD | 0.00 USD | 194.90 USD | `-21.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 769,530.00 USD | 0.00 USD | 4,940.00 USD | `-20.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 764,590.00 USD | 0.00 USD | 9,870.00 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 754,720.00 USD | 0.00 USD | 3,550.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 751,170.00 USD | 0.00 USD | 25,950.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 725,220.00 USD | 0.00 USD | 19,100.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 706,120.00 USD | 0.00 USD | 299,650.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 406,470.00 USD | 0.00 USD | 2,590.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 403,880.00 USD | 0.00 USD | 1,050.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 402,830.00 USD | 0.00 USD | 2,820.00 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 400,010.00 USD | 0.00 USD | 6,330.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 393,680.00 USD | 0.00 USD | 19,650.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 374,030.00 USD | 0.00 USD | 5,160.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 368,860.00 USD | 0.00 USD | 4,590.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 364,270.00 USD | 0.00 USD | 5,470.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 358,790.00 USD | 0.00 USD | 3,780.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 355,010.00 USD | 0.00 USD | 3,270.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 351,740.00 USD | 0.00 USD | 18,860.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 332,880.00 USD | 0.00 USD | 27,100.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 305,770.00 USD | 0.00 USD | 69,570.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 236,210.00 USD | 0.00 USD | 13,780.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 222,430.00 USD | 0.00 USD | 48,420.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 174,010.00 USD | 0.00 USD | 54,150.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 119,870.00 USD | 0.00 USD | 119,870.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 6,620.00 USD | 2,160.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 6,780.00 USD | 156.55 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 63,050.00 USD | 56,270.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 65,010.00 USD | 1,960.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 75,320.00 USD | 10,320.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 76,660.00 USD | 1,340.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 77,160.00 USD | 500.49 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 88,270.00 USD | 11,110.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 144,800.00 USD | 56,530.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 186,280.00 USD | 41,470.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 207,010.00 USD | 20,730.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 207,470.00 USD | 461.02 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 213,970.00 USD | 6,500.00 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 215,020.00 USD | 1,050.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 218,860.00 USD | 3,840.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 223,850.00 USD | 4,990.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 238,250.00 USD | 14,400.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 240,880.00 USD | 2,630.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 242,900.00 USD | 2,020.00 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 244,960.00 USD | 2,060.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 245,090.00 USD | 120.50 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 245,350.00 USD | 266.44 USD | 0.00 USD | `+19.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 262,460.00 USD | 17,110.00 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 263,260.00 USD | 798.06 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 270,250.00 USD | 6,990.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 270,470.00 USD | 218.25 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 273,080.00 USD | 2,610.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 286,000.00 USD | 12,920.00 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 286,950.00 USD | 950.82 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 298,460.00 USD | 11,500.00 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 302,640.00 USD | 4,180.00 USD | 0.00 USD | `+29.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 535,680.00 USD | 233,040.00 USD | 0.00 USD | `+30.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 540,070.00 USD | 4,380.00 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 540,960.00 USD | 893.01 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 541,350.00 USD | 388.75 USD | 0.00 USD | `+32.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 568,400.00 USD | 27,050.00 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 570,730.00 USD | 2,330.00 USD | 0.00 USD | `+34.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 576,070.00 USD | 5,340.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 581,390.00 USD | 5,320.00 USD | 0.00 USD | `+36.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 590,560.00 USD | 9,170.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 597,360.00 USD | 6,800.00 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 616,120.00 USD | 18,760.00 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 622,660.00 USD | 6,540.00 USD | 0.00 USD | `+39.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 629,240.00 USD | 6,580.00 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 639,170.00 USD | 9,930.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 652,490.00 USD | 13,320.00 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 666,730.00 USD | 14,240.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 751,090.00 USD | 84,360.00 USD | 0.00 USD | `+44.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 752,780.00 USD | 1,700.00 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 762,290.00 USD | 9,510.00 USD | 0.00 USD | `+45.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 764,000.00 USD | 1,710.00 USD | 0.00 USD | `+46.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 766,250.00 USD | 2,250.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 864,590.00 USD | 98,330.00 USD | 0.00 USD | `+48.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 886,260.00 USD | 21,670.00 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 892,690.00 USD | 6,430.00 USD | 0.00 USD | `+50.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 897,100.00 USD | 4,410.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 901,540.00 USD | 4,440.00 USD | 0.00 USD | `+51.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 906,000.00 USD | 4,460.00 USD | 0.00 USD | `+52.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 906,450.00 USD | 448.75 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 942,030.00 USD | 35,590.00 USD | 0.00 USD | `+54.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 942,490.00 USD | 453.75 USD | 0.00 USD | `+55.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 943,320.00 USD | 830.38 USD | 0.00 USD | `+56.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 943,780.00 USD | 458.75 USD | 0.00 USD | `+56.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 944,240.00 USD | 461.25 USD | 0.00 USD | `+57.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 948,780.00 USD | 4,540.00 USD | 0.00 USD | `+58.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 949,250.00 USD | 466.25 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 949,720.00 USD | 468.75 USD | 0.00 USD | `+60.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 950,190.00 USD | 471.25 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 950,660.00 USD | 473.75 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,020,000.00 USD | 67,000.00 USD | 0.00 USD | `+62.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,020,000.00 USD | 574.50 USD | 0.00 USD | `+63.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,020,000.00 USD | 577.50 USD | 0.00 USD | `+64.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,020,000.00 USD | 2,710.00 USD | 0.00 USD | `+65.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,020,000.00 USD | 972.50 USD | 0.00 USD | `+66.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,030,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,030,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,030,000.00 USD | 1,690.00 USD | 0.00 USD | `+68.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,030,000.00 USD | 992.50 USD | 0.00 USD | `+69.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,040,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,650,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,650,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,660,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,660,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,660,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,660,000.00 USD | 1,860.00 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,660,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,660,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,670,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,670,000.00 USD | 1,060.00 USD | 0.00 USD | `+80.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,670,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,720,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+82.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,720,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,720,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,730,000.00 USD | 3,280.00 USD | 0.00 USD | `+86.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,730,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,730,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,730,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,730,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,730,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,730,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,730,000.00 USD | 1,130.00 USD | 0.00 USD | `+92.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,730,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,740,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,740,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,740,000.00 USD | 1,150.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,870,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,870,000.00 USD | 1,160.00 USD | 0.00 USD | `+97.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,870,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,870,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.70%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.24` | 20,290,000.00 USD | 0.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD |
| `7D` | `10.26` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD |
| `1D` | `10.27` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 25,950.00 USD | 5,810.00 USD | 4,130.00 USD |
| `7D` | `10.28` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD |
| `1D` | `10.29` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 14,970.00 USD | 6,380.00 USD | 13,580.00 USD |
| `7D` | `10.30` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD |
| `1D` | `10.31` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 20,160.00 USD | 4,360.00 USD | 10,280.00 USD |
| `7D` | `10.32` | 19,540,000.00 USD | 0.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `1D` | `10.33` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 25,720.00 USD | 9,500.00 USD | 11,720.00 USD |
| `7D` | `10.34` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD |
| `1D` | `10.35` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 3,750.00 USD | 4,250.00 USD | 4.92 USD |
| `7D` | `10.36` | 19,270,000.00 USD | 0.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD |
| `1D` | `10.37` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 156.89 USD | 3,710.00 USD | 5,960.00 USD |
| `7D` | `10.38` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD |
| `1D` | `10.39` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 2,580.00 USD | 1,810.00 USD | 7,150.00 USD |
| `7D` | `10.40` | 19,180,000.00 USD | 0.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD |
| `1D` | `10.41` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 21,850.00 USD | 9,160.00 USD | 3.03 USD |
| `7D` | `10.42` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD |
| `1D` | `10.43` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 32,610.00 USD | 11,330.00 USD | 12,300.00 USD |
| `7D` | `10.44` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD |
| `1D` | `10.45` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 22,830.00 USD | 9,270.00 USD | 10,510.00 USD |
| `7D` | `10.46` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD |
| `1D` | `10.47` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 9,880.00 USD | 2,060.00 USD | 11,260.00 USD |
| `7D` | `10.48` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `10.49` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 24,450.00 USD | 9,610.00 USD | 17,410.00 USD |
| `7D` | `10.50` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD |
| `1D` | `10.51` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 25,860.00 USD | 4,270.00 USD | 5,430.00 USD |
| `7D` | `10.52` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD |
| `1D` | `10.53` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 8,070.00 USD | 5,270.00 USD | 4,610.00 USD |
| `7D` | `10.54` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD |
| `1D` | `10.55` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 7,160.00 USD | 2,730.00 USD | 1,820.00 USD |
| `7D` | `10.56` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD |
| `1D` | `10.57` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 16,060.00 USD | 4,520.00 USD | 8,190.00 USD |
| `7D` | `10.58` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD |
| `1D` | `10.59` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 14,080.00 USD | 2,760.00 USD | 3,120.00 USD |
| `7D` | `10.60` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD |
| `1D` | `10.61` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 12,640.00 USD | 7,830.00 USD | 5,610.00 USD |
| `7D` | `10.62` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD |
| `1D` | `10.63` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 22,390.00 USD | 5,060.00 USD | 12,730.00 USD |
| `7D` | `10.64` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.65` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 18,690.00 USD | 3,770.00 USD | 14,940.00 USD |
| `7D` | `10.66` | 18,200,000.00 USD | 0.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.67` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 442.43 USD | 1,480.00 USD | 10.09 USD |
| `7D` | `10.68` | 18,180,000.00 USD | 0.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.69` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 11,810.00 USD | 3,650.00 USD | 1,550.00 USD |
| `7D` | `10.70` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.71` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 3,410.00 USD | 1,570.00 USD | 3,730.00 USD |
| `7D` | `10.72` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD |
| `1D` | `10.73` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 6,610.00 USD | 3,000.00 USD | 6,980.00 USD |
| `7D` | `10.74` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD |
| `1D` | `10.75` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 20,270.00 USD | 4,650.00 USD | 3,870.00 USD |
| `7D` | `10.76` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD |
| `1D` | `10.77` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 5,310.00 USD | 4,090.00 USD | 2,690.00 USD |
| `7D` | `10.78` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD |
| `1D` | `10.79` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 2,790.00 USD | 2,540.00 USD | 30.92 USD |
| `7D` | `10.80` | 18,010,000.00 USD | 0.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD |
| `1D` | `10.81` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 1,970.00 USD | 0.00 USD | 22.32 USD |
| `7D` | `10.82` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD |
| `1D` | `10.83` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 2,830.00 USD | 160.15 USD | 76.98 USD |
| `7D` | `10.84` | 17,690,000.00 USD | 0.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.85` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 1,690.00 USD | 4,450.00 USD | 3,740.00 USD |
| `7D` | `10.86` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD |
| `1D` | `10.87` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 576.29 USD | 2,760.00 USD | 209.94 USD |
| `7D` | `10.88` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD |
| `1D` | `10.89` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 1,860.00 USD | 11,320.00 USD | 36,650.00 USD |
| `7D` | `10.90` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.91` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 685.29 USD | 10,840.00 USD | 25,750.00 USD |
| `7D` | `10.92` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.93` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 96,860.00 USD | 28,100.00 USD | 41,530.00 USD |
| `7D` | `10.94` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.95` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 45,000.00 USD | 14,550.00 USD | 17,250.00 USD |
| `7D` | `10.96` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.97` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 80,360.00 USD | 15,940.00 USD | 33,990.00 USD |
| `7D` | `10.98` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD |
| `1D` | `10.99` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 48,940.00 USD | 15,200.00 USD | 14,840.00 USD |
| `7D` | `11.00` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `1D` | `11.01` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 53,360.00 USD | 23,840.00 USD | 28,300.00 USD |
| `7D` | `11.02` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD |
| `1D` | `11.03` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 68,450.00 USD | 12,950.00 USD | 21,730.00 USD |
| `7D` | `11.04` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `1D` | `11.05` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 14,150.00 USD | 402.52 USD | 8,210.00 USD |
| `7D` | `11.06` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.07` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 25,280.00 USD | 21,300.00 USD | 30,860.00 USD |
| `7D` | `11.08` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD |
| `1D` | `11.09` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 9,540.00 USD | 9,350.00 USD | 10,960.00 USD |
| `7D` | `11.10` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD |
| `1D` | `11.11` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 52,180.00 USD | 45,500.00 USD | 79,840.00 USD |
| `7D` | `11.12` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.13` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 89,330.00 USD | 55,180.00 USD | 89,990.00 USD |
| `7D` | `11.14` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD |
| `1D` | `11.15` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 188,500.00 USD | 67,260.00 USD | 112,200.00 USD |
| `7D` | `11.16` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.17` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 153,150.00 USD | 52,240.00 USD | 66,510.00 USD |
| `7D` | `11.18` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD |
| `1D` | `11.19` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 257,350.00 USD | 63,490.00 USD | 91,270.00 USD |
| `7D` | `11.20` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD |
| `1D` | `11.21` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 113,460.00 USD | 22,410.00 USD | 77,010.00 USD |
| `7D` | `11.22` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD |
| `1D` | `11.23` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 131,420.00 USD | 43,780.00 USD | 58,500.00 USD |
| `7D` | `11.24` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD |
| `1D` | `11.25` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 205,010.00 USD | 55,560.00 USD | 73,610.00 USD |
| `7D` | `11.26` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD |
| `1D` | `11.27` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 72,930.00 USD | 38,810.00 USD | 31,850.00 USD |
| `7D` | `11.28` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD |
| `1D` | `11.29` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 77,300.00 USD | 26,000.00 USD | 37,070.00 USD |
| `7D` | `11.30` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD |
| `1D` | `11.31` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 67,970.00 USD | 15,830.00 USD | 37,070.00 USD |
| `7D` | `11.32` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD |
| `1D` | `11.33` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 140,030.00 USD | 27,960.00 USD | 20,000.00 USD |
| `7D` | `11.34` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD |
| `1D` | `11.35` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 146,250.00 USD | 85,790.00 USD | 54,460.00 USD |
| `7D` | `11.36` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD |
| `1D` | `11.37` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 160,130.00 USD | 58,390.00 USD | 93,700.00 USD |
| `7D` | `11.38` | 962,530.00 USD | 0.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.39` | 809,070.00 USD | 0.00 USD | 809,070.00 USD | 54,830.00 USD | 37,490.00 USD | 50,880.00 USD |
| `7D` | `11.40` | 871,150.00 USD | 0.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.41` | 665,870.00 USD | 0.00 USD | 665,870.00 USD | 114,970.00 USD | 34,560.00 USD | 83,700.00 USD |
| `7D` | `11.42` | 677,690.00 USD | 0.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD |
| `1D` | `11.43` | 432,640.00 USD | 0.00 USD | 432,640.00 USD | 50,600.00 USD | 26,360.00 USD | 88,270.00 USD |
| `7D` | `11.44` | 536,960.00 USD | 0.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD |
| `1D` | `11.45` | 267,410.00 USD | 0.00 USD | 267,410.00 USD | 0.00 USD | 83.92 USD | 68,310.00 USD |
| `7D` | `11.46` | 264,830.00 USD | 0.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD |
| `1D` | `11.47` | 199,020.00 USD | 0.00 USD | 199,020.00 USD | 0.00 USD | 30.00 USD | 28,440.00 USD |
| `7D` | `11.48` | 128,570.00 USD | 0.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `11.49` | 170,550.00 USD | 0.00 USD | 170,550.00 USD | 10,420.00 USD | 18,420.00 USD | 15,460.00 USD |
| `7D` | `11.50` | 88,130.00 USD | 0.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD |
| `1D` | `11.51` | 126,250.00 USD | 0.00 USD | 126,250.00 USD | 83,540.00 USD | 0.00 USD | 42,710.00 USD |
| `1D` | `11.52` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `7D` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `1D` | `11.53` | 37,210.00 USD | 37,210.00 USD | 0.00 USD | 13,090.00 USD | 0.00 USD | 24,130.00 USD |
| `7D` | `11.54` | 94,830.00 USD | 94,830.00 USD | 0.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD |
| `1D` | `11.55` | 83,270.00 USD | 83,270.00 USD | 0.00 USD | 21,770.00 USD | 0.00 USD | 24,280.00 USD |
| `7D` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD |
| `1D` | `11.57` | 233,550.00 USD | 233,550.00 USD | 0.00 USD | 77,390.00 USD | 0.00 USD | 72,890.00 USD |
| `7D` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.59` | 273,530.00 USD | 273,530.00 USD | 0.00 USD | 11,470.00 USD | 75.80 USD | 28,440.00 USD |
| `7D` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.61` | 340,430.00 USD | 340,430.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.64` | 222,010.00 USD | 222,010.00 USD | 0.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD |
| `7D` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD |
| `1D` | `11.69` | 410,070.00 USD | 410,070.00 USD | 0.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD |
| `1D` | `11.71` | 541,040.00 USD | 541,040.00 USD | 0.00 USD | 118,160.00 USD | 12,820.00 USD | 0.00 USD |
| `7D` | `11.72` | 484,570.00 USD | 484,570.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 587,780.00 USD | 587,780.00 USD | 0.00 USD | 46,440.00 USD | 300.68 USD | 0.00 USD |
| `1D` | `11.75` | 602,310.00 USD | 602,310.00 USD | 0.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD |
| `7D` | `11.76` | 532,760.00 USD | 532,760.00 USD | 0.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.77` | 619,270.00 USD | 619,270.00 USD | 0.00 USD | 16,180.00 USD | 777.33 USD | 0.00 USD |
| `1D` | `11.79` | 620,030.00 USD | 620,030.00 USD | 0.00 USD | 0.00 USD | 755.20 USD | 0.00 USD |
| `7D` | `11.80` | 672,880.00 USD | 672,880.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.81` | 633,970.00 USD | 633,970.00 USD | 0.00 USD | 0.00 USD | 13,940.00 USD | 0.00 USD |
| `7D` | `11.82` | 873,430.00 USD | 873,430.00 USD | 0.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.83` | 645,470.00 USD | 645,470.00 USD | 0.00 USD | 0.00 USD | 11,510.00 USD | 0.00 USD |
| `7D` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD |
| `1D` | `11.85` | 789,050.00 USD | 789,050.00 USD | 0.00 USD | 55,600.00 USD | 22,590.00 USD | 65,400.00 USD |
| `7D` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD |
| `1D` | `11.87` | 872,890.00 USD | 872,890.00 USD | 0.00 USD | 19,640.00 USD | 26,360.00 USD | 37,840.00 USD |
| `7D` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD |
| `1D` | `11.89` | 942,980.00 USD | 942,980.00 USD | 0.00 USD | 44,160.00 USD | 11,410.00 USD | 14,520.00 USD |
| `7D` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.91` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 62,930.00 USD | 18,340.00 USD | 18,550.00 USD |
| `7D` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD |
| `1D` | `11.93` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 78,080.00 USD | 27,850.00 USD | 28,460.00 USD |
| `7D` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD |
| `1D` | `11.95` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 1,220.00 USD | 14,280.00 USD | 22,560.00 USD |
| `7D` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD |
| `1D` | `11.97` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 44,480.00 USD | 27,610.00 USD | 60,810.00 USD |
| `7D` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD |
| `1D` | `11.99` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 38,440.00 USD | 7,350.00 USD | 42,890.00 USD |
| `7D` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD |
| `1D` | `12.01` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 73,670.00 USD | 467.98 USD | 26,130.00 USD |
| `7D` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD |
| `1D` | `12.03` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 155,160.00 USD | 72,030.00 USD | 49,450.00 USD |
| `7D` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD |
| `1D` | `12.05` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 234,920.00 USD | 68,310.00 USD | 113,670.00 USD |
| `7D` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD |
| `1D` | `12.07` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 169,050.00 USD | 63,630.00 USD | 125,670.00 USD |
| `7D` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD |
| `1D` | `12.09` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 17,390.00 USD | 20,350.00 USD | 17,590.00 USD |
| `7D` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.11` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 85,570.00 USD | 28,990.00 USD | 71,710.00 USD |
| `7D` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD |
| `1D` | `12.13` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 116,600.00 USD | 34,960.00 USD | 44,190.00 USD |
| `7D` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD |
| `1D` | `12.15` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 114,260.00 USD | 42,360.00 USD | 65,390.00 USD |
| `7D` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD |
| `1D` | `12.17` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 115,340.00 USD | 58,030.00 USD | 61,070.00 USD |
| `7D` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD |
| `1D` | `12.19` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 64,080.00 USD | 18,960.00 USD | 9,890.00 USD |
| `7D` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD |
| `1D` | `12.21` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 68,990.00 USD | 22,360.00 USD | 39,130.00 USD |
| `7D` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD |
| `1D` | `12.23` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 40,830.00 USD | 23,750.00 USD | 10,120.00 USD |
| `7D` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD |
| `1D` | `12.25` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 14,490.00 USD | 12,760.00 USD | 7,630.00 USD |
| `7D` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD |
| `1D` | `12.27` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 77,420.00 USD | 19,410.00 USD | 37,520.00 USD |
| `7D` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD |
| `1D` | `12.29` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 42,500.00 USD | 27,440.00 USD | 52,410.00 USD |
| `7D` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD |
| `1D` | `12.31` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 49,170.00 USD | 5,800.00 USD | 14,650.00 USD |
| `7D` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.33` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 1,880.00 USD | 3,700.00 USD | 7,610.00 USD |
| `7D` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD |
| `1D` | `12.35` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 20,340.00 USD | 8,540.00 USD | 9,410.00 USD |
| `7D` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD |
| `1D` | `12.37` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 27,200.00 USD | 9,040.00 USD | 5,470.00 USD |
| `7D` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD |
| `1D` | `12.39` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 29,120.00 USD | 12,560.00 USD | 21,670.00 USD |
| `7D` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD |
| `1D` | `12.41` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 37,330.00 USD | 19,880.00 USD | 23,480.00 USD |
| `7D` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD |
| `1D` | `12.43` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 23,540.00 USD | 5,940.00 USD | 196.48 USD |
| `7D` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD |
| `1D` | `12.45` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 11,170.00 USD | 4,330.00 USD | 6,410.00 USD |
| `7D` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD |
| `1D` | `12.47` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 1,620.00 USD | 12,000.00 USD | 12,410.00 USD |
| `7D` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD |
| `1D` | `12.49` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 317.79 USD | 63.95 USD | 1,500.00 USD |
| `7D` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD |
| `1D` | `12.51` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 11,820.00 USD | 7,590.00 USD | 14,750.00 USD |
| `7D` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.53` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 19,320.00 USD | 1,680.00 USD | 4,250.00 USD |
| `7D` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD |
| `1D` | `12.55` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 17,070.00 USD | 5,800.00 USD | 4,080.00 USD |
| `7D` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD |
| `1D` | `12.57` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 15,700.00 USD | 6,380.00 USD | 13,680.00 USD |
| `7D` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD |
| `1D` | `12.59` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 6,640.00 USD | 1,010.00 USD | 3,280.00 USD |
| `7D` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.61` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 17,820.00 USD | 3,350.00 USD | 7,170.00 USD |
| `7D` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.63` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 26,060.00 USD | 9,500.00 USD | 11,720.00 USD |
| `7D` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.65` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 4,110.00 USD | 4,250.00 USD | 4.92 USD |
| `7D` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.67` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 156.89 USD | 3,710.00 USD | 5,960.00 USD |
| `7D` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD |
| `1D` | `12.69` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 3,670.00 USD | 1,810.00 USD | 7,260.00 USD |
| `7D` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD |
| `1D` | `12.71` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 242.20 USD | 31.80 USD | 1.40 USD |
| `7D` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD |
| `1D` | `12.73` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 22,130.00 USD | 9,120.00 USD | 1.63 USD |
| `7D` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD |
| `1D` | `12.75` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 32,610.00 USD | 11,330.00 USD | 12,300.00 USD |
| `7D` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD |
| `1D` | `12.77` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 22,830.00 USD | 9,270.00 USD | 10,510.00 USD |
| `7D` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD |
| `1D` | `12.79` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 9,880.00 USD | 2,060.00 USD | 11,260.00 USD |
| `7D` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.81` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 7,290.00 USD | 3,830.00 USD | 7,630.00 USD |
| `7D` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.83` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 17,160.00 USD | 5,780.00 USD | 9,790.00 USD |
| `7D` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD |
| `1D` | `12.85` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 25,860.00 USD | 4,270.00 USD | 5,430.00 USD |
| `7D` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD |
| `1D` | `12.87` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 7,900.00 USD | 5,270.00 USD | 4,580.00 USD |
| `7D` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD |
| `1D` | `12.89` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 6,710.00 USD | 2,730.00 USD | 1,820.00 USD |
| `7D` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD |
| `1D` | `12.91` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 15,190.00 USD | 4,520.00 USD | 8,190.00 USD |
| `7D` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD |
| `1D` | `12.93` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 212.28 USD | 0.00 USD | 0.00 USD |
| `7D` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD |
| `1D` | `12.95` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 13,070.00 USD | 2,760.00 USD | 3,050.00 USD |
| `7D` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD |
| `1D` | `12.97` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 10,200.00 USD | 7,720.00 USD | 5,520.00 USD |
| `7D` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD |
| `7D` | `13.00` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD |
| `7D` | `13.02` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `7D` | `13.04` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 303.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.06` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD |
| `7D` | `13.10` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 18,460.00 USD | 5,730.00 USD | 7,600.00 USD |
| `7D` | `13.12` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 945.50 USD | 4,010.00 USD | 20.43 USD |
| `7D` | `13.14` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 321.45 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.16` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.86 USD |
| `7D` | `13.18` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,370.00 USD |
| `7D` | `13.20` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `13.22` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 23,980.00 USD | 213.60 USD | 37.80 USD |
| `7D` | `13.24` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 18,770.00 USD | 4,640.00 USD | 11,590.00 USD |
| `7D` | `13.26` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 463.75 USD | 5,860.00 USD | 10,920.00 USD |
| `7D` | `13.27` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 9,830.00 USD | 2,560.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `543.48M` | Total OI Tokens: `47,534,857.1 LINK`
  * 1h OI Change: `-2.10%` | 4h OI Change: `-5.04%` | 24h OI Change: `-5.81%`
  * Exchange Breakdown: Binance=`103.04M` | Bybit=`63.94M` | OKX=`26.19M` | Hyperliquid=`55.10M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.44K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0095%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0042%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0095%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0019%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `40.05%` | `59.95%` | `0.67` | 14,680,000.00 USD |
| `15M` | `Binance` | `40.42%` | `59.58%` | `0.68` | 4,330,000.00 USD |
| `15M` | `OKX` | `30.43%` | `69.57%` | `0.44` | 2,200,000.00 USD |
| `15M` | `Bybit` | `39.31%` | `60.69%` | `0.65` | 1,340,000.00 USD |
| `15M` | `KuCoin` | `61.02%` | `38.98%` | `1.57` | 121,890.00 USD |
| `15M` | `Gate` | `43.18%` | `56.82%` | `0.76` | 202,700.00 USD |
| `15M` | `Bitget` | `35.93%` | `64.07%` | `0.56` | 511,360.00 USD |
| `15M` | `BingX` | `17.91%` | `82.09%` | `0.22` | 330,500.00 USD |
| `15M` | `MEXC` | `49.95%` | `50.05%` | `1.00` | 3,550,000.00 USD |
| `15M` | `Bitunix` | `54.64%` | `45.36%` | `1.20` | 897,230.00 USD |
| `15M` | `Hyperliquid` | `15.47%` | `84.53%` | `0.18` | 414,960.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.98%` | `55.02%` | `0.82` | 266,800.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `14.72%` | `85.28%` | `0.17` | 337,510.00 USD |
| `15M` | `HTX` | `28.97%` | `71.03%` | `0.41` | 5,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `15.83%` | `84.17%` | `0.19` | 104,100.00 USD |
| `15M` | `Aster` | `12.05%` | `87.95%` | `0.14` | 30,670.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `20.89%` | `79.11%` | `0.26` | 30,730.00 USD |
| `15M` | `Whale Positions` | `40.42%` | `59.58%` | `0.68` | 4,330,000.00 USD |
| `15M` | `Global Accounts` | `40.05%` | `59.95%` | `0.67` | 14,680,000.00 USD |
| `1H` | `LINK` | `44.65%` | `55.35%` | `0.81` | 26,450,000.00 USD |
| `1H` | `Binance` | `44.9%` | `55.1%` | `0.81` | 7,100,000.00 USD |
| `1H` | `OKX` | `47.26%` | `52.74%` | `0.90` | 3,550,000.00 USD |
| `1H` | `Bybit` | `44.65%` | `55.35%` | `0.81` | 2,170,000.00 USD |
| `1H` | `KuCoin` | `45.95%` | `54.05%` | `0.85` | 112,040.00 USD |
| `1H` | `Gate` | `40.72%` | `59.28%` | `0.69` | 355,560.00 USD |
| `1H` | `Bitget` | `48.09%` | `51.91%` | `0.93` | 992,160.00 USD |
| `1H` | `BingX` | `36.54%` | `63.46%` | `0.58` | 739,680.00 USD |
| `1H` | `MEXC` | `48.88%` | `51.12%` | `0.96` | 8,550,000.00 USD |
| `1H` | `Bitunix` | `37.53%` | `62.47%` | `0.60` | 696,910.00 USD |
| `1H` | `Hyperliquid` | `26.97%` | `73.03%` | `0.37` | 606,820.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.21%` | `48.79%` | `1.05` | 495,790.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `6.35%` | `93.65%` | `0.07` | 788,360.00 USD |
| `1H` | `HTX` | `46.86%` | `53.14%` | `0.88` | 12,630.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.13%` | `56.87%` | `0.76` | 170,100.00 USD |
| `1H` | `Aster` | `23.71%` | `76.29%` | `0.31` | 48,090.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.89%` | `48.11%` | `1.08` | 66,820.00 USD |
| `1H` | `Whale Positions` | `44.9%` | `55.1%` | `0.81` | 7,100,000.00 USD |
| `1H` | `Global Accounts` | `44.65%` | `55.35%` | `0.81` | 26,450,000.00 USD |
| `4H` | `LINK` | `45.66%` | `54.34%` | `0.84` | 12,150,000.00 USD |
| `4H` | `Binance` | `51.65%` | `48.35%` | `1.07` | 4,180,000.00 USD |
| `4H` | `OKX` | `45.97%` | `54.03%` | `0.85` | 757,250.00 USD |
| `4H` | `Bybit` | `62.46%` | `37.54%` | `1.66` | 594,860.00 USD |
| `4H` | `KuCoin` | `50.58%` | `49.42%` | `1.02` | 258,290.00 USD |
| `4H` | `Gate` | `76.34%` | `23.66%` | `3.23` | 768,430.00 USD |
| `4H` | `Bitget` | `56.85%` | `43.15%` | `1.32` | 159,390.00 USD |
| `4H` | `BingX` | `24.66%` | `75.34%` | `0.33` | 1,090,000.00 USD |
| `4H` | `MEXC` | `54.62%` | `45.38%` | `1.20` | 114,680.00 USD |
| `4H` | `Bitunix` | `50.15%` | `49.85%` | `1.01` | 122,050.00 USD |
| `4H` | `Hyperliquid` | `74.19%` | `25.81%` | `2.87` | 265,140.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.8%` | `50.2%` | `0.99` | 1,850,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.1%` | `89.9%` | `0.11` | 1,620,000.00 USD |
| `4H` | `HTX` | `56.59%` | `43.41%` | `1.30` | 203,990.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `73.76%` | `26.24%` | `2.81` | 68,090.00 USD |
| `4H` | `Aster` | `12.23%` | `87.77%` | `0.14` | 9,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `25.08%` | `74.92%` | `0.33` | 94,780.00 USD |
| `4H` | `Whale Positions` | `51.65%` | `48.35%` | `1.07` | 4,180,000.00 USD |
| `4H` | `Global Accounts` | `45.66%` | `54.34%` | `0.84` | 12,150,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.71` | `11.70` | `11.71` | `11.74` | `11.66` | 1,705,508.25 USD | 855,092.75 USD | 850,415.50 USD | 4,677.25 USD | `+0.27%` | `14B / 10S` |
| `0:00 UTC` | `11.73` | `11.73` | `11.73` | `11.75` | `11.71` | 756,364.68 USD | 311,101.50 USD | 445,263.18 USD | -134,161.69 USD | `-17.74%` | `6B / 13S` |
| `5:00 UTC` | `11.74` | `11.73` | `11.74` | `11.76` | `11.69` | 1,033,883.46 USD | 539,127.77 USD | 494,755.69 USD | 44,372.08 USD | `+4.29%` | `15B / 13S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.68` | `11.66` | `11.68` | `11.68` | `11.63` | 997,243.09 USD | 360,139.33 USD | 637,103.76 USD | -276,964.43 USD | `-27.77%` | `11B / 15S` |
| `0:00 UTC` | `11.72` | `11.71` | `11.72` | `11.73` | `11.68` | 1,229,457.09 USD | 722,946.86 USD | 506,510.23 USD | 216,436.63 USD | `+17.60%` | `13B / 6S` |
| `5:00 UTC` | `11.70` | `11.70` | `11.70` | `11.72` | `11.68` | 638,959.31 USD | 356,011.33 USD | 282,947.98 USD | 73,063.35 USD | `+11.43%` | `5B / 5S` |
| `0:00 UTC` | `11.49` | `11.52` | `11.49` | `11.69` | `11.42` | 6,317,534.61 USD | 2,945,176.55 USD | 3,372,358.06 USD | -427,181.51 USD | `-6.76%` | `7B / 37S` |

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
| `5m` | -47,170.00 USD | -799,800.00 USD | **`DISTRIBUTION`** |
| `15m` | -76,020.00 USD | -774,160.00 USD | **`DISTRIBUTION`** |
| `30m` | -154,180.00 USD | -526,700.00 USD | **`DISTRIBUTION`** |
| `1h` | -256,150.00 USD | -271,600.00 USD | **`DISTRIBUTION`** |
| `2h` | -281,360.00 USD | -408,270.00 USD | **`DISTRIBUTION`** |
| `4h` | -844,530.00 USD | -3,040,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 221,240.00 USD | -787,080.00 USD | **`DISTRIBUTION`** |
| `8h` | 116,560.00 USD | -765,710.00 USD | **`DISTRIBUTION`** |
| `12h` | 23,250.00 USD | -173,410.00 USD | **`DISTRIBUTION`** |
| `24h` | -500,580.00 USD | -6,730,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,900,000.00 USD | -23,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -68,980,000.00 USD | -187,820,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-47.17K` | 15m=`-76.02K` | 1h=`-256.15K` | 24h=`-500.58K`
* Futures Capital Netflows: 5m=`-799.80K` | 15m=`-774.16K` | 1h=`-271.60K` | 24h=`-6.73M`
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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.89` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.11` (Risk Distance: `0.2140` pts)
  * +2.5R Take Profit: `11.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.60`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
