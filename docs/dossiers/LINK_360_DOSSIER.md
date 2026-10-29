# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 04:28:57 IST` (`2026-10-29 22:58:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.66` | **Live Ask Quote**: `10.75` | **Mid Price**: `10.70`
- **Spread Points**: `87.00` | **Spread BPS**: `81.27 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.44` | VWAP Z-Score: `-2.36` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1355` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `22.65` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.30` | Lower -3.00σ Band: `10.58`
  * Upper +2.51σ Band: `12.16` | Lower -2.51σ Band: `10.72`
  * Upper +2.01σ Band: `12.01` | Lower -2.01σ Band: `10.87`
  * Upper +2.00σ Band: `12.01` | Lower -2.00σ Band: `10.87`
  * Upper +1.28σ Band: `11.81` | Lower -1.28σ Band: `11.08`
  * Upper +1.00σ Band: `11.73` | Lower -1.00σ Band: `11.16`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.00` | EMA-20=`11.22` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.42` (Slope: `+0.0000`) | EMA-100=`11.49`
  * Institutional Anchors: EMA-144=`11.50` | EMA-200=`11.48` (Slope: `-0.4257`) | EMA-233=`11.48`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.75` | Weekly High=`11.96` | Weekly Low=`10.75`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-3.77%`)
  * Point of Control (POC) = `10.81` (Distance: `-0.99%`)
  * Value Area Low (VAL) = `10.80` (Distance: `-0.92%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.62` | Weekly POC=`11.42` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.66`
  * London Session (08:00-16:00 UTC): High=`10.75` | Low=`10.66`
  * New York Session (13:00-21:00 UTC): High=`10.77` | Low=`10.64`
  * Initial Balance (First Hour): IB High=`10.74` | IB Low=`10.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.66` - `10.75`
  * Optimal Trade Entry (OTE 0.705): `10.73`
  * Structural Invalidation Anchor (0.786): `10.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.91` | `10.92` | `10.87` | `10.91` | `203,083` | 2,212,288.86 USD | -448,075.67 USD | `-20.25%` | -9,929,231.32 USD | `-0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `10.91` | `10.95` | `10.89` | `10.90` | `188,557` | 2,058,740.02 USD | -505,426.38 USD | `-24.55%` | -10,434,657.71 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `10.90` | `10.97` | `10.88` | `10.97` | `127,202` | 1,391,084.94 USD | -206,948.71 USD | `-14.88%` | -10,641,606.42 USD | `+0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.04` | `11.06` | `10.85` | `10.88` | `878,785` | 9,610,457.01 USD | -1,757,744.32 USD | `-18.29%` | -9,455,037.33 USD | `-1.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `10.88` | `10.95` | `10.87` | `10.90` | `583,779` | 6,365,804.82 USD | -994,413.92 USD | `-15.62%` | -10,449,451.25 USD | `-0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `10.90` | `10.97` | `10.88` | `10.97` | `127,202` | 1,391,084.94 USD | -206,948.71 USD | `-14.88%` | -10,656,399.96 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.69` | `11.69` | `10.87` | `10.99` | `3,805,467` | 42,673,690.41 USD | -4,269,954.14 USD | `-10.01%` | -5,856,672.77 USD | `-3.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `10.99` | `11.29` | `10.95` | `11.05` | `1,981,647` | 22,042,313.47 USD | -1,846,592.95 USD | `-8.38%` | -7,703,265.72 USD | `-1.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.06` | `10.85` | `10.96` | `1,588,256` | 17,350,790.09 USD | -2,959,011.99 USD | `-17.05%` | -10,662,277.71 USD | `-2.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.85` | `10.97` | `7,376,853` | 82,083,062.41 USD | -9,075,365.81 USD | `-11.06%` | -10,793,863.42 USD | `-2.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.85` | `10.97` | `7,376,853` | 82,083,062.41 USD | -9,075,365.81 USD | `-11.06%` | -10,793,863.42 USD | `-2.11` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.70`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

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
| `ANNOUNCEMENT` | `INFO` | `11.52` | 6,666.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.67K USD at 11.5200 USD [API] | `2026-10-28 13:52:39` |
| `ANNOUNCEMENT` | `INFO` | `13.19` | 10,315.36 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 10.32K USD at 13.1910 USD [API] | `2026-10-02 18:39:42` |
| `ANNOUNCEMENT` | `INFO` | `11.56` | 5,208.88 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.21K USD at 11.5650 USD [API] | `2026-10-28 15:01:32` |
| `ANNOUNCEMENT` | `INFO` | `11.54` | 5,267.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.27K USD at 11.5420 USD [API] | `2026-10-28 16:28:53` |
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
| `Live` | `Long Liquidation` | `9.55` | 14,810.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.61` | 5,430,000.00 USD | 5,430,000.00 USD | 486.28 USD | 0.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 5,420,000.00 USD | 5,420,000.00 USD | 10,700.00 USD | 0.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 5,410,000.00 USD | 5,410,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 10,670.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.67` | 5,390,000.00 USD | 5,390,000.00 USD | 115.45 USD | 1,920.00 USD | 8.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 5,390,000.00 USD | 5,390,000.00 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 7.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.73` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 14,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.75` | 5,460,000.00 USD | 5,460,000.00 USD | 40,030.00 USD | 434.05 USD | 13,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 156,790.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.77` | 5,400,000.00 USD | 5,400,000.00 USD | 112,940.00 USD | 7,340.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.77` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.79` | 5,260,000.00 USD | 5,260,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 5,350,000.00 USD | 5,350,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.81` | 5,250,000.00 USD | 5,250,000.00 USD | 73,100.00 USD | 18,150.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 5,300,000.00 USD | 5,300,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 5,150,000.00 USD | 5,150,000.00 USD | 37,110.00 USD | 580.25 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 5,200,000.00 USD | 5,200,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 5,160,000.00 USD | 5,160,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 118,790.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 5,100,000.00 USD | 5,100,000.00 USD | 9,950.00 USD | 146.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 5,080,000.00 USD | 5,080,000.00 USD | 17,040.00 USD | 13,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 11,990.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 5,050,000.00 USD | 5,050,000.00 USD | 13,840.00 USD | 5,540.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 5,030,000.00 USD | 5,030,000.00 USD | 9,450.00 USD | 5,730.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,080,000.00 USD | 5,080,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 829,740.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 5,850.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 598.17 USD | 154.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 6,560.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 4,970,000.00 USD | 4,970,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 660,920.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.07` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 351.10 USD | 153.34 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 4,960,000.00 USD | 4,960,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,000,000.00 USD | 5,000,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 4,960,000.00 USD | 4,960,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,000,000.00 USD | 5,000,000.00 USD | 279.85 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.13` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 4,990,000.00 USD | 4,990,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 4,940,000.00 USD | 4,940,000.00 USD | 7,090.00 USD | 0.00 USD | 62.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 4,940,000.00 USD | 4,940,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 16,120.00 USD | 797,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.17` | 4,940,000.00 USD | 4,940,000.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 4,880,000.00 USD | 4,880,000.00 USD | 65,660.00 USD | 3,240.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 4,940,000.00 USD | 4,940,000.00 USD | 1,410.00 USD | 29.65 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 4,790,000.00 USD | 4,790,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 4,930,000.00 USD | 4,930,000.00 USD | 53.57 USD | 3,080.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 4,740,000.00 USD | 4,740,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 4,920,000.00 USD | 4,920,000.00 USD | 10,890.00 USD | 7,660.00 USD | 23,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 4,630,000.00 USD | 4,630,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 4,880,000.00 USD | 4,880,000.00 USD | 26,800.00 USD | 1,680.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 4,320,000.00 USD | 4,320,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 35,850.00 USD | 781,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.27` | 4,840,000.00 USD | 4,840,000.00 USD | 18,050.00 USD | 5,870.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 4,210,000.00 USD | 4,210,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 4,810,000.00 USD | 4,810,000.00 USD | 17,890.00 USD | 6,330.00 USD | 13,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 4,020,000.00 USD | 4,020,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 4,770,000.00 USD | 4,770,000.00 USD | 24,410.00 USD | 4,350.00 USD | 10,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 3,940,000.00 USD | 3,940,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 4,730,000.00 USD | 4,730,000.00 USD | 30,780.00 USD | 9,510.00 USD | 12,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 3,750,000.00 USD | 3,750,000.00 USD | 58,810.00 USD | 28,270.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 4,680,000.00 USD | 4,680,000.00 USD | 12,800.00 USD | 4,280.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 3,640,000.00 USD | 3,640,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 6,390.00 USD | 745,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.37` | 4,650,000.00 USD | 4,650,000.00 USD | 8,240.00 USD | 7,170.00 USD | 65,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 3,570,000.00 USD | 3,570,000.00 USD | 12,950.00 USD | 12,460.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 4,570,000.00 USD | 4,570,000.00 USD | 7,450.00 USD | 6,430.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 3,520,000.00 USD | 3,520,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 4,550,000.00 USD | 4,550,000.00 USD | 259,620.00 USD | 10,890.00 USD | 39,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 3,440,000.00 USD | 3,440,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 4,240,000.00 USD | 4,240,000.00 USD | 172,340.00 USD | 35,040.00 USD | 71,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 3,300,000.00 USD | 3,300,000.00 USD | 32,710.00 USD | 22,700.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 3,960,000.00 USD | 3,960,000.00 USD | 130,840.00 USD | 18,730.00 USD | 18,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 3,230,000.00 USD | 3,230,000.00 USD | 149,660.00 USD | 48,540.00 USD | 105,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 16,050.00 USD | 738,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.47` | 3,790,000.00 USD | 3,790,000.00 USD | 219,660.00 USD | 44,830.00 USD | 77,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 2,930,000.00 USD | 2,930,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 3,450,000.00 USD | 3,450,000.00 USD | 124,820.00 USD | 16,220.00 USD | 17,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 2,620,000.00 USD | 2,620,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 3,290,000.00 USD | 3,290,000.00 USD | 27,700.00 USD | 4,710.00 USD | 13,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 2,420,000.00 USD | 2,420,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 3,250,000.00 USD | 3,250,000.00 USD | 43,880.00 USD | 5,630.00 USD | 29,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 2,330,000.00 USD | 2,330,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 3,170,000.00 USD | 3,170,000.00 USD | 7,160.00 USD | 2,280.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 2,290,000.00 USD | 2,290,000.00 USD | 55,490.00 USD | 19,150.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 439,980.00 USD | 722,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.57` | 3,160,000.00 USD | 3,160,000.00 USD | 52,260.00 USD | 37,050.00 USD | 34,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 2,200,000.00 USD | 2,200,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 3,030,000.00 USD | 3,030,000.00 USD | 48,700.00 USD | 22,500.00 USD | 98,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 2,040,000.00 USD | 2,040,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 2,860,000.00 USD | 2,860,000.00 USD | 231,320.00 USD | 12,140.00 USD | 103,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 1,940,000.00 USD | 1,940,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 2,520,000.00 USD | 2,520,000.00 USD | 464,250.00 USD | 47,160.00 USD | 117,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 1,780,000.00 USD | 1,780,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 1,890,000.00 USD | 1,890,000.00 USD | 165,270.00 USD | 54,500.00 USD | 78,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 1,680,000.00 USD | 1,680,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 156,990.00 USD | 282,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.67` | 1,590,000.00 USD | 1,590,000.00 USD | 224,600.00 USD | 20,340.00 USD | 27,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 1,610,000.00 USD | 1,610,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.69` | 1,320,000.00 USD | 1,320,000.00 USD | 425,050.00 USD | 95,980.00 USD | 143,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 1,120,000.00 USD | 1,120,000.00 USD | 383,680.00 USD | 49,270.00 USD | 45,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.71` | 653,530.00 USD | 653,530.00 USD | 223,440.00 USD | 15,350.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 642,800.00 USD | 642,800.00 USD | 238,550.00 USD | 12,470.00 USD | 73,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.73` | 411,010.00 USD | 411,010.00 USD | 8,140.00 USD | 3,750.00 USD | 37,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 318,680.00 USD | 318,680.00 USD | 28,700.00 USD | 5,730.00 USD | 173.33 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.75` | 361,400.00 USD | 361,400.00 USD | 91,880.00 USD | 5,640.00 USD | 54,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 284,070.00 USD | 284,070.00 USD | 17,290.00 USD | 4,890.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 38,850.00 USD | 125,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.77` | 209,590.00 USD | 209,590.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 243,330.00 USD | 243,330.00 USD | 16,290.00 USD | 15,910.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.79` | 200,190.00 USD | 200,190.00 USD | 88,000.00 USD | 85,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 202,270.00 USD | 202,270.00 USD | 33,460.00 USD | 59,950.00 USD | 24,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.81` | 27,080.00 USD | 27,080.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 83,900.00 USD | 83,900.00 USD | 9,380.00 USD | 0.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 14,060.00 USD | 14,060.00 USD | 13,720.00 USD | 0.00 USD | 340.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.85` | 3,640.00 USD | 3,640.00 USD | 3,420.00 USD | 0.00 USD | 222.19 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 86,340.00 USD | 87,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.87` | 209.94 USD | 209.94 USD | 0.00 USD | 0.00 USD | 209.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.91` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 0.00 USD | 225.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.93` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 622.92 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,420.00 USD | 1,420.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 12,310.00 USD | 12,310.00 USD | 7,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 677.80 USD | 677.80 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.97` | 17,140.00 USD | 17,140.00 USD | 124.21 USD | 15,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.97` | 24,990.00 USD | 24,990.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.99` | 18,610.00 USD | 18,610.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 40,600.00 USD | 40,600.00 USD | 15,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.01` | 45,360.00 USD | 45,360.00 USD | 0.00 USD | 0.00 USD | 26,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 51,190.00 USD | 51,190.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.03` | 117,050.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD | 71,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 60,560.00 USD | 60,560.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.05` | 377,640.00 USD | 377,640.00 USD | 192,840.00 USD | 2,170.00 USD | 65,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 67,090.00 USD | 67,090.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.05` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.07` | 908,470.00 USD | 908,470.00 USD | 435,240.00 USD | 16,820.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 74,600.00 USD | 74,600.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 1,110,000.00 USD | 1,110,000.00 USD | 126,930.00 USD | 34,010.00 USD | 40,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 82,100.00 USD | 82,100.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 1,360,000.00 USD | 1,360,000.00 USD | 216,430.00 USD | 18,460.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 507,900.00 USD | 507,900.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 1,990,000.00 USD | 1,990,000.00 USD | 408,510.00 USD | 85,870.00 USD | 132,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 967,940.00 USD | 967,940.00 USD | 372,210.00 USD | 48,150.00 USD | 39,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 2,190,000.00 USD | 2,190,000.00 USD | 194,240.00 USD | 13,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 1,260,000.00 USD | 1,260,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 2,260,000.00 USD | 2,260,000.00 USD | 165.70 USD | 51,630.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 1,260,000.00 USD | 1,260,000.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 2,400,000.00 USD | 2,400,000.00 USD | 72,110.00 USD | 63,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 2,590,000.00 USD | 2,590,000.00 USD | 112,460.00 USD | 0.00 USD | 76,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 1,580,000.00 USD | 1,580,000.00 USD | 311,160.00 USD | 698.80 USD | 17.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 2,890,000.00 USD | 2,890,000.00 USD | 191,590.00 USD | 1,250.00 USD | 107,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 1,880,000.00 USD | 1,880,000.00 USD | 241,160.00 USD | 59,950.00 USD | 25.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 3,130,000.00 USD | 3,130,000.00 USD | 90,500.00 USD | 39,800.00 USD | 114,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 2,340,000.00 USD | 2,340,000.00 USD | 330,300.00 USD | 0.00 USD | 129,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 2,420.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.27` | 3,610,000.00 USD | 3,610,000.00 USD | 304,550.00 USD | 2,670.00 USD | 175,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 2,780,000.00 USD | 2,780,000.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 4,110,000.00 USD | 4,110,000.00 USD | 163,770.00 USD | 122,050.00 USD | 213,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 3,000,000.00 USD | 3,000,000.00 USD | 104,970.00 USD | 57,050.00 USD | 56,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 4,330,000.00 USD | 4,330,000.00 USD | 63,250.00 USD | 69,420.00 USD | 79,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 3,310,000.00 USD | 3,310,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 4,590,000.00 USD | 4,590,000.00 USD | 198,020.00 USD | 37,890.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 3,670,000.00 USD | 3,670,000.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 5,090,000.00 USD | 5,090,000.00 USD | 300,200.00 USD | 125,560.00 USD | 66,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 3,950,000.00 USD | 3,950,000.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.37` | 5,340,000.00 USD | 5,340,000.00 USD | 150,920.00 USD | 80,560.00 USD | 22,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 4,270,000.00 USD | 4,270,000.00 USD | 110,820.00 USD | 72,750.00 USD | 131,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 5,390,000.00 USD | 5,390,000.00 USD | 1,530.00 USD | 36,100.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 5,650,000.00 USD | 5,650,000.00 USD | 91,890.00 USD | 34,170.00 USD | 140,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 16,010.00 USD | 34,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 5,820,000.00 USD | 5,820,000.00 USD | 52,230.00 USD | 25,530.00 USD | 88,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 4,640,000.00 USD | 4,640,000.00 USD | 138,950.00 USD | 52,330.00 USD | 91,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 5,930,000.00 USD | 5,930,000.00 USD | 44,620.00 USD | 70,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 4,950,000.00 USD | 4,950,000.00 USD | 203,890.00 USD | 68,950.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.47` | 6,020,000.00 USD | 6,020,000.00 USD | 47,140.00 USD | 19,290.00 USD | 23,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 5,040,000.00 USD | 5,040,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 6,110,000.00 USD | 6,110,000.00 USD | 33,390.00 USD | 22,220.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 5,180,000.00 USD | 5,180,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 6,210,000.00 USD | 6,210,000.00 USD | 41,360.00 USD | 27,210.00 USD | 30,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 5,250,000.00 USD | 5,250,000.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 6,290,000.00 USD | 6,290,000.00 USD | 32,640.00 USD | 17,750.00 USD | 29,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 5,340,000.00 USD | 5,340,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 6,330,000.00 USD | 6,330,000.00 USD | 22,840.00 USD | 407.50 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.57` | 6,440,000.00 USD | 6,440,000.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 6,500,000.00 USD | 6,500,000.00 USD | 15,100.00 USD | 7,830.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 6,730,000.00 USD | 6,730,000.00 USD | 153,200.00 USD | 260.05 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 5,480,000.00 USD | 5,480,000.00 USD | 44,670.00 USD | 10,190.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 6,750,000.00 USD | 6,750,000.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 5,520,000.00 USD | 5,520,000.00 USD | 43,680.00 USD | 0.00 USD | 309.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 6,750,000.00 USD | 6,750,000.00 USD | 1,410.00 USD | 386.12 USD | 46.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 877.75 USD | 18,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 5,600.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.67` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.67` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 6,840,000.00 USD | 6,840,000.00 USD | 59,600.00 USD | 29,150.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 6,990,000.00 USD | 6,990,000.00 USD | 138,560.00 USD | 13,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 5,820,000.00 USD | 5,820,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 7,130,000.00 USD | 7,130,000.00 USD | 98,180.00 USD | 495.80 USD | 41,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 7,240,000.00 USD | 7,240,000.00 USD | 20,910.00 USD | 31,550.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 5,860,000.00 USD | 5,860,000.00 USD | 17,390.00 USD | 0.00 USD | 547.35 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 62,000.00 USD | 72,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.77` | 7,300,000.00 USD | 7,300,000.00 USD | 40,510.00 USD | 18,010.00 USD | 177.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 6,000,000.00 USD | 6,000,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 7,350,000.00 USD | 7,350,000.00 USD | 11,110.00 USD | 0.00 USD | 40,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 6,080,000.00 USD | 6,080,000.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 15,660.00 USD | 327.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 6,240,000.00 USD | 6,240,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 7,410,000.00 USD | 7,410,000.00 USD | 11,070.00 USD | 12,530.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 6,370,000.00 USD | 6,370,000.00 USD | 81,180.00 USD | 45,270.00 USD | 441.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 7,590,000.00 USD | 7,590,000.00 USD | 76,700.00 USD | 21,690.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 6,590,000.00 USD | 6,590,000.00 USD | 178,690.00 USD | 39,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 7,680,000.00 USD | 7,680,000.00 USD | 19,640.00 USD | 25,210.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 6,610,000.00 USD | 6,610,000.00 USD | 438.10 USD | 4,980.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 7,760,000.00 USD | 7,760,000.00 USD | 44,160.00 USD | 12,100.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 6,670,000.00 USD | 6,670,000.00 USD | 40,020.00 USD | 15,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 7,910,000.00 USD | 7,910,000.00 USD | 102,960.00 USD | 18,980.00 USD | 31,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 6,750,000.00 USD | 6,750,000.00 USD | 82,030.00 USD | 0.00 USD | 35.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 8,110,000.00 USD | 8,110,000.00 USD | 135,130.00 USD | 28,490.00 USD | 28,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 6,820,000.00 USD | 6,820,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 8,250,000.00 USD | 8,250,000.00 USD | 85,850.00 USD | 18,280.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 7,070,000.00 USD | 7,070,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 8,460,000.00 USD | 8,460,000.00 USD | 77,200.00 USD | 36,400.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 7,730,000.00 USD | 7,730,000.00 USD | 403,040.00 USD | 35,810.00 USD | 223,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 8,660,000.00 USD | 8,660,000.00 USD | 123,700.00 USD | 25,550.00 USD | 46,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 8,200,000.00 USD | 8,200,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 8,780,000.00 USD | 8,780,000.00 USD | 60,120.00 USD | 12,220.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 8,660,000.00 USD | 8,660,000.00 USD | 204,590.00 USD | 6,390.00 USD | 247,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 8,950,000.00 USD | 8,950,000.00 USD | 88,410.00 USD | 43,040.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 9,350,000.00 USD | 9,350,000.00 USD | 347,250.00 USD | 140,540.00 USD | 205,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 9,310,000.00 USD | 9,310,000.00 USD | 211,220.00 USD | 59,410.00 USD | 90,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 10,000,000.00 USD | 10,000,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.07` | 9,580,000.00 USD | 9,580,000.00 USD | 114,130.00 USD | 52,960.00 USD | 97,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 10,570,000.00 USD | 10,570,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 9,630,000.00 USD | 9,630,000.00 USD | 17,390.00 USD | 18,150.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 10,870,000.00 USD | 10,870,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 9,820,000.00 USD | 9,820,000.00 USD | 94,540.00 USD | 34,450.00 USD | 55,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 11,150,000.00 USD | 11,150,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 9,980,000.00 USD | 9,980,000.00 USD | 94,650.00 USD | 34,210.00 USD | 39,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 11,420,000.00 USD | 11,420,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 10,210,000.00 USD | 10,210,000.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 12,020,000.00 USD | 12,020,000.00 USD | 325,540.00 USD | 125,190.00 USD | 144,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.17` | 10,460,000.00 USD | 10,460,000.00 USD | 122,970.00 USD | 63,760.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 12,170,000.00 USD | 12,170,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 10,560,000.00 USD | 10,560,000.00 USD | 64,080.00 USD | 23,440.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 12,500,000.00 USD | 12,500,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 10,700,000.00 USD | 10,700,000.00 USD | 52,950.00 USD | 28,910.00 USD | 50,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 12,910,000.00 USD | 12,910,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 10,740,000.00 USD | 10,740,000.00 USD | 14,580.00 USD | 24,860.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 13,130,000.00 USD | 13,130,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 10,760,000.00 USD | 10,760,000.00 USD | 6,540.00 USD | 5,600.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 13,420,000.00 USD | 13,420,000.00 USD | 136,810.00 USD | 56,100.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,010.00 USD | 73,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.27` | 10,850,000.00 USD | 10,850,000.00 USD | 52,420.00 USD | 9,860.00 USD | 22,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 13,650,000.00 USD | 13,650,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 10,940,000.00 USD | 10,940,000.00 USD | 38,460.00 USD | 19,790.00 USD | 34,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 14,170,000.00 USD | 14,170,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 10,970,000.00 USD | 10,970,000.00 USD | 19,750.00 USD | 4,950.00 USD | 9,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 14,410,000.00 USD | 14,410,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 10,980,000.00 USD | 10,980,000.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 14,680,000.00 USD | 14,680,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 11,020,000.00 USD | 11,020,000.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 14,820,000.00 USD | 14,820,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 73,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.37` | 11,040,000.00 USD | 11,040,000.00 USD | 8,820.00 USD | 5,700.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 14,890,000.00 USD | 14,890,000.00 USD | 32,750.00 USD | 24,190.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 11,100,000.00 USD | 11,100,000.00 USD | 28,580.00 USD | 12,560.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 15,230,000.00 USD | 15,230,000.00 USD | 122,920.00 USD | 42,040.00 USD | 174,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 11,190,000.00 USD | 11,190,000.00 USD | 42,540.00 USD | 19,880.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 15,430,000.00 USD | 15,430,000.00 USD | 58,100.00 USD | 25,020.00 USD | 114,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 11,220,000.00 USD | 11,220,000.00 USD | 23,090.00 USD | 5,940.00 USD | 196.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 16,020,000.00 USD | 16,020,000.00 USD | 237,780.00 USD | 22,230.00 USD | 333,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 11,240,000.00 USD | 11,240,000.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 16,440,000.00 USD | 16,440,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 12,000.00 USD | 12,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 16,590,000.00 USD | 16,590,000.00 USD | 45,860.00 USD | 29,080.00 USD | 76,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 16,760,000.00 USD | 16,760,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 17,010,000.00 USD | 17,010,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 17,320,000.00 USD | 17,320,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 17,560,000.00 USD | 17,560,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 242.22 USD | 74,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.57` | 17,750,000.00 USD | 17,750,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 17,870,000.00 USD | 17,870,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 18,000,000.00 USD | 18,000,000.00 USD | 41,220.00 USD | 29,270.00 USD | 58,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 18,170,000.00 USD | 18,170,000.00 USD | 64,120.00 USD | 28,270.00 USD | 81,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 18,270,000.00 USD | 18,270,000.00 USD | 57,370.00 USD | 26,110.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 18,560,000.00 USD | 18,560,000.00 USD | 54,670.00 USD | 16,240.00 USD | 223,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 18,800,000.00 USD | 18,800,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 18,890,000.00 USD | 18,890,000.00 USD | 21,450.00 USD | 43,220.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 18,980,000.00 USD | 18,980,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 19,050,000.00 USD | 19,050,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.75` | 531.68 USD | 74,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.77` | 19,140,000.00 USD | 19,140,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 19,230,000.00 USD | 19,230,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 19,250,000.00 USD | 19,250,000.00 USD | 7,760.00 USD | 0.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 19,280,000.00 USD | 19,280,000.00 USD | 15,730.00 USD | 183.20 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 19,360,000.00 USD | 19,360,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 1,760.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.87` | 19,400,000.00 USD | 19,400,000.00 USD | 9,820.00 USD | 6,560.00 USD | 21,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 19,490,000.00 USD | 19,490,000.00 USD | 48,720.00 USD | 18,800.00 USD | 20,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 19,590,000.00 USD | 19,590,000.00 USD | 59,260.00 USD | 15,540.00 USD | 23,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 19,610,000.00 USD | 19,610,000.00 USD | 26,330.00 USD | 231.70 USD | 43.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 19,630,000.00 USD | 19,630,000.00 USD | 1,920.00 USD | 9,210.00 USD | 4,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 19,660,000.00 USD | 19,660,000.00 USD | 13,890.00 USD | 10,560.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 19,740,000.00 USD | 19,740,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 19,740,000.00 USD | 19,740,000.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 19,750,000.00 USD | 19,750,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 19,750,000.00 USD | 19,750,000.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.07` | 19,800,000.00 USD | 19,800,000.00 USD | 23,750.00 USD | 6,890.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 19,820,000.00 USD | 19,820,000.00 USD | 16,060.00 USD | 527.72 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 19,850,000.00 USD | 19,850,000.00 USD | 19,270.00 USD | 5,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 19,870,000.00 USD | 19,870,000.00 USD | 13,360.00 USD | 4,010.00 USD | 21.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.17` | 19,880,000.00 USD | 19,880,000.00 USD | 0.00 USD | 3,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 19,890,000.00 USD | 19,890,000.00 USD | 972.55 USD | 0.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 19,920,000.00 USD | 19,920,000.00 USD | 13,890.00 USD | 6,210.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 19,930,000.00 USD | 19,930,000.00 USD | 10,840.00 USD | 146.97 USD | 37.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 20,000,000.00 USD | 20,000,000.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 20,030,000.00 USD | 20,030,000.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 20,040,000.00 USD | 20,040,000.00 USD | 6,180.00 USD | 2,560.00 USD | 17.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 20,070,000.00 USD | 20,070,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 20,070,000.00 USD | 20,070,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.35` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 158.65 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `2.15` | 12,680,000.00 USD | 0.00 USD | 3,150.00 USD | `-80.54%` | `1,466,000.00` |
| `Live` | `Long` | `2.45` | 12,670,000.00 USD | 0.00 USD | 1,850.00 USD | `-77.83%` | `756,900.00` |
| `Live` | `Long` | `2.55` | 12,670,000.00 USD | 0.00 USD | 25,070.00 USD | `-76.93%` | `9,829,500.00` |
| `Live` | `Long` | `2.65` | 12,650,000.00 USD | 0.00 USD | 2,550.00 USD | `-76.02%` | `961,300.00` |
| `Live` | `Long` | `2.95` | 12,640,000.00 USD | 0.00 USD | 9,610.00 USD | `-73.31%` | `3,259,000.00` |
| `Live` | `Long` | `3.05` | 12,630,000.00 USD | 0.00 USD | 6,640.00 USD | `-72.40%` | `2,176,000.00` |
| `Live` | `Long` | `3.15` | 12,630,000.00 USD | 0.00 USD | 297.99 USD | `-71.50%` | `94,600.00` |
| `Live` | `Long` | `3.25` | 12,630,000.00 USD | 0.00 USD | 2,990.00 USD | `-70.59%` | `920,000.00` |
| `Live` | `Long` | `3.35` | 12,620,000.00 USD | 0.00 USD | 796.30 USD | `-69.69%` | `237,700.00` |
| `Live` | `Long` | `3.45` | 12,620,000.00 USD | 0.00 USD | 10,470.00 USD | `-68.78%` | `3,034,300.00` |
| `Live` | `Long` | `3.65` | 12,610,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.97%` | `600,000.00` |
| `Live` | `Long` | `3.75` | 12,610,000.00 USD | 0.00 USD | 4,710.00 USD | `-66.07%` | `1,255,000.00` |
| `Live` | `Long` | `3.85` | 12,610,000.00 USD | 0.00 USD | 713.79 USD | `-65.16%` | `185,400.00` |
| `Live` | `Long` | `3.95` | 12,610,000.00 USD | 0.00 USD | 40,120.00 USD | `-64.26%` | `10,155,700.00` |
| `Live` | `Long` | `4.05` | 12,570,000.00 USD | 0.00 USD | 950.54 USD | `-63.35%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,560,000.00 USD | 0.00 USD | 251.91 USD | `-62.45%` | `60,700.00` |
| `Live` | `Long` | `4.25` | 12,560,000.00 USD | 0.00 USD | 11,890.00 USD | `-61.54%` | `2,797,900.00` |
| `Live` | `Long` | `4.35` | 12,550,000.00 USD | 0.00 USD | 1,490.00 USD | `-60.64%` | `341,500.00` |
| `Live` | `Long` | `4.45` | 12,550,000.00 USD | 0.00 USD | 381.37 USD | `-59.73%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 12,550,000.00 USD | 0.00 USD | 4,190.00 USD | `-58.83%` | `919,800.00` |
| `Live` | `Long` | `4.65` | 12,550,000.00 USD | 0.00 USD | 383.63 USD | `-57.92%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 12,550,000.00 USD | 0.00 USD | 237,160.00 USD | `-57.02%` | `49,928,100.00` |
| `Live` | `Long` | `4.85` | 12,310,000.00 USD | 0.00 USD | 1,620.00 USD | `-56.11%` | `334,900.00` |
| `Live` | `Long` | `4.95` | 12,310,000.00 USD | 0.00 USD | 883.08 USD | `-55.21%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 12,310,000.00 USD | 0.00 USD | 9,450.00 USD | `-54.30%` | `1,871,300.00` |
| `Live` | `Long` | `5.15` | 12,300,000.00 USD | 0.00 USD | 266.26 USD | `-53.40%` | `51,700.00` |
| `Live` | `Long` | `5.25` | 12,300,000.00 USD | 0.00 USD | 886.73 USD | `-52.49%` | `168,900.00` |
| `Live` | `Long` | `5.35` | 12,300,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.59%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,750,000.00 USD | 0.00 USD | 16,490.00 USD | `-50.68%` | `3,025,500.00` |
| `Live` | `Long` | `5.55` | 11,740,000.00 USD | 0.00 USD | 2,750.00 USD | `-49.78%` | `495,200.00` |
| `Live` | `Long` | `5.65` | 11,730,000.00 USD | 0.00 USD | 35,720.00 USD | `-48.87%` | `6,321,800.00` |
| `Live` | `Long` | `5.75` | 11,700,000.00 USD | 0.00 USD | 102,400.00 USD | `-47.97%` | `17,809,500.00` |
| `Live` | `Long` | `5.85` | 11,600,000.00 USD | 0.00 USD | 20,170.00 USD | `-47.06%` | `3,447,900.00` |
| `Live` | `Long` | `5.95` | 11,580,000.00 USD | 0.00 USD | 5,690.00 USD | `-46.16%` | `956,800.00` |
| `Live` | `Long` | `6.05` | 11,570,000.00 USD | 0.00 USD | 68,200.00 USD | `-45.25%` | `11,272,000.00` |
| `Live` | `Long` | `6.15` | 11,500,000.00 USD | 0.00 USD | 6,240.00 USD | `-44.35%` | `1,013,900.00` |
| `Live` | `Long` | `6.25` | 11,500,000.00 USD | 0.00 USD | 88,130.00 USD | `-43.44%` | `14,101,300.00` |
| `Live` | `Long` | `6.35` | 11,410,000.00 USD | 0.00 USD | 15,990.00 USD | `-42.54%` | `2,518,400.00` |
| `Live` | `Long` | `6.45` | 11,390,000.00 USD | 0.00 USD | 16,300.00 USD | `-41.63%` | `2,527,100.00` |
| `Live` | `Long` | `6.55` | 11,380,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.73%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 11,370,000.00 USD | 0.00 USD | 9,260.00 USD | `-39.82%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 11,360,000.00 USD | 0.00 USD | 3,350.00 USD | `-38.92%` | `496,500.00` |
| `Live` | `Long` | `6.85` | 11,360,000.00 USD | 0.00 USD | 71,320.00 USD | `-38.01%` | `10,412,100.00` |
| `Live` | `Long` | `6.95` | 11,290,000.00 USD | 0.00 USD | 810.37 USD | `-37.11%` | `116,600.00` |
| `Live` | `Long` | `7.05` | 11,290,000.00 USD | 0.00 USD | 2,560.00 USD | `-36.20%` | `363,400.00` |
| `Live` | `Long` | `7.15` | 11,290,000.00 USD | 0.00 USD | 42,950.00 USD | `-35.30%` | `6,007,300.00` |
| `Live` | `Long` | `7.25` | 11,240,000.00 USD | 0.00 USD | 10,500.00 USD | `-34.40%` | `1,448,500.00` |
| `Live` | `Long` | `7.35` | 11,230,000.00 USD | 0.00 USD | 33,870.00 USD | `-33.49%` | `4,607,900.00` |
| `Live` | `Long` | `7.45` | 11,200,000.00 USD | 0.00 USD | 6,280.00 USD | `-32.59%` | `843,100.00` |
| `Live` | `Long` | `7.55` | 11,190,000.00 USD | 0.00 USD | 17,880.00 USD | `-31.68%` | `2,368,600.00` |
| `Live` | `Long` | `7.65` | 11,170,000.00 USD | 0.00 USD | 52,770.00 USD | `-30.78%` | `6,897,400.00` |
| `Live` | `Long` | `7.75` | 11,120,000.00 USD | 0.00 USD | 14,300.00 USD | `-29.87%` | `1,844,600.00` |
| `Live` | `Long` | `7.85` | 11,110,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-28.97%` | `165,733,400.00` |
| `Live` | `Long` | `7.95` | 9,810,000.00 USD | 0.00 USD | 13,390.00 USD | `-28.06%` | `1,684,800.00` |
| `Live` | `Long` | `8.05` | 9,790,000.00 USD | 0.00 USD | 65,630.00 USD | `-27.16%` | `8,152,700.00` |
| `Live` | `Long` | `8.15` | 9,730,000.00 USD | 0.00 USD | 193,680.00 USD | `-26.25%` | `23,764,700.00` |
| `Live` | `Long` | `8.25` | 9,530,000.00 USD | 0.00 USD | 42,600.00 USD | `-25.35%` | `5,163,100.00` |
| `Live` | `Long` | `8.35` | 9,490,000.00 USD | 0.00 USD | 12,890.00 USD | `-24.44%` | `1,543,700.00` |
| `Live` | `Long` | `8.45` | 9,480,000.00 USD | 0.00 USD | 14,470.00 USD | `-23.54%` | `1,712,400.00` |
| `Live` | `Long` | `8.55` | 9,460,000.00 USD | 0.00 USD | 17,800.00 USD | `-22.63%` | `2,082,000.00` |
| `Live` | `Long` | `8.65` | 9,450,000.00 USD | 0.00 USD | 19,940.00 USD | `-21.73%` | `2,305,500.00` |
| `Live` | `Long` | `8.75` | 9,430,000.00 USD | 0.00 USD | 308,140.00 USD | `-20.82%` | `35,215,700.00` |
| `Live` | `Long` | `8.85` | 9,120,000.00 USD | 0.00 USD | 28,570.00 USD | `-19.92%` | `3,228,700.00` |
| `Live` | `Long` | `8.95` | 9,090,000.00 USD | 0.00 USD | 457,490.00 USD | `-19.01%` | `51,116,100.00` |
| `Live` | `Long` | `9.05` | 8,630,000.00 USD | 0.00 USD | 66,460.00 USD | `-18.11%` | `7,343,500.00` |
| `Live` | `Long` | `9.15` | 8,560,000.00 USD | 0.00 USD | 3,770,000.00 USD | `-17.20%` | `412,377,300.00` |
| `Live` | `Long` | `9.25` | 4,790,000.00 USD | 0.00 USD | 5,600.00 USD | `-16.30%` | `605,100.00` |
| `Live` | `Long` | `9.35` | 4,790,000.00 USD | 0.00 USD | 2,160,000.00 USD | `-15.39%` | `231,375,700.00` |
| `Live` | `Long` | `9.45` | 2,620,000.00 USD | 0.00 USD | 33,630.00 USD | `-14.49%` | `3,558,800.00` |
| `Live` | `Long` | `9.55` | 2,590,000.00 USD | 0.00 USD | 14,810.00 USD | `-13.58%` | `1,550,700.00` |
| `Live` | `Long` | `9.65` | 2,570,000.00 USD | 0.00 USD | 10,670.00 USD | `-12.68%` | `1,106,100.00` |
| `Live` | `Long` | `9.75` | 2,560,000.00 USD | 0.00 USD | 156,790.00 USD | `-11.77%` | `16,081,200.00` |
| `Live` | `Long` | `9.85` | 2,410,000.00 USD | 0.00 USD | 118,790.00 USD | `-10.87%` | `12,060,100.00` |
| `Live` | `Long` | `9.95` | 2,290,000.00 USD | 0.00 USD | 829,740.00 USD | `-9.96%` | `83,391,300.00` |
| `Live` | `Long` | `10.05` | 1,460,000.00 USD | 0.00 USD | 660,920.00 USD | `-9.06%` | `65,763,600.00` |
| `Live` | `Long` | `10.15` | 797,240.00 USD | 0.00 USD | 16,120.00 USD | `-8.15%` | `1,588,300.00` |
| `Live` | `Long` | `10.25` | 781,120.00 USD | 0.00 USD | 35,850.00 USD | `-7.25%` | `3,497,200.00` |
| `Live` | `Long` | `10.35` | 745,280.00 USD | 0.00 USD | 6,390.00 USD | `-6.34%` | `617,200.00` |
| `Live` | `Long` | `10.45` | 738,890.00 USD | 0.00 USD | 16,050.00 USD | `-5.44%` | `1,535,700.00` |
| `Live` | `Long` | `10.55` | 722,840.00 USD | 0.00 USD | 439,980.00 USD | `-4.53%` | `41,704,600.00` |
| `Live` | `Long` | `10.65` | 282,860.00 USD | 0.00 USD | 156,990.00 USD | `-3.63%` | `14,741,200.00` |
| `Live` | `Long` | `10.75` | 125,860.00 USD | 0.00 USD | 38,850.00 USD | `-2.72%` | `3,613,800.00` |
| `Live` | `Long` | `10.85` | 87,020.00 USD | 0.00 USD | 86,340.00 USD | `-1.82%` | `7,957,400.00` |
| `Live` | `Long` | `10.95` | 677.80 USD | 0.00 USD | 677.80 USD | `-0.91%` | `61,900.00` |
| `Live` | `Short` | `11.05` | 2,160.00 USD | 2,160.00 USD | 0.00 USD | `-0.01%` | `195,300.00` |
| `Live` | `Short` | `11.25` | 4,580.00 USD | 2,420.00 USD | 0.00 USD | `+1.80%` | `215,000.00` |
| `Live` | `Short` | `11.65` | 10,180.00 USD | 5,600.00 USD | 0.00 USD | `+5.42%` | `480,700.00` |
| `Live` | `Short` | `11.75` | 72,180.00 USD | 62,000.00 USD | 0.00 USD | `+6.33%` | `5,276,800.00` |
| `Live` | `Short` | `12.25` | 73,190.00 USD | 1,010.00 USD | 0.00 USD | `+10.85%` | `82,200.00` |
| `Live` | `Short` | `12.35` | 73,920.00 USD | 736.06 USD | 0.00 USD | `+11.75%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 74,160.00 USD | 242.22 USD | 0.00 USD | `+13.56%` | `19,300.00` |
| `Live` | `Short` | `12.75` | 74,700.00 USD | 531.68 USD | 0.00 USD | `+15.37%` | `41,700.00` |
| `Live` | `Short` | `12.85` | 76,450.00 USD | 1,760.00 USD | 0.00 USD | `+16.28%` | `136,700.00` |
| `Live` | `Short` | `13.45` | 81,740.00 USD | 5,280.00 USD | 0.00 USD | `+21.71%` | `392,900.00` |
| `Live` | `Short` | `13.55` | 83,330.00 USD | 1,590.00 USD | 0.00 USD | `+22.61%` | `117,500.00` |
| `Live` | `Short` | `14.05` | 83,430.00 USD | 102.56 USD | 0.00 USD | `+27.14%` | `7,300.00` |
| `Live` | `Short` | `14.15` | 83,780.00 USD | 349.51 USD | 0.00 USD | `+28.04%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 84,330.00 USD | 544.35 USD | 0.00 USD | `+28.95%` | `38,200.00` |
| `Live` | `Short` | `14.45` | 84,600.00 USD | 276.00 USD | 0.00 USD | `+30.76%` | `19,100.00` |
| `Live` | `Short` | `14.75` | 84,920.00 USD | 321.55 USD | 0.00 USD | `+33.47%` | `21,800.00` |
| `Live` | `Short` | `14.95` | 110,260.00 USD | 25,330.00 USD | 0.00 USD | `+35.28%` | `1,694,600.00` |
| `Live` | `Short` | `15.15` | 172,760.00 USD | 62,510.00 USD | 0.00 USD | `+37.09%` | `4,125,800.00` |
| `Live` | `Short` | `15.25` | 172,920.00 USD | 155.55 USD | 0.00 USD | `+38.00%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 173,760.00 USD | 838.14 USD | 0.00 USD | `+40.71%` | `53,900.00` |
| `Live` | `Short` | `15.65` | 174,040.00 USD | 284.83 USD | 0.00 USD | `+41.62%` | `18,200.00` |
| `Live` | `Short` | `15.85` | 174,310.00 USD | 271.04 USD | 0.00 USD | `+43.43%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 174,450.00 USD | 138.76 USD | 0.00 USD | `+44.33%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 175,850.00 USD | 1,390.00 USD | 0.00 USD | `+47.95%` | `85,300.00` |
| `Live` | `Short` | `16.75` | 193,570.00 USD | 17,720.00 USD | 0.00 USD | `+51.57%` | `1,058,000.00` |
| `Live` | `Short` | `16.95` | 284,170.00 USD | 90,600.00 USD | 0.00 USD | `+53.38%` | `5,345,300.00` |
| `Live` | `Short` | `17.15` | 286,510.00 USD | 2,330.00 USD | 0.00 USD | `+55.19%` | `136,100.00` |
| `Live` | `Short` | `17.45` | 381,520.00 USD | 95,020.00 USD | 0.00 USD | `+57.90%` | `5,445,000.00` |
| `Live` | `Short` | `17.55` | 382,910.00 USD | 1,390.00 USD | 0.00 USD | `+58.81%` | `79,100.00` |
| `Live` | `Short` | `17.75` | 410,230.00 USD | 27,320.00 USD | 0.00 USD | `+60.62%` | `1,539,000.00` |
| `Live` | `Short` | `17.85` | 659,800.00 USD | 249,580.00 USD | 0.00 USD | `+61.52%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 660,160.00 USD | 351.82 USD | 0.00 USD | `+62.43%` | `19,600.00` |
| `Live` | `Short` | `18.05` | 667,710.00 USD | 7,550.00 USD | 0.00 USD | `+63.33%` | `418,300.00` |
| `Live` | `Short` | `18.25` | 676,120.00 USD | 8,420.00 USD | 0.00 USD | `+65.14%` | `461,100.00` |
| `Live` | `Short` | `18.35` | 676,240.00 USD | 121.11 USD | 0.00 USD | `+66.05%` | `6,600.00` |
| `Live` | `Short` | `18.45` | 680,130.00 USD | 3,890.00 USD | 0.00 USD | `+66.95%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 710,450.00 USD | 30,310.00 USD | 0.00 USD | `+67.86%` | `1,634,200.00` |
| `Live` | `Short` | `18.65` | 710,630.00 USD | 186.50 USD | 0.00 USD | `+68.76%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 726,710.00 USD | 16,080.00 USD | 0.00 USD | `+69.67%` | `857,700.00` |
| `Live` | `Short` | `18.85` | 727,170.00 USD | 456.17 USD | 0.00 USD | `+70.57%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 800,980.00 USD | 73,810.00 USD | 0.00 USD | `+71.48%` | `3,895,000.00` |
| `Live` | `Short` | `19.05` | 1,520,000.00 USD | 718,380.00 USD | 0.00 USD | `+72.38%` | `37,710,000.00` |
| `Live` | `Short` | `19.55` | 2,340,000.00 USD | 820,020.00 USD | 0.00 USD | `+76.91%` | `41,944,600.00` |
| `Live` | `Short` | `19.65` | 2,380,000.00 USD | 38,790.00 USD | 0.00 USD | `+77.81%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,380,000.00 USD | 291.27 USD | 0.00 USD | `+80.53%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 4,700,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+82.34%` | `115,024,600.00` |
| `Live` | `Short` | `20.55` | 4,700,000.00 USD | 7,250.00 USD | 0.00 USD | `+85.96%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 4,710,000.00 USD | 2,040.00 USD | 0.00 USD | `+88.67%` | `97,800.00` |
| `Live` | `Short` | `21.05` | 4,710,000.00 USD | 5,700.00 USD | 0.00 USD | `+90.48%` | `270,600.00` |
| `Live` | `Short` | `21.35` | 4,710,000.00 USD | 3,680.00 USD | 0.00 USD | `+93.20%` | `172,500.00` |
| `Live` | `Short` | `21.85` | 4,720,000.00 USD | 2,740.00 USD | 0.00 USD | `+97.72%` | `125,600.00` |
| `Live` | `Short` | `21.95` | 4,720,000.00 USD | 140.48 USD | 0.00 USD | `+98.62%` | `6,400.00` |
| `Live` | `Short` | `22.05` | 4,720,000.00 USD | 1,020.00 USD | 0.00 USD | `+99.53%` | `46,100.00` |
| `Live` | `Short` | `22.15` | 4,730,000.00 USD | 16,090.00 USD | 0.00 USD | `+100.43%` | `726,300.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 635,490.00 USD | 0.00 USD | 431.68 USD | `-67.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 635,060.00 USD | 0.00 USD | 290.29 USD | `-58.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 634,770.00 USD | 0.00 USD | 120.22 USD | `-52.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 634,650.00 USD | 0.00 USD | 107.09 USD | `-45.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 634,540.00 USD | 0.00 USD | 4,260.00 USD | `-40.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 630,280.00 USD | 0.00 USD | 133.00 USD | `-39.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 630,150.00 USD | 0.00 USD | 3,770.00 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 626,380.00 USD | 0.00 USD | 2,070.00 USD | `-34.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 624,310.00 USD | 0.00 USD | 3,740.00 USD | `-32.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 620,570.00 USD | 0.00 USD | 1,050.00 USD | `-31.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 619,510.00 USD | 0.00 USD | 146.80 USD | `-28.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 619,370.00 USD | 0.00 USD | 5,000.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 614,360.00 USD | 0.00 USD | 564.79 USD | `-26.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 613,800.00 USD | 0.00 USD | 10,660.00 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 603,140.00 USD | 0.00 USD | 1,360.00 USD | `-23.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 601,780.00 USD | 0.00 USD | 52,990.00 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 548,790.00 USD | 0.00 USD | 186.84 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 548,610.00 USD | 0.00 USD | 742.88 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 547,860.00 USD | 0.00 USD | 196.47 USD | `-19.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 547,670.00 USD | 0.00 USD | 1,320.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 546,350.00 USD | 0.00 USD | 2,240.00 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 544,110.00 USD | 0.00 USD | 194.90 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 543,910.00 USD | 0.00 USD | 4,940.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 538,970.00 USD | 0.00 USD | 2,090.00 USD | `-14.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 536,880.00 USD | 0.00 USD | 10,530.00 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 526,350.00 USD | 0.00 USD | 3,550.00 USD | `-12.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 522,800.00 USD | 0.00 USD | 6,490.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 516,310.00 USD | 0.00 USD | 23,380.00 USD | `-10.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 492,930.00 USD | 0.00 USD | 300,150.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 192,780.00 USD | 0.00 USD | 2,590.00 USD | `-9.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 190,190.00 USD | 0.00 USD | 1,050.00 USD | `-8.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 189,140.00 USD | 0.00 USD | 93,280.00 USD | `-7.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 95,860.00 USD | 0.00 USD | 7,430.00 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 88,430.00 USD | 0.00 USD | 31,450.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 56,980.00 USD | 0.00 USD | 25,350.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 31,630.00 USD | 0.00 USD | 2,300.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 29,330.00 USD | 0.00 USD | 10,250.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 19,080.00 USD | 0.00 USD | 12,140.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 6,940.00 USD | 0.00 USD | 981.12 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 5,960.00 USD | 0.00 USD | 5,960.00 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 958.90 USD | 958.90 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 66,070.00 USD | 65,110.00 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 76,080.00 USD | 10,000.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 76,750.00 USD | 674.40 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 78,870.00 USD | 2,120.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 79,600.00 USD | 732.79 USD | 0.00 USD | `+5.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 80,180.00 USD | 578.10 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 80,660.00 USD | 484.67 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 83,960.00 USD | 3,290.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 137,620.00 USD | 53,670.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 138,290.00 USD | 663.39 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 154,270.00 USD | 15,980.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 154,930.00 USD | 658.25 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 155,170.00 USD | 240.28 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 275,470.00 USD | 120,300.00 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 359,340.00 USD | 83,880.00 USD | 0.00 USD | `+14.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 368,780.00 USD | 9,430.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 388,830.00 USD | 20,060.00 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 389,290.00 USD | 461.02 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 405,920.00 USD | 16,630.00 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 406,970.00 USD | 1,050.00 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 408,290.00 USD | 1,320.00 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 413,020.00 USD | 4,730.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 415,210.00 USD | 2,200.00 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 415,380.00 USD | 165.31 USD | 0.00 USD | `+22.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 417,530.00 USD | 2,150.00 USD | 0.00 USD | `+23.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 419,590.00 USD | 2,060.00 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 423,940.00 USD | 4,350.00 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 424,210.00 USD | 266.44 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 448,990.00 USD | 24,790.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 449,500.00 USD | 506.57 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 452,910.00 USD | 3,410.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 453,630.00 USD | 718.16 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 453,850.00 USD | 218.25 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 456,460.00 USD | 2,610.00 USD | 0.00 USD | `+32.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 469,380.00 USD | 12,920.00 USD | 0.00 USD | `+33.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 470,330.00 USD | 950.82 USD | 0.00 USD | `+35.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 482,950.00 USD | 12,620.00 USD | 0.00 USD | `+36.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 487,060.00 USD | 4,110.00 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 720,100.00 USD | 233,040.00 USD | 0.00 USD | `+38.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 721,280.00 USD | 1,180.00 USD | 0.00 USD | `+38.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 722,170.00 USD | 893.01 USD | 0.00 USD | `+39.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 723,270.00 USD | 1,100.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 724,220.00 USD | 949.96 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 726,550.00 USD | 2,330.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 731,890.00 USD | 5,340.00 USD | 0.00 USD | `+43.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 737,390.00 USD | 5,500.00 USD | 0.00 USD | `+44.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 746,560.00 USD | 9,170.00 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 753,360.00 USD | 6,800.00 USD | 0.00 USD | `+46.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 772,120.00 USD | 18,760.00 USD | 0.00 USD | `+47.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 806,350.00 USD | 34,220.00 USD | 0.00 USD | `+47.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 812,930.00 USD | 6,580.00 USD | 0.00 USD | `+48.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 822,860.00 USD | 9,930.00 USD | 0.00 USD | `+49.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 836,180.00 USD | 13,320.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 850,410.00 USD | 14,240.00 USD | 0.00 USD | `+51.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 934,770.00 USD | 84,360.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 936,460.00 USD | 1,700.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 945,970.00 USD | 9,510.00 USD | 0.00 USD | `+54.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 947,690.00 USD | 1,710.00 USD | 0.00 USD | `+55.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 949,990.00 USD | 2,300.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,050,000.00 USD | 98,330.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,070,000.00 USD | 19,070.00 USD | 0.00 USD | `+57.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,070,000.00 USD | 4,390.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,080,000.00 USD | 6,200.00 USD | 0.00 USD | `+59.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,080,000.00 USD | 4,440.00 USD | 0.00 USD | `+60.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,090,000.00 USD | 4,460.00 USD | 0.00 USD | `+61.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,090,000.00 USD | 448.75 USD | 0.00 USD | `+62.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,120,000.00 USD | 35,940.00 USD | 0.00 USD | `+63.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,120,000.00 USD | 453.75 USD | 0.00 USD | `+64.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,120,000.00 USD | 830.38 USD | 0.00 USD | `+65.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,130,000.00 USD | 458.75 USD | 0.00 USD | `+66.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,130,000.00 USD | 461.25 USD | 0.00 USD | `+66.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,130,000.00 USD | 4,540.00 USD | 0.00 USD | `+67.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,130,000.00 USD | 466.25 USD | 0.00 USD | `+68.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,130,000.00 USD | 468.75 USD | 0.00 USD | `+69.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,130,000.00 USD | 1,960.00 USD | 0.00 USD | `+70.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,130,000.00 USD | 473.75 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,200,000.00 USD | 67,000.00 USD | 0.00 USD | `+72.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,200,000.00 USD | 574.50 USD | 0.00 USD | `+73.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,200,000.00 USD | 577.50 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,200,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,210,000.00 USD | 972.50 USD | 0.00 USD | `+76.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,210,000.00 USD | 7,680.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,210,000.00 USD | 786.00 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,220,000.00 USD | 1,690.00 USD | 0.00 USD | `+78.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,220,000.00 USD | 992.50 USD | 0.00 USD | `+79.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,220,000.00 USD | 997.50 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,830,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+81.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,830,000.00 USD | 1,010.00 USD | 0.00 USD | `+82.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,840,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,840,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,840,000.00 USD | 1,860.00 USD | 0.00 USD | `+87.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,840,000.00 USD | 1,410.00 USD | 0.00 USD | `+88.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,840,000.00 USD | 1,050.00 USD | 0.00 USD | `+89.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,850,000.00 USD | 4,000.00 USD | 0.00 USD | `+90.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,900,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,900,000.00 USD | 3,170.00 USD | 0.00 USD | `+94.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,900,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,900,000.00 USD | 1,090.00 USD | 0.00 USD | `+96.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,910,000.00 USD | 3,280.00 USD | 0.00 USD | `+97.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,910,000.00 USD | 2,110.00 USD | 0.00 USD | `+98.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,910,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,910,000.00 USD | 1,110.00 USD | 0.00 USD | `+100.43%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.61` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 486.28 USD | 0.00 USD | 9,340.00 USD |
| `7D` | `9.63` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 10,700.00 USD | 0.00 USD | 5,820.00 USD |
| `7D` | `9.65` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,460.00 USD |
| `7D` | `9.67` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 115.45 USD | 1,920.00 USD | 8.80 USD |
| `7D` | `9.69` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 4,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.71` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 7.14 USD |
| `1D` | `9.73` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 14,380.00 USD |
| `1D` | `9.75` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 40,030.00 USD | 434.05 USD | 13,160.00 USD |
| `7D` | `9.75` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD |
| `1D` | `9.77` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 112,940.00 USD | 7,340.00 USD | 19,810.00 USD |
| `7D` | `9.77` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.79` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 15,980.00 USD | 146.87 USD | 18.33 USD |
| `7D` | `9.79` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD |
| `1D` | `9.81` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 73,100.00 USD | 18,150.00 USD | 9,690.00 USD |
| `7D` | `9.81` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD |
| `1D` | `9.83` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 37,110.00 USD | 580.25 USD | 10,480.00 USD |
| `7D` | `9.83` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD |
| `7D` | `9.85` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `9.87` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 9,950.00 USD | 146.00 USD | 10,300.00 USD |
| `1D` | `9.91` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 17,040.00 USD | 13,010.00 USD | 0.00 USD |
| `7D` | `9.91` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 0.00 USD | 11,990.00 USD | 107.02 USD |
| `1D` | `9.93` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 13,840.00 USD | 5,540.00 USD | 118.68 USD |
| `7D` | `9.93` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.95` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 9,450.00 USD | 5,730.00 USD | 8,640.00 USD |
| `7D` | `9.95` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD |
| `1D` | `9.97` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 5,850.00 USD | 7,710.00 USD |
| `7D` | `9.97` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 598.17 USD | 154.66 USD |
| `1D` | `9.99` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 6,560.00 USD | 11,790.00 USD |
| `7D` | `9.99` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 25,530.00 USD |
| `7D` | `10.01` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.03` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD |
| `1D` | `10.05` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 10,250.00 USD | 0.00 USD | 39.83 USD |
| `1D` | `10.07` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD |
| `7D` | `10.07` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 351.10 USD | 153.34 USD |
| `1D` | `10.09` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 1,180.00 USD | 0.00 USD | 241.11 USD |
| `7D` | `10.09` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 7,530.00 USD | 7,510.00 USD | 71.35 USD |
| `7D` | `10.11` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 279.85 USD | 0.00 USD | 5,960.00 USD |
| `1D` | `10.13` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 54.51 USD |
| `7D` | `10.13` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,050.00 USD |
| `1D` | `10.15` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 7,090.00 USD | 0.00 USD | 62.75 USD |
| `7D` | `10.15` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,710.00 USD |
| `1D` | `10.17` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 1,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.17` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 65,660.00 USD | 3,240.00 USD | 21,570.00 USD |
| `1D` | `10.19` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 1,410.00 USD | 29.65 USD | 46.76 USD |
| `7D` | `10.19` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,730.00 USD |
| `1D` | `10.21` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 53.57 USD | 3,080.00 USD | 12,410.00 USD |
| `7D` | `10.21` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,420.00 USD |
| `1D` | `10.23` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 10,890.00 USD | 7,660.00 USD | 23,780.00 USD |
| `7D` | `10.23` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,270.00 USD |
| `1D` | `10.25` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 26,800.00 USD | 1,680.00 USD | 11,020.00 USD |
| `7D` | `10.25` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,530.00 USD |
| `1D` | `10.27` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 18,050.00 USD | 5,870.00 USD | 4,400.00 USD |
| `7D` | `10.27` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,780.00 USD |
| `1D` | `10.29` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 17,890.00 USD | 6,330.00 USD | 13,860.00 USD |
| `7D` | `10.29` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,060.00 USD |
| `1D` | `10.31` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 24,410.00 USD | 4,350.00 USD | 10,430.00 USD |
| `7D` | `10.31` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,110.00 USD |
| `1D` | `10.33` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 30,780.00 USD | 9,510.00 USD | 12,120.00 USD |
| `7D` | `10.33` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 58,810.00 USD | 28,270.00 USD | 26,190.00 USD |
| `1D` | `10.35` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 12,800.00 USD | 4,280.00 USD | 8,400.00 USD |
| `7D` | `10.35` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,940.00 USD |
| `1D` | `10.37` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 8,240.00 USD | 7,170.00 USD | 65,450.00 USD |
| `7D` | `10.37` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 12,950.00 USD | 12,460.00 USD | 25,090.00 USD |
| `1D` | `10.39` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 7,450.00 USD | 6,430.00 USD | 7,150.00 USD |
| `7D` | `10.39` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,780.00 USD |
| `1D` | `10.41` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 259,620.00 USD | 10,890.00 USD | 39,680.00 USD |
| `7D` | `10.41` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,610.00 USD |
| `1D` | `10.43` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 172,340.00 USD | 35,040.00 USD | 71,990.00 USD |
| `7D` | `10.43` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 32,710.00 USD | 22,700.00 USD | 14,730.00 USD |
| `1D` | `10.45` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 130,840.00 USD | 18,730.00 USD | 18,330.00 USD |
| `7D` | `10.45` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 149,660.00 USD | 48,540.00 USD | 105,370.00 USD |
| `1D` | `10.47` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 219,660.00 USD | 44,830.00 USD | 77,570.00 USD |
| `7D` | `10.47` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,410.00 USD |
| `1D` | `10.49` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 124,820.00 USD | 16,220.00 USD | 17,410.00 USD |
| `7D` | `10.49` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,260.00 USD |
| `1D` | `10.51` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 27,700.00 USD | 4,710.00 USD | 13,570.00 USD |
| `7D` | `10.51` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,800.00 USD |
| `1D` | `10.53` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 43,880.00 USD | 5,630.00 USD | 29,830.00 USD |
| `7D` | `10.53` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,450.00 USD |
| `1D` | `10.55` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 7,160.00 USD | 2,280.00 USD | 1,820.00 USD |
| `7D` | `10.55` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 55,490.00 USD | 19,150.00 USD | 20,850.00 USD |
| `1D` | `10.57` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 52,260.00 USD | 37,050.00 USD | 34,930.00 USD |
| `7D` | `10.57` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,350.00 USD |
| `1D` | `10.59` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 48,700.00 USD | 22,500.00 USD | 98,170.00 USD |
| `7D` | `10.59` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,430.00 USD |
| `1D` | `10.61` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 231,320.00 USD | 12,140.00 USD | 103,400.00 USD |
| `7D` | `10.61` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,560.00 USD |
| `1D` | `10.63` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 464,250.00 USD | 47,160.00 USD | 117,300.00 USD |
| `7D` | `10.63` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,980.00 USD |
| `1D` | `10.65` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 165,270.00 USD | 54,500.00 USD | 78,060.00 USD |
| `7D` | `10.65` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,590.00 USD |
| `1D` | `10.67` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 224,600.00 USD | 20,340.00 USD | 27,550.00 USD |
| `7D` | `10.67` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,040.00 USD |
| `1D` | `10.69` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 425,050.00 USD | 95,980.00 USD | 143,210.00 USD |
| `7D` | `10.69` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 383,680.00 USD | 49,270.00 USD | 45,190.00 USD |
| `1D` | `10.71` | 653,530.00 USD | 0.00 USD | 653,530.00 USD | 223,440.00 USD | 15,350.00 USD | 3,730.00 USD |
| `7D` | `10.71` | 642,800.00 USD | 0.00 USD | 642,800.00 USD | 238,550.00 USD | 12,470.00 USD | 73,100.00 USD |
| `1D` | `10.73` | 411,010.00 USD | 0.00 USD | 411,010.00 USD | 8,140.00 USD | 3,750.00 USD | 37,720.00 USD |
| `7D` | `10.73` | 318,680.00 USD | 0.00 USD | 318,680.00 USD | 28,700.00 USD | 5,730.00 USD | 173.33 USD |
| `1D` | `10.75` | 361,400.00 USD | 0.00 USD | 361,400.00 USD | 91,880.00 USD | 5,640.00 USD | 54,300.00 USD |
| `7D` | `10.75` | 284,070.00 USD | 0.00 USD | 284,070.00 USD | 17,290.00 USD | 4,890.00 USD | 18,560.00 USD |
| `1D` | `10.77` | 209,590.00 USD | 0.00 USD | 209,590.00 USD | 5,310.00 USD | 4,090.00 USD | 0.00 USD |
| `7D` | `10.77` | 243,330.00 USD | 0.00 USD | 243,330.00 USD | 16,290.00 USD | 15,910.00 USD | 8,860.00 USD |
| `1D` | `10.79` | 200,190.00 USD | 0.00 USD | 200,190.00 USD | 88,000.00 USD | 85,100.00 USD | 0.00 USD |
| `7D` | `10.79` | 202,270.00 USD | 0.00 USD | 202,270.00 USD | 33,460.00 USD | 59,950.00 USD | 24,960.00 USD |
| `1D` | `10.81` | 27,080.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD |
| `7D` | `10.81` | 83,900.00 USD | 0.00 USD | 83,900.00 USD | 9,380.00 USD | 0.00 USD | 60,460.00 USD |
| `1D` | `10.82` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.83` | 14,060.00 USD | 0.00 USD | 14,060.00 USD | 13,720.00 USD | 0.00 USD | 340.35 USD |
| `7D` | `10.84` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.85` | 3,640.00 USD | 3,640.00 USD | 0.00 USD | 3,420.00 USD | 0.00 USD | 222.19 USD |
| `1D` | `10.87` | 209.94 USD | 209.94 USD | 0.00 USD | 0.00 USD | 0.00 USD | 209.94 USD |
| `7D` | `10.91` | 3,860.00 USD | 3,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 225.84 USD |
| `7D` | `10.93` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 622.92 USD |
| `1D` | `10.95` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.95` | 12,310.00 USD | 12,310.00 USD | 0.00 USD | 7,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.97` | 17,140.00 USD | 17,140.00 USD | 0.00 USD | 124.21 USD | 15,600.00 USD | 0.00 USD |
| `7D` | `10.97` | 24,990.00 USD | 24,990.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 18,610.00 USD | 18,610.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 40,600.00 USD | 40,600.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.01` | 45,360.00 USD | 45,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26,740.00 USD |
| `7D` | `11.01` | 51,190.00 USD | 51,190.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.03` | 117,050.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 71,690.00 USD |
| `7D` | `11.03` | 60,560.00 USD | 60,560.00 USD | 0.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.05` | 377,640.00 USD | 377,640.00 USD | 0.00 USD | 192,840.00 USD | 2,170.00 USD | 65,580.00 USD |
| `7D` | `11.05` | 67,090.00 USD | 67,090.00 USD | 0.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.07` | 908,470.00 USD | 908,470.00 USD | 0.00 USD | 435,240.00 USD | 16,820.00 USD | 78,770.00 USD |
| `7D` | `11.07` | 74,600.00 USD | 74,600.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.09` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 126,930.00 USD | 34,010.00 USD | 40,600.00 USD |
| `7D` | `11.09` | 82,100.00 USD | 82,100.00 USD | 0.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `11.11` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 216,430.00 USD | 18,460.00 USD | 15,640.00 USD |
| `7D` | `11.11` | 507,900.00 USD | 507,900.00 USD | 0.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD |
| `1D` | `11.13` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 408,510.00 USD | 85,870.00 USD | 132,140.00 USD |
| `7D` | `11.13` | 967,940.00 USD | 967,940.00 USD | 0.00 USD | 372,210.00 USD | 48,150.00 USD | 39,680.00 USD |
| `1D` | `11.15` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 194,240.00 USD | 13,390.00 USD | 0.00 USD |
| `7D` | `11.15` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 64,880.00 USD |
| `1D` | `11.17` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 165.70 USD | 51,630.00 USD | 15,020.00 USD |
| `7D` | `11.17` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.19` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 72,110.00 USD | 63,410.00 USD | 0.00 USD |
| `1D` | `11.21` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 112,460.00 USD | 0.00 USD | 76,790.00 USD |
| `7D` | `11.21` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 311,160.00 USD | 698.80 USD | 17.04 USD |
| `1D` | `11.23` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 191,590.00 USD | 1,250.00 USD | 107,710.00 USD |
| `7D` | `11.23` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 241,160.00 USD | 59,950.00 USD | 25.02 USD |
| `1D` | `11.25` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 90,500.00 USD | 39,800.00 USD | 114,980.00 USD |
| `7D` | `11.25` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,430.00 USD |
| `1D` | `11.27` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 304,550.00 USD | 2,670.00 USD | 175,630.00 USD |
| `7D` | `11.27` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD |
| `1D` | `11.29` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 163,770.00 USD | 122,050.00 USD | 213,620.00 USD |
| `7D` | `11.29` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 104,970.00 USD | 57,050.00 USD | 56,250.00 USD |
| `1D` | `11.31` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 63,250.00 USD | 69,420.00 USD | 79,800.00 USD |
| `7D` | `11.31` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 198,020.00 USD | 37,890.00 USD | 31,620.00 USD |
| `7D` | `11.33` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD |
| `1D` | `11.35` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 300,200.00 USD | 125,560.00 USD | 66,390.00 USD |
| `7D` | `11.35` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD |
| `1D` | `11.37` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 150,920.00 USD | 80,560.00 USD | 22,240.00 USD |
| `7D` | `11.37` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 110,820.00 USD | 72,750.00 USD | 131,520.00 USD |
| `1D` | `11.39` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 1,530.00 USD | 36,100.00 USD | 7,510.00 USD |
| `7D` | `11.39` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 91,890.00 USD | 34,170.00 USD | 140,440.00 USD |
| `7D` | `11.41` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,970.00 USD |
| `1D` | `11.43` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 52,230.00 USD | 25,530.00 USD | 88,320.00 USD |
| `7D` | `11.43` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 138,950.00 USD | 52,330.00 USD | 91,960.00 USD |
| `1D` | `11.45` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 44,620.00 USD | 70,070.00 USD | 0.00 USD |
| `7D` | `11.45` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 203,890.00 USD | 68,950.00 USD | 37,930.00 USD |
| `1D` | `11.47` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 47,140.00 USD | 19,290.00 USD | 23,420.00 USD |
| `7D` | `11.47` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 33,390.00 USD | 22,220.00 USD | 34,640.00 USD |
| `7D` | `11.49` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 41,360.00 USD | 27,210.00 USD | 30,920.00 USD |
| `7D` | `11.51` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD |
| `1D` | `11.53` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 32,640.00 USD | 17,750.00 USD | 29,710.00 USD |
| `7D` | `11.53` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,370.00 USD |
| `1D` | `11.55` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 22,840.00 USD | 407.50 USD | 11,900.00 USD |
| `7D` | `11.55` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,790.00 USD |
| `1D` | `11.57` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | 23,920.00 USD |
| `7D` | `11.57` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD |
| `1D` | `11.59` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 15,100.00 USD | 7,830.00 USD | 39,570.00 USD |
| `7D` | `11.59` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.61` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 153,200.00 USD | 260.05 USD | 71,370.00 USD |
| `7D` | `11.61` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 201.68 USD |
| `1D` | `11.63` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 15,720.00 USD |
| `7D` | `11.63` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 43,680.00 USD | 0.00 USD | 309.32 USD |
| `1D` | `11.65` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 1,410.00 USD | 386.12 USD | 46.76 USD |
| `7D` | `11.65` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,130.00 USD |
| `1D` | `11.67` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 1,260.00 USD | 0.00 USD |
| `7D` | `11.67` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.69` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 59,600.00 USD | 29,150.00 USD | 313.96 USD |
| `7D` | `11.69` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.71` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 138,560.00 USD | 13,020.00 USD | 0.00 USD |
| `7D` | `11.71` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 98,180.00 USD | 495.80 USD | 41,790.00 USD |
| `7D` | `11.73` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `11.75` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 20,910.00 USD | 31,550.00 USD | 61,350.00 USD |
| `7D` | `11.75` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 547.35 USD |
| `1D` | `11.77` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 40,510.00 USD | 18,010.00 USD | 177.93 USD |
| `7D` | `11.77` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 11,110.00 USD | 0.00 USD | 40,080.00 USD |
| `7D` | `11.79` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.81` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 15,660.00 USD | 327.53 USD |
| `7D` | `11.81` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 11,070.00 USD | 12,530.00 USD | 18,420.00 USD |
| `7D` | `11.83` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 441.76 USD |
| `1D` | `11.85` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 76,700.00 USD | 21,690.00 USD | 82,330.00 USD |
| `7D` | `11.85` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 0.00 USD |
| `1D` | `11.87` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 19,640.00 USD | 25,210.00 USD | 37,840.00 USD |
| `7D` | `11.87` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,040.00 USD |
| `1D` | `11.89` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 44,160.00 USD | 12,100.00 USD | 28,900.00 USD |
| `7D` | `11.89` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 0.00 USD |
| `1D` | `11.91` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 102,960.00 USD | 18,980.00 USD | 31,710.00 USD |
| `7D` | `11.91` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | 35.60 USD |
| `1D` | `11.93` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 135,130.00 USD | 28,490.00 USD | 28,590.00 USD |
| `7D` | `11.93` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 85,850.00 USD | 18,280.00 USD | 41,560.00 USD |
| `7D` | `11.95` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,200.00 USD |
| `1D` | `11.97` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 77,200.00 USD | 36,400.00 USD | 97,330.00 USD |
| `7D` | `11.97` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 403,040.00 USD | 35,810.00 USD | 223,200.00 USD |
| `1D` | `11.99` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 123,700.00 USD | 25,550.00 USD | 46,860.00 USD |
| `7D` | `11.99` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,010.00 USD |
| `1D` | `12.01` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 60,120.00 USD | 12,220.00 USD | 52,780.00 USD |
| `7D` | `12.01` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 204,590.00 USD | 6,390.00 USD | 247,730.00 USD |
| `1D` | `12.03` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 88,410.00 USD | 43,040.00 USD | 36,690.00 USD |
| `7D` | `12.03` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 347,250.00 USD | 140,540.00 USD | 205,700.00 USD |
| `1D` | `12.05` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 211,220.00 USD | 59,410.00 USD | 90,390.00 USD |
| `7D` | `12.05` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,770.00 USD |
| `1D` | `12.07` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 114,130.00 USD | 52,960.00 USD | 97,550.00 USD |
| `7D` | `12.07` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,170.00 USD |
| `1D` | `12.09` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 17,390.00 USD | 18,150.00 USD | 17,590.00 USD |
| `7D` | `12.09` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,650.00 USD |
| `1D` | `12.11` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 94,540.00 USD | 34,450.00 USD | 55,330.00 USD |
| `7D` | `12.11` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,210.00 USD |
| `1D` | `12.13` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 94,650.00 USD | 34,210.00 USD | 39,740.00 USD |
| `7D` | `12.13` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,310.00 USD |
| `1D` | `12.15` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 116,080.00 USD | 42,360.00 USD | 65,390.00 USD |
| `7D` | `12.15` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 144,940.00 USD |
| `1D` | `12.17` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 122,970.00 USD | 63,760.00 USD | 69,710.00 USD |
| `7D` | `12.17` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,090.00 USD |
| `1D` | `12.19` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 64,080.00 USD | 23,440.00 USD | 12,250.00 USD |
| `7D` | `12.19` | 12,500,000.00 USD | 12,500,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,560.00 USD |
| `1D` | `12.21` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 52,950.00 USD | 28,910.00 USD | 50,920.00 USD |
| `7D` | `12.21` | 12,910,000.00 USD | 12,910,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,230.00 USD |
| `1D` | `12.23` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 14,580.00 USD | 24,860.00 USD | 4,690.00 USD |
| `7D` | `12.23` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,080.00 USD |
| `1D` | `12.25` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 6,540.00 USD | 5,600.00 USD | 7,630.00 USD |
| `7D` | `12.25` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 103,120.00 USD |
| `1D` | `12.27` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 52,420.00 USD | 9,860.00 USD | 22,930.00 USD |
| `7D` | `12.27` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,370.00 USD |
| `1D` | `12.29` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 38,460.00 USD | 19,790.00 USD | 34,620.00 USD |
| `7D` | `12.29` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,450.00 USD |
| `1D` | `12.31` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 19,750.00 USD | 4,950.00 USD | 9,840.00 USD |
| `7D` | `12.31` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,200.00 USD |
| `1D` | `12.33` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 1,880.00 USD | 3,680.00 USD | 3,290.00 USD |
| `7D` | `12.33` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,150.00 USD |
| `1D` | `12.35` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 19,880.00 USD | 12,610.00 USD | 5,540.00 USD |
| `7D` | `12.35` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,250.00 USD |
| `1D` | `12.37` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 8,820.00 USD | 5,700.00 USD | 3,150.00 USD |
| `7D` | `12.37` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 12,400.00 USD |
| `1D` | `12.39` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 28,580.00 USD | 12,560.00 USD | 21,540.00 USD |
| `7D` | `12.39` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 122,920.00 USD | 42,040.00 USD | 174,110.00 USD |
| `1D` | `12.41` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 42,540.00 USD | 19,880.00 USD | 23,470.00 USD |
| `7D` | `12.41` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 114,020.00 USD |
| `1D` | `12.43` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 23,090.00 USD | 5,940.00 USD | 196.48 USD |
| `7D` | `12.43` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 333,910.00 USD |
| `1D` | `12.45` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 10,690.00 USD | 4,330.00 USD | 6,410.00 USD |
| `7D` | `12.45` | 16,440,000.00 USD | 16,440,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,760.00 USD |
| `1D` | `12.47` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 12,000.00 USD | 12,410.00 USD |
| `7D` | `12.47` | 16,590,000.00 USD | 16,590,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 76,090.00 USD |
| `7D` | `12.49` | 16,760,000.00 USD | 16,760,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,500.00 USD |
| `7D` | `12.51` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 133,990.00 USD | 26,650.00 USD | 85,950.00 USD |
| `7D` | `12.53` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,110.00 USD |
| `7D` | `12.55` | 17,560,000.00 USD | 17,560,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,050.00 USD |
| `7D` | `12.57` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 118,650.00 USD | 65,650.00 USD | 10,630.00 USD |
| `7D` | `12.59` | 17,870,000.00 USD | 17,870,000.00 USD | 0.00 USD | 65,910.00 USD | 14,350.00 USD | 36,490.00 USD |
| `7D` | `12.61` | 18,000,000.00 USD | 18,000,000.00 USD | 0.00 USD | 41,220.00 USD | 29,270.00 USD | 58,850.00 USD |
| `7D` | `12.63` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 64,120.00 USD | 28,270.00 USD | 81,540.00 USD |
| `7D` | `12.65` | 18,270,000.00 USD | 18,270,000.00 USD | 0.00 USD | 57,370.00 USD | 26,110.00 USD | 8,700.00 USD |
| `7D` | `12.67` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 54,670.00 USD | 16,240.00 USD | 223,940.00 USD |
| `7D` | `12.69` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 44,600.00 USD | 30,290.00 USD | 165,570.00 USD |
| `7D` | `12.71` | 18,890,000.00 USD | 18,890,000.00 USD | 0.00 USD | 21,450.00 USD | 43,220.00 USD | 24,490.00 USD |
| `7D` | `12.73` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 28,160.00 USD |
| `7D` | `12.75` | 19,050,000.00 USD | 19,050,000.00 USD | 0.00 USD | 33,190.00 USD | 22,700.00 USD | 14,790.00 USD |
| `7D` | `12.77` | 19,140,000.00 USD | 19,140,000.00 USD | 0.00 USD | 34,550.00 USD | 11,060.00 USD | 42,290.00 USD |
| `7D` | `12.79` | 19,230,000.00 USD | 19,230,000.00 USD | 0.00 USD | 55,160.00 USD | 22,760.00 USD | 6,700.00 USD |
| `7D` | `12.81` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,750.00 USD |
| `7D` | `12.83` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,090.00 USD |
| `7D` | `12.85` | 19,360,000.00 USD | 19,360,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD |
| `7D` | `12.87` | 19,400,000.00 USD | 19,400,000.00 USD | 0.00 USD | 9,820.00 USD | 6,560.00 USD | 21,100.00 USD |
| `7D` | `12.89` | 19,490,000.00 USD | 19,490,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,730.00 USD |
| `7D` | `12.91` | 19,590,000.00 USD | 19,590,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 23,310.00 USD |
| `7D` | `12.93` | 19,610,000.00 USD | 19,610,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 43.53 USD |
| `7D` | `12.95` | 19,630,000.00 USD | 19,630,000.00 USD | 0.00 USD | 1,920.00 USD | 9,210.00 USD | 4,110.00 USD |
| `7D` | `12.97` | 19,660,000.00 USD | 19,660,000.00 USD | 0.00 USD | 13,890.00 USD | 10,560.00 USD | 9,950.00 USD |
| `7D` | `12.99` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,590.00 USD |
| `7D` | `13.01` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `13.03` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 303.50 USD | 3,710.00 USD | 0.00 USD |
| `7D` | `13.07` | 19,800,000.00 USD | 19,800,000.00 USD | 0.00 USD | 23,750.00 USD | 6,890.00 USD | 17,910.00 USD |
| `7D` | `13.09` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 16,060.00 USD | 527.72 USD | 7,630.00 USD |
| `7D` | `13.11` | 19,850,000.00 USD | 19,850,000.00 USD | 0.00 USD | 19,270.00 USD | 5,960.00 USD | 0.00 USD |
| `7D` | `13.13` | 19,870,000.00 USD | 19,870,000.00 USD | 0.00 USD | 13,360.00 USD | 4,010.00 USD | 21.51 USD |
| `7D` | `13.17` | 19,880,000.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,400.00 USD |
| `7D` | `13.19` | 19,890,000.00 USD | 19,890,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,690.00 USD |
| `7D` | `13.21` | 19,920,000.00 USD | 19,920,000.00 USD | 0.00 USD | 13,890.00 USD | 6,210.00 USD | 8,940.00 USD |
| `7D` | `13.23` | 19,930,000.00 USD | 19,930,000.00 USD | 0.00 USD | 10,840.00 USD | 146.97 USD | 37.80 USD |
| `7D` | `13.25` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD |
| `7D` | `13.27` | 20,030,000.00 USD | 20,030,000.00 USD | 0.00 USD | 10,290.00 USD | 14,130.00 USD | 10,920.00 USD |
| `7D` | `13.29` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 6,180.00 USD | 2,560.00 USD | 17.60 USD |
| `7D` | `13.31` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 12,560.00 USD | 6,580.00 USD | 6,550.00 USD |
| `7D` | `13.33` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.35` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 158.65 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `528.67M` | Total OI Tokens: `48,934,001.9 LINK`
  * 1h OI Change: `+0.89%` | 4h OI Change: `-4.61%` | 24h OI Change: `-7.71%`
  * Exchange Breakdown: Binance=`103.14M` | Bybit=`62.60M` | OKX=`25.96M` | Hyperliquid=`50.64M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.82K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0015%` | **USDT OKX** | `0.0093%` |
| **USDT Bybit** | `0.0051%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0013%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0063%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `51.49%` | `48.51%` | `1.06` | 28,120,000.00 USD |
| `15M` | `Binance` | `49.94%` | `50.06%` | `1.00` | 10,440,000.00 USD |
| `15M` | `OKX` | `51.45%` | `48.55%` | `1.06` | 5,070,000.00 USD |
| `15M` | `Bybit` | `53.91%` | `46.09%` | `1.17` | 2,510,000.00 USD |
| `15M` | `KuCoin` | `41.92%` | `58.08%` | `0.72` | 45,470.00 USD |
| `15M` | `Gate` | `53.21%` | `46.79%` | `1.14` | 3,220,000.00 USD |
| `15M` | `Bitget` | `60.22%` | `39.78%` | `1.51` | 403,620.00 USD |
| `15M` | `BingX` | `59.93%` | `40.07%` | `1.50` | 129,650.00 USD |
| `15M` | `MEXC` | `57.31%` | `42.69%` | `1.34` | 3,520,000.00 USD |
| `15M` | `Bitunix` | `48.38%` | `51.62%` | `0.94` | 653,480.00 USD |
| `15M` | `Hyperliquid` | `39.81%` | `60.19%` | `0.66` | 64,650.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.41%` | `48.59%` | `1.06` | 87,940.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 15,190.00 USD |
| `15M` | `WhiteBIT` | `52.9%` | `47.1%` | `1.12` | 61,950.00 USD |
| `15M` | `HTX` | `37.82%` | `62.18%` | `0.61` | 24,680.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `53.39%` | `46.61%` | `1.15` | 169,810.00 USD |
| `15M` | `Aster` | `50.36%` | `49.64%` | `1.01` | 1,670,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `41.24%` | `58.76%` | `0.70` | 39,000.00 USD |
| `15M` | `Whale Positions` | `49.94%` | `50.06%` | `1.00` | 10,440,000.00 USD |
| `15M` | `Global Accounts` | `51.49%` | `48.51%` | `1.06` | 28,120,000.00 USD |
| `1H` | `LINK` | `49.18%` | `50.82%` | `0.97` | 281,480,000.00 USD |
| `1H` | `Binance` | `49.54%` | `50.46%` | `0.98` | 124,620,000.00 USD |
| `1H` | `OKX` | `51.15%` | `48.85%` | `1.05` | 33,410,000.00 USD |
| `1H` | `Bybit` | `47.77%` | `52.23%` | `0.91` | 60,470,000.00 USD |
| `1H` | `KuCoin` | `51.84%` | `48.16%` | `1.08` | 1,480,000.00 USD |
| `1H` | `Gate` | `50.25%` | `49.75%` | `1.01` | 8,040,000.00 USD |
| `1H` | `Bitget` | `53.6%` | `46.4%` | `1.16` | 8,490,000.00 USD |
| `1H` | `BingX` | `56.33%` | `43.67%` | `1.29` | 2,360,000.00 USD |
| `1H` | `MEXC` | `49.86%` | `50.14%` | `0.99` | 3,670,000.00 USD |
| `1H` | `Bitunix` | `51.96%` | `48.04%` | `1.08` | 4,280,000.00 USD |
| `1H` | `Hyperliquid` | `50.66%` | `49.34%` | `1.03` | 14,110,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.72%` | `50.28%` | `0.99` | 4,060,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `31.3%` | `68.7%` | `0.46` | 10,020,000.00 USD |
| `1H` | `HTX` | `59.3%` | `40.7%` | `1.46` | 1,000,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.64%` | `46.36%` | `1.16` | 1,510,000.00 USD |
| `1H` | `Aster` | `68.88%` | `31.12%` | `2.21` | 2,150,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.63%` | `56.37%` | `0.77` | 1,810,000.00 USD |
| `1H` | `Whale Positions` | `49.54%` | `50.46%` | `0.98` | 124,620,000.00 USD |
| `1H` | `Global Accounts` | `49.18%` | `50.82%` | `0.97` | 281,480,000.00 USD |
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
| `0:00 UTC` | `11.13` | `11.25` | `11.13` | `11.55` | `11.03` | 15,867,227.37 USD | 6,488,166.63 USD | 9,379,060.74 USD | -2,890,894.11 USD | `-18.22%` | `4B / 29S` |
| `5:00 UTC` | `11.00` | `11.03` | `11.00` | `11.19` | `10.87` | 17,839,722.17 USD | 8,415,517.99 USD | 9,424,204.18 USD | -1,008,686.19 USD | `-5.65%` | `9B / 18S` |
| `0:00 UTC` | `11.11` | `11.06` | `11.11` | `11.18` | `10.95` | 10,677,747.31 USD | 5,105,845.59 USD | 5,571,901.72 USD | -466,056.13 USD | `-4.36%` | `1B / 2S` |
| `5:00 UTC` | `11.18` | `11.21` | `11.18` | `11.30` | `11.14` | 5,823,506.96 USD | 2,554,704.96 USD | 3,268,802.01 USD | -714,097.05 USD | `-12.26%` | `10B / 21S` |
| `0:00 UTC` | `11.23` | `11.21` | `11.23` | `11.27` | `11.10` | 3,064,696.05 USD | 1,263,662.15 USD | 1,801,033.90 USD | -537,371.74 USD | `-17.53%` | `20B / 42S` |
| `5:00 UTC` | `11.10` | `11.09` | `11.10` | `11.13` | `11.03` | 2,476,363.14 USD | 1,173,647.56 USD | 1,302,715.59 USD | -129,068.03 USD | `-5.21%` | `19B / 14S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `11.06` | `10.85` | 9,610,457.01 USD | 3,926,356.34 USD | 5,684,100.67 USD | -1,757,744.32 USD | `-18.29%` | `3B / 20S` |
| `5:00 UTC` | `10.89` | `10.91` | `10.89` | `10.95` | `10.87` | 6,365,804.82 USD | 2,685,695.45 USD | 3,680,109.37 USD | -994,413.92 USD | `-15.62%` | `1B / 9S` |
| `0:00 UTC` | `10.83` | `10.85` | `10.83` | `10.97` | `10.79` | 25,964,116.59 USD | 9,923,976.23 USD | 16,040,140.36 USD | -6,116,164.13 USD | `-23.56%` | `4B / 36S` |
| `5:00 UTC` | `10.79` | `10.79` | `10.79` | `10.84` | `10.74` | 6,028,526.31 USD | 2,951,712.95 USD | 3,076,813.36 USD | -125,100.41 USD | `-2.08%` | `9B / 18S` |

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
| `5m` | 100,170.00 USD | 455,730.00 USD | **`ACCUMULATION`** |
| `15m` | -288,200.00 USD | -4,140,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -642,930.00 USD | -8,340,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -847,890.00 USD | -10,220,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,000,000.00 USD | -13,010,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -6,710,000.00 USD | -20,100,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,540,000.00 USD | -22,100,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,760,000.00 USD | -21,200,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -6,160,000.00 USD | -21,390,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -6,790,000.00 USD | -25,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -15,350,000.00 USD | -44,110,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -76,050,000.00 USD | -206,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+100.17K` | 15m=`-288.20K` | 1h=`-847.89K` | 24h=`-6.79M`
* Futures Capital Netflows: 5m=`+455.73K` | 15m=`-4.14M` | 1h=`-10.22M` | 24h=`-25.48M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `10.51` (Risk Distance: `0.2931` pts)
  * +2.5R Take Profit: `11.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.42` (Risk Distance: `0.2931` pts)
  * +2.5R Take Profit: `10.39`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
