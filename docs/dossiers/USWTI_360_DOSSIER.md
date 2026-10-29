# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 01:57:19 IST` (`2026-10-29 20:27:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.58` | **Live Ask Quote**: `103.63` | **Mid Price**: `103.61`
- **Spread Points**: `46.00` | **Spread BPS**: `4.44 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.97` | VWAP Z-Score: `+2.45` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.3840` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `70.71` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.81` | Lower -3.00σ Band: `100.13`
  * Upper +2.51σ Band: `103.51` | Lower -2.51σ Band: `100.43`
  * Upper +2.01σ Band: `103.20` | Lower -2.01σ Band: `100.73`
  * Upper +2.00σ Band: `103.20` | Lower -2.00σ Band: `100.74`
  * Upper +1.28σ Band: `102.76` | Lower -1.28σ Band: `101.18`
  * Upper +1.00σ Band: `102.58` | Lower -1.00σ Band: `101.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.98` | EMA-20=`102.56` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.25` (Slope: `+0.0000`) | EMA-100=`102.23`
  * Institutional Anchors: EMA-144=`102.24` | EMA-200=`102.15` (Slope: `+0.0885`) | EMA-233=`102.11`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.77` (Distance: `+0.80%`)
  * Point of Control (POC) = `102.01` (Distance: `+1.56%`)
  * Value Area Low (VAL) = `101.46` (Distance: `+2.11%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.06` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.19` - `104.02`
  * Optimal Trade Entry (OTE 0.705): `103.82`
  * Structural Invalidation Anchor (0.786): `104.44`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `102.42` | `102.55` | `102.33` | `102.50` | `504` | 51,658.99 USD | 22,826.07 USD | `+44.19%` | 112,435.60 USD | `+0.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `102.51` | `102.51` | `102.16` | `102.16` | `439` | 44,847.36 USD | -40,362.63 USD | `-90.00%` | 72,072.98 USD | `-2.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `102.14` | `102.14` | `101.97` | `102.08` | `499` | 50,936.92 USD | -2,315.31 USD | `-4.55%` | 69,757.66 USD | `-0.66` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `101.69` | `102.01` | `101.64` | `101.98` | `1,107` | 112,889.65 USD | 89,243.84 USD | `+79.05%` | 160,564.26 USD | `+0.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.97` | `102.55` | `101.90` | `102.50` | `1,515` | 155,284.47 USD | 129,005.56 USD | `+83.08%` | 289,569.82 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.51` | `102.51` | `101.97` | `102.46` | `1,278` | 130,941.32 USD | 46,071.95 USD | `+35.19%` | 335,641.77 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `100.94` | `101.53` | `100.68` | `101.35` | `7,439` | 753,964.97 USD | 405,912.66 USD | `+53.84%` | -1,045,389.30 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -516,896.02 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.97` | `102.88` | `101.90` | `102.56` | `5,791` | 593,913.38 USD | 283,583.00 USD | `+47.75%` | -233,313.02 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.63` | `101.90` | `103.59` | `15,315` | 1,586,557.43 USD | 1,427,901.68 USD | `+90.00%` | 1,595,774.40 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,027,007.90 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -1,556,424.27 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.63` | `101.90` | `103.59` | `15,315` | 1,586,557.43 USD | 1,427,901.68 USD | `+90.00%` | 1,595,774.40 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,945,071.12 USD | `300,817.26` | `98.89` | `102.94` | `31.75` | 1,195,570.09 USD | `+3.86%` | `3X Cross` |
| `111` | `0x30af...393e` | `LONG` | 18,291,941.14 USD | `177,712.44` | `100.98` | `102.94` | `93.19` | 346,539.25 USD | `+1.89%` | `10X Isolated` |
| `158` | `0x58f0...0d20` | `SHORT` | 12,989,681.68 USD | `126,260.51` | `96.77` | `102.94` | `104.25` | -771,589.26 USD | `-5.94%` | `20X Cross` |
| `217` | `0x9e2c...5508` | `LONG` | 10,289,000.00 USD | `100,000.00` | `100.89` | `102.94` | `78.40` | 199,761.86 USD | `+1.94%` | `20X Cross` |
| `254` | `0xebe1...4070` | `LONG` | 9,262,795.99 USD | `89,999.96` | `101.87` | `102.94` | `0.000000` | 94,377.61 USD | `+1.02%` | `20X Cross` |
| `301` | `0x7fda...17d1` | `SHORT` | 8,095,981.78 USD | `78,647.58` | `100.15` | `102.94` | `206.65` | -219,359.93 USD | `-2.71%` | `20X Cross` |
| `340` | `0x10e1...f4bd` | `LONG` | 6,958,026.48 USD | `67,625.88` | `84.36` | `102.94` | `58.54` | 1,252,796.10 USD | `+18.01%` | `3X Isolated` |
| `367` | `0x4692...164f` | `SHORT` | 6,555,841.99 USD | `63,686.05` | `101.81` | `102.94` | `1043.07` | -71,715.33 USD | `-1.09%` | `5X Cross` |
| `406` | `0x0c4a...1b19` | `SHORT` | 5,743,796.92 USD | `55,802.94` | `102.08` | `102.94` | `106.83` | -47,149.54 USD | `-0.82%` | `20X Isolated` |
| `410` | `0xea00...a918` | `SHORT` | 5,672,861.18 USD | `55,151.29` | `89.22` | `102.94` | `265.26` | -752,136.68 USD | `-13.26%` | `20X Cross` |
| `544` | `0x5989...bc29` | `SHORT` | 4,177,699.72 USD | `40,591.72` | `99.23` | `102.94` | `111.59` | -149,765.04 USD | `-3.58%` | `10X Cross` |
| `559` | `0xd507...c948` | `LONG` | 4,097,488.60 USD | `39,808.50` | `93.57` | `102.94` | `81.35` | 372,413.18 USD | `+9.09%` | `7X Isolated` |
| `716` | `0xb5e7...eff1` | `SHORT` | 3,204,446.40 USD | `31,132.29` | `91.71` | `102.94` | `144.89` | -349,237.76 USD | `-10.90%` | `20X Cross` |
| `752` | `0xd84a...c8a5` | `SHORT` | 3,087,900.00 USD | `30,000.00` | `101.76` | `102.94` | `125.80` | -35,050.00 USD | `-1.14%` | `20X Cross` |
| `806` | `0x61d7...7dee` | `LONG` | 2,866,039.78 USD | `27,858.08` | `88.25` | `102.94` | `83.51` | 407,563.78 USD | `+14.22%` | `20X Cross` |
| `879` | `0xf0ae...2f74` | `SHORT` | 2,572,750.00 USD | `25,000.00` | `100.78` | `102.94` | `173.54` | -53,231.39 USD | `-2.07%` | `20X Cross` |
| `897` | `0xb8f3...04ea` | `SHORT` | 2,527,010.91 USD | `24,560.32` | `102.91` | `102.94` | `114.78` | 496.08 USD | `+0.02%` | `7X Isolated` |
| `905` | `0x354b...6425` | `SHORT` | 2,503,484.95 USD | `24,319.85` | `101.49` | `102.94` | `547.56` | -35,157.32 USD | `-1.40%` | `8X Cross` |
| `908` | `0x645b...87b8` | `SHORT` | 2,501,248.70 USD | `24,302.84` | `101.22` | `102.94` | `134.77` | -41,287.14 USD | `-1.65%` | `3X Isolated` |
| `1100` | `0x9aa5...58af` | `SHORT` | 2,024,539.32 USD | `19,671.00` | `101.76` | `102.94` | `506.85` | -22,788.39 USD | `-1.13%` | `20X Cross` |
| `1149` | `0xfc66...ca06` | `SHORT` | 1,973,277.55 USD | `19,169.20` | `101.21` | `102.94` | `2194.99` | -33,068.85 USD | `-1.68%` | `3X Cross` |
| `1283` | `0x4169...6f06` | `LONG` | 1,767,842.31 USD | `17,175.19` | `76.61` | `102.94` | `82.99` | 452,074.31 USD | `+25.57%` | `12X Isolated` |
| `1289` | `0x6788...98d4` | `SHORT` | 1,748,790.00 USD | `17,000.00` | `99.31` | `102.94` | `193.15` | -60,465.41 USD | `-3.46%` | `20X Cross` |
| `1361` | `0xa99c...40d5` | `SHORT` | 1,656,207.00 USD | `16,100.00` | `101.02` | `102.94` | `155.84` | -29,749.63 USD | `-1.80%` | `20X Cross` |
| `1372` | `0x1bf6...5bfa` | `SHORT` | 1,646,240.00 USD | `16,000.00` | `99.60` | `102.94` | `224.76` | -52,617.69 USD | `-3.20%` | `20X Cross` |
| `1375` | `0xfdfb...dbb9` | `SHORT` | 1,642,494.33 USD | `15,966.70` | `101.16` | `102.94` | `107.16` | -27,264.82 USD | `-1.66%` | `20X Cross` |
| `1462` | `0x17c3...a868` | `LONG` | 1,544,023.75 USD | `15,010.92` | `95.13` | `102.94` | `64.99` | 115,967.68 USD | `+7.51%` | `3X Isolated` |
| `1463` | `0x34ea...2f47` | `SHORT` | 1,543,050.00 USD | `15,000.00` | `99.80` | `102.94` | `193.71` | -46,048.69 USD | `-2.98%` | `20X Cross` |
| `1570` | `0xfb29...21dd` | `LONG` | 1,413,762.46 USD | `13,744.53` | `89.85` | `102.94` | `84.62` | 178,768.50 USD | `+12.64%` | `20X Cross` |
| `1600` | `0x5d6f...6f8a` | `LONG` | 1,389,015.00 USD | `13,500.00` | `101.84` | `102.94` | `19.71` | 14,210.00 USD | `+1.02%` | `20X Cross` |
| `1601` | `0x6fa6...825e` | `SHORT` | 1,388,880.00 USD | `13,500.00` | `102.95` | `102.94` | `135.50` | 894.27 USD | `+0.06%` | `20X Isolated` |
| `1613` | `0xa9d9...b48e` | `SHORT` | 1,372,399.97 USD | `13,333.33` | `96.39` | `102.94` | `174.86` | -87,152.78 USD | `-6.35%` | `20X Cross` |
| `1644` | `0xfc27...9d9d` | `LONG` | 1,325,528.94 USD | `12,876.71` | `101.83` | `102.94` | `0.000000` | 14,280.61 USD | `+1.08%` | `20X Cross` |
| `1704` | `0x89c2...c94b` | `LONG` | 1,272,697.64 USD | `12,364.69` | `75.25` | `102.94` | `45.77` | 342,214.49 USD | `+26.89%` | `3X Isolated` |
| `1737` | `0xcd81...36e3` | `SHORT` | 1,240,899.34 USD | `12,063.96` | `97.96` | `102.94` | `110.56` | -59,060.42 USD | `-4.76%` | `20X Cross` |
| `1741` | `0x436c...b3d1` | `SHORT` | 1,235,040.00 USD | `12,000.00` | `101.05` | `102.94` | `204.52` | -22,380.17 USD | `-1.81%` | `20X Cross` |
| `1747` | `0xe1d3...7766` | `SHORT` | 1,225,961.60 USD | `11,918.74` | `102.74` | `102.94` | `182.88` | -1,378.44 USD | `-0.11%` | `20X Cross` |
| `1800` | `0x9dea...d617` | `LONG` | 1,173,370.13 USD | `11,400.80` | `90.37` | `102.94` | `2.82` | 143,096.41 USD | `+12.20%` | `20X Cross` |
| `1806` | `0x91fd...9841` | `LONG` | 1,166,709.29 USD | `11,334.98` | `101.16` | `102.94` | `95.59` | 20,047.09 USD | `+1.72%` | `13X Isolated` |
| `1830` | `0x8afa...8113` | `SHORT` | 1,142,253.09 USD | `11,101.69` | `100.52` | `102.94` | `107.79` | -26,308.58 USD | `-2.30%` | `10X Isolated` |
| `1845` | `0x8607...08d5` | `SHORT` | 1,132,034.64 USD | `10,998.10` | `92.18` | `102.94` | `135.03` | -118,244.94 USD | `-10.45%` | `4X Isolated` |
| `1970` | `0xf29c...9971` | `SHORT` | 1,029,300.00 USD | `10,000.00` | `101.10` | `102.94` | `118.37` | -18,303.97 USD | `-1.78%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`99.18` (Vol: 6,700,000.00 USD, Dist: `--3.62%`)
  * 48H Horizon: Short MP=`103.99` (Vol: 6,400,000.00 USD, Dist: `+1.05%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--3.62%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 6,400,000.00 USD, Dist: `+1.11%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.55%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+1.05%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--3.55%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.42` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.40` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-41.17K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
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
| `19:45:00` | `101.72` | `101.72` | `101.72` | `101.78` | `101.64` | 41,602.66 USD | 23,883.01 USD | 17,719.65 USD | 6,163.36 USD | `+14.81%` | `1B / 0S` |
| `19:45:00` | `101.98` | `101.98` | `101.98` | `102.01` | `101.64` | 112,889.65 USD | 101,066.74 USD | 11,822.90 USD | 89,243.84 USD | `+79.05%` | `1B / 0S` |
| `19:50:00` | `101.86` | `101.86` | `101.86` | `101.87` | `101.68` | 31,066.69 USD | 28,000.90 USD | 3,065.79 USD | 24,935.11 USD | `+80.26%` | `1B / 0S` |
| `19:55:00` | `101.98` | `101.98` | `101.98` | `102.01` | `101.83` | 40,077.35 USD | 32,562.85 USD | 7,514.50 USD | 25,048.35 USD | `+62.50%` | `1B / 0S` |
| `20:00:00` | `102.50` | `102.50` | `102.50` | `102.55` | `101.90` | 155,284.47 USD | 142,145.01 USD | 13,139.46 USD | 129,005.56 USD | `+83.08%` | `1B / 0S` |
| `20:00:00` | `102.56` | `102.56` | `102.56` | `102.88` | `101.90` | 593,913.38 USD | 438,748.19 USD | 155,165.19 USD | 283,583.00 USD | `+47.75%` | `1B / 0S` |
| `20:00:00` | `103.52` | `103.52` | `103.52` | `103.63` | `101.90` | 1,526,195.36 USD | 1,438,077.84 USD | 88,117.52 USD | 1,349,960.33 USD | `+88.45%` | `1B / 0S` |
| `20:00:00` | `102.22` | `102.22` | `102.22` | `102.23` | `101.90` | 46,920.36 USD | 43,898.97 USD | 3,021.39 USD | 40,877.58 USD | `+87.12%` | `1B / 0S` |
| `20:05:00` | `102.43` | `102.43` | `102.43` | `102.48` | `102.21` | 56,540.26 USD | 47,640.40 USD | 8,899.86 USD | 38,740.55 USD | `+68.52%` | `1B / 0S` |
| `20:10:00` | `102.50` | `102.50` | `102.50` | `102.55` | `102.33` | 51,658.99 USD | 37,242.53 USD | 14,416.46 USD | 22,826.07 USD | `+44.19%` | `1B / 0S` |
| `0:00 UTC` | `101.95` | `101.91` | `101.95` | `102.02` | `101.77` | 7,849,002.75 USD | 3,456,195.71 USD | 4,392,807.03 USD | -936,611.32 USD | `-11.93%` | `2B / 3S` |
| `5:00 UTC` | `102.00` | `102.03` | `102.00` | `102.18` | `101.80` | 13,778,364.28 USD | 6,276,241.74 USD | 7,502,122.54 USD | -1,225,880.80 USD | `-8.90%` | `6B / 5S` |
| `0:00 UTC` | `102.25` | `102.23` | `102.25` | `102.41` | `102.00` | 12,832,227.15 USD | 6,368,450.04 USD | 6,463,777.11 USD | -95,327.07 USD | `-0.74%` | `9B / 6S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.37` | `102.32` | `102.37` | `102.44` | `102.16` | 7,394,503.21 USD | 3,870,700.86 USD | 3,523,802.35 USD | 346,898.52 USD | `+4.69%` | `5B / 3S` |
| `5:00 UTC` | `102.37` | `102.38` | `102.37` | `102.44` | `102.30` | 4,333,204.12 USD | 1,824,676.12 USD | 2,508,528.00 USD | -683,851.88 USD | `-15.78%` | `1B / 3S` |
| `0:00 UTC` | `102.43` | `102.38` | `102.43` | `102.48` | `102.30` | 3,151,223.23 USD | 1,856,912.02 USD | 1,294,311.21 USD | 562,600.81 USD | `+17.85%` | `8B / 4S` |
| `5:00 UTC` | `102.81` | `102.73` | `102.81` | `102.97` | `102.35` | 32,224,554.20 USD | 17,495,336.21 USD | 14,729,217.99 USD | 2,766,118.21 USD | `+8.58%` | `13B / 7S` |
| `0:00 UTC` | `103.00` | `102.95` | `103.00` | `103.06` | `102.81` | 19,638,941.63 USD | 9,830,854.95 USD | 9,808,086.67 USD | 22,768.28 USD | `+0.12%` | `2B / 4S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.82` | 2,997,907.34 USD | 577,782.08 USD | 2,420,125.27 USD | -1,842,343.19 USD | `-61.45%` | `2B / 9S` |

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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.46` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.93` (Risk Distance: `0.5298` pts)
  * +2.5R Take Profit: `102.79`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.53 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.77` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.30` (Risk Distance: `0.5298` pts)
  * +2.5R Take Profit: `101.45`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.53 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.44`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
