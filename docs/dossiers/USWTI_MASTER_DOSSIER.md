# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 00:50:30 IST` (`2026-10-29 19:20:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.88` | **Live Ask Quote**: `102.92` | **Mid Price**: `102.90`
- **Spread Points**: `46.00` | **Spread BPS**: `4.47 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.91` | VWAP Z-Score: `+1.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4179` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `62.65` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.61` | Lower -3.00σ Band: `100.22`
  * Upper +2.51σ Band: `103.33` | Lower -2.51σ Band: `100.49`
  * Upper +2.01σ Band: `103.05` | Lower -2.01σ Band: `100.78`
  * Upper +2.00σ Band: `103.04` | Lower -2.00σ Band: `100.78`
  * Upper +1.28σ Band: `102.64` | Lower -1.28σ Band: `101.19`
  * Upper +1.00σ Band: `102.48` | Lower -1.00σ Band: `101.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.49` | EMA-20=`102.16` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.05` (Slope: `+0.0000`) | EMA-100=`102.13`
  * Institutional Anchors: EMA-144=`102.17` | EMA-200=`102.12` (Slope: `+0.0290`) | EMA-233=`102.07`
- **Range Boundaries**: 24H High=`103.78` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.76` (Distance: `+0.22%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.94%`)
  * Value Area Low (VAL) = `101.53` (Distance: `+1.44%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`102.97` | Weekly POC=`102.03` | Weekly VAL=`101.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `102.49` - `103.31`
  * Optimal Trade Entry (OTE 0.705): `103.10`
  * Structural Invalidation Anchor (0.786): `103.72`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.17` | `101.34` | `101.10` | `101.32` | `648` | 65,654.06 USD | 48,412.98 USD | `+73.74%` | -162,957.23 USD | `+1.60` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.32` | `101.53` | `101.27` | `101.35` | `482` | 48,852.15 USD | -5,636.79 USD | `-11.54%` | -168,594.02 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `101.36` | `101.63` | `101.32` | `101.61` | `663` | 67,368.76 USD | 57,806.74 USD | `+85.81%` | -110,787.28 USD | `+1.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `100.90` | `101.16` | `100.77` | `101.06` | `1,856` | 187,572.93 USD | 85,369.73 USD | `+45.51%` | -346,006.23 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.06` | `101.53` | `101.02` | `101.35` | `2,109` | 213,753.48 USD | 95,236.70 USD | `+44.55%` | -250,769.53 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.36` | `101.69` | `101.32` | `101.52` | `1,669` | 169,441.89 USD | 46,939.98 USD | `+27.70%` | -203,829.55 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,764,580.77 USD | `300,817.26` | `98.89` | `102.32` | `32.19` | 1,015,079.74 USD | `+3.30%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,178,205.18 USD | `177,712.44` | `100.98` | `102.32` | `93.19` | 232,803.29 USD | `+1.28%` | `10X Isolated` |
| `161` | `0x58f0...0d20` | `SHORT` | 12,912,662.77 USD | `126,260.51` | `96.77` | `102.32` | `103.87` | -694,570.34 USD | `-5.38%` | `20X Cross` |
| `218` | `0x9e2c...5508` | `LONG` | 10,229,000.00 USD | `100,000.00` | `100.89` | `102.32` | `79.25` | 139,761.86 USD | `+1.37%` | `20X Cross` |
| `234` | `0xebe1...4070` | `LONG` | 9,920,185.91 USD | `96,999.96` | `101.87` | `102.32` | `0.000000` | 38,668.12 USD | `+0.39%` | `20X Cross` |
| `305` | `0x7fda...17d1` | `SHORT` | 8,055,092.52 USD | `78,763.01` | `100.15` | `102.32` | `209.20` | -166,910.66 USD | `-2.07%` | `20X Cross` |
| `342` | `0x10e1...f4bd` | `LONG` | 6,917,450.96 USD | `67,625.88` | `84.36` | `102.32` | `58.54` | 1,212,220.58 USD | `+17.52%` | `3X Isolated` |
| `378` | `0x4692...164f` | `SHORT` | 6,421,518.37 USD | `62,789.85` | `101.53` | `102.32` | `1035.15` | -46,767.59 USD | `-0.73%` | `5X Cross` |
| `408` | `0x0c4a...1b19` | `SHORT` | 5,708,083.04 USD | `55,802.94` | `102.08` | `102.32` | `106.83` | -11,435.66 USD | `-0.20%` | `20X Isolated` |
| `418` | `0xea00...a918` | `SHORT` | 5,639,770.40 USD | `55,151.29` | `89.22` | `102.32` | `272.62` | -719,045.91 USD | `-12.75%` | `20X Cross` |
| `551` | `0x5989...bc29` | `SHORT` | 4,151,315.10 USD | `40,591.72` | `99.23` | `102.32` | `111.59` | -123,380.42 USD | `-2.97%` | `10X Cross` |
| `563` | `0xd507...c948` | `LONG` | 4,072,011.16 USD | `39,808.50` | `93.57` | `102.32` | `81.35` | 346,935.75 USD | `+8.52%` | `7X Isolated` |
| `734` | `0xb5e7...eff1` | `SHORT` | 3,184,521.74 USD | `31,132.29` | `91.71` | `102.32` | `145.22` | -329,313.09 USD | `-10.34%` | `20X Cross` |
| `771` | `0xd84a...c8a5` | `SHORT` | 3,068,700.00 USD | `30,000.00` | `101.76` | `102.32` | `126.24` | -15,850.00 USD | `-0.52%` | `20X Cross` |
| `790` | `0x354b...6425` | `SHORT` | 2,977,002.78 USD | `29,092.18` | `101.24` | `102.32` | `476.70` | -31,816.64 USD | `-1.07%` | `8X Cross` |
| `819` | `0x61d7...7dee` | `LONG` | 2,849,046.35 USD | `27,858.08` | `88.25` | `102.32` | `83.51` | 390,570.35 USD | `+13.71%` | `20X Cross` |
| `897` | `0xf0ae...2f74` | `SHORT` | 2,557,250.00 USD | `25,000.00` | `100.78` | `102.32` | `173.73` | -37,731.39 USD | `-1.48%` | `20X Cross` |
| `913` | `0xb8f3...04ea` | `SHORT` | 2,512,274.72 USD | `24,560.32` | `102.91` | `102.32` | `114.78` | 15,232.27 USD | `+0.61%` | `7X Isolated` |
| `923` | `0x645b...87b8` | `SHORT` | 2,485,451.86 USD | `24,302.84` | `101.22` | `102.32` | `134.77` | -25,490.30 USD | `-1.03%` | `3X Isolated` |
| `1000` | `0xfc66...ca06` | `SHORT` | 2,301,848.47 USD | `22,507.56` | `101.16` | `102.32` | `1952.35` | -25,076.06 USD | `-1.09%` | `3X Cross` |
| `1122` | `0x9aa5...58af` | `SHORT` | 2,012,146.59 USD | `19,671.00` | `101.76` | `102.32` | `494.04` | -10,395.66 USD | `-0.52%` | `20X Cross` |
| `1297` | `0x4169...6f06` | `LONG` | 1,756,850.19 USD | `17,175.19` | `76.61` | `102.32` | `82.99` | 441,082.19 USD | `+25.11%` | `12X Isolated` |
| `1312` | `0x6788...98d4` | `SHORT` | 1,739,610.00 USD | `17,000.00` | `99.31` | `102.32` | `192.45` | -51,285.41 USD | `-2.95%` | `20X Cross` |
| `1375` | `0xa99c...40d5` | `SHORT` | 1,646,547.00 USD | `16,100.00` | `101.02` | `102.32` | `157.08` | -20,089.63 USD | `-1.22%` | `20X Cross` |
| `1380` | `0x1bf6...5bfa` | `SHORT` | 1,636,640.00 USD | `16,000.00` | `99.60` | `102.32` | `224.49` | -43,017.69 USD | `-2.63%` | `20X Cross` |
| `1385` | `0xfdfb...dbb9` | `SHORT` | 1,632,914.31 USD | `15,966.70` | `101.16` | `102.32` | `107.17` | -17,684.80 USD | `-1.08%` | `20X Cross` |
| `1476` | `0x17c3...a868` | `LONG` | 1,535,017.19 USD | `15,010.92` | `95.13` | `102.32` | `64.99` | 106,961.12 USD | `+6.97%` | `3X Isolated` |
| `1478` | `0x34ea...2f47` | `SHORT` | 1,534,050.00 USD | `15,000.00` | `99.80` | `102.32` | `193.34` | -37,048.69 USD | `-2.42%` | `20X Cross` |
| `1560` | `0x91fd...9841` | `LONG` | 1,424,006.35 USD | `13,923.99` | `101.16` | `102.32` | `95.59` | 15,436.19 USD | `+1.08%` | `13X Isolated` |
| `1584` | `0xfb29...21dd` | `LONG` | 1,405,928.08 USD | `13,744.53` | `89.85` | `102.32` | `84.58` | 170,934.12 USD | `+12.16%` | `20X Cross` |
| `1604` | `0x5d6f...6f8a` | `LONG` | 1,380,915.00 USD | `13,500.00` | `101.84` | `102.32` | `21.27` | 6,110.00 USD | `+0.44%` | `20X Cross` |
| `1605` | `0x6fa6...825e` | `SHORT` | 1,380,645.00 USD | `13,500.00` | `102.95` | `102.32` | `135.50` | 9,129.27 USD | `+0.66%` | `20X Isolated` |
| `1621` | `0xa9d9...b48e` | `SHORT` | 1,363,866.63 USD | `13,333.33` | `96.39` | `102.32` | `175.38` | -78,619.45 USD | `-5.76%` | `20X Cross` |
| `1723` | `0x89c2...c94b` | `LONG` | 1,264,536.95 USD | `12,364.69` | `75.25` | `102.32` | `45.77` | 334,053.80 USD | `+26.42%` | `3X Isolated` |
| `1741` | `0xcd81...36e3` | `SHORT` | 1,233,781.60 USD | `12,063.96` | `97.96` | `102.32` | `111.28` | -51,942.68 USD | `-4.21%` | `20X Cross` |
| `1745` | `0x436c...b3d1` | `SHORT` | 1,227,240.00 USD | `12,000.00` | `101.05` | `102.32` | `203.54` | -14,580.17 USD | `-1.19%` | `20X Cross` |
| `1806` | `0xe1d3...7766` | `SHORT` | 1,170,014.85 USD | `11,441.57` | `102.18` | `102.32` | `187.94` | -923.39 USD | `-0.08%` | `20X Cross` |
| `1810` | `0x9dea...d617` | `LONG` | 1,166,187.63 USD | `11,400.80` | `90.37` | `102.32` | `1.68` | 135,913.90 USD | `+11.65%` | `20X Cross` |
| `1844` | `0x8afa...8113` | `SHORT` | 1,135,592.07 USD | `11,101.69` | `100.52` | `102.32` | `107.79` | -19,647.57 USD | `-1.73%` | `10X Isolated` |
| `1856` | `0x8607...08d5` | `SHORT` | 1,124,995.85 USD | `10,998.10` | `92.18` | `102.32` | `135.03` | -111,206.15 USD | `-9.89%` | `4X Isolated` |
| `1975` | `0xfc27...9d9d` | `LONG` | 1,028,736.79 USD | `10,059.03` | `101.59` | `102.32` | `0.000000` | 6,857.44 USD | `+0.67%` | `20X Cross` |
| `1991` | `0xf29c...9971` | `SHORT` | 1,022,700.00 USD | `10,000.00` | `101.10` | `102.32` | `118.37` | -11,703.97 USD | `-1.14%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.09` (Vol: 2,100,000.00 USD, Dist: `+0.86%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--2.97%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.98%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.90%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+1.73%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.90%`)
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
  * Current Rate: `-44.39K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `18:30:00` | `100.88` | `100.88` | `100.88` | `100.98` | `100.77` | 64,057.53 USD | 30,856.98 USD | 33,200.55 USD | -2,343.57 USD | `-3.66%` | `0B / 1S` |
| `18:35:00` | `101.02` | `101.02` | `101.02` | `101.06` | `100.85` | 64,452.04 USD | 54,600.95 USD | 9,851.08 USD | 44,749.87 USD | `+69.43%` | `1B / 0S` |
| `18:40:00` | `101.06` | `101.06` | `101.06` | `101.16` | `101.00` | 58,919.73 USD | 30,524.68 USD | 28,395.05 USD | 2,129.63 USD | `+3.61%` | `1B / 0S` |
| `18:45:00` | `101.17` | `101.17` | `101.17` | `101.37` | `101.02` | 99,045.43 USD | 53,732.86 USD | 45,312.57 USD | 8,420.29 USD | `+8.50%` | `1B / 0S` |
| `18:45:00` | `101.35` | `101.35` | `101.35` | `101.53` | `101.02` | 213,753.48 USD | 154,495.09 USD | 59,258.39 USD | 95,236.70 USD | `+44.55%` | `1B / 0S` |
| `18:50:00` | `101.32` | `101.32` | `101.32` | `101.34` | `101.10` | 65,654.06 USD | 57,033.52 USD | 8,620.54 USD | 48,412.98 USD | `+73.74%` | `1B / 0S` |
| `18:55:00` | `101.35` | `101.35` | `101.35` | `101.53` | `101.27` | 48,852.15 USD | 21,607.68 USD | 27,244.47 USD | -5,636.79 USD | `-11.54%` | `0B / 1S` |
| `19:00:00` | `101.98` | `101.98` | `101.98` | `102.01` | `101.32` | 590,044.71 USD | 559,268.99 USD | 30,775.71 USD | 528,493.28 USD | `+89.57%` | `1B / 0S` |
| `19:00:00` | `101.61` | `101.61` | `101.61` | `101.63` | `101.32` | 67,368.76 USD | 62,587.75 USD | 4,781.01 USD | 57,806.74 USD | `+85.81%` | `1B / 0S` |
| `19:00:00` | `101.52` | `101.52` | `101.52` | `101.69` | `101.32` | 169,441.89 USD | 108,190.93 USD | 61,250.95 USD | 46,939.98 USD | `+27.70%` | `1B / 0S` |
| `5:00 UTC` | `101.12` | `101.21` | `101.12` | `101.41` | `101.05` | 8,287,817.82 USD | 4,949,702.76 USD | 3,338,115.06 USD | 1,611,587.69 USD | `+19.45%` | `9B / 2S` |
| `0:00 UTC` | `101.80` | `101.69` | `101.80` | `101.95` | `101.28` | 21,400,336.48 USD | 10,768,028.88 USD | 10,632,307.61 USD | 135,721.27 USD | `+0.63%` | `15B / 6S` |
| `5:00 UTC` | `101.68` | `101.64` | `101.68` | `101.91` | `101.38` | 9,829,156.63 USD | 4,338,777.97 USD | 5,490,378.67 USD | -1,151,600.70 USD | `-11.72%` | `10B / 10S` |
| `0:00 UTC` | `102.41` | `102.23` | `102.41` | `102.50` | `101.82` | 76,189,579.98 USD | 39,225,207.15 USD | 36,964,372.83 USD | 2,260,834.33 USD | `+2.97%` | `20B / 3S` |
| `5:00 UTC` | `102.02` | `102.01` | `102.02` | `102.13` | `101.85` | 13,174,401.35 USD | 6,982,040.79 USD | 6,192,360.55 USD | 789,680.24 USD | `+5.99%` | `1B / 6S` |
| `0:00 UTC` | `101.95` | `101.91` | `101.95` | `102.02` | `101.77` | 7,849,002.75 USD | 3,456,195.71 USD | 4,392,807.03 USD | -936,611.32 USD | `-11.93%` | `2B / 3S` |
| `5:00 UTC` | `102.00` | `102.03` | `102.00` | `102.18` | `101.80` | 13,778,364.28 USD | 6,276,241.74 USD | 7,502,122.54 USD | -1,225,880.80 USD | `-8.90%` | `6B / 5S` |
| `0:00 UTC` | `102.25` | `102.23` | `102.25` | `102.41` | `102.00` | 12,832,227.15 USD | 6,368,450.04 USD | 6,463,777.11 USD | -95,327.07 USD | `-0.74%` | `9B / 6S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.19` | `102.22` | `102.19` | `102.30` | `102.16` | 2,029,859.55 USD | 1,021,017.18 USD | 1,008,842.37 USD | 12,174.81 USD | `+0.60%` | `3B / 0S` |

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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.53` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.96` (Risk Distance: `0.5704` pts)
  * +2.5R Take Profit: `102.95`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.76` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.33` (Risk Distance: `0.5704` pts)
  * +2.5R Take Profit: `101.34`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.72`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
