# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 11:23:17 IST` (`2026-10-30 05:53:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `48` | `0x5b5d...c060` | `SHORT` | 25,987,202.24 USD | `6,489.82` | `4185.46` | `4003.60` | `29194.30` | 1,175,748.77 USD | `+4.52%` | `4X Cross` |
| `50` | `0x4692...164f` | `SHORT` | 25,297,888.43 USD | `6,317.68` | `4128.93` | `4003.60` | `13970.82` | 787,400.10 USD | `+3.11%` | `5X Cross` |
| `65` | `0xb83d...6e36` | `SHORT` | 23,506,599.14 USD | `5,869.90` | `4228.86` | `4003.60` | `26855.79` | 1,316,422.80 USD | `+5.60%` | `5X Cross` |
| `101` | `0xec0b...b078` | `LONG` | 19,335,909.01 USD | `4,828.91` | `4157.43` | `4003.60` | `2265.43` | -739,973.31 USD | `-3.83%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,220,455.41 USD | `3,551.74` | `4127.81` | `4003.60` | `605.92` | -440,481.59 USD | `-3.10%` | `3X Cross` |
| `159` | `0x7a6d...f79c` | `SHORT` | 13,085,272.01 USD | `3,268.21` | `4228.94` | `4003.60` | `4375.45` | 735,807.12 USD | `+5.62%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,612,470.40 USD | `2,900.00` | `4364.92` | `4003.60` | `4235.92` | 1,045,805.93 USD | `+9.01%` | `20X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,810,120.00 USD | `2,200.00` | `4112.20` | `4003.60` | `4331.40` | 236,734.59 USD | `+2.69%` | `20X Cross` |
| `262` | `0x3678...b209` | `LONG` | 8,808,360.00 USD | `2,200.00` | `4176.09` | `4003.60` | `2596.68` | -379,059.30 USD | `-4.30%` | `25X Cross` |
| `299` | `0xacb6...efbd` | `SHORT` | 7,910,563.10 USD | `1,975.37` | `4048.55` | `4003.60` | `6575.38` | 86,828.62 USD | `+1.10%` | `6X Cross` |
| `367` | `0xc26c...b8f4` | `LONG` | 6,325,811.02 USD | `1,579.95` | `4075.62` | `4003.60` | `0.000000` | -113,485.95 USD | `-1.79%` | `1X Cross` |
| `563` | `0x63da...8add` | `LONG` | 4,003,800.00 USD | `1,000.00` | `4021.46` | `4003.60` | `3564.37` | -17,660.96 USD | `-0.44%` | `25X Cross` |
| `569` | `0xf3dc...1672` | `LONG` | 3,940,626.17 USD | `984.27` | `4018.39` | `4003.60` | `2909.97` | -14,560.52 USD | `-0.37%` | `20X Cross` |
| `584` | `0x9aa5...58af` | `LONG` | 3,890,648.90 USD | `971.64` | `4279.98` | `4003.60` | `0.000000` | -267,960.19 USD | `-6.89%` | `20X Cross` |
| `591` | `0x354b...6425` | `LONG` | 3,839,352.47 USD | `958.81` | `4004.93` | `4003.60` | `0.000000` | -608.75 USD | `-0.02%` | `10X Cross` |
| `673` | `0x4a20...3c26` | `LONG` | 3,352,780.92 USD | `837.40` | `4599.73` | `4003.60` | `0.000000` | -499,039.46 USD | `-14.88%` | `20X Cross` |
| `828` | `0x0fac...7a0a` | `LONG` | 2,748,891.89 USD | `686.49` | `4290.34` | `4003.60` | `1143.91` | -196,366.82 USD | `-7.14%` | `25X Cross` |
| `903` | `0x625e...a354` | `SHORT` | 2,482,852.00 USD | `620.00` | `4122.81` | `4003.60` | `4342.50` | 73,295.03 USD | `+2.95%` | `20X Cross` |
| `909` | `0xd8c5...99b0` | `SHORT` | 2,475,769.35 USD | `618.35` | `4175.35` | `4003.60` | `34175.94` | 106,083.26 USD | `+4.28%` | `4X Cross` |
| `934` | `0xeae3...e8ad` | `SHORT` | 2,402,280.00 USD | `600.00` | `4104.77` | `4003.60` | `4325.52` | 60,585.11 USD | `+2.52%` | `20X Cross` |
| `937` | `0xf285...fa82` | `LONG` | 2,394,995.46 USD | `598.11` | `4146.45` | `4003.60` | `3891.51` | -85,024.10 USD | `-3.55%` | `25X Cross` |
| `951` | `0x12f7...8750` | `LONG` | 2,344,668.12 USD | `585.61` | `4082.77` | `4003.60` | `2582.53` | -46,248.86 USD | `-1.97%` | `10X Cross` |
| `1092` | `0x413c...886c` | `LONG` | 2,001,800.00 USD | `500.00` | `4010.43` | `4003.60` | `0.000000` | -3,416.23 USD | `-0.17%` | `2X Cross` |
| `1099` | `0x9c06...0560` | `LONG` | 1,995,812.39 USD | `498.42` | `4012.76` | `4003.60` | `0.000000` | -4,219.10 USD | `-0.21%` | `25X Cross` |
| `1104` | `0x61ce...a62b` | `SHORT` | 1,991,854.76 USD | `497.50` | `4071.66` | `4003.60` | `4715.52` | 33,814.03 USD | `+1.70%` | `20X Cross` |
| `1214` | `0xead5...69f2` | `LONG` | 1,817,223.01 USD | `453.78` | `4220.88` | `4003.60` | `3539.20` | -98,145.05 USD | `-5.40%` | `5X Isolated` |
| `1304` | `0x46fc...1195` | `LONG` | 1,661,275.55 USD | `414.87` | `4053.27` | `4003.60` | `2152.77` | -20,317.29 USD | `-1.22%` | `20X Cross` |
| `1347` | `0x6d15...d374` | `LONG` | 1,601,840.00 USD | `400.00` | `4068.25` | `4003.60` | `3842.07` | -25,460.00 USD | `-1.59%` | `25X Cross` |
| `1348` | `0xee02...309d` | `SHORT` | 1,601,720.00 USD | `400.00` | `4438.84` | `4003.60` | `4227.14` | 173,818.60 USD | `+10.85%` | `25X Isolated` |
| `1396` | `0x02a7...fe9f` | `SHORT` | 1,561,482.00 USD | `390.00` | `4055.02` | `4003.60` | `4306.96` | 19,977.25 USD | `+1.28%` | `25X Cross` |
| `1432` | `0x7e77...b8d2` | `SHORT` | 1,521,444.00 USD | `380.00` | `4131.92` | `4003.60` | `4293.77` | 48,685.64 USD | `+3.20%` | `20X Cross` |
| `1458` | `0x72c2...9b37` | `LONG` | 1,493,905.79 USD | `373.13` | `4000.98` | `4003.60` | `3778.31` | 1,012.27 USD | `+0.07%` | `13X Isolated` |
| `1507` | `0xaa44...b844` | `LONG` | 1,441,296.00 USD | `360.00` | `4043.10` | `4003.60` | `2819.86` | -14,221.63 USD | `-0.99%` | `4X Cross` |
| `1611` | `0xa41f...d50a` | `LONG` | 1,317,230.04 USD | `328.96` | `4468.89` | `4003.60` | `3802.43` | -152,867.81 USD | `-11.61%` | `15X Cross` |
| `1629` | `0x7fda...17d1` | `SHORT` | 1,299,852.61 USD | `324.62` | `4013.13` | `4003.60` | `30211.94` | 2,899.28 USD | `+0.22%` | `20X Cross` |
| `1661` | `0xbf5a...88ba` | `SHORT` | 1,271,985.52 USD | `317.65` | `4091.80` | `4003.60` | `10010.37` | 27,797.52 USD | `+2.19%` | `20X Cross` |
| `1698` | `0xff31...ff6c` | `SHORT` | 1,241,178.00 USD | `310.00` | `4372.43` | `4003.60` | `4789.43` | 114,277.38 USD | `+9.21%` | `10X Isolated` |
| `1721` | `0xada6...6f88` | `LONG` | 1,215,114.14 USD | `303.50` | `4166.46` | `4003.60` | `1790.47` | -49,398.72 USD | `-4.07%` | `5X Cross` |
| `1886` | `0x50e2...d770` | `LONG` | 1,082,497.00 USD | `270.37` | `4243.58` | `4003.60` | `2562.36` | -64,829.46 USD | `-5.99%` | `20X Cross` |
| `1902` | `0x4c92...4f17` | `SHORT` | 1,067,895.54 USD | `266.72` | `4260.98` | `4003.60` | `6510.11` | 68,596.70 USD | `+6.42%` | `20X Cross` |
| `1977` | `0xd346...c4f3` | `LONG` | 1,021,792.45 USD | `255.17` | `4188.66` | `4003.60` | `3310.69` | -47,044.06 USD | `-4.60%` | `5X Isolated` |

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
| `7D` | `3589.40` | 22,420,000.00 USD | 0.00 USD | 22,420,000.00 USD | 35,920.00 USD | 0.00 USD | 35,210.00 USD |
| `1D` | `3591.10` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `3593.70` | 22,350,000.00 USD | 0.00 USD | 22,350,000.00 USD | 90,500.00 USD | 0.00 USD | 155,760.00 USD |
| `1D` | `3595.30` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 24,410.00 USD | 0.00 USD | 19,250.00 USD |
| `7D` | `3598.00` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 98,280.00 USD | 0.00 USD | 321,490.00 USD |
| `1D` | `3599.50` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 1,490.00 USD | 0.00 USD | 34,940.00 USD |
| `7D` | `3602.30` | 21,680,000.00 USD | 0.00 USD | 21,680,000.00 USD | 108,630.00 USD | 0.00 USD | 107,230.00 USD |
| `1D` | `3603.70` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 11,380.00 USD | 0.00 USD | 33,720.00 USD |
| `7D` | `3606.60` | 21,470,000.00 USD | 0.00 USD | 21,470,000.00 USD | 25,640.00 USD | 0.00 USD | 110,830.00 USD |
| `1D` | `3607.90` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 18,250.00 USD | 0.00 USD | 64,400.00 USD |
| `7D` | `3610.90` | 21,330,000.00 USD | 0.00 USD | 21,330,000.00 USD | 52,340.00 USD | 0.00 USD | 52,820.00 USD |
| `1D` | `3612.10` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 17,620.00 USD | 0.00 USD | 26,900.00 USD |
| `7D` | `3615.20` | 21,230,000.00 USD | 0.00 USD | 21,230,000.00 USD | 24,770.00 USD | 0.00 USD | 49,210.00 USD |
| `1D` | `3616.30` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 10,800.00 USD | 0.00 USD | 30,830.00 USD |
| `7D` | `3619.50` | 21,150,000.00 USD | 0.00 USD | 21,150,000.00 USD | 27,850.00 USD | 0.00 USD | 86,040.00 USD |
| `1D` | `3620.50` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 21,740.00 USD | 0.00 USD | 66,750.00 USD |
| `7D` | `3623.80` | 21,040,000.00 USD | 0.00 USD | 21,040,000.00 USD | 35,700.00 USD | 0.00 USD | 131,440.00 USD |
| `1D` | `3624.70` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 22,580.00 USD | 0.00 USD | 37,460.00 USD |
| `7D` | `3628.10` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 47,240.00 USD | 0.00 USD | 35,770.00 USD |
| `1D` | `3628.90` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 4,190.00 USD | 0.00 USD | 21,120.00 USD |
| `7D` | `3632.40` | 20,790,000.00 USD | 0.00 USD | 20,790,000.00 USD | 46,540.00 USD | 0.00 USD | 92,000.00 USD |
| `1D` | `3633.10` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 2,840.00 USD |
| `7D` | `3636.70` | 20,650,000.00 USD | 0.00 USD | 20,650,000.00 USD | 59,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3641.00` | 20,590,000.00 USD | 0.00 USD | 20,590,000.00 USD | 60,700.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3645.30` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 12,340.00 USD | 0.00 USD | 15,470.00 USD |
| `7D` | `3649.60` | 20,490,000.00 USD | 0.00 USD | 20,490,000.00 USD | 7,110.00 USD | 0.00 USD | 11,910.00 USD |
| `7D` | `3653.90` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 5,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3658.20` | 20,470,000.00 USD | 0.00 USD | 20,470,000.00 USD | 13,450.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3821.60` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3825.90` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 50,700.00 USD | 0.00 USD | 12,110.00 USD |
| `7D` | `3830.20` | 20,370,000.00 USD | 0.00 USD | 20,370,000.00 USD | 126,670.00 USD | 0.00 USD | 333,830.00 USD |
| `1D` | `3830.50` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `3834.50` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 284,980.00 USD | 0.00 USD | 564,320.00 USD |
| `1D` | `3834.70` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 87,400.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `3838.80` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 311,710.00 USD | 0.00 USD | 789,870.00 USD |
| `1D` | `3838.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 22,350.00 USD | 0.00 USD | 119,800.00 USD |
| `1D` | `3843.10` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 28,460.00 USD | 0.00 USD | 97,130.00 USD |
| `7D` | `3843.10` | 17,960,000.00 USD | 0.00 USD | 17,960,000.00 USD | 301,350.00 USD | 0.00 USD | 359,480.00 USD |
| `1D` | `3847.30` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 66,000.00 USD | 0.00 USD | 195,170.00 USD |
| `7D` | `3847.40` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 115,590.00 USD | 0.00 USD | 366,480.00 USD |
| `1D` | `3851.50` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 73,320.00 USD | 0.00 USD | 129,680.00 USD |
| `7D` | `3851.70` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `3855.70` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 27,220.00 USD | 0.00 USD | 99,710.00 USD |
| `7D` | `3856.00` | 16,420,000.00 USD | 0.00 USD | 16,420,000.00 USD | 102,180.00 USD | 0.00 USD | 221,820.00 USD |
| `1D` | `3859.90` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 68,340.00 USD | 0.00 USD | 112,500.00 USD |
| `7D` | `3860.30` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 94,100.00 USD | 0.00 USD | 225,170.00 USD |
| `1D` | `3864.10` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 100,000.00 USD | 0.00 USD | 215,080.00 USD |
| `7D` | `3864.60` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 110,300.00 USD | 0.00 USD | 363,130.00 USD |
| `1D` | `3868.30` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 39,090.00 USD | 0.00 USD | 66,820.00 USD |
| `7D` | `3868.90` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 192,180.00 USD | 0.00 USD | 163,110.00 USD |
| `1D` | `3872.50` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 6,710.00 USD | 0.00 USD | 69,480.00 USD |
| `7D` | `3873.20` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 110,510.00 USD | 0.00 USD | 217,930.00 USD |
| `7D` | `3877.50` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 193,240.00 USD | 0.00 USD | 69,410.00 USD |
| `7D` | `3881.80` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 207,010.00 USD | 0.00 USD | 64,320.00 USD |
| `7D` | `3886.10` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 73,970.00 USD | 0.00 USD | 77,880.00 USD |
| `7D` | `3890.40` | 13,940,000.00 USD | 0.00 USD | 13,940,000.00 USD | 54,860.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `3894.70` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3899.00` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 77,640.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `3903.30` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `7D` | `3907.60` | 13,600,000.00 USD | 0.00 USD | 13,600,000.00 USD | 161,150.00 USD | 0.00 USD | 269,880.00 USD |
| `1D` | `3910.30` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `3911.90` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 413,650.00 USD | 0.00 USD | 689,910.00 USD |
| `1D` | `3914.50` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 174,800.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `3916.20` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 711,980.00 USD | 0.00 USD | 1,380,000.00 USD |
| `1D` | `3918.70` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 44,700.00 USD | 0.00 USD | 186,400.00 USD |
| `7D` | `3920.50` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 681,530.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `3922.90` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 56,910.00 USD | 0.00 USD | 247,470.00 USD |
| `7D` | `3924.80` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 288,510.00 USD | 0.00 USD | 470,810.00 USD |
| `1D` | `3927.10` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 114,120.00 USD | 0.00 USD | 380,740.00 USD |
| `7D` | `3929.10` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 184,740.00 USD | 0.00 USD | 836,390.00 USD |
| `1D` | `3931.30` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 162,220.00 USD | 0.00 USD | 249,590.00 USD |
| `7D` | `3933.40` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 422,690.00 USD | 0.00 USD | 330,810.00 USD |
| `1D` | `3935.50` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 22,890.00 USD | 0.00 USD | 208,370.00 USD |
| `7D` | `3937.70` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 142,730.00 USD | 0.00 USD | 514,090.00 USD |
| `1D` | `3939.70` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 149,180.00 USD | 0.00 USD | 198,540.00 USD |
| `7D` | `3942.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 180,040.00 USD | 0.00 USD | 532,380.00 USD |
| `1D` | `3943.90` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 180,760.00 USD | 0.00 USD | 412,900.00 USD |
| `7D` | `3946.30` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 245,000.00 USD | 0.00 USD | 536,720.00 USD |
| `1D` | `3948.10` | 458,930.00 USD | 0.00 USD | 458,930.00 USD | 114,830.00 USD | 0.00 USD | 184,750.00 USD |
| `7D` | `3950.60` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 333,580.00 USD | 0.00 USD | 326,980.00 USD |
| `1D` | `3952.30` | 159,350.00 USD | 0.00 USD | 159,350.00 USD | 17,330.00 USD | 0.00 USD | 142,010.00 USD |
| `7D` | `3954.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 301,500.00 USD | 0.00 USD | 484,700.00 USD |
| `7D` | `3959.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `7D` | `3963.50` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 299,960.00 USD | 0.00 USD | 181,590.00 USD |
| `7D` | `3967.80` | 852,100.00 USD | 0.00 USD | 852,100.00 USD | 145,360.00 USD | 0.00 USD | 102,810.00 USD |
| `7D` | `3972.10` | 603,940.00 USD | 0.00 USD | 603,940.00 USD | 138,010.00 USD | 0.00 USD | 152,640.00 USD |
| `7D` | `3976.40` | 313,290.00 USD | 0.00 USD | 313,290.00 USD | 39,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3980.70` | 273,680.00 USD | 0.00 USD | 273,680.00 USD | 111,850.00 USD | 0.00 USD | 115,850.00 USD |
| `7D` | `3985.00` | 45,980.00 USD | 0.00 USD | 45,980.00 USD | 11,550.00 USD | 0.00 USD | 34,430.00 USD |
| `7D` | `4002.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4002.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4066.70` | 170,220.00 USD | 170,220.00 USD | 0.00 USD | 31,730.00 USD | 0.00 USD | 138,490.00 USD |
| `1D` | `4069.90` | 59,730.00 USD | 59,730.00 USD | 0.00 USD | 30,930.00 USD | 0.00 USD | 28,790.00 USD |
| `7D` | `4071.00` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 344,960.00 USD | 0.00 USD | 821,300.00 USD |
| `1D` | `4074.10` | 310,720.00 USD | 310,720.00 USD | 0.00 USD | 166,380.00 USD | 0.00 USD | 84,610.00 USD |
| `7D` | `4075.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 594,700.00 USD | 0.00 USD | 1,110,000.00 USD |
| `1D` | `4078.30` | 541,240.00 USD | 541,240.00 USD | 0.00 USD | 53,120.00 USD | 0.00 USD | 177,410.00 USD |
| `7D` | `4079.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 657,780.00 USD | 0.00 USD | 1,450,000.00 USD |
| `1D` | `4082.50` | 827,630.00 USD | 827,630.00 USD | 0.00 USD | 56,910.00 USD | 0.00 USD | 229,470.00 USD |
| `7D` | `4083.90` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 409,290.00 USD | 0.00 USD | 674,150.00 USD |
| `1D` | `4086.70` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 99,170.00 USD | 0.00 USD | 328,940.00 USD |
| `7D` | `4088.20` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 238,100.00 USD | 0.00 USD | 821,070.00 USD |
| `1D` | `4090.90` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 158,790.00 USD | 0.00 USD | 259,780.00 USD |
| `7D` | `4092.50` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 328,600.00 USD | 0.00 USD | 269,750.00 USD |
| `1D` | `4095.10` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 33,980.00 USD | 0.00 USD | 176,600.00 USD |
| `7D` | `4096.80` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 204,360.00 USD | 0.00 USD | 443,640.00 USD |
| `1D` | `4099.30` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 113,960.00 USD | 0.00 USD | 197,190.00 USD |
| `7D` | `4101.10` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 158,830.00 USD | 0.00 USD | 371,980.00 USD |
| `1D` | `4103.50` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 172,480.00 USD | 0.00 USD | 409,020.00 USD |
| `7D` | `4105.40` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 233,550.00 USD | 0.00 USD | 804,610.00 USD |
| `1D` | `4107.70` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 138,120.00 USD | 0.00 USD | 224,240.00 USD |
| `7D` | `4109.70` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 260,650.00 USD | 0.00 USD | 222,470.00 USD |
| `1D` | `4111.90` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 40,060.00 USD | 0.00 USD | 113,470.00 USD |
| `7D` | `4114.00` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 208,370.00 USD | 0.00 USD | 339,000.00 USD |
| `1D` | `4116.10` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 94,650.00 USD |
| `7D` | `4118.30` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 459,050.00 USD | 0.00 USD | 339,430.00 USD |
| `7D` | `4122.60` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 424,980.00 USD | 0.00 USD | 37,080.00 USD |
| `7D` | `4126.90` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 217,200.00 USD | 0.00 USD | 232,760.00 USD |
| `7D` | `4131.20` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 74,180.00 USD | 0.00 USD | 107,640.00 USD |
| `7D` | `4135.50` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 76,300.00 USD | 0.00 USD | 59,560.00 USD |
| `7D` | `4139.80` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 63,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4144.10` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 122,010.00 USD | 0.00 USD | 162,400.00 USD |
| `7D` | `4148.40` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 112,610.00 USD | 0.00 USD | 159,260.00 USD |
| `1D` | `4149.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 15,470.00 USD | 0.00 USD | 14,400.00 USD |
| `7D` | `4152.70` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 274,610.00 USD | 0.00 USD | 474,970.00 USD |
| `1D` | `4153.90` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 83,190.00 USD | 0.00 USD | 42,310.00 USD |
| `7D` | `4157.00` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 318,580.00 USD | 0.00 USD | 792,530.00 USD |
| `1D` | `4158.10` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 26,560.00 USD | 0.00 USD | 88,700.00 USD |
| `7D` | `4161.30` | 16,480,000.00 USD | 16,480,000.00 USD | 0.00 USD | 325,310.00 USD | 0.00 USD | 513,530.00 USD |
| `1D` | `4162.30` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 28,460.00 USD | 0.00 USD | 93,520.00 USD |
| `7D` | `4165.60` | 16,930,000.00 USD | 16,930,000.00 USD | 0.00 USD | 123,720.00 USD | 0.00 USD | 320,540.00 USD |
| `1D` | `4166.50` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 35,670.00 USD | 0.00 USD | 133,830.00 USD |
| `7D` | `4169.90` | 17,230,000.00 USD | 17,230,000.00 USD | 0.00 USD | 55,890.00 USD | 0.00 USD | 251,660.00 USD |
| `1D` | `4170.70` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 83,520.00 USD | 0.00 USD | 164,850.00 USD |
| `7D` | `4174.20` | 17,610,000.00 USD | 17,610,000.00 USD | 0.00 USD | 211,340.00 USD | 0.00 USD | 165,400.00 USD |
| `1D` | `4174.90` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 26,780.00 USD | 0.00 USD | 95,550.00 USD |
| `7D` | `4178.50` | 17,850,000.00 USD | 17,850,000.00 USD | 0.00 USD | 46,950.00 USD | 0.00 USD | 194,990.00 USD |
| `1D` | `4179.10` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | 104,490.00 USD |
| `7D` | `4182.80` | 18,190,000.00 USD | 18,190,000.00 USD | 0.00 USD | 90,220.00 USD | 0.00 USD | 250,080.00 USD |
| `1D` | `4183.30` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 85,580.00 USD | 0.00 USD | 162,760.00 USD |
| `7D` | `4187.10` | 18,640,000.00 USD | 18,640,000.00 USD | 0.00 USD | 110,000.00 USD | 0.00 USD | 336,970.00 USD |
| `1D` | `4187.50` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 85,680.00 USD | 0.00 USD | 146,440.00 USD |
| `7D` | `4191.40` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 186,760.00 USD | 0.00 USD | 155,040.00 USD |
| `1D` | `4191.70` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 20,030.00 USD | 0.00 USD | 51,510.00 USD |
| `7D` | `4195.70` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 94,060.00 USD | 0.00 USD | 164,530.00 USD |
| `1D` | `4195.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | 63,720.00 USD |
| `7D` | `4200.00` | 19,540,000.00 USD | 19,540,000.00 USD | 0.00 USD | 192,150.00 USD | 0.00 USD | 109,630.00 USD |
| `7D` | `4204.30` | 19,760,000.00 USD | 19,760,000.00 USD | 0.00 USD | 196,490.00 USD | 0.00 USD | 26,130.00 USD |
| `7D` | `4208.60` | 19,970,000.00 USD | 19,970,000.00 USD | 0.00 USD | 102,040.00 USD | 0.00 USD | 108,790.00 USD |
| `7D` | `4212.90` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4217.20` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `7D` | `4221.50` | 20,170,000.00 USD | 20,170,000.00 USD | 0.00 USD | 34,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4225.80` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 41,360.00 USD | 0.00 USD | 75,140.00 USD |
| `7D` | `4230.10` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 5,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4376.30` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4384.90` | 20,330,000.00 USD | 20,330,000.00 USD | 0.00 USD | 24,110.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `4389.10` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 6,190.00 USD | 0.00 USD | 3,450.00 USD |
| `7D` | `4389.20` | 20,480,000.00 USD | 20,480,000.00 USD | 0.00 USD | 37,410.00 USD | 0.00 USD | 117,500.00 USD |
| `1D` | `4393.30` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 9,110.00 USD |
| `7D` | `4393.50` | 20,690,000.00 USD | 20,690,000.00 USD | 0.00 USD | 79,830.00 USD | 0.00 USD | 125,350.00 USD |
| `1D` | `4397.50` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 7,610.00 USD | 0.00 USD | 32,650.00 USD |
| `7D` | `4397.80` | 21,050,000.00 USD | 21,050,000.00 USD | 0.00 USD | 83,340.00 USD | 0.00 USD | 273,660.00 USD |
| `1D` | `4401.70` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 11,380.00 USD | 0.00 USD | 30,450.00 USD |
| `7D` | `4402.10` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 108,630.00 USD | 0.00 USD | 88,420.00 USD |
| `1D` | `4405.90` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4406.40` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 23,790.00 USD | 0.00 USD | 109,460.00 USD |
| `1D` | `4410.10` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 13,560.00 USD | 0.00 USD | 58,710.00 USD |
| `7D` | `4410.70` | 21,420,000.00 USD | 21,420,000.00 USD | 0.00 USD | 13,760.00 USD | 0.00 USD | 31,580.00 USD |
| `1D` | `4413.90` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 17,620.00 USD | 0.00 USD | 21,390.00 USD |
| `7D` | `4415.00` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 54,030.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4419.30` | 21,570,000.00 USD | 21,570,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | 49,210.00 USD |
| `7D` | `4423.60` | 21,660,000.00 USD | 21,660,000.00 USD | 0.00 USD | 24,010.00 USD | 0.00 USD | 70,600.00 USD |
| `7D` | `4427.90` | 21,830,000.00 USD | 21,830,000.00 USD | 0.00 USD | 28,470.00 USD | 0.00 USD | 138,380.00 USD |
| `7D` | `4432.20` | 21,900,000.00 USD | 21,900,000.00 USD | 0.00 USD | 35,220.00 USD | 0.00 USD | 33,300.00 USD |
| `7D` | `4435.80` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 19,260.00 USD | 0.00 USD | 37,190.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `793.50M` | Total OI Tokens: `198,160.0 XAUT`
  * 1h OI Change: `-1.34%` | 4h OI Change: `-1.27%` | 24h OI Change: `-6.45%`
  * Exchange Breakdown: Binance=`61.19M` | Bybit=`144.92M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `52.64%` | `47.36%` | `1.11` | 1,070,000.00 USD |
| `15M` | `Binance` | `51.51%` | `48.49%` | `1.06` | 394,330.00 USD |
| `15M` | `OKX` | `57.02%` | `42.98%` | `1.33` | 141,410.00 USD |
| `15M` | `Bybit` | `53.96%` | `46.04%` | `1.17` | 165,290.00 USD |
| `15M` | `KuCoin` | `46.25%` | `53.75%` | `0.86` | 62,640.00 USD |
| `15M` | `Gate` | `61.77%` | `38.23%` | `1.62` | 9,940.00 USD |
| `15M` | `Bitget` | `80.16%` | `19.84%` | `4.04` | 22,270.00 USD |
| `15M` | `BingX` | `43.65%` | `56.35%` | `0.77` | 24,100.00 USD |
| `15M` | `MEXC` | `56.35%` | `43.65%` | `1.29` | 32,480.00 USD |
| `15M` | `Bitunix` | `54.75%` | `45.25%` | `1.21` | 10,910.00 USD |
| `15M` | `Hyperliquid` | `72.56%` | `27.44%` | `2.64` | 6,550.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.88%` | `51.12%` | `0.96` | 192,210.00 USD |
| `15M` | `Crypto.com` | `18.69%` | `81.31%` | `0.23` | 2.14 USD |
| `15M` | `WhiteBIT` | `50.9%` | `49.1%` | `1.04` | 5,990.00 USD |
| `15M` | `HTX` | `47.66%` | `52.34%` | `0.91` | 1.30 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 10.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.94%` | `55.06%` | `0.82` | 2,050.00 USD |
| `15M` | `Whale Positions` | `51.51%` | `48.49%` | `1.06` | 394,330.00 USD |
| `15M` | `Global Accounts` | `52.64%` | `47.36%` | `1.11` | 1,070,000.00 USD |
| `1H` | `XAUT` | `54.29%` | `45.71%` | `1.19` | 5,160,000.00 USD |
| `1H` | `Binance` | `55.25%` | `44.75%` | `1.23` | 2,010,000.00 USD |
| `1H` | `OKX` | `54.02%` | `45.98%` | `1.17` | 617,820.00 USD |
| `1H` | `Bybit` | `59.7%` | `40.3%` | `1.48` | 642,700.00 USD |
| `1H` | `KuCoin` | `49.48%` | `50.52%` | `0.98` | 265,210.00 USD |
| `1H` | `Gate` | `34.26%` | `65.74%` | `0.52` | 53,620.00 USD |
| `1H` | `Bitget` | `71.46%` | `28.54%` | `2.50` | 102,630.00 USD |
| `1H` | `BingX` | `45.89%` | `54.11%` | `0.85` | 118,860.00 USD |
| `1H` | `MEXC` | `38.33%` | `61.67%` | `0.62` | 153,170.00 USD |
| `1H` | `Bitunix` | `73.71%` | `26.29%` | `2.80` | 99,280.00 USD |
| `1H` | `Hyperliquid` | `88.9%` | `11.1%` | `8.01` | 61,130.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.87%` | `51.13%` | `0.96` | 994,030.00 USD |
| `1H` | `Crypto.com` | `17.99%` | `82.01%` | `0.22` | 4.50 USD |
| `1H` | `WhiteBIT` | `61.42%` | `38.58%` | `1.59` | 39,700.00 USD |
| `1H` | `HTX` | `30.93%` | `69.07%` | `0.45` | 1,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.84%` | `6.16%` | `15.23` | 162.25 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.98%` | `56.02%` | `0.79` | 10,140.00 USD |
| `1H` | `Whale Positions` | `55.25%` | `44.75%` | `1.23` | 2,010,000.00 USD |
| `1H` | `Global Accounts` | `54.29%` | `45.71%` | `1.19` | 5,160,000.00 USD |
| `4H` | `XAUT` | `48.39%` | `51.61%` | `0.94` | 51,370,000.00 USD |
| `4H` | `Binance` | `50.38%` | `49.62%` | `1.02` | 21,020,000.00 USD |
| `4H` | `OKX` | `47.7%` | `52.3%` | `0.91` | 9,650,000.00 USD |
| `4H` | `Bybit` | `49.95%` | `50.05%` | `1.00` | 4,830,000.00 USD |
| `4H` | `KuCoin` | `48.36%` | `51.64%` | `0.94` | 376,800.00 USD |
| `4H` | `Gate` | `52.43%` | `47.57%` | `1.10` | 1,380,000.00 USD |
| `4H` | `Bitget` | `47.26%` | `52.74%` | `0.90` | 3,500,000.00 USD |
| `4H` | `BingX` | `28.18%` | `71.82%` | `0.39` | 2,270,000.00 USD |
| `4H` | `MEXC` | `39.4%` | `60.6%` | `0.65` | 2,950,000.00 USD |
| `4H` | `Bitunix` | `46.83%` | `53.17%` | `0.88` | 1,200,000.00 USD |
| `4H` | `Hyperliquid` | `54.8%` | `45.2%` | `1.21` | 1,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.9%` | `50.1%` | `1.00` | 1,630,000.00 USD |
| `4H` | `Crypto.com` | `45.34%` | `54.66%` | `0.83` | 20,980.00 USD |
| `4H` | `WhiteBIT` | `73.9%` | `26.1%` | `2.83` | 537,700.00 USD |
| `4H` | `HTX` | `28.78%` | `71.22%` | `0.40` | 23,730.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `88.73%` | `11.27%` | `7.87` | 24,170.00 USD |
| `4H` | `Aster` | `76.52%` | `23.48%` | `3.26` | 17,760.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `58.99%` | `41.01%` | `1.44` | 66,300.00 USD |
| `4H` | `Whale Positions` | `50.38%` | `49.62%` | `1.02` | 21,020,000.00 USD |
| `4H` | `Global Accounts` | `48.39%` | `51.61%` | `0.94` | 51,370,000.00 USD |


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
| `5m` | -15,910.00 USD | -38,760.00 USD | **`DISTRIBUTION`** |
| `15m` | -44,440.00 USD | -55,010.00 USD | **`DISTRIBUTION`** |
| `30m` | -79,430.00 USD | -60.19 USD | **`DISTRIBUTION`** |
| `1h` | -7,710.00 USD | -155,040.00 USD | **`DISTRIBUTION`** |
| `2h` | -242,720.00 USD | -732,960.00 USD | **`DISTRIBUTION`** |
| `4h` | -778,290.00 USD | -881,300.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,410,000.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,130,000.00 USD | -3,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,140,000.00 USD | -1,700,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -386,750.00 USD | -2,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -72,680,000.00 USD | -19,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -180,090,000.00 USD | -85,220,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-15.91K` | 15m=`-44.44K` | 1h=`-7.71K` | 24h=`-386.75K`
* Futures Capital Netflows: 5m=`-38.76K` | 15m=`-55.01K` | 1h=`-155.04K` | 24h=`-2.31M`
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
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
