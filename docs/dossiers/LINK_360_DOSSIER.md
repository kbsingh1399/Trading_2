# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 09:37:20 IST` (`2026-10-30 04:07:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.86` | **Live Ask Quote**: `10.95` | **Mid Price**: `10.91`
- **Spread Points**: `85.00` | **Spread BPS**: `77.94 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.91` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `10.98` | Lower -3.00σ Band: `10.83`
  * Upper +2.51σ Band: `10.97` | Lower -2.51σ Band: `10.85`
  * Upper +2.01σ Band: `10.95` | Lower -2.01σ Band: `10.86`
  * Upper +2.00σ Band: `10.95` | Lower -2.00σ Band: `10.86`
  * Upper +1.28σ Band: `10.94` | Lower -1.28σ Band: `10.87`
  * Upper +1.00σ Band: `10.93` | Lower -1.00σ Band: `10.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.91` | EMA-20=`10.91` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.91` (Slope: `+0.0000`) | EMA-100=`10.91`
  * Institutional Anchors: EMA-144=`10.91` | EMA-200=`10.91` (Slope: `+0.0000`) | EMA-233=`10.91`
- **Range Boundaries**: 24H High=`11.01` | 24H Low=`10.80` | Weekly High=`11.12` | Weekly Low=`10.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.86` (Distance: `+0.35%`)
  * Point of Control (POC) = `10.48` (Distance: `+4.00%`)
  * Value Area Low (VAL) = `10.35` (Distance: `+5.33%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.71` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`10.95` | Low=`10.86`
  * New York Session (13:00-21:00 UTC): High=`10.97` | Low=`10.84`
  * Initial Balance (First Hour): IB High=`10.94` | IB Low=`10.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.86` - `10.95`
  * Optimal Trade Entry (OTE 0.705): `10.93`
  * Structural Invalidation Anchor (0.786): `10.99`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.91` | `10.95` | `10.91` | `10.94` | `63,652` | 695,400.51 USD | 61,172.30 USD | `+8.80%` | -12,105,986.76 USD | `-0.27` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `10.94` | `10.97` | `10.93` | `10.97` | `69,446` | 760,720.96 USD | -927.36 USD | `-0.12%` | -12,106,914.12 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `10.97` | `10.97` | `10.97` | `10.97` | `352` | 3,858.35 USD | 3,858.35 USD | `+100.00%` | -12,103,055.77 USD | `-0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `10.75` | `10.81` | `10.73` | `10.80` | `154,882` | 1,669,099.58 USD | 54,637.51 USD | `+3.27%` | -12,753,062.74 USD | `+0.18` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `10.80` | `10.95` | `10.78` | `10.94` | `309,655` | 3,369,524.30 USD | 608,885.30 USD | `+18.07%` | -12,144,177.45 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `10.94` | `10.97` | `10.93` | `10.97` | `69,797` | 764,579.31 USD | 2,930.99 USD | `+0.38%` | -12,141,246.46 USD | `-0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `10.50` | `10.64` | `10.41` | `10.52` | `1,696,592` | 17,877,795.02 USD | -222,167.06 USD | `-1.24%` | -14,296,837.39 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `10.52` | `10.74` | `10.47` | `10.72` | `1,548,991` | 16,462,599.15 USD | 1,237,330.15 USD | `+7.52%` | -13,059,507.24 USD | `+0.86` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.72` | `10.97` | `10.71` | `10.97` | `700,980` | 7,595,010.26 USD | 918,260.79 USD | `+12.09%` | -12,141,246.46 USD | `+0.70` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.97` | `10.25` | `10.97` | `7,565,730` | 79,727,206.60 USD | 1,744,278.12 USD | `+2.19%` | -12,141,246.46 USD | `+0.67` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | 329,195.75 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,661,099.58 USD | `+1.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 631,714.40 USD | `-1.41` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,885,524.58 USD | `-1.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.97` | `10.25` | `10.97` | `7,565,730` | 79,727,206.60 USD | 1,744,278.12 USD | `+2.19%` | -12,141,246.46 USD | `+0.67` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`10.91`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `421` | `0xecb6...2b00` | `SHORT` | 5,192,579.85 USD | `475,728,800.00` | `10.66` | `10.92` | `64.29` | -121,951.97 USD | `-2.35%` | `10X Cross` |
| `511` | `0x73ce...8ce9` | `LONG` | 4,362,926.52 USD | `400,011,600.00` | `12.05` | `10.92` | `7.82` | -456,827.18 USD | `-10.47%` | `5X Cross` |
| `857` | `0xb83d...6e36` | `SHORT` | 2,639,635.79 USD | `242,013,000.00` | `12.93` | `10.92` | `551.90` | 490,258.40 USD | `+18.57%` | `3X Cross` |
| `903` | `0x458d...ab3b` | `LONG` | 2,480,669.29 USD | `227,156,700.00` | `13.13` | `10.92` | `9.34` | -501,561.11 USD | `-20.22%` | `3X Isolated` |
| `976` | `0xdd53...2b13` | `SHORT` | 2,253,264.95 USD | `206,475,300.00` | `11.92` | `10.92` | `307.66` | 207,957.98 USD | `+9.23%` | `3X Cross` |
| `1006` | `0x3dc9...54b0` | `SHORT` | 2,181,200.00 USD | `200,000,000.00` | `7.56` | `10.92` | `96.01` | -670,041.58 USD | `-30.72%` | `10X Cross` |
| `1019` | `0x45d2...4029` | `SHORT` | 2,132,709.50 USD | `195,500,000.00` | `11.54` | `10.92` | `222.18` | 123,773.93 USD | `+5.80%` | `10X Cross` |
| `1189` | `0x6540...f7b7` | `LONG` | 1,845,315.18 USD | `169,093,300.00` | `12.40` | `10.92` | `6.69` | -251,995.06 USD | `-13.66%` | `5X Isolated` |
| `1273` | `0xeadc...9d55` | `LONG` | 1,719,784.59 USD | `157,691,600.00` | `9.43` | `10.92` | `0.000000` | 233,129.69 USD | `+13.56%` | `10X Cross` |
| `1498` | `0x5b5d...c060` | `SHORT` | 1,437,143.60 USD | `131,775,500.00` | `13.61` | `10.92` | `1218.58` | 356,114.37 USD | `+24.78%` | `3X Cross` |
| `1673` | `0xf6f3...47f8` | `SHORT` | 1,254,228.24 USD | `115,024,600.00` | `11.42` | `10.92` | `19.51` | 59,101.95 USD | `+4.71%` | `5X Cross` |
| `1783` | `0x9df2...c665` | `SHORT` | 1,159,403.31 USD | `106,221,100.00` | `11.48` | `10.92` | `299.14` | 60,121.91 USD | `+5.19%` | `10X Cross` |
| `1855` | `0xfe7e...11b4` | `LONG` | 1,103,964.93 USD | `101,142,000.00` | `14.47` | `10.92` | `5.32` | -359,148.22 USD | `-32.53%` | `5X Isolated` |
| `1881` | `0x8af7...fa05` | `SHORT` | 1,076,887.00 USD | `98,661,200.00` | `14.08` | `10.92` | `203.30` | 312,295.54 USD | `+29.00%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.80` | 9,848.97 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 9.85K USD at 11.7980 USD [API] | `2026-10-28 23:32:10` |
| `ANNOUNCEMENT` | `INFO` | `11.80` | 6,665.87 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.7980 USD [API] | `2026-10-28 23:32:10` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 7,780.81 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.78K USD at 11.8070 USD [API] | `2026-10-29 00:34:16` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 12,848.38 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 12.85K USD at 11.8070 USD [API] | `2026-10-29 00:35:59` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 6,408.84 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.41K USD at 11.8070 USD [API] | `2026-10-29 00:35:59` |
| `ANNOUNCEMENT` | `INFO` | `11.78` | 7,539.20 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.54K USD at 11.7800 USD [API] | `2026-10-29 00:45:46` |
| `ANNOUNCEMENT` | `INFO` | `11.66` | 818.53 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.82K USD at 11.6600 USD [API] | `2026-09-18 03:10:57` |
| `ANNOUNCEMENT` | `INFO` | `11.66` | 145.75 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.15K USD at 11.6600 USD [API] | `2026-09-18 03:10:57` |
| `ANNOUNCEMENT` | `INFO` | `11.66` | 163.24 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.16K USD at 11.6600 USD [API] | `2026-09-18 03:10:57` |
| `ANNOUNCEMENT` | `INFO` | `11.66` | 621.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.62K USD at 11.6590 USD [API] | `2026-09-18 03:10:57` |
| `ANNOUNCEMENT` | `INFO` | `13.50` | 3,979.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 3.98K USD at 13.5000 USD [API] | `2026-09-07 05:38:09` |
| `ANNOUNCEMENT` | `INFO` | `13.50` | 70.20 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.07K USD at 13.5000 USD [API] | `2026-09-07 05:38:09` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 3,490.55 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 3.49K USD at 11.5390 USD [API] | `2026-08-21 07:27:50` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 1,385.83 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.39K USD at 11.5390 USD [API] | `2026-08-21 07:27:50` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 81.92 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.08K USD at 11.5380 USD [API] | `2026-08-21 07:27:50` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 811.05 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.81K USD at 11.5370 USD [API] | `2026-08-21 07:27:50` |
| `ANNOUNCEMENT` | `INFO` | `8.20` | 1,640.00 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.64K USD at 8.2000 USD [API] | `2026-07-29 20:02:06` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 9,412.14 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 9.41K USD at 11.7740 USD [API] | `2026-10-29 00:49:26` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,372.48 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.37K USD at 11.7740 USD [API] | `2026-10-29 00:49:26` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,470.48 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.7670 USD [API] | `2026-10-29 00:51:12` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,555.20 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.56K USD at 11.7670 USD [API] | `2026-10-29 00:52:25` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 12,274.06 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 12.27K USD at 12.7430 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 238.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.24K USD at 12.7430 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 1,682.21 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 1.68K USD at 12.7440 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 254.88 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.25K USD at 12.7440 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 21,691.99 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 21.69K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 8,369.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 8.37K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 58.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 58.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 58.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 58.63 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.74` | 432.06 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.43K USD at 12.7450 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 164.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.16K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 4,018.81 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 4.02K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 14,599.27 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 14.60K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 166.97 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.17K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `12.75` | 1,874.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 1.87K USD at 12.7460 USD [API] | `2026-10-12 21:47:08` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--5.87%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--5.88%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--5.88%`)
  * 7D Horizon: Short MP=`11.05` (Vol: 597,700.00 USD, Dist: `+0.97%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--5.87%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 3,060.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 11,150.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 74,520.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 21,560.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 735.08 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 1,040.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,770.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 549.99 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 811.85 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,270.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 3,450.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 10,680.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 4,980.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 1,090.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 1,070.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 7,030.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 3,080.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 802.34 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 9,200.00 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 237,650.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 56,570.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 2,370.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 2,220.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 111,070.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 542,610.00 USD | 10,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 27,550.00 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 97,760.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 17,530.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 7,080.00 USD | 10,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 5,970.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 37,790.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 26,860.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 26,950.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 65,590.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 9,260.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,160,000.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 12,460.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 51,630.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 2,690.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 30,340.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 10,840.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 7,450.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 8,670.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 20,710.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 5,660.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 11,940.00 USD | 8,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,180,000.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 175,130.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 64,760.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 37,390.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 44,520.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 93,840.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 33,960.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 16,100.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 355,910.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 22,760.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 58,400.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 451,200.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 94,680.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,590.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 23,340.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.45` | 4,750,000.00 USD | 4,750,000.00 USD | 9,040.00 USD | 2,740.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 55,850.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.47` | 4,730,000.00 USD | 4,730,000.00 USD | 1,820.00 USD | 1,380.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.53` | 4,730,000.00 USD | 4,730,000.00 USD | 80.78 USD | 7,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.55` | 4,720,000.00 USD | 4,720,000.00 USD | 6,860.00 USD | 8,690.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 52,890.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.65` | 197,970.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.75` | 74,090.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `9.85` | 82,120.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 4,160,000.00 USD | 4,160,000.00 USD | 9,950.00 USD | 288.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 4,140,000.00 USD | 4,140,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 4,110,000.00 USD | 4,110,000.00 USD | 13,840.00 USD | 5,580.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 4,090,000.00 USD | 4,090,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 440,220.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 4,060,000.00 USD | 4,060,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 4,030,000.00 USD | 4,030,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 4,030,000.00 USD | 4,030,000.00 USD | 1,230.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 4,030,000.00 USD | 4,030,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 792,160.00 USD | 882,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 4,020,000.00 USD | 4,020,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 4,010,000.00 USD | 4,010,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 4,000,000.00 USD | 4,000,000.00 USD | 9,270.00 USD | 104.05 USD | 62.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 61,700.00 USD | 90,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `10.25` | 27,350.00 USD | 28,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `10.45` | 990.66 USD | 990.66 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `10.55` | 803.91 USD | 803.91 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `10.65` | 1,740.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `10.77` | 756,060.00 USD | 756,060.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.77` | 98,870.00 USD | 98,870.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.79` | 929,710.00 USD | 929,710.00 USD | 88,000.00 USD | 85,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.79` | 192,270.00 USD | 192,270.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.81` | 992,460.00 USD | 992,460.00 USD | 0.00 USD | 62,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.83` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 34,810.00 USD | 50,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.85` | 1,180,000.00 USD | 1,180,000.00 USD | 75,750.00 USD | 26,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.85` | 1,870.00 USD | 4,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.87` | 1,670,000.00 USD | 1,670,000.00 USD | 201,960.00 USD | 25,470.00 USD | 259,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.89` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 35,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.91` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 11,350.00 USD | 71,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.93` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,910,000.00 USD | 1,910,000.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `11.15` | 5,830.00 USD | 10,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.25` | 3,180.00 USD | 13,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.35` | 269.00 USD | 13,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 13,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.55` | 143.22 USD | 14,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `11.85` | 494.15 USD | 14,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.15` | 1,270.00 USD | 15,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 17,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.35` | 1,650.00 USD | 18,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.55` | 380.27 USD | 19,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 19,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 19,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `13.25` | 1,870.00 USD | 21,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.27` | 21,340,000.00 USD | 21,340,000.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 21,350,000.00 USD | 21,350,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 21,370,000.00 USD | 21,370,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 21,380,000.00 USD | 21,380,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.35` | 21,380,000.00 USD | 21,380,000.00 USD | 0.00 USD | 158.65 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 27,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 203.25 USD | 27,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 344.56 USD | 27,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 28,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.55` | 582.00 USD | 28,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 54,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.05` | 153.51 USD | 54,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 54,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 158.07 USD | 55,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 55,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 55,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 226.10 USD | 55,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 57,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,190.00 USD | 71,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 91,200.00 USD | 162,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 17,830.00 USD | 180,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 260,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 12,330.00 USD | 272,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 27,720.00 USD | 300,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,080.00 USD | 551,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 553,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 5,610.00 USD | 558,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 691,980.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 4,620.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 309.59 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 29,160.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 231.19 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.35` | 75,370.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 820,330.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 44,610.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 2,280,000.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 637.59 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.65` | 3,560.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.95` | 213.69 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.15` | 124.79 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,100,000.00 USD | 0.00 USD | 2,960.00 USD | `-79.46%` | `1,313,700.00` |
| `Live` | `Long` | `2.35` | 12,090,000.00 USD | 0.00 USD | 2,350.00 USD | `-78.54%` | `1,000,000.00` |
| `Live` | `Long` | `2.45` | 12,090,000.00 USD | 0.00 USD | 1,110.00 USD | `-77.63%` | `452,300.00` |
| `Live` | `Long` | `2.55` | 12,090,000.00 USD | 0.00 USD | 1,550.00 USD | `-76.72%` | `606,600.00` |
| `Live` | `Long` | `2.65` | 12,090,000.00 USD | 0.00 USD | 2,550.00 USD | `-75.81%` | `961,300.00` |
| `Live` | `Long` | `2.75` | 12,090,000.00 USD | 0.00 USD | 260.15 USD | `-74.89%` | `94,600.00` |
| `Live` | `Long` | `3.05` | 12,090,000.00 USD | 0.00 USD | 7,300.00 USD | `-72.15%` | `2,394,200.00` |
| `Live` | `Long` | `3.15` | 12,080,000.00 USD | 0.00 USD | 297.99 USD | `-71.24%` | `94,600.00` |
| `Live` | `Long` | `3.35` | 12,080,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.41%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,080,000.00 USD | 0.00 USD | 1,450.00 USD | `-68.50%` | `421,000.00` |
| `Live` | `Long` | `3.55` | 12,080,000.00 USD | 0.00 USD | 19,960.00 USD | `-67.59%` | `5,622,000.00` |
| `Live` | `Long` | `3.65` | 12,060,000.00 USD | 0.00 USD | 4,770.00 USD | `-66.68%` | `1,307,000.00` |
| `Live` | `Long` | `3.85` | 12,050,000.00 USD | 0.00 USD | 250.25 USD | `-64.85%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,050,000.00 USD | 0.00 USD | 4,420.00 USD | `-63.94%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,050,000.00 USD | 0.00 USD | 6,480.00 USD | `-63.02%` | `1,601,100.00` |
| `Live` | `Long` | `4.15` | 12,040,000.00 USD | 0.00 USD | 45,660.00 USD | `-62.11%` | `11,003,200.00` |
| `Live` | `Long` | `4.25` | 11,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-61.20%` | `1,198,100.00` |
| `Live` | `Long` | `4.35` | 11,990,000.00 USD | 0.00 USD | 595.08 USD | `-60.28%` | `136,800.00` |
| `Live` | `Long` | `4.45` | 11,990,000.00 USD | 0.00 USD | 381.37 USD | `-59.37%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 11,990,000.00 USD | 0.00 USD | 7,300.00 USD | `-58.46%` | `1,604,500.00` |
| `Live` | `Long` | `4.65` | 11,980,000.00 USD | 0.00 USD | 48,700.00 USD | `-57.55%` | `10,473,800.00` |
| `Live` | `Long` | `4.75` | 11,930,000.00 USD | 0.00 USD | 233,170.00 USD | `-56.63%` | `49,088,200.00` |
| `Live` | `Long` | `4.85` | 11,700,000.00 USD | 0.00 USD | 6,530.00 USD | `-55.72%` | `1,346,600.00` |
| `Live` | `Long` | `4.95` | 11,690,000.00 USD | 0.00 USD | 2,060.00 USD | `-54.81%` | `416,200.00` |
| `Live` | `Long` | `5.05` | 11,690,000.00 USD | 0.00 USD | 4,620.00 USD | `-53.89%` | `914,400.00` |
| `Live` | `Long` | `5.15` | 11,690,000.00 USD | 0.00 USD | 89,580.00 USD | `-52.98%` | `17,393,500.00` |
| `Live` | `Long` | `5.25` | 11,600,000.00 USD | 0.00 USD | 3,730.00 USD | `-52.07%` | `711,000.00` |
| `Live` | `Long` | `5.35` | 11,590,000.00 USD | 0.00 USD | 545,540.00 USD | `-51.15%` | `101,970,200.00` |
| `Live` | `Long` | `5.45` | 11,050,000.00 USD | 0.00 USD | 138.97 USD | `-50.24%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 11,050,000.00 USD | 0.00 USD | 41,970.00 USD | `-49.33%` | `7,562,900.00` |
| `Live` | `Long` | `5.65` | 11,000,000.00 USD | 0.00 USD | 35,770.00 USD | `-48.42%` | `6,330,200.00` |
| `Live` | `Long` | `5.75` | 10,970,000.00 USD | 0.00 USD | 276.57 USD | `-47.50%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 10,970,000.00 USD | 0.00 USD | 1,700.00 USD | `-46.59%` | `290,500.00` |
| `Live` | `Long` | `5.95` | 10,970,000.00 USD | 0.00 USD | 5,380.00 USD | `-45.68%` | `903,400.00` |
| `Live` | `Long` | `6.05` | 10,960,000.00 USD | 0.00 USD | 21,070.00 USD | `-44.76%` | `3,482,800.00` |
| `Live` | `Long` | `6.15` | 10,940,000.00 USD | 0.00 USD | 6,990.00 USD | `-43.85%` | `1,136,400.00` |
| `Live` | `Long` | `6.25` | 10,930,000.00 USD | 0.00 USD | 40,180.00 USD | `-42.94%` | `6,429,000.00` |
| `Live` | `Long` | `6.35` | 10,890,000.00 USD | 0.00 USD | 56,480.00 USD | `-42.03%` | `8,895,000.00` |
| `Live` | `Long` | `6.45` | 10,840,000.00 USD | 0.00 USD | 15,730.00 USD | `-41.11%` | `2,439,300.00` |
| `Live` | `Long` | `6.55` | 10,820,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.20%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 10,820,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-39.29%` | `171,172,800.00` |
| `Live` | `Long` | `6.75` | 9,680,000.00 USD | 0.00 USD | 12,630.00 USD | `-38.37%` | `1,870,900.00` |
| `Live` | `Long` | `6.85` | 9,670,000.00 USD | 0.00 USD | 29,030.00 USD | `-37.46%` | `4,238,400.00` |
| `Live` | `Long` | `6.95` | 9,640,000.00 USD | 0.00 USD | 61,990.00 USD | `-36.55%` | `8,919,300.00` |
| `Live` | `Long` | `7.05` | 9,580,000.00 USD | 0.00 USD | 689,480.00 USD | `-35.63%` | `97,799,200.00` |
| `Live` | `Long` | `7.15` | 8,890,000.00 USD | 0.00 USD | 34,590.00 USD | `-34.72%` | `4,837,400.00` |
| `Live` | `Long` | `7.25` | 8,850,000.00 USD | 0.00 USD | 57,480.00 USD | `-33.81%` | `7,927,800.00` |
| `Live` | `Long` | `7.35` | 8,790,000.00 USD | 0.00 USD | 18,570.00 USD | `-32.90%` | `2,526,400.00` |
| `Live` | `Long` | `7.45` | 8,780,000.00 USD | 0.00 USD | 8,530.00 USD | `-31.98%` | `1,145,600.00` |
| `Live` | `Long` | `7.55` | 8,770,000.00 USD | 0.00 USD | 25,580.00 USD | `-31.07%` | `3,388,500.00` |
| `Live` | `Long` | `7.65` | 8,740,000.00 USD | 0.00 USD | 155,020.00 USD | `-30.16%` | `20,264,400.00` |
| `Live` | `Long` | `7.75` | 8,590,000.00 USD | 0.00 USD | 631.62 USD | `-29.24%` | `81,500.00` |
| `Live` | `Long` | `7.85` | 8,590,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.33%` | `400,939,100.00` |
| `Live` | `Long` | `7.95` | 5,440,000.00 USD | 0.00 USD | 16,960.00 USD | `-27.42%` | `2,133,900.00` |
| `Live` | `Long` | `8.05` | 5,420,000.00 USD | 0.00 USD | 118,610.00 USD | `-26.50%` | `14,733,800.00` |
| `Live` | `Long` | `8.15` | 5,300,000.00 USD | 0.00 USD | 39,090.00 USD | `-25.59%` | `4,795,900.00` |
| `Live` | `Long` | `8.25` | 5,260,000.00 USD | 0.00 USD | 34,340.00 USD | `-24.68%` | `4,162,900.00` |
| `Live` | `Long` | `8.35` | 5,230,000.00 USD | 0.00 USD | 28,950.00 USD | `-23.77%` | `3,466,900.00` |
| `Live` | `Long` | `8.45` | 5,200,000.00 USD | 0.00 USD | 12,500.00 USD | `-22.85%` | `1,478,800.00` |
| `Live` | `Long` | `8.55` | 5,190,000.00 USD | 0.00 USD | 15,820.00 USD | `-21.94%` | `1,849,800.00` |
| `Live` | `Long` | `8.65` | 5,170,000.00 USD | 0.00 USD | 356,160.00 USD | `-21.03%` | `41,174,900.00` |
| `Live` | `Long` | `8.75` | 4,820,000.00 USD | 0.00 USD | 28,630.00 USD | `-20.11%` | `3,271,900.00` |
| `Live` | `Long` | `8.85` | 4,790,000.00 USD | 0.00 USD | 61,500.00 USD | `-19.20%` | `6,949,200.00` |
| `Live` | `Long` | `8.95` | 4,730,000.00 USD | 0.00 USD | 460,150.00 USD | `-18.29%` | `51,413,900.00` |
| `Live` | `Long` | `9.05` | 4,270,000.00 USD | 0.00 USD | 87,450.00 USD | `-17.37%` | `9,662,700.00` |
| `Live` | `Long` | `9.15` | 4,180,000.00 USD | 0.00 USD | 76,340.00 USD | `-16.46%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,100,000.00 USD | 0.00 USD | 17,690.00 USD | `-15.55%` | `1,912,100.00` |
| `Live` | `Long` | `9.35` | 4,080,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-14.64%` | `229,680,600.00` |
| `Live` | `Long` | `9.45` | 1,940,000.00 USD | 0.00 USD | 46,880.00 USD | `-13.72%` | `4,961,100.00` |
| `Live` | `Long` | `9.55` | 1,890,000.00 USD | 0.00 USD | 54,080.00 USD | `-12.81%` | `5,663,000.00` |
| `Live` | `Long` | `9.65` | 1,840,000.00 USD | 0.00 USD | 202,600.00 USD | `-11.90%` | `20,995,300.00` |
| `Live` | `Long` | `9.75` | 1,630,000.00 USD | 0.00 USD | 73,650.00 USD | `-10.98%` | `7,553,700.00` |
| `Live` | `Long` | `9.85` | 1,560,000.00 USD | 0.00 USD | 81,980.00 USD | `-10.07%` | `8,322,900.00` |
| `Live` | `Long` | `9.95` | 1,480,000.00 USD | 0.00 USD | 440,220.00 USD | `-9.16%` | `44,243,500.00` |
| `Live` | `Long` | `10.05` | 1,040,000.00 USD | 0.00 USD | 788,850.00 USD | `-8.24%` | `78,492,700.00` |
| `Live` | `Long` | `10.15` | 248,800.00 USD | 0.00 USD | 69,150.00 USD | `-7.33%` | `6,813,000.00` |
| `Live` | `Long` | `10.25` | 179,650.00 USD | 0.00 USD | 41,320.00 USD | `-6.42%` | `4,031,700.00` |
| `Live` | `Long` | `10.35` | 138,320.00 USD | 0.00 USD | 138,320.00 USD | `-5.51%` | `13,364,500.00` |
| `Live` | `Short` | `11.05` | 3,750.00 USD | 3,750.00 USD | 0.00 USD | `+0.89%` | `339,500.00` |
| `Live` | `Short` | `11.15` | 6,720.00 USD | 2,970.00 USD | 0.00 USD | `+1.80%` | `266,300.00` |
| `Live` | `Short` | `11.45` | 6,970.00 USD | 249.61 USD | 0.00 USD | `+4.54%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 11,770.00 USD | 4,800.00 USD | 0.00 USD | `+5.45%` | `415,600.00` |
| `Live` | `Short` | `11.65` | 35,540.00 USD | 23,770.00 USD | 0.00 USD | `+6.36%` | `2,040,400.00` |
| `Live` | `Short` | `11.95` | 35,750.00 USD | 205.54 USD | 0.00 USD | `+9.10%` | `17,200.00` |
| `Live` | `Short` | `12.15` | 37,020.00 USD | 1,270.00 USD | 0.00 USD | `+10.93%` | `104,700.00` |
| `Live` | `Short` | `12.25` | 38,450.00 USD | 1,430.00 USD | 0.00 USD | `+11.84%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 39,190.00 USD | 736.06 USD | 0.00 USD | `+12.75%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 39,700.00 USD | 519.16 USD | 0.00 USD | `+13.67%` | `41,700.00` |
| `Live` | `Short` | `12.55` | 41,020.00 USD | 1,310.00 USD | 0.00 USD | `+14.58%` | `104,500.00` |
| `Live` | `Short` | `12.65` | 41,450.00 USD | 435.16 USD | 0.00 USD | `+15.49%` | `34,400.00` |
| `Live` | `Short` | `13.45` | 46,880.00 USD | 5,430.00 USD | 0.00 USD | `+22.80%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 139,780.00 USD | 92,890.00 USD | 0.00 USD | `+23.71%` | `6,855,700.00` |
| `Live` | `Short` | `14.15` | 140,130.00 USD | 349.51 USD | 0.00 USD | `+29.19%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 140,670.00 USD | 544.35 USD | 0.00 USD | `+30.10%` | `38,200.00` |
| `Live` | `Short` | `14.95` | 166,000.00 USD | 25,330.00 USD | 0.00 USD | `+36.49%` | `1,694,600.00` |
| `Live` | `Short` | `15.25` | 166,160.00 USD | 155.55 USD | 0.00 USD | `+39.23%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 166,740.00 USD | 578.46 USD | 0.00 USD | `+41.97%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 167,010.00 USD | 271.04 USD | 0.00 USD | `+44.71%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 167,150.00 USD | 138.76 USD | 0.00 USD | `+45.62%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 168,540.00 USD | 1,390.00 USD | 0.00 USD | `+49.27%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 168,770.00 USD | 230.30 USD | 0.00 USD | `+50.19%` | `14,000.00` |
| `Live` | `Short` | `16.55` | 200,480.00 USD | 31,700.00 USD | 0.00 USD | `+51.10%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 291,680.00 USD | 91,200.00 USD | 0.00 USD | `+52.93%` | `5,445,000.00` |
| `Live` | `Short` | `16.85` | 307,440.00 USD | 15,760.00 USD | 0.00 USD | `+53.84%` | `935,400.00` |
| `Live` | `Short` | `16.95` | 387,210.00 USD | 79,770.00 USD | 0.00 USD | `+54.75%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 388,580.00 USD | 1,370.00 USD | 0.00 USD | `+56.58%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 415,280.00 USD | 26,700.00 USD | 0.00 USD | `+58.40%` | `1,539,000.00` |
| `Live` | `Short` | `17.75` | 420,770.00 USD | 5,480.00 USD | 0.00 USD | `+62.06%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 421,020.00 USD | 249.90 USD | 0.00 USD | `+62.97%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 672,210.00 USD | 251,200.00 USD | 0.00 USD | `+63.88%` | `13,994,200.00` |
| `Live` | `Short` | `18.05` | 674,900.00 USD | 2,690.00 USD | 0.00 USD | `+64.80%` | `149,000.00` |
| `Live` | `Short` | `18.25` | 702,700.00 USD | 27,790.00 USD | 0.00 USD | `+66.62%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 706,590.00 USD | 3,890.00 USD | 0.00 USD | `+68.45%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,410,000.00 USD | 699,710.00 USD | 0.00 USD | `+69.36%` | `37,720,000.00` |
| `Live` | `Short` | `18.65` | 1,410,000.00 USD | 186.50 USD | 0.00 USD | `+70.27%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 1,480,000.00 USD | 75,870.00 USD | 0.00 USD | `+72.10%` | `4,024,800.00` |
| `Live` | `Short` | `19.35` | 3,710,000.00 USD | 2,230,000.00 USD | 0.00 USD | `+76.66%` | `115,024,600.00` |
| `Live` | `Short` | `19.55` | 3,710,000.00 USD | 316.71 USD | 0.00 USD | `+78.49%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,750,000.00 USD | 38,790.00 USD | 0.00 USD | `+79.40%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,750,000.00 USD | 359.45 USD | 0.00 USD | `+80.32%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 3,750,000.00 USD | 289.81 USD | 0.00 USD | `+81.23%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,750,000.00 USD | 637.59 USD | 0.00 USD | `+83.05%` | `31,800.00` |
| `Live` | `Short` | `20.15` | 3,750,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.97%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,750,000.00 USD | 1,770.00 USD | 0.00 USD | `+86.71%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,760,000.00 USD | 7,250.00 USD | 0.00 USD | `+87.62%` | `353,000.00` |
| `Live` | `Short` | `20.65` | 3,760,000.00 USD | 185.85 USD | 0.00 USD | `+88.53%` | `9,000.00` |
| `Live` | `Short` | `21.25` | 3,760,000.00 USD | 3,670.00 USD | 0.00 USD | `+94.01%` | `172,500.00` |
| `Live` | `Short` | `21.75` | 3,760,000.00 USD | 119.62 USD | 0.00 USD | `+98.58%` | `5,500.00` |
| `Live` | `Short` | `21.95` | 3,760,000.00 USD | 223.89 USD | 0.00 USD | `+100.40%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 403,300.00 USD | 0.00 USD | 182.03 USD | `-77.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 403,120.00 USD | 0.00 USD | 209.48 USD | `-71.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 402,910.00 USD | 0.00 USD | 431.68 USD | `-67.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 402,480.00 USD | 0.00 USD | 290.29 USD | `-58.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 402,190.00 USD | 0.00 USD | 120.22 USD | `-52.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 402,070.00 USD | 0.00 USD | 251.68 USD | `-44.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 401,820.00 USD | 0.00 USD | 749.30 USD | `-42.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 401,070.00 USD | 0.00 USD | 186.41 USD | `-41.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 400,880.00 USD | 0.00 USD | 3,760.00 USD | `-40.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 397,120.00 USD | 0.00 USD | 133.00 USD | `-39.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 396,980.00 USD | 0.00 USD | 1,320.00 USD | `-36.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 395,670.00 USD | 0.00 USD | 3,770.00 USD | `-35.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 391,900.00 USD | 0.00 USD | 2,070.00 USD | `-33.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 389,830.00 USD | 0.00 USD | 3,740.00 USD | `-31.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 386,080.00 USD | 0.00 USD | 1,050.00 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 385,030.00 USD | 0.00 USD | 120.90 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 384,910.00 USD | 0.00 USD | 146.80 USD | `-28.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 384,760.00 USD | 0.00 USD | 124.02 USD | `-27.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 384,640.00 USD | 0.00 USD | 5,000.00 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 379,640.00 USD | 0.00 USD | 393.64 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 379,240.00 USD | 0.00 USD | 10,560.00 USD | `-24.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 368,680.00 USD | 0.00 USD | 3,110.00 USD | `-23.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 365,570.00 USD | 0.00 USD | 1,480.00 USD | `-22.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 364,090.00 USD | 0.00 USD | 52,990.00 USD | `-21.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 311,110.00 USD | 0.00 USD | 186.84 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 310,920.00 USD | 0.00 USD | 742.88 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 310,180.00 USD | 0.00 USD | 902.70 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 309,280.00 USD | 0.00 USD | 1,570.00 USD | `-18.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 307,710.00 USD | 0.00 USD | 3,340.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 304,370.00 USD | 0.00 USD | 194.90 USD | `-16.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 304,180.00 USD | 0.00 USD | 232.18 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 303,940.00 USD | 0.00 USD | 7,060.00 USD | `-14.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 296,890.00 USD | 0.00 USD | 2,310.00 USD | `-13.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 294,580.00 USD | 0.00 USD | 19,460.00 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 275,120.00 USD | 0.00 USD | 686.12 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 274,430.00 USD | 0.00 USD | 409.50 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 274,020.00 USD | 0.00 USD | 24,850.00 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 249,170.00 USD | 0.00 USD | 13,710.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 235,460.00 USD | 0.00 USD | 42,800.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 192,660.00 USD | 0.00 USD | 51,860.00 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 140,800.00 USD | 0.00 USD | 111,500.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 29,300.00 USD | 0.00 USD | 245.30 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 29,060.00 USD | 0.00 USD | 1,310.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 27,740.00 USD | 0.00 USD | 11,130.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 16,610.00 USD | 0.00 USD | 4,200.00 USD | `-2.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 12,410.00 USD | 0.00 USD | 413.88 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 11,990.00 USD | 0.00 USD | 5,430.00 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 6,570.00 USD | 0.00 USD | 6,570.00 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 77,760.00 USD | 77,760.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 103,570.00 USD | 25,810.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 118,110.00 USD | 14,540.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 124,270.00 USD | 6,170.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 124,670.00 USD | 396.17 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 162,860.00 USD | 38,190.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 165,100.00 USD | 2,250.00 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 165,850.00 USD | 746.12 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 166,100.00 USD | 253.59 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 169,900.00 USD | 3,790.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 197,870.00 USD | 27,980.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 199,690.00 USD | 1,820.00 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 209,290.00 USD | 9,590.00 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 209,880.00 USD | 597.74 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 214,780.00 USD | 4,890.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 271,560.00 USD | 56,780.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 277,730.00 USD | 6,180.00 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 278,410.00 USD | 679.57 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 298,780.00 USD | 20,360.00 USD | 0.00 USD | `+17.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 299,230.00 USD | 451.95 USD | 0.00 USD | `+18.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 315,860.00 USD | 16,630.00 USD | 0.00 USD | `+19.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 316,780.00 USD | 919.19 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 318,100.00 USD | 1,320.00 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 325,880.00 USD | 7,790.00 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 328,420.00 USD | 2,540.00 USD | 0.00 USD | `+22.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 328,580.00 USD | 165.31 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 329,540.00 USD | 954.14 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 349,090.00 USD | 19,550.00 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 353,970.00 USD | 4,880.00 USD | 0.00 USD | `+26.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 354,240.00 USD | 266.44 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 370,500.00 USD | 16,260.00 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 370,650.00 USD | 152.82 USD | 0.00 USD | `+29.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 374,930.00 USD | 4,280.00 USD | 0.00 USD | `+30.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 378,340.00 USD | 3,410.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 397,780.00 USD | 19,440.00 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 398,000.00 USD | 218.25 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 400,520.00 USD | 2,520.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 407,790.00 USD | 7,270.00 USD | 0.00 USD | `+34.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 408,740.00 USD | 950.82 USD | 0.00 USD | `+36.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 433,590.00 USD | 24,860.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 436,040.00 USD | 2,450.00 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 669,080.00 USD | 233,040.00 USD | 0.00 USD | `+39.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 670,000.00 USD | 924.07 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 670,900.00 USD | 893.01 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 671,550.00 USD | 653.10 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 672,020.00 USD | 472.63 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 675,320.00 USD | 3,290.00 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 678,490.00 USD | 3,170.00 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 683,620.00 USD | 5,130.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 698,700.00 USD | 15,080.00 USD | 0.00 USD | `+46.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 705,500.00 USD | 6,800.00 USD | 0.00 USD | `+47.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 712,000.00 USD | 6,500.00 USD | 0.00 USD | `+48.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 718,540.00 USD | 6,540.00 USD | 0.00 USD | `+49.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 725,120.00 USD | 6,580.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 735,050.00 USD | 9,930.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 839,030.00 USD | 103,980.00 USD | 0.00 USD | `+52.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 853,270.00 USD | 14,240.00 USD | 0.00 USD | `+52.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 937,620.00 USD | 84,360.00 USD | 0.00 USD | `+53.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 939,320.00 USD | 1,700.00 USD | 0.00 USD | `+54.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 946,680.00 USD | 7,370.00 USD | 0.00 USD | `+55.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 963,370.00 USD | 16,690.00 USD | 0.00 USD | `+56.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 965,680.00 USD | 2,300.00 USD | 0.00 USD | `+57.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 967,410.00 USD | 1,740.00 USD | 0.00 USD | `+58.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 989,100.00 USD | 21,690.00 USD | 0.00 USD | `+59.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 993,490.00 USD | 4,390.00 USD | 0.00 USD | `+60.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 997,900.00 USD | 4,410.00 USD | 0.00 USD | `+61.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,000,000.00 USD | 4,440.00 USD | 0.00 USD | `+62.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,010,000.00 USD | 4,460.00 USD | 0.00 USD | `+62.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,010,000.00 USD | 448.75 USD | 0.00 USD | `+63.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,040,000.00 USD | 30,960.00 USD | 0.00 USD | `+64.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,040,000.00 USD | 453.75 USD | 0.00 USD | `+65.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,040,000.00 USD | 456.25 USD | 0.00 USD | `+66.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,040,000.00 USD | 458.75 USD | 0.00 USD | `+67.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,040,000.00 USD | 461.25 USD | 0.00 USD | `+68.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,040,000.00 USD | 4,540.00 USD | 0.00 USD | `+69.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,050,000.00 USD | 466.25 USD | 0.00 USD | `+70.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,050,000.00 USD | 468.75 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,050,000.00 USD | 471.25 USD | 0.00 USD | `+72.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,050,000.00 USD | 473.75 USD | 0.00 USD | `+73.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,110,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,110,000.00 USD | 574.50 USD | 0.00 USD | `+74.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,110,000.00 USD | 577.50 USD | 0.00 USD | `+75.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,120,000.00 USD | 2,710.00 USD | 0.00 USD | `+76.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,120,000.00 USD | 972.50 USD | 0.00 USD | `+77.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,130,000.00 USD | 7,680.00 USD | 0.00 USD | `+78.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,130,000.00 USD | 786.00 USD | 0.00 USD | `+79.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,130,000.00 USD | 790.00 USD | 0.00 USD | `+80.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,130,000.00 USD | 992.50 USD | 0.00 USD | `+81.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,130,000.00 USD | 997.50 USD | 0.00 USD | `+82.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,730,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+83.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,730,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,730,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,740,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,740,000.00 USD | 1,020.00 USD | 0.00 USD | `+86.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,740,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,740,000.00 USD | 1,030.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,740,000.00 USD | 1,040.00 USD | 0.00 USD | `+89.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,740,000.00 USD | 1,410.00 USD | 0.00 USD | `+90.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,740,000.00 USD | 1,050.00 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,750,000.00 USD | 4,000.00 USD | 0.00 USD | `+92.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,750,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,750,000.00 USD | 1,060.00 USD | 0.00 USD | `+94.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,800,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+94.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,800,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,800,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,800,000.00 USD | 1,080.00 USD | 0.00 USD | `+97.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,800,000.00 USD | 1,090.00 USD | 0.00 USD | `+98.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,800,000.00 USD | 3,280.00 USD | 0.00 USD | `+99.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,800,000.00 USD | 1,100.00 USD | 0.00 USD | `+100.40%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `513.75M` | Total OI Tokens: `47,093,807.2 LINK`
  * 1h OI Change: `-4.88%` | 4h OI Change: `-3.36%` | 24h OI Change: `-6.31%`
  * Exchange Breakdown: Binance=`101.74M` | Bybit=`69.99M` | OKX=`26.16M` | Hyperliquid=`55.20M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-10.29K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0054%` | **USDT OKX** | `-0.0026%` |
| **USDT Bybit** | `-0.0235%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0055%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `43.78%` | `56.22%` | `0.78` | 15,740,000.00 USD |
| `15M` | `Binance` | `40.46%` | `59.54%` | `0.68` | 7,410,000.00 USD |
| `15M` | `OKX` | `40.34%` | `59.66%` | `0.68` | 3,020,000.00 USD |
| `15M` | `Bybit` | `59.74%` | `40.26%` | `1.48` | 1,260,000.00 USD |
| `15M` | `KuCoin` | `73.46%` | `26.54%` | `2.77` | 38,360.00 USD |
| `15M` | `Gate` | `49.23%` | `50.77%` | `0.97` | 1,940,000.00 USD |
| `15M` | `Bitget` | `33.16%` | `66.84%` | `0.50` | 199,010.00 USD |
| `15M` | `BingX` | `24.81%` | `75.19%` | `0.33` | 298,160.00 USD |
| `15M` | `MEXC` | `62.04%` | `37.96%` | `1.63` | 666,160.00 USD |
| `15M` | `Bitunix` | `41.68%` | `58.32%` | `0.71` | 443,860.00 USD |
| `15M` | `Hyperliquid` | `76.21%` | `23.79%` | `3.20` | 78,160.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.88%` | `55.12%` | `0.81` | 51,700.00 USD |
| `15M` | `Crypto.com` | `33.08%` | `66.92%` | `0.49` | 29,330.00 USD |
| `15M` | `WhiteBIT` | `17.47%` | `82.53%` | `0.21` | 115,240.00 USD |
| `15M` | `HTX` | `39.58%` | `60.42%` | `0.66` | 70,470.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `51.72%` | `48.28%` | `1.07` | 119,670.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `5.87%` | `94.13%` | `0.06` | 4,820.00 USD |
| `15M` | `Whale Positions` | `40.46%` | `59.54%` | `0.68` | 7,410,000.00 USD |
| `15M` | `Global Accounts` | `43.78%` | `56.22%` | `0.78` | 15,740,000.00 USD |
| `1H` | `LINK` | `48.04%` | `51.96%` | `0.92` | 21,460,000.00 USD |
| `1H` | `Binance` | `50.1%` | `49.9%` | `1.00` | 8,030,000.00 USD |
| `1H` | `OKX` | `50.5%` | `49.5%` | `1.02` | 2,160,000.00 USD |
| `1H` | `Bybit` | `47.26%` | `52.74%` | `0.90` | 2,390,000.00 USD |
| `1H` | `KuCoin` | `51.71%` | `48.29%` | `1.07` | 154,730.00 USD |
| `1H` | `Gate` | `50.97%` | `49.03%` | `1.04` | 379,710.00 USD |
| `1H` | `Bitget` | `54.61%` | `45.39%` | `1.20` | 1,040,000.00 USD |
| `1H` | `BingX` | `49.22%` | `50.78%` | `0.97` | 1,000,000.00 USD |
| `1H` | `MEXC` | `33.97%` | `66.03%` | `0.51` | 1,040,000.00 USD |
| `1H` | `Bitunix` | `43.57%` | `56.43%` | `0.77` | 593,580.00 USD |
| `1H` | `Hyperliquid` | `65.8%` | `34.2%` | `1.92` | 128,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.2%` | `50.8%` | `0.97` | 3,960,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.62%` | `94.38%` | `0.06` | 175,720.00 USD |
| `1H` | `HTX` | `36.89%` | `63.11%` | `0.58` | 147,390.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.12%` | `99.88%` | `0.00` | 300.32 USD |
| `1H` | `Aster` | `9.28%` | `90.72%` | `0.10` | 225,730.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.54%` | `84.46%` | `0.18` | 48,860.00 USD |
| `1H` | `Whale Positions` | `50.1%` | `49.9%` | `1.00` | 8,030,000.00 USD |
| `1H` | `Global Accounts` | `48.04%` | `51.96%` | `0.92` | 21,460,000.00 USD |
| `4H` | `LINK` | `49.50%` | `50.50%` | `0.98` | 213,160,000.00 USD |
| `4H` | `Binance` | `50.19%` | `49.81%` | `1.01` | 78,380,000.00 USD |
| `4H` | `OKX` | `49.69%` | `50.31%` | `0.99` | 19,860,000.00 USD |
| `4H` | `Bybit` | `47.05%` | `52.95%` | `0.89` | 26,970,000.00 USD |
| `4H` | `KuCoin` | `47.34%` | `52.66%` | `0.90` | 1,810,000.00 USD |
| `4H` | `Gate` | `59.13%` | `40.87%` | `1.45` | 7,560,000.00 USD |
| `4H` | `Bitget` | `49.28%` | `50.72%` | `0.97` | 9,250,000.00 USD |
| `4H` | `BingX` | `49.64%` | `50.36%` | `0.99` | 7,960,000.00 USD |
| `4H` | `MEXC` | `47.42%` | `52.58%` | `0.90` | 11,740,000.00 USD |
| `4H` | `Bitunix` | `44.12%` | `55.88%` | `0.79` | 6,050,000.00 USD |
| `4H` | `Hyperliquid` | `54.07%` | `45.93%` | `1.18` | 2,330,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.15%` | `49.85%` | `1.01` | 37,790,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `17.84%` | `82.16%` | `0.22` | 831,700.00 USD |
| `4H` | `HTX` | `50.31%` | `49.69%` | `1.01` | 898,450.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `50.77%` | `49.23%` | `1.03` | 1,020,000.00 USD |
| `4H` | `Aster` | `30.81%` | `69.19%` | `0.45` | 570,960.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.78%` | `76.22%` | `0.31` | 146,340.00 USD |
| `4H` | `Whale Positions` | `50.19%` | `49.81%` | `1.01` | 78,380,000.00 USD |
| `4H` | `Global Accounts` | `49.50%` | `50.50%` | `0.98` | 213,160,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `10.49` | `10.50` | `10.49` | `10.54` | `10.47` | 2,418,538.29 USD | 1,213,398.88 USD | 1,205,139.41 USD | 8,259.48 USD | `+0.34%` | `5B / 7S` |
| `0:00 UTC` | `10.49` | `10.51` | `10.49` | `10.58` | `10.47` | 4,555,787.03 USD | 1,937,641.47 USD | 2,618,145.56 USD | -680,504.09 USD | `-14.94%` | `34B / 12S` |
| `5:00 UTC` | `10.66` | `10.66` | `10.66` | `10.72` | `10.57` | 8,088,225.29 USD | 5,081,569.93 USD | 3,006,655.36 USD | 2,074,914.56 USD | `+25.65%` | `34B / 2S` |
| `0:00 UTC` | `10.72` | `10.71` | `10.72` | `10.74` | `10.66` | 2,303,326.18 USD | 1,025,885.42 USD | 1,277,440.76 USD | -251,555.33 USD | `-10.92%` | `6B / 12S` |
| `5:00 UTC` | `10.70` | `10.70` | `10.70` | `10.73` | `10.67` | 1,515,260.65 USD | 804,867.83 USD | 710,392.82 USD | 94,475.01 USD | `+6.23%` | `8B / 5S` |
| `0:00 UTC` | `10.77` | `10.75` | `10.77` | `10.78` | `10.71` | 1,791,807.07 USD | 1,021,807.03 USD | 770,000.04 USD | 251,806.99 USD | `+14.05%` | `17B / 3S` |
| `5:00 UTC` | `10.80` | `10.78` | `10.80` | `10.81` | `10.74` | 1,669,099.58 USD | 861,868.55 USD | 807,231.03 USD | 54,637.51 USD | `+3.27%` | `11B / 7S` |
| `0:00 UTC` | `10.91` | `10.88` | `10.91` | `10.95` | `10.78` | 3,369,524.30 USD | 1,989,204.80 USD | 1,380,319.50 USD | 608,885.30 USD | `+18.07%` | `47B / 26S` |
| `5:00 UTC` | `10.94` | `10.95` | `10.94` | `10.98` | `10.93` | 1,915,931.41 USD | 933,547.46 USD | 982,383.95 USD | -48,836.49 USD | `-2.55%` | `2B / 6S` |
| `0:00 UTC` | `10.96` | `10.95` | `10.96` | `10.96` | `10.95` | 26,566.60 USD | 12,300.99 USD | 14,265.61 USD | -1,964.62 USD | `-7.40%` | `3B / 5S` |

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
| `5m` | -106,060.00 USD | -11,980.00 USD | **`DISTRIBUTION`** |
| `15m` | -157,480.00 USD | 11,320.00 USD | **`DISTRIBUTION`** |
| `30m` | 10,350.00 USD | 582,730.00 USD | **`ACCUMULATION`** |
| `1h` | 99,450.00 USD | 1,120,000.00 USD | **`ACCUMULATION`** |
| `2h` | -8,980.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `4h` | 237,310.00 USD | 393,820.00 USD | **`ACCUMULATION`** |
| `6h` | -5,230,000.00 USD | -10,040,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,490,000.00 USD | -19,560,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -11,380,000.00 USD | -23,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -9,950,000.00 USD | -19,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,090,000.00 USD | -44,340,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,270,000.00 USD | -197,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-106.06K` | 15m=`-157.48K` | 1h=`+99.45K` | 24h=`-9.95M`
* Futures Capital Netflows: 5m=`-11.98K` | 15m=`+11.32K` | 1h=`+1.12M` | 24h=`-19.88M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `9.02` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `13.67`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.86` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.19` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `7.55`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
