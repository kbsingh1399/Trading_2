# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:14:11 IST` (`2026-10-30 05:44:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26641.21` | **Live Ask Quote**: `26643.45` | **Mid Price**: `26642.33`
- **Spread Points**: `224.00` | **Spread BPS**: `0.84 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26642.33` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.61` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26828.83` | Lower -3.00σ Band: `26455.83`
  * Upper +2.51σ Band: `26788.86` | Lower -2.51σ Band: `26495.80`
  * Upper +2.01σ Band: `26754.23` | Lower -2.01σ Band: `26530.43`
  * Upper +2.00σ Band: `26748.90` | Lower -2.00σ Band: `26535.76`
  * Upper +1.28σ Band: `26716.93` | Lower -1.28σ Band: `26567.73`
  * Upper +1.00σ Band: `26695.61` | Lower -1.00σ Band: `26589.05`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26642.33` | EMA-20=`26642.33` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26642.33` (Slope: `+0.0000`) | EMA-100=`26642.33`
  * Institutional Anchors: EMA-144=`26642.33` | EMA-200=`26642.33` (Slope: `+0.0000`) | EMA-233=`26642.33`
- **Range Boundaries**: 24H High=`26908.75` | 24H Low=`26375.91` | Weekly High=`27175.18` | Weekly Low=`26109.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26722.26` (Distance: `+0.00%`)
  * Point of Control (POC) = `26642.33` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26562.40` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26748.90` | POC=`26642.33` | VAL=`26535.76`
  * Prior Day Extremes: PDH=`26802.18` | PDL=`26482.48` | PDC=`26642.33`
  * Monday Range Blueprint: High=`26775.54` | Mid=`26642.33` | Low=`26509.12`
  * Developing Weekly Value Area: Weekly VAH=`26855.47` | Weekly POC=`26642.33` | Weekly VAL=`26429.19`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26695.61` | Low=`26589.05`
  * London Session (08:00-16:00 UTC): High=`26748.90` | Low=`26535.76`
  * New York Session (13:00-21:00 UTC): High=`26802.18` | Low=`26482.48`
  * Initial Balance (First Hour): IB High=`26722.26` | IB Low=`26562.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26535.76` - `26748.90`
  * Optimal Trade Entry (OTE 0.705): `26695.61`
  * Structural Invalidation Anchor (0.786): `26855.47`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 26,000,830.87 USD | `6,489.82` | `4185.46` | `4007.30` | `29210.89` | 1,162,120.14 USD | `+4.47%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,308,168.21 USD | `6,316.15` | `4129.00` | `4007.30` | `13940.65` | 771,205.80 USD | `+3.05%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,520,099.91 USD | `5,869.90` | `4228.86` | `4007.30` | `26885.02` | 1,302,922.03 USD | `+5.54%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,347,015.49 USD | `4,828.91` | `4157.43` | `4007.30` | `2265.26` | -728,866.82 USD | `-3.77%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,229,689.93 USD | `3,551.74` | `4127.81` | `4007.30` | `590.97` | -431,247.07 USD | `-3.03%` | `3X Cross` |
| `160` | `0x7a6d...f79c` | `SHORT` | 13,093,769.36 USD | `3,268.21` | `4228.94` | `4007.30` | `4374.56` | 727,309.77 USD | `+5.55%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,618,560.40 USD | `2,900.00` | `4364.92` | `4007.30` | `4235.92` | 1,039,715.93 USD | `+8.95%` | `20X Cross` |
| `263` | `0x41e5...0825` | `SHORT` | 8,815,180.00 USD | `2,200.00` | `4112.20` | `4007.30` | `4331.40` | 231,674.59 USD | `+2.63%` | `20X Cross` |
| `264` | `0x3678...b209` | `LONG` | 8,814,300.00 USD | `2,200.00` | `4176.09` | `4007.30` | `2584.47` | -373,119.30 USD | `-4.23%` | `25X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,915,106.45 USD | `1,975.37` | `4048.55` | `4007.30` | `6556.78` | 82,285.27 USD | `+1.04%` | `6X Cross` |
| `364` | `0xc26c...b8f4` | `LONG` | 6,330,234.88 USD | `1,579.95` | `4075.62` | `4007.30` | `0.000000` | -109,062.09 USD | `-1.72%` | `1X Cross` |
| `567` | `0x63da...8add` | `LONG` | 4,006,400.00 USD | `1,000.00` | `4021.46` | `4007.30` | `3564.37` | -15,060.96 USD | `-0.38%` | `25X Cross` |
| `574` | `0xf3dc...1672` | `LONG` | 3,943,382.13 USD | `984.27` | `4018.39` | `4007.30` | `2908.52` | -11,804.56 USD | `-0.30%` | `20X Cross` |
| `589` | `0x9aa5...58af` | `LONG` | 3,892,883.67 USD | `971.64` | `4279.98` | `4007.30` | `0.000000` | -265,725.41 USD | `-6.83%` | `20X Cross` |
| `594` | `0x354b...6425` | `LONG` | 3,841,365.97 USD | `958.81` | `4004.93` | `4007.30` | `0.000000` | 1,404.75 USD | `+0.04%` | `10X Cross` |
| `677` | `0x4a20...3c26` | `LONG` | 3,355,041.90 USD | `837.40` | `4599.73` | `4007.30` | `0.000000` | -496,778.48 USD | `-14.81%` | `20X Cross` |
| `831` | `0x0fac...7a0a` | `LONG` | 2,750,402.15 USD | `686.49` | `4290.34` | `4007.30` | `1131.97` | -194,856.55 USD | `-7.08%` | `25X Cross` |
| `906` | `0x625e...a354` | `SHORT` | 2,484,278.00 USD | `620.00` | `4122.81` | `4007.00` | `4342.50` | 71,869.03 USD | `+2.89%` | `20X Cross` |
| `911` | `0xd8c5...99b0` | `SHORT` | 2,477,438.91 USD | `618.35` | `4175.35` | `4007.00` | `34099.13` | 104,413.70 USD | `+4.21%` | `4X Cross` |
| `937` | `0xeae3...e8ad` | `SHORT` | 2,403,900.00 USD | `600.00` | `4104.77` | `4007.00` | `4325.52` | 58,965.11 USD | `+2.45%` | `20X Cross` |
| `939` | `0xf285...fa82` | `LONG` | 2,396,251.48 USD | `598.11` | `4146.45` | `4007.00` | `3891.51` | -83,768.07 USD | `-3.50%` | `25X Cross` |
| `956` | `0x12f7...8750` | `LONG` | 2,346,190.71 USD | `585.61` | `4082.77` | `4007.00` | `2580.91` | -44,726.27 USD | `-1.91%` | `10X Cross` |
| `1096` | `0x413c...886c` | `LONG` | 2,003,750.00 USD | `500.00` | `4010.43` | `4007.00` | `0.000000` | -1,466.23 USD | `-0.07%` | `2X Cross` |
| `1103` | `0x9c06...0560` | `LONG` | 1,996,859.07 USD | `498.42` | `4012.76` | `4007.00` | `0.000000` | -3,172.43 USD | `-0.16%` | `25X Cross` |
| `1105` | `0x61ce...a62b` | `SHORT` | 1,993,198.02 USD | `497.50` | `4071.66` | `4007.00` | `4715.08` | 32,470.77 USD | `+1.63%` | `20X Cross` |
| `1215` | `0xead5...69f2` | `LONG` | 1,818,266.71 USD | `453.78` | `4220.88` | `4007.00` | `3539.20` | -97,101.35 USD | `-5.34%` | `5X Isolated` |
| `1304` | `0x46fc...1195` | `LONG` | 1,662,354.22 USD | `414.87` | `4053.27` | `4007.00` | `2131.61` | -19,238.62 USD | `-1.16%` | `20X Cross` |
| `1349` | `0x6d15...d374` | `LONG` | 1,602,760.00 USD | `400.00` | `4068.25` | `4007.00` | `3842.07` | -24,540.00 USD | `-1.53%` | `25X Cross` |
| `1350` | `0xee02...309d` | `SHORT` | 1,602,560.00 USD | `400.00` | `4438.84` | `4007.00` | `4227.14` | 172,978.60 USD | `+10.79%` | `25X Isolated` |
| `1395` | `0x02a7...fe9f` | `SHORT` | 1,562,496.00 USD | `390.00` | `4055.02` | `4007.00` | `4306.96` | 18,963.25 USD | `+1.21%` | `25X Cross` |
| `1437` | `0x7e77...b8d2` | `SHORT` | 1,522,470.00 USD | `380.00` | `4131.92` | `4007.00` | `4293.77` | 47,659.64 USD | `+3.13%` | `20X Cross` |
| `1461` | `0x72c2...9b37` | `LONG` | 1,494,913.24 USD | `373.13` | `4000.98` | `4007.00` | `3778.31` | 2,019.72 USD | `+0.14%` | `13X Isolated` |
| `1508` | `0xaa44...b844` | `LONG` | 1,442,304.00 USD | `360.00` | `4043.10` | `4007.00` | `2819.34` | -13,213.63 USD | `-0.92%` | `4X Cross` |
| `1609` | `0xa41f...d50a` | `LONG` | 1,317,986.65 USD | `328.96` | `4468.89` | `4007.00` | `3802.43` | -152,111.20 USD | `-11.54%` | `15X Cross` |
| `1627` | `0x7fda...17d1` | `SHORT` | 1,301,439.81 USD | `324.83` | `4013.13` | `4007.00` | `30340.41` | 2,154.04 USD | `+0.17%` | `20X Cross` |
| `1662` | `0xbf5a...88ba` | `SHORT` | 1,272,652.59 USD | `317.65` | `4091.80` | `4007.00` | `10008.19` | 27,130.44 USD | `+2.13%` | `20X Cross` |
| `1694` | `0xff31...ff6c` | `SHORT` | 1,242,015.00 USD | `310.00` | `4372.43` | `4007.00` | `4789.43` | 113,440.38 USD | `+9.13%` | `10X Isolated` |
| `1719` | `0xada6...6f88` | `LONG` | 1,215,933.59 USD | `303.50` | `4166.46` | `4007.00` | `1789.16` | -48,579.28 USD | `-4.00%` | `5X Cross` |
| `1887` | `0x50e2...d770` | `LONG` | 1,083,335.14 USD | `270.37` | `4243.58` | `4007.00` | `2562.36` | -63,991.33 USD | `-5.91%` | `20X Cross` |
| `1899` | `0x4c92...4f17` | `SHORT` | 1,068,589.01 USD | `266.72` | `4260.98` | `4007.00` | `6513.28` | 67,903.23 USD | `+6.35%` | `20X Cross` |
| `1977` | `0xd346...c4f3` | `LONG` | 1,022,328.31 USD | `255.17` | `4188.66` | `4007.00` | `3310.69` | -46,508.20 USD | `-4.55%` | `5X Isolated` |

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
| `7D` | `3589.40` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.10` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `3593.70` | 22,440,000.00 USD | 0.00 USD | 22,440,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3595.30` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 24,410.00 USD | 0.00 USD | 19,250.00 USD |
| `7D` | `3598.00` | 22,190,000.00 USD | 0.00 USD | 22,190,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3599.50` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 1,490.00 USD | 0.00 USD | 34,940.00 USD |
| `7D` | `3602.30` | 21,770,000.00 USD | 0.00 USD | 21,770,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3603.70` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 11,380.00 USD | 0.00 USD | 31,900.00 USD |
| `7D` | `3606.60` | 21,550,000.00 USD | 0.00 USD | 21,550,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3607.90` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 18,250.00 USD | 0.00 USD | 64,400.00 USD |
| `7D` | `3610.90` | 21,420,000.00 USD | 0.00 USD | 21,420,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.10` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 17,620.00 USD | 0.00 USD | 26,900.00 USD |
| `7D` | `3615.20` | 21,310,000.00 USD | 0.00 USD | 21,310,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.30` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.50` | 21,240,000.00 USD | 0.00 USD | 21,240,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.50` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 21,740.00 USD | 0.00 USD | 66,750.00 USD |
| `7D` | `3623.80` | 21,120,000.00 USD | 0.00 USD | 21,120,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3624.70` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 22,580.00 USD | 0.00 USD | 37,460.00 USD |
| `7D` | `3628.10` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 47,240.00 USD | 0.00 USD | 35,770.00 USD |
| `1D` | `3628.90` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 6,460.00 USD | 0.00 USD | 22,590.00 USD |
| `7D` | `3632.40` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3633.10` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 620.53 USD | 0.00 USD | 5,000.00 USD |
| `7D` | `3636.70` | 20,740,000.00 USD | 0.00 USD | 20,740,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.00` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,570,000.00 USD | 0.00 USD | 20,570,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,560,000.00 USD | 0.00 USD | 20,560,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,550,000.00 USD | 0.00 USD | 20,550,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `7D` | `3830.20` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3830.50` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `3834.50` | 19,990,000.00 USD | 0.00 USD | 19,990,000.00 USD | 284,980.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3834.70` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 87,400.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `3838.80` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 311,710.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3838.90` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 22,350.00 USD | 0.00 USD | 119,800.00 USD |
| `1D` | `3843.10` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 28,460.00 USD | 0.00 USD | 97,130.00 USD |
| `7D` | `3843.10` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 291,740.00 USD | 0.00 USD | 359,480.00 USD |
| `1D` | `3847.30` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 66,000.00 USD | 0.00 USD | 187,980.00 USD |
| `7D` | `3847.40` | 17,390,000.00 USD | 0.00 USD | 17,390,000.00 USD | 115,590.00 USD | 0.00 USD | 366,480.00 USD |
| `1D` | `3851.50` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 73,320.00 USD | 0.00 USD | 129,680.00 USD |
| `7D` | `3851.70` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3855.70` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 27,220.00 USD | 0.00 USD | 99,710.00 USD |
| `7D` | `3856.00` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3859.90` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 68,340.00 USD | 0.00 USD | 112,500.00 USD |
| `7D` | `3860.30` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3864.10` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 100,000.00 USD | 0.00 USD | 215,080.00 USD |
| `7D` | `3864.60` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3868.30` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 42,000.00 USD | 0.00 USD | 70,520.00 USD |
| `7D` | `3868.90` | 15,400,000.00 USD | 0.00 USD | 15,400,000.00 USD | 192,180.00 USD | 0.00 USD | 200,860.00 USD |
| `1D` | `3872.50` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 10,390.00 USD | 0.00 USD | 72,870.00 USD |
| `7D` | `3873.20` | 15,010,000.00 USD | 0.00 USD | 15,010,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `1D` | `3876.70` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 1,550.00 USD | 0.00 USD | 2,020.00 USD |
| `7D` | `3877.50` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `7D` | `3881.80` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `1D` | `3910.30` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `3911.90` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3914.50` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 174,800.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `3916.20` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 711,980.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3918.70` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 44,700.00 USD | 0.00 USD | 186,400.00 USD |
| `7D` | `3920.50` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 681,530.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3922.90` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 56,910.00 USD | 0.00 USD | 247,470.00 USD |
| `7D` | `3924.80` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 269,290.00 USD | 0.00 USD | 470,810.00 USD |
| `1D` | `3927.10` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 114,120.00 USD | 0.00 USD | 366,360.00 USD |
| `7D` | `3929.10` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 184,740.00 USD | 0.00 USD | 836,390.00 USD |
| `1D` | `3931.30` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 162,220.00 USD | 0.00 USD | 249,590.00 USD |
| `7D` | `3933.40` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3935.50` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 22,890.00 USD | 0.00 USD | 208,370.00 USD |
| `7D` | `3937.70` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3939.70` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 149,180.00 USD | 0.00 USD | 198,540.00 USD |
| `7D` | `3942.00` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3943.90` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 180,760.00 USD | 0.00 USD | 412,900.00 USD |
| `7D` | `3946.30` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.10` | 493,440.00 USD | 0.00 USD | 493,440.00 USD | 120,660.00 USD | 0.00 USD | 184,750.00 USD |
| `7D` | `3950.60` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 333,580.00 USD | 0.00 USD | 402,490.00 USD |
| `1D` | `3952.30` | 188,020.00 USD | 0.00 USD | 188,020.00 USD | 22,840.00 USD | 0.00 USD | 156,180.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `1D` | `3956.50` | 9,010.00 USD | 0.00 USD | 9,010.00 USD | 4,970.00 USD | 0.00 USD | 4,040.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `1D` | `4005.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4005.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `1D` | `4069.90` | 59,730.00 USD | 59,730.00 USD | 0.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4074.10` | 310,720.00 USD | 310,720.00 USD | 0.00 USD | 166,380.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,700.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4078.30` | 541,240.00 USD | 541,240.00 USD | 0.00 USD | 53,120.00 USD | 0.00 USD | 177,410.00 USD |
| `7D` | `4079.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 657,780.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4082.50` | 827,630.00 USD | 827,630.00 USD | 0.00 USD | 56,910.00 USD | 0.00 USD | 229,470.00 USD |
| `7D` | `4083.90` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 390,080.00 USD | 0.00 USD | 674,150.00 USD |
| `1D` | `4086.70` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 99,170.00 USD | 0.00 USD | 314,560.00 USD |
| `7D` | `4088.20` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 821,070.00 USD |
| `1D` | `4090.90` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 158,790.00 USD | 0.00 USD | 259,780.00 USD |
| `7D` | `4092.50` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4095.10` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 33,980.00 USD | 0.00 USD | 176,600.00 USD |
| `7D` | `4096.80` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4099.30` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 113,960.00 USD | 0.00 USD | 197,190.00 USD |
| `7D` | `4101.10` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4103.50` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 172,480.00 USD | 0.00 USD | 409,020.00 USD |
| `7D` | `4105.40` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4107.70` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 138,120.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `4109.70` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 297,980.00 USD |
| `1D` | `4111.90` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 51,400.00 USD | 0.00 USD | 120,860.00 USD |
| `7D` | `4114.00` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4116.10` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 9,750.00 USD | 0.00 USD | 105,470.00 USD |
| `7D` | `4118.30` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `7D` | `4122.60` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,900,000.00 USD | 12,900,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `4152.70` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.90` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 83,190.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `4157.00` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 318,580.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4158.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 26,560.00 USD | 0.00 USD | 88,700.00 USD |
| `7D` | `4161.30` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 325,310.00 USD | 0.00 USD | 513,530.00 USD |
| `1D` | `4162.30` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 28,460.00 USD | 0.00 USD | 93,520.00 USD |
| `7D` | `4165.60` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 114,110.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4166.50` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 35,670.00 USD | 0.00 USD | 126,640.00 USD |
| `7D` | `4169.90` | 17,280,000.00 USD | 17,280,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 251,660.00 USD |
| `1D` | `4170.70` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 83,520.00 USD | 0.00 USD | 164,850.00 USD |
| `7D` | `4174.20` | 17,660,000.00 USD | 17,660,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4174.90` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 26,780.00 USD | 0.00 USD | 95,550.00 USD |
| `7D` | `4178.50` | 17,900,000.00 USD | 17,900,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4179.10` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | 104,490.00 USD |
| `7D` | `4182.80` | 18,240,000.00 USD | 18,240,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4183.30` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 162,760.00 USD |
| `7D` | `4187.10` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4187.50` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 85,680.00 USD | 0.00 USD | 146,440.00 USD |
| `7D` | `4191.40` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 192,800.00 USD |
| `1D` | `4191.70` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 25,700.00 USD | 0.00 USD | 55,210.00 USD |
| `7D` | `4195.70` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4195.90` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 4,870.00 USD | 0.00 USD | 69,130.00 USD |
| `7D` | `4200.00` | 19,630,000.00 USD | 19,630,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `7D` | `4204.30` | 19,850,000.00 USD | 19,850,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,250,000.00 USD | 20,250,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,370,000.00 USD | 20,370,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,410,000.00 USD | 20,410,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `4389.10` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4389.20` | 20,570,000.00 USD | 20,570,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4393.30` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 9,110.00 USD |
| `7D` | `4393.50` | 20,770,000.00 USD | 20,770,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4397.50` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 7,610.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4397.80` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4401.70` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 11,380.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4402.10` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `1D` | `4405.90` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | 19,570.00 USD |
| `7D` | `4406.40` | 21,460,000.00 USD | 21,460,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `1D` | `4410.10` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 13,560.00 USD | 0.00 USD | 58,710.00 USD |
| `7D` | `4410.70` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `1D` | `4413.90` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 17,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4415.00` | 21,590,000.00 USD | 21,590,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,750,000.00 USD | 21,750,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
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
  * Total Open Interest: `794.11M` | Total OI Tokens: `198,120.6 XAUT`
  * 1h OI Change: `-1.87%` | 4h OI Change: `-1.17%` | 24h OI Change: `-6.56%`
  * Exchange Breakdown: Binance=`61.22M` | Bybit=`145.06M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `44.29%` | `55.71%` | `0.80` | 1,330,000.00 USD |
| `15M` | `Binance` | `44.43%` | `55.57%` | `0.80` | 232,740.00 USD |
| `15M` | `OKX` | `57.89%` | `42.11%` | `1.37` | 137,110.00 USD |
| `15M` | `Bybit` | `43.16%` | `56.84%` | `0.76` | 95,930.00 USD |
| `15M` | `KuCoin` | `50.04%` | `49.96%` | `1.00` | 162,640.00 USD |
| `15M` | `Gate` | `42.54%` | `57.46%` | `0.74` | 19,680.00 USD |
| `15M` | `Bitget` | `57.8%` | `42.2%` | `1.37` | 170,920.00 USD |
| `15M` | `BingX` | `27.52%` | `72.48%` | `0.38` | 358,610.00 USD |
| `15M` | `MEXC` | `55.21%` | `44.79%` | `1.23` | 47,250.00 USD |
| `15M` | `Bitunix` | `17.43%` | `82.57%` | `0.21` | 22,820.00 USD |
| `15M` | `Hyperliquid` | `76.42%` | `23.58%` | `3.24` | 3,940.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.33%` | `49.67%` | `1.01` | 63,210.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `92.72%` | `7.28%` | `12.74` | 14,890.00 USD |
| `15M` | `HTX` | `34.66%` | `65.34%` | `0.53` | 38.84 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0.22%` | `99.78%` | `0.00` | 2,550.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `28.93%` | `71.07%` | `0.41` | 310.30 USD |
| `15M` | `Whale Positions` | `44.43%` | `55.57%` | `0.80` | 232,740.00 USD |
| `15M` | `Global Accounts` | `44.29%` | `55.71%` | `0.80` | 1,330,000.00 USD |
| `1H` | `XAUT` | `50.45%` | `49.55%` | `1.02` | 5,470,000.00 USD |
| `1H` | `Binance` | `58%` | `42%` | `1.38` | 1,950,000.00 USD |
| `1H` | `OKX` | `53.26%` | `46.74%` | `1.14` | 610,000.00 USD |
| `1H` | `Bybit` | `59.42%` | `40.58%` | `1.46` | 583,630.00 USD |
| `1H` | `KuCoin` | `48.81%` | `51.19%` | `0.95` | 252,590.00 USD |
| `1H` | `Gate` | `33.92%` | `66.08%` | `0.51` | 58,400.00 USD |
| `1H` | `Bitget` | `71.99%` | `28.01%` | `2.57` | 95,700.00 USD |
| `1H` | `BingX` | `10.53%` | `89.47%` | `0.12` | 560,580.00 USD |
| `1H` | `MEXC` | `33.76%` | `66.24%` | `0.51` | 172,780.00 USD |
| `1H` | `Bitunix` | `73.87%` | `26.13%` | `2.83` | 96,580.00 USD |
| `1H` | `Hyperliquid` | `89.04%` | `10.96%` | `8.12` | 60,210.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.09%` | `51.91%` | `0.93` | 976,910.00 USD |
| `1H` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.61 USD |
| `1H` | `WhiteBIT` | `68.51%` | `31.49%` | `2.18` | 41,050.00 USD |
| `1H` | `HTX` | `37.12%` | `62.88%` | `0.59` | 1,350.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.84%` | `6.16%` | `15.23` | 162.25 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `38.98%` | `61.02%` | `0.64` | 10,440.00 USD |
| `1H` | `Whale Positions` | `58%` | `42%` | `1.38` | 1,950,000.00 USD |
| `1H` | `Global Accounts` | `50.45%` | `49.55%` | `1.02` | 5,470,000.00 USD |
| `4H` | `XAUT` | `41.48%` | `58.52%` | `0.71` | 26,690,000.00 USD |
| `4H` | `Binance` | `51.56%` | `48.44%` | `1.06` | 8,150,000.00 USD |
| `4H` | `OKX` | `51.4%` | `48.6%` | `1.06` | 2,280,000.00 USD |
| `4H` | `Bybit` | `54.2%` | `45.8%` | `1.18` | 2,880,000.00 USD |
| `4H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 1,050,000.00 USD |
| `4H` | `Gate` | `48.23%` | `51.77%` | `0.93` | 347,750.00 USD |
| `4H` | `Bitget` | `51.13%` | `48.87%` | `1.05` | 392,650.00 USD |
| `4H` | `BingX` | `6.31%` | `93.69%` | `0.07` | 5,770,000.00 USD |
| `4H` | `MEXC` | `47.97%` | `52.03%` | `0.92` | 870,680.00 USD |
| `4H` | `Bitunix` | `50.57%` | `49.43%` | `1.02` | 302,380.00 USD |
| `4H` | `Hyperliquid` | `58.98%` | `41.02%` | `1.44` | 172,920.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.6%` | `51.4%` | `0.95` | 4,210,000.00 USD |
| `4H` | `Crypto.com` | `7.23%` | `92.77%` | `0.08` | 756.52 USD |
| `4H` | `WhiteBIT` | `74.02%` | `25.98%` | `2.85` | 161,210.00 USD |
| `4H` | `HTX` | `54.28%` | `45.72%` | `1.19` | 8,480.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `7.41%` | `92.59%` | `0.08` | 30,780.00 USD |
| `4H` | `Aster` | `72.53%` | `27.47%` | `2.64` | 503.62 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `67.59%` | `32.41%` | `2.09` | 50,640.00 USD |
| `4H` | `Whale Positions` | `51.56%` | `48.44%` | `1.06` | 8,150,000.00 USD |
| `4H` | `Global Accounts` | `41.48%` | `58.52%` | `0.71` | 26,690,000.00 USD |


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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26562.40` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26479.12` (Risk Distance: `83.29` pts)
  * +2.5R Take Profit: `26770.62`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26722.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26805.54` (Risk Distance: `83.29` pts)
  * +2.5R Take Profit: `26514.04`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.83 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26855.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
