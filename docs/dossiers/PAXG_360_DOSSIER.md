# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 10:46:56 IST` (`2026-10-30 05:16:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4001.05` | **Live Ask Quote**: `4001.13` | **Mid Price**: `4001.09`
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
  * Session VWAP: `4003.04` | VWAP Z-Score: `-1.03` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.55` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.67` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4021.36` | Lower -3.00σ Band: `3984.71`
  * Upper +2.51σ Band: `4018.37` | Lower -2.51σ Band: `3987.70`
  * Upper +2.01σ Band: `4015.32` | Lower -2.01σ Band: `3990.76`
  * Upper +2.00σ Band: `4015.25` | Lower -2.00σ Band: `3990.82`
  * Upper +1.28σ Band: `4010.86` | Lower -1.28σ Band: `3995.22`
  * Upper +1.00σ Band: `4009.15` | Lower -1.00σ Band: `3996.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3996.08` | EMA-20=`4000.89` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4009.63` (Slope: `+0.0000`) | EMA-100=`4018.45`
  * Institutional Anchors: EMA-144=`4022.64` | EMA-200=`4025.03` (Slope: `-0.0871`) | EMA-233=`4026.89`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.04` (Distance: `-0.30%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.15%`)
  * Value Area Low (VAL) = `3996.44` (Distance: `+0.12%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4001.83` | Low=`3996.58`
  * New York Session (13:00-21:00 UTC): High=`4025.10` | Low=`3977.08`
  * Initial Balance (First Hour): IB High=`4001.83` | IB Low=`3996.58`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3985.09` - `4017.09`
  * Optimal Trade Entry (OTE 0.705): `4009.09`
  * Structural Invalidation Anchor (0.786): `4033.10`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4002.94` | `4006.91` | `4002.94` | `4004.37` | `118` | 474,397.00 USD | 176,598.99 USD | `+37.23%` | -246,594.81 USD | `+0.94` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4004.37` | `4008.06` | `4003.79` | `4008.06` | `145` | 582,787.13 USD | 370,046.56 USD | `+63.50%` | 123,451.75 USD | `+1.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4008.05` | `4009.65` | `4008.05` | `4009.19` | `38` | 153,156.68 USD | 15,935.03 USD | `+10.40%` | 139,386.78 USD | `-0.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4002.91` | `4005.00` | `3998.22` | `4000.31` | `196` | 783,504.25 USD | -463,603.73 USD | `-59.17%` | -883,864.39 USD | `-1.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4000.32` | `4003.79` | `3999.97` | `4002.94` | `232` | 930,315.12 USD | 460,670.59 USD | `+49.52%` | -423,193.80 USD | `+1.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4002.94` | `4009.65` | `4002.94` | `4009.19` | `302` | 1,210,340.81 USD | 562,580.58 USD | `+46.48%` | 139,386.78 USD | `+1.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -446,454.31 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -9,185.48 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4009.65` | `4002.94` | `4009.19` | `302` | 1,210,340.81 USD | 562,580.58 USD | `+46.48%` | 553,395.10 USD | `+1.10` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4009.65` | `3995.14` | `4009.19` | `2,092` | 8,368,706.96 USD | 999,849.41 USD | `+11.95%` | 947,757.87 USD | `+1.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4009.65` | `3995.14` | `4009.19` | `2,092` | 8,368,706.96 USD | 999,849.41 USD | `+11.95%` | 947,757.87 USD | `+1.02` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `4000.40` | `14.4531` | 57,818.18 USD | 882,998.77 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4000.50` | `2.8786` | 11,515.84 USD | 825,180.59 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4000.60` | `10.6287` | 42,521.18 USD | 813,664.75 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4000.70` | `7.9805` | 31,927.59 USD | 771,143.57 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4000.80` | `58.8168` | 235,314.25 USD | 739,215.99 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4000.90` | `14.9875` | 59,963.49 USD | 503,901.73 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4001.00` | `25.7686` | 103,100.17 USD | 443,938.25 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4001.10` | `5.2469` | 20,993.37 USD | 340,838.08 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4001.20` | `17.1298` | 68,539.76 USD | 319,844.71 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4001.30` | `9.8948` | 39,592.06 USD | 251,304.95 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4001.40` | `26.5548` | 106,256.38 USD | 211,712.89 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4001.50` | `0.4921` | 1,969.14 USD | 105,456.51 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4001.60` | `6.1860` | 24,753.90 USD | 103,487.37 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4001.70` | `0.9953` | 3,982.89 USD | 78,733.47 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4001.80` | `3.7483` | 14,999.95 USD | 74,750.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4001.90` | `3.7482` | 14,999.92 USD | 59,750.64 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4002.00` | `1.2460` | 4,986.49 USD | 44,750.71 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4002.10` | `8.9946` | 35,997.29 USD | 39,764.22 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4002.20` | `0.7327` | 2,932.41 USD | 3,766.93 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4002.50` | `0.2085` | 834.52 USD | 834.52 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4002.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,002.55` | `0.00%` | `-` |
| `ASK` | `4002.60` | `56.8656` | 227,610.25 USD | 227,610.25 USD | `10 orders` | `+0.00%` | `-` |
| `ASK` | `4002.70` | `16.2512` | 65,048.68 USD | 292,658.93 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4002.80` | `5.0998` | 20,413.48 USD | 313,072.41 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4002.90` | `3.7472` | 14,999.67 USD | 328,072.08 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4003.00` | `5.2463` | 21,000.94 USD | 349,073.01 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4003.10` | `3.7470` | 14,999.62 USD | 364,072.63 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4003.20` | `54.7196` | 219,053.50 USD | 583,126.13 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4003.30` | `5.2463` | 21,002.51 USD | 604,128.65 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4003.50` | `8.2926` | 33,199.42 USD | 637,328.07 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4003.60` | `20.0925` | 80,442.33 USD | 717,770.40 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4003.70` | `6.7740` | 27,121.06 USD | 744,891.47 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4003.80` | `8.6426` | 34,603.24 USD | 779,494.71 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4003.90` | `11.3061` | 45,268.49 USD | 824,763.20 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4004.00` | `86.0045` | 344,362.02 USD | 1,169,125.22 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4004.10` | `5.2466` | 21,007.91 USD | 1,190,133.13 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4004.20` | `6.9223` | 27,718.27 USD | 1,217,851.40 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4004.30` | `0.2497` | 999.87 USD | 1,218,851.28 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4004.40` | `5.7148` | 22,884.35 USD | 1,241,735.62 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4004.50` | `1.3415` | 5,372.04 USD | 1,247,107.66 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4004.60` | `4.7073` | 18,850.85 USD | 1,265,958.51 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,965,785.82 USD | `6,489.82` | `4185.46` | `4000.60` | `29243.65` | 1,197,165.19 USD | `+4.61%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,245,230.13 USD | `6,309.73` | `4129.12` | `4000.60` | `13945.92` | 808,429.68 USD | `+3.20%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,487,228.47 USD | `5,869.90` | `4228.86` | `4000.60` | `26877.59` | 1,335,793.47 USD | `+5.69%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,320,456.51 USD | `4,828.91` | `4157.43` | `4000.60` | `2262.93` | -755,425.81 USD | `-3.91%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,209,518.29 USD | `3,551.49` | `4127.82` | `4000.60` | `591.16` | -450,423.66 USD | `-3.17%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,076,121.01 USD | `3,268.21` | `4228.94` | `4000.60` | `4373.16` | 744,958.12 USD | `+5.70%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,602,900.40 USD | `2,900.00` | `4364.92` | `4000.60` | `4235.92` | 1,055,375.93 USD | `+9.10%` | `20X Cross` |
| `264` | `0x41e5...0825` | `SHORT` | 8,802,860.00 USD | `2,200.00` | `4112.20` | `4000.60` | `4331.40` | 243,994.59 USD | `+2.77%` | `20X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,802,420.00 USD | `2,200.00` | `4176.09` | `4000.60` | `2594.95` | -384,999.30 USD | `-4.37%` | `25X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,904,044.38 USD | `1,975.37` | `4048.55` | `4000.60` | `6578.70` | 93,347.33 USD | `+1.18%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,321,387.15 USD | `1,579.95` | `4075.62` | `4000.60` | `0.000000` | -117,909.82 USD | `-1.87%` | `1X Cross` |
| `568` | `0x63da...8add` | `LONG` | 4,001,000.00 USD | `1,000.00` | `4021.46` | `4000.60` | `3564.37` | -20,460.96 USD | `-0.51%` | `25X Cross` |
| `577` | `0xf3dc...1672` | `LONG` | 3,938,165.50 USD | `984.27` | `4018.39` | `4000.60` | `2911.94` | -17,021.20 USD | `-0.43%` | `20X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,887,539.64 USD | `971.64` | `4279.98` | `4000.60` | `0.000000` | -271,069.44 USD | `-6.97%` | `20X Cross` |
| `597` | `0x354b...6425` | `LONG` | 3,837,955.55 USD | `959.23` | `4004.93` | `4000.60` | `0.000000` | -3,678.53 USD | `-0.10%` | `10X Cross` |
| `678` | `0x4a20...3c26` | `LONG` | 3,350,519.94 USD | `837.40` | `4599.73` | `4000.60` | `0.000000` | -501,300.44 USD | `-14.96%` | `20X Cross` |
| `831` | `0x0fac...7a0a` | `LONG` | 2,746,626.48 USD | `686.49` | `4290.34` | `4000.60` | `1178.71` | -198,632.22 USD | `-7.23%` | `25X Cross` |
| `910` | `0x625e...a354` | `SHORT` | 2,480,806.00 USD | `620.00` | `4122.81` | `4000.60` | `4342.50` | 75,341.03 USD | `+3.04%` | `20X Cross` |
| `916` | `0xd8c5...99b0` | `SHORT` | 2,474,099.79 USD | `618.35` | `4175.35` | `4000.60` | `34155.67` | 107,752.81 USD | `+4.36%` | `4X Cross` |
| `938` | `0xeae3...e8ad` | `SHORT` | 2,400,660.00 USD | `600.00` | `4104.77` | `4000.60` | `4325.52` | 62,205.11 USD | `+2.59%` | `20X Cross` |
| `941` | `0xf285...fa82` | `LONG` | 2,393,021.71 USD | `598.11` | `4146.45` | `4000.60` | `3891.51` | -86,997.85 USD | `-3.64%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,343,028.41 USD | `585.61` | `4082.77` | `4000.60` | `2595.93` | -47,888.57 USD | `-2.04%` | `10X Cross` |
| `1097` | `0x413c...886c` | `LONG` | 2,000,550.00 USD | `500.00` | `4010.43` | `4000.60` | `0.000000` | -4,666.23 USD | `-0.23%` | `2X Cross` |
| `1101` | `0x9c06...0560` | `LONG` | 1,994,167.62 USD | `498.42` | `4012.76` | `4000.60` | `0.000000` | -5,863.88 USD | `-0.29%` | `25X Cross` |
| `1104` | `0x61ce...a62b` | `SHORT` | 1,990,561.25 USD | `497.50` | `4071.66` | `4000.60` | `4715.24` | 35,107.54 USD | `+1.76%` | `20X Cross` |
| `1179` | `0x2edd...8179` | `LONG` | 1,883,123.15 USD | `469.89` | `4164.68` | `4007.20` | `0.000000` | -73,809.37 USD | `-3.92%` | `10X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,815,725.52 USD | `453.78` | `4220.88` | `4000.60` | `3539.20` | -99,642.54 USD | `-5.49%` | `5X Isolated` |
| `1276` | `0x7a6d...f79c` | `SHORT` | 1,716,686.00 USD | `428.38` | `4136.09` | `4007.20` | `5358.06` | 55,129.00 USD | `+3.21%` | `10X Cross` |
| `1288` | `0x46fc...1195` | `LONG` | 1,689,030.76 USD | `422.14` | `4053.27` | `4000.60` | `2161.72` | -22,024.11 USD | `-1.30%` | `20X Cross` |
| `1352` | `0x6d15...d374` | `LONG` | 1,600,520.00 USD | `400.00` | `4068.25` | `4000.60` | `3842.07` | -26,780.00 USD | `-1.67%` | `25X Cross` |
| `1353` | `0xee02...309d` | `SHORT` | 1,600,400.00 USD | `400.00` | `4438.84` | `4000.60` | `4227.14` | 175,138.60 USD | `+10.94%` | `25X Isolated` |
| `1392` | `0x51f6...2b39` | `LONG` | 1,564,348.54 USD | `390.33` | `4228.91` | `4007.20` | `563.24` | -86,304.55 USD | `-5.52%` | `10X Cross` |
| `1398` | `0x02a7...fe9f` | `SHORT` | 1,560,390.00 USD | `390.00` | `4055.02` | `4000.60` | `4306.96` | 21,069.25 USD | `+1.35%` | `25X Cross` |
| `1442` | `0x7e77...b8d2` | `SHORT` | 1,520,418.00 USD | `380.00` | `4131.92` | `4000.60` | `4293.77` | 49,711.64 USD | `+3.27%` | `20X Cross` |
| `1464` | `0x72c2...9b37` | `LONG` | 1,492,935.64 USD | `373.13` | `4000.98` | `4000.60` | `3778.31` | 42.13 USD | `+0.00%` | `13X Isolated` |
| `1505` | `0x781e...96b7` | `SHORT` | 1,447,256.66 USD | `361.11` | `4363.51` | `4007.20` | `12925.09` | 128,449.98 USD | `+8.88%` | `10X Cross` |
| `1511` | `0xaa44...b844` | `LONG` | 1,440,396.00 USD | `360.00` | `4043.10` | `4000.60` | `2819.07` | -15,121.63 USD | `-1.05%` | `4X Cross` |
| `1617` | `0xa41f...d50a` | `LONG` | 1,316,177.36 USD | `328.96` | `4468.89` | `4000.60` | `3802.43` | -153,920.49 USD | `-11.69%` | `15X Cross` |
| `1634` | `0x7fda...17d1` | `SHORT` | 1,300,544.65 USD | `325.05` | `4013.13` | `4000.60` | `30382.08` | 3,943.32 USD | `+0.30%` | `20X Cross` |
| `1666` | `0xbf5a...88ba` | `SHORT` | 1,270,937.25 USD | `317.65` | `4091.80` | `4000.60` | `10000.26` | 28,845.78 USD | `+2.27%` | `20X Cross` |
| `1701` | `0xff31...ff6c` | `SHORT` | 1,240,341.00 USD | `310.00` | `4372.43` | `4000.60` | `4789.43` | 115,114.38 USD | `+9.28%` | `10X Isolated` |
| `1725` | `0xada6...6f88` | `LONG` | 1,214,325.05 USD | `303.50` | `4166.46` | `4000.60` | `1787.91` | -50,187.82 USD | `-4.13%` | `5X Cross` |
| `1891` | `0x50e2...d770` | `LONG` | 1,081,767.00 USD | `270.37` | `4243.58` | `4000.60` | `2562.36` | -65,559.46 USD | `-6.06%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,067,175.39 USD | `266.72` | `4260.98` | `4000.60` | `6517.93` | 69,316.84 USD | `+6.50%` | `20X Cross` |
| `1990` | `0xd346...c4f3` | `LONG` | 1,020,950.37 USD | `255.17` | `4188.66` | `4000.60` | `3310.69` | -47,886.13 USD | `-4.69%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.81` (Vol: 274,500.00 USD, Dist: `+2.67%`) | Long MP=`3936.71` (Vol: 378,100.00 USD, Dist: `--1.65%`)
  * 48H Horizon: Short MP=`4097.67` (Vol: 378,100.00 USD, Dist: `+2.37%`) | Long MP=`3936.55` (Vol: 378,100.00 USD, Dist: `--1.66%`)
  * 3D Horizon: Short MP=`4097.67` (Vol: 405,200.00 USD, Dist: `+2.37%`) | Long MP=`3936.55` (Vol: 405,200.00 USD, Dist: `--1.66%`)
  * 7D Horizon: Short MP=`4086.63` (Vol: 910,300.00 USD, Dist: `+2.09%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--2.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3596.10` | 16,690,000.00 USD | 16,690,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.40` | 4,890,000.00 USD | 4,890,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,660,000.00 USD | 16,660,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.50` | 4,880,000.00 USD | 4,880,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 16,500,000.00 USD | 16,500,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.60` | 4,820,000.00 USD | 4,820,000.00 USD | 55,240.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 16,230,000.00 USD | 16,230,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.70` | 4,760,000.00 USD | 4,760,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 16,040,000.00 USD | 16,040,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.80` | 4,730,000.00 USD | 4,730,000.00 USD | 31,710.00 USD | 0.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,940,000.00 USD | 15,940,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.90` | 4,700,000.00 USD | 4,700,000.00 USD | 46,830.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,820,000.00 USD | 15,820,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 4,640,000.00 USD | 4,640,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,740,000.00 USD | 15,740,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.10` | 4,560,000.00 USD | 4,560,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,660,000.00 USD | 15,660,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 4,520,000.00 USD | 4,520,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 15,540,000.00 USD | 15,540,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.30` | 4,480,000.00 USD | 4,480,000.00 USD | 14,390.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 15,450,000.00 USD | 15,450,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.40` | 4,460,000.00 USD | 4,460,000.00 USD | 6,330.00 USD | 0.00 USD | 205.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 15,390,000.00 USD | 15,390,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.50` | 4,460,000.00 USD | 4,460,000.00 USD | 3,000.00 USD | 0.00 USD | 592.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 15,340,000.00 USD | 15,340,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 15,310,000.00 USD | 15,310,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 15,280,000.00 USD | 15,280,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 15,230,000.00 USD | 15,230,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 15,220,000.00 USD | 15,220,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 15,210,000.00 USD | 15,210,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 15,190,000.00 USD | 15,190,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.30` | 4,450,000.00 USD | 4,450,000.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,990,000.00 USD | 14,990,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.40` | 4,370,000.00 USD | 4,370,000.00 USD | 183,520.00 USD | 0.00 USD | 102,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 14,330,000.00 USD | 14,330,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.50` | 4,090,000.00 USD | 4,090,000.00 USD | 46,980.00 USD | 0.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,640,000.00 USD | 13,640,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.60` | 4,020,000.00 USD | 4,020,000.00 USD | 85,690.00 USD | 0.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 13,100,000.00 USD | 13,100,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.70` | 3,920,000.00 USD | 3,920,000.00 USD | 96,830.00 USD | 0.00 USD | 15,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,800,000.00 USD | 12,800,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,810,000.00 USD | 3,810,000.00 USD | 159,360.00 USD | 0.00 USD | 32,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 12,390,000.00 USD | 12,390,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.90` | 3,610,000.00 USD | 3,610,000.00 USD | 214,000.00 USD | 0.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 12,140,000.00 USD | 12,140,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.00` | 3,370,000.00 USD | 3,370,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,860,000.00 USD | 11,860,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.10` | 3,200,000.00 USD | 3,200,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,540,000.00 USD | 11,540,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.20` | 3,060,000.00 USD | 3,060,000.00 USD | 54,860.00 USD | 0.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 11,150,000.00 USD | 11,150,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.30` | 3,000,000.00 USD | 3,000,000.00 USD | 16,620.00 USD | 0.00 USD | 981.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,830,000.00 USD | 10,830,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.40` | 2,980,000.00 USD | 2,980,000.00 USD | 13,610.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,680,000.00 USD | 10,680,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,570,000.00 USD | 10,570,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,440,000.00 USD | 10,440,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 10,330,000.00 USD | 10,330,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 10,240,000.00 USD | 10,240,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 10,170,000.00 USD | 10,170,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.20` | 2,970,000.00 USD | 2,970,000.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 10,120,000.00 USD | 10,120,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.30` | 2,930,000.00 USD | 2,930,000.00 USD | 132,900.00 USD | 0.00 USD | 148,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 9,220,000.00 USD | 9,220,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.40` | 2,640,000.00 USD | 2,640,000.00 USD | 346,980.00 USD | 0.00 USD | 152,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,820,000.00 USD | 7,820,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.50` | 2,140,000.00 USD | 2,140,000.00 USD | 56,230.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,460,000.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 2,060,000.00 USD | 2,060,000.00 USD | 221,570.00 USD | 0.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,710,000.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.70` | 1,790,000.00 USD | 1,790,000.00 USD | 215,190.00 USD | 0.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,800,000.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.80` | 1,550,000.00 USD | 1,550,000.00 USD | 330,910.00 USD | 0.00 USD | 64,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,410,000.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.90` | 1,160,000.00 USD | 1,160,000.00 USD | 360,350.00 USD | 0.00 USD | 57,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,860,000.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.00` | 740,440.00 USD | 740,440.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 3,200,000.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.10` | 355,110.00 USD | 355,110.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,580,000.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.20` | 143,800.00 USD | 143,800.00 USD | 92,090.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,820,000.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.30` | 49,250.00 USD | 49,250.00 USD | 25,790.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 21,000.00 USD | 21,000.00 USD | 18,860.00 USD | 0.00 USD | 2,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.10` | 44,190.00 USD | 44,190.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.20` | 319,490.00 USD | 319,490.00 USD | 132,900.00 USD | 0.00 USD | 142,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.30` | 795,350.00 USD | 795,350.00 USD | 317,470.00 USD | 0.00 USD | 158,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.40` | 891,210.00 USD | 891,210.00 USD | 70,210.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.50` | 1,130,000.00 USD | 1,130,000.00 USD | 195,060.00 USD | 0.00 USD | 41,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,800,000.00 USD | 4,800,000.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.60` | 1,340,000.00 USD | 1,340,000.00 USD | 188,180.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,540,000.00 USD | 5,540,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.70` | 1,710,000.00 USD | 1,710,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 6,040,000.00 USD | 6,040,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 2,210,000.00 USD | 2,210,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,630,000.00 USD | 6,630,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.90` | 2,520,000.00 USD | 2,520,000.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,110,000.00 USD | 7,110,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.00` | 2,790,000.00 USD | 2,790,000.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,730,000.00 USD | 7,730,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.10` | 2,900,000.00 USD | 2,900,000.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,530,000.00 USD | 8,530,000.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.20` | 2,930,000.00 USD | 2,930,000.00 USD | 28,520.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,960,000.00 USD | 8,960,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.30` | 2,970,000.00 USD | 2,970,000.00 USD | 31,940.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 9,140,000.00 USD | 9,140,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 538.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,380,000.00 USD | 9,380,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,620,000.00 USD | 9,620,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,900,000.00 USD | 9,900,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,960,000.00 USD | 9,960,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 10,090,000.00 USD | 10,090,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 10,160,000.00 USD | 10,160,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,630,000.00 USD | 10,630,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.10` | 3,040,000.00 USD | 3,040,000.00 USD | 37,720.00 USD | 0.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,380,000.00 USD | 11,380,000.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.20` | 3,310,000.00 USD | 3,310,000.00 USD | 184,330.00 USD | 0.00 USD | 85,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,970,000.00 USD | 11,970,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.30` | 3,400,000.00 USD | 3,400,000.00 USD | 53,170.00 USD | 0.00 USD | 31,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,340,000.00 USD | 12,340,000.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4172.40` | 3,470,000.00 USD | 3,470,000.00 USD | 54,040.00 USD | 0.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.50` | 3,590,000.00 USD | 3,590,000.00 USD | 95,500.00 USD | 0.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,800,000.00 USD | 12,800,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.60` | 3,710,000.00 USD | 3,710,000.00 USD | 112,920.00 USD | 0.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,990,000.00 USD | 12,990,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.70` | 3,880,000.00 USD | 3,880,000.00 USD | 142,270.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 13,210,000.00 USD | 13,210,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.80` | 4,110,000.00 USD | 4,110,000.00 USD | 197,110.00 USD | 0.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,500,000.00 USD | 13,500,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 4,280,000.00 USD | 4,280,000.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,790,000.00 USD | 13,790,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.00` | 4,380,000.00 USD | 4,380,000.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 14,120,000.00 USD | 14,120,000.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.10` | 4,420,000.00 USD | 4,420,000.00 USD | 40,760.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 14,420,000.00 USD | 14,420,000.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 4,440,000.00 USD | 4,440,000.00 USD | 14,000.00 USD | 0.00 USD | 817.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,640,000.00 USD | 14,640,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.30` | 4,450,000.00 USD | 4,450,000.00 USD | 13,610.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,720,000.00 USD | 14,720,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,840,000.00 USD | 14,840,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,960,000.00 USD | 14,960,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 15,080,000.00 USD | 15,080,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 15,110,000.00 USD | 15,110,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 15,180,000.00 USD | 15,180,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 15,200,000.00 USD | 15,200,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 15,260,000.00 USD | 15,260,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4397.90` | 4,460,000.00 USD | 4,460,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 15,390,000.00 USD | 15,390,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4402.00` | 4,500,000.00 USD | 4,500,000.00 USD | 14,970.00 USD | 0.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,610,000.00 USD | 15,610,000.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4406.10` | 4,580,000.00 USD | 4,580,000.00 USD | 52,600.00 USD | 0.00 USD | 23,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,790,000.00 USD | 15,790,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4410.10` | 4,590,000.00 USD | 4,590,000.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,880,000.00 USD | 15,880,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,980,000.00 USD | 15,980,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 16,070,000.00 USD | 16,070,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 16,130,000.00 USD | 16,130,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,200,000.00 USD | 16,200,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 16,270,000.00 USD | 16,270,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 16,360,000.00 USD | 16,360,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 16,400,000.00 USD | 16,400,000.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.10` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3598.40` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.40` | 16,660,000.00 USD | 0.00 USD | 16,660,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3602.50` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD |
| `7D` | `3604.70` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.60` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 55,240.00 USD | 0.00 USD | 11,510.00 USD |
| `7D` | `3609.00` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.70` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `3613.30` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3614.80` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 31,710.00 USD | 0.00 USD | 7,820.00 USD |
| `7D` | `3617.60` | 15,940,000.00 USD | 0.00 USD | 15,940,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3618.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 46,830.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3621.90` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3623.00` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD |
| `7D` | `3626.20` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.10` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD |
| `7D` | `3630.50` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.20` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3634.80` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.30` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 14,390.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.10` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3639.40` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 6,330.00 USD | 0.00 USD | 205.66 USD |
| `7D` | `3643.40` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `3643.50` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 3,000.00 USD | 0.00 USD | 592.01 USD |
| `7D` | `3647.70` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `3840.30` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `3841.20` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3844.40` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 183,520.00 USD | 0.00 USD | 102,820.00 USD |
| `7D` | `3845.50` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3848.50` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 46,980.00 USD | 0.00 USD | 17,960.00 USD |
| `7D` | `3849.80` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3852.60` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 85,690.00 USD | 0.00 USD | 19,430.00 USD |
| `7D` | `3854.10` | 13,100,000.00 USD | 0.00 USD | 13,100,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD |
| `1D` | `3856.70` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 96,830.00 USD | 0.00 USD | 15,800.00 USD |
| `7D` | `3858.40` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3860.80` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 159,360.00 USD | 0.00 USD | 32,070.00 USD |
| `7D` | `3862.70` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3864.90` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 214,000.00 USD | 0.00 USD | 29,400.00 USD |
| `7D` | `3867.00` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3869.00` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD |
| `7D` | `3871.30` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3873.10` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD |
| `7D` | `3875.60` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3877.20` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 54,860.00 USD | 0.00 USD | 3,850.00 USD |
| `7D` | `3879.90` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3881.30` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 16,620.00 USD | 0.00 USD | 981.17 USD |
| `7D` | `3884.20` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3885.40` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 13,610.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `3888.50` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `1D` | `3918.20` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3918.60` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3922.30` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 132,900.00 USD | 0.00 USD | 148,480.00 USD |
| `7D` | `3922.90` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3926.40` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 346,980.00 USD | 0.00 USD | 152,310.00 USD |
| `7D` | `3927.20` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3930.50` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 56,230.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `3931.50` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD |
| `1D` | `3934.60` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 221,570.00 USD | 0.00 USD | 51,400.00 USD |
| `7D` | `3935.80` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3938.70` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 215,190.00 USD | 0.00 USD | 21,520.00 USD |
| `7D` | `3940.10` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3942.80` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 330,910.00 USD | 0.00 USD | 64,500.00 USD |
| `7D` | `3944.40` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3946.90` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 360,350.00 USD | 0.00 USD | 57,110.00 USD |
| `7D` | `3948.70` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3951.00` | 740,440.00 USD | 0.00 USD | 740,440.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD |
| `7D` | `3953.00` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3955.10` | 355,110.00 USD | 0.00 USD | 355,110.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3957.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3959.20` | 143,800.00 USD | 0.00 USD | 143,800.00 USD | 92,090.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3961.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.30` | 49,250.00 USD | 0.00 USD | 49,250.00 USD | 25,790.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `3967.40` | 21,000.00 USD | 0.00 USD | 21,000.00 USD | 18,860.00 USD | 0.00 USD | 2,130.00 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4006.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4007.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4078.10` | 44,190.00 USD | 44,190.00 USD | 0.00 USD | 44,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4082.20` | 319,490.00 USD | 319,490.00 USD | 0.00 USD | 132,900.00 USD | 0.00 USD | 142,400.00 USD |
| `1D` | `4086.30` | 795,350.00 USD | 795,350.00 USD | 0.00 USD | 317,470.00 USD | 0.00 USD | 158,390.00 USD |
| `7D` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4090.40` | 891,210.00 USD | 891,210.00 USD | 0.00 USD | 70,210.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4094.50` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 41,230.00 USD |
| `7D` | `4094.90` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD |
| `1D` | `4098.60` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 188,180.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `4099.20` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.70` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD |
| `7D` | `4103.50` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4106.80` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `4107.80` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4110.90` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD |
| `7D` | `4112.10` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4115.00` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `4116.40` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4119.10` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD |
| `7D` | `4120.70` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.20` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 28,520.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4125.00` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `4127.30` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 31,940.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `4129.30` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `1D` | `4131.40` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 538.62 USD |
| `7D` | `4133.60` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.10` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 37,720.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `4163.70` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4164.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 184,330.00 USD | 0.00 USD | 85,280.00 USD |
| `7D` | `4168.00` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.30` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 53,170.00 USD | 0.00 USD | 31,320.00 USD |
| `7D` | `4172.30` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD |
| `1D` | `4172.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 54,040.00 USD | 0.00 USD | 14,480.00 USD |
| `1D` | `4176.50` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 95,500.00 USD | 0.00 USD | 24,450.00 USD |
| `7D` | `4176.60` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4180.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 112,920.00 USD | 0.00 USD | 12,590.00 USD |
| `7D` | `4180.90` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4184.70` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 142,270.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `4185.20` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4188.80` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 197,110.00 USD | 0.00 USD | 27,480.00 USD |
| `7D` | `4189.50` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4192.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4193.80` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4197.00` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4198.10` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4201.10` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 40,760.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4202.40` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4205.20` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD | 817.23 USD |
| `7D` | `4206.70` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `4209.30` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 13,610.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `4211.00` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `7D` | `4215.30` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4397.90` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4400.20` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4402.00` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 14,970.00 USD | 0.00 USD | 23,850.00 USD |
| `7D` | `4404.50` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4406.10` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 52,600.00 USD | 0.00 USD | 23,490.00 USD |
| `7D` | `4408.80` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `1D` | `4410.10` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4413.10` | 15,880,000.00 USD | 15,880,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `4417.40` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `7D` | `4421.70` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4426.00` | 16,130,000.00 USD | 16,130,000.00 USD | 0.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.30` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.60` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.90` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4440.70` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `276.38M` | Total OI Tokens: `68,963.6 PAXG`
  * 1h OI Change: `-0.08%` | 4h OI Change: `+0.47%` | 24h OI Change: `+0.84%`
  * Exchange Breakdown: Binance=`107.26M` | Bybit=`22.11M` | OKX=`-` | Hyperliquid=`24.73M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.71K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `42.99%` | `57.01%` | `0.75` | 2,420,000.00 USD |
| `15M` | `Binance` | `38.07%` | `61.93%` | `0.61` | 728,560.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `52.02%` | `47.98%` | `1.08` | 227,100.00 USD |
| `15M` | `KuCoin` | `51.09%` | `48.91%` | `1.04` | 11,470.00 USD |
| `15M` | `Gate` | `71.02%` | `28.98%` | `2.45` | 102,790.00 USD |
| `15M` | `Bitget` | `30.58%` | `69.42%` | `0.44` | 101,650.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `27.76%` | `72.24%` | `0.38` | 719,230.00 USD |
| `15M` | `Bitunix` | `74.32%` | `25.68%` | `2.89` | 164,870.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `78.08%` | `21.92%` | `3.56` | 239,100.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `20.88%` | `79.12%` | `0.26` | 120,810.00 USD |
| `15M` | `HTX` | `2.09%` | `97.91%` | `0.02` | 2,870.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `38.07%` | `61.93%` | `0.61` | 728,560.00 USD |
| `15M` | `Global Accounts` | `42.99%` | `57.01%` | `0.75` | 2,420,000.00 USD |
| `1H` | `PAXG` | `43.19%` | `56.81%` | `0.76` | 13,060,000.00 USD |
| `1H` | `Binance` | `47.52%` | `52.48%` | `0.91` | 1,830,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `47.66%` | `52.34%` | `0.91` | 708,720.00 USD |
| `1H` | `KuCoin` | `44.12%` | `55.88%` | `0.79` | 42,660.00 USD |
| `1H` | `Gate` | `48.31%` | `51.69%` | `0.93` | 506,790.00 USD |
| `1H` | `Bitget` | `35.91%` | `64.09%` | `0.56` | 441,550.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `40.68%` | `59.32%` | `0.69` | 8,080,000.00 USD |
| `1H` | `Bitunix` | `44.57%` | `55.43%` | `0.80` | 447,820.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `65.03%` | `34.97%` | `1.86` | 533,350.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `17.16%` | `82.84%` | `0.21` | 337,000.00 USD |
| `1H` | `HTX` | `89.96%` | `10.04%` | `8.96` | 133,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `47.52%` | `52.48%` | `0.91` | 1,830,000.00 USD |
| `1H` | `Global Accounts` | `43.19%` | `56.81%` | `0.76` | 13,060,000.00 USD |
| `4H` | `PAXG` | `43.56%` | `56.44%` | `0.77` | 25,910,000.00 USD |
| `4H` | `Binance` | `51.06%` | `48.94%` | `1.04` | 8,450,000.00 USD |
| `4H` | `OKX` | `51.38%` | `48.62%` | `1.06` | 2,300,000.00 USD |
| `4H` | `Bybit` | `53.1%` | `46.9%` | `1.13` | 2,840,000.00 USD |
| `4H` | `KuCoin` | `50%` | `50%` | `1.00` | 1,100,000.00 USD |
| `4H` | `Gate` | `48.08%` | `51.92%` | `0.93` | 388,950.00 USD |
| `4H` | `Bitget` | `48.01%` | `51.99%` | `0.92` | 424,700.00 USD |
| `4H` | `BingX` | `8.74%` | `91.26%` | `0.10` | 4,430,000.00 USD |
| `4H` | `MEXC` | `46.87%` | `53.13%` | `0.88` | 905,470.00 USD |
| `4H` | `Bitunix` | `50.27%` | `49.73%` | `1.01` | 306,480.00 USD |
| `4H` | `Hyperliquid` | `56.55%` | `43.45%` | `1.30` | 155,570.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.8%` | `51.2%` | `0.95` | 4,340,000.00 USD |
| `4H` | `Crypto.com` | `26.54%` | `73.46%` | `0.36` | 968.24 USD |
| `4H` | `WhiteBIT` | `71.94%` | `28.06%` | `2.56` | 159,150.00 USD |
| `4H` | `HTX` | `53.93%` | `46.07%` | `1.17` | 9,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `14.64%` | `85.36%` | `0.17` | 33,430.00 USD |
| `4H` | `Aster` | `64.28%` | `35.72%` | `1.80` | 495.35 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `68.79%` | `31.21%` | `2.20` | 55,020.00 USD |
| `4H` | `Whale Positions` | `51.06%` | `48.94%` | `1.04` | 8,450,000.00 USD |
| `4H` | `Global Accounts` | `43.56%` | `56.44%` | `0.77` | 25,910,000.00 USD |


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
| `5m` | 739,010.00 USD | 313,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,090,000.00 USD | 984,770.00 USD | **`ACCUMULATION`** |
| `30m` | 1,770,000.00 USD | 852,620.00 USD | **`ACCUMULATION`** |
| `1h` | 1,820,000.00 USD | 1,320,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,850,000.00 USD | 1,220,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,780,000.00 USD | 947,300.00 USD | **`ACCUMULATION`** |
| `6h` | 1,820,000.00 USD | -14,240.00 USD | **`ACCUMULATION`** |
| `8h` | 834,900.00 USD | -10,510.00 USD | **`ACCUMULATION`** |
| `12h` | 150,700.00 USD | 69,200.00 USD | **`ACCUMULATION`** |
| `24h` | 545,620.00 USD | 217,840.00 USD | **`ACCUMULATION`** |
| `1w` | -7,640,000.00 USD | -8,690,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -17,930,000.00 USD | -69,350,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+739.01K` | 15m=`+1.09M` | 1h=`+1.82M` | 24h=`+545.62K`
* Futures Capital Netflows: 5m=`+313.00K` | 15m=`+984.77K` | 1h=`+1.32M` | 24h=`+217.84K`
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
  * `2026-10-30 09:51:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:39:14 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:40:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.44` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3987.26` (Risk Distance: `9.18` pts)
  * +2.5R Take Profit: `4019.40`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.22` (Risk Distance: `9.18` pts)
  * +2.5R Take Profit: `3990.08`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4033.10`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
