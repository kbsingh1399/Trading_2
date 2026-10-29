# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 03:28:19 IST` (`2026-10-29 21:58:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:25:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,582,474.28 USD | `6,365.38` | `4188.90` | `4019.00` | `32442.65` | 1,081,497.02 USD | `+4.23%` | `4X Cross` |
| `53` | `0x4692...164f` | `SHORT` | 25,404,084.53 USD | `6,321.00` | `4133.07` | `4019.00` | `13755.56` | 721,089.26 USD | `+2.84%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,591,125.69 USD | `5,869.90` | `4228.86` | `4019.00` | `30044.83` | 1,231,896.25 USD | `+5.22%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,407,859.72 USD | `4,828.91` | `4157.43` | `4019.00` | `2224.57` | -668,022.59 USD | `-3.44%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,199,211.00 USD | `3,533.02` | `4129.12` | `4019.00` | `419.56` | -389,066.30 USD | `-2.74%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,134,948.85 USD | `3,268.21` | `4228.94` | `4019.00` | `4397.76` | 686,130.28 USD | `+5.22%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,655,100.40 USD | `2,900.00` | `4364.92` | `4019.00` | `4235.67` | 1,003,175.93 USD | `+8.61%` | `20X Cross` |
| `263` | `0xfc66...ca06` | `SHORT` | 8,982,973.86 USD | `2,235.07` | `4031.28` | `4019.00` | `13931.18` | 27,238.78 USD | `+0.30%` | `3X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,841,800.00 USD | `2,200.00` | `4176.09` | `4019.00` | `2606.83` | -345,619.30 USD | `-3.91%` | `25X Cross` |
| `266` | `0x41e5...0825` | `SHORT` | 8,841,800.00 USD | `2,200.00` | `4112.20` | `4019.00` | `4331.15` | 205,054.59 USD | `+2.32%` | `20X Cross` |
| `300` | `0xacb6...efbd` | `SHORT` | 7,939,008.41 USD | `1,975.37` | `4048.55` | `4019.00` | `6500.93` | 58,383.30 USD | `+0.74%` | `6X Cross` |
| `374` | `0xc26c...b8f4` | `LONG` | 6,349,826.28 USD | `1,579.95` | `4075.62` | `4019.00` | `0.000000` | -89,470.69 USD | `-1.41%` | `1X Cross` |
| `404` | `0x12d2...f97f` | `LONG` | 5,634,408.11 USD | `1,401.94` | `4278.91` | `4019.00` | `3067.57` | -364,382.47 USD | `-6.47%` | `20X Cross` |
| `555` | `0x63da...8add` | `LONG` | 4,019,000.00 USD | `1,000.00` | `4021.46` | `4019.00` | `3564.11` | -2,460.96 USD | `-0.06%` | `25X Cross` |
| `569` | `0x354b...6425` | `LONG` | 3,969,710.18 USD | `987.74` | `4031.85` | `4019.00` | `0.000000` | -12,697.16 USD | `-0.32%` | `10X Cross` |
| `582` | `0x9aa5...58af` | `LONG` | 3,905,029.20 USD | `971.64` | `4279.98` | `4019.00` | `0.000000` | -253,579.89 USD | `-6.49%` | `20X Cross` |
| `610` | `0xf3dc...1672` | `LONG` | 3,740,752.00 USD | `930.74` | `4024.62` | `4019.00` | `3337.59` | -5,140.56 USD | `-0.14%` | `20X Cross` |
| `685` | `0x4a20...3c26` | `LONG` | 3,365,509.39 USD | `837.40` | `4599.73` | `4019.00` | `0.000000` | -486,310.99 USD | `-14.45%` | `20X Cross` |
| `833` | `0x0fac...7a0a` | `LONG` | 2,758,983.21 USD | `686.49` | `4290.34` | `4019.00` | `1433.27` | -186,275.49 USD | `-6.75%` | `25X Cross` |
| `880` | `0xd8c5...99b0` | `SHORT` | 2,581,624.34 USD | `642.35` | `4175.35` | `4019.00` | `32795.88` | 100,436.83 USD | `+3.89%` | `4X Cross` |
| `916` | `0x625e...a354` | `SHORT` | 2,491,842.00 USD | `620.00` | `4122.81` | `4019.00` | `4342.25` | 64,305.03 USD | `+2.58%` | `20X Cross` |
| `944` | `0xeae3...e8ad` | `SHORT` | 2,411,400.00 USD | `600.00` | `4104.77` | `4019.00` | `4325.27` | 51,465.11 USD | `+2.13%` | `20X Cross` |
| `947` | `0xf285...fa82` | `LONG` | 2,403,787.61 USD | `598.11` | `4146.45` | `4019.00` | `3891.24` | -76,231.94 USD | `-3.17%` | `25X Cross` |
| `966` | `0x12f7...8750` | `LONG` | 2,353,569.40 USD | `585.61` | `4082.77` | `4019.00` | `2516.38` | -37,347.58 USD | `-1.59%` | `10X Cross` |
| `1114` | `0x413c...886c` | `LONG` | 2,009,550.00 USD | `500.00` | `4010.43` | `4019.00` | `0.000000` | 4,333.77 USD | `+0.22%` | `2X Cross` |
| `1121` | `0x61ce...a62b` | `SHORT` | 1,999,466.57 USD | `497.50` | `4071.66` | `4019.00` | `4710.08` | 26,202.22 USD | `+1.31%` | `20X Cross` |
| `1124` | `0x0593...40f9` | `LONG` | 1,994,135.36 USD | `496.18` | `4024.57` | `4019.00` | `3701.73` | -2,768.47 USD | `-0.14%` | `10X Isolated` |
| `1249` | `0xead5...69f2` | `LONG` | 1,823,757.49 USD | `453.78` | `4220.88` | `4019.00` | `3538.94` | -91,610.56 USD | `-5.02%` | `5X Isolated` |
| `1361` | `0x46fc...1195` | `LONG` | 1,650,490.84 USD | `410.66` | `4055.10` | `4019.00` | `2129.51` | -14,785.65 USD | `-0.90%` | `20X Cross` |
| `1391` | `0x6d15...d374` | `LONG` | 1,607,640.00 USD | `400.00` | `4068.25` | `4019.00` | `3841.81` | -19,660.00 USD | `-1.22%` | `25X Cross` |
| `1392` | `0xee02...309d` | `SHORT` | 1,607,600.00 USD | `400.00` | `4438.84` | `4019.00` | `4226.89` | 167,938.60 USD | `+10.45%` | `25X Isolated` |
| `1434` | `0x02a7...fe9f` | `SHORT` | 1,567,410.00 USD | `390.00` | `4055.02` | `4019.00` | `4306.71` | 14,049.25 USD | `+0.90%` | `25X Cross` |
| `1470` | `0x7e77...b8d2` | `SHORT` | 1,527,220.00 USD | `380.00` | `4131.92` | `4019.00` | `4293.51` | 42,909.64 USD | `+2.81%` | `20X Cross` |
| `1490` | `0x72c2...9b37` | `LONG` | 1,499,614.69 USD | `373.13` | `4000.98` | `4019.00` | `3778.04` | 6,721.18 USD | `+0.45%` | `13X Isolated` |
| `1542` | `0xaa44...b844` | `LONG` | 1,446,876.00 USD | `360.00` | `4043.10` | `4019.00` | `2803.26` | -8,641.63 USD | `-0.60%` | `4X Cross` |
| `1650` | `0xa41f...d50a` | `LONG` | 1,322,098.68 USD | `328.96` | `4468.89` | `4019.00` | `3833.19` | -147,999.17 USD | `-11.19%` | `15X Cross` |
| `1669` | `0x49e9...e1d0` | `SHORT` | 1,300,062.90 USD | `323.48` | `4025.23` | `4019.00` | `32369.09` | 2,015.42 USD | `+0.16%` | `4X Cross` |
| `1681` | `0xada6...6f88` | `LONG` | 1,283,168.64 USD | `319.28` | `4166.46` | `4019.00` | `1972.27` | -47,081.87 USD | `-3.67%` | `5X Cross` |
| `1685` | `0xbf5a...88ba` | `SHORT` | 1,276,655.04 USD | `317.65` | `4091.80` | `4019.00` | `9941.58` | 23,127.99 USD | `+1.81%` | `20X Cross` |
| `1721` | `0xff31...ff6c` | `SHORT` | 1,245,890.00 USD | `310.00` | `4372.43` | `4019.00` | `4789.18` | 109,565.38 USD | `+8.79%` | `10X Isolated` |
| `1888` | `0x50e2...d770` | `LONG` | 1,086,606.58 USD | `270.37` | `4243.58` | `4019.00` | `2562.10` | -60,719.88 USD | `-5.59%` | `20X Cross` |
| `1903` | `0x4c92...4f17` | `SHORT` | 1,071,949.69 USD | `266.72` | `4260.98` | `4019.00` | `6519.71` | 64,542.55 USD | `+6.02%` | `20X Cross` |
| `1968` | `0xd346...c4f3` | `LONG` | 1,025,543.50 USD | `255.17` | `4188.66` | `4019.00` | `3310.42` | -43,293.01 USD | `-4.22%` | `5X Isolated` |
| `2010` | `0x1581...463b` | `LONG` | 1,004,775.00 USD | `250.00` | `4003.77` | `4019.00` | `3547.37` | 3,831.41 USD | `+0.38%` | `15X Cross` |

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
| `7D` | `3605.20` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 33,130.00 USD | 0.00 USD | 98,140.00 USD |
| `7D` | `3609.40` | 21,570,000.00 USD | 0.00 USD | 21,570,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `7D` | `3613.60` | 21,520,000.00 USD | 0.00 USD | 21,520,000.00 USD | 76,290.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3615.30` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 8,720.00 USD | 0.00 USD | 27,180.00 USD |
| `7D` | `3617.80` | 21,370,000.00 USD | 0.00 USD | 21,370,000.00 USD | 45,810.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3619.50` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 20,890.00 USD | 0.00 USD | 39,740.00 USD |
| `7D` | `3622.00` | 21,230,000.00 USD | 0.00 USD | 21,230,000.00 USD | 72,670.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3623.70` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 22,000.00 USD | 0.00 USD | 60,960.00 USD |
| `7D` | `3626.20` | 21,010,000.00 USD | 0.00 USD | 21,010,000.00 USD | 50,450.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3627.90` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 14,690.00 USD | 0.00 USD | 20,720.00 USD |
| `7D` | `3630.40` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3632.10` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 28,830.00 USD | 0.00 USD | 57,040.00 USD |
| `7D` | `3634.60` | 20,790,000.00 USD | 0.00 USD | 20,790,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3636.30` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 31,320.00 USD | 0.00 USD | 4,870.00 USD |
| `7D` | `3638.80` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3640.50` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 12,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.00` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3644.70` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 11,040.00 USD | 0.00 USD | 12,850.00 USD |
| `7D` | `3647.20` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3648.90` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 5,830.00 USD | 0.00 USD | 13,090.00 USD |
| `1D` | `3653.10` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 5,880.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.60` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3657.30` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 1,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3659.80` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,490,000.00 USD | 0.00 USD | 20,490,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,830,000.00 USD | 0.00 USD | 19,830,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,970,000.00 USD | 0.00 USD | 18,970,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3846.30` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 8,040.00 USD | 0.00 USD | 24,730.00 USD |
| `7D` | `3848.80` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3850.50` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 18,330.00 USD | 0.00 USD | 59,540.00 USD |
| `7D` | `3853.00` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 158,100.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3854.70` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 10,670.00 USD | 0.00 USD | 72,900.00 USD |
| `7D` | `3857.20` | 17,070,000.00 USD | 0.00 USD | 17,070,000.00 USD | 214,090.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3858.90` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 61,500.00 USD | 0.00 USD | 95,370.00 USD |
| `7D` | `3861.40` | 16,540,000.00 USD | 0.00 USD | 16,540,000.00 USD | 216,400.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3863.10` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 84,590.00 USD | 0.00 USD | 218,110.00 USD |
| `7D` | `3865.60` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 144,640.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3867.30` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 59,590.00 USD | 0.00 USD | 90,980.00 USD |
| `7D` | `3869.80` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3871.50` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 82,830.00 USD | 0.00 USD | 144,120.00 USD |
| `7D` | `3874.00` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3875.70` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 84,300.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `3878.20` | 14,570,000.00 USD | 0.00 USD | 14,570,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3879.90` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 38,130.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `3882.40` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3884.10` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3886.60` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3888.30` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 18,090.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `3890.80` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3892.50` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 17,230.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `3895.00` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3896.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 14,710.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3900.90` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 4,320.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `3903.40` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,330,000.00 USD | 0.00 USD | 12,330,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.10` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.30` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 52,750.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `3932.80` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.50` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 21,350.00 USD | 0.00 USD | 106,170.00 USD |
| `7D` | `3937.00` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.70` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 96,390.00 USD | 0.00 USD | 193,600.00 USD |
| `7D` | `3941.20` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 410,360.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.90` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 168,770.00 USD | 0.00 USD | 429,290.00 USD |
| `7D` | `3945.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 290,700.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3947.10` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 137,820.00 USD | 0.00 USD | 206,770.00 USD |
| `7D` | `3949.60` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3951.30` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 110,730.00 USD | 0.00 USD | 230,270.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3955.50` | 883,700.00 USD | 0.00 USD | 883,700.00 USD | 155,660.00 USD | 0.00 USD | 199,600.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3959.70` | 528,440.00 USD | 0.00 USD | 528,440.00 USD | 133,860.00 USD | 0.00 USD | 23,580.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.90` | 371,000.00 USD | 0.00 USD | 371,000.00 USD | 67,780.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3968.10` | 296,190.00 USD | 0.00 USD | 296,190.00 USD | 58,270.00 USD | 0.00 USD | 64,250.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3972.30` | 173,670.00 USD | 0.00 USD | 173,670.00 USD | 21,230.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3976.50` | 87,000.00 USD | 0.00 USD | 87,000.00 USD | 47,770.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3980.70` | 11,850.00 USD | 0.00 USD | 11,850.00 USD | 8,640.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `4015.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4016.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4089.90` | 196,680.00 USD | 196,680.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `4092.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 216,890.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.10` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.60` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.30` | 561,140.00 USD | 561,140.00 USD | 0.00 USD | 71,150.00 USD | 0.00 USD | 175,640.00 USD |
| `7D` | `4100.80` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.50` | 984,950.00 USD | 984,950.00 USD | 0.00 USD | 140,490.00 USD | 0.00 USD | 283,320.00 USD |
| `7D` | `4105.00` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 455,740.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.70` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `4109.20` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 350,460.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.90` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 68,280.00 USD | 0.00 USD | 110,410.00 USD |
| `7D` | `4113.40` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4115.10` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 168,010.00 USD | 0.00 USD | 307,850.00 USD |
| `7D` | `4117.60` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4119.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 154,350.00 USD | 0.00 USD | 86,190.00 USD |
| `7D` | `4121.80` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.50` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 50,390.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `4126.00` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.70` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `4130.20` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.90` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 22,050.00 USD | 0.00 USD | 39,020.00 USD |
| `7D` | `4134.40` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4136.10` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 46,630.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.60` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4140.30` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 17,240.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4144.50` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 8,640.00 USD | 0.00 USD | 3,200.00 USD |
| `7D` | `4147.00` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,940,000.00 USD | 14,940,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,250,000.00 USD | 16,250,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4168.00` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4169.70` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `4172.20` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4173.90` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `4176.40` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4178.10` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 24,170.00 USD | 0.00 USD | 83,730.00 USD |
| `7D` | `4180.60` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 168,040.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4182.30` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 75,810.00 USD | 0.00 USD | 117,710.00 USD |
| `7D` | `4184.80` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 246,800.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4186.50` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 77,800.00 USD | 0.00 USD | 186,800.00 USD |
| `7D` | `4189.00` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 140,280.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4190.70` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 43,350.00 USD | 0.00 USD | 59,260.00 USD |
| `7D` | `4193.20` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4194.90` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 76,790.00 USD | 0.00 USD | 134,500.00 USD |
| `7D` | `4197.40` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4199.10` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 81,580.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `4201.60` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4203.30` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 35,070.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `4205.80` | 19,900,000.00 USD | 19,900,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4207.50` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 38,160.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `4210.00` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4211.70` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 15,530.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `4214.20` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4215.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 13,550.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `4218.40` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4220.10` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 20,950.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4224.30` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 1,600.00 USD |
| `7D` | `4226.80` | 20,350,000.00 USD | 20,350,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,770,000.00 USD | 20,770,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 21,040,000.00 USD | 21,040,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,290,000.00 USD | 21,290,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.10` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 23,310.00 USD |
| `7D` | `4411.60` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4413.30` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,110.00 USD | 0.00 USD | 16,680.00 USD |
| `7D` | `4415.80` | 21,440,000.00 USD | 21,440,000.00 USD | 0.00 USD | 67,100.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4417.50` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 4,120.00 USD | 0.00 USD | 17,310.00 USD |
| `7D` | `4420.00` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 48,480.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4421.70` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 16,680.00 USD | 0.00 USD | 23,630.00 USD |
| `7D` | `4424.20` | 21,710,000.00 USD | 21,710,000.00 USD | 0.00 USD | 44,690.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4425.90` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 13,690.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `4428.40` | 21,880,000.00 USD | 21,880,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `4430.10` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 20,640.00 USD | 0.00 USD | 27,280.00 USD |
| `7D` | `4432.60` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `4433.10` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 6,460.00 USD | 0.00 USD | 6,960.00 USD |
| `7D` | `4436.80` | 22,050,000.00 USD | 22,050,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4439.40` | 22,150,000.00 USD | 22,150,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `826.04M` | Total OI Tokens: `205,608.1 XAUT`
  * 1h OI Change: `+0.12%` | 4h OI Change: `-1.80%` | 24h OI Change: `-0.33%`
  * Exchange Breakdown: Binance=`61.67M` | Bybit=`143.00M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `47.49%` | `52.51%` | `0.90` | 7,470,000.00 USD |
| `15M` | `Binance` | `45.23%` | `54.77%` | `0.83` | 2,430,000.00 USD |
| `15M` | `OKX` | `49.02%` | `50.98%` | `0.96` | 1,240,000.00 USD |
| `15M` | `Bybit` | `53.18%` | `46.82%` | `1.14` | 1,620,000.00 USD |
| `15M` | `KuCoin` | `46.2%` | `53.8%` | `0.86` | 39,440.00 USD |
| `15M` | `Gate` | `43.34%` | `56.66%` | `0.76` | 289,980.00 USD |
| `15M` | `Bitget` | `28.65%` | `71.35%` | `0.40` | 274,420.00 USD |
| `15M` | `BingX` | `57.11%` | `42.89%` | `1.33` | 174,820.00 USD |
| `15M` | `MEXC` | `31.37%` | `68.63%` | `0.46` | 442,280.00 USD |
| `15M` | `Bitunix` | `44.98%` | `55.02%` | `0.82` | 131,120.00 USD |
| `15M` | `Hyperliquid` | `50.16%` | `49.84%` | `1.01` | 288,910.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.42%` | `50.58%` | `0.98` | 275,290.00 USD |
| `15M` | `Crypto.com` | `82.35%` | `17.65%` | `4.67` | 1,640.00 USD |
| `15M` | `WhiteBIT` | `87.63%` | `12.37%` | `7.08` | 164,710.00 USD |
| `15M` | `HTX` | `30.17%` | `69.83%` | `0.43` | 1,020.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.73%` | `52.27%` | `0.91` | 19,550.00 USD |
| `15M` | `Aster` | `88.26%` | `11.74%` | `7.52` | 3,180.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.82%` | `76.18%` | `0.31` | 65,110.00 USD |
| `15M` | `Whale Positions` | `45.23%` | `54.77%` | `0.83` | 2,430,000.00 USD |
| `15M` | `Global Accounts` | `47.49%` | `52.51%` | `0.90` | 7,470,000.00 USD |
| `1H` | `XAUT` | `53.08%` | `46.92%` | `1.13` | 43,850,000.00 USD |
| `1H` | `Binance` | `51.49%` | `48.51%` | `1.06` | 18,220,000.00 USD |
| `1H` | `OKX` | `60.51%` | `39.49%` | `1.53` | 6,630,000.00 USD |
| `1H` | `Bybit` | `48.9%` | `51.1%` | `0.96` | 7,500,000.00 USD |
| `1H` | `KuCoin` | `53.1%` | `46.9%` | `1.13` | 289,890.00 USD |
| `1H` | `Gate` | `57.72%` | `42.28%` | `1.37` | 1,220,000.00 USD |
| `1H` | `Bitget` | `52.44%` | `47.56%` | `1.10` | 1,550,000.00 USD |
| `1H` | `BingX` | `47.31%` | `52.69%` | `0.90` | 775,540.00 USD |
| `1H` | `MEXC` | `52.72%` | `47.28%` | `1.12` | 2,310,000.00 USD |
| `1H` | `Bitunix` | `50.91%` | `49.09%` | `1.04` | 650,500.00 USD |
| `1H` | `Hyperliquid` | `58.82%` | `41.18%` | `1.43` | 1,480,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 2,370,000.00 USD |
| `1H` | `Crypto.com` | `51.53%` | `48.47%` | `1.06` | 15,180.00 USD |
| `1H` | `WhiteBIT` | `81.15%` | `18.85%` | `4.31` | 452,160.00 USD |
| `1H` | `HTX` | `55.52%` | `44.48%` | `1.25` | 9,100.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.15%` | `56.85%` | `0.76` | 165,790.00 USD |
| `1H` | `Aster` | `63.9%` | `36.1%` | `1.77` | 99,240.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.28%` | `52.72%` | `0.90` | 126,480.00 USD |
| `1H` | `Whale Positions` | `51.49%` | `48.51%` | `1.06` | 18,220,000.00 USD |
| `1H` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 43,850,000.00 USD |
| `4H` | `XAUT` | `47.15%` | `52.85%` | `0.89` | 61,520,000.00 USD |
| `4H` | `Binance` | `56.28%` | `43.72%` | `1.29` | 6,220,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `54.93%` | `45.07%` | `1.22` | 6,260,000.00 USD |
| `4H` | `KuCoin` | `23.98%` | `76.02%` | `0.32` | 276,730.00 USD |
| `4H` | `Gate` | `52.67%` | `47.33%` | `1.11` | 2,640,000.00 USD |
| `4H` | `Bitget` | `58.2%` | `41.8%` | `1.39` | 1,770,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `42.21%` | `57.79%` | `0.73` | 34,850,000.00 USD |
| `4H` | `Bitunix` | `53.45%` | `46.55%` | `1.15` | 3,460,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.59%` | `42.41%` | `1.36` | 4,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `15.04%` | `84.96%` | `0.18` | 1,020,000.00 USD |
| `4H` | `HTX` | `34.99%` | `65.01%` | `0.54` | 10,840.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.59%` | `57.41%` | `0.74` | 134,010.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `56.28%` | `43.72%` | `1.29` | 6,220,000.00 USD |
| `4H` | `Global Accounts` | `47.15%` | `52.85%` | `0.89` | 61,520,000.00 USD |


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
| `5m` | -429,950.00 USD | -50,850.00 USD | **`DISTRIBUTION`** |
| `15m` | -425,780.00 USD | -86,880.00 USD | **`DISTRIBUTION`** |
| `30m` | -329,830.00 USD | 227,860.00 USD | **`DISTRIBUTION`** |
| `1h` | 205,020.00 USD | 629,870.00 USD | **`ACCUMULATION`** |
| `2h` | -227,360.00 USD | 659,290.00 USD | **`ACCUMULATION`** |
| `4h` | -538,800.00 USD | 1,460,000.00 USD | **`ACCUMULATION`** |
| `6h` | -585,200.00 USD | 1,030,000.00 USD | **`ACCUMULATION`** |
| `8h` | -845,220.00 USD | 1,240,000.00 USD | **`ACCUMULATION`** |
| `12h` | 234,560.00 USD | 1,100,000.00 USD | **`ACCUMULATION`** |
| `24h` | -588,690.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `1w` | -80,310,000.00 USD | -19,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,710,000.00 USD | -84,180,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-429.95K` | 15m=`-425.78K` | 1h=`+205.02K` | 24h=`-588.69K`
* Futures Capital Netflows: 5m=`-50.85K` | 15m=`-86.88K` | 1h=`+629.87K` | 24h=`+1.01M`
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
  * `2026-10-30 02:54:14 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:21:14 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:20:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:14 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
