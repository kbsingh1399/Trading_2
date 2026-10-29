# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26704.89` | **Live Ask Quote**: `26707.07` | **Mid Price**: `26705.98`
- **Spread Points**: `218.00` | **Spread BPS**: `0.82 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26705.98` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.76` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26892.92` | Lower -3.00σ Band: `26519.04`
  * Upper +2.51σ Band: `26852.86` | Lower -2.51σ Band: `26559.10`
  * Upper +2.01σ Band: `26818.15` | Lower -2.01σ Band: `26593.81`
  * Upper +2.00σ Band: `26812.80` | Lower -2.00σ Band: `26599.16`
  * Upper +1.28σ Band: `26780.76` | Lower -1.28σ Band: `26631.20`
  * Upper +1.00σ Band: `26759.39` | Lower -1.00σ Band: `26652.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26705.98` | EMA-20=`26705.98` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26705.98` (Slope: `+0.0000`) | EMA-100=`26705.98`
  * Institutional Anchors: EMA-144=`26705.98` | EMA-200=`26705.98` (Slope: `+0.0000`) | EMA-233=`26705.98`
- **Range Boundaries**: 24H High=`26973.04` | 24H Low=`26438.92` | Weekly High=`27240.10` | Weekly Low=`26171.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26786.10` (Distance: `+0.00%`)
  * Point of Control (POC) = `26705.98` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26625.86` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26812.80` | POC=`26705.98` | VAL=`26599.16`
  * Prior Day Extremes: PDH=`26866.22` | PDL=`26545.74` | PDC=`26705.98`
  * Monday Range Blueprint: High=`26839.51` | Mid=`26705.98` | Low=`26572.45`
  * Developing Weekly Value Area: Weekly VAH=`26919.63` | Weekly POC=`26705.98` | Weekly VAL=`26492.33`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26759.39` | Low=`26652.57`
  * London Session (08:00-16:00 UTC): High=`26812.80` | Low=`26599.16`
  * New York Session (13:00-21:00 UTC): High=`26866.22` | Low=`26545.74`
  * Initial Balance (First Hour): IB High=`26786.10` | IB Low=`26625.86`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26599.16` - `26812.80`
  * Optimal Trade Entry (OTE 0.705): `26759.39`
  * Structural Invalidation Anchor (0.786): `26919.63`

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
| `1225` | `0xead5...69f2` | `LONG` | 1,822,078.49 USD | `453.78` | `4220.88` | `4015.10` | `3538.97` | -93,289.57 USD | `-5.12%` | `5X Isolated` |
| `1315` | `0x46fc...1195` | `LONG` | 1,671,854.72 USD | `416.39` | `4054.56` | `4015.10` | `2203.96` | -16,431.27 USD | `-0.98%` | `20X Cross` |
| `1369` | `0x6d15...d374` | `LONG` | 1,606,040.00 USD | `400.00` | `4068.25` | `4015.10` | `3841.84` | -21,260.00 USD | `-1.32%` | `25X Cross` |
| `1370` | `0xee02...309d` | `SHORT` | 1,605,920.00 USD | `400.00` | `4438.84` | `4015.10` | `4226.91` | 169,618.60 USD | `+10.56%` | `25X Isolated` |
| `1407` | `0x02a7...fe9f` | `SHORT` | 1,565,889.00 USD | `390.00` | `4055.02` | `4015.10` | `4306.73` | 15,570.25 USD | `+0.99%` | `25X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,525,624.00 USD | `380.00` | `4131.92` | `4015.10` | `4293.54` | 44,505.64 USD | `+2.92%` | `20X Cross` |
| `1463` | `0x9c06...0560` | `LONG` | 1,498,679.84 USD | `373.26` | `4018.98` | `4015.10` | `0.000000` | -1,451.97 USD | `-0.10%` | `25X Cross` |
| `1464` | `0x72c2...9b37` | `LONG` | 1,498,159.48 USD | `373.13` | `4000.98` | `4015.10` | `3778.07` | 5,265.97 USD | `+0.35%` | `13X Isolated` |
| `1507` | `0xaa44...b844` | `LONG` | 1,445,364.00 USD | `360.00` | `4043.10` | `4015.10` | `2822.64` | -10,153.63 USD | `-0.70%` | `4X Cross` |
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
| `7D` | `3605.20` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 33,130.00 USD | 0.00 USD | 98,140.00 USD |
| `7D` | `3609.40` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3613.20` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 5,770.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `3613.60` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 76,290.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3617.30` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 19,330.00 USD | 0.00 USD | 34,220.00 USD |
| `7D` | `3617.80` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3621.40` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 16,740.00 USD | 0.00 USD | 75,430.00 USD |
| `7D` | `3622.00` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3625.50` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 19,270.00 USD | 0.00 USD | 31,000.00 USD |
| `7D` | `3626.20` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3629.60` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 28,970.00 USD | 0.00 USD | 46,190.00 USD |
| `7D` | `3630.40` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3633.70` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 32,440.00 USD | 0.00 USD | 23,370.00 USD |
| `7D` | `3634.60` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3637.80` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 11,970.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `3638.80` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3641.90` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 17,040.00 USD | 0.00 USD | 5,050.00 USD |
| `7D` | `3643.00` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3646.00` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 2,430.00 USD | 0.00 USD | 3,080.00 USD |
| `7D` | `3647.20` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3650.10` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 7,240.00 USD | 0.00 USD | 11,750.00 USD |
| `1D` | `3654.20` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 1,960.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3846.90` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 8,040.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `3848.80` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3851.00` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 21,210.00 USD | 0.00 USD | 60,020.00 USD |
| `7D` | `3853.00` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3855.10` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 11,440.00 USD | 0.00 USD | 76,000.00 USD |
| `7D` | `3857.20` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3859.20` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 74,590.00 USD | 0.00 USD | 95,930.00 USD |
| `7D` | `3861.40` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3863.30` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 90,380.00 USD | 0.00 USD | 213,930.00 USD |
| `7D` | `3865.60` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3867.40` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `3869.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3871.50` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 82,830.00 USD | 0.00 USD | 144,120.00 USD |
| `7D` | `3874.00` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3875.60` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 82,740.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `3878.20` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3879.70` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 39,690.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `3882.40` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3883.80` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 33,040.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3886.60` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.90` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 19,020.00 USD | 0.00 USD | 14,240.00 USD |
| `7D` | `3890.80` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3892.00` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 17,230.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `3895.00` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3896.10` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 10,980.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `7D` | `3928.60` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3928.90` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3933.00` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3937.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3937.10` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 54,630.00 USD | 0.00 USD | 195,810.00 USD |
| `1D` | `3941.20` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 182,730.00 USD | 0.00 USD | 247,810.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3945.30` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 155,600.00 USD | 0.00 USD | 381,000.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3949.40` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 92,210.00 USD | 0.00 USD | 117,240.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3953.50` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 174,760.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3957.60` | 608,630.00 USD | 0.00 USD | 608,630.00 USD | 156,230.00 USD | 0.00 USD | 98,400.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3961.70` | 354,010.00 USD | 0.00 USD | 354,010.00 USD | 50,390.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3965.80` | 289,910.00 USD | 0.00 USD | 289,910.00 USD | 90,460.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3969.90` | 171,640.00 USD | 0.00 USD | 171,640.00 USD | 13,670.00 USD | 0.00 USD | 15,390.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3974.00` | 142,580.00 USD | 0.00 USD | 142,580.00 USD | 46,630.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3978.10` | 37,170.00 USD | 0.00 USD | 37,170.00 USD | 9,780.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4009.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4011.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4088.80` | 181,740.00 USD | 181,740.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 145,680.00 USD |
| `7D` | `4092.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 216,890.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4092.90` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 95,030.00 USD |
| `7D` | `4096.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4097.00` | 521,170.00 USD | 521,170.00 USD | 0.00 USD | 48,410.00 USD | 0.00 USD | 165,220.00 USD |
| `7D` | `4100.80` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4101.10` | 858,060.00 USD | 858,060.00 USD | 0.00 USD | 136,680.00 USD | 0.00 USD | 200,210.00 USD |
| `7D` | `4105.00` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 455,740.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4105.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 185,790.00 USD | 0.00 USD | 403,540.00 USD |
| `7D` | `4109.20` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 350,460.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4109.30` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 94,290.00 USD | 0.00 USD | 163,130.00 USD |
| `1D` | `4113.40` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 156,520.00 USD | 0.00 USD | 267,450.00 USD |
| `7D` | `4113.40` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4117.50` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 135,340.00 USD | 0.00 USD | 126,800.00 USD |
| `7D` | `4117.60` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4121.60` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 109,530.00 USD | 0.00 USD | 23,580.00 USD |
| `7D` | `4121.80` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4125.70` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 49,110.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `4126.00` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4129.80` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 55,010.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `4130.20` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4133.90` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 4,560.00 USD | 0.00 USD | 41,560.00 USD |
| `7D` | `4134.40` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4138.00` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 42,080.00 USD | 0.00 USD | 50,440.00 USD |
| `7D` | `4138.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4142.10` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 9,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4142.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `1D` | `4166.70` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 8,040.00 USD | 0.00 USD | 24,730.00 USD |
| `7D` | `4168.00` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4170.80` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 18,330.00 USD | 0.00 USD | 55,590.00 USD |
| `7D` | `4172.20` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4174.90` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 10,670.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `4176.40` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4179.00` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | 102,000.00 USD |
| `7D` | `4180.60` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4183.10` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 79,860.00 USD | 0.00 USD | 150,940.00 USD |
| `7D` | `4184.80` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4187.20` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 88,240.00 USD | 0.00 USD | 165,490.00 USD |
| `7D` | `4189.00` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4191.30` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 34,140.00 USD | 0.00 USD | 52,500.00 USD |
| `7D` | `4193.20` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4195.40` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 69,730.00 USD | 0.00 USD | 138,720.00 USD |
| `7D` | `4197.40` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4199.50` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 81,580.00 USD | 0.00 USD | 57,290.00 USD |
| `7D` | `4201.60` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4203.60` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 35,070.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `4205.80` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4207.70` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `4210.00` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4211.80` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 13,900.00 USD | 0.00 USD | 14,240.00 USD |
| `7D` | `4214.20` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4215.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4220.00` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 17,220.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4408.60` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `4411.60` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4412.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `4415.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4416.80` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 13,680.00 USD |
| `7D` | `4420.00` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4420.90` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 15,460.00 USD | 0.00 USD | 21,900.00 USD |
| `7D` | `4424.20` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4425.00` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 15,620.00 USD | 0.00 USD | 57,770.00 USD |
| `1D` | `4425.50` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 1,940.00 USD | 0.00 USD | 7,480.00 USD |
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
  * Total Open Interest: `795.21M` | Total OI Tokens: `198,260.6 XAUT`
  * 1h OI Change: `-3.68%` | 4h OI Change: `-5.85%` | 24h OI Change: `-0.38%`
  * Exchange Breakdown: Binance=`61.49M` | Bybit=`142.43M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `51.95%` | `48.05%` | `1.08` | 5,700,000.00 USD |
| `15M` | `Binance` | `26.81%` | `73.19%` | `0.37` | 732,090.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `49.8%` | `50.2%` | `0.99` | 178,820.00 USD |
| `15M` | `KuCoin` | `5.72%` | `94.28%` | `0.06` | 8,420.00 USD |
| `15M` | `Gate` | `43%` | `57%` | `0.75` | 141,680.00 USD |
| `15M` | `Bitget` | `39.61%` | `60.39%` | `0.66` | 195,130.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `58.67%` | `41.33%` | `1.42` | 4,110,000.00 USD |
| `15M` | `Bitunix` | `38.58%` | `61.42%` | `0.63` | 88,540.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.97%` | `50.03%` | `1.00` | 166,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 67,510.00 USD |
| `15M` | `HTX` | `90.93%` | `9.07%` | `10.03` | 3,980.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `72.69%` | `27.31%` | `2.66` | 2,740.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `26.81%` | `73.19%` | `0.37` | 732,090.00 USD |
| `15M` | `Global Accounts` | `51.95%` | `48.05%` | `1.08` | 5,700,000.00 USD |
| `1H` | `XAUT` | `53.97%` | `46.03%` | `1.17` | 19,290,000.00 USD |
| `1H` | `Binance` | `51.73%` | `48.27%` | `1.07` | 7,700,000.00 USD |
| `1H` | `OKX` | `60.15%` | `39.85%` | `1.51` | 2,710,000.00 USD |
| `1H` | `Bybit` | `57.76%` | `42.24%` | `1.37` | 2,220,000.00 USD |
| `1H` | `KuCoin` | `52.64%` | `47.36%` | `1.11` | 169,070.00 USD |
| `1H` | `Gate` | `42.57%` | `57.43%` | `0.74` | 1,030,000.00 USD |
| `1H` | `Bitget` | `52.36%` | `47.64%` | `1.10` | 457,030.00 USD |
| `1H` | `BingX` | `35.54%` | `64.46%` | `0.55` | 832,020.00 USD |
| `1H` | `MEXC` | `50.72%` | `49.28%` | `1.03` | 1,290,000.00 USD |
| `1H` | `Bitunix` | `51.11%` | `48.89%` | `1.05` | 359,500.00 USD |
| `1H` | `Hyperliquid` | `62.74%` | `37.26%` | `1.68` | 1,050,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 846,520.00 USD |
| `1H` | `Crypto.com` | `39.08%` | `60.92%` | `0.64` | 9,520.00 USD |
| `1H` | `WhiteBIT` | `95.8%` | `4.2%` | `22.81` | 465,550.00 USD |
| `1H` | `HTX` | `45.38%` | `54.62%` | `0.83` | 3,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `56.85%` | `43.15%` | `1.32` | 28,040.00 USD |
| `1H` | `Aster` | `79.63%` | `20.37%` | `3.91` | 56,510.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `35.53%` | `64.47%` | `0.55` | 76,370.00 USD |
| `1H` | `Whale Positions` | `51.73%` | `48.27%` | `1.07` | 7,700,000.00 USD |
| `1H` | `Global Accounts` | `53.97%` | `46.03%` | `1.17` | 19,290,000.00 USD |
| `4H` | `XAUT` | `45.20%` | `54.80%` | `0.82` | 64,100,000.00 USD |
| `4H` | `Binance` | `50.57%` | `49.43%` | `1.02` | 7,280,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.32%` | `46.68%` | `1.14` | 5,740,000.00 USD |
| `4H` | `KuCoin` | `25.28%` | `74.72%` | `0.34` | 317,290.00 USD |
| `4H` | `Gate` | `48.49%` | `51.51%` | `0.94` | 2,860,000.00 USD |
| `4H` | `Bitget` | `53.21%` | `46.79%` | `1.14` | 2,180,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `41.39%` | `58.61%` | `0.71` | 36,330,000.00 USD |
| `4H` | `Bitunix` | `44.84%` | `55.16%` | `0.81` | 3,460,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.47%` | `41.53%` | `1.41` | 4,800,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `15.34%` | `84.66%` | `0.18` | 1,010,000.00 USD |
| `4H` | `HTX` | `50.97%` | `49.03%` | `1.04` | 16,990.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.61%` | `56.39%` | `0.77` | 94,420.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `50.57%` | `49.43%` | `1.02` | 7,280,000.00 USD |
| `4H` | `Global Accounts` | `45.20%` | `54.80%` | `0.82` | 64,100,000.00 USD |


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
| `5m` | -22,970.00 USD | -117,960.00 USD | **`DISTRIBUTION`** |
| `15m` | -59,710.00 USD | -388,270.00 USD | **`DISTRIBUTION`** |
| `30m` | 74,320.00 USD | -379,570.00 USD | **`DISTRIBUTION`** |
| `1h` | -74,710.00 USD | -457,180.00 USD | **`DISTRIBUTION`** |
| `2h` | -436,800.00 USD | -229,190.00 USD | **`DISTRIBUTION`** |
| `4h` | -29,520.00 USD | 401,030.00 USD | **`ACCUMULATION`** |
| `6h` | -523,780.00 USD | 890,810.00 USD | **`ACCUMULATION`** |
| `8h` | -592,590.00 USD | 1,070,000.00 USD | **`ACCUMULATION`** |
| `12h` | -271,600.00 USD | 765,330.00 USD | **`ACCUMULATION`** |
| `24h` | -451,030.00 USD | 895,810.00 USD | **`ACCUMULATION`** |
| `1w` | -79,790,000.00 USD | -20,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,840,000.00 USD | -83,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-22.97K` | 15m=`-59.71K` | 1h=`-74.71K` | 24h=`-451.03K`
* Futures Capital Netflows: 5m=`-117.96K` | 15m=`-388.27K` | 1h=`-457.18K` | 24h=`+895.81K`
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
  * Execution Entry: `26625.86` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26542.47` (Risk Distance: `83.39` pts)
  * +2.5R Take Profit: `26834.33`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26786.10` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26869.49` (Risk Distance: `83.39` pts)
  * +2.5R Take Profit: `26577.63`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26919.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
