# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:18:33 IST` (`2026-10-29 20:48:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26781.98` | **Live Ask Quote**: `26785.31` | **Mid Price**: `26783.65`
- **Spread Points**: `333.00` | **Spread BPS**: `1.24 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26783.65` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.96` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26971.13` | Lower -3.00σ Band: `26596.16`
  * Upper +2.51σ Band: `26930.96` | Lower -2.51σ Band: `26636.33`
  * Upper +2.01σ Band: `26896.14` | Lower -2.01σ Band: `26671.15`
  * Upper +2.00σ Band: `26890.78` | Lower -2.00σ Band: `26676.51`
  * Upper +1.28σ Band: `26858.64` | Lower -1.28σ Band: `26708.65`
  * Upper +1.00σ Band: `26837.21` | Lower -1.00σ Band: `26730.08`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26783.65` | EMA-20=`26783.65` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26783.65` (Slope: `+0.0000`) | EMA-100=`26783.65`
  * Institutional Anchors: EMA-144=`26783.65` | EMA-200=`26783.65` (Slope: `+0.0000`) | EMA-233=`26783.65`
- **Range Boundaries**: 24H High=`27051.48` | 24H Low=`26515.81` | Weekly High=`27319.32` | Weekly Low=`26247.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26864.00` (Distance: `+0.00%`)
  * Point of Control (POC) = `26783.65` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26703.29` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26890.78` | POC=`26783.65` | VAL=`26676.51`
  * Prior Day Extremes: PDH=`26944.35` | PDL=`26622.94` | PDC=`26783.65`
  * Monday Range Blueprint: High=`26917.56` | Mid=`26783.65` | Low=`26649.73`
  * Developing Weekly Value Area: Weekly VAH=`26997.91` | Weekly POC=`26783.65` | Weekly VAL=`26569.38`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26837.21` | Low=`26730.08`
  * London Session (08:00-16:00 UTC): High=`26890.78` | Low=`26676.51`
  * New York Session (13:00-21:00 UTC): High=`26944.35` | Low=`26622.94`
  * Initial Balance (First Hour): IB High=`26864.00` | IB Low=`26703.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26676.51` - `26890.78`
  * Optimal Trade Entry (OTE 0.705): `26837.21`
  * Structural Invalidation Anchor (0.786): `26997.91`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x5b5d...c060` | `SHORT` | 25,503,135.31 USD | `6,334.29` | `4191.43` | `4023.10` | `31463.80` | 1,046,671.13 USD | `+4.10%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,396,629.75 USD | `6,311.29` | `4133.61` | `4023.10` | `13622.06` | 691,789.38 USD | `+2.72%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,034,032.32 USD | `5,717.06` | `4234.49` | `4023.10` | `29670.02` | 1,174,842.91 USD | `+5.10%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,441,662.07 USD | `4,828.91` | `4157.43` | `4023.10` | `2174.12` | -634,220.25 USD | `-3.26%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,164,961.89 USD | `3,520.56` | `4129.51` | `4023.10` | `355.95` | -373,227.47 USD | `-2.63%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,151,616.74 USD | `3,268.21` | `4228.94` | `4023.10` | `4392.92` | 669,462.39 USD | `+5.09%` | `25X Cross` |
| `177` | `0xa742...e390` | `SHORT` | 11,675,980.40 USD | `2,900.00` | `4364.92` | `4023.10` | `4235.64` | 982,295.93 USD | `+8.41%` | `20X Cross` |
| `270` | `0x41e5...0825` | `SHORT` | 8,863,580.00 USD | `2,200.00` | `4112.20` | `4023.10` | `4331.13` | 183,274.59 USD | `+2.07%` | `20X Cross` |
| `273` | `0x3678...b209` | `LONG` | 8,851,040.00 USD | `2,200.00` | `4176.09` | `4023.10` | `2712.70` | -336,379.30 USD | `-3.80%` | `25X Cross` |
| `306` | `0xfc66...ca06` | `SHORT` | 7,970,847.70 USD | `1,981.17` | `4032.86` | `4023.10` | `24530.00` | 18,958.52 USD | `+0.24%` | `3X Cross` |
| `308` | `0xacb6...efbd` | `SHORT` | 7,953,231.07 USD | `1,975.37` | `4048.55` | `4023.10` | `6484.06` | 44,160.64 USD | `+0.56%` | `6X Cross` |
| `379` | `0xc26c...b8f4` | `LONG` | 6,357,884.04 USD | `1,579.95` | `4075.62` | `4023.10` | `0.000000` | -81,412.93 USD | `-1.28%` | `1X Cross` |
| `412` | `0x12d2...f97f` | `LONG` | 5,644,502.10 USD | `1,401.94` | `4278.91` | `4023.10` | `2842.10` | -354,288.48 USD | `-6.28%` | `20X Cross` |
| `562` | `0x63da...8add` | `LONG` | 4,024,100.00 USD | `1,000.00` | `4021.46` | `4023.10` | `3564.08` | 2,639.04 USD | `+0.07%` | `25X Cross` |
| `586` | `0x354b...6425` | `LONG` | 3,935,944.50 USD | `978.29` | `4031.93` | `4023.10` | `0.000000` | -8,444.62 USD | `-0.21%` | `10X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,911,927.86 USD | `971.64` | `4279.98` | `4023.10` | `0.000000` | -246,681.23 USD | `-6.31%` | `20X Cross` |
| `617` | `0xf3dc...1672` | `LONG` | 3,745,312.65 USD | `930.74` | `4024.62` | `4023.10` | `3337.56` | -579.91 USD | `-0.02%` | `20X Cross` |
| `681` | `0x4a20...3c26` | `LONG` | 3,369,110.21 USD | `837.40` | `4599.73` | `4023.10` | `0.000000` | -482,710.17 USD | `-14.33%` | `20X Cross` |
| `839` | `0x0fac...7a0a` | `LONG` | 2,761,729.15 USD | `686.49` | `4290.34` | `4023.10` | `1592.26` | -183,529.55 USD | `-6.65%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,584,258.00 USD | `642.35` | `4175.35` | `4023.10` | `32697.38` | 97,803.18 USD | `+3.78%` | `4X Cross` |
| `909` | `0x625e...a354` | `SHORT` | 2,496,368.00 USD | `620.00` | `4122.81` | `4023.10` | `4342.23` | 59,779.03 USD | `+2.39%` | `20X Cross` |
| `933` | `0xeae3...e8ad` | `SHORT` | 2,413,920.00 USD | `600.00` | `4104.77` | `4023.10` | `4325.25` | 48,945.11 USD | `+2.03%` | `20X Cross` |
| `940` | `0xf285...fa82` | `LONG` | 2,408,093.97 USD | `598.11` | `4146.45` | `4023.10` | `3891.22` | -71,925.58 USD | `-2.99%` | `25X Cross` |
| `957` | `0x12f7...8750` | `LONG` | 2,356,556.02 USD | `585.61` | `4082.77` | `4023.10` | `2534.97` | -34,360.96 USD | `-1.46%` | `10X Cross` |
| `1114` | `0x413c...886c` | `LONG` | 2,011,500.00 USD | `500.00` | `4010.43` | `4023.10` | `0.000000` | 6,283.77 USD | `+0.31%` | `2X Cross` |
| `1124` | `0x61ce...a62b` | `SHORT` | 2,001,556.08 USD | `497.50` | `4071.66` | `4023.10` | `4716.94` | 24,112.71 USD | `+1.20%` | `20X Cross` |
| `1132` | `0x0593...40f9` | `LONG` | 1,996,169.69 USD | `496.18` | `4024.57` | `4023.10` | `3701.71` | -734.14 USD | `-0.04%` | `10X Isolated` |
| `1249` | `0xead5...69f2` | `LONG` | 1,828,159.20 USD | `453.78` | `4220.88` | `4023.10` | `3538.92` | -87,208.86 USD | `-4.77%` | `5X Isolated` |
| `1364` | `0x46fc...1195` | `LONG` | 1,647,454.13 USD | `409.49` | `4055.28` | `4023.10` | `2053.63` | -13,136.75 USD | `-0.80%` | `20X Cross` |
| `1393` | `0x6d15...d374` | `LONG` | 1,611,600.00 USD | `400.00` | `4068.25` | `4023.10` | `3841.79` | -15,700.00 USD | `-0.97%` | `25X Cross` |
| `1396` | `0xee02...309d` | `SHORT` | 1,610,480.00 USD | `400.00` | `4438.84` | `4023.10` | `4226.86` | 165,058.60 USD | `+10.25%` | `25X Isolated` |
| `1437` | `0x02a7...fe9f` | `SHORT` | 1,569,399.00 USD | `390.00` | `4055.02` | `4023.10` | `4306.68` | 12,060.25 USD | `+0.77%` | `25X Cross` |
| `1479` | `0x7e77...b8d2` | `SHORT` | 1,528,778.00 USD | `380.00` | `4131.92` | `4023.10` | `4293.49` | 41,351.64 USD | `+2.70%` | `20X Cross` |
| `1501` | `0x72c2...9b37` | `LONG` | 1,501,107.22 USD | `373.13` | `4000.98` | `4023.10` | `3778.02` | 8,213.70 USD | `+0.55%` | `13X Isolated` |
| `1537` | `0xaa44...b844` | `LONG` | 1,448,640.00 USD | `360.00` | `4043.10` | `4023.10` | `2803.24` | -6,877.63 USD | `-0.47%` | `4X Cross` |
| `1646` | `0xa41f...d50a` | `LONG` | 1,324,434.31 USD | `328.96` | `4468.89` | `4023.10` | `3833.16` | -145,663.54 USD | `-11.00%` | `15X Cross` |
| `1665` | `0x49e9...e1d0` | `SHORT` | 1,302,230.22 USD | `323.48` | `4025.23` | `4023.10` | `31676.92` | -151.89 USD | `-0.01%` | `4X Cross` |
| `1688` | `0xada6...6f88` | `LONG` | 1,284,445.74 USD | `319.28` | `4166.46` | `4023.10` | `1935.33` | -45,804.77 USD | `-3.57%` | `5X Cross` |
| `1694` | `0xbf5a...88ba` | `SHORT` | 1,278,942.16 USD | `317.65` | `4091.80` | `4023.10` | `10297.64` | 20,840.87 USD | `+1.63%` | `20X Cross` |
| `1728` | `0xff31...ff6c` | `SHORT` | 1,247,192.00 USD | `310.00` | `4372.43` | `4023.10` | `4789.15` | 108,263.38 USD | `+8.68%` | `10X Isolated` |
| `1898` | `0x50e2...d770` | `LONG` | 1,087,769.16 USD | `270.37` | `4243.58` | `4023.10` | `2562.07` | -59,557.30 USD | `-5.48%` | `20X Cross` |
| `1918` | `0x4c92...4f17` | `SHORT` | 1,073,309.96 USD | `266.72` | `4260.98` | `4023.10` | `6503.96` | 63,182.27 USD | `+5.89%` | `20X Cross` |
| `1974` | `0xd346...c4f3` | `LONG` | 1,027,380.75 USD | `255.17` | `4188.66` | `4023.10` | `3310.40` | -41,455.75 USD | `-4.04%` | `5X Isolated` |
| `2008` | `0x1581...463b` | `LONG` | 1,007,275.00 USD | `250.00` | `4003.77` | `4023.10` | `3504.62` | 6,331.41 USD | `+0.63%` | `15X Cross` |
| `2014` | `0xe47f...758c` | `LONG` | 1,006,050.00 USD | `250.00` | `4020.00` | `4023.10` | `3774.32` | 1,050.00 USD | `+0.10%` | `20X Cross` |

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
| `1D` | `3607.20` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 4,980.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `3609.30` | 21,630,000.00 USD | 0.00 USD | 21,630,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3611.40` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 4,320.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `3613.50` | 21,580,000.00 USD | 0.00 USD | 21,580,000.00 USD | 76,290.00 USD | 0.00 USD | 59,640.00 USD |
| `1D` | `3615.60` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 7,520.00 USD | 0.00 USD | 21,740.00 USD |
| `7D` | `3617.70` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 38,860.00 USD | 0.00 USD | 93,380.00 USD |
| `1D` | `3619.80` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 10,780.00 USD | 0.00 USD | 41,740.00 USD |
| `7D` | `3621.90` | 21,320,000.00 USD | 0.00 USD | 21,320,000.00 USD | 79,860.00 USD | 0.00 USD | 127,200.00 USD |
| `1D` | `3624.00` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 22,610.00 USD | 0.00 USD | 57,190.00 USD |
| `7D` | `3626.10` | 21,110,000.00 USD | 0.00 USD | 21,110,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3628.20` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 19,660.00 USD | 0.00 USD | 17,120.00 USD |
| `7D` | `3630.30` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3632.40` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 26,060.00 USD | 0.00 USD | 58,360.00 USD |
| `7D` | `3634.50` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3636.60` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 31,600.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3638.70` | 20,750,000.00 USD | 0.00 USD | 20,750,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3640.80` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 12,480.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `3642.90` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3645.00` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 8,670.00 USD | 0.00 USD | 10,420.00 USD |
| `7D` | `3647.10` | 20,640,000.00 USD | 0.00 USD | 20,640,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3649.20` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 4,800.00 USD | 0.00 USD | 13,090.00 USD |
| `7D` | `3651.30` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3653.40` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 5,880.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.50` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3657.60` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 6,030.00 USD | 0.00 USD | 14,250.00 USD |
| `7D` | `3659.70` | 20,580,000.00 USD | 0.00 USD | 20,580,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 20,410,000.00 USD | 0.00 USD | 20,410,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 19,900,000.00 USD | 0.00 USD | 19,900,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,110,000.00 USD | 0.00 USD | 18,110,000.00 USD | 156,600.00 USD | 0.00 USD | 170,790.00 USD |
| `1D` | `3846.60` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 8,040.00 USD | 0.00 USD | 37,460.00 USD |
| `7D` | `3848.70` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 65,850.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3850.80` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 18,330.00 USD | 0.00 USD | 62,950.00 USD |
| `7D` | `3852.90` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 164,660.00 USD | 0.00 USD | 106,350.00 USD |
| `1D` | `3855.00` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 10,670.00 USD | 0.00 USD | 69,730.00 USD |
| `7D` | `3857.10` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 216,800.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3859.20` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 28,860.00 USD | 0.00 USD | 68,820.00 USD |
| `7D` | `3861.30` | 16,690,000.00 USD | 0.00 USD | 16,690,000.00 USD | 191,980.00 USD | 0.00 USD | 504,420.00 USD |
| `1D` | `3863.40` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 86,790.00 USD | 0.00 USD | 207,740.00 USD |
| `7D` | `3865.50` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 192,300.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3867.60` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 57,970.00 USD | 0.00 USD | 92,380.00 USD |
| `7D` | `3869.70` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3871.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 79,720.00 USD | 0.00 USD | 139,720.00 USD |
| `7D` | `3873.90` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3876.00` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 85,890.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `3878.10` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3880.20` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 35,070.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `3882.30` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3884.40` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 45,230.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3886.50` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3888.60` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 11,030.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `3890.70` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3892.80` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 23,320.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `3894.90` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.00` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 10,410.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.10` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3901.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 19,220.00 USD | 0.00 USD | 37,230.00 USD |
| `7D` | `3903.30` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.50` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 8,880,000.00 USD | 0.00 USD | 8,880,000.00 USD | 334,680.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.40` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 16,080.00 USD | 0.00 USD | 49,460.00 USD |
| `7D` | `3928.50` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.60` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 36,670.00 USD | 0.00 USD | 119,080.00 USD |
| `7D` | `3932.70` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.80` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 21,350.00 USD | 0.00 USD | 139,170.00 USD |
| `7D` | `3936.90` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3939.00` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 49,900.00 USD | 0.00 USD | 170,210.00 USD |
| `7D` | `3941.10` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 291,240.00 USD | 0.00 USD | 726,850.00 USD |
| `1D` | `3943.20` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 170,110.00 USD | 0.00 USD | 375,410.00 USD |
| `7D` | `3945.30` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 456,320.00 USD | 0.00 USD | 817,570.00 USD |
| `1D` | `3947.40` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 109,690.00 USD | 0.00 USD | 216,000.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3951.60` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 117,220.00 USD | 0.00 USD | 214,020.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3955.80` | 971,310.00 USD | 0.00 USD | 971,310.00 USD | 192,180.00 USD | 0.00 USD | 189,050.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3960.00` | 590,090.00 USD | 0.00 USD | 590,090.00 USD | 109,530.00 USD | 0.00 USD | 23,580.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3964.20` | 456,980.00 USD | 0.00 USD | 456,980.00 USD | 60,150.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3968.40` | 389,800.00 USD | 0.00 USD | 389,800.00 USD | 47,230.00 USD | 0.00 USD | 64,250.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3972.60` | 278,320.00 USD | 0.00 USD | 278,320.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3976.80` | 185,780.00 USD | 0.00 USD | 185,780.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3981.00` | 116,500.00 USD | 0.00 USD | 116,500.00 USD | 42,030.00 USD | 0.00 USD | 74,460.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4024.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4024.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 415,530.00 USD |
| `1D` | `4086.00` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.10` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4090.20` | 200,730.00 USD | 200,730.00 USD | 0.00 USD | 40,090.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.30` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 230,630.00 USD | 0.00 USD | 290,760.00 USD |
| `1D` | `4094.40` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 26,730.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.50` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.60` | 510,710.00 USD | 510,710.00 USD | 0.00 USD | 47,890.00 USD | 0.00 USD | 148,470.00 USD |
| `7D` | `4100.70` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 267,010.00 USD | 0.00 USD | 676,330.00 USD |
| `1D` | `4102.80` | 918,170.00 USD | 918,170.00 USD | 0.00 USD | 106,640.00 USD | 0.00 USD | 300,830.00 USD |
| `7D` | `4104.90` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 551,060.00 USD | 0.00 USD | 782,130.00 USD |
| `1D` | `4107.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 166,640.00 USD | 0.00 USD | 310,860.00 USD |
| `7D` | `4109.10` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 298,470.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4111.20` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 81,230.00 USD | 0.00 USD | 103,910.00 USD |
| `7D` | `4113.30` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4115.40` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 148,740.00 USD | 0.00 USD | 296,360.00 USD |
| `7D` | `4117.50` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4119.60` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 157,290.00 USD | 0.00 USD | 86,190.00 USD |
| `7D` | `4121.70` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.80` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 47,460.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `4125.90` | 12,720,000.00 USD | 12,720,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4128.00` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 93,710.00 USD | 0.00 USD | 32,390.00 USD |
| `7D` | `4130.10` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4132.20` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 18,800.00 USD | 0.00 USD | 41,110.00 USD |
| `7D` | `4134.30` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4136.40` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 46,630.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.50` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4140.60` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 20,830.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.70` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4144.80` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 38,450.00 USD | 0.00 USD | 74,460.00 USD |
| `7D` | `4146.90` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.10` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4167.90` | 16,630,000.00 USD | 16,630,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4170.00` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `4172.10` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4174.20` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `4176.30` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 227,820.00 USD |
| `1D` | `4178.40` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 23,940.00 USD | 0.00 USD | 70,140.00 USD |
| `7D` | `4180.50` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 143,630.00 USD | 0.00 USD | 275,830.00 USD |
| `1D` | `4182.60` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 44,460.00 USD | 0.00 USD | 104,330.00 USD |
| `7D` | `4184.70` | 18,360,000.00 USD | 18,360,000.00 USD | 0.00 USD | 276,110.00 USD | 0.00 USD | 363,510.00 USD |
| `1D` | `4186.80` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 72,740.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `4188.90` | 18,850,000.00 USD | 18,850,000.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4191.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 46,100.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `4193.10` | 19,220,000.00 USD | 19,220,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4195.20` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 134,500.00 USD |
| `7D` | `4197.30` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4199.40` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 81,580.00 USD | 0.00 USD | 62,040.00 USD |
| `7D` | `4201.50` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4203.60` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 35,070.00 USD | 0.00 USD | 7,160.00 USD |
| `7D` | `4205.70` | 19,960,000.00 USD | 19,960,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4207.80` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `4209.90` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4212.00` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 18,090.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `4214.10` | 20,210,000.00 USD | 20,210,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4216.20` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 17,230.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `4218.30` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4220.40` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 14,710.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.50` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4224.60` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 21,020.00 USD | 0.00 USD | 37,230.00 USD |
| `7D` | `4226.70` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4377.90` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 20,840,000.00 USD | 20,840,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.30` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.40` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 23,310.00 USD |
| `7D` | `4411.50` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4413.60` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 16,680.00 USD |
| `7D` | `4415.70` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4417.80` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 7,480.00 USD | 0.00 USD | 17,310.00 USD |
| `7D` | `4419.90` | 21,630,000.00 USD | 21,630,000.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4422.00` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | 18,190.00 USD |
| `7D` | `4424.10` | 21,760,000.00 USD | 21,760,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4426.20` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 16,740.00 USD | 0.00 USD | 61,140.00 USD |
| `7D` | `4428.30` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 53,630.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4430.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 17,590.00 USD | 0.00 USD | 27,280.00 USD |
| `7D` | `4432.50` | 22,060,000.00 USD | 22,060,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `4433.90` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 11,170.00 USD | 0.00 USD | 6,960.00 USD |
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
  * Total Open Interest: `825.09M` | Total OI Tokens: `205,298.7 XAUT`
  * 1h OI Change: `-2.24%` | 4h OI Change: `-1.97%` | 24h OI Change: `+0.64%`
  * Exchange Breakdown: Binance=`61.76M` | Bybit=`143.46M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `19.58%` | `80.42%` | `0.24` | 11,400,000.00 USD |
| `15M` | `Binance` | `38.42%` | `61.58%` | `0.62` | 906,580.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `40.9%` | `59.1%` | `0.69` | 377,950.00 USD |
| `15M` | `KuCoin` | `32.32%` | `67.68%` | `0.48` | 11,270.00 USD |
| `15M` | `Gate` | `41%` | `59%` | `0.69` | 216,560.00 USD |
| `15M` | `Bitget` | `48.92%` | `51.08%` | `0.96` | 95,620.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `14.78%` | `85.22%` | `0.17` | 8,790,000.00 USD |
| `15M` | `Bitunix` | `17.66%` | `82.34%` | `0.21` | 331,830.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `39.18%` | `60.82%` | `0.64` | 594,440.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 75,920.00 USD |
| `15M` | `HTX` | `30.7%` | `69.3%` | `0.44` | 759.79 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 3,410.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `38.42%` | `61.58%` | `0.62` | 906,580.00 USD |
| `15M` | `Global Accounts` | `19.58%` | `80.42%` | `0.24` | 11,400,000.00 USD |
| `1H` | `XAUT` | `41.93%` | `58.07%` | `0.72` | 42,730,000.00 USD |
| `1H` | `Binance` | `40.46%` | `59.54%` | `0.68` | 16,730,000.00 USD |
| `1H` | `OKX` | `40.64%` | `59.36%` | `0.68` | 6,400,000.00 USD |
| `1H` | `Bybit` | `42.21%` | `57.79%` | `0.73` | 4,950,000.00 USD |
| `1H` | `KuCoin` | `41.99%` | `58.01%` | `0.72` | 363,360.00 USD |
| `1H` | `Gate` | `43.84%` | `56.16%` | `0.78` | 1,560,000.00 USD |
| `1H` | `Bitget` | `40.02%` | `59.98%` | `0.67` | 1,880,000.00 USD |
| `1H` | `BingX` | `61.35%` | `38.65%` | `1.59` | 1,510,000.00 USD |
| `1H` | `MEXC` | `43.36%` | `56.64%` | `0.77` | 4,710,000.00 USD |
| `1H` | `Bitunix` | `46.39%` | `53.61%` | `0.87` | 846,110.00 USD |
| `1H` | `Hyperliquid` | `29.48%` | `70.52%` | `0.42` | 1,860,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.24%` | `48.76%` | `1.05` | 1,240,000.00 USD |
| `1H` | `Crypto.com` | `44.4%` | `55.6%` | `0.80` | 9,660.00 USD |
| `1H` | `WhiteBIT` | `64.6%` | `35.4%` | `1.82` | 238,840.00 USD |
| `1H` | `HTX` | `51.13%` | `48.87%` | `1.05` | 26,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.4%` | `58.6%` | `0.71` | 183,950.00 USD |
| `1H` | `Aster` | `29.79%` | `70.21%` | `0.42` | 93,880.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `35.17%` | `64.83%` | `0.54` | 120,250.00 USD |
| `1H` | `Whale Positions` | `40.46%` | `59.54%` | `0.68` | 16,730,000.00 USD |
| `1H` | `Global Accounts` | `41.93%` | `58.07%` | `0.72` | 42,730,000.00 USD |
| `4H` | `XAUT` | `46.57%` | `53.43%` | `0.87` | 64,550,000.00 USD |
| `4H` | `Binance` | `53.85%` | `46.15%` | `1.17` | 5,070,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `53.12%` | `46.88%` | `1.13` | 5,930,000.00 USD |
| `4H` | `KuCoin` | `48.1%` | `51.9%` | `0.93` | 261,390.00 USD |
| `4H` | `Gate` | `56.03%` | `43.97%` | `1.27` | 2,350,000.00 USD |
| `4H` | `Bitget` | `51.03%` | `48.97%` | `1.04` | 1,980,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `44.29%` | `55.71%` | `0.80` | 40,610,000.00 USD |
| `4H` | `Bitunix` | `50.12%` | `49.88%` | `1.00` | 2,230,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.25%` | `49.75%` | `1.01` | 4,820,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.58%` | `87.42%` | `0.14` | 1,150,000.00 USD |
| `4H` | `HTX` | `58.86%` | `41.14%` | `1.43` | 14,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.97%` | `63.03%` | `0.59` | 149,000.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.85%` | `46.15%` | `1.17` | 5,070,000.00 USD |
| `4H` | `Global Accounts` | `46.57%` | `53.43%` | `0.87` | 64,550,000.00 USD |


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
| `5m` | -164,150.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -275,740.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -235,310.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -100,610.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -112,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -602,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -661,740.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,230,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | 592,590.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `24h` | -992,750.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -79,970,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,770,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-164.15K` | 15m=`-275.74K` | 1h=`-100.61K` | 24h=`-992.75K`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26703.29` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26617.95` (Risk Distance: `85.35` pts)
  * +2.5R Take Profit: `26916.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26864.00` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26949.34` (Risk Distance: `85.35` pts)
  * +2.5R Take Profit: `26650.63`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26997.91`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
