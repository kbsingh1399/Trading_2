# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 00:47:28 IST` (`2026-10-29 19:17:28 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26704.25` | **Live Ask Quote**: `26706.45` | **Mid Price**: `26705.35`
- **Spread Points**: `220.00` | **Spread BPS**: `0.82 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26705.35` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.76` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26892.29` | Lower -3.00σ Band: `26518.41`
  * Upper +2.51σ Band: `26852.23` | Lower -2.51σ Band: `26558.47`
  * Upper +2.01σ Band: `26817.51` | Lower -2.01σ Band: `26593.19`
  * Upper +2.00σ Band: `26812.17` | Lower -2.00σ Band: `26598.53`
  * Upper +1.28σ Band: `26780.12` | Lower -1.28σ Band: `26630.58`
  * Upper +1.00σ Band: `26758.76` | Lower -1.00σ Band: `26651.94`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26705.35` | EMA-20=`26705.35` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26705.35` (Slope: `+0.0000`) | EMA-100=`26705.35`
  * Institutional Anchors: EMA-144=`26705.35` | EMA-200=`26705.35` (Slope: `+0.0000`) | EMA-233=`26705.35`
- **Range Boundaries**: 24H High=`26972.40` | 24H Low=`26438.30` | Weekly High=`27239.46` | Weekly Low=`26171.24`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26785.47` (Distance: `+0.00%`)
  * Point of Control (POC) = `26705.35` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26625.23` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26812.17` | POC=`26705.35` | VAL=`26598.53`
  * Prior Day Extremes: PDH=`26865.58` | PDL=`26545.12` | PDC=`26705.35`
  * Monday Range Blueprint: High=`26838.88` | Mid=`26705.35` | Low=`26571.82`
  * Developing Weekly Value Area: Weekly VAH=`26918.99` | Weekly POC=`26705.35` | Weekly VAL=`26491.71`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26758.76` | Low=`26651.94`
  * London Session (08:00-16:00 UTC): High=`26812.17` | Low=`26598.53`
  * New York Session (13:00-21:00 UTC): High=`26865.58` | Low=`26545.12`
  * Initial Balance (First Hour): IB High=`26785.47` | IB Low=`26625.23`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26598.53` - `26812.17`
  * Optimal Trade Entry (OTE 0.705): `26758.76`
  * Structural Invalidation Anchor (0.786): `26918.99`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,569,795.03 USD | `6,373.65` | `4191.43` | `4011.40` | `29487.42` | 1,144,954.17 USD | `+4.48%` | `4X Cross` |
| `55` | `0x4692...164f` | `SHORT` | 25,353,309.07 USD | `6,319.68` | `4133.85` | `4011.40` | `13326.01` | 771,372.36 USD | `+3.04%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,935,698.90 USD | `5,717.06` | `4234.49` | `4011.40` | `27856.40` | 1,273,176.33 USD | `+5.55%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,372,608.70 USD | `4,828.91` | `4157.43` | `4011.40` | `2103.11` | -703,273.61 USD | `-3.63%` | `25X Cross` |
| `147` | `0x645b...87b8` | `LONG` | 14,108,122.55 USD | `3,516.66` | `4129.63` | `4011.40` | `309.51` | -414,388.32 USD | `-2.94%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,111,417.72 USD | `3,268.21` | `4228.94` | `4011.40` | `4410.40` | 709,661.41 USD | `+5.41%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,634,220.40 USD | `2,900.00` | `4364.92` | `4011.40` | `4235.62` | 1,024,055.93 USD | `+8.80%` | `20X Cross` |
| `275` | `0x41e5...0825` | `SHORT` | 8,826,180.00 USD | `2,200.00` | `4112.20` | `4011.40` | `4331.10` | 220,674.59 USD | `+2.50%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,825,960.00 USD | `2,200.00` | `4176.09` | `4011.40` | `2476.50` | -361,459.30 USD | `-4.10%` | `25X Cross` |
| `308` | `0xfc66...ca06` | `SHORT` | 7,971,003.70 USD | `1,986.89` | `4032.86` | `4011.40` | `25072.27` | 41,862.47 USD | `+0.53%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,924,785.76 USD | `1,975.37` | `4048.55` | `4011.40` | `6507.99` | 72,605.96 USD | `+0.92%` | `6X Cross` |
| `381` | `0xc26c...b8f4` | `LONG` | 6,338,450.63 USD | `1,579.95` | `4075.62` | `4011.40` | `0.000000` | -100,846.34 USD | `-1.59%` | `1X Cross` |
| `419` | `0x12d2...f97f` | `LONG` | 5,624,314.12 USD | `1,401.94` | `4278.91` | `4011.40` | `2555.83` | -374,476.45 USD | `-6.66%` | `20X Cross` |
| `573` | `0x63da...8add` | `LONG` | 4,011,800.00 USD | `1,000.00` | `4021.46` | `4011.40` | `3564.06` | -9,660.96 USD | `-0.24%` | `25X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,898,033.38 USD | `971.64` | `4279.98` | `4011.40` | `0.000000` | -260,575.71 USD | `-6.68%` | `20X Cross` |
| `625` | `0xf3dc...1672` | `LONG` | 3,733,585.28 USD | `930.74` | `4024.62` | `4011.40` | `3337.54` | -12,307.28 USD | `-0.33%` | `20X Cross` |
| `686` | `0x4a20...3c26` | `LONG` | 3,359,480.12 USD | `837.40` | `4599.73` | `4011.40` | `0.000000` | -492,340.27 USD | `-14.66%` | `20X Cross` |
| `765` | `0x354b...6425` | `LONG` | 3,076,173.31 USD | `766.88` | `4035.05` | `4011.40` | `0.000000` | -18,217.92 USD | `-0.59%` | `10X Cross` |
| `846` | `0x0fac...7a0a` | `LONG` | 2,754,040.52 USD | `686.49` | `4290.34` | `4011.40` | `1291.95` | -191,218.18 USD | `-6.94%` | `25X Cross` |
| `885` | `0xd8c5...99b0` | `SHORT` | 2,576,999.39 USD | `642.35` | `4175.35` | `4011.40` | `32112.67` | 105,061.79 USD | `+4.08%` | `4X Cross` |
| `920` | `0x625e...a354` | `SHORT` | 2,487,316.00 USD | `620.00` | `4122.81` | `4011.40` | `4342.20` | 68,831.03 USD | `+2.77%` | `20X Cross` |
| `948` | `0xeae3...e8ad` | `SHORT` | 2,407,080.00 USD | `600.00` | `4104.77` | `4011.40` | `4325.22` | 55,785.11 USD | `+2.32%` | `20X Cross` |
| `952` | `0xf285...fa82` | `LONG` | 2,399,481.25 USD | `598.11` | `4146.45` | `4011.40` | `3891.19` | -80,538.30 USD | `-3.36%` | `25X Cross` |
| `969` | `0x12f7...8750` | `LONG` | 2,349,353.01 USD | `585.61` | `4082.77` | `4011.40` | `2176.55` | -41,563.97 USD | `-1.77%` | `10X Cross` |
| `1130` | `0x413c...886c` | `LONG` | 2,005,900.00 USD | `500.00` | `4010.43` | `4011.40` | `0.000000` | 683.77 USD | `+0.03%` | `2X Cross` |
| `1140` | `0x61ce...a62b` | `SHORT` | 1,995,785.04 USD | `497.50` | `4071.66` | `4011.40` | `4693.32` | 29,883.75 USD | `+1.50%` | `20X Cross` |
| `1144` | `0x0593...40f9` | `LONG` | 1,990,562.89 USD | `496.18` | `4024.57` | `4011.40` | `3701.68` | -6,340.94 USD | `-0.32%` | `10X Isolated` |
| `1262` | `0xead5...69f2` | `LONG` | 1,820,490.25 USD | `453.78` | `4220.88` | `4011.40` | `3538.89` | -94,877.81 USD | `-5.21%` | `5X Isolated` |
| `1386` | `0x46fc...1195` | `LONG` | 1,632,754.12 USD | `407.03` | `4055.53` | `4011.40` | `1942.67` | -17,965.69 USD | `-1.10%` | `20X Cross` |
| `1423` | `0x6d15...d374` | `LONG` | 1,604,720.00 USD | `400.00` | `4068.25` | `4011.40` | `3841.76` | -22,580.00 USD | `-1.41%` | `25X Cross` |
| `1424` | `0xee02...309d` | `SHORT` | 1,604,720.00 USD | `400.00` | `4438.84` | `4011.40` | `4226.84` | 170,818.60 USD | `+10.64%` | `25X Isolated` |
| `1450` | `0x02a7...fe9f` | `SHORT` | 1,564,602.00 USD | `390.00` | `4055.02` | `4011.40` | `4306.66` | 16,857.25 USD | `+1.08%` | `25X Cross` |
| `1487` | `0x7e77...b8d2` | `SHORT` | 1,524,484.00 USD | `380.00` | `4131.92` | `4011.40` | `4293.46` | 45,645.64 USD | `+2.99%` | `20X Cross` |
| `1506` | `0x72c2...9b37` | `LONG` | 1,496,853.52 USD | `373.13` | `4000.98` | `4011.40` | `3777.99` | 3,960.01 USD | `+0.26%` | `13X Isolated` |
| `1542` | `0xaa44...b844` | `LONG` | 1,444,104.00 USD | `360.00` | `4043.10` | `4011.40` | `2803.21` | -11,413.63 USD | `-0.79%` | `4X Cross` |
| `1655` | `0xa41f...d50a` | `LONG` | 1,319,730.15 USD | `328.96` | `4468.89` | `4011.40` | `3833.14` | -150,367.70 USD | `-11.39%` | `15X Cross` |
| `1682` | `0x49e9...e1d0` | `SHORT` | 1,297,885.40 USD | `323.56` | `4025.23` | `4011.40` | `28363.38` | 4,507.30 USD | `+0.35%` | `4X Cross` |
| `1704` | `0xada6...6f88` | `LONG` | 1,280,806.00 USD | `319.28` | `4166.46` | `4011.40` | `1875.80` | -49,444.51 USD | `-3.86%` | `5X Cross` |
| `1716` | `0xbf5a...88ba` | `SHORT` | 1,274,367.93 USD | `317.65` | `4091.80` | `4011.40` | `10476.44` | 25,415.10 USD | `+1.99%` | `20X Cross` |
| `1734` | `0xff31...ff6c` | `SHORT` | 1,243,658.00 USD | `310.00` | `4372.43` | `4011.40` | `4789.13` | 111,797.38 USD | `+8.99%` | `10X Isolated` |
| `1901` | `0x50e2...d770` | `LONG` | 1,084,659.94 USD | `270.37` | `4243.58` | `4011.40` | `2562.05` | -62,666.53 USD | `-5.78%` | `20X Cross` |
| `1914` | `0x4c92...4f17` | `SHORT` | 1,069,895.94 USD | `266.72` | `4260.98` | `4011.40` | `6520.25` | 66,596.29 USD | `+6.22%` | `20X Cross` |
| `1988` | `0xd346...c4f3` | `LONG` | 1,023,706.25 USD | `255.17` | `4188.66` | `4011.40` | `3310.37` | -45,130.26 USD | `-4.41%` | `5X Isolated` |
| `2029` | `0x1581...463b` | `LONG` | 1,002,950.00 USD | `250.00` | `4003.77` | `4011.40` | `3504.59` | 2,006.41 USD | `+0.20%` | `15X Cross` |
| `2030` | `0xe47f...758c` | `LONG` | 1,002,950.00 USD | `250.00` | `4020.00` | `4011.40` | `3774.29` | -2,050.00 USD | `-0.20%` | `20X Cross` |

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
| `7D` | `3605.10` | 22,740,000.00 USD | 0.00 USD | 22,740,000.00 USD | 33,130.00 USD | 0.00 USD | 129,270.00 USD |
| `1D` | `3606.30` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `3609.30` | 22,570,000.00 USD | 0.00 USD | 22,570,000.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `3610.50` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 4,870.00 USD | 0.00 USD | 25,000.00 USD |
| `7D` | `3613.50` | 22,500,000.00 USD | 0.00 USD | 22,500,000.00 USD | 84,000.00 USD | 0.00 USD | 67,380.00 USD |
| `1D` | `3614.70` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 7,480.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `3617.70` | 22,350,000.00 USD | 0.00 USD | 22,350,000.00 USD | 51,620.00 USD | 0.00 USD | 104,640.00 USD |
| `1D` | `3618.90` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 6,260.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3621.90` | 22,200,000.00 USD | 0.00 USD | 22,200,000.00 USD | 86,890.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `3623.10` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.10` | 21,960,000.00 USD | 0.00 USD | 21,960,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3627.30` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 16,010.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.30` | 21,820,000.00 USD | 0.00 USD | 21,820,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3631.50` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 30,160.00 USD | 0.00 USD | 55,360.00 USD |
| `7D` | `3634.50` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.70` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 30,630.00 USD | 0.00 USD | 13,460.00 USD |
| `7D` | `3638.70` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3644.10` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 14,060.00 USD | 0.00 USD | 10,260.00 USD |
| `7D` | `3647.10` | 21,490,000.00 USD | 0.00 USD | 21,490,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3648.30` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `3651.30` | 21,460,000.00 USD | 0.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3652.50` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 12,890.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.50` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.70` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3659.70` | 21,430,000.00 USD | 0.00 USD | 21,430,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3660.90` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 21,410,000.00 USD | 0.00 USD | 21,410,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 21,260,000.00 USD | 0.00 USD | 21,260,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 20,750,000.00 USD | 0.00 USD | 20,750,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,960,000.00 USD | 0.00 USD | 18,960,000.00 USD | 156,600.00 USD | 0.00 USD | 212,340.00 USD |
| `1D` | `3845.70` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 10,120.00 USD |
| `7D` | `3848.70` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 74,350.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3849.90` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 24,940.00 USD | 0.00 USD | 70,190.00 USD |
| `7D` | `3852.90` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 183,930.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `3854.10` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 10,670.00 USD | 0.00 USD | 53,090.00 USD |
| `7D` | `3857.10` | 17,860,000.00 USD | 0.00 USD | 17,860,000.00 USD | 248,680.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3858.30` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 22,220.00 USD | 0.00 USD | 76,220.00 USD |
| `7D` | `3861.30` | 17,370,000.00 USD | 0.00 USD | 17,370,000.00 USD | 209,570.00 USD | 0.00 USD | 532,590.00 USD |
| `1D` | `3862.50` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 74,720.00 USD | 0.00 USD | 201,260.00 USD |
| `7D` | `3865.50` | 16,630,000.00 USD | 0.00 USD | 16,630,000.00 USD | 203,250.00 USD | 0.00 USD | 370,450.00 USD |
| `1D` | `3866.70` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 55,080.00 USD | 0.00 USD | 107,070.00 USD |
| `7D` | `3869.70` | 16,060,000.00 USD | 0.00 USD | 16,060,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3870.90` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 58,610.00 USD | 0.00 USD | 116,730.00 USD |
| `7D` | `3873.90` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3875.10` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 96,090.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `3878.10` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3879.30` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 54,760.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `3882.30` | 14,980,000.00 USD | 0.00 USD | 14,980,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3883.50` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 33,040.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3886.50` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.70` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 20,650.00 USD | 0.00 USD | 26,060.00 USD |
| `7D` | `3890.70` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.90` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `3894.90` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3896.10` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 26,000.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3899.10` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3900.30` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3903.30` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `3904.50` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3907.50` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 334,680.00 USD | 0.00 USD | 450,920.00 USD |
| `7D` | `3928.50` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3929.70` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 40,090.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.70` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 377,610.00 USD | 0.00 USD | 390,200.00 USD |
| `1D` | `3933.90` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 31,140.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3936.90` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 449,520.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.10` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 37,890.00 USD | 0.00 USD | 142,240.00 USD |
| `7D` | `3941.10` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 320,330.00 USD | 0.00 USD | 783,180.00 USD |
| `1D` | `3942.30` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 129,870.00 USD | 0.00 USD | 384,040.00 USD |
| `7D` | `3945.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 513,380.00 USD | 0.00 USD | 928,940.00 USD |
| `1D` | `3946.50` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 120,480.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.70` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 116,680.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3954.90` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 115,530.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3959.10` | 911,760.00 USD | 0.00 USD | 911,760.00 USD | 165,800.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.30` | 701,850.00 USD | 0.00 USD | 701,850.00 USD | 61,440.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.50` | 633,380.00 USD | 0.00 USD | 633,380.00 USD | 81,110.00 USD | 0.00 USD | 51,280.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.70` | 500,990.00 USD | 0.00 USD | 500,990.00 USD | 55,160.00 USD | 0.00 USD | 83,520.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.90` | 362,310.00 USD | 0.00 USD | 362,310.00 USD | 64,650.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3980.10` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3984.30` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `1D` | `3988.50` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4010.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4010.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 498,640.00 USD |
| `7D` | `4088.10` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4089.30` | 196,680.00 USD | 196,680.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `4092.30` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 286,170.00 USD | 0.00 USD | 391,950.00 USD |
| `1D` | `4093.50` | 304,680.00 USD | 304,680.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 80,080.00 USD |
| `7D` | `4096.50` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 508,690.00 USD |
| `1D` | `4097.70` | 479,260.00 USD | 479,260.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 133,100.00 USD |
| `7D` | `4100.70` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 330,780.00 USD | 0.00 USD | 732,670.00 USD |
| `1D` | `4101.90` | 775,130.00 USD | 775,130.00 USD | 0.00 USD | 87,220.00 USD | 0.00 USD | 208,650.00 USD |
| `7D` | `4104.90` | 10,220,000.00 USD | 10,220,000.00 USD | 0.00 USD | 586,230.00 USD | 0.00 USD | 893,490.00 USD |
| `1D` | `4106.10` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 127,950.00 USD | 0.00 USD | 381,000.00 USD |
| `7D` | `4109.10` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 320,370.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4110.30` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 86,700.00 USD | 0.00 USD | 111,120.00 USD |
| `7D` | `4113.30` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.50` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 153,580.00 USD | 0.00 USD | 269,000.00 USD |
| `7D` | `4117.50` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.70` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 163,150.00 USD | 0.00 USD | 124,080.00 USD |
| `7D` | `4121.70` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.90` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 18,770.00 USD |
| `7D` | `4125.90` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.10` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.10` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.30` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 80,280.00 USD |
| `7D` | `4134.30` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.50` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.70` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 52,000.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4142.70` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.90` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4146.90` | 14,360,000.00 USD | 14,360,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `1D` | `4148.10` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4151.10` | 14,800,000.00 USD | 14,800,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 249,320.00 USD |
| `7D` | `4167.90` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4169.10` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `4172.10` | 17,570,000.00 USD | 17,570,000.00 USD | 0.00 USD | 128,920.00 USD | 0.00 USD | 195,980.00 USD |
| `1D` | `4173.30` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 13,960.00 USD | 0.00 USD | 40,040.00 USD |
| `7D` | `4176.30` | 18,010,000.00 USD | 18,010,000.00 USD | 0.00 USD | 192,580.00 USD | 0.00 USD | 247,170.00 USD |
| `1D` | `4177.50` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 47,860.00 USD |
| `7D` | `4180.50` | 18,490,000.00 USD | 18,490,000.00 USD | 0.00 USD | 175,510.00 USD | 0.00 USD | 304,000.00 USD |
| `1D` | `4181.70` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 29,200.00 USD | 0.00 USD | 86,730.00 USD |
| `7D` | `4184.70` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 293,700.00 USD | 0.00 USD | 419,190.00 USD |
| `1D` | `4185.90` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 75,900.00 USD | 0.00 USD | 203,290.00 USD |
| `7D` | `4188.90` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 169,570.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4190.10` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 41,700.00 USD | 0.00 USD | 73,850.00 USD |
| `7D` | `4193.10` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4194.30` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 79,720.00 USD | 0.00 USD | 139,720.00 USD |
| `7D` | `4197.30` | 20,400,000.00 USD | 20,400,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4198.50` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 81,270.00 USD | 0.00 USD | 60,040.00 USD |
| `7D` | `4201.50` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4202.70` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 39,690.00 USD | 0.00 USD | 9,160.00 USD |
| `7D` | `4205.70` | 20,810,000.00 USD | 20,810,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.90` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.90` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4211.10` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 23,620.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `4214.10` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4215.30` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 35,270.00 USD |
| `7D` | `4218.30` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4219.50` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 37,220.00 USD | 0.00 USD | 31,270.00 USD |
| `7D` | `4222.50` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 13,990.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4226.70` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4227.90` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `1D` | `4232.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4377.90` | 21,280,000.00 USD | 21,280,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,960,000.00 USD | 21,960,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 76,590.00 USD |
| `7D` | `4407.30` | 22,230,000.00 USD | 22,230,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4408.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `4411.50` | 22,300,000.00 USD | 22,300,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `4412.70` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `4415.70` | 22,390,000.00 USD | 22,390,000.00 USD | 0.00 USD | 49,730.00 USD | 0.00 USD | 41,080.00 USD |
| `1D` | `4416.90` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 10,100.00 USD |
| `7D` | `4419.90` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 79,360.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4421.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 14,440.00 USD |
| `7D` | `4424.10` | 22,690,000.00 USD | 22,690,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 103,150.00 USD |
| `1D` | `4425.30` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 11,750.00 USD | 0.00 USD | 59,900.00 USD |
| `1D` | `4426.60` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |
| `7D` | `4428.30` | 22,900,000.00 USD | 22,900,000.00 USD | 0.00 USD | 60,670.00 USD | 0.00 USD | 153,720.00 USD |
| `7D` | `4432.50` | 23,020,000.00 USD | 23,020,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.70` | 23,080,000.00 USD | 23,080,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 23,170,000.00 USD | 23,170,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `843.34M` | Total OI Tokens: `210,281.8 XAUT`
  * 1h OI Change: `-0.48%` | 4h OI Change: `-1.72%` | 24h OI Change: `+3.91%`
  * Exchange Breakdown: Binance=`62.12M` | Bybit=`144.59M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `48.65%` | `51.35%` | `0.95` | 1,490,000.00 USD |
| `15M` | `Binance` | `51.65%` | `48.35%` | `1.07` | 631,010.00 USD |
| `15M` | `OKX` | `53.02%` | `46.98%` | `1.13` | 161,910.00 USD |
| `15M` | `Bybit` | `45.9%` | `54.1%` | `0.85` | 78,870.00 USD |
| `15M` | `KuCoin` | `63.46%` | `36.54%` | `1.74` | 791.75 USD |
| `15M` | `Gate` | `44.83%` | `55.17%` | `0.81` | 146,900.00 USD |
| `15M` | `Bitget` | `5.93%` | `94.07%` | `0.06` | 120,410.00 USD |
| `15M` | `BingX` | `47.45%` | `52.55%` | `0.90` | 80,730.00 USD |
| `15M` | `MEXC` | `60.45%` | `39.55%` | `1.53` | 76,860.00 USD |
| `15M` | `Bitunix` | `59.87%` | `40.13%` | `1.49` | 21,890.00 USD |
| `15M` | `Hyperliquid` | `12.44%` | `87.56%` | `0.14` | 16,590.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.77%` | `49.23%` | `1.03` | 56,800.00 USD |
| `15M` | `Crypto.com` | `98.73%` | `1.27%` | `77.74` | 729.41 USD |
| `15M` | `WhiteBIT` | `76.29%` | `23.71%` | `3.22` | 84,100.00 USD |
| `15M` | `HTX` | `56.8%` | `43.2%` | `1.31` | 92.72 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `25.67%` | `74.33%` | `0.35` | 2,580.00 USD |
| `15M` | `Aster` | `47.08%` | `52.92%` | `0.89` | 649.86 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `96.71%` | `3.29%` | `29.40` | 9,130.00 USD |
| `15M` | `Whale Positions` | `51.65%` | `48.35%` | `1.07` | 631,010.00 USD |
| `15M` | `Global Accounts` | `48.65%` | `51.35%` | `0.95` | 1,490,000.00 USD |
| `1H` | `XAUT` | `51.59%` | `48.41%` | `1.07` | 3,900,000.00 USD |
| `1H` | `Binance` | `50.73%` | `49.27%` | `1.03` | 1,460,000.00 USD |
| `1H` | `OKX` | `48.98%` | `51.02%` | `0.96` | 377,840.00 USD |
| `1H` | `Bybit` | `45.72%` | `54.28%` | `0.84` | 404,430.00 USD |
| `1H` | `KuCoin` | `52.56%` | `47.44%` | `1.11` | 9,120.00 USD |
| `1H` | `Gate` | `54.69%` | `45.31%` | `1.21` | 39,020.00 USD |
| `1H` | `Bitget` | `64.85%` | `35.15%` | `1.84` | 187,890.00 USD |
| `1H` | `BingX` | `50.57%` | `49.43%` | `1.02` | 292,630.00 USD |
| `1H` | `MEXC` | `50.39%` | `49.61%` | `1.02` | 182,150.00 USD |
| `1H` | `Bitunix` | `55.23%` | `44.77%` | `1.23` | 37,770.00 USD |
| `1H` | `Hyperliquid` | `35.9%` | `64.1%` | `0.56` | 14,750.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.72%` | `52.28%` | `0.91` | 753,110.00 USD |
| `1H` | `Crypto.com` | `0%` | `100%` | `0.00` | 548.82 USD |
| `1H` | `WhiteBIT` | `92.54%` | `7.46%` | `12.40` | 135,280.00 USD |
| `1H` | `HTX` | `12.27%` | `87.73%` | `0.14` | 222.87 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `66.65%` | `33.35%` | `2.00` | 5,450.00 USD |
| `1H` | `Aster` | `0%` | `100%` | `0.00` | 5.06 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `17.64%` | `82.36%` | `0.21` | 1,600.00 USD |
| `1H` | `Whale Positions` | `50.73%` | `49.27%` | `1.03` | 1,460,000.00 USD |
| `1H` | `Global Accounts` | `51.59%` | `48.41%` | `1.07` | 3,900,000.00 USD |
| `4H` | `XAUT` | `47.15%` | `52.85%` | `0.89` | 51,430,000.00 USD |
| `4H` | `Binance` | `45.33%` | `54.67%` | `0.83` | 18,800,000.00 USD |
| `4H` | `OKX` | `47.47%` | `52.53%` | `0.90` | 10,250,000.00 USD |
| `4H` | `Bybit` | `48.74%` | `51.26%` | `0.95` | 4,020,000.00 USD |
| `4H` | `KuCoin` | `49.6%` | `50.4%` | `0.98` | 488,010.00 USD |
| `4H` | `Gate` | `48.76%` | `51.24%` | `0.95` | 1,670,000.00 USD |
| `4H` | `Bitget` | `46.59%` | `53.41%` | `0.87` | 2,360,000.00 USD |
| `4H` | `BingX` | `33.92%` | `66.08%` | `0.51` | 2,530,000.00 USD |
| `4H` | `MEXC` | `46.45%` | `53.55%` | `0.87` | 4,560,000.00 USD |
| `4H` | `Bitunix` | `49.65%` | `50.35%` | `0.99` | 1,160,000.00 USD |
| `4H` | `Hyperliquid` | `47.53%` | `52.47%` | `0.91` | 1,470,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.98%` | `51.02%` | `0.96` | 2,450,000.00 USD |
| `4H` | `Crypto.com` | `53.46%` | `46.54%` | `1.15` | 27,240.00 USD |
| `4H` | `WhiteBIT` | `83.64%` | `16.36%` | `5.11` | 1,300,000.00 USD |
| `4H` | `HTX` | `46.9%` | `53.1%` | `0.88` | 9,960.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.99%` | `51.01%` | `0.96` | 155,390.00 USD |
| `4H` | `Aster` | `85.97%` | `14.03%` | `6.13` | 54,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.84%` | `49.16%` | `1.03` | 148,190.00 USD |
| `4H` | `Whale Positions` | `45.33%` | `54.67%` | `0.83` | 18,800,000.00 USD |
| `4H` | `Global Accounts` | `47.15%` | `52.85%` | `0.89` | 51,430,000.00 USD |


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
| `5m` | -66,770.00 USD | 5,030.00 USD | **`DISTRIBUTION`** |
| `15m` | -65,990.00 USD | 63,510.00 USD | **`DISTRIBUTION`** |
| `30m` | -86,080.00 USD | 157,030.00 USD | **`ACCUMULATION`** |
| `1h` | -295,320.00 USD | 179,630.00 USD | **`DISTRIBUTION`** |
| `2h` | -560,860.00 USD | 473,260.00 USD | **`DISTRIBUTION`** |
| `4h` | -621,360.00 USD | 330,460.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,050,000.00 USD | 826,570.00 USD | **`DISTRIBUTION`** |
| `8h` | -237,460.00 USD | 273,400.00 USD | **`ACCUMULATION`** |
| `12h` | 297,110.00 USD | 141,430.00 USD | **`ACCUMULATION`** |
| `24h` | -1,290,000.00 USD | 263,970.00 USD | **`DISTRIBUTION`** |
| `1w` | -82,680,000.00 USD | -20,480,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,230,000.00 USD | -85,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-66.77K` | 15m=`-65.99K` | 1h=`-295.32K` | 24h=`-1.29M`
* Futures Capital Netflows: 5m=`+5.03K` | 15m=`+63.51K` | 1h=`+179.63K` | 24h=`+263.97K`
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
  * `2026-10-30 00:17:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:38:29 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26625.23` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26541.82` (Risk Distance: `83.42` pts)
  * +2.5R Take Profit: `26833.77`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26785.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26868.88` (Risk Distance: `83.42` pts)
  * +2.5R Take Profit: `26576.93`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26918.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
