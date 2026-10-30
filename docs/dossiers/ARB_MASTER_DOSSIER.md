# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:35:25 IST` (`2026-10-30 06:05:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `Live` | `Long` | `0.0385` | 1,790,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.51%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0395` | 1,790,000.00 USD | 0.00 USD | 101.26 USD | `-75.90%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,790,000.00 USD | 0.00 USD | 110.22 USD | `-74.68%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,790,000.00 USD | 0.00 USD | 170.00 USD | `-74.06%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,790,000.00 USD | 0.00 USD | 170,550.00 USD | `-70.40%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,620,000.00 USD | 0.00 USD | 552.90 USD | `-69.79%` | `11,169,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,620,000.00 USD | 0.00 USD | 610.70 USD | `-69.18%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,620,000.00 USD | 0.00 USD | 5,170.00 USD | `-68.57%` | `100,367,200,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,610,000.00 USD | 0.00 USD | 289.43 USD | `-67.96%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,610,000.00 USD | 0.00 USD | 1,070.00 USD | `-67.35%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,610,000.00 USD | 0.00 USD | 2,270.00 USD | `-66.74%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,610,000.00 USD | 0.00 USD | 16,360.00 USD | `-65.52%` | `289,477,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,590,000.00 USD | 0.00 USD | 1,230.00 USD | `-64.30%` | `20,953,500,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,590,000.00 USD | 0.00 USD | 3,870.00 USD | `-63.69%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,590,000.00 USD | 0.00 USD | 6,360.00 USD | `-61.86%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,580,000.00 USD | 0.00 USD | 373.83 USD | `-61.25%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 99,790.00 USD | `-58.81%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-58.20%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,480,000.00 USD | 0.00 USD | 59,500.00 USD | `-57.59%` | `856,116,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,420,000.00 USD | 0.00 USD | 3,510.00 USD | `-56.98%` | `49,751,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,420,000.00 USD | 0.00 USD | 5,840.00 USD | `-56.37%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,410,000.00 USD | 0.00 USD | 111.58 USD | `-55.76%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,410,000.00 USD | 0.00 USD | 2,440.00 USD | `-55.15%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,410,000.00 USD | 0.00 USD | 226.17 USD | `-54.54%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,410,000.00 USD | 0.00 USD | 1,710.00 USD | `-53.93%` | `22,623,800,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,410,000.00 USD | 0.00 USD | 14,690.00 USD | `-53.32%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,390,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.49%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,390,000.00 USD | 0.00 USD | 815.00 USD | `-50.27%` | `10,000,000,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,390,000.00 USD | 0.00 USD | 23,260.00 USD | `-49.66%` | `281,949,900,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,360,000.00 USD | 0.00 USD | 2,580.00 USD | `-47.82%` | `30,172,300,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,360,000.00 USD | 0.00 USD | 19,460.00 USD | `-47.21%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,340,000.00 USD | 0.00 USD | 518.25 USD | `-46.60%` | `5,922,900,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,340,000.00 USD | 0.00 USD | 362.62 USD | `-45.99%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,340,000.00 USD | 0.00 USD | 362.22 USD | `-45.38%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,340,000.00 USD | 0.00 USD | 113.80 USD | `-44.16%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,340,000.00 USD | 0.00 USD | 2,300.00 USD | `-43.55%` | `24,866,500,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,340,000.00 USD | 0.00 USD | 814.24 USD | `-42.94%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,340,000.00 USD | 0.00 USD | 1,510.00 USD | `-42.33%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,340,000.00 USD | 0.00 USD | 1,910.00 USD | `-41.72%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,330,000.00 USD | 0.00 USD | 2,320.00 USD | `-41.11%` | `24,090,300,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 12,280.00 USD | `-39.89%` | `124,716,300,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,320,000.00 USD | 0.00 USD | 16,370.00 USD | `-39.28%` | `164,490,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,300,000.00 USD | 0.00 USD | 2,950.00 USD | `-38.67%` | `29,364,800,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,300,000.00 USD | 0.00 USD | 7,310.00 USD | `-37.45%` | `71,304,800,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 802.14 USD | `-36.84%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,290,000.00 USD | 0.00 USD | 6,230.00 USD | `-36.23%` | `59,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,290,000.00 USD | 0.00 USD | 8,190.00 USD | `-35.62%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,280,000.00 USD | 0.00 USD | 450.48 USD | `-35.01%` | `4,229,900,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,280,000.00 USD | 0.00 USD | 1,060.00 USD | `-34.40%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,280,000.00 USD | 0.00 USD | 125,900.00 USD | `-33.79%` | `1,160,394,900,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,150,000.00 USD | 0.00 USD | 105.42 USD | `-33.18%` | `962,700,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,150,000.00 USD | 0.00 USD | 14,360.00 USD | `-32.57%` | `129,913,800,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,140,000.00 USD | 0.00 USD | 425.50 USD | `-31.96%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,140,000.00 USD | 0.00 USD | 368.45 USD | `-31.35%` | `3,275,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,140,000.00 USD | 0.00 USD | 281.48 USD | `-30.74%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,140,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.13%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,130,000.00 USD | 0.00 USD | 7,820.00 USD | `-29.52%` | `67,704,600,000,000.01` |
| `Live` | `Long` | `0.1165` | 1,120,000.00 USD | 0.00 USD | 1,290.00 USD | `-28.91%` | `11,058,900,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,120,000.00 USD | 0.00 USD | 6,640.00 USD | `-28.30%` | `56,551,000,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,110,000.00 USD | 0.00 USD | 25,800.00 USD | `-27.69%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,090,000.00 USD | 0.00 USD | 1,830.00 USD | `-27.08%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,080,000.00 USD | 0.00 USD | 303.75 USD | `-25.86%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,080,000.00 USD | 0.00 USD | 19,380.00 USD | `-25.25%` | `158,167,100,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,060,000.00 USD | 0.00 USD | 50,430.00 USD | `-24.64%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,010,000.00 USD | 0.00 USD | 1,060.00 USD | `-24.03%` | `8,486,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,010,000.00 USD | 0.00 USD | 134.66 USD | `-23.41%` | `1,073,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,010,000.00 USD | 0.00 USD | 29,370.00 USD | `-22.80%` | `232,151,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 982,560.00 USD | 0.00 USD | 9,780.00 USD | `-21.58%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 972,780.00 USD | 0.00 USD | 3,750.00 USD | `-20.97%` | `28,932,500,000,000.00` |
| `Live` | `Long` | `0.1305` | 969,030.00 USD | 0.00 USD | 16,660.00 USD | `-20.36%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 952,380.00 USD | 0.00 USD | 12,580.00 USD | `-19.75%` | `95,671,200,000,000.00` |
| `Live` | `Long` | `0.1325` | 939,800.00 USD | 0.00 USD | 4,810.00 USD | `-19.14%` | `36,288,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 934,990.00 USD | 0.00 USD | 55,620.00 USD | `-18.53%` | `416,597,000,000,000.00` |
| `Live` | `Long` | `0.1345` | 879,370.00 USD | 0.00 USD | 44,440.00 USD | `-17.92%` | `330,382,400,000,000.00` |
| `Live` | `Long` | `0.1355` | 834,940.00 USD | 0.00 USD | 8,620.00 USD | `-17.31%` | `63,632,100,000,000.00` |
| `Live` | `Long` | `0.1365` | 826,310.00 USD | 0.00 USD | 4,240.00 USD | `-16.70%` | `31,078,200,000,000.00` |
| `Live` | `Long` | `0.1375` | 822,070.00 USD | 0.00 USD | 13,710.00 USD | `-16.09%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 808,360.00 USD | 0.00 USD | 16,480.00 USD | `-15.48%` | `119,008,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 791,880.00 USD | 0.00 USD | 5,960.00 USD | `-14.87%` | `42,721,100,000,000.00` |
| `Live` | `Long` | `0.1405` | 785,920.00 USD | 0.00 USD | 2,640.00 USD | `-14.26%` | `18,781,700,000,000.00` |
| `Live` | `Long` | `0.1415` | 783,280.00 USD | 0.00 USD | 19,390.00 USD | `-13.65%` | `137,014,700,000,000.02` |
| `Live` | `Long` | `0.1425` | 763,890.00 USD | 0.00 USD | 499,000.00 USD | `-13.04%` | `3,501,785,500,000,000.00` |
| `Live` | `Long` | `0.1435` | 264,890.00 USD | 0.00 USD | 18,970.00 USD | `-12.43%` | `132,163,100,000,000.00` |
| `Live` | `Long` | `0.1445` | 245,920.00 USD | 0.00 USD | 9,510.00 USD | `-11.82%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 236,410.00 USD | 0.00 USD | 92,570.00 USD | `-11.21%` | `636,187,800,000,000.00` |
| `Live` | `Long` | `0.1465` | 143,840.00 USD | 0.00 USD | 31,100.00 USD | `-10.60%` | `212,319,500,000,000.00` |
| `Live` | `Long` | `0.1475` | 112,740.00 USD | 0.00 USD | 80,080.00 USD | `-9.99%` | `542,919,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 32,660.00 USD | 0.00 USD | 2,500.00 USD | `-9.38%` | `16,826,900,000,000.00` |
| `Live` | `Long` | `0.1495` | 30,160.00 USD | 0.00 USD | 1,720.00 USD | `-8.77%` | `11,513,300,000,000.00` |
| `Live` | `Long` | `0.1515` | 28,440.00 USD | 0.00 USD | 2,570.00 USD | `-7.55%` | `16,978,000,000,000.00` |
| `Live` | `Long` | `0.1525` | 25,860.00 USD | 0.00 USD | 2,140.00 USD | `-6.94%` | `14,050,400,000,000.00` |
| `Live` | `Long` | `0.1535` | 23,720.00 USD | 0.00 USD | 11,530.00 USD | `-6.33%` | `75,134,600,000,000.00` |
| `Live` | `Long` | `0.1545` | 12,190.00 USD | 0.00 USD | 3,230.00 USD | `-5.72%` | `20,932,600,000,000.00` |
| `Live` | `Long` | `0.1565` | 8,950.00 USD | 0.00 USD | 8,950.00 USD | `-4.50%` | `57,214,100,000,000.00` |
| `Live` | `Short` | `0.1665` | 215.45 USD | 215.45 USD | 0.00 USD | `+1.60%` | `1,294,000,000,000.00` |
| `Live` | `Short` | `0.1675` | 4,860.00 USD | 4,640.00 USD | 0.00 USD | `+2.22%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1715` | 6,340.00 USD | 1,480.00 USD | 0.00 USD | `+4.66%` | `8,642,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 6,480.00 USD | 138.82 USD | 0.00 USD | `+8.93%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1845` | 9,110.00 USD | 2,630.00 USD | 0.00 USD | `+12.59%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1855` | 9,730.00 USD | 616.01 USD | 0.00 USD | `+13.20%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 13,320.00 USD | 3,600.00 USD | 0.00 USD | `+14.42%` | `19,174,300,000,000.00` |
| `Live` | `Short` | `0.1945` | 13,950.00 USD | 623.68 USD | 0.00 USD | `+18.69%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 14,100.00 USD | 150.10 USD | 0.00 USD | `+20.52%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 25,690.00 USD | 11,590.00 USD | 0.00 USD | `+25.40%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2065` | 29,850.00 USD | 4,160.00 USD | 0.00 USD | `+26.01%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2075` | 30,370.00 USD | 514.81 USD | 0.00 USD | `+26.62%` | `2,481,000,000,000.00` |
| `Live` | `Short` | `0.2085` | 30,560.00 USD | 198.08 USD | 0.00 USD | `+27.24%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 30,730.00 USD | 164.23 USD | 0.00 USD | `+27.85%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 30,920.00 USD | 190.73 USD | 0.00 USD | `+28.46%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2135` | 46,610.00 USD | 15,690.00 USD | 0.00 USD | `+30.29%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 87,950.00 USD | 41,330.00 USD | 0.00 USD | `+31.51%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 88,160.00 USD | 213.22 USD | 0.00 USD | `+32.73%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 175,960.00 USD | 87,800.00 USD | 0.00 USD | `+33.95%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2205` | 202,200.00 USD | 26,240.00 USD | 0.00 USD | `+34.56%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 202,310.00 USD | 114.52 USD | 0.00 USD | `+36.39%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 202,650.00 USD | 338.64 USD | 0.00 USD | `+37.00%` | `1,508,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 202,800.00 USD | 154.78 USD | 0.00 USD | `+37.61%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 209,790.00 USD | 6,980.00 USD | 0.00 USD | `+40.05%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 225,720.00 USD | 15,930.00 USD | 0.00 USD | `+43.71%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 225,820.00 USD | 102.62 USD | 0.00 USD | `+44.93%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 226,610.00 USD | 796.25 USD | 0.00 USD | `+47.98%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2435` | 275,310.00 USD | 48,700.00 USD | 0.00 USD | `+48.59%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2455` | 275,550.00 USD | 231.97 USD | 0.00 USD | `+49.81%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 297,590.00 USD | 22,040.00 USD | 0.00 USD | `+50.42%` | `89,431,500,000,000.00` |
| `Live` | `Short` | `0.2545` | 298,140.00 USD | 546.54 USD | 0.00 USD | `+55.31%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 302,000.00 USD | 3,870.00 USD | 0.00 USD | `+56.53%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 330,910.00 USD | 28,910.00 USD | 0.00 USD | `+57.14%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 383,530.00 USD | 52,620.00 USD | 0.00 USD | `+57.75%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 383,690.00 USD | 154.94 USD | 0.00 USD | `+59.58%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2635` | 566,200.00 USD | 182,510.00 USD | 0.00 USD | `+60.80%` | `692,636,800,000,000.00` |
| `Live` | `Short` | `0.2685` | 566,420.00 USD | 226.51 USD | 0.00 USD | `+63.85%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 579,670.00 USD | 13,240.00 USD | 0.00 USD | `+65.68%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 579,880.00 USD | 214.21 USD | 0.00 USD | `+66.29%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 591,480.00 USD | 11,600.00 USD | 0.00 USD | `+67.51%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 591,960.00 USD | 482.84 USD | 0.00 USD | `+70.56%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2835` | 592,120.00 USD | 154.73 USD | 0.00 USD | `+73.00%` | `545,800,000,000.00` |
| `Live` | `Short` | `0.2915` | 890,180.00 USD | 298,060.00 USD | 0.00 USD | `+77.88%` | `1,022,511,200,000,000.00` |
| `Live` | `Short` | `0.2925` | 890,970.00 USD | 794.52 USD | 0.00 USD | `+78.50%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2985` | 891,450.00 USD | 474.76 USD | 0.00 USD | `+82.16%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2995` | 893,340.00 USD | 1,900.00 USD | 0.00 USD | `+82.77%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3025` | 895,640.00 USD | 2,300.00 USD | 0.00 USD | `+84.60%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3075` | 901,940.00 USD | 6,290.00 USD | 0.00 USD | `+87.65%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 902,300.00 USD | 363.72 USD | 0.00 USD | `+88.26%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 914,220.00 USD | 11,930.00 USD | 0.00 USD | `+89.48%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3175` | 914,450.00 USD | 227.49 USD | 0.00 USD | `+93.75%` | `716,500,000,000.00` |
| `Live` | `Short` | `0.3195` | 914,700.00 USD | 247.87 USD | 0.00 USD | `+94.97%` | `775,800,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 713,850.00 USD | 0.00 USD | 355.00 USD | `-78.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 713,500.00 USD | 0.00 USD | 297.50 USD | `-74.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 713,200.00 USD | 0.00 USD | 353.50 USD | `-69.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 712,850.00 USD | 0.00 USD | 276.53 USD | `-66.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 712,570.00 USD | 0.00 USD | 4,310.00 USD | `-66.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 708,260.00 USD | 0.00 USD | 475.11 USD | `-61.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 707,780.00 USD | 0.00 USD | 131.16 USD | `-60.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 707,650.00 USD | 0.00 USD | 881.45 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 706,770.00 USD | 0.00 USD | 1,070.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 705,700.00 USD | 0.00 USD | 1,050.00 USD | `-58.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 704,640.00 USD | 0.00 USD | 1,010.00 USD | `-57.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 703,640.00 USD | 0.00 USD | 4,100.00 USD | `-56.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 699,530.00 USD | 0.00 USD | 529.04 USD | `-56.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 699,000.00 USD | 0.00 USD | 2,390.00 USD | `-55.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 696,610.00 USD | 0.00 USD | 757.39 USD | `-53.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 695,860.00 USD | 0.00 USD | 1,490.00 USD | `-52.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 694,370.00 USD | 0.00 USD | 277.37 USD | `-47.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 694,100.00 USD | 0.00 USD | 262.50 USD | `-46.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 693,830.00 USD | 0.00 USD | 795.57 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 693,040.00 USD | 0.00 USD | 181.00 USD | `-44.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 692,860.00 USD | 0.00 USD | 3,810.00 USD | `-38.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 689,040.00 USD | 0.00 USD | 1,550.00 USD | `-37.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 687,500.00 USD | 0.00 USD | 116.07 USD | `-34.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 687,380.00 USD | 0.00 USD | 19,070.00 USD | `-33.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 668,310.00 USD | 0.00 USD | 577.22 USD | `-32.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 667,730.00 USD | 0.00 USD | 343.50 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 667,390.00 USD | 0.00 USD | 26,280.00 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 641,110.00 USD | 0.00 USD | 105.75 USD | `-28.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 641,000.00 USD | 0.00 USD | 24,280.00 USD | `-26.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 616,720.00 USD | 0.00 USD | 83,620.00 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 533,090.00 USD | 0.00 USD | 487.10 USD | `-25.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 532,610.00 USD | 0.00 USD | 14,940.00 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 517,670.00 USD | 0.00 USD | 129,320.00 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 388,350.00 USD | 0.00 USD | 2,670.00 USD | `-22.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 385,680.00 USD | 0.00 USD | 473.27 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 385,210.00 USD | 0.00 USD | 203,210.00 USD | `-21.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 182,000.00 USD | 0.00 USD | 2,800.00 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 179,200.00 USD | 0.00 USD | 1,590.00 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 177,610.00 USD | 0.00 USD | 6,000.00 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 171,600.00 USD | 0.00 USD | 795.99 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 170,810.00 USD | 0.00 USD | 502.28 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 170,300.00 USD | 0.00 USD | 162.60 USD | `-17.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 170,140.00 USD | 0.00 USD | 700.86 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 169,440.00 USD | 0.00 USD | 13,710.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 155,730.00 USD | 0.00 USD | 108.57 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 155,620.00 USD | 0.00 USD | 3,520.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 152,100.00 USD | 0.00 USD | 127.35 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 151,970.00 USD | 0.00 USD | 24,850.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 127,120.00 USD | 0.00 USD | 1,300.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 125,820.00 USD | 0.00 USD | 25,960.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 99,860.00 USD | 0.00 USD | 46,480.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 53,380.00 USD | 0.00 USD | 14,830.00 USD | `-10.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 38,550.00 USD | 0.00 USD | 3,470.00 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 35,080.00 USD | 0.00 USD | 3,610.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 31,470.00 USD | 0.00 USD | 2,390.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 29,080.00 USD | 0.00 USD | 3,010.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 26,070.00 USD | 0.00 USD | 192.48 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 25,880.00 USD | 0.00 USD | 4,890.00 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 20,990.00 USD | 0.00 USD | 175.79 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 20,820.00 USD | 0.00 USD | 197.87 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 20,620.00 USD | 0.00 USD | 10,670.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 9,950.00 USD | 0.00 USD | 182.71 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 9,770.00 USD | 0.00 USD | 201.71 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 9,570.00 USD | 0.00 USD | 1,350.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 8,210.00 USD | 0.00 USD | 2,860.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 5,360.00 USD | 0.00 USD | 2,450.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 2,910.00 USD | 0.00 USD | 1,620.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 1,290.00 USD | 0.00 USD | 249.16 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 62,730.00 USD | 62,730.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 65,920.00 USD | 3,190.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 104,960.00 USD | 39,040.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 105,550.00 USD | 589.50 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 106,700.00 USD | 1,150.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 107,020.00 USD | 317.95 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 107,580.00 USD | 564.90 USD | 0.00 USD | `+4.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 109,380.00 USD | 1,800.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 109,950.00 USD | 571.13 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 118,790.00 USD | 8,840.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 119,010.00 USD | 219.54 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 120,360.00 USD | 1,350.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 121,040.00 USD | 683.00 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 121,380.00 USD | 336.40 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 123,850.00 USD | 2,470.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 150,240.00 USD | 26,390.00 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 161,770.00 USD | 11,540.00 USD | 0.00 USD | `+10.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 172,020.00 USD | 10,240.00 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 172,880.00 USD | 864.12 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 175,410.00 USD | 2,520.00 USD | 0.00 USD | `+11.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 175,680.00 USD | 276.75 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 175,810.00 USD | 128.68 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 179,180.00 USD | 3,370.00 USD | 0.00 USD | `+13.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 182,880.00 USD | 3,700.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 183,130.00 USD | 245.50 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 183,660.00 USD | 531.47 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 184,360.00 USD | 697.34 USD | 0.00 USD | `+16.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 184,580.00 USD | 222.24 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 213,710.00 USD | 29,130.00 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 220,780.00 USD | 7,070.00 USD | 0.00 USD | `+18.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 220,970.00 USD | 194.50 USD | 0.00 USD | `+18.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 221,110.00 USD | 137.77 USD | 0.00 USD | `+19.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 221,240.00 USD | 133.19 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 225,000.00 USD | 3,750.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 225,490.00 USD | 492.19 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 248,240.00 USD | 22,750.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 248,800.00 USD | 560.96 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 270,140.00 USD | 21,340.00 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 356,040.00 USD | 85,900.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 357,500.00 USD | 1,470.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 357,680.00 USD | 174.20 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 359,750.00 USD | 2,080.00 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 360,000.00 USD | 252.51 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 362,370.00 USD | 2,370.00 USD | 0.00 USD | `+28.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 362,500.00 USD | 126.50 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 362,860.00 USD | 356.72 USD | 0.00 USD | `+29.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 363,220.00 USD | 361.76 USD | 0.00 USD | `+31.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 363,580.00 USD | 365.12 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 369,860.00 USD | 6,280.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 370,230.00 USD | 368.47 USD | 0.00 USD | `+33.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 392,720.00 USD | 22,490.00 USD | 0.00 USD | `+34.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 393,050.00 USD | 333.91 USD | 0.00 USD | `+35.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 397,030.00 USD | 3,980.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 397,410.00 USD | 378.55 USD | 0.00 USD | `+37.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 397,790.00 USD | 380.23 USD | 0.00 USD | `+38.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 401,620.00 USD | 3,840.00 USD | 0.00 USD | `+39.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 435,440.00 USD | 33,820.00 USD | 0.00 USD | `+40.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 439,700.00 USD | 4,260.00 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 441,220.00 USD | 1,520.00 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 462,450.00 USD | 21,230.00 USD | 0.00 USD | `+44.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 464,980.00 USD | 2,530.00 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 484,700.00 USD | 19,720.00 USD | 0.00 USD | `+46.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 494,000.00 USD | 9,300.00 USD | 0.00 USD | `+47.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 495,910.00 USD | 1,910.00 USD | 0.00 USD | `+49.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 514,660.00 USD | 18,750.00 USD | 0.00 USD | `+50.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 515,210.00 USD | 551.23 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 515,610.00 USD | 397.90 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 519,940.00 USD | 4,330.00 USD | 0.00 USD | `+52.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 520,260.00 USD | 320.66 USD | 0.00 USD | `+53.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 536,150.00 USD | 15,880.00 USD | 0.00 USD | `+54.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 538,150.00 USD | 2,000.00 USD | 0.00 USD | `+55.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 540,700.00 USD | 2,550.00 USD | 0.00 USD | `+55.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 552,430.00 USD | 11,730.00 USD | 0.00 USD | `+56.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 557,590.00 USD | 5,160.00 USD | 0.00 USD | `+57.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 574,460.00 USD | 16,870.00 USD | 0.00 USD | `+58.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 601,240.00 USD | 26,790.00 USD | 0.00 USD | `+58.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 601,520.00 USD | 272.88 USD | 0.00 USD | `+65.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 601,630.00 USD | 114.99 USD | 0.00 USD | `+68.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 602,030.00 USD | 394.01 USD | 0.00 USD | `+68.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 602,400.00 USD | 375.53 USD | 0.00 USD | `+71.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 604,540.00 USD | 2,130.00 USD | 0.00 USD | `+74.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 605,120.00 USD | 579.27 USD | 0.00 USD | `+74.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 606,870.00 USD | 1,750.00 USD | 0.00 USD | `+77.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 606,970.00 USD | 101.21 USD | 0.00 USD | `+80.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 607,230.00 USD | 262.73 USD | 0.00 USD | `+80.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 608,670.00 USD | 1,440.00 USD | 0.00 USD | `+81.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 614,100.00 USD | 5,430.00 USD | 0.00 USD | `+83.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 619,530.00 USD | 5,430.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 619,820.00 USD | 289.61 USD | 0.00 USD | `+86.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 620,300.00 USD | 487.09 USD | 0.00 USD | `+87.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 626,870.00 USD | 6,570.00 USD | 0.00 USD | `+88.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 632,050.00 USD | 5,180.00 USD | 0.00 USD | `+91.92%` | `TACTICAL (Retail Cluster)` |

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
| `15M` | `ARB` | `46.74%` | `53.26%` | `0.88` | 1,060,000.00 USD |
| `15M` | `Binance` | `59.15%` | `40.85%` | `1.45` | 390,390.00 USD |
| `15M` | `OKX` | `36.15%` | `63.85%` | `0.57` | 156,190.00 USD |
| `15M` | `Bybit` | `58.16%` | `41.84%` | `1.39` | 103,360.00 USD |
| `15M` | `KuCoin` | `50.42%` | `49.58%` | `1.02` | 54,270.00 USD |
| `15M` | `Gate` | `36.34%` | `63.66%` | `0.57` | 19,240.00 USD |
| `15M` | `Bitget` | `65.92%` | `34.08%` | `1.93` | 15,550.00 USD |
| `15M` | `BingX` | `27.06%` | `72.94%` | `0.37` | 29,310.00 USD |
| `15M` | `MEXC` | `36.2%` | `63.8%` | `0.57` | 16,390.00 USD |
| `15M` | `Bitunix` | `6.34%` | `93.66%` | `0.07` | 74,250.00 USD |
| `15M` | `Hyperliquid` | `78.13%` | `21.87%` | `3.57` | 7,610.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `41.01%` | `58.99%` | `0.70` | 187,700.00 USD |
| `15M` | `Crypto.com` | `7.4%` | `92.6%` | `0.08` | 9.72 USD |
| `15M` | `WhiteBIT` | `15.85%` | `84.15%` | `0.19` | 4,320.00 USD |
| `15M` | `HTX` | `50.3%` | `49.7%` | `1.01` | 298.75 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `64.63%` | `35.37%` | `1.83` | 144.40 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `66.42%` | `33.58%` | `1.98` | 2,410.00 USD |
| `15M` | `Whale Positions` | `59.15%` | `40.85%` | `1.45` | 390,390.00 USD |
| `15M` | `Global Accounts` | `46.74%` | `53.26%` | `0.88` | 1,060,000.00 USD |
| `1H` | `ARB` | `45.96%` | `54.04%` | `0.85` | 4,560,000.00 USD |
| `1H` | `Binance` | `48.64%` | `51.36%` | `0.95` | 1,680,000.00 USD |
| `1H` | `OKX` | `48.93%` | `51.07%` | `0.96` | 591,080.00 USD |
| `1H` | `Bybit` | `46.29%` | `53.71%` | `0.86` | 616,570.00 USD |
| `1H` | `KuCoin` | `49.2%` | `50.8%` | `0.97` | 232,940.00 USD |
| `1H` | `Gate` | `35.48%` | `64.52%` | `0.55` | 64,150.00 USD |
| `1H` | `Bitget` | `46.84%` | `53.16%` | `0.88` | 90,400.00 USD |
| `1H` | `BingX` | `33.91%` | `66.09%` | `0.51` | 118,690.00 USD |
| `1H` | `MEXC` | `45.5%` | `54.5%` | `0.83` | 113,950.00 USD |
| `1H` | `Bitunix` | `32.11%` | `67.89%` | `0.47` | 156,960.00 USD |
| `1H` | `Hyperliquid` | `65.66%` | `34.34%` | `1.91` | 46,150.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.92%` | `50.08%` | `1.00` | 822,620.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 18.12 USD |
| `1H` | `WhiteBIT` | `70.45%` | `29.55%` | `2.38` | 23,360.00 USD |
| `1H` | `HTX` | `30.66%` | `69.34%` | `0.44` | 813.84 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `37.92%` | `62.08%` | `0.61` | 265.73 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `32.97%` | `67.03%` | `0.49` | 9,200.00 USD |
| `1H` | `Whale Positions` | `48.64%` | `51.36%` | `0.95` | 1,680,000.00 USD |
| `1H` | `Global Accounts` | `45.96%` | `54.04%` | `0.85` | 4,560,000.00 USD |
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
| `5m` | 117,220.00 USD | 42,810.00 USD | **`ACCUMULATION`** |
| `15m` | -98,510.00 USD | -703,290.00 USD | **`DISTRIBUTION`** |
| `30m` | 18,890.00 USD | -769,160.00 USD | **`DISTRIBUTION`** |
| `1h` | -207,700.00 USD | -1,810,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -89,220.00 USD | -2,860,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -32,250.00 USD | -1,210,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -402,280.00 USD | -2,430,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -64,090.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,200,000.00 USD | -6,710,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,070,000.00 USD | -11,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,630,000.00 USD | -38,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,890,000.00 USD | -163,920,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+117.22K` | 15m=`-98.51K` | 1h=`-207.70K` | 24h=`-2.07M`
* Futures Capital Netflows: 5m=`+42.81K` | 15m=`-703.29K` | 1h=`-1.81M` | 24h=`-11.49M`
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
