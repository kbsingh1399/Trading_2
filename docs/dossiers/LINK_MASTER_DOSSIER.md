# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 02:42:47 IST` (`2026-10-29 21:12:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.92` | **Live Ask Quote**: `11.01` | **Mid Price**: `10.96`
- **Spread Points**: `90.00` | **Spread BPS**: `82.11 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.52` | VWAP Z-Score: `-2.59` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1237` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `17.82` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.17` | Lower -3.00σ Band: `10.88`
  * Upper +2.51σ Band: `12.06` | Lower -2.51σ Band: `10.98`
  * Upper +2.01σ Band: `11.96` | Lower -2.01σ Band: `11.09`
  * Upper +2.00σ Band: `11.95` | Lower -2.00σ Band: `11.09`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.25`
  * Upper +1.00σ Band: `11.74` | Lower -1.00σ Band: `11.31`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.37` | EMA-20=`11.52` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.57` (Slope: `+0.0000`) | EMA-100=`11.57`
  * Institutional Anchors: EMA-144=`11.55` | EMA-200=`11.52` (Slope: `-0.0325`) | EMA-233=`11.51`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.85` | Weekly High=`11.96` | Weekly Low=`10.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.95` (Distance: `+0.54%`)
  * Point of Control (POC) = `10.91` (Distance: `+0.81%`)
  * Value Area Low (VAL) = `10.91` (Distance: `+0.81%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.59` | Weekly POC=`11.42` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`10.96` | Low=`10.91`
  * London Session (08:00-16:00 UTC): High=`11.00` | Low=`10.92`
  * New York Session (13:00-21:00 UTC): High=`11.03` | Low=`10.90`
  * Initial Balance (First Hour): IB High=`10.99` | IB Low=`10.93`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.92` - `11.00`
  * Optimal Trade Entry (OTE 0.705): `10.98`
  * Structural Invalidation Anchor (0.786): `11.05`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.09` | `11.11` | `10.98` | `10.99` | `340,746` | 3,762,688.95 USD | -211,679.47 USD | `-5.63%` | -6,530,781.53 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `10.99` | `11.07` | `10.95` | `10.98` | `341,740` | 3,760,221.18 USD | -32,119.27 USD | `-0.85%` | -6,562,900.80 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `10.98` | `10.99` | `10.96` | `10.99` | `20,426` | 224,146.24 USD | 47,901.10 USD | `+21.37%` | -6,514,999.70 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.52` | `11.55` | `11.03` | `11.09` | `1,410,169` | 15,867,207.08 USD | -2,890,914.41 USD | `-18.22%` | -5,489,516.00 USD | `-4.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.09` | `11.19` | `10.87` | `10.99` | `1,617,019` | 17,839,742.46 USD | -1,008,665.90 USD | `-5.65%` | -6,498,181.90 USD | `-1.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.99` | `11.07` | `10.95` | `10.98` | `361,166` | 3,973,379.26 USD | 18,185.72 USD | `+0.46%` | -6,479,996.17 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.73` | `11.63` | `11.69` | `318,927` | 3,725,220.26 USD | -245,323.17 USD | `-6.59%` | -2,290,022.42 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.69` | `11.69` | `10.87` | `10.99` | `3,805,467` | 42,673,690.41 USD | -4,269,954.14 USD | `-10.01%` | -6,559,976.56 USD | `-3.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `10.99` | `11.07` | `10.95` | `10.99` | `368,099` | 4,049,582.32 USD | 12,788.80 USD | `+0.32%` | -6,547,187.76 USD | `+0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `10.99` | `4,168,853` | 46,671,471.62 USD | -4,249,252.66 USD | `-9.10%` | -5,967,750.26 USD | `-1.76` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `10.99` | `4,168,853` | 46,671,471.62 USD | -4,249,252.66 USD | `-9.10%` | -5,967,750.26 USD | `-1.76` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.96`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `497` | `0x73ce...8ce9` | `LONG` | 4,420,128.18 USD | `400,011,600.00` | `12.05` | `11.06` | `9.12` | -399,625.52 USD | `-9.04%` | `5X Cross` |
| `677` | `0xb83d...6e36` | `SHORT` | 3,309,558.52 USD | `299,751,700.00` | `12.93` | `11.06` | `497.54` | 567,055.98 USD | `+17.13%` | `3X Cross` |
| `810` | `0x5b5d...c060` | `SHORT` | 2,797,579.51 USD | `253,105,900.00` | `13.61` | `11.06` | `693.28` | 646,794.99 USD | `+23.12%` | `3X Cross` |
| `893` | `0x458d...ab3b` | `LONG` | 2,505,765.56 USD | `227,156,700.00` | `13.13` | `11.06` | `9.34` | -476,464.84 USD | `-19.01%` | `3X Isolated` |
| `980` | `0xdd53...2b13` | `SHORT` | 2,264,621.09 USD | `206,475,300.00` | `11.92` | `11.06` | `306.99` | 196,601.84 USD | `+8.68%` | `3X Cross` |
| `1001` | `0x3dc9...54b0` | `SHORT` | 2,207,000.00 USD | `200,000,000.00` | `7.56` | `11.06` | `93.46` | -695,841.58 USD | `-31.53%` | `10X Cross` |
| `1024` | `0x45d2...4029` | `SHORT` | 2,146,003.50 USD | `195,500,000.00` | `11.54` | `11.06` | `218.22` | 110,479.93 USD | `+5.15%` | `10X Cross` |
| `1229` | `0x6540...f7b7` | `LONG` | 1,820,600.10 USD | `165,871,000.00` | `12.46` | `11.06` | `7.80` | -245,668.13 USD | `-13.49%` | `5X Isolated` |
| `1281` | `0xeadc...9d55` | `LONG` | 1,736,972.97 USD | `157,691,600.00` | `9.43` | `11.06` | `0.000000` | 250,318.07 USD | `+14.41%` | `10X Cross` |
| `1656` | `0xf6f3...47f8` | `SHORT` | 1,269,871.58 USD | `115,024,600.00` | `11.42` | `11.06` | `20.40` | 43,458.60 USD | `+3.42%` | `5X Cross` |
| `1690` | `0x9df2...c665` | `SHORT` | 1,240,170.94 USD | `112,344,500.00` | `11.48` | `11.06` | `284.43` | 49,984.13 USD | `+4.03%` | `10X Cross` |
| `1825` | `0xfe7e...11b4` | `LONG` | 1,111,348.30 USD | `101,142,000.00` | `14.47` | `11.06` | `5.33` | -351,764.85 USD | `-31.65%` | `5X Isolated` |
| `1855` | `0x8af7...fa05` | `SHORT` | 1,082,116.04 USD | `98,661,200.00` | `14.08` | `11.06` | `205.07` | 307,066.50 USD | `+28.38%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.69` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6900 USD [API] | `2026-10-28 04:27:58` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 8,700.10 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.70K USD at 11.7110 USD [API] | `2026-10-28 07:18:08` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 24,983.08 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 24.98K USD at 11.7110 USD [API] | `2026-10-28 07:18:08` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 5,522.23 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.52K USD at 11.7220 USD [API] | `2026-10-28 07:33:08` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 868.24 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.87K USD at 12.4390 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 5,739.35 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 5.74K USD at 12.4390 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 2,433.07 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 2.43K USD at 12.4390 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 237.60 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.24K USD at 12.4400 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 49.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.05K USD at 12.4400 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 62.20 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.4400 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 676.79 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.68K USD at 12.4410 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 2,433.46 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 2.43K USD at 12.4410 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 276.21 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.28K USD at 12.4420 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 49.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.05K USD at 12.4420 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 14.93 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.01K USD at 12.4420 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.44` | 236.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.24K USD at 12.4430 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.45` | 1,093.92 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 1.09K USD at 12.4450 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `12.45` | 2,162.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 2.16K USD at 12.4450 USD [API] | `2026-09-23 14:11:26` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 3,041.12 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 3.04K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 614.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.61K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,468.37 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 5.47K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 7,510.20 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 7.51K USD at 11.8420 USD [API] | `2026-10-28 08:37:43` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 1,550.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 1.55K USD at 11.8470 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.81` | 5,332.67 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.33K USD at 11.8110 USD [API] | `2026-10-28 08:49:47` |
| `ANNOUNCEMENT` | `INFO` | `11.79` | 6,159.35 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.16K USD at 11.7950 USD [API] | `2026-10-28 09:01:38` |
| `ANNOUNCEMENT` | `INFO` | `11.87` | 14,602.56 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 14.60K USD at 11.8720 USD [API] | `2026-10-28 09:51:15` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,683.90 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.68K USD at 11.8390 USD [API] | `2026-10-28 10:24:35` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 7,011.24 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.01K USD at 11.7520 USD [API] | `2026-10-28 11:25:24` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 8,887.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.89K USD at 11.7530 USD [API] | `2026-10-28 11:25:24` |
| `ANNOUNCEMENT` | `INFO` | `11.75` | 7,503.12 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.50K USD at 11.7530 USD [API] | `2026-10-28 11:25:24` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.92` (Vol: 146,200.00 USD, Dist: `+3.39%`) | Long MP=`11.40` (Vol: 165,300.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+4.50%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--2.18%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+5.97%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--3.29%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+5.98%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--3.26%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 486.45 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,230.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 4,150.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 27,030.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,620.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 961.07 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 592.95 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,190.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 2,510.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,630.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,750.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 13,360.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,300.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 12,630.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 4,470.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 17,540.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 50,880.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 239,270.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 91,360.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 886.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 20,990.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 748.14 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 1,520.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 22,830.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 790.76 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 68,690.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 9,240.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 80,020.00 USD | 11,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 23,300.00 USD | 11,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 7,650.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 34,470.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 37,510.00 USD | 11,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 14,440.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 686,800.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 8,460.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 52,130.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 9,870.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 19,770.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 9,240.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 14,100.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,010.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 171,890.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,410,000.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 29,940.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 35,750.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,780.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 53,810.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 21,580.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,370.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 312,090.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,570.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 505,780.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 76,580.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,720,000.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 41,710.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 26,730.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 12,490.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 9,080.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 54,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 19,550.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 2,370,000.00 USD | 2,370,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 2,340,000.00 USD | 2,340,000.00 USD | 13,840.00 USD | 5,510.00 USD | 118.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 2,320,000.00 USD | 2,320,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 760,400.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 2,320,000.00 USD | 2,320,000.00 USD | 7,630.00 USD | 5,270.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 6,510.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 2,280,000.00 USD | 2,280,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 647,590.00 USD | 989,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 28,910.00 USD | 342,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 2,270,000.00 USD | 2,270,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 2,260,000.00 USD | 2,260,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 2,230,000.00 USD | 2,230,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 20,290,000.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 35,700.00 USD | 313,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 2,170,000.00 USD | 2,170,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 19,910,000.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 2,160,000.00 USD | 2,160,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 19,770,000.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 2,110,000.00 USD | 2,110,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 19,650,000.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 2,090,000.00 USD | 2,090,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 19,540,000.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 2,040,000.00 USD | 2,040,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 19,400,000.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 14,650.00 USD | 277,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 2,000,000.00 USD | 2,000,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 19,270,000.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 1,970,000.00 USD | 1,970,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 19,240,000.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 1,950,000.00 USD | 1,950,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 19,180,000.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 1,920,000.00 USD | 1,920,000.00 USD | 20,220.00 USD | 10,800.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 19,030,000.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 1,880,000.00 USD | 1,880,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 18,950,000.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 16,780.00 USD | 262,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 1,810,000.00 USD | 1,810,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 18,890,000.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 1,790,000.00 USD | 1,790,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 18,780,000.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 1,760,000.00 USD | 1,760,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 18,730,000.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 1,720,000.00 USD | 1,720,000.00 USD | 29,580.00 USD | 4,150.00 USD | 30,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 18,660,000.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 1,650,000.00 USD | 1,650,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 18,590,000.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 68,110.00 USD | 246,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 1,650,000.00 USD | 1,650,000.00 USD | 58,790.00 USD | 23,780.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 18,550,000.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 1,560,000.00 USD | 1,560,000.00 USD | 37,820.00 USD | 16,800.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 18,460,000.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 1,490,000.00 USD | 1,490,000.00 USD | 15,350.00 USD | 5,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 18,350,000.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 1,460,000.00 USD | 1,460,000.00 USD | 41,350.00 USD | 12,240.00 USD | 46,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 18,300,000.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 1,360,000.00 USD | 1,360,000.00 USD | 13,350.00 USD | 20,950.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 18,250,000.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 40,290.00 USD | 177,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 1,310,000.00 USD | 1,310,000.00 USD | 33,630.00 USD | 16,150.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 18,200,000.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 1,230,000.00 USD | 1,230,000.00 USD | 17,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 18,180,000.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 1,210,000.00 USD | 1,210,000.00 USD | 37,930.00 USD | 2,570.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 18,150,000.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 1,160,000.00 USD | 1,160,000.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 18,130,000.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 1,140,000.00 USD | 1,140,000.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 18,090,000.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 50,130.00 USD | 137,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 1,060,000.00 USD | 1,060,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 18,070,000.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 1,040,000.00 USD | 1,040,000.00 USD | 86,290.00 USD | 38,770.00 USD | 57.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 18,050,000.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 917,600.00 USD | 917,600.00 USD | 73,580.00 USD | 27,960.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 18,010,000.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 790,340.00 USD | 790,340.00 USD | 30,650.00 USD | 1,080.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 17,870,000.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 758,540.00 USD | 758,540.00 USD | 54,340.00 USD | 14,120.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,690,000.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 86,320.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 620,770.00 USD | 620,770.00 USD | 976.86 USD | 30,860.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 17,540,000.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 585,120.00 USD | 585,120.00 USD | 34,130.00 USD | 42,700.00 USD | 82,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 17,190,000.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 425,510.00 USD | 425,510.00 USD | 23,940.00 USD | 3,600.00 USD | 0.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 16,720,000.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 397,970.00 USD | 397,970.00 USD | 97,980.00 USD | 29,320.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 16,290,000.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 248,520.00 USD | 248,520.00 USD | 98,180.00 USD | 17,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 15,390,000.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 1,240.00 USD | 1,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 133,280.00 USD | 133,280.00 USD | 96,940.00 USD | 23,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 14,800,000.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 13,330.00 USD | 13,330.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 14,240,000.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 13,870,000.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 13,480,000.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,970,000.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 12,320,000.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 11,910,000.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 106.40 USD | 106.40 USD | 0.00 USD | 0.00 USD | 106.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 11,100,000.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 18,870.00 USD | 18,870.00 USD | 632.30 USD | 18,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 9,910,000.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 100,050.00 USD | 100,050.00 USD | 1,890.00 USD | 79,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 8,860,000.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.16` | 151,360.00 USD | 151,360.00 USD | 337.20 USD | 50,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 7,370,000.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 199,100.00 USD | 199,100.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 6,060,000.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 393,210.00 USD | 393,210.00 USD | 43,350.00 USD | 52,080.00 USD | 98,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,630,000.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 779,220.00 USD | 779,220.00 USD | 262,690.00 USD | 80,150.00 USD | 43,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,870,000.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 1,030,000.00 USD | 1,030,000.00 USD | 69,220.00 USD | 84,150.00 USD | 96,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 3,160,000.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 1,170,000.00 USD | 1,170,000.00 USD | 28,620.00 USD | 41,930.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,860,000.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 1,430,000.00 USD | 1,430,000.00 USD | 38,150.00 USD | 34,520.00 USD | 186,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 2,290,000.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 60,470.00 USD | 41,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,880,000.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 1,690,000.00 USD | 1,690,000.00 USD | 32,630.00 USD | 66,390.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,810,000.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 1,940,000.00 USD | 1,940,000.00 USD | 197,970.00 USD | 53,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,640,000.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 6,720.00 USD | 456,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.36` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 83,880.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 1,280,000.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 2,150,000.00 USD | 2,150,000.00 USD | 51,260.00 USD | 55,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 962,530.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 871,150.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 2,470,000.00 USD | 2,470,000.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 677,690.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 2,590,000.00 USD | 2,590,000.00 USD | 42,610.00 USD | 18,500.00 USD | 52,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 536,960.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 99,610.00 USD | 556,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 2,650,000.00 USD | 2,650,000.00 USD | 34,610.00 USD | 13,980.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.46` | 264,830.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 2,670,000.00 USD | 2,670,000.00 USD | 14,310.00 USD | 4,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 128,570.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 2,740,000.00 USD | 2,740,000.00 USD | 19,080.00 USD | 18,560.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 88,130.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 2,780,000.00 USD | 2,780,000.00 USD | 29,340.00 USD | 13,170.00 USD | 418.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 2,850,000.00 USD | 2,850,000.00 USD | 16,150.00 USD | 16,150.00 USD | 29,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 94,830.00 USD | 94,830.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 2,110.00 USD | 558,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 2,920,000.00 USD | 2,920,000.00 USD | 64,190.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 2,990,000.00 USD | 2,990,000.00 USD | 45,400.00 USD | 75.80 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 3,180,000.00 USD | 3,180,000.00 USD | 124,870.00 USD | 289.75 USD | 67,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 3,260,000.00 USD | 3,260,000.00 USD | 42,200.00 USD | 0.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 222,010.00 USD | 222,010.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 60,080.00 USD | 618,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 3,330,000.00 USD | 3,330,000.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 313.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 3,580,000.00 USD | 3,580,000.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 484,570.00 USD | 484,570.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 3,710,000.00 USD | 3,710,000.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 2,100.00 USD | 620,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.76` | 3,760,000.00 USD | 3,760,000.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 532,760.00 USD | 532,760.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 3,840,000.00 USD | 3,840,000.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 14,340.00 USD | 66.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 672,880.00 USD | 672,880.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 3,880,000.00 USD | 3,880,000.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 873,430.00 USD | 873,430.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 4,010,000.00 USD | 4,010,000.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 2,440.00 USD | 623,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 4,080,000.00 USD | 4,080,000.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 4,180,000.00 USD | 4,180,000.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 4,240,000.00 USD | 4,240,000.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 4,410,000.00 USD | 4,410,000.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 4,470,000.00 USD | 4,470,000.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 4,580,000.00 USD | 4,580,000.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 4,740,000.00 USD | 4,740,000.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 4,850,000.00 USD | 4,850,000.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 4,950,000.00 USD | 4,950,000.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 5,330,000.00 USD | 5,330,000.00 USD | 209,440.00 USD | 65,620.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 5,750,000.00 USD | 5,750,000.00 USD | 187,660.00 USD | 88,160.00 USD | 147,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 5,960,000.00 USD | 5,960,000.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 6,030,000.00 USD | 6,030,000.00 USD | 36,180.00 USD | 16,940.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 6,290,000.00 USD | 6,290,000.00 USD | 138,630.00 USD | 60,020.00 USD | 63,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 6,470,000.00 USD | 6,470,000.00 USD | 92,340.00 USD | 33,200.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 6,710,000.00 USD | 6,710,000.00 USD | 126,410.00 USD | 37,730.00 USD | 67,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 6,890,000.00 USD | 6,890,000.00 USD | 112,590.00 USD | 42,150.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 7,050,000.00 USD | 7,050,000.00 USD | 77,890.00 USD | 43,590.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 7,110,000.00 USD | 7,110,000.00 USD | 12,890.00 USD | 16,530.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 7,140,000.00 USD | 7,140,000.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 552.48 USD | 623,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 7,220,000.00 USD | 7,220,000.00 USD | 43,220.00 USD | 22,010.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 7,360,000.00 USD | 7,360,000.00 USD | 83,960.00 USD | 17,410.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 7,470,000.00 USD | 7,470,000.00 USD | 57,170.00 USD | 16,300.00 USD | 36,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 7,480,000.00 USD | 7,480,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 7,520,000.00 USD | 7,520,000.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 624,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 7,560,000.00 USD | 7,560,000.00 USD | 19,360.00 USD | 9,040.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 7,600,000.00 USD | 7,600,000.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 7,650,000.00 USD | 7,650,000.00 USD | 18,820.00 USD | 12,140.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 7,730,000.00 USD | 7,730,000.00 USD | 57,850.00 USD | 13,980.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 7,770,000.00 USD | 7,770,000.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.46` | 7,780,000.00 USD | 7,780,000.00 USD | 411.51 USD | 9,440.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 7,790,000.00 USD | 7,790,000.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 7,810,000.00 USD | 7,810,000.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 7,870,000.00 USD | 7,870,000.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 7,890,000.00 USD | 7,890,000.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,870.00 USD | 626,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.56` | 7,930,000.00 USD | 7,930,000.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 7,950,000.00 USD | 7,950,000.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 7,970,000.00 USD | 7,970,000.00 USD | 15,910.00 USD | 3,320.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 8,000,000.00 USD | 8,000,000.00 USD | 13,610.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 8,050,000.00 USD | 8,050,000.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 527.51 USD | 626,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 8,080,000.00 USD | 8,080,000.00 USD | 4,580.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 8,100,000.00 USD | 8,100,000.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 8,130,000.00 USD | 8,130,000.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 8,170,000.00 USD | 8,170,000.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 8,230,000.00 USD | 8,230,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 8,250,000.00 USD | 8,250,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 8,280,000.00 USD | 8,280,000.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 8,290,000.00 USD | 8,290,000.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 8,320,000.00 USD | 8,320,000.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 627,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 8,360,000.00 USD | 8,360,000.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 8,370,000.00 USD | 8,370,000.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 8,390,000.00 USD | 8,390,000.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 8,400,000.00 USD | 8,400,000.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 8,410,000.00 USD | 8,410,000.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 8,410,000.00 USD | 8,410,000.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 8,450,000.00 USD | 8,450,000.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 8,480,000.00 USD | 8,480,000.00 USD | 11,890.00 USD | 7,680.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 14,560,000.00 USD | 14,560,000.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 14,580,000.00 USD | 14,580,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 14,580,000.00 USD | 14,580,000.00 USD | 303.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 1,520.00 USD | 628,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.06` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.10` | 14,620,000.00 USD | 14,620,000.00 USD | 18,460.00 USD | 5,730.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.12` | 14,620,000.00 USD | 14,620,000.00 USD | 945.50 USD | 4,010.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.14` | 14,620,000.00 USD | 14,620,000.00 USD | 321.45 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.16` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 57.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.18` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 3,960.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.20` | 14,650,000.00 USD | 14,650,000.00 USD | 972.55 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.22` | 14,680,000.00 USD | 14,680,000.00 USD | 23,980.00 USD | 213.60 USD | 37.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.24` | 14,710,000.00 USD | 14,710,000.00 USD | 18,770.00 USD | 4,640.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.26` | 14,730,000.00 USD | 14,730,000.00 USD | 463.75 USD | 5,860.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 14,740,000.00 USD | 14,740,000.00 USD | 9,830.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,280.00 USD | 633,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 2,990.00 USD | 636,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 347.04 USD | 637,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 637,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 321.55 USD | 638,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 663,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.15` | 368.14 USD | 663,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 664,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 720,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 721,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 722,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 17,510.00 USD | 740,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 10,770.00 USD | 750,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 830,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 2,330.00 USD | 832,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 121,870.00 USD | 954,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 5,480.00 USD | 960,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 72,830.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 707,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 2,340,000.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,270.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 10,800.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 17,530.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 12,670,000.00 USD | 0.00 USD | 486.45 USD | `-78.61%` | `207,000.00` |
| `Live` | `Long` | `2.45` | 12,670,000.00 USD | 0.00 USD | 1,230.00 USD | `-77.70%` | `502,600.00` |
| `Live` | `Long` | `2.65` | 12,670,000.00 USD | 0.00 USD | 4,150.00 USD | `-75.88%` | `1,567,100.00` |
| `Live` | `Long` | `2.75` | 12,660,000.00 USD | 0.00 USD | 27,030.00 USD | `-74.97%` | `9,829,500.00` |
| `Live` | `Long` | `2.85` | 12,630,000.00 USD | 0.00 USD | 2,620.00 USD | `-74.06%` | `920,000.00` |
| `Live` | `Long` | `3.05` | 12,630,000.00 USD | 0.00 USD | 6,390.00 USD | `-72.24%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 12,630,000.00 USD | 0.00 USD | 961.07 USD | `-71.33%` | `305,100.00` |
| `Live` | `Long` | `3.35` | 12,620,000.00 USD | 0.00 USD | 592.95 USD | `-69.51%` | `177,000.00` |
| `Live` | `Long` | `3.45` | 12,620,000.00 USD | 0.00 USD | 8,190.00 USD | `-68.60%` | `2,373,100.00` |
| `Live` | `Long` | `3.55` | 12,620,000.00 USD | 0.00 USD | 2,510.00 USD | `-67.69%` | `707,000.00` |
| `Live` | `Long` | `3.65` | 12,610,000.00 USD | 0.00 USD | 2,630.00 USD | `-66.78%` | `719,500.00` |
| `Live` | `Long` | `3.75` | 12,610,000.00 USD | 0.00 USD | 3,750.00 USD | `-65.87%` | `1,000,000.00` |
| `Live` | `Long` | `3.85` | 12,610,000.00 USD | 0.00 USD | 13,360.00 USD | `-64.96%` | `3,469,700.00` |
| `Live` | `Long` | `4.05` | 12,590,000.00 USD | 0.00 USD | 6,300.00 USD | `-63.14%` | `1,554,700.00` |
| `Live` | `Long` | `4.35` | 12,590,000.00 USD | 0.00 USD | 12,630.00 USD | `-60.41%` | `2,903,200.00` |
| `Live` | `Long` | `4.45` | 12,570,000.00 USD | 0.00 USD | 4,470.00 USD | `-59.50%` | `1,005,500.00` |
| `Live` | `Long` | `4.65` | 12,570,000.00 USD | 0.00 USD | 17,540.00 USD | `-57.68%` | `3,772,100.00` |
| `Live` | `Long` | `4.75` | 12,550,000.00 USD | 0.00 USD | 50,880.00 USD | `-56.77%` | `10,712,500.00` |
| `Live` | `Long` | `4.85` | 12,500,000.00 USD | 0.00 USD | 239,270.00 USD | `-55.86%` | `49,334,900.00` |
| `Live` | `Long` | `4.95` | 12,260,000.00 USD | 0.00 USD | 883.08 USD | `-54.95%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 12,260,000.00 USD | 0.00 USD | 91,360.00 USD | `-54.04%` | `18,091,700.00` |
| `Live` | `Long` | `5.25` | 12,170,000.00 USD | 0.00 USD | 886.73 USD | `-52.22%` | `168,900.00` |
| `Live` | `Long` | `5.35` | 12,170,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.31%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,630,000.00 USD | 0.00 USD | 20,990.00 USD | `-50.40%` | `3,850,700.00` |
| `Live` | `Long` | `5.55` | 11,610,000.00 USD | 0.00 USD | 748.14 USD | `-49.49%` | `134,800.00` |
| `Live` | `Long` | `5.65` | 11,610,000.00 USD | 0.00 USD | 35,600.00 USD | `-48.58%` | `6,300,800.00` |
| `Live` | `Long` | `5.75` | 11,570,000.00 USD | 0.00 USD | 1,520.00 USD | `-47.67%` | `263,500.00` |
| `Live` | `Long` | `5.85` | 11,570,000.00 USD | 0.00 USD | 22,830.00 USD | `-46.76%` | `3,901,800.00` |
| `Live` | `Long` | `5.95` | 11,550,000.00 USD | 0.00 USD | 790.76 USD | `-45.85%` | `132,900.00` |
| `Live` | `Long` | `6.05` | 11,550,000.00 USD | 0.00 USD | 68,690.00 USD | `-44.93%` | `11,354,000.00` |
| `Live` | `Long` | `6.15` | 11,480,000.00 USD | 0.00 USD | 9,240.00 USD | `-44.02%` | `1,502,600.00` |
| `Live` | `Long` | `6.25` | 11,470,000.00 USD | 0.00 USD | 80,020.00 USD | `-43.11%` | `12,802,500.00` |
| `Live` | `Long` | `6.35` | 11,390,000.00 USD | 0.00 USD | 23,300.00 USD | `-42.20%` | `3,669,800.00` |
| `Live` | `Long` | `6.45` | 11,360,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.29%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 11,350,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.38%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 11,350,000.00 USD | 0.00 USD | 9,260.00 USD | `-39.47%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 11,340,000.00 USD | 0.00 USD | 7,650.00 USD | `-38.56%` | `1,133,600.00` |
| `Live` | `Long` | `6.85` | 11,340,000.00 USD | 0.00 USD | 34,470.00 USD | `-37.65%` | `5,031,900.00` |
| `Live` | `Long` | `6.95` | 11,300,000.00 USD | 0.00 USD | 37,510.00 USD | `-36.74%` | `5,397,100.00` |
| `Live` | `Long` | `7.05` | 11,260,000.00 USD | 0.00 USD | 14,440.00 USD | `-35.83%` | `2,047,600.00` |
| `Live` | `Long` | `7.15` | 11,250,000.00 USD | 0.00 USD | 686,800.00 USD | `-34.92%` | `96,055,400.00` |
| `Live` | `Long` | `7.25` | 10,560,000.00 USD | 0.00 USD | 8,460.00 USD | `-34.01%` | `1,167,100.00` |
| `Live` | `Long` | `7.35` | 10,550,000.00 USD | 0.00 USD | 52,130.00 USD | `-33.10%` | `7,092,500.00` |
| `Live` | `Long` | `7.45` | 10,500,000.00 USD | 0.00 USD | 9,870.00 USD | `-32.19%` | `1,324,400.00` |
| `Live` | `Long` | `7.55` | 10,490,000.00 USD | 0.00 USD | 19,770.00 USD | `-31.28%` | `2,618,600.00` |
| `Live` | `Long` | `7.65` | 10,470,000.00 USD | 0.00 USD | 9,240.00 USD | `-30.37%` | `1,208,100.00` |
| `Live` | `Long` | `7.75` | 10,460,000.00 USD | 0.00 USD | 14,100.00 USD | `-29.46%` | `1,819,600.00` |
| `Live` | `Long` | `7.85` | 10,450,000.00 USD | 0.00 USD | 3,010.00 USD | `-28.55%` | `383,000.00` |
| `Live` | `Long` | `7.95` | 10,450,000.00 USD | 0.00 USD | 171,890.00 USD | `-27.64%` | `21,621,200.00` |
| `Live` | `Long` | `8.05` | 10,270,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-26.73%` | `174,682,100.00` |
| `Live` | `Long` | `8.15` | 8,870,000.00 USD | 0.00 USD | 29,940.00 USD | `-25.82%` | `3,673,500.00` |
| `Live` | `Long` | `8.25` | 8,840,000.00 USD | 0.00 USD | 35,750.00 USD | `-24.91%` | `4,333,100.00` |
| `Live` | `Long` | `8.35` | 8,800,000.00 USD | 0.00 USD | 7,780.00 USD | `-24.00%` | `932,100.00` |
| `Live` | `Long` | `8.45` | 8,790,000.00 USD | 0.00 USD | 53,810.00 USD | `-23.09%` | `6,368,100.00` |
| `Live` | `Long` | `8.55` | 8,740,000.00 USD | 0.00 USD | 21,580.00 USD | `-22.18%` | `2,523,600.00` |
| `Live` | `Long` | `8.65` | 8,720,000.00 USD | 0.00 USD | 15,370.00 USD | `-21.27%` | `1,777,300.00` |
| `Live` | `Long` | `8.75` | 8,700,000.00 USD | 0.00 USD | 312,090.00 USD | `-20.36%` | `35,667,200.00` |
| `Live` | `Long` | `8.85` | 8,390,000.00 USD | 0.00 USD | 28,570.00 USD | `-19.45%` | `3,228,700.00` |
| `Live` | `Long` | `8.95` | 8,360,000.00 USD | 0.00 USD | 505,780.00 USD | `-18.54%` | `56,512,000.00` |
| `Live` | `Long` | `9.05` | 7,860,000.00 USD | 0.00 USD | 76,580.00 USD | `-17.63%` | `8,462,300.00` |
| `Live` | `Long` | `9.15` | 7,780,000.00 USD | 0.00 USD | 3,720,000.00 USD | `-16.72%` | `406,248,000.00` |
| `Live` | `Long` | `9.25` | 4,060,000.00 USD | 0.00 USD | 41,710.00 USD | `-15.81%` | `4,509,300.00` |
| `Live` | `Long` | `9.35` | 4,020,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-14.90%` | `229,832,900.00` |
| `Live` | `Long` | `9.45` | 1,870,000.00 USD | 0.00 USD | 26,730.00 USD | `-13.99%` | `2,829,000.00` |
| `Live` | `Long` | `9.55` | 1,850,000.00 USD | 0.00 USD | 12,490.00 USD | `-13.08%` | `1,307,500.00` |
| `Live` | `Long` | `9.65` | 1,830,000.00 USD | 0.00 USD | 9,080.00 USD | `-12.17%` | `940,600.00` |
| `Live` | `Long` | `9.75` | 1,820,000.00 USD | 0.00 USD | 54,360.00 USD | `-11.26%` | `5,575,400.00` |
| `Live` | `Long` | `9.85` | 1,770,000.00 USD | 0.00 USD | 19,550.00 USD | `-10.35%` | `1,985,100.00` |
| `Live` | `Long` | `9.95` | 1,750,000.00 USD | 0.00 USD | 760,400.00 USD | `-9.44%` | `76,422,600.00` |
| `Live` | `Long` | `10.05` | 989,720.00 USD | 0.00 USD | 647,590.00 USD | `-8.53%` | `64,436,800.00` |
| `Live` | `Long` | `10.15` | 342,130.00 USD | 0.00 USD | 28,910.00 USD | `-7.62%` | `2,848,100.00` |
| `Live` | `Long` | `10.25` | 313,230.00 USD | 0.00 USD | 35,700.00 USD | `-6.71%` | `3,482,600.00` |
| `Live` | `Long` | `10.35` | 277,530.00 USD | 0.00 USD | 14,650.00 USD | `-5.80%` | `1,415,900.00` |
| `Live` | `Long` | `10.45` | 262,880.00 USD | 0.00 USD | 16,780.00 USD | `-4.89%` | `1,606,100.00` |
| `Live` | `Long` | `10.55` | 246,090.00 USD | 0.00 USD | 68,110.00 USD | `-3.98%` | `6,456,000.00` |
| `Live` | `Long` | `10.65` | 177,980.00 USD | 0.00 USD | 40,290.00 USD | `-3.07%` | `3,782,800.00` |
| `Live` | `Long` | `10.75` | 137,690.00 USD | 0.00 USD | 50,130.00 USD | `-2.16%` | `4,663,700.00` |
| `Live` | `Long` | `10.85` | 87,560.00 USD | 0.00 USD | 86,320.00 USD | `-1.25%` | `7,955,900.00` |
| `Live` | `Long` | `10.95` | 1,240.00 USD | 0.00 USD | 1,240.00 USD | `-0.34%` | `113,000.00` |
| `Live` | `Short` | `11.15` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | `+1.48%` | `40,371,500.00` |
| `Live` | `Short` | `11.35` | 456,860.00 USD | 6,720.00 USD | 0.00 USD | `+3.30%` | `591,900.00` |
| `Live` | `Short` | `11.45` | 556,480.00 USD | 99,610.00 USD | 0.00 USD | `+4.21%` | `8,700,000.00` |
| `Live` | `Short` | `11.55` | 558,580.00 USD | 2,110.00 USD | 0.00 USD | `+5.12%` | `182,300.00` |
| `Live` | `Short` | `11.65` | 618,660.00 USD | 60,080.00 USD | 0.00 USD | `+6.03%` | `5,156,700.00` |
| `Live` | `Short` | `11.75` | 620,760.00 USD | 2,100.00 USD | 0.00 USD | `+6.94%` | `178,700.00` |
| `Live` | `Short` | `11.85` | 623,200.00 USD | 2,440.00 USD | 0.00 USD | `+7.85%` | `206,300.00` |
| `Live` | `Short` | `12.25` | 623,750.00 USD | 552.48 USD | 0.00 USD | `+11.50%` | `45,100.00` |
| `Live` | `Short` | `12.35` | 624,490.00 USD | 736.06 USD | 0.00 USD | `+12.41%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 626,360.00 USD | 1,870.00 USD | 0.00 USD | `+14.23%` | `149,100.00` |
| `Live` | `Short` | `12.65` | 626,890.00 USD | 527.51 USD | 0.00 USD | `+15.14%` | `41,700.00` |
| `Live` | `Short` | `12.85` | 627,030.00 USD | 138.78 USD | 0.00 USD | `+16.96%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 628,540.00 USD | 1,520.00 USD | 0.00 USD | `+18.78%` | `116,200.00` |
| `Live` | `Short` | `13.45` | 633,830.00 USD | 5,280.00 USD | 0.00 USD | `+22.42%` | `392,900.00` |
| `Live` | `Short` | `13.55` | 636,810.00 USD | 2,990.00 USD | 0.00 USD | `+23.33%` | `220,300.00` |
| `Live` | `Short` | `14.05` | 637,160.00 USD | 347.04 USD | 0.00 USD | `+27.88%` | `24,700.00` |
| `Live` | `Short` | `14.45` | 637,700.00 USD | 541.88 USD | 0.00 USD | `+31.52%` | `37,500.00` |
| `Live` | `Short` | `14.75` | 638,020.00 USD | 321.55 USD | 0.00 USD | `+34.25%` | `21,800.00` |
| `Live` | `Short` | `14.95` | 663,360.00 USD | 25,330.00 USD | 0.00 USD | `+36.07%` | `1,694,600.00` |
| `Live` | `Short` | `15.15` | 663,730.00 USD | 368.14 USD | 0.00 USD | `+37.89%` | `24,300.00` |
| `Live` | `Short` | `15.55` | 664,560.00 USD | 838.14 USD | 0.00 USD | `+41.53%` | `53,900.00` |
| `Live` | `Short` | `15.85` | 720,910.00 USD | 56,350.00 USD | 0.00 USD | `+44.26%` | `3,554,900.00` |
| `Live` | `Short` | `15.95` | 721,050.00 USD | 138.76 USD | 0.00 USD | `+45.17%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 722,580.00 USD | 1,530.00 USD | 0.00 USD | `+48.81%` | `93,700.00` |
| `Live` | `Short` | `16.55` | 740,090.00 USD | 17,510.00 USD | 0.00 USD | `+50.63%` | `1,058,000.00` |
| `Live` | `Short` | `16.85` | 750,860.00 USD | 10,770.00 USD | 0.00 USD | `+53.36%` | `639,000.00` |
| `Live` | `Short` | `16.95` | 830,630.00 USD | 79,770.00 USD | 0.00 USD | `+54.27%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 832,960.00 USD | 2,330.00 USD | 0.00 USD | `+56.09%` | `136,100.00` |
| `Live` | `Short` | `17.45` | 954,830.00 USD | 121,870.00 USD | 0.00 USD | `+58.82%` | `6,984,000.00` |
| `Live` | `Short` | `17.75` | 960,320.00 USD | 5,480.00 USD | 0.00 USD | `+61.55%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 1,210,000.00 USD | 249,580.00 USD | 0.00 USD | `+62.46%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 1,210,000.00 USD | 621.07 USD | 0.00 USD | `+63.37%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 1,210,000.00 USD | 1,970.00 USD | 0.00 USD | `+64.29%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 1,240,000.00 USD | 27,790.00 USD | 0.00 USD | `+66.11%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 1,240,000.00 USD | 3,890.00 USD | 0.00 USD | `+67.93%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,240,000.00 USD | 185.50 USD | 0.00 USD | `+68.84%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 1,320,000.00 USD | 72,830.00 USD | 0.00 USD | `+69.75%` | `3,905,000.00` |
| `Live` | `Short` | `18.75` | 2,020,000.00 USD | 707,620.00 USD | 0.00 USD | `+70.66%` | `37,739,700.00` |
| `Live` | `Short` | `18.85` | 2,030,000.00 USD | 456.17 USD | 0.00 USD | `+71.57%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,040,000.00 USD | 16,250.00 USD | 0.00 USD | `+72.48%` | `857,700.00` |
| `Live` | `Short` | `19.65` | 2,080,000.00 USD | 38,790.00 USD | 0.00 USD | `+78.85%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,080,000.00 USD | 291.27 USD | 0.00 USD | `+81.58%` | `14,600.00` |
| `Live` | `Short` | `20.35` | 4,420,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+85.22%` | `115,024,600.00` |
| `Live` | `Short` | `20.45` | 4,420,000.00 USD | 1,270.00 USD | 0.00 USD | `+86.13%` | `62,300.00` |
| `Live` | `Short` | `20.55` | 4,430,000.00 USD | 10,800.00 USD | 0.00 USD | `+87.04%` | `525,500.00` |
| `Live` | `Short` | `21.95` | 4,450,000.00 USD | 17,530.00 USD | 0.00 USD | `+99.78%` | `798,800.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 583,520.00 USD | 0.00 USD | 431.68 USD | `-67.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 583,080.00 USD | 0.00 USD | 290.29 USD | `-58.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 582,790.00 USD | 0.00 USD | 120.22 USD | `-52.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 582,670.00 USD | 0.00 USD | 107.09 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 582,570.00 USD | 0.00 USD | 3,760.00 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 578,800.00 USD | 0.00 USD | 133.00 USD | `-39.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 578,670.00 USD | 0.00 USD | 3,770.00 USD | `-35.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 574,900.00 USD | 0.00 USD | 2,070.00 USD | `-34.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 572,830.00 USD | 0.00 USD | 3,740.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 569,090.00 USD | 0.00 USD | 1,050.00 USD | `-31.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 568,030.00 USD | 0.00 USD | 146.80 USD | `-28.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 567,890.00 USD | 0.00 USD | 5,000.00 USD | `-26.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 562,890.00 USD | 0.00 USD | 564.79 USD | `-25.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 562,320.00 USD | 0.00 USD | 10,660.00 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 551,660.00 USD | 0.00 USD | 1,360.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 550,300.00 USD | 0.00 USD | 30,250.00 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 520,050.00 USD | 0.00 USD | 186.84 USD | `-21.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 519,860.00 USD | 0.00 USD | 742.88 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 519,120.00 USD | 0.00 USD | 196.47 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 518,930.00 USD | 0.00 USD | 1,320.00 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 517,610.00 USD | 0.00 USD | 2,240.00 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 515,360.00 USD | 0.00 USD | 194.90 USD | `-16.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 515,170.00 USD | 0.00 USD | 7,050.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 508,120.00 USD | 0.00 USD | 10,530.00 USD | `-13.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 497,590.00 USD | 0.00 USD | 3,550.00 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 494,040.00 USD | 0.00 USD | 6,490.00 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 487,560.00 USD | 0.00 USD | 23,380.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 464,180.00 USD | 0.00 USD | 299,650.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 164,520.00 USD | 0.00 USD | 2,590.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 161,930.00 USD | 0.00 USD | 1,050.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 160,880.00 USD | 0.00 USD | 92,770.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 68,110.00 USD | 0.00 USD | 7,610.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 60,500.00 USD | 0.00 USD | 21,220.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 39,280.00 USD | 0.00 USD | 24,160.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 15,130.00 USD | 0.00 USD | 2,300.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 12,820.00 USD | 0.00 USD | 6,800.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 6,020.00 USD | 0.00 USD | 5,870.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 148.92 USD | 0.00 USD | 148.92 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 18,860.00 USD | 18,860.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 19,820.00 USD | 958.90 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 81,850.00 USD | 62,030.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 82,880.00 USD | 1,030.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 83,170.00 USD | 287.39 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 83,290.00 USD | 116.66 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 84,020.00 USD | 732.79 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 88,480.00 USD | 4,460.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 89,130.00 USD | 651.75 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 89,290.00 USD | 156.55 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 137,400.00 USD | 48,110.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 139,280.00 USD | 1,880.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 155,260.00 USD | 15,980.00 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 155,910.00 USD | 649.61 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 156,770.00 USD | 859.05 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 277,070.00 USD | 120,300.00 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 327,310.00 USD | 50,240.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 340,470.00 USD | 13,170.00 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 360,530.00 USD | 20,060.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 360,990.00 USD | 461.02 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 367,180.00 USD | 6,190.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 368,230.00 USD | 1,050.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 369,550.00 USD | 1,320.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 374,280.00 USD | 4,730.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 376,470.00 USD | 2,200.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 376,640.00 USD | 165.31 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 378,790.00 USD | 2,150.00 USD | 0.00 USD | `+24.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 380,850.00 USD | 2,060.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 385,200.00 USD | 4,350.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 385,460.00 USD | 266.44 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 410,250.00 USD | 24,790.00 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 410,760.00 USD | 506.57 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 414,170.00 USD | 3,410.00 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 414,390.00 USD | 218.25 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 417,000.00 USD | 2,610.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 429,920.00 USD | 12,920.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 430,880.00 USD | 950.82 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 443,490.00 USD | 12,620.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 445,700.00 USD | 2,200.00 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 678,740.00 USD | 233,040.00 USD | 0.00 USD | `+38.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 679,920.00 USD | 1,180.00 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 680,810.00 USD | 893.01 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 681,200.00 USD | 388.75 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 682,150.00 USD | 949.96 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 684,480.00 USD | 2,330.00 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 689,820.00 USD | 5,340.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 695,170.00 USD | 5,350.00 USD | 0.00 USD | `+45.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 704,340.00 USD | 9,170.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 711,140.00 USD | 6,800.00 USD | 0.00 USD | `+46.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 729,900.00 USD | 18,760.00 USD | 0.00 USD | `+47.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 764,130.00 USD | 34,220.00 USD | 0.00 USD | `+48.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 770,710.00 USD | 6,580.00 USD | 0.00 USD | `+49.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 780,640.00 USD | 9,930.00 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 793,960.00 USD | 13,320.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 808,200.00 USD | 14,240.00 USD | 0.00 USD | `+52.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 892,550.00 USD | 84,360.00 USD | 0.00 USD | `+53.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 894,250.00 USD | 1,700.00 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 906,740.00 USD | 12,500.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 908,460.00 USD | 1,710.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 910,760.00 USD | 2,300.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,010,000.00 USD | 98,330.00 USD | 0.00 USD | `+57.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,030,000.00 USD | 18,030.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,030,000.00 USD | 4,390.00 USD | 0.00 USD | `+59.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,040,000.00 USD | 4,410.00 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,040,000.00 USD | 4,440.00 USD | 0.00 USD | `+61.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,040,000.00 USD | 4,460.00 USD | 0.00 USD | `+62.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,050,000.00 USD | 448.75 USD | 0.00 USD | `+63.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,080,000.00 USD | 35,590.00 USD | 0.00 USD | `+64.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,080,000.00 USD | 453.75 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,080,000.00 USD | 830.38 USD | 0.00 USD | `+66.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,080,000.00 USD | 458.75 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,080,000.00 USD | 461.25 USD | 0.00 USD | `+67.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,090,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,090,000.00 USD | 466.25 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,090,000.00 USD | 468.75 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,090,000.00 USD | 471.25 USD | 0.00 USD | `+71.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,090,000.00 USD | 473.75 USD | 0.00 USD | `+72.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,160,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,160,000.00 USD | 574.50 USD | 0.00 USD | `+74.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,160,000.00 USD | 577.50 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,160,000.00 USD | 2,710.00 USD | 0.00 USD | `+76.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,160,000.00 USD | 972.50 USD | 0.00 USD | `+77.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,170,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,170,000.00 USD | 1,680.00 USD | 0.00 USD | `+78.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,170,000.00 USD | 1,690.00 USD | 0.00 USD | `+79.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,170,000.00 USD | 992.50 USD | 0.00 USD | `+80.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,170,000.00 USD | 997.50 USD | 0.00 USD | `+81.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,790,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+82.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,790,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,790,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,790,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,790,000.00 USD | 1,020.00 USD | 0.00 USD | `+86.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,790,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,790,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,800,000.00 USD | 1,860.00 USD | 0.00 USD | `+88.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,800,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,800,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,800,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,800,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,810,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,850,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+94.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,850,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,850,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,860,000.00 USD | 1,080.00 USD | 0.00 USD | `+97.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,860,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,860,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,860,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `9.86` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD |
| `1D` | `9.90` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD |
| `1D` | `9.92` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 13,840.00 USD | 5,510.00 USD | 118.68 USD |
| `1D` | `9.94` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD |
| `1D` | `9.96` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 7,630.00 USD | 5,270.00 USD | 8,380.00 USD |
| `1D` | `9.98` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 0.00 USD | 6,510.00 USD | 11,790.00 USD |
| `1D` | `10.04` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD |
| `1D` | `10.06` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD |
| `1D` | `10.14` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD |
| `1D` | `10.16` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD |
| `1D` | `10.18` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD |
| `1D` | `10.20` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD |
| `1D` | `10.22` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD |
| `1D` | `10.24` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,520.00 USD |
| `7D` | `10.24` | 20,290,000.00 USD | 0.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD |
| `1D` | `10.26` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `10.26` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD |
| `1D` | `10.28` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD |
| `7D` | `10.28` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD |
| `1D` | `10.30` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD |
| `7D` | `10.30` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD |
| `1D` | `10.32` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,380.00 USD |
| `7D` | `10.32` | 19,540,000.00 USD | 0.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `1D` | `10.34` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `10.34` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD |
| `1D` | `10.36` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `10.36` | 19,270,000.00 USD | 0.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD |
| `1D` | `10.38` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `10.38` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD |
| `1D` | `10.40` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD |
| `7D` | `10.40` | 19,180,000.00 USD | 0.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD |
| `1D` | `10.42` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 20,220.00 USD | 10,800.00 USD | 7,000.00 USD |
| `7D` | `10.42` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD |
| `1D` | `10.44` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `10.44` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD |
| `1D` | `10.46` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `10.46` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD |
| `1D` | `10.48` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD |
| `7D` | `10.48` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `10.50` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD |
| `7D` | `10.50` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD |
| `1D` | `10.52` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 29,580.00 USD | 4,150.00 USD | 30,670.00 USD |
| `7D` | `10.52` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD |
| `1D` | `10.54` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `10.54` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD |
| `1D` | `10.56` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 58,790.00 USD | 23,780.00 USD | 1,810.00 USD |
| `7D` | `10.56` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD |
| `1D` | `10.58` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 37,820.00 USD | 16,800.00 USD | 21,000.00 USD |
| `7D` | `10.58` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD |
| `1D` | `10.60` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 15,350.00 USD | 5,500.00 USD | 3,180.00 USD |
| `7D` | `10.60` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD |
| `1D` | `10.62` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 41,350.00 USD | 12,240.00 USD | 46,770.00 USD |
| `7D` | `10.62` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD |
| `1D` | `10.64` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 13,350.00 USD | 20,950.00 USD | 12,940.00 USD |
| `7D` | `10.64` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.66` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 33,630.00 USD | 16,150.00 USD | 34,150.00 USD |
| `7D` | `10.66` | 18,200,000.00 USD | 0.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.68` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 17,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 18,180,000.00 USD | 0.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.70` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 37,930.00 USD | 2,570.00 USD | 11,070.00 USD |
| `7D` | `10.70` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.72` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD |
| `7D` | `10.72` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD |
| `1D` | `10.74` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD |
| `7D` | `10.74` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD |
| `1D` | `10.76` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD |
| `7D` | `10.76` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD |
| `1D` | `10.78` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 86,290.00 USD | 38,770.00 USD | 57.12 USD |
| `7D` | `10.78` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD |
| `1D` | `10.80` | 917,600.00 USD | 0.00 USD | 917,600.00 USD | 73,580.00 USD | 27,960.00 USD | 25,730.00 USD |
| `7D` | `10.80` | 18,010,000.00 USD | 0.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD |
| `1D` | `10.82` | 790,340.00 USD | 0.00 USD | 790,340.00 USD | 30,650.00 USD | 1,080.00 USD | 68.68 USD |
| `7D` | `10.82` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD |
| `1D` | `10.84` | 758,540.00 USD | 0.00 USD | 758,540.00 USD | 54,340.00 USD | 14,120.00 USD | 69,300.00 USD |
| `7D` | `10.84` | 17,690,000.00 USD | 0.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.86` | 620,770.00 USD | 0.00 USD | 620,770.00 USD | 976.86 USD | 30,860.00 USD | 3,820.00 USD |
| `7D` | `10.86` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 585,120.00 USD | 0.00 USD | 585,120.00 USD | 34,130.00 USD | 42,700.00 USD | 82,790.00 USD |
| `7D` | `10.88` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD |
| `1D` | `10.90` | 425,510.00 USD | 0.00 USD | 425,510.00 USD | 23,940.00 USD | 3,600.00 USD | 0.39 USD |
| `7D` | `10.90` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.92` | 397,970.00 USD | 0.00 USD | 397,970.00 USD | 97,980.00 USD | 29,320.00 USD | 22,140.00 USD |
| `7D` | `10.92` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.94` | 248,520.00 USD | 0.00 USD | 248,520.00 USD | 98,180.00 USD | 17,060.00 USD | 0.00 USD |
| `7D` | `10.94` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.96` | 133,280.00 USD | 0.00 USD | 133,280.00 USD | 96,940.00 USD | 23,010.00 USD | 0.00 USD |
| `7D` | `10.96` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.98` | 13,330.00 USD | 0.00 USD | 13,330.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.98` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD |
| `7D` | `11.00` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `7D` | `11.02` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD |
| `7D` | `11.04` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `7D` | `11.06` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.08` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.08` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD |
| `1D` | `11.10` | 106.40 USD | 106.40 USD | 0.00 USD | 0.00 USD | 0.00 USD | 106.40 USD |
| `7D` | `11.10` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD |
| `1D` | `11.12` | 18,870.00 USD | 18,870.00 USD | 0.00 USD | 632.30 USD | 18,140.00 USD | 0.00 USD |
| `7D` | `11.12` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.14` | 100,050.00 USD | 100,050.00 USD | 0.00 USD | 1,890.00 USD | 79,290.00 USD | 0.00 USD |
| `7D` | `11.14` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD |
| `1D` | `11.16` | 151,360.00 USD | 151,360.00 USD | 0.00 USD | 337.20 USD | 50,970.00 USD | 0.00 USD |
| `7D` | `11.16` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.18` | 199,100.00 USD | 199,100.00 USD | 0.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD |
| `7D` | `11.18` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD |
| `1D` | `11.20` | 393,210.00 USD | 393,210.00 USD | 0.00 USD | 43,350.00 USD | 52,080.00 USD | 98,690.00 USD |
| `7D` | `11.20` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD |
| `1D` | `11.22` | 779,220.00 USD | 779,220.00 USD | 0.00 USD | 262,690.00 USD | 80,150.00 USD | 43,170.00 USD |
| `7D` | `11.22` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD |
| `1D` | `11.24` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 69,220.00 USD | 84,150.00 USD | 96,090.00 USD |
| `7D` | `11.24` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 28,620.00 USD | 41,930.00 USD | 70,350.00 USD |
| `7D` | `11.26` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD |
| `1D` | `11.28` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 38,150.00 USD | 34,520.00 USD | 186,730.00 USD |
| `7D` | `11.28` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 60,470.00 USD | 41,980.00 USD |
| `7D` | `11.30` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD |
| `1D` | `11.32` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 32,630.00 USD | 66,390.00 USD | 58,940.00 USD |
| `7D` | `11.32` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD |
| `1D` | `11.34` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 197,970.00 USD | 53,750.00 USD | 0.00 USD |
| `7D` | `11.34` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD |
| `1D` | `11.36` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 83,880.00 USD | 22,140.00 USD |
| `7D` | `11.36` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 51,260.00 USD | 55,490.00 USD | 0.00 USD |
| `7D` | `11.38` | 962,530.00 USD | 0.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD |
| `7D` | `11.40` | 871,150.00 USD | 0.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD |
| `7D` | `11.42` | 677,690.00 USD | 0.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD |
| `1D` | `11.44` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 42,610.00 USD | 18,500.00 USD | 52,860.00 USD |
| `7D` | `11.44` | 536,960.00 USD | 0.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 34,610.00 USD | 13,980.00 USD | 12,800.00 USD |
| `7D` | `11.46` | 264,830.00 USD | 0.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD |
| `1D` | `11.48` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 14,310.00 USD | 4,700.00 USD | 0.00 USD |
| `7D` | `11.48` | 128,570.00 USD | 0.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `11.50` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 19,080.00 USD | 18,560.00 USD | 34,640.00 USD |
| `7D` | `11.50` | 88,130.00 USD | 0.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD |
| `1D` | `11.52` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 29,340.00 USD | 13,170.00 USD | 418.82 USD |
| `7D` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `7D` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `1D` | `11.54` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 16,150.00 USD | 16,150.00 USD | 29,470.00 USD |
| `7D` | `11.54` | 94,830.00 USD | 94,830.00 USD | 0.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD |
| `1D` | `11.56` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 64,190.00 USD | 0.00 USD | 15,160.00 USD |
| `7D` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD |
| `1D` | `11.58` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 45,400.00 USD | 75.80 USD | 17,790.00 USD |
| `7D` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 124,870.00 USD | 289.75 USD | 67,340.00 USD |
| `7D` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.62` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 42,200.00 USD | 0.00 USD | 33,860.00 USD |
| `7D` | `11.64` | 222,010.00 USD | 222,010.00 USD | 0.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD |
| `7D` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD |
| `1D` | `11.70` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.96 USD |
| `1D` | `11.72` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD |
| `7D` | `11.72` | 484,570.00 USD | 484,570.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD |
| `1D` | `11.76` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD |
| `7D` | `11.76` | 532,760.00 USD | 532,760.00 USD | 0.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD |
| `1D` | `11.80` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 14,340.00 USD | 66.63 USD |
| `7D` | `11.80` | 672,880.00 USD | 672,880.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD |
| `7D` | `11.82` | 873,430.00 USD | 873,430.00 USD | 0.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD |
| `7D` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD |
| `1D` | `11.86` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD |
| `7D` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD |
| `1D` | `11.88` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD |
| `7D` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD |
| `1D` | `11.90` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD |
| `7D` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.92` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD |
| `7D` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD |
| `1D` | `11.94` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD |
| `7D` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD |
| `7D` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD |
| `1D` | `11.98` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD |
| `7D` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD |
| `1D` | `12.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD |
| `7D` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD |
| `1D` | `12.02` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD |
| `7D` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD |
| `1D` | `12.04` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 209,440.00 USD | 65,620.00 USD | 97,900.00 USD |
| `7D` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD |
| `1D` | `12.06` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 187,660.00 USD | 88,160.00 USD | 147,980.00 USD |
| `7D` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD |
| `1D` | `12.08` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD |
| `7D` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD |
| `1D` | `12.10` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 36,180.00 USD | 16,940.00 USD | 22,460.00 USD |
| `7D` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 138,630.00 USD | 60,020.00 USD | 63,050.00 USD |
| `7D` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD |
| `1D` | `12.14` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 92,340.00 USD | 33,200.00 USD | 55,720.00 USD |
| `7D` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD |
| `1D` | `12.16` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 126,410.00 USD | 37,730.00 USD | 67,630.00 USD |
| `7D` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD |
| `1D` | `12.18` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 112,590.00 USD | 42,150.00 USD | 33,450.00 USD |
| `7D` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD |
| `1D` | `12.20` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 77,890.00 USD | 43,590.00 USD | 31,800.00 USD |
| `7D` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD |
| `1D` | `12.22` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 12,890.00 USD | 16,530.00 USD | 28,210.00 USD |
| `7D` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD |
| `1D` | `12.24` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD |
| `1D` | `12.26` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 43,220.00 USD | 22,010.00 USD | 21,450.00 USD |
| `7D` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD |
| `1D` | `12.28` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 83,960.00 USD | 17,410.00 USD | 37,620.00 USD |
| `7D` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD |
| `1D` | `12.30` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 57,170.00 USD | 16,300.00 USD | 36,460.00 USD |
| `7D` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD |
| `1D` | `12.32` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.34` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD |
| `7D` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD |
| `1D` | `12.36` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 19,360.00 USD | 9,040.00 USD | 5,460.00 USD |
| `7D` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD |
| `1D` | `12.38` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD |
| `7D` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD |
| `1D` | `12.40` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 18,820.00 USD | 12,140.00 USD | 22,980.00 USD |
| `7D` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD |
| `1D` | `12.42` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 57,850.00 USD | 13,980.00 USD | 9,730.00 USD |
| `7D` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD |
| `1D` | `12.46` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 411.51 USD | 9,440.00 USD | 4,210.00 USD |
| `7D` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD |
| `1D` | `12.48` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD |
| `7D` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD |
| `1D` | `12.50` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD |
| `7D` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD |
| `1D` | `12.52` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD |
| `7D` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.54` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD |
| `1D` | `12.56` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD |
| `1D` | `12.58` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD |
| `7D` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD |
| `1D` | `12.60` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 15,910.00 USD | 3,320.00 USD | 1,180.00 USD |
| `7D` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.62` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 13,610.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.64` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.66` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 4,580.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.68` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD |
| `1D` | `12.70` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD |
| `7D` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD |
| `1D` | `12.72` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD |
| `7D` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD |
| `1D` | `12.74` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD |
| `7D` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD |
| `1D` | `12.76` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD |
| `1D` | `12.78` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD |
| `1D` | `12.80` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD |
| `7D` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.82` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD |
| `7D` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.84` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD |
| `1D` | `12.86` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD |
| `7D` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD |
| `1D` | `12.88` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD |
| `1D` | `12.90` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD |
| `7D` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD |
| `1D` | `12.92` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD |
| `7D` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD |
| `1D` | `12.94` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD |
| `1D` | `12.96` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD |
| `7D` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD |
| `1D` | `12.98` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD |
| `7D` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD |
| `1D` | `13.00` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 11,890.00 USD | 7,680.00 USD | 12,890.00 USD |
| `7D` | `13.00` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD |
| `7D` | `13.02` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `7D` | `13.04` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 303.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.06` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD |
| `7D` | `13.10` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 18,460.00 USD | 5,730.00 USD | 7,600.00 USD |
| `7D` | `13.12` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 945.50 USD | 4,010.00 USD | 20.43 USD |
| `7D` | `13.14` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 321.45 USD | 0.00 USD | 0.00 USD |
| `7D` | `13.16` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57.86 USD |
| `7D` | `13.18` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,370.00 USD |
| `7D` | `13.20` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 18,620.00 USD |
| `7D` | `13.22` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 23,980.00 USD | 213.60 USD | 37.80 USD |
| `7D` | `13.24` | 14,710,000.00 USD | 14,710,000.00 USD | 0.00 USD | 18,770.00 USD | 4,640.00 USD | 11,590.00 USD |
| `7D` | `13.26` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 463.75 USD | 5,860.00 USD | 10,920.00 USD |
| `7D` | `13.27` | 14,740,000.00 USD | 14,740,000.00 USD | 0.00 USD | 9,830.00 USD | 2,560.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `525.54M` | Total OI Tokens: `47,478,706.8 LINK`
  * 1h OI Change: `-3.33%` | 4h OI Change: `-7.14%` | 24h OI Change: `-8.71%`
  * Exchange Breakdown: Binance=`100.25M` | Bybit=`62.61M` | OKX=`25.58M` | Hyperliquid=`50.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.47K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0048%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0019%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0006%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0084%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `49.51%` | `50.49%` | `0.98` | 36,260,000.00 USD |
| `15M` | `Binance` | `48.12%` | `51.88%` | `0.93` | 12,780,000.00 USD |
| `15M` | `OKX` | `53.17%` | `46.83%` | `1.14` | 4,360,000.00 USD |
| `15M` | `Bybit` | `50.27%` | `49.73%` | `1.01` | 3,280,000.00 USD |
| `15M` | `KuCoin` | `47.54%` | `52.46%` | `0.91` | 273,510.00 USD |
| `15M` | `Gate` | `50.14%` | `49.86%` | `1.01` | 655,890.00 USD |
| `15M` | `Bitget` | `44.56%` | `55.44%` | `0.80` | 1,450,000.00 USD |
| `15M` | `BingX` | `60.09%` | `39.91%` | `1.51` | 949,030.00 USD |
| `15M` | `MEXC` | `49.45%` | `50.55%` | `0.98` | 6,410,000.00 USD |
| `15M` | `Bitunix` | `54.52%` | `45.48%` | `1.20` | 1,200,000.00 USD |
| `15M` | `Hyperliquid` | `49.11%` | `50.89%` | `0.97` | 3,130,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.8%` | `51.2%` | `0.95` | 972,380.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `30.42%` | `69.58%` | `0.44` | 150,540.00 USD |
| `15M` | `HTX` | `33.2%` | `66.8%` | `0.50` | 20,840.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `41.54%` | `58.46%` | `0.71` | 501,330.00 USD |
| `15M` | `Aster` | `63.13%` | `36.87%` | `1.71` | 90,720.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `22.8%` | `77.2%` | `0.30` | 41,770.00 USD |
| `15M` | `Whale Positions` | `48.12%` | `51.88%` | `0.93` | 12,780,000.00 USD |
| `15M` | `Global Accounts` | `49.51%` | `50.49%` | `0.98` | 36,260,000.00 USD |
| `1H` | `LINK` | `45.98%` | `54.02%` | `0.85` | 208,110,000.00 USD |
| `1H` | `Binance` | `45.44%` | `54.56%` | `0.83` | 71,030,000.00 USD |
| `1H` | `OKX` | `49.46%` | `50.54%` | `0.98` | 26,830,000.00 USD |
| `1H` | `Bybit` | `46.3%` | `53.7%` | `0.86` | 22,540,000.00 USD |
| `1H` | `KuCoin` | `48.69%` | `51.31%` | `0.95` | 1,840,000.00 USD |
| `1H` | `Gate` | `43.96%` | `56.04%` | `0.78` | 10,290,000.00 USD |
| `1H` | `Bitget` | `45.46%` | `54.54%` | `0.83` | 18,740,000.00 USD |
| `1H` | `BingX` | `47.52%` | `52.48%` | `0.91` | 5,090,000.00 USD |
| `1H` | `MEXC` | `49.52%` | `50.48%` | `0.98` | 10,880,000.00 USD |
| `1H` | `Bitunix` | `43.2%` | `56.8%` | `0.76` | 4,930,000.00 USD |
| `1H` | `Hyperliquid` | `35.42%` | `64.58%` | `0.55` | 3,340,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.69%` | `50.31%` | `0.99` | 30,630,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `15.45%` | `84.55%` | `0.18` | 628,220.00 USD |
| `1H` | `HTX` | `42.16%` | `57.84%` | `0.73` | 285,220.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.23%` | `46.77%` | `1.14` | 753,630.00 USD |
| `1H` | `Aster` | `27.87%` | `72.13%` | `0.39` | 202,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `40.94%` | `59.06%` | `0.69` | 67,670.00 USD |
| `1H` | `Whale Positions` | `45.44%` | `54.56%` | `0.83` | 71,030,000.00 USD |
| `1H` | `Global Accounts` | `45.98%` | `54.02%` | `0.85` | 208,110,000.00 USD |
| `4H` | `LINK` | `45.86%` | `54.14%` | `0.85` | 61,640,000.00 USD |
| `4H` | `Binance` | `45.96%` | `54.04%` | `0.85` | 24,010,000.00 USD |
| `4H` | `OKX` | `47.12%` | `52.88%` | `0.89` | 6,030,000.00 USD |
| `4H` | `Bybit` | `45.97%` | `54.03%` | `0.85` | 9,470,000.00 USD |
| `4H` | `KuCoin` | `49.71%` | `50.29%` | `0.99` | 422,270.00 USD |
| `4H` | `Gate` | `45.63%` | `54.37%` | `0.84` | 2,810,000.00 USD |
| `4H` | `Bitget` | `45.73%` | `54.27%` | `0.84` | 1,510,000.00 USD |
| `4H` | `BingX` | `44.89%` | `55.11%` | `0.81` | 2,400,000.00 USD |
| `4H` | `MEXC` | `49.46%` | `50.54%` | `0.98` | 514,840.00 USD |
| `4H` | `Bitunix` | `46.38%` | `53.62%` | `0.86` | 791,460.00 USD |
| `4H` | `Hyperliquid` | `34.15%` | `65.85%` | `0.52` | 4,960,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 3,830,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.36%` | `88.64%` | `0.13` | 3,960,000.00 USD |
| `4H` | `HTX` | `44.52%` | `55.48%` | `0.80` | 265,160.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.93%` | `55.07%` | `0.82` | 439,180.00 USD |
| `4H` | `Aster` | `23.78%` | `76.22%` | `0.31` | 55,580.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.18%` | `59.82%` | `0.67` | 145,310.00 USD |
| `4H` | `Whale Positions` | `45.96%` | `54.04%` | `0.85` | 24,010,000.00 USD |
| `4H` | `Global Accounts` | `45.86%` | `54.14%` | `0.85` | 61,640,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.68` | `11.66` | `11.68` | `11.68` | `11.63` | 997,243.09 USD | 360,139.33 USD | 637,103.76 USD | -276,964.43 USD | `-27.77%` | `11B / 15S` |
| `0:00 UTC` | `11.72` | `11.71` | `11.72` | `11.73` | `11.68` | 1,229,457.09 USD | 722,946.86 USD | 506,510.23 USD | 216,436.63 USD | `+17.60%` | `13B / 6S` |
| `5:00 UTC` | `11.70` | `11.70` | `11.70` | `11.72` | `11.68` | 638,959.31 USD | 356,011.33 USD | 282,947.98 USD | 73,063.35 USD | `+11.43%` | `5B / 5S` |
| `0:00 UTC` | `11.53` | `11.52` | `11.53` | `11.69` | `11.42` | 7,042,914.29 USD | 3,385,099.97 USD | 3,657,814.32 USD | -272,714.35 USD | `-3.87%` | `7B / 36S` |
| `5:00 UTC` | `11.53` | `11.53` | `11.53` | `11.57` | `11.50` | 1,919,098.80 USD | 908,695.92 USD | 1,010,402.88 USD | -101,706.95 USD | `-5.30%` | `5B / 9S` |
| `0:00 UTC` | `11.13` | `11.25` | `11.13` | `11.55` | `11.03` | 15,867,227.37 USD | 6,488,166.63 USD | 9,379,060.74 USD | -2,890,894.11 USD | `-18.22%` | `4B / 29S` |
| `5:00 UTC` | `11.00` | `11.03` | `11.00` | `11.19` | `10.87` | 17,839,722.17 USD | 8,415,517.99 USD | 9,424,204.18 USD | -1,008,686.19 USD | `-5.65%` | `9B / 18S` |
| `0:00 UTC` | `11.11` | `11.05` | `11.11` | `11.15` | `10.95` | 9,198,852.48 USD | 4,309,450.89 USD | 4,889,401.59 USD | -579,950.70 USD | `-6.30%` | `0B / 3S` |

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
| `5m` | -432,830.00 USD | -867,310.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,060,000.00 USD | -755,100.00 USD | **`DISTRIBUTION`** |
| `30m` | -3,300,000.00 USD | -6,620,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,680,000.00 USD | -7,430,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,710,000.00 USD | -7,610,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,600,000.00 USD | -9,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,420,000.00 USD | -9,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,730,000.00 USD | -7,830,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -3,610,000.00 USD | -7,810,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -4,110,000.00 USD | -13,290,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -12,670,000.00 USD | -31,480,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -72,800,000.00 USD | -193,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-432.83K` | 15m=`-1.06M` | 1h=`-3.68M` | 24h=`-4.11M`
* Futures Capital Netflows: 5m=`-867.31K` | 15m=`-755.10K` | 1h=`-7.43M` | 24h=`-13.29M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `10.91` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.63` (Risk Distance: `0.2834` pts)
  * +2.5R Take Profit: `11.62`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.95` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.23` (Risk Distance: `0.2834` pts)
  * +2.5R Take Profit: `10.24`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.05`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
