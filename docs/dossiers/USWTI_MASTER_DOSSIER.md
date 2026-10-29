# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 01:26:55 IST` (`2026-10-29 19:56:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.28` | **Live Ask Quote**: `103.34` | **Mid Price**: `103.31`
- **Spread Points**: `56.00` | **Spread BPS**: `5.42 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `101.93` | VWAP Z-Score: `+1.74` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3770` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `64.15` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.67` | Lower -3.00σ Band: `100.20`
  * Upper +2.51σ Band: `103.38` | Lower -2.51σ Band: `100.48`
  * Upper +2.01σ Band: `103.09` | Lower -2.01σ Band: `100.77`
  * Upper +2.00σ Band: `103.09` | Lower -2.00σ Band: `100.78`
  * Upper +1.28σ Band: `102.67` | Lower -1.28σ Band: `101.19`
  * Upper +1.00σ Band: `102.51` | Lower -1.00σ Band: `101.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.71` | EMA-20=`102.37` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.15` (Slope: `+0.0000`) | EMA-100=`102.18`
  * Institutional Anchors: EMA-144=`102.20` | EMA-200=`102.13` (Slope: `+0.0658`) | EMA-233=`102.09`
- **Range Boundaries**: 24H High=`103.68` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.77` (Distance: `+0.57%`)
  * Point of Control (POC) = `102.01` (Distance: `+1.31%`)
  * Value Area Low (VAL) = `101.50` (Distance: `+1.82%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.03` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `102.90` - `103.73`
  * Optimal Trade Entry (OTE 0.705): `103.52`
  * Structural Invalidation Anchor (0.786): `104.14`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.87` | `101.88` | `101.75` | `101.81` | `487` | 49,580.50 USD | -14,874.15 USD | `-30.00%` | -37,502.30 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `101.81` | `101.86` | `101.69` | `101.72` | `436` | 44,349.05 USD | -26,087.68 USD | `-58.82%` | -63,589.97 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `101.70` | `101.75` | `101.58` | `101.70` | `441` | 44,848.82 USD | 9,233.58 USD | `+20.59%` | -54,356.39 USD | `-0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `101.36` | `101.69` | `101.32` | `101.52` | `1,669` | 169,441.89 USD | 46,939.98 USD | `+27.70%` | -133,778.07 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.53` | `101.87` | `101.46` | `101.86` | `1,646` | 167,658.27 USD | 145,167.52 USD | `+86.59%` | 11,389.46 USD | `+1.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.87` | `101.88` | `101.58` | `101.70` | `1,364` | 138,716.07 USD | -53,174.49 USD | `-38.33%` | -41,785.04 USD | `-0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.16` | `101.85` | `100.81` | `100.95` | `8,946` | 903,080.81 USD | -425,750.58 USD | `-47.14%` | -1,764,218.73 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `100.94` | `101.53` | `100.68` | `101.35` | `7,439` | 753,964.97 USD | 405,912.66 USD | `+53.84%` | -1,358,306.06 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -829,812.78 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,896,940.36 USD | `300,817.26` | `98.89` | `102.74` | `31.93` | 1,147,439.33 USD | `+3.71%` | `3X Cross` |
| `111` | `0x30af...393e` | `LONG` | 18,254,621.53 USD | `177,712.44` | `100.98` | `102.74` | `93.19` | 309,219.64 USD | `+1.69%` | `10X Isolated` |
| `160` | `0x58f0...0d20` | `SHORT` | 12,968,217.39 USD | `126,260.51` | `96.77` | `102.74` | `103.98` | -750,124.97 USD | `-5.78%` | `20X Cross` |
| `216` | `0x9e2c...5508` | `LONG` | 10,271,000.00 USD | `100,000.00` | `100.89` | `102.74` | `78.78` | 181,761.86 USD | `+1.77%` | `20X Cross` |
| `260` | `0xebe1...4070` | `LONG` | 9,244,795.99 USD | `89,999.96` | `101.87` | `102.74` | `0.000000` | 76,377.62 USD | `+0.83%` | `20X Cross` |
| `304` | `0x7fda...17d1` | `SHORT` | 8,091,323.50 USD | `78,763.01` | `100.15` | `102.74` | `210.43` | -203,141.64 USD | `-2.51%` | `20X Cross` |
| `341` | `0x10e1...f4bd` | `LONG` | 6,947,206.34 USD | `67,625.88` | `84.36` | `102.74` | `58.54` | 1,241,975.96 USD | `+17.88%` | `3X Isolated` |
| `360` | `0x4692...164f` | `SHORT` | 6,652,867.47 USD | `64,767.01` | `101.66` | `102.74` | `996.99` | -68,689.35 USD | `-1.03%` | `5X Cross` |
| `407` | `0x0c4a...1b19` | `SHORT` | 5,732,078.30 USD | `55,802.94` | `102.08` | `102.74` | `106.83` | -35,430.92 USD | `-0.62%` | `20X Isolated` |
| `410` | `0xea00...a918` | `SHORT` | 5,665,140.00 USD | `55,151.29` | `89.22` | `102.74` | `272.85` | -744,415.50 USD | `-13.14%` | `20X Cross` |
| `550` | `0x5989...bc29` | `SHORT` | 4,169,175.46 USD | `40,591.72` | `99.23` | `102.74` | `111.59` | -141,240.78 USD | `-3.39%` | `10X Cross` |
| `564` | `0xd507...c948` | `LONG` | 4,089,526.90 USD | `39,808.50` | `93.57` | `102.74` | `81.35` | 364,451.48 USD | `+8.91%` | `7X Isolated` |
| `736` | `0xb5e7...eff1` | `SHORT` | 3,197,908.62 USD | `31,132.29` | `91.71` | `102.74` | `145.09` | -342,699.98 USD | `-10.72%` | `20X Cross` |
| `738` | `0x354b...6425` | `SHORT` | 3,194,071.72 USD | `31,094.94` | `101.47` | `102.74` | `452.42` | -38,992.85 USD | `-1.22%` | `8X Cross` |
| `765` | `0xd84a...c8a5` | `SHORT` | 3,081,600.00 USD | `30,000.00` | `101.76` | `102.74` | `125.99` | -28,750.00 USD | `-0.93%` | `20X Cross` |
| `819` | `0x61d7...7dee` | `LONG` | 2,861,303.91 USD | `27,858.08` | `88.25` | `102.74` | `83.51` | 402,827.91 USD | `+14.08%` | `20X Cross` |
| `893` | `0xf0ae...2f74` | `SHORT` | 2,568,000.00 USD | `25,000.00` | `100.78` | `102.74` | `173.15` | -48,481.39 USD | `-1.89%` | `20X Cross` |
| `908` | `0xb8f3...04ea` | `SHORT` | 2,522,590.06 USD | `24,560.32` | `102.91` | `102.74` | `114.78` | 4,916.94 USD | `+0.19%` | `7X Isolated` |
| `917` | `0x645b...87b8` | `SHORT` | 2,496,145.11 USD | `24,302.84` | `101.22` | `102.74` | `134.77` | -36,183.55 USD | `-1.45%` | `3X Isolated` |
| `1114` | `0x9aa5...58af` | `SHORT` | 2,020,801.83 USD | `19,671.00` | `101.76` | `102.74` | `491.28` | -19,050.90 USD | `-0.94%` | `20X Cross` |
| `1125` | `0xfc66...ca06` | `SHORT` | 2,009,563.78 USD | `19,559.70` | `101.21` | `102.74` | `2121.73` | -29,830.57 USD | `-1.48%` | `3X Cross` |
| `1289` | `0x4169...6f06` | `LONG` | 1,764,235.52 USD | `17,175.19` | `76.61` | `102.74` | `82.99` | 448,467.52 USD | `+25.42%` | `12X Isolated` |
| `1309` | `0x6788...98d4` | `SHORT` | 1,746,070.00 USD | `17,000.00` | `99.31` | `102.74` | `191.68` | -57,745.41 USD | `-3.31%` | `20X Cross` |
| `1373` | `0xa99c...40d5` | `SHORT` | 1,653,631.00 USD | `16,100.00` | `101.02` | `102.74` | `156.43` | -27,173.63 USD | `-1.64%` | `20X Cross` |
| `1382` | `0x1bf6...5bfa` | `SHORT` | 1,643,360.00 USD | `16,000.00` | `99.60` | `102.74` | `223.83` | -49,737.69 USD | `-3.03%` | `20X Cross` |
| `1385` | `0xfdfb...dbb9` | `SHORT` | 1,639,939.65 USD | `15,966.70` | `101.16` | `102.74` | `107.51` | -24,710.15 USD | `-1.51%` | `20X Cross` |
| `1474` | `0x17c3...a868` | `LONG` | 1,541,922.22 USD | `15,010.92` | `95.13` | `102.74` | `64.99` | 113,866.15 USD | `+7.38%` | `3X Isolated` |
| `1475` | `0x34ea...2f47` | `SHORT` | 1,540,650.00 USD | `15,000.00` | `99.80` | `102.74` | `192.78` | -43,648.69 USD | `-2.83%` | `20X Cross` |
| `1574` | `0xfb29...21dd` | `LONG` | 1,411,700.78 USD | `13,744.53` | `89.85` | `102.74` | `84.60` | 176,706.82 USD | `+12.52%` | `20X Cross` |
| `1603` | `0x5d6f...6f8a` | `LONG` | 1,386,720.00 USD | `13,500.00` | `101.84` | `102.74` | `20.35` | 11,915.00 USD | `+0.86%` | `20X Cross` |
| `1604` | `0x6fa6...825e` | `SHORT` | 1,386,585.00 USD | `13,500.00` | `102.95` | `102.74` | `135.50` | 3,189.27 USD | `+0.23%` | `20X Isolated` |
| `1615` | `0xa9d9...b48e` | `SHORT` | 1,369,599.97 USD | `13,333.33` | `96.39` | `102.74` | `175.20` | -84,352.78 USD | `-6.16%` | `20X Cross` |
| `1728` | `0x89c2...c94b` | `LONG` | 1,269,977.41 USD | `12,364.69` | `75.25` | `102.74` | `45.77` | 339,494.26 USD | `+26.73%` | `3X Isolated` |
| `1744` | `0xcd81...36e3` | `SHORT` | 1,239,210.38 USD | `12,063.96` | `97.96` | `102.74` | `111.37` | -57,371.46 USD | `-4.63%` | `20X Cross` |
| `1747` | `0x436c...b3d1` | `SHORT` | 1,232,520.00 USD | `12,000.00` | `101.05` | `102.74` | `202.70` | -19,860.17 USD | `-1.61%` | `20X Cross` |
| `1813` | `0x9dea...d617` | `LONG` | 1,170,975.96 USD | `11,400.80` | `90.37` | `102.74` | `0.000000` | 140,702.24 USD | `+12.02%` | `20X Cross` |
| `1823` | `0x91fd...9841` | `LONG` | 1,164,328.94 USD | `11,334.98` | `101.16` | `102.74` | `95.59` | 17,666.75 USD | `+1.52%` | `13X Isolated` |
| `1844` | `0x8afa...8113` | `SHORT` | 1,140,254.79 USD | `11,101.69` | `100.52` | `102.74` | `107.79` | -24,310.28 USD | `-2.13%` | `10X Isolated` |
| `1859` | `0x8607...08d5` | `SHORT` | 1,129,615.06 USD | `10,998.10` | `92.18` | `102.74` | `135.03` | -115,825.35 USD | `-10.25%` | `4X Isolated` |
| `1922` | `0xfc27...9d9d` | `LONG` | 1,070,198.92 USD | `10,417.59` | `101.61` | `102.74` | `0.000000` | 11,664.96 USD | `+1.09%` | `20X Cross` |
| `1988` | `0xf29c...9971` | `SHORT` | 1,027,100.00 USD | `10,000.00` | `101.10` | `102.74` | `118.37` | -16,103.97 USD | `-1.57%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`102.87` (Vol: 2,300,000.00 USD, Dist: `+0.45%`) | Long MP=`99.19` (Vol: 6,700,000.00 USD, Dist: `--3.14%`)
  * 48H Horizon: Short MP=`103.99` (Vol: 6,400,000.00 USD, Dist: `+1.54%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--3.16%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.59%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.09%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+1.53%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--3.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `101.99` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `103.95` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-41.37K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `19:05:00` | `101.60` | `101.60` | `101.60` | `101.69` | `101.47` | 52,729.36 USD | 28,521.79 USD | 24,207.57 USD | 4,314.22 USD | `+8.18%` | `1B / 0S` |
| `19:10:00` | `101.52` | `101.52` | `101.52` | `101.61` | `101.39` | 49,441.70 USD | 23,878.09 USD | 25,563.61 USD | -1,685.51 USD | `-3.41%` | `0B / 1S` |
| `19:15:00` | `101.58` | `101.58` | `101.58` | `101.61` | `101.46` | 42,764.34 USD | 31,335.94 USD | 11,428.40 USD | 19,907.54 USD | `+46.55%` | `1B / 0S` |
| `19:15:00` | `101.86` | `101.86` | `101.86` | `101.87` | `101.46` | 167,658.27 USD | 156,412.90 USD | 11,245.37 USD | 145,167.52 USD | `+86.59%` | `1B / 0S` |
| `19:20:00` | `101.61` | `101.61` | `101.61` | `101.65` | `101.47` | 54,665.10 USD | 37,961.88 USD | 16,703.23 USD | 21,258.65 USD | `+38.89%` | `1B / 0S` |
| `19:25:00` | `101.86` | `101.86` | `101.86` | `101.87` | `101.57` | 69,976.45 USD | 65,894.49 USD | 4,081.96 USD | 61,812.53 USD | `+88.33%` | `1B / 0S` |
| `19:30:00` | `101.81` | `101.81` | `101.81` | `101.88` | `101.75` | 49,580.50 USD | 17,353.17 USD | 32,227.32 USD | -14,874.15 USD | `-30.00%` | `0B / 1S` |
| `19:30:00` | `101.70` | `101.70` | `101.70` | `101.88` | `101.58` | 138,716.07 USD | 42,770.79 USD | 95,945.28 USD | -53,174.49 USD | `-38.33%` | `0B / 1S` |
| `19:35:00` | `101.72` | `101.72` | `101.72` | `101.86` | `101.69` | 44,349.05 USD | 9,130.69 USD | 35,218.36 USD | -26,087.68 USD | `-58.82%` | `0B / 1S` |
| `19:40:00` | `101.70` | `101.70` | `101.70` | `101.75` | `101.58` | 44,848.82 USD | 27,041.20 USD | 17,807.62 USD | 9,233.58 USD | `+20.59%` | `1B / 0S` |
| `0:00 UTC` | `102.41` | `102.23` | `102.41` | `102.50` | `101.82` | 76,189,579.98 USD | 39,225,207.15 USD | 36,964,372.83 USD | 2,260,834.33 USD | `+2.97%` | `20B / 3S` |
| `5:00 UTC` | `102.02` | `102.01` | `102.02` | `102.13` | `101.85` | 13,174,401.35 USD | 6,982,040.79 USD | 6,192,360.55 USD | 789,680.24 USD | `+5.99%` | `1B / 6S` |
| `0:00 UTC` | `101.95` | `101.91` | `101.95` | `102.02` | `101.77` | 7,849,002.75 USD | 3,456,195.71 USD | 4,392,807.03 USD | -936,611.32 USD | `-11.93%` | `2B / 3S` |
| `5:00 UTC` | `102.00` | `102.03` | `102.00` | `102.18` | `101.80` | 13,778,364.28 USD | 6,276,241.74 USD | 7,502,122.54 USD | -1,225,880.80 USD | `-8.90%` | `6B / 5S` |
| `0:00 UTC` | `102.25` | `102.23` | `102.25` | `102.41` | `102.00` | 12,832,227.15 USD | 6,368,450.04 USD | 6,463,777.11 USD | -95,327.07 USD | `-0.74%` | `9B / 6S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.37` | `102.32` | `102.37` | `102.44` | `102.16` | 7,394,503.21 USD | 3,870,700.86 USD | 3,523,802.35 USD | 346,898.52 USD | `+4.69%` | `5B / 3S` |
| `5:00 UTC` | `102.37` | `102.38` | `102.37` | `102.44` | `102.30` | 4,333,204.12 USD | 1,824,676.12 USD | 2,508,528.00 USD | -683,851.88 USD | `-15.78%` | `1B / 3S` |
| `0:00 UTC` | `102.43` | `102.38` | `102.43` | `102.48` | `102.30` | 3,151,223.23 USD | 1,856,912.02 USD | 1,294,311.21 USD | 562,600.81 USD | `+17.85%` | `8B / 4S` |
| `5:00 UTC` | `102.50` | `102.47` | `102.50` | `102.53` | `102.35` | 3,521,986.31 USD | 2,235,465.86 USD | 1,286,520.45 USD | 948,945.41 USD | `+26.94%` | `5B / 5S` |

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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.50` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.96` (Risk Distance: `0.5364` pts)
  * +2.5R Take Profit: `102.84`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.54 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.77` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.30` (Risk Distance: `0.5364` pts)
  * +2.5R Take Profit: `101.43`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.54 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.14`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
