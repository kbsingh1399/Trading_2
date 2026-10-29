# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUAUD
**Canonical Key**: `XAUAUD` | **Broker Instrument**: `XAUAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 02:21:35 IST` (`2026-10-29 20:51:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `5724.69` | **Live Ask Quote**: `5725.49` | **Mid Price**: `5725.09`
- **Spread Points**: `80.00` | **Spread BPS**: `1.40 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
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
  * Value Area High (VAH) = `5737.68` (Distance: `-0.22%`)
  * Point of Control (POC) = `5726.72` (Distance: `-0.03%`)
  * Value Area Low (VAL) = `5712.43` (Distance: `+0.22%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`5764.78` | POC=`5754.66` | VAL=`5735.88`
  * Prior Day Extremes: PDH=`5785.73` | PDL=`5713.48` | PDC=`5765.90`
  * Monday Range Blueprint: High=`5739.86` | Mid=`5698.93` | Low=`5658.00`
  * Developing Weekly Value Area: Weekly VAH=`5753.80` | Weekly POC=`5728.25` | Weekly VAL=`5701.85`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`5767.92` | Low=`5722.11`
  * London Session (08:00-16:00 UTC): High=`5737.22` | Low=`5707.15`
  * New York Session (13:00-21:00 UTC): High=`5748.81` | Low=`5697.63`
  * Initial Balance (First Hour): IB High=`5734.96` | IB Low=`5707.15`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `5702.19` - `5747.99`
  * Optimal Trade Entry (OTE 0.705): `5736.54`
  * Structural Invalidation Anchor (0.786): `5770.89`

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
| `1249` | `0xead5...69f2` | `LONG` | 1,828,159.20 USD | `453.78` | `4220.88` | `4023.10` | `3538.92` | -87,208.86 USD | `-4.77%` | `5X Isolated` |
| `1364` | `0x46fc...1195` | `LONG` | 1,647,454.13 USD | `409.49` | `4055.28` | `4023.10` | `2053.63` | -13,136.75 USD | `-0.80%` | `20X Cross` |
| `1393` | `0x6d15...d374` | `LONG` | 1,611,600.00 USD | `400.00` | `4068.25` | `4023.10` | `3841.79` | -15,700.00 USD | `-0.97%` | `25X Cross` |
| `1396` | `0xee02...309d` | `SHORT` | 1,610,480.00 USD | `400.00` | `4438.84` | `4023.10` | `4226.86` | 165,058.60 USD | `+10.25%` | `25X Isolated` |
| `1437` | `0x02a7...fe9f` | `SHORT` | 1,569,399.00 USD | `390.00` | `4055.02` | `4023.10` | `4306.68` | 12,060.25 USD | `+0.77%` | `25X Cross` |
| `1479` | `0x7e77...b8d2` | `SHORT` | 1,528,778.00 USD | `380.00` | `4131.92` | `4023.10` | `4293.49` | 41,351.64 USD | `+2.70%` | `20X Cross` |
| `1501` | `0x72c2...9b37` | `LONG` | 1,501,107.22 USD | `373.13` | `4000.98` | `4023.10` | `3778.02` | 8,213.70 USD | `+0.55%` | `13X Isolated` |
| `1537` | `0xaa44...b844` | `LONG` | 1,448,640.00 USD | `360.00` | `4043.10` | `4023.10` | `2803.24` | -6,877.63 USD | `-0.47%` | `4X Cross` |
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
  * 24H Horizon: Short MP=`4115.08` (Vol: 152,200.00 USD, Dist: `+2.30%`) | Long MP=`3965.14` (Vol: 154,800.00 USD, Dist: `--1.43%`)
  * 48H Horizon: Short MP=`4118.09` (Vol: 350,900.00 USD, Dist: `+2.37%`) | Long MP=`3957.22` (Vol: 390,800.00 USD, Dist: `--1.63%`)
  * 3D Horizon: Short MP=`4110.46` (Vol: 300,700.00 USD, Dist: `+2.18%`) | Long MP=`3959.21` (Vol: 388,300.00 USD, Dist: `--1.58%`)
  * 7D Horizon: Short MP=`4082.49` (Vol: 552,000.00 USD, Dist: `+1.49%`) | Long MP=`3921.81` (Vol: 617,500.00 USD, Dist: `--2.51%`)
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
| `1D` | `3609.80` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3609.80` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `1D` | `3614.00` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3614.00` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `1D` | `3618.20` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 7,370.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3618.20` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 7,370.00 USD | 0.00 USD | 27,380.00 USD |
| `1D` | `3622.40` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `7D` | `3622.40` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `1D` | `3626.60` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `3626.60` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `1D` | `3630.80` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3630.80` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `1D` | `3635.00` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3635.00` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `1D` | `3639.20` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3639.20` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.40` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3643.40` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `1D` | `3647.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 1,030.00 USD | 0.00 USD | 12,640.00 USD |
| `7D` | `3647.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 1,030.00 USD | 0.00 USD | 12,640.00 USD |
| `1D` | `3651.80` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3651.80` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `3656.00` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 1,730.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `3656.00` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 1,730.00 USD | 0.00 USD | 5,900.00 USD |
| `1D` | `3849.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3849.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `1D` | `3853.40` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `3853.40` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `1D` | `3857.60` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 23,940.00 USD | 0.00 USD | 74,240.00 USD |
| `7D` | `3857.60` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 23,940.00 USD | 0.00 USD | 74,240.00 USD |
| `1D` | `3861.80` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 60,240.00 USD | 0.00 USD | 187,340.00 USD |
| `7D` | `3861.80` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 60,240.00 USD | 0.00 USD | 187,340.00 USD |
| `1D` | `3866.00` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 78,760.00 USD | 0.00 USD | 134,060.00 USD |
| `7D` | `3866.00` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 78,760.00 USD | 0.00 USD | 134,060.00 USD |
| `1D` | `3870.20` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `7D` | `3870.20` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `1D` | `3874.40` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `7D` | `3874.40` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `1D` | `3878.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `7D` | `3878.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3882.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3882.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `3887.00` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `3887.00` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `3891.20` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,840.00 USD | 0.00 USD | 39,210.00 USD |
| `7D` | `3891.20` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,840.00 USD | 0.00 USD | 39,210.00 USD |
| `1D` | `3895.40` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3895.40` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `1D` | `3899.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,110.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `3899.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,110.00 USD | 0.00 USD | 16,340.00 USD |
| `1D` | `3929.00` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3929.00` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `1D` | `3933.20` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3933.20` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `1D` | `3937.40` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 47,890.00 USD | 0.00 USD | 140,290.00 USD |
| `7D` | `3937.40` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 47,890.00 USD | 0.00 USD | 140,290.00 USD |
| `1D` | `3941.60` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 95,210.00 USD | 0.00 USD | 291,500.00 USD |
| `7D` | `3941.60` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 95,210.00 USD | 0.00 USD | 291,500.00 USD |
| `1D` | `3945.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `3945.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `1D` | `3950.00` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `7D` | `3950.00` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `1D` | `3954.20` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `7D` | `3954.20` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `1D` | `3958.40` | 664,290.00 USD | 0.00 USD | 664,290.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `7D` | `3958.40` | 664,290.00 USD | 0.00 USD | 664,290.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `1D` | `3962.60` | 434,690.00 USD | 0.00 USD | 434,690.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3962.60` | 434,690.00 USD | 0.00 USD | 434,690.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `1D` | `3966.80` | 378,370.00 USD | 0.00 USD | 378,370.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3966.80` | 378,370.00 USD | 0.00 USD | 378,370.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `1D` | `3971.00` | 241,240.00 USD | 0.00 USD | 241,240.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3971.00` | 241,240.00 USD | 0.00 USD | 241,240.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `1D` | `3975.20` | 174,850.00 USD | 0.00 USD | 174,850.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3975.20` | 174,850.00 USD | 0.00 USD | 174,850.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `1D` | `3979.40` | 62,150.00 USD | 0.00 USD | 62,150.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3979.40` | 62,150.00 USD | 0.00 USD | 62,150.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `4016.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4019.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `7D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `1D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `1D` | `4097.00` | 452,500.00 USD | 452,500.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 109,700.00 USD |
| `7D` | `4097.00` | 452,500.00 USD | 452,500.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 109,700.00 USD |
| `1D` | `4101.20` | 711,940.00 USD | 711,940.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 200,210.00 USD |
| `7D` | `4101.20` | 711,940.00 USD | 711,940.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 200,210.00 USD |
| `1D` | `4105.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 181,350.00 USD | 0.00 USD | 406,570.00 USD |
| `7D` | `4105.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 181,350.00 USD | 0.00 USD | 406,570.00 USD |
| `1D` | `4109.60` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `7D` | `4109.60` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `1D` | `4113.80` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `7D` | `4113.80` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `1D` | `4118.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `4118.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `1D` | `4122.20` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `4122.20` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `1D` | `4126.40` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4126.40` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `1D` | `4130.60` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4130.60` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `1D` | `4134.80` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4134.80` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `1D` | `4139.00` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4139.00` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `1D` | `4143.20` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 12,230.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `4143.20` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 12,230.00 USD | 0.00 USD | 32,690.00 USD |
| `1D` | `4168.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `4168.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `1D` | `4172.60` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4172.60` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `1D` | `4176.80` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `7D` | `4176.80` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `1D` | `4181.00` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 81,660.00 USD |
| `7D` | `4181.00` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 81,660.00 USD |
| `1D` | `4185.20` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 203,210.00 USD |
| `7D` | `4185.20` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 203,210.00 USD |
| `1D` | `4189.40` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `4189.40` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `1D` | `4193.60` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `7D` | `4193.60` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `1D` | `4197.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `4197.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `1D` | `4202.00` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `4202.00` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `1D` | `4206.20` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4206.20` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `4210.40` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4210.40` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `4214.60` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4214.60` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 19,870.00 USD |
| `1D` | `4218.80` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `7D` | `4218.80` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `1D` | `4223.00` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `4223.00` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `1D` | `4407.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4407.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `1D` | `4412.00` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `4412.00` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `1D` | `4416.20` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `4416.20` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `1D` | `4420.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `7D` | `4420.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `1D` | `4424.60` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 53,200.00 USD |
| `7D` | `4424.60` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 53,200.00 USD |
| `1D` | `4428.80` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `7D` | `4428.80` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `1D` | `4433.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `7D` | `4433.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4433.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4433.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `825.09M` | Total OI Tokens: `205,298.7 XAUT`
  * 1h OI Change: `-2.24%` | 4h OI Change: `-1.97%` | 24h OI Change: `+0.64%`
  * Exchange Breakdown: Binance=`61.76M` | Bybit=`143.46M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `91.56K` | Last 24h: `245.96K` | Last 3d: `915.11K` | Last 7d: `2.40M`
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
| `15M` | `XAUT` | `19.58%` | `80.42%` | `0.24` | 11,400,000.00 USD |
| `15M` | `Binance` | `38.42%` | `61.58%` | `0.62` | 906,580.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `40.9%` | `59.1%` | `0.69` | 377,950.00 USD |
| `15M` | `KuCoin` | `32.32%` | `67.68%` | `0.48` | 11,270.00 USD |
| `15M` | `Gate` | `41%` | `59%` | `0.69` | 216,560.00 USD |
| `15M` | `Bitget` | `48.92%` | `51.08%` | `0.96` | 95,620.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `14.78%` | `85.22%` | `0.17` | 8,790,000.00 USD |
| `15M` | `Bitunix` | `17.66%` | `82.34%` | `0.21` | 331,830.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `39.18%` | `60.82%` | `0.64` | 594,440.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 75,920.00 USD |
| `15M` | `HTX` | `30.7%` | `69.3%` | `0.44` | 759.79 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 3,410.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `38.42%` | `61.58%` | `0.62` | 906,580.00 USD |
| `15M` | `Global Accounts` | `19.58%` | `80.42%` | `0.24` | 11,400,000.00 USD |
| `1H` | `XAUT` | `41.93%` | `58.07%` | `0.72` | 42,730,000.00 USD |
| `1H` | `Binance` | `40.46%` | `59.54%` | `0.68` | 16,730,000.00 USD |
| `1H` | `OKX` | `40.64%` | `59.36%` | `0.68` | 6,400,000.00 USD |
| `1H` | `Bybit` | `42.21%` | `57.79%` | `0.73` | 4,950,000.00 USD |
| `1H` | `KuCoin` | `41.99%` | `58.01%` | `0.72` | 363,360.00 USD |
| `1H` | `Gate` | `43.84%` | `56.16%` | `0.78` | 1,560,000.00 USD |
| `1H` | `Bitget` | `40.02%` | `59.98%` | `0.67` | 1,880,000.00 USD |
| `1H` | `BingX` | `61.35%` | `38.65%` | `1.59` | 1,510,000.00 USD |
| `1H` | `MEXC` | `43.36%` | `56.64%` | `0.77` | 4,710,000.00 USD |
| `1H` | `Bitunix` | `46.39%` | `53.61%` | `0.87` | 846,110.00 USD |
| `1H` | `Hyperliquid` | `29.48%` | `70.52%` | `0.42` | 1,860,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.24%` | `48.76%` | `1.05` | 1,240,000.00 USD |
| `1H` | `Crypto.com` | `44.4%` | `55.6%` | `0.80` | 9,660.00 USD |
| `1H` | `WhiteBIT` | `64.6%` | `35.4%` | `1.82` | 238,840.00 USD |
| `1H` | `HTX` | `51.13%` | `48.87%` | `1.05` | 26,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.4%` | `58.6%` | `0.71` | 183,950.00 USD |
| `1H` | `Aster` | `29.79%` | `70.21%` | `0.42` | 93,880.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `35.17%` | `64.83%` | `0.54` | 120,250.00 USD |
| `1H` | `Whale Positions` | `40.46%` | `59.54%` | `0.68` | 16,730,000.00 USD |
| `1H` | `Global Accounts` | `41.93%` | `58.07%` | `0.72` | 42,730,000.00 USD |
| `4H` | `XAUT` | `46.57%` | `53.43%` | `0.87` | 64,550,000.00 USD |
| `4H` | `Binance` | `53.85%` | `46.15%` | `1.17` | 5,070,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.12%` | `46.88%` | `1.13` | 5,930,000.00 USD |
| `4H` | `KuCoin` | `48.1%` | `51.9%` | `0.93` | 261,390.00 USD |
| `4H` | `Gate` | `56.03%` | `43.97%` | `1.27` | 2,350,000.00 USD |
| `4H` | `Bitget` | `51.03%` | `48.97%` | `1.04` | 1,980,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `44.29%` | `55.71%` | `0.80` | 40,610,000.00 USD |
| `4H` | `Bitunix` | `50.12%` | `49.88%` | `1.00` | 2,230,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.25%` | `49.75%` | `1.01` | 4,820,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.58%` | `87.42%` | `0.14` | 1,150,000.00 USD |
| `4H` | `HTX` | `58.86%` | `41.14%` | `1.43` | 14,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.97%` | `63.03%` | `0.59` | 149,000.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.85%` | `46.15%` | `1.17` | 5,070,000.00 USD |
| `4H` | `Global Accounts` | `46.57%` | `53.43%` | `0.87` | 64,550,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4015.95` | `4015.70` | `4015.95` | `4018.95` | `4013.55` | 13,405,013.83 USD | 4,667,069.40 USD | 8,737,944.43 USD | -4,070,875.03 USD | `-30.37%` | `0B / 8S` |
| `0:00 UTC` | `4016.25` | `4015.09` | `4016.25` | `4017.15` | `4012.95` | 11,069,583.99 USD | 5,073,905.23 USD | 5,995,678.75 USD | -921,773.52 USD | `-8.33%` | `1B / 0S` |
| `5:00 UTC` | `4018.65` | `4017.94` | `4018.65` | `4019.55` | `4015.65` | 8,462,808.39 USD | 3,963,106.36 USD | 4,499,702.03 USD | -536,595.67 USD | `-6.34%` | `3B / 1S` |
| `0:00 UTC` | `4020.15` | `4019.82` | `4020.15` | `4021.95` | `4017.45` | 8,239,213.90 USD | 4,102,043.46 USD | 4,137,170.44 USD | -35,126.97 USD | `-0.43%` | `2B / 1S` |
| `5:00 UTC` | `4023.15` | `4021.35` | `4023.15` | `4024.65` | `4017.45` | 6,445,259.27 USD | 3,466,207.92 USD | 2,979,051.36 USD | 487,156.56 USD | `+7.56%` | `8B / 2S` |
| `0:00 UTC` | `4026.15` | `4025.44` | `4026.15` | `4027.05` | `4022.85` | 9,144,271.05 USD | 4,882,647.78 USD | 4,261,623.27 USD | 621,024.51 USD | `+6.79%` | `3B / 0S` |
| `5:00 UTC` | `4027.95` | `4028.04` | `4027.95` | `4030.05` | `4025.55` | 9,968,155.30 USD | 4,171,077.53 USD | 5,797,077.77 USD | -1,626,000.23 USD | `-16.31%` | `1B / 2S` |
| `0:00 UTC` | `4036.05` | `4033.96` | `4036.05` | `4039.35` | `4027.95` | 35,619,288.58 USD | 16,236,367.43 USD | 19,382,921.15 USD | -3,146,553.72 USD | `-8.83%` | `3B / 3S` |
| `5:00 UTC` | `4033.05` | `4032.94` | `4033.05` | `4034.85` | `4030.95` | 10,349,985.63 USD | 4,839,786.31 USD | 5,510,199.31 USD | -670,413.00 USD | `-6.48%` | `1B / 3S` |
| `0:00 UTC` | `4034.25` | `4034.24` | `4034.25` | `4035.75` | `4032.15` | 12,254,377.32 USD | 4,050,455.74 USD | 8,203,921.58 USD | -4,153,465.83 USD | `-33.89%` | `0B / 4S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |
| `10-28 20:04` | `Volume 5.0K XAU` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `4045.20` | 1,000.00 USD | 0.00 USD |
| `10-28 17:48` | `Volume 5.0K XAU` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `4068.50` | 2,200.00 USD | 0.00 USD |
| `10-28 16:57` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4052.80` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 10:56` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4041.20` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_EUR (XAUEUR.pi) Metal Auction: ROTA | `3633.06` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_GBP (XAUGBP.pi) Metal Auction: ROTA | `3040.99` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -164,150.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -275,740.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -235,310.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -100,610.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -112,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -602,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -661,740.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,230,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | 592,590.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `24h` | -992,750.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -79,970,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,770,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-164.15K` | 15m=`-275.74K` | 1h=`-100.61K` | 24h=`-992.75K`
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
  * Execution Entry: `5712.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `5702.94` (Risk Distance: `9.49` pts)
  * +2.5R Take Profit: `5736.15`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.09 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `5737.68` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `5747.17` (Risk Distance: `9.49` pts)
  * +2.5R Take Profit: `5713.96`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.09 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`5770.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
