# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.17` | **Live Ask Quote**: `104.20` | **Mid Price**: `104.19`
- **Spread Points**: `32.00` | **Spread BPS**: `3.07 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.08` | VWAP Z-Score: `+0.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3657` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.71` | Lower -3.00σ Band: `102.45`
  * Upper +2.51σ Band: `105.44` | Lower -2.51σ Band: `102.71`
  * Upper +2.01σ Band: `105.17` | Lower -2.01σ Band: `102.99`
  * Upper +2.00σ Band: `105.17` | Lower -2.00σ Band: `102.99`
  * Upper +1.28σ Band: `104.78` | Lower -1.28σ Band: `103.38`
  * Upper +1.00σ Band: `104.62` | Lower -1.00σ Band: `103.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.18` | EMA-20=`104.00` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.63` (Slope: `+0.0000`) | EMA-100=`103.20`
  * Institutional Anchors: EMA-144=`102.95` | EMA-200=`102.73` (Slope: `+0.1600`) | EMA-233=`102.66`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.61` (Distance: `-0.43%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.10%`)
  * Value Area Low (VAL) = `103.38` (Distance: `+0.76%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.33` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.72` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.81` | Low=`103.56`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.77` - `104.60`
  * Optimal Trade Entry (OTE 0.705): `104.40`
  * Structural Invalidation Anchor (0.786): `105.02`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.59` | `103.87` | `103.52` | `103.82` | `348` | 36,130.75 USD | 25,414.00 USD | `+70.34%` | 392,005.26 USD | `+2.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.83` | `103.85` | `103.72` | `103.77` | `296` | 30,715.92 USD | -10,476.75 USD | `-34.11%` | 381,528.51 USD | `-1.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `103.78` | `103.98` | `103.76` | `103.93` | `277` | 28,788.61 USD | 16,953.29 USD | `+58.89%` | 398,481.80 USD | `+1.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.55` | `103.65` | `103.51` | `103.57` | `418` | 43,292.26 USD | 908.23 USD | `+2.10%` | 653,674.47 USD | `+0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `103.56` | `103.66` | `103.52` | `103.60` | `330` | 34,188.00 USD | 7,936.50 USD | `+23.21%` | 661,610.97 USD | `+0.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.59` | `103.98` | `103.52` | `103.93` | `921` | 95,719.53 USD | 71,280.50 USD | `+74.47%` | 732,891.47 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.00` | `104.13` | `103.75` | `103.82` | `2,020` | 209,716.40 USD | -114,516.19 USD | `-54.61%` | 683,818.49 USD | `-0.47` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.83` | `103.95` | `103.45` | `103.55` | `1,077` | 111,525.50 USD | -64,177.65 USD | `-57.55%` | 619,640.84 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.55` | `104.12` | `103.51` | `103.92` | `2,479` | 257,617.68 USD | 123,135.37 USD | `+47.80%` | 742,776.20 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.52` | `15,739` | 1,645,008.80 USD | 1,104,204.63 USD | `+67.12%` | 3,808,900.87 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,724,296.99 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 3,306,037.16 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.52` | `15,739` | 1,645,008.80 USD | 1,104,204.63 USD | `+67.12%` | 3,808,900.87 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `38` | `0x0cc1...c7cb` | `LONG` | 31,212,798.48 USD | `300,817.26` | `98.89` | `103.68` | `30.96` | 1,463,297.45 USD | `+4.69%` | `3X Cross` |
| `106` | `0x30af...393e` | `LONG` | 18,434,111.09 USD | `177,712.44` | `100.98` | `103.68` | `93.19` | 488,709.20 USD | `+2.65%` | `10X Isolated` |
| `290` | `0x7fda...17d1` | `SHORT` | 8,157,326.89 USD | `78,647.58` | `100.15` | `103.68` | `209.93` | -280,705.05 USD | `-3.44%` | `20X Cross` |
| `331` | `0x10e1...f4bd` | `LONG` | 7,020,242.29 USD | `67,625.88` | `84.36` | `103.68` | `58.53` | 1,315,011.91 USD | `+18.73%` | `3X Isolated` |
| `399` | `0xea00...a918` | `SHORT` | 5,721,945.82 USD | `55,151.29` | `89.22` | `103.68` | `229.35` | -801,221.32 USD | `-14.00%` | `20X Cross` |
| `483` | `0x354b...6425` | `SHORT` | 4,651,040.14 USD | `44,842.27` | `102.97` | `103.68` | `345.64` | -33,558.43 USD | `-0.72%` | `8X Cross` |
| `497` | `0x5989...bc29` | `SHORT` | 4,533,015.85 USD | `43,691.72` | `99.48` | `103.68` | `113.23` | -186,708.94 USD | `-4.12%` | `10X Cross` |
| `538` | `0x4692...164f` | `SHORT` | 4,222,420.77 USD | `40,709.80` | `103.40` | `103.68` | `1664.00` | -12,966.49 USD | `-0.31%` | `5X Cross` |
| `546` | `0xd84a...c8a5` | `SHORT` | 4,149,200.00 USD | `40,000.00` | `101.97` | `103.68` | `118.83` | -70,570.00 USD | `-1.70%` | `20X Cross` |
| `547` | `0xd507...c948` | `LONG` | 4,129,335.39 USD | `39,808.50` | `93.57` | `103.68` | `82.63` | 404,259.98 USD | `+9.79%` | `7X Isolated` |
| `704` | `0xb5e7...eff1` | `SHORT` | 3,229,352.23 USD | `31,132.29` | `91.71` | `103.68` | `144.50` | -374,143.59 USD | `-11.59%` | `20X Cross` |
| `742` | `0xbd33...4200` | `SHORT` | 3,110,104.95 USD | `29,982.69` | `104.89` | `103.68` | `403.27` | 34,779.93 USD | `+1.12%` | `20X Cross` |
| `797` | `0x61d7...7dee` | `LONG` | 2,889,719.16 USD | `27,858.08` | `88.25` | `103.68` | `83.50` | 431,243.16 USD | `+14.92%` | `20X Cross` |
| `880` | `0xf0ae...2f74` | `SHORT` | 2,593,250.00 USD | `25,000.00` | `100.78` | `103.68` | `175.45` | -73,731.39 USD | `-2.84%` | `20X Cross` |
| `884` | `0x645b...87b8` | `SHORT` | 2,582,369.97 USD | `24,895.11` | `101.26` | `103.68` | `134.75` | -61,414.51 USD | `-2.38%` | `3X Isolated` |
| `910` | `0x40f2...6a9e` | `LONG` | 2,496,205.50 USD | `24,064.45` | `103.38` | `103.68` | `101.11` | 8,346.85 USD | `+0.33%` | `20X Cross` |
| `1026` | `0xebe1...4070` | `LONG` | 2,178,957.51 USD | `20,999.98` | `101.87` | `103.68` | `0.000000` | 39,661.41 USD | `+1.82%` | `20X Cross` |
| `1077` | `0x9aa5...58af` | `SHORT` | 2,042,046.51 USD | `19,671.00` | `101.76` | `103.68` | `579.44` | -40,295.58 USD | `-1.97%` | `20X Cross` |
| `1253` | `0x4169...6f06` | `LONG` | 1,781,582.46 USD | `17,175.19` | `76.61` | `103.68` | `82.98` | 465,814.46 USD | `+26.15%` | `12X Isolated` |
| `1266` | `0x6788...98d4` | `SHORT` | 1,763,750.00 USD | `17,000.00` | `99.31` | `103.68` | `196.99` | -75,425.41 USD | `-4.28%` | `20X Cross` |
| `1309` | `0xa99c...40d5` | `SHORT` | 1,670,536.00 USD | `16,100.00` | `101.02` | `103.68` | `152.13` | -44,078.63 USD | `-2.64%` | `20X Cross` |
| `1318` | `0x1bf6...5bfa` | `SHORT` | 1,659,680.00 USD | `16,000.00` | `99.60` | `103.68` | `226.26` | -66,057.69 USD | `-3.98%` | `20X Cross` |
| `1366` | `0xce97...7e78` | `SHORT` | 1,578,818.83 USD | `15,220.47` | `103.04` | `103.68` | `120.64` | -10,529.58 USD | `-0.67%` | `5X Isolated` |
| `1370` | `0xe5dd...ecba` | `SHORT` | 1,575,640.84 USD | `15,178.12` | `102.71` | `103.68` | `146.06` | -16,703.06 USD | `-1.06%` | `20X Cross` |
| `1405` | `0x5d6f...6f8a` | `LONG` | 1,557,150.00 USD | `15,000.00` | `101.91` | `103.68` | `25.60` | 28,495.00 USD | `+1.83%` | `20X Cross` |
| `1409` | `0x34ea...2f47` | `SHORT` | 1,556,250.00 USD | `15,000.00` | `99.80` | `103.68` | `198.04` | -59,248.69 USD | `-3.81%` | `20X Cross` |
| `1417` | `0xfc27...9d9d` | `LONG` | 1,541,756.21 USD | `14,864.60` | `102.69` | `103.68` | `0.000000` | 15,353.76 USD | `+1.00%` | `20X Cross` |
| `1520` | `0xfb29...21dd` | `LONG` | 1,426,957.21 USD | `13,744.53` | `89.85` | `103.68` | `84.70` | 191,963.25 USD | `+13.45%` | `20X Cross` |
| `1548` | `0x6fa6...825e` | `SHORT` | 1,400,355.00 USD | `13,500.00` | `102.95` | `103.68` | `135.50` | -10,580.73 USD | `-0.76%` | `20X Isolated` |
| `1560` | `0xa9d9...b48e` | `SHORT` | 1,384,133.30 USD | `13,333.33` | `96.39` | `103.68` | `173.42` | -98,886.11 USD | `-7.14%` | `20X Cross` |
| `1627` | `0x936c...bb0f` | `SHORT` | 1,316,370.46 USD | `12,687.91` | `101.39` | `103.68` | `163.64` | -29,897.58 USD | `-2.27%` | `2X Isolated` |
| `1665` | `0x89c2...c94b` | `LONG` | 1,282,960.34 USD | `12,364.69` | `75.25` | `103.68` | `45.76` | 352,477.19 USD | `+27.47%` | `3X Isolated` |
| `1701` | `0xcd81...36e3` | `SHORT` | 1,251,636.26 USD | `12,063.96` | `97.96` | `103.68` | `108.92` | -69,797.34 USD | `-5.58%` | `20X Cross` |
| `1714` | `0x436c...b3d1` | `SHORT` | 1,245,000.00 USD | `12,000.00` | `101.05` | `103.68` | `220.33` | -32,340.17 USD | `-2.60%` | `20X Cross` |
| `1768` | `0x9dea...d617` | `LONG` | 1,182,604.78 USD | `11,400.80` | `90.37` | `103.68` | `3.60` | 152,331.05 USD | `+12.88%` | `20X Cross` |
| `1778` | `0x17c3...a868` | `LONG` | 1,173,850.90 USD | `11,306.60` | `95.13` | `103.68` | `64.99` | 98,204.03 USD | `+8.37%` | `3X Isolated` |
| `1826` | `0x8607...08d5` | `SHORT` | 1,140,833.12 USD | `10,998.10` | `92.18` | `103.68` | `135.02` | -127,043.42 USD | `-11.14%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 4,100,000.00 USD, Dist: `+1.91%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.52%`)
  * 48H Horizon: Short MP=`104.86` (Vol: 2,600,000.00 USD, Dist: `+0.97%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--1.95%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+1.93%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.55%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+1.67%`) | Long MP=`99.12` (Vol: 8,800,000.00 USD, Dist: `--4.55%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.38` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.23` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-203.24K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0358%` | **USDT OKX** | `-0.0292%` |
| **USDT Bybit** | `-0.0851%` | **USDT KuCoin** | `-0.0270%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0454%` | **USDT Bitget** | `-0.0243%` |
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
| `08:05:00` | `103.57` | `103.57` | `103.57` | `103.65` | `103.56` | 12,531.97 USD | 1,740.55 USD | 10,791.42 USD | -9,050.87 USD | `-72.22%` | `0B / 1S` |
| `08:10:00` | `103.57` | `103.57` | `103.57` | `103.61` | `103.55` | 11,703.41 USD | 5,401.57 USD | 6,301.84 USD | -900.26 USD | `-7.69%` | `0B / 1S` |
| `08:15:00` | `103.60` | `103.60` | `103.60` | `103.66` | `103.52` | 34,188.00 USD | 21,062.25 USD | 13,125.75 USD | 7,936.50 USD | `+23.21%` | `1B / 0S` |
| `08:15:00` | `103.52` | `103.52` | `103.52` | `103.58` | `103.52` | 10,144.96 USD | 780.38 USD | 9,364.58 USD | -8,584.20 USD | `-84.62%` | `0B / 1S` |
| `08:20:00` | `103.59` | `103.59` | `103.59` | `103.59` | `103.52` | 11,602.08 USD | 11,021.98 USD | 580.10 USD | 10,441.87 USD | `+90.00%` | `1B / 0S` |
| `08:25:00` | `103.60` | `103.60` | `103.60` | `103.66` | `103.58` | 12,432.00 USD | 5,106.00 USD | 7,326.00 USD | -2,220.00 USD | `-17.86%` | `0B / 1S` |
| `08:30:00` | `103.82` | `103.82` | `103.82` | `103.87` | `103.52` | 36,130.75 USD | 30,772.38 USD | 5,358.37 USD | 25,414.00 USD | `+70.34%` | `1B / 0S` |
| `08:30:00` | `103.93` | `103.93` | `103.93` | `103.98` | `103.52` | 95,719.53 USD | 83,500.02 USD | 12,219.51 USD | 71,280.50 USD | `+74.47%` | `1B / 0S` |
| `08:35:00` | `103.77` | `103.77` | `103.77` | `103.85` | `103.72` | 30,715.92 USD | 10,119.59 USD | 20,596.33 USD | -10,476.75 USD | `-34.11%` | `0B / 1S` |
| `08:40:00` | `103.93` | `103.93` | `103.93` | `103.98` | `103.76` | 28,788.61 USD | 22,870.95 USD | 5,917.66 USD | 16,953.29 USD | `+58.89%` | `1B / 0S` |
| `0:00 UTC` | `102.66` | `102.70` | `102.66` | `103.00` | `102.55` | 55,717,494.76 USD | 35,444,287.30 USD | 20,273,207.46 USD | 15,171,079.85 USD | `+27.23%` | `8B / 8S` |
| `5:00 UTC` | `103.00` | `102.96` | `103.00` | `103.12` | `102.84` | 8,335,847.24 USD | 3,078,570.11 USD | 5,257,277.13 USD | -2,178,707.03 USD | `-26.14%` | `4B / 5S` |
| `0:00 UTC` | `103.22` | `103.18` | `103.22` | `103.38` | `102.91` | 7,833,614.37 USD | 4,518,281.07 USD | 3,315,333.30 USD | 1,202,947.77 USD | `+15.36%` | `10B / 7S` |
| `5:00 UTC` | `103.57` | `103.51` | `103.57` | `103.68` | `103.16` | 13,871,996.58 USD | 7,371,562.11 USD | 6,500,434.46 USD | 871,127.65 USD | `+6.28%` | `13B / 5S` |
| `0:00 UTC` | `103.81` | `103.77` | `103.81` | `103.93` | `103.44` | 11,322,481.70 USD | 6,201,023.76 USD | 5,121,457.94 USD | 1,079,565.82 USD | `+9.53%` | `13B / 8S` |
| `5:00 UTC` | `103.97` | `104.00` | `103.97` | `104.22` | `103.69` | 15,722,195.08 USD | 7,756,867.01 USD | 7,965,328.07 USD | -208,461.06 USD | `-1.33%` | `8B / 12S` |
| `0:00 UTC` | `104.00` | `103.97` | `104.00` | `104.09` | `103.80` | 12,864,820.33 USD | 5,029,660.97 USD | 7,835,159.36 USD | -2,805,498.39 USD | `-21.81%` | `3B / 7S` |
| `5:00 UTC` | `103.66` | `103.71` | `103.66` | `103.91` | `103.53` | 12,894,660.60 USD | 5,121,489.28 USD | 7,773,171.32 USD | -2,651,682.04 USD | `-20.56%` | `1B / 7S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.82` | `103.81` | `103.82` | `103.91` | `103.69` | 1,421,913.90 USD | 709,976.49 USD | 711,937.41 USD | -1,960.91 USD | `-0.14%` | `4B / 4S` |

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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.38` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.89` (Risk Distance: `0.4868` pts)
  * +2.5R Take Profit: `104.59`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.49 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.10` (Risk Distance: `0.4868` pts)
  * +2.5R Take Profit: `103.40`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.49 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.02`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
