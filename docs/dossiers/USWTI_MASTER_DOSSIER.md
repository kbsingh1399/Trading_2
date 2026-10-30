# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 08:00:30 IST` (`2026-10-30 02:30:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `105.06` | **Live Ask Quote**: `105.12` | **Mid Price**: `105.09`
- **Spread Points**: `55.00` | **Spread BPS**: `5.23 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `104.14` | VWAP Z-Score: `+1.03` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4021` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `76.45` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.48` | Lower -3.00σ Band: `101.79`
  * Upper +2.51σ Band: `106.10` | Lower -2.51σ Band: `102.17`
  * Upper +2.01σ Band: `105.71` | Lower -2.01σ Band: `102.56`
  * Upper +2.00σ Band: `105.70` | Lower -2.00σ Band: `102.57`
  * Upper +1.28σ Band: `105.14` | Lower -1.28σ Band: `103.13`
  * Upper +1.00σ Band: `104.92` | Lower -1.00σ Band: `103.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.92` | EMA-20=`103.53` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.97` (Slope: `+0.0000`) | EMA-100=`102.66`
  * Institutional Anchors: EMA-144=`102.53` | EMA-200=`102.35` (Slope: `+0.1590`) | EMA-233=`102.30`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.94` (Distance: `-0.05%`)
  * Point of Control (POC) = `103.38` (Distance: `+1.46%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+1.78%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.15` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`105.51` | Low=`104.67`
  * New York Session (13:00-21:00 UTC): High=`105.72` | Low=`104.46`
  * Initial Balance (First Hour): IB High=`105.41` | IB Low=`104.78`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `104.67` - `105.51`
  * Optimal Trade Entry (OTE 0.705): `105.30`
  * Structural Invalidation Anchor (0.786): `105.93`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.46` | `103.46` | `103.41` | `103.44` | `62` | 6,413.59 USD | 583.05 USD | `+9.09%` | 188,917.06 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `103.44` | `103.44` | `103.28` | `103.38` | `76` | 7,856.50 USD | -859.30 USD | `-10.94%` | 188,057.76 USD | `+0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `103.37` | `103.40` | `103.36` | `103.38` | `26` | 2,687.88 USD | 447.98 USD | `+16.67%` | 188,505.74 USD | `+0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.45` | `103.54` | `103.45` | `103.47` | `158` | 16,347.47 USD | -4,086.87 USD | `-25.00%` | 461,093.45 USD | `-0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `103.47` | `103.50` | `103.38` | `103.45` | `130` | 13,448.50 USD | 0.00 USD | `+0.00%` | 461,093.45 USD | `-0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `103.46` | `103.46` | `103.28` | `103.38` | `164` | 16,954.32 USD | -2,825.72 USD | `-16.67%` | 458,267.73 USD | `-0.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.41` | `103.64` | `103.39` | `103.54` | `3,425` | 354,634.78 USD | 138,377.10 USD | `+39.02%` | 264,832.59 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.47` | `103.54` | `103.22` | `103.45` | `907` | 93,829.15 USD | 17,338.00 USD | `+18.48%` | 282,170.59 USD | `-0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `103.46` | `103.48` | `103.24` | `103.48` | `567` | 58,673.16 USD | 30,533.99 USD | `+52.04%` | 312,704.58 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 233,244.08 USD | `+1.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,814,984.24 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 1,546,899.17 USD | `-0.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -1,491,052.92 USD | `+1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,353,751.12 USD | `+1.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 233,244.08 USD | `+1.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,814,984.24 USD | `+1.15` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 1,546,899.17 USD | `-0.53` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `38` | `0x0cc1...c7cb` | `LONG` | 31,330,117.21 USD | `300,817.26` | `98.89` | `104.13` | `30.90` | 1,580,616.18 USD | `+5.05%` | `3X Cross` |
| `103` | `0x30af...393e` | `LONG` | 18,510,527.44 USD | `177,712.44` | `100.98` | `104.13` | `93.19` | 565,125.55 USD | `+3.05%` | `10X Isolated` |
| `282` | `0x7fda...17d1` | `SHORT` | 8,191,145.35 USD | `78,647.58` | `100.15` | `104.13` | `211.98` | -314,523.50 USD | `-3.84%` | `20X Cross` |
| `321` | `0x10e1...f4bd` | `LONG` | 7,043,235.09 USD | `67,625.88` | `84.36` | `104.13` | `58.53` | 1,338,004.71 USD | `+19.00%` | `3X Isolated` |
| `391` | `0xea00...a918` | `SHORT` | 5,744,006.33 USD | `55,151.29` | `89.22` | `104.13` | `219.01` | -823,281.84 USD | `-14.33%` | `20X Cross` |
| `431` | `0x4692...164f` | `SHORT` | 4,984,237.08 USD | `47,856.33` | `103.71` | `104.13` | `1420.96` | -21,004.70 USD | `-0.42%` | `5X Cross` |
| `475` | `0x5989...bc29` | `SHORT` | 4,550,055.62 USD | `43,691.72` | `99.48` | `104.13` | `113.23` | -203,748.71 USD | `-4.48%` | `10X Cross` |
| `527` | `0xebe1...4070` | `LONG` | 4,165,597.08 USD | `39,999.97` | `101.87` | `104.13` | `0.000000` | 90,745.56 USD | `+2.18%` | `20X Cross` |
| `528` | `0xd84a...c8a5` | `SHORT` | 4,165,200.00 USD | `40,000.00` | `101.97` | `104.13` | `118.78` | -86,570.00 USD | `-2.08%` | `20X Cross` |
| `529` | `0xd507...c948` | `LONG` | 4,146,054.96 USD | `39,808.50` | `93.57` | `104.13` | `81.34` | 420,979.55 USD | `+10.15%` | `7X Isolated` |
| `587` | `0x354b...6425` | `SHORT` | 3,790,799.41 USD | `36,400.99` | `102.55` | `104.13` | `400.72` | -57,733.92 USD | `-1.52%` | `8X Cross` |
| `678` | `0xb5e7...eff1` | `SHORT` | 3,242,739.12 USD | `31,132.29` | `91.71` | `104.13` | `144.47` | -387,530.47 USD | `-11.95%` | `20X Cross` |
| `712` | `0xbd33...4200` | `SHORT` | 3,122,697.68 USD | `29,982.69` | `104.89` | `104.13` | `403.27` | 22,187.19 USD | `+0.71%` | `20X Cross` |
| `774` | `0x61d7...7dee` | `LONG` | 2,901,419.55 USD | `27,858.08` | `88.25` | `104.13` | `83.50` | 442,943.55 USD | `+15.27%` | `20X Cross` |
| `859` | `0xf0ae...2f74` | `SHORT` | 2,603,750.00 USD | `25,000.00` | `100.78` | `104.13` | `176.00` | -84,231.39 USD | `-3.24%` | `20X Cross` |
| `881` | `0x645b...87b8` | `SHORT` | 2,530,898.17 USD | `24,302.84` | `101.22` | `104.13` | `134.76` | -70,936.61 USD | `-2.80%` | `3X Isolated` |
| `936` | `0x58f0...0d20` | `SHORT` | 2,344,352.40 USD | `22,511.55` | `96.77` | `104.13` | `106.34` | -165,934.61 USD | `-7.08%` | `20X Cross` |
| `1049` | `0x9aa5...58af` | `SHORT` | 2,048,734.65 USD | `19,671.00` | `101.76` | `104.13` | `595.12` | -46,983.72 USD | `-2.29%` | `20X Cross` |
| `1216` | `0x4169...6f06` | `LONG` | 1,788,967.79 USD | `17,175.19` | `76.61` | `104.13` | `82.98` | 473,199.79 USD | `+26.45%` | `12X Isolated` |
| `1227` | `0x6788...98d4` | `SHORT` | 1,770,550.00 USD | `17,000.00` | `99.31` | `104.13` | `201.70` | -82,225.41 USD | `-4.64%` | `20X Cross` |
| `1277` | `0xa99c...40d5` | `SHORT` | 1,676,815.00 USD | `16,100.00` | `101.02` | `104.13` | `151.20` | -50,357.63 USD | `-3.00%` | `20X Cross` |
| `1283` | `0x1bf6...5bfa` | `SHORT` | 1,666,400.00 USD | `16,000.00` | `99.60` | `104.13` | `225.98` | -72,777.69 USD | `-4.37%` | `20X Cross` |
| `1299` | `0xbd69...45fb` | `SHORT` | 1,638,372.87 USD | `15,735.43` | `104.40` | `104.13` | `115.33` | 4,413.77 USD | `+0.27%` | `20X Cross` |
| `1310` | `0xe5dd...ecba` | `SHORT` | 1,622,347.20 USD | `15,575.53` | `102.71` | `104.13` | `144.69` | -22,591.83 USD | `-1.39%` | `20X Cross` |
| `1361` | `0x5d6f...6f8a` | `LONG` | 1,562,400.00 USD | `15,000.00` | `101.91` | `104.13` | `25.38` | 33,745.00 USD | `+2.16%` | `20X Cross` |
| `1362` | `0x34ea...2f47` | `SHORT` | 1,562,250.00 USD | `15,000.00` | `99.80` | `104.13` | `201.76` | -65,248.69 USD | `-4.18%` | `20X Cross` |
| `1441` | `0xfc27...9d9d` | `LONG` | 1,487,680.72 USD | `14,285.39` | `102.69` | `104.13` | `0.000000` | 20,780.45 USD | `+1.40%` | `20X Cross` |
| `1486` | `0xfb29...21dd` | `LONG` | 1,431,080.57 USD | `13,744.53` | `89.85` | `104.13` | `84.76` | 196,086.61 USD | `+13.70%` | `20X Cross` |
| `1512` | `0x6fa6...825e` | `SHORT` | 1,405,890.00 USD | `13,500.00` | `102.95` | `104.13` | `135.50` | -16,115.73 USD | `-1.15%` | `20X Isolated` |
| `1530` | `0xa9d9...b48e` | `SHORT` | 1,388,399.97 USD | `13,333.33` | `96.39` | `104.13` | `173.42` | -103,152.78 USD | `-7.43%` | `20X Cross` |
| `1581` | `0x936c...bb0f` | `SHORT` | 1,321,318.74 USD | `12,687.91` | `101.39` | `104.13` | `163.64` | -34,845.87 USD | `-2.64%` | `2X Isolated` |
| `1614` | `0x89c2...c94b` | `LONG` | 1,287,782.57 USD | `12,364.69` | `75.25` | `104.13` | `45.76` | 357,299.42 USD | `+27.75%` | `3X Isolated` |
| `1635` | `0xcd81...36e3` | `SHORT` | 1,256,461.85 USD | `12,063.96` | `97.96` | `104.13` | `108.86` | -74,622.93 USD | `-5.94%` | `20X Cross` |
| `1644` | `0x436c...b3d1` | `SHORT` | 1,249,680.00 USD | `12,000.00` | `101.05` | `104.13` | `211.24` | -37,020.17 USD | `-2.96%` | `20X Cross` |
| `1715` | `0x9dea...d617` | `LONG` | 1,187,393.11 USD | `11,400.80` | `90.37` | `104.13` | `8.82` | 157,119.39 USD | `+13.23%` | `20X Cross` |
| `1726` | `0x17c3...a868` | `LONG` | 1,177,582.08 USD | `11,306.60` | `95.13` | `104.13` | `64.99` | 101,935.21 USD | `+8.66%` | `3X Isolated` |
| `1761` | `0x0242...ffa1` | `LONG` | 1,145,750.71 USD | `11,000.97` | `104.43` | `104.13` | `0.000000` | -3,132.86 USD | `-0.27%` | `10X Cross` |
| `1763` | `0x8607...08d5` | `SHORT` | 1,145,452.32 USD | `10,998.10` | `92.18` | `104.13` | `135.02` | -131,662.62 USD | `-11.49%` | `4X Isolated` |
| `1844` | `0xb078...de15` | `LONG` | 1,083,244.18 USD | `10,401.81` | `104.67` | `104.13` | `0.000000` | -5,482.71 USD | `-0.51%` | `5X Cross` |
| `1874` | `0xce97...7e78` | `SHORT` | 1,054,445.64 USD | `10,124.30` | `103.21` | `104.13` | `120.85` | -9,493.80 USD | `-0.90%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `84.50` | 2,999.92 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Short: 3.00K USD at 84.5000 USD [API] | `2026-06-11 19:34:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.89` (Vol: 2,900,000.00 USD, Dist: `+1.13%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--3.47%`)
  * 48H Horizon: Short MP=`103.96` (Vol: 7,400,000.00 USD, Dist: `+1.20%`) | Long MP=`99.48` (Vol: 4,500,000.00 USD, Dist: `--3.16%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 7,000,000.00 USD, Dist: `+1.27%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.39%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 11,000,000.00 USD, Dist: `+1.22%`) | Long MP=`99.12` (Vol: 10,200,000.00 USD, Dist: `--3.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.94` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.95` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-157.58K` | Last 24h: `-366.73K` | Last 3d: `-686.90K` | Last 7d: `-1.13M`
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
| `01:40:00` | `103.47` | `103.47` | `103.47` | `103.54` | `103.47` | 4,035.14 USD | 201.76 USD | 3,833.38 USD | -3,631.62 USD | `-90.00%` | `0B / 1S` |
| `01:45:00` | `103.47` | `103.47` | `103.47` | `103.50` | `103.46` | 3,931.67 USD | 982.92 USD | 2,948.75 USD | -1,965.83 USD | `-50.00%` | `0B / 1S` |
| `01:45:00` | `103.45` | `103.45` | `103.45` | `103.50` | `103.38` | 13,448.50 USD | 6,724.25 USD | 6,724.25 USD | 0.00 USD | `+0.00%` | `1B / 0S` |
| `01:50:00` | `103.41` | `103.41` | `103.41` | `103.50` | `103.39` | 4,550.04 USD | 920.84 USD | 3,629.20 USD | -2,708.36 USD | `-59.52%` | `0B / 1S` |
| `01:55:00` | `103.45` | `103.45` | `103.45` | `103.45` | `103.38` | 4,965.60 USD | 4,344.90 USD | 620.70 USD | 3,724.20 USD | `+75.00%` | `1B / 0S` |
| `02:00:00` | `103.38` | `103.38` | `103.38` | `103.46` | `103.28` | 16,954.32 USD | 7,064.30 USD | 9,890.02 USD | -2,825.72 USD | `-16.67%` | `0B / 1S` |
| `02:00:00` | `103.48` | `103.48` | `103.48` | `103.48` | `103.24` | 58,673.16 USD | 44,603.58 USD | 14,069.58 USD | 30,533.99 USD | `+52.04%` | `1B / 0S` |
| `02:00:00` | `103.44` | `103.44` | `103.44` | `103.46` | `103.41` | 6,413.59 USD | 3,498.32 USD | 2,915.27 USD | 583.05 USD | `+9.09%` | `1B / 0S` |
| `02:05:00` | `103.38` | `103.38` | `103.38` | `103.44` | `103.28` | 7,856.50 USD | 3,498.60 USD | 4,357.90 USD | -859.30 USD | `-10.94%` | `0B / 1S` |
| `02:10:00` | `103.38` | `103.38` | `103.38` | `103.40` | `103.36` | 2,687.88 USD | 1,567.93 USD | 1,119.95 USD | 447.98 USD | `+16.67%` | `1B / 0S` |
| `0:00 UTC` | `102.91` | `102.88` | `102.91` | `103.00` | `102.75` | 22,493,822.01 USD | 8,410,545.53 USD | 14,083,276.47 USD | -5,672,730.94 USD | `-25.22%` | `1B / 6S` |
| `5:00 UTC` | `102.84` | `102.85` | `102.84` | `102.91` | `102.78` | 12,501,739.47 USD | 4,708,353.14 USD | 7,793,386.33 USD | -3,085,033.19 USD | `-24.68%` | `1B / 4S` |
| `0:00 UTC` | `102.80` | `102.83` | `102.80` | `102.93` | `102.75` | 11,683,758.36 USD | 3,517,048.40 USD | 8,166,709.96 USD | -4,649,661.56 USD | `-39.80%` | `1B / 5S` |
| `5:00 UTC` | `102.85` | `102.74` | `102.85` | `102.88` | `102.57` | 8,986,938.51 USD | 2,421,078.21 USD | 6,565,860.30 USD | -4,144,782.09 USD | `-46.12%` | `3B / 14S` |
| `0:00 UTC` | `102.78` | `102.78` | `102.78` | `103.02` | `102.57` | 31,355,759.70 USD | 14,370,056.44 USD | 16,985,703.26 USD | -2,615,646.82 USD | `-8.34%` | `6B / 5S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.81` | 12,332,708.79 USD | 3,885,730.79 USD | 8,446,978.00 USD | -4,561,247.21 USD | `-36.98%` | `0B / 5S` |
| `0:00 UTC` | `104.23` | `103.97` | `104.23` | `104.72` | `102.88` | 80,432,525.97 USD | 47,963,579.07 USD | 32,468,946.89 USD | 15,494,632.18 USD | `+19.26%` | `55B / 11S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.20` | `104.16` | `104.37` | `104.05` | 8,207,326.66 USD | 2,774,005.16 USD | 5,433,321.50 USD | -2,659,316.34 USD | `-32.40%` | `2B / 8S` |

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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.05` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.49` (Risk Distance: `0.5650` pts)
  * +2.5R Take Profit: `104.47`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.94` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.50` (Risk Distance: `0.5650` pts)
  * +2.5R Take Profit: `103.52`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.93`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
