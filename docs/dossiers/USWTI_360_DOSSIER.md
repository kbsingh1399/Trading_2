# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 15:57:26 IST` (`2026-10-30 10:27:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.84` | **Live Ask Quote**: `104.89` | **Mid Price**: `104.86`
- **Spread Points**: `46.00` | **Spread BPS**: `4.39 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.86` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.60` | Lower -3.00σ Band: `104.13`
  * Upper +2.51σ Band: `105.44` | Lower -2.51σ Band: `104.29`
  * Upper +2.01σ Band: `105.30` | Lower -2.01σ Band: `104.42`
  * Upper +2.00σ Band: `105.28` | Lower -2.00σ Band: `104.44`
  * Upper +1.28σ Band: `105.16` | Lower -1.28σ Band: `104.57`
  * Upper +1.00σ Band: `105.07` | Lower -1.00σ Band: `104.65`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.86` | EMA-20=`104.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`104.86` (Slope: `+0.0000`) | EMA-100=`104.86`
  * Institutional Anchors: EMA-144=`104.86` | EMA-200=`104.86` (Slope: `+0.0000`) | EMA-233=`104.86`
- **Range Boundaries**: 24H High=`105.91` | 24H Low=`103.81` | Weekly High=`106.96` | Weekly Low=`102.77`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.94` (Distance: `-0.03%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.82%`)
  * Value Area Low (VAL) = `103.55` (Distance: `+1.32%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.40` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.92` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.92` | Low=`104.33`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.44` - `105.28`
  * Optimal Trade Entry (OTE 0.705): `105.07`
  * Structural Invalidation Anchor (0.786): `105.70`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.74` | `103.78` | `103.64` | `103.75` | `302` | 31,331.90 USD | 9,863.75 USD | `+31.48%` | 393,800.51 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.75` | `103.94` | `103.68` | `103.94` | `296` | 30,767.13 USD | 26,625.40 USD | `+86.54%` | 420,425.91 USD | `+0.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.95` | `104.10` | `103.91` | `104.06` | `343` | 35,693.27 USD | 21,529.27 USD | `+60.32%` | 441,955.18 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.51` | `103.61` | `103.36` | `103.45` | `925` | 95,689.40 USD | -24,879.24 USD | `-26.00%` | 520,708.14 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.46` | `103.86` | `103.46` | `103.75` | `1,084` | 112,462.83 USD | 64,562.00 USD | `+57.41%` | 585,270.13 USD | `+1.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.75` | `104.18` | `103.68` | `104.11` | `986` | 102,650.49 USD | 73,618.03 USD | `+71.72%` | 658,888.16 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,333,125.39 USD | `300,817.26` | `98.89` | `104.19` | `30.66` | 1,583,624.35 USD | `+5.05%` | `3X Cross` |
| `108` | `0x30af...393e` | `LONG` | 18,515,858.81 USD | `177,712.44` | `100.98` | `104.19` | `93.19` | 570,456.92 USD | `+3.08%` | `10X Isolated` |
| `284` | `0x7fda...17d1` | `SHORT` | 8,191,931.83 USD | `78,647.58` | `100.15` | `104.19` | `208.91` | -315,309.98 USD | `-3.85%` | `20X Cross` |
| `326` | `0x10e1...f4bd` | `LONG` | 7,045,940.12 USD | `67,625.88` | `84.36` | `104.19` | `58.53` | 1,340,709.74 USD | `+19.03%` | `3X Isolated` |
| `392` | `0xea00...a918` | `SHORT` | 5,746,212.38 USD | `55,151.29` | `89.22` | `104.19` | `226.80` | -825,487.89 USD | `-14.37%` | `20X Cross` |
| `485` | `0x5989...bc29` | `SHORT` | 4,552,240.20 USD | `43,691.72` | `99.48` | `104.19` | `113.23` | -205,933.30 USD | `-4.52%` | `10X Cross` |
| `492` | `0x354b...6425` | `SHORT` | 4,488,758.22 USD | `43,094.84` | `102.98` | `104.19` | `357.41` | -50,724.14 USD | `-1.13%` | `8X Cross` |
| `529` | `0xd84a...c8a5` | `SHORT` | 4,166,800.00 USD | `40,000.00` | `101.97` | `104.19` | `118.60` | -88,170.00 USD | `-2.12%` | `20X Cross` |
| `530` | `0xd507...c948` | `LONG` | 4,147,647.30 USD | `39,808.50` | `93.57` | `104.19` | `85.21` | 422,571.89 USD | `+10.19%` | `7X Isolated` |
| `549` | `0x4692...164f` | `SHORT` | 4,001,350.67 USD | `38,415.43` | `103.56` | `104.19` | `1776.95` | -22,943.57 USD | `-0.57%` | `5X Cross` |
| `685` | `0xb5e7...eff1` | `SHORT` | 3,243,050.44 USD | `31,132.29` | `91.71` | `104.19` | `144.48` | -387,841.80 USD | `-11.96%` | `20X Cross` |
| `714` | `0xbd33...4200` | `SHORT` | 3,123,896.99 USD | `29,982.69` | `104.89` | `104.19` | `403.27` | 20,987.89 USD | `+0.67%` | `20X Cross` |
| `780` | `0x61d7...7dee` | `LONG` | 2,902,255.30 USD | `27,858.08` | `88.25` | `104.19` | `83.50` | 443,779.29 USD | `+15.29%` | `20X Cross` |
| `859` | `0xf0ae...2f74` | `SHORT` | 2,604,250.00 USD | `25,000.00` | `100.78` | `104.19` | `175.77` | -84,731.39 USD | `-3.25%` | `20X Cross` |
| `861` | `0x645b...87b8` | `SHORT` | 2,593,323.82 USD | `24,895.11` | `101.26` | `104.19` | `134.75` | -72,368.36 USD | `-2.79%` | `3X Isolated` |
| `865` | `0x40f2...6a9e` | `LONG` | 2,568,535.43 USD | `24,652.42` | `103.40` | `104.19` | `101.25` | 19,469.91 USD | `+0.76%` | `20X Cross` |
| `1024` | `0xebe1...4070` | `LONG` | 2,083,597.50 USD | `19,999.98` | `101.87` | `104.19` | `0.000000` | 46,172.76 USD | `+2.22%` | `20X Cross` |
| `1044` | `0x9aa5...58af` | `SHORT` | 2,049,128.07 USD | `19,671.00` | `101.76` | `104.19` | `574.70` | -47,377.14 USD | `-2.31%` | `20X Cross` |
| `1225` | `0x4169...6f06` | `LONG` | 1,789,483.05 USD | `17,175.19` | `76.61` | `104.19` | `82.98` | 473,715.05 USD | `+26.47%` | `12X Isolated` |
| `1241` | `0x6788...98d4` | `SHORT` | 1,770,720.00 USD | `17,000.00` | `99.31` | `104.19` | `196.17` | -82,395.41 USD | `-4.65%` | `20X Cross` |
| `1288` | `0xa99c...40d5` | `SHORT` | 1,677,137.00 USD | `16,100.00` | `101.02` | `104.19` | `151.91` | -50,679.63 USD | `-3.02%` | `20X Cross` |
| `1295` | `0x1bf6...5bfa` | `SHORT` | 1,666,720.00 USD | `16,000.00` | `99.60` | `104.19` | `227.10` | -73,097.69 USD | `-4.39%` | `20X Cross` |
| `1312` | `0xce97...7e78` | `SHORT` | 1,642,978.09 USD | `15,772.08` | `103.16` | `104.19` | `120.78` | -15,990.14 USD | `-0.97%` | `5X Isolated` |
| `1350` | `0xfc27...9d9d` | `LONG` | 1,586,683.76 USD | `15,233.14` | `102.72` | `104.19` | `0.000000` | 21,990.70 USD | `+1.39%` | `20X Cross` |
| `1352` | `0xe5dd...ecba` | `SHORT` | 1,581,104.97 USD | `15,178.12` | `102.71` | `104.19` | `145.56` | -22,167.18 USD | `-1.40%` | `20X Cross` |
| `1368` | `0x5d6f...6f8a` | `LONG` | 1,562,850.00 USD | `15,000.00` | `101.91` | `104.19` | `24.73` | 34,195.00 USD | `+2.19%` | `20X Cross` |
| `1369` | `0x34ea...2f47` | `SHORT` | 1,562,400.00 USD | `15,000.00` | `99.80` | `104.19` | `197.88` | -65,398.69 USD | `-4.19%` | `20X Cross` |
| `1497` | `0xfb29...21dd` | `LONG` | 1,432,042.68 USD | `13,744.53` | `89.85` | `104.19` | `84.68` | 197,048.72 USD | `+13.76%` | `20X Cross` |
| `1522` | `0x6fa6...825e` | `SHORT` | 1,406,565.00 USD | `13,500.00` | `102.95` | `104.19` | `135.50` | -16,790.73 USD | `-1.19%` | `20X Isolated` |
| `1540` | `0xa9d9...b48e` | `SHORT` | 1,388,933.30 USD | `13,333.33` | `96.39` | `104.19` | `173.27` | -103,686.11 USD | `-7.47%` | `20X Cross` |
| `1595` | `0x936c...bb0f` | `SHORT` | 1,321,572.50 USD | `12,687.91` | `101.39` | `104.19` | `163.64` | -35,099.63 USD | `-2.66%` | `2X Isolated` |
| `1627` | `0x89c2...c94b` | `LONG` | 1,288,029.86 USD | `12,364.69` | `75.25` | `104.19` | `45.76` | 357,546.71 USD | `+27.76%` | `3X Isolated` |
| `1662` | `0xcd81...36e3` | `SHORT` | 1,256,944.41 USD | `12,063.96` | `97.96` | `104.19` | `109.36` | -75,105.49 USD | `-5.98%` | `20X Cross` |
| `1673` | `0x436c...b3d1` | `SHORT` | 1,250,280.00 USD | `12,000.00` | `101.05` | `104.19` | `220.07` | -37,620.17 USD | `-3.01%` | `20X Cross` |
| `1738` | `0x9dea...d617` | `LONG` | 1,187,621.13 USD | `11,400.80` | `90.37` | `104.19` | `6.04` | 157,347.40 USD | `+13.25%` | `20X Cross` |
| `1747` | `0x17c3...a868` | `LONG` | 1,178,034.34 USD | `11,306.60` | `95.13` | `104.19` | `64.99` | 102,387.47 USD | `+8.69%` | `3X Isolated` |
| `1793` | `0x8607...08d5` | `SHORT` | 1,145,672.29 USD | `10,998.10` | `92.18` | `104.19` | `135.02` | -131,882.58 USD | `-11.51%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.97%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.84%`)
  * 48H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.97%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.27%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.37%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.87%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+1.33%`) | Long MP=`99.12` (Vol: 8,000,000.00 USD, Dist: `--4.87%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.66` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.47` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-166.80K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0276%` | **USDT OKX** | `-0.0312%` |
| **USDT Bybit** | `-0.0657%` | **USDT KuCoin** | `-0.0236%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0483%` | **USDT Bitget** | `-0.0233%` |
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
| `09:40:00` | `103.50` | `103.50` | `103.50` | `103.50` | `103.29` | 30,842.40 USD | 29,051.79 USD | 1,790.61 USD | 27,261.18 USD | `+88.39%` | `1B / 0S` |
| `09:45:00` | `103.58` | `103.58` | `103.58` | `103.61` | `103.50` | 37,598.81 USD | 29,053.63 USD | 8,545.18 USD | 20,508.44 USD | `+54.55%` | `1B / 0S` |
| `09:45:00` | `103.45` | `103.45` | `103.45` | `103.61` | `103.36` | 95,689.40 USD | 35,405.08 USD | 60,284.32 USD | -24,879.24 USD | `-26.00%` | `0B / 1S` |
| `09:50:00` | `103.50` | `103.50` | `103.50` | `103.59` | `103.44` | 29,496.93 USD | 9,154.22 USD | 20,342.71 USD | -11,188.49 USD | `-37.93%` | `0B / 1S` |
| `09:55:00` | `103.45` | `103.45` | `103.45` | `103.51` | `103.36` | 28,655.10 USD | 12,894.79 USD | 15,760.30 USD | -2,865.51 USD | `-10.00%` | `0B / 1S` |
| `10:00:00` | `103.75` | `103.75` | `103.75` | `103.86` | `103.46` | 112,462.83 USD | 88,512.41 USD | 23,950.42 USD | 64,562.00 USD | `+57.41%` | `1B / 0S` |
| `10:00:00` | `104.45` | `104.45` | `104.45` | `104.72` | `103.46` | 461,973.50 USD | 386,651.74 USD | 75,321.77 USD | 311,329.97 USD | `+67.39%` | `1B / 0S` |
| `10:00:00` | `103.58` | `103.58` | `103.58` | `103.61` | `103.46` | 39,981.11 USD | 33,983.94 USD | 5,997.17 USD | 27,986.78 USD | `+70.00%` | `1B / 0S` |
| `10:05:00` | `103.76` | `103.76` | `103.76` | `103.86` | `103.47` | 41,088.17 USD | 30,025.97 USD | 11,062.20 USD | 18,963.77 USD | `+46.15%` | `1B / 0S` |
| `10:10:00` | `103.75` | `103.75` | `103.75` | `103.78` | `103.64` | 31,331.90 USD | 20,597.82 USD | 10,734.08 USD | 9,863.75 USD | `+31.48%` | `1B / 0S` |
| `0:00 UTC` | `104.00` | `103.97` | `104.00` | `104.09` | `103.80` | 12,864,820.33 USD | 5,029,660.97 USD | 7,835,159.36 USD | -2,805,498.39 USD | `-21.81%` | `3B / 7S` |
| `5:00 UTC` | `103.66` | `103.71` | `103.66` | `103.91` | `103.53` | 12,894,660.60 USD | 5,121,489.28 USD | 7,773,171.32 USD | -2,651,682.04 USD | `-20.56%` | `1B / 7S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `104.13` | `104.11` | `104.13` | `104.23` | `103.91` | 11,480,392.01 USD | 6,191,179.30 USD | 5,289,212.71 USD | 901,966.59 USD | `+7.86%` | `6B / 4S` |
| `0:00 UTC` | `104.13` | `104.08` | `104.13` | `104.30` | `103.81` | 32,456,048.03 USD | 16,079,340.84 USD | 16,376,707.20 USD | -297,366.36 USD | `-0.92%` | `6B / 5S` |
| `5:00 UTC` | `104.27` | `104.25` | `104.27` | `104.28` | `104.20` | 984,835.01 USD | 432,612.15 USD | 552,222.86 USD | -119,610.71 USD | `-12.15%` | `0B / 3S` |

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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.28` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `106.72`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `106.21` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `101.76`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.70`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
