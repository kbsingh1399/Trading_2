# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 11:26:19 IST` (`2026-10-30 05:56:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3998.50` | **Live Ask Quote**: `3998.58` | **Mid Price**: `3998.54`
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
  * Session VWAP: `4003.04` | VWAP Z-Score: `-0.15` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.64` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `49.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4020.58` | Lower -3.00σ Band: `3985.50`
  * Upper +2.51σ Band: `4017.71` | Lower -2.51σ Band: `3988.37`
  * Upper +2.01σ Band: `4014.79` | Lower -2.01σ Band: `3991.29`
  * Upper +2.00σ Band: `4014.73` | Lower -2.00σ Band: `3991.35`
  * Upper +1.28σ Band: `4010.52` | Lower -1.28σ Band: `3995.56`
  * Upper +1.00σ Band: `4008.89` | Lower -1.00σ Band: `3997.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3999.29` | EMA-20=`4001.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4008.83` (Slope: `+0.0000`) | EMA-100=`4017.52`
  * Institutional Anchors: EMA-144=`4021.83` | EMA-200=`4024.50` (Slope: `-0.0876`) | EMA-233=`4026.54`
- **Range Boundaries**: 24H High=`4046.38` | 24H Low=`3987.44` | Weekly High=`4082.75` | Weekly Low=`3987.44`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4012.77` (Distance: `-0.37%`)
  * Point of Control (POC) = `4006.95` (Distance: `-0.23%`)
  * Value Area Low (VAL) = `3996.99` (Distance: `+0.02%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4050.33` | Weekly POC=`4014.77` | Weekly VAL=`4003.61`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3996.58`
  * New York Session (13:00-21:00 UTC): High=`4022.53` | Low=`3974.55`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3996.58`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3982.55` - `4014.53`
  * Optimal Trade Entry (OTE 0.705): `4006.54`
  * Structural Invalidation Anchor (0.786): `4030.53`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4013.80` | `4017.75` | `4011.82` | `4012.04` | `115` | 462,669.51 USD | 733.60 USD | `+0.16%` | 72,221.16 USD | `-0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4012.05` | `4014.05` | `4010.55` | `4010.85` | `27` | 108,971.39 USD | -5,429.51 USD | `-4.98%` | 66,791.64 USD | `-0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `4010.81` | `4012.08` | `4009.35` | `4010.71` | `28` | 111,537.15 USD | -11,622.25 USD | `-10.42%` | 55,169.40 USD | `-0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4002.94` | `4009.65` | `4002.94` | `4007.11` | `318` | 1,272,733.92 USD | 529,845.01 USD | `+41.63%` | 314,069.01 USD | `+1.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4007.11` | `4014.29` | `4006.74` | `4013.79` | `199` | 799,958.77 USD | -242,581.45 USD | `-30.32%` | 71,487.55 USD | `-0.82` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4013.80` | `4017.75` | `4009.35` | `4010.71` | `170` | 683,178.05 USD | -16,318.16 USD | `-2.39%` | 55,169.40 USD | `-0.06` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4006.40` | `3997.60` | `4000.51` | `1,181` | 4,723,785.37 USD | -221,801.65 USD | `-4.70%` | -446,454.31 USD | `-0.50` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4000.52` | `4005.00` | `3995.14` | `4002.94` | `1,790` | 7,158,366.15 USD | 437,268.83 USD | `+6.11%` | -9,185.48 USD | `+0.91` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4002.94` | `4017.75` | `4002.94` | `4010.71` | `687` | 2,755,870.74 USD | 270,945.40 USD | `+9.83%` | 261,759.92 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `4010.71` | `2,478` | 9,917,485.57 USD | 711,462.91 USD | `+7.17%` | 659,371.37 USD | `+0.77` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 179,736.73 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,272,553.27 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,290,409.62 USD | `-0.60` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | -52,091.54 USD | `-1.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3995.14` | `4004.60` | `2,539` | 10,161,402.81 USD | 678,749.29 USD | `+6.68%` | 626,657.75 USD | `+0.74` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `BID` | `3997.70` | `3.1071` | 12,421.25 USD | 772,011.36 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `3997.80` | `13.3038` | 53,185.93 USD | 759,590.11 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `3997.90` | `56.9072` | 227,509.29 USD | 706,404.18 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3998.00` | `5.3119` | 21,236.98 USD | 478,894.88 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3998.10` | `0.4984` | 1,992.65 USD | 457,657.91 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3998.20` | `6.2855` | 25,130.69 USD | 455,665.25 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3998.30` | `7.9471` | 31,774.89 USD | 430,534.57 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3998.40` | `7.1955` | 28,770.49 USD | 398,759.68 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3998.50` | `31.6949` | 126,732.06 USD | 369,989.19 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3998.60` | `11.2023` | 44,793.52 USD | 243,257.13 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3998.70` | `21.1568` | 84,599.70 USD | 198,463.61 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3998.80` | `0.0255` | 101.97 USD | 113,863.92 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3998.90` | `3.7510` | 14,999.87 USD | 113,761.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3999.00` | `5.2499` | 20,994.35 USD | 98,762.08 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3999.10` | `9.0007` | 35,994.70 USD | 77,767.73 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3999.20` | `2.5676` | 10,268.35 USD | 41,773.03 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3999.30` | `3.0604` | 12,239.46 USD | 31,504.68 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3999.40` | `3.8997` | 15,596.46 USD | 19,265.22 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3999.50` | `0.0761` | 304.36 USD | 3,668.76 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4000.00` | `0.8411` | 3,364.40 USD | 3,364.40 USD | `5 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4000.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,000.05` | `0.00%` | `-` |
| `ASK` | `4000.10` | `105.3039` | 421,226.13 USD | 421,226.13 USD | `19 orders` | `+0.00%` | `-` |
| `ASK` | `4000.20` | `16.7720` | 67,091.35 USD | 488,317.48 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `4000.30` | `55.3083` | 221,249.79 USD | 709,567.28 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4000.40` | `12.9614` | 51,850.78 USD | 761,418.06 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `4000.60` | `35.5110` | 142,065.31 USD | 903,483.37 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `4000.70` | `17.7350` | 70,952.41 USD | 974,435.78 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4000.80` | `5.0270` | 20,112.02 USD | 994,547.80 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `4000.90` | `93.4882` | 374,036.94 USD | 1,368,584.74 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4001.00` | `4.2468` | 16,991.45 USD | 1,385,576.19 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4001.10` | `3.2317` | 12,930.35 USD | 1,398,506.55 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4001.20` | `13.1759` | 52,719.41 USD | 1,451,225.96 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `4001.30` | `10.2486` | 41,007.72 USD | 1,492,233.68 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `4001.40` | `0.4686` | 1,875.06 USD | 1,494,108.74 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4001.50` | `5.8213` | 23,293.93 USD | 1,517,402.67 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4001.60` | `6.4986` | 26,004.80 USD | 1,543,407.47 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4001.70` | `5.1057` | 20,431.48 USD | 1,563,838.95 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4001.80` | `9.4820` | 37,945.07 USD | 1,601,784.01 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4001.90` | `66.7405` | 267,088.81 USD | 1,868,872.82 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `4002.00` | `4.7112` | 18,854.22 USD | 1,887,727.04 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4002.10` | `22.0571` | 88,274.72 USD | 1,976,001.76 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,943,720.42 USD | `6,489.82` | `4185.46` | `3997.00` | `29557.32` | 1,219,230.59 USD | `+4.70%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,250,211.58 USD | `6,316.34` | `4128.90` | `3997.00` | `14001.33` | 829,345.13 USD | `+3.28%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,463,161.88 USD | `5,869.90` | `4228.86` | `3997.00` | `27231.12` | 1,359,860.05 USD | `+5.80%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,303,072.44 USD | `4,828.91` | `4157.43` | `3997.00` | `2281.47` | -772,809.87 USD | `-4.00%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,197,369.10 USD | `3,551.74` | `4127.81` | `3997.00` | `616.68` | -463,567.90 USD | `-3.27%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,064,028.62 USD | `3,268.21` | `4228.94` | `3997.00` | `4375.71` | 757,050.51 USD | `+5.79%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,592,170.40 USD | `2,900.00` | `4364.92` | `3997.00` | `4235.92` | 1,066,105.93 USD | `+9.20%` | `20X Cross` |
| `260` | `0x41e5...0825` | `SHORT` | 8,794,280.00 USD | `2,200.00` | `4112.20` | `3997.00` | `4331.40` | 252,574.59 USD | `+2.87%` | `20X Cross` |
| `261` | `0x3678...b209` | `LONG` | 8,794,060.00 USD | `2,200.00` | `4176.09` | `3997.00` | `2644.12` | -393,359.30 USD | `-4.47%` | `25X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,896,340.44 USD | `1,975.37` | `4048.55` | `3997.00` | `6607.26` | 101,051.27 USD | `+1.28%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,315,541.33 USD | `1,579.95` | `4075.62` | `3997.00` | `0.000000` | -123,755.64 USD | `-1.96%` | `1X Cross` |
| `561` | `0x63da...8add` | `LONG` | 3,997,300.00 USD | `1,000.00` | `4021.46` | `3997.00` | `3564.37` | -24,160.96 USD | `-0.60%` | `25X Cross` |
| `570` | `0xf3dc...1672` | `LONG` | 3,935,507.97 USD | `984.27` | `4018.39` | `3997.00` | `2894.46` | -19,678.73 USD | `-0.50%` | `20X Cross` |
| `587` | `0x9aa5...58af` | `LONG` | 3,884,041.73 USD | `971.64` | `4279.98` | `3997.00` | `0.000000` | -274,567.35 USD | `-7.07%` | `20X Cross` |
| `591` | `0x354b...6425` | `LONG` | 3,832,640.82 USD | `958.81` | `4004.93` | `3997.00` | `0.000000` | -7,320.40 USD | `-0.19%` | `10X Cross` |
| `671` | `0x4a20...3c26` | `LONG` | 3,347,337.82 USD | `837.40` | `4599.73` | `3997.00` | `0.000000` | -504,482.56 USD | `-15.07%` | `20X Cross` |
| `825` | `0x0fac...7a0a` | `LONG` | 2,744,086.49 USD | `686.49` | `4290.34` | `3997.00` | `1247.35` | -201,172.21 USD | `-7.33%` | `25X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,478,264.00 USD | `620.00` | `4122.81` | `3997.00` | `4342.50` | 77,883.03 USD | `+3.14%` | `20X Cross` |
| `908` | `0xd8c5...99b0` | `SHORT` | 2,471,811.88 USD | `618.35` | `4175.35` | `3997.00` | `34228.28` | 110,040.73 USD | `+4.45%` | `4X Cross` |
| `934` | `0xeae3...e8ad` | `SHORT` | 2,398,440.00 USD | `600.00` | `4104.77` | `3997.00` | `4325.52` | 64,425.11 USD | `+2.69%` | `20X Cross` |
| `936` | `0xf285...fa82` | `LONG` | 2,390,988.15 USD | `598.11` | `4146.45` | `3997.00` | `3891.51` | -89,031.41 USD | `-3.72%` | `25X Cross` |
| `955` | `0x12f7...8750` | `LONG` | 2,340,861.65 USD | `585.61` | `4082.77` | `3997.00` | `2609.64` | -50,055.33 USD | `-2.14%` | `10X Cross` |
| `1092` | `0x413c...886c` | `LONG` | 1,999,200.00 USD | `500.00` | `4010.43` | `3997.00` | `0.000000` | -6,016.23 USD | `-0.30%` | `2X Cross` |
| `1097` | `0x9c06...0560` | `LONG` | 1,992,323.47 USD | `498.42` | `4012.76` | `3997.00` | `0.000000` | -7,708.02 USD | `-0.39%` | `25X Cross` |
| `1101` | `0x61ce...a62b` | `SHORT` | 1,988,869.74 USD | `497.50` | `4071.66` | `3997.00` | `4718.93` | 36,799.05 USD | `+1.85%` | `20X Cross` |
| `1174` | `0x2edd...8179` | `LONG` | 1,881,055.64 USD | `469.89` | `4164.68` | `4003.10` | `0.000000` | -75,876.88 USD | `-4.03%` | `10X Cross` |
| `1216` | `0xead5...69f2` | `LONG` | 1,813,955.76 USD | `453.78` | `4220.88` | `3997.00` | `3539.20` | -101,412.30 USD | `-5.59%` | `5X Isolated` |
| `1278` | `0x7a6d...f79c` | `SHORT` | 1,715,786.41 USD | `428.38` | `4136.09` | `4003.10` | `5366.63` | 56,028.60 USD | `+3.27%` | `10X Cross` |
| `1308` | `0x46fc...1195` | `LONG` | 1,658,537.39 USD | `414.87` | `4053.27` | `3997.00` | `2165.62` | -23,055.46 USD | `-1.39%` | `20X Cross` |
| `1345` | `0x6d15...d374` | `LONG` | 1,598,960.00 USD | `400.00` | `4068.25` | `3997.00` | `3842.07` | -28,340.00 USD | `-1.77%` | `25X Cross` |
| `1346` | `0xee02...309d` | `SHORT` | 1,598,920.00 USD | `400.00` | `4438.84` | `3997.00` | `4227.14` | 176,618.60 USD | `+11.05%` | `25X Isolated` |
| `1389` | `0x51f6...2b39` | `LONG` | 1,566,956.56 USD | `391.43` | `4228.28` | `4003.10` | `478.29` | -88,102.96 USD | `-5.62%` | `10X Cross` |
| `1394` | `0x02a7...fe9f` | `SHORT` | 1,558,947.00 USD | `390.00` | `4055.02` | `3997.00` | `4306.96` | 22,512.25 USD | `+1.44%` | `25X Cross` |
| `1429` | `0x7e77...b8d2` | `SHORT` | 1,519,012.00 USD | `380.00` | `4131.92` | `3997.00` | `4293.77` | 51,117.64 USD | `+3.37%` | `20X Cross` |
| `1451` | `0x72c2...9b37` | `LONG` | 1,492,264.01 USD | `373.13` | `4000.98` | `3997.00` | `3778.31` | -629.51 USD | `-0.04%` | `13X Isolated` |
| `1488` | `0x781e...96b7` | `SHORT` | 1,446,672.52 USD | `361.37` | `4363.26` | `4003.10` | `13165.76` | 130,077.28 USD | `+8.99%` | `10X Cross` |
| `1501` | `0xaa44...b844` | `LONG` | 1,439,424.00 USD | `360.00` | `4043.10` | `3997.00` | `2819.93` | -16,093.63 USD | `-1.12%` | `4X Cross` |
| `1605` | `0xa41f...d50a` | `LONG` | 1,314,993.10 USD | `328.96` | `4468.89` | `3997.00` | `3802.43` | -155,104.75 USD | `-11.80%` | `15X Cross` |
| `1649` | `0x7fda...17d1` | `SHORT` | 1,277,275.63 USD | `319.53` | `4013.13` | `3997.00` | `30647.15` | 5,026.55 USD | `+0.39%` | `20X Cross` |
| `1659` | `0xbf5a...88ba` | `SHORT` | 1,269,793.70 USD | `317.65` | `4091.80` | `3997.00` | `9985.72` | 29,989.34 USD | `+2.36%` | `20X Cross` |
| `1693` | `0xff31...ff6c` | `SHORT` | 1,239,163.00 USD | `310.00` | `4372.43` | `3997.00` | `4789.43` | 116,292.38 USD | `+9.38%` | `10X Isolated` |
| `1719` | `0xada6...6f88` | `LONG` | 1,213,778.75 USD | `303.50` | `4166.46` | `3997.00` | `1790.90` | -50,734.11 USD | `-4.18%` | `5X Cross` |
| `1883` | `0x50e2...d770` | `LONG` | 1,080,739.61 USD | `270.37` | `4243.58` | `3997.00` | `2562.36` | -66,586.85 USD | `-6.16%` | `20X Cross` |
| `1897` | `0x4c92...4f17` | `SHORT` | 1,066,161.85 USD | `266.72` | `4260.98` | `3997.00` | `6505.26` | 70,330.38 USD | `+6.60%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,020,082.78 USD | `255.17` | `4188.66` | `3997.00` | `3310.69` | -48,753.73 USD | `-4.78%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4084.50` (Vol: 319,200.00 USD, Dist: `+1.79%`) | Long MP=`3949.61` (Vol: 346,900.00 USD, Dist: `--1.57%`)
  * 48H Horizon: Short MP=`4097.67` (Vol: 378,100.00 USD, Dist: `+2.12%`) | Long MP=`3936.55` (Vol: 378,100.00 USD, Dist: `--1.89%`)
  * 3D Horizon: Short MP=`4097.67` (Vol: 405,200.00 USD, Dist: `+2.12%`) | Long MP=`3936.55` (Vol: 405,200.00 USD, Dist: `--1.89%`)
  * 7D Horizon: Short MP=`4086.63` (Vol: 910,300.00 USD, Dist: `+1.85%`) | Long MP=`3923.02` (Vol: 1,000,000.00 USD, Dist: `--2.23%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3596.10` | 16,110,000.00 USD | 16,110,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3600.40` | 16,090,000.00 USD | 16,090,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3601.80` | 4,880,000.00 USD | 4,880,000.00 USD | 22,150.00 USD | 0.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3604.70` | 15,920,000.00 USD | 15,920,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.00` | 4,830,000.00 USD | 4,830,000.00 USD | 58,500.00 USD | 0.00 USD | 22,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3609.00` | 15,650,000.00 USD | 15,650,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.20` | 4,750,000.00 USD | 4,750,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3613.30` | 15,460,000.00 USD | 15,460,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.40` | 4,730,000.00 USD | 4,730,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3617.60` | 15,360,000.00 USD | 15,360,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.60` | 4,680,000.00 USD | 4,680,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3621.90` | 15,240,000.00 USD | 15,240,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.80` | 4,640,000.00 USD | 4,640,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3626.20` | 15,160,000.00 USD | 15,160,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.00` | 4,550,000.00 USD | 4,550,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3630.50` | 15,080,000.00 USD | 15,080,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 4,510,000.00 USD | 4,510,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3634.80` | 14,960,000.00 USD | 14,960,000.00 USD | 44,190.00 USD | 0.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.40` | 4,460,000.00 USD | 4,460,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3639.10` | 14,910,000.00 USD | 14,910,000.00 USD | 22,690.00 USD | 0.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.60` | 4,450,000.00 USD | 4,450,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3643.40` | 14,880,000.00 USD | 14,880,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3647.70` | 14,830,000.00 USD | 14,830,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3652.00` | 14,800,000.00 USD | 14,800,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3656.30` | 14,770,000.00 USD | 14,770,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3660.60` | 14,730,000.00 USD | 14,730,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3664.90` | 14,710,000.00 USD | 14,710,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3669.20` | 14,700,000.00 USD | 14,700,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3832.60` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3836.90` | 14,690,000.00 USD | 14,690,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3841.20` | 4,450,000.00 USD | 4,450,000.00 USD | 63,550.00 USD | 0.00 USD | 66,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3841.20` | 14,480,000.00 USD | 14,480,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3845.40` | 4,320,000.00 USD | 4,320,000.00 USD | 183,730.00 USD | 0.00 USD | 78,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3845.50` | 13,830,000.00 USD | 13,830,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3849.60` | 4,060,000.00 USD | 4,060,000.00 USD | 35,100.00 USD | 0.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3849.80` | 13,130,000.00 USD | 13,130,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.80` | 4,000,000.00 USD | 4,000,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.10` | 12,590,000.00 USD | 12,590,000.00 USD | 249,250.00 USD | 0.00 USD | 66,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.00` | 3,850,000.00 USD | 3,850,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3858.40` | 12,280,000.00 USD | 12,280,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.20` | 3,730,000.00 USD | 3,730,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3862.70` | 11,870,000.00 USD | 11,870,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.40` | 3,520,000.00 USD | 3,520,000.00 USD | 199,300.00 USD | 0.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.00` | 11,630,000.00 USD | 11,630,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.60` | 3,290,000.00 USD | 3,290,000.00 USD | 160,940.00 USD | 0.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.30` | 11,340,000.00 USD | 11,340,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3874.80` | 3,110,000.00 USD | 3,110,000.00 USD | 83,160.00 USD | 0.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.60` | 11,020,000.00 USD | 11,020,000.00 USD | 297,370.00 USD | 0.00 USD | 29,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.00` | 3,010,000.00 USD | 3,010,000.00 USD | 43,430.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3879.90` | 10,690,000.00 USD | 10,690,000.00 USD | 170,480.00 USD | 0.00 USD | 27,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.20` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.20` | 10,490,000.00 USD | 10,490,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,340,000.00 USD | 10,340,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.80` | 10,230,000.00 USD | 10,230,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3897.10` | 10,100,000.00 USD | 10,100,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.40` | 9,990,000.00 USD | 9,990,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.70` | 9,900,000.00 USD | 9,900,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3910.00` | 9,830,000.00 USD | 9,830,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3914.30` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3918.60` | 9,790,000.00 USD | 9,790,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3921.00` | 2,970,000.00 USD | 2,970,000.00 USD | 127,100.00 USD | 0.00 USD | 115,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.90` | 8,880,000.00 USD | 8,880,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3925.20` | 2,720,000.00 USD | 2,720,000.00 USD | 357,750.00 USD | 0.00 USD | 163,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3927.20` | 7,480,000.00 USD | 7,480,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3929.40` | 2,200,000.00 USD | 2,200,000.00 USD | 79,920.00 USD | 0.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3931.50` | 6,120,000.00 USD | 6,120,000.00 USD | 605,700.00 USD | 0.00 USD | 168,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.60` | 2,060,000.00 USD | 2,060,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3935.80` | 5,350,000.00 USD | 5,350,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3937.80` | 1,800,000.00 USD | 1,800,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3940.10` | 4,440,000.00 USD | 4,440,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.00` | 1,570,000.00 USD | 1,570,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3944.40` | 4,050,000.00 USD | 4,050,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.20` | 1,190,000.00 USD | 1,190,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3948.70` | 3,500,000.00 USD | 3,500,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.40` | 699,920.00 USD | 699,920.00 USD | 347,740.00 USD | 0.00 USD | 43,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3953.00` | 2,830,000.00 USD | 2,830,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 308,350.00 USD | 308,350.00 USD | 173,010.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3957.30` | 2,210,000.00 USD | 2,210,000.00 USD | 478,000.00 USD | 0.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.80` | 102,710.00 USD | 102,710.00 USD | 87,950.00 USD | 0.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3961.60` | 1,690,000.00 USD | 1,690,000.00 USD | 305,950.00 USD | 0.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.00` | 11,170.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3965.90` | 1,320,000.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3970.20` | 1,050,000.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3974.50` | 831,670.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3978.80` | 579,930.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3983.10` | 237,060.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3987.40` | 208,420.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3991.70` | 46,230.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4080.60` | 227,000.00 USD | 227,000.00 USD | 127,100.00 USD | 0.00 USD | 99,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4084.80` | 750,200.00 USD | 750,200.00 USD | 346,920.00 USD | 0.00 USD | 176,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4089.00` | 859,720.00 USD | 859,720.00 USD | 76,430.00 USD | 0.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.20` | 1,090,000.00 USD | 1,090,000.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.90` | 4,820,000.00 USD | 4,820,000.00 USD | 498,510.00 USD | 0.00 USD | 127,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.40` | 1,340,000.00 USD | 1,340,000.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4099.20` | 5,570,000.00 USD | 5,570,000.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.60` | 1,690,000.00 USD | 1,690,000.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4103.50` | 6,060,000.00 USD | 6,060,000.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4105.80` | 2,170,000.00 USD | 2,170,000.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4107.80` | 6,660,000.00 USD | 6,660,000.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.00` | 2,480,000.00 USD | 2,480,000.00 USD | 271,030.00 USD | 0.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4112.10` | 7,130,000.00 USD | 7,130,000.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.20` | 2,810,000.00 USD | 2,810,000.00 USD | 294,970.00 USD | 0.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4116.40` | 7,750,000.00 USD | 7,750,000.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.40` | 2,930,000.00 USD | 2,930,000.00 USD | 105,160.00 USD | 0.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4120.70` | 8,190,000.00 USD | 8,190,000.00 USD | 404,230.00 USD | 0.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.60` | 2,970,000.00 USD | 2,970,000.00 USD | 34,710.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4125.00` | 8,620,000.00 USD | 8,620,000.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4129.30` | 8,800,000.00 USD | 8,800,000.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4133.60` | 9,050,000.00 USD | 9,050,000.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4137.90` | 9,280,000.00 USD | 9,280,000.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4142.20` | 9,560,000.00 USD | 9,560,000.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4146.50` | 9,620,000.00 USD | 9,620,000.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4150.80` | 9,750,000.00 USD | 9,750,000.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4155.10` | 9,820,000.00 USD | 9,820,000.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4159.40` | 10,300,000.00 USD | 10,300,000.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.40` | 3,070,000.00 USD | 3,070,000.00 USD | 63,550.00 USD | 0.00 USD | 38,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4163.70` | 11,040,000.00 USD | 11,040,000.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.60` | 3,320,000.00 USD | 3,320,000.00 USD | 164,700.00 USD | 0.00 USD | 86,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4168.00` | 11,630,000.00 USD | 11,630,000.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.80` | 3,390,000.00 USD | 3,390,000.00 USD | 46,980.00 USD | 0.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4172.30` | 12,020,000.00 USD | 12,020,000.00 USD | 302,850.00 USD | 0.00 USD | 82,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.00` | 3,500,000.00 USD | 3,500,000.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4176.60` | 12,470,000.00 USD | 12,470,000.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.20` | 3,620,000.00 USD | 3,620,000.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4180.90` | 12,660,000.00 USD | 12,660,000.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.40` | 3,780,000.00 USD | 3,780,000.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4185.20` | 12,880,000.00 USD | 12,880,000.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.60` | 3,970,000.00 USD | 3,970,000.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4189.50` | 13,170,000.00 USD | 13,170,000.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.80` | 4,170,000.00 USD | 4,170,000.00 USD | 173,310.00 USD | 0.00 USD | 25,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4193.80` | 13,470,000.00 USD | 13,470,000.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.00` | 4,340,000.00 USD | 4,340,000.00 USD | 148,350.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4198.10` | 13,730,000.00 USD | 13,730,000.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.20` | 4,410,000.00 USD | 4,410,000.00 USD | 61,860.00 USD | 0.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.40` | 4,450,000.00 USD | 4,450,000.00 USD | 38,300.00 USD | 0.00 USD | 510.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4202.40` | 13,910,000.00 USD | 13,910,000.00 USD | 157,220.00 USD | 0.00 USD | 18,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.60` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4206.70` | 14,130,000.00 USD | 14,130,000.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.00` | 14,220,000.00 USD | 14,220,000.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4215.30` | 14,330,000.00 USD | 14,330,000.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4219.60` | 14,450,000.00 USD | 14,450,000.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4223.90` | 14,580,000.00 USD | 14,580,000.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.20` | 14,610,000.00 USD | 14,610,000.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.50` | 14,670,000.00 USD | 14,670,000.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4236.80` | 14,690,000.00 USD | 14,690,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4391.60` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4395.90` | 14,760,000.00 USD | 14,760,000.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4399.80` | 4,470,000.00 USD | 4,470,000.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.20` | 14,890,000.00 USD | 14,890,000.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.00` | 4,550,000.00 USD | 4,550,000.00 USD | 51,100.00 USD | 0.00 USD | 28,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4404.50` | 15,100,000.00 USD | 15,100,000.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4408.20` | 4,580,000.00 USD | 4,580,000.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4408.80` | 15,290,000.00 USD | 15,290,000.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4412.40` | 4,600,000.00 USD | 4,600,000.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.10` | 15,370,000.00 USD | 15,370,000.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4416.60` | 4,630,000.00 USD | 4,630,000.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.40` | 15,470,000.00 USD | 15,470,000.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4420.80` | 4,670,000.00 USD | 4,670,000.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.70` | 15,560,000.00 USD | 15,560,000.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4421.80` | 4,680,000.00 USD | 4,680,000.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.00` | 15,630,000.00 USD | 15,630,000.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 15,700,000.00 USD | 15,700,000.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.60` | 15,760,000.00 USD | 15,760,000.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.90` | 15,850,000.00 USD | 15,850,000.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4440.70` | 15,870,000.00 USD | 15,870,000.00 USD | 23,500.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |

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
| `7D` | `3596.10` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3600.40` | 16,090,000.00 USD | 0.00 USD | 16,090,000.00 USD | 143,980.00 USD | 0.00 USD | 24,440.00 USD |
| `1D` | `3601.80` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 22,150.00 USD | 0.00 USD | 24,530.00 USD |
| `7D` | `3604.70` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 198,670.00 USD | 0.00 USD | 69,070.00 USD |
| `1D` | `3606.00` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 58,500.00 USD | 0.00 USD | 22,800.00 USD |
| `7D` | `3609.00` | 15,650,000.00 USD | 0.00 USD | 15,650,000.00 USD | 149,900.00 USD | 0.00 USD | 35,820.00 USD |
| `1D` | `3610.20` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3613.30` | 15,460,000.00 USD | 0.00 USD | 15,460,000.00 USD | 90,850.00 USD | 0.00 USD | 15,620.00 USD |
| `1D` | `3614.40` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD |
| `7D` | `3617.60` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 109,140.00 USD | 0.00 USD | 5,470.00 USD |
| `1D` | `3618.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 34,170.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3621.90` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 54,110.00 USD | 0.00 USD | 24,610.00 USD |
| `1D` | `3622.80` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 73,510.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `3626.20` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 74,080.00 USD | 0.00 USD | 13,530.00 USD |
| `1D` | `3627.00` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 40,800.00 USD | 0.00 USD | 6,780.00 USD |
| `7D` | `3630.50` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 98,000.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `3631.20` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 35,410.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3634.80` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 44,190.00 USD | 0.00 USD | 6,850.00 USD |
| `1D` | `3635.40` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 12,560.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3639.10` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 22,690.00 USD | 0.00 USD | 8,880.00 USD |
| `1D` | `3639.60` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.40` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 42,520.00 USD | 0.00 USD | 10,970.00 USD |
| `7D` | `3647.70` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 20,510.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3652.00` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3656.30` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 39,830.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `3660.60` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 11,970.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3664.90` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 7,390.00 USD | 0.00 USD | 2,700.00 USD |
| `7D` | `3669.20` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3832.60` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3836.90` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 194,860.00 USD | 0.00 USD | 12,240.00 USD |
| `1D` | `3841.20` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 63,550.00 USD | 0.00 USD | 66,030.00 USD |
| `7D` | `3841.20` | 14,480,000.00 USD | 0.00 USD | 14,480,000.00 USD | 553,720.00 USD | 0.00 USD | 100,310.00 USD |
| `1D` | `3845.40` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 183,730.00 USD | 0.00 USD | 78,900.00 USD |
| `7D` | `3845.50` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 518,150.00 USD | 0.00 USD | 176,560.00 USD |
| `1D` | `3849.60` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 35,100.00 USD | 0.00 USD | 24,620.00 USD |
| `7D` | `3849.80` | 13,130,000.00 USD | 0.00 USD | 13,130,000.00 USD | 442,940.00 USD | 0.00 USD | 95,570.00 USD |
| `1D` | `3853.80` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 115,420.00 USD | 0.00 USD | 34,820.00 USD |
| `7D` | `3854.10` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 249,250.00 USD | 0.00 USD | 66,410.00 USD |
| `1D` | `3858.00` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 96,590.00 USD | 0.00 USD | 24,610.00 USD |
| `7D` | `3858.40` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 385,210.00 USD | 0.00 USD | 20,910.00 USD |
| `1D` | `3862.20` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 176,170.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3862.70` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 188,420.00 USD | 0.00 USD | 56,900.00 USD |
| `1D` | `3866.40` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 199,300.00 USD | 0.00 USD | 29,260.00 USD |
| `7D` | `3867.00` | 11,630,000.00 USD | 0.00 USD | 11,630,000.00 USD | 226,270.00 USD | 0.00 USD | 58,590.00 USD |
| `1D` | `3870.60` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 160,940.00 USD | 0.00 USD | 18,490.00 USD |
| `7D` | `3871.30` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 289,060.00 USD | 0.00 USD | 33,610.00 USD |
| `1D` | `3874.80` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 83,160.00 USD | 0.00 USD | 14,970.00 USD |
| `7D` | `3875.60` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 297,370.00 USD | 0.00 USD | 29,270.00 USD |
| `1D` | `3879.00` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 43,430.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `3879.90` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 170,480.00 USD | 0.00 USD | 27,170.00 USD |
| `1D` | `3883.20` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3884.20` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 110,950.00 USD | 0.00 USD | 43,540.00 USD |
| `7D` | `3888.50` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `3892.80` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `7D` | `3897.10` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `7D` | `3901.40` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 73,850.00 USD | 0.00 USD | 15,960.00 USD |
| `7D` | `3905.70` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 55,280.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3910.00` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 34,960.00 USD | 0.00 USD | 1,900.00 USD |
| `7D` | `3914.30` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3918.60` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 864,580.00 USD | 0.00 USD | 35,850.00 USD |
| `1D` | `3921.00` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 127,100.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3922.90` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 1,040,000.00 USD | 0.00 USD | 357,260.00 USD |
| `1D` | `3925.20` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 357,750.00 USD | 0.00 USD | 163,440.00 USD |
| `7D` | `3927.20` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 1,110,000.00 USD | 0.00 USD | 253,110.00 USD |
| `1D` | `3929.40` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 79,920.00 USD | 0.00 USD | 59,820.00 USD |
| `7D` | `3931.50` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 605,700.00 USD | 0.00 USD | 168,200.00 USD |
| `1D` | `3933.60` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `3935.80` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 797,940.00 USD | 0.00 USD | 109,880.00 USD |
| `1D` | `3937.80` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `3940.10` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 348,350.00 USD | 0.00 USD | 45,960.00 USD |
| `1D` | `3942.00` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 305,680.00 USD | 0.00 USD | 69,700.00 USD |
| `7D` | `3944.40` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 408,250.00 USD | 0.00 USD | 139,590.00 USD |
| `1D` | `3946.20` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `3948.70` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 596,220.00 USD | 0.00 USD | 68,420.00 USD |
| `1D` | `3950.40` | 699,920.00 USD | 0.00 USD | 699,920.00 USD | 347,740.00 USD | 0.00 USD | 43,820.00 USD |
| `7D` | `3953.00` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 531,020.00 USD | 0.00 USD | 88,650.00 USD |
| `1D` | `3954.60` | 308,350.00 USD | 0.00 USD | 308,350.00 USD | 173,010.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3957.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 478,000.00 USD | 0.00 USD | 49,670.00 USD |
| `1D` | `3958.80` | 102,710.00 USD | 0.00 USD | 102,710.00 USD | 87,950.00 USD | 0.00 USD | 3,590.00 USD |
| `7D` | `3961.60` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 305,950.00 USD | 0.00 USD | 60,830.00 USD |
| `1D` | `3963.00` | 11,170.00 USD | 0.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3965.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 202,410.00 USD | 0.00 USD | 64,760.00 USD |
| `7D` | `3970.20` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3974.50` | 831,670.00 USD | 0.00 USD | 831,670.00 USD | 227,060.00 USD | 0.00 USD | 24,680.00 USD |
| `7D` | `3978.80` | 579,930.00 USD | 0.00 USD | 579,930.00 USD | 331,960.00 USD | 0.00 USD | 10,910.00 USD |
| `7D` | `3983.10` | 237,060.00 USD | 0.00 USD | 237,060.00 USD | 0.00 USD | 0.00 USD | 28,630.00 USD |
| `7D` | `3987.40` | 208,420.00 USD | 0.00 USD | 208,420.00 USD | 134,250.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `3991.70` | 46,230.00 USD | 0.00 USD | 46,230.00 USD | 46,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4009.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4010.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.40` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.70` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `4080.60` | 227,000.00 USD | 227,000.00 USD | 0.00 USD | 127,100.00 USD | 0.00 USD | 99,890.00 USD |
| `7D` | `4082.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 255,440.00 USD |
| `1D` | `4084.80` | 750,200.00 USD | 750,200.00 USD | 0.00 USD | 346,920.00 USD | 0.00 USD | 176,290.00 USD |
| `7D` | `4086.30` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 944,930.00 USD | 0.00 USD | 319,180.00 USD |
| `1D` | `4089.00` | 859,720.00 USD | 859,720.00 USD | 0.00 USD | 76,430.00 USD | 0.00 USD | 33,090.00 USD |
| `7D` | `4090.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 791,050.00 USD | 0.00 USD | 164,600.00 USD |
| `1D` | `4093.20` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 157,510.00 USD | 0.00 USD | 77,320.00 USD |
| `7D` | `4094.90` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 498,510.00 USD | 0.00 USD | 127,890.00 USD |
| `1D` | `4097.40` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 197,620.00 USD | 0.00 USD | 51,660.00 USD |
| `7D` | `4099.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 712,920.00 USD | 0.00 USD | 31,920.00 USD |
| `1D` | `4101.60` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 298,260.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4103.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 373,230.00 USD | 0.00 USD | 117,160.00 USD |
| `1D` | `4105.80` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 405,090.00 USD | 0.00 USD | 70,840.00 USD |
| `7D` | `4107.80` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 471,200.00 USD | 0.00 USD | 128,670.00 USD |
| `1D` | `4110.00` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 271,030.00 USD | 0.00 USD | 39,710.00 USD |
| `7D` | `4112.10` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 418,780.00 USD | 0.00 USD | 55,560.00 USD |
| `1D` | `4114.20` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 294,970.00 USD | 0.00 USD | 37,210.00 USD |
| `7D` | `4116.40` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 558,330.00 USD | 0.00 USD | 63,430.00 USD |
| `1D` | `4118.40` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 105,160.00 USD | 0.00 USD | 16,410.00 USD |
| `7D` | `4120.70` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 404,230.00 USD | 0.00 USD | 36,010.00 USD |
| `1D` | `4122.60` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 34,710.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4125.00` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 357,280.00 USD | 0.00 USD | 70,770.00 USD |
| `7D` | `4129.30` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `4133.60` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `4137.90` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 222,900.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `4142.20` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 265,470.00 USD | 0.00 USD | 14,780.00 USD |
| `7D` | `4146.50` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 23,520.00 USD |
| `7D` | `4150.80` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 100,140.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4155.10` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 70,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4159.40` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 423,370.00 USD | 0.00 USD | 50,710.00 USD |
| `1D` | `4160.40` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 63,550.00 USD | 0.00 USD | 38,310.00 USD |
| `7D` | `4163.70` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 572,270.00 USD | 0.00 USD | 175,240.00 USD |
| `1D` | `4164.60` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 164,700.00 USD | 0.00 USD | 86,180.00 USD |
| `7D` | `4168.00` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 488,660.00 USD | 0.00 USD | 99,070.00 USD |
| `1D` | `4168.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 28,700.00 USD |
| `7D` | `4172.30` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 302,850.00 USD | 0.00 USD | 82,190.00 USD |
| `1D` | `4173.00` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 74,610.00 USD | 0.00 USD | 34,000.00 USD |
| `7D` | `4176.60` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 398,970.00 USD | 0.00 USD | 54,940.00 USD |
| `1D` | `4177.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 88,500.00 USD | 0.00 USD | 31,470.00 USD |
| `7D` | `4180.90` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 168,570.00 USD | 0.00 USD | 21,400.00 USD |
| `1D` | `4181.40` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD |
| `7D` | `4185.20` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 161,680.00 USD | 0.00 USD | 61,120.00 USD |
| `1D` | `4185.60` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 165,300.00 USD | 0.00 USD | 28,810.00 USD |
| `7D` | `4189.50` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 246,970.00 USD | 0.00 USD | 44,470.00 USD |
| `1D` | `4189.80` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 173,310.00 USD | 0.00 USD | 25,830.00 USD |
| `7D` | `4193.80` | 13,470,000.00 USD | 13,470,000.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 31,970.00 USD |
| `1D` | `4194.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 148,350.00 USD | 0.00 USD | 19,440.00 USD |
| `7D` | `4198.10` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 242,970.00 USD | 0.00 USD | 25,890.00 USD |
| `1D` | `4198.20` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 61,860.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `4202.40` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 38,300.00 USD | 0.00 USD | 510.84 USD |
| `7D` | `4202.40` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 157,220.00 USD | 0.00 USD | 18,000.00 USD |
| `1D` | `4206.60` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4206.70` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 178,610.00 USD | 0.00 USD | 39,990.00 USD |
| `7D` | `4211.00` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 62,650.00 USD | 0.00 USD | 25,510.00 USD |
| `7D` | `4215.30` | 14,330,000.00 USD | 14,330,000.00 USD | 0.00 USD | 97,630.00 USD | 0.00 USD | 19,970.00 USD |
| `7D` | `4219.60` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 109,910.00 USD | 0.00 USD | 6,690.00 USD |
| `7D` | `4223.90` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 116,270.00 USD | 0.00 USD | 8,380.00 USD |
| `7D` | `4228.20` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 17,060.00 USD | 0.00 USD | 13,080.00 USD |
| `7D` | `4232.50` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 56,630.00 USD | 0.00 USD | 10,620.00 USD |
| `7D` | `4236.80` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4391.60` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4395.90` | 14,760,000.00 USD | 14,760,000.00 USD | 0.00 USD | 59,780.00 USD | 0.00 USD | 4,890.00 USD |
| `1D` | `4399.80` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 11,760.00 USD | 0.00 USD | 10,970.00 USD |
| `7D` | `4400.20` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 111,100.00 USD | 0.00 USD | 19,550.00 USD |
| `1D` | `4404.00` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 51,100.00 USD | 0.00 USD | 28,620.00 USD |
| `7D` | `4404.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 164,380.00 USD | 0.00 USD | 53,870.00 USD |
| `1D` | `4408.20` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 23,070.00 USD | 0.00 USD | 7,740.00 USD |
| `7D` | `4408.80` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 148,970.00 USD | 0.00 USD | 32,000.00 USD |
| `1D` | `4412.40` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `4413.10` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 64,870.00 USD | 0.00 USD | 22,760.00 USD |
| `1D` | `4416.60` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 19,970.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `4417.40` | 15,470,000.00 USD | 15,470,000.00 USD | 0.00 USD | 87,130.00 USD | 0.00 USD | 14,100.00 USD |
| `1D` | `4420.80` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 32,630.00 USD | 0.00 USD | 5,280.00 USD |
| `7D` | `4421.70` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 86,150.00 USD | 0.00 USD | 3,250.00 USD |
| `1D` | `4421.80` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 9,110.00 USD | 0.00 USD | 434.26 USD |
| `7D` | `4426.00` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 45,280.00 USD | 0.00 USD | 17,700.00 USD |
| `7D` | `4430.30` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 49,350.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `4434.60` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 58,370.00 USD | 0.00 USD | 7,490.00 USD |
| `7D` | `4438.90` | 15,850,000.00 USD | 15,850,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 9,530.00 USD |
| `7D` | `4440.70` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 23,500.00 USD | 0.00 USD | 1,350.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.84M` | Total OI Tokens: `68,776.5 PAXG`
  * 1h OI Change: `-0.10%` | 4h OI Change: `+0.19%` | 24h OI Change: `+0.76%`
  * Exchange Breakdown: Binance=`106.91M` | Bybit=`22.24M` | OKX=`-` | Hyperliquid=`24.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-1.98K` | Last 24h: `24.09K` | Last 3d: `91.36K` | Last 7d: `222.86K`
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
| `15M` | `PAXG` | `41.96%` | `58.04%` | `0.72` | 809,980.00 USD |
| `15M` | `Binance` | `46.78%` | `53.22%` | `0.88` | 398,710.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `51.44%` | `48.56%` | `1.06` | 48,010.00 USD |
| `15M` | `KuCoin` | `51.45%` | `48.55%` | `1.06` | 86,320.00 USD |
| `15M` | `Gate` | `49.5%` | `50.5%` | `0.98` | 8,740.00 USD |
| `15M` | `Bitget` | `52.55%` | `47.45%` | `1.11` | 84,240.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `47.69%` | `52.31%` | `0.91` | 49,070.00 USD |
| `15M` | `Bitunix` | `42.08%` | `57.92%` | `0.73` | 12,620.00 USD |
| `15M` | `Hyperliquid` | `1.18%` | `98.82%` | `0.01` | 41,610.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.27%` | `99.73%` | `0.00` | 72,060.00 USD |
| `15M` | `HTX` | `30.54%` | `69.46%` | `0.44` | 2,580.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 2,670.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `83.44%` | `16.56%` | `5.04` | 3,340.00 USD |
| `15M` | `Whale Positions` | `46.78%` | `53.22%` | `0.88` | 398,710.00 USD |
| `15M` | `Global Accounts` | `41.96%` | `58.04%` | `0.72` | 809,980.00 USD |
| `1H` | `PAXG` | `58.13%` | `41.87%` | `1.39` | 6,300,000.00 USD |
| `1H` | `Binance` | `58.71%` | `41.29%` | `1.42` | 3,570,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `82.88%` | `17.12%` | `4.84` | 699,120.00 USD |
| `1H` | `KuCoin` | `51.89%` | `48.11%` | `1.08` | 335,370.00 USD |
| `1H` | `Gate` | `43.11%` | `56.89%` | `0.76` | 116,350.00 USD |
| `1H` | `Bitget` | `53.48%` | `46.52%` | `1.15` | 899,170.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `71.81%` | `28.19%` | `2.55` | 117,340.00 USD |
| `1H` | `Bitunix` | `66.12%` | `33.88%` | `1.95` | 137,380.00 USD |
| `1H` | `Hyperliquid` | `45.61%` | `54.39%` | `0.84` | 124,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.78%` | `91.22%` | `0.10` | 253,240.00 USD |
| `1H` | `HTX` | `50.77%` | `49.23%` | `1.03` | 15,630.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `69.08%` | `30.92%` | `2.23` | 440.84 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `62.39%` | `37.61%` | `1.66` | 27,920.00 USD |
| `1H` | `Whale Positions` | `58.71%` | `41.29%` | `1.42` | 3,570,000.00 USD |
| `1H` | `Global Accounts` | `58.13%` | `41.87%` | `1.39` | 6,300,000.00 USD |
| `4H` | `PAXG` | `42.52%` | `57.48%` | `0.74` | 51,690,000.00 USD |
| `4H` | `Binance` | `45.67%` | `54.33%` | `0.84` | 7,590,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `46.06%` | `53.94%` | `0.85` | 3,500,000.00 USD |
| `4H` | `KuCoin` | `59.62%` | `40.38%` | `1.48` | 254,330.00 USD |
| `4H` | `Gate` | `47.89%` | `52.11%` | `0.92` | 1,870,000.00 USD |
| `4H` | `Bitget` | `46.18%` | `53.82%` | `0.86` | 2,860,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `39.77%` | `60.23%` | `0.66` | 29,640,000.00 USD |
| `4H` | `Bitunix` | `53.24%` | `46.76%` | `1.14` | 1,290,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.08%` | `47.92%` | `1.09` | 3,030,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `22.92%` | `77.08%` | `0.30` | 1,480,000.00 USD |
| `4H` | `HTX` | `83.14%` | `16.86%` | `4.93` | 157,780.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.26%` | `23.74%` | `3.21` | 2,900.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `45.67%` | `54.33%` | `0.84` | 7,590,000.00 USD |
| `4H` | `Global Accounts` | `42.52%` | `57.48%` | `0.74` | 51,690,000.00 USD |


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
| `5m` | -22,720.00 USD | -29,530.00 USD | **`DISTRIBUTION`** |
| `15m` | -78,350.00 USD | -51,260.00 USD | **`DISTRIBUTION`** |
| `30m` | -20,500.00 USD | 41,190.00 USD | **`ACCUMULATION`** |
| `1h` | 1,840,000.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,740,000.00 USD | 920,870.00 USD | **`ACCUMULATION`** |
| `4h` | 1,680,000.00 USD | 941,340.00 USD | **`ACCUMULATION`** |
| `6h` | 1,810,000.00 USD | 3,630.00 USD | **`ACCUMULATION`** |
| `8h` | 1,980,000.00 USD | -277,760.00 USD | **`ACCUMULATION`** |
| `12h` | 412,310.00 USD | 354,600.00 USD | **`ACCUMULATION`** |
| `24h` | 456,740.00 USD | 599,800.00 USD | **`ACCUMULATION`** |
| `1w` | -6,690,000.00 USD | -8,910,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -18,030,000.00 USD | -69,560,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-22.72K` | 15m=`-78.35K` | 1h=`+1.84M` | 24h=`+456.74K`
* Futures Capital Netflows: 5m=`-29.53K` | 15m=`-51.26K` | 1h=`+1.14M` | 24h=`+599.80K`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3996.99` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3987.70` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `4020.20`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4012.77` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4022.06` (Risk Distance: `9.29` pts)
  * +2.5R Take Profit: `3989.56`
  * Mathematical Lot Sizing: **`1.07 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4030.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
