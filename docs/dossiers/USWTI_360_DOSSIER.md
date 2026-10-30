# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.79` | **Live Ask Quote**: `104.85` | **Mid Price**: `104.82`
- **Spread Points**: `60.00` | **Spread BPS**: `5.72 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.23` | VWAP Z-Score: `+1.29` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3551` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `63.13` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.80` | Lower -3.00σ Band: `102.65`
  * Upper +2.51σ Band: `105.55` | Lower -2.51σ Band: `102.90`
  * Upper +2.01σ Band: `105.28` | Lower -2.01σ Band: `103.17`
  * Upper +2.00σ Band: `105.28` | Lower -2.00σ Band: `103.17`
  * Upper +1.28σ Band: `104.90` | Lower -1.28σ Band: `103.55`
  * Upper +1.00σ Band: `104.75` | Lower -1.00σ Band: `103.70`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.70` | EMA-20=`104.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`104.02` (Slope: `+0.0000`) | EMA-100=`103.50`
  * Institutional Anchors: EMA-144=`103.20` | EMA-200=`102.95` (Slope: `+0.2071`) | EMA-233=`102.87`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `105.02` (Distance: `-0.31%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.62%`)
  * Value Area Low (VAL) = `103.73` (Distance: `+0.93%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.44` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`105.14` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`105.14` | Low=`104.33`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.40` - `105.24`
  * Optimal Trade Entry (OTE 0.705): `105.03`
  * Structural Invalidation Anchor (0.786): `105.66`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.53` | `104.53` | `104.29` | `104.41` | `437` | 45,628.48 USD | -10,243.13 USD | `-22.45%` | 462,664.70 USD | `-0.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.41` | `104.42` | `104.05` | `104.14` | `445` | 46,343.64 USD | -28,567.99 USD | `-61.64%` | 434,096.71 USD | `-1.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.15` | `104.31` | `104.09` | `104.13` | `421` | 43,837.47 USD | -16,040.53 USD | `-36.59%` | 418,056.18 USD | `-0.80` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.43` | `104.45` | `104.03` | `104.31` | `1,863` | 194,322.08 USD | 936.49 USD | `+0.48%` | 850,552.23 USD | `-0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `104.34` | `104.59` | `104.29` | `104.41` | `1,473` | 153,800.35 USD | 5,092.73 USD | `+3.31%` | 855,644.96 USD | `-0.16` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `104.41` | `104.42` | `104.05` | `104.25` | `1,233` | 128,543.95 USD | -21,130.51 USD | `-16.44%` | 834,514.45 USD | `-0.69` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.90` | `104.09` | `103.08` | `103.45` | `4,485` | 463,964.28 USD | -168,609.15 USD | `-36.34%` | 630,221.87 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `104.72` | `103.46` | `104.45` | `4,423` | 461,973.50 USD | 311,329.97 USD | `+67.39%` | 941,551.84 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.45` | `104.61` | `104.03` | `104.25` | `5,972` | 622,598.92 USD | -182,485.89 USD | `-29.31%` | 759,065.96 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,300,035.49 USD | `300,817.26` | `98.89` | `104.07` | `30.68` | 1,550,534.45 USD | `+4.95%` | `3X Cross` |
| `107` | `0x30af...393e` | `LONG` | 18,496,310.44 USD | `177,712.44` | `100.98` | `104.07` | `93.19` | 550,908.55 USD | `+2.98%` | `10X Isolated` |
| `237` | `0x2a8a...ca60` | `LONG` | 9,368,942.93 USD | `90,034.05` | `104.27` | `104.07` | `101.52` | -18,794.49 USD | `-0.20%` | `20X Cross` |
| `289` | `0x7fda...17d1` | `SHORT` | 8,186,426.50 USD | `78,647.58` | `100.15` | `104.07` | `210.00` | -309,804.65 USD | `-3.78%` | `20X Cross` |
| `329` | `0x10e1...f4bd` | `LONG` | 7,037,148.76 USD | `67,625.88` | `84.36` | `104.07` | `58.53` | 1,331,918.38 USD | `+18.93%` | `3X Isolated` |
| `381` | `0x354b...6425` | `SHORT` | 6,034,242.92 USD | `57,971.40` | `103.36` | `104.07` | `294.09` | -42,592.70 USD | `-0.71%` | `8X Cross` |
| `394` | `0xea00...a918` | `SHORT` | 5,739,594.23 USD | `55,151.29` | `89.22` | `104.07` | `227.33` | -818,869.74 USD | `-14.27%` | `20X Cross` |
| `488` | `0x5989...bc29` | `SHORT` | 4,546,560.28 USD | `43,691.72` | `99.48` | `104.07` | `113.23` | -200,253.38 USD | `-4.40%` | `10X Cross` |
| `530` | `0xd84a...c8a5` | `SHORT` | 4,163,200.00 USD | `40,000.00` | `101.97` | `104.07` | `118.61` | -84,570.00 USD | `-2.03%` | `20X Cross` |
| `535` | `0xd507...c948` | `LONG` | 4,142,472.20 USD | `39,808.50` | `93.57` | `104.07` | `85.21` | 417,396.79 USD | `+10.08%` | `7X Isolated` |
| `563` | `0x4692...164f` | `SHORT` | 3,946,744.10 USD | `37,916.65` | `103.84` | `104.07` | `1817.47` | -9,629.77 USD | `-0.24%` | `5X Cross` |
| `692` | `0xb5e7...eff1` | `SHORT` | 3,240,248.54 USD | `31,132.29` | `91.71` | `104.07` | `144.68` | -385,039.89 USD | `-11.88%` | `20X Cross` |
| `722` | `0xbd33...4200` | `SHORT` | 3,120,598.90 USD | `29,982.69` | `104.89` | `104.07` | `403.27` | 24,285.98 USD | `+0.78%` | `20X Cross` |
| `786` | `0x61d7...7dee` | `LONG` | 2,898,912.33 USD | `27,858.08` | `88.25` | `104.07` | `83.50` | 440,436.32 USD | `+15.19%` | `20X Cross` |
| `862` | `0xf0ae...2f74` | `SHORT` | 2,602,000.00 USD | `25,000.00` | `100.78` | `104.07` | `176.07` | -82,481.39 USD | `-3.17%` | `20X Cross` |
| `864` | `0x645b...87b8` | `SHORT` | 2,590,585.35 USD | `24,895.11` | `101.26` | `104.07` | `134.75` | -69,629.90 USD | `-2.69%` | `3X Isolated` |
| `871` | `0x40f2...6a9e` | `LONG` | 2,565,330.62 USD | `24,652.42` | `103.40` | `104.07` | `101.26` | 16,265.09 USD | `+0.63%` | `20X Cross` |
| `1049` | `0x9aa5...58af` | `SHORT` | 2,047,554.39 USD | `19,671.00` | `101.76` | `104.07` | `570.10` | -45,803.46 USD | `-2.24%` | `20X Cross` |
| `1153` | `0xce97...7e78` | `SHORT` | 1,907,395.96 USD | `18,324.49` | `103.63` | `104.07` | `121.33` | -8,373.18 USD | `-0.44%` | `5X Isolated` |
| `1227` | `0x4169...6f06` | `LONG` | 1,787,593.78 USD | `17,175.19` | `76.61` | `104.07` | `82.98` | 471,825.78 USD | `+26.39%` | `12X Isolated` |
| `1239` | `0x6788...98d4` | `SHORT` | 1,768,850.00 USD | `17,000.00` | `99.31` | `104.07` | `196.18` | -80,525.41 USD | `-4.55%` | `20X Cross` |
| `1294` | `0xa99c...40d5` | `SHORT` | 1,675,205.00 USD | `16,100.00` | `101.02` | `104.07` | `148.20` | -48,747.63 USD | `-2.91%` | `20X Cross` |
| `1297` | `0x1bf6...5bfa` | `SHORT` | 1,664,960.00 USD | `16,000.00` | `99.60` | `104.07` | `227.19` | -71,337.69 USD | `-4.28%` | `20X Cross` |
| `1337` | `0xe5dd...ecba` | `SHORT` | 1,619,130.41 USD | `15,556.59` | `102.79` | `104.07` | `144.29` | -20,089.52 USD | `-1.24%` | `20X Cross` |
| `1374` | `0x5d6f...6f8a` | `LONG` | 1,561,200.00 USD | `15,000.00` | `101.91` | `104.07` | `24.68` | 32,545.00 USD | `+2.08%` | `20X Cross` |
| `1375` | `0x34ea...2f47` | `SHORT` | 1,560,600.00 USD | `15,000.00` | `99.80` | `104.07` | `197.83` | -63,598.69 USD | `-4.08%` | `20X Cross` |
| `1503` | `0xfb29...21dd` | `LONG` | 1,430,118.45 USD | `13,744.53` | `89.85` | `104.07` | `84.67` | 195,124.49 USD | `+13.64%` | `20X Cross` |
| `1523` | `0x6fa6...825e` | `SHORT` | 1,404,810.00 USD | `13,500.00` | `102.95` | `104.07` | `135.50` | -15,035.73 USD | `-1.07%` | `20X Isolated` |
| `1547` | `0xa9d9...b48e` | `SHORT` | 1,387,733.30 USD | `13,333.33` | `96.39` | `104.07` | `173.43` | -102,486.11 USD | `-7.39%` | `20X Cross` |
| `1606` | `0x936c...bb0f` | `SHORT` | 1,320,303.71 USD | `12,687.91` | `101.39` | `104.07` | `163.64` | -33,830.84 USD | `-2.56%` | `2X Isolated` |
| `1645` | `0x89c2...c94b` | `LONG` | 1,286,546.10 USD | `12,364.69` | `75.25` | `104.07` | `45.76` | 356,062.95 USD | `+27.68%` | `3X Isolated` |
| `1675` | `0xcd81...36e3` | `SHORT` | 1,255,134.81 USD | `12,063.96` | `97.96` | `104.07` | `109.79` | -73,295.89 USD | `-5.84%` | `20X Cross` |
| `1684` | `0x436c...b3d1` | `SHORT` | 1,248,720.00 USD | `12,000.00` | `101.05` | `104.07` | `219.34` | -36,060.17 USD | `-2.89%` | `20X Cross` |
| `1748` | `0x9dea...d617` | `LONG` | 1,186,709.06 USD | `11,400.80` | `90.37` | `104.07` | `0.000000` | 156,435.34 USD | `+13.18%` | `20X Cross` |
| `1757` | `0x17c3...a868` | `LONG` | 1,176,225.29 USD | `11,306.60` | `95.13` | `104.07` | `64.99` | 100,578.42 USD | `+8.55%` | `3X Isolated` |
| `1804` | `0x8607...08d5` | `SHORT` | 1,144,462.49 USD | `10,998.10` | `92.18` | `104.07` | `135.02` | -130,672.79 USD | `-11.42%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.86%`)
  * 48H Horizon: Short MP=`105.21` (Vol: 4,700,000.00 USD, Dist: `+0.95%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.35%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.89%`)
  * 7D Horizon: Short MP=`105.22` (Vol: 4,800,000.00 USD, Dist: `+0.96%`) | Long MP=`99.12` (Vol: 8,000,000.00 USD, Dist: `--4.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `104.00` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.73` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-133.86K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0215%` | **USDT OKX** | `-0.0253%` |
| **USDT Bybit** | `-0.0541%` | **USDT KuCoin** | `-0.0233%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0397%` | **USDT Bitget** | `-0.0189%` |
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
| `10:40:00` | `104.35` | `104.35` | `104.35` | `104.42` | `104.24` | 39,756.59 USD | 27,897.38 USD | 11,859.21 USD | 16,038.17 USD | `+40.34%` | `1B / 0S` |
| `10:45:00` | `104.40` | `104.40` | `104.40` | `104.40` | `104.19` | 37,792.08 USD | 30,593.59 USD | 7,198.49 USD | 23,395.09 USD | `+61.90%` | `1B / 0S` |
| `10:45:00` | `104.45` | `104.45` | `104.45` | `104.72` | `104.19` | 130,246.66 USD | 70,652.67 USD | 59,593.99 USD | 11,058.68 USD | `+8.49%` | `1B / 0S` |
| `10:50:00` | `104.65` | `104.65` | `104.65` | `104.72` | `104.40` | 47,824.14 USD | 39,417.55 USD | 8,406.59 USD | 31,010.96 USD | `+64.84%` | `1B / 0S` |
| `10:55:00` | `104.45` | `104.45` | `104.45` | `104.70` | `104.38` | 44,703.74 USD | 8,381.95 USD | 36,321.79 USD | -27,939.84 USD | `-62.50%` | `0B / 1S` |
| `11:00:00` | `104.25` | `104.25` | `104.25` | `104.61` | `104.03` | 622,598.92 USD | 220,056.51 USD | 402,542.40 USD | -182,485.89 USD | `-29.31%` | `0B / 1S` |
| `11:00:00` | `104.50` | `104.50` | `104.50` | `104.59` | `104.30` | 57,996.39 USD | 36,370.62 USD | 21,625.77 USD | 14,744.84 USD | `+25.42%` | `1B / 0S` |
| `11:00:00` | `104.43` | `104.43` | `104.43` | `104.61` | `104.30` | 146,512.48 USD | 63,953.86 USD | 82,558.62 USD | -18,604.76 USD | `-12.70%` | `0B / 1S` |
| `11:05:00` | `104.54` | `104.54` | `104.54` | `104.61` | `104.45` | 45,998.92 USD | 28,389.96 USD | 17,608.96 USD | 10,781.00 USD | `+23.44%` | `1B / 0S` |
| `11:10:00` | `104.43` | `104.43` | `104.43` | `104.58` | `104.37` | 42,606.62 USD | 10,132.06 USD | 32,474.56 USD | -22,342.50 USD | `-52.44%` | `0B / 1S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `104.13` | `104.11` | `104.13` | `104.23` | `103.91` | 11,480,392.01 USD | 6,191,179.30 USD | 5,289,212.71 USD | 901,966.59 USD | `+7.86%` | `6B / 4S` |
| `0:00 UTC` | `104.13` | `104.08` | `104.13` | `104.30` | `103.81` | 32,456,048.03 USD | 16,079,340.84 USD | 16,376,707.20 USD | -297,366.36 USD | `-0.92%` | `6B / 5S` |
| `5:00 UTC` | `104.27` | `104.27` | `104.27` | `104.38` | `104.16` | 6,725,440.32 USD | 3,224,158.80 USD | 3,501,281.52 USD | -277,122.71 USD | `-4.12%` | `3B / 5S` |
| `0:00 UTC` | `104.25` | `104.18` | `104.25` | `104.31` | `104.02` | 8,036,249.92 USD | 3,423,895.23 USD | 4,612,354.69 USD | -1,188,459.46 USD | `-14.79%` | `2B / 6S` |
| `5:00 UTC` | `104.35` | `104.33` | `104.35` | `104.43` | `104.18` | 7,252,663.05 USD | 2,783,961.75 USD | 4,468,701.30 USD | -1,684,739.55 USD | `-23.23%` | `4B / 5S` |
| `0:00 UTC` | `104.27` | `104.27` | `104.27` | `104.41` | `104.12` | 15,166,157.59 USD | 7,105,752.36 USD | 8,060,405.23 USD | -954,652.87 USD | `-6.29%` | `4B / 2S` |
| `5:00 UTC` | `104.34` | `104.34` | `104.34` | `104.41` | `104.28` | 2,375,763.92 USD | 790,363.88 USD | 1,585,400.04 USD | -795,036.16 USD | `-33.46%` | `3B / 3S` |

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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `103.22` (Risk Distance: `0.5161` pts)
  * +2.5R Take Profit: `105.02`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.52 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `105.02` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.54` (Risk Distance: `0.5161` pts)
  * +2.5R Take Profit: `103.73`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.52 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.66`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
