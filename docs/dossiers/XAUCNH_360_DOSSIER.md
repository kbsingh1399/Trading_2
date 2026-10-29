# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUCNH
**Canonical Key**: `XAUCNH` | **Broker Instrument**: `XAUCNH.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 02:30:40 IST` (`2026-10-29 21:00:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `26764.70` | **Live Ask Quote**: `26768.05` | **Mid Price**: `26766.38`
- **Spread Points**: `335.00` | **Spread BPS**: `1.25 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `26766.38` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `66.92` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `26953.74` | Lower -3.00σ Band: `26579.01`
  * Upper +2.51σ Band: `26913.59` | Lower -2.51σ Band: `26619.16`
  * Upper +2.01σ Band: `26878.79` | Lower -2.01σ Band: `26653.96`
  * Upper +2.00σ Band: `26873.44` | Lower -2.00σ Band: `26659.31`
  * Upper +1.28σ Band: `26841.32` | Lower -1.28σ Band: `26691.43`
  * Upper +1.00σ Band: `26819.91` | Lower -1.00σ Band: `26712.84`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`26766.38` | EMA-20=`26766.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`26766.38` (Slope: `+0.0000`) | EMA-100=`26766.38`
  * Institutional Anchors: EMA-144=`26766.38` | EMA-200=`26766.38` (Slope: `+0.0000`) | EMA-233=`26766.38`
- **Range Boundaries**: 24H High=`27034.04` | 24H Low=`26498.71` | Weekly High=`27301.70` | Weekly Low=`26231.05`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `26846.67` (Distance: `+0.00%`)
  * Point of Control (POC) = `26766.38` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `26686.08` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`26873.44` | POC=`26766.38` | VAL=`26659.31`
  * Prior Day Extremes: PDH=`26926.97` | PDL=`26605.78` | PDC=`26766.38`
  * Monday Range Blueprint: High=`26900.21` | Mid=`26766.38` | Low=`26632.54`
  * Developing Weekly Value Area: Weekly VAH=`26980.51` | Weekly POC=`26766.38` | Weekly VAL=`26552.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`26819.91` | Low=`26712.84`
  * London Session (08:00-16:00 UTC): High=`26873.44` | Low=`26659.31`
  * New York Session (13:00-21:00 UTC): High=`26926.97` | Low=`26605.78`
  * Initial Balance (First Hour): IB High=`26846.67` | IB Low=`26686.08`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `26659.31` - `26873.44`
  * Optimal Trade Entry (OTE 0.705): `26819.91`
  * Structural Invalidation Anchor (0.786): `26980.51`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:26:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `53` | `0x4692...164f` | `SHORT` | 25,385,187.01 USD | `6,313.15` | `4133.51` | `4021.30` | `13663.36` | 710,314.23 USD | `+2.80%` | `5X Cross` |
| `54` | `0x5b5d...c060` | `SHORT` | 25,316,514.99 USD | `6,295.45` | `4191.43` | `4021.30` | `33232.02` | 1,070,470.40 USD | `+4.23%` | `4X Cross` |
| `67` | `0xb83d...6e36` | `SHORT` | 22,987,152.44 USD | `5,717.06` | `4234.49` | `4021.30` | `30986.77` | 1,221,722.79 USD | `+5.31%` | `5X Cross` |
| `95` | `0xec0b...b078` | `LONG` | 19,413,171.52 USD | `4,828.91` | `4157.43` | `4021.30` | `2245.20` | -662,710.80 USD | `-3.41%` | `25X Cross` |
| `141` | `0x645b...87b8` | `LONG` | 14,157,170.98 USD | `3,520.81` | `4129.50` | `4021.30` | `368.26` | -382,029.11 USD | `-2.70%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,141,812.10 USD | `3,268.21` | `4228.94` | `4021.30` | `4393.69` | 679,267.03 USD | `+5.17%` | `25X Cross` |
| `172` | `0xa742...e390` | `SHORT` | 11,658,870.40 USD | `2,900.00` | `4364.92` | `4021.30` | `4235.64` | 999,405.93 USD | `+8.57%` | `20X Cross` |
| `268` | `0x3678...b209` | `LONG` | 8,846,200.00 USD | `2,200.00` | `4176.09` | `4021.30` | `2582.59` | -341,219.30 USD | `-3.86%` | `25X Cross` |
| `269` | `0x41e5...0825` | `SHORT` | 8,844,220.00 USD | `2,200.00` | `4112.20` | `4021.30` | `4331.13` | 202,634.59 USD | `+2.29%` | `20X Cross` |
| `303` | `0xfc66...ca06` | `SHORT` | 7,965,696.65 USD | `1,981.17` | `4032.86` | `4021.30` | `24588.02` | 24,109.57 USD | `+0.30%` | `3X Cross` |
| `305` | `0xacb6...efbd` | `SHORT` | 7,944,144.37 USD | `1,975.37` | `4048.55` | `4021.30` | `6506.07` | 53,247.34 USD | `+0.67%` | `6X Cross` |
| `373` | `0xc26c...b8f4` | `LONG` | 6,351,722.23 USD | `1,579.95` | `4075.62` | `4021.30` | `0.000000` | -87,574.74 USD | `-1.38%` | `1X Cross` |
| `406` | `0x12d2...f97f` | `LONG` | 5,636,090.44 USD | `1,401.94` | `4278.91` | `4021.30` | `3074.39` | -362,700.13 USD | `-6.44%` | `20X Cross` |
| `553` | `0x63da...8add` | `LONG` | 4,021,000.00 USD | `1,000.00` | `4021.46` | `4021.30` | `3564.08` | -460.96 USD | `-0.01%` | `25X Cross` |
| `564` | `0x354b...6425` | `LONG` | 3,971,685.65 USD | `987.74` | `4031.85` | `4021.30` | `0.000000` | -10,721.68 USD | `-0.27%` | `10X Cross` |
| `577` | `0x9aa5...58af` | `LONG` | 3,907,555.47 USD | `971.64` | `4279.98` | `4021.30` | `0.000000` | -251,053.62 USD | `-6.42%` | `20X Cross` |
| `607` | `0xf3dc...1672` | `LONG` | 3,742,706.57 USD | `930.74` | `4024.62` | `4021.30` | `3337.56` | -3,186.00 USD | `-0.09%` | `20X Cross` |
| `669` | `0x4a20...3c26` | `LONG` | 3,366,932.97 USD | `837.40` | `4599.73` | `4021.30` | `0.000000` | -484,887.41 USD | `-14.40%` | `20X Cross` |
| `827` | `0x0fac...7a0a` | `LONG` | 2,760,493.48 USD | `686.49` | `4290.34` | `4021.30` | `1288.86` | -184,765.22 USD | `-6.69%` | `25X Cross` |
| `868` | `0xd8c5...99b0` | `SHORT` | 2,583,037.52 USD | `642.35` | `4175.35` | `4021.30` | `32816.79` | 99,023.65 USD | `+3.83%` | `4X Cross` |
| `897` | `0x625e...a354` | `SHORT` | 2,492,524.00 USD | `620.00` | `4122.81` | `4021.30` | `4342.23` | 63,623.03 USD | `+2.55%` | `20X Cross` |
| `923` | `0xeae3...e8ad` | `SHORT` | 2,412,720.00 USD | `600.00` | `4104.77` | `4021.30` | `4325.25` | 50,145.11 USD | `+2.08%` | `20X Cross` |
| `930` | `0xf285...fa82` | `LONG` | 2,404,505.34 USD | `598.11` | `4146.45` | `4021.30` | `3891.22` | -75,514.21 USD | `-3.14%` | `25X Cross` |
| `946` | `0x12f7...8750` | `LONG` | 2,354,799.19 USD | `585.61` | `4082.77` | `4021.30` | `2512.71` | -36,117.79 USD | `-1.53%` | `10X Cross` |
| `1102` | `0x413c...886c` | `LONG` | 2,010,700.00 USD | `500.00` | `4010.43` | `4021.30` | `0.000000` | 5,483.77 USD | `+0.27%` | `2X Cross` |
| `1111` | `0x61ce...a62b` | `SHORT` | 2,000,561.07 USD | `497.50` | `4071.66` | `4021.30` | `4712.53` | 25,107.72 USD | `+1.26%` | `20X Cross` |
| `1116` | `0x0593...40f9` | `LONG` | 1,995,226.95 USD | `496.18` | `4024.57` | `4021.30` | `3701.71` | -1,676.88 USD | `-0.08%` | `10X Isolated` |
| `1239` | `0xead5...69f2` | `LONG` | 1,824,302.03 USD | `453.78` | `4220.88` | `4021.30` | `3538.92` | -91,066.02 USD | `-4.99%` | `5X Isolated` |
| `1344` | `0x46fc...1195` | `LONG` | 1,646,553.26 USD | `409.49` | `4055.28` | `4021.30` | `2094.20` | -14,037.63 USD | `-0.85%` | `20X Cross` |
| `1382` | `0xee02...309d` | `SHORT` | 1,608,640.00 USD | `400.00` | `4438.84` | `4021.30` | `4226.86` | 166,898.60 USD | `+10.38%` | `25X Isolated` |
| `1383` | `0x6d15...d374` | `LONG` | 1,608,320.00 USD | `400.00` | `4068.25` | `4021.30` | `3841.79` | -18,980.00 USD | `-1.18%` | `25X Cross` |
| `1421` | `0x02a7...fe9f` | `SHORT` | 1,568,190.00 USD | `390.00` | `4055.02` | `4021.30` | `4306.68` | 13,269.25 USD | `+0.85%` | `25X Cross` |
| `1462` | `0x7e77...b8d2` | `SHORT` | 1,528,056.00 USD | `380.00` | `4131.92` | `4021.30` | `4293.49` | 42,073.64 USD | `+2.75%` | `20X Cross` |
| `1483` | `0x72c2...9b37` | `LONG` | 1,500,435.58 USD | `373.13` | `4000.98` | `4021.30` | `3778.02` | 7,542.07 USD | `+0.50%` | `13X Isolated` |
| `1519` | `0xaa44...b844` | `LONG` | 1,447,668.00 USD | `360.00` | `4043.10` | `4021.30` | `2803.24` | -7,849.63 USD | `-0.54%` | `4X Cross` |
| `1632` | `0xa41f...d50a` | `LONG` | 1,322,493.43 USD | `328.96` | `4468.89` | `4021.30` | `3833.16` | -147,604.42 USD | `-11.16%` | `15X Cross` |
| `1652` | `0x49e9...e1d0` | `SHORT` | 1,300,709.86 USD | `323.48` | `4025.23` | `4021.30` | `30978.66` | 1,368.46 USD | `+0.11%` | `4X Cross` |
| `1668` | `0xada6...6f88` | `LONG` | 1,283,871.04 USD | `319.28` | `4166.46` | `4021.30` | `1940.43` | -46,379.47 USD | `-3.61%` | `5X Cross` |
| `1672` | `0xbf5a...88ba` | `SHORT` | 1,277,036.23 USD | `317.65` | `4091.80` | `4021.30` | `10337.50` | 22,746.80 USD | `+1.78%` | `20X Cross` |
| `1708` | `0xff31...ff6c` | `SHORT` | 1,246,572.00 USD | `310.00` | `4372.43` | `4021.30` | `4789.15` | 108,883.38 USD | `+8.73%` | `10X Isolated` |
| `1872` | `0x50e2...d770` | `LONG` | 1,087,066.21 USD | `270.37` | `4243.58` | `4021.30` | `2562.07` | -60,260.26 USD | `-5.54%` | `20X Cross` |
| `1896` | `0x4c92...4f17` | `SHORT` | 1,072,483.13 USD | `266.72` | `4260.98` | `4021.30` | `6500.43` | 64,009.11 USD | `+5.97%` | `20X Cross` |
| `1951` | `0xd346...c4f3` | `LONG` | 1,026,053.85 USD | `255.17` | `4188.66` | `4021.30` | `3310.40` | -42,782.66 USD | `-4.17%` | `5X Isolated` |
| `1982` | `0x1581...463b` | `LONG` | 1,005,100.00 USD | `250.00` | `4003.77` | `4021.30` | `3504.62` | 4,156.41 USD | `+0.41%` | `15X Cross` |

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
| `1D` | `3609.80` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3609.80` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 6,940.00 USD | 0.00 USD | 27,360.00 USD |
| `1D` | `3614.00` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3614.00` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 3,810.00 USD | 0.00 USD | 23,870.00 USD |
| `1D` | `3618.20` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 7,370.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `3618.20` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 7,370.00 USD | 0.00 USD | 27,380.00 USD |
| `1D` | `3622.40` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `7D` | `3622.40` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 24,780.00 USD | 0.00 USD | 72,320.00 USD |
| `1D` | `3626.60` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `7D` | `3626.60` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 13,180.00 USD | 0.00 USD | 21,260.00 USD |
| `1D` | `3630.80` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `7D` | `3630.80` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 32,990.00 USD | 0.00 USD | 49,100.00 USD |
| `1D` | `3635.00` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `7D` | `3635.00` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 30,630.00 USD | 0.00 USD | 19,720.00 USD |
| `1D` | `3639.20` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3639.20` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 7,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3643.40` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `7D` | `3643.40` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 20,120.00 USD | 0.00 USD | 8,680.00 USD |
| `1D` | `3647.60` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 1,030.00 USD | 0.00 USD | 12,640.00 USD |
| `7D` | `3647.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 1,030.00 USD | 0.00 USD | 12,640.00 USD |
| `1D` | `3651.80` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `7D` | `3651.80` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 10,690.00 USD | 0.00 USD | 10,090.00 USD |
| `1D` | `3656.00` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 1,730.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `3656.00` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 1,730.00 USD | 0.00 USD | 5,900.00 USD |
| `1D` | `3849.20` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `3849.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 18,030.00 USD | 0.00 USD | 80,320.00 USD |
| `1D` | `3853.40` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `7D` | `3853.40` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,390.00 USD | 0.00 USD | 43,440.00 USD |
| `1D` | `3857.60` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 27,380.00 USD | 0.00 USD | 74,240.00 USD |
| `7D` | `3857.60` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 23,940.00 USD | 0.00 USD | 74,240.00 USD |
| `1D` | `3861.80` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 60,240.00 USD | 0.00 USD | 187,340.00 USD |
| `7D` | `3861.80` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 60,240.00 USD | 0.00 USD | 187,340.00 USD |
| `1D` | `3866.00` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 78,760.00 USD | 0.00 USD | 134,060.00 USD |
| `7D` | `3866.00` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 78,760.00 USD | 0.00 USD | 134,060.00 USD |
| `1D` | `3870.20` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `7D` | `3870.20` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 58,340.00 USD | 0.00 USD | 110,580.00 USD |
| `1D` | `3874.40` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `7D` | `3874.40` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 66,220.00 USD | 0.00 USD | 116,310.00 USD |
| `1D` | `3878.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `7D` | `3878.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 83,460.00 USD | 0.00 USD | 15,080.00 USD |
| `1D` | `3882.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `3882.80` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 33,890.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `3887.00` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `3887.00` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 29,130.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `3891.20` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,840.00 USD | 0.00 USD | 39,210.00 USD |
| `7D` | `3891.20` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,840.00 USD | 0.00 USD | 39,210.00 USD |
| `1D` | `3895.40` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `7D` | `3895.40` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 29,660.00 USD | 0.00 USD | 13,690.00 USD |
| `1D` | `3899.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,110.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `3899.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,110.00 USD | 0.00 USD | 16,340.00 USD |
| `1D` | `3929.00` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `7D` | `3929.00` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 36,050.00 USD | 0.00 USD | 160,630.00 USD |
| `1D` | `3933.20` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `7D` | `3933.20` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 30,770.00 USD | 0.00 USD | 86,890.00 USD |
| `1D` | `3937.40` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 54,760.00 USD | 0.00 USD | 140,290.00 USD |
| `7D` | `3937.40` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 47,890.00 USD | 0.00 USD | 140,290.00 USD |
| `1D` | `3941.60` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 95,210.00 USD | 0.00 USD | 291,500.00 USD |
| `7D` | `3941.60` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 95,210.00 USD | 0.00 USD | 291,500.00 USD |
| `1D` | `3945.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `7D` | `3945.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 176,490.00 USD | 0.00 USD | 337,150.00 USD |
| `1D` | `3950.00` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `7D` | `3950.00` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 87,540.00 USD | 0.00 USD | 121,900.00 USD |
| `1D` | `3954.20` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `7D` | `3954.20` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 150,980.00 USD | 0.00 USD | 308,010.00 USD |
| `1D` | `3958.40` | 664,290.00 USD | 0.00 USD | 664,290.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `7D` | `3958.40` | 664,290.00 USD | 0.00 USD | 664,290.00 USD | 155,060.00 USD | 0.00 USD | 74,540.00 USD |
| `1D` | `3962.60` | 434,690.00 USD | 0.00 USD | 434,690.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3962.60` | 434,690.00 USD | 0.00 USD | 434,690.00 USD | 47,460.00 USD | 0.00 USD | 8,860.00 USD |
| `1D` | `3966.80` | 378,370.00 USD | 0.00 USD | 378,370.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `7D` | `3966.80` | 378,370.00 USD | 0.00 USD | 378,370.00 USD | 93,710.00 USD | 0.00 USD | 43,420.00 USD |
| `1D` | `3971.00` | 241,240.00 USD | 0.00 USD | 241,240.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `7D` | `3971.00` | 241,240.00 USD | 0.00 USD | 241,240.00 USD | 18,800.00 USD | 0.00 USD | 47,600.00 USD |
| `1D` | `3975.20` | 174,850.00 USD | 0.00 USD | 174,850.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `7D` | `3975.20` | 174,850.00 USD | 0.00 USD | 174,850.00 USD | 46,630.00 USD | 0.00 USD | 66,060.00 USD |
| `1D` | `3979.40` | 62,150.00 USD | 0.00 USD | 62,150.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `3979.40` | 62,150.00 USD | 0.00 USD | 62,150.00 USD | 29,470.00 USD | 0.00 USD | 32,690.00 USD |
| `1D` | `4016.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4016.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `7D` | `4088.60` | 164,120.00 USD | 164,120.00 USD | 0.00 USD | 36,050.00 USD | 0.00 USD | 128,070.00 USD |
| `1D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `7D` | `4092.80` | 307,540.00 USD | 307,540.00 USD | 0.00 USD | 30,770.00 USD | 0.00 USD | 112,650.00 USD |
| `1D` | `4097.00` | 459,370.00 USD | 459,370.00 USD | 0.00 USD | 42,130.00 USD | 0.00 USD | 109,700.00 USD |
| `7D` | `4097.00` | 452,500.00 USD | 452,500.00 USD | 0.00 USD | 35,260.00 USD | 0.00 USD | 109,700.00 USD |
| `1D` | `4101.20` | 718,810.00 USD | 718,810.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 200,210.00 USD |
| `7D` | `4101.20` | 711,940.00 USD | 711,940.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 200,210.00 USD |
| `1D` | `4105.40` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 181,350.00 USD | 0.00 USD | 406,570.00 USD |
| `7D` | `4105.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 181,350.00 USD | 0.00 USD | 406,570.00 USD |
| `1D` | `4109.60` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `7D` | `4109.60` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 83,390.00 USD | 0.00 USD | 147,710.00 USD |
| `1D` | `4113.80` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `7D` | `4113.80` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 159,440.00 USD | 0.00 USD | 279,430.00 USD |
| `1D` | `4118.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `7D` | `4118.00` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165,680.00 USD | 0.00 USD | 120,080.00 USD |
| `1D` | `4122.20` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `7D` | `4122.20` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 76,260.00 USD | 0.00 USD | 18,320.00 USD |
| `1D` | `4126.40` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `7D` | `4126.40` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 66,080.00 USD | 0.00 USD | 19,170.00 USD |
| `1D` | `4130.60` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `7D` | `4130.60` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 41,290.00 USD | 0.00 USD | 52,120.00 USD |
| `1D` | `4134.80` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `7D` | `4134.80` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 27,100.00 USD | 0.00 USD | 65,440.00 USD |
| `1D` | `4139.00` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `7D` | `4139.00` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 41,900.00 USD | 0.00 USD | 27,390.00 USD |
| `1D` | `4143.20` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 12,230.00 USD | 0.00 USD | 32,690.00 USD |
| `7D` | `4143.20` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 12,230.00 USD | 0.00 USD | 32,690.00 USD |
| `1D` | `4168.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `4168.40` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 18,030.00 USD | 0.00 USD | 64,030.00 USD |
| `1D` | `4172.60` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `4172.60` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 12,370.00 USD | 0.00 USD | 53,820.00 USD |
| `1D` | `4176.80` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `7D` | `4176.80` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 18,690.00 USD | 0.00 USD | 57,350.00 USD |
| `1D` | `4181.00` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 23,000.00 USD | 0.00 USD | 81,660.00 USD |
| `7D` | `4181.00` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 19,570.00 USD | 0.00 USD | 81,660.00 USD |
| `1D` | `4185.20` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 203,210.00 USD |
| `7D` | `4185.20` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 84,040.00 USD | 0.00 USD | 203,210.00 USD |
| `1D` | `4189.40` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `7D` | `4189.40` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 55,760.00 USD | 0.00 USD | 87,970.00 USD |
| `1D` | `4193.60` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `7D` | `4193.60` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 66,890.00 USD | 0.00 USD | 107,010.00 USD |
| `1D` | `4197.80` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `7D` | `4197.80` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 62,110.00 USD | 0.00 USD | 94,520.00 USD |
| `1D` | `4202.00` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `7D` | `4202.00` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 66,930.00 USD | 0.00 USD | 11,790.00 USD |
| `1D` | `4206.20` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `7D` | `4206.20` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 26,330.00 USD | 0.00 USD | 3,510.00 USD |
| `1D` | `4210.40` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `7D` | `4210.40` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 35,920.00 USD | 0.00 USD | 25,640.00 USD |
| `1D` | `4214.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 19,870.00 USD |
| `7D` | `4214.60` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | 19,870.00 USD |
| `1D` | `4218.80` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `7D` | `4218.80` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 33,030.00 USD |
| `1D` | `4223.00` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `7D` | `4223.00` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 14,730.00 USD | 0.00 USD | 16,340.00 USD |
| `1D` | `4407.80` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `7D` | `4407.80` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 3,220.00 USD | 0.00 USD | 14,990.00 USD |
| `1D` | `4412.00` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `4412.00` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 3,720.00 USD | 0.00 USD | 16,420.00 USD |
| `1D` | `4416.20` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `7D` | `4416.20` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 3,810.00 USD | 0.00 USD | 9,950.00 USD |
| `1D` | `4420.40` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `7D` | `4420.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,060.00 USD | 0.00 USD | 21,890.00 USD |
| `1D` | `4424.60` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 53,200.00 USD |
| `7D` | `4424.60` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 13,060.00 USD | 0.00 USD | 53,200.00 USD |
| `1D` | `4428.80` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `7D` | `4428.80` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | 45,980.00 USD |
| `1D` | `4433.00` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `7D` | `4433.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 8,250.00 USD | 0.00 USD | 13,810.00 USD |
| `1D` | `4433.70` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4433.70` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,580.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `824.42M` | Total OI Tokens: `205,197.2 XAUT`
  * 1h OI Change: `-5.06%` | 4h OI Change: `-2.00%` | 24h OI Change: `+0.51%`
  * Exchange Breakdown: Binance=`61.68M` | Bybit=`143.42M` | OKX=`-` | Hyperliquid=`-`
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
| `15M` | `XAUT` | `18.40%` | `81.60%` | `0.23` | 13,850,000.00 USD |
| `15M` | `Binance` | `37.5%` | `62.5%` | `0.60` | 1,120,000.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `29.28%` | `70.72%` | `0.41` | 664,150.00 USD |
| `15M` | `KuCoin` | `4.92%` | `95.08%` | `0.05` | 110,210.00 USD |
| `15M` | `Gate` | `29.66%` | `70.34%` | `0.42` | 466,510.00 USD |
| `15M` | `Bitget` | `59.43%` | `40.57%` | `1.46` | 184,510.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `10.41%` | `89.59%` | `0.12` | 10,180,000.00 USD |
| `15M` | `Bitunix` | `32.5%` | `67.5%` | `0.48` | 346,380.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `72.12%` | `27.88%` | `2.59` | 693,460.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.97%` | `98.03%` | `0.02` | 65,130.00 USD |
| `15M` | `HTX` | `8.76%` | `91.24%` | `0.10` | 1,510.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `41.64%` | `58.36%` | `0.71` | 8,290.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `37.5%` | `62.5%` | `0.60` | 1,120,000.00 USD |
| `15M` | `Global Accounts` | `18.40%` | `81.60%` | `0.23` | 13,850,000.00 USD |
| `1H` | `XAUT` | `38.58%` | `61.42%` | `0.63` | 27,600,000.00 USD |
| `1H` | `Binance` | `49.98%` | `50.02%` | `1.00` | 2,580,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `50.43%` | `49.57%` | `1.02` | 2,380,000.00 USD |
| `1H` | `KuCoin` | `17.36%` | `82.64%` | `0.21` | 147,740.00 USD |
| `1H` | `Gate` | `51.18%` | `48.82%` | `1.05` | 1,350,000.00 USD |
| `1H` | `Bitget` | `61.4%` | `38.6%` | `1.59` | 771,790.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `31.03%` | `68.97%` | `0.45` | 16,410,000.00 USD |
| `1H` | `Bitunix` | `36.56%` | `63.44%` | `0.58` | 963,350.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.43%` | `43.57%` | `1.30` | 2,480,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `22.64%` | `77.36%` | `0.29` | 440,160.00 USD |
| `1H` | `HTX` | `30.27%` | `69.73%` | `0.43` | 3,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.62%` | `67.38%` | `0.48` | 60,290.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `49.98%` | `50.02%` | `1.00` | 2,580,000.00 USD |
| `1H` | `Global Accounts` | `38.58%` | `61.42%` | `0.63` | 27,600,000.00 USD |
| `4H` | `XAUT` | `46.09%` | `53.91%` | `0.85` | 48,730,000.00 USD |
| `4H` | `Binance` | `45.41%` | `54.59%` | `0.83` | 18,450,000.00 USD |
| `4H` | `OKX` | `44.84%` | `55.16%` | `0.81` | 6,270,000.00 USD |
| `4H` | `Bybit` | `44.02%` | `55.98%` | `0.79` | 7,700,000.00 USD |
| `4H` | `KuCoin` | `47.37%` | `52.63%` | `0.90` | 483,220.00 USD |
| `4H` | `Gate` | `45.86%` | `54.14%` | `0.85` | 441,900.00 USD |
| `4H` | `Bitget` | `49.61%` | `50.39%` | `0.98` | 3,260,000.00 USD |
| `4H` | `BingX` | `46.4%` | `53.6%` | `0.87` | 1,760,000.00 USD |
| `4H` | `MEXC` | `43.16%` | `56.84%` | `0.76` | 2,130,000.00 USD |
| `4H` | `Bitunix` | `45.65%` | `54.35%` | `0.84` | 572,270.00 USD |
| `4H` | `Hyperliquid` | `34.45%` | `65.55%` | `0.53` | 646,300.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.75%` | `52.25%` | `0.91` | 6,120,000.00 USD |
| `4H` | `Crypto.com` | `27.73%` | `72.27%` | `0.38` | 18,470.00 USD |
| `4H` | `WhiteBIT` | `88.16%` | `11.84%` | `7.45` | 669,580.00 USD |
| `4H` | `HTX` | `46.28%` | `53.72%` | `0.86` | 42,870.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.22%` | `47.78%` | `1.09` | 55,450.00 USD |
| `4H` | `Aster` | `30.78%` | `69.22%` | `0.44` | 51,470.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.09%` | `48.91%` | `1.04` | 70,080.00 USD |
| `4H` | `Whale Positions` | `45.41%` | `54.59%` | `0.83` | 18,450,000.00 USD |
| `4H` | `Global Accounts` | `46.09%` | `53.91%` | `0.85` | 48,730,000.00 USD |


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
| `5m` | 16,870.00 USD | -77,590.00 USD | **`DISTRIBUTION`** |
| `15m` | -398,230.00 USD | -643,050.00 USD | **`DISTRIBUTION`** |
| `30m` | -533,970.00 USD | -582,530.00 USD | **`DISTRIBUTION`** |
| `1h` | -391,420.00 USD | -15,090.00 USD | **`DISTRIBUTION`** |
| `2h` | 68,690.00 USD | 306,330.00 USD | **`ACCUMULATION`** |
| `4h` | -356,570.00 USD | 654,250.00 USD | **`ACCUMULATION`** |
| `6h` | -503,040.00 USD | 532,290.00 USD | **`ACCUMULATION`** |
| `8h` | -1,230,000.00 USD | 543,430.00 USD | **`DISTRIBUTION`** |
| `12h` | 379,330.00 USD | 659,960.00 USD | **`ACCUMULATION`** |
| `24h` | -1,080,000.00 USD | 214,870.00 USD | **`DISTRIBUTION`** |
| `1w` | -80,110,000.00 USD | -20,490,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -179,130,000.00 USD | -85,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.87K` | 15m=`-398.23K` | 1h=`-391.42K` | 24h=`-1.08M`
* Futures Capital Netflows: 5m=`-77.59K` | 15m=`-643.05K` | 1h=`-15.09K` | 24h=`+214.87K`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `26686.08` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `26600.75` (Risk Distance: `85.32` pts)
  * +2.5R Take Profit: `26899.39`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `26846.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `26932.00` (Risk Distance: `85.32` pts)
  * +2.5R Take Profit: `26633.36`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.85 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`26980.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
