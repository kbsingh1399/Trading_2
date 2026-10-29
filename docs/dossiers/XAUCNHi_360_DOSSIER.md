# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 04:07:44 IST` (`2026-10-29 22:37:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26767.58` | **Live Ask Quote**: `26769.85` | **Mid Price**: `26768.72`
- **Spread Points**: `227.00` | **Spread BPS**: `0.85 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26768.72` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.92` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26956.10` | Lower -3.00σ Band: `26581.33`
  * Upper +2.51σ Band: `26915.94` | Lower -2.51σ Band: `26621.49`
  * Upper +2.01σ Band: `26881.14` | Lower -2.01σ Band: `26656.29`
  * Upper +2.00σ Band: `26875.79` | Lower -2.00σ Band: `26661.64`
  * Upper +1.28σ Band: `26843.67` | Lower -1.28σ Band: `26693.76`
  * Upper +1.00σ Band: `26822.25` | Lower -1.00σ Band: `26715.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26768.72` | EMA-20=`26768.72` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26768.72` (Slope: `+0.0000`) | EMA-100=`26768.72`
  * Institutional Anchors: EMA-144=`26768.72` | EMA-200=`26768.72` (Slope: `+0.0000`) | EMA-233=`26768.72`
- **Range Boundaries**: 24H High=`27036.40` | 24H Low=`26501.03` | Weekly High=`27304.09` | Weekly Low=`26233.34`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26849.02` (Distance: `+0.00%`)
  * Point of Control (POC) = `26768.72` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26688.41` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26875.79` | POC=`26768.72` | VAL=`26661.64`
  * Prior Day Extremes: PDH=`26929.33` | PDL=`26608.10` | PDC=`26768.72`
  * Monday Range Blueprint: High=`26902.56` | Mid=`26768.72` | Low=`26634.87`
  * Developing Weekly Value Area: Weekly VAH=`26982.86` | Weekly POC=`26768.72` | Weekly VAL=`26554.57`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26822.25` | Low=`26715.18`
  * London Session (08:00-16:00 UTC): High=`26875.79` | Low=`26661.64`
  * New York Session (13:00-21:00 UTC): High=`26929.33` | Low=`26608.10`
  * Initial Balance (First Hour): IB High=`26849.02` | IB Low=`26688.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26661.64` - `26875.79`
  * Optimal Trade Entry (OTE 0.705): `26822.25`
  * Structural Invalidation Anchor (0.786): `26982.86`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:05:52 IST` |

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
| `1234` | `0xead5...69f2` | `LONG` | 1,824,528.93 USD | `453.78` | `4220.88` | `4020.70` | `3538.94` | -90,839.13 USD | `-4.98%` | `5X Isolated` |
| `1348` | `0x46fc...1195` | `LONG` | 1,651,188.97 USD | `410.66` | `4055.10` | `4020.70` | `2142.76` | -14,087.53 USD | `-0.85%` | `20X Cross` |
| `1380` | `0x6d15...d374` | `LONG` | 1,608,280.00 USD | `400.00` | `4068.25` | `4020.70` | `3841.81` | -19,020.00 USD | `-1.18%` | `25X Cross` |
| `1381` | `0xee02...309d` | `SHORT` | 1,608,200.00 USD | `400.00` | `4438.84` | `4020.70` | `4226.89` | 167,338.60 USD | `+10.41%` | `25X Isolated` |
| `1416` | `0x02a7...fe9f` | `SHORT` | 1,568,034.00 USD | `390.00` | `4055.02` | `4020.70` | `4306.71` | 13,425.25 USD | `+0.86%` | `25X Cross` |
| `1452` | `0x7e77...b8d2` | `SHORT` | 1,527,828.00 USD | `380.00` | `4131.92` | `4020.70` | `4293.51` | 42,301.64 USD | `+2.77%` | `20X Cross` |
| `1469` | `0x72c2...9b37` | `LONG` | 1,500,249.02 USD | `373.13` | `4000.98` | `4020.70` | `3778.05` | 7,355.50 USD | `+0.49%` | `13X Isolated` |
| `1519` | `0xaa44...b844` | `LONG` | 1,447,344.00 USD | `360.00` | `4043.10` | `4020.70` | `2803.27` | -8,173.63 USD | `-0.56%` | `4X Cross` |
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
| `7D` | `3613.60` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 76,290.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3614.30` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 5,270.00 USD | 0.00 USD | 25,900.00 USD |
| `7D` | `3617.80` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.40` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 17,630.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.50` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 23,830.00 USD | 0.00 USD | 68,370.00 USD |
| `7D` | `3626.20` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3626.60` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 13,180.00 USD | 0.00 USD | 17,830.00 USD |
| `7D` | `3630.40` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.70` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 28,270.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3634.60` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3634.80` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 35,340.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3638.80` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3638.90` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.00` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 17,700.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3643.00` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3647.10` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 2,430.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `3647.20` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3651.20` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 7,240.00 USD | 0.00 USD | 13,210.00 USD |
| `1D` | `3655.30` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3655.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.00` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `3848.80` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.10` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 15,390.00 USD | 0.00 USD | 56,320.00 USD |
| `7D` | `3853.00` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.20` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 24,210.00 USD | 0.00 USD | 73,650.00 USD |
| `7D` | `3857.20` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.30` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 81,130.00 USD | 0.00 USD | 103,900.00 USD |
| `7D` | `3861.40` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 84,570.00 USD | 0.00 USD | 219,310.00 USD |
| `7D` | `3865.60` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.50` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 43,350.00 USD | 0.00 USD | 59,260.00 USD |
| `7D` | `3869.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3872.60` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 76,790.00 USD | 0.00 USD | 141,780.00 USD |
| `7D` | `3874.00` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3876.70` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 91,460.00 USD | 0.00 USD | 57,290.00 USD |
| `7D` | `3878.20` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3880.80` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 25,200.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `3882.40` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3884.90` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 45,230.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `3886.60` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.00` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 8,460.00 USD | 0.00 USD | 12,020.00 USD |
| `7D` | `3890.80` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.10` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 23,320.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `3895.00` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.20` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3925.90` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.00` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 49,890.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `3932.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.10` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 24,210.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3937.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.20` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 82,040.00 USD | 0.00 USD | 199,890.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.30` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 181,230.00 USD | 0.00 USD | 404,740.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.40` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 148,140.00 USD | 0.00 USD | 219,880.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.50` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 85,520.00 USD | 0.00 USD | 148,290.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3954.60` | 995,470.00 USD | 0.00 USD | 995,470.00 USD | 146,690.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3958.70` | 552,880.00 USD | 0.00 USD | 552,880.00 USD | 161,750.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3962.80` | 347,020.00 USD | 0.00 USD | 347,020.00 USD | 40,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3966.90` | 299,220.00 USD | 0.00 USD | 299,220.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.00` | 162,090.00 USD | 0.00 USD | 162,090.00 USD | 13,670.00 USD | 0.00 USD | 25,940.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.10` | 122,480.00 USD | 0.00 USD | 122,480.00 USD | 46,630.00 USD | 0.00 USD | 38,680.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.20` | 37,170.00 USD | 0.00 USD | 37,170.00 USD | 9,780.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4015.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4015.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `1D` | `4085.80` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4089.90` | 196,680.00 USD | 196,680.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 216,890.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.00` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.10` | 575,530.00 USD | 575,530.00 USD | 0.00 USD | 83,300.00 USD | 0.00 USD | 177,880.00 USD |
| `7D` | `4100.80` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.20` | 990,740.00 USD | 990,740.00 USD | 0.00 USD | 146,290.00 USD | 0.00 USD | 268,920.00 USD |
| `7D` | `4105.00` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 455,740.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.30` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 150,220.00 USD | 0.00 USD | 347,480.00 USD |
| `7D` | `4109.20` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 350,460.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.40` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 92,210.00 USD | 0.00 USD | 111,120.00 USD |
| `7D` | `4113.40` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 148,080.00 USD | 0.00 USD | 269,000.00 USD |
| `7D` | `4117.60` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.60` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 163,150.00 USD | 0.00 USD | 124,080.00 USD |
| `7D` | `4121.80` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.70` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4126.00` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4126.80` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4130.20` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4130.90` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 31,060.00 USD | 0.00 USD | 37,130.00 USD |
| `7D` | `4134.40` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.00` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.10` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `1D` | `4167.80` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 8,040.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4168.00` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4171.90` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 21,210.00 USD | 0.00 USD | 60,020.00 USD |
| `7D` | `4172.20` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4176.00` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 49,010.00 USD |
| `7D` | `4176.40` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.10` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 68,300.00 USD | 0.00 USD | 100,580.00 USD |
| `7D` | `4180.60` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.20` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 74,810.00 USD | 0.00 USD | 192,300.00 USD |
| `7D` | `4184.80` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.30` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 62,590.00 USD | 0.00 USD | 88,140.00 USD |
| `7D` | `4189.00` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.40` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 42,760.00 USD | 0.00 USD | 71,970.00 USD |
| `7D` | `4193.20` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.50` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 73,350.00 USD | 0.00 USD | 136,440.00 USD |
| `7D` | `4197.40` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4200.60` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4201.60` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4204.70` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 23,730.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4208.80` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 45,230.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4212.90` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 8,460.00 USD | 0.00 USD | 9,730.00 USD |
| `7D` | `4214.20` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.00` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 17,230.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.10` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 10,980.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.70` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4413.80` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4415.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4417.90` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 17,310.00 USD |
| `7D` | `4420.00` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.00` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 13,320.00 USD | 0.00 USD | 28,980.00 USD |
| `7D` | `4424.20` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4426.10` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 16,740.00 USD | 0.00 USD | 61,140.00 USD |
| `7D` | `4428.40` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4429.00` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 15,330.00 USD | 0.00 USD | 20,440.00 USD |
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
  * Total Open Interest: `824.94M` | Total OI Tokens: `205,419.8 XAUT`
  * 1h OI Change: `+0.19%` | 4h OI Change: `-2.32%` | 24h OI Change: `+2.23%`
  * Exchange Breakdown: Binance=`61.60M` | Bybit=`142.73M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `50.76%` | `49.24%` | `1.03` | 2,150,000.00 USD |
| `15M` | `Binance` | `56.77%` | `43.23%` | `1.31` | 770,740.00 USD |
| `15M` | `OKX` | `49%` | `51%` | `0.96` | 199,610.00 USD |
| `15M` | `Bybit` | `52.69%` | `47.31%` | `1.11` | 228,760.00 USD |
| `15M` | `KuCoin` | `38.93%` | `61.07%` | `0.64` | 11,120.00 USD |
| `15M` | `Gate` | `58.15%` | `41.85%` | `1.39` | 30,340.00 USD |
| `15M` | `Bitget` | `41.39%` | `58.61%` | `0.71` | 56,130.00 USD |
| `15M` | `BingX` | `49.66%` | `50.34%` | `0.99` | 70,560.00 USD |
| `15M` | `MEXC` | `65.61%` | `34.39%` | `1.91` | 170,750.00 USD |
| `15M` | `Bitunix` | `51.84%` | `48.16%` | `1.08` | 17,400.00 USD |
| `15M` | `Hyperliquid` | `48.33%` | `51.67%` | `0.94` | 37,330.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.65%` | `55.35%` | `0.81` | 362,670.00 USD |
| `15M` | `Crypto.com` | `19.35%` | `80.65%` | `0.24` | 2.17 USD |
| `15M` | `WhiteBIT` | `27.16%` | `72.84%` | `0.37` | 189,320.00 USD |
| `15M` | `HTX` | `67.45%` | `32.55%` | `2.07` | 158.80 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 18.75 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 20.56 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.55%` | `50.45%` | `0.98` | 2,780.00 USD |
| `15M` | `Whale Positions` | `56.77%` | `43.23%` | `1.31` | 770,740.00 USD |
| `15M` | `Global Accounts` | `50.76%` | `49.24%` | `1.03` | 2,150,000.00 USD |
| `1H` | `XAUT` | `50.58%` | `49.42%` | `1.02` | 35,330,000.00 USD |
| `1H` | `Binance` | `47.24%` | `52.76%` | `0.90` | 13,020,000.00 USD |
| `1H` | `OKX` | `58.2%` | `41.8%` | `1.39` | 5,280,000.00 USD |
| `1H` | `Bybit` | `48.6%` | `51.4%` | `0.95` | 7,220,000.00 USD |
| `1H` | `KuCoin` | `51.82%` | `48.18%` | `1.08` | 175,360.00 USD |
| `1H` | `Gate` | `50.68%` | `49.32%` | `1.03` | 1,220,000.00 USD |
| `1H` | `Bitget` | `46.93%` | `53.07%` | `0.88` | 1,060,000.00 USD |
| `1H` | `BingX` | `48.84%` | `51.16%` | `0.95` | 690,590.00 USD |
| `1H` | `MEXC` | `42.99%` | `57.01%` | `0.75` | 1,900,000.00 USD |
| `1H` | `Bitunix` | `52.01%` | `47.99%` | `1.08` | 696,310.00 USD |
| `1H` | `Hyperliquid` | `57.94%` | `42.06%` | `1.38` | 2,060,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.19%` | `46.81%` | `1.14` | 1,170,000.00 USD |
| `1H` | `Crypto.com` | `58.06%` | `41.94%` | `1.38` | 13,810.00 USD |
| `1H` | `WhiteBIT` | `88.62%` | `11.38%` | `7.79` | 515,820.00 USD |
| `1H` | `HTX` | `47.62%` | `52.38%` | `0.91` | 4,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.16%` | `50.84%` | `0.97` | 95,820.00 USD |
| `1H` | `Aster` | `48.82%` | `51.18%` | `0.95` | 74,720.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.26%` | `63.74%` | `0.57` | 142,370.00 USD |
| `1H` | `Whale Positions` | `47.24%` | `52.76%` | `0.90` | 13,020,000.00 USD |
| `1H` | `Global Accounts` | `50.58%` | `49.42%` | `1.02` | 35,330,000.00 USD |
| `4H` | `XAUT` | `44.41%` | `55.59%` | `0.80` | 81,520,000.00 USD |
| `4H` | `Binance` | `45.54%` | `54.46%` | `0.84` | 34,260,000.00 USD |
| `4H` | `OKX` | `49.52%` | `50.48%` | `0.98` | 9,320,000.00 USD |
| `4H` | `Bybit` | `47.77%` | `52.23%` | `0.91` | 11,890,000.00 USD |
| `4H` | `KuCoin` | `48.93%` | `51.07%` | `0.96` | 2,500,000.00 USD |
| `4H` | `Gate` | `50.7%` | `49.3%` | `1.03` | 1,780,000.00 USD |
| `4H` | `Bitget` | `47.05%` | `52.95%` | `0.89` | 3,320,000.00 USD |
| `4H` | `BingX` | `19.41%` | `80.59%` | `0.24` | 6,460,000.00 USD |
| `4H` | `MEXC` | `42.62%` | `57.38%` | `0.74` | 4,390,000.00 USD |
| `4H` | `Bitunix` | `41.61%` | `58.39%` | `0.71` | 1,540,000.00 USD |
| `4H` | `Hyperliquid` | `45.91%` | `54.09%` | `0.85` | 1,830,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.76%` | `51.24%` | `0.95` | 1,320,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.14%` | `53.86%` | `0.86` | 2,280,000.00 USD |
| `4H` | `HTX` | `54.16%` | `45.84%` | `1.18` | 75,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.64%` | `45.36%` | `1.20` | 241,540.00 USD |
| `4H` | `Aster` | `56.16%` | `43.84%` | `1.28` | 217,180.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `20.23%` | `79.77%` | `0.25` | 80,570.00 USD |
| `4H` | `Whale Positions` | `45.54%` | `54.46%` | `0.84` | 34,260,000.00 USD |
| `4H` | `Global Accounts` | `44.41%` | `55.59%` | `0.80` | 81,520,000.00 USD |


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
| `5m` | 14,790.00 USD | -3,680.00 USD | **`ACCUMULATION`** |
| `15m` | 67,790.00 USD | -66,060.00 USD | **`ACCUMULATION`** |
| `30m` | 116,110.00 USD | -170,290.00 USD | **`DISTRIBUTION`** |
| `1h` | -212,550.00 USD | 219,850.00 USD | **`ACCUMULATION`** |
| `2h` | -327,270.00 USD | 48,720.00 USD | **`DISTRIBUTION`** |
| `4h` | -60,130.00 USD | 915,440.00 USD | **`ACCUMULATION`** |
| `6h` | -565,080.00 USD | 1,250,000.00 USD | **`ACCUMULATION`** |
| `8h` | -585,310.00 USD | 1,630,000.00 USD | **`ACCUMULATION`** |
| `12h` | 247,080.00 USD | 1,120,000.00 USD | **`ACCUMULATION`** |
| `24h` | -343,990.00 USD | 1,340,000.00 USD | **`ACCUMULATION`** |
| `1w` | -79,860,000.00 USD | -19,900,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,660,000.00 USD | -83,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+14.79K` | 15m=`+67.79K` | 1h=`-212.55K` | 24h=`-343.99K`
* Futures Capital Netflows: 5m=`-3.68K` | 15m=`-66.06K` | 1h=`+219.85K` | 24h=`+1.34M`
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
  * Execution Entry: `26688.41` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26604.70` (Risk Distance: `83.71` pts)
  * +2.5R Take Profit: `26897.69`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26849.02` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26932.73` (Risk Distance: `83.71` pts)
  * +2.5R Take Profit: `26639.74`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26982.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
