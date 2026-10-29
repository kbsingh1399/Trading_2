# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 01:05:40 IST` (`2026-10-29 19:35:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26733.12` | **Live Ask Quote**: `26735.17` | **Mid Price**: `26734.14`
- **Spread Points**: `205.00` | **Spread BPS**: `0.77 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26734.14` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.84` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26921.28` | Lower -3.00σ Band: `26547.01`
  * Upper +2.51σ Band: `26881.18` | Lower -2.51σ Band: `26587.11`
  * Upper +2.01σ Band: `26846.43` | Lower -2.01σ Band: `26621.86`
  * Upper +2.00σ Band: `26841.08` | Lower -2.00σ Band: `26627.21`
  * Upper +1.28σ Band: `26809.00` | Lower -1.28σ Band: `26659.29`
  * Upper +1.00σ Band: `26787.61` | Lower -1.00σ Band: `26680.68`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26734.14` | EMA-20=`26734.14` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26734.14` (Slope: `+0.0000`) | EMA-100=`26734.14`
  * Institutional Anchors: EMA-144=`26734.14` | EMA-200=`26734.14` (Slope: `+0.0000`) | EMA-233=`26734.14`
- **Range Boundaries**: 24H High=`27001.49` | 24H Low=`26466.80` | Weekly High=`27268.83` | Weekly Low=`26199.46`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26814.35` (Distance: `+0.00%`)
  * Point of Control (POC) = `26734.14` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26653.94` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26841.08` | POC=`26734.14` | VAL=`26627.21`
  * Prior Day Extremes: PDH=`26894.55` | PDL=`26573.74` | PDC=`26734.14`
  * Monday Range Blueprint: High=`26867.82` | Mid=`26734.14` | Low=`26600.47`
  * Developing Weekly Value Area: Weekly VAH=`26948.02` | Weekly POC=`26734.14` | Weekly VAL=`26520.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26787.61` | Low=`26680.68`
  * London Session (08:00-16:00 UTC): High=`26841.08` | Low=`26627.21`
  * New York Session (13:00-21:00 UTC): High=`26894.55` | Low=`26573.74`
  * Initial Balance (First Hour): IB High=`26814.35` | IB Low=`26653.94`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26627.21` - `26841.08`
  * Optimal Trade Entry (OTE 0.705): `26787.61`
  * Structural Invalidation Anchor (0.786): `26948.02`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:03:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `54` | `0x5b5d...c060` | `SHORT` | 25,606,924.88 USD | `6,373.21` | `4191.43` | `4017.80` | `29294.99` | 1,105,999.37 USD | `+4.32%` | `4X Cross` |
| `56` | `0x4692...164f` | `SHORT` | 25,355,616.89 USD | `6,310.66` | `4133.85` | `4017.80` | `13286.73` | 731,774.93 USD | `+2.89%` | `5X Cross` |
| `73` | `0xb83d...6e36` | `SHORT` | 22,967,142.73 USD | `5,717.06` | `4234.49` | `4017.80` | `27625.73` | 1,241,732.50 USD | `+5.41%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,399,167.69 USD | `4,828.91` | `4157.43` | `4017.80` | `2088.49` | -676,714.63 USD | `-3.49%` | `25X Cross` |
| `146` | `0x645b...87b8` | `LONG` | 14,138,217.94 USD | `3,518.90` | `4129.56` | `4017.80` | `295.02` | -393,276.64 USD | `-2.78%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,131,026.99 USD | `3,268.21` | `4228.94` | `4017.80` | `4409.10` | 690,052.14 USD | `+5.26%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,651,910.40 USD | `2,900.00` | `4364.92` | `4017.80` | `4235.62` | 1,006,365.93 USD | `+8.64%` | `20X Cross` |
| `276` | `0x3678...b209` | `LONG` | 8,839,160.00 USD | `2,200.00` | `4176.09` | `4017.80` | `2490.23` | -348,259.30 USD | `-3.94%` | `25X Cross` |
| `277` | `0x41e5...0825` | `SHORT` | 8,838,060.00 USD | `2,200.00` | `4112.20` | `4017.80` | `4331.10` | 208,794.59 USD | `+2.36%` | `20X Cross` |
| `309` | `0xfc66...ca06` | `SHORT` | 7,983,123.72 USD | `1,986.89` | `4032.86` | `4017.80` | `24965.12` | 29,742.45 USD | `+0.37%` | `3X Cross` |
| `312` | `0xacb6...efbd` | `SHORT` | 7,935,650.29 USD | `1,975.37` | `4048.55` | `4017.80` | `6496.21` | 61,741.43 USD | `+0.78%` | `6X Cross` |
| `382` | `0xc26c...b8f4` | `LONG` | 6,347,930.34 USD | `1,579.95` | `4075.62` | `4017.80` | `0.000000` | -91,366.63 USD | `-1.44%` | `1X Cross` |
| `420` | `0x12d2...f97f` | `LONG` | 5,632,024.81 USD | `1,401.94` | `4278.91` | `4017.80` | `2510.26` | -366,765.77 USD | `-6.51%` | `20X Cross` |
| `574` | `0x63da...8add` | `LONG` | 4,017,800.00 USD | `1,000.00` | `4021.46` | `4017.80` | `3564.06` | -3,660.96 USD | `-0.09%` | `25X Cross` |
| `596` | `0x9aa5...58af` | `LONG` | 3,903,377.41 USD | `971.64` | `4279.98` | `4017.80` | `0.000000` | -255,231.68 USD | `-6.54%` | `20X Cross` |
| `625` | `0xf3dc...1672` | `LONG` | 3,739,355.89 USD | `930.74` | `4024.62` | `4017.80` | `3337.54` | -6,536.67 USD | `-0.17%` | `20X Cross` |
| `687` | `0x4a20...3c26` | `LONG` | 3,364,504.51 USD | `837.40` | `4599.73` | `4017.80` | `0.000000` | -487,315.87 USD | `-14.48%` | `20X Cross` |
| `702` | `0x354b...6425` | `LONG` | 3,298,036.56 USD | `820.84` | `4033.57` | `4017.80` | `0.000000` | -12,865.05 USD | `-0.39%` | `10X Cross` |
| `843` | `0x0fac...7a0a` | `LONG` | 2,758,228.08 USD | `686.49` | `4290.34` | `4017.80` | `1360.30` | -187,030.62 USD | `-6.78%` | `25X Cross` |
| `888` | `0xd8c5...99b0` | `SHORT` | 2,580,853.52 USD | `642.35` | `4175.35` | `4017.80` | `32023.22` | 101,207.66 USD | `+3.92%` | `4X Cross` |
| `922` | `0x625e...a354` | `SHORT` | 2,490,726.00 USD | `620.00` | `4122.81` | `4017.80` | `4342.20` | 65,421.03 USD | `+2.63%` | `20X Cross` |
| `948` | `0xeae3...e8ad` | `SHORT` | 2,410,680.00 USD | `600.00` | `4104.77` | `4017.80` | `4325.22` | 52,185.11 USD | `+2.16%` | `20X Cross` |
| `951` | `0xf285...fa82` | `LONG` | 2,403,129.70 USD | `598.11` | `4146.45` | `4017.80` | `3891.19` | -76,889.86 USD | `-3.20%` | `25X Cross` |
| `968` | `0x12f7...8750` | `LONG` | 2,352,866.67 USD | `585.61` | `4082.77` | `4017.80` | `2153.70` | -38,050.31 USD | `-1.62%` | `10X Cross` |
| `1124` | `0x413c...886c` | `LONG` | 2,008,800.00 USD | `500.00` | `4010.43` | `4017.80` | `0.000000` | 3,583.77 USD | `+0.18%` | `2X Cross` |
| `1139` | `0x61ce...a62b` | `SHORT` | 1,998,770.06 USD | `497.50` | `4071.66` | `4017.80` | `4692.26` | 26,898.73 USD | `+1.35%` | `20X Cross` |
| `1146` | `0x0593...40f9` | `LONG` | 1,993,539.95 USD | `496.18` | `4024.57` | `4017.80` | `3701.68` | -3,363.88 USD | `-0.17%` | `10X Isolated` |
| `1264` | `0xead5...69f2` | `LONG` | 1,822,986.06 USD | `453.78` | `4220.88` | `4017.80` | `3538.89` | -92,382.00 USD | `-5.07%` | `5X Isolated` |
| `1390` | `0x46fc...1195` | `LONG` | 1,635,399.81 USD | `407.03` | `4055.53` | `4017.80` | `1947.08` | -15,320.01 USD | `-0.94%` | `20X Cross` |
| `1426` | `0xee02...309d` | `SHORT` | 1,607,160.00 USD | `400.00` | `4438.84` | `4017.80` | `4226.84` | 168,378.60 USD | `+10.48%` | `25X Isolated` |
| `1427` | `0x6d15...d374` | `LONG` | 1,606,920.00 USD | `400.00` | `4068.25` | `4017.80` | `3841.76` | -20,380.00 USD | `-1.27%` | `25X Cross` |
| `1452` | `0x02a7...fe9f` | `SHORT` | 1,566,942.00 USD | `390.00` | `4055.02` | `4017.80` | `4306.66` | 14,517.25 USD | `+0.93%` | `25X Cross` |
| `1491` | `0x7e77...b8d2` | `SHORT` | 1,526,764.00 USD | `380.00` | `4131.92` | `4017.80` | `4293.46` | 43,365.64 USD | `+2.84%` | `20X Cross` |
| `1509` | `0x72c2...9b37` | `LONG` | 1,499,092.31 USD | `373.13` | `4000.98` | `4017.80` | `3777.99` | 6,198.80 USD | `+0.41%` | `13X Isolated` |
| `1547` | `0xaa44...b844` | `LONG` | 1,446,336.00 USD | `360.00` | `4043.10` | `4017.80` | `2803.21` | -9,181.63 USD | `-0.63%` | `4X Cross` |
| `1658` | `0xa41f...d50a` | `LONG` | 1,321,539.44 USD | `328.96` | `4468.89` | `4017.80` | `3833.14` | -148,558.41 USD | `-11.24%` | `15X Cross` |
| `1683` | `0x49e9...e1d0` | `SHORT` | 1,300,020.88 USD | `323.56` | `4025.23` | `4017.80` | `28790.63` | 2,371.82 USD | `+0.18%` | `4X Cross` |
| `1712` | `0xada6...6f88` | `LONG` | 1,282,721.65 USD | `319.28` | `4166.46` | `4017.80` | `1867.19` | -47,528.86 USD | `-3.71%` | `5X Cross` |
| `1719` | `0xbf5a...88ba` | `SHORT` | 1,276,115.03 USD | `317.65` | `4091.80` | `4017.80` | `10495.54` | 23,668.00 USD | `+1.85%` | `20X Cross` |
| `1740` | `0xff31...ff6c` | `SHORT` | 1,245,518.00 USD | `310.00` | `4372.43` | `4017.80` | `4789.13` | 109,937.38 USD | `+8.83%` | `10X Isolated` |
| `1906` | `0x50e2...d770` | `LONG` | 1,086,282.14 USD | `270.37` | `4243.58` | `4017.80` | `2562.05` | -61,044.32 USD | `-5.62%` | `20X Cross` |
| `1918` | `0x4c92...4f17` | `SHORT` | 1,071,629.62 USD | `266.72` | `4260.98` | `4017.80` | `6523.15` | 64,862.61 USD | `+6.05%` | `20X Cross` |
| `1993` | `0xd346...c4f3` | `LONG` | 1,025,262.81 USD | `255.17` | `4188.66` | `4017.90` | `3310.37` | -43,573.70 USD | `-4.25%` | `5X Isolated` |
| `2033` | `0xe47f...758c` | `LONG` | 1,004,400.00 USD | `250.00` | `4020.00` | `4017.90` | `3774.29` | -600.00 USD | `-0.06%` | `20X Cross` |
| `2034` | `0x1581...463b` | `LONG` | 1,004,325.00 USD | `250.00` | `4003.77` | `4017.90` | `3504.59` | 3,381.41 USD | `+0.34%` | `15X Cross` |

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
| `7D` | `3605.10` | 22,630,000.00 USD | 0.00 USD | 22,630,000.00 USD | 33,130.00 USD | 0.00 USD | 129,270.00 USD |
| `1D` | `3606.50` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 3,220.00 USD | 0.00 USD | 19,260.00 USD |
| `7D` | `3609.30` | 22,470,000.00 USD | 0.00 USD | 22,470,000.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `3610.60` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 4,870.00 USD | 0.00 USD | 20,730.00 USD |
| `7D` | `3613.50` | 22,400,000.00 USD | 0.00 USD | 22,400,000.00 USD | 84,000.00 USD | 0.00 USD | 67,380.00 USD |
| `1D` | `3614.70` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 7,480.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `3617.70` | 22,240,000.00 USD | 0.00 USD | 22,240,000.00 USD | 38,860.00 USD | 0.00 USD | 104,640.00 USD |
| `1D` | `3618.80` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 6,260.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3621.90` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 86,890.00 USD | 0.00 USD | 149,470.00 USD |
| `1D` | `3622.90` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 17,390.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.10` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 57,780.00 USD | 0.00 USD | 87,140.00 USD |
| `1D` | `3627.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 14,290.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.30` | 21,720,000.00 USD | 0.00 USD | 21,720,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3631.10` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 31,880.00 USD | 0.00 USD | 53,030.00 USD |
| `7D` | `3634.50` | 21,610,000.00 USD | 0.00 USD | 21,610,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.20` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 30,630.00 USD | 0.00 USD | 15,790.00 USD |
| `7D` | `3638.70` | 21,510,000.00 USD | 0.00 USD | 21,510,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.30` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3642.90` | 21,440,000.00 USD | 0.00 USD | 21,440,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.40` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3647.10` | 21,400,000.00 USD | 0.00 USD | 21,400,000.00 USD | 19,450.00 USD | 0.00 USD | 8,230.00 USD |
| `1D` | `3647.50` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 8,260.00 USD | 0.00 USD | 18,280.00 USD |
| `7D` | `3651.30` | 21,370,000.00 USD | 0.00 USD | 21,370,000.00 USD | 0.00 USD | 0.00 USD | 11,910.00 USD |
| `1D` | `3651.60` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 13,710.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3655.50` | 21,360,000.00 USD | 0.00 USD | 21,360,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `1D` | `3655.70` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 7,520.00 USD | 0.00 USD | 27,270.00 USD |
| `7D` | `3659.70` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3659.80` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.30` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.70` | 21,320,000.00 USD | 0.00 USD | 21,320,000.00 USD | 80,570.00 USD | 0.00 USD | 69,240.00 USD |
| `7D` | `3831.90` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 153,350.00 USD | 0.00 USD | 354,960.00 USD |
| `7D` | `3836.10` | 20,660,000.00 USD | 0.00 USD | 20,660,000.00 USD | 262,010.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.30` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 359,570.00 USD | 0.00 USD | 588,790.00 USD |
| `7D` | `3844.50` | 18,870,000.00 USD | 0.00 USD | 18,870,000.00 USD | 156,600.00 USD | 0.00 USD | 212,340.00 USD |
| `1D` | `3848.40` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3848.70` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 74,350.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.50` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 15,390.00 USD | 0.00 USD | 40,040.00 USD |
| `7D` | `3852.90` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 183,930.00 USD | 0.00 USD | 176,300.00 USD |
| `1D` | `3856.60` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 20,740.00 USD | 0.00 USD | 58,940.00 USD |
| `7D` | `3857.10` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 216,800.00 USD | 0.00 USD | 242,280.00 USD |
| `1D` | `3860.70` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 43,610.00 USD | 0.00 USD | 111,940.00 USD |
| `7D` | `3861.30` | 17,310,000.00 USD | 0.00 USD | 17,310,000.00 USD | 209,570.00 USD | 0.00 USD | 532,590.00 USD |
| `1D` | `3864.80` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 63,970.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `3865.50` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 203,250.00 USD | 0.00 USD | 370,450.00 USD |
| `1D` | `3868.90` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 50,420.00 USD | 0.00 USD | 58,620.00 USD |
| `7D` | `3869.70` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 252,790.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3873.00` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 84,010.00 USD | 0.00 USD | 156,630.00 USD |
| `7D` | `3873.90` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 116,430.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3877.10` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 77,180.00 USD | 0.00 USD | 43,100.00 USD |
| `7D` | `3878.10` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 201,690.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3881.20` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 25,200.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `3882.30` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 183,420.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3885.30` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3886.50` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.40` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 31,370.00 USD | 0.00 USD | 44,690.00 USD |
| `7D` | `3890.70` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.50` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 23,320.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3894.90` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.60` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 26,020.00 USD | 0.00 USD | 34,480.00 USD |
| `7D` | `3899.10` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `1D` | `3901.70` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 19,170.00 USD | 0.00 USD | 55,050.00 USD |
| `7D` | `3903.30` | 14,230,000.00 USD | 0.00 USD | 14,230,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `3905.80` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3907.50` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 161,150.00 USD | 0.00 USD | 138,490.00 USD |
| `7D` | `3911.70` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 306,700.00 USD | 0.00 USD | 709,920.00 USD |
| `7D` | `3915.90` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `3920.10` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 695,090.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `3924.30` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 334,680.00 USD | 0.00 USD | 450,920.00 USD |
| `1D` | `3926.30` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 16,080.00 USD | 0.00 USD | 49,460.00 USD |
| `7D` | `3928.50` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.40` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 36,670.00 USD | 0.00 USD | 119,080.00 USD |
| `7D` | `3932.70` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 377,610.00 USD | 0.00 USD | 390,200.00 USD |
| `1D` | `3934.50` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 21,350.00 USD | 0.00 USD | 98,260.00 USD |
| `7D` | `3936.90` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 414,840.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.60` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 44,450.00 USD | 0.00 USD | 152,440.00 USD |
| `7D` | `3941.10` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 291,240.00 USD | 0.00 USD | 783,180.00 USD |
| `1D` | `3942.70` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 146,280.00 USD | 0.00 USD | 385,730.00 USD |
| `7D` | `3945.30` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 513,380.00 USD | 0.00 USD | 928,940.00 USD |
| `1D` | `3946.80` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 108,820.00 USD | 0.00 USD | 193,070.00 USD |
| `7D` | `3949.50` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 519,110.00 USD | 0.00 USD | 541,140.00 USD |
| `1D` | `3950.90` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 105,370.00 USD | 0.00 USD | 221,160.00 USD |
| `7D` | `3953.70` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 188,120.00 USD | 0.00 USD | 355,430.00 USD |
| `1D` | `3955.00` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 132,450.00 USD | 0.00 USD | 229,390.00 USD |
| `7D` | `3957.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 419,380.00 USD | 0.00 USD | 219,250.00 USD |
| `1D` | `3959.10` | 884,130.00 USD | 0.00 USD | 884,130.00 USD | 148,890.00 USD | 0.00 USD | 33,390.00 USD |
| `7D` | `3962.10` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.20` | 701,850.00 USD | 0.00 USD | 701,850.00 USD | 57,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.30` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.30` | 637,060.00 USD | 0.00 USD | 637,060.00 USD | 84,790.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3970.50` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.40` | 508,850.00 USD | 0.00 USD | 508,850.00 USD | 55,160.00 USD | 0.00 USD | 75,760.00 USD |
| `7D` | `3974.70` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.50` | 377,930.00 USD | 0.00 USD | 377,930.00 USD | 64,650.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3978.90` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.60` | 247,210.00 USD | 0.00 USD | 247,210.00 USD | 29,470.00 USD | 0.00 USD | 44,790.00 USD |
| `7D` | `3983.10` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `3983.70` | 172,960.00 USD | 0.00 USD | 172,960.00 USD | 58,670.00 USD | 0.00 USD | 106,890.00 USD |
| `1D` | `3987.80` | 7,400.00 USD | 0.00 USD | 7,400.00 USD | 7,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4014.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4014.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.10` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.30` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.50` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 466,320.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `4079.70` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 633,160.00 USD | 0.00 USD | 1,210,000.00 USD |
| `7D` | `4083.90` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 367,930.00 USD | 0.00 USD | 498,640.00 USD |
| `1D` | `4086.20` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.10` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 206,900.00 USD | 0.00 USD | 480,330.00 USD |
| `1D` | `4090.30` | 200,730.00 USD | 200,730.00 USD | 0.00 USD | 40,090.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.30` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 286,170.00 USD | 0.00 USD | 391,950.00 USD |
| `1D` | `4094.40` | 314,350.00 USD | 314,350.00 USD | 0.00 USD | 26,730.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `4096.50` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 404,710.00 USD | 0.00 USD | 508,690.00 USD |
| `1D` | `4098.50` | 493,990.00 USD | 493,990.00 USD | 0.00 USD | 45,160.00 USD | 0.00 USD | 134,480.00 USD |
| `7D` | `4100.70` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 267,010.00 USD | 0.00 USD | 732,670.00 USD |
| `1D` | `4102.60` | 851,920.00 USD | 851,920.00 USD | 0.00 USD | 95,210.00 USD | 0.00 USD | 262,720.00 USD |
| `7D` | `4104.90` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 586,230.00 USD | 0.00 USD | 893,490.00 USD |
| `1D` | `4106.70` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 148,830.00 USD | 0.00 USD | 330,980.00 USD |
| `7D` | `4109.10` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 320,370.00 USD | 0.00 USD | 543,600.00 USD |
| `1D` | `4110.80` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 68,280.00 USD | 0.00 USD | 105,010.00 USD |
| `7D` | `4113.30` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 333,670.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.90` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 166,130.00 USD | 0.00 USD | 293,620.00 USD |
| `7D` | `4117.50` | 12,370,000.00 USD | 12,370,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4119.00` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 156,230.00 USD | 0.00 USD | 98,400.00 USD |
| `7D` | `4121.70` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4123.10` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 50,390.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `4125.90` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 288,790.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.20` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 90,460.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.10` | 13,520,000.00 USD | 13,520,000.00 USD | 0.00 USD | 195,730.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.30` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 42,220.00 USD | 0.00 USD | 80,280.00 USD |
| `7D` | `4134.30` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.40` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 58,220.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4138.50` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.50` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 52,000.00 USD | 0.00 USD | 39,490.00 USD |
| `7D` | `4142.70` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `1D` | `4143.60` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 50,560.00 USD | 0.00 USD | 139,570.00 USD |
| `7D` | `4146.90` | 14,290,000.00 USD | 14,290,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `1D` | `4147.70` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 27,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4151.10` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.30` | 15,450,000.00 USD | 15,450,000.00 USD | 0.00 USD | 227,640.00 USD | 0.00 USD | 491,090.00 USD |
| `7D` | `4159.50` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 322,100.00 USD | 0.00 USD | 629,440.00 USD |
| `7D` | `4163.70` | 16,840,000.00 USD | 16,840,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 249,320.00 USD |
| `7D` | `4167.90` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4168.20` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4172.10` | 17,500,000.00 USD | 17,500,000.00 USD | 0.00 USD | 128,920.00 USD | 0.00 USD | 195,980.00 USD |
| `1D` | `4172.30` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 11,230.00 USD | 0.00 USD | 69,710.00 USD |
| `7D` | `4176.30` | 17,940,000.00 USD | 17,940,000.00 USD | 0.00 USD | 192,580.00 USD | 0.00 USD | 247,170.00 USD |
| `1D` | `4176.40` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 11,440.00 USD | 0.00 USD | 50,360.00 USD |
| `1D` | `4180.50` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 22,220.00 USD | 0.00 USD | 63,750.00 USD |
| `7D` | `4180.50` | 18,390,000.00 USD | 18,390,000.00 USD | 0.00 USD | 143,630.00 USD | 0.00 USD | 304,000.00 USD |
| `1D` | `4184.60` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 80,520.00 USD | 0.00 USD | 187,700.00 USD |
| `7D` | `4184.70` | 19,100,000.00 USD | 19,100,000.00 USD | 0.00 USD | 293,700.00 USD | 0.00 USD | 419,190.00 USD |
| `1D` | `4188.70` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 45,630.00 USD | 0.00 USD | 85,290.00 USD |
| `7D` | `4188.90` | 19,600,000.00 USD | 19,600,000.00 USD | 0.00 USD | 169,570.00 USD | 0.00 USD | 331,160.00 USD |
| `1D` | `4192.80` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 50,440.00 USD | 0.00 USD | 104,640.00 USD |
| `7D` | `4193.10` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 203,970.00 USD |
| `1D` | `4196.90` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 109,340.00 USD |
| `7D` | `4197.30` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4201.00` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 80,870.00 USD | 0.00 USD | 21,140.00 USD |
| `7D` | `4201.50` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4205.10` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.70` | 20,720,000.00 USD | 20,720,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 64,320.00 USD |
| `1D` | `4209.20` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 46,860.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4209.90` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `1D` | `4213.30` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 27,500.00 USD | 0.00 USD | 34,640.00 USD |
| `7D` | `4214.10` | 20,970,000.00 USD | 20,970,000.00 USD | 0.00 USD | 54,860.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.40` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 27,190.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.30` | 21,020,000.00 USD | 21,020,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.50` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 21,700.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `4222.50` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 66,250.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `4225.60` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 23,490.00 USD | 0.00 USD | 69,790.00 USD |
| `7D` | `4226.70` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4229.70` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4377.90` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.30` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.50` | 21,390,000.00 USD | 21,390,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.70` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 68,330.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4398.90` | 21,860,000.00 USD | 21,860,000.00 USD | 0.00 USD | 71,200.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.10` | 22,030,000.00 USD | 22,030,000.00 USD | 0.00 USD | 94,460.00 USD | 0.00 USD | 76,590.00 USD |
| `7D` | `4407.30` | 22,130,000.00 USD | 22,130,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4410.10` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.50` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 14,530.00 USD | 0.00 USD | 55,320.00 USD |
| `1D` | `4414.20` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 10,170.00 USD |
| `7D` | `4415.70` | 22,290,000.00 USD | 22,290,000.00 USD | 0.00 USD | 49,730.00 USD | 0.00 USD | 41,080.00 USD |
| `1D` | `4418.30` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 15,290.00 USD |
| `7D` | `4419.90` | 22,440,000.00 USD | 22,440,000.00 USD | 0.00 USD | 66,610.00 USD | 0.00 USD | 78,200.00 USD |
| `1D` | `4421.90` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | 18,190.00 USD |
| `7D` | `4424.10` | 22,580,000.00 USD | 22,580,000.00 USD | 0.00 USD | 40,080.00 USD | 0.00 USD | 103,150.00 USD |
| `7D` | `4428.30` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 60,670.00 USD | 0.00 USD | 153,720.00 USD |
| `7D` | `4432.50` | 22,910,000.00 USD | 22,910,000.00 USD | 0.00 USD | 59,640.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.70` | 22,970,000.00 USD | 22,970,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4440.50` | 23,060,000.00 USD | 23,060,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `845.42M` | Total OI Tokens: `210,556.2 XAUT`
  * 1h OI Change: `-0.07%` | 4h OI Change: `-1.14%` | 24h OI Change: `+3.12%`
  * Exchange Breakdown: Binance=`62.17M` | Bybit=`144.75M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `62.02%` | `37.98%` | `1.63` | 1,240,000.00 USD |
| `15M` | `Binance` | `57.99%` | `42.01%` | `1.38` | 530,060.00 USD |
| `15M` | `OKX` | `67.79%` | `32.21%` | `2.10` | 157,590.00 USD |
| `15M` | `Bybit` | `70.17%` | `29.83%` | `2.35` | 144,280.00 USD |
| `15M` | `KuCoin` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Gate` | `80.95%` | `19.05%` | `4.25` | 16,270.00 USD |
| `15M` | `Bitget` | `61.43%` | `38.57%` | `1.59` | 22,640.00 USD |
| `15M` | `BingX` | `49.66%` | `50.34%` | `0.99` | 63,910.00 USD |
| `15M` | `MEXC` | `61.96%` | `38.04%` | `1.63` | 92,990.00 USD |
| `15M` | `Bitunix` | `56.52%` | `43.48%` | `1.30` | 44,480.00 USD |
| `15M` | `Hyperliquid` | `69.54%` | `30.46%` | `2.28` | 8,900.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.12%` | `47.88%` | `1.09` | 41,670.00 USD |
| `15M` | `Crypto.com` | `76.03%` | `23.97%` | `3.17` | 57.60 USD |
| `15M` | `WhiteBIT` | `80.75%` | `19.25%` | `4.19` | 98,970.00 USD |
| `15M` | `HTX` | `32.41%` | `67.59%` | `0.48` | 185.11 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 1,920.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 323.03 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.31%` | `85.69%` | `0.17` | 12,650.00 USD |
| `15M` | `Whale Positions` | `57.99%` | `42.01%` | `1.38` | 530,060.00 USD |
| `15M` | `Global Accounts` | `62.02%` | `37.98%` | `1.63` | 1,240,000.00 USD |
| `1H` | `XAUT` | `58.19%` | `41.81%` | `1.39` | 6,890,000.00 USD |
| `1H` | `Binance` | `52.76%` | `47.24%` | `1.12` | 675,330.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `61.99%` | `38.01%` | `1.63` | 569,830.00 USD |
| `1H` | `KuCoin` | `26.19%` | `73.81%` | `0.35` | 27,920.00 USD |
| `1H` | `Gate` | `61.68%` | `38.32%` | `1.61` | 336,380.00 USD |
| `1H` | `Bitget` | `56.48%` | `43.52%` | `1.30` | 237,990.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `61.01%` | `38.99%` | `1.56` | 3,880,000.00 USD |
| `1H` | `Bitunix` | `65.93%` | `34.07%` | `1.94` | 312,320.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.97%` | `45.03%` | `1.22` | 608,410.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.77%` | `80.23%` | `0.25` | 227,210.00 USD |
| `1H` | `HTX` | `55.95%` | `44.05%` | `1.27` | 1,280.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `7.72%` | `92.28%` | `0.08` | 19,640.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `52.76%` | `47.24%` | `1.12` | 675,330.00 USD |
| `1H` | `Global Accounts` | `58.19%` | `41.81%` | `1.39` | 6,890,000.00 USD |
| `4H` | `XAUT` | `52.55%` | `47.45%` | `1.11` | 51,570,000.00 USD |
| `4H` | `Binance` | `54.69%` | `45.31%` | `1.21` | 4,520,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.36%` | `50.64%` | `0.97` | 4,800,000.00 USD |
| `4H` | `KuCoin` | `52.26%` | `47.74%` | `1.09` | 303,010.00 USD |
| `4H` | `Gate` | `53.55%` | `46.45%` | `1.15` | 1,730,000.00 USD |
| `4H` | `Bitget` | `44.46%` | `55.54%` | `0.80` | 1,730,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.3%` | `45.7%` | `1.19` | 31,190,000.00 USD |
| `4H` | `Bitunix` | `61.33%` | `38.67%` | `1.59` | 1,630,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.37%` | `47.63%` | `1.10` | 4,160,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `13.21%` | `86.79%` | `0.15` | 1,340,000.00 USD |
| `4H` | `HTX` | `93.04%` | `6.96%` | `13.37` | 70,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.51%` | `54.49%` | `0.84` | 121,060.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `54.69%` | `45.31%` | `1.21` | 4,520,000.00 USD |
| `4H` | `Global Accounts` | `52.55%` | `47.45%` | `1.11` | 51,570,000.00 USD |


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
| `5m` | 99,210.00 USD | 33,030.00 USD | **`ACCUMULATION`** |
| `15m` | 160,980.00 USD | -13,360.00 USD | **`ACCUMULATION`** |
| `30m` | 110,600.00 USD | 51,560.00 USD | **`ACCUMULATION`** |
| `1h` | 93,420.00 USD | 168,940.00 USD | **`ACCUMULATION`** |
| `2h` | -297,820.00 USD | 537,520.00 USD | **`ACCUMULATION`** |
| `4h` | -411,970.00 USD | 355,550.00 USD | **`DISTRIBUTION`** |
| `6h` | -790,540.00 USD | 843,840.00 USD | **`ACCUMULATION`** |
| `8h` | -28,290.00 USD | 79,400.00 USD | **`ACCUMULATION`** |
| `12h` | 512,760.00 USD | 290,640.00 USD | **`ACCUMULATION`** |
| `24h` | -904,920.00 USD | -84,750.00 USD | **`DISTRIBUTION`** |
| `1w` | -82,330,000.00 USD | -20,540,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -178,150,000.00 USD | -85,210,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+99.21K` | 15m=`+160.98K` | 1h=`+93.42K` | 24h=`-904.92K`
* Futures Capital Netflows: 5m=`+33.03K` | 15m=`-13.36K` | 1h=`+168.94K` | 24h=`-84.75K`
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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26653.94` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26570.67` (Risk Distance: `83.28` pts)
  * +2.5R Take Profit: `26862.14`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26814.35` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26897.62` (Risk Distance: `83.28` pts)
  * +2.5R Take Profit: `26606.15`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26948.02`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
