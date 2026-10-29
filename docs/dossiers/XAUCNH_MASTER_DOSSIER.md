# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 01:42:07 IST` (`2026-10-29 20:12:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26781.48` | **Live Ask Quote**: `26783.55` | **Mid Price**: `26782.51`
- **Spread Points**: `207.00` | **Spread BPS**: `0.77 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26782.51` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.96` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26969.99` | Lower -3.00σ Band: `26595.04`
  * Upper +2.51σ Band: `26929.82` | Lower -2.51σ Band: `26635.21`
  * Upper +2.01σ Band: `26895.00` | Lower -2.01σ Band: `26670.03`
  * Upper +2.00σ Band: `26889.65` | Lower -2.00σ Band: `26675.38`
  * Upper +1.28σ Band: `26857.51` | Lower -1.28σ Band: `26707.52`
  * Upper +1.00σ Band: `26836.08` | Lower -1.00σ Band: `26728.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26782.51` | EMA-20=`26782.51` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26782.51` (Slope: `+0.0000`) | EMA-100=`26782.51`
  * Institutional Anchors: EMA-144=`26782.51` | EMA-200=`26782.51` (Slope: `+0.0000`) | EMA-233=`26782.51`
- **Range Boundaries**: 24H High=`27050.34` | 24H Low=`26514.69` | Weekly High=`27318.17` | Weekly Low=`26246.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26862.86` (Distance: `+0.00%`)
  * Point of Control (POC) = `26782.51` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26702.17` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26889.65` | POC=`26782.51` | VAL=`26675.38`
  * Prior Day Extremes: PDH=`26943.21` | PDL=`26621.82` | PDC=`26782.51`
  * Monday Range Blueprint: High=`26916.43` | Mid=`26782.51` | Low=`26648.60`
  * Developing Weekly Value Area: Weekly VAH=`26996.78` | Weekly POC=`26782.51` | Weekly VAL=`26568.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26836.08` | Low=`26728.95`
  * London Session (08:00-16:00 UTC): High=`26889.65` | Low=`26675.38`
  * New York Session (13:00-21:00 UTC): High=`26943.21` | Low=`26621.82`
  * Initial Balance (First Hour): IB High=`26862.86` | IB Low=`26702.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26675.38` - `26889.65`
  * Optimal Trade Entry (OTE 0.705): `26836.08`
  * Structural Invalidation Anchor (0.786): `26996.78`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x5b5d...c060` | `SHORT` | 25,635,004.11 USD | `6,362.46` | `4191.43` | `4028.80` | `30624.94` | 1,032,874.75 USD | `+4.03%` | `4X Cross` |
| `54` | `0x4692...164f` | `SHORT` | 25,434,606.45 USD | `6,313.04` | `4133.81` | `4028.80` | `13716.43` | 662,313.91 USD | `+2.60%` | `5X Cross` |
| `69` | `0xb83d...6e36` | `SHORT` | 23,027,743.56 USD | `5,717.06` | `4234.49` | `4028.80` | `29019.73` | 1,181,131.67 USD | `+5.13%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,432,970.04 USD | `4,828.91` | `4157.43` | `4028.80` | `2113.33` | -642,912.28 USD | `-3.31%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,178,344.68 USD | `3,519.42` | `4129.54` | `4028.80` | `363.75` | -355,270.42 USD | `-2.51%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,167,957.80 USD | `3,268.21` | `4228.94` | `4028.80` | `4424.86` | 653,121.33 USD | `+4.96%` | `25X Cross` |
| `176` | `0xa742...e390` | `SHORT` | 11,683,810.40 USD | `2,900.00` | `4364.92` | `4028.80` | `4235.64` | 974,465.93 USD | `+8.34%` | `20X Cross` |
| `272` | `0x3678...b209` | `LONG` | 8,864,020.00 USD | `2,200.00` | `4176.09` | `4028.80` | `2558.21` | -323,399.30 USD | `-3.65%` | `25X Cross` |
| `274` | `0x41e5...0825` | `SHORT` | 8,854,120.00 USD | `2,200.00` | `4112.20` | `4028.80` | `4331.13` | 192,734.59 USD | `+2.18%` | `20X Cross` |
| `308` | `0xfc66...ca06` | `SHORT` | 8,002,992.62 USD | `1,986.89` | `4032.86` | `4028.80` | `24196.18` | 9,873.55 USD | `+0.12%` | `3X Cross` |
| `311` | `0xacb6...efbd` | `SHORT` | 7,956,589.20 USD | `1,975.37` | `4048.55` | `4028.80` | `6482.79` | 40,802.52 USD | `+0.51%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,365,783.80 USD | `1,579.95` | `4075.62` | `4028.80` | `0.000000` | -73,513.17 USD | `-1.15%` | `1X Cross` |
| `414` | `0x12d2...f97f` | `LONG` | 5,642,679.58 USD | `1,401.94` | `4278.91` | `4028.80` | `2606.27` | -356,111.00 USD | `-6.31%` | `20X Cross` |
| `566` | `0x63da...8add` | `LONG` | 4,028,600.00 USD | `1,000.00` | `4021.46` | `4028.80` | `3564.08` | 7,139.04 USD | `+0.18%` | `25X Cross` |
| `588` | `0x9aa5...58af` | `LONG` | 3,913,773.98 USD | `971.64` | `4279.98` | `4028.80` | `0.000000` | -244,835.11 USD | `-6.26%` | `20X Cross` |
| `613` | `0xf3dc...1672` | `LONG` | 3,748,197.95 USD | `930.74` | `4024.62` | `4028.80` | `3337.56` | 2,305.39 USD | `+0.06%` | `20X Cross` |
| `685` | `0x4a20...3c26` | `LONG` | 3,373,883.39 USD | `837.40` | `4599.73` | `4028.80` | `0.000000` | -477,936.99 USD | `-14.17%` | `20X Cross` |
| `699` | `0x354b...6425` | `LONG` | 3,326,933.47 USD | `825.77` | `4033.51` | `4028.80` | `0.000000` | -3,809.15 USD | `-0.11%` | `10X Cross` |
| `839` | `0x0fac...7a0a` | `LONG` | 2,765,161.58 USD | `686.49` | `4290.34` | `4028.80` | `1398.89` | -180,097.12 USD | `-6.51%` | `25X Cross` |
| `879` | `0xd8c5...99b0` | `SHORT` | 2,588,047.89 USD | `642.35` | `4175.35` | `4028.80` | `32927.96` | 94,013.29 USD | `+3.63%` | `4X Cross` |
| `912` | `0x625e...a354` | `SHORT` | 2,495,252.00 USD | `620.00` | `4122.81` | `4028.80` | `4342.23` | 60,895.03 USD | `+2.44%` | `20X Cross` |
| `937` | `0xeae3...e8ad` | `SHORT` | 2,417,040.00 USD | `600.00` | `4104.77` | `4028.80` | `4325.25` | 45,825.11 USD | `+1.90%` | `20X Cross` |
| `943` | `0xf285...fa82` | `LONG` | 2,409,708.86 USD | `598.11` | `4146.45` | `4028.80` | `3891.22` | -70,310.69 USD | `-2.92%` | `25X Cross` |
| `957` | `0x12f7...8750` | `LONG` | 2,359,484.07 USD | `585.61` | `4082.77` | `4028.80` | `2297.77` | -31,432.91 USD | `-1.33%` | `10X Cross` |
| `1113` | `0x413c...886c` | `LONG` | 2,013,300.00 USD | `500.00` | `4010.43` | `4028.80` | `0.000000` | 8,083.77 USD | `+0.40%` | `2X Cross` |
| `1126` | `0x61ce...a62b` | `SHORT` | 2,003,695.35 USD | `497.50` | `4071.66` | `4028.80` | `4700.89` | 21,973.44 USD | `+1.10%` | `20X Cross` |
| `1131` | `0x0593...40f9` | `LONG` | 1,998,799.43 USD | `496.18` | `4024.57` | `4028.80` | `3701.71` | 1,895.60 USD | `+0.09%` | `10X Isolated` |
| `1256` | `0xead5...69f2` | `LONG` | 1,826,616.33 USD | `453.78` | `4220.88` | `4028.80` | `3538.92` | -88,751.73 USD | `-4.86%` | `5X Isolated` |
| `1382` | `0x46fc...1195` | `LONG` | 1,639,887.13 USD | `407.07` | `4055.53` | `4028.80` | `2050.39` | -11,005.29 USD | `-0.67%` | `20X Cross` |
| `1413` | `0xee02...309d` | `SHORT` | 1,609,680.00 USD | `400.00` | `4438.84` | `4028.80` | `4226.86` | 165,858.60 USD | `+10.30%` | `25X Isolated` |
| `1414` | `0x6d15...d374` | `LONG` | 1,609,560.00 USD | `400.00` | `4068.25` | `4028.80` | `3841.79` | -17,740.00 USD | `-1.10%` | `25X Cross` |
| `1450` | `0x02a7...fe9f` | `SHORT` | 1,569,477.00 USD | `390.00` | `4055.02` | `4028.80` | `4306.68` | 11,982.25 USD | `+0.76%` | `25X Cross` |
| `1477` | `0x7e77...b8d2` | `SHORT` | 1,530,792.00 USD | `380.00` | `4131.92` | `4028.80` | `4293.49` | 39,337.64 USD | `+2.57%` | `20X Cross` |
| `1505` | `0x72c2...9b37` | `LONG` | 1,502,786.31 USD | `373.13` | `4000.98` | `4028.80` | `3778.02` | 9,892.80 USD | `+0.66%` | `13X Isolated` |
| `1537` | `0xaa44...b844` | `LONG` | 1,449,756.00 USD | `360.00` | `4043.10` | `4028.80` | `2803.24` | -5,761.63 USD | `-0.40%` | `4X Cross` |
| `1648` | `0xa41f...d50a` | `LONG` | 1,325,026.44 USD | `328.96` | `4468.89` | `4028.80` | `3833.16` | -145,071.41 USD | `-10.95%` | `15X Cross` |
| `1670` | `0x49e9...e1d0` | `SHORT` | 1,303,256.45 USD | `323.56` | `4025.23` | `4028.80` | `33199.10` | -863.75 USD | `-0.07%` | `4X Cross` |
| `1697` | `0xada6...6f88` | `LONG` | 1,285,882.48 USD | `319.28` | `4166.46` | `4028.80` | `1930.83` | -44,368.03 USD | `-3.45%` | `5X Cross` |
| `1707` | `0xbf5a...88ba` | `SHORT` | 1,279,513.94 USD | `317.65` | `4091.80` | `4028.80` | `10401.51` | 20,269.10 USD | `+1.58%` | `20X Cross` |
| `1735` | `0xff31...ff6c` | `SHORT` | 1,249,021.00 USD | `310.00` | `4372.43` | `4028.80` | `4789.15` | 106,434.38 USD | `+8.52%` | `10X Isolated` |
| `1901` | `0x50e2...d770` | `LONG` | 1,088,039.53 USD | `270.37` | `4243.58` | `4028.80` | `2562.07` | -59,286.93 USD | `-5.45%` | `20X Cross` |
| `1913` | `0x4c92...4f17` | `SHORT` | 1,074,643.57 USD | `266.72` | `4260.98` | `4028.80` | `6517.69` | 61,848.67 USD | `+5.76%` | `20X Cross` |
| `1985` | `0xd346...c4f3` | `LONG` | 1,026,870.41 USD | `255.17` | `4188.66` | `4028.80` | `3310.40` | -41,966.10 USD | `-4.09%` | `5X Isolated` |
| `2019` | `0xe47f...758c` | `LONG` | 1,006,650.00 USD | `250.00` | `4020.00` | `4028.80` | `3774.32` | 1,650.00 USD | `+0.16%` | `20X Cross` |
| `2025` | `0x1581...463b` | `LONG` | 1,005,825.00 USD | `250.00` | `4003.77` | `4028.80` | `3504.62` | 4,881.41 USD | `+0.49%` | `15X Cross` |

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
| `7D` | `3605.10` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 33,130.00 USD | 0.00 USD | 112,650.00 USD |
| `1D` | `3605.60` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 4,050.00 USD |
| `7D` | `3609.30` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3609.80` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3613.50` | 21,810,000.00 USD | 0.00 USD | 21,810,000.00 USD | 76,290.00 USD | 0.00 USD | 59,640.00 USD |
| `1D` | `3614.00` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3617.70` | 21,670,000.00 USD | 0.00 USD | 21,670,000.00 USD | 38,860.00 USD | 0.00 USD | 93,380.00 USD |
| `1D` | `3618.20` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 7,370.00 USD | 0.00 USD | 22,030.00 USD |
| `7D` | `3621.90` | 21,540,000.00 USD | 0.00 USD | 21,540,000.00 USD | 79,860.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `3622.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `7D` | `3626.10` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3626.60` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `3630.30` | 21,160,000.00 USD | 0.00 USD | 21,160,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.80` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3634.50` | 21,050,000.00 USD | 0.00 USD | 21,050,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.00` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3638.70` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.20` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 20,880,000.00 USD | 0.00 USD | 20,880,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.40` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3647.10` | 20,840,000.00 USD | 0.00 USD | 20,840,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3647.60` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 5,060.00 USD | 0.00 USD | 12,640.00 USD |
| `7D` | `3651.30` | 20,810,000.00 USD | 0.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3651.80` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.50` | 20,800,000.00 USD | 0.00 USD | 20,800,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3656.00` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 6,030.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3659.70` | 20,780,000.00 USD | 0.00 USD | 20,780,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 20,770,000.00 USD | 0.00 USD | 20,770,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 20,760,000.00 USD | 0.00 USD | 20,760,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 20,100,000.00 USD | 0.00 USD | 20,100,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,260,000.00 USD | 0.00 USD | 19,260,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,310,000.00 USD | 0.00 USD | 18,310,000.00 USD | 156,600.00 USD | 0.00 USD | 170,790.00 USD |
| `7D` | `3848.70` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 65,850.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3849.20` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3852.90` | 17,620,000.00 USD | 0.00 USD | 17,620,000.00 USD | 164,660.00 USD | 0.00 USD | 106,350.00 USD |
| `1D` | `3853.40` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `3857.10` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 216,800.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3857.60` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 23,940.00 USD | 0.00 USD | 74,240.00 USD |
| `7D` | `3861.30` | 16,890,000.00 USD | 0.00 USD | 16,890,000.00 USD | 191,980.00 USD | 0.00 USD | 504,420.00 USD |
| `1D` | `3861.80` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 60,240.00 USD | 0.00 USD | 173,960.00 USD |
| `7D` | `3865.50` | 16,200,000.00 USD | 0.00 USD | 16,200,000.00 USD | 203,250.00 USD | 0.00 USD | 370,450.00 USD |
| `1D` | `3866.00` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 74,140.00 USD | 0.00 USD | 134,060.00 USD |
| `7D` | `3869.70` | 15,620,000.00 USD | 0.00 USD | 15,620,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3870.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `7D` | `3873.90` | 15,120,000.00 USD | 0.00 USD | 15,120,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3874.40` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `7D` | `3878.10` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3878.60` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `7D` | `3882.30` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3882.80` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3886.50` | 14,290,000.00 USD | 0.00 USD | 14,290,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3887.00` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `3890.70` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3891.20` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 18,800.00 USD | 0.00 USD | 39,210.00 USD |
| `7D` | `3894.90` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3895.40` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.10` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3899.60` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 21,020.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `3903.30` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.50` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 334,680.00 USD | 0.00 USD | 367,820.00 USD |
| `7D` | `3928.50` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3929.00` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3932.70` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 322,060.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3933.20` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3936.90` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3937.40` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 47,890.00 USD | 0.00 USD | 140,290.00 USD |
| `7D` | `3941.10` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 291,240.00 USD | 0.00 USD | 726,850.00 USD |
| `1D` | `3941.60` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 95,210.00 USD | 0.00 USD | 264,740.00 USD |
| `7D` | `3945.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 478,210.00 USD | 0.00 USD | 928,940.00 USD |
| `1D` | `3945.80` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 167,260.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.00` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3954.20` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3958.40` | 828,890.00 USD | 0.00 USD | 828,890.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3962.60` | 599,290.00 USD | 0.00 USD | 599,290.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3966.80` | 542,980.00 USD | 0.00 USD | 542,980.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.00` | 405,850.00 USD | 0.00 USD | 405,850.00 USD | 46,710.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.20` | 311,540.00 USD | 0.00 USD | 311,540.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.40` | 198,850.00 USD | 0.00 USD | 198,850.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3983.60` | 136,690.00 USD | 0.00 USD | 136,690.00 USD | 29,800.00 USD | 0.00 USD | 106,890.00 USD |
| `7D` | `4025.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4028.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 415,530.00 USD |
| `7D` | `4088.10` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `7D` | `4092.30` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 230,630.00 USD | 0.00 USD | 290,760.00 USD |
| `1D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `4096.50` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4097.00` | 452,500.00 USD | 452,500.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 109,700.00 USD |
| `7D` | `4100.70` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 267,010.00 USD | 0.00 USD | 676,330.00 USD |
| `1D` | `4101.20` | 685,180.00 USD | 685,180.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 173,450.00 USD |
| `7D` | `4104.90` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 551,060.00 USD | 0.00 USD | 893,490.00 USD |
| `1D` | `4105.40` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 172,120.00 USD | 0.00 USD | 406,570.00 USD |
| `7D` | `4109.10` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 320,370.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4109.60` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `7D` | `4113.30` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4113.80` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `7D` | `4117.50` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.00` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `4121.70` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.20` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `4125.90` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4126.40` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4130.10` | 13,150,000.00 USD | 13,150,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4130.60` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4134.30` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4134.80` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 55,010.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.70` | 13,640,000.00 USD | 13,640,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.20` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 42,030.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4146.90` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.10` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 16,040,000.00 USD | 16,040,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `7D` | `4167.90` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.40` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `4172.10` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 120,430.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4172.60` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4176.30` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 227,820.00 USD |
| `1D` | `4176.80` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `7D` | `4180.50` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 143,630.00 USD | 0.00 USD | 275,830.00 USD |
| `1D` | `4181.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 68,280.00 USD |
| `7D` | `4184.70` | 18,550,000.00 USD | 18,550,000.00 USD | 0.00 USD | 276,110.00 USD | 0.00 USD | 419,190.00 USD |
| `1D` | `4185.20` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 81,790.00 USD | 0.00 USD | 203,210.00 USD |
| `7D` | `4188.90` | 19,050,000.00 USD | 19,050,000.00 USD | 0.00 USD | 169,570.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4189.40` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 53,390.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `4193.10` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4193.60` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `7D` | `4197.30` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4197.80` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `4201.50` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4202.00` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `4205.70` | 20,160,000.00 USD | 20,160,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4206.20` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4209.90` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4210.40` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4214.10` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4214.60` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4218.30` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4218.80` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `7D` | `4222.50` | 20,570,000.00 USD | 20,570,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4223.00` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `4226.70` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4227.20` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 14,900.00 USD | 0.00 USD | 53,440.00 USD |
| `7D` | `4377.90` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 20,690,000.00 USD | 20,690,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 20,830,000.00 USD | 20,830,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 21,040,000.00 USD | 21,040,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,310,000.00 USD | 21,310,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.30` | 21,560,000.00 USD | 21,560,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4407.80` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4411.50` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4412.00` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `4415.70` | 21,680,000.00 USD | 21,680,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4416.20` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `4419.90` | 21,830,000.00 USD | 21,830,000.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4420.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `7D` | `4424.10` | 21,960,000.00 USD | 21,960,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4424.60` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 47,850.00 USD |
| `7D` | `4428.30` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 53,630.00 USD | 0.00 USD | 153,720.00 USD |
| `1D` | `4428.80` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `7D` | `4432.50` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `1D` | `4433.00` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4434.10` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 6,440.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4436.70` | 22,340,000.00 USD | 22,340,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `873.96M` | Total OI Tokens: `217,113.3 XAUT`
  * 1h OI Change: `+3.46%` | 4h OI Change: `+1.50%` | 24h OI Change: `+6.14%`
  * Exchange Breakdown: Binance=`62.13M` | Bybit=`144.09M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `61.00%` | `39.00%` | `1.56` | 10,420,000.00 USD |
| `15M` | `Binance` | `59.05%` | `40.95%` | `1.44` | 740,340.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `57.83%` | `42.17%` | `1.37` | 1,150,000.00 USD |
| `15M` | `KuCoin` | `68.33%` | `31.67%` | `2.16` | 30,210.00 USD |
| `15M` | `Gate` | `69.23%` | `30.77%` | `2.25` | 289,010.00 USD |
| `15M` | `Bitget` | `72.16%` | `27.84%` | `2.59` | 292,770.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `62.9%` | `37.1%` | `1.70` | 6,900,000.00 USD |
| `15M` | `Bitunix` | `60.65%` | `39.35%` | `1.54` | 227,840.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.25%` | `51.75%` | `0.93` | 664,100.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `17.89%` | `82.11%` | `0.22` | 110,110.00 USD |
| `15M` | `HTX` | `37.14%` | `62.86%` | `0.59` | 281.26 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `20.26%` | `79.74%` | `0.25` | 14,720.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `59.05%` | `40.95%` | `1.44` | 740,340.00 USD |
| `15M` | `Global Accounts` | `61.00%` | `39.00%` | `1.56` | 10,420,000.00 USD |
| `1H` | `XAUT` | `54.70%` | `45.30%` | `1.21` | 20,890,000.00 USD |
| `1H` | `Binance` | `53.19%` | `46.81%` | `1.14` | 1,400,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `61.79%` | `38.21%` | `1.62` | 1,730,000.00 USD |
| `1H` | `KuCoin` | `42.94%` | `57.06%` | `0.75` | 60,660.00 USD |
| `1H` | `Gate` | `60.52%` | `39.48%` | `1.53` | 604,450.00 USD |
| `1H` | `Bitget` | `66.72%` | `33.28%` | `2.00` | 542,160.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `53.93%` | `46.07%` | `1.17` | 14,630,000.00 USD |
| `1H` | `Bitunix` | `49.38%` | `50.62%` | `0.98` | 483,710.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `60.95%` | `39.05%` | `1.56` | 1,160,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.01%` | `91.99%` | `0.09` | 245,820.00 USD |
| `1H` | `HTX` | `37.76%` | `62.24%` | `0.61` | 1,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `12.64%` | `87.36%` | `0.14` | 34,220.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `53.19%` | `46.81%` | `1.14` | 1,400,000.00 USD |
| `1H` | `Global Accounts` | `54.70%` | `45.30%` | `1.21` | 20,890,000.00 USD |
| `4H` | `XAUT` | `53.39%` | `46.61%` | `1.15` | 65,030,000.00 USD |
| `4H` | `Binance` | `56.89%` | `43.11%` | `1.32` | 5,350,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `52.36%` | `47.64%` | `1.10` | 6,190,000.00 USD |
| `4H` | `KuCoin` | `49.26%` | `50.74%` | `0.97` | 313,850.00 USD |
| `4H` | `Gate` | `54.41%` | `45.59%` | `1.19` | 2,100,000.00 USD |
| `4H` | `Bitget` | `50.29%` | `49.71%` | `1.01` | 2,070,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.4%` | `45.6%` | `1.19` | 41,140,000.00 USD |
| `4H` | `Bitunix` | `59.03%` | `40.97%` | `1.44` | 1,880,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.36%` | `47.64%` | `1.10` | 4,710,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `6.04%` | `93.96%` | `0.06` | 1,100,000.00 USD |
| `4H` | `HTX` | `65.75%` | `34.25%` | `1.92` | 12,790.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.1%` | `59.9%` | `0.67` | 151,230.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `56.89%` | `43.11%` | `1.32` | 5,350,000.00 USD |
| `4H` | `Global Accounts` | `53.39%` | `46.61%` | `1.15` | 65,030,000.00 USD |


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
| `5m` | -92,810.00 USD | 83,850.00 USD | **`DISTRIBUTION`** |
| `15m` | -107,760.00 USD | 194,210.00 USD | **`ACCUMULATION`** |
| `30m` | -106,170.00 USD | 281,290.00 USD | **`ACCUMULATION`** |
| `1h` | 24,450.00 USD | 333,920.00 USD | **`ACCUMULATION`** |
| `2h` | -230,230.00 USD | 780,740.00 USD | **`ACCUMULATION`** |
| `4h` | -546,370.00 USD | 457,390.00 USD | **`DISTRIBUTION`** |
| `6h` | -876,200.00 USD | 772,210.00 USD | **`DISTRIBUTION`** |
| `8h` | -490,890.00 USD | 631,640.00 USD | **`ACCUMULATION`** |
| `12h` | 383,800.00 USD | 599,610.00 USD | **`ACCUMULATION`** |
| `24h` | -1,110,000.00 USD | 143,310.00 USD | **`DISTRIBUTION`** |
| `1w` | -81,140,000.00 USD | -20,400,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,390,000.00 USD | -85,090,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-92.81K` | 15m=`-107.76K` | 1h=`+24.45K` | 24h=`-1.11M`
* Futures Capital Netflows: 5m=`+83.85K` | 15m=`+194.21K` | 1h=`+333.92K` | 24h=`+143.31K`
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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26702.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26618.71` (Risk Distance: `83.45` pts)
  * +2.5R Take Profit: `26910.80`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26862.86` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26946.32` (Risk Distance: `83.45` pts)
  * +2.5R Take Profit: `26654.23`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26996.78`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
