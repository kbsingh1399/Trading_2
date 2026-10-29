# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 00:38:22 IST` (`2026-10-29 19:08:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.60` | **Live Ask Quote**: `11.69` | **Mid Price**: `11.64`
- **Spread Points**: `87.00` | **Spread BPS**: `74.71 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.57` | VWAP Z-Score: `+0.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0745` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.76` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.11` | Lower -3.00σ Band: `11.02`
  * Upper +2.51σ Band: `12.02` | Lower -2.51σ Band: `11.11`
  * Upper +2.01σ Band: `11.93` | Lower -2.01σ Band: `11.20`
  * Upper +2.00σ Band: `11.93` | Lower -2.00σ Band: `11.20`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.33`
  * Upper +1.00σ Band: `11.75` | Lower -1.00σ Band: `11.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.68` | EMA-20=`11.70` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.64` (Slope: `+0.0000`) | EMA-100=`11.59`
  * Institutional Anchors: EMA-144=`11.57` | EMA-200=`11.54` (Slope: `+0.2170`) | EMA-233=`11.51`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`11.23` | Weekly High=`11.96` | Weekly Low=`11.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.91` (Distance: `-2.23%`)
  * Point of Control (POC) = `11.77` (Distance: `-1.11%`)
  * Value Area Low (VAL) = `11.44` (Distance: `+1.75%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `11.60` - `11.69`
  * Optimal Trade Entry (OTE 0.705): `11.67`
  * Structural Invalidation Anchor (0.786): `11.74`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.66` | `11.71` | `11.66` | `11.69` | `63,779` | 745,802.25 USD | 539,439.84 USD | `+72.33%` | 58,468.43 USD | `+3.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `11.69` | `11.71` | `11.68` | `11.68` | `14,562` | 170,340.48 USD | 46,535.86 USD | `+27.32%` | 105,004.29 USD | `+0.17` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.68` | `11.69` | `11.64` | `11.65` | `19,206` | 223,833.68 USD | 12,026.48 USD | `+5.37%` | 117,030.77 USD | `-0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.70` | `11.71` | `11.62` | `11.65` | `207,793` | 2,420,411.57 USD | -212,180.19 USD | `-8.77%` | -579,906.53 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `11.65` | `11.71` | `11.64` | `11.68` | `100,997` | 1,180,195.23 USD | 690,200.05 USD | `+58.48%` | 110,293.52 USD | `+1.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.68` | `11.69` | `11.64` | `11.65` | `19,206` | 223,833.68 USD | 12,026.48 USD | `+5.37%` | 122,320.01 USD | `-0.05` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.86` | `11.87` | `11.66` | `11.74` | `476,252` | 5,603,289.28 USD | -228,969.33 USD | `-4.09%` | -626,109.15 USD | `-0.20` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.68` | `461,460` | 5,390,854.94 USD | 388,230.26 USD | `+7.20%` | -237,878.89 USD | `+0.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.69` | `11.64` | `11.65` | `19,231` | 224,118.55 USD | 12,311.35 USD | `+5.49%` | -225,567.54 USD | `+0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.65` | `1,769,802` | 20,898,094.07 USD | -772,035.52 USD | `-3.69%` | -225,852.41 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.81` | `11.84` | `11.28` | `11.39` | `2,525,579` | 29,055,853.55 USD | -2,350,212.00 USD | `-8.09%` | -1,114,916.46 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -1,079,102.33 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -785,720.71 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 546,183.12 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.65` | `1,769,802` | 20,898,094.07 USD | -772,035.52 USD | `-3.69%` | -225,852.41 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`11.64`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `492` | `0x73ce...8ce9` | `LONG` | 4,664,535.27 USD | `400,011,600.00` | `12.05` | `11.65` | `9.13` | -155,218.44 USD | `-3.33%` | `5X Cross` |
| `641` | `0x5b5d...c060` | `SHORT` | 3,634,950.32 USD | `311,728,200.00` | `13.61` | `11.65` | `494.76` | 607,181.79 USD | `+16.70%` | `3X Cross` |
| `651` | `0xb83d...6e36` | `SHORT` | 3,593,360.47 USD | `308,152,000.00` | `12.93` | `11.65` | `421.89` | 391,893.02 USD | `+10.91%` | `3X Cross` |
| `866` | `0x458d...ab3b` | `LONG` | 2,648,647.12 USD | `227,156,700.00` | `13.13` | `11.65` | `9.34` | -333,583.27 USD | `-12.59%` | `3X Isolated` |
| `950` | `0xdd53...2b13` | `SHORT` | 2,406,882.57 USD | `206,475,300.00` | `11.92` | `11.65` | `274.79` | 54,340.36 USD | `+2.26%` | `3X Cross` |
| `983` | `0x3dc9...54b0` | `SHORT` | 2,332,000.00 USD | `200,000,000.00` | `7.56` | `11.65` | `81.68` | -820,841.58 USD | `-35.20%` | `10X Cross` |
| `1003` | `0x45d2...4029` | `SHORT` | 2,278,552.50 USD | `195,500,000.00` | `11.54` | `11.65` | `192.55` | -22,069.07 USD | `-0.97%` | `10X Cross` |
| `1202` | `0x6540...f7b7` | `LONG` | 1,909,141.49 USD | `163,776,400.00` | `12.48` | `11.65` | `8.01` | -134,248.79 USD | `-7.03%` | `5X Isolated` |
| `1255` | `0xeadc...9d55` | `LONG` | 1,838,784.98 USD | `157,691,600.00` | `9.43` | `11.65` | `0.000000` | 352,130.08 USD | `+19.15%` | `10X Cross` |
| `1610` | `0x9df2...c665` | `SHORT` | 1,374,897.20 USD | `117,905,600.00` | `11.48` | `11.65` | `252.32` | -20,878.92 USD | `-1.52%` | `10X Cross` |
| `1635` | `0xf6f3...47f8` | `SHORT` | 1,341,186.84 USD | `115,024,600.00` | `11.42` | `11.65` | `18.78` | -27,856.65 USD | `-2.08%` | `5X Cross` |
| `1795` | `0xfe7e...11b4` | `LONG` | 1,179,315.72 USD | `101,142,000.00` | `14.47` | `11.65` | `5.33` | -283,797.43 USD | `-24.06%` | `5X Isolated` |
| `1828` | `0x8af7...fa05` | `SHORT` | 1,150,093.61 USD | `98,661,200.00` | `14.08` | `11.65` | `203.96` | 239,088.93 USD | `+20.79%` | `10X Cross` |
| `1882` | `0xb7ec...5166` | `LONG` | 1,102,149.91 USD | `94,515,900.00` | `9.01` | `11.65` | `7.20` | 250,289.33 USD | `+22.71%` | `4X Cross` |

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
  * 24H Horizon: Short MP=`12.05` (Vol: 117,000.00 USD, Dist: `+3.17%`) | Long MP=`11.18` (Vol: 185,200.00 USD, Dist: `--4.25%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+3.17%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--3.42%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.62%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--4.51%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+4.64%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--4.48%`)
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
| `1D` | `Long Liquidation` | `10.46` | 6,470,000.00 USD | 6,470,000.00 USD | 27,560.00 USD | 8,350.00 USD | 22,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 19,170,000.00 USD | 19,170,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 6,410,000.00 USD | 6,410,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 19,060,000.00 USD | 19,060,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 6,380,000.00 USD | 6,380,000.00 USD | 23,730.00 USD | 7,140.00 USD | 8,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 19,000,000.00 USD | 19,000,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 6,340,000.00 USD | 6,340,000.00 USD | 23,530.00 USD | 3,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 18,930,000.00 USD | 18,930,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 6,310,000.00 USD | 6,310,000.00 USD | 4,350.00 USD | 3,800.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 18,890,000.00 USD | 18,890,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,960.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 6,290,000.00 USD | 6,290,000.00 USD | 22,600.00 USD | 9,260.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 18,840,000.00 USD | 18,840,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 6,250,000.00 USD | 6,250,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 18,750,000.00 USD | 18,750,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 6,220,000.00 USD | 6,220,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 18,640,000.00 USD | 18,640,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 6,210,000.00 USD | 6,210,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 18,590,000.00 USD | 18,590,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 6,160,000.00 USD | 6,160,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 18,550,000.00 USD | 18,550,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 6,120,000.00 USD | 6,120,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 18,500,000.00 USD | 18,500,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 6,090,000.00 USD | 6,090,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 18,470,000.00 USD | 18,470,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 6,080,000.00 USD | 6,080,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 18,450,000.00 USD | 18,450,000.00 USD | 14,670.00 USD | 0.00 USD | 188.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 6,070,000.00 USD | 6,070,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 18,430,000.00 USD | 18,430,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 6,050,000.00 USD | 6,050,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 18,390,000.00 USD | 18,390,000.00 USD | 20,210.00 USD | 4,010.00 USD | 318.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 6,020,000.00 USD | 6,020,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 18,360,000.00 USD | 18,360,000.00 USD | 16,310.00 USD | 0.00 USD | 294.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 6,000,000.00 USD | 6,000,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 18,350,000.00 USD | 18,350,000.00 USD | 14,200.00 USD | 4,000.00 USD | 23,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 5,990,000.00 USD | 5,990,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 18,300,000.00 USD | 18,300,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 5,990,000.00 USD | 5,990,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 18,170,000.00 USD | 18,170,000.00 USD | 135,080.00 USD | 28,860.00 USD | 10,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 5,990,000.00 USD | 5,990,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,990,000.00 USD | 17,990,000.00 USD | 79,220.00 USD | 38,860.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 79,970.00 USD | 797,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 5,980,000.00 USD | 5,980,000.00 USD | 976.86 USD | 4,520.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 17,830,000.00 USD | 17,830,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 5,970,000.00 USD | 5,970,000.00 USD | 1,740.00 USD | 10,400.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 17,470,000.00 USD | 17,470,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 5,950,000.00 USD | 5,950,000.00 USD | 3,610.00 USD | 3,770.00 USD | 26,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 17,010,000.00 USD | 17,010,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 5,910,000.00 USD | 5,910,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 16,580,000.00 USD | 16,580,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 5,760,000.00 USD | 5,760,000.00 USD | 47,590.00 USD | 17,110.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 15,670,000.00 USD | 15,670,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,090.00 USD | 717,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 5,690,000.00 USD | 5,690,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 15,080,000.00 USD | 15,080,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 5,540,000.00 USD | 5,540,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 14,530,000.00 USD | 14,530,000.00 USD | 96,870.00 USD | 110,950.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 5,480,000.00 USD | 5,480,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 14,160,000.00 USD | 14,160,000.00 USD | 134,000.00 USD | 91,410.00 USD | 160,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 5,440,000.00 USD | 5,440,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 13,770,000.00 USD | 13,770,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 5,280,000.00 USD | 5,280,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 13,260,000.00 USD | 13,260,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 27,780.00 USD | 159,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 5,250,000.00 USD | 5,250,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 12,600,000.00 USD | 12,600,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 5,210,000.00 USD | 5,210,000.00 USD | 28,790.00 USD | 15,060.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 12,200,000.00 USD | 12,200,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 5,140,000.00 USD | 5,140,000.00 USD | 34,720.00 USD | 30,270.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 11,390,000.00 USD | 11,390,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 5,040,000.00 USD | 5,040,000.00 USD | 54,370.00 USD | 33,090.00 USD | 75,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 10,190,000.00 USD | 10,190,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 4,880,000.00 USD | 4,880,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 9,150,000.00 USD | 9,150,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 48,310.00 USD | 131,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 4,490,000.00 USD | 4,490,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 7,670,000.00 USD | 7,670,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 4,200,000.00 USD | 4,200,000.00 USD | 137,180.00 USD | 43,130.00 USD | 55,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 6,360,000.00 USD | 6,360,000.00 USD | 659,190.00 USD | 214,580.00 USD | 541,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 3,960,000.00 USD | 3,960,000.00 USD | 222,000.00 USD | 47,730.00 USD | 92,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,950,000.00 USD | 4,950,000.00 USD | 371,240.00 USD | 240,290.00 USD | 128,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 3,600,000.00 USD | 3,600,000.00 USD | 103,870.00 USD | 34,010.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 4,210,000.00 USD | 4,210,000.00 USD | 208,020.00 USD | 228,180.00 USD | 217,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 3,410,000.00 USD | 3,410,000.00 USD | 116,260.00 USD | 69,400.00 USD | 90,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 3,560,000.00 USD | 3,560,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 72,340.00 USD | 83,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.26` | 3,140,000.00 USD | 3,140,000.00 USD | 189,850.00 USD | 53,910.00 USD | 63,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 3,260,000.00 USD | 3,260,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.28` | 2,830,000.00 USD | 2,830,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 2,690,000.00 USD | 2,690,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.30` | 2,700,000.00 USD | 2,700,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 2,280,000.00 USD | 2,280,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.32` | 2,570,000.00 USD | 2,570,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 2,210,000.00 USD | 2,210,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.34` | 2,450,000.00 USD | 2,450,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 2,040,000.00 USD | 2,040,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 10,910.00 USD | 10,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.36` | 2,180,000.00 USD | 2,180,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 1,680,000.00 USD | 1,680,000.00 USD | 170,150.00 USD | 48,220.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.38` | 1,780,000.00 USD | 1,780,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 1,400,000.00 USD | 1,400,000.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.40` | 1,660,000.00 USD | 1,660,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 1,310,000.00 USD | 1,310,000.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.42` | 1,460,000.00 USD | 1,460,000.00 USD | 106,690.00 USD | 34,500.00 USD | 53,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 1,120,000.00 USD | 1,120,000.00 USD | 61,980.00 USD | 0.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.44` | 1,270,000.00 USD | 1,270,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 1,000,000.00 USD | 1,000,000.00 USD | 148,600.00 USD | 44,370.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.46` | 1,020,000.00 USD | 1,020,000.00 USD | 177,600.00 USD | 30,500.00 USD | 24,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.46` | 769,190.00 USD | 769,190.00 USD | 0.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.48` | 789,010.00 USD | 789,010.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 759,150.00 USD | 759,150.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.50` | 711,660.00 USD | 711,660.00 USD | 74,140.00 USD | 61,630.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 718,720.00 USD | 718,720.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.52` | 561,580.00 USD | 561,580.00 USD | 13,090.00 USD | 34,130.00 USD | 46,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.52` | 630,580.00 USD | 630,580.00 USD | 0.00 USD | 37,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.54` | 468,030.00 USD | 468,030.00 USD | 0.00 USD | 7,330.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.54` | 593,050.00 USD | 593,050.00 USD | 34,770.00 USD | 27,190.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.56` | 445,430.00 USD | 445,430.00 USD | 53,760.00 USD | 16,480.00 USD | 88,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.56` | 479,570.00 USD | 479,570.00 USD | 0.00 USD | 28,460.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.58` | 286,470.00 USD | 286,470.00 USD | 45,400.00 USD | 18,680.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.58` | 413,220.00 USD | 413,220.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.60` | 204,830.00 USD | 204,830.00 USD | 78,360.00 USD | 9,700.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.60` | 381,600.00 USD | 381,600.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.62` | 97,440.00 USD | 97,440.00 USD | 0.00 USD | 7,350.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.64` | 358,820.00 USD | 358,820.00 USD | 68,740.00 USD | 79,630.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.66` | 83,510.00 USD | 83,510.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.66` | 154,750.00 USD | 154,750.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.68` | 45,920.00 USD | 45,920.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.68` | 92,780.00 USD | 92,780.00 USD | 88,140.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 230.72 USD | 230.72 USD | 0.00 USD | 230.72 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 177,650.00 USD | 177,650.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 195,940.00 USD | 195,940.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 177,970.00 USD | 177,970.00 USD | 0.00 USD | 324.58 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 178,310.00 USD | 178,310.00 USD | 0.00 USD | 342.56 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 244,130.00 USD | 244,130.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 195,350.00 USD | 195,350.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 196,410.00 USD | 196,410.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 384,250.00 USD | 384,250.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 545,000.00 USD | 545,000.00 USD | 158,640.00 USD | 1,970.00 USD | 133.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 280,320.00 USD | 280,320.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 764,330.00 USD | 764,330.00 USD | 178,690.00 USD | 40,640.00 USD | 10.32 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 2,390.00 USD | 2,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 352,480.00 USD | 352,480.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 770,990.00 USD | 770,990.00 USD | 0.00 USD | 6,610.00 USD | 42.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 408,420.00 USD | 408,420.00 USD | 19,640.00 USD | 15,360.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 783,970.00 USD | 783,970.00 USD | 10,340.00 USD | 2,480.00 USD | 165.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 452,640.00 USD | 452,640.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 795,940.00 USD | 795,940.00 USD | 11,220.00 USD | 612.37 USD | 145.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 525,610.00 USD | 525,610.00 USD | 59,860.00 USD | 13,090.00 USD | 20.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 803,120.00 USD | 803,120.00 USD | 7,000.00 USD | 0.00 USD | 169.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 571,190.00 USD | 571,190.00 USD | 1,220.00 USD | 15,870.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 993,220.00 USD | 993,220.00 USD | 17,060.00 USD | 24,600.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 637,940.00 USD | 637,940.00 USD | 12,210.00 USD | 26,690.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 1,150,000.00 USD | 1,150,000.00 USD | 6,640.00 USD | 1,490.00 USD | 151,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 774,900.00 USD | 774,900.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 1,770,000.00 USD | 1,770,000.00 USD | 391,180.00 USD | 34,700.00 USD | 190,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 923,090.00 USD | 923,090.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 2,270,000.00 USD | 2,270,000.00 USD | 304,560.00 USD | 7,460.00 USD | 183,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 1,030,000.00 USD | 1,030,000.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 2,780,000.00 USD | 2,780,000.00 USD | 244,440.00 USD | 47,410.00 USD | 222,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 1,440,000.00 USD | 1,440,000.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 3,390,000.00 USD | 3,390,000.00 USD | 292,690.00 USD | 137,340.00 USD | 179,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 1,900,000.00 USD | 1,900,000.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 3,870,000.00 USD | 3,870,000.00 USD | 234,210.00 USD | 101,560.00 USD | 145,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 2,120,000.00 USD | 2,120,000.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 4,520,000.00 USD | 4,520,000.00 USD | 375,670.00 USD | 106,090.00 USD | 165,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 2,180,000.00 USD | 2,180,000.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 4,650,000.00 USD | 4,650,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 2,420,000.00 USD | 2,420,000.00 USD | 141,930.00 USD | 49,190.00 USD | 50,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 5,010,000.00 USD | 5,010,000.00 USD | 174,090.00 USD | 67,240.00 USD | 119,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 2,610,000.00 USD | 2,610,000.00 USD | 109,520.00 USD | 28,690.00 USD | 49,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 5,290,000.00 USD | 5,290,000.00 USD | 118,920.00 USD | 65,050.00 USD | 93,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,130.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 2,840,000.00 USD | 2,840,000.00 USD | 103,500.00 USD | 61,100.00 USD | 64,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 5,630,000.00 USD | 5,630,000.00 USD | 183,570.00 USD | 86,510.00 USD | 72,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 3,070,000.00 USD | 3,070,000.00 USD | 122,240.00 USD | 49,700.00 USD | 53,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 5,760,000.00 USD | 5,760,000.00 USD | 57,680.00 USD | 42,810.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 3,240,000.00 USD | 3,240,000.00 USD | 94,060.00 USD | 48,470.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 6,090,000.00 USD | 6,090,000.00 USD | 194,760.00 USD | 51,340.00 USD | 78,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 3,370,000.00 USD | 3,370,000.00 USD | 29,450.00 USD | 42,870.00 USD | 52,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 6,500,000.00 USD | 6,500,000.00 USD | 261,490.00 USD | 56,370.00 USD | 93,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 3,420,000.00 USD | 3,420,000.00 USD | 33,920.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 6,740,000.00 USD | 6,740,000.00 USD | 70,650.00 USD | 58,900.00 USD | 114,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,710.00 USD | 5,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 3,530,000.00 USD | 3,530,000.00 USD | 59,230.00 USD | 27,170.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 7,050,000.00 USD | 7,050,000.00 USD | 202,660.00 USD | 56,010.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 3,690,000.00 USD | 3,690,000.00 USD | 99,490.00 USD | 24,800.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 7,540,000.00 USD | 7,540,000.00 USD | 238,210.00 USD | 76,160.00 USD | 170,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 3,820,000.00 USD | 3,820,000.00 USD | 59,030.00 USD | 24,040.00 USD | 45,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 7,890,000.00 USD | 7,890,000.00 USD | 178,010.00 USD | 79,440.00 USD | 96,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 3,830,000.00 USD | 3,830,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 8,080,000.00 USD | 8,080,000.00 USD | 120,640.00 USD | 46,590.00 USD | 18,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 3,890,000.00 USD | 3,890,000.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 8,330,000.00 USD | 8,330,000.00 USD | 158,050.00 USD | 81,530.00 USD | 13,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 103,300.00 USD | 108,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 3,920,000.00 USD | 3,920,000.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 8,480,000.00 USD | 8,480,000.00 USD | 97,320.00 USD | 30,690.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 3,970,000.00 USD | 3,970,000.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 8,660,000.00 USD | 8,660,000.00 USD | 7,170.00 USD | 7,370.00 USD | 166,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 4,030,000.00 USD | 4,030,000.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 9,150,000.00 USD | 9,150,000.00 USD | 196,150.00 USD | 41,260.00 USD | 258,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 4,110,000.00 USD | 4,110,000.00 USD | 51,980.00 USD | 13,980.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 9,730,000.00 USD | 9,730,000.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 4,140,000.00 USD | 4,140,000.00 USD | 17,630.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 10,210,000.00 USD | 10,210,000.00 USD | 162,080.00 USD | 68,340.00 USD | 247,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,930.00 USD | 113,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 4,170,000.00 USD | 4,170,000.00 USD | 2,900.00 USD | 15,260.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 10,460,000.00 USD | 10,460,000.00 USD | 84,310.00 USD | 78,160.00 USD | 86,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 4,190,000.00 USD | 4,190,000.00 USD | 2,220.00 USD | 2,560.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 10,690,000.00 USD | 10,690,000.00 USD | 31,320.00 USD | 20,570.00 USD | 180,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 4,200,000.00 USD | 4,200,000.00 USD | 1,320.00 USD | 4,320.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 10,940,000.00 USD | 10,940,000.00 USD | 153,430.00 USD | 20,380.00 USD | 74,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 4,240,000.00 USD | 4,240,000.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 11,280,000.00 USD | 11,280,000.00 USD | 165,890.00 USD | 45,040.00 USD | 125,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 4,260,000.00 USD | 4,260,000.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 11,540,000.00 USD | 11,540,000.00 USD | 96,800.00 USD | 59,960.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.56` | 4,300,000.00 USD | 4,300,000.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 11,730,000.00 USD | 11,730,000.00 USD | 128,070.00 USD | 30,820.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 4,320,000.00 USD | 4,320,000.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 11,930,000.00 USD | 11,930,000.00 USD | 97,670.00 USD | 66,210.00 USD | 41,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 4,330,000.00 USD | 4,330,000.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 12,050,000.00 USD | 12,050,000.00 USD | 56,420.00 USD | 26,450.00 USD | 39,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 4,360,000.00 USD | 4,360,000.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 12,120,000.00 USD | 12,120,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 4,390,000.00 USD | 4,390,000.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 12,420,000.00 USD | 12,420,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 4,380.00 USD | 117,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 4,400,000.00 USD | 4,400,000.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 12,580,000.00 USD | 12,580,000.00 USD | 43,740.00 USD | 9,020.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 4,410,000.00 USD | 4,410,000.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 12,870,000.00 USD | 12,870,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 13,090,000.00 USD | 13,090,000.00 USD | 22,060.00 USD | 50,120.00 USD | 142,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 4,430,000.00 USD | 4,430,000.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 13,270,000.00 USD | 13,270,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 4,460,000.00 USD | 4,460,000.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 13,350,000.00 USD | 13,350,000.00 USD | 38,570.00 USD | 18,330.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 4,530,000.00 USD | 4,530,000.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 13,400,000.00 USD | 13,400,000.00 USD | 15,760.00 USD | 6,360.00 USD | 29,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 4,550,000.00 USD | 4,550,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 13,510,000.00 USD | 13,510,000.00 USD | 78,020.00 USD | 15,750.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 4,580,000.00 USD | 4,580,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 13,570,000.00 USD | 13,570,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 4,580,000.00 USD | 4,580,000.00 USD | 2,680.00 USD | 1,320.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 13,590,000.00 USD | 13,590,000.00 USD | 14,750.00 USD | 132.05 USD | 4,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 4,620,000.00 USD | 4,620,000.00 USD | 21,050.00 USD | 5,820.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 13,640,000.00 USD | 13,640,000.00 USD | 29,710.00 USD | 15,990.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 117,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 4,650,000.00 USD | 4,650,000.00 USD | 23,530.00 USD | 3,790.00 USD | 7,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 13,690,000.00 USD | 13,690,000.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 4,670,000.00 USD | 4,670,000.00 USD | 3,720.00 USD | 3,800.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 13,730,000.00 USD | 13,730,000.00 USD | 24,580.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 4,710,000.00 USD | 4,710,000.00 USD | 21,720.00 USD | 9,260.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 13,810,000.00 USD | 13,810,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 4,730,000.00 USD | 4,730,000.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 13,880,000.00 USD | 13,880,000.00 USD | 50,620.00 USD | 13,030.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 4,740,000.00 USD | 4,740,000.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 13,910,000.00 USD | 13,910,000.00 USD | 27,900.00 USD | 1,070.00 USD | 123.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 4,750,000.00 USD | 4,750,000.00 USD | 227.00 USD | 5,090.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 13,950,000.00 USD | 13,950,000.00 USD | 14,650.00 USD | 11,970.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 4,790,000.00 USD | 4,790,000.00 USD | 24,650.00 USD | 7,080.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 13,990,000.00 USD | 13,990,000.00 USD | 13,860.00 USD | 6,970.00 USD | 19,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 4,830,000.00 USD | 4,830,000.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 14,030,000.00 USD | 14,030,000.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.02` | 4,860,000.00 USD | 4,860,000.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 14,040,000.00 USD | 14,040,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.04` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 14,040,000.00 USD | 14,040,000.00 USD | 303.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 118,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `13.06` | 4,870,000.00 USD | 4,870,000.00 USD | 9,530.00 USD | 1,380.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.06` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.08` | 4,880,000.00 USD | 4,880,000.00 USD | 7,160.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `3.55` | 1,020,000.00 USD | 0.00 USD | 431.68 USD | `-69.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 1,020,000.00 USD | 0.00 USD | 290.29 USD | `-61.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 1,020,000.00 USD | 0.00 USD | 120.22 USD | `-55.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 1,020,000.00 USD | 0.00 USD | 107.09 USD | `-48.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 1,020,000.00 USD | 0.00 USD | 3,760.00 USD | `-43.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 1,020,000.00 USD | 0.00 USD | 133.00 USD | `-43.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 1,020,000.00 USD | 0.00 USD | 3,770.00 USD | `-39.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 1,020,000.00 USD | 0.00 USD | 2,070.00 USD | `-37.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 1,010,000.00 USD | 0.00 USD | 3,740.00 USD | `-36.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 1,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 1,010,000.00 USD | 0.00 USD | 146.80 USD | `-32.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 1,010,000.00 USD | 0.00 USD | 5,000.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 1,000,000.00 USD | 0.00 USD | 393.64 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 1,000,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 993,120.00 USD | 0.00 USD | 1,360.00 USD | `-27.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 991,760.00 USD | 0.00 USD | 30,250.00 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 961,510.00 USD | 0.00 USD | 186.84 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 961,320.00 USD | 0.00 USD | 742.88 USD | `-25.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 960,580.00 USD | 0.00 USD | 180.54 USD | `-24.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 960,400.00 USD | 0.00 USD | 1,320.00 USD | `-23.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 959,080.00 USD | 0.00 USD | 2,440.00 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 956,640.00 USD | 0.00 USD | 194.90 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 956,440.00 USD | 0.00 USD | 4,940.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 951,500.00 USD | 0.00 USD | 9,870.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 941,630.00 USD | 0.00 USD | 3,550.00 USD | `-17.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 938,090.00 USD | 0.00 USD | 25,950.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 912,130.00 USD | 0.00 USD | 19,100.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 893,030.00 USD | 0.00 USD | 299,650.00 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 593,380.00 USD | 0.00 USD | 2,590.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 590,790.00 USD | 0.00 USD | 1,050.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 589,740.00 USD | 0.00 USD | 2,820.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 586,920.00 USD | 0.00 USD | 2,000.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 584,920.00 USD | 0.00 USD | 19,450.00 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 565,470.00 USD | 0.00 USD | 5,160.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 560,310.00 USD | 0.00 USD | 4,590.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 555,720.00 USD | 0.00 USD | 5,470.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 550,240.00 USD | 0.00 USD | 4,370.00 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 545,870.00 USD | 0.00 USD | 6,510.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 539,360.00 USD | 0.00 USD | 16,530.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 522,830.00 USD | 0.00 USD | 24,830.00 USD | `-4.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 497,990.00 USD | 0.00 USD | 46,190.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 451,810.00 USD | 0.00 USD | 14,120.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 437,690.00 USD | 0.00 USD | 19,680.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 418,010.00 USD | 0.00 USD | 7,530.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 410,470.00 USD | 0.00 USD | 410,470.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 15,120.00 USD | 15,120.00 USD | 0.00 USD | `+0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 15,500.00 USD | 382.75 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 15,660.00 USD | 156.55 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 54,920.00 USD | 39,260.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 89,410.00 USD | 34,500.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 100,250.00 USD | 10,830.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 101,580.00 USD | 1,340.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 101,890.00 USD | 307.52 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 113,000.00 USD | 11,110.00 USD | 0.00 USD | `+7.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 169,530.00 USD | 56,530.00 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 211,010.00 USD | 41,470.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 231,730.00 USD | 20,730.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 232,520.00 USD | 784.77 USD | 0.00 USD | `+10.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 239,020.00 USD | 6,500.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 240,070.00 USD | 1,050.00 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 243,910.00 USD | 3,840.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 248,900.00 USD | 4,990.00 USD | 0.00 USD | `+14.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 263,420.00 USD | 14,520.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 266,060.00 USD | 2,630.00 USD | 0.00 USD | `+16.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 268,080.00 USD | 2,020.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 270,140.00 USD | 2,060.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 270,260.00 USD | 120.50 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 270,520.00 USD | 266.44 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 287,640.00 USD | 17,110.00 USD | 0.00 USD | `+20.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 288,700.00 USD | 1,060.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 295,690.00 USD | 6,990.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 295,910.00 USD | 218.25 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 298,520.00 USD | 2,610.00 USD | 0.00 USD | `+25.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 311,440.00 USD | 12,920.00 USD | 0.00 USD | `+26.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 312,390.00 USD | 950.82 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 323,620.00 USD | 11,220.00 USD | 0.00 USD | `+28.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 325,440.00 USD | 1,830.00 USD | 0.00 USD | `+29.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 558,480.00 USD | 233,040.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 571,980.00 USD | 13,500.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 572,870.00 USD | 893.01 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 573,260.00 USD | 388.75 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 599,370.00 USD | 26,100.00 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 601,470.00 USD | 2,110.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 606,810.00 USD | 5,340.00 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 612,130.00 USD | 5,320.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 621,300.00 USD | 9,170.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 628,100.00 USD | 6,800.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 646,860.00 USD | 18,760.00 USD | 0.00 USD | `+39.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 653,400.00 USD | 6,540.00 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 659,980.00 USD | 6,580.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 669,910.00 USD | 9,930.00 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 683,230.00 USD | 13,320.00 USD | 0.00 USD | `+42.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 697,470.00 USD | 14,240.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 781,830.00 USD | 84,360.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 783,520.00 USD | 1,700.00 USD | 0.00 USD | `+45.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 793,030.00 USD | 9,510.00 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 794,740.00 USD | 1,710.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 796,990.00 USD | 2,250.00 USD | 0.00 USD | `+47.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 895,330.00 USD | 98,330.00 USD | 0.00 USD | `+48.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 916,990.00 USD | 21,670.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 923,430.00 USD | 6,430.00 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 927,840.00 USD | 4,410.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 932,280.00 USD | 4,440.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 936,740.00 USD | 4,460.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 937,190.00 USD | 448.75 USD | 0.00 USD | `+53.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 972,770.00 USD | 35,590.00 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 973,230.00 USD | 453.75 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 974,060.00 USD | 830.38 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 974,510.00 USD | 458.75 USD | 0.00 USD | `+57.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 974,980.00 USD | 461.25 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 979,520.00 USD | 4,540.00 USD | 0.00 USD | `+58.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 979,990.00 USD | 466.25 USD | 0.00 USD | `+59.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 980,460.00 USD | 468.75 USD | 0.00 USD | `+60.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 980,930.00 USD | 471.25 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 981,400.00 USD | 473.75 USD | 0.00 USD | `+62.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,050,000.00 USD | 67,000.00 USD | 0.00 USD | `+63.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,050,000.00 USD | 574.50 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,050,000.00 USD | 577.50 USD | 0.00 USD | `+64.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,050,000.00 USD | 2,710.00 USD | 0.00 USD | `+65.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,050,000.00 USD | 972.50 USD | 0.00 USD | `+66.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,060,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,060,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,060,000.00 USD | 1,690.00 USD | 0.00 USD | `+69.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,070,000.00 USD | 992.50 USD | 0.00 USD | `+69.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,070,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,680,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,690,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,690,000.00 USD | 1,020.00 USD | 0.00 USD | `+75.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,690,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,690,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,690,000.00 USD | 1,860.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,690,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,700,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,700,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,700,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,700,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,750,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,750,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,750,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,750,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,750,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,760,000.00 USD | 3,280.00 USD | 0.00 USD | `+87.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,760,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,760,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,760,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,760,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,760,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,760,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,760,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,770,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,770,000.00 USD | 1,150.00 USD | 0.00 USD | `+96.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,900,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,900,000.00 USD | 1,160.00 USD | 0.00 USD | `+99.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,900,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.89%` | `TACTICAL (Retail Cluster)` |

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
| `1D` | `10.46` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 27,560.00 USD | 8,350.00 USD | 16,510.00 USD |
| `7D` | `10.46` | 19,170,000.00 USD | 0.00 USD | 19,170,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,650.00 USD |
| `1D` | `10.48` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD |
| `7D` | `10.48` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,380.00 USD |
| `1D` | `10.50` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 23,170.00 USD | 7,140.00 USD | 8,180.00 USD |
| `7D` | `10.50` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,660.00 USD |
| `1D` | `10.52` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 22,700.00 USD | 3,790.00 USD | 3,090.00 USD |
| `7D` | `10.52` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 19,300.00 USD | 8,750.00 USD | 19,470.00 USD |
| `1D` | `10.54` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 4,350.00 USD | 3,800.00 USD | 9,590.00 USD |
| `7D` | `10.54` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,860.00 USD |
| `1D` | `10.56` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 22,600.00 USD | 7,180.00 USD | 1,810.00 USD |
| `7D` | `10.56` | 18,840,000.00 USD | 0.00 USD | 18,840,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,310.00 USD |
| `1D` | `10.58` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 20,460.00 USD | 5,420.00 USD | 8,210.00 USD |
| `7D` | `10.58` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,240.00 USD |
| `1D` | `10.60` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 1,040.00 USD | 5,090.00 USD | 3,230.00 USD |
| `7D` | `10.60` | 18,640,000.00 USD | 0.00 USD | 18,640,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,590.00 USD |
| `1D` | `10.62` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 25,570.00 USD | 7,080.00 USD | 12,050.00 USD |
| `7D` | `10.62` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,170.00 USD |
| `1D` | `10.64` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 18,390.00 USD | 7,780.00 USD | 16,540.00 USD |
| `7D` | `10.64` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,430.00 USD |
| `1D` | `10.66` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 17,480.00 USD | 3,100.00 USD | 4,680.00 USD |
| `7D` | `10.66` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,240.00 USD |
| `1D` | `10.68` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 10,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,580.00 USD |
| `1D` | `10.70` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 8,380.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `10.70` | 18,450,000.00 USD | 0.00 USD | 18,450,000.00 USD | 14,670.00 USD | 0.00 USD | 188.12 USD |
| `1D` | `10.72` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 6,390.00 USD | 5,500.00 USD | 7,370.00 USD |
| `7D` | `10.72` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,810.00 USD |
| `1D` | `10.74` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 12,810.00 USD | 8,380.00 USD | 7,200.00 USD |
| `7D` | `10.74` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 20,210.00 USD | 4,010.00 USD | 318.38 USD |
| `1D` | `10.76` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,610.00 USD |
| `7D` | `10.76` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 16,310.00 USD | 0.00 USD | 294.21 USD |
| `1D` | `10.78` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 1,070.00 USD | 4,870.00 USD | 3,000.00 USD |
| `7D` | `10.78` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 14,200.00 USD | 4,000.00 USD | 23,690.00 USD |
| `1D` | `10.80` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 4,360.00 USD | 0.00 USD | 51.14 USD |
| `7D` | `10.80` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,490.00 USD |
| `1D` | `10.82` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 2,030.00 USD | 0.00 USD | 68.68 USD |
| `7D` | `10.82` | 18,170,000.00 USD | 0.00 USD | 18,170,000.00 USD | 135,080.00 USD | 28,860.00 USD | 10,980.00 USD |
| `1D` | `10.84` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 1,520.00 USD | 160.15 USD | 31.01 USD |
| `7D` | `10.84` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 79,220.00 USD | 38,860.00 USD | 46,230.00 USD |
| `1D` | `10.86` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 976.86 USD | 4,520.00 USD | 3,770.00 USD |
| `7D` | `10.86` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 239,570.00 USD | 18,350.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 1,740.00 USD | 10,400.00 USD | 16,270.00 USD |
| `7D` | `10.88` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,540.00 USD |
| `1D` | `10.90` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 1,120.00 USD | 3,770.00 USD | 26,510.00 USD |
| `7D` | `10.90` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,670.00 USD |
| `1D` | `10.92` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 66,820.00 USD | 28,790.00 USD | 58,390.00 USD |
| `7D` | `10.92` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,080.00 USD |
| `1D` | `10.94` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 47,590.00 USD | 17,110.00 USD | 5,770.00 USD |
| `7D` | `10.94` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,940.00 USD |
| `1D` | `10.96` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 97,290.00 USD | 23,300.00 USD | 28,990.00 USD |
| `7D` | `10.96` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,320.00 USD |
| `1D` | `10.98` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 23,860.00 USD | 2,590.00 USD | 27,270.00 USD |
| `7D` | `10.98` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 96,870.00 USD | 110,950.00 USD | 161,880.00 USD |
| `1D` | `11.00` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 18,750.00 USD | 7,740.00 USD | 22,380.00 USD |
| `7D` | `11.00` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 134,000.00 USD | 91,410.00 USD | 160,860.00 USD |
| `1D` | `11.02` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 96,430.00 USD | 24,240.00 USD | 31,970.00 USD |
| `7D` | `11.02` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,840.00 USD |
| `1D` | `11.04` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 14,810.00 USD | 12,540.00 USD | 2,830.00 USD |
| `7D` | `11.04` | 13,260,000.00 USD | 0.00 USD | 13,260,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,840.00 USD |
| `1D` | `11.06` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 18,980.00 USD | 3,150.00 USD | 20,340.00 USD |
| `7D` | `11.06` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,800.00 USD |
| `1D` | `11.08` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 28,790.00 USD | 15,060.00 USD | 29,500.00 USD |
| `7D` | `11.08` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,470.00 USD |
| `1D` | `11.10` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 31,390.00 USD | 30,270.00 USD | 32,470.00 USD |
| `7D` | `11.10` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,360.00 USD |
| `1D` | `11.12` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 54,370.00 USD | 33,090.00 USD | 75,860.00 USD |
| `7D` | `11.12` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,950.00 USD |
| `1D` | `11.14` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 169,390.00 USD | 74,650.00 USD | 137,850.00 USD |
| `7D` | `11.14` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 692,090.00 USD | 176,150.00 USD | 604,600.00 USD |
| `1D` | `11.16` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 170,410.00 USD | 51,900.00 USD | 75,190.00 USD |
| `7D` | `11.16` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,990.00 USD |
| `1D` | `11.18` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 137,180.00 USD | 43,130.00 USD | 55,140.00 USD |
| `7D` | `11.18` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 659,190.00 USD | 214,580.00 USD | 541,440.00 USD |
| `1D` | `11.20` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 222,000.00 USD | 47,730.00 USD | 92,450.00 USD |
| `7D` | `11.20` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 371,240.00 USD | 240,290.00 USD | 128,880.00 USD |
| `1D` | `11.22` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 97,140.00 USD | 31,710.00 USD | 37,230.00 USD |
| `7D` | `11.22` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 208,020.00 USD | 228,180.00 USD | 217,320.00 USD |
| `1D` | `11.24` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 111,250.00 USD | 63,170.00 USD | 83,000.00 USD |
| `7D` | `11.24` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 189,850.00 USD | 48,720.00 USD | 55,920.00 USD |
| `7D` | `11.26` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD |
| `1D` | `11.28` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 53,900.00 USD | 18,650.00 USD | 54,240.00 USD |
| `7D` | `11.28` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 83,100.00 USD | 19,980.00 USD | 31,710.00 USD |
| `7D` | `11.30` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD |
| `1D` | `11.32` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 72,190.00 USD | 16,200.00 USD | 28,360.00 USD |
| `7D` | `11.32` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD |
| `1D` | `11.34` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 203,070.00 USD | 40,470.00 USD | 25,180.00 USD |
| `7D` | `11.34` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD |
| `1D` | `11.36` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 232,100.00 USD | 83,300.00 USD | 85,030.00 USD |
| `7D` | `11.36` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 170,150.00 USD | 48,220.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 22,780.00 USD | 44,790.00 USD | 58,270.00 USD |
| `7D` | `11.38` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 90,940.00 USD | 23,630.00 USD | 78,680.00 USD |
| `7D` | `11.40` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 106,690.00 USD | 34,500.00 USD | 53,910.00 USD |
| `7D` | `11.42` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 61,980.00 USD | 0.00 USD | 55,710.00 USD |
| `1D` | `11.44` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 130,750.00 USD | 43,710.00 USD | 71,320.00 USD |
| `7D` | `11.44` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 148,600.00 USD | 44,370.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 928,090.00 USD | 0.00 USD | 928,090.00 USD | 177,600.00 USD | 30,500.00 USD | 24,850.00 USD |
| `7D` | `11.46` | 769,190.00 USD | 0.00 USD | 769,190.00 USD | 0.00 USD | 10,040.00 USD | 0.00 USD |
| `1D` | `11.48` | 695,130.00 USD | 0.00 USD | 695,130.00 USD | 16,710.00 USD | 25,810.00 USD | 34,840.00 USD |
| `7D` | `11.48` | 759,150.00 USD | 0.00 USD | 759,150.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `11.50` | 617,780.00 USD | 0.00 USD | 617,780.00 USD | 74,140.00 USD | 51,260.00 USD | 14,300.00 USD |
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
| `1D` | `11.64` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.64` | 358,820.00 USD | 0.00 USD | 358,820.00 USD | 68,740.00 USD | 79,630.00 USD | 55,700.00 USD |
| `1D` | `11.66` | 37,590.00 USD | 37,590.00 USD | 0.00 USD | 0.00 USD | 12,710.00 USD | 24,880.00 USD |
| `7D` | `11.66` | 154,750.00 USD | 0.00 USD | 154,750.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 83,510.00 USD | 83,510.00 USD | 0.00 USD | 0.00 USD | 294.87 USD | 45,630.00 USD |
| `7D` | `11.68` | 92,780.00 USD | 0.00 USD | 92,780.00 USD | 88,140.00 USD | 4,650.00 USD | 0.00 USD |
| `1D` | `11.70` | 83,740.00 USD | 83,740.00 USD | 0.00 USD | 0.00 USD | 230.72 USD | 0.00 USD |
| `7D` | `11.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.72` | 261,160.00 USD | 261,160.00 USD | 0.00 USD | 164,600.00 USD | 12,820.00 USD | 0.00 USD |
| `7D` | `11.72` | 195,940.00 USD | 195,940.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 261,490.00 USD | 261,490.00 USD | 0.00 USD | 0.00 USD | 324.58 USD | 0.00 USD |
| `1D` | `11.76` | 261,830.00 USD | 261,830.00 USD | 0.00 USD | 0.00 USD | 342.56 USD | 0.00 USD |
| `7D` | `11.76` | 244,130.00 USD | 244,130.00 USD | 0.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 278,860.00 USD | 278,860.00 USD | 0.00 USD | 16,180.00 USD | 850.97 USD | 0.00 USD |
| `1D` | `11.80` | 279,920.00 USD | 279,920.00 USD | 0.00 USD | 0.00 USD | 1,060.00 USD | 0.00 USD |
| `7D` | `11.80` | 384,250.00 USD | 384,250.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.82` | 545,000.00 USD | 545,000.00 USD | 0.00 USD | 158,640.00 USD | 1,970.00 USD | 133.38 USD |
| `1D` | `11.84` | 363,840.00 USD | 363,840.00 USD | 0.00 USD | 55,360.00 USD | 1,130.00 USD | 27,420.00 USD |
| `7D` | `11.84` | 764,330.00 USD | 764,330.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 10.32 USD |
| `1D` | `11.86` | 435,990.00 USD | 435,990.00 USD | 0.00 USD | 232.40 USD | 33,940.00 USD | 37,980.00 USD |
| `7D` | `11.86` | 770,990.00 USD | 770,990.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | 42.92 USD |
| `1D` | `11.88` | 491,940.00 USD | 491,940.00 USD | 0.00 USD | 19,640.00 USD | 15,360.00 USD | 20,940.00 USD |
| `7D` | `11.88` | 783,970.00 USD | 783,970.00 USD | 0.00 USD | 10,340.00 USD | 2,480.00 USD | 165.54 USD |
| `1D` | `11.90` | 536,150.00 USD | 536,150.00 USD | 0.00 USD | 44,160.00 USD | 59.50 USD | 0.00 USD |
| `7D` | `11.90` | 795,940.00 USD | 795,940.00 USD | 0.00 USD | 11,220.00 USD | 612.37 USD | 145.40 USD |
| `1D` | `11.92` | 609,130.00 USD | 609,130.00 USD | 0.00 USD | 59,860.00 USD | 13,090.00 USD | 20.02 USD |
| `7D` | `11.92` | 803,120.00 USD | 803,120.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | 169.96 USD |
| `1D` | `11.94` | 654,700.00 USD | 654,700.00 USD | 0.00 USD | 1,220.00 USD | 15,870.00 USD | 28,480.00 USD |
| `7D` | `11.94` | 993,220.00 USD | 993,220.00 USD | 0.00 USD | 17,060.00 USD | 24,600.00 USD | 148,450.00 USD |
| `1D` | `11.96` | 721,460.00 USD | 721,460.00 USD | 0.00 USD | 12,210.00 USD | 26,690.00 USD | 27,850.00 USD |
| `7D` | `11.96` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 6,640.00 USD | 1,490.00 USD | 151,660.00 USD |
| `1D` | `11.98` | 858,420.00 USD | 858,420.00 USD | 0.00 USD | 61,680.00 USD | 7,680.00 USD | 67,590.00 USD |
| `7D` | `11.98` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 391,180.00 USD | 34,700.00 USD | 190,650.00 USD |
| `1D` | `12.00` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 106,180.00 USD | 351.59 USD | 41,650.00 USD |
| `7D` | `12.00` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 304,560.00 USD | 7,460.00 USD | 183,600.00 USD |
| `1D` | `12.02` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 59,970.00 USD | 32,820.00 USD | 15,260.00 USD |
| `7D` | `12.02` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 244,440.00 USD | 47,410.00 USD | 222,490.00 USD |
| `1D` | `12.04` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 233,510.00 USD | 73,470.00 USD | 97,900.00 USD |
| `7D` | `12.04` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 292,690.00 USD | 137,340.00 USD | 179,710.00 USD |
| `1D` | `12.06` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 221,050.00 USD | 88,350.00 USD | 155,690.00 USD |
| `7D` | `12.06` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 234,210.00 USD | 101,560.00 USD | 145,610.00 USD |
| `1D` | `12.08` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 123,260.00 USD | 45,990.00 USD | 52,780.00 USD |
| `7D` | `12.08` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 165,220.00 USD |
| `1D` | `12.10` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 19,140.00 USD | 9,670.00 USD | 31,090.00 USD |
| `7D` | `12.10` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 141,930.00 USD | 49,190.00 USD | 50,370.00 USD |
| `7D` | `12.12` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 174,090.00 USD | 67,240.00 USD | 119,400.00 USD |
| `1D` | `12.14` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 109,520.00 USD | 28,690.00 USD | 49,160.00 USD |
| `7D` | `12.14` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 118,920.00 USD | 65,050.00 USD | 93,050.00 USD |
| `1D` | `12.16` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 96,770.00 USD | 58,800.00 USD | 53,300.00 USD |
| `7D` | `12.16` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 183,570.00 USD | 86,510.00 USD | 72,100.00 USD |
| `1D` | `12.18` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 117,230.00 USD | 43,460.00 USD | 45,950.00 USD |
| `7D` | `12.18` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 57,680.00 USD | 42,810.00 USD | 31,960.00 USD |
| `1D` | `12.20` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 94,060.00 USD | 43,290.00 USD | 25,360.00 USD |
| `7D` | `12.20` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 194,760.00 USD | 51,340.00 USD | 78,380.00 USD |
| `1D` | `12.22` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 29,450.00 USD | 42,870.00 USD | 52,640.00 USD |
| `7D` | `12.22` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 261,490.00 USD | 56,370.00 USD | 93,640.00 USD |
| `1D` | `12.24` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 33,920.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.24` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 70,650.00 USD | 58,900.00 USD | 114,600.00 USD |
| `1D` | `12.26` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 55,900.00 USD | 27,170.00 USD | 21,490.00 USD |
| `7D` | `12.26` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 202,660.00 USD | 56,010.00 USD | 50,570.00 USD |
| `1D` | `12.28` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 99,490.00 USD | 24,800.00 USD | 37,620.00 USD |
| `7D` | `12.28` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 238,210.00 USD | 76,160.00 USD | 170,690.00 USD |
| `1D` | `12.30` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 59,030.00 USD | 24,040.00 USD | 45,440.00 USD |
| `7D` | `12.30` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 178,010.00 USD | 79,440.00 USD | 96,690.00 USD |
| `1D` | `12.32` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.32` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 120,640.00 USD | 46,590.00 USD | 18,010.00 USD |
| `1D` | `12.34` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 29,420.00 USD | 8,560.00 USD | 17,040.00 USD |
| `7D` | `12.34` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 158,050.00 USD | 81,530.00 USD | 13,430.00 USD |
| `1D` | `12.36` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 19,510.00 USD | 9,040.00 USD | 5,460.00 USD |
| `7D` | `12.36` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 97,320.00 USD | 30,690.00 USD | 18,500.00 USD |
| `1D` | `12.38` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 30,170.00 USD | 6,420.00 USD | 12,760.00 USD |
| `7D` | `12.38` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 166,020.00 USD |
| `1D` | `12.40` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 18,820.00 USD | 23,720.00 USD | 22,980.00 USD |
| `7D` | `12.40` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 196,150.00 USD | 41,260.00 USD | 258,500.00 USD |
| `1D` | `12.42` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 51,980.00 USD | 13,980.00 USD | 9,680.00 USD |
| `7D` | `12.42` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 17,630.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.44` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 162,080.00 USD | 68,340.00 USD | 247,990.00 USD |
| `1D` | `12.46` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 411.51 USD | 15,260.00 USD | 11,590.00 USD |
| `7D` | `12.46` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 84,310.00 USD | 78,160.00 USD | 86,180.00 USD |
| `1D` | `12.48` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 2,220.00 USD | 2,560.00 USD | 8,380.00 USD |
| `7D` | `12.48` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 31,320.00 USD | 20,570.00 USD | 180,460.00 USD |
| `1D` | `12.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 1,320.00 USD | 4,320.00 USD | 8,230.00 USD |
| `7D` | `12.50` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 153,430.00 USD | 20,380.00 USD | 74,680.00 USD |
| `1D` | `12.52` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 21,510.00 USD | 5,020.00 USD | 12,100.00 USD |
| `7D` | `12.52` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 165,890.00 USD | 45,040.00 USD | 125,090.00 USD |
| `1D` | `12.54` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 14,970.00 USD | 2,830.00 USD | 38.33 USD |
| `7D` | `12.54` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 96,800.00 USD | 59,960.00 USD | 107,090.00 USD |
| `1D` | `12.56` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 26,360.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.56` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 128,070.00 USD | 30,820.00 USD | 27,480.00 USD |
| `1D` | `12.58` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 11,120.00 USD |
| `7D` | `12.58` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 97,670.00 USD | 66,210.00 USD | 41,120.00 USD |
| `1D` | `12.60` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 3,990.00 USD | 1,310.00 USD | 1,180.00 USD |
| `7D` | `12.60` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 56,420.00 USD | 26,450.00 USD | 39,140.00 USD |
| `1D` | `12.62` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 12,620.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,130.00 USD |
| `1D` | `12.64` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 19,680.00 USD | 4,240.00 USD | 7,570.00 USD |
| `7D` | `12.64` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,820.00 USD |
| `1D` | `12.66` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 394.11 USD | 23.77 USD | 3,290.00 USD |
| `7D` | `12.66` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 43,740.00 USD | 9,020.00 USD | 99,100.00 USD |
| `1D` | `12.68` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 3,670.00 USD | 1,490.00 USD | 7,130.00 USD |
| `7D` | `12.68` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,470.00 USD |
| `1D` | `12.70` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,140.00 USD | 2,780.00 USD |
| `7D` | `12.70` | 13,090,000.00 USD | 13,090,000.00 USD | 0.00 USD | 22,060.00 USD | 50,120.00 USD | 142,780.00 USD |
| `1D` | `12.72` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 3.03 USD |
| `7D` | `12.72` | 13,270,000.00 USD | 13,270,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,170.00 USD |
| `1D` | `12.74` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 20,500.00 USD | 8,140.00 USD | 6,520.00 USD |
| `7D` | `12.74` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 20,890.00 USD |
| `1D` | `12.76` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 39,130.00 USD | 11,090.00 USD | 16,280.00 USD |
| `7D` | `12.76` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 15,760.00 USD | 6,360.00 USD | 29,510.00 USD |
| `1D` | `12.78` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.78` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 78,020.00 USD | 15,750.00 USD | 18,720.00 USD |
| `1D` | `12.80` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 12,430.00 USD | 4,740.00 USD | 9,480.00 USD |
| `7D` | `12.80` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,530.00 USD |
| `1D` | `12.82` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 2,680.00 USD | 1,320.00 USD | 1,990.00 USD |
| `7D` | `12.82` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 4,980.00 USD |
| `1D` | `12.84` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 20,500.00 USD | 5,820.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 29,710.00 USD | 15,990.00 USD | 7,980.00 USD |
| `1D` | `12.86` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 22,700.00 USD | 3,790.00 USD | 3,060.00 USD |
| `7D` | `12.86` | 13,690,000.00 USD | 13,690,000.00 USD | 0.00 USD | 14,970.00 USD | 8,750.00 USD | 19,370.00 USD |
| `1D` | `12.88` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 3,720.00 USD | 3,800.00 USD | 9,590.00 USD |
| `7D` | `12.88` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 24,580.00 USD | 4,610.00 USD | 12,750.00 USD |
| `1D` | `12.90` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 21,720.00 USD | 7,180.00 USD | 1,810.00 USD |
| `7D` | `12.90` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,200.00 USD |
| `1D` | `12.92` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 6,680.00 USD | 4,130.00 USD | 8,200.00 USD |
| `7D` | `12.92` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 11,060.00 USD |
| `1D` | `12.94` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 13,280.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.94` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 123.98 USD |
| `1D` | `12.96` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,220.00 USD |
| `7D` | `12.96` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 14,650.00 USD | 11,970.00 USD | 10,480.00 USD |
| `1D` | `12.98` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 24,650.00 USD | 7,080.00 USD | 12,040.00 USD |
| `7D` | `12.98` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 19,020.00 USD |
| `1D` | `13.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 17,330.00 USD | 7,780.00 USD | 16,490.00 USD |
| `7D` | `13.00` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD |
| `1D` | `13.02` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 16,830.00 USD | 3,100.00 USD | 4,670.00 USD |
| `7D` | `13.02` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `1D` | `13.04` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `13.04` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 303.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.06` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD |
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
  * Total Open Interest: `555.01M` | Total OI Tokens: `47,661,391.5 LINK`
  * 1h OI Change: `-1.08%` | 4h OI Change: `-1.59%` | 24h OI Change: `-2.59%`
  * Exchange Breakdown: Binance=`105.49M` | Bybit=`65.52M` | OKX=`26.41M` | Hyperliquid=`56.44M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.76K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0003%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0057%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `48.64%` | `51.36%` | `0.95` | 395,930.00 USD |
| `15M` | `Binance` | `48.24%` | `51.76%` | `0.93` | 100,890.00 USD |
| `15M` | `OKX` | `58.39%` | `41.61%` | `1.40` | 23,440.00 USD |
| `15M` | `Bybit` | `89.47%` | `10.53%` | `8.50` | 16,430.00 USD |
| `15M` | `KuCoin` | `54.14%` | `45.86%` | `1.18` | 17,190.00 USD |
| `15M` | `Gate` | `48.32%` | `51.68%` | `0.93` | 13,390.00 USD |
| `15M` | `Bitget` | `75.5%` | `24.5%` | `3.08` | 1,230.00 USD |
| `15M` | `BingX` | `51.16%` | `48.84%` | `1.05` | 32,760.00 USD |
| `15M` | `MEXC` | `52.22%` | `47.78%` | `1.09` | 3,660.00 USD |
| `15M` | `Bitunix` | `52.49%` | `47.51%` | `1.10` | 2,900.00 USD |
| `15M` | `Hyperliquid` | `72.45%` | `27.55%` | `2.63` | 496.83 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.93%` | `50.07%` | `1.00` | 62,570.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `38.61%` | `61.39%` | `0.63` | 106,360.00 USD |
| `15M` | `HTX` | `37.51%` | `62.49%` | `0.60` | 13,140.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `69.7%` | `30.3%` | `2.30` | 1,280.00 USD |
| `15M` | `Aster` | `38.56%` | `61.44%` | `0.63` | 54.98 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 122.98 USD |
| `15M` | `Whale Positions` | `48.24%` | `51.76%` | `0.93` | 100,890.00 USD |
| `15M` | `Global Accounts` | `48.64%` | `51.36%` | `0.95` | 395,930.00 USD |
| `1H` | `LINK` | `46.92%` | `53.08%` | `0.88` | 2,470,000.00 USD |
| `1H` | `Binance` | `53.71%` | `46.29%` | `1.16` | 888,490.00 USD |
| `1H` | `OKX` | `44.31%` | `55.69%` | `0.80` | 146,310.00 USD |
| `1H` | `Bybit` | `39.15%` | `60.85%` | `0.64` | 143,360.00 USD |
| `1H` | `KuCoin` | `47.33%` | `52.67%` | `0.90` | 64,280.00 USD |
| `1H` | `Gate` | `49.46%` | `50.54%` | `0.98` | 61,470.00 USD |
| `1H` | `Bitget` | `44.57%` | `55.43%` | `0.80` | 46,300.00 USD |
| `1H` | `BingX` | `40.98%` | `59.02%` | `0.69` | 127,500.00 USD |
| `1H` | `MEXC` | `49.11%` | `50.89%` | `0.97` | 21,530.00 USD |
| `1H` | `Bitunix` | `50.88%` | `49.12%` | `1.04` | 29,510.00 USD |
| `1H` | `Hyperliquid` | `17.77%` | `82.23%` | `0.22` | 54,040.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.71%` | `45.29%` | `1.21` | 397,270.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `17.02%` | `82.98%` | `0.21` | 434,200.00 USD |
| `1H` | `HTX` | `27.35%` | `72.65%` | `0.38` | 45,130.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `17.42%` | `82.58%` | `0.21` | 2,760.00 USD |
| `1H` | `Aster` | `43.45%` | `56.55%` | `0.77` | 1,960.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `39.73%` | `60.27%` | `0.66` | 4,050.00 USD |
| `1H` | `Whale Positions` | `53.71%` | `46.29%` | `1.16` | 888,490.00 USD |
| `1H` | `Global Accounts` | `46.92%` | `53.08%` | `0.88` | 2,470,000.00 USD |
| `4H` | `LINK` | `45.14%` | `54.86%` | `0.82` | 11,430,000.00 USD |
| `4H` | `Binance` | `51.72%` | `48.28%` | `1.07` | 4,120,000.00 USD |
| `4H` | `OKX` | `45.55%` | `54.45%` | `0.84` | 694,650.00 USD |
| `4H` | `Bybit` | `51.61%` | `48.39%` | `1.07` | 579,260.00 USD |
| `4H` | `KuCoin` | `49.67%` | `50.33%` | `0.99` | 266,990.00 USD |
| `4H` | `Gate` | `58.56%` | `41.44%` | `1.41` | 285,280.00 USD |
| `4H` | `Bitget` | `60.5%` | `39.5%` | `1.53` | 161,340.00 USD |
| `4H` | `BingX` | `27.6%` | `72.4%` | `0.38` | 979,100.00 USD |
| `4H` | `MEXC` | `62.43%` | `37.57%` | `1.66` | 148,700.00 USD |
| `4H` | `Bitunix` | `51.47%` | `48.53%` | `1.06` | 120,230.00 USD |
| `4H` | `Hyperliquid` | `82.92%` | `17.08%` | `4.85` | 384,760.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.18%` | `49.82%` | `1.01` | 1,790,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.19%` | `88.81%` | `0.13` | 1,540,000.00 USD |
| `4H` | `HTX` | `53.7%` | `46.3%` | `1.16` | 196,260.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `78.58%` | `21.42%` | `3.67` | 102,850.00 USD |
| `4H` | `Aster` | `21.05%` | `78.95%` | `0.27` | 8,790.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.69%` | `72.31%` | `0.38` | 63,390.00 USD |
| `4H` | `Whale Positions` | `51.72%` | `48.28%` | `1.07` | 4,120,000.00 USD |
| `4H` | `Global Accounts` | `45.14%` | `54.86%` | `0.82` | 11,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.84` | `11.85` | `11.84` | `11.87` | `11.83` | 923,896.67 USD | 361,612.35 USD | 562,284.32 USD | -200,671.96 USD | `-21.72%` | `4B / 14S` |
| `0:00 UTC` | `11.83` | `11.83` | `11.83` | `11.87` | `11.79` | 1,261,426.96 USD | 528,120.38 USD | 733,306.58 USD | -205,186.20 USD | `-16.27%` | `8B / 14S` |
| `5:00 UTC` | `11.80` | `11.80` | `11.80` | `11.83` | `11.79` | 889,528.52 USD | 480,169.70 USD | 409,358.82 USD | 70,810.88 USD | `+7.96%` | `8B / 3S` |
| `0:00 UTC` | `11.78` | `11.76` | `11.78` | `11.84` | `11.71` | 1,746,825.55 USD | 823,777.15 USD | 923,048.41 USD | -99,271.26 USD | `-5.68%` | `22B / 37S` |
| `5:00 UTC` | `11.71` | `11.70` | `11.71` | `11.74` | `11.66` | 1,705,508.25 USD | 855,092.75 USD | 850,415.50 USD | 4,677.25 USD | `+0.27%` | `14B / 10S` |
| `0:00 UTC` | `11.73` | `11.73` | `11.73` | `11.75` | `11.71` | 756,364.68 USD | 311,101.50 USD | 445,263.18 USD | -134,161.69 USD | `-17.74%` | `6B / 13S` |
| `5:00 UTC` | `11.74` | `11.73` | `11.74` | `11.76` | `11.69` | 1,033,883.46 USD | 539,127.77 USD | 494,755.69 USD | 44,372.08 USD | `+4.29%` | `15B / 13S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.65` | `11.66` | `11.65` | `11.69` | `11.65` | 115,542.65 USD | 55,662.25 USD | 59,880.40 USD | -4,218.15 USD | `-3.65%` | `8B / 12S` |

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
| `5m` | -21,870.00 USD | -140,210.00 USD | **`DISTRIBUTION`** |
| `15m` | -23,130.00 USD | 631,250.00 USD | **`ACCUMULATION`** |
| `30m` | -54,530.00 USD | 601,410.00 USD | **`ACCUMULATION`** |
| `1h` | -34,780.00 USD | -169,950.00 USD | **`DISTRIBUTION`** |
| `2h` | -813,190.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -159,930.00 USD | -1,860,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 315,600.00 USD | -870,950.00 USD | **`DISTRIBUTION`** |
| `8h` | 326,040.00 USD | -598,080.00 USD | **`DISTRIBUTION`** |
| `12h` | 386,100.00 USD | 586,860.00 USD | **`ACCUMULATION`** |
| `24h` | 498,380.00 USD | -3,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,040,000.00 USD | -23,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -68,240,000.00 USD | -187,290,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-21.87K` | 15m=`-23.13K` | 1h=`-34.78K` | 24h=`+498.38K`
* Futures Capital Netflows: 5m=`-140.21K` | 15m=`+631.25K` | 1h=`-169.95K` | 24h=`-3.38M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `11.22` (Risk Distance: `0.2199` pts)
  * +2.5R Take Profit: `11.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.13` (Risk Distance: `0.2199` pts)
  * +2.5R Take Profit: `11.36`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.74`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
