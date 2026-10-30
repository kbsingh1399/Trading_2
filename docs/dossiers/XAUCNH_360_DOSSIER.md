# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 10:22:41 IST` (`2026-10-30 04:52:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26559.96` | **Live Ask Quote**: `26562.20` | **Mid Price**: `26561.08`
- **Spread Points**: `224.00` | **Spread BPS**: `0.84 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26561.08` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.40` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26747.01` | Lower -3.00σ Band: `26375.15`
  * Upper +2.51σ Band: `26707.17` | Lower -2.51σ Band: `26414.99`
  * Upper +2.01σ Band: `26672.64` | Lower -2.01σ Band: `26449.52`
  * Upper +2.00σ Band: `26667.32` | Lower -2.00σ Band: `26454.84`
  * Upper +1.28σ Band: `26635.45` | Lower -1.28σ Band: `26486.71`
  * Upper +1.00σ Band: `26614.20` | Lower -1.00σ Band: `26507.96`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26561.08` | EMA-20=`26561.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26561.08` (Slope: `+0.0000`) | EMA-100=`26561.08`
  * Institutional Anchors: EMA-144=`26561.08` | EMA-200=`26561.08` (Slope: `+0.0000`) | EMA-233=`26561.08`
- **Range Boundaries**: 24H High=`26826.69` | 24H Low=`26295.47` | Weekly High=`27092.30` | Weekly Low=`26029.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26640.76` (Distance: `+0.00%`)
  * Point of Control (POC) = `26561.08` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26481.40` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26667.32` | POC=`26561.08` | VAL=`26454.84`
  * Prior Day Extremes: PDH=`26720.45` | PDL=`26401.71` | PDC=`26561.08`
  * Monday Range Blueprint: High=`26693.89` | Mid=`26561.08` | Low=`26428.27`
  * Developing Weekly Value Area: Weekly VAH=`26773.57` | Weekly POC=`26561.08` | Weekly VAL=`26348.59`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26614.20` | Low=`26507.96`
  * London Session (08:00-16:00 UTC): High=`26667.32` | Low=`26454.84`
  * New York Session (13:00-21:00 UTC): High=`26720.45` | Low=`26401.71`
  * Initial Balance (First Hour): IB High=`26640.76` | IB Low=`26481.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26454.84` - `26667.32`
  * Optimal Trade Entry (OTE 0.705): `26614.20`
  * Structural Invalidation Anchor (0.786): `26773.57`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,924,250.95 USD | `6,489.82` | `4185.46` | `3994.60` | `29525.77` | 1,238,700.06 USD | `+4.78%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,196,754.40 USD | `6,307.70` | `4129.22` | `3994.60` | `13924.66` | 849,149.51 USD | `+3.37%` | `5X Cross` |
| `66` | `0xb83d...6e36` | `SHORT` | 23,442,617.23 USD | `5,869.90` | `4228.86` | `3994.60` | `27207.63` | 1,380,404.70 USD | `+5.89%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,283,756.81 USD | `4,828.91` | `4157.43` | `3994.60` | `2275.83` | -792,125.50 USD | `-4.11%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,177,089.86 USD | `3,549.06` | `4127.91` | `3994.60` | `575.47` | -473,145.04 USD | `-3.34%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,055,204.45 USD | `3,268.21` | `4228.94` | `3994.60` | `4393.72` | 765,874.68 USD | `+5.87%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,584,340.40 USD | `2,900.00` | `4364.92` | `3994.60` | `4235.87` | 1,073,935.93 USD | `+9.27%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,788,120.00 USD | `2,200.00` | `4176.09` | `3994.60` | `2648.86` | -399,299.30 USD | `-4.54%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,786,140.00 USD | `2,200.00` | `4112.20` | `3994.60` | `4331.35` | 260,714.59 USD | `+2.97%` | `20X Cross` |
| `301` | `0xacb6...efbd` | `SHORT` | 7,889,031.57 USD | `1,975.37` | `4048.55` | `3994.60` | `6597.76` | 108,360.14 USD | `+1.37%` | `6X Cross` |
| `368` | `0xc26c...b8f4` | `LONG` | 6,311,275.46 USD | `1,579.95` | `4075.62` | `3994.60` | `0.000000` | -128,021.51 USD | `-2.03%` | `1X Cross` |
| `560` | `0x63da...8add` | `LONG` | 3,994,600.00 USD | `1,000.00` | `4021.46` | `3994.60` | `3564.32` | -26,860.96 USD | `-0.67%` | `25X Cross` |
| `572` | `0xf3dc...1672` | `LONG` | 3,930,881.89 USD | `984.27` | `4018.39` | `3994.60` | `2902.06` | -24,304.80 USD | `-0.62%` | `20X Cross` |
| `584` | `0x9aa5...58af` | `LONG` | 3,881,321.13 USD | `971.64` | `4279.98` | `3994.60` | `0.000000` | -277,287.95 USD | `-7.14%` | `20X Cross` |
| `590` | `0x354b...6425` | `LONG` | 3,850,239.55 USD | `963.86` | `4004.93` | `3994.60` | `0.000000` | -9,961.41 USD | `-0.26%` | `10X Cross` |
| `676` | `0x4a20...3c26` | `LONG` | 3,345,076.84 USD | `837.40` | `4599.73` | `3994.60` | `0.000000` | -506,743.54 USD | `-15.15%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,742,232.98 USD | `686.49` | `4290.34` | `3994.60` | `1274.35` | -203,025.72 USD | `-7.40%` | `25X Cross` |
| `914` | `0x625e...a354` | `SHORT` | 2,476,094.00 USD | `620.00` | `4122.81` | `3994.60` | `4342.45` | 80,053.03 USD | `+3.23%` | `20X Cross` |
| `919` | `0xd8c5...99b0` | `SHORT` | 2,470,080.48 USD | `618.35` | `4175.35` | `3994.60` | `34172.83` | 111,772.12 USD | `+4.53%` | `4X Cross` |
| `940` | `0xeae3...e8ad` | `SHORT` | 2,396,760.00 USD | `600.00` | `4104.77` | `3994.60` | `4325.47` | 66,105.11 USD | `+2.76%` | `20X Cross` |
| `943` | `0xf285...fa82` | `LONG` | 2,389,193.83 USD | `598.11` | `4146.45` | `3994.60` | `3891.45` | -90,825.72 USD | `-3.80%` | `25X Cross` |
| `959` | `0x12f7...8750` | `LONG` | 2,339,280.50 USD | `585.61` | `4082.77` | `3994.60` | `2633.79` | -51,636.48 USD | `-2.21%` | `10X Cross` |
| `1100` | `0x413c...886c` | `LONG` | 1,997,300.00 USD | `500.00` | `4010.43` | `3994.60` | `0.000000` | -7,916.23 USD | `-0.40%` | `2X Cross` |
| `1103` | `0x9c06...0560` | `LONG` | 1,990,977.75 USD | `498.42` | `4012.76` | `3994.60` | `0.000000` | -9,053.75 USD | `-0.45%` | `25X Cross` |
| `1107` | `0x61ce...a62b` | `SHORT` | 1,987,327.48 USD | `497.50` | `4071.66` | `3994.60` | `4718.36` | 38,341.31 USD | `+1.93%` | `20X Cross` |
| `1222` | `0xead5...69f2` | `LONG` | 1,812,276.76 USD | `453.78` | `4220.88` | `3994.60` | `3539.15` | -103,091.30 USD | `-5.69%` | `5X Isolated` |
| `1290` | `0x46fc...1195` | `LONG` | 1,693,515.86 USD | `423.95` | `4053.27` | `3994.60` | `2158.73` | -24,874.21 USD | `-1.47%` | `20X Cross` |
| `1362` | `0xee02...309d` | `SHORT` | 1,597,840.00 USD | `400.00` | `4438.84` | `3994.60` | `4227.09` | 177,698.60 USD | `+11.12%` | `25X Isolated` |
| `1363` | `0x6d15...d374` | `LONG` | 1,597,480.00 USD | `400.00` | `4068.25` | `3994.60` | `3842.02` | -29,820.00 USD | `-1.87%` | `25X Cross` |
| `1409` | `0x02a7...fe9f` | `SHORT` | 1,557,894.00 USD | `390.00` | `4055.02` | `3994.60` | `4306.91` | 23,565.25 USD | `+1.51%` | `25X Cross` |
| `1448` | `0x7e77...b8d2` | `SHORT` | 1,517,948.00 USD | `380.00` | `4131.92` | `3994.60` | `4293.71` | 52,181.64 USD | `+3.44%` | `20X Cross` |
| `1466` | `0x72c2...9b37` | `LONG` | 1,490,510.29 USD | `373.13` | `4000.98` | `3994.60` | `3778.25` | -2,383.22 USD | `-0.16%` | `13X Isolated` |
| `1512` | `0xaa44...b844` | `LONG` | 1,438,056.00 USD | `360.00` | `4043.10` | `3994.60` | `2818.36` | -17,461.63 USD | `-1.21%` | `4X Cross` |
| `1619` | `0xa41f...d50a` | `LONG` | 1,313,775.94 USD | `328.96` | `4468.89` | `3994.60` | `3802.38` | -156,321.91 USD | `-11.90%` | `15X Cross` |
| `1632` | `0x7fda...17d1` | `SHORT` | 1,301,729.49 USD | `325.87` | `4013.13` | `3994.60` | `30407.47` | 6,038.82 USD | `+0.46%` | `20X Cross` |
| `1666` | `0xbf5a...88ba` | `SHORT` | 1,268,904.26 USD | `317.65` | `4091.80` | `3994.60` | `9824.22` | 30,878.77 USD | `+2.43%` | `20X Cross` |
| `1702` | `0xff31...ff6c` | `SHORT` | 1,238,047.00 USD | `310.00` | `4372.43` | `3994.60` | `4789.38` | 117,408.38 USD | `+9.48%` | `10X Isolated` |
| `1729` | `0xada6...6f88` | `LONG` | 1,212,079.16 USD | `303.50` | `4166.46` | `3994.60` | `1784.39` | -52,433.70 USD | `-4.33%` | `5X Cross` |
| `1894` | `0x50e2...d770` | `LONG` | 1,080,009.62 USD | `270.37` | `4243.58` | `3994.60` | `2562.31` | -67,316.84 USD | `-6.23%` | `20X Cross` |
| `1912` | `0x4c92...4f17` | `SHORT` | 1,065,441.71 USD | `266.72` | `4260.98` | `3994.60` | `6509.84` | 71,050.53 USD | `+6.67%` | `20X Cross` |
| `1985` | `0xd346...c4f3` | `LONG` | 1,019,317.26 USD | `255.17` | `4188.66` | `3994.60` | `3310.63` | -49,519.25 USD | `-4.86%` | `5X Isolated` |

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
| `7D` | `3589.40` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3592.20` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 20,370.00 USD | 0.00 USD | 9,080.00 USD |
| `7D` | `3593.70` | 22,440,000.00 USD | 0.00 USD | 22,440,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3596.30` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 11,720.00 USD | 0.00 USD | 27,080.00 USD |
| `7D` | `3598.00` | 22,190,000.00 USD | 0.00 USD | 22,190,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3600.40` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 22,930.00 USD |
| `7D` | `3602.30` | 21,770,000.00 USD | 0.00 USD | 21,770,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3604.50` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 3,310.00 USD | 0.00 USD | 29,770.00 USD |
| `7D` | `3606.60` | 21,560,000.00 USD | 0.00 USD | 21,560,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3608.60` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 22,180.00 USD | 0.00 USD | 56,790.00 USD |
| `7D` | `3610.90` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.70` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 13,690.00 USD | 0.00 USD | 26,910.00 USD |
| `7D` | `3615.20` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.80` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 10,800.00 USD | 0.00 USD | 28,070.00 USD |
| `7D` | `3619.50` | 21,240,000.00 USD | 0.00 USD | 21,240,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.90` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 23,690.00 USD | 0.00 USD | 70,060.00 USD |
| `7D` | `3623.80` | 21,130,000.00 USD | 0.00 USD | 21,130,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3625.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 20,640.00 USD | 0.00 USD | 37,880.00 USD |
| `7D` | `3628.10` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 47,240.00 USD | 0.00 USD | 46,890.00 USD |
| `1D` | `3629.10` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 6,460.00 USD | 0.00 USD | 18,870.00 USD |
| `7D` | `3632.40` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3633.20` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 2,460.00 USD | 0.00 USD | 8,120.00 USD |
| `7D` | `3636.70` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3637.30` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 2,020.00 USD | 0.00 USD | 1,490.00 USD |
| `7D` | `3641.00` | 20,670,000.00 USD | 0.00 USD | 20,670,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,540,000.00 USD | 0.00 USD | 20,540,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `1D` | `3830.00` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 9,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.20` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3834.10` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 80,990.00 USD | 0.00 USD | 47,190.00 USD |
| `7D` | `3834.50` | 19,980,000.00 USD | 0.00 USD | 19,980,000.00 USD | 284,990.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3838.20` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 32,520.00 USD | 0.00 USD | 98,220.00 USD |
| `7D` | `3838.80` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 311,710.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3842.30` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 10,530.00 USD | 0.00 USD | 93,880.00 USD |
| `7D` | `3843.10` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 280,670.00 USD | 0.00 USD | 340,870.00 USD |
| `1D` | `3846.40` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 49,580.00 USD | 0.00 USD | 167,380.00 USD |
| `7D` | `3847.40` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 115,590.00 USD | 0.00 USD | 348,900.00 USD |
| `1D` | `3850.50` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 79,400.00 USD | 0.00 USD | 105,390.00 USD |
| `7D` | `3851.70` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3854.60` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 16,990.00 USD | 0.00 USD | 108,750.00 USD |
| `7D` | `3856.00` | 16,560,000.00 USD | 0.00 USD | 16,560,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3858.70` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 74,330.00 USD | 0.00 USD | 112,190.00 USD |
| `7D` | `3860.30` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3862.80` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 88,650.00 USD | 0.00 USD | 203,230.00 USD |
| `7D` | `3864.60` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3866.90` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 57,210.00 USD | 0.00 USD | 108,000.00 USD |
| `7D` | `3868.90` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 192,180.00 USD | 0.00 USD | 245,420.00 USD |
| `1D` | `3871.00` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 20,190.00 USD | 0.00 USD | 72,010.00 USD |
| `7D` | `3873.20` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `1D` | `3875.10` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 10,940.00 USD | 0.00 USD | 20,300.00 USD |
| `7D` | `3877.50` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `1D` | `3879.20` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 6,870.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `3881.80` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.90` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3912.00` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 145,610.00 USD | 0.00 USD | 63,400.00 USD |
| `1D` | `3916.10` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 93,170.00 USD | 0.00 USD | 174,960.00 USD |
| `7D` | `3916.20` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 712,000.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3920.20` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 11,650.00 USD | 0.00 USD | 121,880.00 USD |
| `7D` | `3920.50` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 681,530.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3924.30` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 25,710.00 USD | 0.00 USD | 228,850.00 USD |
| `7D` | `3924.80` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 247,150.00 USD | 0.00 USD | 433,600.00 USD |
| `1D` | `3928.40` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 135,190.00 USD | 0.00 USD | 327,360.00 USD |
| `7D` | `3929.10` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 184,740.00 USD | 0.00 USD | 801,220.00 USD |
| `1D` | `3932.50` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 140,320.00 USD | 0.00 USD | 217,950.00 USD |
| `7D` | `3933.40` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3936.60` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 48,410.00 USD | 0.00 USD | 204,270.00 USD |
| `7D` | `3937.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3940.70` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 171,850.00 USD | 0.00 USD | 211,630.00 USD |
| `7D` | `3942.00` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3944.80` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 172,700.00 USD | 0.00 USD | 431,260.00 USD |
| `7D` | `3946.30` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.90` | 431,450.00 USD | 0.00 USD | 431,450.00 USD | 76,130.00 USD | 0.00 USD | 126,140.00 USD |
| `7D` | `3950.60` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 333,580.00 USD | 0.00 USD | 491,590.00 USD |
| `1D` | `3953.00` | 229,180.00 USD | 0.00 USD | 229,180.00 USD | 30,470.00 USD | 0.00 USD | 145,750.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `1D` | `3957.10` | 52,960.00 USD | 0.00 USD | 52,960.00 USD | 13,440.00 USD | 0.00 USD | 19,630.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `1D` | `3961.20` | 19,880.00 USD | 0.00 USD | 19,880.00 USD | 10,620.00 USD | 0.00 USD | 9,260.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `7D` | `3994.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3994.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4071.90` | 233,240.00 USD | 233,240.00 USD | 0.00 USD | 152,500.00 USD | 0.00 USD | 80,750.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,710.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4076.00` | 477,130.00 USD | 477,130.00 USD | 0.00 USD | 86,290.00 USD | 0.00 USD | 157,610.00 USD |
| `7D` | `4079.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 657,780.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4080.10` | 610,660.00 USD | 610,660.00 USD | 0.00 USD | 11,650.00 USD | 0.00 USD | 121,880.00 USD |
| `7D` | `4083.90` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 636,940.00 USD |
| `1D` | `4084.20` | 802,570.00 USD | 802,570.00 USD | 0.00 USD | 25,710.00 USD | 0.00 USD | 166,200.00 USD |
| `7D` | `4088.20` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 785,900.00 USD |
| `1D` | `4088.30` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 135,190.00 USD | 0.00 USD | 372,070.00 USD |
| `1D` | `4092.40` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 134,290.00 USD | 0.00 USD | 235,900.00 USD |
| `7D` | `4092.50` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4096.50` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 37,390.00 USD | 0.00 USD | 177,100.00 USD |
| `7D` | `4096.80` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4100.60` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 137,890.00 USD | 0.00 USD | 188,110.00 USD |
| `7D` | `4101.10` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4104.70` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 175,270.00 USD | 0.00 USD | 412,900.00 USD |
| `7D` | `4105.40` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4108.80` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 111,510.00 USD | 0.00 USD | 175,940.00 USD |
| `7D` | `4109.70` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 387,080.00 USD |
| `1D` | `4112.90` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 31,990.00 USD | 0.00 USD | 144,030.00 USD |
| `7D` | `4114.00` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4117.00` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 21,870.00 USD | 0.00 USD | 40,600.00 USD |
| `7D` | `4118.30` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4121.10` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 13,740.00 USD | 0.00 USD | 9,260.00 USD |
| `7D` | `4122.60` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.80` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `4152.70` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.90` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 83,190.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `4157.00` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 318,590.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4158.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 24,310.00 USD | 0.00 USD | 88,700.00 USD |
| `7D` | `4161.30` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 314,240.00 USD | 0.00 USD | 494,920.00 USD |
| `1D` | `4162.10` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 10,530.00 USD | 0.00 USD | 72,670.00 USD |
| `7D` | `4165.60` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4166.20` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 35,670.00 USD | 0.00 USD | 106,040.00 USD |
| `7D` | `4169.90` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 234,080.00 USD |
| `1D` | `4170.30` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 61,420.00 USD | 0.00 USD | 154,940.00 USD |
| `7D` | `4174.20` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4174.40` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 45,240.00 USD | 0.00 USD | 104,760.00 USD |
| `1D` | `4178.50` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 44,660.00 USD | 0.00 USD | 103,420.00 USD |
| `7D` | `4178.50` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4182.60` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 123,510.00 USD |
| `7D` | `4182.80` | 18,190,000.00 USD | 18,190,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4186.70` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 75,110.00 USD | 0.00 USD | 187,540.00 USD |
| `7D` | `4187.10` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4190.80` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 38,070.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `4191.40` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 237,350.00 USD |
| `1D` | `4194.90` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | 72,870.00 USD |
| `7D` | `4195.70` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4199.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 6,720.00 USD | 0.00 USD | 9,820.00 USD |
| `7D` | `4200.00` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `1D` | `4203.10` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 5,310.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `4204.30` | 19,840,000.00 USD | 19,840,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,140,000.00 USD | 20,140,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,210,000.00 USD | 20,210,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,240,000.00 USD | 20,240,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,400,000.00 USD | 20,400,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `4387.60` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 3,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4389.20` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4391.70` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 18,270.00 USD | 0.00 USD | 12,550.00 USD |
| `7D` | `4393.50` | 20,760,000.00 USD | 20,760,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4395.80` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 23,610.00 USD |
| `7D` | `4397.80` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4399.40` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,490.00 USD |
| `7D` | `4402.10` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `7D` | `4406.40` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `7D` | `4410.70` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `7D` | `4415.00` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4427.90` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.20` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 35,220.00 USD | 0.00 USD | 44,420.00 USD |
| `7D` | `4435.80` | 22,040,000.00 USD | 22,040,000.00 USD | 0.00 USD | 19,260.00 USD | 0.00 USD | 37,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `804.55M` | Total OI Tokens: `201,357.4 XAUT`
  * 1h OI Change: `-0.03%` | 4h OI Change: `+1.34%` | 24h OI Change: `-5.59%`
  * Exchange Breakdown: Binance=`61.18M` | Bybit=`144.45M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `44.62%` | `55.38%` | `0.81` | 4,530,000.00 USD |
| `15M` | `Binance` | `45.41%` | `54.59%` | `0.83` | 2,060,000.00 USD |
| `15M` | `OKX` | `40.63%` | `59.37%` | `0.68` | 848,740.00 USD |
| `15M` | `Bybit` | `50.14%` | `49.86%` | `1.01` | 370,600.00 USD |
| `15M` | `KuCoin` | `52.64%` | `47.36%` | `1.11` | 21,300.00 USD |
| `15M` | `Gate` | `56.56%` | `43.44%` | `1.30` | 47,130.00 USD |
| `15M` | `Bitget` | `69.24%` | `30.76%` | `2.25` | 271,390.00 USD |
| `15M` | `BingX` | `40.08%` | `59.92%` | `0.67` | 238,730.00 USD |
| `15M` | `MEXC` | `20.67%` | `79.33%` | `0.26` | 384,930.00 USD |
| `15M` | `Bitunix` | `42.14%` | `57.86%` | `0.73` | 78,300.00 USD |
| `15M` | `Hyperliquid` | `55.44%` | `44.56%` | `1.24` | 33,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.66%` | `50.34%` | `0.99` | 129,060.00 USD |
| `15M` | `Crypto.com` | `66.95%` | `33.05%` | `2.03` | 2,150.00 USD |
| `15M` | `WhiteBIT` | `81.07%` | `18.93%` | `4.28` | 27,820.00 USD |
| `15M` | `HTX` | `46.15%` | `53.85%` | `0.86` | 1,070.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `67.03%` | `32.97%` | `2.03` | 2,300.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `96.05%` | `3.95%` | `24.32` | 12,730.00 USD |
| `15M` | `Whale Positions` | `45.41%` | `54.59%` | `0.83` | 2,060,000.00 USD |
| `15M` | `Global Accounts` | `44.62%` | `55.38%` | `0.81` | 4,530,000.00 USD |
| `1H` | `XAUT` | `51.02%` | `48.98%` | `1.04` | 12,310,000.00 USD |
| `1H` | `Binance` | `54.13%` | `45.87%` | `1.18` | 5,580,000.00 USD |
| `1H` | `OKX` | `48.71%` | `51.29%` | `0.95` | 1,990,000.00 USD |
| `1H` | `Bybit` | `55.19%` | `44.81%` | `1.23` | 1,140,000.00 USD |
| `1H` | `KuCoin` | `51.18%` | `48.82%` | `1.05` | 108,150.00 USD |
| `1H` | `Gate` | `54.33%` | `45.67%` | `1.19` | 395,290.00 USD |
| `1H` | `Bitget` | `51.78%` | `48.22%` | `1.07` | 700,570.00 USD |
| `1H` | `BingX` | `43.35%` | `56.65%` | `0.77` | 496,910.00 USD |
| `1H` | `MEXC` | `38.49%` | `61.51%` | `0.63` | 737,500.00 USD |
| `1H` | `Bitunix` | `41.04%` | `58.96%` | `0.70` | 235,620.00 USD |
| `1H` | `Hyperliquid` | `31.42%` | `68.58%` | `0.46` | 275,200.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.56%` | `50.44%` | `0.98` | 503,860.00 USD |
| `1H` | `Crypto.com` | `14.68%` | `85.32%` | `0.17` | 2,470.00 USD |
| `1H` | `WhiteBIT` | `64.76%` | `35.24%` | `1.84` | 114,000.00 USD |
| `1H` | `HTX` | `48.45%` | `51.55%` | `0.94` | 1,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `76.04%` | `23.96%` | `3.17` | 6,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `82.1%` | `17.9%` | `4.59` | 18,530.00 USD |
| `1H` | `Whale Positions` | `54.13%` | `45.87%` | `1.18` | 5,580,000.00 USD |
| `1H` | `Global Accounts` | `51.02%` | `48.98%` | `1.04` | 12,310,000.00 USD |
| `4H` | `XAUT` | `52.07%` | `47.93%` | `1.09` | 51,380,000.00 USD |
| `4H` | `Binance` | `52.56%` | `47.44%` | `1.11` | 21,160,000.00 USD |
| `4H` | `OKX` | `53.41%` | `46.59%` | `1.15` | 8,380,000.00 USD |
| `4H` | `Bybit` | `54.15%` | `45.85%` | `1.18` | 6,260,000.00 USD |
| `4H` | `KuCoin` | `52.58%` | `47.42%` | `1.11` | 413,730.00 USD |
| `4H` | `Gate` | `54.78%` | `45.22%` | `1.21` | 1,930,000.00 USD |
| `4H` | `Bitget` | `51.52%` | `48.48%` | `1.06` | 2,730,000.00 USD |
| `4H` | `BingX` | `37.69%` | `62.31%` | `0.60` | 1,810,000.00 USD |
| `4H` | `MEXC` | `48.03%` | `51.97%` | `0.92` | 2,540,000.00 USD |
| `4H` | `Bitunix` | `48.44%` | `51.56%` | `0.94` | 1,330,000.00 USD |
| `4H` | `Hyperliquid` | `50.05%` | `49.95%` | `1.00` | 2,280,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.38%` | `50.62%` | `0.98` | 1,870,000.00 USD |
| `4H` | `Crypto.com` | `48.59%` | `51.41%` | `0.95` | 27,130.00 USD |
| `4H` | `WhiteBIT` | `78.38%` | `21.62%` | `3.63` | 465,470.00 USD |
| `4H` | `HTX` | `27.81%` | `72.19%` | `0.39` | 28,770.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.18%` | `56.82%` | `0.76` | 71,720.00 USD |
| `4H` | `Aster` | `69.8%` | `30.2%` | `2.31` | 25,440.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `63%` | `37%` | `1.70` | 78,160.00 USD |
| `4H` | `Whale Positions` | `52.56%` | `47.44%` | `1.11` | 21,160,000.00 USD |
| `4H` | `Global Accounts` | `52.07%` | `47.93%` | `1.09` | 51,380,000.00 USD |


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
| `5m` | -50,880.00 USD | -95,700.00 USD | **`DISTRIBUTION`** |
| `15m` | 2,270.00 USD | -129,090.00 USD | **`DISTRIBUTION`** |
| `30m` | 198,690.00 USD | 17,800.00 USD | **`ACCUMULATION`** |
| `1h` | -83,110.00 USD | -640,730.00 USD | **`DISTRIBUTION`** |
| `2h` | -592,410.00 USD | -863,380.00 USD | **`DISTRIBUTION`** |
| `4h` | -956,870.00 USD | -1,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,610,000.00 USD | -2,950,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,750,000.00 USD | -2,210,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,260,000.00 USD | -1,750,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -341,240.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -75,300,000.00 USD | -20,380,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,570,000.00 USD | -84,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-50.88K` | 15m=`+2.27K` | 1h=`-83.11K` | 24h=`-341.24K`
* Futures Capital Netflows: 5m=`-95.70K` | 15m=`-129.09K` | 1h=`-640.73K` | 24h=`-2.54M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26481.40` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26398.35` (Risk Distance: `83.04` pts)
  * +2.5R Take Profit: `26689.00`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26640.76` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26723.81` (Risk Distance: `83.04` pts)
  * +2.5R Take Profit: `26433.16`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26773.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
