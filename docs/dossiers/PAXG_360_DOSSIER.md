# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 01:51:15 IST` (`2026-10-29 20:21:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4026.66` | **Live Ask Quote**: `4026.74` | **Mid Price**: `4026.70`
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
  * Session VWAP: `4029.71` | VWAP Z-Score: `-0.58` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.78` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.70` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4065.41` | Lower -3.00σ Band: `3994.02`
  * Upper +2.51σ Band: `4059.58` | Lower -2.51σ Band: `3999.85`
  * Upper +2.01σ Band: `4053.63` | Lower -2.01σ Band: `4005.80`
  * Upper +2.00σ Band: `4053.51` | Lower -2.00σ Band: `4005.92`
  * Upper +1.28σ Band: `4044.94` | Lower -1.28σ Band: `4014.48`
  * Upper +1.00σ Band: `4041.61` | Lower -1.00σ Band: `4017.82`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4015.86` | EMA-20=`4017.00` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.95` (Slope: `+0.0000`) | EMA-100=`4029.62`
  * Institutional Anchors: EMA-144=`4031.43` | EMA-200=`4031.61` (Slope: `-0.0557`) | EMA-233=`4030.85`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4040.10` (Distance: `-0.32%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.01%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.26%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4059.03` | POC=`4041.68` | VAL=`4035.89`
  * Prior Day Extremes: PDH=`4082.75` | PDL=`4024.90` | PDC=`4067.36`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4069.28` | Low=`4035.73`
  * London Session (08:00-16:00 UTC): High=`4046.38` | Low=`4015.80`
  * New York Session (13:00-21:00 UTC): High=`4039.31` | Low=`4010.16`
  * Initial Balance (First Hour): IB High=`4046.38` | IB Low=`4022.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4010.59` - `4042.81`
  * Optimal Trade Entry (OTE 0.705): `4034.75`
  * Structural Invalidation Anchor (0.786): `4058.91`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4025.61` | `4028.13` | `4024.22` | `4028.12` | `148` | 597,702.30 USD | -77,626.16 USD | `-12.99%` | 1,558,272.26 USD | `-0.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4028.12` | `4033.50` | `4028.12` | `4031.24` | `182` | 733,816.50 USD | 336,553.91 USD | `+45.86%` | 1,894,826.17 USD | `+2.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4031.24` | `4031.61` | `4028.85` | `4028.86` | `36` | 144,599.80 USD | -56,226.08 USD | `-38.88%` | 1,838,600.09 USD | `-0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4020.84` | `4023.61` | `4019.80` | `4022.48` | `119` | 477,711.99 USD | -158,924.13 USD | `-33.27%` | 1,573,296.90 USD | `-0.64` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4022.48` | `4025.99` | `4022.01` | `4025.60` | `107` | 430,285.41 USD | 62,601.52 USD | `+14.55%` | 1,635,898.42 USD | `+0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4025.61` | `4033.50` | `4024.22` | `4028.85` | `366` | 1,476,219.32 USD | 202,770.16 USD | `+13.74%` | 1,838,668.58 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4011.95` | `4017.97` | `4011.01` | `4017.56` | `511` | 2,050,996.96 USD | 1,105,382.66 USD | `+53.89%` | 2,342,518.27 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4025.99` | `4014.71` | `4025.60` | `520` | 2,091,733.78 USD | -652,688.52 USD | `-31.20%` | 1,689,829.74 USD | `-1.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4024.22` | `4028.85` | `366` | 1,476,219.32 USD | 202,770.16 USD | `+13.74%` | 1,892,599.90 USD | `+0.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4024.22` | `4028.85` | `366` | 1,476,219.32 USD | 202,770.16 USD | `+13.74%` | 1,449,917.49 USD | `-0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4024.22` | `4028.85` | `366` | 1,476,219.32 USD | 202,770.16 USD | `+13.74%` | 1,449,917.49 USD | `-0.07` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `4025.80` | `5.4550` | 21,960.74 USD | 1,205,672.21 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4025.90` | `1.8985` | 7,643.17 USD | 1,183,711.48 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4026.00` | `45.4990` | 183,178.97 USD | 1,176,068.30 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4026.10` | `11.4928` | 46,271.16 USD | 992,889.33 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4026.20` | `3.6210` | 14,578.87 USD | 946,618.17 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4026.30` | `1.0014` | 4,031.94 USD | 932,039.30 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4026.40` | `9.4439` | 38,024.92 USD | 928,007.36 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4026.50` | `0.4469` | 1,799.44 USD | 889,982.44 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4026.60` | `90.0080` | 362,426.21 USD | 888,183.00 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4026.70` | `13.3207` | 53,638.46 USD | 525,756.79 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4026.90` | `0.2769` | 1,115.05 USD | 472,118.32 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4027.00` | `3.9695` | 15,985.18 USD | 471,003.27 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4027.10` | `1.1147` | 4,489.01 USD | 455,018.10 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4027.20` | `57.3102` | 230,799.64 USD | 450,529.09 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4027.30` | `10.1685` | 40,951.60 USD | 219,729.45 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4027.40` | `7.4481` | 29,996.48 USD | 178,777.85 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4027.50` | `3.3000` | 13,290.75 USD | 148,781.37 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4027.60` | `0.1778` | 716.11 USD | 135,490.62 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4027.70` | `5.0400` | 20,299.61 USD | 134,774.52 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `4027.80` | `28.4212` | 114,474.91 USD | 114,474.91 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4027.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,027.85` | `0.00%` | `-` |
| `ASK` | `4027.90` | `23.2998` | 93,849.26 USD | 93,849.26 USD | `9 orders` | `+0.00%` | `-` |
| `ASK` | `4028.00` | `23.6231` | 95,153.85 USD | 189,003.11 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4028.10` | `3.7808` | 15,229.44 USD | 204,232.55 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4028.20` | `13.3965` | 53,963.78 USD | 258,196.33 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4028.30` | `9.2005` | 37,062.37 USD | 295,258.71 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4028.40` | `2.4196` | 9,747.12 USD | 305,005.82 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4028.50` | `1.2634` | 5,089.61 USD | 310,095.43 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4028.60` | `25.8543` | 104,156.63 USD | 414,252.06 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4028.70` | `8.4325` | 33,972.01 USD | 448,224.08 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4028.80` | `9.7657` | 39,344.05 USD | 487,568.13 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `4028.90` | `26.6048` | 107,188.08 USD | 594,756.21 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `4029.00` | `2.1471` | 8,650.67 USD | 603,406.87 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4029.10` | `23.2070` | 93,503.32 USD | 696,910.20 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `4029.20` | `10.0233` | 40,385.88 USD | 737,296.08 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4029.30` | `12.2023` | 49,166.73 USD | 786,462.80 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4029.40` | `41.1626` | 165,860.58 USD | 952,323.39 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4029.50` | `14.7917` | 59,603.16 USD | 1,011,926.54 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4029.60` | `9.3811` | 37,802.08 USD | 1,049,728.62 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4029.70` | `12.8660` | 51,846.12 USD | 1,101,574.74 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `4029.80` | `14.1453` | 57,002.73 USD | 1,158,577.47 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `50` | `0x5b5d...c060` | `SHORT` | 25,555,709.78 USD | `6,347.04` | `4191.43` | `4026.50` | `30248.35` | 1,047,507.33 USD | `+4.10%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,446,085.40 USD | `6,319.81` | `4133.70` | `4026.50` | `13551.37` | 678,127.85 USD | `+2.66%` | `5X Cross` |
| `70` | `0xb83d...6e36` | `SHORT` | 23,027,743.56 USD | `5,717.06` | `4234.49` | `4026.50` | `28574.98` | 1,181,131.67 USD | `+5.13%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,449,871.21 USD | `4,828.91` | `4157.43` | `4026.50` | `2132.22` | -626,011.10 USD | `-3.22%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,175,037.83 USD | `3,520.52` | `4129.51` | `4026.50` | `327.84` | -363,017.86 USD | `-2.56%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,159,133.63 USD | `3,268.21` | `4228.94` | `4026.50` | `4390.27` | 661,945.50 USD | `+5.03%` | `25X Cross` |
| `175` | `0xa742...e390` | `SHORT` | 11,676,560.40 USD | `2,900.00` | `4364.92` | `4026.50` | `4235.64` | 981,715.93 USD | `+8.41%` | `20X Cross` |
| `272` | `0x41e5...0825` | `SHORT` | 8,860,280.00 USD | `2,200.00` | `4112.20` | `4026.50` | `4331.13` | 186,574.59 USD | `+2.11%` | `20X Cross` |
| `274` | `0x3678...b209` | `LONG` | 8,858,080.00 USD | `2,200.00` | `4176.09` | `4026.50` | `2528.23` | -329,339.30 USD | `-3.72%` | `25X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 8,000,012.29 USD | `1,986.89` | `4032.86` | `4026.50` | `24220.55` | 12,853.88 USD | `+0.16%` | `3X Cross` |
| `313` | `0xacb6...efbd` | `SHORT` | 7,956,589.20 USD | `1,975.37` | `4048.55` | `4026.50` | `6484.24` | 40,802.52 USD | `+0.51%` | `6X Cross` |
| `380` | `0xc26c...b8f4` | `LONG` | 6,361,517.93 USD | `1,579.95` | `4075.62` | `4026.50` | `0.000000` | -77,779.04 USD | `-1.22%` | `1X Cross` |
| `412` | `0x12d2...f97f` | `LONG` | 5,646,885.40 USD | `1,401.94` | `4278.91` | `4026.50` | `2645.54` | -351,905.18 USD | `-6.23%` | `20X Cross` |
| `571` | `0x63da...8add` | `LONG` | 4,026,400.00 USD | `1,000.00` | `4021.46` | `4026.50` | `3564.08` | 4,939.04 USD | `+0.12%` | `25X Cross` |
| `589` | `0x9aa5...58af` | `LONG` | 3,913,579.65 USD | `971.64` | `4279.98` | `4026.50` | `0.000000` | -245,029.44 USD | `-6.26%` | `20X Cross` |
| `619` | `0xf3dc...1672` | `LONG` | 3,747,732.58 USD | `930.74` | `4024.62` | `4026.50` | `3337.56` | 1,840.02 USD | `+0.05%` | `20X Cross` |
| `676` | `0x4a20...3c26` | `LONG` | 3,371,706.15 USD | `837.40` | `4599.73` | `4026.50` | `0.000000` | -480,114.23 USD | `-14.24%` | `20X Cross` |
| `680` | `0x354b...6425` | `LONG` | 3,350,349.32 USD | `832.10` | `4033.48` | `4026.50` | `0.000000` | -5,896.59 USD | `-0.18%` | `10X Cross` |
| `832` | `0x0fac...7a0a` | `LONG` | 2,764,063.20 USD | `686.49` | `4290.34` | `4026.50` | `1303.96` | -181,195.50 USD | `-6.56%` | `25X Cross` |
| `875` | `0xd8c5...99b0` | `SHORT` | 2,586,442.00 USD | `642.35` | `4175.35` | `4026.50` | `32817.71` | 95,619.17 USD | `+3.70%` | `4X Cross` |
| `908` | `0x625e...a354` | `SHORT` | 2,497,298.00 USD | `620.00` | `4122.81` | `4026.50` | `4342.23` | 58,849.03 USD | `+2.36%` | `20X Cross` |
| `929` | `0xeae3...e8ad` | `SHORT` | 2,415,720.00 USD | `600.00` | `4104.77` | `4026.50` | `4325.25` | 47,145.11 USD | `+1.95%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,409,050.94 USD | `598.11` | `4146.45` | `4026.50` | `3891.22` | -70,968.61 USD | `-2.95%` | `25X Cross` |
| `954` | `0x12f7...8750` | `LONG` | 2,357,902.92 USD | `585.61` | `4082.77` | `4026.50` | `2281.19` | -33,014.06 USD | `-1.40%` | `10X Cross` |
| `1108` | `0x413c...886c` | `LONG` | 2,013,700.00 USD | `500.00` | `4010.43` | `4026.50` | `0.000000` | 8,483.77 USD | `+0.42%` | `2X Cross` |
| `1120` | `0x61ce...a62b` | `SHORT` | 2,003,695.35 USD | `497.50` | `4071.66` | `4026.50` | `4698.48` | 21,973.44 USD | `+1.10%` | `20X Cross` |
| `1129` | `0x0593...40f9` | `LONG` | 1,997,856.69 USD | `496.18` | `4024.57` | `4026.50` | `3701.71` | 952.86 USD | `+0.05%` | `10X Isolated` |
| `1250` | `0xead5...69f2` | `LONG` | 1,827,569.28 USD | `453.78` | `4220.88` | `4026.50` | `3538.92` | -87,798.78 USD | `-4.80%` | `5X Isolated` |
| `1251` | `0x2edd...8179` | `LONG` | 1,827,036.35 USD | `453.58` | `4169.95` | `4027.80` | `0.000000` | -64,387.77 USD | `-3.52%` | `10X Cross` |
| `1305` | `0x7a6d...f79c` | `SHORT` | 1,726,067.50 USD | `428.38` | `4136.09` | `4027.80` | `5534.05` | 45,747.50 USD | `+2.65%` | `10X Cross` |
| `1380` | `0x46fc...1195` | `LONG` | 1,639,377.35 USD | `407.16` | `4055.52` | `4026.50` | `2000.49` | -11,860.18 USD | `-0.72%` | `20X Cross` |
| `1398` | `0x6d15...d374` | `LONG` | 1,611,160.00 USD | `400.00` | `4068.25` | `4026.50` | `3841.79` | -16,140.00 USD | `-1.00%` | `25X Cross` |
| `1400` | `0xee02...309d` | `SHORT` | 1,610,560.00 USD | `400.00` | `4438.84` | `4026.50` | `4226.86` | 164,978.60 USD | `+10.24%` | `25X Isolated` |
| `1443` | `0x02a7...fe9f` | `SHORT` | 1,570,296.00 USD | `390.00` | `4055.02` | `4026.50` | `4306.68` | 11,163.25 USD | `+0.71%` | `25X Cross` |
| `1474` | `0x51f6...2b39` | `LONG` | 1,532,635.66 USD | `380.49` | `4234.66` | `4027.80` | `0.000000` | -78,592.41 USD | `-5.13%` | `10X Cross` |
| `1476` | `0x7e77...b8d2` | `SHORT` | 1,530,032.00 USD | `380.00` | `4131.92` | `4026.50` | `4293.49` | 40,097.64 USD | `+2.62%` | `20X Cross` |
| `1500` | `0x72c2...9b37` | `LONG` | 1,502,898.25 USD | `373.13` | `4000.98` | `4026.50` | `3778.02` | 10,004.73 USD | `+0.67%` | `13X Isolated` |
| `1534` | `0xaa44...b844` | `LONG` | 1,449,864.00 USD | `360.00` | `4043.10` | `4026.50` | `2803.24` | -5,653.63 USD | `-0.39%` | `4X Cross` |
| `1535` | `0x781e...96b7` | `SHORT` | 1,448,197.29 USD | `359.55` | `4365.03` | `4027.80` | `13004.90` | 121,250.19 USD | `+8.37%` | `10X Cross` |
| `1640` | `0xa41f...d50a` | `LONG` | 1,324,993.55 USD | `328.96` | `4468.89` | `4026.50` | `3833.16` | -145,104.31 USD | `-10.95%` | `15X Cross` |
| `1667` | `0x49e9...e1d0` | `SHORT` | 1,302,456.65 USD | `323.48` | `4025.23` | `4026.50` | `32203.15` | -378.32 USD | `-0.03%` | `4X Cross` |
| `1686` | `0xada6...6f88` | `LONG` | 1,285,563.20 USD | `319.28` | `4166.46` | `4026.50` | `1934.05` | -44,687.31 USD | `-3.48%` | `5X Cross` |
| `1695` | `0xbf5a...88ba` | `SHORT` | 1,279,450.41 USD | `317.65` | `4091.80` | `4026.50` | `10425.31` | 20,332.63 USD | `+1.59%` | `20X Cross` |
| `1727` | `0xff31...ff6c` | `SHORT` | 1,248,215.00 USD | `310.00` | `4372.43` | `4026.50` | `4789.15` | 107,240.38 USD | `+8.59%` | `10X Isolated` |
| `1887` | `0x50e2...d770` | `LONG` | 1,088,607.30 USD | `270.37` | `4243.58` | `4026.50` | `2562.07` | -58,719.16 USD | `-5.39%` | `20X Cross` |
| `1908` | `0x4c92...4f17` | `SHORT` | 1,073,923.42 USD | `266.72` | `4260.98` | `4026.50` | `6513.27` | 62,568.82 USD | `+5.83%` | `20X Cross` |
| `1974` | `0xd346...c4f3` | `LONG` | 1,027,431.79 USD | `255.17` | `4188.66` | `4026.50` | `3310.40` | -41,404.72 USD | `-4.03%` | `5X Isolated` |
| `2007` | `0x1581...463b` | `LONG` | 1,006,850.00 USD | `250.00` | `4003.77` | `4026.50` | `3504.62` | 5,906.41 USD | `+0.59%` | `15X Cross` |
| `2008` | `0xe47f...758c` | `LONG` | 1,006,850.00 USD | `250.00` | `4020.00` | `4026.50` | `3774.32` | 1,850.00 USD | `+0.18%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.50` (Vol: 281,800.00 USD, Dist: `+2.05%`) | Long MP=`3936.63` (Vol: 356,200.00 USD, Dist: `--2.27%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.74%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.26%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.72%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.25%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.07%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.20` | 16,450,000.00 USD | 16,450,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.90` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,370,000.00 USD | 16,370,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3616.10` | 3,670,000.00 USD | 3,670,000.00 USD | 32,630.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,220,000.00 USD | 16,220,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3620.30` | 3,640,000.00 USD | 3,640,000.00 USD | 27,560.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,170,000.00 USD | 16,170,000.00 USD | 88,630.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3624.50` | 3,600,000.00 USD | 3,600,000.00 USD | 47,000.00 USD | 0.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,060,000.00 USD | 16,060,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3628.70` | 3,550,000.00 USD | 3,550,000.00 USD | 40,670.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,860,000.00 USD | 15,860,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.90` | 3,500,000.00 USD | 3,500,000.00 USD | 23,790.00 USD | 0.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,740,000.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3637.10` | 3,480,000.00 USD | 3,480,000.00 USD | 46,440.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3641.30` | 3,420,000.00 USD | 3,420,000.00 USD | 17,190.00 USD | 0.00 USD | 5,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,600,000.00 USD | 15,600,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3645.50` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,540,000.00 USD | 15,540,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3649.70` | 3,400,000.00 USD | 3,400,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,510,000.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3653.90` | 3,370,000.00 USD | 3,370,000.00 USD | 19,450.00 USD | 0.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,490,000.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3658.10` | 3,350,000.00 USD | 3,350,000.00 USD | 6,980.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,430,000.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3662.30` | 3,340,000.00 USD | 3,340,000.00 USD | 7,410.00 USD | 0.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,420,000.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,400,000.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,390,000.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,970,000.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,450,000.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,920,000.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3855.50` | 3,330,000.00 USD | 3,330,000.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,630,000.00 USD | 13,630,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3859.70` | 3,260,000.00 USD | 3,260,000.00 USD | 47,060.00 USD | 0.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,210,000.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3863.90` | 3,210,000.00 USD | 3,210,000.00 USD | 142,990.00 USD | 0.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,030,000.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.10` | 3,060,000.00 USD | 3,060,000.00 USD | 156,000.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,690,000.00 USD | 12,690,000.00 USD | 615,690.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.30` | 2,880,000.00 USD | 2,880,000.00 USD | 132,230.00 USD | 0.00 USD | 19,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 12,030,000.00 USD | 12,030,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.50` | 2,720,000.00 USD | 2,720,000.00 USD | 85,580.00 USD | 0.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,650,000.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.70` | 2,630,000.00 USD | 2,630,000.00 USD | 125,260.00 USD | 0.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,060,000.00 USD | 11,060,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.90` | 2,490,000.00 USD | 2,490,000.00 USD | 30,560.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,850,000.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.10` | 2,440,000.00 USD | 2,440,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,760,000.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.30` | 2,410,000.00 USD | 2,410,000.00 USD | 69,580.00 USD | 0.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,630,000.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.50` | 2,340,000.00 USD | 2,340,000.00 USD | 41,140.00 USD | 0.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,500,000.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.70` | 2,290,000.00 USD | 2,290,000.00 USD | 24,120.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,380,000.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3905.90` | 2,260,000.00 USD | 2,260,000.00 USD | 17,740.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,330,000.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3910.10` | 2,240,000.00 USD | 2,240,000.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,280,000.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,250,000.00 USD | 10,250,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,890,000.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,100,000.00 USD | 9,100,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,120,000.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,010,000.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.30` | 2,220,000.00 USD | 2,220,000.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,510,000.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.50` | 2,130,000.00 USD | 2,130,000.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,790,000.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.70` | 1,980,000.00 USD | 1,980,000.00 USD | 193,530.00 USD | 0.00 USD | 13,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,360,000.00 USD | 5,360,000.00 USD | 617,970.00 USD | 0.00 USD | 123,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.90` | 1,780,000.00 USD | 1,780,000.00 USD | 358,170.00 USD | 0.00 USD | 48,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,620,000.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3952.10` | 1,370,000.00 USD | 1,370,000.00 USD | 269,020.00 USD | 0.00 USD | 39,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,450,000.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3956.30` | 1,060,000.00 USD | 1,060,000.00 USD | 126,930.00 USD | 0.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.50` | 913,890.00 USD | 913,890.00 USD | 298,450.00 USD | 0.00 USD | 37,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.70` | 577,760.00 USD | 577,760.00 USD | 103,610.00 USD | 0.00 USD | 29,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3968.90` | 444,540.00 USD | 444,540.00 USD | 3,860.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3973.10` | 422,410.00 USD | 422,410.00 USD | 136,790.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3977.30` | 276,830.00 USD | 276,830.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3981.50` | 170,290.00 USD | 170,290.00 USD | 48,970.00 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3985.70` | 102,700.00 USD | 102,700.00 USD | 51,230.00 USD | 0.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3989.90` | 46,860.00 USD | 46,860.00 USD | 41,610.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.90` | 65,020.00 USD | 65,020.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.10` | 208,440.00 USD | 208,440.00 USD | 132,300.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.30` | 382,800.00 USD | 382,800.00 USD | 162,650.00 USD | 0.00 USD | 11,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.50` | 729,730.00 USD | 729,730.00 USD | 309,220.00 USD | 0.00 USD | 37,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 1,030,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.70` | 1,080,000.00 USD | 1,080,000.00 USD | 316,350.00 USD | 0.00 USD | 38,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.90` | 1,280,000.00 USD | 1,280,000.00 USD | 161,350.00 USD | 0.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4120.10` | 1,500,000.00 USD | 1,500,000.00 USD | 219,130.00 USD | 0.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.30` | 1,720,000.00 USD | 1,720,000.00 USD | 167,900.00 USD | 0.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4128.50` | 1,790,000.00 USD | 1,790,000.00 USD | 45,250.00 USD | 0.00 USD | 24,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4132.70` | 1,860,000.00 USD | 1,860,000.00 USD | 52,390.00 USD | 0.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4136.90` | 2,020,000.00 USD | 2,020,000.00 USD | 147,720.00 USD | 0.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4141.10` | 2,080,000.00 USD | 2,080,000.00 USD | 62,390.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4145.30` | 2,140,000.00 USD | 2,140,000.00 USD | 48,240.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4149.50` | 2,190,000.00 USD | 2,190,000.00 USD | 35,490.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4153.70` | 2,220,000.00 USD | 2,220,000.00 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4174.70` | 2,240,000.00 USD | 2,240,000.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4178.90` | 2,330,000.00 USD | 2,330,000.00 USD | 84,040.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4183.10` | 2,400,000.00 USD | 2,400,000.00 USD | 65,710.00 USD | 0.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4187.30` | 2,590,000.00 USD | 2,590,000.00 USD | 170,230.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 12,990,000.00 USD | 12,990,000.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4191.50` | 2,720,000.00 USD | 2,720,000.00 USD | 121,870.00 USD | 0.00 USD | 18,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,630,000.00 USD | 13,630,000.00 USD | 600,710.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4195.70` | 2,850,000.00 USD | 2,850,000.00 USD | 106,090.00 USD | 0.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4199.90` | 2,950,000.00 USD | 2,950,000.00 USD | 92,770.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,490,000.00 USD | 14,490,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.10` | 3,070,000.00 USD | 3,070,000.00 USD | 103,700.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.30` | 3,110,000.00 USD | 3,110,000.00 USD | 30,560.00 USD | 0.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.50` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4216.70` | 3,200,000.00 USD | 3,200,000.00 USD | 70,190.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4220.90` | 3,250,000.00 USD | 3,250,000.00 USD | 47,870.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.10` | 3,280,000.00 USD | 3,280,000.00 USD | 22,780.00 USD | 0.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.30` | 3,310,000.00 USD | 3,310,000.00 USD | 27,320.00 USD | 0.00 USD | 604.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,330,000.00 USD | 15,330,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4233.50` | 3,330,000.00 USD | 3,330,000.00 USD | 20,800.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,390,000.00 USD | 15,390,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,540,000.00 USD | 15,540,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,800,000.00 USD | 15,800,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.10` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 674.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,980,000.00 USD | 15,980,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.30` | 3,360,000.00 USD | 3,360,000.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,090,000.00 USD | 16,090,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.50` | 3,370,000.00 USD | 3,370,000.00 USD | 7,800.00 USD | 0.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.70` | 3,410,000.00 USD | 3,410,000.00 USD | 32,190.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.90` | 3,470,000.00 USD | 3,470,000.00 USD | 53,120.00 USD | 0.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,380,000.00 USD | 16,380,000.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4435.10` | 3,500,000.00 USD | 3,500,000.00 USD | 25,850.00 USD | 0.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,500,000.00 USD | 16,500,000.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.90` | 3,530,000.00 USD | 3,530,000.00 USD | 21,740.00 USD | 0.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,620,000.00 USD | 16,620,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,700,000.00 USD | 16,700,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,750,000.00 USD | 16,750,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3611.90` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 1,110.00 USD |
| `7D` | `3615.50` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3616.10` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 32,630.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `3619.80` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3620.30` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 27,560.00 USD | 0.00 USD | 3,220.00 USD |
| `7D` | `3624.10` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 88,630.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3624.50` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 47,000.00 USD | 0.00 USD | 6,480.00 USD |
| `7D` | `3628.40` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3628.70` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 40,670.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `3632.70` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 112,500.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3632.90` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 23,790.00 USD | 0.00 USD | 5,630.00 USD |
| `7D` | `3637.00` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3637.10` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 46,440.00 USD | 0.00 USD | 5,190.00 USD |
| `1D` | `3641.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 17,190.00 USD | 0.00 USD | 5,510.00 USD |
| `7D` | `3641.30` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3645.50` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `3645.60` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3649.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 23,000.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3649.90` | 15,510,000.00 USD | 0.00 USD | 15,510,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3653.90` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 19,450.00 USD | 0.00 USD | 1,860.00 USD |
| `7D` | `3654.20` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3658.10` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 6,980.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3658.50` | 15,430,000.00 USD | 0.00 USD | 15,430,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3662.30` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 1,070.00 USD | 0.00 USD | 1,820.00 USD |
| `7D` | `3662.80` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3667.10` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.50` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD |
| `7D` | `3852.00` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3855.50` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `3856.30` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3859.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 47,060.00 USD | 0.00 USD | 5,540.00 USD |
| `7D` | `3860.60` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3863.90` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 142,990.00 USD | 0.00 USD | 8,940.00 USD |
| `7D` | `3864.90` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD |
| `1D` | `3868.10` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 159,700.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3869.20` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 615,690.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3872.30` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 141,010.00 USD | 0.00 USD | 19,130.00 USD |
| `7D` | `3873.50` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 331,860.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3876.50` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 85,580.00 USD | 0.00 USD | 8,340.00 USD |
| `7D` | `3877.80` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3880.70` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 125,260.00 USD | 0.00 USD | 19,810.00 USD |
| `7D` | `3882.10` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3884.90` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 30,560.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3886.40` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3889.10` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3890.70` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3893.30` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 69,580.00 USD | 0.00 USD | 4,860.00 USD |
| `7D` | `3895.00` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3897.50` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 41,140.00 USD | 0.00 USD | 4,250.00 USD |
| `7D` | `3899.30` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3901.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 24,120.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3903.60` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3905.90` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 17,740.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `3916.50` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `7D` | `3933.70` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3935.30` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 78,740.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3938.00` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3939.50` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 137,710.00 USD | 0.00 USD | 8,800.00 USD |
| `7D` | `3942.30` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3943.70` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 193,530.00 USD | 0.00 USD | 13,400.00 USD |
| `7D` | `3946.60` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 617,970.00 USD | 0.00 USD | 123,630.00 USD |
| `1D` | `3947.90` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 365,560.00 USD | 0.00 USD | 48,890.00 USD |
| `7D` | `3950.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,080,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3952.10` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 286,570.00 USD | 0.00 USD | 39,650.00 USD |
| `7D` | `3955.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 779,760.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3956.30` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 126,930.00 USD | 0.00 USD | 20,170.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3960.50` | 882,190.00 USD | 0.00 USD | 882,190.00 USD | 298,450.00 USD | 0.00 USD | 37,680.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3964.70` | 546,060.00 USD | 0.00 USD | 546,060.00 USD | 103,610.00 USD | 0.00 USD | 29,610.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3968.90` | 412,830.00 USD | 0.00 USD | 412,830.00 USD | 3,860.00 USD | 0.00 USD | 18,270.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3973.10` | 390,700.00 USD | 0.00 USD | 390,700.00 USD | 136,790.00 USD | 0.00 USD | 8,780.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3977.30` | 245,120.00 USD | 0.00 USD | 245,120.00 USD | 99,330.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3981.50` | 138,580.00 USD | 0.00 USD | 138,580.00 USD | 48,970.00 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3985.70` | 70,990.00 USD | 0.00 USD | 70,990.00 USD | 51,230.00 USD | 0.00 USD | 4,620.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `1D` | `3989.90` | 15,150.00 USD | 0.00 USD | 15,150.00 USD | 9,900.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4027.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4028.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD |
| `7D` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4094.90` | 65,020.00 USD | 65,020.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4099.10` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 132,300.00 USD | 0.00 USD | 11,120.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4103.30` | 382,800.00 USD | 382,800.00 USD | 0.00 USD | 162,650.00 USD | 0.00 USD | 11,700.00 USD |
| `7D` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD |
| `1D` | `4107.50` | 729,730.00 USD | 729,730.00 USD | 0.00 USD | 309,220.00 USD | 0.00 USD | 37,710.00 USD |
| `7D` | `4110.00` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4111.70` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 332,460.00 USD | 0.00 USD | 38,900.00 USD |
| `7D` | `4114.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 796,260.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4115.90` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 170,180.00 USD | 0.00 USD | 31,910.00 USD |
| `7D` | `4118.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4120.10` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 219,130.00 USD | 0.00 USD | 6,490.00 USD |
| `7D` | `4122.90` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4124.30` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 167,900.00 USD | 0.00 USD | 44,890.00 USD |
| `7D` | `4127.20` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4128.50` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 45,250.00 USD | 0.00 USD | 24,700.00 USD |
| `7D` | `4131.50` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4132.70` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 52,390.00 USD | 0.00 USD | 17,870.00 USD |
| `7D` | `4135.80` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4136.90` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 147,720.00 USD | 0.00 USD | 10,630.00 USD |
| `7D` | `4140.10` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4141.10` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 62,390.00 USD | 0.00 USD | 4,670.00 USD |
| `7D` | `4144.40` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4145.30` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 48,240.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4148.70` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4149.50` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 35,490.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `7D` | `4157.30` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.60` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.90` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4174.70` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `4178.80` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4178.90` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 5,560.00 USD |
| `1D` | `4183.10` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 65,710.00 USD | 0.00 USD | 5,850.00 USD |
| `7D` | `4183.10` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4187.30` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 170,230.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4187.40` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD |
| `1D` | `4191.50` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 125,570.00 USD | 0.00 USD | 18,090.00 USD |
| `7D` | `4191.70` | 13,630,000.00 USD | 13,630,000.00 USD | 0.00 USD | 600,710.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4195.70` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 114,870.00 USD | 0.00 USD | 17,270.00 USD |
| `7D` | `4196.00` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 309,010.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4199.90` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 92,770.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `4200.30` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4204.10` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 103,700.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `4204.60` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4208.30` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 30,560.00 USD | 0.00 USD | 13,700.00 USD |
| `7D` | `4208.90` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4212.50` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `4213.20` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4216.70` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 70,190.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4217.50` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4220.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 47,870.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4221.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4225.10` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 22,780.00 USD | 0.00 USD | 9,310.00 USD |
| `7D` | `4226.10` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4229.30` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | 604.20 USD |
| `7D` | `4230.40` | 15,330,000.00 USD | 15,330,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4233.50` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 4,950.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `4234.70` | 15,380,000.00 USD | 15,380,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.50` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,540,000.00 USD | 15,540,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `1D` | `4414.10` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.96 USD |
| `7D` | `4415.30` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4418.30` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `4419.60` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4422.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 1,620.00 USD |
| `7D` | `4423.90` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4426.70` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `4428.20` | 16,220,000.00 USD | 16,220,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD |
| `1D` | `4430.90` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 53,120.00 USD | 0.00 USD | 7,790.00 USD |
| `7D` | `4432.50` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4435.10` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 25,850.00 USD | 0.00 USD | 4,310.00 USD |
| `7D` | `4436.80` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 104,840.00 USD | 0.00 USD | 10,990.00 USD |
| `1D` | `4439.10` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 21,740.00 USD | 0.00 USD | 5,340.00 USD |
| `7D` | `4441.10` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.06M` | Total OI Tokens: `68,264.0 PAXG`
  * 1h OI Change: `+0.28%` | 4h OI Change: `+0.16%` | 24h OI Change: `-0.05%`
  * Exchange Breakdown: Binance=`107.41M` | Bybit=`19.95M` | OKX=`-` | Hyperliquid=`25.14M`
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
| `15M` | `PAXG` | `55.68%` | `44.32%` | `1.26` | 2,600,000.00 USD |
| `15M` | `Binance` | `56.58%` | `43.42%` | `1.30` | 1,500,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `53.08%` | `46.92%` | `1.13` | 82,390.00 USD |
| `15M` | `KuCoin` | `60.58%` | `39.42%` | `1.54` | 147,470.00 USD |
| `15M` | `Gate` | `45.06%` | `54.94%` | `0.82` | 30,490.00 USD |
| `15M` | `Bitget` | `56.86%` | `43.14%` | `1.32` | 590,870.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `53.29%` | `46.71%` | `1.14` | 4,780.00 USD |
| `15M` | `Bitunix` | `71.07%` | `28.93%` | `2.46` | 50,420.00 USD |
| `15M` | `Hyperliquid` | `65.47%` | `34.53%` | `1.90` | 12,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `38.34%` | `61.66%` | `0.62` | 175,720.00 USD |
| `15M` | `HTX` | `29.05%` | `70.95%` | `0.41` | 4,590.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `94.21%` | `5.79%` | `16.27` | 2,990.00 USD |
| `15M` | `Aster` | `77.42%` | `22.58%` | `3.43` | 124.96 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `21.45%` | `78.55%` | `0.27` | 2,440.00 USD |
| `15M` | `Whale Positions` | `56.58%` | `43.42%` | `1.30` | 1,500,000.00 USD |
| `15M` | `Global Accounts` | `55.68%` | `44.32%` | `1.26` | 2,600,000.00 USD |
| `1H` | `PAXG` | `57.23%` | `42.77%` | `1.34` | 4,630,000.00 USD |
| `1H` | `Binance` | `55.39%` | `44.61%` | `1.24` | 2,670,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `63.49%` | `36.51%` | `1.74` | 122,800.00 USD |
| `1H` | `KuCoin` | `55.68%` | `44.32%` | `1.26` | 279,940.00 USD |
| `1H` | `Gate` | `51.51%` | `48.49%` | `1.06` | 56,420.00 USD |
| `1H` | `Bitget` | `56.99%` | `43.01%` | `1.33` | 852,810.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `73.13%` | `26.87%` | `2.72` | 21,220.00 USD |
| `1H` | `Bitunix` | `63.12%` | `36.88%` | `1.71` | 85,230.00 USD |
| `1H` | `Hyperliquid` | `88.64%` | `11.36%` | `7.80` | 56,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `61.82%` | `38.18%` | `1.62` | 460,080.00 USD |
| `1H` | `HTX` | `54.54%` | `45.46%` | `1.20` | 8,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `96.43%` | `3.57%` | `27.01` | 6,650.00 USD |
| `1H` | `Aster` | `99.14%` | `0.86%` | `115.28` | 3,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `63.1%` | `36.9%` | `1.71` | 6,680.00 USD |
| `1H` | `Whale Positions` | `55.39%` | `44.61%` | `1.24` | 2,670,000.00 USD |
| `1H` | `Global Accounts` | `57.23%` | `42.77%` | `1.34` | 4,630,000.00 USD |
| `4H` | `PAXG` | `56.27%` | `43.73%` | `1.29` | 57,630,000.00 USD |
| `4H` | `Binance` | `58.33%` | `41.67%` | `1.40` | 4,510,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.02%` | `45.98%` | `1.17` | 5,850,000.00 USD |
| `4H` | `KuCoin` | `48.2%` | `51.8%` | `0.93` | 283,490.00 USD |
| `4H` | `Gate` | `58.23%` | `41.77%` | `1.39` | 2,170,000.00 USD |
| `4H` | `Bitget` | `50.33%` | `49.67%` | `1.01` | 1,990,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `58.2%` | `41.8%` | `1.39` | 35,290,000.00 USD |
| `4H` | `Bitunix` | `60.69%` | `39.31%` | `1.54` | 1,750,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.33%` | `45.67%` | `1.19` | 4,490,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `10.5%` | `89.5%` | `0.12` | 1,130,000.00 USD |
| `4H` | `HTX` | `67.02%` | `32.98%` | `2.03` | 12,710.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.71%` | `59.29%` | `0.69` | 161,350.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `58.33%` | `41.67%` | `1.40` | 4,510,000.00 USD |
| `4H` | `Global Accounts` | `56.27%` | `43.73%` | `1.29` | 57,630,000.00 USD |


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
| `5m` | -11,270.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -47,600.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -119,770.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -66,230.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -439,260.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -195,720.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | 93,790.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `8h` | -204,160.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -467,130.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | 11,690.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1w` | -8,270,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,810,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.27K` | 15m=`-47.60K` | 1h=`-66.23K` | 24h=`+11.69K`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4016.67` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4008.41` (Risk Distance: `8.26` pts)
  * +2.5R Take Profit: `4037.31`
  * Mathematical Lot Sizing: **`1.21 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4040.10` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4048.36` (Risk Distance: `8.26` pts)
  * +2.5R Take Profit: `4019.46`
  * Mathematical Lot Sizing: **`1.21 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4058.91`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
