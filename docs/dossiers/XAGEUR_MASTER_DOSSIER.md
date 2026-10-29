# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGEUR
**Canonical Key**: `XAGEUR` | **Broker Instrument**: `XAGEUR.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 01:02:38 IST` (`2026-10-29 19:32:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.07` | **Live Ask Quote**: `52.11` | **Mid Price**: `52.09`
- **Spread Points**: `36.00` | **Spread BPS**: `6.91 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `52.76` | VWAP Z-Score: `-1.40` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2007` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.68` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.38` | Lower -3.00σ Band: `51.14`
  * Upper +2.51σ Band: `54.11` | Lower -2.51σ Band: `51.40`
  * Upper +2.01σ Band: `53.84` | Lower -2.01σ Band: `51.67`
  * Upper +2.00σ Band: `53.84` | Lower -2.00σ Band: `51.68`
  * Upper +1.28σ Band: `53.45` | Lower -1.28σ Band: `52.06`
  * Upper +1.00σ Band: `53.30` | Lower -1.00σ Band: `52.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.10` | EMA-20=`52.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.51` (Slope: `+0.0000`) | EMA-100=`52.87`
  * Institutional Anchors: EMA-144=`53.06` | EMA-200=`53.23` (Slope: `-0.2567`) | EMA-233=`53.30`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.96` (Distance: `-1.65%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.71%`)
  * Value Area Low (VAL) = `51.99` (Distance: `+0.19%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.23`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.88` - `52.30`
  * Optimal Trade Entry (OTE 0.705): `52.19`
  * Structural Invalidation Anchor (0.786): `52.51`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.36` | `52.41` | `52.26` | `52.39` | `2,104` | 110,230.66 USD | 49,815.78 USD | `+45.19%` | -592,466.86 USD | `+0.91` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.39` | `52.43` | `52.35` | `52.42` | `1,277` | 66,937.79 USD | 38,512.15 USD | `+57.53%` | -553,954.71 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.42` | `52.47` | `52.39` | `52.46` | `1,426` | 74,810.81 USD | 52,950.51 USD | `+70.78%` | -501,004.20 USD | `+1.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.47` | `52.65` | `52.32` | `52.51` | `5,216` | 273,871.30 USD | 33,811.27 USD | `+12.35%` | -1,306,009.14 USD | `+0.31` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `52.51` | `52.51` | `52.26` | `52.39` | `5,381` | 281,915.97 USD | -53,564.03 USD | `-19.00%` | -1,359,573.18 USD | `-0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.39` | `52.48` | `52.35` | `52.40` | `4,100` | 214,823.60 USD | -25,957.85 USD | `-12.08%` | -1,385,531.03 USD | `+0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -679,727.93 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.61` | `52.65` | `52.32` | `52.51` | `20,260` | 1,063,771.56 USD | -103,422.23 USD | `-9.72%` | -783,150.17 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `52.51` | `52.51` | `52.26` | `52.42` | `15,925` | 834,740.72 USD | -28,381.18 USD | `-3.40%` | -811,531.35 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `53.52` | `54.09` | `53.37` | `53.37` | `22,849` | 1,219,382.58 USD | -735,688.52 USD | `-60.33%` | -336,770.30 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,495,594.11 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -2,786,118.52 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -4,826,166.37 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,279,386.10 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `52.08` | `191.9400` | 9,997.00 USD | 273,994.69 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.08` | `628.5400` | 32,736.25 USD | 306,730.94 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.08` | `84.3900` | 4,395.20 USD | 311,126.14 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `52.09` | `16.8200` | 876.24 USD | 21,550.25 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.09` | `172.2000` | 8,970.59 USD | 30,520.84 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `16.5100` | 860.06 USD | 31,380.89 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `238.2000` | 12,408.31 USD | 43,789.21 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `532.1400` | 27,719.70 USD | 71,508.91 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `1754.7400` | 91,404.41 USD | 162,913.32 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `427.4600` | 22,265.96 USD | 185,179.28 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `144.6400` | 7,534.01 USD | 192,713.29 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `133.4700` | 6,952.05 USD | 199,665.34 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `80.4800` | 4,191.88 USD | 203,857.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `1154.6600` | 60,140.47 USD | 263,997.69 USD | `3 orders` | `-0.03%` | `-` |
| `ASK` | `52.10` | `330.1100` | 17,200.38 USD | 184,143.50 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `52.10` | `1460.9700` | 76,122.38 USD | 166,943.12 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `52.10` | `1743.1000` | 90,820.74 USD | 90,820.74 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.10` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.10` | `0.00%` | `-` |
| `BID` | `52.10` | `40.1900` | 2,093.98 USD | 2,093.98 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.10` | `76.5200` | 3,986.69 USD | 6,080.67 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.10` | `65.4400` | 3,409.36 USD | 9,490.03 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.10` | `1.3100` | 68.25 USD | 9,558.28 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.10` | `10.8500` | 565.25 USD | 10,123.53 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.10` | `202.5200` | 10,550.48 USD | 20,674.01 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `52.11` | `5800.8600` | 302,306.02 USD | 908,677.20 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `683.8000` | 35,634.87 USD | 606,371.19 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `2560.4800` | 133,431.73 USD | 570,736.32 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `206.6400` | 10,768.22 USD | 437,304.58 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `3209.2300` | 167,232.98 USD | 426,536.37 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `263.9000` | 13,751.57 USD | 259,303.39 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `299.3800` | 15,600.09 USD | 245,551.82 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `803.3300` | 41,859.12 USD | 229,951.73 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `75.7900` | 3,949.11 USD | 188,092.62 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.12` | `43.9800` | 2,292.37 USD | 1,843,784.24 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.12` | `5788.2500` | 301,689.38 USD | 1,841,491.87 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `52.12` | `833.7900` | 43,457.13 USD | 1,539,802.50 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `835.3900` | 43,539.69 USD | 1,496,345.36 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `5876.3200` | 306,262.05 USD | 1,452,805.67 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `176.6100` | 9,204.38 USD | 1,146,543.62 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `177.6800` | 9,259.97 USD | 1,137,339.24 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `4209.9600` | 219,402.07 USD | 1,128,079.27 USD | `3 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,415,175.11 USD | `333,790.30` | `59.15` | `52.17` | `535.04` | 2,327,858.84 USD | `+13.37%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,251,507.61 USD | `311,486.71` | `53.37` | `52.17` | `239.93` | 373,756.13 USD | `+2.30%` | `5X Cross` |
| `177` | `0x49e9...e1d0` | `SHORT` | 11,693,672.75 USD | `224,132.65` | `55.61` | `52.17` | `87.92` | 769,373.85 USD | `+6.58%` | `4X Cross` |
| `208` | `0xacb6...efbd` | `SHORT` | 10,484,275.96 USD | `201,133.33` | `59.63` | `52.17` | `76.54` | 1,508,381.16 USD | `+14.39%` | `6X Cross` |
| `247` | `0xc26c...b8f4` | `LONG` | 9,467,671.95 USD | `181,463.41` | `55.43` | `52.17` | `0.000000` | -591,083.13 USD | `-6.24%` | `2X Cross` |
| `367` | `0x645b...87b8` | `LONG` | 6,590,095.85 USD | `126,309.96` | `56.63` | `52.17` | `0.000000` | -563,385.03 USD | `-8.55%` | `3X Cross` |
| `368` | `0xd8c5...99b0` | `SHORT` | 6,589,737.53 USD | `126,320.04` | `61.98` | `52.17` | `194.63` | 1,239,600.32 USD | `+18.81%` | `3X Cross` |
| `403` | `0xe9ff...5903` | `SHORT` | 5,891,954.60 USD | `112,996.08` | `60.07` | `52.17` | `196.71` | 895,996.20 USD | `+15.21%` | `5X Cross` |
| `432` | `0xfc66...ca06` | `SHORT` | 5,409,607.97 USD | `103,683.98` | `54.61` | `52.17` | `454.36` | 252,172.55 USD | `+4.66%` | `3X Cross` |
| `598` | `0x4e23...20c3` | `SHORT` | 3,897,490.02 USD | `74,733.28` | `52.44` | `52.17` | `221.63` | 21,747.38 USD | `+0.56%` | `16X Cross` |
| `613` | `0x354b...6425` | `LONG` | 3,820,684.62 USD | `73,231.07` | `52.43` | `52.17` | `0.000000` | -18,702.92 USD | `-0.49%` | `10X Cross` |
| `630` | `0x9aa5...58af` | `LONG` | 3,713,421.30 USD | `71,243.43` | `61.59` | `52.17` | `0.000000` | -674,736.22 USD | `-18.17%` | `20X Cross` |
| `751` | `0x2056...8396` | `LONG` | 3,127,380.00 USD | `60,000.00` | `66.92` | `52.17` | `21.34` | -887,947.14 USD | `-28.39%` | `10X Cross` |
| `876` | `0x0242...ffa1` | `SHORT` | 2,604,352.34 USD | `49,916.67` | `56.48` | `52.17` | `281.69` | 214,779.52 USD | `+8.25%` | `10X Cross` |
| `884` | `0x960b...f0fc` | `LONG` | 2,580,419.60 USD | `49,457.96` | `55.82` | `52.17` | `0.000000` | -180,517.42 USD | `-7.00%` | `25X Cross` |
| `980` | `0x8b9d...7b28` | `LONG` | 2,336,288.90 USD | `44,823.47` | `58.35` | `52.17` | `0.000000` | -279,159.64 USD | `-11.95%` | `10X Cross` |
| `1073` | `0x5647...e7de` | `LONG` | 2,098,781.19 USD | `40,262.07` | `57.38` | `52.17` | `0.000000` | -211,456.42 USD | `-10.08%` | `20X Cross` |
| `1081` | `0xa2ce...3126` | `LONG` | 2,085,640.00 USD | `40,000.00` | `74.30` | `52.17` | `0.000000` | -886,415.49 USD | `-42.50%` | `20X Cross` |
| `1419` | `0xce97...7e78` | `LONG` | 1,610,882.68 USD | `30,875.20` | `52.22` | `52.17` | `0.000000` | -1,311.75 USD | `-0.08%` | `5X Cross` |
| `1452` | `0x3678...b209` | `LONG` | 1,565,190.00 USD | `30,000.00` | `57.15` | `52.17` | `0.000000` | -149,310.00 USD | `-9.54%` | `20X Cross` |
| `1453` | `0x5a88...d997` | `LONG` | 1,565,010.00 USD | `30,000.00` | `59.50` | `52.17` | `37.69` | -219,877.59 USD | `-14.05%` | `25X Cross` |
| `1678` | `0x7ea9...fc7f` | `LONG` | 1,303,050.00 USD | `25,000.00` | `53.60` | `52.17` | `18.27` | -36,954.05 USD | `-2.84%` | `25X Cross` |
| `1801` | `0xf517...c032` | `LONG` | 1,179,481.06 USD | `22,627.50` | `66.29` | `52.17` | `0.000000` | -320,514.04 USD | `-27.17%` | `20X Cross` |
| `1918` | `0xcc9f...d218` | `LONG` | 1,069,656.80 USD | `20,520.60` | `52.63` | `52.17` | `26.86` | -10,251.25 USD | `-0.96%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `81.27` | 429.11 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 0.43K USD at 81.2710 USD [API] | `2026-02-01 23:01:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.52` (Vol: 3,600,000.00 USD, Dist: `+2.51%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.02%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.50%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.02%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.50%`) | Long MP=`51.96` (Vol: 4,300,000.00 USD, Dist: `--0.49%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+5.01%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.48%`)
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
  * Current Rate: `65.77K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0116%` | **USDT BingX** | `-` |
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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `51.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.69` (Risk Distance: `0.2948` pts)
  * +2.5R Take Profit: `52.72`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.96` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.25` (Risk Distance: `0.2948` pts)
  * +2.5R Take Profit: `52.22`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
