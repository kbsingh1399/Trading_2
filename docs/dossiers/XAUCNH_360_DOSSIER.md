# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26640.94` | **Live Ask Quote**: `26643.41` | **Mid Price**: `26642.17`
- **Spread Points**: `247.00` | **Spread BPS**: `0.93 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26642.17` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.61` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26828.67` | Lower -3.00σ Band: `26455.68`
  * Upper +2.51σ Band: `26788.71` | Lower -2.51σ Band: `26495.64`
  * Upper +2.01σ Band: `26754.07` | Lower -2.01σ Band: `26530.28`
  * Upper +2.00σ Band: `26748.74` | Lower -2.00σ Band: `26535.61`
  * Upper +1.28σ Band: `26716.77` | Lower -1.28σ Band: `26567.58`
  * Upper +1.00σ Band: `26695.46` | Lower -1.00σ Band: `26588.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26642.17` | EMA-20=`26642.17` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26642.17` (Slope: `+0.0000`) | EMA-100=`26642.17`
  * Institutional Anchors: EMA-144=`26642.17` | EMA-200=`26642.17` (Slope: `+0.0000`) | EMA-233=`26642.17`
- **Range Boundaries**: 24H High=`26908.60` | 24H Low=`26375.75` | Weekly High=`27175.02` | Weekly Low=`26109.33`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26722.10` (Distance: `+0.00%`)
  * Point of Control (POC) = `26642.17` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26562.25` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26748.74` | POC=`26642.17` | VAL=`26535.61`
  * Prior Day Extremes: PDH=`26802.03` | PDL=`26482.32` | PDC=`26642.17`
  * Monday Range Blueprint: High=`26775.39` | Mid=`26642.17` | Low=`26508.96`
  * Developing Weekly Value Area: Weekly VAH=`26855.31` | Weekly POC=`26642.17` | Weekly VAL=`26429.04`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26695.46` | Low=`26588.89`
  * London Session (08:00-16:00 UTC): High=`26748.74` | Low=`26535.61`
  * New York Session (13:00-21:00 UTC): High=`26802.03` | Low=`26482.32`
  * Initial Balance (First Hour): IB High=`26722.10` | IB Low=`26562.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26535.61` - `26748.74`
  * Optimal Trade Entry (OTE 0.705): `26695.46`
  * Structural Invalidation Anchor (0.786): `26855.31`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,997,585.96 USD | `6,489.82` | `4185.46` | `4008.60` | `32398.42` | 1,165,365.05 USD | `+4.48%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,351,813.16 USD | `6,324.04` | `4130.10` | `4008.60` | `14043.82` | 767,146.39 USD | `+3.03%` | `5X Cross` |
| `59` | `0xb83d...6e36` | `SHORT` | 23,535,948.63 USD | `5,869.90` | `4228.86` | `4008.60` | `29873.68` | 1,287,073.30 USD | `+5.47%` | `5X Cross` |
| `94` | `0xec0b...b078` | `LONG` | 19,360,053.54 USD | `4,828.91` | `4157.43` | `4008.60` | `2380.95` | -715,828.77 USD | `-3.70%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,151,561.21 USD | `3,532.68` | `4128.55` | `4008.60` | `579.90` | -433,292.52 USD | `-3.06%` | `3X Cross` |
| `155` | `0x7a6d...f79c` | `SHORT` | 13,100,305.79 USD | `3,268.21` | `4228.94` | `4008.60` | `4402.23` | 720,773.34 USD | `+5.50%` | `25X Cross` |
| `172` | `0xa742...e390` | `SHORT` | 11,625,230.40 USD | `2,900.00` | `4364.92` | `4008.60` | `4235.80` | 1,033,045.93 USD | `+8.89%` | `20X Cross` |
| `252` | `0x41e5...0825` | `SHORT` | 8,821,120.00 USD | `2,200.00` | `4112.20` | `4008.60` | `4331.28` | 225,734.59 USD | `+2.56%` | `20X Cross` |
| `253` | `0x3678...b209` | `LONG` | 8,812,980.00 USD | `2,200.00` | `4176.09` | `4008.60` | `2820.58` | -374,439.30 USD | `-4.25%` | `25X Cross` |
| `292` | `0xacb6...efbd` | `SHORT` | 7,919,649.80 USD | `1,975.37` | `4048.55` | `4008.60` | `6572.40` | 77,741.92 USD | `+0.98%` | `6X Cross` |
| `355` | `0xc26c...b8f4` | `LONG` | 6,329,128.92 USD | `1,579.95` | `4075.62` | `4008.60` | `0.000000` | -110,168.05 USD | `-1.74%` | `1X Cross` |
| `468` | `0x354b...6425` | `LONG` | 4,562,001.57 USD | `1,138.00` | `4004.98` | `4008.60` | `0.000000` | 4,341.22 USD | `+0.10%` | `10X Cross` |
| `539` | `0x63da...8add` | `LONG` | 4,005,900.00 USD | `1,000.00` | `4021.46` | `4008.60` | `3564.24` | -15,560.96 USD | `-0.39%` | `25X Cross` |
| `551` | `0x9aa5...58af` | `LONG` | 3,895,507.11 USD | `971.64` | `4279.98` | `4008.60` | `0.000000` | -263,101.98 USD | `-6.75%` | `20X Cross` |
| `592` | `0xf3dc...1672` | `LONG` | 3,705,475.35 USD | `924.34` | `4019.12` | `4008.60` | `2838.70` | -9,540.83 USD | `-0.26%` | `20X Cross` |
| `650` | `0x4a20...3c26` | `LONG` | 3,354,539.46 USD | `837.40` | `4599.73` | `4008.60` | `0.000000` | -497,280.92 USD | `-14.82%` | `20X Cross` |
| `810` | `0x0fac...7a0a` | `LONG` | 2,751,981.07 USD | `686.49` | `4290.34` | `4008.60` | `1650.27` | -193,277.64 USD | `-7.02%` | `25X Cross` |
| `877` | `0xd8c5...99b0` | `SHORT` | 2,525,138.69 USD | `630.35` | `4175.35` | `4008.60` | `33897.13` | 106,818.20 USD | `+4.23%` | `4X Cross` |
| `887` | `0x625e...a354` | `SHORT` | 2,485,952.00 USD | `620.00` | `4122.81` | `4008.60` | `4342.38` | 70,195.03 USD | `+2.82%` | `20X Cross` |
| `913` | `0xeae3...e8ad` | `SHORT` | 2,403,540.00 USD | `600.00` | `4104.77` | `4008.60` | `4325.40` | 59,325.11 USD | `+2.47%` | `20X Cross` |
| `916` | `0xf285...fa82` | `LONG` | 2,397,866.36 USD | `598.11` | `4146.45` | `4008.60` | `3891.38` | -82,153.19 USD | `-3.43%` | `25X Cross` |
| `937` | `0x12f7...8750` | `LONG` | 2,345,897.90 USD | `585.61` | `4082.77` | `4008.60` | `2955.09` | -45,019.08 USD | `-1.92%` | `10X Cross` |
| `1065` | `0x413c...886c` | `LONG` | 2,004,400.00 USD | `500.00` | `4010.43` | `4008.60` | `0.000000` | -816.23 USD | `-0.04%` | `2X Cross` |
| `1068` | `0x61ce...a62b` | `SHORT` | 1,994,392.03 USD | `497.50` | `4071.66` | `4008.60` | `4737.33` | 31,276.76 USD | `+1.57%` | `20X Cross` |
| `1181` | `0xead5...69f2` | `LONG` | 1,819,491.93 USD | `453.78` | `4220.88` | `4008.60` | `3539.07` | -95,876.13 USD | `-5.27%` | `5X Isolated` |
| `1282` | `0x46fc...1195` | `LONG` | 1,665,316.08 USD | `415.36` | `4054.40` | `4008.60` | `2237.39` | -18,735.53 USD | `-1.13%` | `20X Cross` |
| `1320` | `0x6d15...d374` | `LONG` | 1,603,840.00 USD | `400.00` | `4068.25` | `4008.60` | `3841.94` | -23,460.00 USD | `-1.46%` | `25X Cross` |
| `1323` | `0xee02...309d` | `SHORT` | 1,603,480.00 USD | `400.00` | `4438.84` | `4008.60` | `4227.02` | 172,058.60 USD | `+10.73%` | `25X Isolated` |
| `1355` | `0x02a7...fe9f` | `SHORT` | 1,562,301.00 USD | `390.00` | `4055.02` | `4008.60` | `4306.83` | 19,158.25 USD | `+1.23%` | `25X Cross` |
| `1401` | `0x7e77...b8d2` | `SHORT` | 1,522,242.00 USD | `380.00` | `4131.92` | `4008.60` | `4293.64` | 47,887.64 USD | `+3.15%` | `20X Cross` |
| `1421` | `0x72c2...9b37` | `LONG` | 1,495,808.76 USD | `373.13` | `4000.98` | `4008.60` | `3778.18` | 2,915.24 USD | `+0.19%` | `13X Isolated` |
| `1423` | `0x9c06...0560` | `LONG` | 1,495,245.84 USD | `373.26` | `4018.98` | `4008.60` | `0.000000` | -4,885.97 USD | `-0.33%` | `25X Cross` |
| `1464` | `0xaa44...b844` | `LONG` | 1,442,124.00 USD | `360.00` | `4043.10` | `4008.60` | `2824.98` | -13,393.63 USD | `-0.93%` | `4X Cross` |
| `1580` | `0xa41f...d50a` | `LONG` | 1,318,874.85 USD | `328.96` | `4468.89` | `4008.60` | `3802.30` | -151,223.00 USD | `-11.47%` | `15X Cross` |
| `1589` | `0x7fda...17d1` | `SHORT` | 1,306,622.34 USD | `325.91` | `4013.13` | `4008.60` | `30143.10` | 1,281.22 USD | `+0.10%` | `20X Cross` |
| `1618` | `0xbf5a...88ba` | `SHORT` | 1,273,510.26 USD | `317.65` | `4091.80` | `4008.60` | `9689.94` | 26,272.77 USD | `+2.06%` | `20X Cross` |
| `1645` | `0xff31...ff6c` | `SHORT` | 1,242,511.00 USD | `310.00` | `4372.43` | `4008.60` | `4789.31` | 112,944.38 USD | `+9.09%` | `10X Isolated` |
| `1680` | `0xada6...6f88` | `LONG` | 1,216,661.98 USD | `303.50` | `4166.46` | `4008.60` | `1809.40` | -47,850.88 USD | `-3.93%` | `5X Cross` |
| `1827` | `0x50e2...d770` | `LONG` | 1,083,064.77 USD | `270.37` | `4243.58` | `4008.60` | `2562.23` | -64,261.69 USD | `-5.93%` | `20X Cross` |
| `1850` | `0x4c92...4f17` | `SHORT` | 1,068,455.65 USD | `266.72` | `4260.98` | `4008.60` | `6484.56` | 68,036.59 USD | `+6.37%` | `20X Cross` |
| `1903` | `0xd346...c4f3` | `LONG` | 1,023,017.28 USD | `255.17` | `4188.66` | `4008.60` | `3310.56` | -45,819.23 USD | `-4.48%` | `5X Isolated` |
| `1950` | `0xe47f...758c` | `LONG` | 1,002,200.00 USD | `250.00` | `4017.99` | `4008.60` | `3737.09` | -2,299.86 USD | `-0.23%` | `20X Cross` |

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
  * Total Open Interest: `816.21M` | Total OI Tokens: `203,931.9 XAUT`
  * 1h OI Change: `+1.05%` | 4h OI Change: `-1.24%` | 24h OI Change: `-4.50%`
  * Exchange Breakdown: Binance=`60.71M` | Bybit=`143.85M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `38.32%` | `61.68%` | `0.62` | 4,150,000.00 USD |
| `15M` | `Binance` | `39.52%` | `60.48%` | `0.65` | 1,400,000.00 USD |
| `15M` | `OKX` | `40.2%` | `59.8%` | `0.67` | 986,600.00 USD |
| `15M` | `Bybit` | `28.65%` | `71.35%` | `0.40` | 445,130.00 USD |
| `15M` | `KuCoin` | `47.53%` | `52.47%` | `0.91` | 159,490.00 USD |
| `15M` | `Gate` | `27.93%` | `72.07%` | `0.39` | 86,150.00 USD |
| `15M` | `Bitget` | `42.1%` | `57.9%` | `0.73` | 36,180.00 USD |
| `15M` | `BingX` | `14.82%` | `85.18%` | `0.17` | 226,940.00 USD |
| `15M` | `MEXC` | `58.42%` | `41.58%` | `1.41` | 60,510.00 USD |
| `15M` | `Bitunix` | `25.02%` | `74.98%` | `0.33` | 102,860.00 USD |
| `15M` | `Hyperliquid` | `74.62%` | `25.38%` | `2.94` | 45,110.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.08%` | `47.92%` | `1.09` | 515,360.00 USD |
| `15M` | `Crypto.com` | `53.85%` | `46.15%` | `1.17` | 35.35 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 77,090.00 USD |
| `15M` | `HTX` | `19.42%` | `80.58%` | `0.24` | 1,700.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0.68%` | `99.32%` | `0.01` | 5,180.00 USD |
| `15M` | `Aster` | `21.99%` | `78.01%` | `0.28` | 159.42 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `31.37%` | `68.63%` | `0.46` | 794.09 USD |
| `15M` | `Whale Positions` | `39.52%` | `60.48%` | `0.65` | 1,400,000.00 USD |
| `15M` | `Global Accounts` | `38.32%` | `61.68%` | `0.62` | 4,150,000.00 USD |
| `1H` | `XAUT` | `51.06%` | `48.94%` | `1.04` | 17,020,000.00 USD |
| `1H` | `Binance` | `48.27%` | `51.73%` | `0.93` | 5,740,000.00 USD |
| `1H` | `OKX` | `48.77%` | `51.23%` | `0.95` | 2,420,000.00 USD |
| `1H` | `Bybit` | `55.81%` | `44.19%` | `1.26` | 1,600,000.00 USD |
| `1H` | `KuCoin` | `34.84%` | `65.16%` | `0.53` | 152,890.00 USD |
| `1H` | `Gate` | `46.33%` | `53.67%` | `0.86` | 1,180,000.00 USD |
| `1H` | `Bitget` | `48.57%` | `51.43%` | `0.94` | 478,470.00 USD |
| `1H` | `BingX` | `48.61%` | `51.39%` | `0.95` | 2,160,000.00 USD |
| `1H` | `MEXC` | `49.79%` | `50.21%` | `0.99` | 365,440.00 USD |
| `1H` | `Bitunix` | `75.97%` | `24.03%` | `3.16` | 472,830.00 USD |
| `1H` | `Hyperliquid` | `31.49%` | `68.51%` | `0.46` | 903,550.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.02%` | `48.98%` | `1.04` | 601,830.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `93.33%` | `6.67%` | `13.99` | 802,120.00 USD |
| `1H` | `HTX` | `48.96%` | `51.04%` | `0.96` | 20,010.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.56%` | `45.44%` | `1.20` | 52,740.00 USD |
| `1H` | `Aster` | `61.51%` | `38.49%` | `1.60` | 59,430.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `61.14%` | `38.86%` | `1.57` | 10,470.00 USD |
| `1H` | `Whale Positions` | `48.27%` | `51.73%` | `0.93` | 5,740,000.00 USD |
| `1H` | `Global Accounts` | `51.06%` | `48.94%` | `1.04` | 17,020,000.00 USD |
| `4H` | `XAUT` | `48.94%` | `51.06%` | `0.96` | 97,980,000.00 USD |
| `4H` | `Binance` | `47.07%` | `52.93%` | `0.89` | 34,160,000.00 USD |
| `4H` | `OKX` | `48.3%` | `51.7%` | `0.93` | 12,790,000.00 USD |
| `4H` | `Bybit` | `51.22%` | `48.78%` | `1.05` | 11,210,000.00 USD |
| `4H` | `KuCoin` | `40.19%` | `59.81%` | `0.67` | 1,370,000.00 USD |
| `4H` | `Gate` | `46.62%` | `53.38%` | `0.87` | 5,540,000.00 USD |
| `4H` | `Bitget` | `49.39%` | `50.61%` | `0.98` | 2,550,000.00 USD |
| `4H` | `BingX` | `45.62%` | `54.38%` | `0.84` | 9,820,000.00 USD |
| `4H` | `MEXC` | `37.26%` | `62.74%` | `0.59` | 4,000,000.00 USD |
| `4H` | `Bitunix` | `51%` | `49%` | `1.04` | 2,350,000.00 USD |
| `4H` | `Hyperliquid` | `43.45%` | `56.55%` | `0.77` | 2,940,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.02%` | `49.98%` | `1.00` | 2,740,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `73.92%` | `26.08%` | `2.83` | 6,950,000.00 USD |
| `4H` | `HTX` | `53.5%` | `46.5%` | `1.15` | 221,630.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `33.97%` | `66.03%` | `0.51` | 720,760.00 USD |
| `4H` | `Aster` | `43.89%` | `56.11%` | `0.78` | 465,530.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `22.23%` | `77.77%` | `0.29` | 151,190.00 USD |
| `4H` | `Whale Positions` | `47.07%` | `52.93%` | `0.89` | 34,160,000.00 USD |
| `4H` | `Global Accounts` | `48.94%` | `51.06%` | `0.96` | 97,980,000.00 USD |


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
| `5m` | 88,460.00 USD | 6,170.00 USD | **`ACCUMULATION`** |
| `15m` | 70,190.00 USD | -202,890.00 USD | **`DISTRIBUTION`** |
| `30m` | -68,070.00 USD | -148,910.00 USD | **`DISTRIBUTION`** |
| `1h` | -261,540.00 USD | -177,660.00 USD | **`DISTRIBUTION`** |
| `2h` | -366,850.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -828,910.00 USD | -2,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,030,000.00 USD | -1,570,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,330,000.00 USD | -891,600.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,690,000.00 USD | -716,920.00 USD | **`DISTRIBUTION`** |
| `24h` | 704,540.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -78,930,000.00 USD | -19,590,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -179,920,000.00 USD | -84,580,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+88.46K` | 15m=`+70.19K` | 1h=`-261.54K` | 24h=`+704.54K`
* Futures Capital Netflows: 5m=`+6.17K` | 15m=`-202.89K` | 1h=`-177.66K` | 24h=`-1.11M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26562.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26478.62` (Risk Distance: `83.63` pts)
  * +2.5R Take Profit: `26771.33`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26722.10` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26805.73` (Risk Distance: `83.63` pts)
  * +2.5R Take Profit: `26513.02`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.84 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26855.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
