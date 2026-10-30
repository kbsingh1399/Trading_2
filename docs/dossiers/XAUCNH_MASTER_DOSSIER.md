# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:41:29 IST` (`2026-10-30 06:11:29 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26554.69` | **Live Ask Quote**: `26556.49` | **Mid Price**: `26555.59`
- **Spread Points**: `180.00` | **Spread BPS**: `0.68 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26555.59` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.39` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26741.48` | Lower -3.00σ Band: `26369.70`
  * Upper +2.51σ Band: `26701.65` | Lower -2.51σ Band: `26409.53`
  * Upper +2.01σ Band: `26667.12` | Lower -2.01σ Band: `26444.06`
  * Upper +2.00σ Band: `26661.81` | Lower -2.00σ Band: `26449.37`
  * Upper +1.28σ Band: `26629.95` | Lower -1.28σ Band: `26481.23`
  * Upper +1.00σ Band: `26608.70` | Lower -1.00σ Band: `26502.48`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26555.59` | EMA-20=`26555.59` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26555.59` (Slope: `+0.0000`) | EMA-100=`26555.59`
  * Institutional Anchors: EMA-144=`26555.59` | EMA-200=`26555.59` (Slope: `+0.0000`) | EMA-233=`26555.59`
- **Range Boundaries**: 24H High=`26821.15` | 24H Low=`26290.03` | Weekly High=`27086.70` | Weekly Low=`26024.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26635.26` (Distance: `+0.00%`)
  * Point of Control (POC) = `26555.59` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26475.92` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26661.81` | POC=`26555.59` | VAL=`26449.37`
  * Prior Day Extremes: PDH=`26714.92` | PDL=`26396.26` | PDC=`26555.59`
  * Monday Range Blueprint: High=`26688.37` | Mid=`26555.59` | Low=`26422.81`
  * Developing Weekly Value Area: Weekly VAH=`26768.03` | Weekly POC=`26555.59` | Weekly VAL=`26343.15`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26608.70` | Low=`26502.48`
  * London Session (08:00-16:00 UTC): High=`26661.81` | Low=`26449.37`
  * New York Session (13:00-21:00 UTC): High=`26714.92` | Low=`26396.26`
  * Initial Balance (First Hour): IB High=`26635.26` | IB Low=`26475.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26449.37` - `26661.81`
  * Optimal Trade Entry (OTE 0.705): `26608.70`
  * Structural Invalidation Anchor (0.786): `26768.03`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,900,238.60 USD | `6,489.82` | `4185.46` | `3990.30` | `29612.79` | 1,262,712.41 USD | `+4.88%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,249,740.26 USD | `6,326.83` | `4128.60` | `3990.30` | `14006.81` | 871,238.02 USD | `+3.45%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,426,181.52 USD | `5,869.90` | `4228.86` | `3990.30` | `27257.87` | 1,396,840.42 USD | `+5.96%` | `5X Cross` |
| `102` | `0xec0b...b078` | `LONG` | 19,271,684.55 USD | `4,828.91` | `4157.43` | `3990.30` | `2286.46` | -804,197.77 USD | `-4.17%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,174,685.86 USD | `3,551.75` | `4127.81` | `3990.30` | `632.19` | -486,299.04 USD | `-3.43%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,043,112.06 USD | `3,268.21` | `4228.94` | `3990.30` | `4375.93` | 777,967.07 USD | `+5.96%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,573,610.40 USD | `2,900.00` | `4364.92` | `3990.30` | `4235.94` | 1,084,665.93 USD | `+9.37%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,779,980.00 USD | `2,200.00` | `4176.09` | `3990.30` | `2636.73` | -407,439.30 USD | `-4.64%` | `25X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,779,980.00 USD | `2,200.00` | `4112.20` | `3990.30` | `4331.43` | 266,874.59 USD | `+3.04%` | `20X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,883,105.47 USD | `1,975.37` | `4048.55` | `3990.30` | `6628.22` | 114,286.25 USD | `+1.45%` | `6X Cross` |
| `368` | `0xc26c...b8f4` | `LONG` | 6,305,429.64 USD | `1,579.95` | `4075.62` | `3990.30` | `0.000000` | -133,867.33 USD | `-2.12%` | `1X Cross` |
| `562` | `0x63da...8add` | `LONG` | 3,990,900.00 USD | `1,000.00` | `4021.46` | `3990.30` | `3564.40` | -30,560.96 USD | `-0.77%` | `25X Cross` |
| `571` | `0xf3dc...1672` | `LONG` | 3,928,125.94 USD | `984.27` | `4018.39` | `3990.30` | `2885.31` | -27,060.76 USD | `-0.69%` | `20X Cross` |
| `586` | `0x9aa5...58af` | `LONG` | 3,877,726.06 USD | `971.64` | `4279.98` | `3990.30` | `0.000000` | -280,883.03 USD | `-7.24%` | `20X Cross` |
| `590` | `0x354b...6425` | `LONG` | 3,826,480.51 USD | `958.80` | `4004.93` | `3990.30` | `0.000000` | -13,456.68 USD | `-0.35%` | `10X Cross` |
| `673` | `0x4a20...3c26` | `LONG` | 3,341,978.46 USD | `837.40` | `4599.73` | `3990.30` | `0.000000` | -509,841.92 USD | `-15.26%` | `20X Cross` |
| `826` | `0x0fac...7a0a` | `LONG` | 2,739,692.99 USD | `686.49` | `4290.34` | `3990.30` | `1217.58` | -205,565.72 USD | `-7.50%` | `25X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,474,358.00 USD | `620.00` | `4122.81` | `3990.30` | `4342.53` | 81,789.03 USD | `+3.31%` | `20X Cross` |
| `910` | `0xd8c5...99b0` | `SHORT` | 2,467,792.57 USD | `618.35` | `4175.35` | `3990.30` | `34250.85` | 114,060.03 USD | `+4.62%` | `4X Cross` |
| `931` | `0xeae3...e8ad` | `SHORT` | 2,394,540.00 USD | `600.00` | `4104.77` | `3990.30` | `4325.55` | 68,325.11 USD | `+2.85%` | `20X Cross` |
| `933` | `0xf285...fa82` | `LONG` | 2,386,980.84 USD | `598.11` | `4146.45` | `3990.30` | `3891.53` | -93,038.72 USD | `-3.90%` | `25X Cross` |
| `952` | `0x12f7...8750` | `LONG` | 2,337,113.74 USD | `585.61` | `4082.77` | `3990.30` | `2612.69` | -53,803.24 USD | `-2.30%` | `10X Cross` |
| `1094` | `0x413c...886c` | `LONG` | 1,995,450.00 USD | `500.00` | `4010.43` | `3990.30` | `0.000000` | -9,766.23 USD | `-0.49%` | `2X Cross` |
| `1099` | `0x9c06...0560` | `LONG` | 1,989,133.60 USD | `498.42` | `4012.76` | `3990.30` | `0.000000` | -10,897.90 USD | `-0.55%` | `25X Cross` |
| `1104` | `0x61ce...a62b` | `SHORT` | 1,985,486.72 USD | `497.50` | `4071.66` | `3990.30` | `4718.97` | 40,182.07 USD | `+2.02%` | `20X Cross` |
| `1216` | `0xead5...69f2` | `LONG` | 1,810,915.41 USD | `453.78` | `4220.88` | `3990.30` | `3539.23` | -104,452.65 USD | `-5.77%` | `5X Isolated` |
| `1312` | `0x46fc...1195` | `LONG` | 1,655,716.26 USD | `414.87` | `4053.27` | `3990.30` | `2170.64` | -25,876.59 USD | `-1.56%` | `20X Cross` |
| `1350` | `0x6d15...d374` | `LONG` | 1,596,360.00 USD | `400.00` | `4068.25` | `3990.30` | `3842.10` | -30,940.00 USD | `-1.94%` | `25X Cross` |
| `1351` | `0xee02...309d` | `SHORT` | 1,596,360.00 USD | `400.00` | `4438.84` | `3990.30` | `4227.17` | 179,178.60 USD | `+11.22%` | `25X Isolated` |
| `1394` | `0x02a7...fe9f` | `SHORT` | 1,556,451.00 USD | `390.00` | `4055.02` | `3990.30` | `4306.98` | 25,008.25 USD | `+1.61%` | `25X Cross` |
| `1429` | `0x7e77...b8d2` | `SHORT` | 1,516,542.00 USD | `380.00` | `4131.92` | `3990.30` | `4293.79` | 53,587.64 USD | `+3.53%` | `20X Cross` |
| `1453` | `0x72c2...9b37` | `LONG` | 1,489,129.71 USD | `373.13` | `4000.98` | `3990.30` | `3778.33` | -3,763.81 USD | `-0.25%` | `13X Isolated` |
| `1502` | `0xaa44...b844` | `LONG` | 1,436,724.00 USD | `360.00` | `4043.10` | `3990.30` | `2820.44` | -18,793.63 USD | `-1.31%` | `4X Cross` |
| `1606` | `0xa41f...d50a` | `LONG` | 1,312,789.05 USD | `328.96` | `4468.89` | `3990.30` | `3802.46` | -157,308.80 USD | `-11.98%` | `15X Cross` |
| `1656` | `0xbf5a...88ba` | `SHORT` | 1,267,728.94 USD | `317.65` | `4091.80` | `3990.30` | `9979.35` | 32,054.09 USD | `+2.53%` | `20X Cross` |
| `1689` | `0x7fda...17d1` | `SHORT` | 1,238,961.10 USD | `310.46` | `4013.13` | `3990.30` | `31166.33` | 6,964.05 USD | `+0.56%` | `20X Cross` |
| `1691` | `0xff31...ff6c` | `SHORT` | 1,237,179.00 USD | `310.00` | `4372.43` | `3990.30` | `4789.46` | 118,276.38 USD | `+9.56%` | `10X Isolated` |
| `1713` | `0xada6...6f88` | `LONG` | 1,211,229.37 USD | `303.50` | `4166.46` | `3990.30` | `1793.48` | -53,283.49 USD | `-4.40%` | `5X Cross` |
| `1876` | `0x50e2...d770` | `LONG` | 1,079,009.26 USD | `270.37` | `4243.58` | `3990.30` | `2562.39` | -68,317.20 USD | `-6.33%` | `20X Cross` |
| `1888` | `0x4c92...4f17` | `SHORT` | 1,064,454.84 USD | `266.72` | `4260.98` | `3990.30` | `6506.54` | 72,037.39 USD | `+6.77%` | `20X Cross` |
| `1963` | `0xd346...c4f3` | `LONG` | 1,018,373.12 USD | `255.17` | `4188.66` | `3990.30` | `3310.71` | -50,463.39 USD | `-4.96%` | `5X Isolated` |

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
  * Total Open Interest: `809.49M` | Total OI Tokens: `202,808.7 XAUT`
  * 1h OI Change: `+0.61%` | 4h OI Change: `-0.82%` | 24h OI Change: `-6.94%`
  * Exchange Breakdown: Binance=`61.08M` | Bybit=`144.45M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `37.10%` | `62.90%` | `0.59` | 4,560,000.00 USD |
| `15M` | `Binance` | `43.63%` | `56.37%` | `0.77` | 1,570,000.00 USD |
| `15M` | `OKX` | `32.26%` | `67.74%` | `0.48` | 885,760.00 USD |
| `15M` | `Bybit` | `33.95%` | `66.05%` | `0.51` | 515,620.00 USD |
| `15M` | `KuCoin` | `45.85%` | `54.15%` | `0.85` | 23,880.00 USD |
| `15M` | `Gate` | `27.61%` | `72.39%` | `0.38` | 174,910.00 USD |
| `15M` | `Bitget` | `28.05%` | `71.95%` | `0.39` | 368,060.00 USD |
| `15M` | `BingX` | `49.6%` | `50.4%` | `0.98` | 418,950.00 USD |
| `15M` | `MEXC` | `18.27%` | `81.73%` | `0.22` | 383,620.00 USD |
| `15M` | `Bitunix` | `39.32%` | `60.68%` | `0.65` | 57,720.00 USD |
| `15M` | `Hyperliquid` | `46.6%` | `53.4%` | `0.87` | 34,660.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.37%` | `58.63%` | `0.71` | 89,670.00 USD |
| `15M` | `Crypto.com` | `88.38%` | `11.62%` | `7.61` | 2,150.00 USD |
| `15M` | `WhiteBIT` | `94.46%` | `5.54%` | `17.05` | 23,030.00 USD |
| `15M` | `HTX` | `50.07%` | `49.93%` | `1.00` | 749.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `43.5%` | `56.5%` | `0.77` | 110.83 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `75.32%` | `24.68%` | `3.05` | 2,780.00 USD |
| `15M` | `Whale Positions` | `43.63%` | `56.37%` | `0.77` | 1,570,000.00 USD |
| `15M` | `Global Accounts` | `37.10%` | `62.90%` | `0.59` | 4,560,000.00 USD |
| `1H` | `XAUT` | `40.17%` | `59.83%` | `0.67` | 17,440,000.00 USD |
| `1H` | `Binance` | `45.81%` | `54.19%` | `0.85` | 6,370,000.00 USD |
| `1H` | `OKX` | `37.92%` | `62.08%` | `0.61` | 3,480,000.00 USD |
| `1H` | `Bybit` | `37.81%` | `62.19%` | `0.61` | 1,770,000.00 USD |
| `1H` | `KuCoin` | `43.85%` | `56.15%` | `0.78` | 82,420.00 USD |
| `1H` | `Gate` | `30.79%` | `69.21%` | `0.44` | 430,460.00 USD |
| `1H` | `Bitget` | `43.12%` | `56.88%` | `0.76` | 1,620,000.00 USD |
| `1H` | `BingX` | `23.29%` | `76.71%` | `0.30` | 1,460,000.00 USD |
| `1H` | `MEXC` | `26.05%` | `73.95%` | `0.35` | 1,080,000.00 USD |
| `1H` | `Bitunix` | `47.74%` | `52.26%` | `0.91` | 302,480.00 USD |
| `1H` | `Hyperliquid` | `54.13%` | `45.87%` | `1.18` | 120,880.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.44%` | `50.56%` | `0.98` | 576,700.00 USD |
| `1H` | `Crypto.com` | `48.36%` | `51.64%` | `0.94` | 4,610.00 USD |
| `1H` | `WhiteBIT` | `86.7%` | `13.3%` | `6.52` | 115,700.00 USD |
| `1H` | `HTX` | `51.12%` | `48.88%` | `1.05` | 3,230.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `89.15%` | `10.85%` | `8.22` | 1,960.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.13%` | `49.87%` | `1.01` | 19,210.00 USD |
| `1H` | `Whale Positions` | `45.81%` | `54.19%` | `0.85` | 6,370,000.00 USD |
| `1H` | `Global Accounts` | `40.17%` | `59.83%` | `0.67` | 17,440,000.00 USD |
| `4H` | `XAUT` | `45.91%` | `54.09%` | `0.85` | 23,400,000.00 USD |
| `4H` | `Binance` | `51.42%` | `48.58%` | `1.06` | 8,070,000.00 USD |
| `4H` | `OKX` | `50.7%` | `49.3%` | `1.03` | 2,310,000.00 USD |
| `4H` | `Bybit` | `53.11%` | `46.89%` | `1.13` | 2,750,000.00 USD |
| `4H` | `KuCoin` | `49.65%` | `50.35%` | `0.99` | 1,000,000.00 USD |
| `4H` | `Gate` | `40.33%` | `59.67%` | `0.68` | 310,670.00 USD |
| `4H` | `Bitget` | `52.57%` | `47.43%` | `1.11` | 380,680.00 USD |
| `4H` | `BingX` | `11.68%` | `88.32%` | `0.13` | 2,840,000.00 USD |
| `4H` | `MEXC` | `46.65%` | `53.35%` | `0.87` | 841,710.00 USD |
| `4H` | `Bitunix` | `44.05%` | `55.95%` | `0.79` | 348,910.00 USD |
| `4H` | `Hyperliquid` | `66.15%` | `33.85%` | `1.95` | 154,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.35%` | `51.65%` | `0.94` | 4,130,000.00 USD |
| `4H` | `Crypto.com` | `0.57%` | `99.43%` | `0.01` | 714.95 USD |
| `4H` | `WhiteBIT` | `73.9%` | `26.1%` | `2.83` | 165,450.00 USD |
| `4H` | `HTX` | `54.81%` | `45.19%` | `1.21` | 8,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `2.89%` | `97.11%` | `0.03` | 28,820.00 USD |
| `4H` | `Aster` | `83.63%` | `16.37%` | `5.11` | 567.30 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.9%` | `35.1%` | `1.85` | 50,910.00 USD |
| `4H` | `Whale Positions` | `51.42%` | `48.58%` | `1.06` | 8,070,000.00 USD |
| `4H` | `Global Accounts` | `45.91%` | `54.09%` | `0.85` | 23,400,000.00 USD |


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
| `5m` | 86,550.00 USD | -63,770.00 USD | **`ACCUMULATION`** |
| `15m` | -61,330.00 USD | -266,130.00 USD | **`DISTRIBUTION`** |
| `30m` | -65,240.00 USD | -313,600.00 USD | **`DISTRIBUTION`** |
| `1h` | -263,060.00 USD | -290,190.00 USD | **`DISTRIBUTION`** |
| `2h` | -29,280.00 USD | -364,570.00 USD | **`DISTRIBUTION`** |
| `4h` | -855,050.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,250,000.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,770,000.00 USD | -3,130,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,090,000.00 USD | -2,060,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 81,830.00 USD | -1,100,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -71,110,000.00 USD | -19,750,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,260,000.00 USD | -85,580,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+86.55K` | 15m=`-61.33K` | 1h=`-263.06K` | 24h=`+81.83K`
* Futures Capital Netflows: 5m=`-63.77K` | 15m=`-266.13K` | 1h=`-290.19K` | 24h=`-1.10M`
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
  * Execution Entry: `26475.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26393.56` (Risk Distance: `82.37` pts)
  * +2.5R Take Profit: `26681.84`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.82 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26635.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26717.62` (Risk Distance: `82.37` pts)
  * +2.5R Take Profit: `26429.34`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.82 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26768.03`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
