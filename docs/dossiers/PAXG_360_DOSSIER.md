# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 02:18:33 IST` (`2026-10-29 20:48:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4023.65` | **Live Ask Quote**: `4023.73` | **Mid Price**: `4023.69`
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
  * Session VWAP: `4029.62` | VWAP Z-Score: `-0.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.91` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `56.34` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.82` | Lower -3.00σ Band: `3994.42`
  * Upper +2.51σ Band: `4059.07` | Lower -2.51σ Band: `4000.17`
  * Upper +2.01σ Band: `4053.20` | Lower -2.01σ Band: `4006.04`
  * Upper +2.00σ Band: `4053.09` | Lower -2.00σ Band: `4006.15`
  * Upper +1.28σ Band: `4044.64` | Lower -1.28σ Band: `4014.60`
  * Upper +1.00σ Band: `4041.35` | Lower -1.00σ Band: `4017.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4019.54` | EMA-20=`4018.66` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4023.20` (Slope: `+0.0000`) | EMA-100=`4029.48`
  * Institutional Anchors: EMA-144=`4031.30` | EMA-200=`4031.59` (Slope: `-0.0517`) | EMA-233=`4030.88`
- **Range Boundaries**: 24H High=`4082.75` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4039.67` (Distance: `-0.39%`)
  * Point of Control (POC) = `4027.32` (Distance: `-0.09%`)
  * Value Area Low (VAL) = `4016.67` (Distance: `+0.18%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `4007.60` - `4039.78`
  * Optimal Trade Entry (OTE 0.705): `4031.74`
  * Structural Invalidation Anchor (0.786): `4055.88`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4027.95` | `4029.95` | `4027.30` | `4029.01` | `79` | 316,817.22 USD | -171,335.72 USD | `-54.08%` | 1,520,957.02 USD | `-0.95` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4029.01` | `4030.42` | `4028.37` | `4028.37` | `81` | 326,054.83 USD | -74,716.39 USD | `-22.92%` | 1,446,240.62 USD | `-0.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4028.38` | `4028.38` | `4023.58` | `4024.57` | `130` | 524,186.95 USD | -98,324.06 USD | `-18.76%` | 1,347,916.57 USD | `-0.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4025.61` | `4033.50` | `4024.22` | `4029.20` | `369` | 1,485,272.51 USD | 203,652.15 USD | `+13.71%` | 1,670,998.43 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4029.20` | `4029.60` | `4026.43` | `4027.95` | `56` | 224,641.89 USD | 21,294.31 USD | `+9.48%` | 1,692,292.74 USD | `-0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4027.95` | `4030.42` | `4023.58` | `4024.57` | `290` | 1,167,344.74 USD | -344,661.91 USD | `-29.53%` | 1,347,630.82 USD | `-1.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4011.95` | `4017.97` | `4011.01` | `4017.56` | `511` | 2,050,996.96 USD | 1,105,382.66 USD | `+53.89%` | 2,342,518.27 USD | `+1.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4017.56` | `4025.99` | `4014.71` | `4025.60` | `520` | 2,091,733.78 USD | -652,688.52 USD | `-31.20%` | 1,689,829.74 USD | `-1.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4023.58` | `4024.57` | `714` | 2,876,973.40 USD | -119,429.71 USD | `-4.15%` | 1,570,400.03 USD | `-0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4023.58` | `4024.57` | `714` | 2,877,259.14 USD | -119,715.46 USD | `-4.16%` | 1,127,431.87 USD | `-0.52` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4023.58` | `4024.57` | `714` | 2,877,259.14 USD | -119,715.46 USD | `-4.16%` | 1,127,431.87 USD | `-0.52` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `BID` | `4025.30` | `0.5244` | 2,110.87 USD | 893,249.95 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `4025.40` | `4.6579` | 18,749.91 USD | 891,139.08 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4025.50` | `1.1349` | 4,568.54 USD | 872,389.17 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4025.60` | `2.9067` | 11,701.21 USD | 867,820.63 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4025.70` | `0.7386` | 2,973.38 USD | 856,119.42 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4025.90` | `21.3939` | 86,129.70 USD | 853,146.04 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `4026.00` | `13.0680` | 52,611.77 USD | 767,016.34 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4026.20` | `0.9859` | 3,969.43 USD | 714,404.57 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4026.40` | `12.1546` | 48,939.28 USD | 710,435.14 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4026.50` | `0.0720` | 289.91 USD | 661,495.86 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `4026.60` | `22.6979` | 91,395.36 USD | 661,205.95 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `4026.70` | `1.0725` | 4,318.64 USD | 569,810.59 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4026.80` | `71.0271` | 286,011.93 USD | 565,491.95 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `4026.90` | `17.3443` | 69,843.76 USD | 279,480.02 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4027.00` | `3.7968` | 15,289.71 USD | 209,636.26 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4027.20` | `18.5555` | 74,726.71 USD | 194,346.55 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `4027.30` | `4.9766` | 20,042.26 USD | 119,619.84 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `4027.40` | `14.3035` | 57,605.92 USD | 99,577.58 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4027.50` | `7.6325` | 30,739.89 USD | 41,971.66 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `4027.60` | `2.7887` | 11,231.77 USD | 11,231.77 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4027.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,027.65` | `0.00%` | `-` |
| `ASK` | `4027.70` | `2.6519` | 10,681.06 USD | 10,681.06 USD | `4 orders` | `+0.00%` | `-` |
| `ASK` | `4027.80` | `0.3734` | 1,503.98 USD | 12,185.04 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `4027.90` | `3.7240` | 14,999.90 USD | 27,184.94 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4028.00` | `4.6968` | 18,918.71 USD | 46,103.65 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4028.10` | `8.8881` | 35,802.16 USD | 81,905.80 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4028.30` | `4.9032` | 19,751.56 USD | 101,657.36 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4028.40` | `3.7235` | 14,999.75 USD | 116,657.11 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4028.50` | `2.3705` | 9,549.56 USD | 126,206.67 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4028.60` | `5.7618` | 23,211.99 USD | 149,418.66 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4028.70` | `2.4287` | 9,784.50 USD | 159,203.16 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4028.80` | `4.0516` | 16,323.09 USD | 175,526.25 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4028.90` | `1.5051` | 6,063.90 USD | 181,590.15 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4029.00` | `4.5888` | 18,488.28 USD | 200,078.42 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4029.10` | `16.3640` | 65,932.19 USD | 266,010.61 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4029.20` | `54.9520` | 221,412.60 USD | 487,423.21 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4029.30` | `17.2891` | 69,662.97 USD | 557,086.18 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `4029.40` | `14.8417` | 59,803.15 USD | 616,889.33 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4029.50` | `1.1926` | 4,805.58 USD | 621,694.91 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4029.60` | `0.7612` | 3,067.33 USD | 624,762.24 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4029.70` | `6.6770` | 26,906.31 USD | 651,668.55 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x5b5d...c060` | `SHORT` | 25,503,135.31 USD | `6,334.29` | `4191.43` | `4023.10` | `31463.80` | 1,046,671.13 USD | `+4.10%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,396,629.75 USD | `6,311.29` | `4133.61` | `4023.10` | `13622.06` | 691,789.38 USD | `+2.72%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,034,032.32 USD | `5,717.06` | `4234.49` | `4023.10` | `29670.02` | 1,174,842.91 USD | `+5.10%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,441,662.07 USD | `4,828.91` | `4157.43` | `4023.10` | `2174.12` | -634,220.25 USD | `-3.26%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,164,961.89 USD | `3,520.56` | `4129.51` | `4023.10` | `355.95` | -373,227.47 USD | `-2.63%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,151,616.74 USD | `3,268.21` | `4228.94` | `4023.10` | `4392.92` | 669,462.39 USD | `+5.09%` | `25X Cross` |
| `177` | `0xa742...e390` | `SHORT` | 11,675,980.40 USD | `2,900.00` | `4364.92` | `4023.10` | `4235.64` | 982,295.93 USD | `+8.41%` | `20X Cross` |
| `270` | `0x41e5...0825` | `SHORT` | 8,863,580.00 USD | `2,200.00` | `4112.20` | `4023.10` | `4331.13` | 183,274.59 USD | `+2.07%` | `20X Cross` |
| `273` | `0x3678...b209` | `LONG` | 8,851,040.00 USD | `2,200.00` | `4176.09` | `4023.10` | `2712.70` | -336,379.30 USD | `-3.80%` | `25X Cross` |
| `306` | `0xfc66...ca06` | `SHORT` | 7,970,847.70 USD | `1,981.17` | `4032.86` | `4023.10` | `24530.00` | 18,958.52 USD | `+0.24%` | `3X Cross` |
| `308` | `0xacb6...efbd` | `SHORT` | 7,953,231.07 USD | `1,975.37` | `4048.55` | `4023.10` | `6484.06` | 44,160.64 USD | `+0.56%` | `6X Cross` |
| `379` | `0xc26c...b8f4` | `LONG` | 6,357,884.04 USD | `1,579.95` | `4075.62` | `4023.10` | `0.000000` | -81,412.93 USD | `-1.28%` | `1X Cross` |
| `412` | `0x12d2...f97f` | `LONG` | 5,644,502.10 USD | `1,401.94` | `4278.91` | `4023.10` | `2842.10` | -354,288.48 USD | `-6.28%` | `20X Cross` |
| `562` | `0x63da...8add` | `LONG` | 4,024,100.00 USD | `1,000.00` | `4021.46` | `4023.10` | `3564.08` | 2,639.04 USD | `+0.07%` | `25X Cross` |
| `586` | `0x354b...6425` | `LONG` | 3,935,944.50 USD | `978.29` | `4031.93` | `4023.10` | `0.000000` | -8,444.62 USD | `-0.21%` | `10X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,911,927.86 USD | `971.64` | `4279.98` | `4023.10` | `0.000000` | -246,681.23 USD | `-6.31%` | `20X Cross` |
| `617` | `0xf3dc...1672` | `LONG` | 3,745,312.65 USD | `930.74` | `4024.62` | `4023.10` | `3337.56` | -579.91 USD | `-0.02%` | `20X Cross` |
| `681` | `0x4a20...3c26` | `LONG` | 3,369,110.21 USD | `837.40` | `4599.73` | `4023.10` | `0.000000` | -482,710.17 USD | `-14.33%` | `20X Cross` |
| `839` | `0x0fac...7a0a` | `LONG` | 2,761,729.15 USD | `686.49` | `4290.34` | `4023.10` | `1592.26` | -183,529.55 USD | `-6.65%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,584,258.00 USD | `642.35` | `4175.35` | `4023.10` | `32697.38` | 97,803.18 USD | `+3.78%` | `4X Cross` |
| `909` | `0x625e...a354` | `SHORT` | 2,496,368.00 USD | `620.00` | `4122.81` | `4023.10` | `4342.23` | 59,779.03 USD | `+2.39%` | `20X Cross` |
| `933` | `0xeae3...e8ad` | `SHORT` | 2,413,920.00 USD | `600.00` | `4104.77` | `4023.10` | `4325.25` | 48,945.11 USD | `+2.03%` | `20X Cross` |
| `940` | `0xf285...fa82` | `LONG` | 2,408,093.97 USD | `598.11` | `4146.45` | `4023.10` | `3891.22` | -71,925.58 USD | `-2.99%` | `25X Cross` |
| `957` | `0x12f7...8750` | `LONG` | 2,356,556.02 USD | `585.61` | `4082.77` | `4023.10` | `2534.97` | -34,360.96 USD | `-1.46%` | `10X Cross` |
| `1114` | `0x413c...886c` | `LONG` | 2,011,500.00 USD | `500.00` | `4010.43` | `4023.10` | `0.000000` | 6,283.77 USD | `+0.31%` | `2X Cross` |
| `1124` | `0x61ce...a62b` | `SHORT` | 2,001,556.08 USD | `497.50` | `4071.66` | `4023.10` | `4716.94` | 24,112.71 USD | `+1.20%` | `20X Cross` |
| `1132` | `0x0593...40f9` | `LONG` | 1,996,169.69 USD | `496.18` | `4024.57` | `4023.10` | `3701.71` | -734.14 USD | `-0.04%` | `10X Isolated` |
| `1201` | `0x2edd...8179` | `LONG` | 1,884,017.76 USD | `468.17` | `4165.52` | `4025.00` | `0.000000` | -66,163.18 USD | `-3.51%` | `10X Cross` |
| `1249` | `0xead5...69f2` | `LONG` | 1,828,159.20 USD | `453.78` | `4220.88` | `4023.10` | `3538.92` | -87,208.86 USD | `-4.77%` | `5X Isolated` |
| `1309` | `0x7a6d...f79c` | `SHORT` | 1,723,754.26 USD | `428.38` | `4136.09` | `4025.00` | `5771.45` | 48,060.75 USD | `+2.79%` | `10X Cross` |
| `1364` | `0x46fc...1195` | `LONG` | 1,647,454.13 USD | `409.49` | `4055.28` | `4023.10` | `2053.63` | -13,136.75 USD | `-0.80%` | `20X Cross` |
| `1393` | `0x6d15...d374` | `LONG` | 1,611,600.00 USD | `400.00` | `4068.25` | `4023.10` | `3841.79` | -15,700.00 USD | `-0.97%` | `25X Cross` |
| `1396` | `0xee02...309d` | `SHORT` | 1,610,480.00 USD | `400.00` | `4438.84` | `4023.10` | `4226.86` | 165,058.60 USD | `+10.25%` | `25X Isolated` |
| `1437` | `0x02a7...fe9f` | `SHORT` | 1,569,399.00 USD | `390.00` | `4055.02` | `4023.10` | `4306.68` | 12,060.25 USD | `+0.77%` | `25X Cross` |
| `1476` | `0x51f6...2b39` | `LONG` | 1,531,151.76 USD | `380.49` | `4234.66` | `4025.00` | `0.000000` | -80,076.30 USD | `-5.23%` | `10X Cross` |
| `1479` | `0x7e77...b8d2` | `SHORT` | 1,528,778.00 USD | `380.00` | `4131.92` | `4023.10` | `4293.49` | 41,351.64 USD | `+2.70%` | `20X Cross` |
| `1501` | `0x72c2...9b37` | `LONG` | 1,501,107.22 USD | `373.13` | `4000.98` | `4023.10` | `3778.02` | 8,213.70 USD | `+0.55%` | `13X Isolated` |
| `1537` | `0xaa44...b844` | `LONG` | 1,448,640.00 USD | `360.00` | `4043.10` | `4023.10` | `2803.24` | -6,877.63 USD | `-0.47%` | `4X Cross` |
| `1539` | `0x781e...96b7` | `SHORT` | 1,446,823.81 USD | `359.55` | `4365.03` | `4025.00` | `13868.86` | 122,623.67 USD | `+8.48%` | `10X Cross` |
| `1646` | `0xa41f...d50a` | `LONG` | 1,324,434.31 USD | `328.96` | `4468.89` | `4023.10` | `3833.16` | -145,663.54 USD | `-11.00%` | `15X Cross` |
| `1665` | `0x49e9...e1d0` | `SHORT` | 1,302,230.22 USD | `323.48` | `4025.23` | `4023.10` | `31676.92` | -151.89 USD | `-0.01%` | `4X Cross` |
| `1688` | `0xada6...6f88` | `LONG` | 1,284,445.74 USD | `319.28` | `4166.46` | `4023.10` | `1935.33` | -45,804.77 USD | `-3.57%` | `5X Cross` |
| `1694` | `0xbf5a...88ba` | `SHORT` | 1,278,942.16 USD | `317.65` | `4091.80` | `4023.10` | `10297.64` | 20,840.87 USD | `+1.63%` | `20X Cross` |
| `1728` | `0xff31...ff6c` | `SHORT` | 1,247,192.00 USD | `310.00` | `4372.43` | `4023.10` | `4789.15` | 108,263.38 USD | `+8.68%` | `10X Isolated` |
| `1898` | `0x50e2...d770` | `LONG` | 1,087,769.16 USD | `270.37` | `4243.58` | `4023.10` | `2562.07` | -59,557.30 USD | `-5.48%` | `20X Cross` |
| `1918` | `0x4c92...4f17` | `SHORT` | 1,073,309.96 USD | `266.72` | `4260.98` | `4023.10` | `6503.96` | 63,182.27 USD | `+5.89%` | `20X Cross` |
| `1974` | `0xd346...c4f3` | `LONG` | 1,027,380.75 USD | `255.17` | `4188.66` | `4023.10` | `3310.40` | -41,455.75 USD | `-4.04%` | `5X Isolated` |
| `2008` | `0x1581...463b` | `LONG` | 1,007,275.00 USD | `250.00` | `4003.77` | `4023.10` | `3504.62` | 6,331.41 USD | `+0.63%` | `15X Cross` |
| `2014` | `0xe47f...758c` | `LONG` | 1,006,050.00 USD | `250.00` | `4020.00` | `4023.10` | `3774.32` | 1,050.00 USD | `+0.10%` | `20X Cross` |

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
| `7D` | `Long Liquidation` | `3611.20` | 16,420,000.00 USD | 16,420,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3613.90` | 3,630,000.00 USD | 3,630,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,340,000.00 USD | 16,340,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.10` | 3,610,000.00 USD | 3,610,000.00 USD | 23,970.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.80` | 16,190,000.00 USD | 16,190,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.30` | 3,590,000.00 USD | 3,590,000.00 USD | 48,120.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3624.10` | 16,140,000.00 USD | 16,140,000.00 USD | 88,630.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.50` | 3,530,000.00 USD | 3,530,000.00 USD | 43,650.00 USD | 0.00 USD | 8,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.40` | 16,030,000.00 USD | 16,030,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,480,000.00 USD | 3,480,000.00 USD | 36,780.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.70` | 15,830,000.00 USD | 15,830,000.00 USD | 103,510.00 USD | 0.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.90` | 3,440,000.00 USD | 3,440,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3637.00` | 15,720,000.00 USD | 15,720,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.10` | 3,410,000.00 USD | 3,410,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3641.30` | 15,580,000.00 USD | 15,580,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.30` | 3,370,000.00 USD | 3,370,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.60` | 15,520,000.00 USD | 15,520,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.50` | 3,360,000.00 USD | 3,360,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.90` | 15,490,000.00 USD | 15,490,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.70` | 3,340,000.00 USD | 3,340,000.00 USD | 20,320.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3654.20` | 15,470,000.00 USD | 15,470,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.90` | 3,320,000.00 USD | 3,320,000.00 USD | 9,600.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3658.50` | 15,410,000.00 USD | 15,410,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3660.10` | 3,310,000.00 USD | 3,310,000.00 USD | 4,760.00 USD | 0.00 USD | 241.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.80` | 15,400,000.00 USD | 15,400,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3664.30` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3667.10` | 15,380,000.00 USD | 15,380,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3830.50` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3839.10` | 15,370,000.00 USD | 15,370,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3843.40` | 14,950,000.00 USD | 14,950,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.70` | 14,430,000.00 USD | 14,430,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3852.00` | 13,900,000.00 USD | 13,900,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.30` | 3,300,000.00 USD | 3,300,000.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3856.30` | 13,610,000.00 USD | 13,610,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3857.50` | 3,280,000.00 USD | 3,280,000.00 USD | 84,040.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.60` | 13,190,000.00 USD | 13,190,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.70` | 3,190,000.00 USD | 3,190,000.00 USD | 81,330.00 USD | 0.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.90` | 13,010,000.00 USD | 13,010,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.90` | 3,110,000.00 USD | 3,110,000.00 USD | 154,610.00 USD | 0.00 USD | 18,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3869.20` | 12,670,000.00 USD | 12,670,000.00 USD | 631,520.00 USD | 0.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.10` | 2,930,000.00 USD | 2,930,000.00 USD | 170,010.00 USD | 0.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3873.50` | 11,990,000.00 USD | 11,990,000.00 USD | 309,370.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.30` | 2,740,000.00 USD | 2,740,000.00 USD | 90,920.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.80` | 11,630,000.00 USD | 11,630,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3878.50` | 2,640,000.00 USD | 2,640,000.00 USD | 137,570.00 USD | 0.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3882.10` | 11,050,000.00 USD | 11,050,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3882.70` | 2,490,000.00 USD | 2,490,000.00 USD | 54,290.00 USD | 0.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3886.40` | 10,840,000.00 USD | 10,840,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3886.90` | 2,410,000.00 USD | 2,410,000.00 USD | 18,450.00 USD | 0.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.70` | 10,750,000.00 USD | 10,750,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3891.10` | 2,390,000.00 USD | 2,390,000.00 USD | 57,500.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3895.00` | 10,610,000.00 USD | 10,610,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3895.30` | 2,320,000.00 USD | 2,320,000.00 USD | 48,610.00 USD | 0.00 USD | 4,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3899.30` | 10,490,000.00 USD | 10,490,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3899.50` | 2,270,000.00 USD | 2,270,000.00 USD | 22,520.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.60` | 10,360,000.00 USD | 10,360,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3903.70` | 2,240,000.00 USD | 2,240,000.00 USD | 30,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3907.90` | 2,210,000.00 USD | 2,210,000.00 USD | 4,950.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.90` | 10,320,000.00 USD | 10,320,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3912.20` | 10,270,000.00 USD | 10,270,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3916.50` | 10,240,000.00 USD | 10,240,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.80` | 9,880,000.00 USD | 9,880,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3925.10` | 9,090,000.00 USD | 9,090,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3929.40` | 8,110,000.00 USD | 8,110,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.10` | 2,200,000.00 USD | 2,200,000.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.70` | 7,000,000.00 USD | 7,000,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3937.30` | 2,190,000.00 USD | 2,190,000.00 USD | 163,880.00 USD | 0.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.00` | 6,500,000.00 USD | 6,500,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3941.50` | 2,020,000.00 USD | 2,020,000.00 USD | 139,180.00 USD | 0.00 USD | 16,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3942.30` | 5,780,000.00 USD | 5,780,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3945.70` | 1,860,000.00 USD | 1,860,000.00 USD | 351,370.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.60` | 5,350,000.00 USD | 5,350,000.00 USD | 617,970.00 USD | 0.00 USD | 123,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3949.90` | 1,470,000.00 USD | 1,470,000.00 USD | 268,960.00 USD | 0.00 USD | 38,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.90` | 4,600,000.00 USD | 4,600,000.00 USD | 1,110,000.00 USD | 0.00 USD | 80,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.10` | 1,170,000.00 USD | 1,170,000.00 USD | 232,080.00 USD | 0.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.20` | 3,410,000.00 USD | 3,410,000.00 USD | 734,780.00 USD | 0.00 USD | 66,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.30` | 901,280.00 USD | 901,280.00 USD | 223,050.00 USD | 0.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.50` | 2,610,000.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.50` | 668,340.00 USD | 668,340.00 USD | 173,130.00 USD | 0.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.80` | 1,600,000.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.70` | 450,320.00 USD | 450,320.00 USD | 45,250.00 USD | 0.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.10` | 1,120,000.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3970.90` | 379,050.00 USD | 379,050.00 USD | 52,390.00 USD | 0.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.40` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 310,110.00 USD | 310,110.00 USD | 147,720.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.30` | 151,490.00 USD | 151,490.00 USD | 46,450.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3981.00` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.50` | 90,820.00 USD | 90,820.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.30` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3987.70` | 30,630.00 USD | 30,630.00 USD | 20,760.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.60` | 134,160.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.90` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4092.70` | 5,620.00 USD | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4096.90` | 173,410.00 USD | 173,410.00 USD | 153,970.00 USD | 0.00 USD | 13,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.10` | 252,320.00 USD | 252,320.00 USD | 65,200.00 USD | 0.00 USD | 13,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.30` | 537,220.00 USD | 537,220.00 USD | 272,350.00 USD | 0.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4109.50` | 888,500.00 USD | 888,500.00 USD | 301,860.00 USD | 0.00 USD | 49,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4110.00` | 6,470,000.00 USD | 6,470,000.00 USD | 1,060,000.00 USD | 0.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4113.70` | 1,220,000.00 USD | 1,220,000.00 USD | 299,000.00 USD | 0.00 USD | 34,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4114.30` | 7,320,000.00 USD | 7,320,000.00 USD | 751,280.00 USD | 0.00 USD | 103,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4117.90` | 1,340,000.00 USD | 1,340,000.00 USD | 101,440.00 USD | 0.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.60` | 8,210,000.00 USD | 8,210,000.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.10` | 1,680,000.00 USD | 1,680,000.00 USD | 295,610.00 USD | 0.00 USD | 37,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.90` | 8,930,000.00 USD | 8,930,000.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.30` | 1,790,000.00 USD | 1,790,000.00 USD | 85,580.00 USD | 0.00 USD | 28,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.20` | 9,180,000.00 USD | 9,180,000.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.50` | 1,830,000.00 USD | 1,830,000.00 USD | 21,900.00 USD | 0.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4131.50` | 9,380,000.00 USD | 9,380,000.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4134.70` | 1,960,000.00 USD | 1,960,000.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.80` | 9,610,000.00 USD | 9,610,000.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4138.90` | 2,060,000.00 USD | 2,060,000.00 USD | 89,640.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.10` | 9,860,000.00 USD | 9,860,000.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.10` | 2,120,000.00 USD | 2,120,000.00 USD | 45,040.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.40` | 10,030,000.00 USD | 10,030,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,170,000.00 USD | 2,170,000.00 USD | 54,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.70` | 10,130,000.00 USD | 10,130,000.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4151.50` | 2,200,000.00 USD | 2,200,000.00 USD | 15,790.00 USD | 0.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.00` | 10,220,000.00 USD | 10,220,000.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,600,000.00 USD | 10,600,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.60` | 11,030,000.00 USD | 11,030,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.90` | 11,440,000.00 USD | 11,440,000.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4170.20` | 11,890,000.00 USD | 11,890,000.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.50` | 12,120,000.00 USD | 12,120,000.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.70` | 2,270,000.00 USD | 2,270,000.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.90` | 2,320,000.00 USD | 2,320,000.00 USD | 42,890.00 USD | 0.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4183.10` | 12,640,000.00 USD | 12,640,000.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.10` | 2,420,000.00 USD | 2,420,000.00 USD | 96,770.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4187.40` | 12,980,000.00 USD | 12,980,000.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.30` | 2,620,000.00 USD | 2,620,000.00 USD | 179,080.00 USD | 0.00 USD | 23,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.70` | 13,640,000.00 USD | 13,640,000.00 USD | 616,550.00 USD | 0.00 USD | 45,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.50` | 2,770,000.00 USD | 2,770,000.00 USD | 123,550.00 USD | 0.00 USD | 20,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4196.00` | 13,960,000.00 USD | 13,960,000.00 USD | 286,520.00 USD | 0.00 USD | 35,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.70` | 2,860,000.00 USD | 2,860,000.00 USD | 83,320.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4200.30` | 14,470,000.00 USD | 14,470,000.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.90` | 3,010,000.00 USD | 3,010,000.00 USD | 138,770.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.60` | 14,720,000.00 USD | 14,720,000.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.10` | 3,080,000.00 USD | 3,080,000.00 USD | 53,090.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.90` | 14,850,000.00 USD | 14,850,000.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4210.30` | 3,110,000.00 USD | 3,110,000.00 USD | 18,450.00 USD | 0.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4213.20` | 14,960,000.00 USD | 14,960,000.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4214.50` | 3,160,000.00 USD | 3,160,000.00 USD | 38,650.00 USD | 0.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4217.50` | 15,070,000.00 USD | 15,070,000.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4218.70` | 3,220,000.00 USD | 3,220,000.00 USD | 61,400.00 USD | 0.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.80` | 15,180,000.00 USD | 15,180,000.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4222.90` | 3,250,000.00 USD | 3,250,000.00 USD | 23,220.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4226.10` | 15,270,000.00 USD | 15,270,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4227.10` | 3,280,000.00 USD | 3,280,000.00 USD | 27,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4230.40` | 15,310,000.00 USD | 15,310,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4231.30` | 3,300,000.00 USD | 3,300,000.00 USD | 13,060.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.70` | 15,360,000.00 USD | 15,360,000.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4239.00` | 15,370,000.00 USD | 15,370,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4389.50` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4398.10` | 15,520,000.00 USD | 15,520,000.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4402.40` | 15,650,000.00 USD | 15,650,000.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.70` | 15,780,000.00 USD | 15,780,000.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4411.00` | 15,900,000.00 USD | 15,900,000.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4415.30` | 15,960,000.00 USD | 15,960,000.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.10` | 3,310,000.00 USD | 3,310,000.00 USD | 8,150.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.60` | 16,070,000.00 USD | 16,070,000.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.30` | 3,340,000.00 USD | 3,340,000.00 USD | 24,480.00 USD | 0.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.90` | 16,120,000.00 USD | 16,120,000.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4424.50` | 3,360,000.00 USD | 3,360,000.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4428.20` | 16,200,000.00 USD | 16,200,000.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4428.70` | 3,420,000.00 USD | 3,420,000.00 USD | 51,530.00 USD | 0.00 USD | 5,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4432.50` | 16,360,000.00 USD | 16,360,000.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4432.90` | 3,450,000.00 USD | 3,450,000.00 USD | 25,170.00 USD | 0.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4436.80` | 16,470,000.00 USD | 16,470,000.00 USD | 95,850.00 USD | 0.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4437.10` | 3,480,000.00 USD | 3,480,000.00 USD | 30,580.00 USD | 0.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4438.90` | 3,490,000.00 USD | 3,490,000.00 USD | 6,660.00 USD | 0.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4441.10` | 16,590,000.00 USD | 16,590,000.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4445.40` | 16,670,000.00 USD | 16,670,000.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4448.40` | 16,720,000.00 USD | 16,720,000.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.20` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 62,260.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `3613.90` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 12,730.00 USD | 0.00 USD | 2,280.00 USD |
| `7D` | `3615.50` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 23,970.00 USD | 0.00 USD | 1,350.00 USD |
| `7D` | `3619.80` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 45,440.00 USD | 0.00 USD | 10,180.00 USD |
| `1D` | `3622.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 48,120.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `3624.10` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 88,630.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `3626.50` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 43,650.00 USD | 0.00 USD | 8,500.00 USD |
| `7D` | `3628.40` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 180,830.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3630.70` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 36,780.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `3632.70` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 103,510.00 USD | 0.00 USD | 13,730.00 USD |
| `1D` | `3634.90` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD |
| `7D` | `3637.00` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 115,810.00 USD | 0.00 USD | 18,230.00 USD |
| `1D` | `3639.10` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3641.30` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 45,790.00 USD | 0.00 USD | 15,750.00 USD |
| `1D` | `3643.30` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3645.60` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 23,870.00 USD | 0.00 USD | 8,820.00 USD |
| `1D` | `3647.50` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.90` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 18,710.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `3651.70` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 20,320.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `3654.20` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 58,600.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `3655.90` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 9,600.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3658.50` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 6,820.00 USD | 0.00 USD | 3,890.00 USD |
| `1D` | `3660.10` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 4,760.00 USD | 0.00 USD | 241.68 USD |
| `7D` | `3662.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 12,530.00 USD | 0.00 USD | 5,170.00 USD |
| `1D` | `3664.30` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 1,580.00 USD |
| `7D` | `3667.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.50` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3839.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 403,730.00 USD | 0.00 USD | 17,920.00 USD |
| `7D` | `3843.40` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 443,720.00 USD | 0.00 USD | 76,510.00 USD |
| `7D` | `3847.70` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 469,440.00 USD | 0.00 USD | 59,220.00 USD |
| `7D` | `3852.00` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 229,390.00 USD | 0.00 USD | 56,860.00 USD |
| `1D` | `3853.30` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 10,060.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `3856.30` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 402,740.00 USD | 0.00 USD | 23,990.00 USD |
| `1D` | `3857.50` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 84,040.00 USD | 0.00 USD | 5,560.00 USD |
| `7D` | `3860.60` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 157,840.00 USD | 0.00 USD | 20,440.00 USD |
| `1D` | `3861.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 81,330.00 USD | 0.00 USD | 5,850.00 USD |
| `7D` | `3864.90` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 289,880.00 USD | 0.00 USD | 52,180.00 USD |
| `1D` | `3865.90` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 154,610.00 USD | 0.00 USD | 18,860.00 USD |
| `7D` | `3869.20` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 631,520.00 USD | 0.00 USD | 39,700.00 USD |
| `1D` | `3870.10` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 170,010.00 USD | 0.00 USD | 21,090.00 USD |
| `7D` | `3873.50` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 309,370.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3874.30` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 90,920.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `3877.80` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 517,800.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `3878.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 137,570.00 USD | 0.00 USD | 8,220.00 USD |
| `7D` | `3882.10` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 178,640.00 USD | 0.00 USD | 35,070.00 USD |
| `1D` | `3882.70` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 54,290.00 USD | 0.00 USD | 25,360.00 USD |
| `7D` | `3886.40` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 61,570.00 USD | 0.00 USD | 28,940.00 USD |
| `1D` | `3886.90` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 18,450.00 USD | 0.00 USD | 6,220.00 USD |
| `7D` | `3890.70` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 109,450.00 USD | 0.00 USD | 23,010.00 USD |
| `1D` | `3891.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 57,500.00 USD | 0.00 USD | 7,420.00 USD |
| `7D` | `3895.00` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 118,940.00 USD | 0.00 USD | 6,690.00 USD |
| `1D` | `3895.30` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 48,610.00 USD | 0.00 USD | 4,850.00 USD |
| `7D` | `3899.30` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3899.50` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 22,520.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3903.60` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `3903.70` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 30,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3907.90` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 4,950.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `3907.90` | 10,320,000.00 USD | 0.00 USD | 10,320,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3912.20` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 16,550.00 USD | 0.00 USD | 9,190.00 USD |
| `7D` | `3916.50` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 340,490.00 USD | 0.00 USD | 24,470.00 USD |
| `7D` | `3920.80` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 718,240.00 USD | 0.00 USD | 65,540.00 USD |
| `7D` | `3925.10` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 857,670.00 USD | 0.00 USD | 125,580.00 USD |
| `7D` | `3929.40` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 936,410.00 USD | 0.00 USD | 173,140.00 USD |
| `1D` | `3933.10` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 5,620.00 USD | 0.00 USD | 6,500.00 USD |
| `7D` | `3933.70` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 442,120.00 USD | 0.00 USD | 58,180.00 USD |
| `1D` | `3937.30` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 163,880.00 USD | 0.00 USD | 7,950.00 USD |
| `7D` | `3938.00` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 693,070.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `3941.50` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 139,180.00 USD | 0.00 USD | 16,100.00 USD |
| `7D` | `3942.30` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 375,470.00 USD | 0.00 USD | 56,660.00 USD |
| `1D` | `3945.70` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 351,370.00 USD | 0.00 USD | 35,820.00 USD |
| `7D` | `3946.60` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 617,970.00 USD | 0.00 USD | 123,630.00 USD |
| `1D` | `3949.90` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 268,960.00 USD | 0.00 USD | 38,310.00 USD |
| `7D` | `3950.90` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 1,110,000.00 USD | 0.00 USD | 80,030.00 USD |
| `1D` | `3954.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 232,080.00 USD | 0.00 USD | 32,410.00 USD |
| `7D` | `3955.20` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 734,780.00 USD | 0.00 USD | 66,110.00 USD |
| `1D` | `3958.30` | 901,280.00 USD | 0.00 USD | 901,280.00 USD | 223,050.00 USD | 0.00 USD | 9,880.00 USD |
| `7D` | `3959.50` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 879,760.00 USD | 0.00 USD | 130,350.00 USD |
| `1D` | `3962.50` | 668,340.00 USD | 0.00 USD | 668,340.00 USD | 173,130.00 USD | 0.00 USD | 44,890.00 USD |
| `7D` | `3963.80` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 396,840.00 USD | 0.00 USD | 79,970.00 USD |
| `1D` | `3966.70` | 450,320.00 USD | 0.00 USD | 450,320.00 USD | 45,250.00 USD | 0.00 USD | 26,010.00 USD |
| `7D` | `3968.10` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 125,300.00 USD | 0.00 USD | 51,020.00 USD |
| `1D` | `3970.90` | 379,050.00 USD | 0.00 USD | 379,050.00 USD | 52,390.00 USD | 0.00 USD | 16,550.00 USD |
| `7D` | `3972.40` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.10` | 310,110.00 USD | 0.00 USD | 310,110.00 USD | 147,720.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.30` | 151,490.00 USD | 0.00 USD | 151,490.00 USD | 46,450.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3981.00` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.50` | 90,820.00 USD | 0.00 USD | 90,820.00 USD | 60,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.30` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 33,890.00 USD |
| `1D` | `3987.70` | 30,630.00 USD | 0.00 USD | 30,630.00 USD | 20,760.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `3989.60` | 134,160.00 USD | 0.00 USD | 134,160.00 USD | 87,550.00 USD | 0.00 USD | 13,510.00 USD |
| `7D` | `3993.90` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4029.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4030.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4071.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4075.60` | 156,550.00 USD | 156,550.00 USD | 0.00 USD | 149,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4079.90` | 913,460.00 USD | 913,460.00 USD | 0.00 USD | 689,060.00 USD | 0.00 USD | 67,860.00 USD |
| `7D` | `4084.20` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 865,000.00 USD | 0.00 USD | 124,950.00 USD |
| `7D` | `4088.50` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 930,460.00 USD | 0.00 USD | 122,030.00 USD |
| `1D` | `4092.70` | 5,620.00 USD | 5,620.00 USD | 0.00 USD | 5,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4092.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 458,780.00 USD | 0.00 USD | 106,220.00 USD |
| `1D` | `4096.90` | 173,410.00 USD | 173,410.00 USD | 0.00 USD | 153,970.00 USD | 0.00 USD | 13,820.00 USD |
| `7D` | `4097.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 805,470.00 USD | 0.00 USD | 47,970.00 USD |
| `1D` | `4101.10` | 252,320.00 USD | 252,320.00 USD | 0.00 USD | 65,200.00 USD | 0.00 USD | 13,700.00 USD |
| `7D` | `4101.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 227,440.00 USD | 0.00 USD | 40,870.00 USD |
| `1D` | `4105.30` | 537,220.00 USD | 537,220.00 USD | 0.00 USD | 272,350.00 USD | 0.00 USD | 12,550.00 USD |
| `7D` | `4105.70` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 606,780.00 USD | 0.00 USD | 90,730.00 USD |
| `1D` | `4109.50` | 888,500.00 USD | 888,500.00 USD | 0.00 USD | 301,860.00 USD | 0.00 USD | 49,410.00 USD |
| `7D` | `4110.00` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 68,720.00 USD |
| `1D` | `4113.70` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 299,000.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `4114.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 751,280.00 USD | 0.00 USD | 103,900.00 USD |
| `1D` | `4117.90` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 101,440.00 USD | 0.00 USD | 19,510.00 USD |
| `7D` | `4118.60` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 752,940.00 USD | 0.00 USD | 128,900.00 USD |
| `1D` | `4122.10` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 295,610.00 USD | 0.00 USD | 37,680.00 USD |
| `7D` | `4122.90` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 645,670.00 USD | 0.00 USD | 75,940.00 USD |
| `1D` | `4126.30` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 28,890.00 USD |
| `7D` | `4127.20` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 184,890.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `4130.50` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 21,900.00 USD | 0.00 USD | 18,990.00 USD |
| `7D` | `4131.50` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 155,590.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4134.70` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4135.80` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 21,340.00 USD |
| `1D` | `4138.90` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 89,640.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `4140.10` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 241,180.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `4143.10` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 45,040.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.40` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 54,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.70` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,000.00 USD |
| `1D` | `4151.50` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 15,790.00 USD | 0.00 USD | 9,870.00 USD |
| `7D` | `4153.00` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 18,110.00 USD |
| `7D` | `4157.30` | 10,600,000.00 USD | 10,600,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.60` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.90` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 350,530.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4170.20` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 361,230.00 USD | 0.00 USD | 82,140.00 USD |
| `7D` | `4174.50` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 212,100.00 USD | 0.00 USD | 23,570.00 USD |
| `1D` | `4176.70` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 65,340.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.80` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 325,580.00 USD | 0.00 USD | 13,490.00 USD |
| `1D` | `4180.90` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 42,890.00 USD | 0.00 USD | 4,400.00 USD |
| `7D` | `4183.10` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 146,480.00 USD | 0.00 USD | 28,330.00 USD |
| `1D` | `4185.10` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 96,770.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `4187.40` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 292,190.00 USD | 0.00 USD | 46,290.00 USD |
| `1D` | `4189.30` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 179,080.00 USD | 0.00 USD | 23,490.00 USD |
| `7D` | `4191.70` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 616,550.00 USD | 0.00 USD | 45,200.00 USD |
| `1D` | `4193.50` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 123,550.00 USD | 0.00 USD | 20,770.00 USD |
| `7D` | `4196.00` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 286,520.00 USD | 0.00 USD | 35,260.00 USD |
| `1D` | `4197.70` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 83,320.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4200.30` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 447,290.00 USD | 0.00 USD | 59,060.00 USD |
| `1D` | `4201.90` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 138,770.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4204.60` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 208,930.00 USD | 0.00 USD | 45,810.00 USD |
| `1D` | `4206.10` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 53,090.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4208.90` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 101,210.00 USD | 0.00 USD | 24,550.00 USD |
| `1D` | `4210.30` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 18,450.00 USD | 0.00 USD | 6,590.00 USD |
| `7D` | `4213.20` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 88,580.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `4214.50` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 38,650.00 USD | 0.00 USD | 8,650.00 USD |
| `7D` | `4217.50` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 103,080.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `4218.70` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 61,400.00 USD | 0.00 USD | 5,080.00 USD |
| `7D` | `4221.80` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 102,580.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `4222.90` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 23,220.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4226.10` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `4227.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 27,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4230.40` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `1D` | `4231.30` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4234.70` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 36,880.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4239.00` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.50` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4398.10` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 135,040.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `4402.40` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 121,510.00 USD | 0.00 USD | 13,930.00 USD |
| `7D` | `4406.70` | 15,780,000.00 USD | 15,780,000.00 USD | 0.00 USD | 112,910.00 USD | 0.00 USD | 19,700.00 USD |
| `7D` | `4411.00` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 89,870.00 USD | 0.00 USD | 27,000.00 USD |
| `7D` | `4415.30` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 56,960.00 USD | 0.00 USD | 6,370.00 USD |
| `1D` | `4416.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 8,150.00 USD | 0.00 USD | 1,530.00 USD |
| `7D` | `4419.60` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 106,130.00 USD | 0.00 USD | 3,450.00 USD |
| `1D` | `4420.30` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 24,480.00 USD | 0.00 USD | 2,100.00 USD |
| `7D` | `4423.90` | 16,120,000.00 USD | 16,120,000.00 USD | 0.00 USD | 35,830.00 USD | 0.00 USD | 7,080.00 USD |
| `1D` | `4424.50` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 23,020.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `4428.20` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 65,320.00 USD | 0.00 USD | 15,320.00 USD |
| `1D` | `4428.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 51,530.00 USD | 0.00 USD | 5,910.00 USD |
| `7D` | `4432.50` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 154,640.00 USD | 0.00 USD | 11,860.00 USD |
| `1D` | `4432.90` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 25,170.00 USD | 0.00 USD | 4,930.00 USD |
| `7D` | `4436.80` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 95,850.00 USD | 0.00 USD | 10,990.00 USD |
| `1D` | `4437.10` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 30,580.00 USD | 0.00 USD | 4,540.00 USD |
| `1D` | `4438.90` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 6,660.00 USD | 0.00 USD | 2,350.00 USD |
| `7D` | `4441.10` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 97,960.00 USD | 0.00 USD | 25,720.00 USD |
| `7D` | `4445.40` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 75,010.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `4448.40` | 16,720,000.00 USD | 16,720,000.00 USD | 0.00 USD | 37,880.00 USD | 0.00 USD | 8,110.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.00M` | Total OI Tokens: `68,335.7 PAXG`
  * 1h OI Change: `+0.14%` | 4h OI Change: `+0.05%` | 24h OI Change: `+0.14%`
  * Exchange Breakdown: Binance=`107.21M` | Bybit=`19.90M` | OKX=`-` | Hyperliquid=`24.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.31K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `40.30%` | `59.70%` | `0.68` | 2,050,000.00 USD |
| `15M` | `Binance` | `38.5%` | `61.5%` | `0.63` | 1,410,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `34.14%` | `65.86%` | `0.52` | 42,800.00 USD |
| `15M` | `KuCoin` | `71.09%` | `28.91%` | `2.46` | 140,030.00 USD |
| `15M` | `Gate` | `67.55%` | `32.45%` | `2.08` | 27,820.00 USD |
| `15M` | `Bitget` | `46.85%` | `53.15%` | `0.88` | 126,800.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `6.83%` | `93.17%` | `0.07` | 13,970.00 USD |
| `15M` | `Bitunix` | `12.5%` | `87.5%` | `0.14` | 88,600.00 USD |
| `15M` | `Hyperliquid` | `2.04%` | `97.96%` | `0.02` | 114,450.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.29%` | `0.71%` | `139.85` | 67,790.00 USD |
| `15M` | `HTX` | `34.18%` | `65.82%` | `0.52` | 4,770.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 245.39 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 1,120.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `84.02%` | `15.98%` | `5.26` | 6,580.00 USD |
| `15M` | `Whale Positions` | `38.5%` | `61.5%` | `0.63` | 1,410,000.00 USD |
| `15M` | `Global Accounts` | `40.30%` | `59.70%` | `0.68` | 2,050,000.00 USD |
| `1H` | `PAXG` | `43.68%` | `56.32%` | `0.78` | 32,030,000.00 USD |
| `1H` | `Binance` | `53.99%` | `46.01%` | `1.17` | 2,210,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `58.41%` | `41.59%` | `1.40` | 2,430,000.00 USD |
| `1H` | `KuCoin` | `57.62%` | `42.38%` | `1.36` | 56,010.00 USD |
| `1H` | `Gate` | `62.86%` | `37.14%` | `1.69` | 1,130,000.00 USD |
| `1H` | `Bitget` | `63.46%` | `36.54%` | `1.74` | 744,880.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `39.29%` | `60.71%` | `0.65` | 21,810,000.00 USD |
| `1H` | `Bitunix` | `39.39%` | `60.61%` | `0.65` | 1,070,000.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.84%` | `49.16%` | `1.03` | 2,080,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `22.15%` | `77.85%` | `0.28` | 443,990.00 USD |
| `1H` | `HTX` | `46.73%` | `53.27%` | `0.88` | 2,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `33.65%` | `66.35%` | `0.51` | 58,320.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `53.99%` | `46.01%` | `1.17` | 2,210,000.00 USD |
| `1H` | `Global Accounts` | `43.68%` | `56.32%` | `0.78` | 32,030,000.00 USD |
| `4H` | `PAXG` | `51.33%` | `48.67%` | `1.05` | 18,470,000.00 USD |
| `4H` | `Binance` | `53.19%` | `46.81%` | `1.14` | 10,360,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `58.14%` | `41.86%` | `1.39` | 412,200.00 USD |
| `4H` | `KuCoin` | `53.24%` | `46.76%` | `1.14` | 1,310,000.00 USD |
| `4H` | `Gate` | `69.11%` | `30.89%` | `2.24` | 279,760.00 USD |
| `4H` | `Bitget` | `52.87%` | `47.13%` | `1.12` | 1,890,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `10.39%` | `89.61%` | `0.12` | 578,450.00 USD |
| `4H` | `Bitunix` | `45.66%` | `54.34%` | `0.84` | 336,850.00 USD |
| `4H` | `Hyperliquid` | `36.91%` | `63.09%` | `0.59` | 1,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `63.9%` | `36.1%` | `1.77` | 1,490,000.00 USD |
| `4H` | `HTX` | `56.41%` | `43.59%` | `1.29` | 51,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.63%` | `53.37%` | `0.87` | 41,820.00 USD |
| `4H` | `Aster` | `48.33%` | `51.67%` | `0.94` | 24,770.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.86%` | `76.14%` | `0.31` | 77,750.00 USD |
| `4H` | `Whale Positions` | `53.19%` | `46.81%` | `1.14` | 10,360,000.00 USD |
| `4H` | `Global Accounts` | `51.33%` | `48.67%` | `1.05` | 18,470,000.00 USD |


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
| `5m` | -73,270.00 USD | -129,600.00 USD | **`DISTRIBUTION`** |
| `15m` | 20,000.00 USD | -352,290.00 USD | **`DISTRIBUTION`** |
| `30m` | 156,070.00 USD | -362,340.00 USD | **`DISTRIBUTION`** |
| `1h` | 56,800.00 USD | -33,850.00 USD | **`ACCUMULATION`** |
| `2h` | -102,250.00 USD | -365,790.00 USD | **`DISTRIBUTION`** |
| `4h` | -519,030.00 USD | 671,860.00 USD | **`ACCUMULATION`** |
| `6h` | 228,080.00 USD | 503,950.00 USD | **`ACCUMULATION`** |
| `8h` | 27,280.00 USD | 1,320,000.00 USD | **`ACCUMULATION`** |
| `12h` | -219,470.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `24h` | 224,660.00 USD | 1,380,000.00 USD | **`ACCUMULATION`** |
| `1w` | -7,720,000.00 USD | -7,730,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -19,790,000.00 USD | -71,530,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-73.27K` | 15m=`+20.00K` | 1h=`+56.80K` | 24h=`+224.66K`
* Futures Capital Netflows: 5m=`-129.60K` | 15m=`-352.29K` | 1h=`-33.85K` | 24h=`+1.38M`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `4008.26` (Risk Distance: `8.41` pts)
  * +2.5R Take Profit: `4037.69`
  * Mathematical Lot Sizing: **`1.18 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4039.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4048.08` (Risk Distance: `8.41` pts)
  * +2.5R Take Profit: `4018.65`
  * Mathematical Lot Sizing: **`1.18 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4055.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
