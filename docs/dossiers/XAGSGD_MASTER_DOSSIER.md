# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 22:49:01 IST` (`2026-10-29 17:19:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `67.03` | **Live Ask Quote**: `67.04` | **Mid Price**: `67.03`
- **Spread Points**: `9.00` | **Spread BPS**: `1.34 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `52.82` | VWAP Z-Score: `-0.76` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2513` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.98` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.39` | Lower -3.00σ Band: `51.24`
  * Upper +2.51σ Band: `54.13` | Lower -2.51σ Band: `51.50`
  * Upper +2.01σ Band: `53.87` | Lower -2.01σ Band: `51.76`
  * Upper +2.00σ Band: `53.87` | Lower -2.00σ Band: `51.77`
  * Upper +1.28σ Band: `53.49` | Lower -1.28σ Band: `52.15`
  * Upper +1.00σ Band: `53.34` | Lower -1.00σ Band: `52.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.43` | EMA-20=`52.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.70` (Slope: `+0.0000`) | EMA-100=`53.03`
  * Institutional Anchors: EMA-144=`53.20` | EMA-200=`53.34` (Slope: `-0.2103`) | EMA-233=`53.40`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.98` | Weekly High=`54.61` | Weekly Low=`51.98`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `53.07` (Distance: `-1.37%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.20%`)
  * Value Area Low (VAL) = `52.03` (Distance: `+0.60%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.48` | Weekly POC=`53.86` | Weekly VAL=`53.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.76` - `67.30`
  * Optimal Trade Entry (OTE 0.705): `67.17`
  * Structural Invalidation Anchor (0.786): `67.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.24` | `52.43` | `52.24` | `52.40` | `3,543` | 185,656.74 USD | 148,023.62 USD | `+79.73%` | -671,487.69 USD | `+1.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.40` | `52.45` | `52.12` | `52.19` | `3,308` | 172,651.14 USD | -103,329.09 USD | `-59.85%` | -774,816.78 USD | `-0.99` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `52.19` | `52.22` | `52.03` | `52.16` | `3,117` | 162,573.37 USD | 10,950.54 USD | `+6.74%` | -763,866.24 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `52.31` | `52.52` | `52.03` | `52.05` | `12,846` | 668,582.92 USD | -492,568.23 USD | `-73.67%` | -1,957,334.03 USD | `-2.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.05` | `52.35` | `51.98` | `52.24` | `9,551` | 498,953.79 USD | 227,811.80 USD | `+45.66%` | -1,729,522.24 USD | `+1.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.24` | `52.45` | `52.03` | `52.16` | `9,968` | 519,900.98 USD | -154,732.43 USD | `-29.76%` | -1,884,254.67 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.36` | `52.72` | `52.30` | `52.37` | `22,190` | 1,162,090.30 USD | -379,003.07 USD | `-32.61%` | -1,358,348.37 USD | `-0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `52.37` | `52.61` | `51.98` | `52.24` | `41,435` | 2,164,605.83 USD | -391,069.83 USD | `-18.07%` | -1,749,418.20 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.24` | `52.76` | `52.03` | `52.61` | `32,755` | 1,723,273.30 USD | 951,587.73 USD | `+55.22%` | -797,830.47 USD | `+1.89` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `52.34` | `800.6700` | 41,911.07 USD | 152,125.80 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.34` | `540.8700` | 28,311.30 USD | 180,437.10 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `52.34` | `421.5500` | 22,065.19 USD | 202,502.29 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.34` | `804.7200` | 42,120.65 USD | 244,622.94 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `52.34` | `166.7100` | 8,725.77 USD | 253,348.71 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.34` | `188.1000` | 9,845.15 USD | 263,193.87 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.34` | `518.4200` | 27,133.58 USD | 290,327.45 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.34` | `282.2600` | 14,772.92 USD | 305,100.37 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.34` | `1229.1600` | 64,330.55 USD | 369,430.92 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.35` | `55.5400` | 2,907.80 USD | 2,976.91 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.35` | `141.7200` | 7,419.61 USD | 10,396.52 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.35` | `1.0100` | 52.88 USD | 10,449.39 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.35` | `19.1000` | 999.92 USD | 11,449.32 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.35` | `464.7600` | 24,330.65 USD | 35,779.97 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.35` | `116.5200` | 6,099.82 USD | 41,879.79 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.35` | `307.2300` | 16,083.18 USD | 57,962.97 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.35` | `215.3100` | 11,271.05 USD | 69,234.02 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.35` | `595.7800` | 31,187.30 USD | 100,421.31 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `52.35` | `187.0900` | 9,793.41 USD | 110,214.73 USD | `2 orders` | `-0.02%` | `-` |
| `ASK` | `52.36` | `949.6900` | 49,729.57 USD | 429,396.59 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.36` | `728.3700` | 38,139.64 USD | 379,667.03 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.36` | `3744.0600` | 196,046.47 USD | 341,527.39 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `52.36` | `310.3400` | 16,249.71 USD | 145,480.92 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.36` | `108.0500` | 5,657.50 USD | 129,231.21 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.36` | `61.8700` | 3,239.45 USD | 123,573.71 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `52.36` | `70.2700` | 3,679.20 USD | 120,334.26 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.36` | `2228.0700` | 116,655.06 USD | 116,655.06 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.36` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.36` | `0.00%` | `-` |
| `BID` | `52.36` | `1.3200` | 69.11 USD | 69.11 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `52.37` | `6226.1700` | 326,083.20 USD | 1,144,278.96 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.37` | `1905.0400` | 99,770.75 USD | 818,195.76 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.37` | `4.7400` | 248.24 USD | 718,425.00 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.37` | `271.3100` | 14,208.23 USD | 718,176.77 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.37` | `4081.8200` | 213,756.75 USD | 703,968.53 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.37` | `384.0000` | 20,108.93 USD | 490,211.78 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `52.37` | `327.1900` | 17,133.63 USD | 470,102.85 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.37` | `450.1600` | 23,572.63 USD | 452,969.22 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.38` | `114.6600` | 6,005.66 USD | 1,288,223.96 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.38` | `147.9500` | 7,749.18 USD | 1,282,218.30 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.38` | `1099.3300` | 57,578.51 USD | 1,274,469.12 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.38` | `1386.3800` | 72,611.65 USD | 1,216,890.61 USD | `5 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `117` | `0x5b5d...c060` | `SHORT` | 17,468,915.35 USD | `333,790.30` | `59.15` | `52.34` | `518.82` | 2,274,118.60 USD | `+13.02%` | `5X Cross` |
| `123` | `0x4692...164f` | `SHORT` | 16,501,105.94 USD | `315,364.00` | `53.43` | `52.34` | `236.35` | 348,088.20 USD | `+2.11%` | `5X Cross` |
| `183` | `0x49e9...e1d0` | `SHORT` | 11,789,461.71 USD | `225,264.86` | `55.61` | `52.34` | `89.34` | 736,542.18 USD | `+6.25%` | `4X Cross` |
| `216` | `0xacb6...efbd` | `SHORT` | 10,524,502.63 USD | `201,133.33` | `59.63` | `52.34` | `76.49` | 1,468,154.49 USD | `+13.95%` | `6X Cross` |
| `255` | `0xc26c...b8f4` | `LONG` | 9,498,520.73 USD | `181,463.41` | `55.43` | `52.34` | `0.000000` | -560,234.35 USD | `-5.90%` | `2X Cross` |
| `373` | `0xd8c5...99b0` | `SHORT` | 6,611,464.57 USD | `126,320.04` | `61.98` | `52.34` | `193.87` | 1,217,873.27 USD | `+18.42%` | `3X Cross` |
| `374` | `0x645b...87b8` | `LONG` | 6,606,416.85 USD | `126,211.54` | `56.64` | `52.34` | `0.000000` | -541,940.70 USD | `-8.20%` | `3X Cross` |
| `409` | `0xe9ff...5903` | `SHORT` | 5,911,615.92 USD | `112,996.08` | `60.07` | `52.34` | `196.21` | 876,334.89 USD | `+14.82%` | `5X Cross` |
| `416` | `0x354b...6425` | `LONG` | 5,777,974.50 USD | `110,426.85` | `52.46` | `52.34` | `0.000000` | -14,867.73 USD | `-0.26%` | `10X Cross` |
| `436` | `0xfc66...ca06` | `SHORT` | 5,609,491.80 USD | `107,208.91` | `54.61` | `52.34` | `436.07` | 244,771.50 USD | `+4.36%` | `3X Cross` |
| `597` | `0x4e23...20c3` | `SHORT` | 3,991,052.30 USD | `76,258.26` | `52.44` | `52.34` | `216.02` | 8,159.63 USD | `+0.20%` | `16X Cross` |
| `639` | `0x9aa5...58af` | `LONG` | 3,727,883.72 USD | `71,243.43` | `61.59` | `52.34` | `0.000000` | -660,273.81 USD | `-17.71%` | `20X Cross` |
| `754` | `0x2056...8396` | `LONG` | 3,139,560.00 USD | `60,000.00` | `66.92` | `52.34` | `21.34` | -875,767.14 USD | `-27.89%` | `10X Cross` |
| `892` | `0x0242...ffa1` | `SHORT` | 2,611,789.92 USD | `49,916.67` | `56.48` | `52.34` | `266.59` | 207,341.94 USD | `+7.94%` | `10X Cross` |
| `903` | `0x960b...f0fc` | `LONG` | 2,588,382.34 USD | `49,457.96` | `55.82` | `52.34` | `0.000000` | -172,554.69 USD | `-6.67%` | `25X Cross` |
| `994` | `0x8b9d...7b28` | `LONG` | 2,345,029.48 USD | `44,823.47` | `58.35` | `52.34` | `0.0269` | -270,419.06 USD | `-11.53%` | `10X Cross` |
| `1079` | `0x5647...e7de` | `LONG` | 2,106,833.60 USD | `40,262.07` | `57.38` | `52.34` | `0.000000` | -203,404.00 USD | `-9.65%` | `20X Cross` |
| `1090` | `0xa2ce...3126` | `LONG` | 2,093,680.00 USD | `40,000.00` | `74.30` | `52.34` | `0.000000` | -878,375.49 USD | `-41.95%` | `20X Cross` |
| `1463` | `0x3678...b209` | `LONG` | 1,570,170.00 USD | `30,000.00` | `57.15` | `52.34` | `0.000000` | -144,330.00 USD | `-9.19%` | `20X Cross` |
| `1464` | `0x5a88...d997` | `LONG` | 1,569,810.00 USD | `30,000.00` | `59.50` | `52.34` | `36.89` | -215,077.59 USD | `-13.70%` | `25X Cross` |
| `1699` | `0x7ea9...fc7f` | `LONG` | 1,308,550.00 USD | `25,000.00` | `53.60` | `52.34` | `18.33` | -31,454.05 USD | `-2.40%` | `25X Cross` |
| `1763` | `0xce97...7e78` | `LONG` | 1,239,831.60 USD | `23,694.37` | `52.43` | `52.34` | `0.000000` | -2,406.78 USD | `-0.19%` | `5X Cross` |
| `1826` | `0xf517...c032` | `LONG` | 1,184,006.56 USD | `22,627.50` | `66.29` | `52.34` | `0.000000` | -315,988.54 USD | `-26.69%` | `20X Cross` |
| `1952` | `0xcc9f...d218` | `LONG` | 1,073,760.92 USD | `20,520.60` | `52.63` | `52.34` | `26.85` | -6,147.13 USD | `-0.57%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.86` (Vol: 3,800,000.00 USD, Dist: `+2.44%`) | Long MP=`51.93` (Vol: 2,700,000.00 USD, Dist: `--1.24%`)
  * 48H Horizon: Short MP=`54.97` (Vol: 4,800,000.00 USD, Dist: `+4.54%`) | Long MP=`51.93` (Vol: 2,400,000.00 USD, Dist: `--1.24%`)
  * 3D Horizon: Short MP=`55.10` (Vol: 5,400,000.00 USD, Dist: `+4.80%`) | Long MP=`51.93` (Vol: 5,000,000.00 USD, Dist: `--1.24%`)
  * 7D Horizon: Short MP=`54.85` (Vol: 8,300,000.00 USD, Dist: `+4.32%`) | Long MP=`51.85` (Vol: 5,600,000.00 USD, Dist: `--1.39%`)
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
  * Current Rate: `39.75K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0062%` | **USDT BingX** | `-` |
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `52.03` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.72` (Risk Distance: `0.3151` pts)
  * +2.5R Take Profit: `52.82`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `53.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.38` (Risk Distance: `0.3151` pts)
  * +2.5R Take Profit: `52.28`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
