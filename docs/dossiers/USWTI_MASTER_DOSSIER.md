# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 08:15:37 IST` (`2026-10-30 02:45:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `104.16` | **Live Ask Quote**: `104.21` | **Mid Price**: `104.18`
- **Spread Points**: `50.00` | **Spread BPS**: `4.80 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.27` | VWAP Z-Score: `+0.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4211` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.94` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.52` | Lower -3.00σ Band: `102.02`
  * Upper +2.51σ Band: `106.16` | Lower -2.51σ Band: `102.39`
  * Upper +2.01σ Band: `105.78` | Lower -2.01σ Band: `102.77`
  * Upper +2.00σ Band: `105.77` | Lower -2.00σ Band: `102.77`
  * Upper +1.28σ Band: `105.23` | Lower -1.28σ Band: `103.31`
  * Upper +1.00σ Band: `105.02` | Lower -1.00σ Band: `103.52`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`104.13` | EMA-20=`103.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.09` (Slope: `+0.0000`) | EMA-100=`102.73`
  * Institutional Anchors: EMA-144=`102.58` | EMA-200=`102.39` (Slope: `+0.1792`) | EMA-233=`102.33`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.83` (Distance: `-0.62%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.78%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+1.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.15` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.60` | Low=`103.77`
  * New York Session (13:00-21:00 UTC): High=`104.81` | Low=`103.56`
  * Initial Balance (First Hour): IB High=`104.50` | IB Low=`103.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.77` - `104.60`
  * Optimal Trade Entry (OTE 0.705): `104.39`
  * Structural Invalidation Anchor (0.786): `105.02`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `38` | `0x0cc1...c7cb` | `LONG` | 31,131,577.82 USD | `300,817.26` | `98.89` | `103.51` | `31.28` | 1,382,076.79 USD | `+4.44%` | `3X Cross` |
| `109` | `0x30af...393e` | `LONG` | 18,393,237.23 USD | `177,712.44` | `100.98` | `103.51` | `93.19` | 447,835.34 USD | `+2.43%` | `10X Isolated` |
| `288` | `0x7fda...17d1` | `SHORT` | 8,144,743.28 USD | `78,647.58` | `100.15` | `103.51` | `212.36` | -268,121.43 USD | `-3.29%` | `20X Cross` |
| `327` | `0x10e1...f4bd` | `LONG` | 7,001,307.05 USD | `67,625.88` | `84.36` | `103.51` | `58.53` | 1,296,076.66 USD | `+18.51%` | `3X Isolated` |
| `393` | `0xea00...a918` | `SHORT` | 5,707,606.48 USD | `55,151.29` | `89.22` | `103.51` | `229.19` | -786,881.99 USD | `-13.79%` | `20X Cross` |
| `450` | `0x4692...164f` | `SHORT` | 4,804,229.66 USD | `46,408.71` | `103.71` | `103.51` | `1456.68` | 9,043.10 USD | `+0.19%` | `5X Cross` |
| `485` | `0x5989...bc29` | `SHORT` | 4,524,714.42 USD | `43,691.72` | `99.48` | `103.51` | `113.23` | -178,407.52 USD | `-3.94%` | `10X Cross` |
| `527` | `0x354b...6425` | `SHORT` | 4,177,271.44 USD | `40,352.31` | `102.67` | `103.51` | `369.61` | -34,387.91 USD | `-0.82%` | `8X Cross` |
| `532` | `0xd84a...c8a5` | `SHORT` | 4,140,000.00 USD | `40,000.00` | `101.97` | `103.51` | `119.05` | -61,370.00 USD | `-1.48%` | `20X Cross` |
| `533` | `0xebe1...4070` | `LONG` | 4,139,597.10 USD | `39,999.97` | `101.87` | `103.51` | `0.000000` | 64,745.58 USD | `+1.56%` | `20X Cross` |
| `538` | `0xd507...c948` | `LONG` | 4,122,567.95 USD | `39,808.50` | `93.57` | `103.51` | `81.34` | 397,492.54 USD | `+9.64%` | `7X Isolated` |
| `683` | `0xb5e7...eff1` | `SHORT` | 3,222,191.81 USD | `31,132.29` | `91.71` | `103.51` | `144.69` | -366,983.16 USD | `-11.39%` | `20X Cross` |
| `725` | `0xbd33...4200` | `SHORT` | 3,103,208.93 USD | `29,982.69` | `104.89` | `103.51` | `403.27` | 41,675.95 USD | `+1.34%` | `20X Cross` |
| `788` | `0x61d7...7dee` | `LONG` | 2,884,983.28 USD | `27,858.08` | `88.25` | `103.51` | `83.50` | 426,507.28 USD | `+14.78%` | `20X Cross` |
| `873` | `0xf0ae...2f74` | `SHORT` | 2,588,000.00 USD | `25,000.00` | `100.78` | `103.51` | `176.32` | -68,481.39 USD | `-2.65%` | `20X Cross` |
| `894` | `0x645b...87b8` | `SHORT` | 2,515,830.41 USD | `24,302.84` | `101.22` | `103.51` | `134.76` | -55,868.85 USD | `-2.22%` | `3X Isolated` |
| `947` | `0x58f0...0d20` | `SHORT` | 2,331,295.70 USD | `22,511.55` | `96.77` | `103.51` | `107.58` | -152,877.92 USD | `-6.56%` | `20X Cross` |
| `1061` | `0x9aa5...58af` | `SHORT` | 2,036,341.92 USD | `19,671.00` | `101.76` | `103.51` | `582.28` | -34,590.99 USD | `-1.70%` | `20X Cross` |
| `1232` | `0x4169...6f06` | `LONG` | 1,777,632.17 USD | `17,175.19` | `76.61` | `103.51` | `82.98` | 461,864.17 USD | `+25.98%` | `12X Isolated` |
| `1245` | `0x6788...98d4` | `SHORT` | 1,759,670.00 USD | `17,000.00` | `99.31` | `103.51` | `201.04` | -71,345.41 USD | `-4.05%` | `20X Cross` |
| `1294` | `0xa99c...40d5` | `SHORT` | 1,666,189.00 USD | `16,100.00` | `101.02` | `103.51` | `152.90` | -39,731.63 USD | `-2.38%` | `20X Cross` |
| `1299` | `0x1bf6...5bfa` | `SHORT` | 1,656,320.00 USD | `16,000.00` | `99.60` | `103.51` | `226.44` | -62,697.69 USD | `-3.79%` | `20X Cross` |
| `1335` | `0xe5dd...ecba` | `SHORT` | 1,612,378.87 USD | `15,575.53` | `102.71` | `103.51` | `144.81` | -12,623.49 USD | `-0.78%` | `20X Cross` |
| `1382` | `0x5d6f...6f8a` | `LONG` | 1,552,800.00 USD | `15,000.00` | `101.91` | `103.51` | `26.75` | 24,145.00 USD | `+1.55%` | `20X Cross` |
| `1383` | `0x34ea...2f47` | `SHORT` | 1,552,350.00 USD | `15,000.00` | `99.80` | `103.51` | `201.36` | -55,348.69 USD | `-3.57%` | `20X Cross` |
| `1462` | `0xfc27...9d9d` | `LONG` | 1,478,395.22 USD | `14,285.39` | `102.69` | `103.51` | `0.000000` | 11,494.94 USD | `+0.78%` | `20X Cross` |
| `1512` | `0xfb29...21dd` | `LONG` | 1,422,284.07 USD | `13,744.53` | `89.85` | `103.51` | `84.69` | 187,290.11 USD | `+13.17%` | `20X Cross` |
| `1533` | `0x6fa6...825e` | `SHORT` | 1,397,520.00 USD | `13,500.00` | `102.95` | `103.51` | `135.50` | -7,745.73 USD | `-0.55%` | `20X Isolated` |
| `1546` | `0xa9d9...b48e` | `SHORT` | 1,379,999.97 USD | `13,333.33` | `96.39` | `103.51` | `173.73` | -94,752.78 USD | `-6.87%` | `20X Cross` |
| `1601` | `0x936c...bb0f` | `SHORT` | 1,313,452.24 USD | `12,687.91` | `101.39` | `103.51` | `163.64` | -26,979.37 USD | `-2.05%` | `2X Isolated` |
| `1638` | `0x89c2...c94b` | `LONG` | 1,279,621.87 USD | `12,364.69` | `75.25` | `103.51` | `45.76` | 349,138.72 USD | `+27.28%` | `3X Isolated` |
| `1667` | `0xcd81...36e3` | `SHORT` | 1,248,499.63 USD | `12,063.96` | `97.96` | `103.51` | `109.05` | -66,660.71 USD | `-5.34%` | `20X Cross` |
| `1676` | `0x436c...b3d1` | `SHORT` | 1,242,120.00 USD | `12,000.00` | `101.05` | `103.51` | `210.30` | -29,460.17 USD | `-2.37%` | `20X Cross` |
| `1742` | `0x9dea...d617` | `LONG` | 1,180,210.61 USD | `11,400.80` | `90.37` | `103.51` | `7.33` | 149,936.89 USD | `+12.70%` | `20X Cross` |
| `1752` | `0x17c3...a868` | `LONG` | 1,170,119.72 USD | `11,306.60` | `95.13` | `103.51` | `64.99` | 94,472.86 USD | `+8.07%` | `3X Isolated` |
| `1795` | `0x0242...ffa1` | `LONG` | 1,138,820.10 USD | `11,000.97` | `104.43` | `103.51` | `0.000000` | -10,063.47 USD | `-0.88%` | `10X Cross` |
| `1796` | `0x8607...08d5` | `SHORT` | 1,138,523.52 USD | `10,998.10` | `92.18` | `103.51` | `135.02` | -124,733.82 USD | `-10.96%` | `4X Isolated` |
| `1881` | `0xb078...de15` | `LONG` | 1,063,791.71 USD | `10,276.19` | `104.67` | `103.51` | `0.000000` | -11,787.74 USD | `-1.11%` | `5X Cross` |

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
  * Current Rate: `-152.76K` | Last 24h: `-366.73K` | Last 3d: `-686.90K` | Last 7d: `-1.13M`
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
| `5:00 UTC` | `102.84` | `102.85` | `102.84` | `102.91` | `102.78` | 12,501,739.47 USD | 4,708,353.14 USD | 7,793,386.33 USD | -3,085,033.19 USD | `-24.68%` | `1B / 4S` |
| `0:00 UTC` | `102.80` | `102.83` | `102.80` | `102.93` | `102.75` | 11,683,758.36 USD | 3,517,048.40 USD | 8,166,709.96 USD | -4,649,661.56 USD | `-39.80%` | `1B / 5S` |
| `5:00 UTC` | `102.85` | `102.74` | `102.85` | `102.88` | `102.57` | 8,986,938.51 USD | 2,421,078.21 USD | 6,565,860.30 USD | -4,144,782.09 USD | `-46.12%` | `3B / 14S` |
| `0:00 UTC` | `102.78` | `102.78` | `102.78` | `103.02` | `102.57` | 31,355,759.70 USD | 14,370,056.44 USD | 16,985,703.26 USD | -2,615,646.82 USD | `-8.34%` | `6B / 5S` |
| `5:00 UTC` | `102.88` | `102.88` | `102.88` | `102.94` | `102.81` | 12,332,708.79 USD | 3,885,730.79 USD | 8,446,978.00 USD | -4,561,247.21 USD | `-36.98%` | `0B / 5S` |
| `0:00 UTC` | `104.23` | `103.97` | `104.23` | `104.72` | `102.88` | 80,432,525.97 USD | 47,963,579.07 USD | 32,468,946.89 USD | 15,494,632.18 USD | `+19.26%` | `55B / 11S` |
| `5:00 UTC` | `104.70` | `104.79` | `104.70` | `105.12` | `104.31` | 57,288,800.08 USD | 26,593,078.99 USD | 30,695,721.09 USD | -4,102,642.10 USD | `-7.16%` | `9B / 11S` |
| `0:00 UTC` | `104.60` | `104.57` | `104.60` | `104.78` | `104.25` | 37,381,511.82 USD | 18,039,773.84 USD | 19,341,737.99 USD | -1,301,964.15 USD | `-3.48%` | `2B / 5S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.60` | `103.70` | `103.60` | `103.94` | `103.56` | 15,977,044.60 USD | 8,854,335.52 USD | 7,122,709.08 USD | 1,731,626.44 USD | `+10.84%` | `3B / 4S` |

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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `102.47` (Risk Distance: `0.5804` pts)
  * +2.5R Take Profit: `104.50`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.58 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.83` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.42` (Risk Distance: `0.5804` pts)
  * +2.5R Take Profit: `103.38`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.58 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`105.02`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
