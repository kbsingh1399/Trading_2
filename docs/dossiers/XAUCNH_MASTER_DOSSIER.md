# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26773.53` | **Live Ask Quote**: `26775.33` | **Mid Price**: `26774.43`
- **Spread Points**: `180.00` | **Spread BPS**: `0.67 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26774.43` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.94` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26961.85` | Lower -3.00σ Band: `26587.01`
  * Upper +2.51σ Band: `26921.69` | Lower -2.51σ Band: `26627.17`
  * Upper +2.01σ Band: `26886.88` | Lower -2.01σ Band: `26661.98`
  * Upper +2.00σ Band: `26881.53` | Lower -2.00σ Band: `26667.33`
  * Upper +1.28σ Band: `26849.40` | Lower -1.28σ Band: `26699.46`
  * Upper +1.00σ Band: `26827.98` | Lower -1.00σ Band: `26720.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26774.43` | EMA-20=`26774.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26774.43` (Slope: `+0.0000`) | EMA-100=`26774.43`
  * Institutional Anchors: EMA-144=`26774.43` | EMA-200=`26774.43` (Slope: `+0.0000`) | EMA-233=`26774.43`
- **Range Boundaries**: 24H High=`27042.17` | 24H Low=`26506.69` | Weekly High=`27309.92` | Weekly Low=`26238.94`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26854.75` (Distance: `+0.00%`)
  * Point of Control (POC) = `26774.43` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26694.11` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26881.53` | POC=`26774.43` | VAL=`26667.33`
  * Prior Day Extremes: PDH=`26935.08` | PDL=`26613.78` | PDC=`26774.43`
  * Monday Range Blueprint: High=`26908.30` | Mid=`26774.43` | Low=`26640.56`
  * Developing Weekly Value Area: Weekly VAH=`26988.63` | Weekly POC=`26774.43` | Weekly VAL=`26560.23`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26827.98` | Low=`26720.88`
  * London Session (08:00-16:00 UTC): High=`26881.53` | Low=`26667.33`
  * New York Session (13:00-21:00 UTC): High=`26935.08` | Low=`26613.78`
  * Initial Balance (First Hour): IB High=`26854.75` | IB Low=`26694.11`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26667.33` - `26881.53`
  * Optimal Trade Entry (OTE 0.705): `26827.98`
  * Structural Invalidation Anchor (0.786): `26988.63`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `56` | `0x5b5d...c060` | `SHORT` | 25,636,130.83 USD | `6,373.66` | `4191.43` | `4022.80` | `28452.07` | 1,078,670.35 USD | `+4.21%` | `4X Cross` |
| `58` | `0x4692...164f` | `SHORT` | 25,257,644.35 USD | `6,279.09` | `4135.05` | `4022.80` | `13265.21` | 706,769.63 USD | `+2.80%` | `5X Cross` |
| `78` | `0xb83d...6e36` | `SHORT` | 22,995,156.32 USD | `5,717.06` | `4234.49` | `4022.80` | `26731.74` | 1,213,718.91 USD | `+5.28%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,422,829.33 USD | `4,828.91` | `4157.43` | `4022.80` | `2052.74` | -653,052.98 USD | `-3.36%` | `25X Cross` |
| `150` | `0x645b...87b8` | `LONG` | 14,146,407.62 USD | `3,517.08` | `4129.71` | `4022.80` | `29.61` | -378,146.12 USD | `-2.67%` | `3X Cross` |
| `162` | `0x7a6d...f79c` | `SHORT` | 13,145,407.13 USD | `3,268.21` | `4228.94` | `4022.80` | `4406.34` | 675,672.00 USD | `+5.14%` | `25X Cross` |
| `185` | `0xa742...e390` | `SHORT` | 11,664,380.40 USD | `2,900.00` | `4364.92` | `4022.80` | `4235.56` | 993,895.93 USD | `+8.52%` | `20X Cross` |
| `279` | `0x41e5...0825` | `SHORT` | 8,848,840.00 USD | `2,200.00` | `4112.20` | `4022.80` | `4331.05` | 198,014.59 USD | `+2.24%` | `20X Cross` |
| `280` | `0x3678...b209` | `LONG` | 8,847,960.00 USD | `2,200.00` | `4176.09` | `4022.80` | `2401.54` | -339,459.30 USD | `-3.84%` | `25X Cross` |
| `317` | `0xfc66...ca06` | `SHORT` | 7,991,866.04 USD | `1,986.89` | `4032.86` | `4022.80` | `24728.70` | 21,000.13 USD | `+0.26%` | `3X Cross` |
| `318` | `0xacb6...efbd` | `SHORT` | 7,945,329.59 USD | `1,975.37` | `4048.55` | `4022.80` | `6482.59` | 52,062.12 USD | `+0.66%` | `6X Cross` |
| `387` | `0xc26c...b8f4` | `LONG` | 6,354,882.13 USD | `1,579.95` | `4075.62` | `4022.80` | `0.000000` | -84,414.84 USD | `-1.33%` | `1X Cross` |
| `433` | `0x12d2...f97f` | `LONG` | 5,638,894.33 USD | `1,401.94` | `4278.91` | `4022.80` | `2426.80` | -359,896.25 USD | `-6.38%` | `20X Cross` |
| `593` | `0x63da...8add` | `LONG` | 4,022,200.00 USD | `1,000.00` | `4021.46` | `4022.80` | `3564.00` | 739.04 USD | `+0.02%` | `25X Cross` |
| `613` | `0x9aa5...58af` | `LONG` | 3,908,138.45 USD | `971.64` | `4279.98` | `4022.80` | `0.000000` | -250,470.63 USD | `-6.41%` | `20X Cross` |
| `636` | `0xf3dc...1672` | `LONG` | 3,743,078.86 USD | `930.74` | `4024.62` | `4022.80` | `3337.48` | -2,813.70 USD | `-0.08%` | `20X Cross` |
| `688` | `0x354b...6425` | `LONG` | 3,431,509.47 USD | `853.08` | `4037.02` | `4022.80` | `0.000000` | -12,389.44 USD | `-0.36%` | `10X Cross` |
| `702` | `0x4a20...3c26` | `LONG` | 3,367,854.11 USD | `837.40` | `4599.73` | `4022.80` | `0.000000` | -483,966.27 USD | `-14.37%` | `20X Cross` |
| `857` | `0x0fac...7a0a` | `LONG` | 2,761,248.62 USD | `686.49` | `4290.34` | `4022.80` | `1227.89` | -184,010.09 USD | `-6.66%` | `25X Cross` |
| `883` | `0xd8c5...99b0` | `SHORT` | 2,650,160.69 USD | `658.95` | `4175.35` | `4022.80` | `31154.13` | 101,186.37 USD | `+3.82%` | `4X Cross` |
| `935` | `0x625e...a354` | `SHORT` | 2,493,764.00 USD | `620.00` | `4122.81` | `4022.80` | `4342.14` | 62,383.03 USD | `+2.50%` | `20X Cross` |
| `962` | `0xeae3...e8ad` | `SHORT` | 2,413,140.00 USD | `600.00` | `4104.77` | `4022.80` | `4325.17` | 49,725.11 USD | `+2.06%` | `20X Cross` |
| `966` | `0xf285...fa82` | `LONG` | 2,405,701.55 USD | `598.11` | `4146.45` | `4022.80` | `3891.13` | -74,318.00 USD | `-3.09%` | `25X Cross` |
| `982` | `0x12f7...8750` | `LONG` | 2,355,443.36 USD | `585.61` | `4082.77` | `4022.80` | `2121.07` | -35,473.62 USD | `-1.51%` | `10X Cross` |
| `1136` | `0x413c...886c` | `LONG` | 2,010,800.00 USD | `500.00` | `4010.43` | `4022.80` | `0.000000` | 5,583.77 USD | `+0.28%` | `2X Cross` |
| `1144` | `0x61ce...a62b` | `SHORT` | 2,001,207.83 USD | `497.50` | `4071.66` | `4022.80` | `4684.06` | 24,460.96 USD | `+1.22%` | `20X Cross` |
| `1147` | `0x0593...40f9` | `LONG` | 1,995,772.75 USD | `496.18` | `4024.57` | `4022.80` | `3701.62` | -1,131.08 USD | `-0.06%` | `10X Isolated` |
| `1267` | `0xead5...69f2` | `LONG` | 1,825,209.60 USD | `453.78` | `4220.88` | `4022.80` | `3538.83` | -90,158.46 USD | `-4.94%` | `5X Isolated` |
| `1395` | `0x46fc...1195` | `LONG` | 1,637,262.49 USD | `407.03` | `4055.53` | `4022.80` | `1895.67` | -13,447.70 USD | `-0.82%` | `20X Cross` |
| `1435` | `0x6d15...d374` | `LONG` | 1,608,880.00 USD | `400.00` | `4068.25` | `4022.80` | `3841.70` | -18,420.00 USD | `-1.14%` | `25X Cross` |
| `1436` | `0xee02...309d` | `SHORT` | 1,608,880.00 USD | `400.00` | `4438.84` | `4022.80` | `4226.78` | 166,658.60 USD | `+10.36%` | `25X Isolated` |
| `1467` | `0x02a7...fe9f` | `SHORT` | 1,568,658.00 USD | `390.00` | `4055.02` | `4022.80` | `4306.60` | 12,801.25 USD | `+0.82%` | `25X Cross` |
| `1503` | `0x7e77...b8d2` | `SHORT` | 1,528,322.00 USD | `380.00` | `4131.92` | `4022.80` | `4293.41` | 41,807.64 USD | `+2.74%` | `20X Cross` |
| `1521` | `0x72c2...9b37` | `LONG` | 1,500,584.84 USD | `373.13` | `4000.98` | `4022.80` | `3777.93` | 7,691.32 USD | `+0.51%` | `13X Isolated` |
| `1568` | `0xaa44...b844` | `LONG` | 1,447,776.00 USD | `360.00` | `4043.10` | `4022.80` | `2820.88` | -7,741.63 USD | `-0.53%` | `9X Cross` |
| `1680` | `0xa41f...d50a` | `LONG` | 1,323,151.36 USD | `328.96` | `4468.89` | `4022.80` | `3833.08` | -146,946.49 USD | `-11.11%` | `15X Cross` |
| `1709` | `0x49e9...e1d0` | `SHORT` | 1,301,412.17 USD | `323.56` | `4025.23` | `4022.80` | `29785.31` | 980.53 USD | `+0.08%` | `4X Cross` |
| `1728` | `0xada6...6f88` | `LONG` | 1,283,998.75 USD | `319.28` | `4166.46` | `4022.80` | `1850.66` | -46,251.76 USD | `-3.60%` | `5X Cross` |
| `1734` | `0xbf5a...88ba` | `SHORT` | 1,277,671.54 USD | `317.65` | `4091.80` | `4022.80` | `10535.69` | 22,111.49 USD | `+1.73%` | `20X Cross` |
| `1753` | `0xff31...ff6c` | `SHORT` | 1,246,758.00 USD | `310.00` | `4372.43` | `4022.80` | `4789.07` | 108,697.38 USD | `+8.72%` | `10X Isolated` |
| `1933` | `0x50e2...d770` | `LONG` | 1,087,363.61 USD | `270.37` | `4243.58` | `4022.80` | `2561.99` | -59,962.85 USD | `-5.51%` | `20X Cross` |
| `1955` | `0x4c92...4f17` | `SHORT` | 1,072,803.20 USD | `266.72` | `4260.98` | `4022.80` | `6533.46` | 63,689.04 USD | `+5.94%` | `20X Cross` |
| `2014` | `0xd346...c4f3` | `LONG` | 1,026,360.06 USD | `255.17` | `4188.66` | `4022.80` | `3310.31` | -42,476.45 USD | `-4.14%` | `5X Isolated` |
| `2051` | `0x1581...463b` | `LONG` | 1,005,550.00 USD | `250.00` | `4003.77` | `4022.80` | `3504.53` | 4,606.41 USD | `+0.46%` | `15X Cross` |

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
| `7D` | `3609.20` | 22,790,000.00 USD | 0.00 USD | 22,790,000.00 USD | 14,530.00 USD | 0.00 USD | 35,720.00 USD |
| `1D` | `3610.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `3613.40` | 22,740,000.00 USD | 0.00 USD | 22,740,000.00 USD | 84,000.00 USD | 0.00 USD | 56,560.00 USD |
| `1D` | `3614.50` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 4,120.00 USD | 0.00 USD | 12,600.00 USD |
| `7D` | `3617.60` | 22,600,000.00 USD | 0.00 USD | 22,600,000.00 USD | 51,620.00 USD | 0.00 USD | 115,460.00 USD |
| `1D` | `3618.70` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 9,620.00 USD | 0.00 USD | 25,870.00 USD |
| `7D` | `3621.80` | 22,430,000.00 USD | 0.00 USD | 22,430,000.00 USD | 86,890.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `3622.90` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.00` | 22,190,000.00 USD | 0.00 USD | 22,190,000.00 USD | 57,780.00 USD | 0.00 USD | 108,960.00 USD |
| `1D` | `3627.10` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 25,060.00 USD | 0.00 USD | 26,370.00 USD |
| `7D` | `3630.20` | 22,030,000.00 USD | 0.00 USD | 22,030,000.00 USD | 43,500.00 USD | 0.00 USD | 76,920.00 USD |
| `1D` | `3631.30` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 45,550.00 USD | 0.00 USD | 56,520.00 USD |
| `7D` | `3634.40` | 21,910,000.00 USD | 0.00 USD | 21,910,000.00 USD | 57,680.00 USD | 0.00 USD | 52,640.00 USD |
| `1D` | `3635.50` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 39,260.00 USD | 0.00 USD | 23,450.00 USD |
| `7D` | `3638.60` | 21,800,000.00 USD | 0.00 USD | 21,800,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.70` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 12,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.80` | 21,720,000.00 USD | 0.00 USD | 21,720,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.90` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 15,910.00 USD | 0.00 USD | 10,260.00 USD |
| `7D` | `3647.00` | 21,680,000.00 USD | 0.00 USD | 21,680,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3648.10` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 10,570.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `3651.20` | 21,660,000.00 USD | 0.00 USD | 21,660,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3652.30` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 19,030.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `3655.40` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.50` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3659.60` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3660.70` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.20` | 21,620,000.00 USD | 0.00 USD | 21,620,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.60` | 21,600,000.00 USD | 0.00 USD | 21,600,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.80` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.00` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 246,890.00 USD | 0.00 USD | 546,240.00 USD |
| `7D` | `3840.20` | 20,150,000.00 USD | 0.00 USD | 20,150,000.00 USD | 361,110.00 USD | 0.00 USD | 609,290.00 USD |
| `7D` | `3844.40` | 19,180,000.00 USD | 0.00 USD | 19,180,000.00 USD | 153,770.00 USD | 0.00 USD | 225,460.00 USD |
| `7D` | `3848.60` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 84,840.00 USD | 0.00 USD | 254,070.00 USD |
| `7D` | `3852.80` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 174,390.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `3853.90` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 11,550.00 USD | 0.00 USD | 36,200.00 USD |
| `7D` | `3857.00` | 18,110,000.00 USD | 0.00 USD | 18,110,000.00 USD | 237,760.00 USD | 0.00 USD | 233,300.00 USD |
| `1D` | `3858.10` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 18,940.00 USD | 0.00 USD | 62,010.00 USD |
| `7D` | `3861.20` | 17,640,000.00 USD | 0.00 USD | 17,640,000.00 USD | 217,880.00 USD | 0.00 USD | 471,770.00 USD |
| `1D` | `3862.30` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 76,420.00 USD | 0.00 USD | 204,570.00 USD |
| `7D` | `3865.40` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 215,210.00 USD | 0.00 USD | 453,310.00 USD |
| `1D` | `3866.50` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 56,660.00 USD | 0.00 USD | 102,470.00 USD |
| `7D` | `3869.60` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 264,150.00 USD | 0.00 USD | 301,510.00 USD |
| `1D` | `3870.70` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 122,880.00 USD | 0.00 USD | 158,470.00 USD |
| `7D` | `3873.80` | 15,720,000.00 USD | 0.00 USD | 15,720,000.00 USD | 135,260.00 USD | 0.00 USD | 223,960.00 USD |
| `1D` | `3874.90` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 133,370.00 USD | 0.00 USD | 115,860.00 USD |
| `7D` | `3878.00` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 201,690.00 USD | 0.00 USD | 46,830.00 USD |
| `1D` | `3879.10` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 65,310.00 USD | 0.00 USD | 17,870.00 USD |
| `7D` | `3882.20` | 15,110,000.00 USD | 0.00 USD | 15,110,000.00 USD | 175,890.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3883.30` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 30,070.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3886.40` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.50` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 30,170.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `3890.60` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 41,760.00 USD | 0.00 USD | 46,800.00 USD |
| `7D` | `3894.80` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3895.90` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 41,330.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `3899.00` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3900.10` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 25,280.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3903.20` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `3904.30` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3907.40` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.60` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.80` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.00` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 637,120.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.20` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 392,650.00 USD | 0.00 USD | 428,640.00 USD |
| `7D` | `3928.40` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 152,680.00 USD | 0.00 USD | 492,830.00 USD |
| `7D` | `3932.60` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 345,440.00 USD | 0.00 USD | 390,200.00 USD |
| `1D` | `3933.70` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `3936.80` | 7,430,000.00 USD | 0.00 USD | 7,430,000.00 USD | 450,660.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3937.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 45,160.00 USD | 0.00 USD | 120,280.00 USD |
| `7D` | `3941.00` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 339,530.00 USD | 0.00 USD | 783,180.00 USD |
| `1D` | `3942.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 116,160.00 USD | 0.00 USD | 308,520.00 USD |
| `7D` | `3945.20` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 524,840.00 USD | 0.00 USD | 974,170.00 USD |
| `1D` | `3946.30` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 134,190.00 USD | 0.00 USD | 303,170.00 USD |
| `7D` | `3949.40` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 514,370.00 USD | 0.00 USD | 605,040.00 USD |
| `1D` | `3950.50` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 203,270.00 USD | 0.00 USD | 198,870.00 USD |
| `7D` | `3953.60` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 234,080.00 USD | 0.00 USD | 413,120.00 USD |
| `1D` | `3954.70` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 215,080.00 USD | 0.00 USD | 331,940.00 USD |
| `7D` | `3957.80` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 424,020.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3958.90` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 199,810.00 USD | 0.00 USD | 69,840.00 USD |
| `7D` | `3962.00` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 406,560.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.10` | 749,680.00 USD | 0.00 USD | 749,680.00 USD | 51,840.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.20` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.30` | 690,810.00 USD | 0.00 USD | 690,810.00 USD | 107,870.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.40` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.50` | 539,520.00 USD | 0.00 USD | 539,520.00 USD | 55,160.00 USD | 0.00 USD | 91,380.00 USD |
| `7D` | `3974.60` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.70` | 392,970.00 USD | 0.00 USD | 392,970.00 USD | 95,320.00 USD | 0.00 USD | 62,540.00 USD |
| `7D` | `3978.80` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.90` | 235,110.00 USD | 0.00 USD | 235,110.00 USD | 37,760.00 USD | 0.00 USD | 58,930.00 USD |
| `7D` | `3983.00` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3984.10` | 138,420.00 USD | 0.00 USD | 138,420.00 USD | 50,370.00 USD | 0.00 USD | 80,640.00 USD |
| `1D` | `3988.30` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.00` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.20` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.40` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 455,280.00 USD | 0.00 USD | 982,190.00 USD |
| `7D` | `4079.60` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 644,210.00 USD | 0.00 USD | 1,260,000.00 USD |
| `7D` | `4083.80` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 498,640.00 USD |
| `7D` | `4088.00` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 195,060.00 USD | 0.00 USD | 455,320.00 USD |
| `7D` | `4092.20` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 274,350.00 USD | 0.00 USD | 329,980.00 USD |
| `1D` | `4093.30` | 78,120.00 USD | 78,120.00 USD | 0.00 USD | 15,820.00 USD | 0.00 USD | 62,300.00 USD |
| `7D` | `4096.40` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 387,320.00 USD | 0.00 USD | 508,690.00 USD |
| `1D` | `4097.50` | 224,030.00 USD | 224,030.00 USD | 0.00 USD | 41,480.00 USD | 0.00 USD | 104,430.00 USD |
| `7D` | `4100.60` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 336,220.00 USD | 0.00 USD | 732,670.00 USD |
| `1D` | `4101.70` | 489,400.00 USD | 489,400.00 USD | 0.00 USD | 73,680.00 USD | 0.00 USD | 191,690.00 USD |
| `7D` | `4104.80` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 572,960.00 USD | 0.00 USD | 761,810.00 USD |
| `1D` | `4105.90` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 141,490.00 USD | 0.00 USD | 398,230.00 USD |
| `7D` | `4109.00` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 368,320.00 USD | 0.00 USD | 784,410.00 USD |
| `1D` | `4110.10` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 137,710.00 USD | 0.00 USD | 118,510.00 USD |
| `7D` | `4113.20` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 345,110.00 USD | 0.00 USD | 402,790.00 USD |
| `1D` | `4114.30` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 261,050.00 USD | 0.00 USD | 337,060.00 USD |
| `7D` | `4117.40` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 341,220.00 USD | 0.00 USD | 368,710.00 USD |
| `1D` | `4118.50` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 228,880.00 USD | 0.00 USD | 168,370.00 USD |
| `7D` | `4121.60` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 14,320.00 USD |
| `7D` | `4125.80` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4126.90` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 76,320.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4130.00` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.10` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 69,470.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4134.20` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 35,540.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.30` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 93,600.00 USD |
| `7D` | `4138.40` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 79,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.50` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 82,670.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4142.60` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 106,350.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.70` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4146.80` | 14,490,000.00 USD | 14,490,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `1D` | `4147.90` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4151.00` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.20` | 15,630,000.00 USD | 15,630,000.00 USD | 0.00 USD | 220,850.00 USD | 0.00 USD | 483,540.00 USD |
| `7D` | `4159.40` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 272,390.00 USD | 0.00 USD | 613,040.00 USD |
| `7D` | `4163.60` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 231,940.00 USD | 0.00 USD | 273,280.00 USD |
| `7D` | `4167.80` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 100,940.00 USD | 0.00 USD | 227,660.00 USD |
| `7D` | `4172.00` | 17,640,000.00 USD | 17,640,000.00 USD | 0.00 USD | 123,010.00 USD | 0.00 USD | 164,990.00 USD |
| `1D` | `4173.10` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 7,910.00 USD | 0.00 USD | 31,150.00 USD |
| `7D` | `4176.20` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 192,580.00 USD | 0.00 USD | 240,240.00 USD |
| `1D` | `4177.30` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 17,630.00 USD | 0.00 USD | 41,130.00 USD |
| `7D` | `4180.40` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 175,510.00 USD | 0.00 USD | 288,270.00 USD |
| `1D` | `4181.50` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 24,180.00 USD | 0.00 USD | 82,950.00 USD |
| `7D` | `4184.60` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 299,430.00 USD | 0.00 USD | 441,860.00 USD |
| `1D` | `4185.70` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 80,920.00 USD | 0.00 USD | 195,570.00 USD |
| `7D` | `4188.80` | 19,770,000.00 USD | 19,770,000.00 USD | 0.00 USD | 160,350.00 USD | 0.00 USD | 335,520.00 USD |
| `1D` | `4189.90` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 44,580.00 USD | 0.00 USD | 81,570.00 USD |
| `7D` | `4193.00` | 20,230,000.00 USD | 20,230,000.00 USD | 0.00 USD | 187,770.00 USD | 0.00 USD | 268,390.00 USD |
| `1D` | `4194.10` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 147,970.00 USD | 0.00 USD | 173,750.00 USD |
| `7D` | `4197.20` | 20,580,000.00 USD | 20,580,000.00 USD | 0.00 USD | 160,800.00 USD | 0.00 USD | 191,460.00 USD |
| `1D` | `4198.30` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 96,620.00 USD | 0.00 USD | 76,410.00 USD |
| `7D` | `4201.40` | 20,800,000.00 USD | 20,800,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4202.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 65,310.00 USD | 0.00 USD | 14,940.00 USD |
| `7D` | `4205.60` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 24,560.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.80` | 21,150,000.00 USD | 21,150,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4210.90` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 35,690.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4214.00` | 21,260,000.00 USD | 21,260,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4215.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 26,810.00 USD | 0.00 USD | 41,760.00 USD |
| `7D` | `4218.20` | 21,310,000.00 USD | 21,310,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4219.30` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 47,660.00 USD | 0.00 USD | 31,270.00 USD |
| `7D` | `4222.40` | 21,410,000.00 USD | 21,410,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.50` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 18,880.00 USD | 0.00 USD | 29,460.00 USD |
| `7D` | `4226.60` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4227.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | 40,320.00 USD |
| `1D` | `4231.90` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 3,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4377.80` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.20` | 21,530,000.00 USD | 21,530,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.40` | 21,680,000.00 USD | 21,680,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.60` | 21,880,000.00 USD | 21,880,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.80` | 22,150,000.00 USD | 22,150,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.00` | 22,320,000.00 USD | 22,320,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 76,590.00 USD |
| `7D` | `4407.20` | 22,420,000.00 USD | 22,420,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `7D` | `4411.40` | 22,480,000.00 USD | 22,480,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 42,930.00 USD |
| `1D` | `4412.50` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,960.00 USD | 0.00 USD | 8,590.00 USD |
| `7D` | `4415.60` | 22,570,000.00 USD | 22,570,000.00 USD | 0.00 USD | 49,730.00 USD | 0.00 USD | 41,080.00 USD |
| `1D` | `4416.70` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 2,660.00 USD | 0.00 USD | 7,410.00 USD |
| `7D` | `4419.80` | 22,700,000.00 USD | 22,700,000.00 USD | 0.00 USD | 79,360.00 USD | 0.00 USD | 58,120.00 USD |
| `1D` | `4420.90` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 7,370.00 USD | 0.00 USD | 12,930.00 USD |
| `7D` | `4424.00` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 123,230.00 USD |
| `1D` | `4425.10` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 11,750.00 USD | 0.00 USD | 59,900.00 USD |
| `1D` | `4426.80` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 6,520.00 USD | 0.00 USD | 16,990.00 USD |
| `7D` | `4428.20` | 23,080,000.00 USD | 23,080,000.00 USD | 0.00 USD | 60,670.00 USD | 0.00 USD | 154,260.00 USD |
| `7D` | `4432.40` | 23,220,000.00 USD | 23,220,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 74,510.00 USD |
| `7D` | `4436.60` | 23,280,000.00 USD | 23,280,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 45,530.00 USD |
| `7D` | `4440.10` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 50,370.00 USD | 0.00 USD | 63,280.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `841.02M` | Total OI Tokens: `209,178.7 XAUT`
  * 1h OI Change: `-1.10%` | 4h OI Change: `-3.66%` | 24h OI Change: `+5.83%`
  * Exchange Breakdown: Binance=`62.47M` | Bybit=`144.57M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `15M` | `Binance` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `OKX` | `38.95%` | `61.05%` | `0.64` | 734,170.00 USD |
| `15M` | `Bybit` | `25.05%` | `74.95%` | `0.33` | 230,250.00 USD |
| `15M` | `KuCoin` | `47.66%` | `52.34%` | `0.91` | 34,430.00 USD |
| `15M` | `Gate` | `42.95%` | `57.05%` | `0.75` | 46,940.00 USD |
| `15M` | `Bitget` | `54.62%` | `45.38%` | `1.20` | 94,830.00 USD |
| `15M` | `BingX` | `29.62%` | `70.38%` | `0.42` | 84,110.00 USD |
| `15M` | `MEXC` | `33.69%` | `66.31%` | `0.51` | 248,940.00 USD |
| `15M` | `Bitunix` | `35.8%` | `64.2%` | `0.56` | 40,090.00 USD |
| `15M` | `Hyperliquid` | `87.5%` | `12.5%` | `7.00` | 77,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.16%` | `49.84%` | `1.01` | 210,120.00 USD |
| `15M` | `Crypto.com` | `42.66%` | `57.34%` | `0.74` | 1,720.00 USD |
| `15M` | `WhiteBIT` | `81.08%` | `18.92%` | `4.29` | 79,160.00 USD |
| `15M` | `HTX` | `20.77%` | `79.23%` | `0.26` | 261.95 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `4.49%` | `95.51%` | `0.05` | 8,210.00 USD |
| `15M` | `Aster` | `1%` | `99%` | `0.01` | 1,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.21%` | `64.79%` | `0.54` | 3,420.00 USD |
| `15M` | `Whale Positions` | `34.18%` | `65.82%` | `0.52` | 1,190,000.00 USD |
| `15M` | `Global Accounts` | `38.95%` | `61.05%` | `0.64` | 3,080,000.00 USD |
| `1H` | `XAUT` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `1H` | `Binance` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `OKX` | `35.47%` | `64.53%` | `0.55` | 2,990,000.00 USD |
| `1H` | `Bybit` | `49.43%` | `50.57%` | `0.98` | 1,030,000.00 USD |
| `1H` | `KuCoin` | `52.33%` | `47.67%` | `1.10` | 139,130.00 USD |
| `1H` | `Gate` | `48.04%` | `51.96%` | `0.92` | 380,970.00 USD |
| `1H` | `Bitget` | `37.78%` | `62.22%` | `0.61` | 673,870.00 USD |
| `1H` | `BingX` | `54.21%` | `45.79%` | `1.18` | 418,970.00 USD |
| `1H` | `MEXC` | `31.32%` | `68.68%` | `0.46` | 1,270,000.00 USD |
| `1H` | `Bitunix` | `42.75%` | `57.25%` | `0.75` | 194,560.00 USD |
| `1H` | `Hyperliquid` | `60.52%` | `39.48%` | `1.53` | 170,120.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 406,890.00 USD |
| `1H` | `Crypto.com` | `54.47%` | `45.53%` | `1.20` | 5,420.00 USD |
| `1H` | `WhiteBIT` | `88.97%` | `11.03%` | `8.07` | 340,390.00 USD |
| `1H` | `HTX` | `56.03%` | `43.97%` | `1.27` | 4,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `24.56%` | `75.44%` | `0.33` | 31,910.00 USD |
| `1H` | `Aster` | `82.55%` | `17.45%` | `4.73` | 10,660.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `34.5%` | `65.5%` | `0.53` | 14,750.00 USD |
| `1H` | `Whale Positions` | `37.47%` | `62.53%` | `0.60` | 4,490,000.00 USD |
| `1H` | `Global Accounts` | `40.62%` | `59.38%` | `0.68` | 12,580,000.00 USD |
| `4H` | `XAUT` | `47.85%` | `52.15%` | `0.92` | 60,600,000.00 USD |
| `4H` | `Binance` | `44.96%` | `55.04%` | `0.82` | 21,990,000.00 USD |
| `4H` | `OKX` | `49.68%` | `50.32%` | `0.99` | 12,200,000.00 USD |
| `4H` | `Bybit` | `49.2%` | `50.8%` | `0.97` | 5,230,000.00 USD |
| `4H` | `KuCoin` | `46.59%` | `53.41%` | `0.87` | 603,060.00 USD |
| `4H` | `Gate` | `48.8%` | `51.2%` | `0.95` | 1,350,000.00 USD |
| `4H` | `Bitget` | `49.94%` | `50.06%` | `1.00` | 3,740,000.00 USD |
| `4H` | `BingX` | `37.36%` | `62.64%` | `0.60` | 2,870,000.00 USD |
| `4H` | `MEXC` | `44.62%` | `55.38%` | `0.81` | 5,000,000.00 USD |
| `4H` | `Bitunix` | `50.28%` | `49.72%` | `1.01` | 1,380,000.00 USD |
| `4H` | `Hyperliquid` | `52.89%` | `47.11%` | `1.12` | 1,890,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.38%` | `50.62%` | `0.98` | 2,630,000.00 USD |
| `4H` | `Crypto.com` | `48.48%` | `51.52%` | `0.94` | 23,490.00 USD |
| `4H` | `WhiteBIT` | `86.13%` | `13.87%` | `6.21` | 1,350,000.00 USD |
| `4H` | `HTX` | `50.42%` | `49.58%` | `1.02` | 16,420.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.23%` | `39.77%` | `1.51` | 140,410.00 USD |
| `4H` | `Aster` | `77.29%` | `22.71%` | `3.40` | 75,550.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.97%` | `53.03%` | `0.89` | 119,400.00 USD |
| `4H` | `Whale Positions` | `44.96%` | `55.04%` | `0.82` | 21,990,000.00 USD |
| `4H` | `Global Accounts` | `47.85%` | `52.15%` | `0.92` | 60,600,000.00 USD |


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
| `5m` | -39,730.00 USD | -39,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -11,970.00 USD | -34,240.00 USD | **`DISTRIBUTION`** |
| `30m` | -76,730.00 USD | -41,550.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,800.00 USD | -91,730.00 USD | **`DISTRIBUTION`** |
| `2h` | -93,250.00 USD | -121,380.00 USD | **`DISTRIBUTION`** |
| `4h` | -520,560.00 USD | 351,720.00 USD | **`DISTRIBUTION`** |
| `6h` | 280,770.00 USD | -152,100.00 USD | **`ACCUMULATION`** |
| `8h` | 952,450.00 USD | -199,140.00 USD | **`ACCUMULATION`** |
| `12h` | 1,850,000.00 USD | -706,700.00 USD | **`ACCUMULATION`** |
| `24h` | -577,680.00 USD | -47,130.00 USD | **`DISTRIBUTION`** |
| `1w` | -85,570,000.00 USD | -21,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -177,050,000.00 USD | -85,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-39.73K` | 15m=`-11.97K` | 1h=`-2.80K` | 24h=`-577.68K`
* Futures Capital Netflows: 5m=`-39.87K` | 15m=`-34.24K` | 1h=`-91.73K` | 24h=`-47.13K`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26694.11` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26611.08` (Risk Distance: `83.02` pts)
  * +2.5R Take Profit: `26901.66`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26854.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26937.78` (Risk Distance: `83.02` pts)
  * +2.5R Take Profit: `26647.20`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26988.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
