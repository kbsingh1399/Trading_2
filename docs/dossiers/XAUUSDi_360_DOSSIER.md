# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUUSD
**Canonical Key**: `XAUUSD` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Precious Metal`
**Timestamp**: `2026-10-30 08:54:59 IST` (`2026-10-30 03:24:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3994.08` | **Live Ask Quote**: `3994.16` | **Mid Price**: `3994.12`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
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
| `1205` | `0xead5...69f2` | `LONG` | 1,812,821.30 USD | `453.78` | `4220.88` | `3994.20` | `3539.13` | -102,546.76 USD | `-5.66%` | `5X Isolated` |
| `1280` | `0x46fc...1195` | `LONG` | 1,685,082.78 USD | `421.86` | `4053.56` | `3994.20` | `2186.86` | -24,959.47 USD | `-1.48%` | `20X Cross` |
| `1343` | `0x6d15...d374` | `LONG` | 1,597,960.00 USD | `400.00` | `4068.25` | `3994.20` | `3842.00` | -29,340.00 USD | `-1.84%` | `25X Cross` |
| `1344` | `0xee02...309d` | `SHORT` | 1,597,720.00 USD | `400.00` | `4438.84` | `3994.20` | `4227.07` | 177,818.60 USD | `+11.13%` | `25X Isolated` |
| `1366` | `0x02a7...fe9f` | `SHORT` | 1,557,777.00 USD | `390.00` | `4055.02` | `3994.20` | `4306.88` | 23,682.25 USD | `+1.52%` | `25X Cross` |
| `1420` | `0x7e77...b8d2` | `SHORT` | 1,518,176.00 USD | `380.00` | `4131.92` | `3994.20` | `4293.69` | 51,953.64 USD | `+3.42%` | `20X Cross` |
| `1448` | `0x9c06...0560` | `LONG` | 1,490,916.01 USD | `373.26` | `4018.98` | `3994.20` | `0.000000` | -9,215.79 USD | `-0.62%` | `25X Cross` |
| `1449` | `0x72c2...9b37` | `LONG` | 1,490,435.66 USD | `373.13` | `4000.98` | `3994.20` | `3778.23` | -2,457.85 USD | `-0.16%` | `13X Isolated` |
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
  * 24H Horizon: Short MP=`4091.67` (Vol: 135,400.00 USD, Dist: `+2.51%`) | Long MP=`3947.57` (Vol: 99,900.00 USD, Dist: `--1.10%`)
  * 48H Horizon: Short MP=`4110.38` (Vol: 300,700.00 USD, Dist: `+2.98%`) | Long MP=`3959.13` (Vol: 388,300.00 USD, Dist: `--0.81%`)
  * 3D Horizon: Short MP=`4110.38` (Vol: 300,700.00 USD, Dist: `+2.98%`) | Long MP=`3959.13` (Vol: 388,300.00 USD, Dist: `--0.81%`)
  * 7D Horizon: Short MP=`4082.49` (Vol: 552,000.00 USD, Dist: `+2.28%`) | Long MP=`3921.81` (Vol: 617,500.00 USD, Dist: `--1.75%`)
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
| `7D` | `3605.20` | 21,460,000.00 USD | 0.00 USD | 21,460,000.00 USD | 33,130.00 USD | 0.00 USD | 98,140.00 USD |
| `7D` | `3609.40` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 22,730.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3610.40` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 16,210.00 USD | 0.00 USD | 16,440.00 USD |
| `7D` | `3613.60` | 21,270,000.00 USD | 0.00 USD | 21,270,000.00 USD | 87,020.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3614.50` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,120.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `3617.80` | 21,110,000.00 USD | 0.00 USD | 21,110,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.60` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 19,950.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 58,610.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.70` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 22,710.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.20` | 20,770,000.00 USD | 0.00 USD | 20,770,000.00 USD | 35,220.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3626.80` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 14,290.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.40` | 20,670,000.00 USD | 0.00 USD | 20,670,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 31,880.00 USD | 0.00 USD | 49,910.00 USD |
| `7D` | `3634.60` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.00` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 30,630.00 USD | 0.00 USD | 18,910.00 USD |
| `7D` | `3638.80` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.10` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.00` | 20,390,000.00 USD | 0.00 USD | 20,390,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.20` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 17,040.00 USD | 0.00 USD | 6,960.00 USD |
| `7D` | `3647.20` | 20,350,000.00 USD | 0.00 USD | 20,350,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3647.30` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 2,430.00 USD | 0.00 USD | 7,140.00 USD |
| `1D` | `3651.40` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 7,240.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `3655.50` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3655.60` | 20,310,000.00 USD | 0.00 USD | 20,310,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,270,000.00 USD | 0.00 USD | 20,270,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,050,000.00 USD | 0.00 USD | 20,050,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,610,000.00 USD | 0.00 USD | 19,610,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,810,000.00 USD | 0.00 USD | 17,810,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.20` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `3848.80` | 17,490,000.00 USD | 0.00 USD | 17,490,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.30` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 50,300.00 USD | 0.00 USD | 64,530.00 USD |
| `7D` | `3853.00` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 205,430.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.40` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 27,320.00 USD | 0.00 USD | 93,700.00 USD |
| `7D` | `3857.20` | 16,800,000.00 USD | 0.00 USD | 16,800,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.50` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 91,370.00 USD | 0.00 USD | 131,510.00 USD |
| `7D` | `3861.40` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 181,250.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 77,800.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `3865.60` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 130,450.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.70` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 46,100.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `3869.80` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 200,270.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3872.80` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 87,380.00 USD | 0.00 USD | 149,870.00 USD |
| `7D` | `3874.00` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3876.90` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 78,110.00 USD | 0.00 USD | 49,200.00 USD |
| `7D` | `3878.20` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3881.00` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 25,200.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `3882.40` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3885.10` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 44,450.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3886.60` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.20` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 6,070.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `3890.80` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.30` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 23,320.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3895.00` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.40` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.10` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.20` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 122,570.00 USD | 0.00 USD | 148,540.00 USD |
| `7D` | `3932.80` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 416,720.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.30` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 21,350.00 USD | 0.00 USD | 105,240.00 USD |
| `7D` | `3937.00` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.40` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 113,960.00 USD | 0.00 USD | 207,720.00 USD |
| `7D` | `3941.20` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 340,060.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.50` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 172,480.00 USD | 0.00 USD | 417,140.00 USD |
| `7D` | `3945.40` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 262,330.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.60` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 138,120.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `3949.60` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 414,070.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.70` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 116,680.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3954.80` | 943,470.00 USD | 0.00 USD | 943,470.00 USD | 115,530.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3958.90` | 532,040.00 USD | 0.00 USD | 532,040.00 USD | 161,750.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.00` | 326,180.00 USD | 0.00 USD | 326,180.00 USD | 40,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.10` | 278,390.00 USD | 0.00 USD | 278,390.00 USD | 88,900.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.20` | 154,710.00 USD | 0.00 USD | 154,710.00 USD | 12,130.00 USD | 0.00 USD | 20,100.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.30` | 122,480.00 USD | 0.00 USD | 122,480.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.40` | 9,780.00 USD | 0.00 USD | 9,780.00 USD | 9,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4012.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4012.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `1D` | `4086.00` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4090.10` | 240,450.00 USD | 240,450.00 USD | 0.00 USD | 79,820.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.40` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 311,550.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.20` | 400,570.00 USD | 400,570.00 USD | 0.00 USD | 56,830.00 USD | 0.00 USD | 103,290.00 USD |
| `7D` | `4096.60` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.30` | 693,870.00 USD | 693,870.00 USD | 0.00 USD | 89,310.00 USD | 0.00 USD | 203,990.00 USD |
| `7D` | `4100.80` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 159,720.00 USD | 0.00 USD | 295,710.00 USD |
| `7D` | `4105.00` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 385,450.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.50` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 151,960.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `4109.20` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 217,050.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.60` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 84,180.00 USD | 0.00 USD | 105,010.00 USD |
| `7D` | `4113.40` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.70` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 148,080.00 USD | 0.00 USD | 277,440.00 USD |
| `7D` | `4117.60` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.80` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 163,150.00 USD | 0.00 USD | 114,580.00 USD |
| `7D` | `4121.80` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.90` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `4126.00` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.00` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 74,770.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.20` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.10` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 26,260.00 USD | 0.00 USD | 22,640.00 USD |
| `7D` | `4134.40` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.20` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.60` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `1D` | `4168.00` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 11,850.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4168.00` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4172.10` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 52,310.00 USD | 0.00 USD | 68,220.00 USD |
| `7D` | `4172.20` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4176.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 70,940.00 USD |
| `7D` | `4176.40` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 74,330.00 USD | 0.00 USD | 87,610.00 USD |
| `7D` | `4180.60` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.40` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 76,950.00 USD | 0.00 USD | 207,280.00 USD |
| `7D` | `4184.80` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 211,650.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.50` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 68,910.00 USD | 0.00 USD | 85,290.00 USD |
| `7D` | `4189.00` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 73,570.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.60` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 50,440.00 USD | 0.00 USD | 66,030.00 USD |
| `7D` | `4193.20` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.70` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 147,950.00 USD |
| `7D` | `4197.40` | 19,260,000.00 USD | 19,260,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4200.80` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 21,140.00 USD |
| `7D` | `4201.60` | 19,460,000.00 USD | 19,460,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4204.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 23,730.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,670,000.00 USD | 19,670,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4209.00` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 44,450.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,830,000.00 USD | 19,830,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4213.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 6,070.00 USD | 0.00 USD | 2,480.00 USD |
| `7D` | `4214.20` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.20` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 19,970,000.00 USD | 19,970,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.30` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,550,000.00 USD | 20,550,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 20,970,000.00 USD | 20,970,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 22,730.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4414.00` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 15,650.00 USD | 0.00 USD | 13,450.00 USD |
| `7D` | `4415.80` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 77,830.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4418.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `4420.00` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.20` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 14,510.00 USD | 0.00 USD | 30,790.00 USD |
| `7D` | `4424.20` | 21,490,000.00 USD | 21,490,000.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4425.80` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 13,690.00 USD | 0.00 USD | 52,460.00 USD |
| `7D` | `4428.40` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `7D` | `4432.60` | 21,750,000.00 USD | 21,750,000.00 USD | 0.00 USD | 44,420.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.80` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4439.40` | 21,900,000.00 USD | 21,900,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `802.32M` | Total OI Tokens: `200,975.7 XAUT`
  * 1h OI Change: `-2.02%` | 4h OI Change: `-1.56%` | 24h OI Change: `-5.45%`
  * Exchange Breakdown: Binance=`60.49M` | Bybit=`143.34M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `0.00` | Last 24h: `239.79K` | Last 3d: `863.21K` | Last 7d: `2.18M`
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
| `15M` | `XAUT` | `36.48%` | `63.52%` | `0.57` | 3,690,000.00 USD |
| `15M` | `Binance` | `33.41%` | `66.59%` | `0.50` | 1,370,000.00 USD |
| `15M` | `OKX` | `36.41%` | `63.59%` | `0.57` | 456,480.00 USD |
| `15M` | `Bybit` | `39.78%` | `60.22%` | `0.66` | 669,330.00 USD |
| `15M` | `KuCoin` | `41.36%` | `58.64%` | `0.71` | 91,030.00 USD |
| `15M` | `Gate` | `19.26%` | `80.74%` | `0.24` | 80,350.00 USD |
| `15M` | `Bitget` | `35.89%` | `64.11%` | `0.56` | 162,380.00 USD |
| `15M` | `BingX` | `46.61%` | `53.39%` | `0.87` | 49,360.00 USD |
| `15M` | `MEXC` | `44.43%` | `55.57%` | `0.80` | 45,210.00 USD |
| `15M` | `Bitunix` | `38.5%` | `61.5%` | `0.63` | 47,380.00 USD |
| `15M` | `Hyperliquid` | `19.72%` | `80.28%` | `0.25` | 27,970.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `39.79%` | `60.21%` | `0.66` | 673,970.00 USD |
| `15M` | `Crypto.com` | `7.94%` | `92.06%` | `0.09` | 6.17 USD |
| `15M` | `WhiteBIT` | `71.59%` | `28.41%` | `2.52` | 10,280.00 USD |
| `15M` | `HTX` | `78.09%` | `21.91%` | `3.56` | 594.74 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 11.85 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 860.80 USD |
| `15M` | `Whale Positions` | `33.41%` | `66.59%` | `0.50` | 1,370,000.00 USD |
| `15M` | `Global Accounts` | `36.48%` | `63.52%` | `0.57` | 3,690,000.00 USD |
| `1H` | `XAUT` | `28.57%` | `71.43%` | `0.40` | 11,790,000.00 USD |
| `1H` | `Binance` | `53.59%` | `46.41%` | `1.15` | 1,570,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `32.33%` | `67.67%` | `0.48` | 716,550.00 USD |
| `1H` | `KuCoin` | `72.87%` | `27.13%` | `2.69` | 88,730.00 USD |
| `1H` | `Gate` | `47.72%` | `52.28%` | `0.91` | 315,200.00 USD |
| `1H` | `Bitget` | `52.8%` | `47.2%` | `1.12` | 586,280.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `17.2%` | `82.8%` | `0.21` | 7,200,000.00 USD |
| `1H` | `Bitunix` | `40.66%` | `59.34%` | `0.69` | 196,830.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.67%` | `56.33%` | `0.78` | 652,690.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `36.14%` | `63.86%` | `0.57` | 455,460.00 USD |
| `1H` | `HTX` | `24.25%` | `75.75%` | `0.32` | 7,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `100%` | `0%` | `1.00` | 1,230.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `53.59%` | `46.41%` | `1.15` | 1,570,000.00 USD |
| `1H` | `Global Accounts` | `28.57%` | `71.43%` | `0.40` | 11,790,000.00 USD |
| `4H` | `XAUT` | `49.20%` | `50.80%` | `0.97` | 87,760,000.00 USD |
| `4H` | `Binance` | `49.25%` | `50.75%` | `0.97` | 35,270,000.00 USD |
| `4H` | `OKX` | `52.83%` | `47.17%` | `1.12` | 11,990,000.00 USD |
| `4H` | `Bybit` | `51.34%` | `48.66%` | `1.06` | 11,330,000.00 USD |
| `4H` | `KuCoin` | `46.94%` | `53.06%` | `0.88` | 686,870.00 USD |
| `4H` | `Gate` | `49.89%` | `50.11%` | `1.00` | 3,550,000.00 USD |
| `4H` | `Bitget` | `52.31%` | `47.69%` | `1.10` | 6,020,000.00 USD |
| `4H` | `BingX` | `29.6%` | `70.4%` | `0.42` | 3,850,000.00 USD |
| `4H` | `MEXC` | `46.82%` | `53.18%` | `0.88` | 3,970,000.00 USD |
| `4H` | `Bitunix` | `46.89%` | `53.11%` | `0.88` | 2,000,000.00 USD |
| `4H` | `Hyperliquid` | `45.94%` | `54.06%` | `0.85` | 4,830,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.39%` | `51.61%` | `0.94` | 2,880,000.00 USD |
| `4H` | `Crypto.com` | `47.53%` | `52.47%` | `0.91` | 34,860.00 USD |
| `4H` | `WhiteBIT` | `86.91%` | `13.09%` | `6.64` | 656,870.00 USD |
| `4H` | `HTX` | `51.44%` | `48.56%` | `1.06` | 132,940.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `56.57%` | `43.43%` | `1.30` | 177,870.00 USD |
| `4H` | `Aster` | `25.01%` | `74.99%` | `0.33` | 176,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `32.66%` | `67.34%` | `0.49` | 202,300.00 USD |
| `4H` | `Whale Positions` | `49.25%` | `50.75%` | `0.97` | 35,270,000.00 USD |
| `4H` | `Global Accounts` | `49.20%` | `50.80%` | `0.97` | 87,760,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4009.95` | `4010.60` | `4009.95` | `4016.25` | `4006.05` | 62,119,740.98 USD | 31,873,156.41 USD | 30,246,584.57 USD | 1,626,571.84 USD | `+2.62%` | `2B / 1S` |
| `5:00 UTC` | `4018.35` | `4015.27` | `4018.35` | `4021.35` | `4007.85` | 23,537,938.01 USD | 12,324,690.76 USD | 11,213,247.26 USD | 1,111,443.50 USD | `+4.72%` | `8B / 5S` |
| `0:00 UTC` | `4012.95` | `4011.64` | `4012.95` | `4018.05` | `4006.35` | 23,090,703.95 USD | 10,667,964.02 USD | 12,422,739.93 USD | -1,754,775.92 USD | `-7.60%` | `2B / 6S` |
| `5:00 UTC` | `4006.35` | `4010.45` | `4006.35` | `4018.05` | `4005.15` | 20,104,069.66 USD | 10,418,811.27 USD | 9,685,258.39 USD | 733,552.89 USD | `+3.65%` | `8B / 3S` |
| `0:00 UTC` | `4019.55` | `4018.60` | `4019.55` | `4021.65` | `4014.45` | 23,123,329.93 USD | 11,738,611.74 USD | 11,384,718.18 USD | 353,893.56 USD | `+1.53%` | `2B / 1S` |
| `5:00 UTC` | `4017.75` | `4018.23` | `4017.75` | `4022.85` | `4013.85` | 11,748,425.82 USD | 4,543,203.48 USD | 7,205,222.34 USD | -2,662,018.86 USD | `-22.66%` | `0B / 10S` |
| `0:00 UTC` | `4012.95` | `4012.70` | `4012.95` | `4015.05` | `4010.55` | 19,243,544.82 USD | 10,660,190.41 USD | 8,583,354.40 USD | 2,076,836.01 USD | `+10.79%` | `2B / 0S` |
| `5:00 UTC` | `4007.55` | `4008.55` | `4007.55` | `4011.75` | `4006.95` | 20,364,355.93 USD | 10,371,947.35 USD | 9,992,408.58 USD | 379,538.77 USD | `+1.86%` | `0B / 5S` |
| `0:00 UTC` | `4003.95` | `4005.15` | `4003.95` | `4009.05` | `4002.45` | 29,389,407.46 USD | 15,260,451.77 USD | 14,128,955.69 USD | 1,131,496.08 USD | `+3.85%` | `4B / 3S` |
| `5:00 UTC` | `4003.95` | `4004.06` | `4003.95` | `4005.15` | `4002.45` | 6,846,670.94 USD | 4,776,761.18 USD | 2,069,909.77 USD | 2,706,851.41 USD | `+39.54%` | `4B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:04` | `Volume 5.0K XAU` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `4045.20` | 1,000.00 USD | 0.00 USD |
| `10-28 17:48` | `Volume 5.0K XAU` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `4068.50` | 2,200.00 USD | 0.00 USD |
| `10-28 16:57` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4052.80` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 10:56` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4041.20` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_EUR (XAUEUR.pi) Metal Auction: ROTA | `3633.06` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_GBP (XAUGBP.pi) Metal Auction: ROTA | `3040.99` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -35,580.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -69,190.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -269,420.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -415,920.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -349,020.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,350,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,660,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,350,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,900,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | 30,970.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1w` | -77,600,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,410,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-35.58K` | 15m=`-69.19K` | 1h=`-415.92K` | 24h=`+30.97K`
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
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4023.15` (Risk Distance: `9.99` pts)
  * +2.5R Take Profit: `3988.18`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4026.07`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
