# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 04:25:55 IST` (`2026-10-29 22:55:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26793.68` | **Live Ask Quote**: `26800.06` | **Mid Price**: `26796.87`
- **Spread Points**: `638.00` | **Spread BPS**: `2.38 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26796.87` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.99` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26984.45` | Lower -3.00σ Band: `26609.29`
  * Upper +2.51σ Band: `26944.25` | Lower -2.51σ Band: `26649.49`
  * Upper +2.01σ Band: `26909.42` | Lower -2.01σ Band: `26684.32`
  * Upper +2.00σ Band: `26904.06` | Lower -2.00σ Band: `26689.68`
  * Upper +1.28σ Band: `26871.90` | Lower -1.28σ Band: `26721.84`
  * Upper +1.00σ Band: `26850.46` | Lower -1.00σ Band: `26743.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26796.87` | EMA-20=`26796.87` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26796.87` (Slope: `+0.0000`) | EMA-100=`26796.87`
  * Institutional Anchors: EMA-144=`26796.87` | EMA-200=`26796.87` (Slope: `+0.0000`) | EMA-233=`26796.87`
- **Range Boundaries**: 24H High=`27064.84` | 24H Low=`26528.90` | Weekly High=`27332.81` | Weekly Low=`26260.93`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26877.26` (Distance: `+0.00%`)
  * Point of Control (POC) = `26796.87` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26716.48` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26904.06` | POC=`26796.87` | VAL=`26689.68`
  * Prior Day Extremes: PDH=`26957.65` | PDL=`26636.09` | PDC=`26796.87`
  * Monday Range Blueprint: High=`26930.85` | Mid=`26796.87` | Low=`26662.89`
  * Developing Weekly Value Area: Weekly VAH=`27011.24` | Weekly POC=`26796.87` | Weekly VAL=`26582.50`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26850.46` | Low=`26743.28`
  * London Session (08:00-16:00 UTC): High=`26904.06` | Low=`26689.68`
  * New York Session (13:00-21:00 UTC): High=`26957.65` | Low=`26636.09`
  * Initial Balance (First Hour): IB High=`26877.26` | IB Low=`26716.48`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26689.68` - `26904.06`
  * Optimal Trade Entry (OTE 0.705): `26850.46`
  * Structural Invalidation Anchor (0.786): `27011.24`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,611,118.50 USD | `6,365.38` | `4188.90` | `4023.50` | `32860.85` | 1,052,852.79 USD | `+4.11%` | `4X Cross` |
| `52` | `0x4692...164f` | `SHORT` | 25,458,974.27 USD | `6,327.57` | `4132.69` | `4023.50` | `13803.39` | 690,960.04 USD | `+2.71%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,617,540.24 USD | `5,869.90` | `4228.86` | `4023.50` | `30640.37` | 1,205,481.70 USD | `+5.10%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,429,106.91 USD | `4,828.91` | `4157.43` | `4023.50` | `2235.38` | -646,775.40 USD | `-3.33%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,217,059.38 USD | `3,533.51` | `4129.10` | `4023.50` | `448.64` | -373,167.07 USD | `-2.62%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,149,655.81 USD | `3,268.21` | `4228.94` | `4023.50` | `4398.03` | 671,423.32 USD | `+5.11%` | `25X Cross` |
| `177` | `0xa742...e390` | `SHORT` | 11,668,150.40 USD | `2,900.00` | `4364.92` | `4023.50` | `4235.67` | 990,125.93 USD | `+8.49%` | `20X Cross` |
| `261` | `0xfc66...ca06` | `SHORT` | 8,851,927.73 USD | `2,200.06` | `4031.28` | `4023.50` | `10334.25` | 17,131.82 USD | `+0.19%` | `3X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,851,700.00 USD | `2,200.00` | `4176.09` | `4023.50` | `2685.37` | -335,719.30 USD | `-3.79%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,851,700.00 USD | `2,200.00` | `4112.20` | `4023.50` | `4331.15` | 195,154.59 USD | `+2.20%` | `20X Cross` |
| `295` | `0xacb6...efbd` | `SHORT` | 7,947,897.57 USD | `1,975.37` | `4048.55` | `4023.50` | `6508.45` | 49,494.14 USD | `+0.62%` | `6X Cross` |
| `365` | `0xc26c...b8f4` | `LONG` | 6,356,936.07 USD | `1,579.95` | `4075.62` | `4023.50` | `0.000000` | -82,360.90 USD | `-1.30%` | `1X Cross` |
| `400` | `0x12d2...f97f` | `LONG` | 5,640,716.86 USD | `1,401.94` | `4278.91` | `4023.50` | `3106.92` | -358,073.72 USD | `-6.35%` | `20X Cross` |
| `548` | `0x63da...8add` | `LONG` | 4,023,500.00 USD | `1,000.00` | `4021.46` | `4023.50` | `3564.11` | 2,039.04 USD | `+0.05%` | `25X Cross` |
| `561` | `0x354b...6425` | `LONG` | 3,950,923.30 USD | `981.96` | `4031.85` | `4023.50` | `0.000000` | -8,203.69 USD | `-0.21%` | `10X Cross` |
| `574` | `0x9aa5...58af` | `LONG` | 3,909,401.59 USD | `971.64` | `4279.98` | `4023.50` | `0.000000` | -249,207.50 USD | `-6.37%` | `20X Cross` |
| `598` | `0xf3dc...1672` | `LONG` | 3,744,847.28 USD | `930.74` | `4024.62` | `4023.50` | `3337.59` | -1,045.29 USD | `-0.03%` | `20X Cross` |
| `673` | `0x4a20...3c26` | `LONG` | 3,369,277.69 USD | `837.40` | `4599.73` | `4023.50` | `0.000000` | -482,542.69 USD | `-14.32%` | `20X Cross` |
| `814` | `0x0fac...7a0a` | `LONG` | 2,762,072.40 USD | `686.49` | `4290.34` | `4023.50` | `1508.96` | -183,186.31 USD | `-6.63%` | `25X Cross` |
| `867` | `0xd8c5...99b0` | `SHORT` | 2,584,514.94 USD | `642.35` | `4175.35` | `4023.50` | `32990.60` | 97,546.24 USD | `+3.77%` | `4X Cross` |
| `894` | `0x625e...a354` | `SHORT` | 2,494,570.00 USD | `620.00` | `4122.81` | `4023.50` | `4342.25` | 61,577.03 USD | `+2.47%` | `20X Cross` |
| `931` | `0xeae3...e8ad` | `SHORT` | 2,414,100.00 USD | `600.00` | `4104.77` | `4023.50` | `4325.27` | 48,765.11 USD | `+2.02%` | `20X Cross` |
| `932` | `0xf285...fa82` | `LONG` | 2,406,479.09 USD | `598.11` | `4146.45` | `4023.50` | `3891.24` | -73,540.46 USD | `-3.06%` | `25X Cross` |
| `952` | `0x12f7...8750` | `LONG` | 2,356,204.65 USD | `585.61` | `4082.77` | `4023.50` | `2553.27` | -34,712.33 USD | `-1.47%` | `10X Cross` |
| `1091` | `0x413c...886c` | `LONG` | 2,011,750.00 USD | `500.00` | `4010.43` | `4023.50` | `0.000000` | 6,533.77 USD | `+0.32%` | `2X Cross` |
| `1100` | `0x61ce...a62b` | `SHORT` | 2,001,705.33 USD | `497.50` | `4071.66` | `4023.50` | `4713.54` | 23,963.46 USD | `+1.20%` | `20X Cross` |
| `1104` | `0x0593...40f9` | `LONG` | 1,996,368.16 USD | `496.18` | `4024.57` | `4023.50` | `3701.73` | -535.67 USD | `-0.03%` | `10X Isolated` |
| `1224` | `0xead5...69f2` | `LONG` | 1,825,799.52 USD | `453.78` | `4220.88` | `4023.50` | `3538.94` | -89,568.54 USD | `-4.91%` | `5X Isolated` |
| `1313` | `0x46fc...1195` | `LONG` | 1,675,352.41 USD | `416.39` | `4054.56` | `4023.50` | `2179.03` | -12,933.58 USD | `-0.77%` | `20X Cross` |
| `1373` | `0x6d15...d374` | `LONG` | 1,609,400.00 USD | `400.00` | `4068.25` | `4023.50` | `3841.81` | -17,900.00 USD | `-1.11%` | `25X Cross` |
| `1374` | `0xee02...309d` | `SHORT` | 1,609,400.00 USD | `400.00` | `4438.84` | `4023.50` | `4226.89` | 166,138.60 USD | `+10.32%` | `25X Isolated` |
| `1408` | `0x02a7...fe9f` | `SHORT` | 1,569,165.00 USD | `390.00` | `4055.02` | `4023.50` | `4306.71` | 12,294.25 USD | `+0.78%` | `25X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,528,930.00 USD | `380.00` | `4131.92` | `4023.50` | `4293.51` | 41,199.64 USD | `+2.69%` | `20X Cross` |
| `1466` | `0x72c2...9b37` | `LONG` | 1,501,293.79 USD | `373.13` | `4000.98` | `4023.50` | `3778.05` | 8,400.27 USD | `+0.56%` | `13X Isolated` |
| `1508` | `0xaa44...b844` | `LONG` | 1,448,460.00 USD | `360.00` | `4043.10` | `4023.50` | `2803.27` | -7,057.63 USD | `-0.49%` | `4X Cross` |
| `1631` | `0xa41f...d50a` | `LONG` | 1,323,579.01 USD | `328.96` | `4468.89` | `4023.50` | `3833.19` | -146,518.84 USD | `-11.07%` | `15X Cross` |
| `1662` | `0xbf5a...88ba` | `SHORT` | 1,278,084.49 USD | `317.65` | `4091.80` | `4023.50` | `9900.41` | 21,698.54 USD | `+1.70%` | `20X Cross` |
| `1701` | `0xff31...ff6c` | `SHORT` | 1,247,285.00 USD | `310.00` | `4372.43` | `4023.50` | `4789.18` | 108,170.38 USD | `+8.67%` | `10X Isolated` |
| `1710` | `0xada6...6f88` | `LONG` | 1,239,641.56 USD | `308.10` | `4166.46` | `4023.50` | `1926.86` | -44,047.46 USD | `-3.55%` | `5X Cross` |
| `1876` | `0x50e2...d770` | `LONG` | 1,087,823.23 USD | `270.37` | `4243.58` | `4023.50` | `2562.10` | -59,503.23 USD | `-5.47%` | `20X Cross` |
| `1893` | `0x4c92...4f17` | `SHORT` | 1,073,149.93 USD | `266.72` | `4260.98` | `4023.50` | `6518.15` | 63,342.30 USD | `+5.90%` | `20X Cross` |
| `1949` | `0xd346...c4f3` | `LONG` | 1,026,691.78 USD | `255.17` | `4188.66` | `4023.50` | `3310.43` | -42,144.72 USD | `-4.10%` | `5X Isolated` |
| `1994` | `0x1581...463b` | `LONG` | 1,005,775.00 USD | `250.00` | `4003.77` | `4023.50` | `3556.56` | 4,831.41 USD | `+0.48%` | `15X Cross` |

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
| `1D` | `3614.70` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 7,480.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `3617.80` | 21,300,000.00 USD | 0.00 USD | 21,300,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.80` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 18,220.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 21,080.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.20` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3627.00` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 14,290.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.40` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3631.10` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 31,880.00 USD | 0.00 USD | 53,030.00 USD |
| `7D` | `3634.60` | 20,720,000.00 USD | 0.00 USD | 20,720,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.20` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 30,630.00 USD | 0.00 USD | 15,790.00 USD |
| `7D` | `3638.80` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.30` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.00` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.40` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3647.20` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3647.50` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 8,310.00 USD |
| `1D` | `3651.60` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 9,200.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.60` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,910,000.00 USD | 0.00 USD | 18,910,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.40` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3848.80` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.50` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 15,390.00 USD | 0.00 USD | 40,040.00 USD |
| `7D` | `3853.00` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.60` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 27,320.00 USD | 0.00 USD | 93,700.00 USD |
| `7D` | `3857.20` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.70` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 89,590.00 USD | 0.00 USD | 125,320.00 USD |
| `7D` | `3861.40` | 16,500,000.00 USD | 0.00 USD | 16,500,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.80` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 77,800.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `3865.60` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.90` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 50,420.00 USD | 0.00 USD | 58,620.00 USD |
| `7D` | `3869.80` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3873.00` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 84,010.00 USD | 0.00 USD | 156,630.00 USD |
| `7D` | `3874.00` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3877.10` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 77,180.00 USD | 0.00 USD | 43,100.00 USD |
| `7D` | `3878.20` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3881.20` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 25,200.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `3882.40` | 14,300,000.00 USD | 0.00 USD | 14,300,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3885.30` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3886.60` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.40` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 6,830.00 USD | 0.00 USD | 19,780.00 USD |
| `7D` | `3890.80` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.50` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 23,320.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3895.00` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.60` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,610,000.00 USD | 0.00 USD | 13,610,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.30` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 16,080.00 USD | 0.00 USD | 49,460.00 USD |
| `7D` | `3928.60` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.40` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 36,670.00 USD | 0.00 USD | 119,080.00 USD |
| `7D` | `3932.80` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.50` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 21,350.00 USD | 0.00 USD | 98,260.00 USD |
| `7D` | `3937.00` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.60` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 120,520.00 USD | 0.00 USD | 221,950.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.70` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 175,320.00 USD | 0.00 USD | 412,490.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.80` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 136,480.00 USD | 0.00 USD | 193,070.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 105,370.00 USD | 0.00 USD | 221,160.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3955.00` | 887,080.00 USD | 0.00 USD | 887,080.00 USD | 132,450.00 USD | 0.00 USD | 229,390.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3959.10` | 525,240.00 USD | 0.00 USD | 525,240.00 USD | 148,890.00 USD | 0.00 USD | 33,390.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.20` | 342,960.00 USD | 0.00 USD | 342,960.00 USD | 57,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.30` | 278,170.00 USD | 0.00 USD | 278,170.00 USD | 84,790.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.40` | 149,960.00 USD | 0.00 USD | 149,960.00 USD | 6,100.00 USD | 0.00 USD | 25,940.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.50` | 117,920.00 USD | 0.00 USD | 117,920.00 USD | 42,080.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.60` | 9,780.00 USD | 0.00 USD | 9,780.00 USD | 9,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `4021.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4022.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `1D` | `4086.20` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4090.30` | 200,730.00 USD | 200,730.00 USD | 0.00 USD | 40,090.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 216,890.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.40` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 26,730.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.60` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.50` | 607,650.00 USD | 607,650.00 USD | 0.00 USD | 89,310.00 USD | 0.00 USD | 203,990.00 USD |
| `7D` | `4100.80` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.60` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 156,170.00 USD | 0.00 USD | 289,480.00 USD |
| `7D` | `4105.00` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 455,740.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.70` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 176,490.00 USD | 0.00 USD | 330,980.00 USD |
| `7D` | `4109.20` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 350,460.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.80` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 68,280.00 USD | 0.00 USD | 105,010.00 USD |
| `7D` | `4113.40` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.90` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 166,130.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `4117.60` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4119.00` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 156,230.00 USD | 0.00 USD | 98,400.00 USD |
| `7D` | `4121.80` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.10` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 50,390.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `4126.00` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.20` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.20` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.30` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 16,920.00 USD | 0.00 USD | 37,130.00 USD |
| `7D` | `4134.40` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.40` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.60` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.50` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4168.00` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.20` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4172.20` | 16,810,000.00 USD | 16,810,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4172.30` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 11,230.00 USD | 0.00 USD | 69,710.00 USD |
| `1D` | `4176.40` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 11,440.00 USD | 0.00 USD | 66,320.00 USD |
| `7D` | `4176.40` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.50` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD | 82,550.00 USD |
| `7D` | `4180.60` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.60` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 84,590.00 USD | 0.00 USD | 201,080.00 USD |
| `7D` | `4184.80` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.70` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 57,210.00 USD | 0.00 USD | 85,290.00 USD |
| `7D` | `4189.00` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.80` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 50,440.00 USD | 0.00 USD | 104,640.00 USD |
| `7D` | `4193.20` | 19,090,000.00 USD | 19,090,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.90` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 109,340.00 USD |
| `7D` | `4197.40` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4201.00` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 80,870.00 USD | 0.00 USD | 21,140.00 USD |
| `7D` | `4201.60` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4205.10` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4209.20` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,990,000.00 USD | 19,990,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4213.30` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 6,830.00 USD | 0.00 USD | 9,730.00 USD |
| `7D` | `4214.20` | 20,080,000.00 USD | 20,080,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.40` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.50` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,980,000.00 USD | 20,980,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4410.10` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4414.20` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4415.80` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4418.30` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `4420.00` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.40` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `4424.20` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4424.70` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 10,800.00 USD | 0.00 USD | 11,440.00 USD |
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
  * Total Open Interest: `823.97M` | Total OI Tokens: `204,866.6 XAUT`
  * 1h OI Change: `-0.24%` | 4h OI Change: `-2.13%` | 24h OI Change: `+2.86%`
  * Exchange Breakdown: Binance=`61.69M` | Bybit=`142.83M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `53.96%` | `46.04%` | `1.17` | 3,170,000.00 USD |
| `15M` | `Binance` | `53.31%` | `46.69%` | `1.14` | 1,350,000.00 USD |
| `15M` | `OKX` | `60.82%` | `39.18%` | `1.55` | 413,520.00 USD |
| `15M` | `Bybit` | `57.83%` | `42.17%` | `1.37` | 337,940.00 USD |
| `15M` | `KuCoin` | `37.18%` | `62.82%` | `0.59` | 41,870.00 USD |
| `15M` | `Gate` | `22.78%` | `77.22%` | `0.30` | 148,230.00 USD |
| `15M` | `Bitget` | `47.52%` | `52.48%` | `0.91` | 77,830.00 USD |
| `15M` | `BingX` | `40.11%` | `59.89%` | `0.67` | 44,670.00 USD |
| `15M` | `MEXC` | `55.13%` | `44.87%` | `1.23` | 264,250.00 USD |
| `15M` | `Bitunix` | `51.52%` | `48.48%` | `1.06` | 34,680.00 USD |
| `15M` | `Hyperliquid` | `60.73%` | `39.27%` | `1.55` | 132,190.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.81%` | `51.19%` | `0.95` | 166,190.00 USD |
| `15M` | `Crypto.com` | `55.96%` | `44.04%` | `1.27` | 3,560.00 USD |
| `15M` | `WhiteBIT` | `84.37%` | `15.63%` | `5.40` | 124,970.00 USD |
| `15M` | `HTX` | `42.41%` | `57.59%` | `0.74` | 772.19 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `19.74%` | `80.26%` | `0.25` | 5,790.00 USD |
| `15M` | `Aster` | `26.85%` | `73.15%` | `0.37` | 501.10 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.68%` | `95.32%` | `0.05` | 13,960.00 USD |
| `15M` | `Whale Positions` | `53.31%` | `46.69%` | `1.14` | 1,350,000.00 USD |
| `15M` | `Global Accounts` | `53.96%` | `46.04%` | `1.17` | 3,170,000.00 USD |
| `1H` | `XAUT` | `48.91%` | `51.09%` | `0.96` | 7,200,000.00 USD |
| `1H` | `Binance` | `51.72%` | `48.28%` | `1.07` | 1,410,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `42.81%` | `57.19%` | `0.75` | 948,590.00 USD |
| `1H` | `KuCoin` | `21.69%` | `78.31%` | `0.28` | 73,340.00 USD |
| `1H` | `Gate` | `40.31%` | `59.69%` | `0.68` | 518,460.00 USD |
| `1H` | `Bitget` | `43.15%` | `56.85%` | `0.76` | 627,740.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `53.78%` | `46.22%` | `1.16` | 1,920,000.00 USD |
| `1H` | `Bitunix` | `50.3%` | `49.7%` | `1.01` | 649,350.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.87%` | `44.13%` | `1.27` | 853,810.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `24.75%` | `75.25%` | `0.33` | 193,290.00 USD |
| `1H` | `HTX` | `39.64%` | `60.36%` | `0.66` | 2,880.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `94.81%` | `5.19%` | `18.27` | 9,360.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `51.72%` | `48.28%` | `1.07` | 1,410,000.00 USD |
| `1H` | `Global Accounts` | `48.91%` | `51.09%` | `0.96` | 7,200,000.00 USD |
| `4H` | `XAUT` | `45.28%` | `54.72%` | `0.83` | 58,940,000.00 USD |
| `4H` | `Binance` | `53.49%` | `46.51%` | `1.15` | 6,510,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.45%` | `45.55%` | `1.20` | 5,710,000.00 USD |
| `4H` | `KuCoin` | `24.23%` | `75.77%` | `0.32` | 314,330.00 USD |
| `4H` | `Gate` | `50.05%` | `49.95%` | `1.00` | 2,730,000.00 USD |
| `4H` | `Bitget` | `55.27%` | `44.73%` | `1.24` | 2,010,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `39.99%` | `60.01%` | `0.67` | 32,300,000.00 USD |
| `4H` | `Bitunix` | `46.08%` | `53.92%` | `0.85` | 3,410,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.78%` | `41.22%` | `1.43` | 4,780,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.68%` | `81.32%` | `0.23` | 1,070,000.00 USD |
| `4H` | `HTX` | `36.54%` | `63.46%` | `0.58` | 12,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.09%` | `59.91%` | `0.67` | 95,380.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `53.49%` | `46.51%` | `1.15` | 6,510,000.00 USD |
| `4H` | `Global Accounts` | `45.28%` | `54.72%` | `0.83` | 58,940,000.00 USD |


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
| `5m` | -97,170.00 USD | -101,340.00 USD | **`DISTRIBUTION`** |
| `15m` | -152,480.00 USD | -50,810.00 USD | **`DISTRIBUTION`** |
| `30m` | -95,230.00 USD | -72,130.00 USD | **`DISTRIBUTION`** |
| `1h` | -458,650.00 USD | -182,040.00 USD | **`DISTRIBUTION`** |
| `2h` | 31,860.00 USD | 144,190.00 USD | **`ACCUMULATION`** |
| `4h` | -156,170.00 USD | 887,220.00 USD | **`ACCUMULATION`** |
| `6h` | -625,640.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | -643,530.00 USD | 1,550,000.00 USD | **`ACCUMULATION`** |
| `12h` | -125,240.00 USD | 1,110,000.00 USD | **`ACCUMULATION`** |
| `24h` | -531,550.00 USD | 1,280,000.00 USD | **`ACCUMULATION`** |
| `1w` | -80,090,000.00 USD | -19,960,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,860,000.00 USD | -83,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-97.17K` | 15m=`-152.48K` | 1h=`-458.65K` | 24h=`-531.55K`
* Futures Capital Netflows: 5m=`-101.34K` | 15m=`-50.81K` | 1h=`-182.04K` | 24h=`+1.28M`
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
  * Execution Entry: `26716.48` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26626.52` (Risk Distance: `89.96` pts)
  * +2.5R Take Profit: `26941.38`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.90 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26877.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26967.22` (Risk Distance: `89.96` pts)
  * +2.5R Take Profit: `26652.36`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.90 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`27011.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
