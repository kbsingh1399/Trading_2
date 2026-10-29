# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 04:38:03 IST` (`2026-10-29 23:08:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.42` | **Live Ask Quote**: `103.47` | **Mid Price**: `103.44`
- **Spread Points**: `46.00` | **Spread BPS**: `4.45 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `102.02` | VWAP Z-Score: `+2.17` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.3023` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.11` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.99` | Lower -3.00σ Band: `100.04`
  * Upper +2.51σ Band: `103.67` | Lower -2.51σ Band: `100.36`
  * Upper +2.01σ Band: `103.34` | Lower -2.01σ Band: `100.69`
  * Upper +2.00σ Band: `103.34` | Lower -2.00σ Band: `100.70`
  * Upper +1.28σ Band: `102.86` | Lower -1.28σ Band: `101.17`
  * Upper +1.00σ Band: `102.68` | Lower -1.00σ Band: `101.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.35` | EMA-20=`103.01` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.55` (Slope: `+0.0000`) | EMA-100=`102.39`
  * Institutional Anchors: EMA-144=`102.35` | EMA-200=`102.22` (Slope: `+0.1390`) | EMA-233=`102.19`
- **Range Boundaries**: 24H High=`103.64` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `103.51` (Distance: `-0.11%`)
  * Point of Control (POC) = `103.45` (Distance: `-0.05%`)
  * Value Area Low (VAL) = `103.34` (Distance: `+0.05%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.08` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`103.54` | Low=`103.22`
  * London Session (08:00-16:00 UTC): High=`103.86` | Low=`103.03`
  * New York Session (13:00-21:00 UTC): High=`104.06` | Low=`102.82`
  * Initial Balance (First Hour): IB High=`103.75` | IB Low=`103.13`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.03` - `103.86`
  * Optimal Trade Entry (OTE 0.705): `103.65`
  * Structural Invalidation Anchor (0.786): `104.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.39` | `103.55` | `103.26` | `103.41` | `527` | 54,497.07 USD | 3,824.36 USD | `+7.02%` | 248,761.43 USD | `-0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `103.41` | `103.63` | `103.39` | `103.61` | `440` | 45,587.96 USD | 37,865.92 USD | `+83.06%` | 286,627.35 USD | `+1.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.60` | `103.60` | `103.39` | `103.50` | `433` | 44,817.23 USD | -9,603.69 USD | `-21.43%` | 277,023.65 USD | `-0.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `102.97` | `103.05` | `102.86` | `102.94` | `491` | 50,543.54 USD | -7,775.93 USD | `-15.38%` | 410,780.33 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `102.94` | `103.55` | `102.92` | `103.41` | `1,247` | 128,952.27 USD | 85,624.31 USD | `+66.40%` | 496,404.64 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.41` | `103.63` | `103.39` | `103.47` | `1,184` | 122,514.40 USD | 1,250.15 USD | `+1.02%` | 497,654.78 USD | `-0.63` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `102.57` | `103.03` | `102.37` | `102.79` | `4,695` | 482,613.14 USD | 151,046.86 USD | `+31.30%` | -143,180.00 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.79` | `103.55` | `102.73` | `103.41` | `3,131` | 323,776.71 USD | 231,808.23 USD | `+71.60%` | 88,628.23 USD | `+0.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.41` | `103.64` | `103.39` | `103.54` | `3,425` | 354,634.78 USD | 138,377.10 USD | `+39.02%` | 227,005.33 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `41` | `0x0cc1...c7cb` | `LONG` | 30,914,989.40 USD | `300,817.26` | `98.89` | `102.78` | `31.89` | 1,165,488.37 USD | `+3.77%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,259,952.90 USD | `177,712.44` | `100.98` | `102.78` | `93.19` | 314,551.01 USD | `+1.72%` | `10X Isolated` |
| `208` | `0x9e2c...5508` | `LONG` | 10,278,000.00 USD | `100,000.00` | `100.89` | `102.78` | `80.64` | 188,761.86 USD | `+1.84%` | `20X Cross` |
| `287` | `0x7fda...17d1` | `SHORT` | 8,081,038.74 USD | `78,647.58` | `100.15` | `102.78` | `204.31` | -204,416.89 USD | `-2.53%` | `20X Cross` |
| `328` | `0x10e1...f4bd` | `LONG` | 6,950,587.64 USD | `67,625.88` | `84.36` | `102.78` | `58.53` | 1,245,357.26 USD | `+17.92%` | `3X Isolated` |
| `353` | `0x4692...164f` | `SHORT` | 6,538,317.53 USD | `63,620.88` | `102.40` | `102.78` | `1073.62` | -23,471.78 USD | `-0.36%` | `5X Cross` |
| `372` | `0xebe1...4070` | `LONG` | 6,268,966.51 USD | `60,999.97` | `101.87` | `102.78` | `0.000000` | 54,817.04 USD | `+0.87%` | `20X Cross` |
| `398` | `0xea00...a918` | `SHORT` | 5,667,897.56 USD | `55,151.29` | `89.22` | `102.78` | `236.53` | -747,173.07 USD | `-13.18%` | `20X Cross` |
| `492` | `0x354b...6425` | `SHORT` | 4,444,599.12 USD | `43,248.02` | `102.10` | `102.78` | `356.59` | -29,103.45 USD | `-0.65%` | `8X Cross` |
| `520` | `0x5989...bc29` | `SHORT` | 4,171,610.96 USD | `40,591.72` | `99.23` | `102.78` | `111.59` | -143,676.28 USD | `-3.44%` | `10X Cross` |
| `526` | `0xd84a...c8a5` | `SHORT` | 4,110,400.00 USD | `40,000.00` | `101.97` | `102.78` | `119.50` | -31,770.00 USD | `-0.77%` | `20X Cross` |
| `533` | `0xd507...c948` | `LONG` | 4,091,517.32 USD | `39,808.50` | `93.57` | `102.78` | `81.34` | 366,441.91 USD | `+8.96%` | `7X Isolated` |
| `697` | `0xb5e7...eff1` | `SHORT` | 3,199,153.91 USD | `31,132.29` | `91.71` | `102.78` | `144.50` | -343,945.27 USD | `-10.75%` | `20X Cross` |
| `794` | `0x61d7...7dee` | `LONG` | 2,862,975.40 USD | `27,858.08` | `88.25` | `102.78` | `83.50` | 404,499.39 USD | `+14.13%` | `20X Cross` |
| `872` | `0xce97...7e78` | `SHORT` | 2,569,314.20 USD | `25,005.49` | `102.73` | `102.78` | `120.32` | -511.11 USD | `-0.02%` | `5X Isolated` |
| `873` | `0xf0ae...2f74` | `SHORT` | 2,568,750.00 USD | `25,000.00` | `100.78` | `102.78` | `177.57` | -49,231.39 USD | `-1.92%` | `20X Cross` |
| `885` | `0xb8f3...04ea` | `SHORT` | 2,524,309.28 USD | `24,560.32` | `102.91` | `102.78` | `114.77` | 3,197.71 USD | `+0.13%` | `7X Isolated` |
| `892` | `0x645b...87b8` | `SHORT` | 2,497,603.28 USD | `24,302.84` | `101.22` | `102.78` | `134.76` | -37,641.72 USD | `-1.51%` | `3X Isolated` |
| `970` | `0x58f0...0d20` | `SHORT` | 2,313,511.58 USD | `22,511.55` | `96.77` | `102.78` | `110.97` | -135,093.79 USD | `-5.84%` | `20X Cross` |
| `1079` | `0x9aa5...58af` | `SHORT` | 2,021,785.38 USD | `19,671.00` | `101.76` | `102.78` | `573.93` | -20,034.45 USD | `-0.99%` | `20X Cross` |
| `1189` | `0xe5dd...ecba` | `SHORT` | 1,868,402.61 USD | `18,183.97` | `102.71` | `102.78` | `138.64` | -735.89 USD | `-0.04%` | `20X Cross` |
| `1244` | `0xfc66...ca06` | `SHORT` | 1,798,031.90 USD | `17,497.39` | `101.34` | `102.78` | `898.28` | -24,905.53 USD | `-1.39%` | `3X Cross` |
| `1262` | `0x4169...6f06` | `LONG` | 1,764,750.77 USD | `17,175.19` | `76.61` | `102.78` | `82.98` | 448,982.77 USD | `+25.44%` | `12X Isolated` |
| `1264` | `0x91fd...9841` | `LONG` | 1,759,350.57 USD | `17,120.97` | `101.72` | `102.78` | `96.17` | 17,863.74 USD | `+1.02%` | `13X Isolated` |
| `1270` | `0x6788...98d4` | `SHORT` | 1,747,090.00 USD | `17,000.00` | `99.31` | `102.78` | `199.48` | -58,765.41 USD | `-3.36%` | `20X Cross` |
| `1330` | `0xa99c...40d5` | `SHORT` | 1,654,597.00 USD | `16,100.00` | `101.02` | `102.78` | `153.33` | -28,139.63 USD | `-1.70%` | `20X Cross` |
| `1340` | `0x1bf6...5bfa` | `SHORT` | 1,644,480.00 USD | `16,000.00` | `99.60` | `102.78` | `228.37` | -50,857.69 USD | `-3.09%` | `20X Cross` |
| `1433` | `0x34ea...2f47` | `SHORT` | 1,541,550.00 USD | `15,000.00` | `99.80` | `102.78` | `201.03` | -44,548.69 USD | `-2.89%` | `20X Cross` |
| `1435` | `0x5d6f...6f8a` | `LONG` | 1,541,250.00 USD | `15,000.00` | `101.91` | `102.78` | `28.79` | 12,595.00 USD | `+0.82%` | `20X Cross` |
| `1547` | `0xfb29...21dd` | `LONG` | 1,412,525.45 USD | `13,744.53` | `89.85` | `102.78` | `84.70` | 177,531.49 USD | `+12.57%` | `20X Cross` |
| `1571` | `0x6fa6...825e` | `SHORT` | 1,387,395.00 USD | `13,500.00` | `102.95` | `102.78` | `135.50` | 2,379.27 USD | `+0.17%` | `20X Isolated` |
| `1586` | `0xa9d9...b48e` | `SHORT` | 1,370,133.30 USD | `13,333.33` | `96.39` | `102.78` | `174.23` | -84,886.11 USD | `-6.20%` | `20X Cross` |
| `1639` | `0x936c...bb0f` | `SHORT` | 1,303,936.31 USD | `12,687.91` | `101.39` | `102.78` | `163.64` | -17,463.43 USD | `-1.34%` | `2X Isolated` |
| `1663` | `0x89c2...c94b` | `LONG` | 1,270,719.29 USD | `12,364.69` | `75.25` | `102.78` | `45.76` | 340,236.14 USD | `+26.78%` | `3X Isolated` |
| `1701` | `0xcd81...36e3` | `SHORT` | 1,239,813.58 USD | `12,063.96` | `97.96` | `102.78` | `109.19` | -57,974.66 USD | `-4.68%` | `20X Cross` |
| `1708` | `0x436c...b3d1` | `SHORT` | 1,233,240.00 USD | `12,000.00` | `101.05` | `102.78` | `209.56` | -20,580.17 USD | `-1.67%` | `20X Cross` |
| `1775` | `0x9dea...d617` | `LONG` | 1,171,774.02 USD | `11,400.80` | `90.37` | `102.78` | `4.95` | 141,500.29 USD | `+12.08%` | `20X Cross` |
| `1785` | `0x17c3...a868` | `LONG` | 1,161,978.97 USD | `11,306.60` | `95.13` | `102.78` | `64.99` | 86,332.11 USD | `+7.43%` | `3X Isolated` |
| `1821` | `0x8607...08d5` | `SHORT` | 1,130,274.94 USD | `10,998.10` | `92.18` | `102.78` | `135.02` | -116,485.24 USD | `-10.31%` | `4X Isolated` |
| `1918` | `0x7717...bd7e` | `SHORT` | 1,050,126.27 USD | `10,220.21` | `102.34` | `102.78` | `134.58` | -4,168.28 USD | `-0.40%` | `20X Cross` |
| `1941` | `0xf29c...9971` | `SHORT` | 1,027,700.00 USD | `10,000.00` | `101.10` | `102.78` | `118.37` | -16,703.97 USD | `-1.63%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `84.50` | 2,999.92 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Short: 3.00K USD at 84.5000 USD [API] | `2026-06-11 19:34:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.89` (Vol: 2,900,000.00 USD, Dist: `+1.00%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--3.59%`)
  * 48H Horizon: Short MP=`104.00` (Vol: 7,100,000.00 USD, Dist: `+1.10%`) | Long MP=`99.18` (Vol: 4,000,000.00 USD, Dist: `--3.58%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 7,000,000.00 USD, Dist: `+1.15%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.51%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 11,000,000.00 USD, Dist: `+1.09%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--3.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.68` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.25` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-293.53K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
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
| `22:20:00` | `102.97` | `102.97` | `102.97` | `102.98` | `102.91` | 19,357.42 USD | 13,481.06 USD | 5,876.36 USD | 7,604.70 USD | `+39.29%` | `1B / 0S` |
| `22:25:00` | `102.97` | `102.97` | `102.97` | `103.02` | `102.94` | 20,902.91 USD | 10,451.45 USD | 10,451.45 USD | 0.00 USD | `+0.00%` | `0B / 0S` |
| `22:30:00` | `102.87` | `102.87` | `102.87` | `102.97` | `102.86` | 16,253.46 USD | 1,523.76 USD | 14,729.70 USD | -13,205.94 USD | `-81.25%` | `0B / 1S` |
| `22:30:00` | `102.94` | `102.94` | `102.94` | `103.05` | `102.86` | 50,543.54 USD | 21,383.81 USD | 29,159.73 USD | -7,775.93 USD | `-15.38%` | `0B / 1S` |
| `22:35:00` | `103.03` | `103.03` | `103.03` | `103.05` | `102.86` | 22,358.59 USD | 21,034.73 USD | 1,323.86 USD | 19,710.87 USD | `+88.16%` | `1B / 0S` |
| `22:40:00` | `102.94` | `102.94` | `102.94` | `103.05` | `102.94` | 11,941.04 USD | 597.05 USD | 11,343.99 USD | -10,746.94 USD | `-90.00%` | `0B / 1S` |
| `22:45:00` | `103.06` | `103.06` | `103.06` | `103.08` | `102.92` | 16,901.02 USD | 14,524.31 USD | 2,376.71 USD | 12,147.61 USD | `+71.88%` | `1B / 0S` |
| `22:45:00` | `103.41` | `103.41` | `103.41` | `103.55` | `102.92` | 128,952.27 USD | 107,288.29 USD | 21,663.98 USD | 85,624.31 USD | `+66.40%` | `1B / 0S` |
| `22:50:00` | `103.39` | `103.39` | `103.39` | `103.43` | `103.04` | 57,484.84 USD | 52,498.91 USD | 4,985.93 USD | 47,512.98 USD | `+82.65%` | `1B / 0S` |
| `22:55:00` | `103.41` | `103.41` | `103.41` | `103.55` | `103.26` | 54,497.07 USD | 29,160.71 USD | 25,336.36 USD | 3,824.36 USD | `+7.02%` | `1B / 0S` |
| `5:00 UTC` | `102.81` | `102.87` | `102.81` | `103.02` | `102.78` | 25,235,874.42 USD | 17,074,162.87 USD | 8,161,711.55 USD | 8,912,451.33 USD | `+35.32%` | `6B / 1S` |
| `0:00 UTC` | `102.00` | `102.25` | `102.00` | `102.98` | `101.69` | 44,005,448.45 USD | 22,985,881.99 USD | 21,019,566.46 USD | 1,966,315.53 USD | `+4.47%` | `19B / 33S` |
| `5:00 UTC` | `101.85` | `102.09` | `101.85` | `102.65` | `101.69` | 23,974,978.54 USD | 13,713,172.54 USD | 10,261,806.01 USD | 3,451,366.53 USD | `+14.40%` | `18B / 9S` |
| `0:00 UTC` | `102.47` | `102.50` | `102.47` | `102.60` | `102.41` | 5,469,868.87 USD | 2,184,741.26 USD | 3,285,127.61 USD | -1,100,386.35 USD | `-20.12%` | `0B / 3S` |
| `5:00 UTC` | `102.62` | `102.58` | `102.62` | `102.66` | `102.50` | 2,045,755.51 USD | 1,077,529.04 USD | 968,226.47 USD | 109,302.57 USD | `+5.34%` | `4B / 1S` |
| `0:00 UTC` | `102.81` | `102.76` | `102.81` | `102.90` | `102.62` | 32,144,198.79 USD | 20,601,970.33 USD | 11,542,228.47 USD | 9,059,741.86 USD | `+28.18%` | `6B / 1S` |
| `5:00 UTC` | `102.85` | `102.84` | `102.85` | `102.93` | `102.69` | 14,929,076.99 USD | 7,121,697.65 USD | 7,807,379.34 USD | -685,681.69 USD | `-4.59%` | `0B / 4S` |
| `0:00 UTC` | `102.95` | `102.92` | `102.95` | `102.97` | `102.84` | 9,938,302.88 USD | 3,679,311.10 USD | 6,258,991.78 USD | -2,579,680.67 USD | `-25.96%` | `0B / 4S` |
| `5:00 UTC` | `102.81` | `102.84` | `102.81` | `102.91` | `102.78` | 8,441,504.20 USD | 4,088,824.06 USD | 4,352,680.15 USD | -263,856.09 USD | `-3.13%` | `1B / 3S` |
| `0:00 UTC` | `102.84` | `102.83` | `102.84` | `102.87` | `102.81` | 2,008,352.43 USD | 1,129,966.74 USD | 878,385.69 USD | 251,581.05 USD | `+12.53%` | `0B / 3S` |

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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.34` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.91` (Risk Distance: `0.4318` pts)
  * +2.5R Take Profit: `104.42`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.43 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `103.51` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.94` (Risk Distance: `0.4318` pts)
  * +2.5R Take Profit: `102.43`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.43 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
