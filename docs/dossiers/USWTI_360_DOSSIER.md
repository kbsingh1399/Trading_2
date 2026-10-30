# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 15:05:59 IST` (`2026-10-30 09:35:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.21` | **Live Ask Quote**: `104.24` | **Mid Price**: `104.22`
- **Spread Points**: `30.00` | **Spread BPS**: `2.88 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.09` | VWAP Z-Score: `+0.41` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3563` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `57.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `105.65` | Lower -3.00σ Band: `102.54`
  * Upper +2.51σ Band: `105.39` | Lower -2.51σ Band: `102.79`
  * Upper +2.01σ Band: `105.13` | Lower -2.01σ Band: `103.05`
  * Upper +2.00σ Band: `105.13` | Lower -2.00σ Band: `103.05`
  * Upper +1.28σ Band: `104.75` | Lower -1.28σ Band: `103.43`
  * Upper +1.00σ Band: `104.61` | Lower -1.00σ Band: `103.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.20` | EMA-20=`104.06` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.70` (Slope: `+0.0000`) | EMA-100=`103.26`
  * Institutional Anchors: EMA-144=`103.00` | EMA-200=`102.77` (Slope: `+0.1682`) | EMA-233=`102.71`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.61` (Distance: `-0.43%`)
  * Point of Control (POC) = `104.06` (Distance: `+0.10%`)
  * Value Area Low (VAL) = `103.41` (Distance: `+0.73%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.37` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.72` | Low=`103.08`
  * New York Session (13:00-21:00 UTC): High=`104.85` | Low=`103.60`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.81` - `104.64`
  * Optimal Trade Entry (OTE 0.705): `104.43`
  * Structural Invalidation Anchor (0.786): `105.06`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.98` | `103.98` | `103.91` | `103.98` | `172` | 17,885.08 USD | 9,581.29 USD | `+53.57%` | 356,385.83 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.99` | `104.04` | `103.33` | `103.35` | `588` | 60,769.80 USD | -54,692.82 USD | `-90.00%` | 301,693.01 USD | `-3.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `103.36` | `103.47` | `103.08` | `103.42` | `1,075` | 111,171.12 USD | 48,366.66 USD | `+43.51%` | 350,059.67 USD | `+2.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.90` | `104.09` | `103.76` | `104.01` | `684` | 71,144.89 USD | 31,522.66 USD | `+44.31%` | 586,939.45 USD | `+0.58` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.02` | `104.04` | `103.33` | `103.35` | `954` | 98,595.90 USD | -88,736.31 USD | `-90.00%` | 498,203.14 USD | `-1.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `103.36` | `103.50` | `103.08` | `103.50` | `1,922` | 198,923.16 USD | 133,899.85 USD | `+67.31%` | 632,102.99 USD | `+2.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:01:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 31,161,659.55 USD | `300,817.26` | `98.89` | `103.63` | `31.12` | 1,412,158.52 USD | `+4.53%` | `3X Cross` |
| `108` | `0x30af...393e` | `LONG` | 18,384,351.61 USD | `177,712.44` | `100.98` | `103.63` | `93.19` | 438,949.72 USD | `+2.39%` | `10X Isolated` |
| `286` | `0x7fda...17d1` | `SHORT` | 8,138,451.47 USD | `78,647.58` | `100.15` | `103.63` | `209.86` | -261,829.63 USD | `-3.22%` | `20X Cross` |
| `326` | `0x10e1...f4bd` | `LONG` | 6,995,896.98 USD | `67,625.88` | `84.36` | `103.63` | `58.53` | 1,290,666.59 USD | `+18.45%` | `3X Isolated` |
| `394` | `0xea00...a918` | `SHORT` | 5,711,467.07 USD | `55,151.29` | `89.22` | `103.63` | `225.57` | -790,742.58 USD | `-13.84%` | `20X Cross` |
| `486` | `0x354b...6425` | `SHORT` | 4,550,669.27 USD | `43,908.43` | `102.98` | `103.63` | `352.09` | -28,964.97 USD | `-0.64%` | `8X Cross` |
| `489` | `0x5989...bc29` | `SHORT` | 4,526,462.09 USD | `43,691.72` | `99.48` | `103.63` | `113.23` | -180,155.19 USD | `-3.98%` | `10X Cross` |
| `535` | `0xd84a...c8a5` | `SHORT` | 4,138,800.00 USD | `40,000.00` | `101.97` | `103.63` | `119.02` | -60,170.00 USD | `-1.45%` | `20X Cross` |
| `538` | `0x4692...164f` | `SHORT` | 4,123,455.76 USD | `39,786.33` | `103.43` | `103.63` | `1705.92` | -8,477.14 USD | `-0.21%` | `5X Cross` |
| `539` | `0xd507...c948` | `LONG` | 4,118,189.01 USD | `39,808.50` | `93.57` | `103.63` | `82.63` | 393,113.60 USD | `+9.55%` | `7X Isolated` |
| `696` | `0xb5e7...eff1` | `SHORT` | 3,220,635.19 USD | `31,132.29` | `91.71` | `103.63` | `144.04` | -365,426.55 USD | `-11.35%` | `20X Cross` |
| `734` | `0xbd33...4200` | `SHORT` | 3,101,709.80 USD | `29,982.69` | `104.89` | `103.63` | `403.27` | 43,175.08 USD | `+1.39%` | `20X Cross` |
| `786` | `0x61d7...7dee` | `LONG` | 2,886,654.77 USD | `27,858.08` | `88.25` | `103.63` | `83.50` | 428,178.77 USD | `+14.83%` | `20X Cross` |
| `866` | `0xf0ae...2f74` | `SHORT` | 2,586,750.00 USD | `25,000.00` | `100.78` | `103.63` | `176.41` | -67,231.39 USD | `-2.60%` | `20X Cross` |
| `869` | `0x645b...87b8` | `SHORT` | 2,579,133.60 USD | `24,895.11` | `101.26` | `103.63` | `134.75` | -58,178.15 USD | `-2.26%` | `3X Isolated` |
| `893` | `0x40f2...6a9e` | `LONG` | 2,489,467.46 USD | `24,064.45` | `103.38` | `103.63` | `101.09` | 1,608.80 USD | `+0.06%` | `20X Cross` |
| `1014` | `0xebe1...4070` | `LONG` | 2,175,597.51 USD | `20,999.98` | `101.87` | `103.63` | `0.000000` | 36,301.41 USD | `+1.67%` | `20X Cross` |
| `1068` | `0x9aa5...58af` | `SHORT` | 2,034,964.95 USD | `19,671.00` | `101.76` | `103.63` | `583.60` | -33,214.02 USD | `-1.63%` | `20X Cross` |
| `1251` | `0x4169...6f06` | `LONG` | 1,777,116.91 USD | `17,175.19` | `76.61` | `103.63` | `82.98` | 461,348.91 USD | `+25.96%` | `12X Isolated` |
| `1258` | `0x6788...98d4` | `SHORT` | 1,761,200.00 USD | `17,000.00` | `99.31` | `103.63` | `197.83` | -72,875.41 USD | `-4.14%` | `20X Cross` |
| `1298` | `0xa99c...40d5` | `SHORT` | 1,667,799.00 USD | `16,100.00` | `101.02` | `103.63` | `151.37` | -41,341.63 USD | `-2.48%` | `20X Cross` |
| `1308` | `0x1bf6...5bfa` | `SHORT` | 1,657,920.00 USD | `16,000.00` | `99.60` | `103.63` | `227.14` | -64,297.69 USD | `-3.88%` | `20X Cross` |
| `1315` | `0xce97...7e78` | `SHORT` | 1,643,660.13 USD | `15,862.38` | `103.08` | `103.63` | `120.69` | -8,586.50 USD | `-0.52%` | `5X Isolated` |
| `1367` | `0xe5dd...ecba` | `SHORT` | 1,570,176.72 USD | `15,178.12` | `102.71` | `103.63` | `146.05` | -11,238.93 USD | `-0.72%` | `20X Cross` |
| `1386` | `0x34ea...2f47` | `SHORT` | 1,553,700.00 USD | `15,000.00` | `99.80` | `103.63` | `199.29` | -56,698.69 USD | `-3.65%` | `20X Cross` |
| `1387` | `0x5d6f...6f8a` | `LONG` | 1,553,550.00 USD | `15,000.00` | `101.91` | `103.63` | `26.36` | 24,895.00 USD | `+1.60%` | `20X Cross` |
| `1413` | `0xfc27...9d9d` | `LONG` | 1,540,269.75 USD | `14,864.60` | `102.69` | `103.63` | `0.000000` | 13,867.30 USD | `+0.90%` | `20X Cross` |
| `1515` | `0xfb29...21dd` | `LONG` | 1,422,284.07 USD | `13,744.53` | `89.85` | `103.63` | `84.72` | 187,290.11 USD | `+13.17%` | `20X Cross` |
| `1536` | `0x6fa6...825e` | `SHORT` | 1,398,600.00 USD | `13,500.00` | `102.95` | `103.63` | `135.50` | -8,825.73 USD | `-0.63%` | `20X Isolated` |
| `1554` | `0xa9d9...b48e` | `SHORT` | 1,379,333.30 USD | `13,333.33` | `96.39` | `103.63` | `173.36` | -94,086.11 USD | `-6.82%` | `20X Cross` |
| `1613` | `0x936c...bb0f` | `SHORT` | 1,314,467.27 USD | `12,687.91` | `101.39` | `103.63` | `163.64` | -27,994.40 USD | `-2.13%` | `2X Isolated` |
| `1651` | `0x89c2...c94b` | `LONG` | 1,280,858.34 USD | `12,364.69` | `75.25` | `103.63` | `45.76` | 350,375.19 USD | `+27.35%` | `3X Isolated` |
| `1687` | `0xcd81...36e3` | `SHORT` | 1,248,017.08 USD | `12,063.96` | `97.96` | `103.63` | `108.95` | -66,178.15 USD | `-5.30%` | `20X Cross` |
| `1694` | `0x436c...b3d1` | `SHORT` | 1,243,200.00 USD | `12,000.00` | `101.05` | `103.63` | `220.86` | -30,540.17 USD | `-2.46%` | `20X Cross` |
| `1758` | `0x9dea...d617` | `LONG` | 1,181,578.70 USD | `11,400.80` | `90.37` | `103.63` | `4.86` | 151,304.98 USD | `+12.81%` | `20X Cross` |
| `1770` | `0x17c3...a868` | `LONG` | 1,170,232.79 USD | `11,306.60` | `95.13` | `103.63` | `64.99` | 94,585.92 USD | `+8.08%` | `3X Isolated` |
| `1819` | `0x8607...08d5` | `SHORT` | 1,139,623.33 USD | `10,998.10` | `92.18` | `103.63` | `135.02` | -125,833.63 USD | `-11.04%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 4,100,000.00 USD, Dist: `+2.01%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.42%`)
  * 48H Horizon: Short MP=`104.86` (Vol: 2,600,000.00 USD, Dist: `+1.07%`) | Long MP=`101.83` (Vol: 5,100,000.00 USD, Dist: `--1.85%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.03%`) | Long MP=`99.12` (Vol: 9,900,000.00 USD, Dist: `--4.46%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+1.77%`) | Long MP=`99.12` (Vol: 8,800,000.00 USD, Dist: `--4.46%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `103.20` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `105.00` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-183.81K` | Last 24h: `-694.60K` | Last 3d: `-989.86K` | Last 7d: `-1.36M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0317%` | **USDT OKX** | `-0.0314%` |
| **USDT Bybit** | `-0.0708%` | **USDT KuCoin** | `-0.0252%` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-0.0453%` | **USDT Bitget** | `-0.0237%` |
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
| `08:50:00` | `104.03` | `104.03` | `104.03` | `104.12` | `103.96` | 32,145.27 USD | 18,332.85 USD | 13,812.42 USD | 4,520.43 USD | `+14.06%` | `1B / 0S` |
| `08:55:00` | `103.92` | `103.92` | `103.92` | `104.03` | `103.91` | 24,629.04 USD | 2,052.42 USD | 22,576.62 USD | -20,524.20 USD | `-83.33%` | `0B / 1S` |
| `09:00:00` | `103.45` | `103.45` | `103.45` | `104.09` | `103.08` | 463,964.28 USD | 147,677.56 USD | 316,286.72 USD | -168,609.15 USD | `-36.34%` | `0B / 1S` |
| `09:00:00` | `103.91` | `103.91` | `103.91` | `103.97` | `103.79` | 27,639.53 USD | 16,430.16 USD | 11,209.36 USD | 5,220.80 USD | `+18.89%` | `1B / 0S` |
| `09:00:00` | `104.01` | `104.01` | `104.01` | `104.09` | `103.76` | 71,144.89 USD | 51,333.78 USD | 19,811.12 USD | 31,522.66 USD | `+44.31%` | `1B / 0S` |
| `09:05:00` | `103.97` | `103.97` | `103.97` | `104.01` | `103.76` | 23,288.83 USD | 16,872.52 USD | 6,416.31 USD | 10,456.21 USD | `+44.90%` | `1B / 0S` |
| `09:10:00` | `104.01` | `104.01` | `104.01` | `104.09` | `103.95` | 20,178.52 USD | 11,530.58 USD | 8,647.94 USD | 2,882.65 USD | `+14.29%` | `1B / 0S` |
| `09:15:00` | `103.35` | `103.35` | `103.35` | `104.04` | `103.33` | 98,595.90 USD | 4,929.80 USD | 93,666.10 USD | -88,736.31 USD | `-90.00%` | `0B / 1S` |
| `09:15:00` | `103.97` | `103.97` | `103.97` | `104.02` | `103.89` | 20,169.79 USD | 9,076.41 USD | 11,093.39 USD | -2,016.98 USD | `-10.00%` | `0B / 1S` |
| `09:20:00` | `103.98` | `103.98` | `103.98` | `103.98` | `103.91` | 17,885.08 USD | 13,733.18 USD | 4,151.89 USD | 9,581.29 USD | `+53.57%` | `1B / 0S` |
| `0:00 UTC` | `103.22` | `103.18` | `103.22` | `103.38` | `102.91` | 7,833,614.37 USD | 4,518,281.07 USD | 3,315,333.30 USD | 1,202,947.77 USD | `+15.36%` | `10B / 7S` |
| `5:00 UTC` | `103.57` | `103.51` | `103.57` | `103.68` | `103.16` | 13,871,996.58 USD | 7,371,562.11 USD | 6,500,434.46 USD | 871,127.65 USD | `+6.28%` | `13B / 5S` |
| `0:00 UTC` | `103.81` | `103.77` | `103.81` | `103.93` | `103.44` | 11,322,481.70 USD | 6,201,023.76 USD | 5,121,457.94 USD | 1,079,565.82 USD | `+9.53%` | `13B / 8S` |
| `5:00 UTC` | `103.97` | `104.00` | `103.97` | `104.22` | `103.69` | 15,722,195.08 USD | 7,756,867.01 USD | 7,965,328.07 USD | -208,461.06 USD | `-1.33%` | `8B / 12S` |
| `0:00 UTC` | `104.00` | `103.97` | `104.00` | `104.09` | `103.80` | 12,864,820.33 USD | 5,029,660.97 USD | 7,835,159.36 USD | -2,805,498.39 USD | `-21.81%` | `3B / 7S` |
| `5:00 UTC` | `103.66` | `103.71` | `103.66` | `103.91` | `103.53` | 12,894,660.60 USD | 5,121,489.28 USD | 7,773,171.32 USD | -2,651,682.04 USD | `-20.56%` | `1B / 7S` |
| `0:00 UTC` | `103.95` | `103.93` | `103.95` | `104.06` | `103.75` | 6,764,822.00 USD | 3,222,639.15 USD | 3,542,182.85 USD | -319,543.70 USD | `-4.72%` | `2B / 2S` |
| `5:00 UTC` | `103.68` | `103.69` | `103.68` | `103.91` | `103.53` | 13,568,328.10 USD | 6,666,787.03 USD | 6,901,541.08 USD | -234,754.05 USD | `-1.73%` | `5B / 11S` |
| `0:00 UTC` | `103.50` | `103.54` | `103.50` | `103.73` | `103.44` | 11,288,542.95 USD | 4,691,353.92 USD | 6,597,189.03 USD | -1,905,835.11 USD | `-16.88%` | `3B / 5S` |
| `5:00 UTC` | `103.75` | `103.67` | `103.75` | `103.81` | `103.52` | 5,925,666.04 USD | 3,064,432.48 USD | 2,861,233.56 USD | 203,198.92 USD | `+3.43%` | `9B / 2S` |

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
  * `2026-10-30 14:41:20 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:20 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:20 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:57:20 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:56:20 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.41` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.94` (Risk Distance: `0.4726` pts)
  * +2.5R Take Profit: `104.59`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.09` (Risk Distance: `0.4726` pts)
  * +2.5R Take Profit: `103.43`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.06`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
