# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 09:37:21 IST` (`2026-10-30 04:07:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.81` | **Live Ask Quote**: `103.86` | **Mid Price**: `103.83`
- **Spread Points**: `46.00` | **Spread BPS**: `4.43 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.21` | VWAP Z-Score: `-0.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3535` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.07` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.16` | Lower -3.00σ Band: `102.26`
  * Upper +2.51σ Band: `105.84` | Lower -2.51σ Band: `102.58`
  * Upper +2.01σ Band: `105.51` | Lower -2.01σ Band: `102.90`
  * Upper +2.00σ Band: `105.51` | Lower -2.00σ Band: `102.91`
  * Upper +1.28σ Band: `105.04` | Lower -1.28σ Band: `103.38`
  * Upper +1.00σ Band: `104.86` | Lower -1.00σ Band: `103.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.97` | EMA-20=`103.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.27` (Slope: `+0.0000`) | EMA-100=`102.87`
  * Institutional Anchors: EMA-144=`102.68` | EMA-200=`102.47` (Slope: `+0.2063`) | EMA-233=`102.41`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.67` (Distance: `-0.79%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.45%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.77%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.25` | Low=`103.42`
  * New York Session (13:00-21:00 UTC): High=`104.46` | Low=`103.21`
  * Initial Balance (First Hour): IB High=`104.14` | IB Low=`103.52`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.42` - `104.25`
  * Optimal Trade Entry (OTE 0.705): `104.04`
  * Structural Invalidation Anchor (0.786): `104.66`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.38` | `103.39` | `103.29` | `103.34` | `122` | 12,607.48 USD | -2,322.43 USD | `-18.42%` | 191,137.13 USD | `-0.58` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `103.34` | `103.39` | `103.31` | `103.33` | `116` | 11,986.28 USD | -3,745.71 USD | `-31.25%` | 187,391.42 USD | `-0.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `103.33` | `103.33` | `103.17` | `103.19` | `167` | 17,232.73 USD | -14,647.82 USD | `-85.00%` | 172,743.60 USD | `-2.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.33` | `103.41` | `103.31` | `103.36` | `254` | 26,254.71 USD | 5,907.31 USD | `+22.50%` | 476,822.26 USD | `-0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.38` | `103.43` | `103.28` | `103.34` | `322` | 33,275.48 USD | -7,764.28 USD | `-23.33%` | 469,057.98 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.34` | `103.39` | `103.06` | `103.07` | `444` | 45,763.08 USD | -41,186.77 USD | `-90.00%` | 427,871.21 USD | `-1.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `42` | `0x0cc1...c7cb` | `LONG` | 31,059,381.68 USD | `300,817.26` | `98.89` | `103.27` | `31.49` | 1,309,880.65 USD | `+4.22%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,336,369.25 USD | `177,712.44` | `100.98` | `103.27` | `93.19` | 390,967.36 USD | `+2.13%` | `10X Isolated` |
| `286` | `0x7fda...17d1` | `SHORT` | 8,120,362.53 USD | `78,647.58` | `100.15` | `103.27` | `209.68` | -243,740.68 USD | `-3.00%` | `20X Cross` |
| `329` | `0x10e1...f4bd` | `LONG` | 6,977,637.99 USD | `67,625.88` | `84.36` | `103.27` | `58.53` | 1,272,407.61 USD | `+18.24%` | `3X Isolated` |
| `391` | `0xea00...a918` | `SHORT` | 5,694,370.18 USD | `55,151.29` | `89.22` | `103.27` | `234.62` | -773,645.68 USD | `-13.59%` | `20X Cross` |
| `412` | `0x354b...6425` | `SHORT` | 5,352,667.97 USD | `51,836.80` | `102.87` | `103.27` | `309.36` | -20,072.48 USD | `-0.37%` | `8X Cross` |
| `467` | `0x4692...164f` | `SHORT` | 4,688,704.41 USD | `45,406.78` | `103.58` | `103.27` | `1487.53` | 14,334.76 USD | `+0.31%` | `5X Cross` |
| `488` | `0x5989...bc29` | `SHORT` | 4,508,111.57 USD | `43,691.72` | `99.48` | `103.27` | `113.23` | -161,804.66 USD | `-3.59%` | `10X Cross` |
| `536` | `0xd84a...c8a5` | `SHORT` | 4,127,200.00 USD | `40,000.00` | `101.97` | `103.27` | `119.23` | -48,570.00 USD | `-1.18%` | `20X Cross` |
| `539` | `0xd507...c948` | `LONG` | 4,107,440.72 USD | `39,808.50` | `93.57` | `103.27` | `82.63` | 382,365.31 USD | `+9.31%` | `7X Isolated` |
| `693` | `0xb5e7...eff1` | `SHORT` | 3,212,229.48 USD | `31,132.29` | `91.71` | `103.27` | `144.59` | -357,020.83 USD | `-11.11%` | `20X Cross` |
| `730` | `0xebe1...4070` | `LONG` | 3,097,497.21 USD | `29,999.97` | `101.87` | `103.27` | `0.000000` | 41,359.18 USD | `+1.34%` | `20X Cross` |
| `732` | `0xbd33...4200` | `SHORT` | 3,093,614.47 USD | `29,982.69` | `104.89` | `103.27` | `403.27` | 51,270.41 USD | `+1.66%` | `20X Cross` |
| `784` | `0x61d7...7dee` | `LONG` | 2,874,397.21 USD | `27,858.08` | `88.25` | `103.27` | `83.50` | 415,921.21 USD | `+14.47%` | `20X Cross` |
| `875` | `0xf0ae...2f74` | `SHORT` | 2,579,500.00 USD | `25,000.00` | `100.78` | `103.27` | `177.32` | -59,981.39 USD | `-2.33%` | `20X Cross` |
| `892` | `0x645b...87b8` | `SHORT` | 2,524,891.01 USD | `24,451.78` | `101.23` | `103.27` | `134.76` | -49,546.75 USD | `-1.96%` | `3X Isolated` |
| `979` | `0x40f2...6a9e` | `LONG` | 2,242,448.91 USD | `21,733.37` | `103.34` | `103.27` | `100.56` | -3,561.05 USD | `-0.16%` | `20X Cross` |
| `1066` | `0x9aa5...58af` | `SHORT` | 2,029,653.78 USD | `19,671.00` | `101.76` | `103.27` | `575.86` | -27,902.85 USD | `-1.37%` | `20X Cross` |
| `1246` | `0x4169...6f06` | `LONG` | 1,772,136.10 USD | `17,175.19` | `76.61` | `103.27` | `82.98` | 456,368.10 USD | `+25.75%` | `12X Isolated` |
| `1255` | `0x6788...98d4` | `SHORT` | 1,755,250.00 USD | `17,000.00` | `99.31` | `103.27` | `201.07` | -66,925.41 USD | `-3.81%` | `20X Cross` |
| `1300` | `0xa99c...40d5` | `SHORT` | 1,662,325.00 USD | `16,100.00` | `101.02` | `103.27` | `152.41` | -35,867.63 USD | `-2.16%` | `20X Cross` |
| `1309` | `0x1bf6...5bfa` | `SHORT` | 1,650,880.00 USD | `16,000.00` | `99.60` | `103.27` | `228.04` | -57,257.69 USD | `-3.47%` | `20X Cross` |
| `1342` | `0xe5dd...ecba` | `SHORT` | 1,607,083.19 USD | `15,575.53` | `102.71` | `103.27` | `144.89` | -7,327.81 USD | `-0.46%` | `20X Cross` |
| `1402` | `0x34ea...2f47` | `SHORT` | 1,548,750.00 USD | `15,000.00` | `99.80` | `103.27` | `201.42` | -51,748.69 USD | `-3.34%` | `20X Cross` |
| `1403` | `0x5d6f...6f8a` | `LONG` | 1,547,700.00 USD | `15,000.00` | `101.91` | `103.27` | `27.55` | 19,045.00 USD | `+1.23%` | `20X Cross` |
| `1458` | `0xfc27...9d9d` | `LONG` | 1,475,109.58 USD | `14,285.39` | `102.69` | `103.27` | `0.000000` | 8,209.30 USD | `+0.56%` | `20X Cross` |
| `1514` | `0xfb29...21dd` | `LONG` | 1,418,710.49 USD | `13,744.53` | `89.85` | `103.27` | `84.68` | 183,716.53 USD | `+12.95%` | `20X Cross` |
| `1540` | `0x6fa6...825e` | `SHORT` | 1,392,930.00 USD | `13,500.00` | `102.95` | `103.27` | `135.50` | -3,155.73 USD | `-0.23%` | `20X Isolated` |
| `1559` | `0xa9d9...b48e` | `SHORT` | 1,375,733.30 USD | `13,333.33` | `96.39` | `103.27` | `174.02` | -90,486.11 USD | `-6.58%` | `20X Cross` |
| `1614` | `0x936c...bb0f` | `SHORT` | 1,310,153.38 USD | `12,687.91` | `101.39` | `103.27` | `163.64` | -23,680.51 USD | `-1.81%` | `2X Isolated` |
| `1646` | `0x89c2...c94b` | `LONG` | 1,276,654.35 USD | `12,364.69` | `75.25` | `103.27` | `45.76` | 346,171.19 USD | `+27.12%` | `3X Isolated` |
| `1684` | `0xcd81...36e3` | `SHORT` | 1,245,604.28 USD | `12,063.96` | `97.96` | `103.27` | `109.19` | -63,765.36 USD | `-5.12%` | `20X Cross` |
| `1690` | `0x436c...b3d1` | `SHORT` | 1,239,120.00 USD | `12,000.00` | `101.05` | `103.27` | `209.83` | -26,460.17 USD | `-2.14%` | `20X Cross` |
| `1754` | `0x9dea...d617` | `LONG` | 1,176,334.34 USD | `11,400.80` | `90.37` | `103.27` | `6.76` | 146,060.61 USD | `+12.42%` | `20X Cross` |
| `1771` | `0x17c3...a868` | `LONG` | 1,167,066.94 USD | `11,306.60` | `95.13` | `103.27` | `64.99` | 91,420.07 USD | `+7.83%` | `3X Isolated` |
| `1814` | `0x8607...08d5` | `SHORT` | 1,135,004.13 USD | `10,998.10` | `92.18` | `103.27` | `135.02` | -121,214.42 USD | `-10.68%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.31%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.15%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.31%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.15%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.32%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.18%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.06%`) | Long MP=`99.21` (Vol: 8,800,000.00 USD, Dist: `--4.10%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.95` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.78` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-176.95K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
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
| `03:15:00` | `103.38` | `103.38` | `103.38` | `103.41` | `103.31` | 8,787.30 USD | 6,370.79 USD | 2,416.51 USD | 3,954.28 USD | `+45.00%` | `1B / 0S` |
| `03:20:00` | `103.41` | `103.41` | `103.41` | `103.41` | `103.32` | 6,514.83 USD | 5,971.93 USD | 542.90 USD | 5,429.02 USD | `+83.33%` | `1B / 0S` |
| `03:25:00` | `103.36` | `103.36` | `103.36` | `103.41` | `103.31` | 10,956.69 USD | 4,793.55 USD | 6,163.14 USD | -1,369.59 USD | `-12.50%` | `0B / 1S` |
| `03:30:00` | `103.30` | `103.30` | `103.30` | `103.42` | `103.28` | 10,536.09 USD | 1,599.23 USD | 8,936.86 USD | -7,337.63 USD | `-69.64%` | `0B / 1S` |
| `03:30:00` | `103.34` | `103.34` | `103.34` | `103.43` | `103.28` | 33,275.48 USD | 12,755.60 USD | 20,519.88 USD | -7,764.28 USD | `-23.33%` | `0B / 1S` |
| `03:35:00` | `103.39` | `103.39` | `103.39` | `103.43` | `103.28` | 10,132.22 USD | 8,021.34 USD | 2,110.88 USD | 5,910.46 USD | `+58.33%` | `1B / 0S` |
| `03:40:00` | `103.34` | `103.34` | `103.34` | `103.39` | `103.29` | 12,607.48 USD | 5,142.52 USD | 7,464.96 USD | -2,322.43 USD | `-18.42%` | `0B / 1S` |
| `03:45:00` | `103.07` | `103.07` | `103.07` | `103.39` | `103.06` | 45,763.08 USD | 2,288.15 USD | 43,474.93 USD | -41,186.77 USD | `-90.00%` | `0B / 1S` |
| `03:45:00` | `103.33` | `103.33` | `103.33` | `103.39` | `103.31` | 11,986.28 USD | 4,120.28 USD | 7,866.00 USD | -3,745.71 USD | `-31.25%` | `0B / 1S` |
| `03:50:00` | `103.19` | `103.19` | `103.19` | `103.33` | `103.17` | 17,232.73 USD | 1,292.45 USD | 15,940.28 USD | -14,647.82 USD | `-85.00%` | `0B / 1S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.60` | `103.57` | `103.60` | `103.66` | `103.45` | 4,757,917.11 USD | 2,812,614.52 USD | 1,945,302.59 USD | 867,311.92 USD | `+18.23%` | `3B / 2S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.37` | `103.38` | `103.41` | `103.35` | 313,079.69 USD | 93,440.85 USD | 219,638.84 USD | -126,198.00 USD | `-40.31%` | `1B / 1S` |

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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `102.56` (Risk Distance: `0.4932` pts)
  * +2.5R Take Profit: `104.29`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.49 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.16` (Risk Distance: `0.4932` pts)
  * +2.5R Take Profit: `103.43`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.49 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.66`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
