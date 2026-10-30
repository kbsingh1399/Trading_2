# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 09:22:12 IST` (`2026-10-30 03:52:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26563.30` | **Live Ask Quote**: `26565.33` | **Mid Price**: `26564.32`
- **Spread Points**: `203.00` | **Spread BPS**: `0.76 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26564.32` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.41` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26750.27` | Lower -3.00σ Band: `26378.36`
  * Upper +2.51σ Band: `26710.42` | Lower -2.51σ Band: `26418.21`
  * Upper +2.01σ Band: `26675.89` | Lower -2.01σ Band: `26452.74`
  * Upper +2.00σ Band: `26670.57` | Lower -2.00σ Band: `26458.06`
  * Upper +1.28σ Band: `26638.70` | Lower -1.28σ Band: `26489.93`
  * Upper +1.00σ Band: `26617.44` | Lower -1.00σ Band: `26511.19`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26564.32` | EMA-20=`26564.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26564.32` (Slope: `+0.0000`) | EMA-100=`26564.32`
  * Institutional Anchors: EMA-144=`26564.32` | EMA-200=`26564.32` (Slope: `+0.0000`) | EMA-233=`26564.32`
- **Range Boundaries**: 24H High=`26829.96` | 24H Low=`26298.67` | Weekly High=`27095.60` | Weekly Low=`26033.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26644.01` (Distance: `+0.00%`)
  * Point of Control (POC) = `26564.32` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26484.62` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26670.57` | POC=`26564.32` | VAL=`26458.06`
  * Prior Day Extremes: PDH=`26723.70` | PDL=`26404.93` | PDC=`26564.32`
  * Monday Range Blueprint: High=`26697.14` | Mid=`26564.32` | Low=`26431.49`
  * Developing Weekly Value Area: Weekly VAH=`26776.83` | Weekly POC=`26564.32` | Weekly VAL=`26351.80`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26617.44` | Low=`26511.19`
  * London Session (08:00-16:00 UTC): High=`26670.57` | Low=`26458.06`
  * New York Session (13:00-21:00 UTC): High=`26723.70` | Low=`26404.93`
  * Initial Balance (First Hour): IB High=`26644.01` | IB Low=`26484.62`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26458.06` - `26670.57`
  * Optimal Trade Entry (OTE 0.705): `26617.44`
  * Structural Invalidation Anchor (0.786): `26776.83`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `49` | `0x5b5d...c060` | `SHORT` | 25,929,442.81 USD | `6,489.82` | `4185.46` | `3995.40` | `30168.87` | 1,233,508.20 USD | `+4.76%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,140,102.00 USD | `6,292.26` | `4129.74` | `3995.40` | `14017.79` | 845,348.61 USD | `+3.36%` | `5X Cross` |
| `62` | `0xb83d...6e36` | `SHORT` | 23,452,596.06 USD | `5,869.90` | `4228.86` | `3995.40` | `27739.58` | 1,370,425.87 USD | `+5.84%` | `5X Cross` |
| `96` | `0xec0b...b078` | `LONG` | 19,293,897.52 USD | `4,828.91` | `4157.43` | `3995.40` | `2310.51` | -781,984.80 USD | `-4.05%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,148,900.83 USD | `3,541.30` | `4128.21` | `3995.40` | `596.60` | -470,349.37 USD | `-3.32%` | `3X Cross` |
| `154` | `0x7a6d...f79c` | `SHORT` | 13,057,492.20 USD | `3,268.21` | `4228.94` | `3995.40` | `4399.49` | 763,586.93 USD | `+5.85%` | `25X Cross` |
| `178` | `0xa742...e390` | `SHORT` | 11,586,660.40 USD | `2,900.00` | `4364.92` | `3995.40` | `4235.84` | 1,071,615.93 USD | `+9.25%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,789,880.00 USD | `2,200.00` | `4176.09` | `3995.40` | `2650.86` | -397,539.30 USD | `-4.52%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,789,880.00 USD | `2,200.00` | `4112.20` | `3995.40` | `4331.33` | 256,974.59 USD | `+2.92%` | `20X Cross` |
| `296` | `0xacb6...efbd` | `SHORT` | 7,892,587.24 USD | `1,975.37` | `4048.55` | `3995.40` | `6593.15` | 104,804.47 USD | `+1.33%` | `6X Cross` |
| `357` | `0xc26c...b8f4` | `LONG` | 6,312,381.43 USD | `1,579.95` | `4075.62` | `3995.40` | `0.000000` | -126,915.54 USD | `-2.01%` | `1X Cross` |
| `500` | `0x354b...6425` | `LONG` | 4,418,884.03 USD | `1,105.99` | `4004.95` | `3995.40` | `0.000000` | -10,568.90 USD | `-0.24%` | `10X Cross` |
| `554` | `0x63da...8add` | `LONG` | 3,995,400.00 USD | `1,000.00` | `4021.46` | `3995.40` | `3564.29` | -26,060.96 USD | `-0.65%` | `25X Cross` |
| `565` | `0xf3dc...1672` | `LONG` | 3,932,259.87 USD | `984.27` | `4018.39` | `3995.40` | `2875.67` | -22,926.82 USD | `-0.58%` | `20X Cross` |
| `577` | `0x9aa5...58af` | `LONG` | 3,882,195.61 USD | `971.64` | `4279.98` | `3995.40` | `0.000000` | -276,413.47 USD | `-7.12%` | `20X Cross` |
| `658` | `0x4a20...3c26` | `LONG` | 3,345,663.02 USD | `837.40` | `4599.73` | `3995.40` | `0.000000` | -506,157.36 USD | `-15.13%` | `20X Cross` |
| `829` | `0x0fac...7a0a` | `LONG` | 2,742,782.17 USD | `686.49` | `4290.34` | `3995.40` | `1209.62` | -202,476.53 USD | `-7.38%` | `25X Cross` |
| `901` | `0xd8c5...99b0` | `SHORT` | 2,518,456.93 USD | `630.35` | `4175.35` | `3995.40` | `33707.24` | 113,499.96 USD | `+4.51%` | `4X Cross` |
| `914` | `0x625e...a354` | `SHORT` | 2,477,148.00 USD | `620.00` | `4122.81` | `3995.40` | `4342.43` | 78,999.03 USD | `+3.19%` | `20X Cross` |
| `941` | `0xeae3...e8ad` | `SHORT` | 2,397,360.00 USD | `600.00` | `4104.77` | `3995.40` | `4325.45` | 65,505.11 USD | `+2.73%` | `20X Cross` |
| `943` | `0xf285...fa82` | `LONG` | 2,389,732.12 USD | `598.11` | `4146.45` | `3995.40` | `3891.43` | -90,287.43 USD | `-3.78%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,339,690.43 USD | `585.61` | `4082.77` | `3995.40` | `2709.10` | -51,226.55 USD | `-2.19%` | `10X Cross` |
| `1094` | `0x413c...886c` | `LONG` | 1,997,550.00 USD | `500.00` | `4010.43` | `3995.40` | `0.000000` | -7,666.23 USD | `-0.38%` | `2X Cross` |
| `1101` | `0x61ce...a62b` | `SHORT` | 1,987,576.23 USD | `497.50` | `4071.66` | `3995.40` | `4723.24` | 38,092.56 USD | `+1.92%` | `20X Cross` |
| `1216` | `0xead5...69f2` | `LONG` | 1,813,093.57 USD | `453.78` | `4220.88` | `3995.40` | `3539.13` | -102,274.49 USD | `-5.64%` | `5X Isolated` |
| `1283` | `0x46fc...1195` | `LONG` | 1,685,462.45 USD | `421.86` | `4053.56` | `3995.40` | `2170.80` | -24,579.80 USD | `-1.46%` | `20X Cross` |
| `1351` | `0x6d15...d374` | `LONG` | 1,598,200.00 USD | `400.00` | `4068.25` | `3995.40` | `3842.00` | -29,100.00 USD | `-1.82%` | `25X Cross` |
| `1352` | `0xee02...309d` | `SHORT` | 1,598,160.00 USD | `400.00` | `4438.84` | `3995.40` | `4227.07` | 177,378.60 USD | `+11.10%` | `25X Isolated` |
| `1394` | `0x02a7...fe9f` | `SHORT` | 1,558,167.00 USD | `390.00` | `4055.02` | `3995.40` | `4306.88` | 23,292.25 USD | `+1.49%` | `25X Cross` |
| `1428` | `0x7e77...b8d2` | `SHORT` | 1,518,290.00 USD | `380.00` | `4131.92` | `3995.40` | `4293.69` | 51,839.64 USD | `+3.41%` | `20X Cross` |
| `1447` | `0x9c06...0560` | `LONG` | 1,491,326.60 USD | `373.26` | `4018.98` | `3995.40` | `0.000000` | -8,805.21 USD | `-0.59%` | `25X Cross` |
| `1448` | `0x72c2...9b37` | `LONG` | 1,490,883.42 USD | `373.13` | `4000.98` | `3995.40` | `3778.23` | -2,010.09 USD | `-0.13%` | `13X Isolated` |
| `1501` | `0xaa44...b844` | `LONG` | 1,438,416.00 USD | `360.00` | `4043.10` | `3995.40` | `2819.98` | -17,101.63 USD | `-1.19%` | `4X Cross` |
| `1611` | `0xa41f...d50a` | `LONG` | 1,314,368.07 USD | `328.96` | `4468.89` | `3995.40` | `3802.35` | -155,729.78 USD | `-11.85%` | `15X Cross` |
| `1621` | `0x7fda...17d1` | `SHORT` | 1,302,124.83 USD | `325.91` | `4013.13` | `3995.40` | `30570.13` | 5,778.72 USD | `+0.44%` | `20X Cross` |
| `1659` | `0xbf5a...88ba` | `SHORT` | 1,269,190.15 USD | `317.65` | `4091.80` | `3995.40` | `9780.20` | 30,592.88 USD | `+2.41%` | `20X Cross` |
| `1693` | `0xff31...ff6c` | `SHORT` | 1,238,543.00 USD | `310.00` | `4372.43` | `3995.40` | `4789.36` | 116,912.38 USD | `+9.44%` | `10X Isolated` |
| `1721` | `0xada6...6f88` | `LONG` | 1,212,504.06 USD | `303.50` | `4166.46` | `3995.40` | `1798.64` | -52,008.80 USD | `-4.29%` | `5X Cross` |
| `1884` | `0x50e2...d770` | `LONG` | 1,080,225.91 USD | `270.37` | `4243.58` | `3995.40` | `2562.28` | -67,100.55 USD | `-6.21%` | `20X Cross` |
| `1897` | `0x4c92...4f17` | `SHORT` | 1,065,628.41 USD | `266.72` | `4260.98` | `3995.40` | `6505.05` | 70,863.82 USD | `+6.65%` | `20X Cross` |
| `1964` | `0xd346...c4f3` | `LONG` | 1,019,521.40 USD | `255.17` | `4188.66` | `3995.40` | `3310.61` | -49,315.11 USD | `-4.84%` | `5X Isolated` |

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
| `7D` | `3605.20` | 21,460,000.00 USD | 0.00 USD | 21,460,000.00 USD | 33,130.00 USD | 0.00 USD | 98,140.00 USD |
| `7D` | `3609.40` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 22,730.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `3610.40` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 16,210.00 USD | 0.00 USD | 16,440.00 USD |
| `7D` | `3613.60` | 21,270,000.00 USD | 0.00 USD | 21,270,000.00 USD | 87,020.00 USD | 0.00 USD | 70,110.00 USD |
| `1D` | `3614.50` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,120.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `3617.80` | 21,110,000.00 USD | 0.00 USD | 21,110,000.00 USD | 37,660.00 USD | 0.00 USD | 92,850.00 USD |
| `1D` | `3618.60` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 19,950.00 USD | 0.00 USD | 38,170.00 USD |
| `7D` | `3622.00` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 58,610.00 USD | 0.00 USD | 153,530.00 USD |
| `1D` | `3622.70` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 22,710.00 USD | 0.00 USD | 69,950.00 USD |
| `7D` | `3626.20` | 20,770,000.00 USD | 0.00 USD | 20,770,000.00 USD | 35,220.00 USD | 0.00 USD | 60,800.00 USD |
| `1D` | `3626.80` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 14,290.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `3630.40` | 20,670,000.00 USD | 0.00 USD | 20,670,000.00 USD | 39,790.00 USD | 0.00 USD | 71,240.00 USD |
| `1D` | `3630.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 31,880.00 USD | 0.00 USD | 49,910.00 USD |
| `7D` | `3634.60` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 53,860.00 USD | 0.00 USD | 46,780.00 USD |
| `1D` | `3635.00` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 30,630.00 USD | 0.00 USD | 18,910.00 USD |
| `7D` | `3638.80` | 20,460,000.00 USD | 0.00 USD | 20,460,000.00 USD | 72,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3639.10` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.00` | 20,390,000.00 USD | 0.00 USD | 20,390,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `1D` | `3643.20` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 17,040.00 USD | 0.00 USD | 6,960.00 USD |
| `7D` | `3647.20` | 20,350,000.00 USD | 0.00 USD | 20,350,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `1D` | `3647.30` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 2,430.00 USD | 0.00 USD | 7,140.00 USD |
| `1D` | `3651.40` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 7,240.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `3655.50` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3655.60` | 20,310,000.00 USD | 0.00 USD | 20,310,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3659.80` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3819.40` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3827.80` | 20,270,000.00 USD | 0.00 USD | 20,270,000.00 USD | 80,570.00 USD | 0.00 USD | 134,940.00 USD |
| `7D` | `3832.00` | 20,050,000.00 USD | 0.00 USD | 20,050,000.00 USD | 156,890.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `3836.20` | 19,610,000.00 USD | 0.00 USD | 19,610,000.00 USD | 278,450.00 USD | 0.00 USD | 579,850.00 USD |
| `7D` | `3840.40` | 18,750,000.00 USD | 0.00 USD | 18,750,000.00 USD | 339,590.00 USD | 0.00 USD | 600,380.00 USD |
| `7D` | `3844.60` | 17,810,000.00 USD | 0.00 USD | 17,810,000.00 USD | 156,600.00 USD | 0.00 USD | 159,210.00 USD |
| `1D` | `3848.20` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `3848.80` | 17,490,000.00 USD | 0.00 USD | 17,490,000.00 USD | 75,110.00 USD | 0.00 USD | 297,560.00 USD |
| `1D` | `3852.30` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 50,300.00 USD | 0.00 USD | 64,530.00 USD |
| `7D` | `3853.00` | 17,120,000.00 USD | 0.00 USD | 17,120,000.00 USD | 205,430.00 USD | 0.00 USD | 119,830.00 USD |
| `1D` | `3856.40` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 27,320.00 USD | 0.00 USD | 93,700.00 USD |
| `7D` | `3857.20` | 16,800,000.00 USD | 0.00 USD | 16,800,000.00 USD | 193,740.00 USD | 0.00 USD | 308,950.00 USD |
| `1D` | `3860.50` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 91,370.00 USD | 0.00 USD | 131,510.00 USD |
| `7D` | `3861.40` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 181,250.00 USD | 0.00 USD | 424,710.00 USD |
| `1D` | `3864.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 77,800.00 USD | 0.00 USD | 190,500.00 USD |
| `7D` | `3865.60` | 15,690,000.00 USD | 0.00 USD | 15,690,000.00 USD | 130,450.00 USD | 0.00 USD | 314,760.00 USD |
| `1D` | `3868.70` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 46,100.00 USD | 0.00 USD | 55,560.00 USD |
| `7D` | `3869.80` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 200,270.00 USD | 0.00 USD | 245,800.00 USD |
| `1D` | `3872.80` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 87,380.00 USD | 0.00 USD | 149,870.00 USD |
| `7D` | `3874.00` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 132,750.00 USD | 0.00 USD | 242,350.00 USD |
| `1D` | `3876.90` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 78,110.00 USD | 0.00 USD | 49,200.00 USD |
| `7D` | `3878.20` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 218,820.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `3881.00` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 25,200.00 USD | 0.00 USD | 6,860.00 USD |
| `7D` | `3882.40` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 149,980.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `3885.10` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 44,450.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `3886.60` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 72,680.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `3889.20` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 6,070.00 USD | 0.00 USD | 12,530.00 USD |
| `7D` | `3890.80` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `1D` | `3893.30` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 23,320.00 USD | 0.00 USD | 19,340.00 USD |
| `7D` | `3895.00` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3897.40` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3899.20` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 87,120.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.40` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 5,770.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `3911.80` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `3916.00` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 524,020.00 USD | 0.00 USD | 1,160,000.00 USD |
| `7D` | `3920.20` | 10,500,000.00 USD | 0.00 USD | 10,500,000.00 USD | 691,980.00 USD | 0.00 USD | 1,150,000.00 USD |
| `7D` | `3924.40` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 307,540.00 USD | 0.00 USD | 367,820.00 USD |
| `1D` | `3926.10` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `3928.60` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 164,520.00 USD | 0.00 USD | 557,530.00 USD |
| `1D` | `3930.20` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 122,570.00 USD | 0.00 USD | 148,540.00 USD |
| `7D` | `3932.80` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 416,720.00 USD | 0.00 USD | 250,300.00 USD |
| `1D` | `3934.30` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 21,350.00 USD | 0.00 USD | 105,240.00 USD |
| `7D` | `3937.00` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 374,140.00 USD | 0.00 USD | 466,590.00 USD |
| `1D` | `3938.40` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 113,960.00 USD | 0.00 USD | 207,720.00 USD |
| `7D` | `3941.20` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 340,060.00 USD | 0.00 USD | 776,550.00 USD |
| `1D` | `3942.50` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 172,480.00 USD | 0.00 USD | 417,140.00 USD |
| `7D` | `3945.40` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 262,330.00 USD | 0.00 USD | 768,760.00 USD |
| `1D` | `3946.60` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 138,120.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `3949.60` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 414,070.00 USD | 0.00 USD | 567,510.00 USD |
| `1D` | `3950.70` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 116,680.00 USD | 0.00 USD | 143,940.00 USD |
| `7D` | `3953.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 221,020.00 USD | 0.00 USD | 353,750.00 USD |
| `1D` | `3954.80` | 943,470.00 USD | 0.00 USD | 943,470.00 USD | 115,530.00 USD | 0.00 USD | 295,900.00 USD |
| `7D` | `3958.00` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 386,480.00 USD | 0.00 USD | 194,560.00 USD |
| `1D` | `3958.90` | 532,040.00 USD | 0.00 USD | 532,040.00 USD | 161,750.00 USD | 0.00 USD | 44,110.00 USD |
| `7D` | `3962.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 392,050.00 USD | 0.00 USD | 52,260.00 USD |
| `1D` | `3963.00` | 326,180.00 USD | 0.00 USD | 326,180.00 USD | 40,760.00 USD | 0.00 USD | 7,030.00 USD |
| `7D` | `3966.40` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 169,920.00 USD | 0.00 USD | 232,140.00 USD |
| `1D` | `3967.10` | 278,390.00 USD | 0.00 USD | 278,390.00 USD | 88,900.00 USD | 0.00 USD | 34,780.00 USD |
| `7D` | `3970.60` | 616,410.00 USD | 0.00 USD | 616,410.00 USD | 109,720.00 USD | 0.00 USD | 93,080.00 USD |
| `1D` | `3971.20` | 154,710.00 USD | 0.00 USD | 154,710.00 USD | 12,130.00 USD | 0.00 USD | 20,100.00 USD |
| `7D` | `3974.80` | 413,600.00 USD | 0.00 USD | 413,600.00 USD | 40,750.00 USD | 0.00 USD | 59,560.00 USD |
| `1D` | `3975.30` | 122,480.00 USD | 0.00 USD | 122,480.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3979.00` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 132,500.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `3979.40` | 9,780.00 USD | 0.00 USD | 9,780.00 USD | 9,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.20` | 104,860.00 USD | 0.00 USD | 104,860.00 USD | 30,500.00 USD | 0.00 USD | 74,360.00 USD |
| `7D` | `4012.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4012.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4067.20` | 301,610.00 USD | 301,610.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 269,880.00 USD |
| `7D` | `4071.40` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 306,700.00 USD | 0.00 USD | 578,530.00 USD |
| `7D` | `4075.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 493,770.00 USD | 0.00 USD | 1,090,000.00 USD |
| `7D` | `4079.80` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 605,710.00 USD | 0.00 USD | 1,190,000.00 USD |
| `7D` | `4084.00` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 382,320.00 USD | 0.00 USD | 375,440.00 USD |
| `1D` | `4086.00` | 20,250.00 USD | 20,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD |
| `7D` | `4088.20` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 206,260.00 USD | 0.00 USD | 579,810.00 USD |
| `1D` | `4090.10` | 240,450.00 USD | 240,450.00 USD | 0.00 USD | 79,820.00 USD | 0.00 USD | 140,390.00 USD |
| `7D` | `4092.40` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 311,550.00 USD | 0.00 USD | 191,280.00 USD |
| `1D` | `4094.20` | 400,570.00 USD | 400,570.00 USD | 0.00 USD | 56,830.00 USD | 0.00 USD | 103,290.00 USD |
| `7D` | `4096.60` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 364,000.00 USD | 0.00 USD | 469,990.00 USD |
| `1D` | `4098.30` | 693,870.00 USD | 693,870.00 USD | 0.00 USD | 89,310.00 USD | 0.00 USD | 203,990.00 USD |
| `7D` | `4100.80` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 315,830.00 USD | 0.00 USD | 726,040.00 USD |
| `1D` | `4102.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 159,720.00 USD | 0.00 USD | 295,710.00 USD |
| `7D` | `4105.00` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 385,450.00 USD | 0.00 USD | 832,390.00 USD |
| `1D` | `4106.50` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 151,960.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `4109.20` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 217,050.00 USD | 0.00 USD | 444,520.00 USD |
| `1D` | `4110.60` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 84,180.00 USD | 0.00 USD | 105,010.00 USD |
| `7D` | `4113.40` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 281,680.00 USD | 0.00 USD | 374,370.00 USD |
| `1D` | `4114.70` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 148,080.00 USD | 0.00 USD | 277,440.00 USD |
| `7D` | `4117.60` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 303,560.00 USD | 0.00 USD | 339,430.00 USD |
| `1D` | `4118.80` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 163,150.00 USD | 0.00 USD | 114,580.00 USD |
| `7D` | `4121.80` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 387,340.00 USD | 0.00 USD | 37,080.00 USD |
| `1D` | `4122.90` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 70,150.00 USD | 0.00 USD | 13,710.00 USD |
| `7D` | `4126.00` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 351,370.00 USD | 0.00 USD | 144,510.00 USD |
| `1D` | `4127.00` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 74,770.00 USD | 0.00 USD | 14,720.00 USD |
| `7D` | `4130.20` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 133,140.00 USD | 0.00 USD | 102,810.00 USD |
| `1D` | `4131.10` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 26,260.00 USD | 0.00 USD | 22,640.00 USD |
| `7D` | `4134.40` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 152,640.00 USD |
| `1D` | `4135.20` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 34,450.00 USD | 0.00 USD | 58,770.00 USD |
| `7D` | `4138.60` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 51,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4139.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 21,970.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4142.80` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 92,890.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `4147.00` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 111,080.00 USD | 0.00 USD | 169,380.00 USD |
| `7D` | `4151.20` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 153,350.00 USD | 0.00 USD | 289,260.00 USD |
| `7D` | `4155.40` | 14,790,000.00 USD | 14,790,000.00 USD | 0.00 USD | 233,160.00 USD | 0.00 USD | 516,490.00 USD |
| `7D` | `4159.60` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 316,580.00 USD | 0.00 USD | 604,050.00 USD |
| `7D` | `4163.80` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 183,970.00 USD | 0.00 USD | 207,770.00 USD |
| `1D` | `4168.00` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 11,850.00 USD | 0.00 USD | 48,150.00 USD |
| `7D` | `4168.00` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 98,340.00 USD | 0.00 USD | 240,170.00 USD |
| `1D` | `4172.10` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 52,310.00 USD | 0.00 USD | 68,220.00 USD |
| `7D` | `4172.20` | 16,750,000.00 USD | 16,750,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 145,380.00 USD |
| `1D` | `4176.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 7,800.00 USD | 0.00 USD | 70,940.00 USD |
| `7D` | `4176.40` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 173,300.00 USD | 0.00 USD | 235,000.00 USD |
| `1D` | `4180.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 74,330.00 USD | 0.00 USD | 87,610.00 USD |
| `7D` | `4180.60` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 147,690.00 USD | 0.00 USD | 293,510.00 USD |
| `1D` | `4184.40` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 76,950.00 USD | 0.00 USD | 207,280.00 USD |
| `7D` | `4184.80` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 211,650.00 USD | 0.00 USD | 370,320.00 USD |
| `1D` | `4188.50` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 68,910.00 USD | 0.00 USD | 85,290.00 USD |
| `7D` | `4189.00` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 73,570.00 USD | 0.00 USD | 319,610.00 USD |
| `1D` | `4192.60` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 50,440.00 USD | 0.00 USD | 66,030.00 USD |
| `7D` | `4193.20` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 167,190.00 USD | 0.00 USD | 184,310.00 USD |
| `1D` | `4196.70` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 57,770.00 USD | 0.00 USD | 147,950.00 USD |
| `7D` | `4197.40` | 19,260,000.00 USD | 19,260,000.00 USD | 0.00 USD | 141,970.00 USD | 0.00 USD | 190,630.00 USD |
| `1D` | `4200.80` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 77,530.00 USD | 0.00 USD | 21,140.00 USD |
| `7D` | `4201.60` | 19,460,000.00 USD | 19,460,000.00 USD | 0.00 USD | 200,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4204.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 23,730.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `4205.80` | 19,670,000.00 USD | 19,670,000.00 USD | 0.00 USD | 142,450.00 USD | 0.00 USD | 72,010.00 USD |
| `1D` | `4209.00` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 44,450.00 USD | 0.00 USD | 16,190.00 USD |
| `7D` | `4210.00` | 19,830,000.00 USD | 19,830,000.00 USD | 0.00 USD | 80,200.00 USD | 0.00 USD | 70,190.00 USD |
| `1D` | `4213.10` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 6,070.00 USD | 0.00 USD | 2,480.00 USD |
| `7D` | `4214.20` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 46,540.00 USD |
| `1D` | `4217.20` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 23,320.00 USD | 0.00 USD | 29,390.00 USD |
| `7D` | `4218.40` | 19,970,000.00 USD | 19,970,000.00 USD | 0.00 USD | 23,760.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `4221.30` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `4222.60` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 62,870.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4226.80` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `7D` | `4378.00` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4386.40` | 20,200,000.00 USD | 20,200,000.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 35,210.00 USD |
| `7D` | `4390.60` | 20,340,000.00 USD | 20,340,000.00 USD | 0.00 USD | 48,920.00 USD | 0.00 USD | 92,640.00 USD |
| `7D` | `4394.80` | 20,550,000.00 USD | 20,550,000.00 USD | 0.00 USD | 69,900.00 USD | 0.00 USD | 138,370.00 USD |
| `7D` | `4399.00` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 72,610.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `4403.20` | 20,970,000.00 USD | 20,970,000.00 USD | 0.00 USD | 91,480.00 USD | 0.00 USD | 59,970.00 USD |
| `7D` | `4407.40` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 75,530.00 USD |
| `1D` | `4409.90` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | 29,820.00 USD |
| `7D` | `4411.60` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 22,730.00 USD | 0.00 USD | 35,080.00 USD |
| `1D` | `4414.00` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 15,650.00 USD | 0.00 USD | 13,450.00 USD |
| `7D` | `4415.80` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 77,830.00 USD | 0.00 USD | 33,340.00 USD |
| `1D` | `4418.10` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 20,900.00 USD |
| `7D` | `4420.00` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 40,330.00 USD | 0.00 USD | 88,140.00 USD |
| `1D` | `4422.20` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 14,510.00 USD | 0.00 USD | 30,790.00 USD |
| `7D` | `4424.20` | 21,490,000.00 USD | 21,490,000.00 USD | 0.00 USD | 30,630.00 USD | 0.00 USD | 91,880.00 USD |
| `1D` | `4425.80` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 13,690.00 USD | 0.00 USD | 52,460.00 USD |
| `7D` | `4428.40` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 34,490.00 USD | 0.00 USD | 131,440.00 USD |
| `7D` | `4432.60` | 21,750,000.00 USD | 21,750,000.00 USD | 0.00 USD | 44,420.00 USD | 0.00 USD | 53,230.00 USD |
| `7D` | `4436.80` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 10,060.00 USD | 0.00 USD | 50,490.00 USD |
| `7D` | `4439.40` | 21,900,000.00 USD | 21,900,000.00 USD | 0.00 USD | 46,540.00 USD | 0.00 USD | 46,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `804.22M` | Total OI Tokens: `201,371.7 XAUT`
  * 1h OI Change: `-1.08%` | 4h OI Change: `+1.32%` | 24h OI Change: `-5.75%`
  * Exchange Breakdown: Binance=`60.59M` | Bybit=`143.37M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `31.21%` | `68.79%` | `0.45` | 2,080,000.00 USD |
| `15M` | `Binance` | `30.99%` | `69.01%` | `0.45` | 541,470.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `48.45%` | `51.55%` | `0.94` | 156,430.00 USD |
| `15M` | `KuCoin` | `86.91%` | `13.09%` | `6.64` | 2,050.00 USD |
| `15M` | `Gate` | `44.75%` | `55.25%` | `0.81` | 136,840.00 USD |
| `15M` | `Bitget` | `46.25%` | `53.75%` | `0.86` | 56,370.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `23.71%` | `76.29%` | `0.31` | 1,000,000.00 USD |
| `15M` | `Bitunix` | `30.77%` | `69.23%` | `0.44` | 21,490.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.49%` | `47.51%` | `1.10` | 133,430.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.37%` | `99.63%` | `0.00` | 27,000.00 USD |
| `15M` | `HTX` | `88.61%` | `11.39%` | `7.78` | 1,930.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `30.99%` | `69.01%` | `0.45` | 541,470.00 USD |
| `15M` | `Global Accounts` | `31.21%` | `68.79%` | `0.45` | 2,080,000.00 USD |
| `1H` | `XAUT` | `55.19%` | `44.81%` | `1.23` | 8,410,000.00 USD |
| `1H` | `Binance` | `53.86%` | `46.14%` | `1.17` | 3,660,000.00 USD |
| `1H` | `OKX` | `58.17%` | `41.83%` | `1.39` | 1,530,000.00 USD |
| `1H` | `Bybit` | `58.48%` | `41.52%` | `1.41` | 865,840.00 USD |
| `1H` | `KuCoin` | `45.37%` | `54.63%` | `0.83` | 88,950.00 USD |
| `1H` | `Gate` | `52.53%` | `47.47%` | `1.11` | 142,950.00 USD |
| `1H` | `Bitget` | `53.91%` | `46.09%` | `1.17` | 519,590.00 USD |
| `1H` | `BingX` | `49.5%` | `50.5%` | `0.98` | 310,800.00 USD |
| `1H` | `MEXC` | `58.26%` | `41.74%` | `1.40` | 445,640.00 USD |
| `1H` | `Bitunix` | `48.85%` | `51.15%` | `0.96` | 279,000.00 USD |
| `1H` | `Hyperliquid` | `64.99%` | `35.01%` | `1.86` | 160,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.24%` | `50.76%` | `0.97` | 287,920.00 USD |
| `1H` | `Crypto.com` | `35.57%` | `64.43%` | `0.55` | 3,210.00 USD |
| `1H` | `WhiteBIT` | `74.51%` | `25.49%` | `2.92` | 98,320.00 USD |
| `1H` | `HTX` | `91.53%` | `8.47%` | `10.81` | 4,050.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.3%` | `99.7%` | `0.00` | 310.79 USD |
| `1H` | `Aster` | `70.4%` | `29.6%` | `2.38` | 3,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.2%` | `85.8%` | `0.17` | 7,790.00 USD |
| `1H` | `Whale Positions` | `53.86%` | `46.14%` | `1.17` | 3,660,000.00 USD |
| `1H` | `Global Accounts` | `55.19%` | `44.81%` | `1.23` | 8,410,000.00 USD |
| `4H` | `XAUT` | `46.52%` | `53.48%` | `0.87` | 63,920,000.00 USD |
| `4H` | `Binance` | `47.52%` | `52.48%` | `0.91` | 11,700,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `42.36%` | `57.64%` | `0.73` | 7,940,000.00 USD |
| `4H` | `KuCoin` | `43.22%` | `56.78%` | `0.76` | 378,350.00 USD |
| `4H` | `Gate` | `44.89%` | `55.11%` | `0.81` | 2,490,000.00 USD |
| `4H` | `Bitget` | `48.38%` | `51.62%` | `0.94` | 3,930,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `46.37%` | `53.63%` | `0.86` | 28,340,000.00 USD |
| `4H` | `Bitunix` | `46.26%` | `53.74%` | `0.86` | 1,580,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.36%` | `42.64%` | `1.35` | 5,840,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `20.16%` | `79.84%` | `0.25` | 1,500,000.00 USD |
| `4H` | `HTX` | `59.68%` | `40.32%` | `1.48` | 44,320.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.7%` | `53.3%` | `0.88` | 176,180.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `47.52%` | `52.48%` | `0.91` | 11,700,000.00 USD |
| `4H` | `Global Accounts` | `46.52%` | `53.48%` | `0.87` | 63,920,000.00 USD |


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
| `5m` | -80,470.00 USD | -121,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -128,890.00 USD | -118,530.00 USD | **`DISTRIBUTION`** |
| `30m` | -252,620.00 USD | -95,610.00 USD | **`DISTRIBUTION`** |
| `1h` | -520,350.00 USD | -304,680.00 USD | **`DISTRIBUTION`** |
| `2h` | -495,340.00 USD | -285,590.00 USD | **`DISTRIBUTION`** |
| `4h` | -781,220.00 USD | -1,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,160,000.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,760,000.00 USD | -1,500,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,070,000.00 USD | -1,290,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -269,720.00 USD | -2,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,020,000.00 USD | -20,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,620,000.00 USD | -84,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-80.47K` | 15m=`-128.89K` | 1h=`-520.35K` | 24h=`-269.72K`
* Futures Capital Netflows: 5m=`-121.87K` | 15m=`-118.53K` | 1h=`-304.68K` | 24h=`-2.05M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26484.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26401.88` (Risk Distance: `82.74` pts)
  * +2.5R Take Profit: `26691.47`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26644.01` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26726.75` (Risk Distance: `82.74` pts)
  * +2.5R Take Profit: `26437.16`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26776.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
