# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 04:47:08 IST` (`2026-10-29 23:17:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `10.63` | **Live Ask Quote**: `10.71` | **Mid Price**: `10.67`
- **Spread Points**: `84.00` | **Spread BPS**: `78.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.41` | VWAP Z-Score: `-2.44` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1337` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `20.00` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.36` | Lower -3.00σ Band: `10.46`
  * Upper +2.51σ Band: `12.20` | Lower -2.51σ Band: `10.62`
  * Upper +2.01σ Band: `12.05` | Lower -2.01σ Band: `10.78`
  * Upper +2.00σ Band: `12.04` | Lower -2.00σ Band: `10.78`
  * Upper +1.28σ Band: `11.82` | Lower -1.28σ Band: `11.01`
  * Upper +1.00σ Band: `11.73` | Lower -1.00σ Band: `11.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.88` | EMA-20=`11.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.36` (Slope: `+0.0000`) | EMA-100=`11.46`
  * Institutional Anchors: EMA-144=`11.47` | EMA-200=`11.47` (Slope: `-0.5687`) | EMA-233=`11.47`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.58` | Weekly High=`11.96` | Weekly Low=`10.58`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.20` (Distance: `-4.61%`)
  * Point of Control (POC) = `10.81` (Distance: `-1.25%`)
  * Value Area Low (VAL) = `10.80` (Distance: `-1.13%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.63` | Weekly POC=`11.42` | Weekly VAL=`11.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.58`
  * London Session (08:00-16:00 UTC): High=`10.71` | Low=`10.63`
  * New York Session (13:00-21:00 UTC): High=`10.74` | Low=`10.61`
  * Initial Balance (First Hour): IB High=`10.70` | IB Low=`10.64`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `10.63` - `10.71`
  * Optimal Trade Entry (OTE 0.705): `10.69`
  * Structural Invalidation Anchor (0.786): `10.76`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.67` | `10.68` | `10.62` | `10.67` | `262,933` | 2,800,623.31 USD | -367,169.08 USD | `-13.11%` | -17,317,805.14 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `10.67` | `10.72` | `10.65` | `10.70` | `274,813` | 2,935,214.63 USD | 218,449.49 USD | `+7.44%` | -17,099,355.65 USD | `+0.80` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `10.70` | `10.71` | `10.67` | `10.69` | `86,406` | 923,435.69 USD | -57,654.76 USD | `-6.24%` | -17,157,010.41 USD | `+0.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.82` | `10.84` | `10.71` | `10.75` | `1,006,324` | 10,836,187.71 USD | 145,199.30 USD | `+1.34%` | -16,422,597.67 USD | `+0.61` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `10.75` | `10.75` | `10.62` | `10.70` | `785,241` | 8,384,727.48 USD | -684,209.01 USD | `-8.16%` | -17,106,806.68 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.70` | `10.71` | `10.67` | `10.68` | `84,695` | 905,146.28 USD | -73,592.27 USD | `-8.13%` | -17,180,398.95 USD | `+0.48` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `10.99` | `11.29` | `10.95` | `11.05` | `1,981,647` | 22,042,313.47 USD | -1,846,592.95 USD | `-8.38%` | -7,835,044.70 USD | `-1.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.06` | `10.71` | `10.75` | `4,861,262` | 52,776,566.13 USD | -8,723,123.08 USD | `-16.53%` | -16,558,167.77 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `10.75` | `10.75` | `10.62` | `10.69` | `871,235` | 9,303,751.61 USD | -745,326.83 USD | `-8.01%` | -17,303,494.60 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.62` | `10.69` | `11,520,023` | 126,800,733.18 USD | -15,581,533.94 USD | `-12.29%` | -17,300,031.54 USD | `-2.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.62` | `10.69` | `11,520,023` | 126,800,733.18 USD | -15,581,533.94 USD | `-12.29%` | -17,300,031.54 USD | `-2.19` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`10.67`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `514` | `0x73ce...8ce9` | `LONG` | 4,266,523.73 USD | `400,011,600.00` | `12.05` | `10.65` | `9.12` | -553,229.98 USD | `-12.97%` | `5X Cross` |
| `876` | `0xb83d...6e36` | `SHORT` | 2,575,744.36 USD | `242,013,000.00` | `12.93` | `10.65` | `626.11` | 554,149.83 USD | `+21.51%` | `3X Cross` |
| `934` | `0x458d...ab3b` | `LONG` | 2,422,853.36 USD | `227,156,700.00` | `13.13` | `10.65` | `9.34` | -559,377.03 USD | `-23.09%` | `3X Isolated` |
| `1015` | `0xdd53...2b13` | `SHORT` | 2,198,755.47 USD | `206,475,300.00` | `11.92` | `10.65` | `310.88` | 262,467.46 USD | `+11.94%` | `3X Cross` |
| `1039` | `0x3dc9...54b0` | `SHORT` | 2,133,800.00 USD | `200,000,000.00` | `7.56` | `10.65` | `95.71` | -622,641.58 USD | `-29.18%` | `10X Cross` |
| `1058` | `0x45d2...4029` | `SHORT` | 2,090,872.50 USD | `195,500,000.00` | `11.54` | `10.65` | `221.81` | 165,610.93 USD | `+7.92%` | `10X Cross` |
| `1085` | `0xecb6...2b00` | `SHORT` | 2,026,136.53 USD | `190,229,700.00` | `10.71` | `10.65` | `159.19` | 12,050.37 USD | `+0.59%` | `10X Cross` |
| `1266` | `0x6540...f7b7` | `LONG` | 1,771,916.79 USD | `166,400,600.00` | `12.45` | `10.65` | `7.22` | -299,064.09 USD | `-16.88%` | `5X Isolated` |
| `1306` | `0xeadc...9d55` | `LONG` | 1,691,084.72 USD | `157,691,600.00` | `9.43` | `10.65` | `0.000000` | 204,429.82 USD | `+12.09%` | `10X Cross` |
| `1552` | `0x5b5d...c060` | `SHORT` | 1,406,044.58 USD | `131,775,500.00` | `13.61` | `10.65` | `1333.13` | 387,213.38 USD | `+27.54%` | `3X Cross` |
| `1721` | `0xf6f3...47f8` | `SHORT` | 1,226,047.21 USD | `115,024,600.00` | `11.42` | `10.65` | `20.73` | 87,282.97 USD | `+7.12%` | `5X Cross` |
| `1747` | `0x9df2...c665` | `SHORT` | 1,197,687.93 USD | `112,543,500.00` | `11.48` | `10.65` | `292.88` | 94,639.53 USD | `+7.90%` | `10X Cross` |
| `1891` | `0xfe7e...11b4` | `LONG` | 1,076,757.73 USD | `101,142,000.00` | `14.47` | `10.65` | `5.33` | -386,355.42 USD | `-35.88%` | `5X Isolated` |
| `1922` | `0x8af7...fa05` | `SHORT` | 1,050,445.80 USD | `98,661,200.00` | `14.08` | `10.65` | `205.92` | 338,736.74 USD | `+32.25%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.85` | 338.77 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.34K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.85` | 1,529.19 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 1.53K USD at 11.8450 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 106.60 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 0.11K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,468.37 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 5.47K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
| `ANNOUNCEMENT` | `INFO` | `11.84` | 5,706.44 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 5.71K USD at 11.8440 USD [API] | `2026-10-28 08:27:20` |
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
| `Live` | `Long Liquidation` | `9.45` | 52,380.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.53` | 4,530,000.00 USD | 4,530,000.00 USD | 80.78 USD | 78.20 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.53` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.55` | 4,530,000.00 USD | 4,530,000.00 USD | 6,860.00 USD | 2,320.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.55` | 6,330,000.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 17,750.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.57` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.57` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.59` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 5,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.59` | 6,330,000.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.61` | 4,510,000.00 USD | 4,510,000.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.61` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.63` | 4,510,000.00 USD | 4,510,000.00 USD | 671.70 USD | 0.00 USD | 105.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.63` | 6,320,000.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.65` | 4,510,000.00 USD | 4,510,000.00 USD | 972.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.65` | 6,300,000.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 14,450.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.67` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.67` | 6,290,000.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.69` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.69` | 6,290,000.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.71` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.73` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.75` | 4,430,000.00 USD | 4,430,000.00 USD | 40,030.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 6,220,000.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 73,310.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.77` | 4,380,000.00 USD | 4,380,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.77` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.79` | 4,240,000.00 USD | 4,240,000.00 USD | 15,980.00 USD | 146.87 USD | 49.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.79` | 6,110,000.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.81` | 4,220,000.00 USD | 4,220,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.81` | 6,060,000.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.83` | 4,120,000.00 USD | 4,120,000.00 USD | 37,110.00 USD | 0.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.83` | 5,960,000.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.85` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.85` | 5,910,000.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 207,090.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.87` | 4,070,000.00 USD | 4,070,000.00 USD | 9,950.00 USD | 288.30 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.91` | 4,050,000.00 USD | 4,050,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.91` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.93` | 4,020,000.00 USD | 4,020,000.00 USD | 13,840.00 USD | 5,580.00 USD | 124.48 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.95` | 4,000,000.00 USD | 4,000,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 5,840,000.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 505,330.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.97` | 3,980,000.00 USD | 3,980,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.99` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.01` | 3,940,000.00 USD | 3,940,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.03` | 3,940,000.00 USD | 3,940,000.00 USD | 1,230.00 USD | 115.90 USD | 310.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.05` | 3,940,000.00 USD | 3,940,000.00 USD | 10,250.00 USD | 0.00 USD | 75.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 665,050.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `10.07` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.09` | 3,930,000.00 USD | 3,930,000.00 USD | 1,180.00 USD | 0.00 USD | 145.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 5,760,000.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.11` | 3,930,000.00 USD | 3,930,000.00 USD | 7,530.00 USD | 7,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 5,760,000.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 5,750,000.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.15` | 3,910,000.00 USD | 3,910,000.00 USD | 9,270.00 USD | 104.05 USD | 99.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 5,690,000.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 12,110.00 USD | 566,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.17` | 3,900,000.00 USD | 3,900,000.00 USD | 3,600.00 USD | 0.00 USD | 490.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 5,640,000.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.19` | 3,900,000.00 USD | 3,900,000.00 USD | 3,360.00 USD | 29.65 USD | 46.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 5,540,000.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.21` | 3,900,000.00 USD | 3,900,000.00 USD | 1,700.00 USD | 3,080.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 5,490,000.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.23` | 3,880,000.00 USD | 3,880,000.00 USD | 10,890.00 USD | 18,580.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 5,380,000.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.25` | 3,810,000.00 USD | 3,810,000.00 USD | 26,800.00 USD | 1,680.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 5,080,000.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 22,430.00 USD | 553,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.27` | 3,770,000.00 USD | 3,770,000.00 USD | 18,050.00 USD | 11,470.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 4,960,000.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.29` | 3,730,000.00 USD | 3,730,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 4,780,000.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.31` | 3,700,000.00 USD | 3,700,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 4,690,000.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.33` | 3,600,000.00 USD | 3,600,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 4,490,000.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.35` | 3,520,000.00 USD | 3,520,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 4,290,000.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 21,330.00 USD | 531,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.37` | 3,450,000.00 USD | 3,450,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 4,220,000.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.39` | 3,370,000.00 USD | 3,370,000.00 USD | 7,450.00 USD | 5,390.00 USD | 44,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 4,100,000.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.41` | 3,310,000.00 USD | 3,310,000.00 USD | 259,620.00 USD | 10,880.00 USD | 39,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 4,030,000.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.43` | 3,000,000.00 USD | 3,000,000.00 USD | 172,340.00 USD | 36,070.00 USD | 71,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 3,690,000.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.45` | 2,720,000.00 USD | 2,720,000.00 USD | 130,840.00 USD | 40,980.00 USD | 54,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 3,620,000.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 48,180.00 USD | 510,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.47` | 2,500,000.00 USD | 2,500,000.00 USD | 219,660.00 USD | 45,040.00 USD | 77,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 3,320,000.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.49` | 2,150,000.00 USD | 2,150,000.00 USD | 124,820.00 USD | 26,560.00 USD | 17,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 3,010,000.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.51` | 1,990,000.00 USD | 1,990,000.00 USD | 27,700.00 USD | 6,670.00 USD | 13,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 2,820,000.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.53` | 1,940,000.00 USD | 1,940,000.00 USD | 43,880.00 USD | 39,730.00 USD | 117,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 2,730,000.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.55` | 1,740,000.00 USD | 1,740,000.00 USD | 7,160.00 USD | 2,730.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 2,660,000.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 443,270.00 USD | 461,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.57` | 1,670,000.00 USD | 1,670,000.00 USD | 52,260.00 USD | 36,690.00 USD | 114,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 2,400,000.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.59` | 1,470,000.00 USD | 1,470,000.00 USD | 48,700.00 USD | 22,350.00 USD | 172,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 2,250,000.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.61` | 1,220,000.00 USD | 1,220,000.00 USD | 231,320.00 USD | 10,040.00 USD | 103,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 2,000,000.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.63` | 878,050.00 USD | 878,050.00 USD | 464,250.00 USD | 49,920.00 USD | 117,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 1,460,000.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.65` | 246,580.00 USD | 246,580.00 USD | 165,270.00 USD | 35,430.00 USD | 45,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 1,360,000.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 18,720.00 USD | 18,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.67` | 246,980.00 USD | 246,980.00 USD | 216,030.00 USD | 3,400.00 USD | 27,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.67` | 493,960.00 USD | 493,960.00 USD | 216,030.00 USD | 3,400.00 USD | 27,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 1,290,000.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.69` | 1,060,000.00 USD | 1,060,000.00 USD | 423,380.00 USD | 3,940.00 USD | 143,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 801,310.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.71` | 1,290,000.00 USD | 1,290,000.00 USD | 219,090.00 USD | 501.67 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 323,480.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.73` | 1,300,000.00 USD | 1,300,000.00 USD | 6,180.00 USD | 0.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 29,560.00 USD | 29,560.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.73` | 59,120.00 USD | 59,120.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.75` | 1,390,000.00 USD | 1,390,000.00 USD | 89,590.00 USD | 430.90 USD | 109.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.75` | 77,290.00 USD | 77,290.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.75` | 18,760.00 USD | 18,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.77` | 1,400,000.00 USD | 1,400,000.00 USD | 5,310.00 USD | 4,090.00 USD | 44.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.77` | 98,870.00 USD | 98,870.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.79` | 1,570,000.00 USD | 1,570,000.00 USD | 88,000.00 USD | 85,640.00 USD | 20.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.79` | 192,270.00 USD | 192,270.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.81` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.87` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 21,840.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.91` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 11,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.93` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.95` | 1,790,000.00 USD | 1,790,000.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.95` | 227,860.00 USD | 227,860.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 2,530.00 USD | 21,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `10.97` | 1,860,000.00 USD | 1,860,000.00 USD | 124.21 USD | 15,600.00 USD | 54,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.97` | 240,550.00 USD | 240,550.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `10.99` | 1,860,000.00 USD | 1,860,000.00 USD | 1,470.00 USD | 0.00 USD | 99.93 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `10.99` | 413,570.00 USD | 413,570.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.01` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 106,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.01` | 424,150.00 USD | 424,150.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.03` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 145,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.03` | 576,560.00 USD | 576,560.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.05` | 2,370,000.00 USD | 2,370,000.00 USD | 192,840.00 USD | 0.00 USD | 65,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.05` | 966,150.00 USD | 966,150.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.05` | 496.15 USD | 21,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.07` | 2,910,000.00 USD | 2,910,000.00 USD | 435,240.00 USD | 18,990.00 USD | 78,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.07` | 973,650.00 USD | 973,650.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.09` | 3,140,000.00 USD | 3,140,000.00 USD | 126,930.00 USD | 44,870.00 USD | 58,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.09` | 981,150.00 USD | 981,150.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.11` | 3,390,000.00 USD | 3,390,000.00 USD | 216,430.00 USD | 19,740.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.13` | 4,020,000.00 USD | 4,020,000.00 USD | 408,510.00 USD | 91,630.00 USD | 132,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.15` | 4,230,000.00 USD | 4,230,000.00 USD | 194,240.00 USD | 11,710.00 USD | 0.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.17` | 4,360,000.00 USD | 4,360,000.00 USD | 165.70 USD | 69,930.00 USD | 59,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.19` | 4,520,000.00 USD | 4,520,000.00 USD | 72,110.00 USD | 63,920.00 USD | 27,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.21` | 4,750,000.00 USD | 4,750,000.00 USD | 114,630.00 USD | 425.43 USD | 116,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.23` | 5,050,000.00 USD | 5,050,000.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.25` | 5,340,000.00 USD | 5,340,000.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 11,850.00 USD | 33,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.27` | 5,820,000.00 USD | 5,820,000.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.29` | 6,320,000.00 USD | 6,320,000.00 USD | 165,410.00 USD | 123,030.00 USD | 213,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.31` | 6,530,000.00 USD | 6,530,000.00 USD | 63,250.00 USD | 67,150.00 USD | 79,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.33` | 6,800,000.00 USD | 6,800,000.00 USD | 198,020.00 USD | 39,030.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.35` | 7,290,000.00 USD | 7,290,000.00 USD | 300,200.00 USD | 124,090.00 USD | 66,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 5,930.00 USD | 39,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.37` | 7,540,000.00 USD | 7,540,000.00 USD | 150,920.00 USD | 78,610.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.39` | 7,590,000.00 USD | 7,590,000.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.41` | 7,860,000.00 USD | 7,860,000.00 USD | 95,030.00 USD | 34,780.00 USD | 140,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.43` | 8,030,000.00 USD | 8,030,000.00 USD | 52,230.00 USD | 26,360.00 USD | 88,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.45` | 8,140,000.00 USD | 8,140,000.00 USD | 46,070.00 USD | 69,710.00 USD | 88.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 20,310.00 USD | 59,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.47` | 8,240,000.00 USD | 8,240,000.00 USD | 48,370.00 USD | 19,590.00 USD | 23,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.49` | 8,330,000.00 USD | 8,330,000.00 USD | 33,390.00 USD | 22,330.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.51` | 8,430,000.00 USD | 8,430,000.00 USD | 41,360.00 USD | 28,330.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.53` | 8,510,000.00 USD | 8,510,000.00 USD | 32,640.00 USD | 16,860.00 USD | 29,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.55` | 8,540,000.00 USD | 8,540,000.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 71,370.00 USD | 131,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.57` | 8,660,000.00 USD | 8,660,000.00 USD | 90,090.00 USD | 0.00 USD | 23,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.59` | 8,720,000.00 USD | 8,720,000.00 USD | 15,100.00 USD | 7,660.00 USD | 39,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.61` | 8,940,000.00 USD | 8,940,000.00 USD | 153,200.00 USD | 0.00 USD | 71,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.63` | 8,960,000.00 USD | 8,960,000.00 USD | 1,510.00 USD | 0.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.65` | 8,960,000.00 USD | 8,960,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 8,500.00 USD | 139,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.69` | 9,050,000.00 USD | 9,050,000.00 USD | 59,600.00 USD | 28,810.00 USD | 491.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.71` | 9,200,000.00 USD | 9,200,000.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.73` | 9,350,000.00 USD | 9,350,000.00 USD | 98,180.00 USD | 5,210.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.75` | 9,460,000.00 USD | 9,460,000.00 USD | 21,990.00 USD | 31,660.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 1,540.00 USD | 141,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.77` | 9,520,000.00 USD | 9,520,000.00 USD | 41,180.00 USD | 18,670.00 USD | 318.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.79` | 9,570,000.00 USD | 9,570,000.00 USD | 12,080.00 USD | 755.20 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.81` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 17,960.00 USD | 17,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.83` | 9,660,000.00 USD | 9,660,000.00 USD | 11,070.00 USD | 11,510.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.85` | 9,840,000.00 USD | 9,840,000.00 USD | 76,700.00 USD | 22,590.00 USD | 82,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.87` | 9,940,000.00 USD | 9,940,000.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.89` | 10,040,000.00 USD | 10,040,000.00 USD | 44,160.00 USD | 11,410.00 USD | 44,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.91` | 10,200,000.00 USD | 10,200,000.00 USD | 102,960.00 USD | 18,340.00 USD | 31,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.93` | 10,390,000.00 USD | 10,390,000.00 USD | 135,130.00 USD | 28,540.00 USD | 28,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.95` | 10,540,000.00 USD | 10,540,000.00 USD | 85,850.00 USD | 21,080.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.97` | 10,750,000.00 USD | 10,750,000.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.99` | 10,940,000.00 USD | 10,940,000.00 USD | 123,700.00 USD | 25,870.00 USD | 46,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.01` | 11,070,000.00 USD | 11,070,000.00 USD | 60,120.00 USD | 9,410.00 USD | 52,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.03` | 11,230,000.00 USD | 11,230,000.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.05` | 11,590,000.00 USD | 11,590,000.00 USD | 211,220.00 USD | 58,720.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.05` | 7,480.00 USD | 148,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.07` | 11,850,000.00 USD | 11,850,000.00 USD | 114,130.00 USD | 53,190.00 USD | 97,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.09` | 11,900,000.00 USD | 11,900,000.00 USD | 17,390.00 USD | 18,490.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.11` | 12,090,000.00 USD | 12,090,000.00 USD | 94,540.00 USD | 34,950.00 USD | 55,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.13` | 12,260,000.00 USD | 12,260,000.00 USD | 94,650.00 USD | 33,860.00 USD | 39,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.15` | 12,480,000.00 USD | 12,480,000.00 USD | 116,080.00 USD | 42,360.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 25,210.00 USD | 173,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.17` | 12,740,000.00 USD | 12,740,000.00 USD | 122,970.00 USD | 64,130.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.19` | 12,840,000.00 USD | 12,840,000.00 USD | 64,080.00 USD | 24,200.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.21` | 12,970,000.00 USD | 12,970,000.00 USD | 52,950.00 USD | 28,750.00 USD | 50,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.23` | 13,010,000.00 USD | 13,010,000.00 USD | 14,580.00 USD | 24,000.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.25` | 13,030,000.00 USD | 13,030,000.00 USD | 2,260.00 USD | 5,380.00 USD | 7,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,010.00 USD | 174,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.27` | 13,120,000.00 USD | 13,120,000.00 USD | 52,420.00 USD | 9,790.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.29` | 13,210,000.00 USD | 13,210,000.00 USD | 38,460.00 USD | 19,780.00 USD | 34,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.31` | 13,240,000.00 USD | 13,240,000.00 USD | 19,750.00 USD | 4,850.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.33` | 13,250,000.00 USD | 13,250,000.00 USD | 1,880.00 USD | 3,680.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.35` | 13,290,000.00 USD | 13,290,000.00 USD | 19,880.00 USD | 12,610.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 117,910.00 USD | 292,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.37` | 13,310,000.00 USD | 13,310,000.00 USD | 8,820.00 USD | 5,700.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.39` | 13,370,000.00 USD | 13,370,000.00 USD | 28,580.00 USD | 12,560.00 USD | 21,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.41` | 13,460,000.00 USD | 13,460,000.00 USD | 42,540.00 USD | 19,990.00 USD | 23,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.43` | 13,480,000.00 USD | 13,480,000.00 USD | 23,090.00 USD | 5,940.00 USD | 113.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.45` | 13,510,000.00 USD | 13,510,000.00 USD | 10,690.00 USD | 4,330.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.47` | 13,530,000.00 USD | 13,530,000.00 USD | 1,620.00 USD | 12,000.00 USD | 12,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.49` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 63.95 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 6,870.00 USD | `Tier 1 CEX` |
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
| `1D` | `9.53` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 80.78 USD | 78.20 USD | 0.00 USD |
| `7D` | `9.53` | 6,340,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 2,870.00 USD | 0.00 USD |
| `1D` | `9.55` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 6,860.00 USD | 2,320.00 USD | 3,590.00 USD |
| `7D` | `9.55` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 633.47 USD | 0.00 USD | 10.22 USD |
| `1D` | `9.57` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 0.00 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `9.57` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 28.93 USD |
| `1D` | `9.59` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 0.00 USD | 5,640.00 USD | 0.00 USD |
| `7D` | `9.59` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 486.28 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `9.61` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 1,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.61` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 4,470.00 USD |
| `1D` | `9.63` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 671.70 USD | 0.00 USD | 105.10 USD |
| `7D` | `9.63` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 10,700.00 USD | 0.00 USD | 5,810.00 USD |
| `1D` | `9.65` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 972.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.65` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 5,140.00 USD | 2,770.00 USD | 5,640.00 USD |
| `1D` | `9.67` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 4,020.00 USD | 17,550.00 USD |
| `7D` | `9.67` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 115.45 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `9.69` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 10,930.00 USD |
| `7D` | `9.69` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 4,510.00 USD | 0.00 USD | 31,480.00 USD |
| `1D` | `9.71` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 15,870.00 USD |
| `7D` | `9.71` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `1D` | `9.73` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 29,230.00 USD |
| `7D` | `9.73` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `1D` | `9.75` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 40,030.00 USD | 0.00 USD | 13,120.00 USD |
| `7D` | `9.75` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 52,150.00 USD | 33.95 USD | 43,640.00 USD |
| `1D` | `9.77` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 112,940.00 USD | 7,910.00 USD | 19,810.00 USD |
| `7D` | `9.77` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.79` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 15,980.00 USD | 146.87 USD | 49.52 USD |
| `7D` | `9.79` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 44,630.00 USD | 671.70 USD | 0.00 USD |
| `1D` | `9.81` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 73,100.00 USD | 18,420.00 USD | 9,730.00 USD |
| `7D` | `9.81` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 55,730.00 USD | 22,970.00 USD | 25,050.00 USD |
| `1D` | `9.83` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 37,110.00 USD | 0.00 USD | 10,450.00 USD |
| `7D` | `9.83` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 40,450.00 USD | 1,030.00 USD | 0.00 USD |
| `1D` | `9.85` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 0.00 USD | 175.40 USD | 0.00 USD |
| `7D` | `9.85` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 26,080.00 USD | 0.00 USD | 12,970.00 USD |
| `1D` | `9.87` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 9,950.00 USD | 288.30 USD | 10,090.00 USD |
| `7D` | `9.89` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.91` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 17,040.00 USD | 12,870.00 USD | 0.00 USD |
| `7D` | `9.91` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `9.93` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 13,840.00 USD | 5,580.00 USD | 124.48 USD |
| `7D` | `9.93` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.95` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 9,450.00 USD | 6,100.00 USD | 8,550.00 USD |
| `7D` | `9.95` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 14,920.00 USD | 22,060.00 USD | 13,780.00 USD |
| `1D` | `9.97` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 3,140.00 USD | 5,500.00 USD | 7,780.00 USD |
| `7D` | `9.97` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 598.17 USD | 0.00 USD |
| `1D` | `9.99` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 0.00 USD | 6,390.00 USD | 12,110.00 USD |
| `7D` | `9.99` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 25,970.00 USD |
| `1D` | `10.01` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 1,460.00 USD | 254.10 USD | 0.00 USD |
| `7D` | `10.01` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.03` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 1,230.00 USD | 115.90 USD | 310.11 USD |
| `1D` | `10.05` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 10,250.00 USD | 0.00 USD | 75.76 USD |
| `7D` | `10.05` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `7D` | `10.07` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `1D` | `10.09` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 1,180.00 USD | 0.00 USD | 145.05 USD |
| `7D` | `10.09` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.11` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 7,530.00 USD | 7,510.00 USD | 0.00 USD |
| `7D` | `10.11` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 4,940.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `10.13` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.15` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 9,270.00 USD | 104.05 USD | 99.30 USD |
| `7D` | `10.15` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `1D` | `10.17` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 3,600.00 USD | 0.00 USD | 490.75 USD |
| `7D` | `10.17` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 65,660.00 USD | 3,240.00 USD | 22,180.00 USD |
| `1D` | `10.19` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 3,360.00 USD | 29.65 USD | 46.29 USD |
| `7D` | `10.19` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.21` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 1,700.00 USD | 3,080.00 USD | 12,530.00 USD |
| `7D` | `10.21` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.23` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 10,890.00 USD | 18,580.00 USD | 41,580.00 USD |
| `7D` | `10.23` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.25` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 26,800.00 USD | 1,680.00 USD | 11,020.00 USD |
| `7D` | `10.25` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.27` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 18,050.00 USD | 11,470.00 USD | 4,290.00 USD |
| `7D` | `10.27` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.29` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 17,890.00 USD | 6,880.00 USD | 13,790.00 USD |
| `7D` | `10.29` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 46,860.00 USD | 30,040.00 USD | 10,370.00 USD |
| `1D` | `10.31` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 24,410.00 USD | 21,490.00 USD | 54,160.00 USD |
| `7D` | `10.31` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 50,440.00 USD | 57,500.00 USD | 95,080.00 USD |
| `1D` | `10.33` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 30,780.00 USD | 9,530.00 USD | 39,380.00 USD |
| `7D` | `10.33` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 58,810.00 USD | 28,270.00 USD | 104,480.00 USD |
| `1D` | `10.35` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 12,800.00 USD | 4,310.00 USD | 48,140.00 USD |
| `7D` | `10.35` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 36,360.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.37` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 8,240.00 USD | 7,110.00 USD | 65,470.00 USD |
| `7D` | `10.37` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 12,950.00 USD | 12,460.00 USD | 96,800.00 USD |
| `1D` | `10.39` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 7,450.00 USD | 5,390.00 USD | 44,570.00 USD |
| `7D` | `10.39` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.41` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 259,620.00 USD | 10,880.00 USD | 39,350.00 USD |
| `7D` | `10.41` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 186,040.00 USD | 28,080.00 USD | 119,280.00 USD |
| `1D` | `10.43` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 172,340.00 USD | 36,070.00 USD | 71,930.00 USD |
| `7D` | `10.43` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.45` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 130,840.00 USD | 40,980.00 USD | 54,340.00 USD |
| `7D` | `10.45` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 149,660.00 USD | 48,540.00 USD | 104,790.00 USD |
| `1D` | `10.47` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 219,660.00 USD | 45,040.00 USD | 77,510.00 USD |
| `7D` | `10.47` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 239,390.00 USD | 46,830.00 USD | 26,370.00 USD |
| `1D` | `10.49` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 124,820.00 USD | 26,560.00 USD | 17,500.00 USD |
| `7D` | `10.49` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 133,330.00 USD | 1,330.00 USD | 57,350.00 USD |
| `1D` | `10.51` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 27,700.00 USD | 6,670.00 USD | 13,350.00 USD |
| `7D` | `10.51` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.53` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 43,880.00 USD | 39,730.00 USD | 117,700.00 USD |
| `7D` | `10.53` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 13,040.00 USD | 34,340.00 USD | 21,130.00 USD |
| `1D` | `10.55` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 7,160.00 USD | 2,730.00 USD | 56,270.00 USD |
| `7D` | `10.55` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 55,490.00 USD | 19,150.00 USD | 178,570.00 USD |
| `1D` | `10.57` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 52,260.00 USD | 36,690.00 USD | 114,810.00 USD |
| `7D` | `10.57` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 87,970.00 USD | 45,510.00 USD | 23,410.00 USD |
| `1D` | `10.59` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 48,700.00 USD | 22,350.00 USD | 172,400.00 USD |
| `7D` | `10.59` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 33,510.00 USD | 35,040.00 USD | 177,490.00 USD |
| `1D` | `10.61` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 231,320.00 USD | 10,040.00 USD | 103,290.00 USD |
| `7D` | `10.61` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 314,370.00 USD | 47,830.00 USD | 177,490.00 USD |
| `1D` | `10.63` | 878,050.00 USD | 0.00 USD | 878,050.00 USD | 464,250.00 USD | 49,920.00 USD | 117,290.00 USD |
| `7D` | `10.63` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 43,710.00 USD | 37,990.00 USD | 22,840.00 USD |
| `1D` | `10.65` | 246,580.00 USD | 0.00 USD | 246,580.00 USD | 165,270.00 USD | 35,430.00 USD | 45,880.00 USD |
| `7D` | `10.65` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 30,090.00 USD | 7,780.00 USD | 32,540.00 USD |
| `1D` | `10.67` | 246,980.00 USD | 246,980.00 USD | 0.00 USD | 216,030.00 USD | 3,400.00 USD | 27,550.00 USD |
| `1D` | `10.67` | 493,960.00 USD | 493,960.00 USD | 0.00 USD | 216,030.00 USD | 3,400.00 USD | 27,550.00 USD |
| `7D` | `10.67` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 244,300.00 USD | 78,350.00 USD | 162,030.00 USD |
| `1D` | `10.69` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 423,380.00 USD | 3,940.00 USD | 143,210.00 USD |
| `7D` | `10.69` | 801,310.00 USD | 0.00 USD | 801,310.00 USD | 383,680.00 USD | 49,270.00 USD | 44,880.00 USD |
| `1D` | `10.71` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 219,090.00 USD | 501.67 USD | 3,730.00 USD |
| `7D` | `10.71` | 323,480.00 USD | 0.00 USD | 323,480.00 USD | 238,550.00 USD | 12,470.00 USD | 72,450.00 USD |
| `1D` | `10.73` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 6,180.00 USD | 0.00 USD | 3,640.00 USD |
| `7D` | `10.73` | 29,560.00 USD | 29,560.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `7D` | `10.73` | 59,120.00 USD | 59,120.00 USD | 0.00 USD | 28,700.00 USD | 853.30 USD | 0.00 USD |
| `1D` | `10.75` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 89,590.00 USD | 430.90 USD | 109.24 USD |
| `7D` | `10.75` | 77,290.00 USD | 77,290.00 USD | 0.00 USD | 17,290.00 USD | 877.75 USD | 0.00 USD |
| `1D` | `10.77` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 5,310.00 USD | 4,090.00 USD | 44.48 USD |
| `7D` | `10.77` | 98,870.00 USD | 98,870.00 USD | 0.00 USD | 16,290.00 USD | 5,290.00 USD | 0.00 USD |
| `1D` | `10.79` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 88,000.00 USD | 85,640.00 USD | 20.34 USD |
| `7D` | `10.79` | 192,270.00 USD | 192,270.00 USD | 0.00 USD | 33,460.00 USD | 59,950.00 USD | 0.00 USD |
| `1D` | `10.81` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD |
| `1D` | `10.87` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 21,840.00 USD | 35,980.00 USD |
| `1D` | `10.91` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 11,350.00 USD | 0.00 USD |
| `1D` | `10.93` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 1,010.00 USD | 0.00 USD |
| `1D` | `10.95` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 1,210.00 USD | 34,250.00 USD | 87,750.00 USD |
| `7D` | `10.95` | 227,860.00 USD | 227,860.00 USD | 0.00 USD | 7,820.00 USD | 27,770.00 USD | 0.00 USD |
| `1D` | `10.97` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 124.21 USD | 15,600.00 USD | 54,540.00 USD |
| `7D` | `10.97` | 240,550.00 USD | 240,550.00 USD | 0.00 USD | 12,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.99` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,470.00 USD | 0.00 USD | 99.93 USD |
| `7D` | `10.99` | 413,570.00 USD | 413,570.00 USD | 0.00 USD | 15,610.00 USD | 0.00 USD | 157,410.00 USD |
| `1D` | `11.01` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 106,110.00 USD |
| `7D` | `11.01` | 424,150.00 USD | 424,150.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.03` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145,940.00 USD |
| `7D` | `11.03` | 576,560.00 USD | 576,560.00 USD | 0.00 USD | 9,370.00 USD | 0.00 USD | 143,040.00 USD |
| `1D` | `11.05` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 192,840.00 USD | 0.00 USD | 65,580.00 USD |
| `7D` | `11.05` | 966,150.00 USD | 966,150.00 USD | 0.00 USD | 256,930.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 435,240.00 USD | 18,990.00 USD | 78,770.00 USD |
| `7D` | `11.07` | 973,650.00 USD | 973,650.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.09` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 126,930.00 USD | 44,870.00 USD | 58,490.00 USD |
| `7D` | `11.09` | 981,150.00 USD | 981,150.00 USD | 0.00 USD | 4,140.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `11.11` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 216,430.00 USD | 19,740.00 USD | 15,640.00 USD |
| `7D` | `11.11` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 228,930.00 USD | 71,610.00 USD | 125,270.00 USD |
| `1D` | `11.13` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 408,510.00 USD | 91,630.00 USD | 132,250.00 USD |
| `7D` | `11.13` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 372,210.00 USD | 48,150.00 USD | 39,630.00 USD |
| `1D` | `11.15` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 194,240.00 USD | 11,710.00 USD | 0.04 USD |
| `7D` | `11.15` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 224,050.00 USD | 2,280.00 USD | 64,850.00 USD |
| `1D` | `11.17` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 165.70 USD | 69,930.00 USD | 59,000.00 USD |
| `7D` | `11.17` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,970.00 USD | 13,890.00 USD | 0.00 USD |
| `1D` | `11.19` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 72,110.00 USD | 63,920.00 USD | 27,330.00 USD |
| `7D` | `11.19` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 78,710.00 USD |
| `1D` | `11.21` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 114,630.00 USD | 425.43 USD | 116,470.00 USD |
| `7D` | `11.21` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 311,160.00 USD | 698.80 USD | 0.00 USD |
| `1D` | `11.23` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 193,610.00 USD | 851.54 USD | 107,710.00 USD |
| `7D` | `11.23` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 241,160.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.25` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 90,500.00 USD | 39,180.00 USD | 152,530.00 USD |
| `7D` | `11.25` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 330,300.00 USD | 0.00 USD | 129,810.00 USD |
| `1D` | `11.27` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 306,490.00 USD | 2,340.00 USD | 175,630.00 USD |
| `7D` | `11.27` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 381,320.00 USD | 0.00 USD | 257,650.00 USD |
| `1D` | `11.29` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 165,410.00 USD | 123,030.00 USD | 213,740.00 USD |
| `7D` | `11.29` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 104,970.00 USD | 57,050.00 USD | 55,980.00 USD |
| `1D` | `11.31` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 63,250.00 USD | 67,150.00 USD | 79,760.00 USD |
| `7D` | `11.31` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 28,170.00 USD | 45,840.00 USD | 236,970.00 USD |
| `1D` | `11.33` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 198,020.00 USD | 39,030.00 USD | 31,760.00 USD |
| `7D` | `11.33` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 165,980.00 USD | 44,720.00 USD | 144,500.00 USD |
| `1D` | `11.35` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 300,200.00 USD | 124,090.00 USD | 66,260.00 USD |
| `7D` | `11.35` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 182,690.00 USD | 84,360.00 USD | 19,810.00 USD |
| `1D` | `11.37` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 150,920.00 USD | 78,610.00 USD | 22,140.00 USD |
| `7D` | `11.37` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 117,040.00 USD | 72,750.00 USD | 131,810.00 USD |
| `1D` | `11.39` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 1,530.00 USD | 38,850.00 USD | 7,510.00 USD |
| `7D` | `11.39` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.41` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 95,030.00 USD | 34,780.00 USD | 140,480.00 USD |
| `7D` | `11.41` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.43` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 52,230.00 USD | 26,360.00 USD | 88,590.00 USD |
| `7D` | `11.43` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 138,950.00 USD | 52,330.00 USD | 92,240.00 USD |
| `1D` | `11.45` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 46,070.00 USD | 69,710.00 USD | 88.88 USD |
| `7D` | `11.45` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 203,890.00 USD | 68,950.00 USD | 38,200.00 USD |
| `1D` | `11.47` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 48,370.00 USD | 19,590.00 USD | 23,450.00 USD |
| `7D` | `11.47` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.49` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 33,390.00 USD | 22,330.00 USD | 34,710.00 USD |
| `7D` | `11.49` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.51` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 41,360.00 USD | 28,330.00 USD | 30,570.00 USD |
| `7D` | `11.51` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 40,840.00 USD | 28,520.00 USD | 0.00 USD |
| `1D` | `11.53` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 32,640.00 USD | 16,860.00 USD | 29,620.00 USD |
| `7D` | `11.53` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 48,860.00 USD | 5,760.00 USD | 32,690.00 USD |
| `1D` | `11.55` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 22,840.00 USD | 802.50 USD | 11,900.00 USD |
| `7D` | `11.55` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 4,660.00 USD | 0.00 USD | 31,460.00 USD |
| `1D` | `11.57` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 90,090.00 USD | 0.00 USD | 23,790.00 USD |
| `7D` | `11.57` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,830.00 USD |
| `1D` | `11.59` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 15,100.00 USD | 7,660.00 USD | 39,620.00 USD |
| `7D` | `11.59` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 325.90 USD | 22,780.00 USD |
| `1D` | `11.61` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 153,200.00 USD | 0.00 USD | 71,210.00 USD |
| `7D` | `11.61` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 44,670.00 USD | 10,190.00 USD | 0.00 USD |
| `1D` | `11.63` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 1,510.00 USD | 0.00 USD | 15,930.00 USD |
| `7D` | `11.63` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 43,680.00 USD | 0.00 USD | 201.68 USD |
| `1D` | `11.65` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.65` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 18,430.00 USD |
| `7D` | `11.67` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 15,520.00 USD | 61,970.00 USD |
| `1D` | `11.69` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 59,600.00 USD | 28,810.00 USD | 491.43 USD |
| `7D` | `11.69` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.71` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 138,560.00 USD | 13,000.00 USD | 0.00 USD |
| `7D` | `11.71` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.73` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 98,180.00 USD | 5,210.00 USD | 41,710.00 USD |
| `7D` | `11.73` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.75` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 21,990.00 USD | 31,660.00 USD | 61,350.00 USD |
| `7D` | `11.75` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.77` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 41,180.00 USD | 18,670.00 USD | 318.22 USD |
| `7D` | `11.77` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 40,430.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.79` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 12,080.00 USD | 755.20 USD | 39,930.00 USD |
| `7D` | `11.79` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 186.31 USD |
| `1D` | `11.81` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 17,960.00 USD | 17,860.00 USD |
| `7D` | `11.81` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.83` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 11,070.00 USD | 11,510.00 USD | 29,460.00 USD |
| `7D` | `11.83` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.85` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 76,700.00 USD | 22,590.00 USD | 82,310.00 USD |
| `7D` | `11.85` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 31,570.00 USD |
| `1D` | `11.87` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 19,640.00 USD | 26,360.00 USD | 53,710.00 USD |
| `7D` | `11.87` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.89` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 44,160.00 USD | 11,410.00 USD | 44,170.00 USD |
| `7D` | `11.89` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 40,020.00 USD | 15,610.00 USD | 28,680.00 USD |
| `1D` | `11.91` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 102,960.00 USD | 18,340.00 USD | 31,640.00 USD |
| `7D` | `11.91` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 134,180.00 USD | 0.00 USD | 27,070.00 USD |
| `1D` | `11.93` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 135,130.00 USD | 28,540.00 USD | 28,440.00 USD |
| `7D` | `11.93` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.95` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 85,850.00 USD | 21,080.00 USD | 41,630.00 USD |
| `7D` | `11.95` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 9,660.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.97` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 77,200.00 USD | 36,360.00 USD | 97,330.00 USD |
| `7D` | `11.97` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 403,040.00 USD | 35,810.00 USD | 223,430.00 USD |
| `1D` | `11.99` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 123,700.00 USD | 25,870.00 USD | 46,940.00 USD |
| `7D` | `11.99` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 277,130.00 USD | 40,080.00 USD | 155,190.00 USD |
| `1D` | `12.01` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 60,120.00 USD | 9,410.00 USD | 52,750.00 USD |
| `7D` | `12.01` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 204,590.00 USD | 6,390.00 USD | 247,680.00 USD |
| `1D` | `12.03` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 79,870.00 USD | 42,920.00 USD | 36,690.00 USD |
| `7D` | `12.03` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 347,250.00 USD | 140,540.00 USD | 205,570.00 USD |
| `1D` | `12.05` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 211,220.00 USD | 58,720.00 USD | 90,380.00 USD |
| `7D` | `12.05` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.07` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 114,130.00 USD | 53,190.00 USD | 97,360.00 USD |
| `7D` | `12.07` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.09` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 17,390.00 USD | 18,490.00 USD | 17,660.00 USD |
| `7D` | `12.09` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.11` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 94,540.00 USD | 34,950.00 USD | 55,280.00 USD |
| `7D` | `12.11` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 84,910.00 USD | 86,750.00 USD | 111,260.00 USD |
| `1D` | `12.13` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 94,650.00 USD | 33,860.00 USD | 39,670.00 USD |
| `7D` | `12.13` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.15` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 116,080.00 USD | 42,360.00 USD | 65,400.00 USD |
| `7D` | `12.15` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.17` | 12,740,000.00 USD | 12,740,000.00 USD | 0.00 USD | 122,970.00 USD | 64,130.00 USD | 69,670.00 USD |
| `7D` | `12.17` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 26,820.00 USD | 72,810.00 USD | 53,310.00 USD |
| `1D` | `12.19` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 64,080.00 USD | 24,200.00 USD | 12,400.00 USD |
| `7D` | `12.19` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 196,200.00 USD | 58,810.00 USD | 79,450.00 USD |
| `1D` | `12.21` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 52,950.00 USD | 28,750.00 USD | 50,890.00 USD |
| `7D` | `12.21` | 14,310,000.00 USD | 14,310,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 141,150.00 USD |
| `1D` | `12.23` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 14,580.00 USD | 24,000.00 USD | 4,580.00 USD |
| `7D` | `12.23` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.25` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 2,260.00 USD | 5,380.00 USD | 7,930.00 USD |
| `7D` | `12.25` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.27` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 52,420.00 USD | 9,790.00 USD | 22,980.00 USD |
| `7D` | `12.27` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.29` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 38,460.00 USD | 19,780.00 USD | 34,580.00 USD |
| `7D` | `12.29` | 15,580,000.00 USD | 15,580,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.31` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 19,750.00 USD | 4,850.00 USD | 9,710.00 USD |
| `7D` | `12.31` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.33` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 1,880.00 USD | 3,680.00 USD | 3,280.00 USD |
| `7D` | `12.33` | 16,080,000.00 USD | 16,080,000.00 USD | 0.00 USD | 169,320.00 USD | 89,700.00 USD | 5,470.00 USD |
| `1D` | `12.35` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 19,880.00 USD | 12,610.00 USD | 5,660.00 USD |
| `7D` | `12.35` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.37` | 13,310,000.00 USD | 13,310,000.00 USD | 0.00 USD | 8,820.00 USD | 5,700.00 USD | 3,150.00 USD |
| `7D` | `12.37` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 32,750.00 USD | 24,190.00 USD | 12,900.00 USD |
| `1D` | `12.39` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 28,580.00 USD | 12,560.00 USD | 21,510.00 USD |
| `7D` | `12.39` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 122,920.00 USD | 42,040.00 USD | 63,080.00 USD |
| `1D` | `12.41` | 13,460,000.00 USD | 13,460,000.00 USD | 0.00 USD | 42,540.00 USD | 19,990.00 USD | 23,440.00 USD |
| `7D` | `12.41` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 58,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.43` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 23,090.00 USD | 5,940.00 USD | 113.86 USD |
| `7D` | `12.43` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.45` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 10,690.00 USD | 4,330.00 USD | 6,510.00 USD |
| `7D` | `12.45` | 17,730,000.00 USD | 17,730,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.47` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 1,620.00 USD | 12,000.00 USD | 12,440.00 USD |
| `7D` | `12.47` | 17,890,000.00 USD | 17,890,000.00 USD | 0.00 USD | 45,860.00 USD | 29,080.00 USD | 75,590.00 USD |
| `1D` | `12.49` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 63.95 USD | 1,340.00 USD |
| `7D` | `12.49` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD |
| `1D` | `12.50` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,870.00 USD |
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
  * Total Open Interest: `524.20M` | Total OI Tokens: `49,292,399.4 LINK`
  * 1h OI Change: `+1.29%` | 4h OI Change: `-5.51%` | 24h OI Change: `-8.44%`
  * Exchange Breakdown: Binance=`100.94M` | Bybit=`62.23M` | OKX=`25.84M` | Hyperliquid=`52.90M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `700.37` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0029%` | **USDT OKX** | `0.0081%` |
| **USDT Bybit** | `0.0015%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0028%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0063%` | **USDT Bitget** | `0.0100%` |
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
| `4H` | `LINK` | `49.24%` | `50.76%` | `0.97` | 578,050,000.00 USD |
| `4H` | `Binance` | `49.82%` | `50.18%` | `0.99` | 239,900,000.00 USD |
| `4H` | `OKX` | `51.51%` | `48.49%` | `1.06` | 66,020,000.00 USD |
| `4H` | `Bybit` | `49.77%` | `50.23%` | `0.99` | 116,890,000.00 USD |
| `4H` | `KuCoin` | `54.92%` | `45.08%` | `1.22` | 3,000,000.00 USD |
| `4H` | `Gate` | `46.55%` | `53.45%` | `0.87` | 22,370,000.00 USD |
| `4H` | `Bitget` | `53.61%` | `46.39%` | `1.16` | 17,050,000.00 USD |
| `4H` | `BingX` | `38.6%` | `61.4%` | `0.63` | 8,340,000.00 USD |
| `4H` | `MEXC` | `44.51%` | `55.49%` | `0.80` | 7,900,000.00 USD |
| `4H` | `Bitunix` | `54.41%` | `45.59%` | `1.19` | 9,040,000.00 USD |
| `4H` | `Hyperliquid` | `52.57%` | `47.43%` | `1.11` | 30,800,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.25%` | `47.75%` | `1.09` | 13,250,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `32.53%` | `67.47%` | `0.48` | 32,400,000.00 USD |
| `4H` | `HTX` | `53.93%` | `46.07%` | `1.17` | 1,940,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.89%` | `36.11%` | `1.77` | 3,550,000.00 USD |
| `4H` | `Aster` | `64.75%` | `35.25%` | `1.84` | 2,790,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.43%` | `52.57%` | `0.90` | 2,790,000.00 USD |
| `4H` | `Whale Positions` | `49.82%` | `50.18%` | `0.99` | 239,900,000.00 USD |
| `4H` | `Global Accounts` | `49.24%` | `50.76%` | `0.97` | 578,050,000.00 USD |


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
| `0:00 UTC` | `10.68` | `10.68` | `10.68` | `10.75` | `10.62` | 7,089,962.43 USD | 3,107,520.31 USD | 3,982,442.12 USD | -874,921.80 USD | `-12.34%` | `4B / 16S` |

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
| `5m` | -229,880.00 USD | -749,120.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,050,000.00 USD | -285,640.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,490,000.00 USD | -6,510,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,050,000.00 USD | -10,240,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,280,000.00 USD | -13,410,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,950,000.00 USD | -21,020,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,550,000.00 USD | -22,270,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -8,420,000.00 USD | -21,280,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,710,000.00 USD | -21,740,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,970,000.00 USD | -25,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,780,000.00 USD | -44,250,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,380,000.00 USD | -204,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-229.88K` | 15m=`-1.05M` | 1h=`-2.05M` | 24h=`-7.97M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `10.51` (Risk Distance: `0.2864` pts)
  * +2.5R Take Profit: `11.52`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.48` (Risk Distance: `0.2864` pts)
  * +2.5R Take Profit: `10.48`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`10.76`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
