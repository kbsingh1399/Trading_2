# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:29:21 IST` (`2026-10-30 05:59:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26606.89` | **Live Ask Quote**: `26608.89` | **Mid Price**: `26607.89`
- **Spread Points**: `200.00` | **Spread BPS**: `0.75 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26607.89` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.52` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26794.15` | Lower -3.00σ Band: `26421.63`
  * Upper +2.51σ Band: `26754.23` | Lower -2.51σ Band: `26461.55`
  * Upper +2.01σ Band: `26719.64` | Lower -2.01σ Band: `26496.14`
  * Upper +2.00σ Band: `26714.32` | Lower -2.00σ Band: `26501.46`
  * Upper +1.28σ Band: `26682.39` | Lower -1.28σ Band: `26533.39`
  * Upper +1.00σ Band: `26661.11` | Lower -1.00σ Band: `26554.67`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26607.89` | EMA-20=`26607.89` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26607.89` (Slope: `+0.0000`) | EMA-100=`26607.89`
  * Institutional Anchors: EMA-144=`26607.89` | EMA-200=`26607.89` (Slope: `+0.0000`) | EMA-233=`26607.89`
- **Range Boundaries**: 24H High=`26873.97` | 24H Low=`26341.81` | Weekly High=`27140.05` | Weekly Low=`26075.73`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26687.71` (Distance: `+0.00%`)
  * Point of Control (POC) = `26607.89` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26528.07` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26714.32` | POC=`26607.89` | VAL=`26501.46`
  * Prior Day Extremes: PDH=`26767.54` | PDL=`26448.24` | PDC=`26607.89`
  * Monday Range Blueprint: High=`26740.93` | Mid=`26607.89` | Low=`26474.85`
  * Developing Weekly Value Area: Weekly VAH=`26820.75` | Weekly POC=`26607.89` | Weekly VAL=`26395.03`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26661.11` | Low=`26554.67`
  * London Session (08:00-16:00 UTC): High=`26714.32` | Low=`26501.46`
  * New York Session (13:00-21:00 UTC): High=`26767.54` | Low=`26448.24`
  * Initial Balance (First Hour): IB High=`26687.71` | IB Low=`26528.07`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26501.46` - `26714.32`
  * Optimal Trade Entry (OTE 0.705): `26661.11`
  * Structural Invalidation Anchor (0.786): `26820.75`

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
| `1216` | `0xead5...69f2` | `LONG` | 1,813,955.76 USD | `453.78` | `4220.88` | `3997.00` | `3539.20` | -101,412.30 USD | `-5.59%` | `5X Isolated` |
| `1308` | `0x46fc...1195` | `LONG` | 1,658,537.39 USD | `414.87` | `4053.27` | `3997.00` | `2165.62` | -23,055.46 USD | `-1.39%` | `20X Cross` |
| `1345` | `0x6d15...d374` | `LONG` | 1,598,960.00 USD | `400.00` | `4068.25` | `3997.00` | `3842.07` | -28,340.00 USD | `-1.77%` | `25X Cross` |
| `1346` | `0xee02...309d` | `SHORT` | 1,598,920.00 USD | `400.00` | `4438.84` | `3997.00` | `4227.14` | 176,618.60 USD | `+11.05%` | `25X Isolated` |
| `1394` | `0x02a7...fe9f` | `SHORT` | 1,558,947.00 USD | `390.00` | `4055.02` | `3997.00` | `4306.96` | 22,512.25 USD | `+1.44%` | `25X Cross` |
| `1429` | `0x7e77...b8d2` | `SHORT` | 1,519,012.00 USD | `380.00` | `4131.92` | `3997.00` | `4293.77` | 51,117.64 USD | `+3.37%` | `20X Cross` |
| `1451` | `0x72c2...9b37` | `LONG` | 1,492,264.01 USD | `373.13` | `4000.98` | `3997.00` | `3778.31` | -629.51 USD | `-0.04%` | `13X Isolated` |
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
| `7D` | `3589.40` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.10` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `3593.70` | 22,380,000.00 USD | 0.00 USD | 22,380,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3595.30` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 24,410.00 USD | 0.00 USD | 19,250.00 USD |
| `7D` | `3598.00` | 22,130,000.00 USD | 0.00 USD | 22,130,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3599.50` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 6,610.00 USD | 0.00 USD | 34,940.00 USD |
| `7D` | `3602.30` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3603.70` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 13,320.00 USD | 0.00 USD | 33,720.00 USD |
| `7D` | `3606.60` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3607.90` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 18,250.00 USD | 0.00 USD | 64,400.00 USD |
| `7D` | `3610.90` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.10` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 17,620.00 USD | 0.00 USD | 26,900.00 USD |
| `7D` | `3615.20` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.30` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.50` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.50` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 21,740.00 USD | 0.00 USD | 66,750.00 USD |
| `7D` | `3623.80` | 21,070,000.00 USD | 0.00 USD | 21,070,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3624.70` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 19,820.00 USD | 0.00 USD | 35,010.00 USD |
| `7D` | `3628.10` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 47,240.00 USD | 0.00 USD | 35,770.00 USD |
| `1D` | `3628.90` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,400.00 USD | 0.00 USD | 21,120.00 USD |
| `7D` | `3632.40` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3633.10` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 2,840.00 USD |
| `7D` | `3636.70` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.00` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,500,000.00 USD | 0.00 USD | 20,500,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,500,000.00 USD | 0.00 USD | 20,500,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `7D` | `3830.20` | 20,400,000.00 USD | 0.00 USD | 20,400,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3830.50` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `3834.50` | 19,940,000.00 USD | 0.00 USD | 19,940,000.00 USD | 284,980.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3834.70` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 87,400.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `3838.80` | 19,090,000.00 USD | 0.00 USD | 19,090,000.00 USD | 321,610.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3838.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 22,350.00 USD | 0.00 USD | 119,800.00 USD |
| `1D` | `3843.10` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 46,080.00 USD | 0.00 USD | 97,130.00 USD |
| `7D` | `3843.10` | 17,980,000.00 USD | 0.00 USD | 17,980,000.00 USD | 301,340.00 USD | 0.00 USD | 359,480.00 USD |
| `1D` | `3847.30` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 66,000.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `3847.40` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 115,590.00 USD | 0.00 USD | 366,480.00 USD |
| `1D` | `3851.50` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 73,320.00 USD | 0.00 USD | 129,680.00 USD |
| `7D` | `3851.70` | 16,830,000.00 USD | 0.00 USD | 16,830,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3855.70` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 27,220.00 USD | 0.00 USD | 99,710.00 USD |
| `7D` | `3856.00` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3859.90` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 68,340.00 USD | 0.00 USD | 112,500.00 USD |
| `7D` | `3860.30` | 16,120,000.00 USD | 0.00 USD | 16,120,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3864.10` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 97,240.00 USD | 0.00 USD | 215,080.00 USD |
| `7D` | `3864.60` | 15,800,000.00 USD | 0.00 USD | 15,800,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3868.30` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 32,990.00 USD | 0.00 USD | 59,180.00 USD |
| `7D` | `3868.90` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 192,180.00 USD | 0.00 USD | 163,110.00 USD |
| `1D` | `3872.50` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 6,710.00 USD | 0.00 USD | 69,480.00 USD |
| `7D` | `3873.20` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `7D` | `3877.50` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `7D` | `3881.80` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `1D` | `3910.30` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `3911.90` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3914.50` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 174,800.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `3916.20` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 711,980.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3918.70` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 44,700.00 USD | 0.00 USD | 186,400.00 USD |
| `7D` | `3920.50` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 701,320.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3922.90` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 92,170.00 USD | 0.00 USD | 247,470.00 USD |
| `7D` | `3924.80` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 288,490.00 USD | 0.00 USD | 470,810.00 USD |
| `1D` | `3927.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 114,120.00 USD | 0.00 USD | 380,740.00 USD |
| `7D` | `3929.10` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 184,740.00 USD | 0.00 USD | 836,390.00 USD |
| `1D` | `3931.30` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 162,220.00 USD | 0.00 USD | 249,590.00 USD |
| `7D` | `3933.40` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3935.50` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 22,890.00 USD | 0.00 USD | 208,370.00 USD |
| `7D` | `3937.70` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3939.70` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 149,180.00 USD | 0.00 USD | 198,540.00 USD |
| `7D` | `3942.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3943.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 180,760.00 USD | 0.00 USD | 412,900.00 USD |
| `7D` | `3946.30` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.10` | 425,910.00 USD | 0.00 USD | 425,910.00 USD | 101,020.00 USD | 0.00 USD | 172,500.00 USD |
| `7D` | `3950.60` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 333,580.00 USD | 0.00 USD | 326,980.00 USD |
| `1D` | `3952.30` | 152,380.00 USD | 0.00 USD | 152,380.00 USD | 13,410.00 USD | 0.00 USD | 138,970.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `3990.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3991.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `1D` | `4069.90` | 59,730.00 USD | 59,730.00 USD | 0.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4074.10` | 310,720.00 USD | 310,720.00 USD | 0.00 USD | 166,380.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,700.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4078.30` | 541,240.00 USD | 541,240.00 USD | 0.00 USD | 53,120.00 USD | 0.00 USD | 177,410.00 USD |
| `7D` | `4079.60` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 677,570.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4082.50` | 853,210.00 USD | 853,210.00 USD | 0.00 USD | 82,490.00 USD | 0.00 USD | 229,470.00 USD |
| `7D` | `4083.90` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 409,280.00 USD | 0.00 USD | 674,150.00 USD |
| `1D` | `4086.70` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 108,840.00 USD | 0.00 USD | 328,940.00 USD |
| `7D` | `4088.20` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 821,070.00 USD |
| `1D` | `4090.90` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 158,790.00 USD | 0.00 USD | 259,780.00 USD |
| `7D` | `4092.50` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4095.10` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 33,980.00 USD | 0.00 USD | 176,600.00 USD |
| `7D` | `4096.80` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4099.30` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 113,960.00 USD | 0.00 USD | 197,190.00 USD |
| `7D` | `4101.10` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4103.50` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 172,480.00 USD | 0.00 USD | 409,020.00 USD |
| `7D` | `4105.40` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4107.70` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 124,320.00 USD | 0.00 USD | 211,990.00 USD |
| `7D` | `4109.70` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 222,470.00 USD |
| `1D` | `4111.90` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 36,140.00 USD | 0.00 USD | 110,430.00 USD |
| `7D` | `4114.00` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4116.10` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 94,650.00 USD |
| `7D` | `4118.30` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `7D` | `4122.60` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `4152.70` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.90` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 83,190.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `4157.00` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 318,580.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4158.10` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 26,560.00 USD | 0.00 USD | 88,700.00 USD |
| `7D` | `4161.30` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 344,810.00 USD | 0.00 USD | 513,530.00 USD |
| `1D` | `4162.30` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 41,250.00 USD | 0.00 USD | 93,520.00 USD |
| `7D` | `4165.60` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4166.50` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 40,500.00 USD | 0.00 USD | 133,830.00 USD |
| `7D` | `4169.90` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 251,660.00 USD |
| `1D` | `4170.70` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 83,520.00 USD | 0.00 USD | 164,850.00 USD |
| `7D` | `4174.20` | 17,640,000.00 USD | 17,640,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4174.90` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 26,780.00 USD | 0.00 USD | 95,550.00 USD |
| `7D` | `4178.50` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4179.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | 104,490.00 USD |
| `7D` | `4182.80` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4183.30` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 162,760.00 USD |
| `7D` | `4187.10` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4187.50` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 78,780.00 USD | 0.00 USD | 142,490.00 USD |
| `7D` | `4191.40` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 155,040.00 USD |
| `1D` | `4191.70` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 18,070.00 USD | 0.00 USD | 47,820.00 USD |
| `7D` | `4195.70` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4195.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | 63,720.00 USD |
| `7D` | `4200.00` | 19,570,000.00 USD | 19,570,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `7D` | `4204.30` | 19,790,000.00 USD | 19,790,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,160,000.00 USD | 20,160,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `4389.10` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4389.20` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4393.30` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 9,110.00 USD |
| `7D` | `4393.50` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4397.50` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 7,610.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4397.80` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4401.70` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 16,500.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4402.10` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `1D` | `4405.90` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 6,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4406.40` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `1D` | `4410.10` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 13,560.00 USD | 0.00 USD | 58,710.00 USD |
| `7D` | `4410.70` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `1D` | `4413.90` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 17,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4415.00` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,600,000.00 USD | 21,600,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4427.90` | 21,860,000.00 USD | 21,860,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.20` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 35,220.00 USD | 0.00 USD | 33,300.00 USD |
| `7D` | `4435.80` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 19,260.00 USD | 0.00 USD | 37,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `792.71M` | Total OI Tokens: `198,333.2 XAUT`
  * 1h OI Change: `-1.48%` | 4h OI Change: `-2.04%` | 24h OI Change: `-7.92%`
  * Exchange Breakdown: Binance=`61.16M` | Bybit=`144.62M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `39.63%` | `60.37%` | `0.66` | 1,970,000.00 USD |
| `15M` | `Binance` | `31.97%` | `68.03%` | `0.47` | 321,880.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `47.4%` | `52.6%` | `0.90` | 167,310.00 USD |
| `15M` | `KuCoin` | `8.32%` | `91.68%` | `0.09` | 15,000.00 USD |
| `15M` | `Gate` | `65.05%` | `34.95%` | `1.86` | 72,420.00 USD |
| `15M` | `Bitget` | `42.88%` | `57.12%` | `0.75` | 121,630.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `28.36%` | `71.64%` | `0.40` | 813,130.00 USD |
| `15M` | `Bitunix` | `85.45%` | `14.55%` | `5.87` | 157,740.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.97%` | `41.03%` | `1.44` | 219,220.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.8%` | `99.2%` | `0.01` | 72,630.00 USD |
| `15M` | `HTX` | `3.78%` | `96.22%` | `0.04` | 2,430.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `31.97%` | `68.03%` | `0.47` | 321,880.00 USD |
| `15M` | `Global Accounts` | `39.63%` | `60.37%` | `0.66` | 1,970,000.00 USD |
| `1H` | `XAUT` | `49.47%` | `50.53%` | `0.98` | 11,700,000.00 USD |
| `1H` | `Binance` | `39.35%` | `60.65%` | `0.65` | 1,750,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `58.4%` | `41.6%` | `1.40` | 842,080.00 USD |
| `1H` | `KuCoin` | `40.02%` | `59.98%` | `0.67` | 51,230.00 USD |
| `1H` | `Gate` | `50.14%` | `49.86%` | `1.01` | 539,300.00 USD |
| `1H` | `Bitget` | `41.16%` | `58.84%` | `0.70` | 726,410.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `51.91%` | `48.09%` | `1.08` | 6,190,000.00 USD |
| `1H` | `Bitunix` | `71.56%` | `28.44%` | `2.52` | 419,660.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `57.36%` | `42.64%` | `1.35` | 832,240.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `7.77%` | `92.23%` | `0.08` | 342,220.00 USD |
| `1H` | `HTX` | `12.03%` | `87.97%` | `0.14` | 8,390.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `39.35%` | `60.65%` | `0.65` | 1,750,000.00 USD |
| `1H` | `Global Accounts` | `49.47%` | `50.53%` | `0.98` | 11,700,000.00 USD |
| `4H` | `XAUT` | `46.00%` | `54.00%` | `0.85` | 23,240,000.00 USD |
| `4H` | `Binance` | `50.96%` | `49.04%` | `1.04` | 7,980,000.00 USD |
| `4H` | `OKX` | `51.29%` | `48.71%` | `1.05` | 2,280,000.00 USD |
| `4H` | `Bybit` | `52.39%` | `47.61%` | `1.10` | 2,730,000.00 USD |
| `4H` | `KuCoin` | `50.46%` | `49.54%` | `1.02` | 1,010,000.00 USD |
| `4H` | `Gate` | `51.51%` | `48.49%` | `1.06` | 361,680.00 USD |
| `4H` | `Bitget` | `51.19%` | `48.81%` | `1.05` | 388,050.00 USD |
| `4H` | `BingX` | `12.04%` | `87.96%` | `0.14` | 2,860,000.00 USD |
| `4H` | `MEXC` | `47.13%` | `52.87%` | `0.89` | 828,380.00 USD |
| `4H` | `Bitunix` | `54.26%` | `45.74%` | `1.19` | 282,460.00 USD |
| `4H` | `Hyperliquid` | `64.83%` | `35.17%` | `1.84` | 149,980.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.26%` | `51.74%` | `0.93` | 4,110,000.00 USD |
| `4H` | `Crypto.com` | `0.56%` | `99.44%` | `0.01` | 709.29 USD |
| `4H` | `WhiteBIT` | `74.1%` | `25.9%` | `2.86` | 163,720.00 USD |
| `4H` | `HTX` | `53.53%` | `46.47%` | `1.15` | 8,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `3.45%` | `96.55%` | `0.04` | 29,520.00 USD |
| `4H` | `Aster` | `91.81%` | `8.19%` | `11.21` | 510.40 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.66%` | `35.34%` | `1.83` | 50,560.00 USD |
| `4H` | `Whale Positions` | `50.96%` | `49.04%` | `1.04` | 7,980,000.00 USD |
| `4H` | `Global Accounts` | `46.00%` | `54.00%` | `0.85` | 23,240,000.00 USD |


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
| `5m` | -25,550.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -103,130.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -29,650.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -180,820.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -245,950.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -865,040.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,330,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,860,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,270,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -186,900.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -71,870,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,170,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-25.55K` | 15m=`-103.13K` | 1h=`-180.82K` | 24h=`-186.90K`
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
  * Execution Entry: `26528.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26445.24` (Risk Distance: `82.82` pts)
  * +2.5R Take Profit: `26735.13`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26687.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26770.54` (Risk Distance: `82.82` pts)
  * +2.5R Take Profit: `26480.65`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26820.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
