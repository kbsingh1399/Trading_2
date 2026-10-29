# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGUSD
**Canonical Key**: `XAGUSD` | **Broker Instrument**: `XAGUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-30 04:01:40 IST` (`2026-10-29 22:31:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `52.05` | **Live Ask Quote**: `52.09` | **Mid Price**: `52.07`
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
  * Session VWAP: `52.73` | VWAP Z-Score: `-1.11` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1753` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `54.35` | Lower -3.00σ Band: `51.11`
  * Upper +2.51σ Band: `54.08` | Lower -2.51σ Band: `51.37`
  * Upper +2.01σ Band: `53.81` | Lower -2.01σ Band: `51.64`
  * Upper +2.00σ Band: `53.81` | Lower -2.00σ Band: `51.65`
  * Upper +1.28σ Band: `53.42` | Lower -1.28σ Band: `52.04`
  * Upper +1.00σ Band: `53.27` | Lower -1.00σ Band: `52.19`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`52.17` | EMA-20=`52.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`52.43` (Slope: `+0.0000`) | EMA-100=`52.77`
  * Institutional Anchors: EMA-144=`52.97` | EMA-200=`53.16` (Slope: `-0.2431`) | EMA-233=`53.24`
- **Range Boundaries**: 24H High=`54.37` | 24H Low=`51.95` | Weekly High=`54.61` | Weekly Low=`51.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.16` (Distance: `-0.16%`)
  * Point of Control (POC) = `52.12` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `52.06` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.49` | Weekly POC=`53.89` | Weekly VAL=`53.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`52.05`
  * London Session (08:00-16:00 UTC): High=`52.28` | Low=`51.86`
  * New York Session (13:00-21:00 UTC): High=`52.38` | Low=`51.76`
  * Initial Balance (First Hour): IB High=`52.23` | IB Low=`51.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `51.86` - `52.28`
  * Optimal Trade Entry (OTE 0.705): `52.18`
  * Structural Invalidation Anchor (0.786): `52.49`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `52.00` | `52.07` | `51.98` | `52.05` | `742` | 38,623.33 USD | 25,510.47 USD | `+66.05%` | -788,718.67 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.05` | `52.11` | `52.05` | `52.11` | `527` | 27,460.92 USD | 23,696.11 USD | `+86.29%` | -765,022.55 USD | `+0.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `52.11` | `52.18` | `52.11` | `52.14` | `619` | 32,274.04 USD | 5,302.16 USD | `+16.43%` | -759,720.39 USD | `+0.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `51.99` | `52.08` | `51.96` | `52.08` | `2,217` | 115,450.28 USD | 88,953.49 USD | `+77.05%` | -1,698,464.50 USD | `+0.67` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `52.08` | `52.10` | `51.99` | `52.00` | `2,318` | 120,533.68 USD | -96,314.30 USD | `-79.91%` | -1,794,778.80 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `52.00` | `52.18` | `51.98` | `52.14` | `1,888` | 98,438.43 USD | 64,520.53 USD | `+65.54%` | -1,730,258.28 USD | `+0.84` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.42` | `52.51` | `51.97` | `52.01` | `15,397` | 800,720.98 USD | -646,338.43 USD | `-80.72%` | -2,335,773.51 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `52.01` | `52.12` | `51.95` | `52.08` | `9,961` | 518,719.08 USD | 235,233.07 USD | `+45.35%` | -2,100,540.44 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `52.08` | `52.36` | `51.98` | `52.35` | `8,673` | 454,014.20 USD | 384,260.00 USD | `+84.64%` | -1,716,280.44 USD | `+1.13` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.37` | `54.37` | `52.98` | `53.22` | `57,426` | 3,056,384.00 USD | -1,158,823.80 USD | `-37.91%` | -1,894,512.32 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `53.22` | `53.50` | `52.45` | `52.73` | `52,817` | 2,785,304.50 USD | -1,290,524.42 USD | `-46.33%` | -3,185,036.74 USD | `-0.97` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.74` | `53.07` | `52.30` | `52.37` | `60,050` | 3,144,818.50 USD | -2,040,047.85 USD | `-64.87%` | -5,225,084.59 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -4,678,304.31 USD | `+1.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -5,671,615.22 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `52.08` | `83.3000` | 4,338.60 USD | 519,683.46 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.08` | `74.6500` | 3,888.00 USD | 523,571.46 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.08` | `671.2700` | 34,961.08 USD | 558,532.54 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `52.08` | `5488.3600` | 285,839.28 USD | 844,371.82 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `52.09` | `83.2900` | 4,338.99 USD | 20,662.62 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `52.09` | `892.8800` | 46,513.69 USD | 67,176.31 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `114.7100` | 5,975.59 USD | 73,151.89 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `333.5700` | 17,376.33 USD | 90,528.22 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `1818.0200` | 94,702.48 USD | 185,230.70 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `637.8900` | 33,227.69 USD | 218,458.39 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `52.09` | `91.0600` | 4,743.22 USD | 223,201.62 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `579.7700` | 30,199.06 USD | 253,400.68 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `163.1800` | 8,499.56 USD | 261,900.23 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `4750.7000` | 247,444.96 USD | 509,345.19 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `52.09` | `115.1900` | 5,999.67 USD | 515,344.86 USD | `1 orders` | `-0.03%` | `-` |
| `ASK` | `52.10` | `69.8300` | 3,638.49 USD | 13,269.28 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `52.10` | `67.6800` | 3,526.40 USD | 9,630.79 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `52.10` | `117.1600` | 6,104.39 USD | 6,104.39 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `52.10` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 52.10` | `0.00%` | `-` |
| `BID` | `52.10` | `7.7100` | 401.71 USD | 401.71 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `52.10` | `5.9200` | 308.44 USD | 710.14 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `52.10` | `7.7300` | 402.72 USD | 1,112.86 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `52.10` | `291.6900` | 15,196.17 USD | 16,309.04 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `52.10` | `0.2800` | 14.59 USD | 16,323.62 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `52.11` | `1203.6600` | 62,727.54 USD | 230,611.06 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `71.2200` | 3,711.49 USD | 167,883.53 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `0.2000` | 10.42 USD | 164,172.04 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `456.6800` | 23,798.05 USD | 164,161.62 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `52.11` | `456.3600` | 23,780.92 USD | 140,363.56 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `71.2200` | 3,711.20 USD | 116,582.65 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `152.4400` | 7,943.34 USD | 112,871.44 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `197.7500` | 10,304.16 USD | 104,928.10 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `52.11` | `1561.3300` | 81,354.66 USD | 94,623.94 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `52.12` | `1786.5400` | 93,118.04 USD | 880,499.47 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `52.12` | `5890.1900` | 307,002.59 USD | 787,381.43 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `52.12` | `236.8200` | 12,343.06 USD | 480,378.84 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `44.8000` | 2,334.93 USD | 468,035.78 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `551.9200` | 28,764.97 USD | 465,700.85 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `188.0200` | 9,799.04 USD | 436,935.88 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `112.1900` | 5,846.89 USD | 427,136.84 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `52.12` | `3658.8100` | 190,678.88 USD | 421,289.95 USD | `3 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,970,539.62 USD | `345,023.32` | `58.92` | `52.09` | `574.47` | 2,358,821.73 USD | `+13.13%` | `5X Cross` |
| `125` | `0x4692...164f` | `SHORT` | 16,182,746.22 USD | `310,692.82` | `53.29` | `52.09` | `250.48` | 374,057.16 USD | `+2.31%` | `5X Cross` |
| `208` | `0xacb6...efbd` | `SHORT` | 10,471,805.69 USD | `201,133.33` | `59.63` | `52.09` | `76.51` | 1,520,851.42 USD | `+14.52%` | `6X Cross` |
| `223` | `0x49e9...e1d0` | `SHORT` | 9,969,206.39 USD | `191,479.84` | `55.61` | `52.09` | `95.87` | 678,158.77 USD | `+6.80%` | `4X Cross` |
| `240` | `0xc26c...b8f4` | `LONG` | 9,451,703.17 USD | `181,463.41` | `55.43` | `52.09` | `0.000000` | -607,051.91 USD | `-6.42%` | `2X Cross` |
| `358` | `0xd8c5...99b0` | `SHORT` | 6,580,263.52 USD | `126,320.04` | `61.98` | `52.09` | `198.68` | 1,249,074.32 USD | `+18.98%` | `3X Cross` |
| `359` | `0x645b...87b8` | `LONG` | 6,577,085.93 USD | `126,309.96` | `56.63` | `52.09` | `0.000000` | -576,394.96 USD | `-8.76%` | `3X Cross` |
| `395` | `0xe9ff...5903` | `SHORT` | 5,883,818.88 USD | `112,996.08` | `60.07` | `52.09` | `199.62` | 904,131.92 USD | `+15.37%` | `5X Cross` |
| `415` | `0xfc66...ca06` | `SHORT` | 5,402,142.73 USD | `103,683.98` | `54.61` | `52.09` | `203.43` | 259,637.80 USD | `+4.81%` | `7X Cross` |
| `614` | `0x9aa5...58af` | `LONG` | 3,709,431.67 USD | `71,243.43` | `61.59` | `52.09` | `0.000000` | -678,725.85 USD | `-18.30%` | `20X Cross` |
| `731` | `0x2056...8396` | `LONG` | 3,123,840.00 USD | `60,000.00` | `66.92` | `52.09` | `21.34` | -891,487.14 USD | `-28.54%` | `10X Cross` |
| `826` | `0x354b...6425` | `LONG` | 2,743,361.29 USD | `52,669.84` | `52.37` | `52.09` | `0.000000` | -14,917.11 USD | `-0.54%` | `10X Cross` |
| `868` | `0x0242...ffa1` | `SHORT` | 2,599,959.67 USD | `49,916.67` | `56.48` | `52.09` | `343.92` | 219,172.19 USD | `+8.43%` | `10X Cross` |
| `874` | `0x960b...f0fc` | `LONG` | 2,576,017.85 USD | `49,457.96` | `55.82` | `52.09` | `0.000000` | -184,919.18 USD | `-7.18%` | `25X Cross` |
| `963` | `0x8b9d...7b28` | `LONG` | 2,335,751.02 USD | `44,823.47` | `58.35` | `52.09` | `0.000000` | -279,697.52 USD | `-11.97%` | `10X Cross` |
| `1051` | `0x5647...e7de` | `LONG` | 2,096,768.08 USD | `40,262.07` | `57.38` | `52.09` | `0.000000` | -213,469.52 USD | `-10.18%` | `20X Cross` |
| `1056` | `0xa2ce...3126` | `LONG` | 2,083,840.00 USD | `40,000.00` | `74.30` | `52.09` | `0.000000` | -888,215.49 USD | `-42.62%` | `20X Cross` |
| `1081` | `0xb078...de15` | `SHORT` | 2,031,354.52 USD | `39,000.01` | `52.58` | `52.09` | `195.35` | 19,164.43 USD | `+0.94%` | `8X Cross` |
| `1421` | `0x5a88...d997` | `LONG` | 1,562,760.00 USD | `30,000.00` | `59.50` | `52.09` | `40.32` | -222,127.59 USD | `-14.21%` | `25X Cross` |
| `1422` | `0x3678...b209` | `LONG` | 1,562,760.00 USD | `30,000.00` | `57.15` | `52.09` | `0.000000` | -151,740.00 USD | `-9.71%` | `20X Cross` |
| `1647` | `0x7ea9...fc7f` | `LONG` | 1,301,775.00 USD | `25,000.00` | `53.60` | `52.09` | `22.80` | -38,229.05 USD | `-2.94%` | `25X Cross` |
| `1725` | `0xce97...7e78` | `LONG` | 1,229,571.54 USD | `23,616.54` | `52.19` | `52.09` | `0.000000` | -2,878.18 USD | `-0.23%` | `5X Cross` |
| `1777` | `0xf517...c032` | `LONG` | 1,178,394.95 USD | `22,627.50` | `66.29` | `52.09` | `0.000000` | -321,600.16 USD | `-27.29%` | `20X Cross` |
| `1906` | `0xcc9f...d218` | `LONG` | 1,068,384.52 USD | `20,520.60` | `52.63` | `52.09` | `26.86` | -11,523.53 USD | `-1.08%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `65.51` | 14,313.28 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:SILVER Liquidated Long: 14.31K USD at 65.5130 USD [API] | `2026-09-04 12:30:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`53.30` (Vol: 3,200,000.00 USD, Dist: `+2.03%`) | Long MP=`51.68` (Vol: 2,700,000.00 USD, Dist: `--1.07%`)
  * 48H Horizon: Short MP=`55.08` (Vol: 4,200,000.00 USD, Dist: `+5.44%`) | Long MP=`51.68` (Vol: 3,100,000.00 USD, Dist: `--1.07%`)
  * 3D Horizon: Short MP=`55.08` (Vol: 4,700,000.00 USD, Dist: `+5.44%`) | Long MP=`51.96` (Vol: 4,000,000.00 USD, Dist: `--0.54%`)
  * 7D Horizon: Short MP=`54.83` (Vol: 7,300,000.00 USD, Dist: `+4.95%`) | Long MP=`51.96` (Vol: 4,900,000.00 USD, Dist: `--0.54%`)
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
  * Current Rate: `8.66K` | Last 24h: `193.96K` | Last 3d: `450.64K` | Last 7d: `729.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-` |
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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `52.06` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `51.80` (Risk Distance: `0.2643` pts)
  * +2.5R Take Profit: `52.72`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.42` (Risk Distance: `0.2643` pts)
  * +2.5R Take Profit: `51.50`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`52.49`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
