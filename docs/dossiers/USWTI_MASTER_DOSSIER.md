# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 10:43:54 IST` (`2026-10-30 05:13:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.59` | **Live Ask Quote**: `103.64` | **Mid Price**: `103.61`
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
  * Session VWAP: `104.18` | VWAP Z-Score: `-0.98` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3175` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.94` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.10` | Lower -3.00σ Band: `102.26`
  * Upper +2.51σ Band: `105.78` | Lower -2.51σ Band: `102.58`
  * Upper +2.01σ Band: `105.46` | Lower -2.01σ Band: `102.89`
  * Upper +2.00σ Band: `105.46` | Lower -2.00σ Band: `102.90`
  * Upper +1.28σ Band: `105.00` | Lower -1.28σ Band: `103.36`
  * Upper +1.00σ Band: `104.82` | Lower -1.00σ Band: `103.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.82` | EMA-20=`103.79` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.34` (Slope: `+0.0000`) | EMA-100=`102.93`
  * Institutional Anchors: EMA-144=`102.74` | EMA-200=`102.52` (Slope: `+0.1808`) | EMA-233=`102.46`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.50` (Distance: `-0.85%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.22%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.53%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`103.65` | Low=`103.51`
  * New York Session (13:00-21:00 UTC): High=`104.23` | Low=`102.99`
  * Initial Balance (First Hour): IB High=`103.65` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.20` - `104.03`
  * Optimal Trade Entry (OTE 0.705): `103.82`
  * Structural Invalidation Anchor (0.786): `104.44`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.92` | `105.25` | `104.92` | `105.11` | `673` | 70,737.01 USD | 25,110.57 USD | `+35.50%` | 475,528.04 USD | `+0.39` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `105.11` | `105.18` | `104.86` | `104.96` | `579` | 60,772.42 USD | -24,801.21 USD | `-40.81%` | 450,726.84 USD | `-1.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.94` | `105.06` | `104.75` | `104.77` | `470` | 49,240.49 USD | -34,702.82 USD | `-70.48%` | 416,024.02 USD | `-1.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.41` | `105.19` | `103.34` | `105.01` | `2,427` | 254,859.27 USD | 211,924.76 USD | `+83.15%` | 1,031,528.59 USD | `+3.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `105.03` | `105.59` | `104.80` | `104.94` | `2,594` | 272,227.33 USD | -98,446.99 USD | `-36.16%` | 933,081.60 USD | `-1.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.92` | `105.25` | `104.75` | `104.77` | `1,722` | 180,408.77 USD | -111,535.28 USD | `-61.82%` | 821,546.32 USD | `-1.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 670,573.75 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 1,176,000.01 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.92` | `105.25` | `103.91` | `103.99` | `4,862` | 505,599.38 USD | -397,014.28 USD | `-78.52%` | 778,985.73 USD | `-1.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -392,114.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,194,880.62 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 30,987,185.54 USD | `300,817.26` | `98.89` | `103.00` | `31.57` | 1,237,684.51 USD | `+3.99%` | `3X Cross` |
| `113` | `0x30af...393e` | `LONG` | 18,306,158.14 USD | `177,712.44` | `100.98` | `103.00` | `93.19` | 360,756.25 USD | `+1.97%` | `10X Isolated` |
| `289` | `0x7fda...17d1` | `SHORT` | 8,100,700.64 USD | `78,647.58` | `100.15` | `103.00` | `212.12` | -224,078.79 USD | `-2.77%` | `20X Cross` |
| `328` | `0x10e1...f4bd` | `LONG` | 6,965,465.33 USD | `67,625.88` | `84.36` | `103.00` | `58.53` | 1,260,234.95 USD | `+18.09%` | `3X Isolated` |
| `394` | `0xea00...a918` | `SHORT` | 5,680,582.36 USD | `55,151.29` | `89.22` | `103.00` | `242.31` | -759,857.86 USD | `-13.38%` | `20X Cross` |
| `421` | `0x354b...6425` | `SHORT` | 5,269,917.84 USD | `51,154.32` | `102.87` | `103.00` | `310.60` | -7,451.79 USD | `-0.14%` | `8X Cross` |
| `460` | `0x4692...164f` | `SHORT` | 4,788,956.61 USD | `46,485.70` | `103.50` | `103.00` | `1444.84` | 22,548.15 USD | `+0.47%` | `5X Cross` |
| `497` | `0x5989...bc29` | `SHORT` | 4,500,683.97 USD | `43,691.72` | `99.48` | `103.00` | `113.23` | -154,377.07 USD | `-3.43%` | `10X Cross` |
| `546` | `0xd84a...c8a5` | `SHORT` | 4,120,400.00 USD | `40,000.00` | `101.97` | `103.00` | `119.26` | -41,770.00 USD | `-1.01%` | `20X Cross` |
| `551` | `0xd507...c948` | `LONG` | 4,100,275.19 USD | `39,808.50` | `93.57` | `103.00` | `82.63` | 375,199.78 USD | `+9.15%` | `7X Isolated` |
| `705` | `0xb5e7...eff1` | `SHORT` | 3,206,936.99 USD | `31,132.29` | `91.71` | `103.00` | `144.73` | -351,728.34 USD | `-10.97%` | `20X Cross` |
| `743` | `0xbd33...4200` | `SHORT` | 3,088,517.41 USD | `29,982.69` | `104.89` | `103.00` | `403.27` | 56,367.47 USD | `+1.83%` | `20X Cross` |
| `768` | `0xebe1...4070` | `LONG` | 2,987,287.22 USD | `28,999.97` | `101.87` | `103.00` | `0.000000` | 33,020.54 USD | `+1.11%` | `20X Cross` |
| `797` | `0x61d7...7dee` | `LONG` | 2,869,939.92 USD | `27,858.08` | `88.25` | `103.00` | `83.50` | 411,463.92 USD | `+14.34%` | `20X Cross` |
| `879` | `0xf0ae...2f74` | `SHORT` | 2,575,250.00 USD | `25,000.00` | `100.78` | `103.00` | `177.32` | -55,731.39 USD | `-2.16%` | `20X Cross` |
| `894` | `0x645b...87b8` | `SHORT` | 2,533,938.85 USD | `24,596.57` | `101.24` | `103.00` | `134.75` | -43,701.48 USD | `-1.72%` | `3X Isolated` |
| `995` | `0x40f2...6a9e` | `LONG` | 2,238,536.90 USD | `21,733.37` | `103.34` | `103.00` | `100.61` | -7,473.05 USD | `-0.33%` | `20X Cross` |
| `1078` | `0x9aa5...58af` | `SHORT` | 2,026,113.00 USD | `19,671.00` | `101.76` | `103.00` | `567.86` | -24,362.07 USD | `-1.20%` | `20X Cross` |
| `1255` | `0x4169...6f06` | `LONG` | 1,769,216.32 USD | `17,175.19` | `76.61` | `103.00` | `82.98` | 453,448.32 USD | `+25.63%` | `12X Isolated` |
| `1264` | `0x6788...98d4` | `SHORT` | 1,751,170.00 USD | `17,000.00` | `99.31` | `103.00` | `199.43` | -62,845.41 USD | `-3.59%` | `20X Cross` |
| `1310` | `0xa99c...40d5` | `SHORT` | 1,658,461.00 USD | `16,100.00` | `101.02` | `103.00` | `153.62` | -32,003.63 USD | `-1.93%` | `20X Cross` |
| `1319` | `0x1bf6...5bfa` | `SHORT` | 1,648,320.00 USD | `16,000.00` | `99.60` | `103.00` | `228.48` | -54,697.69 USD | `-3.32%` | `20X Cross` |
| `1398` | `0xe5dd...ecba` | `SHORT` | 1,563,498.35 USD | `15,178.12` | `102.71` | `103.00` | `146.16` | -4,560.56 USD | `-0.29%` | `20X Cross` |
| `1413` | `0x5d6f...6f8a` | `LONG` | 1,545,000.00 USD | `15,000.00` | `101.91` | `103.00` | `27.68` | 16,345.00 USD | `+1.06%` | `20X Cross` |
| `1414` | `0x34ea...2f47` | `SHORT` | 1,544,700.00 USD | `15,000.00` | `99.80` | `103.00` | `200.48` | -47,698.69 USD | `-3.09%` | `20X Cross` |
| `1456` | `0xfc27...9d9d` | `LONG` | 1,499,205.38 USD | `14,555.39` | `102.69` | `103.00` | `0.000000` | 4,546.40 USD | `+0.30%` | `20X Cross` |
| `1524` | `0xfb29...21dd` | `LONG` | 1,415,824.14 USD | `13,744.53` | `89.85` | `103.00` | `84.63` | 180,830.18 USD | `+12.77%` | `20X Cross` |
| `1550` | `0x6fa6...825e` | `SHORT` | 1,390,635.00 USD | `13,500.00` | `102.95` | `103.00` | `135.50` | -860.73 USD | `-0.06%` | `20X Isolated` |
| `1565` | `0xa9d9...b48e` | `SHORT` | 1,373,466.63 USD | `13,333.33` | `96.39` | `103.00` | `174.14` | -88,219.45 USD | `-6.42%` | `20X Cross` |
| `1624` | `0x936c...bb0f` | `SHORT` | 1,306,981.40 USD | `12,687.91` | `101.39` | `103.00` | `163.64` | -20,508.53 USD | `-1.57%` | `2X Isolated` |
| `1663` | `0x89c2...c94b` | `LONG` | 1,273,686.82 USD | `12,364.69` | `75.25` | `103.00` | `45.76` | 343,203.67 USD | `+26.95%` | `3X Isolated` |
| `1697` | `0xcd81...36e3` | `SHORT` | 1,242,588.29 USD | `12,063.96` | `97.96` | `103.00` | `108.98` | -60,749.37 USD | `-4.89%` | `20X Cross` |
| `1709` | `0x436c...b3d1` | `SHORT` | 1,236,120.00 USD | `12,000.00` | `101.05` | `103.00` | `208.60` | -23,460.17 USD | `-1.90%` | `20X Cross` |
| `1774` | `0x9dea...d617` | `LONG` | 1,174,396.20 USD | `11,400.80` | `90.37` | `103.00` | `4.87` | 144,122.48 USD | `+12.27%` | `20X Cross` |
| `1790` | `0x17c3...a868` | `LONG` | 1,164,579.49 USD | `11,306.60` | `95.13` | `103.00` | `64.99` | 88,932.62 USD | `+7.64%` | `3X Isolated` |
| `1830` | `0x8607...08d5` | `SHORT` | 1,133,024.47 USD | `10,998.10` | `92.18` | `103.00` | `135.02` | -119,234.76 USD | `-10.52%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.66%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--3.81%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.66%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--3.81%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.68%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--3.85%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.42%`) | Long MP=`99.12` (Vol: 8,700,000.00 USD, Dist: `--3.85%`)
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
  * Current Rate: `-202.75K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
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
| `04:30:00` | `103.69` | `103.69` | `103.69` | `103.69` | `103.34` | 37,328.40 USD | 35,461.98 USD | 1,866.42 USD | 33,595.56 USD | `+90.00%` | `1B / 0S` |
| `04:35:00` | `104.59` | `104.59` | `104.59` | `104.83` | `103.63` | 90,893.05 USD | 76,501.65 USD | 14,391.40 USD | 62,110.25 USD | `+68.33%` | `1B / 0S` |
| `04:40:00` | `105.01` | `105.01` | `105.01` | `105.19` | `104.60` | 125,801.98 USD | 96,201.51 USD | 29,600.47 USD | 66,601.05 USD | `+52.94%` | `1B / 0S` |
| `04:45:00` | `105.45` | `105.45` | `105.45` | `105.56` | `104.97` | 100,810.20 USD | 84,949.97 USD | 15,860.23 USD | 69,089.75 USD | `+68.53%` | `1B / 0S` |
| `04:45:00` | `104.94` | `104.94` | `104.94` | `105.59` | `104.80` | 272,227.33 USD | 86,890.17 USD | 185,337.16 USD | -98,446.99 USD | `-36.16%` | `0B / 1S` |
| `04:50:00` | `105.48` | `105.48` | `105.48` | `105.59` | `105.31` | 91,771.95 USD | 54,646.02 USD | 37,125.93 USD | 17,520.10 USD | `+19.09%` | `1B / 0S` |
| `04:55:00` | `104.94` | `104.94` | `104.94` | `105.53` | `104.80` | 80,597.76 USD | 13,386.96 USD | 67,210.80 USD | -53,823.85 USD | `-66.78%` | `0B / 1S` |
| `05:00:00` | `105.11` | `105.11` | `105.11` | `105.25` | `104.92` | 70,737.01 USD | 47,923.79 USD | 22,813.22 USD | 25,110.57 USD | `+35.50%` | `1B / 0S` |
| `05:00:00` | `103.99` | `103.99` | `103.99` | `105.25` | `103.91` | 505,599.38 USD | 54,292.55 USD | 451,306.83 USD | -397,014.28 USD | `-78.52%` | `0B / 1S` |
| `05:00:00` | `104.77` | `104.77` | `104.77` | `105.25` | `104.75` | 180,408.77 USD | 34,436.74 USD | 145,972.03 USD | -111,535.28 USD | `-61.82%` | `0B / 1S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.60` | `103.57` | `103.60` | `103.66` | `103.45` | 4,757,917.11 USD | 2,812,614.52 USD | 1,945,302.59 USD | 867,311.92 USD | `+18.23%` | `3B / 2S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.23` | 3,756,770.69 USD | 2,127,360.29 USD | 1,629,410.40 USD | 497,949.89 USD | `+13.25%` | `2B / 1S` |
| `0:00 UTC` | `103.25` | `103.28` | `103.25` | `103.37` | `103.23` | 2,263,324.74 USD | 1,120,957.51 USD | 1,142,367.23 USD | -21,409.73 USD | `-0.95%` | `3B / 0S` |
| `5:00 UTC` | `103.00` | `103.14` | `103.00` | `103.50` | `102.94` | 9,234,794.82 USD | 4,542,925.91 USD | 4,691,868.91 USD | -148,943.00 USD | `-1.61%` | `4B / 6S` |
| `0:00 UTC` | `103.15` | `103.11` | `103.15` | `103.19` | `103.05` | 1,706,794.57 USD | 958,339.81 USD | 748,454.76 USD | 209,885.05 USD | `+12.30%` | `1B / 0S` |

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
  * `2026-10-30 09:51:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:39:14 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:40:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `102.60` (Risk Distance: `0.4500` pts)
  * +2.5R Take Profit: `104.18`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.45 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.95` (Risk Distance: `0.4500` pts)
  * +2.5R Take Profit: `103.37`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.45 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.44`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
