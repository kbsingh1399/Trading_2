# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:00:21 IST` (`2026-10-29 20:30:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26794.56` | **Live Ask Quote**: `26796.09` | **Mid Price**: `26795.33`
- **Spread Points**: `153.00` | **Spread BPS**: `0.57 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26795.33` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.99` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26982.89` | Lower -3.00σ Band: `26607.76`
  * Upper +2.51σ Band: `26942.70` | Lower -2.51σ Band: `26647.95`
  * Upper +2.01σ Band: `26907.87` | Lower -2.01σ Band: `26682.78`
  * Upper +2.00σ Band: `26902.51` | Lower -2.00σ Band: `26688.14`
  * Upper +1.28σ Band: `26870.35` | Lower -1.28σ Band: `26720.30`
  * Upper +1.00σ Band: `26848.92` | Lower -1.00σ Band: `26741.73`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26795.33` | EMA-20=`26795.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26795.33` (Slope: `+0.0000`) | EMA-100=`26795.33`
  * Institutional Anchors: EMA-144=`26795.33` | EMA-200=`26795.33` (Slope: `+0.0000`) | EMA-233=`26795.33`
- **Range Boundaries**: 24H High=`27063.28` | 24H Low=`26527.37` | Weekly High=`27331.23` | Weekly Low=`26259.42`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26875.71` (Distance: `+0.00%`)
  * Point of Control (POC) = `26795.33` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26714.94` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26902.51` | POC=`26795.33` | VAL=`26688.14`
  * Prior Day Extremes: PDH=`26956.10` | PDL=`26634.55` | PDC=`26795.33`
  * Monday Range Blueprint: High=`26929.30` | Mid=`26795.33` | Low=`26661.35`
  * Developing Weekly Value Area: Weekly VAH=`27009.69` | Weekly POC=`26795.33` | Weekly VAL=`26580.96`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26848.92` | Low=`26741.73`
  * London Session (08:00-16:00 UTC): High=`26902.51` | Low=`26688.14`
  * New York Session (13:00-21:00 UTC): High=`26956.10` | Low=`26634.55`
  * Initial Balance (First Hour): IB High=`26875.71` | IB Low=`26714.94`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26688.14` - `26902.51`
  * Optimal Trade Entry (OTE 0.705): `26848.92`
  * Structural Invalidation Anchor (0.786): `27009.69`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,559,225.15 USD | `6,346.33` | `4191.43` | `4027.20` | `30400.24` | 1,041,044.96 USD | `+4.07%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,453,925.42 USD | `6,320.35` | `4133.69` | `4027.20` | `13546.81` | 672,426.95 USD | `+2.64%` | `5X Cross` |
| `70` | `0xb83d...6e36` | `SHORT` | 23,023,741.62 USD | `5,717.06` | `4234.49` | `4027.20` | `28620.80` | 1,185,133.61 USD | `+5.15%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,447,939.65 USD | `4,828.91` | `4157.43` | `4027.20` | `2129.96` | -627,942.67 USD | `-3.23%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,178,340.01 USD | `3,520.56` | `4129.51` | `4027.20` | `336.34` | -359,849.35 USD | `-2.54%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,162,728.66 USD | `3,268.21` | `4228.94` | `4027.20` | `4388.93` | 658,350.47 USD | `+5.00%` | `25X Cross` |
| `175` | `0xa742...e390` | `SHORT` | 11,679,750.40 USD | `2,900.00` | `4364.92` | `4027.20` | `4235.64` | 978,525.93 USD | `+8.38%` | `20X Cross` |
| `274` | `0x3678...b209` | `LONG` | 8,860,060.00 USD | `2,200.00` | `4176.09` | `4027.20` | `2558.32` | -327,359.30 USD | `-3.69%` | `25X Cross` |
| `275` | `0x41e5...0825` | `SHORT` | 8,859,840.00 USD | `2,200.00` | `4112.20` | `4027.20` | `4331.13` | 187,014.59 USD | `+2.11%` | `20X Cross` |
| `310` | `0xfc66...ca06` | `SHORT` | 7,997,180.77 USD | `1,985.74` | `4032.86` | `4027.20` | `24321.76` | 11,059.29 USD | `+0.14%` | `3X Cross` |
| `312` | `0xacb6...efbd` | `SHORT` | 7,955,403.98 USD | `1,975.37` | `4048.55` | `4027.20` | `6484.38` | 41,987.74 USD | `+0.53%` | `6X Cross` |
| `380` | `0xc26c...b8f4` | `LONG` | 6,363,255.87 USD | `1,579.95` | `4075.62` | `4027.20` | `0.000000` | -76,041.10 USD | `-1.20%` | `1X Cross` |
| `413` | `0x12d2...f97f` | `LONG` | 5,646,184.43 USD | `1,401.94` | `4278.91` | `4027.20` | `2653.76` | -352,606.15 USD | `-6.25%` | `20X Cross` |
| `572` | `0x63da...8add` | `LONG` | 4,027,300.00 USD | `1,000.00` | `4021.46` | `4027.20` | `3564.08` | 5,839.04 USD | `+0.14%` | `25X Cross` |
| `591` | `0x9aa5...58af` | `LONG` | 3,913,093.83 USD | `971.64` | `4279.98` | `4027.20` | `0.000000` | -245,515.26 USD | `-6.27%` | `20X Cross` |
| `619` | `0xf3dc...1672` | `LONG` | 3,748,570.25 USD | `930.74` | `4024.62` | `4027.20` | `3337.56` | 2,677.69 USD | `+0.07%` | `20X Cross` |
| `676` | `0x4a20...3c26` | `LONG` | 3,372,627.29 USD | `837.40` | `4599.73` | `4027.20` | `0.000000` | -479,193.09 USD | `-14.21%` | `20X Cross` |
| `679` | `0x354b...6425` | `LONG` | 3,352,124.77 USD | `832.35` | `4033.48` | `4027.20` | `0.000000` | -5,147.45 USD | `-0.15%` | `10X Cross` |
| `834` | `0x0fac...7a0a` | `LONG` | 2,764,612.39 USD | `686.49` | `4290.34` | `4027.20` | `1387.90` | -180,646.31 USD | `-6.53%` | `25X Cross` |
| `875` | `0xd8c5...99b0` | `SHORT` | 2,587,020.12 USD | `642.35` | `4175.35` | `4027.20` | `32749.66` | 95,041.05 USD | `+3.67%` | `4X Cross` |
| `910` | `0x625e...a354` | `SHORT` | 2,496,864.00 USD | `620.00` | `4122.81` | `4027.20` | `4342.23` | 59,283.03 USD | `+2.37%` | `20X Cross` |
| `930` | `0xeae3...e8ad` | `SHORT` | 2,416,500.00 USD | `600.00` | `4104.77` | `4027.20` | `4325.25` | 46,365.11 USD | `+1.92%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,408,811.70 USD | `598.11` | `4146.45` | `4027.20` | `3891.22` | -71,207.85 USD | `-2.96%` | `25X Cross` |
| `951` | `0x12f7...8750` | `LONG` | 2,358,488.53 USD | `585.61` | `4082.77` | `4027.20` | `2293.04` | -32,428.45 USD | `-1.37%` | `10X Cross` |
| `1110` | `0x413c...886c` | `LONG` | 2,013,750.00 USD | `500.00` | `4010.43` | `4027.20` | `0.000000` | 8,533.77 USD | `+0.42%` | `2X Cross` |
| `1120` | `0x61ce...a62b` | `SHORT` | 2,003,695.35 USD | `497.50` | `4071.66` | `4027.20` | `4698.37` | 21,973.44 USD | `+1.10%` | `20X Cross` |
| `1128` | `0x0593...40f9` | `LONG` | 1,998,303.25 USD | `496.18` | `4024.57` | `4027.20` | `3701.71` | 1,399.42 USD | `+0.07%` | `10X Isolated` |
| `1249` | `0xead5...69f2` | `LONG` | 1,827,478.52 USD | `453.78` | `4220.88` | `4027.20` | `3538.92` | -87,889.54 USD | `-4.81%` | `5X Isolated` |
| `1363` | `0x46fc...1195` | `LONG` | 1,653,844.98 USD | `410.66` | `4055.28` | `4027.20` | `2036.03` | -11,490.59 USD | `-0.69%` | `20X Cross` |
| `1399` | `0xee02...309d` | `SHORT` | 1,611,000.00 USD | `400.00` | `4438.84` | `4027.20` | `4226.86` | 164,538.60 USD | `+10.21%` | `25X Isolated` |
| `1400` | `0x6d15...d374` | `LONG` | 1,610,880.00 USD | `400.00` | `4068.25` | `4027.20` | `3841.79` | -16,420.00 USD | `-1.02%` | `25X Cross` |
| `1441` | `0x02a7...fe9f` | `SHORT` | 1,570,647.00 USD | `390.00` | `4055.02` | `4027.20` | `4306.68` | 10,812.25 USD | `+0.69%` | `25X Cross` |
| `1474` | `0x7e77...b8d2` | `SHORT` | 1,530,412.00 USD | `380.00` | `4131.92` | `4027.20` | `4293.49` | 39,717.64 USD | `+2.60%` | `20X Cross` |
| `1497` | `0x72c2...9b37` | `LONG` | 1,502,786.31 USD | `373.13` | `4000.98` | `4027.20` | `3778.02` | 9,892.80 USD | `+0.66%` | `13X Isolated` |
| `1536` | `0xaa44...b844` | `LONG` | 1,449,900.00 USD | `360.00` | `4043.10` | `4027.20` | `2803.24` | -5,617.63 USD | `-0.39%` | `4X Cross` |
| `1645` | `0xa41f...d50a` | `LONG` | 1,324,861.96 USD | `328.96` | `4468.89` | `4027.20` | `3833.16` | -145,235.89 USD | `-10.96%` | `15X Cross` |
| `1671` | `0x49e9...e1d0` | `SHORT` | 1,302,715.43 USD | `323.48` | `4025.23` | `4027.20` | `31381.78` | -637.11 USD | `-0.05%` | `4X Cross` |
| `1688` | `0xada6...6f88` | `LONG` | 1,285,850.55 USD | `319.28` | `4166.46` | `4027.20` | `1922.13` | -44,399.96 USD | `-3.45%` | `5X Cross` |
| `1697` | `0xbf5a...88ba` | `SHORT` | 1,279,323.34 USD | `317.65` | `4091.80` | `4027.20` | `10429.38` | 20,459.69 USD | `+1.60%` | `20X Cross` |
| `1734` | `0xff31...ff6c` | `SHORT` | 1,248,494.00 USD | `310.00` | `4372.43` | `4027.20` | `4789.15` | 106,961.38 USD | `+8.57%` | `10X Isolated` |
| `1891` | `0x50e2...d770` | `LONG` | 1,088,850.63 USD | `270.37` | `4243.58` | `4027.20` | `2562.07` | -58,475.83 USD | `-5.37%` | `20X Cross` |
| `1909` | `0x4c92...4f17` | `SHORT` | 1,074,190.14 USD | `266.72` | `4260.98` | `4027.20` | `6504.67` | 62,302.09 USD | `+5.80%` | `20X Cross` |
| `1974` | `0xd346...c4f3` | `LONG` | 1,027,712.48 USD | `255.17` | `4188.66` | `4027.20` | `3310.40` | -41,124.03 USD | `-4.00%` | `5X Isolated` |
| `2008` | `0xe47f...758c` | `LONG` | 1,006,875.00 USD | `250.00` | `4020.00` | `4027.20` | `3774.32` | 1,875.00 USD | `+0.19%` | `20X Cross` |
| `2009` | `0x1581...463b` | `LONG` | 1,006,850.00 USD | `250.00` | `4003.77` | `4027.20` | `3504.62` | 5,906.41 USD | `+0.59%` | `15X Cross` |

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
| `7D` | `3605.10` | 21,780,000.00 USD | 0.00 USD | 21,780,000.00 USD | 33,130.00 USD | 0.00 USD | 112,650.00 USD |
| `1D` | `3605.60` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 4,050.00 USD |
| `7D` | `3609.30` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3609.80` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3613.50` | 21,580,000.00 USD | 0.00 USD | 21,580,000.00 USD | 76,290.00 USD | 0.00 USD | 59,640.00 USD |
| `1D` | `3614.00` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3617.70` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 38,860.00 USD | 0.00 USD | 93,380.00 USD |
| `1D` | `3618.20` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 7,370.00 USD | 0.00 USD | 22,030.00 USD |
| `7D` | `3621.90` | 21,320,000.00 USD | 0.00 USD | 21,320,000.00 USD | 79,860.00 USD | 0.00 USD | 127,200.00 USD |
| `1D` | `3622.40` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `7D` | `3626.10` | 21,110,000.00 USD | 0.00 USD | 21,110,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3626.60` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `3630.30` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.80` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3634.50` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.00` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3638.70` | 20,750,000.00 USD | 0.00 USD | 20,750,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.20` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.40` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3647.10` | 20,640,000.00 USD | 0.00 USD | 20,640,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3647.60` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 5,060.00 USD | 0.00 USD | 12,640.00 USD |
| `7D` | `3651.30` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3651.80` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.50` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.00` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 6,030.00 USD | 0.00 USD | 14,250.00 USD |
| `7D` | `3659.70` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 20,410,000.00 USD | 0.00 USD | 20,410,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 19,900,000.00 USD | 0.00 USD | 19,900,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,110,000.00 USD | 0.00 USD | 18,110,000.00 USD | 156,600.00 USD | 0.00 USD | 170,790.00 USD |
| `7D` | `3848.70` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 65,850.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3849.20` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3852.90` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 164,660.00 USD | 0.00 USD | 106,350.00 USD |
| `1D` | `3853.40` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `3857.10` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 216,800.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3857.60` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 23,940.00 USD | 0.00 USD | 74,240.00 USD |
| `7D` | `3861.30` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 191,980.00 USD | 0.00 USD | 504,420.00 USD |
| `1D` | `3861.80` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 60,240.00 USD | 0.00 USD | 173,960.00 USD |
| `7D` | `3865.50` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 192,300.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3866.00` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 74,140.00 USD | 0.00 USD | 134,060.00 USD |
| `7D` | `3869.70` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3870.20` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `7D` | `3873.90` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3874.40` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `7D` | `3878.10` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3878.60` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `7D` | `3882.30` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3882.80` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3886.50` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.00` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `3890.70` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.20` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 18,800.00 USD | 0.00 USD | 39,210.00 USD |
| `7D` | `3894.90` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3895.40` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.10` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3899.60` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 21,020.00 USD | 0.00 USD | 37,230.00 USD |
| `7D` | `3903.30` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.50` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 334,680.00 USD | 0.00 USD | 367,820.00 USD |
| `7D` | `3928.50` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3929.00` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.70` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3933.20` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3936.90` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3937.40` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 47,890.00 USD | 0.00 USD | 140,290.00 USD |
| `7D` | `3941.10` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 291,240.00 USD | 0.00 USD | 726,850.00 USD |
| `1D` | `3941.60` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 95,210.00 USD | 0.00 USD | 264,740.00 USD |
| `7D` | `3945.30` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 456,320.00 USD | 0.00 USD | 817,570.00 USD |
| `1D` | `3945.80` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 167,260.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.00` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3954.20` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3958.40` | 763,780.00 USD | 0.00 USD | 763,780.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3962.60` | 534,180.00 USD | 0.00 USD | 534,180.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3966.80` | 477,870.00 USD | 0.00 USD | 477,870.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.00` | 340,740.00 USD | 0.00 USD | 340,740.00 USD | 46,710.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.20` | 246,430.00 USD | 0.00 USD | 246,430.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.40` | 133,740.00 USD | 0.00 USD | 133,740.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3983.60` | 71,580.00 USD | 0.00 USD | 71,580.00 USD | 29,800.00 USD | 0.00 USD | 41,780.00 USD |
| `1D` | `4022.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4022.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
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
| `1D` | `4097.00` | 452,500.00 USD | 452,500.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 109,700.00 USD |
| `7D` | `4100.70` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 267,010.00 USD | 0.00 USD | 676,330.00 USD |
| `1D` | `4101.20` | 685,180.00 USD | 685,180.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 173,450.00 USD |
| `7D` | `4104.90` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 551,060.00 USD | 0.00 USD | 782,130.00 USD |
| `1D` | `4105.40` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 172,120.00 USD | 0.00 USD | 406,570.00 USD |
| `7D` | `4109.10` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 298,470.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4109.60` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `7D` | `4113.30` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4113.80` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `7D` | `4117.50` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.00` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `4121.70` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.20` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `4125.90` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4126.40` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4130.10` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4130.60` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4134.30` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4134.80` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 55,010.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.70` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.20` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 42,030.00 USD | 0.00 USD | 74,460.00 USD |
| `7D` | `4146.90` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.10` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4167.90` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.40` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `4172.10` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4172.60` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4176.30` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 227,820.00 USD |
| `1D` | `4176.80` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `7D` | `4180.50` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 143,630.00 USD | 0.00 USD | 275,830.00 USD |
| `1D` | `4181.00` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 68,280.00 USD |
| `7D` | `4184.70` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 276,110.00 USD | 0.00 USD | 363,510.00 USD |
| `1D` | `4185.20` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 81,790.00 USD | 0.00 USD | 203,210.00 USD |
| `7D` | `4188.90` | 18,850,000.00 USD | 18,850,000.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4189.40` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 53,390.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `4193.10` | 19,220,000.00 USD | 19,220,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4193.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `7D` | `4197.30` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4197.80` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `4201.50` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4202.00` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `4205.70` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.20` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.90` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4210.40` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4214.10` | 20,210,000.00 USD | 20,210,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4214.60` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4218.30` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4218.80` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `7D` | `4222.50` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.00` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `4226.70` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4227.20` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 14,900.00 USD | 0.00 USD | 20,890.00 USD |
| `7D` | `4377.90` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 20,840,000.00 USD | 20,840,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.30` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4407.80` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4411.50` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4412.00` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `4415.70` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4416.20` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `4419.90` | 21,630,000.00 USD | 21,630,000.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4420.40` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `7D` | `4424.10` | 21,760,000.00 USD | 21,760,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4424.60` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 47,850.00 USD |
| `7D` | `4428.30` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 53,630.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4428.80` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `7D` | `4432.50` | 22,060,000.00 USD | 22,060,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `4433.00` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4434.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 6,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4436.70` | 22,120,000.00 USD | 22,120,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 22,210,000.00 USD | 22,210,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `869.76M` | Total OI Tokens: `216,162.0 XAUT`
  * 1h OI Change: `+2.92%` | 4h OI Change: `+2.26%` | 24h OI Change: `+6.07%`
  * Exchange Breakdown: Binance=`62.03M` | Bybit=`143.73M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `40.66%` | `59.34%` | `0.69` | 3,260,000.00 USD |
| `15M` | `Binance` | `61.44%` | `38.56%` | `1.59` | 1,010,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 340,880.00 USD |
| `15M` | `Bybit` | `39.96%` | `60.04%` | `0.67` | 279,220.00 USD |
| `15M` | `KuCoin` | `48.45%` | `51.55%` | `0.94` | 46,720.00 USD |
| `15M` | `Gate` | `53.14%` | `46.86%` | `1.13` | 69,790.00 USD |
| `15M` | `Bitget` | `57.3%` | `42.7%` | `1.34` | 150,670.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 444,360.00 USD |
| `15M` | `MEXC` | `31.56%` | `68.44%` | `0.46` | 365,880.00 USD |
| `15M` | `Bitunix` | `35.91%` | `64.09%` | `0.56` | 130,170.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 107,340.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.09%` | `63.91%` | `0.56` | 220,580.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 2,190.00 USD |
| `15M` | `WhiteBIT` | `36.28%` | `63.72%` | `0.57` | 73,520.00 USD |
| `15M` | `HTX` | `41.56%` | `58.44%` | `0.71` | 187.92 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 151.71 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 1,130.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 22,550.00 USD |
| `15M` | `Whale Positions` | `61.44%` | `38.56%` | `1.59` | 1,010,000.00 USD |
| `15M` | `Global Accounts` | `40.66%` | `59.34%` | `0.69` | 3,260,000.00 USD |
| `1H` | `XAUT` | `53.90%` | `46.10%` | `1.17` | 23,620,000.00 USD |
| `1H` | `Binance` | `58.9%` | `41.1%` | `1.43` | 1,690,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `61.19%` | `38.81%` | `1.58` | 2,250,000.00 USD |
| `1H` | `KuCoin` | `46.15%` | `53.85%` | `0.86` | 63,890.00 USD |
| `1H` | `Gate` | `64.03%` | `35.97%` | `1.78` | 997,860.00 USD |
| `1H` | `Bitget` | `63.52%` | `36.48%` | `1.74` | 725,390.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `52.03%` | `47.97%` | `1.08` | 14,980,000.00 USD |
| `1H` | `Bitunix` | `44.54%` | `55.46%` | `0.80` | 669,220.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.1%` | `41.9%` | `1.39` | 1,740,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `23.1%` | `76.9%` | `0.30` | 425,680.00 USD |
| `1H` | `HTX` | `42.07%` | `57.93%` | `0.73` | 2,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `33.56%` | `66.44%` | `0.51` | 61,010.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `58.9%` | `41.1%` | `1.43` | 1,690,000.00 USD |
| `1H` | `Global Accounts` | `53.90%` | `46.10%` | `1.17` | 23,620,000.00 USD |
| `4H` | `XAUT` | `56.45%` | `43.55%` | `1.30` | 57,100,000.00 USD |
| `4H` | `Binance` | `58.08%` | `41.92%` | `1.39` | 4,390,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.1%` | `45.9%` | `1.18` | 5,680,000.00 USD |
| `4H` | `KuCoin` | `48.67%` | `51.33%` | `0.95` | 257,670.00 USD |
| `4H` | `Gate` | `57.91%` | `42.09%` | `1.38` | 2,180,000.00 USD |
| `4H` | `Bitget` | `50.4%` | `49.6%` | `1.02` | 1,990,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `58.73%` | `41.27%` | `1.42` | 34,960,000.00 USD |
| `4H` | `Bitunix` | `58.17%` | `41.83%` | `1.39` | 1,840,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.75%` | `46.25%` | `1.16` | 4,450,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.44%` | `87.56%` | `0.14` | 1,160,000.00 USD |
| `4H` | `HTX` | `66.82%` | `33.18%` | `2.01` | 12,950.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.04%` | `59.96%` | `0.67` | 160,550.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `58.08%` | `41.92%` | `1.39` | 4,390,000.00 USD |
| `4H` | `Global Accounts` | `56.45%` | `43.55%` | `1.30` | 57,100,000.00 USD |


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
| `5m` | -45,400.00 USD | -5,670.00 USD | **`DISTRIBUTION`** |
| `15m` | 72,790.00 USD | -52,300.00 USD | **`ACCUMULATION`** |
| `30m` | 144,100.00 USD | 608,520.00 USD | **`ACCUMULATION`** |
| `1h` | 275,740.00 USD | 771,840.00 USD | **`ACCUMULATION`** |
| `2h` | 77,750.00 USD | 924,110.00 USD | **`ACCUMULATION`** |
| `4h` | -437,680.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `6h` | -470,710.00 USD | 1,270,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,150,000.00 USD | 1,190,000.00 USD | **`ACCUMULATION`** |
| `12h` | 726,400.00 USD | 1,230,000.00 USD | **`ACCUMULATION`** |
| `24h` | -770,540.00 USD | 1,200,000.00 USD | **`ACCUMULATION`** |
| `1w` | -79,850,000.00 USD | -19,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,120,000.00 USD | -84,580,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-45.40K` | 15m=`+72.79K` | 1h=`+275.74K` | 24h=`-770.54K`
* Futures Capital Netflows: 5m=`-5.67K` | 15m=`-52.30K` | 1h=`+771.84K` | 24h=`+1.20M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26714.94` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26632.26` (Risk Distance: `82.68` pts)
  * +2.5R Take Profit: `26921.64`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26875.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26958.39` (Risk Distance: `82.68` pts)
  * +2.5R Take Profit: `26669.01`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`27009.69`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
