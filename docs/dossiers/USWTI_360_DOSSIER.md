# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.49` | **Live Ask Quote**: `102.52` | **Mid Price**: `102.51`
- **Spread Points**: `30.00` | **Spread BPS**: `2.93 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.83` | VWAP Z-Score: `+0.27` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4306` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.74` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.47` | Lower -3.00σ Band: `100.20`
  * Upper +2.51σ Band: `103.20` | Lower -2.51σ Band: `100.46`
  * Upper +2.01σ Band: `102.93` | Lower -2.01σ Band: `100.74`
  * Upper +2.00σ Band: `102.92` | Lower -2.00σ Band: `100.74`
  * Upper +1.28σ Band: `102.53` | Lower -1.28σ Band: `101.13`
  * Upper +1.00σ Band: `102.38` | Lower -1.00σ Band: `101.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`101.56` | EMA-20=`101.57` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`101.83` (Slope: `+0.0000`) | EMA-100=`102.04`
  * Institutional Anchors: EMA-144=`102.12` | EMA-200=`102.10` (Slope: `-0.0896`) | EMA-233=`102.03`
- **Range Boundaries**: 24H High=`104.23` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.71` (Distance: `-0.19%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.48%`)
  * Value Area Low (VAL) = `101.48` (Distance: `+1.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.03` | Weekly POC=`102.03` | Weekly VAL=`101.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `102.10` - `102.92`
  * Optimal Trade Entry (OTE 0.705): `102.71`
  * Structural Invalidation Anchor (0.786): `103.33`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.16` | `101.59` | `101.15` | `101.56` | `867` | 88,049.92 USD | 78,435.27 USD | `+89.08%` | 71,405.41 USD | `+1.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.55` | `101.65` | `101.44` | `101.56` | `679` | 68,957.20 USD | 4,738.77 USD | `+6.87%` | 76,144.18 USD | `+0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `101.55` | `101.85` | `101.55` | `101.71` | `843` | 85,738.16 USD | 24,578.27 USD | `+28.67%` | 100,722.45 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.07` | `101.15` | `100.55` | `100.72` | `2,711` | 273,057.34 USD | -134,256.98 USD | `-49.17%` | -17,428.78 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `100.72` | `101.19` | `100.46` | `101.17` | `2,459` | 248,769.65 USD | 194,585.58 USD | `+78.22%` | 177,156.80 USD | `+2.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.16` | `101.85` | `101.15` | `101.71` | `2,389` | 242,975.63 USD | 168,160.12 USD | `+69.21%` | 345,316.91 USD | `+1.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.68` | `102.69` | `101.88` | `101.97` | `4,809` | 490,368.92 USD | -410,972.96 USD | `-83.81%` | -614,050.18 USD | `-1.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.97` | `101.98` | `100.46` | `101.17` | `10,331` | 1,045,156.28 USD | -311,556.76 USD | `-29.81%` | -925,606.94 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.16` | `101.85` | `100.81` | `100.95` | `8,946` | 903,080.81 USD | -425,750.58 USD | `-47.14%` | -1,351,357.52 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -2,178,472.68 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -2,041,170.88 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | -454,175.69 USD | `+2.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.70` | `102.95` | `102.42` | `102.61` | `2,667` | 273,647.54 USD | -65,371.36 USD | `-23.89%` | -687,419.76 USD | `+1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,649,056.31 USD | `-1.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -2,178,472.68 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -2,041,170.88 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | -454,175.69 USD | `+2.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 30,623,196.66 USD | `300,817.26` | `98.89` | `101.80` | `32.41` | 873,695.63 USD | `+2.85%` | `3X Cross` |
| `114` | `0x30af...393e` | `LONG` | 18,094,680.34 USD | `177,712.44` | `100.98` | `101.80` | `93.19` | 149,278.45 USD | `+0.82%` | `10X Isolated` |
| `168` | `0x58f0...0d20` | `SHORT` | 12,854,582.93 USD | `126,260.51` | `96.77` | `101.80` | `105.18` | -636,490.51 USD | `-4.95%` | `20X Cross` |
| `175` | `0xebe1...4070` | `LONG` | 12,215,995.42 USD | `119,999.96` | `101.87` | `101.80` | `6.05` | -8,596.62 USD | `-0.07%` | `20X Cross` |
| `228` | `0x9e2c...5508` | `LONG` | 10,182,000.00 USD | `100,000.00` | `100.89` | `101.80` | `79.61` | 92,761.86 USD | `+0.91%` | `20X Cross` |
| `315` | `0x7fda...17d1` | `SHORT` | 8,018,073.91 USD | `78,763.01` | `100.15` | `101.80` | `193.64` | -129,892.05 USD | `-1.62%` | `20X Cross` |
| `352` | `0x10e1...f4bd` | `LONG` | 6,885,666.80 USD | `67,625.88` | `84.36` | `101.80` | `58.54` | 1,180,436.41 USD | `+17.14%` | `3X Isolated` |
| `406` | `0x4692...164f` | `SHORT` | 6,045,237.73 USD | `59,377.64` | `100.97` | `101.80` | `1074.44` | -50,117.58 USD | `-0.83%` | `5X Cross` |
| `422` | `0x0c4a...1b19` | `SHORT` | 5,681,855.66 USD | `55,802.94` | `102.08` | `101.80` | `106.83` | 14,791.73 USD | `+0.26%` | `20X Isolated` |
| `435` | `0xea00...a918` | `SHORT` | 5,615,503.84 USD | `55,151.29` | `89.22` | `101.80` | `286.11` | -694,779.34 USD | `-12.37%` | `20X Cross` |
| `575` | `0x5989...bc29` | `SHORT` | 4,132,642.91 USD | `40,591.72` | `99.23` | `101.80` | `111.59` | -104,708.23 USD | `-2.53%` | `10X Cross` |
| `584` | `0xd507...c948` | `LONG` | 4,053,301.16 USD | `39,808.50` | `93.57` | `101.80` | `81.35` | 328,225.75 USD | `+8.10%` | `7X Isolated` |
| `585` | `0x354b...6425` | `SHORT` | 4,050,983.96 USD | `39,789.65` | `100.80` | `101.80` | `371.50` | -40,142.59 USD | `-0.99%` | `8X Cross` |
| `746` | `0xb5e7...eff1` | `SHORT` | 3,169,889.56 USD | `31,132.29` | `91.71` | `101.80` | `145.88` | -314,680.92 USD | `-9.93%` | `20X Cross` |
| `783` | `0xd84a...c8a5` | `SHORT` | 3,054,600.00 USD | `30,000.00` | `101.76` | `101.80` | `126.46` | -1,750.00 USD | `-0.06%` | `20X Cross` |
| `841` | `0x61d7...7dee` | `LONG` | 2,836,510.21 USD | `27,858.08` | `88.25` | `101.80` | `83.50` | 378,034.21 USD | `+13.33%` | `20X Cross` |
| `919` | `0xf0ae...2f74` | `SHORT` | 2,545,500.00 USD | `25,000.00` | `100.78` | `101.80` | `172.34` | -25,981.39 USD | `-1.02%` | `20X Cross` |
| `932` | `0xb8f3...04ea` | `SHORT` | 2,500,731.38 USD | `24,560.32` | `102.91` | `101.80` | `114.77` | 26,775.62 USD | `+1.07%` | `7X Isolated` |
| `941` | `0x645b...87b8` | `SHORT` | 2,474,272.55 USD | `24,302.84` | `101.22` | `101.80` | `134.77` | -14,310.99 USD | `-0.58%` | `3X Isolated` |
| `1142` | `0x9aa5...58af` | `SHORT` | 2,002,901.22 USD | `19,671.00` | `101.76` | `101.80` | `468.51` | -1,150.29 USD | `-0.06%` | `20X Cross` |
| `1315` | `0x4169...6f06` | `LONG` | 1,748,777.85 USD | `17,175.19` | `76.61` | `101.80` | `82.99` | 433,009.85 USD | `+24.76%` | `12X Isolated` |
| `1323` | `0x6788...98d4` | `SHORT` | 1,731,790.00 USD | `17,000.00` | `99.31` | `101.80` | `189.78` | -43,465.41 USD | `-2.51%` | `20X Cross` |
| `1349` | `0xfc66...ca06` | `SHORT` | 1,700,157.45 USD | `16,702.60` | `100.71` | `101.80` | `2552.94` | -18,023.15 USD | `-1.06%` | `3X Cross` |
| `1391` | `0xa99c...40d5` | `SHORT` | 1,639,624.00 USD | `16,100.00` | `101.02` | `101.80` | `158.35` | -13,166.63 USD | `-0.80%` | `20X Cross` |
| `1402` | `0x1bf6...5bfa` | `SHORT` | 1,629,120.00 USD | `16,000.00` | `99.60` | `101.80` | `222.33` | -35,497.69 USD | `-2.18%` | `20X Cross` |
| `1455` | `0xe1d3...7766` | `SHORT` | 1,581,465.62 USD | `15,530.45` | `101.33` | `101.80` | `168.27` | -7,788.09 USD | `-0.49%` | `20X Cross` |
| `1489` | `0x91fd...9841` | `LONG` | 1,541,043.46 USD | `15,134.98` | `101.16` | `101.80` | `95.58` | 9,967.96 USD | `+0.65%` | `13X Isolated` |
| `1502` | `0x17c3...a868` | `LONG` | 1,528,712.60 USD | `15,010.92` | `95.13` | `101.80` | `64.99` | 100,656.53 USD | `+6.58%` | `3X Isolated` |
| `1504` | `0x34ea...2f47` | `SHORT` | 1,527,600.00 USD | `15,000.00` | `99.80` | `101.80` | `191.00` | -30,598.69 USD | `-2.00%` | `20X Cross` |
| `1617` | `0xfb29...21dd` | `LONG` | 1,399,605.59 USD | `13,744.53` | `89.85` | `101.80` | `84.51` | 164,611.63 USD | `+11.76%` | `20X Cross` |
| `1637` | `0x6fa6...825e` | `SHORT` | 1,374,435.00 USD | `13,500.00` | `102.95` | `101.80` | `135.50` | 15,339.27 USD | `+1.12%` | `20X Isolated` |
| `1647` | `0xa9d9...b48e` | `SHORT` | 1,357,599.97 USD | `13,333.33` | `96.39` | `101.80` | `176.25` | -72,352.78 USD | `-5.33%` | `20X Cross` |
| `1743` | `0x89c2...c94b` | `LONG` | 1,258,725.54 USD | `12,364.69` | `75.25` | `101.80` | `45.77` | 328,242.39 USD | `+26.08%` | `3X Isolated` |
| `1771` | `0xcd81...36e3` | `SHORT` | 1,228,352.81 USD | `12,063.96` | `97.96` | `101.80` | `111.99` | -46,513.89 USD | `-3.79%` | `20X Cross` |
| `1776` | `0xfc27...9d9d` | `LONG` | 1,225,689.10 USD | `12,040.17` | `101.55` | `101.80` | `0.000000` | 3,023.23 USD | `+0.25%` | `20X Cross` |
| `1780` | `0x436c...b3d1` | `SHORT` | 1,221,720.00 USD | `12,000.00` | `101.05` | `101.80` | `200.11` | -9,060.17 USD | `-0.74%` | `20X Cross` |
| `1786` | `0xfdfb...dbb9` | `SHORT` | 1,215,193.88 USD | `11,932.38` | `100.90` | `101.80` | `110.95` | -11,211.26 USD | `-0.92%` | `20X Cross` |
| `1852` | `0x9dea...d617` | `LONG` | 1,160,829.25 USD | `11,400.80` | `90.37` | `101.80` | `0.000000` | 130,555.53 USD | `+11.25%` | `20X Cross` |
| `1889` | `0x8afa...8113` | `SHORT` | 1,130,374.28 USD | `11,101.69` | `100.52` | `101.80` | `107.79` | -14,429.77 USD | `-1.28%` | `10X Isolated` |
| `1899` | `0x8607...08d5` | `SHORT` | 1,119,826.75 USD | `10,998.10` | `92.18` | `101.80` | `135.02` | -106,037.04 USD | `-9.47%` | `4X Isolated` |
| `1908` | `0xce97...7e78` | `SHORT` | 1,109,047.88 USD | `10,892.24` | `100.84` | `101.80` | `118.06` | -10,642.91 USD | `-0.96%` | `5X Isolated` |
| `2022` | `0xf29c...9971` | `SHORT` | 1,018,700.00 USD | `10,000.00` | `101.10` | `101.80` | `118.37` | -7,703.97 USD | `-0.76%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.97` (Vol: 6,300,000.00 USD, Dist: `+2.30%`) | Long MP=`99.19` (Vol: 6,700,000.00 USD, Dist: `--2.40%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+2.37%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.42%`)
  * 3D Horizon: Short MP=`103.95` (Vol: 6,600,000.00 USD, Dist: `+2.29%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.34%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+2.31%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.34%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `100.90` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `103.05` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-47.83K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
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
| `16:40:00` | `100.72` | `100.72` | `100.72` | `100.83` | `100.55` | 80,376.16 USD | 51,271.98 USD | 29,104.18 USD | 22,167.80 USD | `+27.58%` | `1B / 0S` |
| `16:45:00` | `100.54` | `100.54` | `100.54` | `100.75` | `100.49` | 81,534.70 USD | 14,033.38 USD | 67,501.32 USD | -53,467.94 USD | `-65.58%` | `0B / 1S` |
| `16:45:00` | `101.17` | `101.17` | `101.17` | `101.19` | `100.46` | 248,769.65 USD | 221,677.62 USD | 27,092.04 USD | 194,585.58 USD | `+78.22%` | `1B / 0S` |
| `16:50:00` | `101.02` | `101.02` | `101.02` | `101.09` | `100.46` | 92,024.66 USD | 81,046.92 USD | 10,977.75 USD | 70,069.17 USD | `+76.14%` | `1B / 0S` |
| `16:55:00` | `101.17` | `101.17` | `101.17` | `101.19` | `100.92` | 74,560.08 USD | 64,105.16 USD | 10,454.92 USD | 53,650.24 USD | `+71.96%` | `1B / 0S` |
| `17:00:00` | `101.71` | `101.71` | `101.71` | `101.85` | `101.15` | 242,975.63 USD | 205,567.87 USD | 37,407.76 USD | 168,160.12 USD | `+69.21%` | `1B / 0S` |
| `17:00:00` | `100.95` | `100.95` | `100.95` | `101.85` | `100.81` | 903,080.81 USD | 238,665.11 USD | 664,415.70 USD | -425,750.58 USD | `-47.14%` | `0B / 1S` |
| `17:00:00` | `101.56` | `101.56` | `101.56` | `101.59` | `101.15` | 88,049.92 USD | 83,242.60 USD | 4,807.32 USD | 78,435.27 USD | `+89.08%` | `1B / 0S` |
| `17:05:00` | `101.56` | `101.56` | `101.56` | `101.65` | `101.44` | 68,957.20 USD | 36,847.98 USD | 32,109.22 USD | 4,738.77 USD | `+6.87%` | `1B / 0S` |
| `17:10:00` | `101.71` | `101.71` | `101.71` | `101.85` | `101.55` | 85,738.16 USD | 55,158.21 USD | 30,579.94 USD | 24,578.27 USD | `+28.67%` | `1B / 0S` |
| `0:00 UTC` | `100.13` | `100.30` | `100.13` | `100.56` | `100.12` | 18,899,637.14 USD | 10,932,396.67 USD | 7,967,240.47 USD | 2,965,156.20 USD | `+15.69%` | `6B / 6S` |
| `5:00 UTC` | `100.31` | `100.29` | `100.31` | `100.41` | `100.20` | 9,748,527.75 USD | 5,287,867.77 USD | 4,460,659.98 USD | 827,207.79 USD | `+8.49%` | `1B / 2S` |
| `0:00 UTC` | `100.31` | `100.37` | `100.31` | `100.57` | `100.18` | 15,813,133.46 USD | 8,656,891.75 USD | 7,156,241.72 USD | 1,500,650.03 USD | `+9.49%` | `10B / 4S` |
| `5:00 UTC` | `100.57` | `100.66` | `100.57` | `100.94` | `100.43` | 21,596,195.23 USD | 13,257,846.46 USD | 8,338,348.77 USD | 4,919,497.70 USD | `+22.78%` | `17B / 2S` |
| `0:00 UTC` | `100.95` | `100.94` | `100.95` | `101.07` | `100.72` | 13,472,246.47 USD | 6,374,941.81 USD | 7,097,304.66 USD | -722,362.84 USD | `-5.36%` | `10B / 3S` |
| `5:00 UTC` | `101.00` | `101.01` | `101.00` | `101.28` | `100.85` | 14,129,778.63 USD | 7,872,450.16 USD | 6,257,328.47 USD | 1,615,121.68 USD | `+11.43%` | `13B / 2S` |
| `0:00 UTC` | `101.13` | `101.14` | `101.13` | `101.27` | `100.97` | 14,591,088.89 USD | 5,760,823.82 USD | 8,830,265.07 USD | -3,069,441.25 USD | `-21.04%` | `3B / 3S` |
| `5:00 UTC` | `101.12` | `101.21` | `101.12` | `101.41` | `101.05` | 8,287,817.82 USD | 4,949,702.76 USD | 3,338,115.06 USD | 1,611,587.69 USD | `+19.45%` | `9B / 2S` |
| `0:00 UTC` | `101.80` | `101.69` | `101.80` | `101.95` | `101.28` | 21,400,336.48 USD | 10,768,028.88 USD | 10,632,307.61 USD | 135,721.27 USD | `+0.63%` | `15B / 6S` |
| `5:00 UTC` | `101.60` | `101.67` | `101.60` | `101.91` | `101.43` | 5,783,046.65 USD | 1,688,450.49 USD | 4,094,596.16 USD | -2,406,145.68 USD | `-41.61%` | `3B / 15S` |

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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.48` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.92` (Risk Distance: `0.5617` pts)
  * +2.5R Take Profit: `102.89`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.27` (Risk Distance: `0.5617` pts)
  * +2.5R Take Profit: `101.31`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.33`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
