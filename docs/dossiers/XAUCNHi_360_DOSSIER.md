# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 00:08:08 IST` (`2026-10-29 18:38:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26667.57` | **Live Ask Quote**: `26669.65` | **Mid Price**: `26668.61`
- **Spread Points**: `208.00` | **Spread BPS**: `0.78 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26668.61` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.67` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26855.29` | Lower -3.00σ Band: `26481.93`
  * Upper +2.51σ Band: `26815.29` | Lower -2.51σ Band: `26521.93`
  * Upper +2.01σ Band: `26780.62` | Lower -2.01σ Band: `26556.60`
  * Upper +2.00σ Band: `26775.28` | Lower -2.00σ Band: `26561.94`
  * Upper +1.28σ Band: `26743.28` | Lower -1.28σ Band: `26593.94`
  * Upper +1.00σ Band: `26721.95` | Lower -1.00σ Band: `26615.27`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26668.61` | EMA-20=`26668.61` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26668.61` (Slope: `+0.0000`) | EMA-100=`26668.61`
  * Institutional Anchors: EMA-144=`26668.61` | EMA-200=`26668.61` (Slope: `+0.0000`) | EMA-233=`26668.61`
- **Range Boundaries**: 24H High=`26935.30` | 24H Low=`26401.92` | Weekly High=`27201.98` | Weekly Low=`26135.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26748.62` (Distance: `+0.00%`)
  * Point of Control (POC) = `26668.61` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26588.60` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26775.28` | POC=`26668.61` | VAL=`26561.94`
  * Prior Day Extremes: PDH=`26828.62` | PDL=`26508.60` | PDC=`26668.61`
  * Monday Range Blueprint: High=`26801.95` | Mid=`26668.61` | Low=`26535.27`
  * Developing Weekly Value Area: Weekly VAH=`26881.96` | Weekly POC=`26668.61` | Weekly VAL=`26455.26`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26721.95` | Low=`26615.27`
  * London Session (08:00-16:00 UTC): High=`26775.28` | Low=`26561.94`
  * New York Session (13:00-21:00 UTC): High=`26828.62` | Low=`26508.60`
  * Initial Balance (First Hour): IB High=`26748.62` | IB Low=`26588.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26561.94` - `26775.28`
  * Optimal Trade Entry (OTE 0.705): `26721.95`
  * Structural Invalidation Anchor (0.786): `26881.96`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:05:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,554,498.28 USD | `6,373.65` | `4191.43` | `4009.40` | `29414.39` | 1,160,250.92 USD | `+4.54%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,338,160.27 USD | `6,319.69` | `4133.88` | `4009.40` | `13330.53` | 786,726.18 USD | `+3.10%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,920,262.84 USD | `5,717.06` | `4234.49` | `4009.40` | `27791.54` | 1,288,612.39 USD | `+5.62%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,361,019.32 USD | `4,828.91` | `4157.43` | `4009.40` | `2095.47` | -714,862.99 USD | `-3.69%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,091,814.12 USD | `3,514.69` | `4129.70` | `4009.40` | `312.44` | -422,828.10 USD | `-3.00%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,103,574.00 USD | `3,268.21` | `4228.94` | `4009.40` | `4409.57` | 717,505.13 USD | `+5.48%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,627,260.40 USD | `2,900.00` | `4364.92` | `4009.40` | `4235.59` | 1,031,015.93 USD | `+8.87%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,820,680.00 USD | `2,200.00` | `4176.09` | `4009.40` | `2460.03` | -366,739.30 USD | `-4.16%` | `25X Cross` |
| `276` | `0x41e5...0825` | `SHORT` | 8,820,020.00 USD | `2,200.00` | `4112.20` | `4009.40` | `4331.08` | 226,834.59 USD | `+2.57%` | `20X Cross` |
| `310` | `0xfc66...ca06` | `SHORT` | 7,966,235.16 USD | `1,986.89` | `4032.86` | `4009.40` | `25141.00` | 46,631.01 USD | `+0.59%` | `3X Cross` |
| `312` | `0xacb6...efbd` | `SHORT` | 7,920,044.87 USD | `1,975.37` | `4048.55` | `4009.40` | `6506.38` | 77,346.84 USD | `+0.98%` | `6X Cross` |
| `384` | `0xc26c...b8f4` | `LONG` | 6,334,658.75 USD | `1,579.95` | `4075.62` | `4009.40` | `0.000000` | -104,638.22 USD | `-1.65%` | `1X Cross` |
| `420` | `0x12d2...f97f` | `LONG` | 5,620,949.46 USD | `1,401.94` | `4278.91` | `4009.40` | `2539.37` | -377,841.12 USD | `-6.72%` | `20X Cross` |
| `576` | `0x63da...8add` | `LONG` | 4,009,400.00 USD | `1,000.00` | `4021.46` | `4009.40` | `3564.03` | -12,060.96 USD | `-0.30%` | `25X Cross` |
| `593` | `0x9aa5...58af` | `LONG` | 3,895,701.43 USD | `971.64` | `4279.98` | `4009.40` | `0.000000` | -262,907.65 USD | `-6.75%` | `20X Cross` |
| `624` | `0xf3dc...1672` | `LONG` | 3,731,723.79 USD | `930.74` | `4024.62` | `4009.40` | `3337.51` | -14,168.77 USD | `-0.38%` | `20X Cross` |
| `685` | `0x4a20...3c26` | `LONG` | 3,357,470.36 USD | `837.40` | `4599.73` | `4009.40` | `0.000000` | -494,350.02 USD | `-14.72%` | `20X Cross` |
| `769` | `0x354b...6425` | `LONG` | 3,068,443.94 USD | `765.31` | `4035.10` | `4009.40` | `0.000000` | -19,669.04 USD | `-0.64%` | `10X Cross` |
| `846` | `0x0fac...7a0a` | `LONG` | 2,752,392.96 USD | `686.49` | `4290.34` | `4009.40` | `1252.08` | -192,865.74 USD | `-7.01%` | `25X Cross` |
| `879` | `0xd8c5...99b0` | `SHORT` | 2,593,876.92 USD | `646.95` | `4175.35` | `4009.40` | `31979.27` | 107,365.85 USD | `+4.14%` | `4X Cross` |
| `921` | `0x625e...a354` | `SHORT` | 2,485,642.00 USD | `620.00` | `4122.81` | `4009.40` | `4342.18` | 70,505.03 USD | `+2.84%` | `20X Cross` |
| `951` | `0xeae3...e8ad` | `SHORT` | 2,405,640.00 USD | `600.00` | `4104.77` | `4009.40` | `4325.20` | 57,225.11 USD | `+2.38%` | `20X Cross` |
| `953` | `0xf285...fa82` | `LONG` | 2,398,045.80 USD | `598.11` | `4146.45` | `4009.40` | `3891.17` | -81,973.76 USD | `-3.42%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,347,947.54 USD | `585.61` | `4082.77` | `4009.40` | `2208.52` | -42,969.44 USD | `-1.83%` | `10X Cross` |
| `1127` | `0x413c...886c` | `LONG` | 2,004,700.00 USD | `500.00` | `4010.43` | `4009.40` | `0.000000` | -516.23 USD | `-0.03%` | `2X Cross` |
| `1134` | `0x61ce...a62b` | `SHORT` | 1,994,690.53 USD | `497.50` | `4071.66` | `4009.40` | `4691.91` | 30,978.26 USD | `+1.55%` | `20X Cross` |
| `1141` | `0x0593...40f9` | `LONG` | 1,989,372.06 USD | `496.18` | `4024.57` | `4009.40` | `3701.65` | -7,531.76 USD | `-0.38%` | `10X Isolated` |
| `1253` | `0xead5...69f2` | `LONG` | 1,819,401.17 USD | `453.78` | `4220.88` | `4009.40` | `3538.86` | -95,966.89 USD | `-5.27%` | `5X Isolated` |
| `1378` | `0x46fc...1195` | `LONG` | 1,631,940.07 USD | `407.03` | `4055.53` | `4009.40` | `1932.06` | -18,779.75 USD | `-1.15%` | `20X Cross` |
| `1417` | `0xee02...309d` | `SHORT` | 1,603,760.00 USD | `400.00` | `4438.84` | `4009.40` | `4226.81` | 171,778.60 USD | `+10.71%` | `25X Isolated` |
| `1418` | `0x6d15...d374` | `LONG` | 1,603,640.00 USD | `400.00` | `4068.25` | `4009.40` | `3841.73` | -23,660.00 USD | `-1.48%` | `25X Cross` |
| `1445` | `0x02a7...fe9f` | `SHORT` | 1,563,666.00 USD | `390.00` | `4055.02` | `4009.40` | `4306.63` | 17,793.25 USD | `+1.14%` | `25X Cross` |
| `1484` | `0x7e77...b8d2` | `SHORT` | 1,523,572.00 USD | `380.00` | `4131.92` | `4009.40` | `4293.44` | 46,557.64 USD | `+3.06%` | `20X Cross` |
| `1504` | `0x72c2...9b37` | `LONG` | 1,496,032.63 USD | `373.13` | `4000.98` | `4009.40` | `3777.97` | 3,139.12 USD | `+0.21%` | `13X Isolated` |
| `1538` | `0xaa44...b844` | `LONG` | 1,443,384.00 USD | `360.00` | `4043.10` | `4009.40` | `2818.35` | -12,133.63 USD | `-0.84%` | `9X Cross` |
| `1649` | `0xa41f...d50a` | `LONG` | 1,318,940.64 USD | `328.96` | `4468.89` | `4009.40` | `3833.11` | -151,157.21 USD | `-11.46%` | `15X Cross` |
| `1680` | `0x49e9...e1d0` | `SHORT` | 1,297,270.64 USD | `323.56` | `4025.23` | `4009.40` | `28321.95` | 5,122.06 USD | `+0.39%` | `4X Cross` |
| `1708` | `0xada6...6f88` | `LONG` | 1,280,103.59 USD | `319.28` | `4166.46` | `4009.40` | `1878.13` | -50,146.92 USD | `-3.92%` | `5X Cross` |
| `1715` | `0xbf5a...88ba` | `SHORT` | 1,273,605.56 USD | `317.65` | `4091.80` | `4009.40` | `10477.92` | 26,177.48 USD | `+2.06%` | `20X Cross` |
| `1733` | `0xff31...ff6c` | `SHORT` | 1,242,914.00 USD | `310.00` | `4372.43` | `4009.40` | `4789.11` | 112,541.38 USD | `+9.05%` | `10X Isolated` |
| `1898` | `0x50e2...d770` | `LONG` | 1,084,011.05 USD | `270.37` | `4243.58` | `4009.40` | `2562.02` | -63,315.41 USD | `-5.84%` | `20X Cross` |
| `1915` | `0x4c92...4f17` | `SHORT` | 1,069,389.17 USD | `266.72` | `4260.98` | `4009.40` | `6524.64` | 67,103.06 USD | `+6.27%` | `20X Cross` |
| `1985` | `0xd346...c4f3` | `LONG` | 1,023,093.83 USD | `255.17` | `4188.66` | `4009.40` | `3310.35` | -45,742.67 USD | `-4.47%` | `5X Isolated` |
| `2020` | `0xe47f...758c` | `LONG` | 1,002,350.00 USD | `250.00` | `4020.00` | `4009.40` | `3774.26` | -2,650.00 USD | `-0.26%` | `20X Cross` |
| `2021` | `0x1581...463b` | `LONG` | 1,002,325.00 USD | `250.00` | `4003.77` | `4009.40` | `3504.56` | 1,381.41 USD | `+0.14%` | `15X Cross` |

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
| `7D` | `3605.80` | 22,820,000.00 USD | 0.00 USD | 22,820,000.00 USD | 23,790.00 USD | 0.00 USD | 104,480.00 USD |
| `1D` | `3607.00` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,220.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `3610.00` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 26,640.00 USD | 0.00 USD | 65,410.00 USD |
| `1D` | `3611.20` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 4,870.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `3614.20` | 22,600,000.00 USD | 0.00 USD | 22,600,000.00 USD | 71,890.00 USD | 0.00 USD | 70,630.00 USD |
| `1D` | `3615.40` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 8,720.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3618.40` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 51,620.00 USD | 0.00 USD | 114,120.00 USD |
| `1D` | `3619.60` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 10,130.00 USD | 0.00 USD | 38,410.00 USD |
| `7D` | `3622.60` | 22,290,000.00 USD | 0.00 USD | 22,290,000.00 USD | 94,230.00 USD | 0.00 USD | 172,800.00 USD |
| `1D` | `3623.80` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 19,570.00 USD | 0.00 USD | 56,930.00 USD |
| `7D` | `3626.80` | 22,020,000.00 USD | 0.00 USD | 22,020,000.00 USD | 64,220.00 USD | 0.00 USD | 61,730.00 USD |
| `1D` | `3628.00` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 27,960.00 USD | 0.00 USD | 20,720.00 USD |
| `7D` | `3631.00` | 21,890,000.00 USD | 0.00 USD | 21,890,000.00 USD | 29,730.00 USD | 0.00 USD | 69,740.00 USD |
| `1D` | `3632.20` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 28,830.00 USD | 0.00 USD | 57,040.00 USD |
| `7D` | `3635.20` | 21,800,000.00 USD | 0.00 USD | 21,800,000.00 USD | 61,800.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `3636.40` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 31,320.00 USD | 0.00 USD | 4,870.00 USD |
| `7D` | `3639.40` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 68,420.00 USD | 0.00 USD | 12,090.00 USD |
| `1D` | `3640.60` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 15,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.60` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 20,110.00 USD | 0.00 USD | 7,240.00 USD |
| `1D` | `3644.80` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 9,850.00 USD | 0.00 USD | 12,850.00 USD |
| `7D` | `3647.80` | 21,590,000.00 USD | 0.00 USD | 21,590,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3649.00` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 18,180.00 USD | 0.00 USD | 18,720.00 USD |
| `1D` | `3653.20` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 10,400.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3656.20` | 21,550,000.00 USD | 0.00 USD | 21,550,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3657.40` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3660.40` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3661.60` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3820.00` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3828.40` | 21,510,000.00 USD | 0.00 USD | 21,510,000.00 USD | 80,570.00 USD | 0.00 USD | 146,810.00 USD |
| `7D` | `3832.60` | 21,290,000.00 USD | 0.00 USD | 21,290,000.00 USD | 186,160.00 USD | 0.00 USD | 335,840.00 USD |
| `7D` | `3836.80` | 20,760,000.00 USD | 0.00 USD | 20,760,000.00 USD | 306,530.00 USD | 0.00 USD | 785,310.00 USD |
| `7D` | `3841.00` | 19,670,000.00 USD | 0.00 USD | 19,670,000.00 USD | 330,550.00 USD | 0.00 USD | 399,250.00 USD |
| `7D` | `3845.20` | 18,940,000.00 USD | 0.00 USD | 18,940,000.00 USD | 144,760.00 USD | 0.00 USD | 269,910.00 USD |
| `1D` | `3846.40` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 8,040.00 USD | 0.00 USD | 37,460.00 USD |
| `7D` | `3849.40` | 18,530,000.00 USD | 0.00 USD | 18,530,000.00 USD | 63,670.00 USD | 0.00 USD | 204,330.00 USD |
| `1D` | `3850.60` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 12,720.00 USD | 0.00 USD | 46,810.00 USD |
| `7D` | `3853.60` | 18,260,000.00 USD | 0.00 USD | 18,260,000.00 USD | 189,560.00 USD | 0.00 USD | 223,000.00 USD |
| `1D` | `3854.80` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 10,670.00 USD | 0.00 USD | 70,970.00 USD |
| `7D` | `3857.80` | 17,850,000.00 USD | 0.00 USD | 17,850,000.00 USD | 217,240.00 USD | 0.00 USD | 359,600.00 USD |
| `1D` | `3859.00` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 25,870.00 USD | 0.00 USD | 76,720.00 USD |
| `7D` | `3862.00` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 243,100.00 USD | 0.00 USD | 410,430.00 USD |
| `1D` | `3863.20` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 86,170.00 USD | 0.00 USD | 207,740.00 USD |
| `7D` | `3866.20` | 16,620,000.00 USD | 0.00 USD | 16,620,000.00 USD | 226,420.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `3867.40` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 44,180.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `3870.40` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 204,870.00 USD | 0.00 USD | 281,590.00 USD |
| `1D` | `3871.60` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 124,160.00 USD | 0.00 USD | 144,120.00 USD |
| `7D` | `3874.60` | 15,580,000.00 USD | 0.00 USD | 15,580,000.00 USD | 160,800.00 USD | 0.00 USD | 205,270.00 USD |
| `1D` | `3875.80` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 96,190.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `3878.80` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 212,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3880.00` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 38,130.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `3883.00` | 15,010,000.00 USD | 0.00 USD | 15,010,000.00 USD | 144,390.00 USD | 0.00 USD | 90,800.00 USD |
| `1D` | `3884.20` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3887.20` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 97,860.00 USD | 0.00 USD | 51,400.00 USD |
| `1D` | `3888.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 34,730.00 USD | 0.00 USD | 40,140.00 USD |
| `7D` | `3891.40` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 38,150.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3892.60` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 44,440.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `3895.60` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3896.80` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 27,790.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3899.80` | 14,490,000.00 USD | 0.00 USD | 14,490,000.00 USD | 80,390.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3901.00` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 23,490.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3904.00` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `3905.20` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3908.20` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 202,620.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `3912.40` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 330,850.00 USD | 0.00 USD | 671,680.00 USD |
| `7D` | `3916.60` | 12,830,000.00 USD | 0.00 USD | 12,830,000.00 USD | 581,260.00 USD | 0.00 USD | 1,500,000.00 USD |
| `7D` | `3920.80` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 692,900.00 USD | 0.00 USD | 764,600.00 USD |
| `7D` | `3925.00` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 216,570.00 USD | 0.00 USD | 495,550.00 USD |
| `1D` | `3926.20` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3929.20` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 167,220.00 USD | 0.00 USD | 481,590.00 USD |
| `1D` | `3930.40` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 41,530.00 USD | 0.00 USD | 148,300.00 USD |
| `7D` | `3933.40` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 366,580.00 USD | 0.00 USD | 392,240.00 USD |
| `1D` | `3934.60` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 21,350.00 USD | 0.00 USD | 98,260.00 USD |
| `7D` | `3937.60` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 480,120.00 USD | 0.00 USD | 555,530.00 USD |
| `1D` | `3938.80` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 47,170.00 USD | 0.00 USD | 152,440.00 USD |
| `7D` | `3941.80` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 419,140.00 USD | 0.00 USD | 954,580.00 USD |
| `1D` | `3943.00` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 146,710.00 USD | 0.00 USD | 420,100.00 USD |
| `7D` | `3946.00` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 406,490.00 USD | 0.00 USD | 721,780.00 USD |
| `1D` | `3947.20` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 110,160.00 USD | 0.00 USD | 196,560.00 USD |
| `7D` | `3950.20` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 505,590.00 USD | 0.00 USD | 510,700.00 USD |
| `1D` | `3951.40` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 190,450.00 USD | 0.00 USD | 222,910.00 USD |
| `7D` | `3954.40` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 253,690.00 USD | 0.00 USD | 447,920.00 USD |
| `1D` | `3955.60` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 182,380.00 USD | 0.00 USD | 199,600.00 USD |
| `7D` | `3958.60` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 393,960.00 USD | 0.00 USD | 93,670.00 USD |
| `1D` | `3959.80` | 885,020.00 USD | 0.00 USD | 885,020.00 USD | 133,860.00 USD | 0.00 USD | 23,580.00 USD |
| `7D` | `3962.80` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 378,040.00 USD | 0.00 USD | 128,640.00 USD |
| `1D` | `3964.00` | 727,580.00 USD | 0.00 USD | 727,580.00 USD | 67,780.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3967.00` | 920,110.00 USD | 0.00 USD | 920,110.00 USD | 147,940.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3968.20` | 652,770.00 USD | 0.00 USD | 652,770.00 USD | 71,380.00 USD | 0.00 USD | 64,250.00 USD |
| `7D` | `3971.20` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3972.40` | 517,140.00 USD | 0.00 USD | 517,140.00 USD | 65,170.00 USD | 0.00 USD | 93,600.00 USD |
| `7D` | `3975.40` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 47,520.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3976.60` | 358,370.00 USD | 0.00 USD | 358,370.00 USD | 101,010.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `3979.60` | 306,520.00 USD | 0.00 USD | 306,520.00 USD | 125,730.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3980.80` | 217,870.00 USD | 0.00 USD | 217,870.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `3983.80` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3985.00` | 27,730.00 USD | 0.00 USD | 27,730.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4005.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4006.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.80` | 366,820.00 USD | 366,820.00 USD | 0.00 USD | 73,200.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `4072.00` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 330,850.00 USD | 0.00 USD | 671,680.00 USD |
| `7D` | `4076.20` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 581,260.00 USD | 0.00 USD | 1,460,000.00 USD |
| `7D` | `4080.40` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 596,280.00 USD | 0.00 USD | 780,680.00 USD |
| `7D` | `4084.60` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 280,380.00 USD | 0.00 USD | 401,520.00 USD |
| `1D` | `4085.80` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.80` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `4090.00` | 192,370.00 USD | 192,370.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4093.00` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 284,270.00 USD | 0.00 USD | 390,200.00 USD |
| `1D` | `4094.20` | 303,130.00 USD | 303,130.00 USD | 0.00 USD | 23,870.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4097.20` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 523,650.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `4098.40` | 482,770.00 USD | 482,770.00 USD | 0.00 USD | 45,160.00 USD | 0.00 USD | 134,480.00 USD |
| `7D` | `4101.40` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 283,320.00 USD | 0.00 USD | 765,580.00 USD |
| `1D` | `4102.60` | 840,700.00 USD | 840,700.00 USD | 0.00 USD | 95,210.00 USD | 0.00 USD | 262,720.00 USD |
| `7D` | `4105.60` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 502,900.00 USD | 0.00 USD | 904,040.00 USD |
| `1D` | `4106.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 148,830.00 USD | 0.00 USD | 330,980.00 USD |
| `7D` | `4109.80` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 445,660.00 USD | 0.00 USD | 479,890.00 USD |
| `1D` | `4111.00` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 160,190.00 USD | 0.00 USD | 110,410.00 USD |
| `7D` | `4114.00` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 226,890.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4115.20` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 182,530.00 USD | 0.00 USD | 307,850.00 USD |
| `7D` | `4118.20` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 450,490.00 USD | 0.00 USD | 368,710.00 USD |
| `1D` | `4119.40` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 154,350.00 USD | 0.00 USD | 86,190.00 USD |
| `7D` | `4122.40` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 370,840.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.60` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 50,390.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `4126.60` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 278,030.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.80` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 103,560.00 USD | 0.00 USD | 32,390.00 USD |
| `7D` | `4130.80` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 95,190.00 USD | 0.00 USD | 195,890.00 USD |
| `1D` | `4132.00` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 58,250.00 USD | 0.00 USD | 62,610.00 USD |
| `7D` | `4135.00` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `4136.20` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 85,040.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4139.20` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4140.40` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 43,400.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4143.40` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 133,450.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4144.60` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4147.60` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 91,260.00 USD | 0.00 USD | 181,250.00 USD |
| `1D` | `4148.80` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4151.80` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 157,490.00 USD | 0.00 USD | 284,670.00 USD |
| `7D` | `4156.00` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 298,560.00 USD | 0.00 USD | 659,320.00 USD |
| `7D` | `4160.20` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 284,560.00 USD | 0.00 USD | 488,930.00 USD |
| `7D` | `4164.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 153,770.00 USD | 0.00 USD | 214,320.00 USD |
| `7D` | `4168.60` | 17,370,000.00 USD | 17,370,000.00 USD | 0.00 USD | 82,260.00 USD | 0.00 USD | 289,910.00 USD |
| `1D` | `4169.80` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 15,870.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `4172.80` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 136,220.00 USD | 0.00 USD | 146,240.00 USD |
| `1D` | `4174.00` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 11,930.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `4177.00` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 219,700.00 USD | 0.00 USD | 254,350.00 USD |
| `1D` | `4178.20` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 20,740.00 USD | 0.00 USD | 63,150.00 USD |
| `7D` | `4181.20` | 18,640,000.00 USD | 18,640,000.00 USD | 0.00 USD | 148,050.00 USD | 0.00 USD | 366,340.00 USD |
| `1D` | `4182.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 43,610.00 USD | 0.00 USD | 104,330.00 USD |
| `7D` | `4185.40` | 19,380,000.00 USD | 19,380,000.00 USD | 0.00 USD | 293,120.00 USD | 0.00 USD | 446,750.00 USD |
| `1D` | `4186.60` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 63,970.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `4189.60` | 19,810,000.00 USD | 19,810,000.00 USD | 0.00 USD | 160,180.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `4190.80` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 61,350.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `4193.80` | 20,170,000.00 USD | 20,170,000.00 USD | 0.00 USD | 166,830.00 USD | 0.00 USD | 187,190.00 USD |
| `1D` | `4195.00` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 105,290.00 USD | 0.00 USD | 134,500.00 USD |
| `7D` | `4198.00` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 158,130.00 USD | 0.00 USD | 184,350.00 USD |
| `1D` | `4199.20` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 88,290.00 USD | 0.00 USD | 62,040.00 USD |
| `7D` | `4202.20` | 20,730,000.00 USD | 20,730,000.00 USD | 0.00 USD | 206,140.00 USD | 0.00 USD | 18,540.00 USD |
| `1D` | `4203.40` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 35,070.00 USD | 0.00 USD | 7,160.00 USD |
| `7D` | `4206.40` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 144,390.00 USD | 0.00 USD | 72,260.00 USD |
| `1D` | `4207.60` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `4210.60` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 67,010.00 USD | 0.00 USD | 51,400.00 USD |
| `1D` | `4211.80` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 24,650.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `4214.80` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `4216.00` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 32,960.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `4219.00` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4220.20` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 47,570.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `4223.20` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4224.40` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `4227.40` | 21,370,000.00 USD | 21,370,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4228.60` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 10,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4232.80` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4378.60` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4382.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4387.00` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 29,060.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4391.20` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 50,030.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4395.40` | 21,820,000.00 USD | 21,820,000.00 USD | 0.00 USD | 71,530.00 USD | 0.00 USD | 157,250.00 USD |
| `7D` | `4399.60` | 22,110,000.00 USD | 22,110,000.00 USD | 0.00 USD | 100,870.00 USD | 0.00 USD | 185,870.00 USD |
| `7D` | `4403.80` | 22,230,000.00 USD | 22,230,000.00 USD | 0.00 USD | 55,000.00 USD | 0.00 USD | 67,000.00 USD |
| `7D` | `4408.00` | 22,340,000.00 USD | 22,340,000.00 USD | 0.00 USD | 25,640.00 USD | 0.00 USD | 82,740.00 USD |
| `1D` | `4409.20` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 23,310.00 USD |
| `7D` | `4412.20` | 22,420,000.00 USD | 22,420,000.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 58,200.00 USD |
| `1D` | `4413.40` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 16,680.00 USD |
| `7D` | `4416.40` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 71,890.00 USD | 0.00 USD | 46,470.00 USD |
| `1D` | `4417.60` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `4420.60` | 22,680,000.00 USD | 22,680,000.00 USD | 0.00 USD | 45,100.00 USD | 0.00 USD | 101,600.00 USD |
| `1D` | `4421.80` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 5,910.00 USD | 0.00 USD | 18,190.00 USD |
| `7D` | `4424.80` | 22,860,000.00 USD | 22,860,000.00 USD | 0.00 USD | 51,730.00 USD | 0.00 USD | 124,410.00 USD |
| `1D` | `4426.00` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 16,740.00 USD | 0.00 USD | 61,140.00 USD |
| `1D` | `4426.50` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,810.00 USD |
| `7D` | `4429.00` | 23,020,000.00 USD | 23,020,000.00 USD | 0.00 USD | 56,250.00 USD | 0.00 USD | 105,180.00 USD |
| `7D` | `4433.20` | 23,130,000.00 USD | 23,130,000.00 USD | 0.00 USD | 62,470.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `4437.40` | 23,210,000.00 USD | 23,210,000.00 USD | 0.00 USD | 24,240.00 USD | 0.00 USD | 51,070.00 USD |
| `7D` | `4440.40` | 23,280,000.00 USD | 23,280,000.00 USD | 0.00 USD | 29,840.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `844.28M` | Total OI Tokens: `210,693.5 XAUT`
  * 1h OI Change: `+0.34%` | 4h OI Change: `-2.71%` | 24h OI Change: `+5.35%`
  * Exchange Breakdown: Binance=`62.10M` | Bybit=`144.54M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `42.31%` | `57.69%` | `0.73` | 3,280,000.00 USD |
| `15M` | `Binance` | `45.65%` | `54.35%` | `0.84` | 1,160,000.00 USD |
| `15M` | `OKX` | `34.43%` | `65.57%` | `0.53` | 639,550.00 USD |
| `15M` | `Bybit` | `39.46%` | `60.54%` | `0.65` | 307,040.00 USD |
| `15M` | `KuCoin` | `51.07%` | `48.93%` | `1.04` | 29,330.00 USD |
| `15M` | `Gate` | `39.1%` | `60.9%` | `0.64` | 210,230.00 USD |
| `15M` | `Bitget` | `53.65%` | `46.35%` | `1.16` | 121,660.00 USD |
| `15M` | `BingX` | `27.22%` | `72.78%` | `0.37` | 91,570.00 USD |
| `15M` | `MEXC` | `37.03%` | `62.97%` | `0.59` | 360,810.00 USD |
| `15M` | `Bitunix` | `47.07%` | `52.93%` | `0.89` | 43,190.00 USD |
| `15M` | `Hyperliquid` | `38.42%` | `61.58%` | `0.62` | 36,440.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.13%` | `50.87%` | `0.97` | 179,680.00 USD |
| `15M` | `Crypto.com` | `65.19%` | `34.81%` | `1.87` | 2,220.00 USD |
| `15M` | `WhiteBIT` | `83.92%` | `16.08%` | `5.22` | 78,540.00 USD |
| `15M` | `HTX` | `48.68%` | `51.32%` | `0.95` | 123.98 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `12.94%` | `87.06%` | `0.15` | 5,670.00 USD |
| `15M` | `Aster` | `1.09%` | `98.91%` | `0.01` | 1,040.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `36.95%` | `63.05%` | `0.59` | 6,500.00 USD |
| `15M` | `Whale Positions` | `45.65%` | `54.35%` | `0.84` | 1,160,000.00 USD |
| `15M` | `Global Accounts` | `42.31%` | `57.69%` | `0.73` | 3,280,000.00 USD |
| `1H` | `XAUT` | `45.02%` | `54.98%` | `0.82` | 12,550,000.00 USD |
| `1H` | `Binance` | `47.33%` | `52.67%` | `0.90` | 5,030,000.00 USD |
| `1H` | `OKX` | `43.62%` | `56.38%` | `0.77` | 2,130,000.00 USD |
| `1H` | `Bybit` | `49.09%` | `50.91%` | `0.96` | 1,020,000.00 USD |
| `1H` | `KuCoin` | `49.47%` | `50.53%` | `0.98` | 134,770.00 USD |
| `1H` | `Gate` | `44.2%` | `55.8%` | `0.79` | 624,390.00 USD |
| `1H` | `Bitget` | `41.22%` | `58.78%` | `0.70` | 528,010.00 USD |
| `1H` | `BingX` | `14.74%` | `85.26%` | `0.17` | 670,250.00 USD |
| `1H` | `MEXC` | `45.44%` | `54.56%` | `0.83` | 1,050,000.00 USD |
| `1H` | `Bitunix` | `45.89%` | `54.11%` | `0.85` | 191,910.00 USD |
| `1H` | `Hyperliquid` | `39.72%` | `60.28%` | `0.66` | 215,180.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.41%` | `50.59%` | `0.98` | 585,530.00 USD |
| `1H` | `Crypto.com` | `59.18%` | `40.82%` | `1.45` | 7,860.00 USD |
| `1H` | `WhiteBIT` | `80.79%` | `19.21%` | `4.21` | 263,730.00 USD |
| `1H` | `HTX` | `19.17%` | `80.83%` | `0.24` | 1,470.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.4%` | `80.6%` | `0.24` | 59,100.00 USD |
| `1H` | `Aster` | `7.12%` | `92.88%` | `0.08` | 3,780.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.26%` | `67.74%` | `0.48` | 34,810.00 USD |
| `1H` | `Whale Positions` | `47.33%` | `52.67%` | `0.90` | 5,030,000.00 USD |
| `1H` | `Global Accounts` | `45.02%` | `54.98%` | `0.82` | 12,550,000.00 USD |
| `4H` | `XAUT` | `45.87%` | `54.13%` | `0.85` | 58,090,000.00 USD |
| `4H` | `Binance` | `44.51%` | `55.49%` | `0.80` | 21,690,000.00 USD |
| `4H` | `OKX` | `46.34%` | `53.66%` | `0.86` | 11,700,000.00 USD |
| `4H` | `Bybit` | `46.93%` | `53.07%` | `0.88` | 4,670,000.00 USD |
| `4H` | `KuCoin` | `47.89%` | `52.11%` | `0.92` | 571,850.00 USD |
| `4H` | `Gate` | `47.52%` | `52.48%` | `0.91` | 1,700,000.00 USD |
| `4H` | `Bitget` | `45.32%` | `54.68%` | `0.83` | 2,800,000.00 USD |
| `4H` | `BingX` | `31.23%` | `68.77%` | `0.45` | 3,030,000.00 USD |
| `4H` | `MEXC` | `44.54%` | `55.46%` | `0.80` | 4,760,000.00 USD |
| `4H` | `Bitunix` | `48.72%` | `51.28%` | `0.95` | 1,310,000.00 USD |
| `4H` | `Hyperliquid` | `49.6%` | `50.4%` | `0.98` | 1,660,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.15%` | `50.85%` | `0.97` | 2,550,000.00 USD |
| `4H` | `Crypto.com` | `53.44%` | `46.56%` | `1.15` | 29,040.00 USD |
| `4H` | `WhiteBIT` | `84.17%` | `15.83%` | `5.32` | 1,220,000.00 USD |
| `4H` | `HTX` | `41.16%` | `58.84%` | `0.70` | 12,680.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.56%` | `53.44%` | `0.87` | 178,690.00 USD |
| `4H` | `Aster` | `83.33%` | `16.67%` | `5.00` | 56,560.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.81%` | `54.19%` | `0.85` | 135,870.00 USD |
| `4H` | `Whale Positions` | `44.51%` | `55.49%` | `0.80` | 21,690,000.00 USD |
| `4H` | `Global Accounts` | `45.87%` | `54.13%` | `0.85` | 58,090,000.00 USD |


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
| `5m` | -27,400.00 USD | 44,030.00 USD | **`ACCUMULATION`** |
| `15m` | -172,620.00 USD | 74,040.00 USD | **`DISTRIBUTION`** |
| `30m` | -182,070.00 USD | 395,170.00 USD | **`ACCUMULATION`** |
| `1h` | -327,620.00 USD | 427,380.00 USD | **`ACCUMULATION`** |
| `2h` | -496,510.00 USD | 314,700.00 USD | **`DISTRIBUTION`** |
| `4h` | -562,210.00 USD | 410,620.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,320,000.00 USD | 373,410.00 USD | **`DISTRIBUTION`** |
| `8h` | 261,700.00 USD | 327,470.00 USD | **`ACCUMULATION`** |
| `12h` | 1,830,000.00 USD | 998,220.00 USD | **`ACCUMULATION`** |
| `24h` | -1,090,000.00 USD | 438,230.00 USD | **`DISTRIBUTION`** |
| `1w` | -84,190,000.00 USD | -20,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,080,000.00 USD | -85,050,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-27.40K` | 15m=`-172.62K` | 1h=`-327.62K` | 24h=`-1.09M`
* Futures Capital Netflows: 5m=`+44.03K` | 15m=`+74.04K` | 1h=`+427.38K` | 24h=`+438.23K`
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
  * `2026-10-29 23:31:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:27 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:27 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26588.60` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26505.48` (Risk Distance: `83.13` pts)
  * +2.5R Take Profit: `26796.42`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26748.62` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26831.74` (Risk Distance: `83.13` pts)
  * +2.5R Take Profit: `26540.80`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26881.96`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
