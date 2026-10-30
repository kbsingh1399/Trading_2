# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 16:09:32 IST` (`2026-10-30 10:39:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.67` | **Live Ask Quote**: `104.72` | **Mid Price**: `104.69`
- **Spread Points**: `49.00` | **Spread BPS**: `4.68 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.16` | VWAP Z-Score: `+1.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3621` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.10` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.71` | Lower -3.00σ Band: `102.60`
  * Upper +2.51σ Band: `105.46` | Lower -2.51σ Band: `102.86`
  * Upper +2.01σ Band: `105.20` | Lower -2.01σ Band: `103.12`
  * Upper +2.00σ Band: `105.19` | Lower -2.00σ Band: `103.12`
  * Upper +1.28σ Band: `104.82` | Lower -1.28σ Band: `103.49`
  * Upper +1.00σ Band: `104.67` | Lower -1.00σ Band: `103.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.49` | EMA-20=`104.26` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.84` (Slope: `+0.0000`) | EMA-100=`103.37`
  * Institutional Anchors: EMA-144=`103.09` | EMA-200=`102.85` (Slope: `+0.1982`) | EMA-233=`102.78`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.94` (Distance: `-0.21%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.63%`)
  * Value Area Low (VAL) = `103.56` (Distance: `+1.11%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.40` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.92` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.92` | Low=`104.33`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.27` - `105.11`
  * Optimal Trade Entry (OTE 0.705): `104.90`
  * Structural Invalidation Anchor (0.786): `105.53`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.74` | `103.78` | `103.64` | `103.75` | `302` | 31,331.90 USD | 9,863.75 USD | `+31.48%` | 393,800.51 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.75` | `103.94` | `103.68` | `103.94` | `296` | 30,767.13 USD | 26,625.40 USD | `+86.54%` | 420,425.91 USD | `+0.95` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.95` | `104.10` | `103.91` | `104.06` | `343` | 35,693.27 USD | 21,529.27 USD | `+60.32%` | 441,955.18 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.51` | `103.61` | `103.36` | `103.45` | `925` | 95,689.40 USD | -24,879.24 USD | `-26.00%` | 520,708.14 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.46` | `103.86` | `103.46` | `103.75` | `1,084` | 112,462.83 USD | 64,562.00 USD | `+57.41%` | 585,270.13 USD | `+1.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.75` | `104.18` | `103.68` | `104.11` | `986` | 102,650.49 USD | 73,618.03 USD | `+71.72%` | 658,888.16 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.55` | `104.12` | `103.51` | `103.92` | `2,479` | 257,617.68 USD | 123,135.37 USD | `+47.80%` | 404,442.13 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.90` | `104.09` | `103.08` | `103.45` | `4,485` | 463,964.28 USD | -168,609.15 USD | `-36.34%` | 235,832.98 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `104.72` | `103.46` | `104.45` | `4,423` | 461,973.50 USD | 311,329.97 USD | `+67.39%` | 547,162.95 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,724,296.99 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 3,306,037.16 USD | `+0.70` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 3,037,952.09 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,704,696.24 USD | `-1.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `103.55` | `104.72` | `103.08` | `104.25` | `17,359` | 1,809,727.83 USD | 775,597.64 USD | `+42.86%` | 3,480,293.88 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:01:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,300,035.49 USD | `300,817.26` | `98.89` | `104.08` | `30.68` | 1,550,534.45 USD | `+4.95%` | `3X Cross` |
| `110` | `0x30af...393e` | `LONG` | 18,492,756.19 USD | `177,712.44` | `100.98` | `104.08` | `93.19` | 547,354.31 USD | `+2.96%` | `10X Isolated` |
| `283` | `0x7fda...17d1` | `SHORT` | 8,187,212.97 USD | `78,647.58` | `100.15` | `104.08` | `209.07` | -310,591.13 USD | `-3.79%` | `20X Cross` |
| `325` | `0x10e1...f4bd` | `LONG` | 7,036,472.50 USD | `67,625.88` | `84.36` | `104.08` | `58.53` | 1,331,242.12 USD | `+18.92%` | `3X Isolated` |
| `394` | `0xea00...a918` | `SHORT` | 5,737,939.69 USD | `55,151.29` | `89.22` | `104.08` | `233.92` | -817,215.20 USD | `-14.24%` | `20X Cross` |
| `487` | `0x5989...bc29` | `SHORT` | 4,546,123.36 USD | `43,691.72` | `99.48` | `104.08` | `113.23` | -199,816.46 USD | `-4.40%` | `10X Cross` |
| `498` | `0x354b...6425` | `SHORT` | 4,469,715.99 USD | `42,940.88` | `102.98` | `104.08` | `359.09` | -47,537.06 USD | `-1.06%` | `8X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,162,800.00 USD | `40,000.00` | `101.97` | `104.08` | `118.61` | -84,170.00 USD | `-2.02%` | `20X Cross` |
| `534` | `0xd507...c948` | `LONG` | 4,144,064.54 USD | `39,808.50` | `93.57` | `104.08` | `85.21` | 418,989.12 USD | `+10.11%` | `7X Isolated` |
| `573` | `0x4692...164f` | `SHORT` | 3,897,068.11 USD | `37,432.22` | `103.57` | `104.08` | `1820.37` | -20,090.50 USD | `-0.52%` | `5X Cross` |
| `691` | `0xb5e7...eff1` | `SHORT` | 3,240,871.18 USD | `31,132.29` | `91.71` | `104.08` | `144.67` | -385,662.54 USD | `-11.90%` | `20X Cross` |
| `721` | `0xbd33...4200` | `SHORT` | 3,120,299.07 USD | `29,982.69` | `104.89` | `104.08` | `403.27` | 24,585.81 USD | `+0.79%` | `20X Cross` |
| `781` | `0x61d7...7dee` | `LONG` | 2,900,026.65 USD | `27,858.08` | `88.25` | `104.08` | `83.50` | 441,550.65 USD | `+15.23%` | `20X Cross` |
| `864` | `0xf0ae...2f74` | `SHORT` | 2,601,500.00 USD | `25,000.00` | `100.78` | `104.08` | `175.25` | -81,981.39 USD | `-3.15%` | `20X Cross` |
| `865` | `0x645b...87b8` | `SHORT` | 2,590,336.40 USD | `24,895.11` | `101.26` | `104.08` | `134.75` | -69,380.95 USD | `-2.68%` | `3X Isolated` |
| `870` | `0x40f2...6a9e` | `LONG` | 2,565,330.62 USD | `24,652.42` | `103.40` | `104.08` | `101.28` | 16,265.09 USD | `+0.63%` | `20X Cross` |
| `1033` | `0xebe1...4070` | `LONG` | 2,080,997.50 USD | `19,999.98` | `101.87` | `104.08` | `0.000000` | 43,572.76 USD | `+2.09%` | `20X Cross` |
| `1050` | `0x9aa5...58af` | `SHORT` | 2,046,767.55 USD | `19,671.00` | `101.76` | `104.08` | `566.93` | -45,016.62 USD | `-2.20%` | `20X Cross` |
| `1225` | `0x4169...6f06` | `LONG` | 1,787,250.27 USD | `17,175.19` | `76.61` | `104.08` | `82.98` | 471,482.27 USD | `+26.38%` | `12X Isolated` |
| `1240` | `0x6788...98d4` | `SHORT` | 1,768,850.00 USD | `17,000.00` | `99.31` | `104.08` | `195.45` | -80,525.41 USD | `-4.55%` | `20X Cross` |
| `1290` | `0xa99c...40d5` | `SHORT` | 1,675,205.00 USD | `16,100.00` | `101.02` | `104.08` | `153.02` | -48,747.63 USD | `-2.91%` | `20X Cross` |
| `1297` | `0x1bf6...5bfa` | `SHORT` | 1,664,800.00 USD | `16,000.00` | `99.60` | `104.08` | `226.55` | -71,177.69 USD | `-4.28%` | `20X Cross` |
| `1337` | `0xce97...7e78` | `SHORT` | 1,608,942.73 USD | `15,463.17` | `103.16` | `104.08` | `120.79` | -13,781.30 USD | `-0.86%` | `5X Isolated` |
| `1351` | `0xfc27...9d9d` | `LONG` | 1,585,617.44 USD | `15,233.14` | `102.72` | `104.08` | `0.000000` | 20,924.38 USD | `+1.32%` | `20X Cross` |
| `1355` | `0xe5dd...ecba` | `SHORT` | 1,579,283.59 USD | `15,178.12` | `102.71` | `104.08` | `145.56` | -20,345.81 USD | `-1.29%` | `20X Cross` |
| `1376` | `0x5d6f...6f8a` | `LONG` | 1,561,500.00 USD | `15,000.00` | `101.91` | `104.08` | `24.62` | 32,845.00 USD | `+2.10%` | `20X Cross` |
| `1378` | `0x34ea...2f47` | `SHORT` | 1,560,600.00 USD | `15,000.00` | `99.80` | `104.08` | `196.49` | -63,598.69 USD | `-4.08%` | `20X Cross` |
| `1503` | `0xfb29...21dd` | `LONG` | 1,430,530.79 USD | `13,744.53` | `89.85` | `104.08` | `84.65` | 195,536.83 USD | `+13.67%` | `20X Cross` |
| `1527` | `0x6fa6...825e` | `SHORT` | 1,404,675.00 USD | `13,500.00` | `102.95` | `104.08` | `135.50` | -14,900.73 USD | `-1.06%` | `20X Isolated` |
| `1552` | `0xa9d9...b48e` | `SHORT` | 1,387,733.30 USD | `13,333.33` | `96.39` | `104.08` | `173.49` | -102,486.11 USD | `-7.39%` | `20X Cross` |
| `1602` | `0x936c...bb0f` | `SHORT` | 1,320,176.83 USD | `12,687.91` | `101.39` | `104.08` | `163.64` | -33,703.96 USD | `-2.55%` | `2X Isolated` |
| `1630` | `0x89c2...c94b` | `LONG` | 1,286,546.10 USD | `12,364.69` | `75.25` | `104.08` | `45.76` | 356,062.95 USD | `+27.68%` | `3X Isolated` |
| `1669` | `0xcd81...36e3` | `SHORT` | 1,255,134.81 USD | `12,063.96` | `97.96` | `104.08` | `109.74` | -73,295.89 USD | `-5.84%` | `20X Cross` |
| `1675` | `0x436c...b3d1` | `SHORT` | 1,249,200.00 USD | `12,000.00` | `101.05` | `104.08` | `219.12` | -36,540.17 USD | `-2.93%` | `20X Cross` |
| `1734` | `0x9dea...d617` | `LONG` | 1,186,253.03 USD | `11,400.80` | `90.37` | `104.08` | `5.09` | 155,979.31 USD | `+13.15%` | `20X Cross` |
| `1743` | `0x17c3...a868` | `LONG` | 1,176,338.35 USD | `11,306.60` | `95.13` | `104.08` | `64.99` | 100,691.48 USD | `+8.56%` | `3X Isolated` |
| `1796` | `0x8607...08d5` | `SHORT` | 1,144,352.51 USD | `10,998.10` | `92.18` | `104.08` | `135.02` | -130,562.81 USD | `-11.41%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+1.07%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.75%`)
  * 48H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+1.07%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.18%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.46%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.78%`)
  * 7D Horizon: Short MP=`105.22` (Vol: 4,800,000.00 USD, Dist: `+1.07%`) | Long MP=`99.12` (Vol: 8,000,000.00 USD, Dist: `--4.78%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.88` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.69` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-166.73K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0276%` | **USDT OKX** | `-0.0309%` |
| **USDT Bybit** | `-0.0637%` | **USDT KuCoin** | `-0.0231%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0473%` | **USDT Bitget** | `-0.0232%` |
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
| `10:00:00` | `103.58` | `103.58` | `103.58` | `103.61` | `103.46` | 39,981.11 USD | 33,983.94 USD | 5,997.17 USD | 27,986.78 USD | `+70.00%` | `1B / 0S` |
| `10:00:00` | `104.45` | `104.45` | `104.45` | `104.72` | `103.46` | 461,973.50 USD | 386,651.74 USD | 75,321.77 USD | 311,329.97 USD | `+67.39%` | `1B / 0S` |
| `10:05:00` | `103.76` | `103.76` | `103.76` | `103.86` | `103.47` | 41,088.17 USD | 30,025.97 USD | 11,062.20 USD | 18,963.77 USD | `+46.15%` | `1B / 0S` |
| `10:10:00` | `103.75` | `103.75` | `103.75` | `103.78` | `103.64` | 31,331.90 USD | 20,597.82 USD | 10,734.08 USD | 9,863.75 USD | `+31.48%` | `1B / 0S` |
| `10:15:00` | `104.11` | `104.11` | `104.11` | `104.18` | `103.68` | 102,650.49 USD | 88,134.26 USD | 14,516.23 USD | 73,618.03 USD | `+71.72%` | `1B / 0S` |
| `10:15:00` | `103.94` | `103.94` | `103.94` | `103.94` | `103.68` | 30,767.13 USD | 28,696.26 USD | 2,070.86 USD | 26,625.40 USD | `+86.54%` | `1B / 0S` |
| `10:20:00` | `104.06` | `104.06` | `104.06` | `104.10` | `103.91` | 35,693.27 USD | 28,611.27 USD | 7,082.00 USD | 21,529.27 USD | `+60.32%` | `1B / 0S` |
| `10:25:00` | `104.11` | `104.11` | `104.11` | `104.18` | `103.99` | 36,125.48 USD | 22,456.38 USD | 13,669.10 USD | 8,787.28 USD | `+24.32%` | `1B / 0S` |
| `10:30:00` | `104.29` | `104.29` | `104.29` | `104.30` | `103.92` | 37,649.77 USD | 32,026.75 USD | 5,623.02 USD | 26,403.74 USD | `+70.13%` | `1B / 0S` |
| `10:30:00` | `104.35` | `104.35` | `104.35` | `104.42` | `103.92` | 115,408.89 USD | 91,750.07 USD | 23,658.82 USD | 68,091.24 USD | `+59.00%` | `1B / 0S` |
| `5:00 UTC` | `103.66` | `103.71` | `103.66` | `103.91` | `103.53` | 12,894,660.60 USD | 5,121,489.28 USD | 7,773,171.32 USD | -2,651,682.04 USD | `-20.56%` | `1B / 7S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `104.13` | `104.11` | `104.13` | `104.23` | `103.91` | 11,480,392.01 USD | 6,191,179.30 USD | 5,289,212.71 USD | 901,966.59 USD | `+7.86%` | `6B / 4S` |
| `0:00 UTC` | `104.13` | `104.08` | `104.13` | `104.30` | `103.81` | 32,456,048.03 USD | 16,079,340.84 USD | 16,376,707.20 USD | -297,366.36 USD | `-0.92%` | `6B / 5S` |
| `5:00 UTC` | `104.27` | `104.27` | `104.27` | `104.38` | `104.16` | 6,725,440.32 USD | 3,224,158.80 USD | 3,501,281.52 USD | -277,122.71 USD | `-4.12%` | `3B / 5S` |
| `0:00 UTC` | `104.16` | `104.15` | `104.16` | `104.25` | `104.02` | 4,781,255.07 USD | 2,056,381.28 USD | 2,724,873.80 USD | -668,492.52 USD | `-13.98%` | `3B / 6S` |

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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.56` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `103.05` (Risk Distance: `0.5080` pts)
  * +2.5R Take Profit: `104.83`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.51 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.44` (Risk Distance: `0.5080` pts)
  * +2.5R Take Profit: `103.67`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.51 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
