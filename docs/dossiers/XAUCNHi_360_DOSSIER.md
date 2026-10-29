# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 23:59:02 IST` (`2026-10-29 18:29:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26672.85` | **Live Ask Quote**: `26674.61` | **Mid Price**: `26673.73`
- **Spread Points**: `176.00` | **Spread BPS**: `0.66 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26673.73` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.68` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26860.45` | Lower -3.00σ Band: `26487.01`
  * Upper +2.51σ Band: `26820.44` | Lower -2.51σ Band: `26527.02`
  * Upper +2.01σ Band: `26785.76` | Lower -2.01σ Band: `26561.70`
  * Upper +2.00σ Band: `26780.42` | Lower -2.00σ Band: `26567.04`
  * Upper +1.28σ Band: `26748.42` | Lower -1.28σ Band: `26599.04`
  * Upper +1.00σ Band: `26727.08` | Lower -1.00σ Band: `26620.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26673.73` | EMA-20=`26673.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26673.73` (Slope: `+0.0000`) | EMA-100=`26673.73`
  * Institutional Anchors: EMA-144=`26673.73` | EMA-200=`26673.73` (Slope: `+0.0000`) | EMA-233=`26673.73`
- **Range Boundaries**: 24H High=`26940.47` | 24H Low=`26406.99` | Weekly High=`27207.20` | Weekly Low=`26140.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26753.75` (Distance: `+0.00%`)
  * Point of Control (POC) = `26673.73` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26593.71` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26780.42` | POC=`26673.73` | VAL=`26567.04`
  * Prior Day Extremes: PDH=`26833.77` | PDL=`26513.69` | PDC=`26673.73`
  * Monday Range Blueprint: High=`26807.10` | Mid=`26673.73` | Low=`26540.36`
  * Developing Weekly Value Area: Weekly VAH=`26887.12` | Weekly POC=`26673.73` | Weekly VAL=`26460.34`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26727.08` | Low=`26620.38`
  * London Session (08:00-16:00 UTC): High=`26780.42` | Low=`26567.04`
  * New York Session (13:00-21:00 UTC): High=`26833.77` | Low=`26513.69`
  * Initial Balance (First Hour): IB High=`26753.75` | IB Low=`26593.71`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26567.04` - `26780.42`
  * Optimal Trade Entry (OTE 0.705): `26727.08`
  * Structural Invalidation Anchor (0.786): `26887.12`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:55:43 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,554,498.28 USD | `6,373.65` | `4191.43` | `4008.70` | `29198.47` | 1,160,250.92 USD | `+4.54%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,268,990.71 USD | `6,304.64` | `4134.18` | `4008.70` | `13351.66` | 795,561.75 USD | `+3.15%` | `5X Cross` |
| `72` | `0xb83d...6e36` | `SHORT` | 22,913,974.08 USD | `5,717.06` | `4234.49` | `4008.70` | `27575.99` | 1,294,901.15 USD | `+5.65%` | `5X Cross` |
| `98` | `0xec0b...b078` | `LONG` | 19,356,673.31 USD | `4,828.91` | `4157.43` | `4008.70` | `2084.33` | -719,209.01 USD | `-3.72%` | `25X Cross` |
| `148` | `0x645b...87b8` | `LONG` | 14,086,456.68 USD | `3,514.59` | `4129.70` | `4008.70` | `293.60` | -427,748.58 USD | `-3.04%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,103,574.00 USD | `3,268.21` | `4228.94` | `4008.70` | `4409.11` | 717,505.13 USD | `+5.48%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,627,260.40 USD | `2,900.00` | `4364.92` | `4008.70` | `4235.59` | 1,031,015.93 USD | `+8.87%` | `20X Cross` |
| `274` | `0x41e5...0825` | `SHORT` | 8,818,700.00 USD | `2,200.00` | `4112.20` | `4008.70` | `4331.08` | 228,154.59 USD | `+2.59%` | `20X Cross` |
| `275` | `0x3678...b209` | `LONG` | 8,817,820.00 USD | `2,200.00` | `4176.09` | `4008.70` | `2452.29` | -369,599.30 USD | `-4.19%` | `25X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,963,453.52 USD | `1,986.89` | `4032.86` | `4008.70` | `25142.42` | 49,412.65 USD | `+0.62%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,918,267.04 USD | `1,975.37` | `4048.55` | `4008.70` | `6509.42` | 79,124.68 USD | `+1.00%` | `6X Cross` |
| `383` | `0xc26c...b8f4` | `LONG` | 6,334,658.75 USD | `1,579.95` | `4075.62` | `4008.70` | `0.000000` | -104,638.22 USD | `-1.65%` | `1X Cross` |
| `422` | `0x12d2...f97f` | `LONG` | 5,619,687.71 USD | `1,401.94` | `4278.91` | `4008.70` | `2512.01` | -379,102.87 USD | `-6.75%` | `20X Cross` |
| `576` | `0x63da...8add` | `LONG` | 4,009,400.00 USD | `1,000.00` | `4021.46` | `4008.70` | `3564.03` | -12,060.96 USD | `-0.30%` | `25X Cross` |
| `593` | `0x9aa5...58af` | `LONG` | 3,894,826.96 USD | `971.64` | `4279.98` | `4008.70` | `0.000000` | -263,782.13 USD | `-6.77%` | `20X Cross` |
| `623` | `0xf3dc...1672` | `LONG` | 3,731,816.87 USD | `930.74` | `4024.62` | `4008.70` | `3337.51` | -14,075.70 USD | `-0.38%` | `20X Cross` |
| `686` | `0x4a20...3c26` | `LONG` | 3,356,381.74 USD | `837.40` | `4599.73` | `4008.70` | `0.000000` | -495,438.64 USD | `-14.76%` | `20X Cross` |
| `788` | `0x354b...6425` | `LONG` | 2,967,414.07 USD | `740.35` | `4036.06` | `4008.70` | `0.000000` | -20,701.38 USD | `-0.70%` | `10X Cross` |
| `848` | `0x0fac...7a0a` | `LONG` | 2,751,431.88 USD | `686.49` | `4290.34` | `4008.70` | `1284.84` | -193,826.82 USD | `-7.04%` | `25X Cross` |
| `880` | `0xd8c5...99b0` | `SHORT` | 2,593,035.89 USD | `646.95` | `4175.35` | `4008.70` | `31965.66` | 108,206.88 USD | `+4.17%` | `4X Cross` |
| `919` | `0x625e...a354` | `SHORT` | 2,485,270.00 USD | `620.00` | `4122.81` | `4008.70` | `4342.18` | 70,877.03 USD | `+2.85%` | `20X Cross` |
| `946` | `0xeae3...e8ad` | `SHORT` | 2,404,860.00 USD | `600.00` | `4104.77` | `4008.70` | `4325.20` | 58,005.11 USD | `+2.41%` | `20X Cross` |
| `948` | `0xf285...fa82` | `LONG` | 2,397,985.98 USD | `598.11` | `4146.45` | `4008.70` | `3891.17` | -82,033.57 USD | `-3.42%` | `25X Cross` |
| `967` | `0x12f7...8750` | `LONG` | 2,347,947.54 USD | `585.61` | `4082.77` | `4008.70` | `2197.88` | -42,969.44 USD | `-1.83%` | `10X Cross` |
| `1129` | `0x413c...886c` | `LONG` | 2,004,050.00 USD | `500.00` | `4010.43` | `4008.70` | `0.000000` | -1,166.23 USD | `-0.06%` | `2X Cross` |
| `1133` | `0x61ce...a62b` | `SHORT` | 1,994,690.53 USD | `497.50` | `4071.66` | `4008.70` | `4689.69` | 30,978.26 USD | `+1.55%` | `20X Cross` |
| `1142` | `0x0593...40f9` | `LONG` | 1,988,727.03 USD | `496.18` | `4024.57` | `4008.70` | `3701.65` | -8,176.80 USD | `-0.41%` | `10X Isolated` |
| `1259` | `0xead5...69f2` | `LONG` | 1,818,992.76 USD | `453.78` | `4220.88` | `4008.70` | `3538.86` | -96,375.30 USD | `-5.30%` | `5X Isolated` |
| `1385` | `0x46fc...1195` | `LONG` | 1,631,410.93 USD | `407.03` | `4055.53` | `4008.70` | `1920.30` | -19,308.88 USD | `-1.18%` | `20X Cross` |
| `1420` | `0xee02...309d` | `SHORT` | 1,603,760.00 USD | `400.00` | `4438.84` | `4008.70` | `4226.81` | 171,778.60 USD | `+10.71%` | `25X Isolated` |
| `1421` | `0x6d15...d374` | `LONG` | 1,603,400.00 USD | `400.00` | `4068.25` | `4008.70` | `3841.73` | -23,900.00 USD | `-1.49%` | `25X Cross` |
| `1452` | `0x02a7...fe9f` | `SHORT` | 1,563,666.00 USD | `390.00` | `4055.02` | `4008.70` | `4306.63` | 17,793.25 USD | `+1.14%` | `25X Cross` |
| `1489` | `0x7e77...b8d2` | `SHORT` | 1,523,078.00 USD | `380.00` | `4131.92` | `4008.70` | `4293.44` | 47,051.64 USD | `+3.09%` | `20X Cross` |
| `1505` | `0x72c2...9b37` | `LONG` | 1,495,547.56 USD | `373.13` | `4000.98` | `4008.70` | `3777.97` | 2,654.05 USD | `+0.18%` | `13X Isolated` |
| `1544` | `0xaa44...b844` | `LONG` | 1,442,916.00 USD | `360.00` | `4043.10` | `4008.70` | `2818.46` | -12,601.63 USD | `-0.87%` | `9X Cross` |
| `1653` | `0xa41f...d50a` | `LONG` | 1,318,644.58 USD | `328.96` | `4468.89` | `4008.70` | `3833.11` | -151,453.27 USD | `-11.49%` | `15X Cross` |
| `1686` | `0x49e9...e1d0` | `SHORT` | 1,296,817.66 USD | `323.56` | `4025.23` | `4008.70` | `28500.88` | 5,575.04 USD | `+0.43%` | `4X Cross` |
| `1706` | `0xada6...6f88` | `LONG` | 1,279,688.53 USD | `319.28` | `4166.46` | `4008.70` | `1874.03` | -50,561.98 USD | `-3.95%` | `5X Cross` |
| `1713` | `0xbf5a...88ba` | `SHORT` | 1,273,573.79 USD | `317.65` | `4091.80` | `4008.70` | `10489.13` | 26,209.24 USD | `+2.06%` | `20X Cross` |
| `1729` | `0xff31...ff6c` | `SHORT` | 1,242,511.00 USD | `310.00` | `4372.43` | `4008.70` | `4789.11` | 112,944.38 USD | `+9.09%` | `10X Isolated` |
| `1895` | `0x50e2...d770` | `LONG` | 1,083,659.58 USD | `270.37` | `4243.58` | `4008.70` | `2562.02` | -63,666.88 USD | `-5.88%` | `20X Cross` |
| `1910` | `0x4c92...4f17` | `SHORT` | 1,069,042.44 USD | `266.72` | `4260.98` | `4008.70` | `6526.28` | 67,449.80 USD | `+6.31%` | `20X Cross` |
| `1982` | `0xd346...c4f3` | `LONG` | 1,023,068.32 USD | `255.17` | `4188.66` | `4008.70` | `3310.35` | -45,768.19 USD | `-4.47%` | `5X Isolated` |
| `2020` | `0xe47f...758c` | `LONG` | 1,002,025.00 USD | `250.00` | `4020.00` | `4008.70` | `3774.26` | -2,975.00 USD | `-0.30%` | `20X Cross` |
| `2021` | `0x1581...463b` | `LONG` | 1,002,000.00 USD | `250.00` | `4003.77` | `4008.70` | `3504.56` | 1,056.41 USD | `+0.11%` | `15X Cross` |

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
| `7D` | `3606.60` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 25,640.00 USD | 0.00 USD | 82,740.00 USD |
| `1D` | `3607.80` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 3,070.00 USD | 0.00 USD | 19,930.00 USD |
| `7D` | `3610.80` | 22,690,000.00 USD | 0.00 USD | 22,690,000.00 USD | 41,120.00 USD | 0.00 USD | 61,070.00 USD |
| `1D` | `3612.00` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 4,320.00 USD | 0.00 USD | 11,530.00 USD |
| `7D` | `3615.00` | 22,590,000.00 USD | 0.00 USD | 22,590,000.00 USD | 82,510.00 USD | 0.00 USD | 67,760.00 USD |
| `1D` | `3616.20` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 7,520.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `3619.20` | 22,440,000.00 USD | 0.00 USD | 22,440,000.00 USD | 44,160.00 USD | 0.00 USD | 126,270.00 USD |
| `1D` | `3620.40` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 13,060.00 USD | 0.00 USD | 55,730.00 USD |
| `7D` | `3623.40` | 22,270,000.00 USD | 0.00 USD | 22,270,000.00 USD | 74,730.00 USD | 0.00 USD | 180,770.00 USD |
| `1D` | `3624.60` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 18,900.00 USD | 0.00 USD | 42,570.00 USD |
| `7D` | `3627.60` | 22,010,000.00 USD | 0.00 USD | 22,010,000.00 USD | 69,700.00 USD | 0.00 USD | 52,580.00 USD |
| `1D` | `3628.80` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 31,930.00 USD | 0.00 USD | 35,340.00 USD |
| `7D` | `3631.80` | 21,890,000.00 USD | 0.00 USD | 21,890,000.00 USD | 40,350.00 USD | 0.00 USD | 97,860.00 USD |
| `1D` | `3633.00` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 37,810.00 USD | 0.00 USD | 39,280.00 USD |
| `7D` | `3636.00` | 21,750,000.00 USD | 0.00 USD | 21,750,000.00 USD | 69,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3637.20` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 19,840.00 USD | 0.00 USD | 3,550.00 USD |
| `7D` | `3640.20` | 21,680,000.00 USD | 0.00 USD | 21,680,000.00 USD | 45,100.00 USD | 0.00 USD | 12,090.00 USD |
| `1D` | `3641.40` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 14,220.00 USD | 0.00 USD | 2,430.00 USD |
| `7D` | `3644.40` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 32,450.00 USD | 0.00 USD | 7,240.00 USD |
| `1D` | `3645.60` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 14,170.00 USD | 0.00 USD | 16,060.00 USD |
| `7D` | `3648.60` | 21,580,000.00 USD | 0.00 USD | 21,580,000.00 USD | 7,110.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3649.80` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 13,370.00 USD | 0.00 USD | 13,090.00 USD |
| `7D` | `3652.80` | 21,560,000.00 USD | 0.00 USD | 21,560,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3654.00` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 9,690.00 USD | 0.00 USD | 11,370.00 USD |
| `7D` | `3657.00` | 21,550,000.00 USD | 0.00 USD | 21,550,000.00 USD | 14,670.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3658.20` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 4,300.00 USD | 0.00 USD | 21,380.00 USD |
| `7D` | `3661.20` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3662.40` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3820.80` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.00` | 21,520,000.00 USD | 0.00 USD | 21,520,000.00 USD | 21,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.20` | 21,500,000.00 USD | 0.00 USD | 21,500,000.00 USD | 101,060.00 USD | 0.00 USD | 171,370.00 USD |
| `7D` | `3833.40` | 21,220,000.00 USD | 0.00 USD | 21,220,000.00 USD | 204,730.00 USD | 0.00 USD | 429,430.00 USD |
| `7D` | `3837.60` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 299,300.00 USD | 0.00 USD | 796,720.00 USD |
| `7D` | `3841.80` | 19,490,000.00 USD | 0.00 USD | 19,490,000.00 USD | 327,490.00 USD | 0.00 USD | 311,660.00 USD |
| `7D` | `3846.00` | 18,850,000.00 USD | 0.00 USD | 18,850,000.00 USD | 94,400.00 USD | 0.00 USD | 284,200.00 USD |
| `1D` | `3847.20` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 3,260.00 USD | 0.00 USD | 23,410.00 USD |
| `7D` | `3850.20` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 74,560.00 USD | 0.00 USD | 186,180.00 USD |
| `1D` | `3851.40` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 16,750.00 USD | 0.00 USD | 69,710.00 USD |
| `7D` | `3854.40` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 258,410.00 USD | 0.00 USD | 238,150.00 USD |
| `1D` | `3855.60` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 20,640.00 USD | 0.00 USD | 50,360.00 USD |
| `7D` | `3858.60` | 17,720,000.00 USD | 0.00 USD | 17,720,000.00 USD | 169,730.00 USD | 0.00 USD | 293,860.00 USD |
| `1D` | `3859.80` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 21,380.00 USD | 0.00 USD | 86,730.00 USD |
| `7D` | `3862.80` | 17,250,000.00 USD | 0.00 USD | 17,250,000.00 USD | 305,210.00 USD | 0.00 USD | 507,720.00 USD |
| `1D` | `3864.00` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 85,380.00 USD | 0.00 USD | 211,840.00 USD |
| `7D` | `3867.00` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 169,570.00 USD | 0.00 USD | 337,640.00 USD |
| `1D` | `3868.20` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 60,930.00 USD | 0.00 USD | 70,520.00 USD |
| `7D` | `3871.20` | 15,930,000.00 USD | 0.00 USD | 15,930,000.00 USD | 175,790.00 USD | 0.00 USD | 201,390.00 USD |
| `1D` | `3872.40` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 115,330.00 USD | 0.00 USD | 134,500.00 USD |
| `7D` | `3875.40` | 15,560,000.00 USD | 0.00 USD | 15,560,000.00 USD | 170,610.00 USD | 0.00 USD | 184,350.00 USD |
| `1D` | `3876.60` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 89,250.00 USD | 0.00 USD | 64,570.00 USD |
| `7D` | `3879.60` | 15,200,000.00 USD | 0.00 USD | 15,200,000.00 USD | 235,310.00 USD | 0.00 USD | 18,540.00 USD |
| `1D` | `3880.80` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 34,120.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `3883.80` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 153,020.00 USD | 0.00 USD | 72,260.00 USD |
| `1D` | `3885.00` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 51,780.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3888.00` | 14,720,000.00 USD | 0.00 USD | 14,720,000.00 USD | 47,590.00 USD | 0.00 USD | 97,950.00 USD |
| `1D` | `3889.20` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 32,990.00 USD | 0.00 USD | 44,690.00 USD |
| `7D` | `3892.20` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `3893.40` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 38,650.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3896.40` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 25,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.60` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 26,020.00 USD | 0.00 USD | 34,480.00 USD |
| `7D` | `3900.60` | 14,480,000.00 USD | 0.00 USD | 14,480,000.00 USD | 74,670.00 USD | 0.00 USD | 75,140.00 USD |
| `1D` | `3901.80` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 19,170.00 USD | 0.00 USD | 55,050.00 USD |
| `7D` | `3904.80` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 48,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3906.00` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3909.00` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 202,120.00 USD | 0.00 USD | 342,730.00 USD |
| `7D` | `3913.20` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 409,470.00 USD | 0.00 USD | 858,860.00 USD |
| `7D` | `3917.40` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 598,600.00 USD | 0.00 USD | 1,500,000.00 USD |
| `7D` | `3921.60` | 10,370,000.00 USD | 0.00 USD | 10,370,000.00 USD | 654,980.00 USD | 0.00 USD | 683,960.00 USD |
| `7D` | `3925.80` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 188,800.00 USD | 0.00 USD | 579,920.00 USD |
| `1D` | `3927.00` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 6,530.00 USD | 0.00 USD | 25,460.00 USD |
| `7D` | `3930.00` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 149,120.00 USD | 0.00 USD | 393,350.00 USD |
| `1D` | `3931.20` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 31,210.00 USD | 0.00 USD | 141,410.00 USD |
| `7D` | `3934.20` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 470,890.00 USD | 0.00 USD | 344,800.00 USD |
| `1D` | `3935.40` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 22,890.00 USD | 0.00 USD | 120,090.00 USD |
| `7D` | `3938.40` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 374,080.00 USD | 0.00 USD | 719,210.00 USD |
| `1D` | `3939.60` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 47,700.00 USD | 0.00 USD | 127,510.00 USD |
| `7D` | `3942.60` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 453,980.00 USD | 0.00 USD | 854,580.00 USD |
| `1D` | `3943.80` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 169,070.00 USD | 0.00 USD | 415,470.00 USD |
| `7D` | `3946.80` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 431,550.00 USD | 0.00 USD | 605,510.00 USD |
| `1D` | `3948.00` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 99,960.00 USD | 0.00 USD | 175,940.00 USD |
| `7D` | `3951.00` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 409,730.00 USD | 0.00 USD | 591,600.00 USD |
| `1D` | `3952.20` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 248,080.00 USD | 0.00 USD | 288,250.00 USD |
| `7D` | `3955.20` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 321,600.00 USD | 0.00 USD | 410,530.00 USD |
| `1D` | `3956.40` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 189,260.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `3959.40` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 424,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3960.60` | 806,620.00 USD | 0.00 USD | 806,620.00 USD | 79,390.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `3963.60` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 277,440.00 USD | 0.00 USD | 181,590.00 USD |
| `1D` | `3964.80` | 708,910.00 USD | 0.00 USD | 708,910.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `3969.00` | 613,430.00 USD | 0.00 USD | 613,430.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `3972.00` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 97,260.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `3973.20` | 491,840.00 USD | 0.00 USD | 491,840.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `7D` | `3976.20` | 354,040.00 USD | 0.00 USD | 354,040.00 USD | 66,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3977.40` | 340,020.00 USD | 0.00 USD | 340,020.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `3980.40` | 287,140.00 USD | 0.00 USD | 287,140.00 USD | 106,350.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `3981.60` | 217,870.00 USD | 0.00 USD | 217,870.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `3984.60` | 64,940.00 USD | 0.00 USD | 64,940.00 USD | 30,500.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `3985.80` | 27,730.00 USD | 0.00 USD | 27,730.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4007.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4007.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4064.40` | 24,220.00 USD | 24,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,220.00 USD |
| `7D` | `4068.60` | 458,640.00 USD | 458,640.00 USD | 0.00 USD | 115,900.00 USD | 0.00 USD | 318,510.00 USD |
| `7D` | `4072.80` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 385,550.00 USD | 0.00 USD | 801,820.00 USD |
| `7D` | `4077.00` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 609,590.00 USD | 0.00 USD | 1,480,000.00 USD |
| `7D` | `4081.20` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 628,480.00 USD | 0.00 USD | 706,940.00 USD |
| `7D` | `4085.40` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 188,370.00 USD | 0.00 USD | 539,830.00 USD |
| `1D` | `4086.60` | 6,530.00 USD | 6,530.00 USD | 0.00 USD | 6,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4089.60` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 122,280.00 USD | 0.00 USD | 306,250.00 USD |
| `1D` | `4090.80` | 151,060.00 USD | 151,060.00 USD | 0.00 USD | 25,450.00 USD | 0.00 USD | 119,080.00 USD |
| `7D` | `4093.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 354,750.00 USD | 0.00 USD | 379,560.00 USD |
| `1D` | `4095.00` | 270,670.00 USD | 270,670.00 USD | 0.00 USD | 21,350.00 USD | 0.00 USD | 98,260.00 USD |
| `7D` | `4098.00` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 462,870.00 USD | 0.00 USD | 439,630.00 USD |
| `1D` | `4099.20` | 437,580.00 USD | 437,580.00 USD | 0.00 USD | 37,890.00 USD | 0.00 USD | 129,020.00 USD |
| `7D` | `4102.20` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 364,620.00 USD | 0.00 USD | 926,810.00 USD |
| `1D` | `4103.40` | 955,450.00 USD | 955,450.00 USD | 0.00 USD | 139,880.00 USD | 0.00 USD | 377,980.00 USD |
| `7D` | `4106.40` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 454,550.00 USD | 0.00 USD | 785,310.00 USD |
| `1D` | `4107.60` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 110,470.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `4110.60` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 491,660.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `4111.80` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 169,530.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `4114.80` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 234,080.00 USD | 0.00 USD | 346,150.00 USD |
| `1D` | `4116.00` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 180,480.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `4119.00` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 403,440.00 USD | 0.00 USD | 286,230.00 USD |
| `1D` | `4120.20` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 161,750.00 USD | 0.00 USD | 42,280.00 USD |
| `7D` | `4123.20` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 379,850.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `4124.40` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 40,760.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `4127.40` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 217,580.00 USD |
| `1D` | `4128.60` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 106,820.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `4131.60` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `1D` | `4132.80` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 62,730.00 USD | 0.00 USD | 84,400.00 USD |
| `7D` | `4135.80` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `4137.00` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 77,300.00 USD | 0.00 USD | 38,680.00 USD |
| `7D` | `4140.00` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4141.20` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 52,040.00 USD | 0.00 USD | 68,970.00 USD |
| `7D` | `4144.20` | 14,230,000.00 USD | 14,230,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `1D` | `4145.40` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 38,340.00 USD | 0.00 USD | 110,090.00 USD |
| `7D` | `4148.40` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.60` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4152.60` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 192,770.00 USD | 0.00 USD | 400,910.00 USD |
| `7D` | `4156.80` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 282,060.00 USD | 0.00 USD | 705,560.00 USD |
| `7D` | `4161.00` | 16,780,000.00 USD | 16,780,000.00 USD | 0.00 USD | 306,320.00 USD | 0.00 USD | 389,380.00 USD |
| `7D` | `4165.20` | 17,090,000.00 USD | 17,090,000.00 USD | 0.00 USD | 108,280.00 USD | 0.00 USD | 194,750.00 USD |
| `7D` | `4169.40` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 68,430.00 USD | 0.00 USD | 228,290.00 USD |
| `1D` | `4170.60` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 15,990.00 USD | 0.00 USD | 55,590.00 USD |
| `7D` | `4173.60` | 17,740,000.00 USD | 17,740,000.00 USD | 0.00 USD | 180,310.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `4174.80` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 10,670.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `4177.80` | 18,190,000.00 USD | 18,190,000.00 USD | 0.00 USD | 215,160.00 USD | 0.00 USD | 233,300.00 USD |
| `1D` | `4179.00` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 18,940.00 USD | 0.00 USD | 67,240.00 USD |
| `7D` | `4182.00` | 18,750,000.00 USD | 18,750,000.00 USD | 0.00 USD | 169,770.00 USD | 0.00 USD | 391,590.00 USD |
| `1D` | `4183.20` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 47,600.00 USD | 0.00 USD | 131,360.00 USD |
| `7D` | `4186.20` | 19,430,000.00 USD | 19,430,000.00 USD | 0.00 USD | 240,030.00 USD | 0.00 USD | 443,220.00 USD |
| `1D` | `4187.40` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 74,410.00 USD | 0.00 USD | 165,490.00 USD |
| `7D` | `4190.40` | 19,880,000.00 USD | 19,880,000.00 USD | 0.00 USD | 211,880.00 USD | 0.00 USD | 239,940.00 USD |
| `1D` | `4191.60` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 85,780.00 USD | 0.00 USD | 55,210.00 USD |
| `7D` | `4194.60` | 20,180,000.00 USD | 20,180,000.00 USD | 0.00 USD | 113,440.00 USD | 0.00 USD | 183,710.00 USD |
| `1D` | `4195.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 91,270.00 USD | 0.00 USD | 153,920.00 USD |
| `7D` | `4198.80` | 20,590,000.00 USD | 20,590,000.00 USD | 0.00 USD | 225,250.00 USD | 0.00 USD | 184,350.00 USD |
| `1D` | `4200.00` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 77,180.00 USD | 0.00 USD | 43,100.00 USD |
| `7D` | `4203.00` | 20,780,000.00 USD | 20,780,000.00 USD | 0.00 USD | 171,420.00 USD | 0.00 USD | 18,540.00 USD |
| `1D` | `4204.20` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 25,200.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4207.20` | 21,010,000.00 USD | 21,010,000.00 USD | 0.00 USD | 153,020.00 USD | 0.00 USD | 72,260.00 USD |
| `1D` | `4208.40` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 45,230.00 USD | 0.00 USD | 13,910.00 USD |
| `7D` | `4211.40` | 21,100,000.00 USD | 21,100,000.00 USD | 0.00 USD | 47,590.00 USD | 0.00 USD | 51,400.00 USD |
| `1D` | `4212.60` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 27,670.00 USD | 0.00 USD | 33,590.00 USD |
| `7D` | `4215.60` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `4216.80` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 44,440.00 USD | 0.00 USD | 32,720.00 USD |
| `7D` | `4219.80` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4221.00` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 26,000.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `4224.00` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 46,450.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `4225.20` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `4228.20` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `4229.40` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4379.40` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4383.60` | 21,390,000.00 USD | 21,390,000.00 USD | 0.00 USD | 6,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4387.80` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 36,240.00 USD | 0.00 USD | 45,030.00 USD |
| `7D` | `4392.00` | 21,640,000.00 USD | 21,640,000.00 USD | 0.00 USD | 58,490.00 USD | 0.00 USD | 116,070.00 USD |
| `7D` | `4396.20` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 80,970.00 USD | 0.00 USD | 210,210.00 USD |
| `7D` | `4400.40` | 22,150,000.00 USD | 22,150,000.00 USD | 0.00 USD | 102,130.00 USD | 0.00 USD | 112,920.00 USD |
| `7D` | `4404.60` | 22,240,000.00 USD | 22,240,000.00 USD | 0.00 USD | 37,920.00 USD | 0.00 USD | 53,740.00 USD |
| `7D` | `4408.80` | 22,350,000.00 USD | 22,350,000.00 USD | 0.00 USD | 16,390.00 USD | 0.00 USD | 95,130.00 USD |
| `1D` | `4410.00` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 3,070.00 USD | 0.00 USD | 19,930.00 USD |
| `7D` | `4413.00` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 41,120.00 USD | 0.00 USD | 48,680.00 USD |
| `1D` | `4414.20` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4417.20` | 22,560,000.00 USD | 22,560,000.00 USD | 0.00 USD | 55,550.00 USD | 0.00 USD | 64,890.00 USD |
| `1D` | `4418.40` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `4421.40` | 22,700,000.00 USD | 22,700,000.00 USD | 0.00 USD | 51,620.00 USD | 0.00 USD | 80,320.00 USD |
| `1D` | `4422.60` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 3,510.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `4425.60` | 22,910,000.00 USD | 22,910,000.00 USD | 0.00 USD | 73,250.00 USD | 0.00 USD | 137,930.00 USD |
| `1D` | `4426.40` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 15,790.00 USD | 0.00 USD | 55,540.00 USD |
| `7D` | `4429.80` | 23,050,000.00 USD | 23,050,000.00 USD | 0.00 USD | 50,900.00 USD | 0.00 USD | 95,480.00 USD |
| `7D` | `4434.00` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 39,790.00 USD | 0.00 USD | 48,750.00 USD |
| `7D` | `4438.20` | 23,250,000.00 USD | 23,250,000.00 USD | 0.00 USD | 34,650.00 USD | 0.00 USD | 75,620.00 USD |
| `7D` | `4440.30` | 23,290,000.00 USD | 23,290,000.00 USD | 0.00 USD | 19,430.00 USD | 0.00 USD | 22,240.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `844.28M` | Total OI Tokens: `210,693.5 XAUT`
  * 1h OI Change: `+0.34%` | 4h OI Change: `-2.71%` | 24h OI Change: `+5.35%`
  * Exchange Breakdown: Binance=`62.10M` | Bybit=`144.54M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `42.59%` | `57.41%` | `0.74` | 1,920,000.00 USD |
| `15M` | `Binance` | `64.44%` | `35.56%` | `1.81` | 826,740.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 319,920.00 USD |
| `15M` | `Bybit` | `40.17%` | `59.83%` | `0.67` | 144,020.00 USD |
| `15M` | `KuCoin` | `31.16%` | `68.84%` | `0.45` | 31,480.00 USD |
| `15M` | `Gate` | `44.94%` | `55.06%` | `0.82` | 136,120.00 USD |
| `15M` | `Bitget` | `37.65%` | `62.35%` | `0.60` | 62,590.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 37,260.00 USD |
| `15M` | `MEXC` | `35.48%` | `64.52%` | `0.55` | 82,280.00 USD |
| `15M` | `Bitunix` | `77.73%` | `22.27%` | `3.49` | 38,110.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 17,730.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `42.43%` | `57.57%` | `0.74` | 96,650.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 3,430.00 USD |
| `15M` | `WhiteBIT` | `0.28%` | `99.72%` | `0.00` | 75,830.00 USD |
| `15M` | `HTX` | `16.85%` | `83.15%` | `0.20` | 170.67 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `81.86%` | `18.14%` | `4.51` | 36,880.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 1,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 7,120.00 USD |
| `15M` | `Whale Positions` | `64.44%` | `35.56%` | `1.81` | 826,740.00 USD |
| `15M` | `Global Accounts` | `42.59%` | `57.41%` | `0.74` | 1,920,000.00 USD |
| `1H` | `XAUT` | `45.97%` | `54.03%` | `0.85` | 10,570,000.00 USD |
| `1H` | `Binance` | `48.19%` | `51.81%` | `0.93` | 4,340,000.00 USD |
| `1H` | `OKX` | `45.65%` | `54.35%` | `0.84` | 1,730,000.00 USD |
| `1H` | `Bybit` | `50.3%` | `49.7%` | `1.01` | 813,220.00 USD |
| `1H` | `KuCoin` | `46.47%` | `53.53%` | `0.87` | 133,710.00 USD |
| `1H` | `Gate` | `48.07%` | `51.93%` | `0.93` | 456,300.00 USD |
| `1H` | `Bitget` | `37.11%` | `62.89%` | `0.59` | 447,640.00 USD |
| `1H` | `BingX` | `15.34%` | `84.66%` | `0.18` | 623,740.00 USD |
| `1H` | `MEXC` | `46.75%` | `53.25%` | `0.88` | 818,170.00 USD |
| `1H` | `Bitunix` | `45.47%` | `54.53%` | `0.83` | 168,360.00 USD |
| `1H` | `Hyperliquid` | `41.44%` | `58.56%` | `0.71` | 196,730.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.6%` | `50.4%` | `0.98` | 495,440.00 USD |
| `1H` | `Crypto.com` | `67.78%` | `32.22%` | `2.10` | 7,570.00 USD |
| `1H` | `WhiteBIT` | `83.42%` | `16.58%` | `5.03` | 264,070.00 USD |
| `1H` | `HTX` | `10.14%` | `89.86%` | `0.11` | 2,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.1%` | `80.9%` | `0.24` | 56,200.00 USD |
| `1H` | `Aster` | `9.84%` | `90.16%` | `0.11` | 2,790.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.35%` | `67.65%` | `0.48` | 30,370.00 USD |
| `1H` | `Whale Positions` | `48.19%` | `51.81%` | `0.93` | 4,340,000.00 USD |
| `1H` | `Global Accounts` | `45.97%` | `54.03%` | `0.85` | 10,570,000.00 USD |
| `4H` | `XAUT` | `49.44%` | `50.56%` | `0.98` | 75,700,000.00 USD |
| `4H` | `Binance` | `54.19%` | `45.81%` | `1.18` | 5,830,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.58%` | `50.42%` | `0.98` | 5,810,000.00 USD |
| `4H` | `KuCoin` | `50.42%` | `49.58%` | `1.02` | 441,350.00 USD |
| `4H` | `Gate` | `49.19%` | `50.81%` | `0.97` | 1,740,000.00 USD |
| `4H` | `Bitget` | `44.37%` | `55.63%` | `0.80` | 2,370,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `49.48%` | `50.52%` | `0.98` | 49,990,000.00 USD |
| `4H` | `Bitunix` | `57.89%` | `42.11%` | `1.37` | 2,120,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.74%` | `46.26%` | `1.16` | 5,620,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.13%` | `90.87%` | `0.10` | 1,560,000.00 USD |
| `4H` | `HTX` | `92.19%` | `7.81%` | `11.80` | 67,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.98%` | `50.02%` | `1.00` | 128,750.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.19%` | `45.81%` | `1.18` | 5,830,000.00 USD |
| `4H` | `Global Accounts` | `49.44%` | `50.56%` | `0.98` | 75,700,000.00 USD |


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
| `5m` | -87,180.00 USD | -12,280.00 USD | **`DISTRIBUTION`** |
| `15m` | -113,090.00 USD | 23,360.00 USD | **`DISTRIBUTION`** |
| `30m` | -305,670.00 USD | 493,970.00 USD | **`ACCUMULATION`** |
| `1h` | -300,450.00 USD | 316,930.00 USD | **`ACCUMULATION`** |
| `2h` | -534,990.00 USD | 230,610.00 USD | **`DISTRIBUTION`** |
| `4h` | -574,740.00 USD | 352,790.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,270,000.00 USD | 494,770.00 USD | **`DISTRIBUTION`** |
| `8h` | 299,600.00 USD | 257,590.00 USD | **`ACCUMULATION`** |
| `12h` | 1,880,000.00 USD | 1,190,000.00 USD | **`ACCUMULATION`** |
| `24h` | -1,180,000.00 USD | 464,140.00 USD | **`DISTRIBUTION`** |
| `1w` | -84,330,000.00 USD | -20,950,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,170,000.00 USD | -85,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-87.18K` | 15m=`-113.09K` | 1h=`-300.45K` | 24h=`-1.18M`
* Futures Capital Netflows: 5m=`-12.28K` | 15m=`+23.36K` | 1h=`+316.93K` | 24h=`+464.14K`
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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26593.71` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26511.05` (Risk Distance: `82.66` pts)
  * +2.5R Take Profit: `26800.36`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26753.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26836.41` (Risk Distance: `82.66` pts)
  * +2.5R Take Profit: `26547.10`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26887.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
