# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 11:17:13 IST` (`2026-10-30 05:47:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.08` | **Live Ask Quote**: `11.17` | **Mid Price**: `11.12`
- **Spread Points**: `85.00` | **Spread BPS**: `76.41 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `10.61` | VWAP Z-Score: `+1.92` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1022` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `64.66` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.30` | Lower -3.00σ Band: `9.92`
  * Upper +2.51σ Band: `11.19` | Lower -2.51σ Band: `10.03`
  * Upper +2.01σ Band: `11.07` | Lower -2.01σ Band: `10.14`
  * Upper +2.00σ Band: `11.07` | Lower -2.00σ Band: `10.15`
  * Upper +1.28σ Band: `10.90` | Lower -1.28σ Band: `10.31`
  * Upper +1.00σ Band: `10.84` | Lower -1.00σ Band: `10.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`10.93` | EMA-20=`10.84` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`10.96` (Slope: `+0.0000`) | EMA-100=`11.16`
  * Institutional Anchors: EMA-144=`11.24` | EMA-200=`11.30` (Slope: `-0.4783`) | EMA-233=`11.33`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.20` | Weekly High=`11.96` | Weekly Low=`10.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `10.92` (Distance: `+1.88%`)
  * Point of Control (POC) = `10.48` (Distance: `+6.12%`)
  * Value Area Low (VAL) = `10.35` (Distance: `+7.47%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.73` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.09` | Low=`10.98`
  * New York Session (13:00-21:00 UTC): High=`11.19` | Low=`11.06`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.08` - `11.17`
  * Optimal Trade Entry (OTE 0.705): `11.15`
  * Structural Invalidation Anchor (0.786): `11.21`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.12` | `11.15` | `11.11` | `11.12` | `57,157` | 635,917.51 USD | 33,430.43 USD | `+5.26%` | -11,288,251.07 USD | `+0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.12` | `11.13` | `11.10` | `11.10` | `36,591` | 406,767.26 USD | -81,831.15 USD | `-20.12%` | -11,370,082.23 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.10` | `11.15` | `11.09` | `11.15` | `34,495` | 383,356.92 USD | 37,998.23 USD | `+9.91%` | -11,332,084.00 USD | `-0.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `11.05` | `11.16` | `11.05` | `11.12` | `184,689` | 2,051,224.58 USD | 35,234.71 USD | `+1.72%` | -11,335,573.66 USD | `-0.10` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `11.12` | `11.15` | `11.11` | `11.12` | `114,358` | 1,272,358.25 USD | 13,892.16 USD | `+1.09%` | -11,321,681.51 USD | `-0.34` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `11.12` | `11.15` | `11.09` | `11.15` | `127,060` | 1,412,866.69 USD | -19,818.33 USD | `-1.40%` | -11,341,499.84 USD | `-0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `10.72` | `10.98` | `10.71` | `10.96` | `806,147` | 8,746,362.36 USD | 866,493.31 USD | `+9.91%` | -11,617,870.44 USD | `+0.68` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `10.96` | `11.09` | `10.90` | `11.05` | `1,032,622` | 11,357,751.81 USD | 314,374.20 USD | `+2.77%` | -11,303,496.23 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `11.05` | `11.16` | `11.05` | `11.14` | `426,275` | 4,738,329.10 USD | 27,428.96 USD | `+0.58%` | -11,276,067.27 USD | `+0.29` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.14` | `1,458,898` | 16,096,080.91 USD | 341,803.16 USD | `+2.12%` | -11,887,024.90 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | 1,625,285.45 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 595,900.27 USD | `-1.27` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -13,921,338.71 USD | `-1.72` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,228,828.07 USD | `+0.68` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.16` | `10.90` | `11.14` | `1,458,898` | 16,096,080.91 USD | 341,803.16 USD | `+2.12%` | -11,887,024.90 USD | `+0.41` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`11.12`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `421` | `0xecb6...2b00` | `SHORT` | 5,283,100.35 USD | `474,757,400.00` | `10.66` | `11.13` | `72.07` | -222,826.28 USD | `-4.22%` | `10X Cross` |
| `506` | `0x73ce...8ce9` | `LONG` | 4,450,529.06 USD | `400,011,600.00` | `12.05` | `11.13` | `7.82` | -369,224.64 USD | `-8.30%` | `5X Cross` |
| `843` | `0xb83d...6e36` | `SHORT` | 2,692,636.64 USD | `242,013,000.00` | `12.93` | `11.13` | `529.26` | 437,257.55 USD | `+16.24%` | `3X Cross` |
| `890` | `0x458d...ab3b` | `LONG` | 2,529,389.85 USD | `227,156,700.00` | `13.13` | `11.13` | `9.34` | -452,840.54 USD | `-17.90%` | `3X Isolated` |
| `973` | `0xdd53...2b13` | `SHORT` | 2,297,037.71 USD | `206,475,300.00` | `11.92` | `11.13` | `295.25` | 164,185.21 USD | `+7.15%` | `3X Cross` |
| `997` | `0x3dc9...54b0` | `SHORT` | 2,226,800.00 USD | `200,000,000.00` | `7.56` | `11.13` | `91.48` | -715,641.58 USD | `-32.14%` | `10X Cross` |
| `1009` | `0x45d2...4029` | `SHORT` | 2,175,561.15 USD | `195,500,000.00` | `11.54` | `11.13` | `212.49` | 80,922.28 USD | `+3.72%` | `10X Cross` |
| `1181` | `0x6540...f7b7` | `LONG` | 1,875,857.53 USD | `168,586,100.00` | `12.40` | `11.13` | `6.69` | -215,161.77 USD | `-11.47%` | `5X Isolated` |
| `1257` | `0xeadc...9d55` | `LONG` | 1,756,211.35 USD | `157,691,600.00` | `9.43` | `11.13` | `0.000000` | 269,556.45 USD | `+15.35%` | `10X Cross` |
| `1481` | `0x5b5d...c060` | `SHORT` | 1,467,583.74 USD | `131,775,500.00` | `13.61` | `11.13` | `1167.53` | 325,674.23 USD | `+22.19%` | `3X Cross` |
| `1651` | `0xf6f3...47f8` | `SHORT` | 1,280,415.89 USD | `115,024,600.00` | `11.42` | `11.13` | `19.04` | 32,914.30 USD | `+2.57%` | `5X Cross` |
| `1821` | `0x9df2...c665` | `SHORT` | 1,136,550.94 USD | `102,152,700.00` | `11.48` | `11.13` | `302.60` | 36,264.94 USD | `+3.19%` | `10X Cross` |
| `1834` | `0xfe7e...11b4` | `LONG` | 1,125,204.75 USD | `101,142,000.00` | `14.47` | `11.13` | `5.32` | -337,908.40 USD | `-30.03%` | `5X Isolated` |
| `1872` | `0x8af7...fa05` | `SHORT` | 1,097,605.85 USD | `98,661,200.00` | `14.08` | `11.13` | `202.48` | 291,576.69 USD | `+26.56%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.29` | 5,507.42 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.51K USD at 11.2880 USD [API] | `2026-10-29 02:37:09` |
| `ANNOUNCEMENT` | `INFO` | `11.29` | 5,463.88 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.2890 USD [API] | `2026-10-29 02:37:09` |
| `ANNOUNCEMENT` | `INFO` | `11.37` | 5,443.96 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.44K USD at 11.3700 USD [API] | `2026-10-29 03:13:53` |
| `ANNOUNCEMENT` | `INFO` | `11.34` | 5,385.66 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.39K USD at 11.3430 USD [API] | `2026-10-29 03:41:10` |
| `ANNOUNCEMENT` | `INFO` | `11.34` | 7,509.07 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.3430 USD [API] | `2026-10-29 03:41:10` |
| `ANNOUNCEMENT` | `INFO` | `11.38` | 6,666.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.67K USD at 11.3800 USD [API] | `2026-10-29 03:43:32` |
| `ANNOUNCEMENT` | `INFO` | `18.50` | 3,700.00 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 3.70K USD at 18.5000 USD [API] | `2025-10-10 21:13:14` |
| `ANNOUNCEMENT` | `INFO` | `11.37` | 6,213.75 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.21K USD at 11.3680 USD [API] | `2026-10-29 04:01:21` |
| `ANNOUNCEMENT` | `INFO` | `11.36` | 8,887.56 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.89K USD at 11.3550 USD [API] | `2026-10-29 04:05:44` |
| `ANNOUNCEMENT` | `INFO` | `11.36` | 9,026.09 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 9.03K USD at 11.3550 USD [API] | `2026-10-29 04:05:44` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+0.97%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.31%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+0.96%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.32%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+0.96%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.32%`)
  * 7D Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+0.97%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--7.31%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 3,400.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,110.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 272.85 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,550.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 166.93 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.95` | 236.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,060.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 11,700.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,720.00 USD | 12,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 2,650.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 46,090.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 5,340.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,490.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 51,580.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 4,190.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 2,200.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 236,150.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 246.87 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 1,320.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 90,930.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 1,550.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,840.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 138.97 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 43,340.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 38,100.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 639.98 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 1,700.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,620.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 14,100.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 12,010.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 74,330.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 19,810.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 15,600.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 12,460.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 48,080.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 109,290.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 675,380.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 32,650.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 4,450.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 18,570.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 8,530.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 172,030.00 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 6,640.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 12,640.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 67,910.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 64,760.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 38,290.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 53,580.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 12,500.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 24,380.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 361,440.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 26,130.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 67,660.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 451,940.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 86,680.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.10` | 15,020,000.00 USD | 15,020,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.12` | 14,930,000.00 USD | 14,930,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.14` | 14,880,000.00 USD | 14,880,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,340.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.16` | 14,830,000.00 USD | 14,830,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.18` | 14,770,000.00 USD | 14,770,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.20` | 14,720,000.00 USD | 14,720,000.00 USD | 14,540.00 USD | 8,360.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.22` | 14,690,000.00 USD | 14,690,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.24` | 14,680,000.00 USD | 14,680,000.00 USD | 717.27 USD | 8,580.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.25` | 17,830.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.26` | 14,640,000.00 USD | 14,640,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.28` | 14,600,000.00 USD | 14,600,000.00 USD | 460.95 USD | 5,490.00 USD | 11,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.30` | 14,590,000.00 USD | 14,590,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.32` | 14,530,000.00 USD | 14,530,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 14,500,000.00 USD | 14,500,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 14,450,000.00 USD | 14,450,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 14,450,000.00 USD | 14,450,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 14,420,000.00 USD | 14,420,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 14,380,000.00 USD | 14,380,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 14,340,000.00 USD | 14,340,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 47,390.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 14,280,000.00 USD | 14,280,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 14,180,000.00 USD | 14,180,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 14,180,000.00 USD | 14,180,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 14,120,000.00 USD | 14,120,000.00 USD | 472.74 USD | 15,010.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 53,950.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 14,100,000.00 USD | 14,100,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 14,010,000.00 USD | 14,010,000.00 USD | 38,760.00 USD | 722.15 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 13,970,000.00 USD | 13,970,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 13,760,000.00 USD | 13,760,000.00 USD | 5,420.00 USD | 0.00 USD | 219.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 13,750,000.00 USD | 13,750,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 201,620.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 13,730,000.00 USD | 13,730,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 13,720,000.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 13,690,000.00 USD | 13,690,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 13,650,000.00 USD | 13,650,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 64,130.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 13,650,000.00 USD | 13,650,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.78` | 9,740,000.00 USD | 9,740,000.00 USD | 113,700.00 USD | 7,910.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.80` | 9,580,000.00 USD | 9,580,000.00 USD | 44,560.00 USD | 5,670.00 USD | 465.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 13,570,000.00 USD | 13,570,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.82` | 9,530,000.00 USD | 9,530,000.00 USD | 85,490.00 USD | 14,930.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 13,480,000.00 USD | 13,480,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.84` | 9,400,000.00 USD | 9,400,000.00 USD | 17,970.00 USD | 7,030.00 USD | 294.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 13,390,000.00 USD | 13,390,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 37,190.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 9,370,000.00 USD | 9,370,000.00 USD | 23,360.00 USD | 3,910.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.86` | 13,320,000.00 USD | 13,320,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 9,340,000.00 USD | 9,340,000.00 USD | 2,240.00 USD | 8,620.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 13,300,000.00 USD | 13,300,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 9,320,000.00 USD | 9,320,000.00 USD | 37,440.00 USD | 27,290.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 13,280,000.00 USD | 13,280,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 9,250,000.00 USD | 9,250,000.00 USD | 14,940.00 USD | 17,480.00 USD | 227.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 13,230,000.00 USD | 13,230,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 9,220,000.00 USD | 9,220,000.00 USD | 1,820.00 USD | 792.40 USD | 160.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 13,210,000.00 USD | 13,210,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 444,140.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 9,220,000.00 USD | 9,220,000.00 USD | 62,740.00 USD | 14,110.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.96` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 11,410.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 9,120,000.00 USD | 9,120,000.00 USD | 17,530.00 USD | 6,740.00 USD | 58,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 13,110,000.00 USD | 13,110,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 9,040,000.00 USD | 9,040,000.00 USD | 1,940.00 USD | 396.47 USD | 51,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,990,000.00 USD | 8,990,000.00 USD | 5,440.00 USD | 13,120.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 13,030,000.00 USD | 13,030,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,950,000.00 USD | 8,950,000.00 USD | 18,000.00 USD | 305.90 USD | 149.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 13,020,000.00 USD | 13,020,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 787,200.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,930,000.00 USD | 8,930,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.06` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 8,850,000.00 USD | 8,850,000.00 USD | 167,250.00 USD | 701.42 USD | 75,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 12,930,000.00 USD | 12,930,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 8,610,000.00 USD | 8,610,000.00 USD | 7,570.00 USD | 42,810.00 USD | 100.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 12,600,000.00 USD | 12,600,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 8,560,000.00 USD | 8,560,000.00 USD | 1,150.00 USD | 20,910.00 USD | 213.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 12,590,000.00 USD | 12,590,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 8,540,000.00 USD | 8,540,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 12,530,000.00 USD | 12,530,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 67,470.00 USD | 249,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 8,470,000.00 USD | 8,470,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.16` | 12,210,000.00 USD | 12,210,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 8,360,000.00 USD | 8,360,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 12,160,000.00 USD | 12,160,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 8,080,000.00 USD | 8,080,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 12,030,000.00 USD | 12,030,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 7,600,000.00 USD | 7,600,000.00 USD | 37,870.00 USD | 22,340.00 USD | 344,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 11,510,000.00 USD | 11,510,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 7,200,000.00 USD | 7,200,000.00 USD | 122,230.00 USD | 71,270.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 10,970,000.00 USD | 10,970,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 43,100.00 USD | 182,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,980,000.00 USD | 6,980,000.00 USD | 66,420.00 USD | 8,070.00 USD | 100,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 10,520,000.00 USD | 10,520,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 6,810,000.00 USD | 6,810,000.00 USD | 172,700.00 USD | 12,030.00 USD | 176,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 10,140,000.00 USD | 10,140,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 6,450,000.00 USD | 6,450,000.00 USD | 169,020.00 USD | 20,970.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 9,800,000.00 USD | 9,800,000.00 USD | 457,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 6,210,000.00 USD | 6,210,000.00 USD | 24,180.00 USD | 1,380.00 USD | 81,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 9,340,000.00 USD | 9,340,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 6,100,000.00 USD | 6,100,000.00 USD | 67,530.00 USD | 9,100.00 USD | 93,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 9,200,000.00 USD | 9,200,000.00 USD | 56,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 139,080.00 USD | 139,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,930,000.00 USD | 5,930,000.00 USD | 5,630.00 USD | 3,580.00 USD | 344.35 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 9,150,000.00 USD | 9,150,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,920,000.00 USD | 5,920,000.00 USD | 40,040.00 USD | 46,620.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 8,750,000.00 USD | 8,750,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,830,000.00 USD | 5,830,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 8,740,000.00 USD | 8,740,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 5,640,000.00 USD | 5,640,000.00 USD | 246,920.00 USD | 0.00 USD | 42.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 8,390,000.00 USD | 8,390,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 5,390,000.00 USD | 5,390,000.00 USD | 199,600.00 USD | 27,590.00 USD | 305,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 8,060,000.00 USD | 8,060,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 152.57 USD | 152.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,860,000.00 USD | 4,860,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 7,270,000.00 USD | 7,270,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 4,530,000.00 USD | 4,530,000.00 USD | 50,100.00 USD | 2,200.00 USD | 55,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 6,850,000.00 USD | 6,850,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 4,430,000.00 USD | 4,430,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 6,630,000.00 USD | 6,630,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 4,350,000.00 USD | 4,350,000.00 USD | 71.67 USD | 10,910.00 USD | 38,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 57,000.00 USD | 131,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.56` | 4,110,000.00 USD | 4,110,000.00 USD | 94,750.00 USD | 23,930.00 USD | 12,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 6,500,000.00 USD | 6,500,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,980,000.00 USD | 3,980,000.00 USD | 28,610.00 USD | 20,070.00 USD | 20,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 4,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 458.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 4,840.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 6,300,000.00 USD | 6,300,000.00 USD | 59,050.00 USD | 0.00 USD | 180.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 3,780,000.00 USD | 3,780,000.00 USD | 42,010.00 USD | 660.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 6,250,000.00 USD | 6,250,000.00 USD | 11,150.00 USD | 0.00 USD | 150.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 3,720,000.00 USD | 3,720,000.00 USD | 29,760.00 USD | 3,610.00 USD | 32.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 6,230,000.00 USD | 6,230,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 9,970.00 USD | 36,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 3,640,000.00 USD | 3,640,000.00 USD | 12,670.00 USD | 7,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 3,620,000.00 USD | 3,620,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 6,210,000.00 USD | 6,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 3,400,000.00 USD | 3,400,000.00 USD | 83,030.00 USD | 23,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 3,300,000.00 USD | 3,300,000.00 USD | 6,560.00 USD | 47,140.00 USD | 25,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 5,600,000.00 USD | 5,600,000.00 USD | 16,310.00 USD | 109,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 3,220,000.00 USD | 3,220,000.00 USD | 190,290.00 USD | 134,860.00 USD | 25,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 5,470,000.00 USD | 5,470,000.00 USD | 535,020.00 USD | 32,650.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 2,870,000.00 USD | 2,870,000.00 USD | 13,650.00 USD | 3,750.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 4,800,000.00 USD | 4,800,000.00 USD | 23,450.00 USD | 70,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 2,840,000.00 USD | 2,840,000.00 USD | 88,080.00 USD | 2,860.00 USD | 181.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 56,610.00 USD | 206,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 2,750,000.00 USD | 2,750,000.00 USD | 308,110.00 USD | 5,310.00 USD | 133.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 4,450,000.00 USD | 4,450,000.00 USD | 295,700.00 USD | 80,420.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.86` | 2,430,000.00 USD | 2,430,000.00 USD | 67,500.00 USD | 17,680.00 USD | 148,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 3,870,000.00 USD | 3,870,000.00 USD | 323,850.00 USD | 3,610.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 1,700.00 USD | 12.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 3,210,000.00 USD | 3,210,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 2,200,000.00 USD | 2,200,000.00 USD | 37,360.00 USD | 3,660.00 USD | 0.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 220,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 2,160,000.00 USD | 2,160,000.00 USD | 80,530.00 USD | 0.00 USD | 45.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 2,490,000.00 USD | 2,490,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 2,080,000.00 USD | 2,080,000.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 2,160,000.00 USD | 2,160,000.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.96` | 2,070,000.00 USD | 2,070,000.00 USD | 1,090.00 USD | 784.50 USD | 87,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 2,150,000.00 USD | 2,150,000.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 117.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 2,090,000.00 USD | 2,090,000.00 USD | 17,930.00 USD | 0.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 2,520.00 USD | 653.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 1,870,000.00 USD | 1,870,000.00 USD | 10,830.00 USD | 2,280.00 USD | 634.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 1,980,000.00 USD | 1,980,000.00 USD | 5,330.00 USD | 27,810.00 USD | 151,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 1,850,000.00 USD | 1,850,000.00 USD | 7,900.00 USD | 31,180.00 USD | 143,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 1,790,000.00 USD | 1,790,000.00 USD | 163,320.00 USD | 18,120.00 USD | 179,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 1,670,000.00 USD | 1,670,000.00 USD | 17,850.00 USD | 40,210.00 USD | 178,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.06` | 1,430,000.00 USD | 1,430,000.00 USD | 518,210.00 USD | 30,510.00 USD | 106,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 1,430,000.00 USD | 1,430,000.00 USD | 4,020.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.08` | 778,080.00 USD | 778,080.00 USD | 3,780.00 USD | 68,940.00 USD | 446,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 1,300,000.00 USD | 1,300,000.00 USD | 14,890.00 USD | 1,810.00 USD | 167,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 259,150.00 USD | 259,150.00 USD | 215,070.00 USD | 44,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 1,110,000.00 USD | 1,110,000.00 USD | 301,790.00 USD | 23,300.00 USD | 173,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 737,370.00 USD | 737,370.00 USD | 448,790.00 USD | 109,110.00 USD | 179,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 1,470,000.00 USD | 1,470,000.00 USD | 448,790.00 USD | 109,110.00 USD | 179,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 612,850.00 USD | 612,850.00 USD | 262,770.00 USD | 115,910.00 USD | 234,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 1,790,000.00 USD | 1,790,000.00 USD | 230,290.00 USD | 19,930.00 USD | 68,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 215,120.00 USD | 215,120.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 430,230.00 USD | 430,230.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.16` | 2,050,000.00 USD | 2,050,000.00 USD | 127,020.00 USD | 79,690.00 USD | 50,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.16` | 699,610.00 USD | 699,610.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 2,250,000.00 USD | 2,250,000.00 USD | 71,610.00 USD | 44,050.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 717,100.00 USD | 717,100.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 2,470,000.00 USD | 2,470,000.00 USD | 65,400.00 USD | 61,120.00 USD | 87,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 1,050,000.00 USD | 1,050,000.00 USD | 171,840.00 USD | 78,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 2,980,000.00 USD | 2,980,000.00 USD | 352,600.00 USD | 47,850.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 1,560,000.00 USD | 1,560,000.00 USD | 482,460.00 USD | 28,690.00 USD | 603.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 3,330,000.00 USD | 3,330,000.00 USD | 110,930.00 USD | 34,630.00 USD | 196,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 1,870,000.00 USD | 1,870,000.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 1,530.00 USD | 4,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.26` | 3,580,000.00 USD | 3,580,000.00 USD | 130,470.00 USD | 13,530.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.26` | 2,690,000.00 USD | 2,690,000.00 USD | 520,990.00 USD | 0.00 USD | 296,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 4,170,000.00 USD | 4,170,000.00 USD | 293,730.00 USD | 59,090.00 USD | 243,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 3,240,000.00 USD | 3,240,000.00 USD | 347,470.00 USD | 57,050.00 USD | 147,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 4,470,000.00 USD | 4,470,000.00 USD | 126,090.00 USD | 74,380.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 3,320,000.00 USD | 3,320,000.00 USD | 24,980.00 USD | 32,240.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 4,740,000.00 USD | 4,740,000.00 USD | 119,640.00 USD | 66,550.00 USD | 82,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 3,820,000.00 USD | 3,820,000.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 5,200,000.00 USD | 5,200,000.00 USD | 313,240.00 USD | 87,030.00 USD | 58,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 4,130,000.00 USD | 4,130,000.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 1,460.00 USD | 5,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.36` | 5,450,000.00 USD | 5,450,000.00 USD | 115,970.00 USD | 76,000.00 USD | 56,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.36` | 4,380,000.00 USD | 4,380,000.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 5,680,000.00 USD | 5,680,000.00 USD | 118,230.00 USD | 85,980.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 4,620,000.00 USD | 4,620,000.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 5,850,000.00 USD | 5,850,000.00 USD | 39,080.00 USD | 32,990.00 USD | 104,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 6,130,000.00 USD | 6,130,000.00 USD | 112,540.00 USD | 68,020.00 USD | 92,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 4,890,000.00 USD | 4,890,000.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 6,340,000.00 USD | 6,340,000.00 USD | 84,630.00 USD | 40,410.00 USD | 84,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 5,320,000.00 USD | 5,320,000.00 USD | 303,190.00 USD | 95,260.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 19.46 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 6,510,000.00 USD | 6,510,000.00 USD | 59,980.00 USD | 65,340.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 99,360.00 USD | 55,470.00 USD | 269.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 6,540,000.00 USD | 6,540,000.00 USD | 14,620.00 USD | 15,390.00 USD | 262.76 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 5,680,000.00 USD | 5,680,000.00 USD | 54,660.00 USD | 84,840.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,650,000.00 USD | 6,650,000.00 USD | 31,090.00 USD | 34,670.00 USD | 45,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 5,810,000.00 USD | 5,810,000.00 USD | 91,790.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,750,000.00 USD | 6,750,000.00 USD | 59,780.00 USD | 13,890.00 USD | 19,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 5,760.00 USD | 33,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,890,000.00 USD | 6,890,000.00 USD | 60,850.00 USD | 16,360.00 USD | 71,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 6,010,000.00 USD | 6,010,000.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 143.22 USD | 6,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 7,010,000.00 USD | 7,010,000.00 USD | 90,400.00 USD | 4,930.00 USD | 23,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 6,100,000.00 USD | 6,100,000.00 USD | 86,650.00 USD | 793.25 USD | 432.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 7,080,000.00 USD | 7,080,000.00 USD | 46,550.00 USD | 335.85 USD | 17,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 7,240,000.00 USD | 7,240,000.00 USD | 91,240.00 USD | 7,320.00 USD | 67,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 6,210,000.00 USD | 6,210,000.00 USD | 44,670.00 USD | 10,510.00 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 7,340,000.00 USD | 7,340,000.00 USD | 44,130.00 USD | 512.95 USD | 48,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 6,270,000.00 USD | 6,270,000.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 7,380,000.00 USD | 7,380,000.00 USD | 4,510.00 USD | 7,410.00 USD | 31,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 6,320,000.00 USD | 6,320,000.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 16,970.00 USD | 23,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,420,000.00 USD | 7,420,000.00 USD | 228.94 USD | 12,290.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,610,000.00 USD | 7,610,000.00 USD | 124,510.00 USD | 35,770.00 USD | 31,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 4,760.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 6,550,000.00 USD | 6,550,000.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,900,000.00 USD | 7,900,000.00 USD | 158,470.00 USD | 18,090.00 USD | 98,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 6,880,000.00 USD | 6,880,000.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 8,080,000.00 USD | 8,080,000.00 USD | 75,970.00 USD | 30,440.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 8,150,000.00 USD | 8,150,000.00 USD | 26,090.00 USD | 15,090.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 7,070,000.00 USD | 7,070,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 8,240,000.00 USD | 8,240,000.00 USD | 27,290.00 USD | 20,660.00 USD | 40,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 7,130,000.00 USD | 7,130,000.00 USD | 8,130.00 USD | 0.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 8,260,000.00 USD | 8,260,000.00 USD | 1,190.00 USD | 18,160.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 7,270,000.00 USD | 7,270,000.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 8,310,000.00 USD | 8,310,000.00 USD | 11,070.00 USD | 53.10 USD | 36,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 7,500,000.00 USD | 7,500,000.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 8,450,000.00 USD | 8,450,000.00 USD | 71,130.00 USD | 11,870.00 USD | 60,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 7,750,000.00 USD | 7,750,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,530,000.00 USD | 8,530,000.00 USD | 10,930.00 USD | 14,080.00 USD | 51,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,630,000.00 USD | 8,630,000.00 USD | 19,750.00 USD | 29,160.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 7,820,000.00 USD | 7,820,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,710,000.00 USD | 8,710,000.00 USD | 43,700.00 USD | 8,750.00 USD | 27,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 7,870,000.00 USD | 7,870,000.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,990,000.00 USD | 8,990,000.00 USD | 230,070.00 USD | 23,110.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 8,080,000.00 USD | 8,080,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 9,100,000.00 USD | 9,100,000.00 USD | 48,250.00 USD | 15,310.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 8,270,000.00 USD | 8,270,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 23,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 9,250,000.00 USD | 9,250,000.00 USD | 64,140.00 USD | 40,240.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 8,450,000.00 USD | 8,450,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 9,440,000.00 USD | 9,440,000.00 USD | 78,260.00 USD | 29,060.00 USD | 81,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 9,110,000.00 USD | 9,110,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,630,000.00 USD | 9,630,000.00 USD | 120,680.00 USD | 24,060.00 USD | 44,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 9,740,000.00 USD | 9,740,000.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,680,000.00 USD | 9,680,000.00 USD | 14,380.00 USD | 11,370.00 USD | 31,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 10,310,000.00 USD | 10,310,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,870,000.00 USD | 9,870,000.00 USD | 90,910.00 USD | 39,490.00 USD | 56,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 10,940,000.00 USD | 10,940,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 10,060,000.00 USD | 10,060,000.00 USD | 76,810.00 USD | 43,200.00 USD | 69,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 11,440,000.00 USD | 11,440,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 10,180,000.00 USD | 10,180,000.00 USD | 38,930.00 USD | 35,220.00 USD | 48,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 12,110,000.00 USD | 12,110,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 10,280,000.00 USD | 10,280,000.00 USD | 48,930.00 USD | 20,220.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 12,290,000.00 USD | 12,290,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 10,490,000.00 USD | 10,490,000.00 USD | 108,350.00 USD | 51,990.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 12,670,000.00 USD | 12,670,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,660,000.00 USD | 10,660,000.00 USD | 75,950.00 USD | 33,190.00 USD | 55,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 13,030,000.00 USD | 13,030,000.00 USD | 147,420.00 USD | 92,520.00 USD | 119,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,880,000.00 USD | 10,880,000.00 USD | 124,570.00 USD | 34,710.00 USD | 67,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 13,440,000.00 USD | 13,440,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 11,080,000.00 USD | 11,080,000.00 USD | 107,720.00 USD | 46,930.00 USD | 41,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 13,580,000.00 USD | 13,580,000.00 USD | 57,680.00 USD | 54,220.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 11,210,000.00 USD | 11,210,000.00 USD | 58,110.00 USD | 43,780.00 USD | 32,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 13,920,000.00 USD | 13,920,000.00 USD | 194,760.00 USD | 51,940.00 USD | 91,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 11,260,000.00 USD | 11,260,000.00 USD | 7,320.00 USD | 16,900.00 USD | 23,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 14,340,000.00 USD | 14,340,000.00 USD | 261,490.00 USD | 56,190.00 USD | 106,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 11,280,000.00 USD | 11,280,000.00 USD | 2,470.00 USD | 8,790.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 14,580,000.00 USD | 14,580,000.00 USD | 70,650.00 USD | 54,230.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 11,310,000.00 USD | 11,310,000.00 USD | 12,640.00 USD | 8,360.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 14,880,000.00 USD | 14,880,000.00 USD | 192,800.00 USD | 55,780.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 11,380,000.00 USD | 11,380,000.00 USD | 49,470.00 USD | 7,490.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 15,300,000.00 USD | 15,300,000.00 USD | 215,790.00 USD | 52,850.00 USD | 148,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 11,410,000.00 USD | 11,410,000.00 USD | 5,730.00 USD | 4,160.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 15,640,000.00 USD | 15,640,000.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 15,710,000.00 USD | 15,710,000.00 USD | 22,620.00 USD | 25,760.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 15,790,000.00 USD | 15,790,000.00 USD | 48,630.00 USD | 18,250.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 25,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 15,870,000.00 USD | 15,870,000.00 USD | 36,210.00 USD | 24,190.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 15,940,000.00 USD | 15,940,000.00 USD | 7,170.00 USD | 6,880.00 USD | 55,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 16,100,000.00 USD | 16,100,000.00 USD | 111,350.00 USD | 41,100.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 16,160,000.00 USD | 16,160,000.00 USD | 23,200.00 USD | 21,440.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 16,280,000.00 USD | 16,280,000.00 USD | 81,360.00 USD | 284.67 USD | 45,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 16,430,000.00 USD | 16,430,000.00 USD | 39,540.00 USD | 25,610.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 16,550,000.00 USD | 16,550,000.00 USD | 31,320.00 USD | 18,070.00 USD | 63,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 16,790,000.00 USD | 16,790,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 17,100,000.00 USD | 17,100,000.00 USD | 163,610.00 USD | 33,380.00 USD | 113,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 17,360,000.00 USD | 17,360,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,310.00 USD | 26,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.56` | 17,480,000.00 USD | 17,480,000.00 USD | 77,880.00 USD | 20,220.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 17,600,000.00 USD | 17,600,000.00 USD | 41,760.00 USD | 34,570.00 USD | 41,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 17,750,000.00 USD | 17,750,000.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 17,820,000.00 USD | 17,820,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 17,950,000.00 USD | 17,950,000.00 USD | 63,450.00 USD | 42,320.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 27,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.66` | 17,990,000.00 USD | 17,990,000.00 USD | 22,530.00 USD | 5,030.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 18,050,000.00 USD | 18,050,000.00 USD | 9,270.00 USD | 18,330.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 18,110,000.00 USD | 18,110,000.00 USD | 2,010.00 USD | 617.78 USD | 52,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 18,220,000.00 USD | 18,220,000.00 USD | 47,740.00 USD | 22,750.00 USD | 40,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 18,330,000.00 USD | 18,330,000.00 USD | 38,570.00 USD | 26,370.00 USD | 40,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 18,380,000.00 USD | 18,380,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 18,560,000.00 USD | 18,560,000.00 USD | 109,130.00 USD | 16,110.00 USD | 52,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 18,650,000.00 USD | 18,650,000.00 USD | 13,700.00 USD | 14,000.00 USD | 61,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 18,670,000.00 USD | 18,670,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 18,720,000.00 USD | 18,720,000.00 USD | 31,320.00 USD | 15,990.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 535.85 USD | 27,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.86` | 18,790,000.00 USD | 18,790,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 18,830,000.00 USD | 18,830,000.00 USD | 23,610.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 18,910,000.00 USD | 18,910,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 19,000,000.00 USD | 19,000,000.00 USD | 50,620.00 USD | 13,030.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 19,030,000.00 USD | 19,030,000.00 USD | 27,900.00 USD | 1,070.00 USD | 69.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 19,080,000.00 USD | 19,080,000.00 USD | 13,150.00 USD | 11,970.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 19,120,000.00 USD | 19,120,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 19,200,000.00 USD | 19,200,000.00 USD | 51,470.00 USD | 9,560.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 19,210,000.00 USD | 19,210,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 19,210,000.00 USD | 19,210,000.00 USD | 303.50 USD | 335.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.06` | 19,240,000.00 USD | 19,240,000.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.08` | 19,280,000.00 USD | 19,280,000.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 33,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 126,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.15` | 349.51 USD | 126,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 3,520.00 USD | 130,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 29,770.00 USD | 159,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.25` | 155.55 USD | 159,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 160,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 160,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 160,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 162,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.45` | 17,400.00 USD | 179,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 14,430.00 USD | 194,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 296,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 375,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 377,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.25` | 26,650.00 USD | 403,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,450.00 USD | 409,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 367.71 USD | 409,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,080.00 USD | 660,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 662,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.15` | 27,640.00 USD | 690,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.35` | 728.50 USD | 691,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 694,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 695,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 73,030.00 USD | 768,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 713,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.15` | 2,200,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 316.71 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.85` | 289.81 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.05` | 637.59 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 63,080.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.85` | 117.99 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.05` | 1,120.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,040,000.00 USD | 0.00 USD | 3,400.00 USD | `-79.65%` | `1,513,300.00` |
| `Live` | `Long` | `2.45` | 12,040,000.00 USD | 0.00 USD | 1,110.00 USD | `-77.84%` | `452,300.00` |
| `Live` | `Long` | `2.55` | 12,040,000.00 USD | 0.00 USD | 272.85 USD | `-76.94%` | `107,000.00` |
| `Live` | `Long` | `2.65` | 12,040,000.00 USD | 0.00 USD | 2,550.00 USD | `-76.04%` | `961,300.00` |
| `Live` | `Long` | `2.75` | 12,040,000.00 USD | 0.00 USD | 166.93 USD | `-75.13%` | `60,700.00` |
| `Live` | `Long` | `2.95` | 12,030,000.00 USD | 0.00 USD | 236.00 USD | `-73.32%` | `80,000.00` |
| `Live` | `Long` | `3.05` | 12,030,000.00 USD | 0.00 USD | 7,060.00 USD | `-72.42%` | `2,314,200.00` |
| `Live` | `Long` | `3.15` | 12,030,000.00 USD | 0.00 USD | 11,700.00 USD | `-71.51%` | `3,713,900.00` |
| `Live` | `Long` | `3.35` | 12,020,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.71%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,010,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.80%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,010,000.00 USD | 0.00 USD | 126.73 USD | `-67.90%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,010,000.00 USD | 0.00 USD | 2,720.00 USD | `-66.99%` | `744,400.00` |
| `Live` | `Long` | `3.75` | 12,000,000.00 USD | 0.00 USD | 2,650.00 USD | `-66.09%` | `707,000.00` |
| `Live` | `Long` | `3.95` | 12,000,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.28%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,000,000.00 USD | 0.00 USD | 46,090.00 USD | `-63.37%` | `11,379,400.00` |
| `Live` | `Long` | `4.15` | 11,950,000.00 USD | 0.00 USD | 5,340.00 USD | `-62.47%` | `1,287,000.00` |
| `Live` | `Long` | `4.25` | 11,940,000.00 USD | 0.00 USD | 5,490.00 USD | `-61.57%` | `1,292,800.00` |
| `Live` | `Long` | `4.45` | 11,940,000.00 USD | 0.00 USD | 51,580.00 USD | `-59.76%` | `11,590,800.00` |
| `Live` | `Long` | `4.55` | 11,890,000.00 USD | 0.00 USD | 4,190.00 USD | `-58.85%` | `919,800.00` |
| `Live` | `Long` | `4.65` | 11,880,000.00 USD | 0.00 USD | 2,200.00 USD | `-57.95%` | `473,800.00` |
| `Live` | `Long` | `4.75` | 11,880,000.00 USD | 0.00 USD | 236,150.00 USD | `-57.04%` | `49,716,700.00` |
| `Live` | `Long` | `4.85` | 11,650,000.00 USD | 0.00 USD | 246.87 USD | `-56.14%` | `50,900.00` |
| `Live` | `Long` | `4.95` | 11,640,000.00 USD | 0.00 USD | 1,320.00 USD | `-55.24%` | `266,200.00` |
| `Live` | `Long` | `5.05` | 11,640,000.00 USD | 0.00 USD | 90,930.00 USD | `-54.33%` | `18,006,100.00` |
| `Live` | `Long` | `5.15` | 11,550,000.00 USD | 0.00 USD | 1,550.00 USD | `-53.43%` | `301,800.00` |
| `Live` | `Long` | `5.25` | 11,550,000.00 USD | 0.00 USD | 5,840.00 USD | `-52.52%` | `1,111,800.00` |
| `Live` | `Long` | `5.35` | 11,550,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.62%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,000,000.00 USD | 0.00 USD | 138.97 USD | `-50.71%` | `25,500.00` |
| `Live` | `Long` | `5.55` | 11,000,000.00 USD | 0.00 USD | 43,340.00 USD | `-49.81%` | `7,808,700.00` |
| `Live` | `Long` | `5.65` | 10,960,000.00 USD | 0.00 USD | 38,100.00 USD | `-48.91%` | `6,743,300.00` |
| `Live` | `Long` | `5.75` | 10,920,000.00 USD | 0.00 USD | 639.98 USD | `-48.00%` | `111,300.00` |
| `Live` | `Long` | `5.85` | 10,920,000.00 USD | 0.00 USD | 1,700.00 USD | `-47.10%` | `290,500.00` |
| `Live` | `Long` | `5.95` | 10,920,000.00 USD | 0.00 USD | 10,620.00 USD | `-46.19%` | `1,784,100.00` |
| `Live` | `Long` | `6.05` | 10,910,000.00 USD | 0.00 USD | 14,100.00 USD | `-45.29%` | `2,331,000.00` |
| `Live` | `Long` | `6.15` | 10,890,000.00 USD | 0.00 USD | 12,010.00 USD | `-44.38%` | `1,952,800.00` |
| `Live` | `Long` | `6.25` | 10,880,000.00 USD | 0.00 USD | 74,330.00 USD | `-43.48%` | `11,892,600.00` |
| `Live` | `Long` | `6.35` | 10,810,000.00 USD | 0.00 USD | 19,810.00 USD | `-42.58%` | `3,120,000.00` |
| `Live` | `Long` | `6.45` | 10,790,000.00 USD | 0.00 USD | 15,600.00 USD | `-41.67%` | `2,418,300.00` |
| `Live` | `Long` | `6.55` | 10,770,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.77%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 10,770,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.86%` | `170,234,200.00` |
| `Live` | `Long` | `6.75` | 9,640,000.00 USD | 0.00 USD | 12,460.00 USD | `-38.96%` | `1,846,500.00` |
| `Live` | `Long` | `6.85` | 9,630,000.00 USD | 0.00 USD | 48,080.00 USD | `-38.05%` | `7,018,900.00` |
| `Live` | `Long` | `6.95` | 9,580,000.00 USD | 0.00 USD | 109,290.00 USD | `-37.15%` | `15,724,500.00` |
| `Live` | `Long` | `7.05` | 9,470,000.00 USD | 0.00 USD | 675,380.00 USD | `-36.25%` | `95,799,200.00` |
| `Live` | `Long` | `7.15` | 8,790,000.00 USD | 0.00 USD | 32,650.00 USD | `-35.34%` | `4,565,800.00` |
| `Live` | `Long` | `7.25` | 8,760,000.00 USD | 0.00 USD | 4,450.00 USD | `-34.44%` | `613,700.00` |
| `Live` | `Long` | `7.35` | 8,760,000.00 USD | 0.00 USD | 18,570.00 USD | `-33.53%` | `2,526,400.00` |
| `Live` | `Long` | `7.45` | 8,740,000.00 USD | 0.00 USD | 8,530.00 USD | `-32.63%` | `1,145,600.00` |
| `Live` | `Long` | `7.55` | 8,730,000.00 USD | 0.00 USD | 172,030.00 USD | `-31.72%` | `22,784,800.00` |
| `Live` | `Long` | `7.65` | 8,560,000.00 USD | 0.00 USD | 6,640.00 USD | `-30.82%` | `868,100.00` |
| `Live` | `Long` | `7.75` | 8,550,000.00 USD | 0.00 USD | 12,640.00 USD | `-29.91%` | `1,630,600.00` |
| `Live` | `Long` | `7.85` | 8,540,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-29.01%` | `401,109,100.00` |
| `Live` | `Long` | `7.95` | 5,390,000.00 USD | 0.00 USD | 67,910.00 USD | `-28.11%` | `8,542,600.00` |
| `Live` | `Long` | `8.05` | 5,320,000.00 USD | 0.00 USD | 64,760.00 USD | `-27.20%` | `8,044,600.00` |
| `Live` | `Long` | `8.15` | 5,260,000.00 USD | 0.00 USD | 38,290.00 USD | `-26.30%` | `4,697,800.00` |
| `Live` | `Long` | `8.25` | 5,220,000.00 USD | 0.00 USD | 53,580.00 USD | `-25.39%` | `6,494,000.00` |
| `Live` | `Long` | `8.35` | 5,160,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.49%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,160,000.00 USD | 0.00 USD | 12,500.00 USD | `-23.58%` | `1,478,800.00` |
| `Live` | `Long` | `8.55` | 5,150,000.00 USD | 0.00 USD | 24,380.00 USD | `-22.68%` | `2,851,500.00` |
| `Live` | `Long` | `8.65` | 5,120,000.00 USD | 0.00 USD | 361,440.00 USD | `-21.78%` | `41,785,400.00` |
| `Live` | `Long` | `8.75` | 4,760,000.00 USD | 0.00 USD | 26,130.00 USD | `-20.87%` | `2,986,200.00` |
| `Live` | `Long` | `8.85` | 4,730,000.00 USD | 0.00 USD | 67,660.00 USD | `-19.97%` | `7,644,700.00` |
| `Live` | `Long` | `8.95` | 4,670,000.00 USD | 0.00 USD | 451,940.00 USD | `-19.06%` | `50,496,300.00` |
| `Live` | `Long` | `9.05` | 4,210,000.00 USD | 0.00 USD | 86,680.00 USD | `-18.16%` | `9,577,800.00` |
| `Live` | `Long` | `9.15` | 4,130,000.00 USD | 0.00 USD | 76,340.00 USD | `-17.25%` | `8,343,000.00` |
| `Live` | `Long` | `9.25` | 4,050,000.00 USD | 0.00 USD | 17,830.00 USD | `-16.35%` | `1,928,000.00` |
| `Live` | `Long` | `9.35` | 4,030,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.45%` | `229,680,600.00` |
| `Live` | `Long` | `9.45` | 1,890,000.00 USD | 0.00 USD | 47,390.00 USD | `-14.54%` | `5,015,000.00` |
| `Live` | `Long` | `9.55` | 1,840,000.00 USD | 0.00 USD | 53,950.00 USD | `-13.64%` | `5,648,900.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 201,620.00 USD | `-12.73%` | `20,893,400.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 64,130.00 USD | `-11.83%` | `6,577,800.00` |
| `Live` | `Long` | `9.85` | 1,520,000.00 USD | 0.00 USD | 37,190.00 USD | `-10.92%` | `3,775,800.00` |
| `Live` | `Long` | `9.95` | 1,480,000.00 USD | 0.00 USD | 444,140.00 USD | `-10.02%` | `44,637,000.00` |
| `Live` | `Long` | `10.05` | 1,040,000.00 USD | 0.00 USD | 787,200.00 USD | `-9.12%` | `78,328,800.00` |
| `Live` | `Long` | `10.15` | 249,810.00 USD | 0.00 USD | 67,470.00 USD | `-8.21%` | `6,647,400.00` |
| `Live` | `Long` | `10.25` | 182,340.00 USD | 0.00 USD | 43,100.00 USD | `-7.31%` | `4,205,100.00` |
| `Live` | `Long` | `10.35` | 139,230.00 USD | 0.00 USD | 139,080.00 USD | `-6.40%` | `13,437,900.00` |
| `Live` | `Long` | `10.45` | 152.57 USD | 0.00 USD | 152.57 USD | `-5.50%` | `14,600.00` |
| `Live` | `Short` | `11.15` | 2,970.00 USD | 2,970.00 USD | 0.00 USD | `+0.83%` | `266,300.00` |
| `Live` | `Short` | `11.25` | 4,500.00 USD | 1,530.00 USD | 0.00 USD | `+1.74%` | `135,800.00` |
| `Live` | `Short` | `11.35` | 5,960.00 USD | 1,460.00 USD | 0.00 USD | `+2.64%` | `129,000.00` |
| `Live` | `Short` | `11.45` | 5,980.00 USD | 19.46 USD | 0.00 USD | `+3.54%` | `1,700.00` |
| `Live` | `Short` | `11.55` | 6,120.00 USD | 143.22 USD | 0.00 USD | `+4.45%` | `12,400.00` |
| `Live` | `Short` | `11.65` | 23,100.00 USD | 16,970.00 USD | 0.00 USD | `+5.35%` | `1,456,900.00` |
| `Live` | `Short` | `11.95` | 23,380.00 USD | 283.21 USD | 0.00 USD | `+8.07%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 24,810.00 USD | 1,430.00 USD | 0.00 USD | `+10.78%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 25,550.00 USD | 736.06 USD | 0.00 USD | `+11.68%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 26,860.00 USD | 1,310.00 USD | 0.00 USD | `+13.49%` | `104,500.00` |
| `Live` | `Short` | `12.65` | 27,290.00 USD | 435.16 USD | 0.00 USD | `+14.40%` | `34,400.00` |
| `Live` | `Short` | `12.85` | 27,830.00 USD | 535.85 USD | 0.00 USD | `+16.21%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 33,260.00 USD | 5,430.00 USD | 0.00 USD | `+21.63%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 126,150.00 USD | 92,890.00 USD | 0.00 USD | `+22.54%` | `6,855,700.00` |
| `Live` | `Short` | `14.15` | 126,500.00 USD | 349.51 USD | 0.00 USD | `+27.96%` | `24,700.00` |
| `Live` | `Short` | `14.25` | 130,020.00 USD | 3,520.00 USD | 0.00 USD | `+28.87%` | `246,800.00` |
| `Live` | `Short` | `14.95` | 159,790.00 USD | 29,770.00 USD | 0.00 USD | `+35.20%` | `1,991,000.00` |
| `Live` | `Short` | `15.25` | 159,940.00 USD | 155.55 USD | 0.00 USD | `+37.91%` | `10,200.00` |
| `Live` | `Short` | `15.55` | 160,520.00 USD | 578.46 USD | 0.00 USD | `+40.62%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 160,790.00 USD | 271.04 USD | 0.00 USD | `+43.34%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 160,930.00 USD | 138.76 USD | 0.00 USD | `+44.24%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 162,320.00 USD | 1,390.00 USD | 0.00 USD | `+47.86%` | `85,300.00` |
| `Live` | `Short` | `16.45` | 179,730.00 USD | 17,400.00 USD | 0.00 USD | `+48.76%` | `1,058,000.00` |
| `Live` | `Short` | `16.55` | 194,150.00 USD | 14,430.00 USD | 0.00 USD | `+49.67%` | `871,700.00` |
| `Live` | `Short` | `16.75` | 296,060.00 USD | 101,910.00 USD | 0.00 USD | `+51.47%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 375,830.00 USD | 79,770.00 USD | 0.00 USD | `+53.28%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 377,200.00 USD | 1,370.00 USD | 0.00 USD | `+55.09%` | `79,700.00` |
| `Live` | `Short` | `17.25` | 403,850.00 USD | 26,650.00 USD | 0.00 USD | `+56.00%` | `1,544,800.00` |
| `Live` | `Short` | `17.65` | 409,300.00 USD | 5,450.00 USD | 0.00 USD | `+59.61%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 409,670.00 USD | 367.71 USD | 0.00 USD | `+61.42%` | `20,600.00` |
| `Live` | `Short` | `17.95` | 660,750.00 USD | 251,080.00 USD | 0.00 USD | `+62.33%` | `13,987,600.00` |
| `Live` | `Short` | `18.05` | 662,720.00 USD | 1,970.00 USD | 0.00 USD | `+63.23%` | `109,300.00` |
| `Live` | `Short` | `18.15` | 690,360.00 USD | 27,640.00 USD | 0.00 USD | `+64.13%` | `1,523,000.00` |
| `Live` | `Short` | `18.35` | 691,090.00 USD | 728.50 USD | 0.00 USD | `+65.94%` | `39,700.00` |
| `Live` | `Short` | `18.45` | 694,980.00 USD | 3,890.00 USD | 0.00 USD | `+66.85%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 695,170.00 USD | 185.50 USD | 0.00 USD | `+67.75%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 695,350.00 USD | 186.50 USD | 0.00 USD | `+68.66%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 768,380.00 USD | 73,030.00 USD | 0.00 USD | `+69.56%` | `3,895,000.00` |
| `Live` | `Short` | `18.85` | 1,480,000.00 USD | 713,280.00 USD | 0.00 USD | `+70.46%` | `37,839,800.00` |
| `Live` | `Short` | `19.15` | 3,680,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+73.18%` | `115,024,600.00` |
| `Live` | `Short` | `19.55` | 3,680,000.00 USD | 316.71 USD | 0.00 USD | `+76.80%` | `16,200.00` |
| `Live` | `Short` | `19.65` | 3,720,000.00 USD | 38,790.00 USD | 0.00 USD | `+77.70%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,720,000.00 USD | 359.45 USD | 0.00 USD | `+78.60%` | `18,200.00` |
| `Live` | `Short` | `19.85` | 3,720,000.00 USD | 289.81 USD | 0.00 USD | `+79.51%` | `14,600.00` |
| `Live` | `Short` | `20.05` | 3,720,000.00 USD | 637.59 USD | 0.00 USD | `+81.32%` | `31,800.00` |
| `Live` | `Short` | `20.15` | 3,730,000.00 USD | 1,260.00 USD | 0.00 USD | `+82.22%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,730,000.00 USD | 1,770.00 USD | 0.00 USD | `+84.93%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,740,000.00 USD | 7,250.00 USD | 0.00 USD | `+85.84%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,740,000.00 USD | 114.68 USD | 0.00 USD | `+88.55%` | `5,500.00` |
| `Live` | `Short` | `21.75` | 3,800,000.00 USD | 63,080.00 USD | 0.00 USD | `+96.69%` | `2,900,400.00` |
| `Live` | `Short` | `21.85` | 3,800,000.00 USD | 117.99 USD | 0.00 USD | `+97.59%` | `5,400.00` |
| `Live` | `Short` | `22.05` | 3,800,000.00 USD | 1,120.00 USD | 0.00 USD | `+99.40%` | `50,600.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 549,930.00 USD | 0.00 USD | 182.03 USD | `-77.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 549,750.00 USD | 0.00 USD | 234.23 USD | `-73.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 549,520.00 USD | 0.00 USD | 209.48 USD | `-71.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 549,310.00 USD | 0.00 USD | 680.89 USD | `-67.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 548,630.00 USD | 0.00 USD | 290.29 USD | `-58.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 548,340.00 USD | 0.00 USD | 120.22 USD | `-52.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 548,220.00 USD | 0.00 USD | 251.68 USD | `-45.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 547,960.00 USD | 0.00 USD | 749.30 USD | `-42.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 547,210.00 USD | 0.00 USD | 772.71 USD | `-41.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 546,440.00 USD | 0.00 USD | 3,760.00 USD | `-40.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 542,680.00 USD | 0.00 USD | 133.00 USD | `-39.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 542,540.00 USD | 0.00 USD | 1,320.00 USD | `-37.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 541,230.00 USD | 0.00 USD | 3,770.00 USD | `-36.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 537,460.00 USD | 0.00 USD | 2,070.00 USD | `-34.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 535,390.00 USD | 0.00 USD | 3,740.00 USD | `-32.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 531,650.00 USD | 0.00 USD | 1,050.00 USD | `-31.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 530,590.00 USD | 0.00 USD | 120.90 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 530,470.00 USD | 0.00 USD | 146.80 USD | `-29.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 530,330.00 USD | 0.00 USD | 124.02 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 530,200.00 USD | 0.00 USD | 5,000.00 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 525,200.00 USD | 0.00 USD | 520.78 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 524,680.00 USD | 0.00 USD | 10,560.00 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 514,110.00 USD | 0.00 USD | 60,230.00 USD | `-24.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 453,890.00 USD | 0.00 USD | 1,480.00 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 452,410.00 USD | 0.00 USD | 52,990.00 USD | `-22.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 399,420.00 USD | 0.00 USD | 186.84 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 399,240.00 USD | 0.00 USD | 742.88 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 398,490.00 USD | 0.00 USD | 902.70 USD | `-19.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 397,590.00 USD | 0.00 USD | 1,570.00 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 396,020.00 USD | 0.00 USD | 4,460.00 USD | `-18.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 391,570.00 USD | 0.00 USD | 194.90 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 391,370.00 USD | 0.00 USD | 232.18 USD | `-16.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 391,140.00 USD | 0.00 USD | 7,060.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 384,080.00 USD | 0.00 USD | 518.80 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 383,560.00 USD | 0.00 USD | 19,460.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 364,100.00 USD | 0.00 USD | 686.12 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 363,420.00 USD | 0.00 USD | 2,370.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 361,040.00 USD | 0.00 USD | 24,850.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 336,190.00 USD | 0.00 USD | 13,710.00 USD | `-10.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 322,480.00 USD | 0.00 USD | 42,800.00 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 279,680.00 USD | 0.00 USD | 51,460.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 228,230.00 USD | 0.00 USD | 107,370.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 120,860.00 USD | 0.00 USD | 731.75 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 120,130.00 USD | 0.00 USD | 2,220.00 USD | `-5.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 117,900.00 USD | 0.00 USD | 12,710.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 105,190.00 USD | 0.00 USD | 19,870.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 85,320.00 USD | 0.00 USD | 1,760.00 USD | `-2.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 83,560.00 USD | 0.00 USD | 5,430.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 78,140.00 USD | 0.00 USD | 188.34 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 77,950.00 USD | 0.00 USD | 77,950.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 24,230.00 USD | 24,230.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 38,780.00 USD | 14,550.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 60,420.00 USD | 21,640.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 60,820.00 USD | 396.17 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 98,890.00 USD | 38,070.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 101,670.00 USD | 2,790.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 103,120.00 USD | 1,440.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 103,230.00 USD | 110.21 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 107,050.00 USD | 3,820.00 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 135,020.00 USD | 27,980.00 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 136,850.00 USD | 1,820.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 230,240.00 USD | 93,390.00 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 230,840.00 USD | 597.74 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 235,730.00 USD | 4,890.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 292,510.00 USD | 56,780.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 298,690.00 USD | 6,180.00 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 299,370.00 USD | 679.57 USD | 0.00 USD | `+15.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 319,730.00 USD | 20,360.00 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 320,180.00 USD | 451.95 USD | 0.00 USD | `+17.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 336,810.00 USD | 16,630.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 337,730.00 USD | 919.19 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 339,050.00 USD | 1,320.00 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 346,830.00 USD | 7,790.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 349,370.00 USD | 2,540.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 349,540.00 USD | 165.31 USD | 0.00 USD | `+22.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 350,490.00 USD | 954.14 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 370,040.00 USD | 19,550.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 374,920.00 USD | 4,880.00 USD | 0.00 USD | `+25.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 375,190.00 USD | 266.44 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 391,450.00 USD | 16,260.00 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 391,600.00 USD | 152.82 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 395,880.00 USD | 4,280.00 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 399,290.00 USD | 3,410.00 USD | 0.00 USD | `+29.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 418,730.00 USD | 19,440.00 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 418,950.00 USD | 218.25 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 421,470.00 USD | 2,520.00 USD | 0.00 USD | `+32.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 428,740.00 USD | 7,270.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 429,690.00 USD | 950.82 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 454,540.00 USD | 24,860.00 USD | 0.00 USD | `+36.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 456,990.00 USD | 2,450.00 USD | 0.00 USD | `+37.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 690,030.00 USD | 233,040.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 690,960.00 USD | 924.07 USD | 0.00 USD | `+38.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 691,850.00 USD | 893.01 USD | 0.00 USD | `+39.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 692,500.00 USD | 653.10 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 692,970.00 USD | 472.63 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 696,270.00 USD | 3,290.00 USD | 0.00 USD | `+42.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 699,440.00 USD | 3,170.00 USD | 0.00 USD | `+43.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 704,570.00 USD | 5,130.00 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 719,650.00 USD | 15,080.00 USD | 0.00 USD | `+45.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 726,450.00 USD | 6,800.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 732,950.00 USD | 6,500.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 739,490.00 USD | 6,540.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 746,070.00 USD | 6,580.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 756,000.00 USD | 9,930.00 USD | 0.00 USD | `+49.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 859,980.00 USD | 103,980.00 USD | 0.00 USD | `+50.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 874,220.00 USD | 14,240.00 USD | 0.00 USD | `+51.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 958,580.00 USD | 84,360.00 USD | 0.00 USD | `+52.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 960,270.00 USD | 1,700.00 USD | 0.00 USD | `+53.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 967,640.00 USD | 7,370.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 984,330.00 USD | 16,690.00 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 986,630.00 USD | 2,300.00 USD | 0.00 USD | `+56.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 988,360.00 USD | 1,740.00 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,010,000.00 USD | 21,690.00 USD | 0.00 USD | `+57.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,010,000.00 USD | 4,390.00 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,020,000.00 USD | 4,410.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,020,000.00 USD | 4,440.00 USD | 0.00 USD | `+60.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,030,000.00 USD | 4,460.00 USD | 0.00 USD | `+61.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,030,000.00 USD | 448.75 USD | 0.00 USD | `+62.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,060,000.00 USD | 30,960.00 USD | 0.00 USD | `+63.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,060,000.00 USD | 453.75 USD | 0.00 USD | `+64.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,060,000.00 USD | 456.25 USD | 0.00 USD | `+65.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,060,000.00 USD | 458.75 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,060,000.00 USD | 461.25 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,070,000.00 USD | 4,540.00 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,070,000.00 USD | 466.25 USD | 0.00 USD | `+68.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,070,000.00 USD | 468.75 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,070,000.00 USD | 471.25 USD | 0.00 USD | `+70.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,070,000.00 USD | 473.75 USD | 0.00 USD | `+71.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,130,000.00 USD | 67,000.00 USD | 0.00 USD | `+72.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,130,000.00 USD | 574.50 USD | 0.00 USD | `+73.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,140,000.00 USD | 577.50 USD | 0.00 USD | `+74.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,140,000.00 USD | 2,710.00 USD | 0.00 USD | `+74.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,140,000.00 USD | 972.50 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,150,000.00 USD | 7,680.00 USD | 0.00 USD | `+76.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,150,000.00 USD | 786.00 USD | 0.00 USD | `+77.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,150,000.00 USD | 790.00 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,150,000.00 USD | 992.50 USD | 0.00 USD | `+79.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,150,000.00 USD | 997.50 USD | 0.00 USD | `+80.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,750,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+81.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,750,000.00 USD | 1,010.00 USD | 0.00 USD | `+82.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,760,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,760,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+85.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,760,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,760,000.00 USD | 1,040.00 USD | 0.00 USD | `+87.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,760,000.00 USD | 1,410.00 USD | 0.00 USD | `+88.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,760,000.00 USD | 1,050.00 USD | 0.00 USD | `+89.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,770,000.00 USD | 4,000.00 USD | 0.00 USD | `+90.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,770,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,820,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,820,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+94.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,820,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,820,000.00 USD | 1,090.00 USD | 0.00 USD | `+96.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,820,000.00 USD | 3,280.00 USD | 0.00 USD | `+97.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+98.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,830,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,830,000.00 USD | 1,110.00 USD | 0.00 USD | `+100.31%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.10` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 48,090.00 USD | 9,480.00 USD | 36,170.00 USD |
| `7D` | `9.12` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 7,650.00 USD | 9,760.00 USD | 29,770.00 USD |
| `7D` | `9.14` | 14,880,000.00 USD | 0.00 USD | 14,880,000.00 USD | 27,430.00 USD | 15,540.00 USD | 6,960.00 USD |
| `7D` | `9.16` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 10,880.00 USD | 13,980.00 USD | 30,500.00 USD |
| `7D` | `9.18` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 33,470.00 USD | 13,370.00 USD | 10,180.00 USD |
| `7D` | `9.20` | 14,720,000.00 USD | 0.00 USD | 14,720,000.00 USD | 14,540.00 USD | 8,360.00 USD | 12.64 USD |
| `7D` | `9.22` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 1,120.00 USD | 6,480.00 USD | 10,450.00 USD |
| `7D` | `9.24` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 717.27 USD | 8,580.00 USD | 23,960.00 USD |
| `7D` | `9.26` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 24,320.00 USD | 3,320.00 USD | 11,760.00 USD |
| `7D` | `9.28` | 14,600,000.00 USD | 0.00 USD | 14,600,000.00 USD | 460.95 USD | 5,490.00 USD | 11,870.00 USD |
| `7D` | `9.30` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 32,460.00 USD | 10,930.00 USD | 12,520.00 USD |
| `7D` | `9.32` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 15,650.00 USD | 12,270.00 USD | 5,690.00 USD |
| `7D` | `9.34` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD |
| `7D` | `9.36` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 14,450,000.00 USD | 0.00 USD | 14,450,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD |
| `7D` | `9.40` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD |
| `7D` | `9.42` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD |
| `7D` | `9.44` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD |
| `7D` | `9.46` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD |
| `7D` | `9.48` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 14,180,000.00 USD | 0.00 USD | 14,180,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD |
| `7D` | `9.52` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD |
| `7D` | `9.54` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 472.74 USD | 15,010.00 USD | 10.22 USD |
| `7D` | `9.56` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD |
| `7D` | `9.58` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 38,760.00 USD | 722.15 USD | 4,210.00 USD |
| `7D` | `9.60` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 63,290.00 USD | 1,030.00 USD | 145,430.00 USD |
| `7D` | `9.62` | 13,760,000.00 USD | 0.00 USD | 13,760,000.00 USD | 5,420.00 USD | 0.00 USD | 219.95 USD |
| `7D` | `9.64` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 8,730.00 USD | 2,770.00 USD | 11,900.00 USD |
| `7D` | `9.66` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.68` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.70` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.74` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD |
| `7D` | `9.76` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD |
| `1D` | `9.78` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 113,700.00 USD | 7,910.00 USD | 38,060.00 USD |
| `7D` | `9.78` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD |
| `1D` | `9.80` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 44,560.00 USD | 5,670.00 USD | 465.49 USD |
| `7D` | `9.80` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD |
| `1D` | `9.82` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 85,490.00 USD | 14,930.00 USD | 27,620.00 USD |
| `7D` | `9.82` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `1D` | `9.84` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 17,970.00 USD | 7,030.00 USD | 294.14 USD |
| `7D` | `9.84` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD |
| `1D` | `9.86` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 23,360.00 USD | 3,910.00 USD | 10,100.00 USD |
| `7D` | `9.86` | 13,320,000.00 USD | 0.00 USD | 13,320,000.00 USD | 5,390.00 USD | 14,570.00 USD | 0.00 USD |
| `1D` | `9.88` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 2,240.00 USD | 8,620.00 USD | 5,190.00 USD |
| `7D` | `9.88` | 13,300,000.00 USD | 0.00 USD | 13,300,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD |
| `1D` | `9.90` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 37,440.00 USD | 27,290.00 USD | 5,280.00 USD |
| `7D` | `9.90` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.92` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 14,940.00 USD | 17,480.00 USD | 227.05 USD |
| `7D` | `9.92` | 13,230,000.00 USD | 0.00 USD | 13,230,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD |
| `1D` | `9.94` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 1,820.00 USD | 792.40 USD | 160.36 USD |
| `7D` | `9.94` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 14,920.00 USD | 50,950.00 USD | 26,390.00 USD |
| `1D` | `9.96` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 62,740.00 USD | 14,110.00 USD | 16,730.00 USD |
| `7D` | `9.96` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 11,410.00 USD | 1,090.00 USD |
| `1D` | `9.98` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 17,530.00 USD | 6,740.00 USD | 58,270.00 USD |
| `7D` | `9.98` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD |
| `1D` | `10.00` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 1,940.00 USD | 396.47 USD | 51,590.00 USD |
| `7D` | `10.00` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 12,870.00 USD |
| `1D` | `10.02` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 5,440.00 USD | 13,120.00 USD | 18,890.00 USD |
| `7D` | `10.02` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD |
| `1D` | `10.04` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 18,000.00 USD | 305.90 USD | 149.46 USD |
| `7D` | `10.04` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD |
| `1D` | `10.06` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,160.00 USD |
| `7D` | `10.06` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD |
| `1D` | `10.08` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 167,250.00 USD | 701.42 USD | 75,870.00 USD |
| `7D` | `10.08` | 12,930,000.00 USD | 0.00 USD | 12,930,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.10` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 7,570.00 USD | 42,810.00 USD | 100.16 USD |
| `7D` | `10.10` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD |
| `1D` | `10.12` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 1,150.00 USD | 20,910.00 USD | 213.92 USD |
| `7D` | `10.12` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD |
| `1D` | `10.14` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,740.00 USD |
| `7D` | `10.14` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD |
| `1D` | `10.16` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,470.00 USD |
| `7D` | `10.16` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD |
| `1D` | `10.18` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,150.00 USD |
| `7D` | `10.18` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD |
| `1D` | `10.20` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,120.00 USD |
| `7D` | `10.20` | 12,030,000.00 USD | 0.00 USD | 12,030,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD |
| `1D` | `10.22` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 37,870.00 USD | 22,340.00 USD | 344,650.00 USD |
| `7D` | `10.22` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD |
| `1D` | `10.24` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 122,230.00 USD | 71,270.00 USD | 22,480.00 USD |
| `7D` | `10.24` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,360.00 USD |
| `1D` | `10.26` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 66,420.00 USD | 8,070.00 USD | 100,810.00 USD |
| `7D` | `10.26` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD |
| `1D` | `10.28` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 172,700.00 USD | 12,030.00 USD | 176,310.00 USD |
| `7D` | `10.28` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.30` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 169,020.00 USD | 20,970.00 USD | 49,830.00 USD |
| `7D` | `10.30` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 457,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 24,180.00 USD | 1,380.00 USD | 81,070.00 USD |
| `7D` | `10.32` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 67,530.00 USD | 9,100.00 USD | 93,530.00 USD |
| `7D` | `10.34` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 56,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.36` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 5,630.00 USD | 3,580.00 USD | 344.35 USD |
| `7D` | `10.36` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.38` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 40,040.00 USD | 46,620.00 USD | 7,700.00 USD |
| `7D` | `10.38` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 88,080.00 USD | 32,290.00 USD | 66,780.00 USD |
| `7D` | `10.40` | 8,740,000.00 USD | 0.00 USD | 8,740,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 246,920.00 USD | 0.00 USD | 42.43 USD |
| `7D` | `10.42` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 229,660.00 USD | 97,940.00 USD | 0.00 USD |
| `1D` | `10.44` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 199,600.00 USD | 27,590.00 USD | 305,400.00 USD |
| `7D` | `10.44` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,100.00 USD |
| `7D` | `10.46` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.48` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 50,100.00 USD | 2,200.00 USD | 55,100.00 USD |
| `7D` | `10.48` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 15,010.00 USD | 36,830.00 USD | 25,420.00 USD |
| `7D` | `10.50` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 3,440.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.52` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 71.67 USD | 10,910.00 USD | 38,570.00 USD |
| `7D` | `10.52` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 0.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 57,000.00 USD | 131,920.00 USD |
| `7D` | `10.54` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD |
| `1D` | `10.56` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 94,750.00 USD | 23,930.00 USD | 12,820.00 USD |
| `7D` | `10.56` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 121,680.00 USD | 74,990.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 28,610.00 USD | 20,070.00 USD | 20,190.00 USD |
| `1D` | `10.60` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 4,790.00 USD | 0.00 USD |
| `7D` | `10.60` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 458.05 USD |
| `1D` | `10.62` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 4,840.00 USD | 118,210.00 USD |
| `7D` | `10.62` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 59,050.00 USD | 0.00 USD | 180.54 USD |
| `1D` | `10.64` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 42,010.00 USD | 660.00 USD | 23,920.00 USD |
| `7D` | `10.64` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 11,150.00 USD | 0.00 USD | 150.41 USD |
| `1D` | `10.66` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 29,760.00 USD | 3,610.00 USD | 32.25 USD |
| `7D` | `10.66` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD |
| `1D` | `10.68` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 0.00 USD | 9,970.00 USD | 36,190.00 USD |
| `7D` | `10.68` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 0.00 USD | 2,430.00 USD | 0.00 USD |
| `1D` | `10.70` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 12,670.00 USD | 7,160.00 USD | 0.00 USD |
| `7D` | `10.70` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.72` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.72` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 83,030.00 USD | 23,680.00 USD | 0.00 USD |
| `7D` | `10.74` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD |
| `1D` | `10.76` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 6,560.00 USD | 47,140.00 USD | 25,950.00 USD |
| `7D` | `10.76` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 16,310.00 USD | 109,140.00 USD | 0.00 USD |
| `1D` | `10.78` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 190,290.00 USD | 134,860.00 USD | 25,670.00 USD |
| `7D` | `10.78` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 535,020.00 USD | 32,650.00 USD | 103,760.00 USD |
| `1D` | `10.80` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 13,650.00 USD | 3,750.00 USD | 10,020.00 USD |
| `7D` | `10.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 23,450.00 USD | 70,260.00 USD | 0.00 USD |
| `1D` | `10.82` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 88,080.00 USD | 2,860.00 USD | 181.38 USD |
| `7D` | `10.82` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 56,610.00 USD | 206,380.00 USD |
| `1D` | `10.84` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 308,110.00 USD | 5,310.00 USD | 133.62 USD |
| `7D` | `10.84` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 295,700.00 USD | 80,420.00 USD | 196,240.00 USD |
| `1D` | `10.86` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 67,500.00 USD | 17,680.00 USD | 148,730.00 USD |
| `7D` | `10.86` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 323,850.00 USD | 3,610.00 USD | 333,920.00 USD |
| `1D` | `10.88` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 1,700.00 USD | 12.95 USD |
| `7D` | `10.88` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD |
| `1D` | `10.90` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 37,360.00 USD | 3,660.00 USD | 0.24 USD |
| `7D` | `10.90` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 220,890.00 USD |
| `1D` | `10.92` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 80,530.00 USD | 0.00 USD | 45.61 USD |
| `7D` | `10.92` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD |
| `1D` | `10.94` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.94` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,090.00 USD | 784.50 USD | 87,870.00 USD |
| `7D` | `10.96` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 10,430.00 USD | 0.00 USD | 50,570.00 USD |
| `1D` | `10.98` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 117.09 USD |
| `7D` | `10.98` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 17,930.00 USD | 0.00 USD | 209,840.00 USD |
| `1D` | `11.00` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | 2,520.00 USD | 653.16 USD |
| `7D` | `11.00` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 10,830.00 USD | 2,280.00 USD | 634.90 USD |
| `1D` | `11.02` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 5,330.00 USD | 27,810.00 USD | 151,400.00 USD |
| `7D` | `11.02` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,900.00 USD | 31,180.00 USD | 143,500.00 USD |
| `1D` | `11.04` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 163,320.00 USD | 18,120.00 USD | 179,100.00 USD |
| `7D` | `11.04` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 17,850.00 USD | 40,210.00 USD | 178,530.00 USD |
| `1D` | `11.06` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 518,210.00 USD | 30,510.00 USD | 106,820.00 USD |
| `7D` | `11.06` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 4,020.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.08` | 778,080.00 USD | 0.00 USD | 778,080.00 USD | 3,780.00 USD | 68,940.00 USD | 446,220.00 USD |
| `7D` | `11.08` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 14,890.00 USD | 1,810.00 USD | 167,460.00 USD |
| `1D` | `11.10` | 259,150.00 USD | 0.00 USD | 259,150.00 USD | 215,070.00 USD | 44,080.00 USD | 0.00 USD |
| `7D` | `11.10` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 301,790.00 USD | 23,300.00 USD | 173,360.00 USD |
| `1D` | `11.12` | 737,370.00 USD | 737,370.00 USD | 0.00 USD | 448,790.00 USD | 109,110.00 USD | 179,470.00 USD |
| `1D` | `11.12` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 448,790.00 USD | 109,110.00 USD | 179,470.00 USD |
| `7D` | `11.12` | 612,850.00 USD | 0.00 USD | 612,850.00 USD | 262,770.00 USD | 115,910.00 USD | 234,170.00 USD |
| `1D` | `11.14` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 230,290.00 USD | 19,930.00 USD | 68,100.00 USD |
| `7D` | `11.14` | 215,120.00 USD | 215,120.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `7D` | `11.14` | 430,230.00 USD | 430,230.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `1D` | `11.16` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 127,020.00 USD | 79,690.00 USD | 50,400.00 USD |
| `7D` | `11.16` | 699,610.00 USD | 699,610.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD |
| `1D` | `11.18` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 71,610.00 USD | 44,050.00 USD | 86,690.00 USD |
| `7D` | `11.18` | 717,100.00 USD | 717,100.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD |
| `1D` | `11.20` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 65,400.00 USD | 61,120.00 USD | 87,280.00 USD |
| `7D` | `11.20` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 171,840.00 USD | 78,020.00 USD | 79,190.00 USD |
| `1D` | `11.22` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 352,600.00 USD | 47,850.00 USD | 117,630.00 USD |
| `7D` | `11.22` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 482,460.00 USD | 28,690.00 USD | 603.14 USD |
| `1D` | `11.24` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 110,930.00 USD | 34,630.00 USD | 196,120.00 USD |
| `7D` | `11.24` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 184,900.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.26` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 130,470.00 USD | 13,530.00 USD | 105,730.00 USD |
| `7D` | `11.26` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 520,990.00 USD | 0.00 USD | 296,010.00 USD |
| `1D` | `11.28` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 293,730.00 USD | 59,090.00 USD | 243,630.00 USD |
| `7D` | `11.28` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 347,470.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 126,090.00 USD | 74,380.00 USD | 99,720.00 USD |
| `7D` | `11.30` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 20,610.00 USD |
| `1D` | `11.32` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 119,640.00 USD | 66,550.00 USD | 82,990.00 USD |
| `7D` | `11.32` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD |
| `1D` | `11.34` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 313,240.00 USD | 87,030.00 USD | 58,250.00 USD |
| `7D` | `11.34` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 127,190.00 USD | 78,260.00 USD | 101,390.00 USD |
| `1D` | `11.36` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 115,970.00 USD | 76,000.00 USD | 56,470.00 USD |
| `7D` | `11.36` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,170.00 USD |
| `7D` | `11.38` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD |
| `1D` | `11.40` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 39,080.00 USD | 32,990.00 USD | 104,510.00 USD |
| `7D` | `11.40` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD |
| `1D` | `11.42` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 112,540.00 USD | 68,020.00 USD | 92,100.00 USD |
| `7D` | `11.42` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 66,800.00 USD | 40,760.00 USD | 115,000.00 USD |
| `1D` | `11.44` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 84,630.00 USD | 40,410.00 USD | 84,210.00 USD |
| `7D` | `11.44` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 303,190.00 USD | 95,260.00 USD | 38,210.00 USD |
| `1D` | `11.46` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 59,980.00 USD | 65,340.00 USD | 48,870.00 USD |
| `7D` | `11.46` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 99,360.00 USD | 55,470.00 USD | 269.04 USD |
| `1D` | `11.48` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 14,620.00 USD | 15,390.00 USD | 262.76 USD |
| `7D` | `11.48` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 54,660.00 USD | 84,840.00 USD | 64,610.00 USD |
| `1D` | `11.50` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 31,090.00 USD | 34,670.00 USD | 45,960.00 USD |
| `7D` | `11.50` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 91,790.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 59,780.00 USD | 13,890.00 USD | 19,410.00 USD |
| `7D` | `11.52` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 33,540.00 USD |
| `1D` | `11.54` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 60,850.00 USD | 16,360.00 USD | 71,160.00 USD |
| `7D` | `11.54` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD |
| `1D` | `11.56` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 90,400.00 USD | 4,930.00 USD | 23,110.00 USD |
| `7D` | `11.56` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 86,650.00 USD | 793.25 USD | 432.76 USD |
| `1D` | `11.58` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 46,550.00 USD | 335.85 USD | 17,660.00 USD |
| `7D` | `11.58` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 91,240.00 USD | 7,320.00 USD | 67,360.00 USD |
| `7D` | `11.60` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 44,670.00 USD | 10,510.00 USD | 23,030.00 USD |
| `1D` | `11.62` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 44,130.00 USD | 512.95 USD | 48,320.00 USD |
| `7D` | `11.62` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 62,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.64` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 4,510.00 USD | 7,410.00 USD | 31,240.00 USD |
| `7D` | `11.64` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD |
| `1D` | `11.66` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,880.00 USD |
| `7D` | `11.66` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.68` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 124,510.00 USD | 35,770.00 USD | 31,900.00 USD |
| `7D` | `11.68` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD |
| `1D` | `11.70` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 4,760.00 USD | 15,400.00 USD |
| `7D` | `11.70` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 0.00 USD |
| `1D` | `11.72` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 158,470.00 USD | 18,090.00 USD | 98,090.00 USD |
| `7D` | `11.72` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD |
| `1D` | `11.74` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 75,970.00 USD | 30,440.00 USD | 73,050.00 USD |
| `7D` | `11.74` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD |
| `1D` | `11.76` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 26,090.00 USD | 15,090.00 USD | 24,650.00 USD |
| `7D` | `11.76` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD |
| `1D` | `11.78` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 27,290.00 USD | 20,660.00 USD | 40,100.00 USD |
| `7D` | `11.78` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 56,750.00 USD |
| `1D` | `11.80` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 1,190.00 USD | 18,160.00 USD | 313.96 USD |
| `7D` | `11.80` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 11,070.00 USD | 53.10 USD | 36,540.00 USD |
| `7D` | `11.82` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 180,980.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 71,130.00 USD | 11,870.00 USD | 60,750.00 USD |
| `7D` | `11.84` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD |
| `1D` | `11.86` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 10,930.00 USD | 14,080.00 USD | 51,100.00 USD |
| `7D` | `11.86` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD |
| `1D` | `11.88` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 19,750.00 USD | 29,160.00 USD | 60,210.00 USD |
| `7D` | `11.88` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD |
| `1D` | `11.90` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 43,700.00 USD | 8,750.00 USD | 27,960.00 USD |
| `7D` | `11.90` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.92` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 230,070.00 USD | 23,110.00 USD | 25,010.00 USD |
| `7D` | `11.92` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD |
| `1D` | `11.94` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 48,250.00 USD | 15,310.00 USD | 40,150.00 USD |
| `7D` | `11.94` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 64,140.00 USD | 40,240.00 USD | 48,040.00 USD |
| `7D` | `11.96` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD |
| `1D` | `11.98` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 78,260.00 USD | 29,060.00 USD | 81,790.00 USD |
| `7D` | `11.98` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD |
| `1D` | `12.00` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 120,680.00 USD | 24,060.00 USD | 44,720.00 USD |
| `7D` | `12.00` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD |
| `1D` | `12.02` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 14,380.00 USD | 11,370.00 USD | 31,460.00 USD |
| `7D` | `12.02` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD |
| `1D` | `12.04` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 90,910.00 USD | 39,490.00 USD | 56,280.00 USD |
| `7D` | `12.04` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD |
| `1D` | `12.06` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 76,810.00 USD | 43,200.00 USD | 69,680.00 USD |
| `7D` | `12.06` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,690.00 USD |
| `1D` | `12.08` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 38,930.00 USD | 35,220.00 USD | 48,320.00 USD |
| `7D` | `12.08` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD |
| `1D` | `12.10` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 48,930.00 USD | 20,220.00 USD | 27,540.00 USD |
| `7D` | `12.10` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 108,350.00 USD | 51,990.00 USD | 50,390.00 USD |
| `7D` | `12.12` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD |
| `1D` | `12.14` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 75,950.00 USD | 33,190.00 USD | 55,740.00 USD |
| `7D` | `12.14` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 147,420.00 USD | 92,520.00 USD | 119,290.00 USD |
| `1D` | `12.16` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 124,570.00 USD | 34,710.00 USD | 67,620.00 USD |
| `7D` | `12.16` | 13,440,000.00 USD | 13,440,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD |
| `1D` | `12.18` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 107,720.00 USD | 46,930.00 USD | 41,420.00 USD |
| `7D` | `12.18` | 13,580,000.00 USD | 13,580,000.00 USD | 0.00 USD | 57,680.00 USD | 54,220.00 USD | 32,160.00 USD |
| `1D` | `12.20` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 58,110.00 USD | 43,780.00 USD | 32,050.00 USD |
| `7D` | `12.20` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 91,300.00 USD |
| `1D` | `12.22` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 7,320.00 USD | 16,900.00 USD | 23,360.00 USD |
| `7D` | `12.22` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 106,120.00 USD |
| `1D` | `12.24` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 2,470.00 USD | 8,790.00 USD | 7,650.00 USD |
| `7D` | `12.24` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 70,650.00 USD | 54,230.00 USD | 115,100.00 USD |
| `1D` | `12.26` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 12,640.00 USD | 8,360.00 USD | 12,140.00 USD |
| `7D` | `12.26` | 14,880,000.00 USD | 14,880,000.00 USD | 0.00 USD | 192,800.00 USD | 55,780.00 USD | 50,600.00 USD |
| `1D` | `12.28` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 49,470.00 USD | 7,490.00 USD | 12,080.00 USD |
| `7D` | `12.28` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 215,790.00 USD | 52,850.00 USD | 148,350.00 USD |
| `1D` | `12.30` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 5,730.00 USD | 4,160.00 USD | 14,220.00 USD |
| `7D` | `12.30` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD |
| `7D` | `12.32` | 15,710,000.00 USD | 15,710,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 18,040.00 USD |
| `7D` | `12.34` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 48,630.00 USD | 18,250.00 USD | 13,590.00 USD |
| `7D` | `12.36` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 36,210.00 USD | 24,190.00 USD | 18,470.00 USD |
| `7D` | `12.38` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 7,170.00 USD | 6,880.00 USD | 55,410.00 USD |
| `7D` | `12.40` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 111,350.00 USD | 41,100.00 USD | 12,560.00 USD |
| `7D` | `12.42` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 23,200.00 USD | 21,440.00 USD | 10,400.00 USD |
| `7D` | `12.44` | 16,280,000.00 USD | 16,280,000.00 USD | 0.00 USD | 81,360.00 USD | 284.67 USD | 45,220.00 USD |
| `7D` | `12.46` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 39,540.00 USD | 25,610.00 USD | 86,160.00 USD |
| `7D` | `12.48` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 63,590.00 USD |
| `7D` | `12.50` | 16,790,000.00 USD | 16,790,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD |
| `7D` | `12.52` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 163,610.00 USD | 33,380.00 USD | 113,900.00 USD |
| `7D` | `12.54` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD |
| `7D` | `12.56` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 77,880.00 USD | 20,220.00 USD | 27,710.00 USD |
| `7D` | `12.58` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 41,760.00 USD | 34,570.00 USD | 41,450.00 USD |
| `7D` | `12.60` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 69,190.00 USD | 23,200.00 USD | 60,890.00 USD |
| `7D` | `12.62` | 17,820,000.00 USD | 17,820,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `7D` | `12.64` | 17,950,000.00 USD | 17,950,000.00 USD | 0.00 USD | 63,450.00 USD | 42,320.00 USD | 25,820.00 USD |
| `7D` | `12.66` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 22,530.00 USD | 5,030.00 USD | 8,780.00 USD |
| `7D` | `12.68` | 18,050,000.00 USD | 18,050,000.00 USD | 0.00 USD | 9,270.00 USD | 18,330.00 USD | 36,330.00 USD |
| `7D` | `12.70` | 18,110,000.00 USD | 18,110,000.00 USD | 0.00 USD | 2,010.00 USD | 617.78 USD | 52,460.00 USD |
| `7D` | `12.72` | 18,220,000.00 USD | 18,220,000.00 USD | 0.00 USD | 47,740.00 USD | 22,750.00 USD | 40,880.00 USD |
| `7D` | `12.74` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 38,570.00 USD | 26,370.00 USD | 40,430.00 USD |
| `7D` | `12.76` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 13,750.00 USD | 14,350.00 USD | 29,650.00 USD |
| `7D` | `12.78` | 18,560,000.00 USD | 18,560,000.00 USD | 0.00 USD | 109,130.00 USD | 16,110.00 USD | 52,020.00 USD |
| `7D` | `12.80` | 18,650,000.00 USD | 18,650,000.00 USD | 0.00 USD | 13,700.00 USD | 14,000.00 USD | 61,100.00 USD |
| `7D` | `12.82` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `7D` | `12.84` | 18,720,000.00 USD | 18,720,000.00 USD | 0.00 USD | 31,320.00 USD | 15,990.00 USD | 7,710.00 USD |
| `7D` | `12.86` | 18,790,000.00 USD | 18,790,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,210.00 USD |
| `7D` | `12.88` | 18,830,000.00 USD | 18,830,000.00 USD | 0.00 USD | 23,610.00 USD | 4,610.00 USD | 12,750.00 USD |
| `7D` | `12.90` | 18,910,000.00 USD | 18,910,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD |
| `7D` | `12.92` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 26,790.00 USD |
| `7D` | `12.94` | 19,030,000.00 USD | 19,030,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 69.74 USD |
| `7D` | `12.96` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 13,150.00 USD | 11,970.00 USD | 24,940.00 USD |
| `7D` | `12.98` | 19,120,000.00 USD | 19,120,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD |
| `7D` | `13.00` | 19,200,000.00 USD | 19,200,000.00 USD | 0.00 USD | 51,470.00 USD | 9,560.00 USD | 20,570.00 USD |
| `7D` | `13.02` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD |
| `7D` | `13.04` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 303.50 USD | 335.85 USD | 0.00 USD |
| `7D` | `13.06` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 22,310.00 USD | 3,370.00 USD | 5,250.00 USD |
| `7D` | `13.08` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 15,920.00 USD | 6,890.00 USD | 12,530.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `523.08M` | Total OI Tokens: `47,006,157.9 LINK`
  * 1h OI Change: `+0.92%` | 4h OI Change: `+0.39%` | 24h OI Change: `-5.66%`
  * Exchange Breakdown: Binance=`102.58M` | Bybit=`70.25M` | OKX=`26.96M` | Hyperliquid=`56.10M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-3.82K` | Last 24h: `29.28K` | Last 3d: `90.77K` | Last 7d: `184.78K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0089%` | **USDT OKX** | `-0.0066%` |
| **USDT Bybit** | `-0.0142%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0087%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0052%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `43.55%` | `56.45%` | `0.77` | 10,260,000.00 USD |
| `15M` | `Binance` | `37.63%` | `62.37%` | `0.60` | 5,340,000.00 USD |
| `15M` | `OKX` | `46.08%` | `53.92%` | `0.85` | 1,730,000.00 USD |
| `15M` | `Bybit` | `51.79%` | `48.21%` | `1.07` | 1,320,000.00 USD |
| `15M` | `KuCoin` | `44.97%` | `55.03%` | `0.82` | 188,070.00 USD |
| `15M` | `Gate` | `49.93%` | `50.07%` | `1.00` | 227,930.00 USD |
| `15M` | `Bitget` | `33.36%` | `66.64%` | `0.50` | 303,930.00 USD |
| `15M` | `BingX` | `38.94%` | `61.06%` | `0.64` | 230,450.00 USD |
| `15M` | `MEXC` | `58.71%` | `41.29%` | `1.42` | 52,390.00 USD |
| `15M` | `Bitunix` | `43.65%` | `56.35%` | `0.77` | 148,550.00 USD |
| `15M` | `Hyperliquid` | `89.05%` | `10.95%` | `8.13` | 256,840.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.74%` | `50.26%` | `0.99` | 171,670.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 46,870.00 USD |
| `15M` | `HTX` | `27.51%` | `72.49%` | `0.38` | 136,270.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `84.6%` | `15.4%` | `5.49` | 23,250.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `91.86%` | `8.14%` | `11.29` | 77,860.00 USD |
| `15M` | `Whale Positions` | `37.63%` | `62.37%` | `0.60` | 5,340,000.00 USD |
| `15M` | `Global Accounts` | `43.55%` | `56.45%` | `0.77` | 10,260,000.00 USD |
| `1H` | `LINK` | `45.38%` | `54.62%` | `0.83` | 32,940,000.00 USD |
| `1H` | `Binance` | `41.44%` | `58.56%` | `0.71` | 16,090,000.00 USD |
| `1H` | `OKX` | `42.57%` | `57.43%` | `0.74` | 4,770,000.00 USD |
| `1H` | `Bybit` | `53.88%` | `46.12%` | `1.17` | 6,040,000.00 USD |
| `1H` | `KuCoin` | `46.42%` | `53.58%` | `0.87` | 749,520.00 USD |
| `1H` | `Gate` | `51.62%` | `48.38%` | `1.07` | 719,090.00 USD |
| `1H` | `Bitget` | `47.76%` | `52.24%` | `0.91` | 1,520,000.00 USD |
| `1H` | `BingX` | `29.87%` | `70.13%` | `0.43` | 337,950.00 USD |
| `1H` | `MEXC` | `54%` | `46%` | `1.17` | 204,590.00 USD |
| `1H` | `Bitunix` | `50.27%` | `49.73%` | `1.01` | 447,970.00 USD |
| `1H` | `Hyperliquid` | `58.78%` | `41.22%` | `1.43` | 875,550.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.93%` | `50.07%` | `1.00` | 349,050.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `51.42%` | `48.58%` | `1.06` | 361,140.00 USD |
| `1H` | `HTX` | `31.86%` | `68.14%` | `0.47` | 208,810.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `60.44%` | `39.56%` | `1.53` | 68,210.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `66.26%` | `33.74%` | `1.96` | 199,040.00 USD |
| `1H` | `Whale Positions` | `41.44%` | `58.56%` | `0.71` | 16,090,000.00 USD |
| `1H` | `Global Accounts` | `45.38%` | `54.62%` | `0.83` | 32,940,000.00 USD |
| `4H` | `LINK` | `47.02%` | `52.98%` | `0.89` | 142,300,000.00 USD |
| `4H` | `Binance` | `47.47%` | `52.53%` | `0.90` | 62,920,000.00 USD |
| `4H` | `OKX` | `46.37%` | `53.63%` | `0.86` | 19,630,000.00 USD |
| `4H` | `Bybit` | `48.82%` | `51.18%` | `0.95` | 25,970,000.00 USD |
| `4H` | `KuCoin` | `48.27%` | `51.73%` | `0.93` | 3,260,000.00 USD |
| `4H` | `Gate` | `38.86%` | `61.14%` | `0.64` | 8,440,000.00 USD |
| `4H` | `Bitget` | `44.79%` | `55.21%` | `0.81` | 5,920,000.00 USD |
| `4H` | `BingX` | `26.96%` | `73.04%` | `0.37` | 1,490,000.00 USD |
| `4H` | `MEXC` | `51.74%` | `48.26%` | `1.07` | 2,340,000.00 USD |
| `4H` | `Bitunix` | `45.4%` | `54.6%` | `0.83` | 1,980,000.00 USD |
| `4H` | `Hyperliquid` | `54.46%` | `45.54%` | `1.20` | 4,700,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.48%` | `52.52%` | `0.90` | 1,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.18%` | `53.82%` | `0.86` | 1,870,000.00 USD |
| `4H` | `HTX` | `44.48%` | `55.52%` | `0.80` | 675,170.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.25%` | `56.75%` | `0.76` | 319,300.00 USD |
| `4H` | `Aster` | `45.89%` | `54.11%` | `0.85` | 172,070.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `55.63%` | `44.37%` | `1.25` | 722,870.00 USD |
| `4H` | `Whale Positions` | `47.47%` | `52.53%` | `0.90` | 62,920,000.00 USD |
| `4H` | `Global Accounts` | `47.02%` | `52.98%` | `0.89` | 142,300,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `10.80` | `10.78` | `10.80` | `10.81` | `10.74` | 1,669,099.58 USD | 861,868.55 USD | 807,231.03 USD | 54,637.51 USD | `+3.27%` | `11B / 7S` |
| `0:00 UTC` | `10.91` | `10.88` | `10.91` | `10.95` | `10.78` | 3,369,524.30 USD | 1,989,204.80 USD | 1,380,319.50 USD | 608,885.30 USD | `+18.07%` | `47B / 26S` |
| `5:00 UTC` | `10.94` | `10.95` | `10.94` | `10.98` | `10.93` | 1,915,931.41 USD | 933,547.46 USD | 982,383.95 USD | -48,836.49 USD | `-2.55%` | `2B / 6S` |
| `0:00 UTC` | `10.93` | `10.94` | `10.93` | `10.99` | `10.90` | 2,589,400.57 USD | 1,319,072.00 USD | 1,270,328.57 USD | 48,743.44 USD | `+1.88%` | `17B / 14S` |
| `5:00 UTC` | `10.99` | `10.99` | `10.99` | `11.02` | `10.96` | 1,907,525.28 USD | 901,785.44 USD | 1,005,739.84 USD | -103,954.39 USD | `-5.45%` | `12B / 13S` |
| `0:00 UTC` | `10.99` | `11.00` | `10.99` | `11.02` | `10.96` | 4,049,528.45 USD | 2,107,266.70 USD | 1,942,261.75 USD | 165,004.95 USD | `+4.07%` | `6B / 12S` |
| `5:00 UTC` | `11.08` | `11.06` | `11.08` | `11.09` | `11.01` | 2,811,297.51 USD | 1,507,938.86 USD | 1,303,358.65 USD | 204,580.21 USD | `+7.28%` | `16B / 8S` |
| `0:00 UTC` | `11.09` | `11.11` | `11.09` | `11.16` | `11.05` | 2,051,224.58 USD | 1,043,229.65 USD | 1,007,994.93 USD | 35,234.71 USD | `+1.72%` | `20B / 16S` |
| `5:00 UTC` | `11.12` | `11.13` | `11.12` | `11.15` | `11.11` | 1,272,358.25 USD | 643,125.20 USD | 629,233.05 USD | 13,892.16 USD | `+1.09%` | `3B / 5S` |
| `0:00 UTC` | `11.12` | `11.12` | `11.12` | `11.15` | `11.10` | 1,122,257.93 USD | 516,602.62 USD | 605,655.31 USD | -89,052.69 USD | `-7.94%` | `5B / 11S` |

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
| `5m` | 152,360.00 USD | -241,480.00 USD | **`DISTRIBUTION`** |
| `15m` | 74,630.00 USD | -501,560.00 USD | **`DISTRIBUTION`** |
| `30m` | 67,670.00 USD | -446,950.00 USD | **`DISTRIBUTION`** |
| `1h` | -223,880.00 USD | -2,830.00 USD | **`DISTRIBUTION`** |
| `2h` | -869,630.00 USD | -1,310,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,170,000.00 USD | 228,940.00 USD | **`DISTRIBUTION`** |
| `6h` | -899,390.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | -5,700,000.00 USD | -20,510,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -11,710,000.00 USD | -21,800,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,110,000.00 USD | -20,550,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -20,470,000.00 USD | -45,690,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -78,260,000.00 USD | -199,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+152.36K` | 15m=`+74.63K` | 1h=`-223.88K` | 24h=`-11.11M`
* Futures Capital Netflows: 5m=`-241.48K` | 15m=`-501.56K` | 1h=`-2.83K` | 24h=`-20.55M`
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
  * Execution Entry: `10.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.10` (Risk Distance: `0.2501` pts)
  * +2.5R Take Profit: `10.98`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `10.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.17` (Risk Distance: `0.2501` pts)
  * +2.5R Take Profit: `10.29`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.21`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
