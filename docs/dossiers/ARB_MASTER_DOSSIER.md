# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:23:17 IST` (`2026-10-30 05:53:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1658` | `0.1658` | `0.1649` | `0.1650` | `4,752,817` | 786,069.93 USD | 316,026.04 USD | `+40.20%` | -8,427,574.34 USD | `+2.14` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1650` | `0.1664` | `0.1648` | `0.1658` | `2,278,169` | 377,602.89 USD | 13,118.76 USD | `+3.47%` | -8,414,455.58 USD | `+0.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1658` | `0.1665` | `0.1654` | `0.1663` | `1,747,424` | 289,922.40 USD | -66,801.91 USD | `-23.04%` | -8,481,257.49 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1637` | `0.1660` | `0.1635` | `0.1650` | `10,426,658` | 1,718,232.82 USD | -224,519.98 USD | `-13.07%` | -8,464,435.82 USD | `-0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1650` | `0.1663` | `0.1649` | `0.1658` | `9,302,309` | 1,541,284.70 USD | -279,164.57 USD | `-18.11%` | -8,743,600.38 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1658` | `0.1665` | `0.1648` | `0.1663` | `8,778,410` | 1,453,595.22 USD | 262,342.89 USD | `+18.05%` | -8,481,257.49 USD | `+0.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1580` | `20,448,591` | 3,216,248.24 USD | 252,196.82 USD | `+7.84%` | -7,911,945.27 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1639` | `0.1577` | `0.1637` | `36,120,104` | 5,820,548.12 USD | -303,641.20 USD | `-5.22%` | -8,215,586.47 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1637` | `0.1665` | `0.1635` | `0.1664` | `28,174,550` | 4,657,738.52 USD | -199,365.33 USD | `-4.28%` | -8,414,951.80 USD | `+0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1664` | `64,294,654` | 10,478,286.65 USD | -503,006.53 USD | `-4.80%` | -7,714,749.17 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1664` | `64,294,654` | 10,478,286.65 USD | -503,006.53 USD | `-4.80%` | -7,714,749.17 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1643` | 8,659.86 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.66K USD at 0.1643 USD [API] | `2026-10-29 02:10:56` |
| `ANNOUNCEMENT` | `INFO` | `0.1661` | 232.02 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.23K USD at 0.1661 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1661` | 4,385.22 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.39K USD at 0.1661 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1662` | 8,757.88 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.76K USD at 0.1662 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1664` | 8,771.05 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.77K USD at 0.1664 USD [API] | `2026-10-29 01:58:28` |
| `ANNOUNCEMENT` | `INFO` | `0.1674` | 48.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.05K USD at 0.1674 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `0.1674` | 25.25 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.03K USD at 0.1674 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 593.49 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.59K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 94.24 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.09K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 437.06 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.44K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 400.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.40K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 49.99 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.05K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1812` | 364.42 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.36K USD at 0.1812 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 94.26 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.09K USD at 0.1813 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 437.11 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.44K USD at 0.1813 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 400.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.40K USD at 0.1813 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 246.02 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.25K USD at 0.1813 USD [API] | `2026-10-14 14:11:59` |
| `ANNOUNCEMENT` | `INFO` | `0.1626` | 9.53 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.01K USD at 0.1626 USD [API] | `2026-10-29 07:17:25` |


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
| `Live` | `Long Liquidation` | `0.0385` | 1,870.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 163,510.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 121.77 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 461.29 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 924.32 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 5,230.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 718.35 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 1,100.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 3,930.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 373.83 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 6,710.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 194.36 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,150.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 61,400.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 18,860.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 1,890.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,580.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 20,320.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 4,830.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 501.81 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,420.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 386.50 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 3,530.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 2,020.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 112,140.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 20,310.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 8,180.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 7,380.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 934.41 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,330.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 640.52 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 13,820.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,640.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 6,230.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 7,420.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 26,330.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 18,250.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,640.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 844.86 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 134.66 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 29,370.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 972,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 3,750.00 USD | 962,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1305` | 8,780,000.00 USD | 8,780,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 959,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1308` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1311` | 8,770,000.00 USD | 8,770,000.00 USD | 6,470.00 USD | 4,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1314` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 4,010.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,660.00 USD | 942,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1317` | 8,750,000.00 USD | 8,750,000.00 USD | 14,240.00 USD | 4,840.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1320` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 2,780.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1323` | 8,700,000.00 USD | 8,700,000.00 USD | 5,580.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 17,180.00 USD | 937,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1326` | 8,690,000.00 USD | 8,690,000.00 USD | 7,890.00 USD | 10,270.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1329` | 8,660,000.00 USD | 8,660,000.00 USD | 11,110.00 USD | 5,000.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1332` | 8,640,000.00 USD | 8,640,000.00 USD | 17,000.00 USD | 1,900.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1335` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 4,190.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,200.00 USD | 920,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1338` | 8,600,000.00 USD | 8,600,000.00 USD | 2,830.00 USD | 9,530.00 USD | 32,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1341` | 8,560,000.00 USD | 8,560,000.00 USD | 6,330.00 USD | 0.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 8,550,000.00 USD | 8,550,000.00 USD | 6,410.00 USD | 5,790.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 44,860.00 USD | 869,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1347` | 8,520,000.00 USD | 8,520,000.00 USD | 31,170.00 USD | 5,000.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1350` | 8,470,000.00 USD | 8,470,000.00 USD | 7,650.00 USD | 8,440.00 USD | 23,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1353` | 8,430,000.00 USD | 8,430,000.00 USD | 7,440.00 USD | 3,540.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 824,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 8,410,000.00 USD | 8,410,000.00 USD | 12,450.00 USD | 8,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1359` | 8,380,000.00 USD | 8,380,000.00 USD | 25,240.00 USD | 6,700.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1362` | 8,340,000.00 USD | 8,340,000.00 USD | 3,340.00 USD | 3,690.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1365` | 8,330,000.00 USD | 8,330,000.00 USD | 11,660.00 USD | 1,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 823,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 8,310,000.00 USD | 8,310,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1371` | 8,300,000.00 USD | 8,300,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1374` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 812,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1377` | 8,260,000.00 USD | 8,260,000.00 USD | 5,780.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 8,250,000.00 USD | 8,250,000.00 USD | 8,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1383` | 8,240,000.00 USD | 8,240,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 16,480.00 USD | 798,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1386` | 8,200,000.00 USD | 8,200,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1395` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 782,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1398` | 8,110,000.00 USD | 8,110,000.00 USD | 6,210.00 USD | 4,200.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1401` | 8,080,000.00 USD | 8,080,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 5,540.00 USD | 776,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1413` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,690.00 USD | 770,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1419` | 4,890,000.00 USD | 4,890,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1419` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1422` | 4,880,000.00 USD | 4,880,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1422` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1425` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,990.00 USD | 754,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1428` | 4,860,000.00 USD | 4,860,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1431` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1434` | 4,860,000.00 USD | 4,860,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1434` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 25,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 254,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1437` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1437` | 8,000,000.00 USD | 8,000,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1440` | 4,830,000.00 USD | 4,830,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 7,980,000.00 USD | 7,980,000.00 USD | 9,760.00 USD | 2,750.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1443` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1443` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 235,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1446` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1452` | 4,780,000.00 USD | 4,780,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 10,680.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,750,000.00 USD | 4,750,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 225,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1458` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1464` | 4,730,000.00 USD | 4,730,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,840.00 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,700,000.00 USD | 4,700,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1467` | 7,920,000.00 USD | 7,920,000.00 USD | 9,720.00 USD | 5,520.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 4,680,000.00 USD | 4,680,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 7,820,000.00 USD | 7,820,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,660,000.00 USD | 4,660,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 7,810,000.00 USD | 7,810,000.00 USD | 19,430.00 USD | 8,790.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 87,010.00 USD | 101,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 4,510,000.00 USD | 4,510,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1476` | 7,770,000.00 USD | 7,770,000.00 USD | 61,700.00 USD | 14,780.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,260,000.00 USD | 4,260,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 7,610,000.00 USD | 7,610,000.00 USD | 67,510.00 USD | 39,730.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 4,090,000.00 USD | 4,090,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 7,460,000.00 USD | 7,460,000.00 USD | 41,960.00 USD | 20,720.00 USD | 59,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,920,000.00 USD | 3,920,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 7,340,000.00 USD | 7,340,000.00 USD | 40,660.00 USD | 7,340.00 USD | 163,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1488` | 3,780,000.00 USD | 3,780,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 7,120,000.00 USD | 7,120,000.00 USD | 44,530.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,750,000.00 USD | 3,750,000.00 USD | 40,720.00 USD | 15,530.00 USD | 16,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 7,070,000.00 USD | 7,070,000.00 USD | 43,480.00 USD | 22,050.00 USD | 85,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 3,680,000.00 USD | 3,680,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 6,920,000.00 USD | 6,920,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,720.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,600,000.00 USD | 3,600,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1497` | 6,860,000.00 USD | 6,860,000.00 USD | 20,880.00 USD | 17,180.00 USD | 188,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,540,000.00 USD | 3,540,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 6,630,000.00 USD | 6,630,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,520,000.00 USD | 3,520,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 6,560,000.00 USD | 6,560,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,470.00 USD | 10,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 3,290,000.00 USD | 3,290,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1506` | 6,520,000.00 USD | 6,520,000.00 USD | 129,280.00 USD | 18,020.00 USD | 217,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 6,160,000.00 USD | 6,160,000.00 USD | 166,980.00 USD | 9,550.00 USD | 82,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 2,890,000.00 USD | 2,890,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 8,620.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,870,000.00 USD | 2,870,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 13,330.00 USD | 369,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 9,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1518` | 2,490,000.00 USD | 2,490,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1518` | 5,460,000.00 USD | 5,460,000.00 USD | 96,310.00 USD | 15,160.00 USD | 108,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,400,000.00 USD | 2,400,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 11,720.00 USD | 144,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,320,000.00 USD | 2,320,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,280,000.00 USD | 2,280,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1527` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 35,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 2,250,000.00 USD | 2,250,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 5,020,000.00 USD | 5,020,000.00 USD | 35,470.00 USD | 16,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,350.00 USD | 8,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 2,180,000.00 USD | 2,180,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 2,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 2,140,000.00 USD | 2,140,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,100,000.00 USD | 2,100,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1545` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1548` | 2,060,000.00 USD | 2,060,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 15,410.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,020,000.00 USD | 2,020,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 21,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 1,970,000.00 USD | 1,970,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,930,000.00 USD | 1,930,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 4,510.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 1,910,000.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 16,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,890,000.00 USD | 1,890,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1566` | 1,840,000.00 USD | 1,840,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1566` | 4,580,000.00 USD | 4,580,000.00 USD | 70,940.00 USD | 29,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,710,000.00 USD | 1,710,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 4,480,000.00 USD | 4,480,000.00 USD | 138,980.00 USD | 5,100.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 1,580,000.00 USD | 1,580,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 4,190,000.00 USD | 4,190,000.00 USD | 208,130.00 USD | 42,920.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,450,000.00 USD | 1,450,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 3,880,000.00 USD | 3,880,000.00 USD | 23,310.00 USD | 88,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 3,770,000.00 USD | 3,770,000.00 USD | 107,560.00 USD | 84,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,440,000.00 USD | 1,440,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 3,570,000.00 USD | 3,570,000.00 USD | 140,060.00 USD | 25,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 1,420,000.00 USD | 1,420,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 3,410,000.00 USD | 3,410,000.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,310,000.00 USD | 1,310,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 3,330,000.00 USD | 3,330,000.00 USD | 69,180.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 1,200,000.00 USD | 1,200,000.00 USD | 15,370.00 USD | 28,520.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 3,170,000.00 USD | 3,170,000.00 USD | 24,840.00 USD | 12,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1596` | 1,020,000.00 USD | 1,020,000.00 USD | 10,260.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1596` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 74,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 55,380.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 997,600.00 USD | 997,600.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 46,490.00 USD | 50,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 940,330.00 USD | 940,330.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 2,810,000.00 USD | 2,810,000.00 USD | 150,770.00 USD | 16,950.00 USD | 264,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 936,490.00 USD | 936,490.00 USD | 34,860.00 USD | 7,790.00 USD | 79,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 2,380,000.00 USD | 2,380,000.00 USD | 129,610.00 USD | 0.00 USD | 289,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 814,120.00 USD | 814,120.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 1,960,000.00 USD | 1,960,000.00 USD | 196,320.00 USD | 0.00 USD | 322,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 777,340.00 USD | 777,340.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 1,440,000.00 USD | 1,440,000.00 USD | 323,670.00 USD | 0.00 USD | 219,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 899,980.00 USD | 899,980.00 USD | 126,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 738,670.00 USD | 738,670.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 709,770.00 USD | 709,770.00 USD | 65,520.00 USD | 22,690.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 773,640.00 USD | 773,640.00 USD | 49,670.00 USD | 156,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1626` | 604,040.00 USD | 604,040.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1626` | 567,100.00 USD | 567,100.00 USD | 0.00 USD | 71,120.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 464,670.00 USD | 464,670.00 USD | 20,520.00 USD | 3,520.00 USD | 104,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 359,220.00 USD | 359,220.00 USD | 147,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 336,510.00 USD | 336,510.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 214,210.00 USD | 214,210.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,460.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1638` | 205,520.00 USD | 205,520.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 211,510.00 USD | 211,510.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 176,400.00 USD | 176,400.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1641` | 187,950.00 USD | 187,950.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 157,330.00 USD | 157,330.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1644` | 158,710.00 USD | 158,710.00 USD | 0.00 USD | 34,100.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1647` | 94,830.00 USD | 94,830.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1647` | 80,070.00 USD | 80,070.00 USD | 0.00 USD | 4,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 69,020.00 USD | 69,020.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1650` | 75,280.00 USD | 75,280.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1659` | 68,280.00 USD | 68,280.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1662` | 36,390.00 USD | 36,390.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1662` | 84,060.00 USD | 84,060.00 USD | 84,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 100,320.00 USD | 100,320.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1665` | 241,140.00 USD | 241,140.00 USD | 87,050.00 USD | 12,670.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 13,460.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1668` | 146,270.00 USD | 146,270.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 379,340.00 USD | 379,340.00 USD | 11,410.00 USD | 39,630.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 175,440.00 USD | 175,440.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1671` | 594,030.00 USD | 594,030.00 USD | 135,250.00 USD | 79,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 244,980.00 USD | 244,980.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1674` | 727,940.00 USD | 727,940.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1677` | 284,440.00 USD | 284,440.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1677` | 864,350.00 USD | 864,350.00 USD | 59,010.00 USD | 77,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 379,650.00 USD | 379,650.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 1,090,000.00 USD | 1,090,000.00 USD | 101,910.00 USD | 68,430.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 482,100.00 USD | 482,100.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1683` | 1,160,000.00 USD | 1,160,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1686` | 616,160.00 USD | 616,160.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1686` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 720,810.00 USD | 720,810.00 USD | 41,580.00 USD | 32,630.00 USD | 30,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1689` | 1,290,000.00 USD | 1,290,000.00 USD | 49,670.00 USD | 63,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 1,030,000.00 USD | 1,030,000.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 1,460,000.00 USD | 1,460,000.00 USD | 33,660.00 USD | 32,070.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,120,000.00 USD | 1,120,000.00 USD | 53,760.00 USD | 26,310.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 1,550,000.00 USD | 1,550,000.00 USD | 17,360.00 USD | 30,490.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,270,000.00 USD | 1,270,000.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1698` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 1,310,000.00 USD | 1,310,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1701` | 1,780,000.00 USD | 1,780,000.00 USD | 55,170.00 USD | 33,810.00 USD | 72,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,340,000.00 USD | 1,340,000.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 712.66 USD | 22,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1707` | 1,490,000.00 USD | 1,490,000.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1707` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1710` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 1,540,000.00 USD | 1,540,000.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1716` | 1,590,000.00 USD | 1,590,000.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,660,000.00 USD | 1,660,000.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1719` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 1,830,000.00 USD | 1,830,000.00 USD | 82,880.00 USD | 28,200.00 USD | 54,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 2,510,000.00 USD | 2,510,000.00 USD | 142,900.00 USD | 12,590.00 USD | 342,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 1,910,000.00 USD | 1,910,000.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1725` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 37,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 1,940,000.00 USD | 1,940,000.00 USD | 18,490.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 3,010,000.00 USD | 3,010,000.00 USD | 452,310.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 1,960,000.00 USD | 1,960,000.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,010,000.00 USD | 2,010,000.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 1,770.00 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1746` | 2,050,000.00 USD | 2,050,000.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 2,170,000.00 USD | 2,170,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 3,210,000.00 USD | 3,210,000.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 2,230,000.00 USD | 2,230,000.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 277,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 2,290,000.00 USD | 2,290,000.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 3,710,000.00 USD | 3,710,000.00 USD | 52,970.00 USD | 0.00 USD | 169,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 2,400,000.00 USD | 2,400,000.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 3,970,000.00 USD | 3,970,000.00 USD | 209,580.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 2,580,000.00 USD | 2,580,000.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 4,370,000.00 USD | 4,370,000.00 USD | 284,080.00 USD | 83,160.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 2,690,000.00 USD | 2,690,000.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 4,710,000.00 USD | 4,710,000.00 USD | 144,160.00 USD | 158,980.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 2,810,000.00 USD | 2,810,000.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 5,020,000.00 USD | 5,020,000.00 USD | 176,410.00 USD | 117,990.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 2,910,000.00 USD | 2,910,000.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 5,210,000.00 USD | 5,210,000.00 USD | 61,490.00 USD | 91,680.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 2,970,000.00 USD | 2,970,000.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 5,400,000.00 USD | 5,400,000.00 USD | 103,820.00 USD | 86,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 25,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1776` | 3,020,000.00 USD | 3,020,000.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 5,600,000.00 USD | 5,600,000.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 3,140,000.00 USD | 3,140,000.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 5,830,000.00 USD | 5,830,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 5,890,000.00 USD | 5,890,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 3,250,000.00 USD | 3,250,000.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 6,140,000.00 USD | 6,140,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 25,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1788` | 3,290,000.00 USD | 3,290,000.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 6,250,000.00 USD | 6,250,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 6,430,000.00 USD | 6,430,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 3,370,000.00 USD | 3,370,000.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 6,530,000.00 USD | 6,530,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 2,560.00 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,420,000.00 USD | 3,420,000.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 6,570,000.00 USD | 6,570,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 3,460,000.00 USD | 3,460,000.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 6,690,000.00 USD | 6,690,000.00 USD | 12,940.00 USD | 38,070.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,510,000.00 USD | 3,510,000.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 6,770,000.00 USD | 6,770,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1806` | 3,540,000.00 USD | 3,540,000.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1806` | 6,860,000.00 USD | 6,860,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,560,000.00 USD | 3,560,000.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 7,010,000.00 USD | 7,010,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,630,000.00 USD | 3,630,000.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 7,110,000.00 USD | 7,110,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,640,000.00 USD | 3,640,000.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 7,240,000.00 USD | 7,240,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 7,350,000.00 USD | 7,350,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 13,320.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 7,480,000.00 USD | 7,480,000.00 USD | 50,880.00 USD | 38,910.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,710,000.00 USD | 3,710,000.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 7,640,000.00 USD | 7,640,000.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,730,000.00 USD | 3,730,000.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 7,800,000.00 USD | 7,800,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 7,940,000.00 USD | 7,940,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,730,000.00 USD | 3,730,000.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 8,190,000.00 USD | 8,190,000.00 USD | 152,480.00 USD | 49,740.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 8,290,000.00 USD | 8,290,000.00 USD | 2,610.00 USD | 47,910.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 8,520,000.00 USD | 8,520,000.00 USD | 81,700.00 USD | 31,130.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 3,750,000.00 USD | 3,750,000.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 8,620,000.00 USD | 8,620,000.00 USD | 43,580.00 USD | 26,100.00 USD | 37,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 8,750,000.00 USD | 8,750,000.00 USD | 34,630.00 USD | 8,590.00 USD | 81,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 8,880,000.00 USD | 8,880,000.00 USD | 35,280.00 USD | 65,230.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 9,200,000.00 USD | 9,200,000.00 USD | 67,340.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,300,000.00 USD | 9,300,000.00 USD | 47,090.00 USD | 4,290.00 USD | 53,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 9,460,000.00 USD | 9,460,000.00 USD | 41,470.00 USD | 21,110.00 USD | 93,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 9,540,000.00 USD | 9,540,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 9,650,000.00 USD | 9,650,000.00 USD | 48,260.00 USD | 13,700.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 9,780,000.00 USD | 9,780,000.00 USD | 54,300.00 USD | 29,050.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 9,960,000.00 USD | 9,960,000.00 USD | 124,660.00 USD | 30,880.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 10,050,000.00 USD | 10,050,000.00 USD | 16,870.00 USD | 33,800.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 10,130,000.00 USD | 10,130,000.00 USD | 27,560.00 USD | 13,320.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1878` | 10,190,000.00 USD | 10,190,000.00 USD | 41,670.00 USD | 12,570.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 28,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 3,040.00 USD | 31,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2025` | 453.88 USD | 32,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 44,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 44,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 44,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 60,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 101,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 101,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 92,220.00 USD | 193,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 26,240.00 USD | 220,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 220,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 106.77 USD | 220,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 260.00 USD | 220,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 227,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 243,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 243,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 23,170.00 USD | 266,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 267,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 49,330.00 USD | 316,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 317,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 321,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 350,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 402,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2605` | 180,430.00 USD | 583,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 583,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 583,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 596,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 596,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 608,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 609,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2865` | 156.37 USD | 609,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 295,180.00 USD | 904,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 905,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 1,900.00 USD | 907,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 479.54 USD | 907,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3035` | 2,310.00 USD | 909,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 916,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 916,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 928,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 928,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3205` | 248.64 USD | 928,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 1,770,000.00 USD | 0.00 USD | 1,870.00 USD | `-76.48%` | `48,585,700,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,770,000.00 USD | 0.00 USD | 110.22 USD | `-74.65%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,770,000.00 USD | 0.00 USD | 170.00 USD | `-74.04%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0465` | 1,770,000.00 USD | 0.00 USD | 163,510.00 USD | `-71.59%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0475` | 1,600,000.00 USD | 0.00 USD | 121.77 USD | `-70.98%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,600,000.00 USD | 0.00 USD | 109.52 USD | `-69.76%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,600,000.00 USD | 0.00 USD | 461.29 USD | `-68.54%` | `8,957,000,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,600,000.00 USD | 0.00 USD | 924.32 USD | `-67.93%` | `17,606,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,600,000.00 USD | 0.00 USD | 5,230.00 USD | `-66.71%` | `95,884,500,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,590,000.00 USD | 0.00 USD | 15,650.00 USD | `-65.48%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,580,000.00 USD | 0.00 USD | 718.35 USD | `-64.87%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,580,000.00 USD | 0.00 USD | 1,100.00 USD | `-64.26%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,580,000.00 USD | 0.00 USD | 3,930.00 USD | `-63.04%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,570,000.00 USD | 0.00 USD | 373.83 USD | `-61.21%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0645` | 1,570,000.00 USD | 0.00 USD | 6,710.00 USD | `-60.60%` | `104,053,400,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,570,000.00 USD | 0.00 USD | 194.36 USD | `-59.37%` | `2,922,700,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,570,000.00 USD | 0.00 USD | 99,790.00 USD | `-58.76%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,470,000.00 USD | 0.00 USD | 313.22 USD | `-58.15%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,470,000.00 USD | 0.00 USD | 976.14 USD | `-57.54%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,460,000.00 USD | 0.00 USD | 2,970.00 USD | `-56.93%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,460,000.00 USD | 0.00 USD | 6,150.00 USD | `-56.32%` | `86,064,300,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,460,000.00 USD | 0.00 USD | 61,400.00 USD | `-55.71%` | `846,829,200,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,390,000.00 USD | 0.00 USD | 2,440.00 USD | `-55.10%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,390,000.00 USD | 0.00 USD | 226.17 USD | `-54.49%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,390,000.00 USD | 0.00 USD | 14,690.00 USD | `-53.27%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,380,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.43%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,370,000.00 USD | 0.00 USD | 18,860.00 USD | `-49.60%` | `228,584,300,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,350,000.00 USD | 0.00 USD | 1,890.00 USD | `-48.99%` | `22,623,800,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,350,000.00 USD | 0.00 USD | 2,580.00 USD | `-47.77%` | `30,172,300,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,350,000.00 USD | 0.00 USD | 20,320.00 USD | `-47.16%` | `234,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,330,000.00 USD | 0.00 USD | 4,830.00 USD | `-46.55%` | `55,220,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,320,000.00 USD | 0.00 USD | 362.62 USD | `-45.93%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,320,000.00 USD | 0.00 USD | 501.81 USD | `-45.32%` | `5,606,800,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,320,000.00 USD | 0.00 USD | 113.80 USD | `-44.10%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,320,000.00 USD | 0.00 USD | 2,420.00 USD | `-43.49%` | `26,112,600,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,320,000.00 USD | 0.00 USD | 814.24 USD | `-42.88%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,320,000.00 USD | 0.00 USD | 1,510.00 USD | `-42.27%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,320,000.00 USD | 0.00 USD | 386.50 USD | `-41.66%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,320,000.00 USD | 0.00 USD | 3,530.00 USD | `-41.05%` | `36,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,310,000.00 USD | 0.00 USD | 2,020.00 USD | `-40.44%` | `20,694,000,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,310,000.00 USD | 0.00 USD | 2,810.00 USD | `-39.83%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,310,000.00 USD | 0.00 USD | 112,140.00 USD | `-39.21%` | `1,127,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,200,000.00 USD | 0.00 USD | 20,310.00 USD | `-38.60%` | `202,055,000,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,180,000.00 USD | 0.00 USD | 8,180.00 USD | `-36.77%` | `79,054,900,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,170,000.00 USD | 0.00 USD | 7,380.00 USD | `-36.16%` | `70,591,600,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,160,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.55%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,150,000.00 USD | 0.00 USD | 934.41 USD | `-34.94%` | `8,773,800,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,150,000.00 USD | 0.00 USD | 1,330.00 USD | `-34.33%` | `12,384,800,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,150,000.00 USD | 0.00 USD | 11,210.00 USD | `-33.72%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,140,000.00 USD | 0.00 USD | 640.52 USD | `-33.11%` | `5,849,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,140,000.00 USD | 0.00 USD | 13,820.00 USD | `-32.49%` | `125,027,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,130,000.00 USD | 0.00 USD | 425.50 USD | `-31.88%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,120,000.00 USD | 0.00 USD | 281.48 USD | `-30.66%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,120,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.05%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,120,000.00 USD | 0.00 USD | 1,640.00 USD | `-29.44%` | `14,227,900,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,110,000.00 USD | 0.00 USD | 6,230.00 USD | `-28.83%` | `53,476,700,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,110,000.00 USD | 0.00 USD | 7,420.00 USD | `-28.22%` | `63,146,600,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,100,000.00 USD | 0.00 USD | 26,330.00 USD | `-27.61%` | `222,158,200,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,070,000.00 USD | 0.00 USD | 1,830.00 USD | `-27.00%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,070,000.00 USD | 0.00 USD | 303.75 USD | `-25.77%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,070,000.00 USD | 0.00 USD | 18,250.00 USD | `-25.16%` | `149,015,600,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,050,000.00 USD | 0.00 USD | 50,640.00 USD | `-24.55%` | `410,038,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,000,000.00 USD | 0.00 USD | 844.86 USD | `-23.94%` | `6,786,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,000,000.00 USD | 0.00 USD | 134.66 USD | `-23.33%` | `1,073,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,000,000.00 USD | 0.00 USD | 29,370.00 USD | `-22.72%` | `232,151,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 972,700.00 USD | 0.00 USD | 9,780.00 USD | `-21.50%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 962,930.00 USD | 0.00 USD | 3,750.00 USD | `-20.89%` | `28,932,500,000,000.00` |
| `Live` | `Long` | `0.1305` | 959,180.00 USD | 0.00 USD | 16,660.00 USD | `-20.28%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 942,520.00 USD | 0.00 USD | 4,660.00 USD | `-19.67%` | `35,435,800,000,000.00` |
| `Live` | `Long` | `0.1325` | 937,860.00 USD | 0.00 USD | 17,180.00 USD | `-19.05%` | `129,631,300,000,000.00` |
| `Live` | `Long` | `0.1335` | 920,690.00 USD | 0.00 USD | 51,200.00 USD | `-18.44%` | `383,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 869,490.00 USD | 0.00 USD | 44,860.00 USD | `-17.83%` | `333,519,800,000,000.00` |
| `Live` | `Long` | `0.1355` | 824,630.00 USD | 0.00 USD | 1,440.00 USD | `-17.22%` | `10,635,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 823,190.00 USD | 0.00 USD | 10,630.00 USD | `-16.61%` | `77,872,500,000,000.00` |
| `Live` | `Long` | `0.1375` | 812,560.00 USD | 0.00 USD | 13,710.00 USD | `-16.00%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 798,850.00 USD | 0.00 USD | 16,480.00 USD | `-15.39%` | `119,008,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 782,370.00 USD | 0.00 USD | 5,960.00 USD | `-14.78%` | `42,721,100,000,000.00` |
| `Live` | `Long` | `0.1405` | 776,410.00 USD | 0.00 USD | 5,540.00 USD | `-14.17%` | `39,457,900,000,000.00` |
| `Live` | `Long` | `0.1415` | 770,860.00 USD | 0.00 USD | 16,690.00 USD | `-13.56%` | `117,929,900,000,000.00` |
| `Live` | `Long` | `0.1425` | 754,180.00 USD | 0.00 USD | 499,990.00 USD | `-12.95%` | `3,508,714,600,000,000.00` |
| `Live` | `Long` | `0.1435` | 254,180.00 USD | 0.00 USD | 18,970.00 USD | `-12.33%` | `132,163,100,000,000.00` |
| `Live` | `Long` | `0.1445` | 235,220.00 USD | 0.00 USD | 9,510.00 USD | `-11.72%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 225,700.00 USD | 0.00 USD | 92,080.00 USD | `-11.11%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 133,630.00 USD | 0.00 USD | 31,840.00 USD | `-10.50%` | `217,358,100,000,000.00` |
| `Live` | `Long` | `0.1475` | 101,780.00 USD | 0.00 USD | 87,010.00 USD | `-9.89%` | `589,875,400,000,000.00` |
| `Live` | `Long` | `0.1485` | 14,780.00 USD | 0.00 USD | 2,290.00 USD | `-9.28%` | `15,410,500,000,000.00` |
| `Live` | `Long` | `0.1495` | 12,490.00 USD | 0.00 USD | 1,720.00 USD | `-8.67%` | `11,513,300,000,000.00` |
| `Live` | `Long` | `0.1505` | 10,770.00 USD | 0.00 USD | 1,470.00 USD | `-8.06%` | `9,790,700,000,000.00` |
| `Live` | `Long` | `0.1515` | 9,290.00 USD | 0.00 USD | 945.33 USD | `-7.45%` | `6,239,800,000,000.00` |
| `Live` | `Long` | `0.1535` | 8,350.00 USD | 0.00 USD | 8,350.00 USD | `-6.23%` | `54,379,100,000,000.00` |
| `Live` | `Short` | `0.1545` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | `-5.61%` | `10,636,500,000,000.00` |
| `Live` | `Short` | `0.1635` | 3,110.00 USD | 1,460.00 USD | 0.00 USD | `-0.12%` | `8,949,600,000,000.00` |
| `Live` | `Short` | `0.1645` | 3,230.00 USD | 118.90 USD | 0.00 USD | `+0.49%` | `722,800,000,000.00` |
| `Live` | `Short` | `0.1665` | 16,690.00 USD | 13,460.00 USD | 0.00 USD | `+1.72%` | `80,863,400,000,000.00` |
| `Live` | `Short` | `0.1675` | 21,330.00 USD | 4,640.00 USD | 0.00 USD | `+2.33%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1705` | 22,050.00 USD | 712.66 USD | 0.00 USD | `+4.16%` | `4,179,800,000,000.00` |
| `Live` | `Short` | `0.1715` | 23,530.00 USD | 1,480.00 USD | 0.00 USD | `+4.77%` | `8,642,500,000,000.00` |
| `Live` | `Short` | `0.1745` | 25,300.00 USD | 1,770.00 USD | 0.00 USD | `+6.60%` | `10,149,600,000,000.00` |
| `Live` | `Short` | `0.1775` | 25,620.00 USD | 316.07 USD | 0.00 USD | `+8.44%` | `1,780,700,000,000.00` |
| `Live` | `Short` | `0.1785` | 25,750.00 USD | 138.82 USD | 0.00 USD | `+9.05%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1795` | 28,310.00 USD | 2,560.00 USD | 0.00 USD | `+9.66%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1945` | 28,940.00 USD | 623.68 USD | 0.00 USD | `+18.82%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 31,980.00 USD | 3,040.00 USD | 0.00 USD | `+20.65%` | `15,399,700,000,000.00` |
| `Live` | `Short` | `0.2025` | 32,430.00 USD | 453.88 USD | 0.00 USD | `+23.71%` | `2,241,400,000,000.00` |
| `Live` | `Short` | `0.2055` | 44,030.00 USD | 11,590.00 USD | 0.00 USD | `+25.54%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 44,220.00 USD | 198.08 USD | 0.00 USD | `+27.37%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 44,390.00 USD | 164.23 USD | 0.00 USD | `+27.99%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 60,080.00 USD | 15,690.00 USD | 0.00 USD | `+30.43%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 101,410.00 USD | 41,330.00 USD | 0.00 USD | `+31.65%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 101,630.00 USD | 213.22 USD | 0.00 USD | `+32.87%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 193,850.00 USD | 92,220.00 USD | 0.00 USD | `+34.09%` | `420,150,900,000,000.00` |
| `Live` | `Short` | `0.2205` | 220,090.00 USD | 26,240.00 USD | 0.00 USD | `+34.71%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 220,200.00 USD | 114.52 USD | 0.00 USD | `+36.54%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 220,310.00 USD | 106.77 USD | 0.00 USD | `+37.15%` | `475,600,000,000.00` |
| `Live` | `Short` | `0.2255` | 220,570.00 USD | 260.00 USD | 0.00 USD | `+37.76%` | `1,153,000,000,000.00` |
| `Live` | `Short` | `0.2295` | 227,390.00 USD | 6,820.00 USD | 0.00 USD | `+40.20%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 243,320.00 USD | 15,930.00 USD | 0.00 USD | `+43.87%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 243,420.00 USD | 102.62 USD | 0.00 USD | `+45.09%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2395` | 266,590.00 USD | 23,170.00 USD | 0.00 USD | `+46.31%` | `96,737,600,000,000.00` |
| `Live` | `Short` | `0.2425` | 267,390.00 USD | 796.25 USD | 0.00 USD | `+48.15%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2455` | 316,720.00 USD | 49,330.00 USD | 0.00 USD | `+49.98%` | `200,947,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 317,270.00 USD | 546.54 USD | 0.00 USD | `+55.48%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 321,130.00 USD | 3,870.00 USD | 0.00 USD | `+56.70%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 350,040.00 USD | 28,910.00 USD | 0.00 USD | `+57.31%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 402,660.00 USD | 52,620.00 USD | 0.00 USD | `+57.92%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2605` | 583,090.00 USD | 180,430.00 USD | 0.00 USD | `+59.14%` | `692,636,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 583,250.00 USD | 154.94 USD | 0.00 USD | `+59.75%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 583,470.00 USD | 226.51 USD | 0.00 USD | `+64.03%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 596,720.00 USD | 13,240.00 USD | 0.00 USD | `+65.86%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 596,930.00 USD | 214.21 USD | 0.00 USD | `+66.47%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 608,530.00 USD | 11,600.00 USD | 0.00 USD | `+67.70%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 609,010.00 USD | 482.84 USD | 0.00 USD | `+70.75%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2865` | 609,170.00 USD | 156.37 USD | 0.00 USD | `+75.03%` | `545,800,000,000.00` |
| `Live` | `Short` | `0.2915` | 904,350.00 USD | 295,180.00 USD | 0.00 USD | `+78.08%` | `1,012,619,700,000,000.00` |
| `Live` | `Short` | `0.2925` | 905,140.00 USD | 794.52 USD | 0.00 USD | `+78.69%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2995` | 907,040.00 USD | 1,900.00 USD | 0.00 USD | `+82.97%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3015` | 907,520.00 USD | 479.54 USD | 0.00 USD | `+84.19%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3035` | 909,830.00 USD | 2,310.00 USD | 0.00 USD | `+85.41%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3075` | 916,120.00 USD | 6,290.00 USD | 0.00 USD | `+87.86%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 916,480.00 USD | 363.72 USD | 0.00 USD | `+88.47%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 928,410.00 USD | 11,930.00 USD | 0.00 USD | `+89.69%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3175` | 928,630.00 USD | 227.49 USD | 0.00 USD | `+93.96%` | `716,500,000,000.00` |
| `Live` | `Short` | `0.3205` | 928,880.00 USD | 248.64 USD | 0.00 USD | `+95.80%` | `775,800,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1305` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1308` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD |
| `7D` | `0.1311` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 6,470.00 USD | 4,610.00 USD | 0.00 USD |
| `7D` | `0.1314` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 0.00 USD | 4,010.00 USD | 4,800.00 USD |
| `7D` | `0.1317` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 14,240.00 USD | 4,840.00 USD | 3,260.00 USD |
| `7D` | `0.1320` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 0.00 USD | 2,780.00 USD | 22,910.00 USD |
| `7D` | `0.1323` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 5,580.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `0.1326` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 7,890.00 USD | 10,270.00 USD | 11,280.00 USD |
| `7D` | `0.1329` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 11,110.00 USD | 5,000.00 USD | 4,970.00 USD |
| `7D` | `0.1332` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 17,000.00 USD | 1,900.00 USD | 9,950.00 USD |
| `7D` | `0.1335` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 0.00 USD | 4,190.00 USD | 2,300.00 USD |
| `7D` | `0.1338` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 2,830.00 USD | 9,530.00 USD | 32,660.00 USD |
| `7D` | `0.1341` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 6,330.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `0.1344` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 6,410.00 USD | 5,790.00 USD | 13,130.00 USD |
| `7D` | `0.1347` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 31,170.00 USD | 5,000.00 USD | 15,770.00 USD |
| `7D` | `0.1350` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 7,650.00 USD | 8,440.00 USD | 23,660.00 USD |
| `7D` | `0.1353` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 7,440.00 USD | 3,540.00 USD | 8,790.00 USD |
| `7D` | `0.1356` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 12,450.00 USD | 8,640.00 USD | 9,380.00 USD |
| `7D` | `0.1359` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 25,240.00 USD | 6,700.00 USD | 8,770.00 USD |
| `7D` | `0.1362` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 3,340.00 USD | 3,690.00 USD | 4,690.00 USD |
| `7D` | `0.1365` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 11,660.00 USD | 1,460.00 USD | 0.00 USD |
| `7D` | `0.1368` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `7D` | `0.1371` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1374` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1377` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 5,780.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1380` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 8,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1383` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `7D` | `0.1386` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `0.1392` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1395` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1398` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 6,210.00 USD | 4,200.00 USD | 22,820.00 USD |
| `7D` | `0.1401` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD |
| `1D` | `0.1413` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD |
| `7D` | `0.1416` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1419` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1419` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1422` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1422` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1425` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD |
| `1D` | `0.1428` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1431` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `0.1434` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1434` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 25,940.00 USD |
| `1D` | `0.1437` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD |
| `7D` | `0.1437` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1440` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD |
| `7D` | `0.1440` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 9,760.00 USD | 2,750.00 USD | 3,610.00 USD |
| `1D` | `0.1443` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD |
| `7D` | `0.1443` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1446` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD |
| `1D` | `0.1452` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1452` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 0.00 USD | 10,680.00 USD | 14,180.00 USD |
| `1D` | `0.1455` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1458` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD |
| `1D` | `0.1461` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD |
| `1D` | `0.1464` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD |
| `7D` | `0.1464` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1467` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD |
| `7D` | `0.1467` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 9,720.00 USD | 5,520.00 USD | 89,310.00 USD |
| `1D` | `0.1470` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD |
| `7D` | `0.1470` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1473` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD |
| `7D` | `0.1473` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 19,430.00 USD | 8,790.00 USD | 14,170.00 USD |
| `1D` | `0.1476` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD |
| `7D` | `0.1476` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 61,700.00 USD | 14,780.00 USD | 81,130.00 USD |
| `1D` | `0.1479` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD |
| `7D` | `0.1479` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 67,510.00 USD | 39,730.00 USD | 43,970.00 USD |
| `1D` | `0.1482` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD |
| `7D` | `0.1482` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 41,960.00 USD | 20,720.00 USD | 59,880.00 USD |
| `1D` | `0.1485` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD |
| `7D` | `0.1485` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 40,660.00 USD | 7,340.00 USD | 163,400.00 USD |
| `1D` | `0.1488` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD |
| `7D` | `0.1488` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 44,530.00 USD | 3,130.00 USD | 10,390.00 USD |
| `1D` | `0.1491` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 40,720.00 USD | 15,530.00 USD | 16,610.00 USD |
| `7D` | `0.1491` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 43,480.00 USD | 22,050.00 USD | 85,470.00 USD |
| `1D` | `0.1494` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD |
| `7D` | `0.1494` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1497` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD |
| `7D` | `0.1497` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 20,880.00 USD | 17,180.00 USD | 188,330.00 USD |
| `1D` | `0.1500` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD |
| `7D` | `0.1500` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `1D` | `0.1503` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD |
| `7D` | `0.1503` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `1D` | `0.1506` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD |
| `7D` | `0.1506` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 129,280.00 USD | 18,020.00 USD | 217,020.00 USD |
| `1D` | `0.1509` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD |
| `7D` | `0.1509` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 166,980.00 USD | 9,550.00 USD | 82,990.00 USD |
| `1D` | `0.1512` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 0.00 USD | 8,620.00 USD | 50,470.00 USD |
| `1D` | `0.1515` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD |
| `7D` | `0.1515` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 0.00 USD | 13,330.00 USD | 369,440.00 USD |
| `1D` | `0.1518` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD |
| `7D` | `0.1518` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 96,310.00 USD | 15,160.00 USD | 108,900.00 USD |
| `1D` | `0.1521` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD |
| `7D` | `0.1521` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 0.00 USD | 11,720.00 USD | 144,600.00 USD |
| `1D` | `0.1524` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1524` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1527` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 0.00 USD | 35,230.00 USD | 0.00 USD |
| `1D` | `0.1530` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD |
| `7D` | `0.1530` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD |
| `7D` | `0.1533` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 35,470.00 USD | 16,570.00 USD | 0.00 USD |
| `1D` | `0.1536` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1536` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 2,910.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1539` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `1D` | `0.1542` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1542` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1548` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD |
| `7D` | `0.1548` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 0.00 USD | 15,410.00 USD | 89,090.00 USD |
| `1D` | `0.1551` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD |
| `7D` | `0.1551` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 0.00 USD | 21,410.00 USD | 0.00 USD |
| `1D` | `0.1554` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1554` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD |
| `7D` | `0.1557` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 0.00 USD | 4,510.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1560` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 0.00 USD | 16,120.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD |
| `7D` | `0.1563` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD |
| `1D` | `0.1566` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD |
| `7D` | `0.1566` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 70,940.00 USD | 29,160.00 USD | 0.00 USD |
| `1D` | `0.1569` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD |
| `7D` | `0.1569` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 138,980.00 USD | 5,100.00 USD | 151,620.00 USD |
| `1D` | `0.1572` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD |
| `7D` | `0.1572` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 208,130.00 USD | 42,920.00 USD | 58,840.00 USD |
| `1D` | `0.1575` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1575` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 23,310.00 USD | 88,960.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1578` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 107,560.00 USD | 84,670.00 USD | 0.00 USD |
| `1D` | `0.1581` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD |
| `7D` | `0.1581` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 140,060.00 USD | 25,110.00 USD | 0.00 USD |
| `1D` | `0.1584` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD |
| `7D` | `0.1584` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1587` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD |
| `7D` | `0.1587` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 69,180.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 15,370.00 USD | 28,520.00 USD | 41,850.00 USD |
| `7D` | `0.1590` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 24,840.00 USD | 12,590.00 USD | 0.00 USD |
| `1D` | `0.1593` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD |
| `7D` | `0.1593` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1596` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 10,260.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `0.1596` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 74,230.00 USD | 0.00 USD |
| `1D` | `0.1599` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1599` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 0.00 USD | 55,380.00 USD | 75,810.00 USD |
| `1D` | `0.1602` | 997,600.00 USD | 0.00 USD | 997,600.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD |
| `7D` | `0.1602` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 46,490.00 USD | 50,120.00 USD |
| `1D` | `0.1605` | 940,330.00 USD | 0.00 USD | 940,330.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1605` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 150,770.00 USD | 16,950.00 USD | 264,260.00 USD |
| `1D` | `0.1608` | 936,490.00 USD | 0.00 USD | 936,490.00 USD | 34,860.00 USD | 7,790.00 USD | 79,710.00 USD |
| `7D` | `0.1608` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 129,610.00 USD | 0.00 USD | 289,270.00 USD |
| `1D` | `0.1611` | 814,120.00 USD | 0.00 USD | 814,120.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD |
| `7D` | `0.1611` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 196,320.00 USD | 0.00 USD | 322,550.00 USD |
| `1D` | `0.1614` | 777,340.00 USD | 0.00 USD | 777,340.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `7D` | `0.1614` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 323,670.00 USD | 0.00 USD | 219,740.00 USD |
| `7D` | `0.1617` | 899,980.00 USD | 0.00 USD | 899,980.00 USD | 126,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1620` | 738,670.00 USD | 0.00 USD | 738,670.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD |
| `1D` | `0.1623` | 709,770.00 USD | 0.00 USD | 709,770.00 USD | 65,520.00 USD | 22,690.00 USD | 17,520.00 USD |
| `7D` | `0.1623` | 773,640.00 USD | 0.00 USD | 773,640.00 USD | 49,670.00 USD | 156,860.00 USD | 0.00 USD |
| `1D` | `0.1626` | 604,040.00 USD | 0.00 USD | 604,040.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD |
| `7D` | `0.1626` | 567,100.00 USD | 0.00 USD | 567,100.00 USD | 0.00 USD | 71,120.00 USD | 136,760.00 USD |
| `1D` | `0.1629` | 464,670.00 USD | 0.00 USD | 464,670.00 USD | 20,520.00 USD | 3,520.00 USD | 104,120.00 USD |
| `7D` | `0.1629` | 359,220.00 USD | 0.00 USD | 359,220.00 USD | 147,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 336,510.00 USD | 0.00 USD | 336,510.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 214,210.00 USD | 0.00 USD | 214,210.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1638` | 205,520.00 USD | 0.00 USD | 205,520.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1638` | 211,510.00 USD | 0.00 USD | 211,510.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `0.1641` | 176,400.00 USD | 0.00 USD | 176,400.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1641` | 187,950.00 USD | 0.00 USD | 187,950.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1644` | 157,330.00 USD | 0.00 USD | 157,330.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD |
| `7D` | `0.1644` | 158,710.00 USD | 0.00 USD | 158,710.00 USD | 0.00 USD | 34,100.00 USD | 44,540.00 USD |
| `1D` | `0.1647` | 94,830.00 USD | 0.00 USD | 94,830.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD |
| `7D` | `0.1647` | 80,070.00 USD | 0.00 USD | 80,070.00 USD | 0.00 USD | 4,800.00 USD | 0.00 USD |
| `1D` | `0.1650` | 69,020.00 USD | 0.00 USD | 69,020.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD |
| `7D` | `0.1650` | 75,280.00 USD | 0.00 USD | 75,280.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `7D` | `0.1659` | 68,280.00 USD | 0.00 USD | 68,280.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1660` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 36,390.00 USD | 0.00 USD | 36,390.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD |
| `7D` | `0.1662` | 84,060.00 USD | 84,060.00 USD | 0.00 USD | 84,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1663` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1665` | 100,320.00 USD | 100,320.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD |
| `7D` | `0.1665` | 241,140.00 USD | 241,140.00 USD | 0.00 USD | 87,050.00 USD | 12,670.00 USD | 57,360.00 USD |
| `1D` | `0.1668` | 146,270.00 USD | 146,270.00 USD | 0.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD |
| `7D` | `0.1668` | 379,340.00 USD | 379,340.00 USD | 0.00 USD | 11,410.00 USD | 39,630.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 175,440.00 USD | 175,440.00 USD | 0.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1671` | 594,030.00 USD | 594,030.00 USD | 0.00 USD | 135,250.00 USD | 79,440.00 USD | 0.00 USD |
| `1D` | `0.1674` | 244,980.00 USD | 244,980.00 USD | 0.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD |
| `7D` | `0.1674` | 727,940.00 USD | 727,940.00 USD | 0.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 284,440.00 USD | 284,440.00 USD | 0.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD |
| `7D` | `0.1677` | 864,350.00 USD | 864,350.00 USD | 0.00 USD | 59,010.00 USD | 77,400.00 USD | 0.00 USD |
| `1D` | `0.1680` | 379,650.00 USD | 379,650.00 USD | 0.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD |
| `7D` | `0.1680` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 101,910.00 USD | 68,430.00 USD | 51,030.00 USD |
| `1D` | `0.1683` | 482,100.00 USD | 482,100.00 USD | 0.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD |
| `7D` | `0.1683` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 616,160.00 USD | 616,160.00 USD | 0.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD |
| `7D` | `0.1686` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 720,810.00 USD | 720,810.00 USD | 0.00 USD | 41,580.00 USD | 32,630.00 USD | 30,440.00 USD |
| `7D` | `0.1689` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 49,670.00 USD | 63,850.00 USD | 0.00 USD |
| `1D` | `0.1692` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD |
| `7D` | `0.1692` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 33,660.00 USD | 32,070.00 USD | 104,450.00 USD |
| `1D` | `0.1695` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 53,760.00 USD | 26,310.00 USD | 19,580.00 USD |
| `7D` | `0.1695` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 17,360.00 USD | 30,490.00 USD | 39,780.00 USD |
| `1D` | `0.1698` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD |
| `7D` | `0.1698` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1701` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `7D` | `0.1701` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 55,170.00 USD | 33,810.00 USD | 72,270.00 USD |
| `1D` | `0.1704` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1707` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD |
| `7D` | `0.1707` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 82,340.00 USD |
| `1D` | `0.1710` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD |
| `7D` | `0.1710` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1713` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `0.1713` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD |
| `7D` | `0.1716` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD |
| `7D` | `0.1719` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `0.1722` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 82,880.00 USD | 28,200.00 USD | 54,110.00 USD |
| `7D` | `0.1722` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 142,900.00 USD | 12,590.00 USD | 342,490.00 USD |
| `1D` | `0.1725` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD |
| `7D` | `0.1725` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,060.00 USD |
| `1D` | `0.1728` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 18,490.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1731` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 452,310.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1734` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD |
| `1D` | `0.1737` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD |
| `7D` | `0.1737` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD |
| `1D` | `0.1740` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD |
| `7D` | `0.1740` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1743` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1743` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1749` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD |
| `1D` | `0.1752` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD |
| `7D` | `0.1752` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 277,890.00 USD |
| `1D` | `0.1755` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD |
| `7D` | `0.1755` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 52,970.00 USD | 0.00 USD | 169,880.00 USD |
| `1D` | `0.1758` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD |
| `7D` | `0.1758` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 209,580.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1761` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD |
| `7D` | `0.1761` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 284,080.00 USD | 83,160.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD |
| `7D` | `0.1764` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 144,160.00 USD | 158,980.00 USD | 40,340.00 USD |
| `1D` | `0.1767` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD |
| `7D` | `0.1767` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 176,410.00 USD | 117,990.00 USD | 8,530.00 USD |
| `1D` | `0.1770` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD |
| `7D` | `0.1770` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 61,490.00 USD | 91,680.00 USD | 44,400.00 USD |
| `1D` | `0.1773` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD |
| `7D` | `0.1773` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 103,820.00 USD | 86,080.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD |
| `7D` | `0.1776` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1779` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD |
| `7D` | `0.1779` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1782` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD |
| `7D` | `0.1782` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1785` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD |
| `7D` | `0.1785` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1788` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1788` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1791` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD |
| `7D` | `0.1791` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD |
| `7D` | `0.1794` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1797` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD |
| `7D` | `0.1797` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1800` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD |
| `7D` | `0.1800` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 12,940.00 USD | 38,070.00 USD | 73,510.00 USD |
| `1D` | `0.1803` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD |
| `7D` | `0.1803` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1806` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD |
| `7D` | `0.1806` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1809` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD |
| `7D` | `0.1809` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1812` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD |
| `7D` | `0.1812` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1815` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `0.1815` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1818` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD |
| `7D` | `0.1818` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1821` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 13,320.00 USD | 6,430.00 USD |
| `7D` | `0.1821` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 50,880.00 USD | 38,910.00 USD | 41,820.00 USD |
| `1D` | `0.1824` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD |
| `7D` | `0.1824` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD |
| `1D` | `0.1827` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD |
| `7D` | `0.1827` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1830` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `0.1830` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1833` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD |
| `7D` | `0.1833` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 152,480.00 USD | 49,740.00 USD | 44,210.00 USD |
| `7D` | `0.1836` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 2,610.00 USD | 47,910.00 USD | 52,650.00 USD |
| `1D` | `0.1839` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD |
| `7D` | `0.1839` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 81,700.00 USD | 31,130.00 USD | 114,190.00 USD |
| `1D` | `0.1840` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD |
| `7D` | `0.1842` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 43,580.00 USD | 26,100.00 USD | 37,550.00 USD |
| `7D` | `0.1845` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 34,630.00 USD | 8,590.00 USD | 81,890.00 USD |
| `7D` | `0.1848` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 35,280.00 USD | 65,230.00 USD | 32,800.00 USD |
| `7D` | `0.1851` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 67,340.00 USD | 28,290.00 USD | 220,580.00 USD |
| `7D` | `0.1854` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 47,090.00 USD | 4,290.00 USD | 53,990.00 USD |
| `7D` | `0.1857` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 41,470.00 USD | 21,110.00 USD | 93,850.00 USD |
| `7D` | `0.1860` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD |
| `7D` | `0.1863` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 48,260.00 USD | 13,700.00 USD | 46,280.00 USD |
| `7D` | `0.1866` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 54,300.00 USD | 29,050.00 USD | 39,240.00 USD |
| `7D` | `0.1869` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 124,660.00 USD | 30,880.00 USD | 29,700.00 USD |
| `7D` | `0.1872` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 16,870.00 USD | 33,800.00 USD | 36,780.00 USD |
| `7D` | `0.1875` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 27,560.00 USD | 13,320.00 USD | 36,560.00 USD |
| `7D` | `0.1878` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 41,670.00 USD | 12,570.00 USD | 7,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `189.19M` | Total OI Tokens: `1,139,585,759.9 ARB`
  * 1h OI Change: `+0.21%` | 4h OI Change: `+6.56%` | 24h OI Change: `-14.36%`
  * Exchange Breakdown: Binance=`42.84M` | Bybit=`26.85M` | OKX=`14.74M` | Hyperliquid=`13.36M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.83K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0041%` | **USDT OKX** | `0.0062%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0060%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0086%` | **USDT Bitget** | `-0.0074%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `52.64%` | `47.36%` | `1.11` | 1,070,000.00 USD |
| `15M` | `Binance` | `51.51%` | `48.49%` | `1.06` | 394,330.00 USD |
| `15M` | `OKX` | `57.02%` | `42.98%` | `1.33` | 141,410.00 USD |
| `15M` | `Bybit` | `53.96%` | `46.04%` | `1.17` | 165,290.00 USD |
| `15M` | `KuCoin` | `46.25%` | `53.75%` | `0.86` | 62,640.00 USD |
| `15M` | `Gate` | `61.77%` | `38.23%` | `1.62` | 9,940.00 USD |
| `15M` | `Bitget` | `80.16%` | `19.84%` | `4.04` | 22,270.00 USD |
| `15M` | `BingX` | `43.65%` | `56.35%` | `0.77` | 24,100.00 USD |
| `15M` | `MEXC` | `56.35%` | `43.65%` | `1.29` | 32,480.00 USD |
| `15M` | `Bitunix` | `54.75%` | `45.25%` | `1.21` | 10,910.00 USD |
| `15M` | `Hyperliquid` | `72.56%` | `27.44%` | `2.64` | 6,550.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.88%` | `51.12%` | `0.96` | 192,210.00 USD |
| `15M` | `Crypto.com` | `18.69%` | `81.31%` | `0.23` | 2.14 USD |
| `15M` | `WhiteBIT` | `50.9%` | `49.1%` | `1.04` | 5,990.00 USD |
| `15M` | `HTX` | `47.66%` | `52.34%` | `0.91` | 1.30 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 10.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.94%` | `55.06%` | `0.82` | 2,050.00 USD |
| `15M` | `Whale Positions` | `51.51%` | `48.49%` | `1.06` | 394,330.00 USD |
| `15M` | `Global Accounts` | `52.64%` | `47.36%` | `1.11` | 1,070,000.00 USD |
| `1H` | `ARB` | `54.29%` | `45.71%` | `1.19` | 5,160,000.00 USD |
| `1H` | `Binance` | `55.25%` | `44.75%` | `1.23` | 2,010,000.00 USD |
| `1H` | `OKX` | `54.02%` | `45.98%` | `1.17` | 617,820.00 USD |
| `1H` | `Bybit` | `59.7%` | `40.3%` | `1.48` | 642,700.00 USD |
| `1H` | `KuCoin` | `49.48%` | `50.52%` | `0.98` | 265,210.00 USD |
| `1H` | `Gate` | `34.26%` | `65.74%` | `0.52` | 53,620.00 USD |
| `1H` | `Bitget` | `71.46%` | `28.54%` | `2.50` | 102,630.00 USD |
| `1H` | `BingX` | `45.89%` | `54.11%` | `0.85` | 118,860.00 USD |
| `1H` | `MEXC` | `38.33%` | `61.67%` | `0.62` | 153,170.00 USD |
| `1H` | `Bitunix` | `73.71%` | `26.29%` | `2.80` | 99,280.00 USD |
| `1H` | `Hyperliquid` | `88.9%` | `11.1%` | `8.01` | 61,130.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.87%` | `51.13%` | `0.96` | 994,030.00 USD |
| `1H` | `Crypto.com` | `17.99%` | `82.01%` | `0.22` | 4.50 USD |
| `1H` | `WhiteBIT` | `61.42%` | `38.58%` | `1.59` | 39,700.00 USD |
| `1H` | `HTX` | `30.93%` | `69.07%` | `0.45` | 1,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.84%` | `6.16%` | `15.23` | 162.25 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.98%` | `56.02%` | `0.79` | 10,140.00 USD |
| `1H` | `Whale Positions` | `55.25%` | `44.75%` | `1.23` | 2,010,000.00 USD |
| `1H` | `Global Accounts` | `54.29%` | `45.71%` | `1.19` | 5,160,000.00 USD |
| `4H` | `ARB` | `48.77%` | `51.23%` | `0.95` | 19,870,000.00 USD |
| `4H` | `Binance` | `50.57%` | `49.43%` | `1.02` | 6,980,000.00 USD |
| `4H` | `OKX` | `49.55%` | `50.45%` | `0.98` | 2,220,000.00 USD |
| `4H` | `Bybit` | `53.16%` | `46.84%` | `1.13` | 1,990,000.00 USD |
| `4H` | `KuCoin` | `50.07%` | `49.93%` | `1.00` | 1,810,000.00 USD |
| `4H` | `Gate` | `48.03%` | `51.97%` | `0.92` | 498,040.00 USD |
| `4H` | `Bitget` | `49.67%` | `50.33%` | `0.99` | 1,860,000.00 USD |
| `4H` | `BingX` | `37.7%` | `62.3%` | `0.61` | 1,930,000.00 USD |
| `4H` | `MEXC` | `50.23%` | `49.77%` | `1.01` | 877,990.00 USD |
| `4H` | `Bitunix` | `43.08%` | `56.92%` | `0.76` | 300,510.00 USD |
| `4H` | `Hyperliquid` | `57.71%` | `42.29%` | `1.36` | 250,750.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.96%` | `50.04%` | `1.00` | 783,470.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `31.79%` | `68.21%` | `0.47` | 291,230.00 USD |
| `4H` | `HTX` | `35.75%` | `64.25%` | `0.56` | 4,640.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `55.1%` | `44.9%` | `1.23` | 7,410.00 USD |
| `4H` | `Aster` | `13.74%` | `86.26%` | `0.16` | 72,630.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `15.23%` | `84.77%` | `0.18` | 14,690.00 USD |
| `4H` | `Whale Positions` | `50.57%` | `49.43%` | `1.02` | 6,980,000.00 USD |
| `4H` | `Global Accounts` | `48.77%` | `51.23%` | `0.95` | 19,870,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,684,179.28 USD | 761,022.88 USD | 923,156.41 USD | -162,133.53 USD | `-9.63%` | `12B / 13S` |
| `5:00 UTC` | `0.1637` | `0.1631` | `0.1637` | `0.1639` | `0.1618` | 1,849,966.09 USD | 605,282.83 USD | 1,244,683.26 USD | -639,400.43 USD | `-34.56%` | `9B / 30S` |
| `0:00 UTC` | `0.1655` | `0.1648` | `0.1655` | `0.1660` | `0.1635` | 1,718,232.82 USD | 746,856.42 USD | 971,376.40 USD | -224,519.98 USD | `-13.07%` | `15B / 23S` |
| `5:00 UTC` | `0.1657` | `0.1657` | `0.1657` | `0.1663` | `0.1649` | 1,541,284.70 USD | 631,060.07 USD | 910,224.63 USD | -279,164.57 USD | `-18.11%` | `10B / 51S` |
| `0:00 UTC` | `0.1657` | `0.1656` | `0.1657` | `0.1665` | `0.1649` | 1,537,020.59 USD | 918,105.56 USD | 618,915.03 USD | 299,190.54 USD | `+19.47%` | `31B / 25S` |
| `5:00 UTC` | `0.1659` | `0.1660` | `0.1659` | `0.1663` | `0.1653` | 206,490.16 USD | 79,839.92 USD | 126,650.25 USD | -46,810.33 USD | `-22.67%` | `9B / 34S` |

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
| `5m` | 26,250.00 USD | -100,590.00 USD | **`DISTRIBUTION`** |
| `15m` | -20,410.00 USD | 195,930.00 USD | **`ACCUMULATION`** |
| `30m` | -66,070.00 USD | -462,490.00 USD | **`DISTRIBUTION`** |
| `1h` | -19,250.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -32,710.00 USD | -1,880,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 143,070.00 USD | -397,540.00 USD | **`DISTRIBUTION`** |
| `6h` | -329,400.00 USD | -1,550,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -95,040.00 USD | -6,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,970,000.00 USD | -5,630,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,060,000.00 USD | -10,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,570,000.00 USD | -38,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,800,000.00 USD | -164,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+26.25K` | 15m=`-20.41K` | 1h=`-19.25K` | 24h=`-2.06M`
* Futures Capital Netflows: 5m=`-100.59K` | 15m=`+195.93K` | 1h=`-2.48M` | 24h=`-10.63M`
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
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
