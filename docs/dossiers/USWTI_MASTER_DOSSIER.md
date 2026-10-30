# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 15:24:08 IST` (`2026-10-30 09:54:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.65` | **Live Ask Quote**: `104.68` | **Mid Price**: `104.66`
- **Spread Points**: `30.00` | **Spread BPS**: `2.87 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.10` | VWAP Z-Score: `+0.82` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3659` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.64` | Lower -3.00σ Band: `102.56`
  * Upper +2.51σ Band: `105.39` | Lower -2.51σ Band: `102.81`
  * Upper +2.01σ Band: `105.13` | Lower -2.01σ Band: `103.07`
  * Upper +2.00σ Band: `105.13` | Lower -2.00σ Band: `103.08`
  * Upper +1.28σ Band: `104.76` | Lower -1.28σ Band: `103.44`
  * Upper +1.00σ Band: `104.61` | Lower -1.00σ Band: `103.59`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.26` | EMA-20=`104.10` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.73` (Slope: `+0.0000`) | EMA-100=`103.28`
  * Institutional Anchors: EMA-144=`103.02` | EMA-200=`102.79` (Slope: `+0.1764`) | EMA-233=`102.73`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.63` (Distance: `+0.03%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.58%`)
  * Value Area Low (VAL) = `103.43` (Distance: `+1.20%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.37` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.72` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`105.29` | Low=`104.04`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.24` - `105.08`
  * Optimal Trade Entry (OTE 0.705): `104.87`
  * Structural Invalidation Anchor (0.786): `105.50`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.34` | `103.50` | `103.29` | `103.50` | `298` | 30,842.40 USD | 27,261.18 USD | `+88.39%` | 388,987.89 USD | `+1.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.51` | `103.61` | `103.50` | `103.58` | `363` | 37,598.81 USD | 20,508.44 USD | `+54.55%` | 409,496.34 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.57` | `103.59` | `103.44` | `103.50` | `285` | 29,496.93 USD | -11,188.49 USD | `-37.93%` | 398,307.84 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.02` | `104.04` | `103.33` | `103.35` | `954` | 98,595.90 USD | -88,736.31 USD | `-90.00%` | 516,842.58 USD | `-1.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.36` | `103.50` | `103.08` | `103.50` | `1,922` | 198,923.16 USD | 133,899.85 USD | `+67.31%` | 650,742.43 USD | `+2.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.51` | `103.61` | `103.36` | `103.45` | `925` | 95,689.40 USD | -24,879.24 USD | `-26.00%` | 625,863.19 USD | `-0.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.83` | `103.95` | `103.45` | `103.55` | `1,077` | 111,525.50 USD | -64,177.65 USD | `-57.55%` | 603,488.42 USD | `-0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.55` | `104.12` | `103.51` | `103.92` | `2,479` | 257,617.68 USD | 123,135.37 USD | `+47.80%` | 726,623.79 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.90` | `104.09` | `103.08` | `103.45` | `4,485` | 463,964.28 USD | -168,609.15 USD | `-36.34%` | 558,014.63 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,303,043.66 USD | `300,817.26` | `98.89` | `104.05` | `30.78` | 1,553,542.63 USD | `+4.96%` | `3X Cross` |
| `108` | `0x30af...393e` | `LONG` | 18,496,310.44 USD | `177,712.44` | `100.98` | `104.05` | `93.19` | 550,908.55 USD | `+2.98%` | `10X Isolated` |
| `284` | `0x7fda...17d1` | `SHORT` | 8,184,067.07 USD | `78,647.58` | `100.15` | `104.05` | `209.06` | -307,445.22 USD | `-3.76%` | `20X Cross` |
| `326` | `0x10e1...f4bd` | `LONG` | 7,038,501.28 USD | `67,625.88` | `84.36` | `104.05` | `58.53` | 1,333,270.90 USD | `+18.94%` | `3X Isolated` |
| `395` | `0xea00...a918` | `SHORT` | 5,739,042.72 USD | `55,151.29` | `89.22` | `104.05` | `225.24` | -818,318.22 USD | `-14.26%` | `20X Cross` |
| `486` | `0x354b...6425` | `SHORT` | 4,553,056.43 USD | `43,754.15` | `102.98` | `104.05` | `354.26` | -47,239.94 USD | `-1.04%` | `8X Cross` |
| `487` | `0x5989...bc29` | `SHORT` | 4,546,997.20 USD | `43,691.72` | `99.48` | `104.05` | `113.23` | -200,690.29 USD | `-4.41%` | `10X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,162,400.00 USD | `40,000.00` | `101.97` | `104.05` | `118.69` | -83,770.00 USD | `-2.01%` | `20X Cross` |
| `534` | `0xd507...c948` | `LONG` | 4,143,268.37 USD | `39,808.50` | `93.57` | `104.05` | `82.63` | 418,192.96 USD | `+10.09%` | `7X Isolated` |
| `536` | `0x4692...164f` | `SHORT` | 4,113,799.09 USD | `39,532.95` | `103.45` | `104.05` | `1727.02` | -24,079.14 USD | `-0.59%` | `5X Cross` |
| `691` | `0xb5e7...eff1` | `SHORT` | 3,239,625.89 USD | `31,132.29` | `91.71` | `104.05` | `144.06` | -384,417.24 USD | `-11.87%` | `20X Cross` |
| `718` | `0xbd33...4200` | `SHORT` | 3,120,598.90 USD | `29,982.69` | `104.89` | `104.05` | `403.27` | 24,285.98 USD | `+0.78%` | `20X Cross` |
| `787` | `0x61d7...7dee` | `LONG` | 2,899,190.91 USD | `27,858.08` | `88.25` | `104.05` | `83.50` | 440,714.90 USD | `+15.20%` | `20X Cross` |
| `865` | `0xf0ae...2f74` | `SHORT` | 2,602,000.00 USD | `25,000.00` | `100.78` | `104.05` | `175.94` | -82,481.39 USD | `-3.17%` | `20X Cross` |
| `866` | `0x645b...87b8` | `SHORT` | 2,590,834.31 USD | `24,895.11` | `101.26` | `104.05` | `134.75` | -69,878.85 USD | `-2.70%` | `3X Isolated` |
| `871` | `0x40f2...6a9e` | `LONG` | 2,565,330.62 USD | `24,652.42` | `103.40` | `104.05` | `101.22` | 16,265.09 USD | `+0.63%` | `20X Cross` |
| `1001` | `0xebe1...4070` | `LONG` | 2,185,257.50 USD | `20,999.98` | `101.87` | `104.05` | `0.000000` | 45,961.40 USD | `+2.10%` | `20X Cross` |
| `1053` | `0x9aa5...58af` | `SHORT` | 2,046,964.26 USD | `19,671.00` | `101.76` | `104.05` | `580.23` | -45,213.33 USD | `-2.21%` | `20X Cross` |
| `1228` | `0x4169...6f06` | `LONG` | 1,787,593.78 USD | `17,175.19` | `76.61` | `104.05` | `82.98` | 471,825.78 USD | `+26.39%` | `12X Isolated` |
| `1247` | `0x6788...98d4` | `SHORT` | 1,769,020.00 USD | `17,000.00` | `99.31` | `104.05` | `196.60` | -80,695.41 USD | `-4.56%` | `20X Cross` |
| `1288` | `0xa99c...40d5` | `SHORT` | 1,675,366.00 USD | `16,100.00` | `101.02` | `104.05` | `151.34` | -48,908.63 USD | `-2.92%` | `20X Cross` |
| `1294` | `0x1bf6...5bfa` | `SHORT` | 1,665,280.00 USD | `16,000.00` | `99.60` | `104.05` | `227.18` | -71,657.69 USD | `-4.30%` | `20X Cross` |
| `1331` | `0xce97...7e78` | `SHORT` | 1,619,242.07 USD | `15,560.66` | `103.08` | `104.05` | `120.70` | -15,159.78 USD | `-0.94%` | `5X Isolated` |
| `1353` | `0xe5dd...ecba` | `SHORT` | 1,579,738.94 USD | `15,178.12` | `102.71` | `104.05` | `145.52` | -20,801.15 USD | `-1.32%` | `20X Cross` |
| `1370` | `0x5d6f...6f8a` | `LONG` | 1,561,200.00 USD | `15,000.00` | `101.91` | `104.05` | `25.06` | 32,545.00 USD | `+2.08%` | `20X Cross` |
| `1372` | `0x34ea...2f47` | `SHORT` | 1,560,900.00 USD | `15,000.00` | `99.80` | `104.05` | `198.55` | -63,898.69 USD | `-4.09%` | `20X Cross` |
| `1380` | `0xfc27...9d9d` | `LONG` | 1,556,175.57 USD | `14,954.60` | `102.69` | `104.05` | `0.000000` | 20,451.83 USD | `+1.31%` | `20X Cross` |
| `1498` | `0xfb29...21dd` | `LONG` | 1,430,393.34 USD | `13,744.53` | `89.85` | `104.05` | `84.72` | 195,399.38 USD | `+13.66%` | `20X Cross` |
| `1522` | `0x6fa6...825e` | `SHORT` | 1,404,945.00 USD | `13,500.00` | `102.95` | `104.05` | `135.50` | -15,170.73 USD | `-1.08%` | `20X Isolated` |
| `1543` | `0xa9d9...b48e` | `SHORT` | 1,387,466.63 USD | `13,333.33` | `96.39` | `104.05` | `173.38` | -102,219.45 USD | `-7.37%` | `20X Cross` |
| `1602` | `0x936c...bb0f` | `SHORT` | 1,320,430.59 USD | `12,687.91` | `101.39` | `104.05` | `163.64` | -33,957.71 USD | `-2.57%` | `2X Isolated` |
| `1637` | `0x89c2...c94b` | `LONG` | 1,286,669.75 USD | `12,364.69` | `75.25` | `104.05` | `45.76` | 356,186.59 USD | `+27.68%` | `3X Isolated` |
| `1675` | `0xcd81...36e3` | `SHORT` | 1,255,376.09 USD | `12,063.96` | `97.96` | `104.05` | `109.20` | -73,537.17 USD | `-5.86%` | `20X Cross` |
| `1686` | `0x436c...b3d1` | `SHORT` | 1,248,840.00 USD | `12,000.00` | `101.05` | `104.05` | `220.21` | -36,180.17 USD | `-2.90%` | `20X Cross` |
| `1747` | `0x9dea...d617` | `LONG` | 1,186,595.06 USD | `11,400.80` | `90.37` | `104.05` | `5.58` | 156,321.33 USD | `+13.17%` | `20X Cross` |
| `1754` | `0x17c3...a868` | `LONG` | 1,176,790.62 USD | `11,306.60` | `95.13` | `104.05` | `64.99` | 101,143.75 USD | `+8.59%` | `3X Isolated` |
| `1806` | `0x8607...08d5` | `SHORT` | 1,144,682.46 USD | `10,998.10` | `92.18` | `104.05` | `135.02` | -130,892.75 USD | `-11.43%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 4,100,000.00 USD, Dist: `+1.78%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.64%`)
  * 48H Horizon: Short MP=`104.59` (Vol: 4,000,000.00 USD, Dist: `+0.59%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--2.07%`)
  * 3D Horizon: Short MP=`104.58` (Vol: 4,000,000.00 USD, Dist: `+0.58%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.67%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+1.54%`) | Long MP=`99.12` (Vol: 8,800,000.00 USD, Dist: `--4.67%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.41` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.19` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-176.30K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0297%` | **USDT OKX** | `-0.0322%` |
| **USDT Bybit** | `-0.0687%` | **USDT KuCoin** | `-0.0244%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0453%` | **USDT Bitget** | `-0.0232%` |
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
| `09:05:00` | `103.97` | `103.97` | `103.97` | `104.01` | `103.76` | 23,288.83 USD | 16,872.52 USD | 6,416.31 USD | 10,456.21 USD | `+44.90%` | `1B / 0S` |
| `09:10:00` | `104.01` | `104.01` | `104.01` | `104.09` | `103.95` | 20,178.52 USD | 11,530.58 USD | 8,647.94 USD | 2,882.65 USD | `+14.29%` | `1B / 0S` |
| `09:15:00` | `103.35` | `103.35` | `103.35` | `104.04` | `103.33` | 98,595.90 USD | 4,929.80 USD | 93,666.10 USD | -88,736.31 USD | `-90.00%` | `0B / 1S` |
| `09:15:00` | `103.97` | `103.97` | `103.97` | `104.02` | `103.89` | 20,169.79 USD | 9,076.41 USD | 11,093.39 USD | -2,016.98 USD | `-10.00%` | `0B / 1S` |
| `09:20:00` | `103.98` | `103.98` | `103.98` | `103.98` | `103.91` | 17,885.08 USD | 13,733.18 USD | 4,151.89 USD | 9,581.29 USD | `+53.57%` | `1B / 0S` |
| `09:25:00` | `103.35` | `103.35` | `103.35` | `104.04` | `103.33` | 60,769.80 USD | 3,038.49 USD | 57,731.31 USD | -54,692.82 USD | `-90.00%` | `0B / 1S` |
| `09:30:00` | `103.42` | `103.42` | `103.42` | `103.47` | `103.08` | 111,171.12 USD | 79,768.89 USD | 31,402.23 USD | 48,366.66 USD | `+43.51%` | `1B / 0S` |
| `09:30:00` | `103.50` | `103.50` | `103.50` | `103.50` | `103.08` | 198,923.16 USD | 166,411.50 USD | 32,511.65 USD | 133,899.85 USD | `+67.31%` | `1B / 0S` |
| `09:35:00` | `103.34` | `103.34` | `103.34` | `103.46` | `103.22` | 56,734.21 USD | 24,616.08 USD | 32,118.13 USD | -7,502.04 USD | `-13.22%` | `0B / 1S` |
| `09:40:00` | `103.50` | `103.50` | `103.50` | `103.50` | `103.29` | 30,842.40 USD | 29,051.79 USD | 1,790.61 USD | 27,261.18 USD | `+88.39%` | `1B / 0S` |
| `0:00 UTC` | `103.81` | `103.77` | `103.81` | `103.93` | `103.44` | 11,322,481.70 USD | 6,201,023.76 USD | 5,121,457.94 USD | 1,079,565.82 USD | `+9.53%` | `13B / 8S` |
| `5:00 UTC` | `103.97` | `104.00` | `103.97` | `104.22` | `103.69` | 15,722,195.08 USD | 7,756,867.01 USD | 7,965,328.07 USD | -208,461.06 USD | `-1.33%` | `8B / 12S` |
| `0:00 UTC` | `104.00` | `103.97` | `104.00` | `104.09` | `103.80` | 12,864,820.33 USD | 5,029,660.97 USD | 7,835,159.36 USD | -2,805,498.39 USD | `-21.81%` | `3B / 7S` |
| `5:00 UTC` | `103.66` | `103.71` | `103.66` | `103.91` | `103.53` | 12,894,660.60 USD | 5,121,489.28 USD | 7,773,171.32 USD | -2,651,682.04 USD | `-20.56%` | `1B / 7S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.82` | `103.52` | 6,144,231.72 USD | 3,135,860.45 USD | 3,008,371.27 USD | 127,489.18 USD | `+2.07%` | `10B / 2S` |
| `0:00 UTC` | `103.59` | `103.73` | `103.59` | `104.00` | `103.55` | 7,182,771.10 USD | 4,006,217.78 USD | 3,176,553.31 USD | 829,664.47 USD | `+11.55%` | `10B / 6S` |
| `5:00 UTC` | `103.97` | `103.96` | `103.97` | `104.00` | `103.91` | 1,042,612.01 USD | 639,518.75 USD | 403,093.26 USD | 236,425.50 USD | `+22.68%` | `3B / 1S` |

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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.94` (Risk Distance: `0.4841` pts)
  * +2.5R Take Profit: `104.64`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.48 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.63` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.12` (Risk Distance: `0.4841` pts)
  * +2.5R Take Profit: `103.42`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.48 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.50`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
