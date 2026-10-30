# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.89` | **Live Ask Quote**: `104.94` | **Mid Price**: `104.91`
- **Spread Points**: `46.00` | **Spread BPS**: `4.38 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1,000.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `10.00 USD` | Point Value (0.01 Lot): `0.1000 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `104.91` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.65` | Lower -3.00σ Band: `104.18`
  * Upper +2.51σ Band: `105.49` | Lower -2.51σ Band: `104.34`
  * Upper +2.01σ Band: `105.35` | Lower -2.01σ Band: `104.47`
  * Upper +2.00σ Band: `105.33` | Lower -2.00σ Band: `104.49`
  * Upper +1.28σ Band: `105.21` | Lower -1.28σ Band: `104.62`
  * Upper +1.00σ Band: `105.12` | Lower -1.00σ Band: `104.70`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.91` | EMA-20=`104.91` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`104.91` (Slope: `+0.0000`) | EMA-100=`104.91`
  * Institutional Anchors: EMA-144=`104.91` | EMA-200=`104.91` (Slope: `+0.0000`) | EMA-233=`104.91`
- **Range Boundaries**: 24H High=`105.96` | 24H Low=`103.86` | Weekly High=`107.01` | Weekly Low=`102.81`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.94` (Distance: `-0.01%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.83%`)
  * Value Area Low (VAL) = `103.58` (Distance: `+1.30%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.40` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.95` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.95` | Low=`104.33`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.49` - `105.33`
  * Optimal Trade Entry (OTE 0.705): `105.12`
  * Structural Invalidation Anchor (0.786): `105.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.24` | `104.42` | `104.24` | `104.35` | `381` | 39,756.59 USD | 16,038.17 USD | `+40.34%` | 455,704.33 USD | `+0.33` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.34` | `104.40` | `104.19` | `104.40` | `362` | 37,792.08 USD | 23,395.09 USD | `+61.90%` | 479,099.42 USD | `+0.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.40` | `104.72` | `104.40` | `104.65` | `457` | 47,824.14 USD | 31,010.96 USD | `+64.84%` | 510,110.38 USD | `+0.91` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.75` | `104.18` | `103.68` | `104.11` | `986` | 102,650.49 USD | 73,618.03 USD | `+71.72%` | 632,600.99 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.12` | `104.42` | `103.92` | `104.35` | `1,106` | 115,408.89 USD | 68,091.24 USD | `+59.00%` | 700,692.24 USD | `+1.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.34` | `104.72` | `104.19` | `104.45` | `1,247` | 130,246.66 USD | 11,058.68 USD | `+8.49%` | 711,750.91 USD | `+0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `103.55` | `104.12` | `103.51` | `103.92` | `2,479` | 257,617.68 USD | 123,135.37 USD | `+47.80%` | 404,442.13 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.90` | `104.09` | `103.08` | `103.45` | `4,485` | 463,964.28 USD | -168,609.15 USD | `-36.34%` | 235,832.98 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `104.72` | `103.46` | `104.45` | `4,423` | 461,973.50 USD | 311,329.97 USD | `+67.39%` | 547,162.95 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,724,296.99 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 3,306,037.16 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,333,125.39 USD | `300,817.26` | `98.89` | `104.14` | `30.60` | 1,583,624.35 USD | `+5.05%` | `3X Cross` |
| `111` | `0x30af...393e` | `LONG` | 18,512,304.56 USD | `177,712.44` | `100.98` | `104.14` | `93.19` | 566,902.67 USD | `+3.06%` | `10X Isolated` |
| `282` | `0x7fda...17d1` | `SHORT` | 8,189,572.40 USD | `78,647.58` | `100.15` | `104.14` | `208.99` | -312,950.55 USD | `-3.82%` | `20X Cross` |
| `323` | `0x10e1...f4bd` | `LONG` | 7,041,206.31 USD | `67,625.88` | `84.36` | `104.14` | `58.53` | 1,335,975.93 USD | `+18.97%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,744,557.85 USD | `55,151.29` | `89.22` | `104.14` | `234.22` | -823,833.35 USD | `-14.34%` | `20X Cross` |
| `489` | `0x5989...bc29` | `SHORT` | 4,549,181.78 USD | `43,691.72` | `99.48` | `104.14` | `113.23` | -202,874.88 USD | `-4.46%` | `10X Cross` |
| `504` | `0x354b...6425` | `SHORT` | 4,440,639.89 USD | `42,645.15` | `102.98` | `104.14` | `362.31` | -48,915.49 USD | `-1.10%` | `8X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,166,800.00 USD | `40,000.00` | `101.97` | `104.14` | `118.57` | -88,170.00 USD | `-2.12%` | `20X Cross` |
| `534` | `0xd507...c948` | `LONG` | 4,144,860.71 USD | `39,808.50` | `93.57` | `104.14` | `85.21` | 419,785.29 USD | `+10.13%` | `7X Isolated` |
| `561` | `0x4692...164f` | `SHORT` | 3,970,702.45 USD | `38,132.17` | `103.59` | `104.14` | `1791.82` | -20,529.56 USD | `-0.52%` | `5X Cross` |
| `689` | `0xb5e7...eff1` | `SHORT` | 3,243,050.44 USD | `31,132.29` | `91.71` | `104.14` | `144.67` | -387,841.80 USD | `-11.96%` | `20X Cross` |
| `719` | `0xbd33...4200` | `SHORT` | 3,123,297.34 USD | `29,982.69` | `104.89` | `104.14` | `403.27` | 21,587.54 USD | `+0.69%` | `20X Cross` |
| `778` | `0x61d7...7dee` | `LONG` | 2,900,583.81 USD | `27,858.08` | `88.25` | `104.14` | `83.50` | 442,107.81 USD | `+15.24%` | `20X Cross` |
| `864` | `0xf0ae...2f74` | `SHORT` | 2,604,000.00 USD | `25,000.00` | `100.78` | `104.14` | `175.21` | -84,481.39 USD | `-3.24%` | `20X Cross` |
| `865` | `0x645b...87b8` | `SHORT` | 2,592,079.06 USD | `24,895.11` | `101.26` | `104.14` | `134.75` | -71,123.60 USD | `-2.74%` | `3X Isolated` |
| `870` | `0x40f2...6a9e` | `LONG` | 2,566,809.76 USD | `24,652.42` | `103.40` | `104.14` | `101.30` | 17,744.24 USD | `+0.69%` | `20X Cross` |
| `1028` | `0xebe1...4070` | `LONG` | 2,083,197.50 USD | `19,999.98` | `101.87` | `104.14` | `0.000000` | 45,772.76 USD | `+2.20%` | `20X Cross` |
| `1051` | `0x9aa5...58af` | `SHORT` | 2,048,144.52 USD | `19,671.00` | `101.76` | `104.14` | `565.76` | -46,393.59 USD | `-2.27%` | `20X Cross` |
| `1228` | `0x4169...6f06` | `LONG` | 1,789,139.54 USD | `17,175.19` | `76.61` | `104.14` | `82.98` | 473,371.54 USD | `+26.46%` | `12X Isolated` |
| `1244` | `0x6788...98d4` | `SHORT` | 1,770,720.00 USD | `17,000.00` | `99.31` | `104.14` | `195.53` | -82,395.41 USD | `-4.65%` | `20X Cross` |
| `1287` | `0xa99c...40d5` | `SHORT` | 1,676,976.00 USD | `16,100.00` | `101.02` | `104.14` | `153.27` | -50,518.63 USD | `-3.01%` | `20X Cross` |
| `1296` | `0x1bf6...5bfa` | `SHORT` | 1,665,920.00 USD | `16,000.00` | `99.60` | `104.14` | `226.42` | -72,297.69 USD | `-4.34%` | `20X Cross` |
| `1348` | `0xfc27...9d9d` | `LONG` | 1,586,683.76 USD | `15,233.14` | `102.72` | `104.14` | `0.000000` | 21,990.70 USD | `+1.39%` | `20X Cross` |
| `1355` | `0xe5dd...ecba` | `SHORT` | 1,580,953.19 USD | `15,178.12` | `102.71` | `104.14` | `145.58` | -22,015.40 USD | `-1.39%` | `20X Cross` |
| `1361` | `0xce97...7e78` | `SHORT` | 1,573,446.89 USD | `15,110.41` | `103.16` | `104.14` | `120.79` | -14,609.15 USD | `-0.93%` | `5X Isolated` |
| `1370` | `0x34ea...2f47` | `SHORT` | 1,562,400.00 USD | `15,000.00` | `99.80` | `104.14` | `196.64` | -65,398.69 USD | `-4.19%` | `20X Cross` |
| `1371` | `0x5d6f...6f8a` | `LONG` | 1,562,400.00 USD | `15,000.00` | `101.91` | `104.14` | `24.48` | 33,745.00 USD | `+2.16%` | `20X Cross` |
| `1496` | `0xfb29...21dd` | `LONG` | 1,431,630.35 USD | `13,744.53` | `89.85` | `104.14` | `84.63` | 196,636.39 USD | `+13.74%` | `20X Cross` |
| `1522` | `0x6fa6...825e` | `SHORT` | 1,405,620.00 USD | `13,500.00` | `102.95` | `104.14` | `135.50` | -15,845.73 USD | `-1.13%` | `20X Isolated` |
| `1545` | `0xa9d9...b48e` | `SHORT` | 1,388,933.30 USD | `13,333.33` | `96.39` | `104.14` | `173.57` | -103,686.11 USD | `-7.47%` | `20X Cross` |
| `1600` | `0x936c...bb0f` | `SHORT` | 1,321,064.98 USD | `12,687.91` | `101.39` | `104.14` | `163.64` | -34,592.11 USD | `-2.62%` | `2X Isolated` |
| `1632` | `0x89c2...c94b` | `LONG` | 1,287,906.21 USD | `12,364.69` | `75.25` | `104.13` | `45.76` | 357,423.06 USD | `+27.75%` | `3X Isolated` |
| `1668` | `0xcd81...36e3` | `SHORT` | 1,256,582.49 USD | `12,063.96` | `97.96` | `104.13` | `109.81` | -74,743.57 USD | `-5.95%` | `20X Cross` |
| `1677` | `0x436c...b3d1` | `SHORT` | 1,249,440.00 USD | `12,000.00` | `101.05` | `104.13` | `218.60` | -36,780.17 USD | `-2.94%` | `20X Cross` |
| `1742` | `0x9dea...d617` | `LONG` | 1,187,051.09 USD | `11,400.80` | `90.37` | `104.13` | `4.77` | 156,777.36 USD | `+13.21%` | `20X Cross` |
| `1753` | `0x17c3...a868` | `LONG` | 1,177,695.14 USD | `11,306.60` | `95.13` | `104.13` | `64.99` | 102,048.28 USD | `+8.67%` | `3X Isolated` |
| `1805` | `0x8607...08d5` | `SHORT` | 1,145,122.38 USD | `10,998.10` | `92.18` | `104.13` | `135.02` | -131,332.68 USD | `-11.47%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.86%`)
  * 48H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.35%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.89%`)
  * 7D Horizon: Short MP=`105.22` (Vol: 4,800,000.00 USD, Dist: `+0.96%`) | Long MP=`99.12` (Vol: 8,000,000.00 USD, Dist: `--4.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-162.31K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0268%` | **USDT OKX** | `-0.0301%` |
| **USDT Bybit** | `-0.0619%` | **USDT KuCoin** | `-0.0221%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0458%` | **USDT Bitget** | `-0.0225%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `10:05:00` | `103.76` | `103.76` | `103.76` | `103.86` | `103.47` | 41,088.17 USD | 30,025.97 USD | 11,062.20 USD | 18,963.77 USD | `+46.15%` | `1B / 0S` |
| `10:10:00` | `103.75` | `103.75` | `103.75` | `103.78` | `103.64` | 31,331.90 USD | 20,597.82 USD | 10,734.08 USD | 9,863.75 USD | `+31.48%` | `1B / 0S` |
| `10:15:00` | `103.94` | `103.94` | `103.94` | `103.94` | `103.68` | 30,767.13 USD | 28,696.26 USD | 2,070.86 USD | 26,625.40 USD | `+86.54%` | `1B / 0S` |
| `10:15:00` | `104.11` | `104.11` | `104.11` | `104.18` | `103.68` | 102,650.49 USD | 88,134.26 USD | 14,516.23 USD | 73,618.03 USD | `+71.72%` | `1B / 0S` |
| `10:20:00` | `104.06` | `104.06` | `104.06` | `104.10` | `103.91` | 35,693.27 USD | 28,611.27 USD | 7,082.00 USD | 21,529.27 USD | `+60.32%` | `1B / 0S` |
| `10:25:00` | `104.11` | `104.11` | `104.11` | `104.18` | `103.99` | 36,125.48 USD | 22,456.38 USD | 13,669.10 USD | 8,787.28 USD | `+24.32%` | `1B / 0S` |
| `10:30:00` | `104.29` | `104.29` | `104.29` | `104.30` | `103.92` | 37,649.77 USD | 32,026.75 USD | 5,623.02 USD | 26,403.74 USD | `+70.13%` | `1B / 0S` |
| `10:30:00` | `104.35` | `104.35` | `104.35` | `104.42` | `103.92` | 115,408.89 USD | 91,750.07 USD | 23,658.82 USD | 68,091.24 USD | `+59.00%` | `1B / 0S` |
| `10:35:00` | `104.24` | `104.24` | `104.24` | `104.39` | `104.19` | 37,942.27 USD | 10,766.12 USD | 27,176.15 USD | -16,410.03 USD | `-43.25%` | `0B / 1S` |
| `10:40:00` | `104.35` | `104.35` | `104.35` | `104.42` | `104.24` | 39,756.59 USD | 27,897.38 USD | 11,859.21 USD | 16,038.17 USD | `+40.34%` | `1B / 0S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `104.13` | `104.11` | `104.13` | `104.23` | `103.91` | 11,480,392.01 USD | 6,191,179.30 USD | 5,289,212.71 USD | 901,966.59 USD | `+7.86%` | `6B / 4S` |
| `0:00 UTC` | `104.13` | `104.08` | `104.13` | `104.30` | `103.81` | 32,456,048.03 USD | 16,079,340.84 USD | 16,376,707.20 USD | -297,366.36 USD | `-0.92%` | `6B / 5S` |
| `5:00 UTC` | `104.27` | `104.27` | `104.27` | `104.38` | `104.16` | 6,725,440.32 USD | 3,224,158.80 USD | 3,501,281.52 USD | -277,122.71 USD | `-4.12%` | `3B / 5S` |
| `0:00 UTC` | `104.25` | `104.18` | `104.25` | `104.31` | `104.02` | 8,036,249.92 USD | 3,423,895.23 USD | 4,612,354.69 USD | -1,188,459.46 USD | `-14.79%` | `2B / 6S` |
| `5:00 UTC` | `104.22` | `104.22` | `104.22` | `104.28` | `104.18` | 1,418,356.54 USD | 485,340.92 USD | 933,015.63 USD | -447,674.71 USD | `-31.56%` | `3B / 3S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | WTI_OIL Macro Delta Flow: AGGRESSIVE BUY | `102.68` | 803,986.89 USD | 803,986.89 USD |
| `10-28 18:20` | `Volume 200K CL` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `102.21` | 51,000.00 USD | 0.00 USD |
| `10-28 11:54` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.96` | 0.00 USD | 0.00 USD |
| `10-28 07:12` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.50` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.58` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.31` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `106.75`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `106.21` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `101.76`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
