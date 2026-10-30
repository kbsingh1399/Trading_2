# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 07:51:26 IST` (`2026-10-30 02:21:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1700` | **Live Ask Quote**: `0.1700` | **Mid Price**: `0.1700`
- **Spread Points**: `0.000034` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
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
  * Session VWAP: `0.1700` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1712` | Lower -3.00σ Band: `0.1688`
  * Upper +2.51σ Band: `0.1710` | Lower -2.51σ Band: `0.1691`
  * Upper +2.01σ Band: `0.1707` | Lower -2.01σ Band: `0.1693`
  * Upper +2.00σ Band: `0.1707` | Lower -2.00σ Band: `0.1693`
  * Upper +1.28σ Band: `0.1705` | Lower -1.28σ Band: `0.1695`
  * Upper +1.00σ Band: `0.1704` | Lower -1.00σ Band: `0.1697`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1700` | EMA-20=`0.1700` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1700` (Slope: `+0.0000`) | EMA-100=`0.1700`
  * Institutional Anchors: EMA-144=`0.1700` | EMA-200=`0.1700` (Slope: `+0.0000`) | EMA-233=`0.1700`
- **Range Boundaries**: 24H High=`0.1717` | 24H Low=`0.1683` | Weekly High=`0.1734` | Weekly Low=`0.1666`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1705` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.1700` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.1695` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1707` | POC=`0.1700` | VAL=`0.1693`
  * Prior Day Extremes: PDH=`0.1710` | PDL=`0.1690` | PDC=`0.1700`
  * Monday Range Blueprint: High=`0.1709` | Mid=`0.1700` | Low=`0.1692`
  * Developing Weekly Value Area: Weekly VAH=`0.1714` | Weekly POC=`0.1700` | Weekly VAL=`0.1687`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1704` | Low=`0.1697`
  * London Session (08:00-16:00 UTC): High=`0.1707` | Low=`0.1693`
  * New York Session (13:00-21:00 UTC): High=`0.1710` | Low=`0.1690`
  * Initial Balance (First Hour): IB High=`0.1705` | IB Low=`0.1695`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1693` - `0.1707`
  * Optimal Trade Entry (OTE 0.705): `0.1704`
  * Structural Invalidation Anchor (0.786): `0.1714`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1533` | `0.1537` | `0.1526` | `0.1526` | `2,553,540` | 391,082.19 USD | -126,368.54 USD | `-32.31%` | -7,807,622.36 USD | `-0.92` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1526` | `0.1540` | `0.1526` | `0.1537` | `3,128,140` | 479,862.26 USD | 99,968.93 USD | `+20.83%` | -7,707,653.43 USD | `+0.79` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1537` | `0.1546` | `0.1537` | `0.1542` | `1,386,514` | 213,901.40 USD | -5,168.65 USD | `-2.42%` | -7,712,822.08 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1534` | `0.1545` | `0.1520` | `0.1535` | `9,432,942` | 1,447,365.29 USD | -163,522.47 USD | `-11.30%` | -7,669,280.79 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1535` | `0.1537` | `0.1524` | `0.1533` | `4,985,990` | 762,631.88 USD | -11,973.03 USD | `-1.57%` | -7,681,253.82 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1533` | `0.1546` | `0.1526` | `0.1542` | `7,068,193` | 1,084,845.85 USD | -31,568.26 USD | `-2.91%` | -7,712,822.08 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1542` | `0.1555` | `0.1471` | `0.1555` | `122,723,994` | 18,580,533.07 USD | -801,003.43 USD | `-4.31%` | -7,539,685.14 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1555` | `0.1558` | `0.1520` | `0.1533` | `31,981,907` | 4,912,629.10 USD | -386,533.95 USD | `-7.87%` | -7,926,219.09 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1533` | `0.1546` | `0.1526` | `0.1542` | `7,068,193` | 1,084,845.85 USD | -31,568.26 USD | `-2.91%` | -7,957,787.35 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1558` | `0.1471` | `0.1542` | `161,774,095` | 24,578,008.03 USD | -1,219,105.64 USD | `-4.96%` | -8,719,239.69 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,340,323.74 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,578,452.08 USD | `-1.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1558` | `0.1471` | `0.1542` | `161,774,095` | 24,578,008.03 USD | -1,219,105.64 USD | `-4.96%` | -8,719,239.69 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.1700`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:43:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1775` | 9,056.78 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 9.06K USD at 0.1775 USD [API] | `2026-10-28 20:06:33` |
| `ANNOUNCEMENT` | `INFO` | `0.1776` | 5,518.78 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 5.52K USD at 0.1776 USD [API] | `2026-10-28 21:22:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1629` (Vol: 153,600.00 USD, Dist: `+4.92%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--2.69%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 7D Horizon: Short MP=`0.1791` (Vol: 196,100.00 USD, Dist: `+15.75%`) | Long MP=`0.1511` (Vol: 221,900.00 USD, Dist: `--2.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0355` | 4,280.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 3,760.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 278.62 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 529.67 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 1,430.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 195,160.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 203.46 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 719.53 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 1,120.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 6,150.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,170.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 595.64 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 4,300.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 5,390.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 4,820.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,420.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 15,140.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 8,340.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,940.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 112.78 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 883.64 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 1,990.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 73,680.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 514.04 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,220.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,760.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 9,310.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 7,670.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 3,260.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 14,220.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,580.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,230.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 14,270.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 4,210.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 8,870.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 10,940.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 9,570.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 3,660.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 1,300.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 2,560.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 471.49 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 6,120.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 150,220.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 3,500.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 897.50 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 17,890.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 34,560.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 7,500.00 USD | 967,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 5,130.00 USD | 960,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 15,110.00 USD | 955,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 11,500.00 USD | 940,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 6,290.00 USD | 928,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 18,440.00 USD | 922,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,380.00 USD | 903,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 18,060.00 USD | 899,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 54,720.00 USD | 881,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,280,000.00 USD | 3,280,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,250,000.00 USD | 3,250,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 3,200,000.00 USD | 3,200,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 583.12 USD | 826,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1348` | 3,170,000.00 USD | 3,170,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 3,110,000.00 USD | 3,110,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 12,930.00 USD | 826,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 3,070,000.00 USD | 3,070,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 3,030,000.00 USD | 3,030,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,990,000.00 USD | 2,990,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 1,690.00 USD | 813,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,970,000.00 USD | 2,970,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1370` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,950,000.00 USD | 2,950,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1373` | 2,710,000.00 USD | 2,710,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 14,170.00 USD | 811,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1376` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1379` | 2,700,000.00 USD | 2,700,000.00 USD | 2,250.00 USD | 821.64 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,950,000.00 USD | 2,950,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1382` | 2,690,000.00 USD | 2,690,000.00 USD | 10,310.00 USD | 9,440.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,930,000.00 USD | 2,930,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1385` | 2,640,000.00 USD | 2,640,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,030.00 USD | 797,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1388` | 2,560,000.00 USD | 2,560,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,890,000.00 USD | 2,890,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 2,540,000.00 USD | 2,540,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 29,080.00 USD | 793,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1397` | 2,450,000.00 USD | 2,450,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,780,000.00 USD | 2,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,760,000.00 USD | 2,760,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 1,610.00 USD | 764,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1412` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 26,150.00 USD | 762,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 2,430,000.00 USD | 2,430,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 484,730.00 USD | 736,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 2,420,000.00 USD | 2,420,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,500.00 USD | 251,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,730,000.00 USD | 2,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 2,390,000.00 USD | 2,390,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,690,000.00 USD | 2,690,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,670,000.00 USD | 2,670,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 36,910.00 USD | 232,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1451` | 2,370,000.00 USD | 2,370,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 85,060.00 USD | 195,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 27,920.00 USD | 110,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,630,000.00 USD | 2,630,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 2,360,000.00 USD | 2,360,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 2,340,000.00 USD | 2,340,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,610,000.00 USD | 2,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 2,250,000.00 USD | 2,250,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 80,080.00 USD | 82,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,580,000.00 USD | 2,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1478` | 2,210,000.00 USD | 2,210,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 2,410,000.00 USD | 2,410,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 1,930,000.00 USD | 1,930,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 1,850,000.00 USD | 1,850,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 2,240,000.00 USD | 2,240,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 1,610,000.00 USD | 1,610,000.00 USD | 8,170.00 USD | 4,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,970,000.00 USD | 1,970,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 1,590,000.00 USD | 1,590,000.00 USD | 38,650.00 USD | 9,450.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,860,000.00 USD | 1,860,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 1,540,000.00 USD | 1,540,000.00 USD | 14,230.00 USD | 3,520.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1496` | 1,510,000.00 USD | 1,510,000.00 USD | 14,390.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,710,000.00 USD | 1,710,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 1,490,000.00 USD | 1,490,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,640,000.00 USD | 1,640,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1502` | 1,480,000.00 USD | 1,480,000.00 USD | 3,610.00 USD | 13,270.00 USD | 130,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 1,550,000.00 USD | 1,550,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 1,340,000.00 USD | 1,340,000.00 USD | 54,760.00 USD | 23,120.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1508` | 1,250,000.00 USD | 1,250,000.00 USD | 200,020.00 USD | 16,950.00 USD | 259,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 1,460,000.00 USD | 1,460,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 774,760.00 USD | 774,760.00 USD | 122,160.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 988,210.00 USD | 988,210.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 645,740.00 USD | 645,740.00 USD | 25,970.00 USD | 1,730.00 USD | 232,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 828,660.00 USD | 828,660.00 USD | 48,970.00 USD | 13,330.00 USD | 377,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1517` | 385,160.00 USD | 385,160.00 USD | 87,420.00 USD | 7,460.00 USD | 141,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 148,550.00 USD | 148,550.00 USD | 44,180.00 USD | 4,100.00 USD | 22,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 389,140.00 USD | 389,140.00 USD | 47,340.00 USD | 22,090.00 USD | 201,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 78,010.00 USD | 78,010.00 USD | 41,110.00 USD | 6,450.00 USD | 5,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 118,540.00 USD | 118,540.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 96,270.00 USD | 96,270.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 62,330.00 USD | 62,330.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 25,060.00 USD | 25,060.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 45,070.00 USD | 45,070.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 36,500.00 USD | 36,500.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 18,270.00 USD | 18,270.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 16,080.00 USD | 16,080.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 14,680.00 USD | 14,680.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 2,560.00 USD | 2,560.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 11,820.00 USD | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1555` | 2,430.00 USD | 2,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1560` | 10,990.00 USD | 10,990.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1562` | 4,970.00 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1564` | 44,740.00 USD | 44,740.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1565` | 312,110.00 USD | 312,110.00 USD | 41,260.00 USD | 13,270.00 USD | 252,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1568` | 599,940.00 USD | 599,940.00 USD | 33,360.00 USD | 38,630.00 USD | 215,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1568` | 323,420.00 USD | 323,420.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1571` | 706,210.00 USD | 706,210.00 USD | 40,700.00 USD | 6,150.00 USD | 59,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1572` | 657,220.00 USD | 657,220.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1574` | 732,180.00 USD | 732,180.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1576` | 1,140,000.00 USD | 1,140,000.00 USD | 44,680.00 USD | 123,840.00 USD | 315,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1577` | 1,150,000.00 USD | 1,150,000.00 USD | 69,720.00 USD | 0.00 USD | 351,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1580` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 7,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 1,470,000.00 USD | 1,470,000.00 USD | 226,250.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1583` | 1,230,000.00 USD | 1,230,000.00 USD | 69,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 1,710,000.00 USD | 1,710,000.00 USD | 80,450.00 USD | 43,370.00 USD | 114,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1586` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 20,750.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 1,820,000.00 USD | 1,820,000.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1589` | 1,320,000.00 USD | 1,320,000.00 USD | 15,100.00 USD | 19,490.00 USD | 13,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1592` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 20,480.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1595` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1598` | 1,510,000.00 USD | 1,510,000.00 USD | 16,680.00 USD | 0.00 USD | 99,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1601` | 1,530,000.00 USD | 1,530,000.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1604` | 1,630,000.00 USD | 1,630,000.00 USD | 99,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 2,690,000.00 USD | 2,690,000.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1605` | 3,070.00 USD | 5,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,470,000.00 USD | 3,470,000.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,440,000.00 USD | 4,440,000.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 37,090.00 USD | 11,530.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1615` | 4,130.00 USD | 9,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1616` | 2,070,000.00 USD | 2,070,000.00 USD | 17,630.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 5,030,000.00 USD | 5,030,000.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 2,200,000.00 USD | 2,200,000.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1622` | 2,330,000.00 USD | 2,330,000.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 2,440,000.00 USD | 2,440,000.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 887.09 USD | 10,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1628` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,600,000.00 USD | 5,600,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1631` | 2,650,000.00 USD | 2,650,000.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 2,680,000.00 USD | 2,680,000.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 3,300.00 USD | 13,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 13,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1646` | 2,800,000.00 USD | 2,800,000.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,860,000.00 USD | 5,860,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 6,110,000.00 USD | 6,110,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 6,300,000.00 USD | 6,300,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 6,490,000.00 USD | 6,490,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 3,240,000.00 USD | 3,240,000.00 USD | 66,630.00 USD | 2,010.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1676` | 3,260,000.00 USD | 3,260,000.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 6,720,000.00 USD | 6,720,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 3,270,000.00 USD | 3,270,000.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,940,000.00 USD | 6,940,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1682` | 3,450,000.00 USD | 3,450,000.00 USD | 154,780.00 USD | 4,560.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 7,010,000.00 USD | 7,010,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 3,510,000.00 USD | 3,510,000.00 USD | 20,370.00 USD | 29,790.00 USD | 13,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1685` | 2,400.00 USD | 16,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1688` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 2,650.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 3,760,000.00 USD | 3,760,000.00 USD | 75,680.00 USD | 76,030.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 7,200,000.00 USD | 7,200,000.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 3,830,000.00 USD | 3,830,000.00 USD | 34,000.00 USD | 22,300.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 7,350,000.00 USD | 7,350,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 3,910,000.00 USD | 3,910,000.00 USD | 36,180.00 USD | 38,310.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1700` | 3,990,000.00 USD | 3,990,000.00 USD | 13,350.00 USD | 21,160.00 USD | 46,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 4,050,000.00 USD | 4,050,000.00 USD | 9,960.00 USD | 14,420.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 7,560,000.00 USD | 7,560,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1706` | 4,110,000.00 USD | 4,110,000.00 USD | 38,860.00 USD | 9,590.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 25,490.00 USD | 87,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 4,200,000.00 USD | 4,200,000.00 USD | 21,630.00 USD | 62,270.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 15,040.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 4,270,000.00 USD | 4,270,000.00 USD | 9,570.00 USD | 27,880.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 17,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 4,300,000.00 USD | 4,300,000.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 8,220,000.00 USD | 8,220,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 797.95 USD | 18,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1727` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1730` | 4,550,000.00 USD | 4,550,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 8,710,000.00 USD | 8,710,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 4,570,000.00 USD | 4,570,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1736` | 4,590,000.00 USD | 4,590,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 4,660,000.00 USD | 4,660,000.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1748` | 4,750,000.00 USD | 4,750,000.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 8,890,000.00 USD | 8,890,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 4,810,000.00 USD | 4,810,000.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 4,890,000.00 USD | 4,890,000.00 USD | 32,060.00 USD | 8,430.00 USD | 42,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 9,480,000.00 USD | 9,480,000.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 5,000,000.00 USD | 5,000,000.00 USD | 15,820.00 USD | 22,420.00 USD | 70,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 5,200,000.00 USD | 5,200,000.00 USD | 94,020.00 USD | 79,990.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 9,850,000.00 USD | 9,850,000.00 USD | 268,160.00 USD | 63,870.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 5,330,000.00 USD | 5,330,000.00 USD | 50,470.00 USD | 16,490.00 USD | 68,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 10,480,000.00 USD | 10,480,000.00 USD | 338,490.00 USD | 252,140.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1766` | 5,430,000.00 USD | 5,430,000.00 USD | 15,830.00 USD | 20,220.00 USD | 62,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 10,850,000.00 USD | 10,850,000.00 USD | 191,690.00 USD | 147,360.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 5,600,000.00 USD | 5,600,000.00 USD | 40,920.00 USD | 78,870.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 5,620,000.00 USD | 5,620,000.00 USD | 22,380.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 11,120,000.00 USD | 11,120,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 11,370,000.00 USD | 11,370,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,620,000.00 USD | 11,620,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,850,000.00 USD | 11,850,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1788` | 12,020,000.00 USD | 12,020,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 12,250,000.00 USD | 12,250,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 3,590.00 USD | 22,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1796` | 12,340,000.00 USD | 12,340,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 12,460,000.00 USD | 12,460,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 12,550,000.00 USD | 12,550,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 12,730,000.00 USD | 12,730,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 12,870,000.00 USD | 12,870,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1816` | 13,020,000.00 USD | 13,020,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 13,180,000.00 USD | 13,180,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 13,390,000.00 USD | 13,390,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 13,570,000.00 USD | 13,570,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 13,780,000.00 USD | 13,780,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 14,120,000.00 USD | 14,120,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 14,460,000.00 USD | 14,460,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 14,680,000.00 USD | 14,680,000.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 14,820,000.00 USD | 14,820,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 15,270,000.00 USD | 15,270,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 15,510,000.00 USD | 15,510,000.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 15,750,000.00 USD | 15,750,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 15,910,000.00 USD | 15,910,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 16,140,000.00 USD | 16,140,000.00 USD | 133,990.00 USD | 38,100.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 16,410,000.00 USD | 16,410,000.00 USD | 138,560.00 USD | 67,770.00 USD | 68,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 591.24 USD | 22,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 16,540,000.00 USD | 16,540,000.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 16,650,000.00 USD | 16,650,000.00 USD | 57,250.00 USD | 22,460.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 16,710,000.00 USD | 16,710,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 16,830,000.00 USD | 16,830,000.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 16,920,000.00 USD | 16,920,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1896` | 16,990,000.00 USD | 16,990,000.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 17,080,000.00 USD | 17,080,000.00 USD | 14,330.00 USD | 10,990.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 17,100,000.00 USD | 17,100,000.00 USD | 8,720.00 USD | 5,070.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 17,140,000.00 USD | 17,140,000.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,170,000.00 USD | 17,170,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1925` | 2,820.00 USD | 25,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,190,000.00 USD | 17,190,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,190,000.00 USD | 17,190,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 26,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,210,000.00 USD | 17,210,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,220,000.00 USD | 17,220,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,240,000.00 USD | 17,240,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 501.79 USD | 26,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 38,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 38,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 38,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2115` | 190.90 USD | 39,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 54,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 96,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 26,090.00 USD | 122,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 209,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 210,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 210,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 24,910.00 USD | 235,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 241,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 257,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 257,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 258,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 259,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 50,500.00 USD | 309,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 310,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 313,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 342,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 395,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 395,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2635` | 201.21 USD | 395,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 396,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 409,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 409,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 437,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 438,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2815` | 310,210.00 USD | 748,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2855` | 224.40 USD | 748,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 748,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 464.84 USD | 749,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 264.59 USD | 749,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 234.62 USD | 749,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 2,330.00 USD | 752,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 758,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 758,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 770,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0355` | 1,890,000.00 USD | 0.00 USD | 4,450.00 USD | `-76.85%` | `125,379,600,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,890,000.00 USD | 0.00 USD | 1,670.00 USD | `-74.90%` | `43,323,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,890,000.00 USD | 0.00 USD | 736.09 USD | `-72.94%` | `17,737,100,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,880,000.00 USD | 0.00 USD | 170.00 USD | `-72.29%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0455` | 1,880,000.00 USD | 0.00 USD | 116.29 USD | `-70.33%` | `2,555,800,000,000.00` |
| `Live` | `Long` | `0.0465` | 1,880,000.00 USD | 0.00 USD | 1,240.00 USD | `-69.68%` | `26,643,700,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,880,000.00 USD | 0.00 USD | 4,270.00 USD | `-68.38%` | `87,976,200,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,880,000.00 USD | 0.00 USD | 109.52 USD | `-67.73%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,880,000.00 USD | 0.00 USD | 289.43 USD | `-65.77%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,880,000.00 USD | 0.00 USD | 2,270.00 USD | `-64.47%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,880,000.00 USD | 0.00 USD | 15,650.00 USD | `-63.16%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,860,000.00 USD | 0.00 USD | 206.94 USD | `-61.20%` | `3,477,900,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,860,000.00 USD | 0.00 USD | 1,490.00 USD | `-60.55%` | `24,586,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,860,000.00 USD | 0.00 USD | 1,170.00 USD | `-59.25%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0655` | 1,860,000.00 USD | 0.00 USD | 230,320.00 USD | `-57.29%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,630,000.00 USD | 0.00 USD | 401.76 USD | `-56.64%` | `6,041,500,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,630,000.00 USD | 0.00 USD | 100,530.00 USD | `-55.99%` | `1,489,306,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,530,000.00 USD | 0.00 USD | 313.22 USD | `-55.34%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,530,000.00 USD | 0.00 USD | 1,600.00 USD | `-54.68%` | `23,002,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,520,000.00 USD | 0.00 USD | 2,970.00 USD | `-54.03%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,520,000.00 USD | 0.00 USD | 10,490.00 USD | `-53.38%` | `146,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,510,000.00 USD | 0.00 USD | 538.40 USD | `-52.73%` | `7,426,200,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,510,000.00 USD | 0.00 USD | 4,950.00 USD | `-52.08%` | `67,411,300,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,510,000.00 USD | 0.00 USD | 226.17 USD | `-51.42%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,510,000.00 USD | 0.00 USD | 14,690.00 USD | `-50.12%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,490,000.00 USD | 0.00 USD | 7,750.00 USD | `-49.47%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,480,000.00 USD | 0.00 USD | 7,240.00 USD | `-48.82%` | `92,219,900,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,480,000.00 USD | 0.00 USD | 12,730.00 USD | `-48.16%` | `160,092,800,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,460,000.00 USD | 0.00 USD | 1,470.00 USD | `-46.86%` | `18,000,000,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,460,000.00 USD | 0.00 USD | 13,940.00 USD | `-46.21%` | `168,979,700,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,450,000.00 USD | 0.00 USD | 5,660.00 USD | `-44.90%` | `67,027,300,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,440,000.00 USD | 0.00 USD | 4,210.00 USD | `-44.25%` | `49,197,200,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,440,000.00 USD | 0.00 USD | 19,460.00 USD | `-43.60%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,420,000.00 USD | 0.00 USD | 281.67 USD | `-42.95%` | `3,219,100,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,420,000.00 USD | 0.00 USD | 514.04 USD | `-42.30%` | `5,808,400,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,420,000.00 USD | 0.00 USD | 76,210.00 USD | `-40.99%` | `842,071,000,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,340,000.00 USD | 0.00 USD | 113.80 USD | `-40.34%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,340,000.00 USD | 0.00 USD | 4,130.00 USD | `-39.69%` | `44,668,100,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,340,000.00 USD | 0.00 USD | 814.24 USD | `-39.04%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,340,000.00 USD | 0.00 USD | 1,510.00 USD | `-38.38%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,330,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.08%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,330,000.00 USD | 0.00 USD | 145.24 USD | `-36.43%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 3,360.00 USD | `-35.78%` | `34,123,500,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,330,000.00 USD | 0.00 USD | 7,890.00 USD | `-35.12%` | `79,293,700,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,320,000.00 USD | 0.00 USD | 4,750.00 USD | `-34.47%` | `47,258,100,000,000.00` |
| `Live` | `Long` | `0.1015` | 1,320,000.00 USD | 0.00 USD | 1,190.00 USD | `-33.82%` | `11,734,500,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,320,000.00 USD | 0.00 USD | 773.66 USD | `-33.17%` | `7,547,900,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,320,000.00 USD | 0.00 USD | 5,200.00 USD | `-32.52%` | `50,240,900,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,310,000.00 USD | 0.00 USD | 6,230.00 USD | `-31.86%` | `59,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,300,000.00 USD | 0.00 USD | 8,670.00 USD | `-31.21%` | `82,163,500,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,300,000.00 USD | 0.00 USD | 4,210.00 USD | `-30.56%` | `39,491,300,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,290,000.00 USD | 0.00 USD | 11,960.00 USD | `-29.91%` | `111,262,400,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,280,000.00 USD | 0.00 USD | 11,210.00 USD | `-29.26%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,270,000.00 USD | 0.00 USD | 6,830.00 USD | `-28.60%` | `62,365,600,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,260,000.00 USD | 0.00 USD | 23,480.00 USD | `-27.95%` | `212,446,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,240,000.00 USD | 0.00 USD | 763.85 USD | `-27.30%` | `6,850,700,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,240,000.00 USD | 0.00 USD | 2,250.00 USD | `-26.65%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,230,000.00 USD | 0.00 USD | 724.13 USD | `-26.00%` | `6,380,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,230,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.34%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,220,000.00 USD | 0.00 USD | 3,370.00 USD | `-24.69%` | `29,178,500,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,220,000.00 USD | 0.00 USD | 1,120.00 USD | `-24.04%` | `9,600,900,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,220,000.00 USD | 0.00 USD | 6,120.00 USD | `-23.39%` | `52,087,700,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,210,000.00 USD | 0.00 USD | 27,310.00 USD | `-22.74%` | `230,428,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,190,000.00 USD | 0.00 USD | 1,830.00 USD | `-22.08%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1205` | 1,190,000.00 USD | 0.00 USD | 5,430.00 USD | `-21.43%` | `45,041,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,180,000.00 USD | 0.00 USD | 303.75 USD | `-20.78%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,180,000.00 USD | 0.00 USD | 18,490.00 USD | `-20.13%` | `150,964,100,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,160,000.00 USD | 0.00 USD | 34,560.00 USD | `-19.48%` | `279,831,800,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,130,000.00 USD | 0.00 USD | 7,500.00 USD | `-18.82%` | `60,262,700,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,120,000.00 USD | 0.00 USD | 136,640.00 USD | `-18.17%` | `1,088,732,600,000,000.12` |
| `Live` | `Long` | `0.1265` | 982,110.00 USD | 0.00 USD | 29,370.00 USD | `-17.52%` | `232,151,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 952,740.00 USD | 0.00 USD | 2,500.00 USD | `-16.87%` | `19,609,200,000,000.00` |
| `Live` | `Long` | `0.1285` | 950,240.00 USD | 0.00 USD | 15,410.00 USD | `-16.22%` | `119,948,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 934,830.00 USD | 0.00 USD | 3,750.00 USD | `-15.56%` | `28,930,900,000,000.00` |
| `Live` | `Long` | `0.1305` | 931,080.00 USD | 0.00 USD | 16,660.00 USD | `-14.91%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 914,420.00 USD | 0.00 USD | 5,820.00 USD | `-14.26%` | `44,230,000,000,000.00` |
| `Live` | `Long` | `0.1325` | 908,600.00 USD | 0.00 USD | 4,810.00 USD | `-13.61%` | `36,288,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 903,800.00 USD | 0.00 USD | 51,200.00 USD | `-12.96%` | `383,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 852,600.00 USD | 0.00 USD | 42,940.00 USD | `-12.30%` | `319,238,900,000,000.00` |
| `Live` | `Long` | `0.1355` | 809,660.00 USD | 0.00 USD | 1,440.00 USD | `-11.65%` | `10,635,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 808,220.00 USD | 0.00 USD | 1,830.00 USD | `-11.00%` | `13,388,500,000,000.00` |
| `Live` | `Long` | `0.1375` | 806,390.00 USD | 0.00 USD | 16,300.00 USD | `-10.35%` | `118,545,200,000,000.00` |
| `Live` | `Long` | `0.1385` | 790,090.00 USD | 0.00 USD | 5,580.00 USD | `-9.70%` | `40,282,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 784,510.00 USD | 0.00 USD | 13,350.00 USD | `-9.04%` | `95,717,800,000,000.00` |
| `Live` | `Long` | `0.1405` | 771,160.00 USD | 0.00 USD | 885.87 USD | `-8.39%` | `6,305,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 770,280.00 USD | 0.00 USD | 42,120.00 USD | `-7.74%` | `297,643,700,000,000.00` |
| `Live` | `Long` | `0.1425` | 728,160.00 USD | 0.00 USD | 486,180.00 USD | `-7.09%` | `3,411,759,100,000,000.00` |
| `Live` | `Long` | `0.1435` | 241,980.00 USD | 0.00 USD | 19,550.00 USD | `-6.44%` | `136,270,200,000,000.02` |
| `Live` | `Long` | `0.1445` | 222,430.00 USD | 0.00 USD | 9,330.00 USD | `-5.78%` | `64,545,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 213,100.00 USD | 0.00 USD | 96,140.00 USD | `-5.13%` | `660,773,400,000,000.00` |
| `Live` | `Long` | `0.1465` | 116,960.00 USD | 0.00 USD | 33,300.00 USD | `-4.48%` | `227,271,100,000,000.00` |
| `Live` | `Long` | `0.1475` | 83,660.00 USD | 0.00 USD | 81,380.00 USD | `-3.83%` | `551,703,100,000,000.00` |
| `Live` | `Long` | `0.1485` | 2,290.00 USD | 0.00 USD | 2,290.00 USD | `-3.18%` | `15,410,500,000,000.00` |
| `Live` | `Short` | `0.1605` | 2,700.00 USD | 2,700.00 USD | 0.00 USD | `+4.65%` | `16,822,400,000,000.00` |
| `Live` | `Short` | `0.1615` | 7,540.00 USD | 4,840.00 USD | 0.00 USD | `+5.30%` | `29,984,800,000,000.00` |
| `Live` | `Short` | `0.1625` | 10,450.00 USD | 2,910.00 USD | 0.00 USD | `+5.95%` | `17,905,900,000,000.00` |
| `Live` | `Short` | `0.1635` | 182,290.00 USD | 171,840.00 USD | 0.00 USD | `+6.60%` | `1,050,979,200,000,000.00` |
| `Live` | `Short` | `0.1645` | 182,410.00 USD | 118.90 USD | 0.00 USD | `+7.26%` | `722,800,000,000.00` |
| `Live` | `Short` | `0.1655` | 182,690.00 USD | 283.15 USD | 0.00 USD | `+7.91%` | `1,710,900,000,000.00` |
| `Live` | `Short` | `0.1685` | 183,530.00 USD | 838.64 USD | 0.00 USD | `+9.87%` | `4,977,100,000,000.00` |
| `Live` | `Short` | `0.1715` | 185,320.00 USD | 1,790.00 USD | 0.00 USD | `+11.82%` | `10,423,200,000,000.00` |
| `Live` | `Short` | `0.1725` | 187,780.00 USD | 2,460.00 USD | 0.00 USD | `+12.47%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1735` | 189,010.00 USD | 1,230.00 USD | 0.00 USD | `+13.13%` | `7,093,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 194,030.00 USD | 5,020.00 USD | 0.00 USD | `+16.39%` | `28,136,200,000,000.00` |
| `Live` | `Short` | `0.1865` | 196,760.00 USD | 2,730.00 USD | 0.00 USD | `+21.60%` | `14,639,700,000,000.00` |
| `Live` | `Short` | `0.1925` | 197,300.00 USD | 543.50 USD | 0.00 USD | `+25.51%` | `2,823,400,000,000.00` |
| `Live` | `Short` | `0.1945` | 197,930.00 USD | 623.68 USD | 0.00 USD | `+26.82%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 198,080.00 USD | 150.10 USD | 0.00 USD | `+28.77%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 209,670.00 USD | 11,590.00 USD | 0.00 USD | `+33.99%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 209,870.00 USD | 198.08 USD | 0.00 USD | `+35.95%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 210,030.00 USD | 164.23 USD | 0.00 USD | `+36.60%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 210,220.00 USD | 190.00 USD | 0.00 USD | `+37.25%` | `902,600,000,000.00` |
| `Live` | `Short` | `0.2135` | 225,910.00 USD | 15,690.00 USD | 0.00 USD | `+39.21%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 267,250.00 USD | 41,330.00 USD | 0.00 USD | `+40.51%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 293,340.00 USD | 26,090.00 USD | 0.00 USD | `+41.81%` | `119,969,800,000,000.00` |
| `Live` | `Short` | `0.2195` | 381,140.00 USD | 87,800.00 USD | 0.00 USD | `+43.12%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 381,260.00 USD | 114.52 USD | 0.00 USD | `+45.73%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 406,170.00 USD | 24,920.00 USD | 0.00 USD | `+47.03%` | `110,499,100,000,000.00` |
| `Live` | `Short` | `0.2295` | 413,000.00 USD | 6,820.00 USD | 0.00 USD | `+49.64%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 428,920.00 USD | 15,930.00 USD | 0.00 USD | `+53.55%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 429,030.00 USD | 102.62 USD | 0.00 USD | `+54.85%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 429,820.00 USD | 796.25 USD | 0.00 USD | `+58.11%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 430,050.00 USD | 231.03 USD | 0.00 USD | `+59.42%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2525` | 480,560.00 USD | 50,500.00 USD | 0.00 USD | `+64.63%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 481,100.00 USD | 546.54 USD | 0.00 USD | `+65.94%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 484,970.00 USD | 3,870.00 USD | 0.00 USD | `+67.24%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 513,880.00 USD | 28,910.00 USD | 0.00 USD | `+67.89%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 566,500.00 USD | 52,620.00 USD | 0.00 USD | `+68.55%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 566,650.00 USD | 154.94 USD | 0.00 USD | `+70.50%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 566,880.00 USD | 226.51 USD | 0.00 USD | `+75.07%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 580,390.00 USD | 13,510.00 USD | 0.00 USD | `+77.02%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 580,600.00 USD | 214.21 USD | 0.00 USD | `+77.67%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 580,880.00 USD | 274.50 USD | 0.00 USD | `+78.98%` | `1,000,000,000,000.00` |
| `Live` | `Short` | `0.2795` | 581,360.00 USD | 482.84 USD | 0.00 USD | `+82.24%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 581,550.00 USD | 187.26 USD | 0.00 USD | `+90.06%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 582,340.00 USD | 794.52 USD | 0.00 USD | `+90.72%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2935` | 582,610.00 USD | 262.80 USD | 0.00 USD | `+91.37%` | `895,400,000,000.00` |
| `Live` | `Short` | `0.3055` | 582,740.00 USD | 133.08 USD | 0.00 USD | `+99.19%` | `435,600,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 687,930.00 USD | 0.00 USD | 355.00 USD | `-76.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 687,580.00 USD | 0.00 USD | 297.50 USD | `-72.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 687,280.00 USD | 0.00 USD | 353.50 USD | `-67.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 686,930.00 USD | 0.00 USD | 276.53 USD | `-64.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 686,650.00 USD | 0.00 USD | 4,310.00 USD | `-63.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 682,340.00 USD | 0.00 USD | 475.11 USD | `-58.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 681,860.00 USD | 0.00 USD | 131.16 USD | `-57.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 681,730.00 USD | 0.00 USD | 881.45 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 680,850.00 USD | 0.00 USD | 1,070.00 USD | `-55.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 679,770.00 USD | 0.00 USD | 1,050.00 USD | `-55.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 678,720.00 USD | 0.00 USD | 1,010.00 USD | `-54.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 677,720.00 USD | 0.00 USD | 4,100.00 USD | `-54.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 673,610.00 USD | 0.00 USD | 529.04 USD | `-53.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 673,080.00 USD | 0.00 USD | 2,390.00 USD | `-52.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 670,690.00 USD | 0.00 USD | 757.39 USD | `-50.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 669,940.00 USD | 0.00 USD | 1,490.00 USD | `-48.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 668,450.00 USD | 0.00 USD | 277.37 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 668,170.00 USD | 0.00 USD | 262.50 USD | `-42.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 667,910.00 USD | 0.00 USD | 795.57 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 667,120.00 USD | 0.00 USD | 181.00 USD | `-40.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 666,940.00 USD | 0.00 USD | 3,810.00 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 663,120.00 USD | 0.00 USD | 1,550.00 USD | `-33.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 661,580.00 USD | 0.00 USD | 116.07 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 661,460.00 USD | 0.00 USD | 19,070.00 USD | `-29.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 642,390.00 USD | 0.00 USD | 577.22 USD | `-27.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 641,810.00 USD | 0.00 USD | 343.50 USD | `-25.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 641,470.00 USD | 0.00 USD | 26,280.00 USD | `-24.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 615,190.00 USD | 0.00 USD | 105.75 USD | `-23.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 615,080.00 USD | 0.00 USD | 24,280.00 USD | `-21.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 590,800.00 USD | 0.00 USD | 83,620.00 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 507,170.00 USD | 0.00 USD | 487.10 USD | `-20.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 506,690.00 USD | 0.00 USD | 14,940.00 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 491,750.00 USD | 0.00 USD | 129,320.00 USD | `-18.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 362,430.00 USD | 0.00 USD | 2,670.00 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 359,760.00 USD | 0.00 USD | 473.27 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 359,290.00 USD | 0.00 USD | 203,210.00 USD | `-16.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 156,080.00 USD | 0.00 USD | 2,800.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 153,280.00 USD | 0.00 USD | 1,590.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 151,690.00 USD | 0.00 USD | 6,000.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 145,680.00 USD | 0.00 USD | 3,350.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 142,330.00 USD | 0.00 USD | 502.28 USD | `-12.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 141,830.00 USD | 0.00 USD | 162.60 USD | `-11.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 141,670.00 USD | 0.00 USD | 700.86 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 140,970.00 USD | 0.00 USD | 13,710.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 127,250.00 USD | 0.00 USD | 108.57 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 127,150.00 USD | 0.00 USD | 3,520.00 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 123,620.00 USD | 0.00 USD | 127.35 USD | `-7.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 123,490.00 USD | 0.00 USD | 24,850.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 98,650.00 USD | 0.00 USD | 1,300.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 97,350.00 USD | 0.00 USD | 26,220.00 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 71,120.00 USD | 0.00 USD | 31,930.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 39,190.00 USD | 0.00 USD | 14,830.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 24,360.00 USD | 0.00 USD | 10,270.00 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 14,090.00 USD | 0.00 USD | 3,610.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 10,480.00 USD | 0.00 USD | 2,390.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 8,090.00 USD | 0.00 USD | 3,010.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 5,080.00 USD | 0.00 USD | 192.48 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 4,890.00 USD | 0.00 USD | 4,890.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1535` | 175.79 USD | 175.79 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1545` | 3,070.00 USD | 2,900.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 3,240.00 USD | 166.52 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 13,340.00 USD | 10,100.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 13,900.00 USD | 554.07 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 178,630.00 USD | 164,730.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 178,760.00 USD | 124.14 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 180,370.00 USD | 1,620.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 180,890.00 USD | 514.57 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 181,140.00 USD | 249.16 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 182,180.00 USD | 1,040.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 246,030.00 USD | 63,850.00 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 249,220.00 USD | 3,190.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 299,430.00 USD | 50,210.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 300,020.00 USD | 589.50 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 301,170.00 USD | 1,150.00 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 301,490.00 USD | 317.95 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 302,050.00 USD | 564.90 USD | 0.00 USD | `+11.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 303,850.00 USD | 1,800.00 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 304,420.00 USD | 571.13 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 313,260.00 USD | 8,840.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 313,480.00 USD | 219.54 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 314,830.00 USD | 1,350.00 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 315,490.00 USD | 657.66 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 315,830.00 USD | 336.40 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 316,730.00 USD | 898.02 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 343,120.00 USD | 26,390.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 354,650.00 USD | 11,540.00 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 364,900.00 USD | 10,240.00 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 365,760.00 USD | 864.12 USD | 0.00 USD | `+18.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 368,290.00 USD | 2,520.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 368,560.00 USD | 276.75 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 368,690.00 USD | 128.68 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 372,060.00 USD | 3,370.00 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 375,760.00 USD | 3,700.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 376,010.00 USD | 245.50 USD | 0.00 USD | `+22.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 376,670.00 USD | 660.73 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 377,370.00 USD | 697.34 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 377,590.00 USD | 222.24 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 406,720.00 USD | 29,130.00 USD | 0.00 USD | `+25.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 413,790.00 USD | 7,070.00 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 413,980.00 USD | 194.50 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 414,120.00 USD | 137.77 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 414,250.00 USD | 133.19 USD | 0.00 USD | `+28.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 418,000.00 USD | 3,750.00 USD | 0.00 USD | `+29.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 418,500.00 USD | 492.19 USD | 0.00 USD | `+30.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 441,250.00 USD | 22,750.00 USD | 0.00 USD | `+30.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 441,810.00 USD | 560.96 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 463,150.00 USD | 21,340.00 USD | 0.00 USD | `+32.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 549,040.00 USD | 85,900.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 550,510.00 USD | 1,470.00 USD | 0.00 USD | `+33.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 550,690.00 USD | 174.20 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 552,760.00 USD | 2,080.00 USD | 0.00 USD | `+35.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 553,010.00 USD | 252.51 USD | 0.00 USD | `+36.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 555,380.00 USD | 2,370.00 USD | 0.00 USD | `+37.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 555,510.00 USD | 126.50 USD | 0.00 USD | `+37.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 555,870.00 USD | 356.72 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 556,230.00 USD | 361.76 USD | 0.00 USD | `+40.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 556,590.00 USD | 365.12 USD | 0.00 USD | `+41.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 562,870.00 USD | 6,280.00 USD | 0.00 USD | `+42.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 563,240.00 USD | 368.47 USD | 0.00 USD | `+43.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 585,730.00 USD | 22,490.00 USD | 0.00 USD | `+43.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 586,060.00 USD | 333.91 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 590,040.00 USD | 3,980.00 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 590,420.00 USD | 378.55 USD | 0.00 USD | `+47.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 590,800.00 USD | 380.23 USD | 0.00 USD | `+47.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 590,980.00 USD | 185.87 USD | 0.00 USD | `+48.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 594,820.00 USD | 3,840.00 USD | 0.00 USD | `+48.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 639,470.00 USD | 44,650.00 USD | 0.00 USD | `+50.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 643,730.00 USD | 4,260.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 645,250.00 USD | 1,520.00 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 666,470.00 USD | 21,230.00 USD | 0.00 USD | `+54.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 669,000.00 USD | 2,530.00 USD | 0.00 USD | `+55.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 669,200.00 USD | 195.67 USD | 0.00 USD | `+56.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 688,920.00 USD | 19,720.00 USD | 0.00 USD | `+56.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 698,220.00 USD | 9,300.00 USD | 0.00 USD | `+57.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 699,970.00 USD | 1,750.00 USD | 0.00 USD | `+60.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 718,720.00 USD | 18,750.00 USD | 0.00 USD | `+60.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 719,280.00 USD | 551.23 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 719,670.00 USD | 397.90 USD | 0.00 USD | `+62.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 724,330.00 USD | 4,660.00 USD | 0.00 USD | `+63.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 724,650.00 USD | 320.66 USD | 0.00 USD | `+63.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 740,540.00 USD | 15,880.00 USD | 0.00 USD | `+65.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 742,530.00 USD | 2,000.00 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 745,090.00 USD | 2,550.00 USD | 0.00 USD | `+66.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 756,820.00 USD | 11,730.00 USD | 0.00 USD | `+67.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 761,980.00 USD | 5,160.00 USD | 0.00 USD | `+67.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 778,850.00 USD | 16,870.00 USD | 0.00 USD | `+69.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 805,630.00 USD | 26,790.00 USD | 0.00 USD | `+69.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 805,910.00 USD | 272.88 USD | 0.00 USD | `+76.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 806,020.00 USD | 114.99 USD | 0.00 USD | `+79.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 806,410.00 USD | 394.01 USD | 0.00 USD | `+80.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 806,790.00 USD | 375.53 USD | 0.00 USD | `+82.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 808,920.00 USD | 2,130.00 USD | 0.00 USD | `+86.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 809,500.00 USD | 579.27 USD | 0.00 USD | `+86.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 811,250.00 USD | 1,750.00 USD | 0.00 USD | `+89.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 811,350.00 USD | 101.21 USD | 0.00 USD | `+92.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 811,620.00 USD | 262.73 USD | 0.00 USD | `+93.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 813,060.00 USD | 1,440.00 USD | 0.00 USD | `+93.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 818,490.00 USD | 5,430.00 USD | 0.00 USD | `+95.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 823,920.00 USD | 5,430.00 USD | 0.00 USD | `+96.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 824,200.00 USD | 289.61 USD | 0.00 USD | `+99.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 824,690.00 USD | 487.09 USD | 0.00 USD | `+99.84%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1336` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD |
| `7D` | `0.1340` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD |
| `7D` | `0.1344` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD |
| `7D` | `0.1348` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD |
| `7D` | `0.1352` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD |
| `7D` | `0.1356` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD |
| `7D` | `0.1360` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD |
| `7D` | `0.1364` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1368` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `1D` | `0.1370` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD |
| `7D` | `0.1372` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1373` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `0.1376` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD |
| `1D` | `0.1379` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 2,250.00 USD | 821.64 USD | 1,020.00 USD |
| `7D` | `0.1380` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `1D` | `0.1382` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 10,310.00 USD | 9,440.00 USD | 29,450.00 USD |
| `7D` | `0.1384` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `1D` | `0.1385` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD |
| `1D` | `0.1388` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD |
| `7D` | `0.1388` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `1D` | `0.1391` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD |
| `7D` | `0.1392` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `1D` | `0.1394` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1396` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD |
| `1D` | `0.1397` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1400` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1400` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1404` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1412` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1416` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1421` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1432` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `0.1433` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1436` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD |
| `7D` | `0.1436` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1439` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD |
| `7D` | `0.1440` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD |
| `1D` | `0.1442` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1444` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1451` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1452` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `7D` | `0.1456` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1460` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `1D` | `0.1463` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `7D` | `0.1464` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1466` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.1468` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD |
| `1D` | `0.1469` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD |
| `1D` | `0.1472` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD |
| `7D` | `0.1472` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1475` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD |
| `7D` | `0.1476` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD |
| `1D` | `0.1478` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD |
| `7D` | `0.1480` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD |
| `1D` | `0.1481` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD |
| `1D` | `0.1484` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD |
| `7D` | `0.1484` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD |
| `1D` | `0.1487` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 8,170.00 USD | 4,430.00 USD | 9,210.00 USD |
| `7D` | `0.1488` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD |
| `1D` | `0.1490` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 38,650.00 USD | 9,450.00 USD | 4,940.00 USD |
| `7D` | `0.1492` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD |
| `1D` | `0.1493` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 14,230.00 USD | 3,520.00 USD | 6,470.00 USD |
| `1D` | `0.1496` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 14,390.00 USD | 5,270.00 USD | 2,530.00 USD |
| `7D` | `0.1496` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD |
| `1D` | `0.1499` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD |
| `7D` | `0.1500` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD |
| `1D` | `0.1502` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 3,610.00 USD | 13,270.00 USD | 130,030.00 USD |
| `7D` | `0.1504` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD |
| `1D` | `0.1505` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 54,760.00 USD | 23,120.00 USD | 7,830.00 USD |
| `1D` | `0.1508` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 200,020.00 USD | 16,950.00 USD | 259,490.00 USD |
| `7D` | `0.1508` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD |
| `1D` | `0.1511` | 774,760.00 USD | 0.00 USD | 774,760.00 USD | 122,160.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 988,210.00 USD | 0.00 USD | 988,210.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD |
| `1D` | `0.1514` | 645,740.00 USD | 0.00 USD | 645,740.00 USD | 25,970.00 USD | 1,730.00 USD | 232,880.00 USD |
| `7D` | `0.1516` | 828,660.00 USD | 0.00 USD | 828,660.00 USD | 48,970.00 USD | 13,330.00 USD | 377,220.00 USD |
| `1D` | `0.1517` | 385,160.00 USD | 0.00 USD | 385,160.00 USD | 87,420.00 USD | 7,460.00 USD | 141,720.00 USD |
| `1D` | `0.1520` | 148,550.00 USD | 0.00 USD | 148,550.00 USD | 44,180.00 USD | 4,100.00 USD | 22,260.00 USD |
| `7D` | `0.1520` | 389,140.00 USD | 0.00 USD | 389,140.00 USD | 47,340.00 USD | 22,090.00 USD | 201,180.00 USD |
| `1D` | `0.1523` | 78,010.00 USD | 0.00 USD | 78,010.00 USD | 41,110.00 USD | 6,450.00 USD | 5,390.00 USD |
| `7D` | `0.1524` | 118,540.00 USD | 0.00 USD | 118,540.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD |
| `7D` | `0.1528` | 96,270.00 USD | 0.00 USD | 96,270.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD |
| `7D` | `0.1532` | 62,330.00 USD | 0.00 USD | 62,330.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD |
| `1D` | `0.1535` | 25,060.00 USD | 0.00 USD | 25,060.00 USD | 0.00 USD | 8,980.00 USD | 0.00 USD |
| `7D` | `0.1536` | 45,070.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `7D` | `0.1540` | 36,500.00 USD | 0.00 USD | 36,500.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `7D` | `0.1544` | 18,270.00 USD | 0.00 USD | 18,270.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1547` | 16,080.00 USD | 0.00 USD | 16,080.00 USD | 0.00 USD | 13,520.00 USD | 0.00 USD |
| `7D` | `0.1548` | 14,680.00 USD | 0.00 USD | 14,680.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1550` | 2,560.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD |
| `7D` | `0.1552` | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD |
| `7D` | `0.1553` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1554` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1560` | 10,990.00 USD | 10,990.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.1562` | 4,970.00 USD | 4,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,970.00 USD |
| `7D` | `0.1564` | 44,740.00 USD | 44,740.00 USD | 0.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `0.1565` | 312,110.00 USD | 312,110.00 USD | 0.00 USD | 41,260.00 USD | 13,270.00 USD | 252,610.00 USD |
| `1D` | `0.1568` | 599,940.00 USD | 599,940.00 USD | 0.00 USD | 33,360.00 USD | 38,630.00 USD | 215,830.00 USD |
| `7D` | `0.1568` | 323,420.00 USD | 323,420.00 USD | 0.00 USD | 111,700.00 USD | 15,360.00 USD | 151,620.00 USD |
| `1D` | `0.1571` | 706,210.00 USD | 706,210.00 USD | 0.00 USD | 40,700.00 USD | 6,150.00 USD | 59,420.00 USD |
| `7D` | `0.1572` | 657,220.00 USD | 657,220.00 USD | 0.00 USD | 235,420.00 USD | 39,540.00 USD | 58,840.00 USD |
| `1D` | `0.1574` | 732,180.00 USD | 732,180.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1576` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 44,680.00 USD | 123,840.00 USD | 315,950.00 USD |
| `1D` | `0.1577` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 69,720.00 USD | 0.00 USD | 351,730.00 USD |
| `1D` | `0.1580` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,930.00 USD |
| `7D` | `0.1580` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 226,250.00 USD | 101,090.00 USD | 0.00 USD |
| `1D` | `0.1583` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 69,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1584` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 80,450.00 USD | 43,370.00 USD | 114,120.00 USD |
| `1D` | `0.1586` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 20,750.00 USD | 16,450.00 USD |
| `7D` | `0.1588` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD |
| `1D` | `0.1589` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 15,100.00 USD | 19,490.00 USD | 13,300.00 USD |
| `1D` | `0.1592` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 20,480.00 USD | 21,620.00 USD |
| `7D` | `0.1592` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 64,620.00 USD | 0.00 USD |
| `1D` | `0.1595` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,910.00 USD |
| `7D` | `0.1596` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 98,530.00 USD | 0.00 USD |
| `1D` | `0.1598` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 16,680.00 USD | 0.00 USD | 99,410.00 USD |
| `7D` | `0.1600` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 60,710.00 USD | 75,810.00 USD |
| `1D` | `0.1601` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1604` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 99,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 188,060.00 USD | 112,090.00 USD | 273,670.00 USD |
| `1D` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD |
| `7D` | `0.1608` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD |
| `1D` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD |
| `7D` | `0.1612` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD |
| `1D` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 37,090.00 USD | 11,530.00 USD | 97,990.00 USD |
| `1D` | `0.1616` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 17,630.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `0.1616` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD |
| `1D` | `0.1619` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD |
| `7D` | `0.1620` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD |
| `1D` | `0.1622` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD |
| `7D` | `0.1624` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD |
| `1D` | `0.1625` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD |
| `1D` | `0.1628` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD |
| `7D` | `0.1628` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `1D` | `0.1631` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD |
| `1D` | `0.1634` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD |
| `7D` | `0.1636` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD |
| `1D` | `0.1637` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD |
| `1D` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD |
| `7D` | `0.1640` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD |
| `1D` | `0.1646` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1648` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1655` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD |
| `1D` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD |
| `7D` | `0.1660` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD |
| `1D` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD |
| `1D` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD |
| `7D` | `0.1664` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1667` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD |
| `7D` | `0.1668` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD |
| `7D` | `0.1672` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1673` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 66,630.00 USD | 2,010.00 USD | 19,670.00 USD |
| `1D` | `0.1676` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD |
| `7D` | `0.1676` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD |
| `1D` | `0.1679` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1680` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD |
| `1D` | `0.1682` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 154,780.00 USD | 4,560.00 USD | 18,740.00 USD |
| `7D` | `0.1684` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1685` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 20,370.00 USD | 29,790.00 USD | 13,450.00 USD |
| `1D` | `0.1688` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 2,650.00 USD | 39,950.00 USD |
| `7D` | `0.1688` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1691` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 75,680.00 USD | 76,030.00 USD | 54,060.00 USD |
| `7D` | `0.1692` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 33,660.00 USD | 70,740.00 USD | 71,020.00 USD |
| `1D` | `0.1694` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 34,000.00 USD | 22,300.00 USD | 11,880.00 USD |
| `7D` | `0.1696` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD |
| `1D` | `0.1697` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 36,180.00 USD | 38,310.00 USD | 6,650.00 USD |
| `1D` | `0.1700` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 13,350.00 USD | 21,160.00 USD | 46,050.00 USD |
| `7D` | `0.1700` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1703` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 9,960.00 USD | 14,420.00 USD | 34,530.00 USD |
| `7D` | `0.1704` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1706` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 38,860.00 USD | 9,590.00 USD | 13,990.00 USD |
| `7D` | `0.1708` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 87,520.00 USD |
| `1D` | `0.1709` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 21,630.00 USD | 62,270.00 USD | 2,710.00 USD |
| `1D` | `0.1712` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 15,040.00 USD | 5,330.00 USD |
| `1D` | `0.1715` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 9,570.00 USD | 27,880.00 USD | 9,370.00 USD |
| `7D` | `0.1716` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD |
| `1D` | `0.1718` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD |
| `7D` | `0.1720` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD |
| `1D` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD |
| `7D` | `0.1724` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD |
| `1D` | `0.1727` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD |
| `1D` | `0.1730` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1732` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1736` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD |
| `7D` | `0.1740` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1742` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD |
| `7D` | `0.1744` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD |
| `1D` | `0.1748` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD |
| `7D` | `0.1748` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1751` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1752` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 291,880.00 USD |
| `1D` | `0.1754` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 32,060.00 USD | 8,430.00 USD | 42,180.00 USD |
| `7D` | `0.1756` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 186,030.00 USD |
| `1D` | `0.1757` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 15,820.00 USD | 22,420.00 USD | 70,640.00 USD |
| `1D` | `0.1760` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 94,020.00 USD | 79,990.00 USD | 21,230.00 USD |
| `7D` | `0.1760` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 268,160.00 USD | 63,870.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 50,470.00 USD | 16,490.00 USD | 68,500.00 USD |
| `7D` | `0.1764` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 338,490.00 USD | 252,140.00 USD | 40,340.00 USD |
| `1D` | `0.1766` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 62,960.00 USD |
| `7D` | `0.1768` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 191,690.00 USD | 147,360.00 USD | 31,570.00 USD |
| `1D` | `0.1769` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 40,920.00 USD | 78,870.00 USD | 44,210.00 USD |
| `1D` | `0.1772` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 22,380.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1772` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD |
| `7D` | `0.1776` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD |
| `7D` | `0.1780` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD |
| `7D` | `0.1784` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `7D` | `0.1788` | 12,020,000.00 USD | 12,020,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `7D` | `0.1792` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD |
| `7D` | `0.1796` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD |
| `7D` | `0.1800` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD |
| `7D` | `0.1804` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD |
| `7D` | `0.1808` | 12,730,000.00 USD | 12,730,000.00 USD | 0.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD |
| `7D` | `0.1812` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD |
| `7D` | `0.1816` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD |
| `7D` | `0.1820` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD |
| `7D` | `0.1824` | 13,390,000.00 USD | 13,390,000.00 USD | 0.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD |
| `7D` | `0.1828` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD |
| `7D` | `0.1832` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD |
| `7D` | `0.1836` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD |
| `7D` | `0.1840` | 14,460,000.00 USD | 14,460,000.00 USD | 0.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD |
| `7D` | `0.1844` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 94,510.00 USD | 20,390.00 USD | 97,510.00 USD |
| `7D` | `0.1848` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD |
| `7D` | `0.1852` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD |
| `7D` | `0.1856` | 15,510,000.00 USD | 15,510,000.00 USD | 0.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD |
| `7D` | `0.1860` | 15,750,000.00 USD | 15,750,000.00 USD | 0.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD |
| `7D` | `0.1864` | 15,910,000.00 USD | 15,910,000.00 USD | 0.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD |
| `7D` | `0.1868` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 133,990.00 USD | 38,100.00 USD | 56,290.00 USD |
| `7D` | `0.1872` | 16,410,000.00 USD | 16,410,000.00 USD | 0.00 USD | 138,560.00 USD | 67,770.00 USD | 68,190.00 USD |
| `7D` | `0.1876` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 65,910.00 USD | 23,180.00 USD | 43,960.00 USD |
| `7D` | `0.1880` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 57,250.00 USD | 22,460.00 USD | 30,950.00 USD |
| `7D` | `0.1884` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD |
| `7D` | `0.1888` | 16,830,000.00 USD | 16,830,000.00 USD | 0.00 USD | 22,970.00 USD | 4,800.00 USD | 88,260.00 USD |
| `7D` | `0.1892` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD |
| `7D` | `0.1896` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 42,320.00 USD | 11,820.00 USD | 18,680.00 USD |
| `7D` | `0.1900` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD |
| `7D` | `0.1904` | 17,080,000.00 USD | 17,080,000.00 USD | 0.00 USD | 14,330.00 USD | 10,990.00 USD | 10,800.00 USD |
| `7D` | `0.1908` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 8,720.00 USD | 5,070.00 USD | 9,380.00 USD |
| `7D` | `0.1912` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 0.00 USD | 9,380.00 USD | 10,330.00 USD |
| `7D` | `0.1916` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD |
| `7D` | `0.1920` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD |
| `7D` | `0.1924` | 17,170,000.00 USD | 17,170,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1928` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD |
| `7D` | `0.1944` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1952` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |
| `7D` | `0.1956` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD |
| `7D` | `0.1960` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1964` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `179.89M` | Total OI Tokens: `1,159,711,327.4 ARB`
  * 1h OI Change: `+0.93%` | 4h OI Change: `-3.34%` | 24h OI Change: `-16.58%`
  * Exchange Breakdown: Binance=`40.44M` | Bybit=`25.14M` | OKX=`13.69M` | Hyperliquid=`12.73M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.29K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0065%` | **USDT OKX** | `-0.0043%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0043%` |
| **USDT MEXC** | `-0.0044%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0043%` | **USDT Bitget** | `-0.0132%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `55.21%` | `44.79%` | `1.23` | 1,330,000.00 USD |
| `15M` | `Binance` | `60.68%` | `39.32%` | `1.54` | 527,850.00 USD |
| `15M` | `OKX` | `68.02%` | `31.98%` | `2.13` | 87,790.00 USD |
| `15M` | `Bybit` | `57.95%` | `42.05%` | `1.38` | 114,270.00 USD |
| `15M` | `KuCoin` | `51%` | `49%` | `1.04` | 89,910.00 USD |
| `15M` | `Gate` | `72.8%` | `27.2%` | `2.68` | 25,230.00 USD |
| `15M` | `Bitget` | `42.54%` | `57.46%` | `0.74` | 10,740.00 USD |
| `15M` | `BingX` | `34.87%` | `65.13%` | `0.54` | 66,160.00 USD |
| `15M` | `MEXC` | `50.71%` | `49.29%` | `1.03` | 102,650.00 USD |
| `15M` | `Bitunix` | `59.99%` | `40.01%` | `1.50` | 11,300.00 USD |
| `15M` | `Hyperliquid` | `52.84%` | `47.16%` | `1.12` | 2,740.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.81%` | `54.19%` | `0.85` | 277,540.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.30 USD |
| `15M` | `WhiteBIT` | `76.33%` | `23.67%` | `3.22` | 6,940.00 USD |
| `15M` | `HTX` | `37.4%` | `62.6%` | `0.60` | 2,570.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.97%` | `33.03%` | `2.03` | 1,520.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 54.56 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `17.58%` | `82.42%` | `0.21` | 306.69 USD |
| `15M` | `Whale Positions` | `60.68%` | `39.32%` | `1.54` | 527,850.00 USD |
| `15M` | `Global Accounts` | `55.21%` | `44.79%` | `1.23` | 1,330,000.00 USD |
| `1H` | `ARB` | `42.03%` | `57.97%` | `0.73` | 6,900,000.00 USD |
| `1H` | `Binance` | `56.1%` | `43.9%` | `1.28` | 2,110,000.00 USD |
| `1H` | `OKX` | `56.78%` | `43.22%` | `1.31` | 479,550.00 USD |
| `1H` | `Bybit` | `56.38%` | `43.62%` | `1.29` | 549,850.00 USD |
| `1H` | `KuCoin` | `50.67%` | `49.33%` | `1.03` | 329,280.00 USD |
| `1H` | `Gate` | `65.37%` | `34.63%` | `1.89` | 128,640.00 USD |
| `1H` | `Bitget` | `50.17%` | `49.83%` | `1.01` | 119,470.00 USD |
| `1H` | `BingX` | `5.6%` | `94.4%` | `0.06` | 1,720,000.00 USD |
| `1H` | `MEXC` | `49.45%` | `50.55%` | `0.98` | 272,460.00 USD |
| `1H` | `Bitunix` | `34.66%` | `65.34%` | `0.53` | 64,400.00 USD |
| `1H` | `Hyperliquid` | `48.45%` | `51.55%` | `0.94` | 40,640.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.33%` | `49.67%` | `1.01` | 1,050,000.00 USD |
| `1H` | `Crypto.com` | `93.75%` | `6.25%` | `15.00` | 271.40 USD |
| `1H` | `WhiteBIT` | `37.88%` | `62.12%` | `0.61` | 17,110.00 USD |
| `1H` | `HTX` | `39.35%` | `60.65%` | `0.65` | 3,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `89.98%` | `10.02%` | `8.98` | 5,440.00 USD |
| `1H` | `Aster` | `31.14%` | `68.86%` | `0.45` | 210.81 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `87.09%` | `12.91%` | `6.75` | 8,490.00 USD |
| `1H` | `Whale Positions` | `56.1%` | `43.9%` | `1.28` | 2,110,000.00 USD |
| `1H` | `Global Accounts` | `42.03%` | `57.97%` | `0.73` | 6,900,000.00 USD |
| `4H` | `ARB` | `45.71%` | `54.29%` | `0.84` | 43,380,000.00 USD |
| `4H` | `Binance` | `48.52%` | `51.48%` | `0.94` | 15,150,000.00 USD |
| `4H` | `OKX` | `45.88%` | `54.12%` | `0.85` | 4,770,000.00 USD |
| `4H` | `Bybit` | `45.96%` | `54.04%` | `0.85` | 6,770,000.00 USD |
| `4H` | `KuCoin` | `49.23%` | `50.77%` | `0.97` | 895,430.00 USD |
| `4H` | `Gate` | `58.85%` | `41.15%` | `1.43` | 833,170.00 USD |
| `4H` | `Bitget` | `47.75%` | `52.25%` | `0.91` | 1,450,000.00 USD |
| `4H` | `BingX` | `15.78%` | `84.22%` | `0.19` | 2,920,000.00 USD |
| `4H` | `MEXC` | `47.57%` | `52.43%` | `0.91` | 2,190,000.00 USD |
| `4H` | `Bitunix` | `44.65%` | `55.35%` | `0.81` | 409,580.00 USD |
| `4H` | `Hyperliquid` | `47.68%` | `52.32%` | `0.91` | 1,070,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.82%` | `52.18%` | `0.92` | 6,150,000.00 USD |
| `4H` | `Crypto.com` | `17.6%` | `82.4%` | `0.21` | 13,470.00 USD |
| `4H` | `WhiteBIT` | `58.81%` | `41.19%` | `1.43` | 544,150.00 USD |
| `4H` | `HTX` | `65.05%` | `34.95%` | `1.86` | 40,030.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.62%` | `54.38%` | `0.84` | 72,110.00 USD |
| `4H` | `Aster` | `20.49%` | `79.51%` | `0.26` | 20,200.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.81%` | `58.19%` | `0.72` | 81,900.00 USD |
| `4H` | `Whale Positions` | `48.52%` | `51.48%` | `0.94` | 15,150,000.00 USD |
| `4H` | `Global Accounts` | `45.71%` | `54.29%` | `0.84` | 43,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1550` | `0.1546` | `0.1550` | `0.1552` | `0.1538` | 1,428,021.10 USD | 808,975.04 USD | 619,046.06 USD | 189,928.98 USD | `+13.30%` | `17B / 10S` |
| `0:00 UTC` | `0.1525` | `0.1532` | `0.1525` | `0.1544` | `0.1522` | 2,110,848.48 USD | 1,098,398.51 USD | 1,012,449.97 USD | 85,948.54 USD | `+4.07%` | `6B / 10S` |
| `5:00 UTC` | `0.1507` | `0.1503` | `0.1507` | `0.1530` | `0.1471` | 10,277,659.34 USD | 4,448,495.39 USD | 5,829,163.95 USD | -1,380,668.57 USD | `-13.43%` | `4B / 24S` |
| `0:00 UTC` | `0.1498` | `0.1510` | `0.1498` | `0.1532` | `0.1492` | 3,257,292.15 USD | 1,571,991.63 USD | 1,685,300.52 USD | -113,308.89 USD | `-3.48%` | `23B / 32S` |
| `5:00 UTC` | `0.1550` | `0.1544` | `0.1550` | `0.1556` | `0.1526` | 2,934,484.43 USD | 1,770,871.27 USD | 1,163,613.16 USD | 607,258.11 USD | `+20.69%` | `21B / 14S` |
| `0:00 UTC` | `0.1552` | `0.1542` | `0.1552` | `0.1557` | `0.1528` | 1,449,793.31 USD | 742,538.14 USD | 707,255.18 USD | 35,282.96 USD | `+2.43%` | `14B / 29S` |
| `5:00 UTC` | `0.1544` | `0.1535` | `0.1544` | `0.1546` | `0.1528` | 1,252,838.62 USD | 503,258.60 USD | 749,580.02 USD | -246,321.42 USD | `-19.66%` | `11B / 39S` |
| `0:00 UTC` | `0.1540` | `0.1534` | `0.1540` | `0.1545` | `0.1520` | 1,447,365.29 USD | 641,921.41 USD | 805,443.88 USD | -163,522.47 USD | `-11.30%` | `6B / 8S` |
| `5:00 UTC` | `0.1525` | `0.1530` | `0.1525` | `0.1537` | `0.1524` | 762,631.88 USD | 375,329.43 USD | 387,302.45 USD | -11,973.03 USD | `-1.57%` | `23B / 18S` |
| `0:00 UTC` | `0.1532` | `0.1533` | `0.1532` | `0.1540` | `0.1526` | 871,742.10 USD | 423,070.07 USD | 448,672.03 USD | -25,601.96 USD | `-2.94%` | `17B / 20S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1671` | 1,100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1677` | 2,200,000.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1667` | 522,000.00 USD | 0.00 USD |
| `10-28 20:42` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1670` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1668` | 0.00 USD | 0.00 USD |
| `10-28 20:36` | `Volume 10M ARB` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1677` | 0.00 USD | 0.00 USD |
| `10-28 20:08` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1637` | 359,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1637` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1642` | 1,100,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,300,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1640` | 0.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1634` | 0.00 USD | 0.00 USD |
| `10-28 19:42` | `Volume 10M ARB` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,900,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1649` | 0.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 10M ARB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1659` | 2,200,000.00 USD | 0.00 USD |
| `10-28 18:55` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1652` | 0.00 USD | 0.00 USD |
| `10-28 18:43` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1646` | 0.00 USD | 0.00 USD |
| `10-28 18:23` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1641` | 0.00 USD | 0.00 USD |
| `10-28 18:08` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1654` | 0.00 USD | 0.00 USD |
| `10-28 17:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 2,000,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1658` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 504,000.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1659` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1676` | 294,000.00 USD | 0.00 USD |
| `10-28 16:55` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1685` | 413,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 15:42` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 751,000.00 USD | 0.00 USD |
| `10-28 14:07` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1701` | 750,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1705` | 3,300,000.00 USD | 0.00 USD |
| `10-28 13:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1683` | 1,800,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1677` | 434,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1677` | 1,900,000.00 USD | 0.00 USD |
| `10-28 12:29` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1684` | 0.00 USD | 0.00 USD |
| `10-28 11:54` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 11:22` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1688` | 1,200,000.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 513,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 09:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1681` | 1,300,000.00 USD | 0.00 USD |
| `10-28 09:09` | `Range 0.0005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.1708` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1688` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1688` | 843,000.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1694` | 0.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1699` | 422,000.00 USD | 0.00 USD |
| `10-28 07:57` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1691` | 1,100,000.00 USD | 0.00 USD |
| `10-28 07:35` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 06:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1691` | 1,600,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 118,750.00 USD | 258,090.00 USD | **`ACCUMULATION`** |
| `15m` | 218,210.00 USD | 154,480.00 USD | **`ACCUMULATION`** |
| `30m` | 262,170.00 USD | 236,820.00 USD | **`ACCUMULATION`** |
| `1h` | 44,860.00 USD | -91,470.00 USD | **`DISTRIBUTION`** |
| `2h` | -110,260.00 USD | -1,230,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 121,640.00 USD | 471,170.00 USD | **`ACCUMULATION`** |
| `6h` | -1,520,000.00 USD | -5,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,110,000.00 USD | -6,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,860,000.00 USD | -7,800,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,090,000.00 USD | -8,460,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,680,000.00 USD | -37,650,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,730,000.00 USD | -164,310,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+118.75K` | 15m=`+218.21K` | 1h=`+44.86K` | 24h=`-2.09M`
* Futures Capital Netflows: 5m=`+258.09K` | 15m=`+154.48K` | 1h=`-91.47K` | 24h=`-8.46M`
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
  * `2026-10-30 07:16:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:39:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:39:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:34 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1695` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.03` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.17`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1705` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.37` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.83`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1714`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
