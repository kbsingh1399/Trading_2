# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-29 21:43:07 IST` (`2026-10-29 16:13:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.62` | **Live Ask Quote**: `11.71` | **Mid Price**: `11.66`
- **Spread Points**: `87.00` | **Spread BPS**: `74.60 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.46` | VWAP Z-Score: `+0.98` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0606` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.13` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.85` | Lower -3.00σ Band: `11.08`
  * Upper +2.51σ Band: `11.79` | Lower -2.51σ Band: `11.14`
  * Upper +2.01σ Band: `11.72` | Lower -2.01σ Band: `11.21`
  * Upper +2.00σ Band: `11.72` | Lower -2.00σ Band: `11.21`
  * Upper +1.28σ Band: `11.63` | Lower -1.28σ Band: `11.30`
  * Upper +1.00σ Band: `11.59` | Lower -1.00σ Band: `11.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.57` | EMA-20=`11.53` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.51` (Slope: `+0.0000`) | EMA-100=`11.52`
  * Institutional Anchors: EMA-144=`11.52` | EMA-200=`11.49` (Slope: `+0.0864`) | EMA-233=`11.48`
- **Range Boundaries**: 24H High=`11.94` | 24H Low=`11.23` | Weekly High=`11.94` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.61` (Distance: `+0.45%`)
  * Point of Control (POC) = `11.32` (Distance: `+2.99%`)
  * Value Area Low (VAL) = `11.29` (Distance: `+3.25%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.53` | Weekly POC=`11.42` | Weekly VAL=`11.26`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.64` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.62` - `11.71`
  * Optimal Trade Entry (OTE 0.705): `11.69`
  * Structural Invalidation Anchor (0.786): `11.76`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.64` | `11.67` | `11.63` | `11.66` | `45,780` | 533,357.90 USD | 75,313.87 USD | `+14.12%` | 434,535.20 USD | `+0.69` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `11.66` | `11.68` | `11.64` | `11.64` | `23,756` | 277,021.09 USD | 31,863.27 USD | `+11.50%` | 466,398.47 USD | `+0.35` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.64` | `11.67` | `11.63` | `11.67` | `21,824` | 254,171.26 USD | 8,416.69 USD | `+3.31%` | 474,815.16 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `11.69` | `11.69` | `11.57` | `11.58` | `186,638` | 2,167,857.89 USD | -356,455.30 USD | `-16.44%` | 265,265.93 USD | `-1.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.58` | `11.68` | `11.57` | `11.64` | `129,275` | 1,501,963.10 USD | 93,955.40 USD | `+6.26%` | 359,221.33 USD | `+0.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `11.64` | `11.68` | `11.63` | `11.67` | `91,361` | 1,064,550.25 USD | 115,593.83 USD | `+10.86%` | 474,815.16 USD | `+0.53` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `11.62` | `11.66` | `11.56` | `11.63` | `448,696` | 5,209,687.36 USD | 306,579.46 USD | `+5.88%` | 322,847.23 USD | `+0.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `11.63` | `11.70` | `11.57` | `11.64` | `589,055` | 6,856,308.35 USD | -443,587.09 USD | `-6.47%` | -120,739.85 USD | `-0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.64` | `11.68` | `11.63` | `11.67` | `91,402` | 1,065,037.62 USD | 115,106.46 USD | `+10.81%` | -5,633.39 USD | `+0.22` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | 598,953.30 USD | `-0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | 892,334.92 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.70` | `11.56` | `11.67` | `1,129,111` | 13,130,545.96 USD | -21,413.80 USD | `-0.16%` | 870,921.13 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.85` | `12.02` | `11.71` | `11.81` | `2,044,351` | 24,224,267.84 USD | 1,235,295.54 USD | `+5.10%` | 2,913,351.17 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | 563,139.18 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | 598,953.30 USD | `-0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | 892,334.92 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.70` | `11.56` | `11.67` | `1,129,111` | 13,130,545.96 USD | -21,413.80 USD | `-0.16%` | 870,921.13 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`11.66`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `498` | `0x73ce...8ce9` | `LONG` | 4,668,935.40 USD | `400,011,600.00` | `12.05` | `11.66` | `9.13` | -150,818.31 USD | `-3.23%` | `5X Cross` |
| `640` | `0x5b5d...c060` | `SHORT` | 3,638,491.55 USD | `311,728,200.00` | `13.61` | `11.66` | `448.91` | 603,640.56 USD | `+16.59%` | `3X Cross` |
| `651` | `0xb83d...6e36` | `SHORT` | 3,596,750.14 USD | `308,152,000.00` | `12.93` | `11.66` | `372.76` | 388,503.35 USD | `+10.80%` | `3X Cross` |
| `869` | `0x458d...ab3b` | `LONG` | 2,651,145.85 USD | `227,156,700.00` | `13.13` | `11.66` | `9.34` | -331,084.55 USD | `-12.49%` | `3X Isolated` |
| `952` | `0xdd53...2b13` | `SHORT` | 2,410,599.13 USD | `206,475,300.00` | `11.92` | `11.66` | `277.53` | 50,623.80 USD | `+2.10%` | `3X Cross` |
| `984` | `0x3dc9...54b0` | `SHORT` | 2,333,400.00 USD | `200,000,000.00` | `7.56` | `11.66` | `98.64` | -822,241.58 USD | `-35.24%` | `10X Cross` |
| `1005` | `0x45d2...4029` | `SHORT` | 2,282,267.00 USD | `195,500,000.00` | `11.54` | `11.66` | `182.08` | -25,783.57 USD | `-1.13%` | `10X Cross` |
| `1187` | `0x6540...f7b7` | `LONG` | 1,939,218.51 USD | `166,107,200.00` | `12.48` | `11.66` | `8.06` | -133,252.49 USD | `-6.87%` | `5X Isolated` |
| `1251` | `0xeadc...9d55` | `LONG` | 1,840,260.97 USD | `157,691,600.00` | `9.43` | `11.66` | `0.000000` | 353,606.07 USD | `+19.21%` | `10X Cross` |
| `1612` | `0x9df2...c665` | `SHORT` | 1,384,359.89 USD | `118,605,200.00` | `11.48` | `11.66` | `254.28` | -22,307.47 USD | `-1.61%` | `10X Cross` |
| `1640` | `0xf6f3...47f8` | `SHORT` | 1,341,646.93 USD | `115,024,600.00` | `11.42` | `11.66` | `18.11` | -28,316.75 USD | `-2.11%` | `5X Cross` |
| `1813` | `0xfe7e...11b4` | `LONG` | 1,180,630.57 USD | `101,142,000.00` | `14.47` | `11.66` | `5.32` | -282,482.58 USD | `-23.93%` | `5X Isolated` |
| `1841` | `0x8af7...fa05` | `SHORT` | 1,151,820.18 USD | `98,661,200.00` | `14.08` | `11.66` | `205.94` | 237,362.36 USD | `+20.61%` | `10X Cross` |
| `1899` | `0xb7ec...5166` | `LONG` | 1,103,095.07 USD | `94,515,900.00` | `9.01` | `11.66` | `7.20` | 251,234.49 USD | `+22.78%` | `4X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.45` | 7,522.65 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.52K USD at 11.4500 USD [API] | `2026-10-27 19:31:15` |
| `ANNOUNCEMENT` | `INFO` | `11.48` | 6,640.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.64K USD at 11.4850 USD [API] | `2026-10-27 19:58:25` |
| `ANNOUNCEMENT` | `INFO` | `11.46` | 5,830.72 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.83K USD at 11.4620 USD [API] | `2026-10-27 20:52:10` |
| `ANNOUNCEMENT` | `INFO` | `11.46` | 5,830.34 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.83K USD at 11.4590 USD [API] | `2026-10-27 20:53:18` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 5,463.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.5510 USD [API] | `2026-10-27 21:32:55` |
| `ANNOUNCEMENT` | `INFO` | `11.55` | 5,037.83 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.04K USD at 11.5520 USD [API] | `2026-10-27 21:32:55` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.80` (Vol: 215,600.00 USD, Dist: `+1.12%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.20%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+3.23%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.37%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.68%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.46%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.69%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 28,870.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 882.98 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 3,200.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,160.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 480.42 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 2,710.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 10,850.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 959.73 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 8,970.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 3,940.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 623.70 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 10,430.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 4,680.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 242,540.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 14,330.00 USD | 13,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 4,240.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,200.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 85,590.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 5,050.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 19,930.00 USD | 13,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 886.73 USD | 13,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 13,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 61,660.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 1,030.00 USD | 12,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 109,160.00 USD | 12,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 8,390.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 19,570.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 1,090.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 68,160.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 4,020.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 45,300.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 15,990.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 141,680.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 23,320.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 5,790.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,210.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 2,260.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 2,400.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 687,950.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 32,250.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 104,990.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 13,150.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 17,400.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 660.96 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 244.12 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 9,770.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 16,150.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,410,000.00 USD | 11,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,870.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 33,420.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,610.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 10,830.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 23,510.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 17,820.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 323,600.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,170.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,640.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 23,250.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,750,000.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 11,350.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 20,680.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 21,100.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 8,970.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 103,770.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 20,800.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.95` | 774,060.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.05` | 646,270.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `10.15` | 17,690.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.16` | 19,550,000.00 USD | 19,550,000.00 USD | 33,480.00 USD | 22,270.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 19,460,000.00 USD | 19,460,000.00 USD | 59,240.00 USD | 284.67 USD | 31,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 19,370,000.00 USD | 19,370,000.00 USD | 32,400.00 USD | 15,700.00 USD | 65,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 19,260,000.00 USD | 19,260,000.00 USD | 101,890.00 USD | 28,560.00 USD | 86,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 19,040,000.00 USD | 19,040,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 299,900.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.26` | 18,850,000.00 USD | 18,850,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 18,710,000.00 USD | 18,710,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 18,590,000.00 USD | 18,590,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 18,480,000.00 USD | 18,480,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 18,340,000.00 USD | 18,340,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 16,320.00 USD | 940,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.36` | 18,210,000.00 USD | 18,210,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 18,180,000.00 USD | 18,180,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 18,120,000.00 USD | 18,120,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 6,460,000.00 USD | 6,460,000.00 USD | 67,080.00 USD | 22,150.00 USD | 60,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 17,970,000.00 USD | 17,970,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 6,310,000.00 USD | 6,310,000.00 USD | 43,620.00 USD | 13,680.00 USD | 15,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 17,890,000.00 USD | 17,890,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 6,240,000.00 USD | 6,240,000.00 USD | 32,530.00 USD | 8,300.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 15,530.00 USD | 924,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.46` | 17,840,000.00 USD | 17,840,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.47` | 6,180,000.00 USD | 6,180,000.00 USD | 9,880.00 USD | 3,890.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 17,730,000.00 USD | 17,730,000.00 USD | 12,660.00 USD | 13,420.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 6,150,000.00 USD | 6,150,000.00 USD | 14,020.00 USD | 4,090.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 17,680,000.00 USD | 17,680,000.00 USD | 26,860.00 USD | 11,560.00 USD | 138.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 6,130,000.00 USD | 6,130,000.00 USD | 26,200.00 USD | 2,120.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 17,640,000.00 USD | 17,640,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 6,100,000.00 USD | 6,100,000.00 USD | 757.16 USD | 3,370.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 17,590,000.00 USD | 17,590,000.00 USD | 25,600.00 USD | 72.80 USD | 12,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 6,090,000.00 USD | 6,090,000.00 USD | 14,930.00 USD | 3,280.00 USD | 5,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 49,340.00 USD | 908,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.56` | 17,550,000.00 USD | 17,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 12,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.57` | 6,070,000.00 USD | 6,070,000.00 USD | 20,230.00 USD | 7,680.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 17,470,000.00 USD | 17,470,000.00 USD | 84,220.00 USD | 6,710.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 6,030,000.00 USD | 6,030,000.00 USD | 14,080.00 USD | 1,300.00 USD | 15.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 17,370,000.00 USD | 17,370,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 6,020,000.00 USD | 6,020,000.00 USD | 9,020.00 USD | 5,440.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 17,330,000.00 USD | 17,330,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 6,000,000.00 USD | 6,000,000.00 USD | 17,770.00 USD | 4,750.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 17,300,000.00 USD | 17,300,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 5,970,000.00 USD | 5,970,000.00 USD | 18,690.00 USD | 6,860.00 USD | 10,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 45,080.00 USD | 859,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.66` | 17,250,000.00 USD | 17,250,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.67` | 5,930,000.00 USD | 5,930,000.00 USD | 442.43 USD | 7.67 USD | 123.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 17,220,000.00 USD | 17,220,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 5,930,000.00 USD | 5,930,000.00 USD | 8,790.00 USD | 1,370.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 17,200,000.00 USD | 17,200,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 5,920,000.00 USD | 5,920,000.00 USD | 4,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 17,180,000.00 USD | 17,180,000.00 USD | 21,070.00 USD | 5,190.00 USD | 264.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 5,920,000.00 USD | 5,920,000.00 USD | 946.26 USD | 4,670.00 USD | 143.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 17,150,000.00 USD | 17,150,000.00 USD | 25,580.00 USD | 3,690.00 USD | 365.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 5,910,000.00 USD | 5,910,000.00 USD | 2,280.00 USD | 0.00 USD | 20.58 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 53,390.00 USD | 814,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.76` | 17,120,000.00 USD | 17,120,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.77` | 5,910,000.00 USD | 5,910,000.00 USD | 1,140.00 USD | 2,330.00 USD | 3,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 17,100,000.00 USD | 17,100,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 5,900,000.00 USD | 5,900,000.00 USD | 3,450.00 USD | 0.00 USD | 93.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 17,060,000.00 USD | 17,060,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 5,900,000.00 USD | 5,900,000.00 USD | 1,970.00 USD | 0.00 USD | 64.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 16,920,000.00 USD | 16,920,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.83` | 5,900,000.00 USD | 5,900,000.00 USD | 3,650.00 USD | 160.15 USD | 76.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 16,740,000.00 USD | 16,740,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.85` | 5,890,000.00 USD | 5,890,000.00 USD | 1,690.00 USD | 4,450.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 109,520.00 USD | 760,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.86` | 16,580,000.00 USD | 16,580,000.00 USD | 238,230.00 USD | 18,350.00 USD | 95,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.87` | 5,880,000.00 USD | 5,880,000.00 USD | 493.01 USD | 2,760.00 USD | 297.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 16,230,000.00 USD | 16,230,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.89` | 5,880,000.00 USD | 5,880,000.00 USD | 6,320.00 USD | 11,320.00 USD | 36,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 15,760,000.00 USD | 15,760,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.91` | 5,830,000.00 USD | 5,830,000.00 USD | 3,580.00 USD | 10,840.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 15,330,000.00 USD | 15,330,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.93` | 5,790,000.00 USD | 5,790,000.00 USD | 98,690.00 USD | 28,100.00 USD | 41,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 14,430,000.00 USD | 14,430,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.95` | 5,620,000.00 USD | 5,620,000.00 USD | 44,790.00 USD | 14,550.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,850.00 USD | 651,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.96` | 13,840,000.00 USD | 13,840,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.97` | 5,540,000.00 USD | 5,540,000.00 USD | 80,360.00 USD | 15,940.00 USD | 33,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 13,280,000.00 USD | 13,280,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.99` | 5,410,000.00 USD | 5,410,000.00 USD | 19,680.00 USD | 10,180.00 USD | 15,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 12,910,000.00 USD | 12,910,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.01` | 5,370,000.00 USD | 5,370,000.00 USD | 50,740.00 USD | 23,880.00 USD | 28,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 12,530,000.00 USD | 12,530,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.03` | 5,260,000.00 USD | 5,260,000.00 USD | 80,130.00 USD | 28,700.00 USD | 53,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,020,000.00 USD | 12,020,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.05` | 5,100,000.00 USD | 5,100,000.00 USD | 14,150.00 USD | 2,650.00 USD | 27,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 29,270.00 USD | 92,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.06` | 11,360,000.00 USD | 11,360,000.00 USD | 127,210.00 USD | 102,780.00 USD | 172,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.07` | 5,060,000.00 USD | 5,060,000.00 USD | 60,560.00 USD | 25,720.00 USD | 87,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 10,960,000.00 USD | 10,960,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.09` | 4,880,000.00 USD | 4,880,000.00 USD | 113,640.00 USD | 36,820.00 USD | 104,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 10,150,000.00 USD | 10,150,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.11` | 4,630,000.00 USD | 4,630,000.00 USD | 100,660.00 USD | 56,750.00 USD | 146,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 8,960,000.00 USD | 8,960,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.13` | 4,320,000.00 USD | 4,320,000.00 USD | 117,830.00 USD | 62,700.00 USD | 98,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 7,910,000.00 USD | 7,910,000.00 USD | 693,360.00 USD | 172,020.00 USD | 596,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.15` | 4,040,000.00 USD | 4,040,000.00 USD | 216,180.00 USD | 64,850.00 USD | 118,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 51,580.00 USD | 63,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.16` | 6,440,000.00 USD | 6,440,000.00 USD | 653,240.00 USD | 189,310.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.17` | 3,640,000.00 USD | 3,640,000.00 USD | 143,330.00 USD | 54,400.00 USD | 53,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 5,140,000.00 USD | 5,140,000.00 USD | 626,210.00 USD | 214,580.00 USD | 528,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.19` | 3,390,000.00 USD | 3,390,000.00 USD | 218,360.00 USD | 52,130.00 USD | 68,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 3,770,000.00 USD | 3,770,000.00 USD | 318,980.00 USD | 228,870.00 USD | 110,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.21` | 3,050,000.00 USD | 3,050,000.00 USD | 111,230.00 USD | 12,810.00 USD | 69,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,110,000.00 USD | 3,110,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.23` | 2,860,000.00 USD | 2,860,000.00 USD | 38,220.00 USD | 29,800.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 2,460,000.00 USD | 2,460,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.25` | 2,730,000.00 USD | 2,730,000.00 USD | 233,570.00 USD | 77,120.00 USD | 90,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 11,530.00 USD | 11,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,180,000.00 USD | 2,180,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.27` | 2,330,000.00 USD | 2,330,000.00 USD | 101,350.00 USD | 70,300.00 USD | 96,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 1,630,000.00 USD | 1,630,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.29` | 2,060,000.00 USD | 2,060,000.00 USD | 128,000.00 USD | 24,250.00 USD | 51,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,230,000.00 USD | 1,230,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.31` | 1,860,000.00 USD | 1,860,000.00 USD | 140,310.00 USD | 12,410.00 USD | 29,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,170,000.00 USD | 1,170,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.33` | 1,670,000.00 USD | 1,670,000.00 USD | 344,120.00 USD | 19,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,040,000.00 USD | 1,040,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.35` | 1,310,000.00 USD | 1,310,000.00 USD | 186,490.00 USD | 74,960.00 USD | 45,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 699,820.00 USD | 699,820.00 USD | 170,150.00 USD | 39,980.00 USD | 29,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.37` | 1,000,000.00 USD | 1,000,000.00 USD | 175,960.00 USD | 42,900.00 USD | 84,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 460,540.00 USD | 460,540.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.39` | 699,910.00 USD | 699,910.00 USD | 54,830.00 USD | 33,810.00 USD | 47,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 369,160.00 USD | 369,160.00 USD | 116,360.00 USD | 0.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.41` | 563,670.00 USD | 563,670.00 USD | 72,850.00 USD | 9,100.00 USD | 37,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.43` | 444,430.00 USD | 444,430.00 USD | 51,370.00 USD | 11,040.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 235,980.00 USD | 235,980.00 USD | 0.00 USD | 7,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.45` | 360,640.00 USD | 360,640.00 USD | 95,760.00 USD | 10,310.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 228,590.00 USD | 228,590.00 USD | 0.00 USD | 364.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.49` | 233,850.00 USD | 233,850.00 USD | 0.00 USD | 834.95 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 228,230.00 USD | 228,230.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.51` | 233,020.00 USD | 233,020.00 USD | 63,350.00 USD | 53,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.52` | 187,250.00 USD | 187,250.00 USD | 0.00 USD | 617.33 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.54` | 186,630.00 USD | 186,630.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.56` | 151,860.00 USD | 151,860.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.57` | 116,220.00 USD | 116,220.00 USD | 0.00 USD | 0.00 USD | 48,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.58` | 141,230.00 USD | 141,230.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.61` | 67,480.00 USD | 67,480.00 USD | 66,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.64` | 109,610.00 USD | 109,610.00 USD | 0.00 USD | 57,480.00 USD | 52,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.65` | 590.50 USD | 590.50 USD | 0.00 USD | 590.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 60,440.00 USD | 60,440.00 USD | 33,150.00 USD | 0.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.67` | 366.47 USD | 366.47 USD | 0.00 USD | 366.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 161,050.00 USD | 161,050.00 USD | 82,060.00 USD | 18,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 831.76 USD | 831.76 USD | 0.00 USD | 465.29 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 301,400.00 USD | 301,400.00 USD | 188,350.00 USD | 48,480.00 USD | 63,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 345,730.00 USD | 345,730.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 369,460.00 USD | 369,460.00 USD | 25,600.00 USD | 36,880.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 368,800.00 USD | 368,800.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 519,930.00 USD | 519,930.00 USD | 95,330.00 USD | 10,850.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 436,240.00 USD | 436,240.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.77` | 830,690.00 USD | 830,690.00 USD | 53,950.00 USD | 15,050.00 USD | 241,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 676,210.00 USD | 676,210.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 1,050,000.00 USD | 1,050,000.00 USD | 62,440.00 USD | 30,260.00 USD | 123,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 905,550.00 USD | 905,550.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 1,280,000.00 USD | 1,280,000.00 USD | 104,080.00 USD | 61,930.00 USD | 71,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 1,210,000.00 USD | 1,210,000.00 USD | 158,640.00 USD | 69,570.00 USD | 75,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 1,710,000.00 USD | 1,710,000.00 USD | 234,650.00 USD | 68,330.00 USD | 125,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,730,000.00 USD | 1,730,000.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 2,020,000.00 USD | 2,020,000.00 USD | 162,890.00 USD | 53,170.00 USD | 91,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.86` | 2,640,000.00 USD | 2,640,000.00 USD | 607,590.00 USD | 35,340.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 2,220,000.00 USD | 2,220,000.00 USD | 117,230.00 USD | 32,850.00 USD | 54,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 3,270,000.00 USD | 3,270,000.00 USD | 361,940.00 USD | 20,500.00 USD | 247,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 2,440,000.00 USD | 2,440,000.00 USD | 132,310.00 USD | 26,980.00 USD | 55,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 3,580,000.00 USD | 3,580,000.00 USD | 177,950.00 USD | 8,800.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 2,620,000.00 USD | 2,620,000.00 USD | 112,550.00 USD | 20,860.00 USD | 44,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 4,080,000.00 USD | 4,080,000.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 2,790,000.00 USD | 2,790,000.00 USD | 71,670.00 USD | 32,980.00 USD | 65,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 4,600,000.00 USD | 4,600,000.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 3,060,000.00 USD | 3,060,000.00 USD | 167,340.00 USD | 41,470.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 209.12 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.96` | 5,110,000.00 USD | 5,110,000.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 3,200,000.00 USD | 3,200,000.00 USD | 120,770.00 USD | 989.33 USD | 18,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 5,700,000.00 USD | 5,700,000.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 3,350,000.00 USD | 3,350,000.00 USD | 60,740.00 USD | 5,690.00 USD | 82,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 6,200,000.00 USD | 6,200,000.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 3,670,000.00 USD | 3,670,000.00 USD | 172,920.00 USD | 43,150.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 6,740,000.00 USD | 6,740,000.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 4,020,000.00 USD | 4,020,000.00 USD | 189,020.00 USD | 71,960.00 USD | 91,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 7,290,000.00 USD | 7,290,000.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 4,430,000.00 USD | 4,430,000.00 USD | 237,860.00 USD | 75,640.00 USD | 98,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.05` | 1,530.00 USD | 2,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.06` | 7,760,000.00 USD | 7,760,000.00 USD | 234,210.00 USD | 97,430.00 USD | 137,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 4,790,000.00 USD | 4,790,000.00 USD | 185,870.00 USD | 68,300.00 USD | 104,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 8,390,000.00 USD | 8,390,000.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 4,840,000.00 USD | 4,840,000.00 USD | 18,290.00 USD | 7,990.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 8,520,000.00 USD | 8,520,000.00 USD | 32,390.00 USD | 73,790.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 4,960,000.00 USD | 4,960,000.00 USD | 63,310.00 USD | 20,950.00 USD | 35,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 8,720,000.00 USD | 8,720,000.00 USD | 74,360.00 USD | 44,490.00 USD | 83,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 5,050,000.00 USD | 5,050,000.00 USD | 62,900.00 USD | 12,200.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 8,850,000.00 USD | 8,850,000.00 USD | 66,650.00 USD | 53,630.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 5,170,000.00 USD | 5,170,000.00 USD | 88,900.00 USD | 19,410.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 2,330.00 USD | 5,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.16` | 9,110,000.00 USD | 9,110,000.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 5,230,000.00 USD | 5,230,000.00 USD | 11,830.00 USD | 25,930.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 9,210,000.00 USD | 9,210,000.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 5,310,000.00 USD | 5,310,000.00 USD | 48,340.00 USD | 15,220.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 9,480,000.00 USD | 9,480,000.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 5,440,000.00 USD | 5,440,000.00 USD | 54,620.00 USD | 38,740.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 9,850,000.00 USD | 9,850,000.00 USD | 259,700.00 USD | 19,920.00 USD | 93,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 5,480,000.00 USD | 5,480,000.00 USD | 34,170.00 USD | 8,610.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 10,110,000.00 USD | 10,110,000.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 5,520,000.00 USD | 5,520,000.00 USD | 21,110.00 USD | 11,680.00 USD | 0.52 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,510.00 USD | 6,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.26` | 10,370,000.00 USD | 10,370,000.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.27` | 5,620,000.00 USD | 5,620,000.00 USD | 66,900.00 USD | 15,720.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 10,840,000.00 USD | 10,840,000.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 5,720,000.00 USD | 5,720,000.00 USD | 38,660.00 USD | 20,940.00 USD | 43,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 11,180,000.00 USD | 11,180,000.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 5,780,000.00 USD | 5,780,000.00 USD | 43,710.00 USD | 8,690.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 11,360,000.00 USD | 11,360,000.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 5,780,000.00 USD | 5,780,000.00 USD | 1,930.00 USD | 19.17 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 11,590,000.00 USD | 11,590,000.00 USD | 140,600.00 USD | 75,950.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 5,810,000.00 USD | 5,810,000.00 USD | 14,000.00 USD | 3,440.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 941.07 USD | 7,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 11,700,000.00 USD | 11,700,000.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.37` | 5,830,000.00 USD | 5,830,000.00 USD | 19,180.00 USD | 3,340.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 11,850,000.00 USD | 11,850,000.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 5,850,000.00 USD | 5,850,000.00 USD | 12,700.00 USD | 5,880.00 USD | 140.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 12,330,000.00 USD | 12,330,000.00 USD | 176,820.00 USD | 41,150.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 5,860,000.00 USD | 5,860,000.00 USD | 1,600.00 USD | 5,800.00 USD | 51.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 12,930,000.00 USD | 12,930,000.00 USD | 155,030.00 USD | 33,450.00 USD | 407,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 5,860,000.00 USD | 5,860,000.00 USD | 764.68 USD | 0.00 USD | 132.56 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 13,450,000.00 USD | 13,450,000.00 USD | 181,610.00 USD | 70,960.00 USD | 272,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 5,880,000.00 USD | 5,880,000.00 USD | 5,200.00 USD | 5,860.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 13,700,000.00 USD | 13,700,000.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 5,890,000.00 USD | 5,890,000.00 USD | 2,170.00 USD | 3,080.00 USD | 12,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 13,940,000.00 USD | 13,940,000.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.49` | 5,900,000.00 USD | 5,900,000.00 USD | 1,710.00 USD | 63.95 USD | 1,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 14,190,000.00 USD | 14,190,000.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.51` | 5,930,000.00 USD | 5,930,000.00 USD | 11,040.00 USD | 7,590.00 USD | 14,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 14,530,000.00 USD | 14,530,000.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.53` | 5,960,000.00 USD | 5,960,000.00 USD | 18,490.00 USD | 1,680.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 14,790,000.00 USD | 14,790,000.00 USD | 98,500.00 USD | 59,960.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.55` | 5,980,000.00 USD | 5,980,000.00 USD | 17,070.00 USD | 5,800.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 313.75 USD | 7,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.56` | 14,980,000.00 USD | 14,980,000.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.57` | 6,020,000.00 USD | 6,020,000.00 USD | 15,370.00 USD | 6,380.00 USD | 13,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 15,180,000.00 USD | 15,180,000.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.59` | 6,030,000.00 USD | 6,030,000.00 USD | 4,030.00 USD | 1,010.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 15,300,000.00 USD | 15,300,000.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.61` | 6,040,000.00 USD | 6,040,000.00 USD | 5,510.00 USD | 1,350.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 15,370,000.00 USD | 15,370,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.63` | 6,090,000.00 USD | 6,090,000.00 USD | 26,330.00 USD | 12,190.00 USD | 11,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 15,670,000.00 USD | 15,670,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.65` | 6,110,000.00 USD | 6,110,000.00 USD | 8,950.00 USD | 7,890.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 15,820,000.00 USD | 15,820,000.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.67` | 6,140,000.00 USD | 6,140,000.00 USD | 10,850.00 USD | 1,840.00 USD | 13,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 16,120,000.00 USD | 16,120,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.69` | 6,210,000.00 USD | 6,210,000.00 USD | 10,910.00 USD | 11,600.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 16,330,000.00 USD | 16,330,000.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.71` | 6,250,000.00 USD | 6,250,000.00 USD | 25,710.00 USD | 2,730.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 16,520,000.00 USD | 16,520,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.73` | 6,320,000.00 USD | 6,320,000.00 USD | 35,330.00 USD | 11,880.00 USD | 20,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 16,600,000.00 USD | 16,600,000.00 USD | 39,840.00 USD | 18,330.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.75` | 6,390,000.00 USD | 6,390,000.00 USD | 43,620.00 USD | 13,680.00 USD | 15,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 16,650,000.00 USD | 16,650,000.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.77` | 6,450,000.00 USD | 6,450,000.00 USD | 32,530.00 USD | 8,300.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 16,760,000.00 USD | 16,760,000.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.79` | 6,470,000.00 USD | 6,470,000.00 USD | 9,880.00 USD | 3,890.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 16,820,000.00 USD | 16,820,000.00 USD | 15,850.00 USD | 13,420.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.81` | 6,480,000.00 USD | 6,480,000.00 USD | 7,290.00 USD | 2,860.00 USD | 28.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 16,830,000.00 USD | 16,830,000.00 USD | 14,750.00 USD | 132.05 USD | 52.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.83` | 6,490,000.00 USD | 6,490,000.00 USD | 6,730.00 USD | 1,230.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 16,860,000.00 USD | 16,860,000.00 USD | 14,540.00 USD | 11,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.85` | 6,530,000.00 USD | 6,530,000.00 USD | 26,200.00 USD | 2,120.00 USD | 3,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 8,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.86` | 16,900,000.00 USD | 16,900,000.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.87` | 6,540,000.00 USD | 6,540,000.00 USD | 582.95 USD | 3,320.00 USD | 7,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 6,550,000.00 USD | 6,550,000.00 USD | 7,490.00 USD | 1,490.00 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 16,940,000.00 USD | 16,940,000.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 17,010,000.00 USD | 17,010,000.00 USD | 41,140.00 USD | 16,610.00 USD | 12,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.35` | 499.29 USD | 8,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,760.00 USD | 14,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 3,150.00 USD | 17,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 37,110.00 USD | 54,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 37,670.00 USD | 92,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 898.79 USD | 93,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 3,280.00 USD | 96,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 139.18 USD | 96,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 615.08 USD | 97,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.85` | 148,830.00 USD | 245,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 252.65 USD | 246,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.05` | 65,030.00 USD | 311,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 46,380.00 USD | 357,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 1,180.00 USD | 358,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 178.41 USD | 358,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 32,620.00 USD | 391,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 391,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 392,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.05` | 1,270.00 USD | 393,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 4,990.00 USD | 398,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 104.64 USD | 398,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 25,170.00 USD | 423,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 66,100.00 USD | 489,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 82,920.00 USD | 572,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 8,240.00 USD | 580,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 338,760.00 USD | 919,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 2,370.00 USD | 921,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 922,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 922,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 5,130.00 USD | 927,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 2,090,000.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 660.38 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 289.81 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 759,860.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.75` | 168.07 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.15` | 2,220.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.45` | 1,500.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 2,040.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 193.16 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.15` | 411,440.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.75` | 910.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 13,560,000.00 USD | 0.00 USD | 28,870.00 USD | `-79.83%` | `12,286,800.00` |
| `Live` | `Long` | `2.45` | 13,530,000.00 USD | 0.00 USD | 882.98 USD | `-78.97%` | `360,400.00` |
| `Live` | `Long` | `2.55` | 13,530,000.00 USD | 0.00 USD | 3,200.00 USD | `-78.11%` | `1,255,000.00` |
| `Live` | `Long` | `2.65` | 13,520,000.00 USD | 0.00 USD | 2,160.00 USD | `-77.25%` | `815,700.00` |
| `Live` | `Long` | `2.75` | 13,520,000.00 USD | 0.00 USD | 480.42 USD | `-76.39%` | `174,700.00` |
| `Live` | `Long` | `2.95` | 13,520,000.00 USD | 0.00 USD | 2,710.00 USD | `-74.68%` | `920,000.00` |
| `Live` | `Long` | `3.05` | 13,520,000.00 USD | 0.00 USD | 6,390.00 USD | `-73.82%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 13,510,000.00 USD | 0.00 USD | 10,850.00 USD | `-72.96%` | `3,445,100.00` |
| `Live` | `Long` | `3.25` | 13,500,000.00 USD | 0.00 USD | 959.73 USD | `-72.10%` | `295,300.00` |
| `Live` | `Long` | `3.35` | 13,500,000.00 USD | 0.00 USD | 8,970.00 USD | `-71.24%` | `2,677,000.00` |
| `Live` | `Long` | `3.65` | 13,490,000.00 USD | 0.00 USD | 3,940.00 USD | `-68.67%` | `1,078,400.00` |
| `Live` | `Long` | `3.85` | 13,490,000.00 USD | 0.00 USD | 623.70 USD | `-66.95%` | `162,000.00` |
| `Live` | `Long` | `3.95` | 13,490,000.00 USD | 0.00 USD | 10,430.00 USD | `-66.09%` | `2,639,600.00` |
| `Live` | `Long` | `4.05` | 13,480,000.00 USD | 0.00 USD | 4,680.00 USD | `-65.24%` | `1,154,500.00` |
| `Live` | `Long` | `4.25` | 13,470,000.00 USD | 0.00 USD | 5,090.00 USD | `-63.52%` | `1,198,100.00` |
| `Live` | `Long` | `4.45` | 13,470,000.00 USD | 0.00 USD | 381.37 USD | `-61.80%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 13,460,000.00 USD | 0.00 USD | 242,540.00 USD | `-60.94%` | `53,305,200.00` |
| `Live` | `Long` | `4.65` | 13,220,000.00 USD | 0.00 USD | 14,330.00 USD | `-60.09%` | `3,082,500.00` |
| `Live` | `Long` | `4.75` | 13,210,000.00 USD | 0.00 USD | 4,240.00 USD | `-59.23%` | `893,200.00` |
| `Live` | `Long` | `4.85` | 13,200,000.00 USD | 0.00 USD | 1,200.00 USD | `-58.37%` | `247,100.00` |
| `Live` | `Long` | `4.95` | 13,200,000.00 USD | 0.00 USD | 85,590.00 USD | `-57.51%` | `17,290,700.00` |
| `Live` | `Long` | `5.05` | 13,120,000.00 USD | 0.00 USD | 5,050.00 USD | `-56.65%` | `1,000,000.00` |
| `Live` | `Long` | `5.15` | 13,110,000.00 USD | 0.00 USD | 19,930.00 USD | `-55.79%` | `3,869,000.00` |
| `Live` | `Long` | `5.25` | 13,090,000.00 USD | 0.00 USD | 886.73 USD | `-54.94%` | `168,900.00` |
| `Live` | `Long` | `5.35` | 13,090,000.00 USD | 0.00 USD | 541,800.00 USD | `-54.08%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 12,550,000.00 USD | 0.00 USD | 61,660.00 USD | `-53.22%` | `11,313,200.00` |
| `Live` | `Long` | `5.55` | 12,490,000.00 USD | 0.00 USD | 1,030.00 USD | `-52.36%` | `184,800.00` |
| `Live` | `Long` | `5.65` | 12,490,000.00 USD | 0.00 USD | 109,160.00 USD | `-51.50%` | `19,320,800.00` |
| `Live` | `Long` | `5.75` | 12,380,000.00 USD | 0.00 USD | 8,390.00 USD | `-50.64%` | `1,458,900.00` |
| `Live` | `Long` | `5.85` | 12,370,000.00 USD | 0.00 USD | 19,570.00 USD | `-49.79%` | `3,346,100.00` |
| `Live` | `Long` | `5.95` | 12,350,000.00 USD | 0.00 USD | 1,090.00 USD | `-48.93%` | `183,400.00` |
| `Live` | `Long` | `6.05` | 12,350,000.00 USD | 0.00 USD | 68,160.00 USD | `-48.07%` | `11,265,500.00` |
| `Live` | `Long` | `6.15` | 12,280,000.00 USD | 0.00 USD | 4,020.00 USD | `-47.21%` | `654,300.00` |
| `Live` | `Long` | `6.25` | 12,280,000.00 USD | 0.00 USD | 45,300.00 USD | `-46.35%` | `7,248,700.00` |
| `Live` | `Long` | `6.35` | 12,230,000.00 USD | 0.00 USD | 15,990.00 USD | `-45.49%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 12,220,000.00 USD | 0.00 USD | 141,680.00 USD | `-44.64%` | `21,966,200.00` |
| `Live` | `Long` | `6.55` | 12,070,000.00 USD | 0.00 USD | 2,710.00 USD | `-43.78%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 12,070,000.00 USD | 0.00 USD | 23,320.00 USD | `-42.92%` | `3,506,700.00` |
| `Live` | `Long` | `6.75` | 12,050,000.00 USD | 0.00 USD | 5,790.00 USD | `-42.06%` | `857,800.00` |
| `Live` | `Long` | `6.85` | 12,040,000.00 USD | 0.00 USD | 5,210.00 USD | `-41.20%` | `761,200.00` |
| `Live` | `Long` | `6.95` | 12,040,000.00 USD | 0.00 USD | 2,260.00 USD | `-40.34%` | `325,300.00` |
| `Live` | `Long` | `7.05` | 12,030,000.00 USD | 0.00 USD | 2,400.00 USD | `-39.48%` | `340,900.00` |
| `Live` | `Long` | `7.15` | 12,030,000.00 USD | 0.00 USD | 687,950.00 USD | `-38.63%` | `96,216,900.00` |
| `Live` | `Long` | `7.25` | 11,340,000.00 USD | 0.00 USD | 32,250.00 USD | `-37.77%` | `4,447,600.00` |
| `Live` | `Long` | `7.35` | 11,310,000.00 USD | 0.00 USD | 104,990.00 USD | `-36.91%` | `14,284,100.00` |
| `Live` | `Long` | `7.45` | 11,210,000.00 USD | 0.00 USD | 13,150.00 USD | `-36.05%` | `1,765,000.00` |
| `Live` | `Long` | `7.55` | 11,190,000.00 USD | 0.00 USD | 17,400.00 USD | `-35.19%` | `2,304,000.00` |
| `Live` | `Long` | `7.65` | 11,180,000.00 USD | 0.00 USD | 660.96 USD | `-34.33%` | `86,400.00` |
| `Live` | `Long` | `7.75` | 11,180,000.00 USD | 0.00 USD | 244.12 USD | `-33.48%` | `31,500.00` |
| `Live` | `Long` | `7.85` | 11,180,000.00 USD | 0.00 USD | 9,770.00 USD | `-32.62%` | `1,244,000.00` |
| `Live` | `Long` | `7.95` | 11,170,000.00 USD | 0.00 USD | 16,150.00 USD | `-31.76%` | `2,031,600.00` |
| `Live` | `Long` | `8.05` | 11,150,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-30.90%` | `174,973,200.00` |
| `Live` | `Long` | `8.15` | 9,740,000.00 USD | 0.00 USD | 16,870.00 USD | `-30.04%` | `2,069,600.00` |
| `Live` | `Long` | `8.25` | 9,720,000.00 USD | 0.00 USD | 33,420.00 USD | `-29.18%` | `4,051,000.00` |
| `Live` | `Long` | `8.35` | 9,690,000.00 USD | 0.00 USD | 7,610.00 USD | `-28.33%` | `911,400.00` |
| `Live` | `Long` | `8.45` | 9,680,000.00 USD | 0.00 USD | 10,830.00 USD | `-27.47%` | `1,281,100.00` |
| `Live` | `Long` | `8.55` | 9,670,000.00 USD | 0.00 USD | 23,510.00 USD | `-26.61%` | `2,750,200.00` |
| `Live` | `Long` | `8.65` | 9,650,000.00 USD | 0.00 USD | 17,820.00 USD | `-25.75%` | `2,060,600.00` |
| `Live` | `Long` | `8.75` | 9,630,000.00 USD | 0.00 USD | 323,600.00 USD | `-24.89%` | `36,983,000.00` |
| `Live` | `Long` | `8.85` | 9,310,000.00 USD | 0.00 USD | 28,170.00 USD | `-24.03%` | `3,183,500.00` |
| `Live` | `Long` | `8.95` | 9,280,000.00 USD | 0.00 USD | 486,640.00 USD | `-23.18%` | `54,373,700.00` |
| `Live` | `Long` | `9.05` | 8,790,000.00 USD | 0.00 USD | 23,250.00 USD | `-22.32%` | `2,569,300.00` |
| `Live` | `Long` | `9.15` | 8,770,000.00 USD | 0.00 USD | 3,750,000.00 USD | `-21.46%` | `410,230,300.00` |
| `Live` | `Long` | `9.25` | 5,020,000.00 USD | 0.00 USD | 11,350.00 USD | `-20.60%` | `1,227,200.00` |
| `Live` | `Long` | `9.35` | 5,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-19.74%` | `229,970,500.00` |
| `Live` | `Long` | `9.45` | 2,850,000.00 USD | 0.00 USD | 20,680.00 USD | `-18.88%` | `2,187,900.00` |
| `Live` | `Long` | `9.55` | 2,830,000.00 USD | 0.00 USD | 21,100.00 USD | `-18.03%` | `2,209,900.00` |
| `Live` | `Long` | `9.65` | 2,810,000.00 USD | 0.00 USD | 8,970.00 USD | `-17.17%` | `929,200.00` |
| `Live` | `Long` | `9.75` | 2,800,000.00 USD | 0.00 USD | 103,770.00 USD | `-16.31%` | `10,642,900.00` |
| `Live` | `Long` | `9.85` | 2,700,000.00 USD | 0.00 USD | 20,800.00 USD | `-15.45%` | `2,111,400.00` |
| `Live` | `Long` | `9.95` | 2,680,000.00 USD | 0.00 USD | 774,060.00 USD | `-14.59%` | `77,795,000.00` |
| `Live` | `Long` | `10.05` | 1,900,000.00 USD | 0.00 USD | 646,270.00 USD | `-13.73%` | `64,305,900.00` |
| `Live` | `Long` | `10.15` | 1,260,000.00 USD | 0.00 USD | 17,690.00 USD | `-12.88%` | `1,743,300.00` |
| `Live` | `Long` | `10.25` | 1,240,000.00 USD | 0.00 USD | 299,900.00 USD | `-12.02%` | `29,258,100.00` |
| `Live` | `Long` | `10.35` | 940,410.00 USD | 0.00 USD | 16,320.00 USD | `-11.16%` | `1,577,100.00` |
| `Live` | `Long` | `10.45` | 924,090.00 USD | 0.00 USD | 15,530.00 USD | `-10.30%` | `1,486,300.00` |
| `Live` | `Long` | `10.55` | 908,560.00 USD | 0.00 USD | 49,340.00 USD | `-9.44%` | `4,676,500.00` |
| `Live` | `Long` | `10.65` | 859,220.00 USD | 0.00 USD | 45,080.00 USD | `-8.58%` | `4,233,300.00` |
| `Live` | `Long` | `10.75` | 814,140.00 USD | 0.00 USD | 53,390.00 USD | `-7.73%` | `4,966,200.00` |
| `Live` | `Long` | `10.85` | 760,750.00 USD | 0.00 USD | 109,520.00 USD | `-6.87%` | `10,093,800.00` |
| `Live` | `Long` | `10.95` | 651,230.00 USD | 0.00 USD | 558,850.00 USD | `-6.01%` | `51,036,400.00` |
| `Live` | `Long` | `11.05` | 92,380.00 USD | 0.00 USD | 29,270.00 USD | `-5.15%` | `2,648,700.00` |
| `Live` | `Long` | `11.15` | 63,120.00 USD | 0.00 USD | 51,580.00 USD | `-4.29%` | `4,626,400.00` |
| `Live` | `Long` | `11.25` | 11,530.00 USD | 0.00 USD | 11,530.00 USD | `-3.43%` | `1,025,100.00` |
| `Live` | `Short` | `11.85` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | `+1.72%` | `87,900.00` |
| `Live` | `Short` | `11.95` | 1,250.00 USD | 209.12 USD | 0.00 USD | `+2.58%` | `17,500.00` |
| `Live` | `Short` | `12.05` | 2,780.00 USD | 1,530.00 USD | 0.00 USD | `+3.43%` | `126,900.00` |
| `Live` | `Short` | `12.15` | 5,110.00 USD | 2,330.00 USD | 0.00 USD | `+4.29%` | `191,500.00` |
| `Live` | `Short` | `12.25` | 6,610.00 USD | 1,510.00 USD | 0.00 USD | `+5.15%` | `123,100.00` |
| `Live` | `Short` | `12.35` | 7,560.00 USD | 941.07 USD | 0.00 USD | `+6.01%` | `76,200.00` |
| `Live` | `Short` | `12.55` | 7,870.00 USD | 313.75 USD | 0.00 USD | `+7.73%` | `25,000.00` |
| `Live` | `Short` | `12.85` | 8,010.00 USD | 138.78 USD | 0.00 USD | `+10.30%` | `10,800.00` |
| `Live` | `Short` | `13.35` | 8,510.00 USD | 499.29 USD | 0.00 USD | `+14.59%` | `37,400.00` |
| `Live` | `Short` | `13.45` | 14,270.00 USD | 5,760.00 USD | 0.00 USD | `+15.45%` | `428,100.00` |
| `Live` | `Short` | `13.55` | 17,410.00 USD | 3,150.00 USD | 0.00 USD | `+16.31%` | `232,400.00` |
| `Live` | `Short` | `14.05` | 54,530.00 USD | 37,110.00 USD | 0.00 USD | `+20.60%` | `2,641,400.00` |
| `Live` | `Short` | `14.15` | 92,190.00 USD | 37,670.00 USD | 0.00 USD | `+21.46%` | `2,661,900.00` |
| `Live` | `Short` | `14.45` | 93,090.00 USD | 898.79 USD | 0.00 USD | `+24.03%` | `62,200.00` |
| `Live` | `Short` | `14.55` | 96,370.00 USD | 3,280.00 USD | 0.00 USD | `+24.89%` | `225,600.00` |
| `Live` | `Short` | `14.65` | 96,510.00 USD | 139.18 USD | 0.00 USD | `+25.75%` | `9,500.00` |
| `Live` | `Short` | `14.75` | 97,130.00 USD | 615.08 USD | 0.00 USD | `+26.61%` | `41,700.00` |
| `Live` | `Short` | `14.85` | 245,960.00 USD | 148,830.00 USD | 0.00 USD | `+27.47%` | `10,022,200.00` |
| `Live` | `Short` | `14.95` | 246,210.00 USD | 252.65 USD | 0.00 USD | `+28.33%` | `16,900.00` |
| `Live` | `Short` | `15.05` | 311,240.00 USD | 65,030.00 USD | 0.00 USD | `+29.18%` | `4,321,100.00` |
| `Live` | `Short` | `15.35` | 357,620.00 USD | 46,380.00 USD | 0.00 USD | `+31.76%` | `3,021,600.00` |
| `Live` | `Short` | `15.55` | 358,800.00 USD | 1,180.00 USD | 0.00 USD | `+33.48%` | `75,700.00` |
| `Live` | `Short` | `15.65` | 358,980.00 USD | 178.41 USD | 0.00 USD | `+34.33%` | `11,400.00` |
| `Live` | `Short` | `15.75` | 391,590.00 USD | 32,620.00 USD | 0.00 USD | `+35.19%` | `2,070,800.00` |
| `Live` | `Short` | `15.85` | 391,870.00 USD | 271.04 USD | 0.00 USD | `+36.05%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 392,000.00 USD | 138.76 USD | 0.00 USD | `+36.91%` | `8,700.00` |
| `Live` | `Short` | `16.05` | 393,270.00 USD | 1,270.00 USD | 0.00 USD | `+37.77%` | `78,900.00` |
| `Live` | `Short` | `16.15` | 398,260.00 USD | 4,990.00 USD | 0.00 USD | `+38.63%` | `309,000.00` |
| `Live` | `Short` | `16.35` | 398,370.00 USD | 104.64 USD | 0.00 USD | `+40.34%` | `6,400.00` |
| `Live` | `Short` | `16.45` | 423,530.00 USD | 25,170.00 USD | 0.00 USD | `+41.20%` | `1,530,000.00` |
| `Live` | `Short` | `16.85` | 489,640.00 USD | 66,100.00 USD | 0.00 USD | `+44.64%` | `3,923,000.00` |
| `Live` | `Short` | `16.95` | 572,550.00 USD | 82,920.00 USD | 0.00 USD | `+45.49%` | `4,891,900.00` |
| `Live` | `Short` | `17.15` | 580,800.00 USD | 8,240.00 USD | 0.00 USD | `+47.21%` | `480,600.00` |
| `Live` | `Short` | `17.45` | 919,550.00 USD | 338,760.00 USD | 0.00 USD | `+49.79%` | `19,413,000.00` |
| `Live` | `Short` | `17.75` | 921,920.00 USD | 2,370.00 USD | 0.00 USD | `+52.36%` | `133,300.00` |
| `Live` | `Short` | `17.85` | 922,170.00 USD | 249.90 USD | 0.00 USD | `+53.22%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 922,790.00 USD | 621.07 USD | 0.00 USD | `+54.08%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 927,920.00 USD | 5,130.00 USD | 0.00 USD | `+54.94%` | `284,100.00` |
| `Live` | `Short` | `18.15` | 3,020,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+55.79%` | `115,024,600.00` |
| `Live` | `Short` | `18.45` | 3,020,000.00 USD | 3,890.00 USD | 0.00 USD | `+58.37%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 3,020,000.00 USD | 660.38 USD | 0.00 USD | `+59.23%` | `35,600.00` |
| `Live` | `Short` | `18.65` | 3,020,000.00 USD | 186.50 USD | 0.00 USD | `+60.09%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 3,020,000.00 USD | 456.17 USD | 0.00 USD | `+61.80%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 3,040,000.00 USD | 16,250.00 USD | 0.00 USD | `+62.66%` | `857,700.00` |
| `Live` | `Short` | `19.65` | 3,080,000.00 USD | 38,790.00 USD | 0.00 USD | `+68.67%` | `1,974,000.00` |
| `Live` | `Short` | `19.85` | 3,080,000.00 USD | 289.81 USD | 0.00 USD | `+70.39%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,840,000.00 USD | 759,860.00 USD | 0.00 USD | `+72.96%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,840,000.00 USD | 7,250.00 USD | 0.00 USD | `+76.39%` | `353,000.00` |
| `Live` | `Short` | `20.75` | 3,840,000.00 USD | 168.07 USD | 0.00 USD | `+78.11%` | `8,100.00` |
| `Live` | `Short` | `21.15` | 3,850,000.00 USD | 2,220.00 USD | 0.00 USD | `+81.55%` | `105,100.00` |
| `Live` | `Short` | `21.45` | 3,850,000.00 USD | 1,500.00 USD | 0.00 USD | `+84.12%` | `69,800.00` |
| `Live` | `Short` | `21.75` | 3,850,000.00 USD | 2,040.00 USD | 0.00 USD | `+86.70%` | `94,000.00` |
| `Live` | `Short` | `21.95` | 3,850,000.00 USD | 193.16 USD | 0.00 USD | `+88.41%` | `8,800.00` |
| `Live` | `Short` | `22.15` | 4,260,000.00 USD | 411,440.00 USD | 0.00 USD | `+90.13%` | `18,575,000.00` |
| `Live` | `Short` | `22.75` | 4,260,000.00 USD | 910.00 USD | 0.00 USD | `+95.28%` | `40,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 656,410.00 USD | 0.00 USD | 431.68 USD | `-69.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 655,980.00 USD | 0.00 USD | 290.29 USD | `-60.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 655,690.00 USD | 0.00 USD | 120.22 USD | `-54.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 655,570.00 USD | 0.00 USD | 107.09 USD | `-48.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 655,460.00 USD | 0.00 USD | 3,760.00 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 651,700.00 USD | 0.00 USD | 133.00 USD | `-42.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 651,560.00 USD | 0.00 USD | 3,770.00 USD | `-39.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 647,800.00 USD | 0.00 USD | 2,070.00 USD | `-37.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 645,720.00 USD | 0.00 USD | 3,740.00 USD | `-36.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 641,980.00 USD | 0.00 USD | 1,050.00 USD | `-35.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 640,930.00 USD | 0.00 USD | 146.80 USD | `-32.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 640,780.00 USD | 0.00 USD | 5,000.00 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 635,780.00 USD | 0.00 USD | 393.64 USD | `-30.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 635,380.00 USD | 0.00 USD | 10,660.00 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 624,720.00 USD | 0.00 USD | 1,360.00 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 623,360.00 USD | 0.00 USD | 30,250.00 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 593,120.00 USD | 0.00 USD | 186.84 USD | `-25.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 592,930.00 USD | 0.00 USD | 7,600.00 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 585,330.00 USD | 0.00 USD | 180.54 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 585,150.00 USD | 0.00 USD | 1,510.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 583,640.00 USD | 0.00 USD | 2,240.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 581,400.00 USD | 0.00 USD | 4,940.00 USD | `-19.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 576,460.00 USD | 0.00 USD | 9,870.00 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 566,590.00 USD | 0.00 USD | 3,550.00 USD | `-17.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 563,040.00 USD | 0.00 USD | 25,950.00 USD | `-16.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 537,090.00 USD | 0.00 USD | 19,100.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 517,990.00 USD | 0.00 USD | 299,650.00 USD | `-14.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 218,340.00 USD | 0.00 USD | 2,760.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 215,570.00 USD | 0.00 USD | 455.74 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 215,120.00 USD | 0.00 USD | 3,230.00 USD | `-12.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 211,890.00 USD | 0.00 USD | 1,810.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 210,070.00 USD | 0.00 USD | 47,440.00 USD | `-10.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 162,630.00 USD | 0.00 USD | 5,300.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 157,330.00 USD | 0.00 USD | 4,460.00 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 152,870.00 USD | 0.00 USD | 6,170.00 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 146,700.00 USD | 0.00 USD | 3,990.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 142,710.00 USD | 0.00 USD | 6,930.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 135,770.00 USD | 0.00 USD | 15,700.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 120,070.00 USD | 0.00 USD | 24,150.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 95,920.00 USD | 0.00 USD | 45,530.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 50,390.00 USD | 0.00 USD | 10,280.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 40,120.00 USD | 0.00 USD | 14,620.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 25,500.00 USD | 0.00 USD | 25,500.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 315.72 USD | 315.72 USD | 0.00 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 6,350.00 USD | 6,030.00 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 58,780.00 USD | 52,430.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 64,390.00 USD | 5,620.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 112,200.00 USD | 47,800.00 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 146,120.00 USD | 33,920.00 USD | 0.00 USD | `+4.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 156,210.00 USD | 10,080.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 157,390.00 USD | 1,180.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 157,590.00 USD | 206.67 USD | 0.00 USD | `+6.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 157,860.00 USD | 263.55 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 209,160.00 USD | 51,300.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 250,630.00 USD | 41,470.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 271,360.00 USD | 20,730.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 271,820.00 USD | 461.02 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 309,630.00 USD | 37,810.00 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 310,680.00 USD | 1,050.00 USD | 0.00 USD | `+12.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 314,800.00 USD | 4,120.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 319,540.00 USD | 4,730.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 333,930.00 USD | 14,390.00 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 336,560.00 USD | 2,630.00 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 338,580.00 USD | 2,020.00 USD | 0.00 USD | `+17.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 340,650.00 USD | 2,060.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 340,770.00 USD | 120.50 USD | 0.00 USD | `+18.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 341,030.00 USD | 266.44 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 358,140.00 USD | 17,110.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 358,940.00 USD | 798.06 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 365,930.00 USD | 6,990.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 366,150.00 USD | 218.25 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 368,760.00 USD | 2,610.00 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 381,680.00 USD | 12,920.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 382,640.00 USD | 950.82 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 393,860.00 USD | 11,220.00 USD | 0.00 USD | `+29.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 395,690.00 USD | 1,830.00 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 628,730.00 USD | 233,040.00 USD | 0.00 USD | `+30.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 642,230.00 USD | 13,500.00 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 643,120.00 USD | 893.01 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 643,510.00 USD | 388.75 USD | 0.00 USD | `+33.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 669,610.00 USD | 26,100.00 USD | 0.00 USD | `+34.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 671,720.00 USD | 2,110.00 USD | 0.00 USD | `+35.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 677,060.00 USD | 5,340.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 682,370.00 USD | 5,320.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 691,540.00 USD | 9,170.00 USD | 0.00 USD | `+37.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 698,350.00 USD | 6,800.00 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 717,110.00 USD | 18,760.00 USD | 0.00 USD | `+39.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 723,650.00 USD | 6,540.00 USD | 0.00 USD | `+40.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 730,230.00 USD | 6,580.00 USD | 0.00 USD | `+41.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 740,160.00 USD | 9,930.00 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 753,480.00 USD | 13,320.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 767,710.00 USD | 14,240.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 852,070.00 USD | 84,360.00 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 853,770.00 USD | 1,700.00 USD | 0.00 USD | `+45.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 863,270.00 USD | 9,510.00 USD | 0.00 USD | `+46.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 879,960.00 USD | 16,690.00 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 882,210.00 USD | 2,250.00 USD | 0.00 USD | `+48.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 980,550.00 USD | 98,330.00 USD | 0.00 USD | `+48.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,000,000.00 USD | 21,670.00 USD | 0.00 USD | `+49.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,010,000.00 USD | 6,430.00 USD | 0.00 USD | `+50.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,010,000.00 USD | 4,410.00 USD | 0.00 USD | `+51.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,020,000.00 USD | 4,440.00 USD | 0.00 USD | `+52.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,020,000.00 USD | 4,460.00 USD | 0.00 USD | `+53.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,020,000.00 USD | 448.75 USD | 0.00 USD | `+54.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,060,000.00 USD | 35,590.00 USD | 0.00 USD | `+54.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,060,000.00 USD | 453.75 USD | 0.00 USD | `+55.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,060,000.00 USD | 830.38 USD | 0.00 USD | `+56.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,060,000.00 USD | 458.75 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,060,000.00 USD | 461.25 USD | 0.00 USD | `+58.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,060,000.00 USD | 4,540.00 USD | 0.00 USD | `+59.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,070,000.00 USD | 466.25 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,070,000.00 USD | 468.75 USD | 0.00 USD | `+60.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,070,000.00 USD | 471.25 USD | 0.00 USD | `+61.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,070,000.00 USD | 473.75 USD | 0.00 USD | `+62.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,130,000.00 USD | 67,000.00 USD | 0.00 USD | `+63.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,130,000.00 USD | 574.50 USD | 0.00 USD | `+64.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,130,000.00 USD | 577.50 USD | 0.00 USD | `+65.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,140,000.00 USD | 2,710.00 USD | 0.00 USD | `+66.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,140,000.00 USD | 972.50 USD | 0.00 USD | `+66.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,150,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,150,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,150,000.00 USD | 1,690.00 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,150,000.00 USD | 992.50 USD | 0.00 USD | `+70.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,160,000.00 USD | 5,170.00 USD | 0.00 USD | `+71.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,770,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+72.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,770,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,770,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,770,000.00 USD | 1,020.00 USD | 0.00 USD | `+75.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,770,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,780,000.00 USD | 1,030.00 USD | 0.00 USD | `+77.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,780,000.00 USD | 1,860.00 USD | 0.00 USD | `+78.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,780,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,780,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,780,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,790,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,790,000.00 USD | 1,060.00 USD | 0.00 USD | `+82.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,830,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+83.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,830,000.00 USD | 1,070.00 USD | 0.00 USD | `+84.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,840,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,840,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,840,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,840,000.00 USD | 3,280.00 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,840,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,840,000.00 USD | 1,100.00 USD | 0.00 USD | `+89.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,840,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,850,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,850,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,850,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,850,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,850,000.00 USD | 1,130.00 USD | 0.00 USD | `+94.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,850,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,850,000.00 USD | 1,140.00 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,850,000.00 USD | 1,150.00 USD | 0.00 USD | `+97.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,980,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,980,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,990,000.00 USD | 1,160.00 USD | 0.00 USD | `+99.57%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `10.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 35,120.00 USD | 15,990.00 USD | 74,890.00 USD |
| `7D` | `10.22` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 101,890.00 USD | 28,560.00 USD | 86,110.00 USD |
| `7D` | `10.24` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 95,370.00 USD | 20,630.00 USD | 73,760.00 USD |
| `7D` | `10.26` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD |
| `7D` | `10.28` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD |
| `7D` | `10.30` | 18,970,000.00 USD | 0.00 USD | 18,970,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD |
| `7D` | `10.32` | 18,870,000.00 USD | 0.00 USD | 18,870,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `7D` | `10.34` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD |
| `7D` | `10.36` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD |
| `7D` | `10.38` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD |
| `7D` | `10.40` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 46,970.00 USD | 22,340.00 USD | 81,850.00 USD |
| `1D` | `10.42` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 79,170.00 USD | 22,500.00 USD | 45,260.00 USD |
| `7D` | `10.42` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD |
| `1D` | `10.44` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 43,450.00 USD | 12,260.00 USD | 18,150.00 USD |
| `7D` | `10.44` | 18,280,000.00 USD | 0.00 USD | 18,280,000.00 USD | 13,750.00 USD | 6,360.00 USD | 29,560.00 USD |
| `1D` | `10.46` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 19,150.00 USD | 3,120.00 USD | 11,210.00 USD |
| `7D` | `10.46` | 18,230,000.00 USD | 0.00 USD | 18,230,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD |
| `1D` | `10.48` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 12,430.00 USD | 5,860.00 USD | 5,280.00 USD |
| `7D` | `10.48` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `10.50` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 14,440.00 USD | 4,760.00 USD | 8,150.00 USD |
| `7D` | `10.50` | 18,060,000.00 USD | 0.00 USD | 18,060,000.00 USD | 42,030.00 USD | 16,000.00 USD | 12,670.00 USD |
| `1D` | `10.52` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 19,070.00 USD | 1,990.00 USD | 7,560.00 USD |
| `7D` | `10.52` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD |
| `1D` | `10.54` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 8,510.00 USD | 3,720.00 USD | 8,030.00 USD |
| `7D` | `10.54` | 17,950,000.00 USD | 0.00 USD | 17,950,000.00 USD | 25,600.00 USD | 72.80 USD | 12,910.00 USD |
| `1D` | `10.56` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 20,140.00 USD | 6,800.00 USD | 3,030.00 USD |
| `7D` | `10.56` | 17,910,000.00 USD | 0.00 USD | 17,910,000.00 USD | 51,230.00 USD | 16,690.00 USD | 12,830.00 USD |
| `1D` | `10.58` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 20,460.00 USD | 3,900.00 USD | 2,040.00 USD |
| `7D` | `10.58` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 84,220.00 USD | 6,710.00 USD | 11,250.00 USD |
| `1D` | `10.60` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 927.38 USD | 3,630.00 USD | 13.45 USD |
| `7D` | `10.60` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 27,070.00 USD | 8,530.00 USD | 4,300.00 USD |
| `1D` | `10.62` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 18,310.00 USD | 4,690.00 USD | 5,890.00 USD |
| `7D` | `10.62` | 17,680,000.00 USD | 0.00 USD | 17,680,000.00 USD | 16,430.00 USD | 3,400.00 USD | 11,460.00 USD |
| `1D` | `10.64` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 9,170.00 USD | 5,650.00 USD | 14,670.00 USD |
| `7D` | `10.64` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.66` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 17,480.00 USD | 3,100.00 USD | 2,030.00 USD |
| `7D` | `10.66` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.68` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 4,580.00 USD | 1,380.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 17,580,000.00 USD | 0.00 USD | 17,580,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.70` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 8,580.00 USD | 0.00 USD | 10.12 USD |
| `7D` | `10.70` | 17,550,000.00 USD | 0.00 USD | 17,550,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.72` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 48.73 USD | 2,350.00 USD | 12.18 USD |
| `7D` | `10.72` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 21,070.00 USD | 4,880.00 USD | 264.88 USD |
| `1D` | `10.74` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 1,880.00 USD | 2,320.00 USD | 142.88 USD |
| `7D` | `10.74` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 25,580.00 USD | 3,690.00 USD | 315.57 USD |
| `1D` | `10.76` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 1,820.00 USD | 0.00 USD | 150.74 USD |
| `7D` | `10.76` | 17,480,000.00 USD | 0.00 USD | 17,480,000.00 USD | 16,310.00 USD | 144.63 USD | 6,970.00 USD |
| `1D` | `10.78` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 1,070.00 USD | 2,330.00 USD | 2,950.00 USD |
| `7D` | `10.78` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 14,200.00 USD | 36.07 USD | 28,740.00 USD |
| `1D` | `10.80` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 4,760.00 USD | 0.00 USD | 76.87 USD |
| `7D` | `10.80` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 65,420.00 USD | 4,180.00 USD | 70,260.00 USD |
| `1D` | `10.82` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 2,030.00 USD | 0.00 USD | 55.92 USD |
| `7D` | `10.82` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 135,080.00 USD | 28,860.00 USD | 11,330.00 USD |
| `1D` | `10.84` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 2,330.00 USD | 160.15 USD | 45.02 USD |
| `7D` | `10.84` | 17,100,000.00 USD | 0.00 USD | 17,100,000.00 USD | 79,220.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.86` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 976.86 USD | 4,520.00 USD | 3,740.00 USD |
| `7D` | `10.86` | 16,930,000.00 USD | 0.00 USD | 16,930,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 2,870.00 USD | 10,400.00 USD | 16,290.00 USD |
| `7D` | `10.88` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,770.00 USD |
| `1D` | `10.90` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 6,580.00 USD | 3,770.00 USD | 26,480.00 USD |
| `7D` | `10.90` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.92` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 67,690.00 USD | 28,790.00 USD | 58,370.00 USD |
| `7D` | `10.92` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.94` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 47,820.00 USD | 17,110.00 USD | 5,970.00 USD |
| `7D` | `10.94` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.96` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,980.00 USD |
| `7D` | `10.96` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.98` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 24,400.00 USD | 2,590.00 USD | 27,200.00 USD |
| `7D` | `10.98` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 95,370.00 USD | 110,950.00 USD | 161,720.00 USD |
| `1D` | `11.00` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 16,000.00 USD | 7,740.00 USD | 22,210.00 USD |
| `7D` | `11.00` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `1D` | `11.02` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 95,850.00 USD | 30,950.00 USD | 36,250.00 USD |
| `7D` | `11.02` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 296,860.00 USD | 73,760.00 USD | 137,830.00 USD |
| `1D` | `11.04` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 26,860.00 USD | 21,620.00 USD | 39,820.00 USD |
| `7D` | `11.04` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `1D` | `11.06` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 48,320.00 USD | 8,320.00 USD | 38,180.00 USD |
| `7D` | `11.06` | 11,720,000.00 USD | 0.00 USD | 11,720,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.08` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 65,540.00 USD | 39,710.00 USD | 125,470.00 USD |
| `7D` | `11.08` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,620.00 USD |
| `1D` | `11.10` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 146,640.00 USD | 48,060.00 USD | 113,730.00 USD |
| `7D` | `11.10` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 459,710.00 USD | 185,380.00 USD | 547,420.00 USD |
| `1D` | `11.12` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 72,050.00 USD | 45,820.00 USD | 108,400.00 USD |
| `7D` | `11.12` | 9,310,000.00 USD | 0.00 USD | 9,310,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.14` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 184,030.00 USD | 79,200.00 USD | 142,550.00 USD |
| `7D` | `11.14` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,760.00 USD |
| `1D` | `11.16` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 193,330.00 USD | 56,510.00 USD | 88,270.00 USD |
| `7D` | `11.16` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.18` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 117,090.00 USD | 41,100.00 USD | 44,560.00 USD |
| `7D` | `11.18` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 641,660.00 USD | 214,580.00 USD | 541,220.00 USD |
| `1D` | `11.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 190,060.00 USD | 42,000.00 USD | 93,660.00 USD |
| `7D` | `11.20` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 371,240.00 USD | 239,970.00 USD | 129,030.00 USD |
| `1D` | `11.22` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 90,220.00 USD | 30,210.00 USD | 48,370.00 USD |
| `7D` | `11.22` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 203,330.00 USD | 228,180.00 USD | 217,010.00 USD |
| `1D` | `11.24` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 126,690.00 USD | 67,420.00 USD | 76,300.00 USD |
| `7D` | `11.24` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 140,690.00 USD | 69,160.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 206,400.00 USD | 76,800.00 USD | 120,620.00 USD |
| `7D` | `11.26` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 314,550.00 USD | 154,510.00 USD | 81,100.00 USD |
| `1D` | `11.28` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 47,350.00 USD | 18,970.00 USD | 68,860.00 USD |
| `7D` | `11.28` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 240,180.00 USD | 30,780.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 152,430.00 USD | 22,430.00 USD | 23,960.00 USD |
| `7D` | `11.30` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 24,980.00 USD | 41,750.00 USD | 0.00 USD |
| `1D` | `11.32` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 259,460.00 USD | 7,960.00 USD | 16,210.00 USD |
| `7D` | `11.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 54,410.00 USD | 892.25 USD | 69,600.00 USD |
| `1D` | `11.34` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 244,400.00 USD | 33,020.00 USD | 13,100.00 USD |
| `7D` | `11.34` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 320,900.00 USD | 20,470.00 USD | 0.00 USD |
| `1D` | `11.36` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 281,440.00 USD | 90,890.00 USD | 70,810.00 USD |
| `7D` | `11.36` | 927,160.00 USD | 0.00 USD | 927,160.00 USD | 170,150.00 USD | 48,220.00 USD | 45,390.00 USD |
| `1D` | `11.38` | 802,600.00 USD | 0.00 USD | 802,600.00 USD | 22,780.00 USD | 38,670.00 USD | 58,270.00 USD |
| `7D` | `11.38` | 663,400.00 USD | 0.00 USD | 663,400.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 682,870.00 USD | 0.00 USD | 682,870.00 USD | 68,450.00 USD | 12,830.00 USD | 66,820.00 USD |
| `7D` | `11.40` | 572,020.00 USD | 0.00 USD | 572,020.00 USD | 116,360.00 USD | 2,880.00 USD | 16,820.00 USD |
| `1D` | `11.42` | 534,770.00 USD | 0.00 USD | 534,770.00 USD | 58,720.00 USD | 14,250.00 USD | 20,520.00 USD |
| `7D` | `11.42` | 435,960.00 USD | 0.00 USD | 435,960.00 USD | 30,910.00 USD | 0.00 USD | 24,730.00 USD |
| `1D` | `11.44` | 441,290.00 USD | 0.00 USD | 441,290.00 USD | 58,750.00 USD | 20,030.00 USD | 42,870.00 USD |
| `7D` | `11.44` | 380,330.00 USD | 0.00 USD | 380,330.00 USD | 104,540.00 USD | 29,600.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 319,640.00 USD | 0.00 USD | 319,640.00 USD | 66,120.00 USD | 3,810.00 USD | 15,240.00 USD |
| `1D` | `11.48` | 234,480.00 USD | 0.00 USD | 234,480.00 USD | 0.00 USD | 834.95 USD | 0.00 USD |
| `7D` | `11.48` | 208,250.00 USD | 0.00 USD | 208,250.00 USD | 0.00 USD | 364.00 USD | 0.00 USD |
| `1D` | `11.50` | 233,650.00 USD | 0.00 USD | 233,650.00 USD | 63,350.00 USD | 29,480.00 USD | 0.00 USD |
| `7D` | `11.50` | 207,890.00 USD | 0.00 USD | 207,890.00 USD | 40,840.00 USD | 141.10 USD | 0.00 USD |
| `1D` | `11.52` | 140,830.00 USD | 0.00 USD | 140,830.00 USD | 0.00 USD | 23,980.00 USD | 0.00 USD |
| `7D` | `11.52` | 166,910.00 USD | 0.00 USD | 166,910.00 USD | 0.00 USD | 617.33 USD | 0.00 USD |
| `7D` | `11.54` | 166,290.00 USD | 0.00 USD | 166,290.00 USD | 34,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.56` | 116,850.00 USD | 0.00 USD | 116,850.00 USD | 0.00 USD | 0.00 USD | 48,730.00 USD |
| `7D` | `11.56` | 131,520.00 USD | 0.00 USD | 131,520.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD |
| `7D` | `11.58` | 120,890.00 USD | 0.00 USD | 120,890.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 68,110.00 USD | 0.00 USD | 68,110.00 USD | 66,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.64` | 89,270.00 USD | 0.00 USD | 89,270.00 USD | 0.00 USD | 56,880.00 USD | 32,380.00 USD |
| `1D` | `11.66` | 1,220.00 USD | 0.00 USD | 1,220.00 USD | 0.00 USD | 677.25 USD | 0.00 USD |
| `7D` | `11.67` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.68` | 542.34 USD | 0.00 USD | 542.34 USD | 0.00 USD | 542.34 USD | 0.00 USD |
| `7D` | `11.68` | 381.10 USD | 381.10 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.69` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.70` | 156,330.00 USD | 156,330.00 USD | 0.00 USD | 82,770.00 USD | 47,670.00 USD | 25,890.00 USD |
| `1D` | `11.72` | 356,850.00 USD | 356,850.00 USD | 0.00 USD | 131,190.00 USD | 25,910.00 USD | 43,420.00 USD |
| `7D` | `11.72` | 185,060.00 USD | 185,060.00 USD | 0.00 USD | 111,900.00 USD | 23,470.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 410,610.00 USD | 410,610.00 USD | 0.00 USD | 25,420.00 USD | 11,980.00 USD | 16,360.00 USD |
| `7D` | `11.74` | 208,130.00 USD | 208,130.00 USD | 0.00 USD | 0.00 USD | 308.67 USD | 22,770.00 USD |
| `1D` | `11.76` | 675,120.00 USD | 675,120.00 USD | 0.00 USD | 107,680.00 USD | 15,900.00 USD | 140,930.00 USD |
| `7D` | `11.76` | 275,570.00 USD | 275,570.00 USD | 0.00 USD | 48,190.00 USD | 185.70 USD | 19,060.00 USD |
| `1D` | `11.78` | 935,180.00 USD | 935,180.00 USD | 0.00 USD | 16,180.00 USD | 18,030.00 USD | 225,840.00 USD |
| `7D` | `11.78` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 0.00 USD | 6,480.00 USD | 233,490.00 USD |
| `1D` | `11.80` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 103,560.00 USD | 36,200.00 USD | 39,580.00 USD |
| `7D` | `11.80` | 744,880.00 USD | 744,880.00 USD | 0.00 USD | 140,120.00 USD | 33,640.00 USD | 55,590.00 USD |
| `1D` | `11.82` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 209,070.00 USD | 90,430.00 USD | 120,330.00 USD |
| `7D` | `11.82` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 158,640.00 USD | 77,820.00 USD | 91,580.00 USD |
| `1D` | `11.84` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 189,720.00 USD | 56,750.00 USD | 98,300.00 USD |
| `7D` | `11.84` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 300,230.00 USD |
| `1D` | `11.86` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 113,730.00 USD | 43,150.00 USD | 85,090.00 USD |
| `7D` | `11.86` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 607,590.00 USD | 38,220.00 USD | 272,680.00 USD |
| `1D` | `11.88` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 155,380.00 USD | 37,550.00 USD | 49,420.00 USD |
| `7D` | `11.88` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 392,850.00 USD | 20,500.00 USD | 271,780.00 USD |
| `1D` | `11.90` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 82,190.00 USD | 22,830.00 USD | 78,790.00 USD |
| `7D` | `11.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 282,480.00 USD | 31,020.00 USD | 158,670.00 USD |
| `1D` | `11.92` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 92,450.00 USD | 17,780.00 USD | 59,930.00 USD |
| `7D` | `11.92` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 219,990.00 USD | 11,690.00 USD | 271,000.00 USD |
| `1D` | `11.94` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 153,170.00 USD | 55,770.00 USD | 76,330.00 USD |
| `7D` | `11.94` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 368,240.00 USD | 1,890.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 130,630.00 USD | 13,270.00 USD | 13,540.00 USD |
| `7D` | `11.96` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 383,010.00 USD | 13,230.00 USD | 114,620.00 USD |
| `1D` | `11.98` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 91,030.00 USD | 3,430.00 USD | 30,130.00 USD |
| `7D` | `11.98` | 5,780,000.00 USD | 5,780,000.00 USD | 0.00 USD | 391,180.00 USD | 1,420.00 USD | 190,600.00 USD |
| `1D` | `12.00` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 129,420.00 USD | 33,920.00 USD | 128,710.00 USD |
| `7D` | `12.00` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 304,560.00 USD | 19,140.00 USD | 183,590.00 USD |
| `1D` | `12.02` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 169,130.00 USD | 50,620.00 USD | 81,400.00 USD |
| `7D` | `12.02` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 244,440.00 USD | 120,930.00 USD | 170,830.00 USD |
| `1D` | `12.04` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 197,410.00 USD | 69,720.00 USD | 90,480.00 USD |
| `7D` | `12.04` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 292,690.00 USD | 119,510.00 USD | 141,950.00 USD |
| `1D` | `12.06` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 191,800.00 USD | 74,220.00 USD | 142,820.00 USD |
| `7D` | `12.06` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 234,210.00 USD | 101,560.00 USD | 145,690.00 USD |
| `1D` | `12.08` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 135,610.00 USD | 36,290.00 USD | 46,610.00 USD |
| `7D` | `12.08` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 142,390.00 USD |
| `1D` | `12.10` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 19,390.00 USD | 6,920.00 USD | 24,570.00 USD |
| `7D` | `12.10` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 76,860.00 USD | 25,560.00 USD | 22,650.00 USD |
| `7D` | `12.12` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 89,810.00 USD | 44,490.00 USD | 95,850.00 USD |
| `1D` | `12.14` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 66,230.00 USD | 10,120.00 USD | 25,830.00 USD |
| `7D` | `12.14` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 118,920.00 USD | 64,740.00 USD | 31,180.00 USD |
| `1D` | `12.16` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 59,700.00 USD | 33,220.00 USD | 18,940.00 USD |
| `7D` | `12.16` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 95,440.00 USD | 84,750.00 USD | 72,030.00 USD |
| `1D` | `12.18` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 29,420.00 USD | 19,650.00 USD | 20,030.00 USD |
| `7D` | `12.18` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 57,680.00 USD | 11,390.00 USD | 32,160.00 USD |
| `1D` | `12.20` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 56,330.00 USD | 19,400.00 USD | 12,810.00 USD |
| `7D` | `12.20` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 160,030.00 USD | 51,550.00 USD | 59,580.00 USD |
| `1D` | `12.22` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 22,910.00 USD | 26,360.00 USD | 29,440.00 USD |
| `7D` | `12.22` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 261,490.00 USD | 19,920.00 USD | 93,540.00 USD |
| `1D` | `12.24` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 36,100.00 USD | 5,930.00 USD | 180.05 USD |
| `7D` | `12.24` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 70,650.00 USD | 70,410.00 USD | 114,820.00 USD |
| `1D` | `12.26` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 51,100.00 USD | 18,930.00 USD | 9,320.00 USD |
| `7D` | `12.26` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 202,660.00 USD | 33,500.00 USD | 24,840.00 USD |
| `1D` | `12.28` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 62,640.00 USD | 17,310.00 USD | 25,640.00 USD |
| `7D` | `12.28` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 238,210.00 USD | 76,160.00 USD | 151,670.00 USD |
| `1D` | `12.30` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 53,480.00 USD | 19,840.00 USD | 31,150.00 USD |
| `7D` | `12.30` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 178,010.00 USD | 79,440.00 USD | 85,330.00 USD |
| `1D` | `12.32` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 391.20 USD | 927.78 USD | 103.98 USD |
| `7D` | `12.32` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 120,640.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.34` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 14,920.00 USD | 3,460.00 USD | 8,330.00 USD |
| `7D` | `12.34` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 140,600.00 USD | 75,950.00 USD | 13,370.00 USD |
| `1D` | `12.36` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 11,940.00 USD | 3,340.00 USD | 2,360.00 USD |
| `7D` | `12.36` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 78,410.00 USD | 24,900.00 USD | 6,470.00 USD |
| `1D` | `12.38` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD | 29.00 USD |
| `7D` | `12.38` | 12,070,000.00 USD | 12,070,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 135,450.00 USD |
| `1D` | `12.40` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 3,400.00 USD | 11,690.00 USD | 44.48 USD |
| `7D` | `12.40` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 176,820.00 USD | 40,380.00 USD | 258,110.00 USD |
| `1D` | `12.42` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 359.83 USD | 0.00 USD | 20.34 USD |
| `7D` | `12.42` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 135,510.00 USD | 33,450.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 2,060.00 USD | 29.65 USD | 360.98 USD |
| `7D` | `12.44` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 159,890.00 USD | 70,960.00 USD | 272,130.00 USD |
| `1D` | `12.46` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 4,980.00 USD | 8,910.00 USD | 11,600.00 USD |
| `7D` | `12.46` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 84,310.00 USD | 68,250.00 USD | 98,800.00 USD |
| `1D` | `12.48` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 8,220.00 USD |
| `7D` | `12.48` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 31,320.00 USD | 27,230.00 USD | 180,400.00 USD |
| `1D` | `12.50` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 1,320.00 USD | 4,320.00 USD | 8,220.00 USD |
| `7D` | `12.50` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 153,810.00 USD | 20,380.00 USD | 74,770.00 USD |
| `1D` | `12.52` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 20,270.00 USD | 5,020.00 USD | 12,150.00 USD |
| `7D` | `12.52` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 165,890.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.54` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 14,590.00 USD | 2,830.00 USD | 92.11 USD |
| `7D` | `12.54` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 96,800.00 USD | 59,960.00 USD | 107,190.00 USD |
| `1D` | `12.56` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,910.00 USD |
| `7D` | `12.56` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 126,580.00 USD | 30,820.00 USD | 27,310.00 USD |
| `1D` | `12.58` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 4,160.00 USD | 1,030.00 USD | 10,890.00 USD |
| `7D` | `12.58` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 97,670.00 USD | 66,210.00 USD | 41,430.00 USD |
| `1D` | `12.60` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 3,410.00 USD | 1,310.00 USD | 1,090.00 USD |
| `7D` | `12.60` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 52,910.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.62` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 12,890.00 USD | 9,540.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.64` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 24,070.00 USD | 10,540.00 USD | 15,180.00 USD |
| `7D` | `12.64` | 15,840,000.00 USD | 15,840,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.66` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 845.26 USD | 888.70 USD | 7,210.00 USD |
| `7D` | `12.66` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 43,740.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.68` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 15,690.00 USD | 5,120.00 USD | 27,310.00 USD |
| `7D` | `12.68` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,980.00 USD |
| `1D` | `12.70` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 5,910.00 USD | 5,550.00 USD | 22,870.00 USD |
| `7D` | `12.70` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 22,340.00 USD | 50,120.00 USD | 142,760.00 USD |
| `1D` | `12.72` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 52,250.00 USD | 9,620.00 USD | 29,920.00 USD |
| `7D` | `12.72` | 16,690,000.00 USD | 16,690,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,140.00 USD |
| `1D` | `12.74` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 26,930.00 USD | 12,730.00 USD | 15,310.00 USD |
| `7D` | `12.74` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 21,020.00 USD |
| `1D` | `12.76` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 43,450.00 USD | 12,260.00 USD | 18,150.00 USD |
| `7D` | `12.76` | 16,820,000.00 USD | 16,820,000.00 USD | 0.00 USD | 15,760.00 USD | 6,360.00 USD | 29,680.00 USD |
| `1D` | `12.78` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 19,150.00 USD | 3,120.00 USD | 11,210.00 USD |
| `7D` | `12.78` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 78,020.00 USD | 15,750.00 USD | 18,730.00 USD |
| `1D` | `12.80` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 12,430.00 USD | 5,860.00 USD | 5,280.00 USD |
| `7D` | `12.80` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.82` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 84.60 USD | 1,230.00 USD | 1,960.00 USD |
| `7D` | `12.82` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.84` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 14,360.00 USD | 3,530.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 17,060,000.00 USD | 17,060,000.00 USD | 0.00 USD | 29,710.00 USD | 15,870.00 USD | 7,710.00 USD |
| `1D` | `12.86` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 19,070.00 USD | 1,990.00 USD | 7,560.00 USD |
| `7D` | `12.86` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD |
| `1D` | `12.88` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 7,490.00 USD | 3,610.00 USD | 8,010.00 USD |
| `7D` | `12.88` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 24,580.00 USD | 72.80 USD | 12,750.00 USD |
| `7D` | `12.90` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 41,140.00 USD | 16,610.00 USD | 13,080.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `556.59M` | Total OI Tokens: `47,765,003.0 LINK`
  * 1h OI Change: `+0.23%` | 4h OI Change: `+1.81%` | 24h OI Change: `-0.76%`
  * Exchange Breakdown: Binance=`106.18M` | Bybit=`65.91M` | OKX=`26.47M` | Hyperliquid=`56.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `18.66K` | Last 24h: `39.23K` | Last 3d: `101.03K` | Last 7d: `149.67K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0097%` | **USDT Bitget** | `0.0086%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `48.56%` | `51.44%` | `0.94` | 3,950,000.00 USD |
| `15M` | `Binance` | `52.11%` | `47.89%` | `1.09` | 1,680,000.00 USD |
| `15M` | `OKX` | `50.1%` | `49.9%` | `1.00` | 382,590.00 USD |
| `15M` | `Bybit` | `45.18%` | `54.82%` | `0.82` | 204,750.00 USD |
| `15M` | `KuCoin` | `43.59%` | `56.41%` | `0.77` | 35,150.00 USD |
| `15M` | `Gate` | `38.76%` | `61.24%` | `0.63` | 163,750.00 USD |
| `15M` | `Bitget` | `32.57%` | `67.43%` | `0.48` | 163,830.00 USD |
| `15M` | `BingX` | `61.43%` | `38.57%` | `1.59` | 143,000.00 USD |
| `15M` | `MEXC` | `41.27%` | `58.73%` | `0.70` | 124,200.00 USD |
| `15M` | `Bitunix` | `48.47%` | `51.53%` | `0.94` | 75,250.00 USD |
| `15M` | `Hyperliquid` | `28.38%` | `71.62%` | `0.40` | 16,820.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.9%` | `46.1%` | `1.17` | 794,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 132,490.00 USD |
| `15M` | `HTX` | `51.94%` | `48.06%` | `1.08` | 9,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `55.22%` | `44.78%` | `1.23` | 20,040.00 USD |
| `15M` | `Aster` | `52.46%` | `47.54%` | `1.10` | 649.43 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `37.37%` | `62.63%` | `0.60` | 2,460.00 USD |
| `15M` | `Whale Positions` | `52.11%` | `47.89%` | `1.09` | 1,680,000.00 USD |
| `15M` | `Global Accounts` | `48.56%` | `51.44%` | `0.94` | 3,950,000.00 USD |
| `1H` | `LINK` | `50.69%` | `49.31%` | `1.03` | 54,520,000.00 USD |
| `1H` | `Binance` | `52.14%` | `47.86%` | `1.09` | 19,300,000.00 USD |
| `1H` | `OKX` | `45.72%` | `54.28%` | `0.84` | 9,670,000.00 USD |
| `1H` | `Bybit` | `54.72%` | `45.28%` | `1.21` | 2,290,000.00 USD |
| `1H` | `KuCoin` | `22.03%` | `77.97%` | `0.28` | 767,440.00 USD |
| `1H` | `Gate` | `49.99%` | `50.01%` | `1.00` | 9,640,000.00 USD |
| `1H` | `Bitget` | `53.91%` | `46.09%` | `1.17` | 1,870,000.00 USD |
| `1H` | `BingX` | `44.61%` | `55.39%` | `0.81` | 727,270.00 USD |
| `1H` | `MEXC` | `48.84%` | `51.16%` | `0.95` | 4,480,000.00 USD |
| `1H` | `Bitunix` | `57.48%` | `42.52%` | `1.35` | 2,040,000.00 USD |
| `1H` | `Hyperliquid` | `14.7%` | `85.3%` | `0.17` | 470,900.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.49%` | `45.51%` | `1.20` | 335,030.00 USD |
| `1H` | `Crypto.com` | `49.65%` | `50.35%` | `0.99` | 50,680.00 USD |
| `1H` | `WhiteBIT` | `76.88%` | `23.12%` | `3.33` | 1,720,000.00 USD |
| `1H` | `HTX` | `34.86%` | `65.14%` | `0.54` | 266,030.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.09%` | `53.91%` | `0.85` | 250,250.00 USD |
| `1H` | `Aster` | `63.72%` | `36.28%` | `1.76` | 664,810.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.86%` | `31.14%` | `2.21` | 5,710.00 USD |
| `1H` | `Whale Positions` | `52.14%` | `47.86%` | `1.09` | 19,300,000.00 USD |
| `1H` | `Global Accounts` | `50.69%` | `49.31%` | `1.03` | 54,520,000.00 USD |
| `4H` | `LINK` | `48.28%` | `51.72%` | `0.93` | 88,690,000.00 USD |
| `4H` | `Binance` | `50.39%` | `49.61%` | `1.02` | 31,290,000.00 USD |
| `4H` | `OKX` | `54.19%` | `45.81%` | `1.18` | 7,660,000.00 USD |
| `4H` | `Bybit` | `52.54%` | `47.46%` | `1.11` | 7,480,000.00 USD |
| `4H` | `KuCoin` | `39.42%` | `60.58%` | `0.65` | 664,120.00 USD |
| `4H` | `Gate` | `45.09%` | `54.91%` | `0.82` | 4,280,000.00 USD |
| `4H` | `Bitget` | `48.81%` | `51.19%` | `0.95` | 4,490,000.00 USD |
| `4H` | `BingX` | `32.08%` | `67.92%` | `0.47` | 4,970,000.00 USD |
| `4H` | `MEXC` | `51.6%` | `48.4%` | `1.07` | 6,470,000.00 USD |
| `4H` | `Bitunix` | `50.14%` | `49.86%` | `1.01` | 2,230,000.00 USD |
| `4H` | `Hyperliquid` | `65.07%` | `34.93%` | `1.86` | 481,150.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.24%` | `47.76%` | `1.09` | 14,970,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `0.85%` | `99.15%` | `0.01` | 2,890,000.00 USD |
| `4H` | `HTX` | `45.8%` | `54.2%` | `0.85` | 370,620.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.12%` | `52.88%` | `0.89` | 444,000.00 USD |
| `4H` | `Aster` | `65.39%` | `34.61%` | `1.89` | 9,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `63.03%` | `36.97%` | `1.70` | 20,120.00 USD |
| `4H` | `Whale Positions` | `50.39%` | `49.61%` | `1.02` | 31,290,000.00 USD |
| `4H` | `Global Accounts` | `48.28%` | `51.72%` | `0.93` | 88,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.61` | `11.62` | `11.61` | `11.64` | `11.60` | 1,343,341.40 USD | 918,798.02 USD | 424,543.38 USD | 494,254.64 USD | `+36.79%` | `16B / 2S` |
| `0:00 UTC` | `11.57` | `11.60` | `11.57` | `11.65` | `11.56` | 1,580,207.85 USD | 669,053.47 USD | 911,154.38 USD | -242,100.91 USD | `-15.32%` | `20B / 30S` |
| `5:00 UTC` | `11.58` | `11.60` | `11.58` | `11.63` | `11.58` | 1,099,120.73 USD | 704,449.96 USD | 394,670.77 USD | 309,779.19 USD | `+28.18%` | `12B / 8S` |
| `0:00 UTC` | `11.64` | `11.63` | `11.64` | `11.66` | `11.59` | 1,673,558.77 USD | 971,773.96 USD | 701,784.82 USD | 269,989.14 USD | `+16.13%` | `15B / 5S` |
| `5:00 UTC` | `11.64` | `11.62` | `11.64` | `11.65` | `11.61` | 856,800.01 USD | 412,856.03 USD | 443,943.98 USD | -31,087.96 USD | `-3.63%` | `5B / 13S` |
| `0:00 UTC` | `11.68` | `11.66` | `11.68` | `11.69` | `11.63` | 1,476,075.54 USD | 585,647.20 USD | 890,428.34 USD | -304,781.14 USD | `-20.65%` | `5B / 9S` |
| `5:00 UTC` | `11.67` | `11.67` | `11.67` | `11.70` | `11.65` | 1,710,411.82 USD | 917,052.89 USD | 793,358.93 USD | 123,693.95 USD | `+7.23%` | `6B / 7S` |
| `0:00 UTC` | `11.59` | `11.62` | `11.59` | `11.69` | `11.57` | 2,167,857.89 USD | 905,701.30 USD | 1,262,156.60 USD | -356,455.30 USD | `-16.44%` | `11B / 32S` |
| `5:00 UTC` | `11.61` | `11.62` | `11.61` | `11.68` | `11.57` | 1,501,963.10 USD | 797,959.25 USD | 704,003.85 USD | 93,955.40 USD | `+6.26%` | `26B / 12S` |
| `0:00 UTC` | `11.66` | `11.65` | `11.66` | `11.68` | `11.63` | 895,782.28 USD | 489,905.36 USD | 405,876.92 USD | 84,028.43 USD | `+9.38%` | `13B / 4S` |

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
| `5m` | 37,890.00 USD | 43,700.00 USD | **`ACCUMULATION`** |
| `15m` | 31,610.00 USD | 211,230.00 USD | **`ACCUMULATION`** |
| `30m` | -181,760.00 USD | 203,600.00 USD | **`ACCUMULATION`** |
| `1h` | -34,810.00 USD | 116,520.00 USD | **`ACCUMULATION`** |
| `2h` | -79,300.00 USD | 221,280.00 USD | **`ACCUMULATION`** |
| `4h` | 98,520.00 USD | 165,370.00 USD | **`ACCUMULATION`** |
| `6h` | -199,420.00 USD | 447,770.00 USD | **`ACCUMULATION`** |
| `8h` | -37,800.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `12h` | 484,090.00 USD | 64,190.00 USD | **`ACCUMULATION`** |
| `24h` | -466.90 USD | -2,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -10,170,000.00 USD | -29,150,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -75,600,000.00 USD | -191,940,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+37.89K` | 15m=`+31.61K` | 1h=`-34.81K` | 24h=`-466.90`
* Futures Capital Netflows: 5m=`+43.70K` | 15m=`+211.23K` | 1h=`+116.52K` | 24h=`-2.37M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `11.09` (Risk Distance: `0.2032` pts)
  * +2.5R Take Profit: `11.80`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.81` (Risk Distance: `0.2032` pts)
  * +2.5R Take Profit: `11.10`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.76`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
