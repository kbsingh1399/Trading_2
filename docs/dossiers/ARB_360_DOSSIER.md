# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 02:33:42 IST` (`2026-10-29 21:03:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1551` | `0.1556` | `0.1508` | `0.1538` | `32,688,391` | 5,009,620.54 USD | -939,339.59 USD | `-18.75%` | -7,894,978.15 USD | `-2.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1538` | `0.1560` | `0.1524` | `0.1539` | `24,002,679` | 3,693,842.56 USD | -786,319.86 USD | `-21.29%` | -8,681,298.01 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1538` | `0.1544` | `0.1537` | `0.1543` | `3,254,803` | 501,668.05 USD | -68,961.56 USD | `-13.75%` | -8,750,259.57 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1657` | `0.1661` | `0.1649` | `0.1650` | `4,340,197` | 718,046.47 USD | 110,593.73 USD | `+15.40%` | -4,530,062.11 USD | `+1.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1650` | `0.1656` | `0.1541` | `0.1551` | `65,543,762` | 10,418,999.97 USD | -2,425,576.45 USD | `-23.28%` | -6,955,638.56 USD | `-4.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1551` | `0.1560` | `0.1508` | `0.1542` | `59,795,295` | 9,181,892.79 USD | -1,810,166.71 USD | `-19.71%` | -8,765,805.27 USD | `-2.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.1696` | `0.1704` | `0.1673` | `0.1687` | `18,975,463` | 3,201,824.26 USD | -35,947.57 USD | `-1.12%` | -4,720,262.78 USD | `+0.39` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1686` | `0.1693` | `0.1678` | `0.1683` | `12,478,051` | 2,101,814.57 USD | 317,188.30 USD | `+15.09%` | -4,403,074.48 USD | `+1.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `144,959,619` | 22,848,810.94 USD | -4,367,959.97 USD | `-19.12%` | -8,771,034.44 USD | `-4.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `144,959,619` | 22,848,810.94 USD | -4,367,959.97 USD | `-19.12%` | -7,939,960.75 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.1652` | `0.1687` | `0.1623` | `0.1631` | `68,085,678` | 11,252,816.65 USD | -909,329.92 USD | `-8.08%` | -705,420.63 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,136,414.44 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,374,542.78 USD | `-1.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,572,000.78 USD | `-0.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `144,959,619` | 22,848,810.94 USD | -4,367,959.97 USD | `-19.12%` | -7,939,960.75 USD | `-2.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 7,480.04 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 7.48K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 99.93 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.10K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 455.89 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.46K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 455.89 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.46K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,816.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.82K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 394.95 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.39K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,816.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.82K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 394.95 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.39K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1704` | 1,274.59 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.27K USD at 0.1704 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `0.1695` | 7,870.81 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 7.87K USD at 0.1695 USD [API] | `2026-10-28 02:08:38` |
| `ANNOUNCEMENT` | `INFO` | `0.1952` | 1,892.80 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.89K USD at 0.1952 USD [API] | `2026-10-02 18:39:18` |
| `ANNOUNCEMENT` | `INFO` | `0.1972` | 32.77 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.03K USD at 0.1972 USD [API] | `2026-10-01 10:02:44` |
| `ANNOUNCEMENT` | `INFO` | `0.2130` | 263.28 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.26K USD at 0.2130 USD [API] | `2026-09-24 08:27:05` |
| `ANNOUNCEMENT` | `INFO` | `0.1607` | 125.43 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.13K USD at 0.1607 USD [API] | `2026-09-16 14:22:29` |
| `ANNOUNCEMENT` | `INFO` | `0.1608` | 997.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.00K USD at 0.1608 USD [API] | `2026-09-16 14:22:29` |
| `ANNOUNCEMENT` | `INFO` | `0.1608` | 400.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.40K USD at 0.1608 USD [API] | `2026-09-16 14:22:29` |
| `ANNOUNCEMENT` | `INFO` | `0.1822` | 28,687.42 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 28.69K USD at 0.1822 USD [API] | `2026-10-07 02:01:17` |
| `ANNOUNCEMENT` | `INFO` | `0.1695` | 9,043.77 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 9.04K USD at 0.1695 USD [API] | `2026-10-28 08:32:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1784` (Vol: 124,200.00 USD, Dist: `+7.91%`) | Long MP=`0.1622` (Vol: 145,200.00 USD, Dist: `--1.94%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+7.88%`) | Long MP=`0.1598` (Vol: 154,300.00 USD, Dist: `--3.38%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+7.88%`) | Long MP=`0.1598` (Vol: 205,900.00 USD, Dist: `--3.38%`)
  * 7D Horizon: Short MP=`0.1834` (Vol: 181,500.00 USD, Dist: `+10.87%`) | Long MP=`0.1616` (Vol: 292,500.00 USD, Dist: `--2.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0345` | 1,180.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 2,200.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 138,900.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 408.10 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0445` | 8,100.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 3,090.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 4,840.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 400.94 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 668.38 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 7,100.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 18,660.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 148.49 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 187.50 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 283.15 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 100,530.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 590.45 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 77,980.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,260.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,370.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 368.95 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 27,480.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 6,180.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 6,040.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 7,840.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 13,950.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 751.50 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 19,010.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 22,430.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 12,960.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 1,320.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 4,130.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 4,090.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 589.63 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 5,970.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 9,200.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 12,790.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 811.82 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,700.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 12,770.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,650.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 342.59 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 534.49 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 2,190.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 1,360.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 16,170.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 11,120.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 1,760.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 26,260.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 6,210.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 14,190.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 8,920.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 34,620.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 3,110.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,960.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 1,200.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 4,190.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 11,100.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,600.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 10,500.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 8,090.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 26,200.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 1,960,000.00 USD | 1,960,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 1,930,000.00 USD | 1,930,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1341` | 1,140,000.00 USD | 1,140,000.00 USD | 3,550.00 USD | 1,460.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1344` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 691.54 USD | 598.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 1,880,000.00 USD | 1,880,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 2,970.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1347` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 670.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1348` | 1,850,000.00 USD | 1,850,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1350` | 1,130,000.00 USD | 1,130,000.00 USD | 5,030.00 USD | 1,310.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 1,790,000.00 USD | 1,790,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1353` | 1,120,000.00 USD | 1,120,000.00 USD | 3,530.00 USD | 1,430.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1356` | 1,110,000.00 USD | 1,110,000.00 USD | 932.52 USD | 0.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1356` | 1,750,000.00 USD | 1,750,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1359` | 1,110,000.00 USD | 1,110,000.00 USD | 2,480.00 USD | 869.31 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 1,710,000.00 USD | 1,710,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1362` | 1,100,000.00 USD | 1,100,000.00 USD | 4,890.00 USD | 950.53 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 1,670,000.00 USD | 1,670,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1365` | 1,090,000.00 USD | 1,090,000.00 USD | 1,340.00 USD | 1,900.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 2,740.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1368` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1368` | 1,650,000.00 USD | 1,650,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1371` | 1,080,000.00 USD | 1,080,000.00 USD | 3,680.00 USD | 1,110.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 1,630,000.00 USD | 1,630,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1374` | 1,080,000.00 USD | 1,080,000.00 USD | 1,790.00 USD | 2,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,750.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1377` | 1,070,000.00 USD | 1,070,000.00 USD | 936.88 USD | 821.64 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1380` | 1,070,000.00 USD | 1,070,000.00 USD | 3,510.00 USD | 7,310.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 1,630,000.00 USD | 1,630,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1383` | 1,050,000.00 USD | 1,050,000.00 USD | 12,820.00 USD | 3,530.00 USD | 5,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 1,610,000.00 USD | 1,610,000.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 5,340.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1386` | 1,030,000.00 USD | 1,030,000.00 USD | 11,810.00 USD | 2,090.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 1,600,000.00 USD | 1,600,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1389` | 1,010,000.00 USD | 1,010,000.00 USD | 17,640.00 USD | 524.77 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1392` | 993,320.00 USD | 993,320.00 USD | 0.00 USD | 1,440.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1395` | 990,850.00 USD | 990,850.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,710.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1398` | 984,630.00 USD | 984,630.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 1,560,000.00 USD | 1,560,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1401` | 972,020.00 USD | 972,020.00 USD | 1,990.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1404` | 967,920.00 USD | 967,920.00 USD | 0.00 USD | 966.86 USD | 2,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 1,540,000.00 USD | 1,540,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,800.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1410` | 964,950.00 USD | 964,950.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1413` | 963,880.00 USD | 963,880.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 75,150.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1422` | 961,480.00 USD | 961,480.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 490,800.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1434` | 948,730.00 USD | 948,730.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,330.00 USD | 921,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1440` | 1,510,000.00 USD | 1,510,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1443` | 944,840.00 USD | 944,840.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 1,490,000.00 USD | 1,490,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 53,790.00 USD | 902,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1452` | 942,700.00 USD | 942,700.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 106.39 USD | 848,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1464` | 939,710.00 USD | 939,710.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 47,190.00 USD | 848,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1467` | 937,720.00 USD | 937,720.00 USD | 3,740.00 USD | 2,700.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 1,450,000.00 USD | 1,450,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 925,610.00 USD | 925,610.00 USD | 8,350.00 USD | 4,180.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 1,420,000.00 USD | 1,420,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 907,880.00 USD | 907,880.00 USD | 20,060.00 USD | 10,370.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 73,750.00 USD | 801,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 852,710.00 USD | 852,710.00 USD | 49,490.00 USD | 11,390.00 USD | 6,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1476` | 1,390,000.00 USD | 1,390,000.00 USD | 49,830.00 USD | 20,180.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 785,090.00 USD | 785,090.00 USD | 85,430.00 USD | 14,840.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 1,310,000.00 USD | 1,310,000.00 USD | 50,400.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 680,900.00 USD | 680,900.00 USD | 18,660.00 USD | 6,350.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 1,170,000.00 USD | 1,170,000.00 USD | 47,020.00 USD | 16,640.00 USD | 43,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 643,630.00 USD | 643,630.00 USD | 13,550.00 USD | 3,320.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,650.00 USD | 727,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1488` | 618,920.00 USD | 618,920.00 USD | 2,660.00 USD | 5,180.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,060,000.00 USD | 1,060,000.00 USD | 24,980.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 603,820.00 USD | 603,820.00 USD | 21,950.00 USD | 10,490.00 USD | 6,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 998,160.00 USD | 998,160.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 564,500.00 USD | 564,500.00 USD | 25,050.00 USD | 5,270.00 USD | 2,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 35,860.00 USD | 724,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 901,010.00 USD | 901,010.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 531,670.00 USD | 531,670.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 529,140.00 USD | 529,140.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 830,580.00 USD | 830,580.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 523,110.00 USD | 523,110.00 USD | 25,000.00 USD | 15,920.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 738,520.00 USD | 738,520.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 102,290.00 USD | 689,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 431,340.00 USD | 431,340.00 USD | 57,660.00 USD | 27,330.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 653,740.00 USD | 653,740.00 USD | 115,630.00 USD | 16,820.00 USD | 104,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 338,630.00 USD | 338,630.00 USD | 106,680.00 USD | 3,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 228,010.00 USD | 228,010.00 USD | 88,190.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 416,770.00 USD | 416,770.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 132,960.00 USD | 132,960.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 9,900.00 USD | 586,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1516` | 257,210.00 USD | 257,210.00 USD | 0.00 USD | 13,330.00 USD | 61,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 128,600.00 USD | 128,600.00 USD | 24,410.00 USD | 10,080.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 182,610.00 USD | 182,610.00 USD | 0.00 USD | 22,090.00 USD | 87,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 69,380.00 USD | 69,380.00 USD | 38,050.00 USD | 1,470.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 18,530.00 USD | 18,530.00 USD | 0.00 USD | 2,970.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 73,470.00 USD | 73,470.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 42,800.00 USD | 576,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1527` | 8,410.00 USD | 8,410.00 USD | 0.00 USD | 0.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 51,200.00 USD | 51,200.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 17,260.00 USD | 17,260.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 189,960.00 USD | 534,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1536` | 8,570.00 USD | 8,570.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1536` | 17,140.00 USD | 17,140.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1540` | 35,360.00 USD | 35,360.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1542` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1544` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1545` | 6,220.00 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 26,170.00 USD | 344,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1548` | 61,520.00 USD | 61,520.00 USD | 0.00 USD | 22,180.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1548` | 41,820.00 USD | 41,820.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1551` | 69,560.00 USD | 69,560.00 USD | 0.00 USD | 4,140.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1552` | 53,630.00 USD | 53,630.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1554` | 76,750.00 USD | 76,750.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 39,570.00 USD | 317,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1557` | 84,020.00 USD | 84,020.00 USD | 0.00 USD | 0.00 USD | 7,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1560` | 89,600.00 USD | 89,600.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1560` | 64,620.00 USD | 64,620.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1563` | 105,650.00 USD | 105,650.00 USD | 0.00 USD | 0.00 USD | 16,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1564` | 122,670.00 USD | 122,670.00 USD | 24,300.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 23,920.00 USD | 278,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1566` | 260,430.00 USD | 260,430.00 USD | 70,290.00 USD | 13,270.00 USD | 71,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1568` | 239,210.00 USD | 239,210.00 USD | 101,180.00 USD | 15,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1569` | 370,140.00 USD | 370,140.00 USD | 82,020.00 USD | 20,660.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1572` | 507,720.00 USD | 507,720.00 USD | 137,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1572` | 524,820.00 USD | 524,820.00 USD | 187,220.00 USD | 39,540.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1575` | 533,690.00 USD | 533,690.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1575` | 4,940.00 USD | 254,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1576` | 693,330.00 USD | 693,330.00 USD | 44,680.00 USD | 123,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1580` | 924,360.00 USD | 924,360.00 USD | 129,940.00 USD | 101,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1584` | 562,290.00 USD | 562,290.00 USD | 28,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1584` | 1,050,000.00 USD | 1,050,000.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1585` | 5,760.00 USD | 249,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1587` | 621,840.00 USD | 621,840.00 USD | 15,100.00 USD | 22,970.00 USD | 21,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1588` | 1,160,000.00 USD | 1,160,000.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1590` | 666,110.00 USD | 666,110.00 USD | 0.00 USD | 27,950.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1592` | 1,350,000.00 USD | 1,350,000.00 USD | 127,590.00 USD | 64,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1593` | 703,220.00 USD | 703,220.00 USD | 0.00 USD | 6,320.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1595` | 63,000.00 USD | 243,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1596` | 761,150.00 USD | 761,150.00 USD | 10,700.00 USD | 19,800.00 USD | 27,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1596` | 1,630,000.00 USD | 1,630,000.00 USD | 174,510.00 USD | 98,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1599` | 809,640.00 USD | 809,640.00 USD | 26,110.00 USD | 22,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1600` | 1,980,000.00 USD | 1,980,000.00 USD | 271,880.00 USD | 60,710.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1602` | 915,710.00 USD | 915,710.00 USD | 106,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1604` | 2,650,000.00 USD | 2,650,000.00 USD | 242,660.00 USD | 112,090.00 USD | 313,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1605` | 982,980.00 USD | 982,980.00 USD | 67,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1605` | 37,640.00 USD | 180,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1608` | 999,140.00 USD | 999,140.00 USD | 0.00 USD | 0.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,270,000.00 USD | 3,270,000.00 USD | 208,080.00 USD | 240,680.00 USD | 172,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1611` | 1,110,000.00 USD | 1,110,000.00 USD | 20,140.00 USD | 11,530.00 USD | 83,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,190,000.00 USD | 4,190,000.00 USD | 304,970.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1614` | 1,170,000.00 USD | 1,170,000.00 USD | 14,300.00 USD | 0.00 USD | 39,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1615` | 17,290.00 USD | 143,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1616` | 4,730,000.00 USD | 4,730,000.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1617` | 1,210,000.00 USD | 1,210,000.00 USD | 31,470.00 USD | 7,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1620` | 1,350,000.00 USD | 1,350,000.00 USD | 85,250.00 USD | 57,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1623` | 1,470,000.00 USD | 1,470,000.00 USD | 53,880.00 USD | 67,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1625` | 106,340.00 USD | 125,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1626` | 1,540,000.00 USD | 1,540,000.00 USD | 51,630.00 USD | 12,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1632` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1635` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,230.00 USD | 19,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1638` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1641` | 1,610,000.00 USD | 1,610,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1644` | 1,680,000.00 USD | 1,680,000.00 USD | 25,030.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1645` | 6,190.00 USD | 18,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1655` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1656` | 1,740,000.00 USD | 1,740,000.00 USD | 9,730.00 USD | 40,450.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,280,000.00 USD | 5,280,000.00 USD | 40,780.00 USD | 11,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 1,800,000.00 USD | 1,800,000.00 USD | 8,220.00 USD | 6,760.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 5,540,000.00 USD | 5,540,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 1,900,000.00 USD | 1,900,000.00 USD | 22,170.00 USD | 5,570.00 USD | 80,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1668` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 5,340.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 5,720,000.00 USD | 5,720,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 1,950,000.00 USD | 1,950,000.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 5,920,000.00 USD | 5,920,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 2,020,000.00 USD | 2,020,000.00 USD | 45,910.00 USD | 2,010.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 6,140,000.00 USD | 6,140,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 2,040,000.00 USD | 2,040,000.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 2,120,000.00 USD | 2,120,000.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,360,000.00 USD | 6,360,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 2,240,000.00 USD | 2,240,000.00 USD | 99,440.00 USD | 3,200.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 6,440,000.00 USD | 6,440,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1686` | 2,310,000.00 USD | 2,310,000.00 USD | 6,560.00 USD | 29,250.00 USD | 33,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 6,980.00 USD | 4,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 2,490,000.00 USD | 2,490,000.00 USD | 82,220.00 USD | 69,050.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 6,600,000.00 USD | 6,600,000.00 USD | 33,660.00 USD | 70,740.00 USD | 40,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 2,550,000.00 USD | 2,550,000.00 USD | 24,260.00 USD | 25,080.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1696` | 6,740,000.00 USD | 6,740,000.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 2,640,000.00 USD | 2,640,000.00 USD | 37,080.00 USD | 56,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 25,330.00 USD | 41,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 6,910,000.00 USD | 6,910,000.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,800,000.00 USD | 2,800,000.00 USD | 53,700.00 USD | 71,860.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1716` | 2,880,000.00 USD | 2,880,000.00 USD | 9,570.00 USD | 25,600.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,930,000.00 USD | 2,930,000.00 USD | 34,230.00 USD | 10,110.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 3,100,000.00 USD | 3,100,000.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 7,540,000.00 USD | 7,540,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 3,140,000.00 USD | 3,140,000.00 USD | 8,230.00 USD | 2,410.00 USD | 33,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 3,160,000.00 USD | 3,160,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 8,030,000.00 USD | 8,030,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 3,170,000.00 USD | 3,170,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 3,230,000.00 USD | 3,230,000.00 USD | 33,580.00 USD | 11,810.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 3,270,000.00 USD | 3,270,000.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 8,210,000.00 USD | 8,210,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 3,390,000.00 USD | 3,390,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 3,450,000.00 USD | 3,450,000.00 USD | 27,740.00 USD | 0.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 271,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,530,000.00 USD | 3,530,000.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1755` | 600.46 USD | 6,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1756` | 8,770,000.00 USD | 8,770,000.00 USD | 97,570.00 USD | 0.00 USD | 186,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 3,680,000.00 USD | 3,680,000.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 9,160,000.00 USD | 9,160,000.00 USD | 277,910.00 USD | 77,870.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,870,000.00 USD | 3,870,000.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 4,000,000.00 USD | 4,000,000.00 USD | 34,410.00 USD | 27,980.00 USD | 61,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 9,830,000.00 USD | 9,830,000.00 USD | 353,950.00 USD | 282,090.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1765` | 339.06 USD | 6,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1767` | 4,130,000.00 USD | 4,130,000.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 10,210,000.00 USD | 10,210,000.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 4,250,000.00 USD | 4,250,000.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 10,480,000.00 USD | 10,480,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 4,320,000.00 USD | 4,320,000.00 USD | 15,040.00 USD | 28,980.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 4,400,000.00 USD | 4,400,000.00 USD | 38,630.00 USD | 19,390.00 USD | 21,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 10,730,000.00 USD | 10,730,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 4,530,000.00 USD | 4,530,000.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 10,990,000.00 USD | 10,990,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 4,610,000.00 USD | 4,610,000.00 USD | 46,310.00 USD | 14,240.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,210,000.00 USD | 11,210,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,760,000.00 USD | 4,760,000.00 USD | 96,920.00 USD | 39,090.00 USD | 14,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 4,850,000.00 USD | 4,850,000.00 USD | 18,550.00 USD | 37,940.00 USD | 36,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 11,380,000.00 USD | 11,380,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,920,000.00 USD | 4,920,000.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 11,610,000.00 USD | 11,610,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 5,030,000.00 USD | 5,030,000.00 USD | 41,300.00 USD | 49,090.00 USD | 15,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 48,610.00 USD | 55,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1796` | 11,700,000.00 USD | 11,700,000.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 5,110,000.00 USD | 5,110,000.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 5,150,000.00 USD | 5,150,000.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 11,820,000.00 USD | 11,820,000.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 5,210,000.00 USD | 5,210,000.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 11,910,000.00 USD | 11,910,000.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,130.00 USD | 58,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1806` | 5,250,000.00 USD | 5,250,000.00 USD | 9,910.00 USD | 14,370.00 USD | 15,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 12,090,000.00 USD | 12,090,000.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 5,300,000.00 USD | 5,300,000.00 USD | 17,680.00 USD | 27,370.00 USD | 7,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 5,390,000.00 USD | 5,390,000.00 USD | 23,530.00 USD | 37,720.00 USD | 22,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 12,230,000.00 USD | 12,230,000.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 5,420,000.00 USD | 5,420,000.00 USD | 13,550.00 USD | 3,320.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 8,150.00 USD | 66,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1816` | 12,380,000.00 USD | 12,380,000.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 5,480,000.00 USD | 5,480,000.00 USD | 37,120.00 USD | 11,780.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 12,540,000.00 USD | 12,540,000.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 5,530,000.00 USD | 5,530,000.00 USD | 21,220.00 USD | 15,970.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 5,570,000.00 USD | 5,570,000.00 USD | 14,850.00 USD | 15,990.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 12,750,000.00 USD | 12,750,000.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 5,610,000.00 USD | 5,610,000.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 12,930,000.00 USD | 12,930,000.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 13,140,000.00 USD | 13,140,000.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 5,620,000.00 USD | 5,620,000.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1836` | 5,630,000.00 USD | 5,630,000.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 13,480,000.00 USD | 13,480,000.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 13,820,000.00 USD | 13,820,000.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1842` | 5,650,000.00 USD | 5,650,000.00 USD | 5,430.00 USD | 4,660.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 14,020,000.00 USD | 14,020,000.00 USD | 94,510.00 USD | 20,390.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1845` | 5,670,000.00 USD | 5,670,000.00 USD | 10,860.00 USD | 7,090.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1848` | 5,690,000.00 USD | 5,690,000.00 USD | 5,910.00 USD | 4,360.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 14,170,000.00 USD | 14,170,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1851` | 5,700,000.00 USD | 5,700,000.00 USD | 6,220.00 USD | 1,730.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 14,620,000.00 USD | 14,620,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1854` | 5,710,000.00 USD | 5,710,000.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 14,840,000.00 USD | 14,840,000.00 USD | 100,160.00 USD | 21,030.00 USD | 106,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1857` | 5,730,000.00 USD | 5,730,000.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1860` | 5,750,000.00 USD | 5,750,000.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 15,100,000.00 USD | 15,100,000.00 USD | 64,600.00 USD | 59,290.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1863` | 5,760,000.00 USD | 5,760,000.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 15,250,000.00 USD | 15,250,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1866` | 5,770,000.00 USD | 5,770,000.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 15,490,000.00 USD | 15,490,000.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1869` | 5,790,000.00 USD | 5,790,000.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1872` | 5,810,000.00 USD | 5,810,000.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 15,990,000.00 USD | 15,990,000.00 USD | 188,990.00 USD | 158,170.00 USD | 155,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1875` | 5,820,000.00 USD | 5,820,000.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1875` | 21,190.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1876` | 16,140,000.00 USD | 16,140,000.00 USD | 65,910.00 USD | 34,900.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1878` | 5,830,000.00 USD | 5,830,000.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 16,260,000.00 USD | 16,260,000.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1881` | 5,840,000.00 USD | 5,840,000.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1883` | 5,840,000.00 USD | 5,840,000.00 USD | 1,710.00 USD | 1,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1884` | 16,320,000.00 USD | 16,320,000.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1888` | 16,450,000.00 USD | 16,450,000.00 USD | 22,970.00 USD | 17,330.00 USD | 88,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1892` | 16,540,000.00 USD | 16,540,000.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1895` | 3,550.00 USD | 91,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1896` | 16,620,000.00 USD | 16,620,000.00 USD | 42,320.00 USD | 17,300.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1900` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1904` | 16,710,000.00 USD | 16,710,000.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1908` | 16,850,000.00 USD | 16,850,000.00 USD | 33,940.00 USD | 50,270.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1912` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1916` | 16,890,000.00 USD | 16,890,000.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 16,920,000.00 USD | 16,920,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 16,940,000.00 USD | 16,940,000.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 16,950,000.00 USD | 16,950,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 1,310.00 USD | 92,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 860.20 USD | 93,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1956` | 16,970,000.00 USD | 16,970,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 16,970,000.00 USD | 16,970,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 16,990,000.00 USD | 16,990,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 93,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1995` | 135.22 USD | 93,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 764.66 USD | 94,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2045` | 399.22 USD | 94,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 106,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 106,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 1,060.00 USD | 107,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 16,070.00 USD | 123,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 164,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 131,700.00 USD | 296,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 26,940.00 USD | 323,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 323,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 330,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 16,250.00 USD | 346,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 346,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 347,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 869.00 USD | 348,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 348,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 9,360.00 USD | 357,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2485` | 21,600.00 USD | 379,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 379,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 383,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 29,500.00 USD | 413,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,030.00 USD | 465,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 465,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 465,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 479,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 479,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 507,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2755` | 438.18 USD | 507,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 508,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 508,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 2,230.00 USD | 510,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 574.36 USD | 511,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 17,550.00 USD | 528,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 225.42 USD | 529,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3165` | 63,300.00 USD | 592,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 9,540.00 USD | 601,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 192.68 USD | 602,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3325` | 148.36 USD | 602,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 258.73 USD | 602,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 63,220.00 USD | 665,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0345` | 2,320,000.00 USD | 0.00 USD | 1,180.00 USD | `-79.50%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0375` | 2,320,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.72%` | `58,778,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 2,310,000.00 USD | 0.00 USD | 1,490.00 USD | `-77.13%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0395` | 2,310,000.00 USD | 0.00 USD | 138,900.00 USD | `-76.53%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0415` | 2,170,000.00 USD | 0.00 USD | 408.10 USD | `-75.34%` | `9,833,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 2,170,000.00 USD | 0.00 USD | 170.00 USD | `-74.75%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0445` | 2,170,000.00 USD | 0.00 USD | 8,100.00 USD | `-73.56%` | `181,960,400,000,000.00` |
| `Live` | `Long` | `0.0455` | 2,160,000.00 USD | 0.00 USD | 3,090.00 USD | `-72.97%` | `67,875,300,000,000.00` |
| `Live` | `Long` | `0.0475` | 2,160,000.00 USD | 0.00 USD | 4,840.00 USD | `-71.78%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 2,160,000.00 USD | 0.00 USD | 400.94 USD | `-70.59%` | `8,099,700,000,000.00` |
| `Live` | `Long` | `0.0525` | 2,160,000.00 USD | 0.00 USD | 289.43 USD | `-68.81%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 2,160,000.00 USD | 0.00 USD | 668.38 USD | `-68.22%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 2,160,000.00 USD | 0.00 USD | 7,100.00 USD | `-67.62%` | `130,366,100,000,000.00` |
| `Live` | `Long` | `0.0565` | 2,150,000.00 USD | 0.00 USD | 18,660.00 USD | `-66.43%` | `330,349,600,000,000.00` |
| `Live` | `Long` | `0.0605` | 2,130,000.00 USD | 0.00 USD | 148.49 USD | `-64.06%` | `2,454,400,000,000.00` |
| `Live` | `Long` | `0.0625` | 2,130,000.00 USD | 0.00 USD | 187.50 USD | `-62.87%` | `3,000,000,000,000.00` |
| `Live` | `Long` | `0.0645` | 2,130,000.00 USD | 0.00 USD | 283.15 USD | `-61.68%` | `4,389,900,000,000.00` |
| `Live` | `Long` | `0.0675` | 2,130,000.00 USD | 0.00 USD | 100,530.00 USD | `-59.90%` | `1,489,314,300,000,000.00` |
| `Live` | `Long` | `0.0685` | 2,030,000.00 USD | 0.00 USD | 590.45 USD | `-59.30%` | `8,619,700,000,000.00` |
| `Live` | `Long` | `0.0695` | 2,030,000.00 USD | 0.00 USD | 77,980.00 USD | `-58.71%` | `1,122,070,000,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,950,000.00 USD | 0.00 USD | 3,260.00 USD | `-58.12%` | `46,211,100,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,950,000.00 USD | 0.00 USD | 5,840.00 USD | `-57.52%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,940,000.00 USD | 0.00 USD | 111.58 USD | `-56.93%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,940,000.00 USD | 0.00 USD | 2,440.00 USD | `-56.33%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,940,000.00 USD | 0.00 USD | 2,370.00 USD | `-55.74%` | `31,857,600,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,940,000.00 USD | 0.00 USD | 368.95 USD | `-55.14%` | `4,886,800,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,940,000.00 USD | 0.00 USD | 14,690.00 USD | `-54.55%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,920,000.00 USD | 0.00 USD | 27,480.00 USD | `-53.36%` | `350,000,000,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,890,000.00 USD | 0.00 USD | 6,180.00 USD | `-52.77%` | `77,676,300,000,000.00` |
| `Live` | `Long` | `0.0805` | 1,890,000.00 USD | 0.00 USD | 6,040.00 USD | `-52.17%` | `75,000,000,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,880,000.00 USD | 0.00 USD | 7,840.00 USD | `-51.58%` | `96,199,600,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,870,000.00 USD | 0.00 USD | 13,950.00 USD | `-50.99%` | `169,093,500,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,860,000.00 USD | 0.00 USD | 751.50 USD | `-50.39%` | `9,000,000,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,860,000.00 USD | 0.00 USD | 19,010.00 USD | `-49.80%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,840,000.00 USD | 0.00 USD | 22,430.00 USD | `-48.02%` | `256,311,700,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,820,000.00 USD | 0.00 USD | 362.62 USD | `-47.42%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,820,000.00 USD | 0.00 USD | 12,960.00 USD | `-46.83%` | `144,809,100,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,800,000.00 USD | 0.00 USD | 1,320.00 USD | `-46.23%` | `14,542,300,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,800,000.00 USD | 0.00 USD | 4,130.00 USD | `-45.05%` | `44,668,100,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,800,000.00 USD | 0.00 USD | 814.24 USD | `-44.45%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,800,000.00 USD | 0.00 USD | 4,090.00 USD | `-43.86%` | `43,276,200,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,790,000.00 USD | 0.00 USD | 589.63 USD | `-42.67%` | `6,110,200,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,790,000.00 USD | 0.00 USD | 145.24 USD | `-42.07%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,790,000.00 USD | 0.00 USD | 5,970.00 USD | `-41.48%` | `60,604,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,790,000.00 USD | 0.00 USD | 9,200.00 USD | `-40.89%` | `92,500,600,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,780,000.00 USD | 0.00 USD | 12,790.00 USD | `-40.29%` | `127,282,000,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,760,000.00 USD | 0.00 USD | 811.82 USD | `-39.10%` | `7,920,200,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,760,000.00 USD | 0.00 USD | 802.14 USD | `-38.51%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,760,000.00 USD | 0.00 USD | 6,700.00 USD | `-37.92%` | `64,126,500,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,760,000.00 USD | 0.00 USD | 12,770.00 USD | `-37.32%` | `121,051,500,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,740,000.00 USD | 0.00 USD | 181.20 USD | `-36.73%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,740,000.00 USD | 0.00 USD | 1,650.00 USD | `-36.13%` | `15,369,200,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,740,000.00 USD | 0.00 USD | 342.59 USD | `-35.54%` | `3,157,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,740,000.00 USD | 0.00 USD | 534.49 USD | `-34.35%` | `4,837,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,740,000.00 USD | 0.00 USD | 425.50 USD | `-33.76%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,740,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.16%` | `19,462,500,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,740,000.00 USD | 0.00 USD | 1,360.00 USD | `-32.57%` | `11,975,200,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,740,000.00 USD | 0.00 USD | 8,950.00 USD | `-31.97%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,730,000.00 USD | 0.00 USD | 16,170.00 USD | `-31.38%` | `140,005,200,000,000.02` |
| `Live` | `Long` | `0.1165` | 1,710,000.00 USD | 0.00 USD | 11,120.00 USD | `-30.79%` | `95,487,400,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,700,000.00 USD | 0.00 USD | 1,760.00 USD | `-30.19%` | `14,957,100,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,700,000.00 USD | 0.00 USD | 26,260.00 USD | `-29.60%` | `221,634,600,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,670,000.00 USD | 0.00 USD | 6,210.00 USD | `-29.00%` | `51,981,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,670,000.00 USD | 0.00 USD | 14,190.00 USD | `-27.82%` | `116,753,600,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,650,000.00 USD | 0.00 USD | 8,920.00 USD | `-27.22%` | `72,830,700,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,640,000.00 USD | 0.00 USD | 34,620.00 USD | `-26.63%` | `280,295,400,000,000.03` |
| `Live` | `Long` | `0.1245` | 1,610,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.03%` | `24,990,900,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,610,000.00 USD | 0.00 USD | 4,960.00 USD | `-25.44%` | `39,542,400,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,600,000.00 USD | 0.00 USD | 1,200.00 USD | `-24.85%` | `9,489,700,000,000.00` |
| `Live` | `Long` | `0.1275` | 1,600,000.00 USD | 0.00 USD | 4,190.00 USD | `-24.25%` | `32,824,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 1,600,000.00 USD | 0.00 USD | 11,100.00 USD | `-23.66%` | `86,356,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 1,580,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.06%` | `30,998,800,000,000.00` |
| `Live` | `Long` | `0.1305` | 1,580,000.00 USD | 0.00 USD | 13,600.00 USD | `-22.47%` | `104,183,100,000,000.00` |
| `Live` | `Long` | `0.1315` | 1,570,000.00 USD | 0.00 USD | 10,500.00 USD | `-21.87%` | `79,839,800,000,000.00` |
| `Live` | `Long` | `0.1325` | 1,560,000.00 USD | 0.00 USD | 8,090.00 USD | `-21.28%` | `61,058,900,000,000.00` |
| `Live` | `Long` | `0.1335` | 1,550,000.00 USD | 0.00 USD | 26,200.00 USD | `-20.69%` | `196,263,500,000,000.00` |
| `Live` | `Long` | `0.1345` | 1,520,000.00 USD | 0.00 USD | 2,970.00 USD | `-20.09%` | `22,103,800,000,000.00` |
| `Live` | `Long` | `0.1365` | 1,520,000.00 USD | 0.00 USD | 2,740.00 USD | `-18.90%` | `20,075,400,000,000.00` |
| `Live` | `Long` | `0.1375` | 1,520,000.00 USD | 0.00 USD | 13,750.00 USD | `-18.31%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.1385` | 1,500,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.72%` | `38,544,200,000,000.00` |
| `Live` | `Long` | `0.1395` | 1,500,000.00 USD | 0.00 USD | 6,710.00 USD | `-17.12%` | `48,115,200,000,000.00` |
| `Live` | `Long` | `0.1405` | 1,490,000.00 USD | 0.00 USD | 2,800.00 USD | `-16.53%` | `19,894,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 1,490,000.00 USD | 0.00 USD | 75,150.00 USD | `-15.93%` | `531,086,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 1,410,000.00 USD | 0.00 USD | 490,800.00 USD | `-15.34%` | `3,444,196,100,000,000.00` |
| `Live` | `Long` | `0.1435` | 921,750.00 USD | 0.00 USD | 19,330.00 USD | `-14.75%` | `134,671,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 902,420.00 USD | 0.00 USD | 53,790.00 USD | `-14.15%` | `372,262,000,000,000.00` |
| `Live` | `Long` | `0.1455` | 848,630.00 USD | 0.00 USD | 106.39 USD | `-13.56%` | `731,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 848,520.00 USD | 0.00 USD | 47,190.00 USD | `-12.96%` | `322,108,600,000,000.00` |
| `Live` | `Long` | `0.1475` | 801,340.00 USD | 0.00 USD | 73,750.00 USD | `-12.37%` | `500,000,000,000,000.00` |
| `Live` | `Long` | `0.1485` | 727,590.00 USD | 0.00 USD | 2,650.00 USD | `-11.78%` | `17,872,100,000,000.00` |
| `Live` | `Long` | `0.1495` | 724,930.00 USD | 0.00 USD | 35,860.00 USD | `-11.18%` | `239,861,300,000,000.00` |
| `Live` | `Long` | `0.1505` | 689,070.00 USD | 0.00 USD | 102,290.00 USD | `-10.59%` | `679,673,200,000,000.00` |
| `Live` | `Long` | `0.1515` | 586,780.00 USD | 0.00 USD | 9,900.00 USD | `-9.99%` | `65,345,600,000,000.00` |
| `Live` | `Long` | `0.1525` | 576,880.00 USD | 0.00 USD | 42,800.00 USD | `-9.40%` | `280,626,000,000,000.00` |
| `Live` | `Long` | `0.1535` | 534,090.00 USD | 0.00 USD | 189,960.00 USD | `-8.80%` | `1,237,517,800,000,000.00` |
| `Live` | `Long` | `0.1545` | 344,130.00 USD | 0.00 USD | 26,170.00 USD | `-8.21%` | `169,378,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 317,960.00 USD | 0.00 USD | 39,570.00 USD | `-7.62%` | `254,462,900,000,000.00` |
| `Live` | `Long` | `0.1565` | 278,390.00 USD | 0.00 USD | 23,920.00 USD | `-7.02%` | `152,866,400,000,000.00` |
| `Live` | `Long` | `0.1575` | 254,470.00 USD | 0.00 USD | 4,940.00 USD | `-6.43%` | `31,351,900,000,000.00` |
| `Live` | `Long` | `0.1585` | 249,530.00 USD | 0.00 USD | 5,760.00 USD | `-5.83%` | `36,335,900,000,000.00` |
| `Live` | `Long` | `0.1595` | 243,770.00 USD | 0.00 USD | 63,000.00 USD | `-5.24%` | `395,011,700,000,000.00` |
| `Live` | `Long` | `0.1605` | 180,760.00 USD | 0.00 USD | 37,640.00 USD | `-4.65%` | `234,510,900,000,000.00` |
| `Live` | `Long` | `0.1615` | 143,120.00 USD | 0.00 USD | 17,290.00 USD | `-4.05%` | `107,085,500,000,000.00` |
| `Live` | `Long` | `0.1625` | 125,830.00 USD | 0.00 USD | 106,340.00 USD | `-3.46%` | `654,420,200,000,000.00` |
| `Live` | `Long` | `0.1635` | 19,490.00 USD | 0.00 USD | 1,230.00 USD | `-2.86%` | `7,496,400,000,000.00` |
| `Live` | `Long` | `0.1645` | 18,260.00 USD | 0.00 USD | 6,190.00 USD | `-2.27%` | `37,630,200,000,000.00` |
| `Live` | `Long` | `0.1655` | 12,070.00 USD | 0.00 USD | 12,070.00 USD | `-1.68%` | `72,938,600,000,000.00` |
| `Live` | `Short` | `0.1685` | 5,550.00 USD | 5,550.00 USD | 0.00 USD | `+0.11%` | `32,933,400,000,000.00` |
| `Live` | `Short` | `0.1755` | 6,150.00 USD | 600.46 USD | 0.00 USD | `+4.27%` | `3,421,400,000,000.00` |
| `Live` | `Short` | `0.1765` | 6,490.00 USD | 339.06 USD | 0.00 USD | `+4.86%` | `1,921,000,000,000.00` |
| `Live` | `Short` | `0.1795` | 55,100.00 USD | 48,610.00 USD | 0.00 USD | `+6.64%` | `270,803,800,000,000.00` |
| `Live` | `Short` | `0.1805` | 58,220.00 USD | 3,130.00 USD | 0.00 USD | `+7.24%` | `17,317,400,000,000.00` |
| `Live` | `Short` | `0.1815` | 66,380.00 USD | 8,150.00 USD | 0.00 USD | `+7.83%` | `44,917,400,000,000.00` |
| `Live` | `Short` | `0.1875` | 87,560.00 USD | 21,190.00 USD | 0.00 USD | `+11.39%` | `112,997,300,000,000.00` |
| `Live` | `Short` | `0.1895` | 91,110.00 USD | 3,550.00 USD | 0.00 USD | `+12.58%` | `18,740,300,000,000.00` |
| `Live` | `Short` | `0.1945` | 92,430.00 USD | 1,310.00 USD | 0.00 USD | `+15.55%` | `6,741,400,000,000.00` |
| `Live` | `Short` | `0.1955` | 93,290.00 USD | 860.20 USD | 0.00 USD | `+16.15%` | `4,400,000,000,000.00` |
| `Live` | `Short` | `0.1975` | 93,440.00 USD | 150.10 USD | 0.00 USD | `+17.34%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.1995` | 93,570.00 USD | 135.22 USD | 0.00 USD | `+18.52%` | `677,800,000,000.00` |
| `Live` | `Short` | `0.2025` | 94,340.00 USD | 764.66 USD | 0.00 USD | `+20.31%` | `3,776,100,000,000.00` |
| `Live` | `Short` | `0.2045` | 94,740.00 USD | 399.22 USD | 0.00 USD | `+21.49%` | `1,952,200,000,000.00` |
| `Live` | `Short` | `0.2055` | 106,330.00 USD | 11,590.00 USD | 0.00 USD | `+22.09%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 106,530.00 USD | 198.08 USD | 0.00 USD | `+23.87%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 107,580.00 USD | 1,060.00 USD | 0.00 USD | `+24.47%` | `5,056,300,000,000.00` |
| `Live` | `Short` | `0.2135` | 123,660.00 USD | 16,070.00 USD | 0.00 USD | `+26.84%` | `75,287,100,000,000.00` |
| `Live` | `Short` | `0.2155` | 164,990.00 USD | 41,330.00 USD | 0.00 USD | `+28.03%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2195` | 296,690.00 USD | 131,700.00 USD | 0.00 USD | `+30.41%` | `600,003,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 323,630.00 USD | 26,940.00 USD | 0.00 USD | `+32.78%` | `120,527,600,000,000.00` |
| `Live` | `Short` | `0.2255` | 323,790.00 USD | 154.78 USD | 0.00 USD | `+33.97%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 330,610.00 USD | 6,820.00 USD | 0.00 USD | `+36.35%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 346,860.00 USD | 16,250.00 USD | 0.00 USD | `+39.91%` | `69,017,500,000,000.00` |
| `Live` | `Short` | `0.2375` | 346,960.00 USD | 102.62 USD | 0.00 USD | `+41.10%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2405` | 347,330.00 USD | 361.66 USD | 0.00 USD | `+42.88%` | `1,503,800,000,000.00` |
| `Live` | `Short` | `0.2425` | 348,190.00 USD | 869.00 USD | 0.00 USD | `+44.07%` | `3,583,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 348,430.00 USD | 231.03 USD | 0.00 USD | `+45.26%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 357,790.00 USD | 9,360.00 USD | 0.00 USD | `+46.45%` | `37,972,200,000,000.00` |
| `Live` | `Short` | `0.2485` | 379,380.00 USD | 21,600.00 USD | 0.00 USD | `+47.64%` | `86,908,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 379,930.00 USD | 546.54 USD | 0.00 USD | `+51.20%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 383,790.00 USD | 3,870.00 USD | 0.00 USD | `+52.39%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 413,290.00 USD | 29,500.00 USD | 0.00 USD | `+52.98%` | `114,561,100,000,000.00` |
| `Live` | `Short` | `0.2585` | 465,320.00 USD | 52,030.00 USD | 0.00 USD | `+53.58%` | `201,260,100,000,000.00` |
| `Live` | `Short` | `0.2615` | 465,470.00 USD | 154.94 USD | 0.00 USD | `+55.36%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 465,700.00 USD | 226.51 USD | 0.00 USD | `+59.52%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 479,210.00 USD | 13,510.00 USD | 0.00 USD | `+61.30%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 479,430.00 USD | 214.21 USD | 0.00 USD | `+61.89%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 507,320.00 USD | 27,890.00 USD | 0.00 USD | `+63.08%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2755` | 507,760.00 USD | 438.18 USD | 0.00 USD | `+63.68%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2795` | 508,240.00 USD | 482.84 USD | 0.00 USD | `+66.05%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 508,430.00 USD | 187.26 USD | 0.00 USD | `+73.18%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 510,650.00 USD | 2,230.00 USD | 0.00 USD | `+73.78%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2955` | 511,230.00 USD | 574.36 USD | 0.00 USD | `+75.56%` | `1,943,700,000,000.00` |
| `Live` | `Short` | `0.2985` | 528,780.00 USD | 17,550.00 USD | 0.00 USD | `+77.34%` | `58,786,700,000,000.00` |
| `Live` | `Short` | `0.3105` | 529,000.00 USD | 225.42 USD | 0.00 USD | `+84.47%` | `726,000,000,000.00` |
| `Live` | `Short` | `0.3165` | 592,300.00 USD | 63,300.00 USD | 0.00 USD | `+88.03%` | `200,000,000,000,000.00` |
| `Live` | `Short` | `0.3295` | 601,840.00 USD | 9,540.00 USD | 0.00 USD | `+95.76%` | `28,943,600,000,000.00` |
| `Live` | `Short` | `0.3305` | 602,030.00 USD | 192.68 USD | 0.00 USD | `+96.35%` | `583,000,000,000.00` |
| `Live` | `Short` | `0.3325` | 602,180.00 USD | 148.36 USD | 0.00 USD | `+97.54%` | `446,200,000,000.00` |
| `Live` | `Short` | `0.3335` | 602,440.00 USD | 258.73 USD | 0.00 USD | `+98.13%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3365` | 665,660.00 USD | 63,220.00 USD | 0.00 USD | `+99.92%` | `187,887,700,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 784,250.00 USD | 0.00 USD | 355.00 USD | `-78.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 783,890.00 USD | 0.00 USD | 600.79 USD | `-74.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 783,290.00 USD | 0.00 USD | 353.50 USD | `-70.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 782,940.00 USD | 0.00 USD | 4,310.00 USD | `-67.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 778,630.00 USD | 0.00 USD | 475.11 USD | `-62.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 778,150.00 USD | 0.00 USD | 131.16 USD | `-61.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 778,020.00 USD | 0.00 USD | 881.45 USD | `-60.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 777,140.00 USD | 0.00 USD | 1,070.00 USD | `-59.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 776,060.00 USD | 0.00 USD | 1,400.00 USD | `-59.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 774,660.00 USD | 0.00 USD | 1,010.00 USD | `-58.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 773,660.00 USD | 0.00 USD | 4,490.00 USD | `-58.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 769,160.00 USD | 0.00 USD | 529.04 USD | `-57.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 768,640.00 USD | 0.00 USD | 2,390.00 USD | `-56.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 766,250.00 USD | 0.00 USD | 757.39 USD | `-55.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 765,490.00 USD | 0.00 USD | 1,490.00 USD | `-53.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 764,000.00 USD | 0.00 USD | 277.37 USD | `-48.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 763,730.00 USD | 0.00 USD | 262.50 USD | `-48.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 763,460.00 USD | 0.00 USD | 795.57 USD | `-47.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 762,670.00 USD | 0.00 USD | 181.00 USD | `-46.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 762,490.00 USD | 0.00 USD | 1,270.00 USD | `-40.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 761,210.00 USD | 0.00 USD | 1,550.00 USD | `-39.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 759,670.00 USD | 0.00 USD | 116.07 USD | `-36.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 759,550.00 USD | 0.00 USD | 19,070.00 USD | `-35.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 740,480.00 USD | 0.00 USD | 577.22 USD | `-34.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 739,900.00 USD | 0.00 USD | 343.50 USD | `-31.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 739,560.00 USD | 0.00 USD | 26,280.00 USD | `-30.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 713,280.00 USD | 0.00 USD | 105.75 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 713,170.00 USD | 0.00 USD | 120.50 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 713,050.00 USD | 0.00 USD | 83,620.00 USD | `-27.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 629,430.00 USD | 0.00 USD | 14,940.00 USD | `-26.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 614,490.00 USD | 0.00 USD | 3,010.00 USD | `-24.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 611,480.00 USD | 0.00 USD | 473.27 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 611,010.00 USD | 0.00 USD | 220,940.00 USD | `-23.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 390,070.00 USD | 0.00 USD | 25,060.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 365,010.00 USD | 0.00 USD | 5,560.00 USD | `-21.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 359,450.00 USD | 0.00 USD | 625.78 USD | `-20.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 358,820.00 USD | 0.00 USD | 9,090.00 USD | `-20.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 349,730.00 USD | 0.00 USD | 16,260.00 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 333,470.00 USD | 0.00 USD | 700.86 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 332,770.00 USD | 0.00 USD | 108.57 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 332,660.00 USD | 0.00 USD | 349.74 USD | `-17.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 332,310.00 USD | 0.00 USD | 3,520.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 328,790.00 USD | 0.00 USD | 127.35 USD | `-15.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 328,660.00 USD | 0.00 USD | 24,850.00 USD | `-15.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 303,810.00 USD | 0.00 USD | 702.55 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 303,110.00 USD | 0.00 USD | 1,960.00 USD | `-14.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 301,150.00 USD | 0.00 USD | 27,090.00 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 274,060.00 USD | 0.00 USD | 119.66 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 273,940.00 USD | 0.00 USD | 2,290.00 USD | `-12.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 271,650.00 USD | 0.00 USD | 4,550.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 267,100.00 USD | 0.00 USD | 2,420.00 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 264,680.00 USD | 0.00 USD | 4,360.00 USD | `-10.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 260,320.00 USD | 0.00 USD | 702.05 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 259,620.00 USD | 0.00 USD | 204.57 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 259,410.00 USD | 0.00 USD | 19,280.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 240,140.00 USD | 0.00 USD | 82,840.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 157,300.00 USD | 0.00 USD | 718.79 USD | `-7.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 156,580.00 USD | 0.00 USD | 443.71 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 156,130.00 USD | 0.00 USD | 17,200.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 138,930.00 USD | 0.00 USD | 70,970.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 67,960.00 USD | 0.00 USD | 16,890.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 51,070.00 USD | 0.00 USD | 16,870.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 34,210.00 USD | 0.00 USD | 877.65 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 33,330.00 USD | 0.00 USD | 20,260.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 13,070.00 USD | 0.00 USD | 4,450.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 8,620.00 USD | 0.00 USD | 6,570.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 2,050.00 USD | 0.00 USD | 1,670.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 386.67 USD | 0.00 USD | 386.67 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 168.50 USD | 168.50 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 296.98 USD | 128.48 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 1,210.00 USD | 913.37 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 3,010.00 USD | 1,800.00 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 3,240.00 USD | 229.89 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 12,080.00 USD | 8,840.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 18,720.00 USD | 6,650.00 USD | 0.00 USD | `+3.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 20,080.00 USD | 1,350.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 28,310.00 USD | 8,230.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 28,650.00 USD | 336.40 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 125,100.00 USD | 96,460.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 152,030.00 USD | 26,930.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 153,160.00 USD | 1,130.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 163,520.00 USD | 10,360.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 164,390.00 USD | 864.12 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 166,910.00 USD | 2,520.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 167,190.00 USD | 276.75 USD | 0.00 USD | `+9.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 167,340.00 USD | 149.79 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 170,530.00 USD | 3,190.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 170,680.00 USD | 147.11 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 170,920.00 USD | 245.50 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 171,580.00 USD | 660.73 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 178,720.00 USD | 7,130.00 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 179,110.00 USD | 396.42 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 180,150.00 USD | 1,040.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 187,220.00 USD | 7,070.00 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 187,960.00 USD | 742.45 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 192,480.00 USD | 4,520.00 USD | 0.00 USD | `+16.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 192,620.00 USD | 133.19 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 192,750.00 USD | 134.20 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 197,210.00 USD | 4,460.00 USD | 0.00 USD | `+17.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 197,700.00 USD | 492.19 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 232,030.00 USD | 34,330.00 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 232,890.00 USD | 863.97 USD | 0.00 USD | `+19.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 257,530.00 USD | 24,640.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 257,710.00 USD | 182.72 USD | 0.00 USD | `+20.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 343,610.00 USD | 85,900.00 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 345,080.00 USD | 1,470.00 USD | 0.00 USD | `+22.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 345,250.00 USD | 174.20 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 347,320.00 USD | 2,080.00 USD | 0.00 USD | `+23.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 347,580.00 USD | 252.51 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 363,390.00 USD | 15,810.00 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 363,510.00 USD | 126.50 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 363,700.00 USD | 190.80 USD | 0.00 USD | `+26.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 364,420.00 USD | 713.94 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 364,630.00 USD | 213.00 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 370,910.00 USD | 6,280.00 USD | 0.00 USD | `+29.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 395,570.00 USD | 24,660.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 395,910.00 USD | 333.91 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 399,880.00 USD | 3,980.00 USD | 0.00 USD | `+32.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 400,260.00 USD | 378.55 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 400,640.00 USD | 380.23 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 400,830.00 USD | 185.87 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 401,020.00 USD | 192.69 USD | 0.00 USD | `+35.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 401,210.00 USD | 187.50 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 445,860.00 USD | 44,650.00 USD | 0.00 USD | `+36.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 446,050.00 USD | 189.14 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 450,310.00 USD | 4,260.00 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 451,820.00 USD | 1,520.00 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 452,020.00 USD | 191.59 USD | 0.00 USD | `+39.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 473,340.00 USD | 21,320.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 475,870.00 USD | 2,530.00 USD | 0.00 USD | `+41.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 476,060.00 USD | 195.67 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 498,310.00 USD | 22,240.00 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 507,610.00 USD | 9,300.00 USD | 0.00 USD | `+43.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 658,380.00 USD | 150,770.00 USD | 0.00 USD | `+45.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 677,130.00 USD | 18,750.00 USD | 0.00 USD | `+46.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 677,680.00 USD | 551.23 USD | 0.00 USD | `+47.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 678,710.00 USD | 1,030.00 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 685,900.00 USD | 7,190.00 USD | 0.00 USD | `+48.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 686,190.00 USD | 289.23 USD | 0.00 USD | `+49.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 691,200.00 USD | 5,010.00 USD | 0.00 USD | `+50.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 707,080.00 USD | 15,880.00 USD | 0.00 USD | `+50.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 708,860.00 USD | 1,780.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 712,440.00 USD | 3,580.00 USD | 0.00 USD | `+51.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 724,170.00 USD | 11,730.00 USD | 0.00 USD | `+52.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 729,330.00 USD | 5,160.00 USD | 0.00 USD | `+52.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 746,200.00 USD | 16,870.00 USD | 0.00 USD | `+54.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 775,330.00 USD | 29,130.00 USD | 0.00 USD | `+54.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 855,120.00 USD | 79,780.00 USD | 0.00 USD | `+57.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 855,390.00 USD | 272.88 USD | 0.00 USD | `+60.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 855,780.00 USD | 394.01 USD | 0.00 USD | `+64.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 875,380.00 USD | 19,600.00 USD | 0.00 USD | `+66.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 877,520.00 USD | 2,130.00 USD | 0.00 USD | `+69.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 878,100.00 USD | 579.27 USD | 0.00 USD | `+70.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 881,100.00 USD | 3,010.00 USD | 0.00 USD | `+72.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 881,210.00 USD | 101.21 USD | 0.00 USD | `+75.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 881,470.00 USD | 262.73 USD | 0.00 USD | `+76.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 882,910.00 USD | 1,440.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 888,570.00 USD | 5,660.00 USD | 0.00 USD | `+78.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 893,990.00 USD | 5,430.00 USD | 0.00 USD | `+79.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 894,280.00 USD | 289.61 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 899,460.00 USD | 5,180.00 USD | 0.00 USD | `+86.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 899,820.00 USD | 357.85 USD | 0.00 USD | `+98.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 900,070.00 USD | 251.29 USD | 0.00 USD | `+99.32%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1336` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD |
| `7D` | `0.1340` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD |
| `1D` | `0.1341` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 3,550.00 USD | 1,460.00 USD | 3,640.00 USD |
| `1D` | `0.1344` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 691.54 USD | 598.60 USD |
| `7D` | `0.1344` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD |
| `1D` | `0.1347` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 670.19 USD |
| `7D` | `0.1348` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD |
| `1D` | `0.1350` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 5,030.00 USD | 1,310.00 USD | 6,250.00 USD |
| `7D` | `0.1352` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD |
| `1D` | `0.1353` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 3,530.00 USD | 1,430.00 USD | 2,910.00 USD |
| `1D` | `0.1356` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 932.52 USD | 0.00 USD | 4,150.00 USD |
| `7D` | `0.1356` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD |
| `1D` | `0.1359` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,480.00 USD | 869.31 USD | 4,230.00 USD |
| `7D` | `0.1360` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD |
| `1D` | `0.1362` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 4,890.00 USD | 950.53 USD | 2,660.00 USD |
| `7D` | `0.1364` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `1D` | `0.1365` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,340.00 USD | 1,900.00 USD | 1,150.00 USD |
| `1D` | `0.1368` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `0.1368` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `1D` | `0.1371` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 3,680.00 USD | 1,110.00 USD | 2,240.00 USD |
| `7D` | `0.1372` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1374` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,790.00 USD | 2,220.00 USD | 0.00 USD |
| `1D` | `0.1377` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 936.88 USD | 821.64 USD | 536.58 USD |
| `1D` | `0.1380` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 3,510.00 USD | 7,310.00 USD | 10,920.00 USD |
| `7D` | `0.1380` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `1D` | `0.1383` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 12,820.00 USD | 3,530.00 USD | 5,220.00 USD |
| `7D` | `0.1384` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 11,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1386` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 11,810.00 USD | 2,090.00 USD | 2,250.00 USD |
| `7D` | `0.1388` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `1D` | `0.1389` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 17,640.00 USD | 524.77 USD | 0.00 USD |
| `1D` | `0.1392` | 993,320.00 USD | 0.00 USD | 993,320.00 USD | 0.00 USD | 1,440.00 USD | 1,020.00 USD |
| `7D` | `0.1392` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD |
| `1D` | `0.1395` | 990,850.00 USD | 0.00 USD | 990,850.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1396` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1398` | 984,630.00 USD | 0.00 USD | 984,630.00 USD | 12,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1400` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1401` | 972,020.00 USD | 0.00 USD | 972,020.00 USD | 1,990.00 USD | 2,100.00 USD | 0.00 USD |
| `1D` | `0.1404` | 967,920.00 USD | 0.00 USD | 967,920.00 USD | 0.00 USD | 966.86 USD | 2,000.00 USD |
| `7D` | `0.1404` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1410` | 964,950.00 USD | 0.00 USD | 964,950.00 USD | 0.00 USD | 0.00 USD | 1,070.00 USD |
| `1D` | `0.1413` | 963,880.00 USD | 0.00 USD | 963,880.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1416` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1422` | 961,480.00 USD | 0.00 USD | 961,480.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1432` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD |
| `1D` | `0.1434` | 948,730.00 USD | 0.00 USD | 948,730.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1440` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD |
| `1D` | `0.1443` | 944,840.00 USD | 0.00 USD | 944,840.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1444` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1452` | 942,700.00 USD | 0.00 USD | 942,700.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1452` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD |
| `7D` | `0.1456` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `7D` | `0.1460` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD |
| `1D` | `0.1464` | 939,710.00 USD | 0.00 USD | 939,710.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD |
| `7D` | `0.1464` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1467` | 937,720.00 USD | 0.00 USD | 937,720.00 USD | 3,740.00 USD | 2,700.00 USD | 5,670.00 USD |
| `7D` | `0.1468` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 9,720.00 USD | 9,180.00 USD | 8,720.00 USD |
| `1D` | `0.1470` | 925,610.00 USD | 0.00 USD | 925,610.00 USD | 8,350.00 USD | 4,180.00 USD | 5,200.00 USD |
| `7D` | `0.1472` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 907,880.00 USD | 0.00 USD | 907,880.00 USD | 20,060.00 USD | 10,370.00 USD | 24,740.00 USD |
| `1D` | `0.1476` | 852,710.00 USD | 0.00 USD | 852,710.00 USD | 49,490.00 USD | 11,390.00 USD | 6,730.00 USD |
| `7D` | `0.1476` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 49,830.00 USD | 20,180.00 USD | 5,320.00 USD |
| `1D` | `0.1479` | 785,090.00 USD | 0.00 USD | 785,090.00 USD | 85,430.00 USD | 14,840.00 USD | 3,930.00 USD |
| `7D` | `0.1480` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 50,400.00 USD | 43,810.00 USD | 50,250.00 USD |
| `1D` | `0.1482` | 680,900.00 USD | 0.00 USD | 680,900.00 USD | 18,660.00 USD | 6,350.00 USD | 12,260.00 USD |
| `7D` | `0.1484` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 47,020.00 USD | 16,640.00 USD | 43,440.00 USD |
| `1D` | `0.1485` | 643,630.00 USD | 0.00 USD | 643,630.00 USD | 13,550.00 USD | 3,320.00 USD | 7,830.00 USD |
| `1D` | `0.1488` | 618,920.00 USD | 0.00 USD | 618,920.00 USD | 2,660.00 USD | 5,180.00 USD | 7,250.00 USD |
| `7D` | `0.1488` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 24,980.00 USD | 10,470.00 USD | 25,980.00 USD |
| `1D` | `0.1491` | 603,820.00 USD | 0.00 USD | 603,820.00 USD | 21,950.00 USD | 10,490.00 USD | 6,890.00 USD |
| `7D` | `0.1492` | 998,160.00 USD | 0.00 USD | 998,160.00 USD | 40,320.00 USD | 21,590.00 USD | 35,230.00 USD |
| `1D` | `0.1494` | 564,500.00 USD | 0.00 USD | 564,500.00 USD | 25,050.00 USD | 5,270.00 USD | 2,510.00 USD |
| `7D` | `0.1496` | 901,010.00 USD | 0.00 USD | 901,010.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD |
| `1D` | `0.1497` | 531,670.00 USD | 0.00 USD | 531,670.00 USD | 0.00 USD | 0.00 USD | 2,530.00 USD |
| `1D` | `0.1500` | 529,140.00 USD | 0.00 USD | 529,140.00 USD | 2,670.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `0.1500` | 830,580.00 USD | 0.00 USD | 830,580.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD |
| `1D` | `0.1503` | 523,110.00 USD | 0.00 USD | 523,110.00 USD | 25,000.00 USD | 15,920.00 USD | 50,850.00 USD |
| `7D` | `0.1504` | 738,520.00 USD | 0.00 USD | 738,520.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD |
| `1D` | `0.1506` | 431,340.00 USD | 0.00 USD | 431,340.00 USD | 57,660.00 USD | 27,330.00 USD | 7,720.00 USD |
| `7D` | `0.1508` | 653,740.00 USD | 0.00 USD | 653,740.00 USD | 115,630.00 USD | 16,820.00 USD | 104,530.00 USD |
| `1D` | `0.1509` | 338,630.00 USD | 0.00 USD | 338,630.00 USD | 106,680.00 USD | 3,940.00 USD | 0.00 USD |
| `1D` | `0.1512` | 228,010.00 USD | 0.00 USD | 228,010.00 USD | 88,190.00 USD | 4,360.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 416,770.00 USD | 0.00 USD | 416,770.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD |
| `1D` | `0.1515` | 132,960.00 USD | 0.00 USD | 132,960.00 USD | 0.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1516` | 257,210.00 USD | 0.00 USD | 257,210.00 USD | 0.00 USD | 13,330.00 USD | 61,270.00 USD |
| `1D` | `0.1518` | 128,600.00 USD | 0.00 USD | 128,600.00 USD | 24,410.00 USD | 10,080.00 USD | 24,730.00 USD |
| `7D` | `0.1520` | 182,610.00 USD | 0.00 USD | 182,610.00 USD | 0.00 USD | 22,090.00 USD | 87,060.00 USD |
| `1D` | `0.1521` | 69,380.00 USD | 0.00 USD | 69,380.00 USD | 38,050.00 USD | 1,470.00 USD | 11,330.00 USD |
| `1D` | `0.1524` | 18,530.00 USD | 0.00 USD | 18,530.00 USD | 0.00 USD | 2,970.00 USD | 7,150.00 USD |
| `7D` | `0.1524` | 73,470.00 USD | 0.00 USD | 73,470.00 USD | 0.00 USD | 13,950.00 USD | 8,320.00 USD |
| `1D` | `0.1527` | 8,410.00 USD | 0.00 USD | 8,410.00 USD | 0.00 USD | 0.00 USD | 8,410.00 USD |
| `7D` | `0.1528` | 51,200.00 USD | 0.00 USD | 51,200.00 USD | 0.00 USD | 33,940.00 USD | 0.00 USD |
| `7D` | `0.1532` | 17,260.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD | 17,260.00 USD | 0.00 USD |
| `1D` | `0.1536` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1536` | 8,570.00 USD | 8,570.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `7D` | `0.1536` | 17,140.00 USD | 17,140.00 USD | 0.00 USD | 0.00 USD | 8,570.00 USD | 0.00 USD |
| `7D` | `0.1540` | 35,360.00 USD | 35,360.00 USD | 0.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `1D` | `0.1542` | 4,490.00 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD |
| `7D` | `0.1544` | 38,960.00 USD | 38,960.00 USD | 0.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 6,220.00 USD | 6,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,730.00 USD |
| `1D` | `0.1548` | 61,520.00 USD | 61,520.00 USD | 0.00 USD | 0.00 USD | 22,180.00 USD | 33,130.00 USD |
| `7D` | `0.1548` | 41,820.00 USD | 41,820.00 USD | 0.00 USD | 0.00 USD | 2,860.00 USD | 0.00 USD |
| `1D` | `0.1551` | 69,560.00 USD | 69,560.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD | 3,890.00 USD |
| `7D` | `0.1552` | 53,630.00 USD | 53,630.00 USD | 0.00 USD | 0.00 USD | 11,820.00 USD | 0.00 USD |
| `1D` | `0.1554` | 76,750.00 USD | 76,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,190.00 USD |
| `1D` | `0.1557` | 84,020.00 USD | 84,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,270.00 USD |
| `1D` | `0.1560` | 89,600.00 USD | 89,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,580.00 USD |
| `7D` | `0.1560` | 64,620.00 USD | 64,620.00 USD | 0.00 USD | 0.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.1563` | 105,650.00 USD | 105,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,050.00 USD |
| `7D` | `0.1564` | 122,670.00 USD | 122,670.00 USD | 0.00 USD | 24,300.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `0.1566` | 260,430.00 USD | 260,430.00 USD | 0.00 USD | 70,290.00 USD | 13,270.00 USD | 71,200.00 USD |
| `7D` | `0.1568` | 239,210.00 USD | 239,210.00 USD | 0.00 USD | 101,180.00 USD | 15,360.00 USD | 0.00 USD |
| `1D` | `0.1569` | 370,140.00 USD | 370,140.00 USD | 0.00 USD | 82,020.00 USD | 20,660.00 USD | 7,030.00 USD |
| `1D` | `0.1572` | 507,720.00 USD | 507,720.00 USD | 0.00 USD | 137,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1572` | 524,820.00 USD | 524,820.00 USD | 0.00 USD | 187,220.00 USD | 39,540.00 USD | 58,840.00 USD |
| `1D` | `0.1575` | 533,690.00 USD | 533,690.00 USD | 0.00 USD | 25,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1576` | 693,330.00 USD | 693,330.00 USD | 0.00 USD | 44,680.00 USD | 123,840.00 USD | 0.00 USD |
| `7D` | `0.1580` | 924,360.00 USD | 924,360.00 USD | 0.00 USD | 129,940.00 USD | 101,090.00 USD | 0.00 USD |
| `1D` | `0.1584` | 562,290.00 USD | 562,290.00 USD | 0.00 USD | 28,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1584` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 80,450.00 USD | 43,370.00 USD | 0.00 USD |
| `1D` | `0.1587` | 621,840.00 USD | 621,840.00 USD | 0.00 USD | 15,100.00 USD | 22,970.00 USD | 21,480.00 USD |
| `7D` | `0.1588` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 69,180.00 USD | 44,590.00 USD | 0.00 USD |
| `1D` | `0.1590` | 666,110.00 USD | 666,110.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD | 16,310.00 USD |
| `7D` | `0.1592` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 127,590.00 USD | 64,620.00 USD | 0.00 USD |
| `1D` | `0.1593` | 703,220.00 USD | 703,220.00 USD | 0.00 USD | 0.00 USD | 6,320.00 USD | 30,800.00 USD |
| `1D` | `0.1596` | 761,150.00 USD | 761,150.00 USD | 0.00 USD | 10,700.00 USD | 19,800.00 USD | 27,430.00 USD |
| `7D` | `0.1596` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 174,510.00 USD | 98,530.00 USD | 0.00 USD |
| `1D` | `0.1599` | 809,640.00 USD | 809,640.00 USD | 0.00 USD | 26,110.00 USD | 22,370.00 USD | 0.00 USD |
| `7D` | `0.1600` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 271,880.00 USD | 60,710.00 USD | 24,520.00 USD |
| `1D` | `0.1602` | 915,710.00 USD | 915,710.00 USD | 0.00 USD | 106,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 242,660.00 USD | 112,090.00 USD | 313,270.00 USD |
| `1D` | `0.1605` | 982,980.00 USD | 982,980.00 USD | 0.00 USD | 67,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1608` | 999,140.00 USD | 999,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,160.00 USD |
| `7D` | `0.1608` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 208,080.00 USD | 240,680.00 USD | 172,000.00 USD |
| `1D` | `0.1611` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 20,140.00 USD | 11,530.00 USD | 83,790.00 USD |
| `7D` | `0.1612` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 304,970.00 USD | 328,050.00 USD | 287,340.00 USD |
| `1D` | `0.1614` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 14,300.00 USD | 0.00 USD | 39,510.00 USD |
| `7D` | `0.1616` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 293,210.00 USD | 131,180.00 USD | 108,800.00 USD |
| `1D` | `0.1617` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 31,470.00 USD | 7,430.00 USD | 0.00 USD |
| `1D` | `0.1620` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 85,250.00 USD | 57,920.00 USD | 0.00 USD |
| `7D` | `0.1620` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD |
| `1D` | `0.1623` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 53,880.00 USD | 67,020.00 USD | 0.00 USD |
| `7D` | `0.1624` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD |
| `1D` | `0.1626` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 51,630.00 USD | 12,640.00 USD | 0.00 USD |
| `1D` | `0.1632` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1635` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 10,690.00 USD | 8,690.00 USD |
| `7D` | `0.1636` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD |
| `1D` | `0.1638` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD |
| `7D` | `0.1640` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1641` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD |
| `1D` | `0.1644` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 25,030.00 USD | 35,000.00 USD | 16,030.00 USD |
| `7D` | `0.1644` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD |
| `7D` | `0.1648` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1656` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 9,730.00 USD | 40,450.00 USD | 8,050.00 USD |
| `7D` | `0.1656` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD |
| `1D` | `0.1659` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 19,240.00 USD | 0.00 USD |
| `7D` | `0.1660` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 40,780.00 USD | 11,020.00 USD | 0.00 USD |
| `1D` | `0.1662` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 8,220.00 USD | 6,760.00 USD | 20,710.00 USD |
| `7D` | `0.1664` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1665` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 22,170.00 USD | 5,570.00 USD | 80,390.00 USD |
| `1D` | `0.1668` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 21,290.00 USD |
| `7D` | `0.1668` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 20,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1672` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD |
| `1D` | `0.1674` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 45,910.00 USD | 2,010.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD |
| `1D` | `0.1680` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 75,420.00 USD | 4,560.00 USD | 0.00 USD |
| `7D` | `0.1680` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 99,440.00 USD | 3,200.00 USD | 18,740.00 USD |
| `7D` | `0.1684` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 6,560.00 USD | 29,250.00 USD | 33,410.00 USD |
| `7D` | `0.1688` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 6,980.00 USD | 4,020.00 USD |
| `1D` | `0.1692` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 82,220.00 USD | 69,050.00 USD | 14,290.00 USD |
| `7D` | `0.1692` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 33,660.00 USD | 70,740.00 USD | 40,690.00 USD |
| `1D` | `0.1695` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 24,260.00 USD | 25,080.00 USD | 6,650.00 USD |
| `7D` | `0.1696` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 39,780.00 USD |
| `1D` | `0.1698` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 37,080.00 USD | 56,690.00 USD | 0.00 USD |
| `7D` | `0.1700` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 41,050.00 USD |
| `1D` | `0.1704` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 55,170.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1707` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 53,700.00 USD | 71,860.00 USD | 13,990.00 USD |
| `7D` | `0.1708` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,040.00 USD |
| `1D` | `0.1713` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `1D` | `0.1716` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 9,570.00 USD | 25,600.00 USD | 16,070.00 USD |
| `7D` | `0.1716` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 34,230.00 USD | 10,110.00 USD | 8,520.00 USD |
| `7D` | `0.1720` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1722` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 100,000.00 USD | 16,860.00 USD | 45,350.00 USD |
| `7D` | `0.1724` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD |
| `1D` | `0.1725` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 8,230.00 USD | 2,410.00 USD | 33,410.00 USD |
| `1D` | `0.1728` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1732` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1734` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `1D` | `0.1737` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 33,580.00 USD | 11,810.00 USD | 6,410.00 USD |
| `1D` | `0.1740` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 1,600.00 USD | 9,640.00 USD |
| `7D` | `0.1740` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD |
| `1D` | `0.1743` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1744` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 8,530.00 USD | 2,460.00 USD | 9,500.00 USD |
| `7D` | `0.1748` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `1D` | `0.1752` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 27,740.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `0.1752` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 271,210.00 USD |
| `1D` | `0.1755` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 21,260.00 USD | 16,650.00 USD | 35,390.00 USD |
| `7D` | `0.1756` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 97,570.00 USD | 0.00 USD | 186,030.00 USD |
| `1D` | `0.1758` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 71,330.00 USD | 31,940.00 USD | 51,130.00 USD |
| `7D` | `0.1760` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 277,910.00 USD | 77,870.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 53,970.00 USD | 88,390.00 USD | 50,220.00 USD |
| `1D` | `0.1764` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 34,410.00 USD | 27,980.00 USD | 61,480.00 USD |
| `7D` | `0.1764` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 353,950.00 USD | 282,090.00 USD | 40,340.00 USD |
| `1D` | `0.1767` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 27,430.00 USD | 52,820.00 USD | 52,230.00 USD |
| `7D` | `0.1768` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 191,690.00 USD | 154,100.00 USD | 31,570.00 USD |
| `1D` | `0.1770` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 36,140.00 USD | 47,810.00 USD | 38,500.00 USD |
| `7D` | `0.1772` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 15,040.00 USD | 28,980.00 USD | 22,840.00 USD |
| `1D` | `0.1776` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 38,630.00 USD | 19,390.00 USD | 21,010.00 USD |
| `7D` | `0.1776` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1779` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 27,480.00 USD | 77,730.00 USD | 25,130.00 USD |
| `7D` | `0.1780` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD |
| `1D` | `0.1782` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 46,310.00 USD | 14,240.00 USD | 14,970.00 USD |
| `7D` | `0.1784` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 96,920.00 USD | 39,090.00 USD | 14,990.00 USD |
| `1D` | `0.1788` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 18,550.00 USD | 37,940.00 USD | 36,930.00 USD |
| `7D` | `0.1788` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1791` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 36,940.00 USD | 15,630.00 USD | 18,080.00 USD |
| `7D` | `0.1792` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 41,300.00 USD | 49,090.00 USD | 15,390.00 USD |
| `7D` | `0.1796` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 17,130.00 USD | 26,110.00 USD | 44,450.00 USD |
| `1D` | `0.1797` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 27,280.00 USD | 22,110.00 USD | 36,970.00 USD |
| `1D` | `0.1800` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 5,820.00 USD | 8,690.00 USD | 25,360.00 USD |
| `7D` | `0.1800` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 12,940.00 USD | 34,680.00 USD | 73,510.00 USD |
| `1D` | `0.1803` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 10,270.00 USD | 35,880.00 USD | 12,560.00 USD |
| `7D` | `0.1804` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 35,280.00 USD | 32,850.00 USD | 23,570.00 USD |
| `1D` | `0.1806` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 9,910.00 USD | 14,370.00 USD | 15,820.00 USD |
| `7D` | `0.1808` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 35,050.00 USD | 67,250.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 17,680.00 USD | 27,370.00 USD | 7,030.00 USD |
| `1D` | `0.1812` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 23,530.00 USD | 37,720.00 USD | 22,960.00 USD |
| `7D` | `0.1812` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 64,990.00 USD | 29,900.00 USD | 50,510.00 USD |
| `1D` | `0.1815` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 13,550.00 USD | 3,320.00 USD | 14,670.00 USD |
| `7D` | `0.1816` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 69,700.00 USD | 33,940.00 USD | 38,270.00 USD |
| `1D` | `0.1818` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 37,120.00 USD | 11,780.00 USD | 11,110.00 USD |
| `7D` | `0.1820` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 65,350.00 USD | 54,880.00 USD | 43,100.00 USD |
| `1D` | `0.1821` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 21,220.00 USD | 15,970.00 USD | 9,370.00 USD |
| `1D` | `0.1824` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 14,850.00 USD | 15,990.00 USD | 16,470.00 USD |
| `7D` | `0.1824` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 80,350.00 USD | 17,880.00 USD | 112,550.00 USD |
| `1D` | `0.1827` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 21,440.00 USD | 6,860.00 USD | 4,170.00 USD |
| `7D` | `0.1828` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 79,610.00 USD | 29,630.00 USD | 69,840.00 USD |
| `1D` | `0.1830` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 4,510.00 USD | 5,690.00 USD |
| `7D` | `0.1832` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 108,540.00 USD | 31,590.00 USD | 74,200.00 USD |
| `1D` | `0.1833` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 4,630.00 USD |
| `1D` | `0.1836` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 3,610.00 USD | 0.00 USD | 728.16 USD |
| `7D` | `0.1836` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 172,660.00 USD | 110,870.00 USD | 52,650.00 USD |
| `1D` | `0.1839` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 7,830.00 USD |
| `7D` | `0.1840` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 141,620.00 USD | 50,840.00 USD | 151,740.00 USD |
| `1D` | `0.1842` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 5,430.00 USD | 4,660.00 USD | 6,200.00 USD |
| `7D` | `0.1844` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 94,510.00 USD | 20,390.00 USD | 82,350.00 USD |
| `1D` | `0.1845` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 10,860.00 USD | 7,090.00 USD | 1,890.00 USD |
| `1D` | `0.1848` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 5,910.00 USD | 4,360.00 USD | 4,500.00 USD |
| `7D` | `0.1848` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD |
| `1D` | `0.1851` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 6,220.00 USD | 1,730.00 USD | 2,640.00 USD |
| `7D` | `0.1852` | 14,620,000.00 USD | 14,620,000.00 USD | 0.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD |
| `1D` | `0.1854` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 4,290.00 USD | 1,690.00 USD | 4,220.00 USD |
| `7D` | `0.1856` | 14,840,000.00 USD | 14,840,000.00 USD | 0.00 USD | 100,160.00 USD | 21,030.00 USD | 106,560.00 USD |
| `1D` | `0.1857` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 10,050.00 USD | 2,630.00 USD | 12,090.00 USD |
| `1D` | `0.1860` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 9,450.00 USD | 4,440.00 USD | 5,820.00 USD |
| `7D` | `0.1860` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 64,600.00 USD | 59,290.00 USD | 127,610.00 USD |
| `1D` | `0.1863` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 8,320.00 USD |
| `7D` | `0.1864` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD |
| `1D` | `0.1866` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | 5,140.00 USD |
| `7D` | `0.1868` | 15,490,000.00 USD | 15,490,000.00 USD | 0.00 USD | 133,990.00 USD | 51,510.00 USD | 56,290.00 USD |
| `1D` | `0.1869` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 4,960.00 USD | 1,740.00 USD | 9,730.00 USD |
| `1D` | `0.1872` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 12,350.00 USD | 5,200.00 USD | 5,320.00 USD |
| `7D` | `0.1872` | 15,990,000.00 USD | 15,990,000.00 USD | 0.00 USD | 188,990.00 USD | 158,170.00 USD | 155,060.00 USD |
| `1D` | `0.1875` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 1,960.00 USD | 2,820.00 USD | 2,290.00 USD |
| `7D` | `0.1876` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 65,910.00 USD | 34,900.00 USD | 43,960.00 USD |
| `1D` | `0.1878` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 4,320.00 USD | 2,760.00 USD | 918.24 USD |
| `7D` | `0.1880` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 57,250.00 USD | 35,940.00 USD | 30,950.00 USD |
| `1D` | `0.1881` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 2,920.00 USD | 6,640.00 USD | 1,240.00 USD |
| `1D` | `0.1883` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 1,710.00 USD | 1,200.00 USD | 0.00 USD |
| `7D` | `0.1884` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 14,000.00 USD | 35,430.00 USD | 9,740.00 USD |
| `7D` | `0.1888` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 22,970.00 USD | 17,330.00 USD | 88,260.00 USD |
| `7D` | `0.1892` | 16,540,000.00 USD | 16,540,000.00 USD | 0.00 USD | 49,980.00 USD | 2,860.00 USD | 34,160.00 USD |
| `7D` | `0.1896` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 42,320.00 USD | 17,300.00 USD | 18,680.00 USD |
| `7D` | `0.1900` | 16,670,000.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 29,650.00 USD | 20,420.00 USD |
| `7D` | `0.1904` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 14,330.00 USD | 17,690.00 USD | 10,800.00 USD |
| `7D` | `0.1908` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 33,940.00 USD | 50,270.00 USD | 52,810.00 USD |
| `7D` | `0.1912` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 15,240.00 USD | 0.00 USD |
| `7D` | `0.1916` | 16,890,000.00 USD | 16,890,000.00 USD | 0.00 USD | 7,460.00 USD | 12,040.00 USD | 11,900.00 USD |
| `7D` | `0.1920` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD |
| `7D` | `0.1924` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD |
| `7D` | `0.1928` | 16,940,000.00 USD | 16,940,000.00 USD | 0.00 USD | 11,600.00 USD | 13,630.00 USD | 0.00 USD |
| `7D` | `0.1944` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1952` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD |
| `7D` | `0.1956` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD |
| `7D` | `0.1960` | 16,970,000.00 USD | 16,970,000.00 USD | 0.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1964` | 16,990,000.00 USD | 16,990,000.00 USD | 0.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `187.41M` | Total OI Tokens: `1,221,224,057.2 ARB`
  * 1h OI Change: `-10.25%` | 4h OI Change: `-12.33%` | 24h OI Change: `-20.95%`
  * Exchange Breakdown: Binance=`43.47M` | Bybit=`26.48M` | OKX=`15.06M` | Hyperliquid=`12.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.05K` | Last 24h: `10.97K` | Last 3d: `22.34K` | Last 7d: `43.06K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0023%` | **USDT OKX** | `0.0092%` |
| **USDT Bybit** | `0.0054%` | **USDT KuCoin** | `0.0057%` |
| **USDT MEXC** | `0.0092%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0077%` | **USDT Bitget** | `0.0024%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `44.11%` | `55.89%` | `0.79` | 19,970,000.00 USD |
| `15M` | `Binance` | `44.89%` | `55.11%` | `0.81` | 7,930,000.00 USD |
| `15M` | `OKX` | `44.74%` | `55.26%` | `0.81` | 2,840,000.00 USD |
| `15M` | `Bybit` | `41.62%` | `58.38%` | `0.71` | 3,720,000.00 USD |
| `15M` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 243,660.00 USD |
| `15M` | `Gate` | `41.26%` | `58.74%` | `0.70` | 145,040.00 USD |
| `15M` | `Bitget` | `46.48%` | `53.52%` | `0.87` | 1,660,000.00 USD |
| `15M` | `BingX` | `33.62%` | `66.38%` | `0.51` | 460,510.00 USD |
| `15M` | `MEXC` | `41.53%` | `58.47%` | `0.71` | 709,450.00 USD |
| `15M` | `Bitunix` | `46.39%` | `53.61%` | `0.87` | 223,790.00 USD |
| `15M` | `Hyperliquid` | `44.14%` | `55.86%` | `0.79` | 261,110.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.85%` | `55.15%` | `0.81` | 1,530,000.00 USD |
| `15M` | `Crypto.com` | `28.97%` | `71.03%` | `0.41` | 17,690.00 USD |
| `15M` | `WhiteBIT` | `58.84%` | `41.16%` | `1.43` | 97,820.00 USD |
| `15M` | `HTX` | `49.1%` | `50.9%` | `0.96` | 36,310.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `54.84%` | `45.16%` | `1.21` | 27,970.00 USD |
| `15M` | `Aster` | `19.97%` | `80.03%` | `0.25` | 21,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `64.6%` | `35.4%` | `1.82` | 38,050.00 USD |
| `15M` | `Whale Positions` | `44.89%` | `55.11%` | `0.81` | 7,930,000.00 USD |
| `15M` | `Global Accounts` | `44.11%` | `55.89%` | `0.79` | 19,970,000.00 USD |
| `1H` | `ARB` | `44.45%` | `55.55%` | `0.80` | 36,060,000.00 USD |
| `1H` | `Binance` | `44.22%` | `55.78%` | `0.79` | 13,800,000.00 USD |
| `1H` | `OKX` | `45.03%` | `54.97%` | `0.82` | 4,900,000.00 USD |
| `1H` | `Bybit` | `42.34%` | `57.66%` | `0.73` | 6,280,000.00 USD |
| `1H` | `KuCoin` | `46.93%` | `53.07%` | `0.88` | 451,150.00 USD |
| `1H` | `Gate` | `47.46%` | `52.54%` | `0.90` | 304,660.00 USD |
| `1H` | `Bitget` | `49.21%` | `50.79%` | `0.97` | 2,890,000.00 USD |
| `1H` | `BingX` | `40.85%` | `59.15%` | `0.69` | 947,300.00 USD |
| `1H` | `MEXC` | `37.34%` | `62.66%` | `0.60` | 1,310,000.00 USD |
| `1H` | `Bitunix` | `43.49%` | `56.51%` | `0.77` | 414,670.00 USD |
| `1H` | `Hyperliquid` | `34.24%` | `65.76%` | `0.52` | 576,230.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.39%` | `52.61%` | `0.90` | 3,750,000.00 USD |
| `1H` | `Crypto.com` | `28.58%` | `71.42%` | `0.40` | 17,920.00 USD |
| `1H` | `WhiteBIT` | `70.85%` | `29.15%` | `2.43` | 218,700.00 USD |
| `1H` | `HTX` | `46.94%` | `53.06%` | `0.88` | 40,950.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `54.38%` | `45.62%` | `1.19` | 45,600.00 USD |
| `1H` | `Aster` | `31.57%` | `68.43%` | `0.46` | 50,080.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.55%` | `46.45%` | `1.15` | 63,530.00 USD |
| `1H` | `Whale Positions` | `44.22%` | `55.78%` | `0.79` | 13,800,000.00 USD |
| `1H` | `Global Accounts` | `44.45%` | `55.55%` | `0.80` | 36,060,000.00 USD |
| `4H` | `ARB` | `46.09%` | `53.91%` | `0.85` | 48,730,000.00 USD |
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
| `5:00 UTC` | `0.1687` | `0.1687` | `0.1687` | `0.1691` | `0.1680` | 541,507.84 USD | 294,376.97 USD | 247,130.87 USD | 47,246.11 USD | `+8.72%` | `31B / 8S` |
| `0:00 UTC` | `0.1684` | `0.1682` | `0.1684` | `0.1688` | `0.1678` | 593,121.43 USD | 297,803.46 USD | 295,317.97 USD | 2,485.50 USD | `+0.42%` | `13B / 13S` |
| `5:00 UTC` | `0.1683` | `0.1683` | `0.1683` | `0.1688` | `0.1678` | 375,189.89 USD | 244,846.62 USD | 130,343.28 USD | 114,503.34 USD | `+30.52%` | `33B / 4S` |
| `0:00 UTC` | `0.1688` | `0.1688` | `0.1688` | `0.1693` | `0.1682` | 680,766.88 USD | 453,606.46 USD | 227,160.42 USD | 226,446.04 USD | `+33.26%` | `32B / 8S` |
| `5:00 UTC` | `0.1682` | `0.1683` | `0.1682` | `0.1688` | `0.1681` | 452,736.37 USD | 213,244.89 USD | 239,491.48 USD | -26,246.58 USD | `-5.80%` | `7B / 12S` |
| `0:00 UTC` | `0.1667` | `0.1655` | `0.1667` | `0.1684` | `0.1640` | 2,535,332.38 USD | 1,148,875.51 USD | 1,386,456.87 USD | -237,581.36 USD | `-9.37%` | `2B / 23S` |
| `5:00 UTC` | `0.1650` | `0.1654` | `0.1650` | `0.1661` | `0.1649` | 718,046.47 USD | 414,320.10 USD | 303,726.37 USD | 110,593.73 USD | `+15.40%` | `33B / 14S` |
| `0:00 UTC` | `0.1592` | `0.1590` | `0.1592` | `0.1655` | `0.1541` | 10,418,999.97 USD | 3,996,711.76 USD | 6,422,288.21 USD | -2,425,576.45 USD | `-23.28%` | `2B / 33S` |
| `5:00 UTC` | `0.1535` | `0.1536` | `0.1535` | `0.1560` | `0.1508` | 10,296,961.64 USD | 4,216,389.14 USD | 6,080,572.50 USD | -1,864,183.37 USD | `-18.10%` | `2B / 11S` |
| `0:00 UTC` | `0.1540` | `0.1537` | `0.1540` | `0.1546` | `0.1528` | 1,233,442.46 USD | 629,619.58 USD | 603,822.87 USD | 25,796.71 USD | `+2.09%` | `39B / 22S` |

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
| `5m` | -266,720.00 USD | -869,510.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,020,000.00 USD | -5,520,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,600,000.00 USD | -6,800,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,800,000.00 USD | -7,100,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,660,000.00 USD | -6,560,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,850,000.00 USD | -7,660,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,600,000.00 USD | -8,700,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,820,000.00 USD | -10,020,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,530,000.00 USD | -10,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,720,000.00 USD | -12,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,630,000.00 USD | -36,670,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,980,000.00 USD | -169,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-266.72K` | 15m=`-1.02M` | 1h=`-1.80M` | 24h=`-2.72M`
* Futures Capital Netflows: 5m=`-869.51K` | 15m=`-5.52M` | 1h=`-7.10M` | 24h=`-12.42M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
