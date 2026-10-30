# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 07:39:18 IST` (`2026-10-30 02:09:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.43` | **Live Ask Quote**: `10.52` | **Mid Price**: `10.48`
- **Spread Points**: `87.00` | **Spread BPS**: `83.04 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `10.43` | VWAP Z-Score: `-1.58` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1493` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `33.61` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.62` | Lower -3.00σ Band: `9.82`
  * Upper +2.51σ Band: `12.39` | Lower -2.51σ Band: `10.04`
  * Upper +2.01σ Band: `12.16` | Lower -2.01σ Band: `10.28`
  * Upper +2.00σ Band: `12.15` | Lower -2.00σ Band: `10.28`
  * Upper +1.28σ Band: `11.81` | Lower -1.28σ Band: `10.62`
  * Upper +1.00σ Band: `11.68` | Lower -1.00σ Band: `10.75`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.51` | EMA-20=`10.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.07` (Slope: `+0.0000`) | EMA-100=`11.28`
  * Institutional Anchors: EMA-144=`11.34` | EMA-200=`11.37` (Slope: `-0.9634`) | EMA-233=`11.39`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.83` (Distance: `-3.23%`)
  * Point of Control (POC) = `10.48` (Distance: `-0.03%`)
  * Value Area Low (VAL) = `10.22` (Distance: `+2.55%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.68` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`10.52` | Low=`10.44`
  * New York Session (13:00-21:00 UTC): High=`10.54` | Low=`10.41`
  * Initial Balance (First Hour): IB High=`10.51` | IB Low=`10.45`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.44` - `10.52`
  * Optimal Trade Entry (OTE 0.705): `10.50`
  * Structural Invalidation Anchor (0.786): `10.56`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.54` | `10.54` | `10.47` | `10.52` | `74,849` | 785,894.60 USD | 54,137.75 USD | `+6.89%` | -15,055,653.22 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `10.52` | `10.52` | `10.47` | `10.50` | `73,804` | 774,162.04 USD | -94,035.84 USD | `-12.15%` | -15,149,689.06 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `10.50` | `10.52` | `10.48` | `10.49` | `49,456` | 519,588.32 USD | -29,127.51 USD | `-5.61%` | -15,178,816.57 USD | `-0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.62` | `10.62` | `10.50` | `10.51` | `317,672` | 3,349,266.76 USD | -121,897.81 USD | `-3.64%` | -15,288,934.75 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `10.51` | `10.62` | `10.41` | `10.53` | `563,128` | 5,937,236.51 USD | 179,143.78 USD | `+3.02%` | -15,109,790.96 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `10.54` | `10.54` | `10.47` | `10.49` | `198,109` | 2,079,644.96 USD | -69,025.61 USD | `-3.32%` | -15,178,816.57 USD | `+0.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `10.75` | `10.75` | `10.53` | `10.61` | `3,504,678` | 37,271,092.72 USD | 322,431.20 USD | `+0.87%` | -14,690,218.67 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `10.61` | `10.65` | `10.25` | `10.50` | `3,619,167` | 37,791,802.16 USD | -189,145.75 USD | `-0.50%` | -14,879,364.43 USD | `+0.24` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `10.50` | `10.64` | `10.41` | `10.49` | `1,664,191` | 17,537,270.76 USD | -301,083.08 USD | `-1.72%` | -15,180,447.51 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.65` | `10.25` | `10.49` | `5,283,171` | 55,327,109.78 USD | -491,140.34 USD | `-0.89%` | -14,376,664.92 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | 329,195.75 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,661,099.58 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.65` | `10.25` | `10.49` | `5,283,171` | 55,327,109.78 USD | -491,140.34 USD | `-0.89%` | -14,376,664.92 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`10.48`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `424` | `0xecb6...2b00` | `SHORT` | 5,007,889.93 USD | `476,488,100.00` | `10.66` | `10.53` | `71.09` | 70,831.07 USD | `+1.41%` | `10X Cross` |
| `516` | `0x73ce...8ce9` | `LONG` | 4,198,921.77 USD | `400,011,600.00` | `12.05` | `10.53` | `7.82` | -620,831.94 USD | `-14.79%` | `5X Cross` |
| `871` | `0xb83d...6e36` | `SHORT` | 2,543,556.63 USD | `242,013,000.00` | `12.93` | `10.53` | `596.75` | 586,337.56 USD | `+23.05%` | `3X Cross` |
| `922` | `0x458d...ab3b` | `LONG` | 2,387,416.92 USD | `227,156,700.00` | `13.13` | `10.53` | `9.34` | -594,813.48 USD | `-24.91%` | `3X Isolated` |
| `994` | `0xdd53...2b13` | `SHORT` | 2,170,881.30 USD | `206,475,300.00` | `11.92` | `10.53` | `324.61` | 290,341.62 USD | `+13.37%` | `3X Cross` |
| `1014` | `0x3dc9...54b0` | `SHORT` | 2,102,182.00 USD | `200,000,000.00` | `7.56` | `10.53` | `103.03` | -591,023.58 USD | `-28.11%` | `10X Cross` |
| `1038` | `0x45d2...4029` | `SHORT` | 2,050,990.50 USD | `195,500,000.00` | `11.54` | `10.53` | `238.77` | 205,492.93 USD | `+10.02%` | `10X Cross` |
| `1216` | `0x6540...f7b7` | `LONG` | 1,782,320.66 USD | `169,935,800.00` | `12.40` | `10.53` | `6.69` | -325,439.34 USD | `-18.26%` | `5X Isolated` |
| `1285` | `0xeadc...9d55` | `LONG` | 1,657,338.72 USD | `157,691,600.00` | `9.43` | `10.53` | `0.000000` | 170,683.81 USD | `+10.30%` | `10X Cross` |
| `1528` | `0x5b5d...c060` | `SHORT` | 1,384,960.50 USD | `131,775,500.00` | `13.61` | `10.53` | `1311.17` | 408,297.46 USD | `+29.48%` | `3X Cross` |
| `1687` | `0xf6f3...47f8` | `SHORT` | 1,209,828.74 USD | `115,024,600.00` | `11.42` | `10.53` | `20.25` | 103,501.44 USD | `+8.56%` | `5X Cross` |
| `1729` | `0x9df2...c665` | `SHORT` | 1,168,118.19 USD | `111,143,500.00` | `11.48` | `10.53` | `300.33` | 107,921.14 USD | `+9.24%` | `10X Cross` |
| `1856` | `0xfe7e...11b4` | `LONG` | 1,061,080.72 USD | `101,142,000.00` | `14.47` | `10.53` | `5.32` | -402,032.43 USD | `-37.89%` | `5X Isolated` |
| `1886` | `0x8af7...fa05` | `SHORT` | 1,036,041.26 USD | `98,661,200.00` | `14.08` | `10.53` | `204.58` | 353,141.28 USD | `+34.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.87` | 16,523.65 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 16.52K USD at 11.8730 USD [API] | `2026-10-28 20:12:42` |
| `ANNOUNCEMENT` | `INFO` | `11.87` | 5,117.26 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.12K USD at 11.8730 USD [API] | `2026-10-28 20:12:41` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 7,505.19 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,466.45 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |
| `ANNOUNCEMENT` | `INFO` | `11.98` | 92.24 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.09K USD at 11.9790 USD [API] | `2026-10-28 20:01:53` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 7,028.87 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.03K USD at 11.7520 USD [API] | `2026-10-28 20:24:25` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 5,465.39 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.7510 USD [API] | `2026-10-28 20:24:25` |
| `ANNOUNCEMENT` | `INFO` | `11.76` | 9,227.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 9.23K USD at 11.7580 USD [API] | `2026-10-28 20:34:32` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,466.99 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8410 USD [API] | `2026-10-28 22:04:16` |
| `ANNOUNCEMENT` | `INFO` | `11.80` | 5,566.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.57K USD at 11.8030 USD [API] | `2026-10-28 22:22:09` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 5,465.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8230 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 10,243.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 10.24K USD at 11.8220 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.82` | 5,407.38 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.41K USD at 11.8220 USD [API] | `2026-10-28 22:53:25` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 7,904.59 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.90K USD at 11.8120 USD [API] | `2026-10-28 23:00:04` |
| `ANNOUNCEMENT` | `INFO` | `11.78` | 7,973.56 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.97K USD at 11.7830 USD [API] | `2026-10-28 23:01:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.09%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`11.11` (Vol: 502,000.00 USD, Dist: `+4.59%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.15` | 681.12 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 1,020.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 670.08 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 31,280.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,850.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 1,470.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 549.99 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 10,740.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 592.95 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 433.45 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 39,500.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 8,760.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 6,930.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 6,080.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 802.78 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 50,520.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 233,370.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 2,070.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 3,620.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 5,050.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 3,680.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 6,180.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 546,470.00 USD | 11,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 112,260.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 37,860.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 276.57 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 15,030.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 790.76 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 65,620.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 11,250.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,180.00 USD | 10,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 23,840.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 48,200.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 25,640.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 10,350.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 6,850.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 33,730.00 USD | 10,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 17,220.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 30,910.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 11,970.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 7,600.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 30,190.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 20,740.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,270,000.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 252.45 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 16,460.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 2,790.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 64,420.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 100,290.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 38,160.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 32,470.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 16,130.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 189,230.00 USD | 9,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 16,350.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 25,730.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 308,920.00 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 31,360.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 450,470.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 66,460.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,750,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 36,020.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,160,000.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.45` | 4,750,000.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 52,380.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.47` | 4,730,000.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.53` | 4,730,000.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.55` | 4,720,000.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 17,750.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.57` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 1,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.57` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.59` | 4,700,000.00 USD | 4,700,000.00 USD | 40,390.00 USD | 6,150.00 USD | 34,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 6,330,000.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.61` | 4,620,000.00 USD | 4,620,000.00 USD | 1,090.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.63` | 4,610,000.00 USD | 4,610,000.00 USD | 671.70 USD | 0.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 6,320,000.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.65` | 4,600,000.00 USD | 4,600,000.00 USD | 972.50 USD | 0.00 USD | 105.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 6,300,000.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 14,450.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.67` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.67` | 6,290,000.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.69` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 10,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 6,290,000.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.71` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.73` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.75` | 4,520,000.00 USD | 4,520,000.00 USD | 40,030.00 USD | 0.00 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 6,220,000.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 73,310.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.77` | 4,460,000.00 USD | 4,460,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.77` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.79` | 4,320,000.00 USD | 4,320,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 6,110,000.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.81` | 4,310,000.00 USD | 4,310,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 6,060,000.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 4,210,000.00 USD | 4,210,000.00 USD | 37,110.00 USD | 0.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 5,960,000.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.85` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 5,910,000.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 207,090.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 4,160,000.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 4,140,000.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 4,110,000.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 4,090,000.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 505,330.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 4,060,000.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 4,030,000.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 4,030,000.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 4,030,000.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 665,050.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 4,020,000.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 4,010,000.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 4,000,000.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 12,110.00 USD | 566,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.17` | 3,990,000.00 USD | 3,990,000.00 USD | 3,600.00 USD | 17,840.00 USD | 424.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 5,640,000.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 3,970,000.00 USD | 3,970,000.00 USD | 3,360.00 USD | 15,950.00 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 5,540,000.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 3,950,000.00 USD | 3,950,000.00 USD | 39,570.00 USD | 17,890.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 5,490,000.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 3,850,000.00 USD | 3,850,000.00 USD | 111,870.00 USD | 20,390.00 USD | 153,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 5,380,000.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 3,570,000.00 USD | 3,570,000.00 USD | 26,800.00 USD | 19,590.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 5,080,000.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 22,430.00 USD | 553,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.27` | 3,510,000.00 USD | 3,510,000.00 USD | 18,050.00 USD | 11,470.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 4,960,000.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 3,440,000.00 USD | 3,440,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 4,780,000.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 3,400,000.00 USD | 3,400,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 4,690,000.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 3,300,000.00 USD | 3,300,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 4,490,000.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 3,220,000.00 USD | 3,220,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 4,290,000.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 21,330.00 USD | 531,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.37` | 3,160,000.00 USD | 3,160,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 4,220,000.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 3,080,000.00 USD | 3,080,000.00 USD | 7,450.00 USD | 41,060.00 USD | 44,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 4,100,000.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 2,980,000.00 USD | 2,980,000.00 USD | 259,620.00 USD | 45,690.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 4,030,000.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 2,590,000.00 USD | 2,590,000.00 USD | 248,090.00 USD | 62,710.00 USD | 71,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 3,690,000.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 2,210,000.00 USD | 2,210,000.00 USD | 332,800.00 USD | 44,610.00 USD | 277,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 3,620,000.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 48,180.00 USD | 510,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.47` | 1,550,000.00 USD | 1,550,000.00 USD | 219,660.00 USD | 80,860.00 USD | 77,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 3,320,000.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 1,170,000.00 USD | 1,170,000.00 USD | 124,820.00 USD | 26,560.00 USD | 88,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 3,010,000.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 933,190.00 USD | 933,190.00 USD | 27,700.00 USD | 6,670.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 2,820,000.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 885,260.00 USD | 885,260.00 USD | 43,880.00 USD | 39,730.00 USD | 117,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 2,730,000.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 684,070.00 USD | 684,070.00 USD | 7,160.00 USD | 517.73 USD | 56,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 2,660,000.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 443,270.00 USD | 461,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.57` | 620,110.00 USD | 620,110.00 USD | 52,260.00 USD | 287.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 2,400,000.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 453,270.00 USD | 453,270.00 USD | 48,700.00 USD | 615.80 USD | 172,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 2,250,000.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 231,530.00 USD | 231,530.00 USD | 231,310.00 USD | 17.90 USD | 210.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 2,000,000.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.63` | 301,170.00 USD | 301,170.00 USD | 301,120.00 USD | 0.00 USD | 51.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 1,460,000.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.65` | 301,820.00 USD | 301,820.00 USD | 644.06 USD | 0.00 USD | 0.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 1,360,000.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 18,720.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.67` | 301,830.00 USD | 301,830.00 USD | 0.00 USD | 0.00 USD | 10.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 1,290,000.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.69` | 423,930.00 USD | 423,930.00 USD | 122,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 801,310.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.71` | 646,780.00 USD | 646,780.00 USD | 219,090.00 USD | 25.97 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 323,480.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.73` | 656,610.00 USD | 656,610.00 USD | 6,180.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 29,560.00 USD | 29,560.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 59,120.00 USD | 59,120.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.75` | 746,660.00 USD | 746,660.00 USD | 89,590.00 USD | 430.90 USD | 20.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.75` | 77,290.00 USD | 77,290.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.75` | 18,760.00 USD | 18,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.77` | 756,060.00 USD | 756,060.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.77` | 98,870.00 USD | 98,870.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.79` | 929,710.00 USD | 929,710.00 USD | 88,000.00 USD | 85,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.79` | 192,270.00 USD | 192,270.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.81` | 992,460.00 USD | 992,460.00 USD | 0.00 USD | 62,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.83` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 34,810.00 USD | 50,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.85` | 1,180,000.00 USD | 1,180,000.00 USD | 75,750.00 USD | 26,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 2,530.00 USD | 21,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.97` | 1,980,000.00 USD | 1,980,000.00 USD | 124.21 USD | 15,600.00 USD | 54,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.97` | 240,550.00 USD | 240,550.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.99` | 1,980,000.00 USD | 1,980,000.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 413,570.00 USD | 413,570.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.01` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 17,840.00 USD | 106,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 424,150.00 USD | 424,150.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.03` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 15,920.00 USD | 145,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 576,560.00 USD | 576,560.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.05` | 2,550,000.00 USD | 2,550,000.00 USD | 192,840.00 USD | 1,480.00 USD | 90,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 966,150.00 USD | 966,150.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.05` | 496.15 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.07` | 3,140,000.00 USD | 3,140,000.00 USD | 473,120.00 USD | 32,310.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 973,650.00 USD | 973,650.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 3,580,000.00 USD | 3,580,000.00 USD | 227,910.00 USD | 46,680.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 981,150.00 USD | 981,150.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 3,850,000.00 USD | 3,850,000.00 USD | 216,430.00 USD | 37,650.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 4,520,000.00 USD | 4,520,000.00 USD | 408,510.00 USD | 91,630.00 USD | 167,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 4,720,000.00 USD | 4,720,000.00 USD | 194,240.00 USD | 11,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 4,850,000.00 USD | 4,850,000.00 USD | 165.70 USD | 69,930.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 5,020,000.00 USD | 5,020,000.00 USD | 72,110.00 USD | 63,920.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 5,250,000.00 USD | 5,250,000.00 USD | 114,530.00 USD | 425.43 USD | 116,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 5,550,000.00 USD | 5,550,000.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 5,830,000.00 USD | 5,830,000.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 11,850.00 USD | 33,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.27` | 6,320,000.00 USD | 6,320,000.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 6,820,000.00 USD | 6,820,000.00 USD | 165,410.00 USD | 123,030.00 USD | 213,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 7,030,000.00 USD | 7,030,000.00 USD | 63,250.00 USD | 67,150.00 USD | 79,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 7,300,000.00 USD | 7,300,000.00 USD | 198,020.00 USD | 38,820.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 7,790,000.00 USD | 7,790,000.00 USD | 297,850.00 USD | 124,090.00 USD | 66,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 5,930.00 USD | 39,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.37` | 8,040,000.00 USD | 8,040,000.00 USD | 150,920.00 USD | 78,610.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 8,090,000.00 USD | 8,090,000.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 8,360,000.00 USD | 8,360,000.00 USD | 95,030.00 USD | 34,780.00 USD | 140,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 8,520,000.00 USD | 8,520,000.00 USD | 52,230.00 USD | 26,360.00 USD | 88,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 8,640,000.00 USD | 8,640,000.00 USD | 46,070.00 USD | 69,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 20,310.00 USD | 59,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.47` | 8,730,000.00 USD | 8,730,000.00 USD | 48,370.00 USD | 19,590.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 8,820,000.00 USD | 8,820,000.00 USD | 33,390.00 USD | 22,330.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 8,920,000.00 USD | 8,920,000.00 USD | 41,360.00 USD | 28,330.00 USD | 30,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 9,000,000.00 USD | 9,000,000.00 USD | 32,640.00 USD | 16,860.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 9,040,000.00 USD | 9,040,000.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 71,370.00 USD | 131,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.57` | 9,150,000.00 USD | 9,150,000.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 9,210,000.00 USD | 9,210,000.00 USD | 15,100.00 USD | 7,660.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 9,440,000.00 USD | 9,440,000.00 USD | 153,200.00 USD | 0.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 9,450,000.00 USD | 9,450,000.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 9,460,000.00 USD | 9,460,000.00 USD | 1,410.00 USD | 7,130.00 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 8,500.00 USD | 139,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.67` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 6,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 9,560,000.00 USD | 9,560,000.00 USD | 59,600.00 USD | 29,410.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 9,710,000.00 USD | 9,710,000.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 9,930,000.00 USD | 9,930,000.00 USD | 138,580.00 USD | 5,720.00 USD | 76,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 10,050,000.00 USD | 10,050,000.00 USD | 21,990.00 USD | 35,620.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 1,540.00 USD | 141,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.77` | 10,120,000.00 USD | 10,120,000.00 USD | 41,180.00 USD | 18,670.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 10,180,000.00 USD | 10,180,000.00 USD | 12,080.00 USD | 755.20 USD | 40,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 17,960.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 10,270,000.00 USD | 10,270,000.00 USD | 11,070.00 USD | 11,510.00 USD | 29,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 10,450,000.00 USD | 10,450,000.00 USD | 76,700.00 USD | 22,590.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 10,550,000.00 USD | 10,550,000.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 10,650,000.00 USD | 10,650,000.00 USD | 44,160.00 USD | 11,410.00 USD | 43,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 10,800,000.00 USD | 10,800,000.00 USD | 102,960.00 USD | 18,340.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 10,990,000.00 USD | 10,990,000.00 USD | 135,130.00 USD | 28,540.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 11,140,000.00 USD | 11,140,000.00 USD | 85,850.00 USD | 21,080.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 11,350,000.00 USD | 11,350,000.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 11,550,000.00 USD | 11,550,000.00 USD | 123,700.00 USD | 25,870.00 USD | 46,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 11,670,000.00 USD | 11,670,000.00 USD | 60,120.00 USD | 9,410.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 11,830,000.00 USD | 11,830,000.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 12,170,000.00 USD | 12,170,000.00 USD | 206,510.00 USD | 58,260.00 USD | 81,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.05` | 7,480.00 USD | 148,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.07` | 12,440,000.00 USD | 12,440,000.00 USD | 114,130.00 USD | 53,190.00 USD | 97,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 12,490,000.00 USD | 12,490,000.00 USD | 17,390.00 USD | 18,490.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 12,680,000.00 USD | 12,680,000.00 USD | 94,540.00 USD | 34,950.00 USD | 55,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 12,850,000.00 USD | 12,850,000.00 USD | 94,650.00 USD | 33,860.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 13,070,000.00 USD | 13,070,000.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 25,210.00 USD | 173,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.17` | 13,330,000.00 USD | 13,330,000.00 USD | 122,970.00 USD | 64,130.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 13,430,000.00 USD | 13,430,000.00 USD | 64,080.00 USD | 24,200.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 13,560,000.00 USD | 13,560,000.00 USD | 52,950.00 USD | 28,750.00 USD | 50,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 13,600,000.00 USD | 13,600,000.00 USD | 14,580.00 USD | 24,000.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 13,620,000.00 USD | 13,620,000.00 USD | 2,260.00 USD | 5,380.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,010.00 USD | 174,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.27` | 13,700,000.00 USD | 13,700,000.00 USD | 52,420.00 USD | 9,580.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 13,790,000.00 USD | 13,790,000.00 USD | 36,110.00 USD | 19,760.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 13,820,000.00 USD | 13,820,000.00 USD | 19,750.00 USD | 4,850.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 13,830,000.00 USD | 13,830,000.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 13,870,000.00 USD | 13,870,000.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 117,910.00 USD | 292,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.37` | 13,890,000.00 USD | 13,890,000.00 USD | 8,820.00 USD | 5,700.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 13,950,000.00 USD | 13,950,000.00 USD | 28,430.00 USD | 12,560.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 14,040,000.00 USD | 14,040,000.00 USD | 42,540.00 USD | 19,990.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 14,070,000.00 USD | 14,070,000.00 USD | 23,090.00 USD | 5,940.00 USD | 88.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 14,090,000.00 USD | 14,090,000.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 12,000.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 903.60 USD | 293,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 113.85 USD | 293,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.67` | 19,800,000.00 USD | 19,800,000.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 20,040,000.00 USD | 20,040,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 20,130,000.00 USD | 20,130,000.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 20,220,000.00 USD | 20,220,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 20,290,000.00 USD | 20,290,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 20,380,000.00 USD | 20,380,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 20,470,000.00 USD | 20,470,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 20,490,000.00 USD | 20,490,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 20,520,000.00 USD | 20,520,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 20,600,000.00 USD | 20,600,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 294,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.87` | 20,640,000.00 USD | 20,640,000.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 20,730,000.00 USD | 20,730,000.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 20,840,000.00 USD | 20,840,000.00 USD | 59,260.00 USD | 15,540.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 20,870,000.00 USD | 20,870,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 20,890,000.00 USD | 20,890,000.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 20,930,000.00 USD | 20,930,000.00 USD | 13,890.00 USD | 10,560.00 USD | 24,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 21,000,000.00 USD | 21,000,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 21,050,000.00 USD | 21,050,000.00 USD | 26,320.00 USD | 2,920.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 21,060,000.00 USD | 21,060,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 21,060,000.00 USD | 21,060,000.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.07` | 21,110,000.00 USD | 21,110,000.00 USD | 23,750.00 USD | 6,890.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 21,130,000.00 USD | 21,130,000.00 USD | 16,060.00 USD | 527.72 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 21,160,000.00 USD | 21,160,000.00 USD | 19,270.00 USD | 5,960.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 21,180,000.00 USD | 21,180,000.00 USD | 13,360.00 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.17` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 21,200,000.00 USD | 21,200,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 21,230,000.00 USD | 21,230,000.00 USD | 13,890.00 USD | 6,210.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 21,240,000.00 USD | 21,240,000.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 21,300,000.00 USD | 21,300,000.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 158.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,280.00 USD | 299,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.85` | 6,470.00 USD | 305,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 449.60 USD | 306,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 1,960.00 USD | 308,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 315.01 USD | 308,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 169,800.00 USD | 478,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 10,800.00 USD | 489,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,500.00 USD | 514,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.15` | 72,340.00 USD | 586,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 587,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 1,280.00 USD | 589,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 589,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 589,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 591,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,190.00 USD | 605,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.65` | 382.95 USD | 605,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 112,250.00 USD | 717,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 797,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 238.70 USD | 797,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 2,090.00 USD | 799,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 18,250.00 USD | 818,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 11,150.00 USD | 829,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 829,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 829,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 254,100.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 28,240.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 4,010.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 3,470.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 5,950.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 126,640.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 714,600.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 1,200.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 29,470.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 897,840.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 254.78 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 2,370,000.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.95` | 4,220.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.25` | 499.38 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.15` | 11,460,000.00 USD | 0.00 USD | 572.98 USD | `-79.51%` | `266,500.00` |
| `Live` | `Long` | `2.25` | 11,460,000.00 USD | 0.00 USD | 5,430.00 USD | `-78.56%` | `2,411,200.00` |
| `Live` | `Long` | `2.35` | 11,460,000.00 USD | 0.00 USD | 11,150.00 USD | `-77.61%` | `4,744,800.00` |
| `Live` | `Long` | `2.55` | 11,450,000.00 USD | 0.00 USD | 51,900.00 USD | `-75.70%` | `20,353,900.00` |
| `Live` | `Long` | `2.65` | 11,390,000.00 USD | 0.00 USD | 1,840.00 USD | `-74.75%` | `694,000.00` |
| `Live` | `Long` | `2.75` | 11,390,000.00 USD | 0.00 USD | 2,750.00 USD | `-73.80%` | `1,000,000.00` |
| `Live` | `Long` | `2.85` | 11,390,000.00 USD | 0.00 USD | 4,060.00 USD | `-72.84%` | `1,423,700.00` |
| `Live` | `Long` | `3.05` | 11,390,000.00 USD | 0.00 USD | 6,390.00 USD | `-70.94%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 11,380,000.00 USD | 0.00 USD | 2,860.00 USD | `-69.98%` | `907,300.00` |
| `Live` | `Long` | `3.25` | 11,380,000.00 USD | 0.00 USD | 33,080.00 USD | `-69.03%` | `10,177,800.00` |
| `Live` | `Long` | `3.35` | 11,340,000.00 USD | 0.00 USD | 700.82 USD | `-68.08%` | `209,200.00` |
| `Live` | `Long` | `3.45` | 11,340,000.00 USD | 0.00 USD | 17,250.00 USD | `-67.13%` | `5,000,000.00` |
| `Live` | `Long` | `3.55` | 11,330,000.00 USD | 0.00 USD | 8,390.00 USD | `-66.17%` | `2,363,000.00` |
| `Live` | `Long` | `3.65` | 11,320,000.00 USD | 0.00 USD | 2,610.00 USD | `-65.22%` | `716,200.00` |
| `Live` | `Long` | `3.75` | 11,310,000.00 USD | 0.00 USD | 1,110.00 USD | `-64.27%` | `295,700.00` |
| `Live` | `Long` | `3.85` | 11,310,000.00 USD | 0.00 USD | 4,950.00 USD | `-63.31%` | `1,287,000.00` |
| `Live` | `Long` | `3.95` | 11,310,000.00 USD | 0.00 USD | 7,090.00 USD | `-62.36%` | `1,796,200.00` |
| `Live` | `Long` | `4.05` | 11,300,000.00 USD | 0.00 USD | 5,480.00 USD | `-61.41%` | `1,353,400.00` |
| `Live` | `Long` | `4.25` | 11,300,000.00 USD | 0.00 USD | 8,100.00 USD | `-59.50%` | `1,905,100.00` |
| `Live` | `Long` | `4.35` | 11,290,000.00 USD | 0.00 USD | 1,570.00 USD | `-58.55%` | `360,300.00` |
| `Live` | `Long` | `4.45` | 11,290,000.00 USD | 0.00 USD | 381.37 USD | `-57.60%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 11,290,000.00 USD | 0.00 USD | 295.75 USD | `-56.64%` | `65,000.00` |
| `Live` | `Long` | `4.65` | 11,290,000.00 USD | 0.00 USD | 9,460.00 USD | `-55.69%` | `2,034,400.00` |
| `Live` | `Long` | `4.75` | 11,280,000.00 USD | 0.00 USD | 1,100.00 USD | `-54.74%` | `232,600.00` |
| `Live` | `Long` | `4.85` | 11,270,000.00 USD | 0.00 USD | 1,190.00 USD | `-53.79%` | `245,800.00` |
| `Live` | `Long` | `4.95` | 11,270,000.00 USD | 0.00 USD | 243,430.00 USD | `-52.83%` | `49,178,400.00` |
| `Live` | `Long` | `5.15` | 11,030,000.00 USD | 0.00 USD | 3,750.00 USD | `-50.93%` | `728,600.00` |
| `Live` | `Long` | `5.25` | 11,030,000.00 USD | 0.00 USD | 58,000.00 USD | `-49.97%` | `11,048,200.00` |
| `Live` | `Long` | `5.35` | 10,970,000.00 USD | 0.00 USD | 633,250.00 USD | `-49.02%` | `118,363,600.00` |
| `Live` | `Long` | `5.45` | 10,340,000.00 USD | 0.00 USD | 60,620.00 USD | `-48.07%` | `11,123,400.00` |
| `Live` | `Long` | `5.55` | 10,270,000.00 USD | 0.00 USD | 28,830.00 USD | `-47.12%` | `5,194,700.00` |
| `Live` | `Long` | `5.65` | 10,250,000.00 USD | 0.00 USD | 38,610.00 USD | `-46.16%` | `6,833,000.00` |
| `Live` | `Long` | `5.75` | 10,210,000.00 USD | 0.00 USD | 17,530.00 USD | `-45.21%` | `3,048,100.00` |
| `Live` | `Long` | `5.85` | 10,190,000.00 USD | 0.00 USD | 1,950.00 USD | `-44.26%` | `332,600.00` |
| `Live` | `Long` | `5.95` | 10,190,000.00 USD | 0.00 USD | 24,770.00 USD | `-43.30%` | `4,162,400.00` |
| `Live` | `Long` | `6.05` | 10,160,000.00 USD | 0.00 USD | 13,590.00 USD | `-42.35%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 10,150,000.00 USD | 0.00 USD | 11,500.00 USD | `-41.40%` | `1,870,700.00` |
| `Live` | `Long` | `6.25` | 10,140,000.00 USD | 0.00 USD | 26,040.00 USD | `-40.44%` | `4,166,700.00` |
| `Live` | `Long` | `6.35` | 10,110,000.00 USD | 0.00 USD | 32,180.00 USD | `-39.49%` | `5,068,400.00` |
| `Live` | `Long` | `6.45` | 10,080,000.00 USD | 0.00 USD | 54,650.00 USD | `-38.54%` | `8,472,100.00` |
| `Live` | `Long` | `6.55` | 10,020,000.00 USD | 0.00 USD | 2,710.00 USD | `-37.59%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 10,020,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-36.63%` | `172,413,700.00` |
| `Live` | `Long` | `6.75` | 8,880,000.00 USD | 0.00 USD | 39,050.00 USD | `-35.68%` | `5,785,400.00` |
| `Live` | `Long` | `6.85` | 8,840,000.00 USD | 0.00 USD | 5,060.00 USD | `-34.73%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 8,830,000.00 USD | 0.00 USD | 30,450.00 USD | `-33.77%` | `4,380,600.00` |
| `Live` | `Long` | `7.05` | 8,800,000.00 USD | 0.00 USD | 12,930.00 USD | `-32.82%` | `1,834,700.00` |
| `Live` | `Long` | `7.15` | 8,790,000.00 USD | 0.00 USD | 25,430.00 USD | `-31.87%` | `3,556,900.00` |
| `Live` | `Long` | `7.25` | 8,760,000.00 USD | 0.00 USD | 5,020.00 USD | `-30.92%` | `691,800.00` |
| `Live` | `Long` | `7.35` | 8,760,000.00 USD | 0.00 USD | 28,660.00 USD | `-29.96%` | `3,899,400.00` |
| `Live` | `Long` | `7.45` | 8,730,000.00 USD | 0.00 USD | 13,330.00 USD | `-29.01%` | `1,789,000.00` |
| `Live` | `Long` | `7.55` | 8,720,000.00 USD | 0.00 USD | 20,690.00 USD | `-28.06%` | `2,740,300.00` |
| `Live` | `Long` | `7.65` | 8,690,000.00 USD | 0.00 USD | 2,230.00 USD | `-27.10%` | `291,100.00` |
| `Live` | `Long` | `7.75` | 8,690,000.00 USD | 0.00 USD | 26,720.00 USD | `-26.15%` | `3,447,200.00` |
| `Live` | `Long` | `7.85` | 8,670,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-25.20%` | `400,792,700.00` |
| `Live` | `Long` | `7.95` | 5,520,000.00 USD | 0.00 USD | 26,900.00 USD | `-24.25%` | `3,384,200.00` |
| `Live` | `Long` | `8.05` | 5,490,000.00 USD | 0.00 USD | 68,240.00 USD | `-23.29%` | `8,476,900.00` |
| `Live` | `Long` | `8.15` | 5,420,000.00 USD | 0.00 USD | 37,390.00 USD | `-22.34%` | `4,587,300.00` |
| `Live` | `Long` | `8.25` | 5,390,000.00 USD | 0.00 USD | 200,780.00 USD | `-21.39%` | `24,337,000.00` |
| `Live` | `Long` | `8.35` | 5,190,000.00 USD | 0.00 USD | 1,880.00 USD | `-20.43%` | `225,000.00` |
| `Live` | `Long` | `8.45` | 5,180,000.00 USD | 0.00 USD | 36,550.00 USD | `-19.48%` | `4,324,900.00` |
| `Live` | `Long` | `8.55` | 5,150,000.00 USD | 0.00 USD | 75,710.00 USD | `-18.53%` | `8,854,900.00` |
| `Live` | `Long` | `8.65` | 5,070,000.00 USD | 0.00 USD | 356,250.00 USD | `-17.58%` | `41,184,800.00` |
| `Live` | `Long` | `8.75` | 4,720,000.00 USD | 0.00 USD | 26,540.00 USD | `-16.62%` | `3,032,600.00` |
| `Live` | `Long` | `8.85` | 4,690,000.00 USD | 0.00 USD | 43,400.00 USD | `-15.67%` | `4,903,800.00` |
| `Live` | `Long` | `8.95` | 4,650,000.00 USD | 0.00 USD | 454,650.00 USD | `-14.72%` | `50,799,200.00` |
| `Live` | `Long` | `9.05` | 4,190,000.00 USD | 0.00 USD | 92,750.00 USD | `-13.76%` | `10,248,400.00` |
| `Live` | `Long` | `9.15` | 4,100,000.00 USD | 0.00 USD | 112,620.00 USD | `-12.81%` | `12,308,300.00` |
| `Live` | `Long` | `9.25` | 3,990,000.00 USD | 0.00 USD | 15,800.00 USD | `-11.86%` | `1,707,700.00` |
| `Live` | `Long` | `9.35` | 3,970,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-10.91%` | `230,381,600.00` |
| `Live` | `Long` | `9.45` | 1,820,000.00 USD | 0.00 USD | 40,290.00 USD | `-9.95%` | `4,263,400.00` |
| `Live` | `Long` | `9.55` | 1,780,000.00 USD | 0.00 USD | 62,130.00 USD | `-9.00%` | `6,506,100.00` |
| `Live` | `Long` | `9.65` | 1,710,000.00 USD | 0.00 USD | 198,730.00 USD | `-8.05%` | `20,594,000.00` |
| `Live` | `Long` | `9.75` | 1,520,000.00 USD | 0.00 USD | 73,550.00 USD | `-7.09%` | `7,543,700.00` |
| `Live` | `Long` | `9.85` | 1,440,000.00 USD | 0.00 USD | 128,680.00 USD | `-6.14%` | `13,063,800.00` |
| `Live` | `Long` | `9.95` | 1,310,000.00 USD | 0.00 USD | 444,330.00 USD | `-5.19%` | `44,655,800.00` |
| `Live` | `Long` | `10.05` | 868,520.00 USD | 0.00 USD | 772,230.00 USD | `-4.24%` | `76,838,500.00` |
| `Live` | `Long` | `10.15` | 96,300.00 USD | 0.00 USD | 63,650.00 USD | `-3.28%` | `6,270,500.00` |
| `Live` | `Long` | `10.25` | 32,650.00 USD | 0.00 USD | 32,650.00 USD | `-2.33%` | `3,185,600.00` |
| `Live` | `Short` | `10.85` | 1,090.00 USD | 1,090.00 USD | 0.00 USD | `+3.39%` | `100,000.00` |
| `Live` | `Short` | `10.95` | 18,980.00 USD | 17,900.00 USD | 0.00 USD | `+4.34%` | `1,634,300.00` |
| `Live` | `Short` | `11.05` | 33,470.00 USD | 14,490.00 USD | 0.00 USD | `+5.29%` | `1,311,600.00` |
| `Live` | `Short` | `11.15` | 35,570.00 USD | 2,100.00 USD | 0.00 USD | `+6.25%` | `187,900.00` |
| `Live` | `Short` | `11.25` | 35,770.00 USD | 196.88 USD | 0.00 USD | `+7.20%` | `17,500.00` |
| `Live` | `Short` | `11.45` | 36,540.00 USD | 775.16 USD | 0.00 USD | `+9.10%` | `67,700.00` |
| `Live` | `Short` | `11.55` | 37,110.00 USD | 572.88 USD | 0.00 USD | `+10.06%` | `49,600.00` |
| `Live` | `Short` | `11.75` | 110,070.00 USD | 72,950.00 USD | 0.00 USD | `+11.96%` | `6,208,800.00` |
| `Live` | `Short` | `12.15` | 114,230.00 USD | 4,160.00 USD | 0.00 USD | `+15.77%` | `342,700.00` |
| `Live` | `Short` | `12.25` | 115,660.00 USD | 1,430.00 USD | 0.00 USD | `+16.73%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 116,400.00 USD | 736.06 USD | 0.00 USD | `+17.68%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 116,780.00 USD | 380.27 USD | 0.00 USD | `+19.59%` | `30,300.00` |
| `Live` | `Short` | `12.65` | 117,210.00 USD | 435.16 USD | 0.00 USD | `+20.54%` | `34,400.00` |
| `Live` | `Short` | `12.85` | 117,350.00 USD | 138.78 USD | 0.00 USD | `+22.45%` | `10,800.00` |
| `Live` | `Short` | `13.15` | 117,500.00 USD | 144.65 USD | 0.00 USD | `+25.30%` | `11,000.00` |
| `Live` | `Short` | `13.45` | 122,780.00 USD | 5,280.00 USD | 0.00 USD | `+28.16%` | `392,900.00` |
| `Live` | `Short` | `13.85` | 123,120.00 USD | 342.10 USD | 0.00 USD | `+31.97%` | `24,700.00` |
| `Live` | `Short` | `14.15` | 124,140.00 USD | 1,020.00 USD | 0.00 USD | `+34.83%` | `71,800.00` |
| `Live` | `Short` | `14.25` | 124,680.00 USD | 544.35 USD | 0.00 USD | `+35.79%` | `38,200.00` |
| `Live` | `Short` | `14.95` | 150,170.00 USD | 25,490.00 USD | 0.00 USD | `+42.46%` | `1,704,800.00` |
| `Live` | `Short` | `15.15` | 212,680.00 USD | 62,510.00 USD | 0.00 USD | `+44.36%` | `4,125,800.00` |
| `Live` | `Short` | `15.55` | 213,250.00 USD | 578.46 USD | 0.00 USD | `+48.17%` | `37,200.00` |
| `Live` | `Short` | `15.65` | 213,410.00 USD | 158.07 USD | 0.00 USD | `+49.13%` | `10,100.00` |
| `Live` | `Short` | `15.85` | 213,680.00 USD | 271.04 USD | 0.00 USD | `+51.03%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 213,820.00 USD | 138.76 USD | 0.00 USD | `+51.98%` | `8,700.00` |
| `Live` | `Short` | `16.25` | 214,050.00 USD | 227.50 USD | 0.00 USD | `+54.84%` | `14,000.00` |
| `Live` | `Short` | `16.35` | 215,580.00 USD | 1,530.00 USD | 0.00 USD | `+55.80%` | `93,400.00` |
| `Live` | `Short` | `16.55` | 229,770.00 USD | 14,190.00 USD | 0.00 USD | `+57.70%` | `857,700.00` |
| `Live` | `Short` | `16.75` | 320,980.00 USD | 91,200.00 USD | 0.00 USD | `+59.61%` | `5,445,000.00` |
| `Live` | `Short` | `16.95` | 400,930.00 USD | 79,960.00 USD | 0.00 USD | `+61.51%` | `4,717,300.00` |
| `Live` | `Short` | `17.05` | 401,120.00 USD | 187.55 USD | 0.00 USD | `+62.47%` | `11,000.00` |
| `Live` | `Short` | `17.15` | 402,490.00 USD | 1,370.00 USD | 0.00 USD | `+63.42%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 420,740.00 USD | 18,250.00 USD | 0.00 USD | `+64.37%` | `1,058,000.00` |
| `Live` | `Short` | `17.45` | 431,890.00 USD | 11,150.00 USD | 0.00 USD | `+66.28%` | `639,000.00` |
| `Live` | `Short` | `17.85` | 432,140.00 USD | 249.90 USD | 0.00 USD | `+70.09%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 432,690.00 USD | 549.27 USD | 0.00 USD | `+71.04%` | `30,600.00` |
| `Live` | `Short` | `18.05` | 686,780.00 USD | 254,100.00 USD | 0.00 USD | `+71.99%` | `14,077,300.00` |
| `Live` | `Short` | `18.15` | 1,370,000.00 USD | 684,440.00 USD | 0.00 USD | `+72.95%` | `37,710,000.00` |
| `Live` | `Short` | `18.35` | 1,400,000.00 USD | 28,240.00 USD | 0.00 USD | `+74.85%` | `1,539,000.00` |
| `Live` | `Short` | `18.45` | 1,400,000.00 USD | 3,890.00 USD | 0.00 USD | `+75.81%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,400,000.00 USD | 921.94 USD | 0.00 USD | `+76.76%` | `49,700.00` |
| `Live` | `Short` | `18.65` | 1,410,000.00 USD | 5,950.00 USD | 0.00 USD | `+77.71%` | `319,000.00` |
| `Live` | `Short` | `18.85` | 1,410,000.00 USD | 456.17 USD | 0.00 USD | `+79.62%` | `24,200.00` |
| `Live` | `Short` | `19.35` | 1,440,000.00 USD | 29,600.00 USD | 0.00 USD | `+84.38%` | `1,529,600.00` |
| `Live` | `Short` | `19.55` | 2,260,000.00 USD | 823,710.00 USD | 0.00 USD | `+86.29%` | `42,133,300.00` |
| `Live` | `Short` | `19.65` | 2,380,000.00 USD | 115,330.00 USD | 0.00 USD | `+87.24%` | `5,869,000.00` |
| `Live` | `Short` | `19.75` | 2,380,000.00 USD | 359.45 USD | 0.00 USD | `+88.19%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 2,380,000.00 USD | 218.35 USD | 0.00 USD | `+89.15%` | `11,000.00` |
| `Live` | `Short` | `19.95` | 2,380,000.00 USD | 291.27 USD | 0.00 USD | `+90.10%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 2,380,000.00 USD | 1,450.00 USD | 0.00 USD | `+92.01%` | `71,900.00` |
| `Live` | `Short` | `20.25` | 4,710,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+92.96%` | `115,047,700.00` |
| `Live` | `Short` | `20.55` | 4,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+95.82%` | `353,000.00` |
| `Live` | `Short` | `20.75` | 4,720,000.00 USD | 228.25 USD | 0.00 USD | `+97.72%` | `11,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 378,750.00 USD | 0.00 USD | 182.03 USD | `-76.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 378,570.00 USD | 0.00 USD | 209.48 USD | `-69.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 378,360.00 USD | 0.00 USD | 431.68 USD | `-66.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 377,930.00 USD | 0.00 USD | 290.29 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 377,640.00 USD | 0.00 USD | 120.22 USD | `-49.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 377,520.00 USD | 0.00 USD | 251.68 USD | `-42.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 377,270.00 USD | 0.00 USD | 749.30 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 376,520.00 USD | 0.00 USD | 186.41 USD | `-38.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 376,330.00 USD | 0.00 USD | 3,760.00 USD | `-37.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 372,570.00 USD | 0.00 USD | 133.00 USD | `-36.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 372,430.00 USD | 0.00 USD | 1,320.00 USD | `-33.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 371,120.00 USD | 0.00 USD | 34,200.00 USD | `-32.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 336,920.00 USD | 0.00 USD | 2,070.00 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 334,840.00 USD | 0.00 USD | 3,740.00 USD | `-29.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 331,100.00 USD | 0.00 USD | 1,050.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 330,050.00 USD | 0.00 USD | 120.90 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 329,930.00 USD | 0.00 USD | 146.80 USD | `-25.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 329,780.00 USD | 0.00 USD | 166.95 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 329,610.00 USD | 0.00 USD | 5,000.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 324,610.00 USD | 0.00 USD | 393.64 USD | `-22.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 324,220.00 USD | 0.00 USD | 10,560.00 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 313,650.00 USD | 0.00 USD | 3,110.00 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 310,540.00 USD | 0.00 USD | 1,480.00 USD | `-19.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 309,070.00 USD | 0.00 USD | 52,990.00 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 256,080.00 USD | 0.00 USD | 186.84 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 255,890.00 USD | 0.00 USD | 742.88 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 255,150.00 USD | 0.00 USD | 4,510.00 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 250,640.00 USD | 0.00 USD | 1,570.00 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 249,070.00 USD | 0.00 USD | 3,160.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 245,910.00 USD | 0.00 USD | 194.90 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 245,710.00 USD | 0.00 USD | 1,020.00 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 244,690.00 USD | 0.00 USD | 7,840.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 236,850.00 USD | 0.00 USD | 2,310.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 234,540.00 USD | 0.00 USD | 9,660.00 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 224,870.00 USD | 0.00 USD | 541.37 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 224,330.00 USD | 0.00 USD | 854.10 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 223,480.00 USD | 0.00 USD | 25,210.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 198,270.00 USD | 0.00 USD | 15,240.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 183,020.00 USD | 0.00 USD | 42,800.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 140,220.00 USD | 0.00 USD | 5,960.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 134,270.00 USD | 0.00 USD | 133,790.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 476.24 USD | 0.00 USD | 245.30 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 230.94 USD | 0.00 USD | 230.94 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.55` | 18,460.00 USD | 18,460.00 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.65` | 71,310.00 USD | 52,850.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.75` | 73,340.00 USD | 2,030.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.85` | 78,760.00 USD | 5,430.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.95` | 84,900.00 USD | 6,130.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 85,570.00 USD | 675.16 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 87,390.00 USD | 1,820.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 101,960.00 USD | 14,560.00 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 108,650.00 USD | 6,690.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 109,050.00 USD | 396.17 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 128,550.00 USD | 19,500.00 USD | 0.00 USD | `+10.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 130,790.00 USD | 2,250.00 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 131,540.00 USD | 746.12 USD | 0.00 USD | `+11.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 131,790.00 USD | 253.59 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 135,420.00 USD | 3,620.00 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 163,260.00 USD | 27,850.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 165,340.00 USD | 2,080.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 174,830.00 USD | 9,490.00 USD | 0.00 USD | `+16.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 175,430.00 USD | 597.74 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 175,670.00 USD | 240.28 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 295,810.00 USD | 120,140.00 USD | 0.00 USD | `+19.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 380,380.00 USD | 84,570.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 381,060.00 USD | 679.57 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 401,430.00 USD | 20,360.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 401,880.00 USD | 451.95 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 418,510.00 USD | 16,630.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 438,130.00 USD | 19,620.00 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 439,440.00 USD | 1,320.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 447,230.00 USD | 7,790.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 449,770.00 USD | 2,540.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 449,930.00 USD | 165.31 USD | 0.00 USD | `+29.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 450,890.00 USD | 954.14 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 452,950.00 USD | 2,060.00 USD | 0.00 USD | `+31.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 457,830.00 USD | 4,880.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 458,090.00 USD | 266.44 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 474,360.00 USD | 16,260.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 474,510.00 USD | 152.82 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 478,780.00 USD | 4,280.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 482,200.00 USD | 3,410.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 501,640.00 USD | 19,440.00 USD | 0.00 USD | `+37.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 501,850.00 USD | 218.25 USD | 0.00 USD | `+38.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 504,100.00 USD | 2,250.00 USD | 0.00 USD | `+39.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 511,370.00 USD | 7,270.00 USD | 0.00 USD | `+40.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 512,320.00 USD | 950.82 USD | 0.00 USD | `+42.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 537,180.00 USD | 24,860.00 USD | 0.00 USD | `+43.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 539,630.00 USD | 2,450.00 USD | 0.00 USD | `+44.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 772,670.00 USD | 233,040.00 USD | 0.00 USD | `+45.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 773,590.00 USD | 924.07 USD | 0.00 USD | `+46.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 774,480.00 USD | 893.01 USD | 0.00 USD | `+47.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 775,140.00 USD | 653.10 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 775,610.00 USD | 472.63 USD | 0.00 USD | `+49.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 778,900.00 USD | 3,290.00 USD | 0.00 USD | `+50.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 782,070.00 USD | 3,170.00 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 787,210.00 USD | 5,130.00 USD | 0.00 USD | `+51.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 802,280.00 USD | 15,080.00 USD | 0.00 USD | `+52.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 809,090.00 USD | 6,800.00 USD | 0.00 USD | `+53.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 815,590.00 USD | 6,500.00 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 822,130.00 USD | 6,540.00 USD | 0.00 USD | `+55.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 828,710.00 USD | 6,580.00 USD | 0.00 USD | `+56.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 838,640.00 USD | 9,930.00 USD | 0.00 USD | `+57.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 942,620.00 USD | 103,980.00 USD | 0.00 USD | `+58.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 956,850.00 USD | 14,240.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 1,040,000.00 USD | 84,360.00 USD | 0.00 USD | `+60.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 1,040,000.00 USD | 1,700.00 USD | 0.00 USD | `+61.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 1,050,000.00 USD | 7,370.00 USD | 0.00 USD | `+62.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 1,050,000.00 USD | 1,710.00 USD | 0.00 USD | `+63.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 1,050,000.00 USD | 2,300.00 USD | 0.00 USD | `+64.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,060,000.00 USD | 1,740.00 USD | 0.00 USD | `+65.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,080,000.00 USD | 21,690.00 USD | 0.00 USD | `+66.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,080,000.00 USD | 4,390.00 USD | 0.00 USD | `+67.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,090,000.00 USD | 4,410.00 USD | 0.00 USD | `+68.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,090,000.00 USD | 4,440.00 USD | 0.00 USD | `+69.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,100,000.00 USD | 4,460.00 USD | 0.00 USD | `+70.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,100,000.00 USD | 448.75 USD | 0.00 USD | `+71.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,130,000.00 USD | 30,960.00 USD | 0.00 USD | `+71.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,130,000.00 USD | 453.75 USD | 0.00 USD | `+72.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,130,000.00 USD | 456.25 USD | 0.00 USD | `+73.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,130,000.00 USD | 458.75 USD | 0.00 USD | `+74.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,130,000.00 USD | 461.25 USD | 0.00 USD | `+75.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,130,000.00 USD | 4,540.00 USD | 0.00 USD | `+76.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,130,000.00 USD | 466.25 USD | 0.00 USD | `+77.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,130,000.00 USD | 468.75 USD | 0.00 USD | `+78.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,130,000.00 USD | 471.25 USD | 0.00 USD | `+79.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,140,000.00 USD | 473.75 USD | 0.00 USD | `+80.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,200,000.00 USD | 67,000.00 USD | 0.00 USD | `+81.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,200,000.00 USD | 574.50 USD | 0.00 USD | `+82.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,200,000.00 USD | 577.50 USD | 0.00 USD | `+83.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,210,000.00 USD | 2,710.00 USD | 0.00 USD | `+84.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,210,000.00 USD | 972.50 USD | 0.00 USD | `+85.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,210,000.00 USD | 7,680.00 USD | 0.00 USD | `+86.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,220,000.00 USD | 786.00 USD | 0.00 USD | `+87.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,220,000.00 USD | 790.00 USD | 0.00 USD | `+88.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,220,000.00 USD | 992.50 USD | 0.00 USD | `+89.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,220,000.00 USD | 997.50 USD | 0.00 USD | `+90.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,820,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+91.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,820,000.00 USD | 1,010.00 USD | 0.00 USD | `+92.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,820,000.00 USD | 1,010.00 USD | 0.00 USD | `+92.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,820,000.00 USD | 1,020.00 USD | 0.00 USD | `+93.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,830,000.00 USD | 1,020.00 USD | 0.00 USD | `+94.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,830,000.00 USD | 1,030.00 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,830,000.00 USD | 1,030.00 USD | 0.00 USD | `+96.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,830,000.00 USD | 1,040.00 USD | 0.00 USD | `+97.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,830,000.00 USD | 1,410.00 USD | 0.00 USD | `+98.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,830,000.00 USD | 1,050.00 USD | 0.00 USD | `+99.63%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `9.45` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD |
| `1D` | `9.47` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD |
| `1D` | `9.53` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD |
| `7D` | `9.53` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD |
| `1D` | `9.55` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD |
| `7D` | `9.55` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD |
| `1D` | `9.57` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 0.00 USD | 1,780.00 USD | 0.00 USD |
| `7D` | `9.57` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD |
| `1D` | `9.59` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 40,390.00 USD | 6,150.00 USD | 34,990.00 USD |
| `7D` | `9.59` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `9.61` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 1,090.00 USD | 3,960.00 USD | 0.00 USD |
| `7D` | `9.61` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `1D` | `9.63` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 671.70 USD | 0.00 USD | 14,300.00 USD |
| `7D` | `9.63` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD |
| `1D` | `9.65` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 972.50 USD | 0.00 USD | 105.10 USD |
| `7D` | `9.65` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD |
| `1D` | `9.67` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD |
| `7D` | `9.67` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `9.69` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 10,890.00 USD |
| `7D` | `9.69` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.71` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD |
| `7D` | `9.71` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `1D` | `9.73` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD |
| `7D` | `9.73` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.75` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 40,030.00 USD | 0.00 USD | 13,160.00 USD |
| `7D` | `9.75` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD |
| `1D` | `9.77` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD |
| `7D` | `9.77` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.79` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD |
| `7D` | `9.79` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD |
| `1D` | `9.81` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,690.00 USD |
| `7D` | `9.81` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD |
| `1D` | `9.83` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 37,110.00 USD | 0.00 USD | 10,480.00 USD |
| `7D` | `9.83` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD |
| `1D` | `9.85` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD |
| `7D` | `9.85` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `9.87` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD |
| `7D` | `9.89` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.91` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD |
| `7D` | `9.91` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.93` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD |
| `7D` | `9.93` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.95` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD |
| `7D` | `9.95` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD |
| `1D` | `9.97` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD |
| `7D` | `9.97` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD |
| `1D` | `9.99` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD |
| `7D` | `9.99` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD |
| `1D` | `10.01` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD |
| `7D` | `10.01` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.03` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD |
| `1D` | `10.05` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD |
| `7D` | `10.05` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `7D` | `10.07` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `1D` | `10.09` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD |
| `7D` | `10.09` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD |
| `7D` | `10.11` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `10.13` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD |
| `7D` | `10.13` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.15` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD |
| `7D` | `10.15` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `1D` | `10.17` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 3,600.00 USD | 17,840.00 USD | 424.12 USD |
| `7D` | `10.17` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD |
| `1D` | `10.19` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 3,360.00 USD | 15,950.00 USD | 46.76 USD |
| `7D` | `10.19` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.21` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 39,570.00 USD | 17,890.00 USD | 37,590.00 USD |
| `7D` | `10.21` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.23` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 111,870.00 USD | 20,390.00 USD | 153,210.00 USD |
| `7D` | `10.23` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.25` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 26,800.00 USD | 19,590.00 USD | 11,020.00 USD |
| `7D` | `10.25` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.27` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 18,050.00 USD | 11,470.00 USD | 40,150.00 USD |
| `7D` | `10.27` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.29` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,860.00 USD |
| `7D` | `10.29` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD |
| `1D` | `10.31` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,300.00 USD |
| `7D` | `10.31` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD |
| `1D` | `10.33` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,350.00 USD |
| `7D` | `10.33` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD |
| `1D` | `10.35` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,090.00 USD |
| `7D` | `10.35` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.37` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,450.00 USD |
| `7D` | `10.37` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD |
| `1D` | `10.39` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 7,450.00 USD | 41,060.00 USD | 44,270.00 USD |
| `7D` | `10.39` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.41` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 259,620.00 USD | 45,690.00 USD | 90,040.00 USD |
| `7D` | `10.41` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD |
| `1D` | `10.43` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 248,090.00 USD | 62,710.00 USD | 71,990.00 USD |
| `7D` | `10.43` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.45` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 332,800.00 USD | 44,610.00 USD | 277,180.00 USD |
| `7D` | `10.45` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD |
| `1D` | `10.47` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 219,660.00 USD | 80,860.00 USD | 77,570.00 USD |
| `7D` | `10.47` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD |
| `1D` | `10.49` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 124,820.00 USD | 26,560.00 USD | 88,910.00 USD |
| `7D` | `10.49` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD |
| `1D` | `10.51` | 933,190.00 USD | 0.00 USD | 933,190.00 USD | 27,700.00 USD | 6,670.00 USD | 13,570.00 USD |
| `7D` | `10.51` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.53` | 885,260.00 USD | 0.00 USD | 885,260.00 USD | 43,880.00 USD | 39,730.00 USD | 117,580.00 USD |
| `7D` | `10.53` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD |
| `1D` | `10.55` | 684,070.00 USD | 0.00 USD | 684,070.00 USD | 7,160.00 USD | 517.73 USD | 56,280.00 USD |
| `7D` | `10.55` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD |
| `1D` | `10.57` | 620,110.00 USD | 0.00 USD | 620,110.00 USD | 52,260.00 USD | 287.00 USD | 114,300.00 USD |
| `7D` | `10.57` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD |
| `1D` | `10.59` | 453,270.00 USD | 0.00 USD | 453,270.00 USD | 48,700.00 USD | 615.80 USD | 172,420.00 USD |
| `7D` | `10.59` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD |
| `1D` | `10.61` | 231,530.00 USD | 0.00 USD | 231,530.00 USD | 231,310.00 USD | 17.90 USD | 210.16 USD |
| `7D` | `10.61` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD |
| `1D` | `10.62` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.63` | 301,170.00 USD | 301,170.00 USD | 0.00 USD | 301,120.00 USD | 0.00 USD | 51.48 USD |
| `7D` | `10.63` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD |
| `1D` | `10.65` | 301,820.00 USD | 301,820.00 USD | 0.00 USD | 644.06 USD | 0.00 USD | 0.40 USD |
| `7D` | `10.65` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD |
| `1D` | `10.67` | 301,830.00 USD | 301,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10.09 USD |
| `7D` | `10.67` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD |
| `1D` | `10.69` | 423,930.00 USD | 423,930.00 USD | 0.00 USD | 122,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.69` | 801,310.00 USD | 0.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD |
| `1D` | `10.71` | 646,780.00 USD | 646,780.00 USD | 0.00 USD | 219,090.00 USD | 25.97 USD | 3,730.00 USD |
| `7D` | `10.71` | 323,480.00 USD | 0.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD |
| `1D` | `10.73` | 656,610.00 USD | 656,610.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `10.73` | 29,560.00 USD | 29,560.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `7D` | `10.73` | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `1D` | `10.75` | 746,660.00 USD | 746,660.00 USD | 0.00 USD | 89,590.00 USD | 430.90 USD | 20.58 USD |
| `7D` | `10.75` | 77,290.00 USD | 77,290.00 USD | 0.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD |
| `1D` | `10.77` | 756,060.00 USD | 756,060.00 USD | 0.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `10.77` | 98,870.00 USD | 98,870.00 USD | 0.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD |
| `1D` | `10.79` | 929,710.00 USD | 929,710.00 USD | 0.00 USD | 88,000.00 USD | 85,640.00 USD | 0.00 USD |
| `7D` | `10.79` | 192,270.00 USD | 192,270.00 USD | 0.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD |
| `1D` | `10.81` | 992,460.00 USD | 992,460.00 USD | 0.00 USD | 0.00 USD | 62,760.00 USD | 0.00 USD |
| `1D` | `10.83` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 34,810.00 USD | 50,360.00 USD |
| `1D` | `10.85` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 75,750.00 USD | 26,640.00 USD | 0.00 USD |
| `1D` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD |
| `1D` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD |
| `1D` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD |
| `1D` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD |
| `1D` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD |
| `7D` | `10.95` | 227,860.00 USD | 227,860.00 USD | 0.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD |
| `1D` | `10.97` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 124.21 USD | 15,600.00 USD | 54,460.00 USD |
| `7D` | `10.97` | 240,550.00 USD | 240,550.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 413,570.00 USD | 413,570.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD |
| `1D` | `11.01` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 17,840.00 USD | 106,110.00 USD |
| `7D` | `11.01` | 424,150.00 USD | 424,150.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.03` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 15,920.00 USD | 145,940.00 USD |
| `7D` | `11.03` | 576,560.00 USD | 576,560.00 USD | 0.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.05` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 192,840.00 USD | 1,480.00 USD | 90,760.00 USD |
| `7D` | `11.05` | 966,150.00 USD | 966,150.00 USD | 0.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 473,120.00 USD | 32,310.00 USD | 78,770.00 USD |
| `7D` | `11.07` | 973,650.00 USD | 973,650.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.09` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 227,910.00 USD | 46,680.00 USD | 170,030.00 USD |
| `7D` | `11.09` | 981,150.00 USD | 981,150.00 USD | 0.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `11.11` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 216,430.00 USD | 37,650.00 USD | 15,640.00 USD |
| `7D` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD |
| `1D` | `11.13` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 408,510.00 USD | 91,630.00 USD | 167,890.00 USD |
| `7D` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD |
| `1D` | `11.15` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 194,240.00 USD | 11,710.00 USD | 0.00 USD |
| `7D` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD |
| `1D` | `11.17` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 165.70 USD | 69,930.00 USD | 58,890.00 USD |
| `7D` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD |
| `1D` | `11.19` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 72,110.00 USD | 63,920.00 USD | 27,230.00 USD |
| `7D` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD |
| `1D` | `11.21` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 114,530.00 USD | 425.43 USD | 116,470.00 USD |
| `7D` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD |
| `1D` | `11.23` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD |
| `7D` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD |
| `7D` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD |
| `1D` | `11.27` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD |
| `7D` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.29` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 165,410.00 USD | 123,030.00 USD | 213,620.00 USD |
| `7D` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD |
| `1D` | `11.31` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 63,250.00 USD | 67,150.00 USD | 79,800.00 USD |
| `7D` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 198,020.00 USD | 38,820.00 USD | 31,620.00 USD |
| `7D` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD |
| `1D` | `11.35` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 297,850.00 USD | 124,090.00 USD | 66,390.00 USD |
| `7D` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD |
| `1D` | `11.37` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 150,920.00 USD | 78,610.00 USD | 22,240.00 USD |
| `7D` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD |
| `1D` | `11.39` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD |
| `7D` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 95,030.00 USD | 34,780.00 USD | 140,440.00 USD |
| `7D` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.43` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 52,230.00 USD | 26,360.00 USD | 88,640.00 USD |
| `7D` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD |
| `1D` | `11.45` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 46,070.00 USD | 69,710.00 USD | 0.00 USD |
| `7D` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.47` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 48,370.00 USD | 19,590.00 USD | 23,420.00 USD |
| `7D` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 33,390.00 USD | 22,330.00 USD | 34,640.00 USD |
| `7D` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 41,360.00 USD | 28,330.00 USD | 30,920.00 USD |
| `7D` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD |
| `1D` | `11.53` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 32,640.00 USD | 16,860.00 USD | 29,710.00 USD |
| `7D` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD |
| `1D` | `11.55` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD |
| `7D` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD |
| `1D` | `11.57` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD |
| `7D` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.59` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 15,100.00 USD | 7,660.00 USD | 39,570.00 USD |
| `7D` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.61` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 153,200.00 USD | 0.00 USD | 71,370.00 USD |
| `7D` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.63` | 9,450,000.00 USD | 9,450,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD |
| `7D` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.65` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 1,410.00 USD | 7,130.00 USD | 46.76 USD |
| `7D` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD |
| `1D` | `11.67` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 6,370.00 USD | 0.00 USD |
| `7D` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.69` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 59,600.00 USD | 29,410.00 USD | 313.96 USD |
| `7D` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.71` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD |
| `7D` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 138,580.00 USD | 5,720.00 USD | 76,780.00 USD |
| `7D` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.75` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 21,990.00 USD | 35,620.00 USD | 61,350.00 USD |
| `7D` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.77` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 41,180.00 USD | 18,670.00 USD | 14,480.00 USD |
| `7D` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 12,080.00 USD | 755.20 USD | 40,180.00 USD |
| `7D` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.81` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 17,960.00 USD | 17,880.00 USD |
| `7D` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 11,070.00 USD | 11,510.00 USD | 29,320.00 USD |
| `7D` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.85` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 76,700.00 USD | 22,590.00 USD | 82,330.00 USD |
| `7D` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.87` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD |
| `7D` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.89` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 44,160.00 USD | 11,410.00 USD | 43,750.00 USD |
| `7D` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.91` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 102,960.00 USD | 18,340.00 USD | 31,710.00 USD |
| `7D` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.93` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 135,130.00 USD | 28,540.00 USD | 28,590.00 USD |
| `7D` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 85,850.00 USD | 21,080.00 USD | 41,560.00 USD |
| `7D` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.97` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD |
| `7D` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.99` | 11,550,000.00 USD | 11,550,000.00 USD | 0.00 USD | 123,700.00 USD | 25,870.00 USD | 46,860.00 USD |
| `7D` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.01` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 60,120.00 USD | 9,410.00 USD | 52,780.00 USD |
| `7D` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD |
| `1D` | `12.03` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD |
| `7D` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD |
| `1D` | `12.05` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 206,510.00 USD | 58,260.00 USD | 81,190.00 USD |
| `7D` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.07` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 114,130.00 USD | 53,190.00 USD | 97,550.00 USD |
| `7D` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.09` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 17,390.00 USD | 18,490.00 USD | 17,590.00 USD |
| `7D` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.11` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 94,540.00 USD | 34,950.00 USD | 55,330.00 USD |
| `7D` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.13` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 94,650.00 USD | 33,860.00 USD | 39,740.00 USD |
| `7D` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.15` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD |
| `7D` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.17` | 13,330,000.00 USD | 13,330,000.00 USD | 0.00 USD | 122,970.00 USD | 64,130.00 USD | 69,710.00 USD |
| `7D` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.19` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 64,080.00 USD | 24,200.00 USD | 12,250.00 USD |
| `7D` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD |
| `1D` | `12.21` | 13,560,000.00 USD | 13,560,000.00 USD | 0.00 USD | 52,950.00 USD | 28,750.00 USD | 50,920.00 USD |
| `7D` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD |
| `1D` | `12.23` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 14,580.00 USD | 24,000.00 USD | 4,690.00 USD |
| `7D` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.25` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 2,260.00 USD | 5,380.00 USD | 7,630.00 USD |
| `7D` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.27` | 13,700,000.00 USD | 13,700,000.00 USD | 0.00 USD | 52,420.00 USD | 9,580.00 USD | 22,930.00 USD |
| `7D` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.29` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 36,110.00 USD | 19,760.00 USD | 30,020.00 USD |
| `7D` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.31` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 19,750.00 USD | 4,850.00 USD | 9,840.00 USD |
| `7D` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.33` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD |
| `7D` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD |
| `1D` | `12.35` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD |
| `7D` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.37` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 8,820.00 USD | 5,700.00 USD | 3,140.00 USD |
| `7D` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD |
| `1D` | `12.39` | 13,950,000.00 USD | 13,950,000.00 USD | 0.00 USD | 28,430.00 USD | 12,560.00 USD | 21,540.00 USD |
| `7D` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD |
| `1D` | `12.41` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 42,540.00 USD | 19,990.00 USD | 23,470.00 USD |
| `7D` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.43` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 23,090.00 USD | 5,940.00 USD | 88.63 USD |
| `7D` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.45` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD |
| `7D` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.47` | 14,110,000.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 12,000.00 USD | 12,400.00 USD |
| `7D` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD |
| `7D` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD |
| `7D` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 0.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD |
| `7D` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD |
| `7D` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD |
| `7D` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 0.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD |
| `7D` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 0.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD |
| `7D` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 0.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD |
| `7D` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD |
| `7D` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 0.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD |
| `7D` | `12.67` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD |
| `7D` | `12.69` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD |
| `7D` | `12.71` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD |
| `7D` | `12.73` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD |
| `7D` | `12.75` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD |
| `7D` | `12.77` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD |
| `7D` | `12.79` | 20,470,000.00 USD | 20,470,000.00 USD | 0.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD |
| `7D` | `12.81` | 20,490,000.00 USD | 20,490,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD |
| `7D` | `12.83` | 20,520,000.00 USD | 20,520,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD |
| `7D` | `12.85` | 20,600,000.00 USD | 20,600,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,810.00 USD |
| `7D` | `12.87` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD |
| `7D` | `12.89` | 20,730,000.00 USD | 20,730,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD |
| `7D` | `12.91` | 20,840,000.00 USD | 20,840,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 39,080.00 USD |
| `7D` | `12.93` | 20,870,000.00 USD | 20,870,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD |
| `7D` | `12.95` | 20,890,000.00 USD | 20,890,000.00 USD | 0.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD |
| `7D` | `12.97` | 20,930,000.00 USD | 20,930,000.00 USD | 0.00 USD | 13,890.00 USD | 10,560.00 USD | 24,350.00 USD |
| `7D` | `12.99` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD |
| `7D` | `13.01` | 21,050,000.00 USD | 21,050,000.00 USD | 0.00 USD | 26,320.00 USD | 2,920.00 USD | 13,340.00 USD |
| `7D` | `13.03` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD |
| `7D` | `13.07` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 23,750.00 USD | 6,890.00 USD | 17,780.00 USD |
| `7D` | `13.09` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 16,060.00 USD | 527.72 USD | 7,600.00 USD |
| `7D` | `13.11` | 21,160,000.00 USD | 21,160,000.00 USD | 0.00 USD | 19,270.00 USD | 5,960.00 USD | 20.43 USD |
| `7D` | `13.13` | 21,180,000.00 USD | 21,180,000.00 USD | 0.00 USD | 13,360.00 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD |
| `7D` | `13.19` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 21,230,000.00 USD | 21,230,000.00 USD | 0.00 USD | 13,890.00 USD | 6,210.00 USD | 8,930.00 USD |
| `7D` | `13.23` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD |
| `7D` | `13.25` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD |
| `7D` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 0.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD |
| `7D` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD |
| `7D` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 0.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD |
| `7D` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 0.00 USD | 158.65 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `522.54M` | Total OI Tokens: `49,685,071.1 LINK`
  * 1h OI Change: `+0.66%` | 4h OI Change: `-0.05%` | 24h OI Change: `-5.02%`
  * Exchange Breakdown: Binance=`98.39M` | Bybit=`63.43M` | OKX=`25.20M` | Hyperliquid=`53.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.36K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0004%` | **USDT OKX** | `0.0023%` |
| **USDT Bybit** | `0.0084%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0002%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `45.26%` | `54.74%` | `0.83` | 83,940,000.00 USD |
| `15M` | `Binance` | `43.34%` | `56.66%` | `0.76` | 31,400,000.00 USD |
| `15M` | `OKX` | `47.17%` | `52.83%` | `0.89` | 15,860,000.00 USD |
| `15M` | `Bybit` | `49.69%` | `50.31%` | `0.99` | 6,200,000.00 USD |
| `15M` | `KuCoin` | `49.22%` | `50.78%` | `0.97` | 4,040,000.00 USD |
| `15M` | `Gate` | `51.16%` | `48.84%` | `1.05` | 4,750,000.00 USD |
| `15M` | `Bitget` | `51.96%` | `48.04%` | `1.08` | 3,500,000.00 USD |
| `15M` | `BingX` | `51.89%` | `48.11%` | `1.08` | 2,720,000.00 USD |
| `15M` | `MEXC` | `39.75%` | `60.25%` | `0.66` | 6,840,000.00 USD |
| `15M` | `Bitunix` | `29.46%` | `70.54%` | `0.42` | 3,430,000.00 USD |
| `15M` | `Hyperliquid` | `52.76%` | `47.24%` | `1.12` | 2,120,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.63%` | `43.37%` | `1.31` | 511,920.00 USD |
| `15M` | `Crypto.com` | `48.08%` | `51.92%` | `0.93` | 212,030.00 USD |
| `15M` | `WhiteBIT` | `22.38%` | `77.62%` | `0.29` | 1,020,000.00 USD |
| `15M` | `HTX` | `48.54%` | `51.46%` | `0.94` | 83,400.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `72.27%` | `27.73%` | `2.61` | 359,990.00 USD |
| `15M` | `Aster` | `40.54%` | `59.46%` | `0.68` | 473,800.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `51.03%` | `48.97%` | `1.04` | 413,470.00 USD |
| `15M` | `Whale Positions` | `43.34%` | `56.66%` | `0.76` | 31,400,000.00 USD |
| `15M` | `Global Accounts` | `45.26%` | `54.74%` | `0.83` | 83,940,000.00 USD |
| `1H` | `LINK` | `46.65%` | `53.35%` | `0.87` | 477,020,000.00 USD |
| `1H` | `Binance` | `46.36%` | `53.64%` | `0.86` | 166,710,000.00 USD |
| `1H` | `OKX` | `46.19%` | `53.81%` | `0.86` | 107,620,000.00 USD |
| `1H` | `Bybit` | `46.87%` | `53.13%` | `0.88` | 42,270,000.00 USD |
| `1H` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 11,990,000.00 USD |
| `1H` | `Gate` | `47.65%` | `52.35%` | `0.91` | 23,840,000.00 USD |
| `1H` | `Bitget` | `53.1%` | `46.9%` | `1.13` | 19,360,000.00 USD |
| `1H` | `BingX` | `49.95%` | `50.05%` | `1.00` | 12,350,000.00 USD |
| `1H` | `MEXC` | `40.45%` | `59.55%` | `0.68` | 37,780,000.00 USD |
| `1H` | `Bitunix` | `39.54%` | `60.46%` | `0.65` | 17,810,000.00 USD |
| `1H` | `Hyperliquid` | `56.69%` | `43.31%` | `1.31` | 18,400,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.95%` | `46.05%` | `1.17` | 5,820,000.00 USD |
| `1H` | `Crypto.com` | `50.86%` | `49.14%` | `1.04` | 1,250,000.00 USD |
| `1H` | `WhiteBIT` | `18.29%` | `81.71%` | `0.22` | 2,670,000.00 USD |
| `1H` | `HTX` | `61.42%` | `38.58%` | `1.59` | 1,130,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `61.52%` | `38.48%` | `1.60` | 1,970,000.00 USD |
| `1H` | `Aster` | `46.95%` | `53.05%` | `0.89` | 3,050,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.57%` | `47.43%` | `1.11` | 3,020,000.00 USD |
| `1H` | `Whale Positions` | `46.36%` | `53.64%` | `0.86` | 166,710,000.00 USD |
| `1H` | `Global Accounts` | `46.65%` | `53.35%` | `0.87` | 477,020,000.00 USD |
| `4H` | `LINK` | `48.12%` | `51.88%` | `0.93` | 935,510,000.00 USD |
| `4H` | `Binance` | `49.52%` | `50.48%` | `0.98` | 589,580,000.00 USD |
| `4H` | `OKX` | `49.39%` | `50.61%` | `0.98` | 70,660,000.00 USD |
| `4H` | `Bybit` | `42.06%` | `57.94%` | `0.73` | 77,010,000.00 USD |
| `4H` | `KuCoin` | `52.17%` | `47.83%` | `1.09` | 4,140,000.00 USD |
| `4H` | `Gate` | `46.69%` | `53.31%` | `0.88` | 19,620,000.00 USD |
| `4H` | `Bitget` | `48.71%` | `51.29%` | `0.95` | 15,930,000.00 USD |
| `4H` | `BingX` | `46.24%` | `53.76%` | `0.86` | 11,590,000.00 USD |
| `4H` | `MEXC` | `47.09%` | `52.91%` | `0.89` | 13,060,000.00 USD |
| `4H` | `Bitunix` | `51.71%` | `48.29%` | `1.07` | 22,240,000.00 USD |
| `4H` | `Hyperliquid` | `43.18%` | `56.82%` | `0.76` | 65,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.71%` | `50.29%` | `0.99` | 5,290,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.76%` | `87.24%` | `0.15` | 1,240,000.00 USD |
| `4H` | `HTX` | `46.78%` | `53.22%` | `0.88` | 2,270,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `68.42%` | `31.58%` | `2.17` | 4,630,000.00 USD |
| `4H` | `Aster` | `45.59%` | `54.41%` | `0.84` | 22,210,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `32.51%` | `67.49%` | `0.48` | 10,740,000.00 USD |
| `4H` | `Whale Positions` | `49.52%` | `50.48%` | `0.98` | 589,580,000.00 USD |
| `4H` | `Global Accounts` | `48.12%` | `51.88%` | `0.93` | 935,510,000.00 USD |


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
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -39,010.00 USD | -182,760.00 USD | **`DISTRIBUTION`** |
| `15m` | -317,230.00 USD | -230,400.00 USD | **`DISTRIBUTION`** |
| `30m` | -10,380.00 USD | 1,010,000.00 USD | **`ACCUMULATION`** |
| `1h` | 385,450.00 USD | 957,310.00 USD | **`ACCUMULATION`** |
| `2h` | 371,980.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,910,000.00 USD | -11,750,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -10,410,000.00 USD | -22,230,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,610,000.00 USD | -23,480,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,090,000.00 USD | -22,180,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,780,000.00 USD | -23,330,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -19,240,000.00 USD | -45,290,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,530,000.00 USD | -199,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-39.01K` | 15m=`-317.23K` | 1h=`+385.45K` | 24h=`-9.78M`
* Futures Capital Netflows: 5m=`-182.76K` | 15m=`-230.40K` | 1h=`+957.31K` | 24h=`-23.33M`
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
  * Execution Entry: `10.22` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `9.91` (Risk Distance: `0.3097` pts)
  * +2.5R Take Profit: `10.99`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.83` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.14` (Risk Distance: `0.3097` pts)
  * +2.5R Take Profit: `10.05`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.56`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
