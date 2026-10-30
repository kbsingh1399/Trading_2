# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 08:45:54 IST` (`2026-10-30 03:15:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.11` | **Live Ask Quote**: `104.16` | **Mid Price**: `104.13`
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
  * Session VWAP: `104.25` | VWAP Z-Score: `-0.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4069` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.63` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.30` | Lower -3.00σ Band: `102.19`
  * Upper +2.51σ Band: `105.97` | Lower -2.51σ Band: `102.52`
  * Upper +2.01σ Band: `105.63` | Lower -2.01σ Band: `102.87`
  * Upper +2.00σ Band: `105.62` | Lower -2.00σ Band: `102.87`
  * Upper +1.28σ Band: `105.12` | Lower -1.28σ Band: `103.37`
  * Upper +1.00σ Band: `104.93` | Lower -1.00σ Band: `103.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.10` | EMA-20=`103.77` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.17` (Slope: `+0.0000`) | EMA-100=`102.78`
  * Institutional Anchors: EMA-144=`102.62` | EMA-200=`102.42` (Slope: `+0.1891`) | EMA-233=`102.36`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.78` (Distance: `-0.61%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.74%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+1.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.55` | Low=`103.72`
  * New York Session (13:00-21:00 UTC): High=`104.76` | Low=`103.51`
  * Initial Balance (First Hour): IB High=`104.45` | IB Low=`103.82`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.72` - `104.55`
  * Optimal Trade Entry (OTE 0.705): `104.34`
  * Structural Invalidation Anchor (0.786): `104.97`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.36` | `103.48` | `103.36` | `103.48` | `45` | 4,656.60 USD | 4,190.94 USD | `+90.00%` | 175,508.99 USD | `+1.38` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.46` | `103.52` | `103.39` | `103.47` | `109` | 11,278.23 USD | 1,735.11 USD | `+15.38%` | 177,244.10 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.47` | `103.53` | `103.30` | `103.35` | `142` | 14,675.70 USD | -7,816.41 USD | `-53.26%` | 169,427.69 USD | `-2.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.33` | `103.39` | `103.24` | `103.30` | `153` | 15,804.75 USD | -3,055.58 USD | `-19.33%` | 431,082.62 USD | `-0.28` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.30` | `103.48` | `103.30` | `103.48` | `110` | 11,382.80 USD | 10,244.52 USD | `+90.00%` | 441,327.14 USD | `-0.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.46` | `103.53` | `103.27` | `103.32` | `396` | 40,914.72 USD | -23,435.83 USD | `-57.28%` | 417,891.32 USD | `-1.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.47` | `103.54` | `103.22` | `103.45` | `907` | 93,829.15 USD | 17,338.00 USD | `+18.48%` | 312,567.32 USD | `-0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `103.46` | `103.48` | `103.24` | `103.48` | `567` | 58,673.16 USD | 30,533.99 USD | `+52.04%` | 343,101.31 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 211,748.90 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:40:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,107,512.44 USD | `300,817.26` | `98.89` | `103.41` | `31.37` | 1,358,011.41 USD | `+4.37%` | `3X Cross` |
| `108` | `0x30af...393e` | `LONG` | 18,377,243.11 USD | `177,712.44` | `100.98` | `103.41` | `93.19` | 431,841.22 USD | `+2.35%` | `10X Isolated` |
| `289` | `0x7fda...17d1` | `SHORT` | 8,132,159.67 USD | `78,647.58` | `100.15` | `103.41` | `211.25` | -255,537.82 USD | `-3.14%` | `20X Cross` |
| `325` | `0x10e1...f4bd` | `LONG` | 6,992,515.68 USD | `67,625.88` | `84.36` | `103.41` | `58.53` | 1,287,285.30 USD | `+18.41%` | `3X Isolated` |
| `394` | `0xea00...a918` | `SHORT` | 5,703,194.38 USD | `55,151.29` | `89.22` | `103.41` | `227.92` | -782,469.89 USD | `-13.72%` | `20X Cross` |
| `455` | `0x4692...164f` | `SHORT` | 4,728,630.31 USD | `45,727.01` | `103.67` | `103.41` | `1481.29` | 12,040.03 USD | `+0.25%` | `5X Cross` |
| `482` | `0x5989...bc29` | `SHORT` | 4,518,160.66 USD | `43,691.72` | `99.48` | `103.41` | `113.23` | -171,853.76 USD | `-3.80%` | `10X Cross` |
| `527` | `0xd84a...c8a5` | `SHORT` | 4,136,400.00 USD | `40,000.00` | `101.97` | `103.41` | `119.12` | -57,770.00 USD | `-1.40%` | `20X Cross` |
| `528` | `0xebe1...4070` | `LONG` | 4,136,397.10 USD | `39,999.97` | `101.87` | `103.41` | `0.000000` | 61,545.58 USD | `+1.49%` | `20X Cross` |
| `531` | `0xd507...c948` | `LONG` | 4,116,198.59 USD | `39,808.50` | `93.57` | `103.41` | `81.34` | 391,123.18 USD | `+9.50%` | `7X Isolated` |
| `577` | `0x354b...6425` | `SHORT` | 3,867,833.68 USD | `37,402.90` | `102.68` | `103.41` | `390.93` | -27,350.53 USD | `-0.71%` | `8X Cross` |
| `684` | `0xb5e7...eff1` | `SHORT` | 3,219,389.90 USD | `31,132.29` | `91.71` | `103.41` | `144.40` | -364,181.26 USD | `-11.31%` | `20X Cross` |
| `720` | `0xbd33...4200` | `SHORT` | 3,100,510.49 USD | `29,982.69` | `104.89` | `103.41` | `403.27` | 44,374.39 USD | `+1.43%` | `20X Cross` |
| `787` | `0x61d7...7dee` | `LONG` | 2,880,804.57 USD | `27,858.08` | `88.25` | `103.41` | `83.50` | 422,328.57 USD | `+14.66%` | `20X Cross` |
| `872` | `0xf0ae...2f74` | `SHORT` | 2,585,250.00 USD | `25,000.00` | `100.78` | `103.41` | `176.90` | -65,731.39 USD | `-2.54%` | `20X Cross` |
| `891` | `0x645b...87b8` | `SHORT` | 2,526,560.90 USD | `24,432.46` | `101.23` | `103.41` | `134.76` | -53,212.39 USD | `-2.11%` | `3X Isolated` |
| `952` | `0x58f0...0d20` | `SHORT` | 2,327,918.97 USD | `22,511.55` | `96.77` | `103.41` | `107.94` | -149,501.18 USD | `-6.42%` | `20X Cross` |
| `1059` | `0x9aa5...58af` | `SHORT` | 2,033,981.40 USD | `19,671.00` | `101.76` | `103.41` | `581.73` | -32,230.47 USD | `-1.58%` | `20X Cross` |
| `1230` | `0x4169...6f06` | `LONG` | 1,776,086.40 USD | `17,175.19` | `76.61` | `103.41` | `82.98` | 460,318.40 USD | `+25.92%` | `12X Isolated` |
| `1240` | `0x6788...98d4` | `SHORT` | 1,757,970.00 USD | `17,000.00` | `99.31` | `103.41` | `202.16` | -69,645.41 USD | `-3.96%` | `20X Cross` |
| `1294` | `0xa99c...40d5` | `SHORT` | 1,664,901.00 USD | `16,100.00` | `101.02` | `103.41` | `151.78` | -38,443.63 USD | `-2.31%` | `20X Cross` |
| `1300` | `0x1bf6...5bfa` | `SHORT` | 1,654,560.00 USD | `16,000.00` | `99.60` | `103.41` | `227.24` | -60,937.69 USD | `-3.68%` | `20X Cross` |
| `1329` | `0xe5dd...ecba` | `SHORT` | 1,610,665.56 USD | `15,575.53` | `102.71` | `103.41` | `144.83` | -10,910.18 USD | `-0.68%` | `20X Cross` |
| `1377` | `0x34ea...2f47` | `SHORT` | 1,551,150.00 USD | `15,000.00` | `99.80` | `103.41` | `201.88` | -54,148.69 USD | `-3.49%` | `20X Cross` |
| `1378` | `0x5d6f...6f8a` | `LONG` | 1,551,150.00 USD | `15,000.00` | `101.91` | `103.41` | `27.06` | 22,495.00 USD | `+1.45%` | `20X Cross` |
| `1457` | `0xfc27...9d9d` | `LONG` | 1,477,252.39 USD | `14,285.39` | `102.69` | `103.41` | `0.000000` | 10,352.11 USD | `+0.70%` | `20X Cross` |
| `1509` | `0xfb29...21dd` | `LONG` | 1,422,421.51 USD | `13,744.53` | `89.85` | `103.41` | `84.72` | 187,427.55 USD | `+13.18%` | `20X Cross` |
| `1533` | `0x6fa6...825e` | `SHORT` | 1,396,035.00 USD | `13,500.00` | `102.95` | `103.41` | `135.50` | -6,260.73 USD | `-0.45%` | `20X Isolated` |
| `1546` | `0xa9d9...b48e` | `SHORT` | 1,378,799.97 USD | `13,333.33` | `96.39` | `103.41` | `173.78` | -93,552.78 USD | `-6.79%` | `20X Cross` |
| `1599` | `0x936c...bb0f` | `SHORT` | 1,312,056.57 USD | `12,687.91` | `101.39` | `103.41` | `163.64` | -25,583.70 USD | `-1.95%` | `2X Isolated` |
| `1630` | `0x89c2...c94b` | `LONG` | 1,278,632.70 USD | `12,364.69` | `75.25` | `103.41` | `45.76` | 348,149.54 USD | `+27.23%` | `3X Isolated` |
| `1668` | `0xcd81...36e3` | `SHORT` | 1,247,534.52 USD | `12,063.96` | `97.96` | `103.41` | `108.76` | -65,695.60 USD | `-5.27%` | `20X Cross` |
| `1675` | `0x436c...b3d1` | `SHORT` | 1,240,920.00 USD | `12,000.00` | `101.05` | `103.41` | `210.73` | -28,260.17 USD | `-2.28%` | `20X Cross` |
| `1739` | `0x9dea...d617` | `LONG` | 1,178,842.51 USD | `11,400.80` | `90.37` | `103.41` | `7.67` | 148,568.79 USD | `+12.60%` | `20X Cross` |
| `1750` | `0x17c3...a868` | `LONG` | 1,169,215.20 USD | `11,306.60` | `95.13` | `103.41` | `64.99` | 93,568.33 USD | `+8.00%` | `3X Isolated` |
| `1793` | `0x0242...ffa1` | `LONG` | 1,137,669.98 USD | `11,001.55` | `104.43` | `103.41` | `0.000000` | -11,273.55 USD | `-0.99%` | `10X Cross` |
| `1794` | `0x8607...08d5` | `SHORT` | 1,137,313.73 USD | `10,998.10` | `92.18` | `103.41` | `135.02` | -123,524.02 USD | `-10.86%` | `4X Isolated` |
| `1896` | `0xb078...de15` | `LONG` | 1,051,159.13 USD | `10,164.97` | `104.67` | `103.41` | `0.000000` | -12,778.30 USD | `-1.22%` | `5X Cross` |

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
| `Envelope` | `Long Liquidation` | `103.09` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.17` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-139.71K` | Last 24h: `-366.73K` | Last 3d: `-686.90K` | Last 7d: `-1.13M`
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
| `02:20:00` | `103.36` | `103.36` | `103.36` | `103.36` | `103.33` | 3,514.07 USD | 2,008.04 USD | 1,506.03 USD | 502.01 USD | `+14.29%` | `1B / 0S` |
| `02:25:00` | `103.33` | `103.33` | `103.33` | `103.38` | `103.31` | 5,993.14 USD | 1,926.37 USD | 4,066.77 USD | -2,140.41 USD | `-35.71%` | `0B / 1S` |
| `02:30:00` | `103.30` | `103.30` | `103.30` | `103.39` | `103.24` | 15,804.75 USD | 6,374.58 USD | 9,430.17 USD | -3,055.58 USD | `-19.33%` | `0B / 1S` |
| `02:30:00` | `103.34` | `103.34` | `103.34` | `103.35` | `103.32` | 1,550.17 USD | 1,291.81 USD | 258.36 USD | 1,033.45 USD | `+66.67%` | `1B / 0S` |
| `02:35:00` | `103.37` | `103.37` | `103.37` | `103.39` | `103.34` | 2,894.36 USD | 2,026.05 USD | 868.31 USD | 1,157.74 USD | `+40.00%` | `1B / 0S` |
| `02:40:00` | `103.30` | `103.30` | `103.30` | `103.38` | `103.24` | 11,362.89 USD | 3,724.50 USD | 7,638.39 USD | -3,913.88 USD | `-34.44%` | `0B / 1S` |
| `02:45:00` | `103.36` | `103.36` | `103.36` | `103.38` | `103.30` | 4,754.56 USD | 4,001.20 USD | 753.36 USD | 3,247.83 USD | `+68.31%` | `1B / 0S` |
| `02:45:00` | `103.48` | `103.48` | `103.48` | `103.48` | `103.30` | 11,382.80 USD | 10,813.66 USD | 569.14 USD | 10,244.52 USD | `+90.00%` | `1B / 0S` |
| `02:50:00` | `103.37` | `103.37` | `103.37` | `103.40` | `103.36` | 1,964.03 USD | 797.89 USD | 1,166.14 USD | -368.26 USD | `-18.75%` | `0B / 1S` |
| `02:55:00` | `103.48` | `103.48` | `103.48` | `103.48` | `103.36` | 4,656.60 USD | 4,423.77 USD | 232.83 USD | 4,190.94 USD | `+90.00%` | `1B / 0S` |
| `5:00 UTC` | `102.85` | `102.74` | `102.85` | `102.88` | `102.57` | 8,986,938.51 USD | 2,421,078.21 USD | 6,565,860.30 USD | -4,144,782.09 USD | `-46.12%` | `3B / 14S` |
| `0:00 UTC` | `102.78` | `102.78` | `102.78` | `103.02` | `102.57` | 31,355,759.70 USD | 14,370,056.44 USD | 16,985,703.26 USD | -2,615,646.82 USD | `-8.34%` | `6B / 5S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.81` | 12,332,708.79 USD | 3,885,730.79 USD | 8,446,978.00 USD | -4,561,247.21 USD | `-36.98%` | `0B / 5S` |
| `0:00 UTC` | `104.23` | `103.97` | `104.23` | `104.72` | `102.88` | 80,432,525.97 USD | 47,963,579.07 USD | 32,468,946.89 USD | 15,494,632.18 USD | `+19.26%` | `55B / 11S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.52` | `103.54` | `103.52` | `103.62` | `103.45` | 2,773,763.98 USD | 1,503,397.33 USD | 1,270,366.66 USD | 233,030.67 USD | `+8.40%` | `0B / 2S` |

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
  * `2026-10-30 08:34:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:38 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:35:38 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:36:38 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:36:38 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `102.50` (Risk Distance: `0.5572` pts)
  * +2.5R Take Profit: `104.45`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.78` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.34` (Risk Distance: `0.5572` pts)
  * +2.5R Take Profit: `103.39`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.56 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.97`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
