# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-29 23:37:49 IST` (`2026-10-29 18:07:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.55` | **Live Ask Quote**: `102.58` | **Mid Price**: `102.57`
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
  * Session VWAP: `101.87` | VWAP Z-Score: `+1.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4409` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.53` | Lower -3.00σ Band: `100.22`
  * Upper +2.51σ Band: `103.26` | Lower -2.51σ Band: `100.49`
  * Upper +2.01σ Band: `102.98` | Lower -2.01σ Band: `100.76`
  * Upper +2.00σ Band: `102.98` | Lower -2.00σ Band: `100.77`
  * Upper +1.28σ Band: `102.58` | Lower -1.28σ Band: `101.17`
  * Upper +1.00σ Band: `102.43` | Lower -1.00σ Band: `101.32`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.15` | EMA-20=`101.89` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`101.94` (Slope: `+0.0000`) | EMA-100=`102.08`
  * Institutional Anchors: EMA-144=`102.14` | EMA-200=`102.11` (Slope: `-0.0364`) | EMA-233=`102.05`
- **Range Boundaries**: 24H High=`103.82` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.71` (Distance: `-0.14%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.53%`)
  * Value Area Low (VAL) = `101.50` (Distance: `+1.05%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `102.16` - `102.98`
  * Optimal Trade Entry (OTE 0.705): `102.77`
  * Structural Invalidation Anchor (0.786): `103.39`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.87` | `101.03` | `100.81` | `100.95` | `526` | 53,098.65 USD | 15,032.49 USD | `+28.31%` | -204,003.91 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `100.94` | `101.15` | `100.92` | `101.03` | `722` | 72,944.38 USD | 14,209.94 USD | `+19.48%` | -189,793.96 USD | `+0.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.03` | `101.03` | `100.68` | `100.74` | `639` | 64,374.78 USD | -47,021.58 USD | `-73.04%` | -236,815.54 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `101.48` | `101.63` | `100.97` | `101.02` | `2,460` | 248,496.90 USD | -195,006.25 USD | `-78.47%` | 29,074.25 USD | `-1.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `101.02` | `101.25` | `100.81` | `100.95` | `1,931` | 194,930.59 USD | -54,147.39 USD | `-27.78%` | -25,073.13 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `100.94` | `101.15` | `100.68` | `100.96` | `1,945` | 196,371.09 USD | 25,019.44 USD | `+12.74%` | -53.69 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 30,647,262.04 USD | `300,817.26` | `98.89` | `101.90` | `32.42` | 897,761.01 USD | `+2.93%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,105,343.08 USD | `177,712.44` | `100.98` | `101.90` | `93.19` | 159,941.19 USD | `+0.88%` | `10X Isolated` |
| `160` | `0x58f0...0d20` | `SHORT` | 12,863,421.17 USD | `126,260.51` | `96.77` | `101.90` | `104.88` | -645,328.74 USD | `-5.02%` | `20X Cross` |
| `213` | `0xebe1...4070` | `LONG` | 10,391,755.82 USD | `101,999.96` | `101.87` | `101.90` | `0.000000` | 881.33 USD | `+0.01%` | `20X Cross` |
| `222` | `0x9e2c...5508` | `LONG` | 10,188,000.00 USD | `100,000.00` | `100.89` | `101.90` | `79.04` | 98,761.86 USD | `+0.97%` | `20X Cross` |
| `307` | `0x7fda...17d1` | `SHORT` | 8,027,525.47 USD | `78,763.01` | `100.15` | `101.90` | `209.28` | -139,343.61 USD | `-1.74%` | `20X Cross` |
| `345` | `0x10e1...f4bd` | `LONG` | 6,889,724.35 USD | `67,625.88` | `84.36` | `101.90` | `58.54` | 1,184,493.97 USD | `+17.19%` | `3X Isolated` |
| `383` | `0x4692...164f` | `SHORT` | 6,245,586.15 USD | `61,279.30` | `101.28` | `101.90` | `1054.43` | -39,072.86 USD | `-0.63%` | `5X Cross` |
| `409` | `0x0c4a...1b19` | `SHORT` | 5,685,203.83 USD | `55,802.94` | `102.08` | `101.90` | `106.83` | 11,443.55 USD | `+0.20%` | `20X Isolated` |
| `422` | `0xea00...a918` | `SHORT` | 5,618,261.40 USD | `55,151.29` | `89.22` | `101.90` | `278.63` | -697,536.91 USD | `-12.42%` | `20X Cross` |
| `555` | `0x5989...bc29` | `SHORT` | 4,135,484.33 USD | `40,591.72` | `99.23` | `101.90` | `111.59` | -107,549.65 USD | `-2.60%` | `10X Cross` |
| `565` | `0xd507...c948` | `LONG` | 4,055,689.67 USD | `39,808.50` | `93.57` | `101.90` | `81.35` | 330,614.26 USD | `+8.15%` | `7X Isolated` |
| `674` | `0x354b...6425` | `SHORT` | 3,425,585.93 USD | `33,610.54` | `101.08` | `101.90` | `425.18` | -28,101.61 USD | `-0.82%` | `8X Cross` |
| `738` | `0xb5e7...eff1` | `SHORT` | 3,171,757.50 USD | `31,132.29` | `91.71` | `101.90` | `145.18` | -316,548.86 USD | `-9.98%` | `20X Cross` |
| `772` | `0xd84a...c8a5` | `SHORT` | 3,056,400.00 USD | `30,000.00` | `101.76` | `101.90` | `126.49` | -3,550.00 USD | `-0.12%` | `20X Cross` |
| `819` | `0x61d7...7dee` | `LONG` | 2,838,181.70 USD | `27,858.08` | `88.25` | `101.90` | `83.50` | 379,705.70 USD | `+13.38%` | `20X Cross` |
| `899` | `0xf0ae...2f74` | `SHORT` | 2,547,000.00 USD | `25,000.00` | `100.78` | `101.90` | `173.33` | -27,481.39 USD | `-1.08%` | `20X Cross` |
| `915` | `0xb8f3...04ea` | `SHORT` | 2,502,204.99 USD | `24,560.32` | `102.91` | `101.90` | `114.78` | 25,302.00 USD | `+1.01%` | `7X Isolated` |
| `924` | `0x645b...87b8` | `SHORT` | 2,476,945.86 USD | `24,302.84` | `101.22` | `101.90` | `134.77` | -16,984.30 USD | `-0.69%` | `3X Isolated` |
| `959` | `0xfc66...ca06` | `SHORT` | 2,377,742.44 USD | `23,329.50` | `101.07` | `101.90` | `1885.76` | -19,788.99 USD | `-0.83%` | `3X Cross` |
| `1128` | `0x9aa5...58af` | `SHORT` | 2,004,081.48 USD | `19,671.00` | `101.76` | `101.90` | `478.50` | -2,330.55 USD | `-0.12%` | `20X Cross` |
| `1302` | `0x4169...6f06` | `LONG` | 1,749,808.36 USD | `17,175.19` | `76.61` | `101.90` | `82.99` | 434,040.36 USD | `+24.81%` | `12X Isolated` |
| `1312` | `0x6788...98d4` | `SHORT` | 1,731,960.00 USD | `17,000.00` | `99.31` | `101.90` | `191.75` | -43,635.41 USD | `-2.52%` | `20X Cross` |
| `1375` | `0xa99c...40d5` | `SHORT` | 1,640,268.00 USD | `16,100.00` | `101.02` | `101.90` | `156.97` | -13,810.63 USD | `-0.84%` | `20X Cross` |
| `1390` | `0x1bf6...5bfa` | `SHORT` | 1,630,080.00 USD | `16,000.00` | `99.60` | `101.90` | `223.67` | -36,457.69 USD | `-2.24%` | `20X Cross` |
| `1391` | `0xfdfb...dbb9` | `SHORT` | 1,626,687.29 USD | `15,966.70` | `101.16` | `101.90` | `107.02` | -11,457.79 USD | `-0.70%` | `20X Cross` |
| `1475` | `0x91fd...9841` | `LONG` | 1,541,951.56 USD | `15,134.98` | `101.16` | `101.90` | `95.58` | 10,876.06 USD | `+0.71%` | `13X Isolated` |
| `1482` | `0x17c3...a868` | `LONG` | 1,529,313.04 USD | `15,010.92` | `95.13` | `101.90` | `64.99` | 101,256.97 USD | `+6.62%` | `3X Isolated` |
| `1485` | `0x34ea...2f47` | `SHORT` | 1,528,050.00 USD | `15,000.00` | `99.80` | `101.90` | `192.93` | -31,048.69 USD | `-2.03%` | `20X Cross` |
| `1593` | `0xfb29...21dd` | `LONG` | 1,400,292.82 USD | `13,744.53` | `89.85` | `101.90` | `84.57` | 165,298.86 USD | `+11.80%` | `20X Cross` |
| `1607` | `0x6fa6...825e` | `SHORT` | 1,375,380.00 USD | `13,500.00` | `102.95` | `101.90` | `135.50` | 14,394.27 USD | `+1.05%` | `20X Isolated` |
| `1623` | `0xa9d9...b48e` | `SHORT` | 1,358,399.97 USD | `13,333.33` | `96.39` | `101.90` | `175.71` | -73,152.78 USD | `-5.39%` | `20X Cross` |
| `1721` | `0x89c2...c94b` | `LONG` | 1,259,714.72 USD | `12,364.69` | `75.25` | `101.90` | `45.77` | 329,231.57 USD | `+26.14%` | `3X Isolated` |
| `1740` | `0xcd81...36e3` | `SHORT` | 1,228,956.01 USD | `12,063.96` | `97.96` | `101.90` | `111.55` | -47,117.09 USD | `-3.83%` | `20X Cross` |
| `1748` | `0x436c...b3d1` | `SHORT` | 1,222,560.00 USD | `12,000.00` | `101.05` | `101.90` | `202.21` | -9,900.17 USD | `-0.81%` | `20X Cross` |
| `1809` | `0x5d6f...6f8a` | `LONG` | 1,171,620.00 USD | `11,500.00` | `101.81` | `101.90` | `7.96` | 815.00 USD | `+0.07%` | `20X Cross` |
| `1819` | `0x9dea...d617` | `LONG` | 1,161,513.30 USD | `11,400.80` | `90.37` | `101.90` | `2.02` | 131,239.58 USD | `+11.30%` | `20X Cross` |
| `1852` | `0x8afa...8113` | `SHORT` | 1,131,040.38 USD | `11,101.69` | `100.52` | `101.90` | `107.79` | -15,095.87 USD | `-1.33%` | `10X Isolated` |
| `1864` | `0x8607...08d5` | `SHORT` | 1,120,486.63 USD | `10,998.10` | `92.18` | `101.90` | `135.03` | -106,696.93 USD | `-9.52%` | `4X Isolated` |
| `1942` | `0xfc27...9d9d` | `LONG` | 1,054,162.03 USD | `10,343.03` | `101.58` | `101.90` | `0.000000` | 3,507.71 USD | `+0.33%` | `20X Cross` |
| `1992` | `0xf29c...9971` | `SHORT` | 1,018,800.00 USD | `10,000.00` | `101.10` | `101.90` | `118.37` | -7,803.97 USD | `-0.77%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.09` (Vol: 2,100,000.00 USD, Dist: `+1.18%`) | Long MP=`99.20` (Vol: 6,700,000.00 USD, Dist: `--2.63%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+2.12%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.66%`)
  * 3D Horizon: Short MP=`103.95` (Vol: 6,300,000.00 USD, Dist: `+2.04%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.58%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+2.06%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.58%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `101.53` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `103.80` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-44.74K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `17:15:00` | `101.53` | `101.53` | `101.53` | `101.75` | `101.45` | 83,758.95 USD | 19,892.75 USD | 63,866.20 USD | -43,973.45 USD | `-52.50%` | `0B / 1S` |
| `17:15:00` | `101.49` | `101.49` | `101.49` | `101.75` | `101.33` | 219,820.84 USD | 68,628.28 USD | 151,192.56 USD | -82,564.29 USD | `-37.56%` | `0B / 1S` |
| `17:20:00` | `101.42` | `101.42` | `101.42` | `101.56` | `101.33` | 73,223.80 USD | 24,355.55 USD | 48,868.24 USD | -24,512.69 USD | `-33.48%` | `0B / 1S` |
| `17:25:00` | `101.49` | `101.49` | `101.49` | `101.63` | `101.37` | 62,820.45 USD | 34,920.78 USD | 27,899.67 USD | 7,021.11 USD | `+11.18%` | `1B / 0S` |
| `17:30:00` | `101.02` | `101.02` | `101.02` | `101.63` | `100.97` | 248,496.90 USD | 26,745.32 USD | 221,751.58 USD | -195,006.25 USD | `-78.47%` | `0B / 1S` |
| `17:30:00` | `101.26` | `101.26` | `101.26` | `101.63` | `101.22` | 70,883.40 USD | 12,268.28 USD | 58,615.12 USD | -46,346.84 USD | `-65.38%` | `0B / 1S` |
| `17:35:00` | `101.26` | `101.26` | `101.26` | `101.44` | `101.23` | 72,297.50 USD | 21,583.96 USD | 50,713.54 USD | -29,129.57 USD | `-40.29%` | `0B / 1S` |
| `17:40:00` | `101.02` | `101.02` | `101.02` | `101.38` | `100.97` | 105,661.69 USD | 16,003.50 USD | 89,658.19 USD | -73,654.68 USD | `-69.71%` | `0B / 1S` |
| `17:45:00` | `101.08` | `101.08` | `101.08` | `101.25` | `100.92` | 76,218.09 USD | 41,284.80 USD | 34,933.29 USD | 6,351.51 USD | `+8.33%` | `1B / 0S` |
| `17:45:00` | `100.95` | `100.95` | `100.95` | `101.25` | `100.81` | 194,930.59 USD | 70,391.60 USD | 124,538.99 USD | -54,147.39 USD | `-27.78%` | `0B / 1S` |
| `5:00 UTC` | `100.57` | `100.66` | `100.57` | `100.94` | `100.43` | 21,596,195.23 USD | 13,257,846.46 USD | 8,338,348.77 USD | 4,919,497.70 USD | `+22.78%` | `17B / 2S` |
| `0:00 UTC` | `100.95` | `100.94` | `100.95` | `101.07` | `100.72` | 13,472,246.47 USD | 6,374,941.81 USD | 7,097,304.66 USD | -722,362.84 USD | `-5.36%` | `10B / 3S` |
| `5:00 UTC` | `101.00` | `101.01` | `101.00` | `101.28` | `100.85` | 14,129,778.63 USD | 7,872,450.16 USD | 6,257,328.47 USD | 1,615,121.68 USD | `+11.43%` | `13B / 2S` |
| `0:00 UTC` | `101.13` | `101.14` | `101.13` | `101.27` | `100.97` | 14,591,088.89 USD | 5,760,823.82 USD | 8,830,265.07 USD | -3,069,441.25 USD | `-21.04%` | `3B / 3S` |
| `5:00 UTC` | `101.12` | `101.21` | `101.12` | `101.41` | `101.05` | 8,287,817.82 USD | 4,949,702.76 USD | 3,338,115.06 USD | 1,611,587.69 USD | `+19.45%` | `9B / 2S` |
| `0:00 UTC` | `101.80` | `101.69` | `101.80` | `101.95` | `101.28` | 21,400,336.48 USD | 10,768,028.88 USD | 10,632,307.61 USD | 135,721.27 USD | `+0.63%` | `15B / 6S` |
| `5:00 UTC` | `101.68` | `101.64` | `101.68` | `101.91` | `101.38` | 9,829,156.63 USD | 4,338,777.97 USD | 5,490,378.67 USD | -1,151,600.70 USD | `-11.72%` | `10B / 10S` |
| `0:00 UTC` | `102.41` | `102.23` | `102.41` | `102.50` | `101.82` | 76,189,579.98 USD | 39,225,207.15 USD | 36,964,372.83 USD | 2,260,834.33 USD | `+2.97%` | `20B / 3S` |
| `5:00 UTC` | `102.02` | `102.01` | `102.02` | `102.13` | `101.85` | 13,174,401.35 USD | 6,982,040.79 USD | 6,192,360.55 USD | 789,680.24 USD | `+5.99%` | `1B / 6S` |
| `0:00 UTC` | `101.88` | `101.90` | `101.88` | `101.95` | `101.85` | 1,135,701.85 USD | 707,638.47 USD | 428,063.38 USD | 279,575.09 USD | `+24.62%` | `3B / 1S` |

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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `100.92` (Risk Distance: `0.5740` pts)
  * +2.5R Take Profit: `102.93`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.29` (Risk Distance: `0.5740` pts)
  * +2.5R Take Profit: `101.28`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
