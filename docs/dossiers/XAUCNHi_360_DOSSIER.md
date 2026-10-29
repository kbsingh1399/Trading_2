# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:48:52 IST` (`2026-10-29 21:18:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26768.71` | **Live Ask Quote**: `26772.08` | **Mid Price**: `26770.40`
- **Spread Points**: `337.00` | **Spread BPS**: `1.26 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26770.40` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.93` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26957.79` | Lower -3.00σ Band: `26583.00`
  * Upper +2.51σ Band: `26917.63` | Lower -2.51σ Band: `26623.16`
  * Upper +2.01σ Band: `26882.83` | Lower -2.01σ Band: `26657.96`
  * Upper +2.00σ Band: `26877.48` | Lower -2.00σ Band: `26663.31`
  * Upper +1.28σ Band: `26845.35` | Lower -1.28σ Band: `26695.44`
  * Upper +1.00σ Band: `26823.94` | Lower -1.00σ Band: `26716.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26770.40` | EMA-20=`26770.40` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26770.40` (Slope: `+0.0000`) | EMA-100=`26770.40`
  * Institutional Anchors: EMA-144=`26770.40` | EMA-200=`26770.40` (Slope: `+0.0000`) | EMA-233=`26770.40`
- **Range Boundaries**: 24H High=`27038.10` | 24H Low=`26502.69` | Weekly High=`27305.80` | Weekly Low=`26234.99`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26850.71` (Distance: `+0.00%`)
  * Point of Control (POC) = `26770.40` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26690.08` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26877.48` | POC=`26770.40` | VAL=`26663.31`
  * Prior Day Extremes: PDH=`26931.02` | PDL=`26609.77` | PDC=`26770.40`
  * Monday Range Blueprint: High=`26904.25` | Mid=`26770.40` | Low=`26636.54`
  * Developing Weekly Value Area: Weekly VAH=`26984.56` | Weekly POC=`26770.40` | Weekly VAL=`26556.23`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26823.94` | Low=`26716.85`
  * London Session (08:00-16:00 UTC): High=`26877.48` | Low=`26663.31`
  * New York Session (13:00-21:00 UTC): High=`26931.02` | Low=`26609.77`
  * Initial Balance (First Hour): IB High=`26850.71` | IB Low=`26690.08`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26663.31` - `26877.48`
  * Optimal Trade Entry (OTE 0.705): `26823.94`
  * Structural Invalidation Anchor (0.786): `26984.56`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x4692...164f` | `SHORT` | 25,397,227.60 USD | `6,316.62` | `4133.30` | `4020.70` | `13715.26` | 711,312.60 USD | `+2.80%` | `5X Cross` |
| `53` | `0x5b5d...c060` | `SHORT` | 25,218,867.74 USD | `6,272.26` | `4191.43` | `4020.70` | `32771.82` | 1,070,917.77 USD | `+4.25%` | `4X Cross` |
| `69` | `0xb83d...6e36` | `SHORT` | 22,980,291.96 USD | `5,717.06` | `4234.49` | `4020.70` | `30770.12` | 1,228,583.26 USD | `+5.35%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,409,791.28 USD | `4,828.91` | `4157.43` | `4020.70` | `2229.40` | -666,091.03 USD | `-3.43%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,160,322.40 USD | `3,521.86` | `4129.47` | `4020.70` | `387.19` | -383,084.98 USD | `-2.71%` | `3X Cross` |
| `155` | `0x7a6d...f79c` | `SHORT` | 13,140,504.81 USD | `3,268.21` | `4228.94` | `4020.70` | `4395.90` | 680,574.32 USD | `+5.18%` | `25X Cross` |
| `172` | `0xa742...e390` | `SHORT` | 11,660,030.40 USD | `2,900.00` | `4364.92` | `4020.70` | `4235.67` | 998,245.93 USD | `+8.56%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,843,120.00 USD | `2,200.00` | `4176.09` | `4020.70` | `2594.00` | -344,299.30 USD | `-3.89%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,843,120.00 USD | `2,200.00` | `4112.20` | `4020.70` | `4331.15` | 203,734.59 USD | `+2.30%` | `20X Cross` |
| `299` | `0xfc66...ca06` | `SHORT` | 7,963,715.48 USD | `1,981.17` | `4032.86` | `4020.70` | `24596.44` | 26,090.74 USD | `+0.33%` | `3X Cross` |
| `302` | `0xacb6...efbd` | `SHORT` | 7,939,996.10 USD | `1,975.37` | `4048.55` | `4020.70` | `6503.97` | 57,395.62 USD | `+0.72%` | `6X Cross` |
| `369` | `0xc26c...b8f4` | `LONG` | 6,350,774.26 USD | `1,579.95` | `4075.62` | `4020.70` | `0.000000` | -88,522.71 USD | `-1.39%` | `1X Cross` |
| `397` | `0x12d2...f97f` | `LONG` | 5,635,109.08 USD | `1,401.94` | `4278.91` | `4020.70` | `3007.52` | -363,681.49 USD | `-6.45%` | `20X Cross` |
| `552` | `0x63da...8add` | `LONG` | 4,019,600.00 USD | `1,000.00` | `4021.46` | `4020.70` | `3564.11` | -1,860.96 USD | `-0.05%` | `25X Cross` |
| `561` | `0x354b...6425` | `LONG` | 3,971,389.33 USD | `987.74` | `4031.85` | `4020.70` | `0.000000` | -11,018.01 USD | `-0.28%` | `10X Cross` |
| `578` | `0x9aa5...58af` | `LONG` | 3,905,515.02 USD | `971.64` | `4279.98` | `4020.70` | `0.000000` | -253,094.07 USD | `-6.48%` | `20X Cross` |
| `605` | `0xf3dc...1672` | `LONG` | 3,741,124.30 USD | `930.74` | `4024.62` | `4020.70` | `3337.59` | -4,768.26 USD | `-0.13%` | `20X Cross` |
| `671` | `0x4a20...3c26` | `LONG` | 3,366,932.97 USD | `837.40` | `4599.73` | `4020.70` | `0.000000` | -484,887.41 USD | `-14.40%` | `20X Cross` |
| `835` | `0x0fac...7a0a` | `LONG` | 2,760,150.24 USD | `686.49` | `4290.34` | `4020.70` | `1367.89` | -185,108.46 USD | `-6.71%` | `25X Cross` |
| `876` | `0xd8c5...99b0` | `SHORT` | 2,582,009.76 USD | `642.35` | `4175.35` | `4020.70` | `32802.83` | 100,051.42 USD | `+3.87%` | `4X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,492,152.00 USD | `620.00` | `4122.81` | `4020.70` | `4342.25` | 63,995.03 USD | `+2.57%` | `20X Cross` |
| `935` | `0xeae3...e8ad` | `SHORT` | 2,411,820.00 USD | `600.00` | `4104.77` | `4020.70` | `4325.27` | 51,045.11 USD | `+2.12%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,404,146.48 USD | `598.11` | `4146.45` | `4020.70` | `3891.24` | -75,873.08 USD | `-3.16%` | `25X Cross` |
| `960` | `0x12f7...8750` | `LONG` | 2,353,920.77 USD | `585.61` | `4082.77` | `4020.70` | `2472.32` | -36,996.21 USD | `-1.57%` | `10X Cross` |
| `1103` | `0x413c...886c` | `LONG` | 2,009,750.00 USD | `500.00` | `4010.43` | `4020.70` | `0.000000` | 4,533.77 USD | `+0.23%` | `2X Cross` |
| `1116` | `0x61ce...a62b` | `SHORT` | 1,999,814.82 USD | `497.50` | `4071.66` | `4020.70` | `4708.15` | 25,853.97 USD | `+1.29%` | `20X Cross` |
| `1121` | `0x0593...40f9` | `LONG` | 1,994,482.69 USD | `496.18` | `4024.57` | `4020.70` | `3701.73` | -2,421.14 USD | `-0.12%` | `10X Isolated` |
| `1246` | `0xead5...69f2` | `LONG` | 1,824,029.76 USD | `453.78` | `4220.88` | `4020.70` | `3538.94` | -91,338.29 USD | `-5.01%` | `5X Isolated` |
| `1353` | `0x46fc...1195` | `LONG` | 1,654,462.29 USD | `411.59` | `4055.10` | `4020.70` | `2084.58` | -14,572.06 USD | `-0.88%` | `20X Cross` |
| `1392` | `0xee02...309d` | `SHORT` | 1,608,280.00 USD | `400.00` | `4438.84` | `4020.70` | `4226.89` | 167,258.60 USD | `+10.40%` | `25X Isolated` |
| `1393` | `0x6d15...d374` | `LONG` | 1,607,840.00 USD | `400.00` | `4068.25` | `4020.70` | `3841.81` | -19,460.00 USD | `-1.21%` | `25X Cross` |
| `1437` | `0x02a7...fe9f` | `SHORT` | 1,567,644.00 USD | `390.00` | `4055.02` | `4020.70` | `4306.71` | 13,815.25 USD | `+0.88%` | `25X Cross` |
| `1467` | `0x7e77...b8d2` | `SHORT` | 1,527,866.00 USD | `380.00` | `4131.92` | `4020.70` | `4293.51` | 42,263.64 USD | `+2.77%` | `20X Cross` |
| `1487` | `0x72c2...9b37` | `LONG` | 1,499,801.26 USD | `373.13` | `4000.98` | `4020.70` | `3778.04` | 6,907.74 USD | `+0.46%` | `13X Isolated` |
| `1528` | `0xaa44...b844` | `LONG` | 1,447,020.00 USD | `360.00` | `4043.10` | `4020.70` | `2803.26` | -8,497.63 USD | `-0.59%` | `4X Cross` |
| `1636` | `0xa41f...d50a` | `LONG` | 1,322,263.16 USD | `328.96` | `4468.89` | `4020.70` | `3833.19` | -147,834.69 USD | `-11.18%` | `15X Cross` |
| `1658` | `0x49e9...e1d0` | `SHORT` | 1,300,612.82 USD | `323.48` | `4025.23` | `4020.70` | `31031.91` | 1,465.51 USD | `+0.11%` | `4X Cross` |
| `1674` | `0xada6...6f88` | `LONG` | 1,283,711.40 USD | `319.28` | `4166.46` | `4020.70` | `1957.73` | -46,539.11 USD | `-3.63%` | `5X Cross` |
| `1680` | `0xbf5a...88ba` | `SHORT` | 1,276,813.87 USD | `317.65` | `4091.80` | `4020.70` | `9965.67` | 22,969.16 USD | `+1.80%` | `20X Cross` |
| `1715` | `0xff31...ff6c` | `SHORT` | 1,246,076.00 USD | `310.00` | `4372.43` | `4020.70` | `4789.18` | 109,379.38 USD | `+8.78%` | `10X Isolated` |
| `1877` | `0x50e2...d770` | `LONG` | 1,086,768.80 USD | `270.37` | `4243.58` | `4020.70` | `2562.10` | -60,557.66 USD | `-5.57%` | `20X Cross` |
| `1899` | `0x4c92...4f17` | `SHORT` | 1,072,109.72 USD | `266.72` | `4260.98` | `4020.70` | `6519.38` | 64,382.51 USD | `+6.01%` | `20X Cross` |
| `1967` | `0xd346...c4f3` | `LONG` | 1,025,696.61 USD | `255.17` | `4188.66` | `4020.70` | `3310.42` | -43,139.90 USD | `-4.21%` | `5X Isolated` |
| `2001` | `0x1581...463b` | `LONG` | 1,004,925.00 USD | `250.00` | `4003.77` | `4020.70` | `3542.13` | 3,981.41 USD | `+0.40%` | `15X Cross` |

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
| `7D` | `3605.10` | 21,650,000.00 USD | 0.00 USD | 21,650,000.00 USD | 33,130.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `3609.30` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3609.80` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3613.50` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 76,290.00 USD | 0.00 USD | 59,640.00 USD |
| `1D` | `3614.00` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3617.70` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 38,860.00 USD | 0.00 USD | 93,380.00 USD |
| `1D` | `3618.20` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 7,370.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3621.90` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 72,670.00 USD | 0.00 USD | 127,200.00 USD |
| `1D` | `3622.40` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `7D` | `3626.10` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3626.60` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `3630.30` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.80` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3634.50` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.00` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3638.70` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.20` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.40` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3647.10` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3647.60` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 1,030.00 USD | 0.00 USD | 12,640.00 USD |
| `7D` | `3651.30` | 20,490,000.00 USD | 0.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3651.80` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.50` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.00` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 1,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3659.70` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 20,290,000.00 USD | 0.00 USD | 20,290,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 19,780,000.00 USD | 0.00 USD | 19,780,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 18,930,000.00 USD | 0.00 USD | 18,930,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 156,600.00 USD | 0.00 USD | 170,790.00 USD |
| `7D` | `3848.70` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 65,850.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3849.20` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3852.90` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 164,660.00 USD | 0.00 USD | 106,350.00 USD |
| `1D` | `3853.40` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `3857.10` | 17,020,000.00 USD | 0.00 USD | 17,020,000.00 USD | 216,800.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3857.60` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 27,380.00 USD | 0.00 USD | 74,240.00 USD |
| `7D` | `3861.30` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 191,980.00 USD | 0.00 USD | 480,010.00 USD |
| `1D` | `3861.80` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 60,240.00 USD | 0.00 USD | 187,340.00 USD |
| `7D` | `3865.50` | 15,890,000.00 USD | 0.00 USD | 15,890,000.00 USD | 174,320.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3866.00` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 78,760.00 USD | 0.00 USD | 134,060.00 USD |
| `7D` | `3869.70` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3870.20` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `7D` | `3873.90` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3874.40` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `7D` | `3878.10` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3878.60` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `7D` | `3882.30` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3882.80` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3886.50` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.00` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `3890.70` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.20` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 4,840.00 USD | 0.00 USD | 39,210.00 USD |
| `7D` | `3894.90` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3895.40` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.10` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3899.60` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 6,110.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `3903.30` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.50` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 10,700,000.00 USD | 0.00 USD | 10,700,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 334,680.00 USD | 0.00 USD | 367,820.00 USD |
| `7D` | `3928.50` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3929.00` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.70` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3933.20` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3936.90` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3937.40` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 54,760.00 USD | 0.00 USD | 140,290.00 USD |
| `7D` | `3941.10` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 291,240.00 USD | 0.00 USD | 726,850.00 USD |
| `1D` | `3941.60` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 95,210.00 USD | 0.00 USD | 291,500.00 USD |
| `7D` | `3945.30` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 420,350.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3945.80` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.00` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3954.20` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3958.40` | 634,800.00 USD | 0.00 USD | 634,800.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3962.60` | 405,210.00 USD | 0.00 USD | 405,210.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3966.80` | 348,890.00 USD | 0.00 USD | 348,890.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.00` | 211,760.00 USD | 0.00 USD | 211,760.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.20` | 145,370.00 USD | 0.00 USD | 145,370.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.40` | 32,670.00 USD | 0.00 USD | 32,670.00 USD | 29,470.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4016.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4017.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 415,530.00 USD |
| `7D` | `4088.10` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `7D` | `4092.30` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 230,630.00 USD | 0.00 USD | 290,760.00 USD |
| `1D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `4096.50` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4097.00` | 459,370.00 USD | 459,370.00 USD | 0.00 USD | 42,130.00 USD | 0.00 USD | 109,700.00 USD |
| `7D` | `4100.70` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 267,010.00 USD | 0.00 USD | 676,330.00 USD |
| `1D` | `4101.20` | 718,810.00 USD | 718,810.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 200,210.00 USD |
| `7D` | `4104.90` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 515,100.00 USD | 0.00 USD | 733,310.00 USD |
| `1D` | `4105.40` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 181,350.00 USD | 0.00 USD | 406,570.00 USD |
| `7D` | `4109.10` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 298,470.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4109.60` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `7D` | `4113.30` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4113.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `7D` | `4117.50` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `4121.70` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.20` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `4125.90` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4126.40` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4130.10` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4130.60` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4134.30` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4134.80` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.00` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.70` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.20` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 12,230.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `4146.90` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.10` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4167.90` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.40` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `4172.10` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4172.60` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4176.30` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 227,820.00 USD |
| `1D` | `4176.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `7D` | `4180.50` | 17,630,000.00 USD | 17,630,000.00 USD | 0.00 USD | 143,630.00 USD | 0.00 USD | 275,830.00 USD |
| `1D` | `4181.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 23,000.00 USD | 0.00 USD | 81,660.00 USD |
| `7D` | `4184.70` | 18,230,000.00 USD | 18,230,000.00 USD | 0.00 USD | 258,130.00 USD | 0.00 USD | 339,100.00 USD |
| `1D` | `4185.20` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 203,210.00 USD |
| `7D` | `4188.90` | 18,720,000.00 USD | 18,720,000.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4189.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `4193.10` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4193.60` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `7D` | `4197.30` | 19,430,000.00 USD | 19,430,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4197.80` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `4201.50` | 19,630,000.00 USD | 19,630,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4202.00` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `4205.70` | 19,830,000.00 USD | 19,830,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.20` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.90` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4210.40` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4214.10` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4214.60` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4218.30` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4218.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `7D` | `4222.50` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `4226.70` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4377.90` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.30` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4407.80` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4411.50` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4412.00` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `4415.70` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4416.20` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `4419.90` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4420.40` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `7D` | `4424.10` | 21,630,000.00 USD | 21,630,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4424.60` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 53,200.00 USD |
| `7D` | `4428.30` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 46,440.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4428.80` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `7D` | `4432.50` | 21,920,000.00 USD | 21,920,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `4433.00` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4433.70` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4436.70` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 22,080,000.00 USD | 22,080,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `824.83M` | Total OI Tokens: `205,148.8 XAUT`
  * 1h OI Change: `-5.29%` | 4h OI Change: `-1.95%` | 24h OI Change: `-0.46%`
  * Exchange Breakdown: Binance=`61.60M` | Bybit=`143.53M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `54.43%` | `45.57%` | `1.19` | 4,300,000.00 USD |
| `15M` | `Binance` | `51.18%` | `48.82%` | `1.05` | 1,690,000.00 USD |
| `15M` | `OKX` | `56.91%` | `43.09%` | `1.32` | 432,280.00 USD |
| `15M` | `Bybit` | `52.89%` | `47.11%` | `1.12` | 623,120.00 USD |
| `15M` | `KuCoin` | `49.91%` | `50.09%` | `1.00` | 9,960.00 USD |
| `15M` | `Gate` | `76.03%` | `23.97%` | `3.17` | 93,680.00 USD |
| `15M` | `Bitget` | `53.97%` | `46.03%` | `1.17` | 232,700.00 USD |
| `15M` | `BingX` | `72.12%` | `27.88%` | `2.59` | 88,970.00 USD |
| `15M` | `MEXC` | `68.25%` | `31.75%` | `2.15` | 269,780.00 USD |
| `15M` | `Bitunix` | `57.79%` | `42.21%` | `1.37` | 47,740.00 USD |
| `15M` | `Hyperliquid` | `54.83%` | `45.17%` | `1.21` | 70,900.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.81%` | `51.19%` | `0.95` | 670,750.00 USD |
| `15M` | `Crypto.com` | `0.5%` | `99.5%` | `0.01` | 1,220.00 USD |
| `15M` | `WhiteBIT` | `96.31%` | `3.69%` | `26.10` | 44,760.00 USD |
| `15M` | `HTX` | `55.74%` | `44.26%` | `1.26` | 914.51 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `98.91%` | `1.09%` | `90.74` | 5,750.00 USD |
| `15M` | `Aster` | `4.57%` | `95.43%` | `0.05` | 2,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `5.96%` | `94.04%` | `0.06` | 3,450.00 USD |
| `15M` | `Whale Positions` | `51.18%` | `48.82%` | `1.05` | 1,690,000.00 USD |
| `15M` | `Global Accounts` | `54.43%` | `45.57%` | `1.19` | 4,300,000.00 USD |
| `1H` | `XAUT` | `45.45%` | `54.55%` | `0.83` | 35,160,000.00 USD |
| `1H` | `Binance` | `45.38%` | `54.62%` | `0.83` | 13,730,000.00 USD |
| `1H` | `OKX` | `44.83%` | `55.17%` | `0.81` | 4,730,000.00 USD |
| `1H` | `Bybit` | `42.75%` | `57.25%` | `0.75` | 5,920,000.00 USD |
| `1H` | `KuCoin` | `46.66%` | `53.34%` | `0.87` | 411,700.00 USD |
| `1H` | `Gate` | `54.48%` | `45.52%` | `1.20` | 336,950.00 USD |
| `1H` | `Bitget` | `50.88%` | `49.12%` | `1.04` | 2,730,000.00 USD |
| `1H` | `BingX` | `38.2%` | `61.8%` | `0.62` | 725,540.00 USD |
| `1H` | `MEXC` | `45.01%` | `54.99%` | `0.82` | 1,370,000.00 USD |
| `1H` | `Bitunix` | `46.14%` | `53.86%` | `0.86` | 402,450.00 USD |
| `1H` | `Hyperliquid` | `37.13%` | `62.87%` | `0.59` | 609,320.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.9%` | `53.1%` | `0.88` | 3,770,000.00 USD |
| `1H` | `Crypto.com` | `26.84%` | `73.16%` | `0.37` | 19,110.00 USD |
| `1H` | `WhiteBIT` | `73.47%` | `26.53%` | `2.77` | 204,830.00 USD |
| `1H` | `HTX` | `48.7%` | `51.3%` | `0.95` | 45,070.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `58.41%` | `41.59%` | `1.40` | 48,820.00 USD |
| `1H` | `Aster` | `39.63%` | `60.37%` | `0.66` | 42,720.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.43%` | `43.57%` | `1.30` | 59,290.00 USD |
| `1H` | `Whale Positions` | `45.38%` | `54.62%` | `0.83` | 13,730,000.00 USD |
| `1H` | `Global Accounts` | `45.45%` | `54.55%` | `0.83` | 35,160,000.00 USD |
| `4H` | `XAUT` | `42.56%` | `57.44%` | `0.74` | 74,460,000.00 USD |
| `4H` | `Binance` | `43.41%` | `56.59%` | `0.77` | 29,560,000.00 USD |
| `4H` | `OKX` | `48.41%` | `51.59%` | `0.94` | 8,740,000.00 USD |
| `4H` | `Bybit` | `45.72%` | `54.28%` | `0.84` | 11,130,000.00 USD |
| `4H` | `KuCoin` | `48.68%` | `51.32%` | `0.95` | 2,440,000.00 USD |
| `4H` | `Gate` | `50.86%` | `49.14%` | `1.04` | 1,550,000.00 USD |
| `4H` | `Bitget` | `42.76%` | `57.24%` | `0.75` | 2,970,000.00 USD |
| `4H` | `BingX` | `17.37%` | `82.63%` | `0.21` | 6,800,000.00 USD |
| `4H` | `MEXC` | `40.94%` | `59.06%` | `0.69` | 4,370,000.00 USD |
| `4H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 1,170,000.00 USD |
| `4H` | `Hyperliquid` | `44.18%` | `55.82%` | `0.79` | 1,640,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.7%` | `51.3%` | `0.95` | 1,370,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.99%` | `53.01%` | `0.89` | 2,000,000.00 USD |
| `4H` | `HTX` | `55.36%` | `44.64%` | `1.24` | 75,690.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `72.74%` | `27.26%` | `2.67` | 409,650.00 USD |
| `4H` | `Aster` | `53.66%` | `46.34%` | `1.16` | 170,440.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `27.03%` | `72.97%` | `0.37` | 61,310.00 USD |
| `4H` | `Whale Positions` | `43.41%` | `56.59%` | `0.77` | 29,560,000.00 USD |
| `4H` | `Global Accounts` | `42.56%` | `57.44%` | `0.74` | 74,460,000.00 USD |


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
| `5m` | 359,120.00 USD | 7,680.00 USD | **`ACCUMULATION`** |
| `15m` | 531,780.00 USD | 126,460.00 USD | **`ACCUMULATION`** |
| `30m` | 402,560.00 USD | -103,220.00 USD | **`ACCUMULATION`** |
| `1h` | 150,620.00 USD | -366,270.00 USD | **`DISTRIBUTION`** |
| `2h` | 303,090.00 USD | 378,110.00 USD | **`ACCUMULATION`** |
| `4h` | -234,830.00 USD | 892,120.00 USD | **`ACCUMULATION`** |
| `6h` | -232,530.00 USD | 763,910.00 USD | **`ACCUMULATION`** |
| `8h` | -614,910.00 USD | 631,100.00 USD | **`ACCUMULATION`** |
| `12h` | 1,070,000.00 USD | 881,460.00 USD | **`ACCUMULATION`** |
| `24h` | -57,540.00 USD | 398,750.00 USD | **`ACCUMULATION`** |
| `1w` | -79,300,000.00 USD | -20,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,130,000.00 USD | -84,620,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+359.12K` | 15m=`+531.78K` | 1h=`+150.62K` | 24h=`-57.54K`
* Futures Capital Netflows: 5m=`+7.68K` | 15m=`+126.46K` | 1h=`-366.27K` | 24h=`+398.75K`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26690.08` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26604.72` (Risk Distance: `85.37` pts)
  * +2.5R Take Profit: `26903.50`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26850.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26936.07` (Risk Distance: `85.37` pts)
  * +2.5R Take Profit: `26637.29`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26984.56`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
