# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 03:49:32 IST` (`2026-10-29 22:19:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4021.96` | **Live Ask Quote**: `4022.04` | **Mid Price**: `4022.00`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `4029.51` | VWAP Z-Score: `-0.71` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.86` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.69` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.49` | Lower -3.00σ Band: `3994.53`
  * Upper +2.51σ Band: `4058.78` | Lower -2.51σ Band: `4000.24`
  * Upper +2.01σ Band: `4052.95` | Lower -2.01σ Band: `4006.07`
  * Upper +2.00σ Band: `4052.83` | Lower -2.00σ Band: `4006.19`
  * Upper +1.28σ Band: `4044.44` | Lower -1.28σ Band: `4014.58`
  * Upper +1.00σ Band: `4041.17` | Lower -1.00σ Band: `4017.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.56` | EMA-20=`4019.44` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4023.03` (Slope: `+0.0000`) | EMA-100=`4029.00`
  * Institutional Anchors: EMA-144=`4030.90` | EMA-200=`4031.28` (Slope: `-0.0420`) | EMA-233=`4030.73`
- **Range Boundaries**: 24H High=`4070.97` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4026.74` (Distance: `-0.12%`)
  * Point of Control (POC) = `4021.21` (Distance: `+0.02%`)
  * Value Area Low (VAL) = `4021.21` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4020.74`
  * London Session (08:00-16:00 UTC): High=`4038.09` | Low=`4005.91`
  * New York Session (13:00-21:00 UTC): High=`4046.13` | Low=`3997.87`
  * Initial Balance (First Hour): IB High=`4034.07` | IB Low=`4009.93`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4005.91` - `4038.09`
  * Optimal Trade Entry (OTE 0.705): `4030.04`
  * Structural Invalidation Anchor (0.786): `4054.18`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4023.28` | `4023.63` | `4022.23` | `4022.97` | `47` | 188,148.23 USD | 44,358.99 USD | `+23.58%` | 2,014,961.92 USD | `+0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4022.98` | `4023.42` | `4022.62` | `4022.63` | `20` | 81,218.19 USD | -5,391.11 USD | `-6.64%` | 2,009,570.81 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4022.62` | `4023.57` | `4022.62` | `4022.98` | `20` | 81,092.20 USD | 75,741.21 USD | `+93.40%` | 2,085,312.02 USD | `+0.85` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4020.01` | `4020.01` | `4018.12` | `4018.13` | `44` | 175,174.25 USD | -58,319.99 USD | `-33.29%` | 1,935,454.73 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4018.12` | `4025.28` | `4017.72` | `4022.63` | `250` | 1,005,666.39 USD | 151,466.76 USD | `+15.06%` | 2,086,921.48 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4022.62` | `4023.57` | `4022.62` | `4022.98` | `20` | 81,092.20 USD | 75,741.21 USD | `+93.40%` | 2,162,662.69 USD | `+0.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,839,422.95 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,963,502.96 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4025.28` | `4017.72` | `4022.98` | `270` | 1,086,758.60 USD | 227,207.97 USD | `+20.91%` | 2,190,710.92 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4022.98` | `1,922` | 7,734,174.23 USD | 112,146.07 USD | `+1.45%` | 1,359,293.39 USD | `-0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4022.98` | `1,922` | 7,734,174.23 USD | 112,146.07 USD | `+1.45%` | 1,359,293.39 USD | `-0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4020.80` | `7.9587` | 32,000.34 USD | 1,634,521.77 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4020.90` | `10.2559` | 41,237.95 USD | 1,602,521.43 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4021.00` | `0.9326` | 3,749.98 USD | 1,561,283.48 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4021.10` | `51.6590` | 207,726.00 USD | 1,557,533.50 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4021.20` | `6.2108` | 24,974.87 USD | 1,349,807.49 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4021.30` | `15.5604` | 62,573.04 USD | 1,324,832.63 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4021.40` | `103.6723` | 416,907.79 USD | 1,262,259.59 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `4021.50` | `16.7620` | 67,408.38 USD | 845,351.80 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4021.60` | `3.5426` | 14,246.92 USD | 777,943.42 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4021.70` | `1.1364` | 4,570.26 USD | 763,696.50 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4021.80` | `0.9324` | 3,749.93 USD | 759,126.24 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4021.90` | `9.4754` | 38,109.11 USD | 755,376.31 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.00` | `50.6579` | 203,746.07 USD | 717,267.20 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4022.10` | `21.0500` | 84,665.21 USD | 513,521.13 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4022.20` | `0.9870` | 3,969.91 USD | 428,855.92 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.30` | `24.1534` | 97,152.22 USD | 424,886.01 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4022.40` | `3.6078` | 14,512.01 USD | 327,733.79 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4022.50` | `24.8591` | 99,995.73 USD | 313,221.78 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4022.60` | `23.9722` | 96,430.57 USD | 213,226.05 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `4022.70` | `29.0341` | 116,795.47 USD | 116,795.47 USD | `14 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4022.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,022.75` | `0.00%` | `-` |
| `ASK` | `4022.80` | `9.2067` | 37,036.71 USD | 37,036.71 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `4022.90` | `6.7697` | 27,233.83 USD | 64,270.54 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `4023.00` | `3.7874` | 15,236.71 USD | 79,507.25 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4023.30` | `17.8776` | 71,926.95 USD | 151,434.20 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4023.50` | `0.2490` | 1,001.85 USD | 152,436.05 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4023.60` | `3.7280` | 14,999.98 USD | 167,436.03 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4023.70` | `0.5868` | 2,361.11 USD | 169,797.14 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4023.80` | `43.7422` | 176,009.86 USD | 345,807.00 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4023.90` | `3.4630` | 13,934.77 USD | 359,741.77 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4024.00` | `4.9650` | 19,979.16 USD | 379,720.93 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4024.10` | `1.2937` | 5,205.98 USD | 384,926.90 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4024.20` | `4.4450` | 17,887.57 USD | 402,814.47 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.30` | `5.4957` | 22,116.35 USD | 424,930.82 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.40` | `7.4879` | 30,134.30 USD | 455,065.12 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4024.50` | `23.4856` | 94,517.80 USD | 549,582.92 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4024.60` | `49.6951` | 200,002.90 USD | 749,585.82 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4024.70` | `5.2203` | 21,010.14 USD | 770,595.96 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4024.80` | `7.5433` | 30,360.27 USD | 800,956.24 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4024.90` | `1.1769` | 4,736.90 USD | 805,693.14 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `4025.20` | `7.7366` | 31,141.36 USD | 836,834.50 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `53` | `0x5b5d...c060` | `SHORT` | 25,604,116.58 USD | `6,365.38` | `4188.90` | `4022.20` | `33117.35` | 1,059,854.71 USD | `+4.14%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,495,222.05 USD | `6,338.15` | `4132.76` | `4022.20` | `13748.53` | 698,844.91 USD | `+2.74%` | `5X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 23,611,083.35 USD | `5,869.90` | `4228.86` | `4022.20` | `30781.92` | 1,211,938.59 USD | `+5.13%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,423,795.11 USD | `4,828.91` | `4157.43` | `4022.20` | `2254.41` | -652,087.20 USD | `-3.36%` | `25X Cross` |
| `145` | `0x645b...87b8` | `LONG` | 14,212,194.68 USD | `3,533.26` | `4129.11` | `4022.20` | `424.97` | -377,054.49 USD | `-2.65%` | `3X Cross` |
| `161` | `0x7a6d...f79c` | `SHORT` | 13,146,060.78 USD | `3,268.21` | `4228.94` | `4022.20` | `4397.75` | 675,018.35 USD | `+5.13%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,664,960.40 USD | `2,900.00` | `4364.92` | `4022.20` | `4235.67` | 993,315.93 USD | `+8.52%` | `20X Cross` |
| `259` | `0xfc66...ca06` | `SHORT` | 8,990,349.59 USD | `2,235.07` | `4031.28` | `4022.20` | `10915.66` | 19,863.05 USD | `+0.22%` | `3X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,849,500.00 USD | `2,200.00` | `4176.09` | `4022.20` | `2659.14` | -337,919.30 USD | `-3.82%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,849,280.00 USD | `2,200.00` | `4112.20` | `4022.20` | `4331.15` | 197,574.59 USD | `+2.23%` | `20X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,945,724.67 USD | `1,975.37` | `4048.55` | `4022.20` | `6503.19` | 51,667.05 USD | `+0.65%` | `6X Cross` |
| `371` | `0xc26c...b8f4` | `LONG` | 6,355,198.12 USD | `1,579.95` | `4075.62` | `4022.20` | `0.000000` | -84,098.85 USD | `-1.32%` | `1X Cross` |
| `402` | `0x12d2...f97f` | `LONG` | 5,639,174.72 USD | `1,401.94` | `4278.91` | `4022.20` | `3176.93` | -359,615.86 USD | `-6.38%` | `20X Cross` |
| `550` | `0x63da...8add` | `LONG` | 4,022,400.00 USD | `1,000.00` | `4021.46` | `4022.20` | `3564.11` | 939.04 USD | `+0.02%` | `25X Cross` |
| `560` | `0x354b...6425` | `LONG` | 3,973,167.26 USD | `987.74` | `4031.85` | `4022.20` | `0.000000` | -9,240.08 USD | `-0.23%` | `10X Cross` |
| `580` | `0x9aa5...58af` | `LONG` | 3,908,332.78 USD | `971.64` | `4279.98` | `4022.20` | `0.000000` | -250,276.30 USD | `-6.40%` | `20X Cross` |
| `603` | `0xf3dc...1672` | `LONG` | 3,743,916.53 USD | `930.74` | `4024.62` | `4022.20` | `3337.59` | -1,976.03 USD | `-0.05%` | `20X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,368,440.29 USD | `837.40` | `4599.73` | `4022.20` | `0.000000` | -483,380.09 USD | `-14.35%` | `20X Cross` |
| `818` | `0x0fac...7a0a` | `LONG` | 2,761,385.91 USD | `686.49` | `4290.34` | `4022.20` | `1446.04` | -183,872.79 USD | `-6.66%` | `25X Cross` |
| `874` | `0xd8c5...99b0` | `SHORT` | 2,583,872.59 USD | `642.35` | `4175.35` | `4022.20` | `32820.33` | 98,188.59 USD | `+3.80%` | `4X Cross` |
| `902` | `0x625e...a354` | `SHORT` | 2,493,888.00 USD | `620.00` | `4122.81` | `4022.20` | `4342.25` | 62,259.03 USD | `+2.50%` | `20X Cross` |
| `934` | `0xeae3...e8ad` | `SHORT` | 2,413,560.00 USD | `600.00` | `4104.77` | `4022.20` | `4325.27` | 49,305.11 USD | `+2.04%` | `20X Cross` |
| `938` | `0xf285...fa82` | `LONG` | 2,405,821.17 USD | `598.11` | `4146.45` | `4022.20` | `3891.24` | -74,198.38 USD | `-3.08%` | `25X Cross` |
| `962` | `0x12f7...8750` | `LONG` | 2,355,560.48 USD | `585.61` | `4082.77` | `4022.20` | `2577.36` | -35,356.50 USD | `-1.50%` | `10X Cross` |
| `1094` | `0x413c...886c` | `LONG` | 2,011,350.00 USD | `500.00` | `4010.43` | `4022.20` | `0.000000` | 6,133.77 USD | `+0.30%` | `2X Cross` |
| `1103` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.20` | `4715.04` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1107` | `0x0593...40f9` | `LONG` | 1,995,871.98 USD | `496.18` | `4024.57` | `4022.20` | `3701.73` | -1,031.85 USD | `-0.05%` | `10X Isolated` |
| `1182` | `0x2edd...8179` | `LONG` | 1,894,577.18 USD | `470.91` | `4164.68` | `4023.04` | `0.000000` | -66,624.13 USD | `-3.52%` | `10X Cross` |
| `1228` | `0xead5...69f2` | `LONG` | 1,825,300.36 USD | `453.78` | `4220.88` | `4022.20` | `3538.94` | -90,067.70 USD | `-4.93%` | `5X Isolated` |
| `1297` | `0x7a6d...f79c` | `SHORT` | 1,723,582.91 USD | `428.38` | `4136.09` | `4023.04` | `5805.65` | 48,232.10 USD | `+2.80%` | `10X Cross` |
| `1338` | `0x46fc...1195` | `LONG` | 1,651,887.09 USD | `410.66` | `4055.10` | `4022.20` | `2141.68` | -13,389.40 USD | `-0.81%` | `20X Cross` |
| `1379` | `0x6d15...d374` | `LONG` | 1,608,960.00 USD | `400.00` | `4068.25` | `4022.20` | `3841.81` | -18,340.00 USD | `-1.14%` | `25X Cross` |
| `1380` | `0xee02...309d` | `SHORT` | 1,608,960.00 USD | `400.00` | `4438.84` | `4022.20` | `4226.89` | 166,578.60 USD | `+10.35%` | `25X Isolated` |
| `1416` | `0x02a7...fe9f` | `SHORT` | 1,568,736.00 USD | `390.00` | `4055.02` | `4022.20` | `4306.71` | 12,723.25 USD | `+0.81%` | `25X Cross` |
| `1451` | `0x51f6...2b39` | `LONG` | 1,534,460.55 USD | `381.40` | `4234.15` | `4023.04` | `0.000000` | -80,455.34 USD | `-5.24%` | `10X Cross` |
| `1456` | `0x7e77...b8d2` | `SHORT` | 1,528,664.00 USD | `380.00` | `4131.92` | `4022.20` | `4293.51` | 41,465.64 USD | `+2.71%` | `20X Cross` |
| `1470` | `0x72c2...9b37` | `LONG` | 1,500,920.65 USD | `373.13` | `4000.98` | `4022.20` | `3778.05` | 8,027.14 USD | `+0.53%` | `13X Isolated` |
| `1515` | `0xaa44...b844` | `LONG` | 1,448,100.00 USD | `360.00` | `4043.10` | `4022.20` | `2803.27` | -7,417.63 USD | `-0.51%` | `4X Cross` |
| `1517` | `0x781e...96b7` | `SHORT` | 1,446,795.02 USD | `359.61` | `4364.97` | `4023.04` | `13576.90` | 122,905.90 USD | `+8.50%` | `10X Cross` |
| `1626` | `0xa41f...d50a` | `LONG` | 1,323,217.15 USD | `328.96` | `4468.89` | `4022.20` | `3833.19` | -146,880.70 USD | `-11.10%` | `15X Cross` |
| `1660` | `0xbf5a...88ba` | `SHORT` | 1,277,735.07 USD | `317.65` | `4091.80` | `4022.20` | `9886.34` | 22,047.96 USD | `+1.73%` | `20X Cross` |
| `1695` | `0xff31...ff6c` | `SHORT` | 1,246,975.00 USD | `310.00` | `4372.43` | `4022.20` | `4789.18` | 108,480.38 USD | `+8.70%` | `10X Isolated` |
| `1705` | `0xada6...6f88` | `LONG` | 1,239,333.46 USD | `308.10` | `4166.46` | `4022.20` | `1898.73` | -44,355.56 USD | `-3.58%` | `5X Cross` |
| `1729` | `0x5238...54e5` | `LONG` | 1,206,720.00 USD | `300.00` | `4023.33` | `4022.20` | `3833.96` | -279.31 USD | `-0.02%` | `15X Isolated` |
| `1871` | `0x50e2...d770` | `LONG` | 1,087,552.87 USD | `270.37` | `4243.58` | `4022.20` | `2562.10` | -59,773.59 USD | `-5.50%` | `20X Cross` |
| `1890` | `0x4c92...4f17` | `SHORT` | 1,072,883.21 USD | `266.72` | `4260.98` | `4022.20` | `6505.31` | 63,609.03 USD | `+5.93%` | `20X Cross` |
| `1943` | `0xd346...c4f3` | `LONG` | 1,026,411.09 USD | `255.17` | `4188.66` | `4022.20` | `3310.43` | -42,425.42 USD | `-4.13%` | `5X Isolated` |
| `1991` | `0x1581...463b` | `LONG` | 1,005,600.00 USD | `250.00` | `4003.77` | `4022.20` | `3571.67` | 4,656.41 USD | `+0.46%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.85` (Vol: 274,500.00 USD, Dist: `+2.26%`) | Long MP=`3937.39` (Vol: 356,200.00 USD, Dist: `--2.04%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.96%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.05%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.94%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.04%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.29%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.39%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,270,000.00 USD | 16,270,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,200,000.00 USD | 16,200,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 3,960,000.00 USD | 3,960,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,920,000.00 USD | 3,920,000.00 USD | 67,500.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,990,000.00 USD | 15,990,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 3,840,000.00 USD | 3,840,000.00 USD | 35,590.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,900,000.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 3,800,000.00 USD | 3,800,000.00 USD | 33,620.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,710,000.00 USD | 15,710,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.60` | 3,760,000.00 USD | 3,760,000.00 USD | 41,580.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,600,000.00 USD | 15,600,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.80` | 3,710,000.00 USD | 3,710,000.00 USD | 17,490.00 USD | 0.00 USD | 9,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,470,000.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3644.00` | 3,690,000.00 USD | 3,690,000.00 USD | 6,610.00 USD | 0.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,400,000.00 USD | 15,400,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3648.20` | 3,680,000.00 USD | 3,680,000.00 USD | 16,690.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,360,000.00 USD | 15,360,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3652.40` | 3,660,000.00 USD | 3,660,000.00 USD | 20,490.00 USD | 0.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,340,000.00 USD | 15,340,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3656.60` | 3,640,000.00 USD | 3,640,000.00 USD | 5,500.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,310,000.00 USD | 15,310,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.80` | 3,630,000.00 USD | 3,630,000.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,280,000.00 USD | 15,280,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,250,000.00 USD | 15,250,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,240,000.00 USD | 15,240,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,880,000.00 USD | 14,880,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,390,000.00 USD | 14,390,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,860,000.00 USD | 13,860,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.00` | 3,630,000.00 USD | 3,630,000.00 USD | 27,940.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,530,000.00 USD | 13,530,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.20` | 3,590,000.00 USD | 3,590,000.00 USD | 78,390.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,230,000.00 USD | 13,230,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.40` | 3,510,000.00 USD | 3,510,000.00 USD | 152,270.00 USD | 0.00 USD | 25,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,940,000.00 USD | 12,940,000.00 USD | 183,740.00 USD | 0.00 USD | 69,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.60` | 3,330,000.00 USD | 3,330,000.00 USD | 196,590.00 USD | 0.00 USD | 25,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,690,000.00 USD | 12,690,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.80` | 3,110,000.00 USD | 3,110,000.00 USD | 153,750.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,150,000.00 USD | 12,150,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.00` | 2,930,000.00 USD | 2,930,000.00 USD | 92,870.00 USD | 0.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,730,000.00 USD | 11,730,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 2,830,000.00 USD | 2,830,000.00 USD | 142,020.00 USD | 0.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,190,000.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 2,680,000.00 USD | 2,680,000.00 USD | 47,790.00 USD | 0.00 USD | 20,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,850,000.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3887.60` | 2,610,000.00 USD | 2,610,000.00 USD | 15,370.00 USD | 0.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,710,000.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.80` | 2,580,000.00 USD | 2,580,000.00 USD | 68,400.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,600,000.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3896.00` | 2,510,000.00 USD | 2,510,000.00 USD | 49,670.00 USD | 0.00 USD | 4,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,470,000.00 USD | 10,470,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3900.20` | 2,460,000.00 USD | 2,460,000.00 USD | 13,430.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,360,000.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.40` | 2,440,000.00 USD | 2,440,000.00 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,270,000.00 USD | 10,270,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,180,000.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,430,000.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,480,000.00 USD | 8,480,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,590,000.00 USD | 7,590,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.80` | 2,420,000.00 USD | 2,420,000.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,750,000.00 USD | 6,750,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.00` | 2,390,000.00 USD | 2,390,000.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,290,000.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 2,210,000.00 USD | 2,210,000.00 USD | 296,180.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,630,000.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,860,000.00 USD | 1,860,000.00 USD | 367,420.00 USD | 0.00 USD | 45,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.60` | 1,450,000.00 USD | 1,450,000.00 USD | 359,720.00 USD | 0.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.80` | 1,050,000.00 USD | 1,050,000.00 USD | 181,840.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.00` | 838,460.00 USD | 838,460.00 USD | 275,140.00 USD | 0.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 550,030.00 USD | 550,030.00 USD | 108,590.00 USD | 0.00 USD | 50,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 391,250.00 USD | 391,250.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.60` | 341,160.00 USD | 341,160.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.80` | 246,570.00 USD | 246,570.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3980.00` | 113,600.00 USD | 113,600.00 USD | 53,190.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3984.20` | 46,190.00 USD | 46,190.00 USD | 44,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3988.40` | 2,110.00 USD | 2,110.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.40` | 12,130.00 USD | 12,130.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.60` | 183,330.00 USD | 183,330.00 USD | 163,880.00 USD | 0.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.80` | 435,100.00 USD | 435,100.00 USD | 224,550.00 USD | 0.00 USD | 27,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.00` | 908,010.00 USD | 908,010.00 USD | 415,230.00 USD | 0.00 USD | 57,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 506,510.00 USD | 0.00 USD | 101,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.20` | 1,210,000.00 USD | 1,210,000.00 USD | 252,410.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,690,000.00 USD | 6,690,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 1,510,000.00 USD | 1,510,000.00 USD | 269,460.00 USD | 0.00 USD | 30,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,690,000.00 USD | 1,690,000.00 USD | 171,150.00 USD | 0.00 USD | 15,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.80` | 1,980,000.00 USD | 1,980,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.00` | 2,070,000.00 USD | 2,070,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.20` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,330,000.00 USD | 9,330,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.40` | 2,230,000.00 USD | 2,230,000.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,560,000.00 USD | 9,560,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,340,000.00 USD | 2,340,000.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,770,000.00 USD | 9,770,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 2,380,000.00 USD | 2,380,000.00 USD | 26,860.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,940,000.00 USD | 9,940,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.00` | 2,420,000.00 USD | 2,420,000.00 USD | 36,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,040,000.00 USD | 10,040,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,130,000.00 USD | 10,130,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,510,000.00 USD | 10,510,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,940,000.00 USD | 10,940,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 2,420,000.00 USD | 2,420,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,930,000.00 USD | 11,930,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.40` | 2,500,000.00 USD | 2,500,000.00 USD | 76,990.00 USD | 0.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.60` | 2,630,000.00 USD | 2,630,000.00 USD | 108,350.00 USD | 0.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.80` | 2,790,000.00 USD | 2,790,000.00 USD | 145,720.00 USD | 0.00 USD | 22,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 249,690.00 USD | 0.00 USD | 59,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.00` | 2,970,000.00 USD | 2,970,000.00 USD | 153,150.00 USD | 0.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,460,000.00 USD | 13,460,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.20` | 3,150,000.00 USD | 3,150,000.00 USD | 164,460.00 USD | 0.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,780,000.00 USD | 13,780,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.40` | 3,220,000.00 USD | 3,220,000.00 USD | 52,550.00 USD | 0.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,220,000.00 USD | 14,220,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.60` | 3,370,000.00 USD | 3,370,000.00 USD | 142,710.00 USD | 0.00 USD | 14,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,560,000.00 USD | 14,560,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.80` | 3,430,000.00 USD | 3,430,000.00 USD | 41,800.00 USD | 0.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,700,000.00 USD | 14,700,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4211.00` | 3,460,000.00 USD | 3,460,000.00 USD | 18,450.00 USD | 0.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,810,000.00 USD | 14,810,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4215.20` | 3,510,000.00 USD | 3,510,000.00 USD | 45,970.00 USD | 0.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,920,000.00 USD | 14,920,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4219.40` | 3,570,000.00 USD | 3,570,000.00 USD | 54,090.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4223.60` | 3,600,000.00 USD | 3,600,000.00 USD | 26,600.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,130,000.00 USD | 15,130,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.80` | 3,630,000.00 USD | 3,630,000.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4232.00` | 3,630,000.00 USD | 3,630,000.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,230,000.00 USD | 15,230,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,330,000.00 USD | 15,330,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,590,000.00 USD | 15,590,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,730,000.00 USD | 15,730,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,790,000.00 USD | 15,790,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.80` | 3,640,000.00 USD | 3,640,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,920,000.00 USD | 15,920,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.00` | 3,670,000.00 USD | 3,670,000.00 USD | 27,270.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,970,000.00 USD | 15,970,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4425.20` | 3,710,000.00 USD | 3,710,000.00 USD | 35,180.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4429.40` | 3,770,000.00 USD | 3,770,000.00 USD | 53,770.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.60` | 3,810,000.00 USD | 3,810,000.00 USD | 35,840.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4436.20` | 3,840,000.00 USD | 3,840,000.00 USD | 18,160.00 USD | 0.00 USD | 3,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,370,000.00 USD | 16,370,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,270,000.00 USD | 0.00 USD | 16,270,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.80` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 61,810.00 USD | 0.00 USD | 9,800.00 USD |
| `7D` | `3623.90` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.00` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `3628.10` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.10` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3632.30` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.20` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3636.50` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3640.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.40` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `3644.90` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.50` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.10` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.60` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 20,320.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `3653.30` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.70` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,460.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.50` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `3854.90` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.60` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 81,940.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `3859.10` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3860.70` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 117,160.00 USD | 0.00 USD | 15,000.00 USD |
| `7D` | `3863.30` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 183,740.00 USD | 0.00 USD | 69,400.00 USD |
| `1D` | `3864.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 215,160.00 USD | 0.00 USD | 31,470.00 USD |
| `7D` | `3867.50` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.90` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 144,700.00 USD | 0.00 USD | 20,980.00 USD |
| `7D` | `3871.70` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.00` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 126,020.00 USD | 0.00 USD | 18,010.00 USD |
| `7D` | `3875.90` | 11,730,000.00 USD | 0.00 USD | 11,730,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.10` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3880.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3881.20` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 105,320.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `3884.30` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3885.30` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 22,630.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3888.50` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.40` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.50` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 79,520.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `3896.90` | 10,470,000.00 USD | 0.00 USD | 10,470,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.60` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 23,220.00 USD | 0.00 USD | 133.60 USD |
| `7D` | `3901.10` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 15,320.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.50` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 55,890.00 USD | 0.00 USD | 11,870.00 USD |
| `7D` | `3934.70` | 6,750,000.00 USD | 0.00 USD | 6,750,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.60` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 156,780.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `3938.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.70` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 320,210.00 USD | 0.00 USD | 51,220.00 USD |
| `7D` | `3943.10` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3946.80` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 347,350.00 USD | 0.00 USD | 49,030.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 119,280.00 USD |
| `1D` | `3950.90` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 346,950.00 USD | 0.00 USD | 39,720.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3955.00` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 181,840.00 USD | 0.00 USD | 28,640.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.10` | 816,170.00 USD | 0.00 USD | 816,170.00 USD | 275,140.00 USD | 0.00 USD | 14,840.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.20` | 526,190.00 USD | 0.00 USD | 526,190.00 USD | 108,590.00 USD | 0.00 USD | 48,640.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.30` | 368,960.00 USD | 0.00 USD | 368,960.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.40` | 318,870.00 USD | 0.00 USD | 318,870.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.50` | 224,280.00 USD | 0.00 USD | 224,280.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.60` | 91,310.00 USD | 0.00 USD | 91,310.00 USD | 46,450.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.70` | 30,640.00 USD | 0.00 USD | 30,640.00 USD | 30,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4021.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4023.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4094.40` | 29,250.00 USD | 29,250.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `1D` | `4098.50` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4102.60` | 502,480.00 USD | 502,480.00 USD | 0.00 USD | 247,160.00 USD | 0.00 USD | 46,880.00 USD |
| `7D` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD |
| `1D` | `4106.70` | 974,450.00 USD | 974,450.00 USD | 0.00 USD | 425,080.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 101,580.00 USD |
| `1D` | `4110.80` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 263,130.00 USD | 0.00 USD | 36,190.00 USD |
| `7D` | `4111.10` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.90` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 252,040.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4119.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 146,650.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4123.10` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 246,290.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.20` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `4132.10` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.40` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.50` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 21,130.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.70` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.40` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.50` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4184.60` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 128,850.00 USD | 0.00 USD | 24,140.00 USD |
| `7D` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 59,740.00 USD |
| `1D` | `4188.70` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 186,400.00 USD | 0.00 USD | 26,010.00 USD |
| `7D` | `4190.90` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.80` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 154,770.00 USD | 0.00 USD | 18,170.00 USD |
| `7D` | `4195.10` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.90` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4199.30` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.00` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 103,730.00 USD | 0.00 USD | 4,310.00 USD |
| `7D` | `4203.50` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.10` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 83,950.00 USD | 0.00 USD | 21,020.00 USD |
| `7D` | `4207.70` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.20` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `4211.90` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `4216.10` | 14,920,000.00 USD | 14,920,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.40` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.50` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 40,830.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4224.50` | 15,130,000.00 USD | 15,130,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.60` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 6,730.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.70` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4414.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.96 USD |
| `7D` | `4417.70` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4418.30` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `4421.90` | 15,970,000.00 USD | 15,970,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.40` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4426.50` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4430.60` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | 8,160.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4434.70` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD |
| `7D` | `4438.70` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.95M` | Total OI Tokens: `68,333.8 PAXG`
  * 1h OI Change: `+0.03%` | 4h OI Change: `+0.25%` | 24h OI Change: `+0.11%`
  * Exchange Breakdown: Binance=`107.33M` | Bybit=`20.05M` | OKX=`-` | Hyperliquid=`24.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.37K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `51.39%` | `48.61%` | `1.06` | 1,160,000.00 USD |
| `15M` | `Binance` | `45.47%` | `54.53%` | `0.83` | 752,730.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `53.75%` | `46.25%` | `1.16` | 25,580.00 USD |
| `15M` | `KuCoin` | `48.98%` | `51.02%` | `0.96` | 91,000.00 USD |
| `15M` | `Gate` | `68.51%` | `31.49%` | `2.18` | 25,200.00 USD |
| `15M` | `Bitget` | `54.48%` | `45.52%` | `1.20` | 113,090.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `87.55%` | `12.45%` | `7.03` | 22,410.00 USD |
| `15M` | `Bitunix` | `48.93%` | `51.07%` | `0.96` | 27,290.00 USD |
| `15M` | `Hyperliquid` | `73.37%` | `26.63%` | `2.76` | 22,680.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.55%` | `2.45%` | `39.82` | 65,070.00 USD |
| `15M` | `HTX` | `57.9%` | `42.1%` | `1.38` | 3,050.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 5,180.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 691.98 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 3,820.00 USD |
| `15M` | `Whale Positions` | `45.47%` | `54.53%` | `0.83` | 752,730.00 USD |
| `15M` | `Global Accounts` | `51.39%` | `48.61%` | `1.06` | 1,160,000.00 USD |
| `1H` | `PAXG` | `54.83%` | `45.17%` | `1.21` | 8,480,000.00 USD |
| `1H` | `Binance` | `54.21%` | `45.79%` | `1.18` | 1,830,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `32.7%` | `67.3%` | `0.49` | 1,130,000.00 USD |
| `1H` | `KuCoin` | `48.18%` | `51.82%` | `0.93` | 79,430.00 USD |
| `1H` | `Gate` | `52.97%` | `47.03%` | `1.13` | 478,700.00 USD |
| `1H` | `Bitget` | `50.92%` | `49.08%` | `1.04` | 532,130.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `60.57%` | `39.43%` | `1.54` | 2,010,000.00 USD |
| `1H` | `Bitunix` | `53.01%` | `46.99%` | `1.13` | 1,440,000.00 USD |
| `1H` | `Hyperliquid` | `60.72%` | `39.28%` | `1.55` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 855,390.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `93.9%` | `6.1%` | `15.39` | 119,870.00 USD |
| `1H` | `HTX` | `67.13%` | `32.87%` | `2.04` | 2,550.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `8.28%` | `91.72%` | `0.09` | 12,030.00 USD |
| `1H` | `Aster` | `93%` | `7%` | `13.29` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.09%` | `53.91%` | `0.85` | 0.00 USD |
| `1H` | `Whale Positions` | `54.21%` | `45.79%` | `1.18` | 1,830,000.00 USD |
| `1H` | `Global Accounts` | `54.83%` | `45.17%` | `1.21` | 8,480,000.00 USD |
| `4H` | `PAXG` | `52.17%` | `47.83%` | `1.09` | 17,750,000.00 USD |
| `4H` | `Binance` | `49.49%` | `50.51%` | `0.98` | 10,910,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `48.21%` | `51.79%` | `0.93` | 623,720.00 USD |
| `4H` | `KuCoin` | `55.06%` | `44.94%` | `1.23` | 1,220,000.00 USD |
| `4H` | `Gate` | `56.22%` | `43.78%` | `1.28` | 294,280.00 USD |
| `4H` | `Bitget` | `54.57%` | `45.43%` | `1.20` | 1,770,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `55.93%` | `44.07%` | `1.27` | 149,250.00 USD |
| `4H` | `Bitunix` | `40.69%` | `59.31%` | `0.69` | 367,630.00 USD |
| `4H` | `Hyperliquid` | `46.09%` | `53.91%` | `0.85` | 930,140.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `76.84%` | `23.16%` | `3.32` | 1,280,000.00 USD |
| `4H` | `HTX` | `67.5%` | `32.5%` | `2.08` | 51,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.98%` | `70.02%` | `0.43` | 41,360.00 USD |
| `4H` | `Aster` | `74.28%` | `25.72%` | `2.89` | 33,520.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.93%` | `50.07%` | `1.00` | 60,740.00 USD |
| `4H` | `Whale Positions` | `49.49%` | `50.51%` | `0.98` | 10,910,000.00 USD |
| `4H` | `Global Accounts` | `52.17%` | `47.83%` | `1.09` | 17,750,000.00 USD |


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
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 961.90 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | -109,360.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -335,070.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,270,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,140,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,740,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,490,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,200,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,650,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,200,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,480,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,150,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+961.90` | 15m=`-109.36K` | 1h=`-1.27M` | 24h=`-1.20M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4021.21` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4012.86` (Risk Distance: `8.35` pts)
  * +2.5R Take Profit: `4042.08`
  * Mathematical Lot Sizing: **`1.19 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4026.74` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4035.09` (Risk Distance: `8.35` pts)
  * +2.5R Take Profit: `4005.87`
  * Mathematical Lot Sizing: **`1.19 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4054.18`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
