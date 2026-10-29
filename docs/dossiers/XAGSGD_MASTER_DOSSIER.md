# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGSGD
**Canonical Key**: `XAGSGD` | **Broker Instrument**: `XAGSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 23:13:20 IST` (`2026-10-29 17:43:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `66.78` | **Live Ask Quote**: `66.80` | **Mid Price**: `66.79`
- **Spread Points**: `16.00` | **Spread BPS**: `2.40 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `52.81` | VWAP Z-Score: `-1.09` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2415` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.24` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.38` | Lower -3.00σ Band: `51.23`
  * Upper +2.51σ Band: `54.12` | Lower -2.51σ Band: `51.49`
  * Upper +2.01σ Band: `53.86` | Lower -2.01σ Band: `51.75`
  * Upper +2.00σ Band: `53.85` | Lower -2.00σ Band: `51.76`
  * Upper +1.28σ Band: `53.48` | Lower -1.28σ Band: `52.13`
  * Upper +1.00σ Band: `53.33` | Lower -1.00σ Band: `52.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.37` | EMA-20=`52.44` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.67` (Slope: `+0.0000`) | EMA-100=`53.00`
  * Institutional Anchors: EMA-144=`53.17` | EMA-200=`53.32` (Slope: `-0.2096`) | EMA-233=`53.38`
- **Range Boundaries**: 24H High=`54.61` | 24H Low=`51.98` | Weekly High=`54.61` | Weekly Low=`51.98`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `53.02` (Distance: `-1.55%`)
  * Point of Control (POC) = `52.45` (Distance: `-0.47%`)
  * Value Area Low (VAL) = `52.03` (Distance: `+0.33%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`54.10` | POC=`53.83` | VAL=`53.54`
  * Prior Day Extremes: PDH=`54.61` | PDL=`53.28` | PDC=`53.94`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.48` | Weekly POC=`53.86` | Weekly VAL=`53.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`54.37` | Low=`52.98`
  * London Session (08:00-16:00 UTC): High=`53.50` | Low=`52.30`
  * New York Session (13:00-21:00 UTC): High=`53.07` | Low=`51.98`
  * Initial Balance (First Hour): IB High=`53.50` | IB Low=`52.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `66.52` - `67.06`
  * Optimal Trade Entry (OTE 0.705): `66.93`
  * Structural Invalidation Anchor (0.786): `67.33`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.19` | `52.22` | `52.03` | `52.16` | `3,117` | 162,573.37 USD | 10,950.54 USD | `+6.74%` | -763,960.87 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `52.16` | `52.48` | `52.14` | `52.42` | `3,355` | 175,865.74 USD | 121,455.67 USD | `+69.06%` | -642,505.20 USD | `+1.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.42` | `52.49` | `52.35` | `52.36` | `2,913` | 152,518.85 USD | -95,853.86 USD | `-62.85%` | -738,359.07 USD | `-0.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.05` | `52.35` | `51.98` | `52.24` | `9,551` | 498,953.79 USD | 227,811.80 USD | `+45.66%` | -1,596,664.76 USD | `+1.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.24` | `52.45` | `52.03` | `52.16` | `9,968` | 519,900.98 USD | -154,732.43 USD | `-29.76%` | -1,751,397.19 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.16` | `52.55` | `52.14` | `52.52` | `8,636` | 453,597.26 USD | 407,449.65 USD | `+89.83%` | -1,343,947.54 USD | `+2.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `BID` | `52.20` | `1157.2900` | 60,416.32 USD | 264,697.31 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.20` | `405.3500` | 21,160.89 USD | 285,858.21 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.20` | `518.4200` | 27,063.08 USD | 312,921.28 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.20` | `59.9300` | 3,128.41 USD | 316,049.69 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.20` | `172.7900` | 9,019.64 USD | 325,069.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.20` | `280.7500` | 14,654.87 USD | 339,724.20 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.20` | `6168.7200` | 321,994.85 USD | 661,719.04 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `52.20` | `1920.6700` | 100,253.21 USD | 761,972.26 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.21` | `153.4000` | 8,009.63 USD | 29,962.34 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.21` | `93.3900` | 4,876.17 USD | 34,838.51 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.21` | `137.9600` | 7,203.17 USD | 42,041.68 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `52.21` | `19.1500` | 999.84 USD | 43,041.52 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.21` | `259.6200` | 13,554.76 USD | 56,596.28 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.21` | `362.0200` | 18,900.70 USD | 75,496.98 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `409.9100` | 21,400.58 USD | 96,897.56 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `385.2000` | 20,110.14 USD | 117,007.70 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `52.21` | `1671.7100` | 87,273.29 USD | 204,280.99 USD | `3 orders` | `-0.02%` | `-` |
| `ASK` | `52.22` | `951.7700` | 49,705.24 USD | 172,720.21 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.22` | `273.1900` | 14,266.80 USD | 123,014.97 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `52.22` | `51.3100` | 2,679.51 USD | 108,748.17 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.22` | `354.1400` | 18,493.54 USD | 106,068.66 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.22` | `153.6100` | 8,021.51 USD | 87,575.12 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.22` | `0.2000` | 10.44 USD | 79,553.60 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.22` | `1523.2900` | 79,543.16 USD | 79,543.16 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.22` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.22` | `0.00%` | `-` |
| `BID` | `52.22` | `173.6300` | 9,066.44 USD | 9,066.44 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `52.22` | `131.7400` | 6,878.94 USD | 15,945.37 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.22` | `115.0500` | 6,007.34 USD | 21,952.71 USD | `1 orders` | `-0.00%` | `-` |
| `ASK` | `52.23` | `369.7500` | 19,313.89 USD | 1,395,979.34 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.23` | `9666.3400` | 504,911.60 USD | 1,376,665.45 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `52.23` | `6311.7900` | 329,683.73 USD | 871,753.84 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.23` | `1987.7100` | 103,822.07 USD | 542,070.12 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `52.23` | `128.2400` | 6,698.10 USD | 438,248.05 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.23` | `133.3900` | 6,966.96 USD | 431,549.94 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `269.5200` | 14,076.76 USD | 424,582.98 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `412.1400` | 21,525.25 USD | 410,506.22 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `93.4200` | 4,879.05 USD | 388,980.98 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `3644.3900` | 190,331.91 USD | 384,101.93 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `52.23` | `403.0600` | 21,049.81 USD | 193,770.02 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `52.24` | `62.9100` | 3,286.23 USD | 1,427,116.24 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `52.24` | `533.1700` | 27,850.67 USD | 1,423,830.01 USD | `4 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `117` | `0x5b5d...c060` | `SHORT` | 17,425,188.82 USD | `333,790.30` | `59.15` | `52.20` | `516.84` | 2,317,845.13 USD | `+13.30%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,355,318.56 USD | `313,344.29` | `53.41` | `52.20` | `237.73` | 380,845.99 USD | `+2.33%` | `5X Cross` |
| `181` | `0x49e9...e1d0` | `SHORT` | 11,757,924.63 USD | `225,264.86` | `55.61` | `52.20` | `88.36` | 768,079.26 USD | `+6.53%` | `4X Cross` |
| `213` | `0xacb6...efbd` | `SHORT` | 10,497,953.03 USD | `201,133.33` | `59.63` | `52.20` | `76.49` | 1,494,704.09 USD | `+14.24%` | `6X Cross` |
| `251` | `0xc26c...b8f4` | `LONG` | 9,473,115.86 USD | `181,463.41` | `55.43` | `52.20` | `0.000000` | -585,639.22 USD | `-6.18%` | `2X Cross` |
| `370` | `0xd8c5...99b0` | `SHORT` | 6,596,053.53 USD | `126,320.04` | `61.98` | `52.20` | `194.17` | 1,233,284.32 USD | `+18.70%` | `3X Cross` |
| `373` | `0x645b...87b8` | `LONG` | 6,587,737.54 USD | `126,211.54` | `56.64` | `52.20` | `0.000000` | -560,620.01 USD | `-8.51%` | `3X Cross` |
| `407` | `0xe9ff...5903` | `SHORT` | 5,901,333.27 USD | `112,996.08` | `60.07` | `52.20` | `196.30` | 886,617.53 USD | `+15.02%` | `5X Cross` |
| `436` | `0xfc66...ca06` | `SHORT` | 5,523,425.61 USD | `105,820.86` | `54.61` | `52.20` | `444.81` | 255,041.66 USD | `+4.62%` | `3X Cross` |
| `492` | `0x354b...6425` | `LONG` | 4,876,115.35 USD | `93,419.33` | `52.46` | `52.20` | `0.000000` | -24,535.53 USD | `-0.50%` | `10X Cross` |
| `597` | `0x4e23...20c3` | `SHORT` | 3,980,147.36 USD | `76,258.26` | `52.44` | `52.20` | `215.91` | 19,064.56 USD | `+0.48%` | `16X Cross` |
| `638` | `0x9aa5...58af` | `LONG` | 3,718,408.34 USD | `71,243.43` | `61.59` | `52.20` | `0.000000` | -669,749.18 USD | `-18.01%` | `20X Cross` |
| `757` | `0x2056...8396` | `LONG` | 3,131,580.00 USD | `60,000.00` | `66.92` | `52.20` | `21.34` | -883,747.14 USD | `-28.22%` | `10X Cross` |
| `892` | `0x0242...ffa1` | `SHORT` | 2,605,450.51 USD | `49,916.67` | `56.48` | `52.20` | `270.34` | 213,681.36 USD | `+8.20%` | `10X Cross` |
| `903` | `0x960b...f0fc` | `LONG` | 2,581,903.34 USD | `49,457.96` | `55.82` | `52.20` | `0.000000` | -179,033.69 USD | `-6.93%` | `25X Cross` |
| `992` | `0x8b9d...7b28` | `LONG` | 2,341,085.01 USD | `44,823.47` | `58.35` | `52.20` | `0.000000` | -274,363.53 USD | `-11.72%` | `10X Cross` |
| `1082` | `0x5647...e7de` | `LONG` | 2,101,519.01 USD | `40,262.07` | `57.38` | `52.20` | `0.000000` | -208,718.59 USD | `-9.93%` | `20X Cross` |
| `1090` | `0xa2ce...3126` | `LONG` | 2,089,160.00 USD | `40,000.00` | `74.30` | `52.20` | `0.000000` | -882,895.49 USD | `-42.26%` | `20X Cross` |
| `1469` | `0x3678...b209` | `LONG` | 1,566,690.00 USD | `30,000.00` | `57.15` | `52.20` | `0.000000` | -147,810.00 USD | `-9.43%` | `20X Cross` |
| `1470` | `0x5a88...d997` | `LONG` | 1,566,630.00 USD | `30,000.00` | `59.50` | `52.20` | `36.91` | -218,257.59 USD | `-13.93%` | `25X Cross` |
| `1705` | `0x7ea9...fc7f` | `LONG` | 1,305,675.00 USD | `25,000.00` | `53.60` | `52.20` | `18.31` | -34,329.05 USD | `-2.63%` | `25X Cross` |
| `1761` | `0xce97...7e78` | `LONG` | 1,238,788.02 USD | `23,733.39` | `52.42` | `52.20` | `0.000000` | -5,383.35 USD | `-0.43%` | `5X Cross` |
| `1821` | `0xf517...c032` | `LONG` | 1,181,019.74 USD | `22,627.50` | `66.29` | `52.20` | `0.000000` | -318,975.37 USD | `-27.01%` | `20X Cross` |
| `1954` | `0xcc9f...d218` | `LONG` | 1,071,052.20 USD | `20,520.60` | `52.63` | `52.20` | `26.85` | -8,855.85 USD | `-0.83%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.86` (Vol: 3,800,000.00 USD, Dist: `+2.85%`) | Long MP=`51.93` (Vol: 2,700,000.00 USD, Dist: `--0.84%`)
  * 48H Horizon: Short MP=`54.97` (Vol: 4,800,000.00 USD, Dist: `+4.96%`) | Long MP=`51.93` (Vol: 2,400,000.00 USD, Dist: `--0.84%`)
  * 3D Horizon: Short MP=`55.10` (Vol: 5,400,000.00 USD, Dist: `+5.22%`) | Long MP=`51.93` (Vol: 5,000,000.00 USD, Dist: `--0.84%`)
  * 7D Horizon: Short MP=`55.10` (Vol: 8,800,000.00 USD, Dist: `+5.21%`) | Long MP=`51.93` (Vol: 6,700,000.00 USD, Dist: `--0.84%`)
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
  * Current Rate: `47.00K` | Last 24h: `163.44K` | Last 3d: `421.23K` | Last 7d: `760.43K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0075%` | **USDT BingX** | `-` |
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `51.72` (Risk Distance: `0.3138` pts)
  * +2.5R Take Profit: `52.82`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `53.02` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `53.33` (Risk Distance: `0.3138` pts)
  * +2.5R Take Profit: `52.24`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.02 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`67.33`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
