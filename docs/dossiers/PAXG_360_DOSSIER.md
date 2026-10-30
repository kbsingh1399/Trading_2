# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 08:54:59 IST` (`2026-10-30 03:24:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3994.08` | **Live Ask Quote**: `3994.16` | **Mid Price**: `3994.12`
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
  * Session VWAP: `4005.27` | VWAP Z-Score: `-2.50` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `8.23` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.31` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4019.18` | Lower -3.00σ Band: `3991.37`
  * Upper +2.51σ Band: `4016.90` | Lower -2.51σ Band: `3993.64`
  * Upper +2.01σ Band: `4014.59` | Lower -2.01σ Band: `3995.96`
  * Upper +2.00σ Band: `4014.54` | Lower -2.00σ Band: `3996.01`
  * Upper +1.28σ Band: `4011.21` | Lower -1.28σ Band: `3999.34`
  * Upper +1.00σ Band: `4009.91` | Lower -1.00σ Band: `4000.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4002.60` | EMA-20=`4007.41` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4014.50` (Slope: `+0.0000`) | EMA-100=`4022.06`
  * Institutional Anchors: EMA-144=`4025.47` | EMA-200=`4027.13` (Slope: `-0.0703`) | EMA-233=`4028.37`
- **Range Boundaries**: 24H High=`4054.55` | 24H Low=`3992.22` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.16` (Distance: `-0.45%`)
  * Point of Control (POC) = `4006.79` (Distance: `-0.29%`)
  * Value Area Low (VAL) = `3998.71` (Distance: `-0.09%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4049.63` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3992.22`
  * London Session (08:00-16:00 UTC): High=`4010.10` | Low=`3978.14`
  * New York Session (13:00-21:00 UTC): High=`4018.08` | Low=`3970.16`
  * Initial Balance (First Hour): IB High=`4006.10` | IB Low=`3982.14`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3978.14` - `4010.10`
  * Optimal Trade Entry (OTE 0.705): `4002.11`
  * Structural Invalidation Anchor (0.786): `4026.07`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4002.34` | `4004.01` | `4001.89` | `4002.36` | `90` | 361,392.98 USD | 92,223.91 USD | `+25.52%` | -351,218.72 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4002.37` | `4003.05` | `3999.30` | `4000.58` | `179` | 717,099.13 USD | -420,055.39 USD | `-58.58%` | -771,274.11 USD | `-3.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4000.58` | `4002.42` | `3999.25` | `4000.31` | `85` | 339,634.70 USD | -42,805.29 USD | `-12.60%` | -814,079.40 USD | `-0.12` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4006.74` | `4007.76` | `4004.07` | `4004.53` | `104` | 417,614.09 USD | 49,319.38 USD | `+11.81%` | -474,774.50 USD | `+0.59` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4004.53` | `4005.00` | `4001.35` | `4002.36` | `218` | 870,882.15 USD | 130,287.72 USD | `+14.96%` | -344,486.78 USD | `+0.95` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4002.37` | `4003.05` | `3999.25` | `4000.30` | `264` | 1,055,185.71 USD | -464,408.79 USD | `-44.01%` | -808,895.58 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4008.10` | `4013.95` | `3999.00` | `4008.79` | `1,150` | 4,606,132.72 USD | -286,613.67 USD | `-6.22%` | -396,780.69 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4008.80` | `4014.92` | `4001.35` | `4002.36` | `667` | 2,671,119.24 USD | -91,693.11 USD | `-3.43%` | -488,473.81 USD | `-0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4002.37` | `4003.05` | `3999.25` | `4000.30` | `264` | 1,055,173.71 USD | -464,396.79 USD | `-44.01%` | -952,870.60 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3999.00` | `4000.31` | `3,221` | 12,908,336.09 USD | -1,583,560.18 USD | `-12.27%` | -951,334.48 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -910,560.46 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | -478,447.19 USD | `+1.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3999.00` | `4000.31` | `3,221` | 12,908,336.09 USD | -1,583,560.18 USD | `-12.27%` | -951,334.48 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,928,144.84 USD | `6,489.82` | `4185.46` | `3994.20` | `30920.60` | 1,234,806.17 USD | `+4.76%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,209,297.89 USD | `6,311.32` | `4129.79` | `3994.20` | `14026.32` | 855,153.32 USD | `+3.39%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,449,661.11 USD | `5,869.90` | `4228.86` | `3994.20` | `28520.64` | 1,373,360.82 USD | `+5.86%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,291,483.07 USD | `4,828.91` | `4157.43` | `3994.20` | `2331.07` | -784,399.25 USD | `-4.07%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,110,538.19 USD | `3,532.67` | `4128.54` | `3994.20` | `597.31` | -474,225.91 USD | `-3.36%` | `3X Cross` |
| `155` | `0x7a6d...f79c` | `SHORT` | 13,054,223.98 USD | `3,268.21` | `4228.94` | `3994.20` | `4399.85` | 766,855.15 USD | `+5.87%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,586,080.40 USD | `2,900.00` | `4364.92` | `3994.20` | `4235.84` | 1,072,195.93 USD | `+9.25%` | `20X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,788,780.00 USD | `2,200.00` | `4112.20` | `3994.20` | `4331.33` | 258,074.59 USD | `+2.94%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,787,460.00 USD | `2,200.00` | `4176.09` | `3994.20` | `2730.84` | -399,959.30 USD | `-4.55%` | `25X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,891,402.02 USD | `1,975.37` | `4048.55` | `3994.20` | `6605.46` | 105,989.70 USD | `+1.34%` | `6X Cross` |
| `360` | `0xc26c...b8f4` | `LONG` | 6,310,801.47 USD | `1,579.95` | `4075.62` | `3994.20` | `0.000000` | -128,495.50 USD | `-2.04%` | `1X Cross` |
| `494` | `0x354b...6425` | `LONG` | 4,418,799.82 USD | `1,106.28` | `4004.98` | `3994.20` | `0.000000` | -11,820.80 USD | `-0.27%` | `10X Cross` |
| `546` | `0x63da...8add` | `LONG` | 3,994,300.00 USD | `1,000.00` | `4021.46` | `3994.20` | `3564.29` | -27,160.96 USD | `-0.68%` | `25X Cross` |
| `556` | `0xf3dc...1672` | `LONG` | 3,931,570.88 USD | `984.27` | `4018.39` | `3994.20` | `2888.19` | -23,615.81 USD | `-0.60%` | `20X Cross` |
| `569` | `0x9aa5...58af` | `LONG` | 3,881,709.79 USD | `971.64` | `4279.98` | `3994.20` | `0.000000` | -276,899.29 USD | `-7.13%` | `20X Cross` |
| `661` | `0x4a20...3c26` | `LONG` | 3,344,825.62 USD | `837.40` | `4599.73` | `3994.20` | `0.000000` | -506,994.76 USD | `-15.16%` | `20X Cross` |
| `822` | `0x0fac...7a0a` | `LONG` | 2,742,027.04 USD | `686.49` | `4290.34` | `3994.20` | `1414.61` | -203,231.67 USD | `-7.41%` | `25X Cross` |
| `892` | `0xd8c5...99b0` | `SHORT` | 2,518,393.90 USD | `630.35` | `4175.35` | `3994.20` | `33779.81` | 113,562.99 USD | `+4.51%` | `4X Cross` |
| `904` | `0x625e...a354` | `SHORT` | 2,476,838.00 USD | `620.00` | `4122.81` | `3994.20` | `4342.43` | 79,309.03 USD | `+3.20%` | `20X Cross` |
| `935` | `0xeae3...e8ad` | `SHORT` | 2,396,640.00 USD | `600.00` | `4104.77` | `3994.20` | `4325.45` | 66,225.11 USD | `+2.76%` | `20X Cross` |
| `940` | `0xf285...fa82` | `LONG` | 2,389,014.40 USD | `598.11` | `4146.45` | `3994.20` | `3891.43` | -91,005.16 USD | `-3.81%` | `25X Cross` |
| `949` | `0x12f7...8750` | `LONG` | 2,339,104.82 USD | `585.61` | `4082.77` | `3994.20` | `2803.18` | -51,812.16 USD | `-2.22%` | `10X Cross` |
| `1083` | `0x413c...886c` | `LONG` | 1,997,300.00 USD | `500.00` | `4010.43` | `3994.20` | `0.000000` | -7,916.23 USD | `-0.40%` | `2X Cross` |
| `1090` | `0x61ce...a62b` | `SHORT` | 1,987,227.98 USD | `497.50` | `4071.66` | `3994.20` | `4728.34` | 38,440.81 USD | `+1.93%` | `20X Cross` |
| `1165` | `0x2edd...8179` | `LONG` | 1,878,894.16 USD | `469.89` | `4164.68` | `3998.20` | `0.000000` | -78,038.36 USD | `-4.15%` | `10X Cross` |
| `1205` | `0xead5...69f2` | `LONG` | 1,812,821.30 USD | `453.78` | `4220.88` | `3994.20` | `3539.13` | -102,546.76 USD | `-5.66%` | `5X Isolated` |
| `1264` | `0x7a6d...f79c` | `SHORT` | 1,712,787.76 USD | `428.38` | `4136.09` | `3998.20` | `5405.55` | 59,027.25 USD | `+3.45%` | `10X Cross` |
| `1280` | `0x46fc...1195` | `LONG` | 1,685,082.78 USD | `421.86` | `4053.56` | `3994.20` | `2186.86` | -24,959.47 USD | `-1.48%` | `20X Cross` |
| `1343` | `0x6d15...d374` | `LONG` | 1,597,960.00 USD | `400.00` | `4068.25` | `3994.20` | `3842.00` | -29,340.00 USD | `-1.84%` | `25X Cross` |
| `1344` | `0xee02...309d` | `SHORT` | 1,597,720.00 USD | `400.00` | `4438.84` | `3994.20` | `4227.07` | 177,818.60 USD | `+11.13%` | `25X Isolated` |
| `1366` | `0x02a7...fe9f` | `SHORT` | 1,557,777.00 USD | `390.00` | `4055.02` | `3994.20` | `4306.88` | 23,682.25 USD | `+1.52%` | `25X Cross` |
| `1369` | `0x51f6...2b39` | `LONG` | 1,555,849.41 USD | `389.07` | `4229.65` | `3998.20` | `408.57` | -89,785.16 USD | `-5.77%` | `10X Cross` |
| `1420` | `0x7e77...b8d2` | `SHORT` | 1,518,176.00 USD | `380.00` | `4131.92` | `3994.20` | `4293.69` | 51,953.64 USD | `+3.42%` | `20X Cross` |
| `1448` | `0x9c06...0560` | `LONG` | 1,490,916.01 USD | `373.26` | `4018.98` | `3994.20` | `0.000000` | -9,215.79 USD | `-0.62%` | `25X Cross` |
| `1449` | `0x72c2...9b37` | `LONG` | 1,490,435.66 USD | `373.13` | `4000.98` | `3994.20` | `3778.23` | -2,457.85 USD | `-0.16%` | `13X Isolated` |
| `1483` | `0x781e...96b7` | `SHORT` | 1,443,347.27 USD | `360.91` | `4363.71` | `3998.20` | `13745.76` | 131,555.24 USD | `+9.11%` | `10X Cross` |
| `1491` | `0xaa44...b844` | `LONG` | 1,437,984.00 USD | `360.00` | `4043.10` | `3994.20` | `2820.84` | -17,533.63 USD | `-1.22%` | `4X Cross` |
| `1597` | `0xa41f...d50a` | `LONG` | 1,314,203.59 USD | `328.96` | `4468.89` | `3994.20` | `3802.35` | -155,894.26 USD | `-11.86%` | `15X Cross` |
| `1609` | `0x7fda...17d1` | `SHORT` | 1,301,994.47 USD | `325.91` | `4013.13` | `3994.20` | `30149.37` | 5,909.08 USD | `+0.45%` | `20X Cross` |
| `1641` | `0xbf5a...88ba` | `SHORT` | 1,269,031.33 USD | `317.65` | `4091.80` | `3994.20` | `9746.02` | 30,751.71 USD | `+2.42%` | `20X Cross` |
| `1681` | `0xff31...ff6c` | `SHORT` | 1,238,512.00 USD | `310.00` | `4372.43` | `3994.20` | `4789.36` | 116,943.38 USD | `+9.44%` | `10X Isolated` |
| `1710` | `0xada6...6f88` | `LONG` | 1,212,291.61 USD | `303.50` | `4166.46` | `3994.20` | `1800.85` | -52,221.25 USD | `-4.31%` | `5X Cross` |
| `1868` | `0x50e2...d770` | `LONG` | 1,079,928.51 USD | `270.37` | `4243.58` | `3994.20` | `2562.28` | -67,397.95 USD | `-6.24%` | `20X Cross` |
| `1877` | `0x4c92...4f17` | `SHORT` | 1,065,601.74 USD | `266.72` | `4260.98` | `3994.20` | `6506.45` | 70,890.49 USD | `+6.65%` | `20X Cross` |
| `1946` | `0xd346...c4f3` | `LONG` | 1,019,240.71 USD | `255.17` | `4188.66` | `3994.20` | `3310.61` | -49,595.80 USD | `-4.87%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.85` (Vol: 274,500.00 USD, Dist: `+2.76%`) | Long MP=`3936.99` (Vol: 378,100.00 USD, Dist: `--1.56%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+2.80%`) | Long MP=`3935.76` (Vol: 350,100.00 USD, Dist: `--1.59%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 353,400.00 USD, Dist: `+2.80%`) | Long MP=`3935.76` (Vol: 350,100.00 USD, Dist: `--1.59%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.80%`) | Long MP=`3923.02` (Vol: 965,800.00 USD, Dist: `--1.91%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,240,000.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,170,000.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.40` | 3,900,000.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,030,000.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.50` | 3,870,000.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,960,000.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.60` | 3,790,000.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,870,000.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,740,000.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,680,000.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.80` | 3,700,000.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,570,000.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.90` | 3,670,000.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,440,000.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.00` | 3,630,000.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,370,000.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.10` | 3,610,000.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,330,000.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.20` | 3,600,000.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,310,000.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.30` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,280,000.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,250,000.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,220,000.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,210,000.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,850,000.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,360,000.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,830,000.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.10` | 3,580,000.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,510,000.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,580,000.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,200,000.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.30` | 3,490,000.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,910,000.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.40` | 3,350,000.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,650,000.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,120,000.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,110,000.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.60` | 2,940,000.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,710,000.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.70` | 2,780,000.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,170,000.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.80` | 2,700,000.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,830,000.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.90` | 2,550,000.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,690,000.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.00` | 2,510,000.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,580,000.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.10` | 2,480,000.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,450,000.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.20` | 2,440,000.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,340,000.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.30` | 2,400,000.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,250,000.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,210,000.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,160,000.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,140,000.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,410,000.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,460,000.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,570,000.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.10` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,730,000.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.20` | 2,320,000.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,270,000.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.30` | 2,150,000.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,600,000.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,790,000.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,110,000.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.50` | 1,360,000.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,140,000.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 955,040.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.70` | 752,230.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.80` | 487,860.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.90` | 298,610.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.00` | 243,280.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 167,990.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.20` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.30` | 23,310.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 300.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.40` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD |
| `7D` | `3619.70` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.50` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `3623.90` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3626.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3628.10` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3630.70` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD |
| `7D` | `3632.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3634.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD |
| `7D` | `3636.50` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3638.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3640.70` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.00` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3644.90` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `3649.10` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `3653.30` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3854.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.20` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3859.10` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD |
| `1D` | `3860.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD |
| `7D` | `3863.30` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD |
| `1D` | `3864.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD |
| `7D` | `3867.50` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD |
| `7D` | `3871.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3872.60` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3875.90` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3876.70` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3880.10` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3880.80` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `3884.30` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3884.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3888.50` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.00` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `3896.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.20` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `3901.10` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD |
| `7D` | `3938.90` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD |
| `1D` | `3942.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD |
| `7D` | `3943.10` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD |
| `1D` | `3946.40` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `3947.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD |
| `1D` | `3950.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD |
| `7D` | `3951.50` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.60` | 955,040.00 USD | 0.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3958.70` | 752,230.00 USD | 0.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3962.80` | 487,860.00 USD | 0.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3966.90` | 298,610.00 USD | 0.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.00` | 243,280.00 USD | 0.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.10` | 167,990.00 USD | 0.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.20` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.30` | 23,310.00 USD | 0.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 0.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 0.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD |
| `7D` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD |
| `1D` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 0.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD |
| `1D` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD |
| `7D` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD |
| `7D` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD |
| `7D` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD |
| `7D` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD |
| `7D` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD |
| `7D` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD |
| `1D` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD |
| `7D` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD |
| `7D` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.94 USD |
| `7D` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD |
| `1D` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD |
| `7D` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.64M` | Total OI Tokens: `68,922.2 PAXG`
  * 1h OI Change: `-0.23%` | 4h OI Change: `+0.64%` | 24h OI Change: `+0.61%`
  * Exchange Breakdown: Binance=`107.57M` | Bybit=`20.72M` | OKX=`-` | Hyperliquid=`24.64M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.62K` | Last 24h: `27.84K` | Last 3d: `98.08K` | Last 7d: `223.34K`
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
| `15M` | `PAXG` | `59.49%` | `40.51%` | `1.47` | 2,080,000.00 USD |
| `15M` | `Binance` | `59.06%` | `40.94%` | `1.44` | 747,090.00 USD |
| `15M` | `OKX` | `64.38%` | `35.62%` | `1.81` | 384,180.00 USD |
| `15M` | `Bybit` | `56.9%` | `43.1%` | `1.32` | 189,870.00 USD |
| `15M` | `KuCoin` | `53.36%` | `46.64%` | `1.14` | 21,550.00 USD |
| `15M` | `Gate` | `61.73%` | `38.27%` | `1.61` | 19,210.00 USD |
| `15M` | `Bitget` | `53.88%` | `46.12%` | `1.17` | 281,610.00 USD |
| `15M` | `BingX` | `60.71%` | `39.29%` | `1.55` | 81,780.00 USD |
| `15M` | `MEXC` | `57.5%` | `42.5%` | `1.35` | 143,810.00 USD |
| `15M` | `Bitunix` | `62.71%` | `37.29%` | `1.68` | 87,450.00 USD |
| `15M` | `Hyperliquid` | `74.05%` | `25.95%` | `2.85` | 56,400.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 36,860.00 USD |
| `15M` | `Crypto.com` | `0.18%` | `99.82%` | `0.00` | 684.63 USD |
| `15M` | `WhiteBIT` | `69.92%` | `30.08%` | `2.32` | 29,610.00 USD |
| `15M` | `HTX` | `81.33%` | `18.67%` | `4.36` | 148.85 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `41.9%` | `58.1%` | `0.72` | 1,060.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 3,550.00 USD |
| `15M` | `Whale Positions` | `59.06%` | `40.94%` | `1.44` | 747,090.00 USD |
| `15M` | `Global Accounts` | `59.49%` | `40.51%` | `1.47` | 2,080,000.00 USD |
| `1H` | `PAXG` | `44.57%` | `55.43%` | `0.80` | 5,880,000.00 USD |
| `1H` | `Binance` | `40.4%` | `59.6%` | `0.68` | 3,120,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `60.08%` | `39.92%` | `1.51` | 873,120.00 USD |
| `1H` | `KuCoin` | `49.79%` | `50.21%` | `0.99` | 382,040.00 USD |
| `1H` | `Gate` | `29.87%` | `70.13%` | `0.43` | 194,340.00 USD |
| `1H` | `Bitget` | `43.16%` | `56.84%` | `0.76` | 631,070.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `26.96%` | `73.04%` | `0.37` | 15,260.00 USD |
| `1H` | `Bitunix` | `33.92%` | `66.08%` | `0.51` | 128,260.00 USD |
| `1H` | `Hyperliquid` | `68.48%` | `31.52%` | `2.17` | 119,990.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `53.79%` | `46.21%` | `1.16` | 314,570.00 USD |
| `1H` | `HTX` | `40.41%` | `59.59%` | `0.68` | 17,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `3.1%` | `96.9%` | `0.03` | 2,060.00 USD |
| `1H` | `Aster` | `0.6%` | `99.4%` | `0.01` | 51,360.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.09%` | `68.91%` | `0.45` | 35,570.00 USD |
| `1H` | `Whale Positions` | `40.4%` | `59.6%` | `0.68` | 3,120,000.00 USD |
| `1H` | `Global Accounts` | `44.57%` | `55.43%` | `0.80` | 5,880,000.00 USD |
| `4H` | `PAXG` | `47.54%` | `52.46%` | `0.91` | 25,070,000.00 USD |
| `4H` | `Binance` | `43.71%` | `56.29%` | `0.78` | 14,360,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `57.35%` | `42.65%` | `1.34` | 1,700,000.00 USD |
| `4H` | `KuCoin` | `50.49%` | `49.51%` | `1.02` | 1,600,000.00 USD |
| `4H` | `Gate` | `44.66%` | `55.34%` | `0.81` | 715,410.00 USD |
| `4H` | `Bitget` | `46.3%` | `53.7%` | `0.86` | 3,610,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `33.56%` | `66.44%` | `0.51` | 116,520.00 USD |
| `4H` | `Bitunix` | `38.66%` | `61.34%` | `0.63` | 443,050.00 USD |
| `4H` | `Hyperliquid` | `56.14%` | `43.86%` | `1.28` | 646,600.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `72.17%` | `27.83%` | `2.59` | 1,050,000.00 USD |
| `4H` | `HTX` | `68.37%` | `31.63%` | `2.16` | 255,130.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `83.68%` | `16.32%` | `5.13` | 330,600.00 USD |
| `4H` | `Aster` | `6.23%` | `93.77%` | `0.07` | 56,600.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.01%` | `54.99%` | `0.82` | 196,830.00 USD |
| `4H` | `Whale Positions` | `43.71%` | `56.29%` | `0.78` | 14,360,000.00 USD |
| `4H` | `Global Accounts` | `47.54%` | `52.46%` | `0.91` | 25,070,000.00 USD |


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
| `5m` | -4,750.00 USD | 23,830.00 USD | **`ACCUMULATION`** |
| `15m` | -58,130.00 USD | -10,980.00 USD | **`DISTRIBUTION`** |
| `30m` | -203,170.00 USD | -347,630.00 USD | **`DISTRIBUTION`** |
| `1h` | -230,560.00 USD | -410,940.00 USD | **`DISTRIBUTION`** |
| `2h` | -175,090.00 USD | -337,820.00 USD | **`DISTRIBUTION`** |
| `4h` | -45,000.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -972,690.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,110,000.00 USD | -787,510.00 USD | **`DISTRIBUTION`** |
| `12h` | -901,000.00 USD | -230,130.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,230,000.00 USD | -635,560.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,520,000.00 USD | -9,610,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,550,000.00 USD | -73,170,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-4.75K` | 15m=`-58.13K` | 1h=`-230.56K` | 24h=`-1.23M`
* Futures Capital Netflows: 5m=`+23.83K` | 15m=`-10.98K` | 1h=`-410.94K` | 24h=`-635.56K`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3998.71` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3988.72` (Risk Distance: `9.99` pts)
  * +2.5R Take Profit: `4023.69`
  * Mathematical Lot Sizing: **`1.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.15` (Risk Distance: `9.99` pts)
  * +2.5R Take Profit: `3988.18`
  * Mathematical Lot Sizing: **`1.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4026.07`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
