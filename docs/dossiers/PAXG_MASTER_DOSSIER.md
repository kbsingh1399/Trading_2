# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 10:34:49 IST` (`2026-10-30 05:04:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3998.71` | **Live Ask Quote**: `3998.79` | **Mid Price**: `3998.75`
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
  * Value Area High (VAH) = `4013.32` (Distance: `-0.38%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.22%`)
  * Value Area Low (VAL) = `3996.44` (Distance: `+0.04%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4001.19` | Low=`3996.73`
  * New York Session (13:00-21:00 UTC): High=`4022.74` | Low=`3974.76`
  * Initial Balance (First Hour): IB High=`4001.19` | IB Low=`3996.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3982.76` - `4014.74`
  * Optimal Trade Entry (OTE 0.705): `4006.75`
  * Structural Invalidation Anchor (0.786): `4030.74`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4002.20` | `4003.61` | `4002.19` | `4003.52` | `76` | 305,177.51 USD | 67,456.61 USD | `+22.10%` | -1,042,710.81 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4003.35` | `4003.79` | `4002.78` | `4002.94` | `131` | 522,606.06 USD | 368,813.96 USD | `+70.57%` | -673,896.85 USD | `+1.95` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4002.94` | `4006.91` | `4002.94` | `4005.00` | `110` | 441,464.46 USD | 172,862.63 USD | `+39.16%` | -501,034.21 USD | `+0.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4002.91` | `4005.00` | `3998.22` | `4000.31` | `196` | 783,504.25 USD | -463,603.73 USD | `-59.17%` | -883,864.39 USD | `-1.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4000.32` | `4003.79` | `3999.97` | `4002.94` | `232` | 930,315.12 USD | 460,670.59 USD | `+49.52%` | -423,193.80 USD | `+1.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4002.94` | `4006.91` | `4002.94` | `4005.01` | `110` | 440,122.78 USD | 171,865.39 USD | `+39.05%` | -251,328.41 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -446,454.31 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -9,185.48 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4006.91` | `4002.94` | `4005.01` | `110` | 439,754.32 USD | 172,169.77 USD | `+39.15%` | 162,984.29 USD | `+0.30` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4006.91` | `3995.14` | `4005.01` | `1,900` | 7,599,658.40 USD | 610,303.68 USD | `+8.03%` | 558,212.15 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4006.91` | `3995.14` | `4005.01` | `1,900` | 7,599,658.40 USD | 610,303.68 USD | `+8.03%` | 558,212.15 USD | `+0.67` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3997.50` | `16.4673` | 65,828.03 USD | 1,281,020.65 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `3997.60` | `80.5388` | 321,961.91 USD | 1,215,192.62 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `3997.70` | `3.8320` | 15,319.19 USD | 893,230.71 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3997.80` | `19.3926` | 77,527.74 USD | 877,911.53 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3997.90` | `7.2464` | 28,970.38 USD | 800,383.79 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3998.00` | `7.7379` | 30,936.12 USD | 771,413.41 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3998.10` | `2.6754` | 10,696.52 USD | 740,477.28 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3998.20` | `67.8007` | 271,080.76 USD | 729,780.77 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3998.30` | `14.3544` | 57,393.20 USD | 458,700.01 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3998.40` | `6.0237` | 24,085.16 USD | 401,306.81 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3998.50` | `11.7415` | 46,948.39 USD | 377,221.65 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3998.60` | `16.5866` | 66,323.18 USD | 330,273.26 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3998.70` | `2.6669` | 10,664.13 USD | 263,950.08 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3998.80` | `30.7036` | 122,777.56 USD | 253,285.95 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `3998.90` | `10.7350` | 42,928.19 USD | 130,508.39 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `3999.00` | `1.8729` | 7,489.73 USD | 87,580.20 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3999.10` | `5.0423` | 20,164.66 USD | 80,090.47 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3999.20` | `3.1041` | 12,413.92 USD | 59,925.81 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3999.30` | `5.7613` | 23,041.17 USD | 47,511.90 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `3999.40` | `6.1186` | 24,470.73 USD | 24,470.73 USD | `5 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3999.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,999.45` | `0.00%` | `-` |
| `ASK` | `3999.50` | `10.7988` | 43,189.80 USD | 43,189.80 USD | `7 orders` | `+0.00%` | `-` |
| `ASK` | `3999.60` | `17.0355` | 68,135.19 USD | 111,324.99 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `3999.70` | `6.4449` | 25,777.67 USD | 137,102.65 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3999.80` | `9.4890` | 37,954.10 USD | 175,056.76 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3999.90` | `33.2158` | 132,859.88 USD | 307,916.63 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4000.00` | `0.0620` | 248.00 USD | 308,164.63 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4000.10` | `60.9266` | 243,712.49 USD | 551,877.13 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4000.20` | `8.9655` | 35,863.79 USD | 587,740.92 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4000.30` | `1.6089` | 6,436.08 USD | 594,177.00 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4000.40` | `11.3706` | 45,486.95 USD | 639,663.95 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4000.50` | `5.5189` | 22,078.36 USD | 661,742.31 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4000.60` | `55.7116` | 222,879.83 USD | 884,622.14 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4000.70` | `8.8391` | 35,362.59 USD | 919,984.72 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4000.80` | `18.8002` | 75,215.84 USD | 995,200.56 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4001.00` | `21.5427` | 86,192.34 USD | 1,081,392.91 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `4001.10` | `14.4079` | 57,647.45 USD | 1,139,040.36 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4001.20` | `90.9155` | 363,771.10 USD | 1,502,811.45 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `4001.40` | `10.9526` | 43,825.73 USD | 1,546,637.19 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4001.50` | `3.3288` | 13,320.19 USD | 1,559,957.38 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `4001.60` | `4.5892` | 18,364.14 USD | 1,578,321.52 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,942,422.46 USD | `6,489.82` | `4185.46` | `3998.10` | `29725.71` | 1,220,528.56 USD | `+4.70%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,219,768.64 USD | `6,307.62` | `4129.22` | `3998.10` | `13932.67` | 825,800.38 USD | `+3.27%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,464,335.86 USD | `5,869.90` | `4228.86` | `3998.10` | `27353.07` | 1,358,686.07 USD | `+5.79%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,303,072.44 USD | `4,828.91` | `4157.43` | `3998.10` | `2277.66` | -772,809.87 USD | `-4.00%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,194,875.41 USD | `3,550.23` | `4127.87` | `3998.10` | `579.00` | -460,010.49 USD | `-3.24%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,064,355.45 USD | `3,268.21` | `4228.94` | `3998.10` | `4371.60` | 756,723.68 USD | `+5.79%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,592,460.40 USD | `2,900.00` | `4364.92` | `3998.10` | `4235.87` | 1,065,815.93 USD | `+9.19%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,794,280.00 USD | `2,200.00` | `4176.09` | `3998.10` | `2641.21` | -393,139.30 USD | `-4.47%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,794,280.00 USD | `2,200.00` | `4112.20` | `3998.10` | `4331.35` | 252,574.59 USD | `+2.87%` | `20X Cross` |
| `300` | `0xacb6...efbd` | `SHORT` | 7,896,340.44 USD | `1,975.37` | `4048.55` | `3998.10` | `6591.18` | 101,051.27 USD | `+1.28%` | `6X Cross` |
| `368` | `0xc26c...b8f4` | `LONG` | 6,315,699.33 USD | `1,579.95` | `4075.62` | `3998.10` | `0.000000` | -123,597.64 USD | `-1.96%` | `1X Cross` |
| `559` | `0x63da...8add` | `LONG` | 3,997,400.00 USD | `1,000.00` | `4021.46` | `3998.10` | `3564.32` | -24,060.96 USD | `-0.60%` | `25X Cross` |
| `573` | `0xf3dc...1672` | `LONG` | 3,934,326.84 USD | `984.27` | `4018.39` | `3998.10` | `2887.50` | -20,859.85 USD | `-0.53%` | `20X Cross` |
| `586` | `0x9aa5...58af` | `LONG` | 3,884,041.73 USD | `971.64` | `4279.98` | `3998.10` | `0.000000` | -274,567.35 USD | `-7.07%` | `20X Cross` |
| `593` | `0x354b...6425` | `LONG` | 3,852,208.12 USD | `963.46` | `4004.93` | `3998.10` | `0.000000` | -6,392.47 USD | `-0.17%` | `10X Cross` |
| `676` | `0x4a20...3c26` | `LONG` | 3,347,421.56 USD | `837.40` | `4599.73` | `3998.10` | `0.000000` | -504,398.82 USD | `-15.07%` | `20X Cross` |
| `829` | `0x0fac...7a0a` | `LONG` | 2,744,772.98 USD | `686.49` | `4290.34` | `3998.10` | `1265.96` | -200,485.73 USD | `-7.30%` | `25X Cross` |
| `912` | `0x625e...a354` | `SHORT` | 2,478,388.00 USD | `620.00` | `4122.81` | `3998.10` | `4342.45` | 77,759.03 USD | `+3.14%` | `20X Cross` |
| `916` | `0xd8c5...99b0` | `SHORT` | 2,471,811.88 USD | `618.35` | `4175.35` | `3998.10` | `34165.49` | 110,040.73 USD | `+4.45%` | `4X Cross` |
| `940` | `0xeae3...e8ad` | `SHORT` | 2,398,440.00 USD | `600.00` | `4104.77` | `3998.10` | `4325.47` | 64,425.11 USD | `+2.69%` | `20X Cross` |
| `943` | `0xf285...fa82` | `LONG` | 2,390,868.52 USD | `598.11` | `4146.45` | `3998.10` | `3891.45` | -89,151.03 USD | `-3.73%` | `25X Cross` |
| `960` | `0x12f7...8750` | `LONG` | 2,340,920.21 USD | `585.61` | `4082.77` | `3998.10` | `2655.48` | -49,996.77 USD | `-2.14%` | `10X Cross` |
| `1101` | `0x413c...886c` | `LONG` | 1,998,600.00 USD | `500.00` | `4010.43` | `3998.10` | `0.000000` | -6,616.23 USD | `-0.33%` | `2X Cross` |
| `1103` | `0x9c06...0560` | `LONG` | 1,992,373.31 USD | `498.42` | `4012.76` | `3998.10` | `0.000000` | -7,658.18 USD | `-0.38%` | `25X Cross` |
| `1106` | `0x61ce...a62b` | `SHORT` | 1,988,620.99 USD | `497.50` | `4071.66` | `3998.10` | `4719.14` | 37,047.80 USD | `+1.86%` | `20X Cross` |
| `1182` | `0x2edd...8179` | `LONG` | 1,880,926.42 USD | `469.89` | `4164.68` | `4003.62` | `0.000000` | -76,006.10 USD | `-4.04%` | `10X Cross` |
| `1221` | `0xead5...69f2` | `LONG` | 1,813,955.76 USD | `453.78` | `4220.88` | `3998.10` | `3539.15` | -101,412.30 USD | `-5.59%` | `5X Isolated` |
| `1284` | `0x7a6d...f79c` | `SHORT` | 1,714,769.01 USD | `428.38` | `4136.09` | `4003.62` | `5383.40` | 57,046.00 USD | `+3.33%` | `10X Cross` |
| `1292` | `0x46fc...1195` | `LONG` | 1,690,479.24 USD | `422.80` | `4053.27` | `3998.10` | `2154.21` | -23,242.28 USD | `-1.37%` | `20X Cross` |
| `1360` | `0x6d15...d374` | `LONG` | 1,598,960.00 USD | `400.00` | `4068.25` | `3998.10` | `3842.02` | -28,340.00 USD | `-1.77%` | `25X Cross` |
| `1361` | `0xee02...309d` | `SHORT` | 1,598,960.00 USD | `400.00` | `4438.84` | `3998.10` | `4227.09` | 176,578.60 USD | `+11.04%` | `25X Isolated` |
| `1402` | `0x51f6...2b39` | `LONG` | 1,562,631.11 USD | `390.33` | `4228.91` | `4003.62` | `550.94` | -88,021.98 USD | `-5.63%` | `10X Cross` |
| `1406` | `0x02a7...fe9f` | `SHORT` | 1,558,986.00 USD | `390.00` | `4055.02` | `3998.10` | `4306.91` | 22,473.25 USD | `+1.44%` | `25X Cross` |
| `1444` | `0x7e77...b8d2` | `SHORT` | 1,519,012.00 USD | `380.00` | `4131.92` | `3998.10` | `4293.71` | 51,117.64 USD | `+3.37%` | `20X Cross` |
| `1464` | `0x72c2...9b37` | `LONG` | 1,491,480.43 USD | `373.13` | `4000.98` | `3998.10` | `3778.25` | -1,413.08 USD | `-0.09%` | `13X Isolated` |
| `1504` | `0x781e...96b7` | `SHORT` | 1,445,741.80 USD | `361.11` | `4363.51` | `4003.62` | `13073.53` | 129,964.84 USD | `+8.99%` | `10X Cross` |
| `1513` | `0xaa44...b844` | `LONG` | 1,438,992.00 USD | `360.00` | `4043.10` | `3998.10` | `2818.36` | -16,525.63 USD | `-1.15%` | `4X Cross` |
| `1624` | `0xa41f...d50a` | `LONG` | 1,314,993.10 USD | `328.96` | `4468.89` | `3998.10` | `3802.38` | -155,104.75 USD | `-11.80%` | `15X Cross` |
| `1636` | `0x7fda...17d1` | `SHORT` | 1,301,952.43 USD | `325.63` | `4013.13` | `3998.10` | `30626.29` | 4,829.45 USD | `+0.37%` | `20X Cross` |
| `1669` | `0xbf5a...88ba` | `SHORT` | 1,269,793.70 USD | `317.65` | `4091.80` | `3998.10` | `9824.94` | 29,989.34 USD | `+2.36%` | `20X Cross` |
| `1704` | `0xff31...ff6c` | `SHORT` | 1,239,194.00 USD | `310.00` | `4372.43` | `3998.10` | `4789.38` | 116,261.38 USD | `+9.38%` | `10X Isolated` |
| `1733` | `0xada6...6f88` | `LONG` | 1,213,141.41 USD | `303.50` | `4166.46` | `3998.10` | `1785.28` | -51,371.46 USD | `-4.23%` | `5X Cross` |
| `1891` | `0x50e2...d770` | `LONG` | 1,080,766.64 USD | `270.37` | `4243.58` | `3998.10` | `2562.31` | -66,559.82 USD | `-6.16%` | `20X Cross` |
| `1910` | `0x4c92...4f17` | `SHORT` | 1,066,188.53 USD | `266.72` | `4260.98` | `3998.10` | `6514.49` | 70,303.71 USD | `+6.59%` | `20X Cross` |
| `1985` | `0xd346...c4f3` | `LONG` | 1,020,031.75 USD | `255.17` | `4188.66` | `3998.10` | `3310.63` | -48,804.76 USD | `-4.78%` | `5X Isolated` |

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
| `7D` | `Long Liquidation` | `3596.10` | 16,700,000.00 USD | 16,700,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.60` | 4,830,000.00 USD | 4,830,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,670,000.00 USD | 16,670,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.70` | 4,820,000.00 USD | 4,820,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 16,500,000.00 USD | 16,500,000.00 USD | 198,750.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.80` | 4,760,000.00 USD | 4,760,000.00 USD | 46,250.00 USD | 0.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 16,230,000.00 USD | 16,230,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.90` | 4,700,000.00 USD | 4,700,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 16,040,000.00 USD | 16,040,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.00` | 4,680,000.00 USD | 4,680,000.00 USD | 37,500.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,940,000.00 USD | 15,940,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.10` | 4,640,000.00 USD | 4,640,000.00 USD | 41,050.00 USD | 0.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,820,000.00 USD | 15,820,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.20` | 4,590,000.00 USD | 4,590,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,740,000.00 USD | 15,740,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.30` | 4,510,000.00 USD | 4,510,000.00 USD | 40,050.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,660,000.00 USD | 15,660,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 4,460,000.00 USD | 4,460,000.00 USD | 29,160.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 15,540,000.00 USD | 15,540,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.50` | 4,420,000.00 USD | 4,420,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 15,450,000.00 USD | 15,450,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.60` | 4,410,000.00 USD | 4,410,000.00 USD | 7,770.00 USD | 0.00 USD | 473.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 15,390,000.00 USD | 15,390,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.70` | 4,400,000.00 USD | 4,400,000.00 USD | 3,000.00 USD | 0.00 USD | 426.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 15,340,000.00 USD | 15,340,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 15,310,000.00 USD | 15,310,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 15,280,000.00 USD | 15,280,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 15,230,000.00 USD | 15,230,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 15,220,000.00 USD | 15,220,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 15,210,000.00 USD | 15,210,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 15,190,000.00 USD | 15,190,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.50` | 4,400,000.00 USD | 4,400,000.00 USD | 63,550.00 USD | 0.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,990,000.00 USD | 14,990,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.60` | 4,290,000.00 USD | 4,290,000.00 USD | 150,990.00 USD | 0.00 USD | 88,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 14,330,000.00 USD | 14,330,000.00 USD | 518,350.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.70` | 4,050,000.00 USD | 4,050,000.00 USD | 38,210.00 USD | 0.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,640,000.00 USD | 13,640,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.80` | 3,990,000.00 USD | 3,990,000.00 USD | 91,670.00 USD | 0.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 13,100,000.00 USD | 13,100,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.90` | 3,880,000.00 USD | 3,880,000.00 USD | 90,850.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,800,000.00 USD | 12,800,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.00` | 3,770,000.00 USD | 3,770,000.00 USD | 159,360.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 12,390,000.00 USD | 12,390,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.10` | 3,580,000.00 USD | 3,580,000.00 USD | 227,140.00 USD | 0.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 12,140,000.00 USD | 12,140,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.20` | 3,320,000.00 USD | 3,320,000.00 USD | 147,850.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,860,000.00 USD | 11,860,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.30` | 3,150,000.00 USD | 3,150,000.00 USD | 116,040.00 USD | 0.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,540,000.00 USD | 11,540,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.40` | 3,020,000.00 USD | 3,020,000.00 USD | 48,550.00 USD | 0.00 USD | 4,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 11,150,000.00 USD | 11,150,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.50` | 2,970,000.00 USD | 2,970,000.00 USD | 20,230.00 USD | 0.00 USD | 817.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,830,000.00 USD | 10,830,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.60` | 2,950,000.00 USD | 2,950,000.00 USD | 13,610.00 USD | 0.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,680,000.00 USD | 10,680,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,570,000.00 USD | 10,570,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,440,000.00 USD | 10,440,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 10,330,000.00 USD | 10,330,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 10,240,000.00 USD | 10,240,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 10,170,000.00 USD | 10,170,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.40` | 2,930,000.00 USD | 2,930,000.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 10,120,000.00 USD | 10,120,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.50` | 2,880,000.00 USD | 2,880,000.00 USD | 173,860.00 USD | 0.00 USD | 197,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 9,220,000.00 USD | 9,220,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.60` | 2,510,000.00 USD | 2,510,000.00 USD | 252,720.00 USD | 0.00 USD | 102,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,820,000.00 USD | 7,820,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.70` | 2,150,000.00 USD | 2,150,000.00 USD | 75,170.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,460,000.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.80` | 2,050,000.00 USD | 2,050,000.00 USD | 202,630.00 USD | 0.00 USD | 52,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,710,000.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.90` | 1,800,000.00 USD | 1,800,000.00 USD | 235,360.00 USD | 0.00 USD | 20,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,800,000.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.00` | 1,540,000.00 USD | 1,540,000.00 USD | 322,690.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,410,000.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.10` | 1,150,000.00 USD | 1,150,000.00 USD | 394,220.00 USD | 0.00 USD | 58,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,860,000.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.20` | 700,710.00 USD | 700,710.00 USD | 307,490.00 USD | 0.00 USD | 36,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 3,200,000.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.30` | 356,780.00 USD | 356,780.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,580,000.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.40` | 151,840.00 USD | 151,840.00 USD | 92,090.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,820,000.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.50` | 57,290.00 USD | 57,290.00 USD | 33,020.00 USD | 0.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.60` | 21,300.00 USD | 21,300.00 USD | 18,860.00 USD | 0.00 USD | 2,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.30` | 52,560.00 USD | 52,560.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.40` | 379,810.00 USD | 379,810.00 USD | 173,860.00 USD | 0.00 USD | 153,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 945,330.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.50` | 779,930.00 USD | 779,930.00 USD | 252,720.00 USD | 0.00 USD | 147,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.60` | 846,280.00 USD | 846,280.00 USD | 40,700.00 USD | 0.00 USD | 25,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.70` | 1,120,000.00 USD | 1,120,000.00 USD | 230,830.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,800,000.00 USD | 4,800,000.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.80` | 1,320,000.00 USD | 1,320,000.00 USD | 176,660.00 USD | 0.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,550,000.00 USD | 5,550,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.90` | 1,670,000.00 USD | 1,670,000.00 USD | 281,430.00 USD | 0.00 USD | 61,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 6,040,000.00 USD | 6,040,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.00` | 2,160,000.00 USD | 2,160,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,640,000.00 USD | 6,640,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.10` | 2,490,000.00 USD | 2,490,000.00 USD | 288,670.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,110,000.00 USD | 7,110,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.20` | 2,740,000.00 USD | 2,740,000.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,730,000.00 USD | 7,730,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.30` | 2,860,000.00 USD | 2,860,000.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,530,000.00 USD | 8,530,000.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.40` | 2,900,000.00 USD | 2,900,000.00 USD | 35,750.00 USD | 0.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,960,000.00 USD | 8,960,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.50` | 2,930,000.00 USD | 2,930,000.00 USD | 31,940.00 USD | 0.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 9,140,000.00 USD | 9,140,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.60` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 538.62 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,380,000.00 USD | 9,380,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,620,000.00 USD | 9,620,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,900,000.00 USD | 9,900,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,960,000.00 USD | 9,960,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 10,090,000.00 USD | 10,090,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 10,160,000.00 USD | 10,160,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,630,000.00 USD | 10,630,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.30` | 3,010,000.00 USD | 3,010,000.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,380,000.00 USD | 11,380,000.00 USD | 572,470.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.40` | 3,250,000.00 USD | 3,250,000.00 USD | 154,860.00 USD | 0.00 USD | 85,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,970,000.00 USD | 11,970,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.50` | 3,340,000.00 USD | 3,340,000.00 USD | 53,170.00 USD | 0.00 USD | 31,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,340,000.00 USD | 12,340,000.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4172.60` | 3,410,000.00 USD | 3,410,000.00 USD | 56,270.00 USD | 0.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,800,000.00 USD | 12,800,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.70` | 3,540,000.00 USD | 3,540,000.00 USD | 106,840.00 USD | 0.00 USD | 24,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.80` | 3,650,000.00 USD | 3,650,000.00 USD | 99,350.00 USD | 0.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,990,000.00 USD | 12,990,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.90` | 3,830,000.00 USD | 3,830,000.00 USD | 150,530.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 13,210,000.00 USD | 13,210,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.00` | 4,070,000.00 USD | 4,070,000.00 USD | 210,710.00 USD | 0.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,500,000.00 USD | 13,500,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.10` | 4,220,000.00 USD | 4,220,000.00 USD | 131,880.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,790,000.00 USD | 13,790,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.20` | 4,320,000.00 USD | 4,320,000.00 USD | 87,740.00 USD | 0.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 14,120,000.00 USD | 14,120,000.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.30` | 4,370,000.00 USD | 4,370,000.00 USD | 40,760.00 USD | 0.00 USD | 1,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 14,420,000.00 USD | 14,420,000.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.40` | 4,390,000.00 USD | 4,390,000.00 USD | 21,790.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,640,000.00 USD | 14,640,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.50` | 4,400,000.00 USD | 4,400,000.00 USD | 9,430.00 USD | 0.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,720,000.00 USD | 14,720,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,840,000.00 USD | 14,840,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,960,000.00 USD | 14,960,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 15,080,000.00 USD | 15,080,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 15,110,000.00 USD | 15,110,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 15,180,000.00 USD | 15,180,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 15,200,000.00 USD | 15,200,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 15,260,000.00 USD | 15,260,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.10` | 4,410,000.00 USD | 4,410,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 15,390,000.00 USD | 15,390,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4402.20` | 4,450,000.00 USD | 4,450,000.00 USD | 14,970.00 USD | 0.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,610,000.00 USD | 15,610,000.00 USD | 164,460.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4406.30` | 4,510,000.00 USD | 4,510,000.00 USD | 43,610.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4408.20` | 4,520,000.00 USD | 4,520,000.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,790,000.00 USD | 15,790,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,880,000.00 USD | 15,880,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,980,000.00 USD | 15,980,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 16,070,000.00 USD | 16,070,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 16,140,000.00 USD | 16,140,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,200,000.00 USD | 16,200,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 16,270,000.00 USD | 16,270,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 16,360,000.00 USD | 16,360,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 16,410,000.00 USD | 16,410,000.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.10` | 16,700,000.00 USD | 0.00 USD | 16,700,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3598.60` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.40` | 16,670,000.00 USD | 0.00 USD | 16,670,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3602.70` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 23,510.00 USD | 0.00 USD | 35,830.00 USD |
| `7D` | `3604.70` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 198,750.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.80` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 46,250.00 USD | 0.00 USD | 11,510.00 USD |
| `7D` | `3609.00` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 19,350.00 USD | 0.00 USD | 2,940.00 USD |
| `7D` | `3613.30` | 16,040,000.00 USD | 0.00 USD | 16,040,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3615.00` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 37,500.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `3617.60` | 15,940,000.00 USD | 0.00 USD | 15,940,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3619.10` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 41,050.00 USD | 0.00 USD | 7,170.00 USD |
| `7D` | `3621.90` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3623.20` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 69,680.00 USD | 0.00 USD | 11,750.00 USD |
| `7D` | `3626.20` | 15,740,000.00 USD | 0.00 USD | 15,740,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.30` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 40,050.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `3630.50` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.40` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 29,160.00 USD | 0.00 USD | 5,770.00 USD |
| `7D` | `3634.80` | 15,540,000.00 USD | 0.00 USD | 15,540,000.00 USD | 90,370.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.50` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.10` | 15,450,000.00 USD | 0.00 USD | 15,450,000.00 USD | 48,670.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3639.60` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 7,770.00 USD | 0.00 USD | 473.15 USD |
| `7D` | `3643.40` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `3643.70` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 3,000.00 USD | 0.00 USD | 426.17 USD |
| `7D` | `3647.70` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `3840.50` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 63,550.00 USD | 0.00 USD | 49,950.00 USD |
| `7D` | `3841.20` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3844.60` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 150,990.00 USD | 0.00 USD | 88,140.00 USD |
| `7D` | `3845.50` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 518,350.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3848.70` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 38,210.00 USD | 0.00 USD | 17,960.00 USD |
| `7D` | `3849.80` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3852.80` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 91,670.00 USD | 0.00 USD | 20,560.00 USD |
| `7D` | `3854.10` | 13,100,000.00 USD | 0.00 USD | 13,100,000.00 USD | 249,250.00 USD | 0.00 USD | 55,150.00 USD |
| `1D` | `3856.90` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 90,850.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `3858.40` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3861.00` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 159,360.00 USD | 0.00 USD | 34,910.00 USD |
| `7D` | `3862.70` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3865.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 227,140.00 USD | 0.00 USD | 29,260.00 USD |
| `7D` | `3867.00` | 12,140,000.00 USD | 0.00 USD | 12,140,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3869.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 147,850.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `3871.30` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3873.30` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 116,040.00 USD | 0.00 USD | 16,210.00 USD |
| `7D` | `3875.60` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 353,500.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3877.40` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 48,550.00 USD | 0.00 USD | 4,010.00 USD |
| `7D` | `3879.90` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 294,740.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3881.50` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 20,230.00 USD | 0.00 USD | 817.23 USD |
| `7D` | `3884.20` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3885.60` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 13,610.00 USD | 0.00 USD | 1,890.00 USD |
| `7D` | `3888.50` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `1D` | `3918.40` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3918.60` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3922.50` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 173,860.00 USD | 0.00 USD | 197,850.00 USD |
| `7D` | `3922.90` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3926.60` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 252,720.00 USD | 0.00 USD | 102,940.00 USD |
| `7D` | `3927.20` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3930.70` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 75,170.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `3931.50` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 605,700.00 USD | 0.00 USD | 145,660.00 USD |
| `1D` | `3934.80` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 202,630.00 USD | 0.00 USD | 52,410.00 USD |
| `7D` | `3935.80` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3938.90` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 235,360.00 USD | 0.00 USD | 20,510.00 USD |
| `7D` | `3940.10` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3943.00` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 322,690.00 USD | 0.00 USD | 64,870.00 USD |
| `7D` | `3944.40` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3947.10` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 394,220.00 USD | 0.00 USD | 58,690.00 USD |
| `7D` | `3948.70` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3951.20` | 700,710.00 USD | 0.00 USD | 700,710.00 USD | 307,490.00 USD | 0.00 USD | 36,430.00 USD |
| `7D` | `3953.00` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3955.30` | 356,780.00 USD | 0.00 USD | 356,780.00 USD | 175,480.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3957.30` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 708,880.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3959.40` | 151,840.00 USD | 0.00 USD | 151,840.00 USD | 92,090.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3961.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 435,840.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.50` | 57,290.00 USD | 0.00 USD | 57,290.00 USD | 33,020.00 USD | 0.00 USD | 2,970.00 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `1D` | `3967.60` | 21,300.00 USD | 0.00 USD | 21,300.00 USD | 18,860.00 USD | 0.00 USD | 2,440.00 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4002.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4003.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4078.30` | 52,560.00 USD | 52,560.00 USD | 0.00 USD | 52,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4082.40` | 379,810.00 USD | 379,810.00 USD | 0.00 USD | 173,860.00 USD | 0.00 USD | 153,400.00 USD |
| `7D` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 945,330.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4086.50` | 779,930.00 USD | 779,930.00 USD | 0.00 USD | 252,720.00 USD | 0.00 USD | 147,390.00 USD |
| `1D` | `4090.60` | 846,280.00 USD | 846,280.00 USD | 0.00 USD | 40,700.00 USD | 0.00 USD | 25,650.00 USD |
| `7D` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4094.70` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 230,830.00 USD | 0.00 USD | 44,470.00 USD |
| `7D` | `4094.90` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 105,350.00 USD |
| `1D` | `4098.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 176,660.00 USD | 0.00 USD | 26,080.00 USD |
| `7D` | `4099.20` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4102.90` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 281,430.00 USD | 0.00 USD | 61,690.00 USD |
| `7D` | `4103.50` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4107.00` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `4107.80` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4111.10` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 288,670.00 USD | 0.00 USD | 39,930.00 USD |
| `7D` | `4112.10` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4115.20` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 219,460.00 USD | 0.00 USD | 32,410.00 USD |
| `7D` | `4116.40` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4119.30` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 109,720.00 USD | 0.00 USD | 7,700.00 USD |
| `7D` | `4120.70` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 765,010.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4123.40` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 35,750.00 USD | 0.00 USD | 1,960.00 USD |
| `7D` | `4125.00` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `4127.50` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 31,940.00 USD | 0.00 USD | 3,240.00 USD |
| `7D` | `4129.30` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `1D` | `4131.60` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 538.62 USD |
| `7D` | `4133.60` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.30` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 44,720.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `4163.70` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 572,470.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4164.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 154,860.00 USD | 0.00 USD | 85,280.00 USD |
| `7D` | `4168.00` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.50` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 53,170.00 USD | 0.00 USD | 31,320.00 USD |
| `7D` | `4172.30` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 70,920.00 USD |
| `1D` | `4172.60` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 56,270.00 USD | 0.00 USD | 14,480.00 USD |
| `7D` | `4176.60` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4176.70` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 106,840.00 USD | 0.00 USD | 24,450.00 USD |
| `1D` | `4180.80` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 99,350.00 USD | 0.00 USD | 12,590.00 USD |
| `7D` | `4180.90` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4184.90` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 150,530.00 USD | 0.00 USD | 30,600.00 USD |
| `7D` | `4185.20` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4189.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 210,710.00 USD | 0.00 USD | 27,480.00 USD |
| `7D` | `4189.50` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4193.10` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 131,880.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4193.80` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4197.20` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 87,740.00 USD | 0.00 USD | 14,730.00 USD |
| `7D` | `4198.10` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 299,100.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4201.30` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 40,760.00 USD | 0.00 USD | 1,230.00 USD |
| `7D` | `4202.40` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 281,480.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4205.40` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 21,790.00 USD | 0.00 USD | 1,070.00 USD |
| `7D` | `4206.70` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `1D` | `4209.50` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 9,430.00 USD | 0.00 USD | 1,630.00 USD |
| `7D` | `4211.00` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `7D` | `4215.30` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4398.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4400.20` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4402.20` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 14,970.00 USD | 0.00 USD | 24,530.00 USD |
| `7D` | `4404.50` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 164,460.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4406.30` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 43,610.00 USD | 0.00 USD | 22,800.00 USD |
| `1D` | `4408.20` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 11,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4408.80` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `7D` | `4413.10` | 15,880,000.00 USD | 15,880,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `7D` | `4417.40` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `7D` | `4421.70` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4426.00` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.30` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.60` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.90` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4440.70` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 1,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `276.27M` | Total OI Tokens: `68,998.7 PAXG`
  * 1h OI Change: `+0.33%` | 4h OI Change: `+0.64%` | 24h OI Change: `+0.84%`
  * Exchange Breakdown: Binance=`107.27M` | Bybit=`22.05M` | OKX=`-` | Hyperliquid=`24.71M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-2.19K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `43.30%` | `56.70%` | `0.76` | 5,510,000.00 USD |
| `15M` | `Binance` | `39.85%` | `60.15%` | `0.66` | 433,850.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `51.72%` | `48.28%` | `1.07` | 149,150.00 USD |
| `15M` | `KuCoin` | `45.34%` | `54.66%` | `0.83` | 10,160.00 USD |
| `15M` | `Gate` | `42.29%` | `57.71%` | `0.73` | 118,520.00 USD |
| `15M` | `Bitget` | `49.87%` | `50.13%` | `0.99` | 114,600.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `50%` | `50%` | `1.00` | 4,350,000.00 USD |
| `15M` | `Bitunix` | `39.26%` | `60.74%` | `0.65` | 181,980.00 USD |
| `15M` | `Hyperliquid` | `98.25%` | `1.75%` | `56.14` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 74,030.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `31.17%` | `68.83%` | `0.45` | 78,740.00 USD |
| `15M` | `HTX` | `83.4%` | `16.6%` | `5.02` | 2,210.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `40.97%` | `59.03%` | `0.69` | 0.00 USD |
| `15M` | `Whale Positions` | `39.85%` | `60.15%` | `0.66` | 433,850.00 USD |
| `15M` | `Global Accounts` | `43.30%` | `56.70%` | `0.76` | 5,510,000.00 USD |
| `1H` | `PAXG` | `47.28%` | `52.72%` | `0.90` | 14,070,000.00 USD |
| `1H` | `Binance` | `50.72%` | `49.28%` | `1.03` | 6,100,000.00 USD |
| `1H` | `OKX` | `42.53%` | `57.47%` | `0.74` | 2,610,000.00 USD |
| `1H` | `Bybit` | `51.74%` | `48.26%` | `1.07` | 1,360,000.00 USD |
| `1H` | `KuCoin` | `53.56%` | `46.44%` | `1.15` | 105,280.00 USD |
| `1H` | `Gate` | `73.07%` | `26.93%` | `2.71` | 279,030.00 USD |
| `1H` | `Bitget` | `46.24%` | `53.76%` | `0.86` | 780,480.00 USD |
| `1H` | `BingX` | `43.06%` | `56.94%` | `0.76` | 517,510.00 USD |
| `1H` | `MEXC` | `30.82%` | `69.18%` | `0.45` | 1,190,000.00 USD |
| `1H` | `Bitunix` | `45.38%` | `54.62%` | `0.83` | 237,240.00 USD |
| `1H` | `Hyperliquid` | `34.31%` | `65.69%` | `0.52` | 274,610.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.63%` | `50.37%` | `0.99` | 486,750.00 USD |
| `1H` | `Crypto.com` | `46.66%` | `53.34%` | `0.87` | 6,120.00 USD |
| `1H` | `WhiteBIT` | `67.83%` | `32.17%` | `2.11` | 108,300.00 USD |
| `1H` | `HTX` | `46.33%` | `53.67%` | `0.86` | 1,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `74.9%` | `25.1%` | `2.98` | 7,610.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `74.45%` | `25.55%` | `2.91` | 18,760.00 USD |
| `1H` | `Whale Positions` | `50.72%` | `49.28%` | `1.03` | 6,100,000.00 USD |
| `1H` | `Global Accounts` | `47.28%` | `52.72%` | `0.90` | 14,070,000.00 USD |
| `4H` | `PAXG` | `40.47%` | `59.53%` | `0.68` | 56,330,000.00 USD |
| `4H` | `Binance` | `48.56%` | `51.44%` | `0.94` | 9,390,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `43.8%` | `56.2%` | `0.78` | 5,660,000.00 USD |
| `4H` | `KuCoin` | `56.01%` | `43.99%` | `1.27` | 327,160.00 USD |
| `4H` | `Gate` | `45.92%` | `54.08%` | `0.85` | 2,180,000.00 USD |
| `4H` | `Bitget` | `46.02%` | `53.98%` | `0.85` | 3,520,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `34.6%` | `65.4%` | `0.53` | 27,930,000.00 USD |
| `4H` | `Bitunix` | `45.64%` | `54.36%` | `0.84` | 1,560,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.08%` | `46.92%` | `1.13` | 3,960,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `20.11%` | `79.89%` | `0.25` | 1,550,000.00 USD |
| `4H` | `HTX` | `84.18%` | `15.82%` | `5.32` | 169,160.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `25.84%` | `74.16%` | `0.35` | 68,020.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `48.56%` | `51.44%` | `0.94` | 9,390,000.00 USD |
| `4H` | `Global Accounts` | `40.47%` | `59.53%` | `0.68` | 56,330,000.00 USD |


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
| `5m` | 41,490.00 USD | -25,320.00 USD | **`ACCUMULATION`** |
| `15m` | 17,810.00 USD | -330,680.00 USD | **`DISTRIBUTION`** |
| `30m` | 73,300.00 USD | -182,210.00 USD | **`DISTRIBUTION`** |
| `1h` | -79,510.00 USD | -278,490.00 USD | **`DISTRIBUTION`** |
| `2h` | -58,930.00 USD | -271,660.00 USD | **`DISTRIBUTION`** |
| `4h` | -271,510.00 USD | -726,230.00 USD | **`DISTRIBUTION`** |
| `6h` | 15,110.00 USD | -1,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,070,000.00 USD | -1,310,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,650,000.00 USD | -802,250.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,180,000.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,360,000.00 USD | -9,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,990,000.00 USD | -72,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+41.49K` | 15m=`+17.81K` | 1h=`-79.51K` | 24h=`-1.18M`
* Futures Capital Netflows: 5m=`-25.32K` | 15m=`-330.68K` | 1h=`-278.49K` | 24h=`-1.07M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4013.32` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.50` (Risk Distance: `9.18` pts)
  * +2.5R Take Profit: `3990.36`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4030.74`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
