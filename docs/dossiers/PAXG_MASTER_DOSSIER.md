# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4011.83` | **Live Ask Quote**: `4011.91` | **Mid Price**: `4011.87`
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
  * Session VWAP: `4029.35` | VWAP Z-Score: `-1.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.81` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.08` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.27` | Lower -3.00σ Band: `3994.42`
  * Upper +2.51σ Band: `4058.57` | Lower -2.51σ Band: `4000.13`
  * Upper +2.01σ Band: `4052.75` | Lower -2.01σ Band: `4005.95`
  * Upper +2.00σ Band: `4052.63` | Lower -2.00σ Band: `4006.07`
  * Upper +1.28σ Band: `4044.25` | Lower -1.28σ Band: `4014.45`
  * Upper +1.00σ Band: `4040.99` | Lower -1.00σ Band: `4017.71`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4019.23` | EMA-20=`4019.15` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.38` (Slope: `+0.0000`) | EMA-100=`4028.18`
  * Institutional Anchors: EMA-144=`4030.27` | EMA-200=`4030.69` (Slope: `-0.0311`) | EMA-233=`4030.45`
- **Range Boundaries**: 24H High=`4068.84` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4025.09` (Distance: `-0.32%`)
  * Point of Control (POC) = `4020.94` (Distance: `-0.22%`)
  * Value Area Low (VAL) = `4017.82` (Distance: `-0.14%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4011.64`
  * London Session (08:00-16:00 UTC): High=`4027.92` | Low=`3995.82`
  * New York Session (13:00-21:00 UTC): High=`4035.94` | Low=`3987.80`
  * Initial Balance (First Hour): IB High=`4023.91` | IB Low=`3999.83`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3995.82` - `4027.92`
  * Optimal Trade Entry (OTE 0.705): `4019.89`
  * Structural Invalidation Anchor (0.786): `4043.96`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4020.55` | `4021.48` | `4018.81` | `4019.40` | `44` | 174,901.51 USD | -24,535.94 USD | `-14.03%` | 1,906,394.51 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `4019.40` | `4019.41` | `4017.45` | `4018.87` | `37` | 147,309.97 USD | 14,022.38 USD | `+9.52%` | 1,920,416.89 USD | `-0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4018.86` | `4018.86` | `4017.19` | `4017.20` | `6` | 22,661.14 USD | -16,690.89 USD | `-73.65%` | 1,903,726.00 USD | `-0.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4026.37` | `4029.17` | `4025.59` | `4025.59` | `113` | 456,921.14 USD | 49,642.38 USD | `+10.86%` | 1,855,816.81 USD | `+0.08` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4025.54` | `4025.54` | `4017.45` | `4018.87` | `136` | 548,572.29 USD | -54,869.29 USD | `-10.00%` | 1,800,947.52 USD | `-0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4018.86` | `4018.86` | `4017.19` | `4017.20` | `6` | 22,661.14 USD | -16,690.89 USD | `-73.65%` | 1,784,256.63 USD | `-0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,132,085.43 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4029.17` | `4017.72` | `4025.59` | `562` | 2,260,235.02 USD | 263,421.07 USD | `+11.65%` | 1,395,506.50 USD | `+0.51` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4025.54` | `4025.54` | `4017.19` | `4017.19` | `142` | 570,160.84 USD | -72,632.77 USD | `-12.74%` | 1,322,873.73 USD | `-0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.19` | `4017.19` | `2,355` | 9,477,811.49 USD | 75,726.40 USD | `+0.80%` | 1,322,873.73 USD | `-0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.19` | `4017.19` | `2,355` | 9,477,811.49 USD | 75,726.40 USD | `+0.80%` | 1,322,873.73 USD | `-0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,555,739.67 USD | `6,365.38` | `4188.90` | `4015.10` | `33092.73` | 1,108,231.62 USD | `+4.34%` | `4X Cross` |
| `52` | `0x4692...164f` | `SHORT` | 25,473,600.79 USD | `6,344.45` | `4132.30` | `4015.10` | `13832.08` | 743,579.71 USD | `+2.92%` | `5X Cross` |
| `68` | `0xb83d...6e36` | `SHORT` | 23,569,407.06 USD | `5,869.90` | `4228.86` | `4015.10` | `30827.52` | 1,253,614.87 USD | `+5.32%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,390,958.55 USD | `4,828.91` | `4157.43` | `4015.10` | `2247.74` | -684,923.77 USD | `-3.53%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,176,368.13 USD | `3,530.76` | `4129.09` | `4015.10` | `465.06` | -402,482.93 USD | `-2.84%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,122,202.82 USD | `3,268.21` | `4228.94` | `4015.10` | `4398.84` | 698,876.31 USD | `+5.33%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,642,920.40 USD | `2,900.00` | `4364.92` | `4015.10` | `4235.69` | 1,015,355.93 USD | `+8.72%` | `20X Cross` |
| `262` | `0x41e5...0825` | `SHORT` | 8,833,660.00 USD | `2,200.00` | `4112.20` | `4015.10` | `4331.18` | 213,194.59 USD | `+2.41%` | `20X Cross` |
| `263` | `0x3678...b209` | `LONG` | 8,832,120.00 USD | `2,200.00` | `4176.09` | `4015.10` | `2736.48` | -355,299.30 USD | `-4.02%` | `25X Cross` |
| `297` | `0xacb6...efbd` | `SHORT` | 7,931,304.47 USD | `1,975.37` | `4048.55` | `4015.10` | `6526.06` | 66,087.24 USD | `+0.83%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,343,664.47 USD | `1,579.95` | `4075.62` | `4015.10` | `0.000000` | -95,632.50 USD | `-1.51%` | `1X Cross` |
| `402` | `0x12d2...f97f` | `LONG` | 5,628,940.54 USD | `1,401.94` | `4278.91` | `4015.10` | `3186.37` | -369,850.04 USD | `-6.57%` | `20X Cross` |
| `414` | `0xfc66...ca06` | `SHORT` | 5,399,654.24 USD | `1,344.84` | `4031.28` | `4015.10` | `14604.21` | 21,768.86 USD | `+0.40%` | `3X Cross` |
| `553` | `0x63da...8add` | `LONG` | 4,014,600.00 USD | `1,000.00` | `4021.46` | `4015.10` | `3564.14` | -6,860.96 USD | `-0.17%` | `25X Cross` |
| `577` | `0x9aa5...58af` | `LONG` | 3,901,045.47 USD | `971.64` | `4279.98` | `4015.10` | `0.000000` | -257,563.62 USD | `-6.60%` | `20X Cross` |
| `601` | `0xf3dc...1672` | `LONG` | 3,737,029.03 USD | `930.74` | `4024.62` | `4015.10` | `3419.30` | -8,863.53 USD | `-0.24%` | `20X Cross` |
| `673` | `0x4a20...3c26` | `LONG` | 3,362,243.54 USD | `837.40` | `4599.73` | `4015.10` | `0.000000` | -489,576.85 USD | `-14.56%` | `20X Cross` |
| `824` | `0x0fac...7a0a` | `LONG` | 2,756,099.98 USD | `686.49` | `4290.34` | `4015.10` | `1547.56` | -189,158.73 USD | `-6.86%` | `25X Cross` |
| `881` | `0xd8c5...99b0` | `SHORT` | 2,578,926.45 USD | `642.35` | `4175.35` | `4015.10` | `33056.02` | 103,134.73 USD | `+4.00%` | `4X Cross` |
| `910` | `0x625e...a354` | `SHORT` | 2,489,548.00 USD | `620.00` | `4122.81` | `4015.10` | `4342.28` | 66,599.03 USD | `+2.68%` | `20X Cross` |
| `942` | `0xeae3...e8ad` | `SHORT` | 2,409,000.00 USD | `600.00` | `4104.77` | `4015.10` | `4325.30` | 53,865.11 USD | `+2.24%` | `20X Cross` |
| `945` | `0xf285...fa82` | `LONG` | 2,401,335.38 USD | `598.11` | `4146.45` | `4015.10` | `3891.27` | -78,684.17 USD | `-3.28%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,351,109.84 USD | `585.61` | `4082.77` | `4015.10` | `2560.70` | -39,807.14 USD | `-1.69%` | `10X Cross` |
| `1102` | `0x413c...886c` | `LONG` | 2,007,950.00 USD | `500.00` | `4010.43` | `4015.10` | `0.000000` | 2,733.77 USD | `+0.14%` | `2X Cross` |
| `1111` | `0x61ce...a62b` | `SHORT` | 1,997,725.30 USD | `497.50` | `4071.66` | `4015.10` | `4715.88` | 27,943.49 USD | `+1.40%` | `20X Cross` |
| `1117` | `0x0593...40f9` | `LONG` | 1,992,448.36 USD | `496.18` | `4024.57` | `4015.10` | `3701.76` | -4,455.47 USD | `-0.22%` | `10X Isolated` |
| `1186` | `0x2edd...8179` | `LONG` | 1,891,940.07 USD | `470.91` | `4164.68` | `4017.50` | `0.000000` | -69,261.24 USD | `-3.66%` | `10X Cross` |
| `1225` | `0xead5...69f2` | `LONG` | 1,822,078.49 USD | `453.78` | `4220.88` | `4015.10` | `3538.97` | -93,289.57 USD | `-5.12%` | `5X Isolated` |
| `1292` | `0x7a6d...f79c` | `SHORT` | 1,721,055.47 USD | `428.38` | `4136.09` | `4017.50` | `5772.18` | 50,759.54 USD | `+2.95%` | `10X Cross` |
| `1315` | `0x46fc...1195` | `LONG` | 1,671,854.72 USD | `416.39` | `4054.56` | `4015.10` | `2203.96` | -16,431.27 USD | `-0.98%` | `20X Cross` |
| `1369` | `0x6d15...d374` | `LONG` | 1,606,040.00 USD | `400.00` | `4068.25` | `4015.10` | `3841.84` | -21,260.00 USD | `-1.32%` | `25X Cross` |
| `1370` | `0xee02...309d` | `SHORT` | 1,605,920.00 USD | `400.00` | `4438.84` | `4015.10` | `4226.91` | 169,618.60 USD | `+10.56%` | `25X Isolated` |
| `1407` | `0x02a7...fe9f` | `SHORT` | 1,565,889.00 USD | `390.00` | `4055.02` | `4015.10` | `4306.73` | 15,570.25 USD | `+0.99%` | `25X Cross` |
| `1443` | `0x51f6...2b39` | `LONG` | 1,533,779.06 USD | `381.76` | `4233.94` | `4017.50` | `0.000000` | -82,592.57 USD | `-5.38%` | `10X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,525,624.00 USD | `380.00` | `4131.92` | `4015.10` | `4293.54` | 44,505.64 USD | `+2.92%` | `20X Cross` |
| `1463` | `0x9c06...0560` | `LONG` | 1,498,679.84 USD | `373.26` | `4018.98` | `4015.10` | `0.000000` | -1,451.97 USD | `-0.10%` | `25X Cross` |
| `1464` | `0x72c2...9b37` | `LONG` | 1,498,159.48 USD | `373.13` | `4000.98` | `4015.10` | `3778.07` | 5,265.97 USD | `+0.35%` | `13X Isolated` |
| `1507` | `0xaa44...b844` | `LONG` | 1,445,364.00 USD | `360.00` | `4043.10` | `4015.10` | `2822.64` | -10,153.63 USD | `-0.70%` | `4X Cross` |
| `1509` | `0x781e...96b7` | `SHORT` | 1,444,781.19 USD | `359.61` | `4364.97` | `4017.50` | `13643.60` | 124,919.73 USD | `+8.65%` | `10X Cross` |
| `1627` | `0xa41f...d50a` | `LONG` | 1,320,749.94 USD | `328.96` | `4468.89` | `4015.10` | `3833.21` | -149,347.92 USD | `-11.31%` | `15X Cross` |
| `1661` | `0xbf5a...88ba` | `SHORT` | 1,275,352.66 USD | `317.65` | `4091.80` | `4015.10` | `9852.91` | 24,430.37 USD | `+1.92%` | `20X Cross` |
| `1694` | `0xff31...ff6c` | `SHORT` | 1,244,681.00 USD | `310.00` | `4372.43` | `4015.10` | `4789.21` | 110,774.38 USD | `+8.90%` | `10X Isolated` |
| `1708` | `0xada6...6f88` | `LONG` | 1,237,053.51 USD | `308.10` | `4166.46` | `4015.10` | `1934.72` | -46,635.50 USD | `-3.77%` | `5X Cross` |
| `1754` | `0x354b...6425` | `LONG` | 1,185,163.34 USD | `295.20` | `4031.85` | `4015.10` | `0.000000` | -5,034.42 USD | `-0.42%` | `10X Cross` |
| `1877` | `0x50e2...d770` | `LONG` | 1,085,416.96 USD | `270.37` | `4243.58` | `4015.10` | `2562.13` | -61,909.50 USD | `-5.70%` | `20X Cross` |
| `1893` | `0x4c92...4f17` | `SHORT` | 1,070,909.48 USD | `266.72` | `4260.98` | `4015.10` | `6512.91` | 65,582.76 USD | `+6.12%` | `20X Cross` |
| `1953` | `0xd346...c4f3` | `LONG` | 1,024,548.32 USD | `255.17` | `4188.66` | `4015.10` | `3310.45` | -44,288.18 USD | `-4.32%` | `5X Isolated` |
| `1999` | `0x1581...463b` | `LONG` | 1,003,775.00 USD | `250.00` | `4003.77` | `4015.10` | `3562.34` | 2,831.41 USD | `+0.28%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.96` (Vol: 346,900.00 USD, Dist: `+2.03%`) | Long MP=`3936.30` (Vol: 356,200.00 USD, Dist: `--2.30%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.70%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.29%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.69%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.28%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.04%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.63%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,290,000.00 USD | 16,290,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,210,000.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.90` | 3,880,000.00 USD | 3,880,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,070,000.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 3,840,000.00 USD | 3,840,000.00 USD | 69,680.00 USD | 0.00 USD | 11,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 16,010,000.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.10` | 3,760,000.00 USD | 3,760,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,910,000.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.20` | 3,720,000.00 USD | 3,720,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,720,000.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.30` | 3,680,000.00 USD | 3,680,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,610,000.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.40` | 3,650,000.00 USD | 3,650,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,480,000.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.50` | 3,610,000.00 USD | 3,610,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,410,000.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.60` | 3,600,000.00 USD | 3,600,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,380,000.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.70` | 3,590,000.00 USD | 3,590,000.00 USD | 14,200.00 USD | 0.00 USD | 916.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,360,000.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.80` | 3,570,000.00 USD | 3,570,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,330,000.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,290,000.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,270,000.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,260,000.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,890,000.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,410,000.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,870,000.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.60` | 3,560,000.00 USD | 3,560,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,550,000.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.70` | 3,560,000.00 USD | 3,560,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,240,000.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.80` | 3,470,000.00 USD | 3,470,000.00 USD | 127,460.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,960,000.00 USD | 12,960,000.00 USD | 183,740.00 USD | 0.00 USD | 74,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.90` | 3,320,000.00 USD | 3,320,000.00 USD | 214,000.00 USD | 0.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,700,000.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.00` | 3,080,000.00 USD | 3,080,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,160,000.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.10` | 2,910,000.00 USD | 2,910,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,740,000.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.20` | 2,770,000.00 USD | 2,770,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,200,000.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.30` | 2,670,000.00 USD | 2,670,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,860,000.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3885.40` | 2,540,000.00 USD | 2,540,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,720,000.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.50` | 2,500,000.00 USD | 2,500,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,610,000.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.60` | 2,470,000.00 USD | 2,470,000.00 USD | 64,720.00 USD | 0.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,480,000.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.70` | 2,400,000.00 USD | 2,400,000.00 USD | 11,950.00 USD | 0.00 USD | 133.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,370,000.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.80` | 2,390,000.00 USD | 2,390,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,280,000.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,230,000.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,190,000.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,160,000.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,440,000.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,490,000.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,600,000.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.60` | 2,380,000.00 USD | 2,380,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,760,000.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.70` | 2,310,000.00 USD | 2,310,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,300,000.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.80` | 2,120,000.00 USD | 2,120,000.00 USD | 305,210.00 USD | 0.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,640,000.00 USD | 5,640,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.90` | 1,760,000.00 USD | 1,760,000.00 USD | 360,350.00 USD | 0.00 USD | 57,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,150,000.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.00` | 1,350,000.00 USD | 1,350,000.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,180,000.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.10` | 960,390.00 USD | 960,390.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.20` | 749,080.00 USD | 749,080.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.30` | 458,960.00 USD | 458,960.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3967.40` | 303,330.00 USD | 303,330.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.50` | 253,240.00 USD | 253,240.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.60` | 158,650.00 USD | 158,650.00 USD | 93,210.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.70` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.80` | 19,950.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.50` | 29,250.00 USD | 29,250.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.70` | 512,670.00 USD | 512,670.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.80` | 1,010,000.00 USD | 1,010,000.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.90` | 1,320,000.00 USD | 1,320,000.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.00` | 1,590,000.00 USD | 1,590,000.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.10` | 1,780,000.00 USD | 1,780,000.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.20` | 2,030,000.00 USD | 2,030,000.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4127.30` | 2,120,000.00 USD | 2,120,000.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4131.40` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.50` | 2,260,000.00 USD | 2,260,000.00 USD | 122,580.00 USD | 0.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 2,340,000.00 USD | 2,340,000.00 USD | 71,850.00 USD | 0.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.70` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.80` | 2,380,000.00 USD | 2,380,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.50` | 2,430,000.00 USD | 2,430,000.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.60` | 2,530,000.00 USD | 2,530,000.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.70` | 2,690,000.00 USD | 2,690,000.00 USD | 131,510.00 USD | 0.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 249,690.00 USD | 0.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.80` | 2,910,000.00 USD | 2,910,000.00 USD | 197,110.00 USD | 0.00 USD | 27,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.90` | 3,080,000.00 USD | 3,080,000.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.00` | 3,190,000.00 USD | 3,190,000.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.10` | 3,310,000.00 USD | 3,310,000.00 USD | 122,050.00 USD | 0.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.20` | 3,400,000.00 USD | 3,400,000.00 USD | 65,640.00 USD | 0.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4209.30` | 3,440,000.00 USD | 3,440,000.00 USD | 22,630.00 USD | 0.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4213.40` | 3,460,000.00 USD | 3,460,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.50` | 3,510,000.00 USD | 3,510,000.00 USD | 45,740.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.60` | 3,550,000.00 USD | 3,550,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.70` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.80` | 3,560,000.00 USD | 3,560,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4414.30` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 674.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4418.40` | 3,590,000.00 USD | 3,590,000.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.50` | 3,620,000.00 USD | 3,620,000.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.60` | 3,660,000.00 USD | 3,660,000.00 USD | 38,880.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.70` | 3,730,000.00 USD | 3,730,000.00 USD | 62,490.00 USD | 0.00 USD | 8,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.20` | 3,750,000.00 USD | 3,750,000.00 USD | 16,560.00 USD | 0.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,300,000.00 USD | 16,300,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,390,000.00 USD | 16,390,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,570,000.00 USD | 16,570,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.90` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 37,670.00 USD | 0.00 USD | 4,330.00 USD |
| `7D` | `3619.70` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3623.00` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 69,680.00 USD | 0.00 USD | 11,270.00 USD |
| `7D` | `3623.90` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3627.10` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 35,590.00 USD | 0.00 USD | 5,730.00 USD |
| `7D` | `3628.10` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3631.20` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 31,790.00 USD | 0.00 USD | 6,070.00 USD |
| `7D` | `3632.30` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3635.30` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 34,680.00 USD | 0.00 USD | 1,320.00 USD |
| `7D` | `3636.50` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3639.40` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 26,220.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3640.70` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.50` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 6,610.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `3644.90` | 15,410,000.00 USD | 0.00 USD | 15,410,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.60` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 12,080.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3649.10` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.70` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 14,200.00 USD | 0.00 USD | 916.56 USD |
| `7D` | `3653.30` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.80` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.60` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 2,810.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `3854.90` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.70` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 81,940.00 USD | 0.00 USD | 3,660.00 USD |
| `7D` | `3859.10` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 272,330.00 USD | 0.00 USD | 14,420.00 USD |
| `1D` | `3860.80` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 127,460.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `3863.30` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 183,740.00 USD | 0.00 USD | 74,000.00 USD |
| `1D` | `3864.90` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 214,000.00 USD | 0.00 USD | 27,300.00 USD |
| `7D` | `3867.50` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3869.00` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 144,700.00 USD | 0.00 USD | 21,610.00 USD |
| `7D` | `3871.70` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 374,120.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3873.10` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 126,020.00 USD | 0.00 USD | 17,270.00 USD |
| `7D` | `3875.90` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3877.20` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 99,080.00 USD | 0.00 USD | 4,780.00 USD |
| `7D` | `3880.10` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3881.30` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 105,320.00 USD | 0.00 USD | 22,610.00 USD |
| `7D` | `3884.30` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3885.40` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 22,630.00 USD | 0.00 USD | 12,350.00 USD |
| `7D` | `3888.50` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.50` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `3892.70` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.60` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 64,720.00 USD | 0.00 USD | 5,370.00 USD |
| `7D` | `3896.90` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.70` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 11,950.00 USD | 0.00 USD | 133.60 USD |
| `7D` | `3901.10` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.80` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.60` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 55,890.00 USD | 0.00 USD | 12,860.00 USD |
| `7D` | `3934.70` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.70` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 177,090.00 USD | 0.00 USD | 7,390.00 USD |
| `7D` | `3938.90` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 625,340.00 USD | 0.00 USD | 34,610.00 USD |
| `1D` | `3942.80` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 305,210.00 USD | 0.00 USD | 53,660.00 USD |
| `7D` | `3943.10` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 376,840.00 USD | 0.00 USD | 104,290.00 USD |
| `1D` | `3946.90` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 360,350.00 USD | 0.00 USD | 57,110.00 USD |
| `7D` | `3947.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD |
| `1D` | `3951.00` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 346,950.00 USD | 0.00 USD | 38,390.00 USD |
| `7D` | `3951.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 891,840.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3955.10` | 960,390.00 USD | 0.00 USD | 960,390.00 USD | 181,840.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3959.20` | 749,080.00 USD | 0.00 USD | 749,080.00 USD | 275,140.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3963.30` | 458,960.00 USD | 0.00 USD | 458,960.00 USD | 108,590.00 USD | 0.00 USD | 47,040.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3967.40` | 303,330.00 USD | 0.00 USD | 303,330.00 USD | 36,900.00 USD | 0.00 USD | 13,190.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.50` | 253,240.00 USD | 0.00 USD | 253,240.00 USD | 77,300.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.60` | 158,650.00 USD | 0.00 USD | 158,650.00 USD | 93,210.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.70` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.80` | 19,950.00 USD | 0.00 USD | 19,950.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4017.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4018.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4094.50` | 29,250.00 USD | 29,250.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4098.60` | 208,440.00 USD | 208,440.00 USD | 0.00 USD | 168,070.00 USD | 0.00 USD | 11,120.00 USD |
| `1D` | `4102.70` | 512,670.00 USD | 512,670.00 USD | 0.00 USD | 255,730.00 USD | 0.00 USD | 48,490.00 USD |
| `7D` | `4102.70` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 101,020.00 USD |
| `1D` | `4106.80` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 441,840.00 USD | 0.00 USD | 52,210.00 USD |
| `7D` | `4106.90` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD |
| `1D` | `4110.90` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 278,400.00 USD | 0.00 USD | 37,810.00 USD |
| `7D` | `4111.10` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4115.00` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 229,730.00 USD | 0.00 USD | 34,530.00 USD |
| `7D` | `4115.30` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4119.10` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 185,530.00 USD | 0.00 USD | 9,560.00 USD |
| `7D` | `4119.50` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4123.20` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 207,400.00 USD | 0.00 USD | 39,080.00 USD |
| `7D` | `4123.70` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4127.30` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 27,400.00 USD |
| `7D` | `4127.90` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4131.40` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,390.00 USD |
| `7D` | `4132.10` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.50` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `4136.30` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.60` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 71,850.00 USD | 0.00 USD | 5,440.00 USD |
| `7D` | `4140.50` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.70` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.80` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,940,000.00 USD | 11,940,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.50` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.60` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 91,790.00 USD | 0.00 USD | 5,360.00 USD |
| `7D` | `4182.50` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 35,310.00 USD |
| `1D` | `4184.70` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 131,510.00 USD | 0.00 USD | 27,230.00 USD |
| `7D` | `4186.70` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 64,330.00 USD |
| `1D` | `4188.80` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 197,110.00 USD | 0.00 USD | 27,480.00 USD |
| `7D` | `4190.90` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 577,660.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.90` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 150,560.00 USD | 0.00 USD | 18,220.00 USD |
| `7D` | `4195.10` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4197.00` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 90,920.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4199.30` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4201.10` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 122,050.00 USD | 0.00 USD | 4,310.00 USD |
| `7D` | `4203.50` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4205.20` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 65,640.00 USD | 0.00 USD | 23,090.00 USD |
| `7D` | `4207.70` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4209.30` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,280.00 USD |
| `7D` | `4211.90` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4213.40` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 7,480.00 USD |
| `7D` | `4216.10` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.50` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 45,740.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `4220.30` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.60` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.70` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.80` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,240,000.00 USD | 15,240,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,340,000.00 USD | 15,340,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,810,000.00 USD | 15,810,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4414.30` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 674.96 USD |
| `7D` | `4417.70` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4418.40` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 1,790.00 USD |
| `7D` | `4421.90` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.50` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | 2,630.00 USD |
| `7D` | `4426.10` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4426.60` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 38,880.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `4430.30` | 16,150,000.00 USD | 16,150,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4430.70` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 62,490.00 USD | 0.00 USD | 8,160.00 USD |
| `1D` | `4433.20` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 16,560.00 USD | 0.00 USD | 3,720.00 USD |
| `7D` | `4434.50` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,570,000.00 USD | 16,570,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `273.85M` | Total OI Tokens: `68,152.5 PAXG`
  * 1h OI Change: `-0.39%` | 4h OI Change: `-0.18%` | 24h OI Change: `-0.15%`
  * Exchange Breakdown: Binance=`107.03M` | Bybit=`20.06M` | OKX=`-` | Hyperliquid=`24.59M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.36K` | Last 24h: `25.45K` | Last 3d: `95.42K` | Last 7d: `223.50K`
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
| `15M` | `PAXG` | `45.93%` | `54.07%` | `0.85` | 920,730.00 USD |
| `15M` | `Binance` | `43.6%` | `56.4%` | `0.77` | 453,160.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `36.14%` | `63.86%` | `0.57` | 41,890.00 USD |
| `15M` | `KuCoin` | `47.49%` | `52.51%` | `0.90` | 87,760.00 USD |
| `15M` | `Gate` | `50.1%` | `49.9%` | `1.00` | 20,480.00 USD |
| `15M` | `Bitget` | `35.61%` | `64.39%` | `0.55` | 223,450.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `41.58%` | `58.42%` | `0.71` | 2,700.00 USD |
| `15M` | `Bitunix` | `47.69%` | `52.31%` | `0.91` | 10,000.00 USD |
| `15M` | `Hyperliquid` | `27.93%` | `72.07%` | `0.39` | 6,670.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.32%` | `0.68%` | `146.06` | 69,190.00 USD |
| `15M` | `HTX` | `45.38%` | `54.62%` | `0.83` | 2,260.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 68.37 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 651.35 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.07%` | `50.93%` | `0.96` | 2,450.00 USD |
| `15M` | `Whale Positions` | `43.6%` | `56.4%` | `0.77` | 453,160.00 USD |
| `15M` | `Global Accounts` | `45.93%` | `54.07%` | `0.85` | 920,730.00 USD |
| `1H` | `PAXG` | `46.61%` | `53.39%` | `0.87` | 9,460,000.00 USD |
| `1H` | `Binance` | `41.1%` | `58.9%` | `0.70` | 1,530,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `42.08%` | `57.92%` | `0.73` | 679,430.00 USD |
| `1H` | `KuCoin` | `49.9%` | `50.1%` | `1.00` | 27,530.00 USD |
| `1H` | `Gate` | `41.5%` | `58.5%` | `0.71` | 543,050.00 USD |
| `1H` | `Bitget` | `30.35%` | `69.65%` | `0.44` | 516,920.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `52.14%` | `47.86%` | `1.09` | 5,120,000.00 USD |
| `1H` | `Bitunix` | `43.03%` | `56.97%` | `0.76` | 205,140.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.26%` | `51.74%` | `0.93` | 583,990.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.93%` | `80.07%` | `0.25` | 238,100.00 USD |
| `1H` | `HTX` | `72.51%` | `27.49%` | `2.64` | 7,360.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `79.91%` | `20.09%` | `3.98` | 4,620.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `41.1%` | `58.9%` | `0.70` | 1,530,000.00 USD |
| `1H` | `Global Accounts` | `46.61%` | `53.39%` | `0.87` | 9,460,000.00 USD |
| `4H` | `PAXG` | `51.78%` | `48.22%` | `1.07` | 18,140,000.00 USD |
| `4H` | `Binance` | `50.62%` | `49.38%` | `1.03` | 10,680,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `46.09%` | `53.91%` | `0.85` | 687,390.00 USD |
| `4H` | `KuCoin` | `53.27%` | `46.73%` | `1.14` | 1,420,000.00 USD |
| `4H` | `Gate` | `50.59%` | `49.41%` | `1.02` | 301,300.00 USD |
| `4H` | `Bitget` | `50.22%` | `49.78%` | `1.01` | 2,290,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `48.62%` | `51.38%` | `0.95` | 125,720.00 USD |
| `4H` | `Bitunix` | `40.11%` | `59.89%` | `0.67` | 360,950.00 USD |
| `4H` | `Hyperliquid` | `41.71%` | `58.29%` | `0.72` | 878,690.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `79.05%` | `20.95%` | `3.77` | 1,190,000.00 USD |
| `4H` | `HTX` | `61.58%` | `38.42%` | `1.60` | 49,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `28.31%` | `71.69%` | `0.39` | 57,470.00 USD |
| `4H` | `Aster` | `85.34%` | `14.66%` | `5.82` | 26,380.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.16%` | `59.84%` | `0.67` | 73,340.00 USD |
| `4H` | `Whale Positions` | `50.62%` | `49.38%` | `1.03` | 10,680,000.00 USD |
| `4H` | `Global Accounts` | `51.78%` | `48.22%` | `1.07` | 18,140,000.00 USD |


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
| `5m` | -25,670.00 USD | 16,300.00 USD | **`DISTRIBUTION`** |
| `15m` | -72,330.00 USD | -60,230.00 USD | **`DISTRIBUTION`** |
| `30m` | 76,960.00 USD | -64,480.00 USD | **`ACCUMULATION`** |
| `1h` | 284,250.00 USD | -60,030.00 USD | **`ACCUMULATION`** |
| `2h` | -955,550.00 USD | 147,710.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,070,000.00 USD | 66,960.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,680,000.00 USD | 51,530.00 USD | **`DISTRIBUTION`** |
| `8h` | -950,460.00 USD | 556,600.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,330,000.00 USD | 1,500,000.00 USD | **`ACCUMULATION`** |
| `24h` | -901,700.00 USD | 1,830,000.00 USD | **`ACCUMULATION`** |
| `1w` | -9,060,000.00 USD | -8,260,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,890,000.00 USD | -71,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-25.67K` | 15m=`-72.33K` | 1h=`+284.25K` | 24h=`-901.70K`
* Futures Capital Netflows: 5m=`+16.30K` | 15m=`-60.23K` | 1h=`-60.03K` | 24h=`+1.83M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4017.82` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.52` (Risk Distance: `8.30` pts)
  * +2.5R Take Profit: `4038.56`
  * Mathematical Lot Sizing: **`1.20 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4025.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4033.39` (Risk Distance: `8.30` pts)
  * +2.5R Take Profit: `4004.35`
  * Mathematical Lot Sizing: **`1.20 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4043.96`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
