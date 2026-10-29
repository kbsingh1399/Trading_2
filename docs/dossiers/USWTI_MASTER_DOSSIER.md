# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-29 23:10:17 IST` (`2026-10-29 17:40:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.78` | **Live Ask Quote**: `102.82` | **Mid Price**: `102.80`
- **Spread Points**: `36.00` | **Spread BPS**: `3.50 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `102.80` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.52` | Lower -3.00σ Band: `102.08`
  * Upper +2.51σ Band: `103.36` | Lower -2.51σ Band: `102.23`
  * Upper +2.01σ Band: `103.23` | Lower -2.01σ Band: `102.37`
  * Upper +2.00σ Band: `103.21` | Lower -2.00σ Band: `102.39`
  * Upper +1.28σ Band: `103.09` | Lower -1.28σ Band: `102.51`
  * Upper +1.00σ Band: `103.00` | Lower -1.00σ Band: `102.59`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.80` | EMA-20=`102.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.80` (Slope: `+0.0000`) | EMA-100=`102.80`
  * Institutional Anchors: EMA-144=`102.80` | EMA-200=`102.80` (Slope: `+0.0000`) | EMA-233=`102.80`
- **Range Boundaries**: 24H High=`103.83` | 24H Low=`101.77` | Weekly High=`104.85` | Weekly Low=`100.74`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.71` (Distance: `-0.02%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.65%`)
  * Value Area Low (VAL) = `101.50` (Distance: `+1.18%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.00` | Weekly POC=`102.03` | Weekly VAL=`101.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `102.39` - `103.21`
  * Optimal Trade Entry (OTE 0.705): `103.00`
  * Structural Invalidation Anchor (0.786): `103.62`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.55` | `101.85` | `101.55` | `101.71` | `843` | 85,738.16 USD | 24,578.27 USD | `+28.67%` | 66,291.54 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.70` | `101.75` | `101.45` | `101.53` | `825` | 83,758.95 USD | -43,973.45 USD | `-52.50%` | 22,318.09 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `101.52` | `101.56` | `101.33` | `101.42` | `722` | 73,223.80 USD | -24,512.69 USD | `-33.48%` | -2,194.59 USD | `-0.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `100.72` | `101.19` | `100.46` | `101.17` | `2,459` | 248,769.65 USD | 194,585.58 USD | `+78.22%` | 61,987.34 USD | `+2.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.16` | `101.85` | `101.15` | `101.71` | `2,389` | 242,975.63 USD | 168,160.12 USD | `+69.21%` | 230,147.46 USD | `+1.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.70` | `101.75` | `101.33` | `101.49` | `2,166` | 219,820.84 USD | -82,564.29 USD | `-37.56%` | 147,583.17 USD | `-0.80` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 30,686,368.28 USD | `300,817.26` | `98.89` | `102.09` | `32.39` | 936,867.25 USD | `+3.05%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,139,108.44 USD | `177,712.44` | `100.98` | `102.09` | `93.19` | 193,706.56 USD | `+1.07%` | `10X Isolated` |
| `164` | `0x58f0...0d20` | `SHORT` | 12,883,622.85 USD | `126,260.51` | `96.77` | `102.09` | `105.15` | -665,530.43 USD | `-5.17%` | `20X Cross` |
| `220` | `0xebe1...4070` | `LONG` | 10,304,015.92 USD | `100,999.96` | `101.87` | `102.09` | `0.000000` | 14,984.50 USD | `+0.15%` | `20X Cross` |
| `223` | `0x9e2c...5508` | `LONG` | 10,207,000.00 USD | `100,000.00` | `100.89` | `102.09` | `79.51` | 117,761.86 USD | `+1.15%` | `20X Cross` |
| `310` | `0x7fda...17d1` | `SHORT` | 8,039,339.92 USD | `78,763.01` | `100.15` | `102.09` | `210.25` | -151,158.06 USD | `-1.88%` | `20X Cross` |
| `348` | `0x10e1...f4bd` | `LONG` | 6,902,573.27 USD | `67,625.88` | `84.36` | `102.09` | `58.54` | 1,197,342.88 USD | `+17.35%` | `3X Isolated` |
| `389` | `0x4692...164f` | `SHORT` | 6,254,685.98 USD | `61,278.40` | `101.17` | `102.09` | `1046.16` | -55,036.17 USD | `-0.88%` | `5X Cross` |
| `417` | `0x0c4a...1b19` | `SHORT` | 5,695,806.39 USD | `55,802.94` | `102.08` | `102.09` | `106.83` | 840.99 USD | `+0.01%` | `20X Isolated` |
| `429` | `0xea00...a918` | `SHORT` | 5,626,534.10 USD | `55,151.29` | `89.22` | `102.09` | `285.56` | -705,809.60 USD | `-12.54%` | `20X Cross` |
| `572` | `0x5989...bc29` | `SHORT` | 4,141,979.01 USD | `40,591.72` | `99.23` | `102.09` | `111.59` | -114,044.33 USD | `-2.75%` | `10X Cross` |
| `581` | `0xd507...c948` | `LONG` | 4,063,253.29 USD | `39,808.50` | `93.57` | `102.09` | `81.35` | 338,177.88 USD | `+8.32%` | `7X Isolated` |
| `603` | `0x354b...6425` | `SHORT` | 3,950,425.52 USD | `38,703.10` | `101.08` | `102.09` | `380.35` | -38,344.98 USD | `-0.97%` | `8X Cross` |
| `748` | `0xb5e7...eff1` | `SHORT` | 3,177,672.64 USD | `31,132.29` | `91.71` | `102.09` | `145.63` | -322,463.99 USD | `-10.15%` | `20X Cross` |
| `777` | `0xd84a...c8a5` | `SHORT` | 3,062,100.00 USD | `30,000.00` | `101.76` | `102.09` | `126.41` | -9,250.00 USD | `-0.30%` | `20X Cross` |
| `836` | `0x61d7...7dee` | `LONG` | 2,842,638.99 USD | `27,858.08` | `88.25` | `102.09` | `83.50` | 384,162.99 USD | `+13.51%` | `20X Cross` |
| `913` | `0xf0ae...2f74` | `SHORT` | 2,551,750.00 USD | `25,000.00` | `100.78` | `102.09` | `172.42` | -32,231.39 USD | `-1.26%` | `20X Cross` |
| `929` | `0xb8f3...04ea` | `SHORT` | 2,506,871.45 USD | `24,560.32` | `102.91` | `102.09` | `114.77` | 20,635.54 USD | `+0.82%` | `7X Isolated` |
| `937` | `0x645b...87b8` | `SHORT` | 2,480,591.29 USD | `24,302.84` | `101.22` | `102.09` | `134.77` | -20,629.73 USD | `-0.83%` | `3X Isolated` |
| `957` | `0xfc66...ca06` | `SHORT` | 2,419,544.65 USD | `23,704.76` | `101.06` | `102.09` | `1846.21` | -23,935.54 USD | `-0.99%` | `3X Cross` |
| `1143` | `0x9aa5...58af` | `SHORT` | 2,007,818.97 USD | `19,671.00` | `101.76` | `102.09` | `467.16` | -6,068.04 USD | `-0.30%` | `20X Cross` |
| `1316` | `0x4169...6f06` | `LONG` | 1,753,071.64 USD | `17,175.19` | `76.61` | `102.09` | `82.99` | 437,303.64 USD | `+24.94%` | `12X Isolated` |
| `1325` | `0x6788...98d4` | `SHORT` | 1,734,340.00 USD | `17,000.00` | `99.31` | `102.09` | `190.19` | -46,015.41 USD | `-2.65%` | `20X Cross` |
| `1393` | `0xa99c...40d5` | `SHORT` | 1,642,361.00 USD | `16,100.00` | `101.02` | `102.09` | `158.14` | -15,903.63 USD | `-0.97%` | `20X Cross` |
| `1402` | `0x1bf6...5bfa` | `SHORT` | 1,633,120.00 USD | `16,000.00` | `99.60` | `102.09` | `222.85` | -39,497.69 USD | `-2.42%` | `20X Cross` |
| `1405` | `0xfdfb...dbb9` | `SHORT` | 1,628,762.97 USD | `15,966.70` | `101.16` | `102.09` | `107.76` | -13,533.46 USD | `-0.83%` | `20X Cross` |
| `1487` | `0x91fd...9841` | `LONG` | 1,544,827.20 USD | `15,134.98` | `101.16` | `102.09` | `95.58` | 13,751.71 USD | `+0.89%` | `13X Isolated` |
| `1498` | `0x17c3...a868` | `LONG` | 1,530,814.13 USD | `15,010.92` | `95.13` | `102.09` | `64.99` | 102,758.06 USD | `+6.71%` | `3X Isolated` |
| `1499` | `0x34ea...2f47` | `SHORT` | 1,530,300.00 USD | `15,000.00` | `99.80` | `102.09` | `191.55` | -33,298.69 USD | `-2.18%` | `20X Cross` |
| `1614` | `0xfb29...21dd` | `LONG` | 1,401,942.16 USD | `13,744.53` | `89.85` | `102.09` | `84.53` | 166,948.20 USD | `+11.91%` | `20X Cross` |
| `1631` | `0x6fa6...825e` | `SHORT` | 1,377,540.00 USD | `13,500.00` | `102.95` | `102.09` | `135.50` | 12,234.27 USD | `+0.89%` | `20X Isolated` |
| `1644` | `0xa9d9...b48e` | `SHORT` | 1,360,933.30 USD | `13,333.33` | `96.39` | `102.09` | `176.04` | -75,686.11 USD | `-5.56%` | `20X Cross` |
| `1745` | `0x89c2...c94b` | `LONG` | 1,261,322.13 USD | `12,364.69` | `75.25` | `102.09` | `45.77` | 330,838.98 USD | `+26.23%` | `3X Isolated` |
| `1770` | `0xcd81...36e3` | `SHORT` | 1,230,765.61 USD | `12,063.96` | `97.96` | `102.09` | `111.96` | -48,926.69 USD | `-3.98%` | `20X Cross` |
| `1775` | `0x436c...b3d1` | `SHORT` | 1,224,480.00 USD | `12,000.00` | `101.05` | `102.09` | `200.30` | -11,820.17 USD | `-0.97%` | `20X Cross` |
| `1842` | `0x9dea...d617` | `LONG` | 1,163,679.45 USD | `11,400.80` | `90.37` | `102.09` | `0.000000` | 133,405.73 USD | `+11.46%` | `20X Cross` |
| `1882` | `0x8afa...8113` | `SHORT` | 1,133,149.70 USD | `11,101.69` | `100.52` | `102.09` | `107.79` | -17,205.20 USD | `-1.52%` | `10X Isolated` |
| `1891` | `0x8607...08d5` | `SHORT` | 1,122,576.27 USD | `10,998.10` | `92.18` | `102.09` | `135.02` | -108,786.57 USD | `-9.69%` | `4X Isolated` |
| `2020` | `0xf29c...9971` | `SHORT` | 1,020,200.00 USD | `10,000.00` | `101.10` | `102.09` | `118.37` | -9,203.97 USD | `-0.90%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`102.20` (Vol: 3,300,000.00 USD, Dist: `+0.34%`) | Long MP=`99.20` (Vol: 6,700,000.00 USD, Dist: `--2.60%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+2.15%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.64%`)
  * 3D Horizon: Short MP=`103.95` (Vol: 6,300,000.00 USD, Dist: `+2.07%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.55%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+2.09%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.55%`)
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
  * Current Rate: `-49.60K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `16:50:00` | `101.02` | `101.02` | `101.02` | `101.09` | `100.46` | 92,024.66 USD | 81,046.92 USD | 10,977.75 USD | 70,069.17 USD | `+76.14%` | `1B / 0S` |
| `16:55:00` | `101.17` | `101.17` | `101.17` | `101.19` | `100.92` | 74,560.08 USD | 64,105.16 USD | 10,454.92 USD | 53,650.24 USD | `+71.96%` | `1B / 0S` |
| `17:00:00` | `100.95` | `100.95` | `100.95` | `101.85` | `100.81` | 903,080.81 USD | 238,665.11 USD | 664,415.70 USD | -425,750.58 USD | `-47.14%` | `0B / 1S` |
| `17:00:00` | `101.56` | `101.56` | `101.56` | `101.59` | `101.15` | 88,049.92 USD | 83,242.60 USD | 4,807.32 USD | 78,435.27 USD | `+89.08%` | `1B / 0S` |
| `17:00:00` | `101.71` | `101.71` | `101.71` | `101.85` | `101.15` | 242,975.63 USD | 205,567.87 USD | 37,407.76 USD | 168,160.12 USD | `+69.21%` | `1B / 0S` |
| `17:05:00` | `101.56` | `101.56` | `101.56` | `101.65` | `101.44` | 68,957.20 USD | 36,847.98 USD | 32,109.22 USD | 4,738.77 USD | `+6.87%` | `1B / 0S` |
| `17:10:00` | `101.71` | `101.71` | `101.71` | `101.85` | `101.55` | 85,738.16 USD | 55,158.21 USD | 30,579.94 USD | 24,578.27 USD | `+28.67%` | `1B / 0S` |
| `17:15:00` | `101.49` | `101.49` | `101.49` | `101.75` | `101.33` | 219,820.84 USD | 68,628.28 USD | 151,192.56 USD | -82,564.29 USD | `-37.56%` | `0B / 1S` |
| `17:15:00` | `101.53` | `101.53` | `101.53` | `101.75` | `101.45` | 83,758.95 USD | 19,892.75 USD | 63,866.20 USD | -43,973.45 USD | `-52.50%` | `0B / 1S` |
| `17:20:00` | `101.42` | `101.42` | `101.42` | `101.56` | `101.33` | 73,223.80 USD | 24,355.55 USD | 48,868.24 USD | -24,512.69 USD | `-33.48%` | `0B / 1S` |
| `5:00 UTC` | `100.31` | `100.29` | `100.31` | `100.41` | `100.20` | 9,748,527.75 USD | 5,287,867.77 USD | 4,460,659.98 USD | 827,207.79 USD | `+8.49%` | `1B / 2S` |
| `0:00 UTC` | `100.31` | `100.37` | `100.31` | `100.57` | `100.18` | 15,813,133.46 USD | 8,656,891.75 USD | 7,156,241.72 USD | 1,500,650.03 USD | `+9.49%` | `10B / 4S` |
| `5:00 UTC` | `100.57` | `100.66` | `100.57` | `100.94` | `100.43` | 21,596,195.23 USD | 13,257,846.46 USD | 8,338,348.77 USD | 4,919,497.70 USD | `+22.78%` | `17B / 2S` |
| `0:00 UTC` | `100.95` | `100.94` | `100.95` | `101.07` | `100.72` | 13,472,246.47 USD | 6,374,941.81 USD | 7,097,304.66 USD | -722,362.84 USD | `-5.36%` | `10B / 3S` |
| `5:00 UTC` | `101.00` | `101.01` | `101.00` | `101.28` | `100.85` | 14,129,778.63 USD | 7,872,450.16 USD | 6,257,328.47 USD | 1,615,121.68 USD | `+11.43%` | `13B / 2S` |
| `0:00 UTC` | `101.13` | `101.14` | `101.13` | `101.27` | `100.97` | 14,591,088.89 USD | 5,760,823.82 USD | 8,830,265.07 USD | -3,069,441.25 USD | `-21.04%` | `3B / 3S` |
| `5:00 UTC` | `101.12` | `101.21` | `101.12` | `101.41` | `101.05` | 8,287,817.82 USD | 4,949,702.76 USD | 3,338,115.06 USD | 1,611,587.69 USD | `+19.45%` | `9B / 2S` |
| `0:00 UTC` | `101.80` | `101.69` | `101.80` | `101.95` | `101.28` | 21,400,336.48 USD | 10,768,028.88 USD | 10,632,307.61 USD | 135,721.27 USD | `+0.63%` | `15B / 6S` |
| `5:00 UTC` | `101.68` | `101.64` | `101.68` | `101.91` | `101.38` | 9,829,156.63 USD | 4,338,777.97 USD | 5,490,378.67 USD | -1,151,600.70 USD | `-11.72%` | `10B / 10S` |
| `0:00 UTC` | `102.41` | `102.24` | `102.41` | `102.50` | `101.82` | 63,290,075.98 USD | 31,880,310.97 USD | 31,409,765.01 USD | 470,545.96 USD | `+0.74%` | `25B / 4S` |

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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `100.24` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `104.63`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.25 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.97` (Risk Distance: `1.25` pts)
  * +2.5R Take Profit: `99.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.25 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.62`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
