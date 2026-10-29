# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 03:55:35 IST` (`2026-10-29 22:25:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26749.52` | **Live Ask Quote**: `26752.08` | **Mid Price**: `26750.80`
- **Spread Points**: `256.00` | **Spread BPS**: `0.96 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26750.80` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.88` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26938.06` | Lower -3.00σ Band: `26563.54`
  * Upper +2.51σ Band: `26897.93` | Lower -2.51σ Band: `26603.67`
  * Upper +2.01σ Band: `26863.15` | Lower -2.01σ Band: `26638.45`
  * Upper +2.00σ Band: `26857.80` | Lower -2.00σ Band: `26643.80`
  * Upper +1.28σ Band: `26825.70` | Lower -1.28σ Band: `26675.90`
  * Upper +1.00σ Band: `26804.30` | Lower -1.00σ Band: `26697.30`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26750.80` | EMA-20=`26750.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26750.80` (Slope: `+0.0000`) | EMA-100=`26750.80`
  * Institutional Anchors: EMA-144=`26750.80` | EMA-200=`26750.80` (Slope: `+0.0000`) | EMA-233=`26750.80`
- **Range Boundaries**: 24H High=`27018.31` | 24H Low=`26483.29` | Weekly High=`27285.82` | Weekly Low=`26215.78`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26831.05` (Distance: `+0.00%`)
  * Point of Control (POC) = `26750.80` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26670.55` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26857.80` | POC=`26750.80` | VAL=`26643.80`
  * Prior Day Extremes: PDH=`26911.30` | PDL=`26590.30` | PDC=`26750.80`
  * Monday Range Blueprint: High=`26884.55` | Mid=`26750.80` | Low=`26617.05`
  * Developing Weekly Value Area: Weekly VAH=`26964.81` | Weekly POC=`26750.80` | Weekly VAL=`26536.79`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26804.30` | Low=`26697.30`
  * London Session (08:00-16:00 UTC): High=`26857.80` | Low=`26643.80`
  * New York Session (13:00-21:00 UTC): High=`26911.30` | Low=`26590.30`
  * Initial Balance (First Hour): IB High=`26831.05` | IB Low=`26670.55`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26643.80` - `26857.80`
  * Optimal Trade Entry (OTE 0.705): `26804.30`
  * Structural Invalidation Anchor (0.786): `26964.81`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `53` | `0x5b5d...c060` | `SHORT` | 25,604,116.58 USD | `6,365.38` | `4188.90` | `4022.20` | `33117.35` | 1,059,854.71 USD | `+4.14%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,495,222.05 USD | `6,338.15` | `4132.76` | `4022.20` | `13748.53` | 698,844.91 USD | `+2.74%` | `5X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 23,611,083.35 USD | `5,869.90` | `4228.86` | `4022.20` | `30781.92` | 1,211,938.59 USD | `+5.13%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,423,795.11 USD | `4,828.91` | `4157.43` | `4022.20` | `2254.41` | -652,087.20 USD | `-3.36%` | `25X Cross` |
| `145` | `0x645b...87b8` | `LONG` | 14,212,194.68 USD | `3,533.26` | `4129.11` | `4022.20` | `424.97` | -377,054.49 USD | `-2.65%` | `3X Cross` |
| `161` | `0x7a6d...f79c` | `SHORT` | 13,146,060.78 USD | `3,268.21` | `4228.94` | `4022.20` | `4397.75` | 675,018.35 USD | `+5.13%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,664,960.40 USD | `2,900.00` | `4364.92` | `4022.20` | `4235.67` | 993,315.93 USD | `+8.52%` | `20X Cross` |
| `259` | `0xfc66...ca06` | `SHORT` | 8,990,349.59 USD | `2,235.07` | `4031.28` | `4022.20` | `10915.66` | 19,863.05 USD | `+0.22%` | `3X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,849,500.00 USD | `2,200.00` | `4176.09` | `4022.20` | `2659.14` | -337,919.30 USD | `-3.82%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,849,280.00 USD | `2,200.00` | `4112.20` | `4022.20` | `4331.15` | 197,574.59 USD | `+2.23%` | `20X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,945,724.67 USD | `1,975.37` | `4048.55` | `4022.20` | `6503.19` | 51,667.05 USD | `+0.65%` | `6X Cross` |
| `371` | `0xc26c...b8f4` | `LONG` | 6,355,198.12 USD | `1,579.95` | `4075.62` | `4022.20` | `0.000000` | -84,098.85 USD | `-1.32%` | `1X Cross` |
| `402` | `0x12d2...f97f` | `LONG` | 5,639,174.72 USD | `1,401.94` | `4278.91` | `4022.20` | `3176.93` | -359,615.86 USD | `-6.38%` | `20X Cross` |
| `550` | `0x63da...8add` | `LONG` | 4,022,400.00 USD | `1,000.00` | `4021.46` | `4022.20` | `3564.11` | 939.04 USD | `+0.02%` | `25X Cross` |
| `560` | `0x354b...6425` | `LONG` | 3,973,167.26 USD | `987.74` | `4031.85` | `4022.20` | `0.000000` | -9,240.08 USD | `-0.23%` | `10X Cross` |
| `580` | `0x9aa5...58af` | `LONG` | 3,908,332.78 USD | `971.64` | `4279.98` | `4022.20` | `0.000000` | -250,276.30 USD | `-6.40%` | `20X Cross` |
| `603` | `0xf3dc...1672` | `LONG` | 3,743,916.53 USD | `930.74` | `4024.62` | `4022.20` | `3337.59` | -1,976.03 USD | `-0.05%` | `20X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,368,440.29 USD | `837.40` | `4599.73` | `4022.20` | `0.000000` | -483,380.09 USD | `-14.35%` | `20X Cross` |
| `818` | `0x0fac...7a0a` | `LONG` | 2,761,385.91 USD | `686.49` | `4290.34` | `4022.20` | `1446.04` | -183,872.79 USD | `-6.66%` | `25X Cross` |
| `874` | `0xd8c5...99b0` | `SHORT` | 2,583,872.59 USD | `642.35` | `4175.35` | `4022.20` | `32820.33` | 98,188.59 USD | `+3.80%` | `4X Cross` |
| `902` | `0x625e...a354` | `SHORT` | 2,493,888.00 USD | `620.00` | `4122.81` | `4022.20` | `4342.25` | 62,259.03 USD | `+2.50%` | `20X Cross` |
| `934` | `0xeae3...e8ad` | `SHORT` | 2,413,560.00 USD | `600.00` | `4104.77` | `4022.20` | `4325.27` | 49,305.11 USD | `+2.04%` | `20X Cross` |
| `938` | `0xf285...fa82` | `LONG` | 2,405,821.17 USD | `598.11` | `4146.45` | `4022.20` | `3891.24` | -74,198.38 USD | `-3.08%` | `25X Cross` |
| `962` | `0x12f7...8750` | `LONG` | 2,355,560.48 USD | `585.61` | `4082.77` | `4022.20` | `2577.36` | -35,356.50 USD | `-1.50%` | `10X Cross` |
| `1094` | `0x413c...886c` | `LONG` | 2,011,350.00 USD | `500.00` | `4010.43` | `4022.20` | `0.000000` | 6,133.77 USD | `+0.30%` | `2X Cross` |
| `1103` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.20` | `4715.04` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1107` | `0x0593...40f9` | `LONG` | 1,995,871.98 USD | `496.18` | `4024.57` | `4022.20` | `3701.73` | -1,031.85 USD | `-0.05%` | `10X Isolated` |
| `1228` | `0xead5...69f2` | `LONG` | 1,825,300.36 USD | `453.78` | `4220.88` | `4022.20` | `3538.94` | -90,067.70 USD | `-4.93%` | `5X Isolated` |
| `1338` | `0x46fc...1195` | `LONG` | 1,651,887.09 USD | `410.66` | `4055.10` | `4022.20` | `2141.68` | -13,389.40 USD | `-0.81%` | `20X Cross` |
| `1379` | `0x6d15...d374` | `LONG` | 1,608,960.00 USD | `400.00` | `4068.25` | `4022.20` | `3841.81` | -18,340.00 USD | `-1.14%` | `25X Cross` |
| `1380` | `0xee02...309d` | `SHORT` | 1,608,960.00 USD | `400.00` | `4438.84` | `4022.20` | `4226.89` | 166,578.60 USD | `+10.35%` | `25X Isolated` |
| `1416` | `0x02a7...fe9f` | `SHORT` | 1,568,736.00 USD | `390.00` | `4055.02` | `4022.20` | `4306.71` | 12,723.25 USD | `+0.81%` | `25X Cross` |
| `1456` | `0x7e77...b8d2` | `SHORT` | 1,528,664.00 USD | `380.00` | `4131.92` | `4022.20` | `4293.51` | 41,465.64 USD | `+2.71%` | `20X Cross` |
| `1470` | `0x72c2...9b37` | `LONG` | 1,500,920.65 USD | `373.13` | `4000.98` | `4022.20` | `3778.05` | 8,027.14 USD | `+0.53%` | `13X Isolated` |
| `1515` | `0xaa44...b844` | `LONG` | 1,448,100.00 USD | `360.00` | `4043.10` | `4022.20` | `2803.27` | -7,417.63 USD | `-0.51%` | `4X Cross` |
| `1626` | `0xa41f...d50a` | `LONG` | 1,323,217.15 USD | `328.96` | `4468.89` | `4022.20` | `3833.19` | -146,880.70 USD | `-11.10%` | `15X Cross` |
| `1660` | `0xbf5a...88ba` | `SHORT` | 1,277,735.07 USD | `317.65` | `4091.80` | `4022.20` | `9886.34` | 22,047.96 USD | `+1.73%` | `20X Cross` |
| `1695` | `0xff31...ff6c` | `SHORT` | 1,246,975.00 USD | `310.00` | `4372.43` | `4022.20` | `4789.18` | 108,480.38 USD | `+8.70%` | `10X Isolated` |
| `1705` | `0xada6...6f88` | `LONG` | 1,239,333.46 USD | `308.10` | `4166.46` | `4022.20` | `1898.73` | -44,355.56 USD | `-3.58%` | `5X Cross` |
| `1729` | `0x5238...54e5` | `LONG` | 1,206,720.00 USD | `300.00` | `4023.33` | `4022.20` | `3833.96` | -279.31 USD | `-0.02%` | `15X Isolated` |
| `1871` | `0x50e2...d770` | `LONG` | 1,087,552.87 USD | `270.37` | `4243.58` | `4022.20` | `2562.10` | -59,773.59 USD | `-5.50%` | `20X Cross` |
| `1890` | `0x4c92...4f17` | `SHORT` | 1,072,883.21 USD | `266.72` | `4260.98` | `4022.20` | `6505.31` | 63,609.03 USD | `+5.93%` | `20X Cross` |
| `1943` | `0xd346...c4f3` | `LONG` | 1,026,411.09 USD | `255.17` | `4188.66` | `4022.20` | `3310.43` | -42,425.42 USD | `-4.13%` | `5X Isolated` |
| `1991` | `0x1581...463b` | `LONG` | 1,005,600.00 USD | `250.00` | `4003.77` | `4022.20` | `3571.67` | 4,656.41 USD | `+0.46%` | `15X Cross` |

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
| `1D` | `3614.30` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 5,270.00 USD | 0.00 USD | 25,900.00 USD |
| `7D` | `3617.80` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.40` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 17,630.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.50` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 23,830.00 USD | 0.00 USD | 68,370.00 USD |
| `7D` | `3626.20` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3626.60` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 13,180.00 USD | 0.00 USD | 17,830.00 USD |
| `7D` | `3630.40` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.70` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 28,270.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3634.60` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3634.80` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 35,340.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3638.80` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3638.90` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.00` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 17,700.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3643.00` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3647.10` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,450.00 USD | 0.00 USD | 9,520.00 USD |
| `7D` | `3647.20` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3651.20` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 7,240.00 USD | 0.00 USD | 13,210.00 USD |
| `1D` | `3655.30` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3655.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.00` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `3848.80` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.10` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 15,390.00 USD | 0.00 USD | 56,320.00 USD |
| `7D` | `3853.00` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.20` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 24,210.00 USD | 0.00 USD | 73,650.00 USD |
| `7D` | `3857.20` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.30` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 81,130.00 USD | 0.00 USD | 103,900.00 USD |
| `7D` | `3861.40` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.40` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 84,570.00 USD | 0.00 USD | 219,310.00 USD |
| `7D` | `3865.60` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.50` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 43,350.00 USD | 0.00 USD | 59,260.00 USD |
| `7D` | `3869.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3872.60` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 76,790.00 USD | 0.00 USD | 141,780.00 USD |
| `7D` | `3874.00` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3876.70` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 91,460.00 USD | 0.00 USD | 57,290.00 USD |
| `7D` | `3878.20` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3880.80` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 25,200.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `3882.40` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3884.90` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 45,230.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `3886.60` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.00` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 11,030.00 USD | 0.00 USD | 19,510.00 USD |
| `7D` | `3890.80` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.10` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 23,320.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `3895.00` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3925.90` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.00` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 49,890.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `3932.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.10` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 24,210.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3937.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.20` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 82,040.00 USD | 0.00 USD | 199,890.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 181,230.00 USD | 0.00 USD | 404,740.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.40` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 148,140.00 USD | 0.00 USD | 219,880.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.50` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 85,520.00 USD | 0.00 USD | 148,290.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3954.60` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 146,690.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3958.70` | 579,650.00 USD | 0.00 USD | 579,650.00 USD | 161,750.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3962.80` | 373,790.00 USD | 0.00 USD | 373,790.00 USD | 40,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3966.90` | 326,000.00 USD | 0.00 USD | 326,000.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.00` | 188,870.00 USD | 0.00 USD | 188,870.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.10` | 122,480.00 USD | 0.00 USD | 122,480.00 USD | 46,630.00 USD | 0.00 USD | 38,680.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.20` | 37,170.00 USD | 0.00 USD | 37,170.00 USD | 9,780.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4016.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4016.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
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
| `1D` | `4130.90` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 36,180.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4134.40` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.00` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.10` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `1D` | `4167.80` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 8,040.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4168.00` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4171.90` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 21,210.00 USD | 0.00 USD | 60,020.00 USD |
| `7D` | `4172.20` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4176.00` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 49,010.00 USD |
| `7D` | `4176.40` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.10` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 68,300.00 USD | 0.00 USD | 100,580.00 USD |
| `7D` | `4180.60` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.20` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 74,810.00 USD | 0.00 USD | 192,300.00 USD |
| `7D` | `4184.80` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.30` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 62,590.00 USD | 0.00 USD | 88,140.00 USD |
| `7D` | `4189.00` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.40` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 42,760.00 USD | 0.00 USD | 71,970.00 USD |
| `7D` | `4193.20` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.50` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 73,350.00 USD | 0.00 USD | 136,440.00 USD |
| `7D` | `4197.40` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4200.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4201.60` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4204.70` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 23,730.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4208.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 45,230.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4212.90` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 11,030.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `4214.20` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.00` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 17,230.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `4218.40` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.10` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 10,980.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.70` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4413.80` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4415.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4417.90` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 17,310.00 USD |
| `7D` | `4420.00` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 13,320.00 USD | 0.00 USD | 28,980.00 USD |
| `7D` | `4424.20` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4426.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 16,740.00 USD | 0.00 USD | 61,140.00 USD |
| `7D` | `4428.40` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4429.00` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 15,330.00 USD | 0.00 USD | 20,440.00 USD |
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
  * Total Open Interest: `825.76M` | Total OI Tokens: `205,478.8 XAUT`
  * 1h OI Change: `+0.11%` | 4h OI Change: `-2.54%` | 24h OI Change: `-0.44%`
  * Exchange Breakdown: Binance=`61.65M` | Bybit=`142.88M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `48.86%` | `51.14%` | `0.96` | 2,270,000.00 USD |
| `15M` | `Binance` | `46.79%` | `53.21%` | `0.88` | 460,540.00 USD |
| `15M` | `OKX` | `57.26%` | `42.74%` | `1.34` | 0.00 USD |
| `15M` | `Bybit` | `42.34%` | `57.66%` | `0.73` | 333,140.00 USD |
| `15M` | `KuCoin` | `41.53%` | `58.47%` | `0.71` | 36,430.00 USD |
| `15M` | `Gate` | `57.9%` | `42.1%` | `1.38` | 243,080.00 USD |
| `15M` | `Bitget` | `52.32%` | `47.68%` | `1.10` | 211,550.00 USD |
| `15M` | `BingX` | `45.87%` | `54.13%` | `0.85` | 0.00 USD |
| `15M` | `MEXC` | `38.72%` | `61.28%` | `0.63` | 630,100.00 USD |
| `15M` | `Bitunix` | `56.3%` | `43.7%` | `1.29` | 43,590.00 USD |
| `15M` | `Hyperliquid` | `59.48%` | `40.52%` | `1.47` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `64.32%` | `35.68%` | `1.80` | 259,670.00 USD |
| `15M` | `Crypto.com` | `65.1%` | `34.9%` | `1.87` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.75%` | `1.25%` | `79.00` | 37,970.00 USD |
| `15M` | `HTX` | `32.05%` | `67.95%` | `0.47` | 939.90 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `48.69%` | `51.31%` | `0.95` | 7,650.00 USD |
| `15M` | `Aster` | `14.88%` | `85.12%` | `0.17` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.93%` | `53.07%` | `0.88` | 0.00 USD |
| `15M` | `Whale Positions` | `46.79%` | `53.21%` | `0.88` | 460,540.00 USD |
| `15M` | `Global Accounts` | `48.86%` | `51.14%` | `0.96` | 2,270,000.00 USD |
| `1H` | `XAUT` | `49.73%` | `50.27%` | `0.99` | 40,240,000.00 USD |
| `1H` | `Binance` | `47.39%` | `52.61%` | `0.90` | 15,620,000.00 USD |
| `1H` | `OKX` | `58.94%` | `41.06%` | `1.44` | 6,070,000.00 USD |
| `1H` | `Bybit` | `45.46%` | `54.54%` | `0.83` | 7,980,000.00 USD |
| `1H` | `KuCoin` | `50.41%` | `49.59%` | `1.02` | 209,600.00 USD |
| `1H` | `Gate` | `54.69%` | `45.31%` | `1.21` | 1,270,000.00 USD |
| `1H` | `Bitget` | `45.29%` | `54.71%` | `0.83` | 1,150,000.00 USD |
| `1H` | `BingX` | `46.43%` | `53.57%` | `0.87` | 901,410.00 USD |
| `1H` | `MEXC` | `46.55%` | `53.45%` | `0.87` | 2,060,000.00 USD |
| `1H` | `Bitunix` | `47.07%` | `52.93%` | `0.89` | 723,340.00 USD |
| `1H` | `Hyperliquid` | `56.72%` | `43.28%` | `1.31` | 1,550,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.39%` | `49.61%` | `1.02` | 1,790,000.00 USD |
| `1H` | `Crypto.com` | `54.28%` | `45.72%` | `1.19` | 16,210.00 USD |
| `1H` | `WhiteBIT` | `85.3%` | `14.7%` | `5.80` | 522,220.00 USD |
| `1H` | `HTX` | `40.07%` | `59.93%` | `0.67` | 4,620.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `31.36%` | `68.64%` | `0.46` | 156,760.00 USD |
| `1H` | `Aster` | `39.56%` | `60.44%` | `0.65` | 94,870.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `33.71%` | `66.29%` | `0.51` | 133,930.00 USD |
| `1H` | `Whale Positions` | `47.39%` | `52.61%` | `0.90` | 15,620,000.00 USD |
| `1H` | `Global Accounts` | `49.73%` | `50.27%` | `0.99` | 40,240,000.00 USD |
| `4H` | `XAUT` | `46.38%` | `53.62%` | `0.86` | 61,690,000.00 USD |
| `4H` | `Binance` | `54.46%` | `45.54%` | `1.20` | 6,480,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.15%` | `45.85%` | `1.18` | 5,980,000.00 USD |
| `4H` | `KuCoin` | `23.05%` | `76.95%` | `0.30` | 309,740.00 USD |
| `4H` | `Gate` | `51.56%` | `48.44%` | `1.06` | 2,730,000.00 USD |
| `4H` | `Bitget` | `59.88%` | `40.12%` | `1.49` | 1,990,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `41.52%` | `58.48%` | `0.71` | 34,560,000.00 USD |
| `4H` | `Bitunix` | `47.83%` | `52.17%` | `0.92` | 3,580,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `59.07%` | `40.93%` | `1.44` | 4,930,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `15.18%` | `84.82%` | `0.18` | 1,010,000.00 USD |
| `4H` | `HTX` | `34.09%` | `65.91%` | `0.52` | 11,150.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.87%` | `60.13%` | `0.66` | 109,830.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.46%` | `45.54%` | `1.20` | 6,480,000.00 USD |
| `4H` | `Global Accounts` | `46.38%` | `53.62%` | `0.86` | 61,690,000.00 USD |


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
| `5m` | -86,220.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | 125,810.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | -339,700.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -289,790.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -35,360.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -168,990.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -264,570.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -845,940.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | 261,290.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `24h` | -450,670.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -80,310,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,720,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-86.22K` | 15m=`+125.81K` | 1h=`-289.79K` | 24h=`-450.67K`
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
  * `2026-10-30 03:30:02 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:54:02 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:51:02 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:02 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26670.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26586.46` (Risk Distance: `84.09` pts)
  * +2.5R Take Profit: `26880.78`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26831.05` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26915.14` (Risk Distance: `84.09` pts)
  * +2.5R Take Profit: `26620.82`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26964.81`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
