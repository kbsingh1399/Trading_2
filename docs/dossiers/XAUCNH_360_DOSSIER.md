# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26541.20` | **Live Ask Quote**: `26543.05` | **Mid Price**: `26542.12`
- **Spread Points**: `185.00` | **Spread BPS**: `0.70 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26542.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.36` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26727.92` | Lower -3.00σ Band: `26356.33`
  * Upper +2.51σ Band: `26688.11` | Lower -2.51σ Band: `26396.14`
  * Upper +2.01σ Band: `26653.60` | Lower -2.01σ Band: `26430.65`
  * Upper +2.00σ Band: `26648.29` | Lower -2.00σ Band: `26435.96`
  * Upper +1.28σ Band: `26616.44` | Lower -1.28σ Band: `26467.81`
  * Upper +1.00σ Band: `26595.21` | Lower -1.00σ Band: `26489.04`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26542.12` | EMA-20=`26542.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26542.12` (Slope: `+0.0000`) | EMA-100=`26542.12`
  * Institutional Anchors: EMA-144=`26542.12` | EMA-200=`26542.12` (Slope: `+0.0000`) | EMA-233=`26542.12`
- **Range Boundaries**: 24H High=`26807.55` | 24H Low=`26276.70` | Weekly High=`27072.97` | Weekly Low=`26011.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26621.75` (Distance: `+0.00%`)
  * Point of Control (POC) = `26542.12` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26462.50` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26648.29` | POC=`26542.12` | VAL=`26435.96`
  * Prior Day Extremes: PDH=`26701.38` | PDL=`26382.87` | PDC=`26542.12`
  * Monday Range Blueprint: High=`26674.84` | Mid=`26542.12` | Low=`26409.41`
  * Developing Weekly Value Area: Weekly VAH=`26754.46` | Weekly POC=`26542.12` | Weekly VAL=`26329.79`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26595.21` | Low=`26489.04`
  * London Session (08:00-16:00 UTC): High=`26648.29` | Low=`26435.96`
  * New York Session (13:00-21:00 UTC): High=`26701.38` | Low=`26382.87`
  * Initial Balance (First Hour): IB High=`26621.75` | IB Low=`26462.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26435.96` - `26648.29`
  * Optimal Trade Entry (OTE 0.705): `26595.21`
  * Structural Invalidation Anchor (0.786): `26754.46`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,900,238.60 USD | `6,489.82` | `4185.46` | `3990.80` | `29393.84` | 1,262,712.41 USD | `+4.88%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,259,422.58 USD | `6,329.25` | `4128.54` | `3990.80` | `13998.90` | 871,173.16 USD | `+3.45%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,426,181.52 USD | `5,869.90` | `4228.86` | `3990.80` | `27046.80` | 1,396,840.42 USD | `+5.96%` | `5X Cross` |
| `102` | `0xec0b...b078` | `LONG` | 19,271,684.55 USD | `4,828.91` | `4157.43` | `3990.80` | `2271.65` | -804,197.77 USD | `-4.17%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,164,983.98 USD | `3,549.32` | `4127.81` | `3990.80` | `621.07` | -485,966.19 USD | `-3.43%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,043,112.06 USD | `3,268.21` | `4228.94` | `3990.80` | `4375.02` | 777,967.07 USD | `+5.96%` | `25X Cross` |
| `183` | `0xa742...e390` | `SHORT` | 11,374,069.39 USD | `2,850.00` | `4364.75` | `3990.80` | `4241.57` | 1,065,497.64 USD | `+9.37%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,779,980.00 USD | `2,200.00` | `4176.09` | `3990.80` | `2613.65` | -407,439.30 USD | `-4.64%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,779,980.00 USD | `2,200.00` | `4112.20` | `3990.80` | `4331.43` | 266,874.59 USD | `+3.04%` | `20X Cross` |
| `300` | `0xacb6...efbd` | `SHORT` | 7,883,500.54 USD | `1,975.37` | `4048.55` | `3990.80` | `6630.41` | 113,891.17 USD | `+1.44%` | `6X Cross` |
| `369` | `0xc26c...b8f4` | `LONG` | 6,305,429.64 USD | `1,579.95` | `4075.62` | `3990.80` | `0.000000` | -133,867.33 USD | `-2.12%` | `1X Cross` |
| `563` | `0x63da...8add` | `LONG` | 3,990,900.00 USD | `1,000.00` | `4021.46` | `3990.80` | `3564.40` | -30,560.96 USD | `-0.77%` | `25X Cross` |
| `580` | `0xf3dc...1672` | `LONG` | 3,928,224.36 USD | `984.27` | `4018.39` | `3990.80` | `2904.08` | -26,962.33 USD | `-0.69%` | `20X Cross` |
| `588` | `0x9aa5...58af` | `LONG` | 3,877,726.06 USD | `971.64` | `4279.98` | `3990.80` | `0.000000` | -280,883.03 USD | `-7.24%` | `20X Cross` |
| `627` | `0x354b...6425` | `LONG` | 3,597,737.68 USD | `901.49` | `4004.93` | `3990.80` | `0.000000` | -12,652.26 USD | `-0.35%` | `10X Cross` |
| `675` | `0x4a20...3c26` | `LONG` | 3,341,978.46 USD | `837.40` | `4599.73` | `3990.80` | `0.000000` | -509,841.92 USD | `-15.26%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,739,692.99 USD | `686.49` | `4290.34` | `3990.80` | `1182.67` | -205,565.72 USD | `-7.50%` | `25X Cross` |
| `906` | `0x625e...a354` | `SHORT` | 2,474,358.00 USD | `620.00` | `4122.81` | `3990.80` | `4342.53` | 81,789.03 USD | `+3.31%` | `20X Cross` |
| `909` | `0xd8c5...99b0` | `SHORT` | 2,467,792.57 USD | `618.35` | `4175.35` | `3990.80` | `34259.09` | 114,060.03 USD | `+4.62%` | `4X Cross` |
| `930` | `0xeae3...e8ad` | `SHORT` | 2,394,600.00 USD | `600.00` | `4104.77` | `3990.80` | `4325.55` | 68,265.11 USD | `+2.85%` | `20X Cross` |
| `932` | `0xf285...fa82` | `LONG` | 2,386,980.84 USD | `598.11` | `4146.45` | `3990.80` | `3891.53` | -93,038.72 USD | `-3.90%` | `25X Cross` |
| `952` | `0x12f7...8750` | `LONG` | 2,337,113.74 USD | `585.61` | `4082.77` | `3990.80` | `2610.30` | -53,803.24 USD | `-2.30%` | `10X Cross` |
| `1092` | `0x413c...886c` | `LONG` | 1,995,500.00 USD | `500.00` | `4010.43` | `3990.80` | `0.000000` | -9,716.23 USD | `-0.49%` | `2X Cross` |
| `1100` | `0x9c06...0560` | `LONG` | 1,989,133.60 USD | `498.42` | `4012.76` | `3990.80` | `0.000000` | -10,897.90 USD | `-0.55%` | `25X Cross` |
| `1106` | `0x61ce...a62b` | `SHORT` | 1,985,536.47 USD | `497.50` | `4071.66` | `3990.80` | `4716.29` | 40,132.32 USD | `+2.02%` | `20X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,811,006.17 USD | `453.78` | `4220.88` | `3990.80` | `3539.23` | -104,361.89 USD | `-5.76%` | `5X Isolated` |
| `1310` | `0x46fc...1195` | `LONG` | 1,653,122.17 USD | `414.22` | `4053.27` | `3990.80` | `2160.93` | -25,836.05 USD | `-1.56%` | `20X Cross` |
| `1344` | `0x6d15...d374` | `LONG` | 1,596,360.00 USD | `400.00` | `4068.25` | `3990.80` | `3842.10` | -30,940.00 USD | `-1.94%` | `25X Cross` |
| `1345` | `0xee02...309d` | `SHORT` | 1,596,360.00 USD | `400.00` | `4438.84` | `3990.80` | `4227.17` | 179,178.60 USD | `+11.22%` | `25X Isolated` |
| `1389` | `0x02a7...fe9f` | `SHORT` | 1,556,451.00 USD | `390.00` | `4055.02` | `3990.80` | `4306.98` | 25,008.25 USD | `+1.61%` | `25X Cross` |
| `1431` | `0x7e77...b8d2` | `SHORT` | 1,516,542.00 USD | `380.00` | `4131.92` | `3990.80` | `4293.79` | 53,587.64 USD | `+3.53%` | `20X Cross` |
| `1452` | `0x72c2...9b37` | `LONG` | 1,489,167.02 USD | `373.13` | `4000.98` | `3990.80` | `3778.33` | -3,726.50 USD | `-0.25%` | `13X Isolated` |
| `1501` | `0xaa44...b844` | `LONG` | 1,436,760.00 USD | `360.00` | `4043.10` | `3990.80` | `2820.31` | -18,757.63 USD | `-1.31%` | `4X Cross` |
| `1607` | `0xa41f...d50a` | `LONG` | 1,312,854.84 USD | `328.96` | `4468.89` | `3990.80` | `3802.46` | -157,243.01 USD | `-11.98%` | `15X Cross` |
| `1659` | `0xbf5a...88ba` | `SHORT` | 1,267,728.94 USD | `317.65` | `4091.80` | `3990.80` | `10002.07` | 32,054.09 USD | `+2.53%` | `20X Cross` |
| `1693` | `0xff31...ff6c` | `SHORT` | 1,237,179.00 USD | `310.00` | `4372.43` | `3990.80` | `4789.46` | 118,276.38 USD | `+9.56%` | `10X Isolated` |
| `1711` | `0x7fda...17d1` | `SHORT` | 1,213,881.32 USD | `304.16` | `4013.13` | `3990.80` | `31968.25` | 6,761.91 USD | `+0.56%` | `20X Cross` |
| `1715` | `0xada6...6f88` | `LONG` | 1,211,259.72 USD | `303.50` | `4166.46` | `3990.80` | `1794.53` | -53,253.14 USD | `-4.40%` | `5X Cross` |
| `1873` | `0x50e2...d770` | `LONG` | 1,079,009.26 USD | `270.37` | `4243.58` | `3990.80` | `2562.39` | -68,317.20 USD | `-6.33%` | `20X Cross` |
| `1887` | `0x4c92...4f17` | `SHORT` | 1,064,454.84 USD | `266.72` | `4260.98` | `3990.80` | `6505.41` | 72,037.39 USD | `+6.77%` | `20X Cross` |
| `1966` | `0xd346...c4f3` | `LONG` | 1,018,373.12 USD | `255.17` | `4188.66` | `3990.80` | `3310.71` | -50,463.39 USD | `-4.96%` | `5X Isolated` |

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
| `7D` | `3589.60` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 37,380.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.10` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `3593.90` | 22,380,000.00 USD | 0.00 USD | 22,380,000.00 USD | 90,390.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3595.30` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 24,410.00 USD | 0.00 USD | 21,200.00 USD |
| `7D` | `3598.20` | 22,130,000.00 USD | 0.00 USD | 22,130,000.00 USD | 96,930.00 USD | 0.00 USD | 334,460.00 USD |
| `1D` | `3599.50` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 6,610.00 USD | 0.00 USD | 34,940.00 USD |
| `7D` | `3602.50` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 108,630.00 USD | 0.00 USD | 94,250.00 USD |
| `1D` | `3603.70` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 13,320.00 USD | 0.00 USD | 33,720.00 USD |
| `7D` | `3606.80` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3607.90` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 18,250.00 USD | 0.00 USD | 64,400.00 USD |
| `7D` | `3611.10` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.10` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 17,620.00 USD | 0.00 USD | 26,900.00 USD |
| `7D` | `3615.40` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.30` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.70` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.50` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 21,740.00 USD | 0.00 USD | 66,750.00 USD |
| `7D` | `3624.00` | 21,070,000.00 USD | 0.00 USD | 21,070,000.00 USD | 35,700.00 USD | 0.00 USD | 135,260.00 USD |
| `1D` | `3624.70` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 16,500.00 USD | 0.00 USD | 31,700.00 USD |
| `7D` | `3628.30` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 47,240.00 USD | 0.00 USD | 49,230.00 USD |
| `1D` | `3628.90` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 3,400.00 USD | 0.00 USD | 21,120.00 USD |
| `7D` | `3632.60` | 20,800,000.00 USD | 0.00 USD | 20,800,000.00 USD | 46,540.00 USD | 0.00 USD | 74,720.00 USD |
| `1D` | `3633.10` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 2,840.00 USD |
| `7D` | `3636.90` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.20` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 60,700.00 USD | 0.00 USD | 19,320.00 USD |
| `7D` | `3645.50` | 20,540,000.00 USD | 0.00 USD | 20,540,000.00 USD | 12,340.00 USD | 0.00 USD | 8,230.00 USD |
| `7D` | `3649.80` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3654.10` | 20,500,000.00 USD | 0.00 USD | 20,500,000.00 USD | 16,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.40` | 20,480,000.00 USD | 0.00 USD | 20,480,000.00 USD | 2,310.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.80` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3826.10` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `7D` | `3830.40` | 20,400,000.00 USD | 0.00 USD | 20,400,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3830.50` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `1D` | `3834.70` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 89,600.00 USD | 0.00 USD | 50,170.00 USD |
| `7D` | `3834.70` | 19,940,000.00 USD | 0.00 USD | 19,940,000.00 USD | 299,820.00 USD | 0.00 USD | 636,110.00 USD |
| `1D` | `3838.90` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 22,350.00 USD | 0.00 USD | 119,800.00 USD |
| `7D` | `3839.00` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 306,770.00 USD | 0.00 USD | 741,540.00 USD |
| `1D` | `3843.10` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 46,080.00 USD | 0.00 USD | 97,130.00 USD |
| `7D` | `3843.30` | 17,950,000.00 USD | 0.00 USD | 17,950,000.00 USD | 301,340.00 USD | 0.00 USD | 336,030.00 USD |
| `1D` | `3847.30` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 66,000.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `3847.60` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 120,700.00 USD | 0.00 USD | 396,440.00 USD |
| `1D` | `3851.50` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 73,320.00 USD | 0.00 USD | 129,680.00 USD |
| `7D` | `3851.90` | 16,800,000.00 USD | 0.00 USD | 16,800,000.00 USD | 171,170.00 USD | 0.00 USD | 214,130.00 USD |
| `1D` | `3855.70` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 27,220.00 USD | 0.00 USD | 99,710.00 USD |
| `7D` | `3856.20` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 102,180.00 USD | 0.00 USD | 205,820.00 USD |
| `1D` | `3859.90` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 68,340.00 USD | 0.00 USD | 112,500.00 USD |
| `7D` | `3860.50` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 99,820.00 USD | 0.00 USD | 211,660.00 USD |
| `1D` | `3864.10` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 83,140.00 USD | 0.00 USD | 203,720.00 USD |
| `7D` | `3864.80` | 15,790,000.00 USD | 0.00 USD | 15,790,000.00 USD | 104,580.00 USD | 0.00 USD | 384,380.00 USD |
| `1D` | `3868.30` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 32,990.00 USD | 0.00 USD | 59,180.00 USD |
| `7D` | `3869.10` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 192,180.00 USD | 0.00 USD | 155,040.00 USD |
| `1D` | `3872.50` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 6,710.00 USD | 0.00 USD | 69,480.00 USD |
| `7D` | `3873.40` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 110,510.00 USD | 0.00 USD | 204,740.00 USD |
| `7D` | `3877.70` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 204,970.00 USD | 0.00 USD | 69,410.00 USD |
| `7D` | `3882.00` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 195,280.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.30` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 80,200.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.60` | 13,950,000.00 USD | 0.00 USD | 13,950,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.90` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.20` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.50` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.80` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 161,150.00 USD | 0.00 USD | 293,620.00 USD |
| `1D` | `3910.30` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `3912.10` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 413,650.00 USD | 0.00 USD | 666,170.00 USD |
| `1D` | `3914.50` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 179,200.00 USD | 0.00 USD | 100,340.00 USD |
| `7D` | `3916.40` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 731,180.00 USD | 0.00 USD | 1,720,000.00 USD |
| `1D` | `3918.70` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 44,700.00 USD | 0.00 USD | 186,400.00 USD |
| `7D` | `3920.70` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 682,120.00 USD | 0.00 USD | 1,080,000.00 USD |
| `1D` | `3922.90` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 92,170.00 USD | 0.00 USD | 247,470.00 USD |
| `7D` | `3925.00` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 288,490.00 USD | 0.00 USD | 564,840.00 USD |
| `1D` | `3927.10` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 114,120.00 USD | 0.00 USD | 380,740.00 USD |
| `7D` | `3929.30` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 184,740.00 USD | 0.00 USD | 722,850.00 USD |
| `1D` | `3931.30` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 162,220.00 USD | 0.00 USD | 249,590.00 USD |
| `7D` | `3933.60` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 429,850.00 USD | 0.00 USD | 361,490.00 USD |
| `1D` | `3935.50` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 22,890.00 USD | 0.00 USD | 208,370.00 USD |
| `7D` | `3937.90` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 135,570.00 USD | 0.00 USD | 483,400.00 USD |
| `1D` | `3939.70` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 149,180.00 USD | 0.00 USD | 198,540.00 USD |
| `7D` | `3942.20` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 204,720.00 USD | 0.00 USD | 582,150.00 USD |
| `1D` | `3943.90` | 968,660.00 USD | 0.00 USD | 968,660.00 USD | 152,570.00 USD | 0.00 USD | 390,180.00 USD |
| `7D` | `3946.50` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 220,330.00 USD | 0.00 USD | 506,970.00 USD |
| `1D` | `3948.10` | 425,910.00 USD | 0.00 USD | 425,910.00 USD | 101,020.00 USD | 0.00 USD | 172,500.00 USD |
| `7D` | `3950.80` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 351,130.00 USD | 0.00 USD | 393,380.00 USD |
| `1D` | `3952.30` | 152,380.00 USD | 0.00 USD | 152,380.00 USD | 13,410.00 USD | 0.00 USD | 138,970.00 USD |
| `7D` | `3955.10` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 283,950.00 USD | 0.00 USD | 398,270.00 USD |
| `7D` | `3959.40` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 424,150.00 USD | 0.00 USD | 27,620.00 USD |
| `7D` | `3963.70` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 288,790.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3968.00` | 840,760.00 USD | 0.00 USD | 840,760.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.30` | 542,230.00 USD | 0.00 USD | 542,230.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.60` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.90` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.20` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `3990.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3991.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.90` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `1D` | `4069.90` | 59,730.00 USD | 59,730.00 USD | 0.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `4071.20` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 406,580.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4074.10` | 330,840.00 USD | 330,840.00 USD | 0.00 USD | 170,780.00 USD | 0.00 USD | 100,340.00 USD |
| `7D` | `4075.50` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 557,700.00 USD | 0.00 USD | 1,170,000.00 USD |
| `1D` | `4078.30` | 561,370.00 USD | 561,370.00 USD | 0.00 USD | 53,120.00 USD | 0.00 USD | 177,410.00 USD |
| `7D` | `4079.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 652,950.00 USD | 0.00 USD | 1,420,000.00 USD |
| `1D` | `4082.50` | 873,330.00 USD | 873,330.00 USD | 0.00 USD | 82,490.00 USD | 0.00 USD | 229,470.00 USD |
| `7D` | `4084.10` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 423,660.00 USD | 0.00 USD | 634,060.00 USD |
| `1D` | `4086.70` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 108,840.00 USD | 0.00 USD | 328,940.00 USD |
| `7D` | `4088.40` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 223,710.00 USD | 0.00 USD | 821,070.00 USD |
| `1D` | `4090.90` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 158,790.00 USD | 0.00 USD | 259,780.00 USD |
| `7D` | `4092.70` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 328,770.00 USD |
| `1D` | `4095.10` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 33,980.00 USD | 0.00 USD | 176,600.00 USD |
| `7D` | `4097.00` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 384,620.00 USD |
| `1D` | `4099.30` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 113,960.00 USD | 0.00 USD | 197,190.00 USD |
| `7D` | `4101.30` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 188,200.00 USD | 0.00 USD | 390,740.00 USD |
| `1D` | `4103.50` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 164,560.00 USD | 0.00 USD | 402,860.00 USD |
| `7D` | `4105.60` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 204,180.00 USD | 0.00 USD | 785,850.00 USD |
| `1D` | `4107.70` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 104,040.00 USD | 0.00 USD | 195,440.00 USD |
| `7D` | `4109.90` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 282,300.00 USD | 0.00 USD | 297,720.00 USD |
| `1D` | `4111.90` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 36,140.00 USD | 0.00 USD | 110,430.00 USD |
| `7D` | `4114.20` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 289,400.00 USD | 0.00 USD | 316,960.00 USD |
| `1D` | `4116.10` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 94,650.00 USD |
| `7D` | `4118.50` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 356,370.00 USD | 0.00 USD | 286,230.00 USD |
| `7D` | `4122.80` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 52,260.00 USD |
| `7D` | `4127.10` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 217,580.00 USD |
| `7D` | `4131.40` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.70` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4140.00` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.30` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.60` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 121,260.00 USD | 0.00 USD | 181,720.00 USD |
| `1D` | `4149.70` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `4152.90` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 269,320.00 USD | 0.00 USD | 478,680.00 USD |
| `1D` | `4153.90` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 85,390.00 USD | 0.00 USD | 50,170.00 USD |
| `7D` | `4157.20` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 321,670.00 USD | 0.00 USD | 803,550.00 USD |
| `1D` | `4158.10` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 26,560.00 USD | 0.00 USD | 88,700.00 USD |
| `7D` | `4161.50` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 343,830.00 USD | 0.00 USD | 502,040.00 USD |
| `1D` | `4162.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 41,250.00 USD | 0.00 USD | 93,520.00 USD |
| `7D` | `4165.80` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 108,620.00 USD | 0.00 USD | 294,840.00 USD |
| `1D` | `4166.50` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 40,500.00 USD | 0.00 USD | 133,830.00 USD |
| `7D` | `4170.10` | 17,280,000.00 USD | 17,280,000.00 USD | 0.00 USD | 76,390.00 USD | 0.00 USD | 251,660.00 USD |
| `1D` | `4170.70` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 83,520.00 USD | 0.00 USD | 164,850.00 USD |
| `7D` | `4174.40` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 190,840.00 USD | 0.00 USD | 180,750.00 USD |
| `1D` | `4174.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 26,780.00 USD | 0.00 USD | 95,550.00 USD |
| `7D` | `4178.70` | 17,950,000.00 USD | 17,950,000.00 USD | 0.00 USD | 54,010.00 USD | 0.00 USD | 241,700.00 USD |
| `1D` | `4179.10` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | 104,490.00 USD |
| `7D` | `4183.00` | 18,250,000.00 USD | 18,250,000.00 USD | 0.00 USD | 101,150.00 USD | 0.00 USD | 196,390.00 USD |
| `1D` | `4183.30` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 159,680.00 USD |
| `7D` | `4187.30` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 92,010.00 USD | 0.00 USD | 328,610.00 USD |
| `1D` | `4187.50` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 64,690.00 USD | 0.00 USD | 134,210.00 USD |
| `7D` | `4191.60` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 155,040.00 USD |
| `1D` | `4191.70` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 18,070.00 USD | 0.00 USD | 47,820.00 USD |
| `1D` | `4195.90` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | 63,720.00 USD |
| `7D` | `4195.90` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 110,510.00 USD | 0.00 USD | 176,870.00 USD |
| `7D` | `4200.20` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 193,240.00 USD | 0.00 USD | 97,280.00 USD |
| `7D` | `4204.50` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 185,710.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.80` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 95,270.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4213.10` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.40` | 20,160,000.00 USD | 20,160,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.70` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4226.00` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.30` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.50` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4385.10` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `4389.10` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4389.40` | 20,530,000.00 USD | 20,530,000.00 USD | 0.00 USD | 49,530.00 USD | 0.00 USD | 126,620.00 USD |
| `1D` | `4393.30` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 11,060.00 USD |
| `7D` | `4393.70` | 20,740,000.00 USD | 20,740,000.00 USD | 0.00 USD | 69,970.00 USD | 0.00 USD | 134,610.00 USD |
| `1D` | `4397.50` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 7,610.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4398.00` | 21,090,000.00 USD | 21,090,000.00 USD | 0.00 USD | 85,930.00 USD | 0.00 USD | 262,520.00 USD |
| `1D` | `4401.70` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 16,500.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4402.30` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 103,800.00 USD | 0.00 USD | 81,180.00 USD |
| `1D` | `4405.90` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 6,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4406.60` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `1D` | `4410.10` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 13,560.00 USD | 0.00 USD | 58,710.00 USD |
| `7D` | `4410.90` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | 47,070.00 USD |
| `1D` | `4413.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 17,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4415.20` | 21,540,000.00 USD | 21,540,000.00 USD | 0.00 USD | 49,560.00 USD | 0.00 USD | 15,490.00 USD |
| `7D` | `4419.50` | 21,600,000.00 USD | 21,600,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 46,670.00 USD |
| `7D` | `4423.80` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4428.10` | 21,860,000.00 USD | 21,860,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.40` | 21,940,000.00 USD | 21,940,000.00 USD | 0.00 USD | 44,420.00 USD | 0.00 USD | 33,300.00 USD |
| `7D` | `4433.30` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `809.83M` | Total OI Tokens: `202,928.2 XAUT`
  * 1h OI Change: `+0.75%` | 4h OI Change: `-1.19%` | 24h OI Change: `-8.38%`
  * Exchange Breakdown: Binance=`61.09M` | Bybit=`144.58M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `51.10%` | `48.90%` | `1.04` | 1,620,000.00 USD |
| `15M` | `Binance` | `51.15%` | `48.85%` | `1.05` | 482,900.00 USD |
| `15M` | `OKX` | `53.2%` | `46.8%` | `1.14` | 88,400.00 USD |
| `15M` | `Bybit` | `40.13%` | `59.87%` | `0.67` | 251,700.00 USD |
| `15M` | `KuCoin` | `51.84%` | `48.16%` | `1.08` | 171,580.00 USD |
| `15M` | `Gate` | `61.61%` | `38.39%` | `1.60` | 47,670.00 USD |
| `15M` | `Bitget` | `54.85%` | `45.15%` | `1.21` | 319,980.00 USD |
| `15M` | `BingX` | `54.53%` | `45.47%` | `1.20` | 72,160.00 USD |
| `15M` | `MEXC` | `72.18%` | `27.82%` | `2.59` | 40,290.00 USD |
| `15M` | `Bitunix` | `52.78%` | `47.22%` | `1.12` | 17,880.00 USD |
| `15M` | `Hyperliquid` | `65.26%` | `34.74%` | `1.88` | 18,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.98%` | `50.02%` | `1.00` | 71,650.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `30.85%` | `69.15%` | `0.45` | 23,950.00 USD |
| `15M` | `HTX` | `99.91%` | `0.09%` | `1110.11` | 201.51 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `43.25%` | `56.75%` | `0.76` | 12,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `4.25%` | `95.75%` | `0.04` | 235.76 USD |
| `15M` | `Whale Positions` | `51.15%` | `48.85%` | `1.05` | 482,900.00 USD |
| `15M` | `Global Accounts` | `51.10%` | `48.90%` | `1.04` | 1,620,000.00 USD |
| `1H` | `XAUT` | `47.66%` | `52.34%` | `0.91` | 4,680,000.00 USD |
| `1H` | `Binance` | `51.18%` | `48.82%` | `1.05` | 1,390,000.00 USD |
| `1H` | `OKX` | `50.78%` | `49.22%` | `1.03` | 437,010.00 USD |
| `1H` | `Bybit` | `47.19%` | `52.81%` | `0.89` | 421,870.00 USD |
| `1H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 615,170.00 USD |
| `1H` | `Gate` | `49.84%` | `50.16%` | `0.99` | 102,290.00 USD |
| `1H` | `Bitget` | `52.03%` | `47.97%` | `1.08` | 454,640.00 USD |
| `1H` | `BingX` | `30.34%` | `69.66%` | `0.44` | 628,310.00 USD |
| `1H` | `MEXC` | `46.32%` | `53.68%` | `0.86` | 196,860.00 USD |
| `1H` | `Bitunix` | `36.76%` | `63.24%` | `0.58` | 62,120.00 USD |
| `1H` | `Hyperliquid` | `62.03%` | `37.97%` | `1.63` | 33,270.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 247,610.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `64.37%` | `35.63%` | `1.81` | 75,360.00 USD |
| `1H` | `HTX` | `39.82%` | `60.18%` | `0.66` | 543.82 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `59.82%` | `40.18%` | `1.49` | 20,890.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `16.54%` | `83.46%` | `0.20` | 1,040.00 USD |
| `1H` | `Whale Positions` | `51.18%` | `48.82%` | `1.05` | 1,390,000.00 USD |
| `1H` | `Global Accounts` | `47.66%` | `52.34%` | `0.91` | 4,680,000.00 USD |
| `4H` | `XAUT` | `48.42%` | `51.58%` | `0.94` | 20,070,000.00 USD |
| `4H` | `Binance` | `49.93%` | `50.07%` | `1.00` | 6,840,000.00 USD |
| `4H` | `OKX` | `48.88%` | `51.12%` | `0.96` | 2,100,000.00 USD |
| `4H` | `Bybit` | `52.33%` | `47.67%` | `1.10` | 2,000,000.00 USD |
| `4H` | `KuCoin` | `50.08%` | `49.92%` | `1.00` | 1,980,000.00 USD |
| `4H` | `Gate` | `39.94%` | `60.06%` | `0.67` | 407,050.00 USD |
| `4H` | `Bitget` | `49.43%` | `50.57%` | `0.98` | 2,080,000.00 USD |
| `4H` | `BingX` | `37.83%` | `62.17%` | `0.61` | 2,090,000.00 USD |
| `4H` | `MEXC` | `52.83%` | `47.17%` | `1.12` | 823,120.00 USD |
| `4H` | `Bitunix` | `41.55%` | `58.45%` | `0.71` | 281,790.00 USD |
| `4H` | `Hyperliquid` | `64.23%` | `35.77%` | `1.80` | 243,480.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.9%` | `50.1%` | `1.00` | 832,510.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `37.84%` | `62.16%` | `0.61` | 296,610.00 USD |
| `4H` | `HTX` | `39.64%` | `60.36%` | `0.66` | 4,180.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `98.21%` | `1.79%` | `54.87` | 2,340.00 USD |
| `4H` | `Aster` | `20.88%` | `79.12%` | `0.26` | 82,880.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `11.82%` | `88.18%` | `0.13` | 11,610.00 USD |
| `4H` | `Whale Positions` | `49.93%` | `50.07%` | `1.00` | 6,840,000.00 USD |
| `4H` | `Global Accounts` | `48.42%` | `51.58%` | `0.94` | 20,070,000.00 USD |


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
| `5m` | -239,840.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -151,390.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -348,440.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -444,980.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -209,490.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,260,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,580,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,100,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,360,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -386,710.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -70,430,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,570,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-239.84K` | 15m=`-151.39K` | 1h=`-444.98K` | 24h=`-386.71K`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26462.50` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26380.10` (Risk Distance: `82.40` pts)
  * +2.5R Take Profit: `26668.50`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.82 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26621.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26704.15` (Risk Distance: `82.40` pts)
  * +2.5R Take Profit: `26415.75`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.82 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26754.46`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
