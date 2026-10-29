# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 02:30:40 IST` (`2026-10-29 21:00:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.52` | **Live Ask Quote**: `103.55` | **Mid Price**: `103.54`
- **Spread Points**: `30.00` | **Spread BPS**: `2.90 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.99` | VWAP Z-Score: `+2.32` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.3567` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `69.16` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.91` | Lower -3.00σ Band: `100.08`
  * Upper +2.51σ Band: `103.60` | Lower -2.51σ Band: `100.39`
  * Upper +2.01σ Band: `103.28` | Lower -2.01σ Band: `100.71`
  * Upper +2.00σ Band: `103.27` | Lower -2.00σ Band: `100.72`
  * Upper +1.28σ Band: `102.81` | Lower -1.28σ Band: `101.18`
  * Upper +1.00σ Band: `102.63` | Lower -1.00σ Band: `101.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.17` | EMA-20=`102.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.35` (Slope: `+0.0000`) | EMA-100=`102.28`
  * Institutional Anchors: EMA-144=`102.27` | EMA-200=`102.18` (Slope: `+0.1057`) | EMA-233=`102.14`
- **Range Boundaries**: 24H High=`103.64` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.76` (Distance: `+0.78%`)
  * Point of Control (POC) = `102.02` (Distance: `+1.51%`)
  * Value Area Low (VAL) = `101.40` (Distance: `+2.13%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.08` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.12` - `103.95`
  * Optimal Trade Entry (OTE 0.705): `103.75`
  * Structural Invalidation Anchor (0.786): `104.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `102.66` | `102.70` | `102.56` | `102.68` | `371` | 38,093.54 USD | 15,106.06 USD | `+39.66%` | 207,406.59 USD | `+0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `102.69` | `102.74` | `102.47` | `102.51` | `475` | 48,691.30 USD | -33,362.56 USD | `-68.52%` | 174,044.03 USD | `-1.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `102.51` | `102.65` | `102.46` | `102.56` | `356` | 36,510.65 USD | 5,284.44 USD | `+14.47%` | 179,328.47 USD | `-0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `102.51` | `102.51` | `101.97` | `102.46` | `1,278` | 130,941.32 USD | 46,071.95 USD | `+35.19%` | 367,428.18 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `102.45` | `102.88` | `102.42` | `102.67` | `1,796` | 184,391.73 USD | 52,049.31 USD | `+28.23%` | 419,477.48 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.66` | `102.74` | `102.46` | `102.56` | `1,202` | 123,274.72 USD | -39,624.02 USD | `-32.14%` | 379,853.47 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `100.94` | `101.53` | `100.68` | `101.35` | `7,439` | 753,964.97 USD | 405,912.66 USD | `+53.84%` | -1,045,389.30 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -516,896.02 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.97` | `102.88` | `101.90` | `102.56` | `5,791` | 593,913.38 USD | 283,583.00 USD | `+47.75%` | -233,313.02 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.53` | `16,864` | 1,745,980.51 USD | 1,550,033.79 USD | `+88.78%` | 1,717,906.51 USD | `+1.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,027,007.90 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -1,556,424.27 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.53` | `16,864` | 1,745,980.51 USD | 1,550,033.79 USD | `+88.78%` | 1,717,906.51 USD | `+1.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,960,111.99 USD | `300,817.26` | `98.89` | `102.94` | `31.90` | 1,210,610.96 USD | `+3.91%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,284,832.64 USD | `177,712.44` | `100.98` | `102.94` | `93.19` | 339,430.75 USD | `+1.86%` | `10X Isolated` |
| `214` | `0x9e2c...5508` | `LONG` | 10,281,000.00 USD | `100,000.00` | `100.89` | `102.94` | `84.81` | 191,761.86 USD | `+1.87%` | `20X Cross` |
| `278` | `0xebe1...4070` | `LONG` | 8,645,276.09 USD | `83,999.96` | `101.87` | `102.94` | `0.000000` | 88,085.77 USD | `+1.02%` | `20X Cross` |
| `295` | `0x7fda...17d1` | `SHORT` | 8,094,408.83 USD | `78,647.58` | `100.15` | `102.94` | `205.67` | -217,786.98 USD | `-2.69%` | `20X Cross` |
| `335` | `0x10e1...f4bd` | `LONG` | 6,959,379.00 USD | `67,625.88` | `84.36` | `102.94` | `58.54` | 1,254,148.62 USD | `+18.02%` | `3X Isolated` |
| `359` | `0x4692...164f` | `SHORT` | 6,557,578.18 USD | `63,709.11` | `102.03` | `102.94` | `1053.76` | -57,146.63 USD | `-0.87%` | `5X Cross` |
| `404` | `0xea00...a918` | `SHORT` | 5,676,721.76 USD | `55,151.29` | `89.22` | `102.94` | `242.26` | -755,997.27 USD | `-13.32%` | `20X Cross` |
| `527` | `0x5989...bc29` | `SHORT` | 4,177,699.72 USD | `40,591.72` | `99.23` | `102.94` | `111.59` | -149,765.04 USD | `-3.58%` | `10X Cross` |
| `539` | `0xd507...c948` | `LONG` | 4,095,896.26 USD | `39,808.50` | `93.57` | `102.94` | `81.35` | 370,820.84 USD | `+9.05%` | `7X Isolated` |
| `680` | `0x354b...6425` | `SHORT` | 3,299,287.34 USD | `32,053.70` | `101.83` | `102.94` | `446.49` | -35,339.59 USD | `-1.07%` | `8X Cross` |
| `703` | `0xb5e7...eff1` | `SHORT` | 3,199,153.91 USD | `31,132.29` | `91.71` | `102.94` | `144.97` | -343,945.27 USD | `-10.75%` | `20X Cross` |
| `736` | `0xd84a...c8a5` | `SHORT` | 3,082,800.00 USD | `30,000.00` | `101.76` | `102.94` | `126.02` | -29,950.00 USD | `-0.97%` | `20X Cross` |
| `792` | `0x61d7...7dee` | `LONG` | 2,864,089.72 USD | `27,858.08` | `88.25` | `102.94` | `83.51` | 405,613.72 USD | `+14.16%` | `20X Cross` |
| `871` | `0xf0ae...2f74` | `SHORT` | 2,572,250.00 USD | `25,000.00` | `100.78` | `102.94` | `173.33` | -52,731.39 USD | `-2.05%` | `20X Cross` |
| `883` | `0xb8f3...04ea` | `SHORT` | 2,527,993.33 USD | `24,560.32` | `102.91` | `102.94` | `114.78` | -486.33 USD | `-0.02%` | `7X Isolated` |
| `893` | `0x645b...87b8` | `SHORT` | 2,501,248.70 USD | `24,302.84` | `101.22` | `102.94` | `134.77` | -41,287.14 USD | `-1.65%` | `3X Isolated` |
| `961` | `0x58f0...0d20` | `SHORT` | 2,317,113.43 USD | `22,511.55` | `96.77` | `102.94` | `112.74` | -138,695.64 USD | `-5.99%` | `20X Cross` |
| `1041` | `0xfc66...ca06` | `SHORT` | 2,116,954.52 USD | `20,566.93` | `101.34` | `102.94` | `2074.47` | -32,771.05 USD | `-1.55%` | `3X Cross` |
| `1095` | `0x9aa5...58af` | `SHORT` | 2,024,342.61 USD | `19,671.00` | `101.76` | `102.94` | `561.80` | -22,591.68 USD | `-1.12%` | `20X Cross` |
| `1198` | `0xe5dd...ecba` | `SHORT` | 1,871,675.72 USD | `18,183.97` | `102.71` | `102.94` | `138.86` | -4,009.01 USD | `-0.21%` | `20X Cross` |
| `1277` | `0x4169...6f06` | `LONG` | 1,767,155.30 USD | `17,175.19` | `76.61` | `102.94` | `82.99` | 451,387.30 USD | `+25.54%` | `12X Isolated` |
| `1288` | `0x6788...98d4` | `SHORT` | 1,749,640.00 USD | `17,000.00` | `99.31` | `102.94` | `198.31` | -61,315.41 USD | `-3.50%` | `20X Cross` |
| `1330` | `0xce97...7e78` | `SHORT` | 1,663,169.80 USD | `16,158.26` | `102.85` | `102.94` | `120.41` | -1,291.27 USD | `-0.08%` | `5X Isolated` |
| `1335` | `0xa99c...40d5` | `SHORT` | 1,657,012.00 USD | `16,100.00` | `101.02` | `102.94` | `155.27` | -30,554.63 USD | `-1.84%` | `20X Cross` |
| `1345` | `0x1bf6...5bfa` | `SHORT` | 1,646,080.00 USD | `16,000.00` | `99.60` | `102.94` | `221.20` | -52,457.69 USD | `-3.19%` | `20X Cross` |
| `1423` | `0x49e9...e1d0` | `SHORT` | 1,567,080.43 USD | `15,224.72` | `102.90` | `102.94` | `125.49` | -423.21 USD | `-0.03%` | `4X Isolated` |
| `1448` | `0x34ea...2f47` | `SHORT` | 1,543,950.00 USD | `15,000.00` | `99.80` | `102.94` | `199.04` | -46,948.69 USD | `-3.04%` | `20X Cross` |
| `1548` | `0xb078...de15` | `SHORT` | 1,421,610.80 USD | `13,811.43` | `102.96` | `102.94` | `540.16` | 445.72 USD | `+0.03%` | `5X Cross` |
| `1556` | `0xfb29...21dd` | `LONG` | 1,414,862.02 USD | `13,744.53` | `89.85` | `102.94` | `84.59` | 179,868.06 USD | `+12.71%` | `20X Cross` |
| `1577` | `0x5d6f...6f8a` | `LONG` | 1,389,015.00 USD | `13,500.00` | `101.84` | `102.94` | `20.26` | 14,210.00 USD | `+1.02%` | `20X Cross` |
| `1578` | `0x6fa6...825e` | `SHORT` | 1,388,610.00 USD | `13,500.00` | `102.95` | `102.94` | `135.50` | 1,164.27 USD | `+0.08%` | `20X Isolated` |
| `1594` | `0xa9d9...b48e` | `SHORT` | 1,370,133.30 USD | `13,333.33` | `96.39` | `102.94` | `174.24` | -84,886.11 USD | `-6.20%` | `20X Cross` |
| `1644` | `0x936c...bb0f` | `SHORT` | 1,305,839.49 USD | `12,687.91` | `101.39` | `102.94` | `163.65` | -19,366.62 USD | `-1.48%` | `2X Isolated` |
| `1675` | `0x89c2...c94b` | `LONG` | 1,272,697.64 USD | `12,364.69` | `75.25` | `102.94` | `45.77` | 342,214.49 USD | `+26.89%` | `3X Isolated` |
| `1711` | `0xcd81...36e3` | `SHORT` | 1,241,743.81 USD | `12,063.96` | `97.96` | `102.94` | `110.41` | -59,904.89 USD | `-4.82%` | `20X Cross` |
| `1716` | `0x436c...b3d1` | `SHORT` | 1,235,160.00 USD | `12,000.00` | `101.05` | `102.94` | `208.34` | -22,500.17 USD | `-1.82%` | `20X Cross` |
| `1774` | `0x9dea...d617` | `LONG` | 1,173,484.14 USD | `11,400.80` | `90.37` | `102.94` | `3.91` | 143,210.41 USD | `+12.20%` | `20X Cross` |
| `1782` | `0x91fd...9841` | `LONG` | 1,166,369.24 USD | `11,334.98` | `101.16` | `102.94` | `95.59` | 19,707.04 USD | `+1.69%` | `13X Isolated` |
| `1785` | `0x17c3...a868` | `LONG` | 1,163,674.96 USD | `11,306.60` | `95.13` | `102.94` | `64.99` | 88,028.10 USD | `+7.56%` | `3X Isolated` |
| `1797` | `0x5a20...2d1b` | `SHORT` | 1,154,514.96 USD | `11,216.51` | `103.06` | `102.94` | `406.70` | 1,492.91 USD | `+0.13%` | `20X Cross` |
| `1821` | `0x8607...08d5` | `SHORT` | 1,131,814.68 USD | `10,998.10` | `92.18` | `102.94` | `135.03` | -118,024.97 USD | `-10.43%` | `4X Isolated` |
| `1945` | `0xf29c...9971` | `SHORT` | 1,029,200.00 USD | `10,000.00` | `101.10` | `102.94` | `118.37` | -18,203.97 USD | `-1.77%` | `5X Isolated` |
| `1979` | `0x2577...4897` | `SHORT` | 1,006,417.32 USD | `9,777.69` | `102.91` | `102.94` | `105.52` | -158.06 USD | `-0.02%` | `20X Isolated` |

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
| `Envelope` | `Long Liquidation` | `102.63` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.50` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-43.56K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
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
| `20:05:00` | `102.43` | `102.43` | `102.43` | `102.48` | `102.21` | 56,540.26 USD | 47,640.40 USD | 8,899.86 USD | 38,740.55 USD | `+68.52%` | `1B / 0S` |
| `20:10:00` | `102.50` | `102.50` | `102.50` | `102.55` | `102.33` | 51,658.99 USD | 37,242.53 USD | 14,416.46 USD | 22,826.07 USD | `+44.19%` | `1B / 0S` |
| `20:15:00` | `102.46` | `102.46` | `102.46` | `102.51` | `101.97` | 130,941.32 USD | 88,506.64 USD | 42,434.69 USD | 46,071.95 USD | `+35.19%` | `1B / 0S` |
| `20:15:00` | `102.16` | `102.16` | `102.16` | `102.51` | `102.16` | 44,847.36 USD | 2,242.37 USD | 42,604.99 USD | -40,362.63 USD | `-90.00%` | `0B / 1S` |
| `20:20:00` | `102.08` | `102.08` | `102.08` | `102.14` | `101.97` | 50,936.92 USD | 24,310.80 USD | 26,626.12 USD | -2,315.31 USD | `-4.55%` | `0B / 1S` |
| `20:25:00` | `102.46` | `102.46` | `102.46` | `102.46` | `102.07` | 34,835.72 USD | 33,093.93 USD | 1,741.79 USD | 31,352.15 USD | `+90.00%` | `1B / 0S` |
| `20:30:00` | `102.78` | `102.78` | `102.78` | `102.88` | `102.42` | 86,232.42 USD | 71,137.03 USD | 15,095.39 USD | 56,041.64 USD | `+64.99%` | `1B / 0S` |
| `20:30:00` | `102.67` | `102.67` | `102.67` | `102.88` | `102.42` | 184,391.73 USD | 118,220.52 USD | 66,171.21 USD | 52,049.31 USD | `+28.23%` | `1B / 0S` |
| `20:35:00` | `102.78` | `102.78` | `102.78` | `102.80` | `102.62` | 59,716.92 USD | 40,972.44 USD | 18,744.48 USD | 22,227.97 USD | `+37.22%` | `1B / 0S` |
| `20:40:00` | `102.67` | `102.67` | `102.67` | `102.83` | `102.63` | 38,603.17 USD | 6,755.55 USD | 31,847.61 USD | -25,092.06 USD | `-65.00%` | `0B / 1S` |
| `0:00 UTC` | `102.25` | `102.23` | `102.25` | `102.41` | `102.00` | 12,832,227.15 USD | 6,368,450.04 USD | 6,463,777.11 USD | -95,327.07 USD | `-0.74%` | `9B / 6S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.37` | `102.32` | `102.37` | `102.44` | `102.16` | 7,394,503.21 USD | 3,870,700.86 USD | 3,523,802.35 USD | 346,898.52 USD | `+4.69%` | `5B / 3S` |
| `5:00 UTC` | `102.37` | `102.38` | `102.37` | `102.44` | `102.30` | 4,333,204.12 USD | 1,824,676.12 USD | 2,508,528.00 USD | -683,851.88 USD | `-15.78%` | `1B / 3S` |
| `0:00 UTC` | `102.43` | `102.38` | `102.43` | `102.48` | `102.30` | 3,151,223.23 USD | 1,856,912.02 USD | 1,294,311.21 USD | 562,600.81 USD | `+17.85%` | `8B / 4S` |
| `5:00 UTC` | `102.81` | `102.73` | `102.81` | `102.97` | `102.35` | 32,224,554.20 USD | 17,495,336.21 USD | 14,729,217.99 USD | 2,766,118.21 USD | `+8.58%` | `13B / 7S` |
| `0:00 UTC` | `103.00` | `102.95` | `103.00` | `103.06` | `102.81` | 19,638,941.63 USD | 9,830,854.95 USD | 9,808,086.67 USD | 22,768.28 USD | `+0.12%` | `2B / 4S` |
| `5:00 UTC` | `103.02` | `102.95` | `103.02` | `103.06` | `102.82` | 8,073,511.20 USD | 2,057,722.32 USD | 6,015,788.89 USD | -3,958,066.57 USD | `-49.03%` | `1B / 13S` |
| `0:00 UTC` | `102.87` | `102.93` | `102.87` | `103.02` | `102.84` | 8,092,099.96 USD | 4,143,913.94 USD | 3,948,186.02 USD | 195,727.93 USD | `+2.42%` | `2B / 2S` |
| `5:00 UTC` | `102.81` | `102.83` | `102.81` | `102.95` | `102.78` | 17,553,152.84 USD | 11,893,882.24 USD | 5,659,270.59 USD | 6,234,611.65 USD | `+35.52%` | `3B / 1S` |

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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.40` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.93` (Risk Distance: `0.4731` pts)
  * +2.5R Take Profit: `102.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.76` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.23` (Risk Distance: `0.4731` pts)
  * +2.5R Take Profit: `101.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
