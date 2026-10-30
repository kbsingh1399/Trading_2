# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 09:13:07 IST` (`2026-10-30 03:43:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.03` | **Live Ask Quote**: `104.08` | **Mid Price**: `104.06`
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
  * Session VWAP: `104.06` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.79` | Lower -3.00σ Band: `103.33`
  * Upper +2.51σ Band: `104.63` | Lower -2.51σ Band: `103.49`
  * Upper +2.01σ Band: `104.50` | Lower -2.01σ Band: `103.62`
  * Upper +2.00σ Band: `104.47` | Lower -2.00σ Band: `103.64`
  * Upper +1.28σ Band: `104.35` | Lower -1.28σ Band: `103.77`
  * Upper +1.00σ Band: `104.27` | Lower -1.00σ Band: `103.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.06` | EMA-20=`104.06` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`104.06` (Slope: `+0.0000`) | EMA-100=`104.06`
  * Institutional Anchors: EMA-144=`104.06` | EMA-200=`104.06` (Slope: `+0.0000`) | EMA-233=`104.06`
- **Range Boundaries**: 24H High=`105.10` | 24H Low=`103.02` | Weekly High=`106.14` | Weekly Low=`101.98`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.75` (Distance: `-0.66%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.66%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.98%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.47` | Low=`103.64`
  * New York Session (13:00-21:00 UTC): High=`104.68` | Low=`103.43`
  * Initial Balance (First Hour): IB High=`104.37` | IB Low=`103.75`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.64` - `104.47`
  * Optimal Trade Entry (OTE 0.705): `104.27`
  * Structural Invalidation Anchor (0.786): `104.89`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:07:15 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 31,119,545.13 USD | `300,817.26` | `98.89` | `103.46` | `31.37` | 1,370,044.10 USD | `+4.40%` | `3X Cross` |
| `110` | `0x30af...393e` | `LONG` | 18,389,682.98 USD | `177,712.44` | `100.98` | `103.46` | `93.19` | 444,281.09 USD | `+2.42%` | `10X Isolated` |
| `284` | `0x7fda...17d1` | `SHORT` | 8,138,451.47 USD | `78,647.58` | `100.15` | `103.46` | `213.07` | -261,829.63 USD | `-3.22%` | `20X Cross` |
| `324` | `0x10e1...f4bd` | `LONG` | 6,997,925.75 USD | `67,625.88` | `84.36` | `103.46` | `58.53` | 1,292,695.37 USD | `+18.47%` | `3X Isolated` |
| `390` | `0xea00...a918` | `SHORT` | 5,704,297.41 USD | `55,151.29` | `89.22` | `103.46` | `236.10` | -783,572.91 USD | `-13.74%` | `20X Cross` |
| `410` | `0x354b...6425` | `SHORT` | 5,370,946.99 USD | `51,898.22` | `102.87` | `103.46` | `309.18` | -32,036.39 USD | `-0.60%` | `8X Cross` |
| `454` | `0x4692...164f` | `SHORT` | 4,849,032.34 USD | `46,859.61` | `103.62` | `103.46` | `1442.71` | 6,534.09 USD | `+0.13%` | `5X Cross` |
| `490` | `0x5989...bc29` | `SHORT` | 4,520,782.16 USD | `43,691.72` | `99.48` | `103.46` | `113.23` | -174,475.26 USD | `-3.86%` | `10X Cross` |
| `536` | `0xd84a...c8a5` | `SHORT` | 4,139,600.00 USD | `40,000.00` | `101.97` | `103.46` | `119.11` | -60,970.00 USD | `-1.47%` | `20X Cross` |
| `540` | `0xd507...c948` | `LONG` | 4,119,383.27 USD | `39,808.50` | `93.57` | `103.46` | `82.63` | 394,307.86 USD | `+9.57%` | `7X Isolated` |
| `645` | `0xebe1...4070` | `LONG` | 3,415,137.81 USD | `32,999.69` | `101.87` | `103.46` | `0.000000` | 53,414.63 USD | `+1.56%` | `20X Cross` |
| `690` | `0xb5e7...eff1` | `SHORT` | 3,221,880.49 USD | `31,132.29` | `91.71` | `103.46` | `144.58` | -366,671.84 USD | `-11.38%` | `20X Cross` |
| `727` | `0xbd33...4200` | `SHORT` | 3,102,909.11 USD | `29,982.69` | `104.89` | `103.46` | `403.27` | 41,975.77 USD | `+1.35%` | `20X Cross` |
| `780` | `0x61d7...7dee` | `LONG` | 2,882,754.64 USD | `27,858.08` | `88.25` | `103.46` | `83.50` | 424,278.63 USD | `+14.72%` | `20X Cross` |
| `880` | `0xf0ae...2f74` | `SHORT` | 2,587,000.00 USD | `25,000.00` | `100.78` | `103.46` | `176.48` | -67,481.39 USD | `-2.61%` | `20X Cross` |
| `897` | `0x645b...87b8` | `SHORT` | 2,530,270.40 USD | `24,451.78` | `101.23` | `103.46` | `134.76` | -54,926.14 USD | `-2.17%` | `3X Isolated` |
| `983` | `0x40f2...6a9e` | `LONG` | 2,248,968.92 USD | `21,733.37` | `103.34` | `103.46` | `100.58` | 2,958.96 USD | `+0.13%` | `20X Cross` |
| `1066` | `0x9aa5...58af` | `SHORT` | 2,035,555.08 USD | `19,671.00` | `101.76` | `103.46` | `572.23` | -33,804.15 USD | `-1.66%` | `20X Cross` |
| `1239` | `0x4169...6f06` | `LONG` | 1,777,288.66 USD | `17,175.19` | `76.61` | `103.46` | `82.98` | 461,520.66 USD | `+25.97%` | `12X Isolated` |
| `1252` | `0x6788...98d4` | `SHORT` | 1,758,990.00 USD | `17,000.00` | `99.31` | `103.46` | `200.89` | -70,665.41 USD | `-4.02%` | `20X Cross` |
| `1293` | `0xa99c...40d5` | `SHORT` | 1,665,545.00 USD | `16,100.00` | `101.02` | `103.46` | `152.94` | -39,087.63 USD | `-2.35%` | `20X Cross` |
| `1300` | `0x1bf6...5bfa` | `SHORT` | 1,655,680.00 USD | `16,000.00` | `99.60` | `103.46` | `226.99` | -62,057.69 USD | `-3.75%` | `20X Cross` |
| `1338` | `0xe5dd...ecba` | `SHORT` | 1,611,755.84 USD | `15,575.53` | `102.71` | `103.46` | `144.88` | -12,000.47 USD | `-0.74%` | `20X Cross` |
| `1397` | `0x5d6f...6f8a` | `LONG` | 1,552,200.00 USD | `15,000.00` | `101.91` | `103.46` | `26.99` | 23,545.00 USD | `+1.52%` | `20X Cross` |
| `1398` | `0x34ea...2f47` | `SHORT` | 1,551,600.00 USD | `15,000.00` | `99.80` | `103.46` | `200.88` | -54,598.69 USD | `-3.52%` | `20X Cross` |
| `1458` | `0xfc27...9d9d` | `LONG` | 1,478,395.22 USD | `14,285.39` | `102.69` | `103.46` | `0.000000` | 11,494.94 USD | `+0.78%` | `20X Cross` |
| `1515` | `0xfb29...21dd` | `LONG` | 1,421,596.84 USD | `13,744.53` | `89.85` | `103.46` | `84.66` | 186,602.88 USD | `+13.13%` | `20X Cross` |
| `1542` | `0x6fa6...825e` | `SHORT` | 1,396,980.00 USD | `13,500.00` | `102.95` | `103.46` | `135.50` | -7,205.73 USD | `-0.52%` | `20X Isolated` |
| `1554` | `0xa9d9...b48e` | `SHORT` | 1,379,866.63 USD | `13,333.33` | `96.39` | `103.46` | `173.90` | -94,619.45 USD | `-6.86%` | `20X Cross` |
| `1612` | `0x936c...bb0f` | `SHORT` | 1,312,817.84 USD | `12,687.91` | `101.39` | `103.46` | `163.64` | -26,344.97 USD | `-2.01%` | `2X Isolated` |
| `1652` | `0x89c2...c94b` | `LONG` | 1,279,127.28 USD | `12,364.69` | `75.25` | `103.46` | `45.76` | 348,644.13 USD | `+27.26%` | `3X Isolated` |
| `1682` | `0xcd81...36e3` | `SHORT` | 1,247,655.16 USD | `12,063.96` | `97.96` | `103.46` | `108.93` | -65,816.24 USD | `-5.28%` | `20X Cross` |
| `1689` | `0x436c...b3d1` | `SHORT` | 1,241,640.00 USD | `12,000.00` | `101.05` | `103.46` | `209.50` | -28,980.17 USD | `-2.33%` | `20X Cross` |
| `1759` | `0x9dea...d617` | `LONG` | 1,179,754.58 USD | `11,400.80` | `90.37` | `103.46` | `6.79` | 149,480.85 USD | `+12.67%` | `20X Cross` |
| `1769` | `0x17c3...a868` | `LONG` | 1,169,328.26 USD | `11,306.60` | `95.13` | `103.46` | `64.99` | 93,681.39 USD | `+8.01%` | `3X Isolated` |
| `1811` | `0x8607...08d5` | `SHORT` | 1,138,083.59 USD | `10,998.10` | `92.18` | `103.46` | `135.02` | -124,293.89 USD | `-10.92%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.26%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.19%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.26%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.19%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.28%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.23%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.01%`) | Long MP=`99.21` (Vol: 8,800,000.00 USD, Dist: `--4.14%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.05` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.01` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-160.91K` | Last 24h: `-366.73K` | Last 3d: `-686.90K` | Last 7d: `-1.13M`
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
| `02:50:00` | `103.37` | `103.37` | `103.37` | `103.40` | `103.36` | 1,964.03 USD | 797.89 USD | 1,166.14 USD | -368.26 USD | `-18.75%` | `0B / 1S` |
| `02:55:00` | `103.48` | `103.48` | `103.48` | `103.48` | `103.36` | 4,656.60 USD | 4,423.77 USD | 232.83 USD | 4,190.94 USD | `+90.00%` | `1B / 0S` |
| `03:00:00` | `103.07` | `103.07` | `103.07` | `103.53` | `103.06` | 145,947.12 USD | 7,297.36 USD | 138,649.76 USD | -131,352.41 USD | `-90.00%` | `0B / 1S` |
| `03:00:00` | `103.47` | `103.47` | `103.47` | `103.52` | `103.39` | 11,278.23 USD | 6,506.67 USD | 4,771.56 USD | 1,735.11 USD | `+15.38%` | `1B / 0S` |
| `03:00:00` | `103.32` | `103.32` | `103.32` | `103.53` | `103.27` | 40,914.72 USD | 8,739.45 USD | 32,175.27 USD | -23,435.83 USD | `-57.28%` | `0B / 1S` |
| `03:05:00` | `103.35` | `103.35` | `103.35` | `103.53` | `103.30` | 14,675.70 USD | 3,429.65 USD | 11,246.05 USD | -7,816.41 USD | `-53.26%` | `0B / 1S` |
| `03:10:00` | `103.32` | `103.32` | `103.32` | `103.39` | `103.27` | 14,981.40 USD | 6,438.29 USD | 8,543.11 USD | -2,104.82 USD | `-14.05%` | `0B / 1S` |
| `03:15:00` | `103.36` | `103.36` | `103.36` | `103.41` | `103.31` | 26,254.71 USD | 16,081.01 USD | 10,173.70 USD | 5,907.31 USD | `+22.50%` | `1B / 0S` |
| `03:15:00` | `103.38` | `103.38` | `103.38` | `103.41` | `103.31` | 8,787.30 USD | 6,370.79 USD | 2,416.51 USD | 3,954.28 USD | `+45.00%` | `1B / 0S` |
| `03:20:00` | `103.41` | `103.41` | `103.41` | `103.41` | `103.32` | 6,514.83 USD | 5,971.93 USD | 542.90 USD | 5,429.02 USD | `+83.33%` | `1B / 0S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.81` | 12,332,708.79 USD | 3,885,730.79 USD | 8,446,978.00 USD | -4,561,247.21 USD | `-36.98%` | `0B / 5S` |
| `0:00 UTC` | `104.23` | `103.97` | `104.23` | `104.72` | `102.88` | 80,432,525.97 USD | 47,963,579.07 USD | 32,468,946.89 USD | 15,494,632.18 USD | `+19.26%` | `55B / 11S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.60` | `103.57` | `103.60` | `103.66` | `103.45` | 4,757,917.11 USD | 2,812,614.52 USD | 1,945,302.59 USD | 867,311.92 USD | `+18.23%` | `3B / 2S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.51` | `103.50` | `103.56` | `103.41` | 1,731,864.96 USD | 786,756.19 USD | 945,108.77 USD | -158,352.58 USD | `-9.14%` | `1B / 5S` |

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
  * `2026-10-30 08:34:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:50 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:02:50 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:01:50 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:03:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:03:50 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:03:50 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `101.78` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `106.23`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `106.02` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `101.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
