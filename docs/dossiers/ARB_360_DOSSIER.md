# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:32:23 IST` (`2026-10-30 06:02:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1654` | `67,097,372` | 10,943,333.22 USD | -550,445.61 USD | `-5.03%` | -7,762,188.25 USD | `+0.66` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

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
| `7D` | `Long Liquidation` | `0.1305` | 8,590,000.00 USD | 8,590,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 959,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1308` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1311` | 8,580,000.00 USD | 8,580,000.00 USD | 6,470.00 USD | 4,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1314` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 4,010.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,660.00 USD | 942,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1317` | 8,560,000.00 USD | 8,560,000.00 USD | 14,240.00 USD | 4,840.00 USD | 3,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1320` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 2,780.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1323` | 8,510,000.00 USD | 8,510,000.00 USD | 5,580.00 USD | 0.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 17,180.00 USD | 937,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1326` | 8,500,000.00 USD | 8,500,000.00 USD | 7,890.00 USD | 10,270.00 USD | 11,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1329` | 8,470,000.00 USD | 8,470,000.00 USD | 11,110.00 USD | 5,000.00 USD | 4,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1332` | 8,450,000.00 USD | 8,450,000.00 USD | 17,000.00 USD | 1,900.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1335` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 4,190.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,200.00 USD | 920,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1338` | 8,420,000.00 USD | 8,420,000.00 USD | 2,830.00 USD | 9,530.00 USD | 32,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1341` | 8,370,000.00 USD | 8,370,000.00 USD | 6,330.00 USD | 0.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 8,360,000.00 USD | 8,360,000.00 USD | 6,410.00 USD | 5,790.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 44,860.00 USD | 869,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1347` | 8,330,000.00 USD | 8,330,000.00 USD | 31,170.00 USD | 5,000.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1350` | 8,280,000.00 USD | 8,280,000.00 USD | 7,650.00 USD | 8,440.00 USD | 23,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1353` | 8,240,000.00 USD | 8,240,000.00 USD | 7,440.00 USD | 3,540.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 824,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 8,220,000.00 USD | 8,220,000.00 USD | 12,450.00 USD | 8,640.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1359` | 8,190,000.00 USD | 8,190,000.00 USD | 25,240.00 USD | 6,700.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1362` | 8,150,000.00 USD | 8,150,000.00 USD | 3,340.00 USD | 3,690.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1365` | 8,140,000.00 USD | 8,140,000.00 USD | 11,660.00 USD | 1,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 823,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 8,130,000.00 USD | 8,130,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1371` | 8,110,000.00 USD | 8,110,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1374` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 812,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1377` | 8,070,000.00 USD | 8,070,000.00 USD | 5,780.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 8,060,000.00 USD | 8,060,000.00 USD | 8,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1383` | 8,060,000.00 USD | 8,060,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 16,480.00 USD | 798,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1386` | 8,010,000.00 USD | 8,010,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1395` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 782,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1398` | 7,920,000.00 USD | 7,920,000.00 USD | 6,210.00 USD | 4,200.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1401` | 7,890,000.00 USD | 7,890,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 5,540.00 USD | 776,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1413` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,690.00 USD | 770,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1419` | 4,770,000.00 USD | 4,770,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1419` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1422` | 4,770,000.00 USD | 4,770,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1422` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1425` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,990.00 USD | 754,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1428` | 4,740,000.00 USD | 4,740,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1431` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1434` | 4,740,000.00 USD | 4,740,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1434` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 25,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 254,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1437` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1437` | 7,820,000.00 USD | 7,820,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1440` | 4,710,000.00 USD | 4,710,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 7,790,000.00 USD | 7,790,000.00 USD | 9,760.00 USD | 2,750.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1443` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1443` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 235,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1446` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1452` | 4,670,000.00 USD | 4,670,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 10,680.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,630,000.00 USD | 4,630,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 225,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1458` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1464` | 4,610,000.00 USD | 4,610,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,840.00 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,580,000.00 USD | 4,580,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1467` | 7,740,000.00 USD | 7,740,000.00 USD | 9,720.00 USD | 5,520.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 4,560,000.00 USD | 4,560,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1470` | 7,630,000.00 USD | 7,630,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,540,000.00 USD | 4,540,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1473` | 7,620,000.00 USD | 7,620,000.00 USD | 19,430.00 USD | 8,790.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 87,010.00 USD | 101,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 4,390,000.00 USD | 4,390,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1476` | 7,580,000.00 USD | 7,580,000.00 USD | 61,700.00 USD | 14,780.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,140,000.00 USD | 4,140,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1479` | 7,420,000.00 USD | 7,420,000.00 USD | 67,510.00 USD | 39,730.00 USD | 43,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 3,970,000.00 USD | 3,970,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1482` | 7,270,000.00 USD | 7,270,000.00 USD | 41,960.00 USD | 20,720.00 USD | 59,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,800,000.00 USD | 3,800,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1485` | 7,150,000.00 USD | 7,150,000.00 USD | 40,660.00 USD | 7,340.00 USD | 163,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1488` | 3,660,000.00 USD | 3,660,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 6,940,000.00 USD | 6,940,000.00 USD | 44,530.00 USD | 3,130.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,630,000.00 USD | 3,630,000.00 USD | 40,720.00 USD | 15,530.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1491` | 6,880,000.00 USD | 6,880,000.00 USD | 43,480.00 USD | 22,050.00 USD | 85,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 3,560,000.00 USD | 3,560,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1494` | 6,730,000.00 USD | 6,730,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,720.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,480,000.00 USD | 3,480,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1497` | 6,670,000.00 USD | 6,670,000.00 USD | 20,880.00 USD | 17,180.00 USD | 188,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,420,000.00 USD | 3,420,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 6,440,000.00 USD | 6,440,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,400,000.00 USD | 3,400,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1503` | 6,370,000.00 USD | 6,370,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,470.00 USD | 10,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 3,170,000.00 USD | 3,170,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1506` | 6,330,000.00 USD | 6,330,000.00 USD | 129,280.00 USD | 18,020.00 USD | 217,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1509` | 5,970,000.00 USD | 5,970,000.00 USD | 166,980.00 USD | 9,550.00 USD | 82,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 2,760,000.00 USD | 2,760,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 8,620.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,750,000.00 USD | 2,750,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1515` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 13,330.00 USD | 369,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 9,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1518` | 2,370,000.00 USD | 2,370,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1518` | 5,270,000.00 USD | 5,270,000.00 USD | 96,310.00 USD | 15,160.00 USD | 108,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,280,000.00 USD | 2,280,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1521` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 11,720.00 USD | 144,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,200,000.00 USD | 2,200,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1524` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,160,000.00 USD | 2,160,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1527` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 35,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 2,130,000.00 USD | 2,130,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1530` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1533` | 4,830,000.00 USD | 4,830,000.00 USD | 35,470.00 USD | 16,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,350.00 USD | 8,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 2,060,000.00 USD | 2,060,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1536` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 2,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1539` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 2,020,000.00 USD | 2,020,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1542` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 1,980,000.00 USD | 1,980,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1545` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1548` | 1,940,000.00 USD | 1,940,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1548` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 15,410.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 1,900,000.00 USD | 1,900,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1551` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 21,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 1,850,000.00 USD | 1,850,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1554` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,810,000.00 USD | 1,810,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1557` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 4,510.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 1,790,000.00 USD | 1,790,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1560` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 16,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,770,000.00 USD | 1,770,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1563` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1566` | 1,720,000.00 USD | 1,720,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1566` | 4,400,000.00 USD | 4,400,000.00 USD | 70,940.00 USD | 29,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,590,000.00 USD | 1,590,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1569` | 4,300,000.00 USD | 4,300,000.00 USD | 138,980.00 USD | 5,100.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 1,460,000.00 USD | 1,460,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1572` | 4,000,000.00 USD | 4,000,000.00 USD | 208,130.00 USD | 42,920.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,330,000.00 USD | 1,330,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1575` | 3,690,000.00 USD | 3,690,000.00 USD | 23,310.00 USD | 88,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1578` | 3,580,000.00 USD | 3,580,000.00 USD | 107,560.00 USD | 84,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,320,000.00 USD | 1,320,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1581` | 3,390,000.00 USD | 3,390,000.00 USD | 140,060.00 USD | 25,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 1,300,000.00 USD | 1,300,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1584` | 3,220,000.00 USD | 3,220,000.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,190,000.00 USD | 1,190,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1587` | 3,140,000.00 USD | 3,140,000.00 USD | 69,180.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 1,080,000.00 USD | 1,080,000.00 USD | 15,370.00 USD | 28,520.00 USD | 51,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1590` | 2,980,000.00 USD | 2,980,000.00 USD | 24,840.00 USD | 12,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 988,040.00 USD | 988,040.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1593` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1596` | 892,990.00 USD | 892,990.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1596` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 74,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 878,020.00 USD | 878,020.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1599` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 55,380.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 864,410.00 USD | 864,410.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1602` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 46,490.00 USD | 50,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 807,140.00 USD | 807,140.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1605` | 2,630,000.00 USD | 2,630,000.00 USD | 150,770.00 USD | 16,950.00 USD | 264,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 803,290.00 USD | 803,290.00 USD | 34,860.00 USD | 7,790.00 USD | 77,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1608` | 2,190,000.00 USD | 2,190,000.00 USD | 129,610.00 USD | 0.00 USD | 289,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 682,820.00 USD | 682,820.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1611` | 1,770,000.00 USD | 1,770,000.00 USD | 196,320.00 USD | 0.00 USD | 322,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 646,030.00 USD | 646,030.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1614` | 1,260,000.00 USD | 1,260,000.00 USD | 323,670.00 USD | 0.00 USD | 219,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1617` | 712,030.00 USD | 712,030.00 USD | 126,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 607,360.00 USD | 607,360.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 578,460.00 USD | 578,460.00 USD | 65,520.00 USD | 22,690.00 USD | 36,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1623` | 585,680.00 USD | 585,680.00 USD | 49,670.00 USD | 156,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1626` | 453,690.00 USD | 453,690.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1626` | 379,150.00 USD | 379,150.00 USD | 0.00 USD | 71,120.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 314,310.00 USD | 314,310.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1629` | 171,270.00 USD | 171,270.00 USD | 147,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 179,170.00 USD | 179,170.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 56,880.00 USD | 56,880.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,460.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1638` | 48,180.00 USD | 48,180.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1638` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 19,070.00 USD | 19,070.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1641` | 29,240.00 USD | 29,240.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1644` | 62,500.00 USD | 62,500.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 107,880.00 USD | 107,880.00 USD | 0.00 USD | 34,100.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1647` | 88,310.00 USD | 88,310.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1647` | 112,680.00 USD | 112,680.00 USD | 0.00 USD | 4,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1650` | 120,940.00 USD | 120,940.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1650` | 119,680.00 USD | 119,680.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1659` | 187,950.00 USD | 187,950.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 157,330.00 USD | 157,330.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1662` | 272,020.00 USD | 272,020.00 USD | 84,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 257,650.00 USD | 257,650.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1665` | 429,100.00 USD | 429,100.00 USD | 87,050.00 USD | 12,670.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 13,460.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1668` | 303,600.00 USD | 303,600.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 567,290.00 USD | 567,290.00 USD | 11,410.00 USD | 39,630.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 332,770.00 USD | 332,770.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1671` | 781,980.00 USD | 781,980.00 USD | 135,250.00 USD | 79,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 402,310.00 USD | 402,310.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1674` | 915,890.00 USD | 915,890.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1677` | 441,770.00 USD | 441,770.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1677` | 1,050,000.00 USD | 1,050,000.00 USD | 59,010.00 USD | 77,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 536,990.00 USD | 536,990.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 1,270,000.00 USD | 1,270,000.00 USD | 101,910.00 USD | 68,430.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 639,440.00 USD | 639,440.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1683` | 1,350,000.00 USD | 1,350,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1686` | 773,500.00 USD | 773,500.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1686` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 897,190.00 USD | 897,190.00 USD | 41,580.00 USD | 32,630.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1689` | 1,480,000.00 USD | 1,480,000.00 USD | 49,670.00 USD | 63,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 1,200,000.00 USD | 1,200,000.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1692` | 1,650,000.00 USD | 1,650,000.00 USD | 33,660.00 USD | 32,070.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,310,000.00 USD | 1,310,000.00 USD | 53,760.00 USD | 26,310.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1695` | 1,730,000.00 USD | 1,730,000.00 USD | 17,360.00 USD | 30,490.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,450,000.00 USD | 1,450,000.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1698` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 1,500,000.00 USD | 1,500,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1701` | 1,970,000.00 USD | 1,970,000.00 USD | 55,170.00 USD | 33,810.00 USD | 72,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,520,000.00 USD | 1,520,000.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1704` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 712.66 USD | 22,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1707` | 1,680,000.00 USD | 1,680,000.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1707` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1710` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 1,720,000.00 USD | 1,720,000.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1713` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1716` | 1,770,000.00 USD | 1,770,000.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,840,000.00 USD | 1,840,000.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1719` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 2,020,000.00 USD | 2,020,000.00 USD | 82,880.00 USD | 28,200.00 USD | 63,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1722` | 2,690,000.00 USD | 2,690,000.00 USD | 142,900.00 USD | 12,590.00 USD | 342,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 2,100,000.00 USD | 2,100,000.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1725` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 37,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 2,130,000.00 USD | 2,130,000.00 USD | 18,490.00 USD | 0.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1731` | 3,190,000.00 USD | 3,190,000.00 USD | 452,310.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 2,150,000.00 USD | 2,150,000.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,210,000.00 USD | 2,210,000.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1737` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1743` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 1,770.00 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1746` | 2,250,000.00 USD | 2,250,000.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 2,370,000.00 USD | 2,370,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1749` | 3,400,000.00 USD | 3,400,000.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 2,430,000.00 USD | 2,430,000.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1752` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 277,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 2,480,000.00 USD | 2,480,000.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1755` | 3,900,000.00 USD | 3,900,000.00 USD | 52,970.00 USD | 0.00 USD | 169,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 2,600,000.00 USD | 2,600,000.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1758` | 4,160,000.00 USD | 4,160,000.00 USD | 209,580.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 2,770,000.00 USD | 2,770,000.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1761` | 4,560,000.00 USD | 4,560,000.00 USD | 284,080.00 USD | 83,160.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 2,890,000.00 USD | 2,890,000.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1764` | 4,900,000.00 USD | 4,900,000.00 USD | 144,160.00 USD | 158,980.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 3,000,000.00 USD | 3,000,000.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1767` | 5,200,000.00 USD | 5,200,000.00 USD | 176,410.00 USD | 117,990.00 USD | 8,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 3,110,000.00 USD | 3,110,000.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1770` | 5,400,000.00 USD | 5,400,000.00 USD | 61,490.00 USD | 91,680.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,160,000.00 USD | 3,160,000.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1773` | 5,590,000.00 USD | 5,590,000.00 USD | 103,820.00 USD | 86,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 25,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1776` | 3,220,000.00 USD | 3,220,000.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 5,790,000.00 USD | 5,790,000.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 3,340,000.00 USD | 3,340,000.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1779` | 6,020,000.00 USD | 6,020,000.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1782` | 6,080,000.00 USD | 6,080,000.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 3,450,000.00 USD | 3,450,000.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1785` | 6,330,000.00 USD | 6,330,000.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 25,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1788` | 3,490,000.00 USD | 3,490,000.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1788` | 6,440,000.00 USD | 6,440,000.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1791` | 6,610,000.00 USD | 6,610,000.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 3,560,000.00 USD | 3,560,000.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1794` | 6,720,000.00 USD | 6,720,000.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 2,560.00 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,620,000.00 USD | 3,620,000.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1797` | 6,760,000.00 USD | 6,760,000.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 3,660,000.00 USD | 3,660,000.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1800` | 6,880,000.00 USD | 6,880,000.00 USD | 12,940.00 USD | 38,070.00 USD | 73,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,710,000.00 USD | 3,710,000.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1803` | 6,960,000.00 USD | 6,960,000.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1806` | 3,730,000.00 USD | 3,730,000.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1806` | 7,050,000.00 USD | 7,050,000.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,760,000.00 USD | 3,760,000.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1809` | 7,190,000.00 USD | 7,190,000.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,820,000.00 USD | 3,820,000.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1812` | 7,300,000.00 USD | 7,300,000.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,840,000.00 USD | 3,840,000.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1815` | 7,420,000.00 USD | 7,420,000.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1818` | 7,530,000.00 USD | 7,530,000.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 13,320.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1821` | 7,670,000.00 USD | 7,670,000.00 USD | 50,880.00 USD | 38,910.00 USD | 41,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,910,000.00 USD | 3,910,000.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1824` | 7,830,000.00 USD | 7,830,000.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,930,000.00 USD | 3,930,000.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1827` | 7,990,000.00 USD | 7,990,000.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1830` | 8,130,000.00 USD | 8,130,000.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,930,000.00 USD | 3,930,000.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1833` | 8,370,000.00 USD | 8,370,000.00 USD | 152,480.00 USD | 49,740.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1836` | 8,480,000.00 USD | 8,480,000.00 USD | 2,610.00 USD | 47,910.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1839` | 8,700,000.00 USD | 8,700,000.00 USD | 81,700.00 USD | 31,130.00 USD | 114,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 3,950,000.00 USD | 3,950,000.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1842` | 8,810,000.00 USD | 8,810,000.00 USD | 43,580.00 USD | 26,100.00 USD | 37,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1845` | 8,940,000.00 USD | 8,940,000.00 USD | 34,630.00 USD | 8,590.00 USD | 81,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 9,070,000.00 USD | 9,070,000.00 USD | 35,280.00 USD | 65,230.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1851` | 9,390,000.00 USD | 9,390,000.00 USD | 67,340.00 USD | 28,290.00 USD | 220,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,490,000.00 USD | 9,490,000.00 USD | 47,090.00 USD | 4,290.00 USD | 53,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1857` | 9,650,000.00 USD | 9,650,000.00 USD | 41,470.00 USD | 21,110.00 USD | 93,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 9,730,000.00 USD | 9,730,000.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1863` | 9,840,000.00 USD | 9,840,000.00 USD | 48,260.00 USD | 13,700.00 USD | 46,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1866` | 9,960,000.00 USD | 9,960,000.00 USD | 54,300.00 USD | 29,050.00 USD | 39,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1869` | 10,150,000.00 USD | 10,150,000.00 USD | 124,660.00 USD | 30,880.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 10,240,000.00 USD | 10,240,000.00 USD | 16,870.00 USD | 33,800.00 USD | 36,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1875` | 10,310,000.00 USD | 10,310,000.00 USD | 27,560.00 USD | 13,320.00 USD | 36,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1876` | 10,330,000.00 USD | 10,330,000.00 USD | 14,220.00 USD | 4,810.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.0355` | 713,850.00 USD | 0.00 USD | 355.00 USD | `-78.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 713,500.00 USD | 0.00 USD | 297.50 USD | `-74.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 713,200.00 USD | 0.00 USD | 353.50 USD | `-69.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 712,850.00 USD | 0.00 USD | 276.53 USD | `-66.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 712,570.00 USD | 0.00 USD | 4,310.00 USD | `-66.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 708,260.00 USD | 0.00 USD | 475.11 USD | `-61.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 707,780.00 USD | 0.00 USD | 131.16 USD | `-59.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 707,650.00 USD | 0.00 USD | 881.45 USD | `-59.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 706,770.00 USD | 0.00 USD | 1,070.00 USD | `-58.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 705,700.00 USD | 0.00 USD | 1,050.00 USD | `-58.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 704,640.00 USD | 0.00 USD | 1,010.00 USD | `-57.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 703,640.00 USD | 0.00 USD | 4,100.00 USD | `-56.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 699,530.00 USD | 0.00 USD | 529.04 USD | `-56.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 699,000.00 USD | 0.00 USD | 2,390.00 USD | `-55.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 696,610.00 USD | 0.00 USD | 757.39 USD | `-53.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 695,860.00 USD | 0.00 USD | 1,490.00 USD | `-52.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 694,370.00 USD | 0.00 USD | 277.37 USD | `-47.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 694,100.00 USD | 0.00 USD | 262.50 USD | `-46.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 693,830.00 USD | 0.00 USD | 795.57 USD | `-45.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 693,040.00 USD | 0.00 USD | 181.00 USD | `-44.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 692,860.00 USD | 0.00 USD | 3,810.00 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 689,040.00 USD | 0.00 USD | 1,550.00 USD | `-37.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 687,500.00 USD | 0.00 USD | 116.07 USD | `-34.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 687,380.00 USD | 0.00 USD | 19,070.00 USD | `-33.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 668,310.00 USD | 0.00 USD | 577.22 USD | `-32.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 667,730.00 USD | 0.00 USD | 343.50 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 667,390.00 USD | 0.00 USD | 26,280.00 USD | `-28.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 641,110.00 USD | 0.00 USD | 105.75 USD | `-28.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 641,000.00 USD | 0.00 USD | 24,280.00 USD | `-26.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 616,720.00 USD | 0.00 USD | 83,620.00 USD | `-25.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 533,090.00 USD | 0.00 USD | 487.10 USD | `-25.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 532,610.00 USD | 0.00 USD | 14,940.00 USD | `-23.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 517,670.00 USD | 0.00 USD | 129,320.00 USD | `-23.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 388,350.00 USD | 0.00 USD | 2,670.00 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 385,680.00 USD | 0.00 USD | 473.27 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 385,210.00 USD | 0.00 USD | 203,210.00 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 182,000.00 USD | 0.00 USD | 2,800.00 USD | `-20.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 179,200.00 USD | 0.00 USD | 1,590.00 USD | `-19.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 177,610.00 USD | 0.00 USD | 6,000.00 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 171,600.00 USD | 0.00 USD | 795.99 USD | `-18.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 170,810.00 USD | 0.00 USD | 502.28 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 170,300.00 USD | 0.00 USD | 162.60 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 170,140.00 USD | 0.00 USD | 700.86 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 169,440.00 USD | 0.00 USD | 13,710.00 USD | `-16.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 155,730.00 USD | 0.00 USD | 108.57 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 155,620.00 USD | 0.00 USD | 3,520.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 152,100.00 USD | 0.00 USD | 127.35 USD | `-13.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 151,970.00 USD | 0.00 USD | 24,850.00 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 127,120.00 USD | 0.00 USD | 1,300.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 125,820.00 USD | 0.00 USD | 25,960.00 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 99,860.00 USD | 0.00 USD | 46,480.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 53,380.00 USD | 0.00 USD | 14,830.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 38,550.00 USD | 0.00 USD | 3,470.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 35,080.00 USD | 0.00 USD | 3,610.00 USD | `-9.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 31,470.00 USD | 0.00 USD | 2,390.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 29,080.00 USD | 0.00 USD | 3,010.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 26,070.00 USD | 0.00 USD | 192.48 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 25,880.00 USD | 0.00 USD | 4,890.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 20,990.00 USD | 0.00 USD | 175.79 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 20,820.00 USD | 0.00 USD | 197.87 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 20,620.00 USD | 0.00 USD | 10,670.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 9,950.00 USD | 0.00 USD | 182.71 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 9,770.00 USD | 0.00 USD | 201.71 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 9,570.00 USD | 0.00 USD | 1,350.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 8,210.00 USD | 0.00 USD | 2,860.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 5,360.00 USD | 0.00 USD | 2,450.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 2,910.00 USD | 0.00 USD | 1,620.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 1,290.00 USD | 0.00 USD | 249.16 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 62,730.00 USD | 62,730.00 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 65,920.00 USD | 3,190.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 104,960.00 USD | 39,040.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 105,550.00 USD | 589.50 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 106,700.00 USD | 1,150.00 USD | 0.00 USD | `+2.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 107,020.00 USD | 317.95 USD | 0.00 USD | `+3.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 107,580.00 USD | 564.90 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 109,380.00 USD | 1,800.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 109,950.00 USD | 571.13 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 118,790.00 USD | 8,840.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 119,010.00 USD | 219.54 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 120,360.00 USD | 1,350.00 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 121,040.00 USD | 683.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 121,380.00 USD | 336.40 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 123,850.00 USD | 2,470.00 USD | 0.00 USD | `+9.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 150,240.00 USD | 26,390.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 161,770.00 USD | 11,540.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 172,020.00 USD | 10,240.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 172,880.00 USD | 864.12 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 175,410.00 USD | 2,520.00 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 175,680.00 USD | 276.75 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 175,810.00 USD | 128.68 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 179,180.00 USD | 3,370.00 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 182,880.00 USD | 3,700.00 USD | 0.00 USD | `+14.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 183,130.00 USD | 245.50 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 183,660.00 USD | 531.47 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 184,360.00 USD | 697.34 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 184,580.00 USD | 222.24 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 213,710.00 USD | 29,130.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 220,780.00 USD | 7,070.00 USD | 0.00 USD | `+18.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 220,970.00 USD | 194.50 USD | 0.00 USD | `+18.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 221,110.00 USD | 137.77 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 221,240.00 USD | 133.19 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 225,000.00 USD | 3,750.00 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 225,490.00 USD | 492.19 USD | 0.00 USD | `+21.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 248,240.00 USD | 22,750.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 248,800.00 USD | 560.96 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 270,140.00 USD | 21,340.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 356,040.00 USD | 85,900.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 357,500.00 USD | 1,470.00 USD | 0.00 USD | `+25.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 357,680.00 USD | 174.20 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 359,750.00 USD | 2,080.00 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 360,000.00 USD | 252.51 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 362,370.00 USD | 2,370.00 USD | 0.00 USD | `+28.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 362,500.00 USD | 126.50 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 362,860.00 USD | 356.72 USD | 0.00 USD | `+29.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 363,220.00 USD | 361.76 USD | 0.00 USD | `+31.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 363,580.00 USD | 365.12 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 369,860.00 USD | 6,280.00 USD | 0.00 USD | `+33.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 370,230.00 USD | 368.47 USD | 0.00 USD | `+34.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 392,720.00 USD | 22,490.00 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 393,050.00 USD | 333.91 USD | 0.00 USD | `+35.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 397,030.00 USD | 3,980.00 USD | 0.00 USD | `+36.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 397,410.00 USD | 378.55 USD | 0.00 USD | `+37.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 397,790.00 USD | 380.23 USD | 0.00 USD | `+38.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 401,620.00 USD | 3,840.00 USD | 0.00 USD | `+39.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 435,440.00 USD | 33,820.00 USD | 0.00 USD | `+40.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 439,700.00 USD | 4,260.00 USD | 0.00 USD | `+42.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 441,220.00 USD | 1,520.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 462,450.00 USD | 21,230.00 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 464,980.00 USD | 2,530.00 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 484,700.00 USD | 19,720.00 USD | 0.00 USD | `+46.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 494,000.00 USD | 9,300.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 495,910.00 USD | 1,910.00 USD | 0.00 USD | `+49.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 514,660.00 USD | 18,750.00 USD | 0.00 USD | `+50.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 515,210.00 USD | 551.23 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 515,610.00 USD | 397.90 USD | 0.00 USD | `+52.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 519,940.00 USD | 4,330.00 USD | 0.00 USD | `+53.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 520,260.00 USD | 320.66 USD | 0.00 USD | `+53.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 536,150.00 USD | 15,880.00 USD | 0.00 USD | `+54.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 538,150.00 USD | 2,000.00 USD | 0.00 USD | `+55.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 540,700.00 USD | 2,550.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 552,430.00 USD | 11,730.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 557,590.00 USD | 5,160.00 USD | 0.00 USD | `+57.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 574,460.00 USD | 16,870.00 USD | 0.00 USD | `+58.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 601,240.00 USD | 26,790.00 USD | 0.00 USD | `+59.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 601,520.00 USD | 272.88 USD | 0.00 USD | `+65.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 601,630.00 USD | 114.99 USD | 0.00 USD | `+68.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 602,030.00 USD | 394.01 USD | 0.00 USD | `+68.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 602,400.00 USD | 375.53 USD | 0.00 USD | `+71.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 604,540.00 USD | 2,130.00 USD | 0.00 USD | `+74.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 605,120.00 USD | 579.27 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 606,870.00 USD | 1,750.00 USD | 0.00 USD | `+77.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 606,970.00 USD | 101.21 USD | 0.00 USD | `+80.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 607,230.00 USD | 262.73 USD | 0.00 USD | `+81.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 608,670.00 USD | 1,440.00 USD | 0.00 USD | `+81.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 614,100.00 USD | 5,430.00 USD | 0.00 USD | `+83.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 619,530.00 USD | 5,430.00 USD | 0.00 USD | `+84.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 619,820.00 USD | 289.61 USD | 0.00 USD | `+86.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 620,300.00 USD | 487.09 USD | 0.00 USD | `+87.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 626,870.00 USD | 6,570.00 USD | 0.00 USD | `+89.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 632,050.00 USD | 5,180.00 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1305` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1308` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD |
| `7D` | `0.1311` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 6,470.00 USD | 4,610.00 USD | 0.00 USD |
| `7D` | `0.1314` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 0.00 USD | 4,010.00 USD | 4,800.00 USD |
| `7D` | `0.1317` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 14,240.00 USD | 4,840.00 USD | 3,260.00 USD |
| `7D` | `0.1320` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 0.00 USD | 2,780.00 USD | 22,910.00 USD |
| `7D` | `0.1323` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 5,580.00 USD | 0.00 USD | 5,190.00 USD |
| `7D` | `0.1326` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 7,890.00 USD | 10,270.00 USD | 11,280.00 USD |
| `7D` | `0.1329` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 11,110.00 USD | 5,000.00 USD | 4,970.00 USD |
| `7D` | `0.1332` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 17,000.00 USD | 1,900.00 USD | 9,950.00 USD |
| `7D` | `0.1335` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 0.00 USD | 4,190.00 USD | 2,300.00 USD |
| `7D` | `0.1338` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 2,830.00 USD | 9,530.00 USD | 32,660.00 USD |
| `7D` | `0.1341` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 6,330.00 USD | 0.00 USD | 6,280.00 USD |
| `7D` | `0.1344` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 6,410.00 USD | 5,790.00 USD | 13,130.00 USD |
| `7D` | `0.1347` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 31,170.00 USD | 5,000.00 USD | 15,770.00 USD |
| `7D` | `0.1350` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 7,650.00 USD | 8,440.00 USD | 23,660.00 USD |
| `7D` | `0.1353` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 7,440.00 USD | 3,540.00 USD | 8,790.00 USD |
| `7D` | `0.1356` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 12,450.00 USD | 8,640.00 USD | 9,380.00 USD |
| `7D` | `0.1359` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 25,240.00 USD | 6,700.00 USD | 8,770.00 USD |
| `7D` | `0.1362` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 3,340.00 USD | 3,690.00 USD | 4,690.00 USD |
| `7D` | `0.1365` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 11,660.00 USD | 1,460.00 USD | 0.00 USD |
| `7D` | `0.1368` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD |
| `7D` | `0.1371` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1374` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1377` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 5,780.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1380` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 8,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1383` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `7D` | `0.1386` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `0.1392` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1395` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1398` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 6,210.00 USD | 4,200.00 USD | 22,820.00 USD |
| `7D` | `0.1401` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD |
| `1D` | `0.1413` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD |
| `7D` | `0.1416` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1419` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1419` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `1D` | `0.1422` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1422` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1425` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD |
| `1D` | `0.1428` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1431` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `0.1434` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1434` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 25,940.00 USD |
| `1D` | `0.1437` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD |
| `7D` | `0.1437` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1440` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD |
| `7D` | `0.1440` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 9,760.00 USD | 2,750.00 USD | 3,610.00 USD |
| `1D` | `0.1443` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD |
| `7D` | `0.1443` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1446` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD |
| `1D` | `0.1452` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1452` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 0.00 USD | 10,680.00 USD | 14,180.00 USD |
| `1D` | `0.1455` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1458` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD |
| `1D` | `0.1461` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD |
| `1D` | `0.1464` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD |
| `7D` | `0.1464` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD |
| `1D` | `0.1467` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD |
| `7D` | `0.1467` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 9,720.00 USD | 5,520.00 USD | 89,310.00 USD |
| `1D` | `0.1470` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD |
| `7D` | `0.1470` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1473` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD |
| `7D` | `0.1473` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 19,430.00 USD | 8,790.00 USD | 14,170.00 USD |
| `1D` | `0.1476` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD |
| `7D` | `0.1476` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 61,700.00 USD | 14,780.00 USD | 81,130.00 USD |
| `1D` | `0.1479` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD |
| `7D` | `0.1479` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 67,510.00 USD | 39,730.00 USD | 43,970.00 USD |
| `1D` | `0.1482` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD |
| `7D` | `0.1482` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 41,960.00 USD | 20,720.00 USD | 59,880.00 USD |
| `1D` | `0.1485` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD |
| `7D` | `0.1485` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 40,660.00 USD | 7,340.00 USD | 163,400.00 USD |
| `1D` | `0.1488` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD |
| `7D` | `0.1488` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 44,530.00 USD | 3,130.00 USD | 10,390.00 USD |
| `1D` | `0.1491` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 40,720.00 USD | 15,530.00 USD | 18,990.00 USD |
| `7D` | `0.1491` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 43,480.00 USD | 22,050.00 USD | 85,470.00 USD |
| `1D` | `0.1494` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD |
| `7D` | `0.1494` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 34,220.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1497` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD |
| `7D` | `0.1497` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 20,880.00 USD | 17,180.00 USD | 188,330.00 USD |
| `1D` | `0.1500` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD |
| `7D` | `0.1500` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 46,820.00 USD | 5,810.00 USD | 21,940.00 USD |
| `1D` | `0.1503` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD |
| `7D` | `0.1503` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 11,490.00 USD | 13,450.00 USD | 9,950.00 USD |
| `1D` | `0.1506` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD |
| `7D` | `0.1506` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 129,280.00 USD | 18,020.00 USD | 217,020.00 USD |
| `1D` | `0.1509` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD |
| `7D` | `0.1509` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 166,980.00 USD | 9,550.00 USD | 82,990.00 USD |
| `1D` | `0.1512` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD |
| `7D` | `0.1512` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 0.00 USD | 8,620.00 USD | 50,470.00 USD |
| `1D` | `0.1515` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD |
| `7D` | `0.1515` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 0.00 USD | 13,330.00 USD | 369,440.00 USD |
| `1D` | `0.1518` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD |
| `7D` | `0.1518` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 96,310.00 USD | 15,160.00 USD | 108,900.00 USD |
| `1D` | `0.1521` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD |
| `7D` | `0.1521` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 0.00 USD | 11,720.00 USD | 144,600.00 USD |
| `1D` | `0.1524` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1524` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 0.00 USD | 18,720.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1527` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 35,230.00 USD | 0.00 USD |
| `1D` | `0.1530` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD |
| `7D` | `0.1530` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 0.00 USD | 9,880.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD |
| `7D` | `0.1533` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 35,470.00 USD | 16,570.00 USD | 0.00 USD |
| `1D` | `0.1536` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1536` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 0.00 USD | 2,910.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1539` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 18,230.00 USD | 0.00 USD |
| `1D` | `0.1542` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1542` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1548` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD |
| `7D` | `0.1548` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 15,410.00 USD | 89,090.00 USD |
| `1D` | `0.1551` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD |
| `7D` | `0.1551` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 21,410.00 USD | 0.00 USD |
| `1D` | `0.1554` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1554` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD |
| `7D` | `0.1557` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 0.00 USD | 4,510.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1560` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 0.00 USD | 16,120.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD |
| `7D` | `0.1563` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD |
| `1D` | `0.1566` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD |
| `7D` | `0.1566` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 70,940.00 USD | 29,160.00 USD | 0.00 USD |
| `1D` | `0.1569` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD |
| `7D` | `0.1569` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 138,980.00 USD | 5,100.00 USD | 151,620.00 USD |
| `1D` | `0.1572` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD |
| `7D` | `0.1572` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 208,130.00 USD | 42,920.00 USD | 58,840.00 USD |
| `1D` | `0.1575` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1575` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 23,310.00 USD | 88,960.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1578` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 107,560.00 USD | 84,670.00 USD | 0.00 USD |
| `1D` | `0.1581` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD |
| `7D` | `0.1581` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 140,060.00 USD | 25,110.00 USD | 0.00 USD |
| `1D` | `0.1584` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD |
| `7D` | `0.1584` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1587` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD |
| `7D` | `0.1587` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 69,180.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 15,370.00 USD | 28,520.00 USD | 51,370.00 USD |
| `7D` | `0.1590` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 24,840.00 USD | 12,590.00 USD | 0.00 USD |
| `1D` | `0.1593` | 988,040.00 USD | 0.00 USD | 988,040.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD |
| `7D` | `0.1593` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1596` | 892,990.00 USD | 0.00 USD | 892,990.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD |
| `7D` | `0.1596` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 0.00 USD | 74,230.00 USD | 0.00 USD |
| `1D` | `0.1599` | 878,020.00 USD | 0.00 USD | 878,020.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1599` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 55,380.00 USD | 75,810.00 USD |
| `1D` | `0.1602` | 864,410.00 USD | 0.00 USD | 864,410.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD |
| `7D` | `0.1602` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 0.00 USD | 46,490.00 USD | 50,120.00 USD |
| `1D` | `0.1605` | 807,140.00 USD | 0.00 USD | 807,140.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1605` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 150,770.00 USD | 16,950.00 USD | 264,260.00 USD |
| `1D` | `0.1608` | 803,290.00 USD | 0.00 USD | 803,290.00 USD | 34,860.00 USD | 7,790.00 USD | 77,820.00 USD |
| `7D` | `0.1608` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 129,610.00 USD | 0.00 USD | 289,270.00 USD |
| `1D` | `0.1611` | 682,820.00 USD | 0.00 USD | 682,820.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD |
| `7D` | `0.1611` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 196,320.00 USD | 0.00 USD | 322,550.00 USD |
| `1D` | `0.1614` | 646,030.00 USD | 0.00 USD | 646,030.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `7D` | `0.1614` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 323,670.00 USD | 0.00 USD | 219,740.00 USD |
| `7D` | `0.1617` | 712,030.00 USD | 0.00 USD | 712,030.00 USD | 126,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1620` | 607,360.00 USD | 0.00 USD | 607,360.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD |
| `1D` | `0.1623` | 578,460.00 USD | 0.00 USD | 578,460.00 USD | 65,520.00 USD | 22,690.00 USD | 36,570.00 USD |
| `7D` | `0.1623` | 585,680.00 USD | 0.00 USD | 585,680.00 USD | 49,670.00 USD | 156,860.00 USD | 0.00 USD |
| `1D` | `0.1626` | 453,690.00 USD | 0.00 USD | 453,690.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD |
| `7D` | `0.1626` | 379,150.00 USD | 0.00 USD | 379,150.00 USD | 0.00 USD | 71,120.00 USD | 136,760.00 USD |
| `1D` | `0.1629` | 314,310.00 USD | 0.00 USD | 314,310.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD |
| `7D` | `0.1629` | 171,270.00 USD | 0.00 USD | 171,270.00 USD | 147,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 179,170.00 USD | 0.00 USD | 179,170.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 56,880.00 USD | 0.00 USD | 56,880.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1638` | 48,180.00 USD | 0.00 USD | 48,180.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1638` | 23,560.00 USD | 0.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `7D` | `0.1639` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1641` | 19,070.00 USD | 0.00 USD | 19,070.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1641` | 29,240.00 USD | 29,240.00 USD | 0.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1643` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1644` | 62,500.00 USD | 62,500.00 USD | 0.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD |
| `7D` | `0.1644` | 107,880.00 USD | 107,880.00 USD | 0.00 USD | 0.00 USD | 34,100.00 USD | 44,540.00 USD |
| `1D` | `0.1647` | 88,310.00 USD | 88,310.00 USD | 0.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD |
| `7D` | `0.1647` | 112,680.00 USD | 112,680.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD | 0.00 USD |
| `1D` | `0.1650` | 120,940.00 USD | 120,940.00 USD | 0.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD |
| `7D` | `0.1650` | 119,680.00 USD | 119,680.00 USD | 0.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `7D` | `0.1659` | 187,950.00 USD | 187,950.00 USD | 0.00 USD | 68,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 157,330.00 USD | 157,330.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD |
| `7D` | `0.1662` | 272,020.00 USD | 272,020.00 USD | 0.00 USD | 84,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1665` | 257,650.00 USD | 257,650.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD |
| `7D` | `0.1665` | 429,100.00 USD | 429,100.00 USD | 0.00 USD | 87,050.00 USD | 12,670.00 USD | 57,360.00 USD |
| `1D` | `0.1668` | 303,600.00 USD | 303,600.00 USD | 0.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD |
| `7D` | `0.1668` | 567,290.00 USD | 567,290.00 USD | 0.00 USD | 11,410.00 USD | 39,630.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 332,770.00 USD | 332,770.00 USD | 0.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1671` | 781,980.00 USD | 781,980.00 USD | 0.00 USD | 135,250.00 USD | 79,440.00 USD | 0.00 USD |
| `1D` | `0.1674` | 402,310.00 USD | 402,310.00 USD | 0.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD |
| `7D` | `0.1674` | 915,890.00 USD | 915,890.00 USD | 0.00 USD | 44,960.00 USD | 88,950.00 USD | 0.00 USD |
| `1D` | `0.1677` | 441,770.00 USD | 441,770.00 USD | 0.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD |
| `7D` | `0.1677` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 59,010.00 USD | 77,400.00 USD | 0.00 USD |
| `1D` | `0.1680` | 536,990.00 USD | 536,990.00 USD | 0.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD |
| `7D` | `0.1680` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 101,910.00 USD | 68,430.00 USD | 51,030.00 USD |
| `1D` | `0.1683` | 639,440.00 USD | 639,440.00 USD | 0.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD |
| `7D` | `0.1683` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 773,500.00 USD | 773,500.00 USD | 0.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD |
| `7D` | `0.1686` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 897,190.00 USD | 897,190.00 USD | 0.00 USD | 41,580.00 USD | 32,630.00 USD | 49,480.00 USD |
| `7D` | `0.1689` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 49,670.00 USD | 63,850.00 USD | 0.00 USD |
| `1D` | `0.1692` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD |
| `7D` | `0.1692` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 33,660.00 USD | 32,070.00 USD | 104,450.00 USD |
| `1D` | `0.1695` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 53,760.00 USD | 26,310.00 USD | 26,570.00 USD |
| `7D` | `0.1695` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 17,360.00 USD | 30,490.00 USD | 39,780.00 USD |
| `1D` | `0.1698` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD |
| `7D` | `0.1698` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 18,830.00 USD |
| `1D` | `0.1701` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `7D` | `0.1701` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 55,170.00 USD | 33,810.00 USD | 72,270.00 USD |
| `1D` | `0.1704` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1704` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 46,880.00 USD | 0.00 USD |
| `1D` | `0.1707` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD |
| `7D` | `0.1707` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 82,340.00 USD |
| `1D` | `0.1710` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD |
| `7D` | `0.1710` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 5,180.00 USD |
| `1D` | `0.1713` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `0.1713` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD |
| `7D` | `0.1716` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD |
| `7D` | `0.1719` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,410.00 USD |
| `1D` | `0.1722` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 82,880.00 USD | 28,200.00 USD | 63,630.00 USD |
| `7D` | `0.1722` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 142,900.00 USD | 12,590.00 USD | 342,490.00 USD |
| `1D` | `0.1725` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD |
| `7D` | `0.1725` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,060.00 USD |
| `1D` | `0.1728` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 18,490.00 USD | 0.00 USD | 14,080.00 USD |
| `7D` | `0.1731` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 452,310.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1734` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD |
| `1D` | `0.1737` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD |
| `7D` | `0.1737` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,430.00 USD |
| `1D` | `0.1740` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD |
| `7D` | `0.1740` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `1D` | `0.1743` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1743` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD |
| `1D` | `0.1749` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1749` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 22,890.00 USD |
| `1D` | `0.1752` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD |
| `7D` | `0.1752` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 277,890.00 USD |
| `1D` | `0.1755` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD |
| `7D` | `0.1755` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 52,970.00 USD | 0.00 USD | 169,880.00 USD |
| `1D` | `0.1758` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD |
| `7D` | `0.1758` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 209,580.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1761` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD |
| `7D` | `0.1761` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 284,080.00 USD | 83,160.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD |
| `7D` | `0.1764` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 144,160.00 USD | 158,980.00 USD | 40,340.00 USD |
| `1D` | `0.1767` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD |
| `7D` | `0.1767` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 176,410.00 USD | 117,990.00 USD | 8,530.00 USD |
| `1D` | `0.1770` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD |
| `7D` | `0.1770` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 61,490.00 USD | 91,680.00 USD | 44,400.00 USD |
| `1D` | `0.1773` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD |
| `7D` | `0.1773` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 103,820.00 USD | 86,080.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD |
| `7D` | `0.1776` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 135,140.00 USD | 59,720.00 USD | 0.00 USD |
| `1D` | `0.1779` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD |
| `7D` | `0.1779` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 52,730.00 USD | 46,410.00 USD | 131,820.00 USD |
| `1D` | `0.1782` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD |
| `7D` | `0.1782` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 20,690.00 USD | 13,990.00 USD | 31,180.00 USD |
| `1D` | `0.1785` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD |
| `7D` | `0.1785` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 153,160.00 USD | 78,850.00 USD | 16,420.00 USD |
| `1D` | `0.1788` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1788` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 73,130.00 USD | 18,250.00 USD | 14,040.00 USD |
| `1D` | `0.1791` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD |
| `7D` | `0.1791` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 155,720.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD |
| `7D` | `0.1794` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 27,100.00 USD | 42,780.00 USD | 36,780.00 USD |
| `1D` | `0.1797` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD |
| `7D` | `0.1797` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 7,670.00 USD |
| `1D` | `0.1800` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD |
| `7D` | `0.1800` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 12,940.00 USD | 38,070.00 USD | 73,510.00 USD |
| `1D` | `0.1803` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD |
| `7D` | `0.1803` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 35,280.00 USD | 25,700.00 USD | 18,250.00 USD |
| `1D` | `0.1806` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD |
| `7D` | `0.1806` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 11,410.00 USD | 56,850.00 USD | 19,880.00 USD |
| `1D` | `0.1809` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD |
| `7D` | `0.1809` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 53,670.00 USD | 30,810.00 USD | 58,890.00 USD |
| `1D` | `0.1812` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD |
| `7D` | `0.1812` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 34,960.00 USD | 16,640.00 USD | 50,510.00 USD |
| `1D` | `0.1815` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `0.1815` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 60,010.00 USD | 30,810.00 USD | 38,270.00 USD |
| `1D` | `0.1818` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD |
| `7D` | `0.1818` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 75,040.00 USD | 24,140.00 USD | 10,390.00 USD |
| `1D` | `0.1821` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 13,320.00 USD | 8,820.00 USD |
| `7D` | `0.1821` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 50,880.00 USD | 38,910.00 USD | 41,820.00 USD |
| `1D` | `0.1824` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD |
| `7D` | `0.1824` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 39,400.00 USD | 17,880.00 USD | 103,440.00 USD |
| `1D` | `0.1827` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD |
| `7D` | `0.1827` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 79,610.00 USD | 18,690.00 USD | 65,670.00 USD |
| `1D` | `0.1830` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `0.1830` | 8,130,000.00 USD | 8,130,000.00 USD | 0.00 USD | 64,890.00 USD | 20,550.00 USD | 52,010.00 USD |
| `1D` | `0.1833` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD |
| `7D` | `0.1833` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 152,480.00 USD | 49,740.00 USD | 44,210.00 USD |
| `7D` | `0.1836` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 2,610.00 USD | 47,910.00 USD | 52,650.00 USD |
| `1D` | `0.1839` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD |
| `7D` | `0.1839` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 81,700.00 USD | 31,130.00 USD | 114,190.00 USD |
| `1D` | `0.1840` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD |
| `7D` | `0.1842` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 43,580.00 USD | 26,100.00 USD | 37,550.00 USD |
| `7D` | `0.1845` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 34,630.00 USD | 8,590.00 USD | 81,890.00 USD |
| `7D` | `0.1848` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 35,280.00 USD | 65,230.00 USD | 32,800.00 USD |
| `7D` | `0.1851` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 67,340.00 USD | 28,290.00 USD | 220,580.00 USD |
| `7D` | `0.1854` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 47,090.00 USD | 4,290.00 USD | 53,990.00 USD |
| `7D` | `0.1857` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 41,470.00 USD | 21,110.00 USD | 93,850.00 USD |
| `7D` | `0.1860` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 49,800.00 USD | 9,640.00 USD | 24,710.00 USD |
| `7D` | `0.1863` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 48,260.00 USD | 13,700.00 USD | 46,280.00 USD |
| `7D` | `0.1866` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 54,300.00 USD | 29,050.00 USD | 39,240.00 USD |
| `7D` | `0.1869` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 124,660.00 USD | 30,880.00 USD | 29,700.00 USD |
| `7D` | `0.1872` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 16,870.00 USD | 33,800.00 USD | 36,780.00 USD |
| `7D` | `0.1875` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 27,560.00 USD | 13,320.00 USD | 36,560.00 USD |
| `7D` | `0.1876` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 14,220.00 USD | 4,810.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `186.32M` | Total OI Tokens: `1,131,590,708.8 ARB`
  * 1h OI Change: `-1.43%` | 4h OI Change: `+5.32%` | 24h OI Change: `-15.08%`
  * Exchange Breakdown: Binance=`42.29M` | Bybit=`26.66M` | OKX=`14.50M` | Hyperliquid=`13.24M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.61K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0031%` | **USDT OKX** | `0.0070%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0068%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0060%` | **USDT Bitget** | `-0.0074%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `35.53%` | `64.47%` | `0.55` | 3,240,000.00 USD |
| `15M` | `Binance` | `41.04%` | `58.96%` | `0.70` | 966,180.00 USD |
| `15M` | `OKX` | `33.27%` | `66.73%` | `0.50` | 617,860.00 USD |
| `15M` | `Bybit` | `29.97%` | `70.03%` | `0.43` | 392,910.00 USD |
| `15M` | `KuCoin` | `42.92%` | `57.08%` | `0.75` | 20,320.00 USD |
| `15M` | `Gate` | `13.83%` | `86.17%` | `0.16` | 177,990.00 USD |
| `15M` | `Bitget` | `48.08%` | `51.92%` | `0.93` | 285,660.00 USD |
| `15M` | `BingX` | `34.56%` | `65.44%` | `0.53` | 232,000.00 USD |
| `15M` | `MEXC` | `15.18%` | `84.82%` | `0.18` | 324,390.00 USD |
| `15M` | `Bitunix` | `59.08%` | `40.92%` | `1.44` | 58,380.00 USD |
| `15M` | `Hyperliquid` | `51.05%` | `48.95%` | `1.04` | 11,680.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.08%` | `50.92%` | `0.96` | 117,020.00 USD |
| `15M` | `Crypto.com` | `37.01%` | `62.99%` | `0.59` | 1,440.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 28,830.00 USD |
| `15M` | `HTX` | `55.41%` | `44.59%` | `1.24` | 1,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `22.22%` | `77.78%` | `0.29` | 49.60 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `92.28%` | `7.72%` | `11.95` | 3,220.00 USD |
| `15M` | `Whale Positions` | `41.04%` | `58.96%` | `0.70` | 966,180.00 USD |
| `15M` | `Global Accounts` | `35.53%` | `64.47%` | `0.55` | 3,240,000.00 USD |
| `1H` | `ARB` | `40.27%` | `59.73%` | `0.67` | 4,760,000.00 USD |
| `1H` | `Binance` | `44.28%` | `55.72%` | `0.79` | 1,790,000.00 USD |
| `1H` | `OKX` | `38.16%` | `61.84%` | `0.62` | 585,510.00 USD |
| `1H` | `Bybit` | `37.49%` | `62.51%` | `0.60` | 625,510.00 USD |
| `1H` | `KuCoin` | `41.92%` | `58.08%` | `0.72` | 261,130.00 USD |
| `1H` | `Gate` | `31.47%` | `68.53%` | `0.46` | 57,260.00 USD |
| `1H` | `Bitget` | `41.75%` | `58.25%` | `0.72` | 103,850.00 USD |
| `1H` | `BingX` | `21.38%` | `78.62%` | `0.27` | 118,580.00 USD |
| `1H` | `MEXC` | `28.88%` | `71.12%` | `0.41` | 142,560.00 USD |
| `1H` | `Bitunix` | `48.11%` | `51.89%` | `0.93` | 95,580.00 USD |
| `1H` | `Hyperliquid` | `73.46%` | `26.54%` | `2.77` | 47,190.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 882,370.00 USD |
| `1H` | `Crypto.com` | `43.1%` | `56.9%` | `0.76` | 14.03 USD |
| `1H` | `WhiteBIT` | `78.85%` | `21.15%` | `3.73` | 38,050.00 USD |
| `1H` | `HTX` | `54.14%` | `45.86%` | `1.18` | 558.49 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `93.31%` | `6.69%` | `13.95` | 255.59 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.94%` | `51.06%` | `0.96` | 9,280.00 USD |
| `1H` | `Whale Positions` | `44.28%` | `55.72%` | `0.79` | 1,790,000.00 USD |
| `1H` | `Global Accounts` | `40.27%` | `59.73%` | `0.67` | 4,760,000.00 USD |
| `4H` | `ARB` | `46.00%` | `54.00%` | `0.85` | 23,240,000.00 USD |
| `4H` | `Binance` | `50.96%` | `49.04%` | `1.04` | 7,980,000.00 USD |
| `4H` | `OKX` | `51.29%` | `48.71%` | `1.05` | 2,280,000.00 USD |
| `4H` | `Bybit` | `52.39%` | `47.61%` | `1.10` | 2,730,000.00 USD |
| `4H` | `KuCoin` | `50.46%` | `49.54%` | `1.02` | 1,010,000.00 USD |
| `4H` | `Gate` | `51.51%` | `48.49%` | `1.06` | 361,680.00 USD |
| `4H` | `Bitget` | `51.19%` | `48.81%` | `1.05` | 388,050.00 USD |
| `4H` | `BingX` | `12.04%` | `87.96%` | `0.14` | 2,860,000.00 USD |
| `4H` | `MEXC` | `47.13%` | `52.87%` | `0.89` | 828,380.00 USD |
| `4H` | `Bitunix` | `54.26%` | `45.74%` | `1.19` | 282,460.00 USD |
| `4H` | `Hyperliquid` | `64.83%` | `35.17%` | `1.84` | 149,980.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.26%` | `51.74%` | `0.93` | 4,110,000.00 USD |
| `4H` | `Crypto.com` | `0.56%` | `99.44%` | `0.01` | 709.29 USD |
| `4H` | `WhiteBIT` | `74.1%` | `25.9%` | `2.86` | 163,720.00 USD |
| `4H` | `HTX` | `53.53%` | `46.47%` | `1.15` | 8,520.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `3.45%` | `96.55%` | `0.04` | 29,520.00 USD |
| `4H` | `Aster` | `91.81%` | `8.19%` | `11.21` | 510.40 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.66%` | `35.34%` | `1.83` | 50,560.00 USD |
| `4H` | `Whale Positions` | `50.96%` | `49.04%` | `1.04` | 7,980,000.00 USD |
| `4H` | `Global Accounts` | `46.00%` | `54.00%` | `0.85` | 23,240,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,684,179.28 USD | 761,022.88 USD | 923,156.41 USD | -162,133.53 USD | `-9.63%` | `12B / 13S` |
| `5:00 UTC` | `0.1637` | `0.1631` | `0.1637` | `0.1639` | `0.1618` | 1,849,966.09 USD | 605,282.83 USD | 1,244,683.26 USD | -639,400.43 USD | `-34.56%` | `9B / 30S` |
| `0:00 UTC` | `0.1655` | `0.1648` | `0.1655` | `0.1660` | `0.1635` | 1,718,232.82 USD | 746,856.42 USD | 971,376.40 USD | -224,519.98 USD | `-13.07%` | `15B / 23S` |
| `5:00 UTC` | `0.1657` | `0.1657` | `0.1657` | `0.1663` | `0.1649` | 1,541,284.70 USD | 631,060.07 USD | 910,224.63 USD | -279,164.57 USD | `-18.11%` | `10B / 51S` |
| `0:00 UTC` | `0.1657` | `0.1656` | `0.1657` | `0.1665` | `0.1649` | 1,537,020.59 USD | 918,105.56 USD | 618,915.03 USD | 299,190.54 USD | `+19.47%` | `31B / 25S` |
| `5:00 UTC` | `0.1640` | `0.1649` | `0.1640` | `0.1663` | `0.1637` | 976,536.74 USD | 358,727.17 USD | 617,809.57 USD | -259,082.40 USD | `-26.53%` | `8B / 45S` |
| `0:00 UTC` | `0.1639` | `0.1639` | `0.1639` | `0.1640` | `0.1638` | 14,827.57 USD | 4,757.30 USD | 10,070.28 USD | -5,312.98 USD | `-35.83%` | `2B / 8S` |

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
| `5m` | -71,020.00 USD | -217,340.00 USD | **`DISTRIBUTION`** |
| `15m` | -33,690.00 USD | -258,090.00 USD | **`DISTRIBUTION`** |
| `30m` | -83,070.00 USD | -424,340.00 USD | **`DISTRIBUTION`** |
| `1h` | -173,080.00 USD | -2,290,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -157,750.00 USD | -2,140,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 57,260.00 USD | -605,510.00 USD | **`DISTRIBUTION`** |
| `6h` | -366,440.00 USD | -1,760,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -198,710.00 USD | -6,260,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,030,000.00 USD | -5,710,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,030,000.00 USD | -10,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,610,000.00 USD | -38,250,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,840,000.00 USD | -164,240,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-71.02K` | 15m=`-33.69K` | 1h=`-173.08K` | 24h=`-2.03M`
* Futures Capital Netflows: 5m=`-217.34K` | 15m=`-258.09K` | 1h=`-2.29M` | 24h=`-10.84M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
