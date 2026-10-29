# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 04:38:02 IST` (`2026-10-29 23:08:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.60` | **Live Ask Quote**: `10.68` | **Mid Price**: `10.64`
- **Spread Points**: `84.00` | **Spread BPS**: `78.93 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.43` | VWAP Z-Score: `-2.45` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1350` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `21.02` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.33` | Lower -3.00σ Band: `10.53`
  * Upper +2.51σ Band: `12.18` | Lower -2.51σ Band: `10.67`
  * Upper +2.01σ Band: `12.03` | Lower -2.01σ Band: `10.82`
  * Upper +2.00σ Band: `12.03` | Lower -2.00σ Band: `10.83`
  * Upper +1.28σ Band: `11.81` | Lower -1.28σ Band: `11.04`
  * Upper +1.00σ Band: `11.73` | Lower -1.00σ Band: `11.13`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.94` | EMA-20=`11.17` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.39` (Slope: `+0.0000`) | EMA-100=`11.47`
  * Institutional Anchors: EMA-144=`11.48` | EMA-200=`11.48` (Slope: `-0.5026`) | EMA-233=`11.47`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.66` | Weekly High=`11.96` | Weekly Low=`10.66`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.16` (Distance: `-4.56%`)
  * Point of Control (POC) = `10.81` (Distance: `-1.51%`)
  * Value Area Low (VAL) = `10.80` (Distance: `-1.43%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.64` | Weekly POC=`11.42` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.59`
  * London Session (08:00-16:00 UTC): High=`10.68` | Low=`10.60`
  * New York Session (13:00-21:00 UTC): High=`10.71` | Low=`10.58`
  * Initial Balance (First Hour): IB High=`10.67` | IB Low=`10.61`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.60` - `10.68`
  * Optimal Trade Entry (OTE 0.705): `10.66`
  * Structural Invalidation Anchor (0.786): `10.73`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.73` | `10.77` | `10.71` | `10.75` | `322,181` | 3,459,877.19 USD | 561,796.83 USD | `+16.24%` | -16,415,057.55 USD | `+1.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `10.75` | `10.75` | `10.66` | `10.67` | `247,496` | 2,648,889.55 USD | -535,489.42 USD | `-20.22%` | -16,950,546.97 USD | `-0.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.67` | `10.68` | `10.64` | `10.66` | `44,685` | 476,249.28 USD | -42,495.95 USD | `-8.92%` | -16,993,042.93 USD | `+0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.90` | `10.97` | `10.79` | `10.82` | `2,392,375` | 25,964,116.59 USD | -6,116,164.13 USD | `-23.56%` | -16,561,823.18 USD | `-3.72` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `10.82` | `10.84` | `10.71` | `10.75` | `1,006,324` | 10,836,187.71 USD | 145,199.30 USD | `+1.34%` | -16,416,623.88 USD | `+0.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `10.75` | `10.75` | `10.64` | `10.66` | `292,324` | 3,126,671.23 USD | -576,752.87 USD | `-18.45%` | -16,993,376.75 USD | `+0.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `10.99` | `11.29` | `10.95` | `11.05` | `1,981,647` | 22,042,313.47 USD | -1,846,592.95 USD | `-8.38%` | -7,835,044.70 USD | `-1.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.06` | `10.71` | `10.75` | `4,861,262` | 52,776,566.13 USD | -8,723,123.08 USD | `-16.53%` | -16,558,167.77 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `10.75` | `10.75` | `10.64` | `10.66` | `295,898` | 3,164,777.21 USD | -548,387.29 USD | `-17.33%` | -17,106,555.06 USD | `+0.09` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.64` | `10.66` | `10,944,274` | 120,657,347.22 USD | -15,388,057.46 USD | `-12.75%` | -17,106,555.06 USD | `-2.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.64` | `10.66` | `10,944,274` | 120,657,347.22 USD | -15,388,057.46 USD | `-12.75%` | -17,106,555.06 USD | `-2.19` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.64`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `509` | `0x73ce...8ce9` | `LONG` | 4,292,924.49 USD | `400,011,600.00` | `12.05` | `10.73` | `9.12` | -526,829.21 USD | `-12.27%` | `5X Cross` |
| `862` | `0xb83d...6e36` | `SHORT` | 2,597,283.52 USD | `242,013,000.00` | `12.93` | `10.73` | `613.05` | 532,610.67 USD | `+20.51%` | `3X Cross` |
| `923` | `0x458d...ab3b` | `LONG` | 2,437,164.23 USD | `227,156,700.00` | `13.13` | `10.73` | `9.34` | -545,066.16 USD | `-22.36%` | `3X Isolated` |
| `1000` | `0xdd53...2b13` | `SHORT` | 2,217,544.72 USD | `206,475,300.00` | `11.92` | `10.73` | `306.90` | 243,678.21 USD | `+10.99%` | `3X Cross` |
| `1027` | `0x3dc9...54b0` | `SHORT` | 2,145,600.00 USD | `200,000,000.00` | `7.56` | `10.73` | `93.99` | -634,441.58 USD | `-29.57%` | `10X Cross` |
| `1046` | `0x45d2...4029` | `SHORT` | 2,098,497.00 USD | `195,500,000.00` | `11.54` | `10.73` | `219.26` | 157,986.43 USD | `+7.53%` | `10X Cross` |
| `1251` | `0x6540...f7b7` | `LONG` | 1,782,431.44 USD | `166,000,600.00` | `12.45` | `10.73` | `7.43` | -284,266.83 USD | `-15.95%` | `5X Isolated` |
| `1303` | `0xeadc...9d55` | `LONG` | 1,691,084.72 USD | `157,691,600.00` | `9.43` | `10.73` | `0.000000` | 204,429.82 USD | `+12.09%` | `10X Cross` |
| `1544` | `0x5b5d...c060` | `SHORT` | 1,413,160.46 USD | `131,775,500.00` | `13.61` | `10.73` | `1311.31` | 380,097.51 USD | `+26.90%` | `3X Cross` |
| `1706` | `0xf6f3...47f8` | `SHORT` | 1,233,983.91 USD | `115,024,600.00` | `11.42` | `10.73` | `20.49` | 79,346.28 USD | `+6.43%` | `5X Cross` |
| `1731` | `0x9df2...c665` | `SHORT` | 1,207,816.84 USD | `112,543,500.00` | `11.48` | `10.73` | `290.31` | 84,510.62 USD | `+7.00%` | `10X Cross` |
| `1877` | `0xfe7e...11b4` | `LONG` | 1,085,658.23 USD | `101,142,000.00` | `14.47` | `10.73` | `5.33` | -377,454.92 USD | `-34.77%` | `5X Isolated` |
| `1892` | `0xecb6...2b00` | `SHORT` | 1,069,803.61 USD | `99,711,400.00` | `10.75` | `10.73` | `292.64` | 2,193.77 USD | `+0.21%` | `10X Cross` |
| `1903` | `0x8af7...fa05` | `SHORT` | 1,059,621.29 USD | `98,661,200.00` | `14.08` | `10.73` | `205.62` | 329,561.25 USD | `+31.10%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.49` | 5,051.98 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.05K USD at 11.4870 USD [API] | `2026-10-28 17:16:52` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 6,901.90 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.90K USD at 11.5320 USD [API] | `2026-10-28 17:59:13` |
| `ANNOUNCEMENT` | `INFO` | `11.53` | 5,026.21 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.03K USD at 11.5280 USD [API] | `2026-10-28 18:00:56` |
| `ANNOUNCEMENT` | `INFO` | `11.62` | 6,665.82 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6190 USD [API] | `2026-10-28 18:30:48` |
| `ANNOUNCEMENT` | `INFO` | `11.70` | 5,466.71 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.6960 USD [API] | `2026-10-28 18:36:16` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 17,715.57 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 17.72K USD at 11.7120 USD [API] | `2026-10-28 18:37:37` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 3,041.12 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 3.04K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 189.55 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.19K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 4,661.79 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 4.66K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 400.43 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.40K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 253.53 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.25K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 99.51 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.10K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 1,529.45 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.53K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 178.89 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.18K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 106.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.11K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 377.92 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.38K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 18.96 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.02K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 1,550.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.55K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 106.61 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.11K USD at 11.8460 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 338.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.34K USD at 11.8460 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 639.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.64K USD at 11.8460 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 23.69 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.02K USD at 11.8460 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 614.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.61K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 106.61 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.11K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 338.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.34K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 1,529.19 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.53K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 106.60 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.11K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,468.37 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 5.47K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,706.44 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 5.71K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.87` | 16,523.65 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 16.52K USD at 11.8730 USD [API] | `2026-10-28 20:12:42` |
| `ANNOUNCEMENT` | `INFO` | `11.87` | 5,117.26 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.12K USD at 11.8730 USD [API] | `2026-10-28 20:12:41` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 7,505.19 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |
| `ANNOUNCEMENT` | `INFO` | `11.77` | 5,466.45 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.47K USD at 11.7710 USD [API] | `2026-10-28 20:20:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.06` (Vol: 500,800.00 USD, Dist: `+2.64%`) | Long MP=`10.62` (Vol: 500,800.00 USD, Dist: `--1.46%`)
  * 48H Horizon: Short MP=`11.12` (Vol: 340,300.00 USD, Dist: `+3.26%`) | Long MP=`10.68` (Vol: 299,800.00 USD, Dist: `--0.88%`)
  * 3D Horizon: Short MP=`11.12` (Vol: 343,900.00 USD, Dist: `+3.26%`) | Long MP=`10.68` (Vol: 306,900.00 USD, Dist: `--0.88%`)
  * 7D Horizon: Short MP=`11.12` (Vol: 349,600.00 USD, Dist: `+3.24%`) | Long MP=`10.69` (Vol: 349,600.00 USD, Dist: `--0.77%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.15` | 3,150.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,850.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 25,070.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,550.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 9,610.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,640.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 297.99 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 2,990.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 796.30 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 10,470.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 4,710.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 713.79 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 40,120.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 251.91 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 11,890.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 1,490.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 4,190.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 237,160.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,620.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 9,450.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 266.26 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 886.73 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 16,490.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 2,750.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,720.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 102,400.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 20,170.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 5,690.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 68,200.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 6,240.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 88,130.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 15,990.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 16,300.00 USD | 11,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 11,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 3,350.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 71,320.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 810.37 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 2,560.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 42,950.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 10,500.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 33,870.00 USD | 11,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 6,280.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 17,880.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 52,770.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 14,300.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 1,300,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 13,390.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 65,630.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 193,680.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 42,600.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 12,890.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 14,470.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 17,800.00 USD | 9,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 19,940.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 308,140.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,570.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 457,490.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 66,460.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,770,000.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 5,600.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,160,000.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 33,630.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 14,810.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.57` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 6,330,000.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.60` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 6,320,000.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.64` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 105.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 6,300,000.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 10,670.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.66` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 4,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.67` | 6,290,000.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.68` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 6,290,000.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.70` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.72` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 14,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.74` | 5,650,000.00 USD | 5,650,000.00 USD | 709.80 USD | 0.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 6,220,000.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 156,790.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.76` | 5,640,000.00 USD | 5,640,000.00 USD | 96,370.00 USD | 689.80 USD | 13,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.77` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.78` | 5,530,000.00 USD | 5,530,000.00 USD | 55,890.00 USD | 7,220.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 6,110,000.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.80` | 5,440,000.00 USD | 5,440,000.00 USD | 37,210.00 USD | 3,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 6,060,000.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.82` | 5,400,000.00 USD | 5,400,000.00 USD | 77,230.00 USD | 14,710.00 USD | 20,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 5,960,000.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.84` | 5,290,000.00 USD | 5,290,000.00 USD | 11,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 5,910,000.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 118,790.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 5,280,000.00 USD | 5,280,000.00 USD | 9,950.00 USD | 463.70 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 5,260,000.00 USD | 5,260,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 5,230,000.00 USD | 5,230,000.00 USD | 13,840.00 USD | 11,040.00 USD | 44.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 5,210,000.00 USD | 5,210,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 829,740.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 5,210,000.00 USD | 5,210,000.00 USD | 7,630.00 USD | 11,250.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 6,740.00 USD | 12,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 254.10 USD | 357.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 5,150,000.00 USD | 5,150,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 660,920.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 91.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 73.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 5,140,000.00 USD | 5,140,000.00 USD | 7,570.00 USD | 0.00 USD | 147.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 5,130,000.00 USD | 5,130,000.00 USD | 1,150.00 USD | 7,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 16,120.00 USD | 797,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 5,130,000.00 USD | 5,130,000.00 USD | 7,170.00 USD | 0.00 USD | 21.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 5,640,000.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 5,120,000.00 USD | 5,120,000.00 USD | 2,920.00 USD | 29.65 USD | 593.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 5,540,000.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 5,490,000.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 5,110,000.00 USD | 5,110,000.00 USD | 536.32 USD | 4,320.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 5,380,000.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 5,090,000.00 USD | 5,090,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 5,080,000.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 35,850.00 USD | 781,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 5,030,000.00 USD | 5,030,000.00 USD | 13,990.00 USD | 2,830.00 USD | 109.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 4,960,000.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 5,010,000.00 USD | 5,010,000.00 USD | 29,240.00 USD | 9,320.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 4,780,000.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 4,960,000.00 USD | 4,960,000.00 USD | 9,060.00 USD | 11,600.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 4,690,000.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 4,930,000.00 USD | 4,930,000.00 USD | 28,010.00 USD | 19,910.00 USD | 82,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 4,490,000.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 4,800,000.00 USD | 4,800,000.00 USD | 32,410.00 USD | 4,260.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 4,290,000.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 6,390.00 USD | 745,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 4,750,000.00 USD | 4,750,000.00 USD | 8,260.00 USD | 3,450.00 USD | 71,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 4,220,000.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 4,670,000.00 USD | 4,670,000.00 USD | 7,450.00 USD | 4,400.00 USD | 80,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 4,100,000.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 4,580,000.00 USD | 4,580,000.00 USD | 109,640.00 USD | 8,470.00 USD | 41,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 4,030,000.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 4,420,000.00 USD | 4,420,000.00 USD | 237,840.00 USD | 20,290.00 USD | 46,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 3,690,000.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 4,110,000.00 USD | 4,110,000.00 USD | 141,180.00 USD | 30,800.00 USD | 36,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 3,620,000.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 16,050.00 USD | 738,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 3,900,000.00 USD | 3,900,000.00 USD | 221,310.00 USD | 49,390.00 USD | 46,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 3,320,000.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 3,590,000.00 USD | 3,590,000.00 USD | 124,220.00 USD | 10,980.00 USD | 46,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 3,010,000.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 3,400,000.00 USD | 3,400,000.00 USD | 79,100.00 USD | 15,300.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 2,820,000.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 3,300,000.00 USD | 3,300,000.00 USD | 65,390.00 USD | 25,650.00 USD | 38,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 2,730,000.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 3,170,000.00 USD | 3,170,000.00 USD | 740.06 USD | 16,650.00 USD | 147,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 2,660,000.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 439,980.00 USD | 722,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,010,000.00 USD | 3,010,000.00 USD | 58,790.00 USD | 23,780.00 USD | 81,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 2,400,000.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 2,840,000.00 USD | 2,840,000.00 USD | 48,460.00 USD | 30,610.00 USD | 129,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 2,250,000.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 2,630,000.00 USD | 2,630,000.00 USD | 15,270.00 USD | 7,950.00 USD | 77,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 2,000,000.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 2,530,000.00 USD | 2,530,000.00 USD | 516,250.00 USD | 27,900.00 USD | 117,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 1,460,000.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 1,870,000.00 USD | 1,870,000.00 USD | 292,600.00 USD | 69,030.00 USD | 148,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 1,360,000.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 156,990.00 USD | 282,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 1,360,000.00 USD | 1,360,000.00 USD | 122,590.00 USD | 17,330.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 1,290,000.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 1,180,000.00 USD | 1,180,000.00 USD | 441,140.00 USD | 94,900.00 USD | 80,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 801,310.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 559,250.00 USD | 559,250.00 USD | 241,770.00 USD | 22,060.00 USD | 78,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 323,480.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 216,540.00 USD | 216,540.00 USD | 112,490.00 USD | 12,290.00 USD | 7,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 29,560.00 USD | 29,560.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 59,120.00 USD | 59,120.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 84,430.00 USD | 84,430.00 USD | 84,420.00 USD | 0.00 USD | 14.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.75` | 77,290.00 USD | 77,290.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 38,850.00 USD | 125,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.76` | 16,890.00 USD | 16,890.00 USD | 12,370.00 USD | 4,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.77` | 98,870.00 USD | 98,870.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.78` | 160,720.00 USD | 160,720.00 USD | 86,290.00 USD | 57,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.79` | 192,270.00 USD | 192,270.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.80` | 218,290.00 USD | 218,290.00 USD | 2,390.00 USD | 55,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 86,340.00 USD | 87,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.94` | 239,890.00 USD | 239,890.00 USD | 454.50 USD | 21,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 677.80 USD | 677.80 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.96` | 358,240.00 USD | 358,240.00 USD | 877.67 USD | 29,730.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.97` | 240,550.00 USD | 240,550.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.98` | 414,180.00 USD | 414,180.00 USD | 1,470.00 USD | 0.00 USD | 54,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 413,570.00 USD | 413,570.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.00` | 493,550.00 USD | 493,550.00 USD | 0.00 USD | 0.00 USD | 79,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 424,150.00 USD | 424,150.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.02` | 591,980.00 USD | 591,980.00 USD | 0.00 USD | 0.00 USD | 98,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 576,560.00 USD | 576,560.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.04` | 666,230.00 USD | 666,230.00 USD | 0.00 USD | 0.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 966,150.00 USD | 966,150.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.05` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.06` | 1,210,000.00 USD | 1,210,000.00 USD | 475,540.00 USD | 3,450.00 USD | 65,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 973,650.00 USD | 973,650.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.08` | 1,660,000.00 USD | 1,660,000.00 USD | 279,470.00 USD | 49,490.00 USD | 119,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 981,150.00 USD | 981,150.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 1,740,000.00 USD | 1,740,000.00 USD | 77,170.00 USD | 1,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 2,330,000.00 USD | 2,330,000.00 USD | 424,370.00 USD | 92,530.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 2,630,000.00 USD | 2,630,000.00 USD | 212,890.00 USD | 12,460.00 USD | 67,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 2,780,000.00 USD | 2,780,000.00 USD | 104,910.00 USD | 50,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 3,000,000.00 USD | 3,000,000.00 USD | 71,610.00 USD | 55,530.00 USD | 86,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 3,130,000.00 USD | 3,130,000.00 USD | 42,500.00 USD | 39,440.00 USD | 47,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 3,480,000.00 USD | 3,480,000.00 USD | 262,060.00 USD | 587.72 USD | 96,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 3,790,000.00 USD | 3,790,000.00 USD | 90,500.00 USD | 28,030.00 USD | 190,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 2,420.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.26` | 4,030,000.00 USD | 4,030,000.00 USD | 125,040.00 USD | 11,690.00 USD | 103,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 4,620,000.00 USD | 4,620,000.00 USD | 279,810.00 USD | 56,750.00 USD | 248,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 4,860,000.00 USD | 4,860,000.00 USD | 63,460.00 USD | 78,590.00 USD | 100,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 5,110,000.00 USD | 5,110,000.00 USD | 101,830.00 USD | 66,860.00 USD | 83,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 5,650,000.00 USD | 5,650,000.00 USD | 397,010.00 USD | 101,070.00 USD | 40,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 5,920,000.00 USD | 5,920,000.00 USD | 108,490.00 USD | 99,470.00 USD | 56,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 6,080,000.00 USD | 6,080,000.00 USD | 106,580.00 USD | 61,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 6,250,000.00 USD | 6,250,000.00 USD | 35,800.00 USD | 24,370.00 USD | 104,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 6,480,000.00 USD | 6,480,000.00 USD | 108,320.00 USD | 45,350.00 USD | 78,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 6,590,000.00 USD | 6,590,000.00 USD | 42,610.00 USD | 18,500.00 USD | 53,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.46` | 6,730,000.00 USD | 6,730,000.00 USD | 49,150.00 USD | 65,340.00 USD | 23,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 6,760,000.00 USD | 6,760,000.00 USD | 14,310.00 USD | 10,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,870,000.00 USD | 6,870,000.00 USD | 31,090.00 USD | 33,490.00 USD | 45,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,930,000.00 USD | 6,930,000.00 USD | 29,340.00 USD | 13,740.00 USD | 19,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 7,020,000.00 USD | 7,020,000.00 USD | 33,710.00 USD | 16,150.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.56` | 7,100,000.00 USD | 7,100,000.00 USD | 65,320.00 USD | 635.25 USD | 15,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 7,170,000.00 USD | 7,170,000.00 USD | 46,550.00 USD | 335.85 USD | 17,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 7,370,000.00 USD | 7,370,000.00 USD | 124,870.00 USD | 7,320.00 USD | 67,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 7,440,000.00 USD | 7,440,000.00 USD | 43,430.00 USD | 0.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 7,460,000.00 USD | 7,460,000.00 USD | 2,920.00 USD | 0.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 5,600.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,550,000.00 USD | 7,550,000.00 USD | 59,600.00 USD | 28,810.00 USD | 79.66 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 150.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,810,000.00 USD | 7,810,000.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,930,000.00 USD | 7,930,000.00 USD | 35,580.00 USD | 17,540.00 USD | 73,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 62,000.00 USD | 72,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,980,000.00 USD | 7,980,000.00 USD | 24,330.00 USD | 14,970.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 8,070,000.00 USD | 8,070,000.00 USD | 27,290.00 USD | 18,740.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 18,370.00 USD | 79.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 8,140,000.00 USD | 8,140,000.00 USD | 11,070.00 USD | 0.00 USD | 36,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 8,280,000.00 USD | 8,280,000.00 USD | 76,470.00 USD | 11,830.00 USD | 55,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,370,000.00 USD | 8,370,000.00 USD | 232.40 USD | 33,990.00 USD | 53,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,470,000.00 USD | 8,470,000.00 USD | 19,640.00 USD | 25,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,550,000.00 USD | 8,550,000.00 USD | 44,870.00 USD | 8,750.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,830,000.00 USD | 8,830,000.00 USD | 230,070.00 USD | 23,160.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,940,000.00 USD | 8,940,000.00 USD | 49,250.00 USD | 15,880.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 9,090,000.00 USD | 9,090,000.00 USD | 65,520.00 USD | 40,320.00 USD | 46,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 9,300,000.00 USD | 9,300,000.00 USD | 82,510.00 USD | 27,320.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,520,000.00 USD | 9,520,000.00 USD | 143,070.00 USD | 24,010.00 USD | 50,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,620,000.00 USD | 9,620,000.00 USD | 54,700.00 USD | 12,710.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,870,000.00 USD | 9,870,000.00 USD | 135,880.00 USD | 52,120.00 USD | 68,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 10,270,000.00 USD | 10,270,000.00 USD | 189,540.00 USD | 72,980.00 USD | 130,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 10,400,000.00 USD | 10,400,000.00 USD | 64,430.00 USD | 28,610.00 USD | 43,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 10,480,000.00 USD | 10,480,000.00 USD | 36,180.00 USD | 16,900.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 10,690,000.00 USD | 10,690,000.00 USD | 109,700.00 USD | 51,990.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,860,000.00 USD | 10,860,000.00 USD | 77,410.00 USD | 33,200.00 USD | 55,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 11,090,000.00 USD | 11,090,000.00 USD | 126,410.00 USD | 37,730.00 USD | 67,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 11,290,000.00 USD | 11,290,000.00 USD | 112,590.00 USD | 48,130.00 USD | 41,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 11,440,000.00 USD | 11,440,000.00 USD | 77,890.00 USD | 43,820.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 11,500,000.00 USD | 11,500,000.00 USD | 12,890.00 USD | 16,780.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 11,530,000.00 USD | 11,530,000.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,010.00 USD | 73,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 11,580,000.00 USD | 11,580,000.00 USD | 19,270.00 USD | 10,090.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 11,690,000.00 USD | 11,690,000.00 USD | 71,130.00 USD | 12,560.00 USD | 26,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 11,750,000.00 USD | 11,750,000.00 USD | 23,720.00 USD | 11,080.00 USD | 26,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 11,760,000.00 USD | 11,760,000.00 USD | 1,610.00 USD | 6,180.00 USD | 20.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 11,790,000.00 USD | 11,790,000.00 USD | 20,540.00 USD | 5,100.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 73,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 11,820,000.00 USD | 11,820,000.00 USD | 8,930.00 USD | 13,210.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 11,850,000.00 USD | 11,850,000.00 USD | 12,360.00 USD | 6,420.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 11,900,000.00 USD | 11,900,000.00 USD | 17,990.00 USD | 12,140.00 USD | 22,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 11,980,000.00 USD | 11,980,000.00 USD | 57,750.00 USD | 13,980.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 12,020,000.00 USD | 12,020,000.00 USD | 17,170.00 USD | 10,270.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.46` | 12,030,000.00 USD | 12,030,000.00 USD | 128.41 USD | 9,440.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 12,040,000.00 USD | 12,040,000.00 USD | 1,620.00 USD | 2,560.00 USD | 8,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.49` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 18,300,000.00 USD | 18,300,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 18,610,000.00 USD | 18,610,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 18,850,000.00 USD | 18,850,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 242.22 USD | 74,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 19,050,000.00 USD | 19,050,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 19,170,000.00 USD | 19,170,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 19,300,000.00 USD | 19,300,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 19,410,000.00 USD | 19,410,000.00 USD | 64,120.00 USD | 28,270.00 USD | 25,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 19,510,000.00 USD | 19,510,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 19,800,000.00 USD | 19,800,000.00 USD | 54,670.00 USD | 16,240.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 20,040,000.00 USD | 20,040,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 20,130,000.00 USD | 20,130,000.00 USD | 21,450.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 20,220,000.00 USD | 20,220,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 20,290,000.00 USD | 20,290,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.75` | 531.68 USD | 74,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.77` | 20,380,000.00 USD | 20,380,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 20,470,000.00 USD | 20,470,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 20,490,000.00 USD | 20,490,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 20,520,000.00 USD | 20,520,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 20,600,000.00 USD | 20,600,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 1,760.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `13.45` | 5,280.00 USD | 81,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,590.00 USD | 83,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 102.56 USD | 83,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 83,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 84,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 276.00 USD | 84,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 321.55 USD | 84,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 110,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.15` | 62,510.00 USD | 172,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 172,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 173,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.65` | 284.83 USD | 174,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 174,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 174,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 175,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 17,720.00 USD | 193,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 90,600.00 USD | 284,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 2,330.00 USD | 286,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 381,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.55` | 1,390.00 USD | 382,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 27,320.00 USD | 410,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 659,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 351.82 USD | 660,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 7,550.00 USD | 667,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 8,420.00 USD | 676,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 121.11 USD | 676,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 680,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 30,310.00 USD | 710,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 710,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 16,080.00 USD | 726,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 727,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 73,810.00 USD | 800,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 718,380.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 820,020.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 2,320,000.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 2,040.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 5,700.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.35` | 3,680.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 2,740.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 140.48 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.05` | 1,020.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.15` | 16,090.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.15` | 12,210,000.00 USD | 0.00 USD | 681.12 USD | `-79.97%` | `316,800.00` |
| `Live` | `Long` | `2.25` | 12,210,000.00 USD | 0.00 USD | 1,020.00 USD | `-79.04%` | `452,300.00` |
| `Live` | `Long` | `2.45` | 12,210,000.00 USD | 0.00 USD | 670.08 USD | `-77.18%` | `273,500.00` |
| `Live` | `Long` | `2.65` | 12,210,000.00 USD | 0.00 USD | 31,280.00 USD | `-75.31%` | `11,804,500.00` |
| `Live` | `Long` | `2.85` | 12,180,000.00 USD | 0.00 USD | 2,850.00 USD | `-73.45%` | `1,000,000.00` |
| `Live` | `Long` | `2.95` | 12,170,000.00 USD | 0.00 USD | 1,470.00 USD | `-72.52%` | `499,600.00` |
| `Live` | `Long` | `3.05` | 12,170,000.00 USD | 0.00 USD | 6,390.00 USD | `-71.59%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 12,160,000.00 USD | 0.00 USD | 549.99 USD | `-70.66%` | `174,600.00` |
| `Live` | `Long` | `3.25` | 12,160,000.00 USD | 0.00 USD | 10,740.00 USD | `-69.73%` | `3,304,000.00` |
| `Live` | `Long` | `3.35` | 12,150,000.00 USD | 0.00 USD | 592.95 USD | `-68.79%` | `177,000.00` |
| `Live` | `Long` | `3.45` | 12,150,000.00 USD | 0.00 USD | 8,030.00 USD | `-67.86%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,140,000.00 USD | 0.00 USD | 433.45 USD | `-66.93%` | `122,100.00` |
| `Live` | `Long` | `3.65` | 12,140,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.00%` | `600,000.00` |
| `Live` | `Long` | `3.95` | 12,140,000.00 USD | 0.00 USD | 39,500.00 USD | `-63.20%` | `10,000,000.00` |
| `Live` | `Long` | `4.05` | 12,100,000.00 USD | 0.00 USD | 950.54 USD | `-62.27%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,100,000.00 USD | 0.00 USD | 8,760.00 USD | `-61.34%` | `2,112,000.00` |
| `Live` | `Long` | `4.25` | 12,090,000.00 USD | 0.00 USD | 6,930.00 USD | `-60.41%` | `1,630,800.00` |
| `Live` | `Long` | `4.35` | 12,090,000.00 USD | 0.00 USD | 6,080.00 USD | `-59.48%` | `1,398,100.00` |
| `Live` | `Long` | `4.45` | 12,080,000.00 USD | 0.00 USD | 802.78 USD | `-58.55%` | `180,400.00` |
| `Live` | `Long` | `4.55` | 12,080,000.00 USD | 0.00 USD | 50,520.00 USD | `-57.62%` | `11,102,600.00` |
| `Live` | `Long` | `4.65` | 12,030,000.00 USD | 0.00 USD | 383.63 USD | `-56.68%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 12,030,000.00 USD | 0.00 USD | 233,370.00 USD | `-55.75%` | `49,130,300.00` |
| `Live` | `Long` | `4.85` | 11,790,000.00 USD | 0.00 USD | 2,070.00 USD | `-54.82%` | `426,800.00` |
| `Live` | `Long` | `4.95` | 11,790,000.00 USD | 0.00 USD | 3,620.00 USD | `-53.89%` | `732,000.00` |
| `Live` | `Long` | `5.05` | 11,790,000.00 USD | 0.00 USD | 5,050.00 USD | `-52.96%` | `1,000,000.00` |
| `Live` | `Long` | `5.15` | 11,780,000.00 USD | 0.00 USD | 3,680.00 USD | `-52.03%` | `714,900.00` |
| `Live` | `Long` | `5.25` | 11,780,000.00 USD | 0.00 USD | 6,180.00 USD | `-51.09%` | `1,176,500.00` |
| `Live` | `Long` | `5.35` | 11,770,000.00 USD | 0.00 USD | 546,470.00 USD | `-50.16%` | `102,143,200.00` |
| `Live` | `Long` | `5.45` | 11,230,000.00 USD | 0.00 USD | 138.97 USD | `-49.23%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 11,230,000.00 USD | 0.00 USD | 112,260.00 USD | `-48.30%` | `20,226,500.00` |
| `Live` | `Long` | `5.65` | 11,120,000.00 USD | 0.00 USD | 37,860.00 USD | `-47.37%` | `6,701,600.00` |
| `Live` | `Long` | `5.75` | 11,080,000.00 USD | 0.00 USD | 276.57 USD | `-46.44%` | `48,100.00` |
| `Live` | `Long` | `5.85` | 11,080,000.00 USD | 0.00 USD | 15,030.00 USD | `-45.51%` | `2,568,900.00` |
| `Live` | `Long` | `5.95` | 11,060,000.00 USD | 0.00 USD | 790.76 USD | `-44.57%` | `132,900.00` |
| `Live` | `Long` | `6.05` | 11,060,000.00 USD | 0.00 USD | 65,620.00 USD | `-43.64%` | `10,846,700.00` |
| `Live` | `Long` | `6.15` | 11,000,000.00 USD | 0.00 USD | 11,250.00 USD | `-42.71%` | `1,829,200.00` |
| `Live` | `Long` | `6.25` | 10,980,000.00 USD | 0.00 USD | 42,180.00 USD | `-41.78%` | `6,748,700.00` |
| `Live` | `Long` | `6.35` | 10,940,000.00 USD | 0.00 USD | 23,840.00 USD | `-40.85%` | `3,755,000.00` |
| `Live` | `Long` | `6.45` | 10,920,000.00 USD | 0.00 USD | 48,200.00 USD | `-39.92%` | `7,472,100.00` |
| `Live` | `Long` | `6.55` | 10,870,000.00 USD | 0.00 USD | 25,640.00 USD | `-38.98%` | `3,914,300.00` |
| `Live` | `Long` | `6.65` | 10,840,000.00 USD | 0.00 USD | 10,350.00 USD | `-38.05%` | `1,556,900.00` |
| `Live` | `Long` | `6.75` | 10,830,000.00 USD | 0.00 USD | 6,850.00 USD | `-37.12%` | `1,014,400.00` |
| `Live` | `Long` | `6.85` | 10,830,000.00 USD | 0.00 USD | 33,730.00 USD | `-36.19%` | `4,924,500.00` |
| `Live` | `Long` | `6.95` | 10,790,000.00 USD | 0.00 USD | 17,220.00 USD | `-35.26%` | `2,477,000.00` |
| `Live` | `Long` | `7.05` | 10,780,000.00 USD | 0.00 USD | 30,910.00 USD | `-34.33%` | `4,384,800.00` |
| `Live` | `Long` | `7.15` | 10,750,000.00 USD | 0.00 USD | 11,970.00 USD | `-33.40%` | `1,674,000.00` |
| `Live` | `Long` | `7.25` | 10,730,000.00 USD | 0.00 USD | 7,600.00 USD | `-32.46%` | `1,048,400.00` |
| `Live` | `Long` | `7.35` | 10,730,000.00 USD | 0.00 USD | 30,190.00 USD | `-31.53%` | `4,107,400.00` |
| `Live` | `Long` | `7.45` | 10,700,000.00 USD | 0.00 USD | 20,740.00 USD | `-30.60%` | `2,783,300.00` |
| `Live` | `Long` | `7.55` | 10,670,000.00 USD | 0.00 USD | 1,270,000.00 USD | `-29.67%` | `168,362,700.00` |
| `Live` | `Long` | `7.65` | 9,400,000.00 USD | 0.00 USD | 252.45 USD | `-28.74%` | `33,000.00` |
| `Live` | `Long` | `7.75` | 9,400,000.00 USD | 0.00 USD | 16,460.00 USD | `-27.81%` | `2,123,900.00` |
| `Live` | `Long` | `7.85` | 9,390,000.00 USD | 0.00 USD | 2,790.00 USD | `-26.87%` | `355,100.00` |
| `Live` | `Long` | `7.95` | 9,380,000.00 USD | 0.00 USD | 64,420.00 USD | `-25.94%` | `8,103,200.00` |
| `Live` | `Long` | `8.05` | 9,320,000.00 USD | 0.00 USD | 100,290.00 USD | `-25.01%` | `12,457,900.00` |
| `Live` | `Long` | `8.15` | 9,220,000.00 USD | 0.00 USD | 38,160.00 USD | `-24.08%` | `4,681,700.00` |
| `Live` | `Long` | `8.25` | 9,180,000.00 USD | 0.00 USD | 32,470.00 USD | `-23.15%` | `3,935,300.00` |
| `Live` | `Long` | `8.35` | 9,150,000.00 USD | 0.00 USD | 16,130.00 USD | `-22.22%` | `1,932,100.00` |
| `Live` | `Long` | `8.45` | 9,130,000.00 USD | 0.00 USD | 189,230.00 USD | `-21.29%` | `22,393,900.00` |
| `Live` | `Long` | `8.55` | 8,940,000.00 USD | 0.00 USD | 16,350.00 USD | `-20.35%` | `1,912,000.00` |
| `Live` | `Long` | `8.65` | 8,930,000.00 USD | 0.00 USD | 25,730.00 USD | `-19.42%` | `2,974,800.00` |
| `Live` | `Long` | `8.75` | 8,900,000.00 USD | 0.00 USD | 308,920.00 USD | `-18.49%` | `35,304,700.00` |
| `Live` | `Long` | `8.85` | 8,590,000.00 USD | 0.00 USD | 31,360.00 USD | `-17.56%` | `3,543,000.00` |
| `Live` | `Long` | `8.95` | 8,560,000.00 USD | 0.00 USD | 450,470.00 USD | `-16.63%` | `50,331,600.00` |
| `Live` | `Long` | `9.05` | 8,110,000.00 USD | 0.00 USD | 66,460.00 USD | `-15.70%` | `7,343,500.00` |
| `Live` | `Long` | `9.15` | 8,040,000.00 USD | 0.00 USD | 3,750,000.00 USD | `-14.76%` | `409,783,700.00` |
| `Live` | `Long` | `9.25` | 4,290,000.00 USD | 0.00 USD | 36,020.00 USD | `-13.83%` | `3,894,500.00` |
| `Live` | `Long` | `9.35` | 4,260,000.00 USD | 0.00 USD | 2,160,000.00 USD | `-12.90%` | `230,732,900.00` |
| `Live` | `Long` | `9.45` | 2,100,000.00 USD | 0.00 USD | 52,380.00 USD | `-11.97%` | `5,542,800.00` |
| `Live` | `Long` | `9.55` | 2,050,000.00 USD | 0.00 USD | 17,750.00 USD | `-11.04%` | `1,858,300.00` |
| `Live` | `Long` | `9.65` | 2,030,000.00 USD | 0.00 USD | 14,450.00 USD | `-10.11%` | `1,496,900.00` |
| `Live` | `Long` | `9.75` | 2,020,000.00 USD | 0.00 USD | 73,310.00 USD | `-9.18%` | `7,518,800.00` |
| `Live` | `Long` | `9.85` | 1,940,000.00 USD | 0.00 USD | 207,090.00 USD | `-8.24%` | `21,024,400.00` |
| `Live` | `Long` | `9.95` | 1,740,000.00 USD | 0.00 USD | 505,330.00 USD | `-7.31%` | `50,786,700.00` |
| `Live` | `Long` | `10.05` | 1,230,000.00 USD | 0.00 USD | 665,050.00 USD | `-6.38%` | `66,174,100.00` |
| `Live` | `Long` | `10.15` | 566,050.00 USD | 0.00 USD | 12,110.00 USD | `-5.45%` | `1,193,500.00` |
| `Live` | `Long` | `10.25` | 553,930.00 USD | 0.00 USD | 22,430.00 USD | `-4.52%` | `2,188,500.00` |
| `Live` | `Long` | `10.35` | 531,500.00 USD | 0.00 USD | 21,330.00 USD | `-3.59%` | `2,061,200.00` |
| `Live` | `Long` | `10.45` | 510,170.00 USD | 0.00 USD | 48,180.00 USD | `-2.65%` | `4,610,800.00` |
| `Live` | `Long` | `10.55` | 461,980.00 USD | 0.00 USD | 443,270.00 USD | `-1.72%` | `42,015,900.00` |
| `Live` | `Long` | `10.65` | 18,720.00 USD | 0.00 USD | 18,720.00 USD | `-0.79%` | `1,757,300.00` |
| `Live` | `Short` | `10.75` | 18,760.00 USD | 18,760.00 USD | 0.00 USD | `+0.14%` | `1,744,800.00` |
| `Live` | `Short` | `10.95` | 21,280.00 USD | 2,530.00 USD | 0.00 USD | `+2.00%` | `230,800.00` |
| `Live` | `Short` | `11.05` | 21,780.00 USD | 496.15 USD | 0.00 USD | `+2.93%` | `44,900.00` |
| `Live` | `Short` | `11.25` | 33,630.00 USD | 11,850.00 USD | 0.00 USD | `+4.80%` | `1,052,900.00` |
| `Live` | `Short` | `11.35` | 39,560.00 USD | 5,930.00 USD | 0.00 USD | `+5.73%` | `522,500.00` |
| `Live` | `Short` | `11.45` | 59,870.00 USD | 20,310.00 USD | 0.00 USD | `+6.66%` | `1,773,900.00` |
| `Live` | `Short` | `11.55` | 131,240.00 USD | 71,370.00 USD | 0.00 USD | `+7.59%` | `6,179,500.00` |
| `Live` | `Short` | `11.65` | 139,740.00 USD | 8,500.00 USD | 0.00 USD | `+8.52%` | `729,700.00` |
| `Live` | `Short` | `11.75` | 141,280.00 USD | 1,540.00 USD | 0.00 USD | `+9.46%` | `131,100.00` |
| `Live` | `Short` | `12.05` | 148,770.00 USD | 7,480.00 USD | 0.00 USD | `+12.25%` | `621,100.00` |
| `Live` | `Short` | `12.15` | 173,970.00 USD | 25,210.00 USD | 0.00 USD | `+13.18%` | `2,074,800.00` |
| `Live` | `Short` | `12.25` | 174,980.00 USD | 1,010.00 USD | 0.00 USD | `+14.11%` | `82,200.00` |
| `Live` | `Short` | `12.35` | 292,890.00 USD | 117,910.00 USD | 0.00 USD | `+15.04%` | `9,547,600.00` |
| `Live` | `Short` | `12.55` | 293,800.00 USD | 903.60 USD | 0.00 USD | `+16.91%` | `72,000.00` |
| `Live` | `Short` | `12.65` | 293,910.00 USD | 113.85 USD | 0.00 USD | `+17.84%` | `9,000.00` |
| `Live` | `Short` | `12.85` | 294,050.00 USD | 138.78 USD | 0.00 USD | `+19.70%` | `10,800.00` |
| `Live` | `Short` | `13.45` | 299,330.00 USD | 5,280.00 USD | 0.00 USD | `+25.29%` | `392,900.00` |
| `Live` | `Short` | `13.85` | 305,810.00 USD | 6,470.00 USD | 0.00 USD | `+29.02%` | `467,300.00` |
| `Live` | `Short` | `14.05` | 306,260.00 USD | 449.60 USD | 0.00 USD | `+30.88%` | `32,000.00` |
| `Live` | `Short` | `14.25` | 308,220.00 USD | 1,960.00 USD | 0.00 USD | `+32.74%` | `137,600.00` |
| `Live` | `Short` | `14.45` | 308,530.00 USD | 315.01 USD | 0.00 USD | `+34.61%` | `21,800.00` |
| `Live` | `Short` | `14.55` | 478,330.00 USD | 169,800.00 USD | 0.00 USD | `+35.54%` | `11,670,000.00` |
| `Live` | `Short` | `14.75` | 489,130.00 USD | 10,800.00 USD | 0.00 USD | `+37.40%` | `732,000.00` |
| `Live` | `Short` | `14.95` | 514,630.00 USD | 25,500.00 USD | 0.00 USD | `+39.26%` | `1,705,700.00` |
| `Live` | `Short` | `15.15` | 586,960.00 USD | 72,340.00 USD | 0.00 USD | `+41.13%` | `4,774,700.00` |
| `Live` | `Short` | `15.55` | 587,800.00 USD | 838.14 USD | 0.00 USD | `+44.85%` | `53,900.00` |
| `Live` | `Short` | `15.65` | 589,080.00 USD | 1,280.00 USD | 0.00 USD | `+45.78%` | `81,700.00` |
| `Live` | `Short` | `15.85` | 589,350.00 USD | 271.04 USD | 0.00 USD | `+47.65%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 589,490.00 USD | 138.76 USD | 0.00 USD | `+48.58%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 591,020.00 USD | 1,530.00 USD | 0.00 USD | `+52.31%` | `93,400.00` |
| `Live` | `Short` | `16.55` | 605,210.00 USD | 14,190.00 USD | 0.00 USD | `+54.17%` | `857,700.00` |
| `Live` | `Short` | `16.65` | 605,600.00 USD | 382.95 USD | 0.00 USD | `+55.10%` | `23,000.00` |
| `Live` | `Short` | `16.75` | 717,840.00 USD | 112,250.00 USD | 0.00 USD | `+56.03%` | `6,701,200.00` |
| `Live` | `Short` | `16.95` | 797,610.00 USD | 79,770.00 USD | 0.00 USD | `+57.89%` | `4,706,300.00` |
| `Live` | `Short` | `17.05` | 797,850.00 USD | 238.70 USD | 0.00 USD | `+58.83%` | `14,000.00` |
| `Live` | `Short` | `17.15` | 799,950.00 USD | 2,090.00 USD | 0.00 USD | `+59.76%` | `122,100.00` |
| `Live` | `Short` | `17.25` | 818,200.00 USD | 18,250.00 USD | 0.00 USD | `+60.69%` | `1,058,000.00` |
| `Live` | `Short` | `17.45` | 829,350.00 USD | 11,150.00 USD | 0.00 USD | `+62.55%` | `639,000.00` |
| `Live` | `Short` | `17.85` | 829,600.00 USD | 249.90 USD | 0.00 USD | `+66.28%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 829,950.00 USD | 351.82 USD | 0.00 USD | `+67.21%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 1,080,000.00 USD | 254,100.00 USD | 0.00 USD | `+68.14%` | `14,077,300.00` |
| `Live` | `Short` | `18.35` | 1,110,000.00 USD | 28,240.00 USD | 0.00 USD | `+70.94%` | `1,539,000.00` |
| `Live` | `Short` | `18.45` | 1,120,000.00 USD | 4,010.00 USD | 0.00 USD | `+71.87%` | `217,400.00` |
| `Live` | `Short` | `18.55` | 1,120,000.00 USD | 3,470.00 USD | 0.00 USD | `+72.80%` | `187,000.00` |
| `Live` | `Short` | `18.65` | 1,130,000.00 USD | 5,950.00 USD | 0.00 USD | `+73.73%` | `319,000.00` |
| `Live` | `Short` | `18.75` | 1,250,000.00 USD | 126,640.00 USD | 0.00 USD | `+74.66%` | `6,754,200.00` |
| `Live` | `Short` | `18.85` | 1,250,000.00 USD | 456.17 USD | 0.00 USD | `+75.59%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 1,970,000.00 USD | 714,600.00 USD | 0.00 USD | `+76.53%` | `37,710,000.00` |
| `Live` | `Short` | `19.05` | 1,970,000.00 USD | 1,200.00 USD | 0.00 USD | `+77.46%` | `62,900.00` |
| `Live` | `Short` | `19.35` | 2,000,000.00 USD | 29,470.00 USD | 0.00 USD | `+80.25%` | `1,523,000.00` |
| `Live` | `Short` | `19.55` | 2,900,000.00 USD | 897,840.00 USD | 0.00 USD | `+82.11%` | `45,925,300.00` |
| `Live` | `Short` | `19.65` | 2,930,000.00 USD | 38,790.00 USD | 0.00 USD | `+83.05%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 2,930,000.00 USD | 254.78 USD | 0.00 USD | `+83.98%` | `12,900.00` |
| `Live` | `Short` | `19.95` | 2,940,000.00 USD | 291.27 USD | 0.00 USD | `+85.84%` | `14,600.00` |
| `Live` | `Short` | `20.55` | 5,310,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+91.43%` | `115,377,600.00` |
| `Live` | `Short` | `20.95` | 5,310,000.00 USD | 4,220.00 USD | 0.00 USD | `+95.16%` | `201,200.00` |
| `Live` | `Short` | `21.25` | 5,310,000.00 USD | 499.38 USD | 0.00 USD | `+97.95%` | `23,500.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 349,130.00 USD | 0.00 USD | 431.68 USD | `-66.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 348,700.00 USD | 0.00 USD | 290.29 USD | `-57.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 348,410.00 USD | 0.00 USD | 120.22 USD | `-51.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 348,290.00 USD | 0.00 USD | 107.09 USD | `-43.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 348,180.00 USD | 0.00 USD | 4,260.00 USD | `-38.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 343,920.00 USD | 0.00 USD | 133.00 USD | `-38.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 343,790.00 USD | 0.00 USD | 3,770.00 USD | `-34.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 340,020.00 USD | 0.00 USD | 2,070.00 USD | `-32.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 337,950.00 USD | 0.00 USD | 3,740.00 USD | `-30.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 334,200.00 USD | 0.00 USD | 1,050.00 USD | `-29.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 333,150.00 USD | 0.00 USD | 146.80 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 333,000.00 USD | 0.00 USD | 166.95 USD | `-25.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 332,840.00 USD | 0.00 USD | 5,000.00 USD | `-25.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 327,840.00 USD | 0.00 USD | 393.64 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 327,440.00 USD | 0.00 USD | 10,660.00 USD | `-23.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 316,780.00 USD | 0.00 USD | 1,360.00 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 315,420.00 USD | 0.00 USD | 52,990.00 USD | `-20.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 262,440.00 USD | 0.00 USD | 186.84 USD | `-19.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 262,250.00 USD | 0.00 USD | 742.88 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 261,510.00 USD | 0.00 USD | 902.70 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 260,600.00 USD | 0.00 USD | 1,570.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 259,030.00 USD | 0.00 USD | 3,060.00 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 255,980.00 USD | 0.00 USD | 194.90 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 255,780.00 USD | 0.00 USD | 531.88 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 255,250.00 USD | 0.00 USD | 5,090.00 USD | `-12.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 250,160.00 USD | 0.00 USD | 2,090.00 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 248,060.00 USD | 0.00 USD | 10,530.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 237,540.00 USD | 0.00 USD | 3,550.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 233,990.00 USD | 0.00 USD | 7,670.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 226,320.00 USD | 0.00 USD | 23,380.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 202,940.00 USD | 0.00 USD | 1,620.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 201,320.00 USD | 0.00 USD | 2,590.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 198,730.00 USD | 0.00 USD | 1,050.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 197,680.00 USD | 0.00 USD | 94,340.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 103,340.00 USD | 0.00 USD | 9,860.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 93,480.00 USD | 0.00 USD | 42,220.00 USD | `-2.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 51,260.00 USD | 0.00 USD | 31,070.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 20,190.00 USD | 0.00 USD | 20,190.00 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.75` | 3,630.00 USD | 3,630.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.85` | 12,270.00 USD | 8,640.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.95` | 81,420.00 USD | 69,150.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 83,170.00 USD | 1,740.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 84,120.00 USD | 958.90 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 115,430.00 USD | 31,310.00 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 125,430.00 USD | 10,000.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 125,820.00 USD | 390.44 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 128,430.00 USD | 2,610.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 129,160.00 USD | 732.79 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 149,680.00 USD | 20,520.00 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 150,310.00 USD | 632.79 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 163,260.00 USD | 12,950.00 USD | 0.00 USD | `+11.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 211,370.00 USD | 48,110.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 212,170.00 USD | 797.04 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 228,150.00 USD | 15,980.00 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 228,640.00 USD | 494.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 228,880.00 USD | 240.28 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 349,030.00 USD | 120,140.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 432,910.00 USD | 83,880.00 USD | 0.00 USD | `+17.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 441,760.00 USD | 8,860.00 USD | 0.00 USD | `+18.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 461,820.00 USD | 20,060.00 USD | 0.00 USD | `+19.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 462,270.00 USD | 451.95 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 478,900.00 USD | 16,630.00 USD | 0.00 USD | `+21.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 479,950.00 USD | 1,050.00 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 481,260.00 USD | 1,320.00 USD | 0.00 USD | `+23.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 486,000.00 USD | 4,730.00 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 488,190.00 USD | 2,200.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 488,360.00 USD | 165.31 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 490,510.00 USD | 2,150.00 USD | 0.00 USD | `+27.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 492,570.00 USD | 2,060.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 496,920.00 USD | 4,350.00 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 497,180.00 USD | 266.44 USD | 0.00 USD | `+29.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 521,970.00 USD | 24,790.00 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 522,480.00 USD | 506.57 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 525,890.00 USD | 3,410.00 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 526,610.00 USD | 718.16 USD | 0.00 USD | `+34.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 526,830.00 USD | 218.25 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 528,680.00 USD | 1,850.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 536,240.00 USD | 7,560.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 537,190.00 USD | 950.82 USD | 0.00 USD | `+39.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 562,240.00 USD | 25,060.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 564,790.00 USD | 2,550.00 USD | 0.00 USD | `+41.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 797,830.00 USD | 233,040.00 USD | 0.00 USD | `+42.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 799,010.00 USD | 1,180.00 USD | 0.00 USD | `+42.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 799,910.00 USD | 893.01 USD | 0.00 USD | `+43.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 801,010.00 USD | 1,100.00 USD | 0.00 USD | `+44.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 801,960.00 USD | 949.96 USD | 0.00 USD | `+45.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 805,400.00 USD | 3,450.00 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 810,740.00 USD | 5,340.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 817,920.00 USD | 7,180.00 USD | 0.00 USD | `+48.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 827,090.00 USD | 9,170.00 USD | 0.00 USD | `+49.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 833,900.00 USD | 6,800.00 USD | 0.00 USD | `+50.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 852,660.00 USD | 18,760.00 USD | 0.00 USD | `+51.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 886,880.00 USD | 34,220.00 USD | 0.00 USD | `+52.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 893,460.00 USD | 6,580.00 USD | 0.00 USD | `+53.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 903,390.00 USD | 9,930.00 USD | 0.00 USD | `+54.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 1,010,000.00 USD | 103,980.00 USD | 0.00 USD | `+55.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 1,020,000.00 USD | 14,240.00 USD | 0.00 USD | `+56.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 1,110,000.00 USD | 84,360.00 USD | 0.00 USD | `+56.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 1,110,000.00 USD | 1,700.00 USD | 0.00 USD | `+57.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 1,120,000.00 USD | 8,830.00 USD | 0.00 USD | `+58.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 1,120,000.00 USD | 1,710.00 USD | 0.00 USD | `+59.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 1,120,000.00 USD | 2,300.00 USD | 0.00 USD | `+60.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,120,000.00 USD | 1,740.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,140,000.00 USD | 19,070.00 USD | 0.00 USD | `+62.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,150,000.00 USD | 4,390.00 USD | 0.00 USD | `+63.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,150,000.00 USD | 4,410.00 USD | 0.00 USD | `+64.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,150,000.00 USD | 4,440.00 USD | 0.00 USD | `+65.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,160,000.00 USD | 4,460.00 USD | 0.00 USD | `+66.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,160,000.00 USD | 448.75 USD | 0.00 USD | `+67.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,200,000.00 USD | 35,940.00 USD | 0.00 USD | `+68.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,200,000.00 USD | 453.75 USD | 0.00 USD | `+69.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,200,000.00 USD | 830.38 USD | 0.00 USD | `+70.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,200,000.00 USD | 458.75 USD | 0.00 USD | `+70.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,200,000.00 USD | 461.25 USD | 0.00 USD | `+71.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,200,000.00 USD | 4,540.00 USD | 0.00 USD | `+72.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,200,000.00 USD | 466.25 USD | 0.00 USD | `+73.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,200,000.00 USD | 468.75 USD | 0.00 USD | `+74.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,200,000.00 USD | 471.25 USD | 0.00 USD | `+75.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,200,000.00 USD | 473.75 USD | 0.00 USD | `+76.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,270,000.00 USD | 67,000.00 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,270,000.00 USD | 2,150.00 USD | 0.00 USD | `+78.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,270,000.00 USD | 577.50 USD | 0.00 USD | `+79.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,280,000.00 USD | 2,710.00 USD | 0.00 USD | `+80.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,280,000.00 USD | 972.50 USD | 0.00 USD | `+81.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,290,000.00 USD | 7,680.00 USD | 0.00 USD | `+82.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,290,000.00 USD | 786.00 USD | 0.00 USD | `+83.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,290,000.00 USD | 1,690.00 USD | 0.00 USD | `+83.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,290,000.00 USD | 992.50 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,290,000.00 USD | 997.50 USD | 0.00 USD | `+85.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,890,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+86.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,890,000.00 USD | 1,010.00 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,890,000.00 USD | 1,010.00 USD | 0.00 USD | `+88.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,900,000.00 USD | 1,020.00 USD | 0.00 USD | `+89.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,900,000.00 USD | 1,020.00 USD | 0.00 USD | `+90.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,900,000.00 USD | 1,030.00 USD | 0.00 USD | `+91.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,900,000.00 USD | 1,030.00 USD | 0.00 USD | `+92.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,900,000.00 USD | 1,040.00 USD | 0.00 USD | `+93.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,900,000.00 USD | 1,410.00 USD | 0.00 USD | `+94.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,900,000.00 USD | 1,050.00 USD | 0.00 USD | `+95.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,910,000.00 USD | 4,000.00 USD | 0.00 USD | `+96.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,910,000.00 USD | 1,060.00 USD | 0.00 USD | `+97.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,910,000.00 USD | 1,060.00 USD | 0.00 USD | `+97.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,960,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+98.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,960,000.00 USD | 2,340.00 USD | 0.00 USD | `+99.81%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.53` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD |
| `7D` | `9.55` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD |
| `7D` | `9.57` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD |
| `7D` | `9.59` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `9.60` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `7D` | `9.61` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `7D` | `9.63` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD |
| `1D` | `9.64` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 105.10 USD |
| `7D` | `9.65` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD |
| `1D` | `9.66` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 0.00 USD | 4,020.00 USD | 0.00 USD |
| `7D` | `9.67` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `9.68` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `9.69` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.70` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 15,910.00 USD |
| `7D` | `9.71` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `1D` | `9.72` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 14,340.00 USD |
| `7D` | `9.73` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.74` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 709.80 USD | 0.00 USD | 14,900.00 USD |
| `7D` | `9.75` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD |
| `1D` | `9.76` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 96,370.00 USD | 689.80 USD | 13,120.00 USD |
| `7D` | `9.77` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.78` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 55,890.00 USD | 7,220.00 USD | 19,810.00 USD |
| `7D` | `9.79` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD |
| `1D` | `9.80` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 37,210.00 USD | 3,860.00 USD | 0.00 USD |
| `7D` | `9.81` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD |
| `1D` | `9.82` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 77,230.00 USD | 14,710.00 USD | 20,200.00 USD |
| `7D` | `9.83` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD |
| `1D` | `9.84` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 11,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.85` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `9.86` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 9,950.00 USD | 463.70 USD | 10,190.00 USD |
| `7D` | `9.89` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.90` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD |
| `7D` | `9.91` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.92` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 13,840.00 USD | 11,040.00 USD | 44.44 USD |
| `7D` | `9.93` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.94` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD |
| `7D` | `9.95` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD |
| `1D` | `9.96` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 7,630.00 USD | 11,250.00 USD | 16,090.00 USD |
| `7D` | `9.97` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD |
| `1D` | `9.98` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 0.00 USD | 6,740.00 USD | 12,220.00 USD |
| `7D` | `9.99` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD |
| `1D` | `10.00` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 0.00 USD | 254.10 USD | 357.76 USD |
| `7D` | `10.01` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.04` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD |
| `7D` | `10.05` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `1D` | `10.06` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 91.65 USD |
| `7D` | `10.07` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `1D` | `10.08` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 73.70 USD |
| `7D` | `10.09` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.10` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 7,570.00 USD | 0.00 USD | 147.11 USD |
| `7D` | `10.11` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD |
| `1D` | `10.12` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 1,150.00 USD | 7,510.00 USD | 0.00 USD |
| `7D` | `10.13` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.14` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD |
| `7D` | `10.15` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `1D` | `10.16` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 7,170.00 USD | 0.00 USD | 21.54 USD |
| `7D` | `10.17` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD |
| `1D` | `10.18` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 2,920.00 USD | 29.65 USD | 593.78 USD |
| `7D` | `10.19` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.20` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD |
| `7D` | `10.21` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.22` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 536.32 USD | 4,320.00 USD | 16,420.00 USD |
| `7D` | `10.23` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.24` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,530.00 USD |
| `7D` | `10.25` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.26` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 13,990.00 USD | 2,830.00 USD | 109.48 USD |
| `7D` | `10.27` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.28` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 29,240.00 USD | 9,320.00 USD | 10,170.00 USD |
| `7D` | `10.29` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD |
| `1D` | `10.30` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 9,060.00 USD | 11,600.00 USD | 10,900.00 USD |
| `7D` | `10.31` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD |
| `1D` | `10.32` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 28,010.00 USD | 19,910.00 USD | 82,500.00 USD |
| `7D` | `10.33` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD |
| `1D` | `10.34` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 32,410.00 USD | 4,260.00 USD | 11,840.00 USD |
| `7D` | `10.35` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.36` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 8,260.00 USD | 3,450.00 USD | 71,500.00 USD |
| `7D` | `10.37` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD |
| `1D` | `10.38` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,450.00 USD | 4,400.00 USD | 80,150.00 USD |
| `7D` | `10.39` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.40` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 109,640.00 USD | 8,470.00 USD | 41,930.00 USD |
| `7D` | `10.41` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD |
| `1D` | `10.42` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 237,840.00 USD | 20,290.00 USD | 46,120.00 USD |
| `7D` | `10.43` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.44` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 141,180.00 USD | 30,800.00 USD | 36,550.00 USD |
| `7D` | `10.45` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD |
| `1D` | `10.46` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 221,310.00 USD | 49,390.00 USD | 46,010.00 USD |
| `7D` | `10.47` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD |
| `1D` | `10.48` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 124,220.00 USD | 10,980.00 USD | 46,850.00 USD |
| `7D` | `10.49` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD |
| `1D` | `10.50` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 79,100.00 USD | 15,300.00 USD | 9,790.00 USD |
| `7D` | `10.51` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.52` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 65,390.00 USD | 25,650.00 USD | 38,280.00 USD |
| `7D` | `10.53` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD |
| `1D` | `10.54` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 740.06 USD | 16,650.00 USD | 147,670.00 USD |
| `7D` | `10.55` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD |
| `1D` | `10.56` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 58,790.00 USD | 23,780.00 USD | 81,260.00 USD |
| `7D` | `10.57` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD |
| `1D` | `10.58` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 48,460.00 USD | 30,610.00 USD | 129,980.00 USD |
| `7D` | `10.59` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD |
| `1D` | `10.60` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 15,270.00 USD | 7,950.00 USD | 77,410.00 USD |
| `7D` | `10.61` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD |
| `1D` | `10.62` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 516,250.00 USD | 27,900.00 USD | 117,670.00 USD |
| `7D` | `10.63` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD |
| `1D` | `10.64` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 292,600.00 USD | 69,030.00 USD | 148,760.00 USD |
| `7D` | `10.65` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD |
| `1D` | `10.66` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 122,590.00 USD | 17,330.00 USD | 44,110.00 USD |
| `7D` | `10.67` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD |
| `1D` | `10.68` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 441,140.00 USD | 94,900.00 USD | 80,020.00 USD |
| `7D` | `10.69` | 801,310.00 USD | 0.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD |
| `1D` | `10.70` | 559,250.00 USD | 0.00 USD | 559,250.00 USD | 241,770.00 USD | 22,060.00 USD | 78,870.00 USD |
| `7D` | `10.71` | 323,480.00 USD | 0.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD |
| `1D` | `10.72` | 216,540.00 USD | 0.00 USD | 216,540.00 USD | 112,490.00 USD | 12,290.00 USD | 7,330.00 USD |
| `7D` | `10.73` | 29,560.00 USD | 29,560.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `7D` | `10.73` | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `1D` | `10.74` | 84,430.00 USD | 0.00 USD | 84,430.00 USD | 84,420.00 USD | 0.00 USD | 14.85 USD |
| `1D` | `10.75` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.75` | 77,290.00 USD | 77,290.00 USD | 0.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD |
| `1D` | `10.76` | 16,890.00 USD | 16,890.00 USD | 0.00 USD | 12,370.00 USD | 4,530.00 USD | 0.00 USD |
| `7D` | `10.77` | 98,870.00 USD | 98,870.00 USD | 0.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD |
| `1D` | `10.78` | 160,720.00 USD | 160,720.00 USD | 0.00 USD | 86,290.00 USD | 57,540.00 USD | 0.00 USD |
| `7D` | `10.79` | 192,270.00 USD | 192,270.00 USD | 0.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD |
| `1D` | `10.80` | 218,290.00 USD | 218,290.00 USD | 0.00 USD | 2,390.00 USD | 55,190.00 USD | 0.00 USD |
| `1D` | `10.94` | 239,890.00 USD | 239,890.00 USD | 0.00 USD | 454.50 USD | 21,140.00 USD | 0.00 USD |
| `7D` | `10.95` | 227,860.00 USD | 227,860.00 USD | 0.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD |
| `1D` | `10.96` | 358,240.00 USD | 358,240.00 USD | 0.00 USD | 877.67 USD | 29,730.00 USD | 87,750.00 USD |
| `7D` | `10.97` | 240,550.00 USD | 240,550.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.98` | 414,180.00 USD | 414,180.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 54,460.00 USD |
| `7D` | `10.99` | 413,570.00 USD | 413,570.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD |
| `1D` | `11.00` | 493,550.00 USD | 493,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 79,370.00 USD |
| `7D` | `11.01` | 424,150.00 USD | 424,150.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.02` | 591,980.00 USD | 591,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98,430.00 USD |
| `7D` | `11.03` | 576,560.00 USD | 576,560.00 USD | 0.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.04` | 666,230.00 USD | 666,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,250.00 USD |
| `7D` | `11.05` | 966,150.00 USD | 966,150.00 USD | 0.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.06` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 475,540.00 USD | 3,450.00 USD | 65,580.00 USD |
| `7D` | `11.07` | 973,650.00 USD | 973,650.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.08` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 279,470.00 USD | 49,490.00 USD | 119,270.00 USD |
| `7D` | `11.09` | 981,150.00 USD | 981,150.00 USD | 0.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `11.10` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 77,170.00 USD | 1,180.00 USD | 0.00 USD |
| `7D` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD |
| `1D` | `11.12` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 424,370.00 USD | 92,530.00 USD | 80,090.00 USD |
| `7D` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD |
| `1D` | `11.14` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 212,890.00 USD | 12,460.00 USD | 67,800.00 USD |
| `7D` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD |
| `1D` | `11.16` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 104,910.00 USD | 50,250.00 USD | 0.00 USD |
| `7D` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD |
| `1D` | `11.18` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 71,610.00 USD | 55,530.00 USD | 86,130.00 USD |
| `7D` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD |
| `1D` | `11.20` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 42,500.00 USD | 39,440.00 USD | 47,830.00 USD |
| `7D` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD |
| `1D` | `11.22` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 262,060.00 USD | 587.72 USD | 96,100.00 USD |
| `7D` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.24` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 90,500.00 USD | 28,030.00 USD | 190,180.00 USD |
| `7D` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD |
| `1D` | `11.26` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 125,040.00 USD | 11,690.00 USD | 103,570.00 USD |
| `7D` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.28` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 279,810.00 USD | 56,750.00 USD | 248,550.00 USD |
| `7D` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD |
| `1D` | `11.30` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 63,460.00 USD | 78,590.00 USD | 100,650.00 USD |
| `7D` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.32` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 101,830.00 USD | 66,860.00 USD | 83,000.00 USD |
| `7D` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD |
| `1D` | `11.34` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 397,010.00 USD | 101,070.00 USD | 40,090.00 USD |
| `7D` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD |
| `1D` | `11.36` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 108,490.00 USD | 99,470.00 USD | 56,240.00 USD |
| `7D` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD |
| `1D` | `11.38` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 106,580.00 USD | 61,510.00 USD | 0.00 USD |
| `7D` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 35,800.00 USD | 24,370.00 USD | 104,440.00 USD |
| `7D` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.42` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 108,320.00 USD | 45,350.00 USD | 78,840.00 USD |
| `7D` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD |
| `1D` | `11.44` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 42,610.00 USD | 18,500.00 USD | 53,180.00 USD |
| `7D` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.46` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 49,150.00 USD | 65,340.00 USD | 23,590.00 USD |
| `7D` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.48` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 14,310.00 USD | 10,140.00 USD | 0.00 USD |
| `7D` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.50` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 31,090.00 USD | 33,490.00 USD | 45,950.00 USD |
| `7D` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 29,340.00 USD | 13,740.00 USD | 19,550.00 USD |
| `7D` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD |
| `1D` | `11.54` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 33,710.00 USD | 16,150.00 USD | 41,520.00 USD |
| `7D` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD |
| `1D` | `11.56` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 65,320.00 USD | 635.25 USD | 15,160.00 USD |
| `7D` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.58` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 46,550.00 USD | 335.85 USD | 17,640.00 USD |
| `7D` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.60` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 124,870.00 USD | 7,320.00 USD | 67,250.00 USD |
| `7D` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.62` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 43,430.00 USD | 0.00 USD | 33,960.00 USD |
| `7D` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.64` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD | 16,750.00 USD |
| `7D` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD |
| `7D` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 59,600.00 USD | 28,810.00 USD | 79.66 USD |
| `7D` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.70` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 150.75 USD |
| `7D` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.72` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD |
| `7D` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.74` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 35,580.00 USD | 17,540.00 USD | 73,010.00 USD |
| `7D` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.76` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 24,330.00 USD | 14,970.00 USD | 10,340.00 USD |
| `7D` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.78` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 27,290.00 USD | 18,740.00 USD | 40,030.00 USD |
| `7D` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.80` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 18,370.00 USD | 79.46 USD |
| `7D` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 11,070.00 USD | 0.00 USD | 36,290.00 USD |
| `7D` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.84` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 76,470.00 USD | 11,830.00 USD | 55,550.00 USD |
| `7D` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.86` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 232.40 USD | 33,990.00 USD | 53,980.00 USD |
| `7D` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.88` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 19,640.00 USD | 25,990.00 USD | 60,210.00 USD |
| `7D` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.90` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 44,870.00 USD | 8,750.00 USD | 28,010.00 USD |
| `7D` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.92` | 8,830,000.00 USD | 8,830,000.00 USD | 0.00 USD | 230,070.00 USD | 23,160.00 USD | 25,030.00 USD |
| `7D` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.94` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 49,250.00 USD | 15,880.00 USD | 40,290.00 USD |
| `7D` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 65,520.00 USD | 40,320.00 USD | 46,080.00 USD |
| `7D` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.98` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 82,510.00 USD | 27,320.00 USD | 98,270.00 USD |
| `7D` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.00` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 143,070.00 USD | 24,010.00 USD | 50,990.00 USD |
| `7D` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD |
| `1D` | `12.02` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 54,700.00 USD | 12,710.00 USD | 31,490.00 USD |
| `7D` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD |
| `1D` | `12.04` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 135,880.00 USD | 52,120.00 USD | 68,700.00 USD |
| `7D` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.06` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 189,540.00 USD | 72,980.00 USD | 130,250.00 USD |
| `7D` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.08` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 64,430.00 USD | 28,610.00 USD | 43,150.00 USD |
| `7D` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.10` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 36,180.00 USD | 16,900.00 USD | 22,430.00 USD |
| `7D` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.12` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 109,700.00 USD | 51,990.00 USD | 50,490.00 USD |
| `7D` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.14` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 77,410.00 USD | 33,200.00 USD | 55,820.00 USD |
| `7D` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.16` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 126,410.00 USD | 37,730.00 USD | 67,580.00 USD |
| `7D` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.18` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 112,590.00 USD | 48,130.00 USD | 41,220.00 USD |
| `7D` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD |
| `1D` | `12.20` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 77,890.00 USD | 43,820.00 USD | 32,240.00 USD |
| `7D` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD |
| `1D` | `12.22` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 12,890.00 USD | 16,780.00 USD | 28,230.00 USD |
| `7D` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.24` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.26` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 19,270.00 USD | 10,090.00 USD | 15,070.00 USD |
| `7D` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.28` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 71,130.00 USD | 12,560.00 USD | 26,050.00 USD |
| `7D` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.30` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 23,720.00 USD | 11,080.00 USD | 26,170.00 USD |
| `7D` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.32` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 1,610.00 USD | 6,180.00 USD | 20.46 USD |
| `7D` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD |
| `1D` | `12.34` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 20,540.00 USD | 5,100.00 USD | 8,830.00 USD |
| `7D` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.36` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 8,930.00 USD | 13,210.00 USD | 3,070.00 USD |
| `7D` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD |
| `1D` | `12.38` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 12,360.00 USD | 6,420.00 USD | 12,650.00 USD |
| `7D` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD |
| `1D` | `12.40` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 17,990.00 USD | 12,140.00 USD | 22,860.00 USD |
| `7D` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.42` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 57,750.00 USD | 13,980.00 USD | 9,680.00 USD |
| `7D` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.44` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 17,170.00 USD | 10,270.00 USD | 6,520.00 USD |
| `7D` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.46` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 128.41 USD | 9,440.00 USD | 4,210.00 USD |
| `7D` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD |
| `1D` | `12.48` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 1,620.00 USD | 2,560.00 USD | 8,240.00 USD |
| `1D` | `12.49` | 12,040,000.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,340.00 USD |
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
  * Total Open Interest: `527.10M` | Total OI Tokens: `49,130,299.1 LINK`
  * 1h OI Change: `+0.54%` | 4h OI Change: `-5.33%` | 24h OI Change: `-7.99%`
  * Exchange Breakdown: Binance=`102.14M` | Bybit=`62.67M` | OKX=`25.92M` | Hyperliquid=`51.55M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.28K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0026%` | **USDT OKX** | `0.0086%` |
| **USDT Bybit** | `0.0018%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0026%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0056%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `46.63%` | `53.37%` | `0.87` | 47,410,000.00 USD |
| `15M` | `Binance` | `43.34%` | `56.66%` | `0.76` | 18,780,000.00 USD |
| `15M` | `OKX` | `52.97%` | `47.03%` | `1.13` | 8,550,000.00 USD |
| `15M` | `Bybit` | `49.33%` | `50.67%` | `0.97` | 7,800,000.00 USD |
| `15M` | `KuCoin` | `48.96%` | `51.04%` | `0.96` | 233,920.00 USD |
| `15M` | `Gate` | `44.86%` | `55.14%` | `0.81` | 1,660,000.00 USD |
| `15M` | `Bitget` | `54.21%` | `45.79%` | `1.18` | 1,540,000.00 USD |
| `15M` | `BingX` | `36.09%` | `63.91%` | `0.56` | 195,070.00 USD |
| `15M` | `MEXC` | `63.25%` | `36.75%` | `1.72` | 395,690.00 USD |
| `15M` | `Bitunix` | `48.57%` | `51.43%` | `0.94` | 618,800.00 USD |
| `15M` | `Hyperliquid` | `43.61%` | `56.39%` | `0.77` | 1,530,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.87%` | `50.13%` | `0.99` | 1,020,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `37.79%` | `62.21%` | `0.61` | 4,020,000.00 USD |
| `15M` | `HTX` | `29.06%` | `70.94%` | `0.41` | 154,710.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `73.08%` | `26.92%` | `2.71` | 304,640.00 USD |
| `15M` | `Aster` | `44.9%` | `55.1%` | `0.81` | 185,950.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.64%` | `45.36%` | `1.20` | 436,010.00 USD |
| `15M` | `Whale Positions` | `43.34%` | `56.66%` | `0.76` | 18,780,000.00 USD |
| `15M` | `Global Accounts` | `46.63%` | `53.37%` | `0.87` | 47,410,000.00 USD |
| `1H` | `LINK` | `47.70%` | `52.30%` | `0.91` | 228,760,000.00 USD |
| `1H` | `Binance` | `48.18%` | `51.82%` | `0.93` | 104,070,000.00 USD |
| `1H` | `OKX` | `51.68%` | `48.32%` | `1.07` | 29,200,000.00 USD |
| `1H` | `Bybit` | `45.58%` | `54.42%` | `0.84` | 43,920,000.00 USD |
| `1H` | `KuCoin` | `48.47%` | `51.53%` | `0.94` | 1,220,000.00 USD |
| `1H` | `Gate` | `50.59%` | `49.41%` | `1.02` | 7,040,000.00 USD |
| `1H` | `Bitget` | `51.99%` | `48.01%` | `1.08` | 7,130,000.00 USD |
| `1H` | `BingX` | `54.03%` | `45.97%` | `1.18` | 1,690,000.00 USD |
| `1H` | `MEXC` | `47.46%` | `52.54%` | `0.90` | 2,950,000.00 USD |
| `1H` | `Bitunix` | `50.04%` | `49.96%` | `1.00` | 3,480,000.00 USD |
| `1H` | `Hyperliquid` | `43.54%` | `56.46%` | `0.77` | 9,550,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 3,650,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `36.03%` | `63.97%` | `0.56` | 10,130,000.00 USD |
| `1H` | `HTX` | `44.13%` | `55.87%` | `0.79` | 761,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.42%` | `46.58%` | `1.15` | 1,200,000.00 USD |
| `1H` | `Aster` | `62.33%` | `37.67%` | `1.65` | 1,040,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `40.38%` | `59.62%` | `0.68` | 1,740,000.00 USD |
| `1H` | `Whale Positions` | `48.18%` | `51.82%` | `0.93` | 104,070,000.00 USD |
| `1H` | `Global Accounts` | `47.70%` | `52.30%` | `0.91` | 228,760,000.00 USD |
| `4H` | `LINK` | `49.27%` | `50.73%` | `0.97` | 550,670,000.00 USD |
| `4H` | `Binance` | `49.9%` | `50.1%` | `1.00` | 229,860,000.00 USD |
| `4H` | `OKX` | `51.32%` | `48.68%` | `1.05` | 61,780,000.00 USD |
| `4H` | `Bybit` | `49.79%` | `50.21%` | `0.99` | 111,540,000.00 USD |
| `4H` | `KuCoin` | `55.02%` | `44.98%` | `1.22` | 2,840,000.00 USD |
| `4H` | `Gate` | `46.55%` | `53.45%` | `0.87` | 21,240,000.00 USD |
| `4H` | `Bitget` | `53.62%` | `46.38%` | `1.16` | 16,410,000.00 USD |
| `4H` | `BingX` | `38.78%` | `61.22%` | `0.63` | 8,250,000.00 USD |
| `4H` | `MEXC` | `44.14%` | `55.86%` | `0.79` | 7,740,000.00 USD |
| `4H` | `Bitunix` | `54.75%` | `45.25%` | `1.21` | 8,640,000.00 USD |
| `4H` | `Hyperliquid` | `52.84%` | `47.16%` | `1.12` | 29,710,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.33%` | `47.67%` | `1.10` | 12,610,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `31.99%` | `68.01%` | `0.47` | 29,880,000.00 USD |
| `4H` | `HTX` | `55.05%` | `44.95%` | `1.22` | 1,850,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `62.22%` | `37.78%` | `1.65` | 3,280,000.00 USD |
| `4H` | `Aster` | `65.95%` | `34.05%` | `1.94` | 2,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.74%` | `54.26%` | `0.84` | 2,400,000.00 USD |
| `4H` | `Whale Positions` | `49.9%` | `50.1%` | `1.00` | 229,860,000.00 USD |
| `4H` | `Global Accounts` | `49.27%` | `50.73%` | `0.97` | 550,670,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.00` | `11.03` | `11.00` | `11.19` | `10.87` | 17,839,722.17 USD | 8,415,517.99 USD | 9,424,204.18 USD | -1,008,686.19 USD | `-5.65%` | `9B / 18S` |
| `0:00 UTC` | `11.11` | `11.06` | `11.11` | `11.18` | `10.95` | 10,677,747.31 USD | 5,105,845.59 USD | 5,571,901.72 USD | -466,056.13 USD | `-4.36%` | `1B / 2S` |
| `5:00 UTC` | `11.18` | `11.21` | `11.18` | `11.30` | `11.14` | 5,823,506.96 USD | 2,554,704.96 USD | 3,268,802.01 USD | -714,097.05 USD | `-12.26%` | `10B / 21S` |
| `0:00 UTC` | `11.23` | `11.21` | `11.23` | `11.27` | `11.10` | 3,064,696.05 USD | 1,263,662.15 USD | 1,801,033.90 USD | -537,371.74 USD | `-17.53%` | `20B / 42S` |
| `5:00 UTC` | `11.10` | `11.09` | `11.10` | `11.13` | `11.03` | 2,476,363.14 USD | 1,173,647.56 USD | 1,302,715.59 USD | -129,068.03 USD | `-5.21%` | `19B / 14S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `11.06` | `10.85` | 9,610,457.01 USD | 3,926,356.34 USD | 5,684,100.67 USD | -1,757,744.32 USD | `-18.29%` | `3B / 20S` |
| `5:00 UTC` | `10.89` | `10.91` | `10.89` | `10.95` | `10.87` | 6,365,804.82 USD | 2,685,695.45 USD | 3,680,109.37 USD | -994,413.92 USD | `-15.62%` | `1B / 9S` |
| `0:00 UTC` | `10.83` | `10.85` | `10.83` | `10.97` | `10.79` | 25,964,116.59 USD | 9,923,976.23 USD | 16,040,140.36 USD | -6,116,164.13 USD | `-23.56%` | `4B / 36S` |
| `5:00 UTC` | `10.79` | `10.77` | `10.79` | `10.84` | `10.71` | 10,836,187.71 USD | 5,490,693.50 USD | 5,345,494.21 USD | 145,199.30 USD | `+1.34%` | `7B / 13S` |
| `0:00 UTC` | `10.71` | `10.71` | `10.71` | `10.75` | `10.67` | 1,838,899.75 USD | 691,083.24 USD | 1,147,816.52 USD | -456,733.28 USD | `-24.84%` | `5B / 20S` |

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
| `5m` | -553,550.00 USD | -749,120.00 USD | **`DISTRIBUTION`** |
| `15m` | -948,990.00 USD | -285,640.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,710,000.00 USD | -6,510,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,780,000.00 USD | -10,240,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,170,000.00 USD | -13,410,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -6,830,000.00 USD | -21,020,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,710,000.00 USD | -22,270,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -7,600,000.00 USD | -21,280,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,190,000.00 USD | -21,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,620,000.00 USD | -25,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,290,000.00 USD | -44,250,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -76,900,000.00 USD | -204,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-553.55K` | 15m=`-948.99K` | 1h=`-1.78M` | 24h=`-7.62M`
* Futures Capital Netflows: 5m=`-749.12K` | 15m=`-285.64K` | 1h=`-10.24M` | 24h=`-25.79M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.80` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.52` (Risk Distance: `0.2880` pts)
  * +2.5R Take Profit: `11.52`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.16` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.45` (Risk Distance: `0.2880` pts)
  * +2.5R Take Profit: `10.44`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.73`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
