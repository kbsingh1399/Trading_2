# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 00:08:07 IST` (`2026-10-29 18:38:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.89` | **Live Ask Quote**: `102.92` | **Mid Price**: `102.90`
- **Spread Points**: `30.00` | **Spread BPS**: `2.92 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.89` | VWAP Z-Score: `+1.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4245` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `62.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.56` | Lower -3.00σ Band: `100.23`
  * Upper +2.51σ Band: `103.29` | Lower -2.51σ Band: `100.50`
  * Upper +2.01σ Band: `103.01` | Lower -2.01σ Band: `100.78`
  * Upper +2.00σ Band: `103.01` | Lower -2.00σ Band: `100.78`
  * Upper +1.28σ Band: `102.61` | Lower -1.28σ Band: `101.18`
  * Upper +1.00σ Band: `102.45` | Lower -1.00σ Band: `101.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.29` | EMA-20=`102.01` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`101.98` (Slope: `+0.0000`) | EMA-100=`102.10`
  * Institutional Anchors: EMA-144=`102.15` | EMA-200=`102.11` (Slope: `-0.0038`) | EMA-233=`102.06`
- **Range Boundaries**: 24H High=`103.78` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.75` (Distance: `+0.13%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.84%`)
  * Value Area Low (VAL) = `101.55` (Distance: `+1.32%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `102.49` - `103.31`
  * Optimal Trade Entry (OTE 0.705): `103.11`
  * Structural Invalidation Anchor (0.786): `103.73`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.83` | `100.98` | `100.81` | `100.91` | `587` | 59,235.93 USD | 21,540.34 USD | `+36.36%` | -234,600.65 USD | `+0.52` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `100.90` | `100.98` | `100.77` | `100.88` | `635` | 64,057.53 USD | -2,343.57 USD | `-3.66%` | -236,944.22 USD | `+0.04` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `100.87` | `101.06` | `100.85` | `101.02` | `638` | 64,452.04 USD | 44,749.87 USD | `+69.43%` | -192,194.35 USD | `+1.29` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `100.94` | `101.15` | `100.68` | `100.96` | `1,945` | 196,371.09 USD | 25,019.44 USD | `+12.74%` | -229,688.39 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `100.96` | `101.02` | `100.79` | `100.91` | `1,529` | 154,295.98 USD | -7,681.40 USD | `-4.98%` | -237,369.79 USD | `+0.06` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `100.90` | `101.16` | `100.77` | `101.06` | `1,856` | 187,572.93 USD | 85,369.73 USD | `+45.51%` | -152,000.06 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.97` | `101.98` | `100.46` | `101.17` | `10,331` | 1,045,156.28 USD | -311,556.76 USD | `-29.81%` | -1,398,780.40 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.16` | `101.85` | `100.81` | `100.95` | `8,946` | 903,080.81 USD | -425,750.58 USD | `-47.14%` | -1,824,530.98 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `100.94` | `101.53` | `100.68` | `101.35` | `7,439` | 753,964.97 USD | 405,912.66 USD | `+53.84%` | -1,418,618.32 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:05:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,716,450.01 USD | `300,817.26` | `98.89` | `102.10` | `32.33` | 966,948.98 USD | `+3.15%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,144,439.82 USD | `177,712.44` | `100.98` | `102.10` | `93.19` | 199,037.93 USD | `+1.10%` | `10X Isolated` |
| `162` | `0x58f0...0d20` | `SHORT` | 12,892,461.08 USD | `126,260.51` | `96.77` | `102.10` | `103.89` | -674,368.66 USD | `-5.23%` | `20X Cross` |
| `218` | `0x9e2c...5508` | `LONG` | 10,211,000.00 USD | `100,000.00` | `100.89` | `102.10` | `79.64` | 121,761.86 USD | `+1.19%` | `20X Cross` |
| `238` | `0xebe1...4070` | `LONG` | 9,904,665.92 USD | `96,999.96` | `101.87` | `102.10` | `0.000000` | 23,148.12 USD | `+0.23%` | `20X Cross` |
| `307` | `0x7fda...17d1` | `SHORT` | 8,041,702.81 USD | `78,763.01` | `100.15` | `102.10` | `208.11` | -153,520.95 USD | `-1.91%` | `20X Cross` |
| `343` | `0x10e1...f4bd` | `LONG` | 6,904,602.04 USD | `67,625.88` | `84.36` | `102.10` | `58.54` | 1,199,371.66 USD | `+17.37%` | `3X Isolated` |
| `382` | `0x4692...164f` | `SHORT` | 6,364,284.92 USD | `62,327.73` | `101.43` | `102.10` | `1042.61` | -42,188.65 USD | `-0.66%` | `5X Cross` |
| `408` | `0x0c4a...1b19` | `SHORT` | 5,697,480.48 USD | `55,802.94` | `102.08` | `102.10` | `106.83` | -833.10 USD | `-0.01%` | `20X Isolated` |
| `418` | `0xea00...a918` | `SHORT` | 5,631,497.71 USD | `55,151.29` | `89.22` | `102.10` | `275.05` | -710,773.22 USD | `-12.62%` | `20X Cross` |
| `553` | `0x5989...bc29` | `SHORT` | 4,144,820.43 USD | `40,591.72` | `99.23` | `102.10` | `111.59` | -116,885.75 USD | `-2.82%` | `10X Cross` |
| `568` | `0xd507...c948` | `LONG` | 4,064,845.63 USD | `39,808.50` | `93.57` | `102.10` | `81.35` | 339,770.22 USD | `+8.36%` | `7X Isolated` |
| `696` | `0x354b...6425` | `SHORT` | 3,321,234.15 USD | `32,526.04` | `101.19` | `102.10` | `436.67` | -29,999.28 USD | `-0.90%` | `8X Cross` |
| `734` | `0xb5e7...eff1` | `SHORT` | 3,178,606.60 USD | `31,132.29` | `91.71` | `102.10` | `145.11` | -323,397.96 USD | `-10.17%` | `20X Cross` |
| `770` | `0xd84a...c8a5` | `SHORT` | 3,063,000.00 USD | `30,000.00` | `101.76` | `102.10` | `126.40` | -10,150.00 USD | `-0.33%` | `20X Cross` |
| `817` | `0x61d7...7dee` | `LONG` | 2,844,589.06 USD | `27,858.08` | `88.25` | `102.10` | `83.50` | 386,113.06 USD | `+13.57%` | `20X Cross` |
| `896` | `0xf0ae...2f74` | `SHORT` | 2,552,500.00 USD | `25,000.00` | `100.78` | `102.10` | `173.53` | -32,981.39 USD | `-1.29%` | `20X Cross` |
| `907` | `0xfc66...ca06` | `SHORT` | 2,528,669.60 USD | `24,764.17` | `101.14` | `102.10` | `1789.28` | -23,941.00 USD | `-0.95%` | `3X Cross` |
| `914` | `0xb8f3...04ea` | `SHORT` | 2,507,853.87 USD | `24,560.32` | `102.91` | `102.10` | `114.78` | 19,653.13 USD | `+0.78%` | `7X Isolated` |
| `922` | `0x645b...87b8` | `SHORT` | 2,481,563.40 USD | `24,302.84` | `101.22` | `102.10` | `134.77` | -21,601.84 USD | `-0.87%` | `3X Isolated` |
| `1125` | `0x9aa5...58af` | `SHORT` | 2,008,605.81 USD | `19,671.00` | `101.76` | `102.10` | `490.64` | -6,854.88 USD | `-0.34%` | `20X Cross` |
| `1294` | `0x4169...6f06` | `LONG` | 1,753,586.90 USD | `17,175.19` | `76.61` | `102.10` | `82.99` | 437,818.90 USD | `+24.97%` | `12X Isolated` |
| `1308` | `0x6788...98d4` | `SHORT` | 1,735,870.00 USD | `17,000.00` | `99.31` | `102.10` | `192.53` | -47,545.41 USD | `-2.74%` | `20X Cross` |
| `1370` | `0xa99c...40d5` | `SHORT` | 1,643,971.00 USD | `16,100.00` | `101.02` | `102.10` | `157.39` | -17,513.63 USD | `-1.07%` | `20X Cross` |
| `1376` | `0x1bf6...5bfa` | `SHORT` | 1,633,760.00 USD | `16,000.00` | `99.60` | `102.10` | `224.04` | -40,137.69 USD | `-2.46%` | `20X Cross` |
| `1381` | `0xfdfb...dbb9` | `SHORT` | 1,630,359.63 USD | `15,966.70` | `101.16` | `102.10` | `106.88` | -15,130.13 USD | `-0.93%` | `20X Cross` |
| `1463` | `0x91fd...9841` | `LONG` | 1,545,281.25 USD | `15,134.98` | `101.16` | `102.10` | `95.58` | 14,205.76 USD | `+0.92%` | `13X Isolated` |
| `1474` | `0x17c3...a868` | `LONG` | 1,532,765.55 USD | `15,010.92` | `95.13` | `102.10` | `64.99` | 104,709.48 USD | `+6.83%` | `3X Isolated` |
| `1476` | `0x34ea...2f47` | `SHORT` | 1,531,650.00 USD | `15,000.00` | `99.80` | `102.10` | `193.51` | -34,648.69 USD | `-2.26%` | `20X Cross` |
| `1584` | `0xfb29...21dd` | `LONG` | 1,403,316.62 USD | `13,744.53` | `89.85` | `102.10` | `84.55` | 168,322.65 USD | `+11.99%` | `20X Cross` |
| `1600` | `0x6fa6...825e` | `SHORT` | 1,378,485.00 USD | `13,500.00` | `102.95` | `102.10` | `135.50` | 11,289.27 USD | `+0.82%` | `20X Isolated` |
| `1601` | `0x5d6f...6f8a` | `LONG` | 1,378,350.00 USD | `13,500.00` | `101.84` | `102.10` | `21.91` | 3,545.00 USD | `+0.26%` | `20X Cross` |
| `1619` | `0xa9d9...b48e` | `SHORT` | 1,361,333.30 USD | `13,333.33` | `96.39` | `102.10` | `175.39` | -76,086.11 USD | `-5.59%` | `20X Cross` |
| `1725` | `0x89c2...c94b` | `LONG` | 1,262,558.60 USD | `12,364.69` | `75.25` | `102.10` | `45.77` | 332,075.45 USD | `+26.30%` | `3X Isolated` |
| `1739` | `0xcd81...36e3` | `SHORT` | 1,231,851.36 USD | `12,063.96` | `97.96` | `102.10` | `111.30` | -50,012.44 USD | `-4.06%` | `20X Cross` |
| `1746` | `0x436c...b3d1` | `SHORT` | 1,225,320.00 USD | `12,000.00` | `101.05` | `102.10` | `203.15` | -12,660.17 USD | `-1.03%` | `20X Cross` |
| `1810` | `0x9dea...d617` | `LONG` | 1,164,135.48 USD | `11,400.80` | `90.37` | `102.10` | `2.34` | 133,861.76 USD | `+11.50%` | `20X Cross` |
| `1850` | `0x8afa...8113` | `SHORT` | 1,133,593.77 USD | `11,101.69` | `100.52` | `102.10` | `107.79` | -17,649.26 USD | `-1.56%` | `10X Isolated` |
| `1856` | `0x8607...08d5` | `SHORT` | 1,123,016.20 USD | `10,998.10` | `92.18` | `102.10` | `135.03` | -109,226.49 USD | `-9.73%` | `4X Isolated` |
| `1986` | `0xf29c...9971` | `SHORT` | 1,021,100.00 USD | `10,000.00` | `101.10` | `102.10` | `118.37` | -10,103.97 USD | `-0.99%` | `5X Isolated` |
| `1989` | `0xfc27...9d9d` | `LONG` | 1,016,819.75 USD | `9,958.08` | `101.58` | `102.10` | `0.000000` | 5,269.19 USD | `+0.52%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.09` (Vol: 2,100,000.00 USD, Dist: `+0.86%`) | Long MP=`99.20` (Vol: 6,700,000.00 USD, Dist: `--2.95%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.98%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.90%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+1.73%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `101.35` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `103.49` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-48.87K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `17:55:00` | `100.95` | `100.95` | `100.95` | `101.03` | `100.81` | 53,098.65 USD | 34,065.57 USD | 19,033.08 USD | 15,032.49 USD | `+28.31%` | `1B / 0S` |
| `18:00:00` | `101.35` | `101.35` | `101.35` | `101.53` | `100.68` | 753,964.97 USD | 579,938.81 USD | 174,026.15 USD | 405,912.66 USD | `+53.84%` | `1B / 0S` |
| `18:00:00` | `101.03` | `101.03` | `101.03` | `101.15` | `100.92` | 72,944.38 USD | 43,577.16 USD | 29,367.22 USD | 14,209.94 USD | `+19.48%` | `1B / 0S` |
| `18:00:00` | `100.96` | `100.96` | `100.96` | `101.15` | `100.68` | 196,371.09 USD | 110,695.27 USD | 85,675.82 USD | 25,019.44 USD | `+12.74%` | `1B / 0S` |
| `18:05:00` | `100.74` | `100.74` | `100.74` | `101.03` | `100.68` | 64,374.78 USD | 8,676.60 USD | 55,698.18 USD | -47,021.58 USD | `-73.04%` | `0B / 1S` |
| `18:10:00` | `100.96` | `100.96` | `100.96` | `100.98` | `100.74` | 58,961.81 USD | 56,013.72 USD | 2,948.09 USD | 53,065.63 USD | `+90.00%` | `1B / 0S` |
| `18:15:00` | `100.91` | `100.91` | `100.91` | `101.02` | `100.79` | 154,295.98 USD | 73,307.29 USD | 80,988.69 USD | -7,681.40 USD | `-4.98%` | `0B / 1S` |
| `18:15:00` | `100.86` | `100.86` | `100.86` | `101.02` | `100.79` | 53,353.88 USD | 15,821.39 USD | 37,532.49 USD | -21,711.10 USD | `-40.69%` | `0B / 1S` |
| `18:20:00` | `100.83` | `100.83` | `100.83` | `100.91` | `100.80` | 41,644.03 USD | 13,723.60 USD | 27,920.43 USD | -14,196.83 USD | `-34.09%` | `0B / 1S` |
| `18:25:00` | `100.91` | `100.91` | `100.91` | `100.98` | `100.81` | 59,235.93 USD | 40,388.13 USD | 18,847.80 USD | 21,540.34 USD | `+36.36%` | `1B / 0S` |
| `5:00 UTC` | `101.00` | `101.01` | `101.00` | `101.28` | `100.85` | 14,129,778.63 USD | 7,872,450.16 USD | 6,257,328.47 USD | 1,615,121.68 USD | `+11.43%` | `13B / 2S` |
| `0:00 UTC` | `101.13` | `101.14` | `101.13` | `101.27` | `100.97` | 14,591,088.89 USD | 5,760,823.82 USD | 8,830,265.07 USD | -3,069,441.25 USD | `-21.04%` | `3B / 3S` |
| `5:00 UTC` | `101.12` | `101.21` | `101.12` | `101.41` | `101.05` | 8,287,817.82 USD | 4,949,702.76 USD | 3,338,115.06 USD | 1,611,587.69 USD | `+19.45%` | `9B / 2S` |
| `0:00 UTC` | `101.80` | `101.69` | `101.80` | `101.95` | `101.28` | 21,400,336.48 USD | 10,768,028.88 USD | 10,632,307.61 USD | 135,721.27 USD | `+0.63%` | `15B / 6S` |
| `5:00 UTC` | `101.68` | `101.64` | `101.68` | `101.91` | `101.38` | 9,829,156.63 USD | 4,338,777.97 USD | 5,490,378.67 USD | -1,151,600.70 USD | `-11.72%` | `10B / 10S` |
| `0:00 UTC` | `102.41` | `102.23` | `102.41` | `102.50` | `101.82` | 76,189,579.98 USD | 39,225,207.15 USD | 36,964,372.83 USD | 2,260,834.33 USD | `+2.97%` | `20B / 3S` |
| `5:00 UTC` | `102.02` | `102.01` | `102.02` | `102.13` | `101.85` | 13,174,401.35 USD | 6,982,040.79 USD | 6,192,360.55 USD | 789,680.24 USD | `+5.99%` | `1B / 6S` |
| `0:00 UTC` | `101.95` | `101.91` | `101.95` | `102.02` | `101.77` | 7,849,002.75 USD | 3,456,195.71 USD | 4,392,807.03 USD | -936,611.32 USD | `-11.93%` | `2B / 3S` |
| `5:00 UTC` | `102.00` | `102.03` | `102.00` | `102.18` | `101.80` | 13,778,364.28 USD | 6,276,241.74 USD | 7,502,122.54 USD | -1,225,880.80 USD | `-8.90%` | `6B / 5S` |
| `0:00 UTC` | `102.27` | `102.19` | `102.27` | `102.32` | `102.00` | 4,795,698.83 USD | 2,667,053.48 USD | 2,128,645.35 USD | 538,408.13 USD | `+11.23%` | `12B / 7S` |

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
  * `2026-10-29 23:31:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:27 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:27 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.99` (Risk Distance: `0.5544` pts)
  * +2.5R Take Profit: `102.93`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.55 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.30` (Risk Distance: `0.5544` pts)
  * +2.5R Take Profit: `101.36`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.55 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.73`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
