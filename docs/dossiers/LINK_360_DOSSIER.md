# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 02:24:36 IST` (`2026-10-29 20:54:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.03` | **Live Ask Quote**: `11.13` | **Mid Price**: `11.08`
- **Spread Points**: `110.00` | **Spread BPS**: `99.28 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.08` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.16` | Lower -3.00σ Band: `11.00`
  * Upper +2.51σ Band: `11.14` | Lower -2.51σ Band: `11.02`
  * Upper +2.01σ Band: `11.13` | Lower -2.01σ Band: `11.03`
  * Upper +2.00σ Band: `11.12` | Lower -2.00σ Band: `11.04`
  * Upper +1.28σ Band: `11.11` | Lower -1.28σ Band: `11.05`
  * Upper +1.00σ Band: `11.10` | Lower -1.00σ Band: `11.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.08` | EMA-20=`11.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.08` (Slope: `+0.0000`) | EMA-100=`11.08`
  * Institutional Anchors: EMA-144=`11.08` | EMA-200=`11.08` (Slope: `+0.0000`) | EMA-233=`11.08`
- **Range Boundaries**: 24H High=`11.19` | 24H Low=`10.97` | Weekly High=`11.30` | Weekly Low=`10.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.89` (Distance: `-6.63%`)
  * Point of Control (POC) = `11.77` (Distance: `-5.72%`)
  * Value Area Low (VAL) = `11.43` (Distance: `-2.88%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.69` | POC=`11.50` | VAL=`11.44`
  * Prior Day Extremes: PDH=`11.94` | PDL=`11.38` | PDC=`11.75`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.59` | Weekly POC=`11.41` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.85` | Low=`11.23`
  * London Session (08:00-16:00 UTC): High=`11.60` | Low=`11.30`
  * New York Session (13:00-21:00 UTC): High=`11.96` | Low=`11.41`
  * Initial Balance (First Hour): IB High=`11.56` | IB Low=`11.41`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.04` - `11.12`
  * Optimal Trade Entry (OTE 0.705): `11.10`
  * Structural Invalidation Anchor (0.786): `11.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.52` | `11.55` | `11.34` | `11.38` | `283,704` | 3,235,376.73 USD | -644,223.14 USD | `-19.91%` | -3,514,685.61 USD | `-2.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `11.38` | `11.42` | `11.33` | `11.35` | `231,586` | 2,633,741.06 USD | -90,828.55 USD | `-3.45%` | -3,605,514.16 USD | `-0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `11.35` | `11.36` | `11.03` | `11.07` | `743,137` | 8,312,129.94 USD | -2,098,862.80 USD | `-25.25%` | -5,704,376.97 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `11.69` | `11.69` | `11.42` | `11.52` | `611,861` | 7,047,642.07 USD | -268,666.88 USD | `-3.81%` | -2,768,755.52 USD | `-0.76` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `11.52` | `11.56` | `11.49` | `11.52` | `166,417` | 1,919,098.80 USD | -101,706.95 USD | `-5.30%` | -2,870,462.47 USD | `-0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `11.52` | `11.55` | `11.03` | `11.10` | `1,246,540` | 14,049,430.14 USD | -2,812,104.10 USD | `-20.02%` | -5,682,566.57 USD | `-4.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `11.74` | `11.76` | `11.62` | `11.68` | `461,460` | 5,390,854.94 USD | 388,230.26 USD | `+7.20%` | -2,106,527.93 USD | `+0.85` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `11.68` | `11.73` | `11.63` | `11.69` | `318,927` | 3,725,220.26 USD | -245,323.17 USD | `-6.59%` | -2,351,851.10 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.69` | `11.69` | `11.03` | `11.07` | `2,036,705` | 23,147,988.60 USD | -3,204,288.33 USD | `-13.84%` | -5,556,139.43 USD | `-3.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `11.03` | `11.10` | `2,024,818` | 23,016,171.01 USD | -3,182,477.94 USD | `-13.83%` | -4,900,975.54 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `11.03` | `11.10` | `2,024,818` | 23,016,171.01 USD | -3,182,477.94 USD | `-13.83%` | -4,900,975.54 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `498` | `0x73ce...8ce9` | `LONG` | 4,548,531.90 USD | `400,011,600.00` | `12.05` | `10.94` | `9.12` | -271,221.80 USD | `-5.96%` | `5X Cross` |
| `652` | `0xb83d...6e36` | `SHORT` | 3,503,996.39 USD | `308,152,000.00` | `12.93` | `10.94` | `455.38` | 481,257.10 USD | `+13.73%` | `3X Cross` |
| `662` | `0x5b5d...c060` | `SHORT` | 3,465,482.40 USD | `311,728,200.00` | `13.61` | `10.94` | `563.22` | 776,649.71 USD | `+22.41%` | `3X Cross` |
| `870` | `0x458d...ab3b` | `LONG` | 2,622,296.94 USD | `227,156,700.00` | `13.13` | `10.94` | `9.34` | -359,933.45 USD | `-13.73%` | `3X Isolated` |
| `977` | `0x3dc9...54b0` | `SHORT` | 2,308,200.00 USD | `200,000,000.00` | `7.56` | `10.94` | `85.43` | -797,041.58 USD | `-34.53%` | `10X Cross` |
| `990` | `0xdd53...2b13` | `SHORT` | 2,285,475.10 USD | `206,475,300.00` | `11.92` | `10.94` | `306.12` | 175,747.83 USD | `+7.69%` | `3X Cross` |
| `1031` | `0x45d2...4029` | `SHORT` | 2,161,057.00 USD | `195,500,000.00` | `11.54` | `10.94` | `221.28` | 95,426.43 USD | `+4.42%` | `10X Cross` |
| `1258` | `0x6540...f7b7` | `LONG` | 1,816,745.67 USD | `163,759,300.00` | `12.48` | `10.94` | `8.01` | -226,431.26 USD | `-12.46%` | `5X Isolated` |
| `1263` | `0xeadc...9d55` | `LONG` | 1,811,245.72 USD | `157,691,600.00` | `9.43` | `10.94` | `0.000000` | 324,590.82 USD | `+17.92%` | `10X Cross` |
| `1693` | `0x9df2...c665` | `SHORT` | 1,279,760.27 USD | `115,773,500.00` | `11.48` | `10.94` | `280.12` | 49,773.15 USD | `+3.89%` | `10X Cross` |
| `1710` | `0xf6f3...47f8` | `SHORT` | 1,266,075.77 USD | `115,024,600.00` | `11.42` | `10.94` | `20.68` | 47,254.41 USD | `+3.73%` | `5X Cross` |
| `1830` | `0xfe7e...11b4` | `LONG` | 1,146,950.28 USD | `101,142,000.00` | `14.47` | `10.94` | `5.33` | -316,162.87 USD | `-27.57%` | `5X Isolated` |
| `1890` | `0x8af7...fa05` | `SHORT` | 1,098,395.14 USD | `98,661,200.00` | `14.08` | `10.94` | `205.57` | 290,787.40 USD | `+26.47%` | `10X Cross` |
| `1904` | `0xb7ec...5166` | `LONG` | 1,085,704.14 USD | `94,515,900.00` | `9.01` | `10.94` | `7.20` | 233,843.57 USD | `+21.54%` | `4X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.56` | 7,438.09 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.44K USD at 11.5570 USD [API] | `2026-10-28 00:12:05` |
| `ANNOUNCEMENT` | `INFO` | `11.62` | 5,464.86 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.6150 USD [API] | `2026-10-28 01:42:58` |
| `ANNOUNCEMENT` | `INFO` | `11.69` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6900 USD [API] | `2026-10-28 04:27:58` |


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
| `Live` | `Long Liquidation` | `2.25` | 747.68 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 4,510.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 30,100.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,240.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 220.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 7,930.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 650.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 927.95 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 369.15 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 302.46 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 379.88 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 9,940.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 2,090.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 2,150.00 USD | 13,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 5,090.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 264.05 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 381.37 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 222,950.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 383.63 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 418.95 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 1,200.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 22,190.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 55,550.00 USD | 13,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 31,030.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,210.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 633,510.00 USD | 13,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 499.77 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 10,170.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 43,840.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 5,120.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 32,070.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 909.76 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 62,770.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 48,450.00 USD | 12,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 42,490.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 16,590.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 141,680.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 15,940.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 4,130.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,820.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 3,700.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 2,740.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 687,520.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 20,150.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 30,960.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 10,880.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 17,030.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,150.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 2,890.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 726.91 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 41,640.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,390,000.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 16,320.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 34,670.00 USD | 10,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,770.00 USD | 10,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 10,670.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 43,900.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 11,540.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 304,290.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 35,020.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 486,640.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 42,820.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,760,000.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 25,310.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,170,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 19,500.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 14,380.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 8,830.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.75` | 103,770.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.85` | 17,700.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 142.30 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 118.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 1,660,000.00 USD | 1,660,000.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 782,600.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 1,660,000.00 USD | 1,660,000.00 USD | 7,630.00 USD | 5,270.00 USD | 44.44 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 645,720.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 44,810.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 1,650,000.00 USD | 1,650,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 1,630,000.00 USD | 1,630,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 1,610,000.00 USD | 1,610,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 20,290,000.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 278,400.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 1,550,000.00 USD | 1,550,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 19,910,000.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 1,540,000.00 USD | 1,540,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 19,770,000.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 1,490,000.00 USD | 1,490,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 19,650,000.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 1,470,000.00 USD | 1,470,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 19,540,000.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 1,420,000.00 USD | 1,420,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 19,400,000.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 9,660.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 1,370,000.00 USD | 1,370,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 19,270,000.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 1,350,000.00 USD | 1,350,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 19,240,000.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 1,330,000.00 USD | 1,330,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 19,180,000.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 1,300,000.00 USD | 1,300,000.00 USD | 20,220.00 USD | 10,800.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 19,030,000.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 1,260,000.00 USD | 1,260,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 18,950,000.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 175,650.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 1,190,000.00 USD | 1,190,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 18,890,000.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 1,170,000.00 USD | 1,170,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 18,780,000.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 1,140,000.00 USD | 1,140,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 18,730,000.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 1,100,000.00 USD | 1,100,000.00 USD | 29,580.00 USD | 4,150.00 USD | 30,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 18,660,000.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 1,030,000.00 USD | 1,030,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 18,590,000.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 40,130.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 1,030,000.00 USD | 1,030,000.00 USD | 16,190.00 USD | 5,660.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 18,550,000.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 1,000,000.00 USD | 1,000,000.00 USD | 3,210.00 USD | 2,820.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 18,460,000.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 987,290.00 USD | 987,290.00 USD | 1,040.00 USD | 5,090.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 18,350,000.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 977,980.00 USD | 977,980.00 USD | 41,350.00 USD | 5,560.00 USD | 12,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 18,300,000.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 918,930.00 USD | 918,930.00 USD | 13,350.00 USD | 20,650.00 USD | 16,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 18,250,000.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 44,080.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 868,390.00 USD | 868,390.00 USD | 17,480.00 USD | 0.00 USD | 4,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 18,200,000.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 846,240.00 USD | 846,240.00 USD | 17,550.00 USD | 2,850.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 18,180,000.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 824,290.00 USD | 824,290.00 USD | 12,300.00 USD | 2,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 18,150,000.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 809,700.00 USD | 809,700.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 18,130,000.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 791,260.00 USD | 791,260.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 18,090,000.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 214,040.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 714,050.00 USD | 714,050.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 18,070,000.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 694,950.00 USD | 694,950.00 USD | 1,070.00 USD | 2,540.00 USD | 57.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 18,050,000.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 691,270.00 USD | 691,270.00 USD | 4,360.00 USD | 0.00 USD | 123.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 18,010,000.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 686,790.00 USD | 686,790.00 USD | 2,030.00 USD | 260.12 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 17,870,000.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 684,430.00 USD | 684,430.00 USD | 54,340.00 USD | 776.90 USD | 31.01 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 17,690,000.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 85,390.00 USD | 866,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 629,290.00 USD | 629,290.00 USD | 976.86 USD | 30,260.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 17,540,000.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 594,230.00 USD | 594,230.00 USD | 1,820.00 USD | 10,400.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 17,190,000.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 558,160.00 USD | 558,160.00 USD | 23,940.00 USD | 3,600.00 USD | 0.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 16,720,000.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 530,620.00 USD | 530,620.00 USD | 97,980.00 USD | 28,740.00 USD | 0.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 16,290,000.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 403,900.00 USD | 403,900.00 USD | 46,920.00 USD | 17,060.00 USD | 81.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 15,390,000.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 558,110.00 USD | 781,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 339,830.00 USD | 339,830.00 USD | 96,940.00 USD | 23,010.00 USD | 96.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 14,800,000.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 219,790.00 USD | 219,790.00 USD | 23,750.00 USD | 2,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 14,240,000.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 193,630.00 USD | 193,630.00 USD | 35,500.00 USD | 12,760.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 13,870,000.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 130,190.00 USD | 130,190.00 USD | 0.00 USD | 23,720.00 USD | 31,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 13,480,000.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 74,600.00 USD | 74,600.00 USD | 0.00 USD | 0.00 USD | 23,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 12,970,000.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.05` | 147,130.00 USD | 223,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.06` | 50,950.00 USD | 50,950.00 USD | 0.00 USD | 0.00 USD | 50,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.06` | 12,320,000.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.08` | 29,350.00 USD | 29,350.00 USD | 0.00 USD | 0.00 USD | 29,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.08` | 11,910,000.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 118,000.00 USD | 118,000.00 USD | 0.00 USD | 24,890.00 USD | 63,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.10` | 11,100,000.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 234,160.00 USD | 234,160.00 USD | 632.30 USD | 39,730.00 USD | 75,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.12` | 9,910,000.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 490,710.00 USD | 490,710.00 USD | 1,890.00 USD | 79,990.00 USD | 174,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.14` | 8,860,000.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.15` | 25,090.00 USD | 75,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.16` | 652,000.00 USD | 652,000.00 USD | 337.20 USD | 51,930.00 USD | 109,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.16` | 7,370,000.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 956,110.00 USD | 956,110.00 USD | 137,030.00 USD | 49,160.00 USD | 117,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.18` | 6,060,000.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 1,330,000.00 USD | 1,330,000.00 USD | 222,000.00 USD | 52,080.00 USD | 98,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.20` | 4,630,000.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,590,000.00 USD | 1,590,000.00 USD | 177,480.00 USD | 43,930.00 USD | 43,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.22` | 3,870,000.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 56,190.00 USD | 70,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.24` | 3,160,000.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.25` | 41,990.00 USD | 50,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.26` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 41,120.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.26` | 2,860,000.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 2,010,000.00 USD | 2,010,000.00 USD | 38,150.00 USD | 21,180.00 USD | 117,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.28` | 2,290,000.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 59,870.00 USD | 41,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.30` | 1,880,000.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 2,140,000.00 USD | 2,140,000.00 USD | 323.10 USD | 34,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.32` | 1,810,000.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 2,400,000.00 USD | 2,400,000.00 USD | 197,970.00 USD | 53,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.34` | 1,640,000.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `11.35` | 8,900.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.36` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 83,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.36` | 1,280,000.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 55,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.38` | 962,530.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.40` | 871,150.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 2,860,000.00 USD | 2,860,000.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.42` | 677,690.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 391.00 USD | 52,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.44` | 536,960.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.46` | 264,830.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 4,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.48` | 128,570.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 2,940,000.00 USD | 2,940,000.00 USD | 19,080.00 USD | 11,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.50` | 88,130.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 2,990,000.00 USD | 2,990,000.00 USD | 29,340.00 USD | 12,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 94,830.00 USD | 94,830.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.56` | 3,070,000.00 USD | 3,070,000.00 USD | 64,190.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 3,130,000.00 USD | 3,130,000.00 USD | 45,400.00 USD | 75.80 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 3,280,000.00 USD | 3,280,000.00 USD | 99,240.00 USD | 0.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 3,360,000.00 USD | 3,360,000.00 USD | 42,200.00 USD | 0.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 222,010.00 USD | 222,010.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 3,430,000.00 USD | 3,430,000.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 3,680,000.00 USD | 3,680,000.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 484,570.00 USD | 484,570.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 3,810,000.00 USD | 3,810,000.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 3,860,000.00 USD | 3,860,000.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 532,760.00 USD | 532,760.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 3,940,000.00 USD | 3,940,000.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 14,340.00 USD | 66.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 672,880.00 USD | 672,880.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 3,980,000.00 USD | 3,980,000.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 873,430.00 USD | 873,430.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 4,120,000.00 USD | 4,120,000.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.86` | 4,190,000.00 USD | 4,190,000.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 4,280,000.00 USD | 4,280,000.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 4,340,000.00 USD | 4,340,000.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 4,510,000.00 USD | 4,510,000.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 4,580,000.00 USD | 4,580,000.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 4,690,000.00 USD | 4,690,000.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 4,850,000.00 USD | 4,850,000.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 4,950,000.00 USD | 4,950,000.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 5,060,000.00 USD | 5,060,000.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 5,430,000.00 USD | 5,430,000.00 USD | 209,440.00 USD | 71,010.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 5,880,000.00 USD | 5,880,000.00 USD | 187,660.00 USD | 88,160.00 USD | 165,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 6,080,000.00 USD | 6,080,000.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 6,130,000.00 USD | 6,130,000.00 USD | 19,140.00 USD | 9,690.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 6,380,000.00 USD | 6,380,000.00 USD | 124,790.00 USD | 54,500.00 USD | 63,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 6,560,000.00 USD | 6,560,000.00 USD | 92,340.00 USD | 33,040.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.16` | 6,780,000.00 USD | 6,780,000.00 USD | 126,410.00 USD | 37,730.00 USD | 59,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 6,970,000.00 USD | 6,970,000.00 USD | 112,590.00 USD | 42,150.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 7,100,000.00 USD | 7,100,000.00 USD | 77,890.00 USD | 37,080.00 USD | 20,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 7,160,000.00 USD | 7,160,000.00 USD | 12,890.00 USD | 16,530.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 7,190,000.00 USD | 7,190,000.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 4,720.00 USD | 6,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 7,280,000.00 USD | 7,280,000.00 USD | 43,220.00 USD | 24,590.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 7,410,000.00 USD | 7,410,000.00 USD | 73,710.00 USD | 17,410.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 7,530,000.00 USD | 7,530,000.00 USD | 57,170.00 USD | 16,300.00 USD | 45,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 7,540,000.00 USD | 7,540,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 7,580,000.00 USD | 7,580,000.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 6,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 7,610,000.00 USD | 7,610,000.00 USD | 19,360.00 USD | 9,040.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 7,650,000.00 USD | 7,650,000.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 7,710,000.00 USD | 7,710,000.00 USD | 18,820.00 USD | 12,140.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 7,790,000.00 USD | 7,790,000.00 USD | 57,850.00 USD | 13,980.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 7,820,000.00 USD | 7,820,000.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 4,240.00 USD | 11,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.46` | 7,840,000.00 USD | 7,840,000.00 USD | 411.51 USD | 9,440.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 7,850,000.00 USD | 7,850,000.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 7,860,000.00 USD | 7,860,000.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 7,930,000.00 USD | 7,930,000.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 7,940,000.00 USD | 7,940,000.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.56` | 7,990,000.00 USD | 7,990,000.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 8,010,000.00 USD | 8,010,000.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 8,030,000.00 USD | 8,030,000.00 USD | 15,910.00 USD | 3,320.00 USD | 1,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 8,060,000.00 USD | 8,060,000.00 USD | 13,610.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 8,110,000.00 USD | 8,110,000.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.66` | 8,130,000.00 USD | 8,130,000.00 USD | 4,580.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 8,150,000.00 USD | 8,150,000.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 8,190,000.00 USD | 8,190,000.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 8,220,000.00 USD | 8,220,000.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 8,290,000.00 USD | 8,290,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 8,310,000.00 USD | 8,310,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 8,340,000.00 USD | 8,340,000.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 8,350,000.00 USD | 8,350,000.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 8,380,000.00 USD | 8,380,000.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 11,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 8,420,000.00 USD | 8,420,000.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 8,430,000.00 USD | 8,430,000.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 8,450,000.00 USD | 8,450,000.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 8,460,000.00 USD | 8,460,000.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 8,460,000.00 USD | 8,460,000.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 8,470,000.00 USD | 8,470,000.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 8,510,000.00 USD | 8,510,000.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 8,550,000.00 USD | 8,550,000.00 USD | 11,890.00 USD | 7,680.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.00` | 14,560,000.00 USD | 14,560,000.00 USD | 28,040.00 USD | 9,560.00 USD | 7,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.02` | 14,580,000.00 USD | 14,580,000.00 USD | 267.65 USD | 6,200.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.04` | 14,580,000.00 USD | 14,580,000.00 USD | 303.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 113.53 USD | 11,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.06` | 14,580,000.00 USD | 14,580,000.00 USD | 0.00 USD | 3,370.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.10` | 14,620,000.00 USD | 14,620,000.00 USD | 18,460.00 USD | 5,730.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.12` | 14,620,000.00 USD | 14,620,000.00 USD | 945.50 USD | 4,010.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.14` | 14,620,000.00 USD | 14,620,000.00 USD | 321.45 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.15` | 274.84 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.16` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 57.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.18` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 3,960.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.20` | 14,650,000.00 USD | 14,650,000.00 USD | 972.55 USD | 0.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.22` | 14,680,000.00 USD | 14,680,000.00 USD | 23,980.00 USD | 213.60 USD | 37.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.24` | 14,710,000.00 USD | 14,710,000.00 USD | 18,770.00 USD | 4,640.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.26` | 14,730,000.00 USD | 14,730,000.00 USD | 463.75 USD | 5,860.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 14,740,000.00 USD | 14,740,000.00 USD | 9,830.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.35` | 113.48 USD | 11,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 7,500.00 USD | 19,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 1,760.00 USD | 20,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 37,130.00 USD | 58,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 952.84 USD | 59,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 59,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 621.16 USD | 60,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 85,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 16,240.00 USD | 101,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 102,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.75` | 34,810.00 USD | 137,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 193,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 193,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.05` | 452.61 USD | 194,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 4,990.00 USD | 199,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 26,300.00 USD | 225,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.65` | 466.20 USD | 226,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 65,630.00 USD | 291,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 371,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 372,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 242.90 USD | 373,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 95,020.00 USD | 468,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 246,540.00 USD | 714,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 714,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 715,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 717,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 721,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 1,980.00 USD | 723,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 723,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 2,160,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.05` | 316.23 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.25` | 571.73 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 418.37 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 767,400.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.65` | 167.27 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.55` | 66,030.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 2,900.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.25` | 413,290.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `22.35` | 894.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.15` | 236.13 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `23.35` | 238.17 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 13,900,000.00 USD | 0.00 USD | 747.68 USD | `-80.76%` | `332,300.00` |
| `Live` | `Long` | `2.35` | 13,900,000.00 USD | 0.00 USD | 4,510.00 USD | `-79.90%` | `1,920,000.00` |
| `Live` | `Long` | `2.45` | 13,900,000.00 USD | 0.00 USD | 30,100.00 USD | `-79.05%` | `12,286,800.00` |
| `Live` | `Long` | `2.65` | 13,870,000.00 USD | 0.00 USD | 2,240.00 USD | `-77.34%` | `844,000.00` |
| `Live` | `Long` | `2.75` | 13,870,000.00 USD | 0.00 USD | 220.00 USD | `-76.48%` | `80,000.00` |
| `Live` | `Long` | `3.05` | 13,870,000.00 USD | 0.00 USD | 6,390.00 USD | `-73.91%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 13,860,000.00 USD | 0.00 USD | 7,930.00 USD | `-73.06%` | `2,516,600.00` |
| `Live` | `Long` | `3.25` | 13,850,000.00 USD | 0.00 USD | 650.00 USD | `-72.20%` | `200,000.00` |
| `Live` | `Long` | `3.35` | 13,850,000.00 USD | 0.00 USD | 927.95 USD | `-71.35%` | `277,000.00` |
| `Live` | `Long` | `3.45` | 13,850,000.00 USD | 0.00 USD | 369.15 USD | `-70.49%` | `107,000.00` |
| `Live` | `Long` | `3.55` | 13,850,000.00 USD | 0.00 USD | 302.46 USD | `-69.64%` | `85,200.00` |
| `Live` | `Long` | `3.65` | 13,850,000.00 USD | 0.00 USD | 2,190.00 USD | `-68.78%` | `600,000.00` |
| `Live` | `Long` | `3.75` | 13,850,000.00 USD | 0.00 USD | 379.88 USD | `-67.93%` | `101,300.00` |
| `Live` | `Long` | `3.95` | 13,850,000.00 USD | 0.00 USD | 9,940.00 USD | `-66.22%` | `2,517,100.00` |
| `Live` | `Long` | `4.05` | 13,840,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.36%` | `516,400.00` |
| `Live` | `Long` | `4.15` | 13,840,000.00 USD | 0.00 USD | 2,150.00 USD | `-64.51%` | `517,600.00` |
| `Live` | `Long` | `4.25` | 13,830,000.00 USD | 0.00 USD | 5,090.00 USD | `-63.65%` | `1,198,100.00` |
| `Live` | `Long` | `4.35` | 13,830,000.00 USD | 0.00 USD | 264.05 USD | `-62.80%` | `60,700.00` |
| `Live` | `Long` | `4.45` | 13,830,000.00 USD | 0.00 USD | 381.37 USD | `-61.94%` | `85,700.00` |
| `Live` | `Long` | `4.55` | 13,830,000.00 USD | 0.00 USD | 222,950.00 USD | `-61.09%` | `49,000,000.00` |
| `Live` | `Long` | `4.65` | 13,600,000.00 USD | 0.00 USD | 383.63 USD | `-60.23%` | `82,500.00` |
| `Live` | `Long` | `4.75` | 13,600,000.00 USD | 0.00 USD | 418.95 USD | `-59.38%` | `88,200.00` |
| `Live` | `Long` | `4.85` | 13,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-58.52%` | `247,100.00` |
| `Live` | `Long` | `4.95` | 13,600,000.00 USD | 0.00 USD | 22,190.00 USD | `-57.67%` | `4,483,600.00` |
| `Live` | `Long` | `5.05` | 13,580,000.00 USD | 0.00 USD | 55,550.00 USD | `-56.81%` | `11,000,000.00` |
| `Live` | `Long` | `5.15` | 13,520,000.00 USD | 0.00 USD | 31,030.00 USD | `-55.95%` | `6,024,400.00` |
| `Live` | `Long` | `5.25` | 13,490,000.00 USD | 0.00 USD | 1,210.00 USD | `-55.10%` | `229,600.00` |
| `Live` | `Long` | `5.35` | 13,490,000.00 USD | 0.00 USD | 633,510.00 USD | `-54.24%` | `118,413,600.00` |
| `Live` | `Long` | `5.45` | 12,860,000.00 USD | 0.00 USD | 499.77 USD | `-53.39%` | `91,700.00` |
| `Live` | `Long` | `5.55` | 12,860,000.00 USD | 0.00 USD | 10,170.00 USD | `-52.53%` | `1,831,900.00` |
| `Live` | `Long` | `5.65` | 12,850,000.00 USD | 0.00 USD | 43,840.00 USD | `-51.68%` | `7,759,700.00` |
| `Live` | `Long` | `5.75` | 12,800,000.00 USD | 0.00 USD | 5,120.00 USD | `-50.82%` | `890,900.00` |
| `Live` | `Long` | `5.85` | 12,800,000.00 USD | 0.00 USD | 32,070.00 USD | `-49.97%` | `5,482,600.00` |
| `Live` | `Long` | `5.95` | 12,770,000.00 USD | 0.00 USD | 909.76 USD | `-49.11%` | `152,900.00` |
| `Live` | `Long` | `6.05` | 12,770,000.00 USD | 0.00 USD | 62,770.00 USD | `-48.26%` | `10,374,600.00` |
| `Live` | `Long` | `6.15` | 12,700,000.00 USD | 0.00 USD | 48,450.00 USD | `-47.40%` | `7,878,800.00` |
| `Live` | `Long` | `6.25` | 12,660,000.00 USD | 0.00 USD | 42,490.00 USD | `-46.55%` | `6,799,200.00` |
| `Live` | `Long` | `6.35` | 12,610,000.00 USD | 0.00 USD | 16,590.00 USD | `-45.69%` | `2,612,900.00` |
| `Live` | `Long` | `6.45` | 12,600,000.00 USD | 0.00 USD | 141,680.00 USD | `-44.84%` | `21,966,200.00` |
| `Live` | `Long` | `6.55` | 12,450,000.00 USD | 0.00 USD | 15,940.00 USD | `-43.98%` | `2,433,500.00` |
| `Live` | `Long` | `6.65` | 12,440,000.00 USD | 0.00 USD | 9,260.00 USD | `-43.13%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 12,430,000.00 USD | 0.00 USD | 4,130.00 USD | `-42.27%` | `612,000.00` |
| `Live` | `Long` | `6.85` | 12,430,000.00 USD | 0.00 USD | 5,820.00 USD | `-41.42%` | `849,200.00` |
| `Live` | `Long` | `6.95` | 12,420,000.00 USD | 0.00 USD | 3,700.00 USD | `-40.56%` | `532,400.00` |
| `Live` | `Long` | `7.05` | 12,420,000.00 USD | 0.00 USD | 2,740.00 USD | `-39.70%` | `388,400.00` |
| `Live` | `Long` | `7.15` | 12,410,000.00 USD | 0.00 USD | 687,520.00 USD | `-38.85%` | `96,156,800.00` |
| `Live` | `Long` | `7.25` | 11,730,000.00 USD | 0.00 USD | 20,150.00 USD | `-37.99%` | `2,778,700.00` |
| `Live` | `Long` | `7.35` | 11,710,000.00 USD | 0.00 USD | 30,960.00 USD | `-37.14%` | `4,211,800.00` |
| `Live` | `Long` | `7.45` | 11,670,000.00 USD | 0.00 USD | 10,880.00 USD | `-36.28%` | `1,460,900.00` |
| `Live` | `Long` | `7.55` | 11,660,000.00 USD | 0.00 USD | 17,030.00 USD | `-35.43%` | `2,255,200.00` |
| `Live` | `Long` | `7.65` | 11,650,000.00 USD | 0.00 USD | 1,150.00 USD | `-34.57%` | `150,000.00` |
| `Live` | `Long` | `7.75` | 11,650,000.00 USD | 0.00 USD | 2,890.00 USD | `-33.72%` | `373,100.00` |
| `Live` | `Long` | `7.85` | 11,640,000.00 USD | 0.00 USD | 726.91 USD | `-32.86%` | `92,600.00` |
| `Live` | `Long` | `7.95` | 11,640,000.00 USD | 0.00 USD | 41,640.00 USD | `-32.01%` | `5,238,200.00` |
| `Live` | `Long` | `8.05` | 11,600,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-31.15%` | `172,206,300.00` |
| `Live` | `Long` | `8.15` | 10,210,000.00 USD | 0.00 USD | 16,320.00 USD | `-30.30%` | `2,002,500.00` |
| `Live` | `Long` | `8.25` | 10,200,000.00 USD | 0.00 USD | 34,670.00 USD | `-29.44%` | `4,202,500.00` |
| `Live` | `Long` | `8.35` | 10,160,000.00 USD | 0.00 USD | 7,770.00 USD | `-28.59%` | `930,800.00` |
| `Live` | `Long` | `8.45` | 10,150,000.00 USD | 0.00 USD | 10,670.00 USD | `-27.73%` | `1,263,100.00` |
| `Live` | `Long` | `8.55` | 10,140,000.00 USD | 0.00 USD | 43,900.00 USD | `-26.88%` | `5,134,100.00` |
| `Live` | `Long` | `8.65` | 10,100,000.00 USD | 0.00 USD | 11,540.00 USD | `-26.02%` | `1,333,800.00` |
| `Live` | `Long` | `8.75` | 10,090,000.00 USD | 0.00 USD | 304,290.00 USD | `-25.17%` | `34,776,300.00` |
| `Live` | `Long` | `8.85` | 9,780,000.00 USD | 0.00 USD | 35,020.00 USD | `-24.31%` | `3,957,300.00` |
| `Live` | `Long` | `8.95` | 9,750,000.00 USD | 0.00 USD | 486,640.00 USD | `-23.46%` | `54,373,700.00` |
| `Live` | `Long` | `9.05` | 9,260,000.00 USD | 0.00 USD | 42,820.00 USD | `-22.60%` | `4,731,900.00` |
| `Live` | `Long` | `9.15` | 9,220,000.00 USD | 0.00 USD | 3,760,000.00 USD | `-21.74%` | `410,561,400.00` |
| `Live` | `Long` | `9.25` | 5,460,000.00 USD | 0.00 USD | 25,310.00 USD | `-20.89%` | `2,736,500.00` |
| `Live` | `Long` | `9.35` | 5,440,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-20.03%` | `232,320,500.00` |
| `Live` | `Long` | `9.45` | 3,270,000.00 USD | 0.00 USD | 19,500.00 USD | `-19.18%` | `2,064,000.00` |
| `Live` | `Long` | `9.55` | 3,250,000.00 USD | 0.00 USD | 14,380.00 USD | `-18.32%` | `1,505,500.00` |
| `Live` | `Long` | `9.65` | 3,230,000.00 USD | 0.00 USD | 8,830.00 USD | `-17.47%` | `914,600.00` |
| `Live` | `Long` | `9.75` | 3,220,000.00 USD | 0.00 USD | 103,770.00 USD | `-16.61%` | `10,642,900.00` |
| `Live` | `Long` | `9.85` | 3,120,000.00 USD | 0.00 USD | 17,700.00 USD | `-15.76%` | `1,796,600.00` |
| `Live` | `Long` | `9.95` | 3,100,000.00 USD | 0.00 USD | 782,600.00 USD | `-14.90%` | `78,653,300.00` |
| `Live` | `Long` | `10.05` | 2,320,000.00 USD | 0.00 USD | 645,720.00 USD | `-14.05%` | `64,250,500.00` |
| `Live` | `Long` | `10.15` | 1,670,000.00 USD | 0.00 USD | 44,810.00 USD | `-13.19%` | `4,415,000.00` |
| `Live` | `Long` | `10.25` | 1,630,000.00 USD | 0.00 USD | 278,400.00 USD | `-12.34%` | `27,161,100.00` |
| `Live` | `Long` | `10.35` | 1,350,000.00 USD | 0.00 USD | 9,660.00 USD | `-11.48%` | `933,500.00` |
| `Live` | `Long` | `10.45` | 1,340,000.00 USD | 0.00 USD | 175,650.00 USD | `-10.63%` | `16,808,400.00` |
| `Live` | `Long` | `10.55` | 1,160,000.00 USD | 0.00 USD | 40,130.00 USD | `-9.77%` | `3,803,600.00` |
| `Live` | `Long` | `10.65` | 1,120,000.00 USD | 0.00 USD | 44,080.00 USD | `-8.92%` | `4,138,800.00` |
| `Live` | `Long` | `10.75` | 1,080,000.00 USD | 0.00 USD | 214,040.00 USD | `-8.06%` | `19,910,900.00` |
| `Live` | `Long` | `10.85` | 866,620.00 USD | 0.00 USD | 85,390.00 USD | `-7.21%` | `7,870,500.00` |
| `Live` | `Long` | `10.95` | 781,230.00 USD | 0.00 USD | 558,110.00 USD | `-6.35%` | `50,969,000.00` |
| `Live` | `Long` | `11.05` | 223,120.00 USD | 0.00 USD | 147,130.00 USD | `-5.49%` | `13,314,900.00` |
| `Live` | `Long` | `11.15` | 75,990.00 USD | 0.00 USD | 25,090.00 USD | `-4.64%` | `2,250,600.00` |
| `Live` | `Long` | `11.25` | 50,890.00 USD | 0.00 USD | 41,990.00 USD | `-3.78%` | `3,732,700.00` |
| `Live` | `Long` | `11.35` | 8,900.00 USD | 0.00 USD | 8,900.00 USD | `-2.93%` | `784,000.00` |
| `Live` | `Short` | `12.15` | 1,390.00 USD | 1,390.00 USD | 0.00 USD | `+3.91%` | `114,600.00` |
| `Live` | `Short` | `12.25` | 6,120.00 USD | 4,720.00 USD | 0.00 USD | `+4.77%` | `385,600.00` |
| `Live` | `Short` | `12.35` | 6,850.00 USD | 736.06 USD | 0.00 USD | `+5.62%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 11,090.00 USD | 4,240.00 USD | 0.00 USD | `+6.48%` | `340,500.00` |
| `Live` | `Short` | `12.85` | 11,230.00 USD | 138.78 USD | 0.00 USD | `+9.90%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 11,340.00 USD | 113.53 USD | 0.00 USD | `+11.61%` | `8,700.00` |
| `Live` | `Short` | `13.15` | 11,620.00 USD | 274.84 USD | 0.00 USD | `+12.47%` | `20,900.00` |
| `Live` | `Short` | `13.35` | 11,730.00 USD | 113.48 USD | 0.00 USD | `+14.18%` | `8,500.00` |
| `Live` | `Short` | `13.45` | 19,230.00 USD | 7,500.00 USD | 0.00 USD | `+15.03%` | `557,600.00` |
| `Live` | `Short` | `13.55` | 20,990.00 USD | 1,760.00 USD | 0.00 USD | `+15.89%` | `130,100.00` |
| `Live` | `Short` | `13.95` | 58,130.00 USD | 37,130.00 USD | 0.00 USD | `+19.31%` | `2,661,900.00` |
| `Live` | `Short` | `14.35` | 59,080.00 USD | 952.84 USD | 0.00 USD | `+22.73%` | `66,400.00` |
| `Live` | `Short` | `14.45` | 59,620.00 USD | 541.88 USD | 0.00 USD | `+23.58%` | `37,500.00` |
| `Live` | `Short` | `14.65` | 60,240.00 USD | 621.16 USD | 0.00 USD | `+25.29%` | `42,400.00` |
| `Live` | `Short` | `14.95` | 85,580.00 USD | 25,330.00 USD | 0.00 USD | `+27.86%` | `1,694,600.00` |
| `Live` | `Short` | `15.35` | 101,820.00 USD | 16,240.00 USD | 0.00 USD | `+31.28%` | `1,058,000.00` |
| `Live` | `Short` | `15.55` | 102,660.00 USD | 838.14 USD | 0.00 USD | `+32.99%` | `53,900.00` |
| `Live` | `Short` | `15.75` | 137,460.00 USD | 34,810.00 USD | 0.00 USD | `+34.70%` | `2,210,000.00` |
| `Live` | `Short` | `15.85` | 193,810.00 USD | 56,350.00 USD | 0.00 USD | `+35.56%` | `3,554,900.00` |
| `Live` | `Short` | `15.95` | 193,950.00 USD | 138.76 USD | 0.00 USD | `+36.41%` | `8,700.00` |
| `Live` | `Short` | `16.05` | 194,400.00 USD | 452.61 USD | 0.00 USD | `+37.27%` | `28,200.00` |
| `Live` | `Short` | `16.15` | 199,390.00 USD | 4,990.00 USD | 0.00 USD | `+38.12%` | `309,000.00` |
| `Live` | `Short` | `16.35` | 225,690.00 USD | 26,300.00 USD | 0.00 USD | `+39.83%` | `1,608,300.00` |
| `Live` | `Short` | `16.65` | 226,150.00 USD | 466.20 USD | 0.00 USD | `+42.40%` | `28,000.00` |
| `Live` | `Short` | `16.85` | 291,780.00 USD | 65,630.00 USD | 0.00 USD | `+44.11%` | `3,895,000.00` |
| `Live` | `Short` | `16.95` | 371,560.00 USD | 79,770.00 USD | 0.00 USD | `+44.96%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 372,920.00 USD | 1,370.00 USD | 0.00 USD | `+46.68%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 373,170.00 USD | 242.90 USD | 0.00 USD | `+48.39%` | `14,000.00` |
| `Live` | `Short` | `17.45` | 468,180.00 USD | 95,020.00 USD | 0.00 USD | `+49.24%` | `5,445,000.00` |
| `Live` | `Short` | `17.65` | 714,720.00 USD | 246,540.00 USD | 0.00 USD | `+50.95%` | `13,968,000.00` |
| `Live` | `Short` | `17.85` | 714,970.00 USD | 249.90 USD | 0.00 USD | `+52.66%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 715,590.00 USD | 621.07 USD | 0.00 USD | `+53.52%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 717,560.00 USD | 1,970.00 USD | 0.00 USD | `+54.37%` | `109,300.00` |
| `Live` | `Short` | `18.45` | 721,450.00 USD | 3,890.00 USD | 0.00 USD | `+57.79%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 723,430.00 USD | 1,980.00 USD | 0.00 USD | `+58.65%` | `106,900.00` |
| `Live` | `Short` | `18.65` | 723,620.00 USD | 186.50 USD | 0.00 USD | `+59.50%` | `10,000.00` |
| `Live` | `Short` | `18.75` | 2,880,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+60.36%` | `115,024,600.00` |
| `Live` | `Short` | `18.85` | 2,880,000.00 USD | 456.17 USD | 0.00 USD | `+61.21%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,900,000.00 USD | 16,250.00 USD | 0.00 USD | `+62.07%` | `857,700.00` |
| `Live` | `Short` | `19.05` | 2,900,000.00 USD | 316.23 USD | 0.00 USD | `+62.92%` | `16,600.00` |
| `Live` | `Short` | `19.25` | 2,900,000.00 USD | 571.73 USD | 0.00 USD | `+64.64%` | `29,700.00` |
| `Live` | `Short` | `19.55` | 2,900,000.00 USD | 418.37 USD | 0.00 USD | `+67.20%` | `21,400.00` |
| `Live` | `Short` | `19.65` | 2,940,000.00 USD | 38,790.00 USD | 0.00 USD | `+68.06%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,940,000.00 USD | 291.27 USD | 0.00 USD | `+70.62%` | `14,600.00` |
| `Live` | `Short` | `20.35` | 3,700,000.00 USD | 767,400.00 USD | 0.00 USD | `+74.04%` | `37,710,000.00` |
| `Live` | `Short` | `20.55` | 3,710,000.00 USD | 7,250.00 USD | 0.00 USD | `+75.75%` | `353,000.00` |
| `Live` | `Short` | `20.65` | 3,710,000.00 USD | 167.27 USD | 0.00 USD | `+76.61%` | `8,100.00` |
| `Live` | `Short` | `21.55` | 3,780,000.00 USD | 66,030.00 USD | 0.00 USD | `+84.31%` | `3,064,200.00` |
| `Live` | `Short` | `21.75` | 3,780,000.00 USD | 2,900.00 USD | 0.00 USD | `+86.02%` | `133,300.00` |
| `Live` | `Short` | `22.25` | 4,190,000.00 USD | 413,290.00 USD | 0.00 USD | `+90.29%` | `18,575,000.00` |
| `Live` | `Short` | `22.35` | 4,200,000.00 USD | 894.00 USD | 0.00 USD | `+91.15%` | `40,000.00` |
| `Live` | `Short` | `23.15` | 4,200,000.00 USD | 236.13 USD | 0.00 USD | `+97.99%` | `10,200.00` |
| `Live` | `Short` | `23.35` | 4,200,000.00 USD | 238.17 USD | 0.00 USD | `+99.70%` | `10,200.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 837,910.00 USD | 0.00 USD | 431.68 USD | `-69.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 837,470.00 USD | 0.00 USD | 290.29 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 837,180.00 USD | 0.00 USD | 120.22 USD | `-55.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 837,060.00 USD | 0.00 USD | 107.09 USD | `-48.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 836,960.00 USD | 0.00 USD | 3,760.00 USD | `-43.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 833,190.00 USD | 0.00 USD | 133.00 USD | `-43.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 833,060.00 USD | 0.00 USD | 3,770.00 USD | `-39.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 829,290.00 USD | 0.00 USD | 2,070.00 USD | `-37.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 827,220.00 USD | 0.00 USD | 3,740.00 USD | `-36.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 823,480.00 USD | 0.00 USD | 1,050.00 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 822,420.00 USD | 0.00 USD | 146.80 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 822,280.00 USD | 0.00 USD | 5,000.00 USD | `-31.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 817,280.00 USD | 0.00 USD | 393.64 USD | `-30.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 816,880.00 USD | 0.00 USD | 10,660.00 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 806,220.00 USD | 0.00 USD | 1,360.00 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 804,860.00 USD | 0.00 USD | 30,250.00 USD | `-26.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 774,610.00 USD | 0.00 USD | 186.84 USD | `-26.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 774,430.00 USD | 0.00 USD | 742.88 USD | `-25.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 773,680.00 USD | 0.00 USD | 196.47 USD | `-24.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 773,490.00 USD | 0.00 USD | 1,520.00 USD | `-23.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 771,970.00 USD | 0.00 USD | 2,240.00 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 769,730.00 USD | 0.00 USD | 194.90 USD | `-21.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 769,530.00 USD | 0.00 USD | 4,940.00 USD | `-20.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 764,590.00 USD | 0.00 USD | 9,870.00 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 754,720.00 USD | 0.00 USD | 3,550.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 751,170.00 USD | 0.00 USD | 25,950.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 725,220.00 USD | 0.00 USD | 19,100.00 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 706,120.00 USD | 0.00 USD | 299,650.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 406,470.00 USD | 0.00 USD | 2,590.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 403,880.00 USD | 0.00 USD | 1,050.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 402,830.00 USD | 0.00 USD | 2,820.00 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 400,010.00 USD | 0.00 USD | 6,330.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 393,680.00 USD | 0.00 USD | 19,650.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 374,030.00 USD | 0.00 USD | 5,160.00 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 368,860.00 USD | 0.00 USD | 4,590.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 364,270.00 USD | 0.00 USD | 5,470.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 358,790.00 USD | 0.00 USD | 3,780.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 355,010.00 USD | 0.00 USD | 3,270.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.05` | 351,740.00 USD | 0.00 USD | 18,860.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.15` | 332,880.00 USD | 0.00 USD | 27,100.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.25` | 305,770.00 USD | 0.00 USD | 69,570.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.35` | 236,210.00 USD | 0.00 USD | 13,780.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.45` | 222,430.00 USD | 0.00 USD | 48,420.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.55` | 174,010.00 USD | 0.00 USD | 54,150.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `11.65` | 119,870.00 USD | 0.00 USD | 119,870.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 6,620.00 USD | 2,160.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 6,780.00 USD | 156.55 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 63,050.00 USD | 56,270.00 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 65,010.00 USD | 1,960.00 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 75,320.00 USD | 10,320.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 76,660.00 USD | 1,340.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 77,160.00 USD | 500.49 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 88,270.00 USD | 11,110.00 USD | 0.00 USD | `+7.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 144,800.00 USD | 56,530.00 USD | 0.00 USD | `+8.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 186,280.00 USD | 41,470.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 207,010.00 USD | 20,730.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 207,470.00 USD | 461.02 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 213,970.00 USD | 6,500.00 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 215,020.00 USD | 1,050.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 218,860.00 USD | 3,840.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 223,850.00 USD | 4,990.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 238,250.00 USD | 14,400.00 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 240,880.00 USD | 2,630.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 242,900.00 USD | 2,020.00 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 244,960.00 USD | 2,060.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 245,090.00 USD | 120.50 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 245,350.00 USD | 266.44 USD | 0.00 USD | `+19.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 262,460.00 USD | 17,110.00 USD | 0.00 USD | `+20.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 263,260.00 USD | 798.06 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 270,250.00 USD | 6,990.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 270,470.00 USD | 218.25 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 273,080.00 USD | 2,610.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 286,000.00 USD | 12,920.00 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 286,950.00 USD | 950.82 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 298,460.00 USD | 11,500.00 USD | 0.00 USD | `+28.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 302,640.00 USD | 4,180.00 USD | 0.00 USD | `+29.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 535,680.00 USD | 233,040.00 USD | 0.00 USD | `+30.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 540,070.00 USD | 4,380.00 USD | 0.00 USD | `+31.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 540,960.00 USD | 893.01 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 541,350.00 USD | 388.75 USD | 0.00 USD | `+32.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 568,400.00 USD | 27,050.00 USD | 0.00 USD | `+33.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 570,730.00 USD | 2,330.00 USD | 0.00 USD | `+34.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 576,070.00 USD | 5,340.00 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 581,390.00 USD | 5,320.00 USD | 0.00 USD | `+36.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 590,560.00 USD | 9,170.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 597,360.00 USD | 6,800.00 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 616,120.00 USD | 18,760.00 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 622,660.00 USD | 6,540.00 USD | 0.00 USD | `+39.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 629,240.00 USD | 6,580.00 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 639,170.00 USD | 9,930.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 652,490.00 USD | 13,320.00 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 666,730.00 USD | 14,240.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 751,090.00 USD | 84,360.00 USD | 0.00 USD | `+44.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 752,780.00 USD | 1,700.00 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 762,290.00 USD | 9,510.00 USD | 0.00 USD | `+45.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 764,000.00 USD | 1,710.00 USD | 0.00 USD | `+46.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 766,250.00 USD | 2,250.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 864,590.00 USD | 98,330.00 USD | 0.00 USD | `+48.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 886,260.00 USD | 21,670.00 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 892,690.00 USD | 6,430.00 USD | 0.00 USD | `+50.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 897,100.00 USD | 4,410.00 USD | 0.00 USD | `+50.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 901,540.00 USD | 4,440.00 USD | 0.00 USD | `+51.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 906,000.00 USD | 4,460.00 USD | 0.00 USD | `+52.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 906,450.00 USD | 448.75 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 942,030.00 USD | 35,590.00 USD | 0.00 USD | `+54.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 942,490.00 USD | 453.75 USD | 0.00 USD | `+55.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 943,320.00 USD | 830.38 USD | 0.00 USD | `+56.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 943,780.00 USD | 458.75 USD | 0.00 USD | `+56.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 944,240.00 USD | 461.25 USD | 0.00 USD | `+57.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 948,780.00 USD | 4,540.00 USD | 0.00 USD | `+58.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 949,250.00 USD | 466.25 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 949,720.00 USD | 468.75 USD | 0.00 USD | `+60.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 950,190.00 USD | 471.25 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 950,660.00 USD | 473.75 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,020,000.00 USD | 67,000.00 USD | 0.00 USD | `+62.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,020,000.00 USD | 574.50 USD | 0.00 USD | `+63.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,020,000.00 USD | 577.50 USD | 0.00 USD | `+64.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,020,000.00 USD | 2,710.00 USD | 0.00 USD | `+65.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,020,000.00 USD | 972.50 USD | 0.00 USD | `+66.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,030,000.00 USD | 7,680.00 USD | 0.00 USD | `+67.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,030,000.00 USD | 1,680.00 USD | 0.00 USD | `+68.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,030,000.00 USD | 1,690.00 USD | 0.00 USD | `+68.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,030,000.00 USD | 992.50 USD | 0.00 USD | `+69.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,040,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,650,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,650,000.00 USD | 1,010.00 USD | 0.00 USD | `+72.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,660,000.00 USD | 1,010.00 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,660,000.00 USD | 1,030.00 USD | 0.00 USD | `+75.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,660,000.00 USD | 1,030.00 USD | 0.00 USD | `+76.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,660,000.00 USD | 1,860.00 USD | 0.00 USD | `+77.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,660,000.00 USD | 1,410.00 USD | 0.00 USD | `+78.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,660,000.00 USD | 1,050.00 USD | 0.00 USD | `+79.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,670,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,670,000.00 USD | 1,060.00 USD | 0.00 USD | `+80.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,670,000.00 USD | 1,060.00 USD | 0.00 USD | `+81.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,720,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+82.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,720,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,720,000.00 USD | 1,080.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,720,000.00 USD | 1,090.00 USD | 0.00 USD | `+86.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,730,000.00 USD | 3,280.00 USD | 0.00 USD | `+86.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,730,000.00 USD | 1,100.00 USD | 0.00 USD | `+87.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,730,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.15` | 3,730,000.00 USD | 1,110.00 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.25` | 3,730,000.00 USD | 1,110.00 USD | 0.00 USD | `+90.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.35` | 3,730,000.00 USD | 1,120.00 USD | 0.00 USD | `+91.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.45` | 3,730,000.00 USD | 1,120.00 USD | 0.00 USD | `+92.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.55` | 3,730,000.00 USD | 1,130.00 USD | 0.00 USD | `+92.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.65` | 3,730,000.00 USD | 1,130.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.75` | 3,740,000.00 USD | 1,140.00 USD | 0.00 USD | `+94.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.85` | 3,740,000.00 USD | 1,140.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.95` | 3,740,000.00 USD | 1,150.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.05` | 3,870,000.00 USD | 129,920.00 USD | 0.00 USD | `+97.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.15` | 3,870,000.00 USD | 1,160.00 USD | 0.00 USD | `+97.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.25` | 3,870,000.00 USD | 1,160.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `23.35` | 3,870,000.00 USD | 1,170.00 USD | 0.00 USD | `+99.70%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `9.86` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 0.00 USD | 142.30 USD | 10,090.00 USD |
| `1D` | `9.92` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 118.68 USD |
| `1D` | `9.94` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.96` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 7,630.00 USD | 5,270.00 USD | 44.44 USD |
| `1D` | `10.06` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD |
| `1D` | `10.14` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD |
| `1D` | `10.16` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD |
| `1D` | `10.18` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD |
| `1D` | `10.20` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD |
| `1D` | `10.22` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD |
| `1D` | `10.24` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,210.00 USD |
| `7D` | `10.24` | 20,290,000.00 USD | 0.00 USD | 20,290,000.00 USD | 185,330.00 USD | 40,380.00 USD | 148,530.00 USD |
| `1D` | `10.26` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `10.26` | 19,910,000.00 USD | 0.00 USD | 19,910,000.00 USD | 41,640.00 USD | 32,250.00 USD | 70,270.00 USD |
| `1D` | `10.28` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD |
| `7D` | `10.28` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 75,000.00 USD | 20,220.00 USD | 27,070.00 USD |
| `1D` | `10.30` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD |
| `7D` | `10.30` | 19,650,000.00 USD | 0.00 USD | 19,650,000.00 USD | 27,600.00 USD | 34,570.00 USD | 40,890.00 USD |
| `1D` | `10.32` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,380.00 USD |
| `7D` | `10.32` | 19,540,000.00 USD | 0.00 USD | 19,540,000.00 USD | 49,920.00 USD | 36,350.00 USD | 58,780.00 USD |
| `1D` | `10.34` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `10.34` | 19,400,000.00 USD | 0.00 USD | 19,400,000.00 USD | 58,890.00 USD | 42,320.00 USD | 25,770.00 USD |
| `1D` | `10.36` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `10.36` | 19,270,000.00 USD | 0.00 USD | 19,270,000.00 USD | 20,010.00 USD | 5,030.00 USD | 8,660.00 USD |
| `1D` | `10.38` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `10.38` | 19,240,000.00 USD | 0.00 USD | 19,240,000.00 USD | 8,810.00 USD | 12,810.00 USD | 36,330.00 USD |
| `1D` | `10.40` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD |
| `7D` | `10.40` | 19,180,000.00 USD | 0.00 USD | 19,180,000.00 USD | 46,970.00 USD | 22,340.00 USD | 82,000.00 USD |
| `1D` | `10.42` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 20,220.00 USD | 10,800.00 USD | 6,580.00 USD |
| `7D` | `10.42` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 38,080.00 USD | 18,330.00 USD | 20,870.00 USD |
| `1D` | `10.44` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `10.44` | 18,950,000.00 USD | 0.00 USD | 18,950,000.00 USD | 13,750.00 USD | 14,350.00 USD | 29,560.00 USD |
| `1D` | `10.46` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `10.46` | 18,890,000.00 USD | 0.00 USD | 18,890,000.00 USD | 77,730.00 USD | 15,750.00 USD | 18,540.00 USD |
| `1D` | `10.48` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD |
| `7D` | `10.48` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 12,660.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `10.50` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD |
| `7D` | `10.50` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 42,030.00 USD | 16,130.00 USD | 12,670.00 USD |
| `1D` | `10.52` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 29,580.00 USD | 4,150.00 USD | 30,670.00 USD |
| `7D` | `10.52` | 18,660,000.00 USD | 0.00 USD | 18,660,000.00 USD | 33,920.00 USD | 8,750.00 USD | 27,230.00 USD |
| `1D` | `10.54` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `10.54` | 18,590,000.00 USD | 0.00 USD | 18,590,000.00 USD | 25,600.00 USD | 4,610.00 USD | 12,910.00 USD |
| `1D` | `10.56` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 16,190.00 USD | 5,660.00 USD | 1,810.00 USD |
| `7D` | `10.56` | 18,550,000.00 USD | 0.00 USD | 18,550,000.00 USD | 51,230.00 USD | 16,690.00 USD | 20,280.00 USD |
| `1D` | `10.58` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 3,210.00 USD | 2,820.00 USD | 8,200.00 USD |
| `7D` | `10.58` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 85,220.00 USD | 14,100.00 USD | 11,250.00 USD |
| `1D` | `10.60` | 987,290.00 USD | 0.00 USD | 987,290.00 USD | 1,040.00 USD | 5,090.00 USD | 3,180.00 USD |
| `7D` | `10.60` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 27,070.00 USD | 11,970.00 USD | 10,670.00 USD |
| `1D` | `10.62` | 977,980.00 USD | 0.00 USD | 977,980.00 USD | 41,350.00 USD | 5,560.00 USD | 12,130.00 USD |
| `7D` | `10.62` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 18,450.00 USD | 6,970.00 USD | 19,040.00 USD |
| `1D` | `10.64` | 918,930.00 USD | 0.00 USD | 918,930.00 USD | 13,350.00 USD | 20,650.00 USD | 16,540.00 USD |
| `7D` | `10.64` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 31,790.00 USD | 9,560.00 USD | 7,380.00 USD |
| `1D` | `10.66` | 868,390.00 USD | 0.00 USD | 868,390.00 USD | 17,480.00 USD | 0.00 USD | 4,680.00 USD |
| `7D` | `10.66` | 18,200,000.00 USD | 0.00 USD | 18,200,000.00 USD | 16,420.00 USD | 6,200.00 USD | 5,350.00 USD |
| `1D` | `10.68` | 846,240.00 USD | 0.00 USD | 846,240.00 USD | 17,550.00 USD | 2,850.00 USD | 1,550.00 USD |
| `7D` | `10.68` | 18,180,000.00 USD | 0.00 USD | 18,180,000.00 USD | 17,710.00 USD | 3,370.00 USD | 5,490.00 USD |
| `1D` | `10.70` | 824,290.00 USD | 0.00 USD | 824,290.00 USD | 12,300.00 USD | 2,280.00 USD | 0.00 USD |
| `7D` | `10.70` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 14,670.00 USD | 0.00 USD | 216.17 USD |
| `1D` | `10.72` | 809,700.00 USD | 0.00 USD | 809,700.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD |
| `7D` | `10.72` | 18,130,000.00 USD | 0.00 USD | 18,130,000.00 USD | 31,590.00 USD | 5,730.00 USD | 7,830.00 USD |
| `1D` | `10.74` | 791,260.00 USD | 0.00 USD | 791,260.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD |
| `7D` | `10.74` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 20,210.00 USD | 4,010.00 USD | 315.57 USD |
| `1D` | `10.76` | 714,050.00 USD | 0.00 USD | 714,050.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD |
| `7D` | `10.76` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 16,310.00 USD | 0.00 USD | 373.14 USD |
| `1D` | `10.78` | 694,950.00 USD | 0.00 USD | 694,950.00 USD | 1,070.00 USD | 2,540.00 USD | 57.12 USD |
| `7D` | `10.78` | 18,050,000.00 USD | 0.00 USD | 18,050,000.00 USD | 14,010.00 USD | 3,960.00 USD | 23,620.00 USD |
| `1D` | `10.80` | 691,270.00 USD | 0.00 USD | 691,270.00 USD | 4,360.00 USD | 0.00 USD | 123.30 USD |
| `7D` | `10.80` | 18,010,000.00 USD | 0.00 USD | 18,010,000.00 USD | 65,420.00 USD | 1,510.00 USD | 70,480.00 USD |
| `1D` | `10.82` | 686,790.00 USD | 0.00 USD | 686,790.00 USD | 2,030.00 USD | 260.12 USD | 68.68 USD |
| `7D` | `10.82` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 135,080.00 USD | 28,810.00 USD | 11,330.00 USD |
| `1D` | `10.84` | 684,430.00 USD | 0.00 USD | 684,430.00 USD | 54,340.00 USD | 776.90 USD | 31.01 USD |
| `7D` | `10.84` | 17,690,000.00 USD | 0.00 USD | 17,690,000.00 USD | 74,730.00 USD | 38,860.00 USD | 45,740.00 USD |
| `1D` | `10.86` | 629,290.00 USD | 0.00 USD | 629,290.00 USD | 976.86 USD | 30,260.00 USD | 3,820.00 USD |
| `7D` | `10.86` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 234,930.00 USD | 15,690.00 USD | 95,190.00 USD |
| `1D` | `10.88` | 594,230.00 USD | 0.00 USD | 594,230.00 USD | 1,820.00 USD | 10,400.00 USD | 23,850.00 USD |
| `7D` | `10.88` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 183,260.00 USD | 71,280.00 USD | 209,750.00 USD |
| `1D` | `10.90` | 558,160.00 USD | 0.00 USD | 558,160.00 USD | 23,940.00 USD | 3,600.00 USD | 0.39 USD |
| `7D` | `10.90` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 251,790.00 USD | 58,210.00 USD | 122,760.00 USD |
| `1D` | `10.92` | 530,620.00 USD | 0.00 USD | 530,620.00 USD | 97,980.00 USD | 28,740.00 USD | 0.60 USD |
| `7D` | `10.92` | 16,290,000.00 USD | 0.00 USD | 16,290,000.00 USD | 460,740.00 USD | 93,310.00 USD | 349,040.00 USD |
| `1D` | `10.94` | 403,900.00 USD | 0.00 USD | 403,900.00 USD | 46,920.00 USD | 17,060.00 USD | 81.93 USD |
| `7D` | `10.94` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 206,150.00 USD | 101,410.00 USD | 281,980.00 USD |
| `1D` | `10.96` | 339,830.00 USD | 0.00 USD | 339,830.00 USD | 96,940.00 USD | 23,010.00 USD | 96.96 USD |
| `7D` | `10.96` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 275,060.00 USD | 70,020.00 USD | 213,120.00 USD |
| `1D` | `10.98` | 219,790.00 USD | 0.00 USD | 219,790.00 USD | 23,750.00 USD | 2,400.00 USD | 0.00 USD |
| `7D` | `10.98` | 14,240,000.00 USD | 0.00 USD | 14,240,000.00 USD | 96,870.00 USD | 110,950.00 USD | 162,270.00 USD |
| `1D` | `11.00` | 193,630.00 USD | 0.00 USD | 193,630.00 USD | 35,500.00 USD | 12,760.00 USD | 15,190.00 USD |
| `7D` | `11.00` | 13,870,000.00 USD | 0.00 USD | 13,870,000.00 USD | 134,000.00 USD | 91,410.00 USD | 161,040.00 USD |
| `1D` | `11.02` | 130,190.00 USD | 0.00 USD | 130,190.00 USD | 0.00 USD | 23,720.00 USD | 31,870.00 USD |
| `7D` | `11.02` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 300,370.00 USD | 73,760.00 USD | 137,830.00 USD |
| `1D` | `11.04` | 74,600.00 USD | 0.00 USD | 74,600.00 USD | 0.00 USD | 0.00 USD | 23,640.00 USD |
| `7D` | `11.04` | 12,970,000.00 USD | 0.00 USD | 12,970,000.00 USD | 337,340.00 USD | 141,930.00 USD | 174,650.00 USD |
| `1D` | `11.06` | 50,950.00 USD | 0.00 USD | 50,950.00 USD | 0.00 USD | 0.00 USD | 50,950.00 USD |
| `7D` | `11.06` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 129,010.00 USD | 102,780.00 USD | 172,780.00 USD |
| `1D` | `11.07` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.08` | 29,350.00 USD | 29,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 29,350.00 USD |
| `7D` | `11.08` | 11,910,000.00 USD | 0.00 USD | 11,910,000.00 USD | 460,410.00 USD | 17,510.00 USD | 334,900.00 USD |
| `1D` | `11.10` | 118,000.00 USD | 118,000.00 USD | 0.00 USD | 0.00 USD | 24,890.00 USD | 63,760.00 USD |
| `7D` | `11.10` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 459,430.00 USD | 185,380.00 USD | 547,370.00 USD |
| `1D` | `11.12` | 234,160.00 USD | 234,160.00 USD | 0.00 USD | 632.30 USD | 39,730.00 USD | 75,790.00 USD |
| `7D` | `11.12` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 580,580.00 USD | 171,810.00 USD | 296,870.00 USD |
| `1D` | `11.14` | 490,710.00 USD | 490,710.00 USD | 0.00 USD | 1,890.00 USD | 79,990.00 USD | 174,660.00 USD |
| `7D` | `11.14` | 8,860,000.00 USD | 0.00 USD | 8,860,000.00 USD | 692,090.00 USD | 196,110.00 USD | 604,650.00 USD |
| `1D` | `11.16` | 652,000.00 USD | 652,000.00 USD | 0.00 USD | 337.20 USD | 51,930.00 USD | 109,030.00 USD |
| `7D` | `11.16` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 653,240.00 USD | 190,740.00 USD | 463,980.00 USD |
| `1D` | `11.18` | 956,110.00 USD | 956,110.00 USD | 0.00 USD | 137,030.00 USD | 49,160.00 USD | 117,920.00 USD |
| `7D` | `11.18` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 658,900.00 USD | 214,580.00 USD | 552,970.00 USD |
| `1D` | `11.20` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 222,000.00 USD | 52,080.00 USD | 98,690.00 USD |
| `7D` | `11.20` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 384,830.00 USD | 247,310.00 USD | 129,030.00 USD |
| `1D` | `11.22` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 177,480.00 USD | 43,930.00 USD | 43,170.00 USD |
| `7D` | `11.22` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 244,560.00 USD | 235,360.00 USD | 236,400.00 USD |
| `1D` | `11.24` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 56,190.00 USD | 70,490.00 USD |
| `7D` | `11.24` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 140,690.00 USD | 80,520.00 USD | 70,880.00 USD |
| `1D` | `11.26` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 41,120.00 USD | 70,350.00 USD |
| `7D` | `11.26` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 314,550.00 USD | 154,510.00 USD | 99,720.00 USD |
| `1D` | `11.28` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 38,150.00 USD | 21,180.00 USD | 117,450.00 USD |
| `7D` | `11.28` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 240,180.00 USD | 47,410.00 USD | 127,140.00 USD |
| `1D` | `11.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 59,870.00 USD | 41,980.00 USD |
| `7D` | `11.30` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 24,980.00 USD | 43,570.00 USD | 0.00 USD |
| `1D` | `11.32` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 323.10 USD | 34,100.00 USD | 0.00 USD |
| `7D` | `11.32` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 54,410.00 USD | 23,400.00 USD | 95,360.00 USD |
| `1D` | `11.34` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 197,970.00 USD | 53,750.00 USD | 0.00 USD |
| `7D` | `11.34` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 320,900.00 USD | 20,470.00 USD | 18,940.00 USD |
| `1D` | `11.36` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 83,300.00 USD | 0.00 USD |
| `7D` | `11.36` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 170,150.00 USD | 88,160.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 55,490.00 USD | 0.00 USD |
| `7D` | `11.38` | 962,530.00 USD | 0.00 USD | 962,530.00 USD | 26,250.00 USD | 22,810.00 USD | 42,320.00 USD |
| `1D` | `11.40` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD |
| `7D` | `11.40` | 871,150.00 USD | 0.00 USD | 871,150.00 USD | 150,730.00 USD | 14,250.00 USD | 28,480.00 USD |
| `1D` | `11.42` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD |
| `7D` | `11.42` | 677,690.00 USD | 0.00 USD | 677,690.00 USD | 61,980.00 USD | 0.00 USD | 78,750.00 USD |
| `1D` | `11.44` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 391.00 USD | 52,860.00 USD |
| `7D` | `11.44` | 536,960.00 USD | 0.00 USD | 536,960.00 USD | 175,790.00 USD | 58,410.00 USD | 37,930.00 USD |
| `7D` | `11.46` | 264,830.00 USD | 0.00 USD | 264,830.00 USD | 73,090.00 USD | 24,400.00 USD | 38,770.00 USD |
| `1D` | `11.48` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 4,300.00 USD | 0.00 USD |
| `7D` | `11.48` | 128,570.00 USD | 0.00 USD | 128,570.00 USD | 17,370.00 USD | 23,070.00 USD | 0.00 USD |
| `1D` | `11.50` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 19,080.00 USD | 11,880.00 USD | 0.00 USD |
| `7D` | `11.50` | 88,130.00 USD | 0.00 USD | 88,130.00 USD | 40,840.00 USD | 10,050.00 USD | 37,240.00 USD |
| `1D` | `11.52` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 29,340.00 USD | 12,870.00 USD | 0.00 USD |
| `7D` | `11.52` | 4,270.00 USD | 4,270.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `7D` | `11.52` | 8,530.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD | 4,270.00 USD | 0.00 USD |
| `7D` | `11.54` | 94,830.00 USD | 94,830.00 USD | 0.00 USD | 34,770.00 USD | 0.00 USD | 51,530.00 USD |
| `1D` | `11.56` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 64,190.00 USD | 0.00 USD | 15,160.00 USD |
| `7D` | `11.56` | 132,710.00 USD | 132,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,880.00 USD |
| `1D` | `11.58` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 45,400.00 USD | 75.80 USD | 17,790.00 USD |
| `7D` | `11.58` | 164,330.00 USD | 164,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 99,240.00 USD | 0.00 USD | 56,270.00 USD |
| `7D` | `11.60` | 187,100.00 USD | 187,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.62` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 42,200.00 USD | 0.00 USD | 33,860.00 USD |
| `7D` | `11.64` | 222,010.00 USD | 222,010.00 USD | 0.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.66` | 283,980.00 USD | 283,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 59,600.00 USD | 10,040.00 USD | 0.00 USD |
| `7D` | `11.68` | 288,630.00 USD | 288,630.00 USD | 0.00 USD | 0.00 USD | 4,650.00 USD | 0.00 USD |
| `1D` | `11.72` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD |
| `7D` | `11.72` | 484,570.00 USD | 484,570.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.74` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD |
| `1D` | `11.76` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD |
| `7D` | `11.76` | 532,760.00 USD | 532,760.00 USD | 0.00 USD | 48,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.78` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD |
| `1D` | `11.80` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 14,340.00 USD | 66.63 USD |
| `7D` | `11.80` | 672,880.00 USD | 672,880.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD |
| `7D` | `11.82` | 873,430.00 USD | 873,430.00 USD | 0.00 USD | 158,640.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD |
| `7D` | `11.84` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 39.34 USD |
| `1D` | `11.86` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD |
| `7D` | `11.86` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | 50.72 USD |
| `1D` | `11.88` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD |
| `7D` | `11.88` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 10,340.00 USD | 2,480.00 USD | 23,250.00 USD |
| `1D` | `11.90` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD |
| `7D` | `11.90` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 38,400.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.92` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD |
| `7D` | `11.92` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 80,090.00 USD | 14,370.00 USD | 38,910.00 USD |
| `1D` | `11.94` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD |
| `7D` | `11.94` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 17,060.00 USD | 24,600.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD |
| `7D` | `11.96` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 6,640.00 USD | 1,490.00 USD | 151,860.00 USD |
| `1D` | `11.98` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD |
| `7D` | `11.98` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 391,180.00 USD | 34,700.00 USD | 190,600.00 USD |
| `1D` | `12.00` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD |
| `7D` | `12.00` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 304,560.00 USD | 7,460.00 USD | 183,590.00 USD |
| `1D` | `12.02` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD |
| `7D` | `12.02` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 244,440.00 USD | 47,410.00 USD | 222,360.00 USD |
| `1D` | `12.04` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 209,440.00 USD | 71,010.00 USD | 97,900.00 USD |
| `7D` | `12.04` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 292,690.00 USD | 137,340.00 USD | 179,840.00 USD |
| `1D` | `12.06` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 187,660.00 USD | 88,160.00 USD | 165,780.00 USD |
| `7D` | `12.06` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 234,210.00 USD | 121,530.00 USD | 145,690.00 USD |
| `1D` | `12.08` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD |
| `7D` | `12.08` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 375,670.00 USD | 106,090.00 USD | 165,170.00 USD |
| `1D` | `12.10` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 19,140.00 USD | 9,690.00 USD | 22,460.00 USD |
| `7D` | `12.10` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 32,390.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 124,790.00 USD | 54,500.00 USD | 63,050.00 USD |
| `7D` | `12.12` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 174,090.00 USD | 67,240.00 USD | 130,690.00 USD |
| `1D` | `12.14` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 92,340.00 USD | 33,040.00 USD | 55,720.00 USD |
| `7D` | `12.14` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 132,510.00 USD | 72,070.00 USD | 93,440.00 USD |
| `1D` | `12.16` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 126,410.00 USD | 37,730.00 USD | 59,290.00 USD |
| `7D` | `12.16` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 220,120.00 USD | 93,690.00 USD | 91,410.00 USD |
| `1D` | `12.18` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 112,590.00 USD | 42,150.00 USD | 33,450.00 USD |
| `7D` | `12.18` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 57,680.00 USD | 42,810.00 USD | 32,160.00 USD |
| `1D` | `12.20` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 77,890.00 USD | 37,080.00 USD | 20,010.00 USD |
| `7D` | `12.20` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 194,760.00 USD | 51,340.00 USD | 78,200.00 USD |
| `1D` | `12.22` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 12,890.00 USD | 16,530.00 USD | 28,210.00 USD |
| `7D` | `12.22` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 261,490.00 USD | 56,190.00 USD | 93,540.00 USD |
| `1D` | `12.24` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.24` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 70,650.00 USD | 53,910.00 USD | 115,100.00 USD |
| `1D` | `12.26` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 43,220.00 USD | 24,590.00 USD | 21,450.00 USD |
| `7D` | `12.26` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 190,490.00 USD | 55,780.00 USD | 50,600.00 USD |
| `1D` | `12.28` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 73,710.00 USD | 17,410.00 USD | 37,620.00 USD |
| `7D` | `12.28` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 215,790.00 USD | 76,160.00 USD | 170,610.00 USD |
| `1D` | `12.30` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 57,170.00 USD | 16,300.00 USD | 45,470.00 USD |
| `7D` | `12.30` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 178,010.00 USD | 66,120.00 USD | 96,720.00 USD |
| `1D` | `12.32` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.32` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 98,550.00 USD | 46,590.00 USD | 18,040.00 USD |
| `1D` | `12.34` | 7,580,000.00 USD | 7,580,000.00 USD | 0.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD |
| `7D` | `12.34` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 145,370.00 USD | 81,530.00 USD | 13,590.00 USD |
| `1D` | `12.36` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 19,360.00 USD | 9,040.00 USD | 5,460.00 USD |
| `7D` | `12.36` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 97,320.00 USD | 30,690.00 USD | 18,470.00 USD |
| `1D` | `12.38` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD |
| `7D` | `12.38` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 7,170.00 USD | 7,370.00 USD | 166,430.00 USD |
| `1D` | `12.40` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 18,820.00 USD | 12,140.00 USD | 22,980.00 USD |
| `7D` | `12.40` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 196,150.00 USD | 41,260.00 USD | 258,110.00 USD |
| `1D` | `12.42` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 57,850.00 USD | 13,980.00 USD | 9,730.00 USD |
| `7D` | `12.42` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 135,510.00 USD | 36,390.00 USD | 408,100.00 USD |
| `1D` | `12.44` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.44` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 162,080.00 USD | 68,340.00 USD | 248,330.00 USD |
| `1D` | `12.46` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 411.51 USD | 9,440.00 USD | 4,210.00 USD |
| `7D` | `12.46` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 84,310.00 USD | 78,070.00 USD | 86,160.00 USD |
| `1D` | `12.48` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD |
| `7D` | `12.48` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 31,320.00 USD | 18,070.00 USD | 180,400.00 USD |
| `1D` | `12.50` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD |
| `7D` | `12.50` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 147,340.00 USD | 20,260.00 USD | 74,690.00 USD |
| `1D` | `12.52` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD |
| `7D` | `12.52` | 11,800,000.00 USD | 11,800,000.00 USD | 0.00 USD | 154,680.00 USD | 45,040.00 USD | 125,100.00 USD |
| `1D` | `12.54` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `12.54` | 12,060,000.00 USD | 12,060,000.00 USD | 0.00 USD | 96,800.00 USD | 53,300.00 USD | 107,050.00 USD |
| `1D` | `12.56` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.56` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 117,030.00 USD | 30,820.00 USD | 27,570.00 USD |
| `1D` | `12.58` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD |
| `7D` | `12.58` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 90,950.00 USD | 66,210.00 USD | 41,290.00 USD |
| `1D` | `12.60` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 15,910.00 USD | 3,320.00 USD | 1,180.00 USD |
| `7D` | `12.60` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 56,420.00 USD | 26,450.00 USD | 38,800.00 USD |
| `1D` | `12.62` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 13,610.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.62` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 35,120.00 USD | 13,140.00 USD | 20,250.00 USD |
| `1D` | `12.64` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `12.64` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 94,550.00 USD | 42,650.00 USD | 163,370.00 USD |
| `1D` | `12.66` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 4,580.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `12.66` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 43,290.00 USD | 9,020.00 USD | 99,050.00 USD |
| `1D` | `12.68` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `12.68` | 13,370,000.00 USD | 13,370,000.00 USD | 0.00 USD | 88,690.00 USD | 22,310.00 USD | 185,520.00 USD |
| `1D` | `12.70` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD |
| `7D` | `12.70` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 22,060.00 USD | 50,120.00 USD | 142,700.00 USD |
| `1D` | `12.72` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD |
| `7D` | `12.72` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 58,240.00 USD | 26,460.00 USD | 99,280.00 USD |
| `1D` | `12.74` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD |
| `7D` | `12.74` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 38,570.00 USD | 18,330.00 USD | 20,910.00 USD |
| `1D` | `12.76` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `12.76` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 15,760.00 USD | 14,350.00 USD | 29,680.00 USD |
| `1D` | `12.78` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.78` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 77,730.00 USD | 15,750.00 USD | 18,630.00 USD |
| `1D` | `12.80` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD |
| `7D` | `12.80` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 15,850.00 USD | 14,000.00 USD | 26,430.00 USD |
| `1D` | `12.82` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD |
| `7D` | `12.82` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 14,750.00 USD | 132.05 USD | 5,000.00 USD |
| `1D` | `12.84` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD |
| `7D` | `12.84` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 29,710.00 USD | 15,990.00 USD | 7,710.00 USD |
| `1D` | `12.86` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD |
| `7D` | `12.86` | 14,220,000.00 USD | 14,220,000.00 USD | 0.00 USD | 29,590.00 USD | 8,750.00 USD | 27,120.00 USD |
| `1D` | `12.88` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `12.88` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 24,250.00 USD | 4,610.00 USD | 12,750.00 USD |
| `1D` | `12.90` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD |
| `7D` | `12.90` | 14,340,000.00 USD | 14,340,000.00 USD | 0.00 USD | 41,610.00 USD | 16,690.00 USD | 20,230.00 USD |
| `1D` | `12.92` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD |
| `7D` | `12.92` | 14,410,000.00 USD | 14,410,000.00 USD | 0.00 USD | 50,620.00 USD | 13,030.00 USD | 11,050.00 USD |
| `1D` | `12.94` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.94` | 14,440,000.00 USD | 14,440,000.00 USD | 0.00 USD | 27,900.00 USD | 1,070.00 USD | 96.13 USD |
| `1D` | `12.96` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD |
| `7D` | `12.96` | 14,480,000.00 USD | 14,480,000.00 USD | 0.00 USD | 14,650.00 USD | 11,970.00 USD | 10,660.00 USD |
| `1D` | `12.98` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD |
| `7D` | `12.98` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 13,860.00 USD | 6,970.00 USD | 18,880.00 USD |
| `1D` | `13.00` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 11,890.00 USD | 7,680.00 USD | 16,490.00 USD |
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
  * Total Open Interest: `518.38M` | Total OI Tokens: `47,412,953.1 LINK`
  * 1h OI Change: `-7.03%` | 4h OI Change: `-8.67%` | 24h OI Change: `-9.15%`
  * Exchange Breakdown: Binance=`98.64M` | Bybit=`61.78M` | OKX=`24.97M` | Hyperliquid=`52.19M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.42K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0053%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0024%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0053%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0006%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `43.72%` | `56.28%` | `0.78` | 8,470,000.00 USD |
| `15M` | `Binance` | `42.34%` | `57.66%` | `0.73` | 3,490,000.00 USD |
| `15M` | `OKX` | `49.03%` | `50.97%` | `0.96` | 677,450.00 USD |
| `15M` | `Bybit` | `40.42%` | `59.58%` | `0.68` | 914,470.00 USD |
| `15M` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 55,690.00 USD |
| `15M` | `Gate` | `30.71%` | `69.29%` | `0.44` | 977,570.00 USD |
| `15M` | `Bitget` | `46.29%` | `53.71%` | `0.86` | 126,050.00 USD |
| `15M` | `BingX` | `41.31%` | `58.69%` | `0.70` | 55,010.00 USD |
| `15M` | `MEXC` | `48.52%` | `51.48%` | `0.94` | 75,760.00 USD |
| `15M` | `Bitunix` | `39.75%` | `60.25%` | `0.66` | 113,440.00 USD |
| `15M` | `Hyperliquid` | `28.55%` | `71.45%` | `0.40` | 910,130.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `66.35%` | `33.65%` | `1.97` | 822,820.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `9.87%` | `90.13%` | `0.11` | 196,890.00 USD |
| `15M` | `HTX` | `40.79%` | `59.21%` | `0.69` | 25,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `57.26%` | `42.74%` | `1.34` | 12,210.00 USD |
| `15M` | `Aster` | `30.6%` | `69.4%` | `0.44` | 14,120.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.82%` | `56.18%` | `0.78` | 1,390.00 USD |
| `15M` | `Whale Positions` | `42.34%` | `57.66%` | `0.73` | 3,490,000.00 USD |
| `15M` | `Global Accounts` | `43.72%` | `56.28%` | `0.78` | 8,470,000.00 USD |
| `1H` | `LINK` | `43.63%` | `56.37%` | `0.77` | 11,670,000.00 USD |
| `1H` | `Binance` | `43.92%` | `56.08%` | `0.78` | 4,530,000.00 USD |
| `1H` | `OKX` | `44.42%` | `55.58%` | `0.80` | 925,900.00 USD |
| `1H` | `Bybit` | `43.65%` | `56.35%` | `0.77` | 1,090,000.00 USD |
| `1H` | `KuCoin` | `48.34%` | `51.66%` | `0.94` | 93,480.00 USD |
| `1H` | `Gate` | `39.79%` | `60.21%` | `0.66` | 1,480,000.00 USD |
| `1H` | `Bitget` | `43.04%` | `56.96%` | `0.76` | 156,020.00 USD |
| `1H` | `BingX` | `37.61%` | `62.39%` | `0.60` | 224,870.00 USD |
| `1H` | `MEXC` | `49.15%` | `50.85%` | `0.97` | 80,250.00 USD |
| `1H` | `Bitunix` | `42.27%` | `57.73%` | `0.73` | 150,200.00 USD |
| `1H` | `Hyperliquid` | `23.82%` | `76.18%` | `0.31` | 882,590.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.02%` | `50.98%` | `0.96` | 1,300,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `13.22%` | `86.78%` | `0.15` | 627,080.00 USD |
| `1H` | `HTX` | `40.59%` | `59.41%` | `0.68` | 68,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43%` | `57%` | `0.75` | 26,240.00 USD |
| `1H` | `Aster` | `12.57%` | `87.43%` | `0.14` | 14,840.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `33.28%` | `66.72%` | `0.50` | 20,840.00 USD |
| `1H` | `Whale Positions` | `43.92%` | `56.08%` | `0.78` | 4,530,000.00 USD |
| `1H` | `Global Accounts` | `43.63%` | `56.37%` | `0.77` | 11,670,000.00 USD |
| `4H` | `LINK` | `44.39%` | `55.61%` | `0.80` | 163,070,000.00 USD |
| `4H` | `Binance` | `44.3%` | `55.7%` | `0.80` | 50,730,000.00 USD |
| `4H` | `OKX` | `45.42%` | `54.58%` | `0.83` | 18,170,000.00 USD |
| `4H` | `Bybit` | `43.78%` | `56.22%` | `0.78` | 15,850,000.00 USD |
| `4H` | `KuCoin` | `48.6%` | `51.4%` | `0.95` | 1,230,000.00 USD |
| `4H` | `Gate` | `42.59%` | `57.41%` | `0.74` | 1,810,000.00 USD |
| `4H` | `Bitget` | `44.11%` | `55.89%` | `0.79` | 6,830,000.00 USD |
| `4H` | `BingX` | `41.7%` | `58.3%` | `0.72` | 5,180,000.00 USD |
| `4H` | `MEXC` | `49.08%` | `50.92%` | `0.96` | 43,640,000.00 USD |
| `4H` | `Bitunix` | `43.84%` | `56.16%` | `0.78` | 6,480,000.00 USD |
| `4H` | `Hyperliquid` | `26.12%` | `73.88%` | `0.35` | 3,860,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.98%` | `50.02%` | `1.00` | 3,880,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `9.19%` | `90.81%` | `0.10` | 3,540,000.00 USD |
| `4H` | `HTX` | `50.74%` | `49.26%` | `1.03` | 105,190.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.45%` | `56.55%` | `0.77` | 891,000.00 USD |
| `4H` | `Aster` | `13.32%` | `86.68%` | `0.15` | 572,020.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.87%` | `58.13%` | `0.72` | 296,490.00 USD |
| `4H` | `Whale Positions` | `44.3%` | `55.7%` | `0.80` | 50,730,000.00 USD |
| `4H` | `Global Accounts` | `44.39%` | `55.61%` | `0.80` | 163,070,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.71` | `11.62` | 2,420,411.57 USD | 1,104,115.69 USD | 1,316,295.88 USD | -212,180.19 USD | `-8.77%` | `11B / 14S` |
| `5:00 UTC` | `11.70` | `11.69` | `11.70` | `11.71` | `11.64` | 1,180,195.23 USD | 935,197.64 USD | 244,997.59 USD | 690,200.05 USD | `+58.48%` | `35B / 7S` |
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.68` | `11.66` | `11.68` | `11.68` | `11.63` | 997,243.09 USD | 360,139.33 USD | 637,103.76 USD | -276,964.43 USD | `-27.77%` | `11B / 15S` |
| `0:00 UTC` | `11.72` | `11.71` | `11.72` | `11.73` | `11.68` | 1,229,457.09 USD | 722,946.86 USD | 506,510.23 USD | 216,436.63 USD | `+17.60%` | `13B / 6S` |
| `5:00 UTC` | `11.70` | `11.70` | `11.70` | `11.72` | `11.68` | 638,959.31 USD | 356,011.33 USD | 282,947.98 USD | 73,063.35 USD | `+11.43%` | `5B / 5S` |
| `0:00 UTC` | `11.53` | `11.52` | `11.53` | `11.69` | `11.42` | 7,042,914.29 USD | 3,385,099.97 USD | 3,657,814.32 USD | -272,714.35 USD | `-3.87%` | `7B / 36S` |
| `5:00 UTC` | `11.53` | `11.53` | `11.53` | `11.57` | `11.50` | 1,919,098.80 USD | 908,695.92 USD | 1,010,402.88 USD | -101,706.95 USD | `-5.30%` | `5B / 9S` |
| `0:00 UTC` | `11.13` | `11.25` | `11.13` | `11.55` | `11.03` | 15,867,227.37 USD | 6,488,166.63 USD | 9,379,060.74 USD | -2,890,894.11 USD | `-18.22%` | `4B / 29S` |
| `5:00 UTC` | `11.00` | `11.02` | `11.00` | `11.19` | `10.87` | 12,670,548.65 USD | 5,845,200.77 USD | 6,825,347.88 USD | -980,147.12 USD | `-7.74%` | `14B / 17S` |

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
| `5m` | -1,360,000.00 USD | -2,740,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,690,000.00 USD | -4,010,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,600,000.00 USD | -3,870,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,510,000.00 USD | -5,270,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,020,000.00 USD | -4,070,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,050,000.00 USD | -6,600,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -170,810.00 USD | -6,430,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,940,000.00 USD | -5,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,020,000.00 USD | -5,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,210,000.00 USD | -10,390,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -10,680,000.00 USD | -28,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -71,080,000.00 USD | -192,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.36M` | 15m=`-1.69M` | 1h=`-1.51M` | 24h=`-2.21M`
* Futures Capital Netflows: 5m=`-2.74M` | 15m=`-4.01M` | 1h=`-5.27M` | 24h=`-10.39M`
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
  * Execution Entry: `11.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.06` (Risk Distance: `1.36` pts)
  * +2.5R Take Profit: `14.84`
  * Mathematical Lot Sizing: **`7.32 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.89` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `13.25` (Risk Distance: `1.36` pts)
  * +2.5R Take Profit: `8.47`
  * Mathematical Lot Sizing: **`7.32 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
