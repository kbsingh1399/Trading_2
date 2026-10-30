# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:43:54 IST` (`2026-10-30 05:13:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1637` | `0.1648` | `0.1635` | `0.1640` | `3,801,811` | 624,294.60 USD | -33,647.26 USD | `-5.39%` | -8,524,881.75 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1639` | `0.1658` | `0.1638` | `0.1656` | `3,855,766` | 635,783.60 USD | -29,979.39 USD | `-4.72%` | -8,554,861.14 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1656` | `0.1660` | `0.1651` | `0.1651` | `1,885,905` | 312,298.42 USD | -129,541.43 USD | `-41.48%` | -8,684,402.57 USD | `-0.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1605` | `0.1625` | `0.1603` | `0.1623` | `10,414,481` | 1,684,179.28 USD | -162,133.53 USD | `-9.63%` | -7,851,834.07 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1623` | `0.1639` | `0.1618` | `0.1637` | `11,341,584` | 1,849,966.09 USD | -639,400.43 USD | `-34.56%` | -8,491,234.50 USD | `-1.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1637` | `0.1660` | `0.1635` | `0.1652` | `9,532,746` | 1,570,603.17 USD | -191,610.94 USD | `-12.20%` | -8,682,845.44 USD | `-0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1580` | `20,448,591` | 3,216,248.24 USD | 252,196.82 USD | `+7.84%` | -7,911,945.27 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1639` | `0.1577` | `0.1637` | `36,120,104` | 5,820,548.12 USD | -303,641.20 USD | `-5.22%` | -8,215,586.47 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1637` | `0.1660` | `0.1635` | `0.1651` | `9,543,521` | 1,572,383.04 USD | -193,161.65 USD | `-12.28%` | -8,408,748.13 USD | `+0.20` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1660` | `0.1577` | `0.1651` | `45,663,586` | 7,392,924.74 USD | -496,809.28 USD | `-6.72%` | -7,708,551.92 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1660` | `0.1577` | `0.1651` | `45,663,586` | 7,392,924.74 USD | -496,809.28 USD | `-6.72%` | -7,708,551.92 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1643` | 1,655.61 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.66K USD at 0.1643 USD [API] | `2026-10-29 02:10:56` |
| `ANNOUNCEMENT` | `INFO` | `0.1644` | 1,656.34 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.66K USD at 0.1644 USD [API] | `2026-10-29 02:10:56` |
| `ANNOUNCEMENT` | `INFO` | `0.1656` | 11.36 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.01K USD at 0.1656 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `0.1656` | 726.35 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.73K USD at 0.1656 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `0.1664` | 114.01 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.11K USD at 0.1664 USD [API] | `2026-10-29 01:58:28` |
| `ANNOUNCEMENT` | `INFO` | `0.1665` | 1,726.62 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.73K USD at 0.1665 USD [API] | `2026-10-29 01:58:28` |
| `ANNOUNCEMENT` | `INFO` | `0.1644` | 1,001.32 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.00K USD at 0.1644 USD [API] | `2026-10-29 02:10:56` |
| `ANNOUNCEMENT` | `INFO` | `0.1647` | 440.63 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.44K USD at 0.1647 USD [API] | `2026-10-29 02:07:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1643` | 8,659.86 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.66K USD at 0.1643 USD [API] | `2026-10-29 02:10:56` |
| `ANNOUNCEMENT` | `INFO` | `0.1661` | 232.02 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.23K USD at 0.1661 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1661` | 4,385.22 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.39K USD at 0.1661 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1662` | 8,757.88 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.76K USD at 0.1662 USD [API] | `2026-10-29 01:59:19` |
| `ANNOUNCEMENT` | `INFO` | `0.1664` | 8,771.05 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 8.77K USD at 0.1664 USD [API] | `2026-10-29 01:58:28` |
| `ANNOUNCEMENT` | `INFO` | `0.1674` | 48.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.05K USD at 0.1674 USD [API] | `2026-10-29 01:49:05` |
| `ANNOUNCEMENT` | `INFO` | `0.1674` | 25.25 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.03K USD at 0.1674 USD [API] | `2026-10-29 01:49:05` |


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
| `7D` | `Long Liquidation` | `0.1304` | 8,480,000.00 USD | 8,480,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 959,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,470,000.00 USD | 8,470,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,660.00 USD | 942,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,450,000.00 USD | 8,450,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,430,000.00 USD | 8,430,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,410,000.00 USD | 8,410,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 17,180.00 USD | 937,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,380,000.00 USD | 8,380,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,350,000.00 USD | 8,350,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,320,000.00 USD | 8,320,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,200.00 USD | 920,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,310,000.00 USD | 8,310,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,280,000.00 USD | 8,280,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 44,860.00 USD | 869,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,240,000.00 USD | 8,240,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,180,000.00 USD | 8,180,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,150,000.00 USD | 8,150,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,120,000.00 USD | 8,120,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 824,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,100,000.00 USD | 8,100,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,060,000.00 USD | 8,060,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,040,000.00 USD | 8,040,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 823,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 8,020,000.00 USD | 8,020,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 8,000,000.00 USD | 8,000,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 812,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 7,960,000.00 USD | 7,960,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 7,940,000.00 USD | 7,940,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 16,480.00 USD | 798,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 7,890,000.00 USD | 7,890,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 4,650,000.00 USD | 4,650,000.00 USD | 15,160.00 USD | 2,340.00 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 4,560,000.00 USD | 4,560,000.00 USD | 3,540.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 782,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1397` | 4,550,000.00 USD | 4,550,000.00 USD | 15,660.00 USD | 953.16 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1397` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 4,530,000.00 USD | 4,530,000.00 USD | 7,330.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 7,790,000.00 USD | 7,790,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1403` | 4,520,000.00 USD | 4,520,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 7,780,000.00 USD | 7,780,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 5,540.00 USD | 776,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1406` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 3,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1409` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 793.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1412` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,690.00 USD | 770,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1418` | 4,510,000.00 USD | 4,510,000.00 USD | 1,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1418` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 4,500,000.00 USD | 4,500,000.00 USD | 8,110.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1424` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 4,030.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,990.00 USD | 754,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1427` | 4,480,000.00 USD | 4,480,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1430` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 4,480,000.00 USD | 4,480,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1433` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 254,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 4,470,000.00 USD | 4,470,000.00 USD | 2,470.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,730,000.00 USD | 7,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 4,450,000.00 USD | 4,450,000.00 USD | 22,050.00 USD | 3,590.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,690,000.00 USD | 7,690,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,660,000.00 USD | 7,660,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1445` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 7,520.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 235,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1448` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1451` | 4,400,000.00 USD | 4,400,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1454` | 4,390,000.00 USD | 4,390,000.00 USD | 15,910.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1454` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 225,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1457` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1460` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 4,350,000.00 USD | 4,350,000.00 USD | 6,950.00 USD | 5,690.00 USD | 6,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,840.00 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 4,340,000.00 USD | 4,340,000.00 USD | 11,020.00 USD | 5,840.00 USD | 13,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,620,000.00 USD | 7,620,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 4,310,000.00 USD | 4,310,000.00 USD | 12,090.00 USD | 4,120.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,510,000.00 USD | 7,510,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 4,280,000.00 USD | 4,280,000.00 USD | 12,160.00 USD | 24,950.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,500,000.00 USD | 7,500,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,180,000.00 USD | 4,180,000.00 USD | 44,650.00 USD | 24,760.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,470,000.00 USD | 7,470,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 87,010.00 USD | 101,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1478` | 4,100,000.00 USD | 4,100,000.00 USD | 136,090.00 USD | 22,450.00 USD | 182,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,440,000.00 USD | 7,440,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 3,760,000.00 USD | 3,760,000.00 USD | 80,730.00 USD | 9,140.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,170,000.00 USD | 7,170,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 3,660,000.00 USD | 3,660,000.00 USD | 68,340.00 USD | 4,610.00 USD | 188,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,070,000.00 USD | 7,070,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,400,000.00 USD | 3,400,000.00 USD | 14,840.00 USD | 0.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 6,870,000.00 USD | 6,870,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 3,380,000.00 USD | 3,380,000.00 USD | 42,470.00 USD | 12,130.00 USD | 8,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 6,780,000.00 USD | 6,780,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,320,000.00 USD | 3,320,000.00 USD | 24,210.00 USD | 6,010.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,660,000.00 USD | 6,660,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,720.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1496` | 3,280,000.00 USD | 3,280,000.00 USD | 53,750.00 USD | 0.00 USD | 28,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,600,000.00 USD | 6,600,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,200,000.00 USD | 3,200,000.00 USD | 14,550.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,360,000.00 USD | 6,360,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1502` | 3,180,000.00 USD | 3,180,000.00 USD | 11,460.00 USD | 15,550.00 USD | 131,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,270,000.00 USD | 6,270,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,020,000.00 USD | 3,020,000.00 USD | 84,100.00 USD | 3,920.00 USD | 31,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,250,000.00 USD | 6,250,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,470.00 USD | 10,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1508` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 1,150.00 USD | 305,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,110,000.00 USD | 6,110,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 6,130.00 USD | 52,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,710,000.00 USD | 5,710,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 2,530,000.00 USD | 2,530,000.00 USD | 16,760.00 USD | 3,900.00 USD | 250,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 9,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,260,000.00 USD | 2,260,000.00 USD | 14,410.00 USD | 6,150.00 USD | 146,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,190,000.00 USD | 5,190,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1520` | 2,090,000.00 USD | 2,090,000.00 USD | 74,090.00 USD | 7,220.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 1,980,000.00 USD | 1,980,000.00 USD | 8,760.00 USD | 4,770.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1526` | 1,960,000.00 USD | 1,960,000.00 USD | 52,690.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 1,900,000.00 USD | 1,900,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1532` | 1,870,000.00 USD | 1,870,000.00 USD | 6,490.00 USD | 11,410.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 1,850,000.00 USD | 1,850,000.00 USD | 10,930.00 USD | 3,970.00 USD | 19,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,710,000.00 USD | 4,710,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,350.00 USD | 8,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1538` | 1,810,000.00 USD | 1,810,000.00 USD | 4,040.00 USD | 16,500.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 1,790,000.00 USD | 1,790,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1544` | 1,750,000.00 USD | 1,750,000.00 USD | 10,090.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1545` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1547` | 1,720,000.00 USD | 1,720,000.00 USD | 24,450.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1550` | 1,690,000.00 USD | 1,690,000.00 USD | 14,460.00 USD | 26,730.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 1,630,000.00 USD | 1,630,000.00 USD | 4,960.00 USD | 5,700.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1556` | 1,610,000.00 USD | 1,610,000.00 USD | 29,960.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 1,570,000.00 USD | 1,570,000.00 USD | 6,990.00 USD | 14,660.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1562` | 1,540,000.00 USD | 1,540,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 1,530,000.00 USD | 1,530,000.00 USD | 80,040.00 USD | 38,290.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,300,000.00 USD | 4,300,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1568` | 1,380,000.00 USD | 1,380,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,200,000.00 USD | 4,200,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,350,000.00 USD | 1,350,000.00 USD | 68,080.00 USD | 7,000.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 3,930,000.00 USD | 3,930,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1574` | 1,120,000.00 USD | 1,120,000.00 USD | 9,200.00 USD | 3,460.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,660,000.00 USD | 3,660,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,520,000.00 USD | 3,520,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1580` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 4,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,380,000.00 USD | 3,380,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,080,000.00 USD | 1,080,000.00 USD | 102,210.00 USD | 10,360.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,120,000.00 USD | 3,120,000.00 USD | 70,150.00 USD | 5,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1586` | 964,250.00 USD | 964,250.00 USD | 9,930.00 USD | 26,220.00 USD | 32,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 3,040,000.00 USD | 3,040,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 895,900.00 USD | 895,900.00 USD | 10,670.00 USD | 21,690.00 USD | 33,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 3,000,000.00 USD | 3,000,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1592` | 830,340.00 USD | 830,340.00 USD | 0.00 USD | 30,010.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 768,360.00 USD | 768,360.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1598` | 758,220.00 USD | 758,220.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 744,610.00 USD | 744,610.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1604` | 742,310.00 USD | 742,310.00 USD | 44,810.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,630,000.00 USD | 2,630,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 683,490.00 USD | 683,490.00 USD | 0.00 USD | 7,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,260,000.00 USD | 2,260,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1610` | 675,700.00 USD | 675,700.00 USD | 48,780.00 USD | 11,340.00 USD | 82,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,780,000.00 USD | 1,780,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 532,830.00 USD | 532,830.00 USD | 0.00 USD | 37,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,420,000.00 USD | 1,420,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1616` | 495,120.00 USD | 495,120.00 USD | 0.00 USD | 12,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 719,920.00 USD | 719,920.00 USD | 187,590.00 USD | 10,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1622` | 482,640.00 USD | 482,640.00 USD | 28,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 521,930.00 USD | 521,930.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 454,400.00 USD | 454,400.00 USD | 70,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 441,570.00 USD | 441,570.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1628` | 383,880.00 USD | 383,880.00 USD | 0.00 USD | 3,520.00 USD | 104,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 215,810.00 USD | 215,810.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1631` | 276,240.00 USD | 276,240.00 USD | 112,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1631` | 139,040.00 USD | 139,040.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1634` | 163,960.00 USD | 163,960.00 USD | 10,020.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,460.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1637` | 145,250.00 USD | 145,250.00 USD | 9,200.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1637` | 68,100.00 USD | 68,100.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1640` | 121,180.00 USD | 121,180.00 USD | 19,160.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1643` | 99,100.00 USD | 99,100.00 USD | 20,200.00 USD | 0.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1643` | 44,540.00 USD | 44,540.00 USD | 0.00 USD | 0.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1646` | 58,200.00 USD | 58,200.00 USD | 14,950.00 USD | 0.00 USD | 17,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1649` | 26,020.00 USD | 26,020.00 USD | 26,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1652` | 62,680.00 USD | 62,680.00 USD | 24,160.00 USD | 11,360.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 91,450.00 USD | 91,450.00 USD | 3,500.00 USD | 8,400.00 USD | 16,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1658` | 163,290.00 USD | 163,290.00 USD | 15,910.00 USD | 55,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1658` | 62,550.00 USD | 62,550.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 241,940.00 USD | 241,940.00 USD | 8,220.00 USD | 12,910.00 USD | 57,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 177,320.00 USD | 177,320.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 428,690.00 USD | 428,690.00 USD | 77,300.00 USD | 18,260.00 USD | 91,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 432,950.00 USD | 432,950.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 13,460.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1667` | 475,870.00 USD | 475,870.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 488,200.00 USD | 488,200.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1670` | 503,640.00 USD | 503,640.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 798,080.00 USD | 798,080.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 593,900.00 USD | 593,900.00 USD | 66,630.00 USD | 3,960.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 842,420.00 USD | 842,420.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1676` | 633,360.00 USD | 633,360.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,070,000.00 USD | 1,070,000.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 660,110.00 USD | 660,110.00 USD | 9,000.00 USD | 10,600.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,220,000.00 USD | 1,220,000.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1682` | 799,840.00 USD | 799,840.00 USD | 114,750.00 USD | 6,240.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,390,000.00 USD | 1,390,000.00 USD | 130,480.00 USD | 28,830.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 897,610.00 USD | 897,610.00 USD | 32,960.00 USD | 37,780.00 USD | 27,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1688` | 953,260.00 USD | 953,260.00 USD | 4,160.00 USD | 2,650.00 USD | 48,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,160,000.00 USD | 1,160,000.00 USD | 75,680.00 USD | 79,000.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,560,000.00 USD | 1,560,000.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1694` | 1,250,000.00 USD | 1,250,000.00 USD | 36,700.00 USD | 23,520.00 USD | 31,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 1,680,000.00 USD | 1,680,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 1,340,000.00 USD | 1,340,000.00 USD | 36,180.00 USD | 40,170.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1700` | 1,430,000.00 USD | 1,430,000.00 USD | 13,350.00 USD | 27,130.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 1,490,000.00 USD | 1,490,000.00 USD | 9,960.00 USD | 16,340.00 USD | 34,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 1,970,000.00 USD | 1,970,000.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 712.66 USD | 22,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1706` | 1,560,000.00 USD | 1,560,000.00 USD | 45,550.00 USD | 9,590.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1706` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 1,650,000.00 USD | 1,650,000.00 USD | 21,630.00 USD | 68,890.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 1,690,000.00 USD | 1,690,000.00 USD | 7,330.00 USD | 19,170.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 1,740,000.00 USD | 1,740,000.00 USD | 13,510.00 USD | 27,880.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 47,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1718` | 1,770,000.00 USD | 1,770,000.00 USD | 12,630.00 USD | 13,260.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 1,900,000.00 USD | 1,900,000.00 USD | 75,410.00 USD | 16,860.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 2,450,000.00 USD | 2,450,000.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 1,970,000.00 USD | 1,970,000.00 USD | 21,930.00 USD | 1,570.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 2,630,000.00 USD | 2,630,000.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1730` | 1,990,000.00 USD | 1,990,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 2,970,000.00 USD | 2,970,000.00 USD | 330,670.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 2,010,000.00 USD | 2,010,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,120,000.00 USD | 3,120,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1736` | 2,040,000.00 USD | 2,040,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 2,070,000.00 USD | 2,070,000.00 USD | 15,900.00 USD | 4,580.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 3,360.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 2,100,000.00 USD | 2,100,000.00 USD | 3,500.00 USD | 2,460.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 1,770.00 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1748` | 2,200,000.00 USD | 2,200,000.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,320,000.00 USD | 3,320,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 2,250,000.00 USD | 2,250,000.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1754` | 2,330,000.00 USD | 2,330,000.00 USD | 34,530.00 USD | 8,430.00 USD | 34,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 3,810,000.00 USD | 3,810,000.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 2,410,000.00 USD | 2,410,000.00 USD | 6,850.00 USD | 14,210.00 USD | 57,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 3,980,000.00 USD | 3,980,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1760` | 2,560,000.00 USD | 2,560,000.00 USD | 58,360.00 USD | 77,180.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,260,000.00 USD | 4,260,000.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 2,690,000.00 USD | 2,690,000.00 USD | 50,470.00 USD | 10,910.00 USD | 68,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 4,660,000.00 USD | 4,660,000.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1766` | 2,790,000.00 USD | 2,790,000.00 USD | 15,830.00 USD | 20,220.00 USD | 63,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,050,000.00 USD | 5,050,000.00 USD | 163,180.00 USD | 190,610.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 2,950,000.00 USD | 2,950,000.00 USD | 40,920.00 USD | 76,440.00 USD | 39,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,290,000.00 USD | 5,290,000.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 3,000,000.00 USD | 3,000,000.00 USD | 16,140.00 USD | 14,970.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,500,000.00 USD | 5,500,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 3,060,000.00 USD | 3,060,000.00 USD | 26,590.00 USD | 20,810.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 5,690,000.00 USD | 5,690,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 25,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1778` | 3,190,000.00 USD | 3,190,000.00 USD | 34,540.00 USD | 77,070.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 5,950,000.00 USD | 5,950,000.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 1,610.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,000,000.00 USD | 6,000,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1784` | 3,280,000.00 USD | 3,280,000.00 USD | 40,030.00 USD | 18,950.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,230,000.00 USD | 6,230,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 25,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1787` | 3,340,000.00 USD | 3,340,000.00 USD | 4,570.00 USD | 45,510.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,400,000.00 USD | 6,400,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1790` | 3,350,000.00 USD | 3,350,000.00 USD | 9,350.00 USD | 0.00 USD | 6,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,520,000.00 USD | 6,520,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 3,380,000.00 USD | 3,380,000.00 USD | 12,930.00 USD | 6,190.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,650,000.00 USD | 6,650,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 2,560.00 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1796` | 3,470,000.00 USD | 3,470,000.00 USD | 26,820.00 USD | 37,260.00 USD | 26,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 6,720,000.00 USD | 6,720,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 3,510,000.00 USD | 3,510,000.00 USD | 10,210.00 USD | 16,910.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1802` | 3,560,000.00 USD | 3,560,000.00 USD | 5,990.00 USD | 29,410.00 USD | 18,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 6,910,000.00 USD | 6,910,000.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 3,580,000.00 USD | 3,580,000.00 USD | 11,250.00 USD | 2,830.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 6,960,000.00 USD | 6,960,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1808` | 3,620,000.00 USD | 3,620,000.00 USD | 8,870.00 USD | 19,850.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,110,000.00 USD | 7,110,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 3,640,000.00 USD | 3,640,000.00 USD | 11,030.00 USD | 4,850.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,220,000.00 USD | 7,220,000.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1814` | 3,700,000.00 USD | 3,700,000.00 USD | 13,160.00 USD | 32,050.00 USD | 14,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,330,000.00 USD | 7,330,000.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1817` | 3,710,000.00 USD | 3,710,000.00 USD | 2,100.00 USD | 5,830.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,430,000.00 USD | 7,430,000.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1820` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 13,140.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,560,000.00 USD | 7,560,000.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 3,740,000.00 USD | 3,740,000.00 USD | 4,680.00 USD | 6,840.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 7,740,000.00 USD | 7,740,000.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1826` | 3,750,000.00 USD | 3,750,000.00 USD | 8,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 7,910,000.00 USD | 7,910,000.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,010,000.00 USD | 8,010,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,180,000.00 USD | 8,180,000.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,390,000.00 USD | 8,390,000.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,700,000.00 USD | 8,700,000.00 USD | 131,250.00 USD | 64,170.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,850,000.00 USD | 8,850,000.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,980,000.00 USD | 8,980,000.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1847` | 9,020,000.00 USD | 9,020,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,280,000.00 USD | 9,280,000.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,490,000.00 USD | 9,490,000.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 9,630,000.00 USD | 9,630,000.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1859` | 9,770,000.00 USD | 9,770,000.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1862` | 9,880,000.00 USD | 9,880,000.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1865` | 9,960,000.00 USD | 9,960,000.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 10,100,000.00 USD | 10,100,000.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1871` | 10,250,000.00 USD | 10,250,000.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1874` | 10,410,000.00 USD | 10,410,000.00 USD | 65,300.00 USD | 43,720.00 USD | 51,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1877` | 10,480,000.00 USD | 10,480,000.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 10,540,000.00 USD | 10,540,000.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1883` | 10,560,000.00 USD | 10,560,000.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1886` | 10,610,000.00 USD | 10,610,000.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1304` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1310` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD |
| `7D` | `0.1313` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD |
| `7D` | `0.1325` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1391` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 15,160.00 USD | 2,340.00 USD | 74,280.00 USD |
| `7D` | `0.1391` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `1D` | `0.1394` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 3,540.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1394` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1397` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 15,660.00 USD | 953.16 USD | 1,480.00 USD |
| `7D` | `0.1397` | 7,810,000.00 USD | 0.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1400` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 7,330.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1400` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1403` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1406` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 3,150.00 USD | 0.00 USD |
| `1D` | `0.1409` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 793.30 USD | 0.00 USD |
| `1D` | `0.1412` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 3,180.00 USD | 0.00 USD |
| `1D` | `0.1418` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 1,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1418` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `0.1421` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 8,110.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1421` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1424` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 0.00 USD | 4,030.00 USD | 2,500.00 USD |
| `1D` | `0.1427` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1430` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `1D` | `0.1433` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1433` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD |
| `1D` | `0.1436` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 2,470.00 USD | 0.00 USD | 20,320.00 USD |
| `7D` | `0.1436` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1439` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 22,050.00 USD | 3,590.00 USD | 4,530.00 USD |
| `7D` | `0.1439` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD |
| `1D` | `0.1442` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD |
| `7D` | `0.1442` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 3,450.00 USD | 5,260.00 USD | 6,160.00 USD |
| `1D` | `0.1445` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 7,520.00 USD | 2,970.00 USD |
| `1D` | `0.1448` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD |
| `1D` | `0.1451` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1451` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD |
| `1D` | `0.1454` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 15,910.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1454` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `0.1457` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1460` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1463` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 6,950.00 USD | 5,690.00 USD | 6,880.00 USD |
| `1D` | `0.1466` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 11,020.00 USD | 5,840.00 USD | 13,350.00 USD |
| `7D` | `0.1466` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1469` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 12,090.00 USD | 4,120.00 USD | 6,650.00 USD |
| `7D` | `0.1469` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1472` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 12,160.00 USD | 24,950.00 USD | 65,860.00 USD |
| `7D` | `0.1472` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1475` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 44,650.00 USD | 24,760.00 USD | 12,280.00 USD |
| `7D` | `0.1475` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD |
| `1D` | `0.1478` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 136,090.00 USD | 22,450.00 USD | 182,820.00 USD |
| `7D` | `0.1478` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1481` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 80,730.00 USD | 9,140.00 USD | 2,770.00 USD |
| `7D` | `0.1481` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD |
| `1D` | `0.1484` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 68,340.00 USD | 4,610.00 USD | 188,330.00 USD |
| `7D` | `0.1484` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD |
| `1D` | `0.1487` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 14,840.00 USD | 0.00 USD | 7,300.00 USD |
| `7D` | `0.1487` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1490` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 42,470.00 USD | 12,130.00 USD | 8,630.00 USD |
| `7D` | `0.1490` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD |
| `1D` | `0.1493` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 24,210.00 USD | 6,010.00 USD | 3,960.00 USD |
| `7D` | `0.1493` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1496` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 53,750.00 USD | 0.00 USD | 28,870.00 USD |
| `7D` | `0.1496` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1499` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 14,550.00 USD | 7,890.00 USD | 2,340.00 USD |
| `7D` | `0.1499` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1502` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 11,460.00 USD | 15,550.00 USD | 131,800.00 USD |
| `7D` | `0.1502` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1505` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 84,100.00 USD | 3,920.00 USD | 31,940.00 USD |
| `7D` | `0.1505` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1508` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 0.00 USD | 1,150.00 USD | 305,480.00 USD |
| `7D` | `0.1508` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1511` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 6,130.00 USD | 52,080.00 USD |
| `7D` | `0.1511` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1514` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 16,760.00 USD | 3,900.00 USD | 250,360.00 USD |
| `7D` | `0.1514` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1517` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 14,410.00 USD | 6,150.00 USD | 146,390.00 USD |
| `7D` | `0.1517` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1520` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 74,090.00 USD | 7,220.00 USD | 33,460.00 USD |
| `7D` | `0.1520` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1523` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 8,760.00 USD | 4,770.00 USD | 8,880.00 USD |
| `7D` | `0.1523` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1526` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 52,690.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1529` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD |
| `7D` | `0.1529` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1532` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 6,490.00 USD | 11,410.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1535` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 10,930.00 USD | 3,970.00 USD | 19,160.00 USD |
| `7D` | `0.1535` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1538` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 4,040.00 USD | 16,500.00 USD | 3,100.00 USD |
| `7D` | `0.1538` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1541` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1544` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 10,090.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1544` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1547` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 24,450.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1547` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1550` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 14,460.00 USD | 26,730.00 USD | 25,090.00 USD |
| `7D` | `0.1550` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1553` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 4,960.00 USD | 5,700.00 USD | 10,240.00 USD |
| `7D` | `0.1553` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1556` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 29,960.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1556` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1559` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 6,990.00 USD | 14,660.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1562` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1562` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1565` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 80,040.00 USD | 38,290.00 USD | 26,360.00 USD |
| `7D` | `0.1565` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1568` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD |
| `7D` | `0.1568` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1571` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 68,080.00 USD | 7,000.00 USD | 154,990.00 USD |
| `7D` | `0.1571` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1574` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 9,200.00 USD | 3,460.00 USD | 14,870.00 USD |
| `7D` | `0.1574` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD |
| `1D` | `0.1577` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1577` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD |
| `1D` | `0.1580` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 4,130.00 USD | 0.00 USD |
| `7D` | `0.1580` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD |
| `1D` | `0.1583` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 102,210.00 USD | 10,360.00 USD | 6,020.00 USD |
| `7D` | `0.1583` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 70,150.00 USD | 5,200.00 USD | 0.00 USD |
| `1D` | `0.1586` | 964,250.00 USD | 0.00 USD | 964,250.00 USD | 9,930.00 USD | 26,220.00 USD | 32,210.00 USD |
| `7D` | `0.1586` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1589` | 895,900.00 USD | 0.00 USD | 895,900.00 USD | 10,670.00 USD | 21,690.00 USD | 33,200.00 USD |
| `7D` | `0.1589` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1592` | 830,340.00 USD | 0.00 USD | 830,340.00 USD | 0.00 USD | 30,010.00 USD | 31,960.00 USD |
| `1D` | `0.1595` | 768,360.00 USD | 0.00 USD | 768,360.00 USD | 0.00 USD | 10,130.00 USD | 0.00 USD |
| `7D` | `0.1595` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1598` | 758,220.00 USD | 0.00 USD | 758,220.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1601` | 744,610.00 USD | 0.00 USD | 744,610.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1604` | 742,310.00 USD | 0.00 USD | 742,310.00 USD | 44,810.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1607` | 683,490.00 USD | 0.00 USD | 683,490.00 USD | 0.00 USD | 7,790.00 USD | 0.00 USD |
| `7D` | `0.1607` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD |
| `1D` | `0.1610` | 675,700.00 USD | 0.00 USD | 675,700.00 USD | 48,780.00 USD | 11,340.00 USD | 82,750.00 USD |
| `7D` | `0.1610` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD |
| `1D` | `0.1613` | 532,830.00 USD | 0.00 USD | 532,830.00 USD | 0.00 USD | 37,710.00 USD | 0.00 USD |
| `7D` | `0.1613` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD |
| `1D` | `0.1616` | 495,120.00 USD | 0.00 USD | 495,120.00 USD | 0.00 USD | 12,480.00 USD | 0.00 USD |
| `7D` | `0.1616` | 719,920.00 USD | 0.00 USD | 719,920.00 USD | 187,590.00 USD | 10,410.00 USD | 0.00 USD |
| `1D` | `0.1622` | 482,640.00 USD | 0.00 USD | 482,640.00 USD | 28,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1622` | 521,930.00 USD | 0.00 USD | 521,930.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD |
| `1D` | `0.1625` | 454,400.00 USD | 0.00 USD | 454,400.00 USD | 70,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1625` | 441,570.00 USD | 0.00 USD | 441,570.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD |
| `1D` | `0.1628` | 383,880.00 USD | 0.00 USD | 383,880.00 USD | 0.00 USD | 3,520.00 USD | 104,120.00 USD |
| `7D` | `0.1628` | 215,810.00 USD | 0.00 USD | 215,810.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1631` | 276,240.00 USD | 0.00 USD | 276,240.00 USD | 112,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1631` | 139,040.00 USD | 0.00 USD | 139,040.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1634` | 163,960.00 USD | 0.00 USD | 163,960.00 USD | 10,020.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1637` | 145,250.00 USD | 0.00 USD | 145,250.00 USD | 9,200.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1637` | 68,100.00 USD | 0.00 USD | 68,100.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `0.1640` | 121,180.00 USD | 0.00 USD | 121,180.00 USD | 19,160.00 USD | 0.00 USD | 2,920.00 USD |
| `1D` | `0.1643` | 99,100.00 USD | 0.00 USD | 99,100.00 USD | 20,200.00 USD | 0.00 USD | 20,690.00 USD |
| `7D` | `0.1643` | 44,540.00 USD | 0.00 USD | 44,540.00 USD | 0.00 USD | 0.00 USD | 44,540.00 USD |
| `1D` | `0.1646` | 58,200.00 USD | 0.00 USD | 58,200.00 USD | 14,950.00 USD | 0.00 USD | 17,230.00 USD |
| `1D` | `0.1649` | 26,020.00 USD | 0.00 USD | 26,020.00 USD | 26,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1650` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1652` | 62,680.00 USD | 62,680.00 USD | 0.00 USD | 24,160.00 USD | 11,360.00 USD | 27,160.00 USD |
| `1D` | `0.1655` | 91,450.00 USD | 91,450.00 USD | 0.00 USD | 3,500.00 USD | 8,400.00 USD | 16,870.00 USD |
| `7D` | `0.1655` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1658` | 163,290.00 USD | 163,290.00 USD | 0.00 USD | 15,910.00 USD | 55,930.00 USD | 0.00 USD |
| `7D` | `0.1658` | 62,550.00 USD | 62,550.00 USD | 0.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD |
| `1D` | `0.1661` | 241,940.00 USD | 241,940.00 USD | 0.00 USD | 8,220.00 USD | 12,910.00 USD | 57,510.00 USD |
| `7D` | `0.1661` | 177,320.00 USD | 177,320.00 USD | 0.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD |
| `1D` | `0.1664` | 428,690.00 USD | 428,690.00 USD | 0.00 USD | 77,300.00 USD | 18,260.00 USD | 91,190.00 USD |
| `7D` | `0.1664` | 432,950.00 USD | 432,950.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1667` | 475,870.00 USD | 475,870.00 USD | 0.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD |
| `7D` | `0.1667` | 488,200.00 USD | 488,200.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1670` | 503,640.00 USD | 503,640.00 USD | 0.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 798,080.00 USD | 798,080.00 USD | 0.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1673` | 593,900.00 USD | 593,900.00 USD | 0.00 USD | 66,630.00 USD | 3,960.00 USD | 19,670.00 USD |
| `7D` | `0.1673` | 842,420.00 USD | 842,420.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD |
| `1D` | `0.1676` | 633,360.00 USD | 633,360.00 USD | 0.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD |
| `7D` | `0.1676` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD |
| `1D` | `0.1679` | 660,110.00 USD | 660,110.00 USD | 0.00 USD | 9,000.00 USD | 10,600.00 USD | 7,150.00 USD |
| `7D` | `0.1679` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD |
| `1D` | `0.1682` | 799,840.00 USD | 799,840.00 USD | 0.00 USD | 114,750.00 USD | 6,240.00 USD | 18,740.00 USD |
| `7D` | `0.1682` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 130,480.00 USD | 28,830.00 USD | 15,310.00 USD |
| `1D` | `0.1685` | 897,610.00 USD | 897,610.00 USD | 0.00 USD | 32,960.00 USD | 37,780.00 USD | 27,030.00 USD |
| `7D` | `0.1685` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1688` | 953,260.00 USD | 953,260.00 USD | 0.00 USD | 4,160.00 USD | 2,650.00 USD | 48,840.00 USD |
| `7D` | `0.1688` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1691` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 75,680.00 USD | 79,000.00 USD | 54,060.00 USD |
| `7D` | `0.1691` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD |
| `1D` | `0.1694` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 36,700.00 USD | 23,520.00 USD | 31,000.00 USD |
| `7D` | `0.1694` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1697` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 36,180.00 USD | 40,170.00 USD | 9,670.00 USD |
| `7D` | `0.1697` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1700` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 13,350.00 USD | 27,130.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1703` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 9,960.00 USD | 16,340.00 USD | 34,530.00 USD |
| `7D` | `0.1703` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1706` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 45,550.00 USD | 9,590.00 USD | 13,990.00 USD |
| `7D` | `0.1706` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1709` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 21,630.00 USD | 68,890.00 USD | 4,190.00 USD |
| `7D` | `0.1709` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1712` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 7,330.00 USD | 19,170.00 USD | 5,330.00 USD |
| `1D` | `0.1715` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 13,510.00 USD | 27,880.00 USD | 9,370.00 USD |
| `7D` | `0.1715` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 47,220.00 USD | 0.00 USD |
| `1D` | `0.1718` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 12,630.00 USD | 13,260.00 USD | 10,190.00 USD |
| `7D` | `0.1718` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1721` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 75,410.00 USD | 16,860.00 USD | 30,720.00 USD |
| `7D` | `0.1721` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD |
| `1D` | `0.1724` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 21,930.00 USD | 1,570.00 USD | 48,370.00 USD |
| `7D` | `0.1724` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD |
| `1D` | `0.1727` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD |
| `1D` | `0.1730` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1730` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 330,670.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1736` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD |
| `1D` | `0.1739` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 15,900.00 USD | 4,580.00 USD | 11,590.00 USD |
| `7D` | `0.1739` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1742` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 11,320.00 USD |
| `1D` | `0.1745` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 8,910.00 USD |
| `7D` | `0.1745` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1748` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 39,610.00 USD |
| `7D` | `0.1748` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1751` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 41,730.00 USD | 0.00 USD | 14,050.00 USD |
| `7D` | `0.1751` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1754` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 34,530.00 USD | 8,430.00 USD | 34,470.00 USD |
| `7D` | `0.1754` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD |
| `1D` | `0.1757` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 6,850.00 USD | 14,210.00 USD | 57,660.00 USD |
| `7D` | `0.1757` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1760` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 58,360.00 USD | 77,180.00 USD | 17,840.00 USD |
| `7D` | `0.1760` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 50,470.00 USD | 10,910.00 USD | 68,500.00 USD |
| `7D` | `0.1763` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD |
| `1D` | `0.1766` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 63,070.00 USD |
| `7D` | `0.1766` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 163,180.00 USD | 190,610.00 USD | 36,540.00 USD |
| `1D` | `0.1769` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 40,920.00 USD | 76,440.00 USD | 39,720.00 USD |
| `7D` | `0.1769` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD |
| `1D` | `0.1772` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 16,140.00 USD | 14,970.00 USD | 21,240.00 USD |
| `7D` | `0.1772` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1775` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 26,590.00 USD | 20,810.00 USD | 5,300.00 USD |
| `7D` | `0.1775` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1778` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 34,540.00 USD | 77,070.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD |
| `1D` | `0.1781` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 1,610.00 USD | 9,410.00 USD |
| `7D` | `0.1781` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1784` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 40,030.00 USD | 18,950.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1787` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 4,570.00 USD | 45,510.00 USD | 10,350.00 USD |
| `7D` | `0.1787` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1790` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 9,350.00 USD | 0.00 USD | 6,270.00 USD |
| `7D` | `0.1790` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1793` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 12,930.00 USD | 6,190.00 USD | 5,670.00 USD |
| `7D` | `0.1793` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1796` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 26,820.00 USD | 37,260.00 USD | 26,290.00 USD |
| `7D` | `0.1796` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1799` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 10,210.00 USD | 16,910.00 USD | 11,410.00 USD |
| `7D` | `0.1799` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1802` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 5,990.00 USD | 29,410.00 USD | 18,750.00 USD |
| `7D` | `0.1802` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD |
| `1D` | `0.1805` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 11,250.00 USD | 2,830.00 USD | 9,240.00 USD |
| `7D` | `0.1805` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1808` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 8,870.00 USD | 19,850.00 USD | 6,190.00 USD |
| `7D` | `0.1808` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1811` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 11,030.00 USD | 4,850.00 USD | 3,770.00 USD |
| `7D` | `0.1811` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD |
| `1D` | `0.1814` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 13,160.00 USD | 32,050.00 USD | 14,590.00 USD |
| `7D` | `0.1814` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD |
| `1D` | `0.1817` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 2,100.00 USD | 5,830.00 USD | 3,340.00 USD |
| `7D` | `0.1817` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1820` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 13,140.00 USD | 3,010.00 USD |
| `7D` | `0.1820` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1823` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 4,680.00 USD | 6,840.00 USD | 5,890.00 USD |
| `7D` | `0.1823` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD |
| `1D` | `0.1826` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 8,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1826` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD |
| `7D` | `0.1829` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD |
| `7D` | `0.1835` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD |
| `7D` | `0.1838` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 131,250.00 USD | 64,170.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 8,850,000.00 USD | 8,850,000.00 USD | 0.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD |
| `7D` | `0.1844` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD |
| `7D` | `0.1847` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD |
| `7D` | `0.1853` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD |
| `7D` | `0.1856` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD |
| `7D` | `0.1859` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD |
| `7D` | `0.1862` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD |
| `7D` | `0.1865` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD |
| `7D` | `0.1868` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD |
| `7D` | `0.1871` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD |
| `7D` | `0.1874` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 65,300.00 USD | 43,720.00 USD | 51,010.00 USD |
| `7D` | `0.1877` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD |
| `7D` | `0.1880` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD |
| `7D` | `0.1883` | 10,560,000.00 USD | 10,560,000.00 USD | 0.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD |
| `7D` | `0.1886` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `189.46M` | Total OI Tokens: `1,150,149,253.5 ARB`
  * 1h OI Change: `+4.03%` | 4h OI Change: `+6.74%` | 24h OI Change: `-14.79%`
  * Exchange Breakdown: Binance=`42.84M` | Bybit=`26.64M` | OKX=`14.60M` | Hyperliquid=`13.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.58K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0030%` | **USDT OKX** | `-0.0013%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0012%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `-0.0106%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `35.97%` | `64.03%` | `0.56` | 5,830,000.00 USD |
| `15M` | `Binance` | `36.48%` | `63.52%` | `0.57` | 2,160,000.00 USD |
| `15M` | `OKX` | `31.24%` | `68.76%` | `0.45` | 1,260,000.00 USD |
| `15M` | `Bybit` | `37.66%` | `62.34%` | `0.60` | 560,870.00 USD |
| `15M` | `KuCoin` | `37.2%` | `62.8%` | `0.59` | 28,980.00 USD |
| `15M` | `Gate` | `45.4%` | `54.6%` | `0.83` | 91,760.00 USD |
| `15M` | `Bitget` | `30.69%` | `69.31%` | `0.44` | 642,690.00 USD |
| `15M` | `BingX` | `63.84%` | `36.16%` | `1.77` | 93,800.00 USD |
| `15M` | `MEXC` | `21.15%` | `78.85%` | `0.27` | 562,620.00 USD |
| `15M` | `Bitunix` | `38.53%` | `61.47%` | `0.63` | 92,210.00 USD |
| `15M` | `Hyperliquid` | `87.34%` | `12.66%` | `6.90` | 120,810.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.79%` | `51.21%` | `0.95` | 95,920.00 USD |
| `15M` | `Crypto.com` | `44.35%` | `55.65%` | `0.80` | 2,120.00 USD |
| `15M` | `WhiteBIT` | `73.07%` | `26.93%` | `2.71` | 117,030.00 USD |
| `15M` | `HTX` | `60.31%` | `39.69%` | `1.52` | 256.04 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `72.89%` | `27.11%` | `2.69` | 1,880.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `48.37%` | `51.63%` | `0.94` | 1,060.00 USD |
| `15M` | `Whale Positions` | `36.48%` | `63.52%` | `0.57` | 2,160,000.00 USD |
| `15M` | `Global Accounts` | `35.97%` | `64.03%` | `0.56` | 5,830,000.00 USD |
| `1H` | `ARB` | `45.76%` | `54.24%` | `0.84` | 5,420,000.00 USD |
| `1H` | `Binance` | `47.7%` | `52.3%` | `0.91` | 1,700,000.00 USD |
| `1H` | `OKX` | `40.57%` | `59.43%` | `0.68` | 551,950.00 USD |
| `1H` | `Bybit` | `49.68%` | `50.32%` | `0.99` | 397,390.00 USD |
| `1H` | `KuCoin` | `51.59%` | `48.41%` | `1.07` | 239,210.00 USD |
| `1H` | `Gate` | `68.54%` | `31.46%` | `2.18` | 23,870.00 USD |
| `1H` | `Bitget` | `43.08%` | `56.92%` | `0.76` | 57,060.00 USD |
| `1H` | `BingX` | `45.76%` | `54.24%` | `0.84` | 1,210,000.00 USD |
| `1H` | `MEXC` | `32.57%` | `67.43%` | `0.48` | 204,280.00 USD |
| `1H` | `Bitunix` | `46.05%` | `53.95%` | `0.85` | 37,760.00 USD |
| `1H` | `Hyperliquid` | `51%` | `49%` | `1.04` | 37,160.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.54%` | `50.46%` | `0.98` | 871,750.00 USD |
| `1H` | `Crypto.com` | `53.35%` | `46.65%` | `1.14` | 0.40 USD |
| `1H` | `WhiteBIT` | `67.36%` | `32.64%` | `2.06` | 56,410.00 USD |
| `1H` | `HTX` | `52.88%` | `47.12%` | `1.12` | 831.82 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `76.56%` | `23.44%` | `3.27` | 94.63 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `74.64%` | `25.36%` | `2.94` | 37,970.00 USD |
| `1H` | `Whale Positions` | `47.7%` | `52.3%` | `0.91` | 1,700,000.00 USD |
| `1H` | `Global Accounts` | `45.76%` | `54.24%` | `0.84` | 5,420,000.00 USD |
| `4H` | `ARB` | `49.93%` | `50.07%` | `1.00` | 49,150,000.00 USD |
| `4H` | `Binance` | `49.89%` | `50.11%` | `1.00` | 20,340,000.00 USD |
| `4H` | `OKX` | `50.09%` | `49.91%` | `1.00` | 8,700,000.00 USD |
| `4H` | `Bybit` | `52.57%` | `47.43%` | `1.11` | 5,100,000.00 USD |
| `4H` | `KuCoin` | `50.16%` | `49.84%` | `1.01` | 398,860.00 USD |
| `4H` | `Gate` | `52.47%` | `47.53%` | `1.10` | 1,480,000.00 USD |
| `4H` | `Bitget` | `49.28%` | `50.72%` | `0.97` | 2,820,000.00 USD |
| `4H` | `BingX` | `44.97%` | `55.03%` | `0.82` | 1,550,000.00 USD |
| `4H` | `MEXC` | `43.5%` | `56.5%` | `0.77` | 2,930,000.00 USD |
| `4H` | `Bitunix` | `47.79%` | `52.21%` | `0.92` | 1,330,000.00 USD |
| `4H` | `Hyperliquid` | `49.86%` | `50.14%` | `0.99` | 2,100,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 1,670,000.00 USD |
| `4H` | `Crypto.com` | `47.54%` | `52.46%` | `0.91` | 27,160.00 USD |
| `4H` | `WhiteBIT` | `75.31%` | `24.69%` | `3.05` | 532,440.00 USD |
| `4H` | `HTX` | `28.36%` | `71.64%` | `0.40` | 28,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.46%` | `57.54%` | `0.74` | 59,380.00 USD |
| `4H` | `Aster` | `72.22%` | `27.78%` | `2.60` | 26,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.27%` | `40.73%` | `1.46` | 65,290.00 USD |
| `4H` | `Whale Positions` | `49.89%` | `50.11%` | `1.00` | 20,340,000.00 USD |
| `4H` | `Global Accounts` | `49.93%` | `50.07%` | `1.00` | 49,150,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1560` | `0.1557` | `0.1560` | `0.1561` | `0.1552` | 724,500.45 USD | 382,680.28 USD | 341,820.18 USD | 40,860.10 USD | `+5.64%` | `10B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1567` | `0.1555` | 659,096.24 USD | 362,345.04 USD | 296,751.20 USD | 65,593.84 USD | `+9.95%` | `17B / 13S` |
| `5:00 UTC` | `0.1568` | `0.1562` | `0.1568` | `0.1570` | `0.1554` | 510,482.89 USD | 331,670.18 USD | 178,812.71 USD | 152,857.47 USD | `+29.94%` | `56B / 25S` |
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,684,179.28 USD | 761,022.88 USD | 923,156.41 USD | -162,133.53 USD | `-9.63%` | `12B / 13S` |
| `5:00 UTC` | `0.1637` | `0.1631` | `0.1637` | `0.1639` | `0.1618` | 1,849,966.09 USD | 605,282.83 USD | 1,244,683.26 USD | -639,400.43 USD | `-34.56%` | `9B / 30S` |
| `0:00 UTC` | `0.1640` | `0.1646` | `0.1640` | `0.1658` | `0.1635` | 1,328,090.37 USD | 609,467.06 USD | 718,623.31 USD | -109,156.25 USD | `-8.22%` | `13B / 18S` |

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
| `5m` | 43,160.00 USD | -399,220.00 USD | **`DISTRIBUTION`** |
| `15m` | 64,590.00 USD | -1,250,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 24,540.00 USD | -1,550,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 132,280.00 USD | -810,160.00 USD | **`DISTRIBUTION`** |
| `2h` | -33,090.00 USD | -218,430.00 USD | **`DISTRIBUTION`** |
| `4h` | 5,250.00 USD | 479,210.00 USD | **`ACCUMULATION`** |
| `6h` | -290,440.00 USD | 78,640.00 USD | **`DISTRIBUTION`** |
| `8h` | 222,040.00 USD | -5,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,060,000.00 USD | -5,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,020,000.00 USD | -9,600,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,450,000.00 USD | -36,520,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,610,000.00 USD | -162,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+43.16K` | 15m=`+64.59K` | 1h=`+132.28K` | 24h=`-2.02M`
* Futures Capital Netflows: 5m=`-399.22K` | 15m=`-1.25M` | 1h=`-810.16K` | 24h=`-9.60M`
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
  * `2026-10-30 09:51:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:39:14 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:40:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
