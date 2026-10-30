# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:05:06 IST` (`2026-10-30 05:35:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26662.85` | **Live Ask Quote**: `26665.27` | **Mid Price**: `26664.06`
- **Spread Points**: `242.00` | **Spread BPS**: `0.91 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26664.06` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.66` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26850.71` | Lower -3.00σ Band: `26477.41`
  * Upper +2.51σ Band: `26810.71` | Lower -2.51σ Band: `26517.41`
  * Upper +2.01σ Band: `26776.05` | Lower -2.01σ Band: `26552.07`
  * Upper +2.00σ Band: `26770.72` | Lower -2.00σ Band: `26557.40`
  * Upper +1.28σ Band: `26738.72` | Lower -1.28σ Band: `26589.40`
  * Upper +1.00σ Band: `26717.39` | Lower -1.00σ Band: `26610.73`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26664.06` | EMA-20=`26664.06` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26664.06` (Slope: `+0.0000`) | EMA-100=`26664.06`
  * Institutional Anchors: EMA-144=`26664.06` | EMA-200=`26664.06` (Slope: `+0.0000`) | EMA-233=`26664.06`
- **Range Boundaries**: 24H High=`26930.70` | 24H Low=`26397.42` | Weekly High=`27197.34` | Weekly Low=`26130.78`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26744.05` (Distance: `+0.00%`)
  * Point of Control (POC) = `26664.06` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26584.07` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26770.72` | POC=`26664.06` | VAL=`26557.40`
  * Prior Day Extremes: PDH=`26824.04` | PDL=`26504.08` | PDC=`26664.06`
  * Monday Range Blueprint: High=`26797.38` | Mid=`26664.06` | Low=`26530.74`
  * Developing Weekly Value Area: Weekly VAH=`26877.37` | Weekly POC=`26664.06` | Weekly VAL=`26450.75`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26717.39` | Low=`26610.73`
  * London Session (08:00-16:00 UTC): High=`26770.72` | Low=`26557.40`
  * New York Session (13:00-21:00 UTC): High=`26824.04` | Low=`26504.08`
  * Initial Balance (First Hour): IB High=`26744.05` | IB Low=`26584.07`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26557.40` - `26770.72`
  * Optimal Trade Entry (OTE 0.705): `26717.39`
  * Structural Invalidation Anchor (0.786): `26877.37`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,976,818.52 USD | `6,489.82` | `4185.46` | `4002.70` | `29219.78` | 1,186,132.49 USD | `+4.57%` | `4X Cross` |
| `51` | `0x4692...164f` | `SHORT` | 25,255,956.67 USD | `6,309.73` | `4129.12` | `4002.70` | `13947.36` | 797,703.14 USD | `+3.16%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,495,446.33 USD | `5,869.90` | `4228.86` | `4002.70` | `26898.69` | 1,327,575.61 USD | `+5.65%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,328,665.65 USD | `4,828.91` | `4157.43` | `4002.70` | `2262.56` | -747,216.67 USD | `-3.87%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,215,555.83 USD | `3,551.49` | `4127.82` | `4002.70` | `589.91` | -444,386.12 USD | `-3.13%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,081,676.98 USD | `3,268.21` | `4228.94` | `4002.70` | `4373.26` | 739,402.15 USD | `+5.65%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,607,830.40 USD | `2,900.00` | `4364.92` | `4002.70` | `4235.92` | 1,050,445.93 USD | `+9.05%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,805,940.00 USD | `2,200.00` | `4176.09` | `4002.70` | `2591.25` | -381,479.30 USD | `-4.33%` | `25X Cross` |
| `265` | `0x41e5...0825` | `SHORT` | 8,805,940.00 USD | `2,200.00` | `4112.20` | `4002.70` | `4331.40` | 240,914.59 USD | `+2.74%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,906,809.90 USD | `1,975.37` | `4048.55` | `4002.70` | `6577.79` | 90,581.82 USD | `+1.15%` | `6X Cross` |
| `366` | `0xc26c...b8f4` | `LONG` | 6,324,073.07 USD | `1,579.95` | `4075.62` | `4002.70` | `0.000000` | -115,223.90 USD | `-1.82%` | `1X Cross` |
| `568` | `0x63da...8add` | `LONG` | 4,002,700.00 USD | `1,000.00` | `4021.46` | `4002.70` | `3564.37` | -18,760.96 USD | `-0.47%` | `25X Cross` |
| `576` | `0xf3dc...1672` | `LONG` | 3,939,740.33 USD | `984.27` | `4018.39` | `4002.70` | `2906.64` | -15,446.36 USD | `-0.39%` | `20X Cross` |
| `590` | `0x9aa5...58af` | `LONG` | 3,889,191.43 USD | `971.64` | `4279.98` | `4002.70` | `0.000000` | -269,417.65 USD | `-6.93%` | `20X Cross` |
| `597` | `0x354b...6425` | `LONG` | 3,837,818.38 USD | `958.81` | `4004.93` | `4002.70` | `0.000000` | -2,142.84 USD | `-0.06%` | `10X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,351,859.78 USD | `837.40` | `4599.73` | `4002.70` | `0.000000` | -499,960.60 USD | `-14.92%` | `20X Cross` |
| `830` | `0x0fac...7a0a` | `LONG` | 2,747,793.51 USD | `686.49` | `4290.34` | `4002.70` | `1173.98` | -197,465.19 USD | `-7.19%` | `25X Cross` |
| `911` | `0x625e...a354` | `SHORT` | 2,481,674.00 USD | `620.00` | `4122.81` | `4002.70` | `4342.50` | 74,473.03 USD | `+3.00%` | `20X Cross` |
| `915` | `0xd8c5...99b0` | `SHORT` | 2,475,089.16 USD | `618.35` | `4175.35` | `4002.70` | `34146.89` | 106,763.45 USD | `+4.31%` | `4X Cross` |
| `941` | `0xeae3...e8ad` | `SHORT` | 2,401,620.00 USD | `600.00` | `4104.77` | `4002.70` | `4325.52` | 61,245.11 USD | `+2.55%` | `20X Cross` |
| `942` | `0xf285...fa82` | `LONG` | 2,394,038.49 USD | `598.11` | `4146.45` | `4002.70` | `3891.51` | -85,981.07 USD | `-3.59%` | `25X Cross` |
| `958` | `0x12f7...8750` | `LONG` | 2,344,023.95 USD | `585.61` | `4082.77` | `4002.70` | `2592.20` | -46,893.03 USD | `-2.00%` | `10X Cross` |
| `1097` | `0x413c...886c` | `LONG` | 2,001,350.00 USD | `500.00` | `4010.43` | `4002.70` | `0.000000` | -3,866.23 USD | `-0.19%` | `2X Cross` |
| `1101` | `0x9c06...0560` | `LONG` | 1,995,014.93 USD | `498.42` | `4012.76` | `4002.70` | `0.000000` | -5,016.57 USD | `-0.25%` | `25X Cross` |
| `1105` | `0x61ce...a62b` | `SHORT` | 1,991,357.26 USD | `497.50` | `4071.66` | `4002.70` | `4715.35` | 34,311.53 USD | `+1.72%` | `20X Cross` |
| `1219` | `0xead5...69f2` | `LONG` | 1,816,360.82 USD | `453.78` | `4220.88` | `4002.70` | `3539.20` | -99,007.24 USD | `-5.45%` | `5X Isolated` |
| `1290` | `0x46fc...1195` | `LONG` | 1,689,706.18 USD | `422.14` | `4053.27` | `4002.70` | `2158.19` | -21,348.69 USD | `-1.26%` | `20X Cross` |
| `1353` | `0x6d15...d374` | `LONG` | 1,601,080.00 USD | `400.00` | `4068.25` | `4002.70` | `3842.07` | -26,220.00 USD | `-1.64%` | `25X Cross` |
| `1354` | `0xee02...309d` | `SHORT` | 1,601,080.00 USD | `400.00` | `4438.84` | `4002.70` | `4227.14` | 174,458.60 USD | `+10.90%` | `25X Isolated` |
| `1398` | `0x02a7...fe9f` | `SHORT` | 1,561,053.00 USD | `390.00` | `4055.02` | `4002.70` | `4306.96` | 20,406.25 USD | `+1.31%` | `25X Cross` |
| `1439` | `0x7e77...b8d2` | `SHORT` | 1,521,026.00 USD | `380.00` | `4131.92` | `4002.70` | `4293.77` | 49,103.64 USD | `+3.23%` | `20X Cross` |
| `1461` | `0x72c2...9b37` | `LONG` | 1,493,532.65 USD | `373.13` | `4000.98` | `4002.70` | `3778.31` | 639.14 USD | `+0.04%` | `13X Isolated` |
| `1509` | `0xaa44...b844` | `LONG` | 1,440,972.00 USD | `360.00` | `4043.10` | `4002.70` | `2819.39` | -14,545.63 USD | `-1.01%` | `4X Cross` |
| `1613` | `0xa41f...d50a` | `LONG` | 1,316,736.60 USD | `328.96` | `4468.89` | `4002.70` | `3802.43` | -153,361.25 USD | `-11.65%` | `15X Cross` |
| `1632` | `0x7fda...17d1` | `SHORT` | 1,301,097.25 USD | `325.05` | `4013.13` | `4002.70` | `30486.81` | 3,390.73 USD | `+0.26%` | `20X Cross` |
| `1667` | `0xbf5a...88ba` | `SHORT` | 1,271,477.27 USD | `317.65` | `4091.80` | `4002.70` | `10006.50` | 28,305.76 USD | `+2.23%` | `20X Cross` |
| `1703` | `0xff31...ff6c` | `SHORT` | 1,240,837.00 USD | `310.00` | `4372.43` | `4002.70` | `4789.43` | 114,618.38 USD | `+9.24%` | `10X Isolated` |
| `1727` | `0xada6...6f88` | `LONG` | 1,214,810.64 USD | `303.50` | `4166.46` | `4002.70` | `1786.50` | -49,702.22 USD | `-4.09%` | `5X Cross` |
| `1892` | `0x50e2...d770` | `LONG` | 1,082,199.59 USD | `270.37` | `4243.58` | `4002.70` | `2562.36` | -65,126.87 USD | `-6.02%` | `20X Cross` |
| `1906` | `0x4c92...4f17` | `SHORT` | 1,067,602.15 USD | `266.72` | `4260.98` | `4002.70` | `6518.05` | 68,890.09 USD | `+6.45%` | `20X Cross` |
| `1989` | `0xd346...c4f3` | `LONG` | 1,021,384.17 USD | `255.17` | `4188.66` | `4002.70` | `3310.69` | -47,452.34 USD | `-4.65%` | `5X Isolated` |

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
| `7D` | `3589.40` | 22,450,000.00 USD | 0.00 USD | 22,450,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.60` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 11,560.00 USD | 0.00 USD | 9,080.00 USD |
| `7D` | `3593.70` | 22,380,000.00 USD | 0.00 USD | 22,380,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3595.70` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 20,530.00 USD | 0.00 USD | 21,010.00 USD |
| `7D` | `3598.00` | 22,140,000.00 USD | 0.00 USD | 22,140,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3599.80` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 2,120.00 USD | 0.00 USD | 29,000.00 USD |
| `7D` | `3602.30` | 21,720,000.00 USD | 0.00 USD | 21,720,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3603.90` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 9,260.00 USD | 0.00 USD | 36,140.00 USD |
| `7D` | `3606.60` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3608.00` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 18,250.00 USD | 0.00 USD | 56,790.00 USD |
| `7D` | `3610.90` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.10` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 17,620.00 USD | 0.00 USD | 24,150.00 USD |
| `7D` | `3615.20` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.20` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.50` | 21,180,000.00 USD | 0.00 USD | 21,180,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.30` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 21,740.00 USD | 0.00 USD | 51,390.00 USD |
| `7D` | `3623.80` | 21,070,000.00 USD | 0.00 USD | 21,070,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3624.40` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 20,320.00 USD | 0.00 USD | 50,440.00 USD |
| `7D` | `3628.10` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 47,240.00 USD | 0.00 USD | 35,770.00 USD |
| `1D` | `3628.50` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 8,720.00 USD | 0.00 USD | 22,860.00 USD |
| `7D` | `3632.40` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3632.60` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 1,240.00 USD | 0.00 USD | 7,110.00 USD |
| `1D` | `3636.70` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 586.98 USD | 0.00 USD | 0.00 USD |
| `7D` | `3636.70` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.00` | 20,620,000.00 USD | 0.00 USD | 20,620,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,500,000.00 USD | 0.00 USD | 20,500,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,500,000.00 USD | 0.00 USD | 20,500,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,480,000.00 USD | 0.00 USD | 20,480,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `1D` | `3829.40` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 9,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3830.20` | 20,400,000.00 USD | 0.00 USD | 20,400,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3833.50` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 72,690.00 USD | 0.00 USD | 44,900.00 USD |
| `7D` | `3834.50` | 19,940,000.00 USD | 0.00 USD | 19,940,000.00 USD | 284,980.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3837.60` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 40,820.00 USD | 0.00 USD | 100,510.00 USD |
| `7D` | `3838.80` | 19,090,000.00 USD | 0.00 USD | 19,090,000.00 USD | 311,710.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3841.70` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 30,710.00 USD | 0.00 USD | 86,540.00 USD |
| `7D` | `3843.10` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 291,740.00 USD | 0.00 USD | 359,480.00 USD |
| `1D` | `3845.80` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 35,670.00 USD | 0.00 USD | 113,030.00 USD |
| `7D` | `3847.40` | 17,340,000.00 USD | 0.00 USD | 17,340,000.00 USD | 115,590.00 USD | 0.00 USD | 348,900.00 USD |
| `1D` | `3849.90` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 83,520.00 USD | 0.00 USD | 171,050.00 USD |
| `7D` | `3851.70` | 16,870,000.00 USD | 0.00 USD | 16,870,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3854.00` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 26,780.00 USD | 0.00 USD | 100,600.00 USD |
| `7D` | `3856.00` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3858.10` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 56,980.00 USD | 0.00 USD | 103,190.00 USD |
| `7D` | `3860.30` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3862.20` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 92,710.00 USD | 0.00 USD | 204,510.00 USD |
| `7D` | `3864.60` | 15,840,000.00 USD | 0.00 USD | 15,840,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3866.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 70,490.00 USD | 0.00 USD | 118,050.00 USD |
| `7D` | `3868.90` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 192,180.00 USD | 0.00 USD | 200,860.00 USD |
| `1D` | `3870.40` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 20,190.00 USD | 0.00 USD | 89,450.00 USD |
| `7D` | `3873.20` | 14,970,000.00 USD | 0.00 USD | 14,970,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `1D` | `3874.50` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 2,480.00 USD | 0.00 USD | 17,780.00 USD |
| `7D` | `3877.50` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `1D` | `3878.60` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 3,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3881.80` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,790,000.00 USD | 0.00 USD | 13,790,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `1D` | `3911.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 124,510.00 USD | 0.00 USD | 63,400.00 USD |
| `7D` | `3911.90` | 13,190,000.00 USD | 0.00 USD | 13,190,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3915.50` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 103,180.00 USD | 0.00 USD | 153,230.00 USD |
| `7D` | `3916.20` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 711,980.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3919.60` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 33,350.00 USD | 0.00 USD | 143,610.00 USD |
| `7D` | `3920.50` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 681,530.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3923.70` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 46,300.00 USD | 0.00 USD | 207,900.00 USD |
| `7D` | `3924.80` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 269,290.00 USD | 0.00 USD | 470,810.00 USD |
| `1D` | `3927.80` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 144,350.00 USD | 0.00 USD | 340,070.00 USD |
| `7D` | `3929.10` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 184,740.00 USD | 0.00 USD | 801,220.00 USD |
| `1D` | `3931.90` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 134,290.00 USD | 0.00 USD | 245,580.00 USD |
| `7D` | `3933.40` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3936.00` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 47,570.00 USD | 0.00 USD | 199,420.00 USD |
| `7D` | `3937.70` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3940.10` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 137,950.00 USD | 0.00 USD | 225,000.00 USD |
| `7D` | `3942.00` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3944.20` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 191,390.00 USD | 0.00 USD | 397,630.00 USD |
| `7D` | `3946.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.30` | 451,490.00 USD | 0.00 USD | 451,490.00 USD | 94,290.00 USD | 0.00 USD | 163,130.00 USD |
| `7D` | `3950.60` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 333,580.00 USD | 0.00 USD | 402,490.00 USD |
| `1D` | `3952.40` | 194,060.00 USD | 0.00 USD | 194,060.00 USD | 22,840.00 USD | 0.00 USD | 156,180.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `1D` | `3956.50` | 15,040.00 USD | 0.00 USD | 15,040.00 USD | 8,070.00 USD | 0.00 USD | 4,040.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `1D` | `3960.60` | 2,930.00 USD | 0.00 USD | 2,930.00 USD | 2,930.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `4005.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4005.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4071.30` | 193,530.00 USD | 193,530.00 USD | 0.00 USD | 130,140.00 USD | 0.00 USD | 63,400.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,700.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4075.40` | 444,310.00 USD | 444,310.00 USD | 0.00 USD | 97,550.00 USD | 0.00 USD | 153,230.00 USD |
| `1D` | `4079.50` | 621,270.00 USD | 621,270.00 USD | 0.00 USD | 33,350.00 USD | 0.00 USD | 143,610.00 USD |
| `7D` | `4079.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 657,780.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4083.60` | 854,620.00 USD | 854,620.00 USD | 0.00 USD | 46,300.00 USD | 0.00 USD | 187,040.00 USD |
| `7D` | `4083.90` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 390,080.00 USD | 0.00 USD | 674,150.00 USD |
| `1D` | `4087.70` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 124,370.00 USD | 0.00 USD | 360,930.00 USD |
| `7D` | `4088.20` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 785,900.00 USD |
| `1D` | `4091.80` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 151,970.00 USD | 0.00 USD | 226,210.00 USD |
| `7D` | `4092.50` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4095.90` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 15,590.00 USD | 0.00 USD | 198,250.00 USD |
| `7D` | `4096.80` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4100.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 153,210.00 USD | 0.00 USD | 175,040.00 USD |
| `7D` | `4101.10` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4104.10` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 164,570.00 USD | 0.00 USD | 406,450.00 USD |
| `7D` | `4105.40` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4108.20` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 170,580.00 USD |
| `7D` | `4109.70` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 297,980.00 USD |
| `1D` | `4112.30` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 40,380.00 USD | 0.00 USD | 178,900.00 USD |
| `7D` | `4114.00` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4116.40` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 4,970.00 USD | 0.00 USD | 35,560.00 USD |
| `7D` | `4118.30` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4120.50` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 6,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4122.60` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.20` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4152.70` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.30` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 80,990.00 USD | 0.00 USD | 47,190.00 USD |
| `7D` | `4157.00` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 318,580.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4157.40` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 32,520.00 USD | 0.00 USD | 98,220.00 USD |
| `7D` | `4161.30` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 325,310.00 USD | 0.00 USD | 513,530.00 USD |
| `1D` | `4161.50` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 30,710.00 USD | 0.00 USD | 86,540.00 USD |
| `1D` | `4165.60` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 90,010.00 USD |
| `7D` | `4165.60` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4169.70` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 53,820.00 USD | 0.00 USD | 177,950.00 USD |
| `7D` | `4169.90` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 234,080.00 USD |
| `1D` | `4173.80` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 64,500.00 USD | 0.00 USD | 95,610.00 USD |
| `7D` | `4174.20` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4177.90` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 27,320.00 USD | 0.00 USD | 105,750.00 USD |
| `7D` | `4178.50` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4182.00` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 82,820.00 USD | 0.00 USD | 114,920.00 USD |
| `7D` | `4182.80` | 18,190,000.00 USD | 18,190,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4186.10` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 82,410.00 USD | 0.00 USD | 187,990.00 USD |
| `7D` | `4187.10` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4190.20` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 40,040.00 USD | 0.00 USD | 65,300.00 USD |
| `7D` | `4191.40` | 19,010,000.00 USD | 19,010,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 192,800.00 USD |
| `1D` | `4194.30` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 11,420.00 USD | 0.00 USD | 78,090.00 USD |
| `7D` | `4195.70` | 19,270,000.00 USD | 19,270,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4198.40` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 4,030.00 USD | 0.00 USD | 2,020.00 USD |
| `7D` | `4200.00` | 19,570,000.00 USD | 19,570,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `1D` | `4202.50` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4204.30` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 20,010,000.00 USD | 20,010,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,170,000.00 USD | 20,170,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,320,000.00 USD | 20,320,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,330,000.00 USD | 20,330,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,360,000.00 USD | 20,360,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `7D` | `4389.20` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4391.10` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 22,060.00 USD | 0.00 USD | 12,550.00 USD |
| `7D` | `4393.50` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4395.20` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 23,610.00 USD |
| `7D` | `4397.80` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4399.30` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,490.00 USD |
| `7D` | `4402.10` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `1D` | `4403.40` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 11,380.00 USD | 0.00 USD | 31,900.00 USD |
| `7D` | `4406.40` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `1D` | `4407.40` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 11,440.00 USD | 0.00 USD | 35,650.00 USD |
| `7D` | `4410.70` | 21,450,000.00 USD | 21,450,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `7D` | `4415.00` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,600,000.00 USD | 21,600,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4427.90` | 21,860,000.00 USD | 21,860,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.20` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 35,220.00 USD | 0.00 USD | 33,300.00 USD |
| `7D` | `4435.80` | 21,990,000.00 USD | 21,990,000.00 USD | 0.00 USD | 19,260.00 USD | 0.00 USD | 37,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `800.75M` | Total OI Tokens: `199,983.4 XAUT`
  * 1h OI Change: `-1.04%` | 4h OI Change: `-0.48%` | 24h OI Change: `-6.05%`
  * Exchange Breakdown: Binance=`61.19M` | Bybit=`144.84M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `31.26%` | `68.74%` | `0.45` | 1,670,000.00 USD |
| `15M` | `Binance` | `33.91%` | `66.09%` | `0.51` | 600,750.00 USD |
| `15M` | `OKX` | `35.66%` | `64.34%` | `0.55` | 193,960.00 USD |
| `15M` | `Bybit` | `42.07%` | `57.93%` | `0.73` | 240,960.00 USD |
| `15M` | `KuCoin` | `42.7%` | `57.3%` | `0.75` | 73,620.00 USD |
| `15M` | `Gate` | `25.96%` | `74.04%` | `0.35` | 22,390.00 USD |
| `15M` | `Bitget` | `46.64%` | `53.36%` | `0.87` | 39,410.00 USD |
| `15M` | `BingX` | `2.96%` | `97.04%` | `0.03` | 40,480.00 USD |
| `15M` | `MEXC` | `19.84%` | `80.16%` | `0.25` | 51,930.00 USD |
| `15M` | `Bitunix` | `27.51%` | `72.49%` | `0.38` | 62,820.00 USD |
| `15M` | `Hyperliquid` | `61.38%` | `38.62%` | `1.59` | 29,980.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.15%` | `49.85%` | `1.01` | 298,790.00 USD |
| `15M` | `Crypto.com` | `1.84%` | `98.16%` | `0.02` | 0.10 USD |
| `15M` | `WhiteBIT` | `83.32%` | `16.68%` | `5.00` | 8,420.00 USD |
| `15M` | `HTX` | `29.97%` | `70.03%` | `0.43` | 513.34 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `46.73%` | `53.27%` | `0.88` | 100.53 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `88.56%` | `11.44%` | `7.74` | 4,180.00 USD |
| `15M` | `Whale Positions` | `33.91%` | `66.09%` | `0.51` | 600,750.00 USD |
| `15M` | `Global Accounts` | `31.26%` | `68.74%` | `0.45` | 1,670,000.00 USD |
| `1H` | `XAUT` | `39.40%` | `60.60%` | `0.65` | 19,740,000.00 USD |
| `1H` | `Binance` | `41.07%` | `58.93%` | `0.70` | 7,540,000.00 USD |
| `1H` | `OKX` | `37.38%` | `62.62%` | `0.60` | 4,040,000.00 USD |
| `1H` | `Bybit` | `45.18%` | `54.82%` | `0.82` | 1,840,000.00 USD |
| `1H` | `KuCoin` | `44.21%` | `55.79%` | `0.79` | 96,990.00 USD |
| `1H` | `Gate` | `45.51%` | `54.49%` | `0.84` | 226,760.00 USD |
| `1H` | `Bitget` | `44.79%` | `55.21%` | `0.81` | 1,760,000.00 USD |
| `1H` | `BingX` | `16.73%` | `83.27%` | `0.20` | 1,300,000.00 USD |
| `1H` | `MEXC` | `27.74%` | `72.26%` | `0.38` | 1,480,000.00 USD |
| `1H` | `Bitunix` | `45.16%` | `54.84%` | `0.82` | 343,010.00 USD |
| `1H` | `Hyperliquid` | `50.83%` | `49.17%` | `1.03` | 343,390.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.91%` | `50.09%` | `1.00` | 511,980.00 USD |
| `1H` | `Crypto.com` | `47.03%` | `52.97%` | `0.89` | 7,550.00 USD |
| `1H` | `WhiteBIT` | `79.1%` | `20.9%` | `3.78` | 207,040.00 USD |
| `1H` | `HTX` | `48.5%` | `51.5%` | `0.94` | 2,890.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `75.66%` | `24.34%` | `3.11` | 5,790.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `58.06%` | `41.94%` | `1.38` | 28,380.00 USD |
| `1H` | `Whale Positions` | `41.07%` | `58.93%` | `0.70` | 7,540,000.00 USD |
| `1H` | `Global Accounts` | `39.40%` | `60.60%` | `0.65` | 19,740,000.00 USD |
| `4H` | `XAUT` | `48.30%` | `51.70%` | `0.93` | 51,410,000.00 USD |
| `4H` | `Binance` | `49.14%` | `50.86%` | `0.97` | 20,710,000.00 USD |
| `4H` | `OKX` | `48.75%` | `51.25%` | `0.95` | 9,310,000.00 USD |
| `4H` | `Bybit` | `51.94%` | `48.06%` | `1.08` | 5,200,000.00 USD |
| `4H` | `KuCoin` | `49.12%` | `50.88%` | `0.97` | 389,400.00 USD |
| `4H` | `Gate` | `51.7%` | `48.3%` | `1.07` | 1,430,000.00 USD |
| `4H` | `Bitget` | `47.48%` | `52.52%` | `0.90` | 3,310,000.00 USD |
| `4H` | `BingX` | `28.98%` | `71.02%` | `0.41` | 2,350,000.00 USD |
| `4H` | `MEXC` | `39.83%` | `60.17%` | `0.66` | 3,070,000.00 USD |
| `4H` | `Bitunix` | `47.57%` | `52.43%` | `0.91` | 1,390,000.00 USD |
| `4H` | `Hyperliquid` | `54%` | `46%` | `1.17` | 1,890,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.8%` | `50.2%` | `0.99` | 1,640,000.00 USD |
| `4H` | `Crypto.com` | `44.35%` | `55.65%` | `0.80` | 23,720.00 USD |
| `4H` | `WhiteBIT` | `74.96%` | `25.04%` | `2.99` | 555,750.00 USD |
| `4H` | `HTX` | `27.29%` | `72.71%` | `0.38` | 28,340.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `76.57%` | `23.43%` | `3.27` | 31,470.00 USD |
| `4H` | `Aster` | `76.2%` | `23.8%` | `3.20` | 24,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `54.48%` | `45.52%` | `1.20` | 75,410.00 USD |
| `4H` | `Whale Positions` | `49.14%` | `50.86%` | `0.97` | 20,710,000.00 USD |
| `4H` | `Global Accounts` | `48.30%` | `51.70%` | `0.93` | 51,410,000.00 USD |


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
| `5m` | -14,420.00 USD | 11,990.00 USD | **`DISTRIBUTION`** |
| `15m` | -71,250.00 USD | 33,160.00 USD | **`DISTRIBUTION`** |
| `30m` | -183,320.00 USD | 8,710.00 USD | **`DISTRIBUTION`** |
| `1h` | -158,360.00 USD | -146,300.00 USD | **`DISTRIBUTION`** |
| `2h` | -335,820.00 USD | -667,250.00 USD | **`DISTRIBUTION`** |
| `4h` | -755,560.00 USD | -988,430.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,800,000.00 USD | -2,740,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,050,000.00 USD | -2,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,200,000.00 USD | -1,680,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -411,520.00 USD | -2,360,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -73,780,000.00 USD | -19,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,100,000.00 USD | -85,150,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-14.42K` | 15m=`-71.25K` | 1h=`-158.36K` | 24h=`-411.52K`
* Futures Capital Netflows: 5m=`+11.99K` | 15m=`+33.16K` | 1h=`-146.30K` | 24h=`-2.36M`
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
  * `2026-10-30 10:58:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:58:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:59:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26584.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26500.45` (Risk Distance: `83.62` pts)
  * +2.5R Take Profit: `26793.12`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26744.05` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26827.67` (Risk Distance: `83.62` pts)
  * +2.5R Take Profit: `26535.00`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26877.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
