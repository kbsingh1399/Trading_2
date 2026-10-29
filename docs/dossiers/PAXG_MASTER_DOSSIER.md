# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 04:04:42 IST` (`2026-10-29 22:34:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4018.34` | **Live Ask Quote**: `4018.42` | **Mid Price**: `4018.38`
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
  * Value Area High (VAH) = `4024.79` (Distance: `-0.16%`)
  * Point of Control (POC) = `4020.72` (Distance: `-0.06%`)
  * Value Area Low (VAL) = `4018.30` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4018.26`
  * London Session (08:00-16:00 UTC): High=`4034.45` | Low=`4002.31`
  * New York Session (13:00-21:00 UTC): High=`4042.49` | Low=`3994.27`
  * Initial Balance (First Hour): IB High=`4030.44` | IB Low=`4006.32`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4002.31` - `4034.45`
  * Optimal Trade Entry (OTE 0.705): `4026.42`
  * Structural Invalidation Anchor (0.786): `4050.53`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4022.62` | `4023.57` | `4021.65` | `4022.01` | `32` | 130,542.54 USD | 68,711.81 USD | `+52.64%` | 2,155,633.29 USD | `+0.77` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4022.02` | `4022.21` | `4021.27` | `4021.48` | `25` | 101,856.61 USD | -26,164.81 USD | `-25.69%` | 2,129,468.48 USD | `-0.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4021.48` | `4021.48` | `4021.47` | `4021.48` | `2` | 6,526.85 USD | -2,408.86 USD | `-36.91%` | 2,127,059.62 USD | `-0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4020.01` | `4020.01` | `4018.12` | `4018.13` | `44` | 175,174.25 USD | -58,319.99 USD | `-33.29%` | 1,935,454.73 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4018.12` | `4025.28` | `4017.72` | `4022.63` | `250` | 1,005,666.39 USD | 151,466.76 USD | `+15.06%` | 2,086,921.48 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4022.62` | `4023.57` | `4021.27` | `4021.48` | `59` | 238,926.00 USD | 40,138.14 USD | `+16.80%` | 2,127,059.62 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,839,422.95 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,963,502.96 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4025.28` | `4017.72` | `4021.48` | `309` | 1,244,592.39 USD | 191,604.89 USD | `+15.39%` | 2,155,107.85 USD | `+0.36` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4021.48` | `1,961` | 7,892,008.03 USD | 76,542.99 USD | `+0.97%` | 1,323,690.32 USD | `-0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4021.48` | `1,961` | 7,892,008.03 USD | 76,542.99 USD | `+0.97%` | 1,323,690.32 USD | `-0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `4018.90` | `24.9371` | 100,219.71 USD | 1,895,060.01 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `4019.00` | `334.4318` | 1,344,081.40 USD | 1,794,840.29 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `4019.10` | `4.5075` | 18,116.09 USD | 450,758.89 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `4019.20` | `3.0900` | 12,419.33 USD | 432,642.80 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4019.30` | `0.4187` | 1,682.88 USD | 420,223.47 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `4019.40` | `10.2505` | 41,200.86 USD | 418,540.59 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4019.50` | `3.4442` | 13,843.96 USD | 377,339.73 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4019.60` | `2.0942` | 8,417.85 USD | 363,495.77 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4019.70` | `27.5274` | 110,651.89 USD | 355,077.92 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `4019.80` | `3.7928` | 15,246.30 USD | 244,426.03 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4019.90` | `7.8772` | 31,665.56 USD | 229,179.73 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `4020.00` | `8.6179` | 34,643.96 USD | 197,514.18 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4020.10` | `5.2771` | 21,214.47 USD | 162,870.22 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4020.20` | `2.8576` | 11,488.12 USD | 141,655.75 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4020.40` | `7.1920` | 28,914.72 USD | 130,167.63 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `4020.50` | `6.5400` | 26,294.07 USD | 101,252.91 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4020.60` | `1.5372` | 6,180.47 USD | 74,958.84 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4020.80` | `1.9098` | 7,678.92 USD | 68,778.37 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4020.90` | `3.8196` | 15,358.23 USD | 61,099.45 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `4021.10` | `11.3753` | 45,741.22 USD | 45,741.22 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4021.15` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,021.15` | `0.00%` | `-` |
| `ASK` | `4021.20` | `206.0293` | 828,485.02 USD | 828,485.02 USD | `29 orders` | `+0.00%` | `-` |
| `ASK` | `4021.30` | `20.0884` | 80,781.48 USD | 909,266.50 USD | `8 orders` | `+0.00%` | `-` |
| `ASK` | `4021.40` | `34.8007` | 139,947.53 USD | 1,049,214.04 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `4021.50` | `0.7678` | 3,087.71 USD | 1,052,301.75 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4021.60` | `12.3493` | 49,663.94 USD | 1,101,965.69 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4021.70` | `8.6028` | 34,597.88 USD | 1,136,563.57 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4021.80` | `0.0497` | 199.88 USD | 1,136,763.46 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4021.90` | `15.4713` | 62,224.02 USD | 1,198,987.48 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4022.00` | `2.5525` | 10,266.16 USD | 1,209,253.63 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4022.10` | `4.9120` | 19,756.56 USD | 1,229,010.19 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4022.20` | `13.4264` | 54,003.67 USD | 1,283,013.85 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4022.30` | `2.9833` | 11,999.73 USD | 1,295,013.58 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4022.40` | `5.2144` | 20,974.40 USD | 1,315,987.98 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `4022.50` | `5.2216` | 21,003.89 USD | 1,336,991.87 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4022.60` | `0.0547` | 220.04 USD | 1,337,211.91 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4022.70` | `2.5324` | 10,187.09 USD | 1,347,398.99 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4022.80` | `16.7020` | 67,188.81 USD | 1,414,587.80 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4022.90` | `1.2371` | 4,976.73 USD | 1,419,564.53 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4023.00` | `13.9615` | 56,167.11 USD | 1,475,731.64 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4023.10` | `2.9828` | 12,000.10 USD | 1,487,731.74 USD | `1 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x5b5d...c060` | `SHORT` | 25,592,022.35 USD | `6,365.38` | `4188.90` | `4020.70` | `32335.12` | 1,071,948.94 USD | `+4.19%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,491,383.07 USD | `6,339.88` | `4132.72` | `4020.70` | `13743.36` | 709,621.67 USD | `+2.78%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,601,104.52 USD | `5,869.90` | `4228.86` | `4020.70` | `30020.64` | 1,221,917.42 USD | `+5.18%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,413,171.52 USD | `4,828.91` | `4157.43` | `4020.70` | `2222.39` | -662,710.80 USD | `-3.41%` | `25X Cross` |
| `145` | `0x645b...87b8` | `LONG` | 14,205,460.17 USD | `3,533.26` | `4129.11` | `4020.70` | `432.20` | -383,767.11 USD | `-2.70%` | `3X Cross` |
| `161` | `0x7a6d...f79c` | `SHORT` | 13,139,851.17 USD | `3,268.21` | `4228.94` | `4020.70` | `4397.21` | 681,227.96 USD | `+5.18%` | `25X Cross` |
| `180` | `0xa742...e390` | `SHORT` | 11,659,450.40 USD | `2,900.00` | `4364.92` | `4020.70` | `4235.67` | 998,825.93 USD | `+8.57%` | `20X Cross` |
| `265` | `0xfc66...ca06` | `SHORT` | 8,986,102.96 USD | `2,235.07` | `4031.28` | `4020.70` | `11040.44` | 24,109.69 USD | `+0.27%` | `3X Cross` |
| `266` | `0x3678...b209` | `LONG` | 8,845,320.00 USD | `2,200.00` | `4176.09` | `4020.70` | `2618.63` | -342,099.30 USD | `-3.87%` | `25X Cross` |
| `267` | `0x41e5...0825` | `SHORT` | 8,844,660.00 USD | `2,200.00` | `4112.20` | `4020.70` | `4331.15` | 202,194.59 USD | `+2.29%` | `20X Cross` |
| `301` | `0xacb6...efbd` | `SHORT` | 7,941,576.39 USD | `1,975.37` | `4048.55` | `4020.70` | `6509.36` | 55,815.32 USD | `+0.70%` | `6X Cross` |
| `372` | `0xc26c...b8f4` | `LONG` | 6,352,196.21 USD | `1,579.95` | `4075.62` | `4020.70` | `0.000000` | -87,100.76 USD | `-1.37%` | `1X Cross` |
| `401` | `0x12d2...f97f` | `LONG` | 5,636,230.64 USD | `1,401.94` | `4278.91` | `4020.70` | `3040.77` | -362,559.94 USD | `-6.43%` | `20X Cross` |
| `551` | `0x63da...8add` | `LONG` | 4,020,600.00 USD | `1,000.00` | `4021.46` | `4020.70` | `3564.11` | -860.96 USD | `-0.02%` | `25X Cross` |
| `572` | `0x354b...6425` | `LONG` | 3,949,407.88 USD | `982.24` | `4031.85` | `4020.70` | `0.000000` | -10,858.52 USD | `-0.27%` | `10X Cross` |
| `579` | `0x9aa5...58af` | `LONG` | 3,906,389.50 USD | `971.64` | `4279.98` | `4020.70` | `0.000000` | -252,219.59 USD | `-6.46%` | `20X Cross` |
| `606` | `0xf3dc...1672` | `LONG` | 3,742,148.12 USD | `930.74` | `4024.62` | `4020.70` | `3337.59` | -3,744.44 USD | `-0.10%` | `20X Cross` |
| `675` | `0x4a20...3c26` | `LONG` | 3,366,765.49 USD | `837.40` | `4599.73` | `4020.70` | `0.000000` | -485,054.89 USD | `-14.41%` | `20X Cross` |
| `818` | `0x0fac...7a0a` | `LONG` | 2,759,944.29 USD | `686.49` | `4290.34` | `4020.70` | `1372.27` | -185,314.41 USD | `-6.71%` | `25X Cross` |
| `873` | `0xd8c5...99b0` | `SHORT` | 2,582,652.11 USD | `642.35` | `4175.35` | `4020.70` | `32847.58` | 99,409.07 USD | `+3.85%` | `4X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,492,586.00 USD | `620.00` | `4122.81` | `4020.70` | `4342.25` | 63,561.03 USD | `+2.55%` | `20X Cross` |
| `935` | `0xeae3...e8ad` | `SHORT` | 2,412,300.00 USD | `600.00` | `4104.77` | `4020.70` | `4325.27` | 50,565.11 USD | `+2.10%` | `20X Cross` |
| `936` | `0xf285...fa82` | `LONG` | 2,404,624.96 USD | `598.11` | `4146.45` | `4020.70` | `3891.24` | -75,394.59 USD | `-3.14%` | `25X Cross` |
| `957` | `0x12f7...8750` | `LONG` | 2,354,447.82 USD | `585.61` | `4082.77` | `4020.70` | `2484.26` | -36,469.16 USD | `-1.55%` | `10X Cross` |
| `1100` | `0x413c...886c` | `LONG` | 2,010,100.00 USD | `500.00` | `4010.43` | `4020.70` | `0.000000` | 4,883.77 USD | `+0.24%` | `2X Cross` |
| `1105` | `0x61ce...a62b` | `SHORT` | 2,000,312.32 USD | `497.50` | `4071.66` | `4020.70` | `4708.42` | 25,356.47 USD | `+1.27%` | `20X Cross` |
| `1109` | `0x0593...40f9` | `LONG` | 1,994,929.25 USD | `496.18` | `4024.57` | `4020.70` | `3701.73` | -1,974.58 USD | `-0.10%` | `10X Isolated` |
| `1182` | `0x2edd...8179` | `LONG` | 1,894,106.27 USD | `470.91` | `4164.68` | `4021.47` | `0.000000` | -67,095.04 USD | `-3.54%` | `10X Cross` |
| `1234` | `0xead5...69f2` | `LONG` | 1,824,528.93 USD | `453.78` | `4220.88` | `4020.70` | `3538.94` | -90,839.13 USD | `-4.98%` | `5X Isolated` |
| `1301` | `0x7a6d...f79c` | `SHORT` | 1,722,726.15 USD | `428.38` | `4136.09` | `4021.47` | `5744.01` | 49,088.86 USD | `+2.85%` | `10X Cross` |
| `1348` | `0x46fc...1195` | `LONG` | 1,651,188.97 USD | `410.66` | `4055.10` | `4020.70` | `2142.76` | -14,087.53 USD | `-0.85%` | `20X Cross` |
| `1380` | `0x6d15...d374` | `LONG` | 1,608,280.00 USD | `400.00` | `4068.25` | `4020.70` | `3841.81` | -19,020.00 USD | `-1.18%` | `25X Cross` |
| `1381` | `0xee02...309d` | `SHORT` | 1,608,200.00 USD | `400.00` | `4438.84` | `4020.70` | `4226.89` | 167,338.60 USD | `+10.41%` | `25X Isolated` |
| `1416` | `0x02a7...fe9f` | `SHORT` | 1,568,034.00 USD | `390.00` | `4055.02` | `4020.70` | `4306.71` | 13,425.25 USD | `+0.86%` | `25X Cross` |
| `1449` | `0x51f6...2b39` | `LONG` | 1,533,735.88 USD | `381.40` | `4234.15` | `4021.47` | `0.000000` | -81,180.01 USD | `-5.29%` | `10X Cross` |
| `1452` | `0x7e77...b8d2` | `SHORT` | 1,527,828.00 USD | `380.00` | `4131.92` | `4020.70` | `4293.51` | 42,301.64 USD | `+2.77%` | `20X Cross` |
| `1469` | `0x72c2...9b37` | `LONG` | 1,500,249.02 USD | `373.13` | `4000.98` | `4020.70` | `3778.05` | 7,355.50 USD | `+0.49%` | `13X Isolated` |
| `1519` | `0xaa44...b844` | `LONG` | 1,447,344.00 USD | `360.00` | `4043.10` | `4020.70` | `2803.27` | -8,173.63 USD | `-0.56%` | `4X Cross` |
| `1520` | `0x781e...96b7` | `SHORT` | 1,446,216.76 USD | `359.61` | `4364.97` | `4021.47` | `13340.24` | 123,484.16 USD | `+8.54%` | `10X Cross` |
| `1634` | `0xa41f...d50a` | `LONG` | 1,322,657.92 USD | `328.96` | `4468.89` | `4020.70` | `3833.19` | -147,439.94 USD | `-11.15%` | `15X Cross` |
| `1670` | `0xbf5a...88ba` | `SHORT` | 1,277,099.76 USD | `317.65` | `4091.80` | `4020.70` | `9934.38` | 22,683.27 USD | `+1.78%` | `20X Cross` |
| `1708` | `0xff31...ff6c` | `SHORT` | 1,246,386.00 USD | `310.00` | `4372.43` | `4020.70` | `4789.18` | 109,069.38 USD | `+8.75%` | `10X Isolated` |
| `1717` | `0xada6...6f88` | `LONG` | 1,238,748.07 USD | `308.10` | `4166.46` | `4020.70` | `1897.96` | -44,940.95 USD | `-3.63%` | `5X Cross` |
| `1741` | `0x5238...54e5` | `LONG` | 1,206,060.00 USD | `300.00` | `4023.33` | `4020.70` | `3833.96` | -939.31 USD | `-0.08%` | `15X Isolated` |
| `1885` | `0x50e2...d770` | `LONG` | 1,087,039.17 USD | `270.37` | `4243.58` | `4020.70` | `2562.10` | -60,287.29 USD | `-5.55%` | `20X Cross` |
| `1903` | `0x4c92...4f17` | `SHORT` | 1,072,323.10 USD | `266.72` | `4260.98` | `4020.70` | `6510.47` | 64,169.14 USD | `+5.98%` | `20X Cross` |
| `1965` | `0xd346...c4f3` | `LONG` | 1,025,926.26 USD | `255.17` | `4188.66` | `4020.70` | `3310.43` | -42,910.25 USD | `-4.18%` | `5X Isolated` |
| `2006` | `0x1581...463b` | `LONG` | 1,005,150.00 USD | `250.00` | `4003.77` | `4020.70` | `3547.61` | 4,206.41 USD | `+0.42%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.85` (Vol: 274,500.00 USD, Dist: `+2.19%`) | Long MP=`3937.39` (Vol: 356,200.00 USD, Dist: `--2.10%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.89%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.11%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.87%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.10%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.22%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.46%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,280,000.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 3,910,000.00 USD | 3,910,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.90` | 3,870,000.00 USD | 3,870,000.00 USD | 61,810.00 USD | 0.00 USD | 9,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,000,000.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.00` | 3,800,000.00 USD | 3,800,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,900,000.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.10` | 3,750,000.00 USD | 3,750,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,720,000.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.20` | 3,710,000.00 USD | 3,710,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.30` | 3,680,000.00 USD | 3,680,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,470,000.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.40` | 3,640,000.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.50` | 3,630,000.00 USD | 3,630,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,370,000.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.60` | 3,620,000.00 USD | 3,620,000.00 USD | 20,320.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,350,000.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.70` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,320,000.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,260,000.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,250,000.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,400,000.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,870,000.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.50` | 3,590,000.00 USD | 3,590,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,540,000.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.60` | 3,580,000.00 USD | 3,580,000.00 USD | 81,940.00 USD | 0.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.70` | 3,500,000.00 USD | 3,500,000.00 USD | 117,160.00 USD | 0.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,950,000.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.80` | 3,360,000.00 USD | 3,360,000.00 USD | 215,160.00 USD | 0.00 USD | 32,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.90` | 3,120,000.00 USD | 3,120,000.00 USD | 144,700.00 USD | 0.00 USD | 20,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.00` | 2,950,000.00 USD | 2,950,000.00 USD | 126,020.00 USD | 0.00 USD | 18,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.10` | 2,810,000.00 USD | 2,810,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,190,000.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.20` | 2,700,000.00 USD | 2,700,000.00 USD | 105,320.00 USD | 0.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,850,000.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.30` | 2,580,000.00 USD | 2,580,000.00 USD | 22,630.00 USD | 0.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,710,000.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.40` | 2,540,000.00 USD | 2,540,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,600,000.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.50` | 2,510,000.00 USD | 2,510,000.00 USD | 79,520.00 USD | 0.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.60` | 2,430,000.00 USD | 2,430,000.00 USD | 16,460.00 USD | 0.00 USD | 133.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,360,000.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.70` | 2,410,000.00 USD | 2,410,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,180,000.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,430,000.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.50` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.60` | 2,320,000.00 USD | 2,320,000.00 USD | 156,780.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,290,000.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.70` | 2,160,000.00 USD | 2,160,000.00 USD | 320,210.00 USD | 0.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,630,000.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.80` | 1,790,000.00 USD | 1,790,000.00 USD | 347,350.00 USD | 0.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.90` | 1,390,000.00 USD | 1,390,000.00 USD | 346,950.00 USD | 0.00 USD | 39,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.00` | 1,000,000.00 USD | 1,000,000.00 USD | 181,840.00 USD | 0.00 USD | 28,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.10` | 791,940.00 USD | 791,940.00 USD | 275,140.00 USD | 0.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 501,960.00 USD | 501,960.00 USD | 108,590.00 USD | 0.00 USD | 48,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.30` | 344,730.00 USD | 344,730.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.40` | 294,650.00 USD | 294,650.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.50` | 200,050.00 USD | 200,050.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.60` | 67,090.00 USD | 67,090.00 USD | 32,920.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.70` | 19,950.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.40` | 29,250.00 USD | 29,250.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.50` | 208,440.00 USD | 208,440.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.60` | 502,480.00 USD | 502,480.00 USD | 247,160.00 USD | 0.00 USD | 46,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.70` | 976,080.00 USD | 976,080.00 USD | 425,080.00 USD | 0.00 USD | 48,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.80` | 1,280,000.00 USD | 1,280,000.00 USD | 263,130.00 USD | 0.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.90` | 1,560,000.00 USD | 1,560,000.00 USD | 252,040.00 USD | 0.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.00` | 1,720,000.00 USD | 1,720,000.00 USD | 146,650.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.10` | 2,000,000.00 USD | 2,000,000.00 USD | 246,290.00 USD | 0.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.20` | 2,090,000.00 USD | 2,090,000.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.40` | 2,250,000.00 USD | 2,250,000.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.50` | 2,360,000.00 USD | 2,360,000.00 USD | 96,240.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.60` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.70` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.40` | 2,450,000.00 USD | 2,450,000.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.50` | 2,550,000.00 USD | 2,550,000.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.60` | 2,700,000.00 USD | 2,700,000.00 USD | 128,850.00 USD | 0.00 USD | 24,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.70` | 2,910,000.00 USD | 2,910,000.00 USD | 186,400.00 USD | 0.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.80` | 3,090,000.00 USD | 3,090,000.00 USD | 154,770.00 USD | 0.00 USD | 18,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.90` | 3,190,000.00 USD | 3,190,000.00 USD | 90,920.00 USD | 0.00 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.00` | 3,300,000.00 USD | 3,300,000.00 USD | 103,730.00 USD | 0.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.10` | 3,400,000.00 USD | 3,400,000.00 USD | 83,950.00 USD | 0.00 USD | 21,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.20` | 3,440,000.00 USD | 3,440,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.30` | 3,470,000.00 USD | 3,470,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.40` | 3,530,000.00 USD | 3,530,000.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.50` | 3,570,000.00 USD | 3,570,000.00 USD | 35,450.00 USD | 0.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.60` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.70` | 3,590,000.00 USD | 3,590,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.20` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 674.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.30` | 3,620,000.00 USD | 3,620,000.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.40` | 3,640,000.00 USD | 3,640,000.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.50` | 3,690,000.00 USD | 3,690,000.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.60` | 3,750,000.00 USD | 3,750,000.00 USD | 55,110.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4434.70` | 3,790,000.00 USD | 3,790,000.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
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
| `7D` | `3611.30` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.80` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 34,120.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.90` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 61,810.00 USD | 0.00 USD | 9,800.00 USD |
| `7D` | `3623.90` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.00` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `3628.10` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.10` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3632.30` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.20` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.30` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3640.70` | 15,470,000.00 USD | 0.00 USD | 15,470,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.40` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.50` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.10` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.60` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 20,320.00 USD | 0.00 USD | 1,480.00 USD |
| `7D` | `3653.30` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.70` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.50` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,810.00 USD | 0.00 USD | 2,150.00 USD |
| `7D` | `3854.90` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.60` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 81,940.00 USD | 0.00 USD | 4,760.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3860.70` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 117,160.00 USD | 0.00 USD | 15,000.00 USD |
| `7D` | `3863.30` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 183,740.00 USD | 0.00 USD | 71,710.00 USD |
| `1D` | `3864.80` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 215,160.00 USD | 0.00 USD | 32,280.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.90` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 144,700.00 USD | 0.00 USD | 20,980.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.00` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 126,020.00 USD | 0.00 USD | 18,010.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.10` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3880.10` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3881.20` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 105,320.00 USD | 0.00 USD | 21,980.00 USD |
| `7D` | `3884.30` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3885.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 22,630.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3888.50` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.40` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,600,000.00 USD | 0.00 USD | 10,600,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.50` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 79,520.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.60` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 16,460.00 USD | 0.00 USD | 133.60 USD |
| `7D` | `3901.10` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.70` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,180,000.00 USD | 0.00 USD | 10,180,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.50` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 11,870.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.60` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 156,780.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `3938.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.70` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 320,210.00 USD | 0.00 USD | 52,850.00 USD |
| `7D` | `3943.10` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3946.80` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 347,350.00 USD | 0.00 USD | 49,030.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 123,890.00 USD |
| `1D` | `3950.90` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 346,950.00 USD | 0.00 USD | 39,720.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3955.00` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 181,840.00 USD | 0.00 USD | 28,640.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.10` | 791,940.00 USD | 0.00 USD | 791,940.00 USD | 275,140.00 USD | 0.00 USD | 14,840.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.20` | 501,960.00 USD | 0.00 USD | 501,960.00 USD | 108,590.00 USD | 0.00 USD | 48,640.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.30` | 344,730.00 USD | 0.00 USD | 344,730.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.40` | 294,650.00 USD | 0.00 USD | 294,650.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.50` | 200,050.00 USD | 0.00 USD | 200,050.00 USD | 122,810.00 USD | 0.00 USD | 10,150.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.60` | 67,090.00 USD | 0.00 USD | 67,090.00 USD | 32,920.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.70` | 19,950.00 USD | 0.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4021.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4021.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
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
| `1D` | `4106.70` | 976,080.00 USD | 976,080.00 USD | 0.00 USD | 425,080.00 USD | 0.00 USD | 48,520.00 USD |
| `7D` | `4106.90` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 106,200.00 USD |
| `1D` | `4110.80` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 263,130.00 USD | 0.00 USD | 36,190.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.90` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 252,040.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `4115.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4119.00` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 146,650.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4119.50` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4123.10` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 246,290.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.20` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `4127.90` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.40` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 136,790.00 USD | 0.00 USD | 6,600.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.50` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 96,240.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.60` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.70` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.40` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.50` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4184.60` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 128,850.00 USD | 0.00 USD | 24,960.00 USD |
| `7D` | `4186.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 62,050.00 USD |
| `1D` | `4188.70` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 186,400.00 USD | 0.00 USD | 26,010.00 USD |
| `7D` | `4190.90` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.80` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 154,770.00 USD | 0.00 USD | 18,170.00 USD |
| `7D` | `4195.10` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.90` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4199.30` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.00` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 103,730.00 USD | 0.00 USD | 4,310.00 USD |
| `7D` | `4203.50` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.10` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 83,950.00 USD | 0.00 USD | 21,020.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.20` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.30` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `4216.10` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.40` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 60,540.00 USD | 0.00 USD | 3,300.00 USD |
| `7D` | `4220.30` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.50` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 35,450.00 USD | 0.00 USD | 3,600.00 USD |
| `7D` | `4224.50` | 15,140,000.00 USD | 15,140,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.60` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.70` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4414.20` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.96 USD |
| `7D` | `4417.70` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4418.30` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.40` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4426.10` | 16,030,000.00 USD | 16,030,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4426.50` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 38,880.00 USD | 0.00 USD | 6,700.00 USD |
| `7D` | `4430.30` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4430.60` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 55,110.00 USD | 0.00 USD | 8,160.00 USD |
| `7D` | `4434.50` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `4434.70` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 33,230.00 USD | 0.00 USD | 4,980.00 USD |
| `7D` | `4438.70` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
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
  * Total Open Interest: `274.56M` | Total OI Tokens: `68,263.1 PAXG`
  * 1h OI Change: `-0.03%` | 4h OI Change: `+0.19%` | 24h OI Change: `-0.06%`
  * Exchange Breakdown: Binance=`107.26M` | Bybit=`20.05M` | OKX=`-` | Hyperliquid=`24.62M`
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
| `15M` | `PAXG` | `39.08%` | `60.92%` | `0.64` | 880,720.00 USD |
| `15M` | `Binance` | `50.16%` | `49.84%` | `1.01` | 216,110.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `42.34%` | `57.66%` | `0.73` | 136,870.00 USD |
| `15M` | `KuCoin` | `90.4%` | `9.6%` | `9.42` | 4,480.00 USD |
| `15M` | `Gate` | `48.58%` | `51.42%` | `0.94` | 78,710.00 USD |
| `15M` | `Bitget` | `17.89%` | `82.11%` | `0.22` | 186,370.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `70.06%` | `29.94%` | `2.34` | 41,650.00 USD |
| `15M` | `Bitunix` | `65.07%` | `34.93%` | `1.86` | 33,400.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `30.95%` | `69.05%` | `0.45` | 140,380.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 34,770.00 USD |
| `15M` | `HTX` | `74.14%` | `25.86%` | `2.87` | 465.86 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 7,520.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `50.16%` | `49.84%` | `1.01` | 216,110.00 USD |
| `15M` | `Global Accounts` | `39.08%` | `60.92%` | `0.64` | 880,720.00 USD |
| `1H` | `PAXG` | `56.35%` | `43.65%` | `1.29` | 3,900,000.00 USD |
| `1H` | `Binance` | `56.42%` | `43.58%` | `1.29` | 2,500,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `33.34%` | `66.66%` | `0.50` | 172,490.00 USD |
| `1H` | `KuCoin` | `50.07%` | `49.93%` | `1.00` | 281,030.00 USD |
| `1H` | `Gate` | `45%` | `55%` | `0.82` | 93,740.00 USD |
| `1H` | `Bitget` | `50.21%` | `49.79%` | `1.01` | 376,130.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `55.26%` | `44.74%` | `1.24` | 44,710.00 USD |
| `1H` | `Bitunix` | `53.08%` | `46.92%` | `1.13` | 66,160.00 USD |
| `1H` | `Hyperliquid` | `72.08%` | `27.92%` | `2.58` | 81,790.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `95.52%` | `4.48%` | `21.32` | 206,610.00 USD |
| `1H` | `HTX` | `56.67%` | `43.33%` | `1.31` | 9,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `14.33%` | `85.67%` | `0.17` | 24,220.00 USD |
| `1H` | `Aster` | `95.19%` | `4.81%` | `19.79` | 19,070.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.96%` | `39.04%` | `1.56` | 19,650.00 USD |
| `1H` | `Whale Positions` | `56.42%` | `43.58%` | `1.29` | 2,500,000.00 USD |
| `1H` | `Global Accounts` | `56.35%` | `43.65%` | `1.29` | 3,900,000.00 USD |
| `4H` | `PAXG` | `52.24%` | `47.76%` | `1.09` | 60,310,000.00 USD |
| `4H` | `Binance` | `49.7%` | `50.3%` | `0.99` | 6,380,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `47.97%` | `52.03%` | `0.92` | 5,780,000.00 USD |
| `4H` | `KuCoin` | `54.79%` | `45.21%` | `1.21` | 309,330.00 USD |
| `4H` | `Gate` | `55.94%` | `44.06%` | `1.27` | 2,700,000.00 USD |
| `4H` | `Bitget` | `53.64%` | `46.36%` | `1.16` | 2,070,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `52.57%` | `47.43%` | `1.11` | 33,580,000.00 USD |
| `4H` | `Bitunix` | `39.56%` | `60.44%` | `0.65` | 3,520,000.00 USD |
| `4H` | `Hyperliquid` | `48.54%` | `51.46%` | `0.94` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 4,870,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `76.64%` | `23.36%` | `3.28` | 1,000,000.00 USD |
| `4H` | `HTX` | `66.8%` | `33.2%` | `2.01` | 11,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.15%` | `64.85%` | `0.54` | 103,120.00 USD |
| `4H` | `Aster` | `84.87%` | `15.13%` | `5.61` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.14%` | `51.86%` | `0.93` | 0.00 USD |
| `4H` | `Whale Positions` | `49.7%` | `50.3%` | `0.99` | 6,380,000.00 USD |
| `4H` | `Global Accounts` | `52.24%` | `47.76%` | `1.09` | 60,310,000.00 USD |


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
| `5m` | -21,190.00 USD | -2,290.00 USD | **`DISTRIBUTION`** |
| `15m` | -9,830.00 USD | 48,660.00 USD | **`ACCUMULATION`** |
| `30m` | -163,900.00 USD | 146,960.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,210,000.00 USD | 253,740.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,450,000.00 USD | -214,460.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,560,000.00 USD | -84,610.00 USD | **`DISTRIBUTION`** |
| `6h` | -949,940.00 USD | 761,560.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,230,000.00 USD | 850,400.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,650,000.00 USD | 1,500,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,180,000.00 USD | 2,120,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,200,000.00 USD | -7,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,160,000.00 USD | -71,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-21.19K` | 15m=`-9.83K` | 1h=`-1.21M` | 24h=`-1.18M`
* Futures Capital Netflows: 5m=`-2.29K` | 15m=`+48.66K` | 1h=`+253.74K` | 24h=`+2.12M`
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
  * Execution Entry: `4018.30` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.95` (Risk Distance: `8.35` pts)
  * +2.5R Take Profit: `4039.17`
  * Mathematical Lot Sizing: **`1.19 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4024.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4033.14` (Risk Distance: `8.35` pts)
  * +2.5R Take Profit: `4003.92`
  * Mathematical Lot Sizing: **`1.19 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4050.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
