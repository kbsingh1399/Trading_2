# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 02:51:55 IST` (`2026-10-29 21:21:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.54` | **Live Ask Quote**: `103.57` | **Mid Price**: `103.56`
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
  * Golden Pocket Zone (0.618 - 0.650): `103.14` - `103.97`
  * Optimal Trade Entry (OTE 0.705): `103.77`
  * Structural Invalidation Anchor (0.786): `104.39`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `102.56` | `102.61` | `102.54` | `102.57` | `393` | 40,309.22 USD | -2,687.28 USD | `-6.67%` | 119,577.03 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `102.55` | `102.62` | `102.37` | `102.42` | `419` | 42,914.82 USD | -23,909.68 USD | `-55.71%` | 95,667.35 USD | `-1.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `102.41` | `102.78` | `102.38` | `102.70` | `542` | 55,662.32 USD | 37,014.03 USD | `+66.50%` | 132,681.38 USD | `+1.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.66` | `102.74` | `102.46` | `102.56` | `1,202` | 123,274.72 USD | -39,624.02 USD | `-32.14%` | 410,320.09 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `102.57` | `102.62` | `102.37` | `102.42` | `1,200` | 122,906.40 USD | -73,493.01 USD | `-59.80%` | 336,827.08 USD | `-0.84` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `102.41` | `102.78` | `102.38` | `102.66` | `1,691` | 173,592.99 USD | 88,338.56 USD | `+50.89%` | 425,165.65 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -802,271.63 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.97` | `102.88` | `101.90` | `102.56` | `5,791` | 593,913.38 USD | 283,583.00 USD | `+47.75%` | -518,688.63 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.57` | `103.03` | `102.37` | `102.79` | `4,695` | 482,613.14 USD | 151,046.86 USD | `+31.30%` | -367,641.77 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `41` | `0x0cc1...c7cb` | `LONG` | 30,707,425.49 USD | `300,817.26` | `98.89` | `102.06` | `31.96` | 957,924.46 USD | `+3.12%` | `3X Cross` |
| `111` | `0x30af...393e` | `LONG` | 18,146,216.94 USD | `177,712.44` | `100.98` | `102.06` | `93.20` | 200,815.05 USD | `+1.11%` | `10X Isolated` |
| `209` | `0x9e2c...5508` | `LONG` | 10,209,000.00 USD | `100,000.00` | `100.89` | `102.06` | `87.02` | 119,761.86 USD | `+1.17%` | `20X Cross` |
| `276` | `0xebe1...4070` | `LONG` | 8,576,396.12 USD | `83,999.96` | `101.87` | `102.06` | `0.000000` | 19,205.80 USD | `+0.22%` | `20X Cross` |
| `297` | `0x7fda...17d1` | `SHORT` | 8,028,344.86 USD | `78,647.58` | `100.15` | `102.06` | `204.69` | -151,723.02 USD | `-1.89%` | `20X Cross` |
| `331` | `0x10e1...f4bd` | `LONG` | 6,903,925.78 USD | `67,625.88` | `84.36` | `102.06` | `58.54` | 1,198,695.40 USD | `+17.36%` | `3X Isolated` |
| `349` | `0x4692...164f` | `SHORT` | 6,613,246.97 USD | `64,791.29` | `102.11` | `102.06` | `1042.60` | 2,450.85 USD | `+0.04%` | `5X Cross` |
| `398` | `0xea00...a918` | `SHORT` | 5,630,394.69 USD | `55,151.29` | `89.22` | `102.06` | `247.30` | -709,670.19 USD | `-12.60%` | `20X Cross` |
| `533` | `0x5989...bc29` | `SHORT` | 4,143,602.68 USD | `40,591.72` | `99.23` | `102.06` | `111.59` | -115,667.99 USD | `-2.79%` | `10X Cross` |
| `543` | `0xd507...c948` | `LONG` | 4,063,651.37 USD | `39,808.50` | `93.57` | `102.06` | `81.35` | 338,575.96 USD | `+8.33%` | `7X Isolated` |
| `686` | `0x354b...6425` | `SHORT` | 3,271,721.16 USD | `32,053.70` | `101.83` | `102.06` | `447.08` | -7,773.41 USD | `-0.24%` | `8X Cross` |
| `710` | `0xb5e7...eff1` | `SHORT` | 3,178,917.93 USD | `31,132.29` | `91.71` | `102.06` | `144.82` | -323,709.28 USD | `-10.18%` | `20X Cross` |
| `748` | `0xd84a...c8a5` | `SHORT` | 3,063,300.00 USD | `30,000.00` | `101.76` | `102.06` | `126.02` | -10,450.00 USD | `-0.34%` | `20X Cross` |
| `806` | `0x61d7...7dee` | `LONG` | 2,844,031.90 USD | `27,858.08` | `88.25` | `102.06` | `83.51` | 385,555.90 USD | `+13.56%` | `20X Cross` |
| `884` | `0xf0ae...2f74` | `SHORT` | 2,552,000.00 USD | `25,000.00` | `100.78` | `102.06` | `174.34` | -32,481.39 USD | `-1.27%` | `20X Cross` |
| `899` | `0xb8f3...04ea` | `SHORT` | 2,507,362.66 USD | `24,560.32` | `102.91` | `102.06` | `114.78` | 20,144.33 USD | `+0.80%` | `7X Isolated` |
| `908` | `0x645b...87b8` | `SHORT` | 2,481,320.37 USD | `24,302.84` | `101.22` | `102.06` | `134.77` | -21,358.81 USD | `-0.86%` | `3X Isolated` |
| `986` | `0x58f0...0d20` | `SHORT` | 2,298,203.73 USD | `22,511.55` | `96.77` | `102.06` | `115.14` | -119,785.94 USD | `-5.21%` | `20X Cross` |
| `1024` | `0xce97...7e78` | `SHORT` | 2,186,925.17 USD | `21,423.64` | `102.73` | `102.06` | `120.34` | 13,905.73 USD | `+0.64%` | `5X Isolated` |
| `1061` | `0xfc66...ca06` | `SHORT` | 2,100,500.97 USD | `20,566.93` | `101.34` | `102.06` | `2074.58` | -16,317.50 USD | `-0.78%` | `3X Cross` |
| `1107` | `0x9aa5...58af` | `SHORT` | 2,008,802.52 USD | `19,671.00` | `101.76` | `102.06` | `555.38` | -7,051.59 USD | `-0.35%` | `20X Cross` |
| `1218` | `0xe5dd...ecba` | `SHORT` | 1,856,037.51 USD | `18,183.97` | `102.71` | `102.06` | `138.74` | 11,629.20 USD | `+0.63%` | `20X Cross` |
| `1288` | `0x4169...6f06` | `LONG` | 1,753,758.65 USD | `17,175.19` | `76.61` | `102.06` | `82.99` | 437,990.65 USD | `+24.97%` | `12X Isolated` |
| `1304` | `0x6788...98d4` | `SHORT` | 1,735,700.00 USD | `17,000.00` | `99.31` | `102.06` | `198.02` | -47,375.41 USD | `-2.73%` | `20X Cross` |
| `1365` | `0xa99c...40d5` | `SHORT` | 1,643,810.00 USD | `16,100.00` | `101.02` | `102.06` | `155.27` | -17,352.63 USD | `-1.06%` | `20X Cross` |
| `1374` | `0x1bf6...5bfa` | `SHORT` | 1,633,600.00 USD | `16,000.00` | `99.60` | `102.06` | `223.07` | -39,977.69 USD | `-2.45%` | `20X Cross` |
| `1445` | `0x49e9...e1d0` | `SHORT` | 1,554,139.42 USD | `15,224.72` | `102.90` | `102.06` | `125.49` | 12,517.80 USD | `+0.81%` | `4X Isolated` |
| `1463` | `0x34ea...2f47` | `SHORT` | 1,531,500.00 USD | `15,000.00` | `99.80` | `102.06` | `199.15` | -34,498.69 USD | `-2.25%` | `20X Cross` |
| `1565` | `0xfb29...21dd` | `LONG` | 1,403,454.06 USD | `13,744.53` | `89.85` | `102.06` | `84.63` | 168,460.10 USD | `+12.00%` | `20X Cross` |
| `1593` | `0x6fa6...825e` | `SHORT` | 1,378,215.00 USD | `13,500.00` | `102.95` | `102.06` | `135.51` | 11,559.27 USD | `+0.84%` | `20X Isolated` |
| `1594` | `0x5d6f...6f8a` | `LONG` | 1,378,080.00 USD | `13,500.00` | `101.84` | `102.06` | `20.49` | 3,275.00 USD | `+0.24%` | `20X Cross` |
| `1604` | `0xa9d9...b48e` | `SHORT` | 1,361,466.63 USD | `13,333.33` | `96.39` | `102.06` | `174.49` | -76,219.45 USD | `-5.60%` | `20X Cross` |
| `1633` | `0xb078...de15` | `SHORT` | 1,327,040.00 USD | `13,000.00` | `102.96` | `102.06` | `559.86` | 11,469.53 USD | `+0.86%` | `5X Cross` |
| `1662` | `0x936c...bb0f` | `SHORT` | 1,295,435.41 USD | `12,687.91` | `101.39` | `102.06` | `163.65` | -8,962.54 USD | `-0.69%` | `2X Isolated` |
| `1672` | `0x5a20...2d1b` | `SHORT` | 1,284,581.11 USD | `12,582.83` | `102.83` | `102.06` | `375.02` | 9,360.89 USD | `+0.73%` | `20X Cross` |
| `1697` | `0x89c2...c94b` | `LONG` | 1,262,434.95 USD | `12,364.69` | `75.25` | `102.06` | `45.77` | 331,951.80 USD | `+26.29%` | `3X Isolated` |
| `1725` | `0xcd81...36e3` | `SHORT` | 1,231,730.72 USD | `12,063.96` | `97.96` | `102.06` | `110.28` | -49,891.80 USD | `-4.05%` | `20X Cross` |
| `1731` | `0x436c...b3d1` | `SHORT` | 1,224,960.00 USD | `12,000.00` | `101.05` | `102.06` | `208.35` | -12,300.17 USD | `-1.00%` | `20X Cross` |
| `1793` | `0x9dea...d617` | `LONG` | 1,163,907.47 USD | `11,400.80` | `90.37` | `102.06` | `5.71` | 133,633.74 USD | `+11.48%` | `20X Cross` |
| `1799` | `0x91fd...9841` | `LONG` | 1,157,414.60 USD | `11,334.98` | `101.16` | `102.06` | `95.59` | 10,752.41 USD | `+0.93%` | `13X Isolated` |
| `1803` | `0x17c3...a868` | `LONG` | 1,154,064.36 USD | `11,306.60` | `95.13` | `102.06` | `65.00` | 78,417.49 USD | `+6.79%` | `3X Isolated` |
| `1841` | `0x8607...08d5` | `SHORT` | 1,122,686.25 USD | `10,998.10` | `92.18` | `102.06` | `135.03` | -108,896.55 USD | `-9.70%` | `4X Isolated` |
| `1879` | `0x7717...bd7e` | `SHORT` | 1,085,507.29 USD | `10,631.81` | `102.34` | `102.06` | `139.86` | 2,539.07 USD | `+0.23%` | `20X Cross` |
| `1949` | `0xf124...d738` | `LONG` | 1,034,475.60 USD | `10,130.00` | `102.56` | `102.06` | `93.72` | -4,416.68 USD | `-0.43%` | `20X Cross` |
| `1978` | `0xf29c...9971` | `SHORT` | 1,020,800.00 USD | `10,000.00` | `101.10` | `102.06` | `118.37` | -9,803.97 USD | `-0.96%` | `5X Isolated` |

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
| `Envelope` | `Long Liquidation` | `102.58` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.37` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-58.37K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
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
| `20:35:00` | `102.78` | `102.78` | `102.78` | `102.80` | `102.62` | 59,716.92 USD | 40,972.44 USD | 18,744.48 USD | 22,227.97 USD | `+37.22%` | `1B / 0S` |
| `20:40:00` | `102.67` | `102.67` | `102.67` | `102.83` | `102.63` | 38,603.17 USD | 6,755.55 USD | 31,847.61 USD | -25,092.06 USD | `-65.00%` | `0B / 1S` |
| `20:45:00` | `102.68` | `102.68` | `102.68` | `102.70` | `102.56` | 38,093.54 USD | 26,599.80 USD | 11,493.74 USD | 15,106.06 USD | `+39.66%` | `1B / 0S` |
| `20:45:00` | `102.56` | `102.56` | `102.56` | `102.74` | `102.46` | 123,274.72 USD | 41,825.35 USD | 81,449.37 USD | -39,624.02 USD | `-32.14%` | `0B / 1S` |
| `20:50:00` | `102.51` | `102.51` | `102.51` | `102.74` | `102.47` | 48,691.30 USD | 7,664.37 USD | 41,026.93 USD | -33,362.56 USD | `-68.52%` | `0B / 1S` |
| `20:55:00` | `102.56` | `102.56` | `102.56` | `102.65` | `102.46` | 36,510.65 USD | 20,897.54 USD | 15,613.11 USD | 5,284.44 USD | `+14.47%` | `1B / 0S` |
| `21:00:00` | `102.42` | `102.42` | `102.42` | `102.62` | `102.37` | 122,906.40 USD | 24,706.69 USD | 98,199.71 USD | -73,493.01 USD | `-59.80%` | `0B / 1S` |
| `21:00:00` | `102.79` | `102.79` | `102.79` | `103.03` | `102.37` | 482,613.14 USD | 316,830.00 USD | 165,783.14 USD | 151,046.86 USD | `+31.30%` | `1B / 0S` |
| `21:00:00` | `102.57` | `102.57` | `102.57` | `102.59` | `102.45` | 39,796.38 USD | 27,004.69 USD | 12,791.69 USD | 14,212.99 USD | `+35.71%` | `1B / 0S` |
| `21:05:00` | `102.57` | `102.57` | `102.57` | `102.61` | `102.54` | 40,309.22 USD | 18,810.97 USD | 21,498.25 USD | -2,687.28 USD | `-6.67%` | `0B / 1S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.37` | `102.32` | `102.37` | `102.44` | `102.16` | 7,394,503.21 USD | 3,870,700.86 USD | 3,523,802.35 USD | 346,898.52 USD | `+4.69%` | `5B / 3S` |
| `5:00 UTC` | `102.37` | `102.38` | `102.37` | `102.44` | `102.30` | 4,333,204.12 USD | 1,824,676.12 USD | 2,508,528.00 USD | -683,851.88 USD | `-15.78%` | `1B / 3S` |
| `0:00 UTC` | `102.43` | `102.38` | `102.43` | `102.48` | `102.30` | 3,151,223.23 USD | 1,856,912.02 USD | 1,294,311.21 USD | 562,600.81 USD | `+17.85%` | `8B / 4S` |
| `5:00 UTC` | `102.81` | `102.73` | `102.81` | `102.97` | `102.35` | 32,224,554.20 USD | 17,495,336.21 USD | 14,729,217.99 USD | 2,766,118.21 USD | `+8.58%` | `13B / 7S` |
| `0:00 UTC` | `103.00` | `102.95` | `103.00` | `103.06` | `102.81` | 19,638,941.63 USD | 9,830,854.95 USD | 9,808,086.67 USD | 22,768.28 USD | `+0.12%` | `2B / 4S` |
| `5:00 UTC` | `103.02` | `102.95` | `103.02` | `103.06` | `102.82` | 8,073,511.20 USD | 2,057,722.32 USD | 6,015,788.89 USD | -3,958,066.57 USD | `-49.03%` | `1B / 13S` |
| `0:00 UTC` | `102.87` | `102.93` | `102.87` | `103.02` | `102.84` | 8,092,099.96 USD | 4,143,913.94 USD | 3,948,186.02 USD | 195,727.93 USD | `+2.42%` | `2B / 2S` |
| `5:00 UTC` | `102.81` | `102.87` | `102.81` | `103.02` | `102.78` | 25,235,874.42 USD | 17,074,162.87 USD | 8,161,711.55 USD | 8,912,451.33 USD | `+35.32%` | `6B / 1S` |
| `0:00 UTC` | `102.16` | `102.35` | `102.16` | `102.98` | `101.94` | 33,294,171.67 USD | 16,268,534.78 USD | 17,025,636.89 USD | -757,102.11 USD | `-2.27%` | `11B / 27S` |

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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
