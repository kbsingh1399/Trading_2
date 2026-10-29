# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 00:35:21 IST` (`2026-10-29 19:05:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26700.58` | **Live Ask Quote**: `26702.26` | **Mid Price**: `26701.42`
- **Spread Points**: `168.00` | **Spread BPS**: `0.63 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26701.42` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.75` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26888.33` | Lower -3.00σ Band: `26514.51`
  * Upper +2.51σ Band: `26848.28` | Lower -2.51σ Band: `26554.56`
  * Upper +2.01σ Band: `26813.57` | Lower -2.01σ Band: `26589.27`
  * Upper +2.00σ Band: `26808.23` | Lower -2.00σ Band: `26594.61`
  * Upper +1.28σ Band: `26776.18` | Lower -1.28σ Band: `26626.66`
  * Upper +1.00σ Band: `26754.82` | Lower -1.00σ Band: `26648.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26701.42` | EMA-20=`26701.42` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26701.42` (Slope: `+0.0000`) | EMA-100=`26701.42`
  * Institutional Anchors: EMA-144=`26701.42` | EMA-200=`26701.42` (Slope: `+0.0000`) | EMA-233=`26701.42`
- **Range Boundaries**: 24H High=`26968.43` | 24H Low=`26434.41` | Weekly High=`27235.45` | Weekly Low=`26167.39`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26781.52` (Distance: `+0.00%`)
  * Point of Control (POC) = `26701.42` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26621.32` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26808.23` | POC=`26701.42` | VAL=`26594.61`
  * Prior Day Extremes: PDH=`26861.63` | PDL=`26541.21` | PDC=`26701.42`
  * Monday Range Blueprint: High=`26834.93` | Mid=`26701.42` | Low=`26567.91`
  * Developing Weekly Value Area: Weekly VAH=`26915.03` | Weekly POC=`26701.42` | Weekly VAL=`26487.81`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26754.82` | Low=`26648.02`
  * London Session (08:00-16:00 UTC): High=`26808.23` | Low=`26594.61`
  * New York Session (13:00-21:00 UTC): High=`26861.63` | Low=`26541.21`
  * Initial Balance (First Hour): IB High=`26781.52` | IB Low=`26621.32`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26594.61` - `26808.23`
  * Optimal Trade Entry (OTE 0.705): `26754.82`
  * Structural Invalidation Anchor (0.786): `26915.03`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,576,168.68 USD | `6,373.65` | `4191.43` | `4012.80` | `29181.84` | 1,138,580.52 USD | `+4.45%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,359,751.09 USD | `6,319.56` | `4133.88` | `4012.80` | `13294.26` | 764,591.35 USD | `+3.01%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,940,844.25 USD | `5,717.06` | `4234.49` | `4012.80` | `27494.25` | 1,268,030.97 USD | `+5.53%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,377,920.50 USD | `4,828.91` | `4157.43` | `4012.80` | `2084.98` | -697,961.82 USD | `-3.60%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,111,639.20 USD | `3,516.66` | `4129.63` | `4012.80` | `304.95` | -410,871.67 USD | `-2.91%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,114,685.93 USD | `3,268.21` | `4228.94` | `4012.80` | `4409.83` | 706,393.20 USD | `+5.39%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,637,410.40 USD | `2,900.00` | `4364.92` | `4012.80` | `4235.59` | 1,020,865.93 USD | `+8.77%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,828,160.00 USD | `2,200.00` | `4176.09` | `4012.80` | `2451.98` | -359,259.30 USD | `-4.07%` | `25X Cross` |
| `277` | `0x41e5...0825` | `SHORT` | 8,827,940.00 USD | `2,200.00` | `4112.20` | `4012.80` | `4331.08` | 218,914.59 USD | `+2.48%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,972,990.59 USD | `1,986.89` | `4032.86` | `4012.80` | `25065.82` | 39,875.58 USD | `+0.50%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,926,958.66 USD | `1,975.37` | `4048.55` | `4012.80` | `6499.57` | 70,433.05 USD | `+0.89%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,340,030.58 USD | `1,579.95` | `4075.62` | `4012.80` | `0.000000` | -99,266.39 USD | `-1.57%` | `1X Cross` |
| `421` | `0x12d2...f97f` | `LONG` | 5,625,856.26 USD | `1,401.94` | `4278.91` | `4012.80` | `2497.95` | -372,934.32 USD | `-6.63%` | `20X Cross` |
| `578` | `0x63da...8add` | `LONG` | 4,012,800.00 USD | `1,000.00` | `4021.46` | `4012.80` | `3564.03` | -8,660.96 USD | `-0.22%` | `25X Cross` |
| `597` | `0x9aa5...58af` | `LONG` | 3,899,102.18 USD | `971.64` | `4279.98` | `4012.80` | `0.000000` | -259,506.90 USD | `-6.66%` | `20X Cross` |
| `626` | `0xf3dc...1672` | `LONG` | 3,734,702.17 USD | `930.74` | `4024.62` | `4012.80` | `3337.51` | -11,190.39 USD | `-0.30%` | `20X Cross` |
| `690` | `0x4a20...3c26` | `LONG` | 3,360,317.52 USD | `837.40` | `4599.73` | `4012.80` | `0.000000` | -491,502.87 USD | `-14.63%` | `20X Cross` |
| `769` | `0x354b...6425` | `LONG` | 3,071,122.53 USD | `765.31` | `4035.10` | `4012.80` | `0.000000` | -16,990.45 USD | `-0.55%` | `10X Cross` |
| `849` | `0x0fac...7a0a` | `LONG` | 2,754,795.66 USD | `686.49` | `4290.34` | `4012.80` | `1248.48` | -190,463.05 USD | `-6.91%` | `25X Cross` |
| `889` | `0xd8c5...99b0` | `SHORT` | 2,577,641.74 USD | `642.35` | `4175.35` | `4012.80` | `32047.83` | 104,419.44 USD | `+4.05%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,487,874.00 USD | `620.00` | `4122.81` | `4012.80` | `4342.18` | 68,273.03 USD | `+2.74%` | `20X Cross` |
| `950` | `0xeae3...e8ad` | `SHORT` | 2,407,560.00 USD | `600.00` | `4104.77` | `4012.80` | `4325.20` | 55,305.11 USD | `+2.30%` | `20X Cross` |
| `952` | `0xf285...fa82` | `LONG` | 2,400,139.17 USD | `598.11` | `4146.45` | `4012.80` | `3891.17` | -79,880.39 USD | `-3.33%` | `25X Cross` |
| `969` | `0x12f7...8750` | `LONG` | 2,349,938.62 USD | `585.61` | `4082.77` | `4012.80` | `2155.86` | -40,978.36 USD | `-1.74%` | `10X Cross` |
| `1132` | `0x413c...886c` | `LONG` | 2,006,350.00 USD | `500.00` | `4010.43` | `4012.80` | `0.000000` | 1,133.77 USD | `+0.06%` | `2X Cross` |
| `1141` | `0x61ce...a62b` | `SHORT` | 1,996,282.54 USD | `497.50` | `4071.66` | `4012.80` | `4690.69` | 29,386.25 USD | `+1.47%` | `20X Cross` |
| `1147` | `0x0593...40f9` | `LONG` | 1,991,059.07 USD | `496.18` | `4024.57` | `4012.80` | `3701.65` | -5,844.76 USD | `-0.29%` | `10X Isolated` |
| `1260` | `0xead5...69f2` | `LONG` | 1,820,989.41 USD | `453.78` | `4220.88` | `4012.80` | `3538.86` | -94,378.65 USD | `-5.18%` | `5X Isolated` |
| `1386` | `0x46fc...1195` | `LONG` | 1,633,242.56 USD | `407.03` | `4055.53` | `4012.80` | `1926.50` | -17,477.26 USD | `-1.07%` | `20X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,605,160.00 USD | `400.00` | `4438.84` | `4012.80` | `4226.81` | 170,378.60 USD | `+10.61%` | `25X Isolated` |
| `1425` | `0x6d15...d374` | `LONG` | 1,605,080.00 USD | `400.00` | `4068.25` | `4012.80` | `3841.73` | -22,220.00 USD | `-1.38%` | `25X Cross` |
| `1453` | `0x02a7...fe9f` | `SHORT` | 1,564,992.00 USD | `390.00` | `4055.02` | `4012.80` | `4306.63` | 16,467.25 USD | `+1.05%` | `25X Cross` |
| `1489` | `0x7e77...b8d2` | `SHORT` | 1,524,864.00 USD | `380.00` | `4131.92` | `4012.80` | `4293.44` | 45,265.64 USD | `+2.97%` | `20X Cross` |
| `1505` | `0x72c2...9b37` | `LONG` | 1,497,226.65 USD | `373.13` | `4000.98` | `4012.80` | `3777.97` | 4,333.14 USD | `+0.29%` | `13X Isolated` |
| `1543` | `0xaa44...b844` | `LONG` | 1,444,536.00 USD | `360.00` | `4043.10` | `4012.80` | `2818.87` | -10,981.63 USD | `-0.76%` | `9X Cross` |
| `1655` | `0xa41f...d50a` | `LONG` | 1,320,092.01 USD | `328.96` | `4468.89` | `4012.80` | `3833.11` | -150,005.84 USD | `-11.36%` | `15X Cross` |
| `1685` | `0x49e9...e1d0` | `SHORT` | 1,298,403.09 USD | `323.56` | `4025.23` | `4012.80` | `28135.71` | 3,989.61 USD | `+0.31%` | `4X Cross` |
| `1712` | `0xada6...6f88` | `LONG` | 1,281,125.27 USD | `319.28` | `4166.46` | `4012.80` | `1868.52` | -49,125.24 USD | `-3.83%` | `5X Cross` |
| `1718` | `0xbf5a...88ba` | `SHORT` | 1,274,717.35 USD | `317.65` | `4091.80` | `4012.80` | `10497.37` | 25,065.68 USD | `+1.97%` | `20X Cross` |
| `1734` | `0xff31...ff6c` | `SHORT` | 1,243,968.00 USD | `310.00` | `4372.43` | `4012.80` | `4789.11` | 111,487.38 USD | `+8.96%` | `10X Isolated` |
| `1900` | `0x50e2...d770` | `LONG` | 1,084,930.30 USD | `270.37` | `4243.58` | `4012.80` | `2562.02` | -62,396.16 USD | `-5.75%` | `20X Cross` |
| `1913` | `0x4c92...4f17` | `SHORT` | 1,070,296.02 USD | `266.72` | `4260.98` | `4012.80` | `6524.92` | 66,196.21 USD | `+6.18%` | `20X Cross` |
| `1989` | `0xd346...c4f3` | `LONG` | 1,023,986.94 USD | `255.17` | `4188.66` | `4012.80` | `3310.35` | -44,849.57 USD | `-4.38%` | `5X Isolated` |
| `2028` | `0x1581...463b` | `LONG` | 1,003,175.00 USD | `250.00` | `4003.77` | `4012.80` | `3504.56` | 2,231.41 USD | `+0.22%` | `15X Cross` |
| `2029` | `0xe47f...758c` | `LONG` | 1,003,175.00 USD | `250.00` | `4020.00` | `4012.80` | `3774.26` | -1,825.00 USD | `-0.18%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
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
| `7D` | `3605.10` | 22,740,000.00 USD | 0.00 USD | 22,740,000.00 USD | 33,130.00 USD | 0.00 USD | 129,270.00 USD |
| `1D` | `3606.30` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `3609.30` | 22,570,000.00 USD | 0.00 USD | 22,570,000.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `3610.50` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 4,870.00 USD | 0.00 USD | 25,000.00 USD |
| `7D` | `3613.50` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 84,000.00 USD | 0.00 USD | 67,380.00 USD |
| `1D` | `3614.70` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 7,480.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `3617.70` | 22,350,000.00 USD | 0.00 USD | 22,350,000.00 USD | 51,620.00 USD | 0.00 USD | 104,640.00 USD |
| `1D` | `3618.90` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 6,260.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3621.90` | 22,200,000.00 USD | 0.00 USD | 22,200,000.00 USD | 86,890.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `3623.10` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.10` | 21,960,000.00 USD | 0.00 USD | 21,960,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3627.30` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 30,540.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.30` | 21,820,000.00 USD | 0.00 USD | 21,820,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3631.50` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 30,160.00 USD | 0.00 USD | 55,360.00 USD |
| `7D` | `3634.50` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.70` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 30,630.00 USD | 0.00 USD | 13,460.00 USD |
| `7D` | `3638.70` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.90` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3644.10` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 14,060.00 USD | 0.00 USD | 10,260.00 USD |
| `7D` | `3647.10` | 21,490,000.00 USD | 0.00 USD | 21,490,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3648.30` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `3651.30` | 21,460,000.00 USD | 0.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3652.50` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 12,890.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.50` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.70` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3659.70` | 21,430,000.00 USD | 0.00 USD | 21,430,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3660.90` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 21,410,000.00 USD | 0.00 USD | 21,410,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 20,750,000.00 USD | 0.00 USD | 20,750,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,960,000.00 USD | 0.00 USD | 18,960,000.00 USD | 156,600.00 USD | 0.00 USD | 212,340.00 USD |
| `1D` | `3845.70` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 10,120.00 USD |
| `7D` | `3848.70` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 74,350.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3849.90` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 24,940.00 USD | 0.00 USD | 70,190.00 USD |
| `7D` | `3852.90` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 183,930.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `3854.10` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 10,670.00 USD | 0.00 USD | 53,090.00 USD |
| `7D` | `3857.10` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 248,680.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3858.30` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 22,220.00 USD | 0.00 USD | 76,220.00 USD |
| `7D` | `3861.30` | 17,370,000.00 USD | 0.00 USD | 17,370,000.00 USD | 209,570.00 USD | 0.00 USD | 532,590.00 USD |
| `1D` | `3862.50` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 74,720.00 USD | 0.00 USD | 201,260.00 USD |
| `7D` | `3865.50` | 16,630,000.00 USD | 0.00 USD | 16,630,000.00 USD | 203,250.00 USD | 0.00 USD | 370,450.00 USD |
| `1D` | `3866.70` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 55,080.00 USD | 0.00 USD | 107,070.00 USD |
| `7D` | `3869.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3870.90` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 94,930.00 USD | 0.00 USD | 116,730.00 USD |
| `7D` | `3873.90` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3875.10` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 96,090.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `3878.10` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3879.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 54,760.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `3882.30` | 14,980,000.00 USD | 0.00 USD | 14,980,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3883.50` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 33,040.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3886.50` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.70` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 20,650.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `3890.70` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.90` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `3894.90` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3896.10` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 26,000.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3899.10` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3900.30` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3903.30` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `3904.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3907.50` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 334,680.00 USD | 0.00 USD | 450,920.00 USD |
| `7D` | `3928.50` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3929.70` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 40,090.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.70` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 377,610.00 USD | 0.00 USD | 390,200.00 USD |
| `1D` | `3933.90` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 31,140.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3936.90` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 449,520.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.10` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 37,890.00 USD | 0.00 USD | 142,240.00 USD |
| `7D` | `3941.10` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 320,330.00 USD | 0.00 USD | 783,180.00 USD |
| `1D` | `3942.30` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 129,870.00 USD | 0.00 USD | 384,040.00 USD |
| `7D` | `3945.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 513,380.00 USD | 0.00 USD | 928,940.00 USD |
| `1D` | `3946.50` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 120,480.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.70` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 189,320.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3954.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 115,530.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3959.10` | 911,760.00 USD | 0.00 USD | 911,760.00 USD | 165,800.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.30` | 701,850.00 USD | 0.00 USD | 701,850.00 USD | 61,440.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.50` | 633,380.00 USD | 0.00 USD | 633,380.00 USD | 81,110.00 USD | 0.00 USD | 51,280.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.70` | 500,990.00 USD | 0.00 USD | 500,990.00 USD | 55,160.00 USD | 0.00 USD | 83,520.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.90` | 362,310.00 USD | 0.00 USD | 362,310.00 USD | 64,650.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3980.10` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3984.30` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `1D` | `3988.50` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4010.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4010.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 498,640.00 USD |
| `7D` | `4088.10` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4089.30` | 196,680.00 USD | 196,680.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `4092.30` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 286,170.00 USD | 0.00 USD | 391,950.00 USD |
| `1D` | `4093.50` | 304,680.00 USD | 304,680.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 80,080.00 USD |
| `7D` | `4096.50` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 508,690.00 USD |
| `1D` | `4097.70` | 479,260.00 USD | 479,260.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 133,100.00 USD |
| `7D` | `4100.70` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 330,780.00 USD | 0.00 USD | 732,670.00 USD |
| `1D` | `4101.90` | 775,130.00 USD | 775,130.00 USD | 0.00 USD | 87,220.00 USD | 0.00 USD | 208,650.00 USD |
| `7D` | `4104.90` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 586,230.00 USD | 0.00 USD | 893,490.00 USD |
| `1D` | `4106.10` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 127,950.00 USD | 0.00 USD | 381,000.00 USD |
| `7D` | `4109.10` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 320,370.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4110.30` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 122,700.00 USD | 0.00 USD | 111,120.00 USD |
| `7D` | `4113.30` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.50` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD | 269,000.00 USD |
| `7D` | `4117.50` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.70` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 163,150.00 USD | 0.00 USD | 124,080.00 USD |
| `7D` | `4121.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.90` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 18,770.00 USD |
| `7D` | `4125.90` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.10` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.10` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.30` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 80,280.00 USD |
| `7D` | `4134.30` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.50` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.70` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 52,000.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4142.70` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.90` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4146.90` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `1D` | `4148.10` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4151.10` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 249,320.00 USD |
| `7D` | `4167.90` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4169.10` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `4172.10` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 128,920.00 USD | 0.00 USD | 195,980.00 USD |
| `1D` | `4173.30` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 13,960.00 USD | 0.00 USD | 40,040.00 USD |
| `7D` | `4176.30` | 18,010,000.00 USD | 18,010,000.00 USD | 0.00 USD | 192,580.00 USD | 0.00 USD | 247,170.00 USD |
| `1D` | `4177.50` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 47,860.00 USD |
| `7D` | `4180.50` | 18,490,000.00 USD | 18,490,000.00 USD | 0.00 USD | 175,510.00 USD | 0.00 USD | 304,000.00 USD |
| `1D` | `4181.70` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 29,200.00 USD | 0.00 USD | 86,730.00 USD |
| `7D` | `4184.70` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 293,700.00 USD | 0.00 USD | 419,190.00 USD |
| `1D` | `4185.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 75,900.00 USD | 0.00 USD | 203,290.00 USD |
| `7D` | `4188.90` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 169,570.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4190.10` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 41,700.00 USD | 0.00 USD | 73,850.00 USD |
| `7D` | `4193.10` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4194.30` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 116,050.00 USD | 0.00 USD | 139,720.00 USD |
| `7D` | `4197.30` | 20,400,000.00 USD | 20,400,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4198.50` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 81,270.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `4201.50` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4202.70` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 39,690.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `4205.70` | 20,810,000.00 USD | 20,810,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.90` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.90` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4211.10` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `4214.10` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4215.30` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `4218.30` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4219.50` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 37,220.00 USD | 0.00 USD | 31,270.00 USD |
| `7D` | `4222.50` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.70` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 13,990.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4226.70` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4227.90` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `1D` | `4232.10` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4377.90` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,960,000.00 USD | 21,960,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 76,590.00 USD |
| `7D` | `4407.30` | 22,230,000.00 USD | 22,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4408.50` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `4411.50` | 22,300,000.00 USD | 22,300,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `4412.70` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `4415.70` | 22,390,000.00 USD | 22,390,000.00 USD | 0.00 USD | 49,730.00 USD | 0.00 USD | 41,080.00 USD |
| `1D` | `4416.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 10,100.00 USD |
| `7D` | `4419.90` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 79,360.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4421.10` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 14,440.00 USD |
| `7D` | `4424.10` | 22,690,000.00 USD | 22,690,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 103,150.00 USD |
| `1D` | `4425.30` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 11,750.00 USD | 0.00 USD | 59,900.00 USD |
| `1D` | `4426.60` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |
| `7D` | `4428.30` | 22,900,000.00 USD | 22,900,000.00 USD | 0.00 USD | 60,670.00 USD | 0.00 USD | 153,720.00 USD |
| `7D` | `4432.50` | 23,020,000.00 USD | 23,020,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.70` | 23,080,000.00 USD | 23,080,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 23,170,000.00 USD | 23,170,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `843.78M` | Total OI Tokens: `210,338.5 XAUT`
  * 1h OI Change: `-0.29%` | 4h OI Change: `-5.56%` | 24h OI Change: `+5.24%`
  * Exchange Breakdown: Binance=`62.16M` | Bybit=`144.66M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `0.0000%` | Last 24h: `0.0000%` | Last 3d: `0.0000%` | Last 7d: `0.0000%`
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
| `15M` | `XAUT` | `62.86%` | `37.14%` | `1.69` | 2,160,000.00 USD |
| `15M` | `Binance` | `59.38%` | `40.62%` | `1.46` | 670,160.00 USD |
| `15M` | `OKX` | `64.16%` | `35.84%` | `1.79` | 339,450.00 USD |
| `15M` | `Bybit` | `52.42%` | `47.58%` | `1.10` | 204,100.00 USD |
| `15M` | `KuCoin` | `46.89%` | `53.11%` | `0.88` | 18,190.00 USD |
| `15M` | `Gate` | `55.77%` | `44.23%` | `1.26` | 49,560.00 USD |
| `15M` | `Bitget` | `46.1%` | `53.9%` | `0.86` | 22,880.00 USD |
| `15M` | `BingX` | `62.33%` | `37.67%` | `1.65` | 198,070.00 USD |
| `15M` | `MEXC` | `75.7%` | `24.3%` | `3.12` | 330,210.00 USD |
| `15M` | `Bitunix` | `74.18%` | `25.82%` | `2.87` | 32,460.00 USD |
| `15M` | `Hyperliquid` | `85.33%` | `14.67%` | `5.82` | 48,440.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.56%` | `47.44%` | `1.11` | 130,020.00 USD |
| `15M` | `Crypto.com` | `59.72%` | `40.28%` | `1.48` | 2,410.00 USD |
| `15M` | `WhiteBIT` | `79.02%` | `20.98%` | `3.77` | 99,290.00 USD |
| `15M` | `HTX` | `48.8%` | `51.2%` | `0.95` | 143.84 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `99.62%` | `0.38%` | `262.16` | 269.18 USD |
| `15M` | `Aster` | `98.38%` | `1.62%` | `60.73` | 338.85 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `11.89%` | `88.11%` | `0.13` | 16,090.00 USD |
| `15M` | `Whale Positions` | `59.38%` | `40.62%` | `1.46` | 670,160.00 USD |
| `15M` | `Global Accounts` | `62.86%` | `37.14%` | `1.69` | 2,160,000.00 USD |
| `1H` | `XAUT` | `52.71%` | `47.29%` | `1.11` | 9,770,000.00 USD |
| `1H` | `Binance` | `52.01%` | `47.99%` | `1.08` | 3,710,000.00 USD |
| `1H` | `OKX` | `51.55%` | `48.45%` | `1.06` | 1,760,000.00 USD |
| `1H` | `Bybit` | `52.82%` | `47.18%` | `1.12` | 868,410.00 USD |
| `1H` | `KuCoin` | `51.64%` | `48.36%` | `1.07` | 113,210.00 USD |
| `1H` | `Gate` | `42.54%` | `57.46%` | `0.74` | 425,310.00 USD |
| `1H` | `Bitget` | `55.13%` | `44.87%` | `1.23` | 391,070.00 USD |
| `1H` | `BingX` | `47.72%` | `52.28%` | `0.91` | 421,220.00 USD |
| `1H` | `MEXC` | `57.72%` | `42.28%` | `1.37` | 873,730.00 USD |
| `1H` | `Bitunix` | `56.33%` | `43.67%` | `1.29` | 152,820.00 USD |
| `1H` | `Hyperliquid` | `63.89%` | `36.11%` | `1.77` | 140,750.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.33%` | `49.67%` | `1.01` | 502,440.00 USD |
| `1H` | `Crypto.com` | `46.98%` | `53.02%` | `0.89` | 7,870.00 USD |
| `1H` | `WhiteBIT` | `74.82%` | `25.18%` | `2.97` | 308,130.00 USD |
| `1H` | `HTX` | `48.14%` | `51.86%` | `0.93` | 607.65 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `18.4%` | `81.6%` | `0.23` | 50,960.00 USD |
| `1H` | `Aster` | `17.54%` | `82.46%` | `0.21` | 2,850.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.05%` | `49.95%` | `1.00` | 40,150.00 USD |
| `1H` | `Whale Positions` | `52.01%` | `47.99%` | `1.08` | 3,710,000.00 USD |
| `1H` | `Global Accounts` | `52.71%` | `47.29%` | `1.11` | 9,770,000.00 USD |
| `4H` | `XAUT` | `47.58%` | `52.42%` | `0.91` | 52,510,000.00 USD |
| `4H` | `Binance` | `45.99%` | `54.01%` | `0.85` | 19,270,000.00 USD |
| `4H` | `OKX` | `47.24%` | `52.76%` | `0.90` | 10,500,000.00 USD |
| `4H` | `Bybit` | `48.86%` | `51.14%` | `0.96` | 4,180,000.00 USD |
| `4H` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 510,210.00 USD |
| `4H` | `Gate` | `49.49%` | `50.51%` | `0.98` | 1,550,000.00 USD |
| `4H` | `Bitget` | `49.13%` | `50.87%` | `0.97` | 2,400,000.00 USD |
| `4H` | `BingX` | `34.97%` | `65.03%` | `0.54` | 2,520,000.00 USD |
| `4H` | `MEXC` | `46.36%` | `53.64%` | `0.86` | 4,700,000.00 USD |
| `4H` | `Bitunix` | `50.08%` | `49.92%` | `1.00` | 1,180,000.00 USD |
| `4H` | `Hyperliquid` | `48.6%` | `51.4%` | `0.95` | 1,510,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.51%` | `50.49%` | `0.98` | 2,490,000.00 USD |
| `4H` | `Crypto.com` | `49.61%` | `50.39%` | `0.98` | 28,160.00 USD |
| `4H` | `WhiteBIT` | `84.09%` | `15.91%` | `5.29` | 1,260,000.00 USD |
| `4H` | `HTX` | `47%` | `53%` | `0.89` | 11,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.68%` | `50.32%` | `0.99` | 164,220.00 USD |
| `4H` | `Aster` | `86.45%` | `13.55%` | `6.38` | 54,300.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.31%` | `48.69%` | `1.05` | 147,260.00 USD |
| `4H` | `Whale Positions` | `45.99%` | `54.01%` | `0.85` | 19,270,000.00 USD |
| `4H` | `Global Accounts` | `47.58%` | `52.42%` | `0.91` | 52,510,000.00 USD |


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
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -11,210.00 USD | -1,330.00 USD | **`DISTRIBUTION`** |
| `15m` | -47,750.00 USD | 74,550.00 USD | **`ACCUMULATION`** |
| `30m` | -56,870.00 USD | 112,400.00 USD | **`ACCUMULATION`** |
| `1h` | -228,150.00 USD | 398,870.00 USD | **`ACCUMULATION`** |
| `2h` | -459,490.00 USD | 454,660.00 USD | **`DISTRIBUTION`** |
| `4h` | -516,790.00 USD | 317,180.00 USD | **`DISTRIBUTION`** |
| `6h` | -994,660.00 USD | 757,600.00 USD | **`DISTRIBUTION`** |
| `8h` | -160,170.00 USD | 405,910.00 USD | **`ACCUMULATION`** |
| `12h` | 310,950.00 USD | 161,480.00 USD | **`ACCUMULATION`** |
| `24h` | -1,120,000.00 USD | 315,550.00 USD | **`DISTRIBUTION`** |
| `1w` | -82,790,000.00 USD | -20,560,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,360,000.00 USD | -85,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.21K` | 15m=`-47.75K` | 1h=`-228.15K` | 24h=`-1.12M`
* Futures Capital Netflows: 5m=`-1.33K` | 15m=`+74.55K` | 1h=`+398.87K` | 24h=`+315.55K`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26621.32` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26538.69` (Risk Distance: `82.62` pts)
  * +2.5R Take Profit: `26827.88`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26781.52` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26864.15` (Risk Distance: `82.62` pts)
  * +2.5R Take Profit: `26574.96`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26915.03`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
