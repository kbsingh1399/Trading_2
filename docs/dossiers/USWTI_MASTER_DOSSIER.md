# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 04:10:46 IST` (`2026-10-29 22:40:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.49` | **Live Ask Quote**: `103.54` | **Mid Price**: `103.51`
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
  * Session VWAP: `103.51` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.24` | Lower -3.00σ Band: `102.79`
  * Upper +2.51σ Band: `104.08` | Lower -2.51σ Band: `102.94`
  * Upper +2.01σ Band: `103.95` | Lower -2.01σ Band: `103.08`
  * Upper +2.00σ Band: `103.93` | Lower -2.00σ Band: `103.10`
  * Upper +1.28σ Band: `103.80` | Lower -1.28σ Band: `103.22`
  * Upper +1.00σ Band: `103.72` | Lower -1.00σ Band: `103.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.51` | EMA-20=`103.51` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.51` (Slope: `+0.0000`) | EMA-100=`103.51`
  * Institutional Anchors: EMA-144=`103.51` | EMA-200=`103.51` (Slope: `+0.0000`) | EMA-233=`103.51`
- **Range Boundaries**: 24H High=`104.55` | 24H Low=`102.48` | Weekly High=`105.58` | Weekly Low=`101.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `103.50` (Distance: `+0.01%`)
  * Point of Control (POC) = `103.45` (Distance: `+0.06%`)
  * Value Area Low (VAL) = `103.32` (Distance: `+0.19%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.08` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`103.54` | Low=`103.22`
  * London Session (08:00-16:00 UTC): High=`103.93` | Low=`103.10`
  * New York Session (13:00-21:00 UTC): High=`104.13` | Low=`102.89`
  * Initial Balance (First Hour): IB High=`103.82` | IB Low=`103.20`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.10` - `103.93`
  * Optimal Trade Entry (OTE 0.705): `103.72`
  * Structural Invalidation Anchor (0.786): `104.34`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `102.95` | `102.98` | `102.91` | `102.97` | `188` | 19,357.42 USD | 7,604.70 USD | `+39.29%` | 137,536.60 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `102.96` | `103.02` | `102.94` | `102.97` | `203` | 20,902.91 USD | 0.00 USD | `+0.00%` | 137,536.60 USD | `-0.07` | **`NEUTRAL`** | `NEUTRAL CHOP` |
| `5m` | `102.97` | `102.97` | `102.86` | `102.87` | `158` | 16,253.46 USD | -13,205.94 USD | `-81.25%` | 124,330.66 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `102.79` | `103.02` | `102.73` | `102.93` | `689` | 70,921.53 USD | 32,281.52 USD | `+45.52%` | 420,538.83 USD | `+0.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.93` | `103.03` | `102.87` | `102.97` | `704` | 72,490.88 USD | 18,802.32 USD | `+25.94%` | 439,341.15 USD | `-0.06` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.97` | `103.05` | `102.86` | `102.94` | `491` | 50,543.54 USD | -7,775.93 USD | `-15.38%` | 431,565.22 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.97` | `102.88` | `101.90` | `102.56` | `5,791` | 593,913.38 USD | 283,583.00 USD | `+47.75%` | -39,922.68 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.57` | `103.03` | `102.37` | `102.79` | `4,695` | 482,613.14 USD | 151,046.86 USD | `+31.30%` | 111,124.18 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.79` | `103.55` | `102.73` | `103.41` | `3,131` | 323,776.71 USD | 231,808.23 USD | `+71.60%` | 342,932.41 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,749,612.88 USD | `+1.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,027,007.90 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -1,556,424.27 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,749,612.88 USD | `+1.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `42` | `0x0cc1...c7cb` | `LONG` | 30,942,062.95 USD | `300,817.26` | `98.89` | `102.89` | `31.83` | 1,192,561.92 USD | `+3.85%` | `3X Cross` |
| `113` | `0x30af...393e` | `LONG` | 18,277,724.15 USD | `177,712.44` | `100.98` | `102.89` | `93.19` | 332,322.26 USD | `+1.82%` | `10X Isolated` |
| `211` | `0x9e2c...5508` | `LONG` | 10,286,000.00 USD | `100,000.00` | `100.89` | `102.89` | `80.26` | 196,761.86 USD | `+1.91%` | `20X Cross` |
| `293` | `0x7fda...17d1` | `SHORT` | 8,090,476.45 USD | `78,647.58` | `100.15` | `102.89` | `204.56` | -213,854.60 USD | `-2.64%` | `20X Cross` |
| `332` | `0xebe1...4070` | `LONG` | 6,994,476.50 USD | `67,999.97` | `101.87` | `102.89` | `0.000000` | 67,227.52 USD | `+0.96%` | `20X Cross` |
| `334` | `0x10e1...f4bd` | `LONG` | 6,955,997.71 USD | `67,625.88` | `84.36` | `102.89` | `58.53` | 1,250,767.33 USD | `+17.98%` | `3X Isolated` |
| `348` | `0x4692...164f` | `SHORT` | 6,654,570.19 USD | `64,689.12` | `102.33` | `102.89` | `1048.87` | -35,217.30 USD | `-0.53%` | `5X Cross` |
| `402` | `0xea00...a918` | `SHORT` | 5,673,964.20 USD | `55,151.29` | `89.22` | `102.89` | `240.37` | -753,239.71 USD | `-13.28%` | `20X Cross` |
| `525` | `0x5989...bc29` | `SHORT` | 4,175,264.22 USD | `40,591.72` | `99.23` | `102.89` | `111.59` | -147,329.54 USD | `-3.53%` | `10X Cross` |
| `534` | `0xd84a...c8a5` | `SHORT` | 4,114,400.00 USD | `40,000.00` | `101.97` | `102.89` | `119.46` | -35,770.00 USD | `-0.87%` | `20X Cross` |
| `540` | `0xd507...c948` | `LONG` | 4,094,303.92 USD | `39,808.50` | `93.57` | `102.89` | `81.34` | 369,228.50 USD | `+9.02%` | `7X Isolated` |
| `674` | `0x354b...6425` | `SHORT` | 3,397,062.07 USD | `33,026.07` | `101.86` | `102.89` | `435.67` | -33,124.33 USD | `-0.98%` | `8X Cross` |
| `706` | `0xb5e7...eff1` | `SHORT` | 3,202,267.14 USD | `31,132.29` | `91.71` | `102.89` | `144.78` | -347,058.50 USD | `-10.84%` | `20X Cross` |
| `795` | `0x61d7...7dee` | `LONG` | 2,865,482.62 USD | `27,858.08` | `88.25` | `102.89` | `83.50` | 407,006.62 USD | `+14.20%` | `20X Cross` |
| `875` | `0xf0ae...2f74` | `SHORT` | 2,571,250.00 USD | `25,000.00` | `100.78` | `102.89` | `175.76` | -51,731.39 USD | `-2.01%` | `20X Cross` |
| `886` | `0xb8f3...04ea` | `SHORT` | 2,526,028.50 USD | `24,560.32` | `102.91` | `102.89` | `114.77` | 1,478.49 USD | `+0.06%` | `7X Isolated` |
| `895` | `0x645b...87b8` | `SHORT` | 2,500,033.56 USD | `24,302.84` | `101.22` | `102.89` | `134.76` | -40,072.00 USD | `-1.60%` | `3X Isolated` |
| `902` | `0xce97...7e78` | `SHORT` | 2,485,405.15 USD | `24,162.99` | `102.72` | `102.89` | `120.31` | -3,261.55 USD | `-0.13%` | `5X Isolated` |
| `966` | `0x58f0...0d20` | `SHORT` | 2,315,537.62 USD | `22,511.55` | `96.77` | `102.89` | `113.39` | -137,119.83 USD | `-5.92%` | `20X Cross` |
| `1038` | `0xfc66...ca06` | `SHORT` | 2,115,514.83 USD | `20,566.93` | `101.34` | `102.89` | `862.09` | -31,331.36 USD | `-1.48%` | `3X Cross` |
| `1083` | `0x9aa5...58af` | `SHORT` | 2,023,555.77 USD | `19,671.00` | `101.76` | `102.89` | `564.78` | -21,804.84 USD | `-1.08%` | `20X Cross` |
| `1190` | `0xe5dd...ecba` | `SHORT` | 1,870,221.01 USD | `18,183.97` | `102.71` | `102.89` | `138.69` | -2,554.29 USD | `-0.14%` | `20X Cross` |
| `1254` | `0x91fd...9841` | `LONG` | 1,783,075.84 USD | `17,334.98` | `101.72` | `102.89` | `96.17` | 19,820.53 USD | `+1.11%` | `13X Isolated` |
| `1268` | `0x4169...6f06` | `LONG` | 1,766,468.29 USD | `17,175.19` | `76.61` | `102.89` | `82.98` | 450,700.29 USD | `+25.51%` | `12X Isolated` |
| `1282` | `0x6788...98d4` | `SHORT` | 1,748,790.00 USD | `17,000.00` | `99.31` | `102.89` | `198.33` | -60,465.41 USD | `-3.46%` | `20X Cross` |
| `1340` | `0xa99c...40d5` | `SHORT` | 1,656,046.00 USD | `16,100.00` | `101.02` | `102.89` | `154.34` | -29,588.63 USD | `-1.79%` | `20X Cross` |
| `1349` | `0x1bf6...5bfa` | `SHORT` | 1,645,760.00 USD | `16,000.00` | `99.60` | `102.89` | `225.91` | -52,137.69 USD | `-3.17%` | `20X Cross` |
| `1440` | `0x34ea...2f47` | `SHORT` | 1,542,900.00 USD | `15,000.00` | `99.80` | `102.89` | `199.63` | -45,898.69 USD | `-2.97%` | `20X Cross` |
| `1441` | `0x5d6f...6f8a` | `LONG` | 1,542,750.00 USD | `15,000.00` | `101.91` | `102.89` | `28.60` | 14,095.00 USD | `+0.91%` | `20X Cross` |
| `1549` | `0xfb29...21dd` | `LONG` | 1,414,037.35 USD | `13,744.53` | `89.85` | `102.89` | `84.67` | 179,043.39 USD | `+12.66%` | `20X Cross` |
| `1570` | `0x6fa6...825e` | `SHORT` | 1,388,475.00 USD | `13,500.00` | `102.95` | `102.89` | `135.50` | 1,299.27 USD | `+0.09%` | `20X Isolated` |
| `1590` | `0xa9d9...b48e` | `SHORT` | 1,371,466.63 USD | `13,333.33` | `96.39` | `102.89` | `174.31` | -86,219.45 USD | `-6.29%` | `20X Cross` |
| `1641` | `0x936c...bb0f` | `SHORT` | 1,305,078.22 USD | `12,687.91` | `101.39` | `102.89` | `163.64` | -18,605.35 USD | `-1.43%` | `2X Isolated` |
| `1670` | `0x89c2...c94b` | `LONG` | 1,271,832.12 USD | `12,364.69` | `75.25` | `102.89` | `45.76` | 341,348.96 USD | `+26.84%` | `3X Isolated` |
| `1707` | `0xcd81...36e3` | `SHORT` | 1,241,140.62 USD | `12,063.96` | `97.96` | `102.89` | `109.75` | -59,301.70 USD | `-4.78%` | `20X Cross` |
| `1717` | `0x436c...b3d1` | `SHORT` | 1,234,320.00 USD | `12,000.00` | `101.05` | `102.89` | `208.97` | -21,660.17 USD | `-1.75%` | `20X Cross` |
| `1779` | `0x9dea...d617` | `LONG` | 1,172,572.07 USD | `11,400.80` | `90.37` | `102.89` | `5.05` | 142,298.35 USD | `+12.14%` | `20X Cross` |
| `1789` | `0x17c3...a868` | `LONG` | 1,162,996.57 USD | `11,306.60` | `95.13` | `102.89` | `64.99` | 87,349.70 USD | `+7.51%` | `3X Isolated` |
| `1825` | `0x8607...08d5` | `SHORT` | 1,131,154.79 USD | `10,998.10` | `92.18` | `102.89` | `135.02` | -117,365.09 USD | `-10.38%` | `4X Isolated` |
| `1920` | `0x7717...bd7e` | `SHORT` | 1,051,250.49 USD | `10,220.21` | `102.34` | `102.89` | `137.31` | -5,292.51 USD | `-0.50%` | `20X Cross` |
| `1947` | `0xf29c...9971` | `SHORT` | 1,028,600.00 USD | `10,000.00` | `101.10` | `102.89` | `118.37` | -17,603.97 USD | `-1.71%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `102.32` | 625.79 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 0.63K USD at 102.3200 USD [API] | `2026-10-28 14:18:07` |
| `ANNOUNCEMENT` | `INFO` | `102.32` | 2,071.37 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.07K USD at 102.3200 USD [API] | `2026-10-28 14:18:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.89` (Vol: 2,900,000.00 USD, Dist: `+1.02%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--3.57%`)
  * 48H Horizon: Short MP=`104.00` (Vol: 7,100,000.00 USD, Dist: `+1.12%`) | Long MP=`99.18` (Vol: 4,000,000.00 USD, Dist: `--3.56%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 7,000,000.00 USD, Dist: `+1.16%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.49%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 11,000,000.00 USD, Dist: `+1.11%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--3.49%`)
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
  * Current Rate: `-294.37K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
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
| `21:55:00` | `102.79` | `102.79` | `102.79` | `102.85` | `102.70` | 21,175.36 USD | 11,646.45 USD | 9,528.91 USD | 2,117.54 USD | `+10.00%` | `1B / 0S` |
| `22:00:00` | `103.41` | `103.41` | `103.41` | `103.55` | `102.73` | 323,776.71 USD | 277,792.47 USD | 45,984.24 USD | 231,808.23 USD | `+71.60%` | `1B / 0S` |
| `22:00:00` | `102.77` | `102.77` | `102.77` | `102.80` | `102.73` | 21,787.24 USD | 10,271.13 USD | 11,516.11 USD | -1,244.99 USD | `-5.71%` | `0B / 1S` |
| `22:00:00` | `102.93` | `102.93` | `102.93` | `103.02` | `102.73` | 70,921.53 USD | 51,601.52 USD | 19,320.00 USD | 32,281.52 USD | `+45.52%` | `1B / 0S` |
| `22:05:00` | `102.83` | `102.83` | `102.83` | `102.85` | `102.76` | 20,669.83 USD | 17,224.86 USD | 3,444.97 USD | 13,779.89 USD | `+66.67%` | `1B / 0S` |
| `22:10:00` | `102.93` | `102.93` | `102.93` | `103.02` | `102.84` | 28,409.78 USD | 18,229.61 USD | 10,180.17 USD | 8,049.44 USD | `+28.33%` | `1B / 0S` |
| `22:15:00` | `102.97` | `102.97` | `102.97` | `103.03` | `102.87` | 72,490.88 USD | 45,646.60 USD | 26,844.28 USD | 18,802.32 USD | `+25.94%` | `1B / 0S` |
| `22:15:00` | `102.94` | `102.94` | `102.94` | `103.03` | `102.87` | 32,221.78 USD | 16,513.66 USD | 15,708.12 USD | 805.54 USD | `+2.50%` | `1B / 0S` |
| `22:20:00` | `102.97` | `102.97` | `102.97` | `102.98` | `102.91` | 19,357.42 USD | 13,481.06 USD | 5,876.36 USD | 7,604.70 USD | `+39.29%` | `1B / 0S` |
| `22:25:00` | `102.97` | `102.97` | `102.97` | `103.02` | `102.94` | 20,902.91 USD | 10,451.45 USD | 10,451.45 USD | 0.00 USD | `+0.00%` | `0B / 0S` |
| `5:00 UTC` | `103.02` | `102.95` | `103.02` | `103.06` | `102.82` | 8,073,511.20 USD | 2,057,722.32 USD | 6,015,788.89 USD | -3,958,066.57 USD | `-49.03%` | `1B / 13S` |
| `0:00 UTC` | `102.87` | `102.93` | `102.87` | `103.02` | `102.84` | 8,092,099.96 USD | 4,143,913.94 USD | 3,948,186.02 USD | 195,727.93 USD | `+2.42%` | `2B / 2S` |
| `5:00 UTC` | `102.81` | `102.87` | `102.81` | `103.02` | `102.78` | 25,235,874.42 USD | 17,074,162.87 USD | 8,161,711.55 USD | 8,912,451.33 USD | `+35.32%` | `6B / 1S` |
| `0:00 UTC` | `102.00` | `102.25` | `102.00` | `102.98` | `101.69` | 44,005,448.45 USD | 22,985,881.99 USD | 21,019,566.46 USD | 1,966,315.53 USD | `+4.47%` | `19B / 33S` |
| `5:00 UTC` | `101.85` | `102.09` | `101.85` | `102.65` | `101.69` | 23,974,978.54 USD | 13,713,172.54 USD | 10,261,806.01 USD | 3,451,366.53 USD | `+14.40%` | `18B / 9S` |
| `0:00 UTC` | `102.47` | `102.50` | `102.47` | `102.60` | `102.41` | 5,469,868.87 USD | 2,184,741.26 USD | 3,285,127.61 USD | -1,100,386.35 USD | `-20.12%` | `0B / 3S` |
| `5:00 UTC` | `102.62` | `102.58` | `102.62` | `102.66` | `102.50` | 2,045,755.51 USD | 1,077,529.04 USD | 968,226.47 USD | 109,302.57 USD | `+5.34%` | `4B / 1S` |
| `0:00 UTC` | `102.81` | `102.76` | `102.81` | `102.90` | `102.62` | 32,144,198.79 USD | 20,601,970.33 USD | 11,542,228.47 USD | 9,059,741.86 USD | `+28.18%` | `6B / 1S` |
| `5:00 UTC` | `102.85` | `102.84` | `102.85` | `102.93` | `102.69` | 14,929,076.99 USD | 7,121,697.65 USD | 7,807,379.34 USD | -685,681.69 USD | `-4.59%` | `0B / 4S` |
| `0:00 UTC` | `102.90` | `102.90` | `102.90` | `102.94` | `102.84` | 1,903,309.93 USD | 1,264,041.91 USD | 639,268.01 USD | 624,773.90 USD | `+32.83%` | `1B / 1S` |

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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.32` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.05` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `106.49`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `103.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.77` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `100.33`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.34`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
