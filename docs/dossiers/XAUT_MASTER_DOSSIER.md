# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUT
**Canonical Key**: `XAUT` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 04:31:59 IST` (`2026-10-29 23:01:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4025.26` | **Live Ask Quote**: `4025.34` | **Mid Price**: `4025.30`
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
  * Session VWAP: `4029.44` | VWAP Z-Score: `-0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `6.66` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4064.38` | Lower -3.00σ Band: `3994.50`
  * Upper +2.51σ Band: `4058.67` | Lower -2.51σ Band: `4000.21`
  * Upper +2.01σ Band: `4052.85` | Lower -2.01σ Band: `4006.03`
  * Upper +2.00σ Band: `4052.73` | Lower -2.00σ Band: `4006.15`
  * Upper +1.28σ Band: `4044.35` | Lower -1.28σ Band: `4014.53`
  * Upper +1.00σ Band: `4041.09` | Lower -1.00σ Band: `4017.80`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4020.35` | EMA-20=`4019.52` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4022.78` (Slope: `+0.0000`) | EMA-100=`4028.62`
  * Institutional Anchors: EMA-144=`4030.61` | EMA-200=`4031.03` (Slope: `-0.0353`) | EMA-233=`4030.62`
- **Range Boundaries**: 24H High=`4070.97` | 24H Low=`4005.38` | Weekly High=`4082.75` | Weekly Low=`3989.09`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4023.86` (Distance: `+0.05%`)
  * Point of Control (POC) = `4020.98` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `4018.04` (Distance: `+0.19%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4051.02` | Weekly POC=`4014.77` | Weekly VAL=`4006.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`4017.62`
  * London Session (08:00-16:00 UTC): High=`4041.40` | Low=`4009.20`
  * New York Session (13:00-21:00 UTC): High=`4049.45` | Low=`4001.15`
  * Initial Balance (First Hour): IB High=`4037.38` | IB Low=`4013.22`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4009.20` - `4041.40`
  * Optimal Trade Entry (OTE 0.705): `4033.35`
  * Structural Invalidation Anchor (0.786): `4057.50`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4022.02` | `4022.21` | `4021.27` | `4021.48` | `25` | 101,856.61 USD | -26,164.81 USD | `-25.69%` | 2,154,553.93 USD | `-0.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4021.48` | `4021.67` | `4020.87` | `4021.49` | `24` | 98,459.99 USD | -5,125.15 USD | `-5.21%` | 2,149,428.78 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4021.48` | `4024.45` | `4021.28` | `4024.45` | `19` | 78,423.42 USD | 19,975.63 USD | `+25.47%` | 2,169,404.41 USD | `+0.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4018.12` | `4025.28` | `4017.72` | `4022.63` | `250` | 1,005,666.39 USD | 151,466.76 USD | `+15.06%` | 2,074,960.21 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4022.62` | `4023.57` | `4020.87` | `4021.49` | `82` | 330,859.14 USD | 37,421.84 USD | `+11.31%` | 2,112,382.04 USD | `+0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4021.48` | `4024.45` | `4021.28` | `4024.45` | `19` | 78,423.42 USD | 19,975.63 USD | `+25.47%` | 2,132,357.68 USD | `+0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `4025.61` | `4033.50` | `4020.69` | `4021.36` | `1,040` | 4,187,720.97 USD | -239,141.91 USD | `-5.71%` | 1,839,422.95 USD | `-0.58` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4021.37` | `4024.66` | `4017.98` | `4018.13` | `612` | 2,459,694.66 USD | 124,080.01 USD | `+5.04%` | 1,963,502.96 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4018.12` | `4025.28` | `4017.72` | `4024.45` | `352` | 1,414,948.95 USD | 208,864.23 USD | `+14.76%` | 2,172,367.19 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4024.45` | `2,004` | 8,062,376.66 USD | 93,814.40 USD | `+1.16%` | 1,340,961.73 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4038.00` | `4046.27` | `4024.73` | `4025.10` | `2,235` | 9,015,658.63 USD | -658,183.92 USD | `-7.30%` | -25,405.94 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -277,782.48 USD | `-0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | 154,330.79 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,247,147.33 USD | `+1.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4017.72` | `4024.45` | `2,004` | 8,062,376.66 USD | 93,814.40 USD | `+1.16%` | 1,340,961.73 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,627,668.50 USD | `6,365.38` | `4188.90` | `4026.00` | `32919.27` | 1,036,302.80 USD | `+4.04%` | `4X Cross` |
| `52` | `0x4692...164f` | `SHORT` | 25,465,120.35 USD | `6,325.01` | `4132.69` | `4026.00` | `13839.40` | 674,235.50 USD | `+2.65%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,631,627.99 USD | `5,869.90` | `4228.86` | `4026.00` | `30649.19` | 1,191,393.94 USD | `+5.04%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,441,662.07 USD | `4,828.91` | `4157.43` | `4026.00` | `2240.73` | -634,220.25 USD | `-3.26%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,228,299.40 USD | `3,534.02` | `4129.09` | `4026.00` | `462.61` | -363,979.46 USD | `-2.56%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,158,153.16 USD | `3,268.21` | `4228.94` | `4026.00` | `4400.12` | 662,925.97 USD | `+5.04%` | `25X Cross` |
| `176` | `0xa742...e390` | `SHORT` | 11,675,690.40 USD | `2,900.00` | `4364.92` | `4026.00` | `4235.67` | 982,585.93 USD | `+8.42%` | `20X Cross` |
| `256` | `0x3678...b209` | `LONG` | 8,857,420.00 USD | `2,200.00` | `4176.09` | `4026.00` | `2701.54` | -329,999.30 USD | `-3.73%` | `25X Cross` |
| `257` | `0x41e5...0825` | `SHORT` | 8,856,980.00 USD | `2,200.00` | `4112.20` | `4026.00` | `4331.15` | 189,874.59 USD | `+2.14%` | `20X Cross` |
| `259` | `0xfc66...ca06` | `SHORT` | 8,843,588.25 USD | `2,196.67` | `4031.28` | `4026.00` | `10393.57` | 11,833.46 USD | `+0.13%` | `3X Cross` |
| `293` | `0xacb6...efbd` | `SHORT` | 7,952,638.46 USD | `1,975.37` | `4048.55` | `4026.00` | `6502.36` | 44,753.25 USD | `+0.56%` | `6X Cross` |
| `363` | `0xc26c...b8f4` | `LONG` | 6,361,043.94 USD | `1,579.95` | `4075.62` | `4026.00` | `0.000000` | -78,253.03 USD | `-1.23%` | `1X Cross` |
| `399` | `0x12d2...f97f` | `LONG` | 5,644,081.52 USD | `1,401.94` | `4278.91` | `4026.00` | `3134.13` | -354,709.06 USD | `-6.28%` | `20X Cross` |
| `546` | `0x63da...8add` | `LONG` | 4,026,100.00 USD | `1,000.00` | `4021.46` | `4026.00` | `3564.11` | 4,639.04 USD | `+0.12%` | `25X Cross` |
| `556` | `0x354b...6425` | `LONG` | 3,953,497.74 USD | `981.97` | `4031.85` | `4026.00` | `0.000000` | -5,650.58 USD | `-0.14%` | `10X Cross` |
| `570` | `0x9aa5...58af` | `LONG` | 3,911,927.86 USD | `971.64` | `4279.98` | `4026.00` | `0.000000` | -246,681.23 USD | `-6.31%` | `20X Cross` |
| `593` | `0xf3dc...1672` | `LONG` | 3,747,267.21 USD | `930.74` | `4024.62` | `4026.00` | `3344.05` | 1,374.65 USD | `+0.04%` | `20X Cross` |
| `666` | `0x4a20...3c26` | `LONG` | 3,371,454.93 USD | `837.40` | `4599.73` | `4026.00` | `0.000000` | -480,365.45 USD | `-14.25%` | `20X Cross` |
| `813` | `0x0fac...7a0a` | `LONG` | 2,763,857.26 USD | `686.49` | `4290.34` | `4026.00` | `1524.32` | -181,401.44 USD | `-6.56%` | `25X Cross` |
| `865` | `0xd8c5...99b0` | `SHORT` | 2,586,185.06 USD | `642.35` | `4175.35` | `4026.00` | `33022.37` | 95,876.11 USD | `+3.71%` | `4X Cross` |
| `894` | `0x625e...a354` | `SHORT` | 2,496,058.00 USD | `620.00` | `4122.81` | `4026.00` | `4342.25` | 60,089.03 USD | `+2.41%` | `20X Cross` |
| `931` | `0xeae3...e8ad` | `SHORT` | 2,415,660.00 USD | `600.00` | `4104.77` | `4026.00` | `4325.27` | 47,205.11 USD | `+1.95%` | `20X Cross` |
| `933` | `0xf285...fa82` | `LONG` | 2,408,034.16 USD | `598.11` | `4146.45` | `4026.00` | `3891.24` | -71,985.39 USD | `-2.99%` | `25X Cross` |
| `955` | `0x12f7...8750` | `LONG` | 2,357,727.24 USD | `585.61` | `4082.77` | `4026.00` | `2539.70` | -33,189.74 USD | `-1.41%` | `10X Cross` |
| `1088` | `0x413c...886c` | `LONG` | 2,013,050.00 USD | `500.00` | `4010.43` | `4026.00` | `0.000000` | 7,833.77 USD | `+0.39%` | `2X Cross` |
| `1100` | `0x61ce...a62b` | `SHORT` | 2,002,998.84 USD | `497.50` | `4071.66` | `4026.00` | `4712.96` | 22,669.95 USD | `+1.13%` | `20X Cross` |
| `1104` | `0x0593...40f9` | `LONG` | 1,997,658.22 USD | `496.18` | `4024.57` | `4026.00` | `3701.73` | 754.39 USD | `+0.04%` | `10X Isolated` |
| `1222` | `0xead5...69f2` | `LONG` | 1,826,888.60 USD | `453.78` | `4220.88` | `4026.00` | `3538.94` | -88,479.46 USD | `-4.84%` | `5X Isolated` |
| `1309` | `0x46fc...1195` | `LONG` | 1,676,435.03 USD | `416.39` | `4054.56` | `4026.00` | `2189.38` | -11,850.96 USD | `-0.71%` | `20X Cross` |
| `1368` | `0xee02...309d` | `SHORT` | 1,610,440.00 USD | `400.00` | `4438.84` | `4026.00` | `4226.89` | 165,098.60 USD | `+10.25%` | `25X Isolated` |
| `1370` | `0x6d15...d374` | `LONG` | 1,610,360.00 USD | `400.00` | `4068.25` | `4026.00` | `3841.81` | -16,940.00 USD | `-1.05%` | `25X Cross` |
| `1403` | `0x02a7...fe9f` | `SHORT` | 1,570,179.00 USD | `390.00` | `4055.02` | `4026.00` | `4306.71` | 11,280.25 USD | `+0.72%` | `25X Cross` |
| `1444` | `0x7e77...b8d2` | `SHORT` | 1,529,918.00 USD | `380.00` | `4131.92` | `4026.00` | `4293.51` | 40,211.64 USD | `+2.63%` | `20X Cross` |
| `1457` | `0x72c2...9b37` | `LONG` | 1,502,263.93 USD | `373.13` | `4000.98` | `4026.00` | `3778.05` | 9,370.41 USD | `+0.62%` | `13X Isolated` |
| `1501` | `0xaa44...b844` | `LONG` | 1,449,396.00 USD | `360.00` | `4043.10` | `4026.00` | `2820.95` | -6,121.63 USD | `-0.42%` | `4X Cross` |
| `1625` | `0xa41f...d50a` | `LONG` | 1,324,368.52 USD | `328.96` | `4468.89` | `4026.00` | `3833.19` | -145,729.33 USD | `-11.00%` | `15X Cross` |
| `1657` | `0xbf5a...88ba` | `SHORT` | 1,278,910.39 USD | `317.65` | `4091.80` | `4026.00` | `9874.78` | 20,872.64 USD | `+1.63%` | `20X Cross` |
| `1689` | `0xff31...ff6c` | `SHORT` | 1,248,091.00 USD | `310.00` | `4372.43` | `4026.00` | `4789.18` | 107,364.38 USD | `+8.60%` | `10X Isolated` |
| `1699` | `0xada6...6f88` | `LONG` | 1,240,442.62 USD | `308.10` | `4166.46` | `4026.00` | `1937.12` | -43,246.40 USD | `-3.49%` | `5X Cross` |
| `1872` | `0x50e2...d770` | `LONG` | 1,088,526.19 USD | `270.37` | `4243.58` | `4026.00` | `2562.10` | -58,800.27 USD | `-5.40%` | `20X Cross` |
| `1887` | `0x4c92...4f17` | `SHORT` | 1,073,843.41 USD | `266.72` | `4260.98` | `4026.00` | `6518.25` | 62,648.83 USD | `+5.83%` | `20X Cross` |
| `1944` | `0xd346...c4f3` | `LONG` | 1,027,355.24 USD | `255.17` | `4188.66` | `4026.00` | `3310.43` | -41,481.27 USD | `-4.04%` | `5X Isolated` |
| `1990` | `0x1581...463b` | `LONG` | 1,006,475.00 USD | `250.00` | `4003.77` | `4026.00` | `3555.39` | 5,531.41 USD | `+0.55%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4225.80` | 325.39 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.33K USD at 4225.8000 USD [API] | `2026-09-28 01:01:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4118.75` (Vol: 171,400.00 USD, Dist: `+2.40%`) | Long MP=`3953.05` (Vol: 152,200.00 USD, Dist: `--1.72%`)
  * 48H Horizon: Short MP=`4118.09` (Vol: 350,900.00 USD, Dist: `+2.38%`) | Long MP=`3957.22` (Vol: 390,800.00 USD, Dist: `--1.62%`)
  * 3D Horizon: Short MP=`4110.46` (Vol: 300,700.00 USD, Dist: `+2.19%`) | Long MP=`3959.21` (Vol: 388,300.00 USD, Dist: `--1.57%`)
  * 7D Horizon: Short MP=`4082.49` (Vol: 552,000.00 USD, Dist: `+1.50%`) | Long MP=`3921.81` (Vol: 617,500.00 USD, Dist: `--2.50%`)
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
| `7D` | `3605.20` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 33,130.00 USD | 0.00 USD | 98,140.00 USD |
| `7D` | `3609.40` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `7D` | `3613.60` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 76,290.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3614.60` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 7,480.00 USD | 0.00 USD | 24,000.00 USD |
| `7D` | `3617.80` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.70` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 18,220.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.80` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 21,080.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.20` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3626.90` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 14,290.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.40` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3631.00` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 31,880.00 USD | 0.00 USD | 53,030.00 USD |
| `7D` | `3634.60` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.10` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 30,630.00 USD | 0.00 USD | 15,790.00 USD |
| `7D` | `3638.80` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.20` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.00` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.30` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 17,700.00 USD | 0.00 USD | 6,960.00 USD |
| `7D` | `3647.20` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3647.40` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 2,430.00 USD | 0.00 USD | 8,310.00 USD |
| `1D` | `3651.50` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 9,200.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.30` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 18,030.00 USD | 0.00 USD | 72,840.00 USD |
| `7D` | `3848.80` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.40` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 15,390.00 USD | 0.00 USD | 47,520.00 USD |
| `7D` | `3853.00` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.50` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 27,320.00 USD | 0.00 USD | 93,700.00 USD |
| `7D` | `3857.20` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.60` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 91,370.00 USD | 0.00 USD | 131,510.00 USD |
| `7D` | `3861.40` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.70` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 77,800.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `3865.60` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.80` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 46,100.00 USD | 0.00 USD | 58,620.00 USD |
| `7D` | `3869.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3872.90` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 88,320.00 USD | 0.00 USD | 148,830.00 USD |
| `7D` | `3874.00` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3877.00` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 77,180.00 USD | 0.00 USD | 50,890.00 USD |
| `7D` | `3878.20` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3881.10` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 25,200.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `3882.40` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3885.20` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3886.60` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.30` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 6,830.00 USD | 0.00 USD | 15,460.00 USD |
| `7D` | `3890.80` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.40` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 23,320.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3895.00` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.50` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.20` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.30` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 52,750.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `3932.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.40` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 21,350.00 USD | 0.00 USD | 106,170.00 USD |
| `7D` | `3937.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.50` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 113,960.00 USD | 0.00 USD | 198,530.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.60` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 185,430.00 USD | 0.00 USD | 417,140.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 125,170.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.80` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 116,680.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3954.90` | 955,670.00 USD | 0.00 USD | 955,670.00 USD | 115,530.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3959.00` | 544,240.00 USD | 0.00 USD | 544,240.00 USD | 161,750.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.10` | 338,370.00 USD | 0.00 USD | 338,370.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.20` | 279,500.00 USD | 0.00 USD | 279,500.00 USD | 94,760.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.30` | 149,960.00 USD | 0.00 USD | 149,960.00 USD | 1,540.00 USD | 0.00 USD | 25,940.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.40` | 122,480.00 USD | 0.00 USD | 122,480.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.50` | 9,780.00 USD | 0.00 USD | 9,780.00 USD | 9,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `4017.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4018.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `1D` | `4086.10` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4090.20` | 200,730.00 USD | 200,730.00 USD | 0.00 USD | 40,090.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 216,890.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.30` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 26,730.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.40` | 607,650.00 USD | 607,650.00 USD | 0.00 USD | 89,310.00 USD | 0.00 USD | 203,990.00 USD |
| `7D` | `4100.80` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.50` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 159,720.00 USD | 0.00 USD | 295,710.00 USD |
| `7D` | `4105.00` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 455,740.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.60` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 154,350.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `4109.20` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 350,460.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.70` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 90,410.00 USD | 0.00 USD | 105,010.00 USD |
| `7D` | `4113.40` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.80` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 142,550.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `4117.60` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.90` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 161,970.00 USD | 0.00 USD | 98,400.00 USD |
| `7D` | `4121.80` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 68,230.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `4126.00` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.10` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.20` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.20` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 16,920.00 USD | 0.00 USD | 28,490.00 USD |
| `7D` | `4134.40` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.30` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4168.00` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.10` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 11,850.00 USD | 0.00 USD | 48,150.00 USD |
| `1D` | `4172.20` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 17,400.00 USD | 0.00 USD | 65,240.00 USD |
| `7D` | `4172.20` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4176.30` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 11,440.00 USD | 0.00 USD | 70,790.00 USD |
| `7D` | `4176.40` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.40` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD | 82,550.00 USD |
| `7D` | `4180.60` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.50` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 82,280.00 USD | 0.00 USD | 207,280.00 USD |
| `7D` | `4184.80` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.60` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 61,290.00 USD | 0.00 USD | 85,290.00 USD |
| `7D` | `4189.00` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.70` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 50,440.00 USD | 0.00 USD | 66,030.00 USD |
| `7D` | `4193.20` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.80` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 147,950.00 USD |
| `7D` | `4197.40` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4200.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 21,140.00 USD |
| `7D` | `4201.60` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4205.00` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 23,730.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4209.10` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4213.20` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD | 5,410.00 USD |
| `7D` | `4214.20` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.30` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.40` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4410.00` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4414.10` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4415.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4418.20` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `4420.00` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.30` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 14,510.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `4424.20` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4425.40` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 13,690.00 USD | 0.00 USD | 41,770.00 USD |
| `7D` | `4428.40` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `7D` | `4432.60` | 21,920,000.00 USD | 21,920,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.80` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4439.40` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `823.81M` | Total OI Tokens: `204,805.2 XAUT`
  * 1h OI Change: `-0.20%` | 4h OI Change: `-2.36%` | 24h OI Change: `+2.94%`
  * Exchange Breakdown: Binance=`61.68M` | Bybit=`142.84M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `0.00` | Last 24h: `245.96K` | Last 3d: `915.11K` | Last 7d: `2.40M`
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
| `15M` | `XAUT` | `55.58%` | `44.42%` | `1.25` | 3,240,000.00 USD |
| `15M` | `Binance` | `53.02%` | `46.98%` | `1.13` | 1,360,000.00 USD |
| `15M` | `OKX` | `59.8%` | `40.2%` | `1.49` | 338,940.00 USD |
| `15M` | `Bybit` | `56.67%` | `43.33%` | `1.31` | 311,270.00 USD |
| `15M` | `KuCoin` | `51.15%` | `48.85%` | `1.05` | 36,010.00 USD |
| `15M` | `Gate` | `44.52%` | `55.48%` | `0.80` | 246,370.00 USD |
| `15M` | `Bitget` | `50.47%` | `49.53%` | `1.02` | 71,330.00 USD |
| `15M` | `BingX` | `49.19%` | `50.81%` | `0.97` | 98,340.00 USD |
| `15M` | `MEXC` | `64.53%` | `35.47%` | `1.82` | 238,260.00 USD |
| `15M` | `Bitunix` | `56.98%` | `43.02%` | `1.32` | 53,460.00 USD |
| `15M` | `Hyperliquid` | `58.49%` | `41.51%` | `1.41` | 114,630.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.69%` | `51.31%` | `0.95` | 221,660.00 USD |
| `15M` | `Crypto.com` | `33.35%` | `66.65%` | `0.50` | 2,660.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 117,370.00 USD |
| `15M` | `HTX` | `30.28%` | `69.72%` | `0.43` | 861.21 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `11.92%` | `88.08%` | `0.14` | 5,450.00 USD |
| `15M` | `Aster` | `18.73%` | `81.27%` | `0.23` | 451.04 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.14%` | `60.86%` | `0.64` | 18,730.00 USD |
| `15M` | `Whale Positions` | `53.02%` | `46.98%` | `1.13` | 1,360,000.00 USD |
| `15M` | `Global Accounts` | `55.58%` | `44.42%` | `1.25` | 3,240,000.00 USD |
| `1H` | `XAUT` | `50.43%` | `49.57%` | `1.02` | 8,230,000.00 USD |
| `1H` | `Binance` | `54.31%` | `45.69%` | `1.19` | 2,950,000.00 USD |
| `1H` | `OKX` | `45.03%` | `54.97%` | `0.82` | 739,690.00 USD |
| `1H` | `Bybit` | `48.82%` | `51.18%` | `0.95` | 1,010,000.00 USD |
| `1H` | `KuCoin` | `37.76%` | `62.24%` | `0.61` | 37,470.00 USD |
| `1H` | `Gate` | `48.74%` | `51.26%` | `0.95` | 162,300.00 USD |
| `1H` | `Bitget` | `49.05%` | `50.95%` | `0.96` | 275,430.00 USD |
| `1H` | `BingX` | `42.11%` | `57.89%` | `0.73` | 294,410.00 USD |
| `1H` | `MEXC` | `52.67%` | `47.33%` | `1.11` | 742,140.00 USD |
| `1H` | `Bitunix` | `50.51%` | `49.49%` | `1.02` | 68,730.00 USD |
| `1H` | `Hyperliquid` | `37.37%` | `62.63%` | `0.60` | 239,080.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.46%` | `50.54%` | `0.98` | 1,340,000.00 USD |
| `1H` | `Crypto.com` | `18.34%` | `81.66%` | `0.22` | 13.25 USD |
| `1H` | `WhiteBIT` | `53.08%` | `46.92%` | `1.13` | 343,360.00 USD |
| `1H` | `HTX` | `38.54%` | `61.46%` | `0.63` | 1,190.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `27.08%` | `72.92%` | `0.37` | 6,950.00 USD |
| `1H` | `Aster` | `8.52%` | `91.48%` | `0.09` | 11,280.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `67.96%` | `32.04%` | `2.12` | 13,650.00 USD |
| `1H` | `Whale Positions` | `54.31%` | `45.69%` | `1.19` | 2,950,000.00 USD |
| `1H` | `Global Accounts` | `50.43%` | `49.57%` | `1.02` | 8,230,000.00 USD |
| `4H` | `XAUT` | `44.49%` | `55.51%` | `0.80` | 82,720,000.00 USD |
| `4H` | `Binance` | `45.28%` | `54.72%` | `0.83` | 35,090,000.00 USD |
| `4H` | `OKX` | `48.64%` | `51.36%` | `0.95` | 9,400,000.00 USD |
| `4H` | `Bybit` | `47.73%` | `52.27%` | `0.91` | 12,060,000.00 USD |
| `4H` | `KuCoin` | `49.07%` | `50.93%` | `0.96` | 2,690,000.00 USD |
| `4H` | `Gate` | `50.15%` | `49.85%` | `1.01` | 1,850,000.00 USD |
| `4H` | `Bitget` | `47.05%` | `52.95%` | `0.89` | 3,380,000.00 USD |
| `4H` | `BingX` | `22.32%` | `77.68%` | `0.29` | 6,080,000.00 USD |
| `4H` | `MEXC` | `42.49%` | `57.51%` | `0.74` | 4,450,000.00 USD |
| `4H` | `Bitunix` | `41.42%` | `58.58%` | `0.71` | 1,560,000.00 USD |
| `4H` | `Hyperliquid` | `43.59%` | `56.41%` | `0.77` | 1,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.84%` | `52.16%` | `0.92` | 1,300,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.63%` | `53.37%` | `0.87` | 2,340,000.00 USD |
| `4H` | `HTX` | `53.91%` | `46.09%` | `1.17` | 75,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.46%` | `46.54%` | `1.15` | 238,720.00 USD |
| `4H` | `Aster` | `55.95%` | `44.05%` | `1.27` | 217,470.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.19%` | `79.81%` | `0.25` | 80,530.00 USD |
| `4H` | `Whale Positions` | `45.28%` | `54.72%` | `0.83` | 35,090,000.00 USD |
| `4H` | `Global Accounts` | `44.49%` | `55.51%` | `0.80` | 82,720,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4034.25` | `4032.78` | `4034.25` | `4035.75` | `4029.15` | 20,678,719.43 USD | 6,048,411.49 USD | 14,630,307.94 USD | -8,581,896.45 USD | `-41.50%` | `0B / 10S` |
| `5:00 UTC` | `4027.05` | `4027.95` | `4027.05` | `4030.95` | `4025.85` | 20,652,312.18 USD | 9,057,345.58 USD | 11,594,966.60 USD | -2,537,621.02 USD | `-12.29%` | `0B / 4S` |
| `0:00 UTC` | `4025.55` | `4026.40` | `4025.55` | `4027.95` | `4025.25` | 7,818,216.37 USD | 4,727,752.16 USD | 3,090,464.21 USD | 1,637,287.96 USD | `+20.94%` | `2B / 0S` |
| `5:00 UTC` | `4028.25` | `4028.75` | `4028.25` | `4030.65` | `4025.85` | 8,803,589.25 USD | 4,465,465.69 USD | 4,338,123.56 USD | 127,342.13 USD | `+1.45%` | `0B / 1S` |
| `0:00 UTC` | `4028.55` | `4028.32` | `4028.55` | `4029.45` | `4026.75` | 4,446,639.42 USD | 3,302,435.87 USD | 1,144,203.55 USD | 2,158,232.32 USD | `+48.54%` | `7B / 0S` |
| `5:00 UTC` | `4027.05` | `4026.44` | `4027.05` | `4028.55` | `4024.65` | 2,877,135.19 USD | 891,261.53 USD | 1,985,873.66 USD | -1,094,612.13 USD | `-38.05%` | `0B / 8S` |
| `0:00 UTC` | `4029.45` | `4029.28` | `4029.45` | `4032.45` | `4024.35` | 21,236,940.50 USD | 10,861,231.68 USD | 10,375,708.82 USD | 485,522.86 USD | `+2.29%` | `6B / 2S` |
| `5:00 UTC` | `4027.95` | `4027.86` | `4027.95` | `4030.35` | `4025.85` | 14,108,709.52 USD | 8,835,489.72 USD | 5,273,219.80 USD | 3,562,269.92 USD | `+25.25%` | `1B / 5S` |
| `0:00 UTC` | `4030.05` | `4029.44` | `4030.05` | `4031.85` | `4025.85` | 20,554,396.68 USD | 10,499,328.97 USD | 10,055,067.71 USD | 444,261.26 USD | `+2.16%` | `4B / 4S` |
| `5:00 UTC` | `4030.05` | `4031.57` | `4030.05` | `4033.65` | `4029.15` | 22,472,114.20 USD | 17,042,692.12 USD | 5,429,422.08 USD | 11,613,270.04 USD | `+51.68%` | `5B / 1S` |

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
| `5m` | 18,510.00 USD | 30,150.00 USD | **`ACCUMULATION`** |
| `15m` | 80,750.00 USD | -38,140.00 USD | **`ACCUMULATION`** |
| `30m` | 58,620.00 USD | 14,590.00 USD | **`ACCUMULATION`** |
| `1h` | 155,050.00 USD | -44,600.00 USD | **`ACCUMULATION`** |
| `2h` | 316,640.00 USD | 635,100.00 USD | **`ACCUMULATION`** |
| `4h` | 36,230.00 USD | 947,020.00 USD | **`ACCUMULATION`** |
| `6h` | -424,730.00 USD | 1,290,000.00 USD | **`ACCUMULATION`** |
| `8h` | -532,890.00 USD | 1,670,000.00 USD | **`ACCUMULATION`** |
| `12h` | -102,330.00 USD | 1,200,000.00 USD | **`ACCUMULATION`** |
| `24h` | -325,260.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `1w` | -79,810,000.00 USD | -19,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,670,000.00 USD | -83,700,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+18.51K` | 15m=`+80.75K` | 1h=`+155.05K` | 24h=`-325.26K`
* Futures Capital Netflows: 5m=`+30.15K` | 15m=`-38.14K` | 1h=`-44.60K` | 24h=`+1.36M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4018.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `4009.93` (Risk Distance: `8.11` pts)
  * +2.5R Take Profit: `4038.31`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.08 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4023.86` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4031.97` (Risk Distance: `8.11` pts)
  * +2.5R Take Profit: `4003.59`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.08 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4057.50`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
