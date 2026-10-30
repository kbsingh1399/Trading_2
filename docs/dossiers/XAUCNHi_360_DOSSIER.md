# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 10:52:59 IST` (`2026-10-30 05:22:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26619.23` | **Live Ask Quote**: `26621.09` | **Mid Price**: `26620.16`
- **Spread Points**: `186.00` | **Spread BPS**: `0.70 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26620.16` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.55` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26806.50` | Lower -3.00σ Band: `26433.82`
  * Upper +2.51σ Band: `26766.57` | Lower -2.51σ Band: `26473.75`
  * Upper +2.01σ Band: `26731.96` | Lower -2.01σ Band: `26508.36`
  * Upper +2.00σ Band: `26726.64` | Lower -2.00σ Band: `26513.68`
  * Upper +1.28σ Band: `26694.70` | Lower -1.28σ Band: `26545.62`
  * Upper +1.00σ Band: `26673.40` | Lower -1.00σ Band: `26566.92`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26620.16` | EMA-20=`26620.16` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26620.16` (Slope: `+0.0000`) | EMA-100=`26620.16`
  * Institutional Anchors: EMA-144=`26620.16` | EMA-200=`26620.16` (Slope: `+0.0000`) | EMA-233=`26620.16`
- **Range Boundaries**: 24H High=`26886.36` | 24H Low=`26353.96` | Weekly High=`27152.56` | Weekly Low=`26087.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26700.02` (Distance: `+0.00%`)
  * Point of Control (POC) = `26620.16` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26540.30` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26726.64` | POC=`26620.16` | VAL=`26513.68`
  * Prior Day Extremes: PDH=`26779.88` | PDL=`26460.44` | PDC=`26620.16`
  * Monday Range Blueprint: High=`26753.26` | Mid=`26620.16` | Low=`26487.06`
  * Developing Weekly Value Area: Weekly VAH=`26833.12` | Weekly POC=`26620.16` | Weekly VAL=`26407.20`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26673.40` | Low=`26566.92`
  * London Session (08:00-16:00 UTC): High=`26726.64` | Low=`26513.68`
  * New York Session (13:00-21:00 UTC): High=`26779.88` | Low=`26460.44`
  * Initial Balance (First Hour): IB High=`26700.02` | IB Low=`26540.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26513.68` - `26726.64`
  * Optimal Trade Entry (OTE 0.705): `26673.40`
  * Structural Invalidation Anchor (0.786): `26833.12`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,965,785.82 USD | `6,489.82` | `4185.46` | `4000.60` | `29243.65` | 1,197,165.19 USD | `+4.61%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,245,230.13 USD | `6,309.73` | `4129.12` | `4000.60` | `13945.92` | 808,429.68 USD | `+3.20%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,487,228.47 USD | `5,869.90` | `4228.86` | `4000.60` | `26877.59` | 1,335,793.47 USD | `+5.69%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,320,456.51 USD | `4,828.91` | `4157.43` | `4000.60` | `2262.93` | -755,425.81 USD | `-3.91%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,209,518.29 USD | `3,551.49` | `4127.82` | `4000.60` | `591.16` | -450,423.66 USD | `-3.17%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,076,121.01 USD | `3,268.21` | `4228.94` | `4000.60` | `4373.16` | 744,958.12 USD | `+5.70%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,602,900.40 USD | `2,900.00` | `4364.92` | `4000.60` | `4235.92` | 1,055,375.93 USD | `+9.10%` | `20X Cross` |
| `264` | `0x41e5...0825` | `SHORT` | 8,802,860.00 USD | `2,200.00` | `4112.20` | `4000.60` | `4331.40` | 243,994.59 USD | `+2.77%` | `20X Cross` |
| `265` | `0x3678...b209` | `LONG` | 8,802,420.00 USD | `2,200.00` | `4176.09` | `4000.60` | `2594.95` | -384,999.30 USD | `-4.37%` | `25X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,904,044.38 USD | `1,975.37` | `4048.55` | `4000.60` | `6578.70` | 93,347.33 USD | `+1.18%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,321,387.15 USD | `1,579.95` | `4075.62` | `4000.60` | `0.000000` | -117,909.82 USD | `-1.87%` | `1X Cross` |
| `568` | `0x63da...8add` | `LONG` | 4,001,000.00 USD | `1,000.00` | `4021.46` | `4000.60` | `3564.37` | -20,460.96 USD | `-0.51%` | `25X Cross` |
| `577` | `0xf3dc...1672` | `LONG` | 3,938,165.50 USD | `984.27` | `4018.39` | `4000.60` | `2911.94` | -17,021.20 USD | `-0.43%` | `20X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,887,539.64 USD | `971.64` | `4279.98` | `4000.60` | `0.000000` | -271,069.44 USD | `-6.97%` | `20X Cross` |
| `597` | `0x354b...6425` | `LONG` | 3,837,955.55 USD | `959.23` | `4004.93` | `4000.60` | `0.000000` | -3,678.53 USD | `-0.10%` | `10X Cross` |
| `678` | `0x4a20...3c26` | `LONG` | 3,350,519.94 USD | `837.40` | `4599.73` | `4000.60` | `0.000000` | -501,300.44 USD | `-14.96%` | `20X Cross` |
| `831` | `0x0fac...7a0a` | `LONG` | 2,746,626.48 USD | `686.49` | `4290.34` | `4000.60` | `1178.71` | -198,632.22 USD | `-7.23%` | `25X Cross` |
| `910` | `0x625e...a354` | `SHORT` | 2,480,806.00 USD | `620.00` | `4122.81` | `4000.60` | `4342.50` | 75,341.03 USD | `+3.04%` | `20X Cross` |
| `916` | `0xd8c5...99b0` | `SHORT` | 2,474,099.79 USD | `618.35` | `4175.35` | `4000.60` | `34155.67` | 107,752.81 USD | `+4.36%` | `4X Cross` |
| `938` | `0xeae3...e8ad` | `SHORT` | 2,400,660.00 USD | `600.00` | `4104.77` | `4000.60` | `4325.52` | 62,205.11 USD | `+2.59%` | `20X Cross` |
| `941` | `0xf285...fa82` | `LONG` | 2,393,021.71 USD | `598.11` | `4146.45` | `4000.60` | `3891.51` | -86,997.85 USD | `-3.64%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,343,028.41 USD | `585.61` | `4082.77` | `4000.60` | `2595.93` | -47,888.57 USD | `-2.04%` | `10X Cross` |
| `1097` | `0x413c...886c` | `LONG` | 2,000,550.00 USD | `500.00` | `4010.43` | `4000.60` | `0.000000` | -4,666.23 USD | `-0.23%` | `2X Cross` |
| `1101` | `0x9c06...0560` | `LONG` | 1,994,167.62 USD | `498.42` | `4012.76` | `4000.60` | `0.000000` | -5,863.88 USD | `-0.29%` | `25X Cross` |
| `1104` | `0x61ce...a62b` | `SHORT` | 1,990,561.25 USD | `497.50` | `4071.66` | `4000.60` | `4715.24` | 35,107.54 USD | `+1.76%` | `20X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,815,725.52 USD | `453.78` | `4220.88` | `4000.60` | `3539.20` | -99,642.54 USD | `-5.49%` | `5X Isolated` |
| `1288` | `0x46fc...1195` | `LONG` | 1,689,030.76 USD | `422.14` | `4053.27` | `4000.60` | `2161.72` | -22,024.11 USD | `-1.30%` | `20X Cross` |
| `1352` | `0x6d15...d374` | `LONG` | 1,600,520.00 USD | `400.00` | `4068.25` | `4000.60` | `3842.07` | -26,780.00 USD | `-1.67%` | `25X Cross` |
| `1353` | `0xee02...309d` | `SHORT` | 1,600,400.00 USD | `400.00` | `4438.84` | `4000.60` | `4227.14` | 175,138.60 USD | `+10.94%` | `25X Isolated` |
| `1398` | `0x02a7...fe9f` | `SHORT` | 1,560,390.00 USD | `390.00` | `4055.02` | `4000.60` | `4306.96` | 21,069.25 USD | `+1.35%` | `25X Cross` |
| `1442` | `0x7e77...b8d2` | `SHORT` | 1,520,418.00 USD | `380.00` | `4131.92` | `4000.60` | `4293.77` | 49,711.64 USD | `+3.27%` | `20X Cross` |
| `1464` | `0x72c2...9b37` | `LONG` | 1,492,935.64 USD | `373.13` | `4000.98` | `4000.60` | `3778.31` | 42.13 USD | `+0.00%` | `13X Isolated` |
| `1511` | `0xaa44...b844` | `LONG` | 1,440,396.00 USD | `360.00` | `4043.10` | `4000.60` | `2819.07` | -15,121.63 USD | `-1.05%` | `4X Cross` |
| `1617` | `0xa41f...d50a` | `LONG` | 1,316,177.36 USD | `328.96` | `4468.89` | `4000.60` | `3802.43` | -153,920.49 USD | `-11.69%` | `15X Cross` |
| `1634` | `0x7fda...17d1` | `SHORT` | 1,300,544.65 USD | `325.05` | `4013.13` | `4000.60` | `30382.08` | 3,943.32 USD | `+0.30%` | `20X Cross` |
| `1666` | `0xbf5a...88ba` | `SHORT` | 1,270,937.25 USD | `317.65` | `4091.80` | `4000.60` | `10000.26` | 28,845.78 USD | `+2.27%` | `20X Cross` |
| `1701` | `0xff31...ff6c` | `SHORT` | 1,240,341.00 USD | `310.00` | `4372.43` | `4000.60` | `4789.43` | 115,114.38 USD | `+9.28%` | `10X Isolated` |
| `1725` | `0xada6...6f88` | `LONG` | 1,214,325.05 USD | `303.50` | `4166.46` | `4000.60` | `1787.91` | -50,187.82 USD | `-4.13%` | `5X Cross` |
| `1891` | `0x50e2...d770` | `LONG` | 1,081,767.00 USD | `270.37` | `4243.58` | `4000.60` | `2562.36` | -65,559.46 USD | `-6.06%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,067,175.39 USD | `266.72` | `4260.98` | `4000.60` | `6517.93` | 69,316.84 USD | `+6.50%` | `20X Cross` |
| `1990` | `0xd346...c4f3` | `LONG` | 1,020,950.37 USD | `255.17` | `4188.66` | `4000.60` | `3310.69` | -47,886.13 USD | `-4.69%` | `5X Isolated` |

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
| `7D` | `3589.40` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.90` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 14,750.00 USD | 0.00 USD | 9,080.00 USD |
| `7D` | `3593.70` | 22,430,000.00 USD | 0.00 USD | 22,430,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3596.00` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 17,330.00 USD | 0.00 USD | 27,080.00 USD |
| `7D` | `3598.00` | 22,190,000.00 USD | 0.00 USD | 22,190,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3600.10` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 4,790.00 USD | 0.00 USD | 22,930.00 USD |
| `7D` | `3602.30` | 21,770,000.00 USD | 0.00 USD | 21,770,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3604.20` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 6,590.00 USD | 0.00 USD | 33,210.00 USD |
| `7D` | `3606.60` | 21,550,000.00 USD | 0.00 USD | 21,550,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3608.30` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 18,250.00 USD | 0.00 USD | 56,790.00 USD |
| `7D` | `3610.90` | 21,410,000.00 USD | 0.00 USD | 21,410,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.40` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 17,620.00 USD | 0.00 USD | 24,150.00 USD |
| `7D` | `3615.20` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.50` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.50` | 21,240,000.00 USD | 0.00 USD | 21,240,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.60` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 21,740.00 USD | 0.00 USD | 66,750.00 USD |
| `7D` | `3623.80` | 21,120,000.00 USD | 0.00 USD | 21,120,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3624.70` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 22,580.00 USD | 0.00 USD | 37,460.00 USD |
| `7D` | `3628.10` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 47,240.00 USD | 0.00 USD | 35,770.00 USD |
| `1D` | `3628.80` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 6,460.00 USD | 0.00 USD | 20,480.00 USD |
| `7D` | `3632.40` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3632.90` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 1,240.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3636.70` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3637.00` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 586.98 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.00` | 20,670,000.00 USD | 0.00 USD | 20,670,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,510,000.00 USD | 0.00 USD | 20,510,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `1D` | `3829.70` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 9,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.20` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3833.80` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 78,750.00 USD | 0.00 USD | 47,190.00 USD |
| `7D` | `3834.50` | 19,990,000.00 USD | 0.00 USD | 19,990,000.00 USD | 284,980.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3837.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 34,760.00 USD | 0.00 USD | 98,220.00 USD |
| `7D` | `3838.80` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 311,710.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3842.00` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 30,710.00 USD | 0.00 USD | 81,260.00 USD |
| `7D` | `3843.10` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 291,740.00 USD | 0.00 USD | 359,460.00 USD |
| `1D` | `3846.10` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 46,430.00 USD | 0.00 USD | 174,630.00 USD |
| `7D` | `3847.40` | 17,390,000.00 USD | 0.00 USD | 17,390,000.00 USD | 115,590.00 USD | 0.00 USD | 348,900.00 USD |
| `1D` | `3850.20` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 79,720.00 USD | 0.00 USD | 112,280.00 USD |
| `7D` | `3851.70` | 16,920,000.00 USD | 0.00 USD | 16,920,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3854.30` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 19,810.00 USD | 0.00 USD | 100,310.00 USD |
| `7D` | `3856.00` | 16,530,000.00 USD | 0.00 USD | 16,530,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3858.40` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 71,290.00 USD | 0.00 USD | 110,300.00 USD |
| `7D` | `3860.30` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3862.50` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 79,980.00 USD | 0.00 USD | 216,780.00 USD |
| `7D` | `3864.60` | 15,890,000.00 USD | 0.00 USD | 15,890,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3866.60` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 68,910.00 USD | 0.00 USD | 103,390.00 USD |
| `7D` | `3868.90` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 192,180.00 USD | 0.00 USD | 217,610.00 USD |
| `1D` | `3870.70` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 20,190.00 USD | 0.00 USD | 80,140.00 USD |
| `7D` | `3873.20` | 15,010,000.00 USD | 0.00 USD | 15,010,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `1D` | `3874.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 4,030.00 USD | 0.00 USD | 17,780.00 USD |
| `7D` | `3877.50` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `1D` | `3878.90` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 2,320.00 USD | 0.00 USD | 916.89 USD |
| `7D` | `3881.80` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `1D` | `3911.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 130,140.00 USD | 0.00 USD | 63,400.00 USD |
| `7D` | `3911.90` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3915.80` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 102,000.00 USD | 0.00 USD | 153,230.00 USD |
| `7D` | `3916.20` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 711,980.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3919.90` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 42,250.00 USD | 0.00 USD | 143,610.00 USD |
| `7D` | `3920.50` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 681,530.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3924.00` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 42,110.00 USD | 0.00 USD | 193,270.00 USD |
| `7D` | `3924.80` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 269,290.00 USD | 0.00 USD | 470,770.00 USD |
| `1D` | `3928.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 135,190.00 USD | 0.00 USD | 372,070.00 USD |
| `7D` | `3929.10` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 184,740.00 USD | 0.00 USD | 801,220.00 USD |
| `1D` | `3932.20` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 134,290.00 USD | 0.00 USD | 235,900.00 USD |
| `7D` | `3933.40` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3936.30` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 54,440.00 USD | 0.00 USD | 177,100.00 USD |
| `7D` | `3937.70` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3940.40` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 148,460.00 USD | 0.00 USD | 225,000.00 USD |
| `7D` | `3942.00` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3944.50` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 188,220.00 USD | 0.00 USD | 430,160.00 USD |
| `7D` | `3946.30` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.60` | 408,290.00 USD | 0.00 USD | 408,290.00 USD | 80,080.00 USD | 0.00 USD | 130,600.00 USD |
| `7D` | `3950.60` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 333,580.00 USD | 0.00 USD | 435,970.00 USD |
| `1D` | `3952.70` | 197,600.00 USD | 0.00 USD | 197,600.00 USD | 22,840.00 USD | 0.00 USD | 156,180.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `1D` | `3956.80` | 18,590.00 USD | 0.00 USD | 18,590.00 USD | 8,070.00 USD | 0.00 USD | 4,040.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `1D` | `3960.90` | 6,480.00 USD | 0.00 USD | 6,480.00 USD | 4,640.00 USD | 0.00 USD | 1,830.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `3999.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3999.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4071.60` | 209,010.00 USD | 209,010.00 USD | 0.00 USD | 145,610.00 USD | 0.00 USD | 63,400.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,700.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4075.70` | 470,490.00 USD | 470,490.00 USD | 0.00 USD | 86,530.00 USD | 0.00 USD | 174,960.00 USD |
| `7D` | `4079.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 657,780.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4079.80` | 621,270.00 USD | 621,270.00 USD | 0.00 USD | 28,900.00 USD | 0.00 USD | 121,880.00 USD |
| `1D` | `4083.90` | 860,840.00 USD | 860,840.00 USD | 0.00 USD | 46,300.00 USD | 0.00 USD | 193,270.00 USD |
| `7D` | `4083.90` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 390,080.00 USD | 0.00 USD | 674,120.00 USD |
| `1D` | `4088.00` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 132,000.00 USD | 0.00 USD | 340,070.00 USD |
| `7D` | `4088.20` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 785,900.00 USD |
| `1D` | `4092.10` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 245,580.00 USD |
| `7D` | `4092.50` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4096.20` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 20,600.00 USD | 0.00 USD | 189,000.00 USD |
| `7D` | `4096.80` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4100.30` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 149,180.00 USD | 0.00 USD | 164,920.00 USD |
| `7D` | `4101.10` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4104.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 169,460.00 USD | 0.00 USD | 406,450.00 USD |
| `7D` | `4105.40` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4108.50` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 114,420.00 USD | 0.00 USD | 203,310.00 USD |
| `7D` | `4109.70` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 331,460.00 USD |
| `1D` | `4112.60` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 40,380.00 USD | 0.00 USD | 146,170.00 USD |
| `7D` | `4114.00` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4116.70` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 4,970.00 USD | 0.00 USD | 35,560.00 USD |
| `7D` | `4118.30` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4120.80` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 7,740.00 USD | 0.00 USD | 1,830.00 USD |
| `7D` | `4122.60` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.50` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 5,780.00 USD |
| `7D` | `4152.70` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.60` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 74,980.00 USD | 0.00 USD | 41,410.00 USD |
| `7D` | `4157.00` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 318,580.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4157.70` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 32,520.00 USD | 0.00 USD | 98,220.00 USD |
| `7D` | `4161.30` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 325,310.00 USD | 0.00 USD | 513,510.00 USD |
| `1D` | `4161.80` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 30,710.00 USD | 0.00 USD | 79,220.00 USD |
| `7D` | `4165.60` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4165.90` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 35,670.00 USD | 0.00 USD | 113,030.00 USD |
| `7D` | `4169.90` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 234,080.00 USD |
| `1D` | `4170.00` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 48,420.00 USD | 0.00 USD | 154,940.00 USD |
| `1D` | `4174.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 58,250.00 USD | 0.00 USD | 104,760.00 USD |
| `7D` | `4174.20` | 17,640,000.00 USD | 17,640,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4178.20` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 28,680.00 USD | 0.00 USD | 103,420.00 USD |
| `7D` | `4178.50` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4182.30` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 90,000.00 USD | 0.00 USD | 123,510.00 USD |
| `7D` | `4182.80` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4186.40` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 77,800.00 USD | 0.00 USD | 183,850.00 USD |
| `7D` | `4187.10` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4190.50` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 36,100.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `4191.40` | 19,060,000.00 USD | 19,060,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 209,540.00 USD |
| `1D` | `4194.60` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 11,420.00 USD | 0.00 USD | 76,570.00 USD |
| `7D` | `4195.70` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4198.70` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 4,030.00 USD | 0.00 USD | 2,020.00 USD |
| `7D` | `4200.00` | 19,620,000.00 USD | 19,620,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `1D` | `4202.80` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,320.00 USD | 0.00 USD | 916.89 USD |
| `7D` | `4204.30` | 19,850,000.00 USD | 19,850,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,250,000.00 USD | 20,250,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `7D` | `4389.20` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4391.40` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 22,060.00 USD | 0.00 USD | 12,550.00 USD |
| `7D` | `4393.50` | 20,770,000.00 USD | 20,770,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4395.50` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 23,610.00 USD |
| `7D` | `4397.80` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4399.60` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD | 22,930.00 USD |
| `7D` | `4402.10` | 21,320,000.00 USD | 21,320,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `1D` | `4403.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 9,260.00 USD | 0.00 USD | 27,520.00 USD |
| `7D` | `4406.40` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `7D` | `4410.70` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `7D` | `4415.00` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4427.90` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.20` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 35,220.00 USD | 0.00 USD | 33,300.00 USD |
| `7D` | `4435.80` | 22,040,000.00 USD | 22,040,000.00 USD | 0.00 USD | 19,260.00 USD | 0.00 USD | 37,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `803.69M` | Total OI Tokens: `200,838.4 XAUT`
  * 1h OI Change: `-0.78%` | 4h OI Change: `-0.14%` | 24h OI Change: `-5.71%`
  * Exchange Breakdown: Binance=`61.18M` | Bybit=`144.68M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `44.29%` | `55.71%` | `0.80` | 5,350,000.00 USD |
| `15M` | `Binance` | `43.21%` | `56.79%` | `0.76` | 1,940,000.00 USD |
| `15M` | `OKX` | `37.78%` | `62.22%` | `0.61` | 1,380,000.00 USD |
| `15M` | `Bybit` | `37.12%` | `62.88%` | `0.59` | 499,130.00 USD |
| `15M` | `KuCoin` | `37.84%` | `62.16%` | `0.61` | 25,080.00 USD |
| `15M` | `Gate` | `63.37%` | `36.63%` | `1.73` | 64,730.00 USD |
| `15M` | `Bitget` | `48.23%` | `51.77%` | `0.93` | 578,120.00 USD |
| `15M` | `BingX` | `50.8%` | `49.2%` | `1.03` | 67,010.00 USD |
| `15M` | `MEXC` | `42.38%` | `57.62%` | `0.74` | 264,360.00 USD |
| `15M` | `Bitunix` | `62.17%` | `37.83%` | `1.64` | 117,200.00 USD |
| `15M` | `Hyperliquid` | `79.66%` | `20.34%` | `3.92` | 120,250.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.13%` | `49.87%` | `1.01` | 134,600.00 USD |
| `15M` | `Crypto.com` | `44.28%` | `55.72%` | `0.79` | 2,140.00 USD |
| `15M` | `WhiteBIT` | `78.09%` | `21.91%` | `3.56` | 133,820.00 USD |
| `15M` | `HTX` | `32.58%` | `67.42%` | `0.48` | 788.52 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `97.56%` | `2.44%` | `39.98` | 1,010.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `8.91%` | `91.09%` | `0.10` | 8,230.00 USD |
| `15M` | `Whale Positions` | `43.21%` | `56.79%` | `0.76` | 1,940,000.00 USD |
| `15M` | `Global Accounts` | `44.29%` | `55.71%` | `0.80` | 5,350,000.00 USD |
| `1H` | `XAUT` | `44.12%` | `55.88%` | `0.79` | 18,200,000.00 USD |
| `1H` | `Binance` | `45.46%` | `54.54%` | `0.83` | 7,550,000.00 USD |
| `1H` | `OKX` | `38.69%` | `61.31%` | `0.63` | 3,830,000.00 USD |
| `1H` | `Bybit` | `47.43%` | `52.57%` | `0.90` | 1,730,000.00 USD |
| `1H` | `KuCoin` | `49.65%` | `50.35%` | `0.99` | 107,140.00 USD |
| `1H` | `Gate` | `55.64%` | `44.36%` | `1.25` | 229,180.00 USD |
| `1H` | `Bitget` | `46.39%` | `53.61%` | `0.87` | 1,450,000.00 USD |
| `1H` | `BingX` | `44.81%` | `55.19%` | `0.81` | 549,600.00 USD |
| `1H` | `MEXC` | `32.47%` | `67.53%` | `0.48` | 1,320,000.00 USD |
| `1H` | `Bitunix` | `48.86%` | `51.14%` | `0.96` | 318,480.00 USD |
| `1H` | `Hyperliquid` | `50.11%` | `49.89%` | `1.00` | 342,450.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.8%` | `50.2%` | `0.99` | 518,850.00 USD |
| `1H` | `Crypto.com` | `45.04%` | `54.96%` | `0.82` | 8,100.00 USD |
| `1H` | `WhiteBIT` | `75.16%` | `24.84%` | `3.03` | 208,050.00 USD |
| `1H` | `HTX` | `58.79%` | `41.21%` | `1.43` | 1,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `78.26%` | `21.74%` | `3.60` | 6,080.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.86%` | `46.14%` | `1.17` | 26,300.00 USD |
| `1H` | `Whale Positions` | `45.46%` | `54.54%` | `0.83` | 7,550,000.00 USD |
| `1H` | `Global Accounts` | `44.12%` | `55.88%` | `0.79` | 18,200,000.00 USD |
| `4H` | `XAUT` | `49.31%` | `50.69%` | `0.97` | 50,330,000.00 USD |
| `4H` | `Binance` | `49.37%` | `50.63%` | `0.98` | 20,700,000.00 USD |
| `4H` | `OKX` | `49.14%` | `50.86%` | `0.97` | 9,140,000.00 USD |
| `4H` | `Bybit` | `51.8%` | `48.2%` | `1.07` | 5,180,000.00 USD |
| `4H` | `KuCoin` | `49.88%` | `50.12%` | `1.00` | 395,220.00 USD |
| `4H` | `Gate` | `51.87%` | `48.13%` | `1.08` | 1,470,000.00 USD |
| `4H` | `Bitget` | `49.17%` | `50.83%` | `0.97` | 2,970,000.00 USD |
| `4H` | `BingX` | `43.95%` | `56.05%` | `0.78` | 1,540,000.00 USD |
| `4H` | `MEXC` | `41.76%` | `58.24%` | `0.72` | 3,040,000.00 USD |
| `4H` | `Bitunix` | `48.52%` | `51.48%` | `0.94` | 1,380,000.00 USD |
| `4H` | `Hyperliquid` | `49.63%` | `50.37%` | `0.99` | 2,090,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.9%` | `50.1%` | `1.00` | 1,690,000.00 USD |
| `4H` | `Crypto.com` | `44.96%` | `55.04%` | `0.82` | 26,800.00 USD |
| `4H` | `WhiteBIT` | `75.85%` | `24.15%` | `3.14` | 548,600.00 USD |
| `4H` | `HTX` | `27.5%` | `72.5%` | `0.38` | 28,570.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44%` | `56%` | `0.79` | 57,200.00 USD |
| `4H` | `Aster` | `72.34%` | `27.66%` | `2.62` | 26,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.17%` | `47.83%` | `1.09` | 71,260.00 USD |
| `4H` | `Whale Positions` | `49.37%` | `50.63%` | `0.98` | 20,700,000.00 USD |
| `4H` | `Global Accounts` | `49.31%` | `50.69%` | `0.97` | 50,330,000.00 USD |


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
| `5m` | -24,040.00 USD | -59,680.00 USD | **`DISTRIBUTION`** |
| `15m` | -687.97 USD | -126,400.00 USD | **`DISTRIBUTION`** |
| `30m` | 76,750.00 USD | -132,770.00 USD | **`DISTRIBUTION`** |
| `1h` | 164,740.00 USD | -45,560.00 USD | **`ACCUMULATION`** |
| `2h` | -283,650.00 USD | -770,950.00 USD | **`DISTRIBUTION`** |
| `4h` | -338,980.00 USD | -708,900.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,640,000.00 USD | -2,870,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,770,000.00 USD | -2,520,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,210,000.00 USD | -1,810,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -305,480.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -75,140,000.00 USD | -19,960,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,360,000.00 USD | -85,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-24.04K` | 15m=`-687.97` | 1h=`+164.74K` | 24h=`-305.48K`
* Futures Capital Netflows: 5m=`-59.68K` | 15m=`-126.40K` | 1h=`-45.56K` | 24h=`-2.48M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26540.30` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26457.65` (Risk Distance: `82.65` pts)
  * +2.5R Take Profit: `26746.93`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26700.02` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26782.67` (Risk Distance: `82.65` pts)
  * +2.5R Take Profit: `26493.39`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26833.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
