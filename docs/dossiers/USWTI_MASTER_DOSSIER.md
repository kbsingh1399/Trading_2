# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 08:33:46 IST` (`2026-10-30 03:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.03` | **Live Ask Quote**: `104.08` | **Mid Price**: `104.05`
- **Spread Points**: `46.00` | **Spread BPS**: `4.42 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.26` | VWAP Z-Score: `-0.19` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4166` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.16` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.38` | Lower -3.00σ Band: `102.14`
  * Upper +2.51σ Band: `106.03` | Lower -2.51σ Band: `102.49`
  * Upper +2.01σ Band: `105.68` | Lower -2.01σ Band: `102.84`
  * Upper +2.00σ Band: `105.67` | Lower -2.00σ Band: `102.85`
  * Upper +1.28σ Band: `105.17` | Lower -1.28σ Band: `103.36`
  * Upper +1.00σ Band: `104.97` | Lower -1.00σ Band: `103.55`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.13` | EMA-20=`103.75` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.13` (Slope: `+0.0000`) | EMA-100=`102.76`
  * Institutional Anchors: EMA-144=`102.60` | EMA-200=`102.40` (Slope: `+0.1858`) | EMA-233=`102.35`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.82` (Distance: `-0.72%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.66%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.98%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.15` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.47` | Low=`103.64`
  * New York Session (13:00-21:00 UTC): High=`104.68` | Low=`103.43`
  * Initial Balance (First Hour): IB High=`104.37` | IB Low=`103.74`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.64` - `104.47`
  * Optimal Trade Entry (OTE 0.705): `104.26`
  * Structural Invalidation Anchor (0.786): `104.89`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.33` | `103.35` | `103.32` | `103.34` | `15` | 1,550.17 USD | 1,033.45 USD | `+66.67%` | 186,373.41 USD | `+0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.34` | `103.39` | `103.34` | `103.37` | `28` | 2,894.36 USD | 1,157.74 USD | `+40.00%` | 187,531.16 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.38` | `103.38` | `103.24` | `103.30` | `110` | 11,362.89 USD | -3,913.88 USD | `-34.44%` | 183,617.27 USD | `-1.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.46` | `103.46` | `103.28` | `103.38` | `164` | 16,954.32 USD | -2,825.72 USD | `-16.67%` | 461,498.70 USD | `-0.40` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.39` | `103.44` | `103.31` | `103.33` | `140` | 14,466.20 USD | -8,390.40 USD | `-58.00%` | 453,108.31 USD | `-0.47` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.33` | `103.39` | `103.24` | `103.30` | `153` | 15,804.75 USD | -3,055.58 USD | `-19.33%` | 450,052.72 USD | `-0.28` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:26:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `38` | `0x0cc1...c7cb` | `LONG` | 31,089,463.41 USD | `300,817.26` | `98.89` | `103.37` | `31.37` | 1,339,962.38 USD | `+4.31%` | `3X Cross` |
| `107` | `0x30af...393e` | `LONG` | 18,361,248.99 USD | `177,712.44` | `100.98` | `103.37` | `93.19` | 415,847.10 USD | `+2.26%` | `10X Isolated` |
| `287` | `0x7fda...17d1` | `SHORT` | 8,125,867.86 USD | `78,647.58` | `100.15` | `103.37` | `211.68` | -249,246.01 USD | `-3.07%` | `20X Cross` |
| `327` | `0x10e1...f4bd` | `LONG` | 6,987,105.61 USD | `67,625.88` | `84.36` | `103.37` | `58.53` | 1,281,875.23 USD | `+18.35%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,698,782.28 USD | `55,151.29` | `89.22` | `103.37` | `224.81` | -778,057.79 USD | `-13.65%` | `20X Cross` |
| `465` | `0x4692...164f` | `SHORT` | 4,637,638.46 USD | `44,881.82` | `103.69` | `103.37` | `1507.45` | 16,276.78 USD | `+0.35%` | `5X Cross` |
| `482` | `0x5989...bc29` | `SHORT` | 4,511,606.90 USD | `43,691.72` | `99.48` | `103.37` | `113.23` | -165,300.00 USD | `-3.66%` | `10X Cross` |
| `531` | `0xebe1...4070` | `LONG` | 4,133,197.11 USD | `39,999.97` | `101.87` | `103.37` | `0.000000` | 58,345.58 USD | `+1.41%` | `20X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,132,800.00 USD | `40,000.00` | `101.97` | `103.37` | `119.13` | -54,170.00 USD | `-1.31%` | `20X Cross` |
| `534` | `0xd507...c948` | `LONG` | 4,113,412.00 USD | `39,808.50` | `93.57` | `103.37` | `81.34` | 388,336.58 USD | `+9.44%` | `7X Isolated` |
| `579` | `0x354b...6425` | `SHORT` | 3,864,841.45 USD | `37,402.90` | `102.68` | `103.37` | `390.85` | -24,358.29 USD | `-0.63%` | `8X Cross` |
| `685` | `0xb5e7...eff1` | `SHORT` | 3,216,588.00 USD | `31,132.29` | `91.71` | `103.37` | `144.49` | -361,379.35 USD | `-11.23%` | `20X Cross` |
| `720` | `0xbd33...4200` | `SHORT` | 3,097,212.39 USD | `29,982.69` | `104.89` | `103.37` | `403.27` | 47,672.49 USD | `+1.54%` | `20X Cross` |
| `787` | `0x61d7...7dee` | `LONG` | 2,876,904.44 USD | `27,858.08` | `88.25` | `103.37` | `83.50` | 418,428.44 USD | `+14.54%` | `20X Cross` |
| `870` | `0xf0ae...2f74` | `SHORT` | 2,582,500.00 USD | `25,000.00` | `100.78` | `103.37` | `177.28` | -62,981.39 USD | `-2.44%` | `20X Cross` |
| `888` | `0x645b...87b8` | `SHORT` | 2,524,606.30 USD | `24,432.46` | `101.23` | `103.37` | `134.76` | -51,257.79 USD | `-2.03%` | `3X Isolated` |
| `951` | `0x58f0...0d20` | `SHORT` | 2,324,542.24 USD | `22,511.55` | `96.77` | `103.37` | `107.05` | -146,124.45 USD | `-6.29%` | `20X Cross` |
| `1056` | `0x9aa5...58af` | `SHORT` | 2,032,407.72 USD | `19,671.00` | `101.76` | `103.37` | `588.23` | -30,656.79 USD | `-1.51%` | `20X Cross` |
| `1227` | `0x4169...6f06` | `LONG` | 1,774,540.63 USD | `17,175.19` | `76.61` | `103.37` | `82.98` | 458,772.63 USD | `+25.85%` | `12X Isolated` |
| `1241` | `0x6788...98d4` | `SHORT` | 1,756,950.00 USD | `17,000.00` | `99.31` | `103.37` | `202.00` | -68,625.41 USD | `-3.91%` | `20X Cross` |
| `1290` | `0xa99c...40d5` | `SHORT` | 1,663,935.00 USD | `16,100.00` | `101.02` | `103.37` | `152.09` | -37,477.63 USD | `-2.25%` | `20X Cross` |
| `1296` | `0x1bf6...5bfa` | `SHORT` | 1,653,280.00 USD | `16,000.00` | `99.60` | `103.37` | `227.63` | -59,657.69 USD | `-3.61%` | `20X Cross` |
| `1327` | `0xe5dd...ecba` | `SHORT` | 1,609,263.76 USD | `15,575.53` | `102.71` | `103.37` | `144.77` | -9,508.38 USD | `-0.59%` | `20X Cross` |
| `1374` | `0x5d6f...6f8a` | `LONG` | 1,549,800.00 USD | `15,000.00` | `101.91` | `103.37` | `27.10` | 21,145.00 USD | `+1.36%` | `20X Cross` |
| `1375` | `0x34ea...2f47` | `SHORT` | 1,548,900.00 USD | `15,000.00` | `99.80` | `103.37` | `202.30` | -51,898.69 USD | `-3.35%` | `20X Cross` |
| `1451` | `0xfc27...9d9d` | `LONG` | 1,476,109.56 USD | `14,285.39` | `102.69` | `103.37` | `0.000000` | 9,209.28 USD | `+0.62%` | `20X Cross` |
| `1500` | `0xfb29...21dd` | `LONG` | 1,420,359.83 USD | `13,744.53` | `89.85` | `103.37` | `84.73` | 185,365.87 USD | `+13.05%` | `20X Cross` |
| `1526` | `0x6fa6...825e` | `SHORT` | 1,394,955.00 USD | `13,500.00` | `102.95` | `103.37` | `135.50` | -5,180.73 USD | `-0.37%` | `20X Isolated` |
| `1541` | `0xa9d9...b48e` | `SHORT` | 1,377,599.97 USD | `13,333.33` | `96.39` | `103.37` | `173.60` | -92,352.78 USD | `-6.70%` | `20X Cross` |
| `1596` | `0x936c...bb0f` | `SHORT` | 1,311,041.53 USD | `12,687.91` | `101.39` | `103.37` | `163.64` | -24,568.66 USD | `-1.87%` | `2X Isolated` |
| `1628` | `0x89c2...c94b` | `LONG` | 1,276,901.64 USD | `12,364.69` | `75.25` | `103.37` | `45.76` | 346,418.49 USD | `+27.13%` | `3X Isolated` |
| `1661` | `0xcd81...36e3` | `SHORT` | 1,246,569.40 USD | `12,063.96` | `97.96` | `103.37` | `108.82` | -64,730.48 USD | `-5.19%` | `20X Cross` |
| `1670` | `0x436c...b3d1` | `SHORT` | 1,239,120.00 USD | `12,000.00` | `101.05` | `103.37` | `211.21` | -26,460.17 USD | `-2.14%` | `20X Cross` |
| `1737` | `0x9dea...d617` | `LONG` | 1,177,588.43 USD | `11,400.80` | `90.37` | `103.37` | `7.37` | 147,314.70 USD | `+12.51%` | `20X Cross` |
| `1746` | `0x17c3...a868` | `LONG` | 1,168,310.67 USD | `11,306.60` | `95.13` | `103.37` | `64.99` | 92,663.80 USD | `+7.93%` | `3X Isolated` |
| `1787` | `0x0242...ffa1` | `LONG` | 1,136,789.85 USD | `11,001.55` | `104.43` | `103.37` | `0.000000` | -12,153.68 USD | `-1.07%` | `10X Cross` |
| `1789` | `0x8607...08d5` | `SHORT` | 1,135,993.96 USD | `10,998.10` | `92.18` | `103.37` | `135.02` | -122,204.25 USD | `-10.76%` | `4X Isolated` |
| `1891` | `0xb078...de15` | `LONG` | 1,050,345.94 USD | `10,164.97` | `104.67` | `103.37` | `0.000000` | -13,591.50 USD | `-1.29%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `Envelope` | `Long Liquidation` | `103.23` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.33` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-141.85K` | Last 24h: `-366.73K` | Last 3d: `-686.90K` | Last 7d: `-1.13M`
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
| `02:05:00` | `103.38` | `103.38` | `103.38` | `103.44` | `103.28` | 7,856.50 USD | 3,498.60 USD | 4,357.90 USD | -859.30 USD | `-10.94%` | `0B / 1S` |
| `02:10:00` | `103.38` | `103.38` | `103.38` | `103.40` | `103.36` | 2,687.88 USD | 1,567.93 USD | 1,119.95 USD | 447.98 USD | `+16.67%` | `1B / 0S` |
| `02:15:00` | `103.33` | `103.33` | `103.33` | `103.44` | `103.31` | 14,466.20 USD | 3,037.90 USD | 11,428.30 USD | -8,390.40 USD | `-58.00%` | `0B / 1S` |
| `02:15:00` | `103.37` | `103.37` | `103.37` | `103.44` | `103.37` | 4,961.76 USD | 858.77 USD | 4,102.99 USD | -3,244.23 USD | `-65.38%` | `0B / 1S` |
| `02:20:00` | `103.36` | `103.36` | `103.36` | `103.36` | `103.33` | 3,514.07 USD | 2,008.04 USD | 1,506.03 USD | 502.01 USD | `+14.29%` | `1B / 0S` |
| `02:25:00` | `103.33` | `103.33` | `103.33` | `103.38` | `103.31` | 5,993.14 USD | 1,926.37 USD | 4,066.77 USD | -2,140.41 USD | `-35.71%` | `0B / 1S` |
| `02:30:00` | `103.34` | `103.34` | `103.34` | `103.35` | `103.32` | 1,550.17 USD | 1,291.81 USD | 258.36 USD | 1,033.45 USD | `+66.67%` | `1B / 0S` |
| `02:30:00` | `103.30` | `103.30` | `103.30` | `103.39` | `103.24` | 15,804.75 USD | 6,374.58 USD | 9,430.17 USD | -3,055.58 USD | `-19.33%` | `0B / 1S` |
| `02:35:00` | `103.37` | `103.37` | `103.37` | `103.39` | `103.34` | 2,894.36 USD | 2,026.05 USD | 868.31 USD | 1,157.74 USD | `+40.00%` | `1B / 0S` |
| `02:40:00` | `103.30` | `103.30` | `103.30` | `103.38` | `103.24` | 11,362.89 USD | 3,724.50 USD | 7,638.39 USD | -3,913.88 USD | `-34.44%` | `0B / 1S` |
| `0:00 UTC` | `102.80` | `102.83` | `102.80` | `102.93` | `102.75` | 11,683,758.36 USD | 3,517,048.40 USD | 8,166,709.96 USD | -4,649,661.56 USD | `-39.80%` | `1B / 5S` |
| `5:00 UTC` | `102.85` | `102.74` | `102.85` | `102.88` | `102.57` | 8,986,938.51 USD | 2,421,078.21 USD | 6,565,860.30 USD | -4,144,782.09 USD | `-46.12%` | `3B / 14S` |
| `0:00 UTC` | `102.78` | `102.78` | `102.78` | `103.02` | `102.57` | 31,355,759.70 USD | 14,370,056.44 USD | 16,985,703.26 USD | -2,615,646.82 USD | `-8.34%` | `6B / 5S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.81` | 12,332,708.79 USD | 3,885,730.79 USD | 8,446,978.00 USD | -4,561,247.21 USD | `-36.98%` | `0B / 5S` |
| `0:00 UTC` | `104.23` | `103.97` | `104.23` | `104.72` | `102.88` | 80,432,525.97 USD | 47,963,579.07 USD | 32,468,946.89 USD | 15,494,632.18 USD | `+19.26%` | `55B / 11S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.65` | `103.62` | `103.65` | `103.72` | `103.48` | 5,449,528.92 USD | 2,343,189.44 USD | 3,106,339.47 USD | -763,150.03 USD | `-14.00%` | `2B / 3S` |

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
  * `2026-10-30 08:00:51 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:21:51 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:51 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:22:51 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:22:51 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:22:51 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:22:51 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `102.48` (Risk Distance: `0.5689` pts)
  * +2.5R Take Profit: `104.48`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.82` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.39` (Risk Distance: `0.5689` pts)
  * +2.5R Take Profit: `103.40`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.57 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
