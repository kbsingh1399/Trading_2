# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 11:44:30 IST` (`2026-10-30 06:14:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1639` | `0.1641` | `0.1630` | `0.1639` | `3,283,720` | 537,120.25 USD | 58,101.97 USD | `+10.82%` | -8,561,563.35 USD | `+0.99` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1639` | `0.1654` | `0.1639` | `0.1647` | `1,775,678` | 292,413.29 USD | 5,685.35 USD | `+1.94%` | -8,555,877.99 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1647` | `0.1655` | `0.1647` | `0.1652` | `951,150` | 157,040.08 USD | 45,119.18 USD | `+28.73%` | -8,510,758.81 USD | `+0.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1658` | `0.1665` | `0.1648` | `0.1661` | `9,280,664` | 1,537,020.59 USD | 299,190.54 USD | `+19.47%` | -8,360,582.91 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1661` | `0.1663` | `0.1637` | `0.1639` | `5,922,743` | 976,536.74 USD | -259,082.40 USD | `-26.53%` | -8,619,665.32 USD | `-1.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1639` | `0.1655` | `0.1630` | `0.1652` | `6,010,547` | 986,573.62 USD | 108,906.50 USD | `+11.04%` | -8,510,758.81 USD | `+0.59` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1639` | `0.1577` | `0.1637` | `36,120,104` | 5,820,548.12 USD | -303,641.20 USD | `-5.22%` | -8,146,927.25 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1637` | `0.1665` | `0.1635` | `0.1639` | `34,932,374` | 5,773,074.84 USD | -463,576.41 USD | `-8.03%` | -8,610,503.66 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1639` | `0.1655` | `0.1630` | `0.1652` | `6,004,815` | 985,626.58 USD | 107,959.46 USD | `+10.95%` | -8,502,544.20 USD | `+0.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1652` | `77,063,026` | 12,580,196.59 USD | -658,311.11 USD | `-5.23%` | -7,870,053.75 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1652` | `77,063,026` | 12,580,196.59 USD | -658,311.11 USD | `-5.23%` | -7,870,053.75 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

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
| `ANNOUNCEMENT` | `INFO` | `0.1633` | 22.99 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 0.02K USD at 0.1633 USD [API] | `2026-10-29 07:15:21` |
| `ANNOUNCEMENT` | `INFO` | `0.1633` | 5,642.04 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 5.64K USD at 0.1633 USD [API] | `2026-10-29 08:09:23` |


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
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 101.26 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 170,550.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 552.90 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 610.70 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 5,170.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 1,070.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 16,360.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 1,230.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,870.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 6,360.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 373.83 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 59,500.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,510.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 1,710.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 815.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 23,260.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 2,580.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 518.25 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 362.22 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,300.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 1,910.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 2,320.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 12,280.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 16,370.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,950.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 7,310.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,230.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 450.48 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 125,900.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 105.42 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,360.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 368.45 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 7,820.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 1,290.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 6,640.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,380.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,430.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,060.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 134.66 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 29,370.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 982,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 3,750.00 USD | 972,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 969,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,690,000.00 USD | 8,690,000.00 USD | 6,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,690,000.00 USD | 8,690,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 12,580.00 USD | 952,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,680,000.00 USD | 8,680,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,660,000.00 USD | 8,660,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,640,000.00 USD | 8,640,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,810.00 USD | 939,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,610,000.00 USD | 8,610,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,570,000.00 USD | 8,570,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,550,000.00 USD | 8,550,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 55,620.00 USD | 934,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,530,000.00 USD | 8,530,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,510,000.00 USD | 8,510,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 44,440.00 USD | 879,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,460,000.00 USD | 8,460,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,400,000.00 USD | 8,400,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,380,000.00 USD | 8,380,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,350,000.00 USD | 8,350,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 8,620.00 USD | 834,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,320,000.00 USD | 8,320,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,280,000.00 USD | 8,280,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,270,000.00 USD | 8,270,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 4,240.00 USD | 826,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 8,240,000.00 USD | 8,240,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 8,230,000.00 USD | 8,230,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 822,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 8,190,000.00 USD | 8,190,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 8,170,000.00 USD | 8,170,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 16,480.00 USD | 808,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 8,120,000.00 USD | 8,120,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 791,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 8,020,000.00 USD | 8,020,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 8,000,000.00 USD | 8,000,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,640.00 USD | 785,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 19,390.00 USD | 783,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1419` | 4,890,000.00 USD | 4,890,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1422` | 4,890,000.00 USD | 4,890,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1425` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,000.00 USD | 763,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1428` | 4,870,000.00 USD | 4,870,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1430` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1433` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1434` | 4,860,000.00 USD | 4,860,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 264,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,950,000.00 USD | 7,950,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1437` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,920,000.00 USD | 7,920,000.00 USD | 23,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1440` | 4,830,000.00 USD | 4,830,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 2,750.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1443` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 245,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1446` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1452` | 4,790,000.00 USD | 4,790,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1454` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,760,000.00 USD | 4,760,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,570.00 USD | 236,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1458` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1464` | 4,740,000.00 USD | 4,740,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,100.00 USD | 143,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,860,000.00 USD | 7,860,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,700,000.00 USD | 4,700,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,750,000.00 USD | 7,750,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 4,680,000.00 USD | 4,680,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,740,000.00 USD | 7,740,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,660,000.00 USD | 4,660,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,710,000.00 USD | 7,710,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 80,080.00 USD | 112,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 4,510,000.00 USD | 4,510,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,670,000.00 USD | 7,670,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,260,000.00 USD | 4,260,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,400,000.00 USD | 7,400,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 4,100,000.00 USD | 4,100,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,310,000.00 USD | 7,310,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,920,000.00 USD | 3,920,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,500.00 USD | 32,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1487` | 7,110,000.00 USD | 7,110,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1488` | 3,780,000.00 USD | 3,780,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 7,020,000.00 USD | 7,020,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,750,000.00 USD | 3,750,000.00 USD | 40,720.00 USD | 15,530.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,880,000.00 USD | 6,880,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 3,680,000.00 USD | 3,680,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,720.00 USD | 30,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,820,000.00 USD | 6,820,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,600,000.00 USD | 3,600,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,580,000.00 USD | 6,580,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,540,000.00 USD | 3,540,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,490,000.00 USD | 6,490,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,520,000.00 USD | 3,520,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,480,000.00 USD | 6,480,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1506` | 3,290,000.00 USD | 3,290,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,330,000.00 USD | 6,330,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,930,000.00 USD | 5,930,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 2,890,000.00 USD | 2,890,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,870,000.00 USD | 2,870,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 2,570.00 USD | 28,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,410,000.00 USD | 5,410,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 2,490,000.00 USD | 2,490,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,400,000.00 USD | 2,400,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,320,000.00 USD | 2,320,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1525` | 2,140.00 USD | 25,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1526` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,280,000.00 USD | 2,280,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 2,250,000.00 USD | 2,250,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,940,000.00 USD | 4,940,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 11,530.00 USD | 23,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 2,190,000.00 USD | 2,190,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 2,140,000.00 USD | 2,140,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,100,000.00 USD | 2,100,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 3,230.00 USD | 12,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 2,060,000.00 USD | 2,060,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,020,000.00 USD | 2,020,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 1,970,000.00 USD | 1,970,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,940,000.00 USD | 1,940,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 1,910,000.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,890,000.00 USD | 1,890,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,520,000.00 USD | 4,520,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 8,950.00 USD | 8,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1566` | 1,840,000.00 USD | 1,840,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,430,000.00 USD | 4,430,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,710,000.00 USD | 1,710,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 4,150,000.00 USD | 4,150,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 1,580,000.00 USD | 1,580,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,880,000.00 USD | 3,880,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,450,000.00 USD | 1,450,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,740,000.00 USD | 3,740,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,600,000.00 USD | 3,600,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,440,000.00 USD | 1,440,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,340,000.00 USD | 3,340,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 1,420,000.00 USD | 1,420,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 3,270,000.00 USD | 3,270,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,310,000.00 USD | 1,310,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 3,230,000.00 USD | 3,230,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 1,200,000.00 USD | 1,200,000.00 USD | 15,370.00 USD | 28,520.00 USD | 51,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1592` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1596` | 1,010,000.00 USD | 1,010,000.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 998,970.00 USD | 998,970.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 985,360.00 USD | 985,360.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,800,000.00 USD | 2,800,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 928,080.00 USD | 928,080.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,430,000.00 USD | 2,430,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 924,240.00 USD | 924,240.00 USD | 34,860.00 USD | 7,790.00 USD | 77,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,950,000.00 USD | 1,950,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 803,760.00 USD | 803,760.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,600,000.00 USD | 1,600,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 766,980.00 USD | 766,980.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 892,950.00 USD | 892,950.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 728,310.00 USD | 728,310.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 705,360.00 USD | 705,360.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 699,410.00 USD | 699,410.00 USD | 65,520.00 USD | 22,690.00 USD | 36,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 550,140.00 USD | 550,140.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1626` | 574,630.00 USD | 574,630.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 290,950.00 USD | 290,950.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 435,260.00 USD | 435,260.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1631` | 214,170.00 USD | 214,170.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 300,120.00 USD | 300,120.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 177,820.00 USD | 177,820.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1637` | 143,230.00 USD | 143,230.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1638` | 169,130.00 USD | 169,130.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1640` | 119,680.00 USD | 119,680.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 140,010.00 USD | 140,010.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1643` | 90,430.00 USD | 90,430.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 120,940.00 USD | 120,940.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1646` | 20,780.00 USD | 20,780.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1647` | 58,440.00 USD | 58,440.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1649` | 7,000.00 USD | 7,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1650` | 32,630.00 USD | 32,630.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 103,750.00 USD | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 36,390.00 USD | 36,390.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 265,580.00 USD | 265,580.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 136,710.00 USD | 136,710.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 215.45 USD | 215.45 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1667` | 320,830.00 USD | 320,830.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1668` | 182,660.00 USD | 182,660.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 630,710.00 USD | 630,710.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 211,830.00 USD | 211,830.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 675,050.00 USD | 675,050.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 281,360.00 USD | 281,360.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 900,830.00 USD | 900,830.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 320,820.00 USD | 320,820.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,050,000.00 USD | 1,050,000.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 416,040.00 USD | 416,040.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,210,000.00 USD | 1,210,000.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 518,490.00 USD | 518,490.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1686` | 652,550.00 USD | 652,550.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,320,000.00 USD | 1,320,000.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 776,250.00 USD | 776,250.00 USD | 41,580.00 USD | 32,630.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,500,000.00 USD | 1,500,000.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 1,080,000.00 USD | 1,080,000.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 1,620,000.00 USD | 1,620,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,190,000.00 USD | 1,190,000.00 USD | 53,760.00 USD | 26,310.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,330,000.00 USD | 1,330,000.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 1,370,000.00 USD | 1,370,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 1,900,000.00 USD | 1,900,000.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,400,000.00 USD | 1,400,000.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1706` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 1,550,000.00 USD | 1,550,000.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 1,600,000.00 USD | 1,600,000.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 6,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1716` | 1,650,000.00 USD | 1,650,000.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,720,000.00 USD | 1,720,000.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 2,420,000.00 USD | 2,420,000.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 1,900,000.00 USD | 1,900,000.00 USD | 82,880.00 USD | 28,200.00 USD | 63,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 2,610,000.00 USD | 2,610,000.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 1,980,000.00 USD | 1,980,000.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 2,010,000.00 USD | 2,010,000.00 USD | 18,490.00 USD | 0.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 2,930,000.00 USD | 2,930,000.00 USD | 306,550.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,070,000.00 USD | 3,070,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 2,030,000.00 USD | 2,030,000.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,080,000.00 USD | 2,080,000.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1746` | 2,130,000.00 USD | 2,130,000.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,270,000.00 USD | 3,270,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 2,250,000.00 USD | 2,250,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 2,310,000.00 USD | 2,310,000.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 3,770,000.00 USD | 3,770,000.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 2,360,000.00 USD | 2,360,000.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 3,940,000.00 USD | 3,940,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 2,480,000.00 USD | 2,480,000.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,220,000.00 USD | 4,220,000.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 2,650,000.00 USD | 2,650,000.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 4,610,000.00 USD | 4,610,000.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 2,770,000.00 USD | 2,770,000.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 4,980,000.00 USD | 4,980,000.00 USD | 163,180.00 USD | 165,520.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 2,880,000.00 USD | 2,880,000.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,210,000.00 USD | 5,210,000.00 USD | 113,280.00 USD | 95,050.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 2,990,000.00 USD | 2,990,000.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,420,000.00 USD | 5,420,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,040,000.00 USD | 3,040,000.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 5,610,000.00 USD | 5,610,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1776` | 3,100,000.00 USD | 3,100,000.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 5,870,000.00 USD | 5,870,000.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 3,210,000.00 USD | 3,210,000.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 5,920,000.00 USD | 5,920,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,150,000.00 USD | 6,150,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 3,330,000.00 USD | 3,330,000.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 6,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,320,000.00 USD | 6,320,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 3,370,000.00 USD | 3,370,000.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,440,000.00 USD | 6,440,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,570,000.00 USD | 6,570,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 3,440,000.00 USD | 3,440,000.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 6,640,000.00 USD | 6,640,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,500,000.00 USD | 3,500,000.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 3,540,000.00 USD | 3,540,000.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 6,830,000.00 USD | 6,830,000.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,590,000.00 USD | 3,590,000.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 6,880,000.00 USD | 6,880,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1806` | 3,610,000.00 USD | 3,610,000.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,030,000.00 USD | 7,030,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,640,000.00 USD | 3,640,000.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,140,000.00 USD | 7,140,000.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,700,000.00 USD | 3,700,000.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,250,000.00 USD | 7,250,000.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,720,000.00 USD | 3,720,000.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,350,000.00 USD | 7,350,000.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,490,000.00 USD | 7,490,000.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 13,320.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 7,680,000.00 USD | 7,680,000.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,790,000.00 USD | 3,790,000.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 7,840,000.00 USD | 7,840,000.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,810,000.00 USD | 3,810,000.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 7,940,000.00 USD | 7,940,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,120,000.00 USD | 8,120,000.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,810,000.00 USD | 3,810,000.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,290,000.00 USD | 8,290,000.00 USD | 111,430.00 USD | 46,260.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,510,000.00 USD | 8,510,000.00 USD | 69,120.00 USD | 39,080.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1839` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1840` | 3,830,000.00 USD | 3,830,000.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,660,000.00 USD | 8,660,000.00 USD | 56,160.00 USD | 47,560.00 USD | 45,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,770,000.00 USD | 8,770,000.00 USD | 34,630.00 USD | 3,900.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,630.00 USD | 9,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1847` | 8,810,000.00 USD | 8,810,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,060,000.00 USD | 9,060,000.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,270,000.00 USD | 9,270,000.00 USD | 62,090.00 USD | 9,590.00 USD | 138,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 9,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 3,600.00 USD | 13,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 13,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 14,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 25,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 4,160.00 USD | 29,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 514.81 USD | 30,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 30,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2105` | 190.73 USD | 30,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 46,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 87,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 88,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 175,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2205` | 26,240.00 USD | 202,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 202,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 338.64 USD | 202,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 202,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 209,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 225,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 225,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 226,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2435` | 48,700.00 USD | 275,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 275,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2465` | 22,040.00 USD | 297,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 298,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 302,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 330,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 383,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 383,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2635` | 182,510.00 USD | 566,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 566,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 579,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 579,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 591,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 591,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 154.73 USD | 592,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 298,060.00 USD | 890,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 890,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 474.76 USD | 891,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 1,900.00 USD | 893,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3025` | 2,300.00 USD | 895,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 901,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 902,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 914,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 914,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3195` | 247.87 USD | 914,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 1,790,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.70%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0395` | 1,790,000.00 USD | 0.00 USD | 101.26 USD | `-76.10%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,790,000.00 USD | 0.00 USD | 110.22 USD | `-74.89%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,790,000.00 USD | 0.00 USD | 170.00 USD | `-74.28%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,790,000.00 USD | 0.00 USD | 170,550.00 USD | `-70.65%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,620,000.00 USD | 0.00 USD | 552.90 USD | `-70.05%` | `11,169,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,620,000.00 USD | 0.00 USD | 610.70 USD | `-69.44%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,620,000.00 USD | 0.00 USD | 5,170.00 USD | `-68.84%` | `100,367,200,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,610,000.00 USD | 0.00 USD | 289.43 USD | `-68.23%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,610,000.00 USD | 0.00 USD | 1,070.00 USD | `-67.62%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,610,000.00 USD | 0.00 USD | 2,270.00 USD | `-67.02%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,610,000.00 USD | 0.00 USD | 16,360.00 USD | `-65.81%` | `289,477,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,590,000.00 USD | 0.00 USD | 1,230.00 USD | `-64.60%` | `20,953,500,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,590,000.00 USD | 0.00 USD | 3,870.00 USD | `-63.99%` | `65,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,590,000.00 USD | 0.00 USD | 6,360.00 USD | `-62.18%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,580,000.00 USD | 0.00 USD | 373.83 USD | `-61.57%` | `5,887,100,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 99,790.00 USD | `-59.15%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-58.55%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,480,000.00 USD | 0.00 USD | 59,500.00 USD | `-57.94%` | `856,116,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,420,000.00 USD | 0.00 USD | 3,510.00 USD | `-57.34%` | `49,751,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,420,000.00 USD | 0.00 USD | 5,840.00 USD | `-56.73%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,410,000.00 USD | 0.00 USD | 111.58 USD | `-56.13%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,410,000.00 USD | 0.00 USD | 2,440.00 USD | `-55.52%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,410,000.00 USD | 0.00 USD | 226.17 USD | `-54.92%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,410,000.00 USD | 0.00 USD | 1,710.00 USD | `-54.31%` | `22,623,800,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,410,000.00 USD | 0.00 USD | 14,690.00 USD | `-53.71%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,390,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.89%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0815` | 1,390,000.00 USD | 0.00 USD | 815.00 USD | `-50.68%` | `10,000,000,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,390,000.00 USD | 0.00 USD | 23,260.00 USD | `-50.08%` | `281,949,900,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,360,000.00 USD | 0.00 USD | 2,580.00 USD | `-48.26%` | `30,172,300,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,360,000.00 USD | 0.00 USD | 19,460.00 USD | `-47.66%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,340,000.00 USD | 0.00 USD | 518.25 USD | `-47.05%` | `5,922,900,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,340,000.00 USD | 0.00 USD | 362.62 USD | `-46.44%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,340,000.00 USD | 0.00 USD | 362.22 USD | `-45.84%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,340,000.00 USD | 0.00 USD | 113.80 USD | `-44.63%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,340,000.00 USD | 0.00 USD | 2,300.00 USD | `-44.02%` | `24,866,500,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,340,000.00 USD | 0.00 USD | 814.24 USD | `-43.42%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,340,000.00 USD | 0.00 USD | 1,510.00 USD | `-42.81%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,340,000.00 USD | 0.00 USD | 1,910.00 USD | `-42.21%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,330,000.00 USD | 0.00 USD | 2,320.00 USD | `-41.60%` | `24,090,300,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 12,280.00 USD | `-40.39%` | `124,716,300,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,320,000.00 USD | 0.00 USD | 16,370.00 USD | `-39.79%` | `164,490,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,300,000.00 USD | 0.00 USD | 2,950.00 USD | `-39.18%` | `29,364,800,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,300,000.00 USD | 0.00 USD | 7,310.00 USD | `-37.97%` | `71,304,800,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 802.14 USD | `-37.37%` | `7,750,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,290,000.00 USD | 0.00 USD | 6,230.00 USD | `-36.76%` | `59,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,290,000.00 USD | 0.00 USD | 8,190.00 USD | `-36.16%` | `77,610,300,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,280,000.00 USD | 0.00 USD | 450.48 USD | `-35.55%` | `4,229,900,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,280,000.00 USD | 0.00 USD | 1,060.00 USD | `-34.95%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,280,000.00 USD | 0.00 USD | 125,900.00 USD | `-34.34%` | `1,160,394,900,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,150,000.00 USD | 0.00 USD | 105.42 USD | `-33.74%` | `962,700,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,150,000.00 USD | 0.00 USD | 14,360.00 USD | `-33.13%` | `129,913,800,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,140,000.00 USD | 0.00 USD | 425.50 USD | `-32.53%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,140,000.00 USD | 0.00 USD | 368.45 USD | `-31.92%` | `3,275,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,140,000.00 USD | 0.00 USD | 281.48 USD | `-31.32%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,140,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.71%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,130,000.00 USD | 0.00 USD | 7,820.00 USD | `-30.11%` | `67,704,600,000,000.01` |
| `Live` | `Long` | `0.1165` | 1,120,000.00 USD | 0.00 USD | 1,290.00 USD | `-29.50%` | `11,058,900,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,120,000.00 USD | 0.00 USD | 6,640.00 USD | `-28.90%` | `56,551,000,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,110,000.00 USD | 0.00 USD | 25,800.00 USD | `-28.29%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,090,000.00 USD | 0.00 USD | 1,830.00 USD | `-27.69%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,080,000.00 USD | 0.00 USD | 303.75 USD | `-26.48%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,080,000.00 USD | 0.00 USD | 19,380.00 USD | `-25.87%` | `158,167,100,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,060,000.00 USD | 0.00 USD | 50,430.00 USD | `-25.26%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,010,000.00 USD | 0.00 USD | 1,060.00 USD | `-24.66%` | `8,486,000,000,000.00` |
| `Live` | `Long` | `0.1255` | 1,010,000.00 USD | 0.00 USD | 134.66 USD | `-24.05%` | `1,073,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 1,010,000.00 USD | 0.00 USD | 29,370.00 USD | `-23.45%` | `232,151,600,000,000.00` |
| `Live` | `Long` | `0.1285` | 982,560.00 USD | 0.00 USD | 9,780.00 USD | `-22.24%` | `76,071,500,000,000.00` |
| `Live` | `Long` | `0.1295` | 972,780.00 USD | 0.00 USD | 3,750.00 USD | `-21.63%` | `28,932,500,000,000.00` |
| `Live` | `Long` | `0.1305` | 969,030.00 USD | 0.00 USD | 16,660.00 USD | `-21.03%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 952,380.00 USD | 0.00 USD | 12,580.00 USD | `-20.42%` | `95,671,200,000,000.00` |
| `Live` | `Long` | `0.1325` | 939,800.00 USD | 0.00 USD | 4,810.00 USD | `-19.82%` | `36,288,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 934,990.00 USD | 0.00 USD | 55,620.00 USD | `-19.21%` | `416,597,000,000,000.00` |
| `Live` | `Long` | `0.1345` | 879,370.00 USD | 0.00 USD | 44,440.00 USD | `-18.61%` | `330,382,400,000,000.00` |
| `Live` | `Long` | `0.1355` | 834,940.00 USD | 0.00 USD | 8,620.00 USD | `-18.00%` | `63,632,100,000,000.00` |
| `Live` | `Long` | `0.1365` | 826,310.00 USD | 0.00 USD | 4,240.00 USD | `-17.40%` | `31,078,200,000,000.00` |
| `Live` | `Long` | `0.1375` | 822,070.00 USD | 0.00 USD | 13,710.00 USD | `-16.79%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 808,360.00 USD | 0.00 USD | 16,480.00 USD | `-16.19%` | `119,008,400,000,000.00` |
| `Live` | `Long` | `0.1395` | 791,880.00 USD | 0.00 USD | 5,960.00 USD | `-15.58%` | `42,721,100,000,000.00` |
| `Live` | `Long` | `0.1405` | 785,920.00 USD | 0.00 USD | 2,640.00 USD | `-14.98%` | `18,781,700,000,000.00` |
| `Live` | `Long` | `0.1415` | 783,280.00 USD | 0.00 USD | 19,390.00 USD | `-14.37%` | `137,014,700,000,000.02` |
| `Live` | `Long` | `0.1425` | 763,890.00 USD | 0.00 USD | 499,000.00 USD | `-13.77%` | `3,501,785,500,000,000.00` |
| `Live` | `Long` | `0.1435` | 264,890.00 USD | 0.00 USD | 18,970.00 USD | `-13.16%` | `132,163,100,000,000.00` |
| `Live` | `Long` | `0.1445` | 245,920.00 USD | 0.00 USD | 9,510.00 USD | `-12.56%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 236,410.00 USD | 0.00 USD | 92,570.00 USD | `-11.95%` | `636,187,800,000,000.00` |
| `Live` | `Long` | `0.1465` | 143,840.00 USD | 0.00 USD | 31,100.00 USD | `-11.35%` | `212,319,500,000,000.00` |
| `Live` | `Long` | `0.1475` | 112,740.00 USD | 0.00 USD | 80,080.00 USD | `-10.74%` | `542,919,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 32,660.00 USD | 0.00 USD | 2,500.00 USD | `-10.14%` | `16,826,900,000,000.00` |
| `Live` | `Long` | `0.1495` | 30,160.00 USD | 0.00 USD | 1,720.00 USD | `-9.53%` | `11,513,300,000,000.00` |
| `Live` | `Long` | `0.1515` | 28,440.00 USD | 0.00 USD | 2,570.00 USD | `-8.32%` | `16,978,000,000,000.00` |
| `Live` | `Long` | `0.1525` | 25,860.00 USD | 0.00 USD | 2,140.00 USD | `-7.72%` | `14,050,400,000,000.00` |
| `Live` | `Long` | `0.1535` | 23,720.00 USD | 0.00 USD | 11,530.00 USD | `-7.11%` | `75,134,600,000,000.00` |
| `Live` | `Long` | `0.1545` | 12,190.00 USD | 0.00 USD | 3,230.00 USD | `-6.51%` | `20,932,600,000,000.00` |
| `Live` | `Long` | `0.1565` | 8,950.00 USD | 0.00 USD | 8,950.00 USD | `-5.30%` | `57,214,100,000,000.00` |
| `Live` | `Short` | `0.1665` | 215.45 USD | 215.45 USD | 0.00 USD | `+0.76%` | `1,294,000,000,000.00` |
| `Live` | `Short` | `0.1675` | 4,860.00 USD | 4,640.00 USD | 0.00 USD | `+1.36%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1715` | 6,340.00 USD | 1,480.00 USD | 0.00 USD | `+3.78%` | `8,642,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 6,480.00 USD | 138.82 USD | 0.00 USD | `+8.02%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1845` | 9,110.00 USD | 2,630.00 USD | 0.00 USD | `+11.65%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1855` | 9,730.00 USD | 616.01 USD | 0.00 USD | `+12.25%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 13,320.00 USD | 3,600.00 USD | 0.00 USD | `+13.46%` | `19,174,300,000,000.00` |
| `Live` | `Short` | `0.1945` | 13,950.00 USD | 623.68 USD | 0.00 USD | `+17.70%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 14,100.00 USD | 150.10 USD | 0.00 USD | `+19.52%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 25,690.00 USD | 11,590.00 USD | 0.00 USD | `+24.36%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2065` | 29,850.00 USD | 4,160.00 USD | 0.00 USD | `+24.96%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2075` | 30,370.00 USD | 514.81 USD | 0.00 USD | `+25.57%` | `2,481,000,000,000.00` |
| `Live` | `Short` | `0.2085` | 30,560.00 USD | 198.08 USD | 0.00 USD | `+26.17%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 30,730.00 USD | 164.23 USD | 0.00 USD | `+26.78%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 30,920.00 USD | 190.73 USD | 0.00 USD | `+27.38%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2135` | 46,610.00 USD | 15,690.00 USD | 0.00 USD | `+29.20%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 87,950.00 USD | 41,330.00 USD | 0.00 USD | `+30.41%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 88,160.00 USD | 213.22 USD | 0.00 USD | `+31.62%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 175,960.00 USD | 87,800.00 USD | 0.00 USD | `+32.83%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2205` | 202,200.00 USD | 26,240.00 USD | 0.00 USD | `+33.43%` | `118,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 202,310.00 USD | 114.52 USD | 0.00 USD | `+35.25%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2245` | 202,650.00 USD | 338.64 USD | 0.00 USD | `+35.85%` | `1,508,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 202,800.00 USD | 154.78 USD | 0.00 USD | `+36.46%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 209,790.00 USD | 6,980.00 USD | 0.00 USD | `+38.88%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 225,720.00 USD | 15,930.00 USD | 0.00 USD | `+42.51%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 225,820.00 USD | 102.62 USD | 0.00 USD | `+43.72%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 226,610.00 USD | 796.25 USD | 0.00 USD | `+46.75%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2435` | 275,310.00 USD | 48,700.00 USD | 0.00 USD | `+47.35%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2455` | 275,550.00 USD | 231.97 USD | 0.00 USD | `+48.56%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2465` | 297,590.00 USD | 22,040.00 USD | 0.00 USD | `+49.17%` | `89,431,500,000,000.00` |
| `Live` | `Short` | `0.2545` | 298,140.00 USD | 546.54 USD | 0.00 USD | `+54.01%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 302,000.00 USD | 3,870.00 USD | 0.00 USD | `+55.22%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 330,910.00 USD | 28,910.00 USD | 0.00 USD | `+55.82%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 383,530.00 USD | 52,620.00 USD | 0.00 USD | `+56.43%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 383,690.00 USD | 154.94 USD | 0.00 USD | `+58.25%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2635` | 566,200.00 USD | 182,510.00 USD | 0.00 USD | `+59.46%` | `692,636,800,000,000.00` |
| `Live` | `Short` | `0.2685` | 566,420.00 USD | 226.51 USD | 0.00 USD | `+62.48%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 579,670.00 USD | 13,240.00 USD | 0.00 USD | `+64.30%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 579,880.00 USD | 214.21 USD | 0.00 USD | `+64.90%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 591,480.00 USD | 11,600.00 USD | 0.00 USD | `+66.11%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 591,960.00 USD | 482.84 USD | 0.00 USD | `+69.14%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2835` | 592,120.00 USD | 154.73 USD | 0.00 USD | `+71.56%` | `545,800,000,000.00` |
| `Live` | `Short` | `0.2915` | 890,180.00 USD | 298,060.00 USD | 0.00 USD | `+76.40%` | `1,022,511,200,000,000.00` |
| `Live` | `Short` | `0.2925` | 890,970.00 USD | 794.52 USD | 0.00 USD | `+77.00%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2985` | 891,450.00 USD | 474.76 USD | 0.00 USD | `+80.64%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.2995` | 893,340.00 USD | 1,900.00 USD | 0.00 USD | `+81.24%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3025` | 895,640.00 USD | 2,300.00 USD | 0.00 USD | `+83.06%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3075` | 901,940.00 USD | 6,290.00 USD | 0.00 USD | `+86.08%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 902,300.00 USD | 363.72 USD | 0.00 USD | `+86.69%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 914,220.00 USD | 11,930.00 USD | 0.00 USD | `+87.90%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3175` | 914,450.00 USD | 227.49 USD | 0.00 USD | `+92.13%` | `716,500,000,000.00` |
| `Live` | `Short` | `0.3195` | 914,700.00 USD | 247.87 USD | 0.00 USD | `+93.34%` | `775,800,000,000.00` |
| `Live` | `Short` | `0.3285` | 972,090.00 USD | 57,390.00 USD | 0.00 USD | `+98.79%` | `174,708,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 840,930.00 USD | 0.00 USD | 355.00 USD | `-78.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 840,570.00 USD | 0.00 USD | 297.50 USD | `-74.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 840,270.00 USD | 0.00 USD | 353.50 USD | `-69.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 839,920.00 USD | 0.00 USD | 276.53 USD | `-67.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 839,640.00 USD | 0.00 USD | 4,310.00 USD | `-66.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 835,330.00 USD | 0.00 USD | 475.11 USD | `-61.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 834,850.00 USD | 0.00 USD | 131.16 USD | `-60.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 834,720.00 USD | 0.00 USD | 881.45 USD | `-59.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 833,840.00 USD | 0.00 USD | 1,070.00 USD | `-59.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 832,770.00 USD | 0.00 USD | 1,050.00 USD | `-58.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 831,720.00 USD | 0.00 USD | 1,010.00 USD | `-57.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 830,710.00 USD | 0.00 USD | 4,100.00 USD | `-57.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 826,600.00 USD | 0.00 USD | 529.04 USD | `-56.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 826,080.00 USD | 0.00 USD | 2,390.00 USD | `-56.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 823,690.00 USD | 0.00 USD | 757.39 USD | `-54.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 822,930.00 USD | 0.00 USD | 1,490.00 USD | `-52.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 821,440.00 USD | 0.00 USD | 277.37 USD | `-47.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 821,170.00 USD | 0.00 USD | 262.50 USD | `-47.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 820,900.00 USD | 0.00 USD | 795.57 USD | `-46.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 820,110.00 USD | 0.00 USD | 181.00 USD | `-45.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 819,930.00 USD | 0.00 USD | 3,810.00 USD | `-39.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 816,110.00 USD | 0.00 USD | 1,550.00 USD | `-37.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 814,570.00 USD | 0.00 USD | 116.07 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 814,450.00 USD | 0.00 USD | 19,070.00 USD | `-34.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 795,380.00 USD | 0.00 USD | 577.22 USD | `-33.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 794,800.00 USD | 0.00 USD | 343.50 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 794,460.00 USD | 0.00 USD | 26,280.00 USD | `-29.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 768,180.00 USD | 0.00 USD | 105.75 USD | `-28.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 768,070.00 USD | 0.00 USD | 24,280.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 743,790.00 USD | 0.00 USD | 83,620.00 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 660,170.00 USD | 0.00 USD | 487.10 USD | `-25.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 659,680.00 USD | 0.00 USD | 14,940.00 USD | `-24.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 644,740.00 USD | 0.00 USD | 129,320.00 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 515,420.00 USD | 0.00 USD | 2,670.00 USD | `-23.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 512,750.00 USD | 0.00 USD | 473.27 USD | `-22.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 512,280.00 USD | 0.00 USD | 203,210.00 USD | `-22.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 309,070.00 USD | 0.00 USD | 1,670.00 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 307,400.00 USD | 0.00 USD | 1,590.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 305,810.00 USD | 0.00 USD | 6,000.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 299,800.00 USD | 0.00 USD | 795.99 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 299,010.00 USD | 0.00 USD | 502.28 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 298,500.00 USD | 0.00 USD | 162.60 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 298,340.00 USD | 0.00 USD | 700.86 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 297,640.00 USD | 0.00 USD | 13,710.00 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 283,930.00 USD | 0.00 USD | 108.57 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 283,820.00 USD | 0.00 USD | 3,520.00 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 280,300.00 USD | 0.00 USD | 127.35 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 280,170.00 USD | 0.00 USD | 24,850.00 USD | `-13.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 255,320.00 USD | 0.00 USD | 1,300.00 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 254,020.00 USD | 0.00 USD | 25,960.00 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 228,060.00 USD | 0.00 USD | 46,010.00 USD | `-11.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 182,060.00 USD | 0.00 USD | 15,150.00 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 166,910.00 USD | 0.00 USD | 2,400.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 164,500.00 USD | 0.00 USD | 2,340.00 USD | `-10.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 162,160.00 USD | 0.00 USD | 2,390.00 USD | `-9.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 159,770.00 USD | 0.00 USD | 3,010.00 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 156,760.00 USD | 0.00 USD | 192.48 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 156,570.00 USD | 0.00 USD | 4,520.00 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 152,060.00 USD | 0.00 USD | 32,990.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 119,070.00 USD | 0.00 USD | 7,350.00 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 111,720.00 USD | 0.00 USD | 500.87 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 111,220.00 USD | 0.00 USD | 14,340.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 96,880.00 USD | 0.00 USD | 499.16 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 96,380.00 USD | 0.00 USD | 9,980.00 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 86,400.00 USD | 0.00 USD | 2,570.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 83,830.00 USD | 0.00 USD | 19,290.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 64,540.00 USD | 0.00 USD | 516.91 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 64,030.00 USD | 0.00 USD | 249.16 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 63,780.00 USD | 0.00 USD | 1,040.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 62,730.00 USD | 0.00 USD | 62,730.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 3,190.00 USD | 3,190.00 USD | 0.00 USD | `+0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 42,230.00 USD | 39,040.00 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 42,820.00 USD | 589.50 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 43,970.00 USD | 1,150.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 44,120.00 USD | 153.58 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 44,680.00 USD | 564.90 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 46,480.00 USD | 1,800.00 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 47,190.00 USD | 706.39 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 47,710.00 USD | 524.32 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 47,930.00 USD | 219.54 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 69,910.00 USD | 21,980.00 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 70,590.00 USD | 683.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 70,930.00 USD | 336.40 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 71,830.00 USD | 898.02 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 76,860.00 USD | 5,030.00 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 88,520.00 USD | 11,660.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 99,360.00 USD | 10,840.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 100,230.00 USD | 864.12 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 102,750.00 USD | 2,520.00 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 103,030.00 USD | 276.75 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 103,160.00 USD | 128.68 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 106,530.00 USD | 3,370.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 110,230.00 USD | 3,700.00 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 110,480.00 USD | 245.50 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 111,010.00 USD | 531.47 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 111,710.00 USD | 697.34 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 111,930.00 USD | 222.24 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 141,050.00 USD | 29,130.00 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 148,130.00 USD | 7,070.00 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 148,320.00 USD | 194.50 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 148,460.00 USD | 137.77 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 148,590.00 USD | 133.19 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 152,340.00 USD | 3,750.00 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 152,830.00 USD | 492.19 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 175,590.00 USD | 22,750.00 USD | 0.00 USD | `+21.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 176,150.00 USD | 560.96 USD | 0.00 USD | `+21.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 197,490.00 USD | 21,340.00 USD | 0.00 USD | `+22.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 283,380.00 USD | 85,900.00 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 284,850.00 USD | 1,470.00 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 285,020.00 USD | 174.20 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 287,100.00 USD | 2,080.00 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 287,350.00 USD | 252.51 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 289,720.00 USD | 2,370.00 USD | 0.00 USD | `+27.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 289,850.00 USD | 126.50 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 290,200.00 USD | 356.72 USD | 0.00 USD | `+28.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 290,560.00 USD | 361.76 USD | 0.00 USD | `+30.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 290,930.00 USD | 363.44 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 291,290.00 USD | 365.12 USD | 0.00 USD | `+31.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 297,570.00 USD | 6,280.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 297,940.00 USD | 368.47 USD | 0.00 USD | `+32.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 320,430.00 USD | 22,490.00 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 320,760.00 USD | 333.91 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 324,740.00 USD | 3,980.00 USD | 0.00 USD | `+35.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 325,120.00 USD | 378.55 USD | 0.00 USD | `+36.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 325,500.00 USD | 380.23 USD | 0.00 USD | `+37.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 329,330.00 USD | 3,840.00 USD | 0.00 USD | `+38.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 363,150.00 USD | 33,820.00 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 367,420.00 USD | 4,260.00 USD | 0.00 USD | `+40.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 368,930.00 USD | 1,520.00 USD | 0.00 USD | `+41.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 390,160.00 USD | 21,230.00 USD | 0.00 USD | `+43.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 392,690.00 USD | 2,530.00 USD | 0.00 USD | `+44.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 412,410.00 USD | 19,720.00 USD | 0.00 USD | `+45.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 421,710.00 USD | 9,300.00 USD | 0.00 USD | `+46.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 423,620.00 USD | 1,910.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 442,370.00 USD | 18,750.00 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 442,920.00 USD | 551.23 USD | 0.00 USD | `+49.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 443,320.00 USD | 397.90 USD | 0.00 USD | `+50.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 447,650.00 USD | 4,330.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 447,970.00 USD | 320.66 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 463,860.00 USD | 15,880.00 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 465,860.00 USD | 2,000.00 USD | 0.00 USD | `+54.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 468,410.00 USD | 2,550.00 USD | 0.00 USD | `+54.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 480,140.00 USD | 11,730.00 USD | 0.00 USD | `+55.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 485,300.00 USD | 5,160.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 502,170.00 USD | 16,870.00 USD | 0.00 USD | `+57.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 528,960.00 USD | 26,790.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 529,230.00 USD | 272.88 USD | 0.00 USD | `+63.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 529,340.00 USD | 114.99 USD | 0.00 USD | `+66.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 529,740.00 USD | 394.01 USD | 0.00 USD | `+67.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 530,110.00 USD | 375.53 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 532,250.00 USD | 2,130.00 USD | 0.00 USD | `+72.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 532,830.00 USD | 579.27 USD | 0.00 USD | `+73.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 534,580.00 USD | 1,750.00 USD | 0.00 USD | `+75.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 534,680.00 USD | 101.21 USD | 0.00 USD | `+78.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 534,940.00 USD | 262.73 USD | 0.00 USD | `+79.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 536,380.00 USD | 1,440.00 USD | 0.00 USD | `+80.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 541,810.00 USD | 5,430.00 USD | 0.00 USD | `+81.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 547,240.00 USD | 5,430.00 USD | 0.00 USD | `+82.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 547,530.00 USD | 289.61 USD | 0.00 USD | `+84.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 548,010.00 USD | 487.09 USD | 0.00 USD | `+85.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 554,590.00 USD | 6,570.00 USD | 0.00 USD | `+87.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 559,760.00 USD | 5,180.00 USD | 0.00 USD | `+90.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 577,280.00 USD | 17,520.00 USD | 0.00 USD | `+92.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1310` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 6,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1313` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,680,000.00 USD | 0.00 USD | 8,680,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD |
| `7D` | `0.1325` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1397` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `0.1400` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1403` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1418` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `0.1419` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1421` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1422` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD |
| `1D` | `0.1425` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD |
| `1D` | `0.1428` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1430` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1433` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD |
| `1D` | `0.1434` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1437` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD |
| `7D` | `0.1439` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 23,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1440` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD |
| `7D` | `0.1442` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 0.00 USD | 2,750.00 USD | 6,160.00 USD |
| `1D` | `0.1443` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD |
| `1D` | `0.1446` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD |
| `7D` | `0.1451` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD |
| `1D` | `0.1452` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1454` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `0.1455` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1458` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD |
| `1D` | `0.1461` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD |
| `1D` | `0.1464` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD |
| `7D` | `0.1466` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD |
| `7D` | `0.1469` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1470` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD |
| `7D` | `0.1472` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD |
| `7D` | `0.1475` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD |
| `1D` | `0.1476` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD |
| `7D` | `0.1478` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1479` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD |
| `7D` | `0.1481` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD |
| `1D` | `0.1482` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD |
| `7D` | `0.1484` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD |
| `1D` | `0.1485` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD |
| `7D` | `0.1487` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1488` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD |
| `7D` | `0.1490` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD |
| `1D` | `0.1491` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 40,720.00 USD | 15,530.00 USD | 18,990.00 USD |
| `7D` | `0.1493` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1494` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 55,530.00 USD | 9,030.00 USD | 14,300.00 USD |
| `7D` | `0.1496` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1497` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD |
| `7D` | `0.1499` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1500` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD |
| `7D` | `0.1502` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1503` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD |
| `7D` | `0.1505` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1506` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 35,380.00 USD | 3,090.00 USD | 205,580.00 USD |
| `7D` | `0.1508` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1509` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD |
| `7D` | `0.1511` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1512` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD |
| `7D` | `0.1514` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1515` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD |
| `7D` | `0.1517` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1518` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD |
| `7D` | `0.1520` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1521` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD |
| `7D` | `0.1523` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1524` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1526` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1529` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1530` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD |
| `7D` | `0.1535` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1536` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1538` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1541` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1542` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1544` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1547` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1548` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD |
| `7D` | `0.1550` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1551` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD |
| `7D` | `0.1553` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1554` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1556` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD |
| `7D` | `0.1559` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1562` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD |
| `7D` | `0.1565` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1566` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD |
| `7D` | `0.1568` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1569` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD |
| `7D` | `0.1571` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1572` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD |
| `7D` | `0.1574` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD |
| `1D` | `0.1575` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1577` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1580` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD |
| `1D` | `0.1581` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD |
| `7D` | `0.1583` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1584` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD |
| `7D` | `0.1586` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1587` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 26,090.00 USD | 40,320.00 USD | 40,370.00 USD |
| `7D` | `0.1589` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 15,370.00 USD | 28,520.00 USD | 51,370.00 USD |
| `7D` | `0.1592` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1593` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 40,990.00 USD | 54,060.00 USD |
| `7D` | `0.1595` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1596` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD |
| `7D` | `0.1598` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1599` | 998,970.00 USD | 0.00 USD | 998,970.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1601` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1602` | 985,360.00 USD | 0.00 USD | 985,360.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1605` | 928,080.00 USD | 0.00 USD | 928,080.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1607` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD |
| `1D` | `0.1608` | 924,240.00 USD | 0.00 USD | 924,240.00 USD | 34,860.00 USD | 7,790.00 USD | 77,820.00 USD |
| `7D` | `0.1610` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD |
| `1D` | `0.1611` | 803,760.00 USD | 0.00 USD | 803,760.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD |
| `7D` | `0.1613` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD |
| `1D` | `0.1614` | 766,980.00 USD | 0.00 USD | 766,980.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `7D` | `0.1616` | 892,950.00 USD | 0.00 USD | 892,950.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1620` | 728,310.00 USD | 0.00 USD | 728,310.00 USD | 10,990.00 USD | 17,910.00 USD | 0.00 USD |
| `7D` | `0.1622` | 705,360.00 USD | 0.00 USD | 705,360.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD |
| `1D` | `0.1623` | 699,410.00 USD | 0.00 USD | 699,410.00 USD | 65,520.00 USD | 22,690.00 USD | 36,570.00 USD |
| `7D` | `0.1625` | 550,140.00 USD | 0.00 USD | 550,140.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD |
| `1D` | `0.1626` | 574,630.00 USD | 0.00 USD | 574,630.00 USD | 63,990.00 USD | 15,100.00 USD | 60,280.00 USD |
| `7D` | `0.1628` | 290,950.00 USD | 0.00 USD | 290,950.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1629` | 435,260.00 USD | 0.00 USD | 435,260.00 USD | 20,520.00 USD | 3,520.00 USD | 111,100.00 USD |
| `7D` | `0.1631` | 214,170.00 USD | 0.00 USD | 214,170.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 300,120.00 USD | 0.00 USD | 300,120.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 177,820.00 USD | 0.00 USD | 177,820.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `0.1637` | 143,230.00 USD | 0.00 USD | 143,230.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `0.1638` | 169,130.00 USD | 0.00 USD | 169,130.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1640` | 119,680.00 USD | 0.00 USD | 119,680.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1641` | 140,010.00 USD | 0.00 USD | 140,010.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1643` | 90,430.00 USD | 0.00 USD | 90,430.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD |
| `1D` | `0.1644` | 120,940.00 USD | 0.00 USD | 120,940.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD |
| `7D` | `0.1646` | 20,780.00 USD | 0.00 USD | 20,780.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.1647` | 58,440.00 USD | 0.00 USD | 58,440.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD |
| `7D` | `0.1649` | 7,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD |
| `1D` | `0.1650` | 32,630.00 USD | 0.00 USD | 32,630.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD |
| `1D` | `0.1651` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1654` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1661` | 103,750.00 USD | 103,750.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1662` | 36,390.00 USD | 36,390.00 USD | 0.00 USD | 0.00 USD | 8,980.00 USD | 27,410.00 USD |
| `7D` | `0.1664` | 265,580.00 USD | 265,580.00 USD | 0.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD |
| `1D` | `0.1665` | 136,710.00 USD | 136,710.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | 91,040.00 USD |
| `7D` | `0.1667` | 320,830.00 USD | 320,830.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1668` | 182,660.00 USD | 182,660.00 USD | 0.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD |
| `7D` | `0.1670` | 630,710.00 USD | 630,710.00 USD | 0.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 211,830.00 USD | 211,830.00 USD | 0.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1673` | 675,050.00 USD | 675,050.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD |
| `1D` | `0.1674` | 281,360.00 USD | 281,360.00 USD | 0.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 900,830.00 USD | 900,830.00 USD | 0.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD |
| `1D` | `0.1677` | 320,820.00 USD | 320,820.00 USD | 0.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD |
| `7D` | `0.1679` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD |
| `1D` | `0.1680` | 416,040.00 USD | 416,040.00 USD | 0.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD |
| `7D` | `0.1682` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 518,490.00 USD | 518,490.00 USD | 0.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD |
| `7D` | `0.1685` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 652,550.00 USD | 652,550.00 USD | 0.00 USD | 25,170.00 USD | 51,130.00 USD | 57,760.00 USD |
| `7D` | `0.1688` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 776,250.00 USD | 776,250.00 USD | 0.00 USD | 41,580.00 USD | 32,630.00 USD | 49,480.00 USD |
| `7D` | `0.1691` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD |
| `1D` | `0.1692` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 84,920.00 USD | 84,150.00 USD | 135,420.00 USD |
| `7D` | `0.1694` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1695` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 53,760.00 USD | 26,310.00 USD | 26,570.00 USD |
| `7D` | `0.1697` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1698` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1701` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `7D` | `0.1703` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1704` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1706` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1707` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD |
| `7D` | `0.1709` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD |
| `1D` | `0.1713` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `0.1715` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD |
| `7D` | `0.1718` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 39,720.00 USD | 20,360.00 USD | 8,520.00 USD |
| `7D` | `0.1721` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD |
| `1D` | `0.1722` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 82,880.00 USD | 28,200.00 USD | 63,630.00 USD |
| `7D` | `0.1724` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD |
| `1D` | `0.1725` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 8,230.00 USD | 11,530.00 USD | 63,550.00 USD |
| `1D` | `0.1728` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 18,490.00 USD | 0.00 USD | 14,080.00 USD |
| `7D` | `0.1730` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 306,550.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1733` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD |
| `1D` | `0.1737` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD |
| `7D` | `0.1739` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1740` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD |
| `1D` | `0.1743` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1745` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD |
| `7D` | `0.1748` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1751` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1752` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD |
| `7D` | `0.1754` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD |
| `1D` | `0.1755` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD |
| `7D` | `0.1757` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1758` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD |
| `7D` | `0.1760` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD |
| `7D` | `0.1763` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD |
| `1D` | `0.1764` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD |
| `7D` | `0.1766` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 163,180.00 USD | 165,520.00 USD | 36,540.00 USD |
| `1D` | `0.1767` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD |
| `7D` | `0.1769` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 113,280.00 USD | 95,050.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD |
| `7D` | `0.1772` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD |
| `7D` | `0.1775` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD |
| `7D` | `0.1778` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD |
| `1D` | `0.1779` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD |
| `7D` | `0.1781` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1782` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD |
| `7D` | `0.1784` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD |
| `7D` | `0.1787` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1790` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1791` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD |
| `7D` | `0.1793` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1794` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD |
| `7D` | `0.1796` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1797` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD |
| `7D` | `0.1799` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1800` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD |
| `7D` | `0.1802` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD |
| `1D` | `0.1803` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD |
| `7D` | `0.1805` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1806` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD |
| `7D` | `0.1808` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD |
| `7D` | `0.1811` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD |
| `1D` | `0.1812` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD |
| `7D` | `0.1814` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD |
| `1D` | `0.1815` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `0.1817` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1818` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD |
| `7D` | `0.1820` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 52,150.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1821` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 13,320.00 USD | 8,820.00 USD |
| `7D` | `0.1823` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 62,540.00 USD | 18,340.00 USD | 105,730.00 USD |
| `1D` | `0.1824` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 14,120.00 USD | 9,310.00 USD | 10,340.00 USD |
| `7D` | `0.1826` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD |
| `1D` | `0.1827` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 9,350.00 USD | 3,020.00 USD | 2,610.00 USD |
| `7D` | `0.1829` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `1D` | `0.1830` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `0.1832` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD |
| `1D` | `0.1833` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD |
| `7D` | `0.1835` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 111,430.00 USD | 46,260.00 USD | 16,530.00 USD |
| `7D` | `0.1838` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 69,120.00 USD | 39,080.00 USD | 106,440.00 USD |
| `1D` | `0.1839` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 6,560.00 USD |
| `1D` | `0.1840` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 1,470.00 USD | 1,970.00 USD | 0.00 USD |
| `7D` | `0.1841` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 56,160.00 USD | 47,560.00 USD | 45,300.00 USD |
| `7D` | `0.1844` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 34,630.00 USD | 3,900.00 USD | 72,920.00 USD |
| `7D` | `0.1847` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD |
| `7D` | `0.1853` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 62,090.00 USD | 9,590.00 USD | 138,780.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `184.59M` | Total OI Tokens: `1,124,505,908.1 ARB`
  * 1h OI Change: `-2.28%` | 4h OI Change: `+4.29%` | 24h OI Change: `-15.72%`
  * Exchange Breakdown: Binance=`41.98M` | Bybit=`26.50M` | OKX=`14.39M` | Hyperliquid=`13.20M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.62K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0026%` | **USDT OKX** | `0.0083%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0081%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0046%` | **USDT Bitget** | `-0.0068%` |
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
| `4H` | `ARB` | `45.91%` | `54.09%` | `0.85` | 23,400,000.00 USD |
| `4H` | `Binance` | `51.42%` | `48.58%` | `1.06` | 8,070,000.00 USD |
| `4H` | `OKX` | `50.7%` | `49.3%` | `1.03` | 2,310,000.00 USD |
| `4H` | `Bybit` | `53.11%` | `46.89%` | `1.13` | 2,750,000.00 USD |
| `4H` | `KuCoin` | `49.65%` | `50.35%` | `0.99` | 1,000,000.00 USD |
| `4H` | `Gate` | `40.33%` | `59.67%` | `0.68` | 310,670.00 USD |
| `4H` | `Bitget` | `52.57%` | `47.43%` | `1.11` | 380,680.00 USD |
| `4H` | `BingX` | `11.68%` | `88.32%` | `0.13` | 2,840,000.00 USD |
| `4H` | `MEXC` | `46.65%` | `53.35%` | `0.87` | 841,710.00 USD |
| `4H` | `Bitunix` | `44.05%` | `55.95%` | `0.79` | 348,910.00 USD |
| `4H` | `Hyperliquid` | `66.15%` | `33.85%` | `1.95` | 154,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.35%` | `51.65%` | `0.94` | 4,130,000.00 USD |
| `4H` | `Crypto.com` | `0.57%` | `99.43%` | `0.01` | 714.95 USD |
| `4H` | `WhiteBIT` | `73.9%` | `26.1%` | `2.83` | 165,450.00 USD |
| `4H` | `HTX` | `54.81%` | `45.19%` | `1.21` | 8,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `2.89%` | `97.11%` | `0.03` | 28,820.00 USD |
| `4H` | `Aster` | `83.63%` | `16.37%` | `5.11` | 567.30 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.9%` | `35.1%` | `1.85` | 50,910.00 USD |
| `4H` | `Whale Positions` | `51.42%` | `48.58%` | `1.06` | 8,070,000.00 USD |
| `4H` | `Global Accounts` | `45.91%` | `54.09%` | `0.85` | 23,400,000.00 USD |


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
| `0:00 UTC` | `0.1634` | `0.1640` | `0.1634` | `0.1654` | `0.1630` | 850,812.60 USD | 458,109.86 USD | 392,702.74 USD | 65,407.12 USD | `+7.69%` | `26B / 10S` |

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
| `5m` | -24,710.00 USD | 42,810.00 USD | **`ACCUMULATION`** |
| `15m` | 56,980.00 USD | -703,290.00 USD | **`DISTRIBUTION`** |
| `30m` | -44,780.00 USD | -769,160.00 USD | **`DISTRIBUTION`** |
| `1h` | -116,170.00 USD | -1,810,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,360.00 USD | -2,860,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -162,820.00 USD | -1,210,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -290,080.00 USD | -2,430,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -62,990.00 USD | -2,540,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,290,000.00 USD | -6,710,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,030,000.00 USD | -11,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,650,000.00 USD | -38,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,740,000.00 USD | -163,920,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-24.71K` | 15m=`+56.98K` | 1h=`-116.17K` | 24h=`-2.03M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
