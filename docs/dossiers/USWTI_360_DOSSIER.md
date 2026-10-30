# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 10:01:31 IST` (`2026-10-30 04:31:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.75` | **Live Ask Quote**: `103.79` | **Mid Price**: `103.77`
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
  * Session VWAP: `103.77` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `104.49` | Lower -3.00σ Band: `103.04`
  * Upper +2.51σ Band: `104.34` | Lower -2.51σ Band: `103.20`
  * Upper +2.01σ Band: `104.20` | Lower -2.01σ Band: `103.33`
  * Upper +2.00σ Band: `104.18` | Lower -2.00σ Band: `103.35`
  * Upper +1.28σ Band: `104.06` | Lower -1.28σ Band: `103.48`
  * Upper +1.00σ Band: `103.98` | Lower -1.00σ Band: `103.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.77` | EMA-20=`103.77` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.77` (Slope: `+0.0000`) | EMA-100=`103.77`
  * Institutional Anchors: EMA-144=`103.77` | EMA-200=`103.77` (Slope: `+0.0000`) | EMA-233=`103.77`
- **Range Boundaries**: 24H High=`104.81` | 24H Low=`102.73` | Weekly High=`105.84` | Weekly Low=`101.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.61` (Distance: `-0.80%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.38%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.70%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.18` | Low=`103.35`
  * New York Session (13:00-21:00 UTC): High=`104.39` | Low=`103.15`
  * Initial Balance (First Hour): IB High=`104.08` | IB Low=`103.46`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.35` - `104.18`
  * Optimal Trade Entry (OTE 0.705): `103.98`
  * Structural Invalidation Anchor (0.786): `104.60`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.31` | `103.41` | `103.27` | `103.40` | `320` | 33,087.68 USD | 24,815.76 USD | `+75.00%` | 197,589.79 USD | `+1.76` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.39` | `103.42` | `103.31` | `103.42` | `259` | 26,784.49 USD | 14,090.97 USD | `+52.61%` | 211,680.76 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.41` | `103.69` | `103.34` | `103.69` | `360` | 37,328.40 USD | 33,595.56 USD | `+90.00%` | 245,276.32 USD | `+1.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.06` | `103.49` | `103.05` | `103.37` | `1,876` | 193,918.37 USD | 112,314.71 USD | `+57.92%` | 643,742.44 USD | `+2.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.37` | `103.42` | `103.27` | `103.42` | `910` | 94,107.65 USD | 55,197.76 USD | `+58.65%` | 698,940.19 USD | `+1.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.41` | `105.19` | `103.34` | `105.01` | `2,427` | 254,859.27 USD | 211,924.76 USD | `+83.15%` | 910,864.95 USD | `+3.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.46` | `103.48` | `103.24` | `103.48` | `567` | 58,673.16 USD | 30,533.99 USD | `+52.04%` | 557,457.58 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 426,105.17 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 931,531.43 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.75` | `15,151` | 1,571,916.25 USD | -137,426.86 USD | `-8.74%` | 2,371,108.86 USD | `-0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -392,114.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,194,880.62 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.75` | `15,151` | 1,571,916.25 USD | -137,426.86 USD | `-8.74%` | 2,371,108.86 USD | `-0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `42` | `0x0cc1...c7cb` | `LONG` | 31,041,332.65 USD | `300,817.26` | `98.89` | `103.20` | `31.53` | 1,291,831.61 USD | `+4.16%` | `3X Cross` |
| `113` | `0x30af...393e` | `LONG` | 18,332,815.00 USD | `177,712.44` | `100.98` | `103.20` | `93.19` | 387,413.11 USD | `+2.11%` | `10X Isolated` |
| `288` | `0x7fda...17d1` | `SHORT` | 8,115,643.68 USD | `78,647.58` | `100.15` | `103.20` | `211.05` | -239,021.83 USD | `-2.95%` | `20X Cross` |
| `331` | `0x10e1...f4bd` | `LONG` | 6,976,285.47 USD | `67,625.88` | `84.36` | `103.20` | `58.53` | 1,271,055.09 USD | `+18.22%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,689,958.07 USD | `55,151.29` | `89.22` | `103.20` | `241.77` | -769,233.58 USD | `-13.52%` | `20X Cross` |
| `413` | `0x354b...6425` | `SHORT` | 5,346,171.74 USD | `51,809.01` | `102.87` | `103.20` | `308.07` | -16,435.09 USD | `-0.31%` | `8X Cross` |
| `472` | `0x4692...164f` | `SHORT` | 4,696,513.20 USD | `45,513.26` | `103.57` | `103.20` | `1474.86` | 17,196.22 USD | `+0.37%` | `5X Cross` |
| `492` | `0x5989...bc29` | `SHORT` | 4,508,548.48 USD | `43,691.72` | `99.48` | `103.20` | `113.23` | -162,241.58 USD | `-3.60%` | `10X Cross` |
| `541` | `0xd84a...c8a5` | `SHORT` | 4,126,400.00 USD | `40,000.00` | `101.97` | `103.20` | `119.25` | -47,770.00 USD | `-1.16%` | `20X Cross` |
| `545` | `0xd507...c948` | `LONG` | 4,106,644.55 USD | `39,808.50` | `93.57` | `103.20` | `82.63` | 381,569.14 USD | `+9.29%` | `7X Isolated` |
| `699` | `0xb5e7...eff1` | `SHORT` | 3,211,606.83 USD | `31,132.29` | `91.71` | `103.20` | `144.79` | -356,398.19 USD | `-11.10%` | `20X Cross` |
| `733` | `0xebe1...4070` | `LONG` | 3,095,697.21 USD | `29,999.97` | `101.87` | `103.20` | `0.000000` | 39,559.18 USD | `+1.28%` | `20X Cross` |
| `734` | `0xbd33...4200` | `SHORT` | 3,093,014.82 USD | `29,982.69` | `104.89` | `103.20` | `403.27` | 51,870.06 USD | `+1.68%` | `20X Cross` |
| `790` | `0x61d7...7dee` | `LONG` | 2,874,118.63 USD | `27,858.08` | `88.25` | `103.20` | `83.50` | 415,642.63 USD | `+14.46%` | `20X Cross` |
| `879` | `0xf0ae...2f74` | `SHORT` | 2,579,000.00 USD | `25,000.00` | `100.78` | `103.20` | `176.37` | -59,481.39 USD | `-2.31%` | `20X Cross` |
| `895` | `0x645b...87b8` | `SHORT` | 2,523,179.38 USD | `24,451.78` | `101.23` | `103.20` | `134.76` | -47,835.12 USD | `-1.90%` | `3X Isolated` |
| `988` | `0x40f2...6a9e` | `LONG` | 2,242,014.24 USD | `21,733.37` | `103.34` | `103.20` | `100.57` | -3,995.71 USD | `-0.18%` | `20X Cross` |
| `1080` | `0x9aa5...58af` | `SHORT` | 2,029,260.36 USD | `19,671.00` | `101.76` | `103.20` | `568.24` | -27,509.43 USD | `-1.36%` | `20X Cross` |
| `1253` | `0x4169...6f06` | `LONG` | 1,771,792.60 USD | `17,175.19` | `76.61` | `103.20` | `82.98` | 456,024.60 USD | `+25.74%` | `12X Isolated` |
| `1263` | `0x6788...98d4` | `SHORT` | 1,754,230.00 USD | `17,000.00` | `99.31` | `103.20` | `198.88` | -65,905.41 USD | `-3.76%` | `20X Cross` |
| `1307` | `0xa99c...40d5` | `SHORT` | 1,661,359.00 USD | `16,100.00` | `101.02` | `103.20` | `153.13` | -34,901.63 USD | `-2.10%` | `20X Cross` |
| `1319` | `0x1bf6...5bfa` | `SHORT` | 1,650,720.00 USD | `16,000.00` | `99.60` | `103.20` | `226.65` | -57,097.69 USD | `-3.46%` | `20X Cross` |
| `1351` | `0xe5dd...ecba` | `SHORT` | 1,606,771.67 USD | `15,575.53` | `102.71` | `103.20` | `145.00` | -7,016.30 USD | `-0.44%` | `20X Cross` |
| `1409` | `0x34ea...2f47` | `SHORT` | 1,547,550.00 USD | `15,000.00` | `99.80` | `103.20` | `200.56` | -50,548.69 USD | `-3.27%` | `20X Cross` |
| `1410` | `0x5d6f...6f8a` | `LONG` | 1,547,400.00 USD | `15,000.00` | `101.91` | `103.20` | `27.64` | 18,745.00 USD | `+1.21%` | `20X Cross` |
| `1474` | `0xfc27...9d9d` | `LONG` | 1,474,109.60 USD | `14,285.39` | `102.69` | `103.20` | `0.000000` | 7,209.33 USD | `+0.49%` | `20X Cross` |
| `1521` | `0xfb29...21dd` | `LONG` | 1,418,023.26 USD | `13,744.53` | `89.85` | `103.20` | `84.67` | 183,029.30 USD | `+12.91%` | `20X Cross` |
| `1543` | `0x6fa6...825e` | `SHORT` | 1,393,065.00 USD | `13,500.00` | `102.95` | `103.20` | `135.50` | -3,290.73 USD | `-0.24%` | `20X Isolated` |
| `1566` | `0xa9d9...b48e` | `SHORT` | 1,375,466.63 USD | `13,333.33` | `96.39` | `103.20` | `174.21` | -90,219.45 USD | `-6.56%` | `20X Cross` |
| `1621` | `0x936c...bb0f` | `SHORT` | 1,309,265.23 USD | `12,687.91` | `101.39` | `103.20` | `163.64` | -22,792.36 USD | `-1.74%` | `2X Isolated` |
| `1656` | `0x89c2...c94b` | `LONG` | 1,275,912.46 USD | `12,364.69` | `75.25` | `103.20` | `45.76` | 345,429.31 USD | `+27.07%` | `3X Isolated` |
| `1694` | `0xcd81...36e3` | `SHORT` | 1,244,639.17 USD | `12,063.96` | `97.96` | `103.20` | `109.34` | -62,800.25 USD | `-5.05%` | `20X Cross` |
| `1698` | `0x436c...b3d1` | `SHORT` | 1,238,280.00 USD | `12,000.00` | `101.05` | `103.20` | `208.34` | -25,620.17 USD | `-2.07%` | `20X Cross` |
| `1763` | `0x9dea...d617` | `LONG` | 1,176,220.33 USD | `11,400.80` | `90.37` | `103.20` | `5.50` | 145,946.61 USD | `+12.41%` | `20X Cross` |
| `1784` | `0x17c3...a868` | `LONG` | 1,166,727.74 USD | `11,306.60` | `95.13` | `103.20` | `64.99` | 91,080.88 USD | `+7.81%` | `3X Isolated` |
| `1825` | `0x8607...08d5` | `SHORT` | 1,134,674.18 USD | `10,998.10` | `92.18` | `103.20` | `135.02` | -120,884.48 USD | `-10.65%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.40%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.05%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.40%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.05%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.42%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.09%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.16%`) | Long MP=`99.12` (Vol: 8,700,000.00 USD, Dist: `--4.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.97` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.65` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-196.33K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
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
| `03:50:00` | `103.19` | `103.19` | `103.19` | `103.33` | `103.17` | 17,232.73 USD | 1,292.45 USD | 15,940.28 USD | -14,647.82 USD | `-85.00%` | `0B / 1S` |
| `03:55:00` | `103.07` | `103.07` | `103.07` | `103.20` | `103.06` | 16,594.27 USD | 921.90 USD | 15,672.37 USD | -14,750.46 USD | `-88.89%` | `0B / 1S` |
| `04:00:00` | `103.80` | `103.80` | `103.80` | `105.59` | `103.05` | 1,557,000.00 USD | 733,380.65 USD | 823,619.35 USD | -90,238.70 USD | `-5.80%` | `0B / 1S` |
| `04:00:00` | `104.94` | `104.94` | `104.94` | `105.59` | `103.05` | 819,305.61 USD | 662,365.93 USD | 156,939.68 USD | 505,426.25 USD | `+61.69%` | `1B / 0S` |
| `04:00:00` | `103.23` | `103.23` | `103.23` | `103.35` | `103.05` | 87,852.99 USD | 62,060.62 USD | 25,792.36 USD | 36,268.26 USD | `+41.28%` | `1B / 0S` |
| `04:00:00` | `103.37` | `103.37` | `103.37` | `103.49` | `103.05` | 193,918.37 USD | 153,116.54 USD | 40,801.83 USD | 112,314.71 USD | `+57.92%` | `1B / 0S` |
| `04:05:00` | `103.39` | `103.39` | `103.39` | `103.47` | `103.09` | 55,105.27 USD | 40,316.52 USD | 14,788.75 USD | 25,527.77 USD | `+46.33%` | `1B / 0S` |
| `04:10:00` | `103.37` | `103.37` | `103.37` | `103.49` | `103.28` | 50,857.06 USD | 23,491.12 USD | 27,365.94 USD | -3,874.82 USD | `-7.62%` | `0B / 1S` |
| `04:15:00` | `103.32` | `103.32` | `103.32` | `103.40` | `103.28` | 34,198.59 USD | 10,806.75 USD | 23,391.83 USD | -12,585.08 USD | `-36.80%` | `0B / 1S` |
| `04:15:00` | `103.42` | `103.42` | `103.42` | `103.42` | `103.27` | 94,107.65 USD | 74,652.70 USD | 19,454.95 USD | 55,197.76 USD | `+58.65%` | `1B / 0S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.60` | `103.57` | `103.60` | `103.66` | `103.45` | 4,757,917.11 USD | 2,812,614.52 USD | 1,945,302.59 USD | 867,311.92 USD | `+18.23%` | `3B / 2S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.27` | 3,220,810.77 USD | 1,914,411.02 USD | 1,306,399.75 USD | 608,011.27 USD | `+18.88%` | `1B / 1S` |

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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `104.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.88` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `101.44`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.60`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
