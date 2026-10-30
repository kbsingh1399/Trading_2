# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 10:52:59 IST` (`2026-10-30 05:22:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1656` | `0.1660` | `0.1649` | `0.1650` | `2,769,081` | 458,154.61 USD | -160,893.33 USD | `-35.12%` | -8,421,692.03 USD | `-1.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1650` | `0.1656` | `0.1649` | `0.1656` | `2,150,462` | 355,378.53 USD | -124,572.18 USD | `-35.05%` | -8,546,264.20 USD | `-0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1656` | `0.1660` | `0.1655` | `0.1658` | `985,667` | 163,388.90 USD | -2,393.75 USD | `-1.47%` | -8,548,657.95 USD | `+0.18` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1623` | `0.1639` | `0.1618` | `0.1637` | `11,341,584` | 1,849,966.09 USD | -639,400.43 USD | `-34.56%` | -8,223,413.46 USD | `-1.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1637` | `0.1660` | `0.1635` | `0.1650` | `10,426,658` | 1,718,232.82 USD | -224,519.98 USD | `-13.07%` | -8,447,933.44 USD | `-0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1650` | `0.1660` | `0.1649` | `0.1657` | `3,129,572` | 517,680.58 USD | -128,027.88 USD | `-24.73%` | -8,575,961.32 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1580` | `20,448,591` | 3,216,248.24 USD | 252,196.82 USD | `+7.84%` | -7,911,945.27 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1580` | `0.1639` | `0.1577` | `0.1637` | `36,120,104` | 5,820,548.12 USD | -303,641.20 USD | `-5.22%` | -8,215,586.47 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1637` | `0.1660` | `0.1635` | `0.1658` | `13,562,787` | 2,237,000.25 USD | -351,485.90 USD | `-15.71%` | -8,567,072.37 USD | `+0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1660` | `0.1577` | `0.1657` | `49,676,234` | 8,056,445.06 USD | -656,172.60 USD | `-8.14%` | -7,867,915.24 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -1,669,122.15 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,866,580.15 USD | `-0.65` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,590,804.13 USD | `-1.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -7,211,742.64 USD | `+0.69` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1660` | `0.1577` | `0.1657` | `49,676,234` | 8,056,445.06 USD | -656,172.60 USD | `-8.14%` | -7,867,915.24 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `7D` | `Long Liquidation` | `0.1304` | 8,540,000.00 USD | 8,540,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 959,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,530,000.00 USD | 8,530,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,660.00 USD | 942,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,510,000.00 USD | 8,510,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,490,000.00 USD | 8,490,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,470,000.00 USD | 8,470,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 17,180.00 USD | 937,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,440,000.00 USD | 8,440,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 8,410,000.00 USD | 8,410,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 8,380,000.00 USD | 8,380,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,200.00 USD | 920,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 8,370,000.00 USD | 8,370,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 8,340,000.00 USD | 8,340,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 44,860.00 USD | 869,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 8,300,000.00 USD | 8,300,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 8,240,000.00 USD | 8,240,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 8,210,000.00 USD | 8,210,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 8,180,000.00 USD | 8,180,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 824,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 8,160,000.00 USD | 8,160,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 8,120,000.00 USD | 8,120,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 8,100,000.00 USD | 8,100,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,630.00 USD | 823,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 8,080,000.00 USD | 8,080,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 8,060,000.00 USD | 8,060,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 812,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 8,020,000.00 USD | 8,020,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 8,010,000.00 USD | 8,010,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 16,480.00 USD | 798,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 7,950,000.00 USD | 7,950,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1395` | 4,610,000.00 USD | 4,610,000.00 USD | 6,700.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 782,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1398` | 4,590,000.00 USD | 4,590,000.00 USD | 12,500.00 USD | 953.16 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 7,850,000.00 USD | 7,850,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1401` | 4,580,000.00 USD | 4,580,000.00 USD | 9,130.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 7,840,000.00 USD | 7,840,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1404` | 4,570,000.00 USD | 4,570,000.00 USD | 2,140.00 USD | 1,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 5,540.00 USD | 776,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1407` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 1,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1410` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 1,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1413` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,690.00 USD | 770,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1419` | 4,560,000.00 USD | 4,560,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1422` | 4,550,000.00 USD | 4,550,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1425` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,990.00 USD | 754,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1428` | 4,530,000.00 USD | 4,530,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1430` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1433` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1434` | 4,530,000.00 USD | 4,530,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 254,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,790,000.00 USD | 7,790,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1437` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,750,000.00 USD | 7,750,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1440` | 4,500,000.00 USD | 4,500,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 5,260.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1443` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 235,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1446` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1452` | 4,450,000.00 USD | 4,450,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1454` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,420,000.00 USD | 4,420,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 225,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1458` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1464` | 4,400,000.00 USD | 4,400,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 31,840.00 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,690,000.00 USD | 7,690,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,370,000.00 USD | 4,370,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,580,000.00 USD | 7,580,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1470` | 4,350,000.00 USD | 4,350,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,570,000.00 USD | 7,570,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,330,000.00 USD | 4,330,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,540,000.00 USD | 7,540,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 87,010.00 USD | 101,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1476` | 4,180,000.00 USD | 4,180,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,500,000.00 USD | 7,500,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 3,930,000.00 USD | 3,930,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 7,230,000.00 USD | 7,230,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1482` | 3,760,000.00 USD | 3,760,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 7,140,000.00 USD | 7,140,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,580,000.00 USD | 3,580,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 14,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1487` | 6,940,000.00 USD | 6,940,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1488` | 3,450,000.00 USD | 3,450,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 6,840,000.00 USD | 6,840,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,420,000.00 USD | 3,420,000.00 USD | 34,570.00 USD | 12,130.00 USD | 14,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,730,000.00 USD | 6,730,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1494` | 3,360,000.00 USD | 3,360,000.00 USD | 51,430.00 USD | 6,010.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 1,720.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,660,000.00 USD | 6,660,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,290,000.00 USD | 3,290,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 6,420,000.00 USD | 6,420,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1500` | 3,230,000.00 USD | 3,230,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 6,330,000.00 USD | 6,330,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,220,000.00 USD | 3,220,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 6,320,000.00 USD | 6,320,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 1,470.00 USD | 10,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1506` | 2,980,000.00 USD | 2,980,000.00 USD | 35,380.00 USD | 3,090.00 USD | 206,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 6,180,000.00 USD | 6,180,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,770,000.00 USD | 5,770,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1512` | 2,580,000.00 USD | 2,580,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,570,000.00 USD | 2,570,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 9,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1517` | 5,250,000.00 USD | 5,250,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1518` | 2,180,000.00 USD | 2,180,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,090,000.00 USD | 2,090,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1524` | 2,010,000.00 USD | 2,010,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 1,970,000.00 USD | 1,970,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1530` | 1,940,000.00 USD | 1,940,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,780,000.00 USD | 4,780,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,350.00 USD | 8,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1536` | 1,880,000.00 USD | 1,880,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1542` | 1,830,000.00 USD | 1,830,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 1,790,000.00 USD | 1,790,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1545` | 1,640.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1548` | 1,760,000.00 USD | 1,760,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 1,710,000.00 USD | 1,710,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1554` | 1,660,000.00 USD | 1,660,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,630,000.00 USD | 1,630,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1560` | 1,600,000.00 USD | 1,600,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,580,000.00 USD | 1,580,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 4,370,000.00 USD | 4,370,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1566` | 1,530,000.00 USD | 1,530,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 4,270,000.00 USD | 4,270,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,400,000.00 USD | 1,400,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 3,990,000.00 USD | 3,990,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1572` | 1,270,000.00 USD | 1,270,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,730,000.00 USD | 3,730,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,140,000.00 USD | 1,140,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,580,000.00 USD | 3,580,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1578` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 3,440,000.00 USD | 3,440,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,130,000.00 USD | 1,130,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 3,180,000.00 USD | 3,180,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1584` | 1,110,000.00 USD | 1,110,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 3,110,000.00 USD | 3,110,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,000,000.00 USD | 1,000,000.00 USD | 20,600.00 USD | 40,320.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 3,070,000.00 USD | 3,070,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1590` | 901,250.00 USD | 901,250.00 USD | 0.00 USD | 17,180.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 842,230.00 USD | 842,230.00 USD | 0.00 USD | 33,440.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1596` | 784,870.00 USD | 784,870.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 783,660.00 USD | 783,660.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1602` | 770,050.00 USD | 770,050.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,700,000.00 USD | 2,700,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 712,770.00 USD | 712,770.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 2,330,000.00 USD | 2,330,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1608` | 708,930.00 USD | 708,930.00 USD | 34,860.00 USD | 7,790.00 USD | 81,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,850,000.00 USD | 1,850,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 584,770.00 USD | 584,770.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 1,490,000.00 USD | 1,490,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1614` | 547,990.00 USD | 547,990.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1616` | 789,420.00 USD | 789,420.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1620` | 509,320.00 USD | 509,320.00 USD | 0.00 USD | 17,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1622` | 601,830.00 USD | 601,830.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1623` | 491,400.00 USD | 491,400.00 USD | 34,770.00 USD | 0.00 USD | 17,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1625` | 521,470.00 USD | 521,470.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1626` | 439,110.00 USD | 439,110.00 USD | 63,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1628` | 295,720.00 USD | 295,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1629` | 375,120.00 USD | 375,120.00 USD | 0.00 USD | 3,520.00 USD | 104,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1631` | 218,940.00 USD | 218,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1632` | 267,490.00 USD | 267,490.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1635` | 145,190.00 USD | 145,190.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,460.00 USD | 3,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1637` | 148,000.00 USD | 148,000.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1638` | 136,500.00 USD | 136,500.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1640` | 124,450.00 USD | 124,450.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1641` | 107,380.00 USD | 107,380.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1643` | 95,200.00 USD | 95,200.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1644` | 88,310.00 USD | 88,310.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 118.90 USD | 3,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1646` | 25,550.00 USD | 25,550.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1647` | 25,810.00 USD | 25,810.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1649` | 11,770.00 USD | 11,770.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1650` | 32,630.00 USD | 32,630.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1650` | 65,260.00 USD | 65,260.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 75,930.00 USD | 75,930.00 USD | 10,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1655` | 36,620.00 USD | 36,620.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1656` | 89,160.00 USD | 89,160.00 USD | 13,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1658` | 99,170.00 USD | 99,170.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 116,650.00 USD | 116,650.00 USD | 6,180.00 USD | 21,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 213,940.00 USD | 213,940.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1662` | 231,520.00 USD | 231,520.00 USD | 19,160.00 USD | 17,500.00 USD | 78,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 469,560.00 USD | 469,560.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 398,210.00 USD | 398,210.00 USD | 66,370.00 USD | 9,280.00 USD | 91,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 13,460.00 USD | 16,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1667` | 524,810.00 USD | 524,810.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1668` | 444,160.00 USD | 444,160.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 834,700.00 USD | 834,700.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 473,330.00 USD | 473,330.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 879,030.00 USD | 879,030.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1674` | 542,870.00 USD | 542,870.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 21,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 1,100,000.00 USD | 1,100,000.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 582,330.00 USD | 582,330.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 1,250,000.00 USD | 1,250,000.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1680` | 677,550.00 USD | 677,550.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 1,420,000.00 USD | 1,420,000.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 779,990.00 USD | 779,990.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1686` | 903,070.00 USD | 903,070.00 USD | 14,180.00 USD | 51,130.00 USD | 57,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 954,280.00 USD | 954,280.00 USD | 10,830.00 USD | 9,950.00 USD | 30,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 1,590,000.00 USD | 1,590,000.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1692` | 1,180,000.00 USD | 1,180,000.00 USD | 84,920.00 USD | 69,050.00 USD | 75,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 1,710,000.00 USD | 1,710,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,260,000.00 USD | 1,260,000.00 USD | 33,240.00 USD | 26,310.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1698` | 1,410,000.00 USD | 1,410,000.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 1,450,000.00 USD | 1,450,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 1,990,000.00 USD | 1,990,000.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1704` | 1,480,000.00 USD | 1,480,000.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 712.66 USD | 22,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1706` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 1,630,000.00 USD | 1,630,000.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1710` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 1,670,000.00 USD | 1,670,000.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1716` | 1,730,000.00 USD | 1,730,000.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 1,790,000.00 USD | 1,790,000.00 USD | 34,230.00 USD | 20,360.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 2,480,000.00 USD | 2,480,000.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1722` | 1,930,000.00 USD | 1,930,000.00 USD | 67,510.00 USD | 16,860.00 USD | 54,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 2,650,000.00 USD | 2,650,000.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 1,980,000.00 USD | 1,980,000.00 USD | 8,230.00 USD | 3,980.00 USD | 33,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1728` | 1,990,000.00 USD | 1,990,000.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 2,970,000.00 USD | 2,970,000.00 USD | 306,550.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 3,110,000.00 USD | 3,110,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1734` | 2,020,000.00 USD | 2,020,000.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,070,000.00 USD | 2,070,000.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1740` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 1,770.00 USD | 25,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1746` | 2,110,000.00 USD | 2,110,000.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 3,310,000.00 USD | 3,310,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 2,230,000.00 USD | 2,230,000.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1752` | 2,290,000.00 USD | 2,290,000.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 3,810,000.00 USD | 3,810,000.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 2,340,000.00 USD | 2,340,000.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 3,980,000.00 USD | 3,980,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1758` | 2,460,000.00 USD | 2,460,000.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 4,260,000.00 USD | 4,260,000.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 2,630,000.00 USD | 2,630,000.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 4,650,000.00 USD | 4,650,000.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1764` | 2,750,000.00 USD | 2,750,000.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 5,040,000.00 USD | 5,040,000.00 USD | 163,180.00 USD | 190,610.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 2,860,000.00 USD | 2,860,000.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 5,280,000.00 USD | 5,280,000.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1770` | 2,970,000.00 USD | 2,970,000.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 5,500,000.00 USD | 5,500,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,020,000.00 USD | 3,020,000.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 5,690,000.00 USD | 5,690,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 25,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1776` | 3,080,000.00 USD | 3,080,000.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 5,950,000.00 USD | 5,950,000.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 3,200,000.00 USD | 3,200,000.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 6,000,000.00 USD | 6,000,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1782` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 6,230,000.00 USD | 6,230,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 3,310,000.00 USD | 3,310,000.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 25,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1787` | 6,390,000.00 USD | 6,390,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1788` | 3,350,000.00 USD | 3,350,000.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 6,520,000.00 USD | 6,520,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 6,650,000.00 USD | 6,650,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1794` | 3,420,000.00 USD | 3,420,000.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 2,560.00 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1796` | 6,720,000.00 USD | 6,720,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 3,480,000.00 USD | 3,480,000.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1800` | 3,520,000.00 USD | 3,520,000.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 6,900,000.00 USD | 6,900,000.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 3,570,000.00 USD | 3,570,000.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 6,960,000.00 USD | 6,960,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1806` | 3,590,000.00 USD | 3,590,000.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 7,110,000.00 USD | 7,110,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 3,620,000.00 USD | 3,620,000.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 7,210,000.00 USD | 7,210,000.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1812` | 3,690,000.00 USD | 3,690,000.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 7,330,000.00 USD | 7,330,000.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 3,700,000.00 USD | 3,700,000.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 7,420,000.00 USD | 7,420,000.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1818` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 7,560,000.00 USD | 7,560,000.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 13,320.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 7,740,000.00 USD | 7,740,000.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1824` | 3,760,000.00 USD | 3,760,000.00 USD | 7,970.00 USD | 5,910.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 7,910,000.00 USD | 7,910,000.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 3,760,000.00 USD | 3,760,000.00 USD | 5,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 8,010,000.00 USD | 8,010,000.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1830` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 8,180,000.00 USD | 8,180,000.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1833` | 3,770,000.00 USD | 3,770,000.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 8,390,000.00 USD | 8,390,000.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1837` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 8,640,000.00 USD | 8,640,000.00 USD | 83,000.00 USD | 64,170.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 8,800,000.00 USD | 8,800,000.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 8,930,000.00 USD | 8,930,000.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1847` | 8,970,000.00 USD | 8,970,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,220,000.00 USD | 9,220,000.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,440,000.00 USD | 9,440,000.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 9,580,000.00 USD | 9,580,000.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1859` | 9,710,000.00 USD | 9,710,000.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1862` | 9,830,000.00 USD | 9,830,000.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1865` | 9,910,000.00 USD | 9,910,000.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 10,050,000.00 USD | 10,050,000.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1871` | 10,200,000.00 USD | 10,200,000.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1874` | 10,330,000.00 USD | 10,330,000.00 USD | 41,180.00 USD | 43,720.00 USD | 51,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1877` | 10,400,000.00 USD | 10,400,000.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1880` | 10,460,000.00 USD | 10,460,000.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1883` | 10,490,000.00 USD | 10,490,000.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1886` | 10,530,000.00 USD | 10,530,000.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1304` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 4,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1310` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 6,470.00 USD | 4,610.00 USD | 4,440.00 USD |
| `7D` | `0.1313` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 5,580.00 USD | 2,780.00 USD | 12,990.00 USD |
| `7D` | `0.1325` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 0.00 USD | 3,040.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `1D` | `0.1395` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 6,700.00 USD | 6,230.00 USD | 0.00 USD |
| `7D` | `0.1397` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1398` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 12,500.00 USD | 953.16 USD | 1,480.00 USD |
| `7D` | `0.1400` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `1D` | `0.1401` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 9,130.00 USD | 2,100.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1404` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 2,140.00 USD | 1,850.00 USD | 0.00 USD |
| `1D` | `0.1407` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 1,300.00 USD | 0.00 USD |
| `1D` | `0.1410` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 1,570.00 USD | 0.00 USD |
| `1D` | `0.1413` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD |
| `7D` | `0.1418` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `1D` | `0.1419` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 3,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `7D` | `0.1421` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `1D` | `0.1422` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 6,100.00 USD | 3,450.00 USD | 6,410.00 USD |
| `1D` | `0.1425` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 0.00 USD | 2,890.00 USD | 2,500.00 USD |
| `1D` | `0.1428` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 3,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1430` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `0.1433` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 5,270.00 USD |
| `1D` | `0.1434` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 6,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1436` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `1D` | `0.1437` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 23,000.00 USD |
| `7D` | `0.1439` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 23,950.00 USD | 0.00 USD | 3,610.00 USD |
| `1D` | `0.1440` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 22,050.00 USD | 3,590.00 USD | 1,850.00 USD |
| `7D` | `0.1442` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 0.00 USD | 5,260.00 USD | 6,160.00 USD |
| `1D` | `0.1443` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 9,660.00 USD | 0.00 USD |
| `1D` | `0.1446` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 5,160.00 USD | 2,970.00 USD |
| `7D` | `0.1451` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 0.00 USD | 10,680.00 USD | 5,150.00 USD |
| `1D` | `0.1452` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 29,330.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1454` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 0.00 USD | 0.00 USD | 9,030.00 USD |
| `1D` | `0.1455` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1458` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 1,610.00 USD | 5,430.00 USD |
| `1D` | `0.1461` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 0.00 USD | 7,870.00 USD | 1,760.00 USD |
| `1D` | `0.1464` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 13,790.00 USD | 2,690.00 USD | 15,460.00 USD |
| `7D` | `0.1466` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 7,920.00 USD | 8,550.00 USD | 5,670.00 USD |
| `7D` | `0.1469` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1470` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 8,350.00 USD | 6,980.00 USD | 5,200.00 USD |
| `7D` | `0.1472` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 36,510.00 USD | 35,860.00 USD | 75,850.00 USD |
| `7D` | `0.1475` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 24,840.00 USD | 13,040.00 USD | 0.00 USD |
| `1D` | `0.1476` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 72,920.00 USD | 21,710.00 USD | 157,130.00 USD |
| `7D` | `0.1478` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1479` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 122,320.00 USD | 16,510.00 USD | 26,770.00 USD |
| `7D` | `0.1481` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 41,960.00 USD | 31,150.00 USD | 19,470.00 USD |
| `1D` | `0.1482` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 45,240.00 USD | 6,260.00 USD | 125,170.00 USD |
| `7D` | `0.1484` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 12,060.00 USD | 3,040.00 USD | 188,220.00 USD |
| `1D` | `0.1485` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 70,980.00 USD | 0.00 USD | 65,940.00 USD |
| `7D` | `0.1487` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 61,970.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1488` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 16,750.00 USD | 3,580.00 USD | 9,310.00 USD |
| `7D` | `0.1490` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 28,940.00 USD | 9,780.00 USD | 77,920.00 USD |
| `1D` | `0.1491` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 34,570.00 USD | 12,130.00 USD | 14,090.00 USD |
| `7D` | `0.1493` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1494` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 51,430.00 USD | 6,010.00 USD | 7,830.00 USD |
| `7D` | `0.1496` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1497` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 35,160.00 USD | 0.00 USD | 21,040.00 USD |
| `7D` | `0.1499` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1500` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 5,920.00 USD | 9,460.00 USD | 2,340.00 USD |
| `7D` | `0.1502` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1503` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 60,170.00 USD | 15,960.00 USD | 156,980.00 USD |
| `7D` | `0.1505` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1506` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 35,380.00 USD | 3,090.00 USD | 206,820.00 USD |
| `7D` | `0.1508` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1509` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 6,130.00 USD | 154,990.00 USD |
| `7D` | `0.1511` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1512` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 5,040.00 USD | 3,900.00 USD | 2,500.00 USD |
| `7D` | `0.1514` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1515` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 13,740.00 USD | 0.00 USD | 371,840.00 USD |
| `7D` | `0.1517` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1518` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 36,780.00 USD | 8,960.00 USD | 46,010.00 USD |
| `7D` | `0.1520` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1521` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 49,700.00 USD | 9,170.00 USD | 21,240.00 USD |
| `7D` | `0.1523` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1524` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1526` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1527` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1529` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1530` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 29,930.00 USD | 15,770.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1533` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 0.00 USD | 4,910.00 USD | 11,690.00 USD |
| `7D` | `0.1535` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1536` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 14,970.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1538` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1541` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `0.1542` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1544` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `7D` | `0.1547` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1548` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 20,250.00 USD | 12,300.00 USD | 9,340.00 USD |
| `7D` | `0.1550` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1551` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 8,630.00 USD | 16,110.00 USD | 25,420.00 USD |
| `7D` | `0.1553` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1554` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 27,810.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1556` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 7,120.00 USD | 13,350.00 USD | 8,390.00 USD |
| `7D` | `0.1559` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 6,990.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1562` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 23,820.00 USD | 19,080.00 USD | 9,940.00 USD |
| `7D` | `0.1565` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1566` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 90,440.00 USD | 21,070.00 USD | 16,410.00 USD |
| `7D` | `0.1568` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1569` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 13,500.00 USD | 0.00 USD | 114,660.00 USD |
| `7D` | `0.1571` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1572` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 54,580.00 USD | 10,460.00 USD | 64,460.00 USD |
| `7D` | `0.1574` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 64,070.00 USD | 79,780.00 USD | 0.00 USD |
| `1D` | `0.1575` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 9,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1577` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 31,130.00 USD | 112,180.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 5,670.00 USD | 0.00 USD |
| `7D` | `0.1580` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 216,490.00 USD | 41,220.00 USD | 0.00 USD |
| `1D` | `0.1581` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 15,810.00 USD | 4,130.00 USD | 0.00 USD |
| `7D` | `0.1583` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 70,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1584` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 86,410.00 USD | 15,210.00 USD | 6,020.00 USD |
| `7D` | `0.1586` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 44,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1587` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 20,600.00 USD | 40,320.00 USD | 40,370.00 USD |
| `7D` | `0.1589` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 34,830.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 901,250.00 USD | 0.00 USD | 901,250.00 USD | 0.00 USD | 17,180.00 USD | 41,850.00 USD |
| `1D` | `0.1593` | 842,230.00 USD | 0.00 USD | 842,230.00 USD | 0.00 USD | 33,440.00 USD | 23,920.00 USD |
| `7D` | `0.1595` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1596` | 784,870.00 USD | 0.00 USD | 784,870.00 USD | 0.00 USD | 1,210.00 USD | 0.00 USD |
| `7D` | `0.1598` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1599` | 783,660.00 USD | 0.00 USD | 783,660.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `7D` | `0.1601` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1602` | 770,050.00 USD | 0.00 USD | 770,050.00 USD | 44,810.00 USD | 12,460.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 72,300.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1605` | 712,770.00 USD | 0.00 USD | 712,770.00 USD | 0.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1607` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 166,880.00 USD | 0.00 USD | 312,980.00 USD |
| `1D` | `0.1608` | 708,930.00 USD | 0.00 USD | 708,930.00 USD | 34,860.00 USD | 7,790.00 USD | 81,500.00 USD |
| `7D` | `0.1610` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 178,210.00 USD | 0.00 USD | 178,270.00 USD |
| `1D` | `0.1611` | 584,770.00 USD | 0.00 USD | 584,770.00 USD | 13,920.00 USD | 22,870.00 USD | 0.00 USD |
| `7D` | `0.1613` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 321,740.00 USD | 0.00 USD | 381,020.00 USD |
| `1D` | `0.1614` | 547,990.00 USD | 0.00 USD | 547,990.00 USD | 0.00 USD | 38,670.00 USD | 0.00 USD |
| `7D` | `0.1616` | 789,420.00 USD | 0.00 USD | 789,420.00 USD | 187,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1620` | 509,320.00 USD | 0.00 USD | 509,320.00 USD | 0.00 USD | 17,910.00 USD | 0.00 USD |
| `7D` | `0.1622` | 601,830.00 USD | 0.00 USD | 601,830.00 USD | 0.00 USD | 80,360.00 USD | 0.00 USD |
| `1D` | `0.1623` | 491,400.00 USD | 0.00 USD | 491,400.00 USD | 34,770.00 USD | 0.00 USD | 17,520.00 USD |
| `7D` | `0.1625` | 521,470.00 USD | 0.00 USD | 521,470.00 USD | 0.00 USD | 122,430.00 USD | 103,330.00 USD |
| `1D` | `0.1626` | 439,110.00 USD | 0.00 USD | 439,110.00 USD | 63,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1628` | 295,720.00 USD | 0.00 USD | 295,720.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1629` | 375,120.00 USD | 0.00 USD | 375,120.00 USD | 0.00 USD | 3,520.00 USD | 104,120.00 USD |
| `7D` | `0.1631` | 218,940.00 USD | 0.00 USD | 218,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 267,490.00 USD | 0.00 USD | 267,490.00 USD | 122,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 145,190.00 USD | 0.00 USD | 145,190.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `0.1637` | 148,000.00 USD | 0.00 USD | 148,000.00 USD | 0.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `0.1638` | 136,500.00 USD | 0.00 USD | 136,500.00 USD | 14,240.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.1640` | 124,450.00 USD | 0.00 USD | 124,450.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD |
| `1D` | `0.1641` | 107,380.00 USD | 0.00 USD | 107,380.00 USD | 16,140.00 USD | 0.00 USD | 2,920.00 USD |
| `7D` | `0.1643` | 95,200.00 USD | 0.00 USD | 95,200.00 USD | 0.00 USD | 25,110.00 USD | 44,540.00 USD |
| `1D` | `0.1644` | 88,310.00 USD | 0.00 USD | 88,310.00 USD | 33,120.00 USD | 0.00 USD | 29,380.00 USD |
| `7D` | `0.1646` | 25,550.00 USD | 0.00 USD | 25,550.00 USD | 0.00 USD | 13,780.00 USD | 0.00 USD |
| `1D` | `0.1647` | 25,810.00 USD | 0.00 USD | 25,810.00 USD | 17,270.00 USD | 0.00 USD | 8,550.00 USD |
| `7D` | `0.1649` | 11,770.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD | 11,770.00 USD | 0.00 USD |
| `1D` | `0.1650` | 32,630.00 USD | 32,630.00 USD | 0.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD |
| `1D` | `0.1650` | 65,260.00 USD | 65,260.00 USD | 0.00 USD | 22,240.00 USD | 0.00 USD | 10,390.00 USD |
| `7D` | `0.1651` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1653` | 75,930.00 USD | 75,930.00 USD | 0.00 USD | 10,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1655` | 36,620.00 USD | 36,620.00 USD | 0.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD |
| `1D` | `0.1656` | 89,160.00 USD | 89,160.00 USD | 0.00 USD | 13,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1658` | 99,170.00 USD | 99,170.00 USD | 0.00 USD | 10,890.00 USD | 0.00 USD | 51,660.00 USD |
| `1D` | `0.1659` | 116,650.00 USD | 116,650.00 USD | 0.00 USD | 6,180.00 USD | 21,310.00 USD | 0.00 USD |
| `7D` | `0.1661` | 213,940.00 USD | 213,940.00 USD | 0.00 USD | 103,750.00 USD | 11,020.00 USD | 0.00 USD |
| `1D` | `0.1662` | 231,520.00 USD | 231,520.00 USD | 0.00 USD | 19,160.00 USD | 17,500.00 USD | 78,220.00 USD |
| `7D` | `0.1664` | 469,560.00 USD | 469,560.00 USD | 0.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD |
| `1D` | `0.1665` | 398,210.00 USD | 398,210.00 USD | 0.00 USD | 66,370.00 USD | 9,280.00 USD | 91,040.00 USD |
| `7D` | `0.1667` | 524,810.00 USD | 524,810.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1668` | 444,160.00 USD | 444,160.00 USD | 0.00 USD | 0.00 USD | 17,230.00 USD | 28,720.00 USD |
| `7D` | `0.1670` | 834,700.00 USD | 834,700.00 USD | 0.00 USD | 114,710.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 473,330.00 USD | 473,330.00 USD | 0.00 USD | 25,320.00 USD | 3,850.00 USD | 0.00 USD |
| `7D` | `0.1673` | 879,030.00 USD | 879,030.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 0.00 USD |
| `1D` | `0.1674` | 542,870.00 USD | 542,870.00 USD | 0.00 USD | 45,910.00 USD | 3,960.00 USD | 19,670.00 USD |
| `7D` | `0.1676` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 84,020.00 USD | 141,760.00 USD | 0.00 USD |
| `1D` | `0.1677` | 582,330.00 USD | 582,330.00 USD | 0.00 USD | 24,880.00 USD | 13,330.00 USD | 1,250.00 USD |
| `7D` | `0.1679` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 52,340.00 USD | 61,850.00 USD | 35,720.00 USD |
| `1D` | `0.1680` | 677,550.00 USD | 677,550.00 USD | 0.00 USD | 72,910.00 USD | 15,160.00 USD | 7,150.00 USD |
| `7D` | `0.1682` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 130,480.00 USD | 18,420.00 USD | 15,310.00 USD |
| `1D` | `0.1683` | 779,990.00 USD | 779,990.00 USD | 0.00 USD | 69,620.00 USD | 8,890.00 USD | 23,930.00 USD |
| `7D` | `0.1685` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 14,000.00 USD | 0.00 USD |
| `1D` | `0.1686` | 903,070.00 USD | 903,070.00 USD | 0.00 USD | 14,180.00 USD | 51,130.00 USD | 57,760.00 USD |
| `7D` | `0.1688` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 954,280.00 USD | 954,280.00 USD | 0.00 USD | 10,830.00 USD | 9,950.00 USD | 30,440.00 USD |
| `7D` | `0.1691` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 71,020.00 USD |
| `1D` | `0.1692` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 84,920.00 USD | 69,050.00 USD | 75,140.00 USD |
| `7D` | `0.1694` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1695` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 33,240.00 USD | 26,310.00 USD | 19,580.00 USD |
| `7D` | `0.1697` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1698` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 37,080.00 USD | 59,440.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1701` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `7D` | `0.1703` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 55,170.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1704` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 3,540.00 USD | 14,420.00 USD | 10,240.00 USD |
| `7D` | `0.1706` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `1D` | `0.1707` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 63,640.00 USD | 72,810.00 USD | 15,460.00 USD |
| `7D` | `0.1709` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 25,490.00 USD | 64,690.00 USD |
| `1D` | `0.1710` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 5,670.00 USD | 8,040.00 USD |
| `1D` | `0.1713` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 9,130.00 USD | 21,450.00 USD | 0.00 USD |
| `7D` | `0.1715` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 42,020.00 USD | 0.00 USD |
| `1D` | `0.1716` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 11,710.00 USD | 27,460.00 USD | 16,070.00 USD |
| `7D` | `0.1718` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,160.00 USD |
| `1D` | `0.1719` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 34,230.00 USD | 20,360.00 USD | 8,520.00 USD |
| `7D` | `0.1721` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 44,020.00 USD | 0.00 USD | 266,220.00 USD |
| `1D` | `0.1722` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 67,510.00 USD | 16,860.00 USD | 54,110.00 USD |
| `7D` | `0.1724` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 104,030.00 USD |
| `1D` | `0.1725` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 8,230.00 USD | 3,980.00 USD | 33,410.00 USD |
| `1D` | `0.1728` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1730` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 306,550.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1733` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1734` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 11,230.00 USD |
| `1D` | `0.1737` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 32,880.00 USD | 11,810.00 USD | 6,410.00 USD |
| `7D` | `0.1739` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1740` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 5,630.00 USD | 5,180.00 USD |
| `1D` | `0.1743` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1745` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 9,500.00 USD |
| `7D` | `0.1748` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 39,700.00 USD |
| `7D` | `0.1751` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 226,130.00 USD |
| `1D` | `0.1752` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 30,470.00 USD |
| `7D` | `0.1754` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 229,230.00 USD |
| `1D` | `0.1755` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 23,280.00 USD |
| `7D` | `0.1757` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1758` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 44,240.00 USD | 17,800.00 USD | 54,670.00 USD |
| `7D` | `0.1760` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 224,680.00 USD | 25,210.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 54,120.00 USD | 73,590.00 USD | 46,830.00 USD |
| `7D` | `0.1763` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 240,020.00 USD | 139,590.00 USD | 12,330.00 USD |
| `1D` | `0.1764` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 25,580.00 USD | 27,980.00 USD | 64,450.00 USD |
| `7D` | `0.1766` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 163,180.00 USD | 190,610.00 USD | 36,540.00 USD |
| `1D` | `0.1767` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 27,430.00 USD | 44,580.00 USD | 39,450.00 USD |
| `7D` | `0.1769` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 113,280.00 USD | 105,160.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 32,300.00 USD | 40,690.00 USD | 32,820.00 USD |
| `7D` | `0.1772` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 10,620.00 USD | 23,730.00 USD | 21,240.00 USD |
| `7D` | `0.1775` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 28,740.00 USD | 12,480.00 USD | 14,440.00 USD |
| `7D` | `0.1778` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 123,700.00 USD |
| `1D` | `0.1779` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 26,670.00 USD | 70,980.00 USD | 18,790.00 USD |
| `7D` | `0.1781` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1782` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 11,740.00 USD | 16,650.00 USD |
| `7D` | `0.1784` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 40,030.00 USD | 32,920.00 USD | 8,780.00 USD |
| `7D` | `0.1787` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 13,920.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1790` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1791` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,880.00 USD |
| `7D` | `0.1793` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1794` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 21,280.00 USD | 39,270.00 USD | 8,060.00 USD |
| `7D` | `0.1796` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1797` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 22,870.00 USD | 10,360.00 USD | 22,300.00 USD |
| `7D` | `0.1799` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1800` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 5,820.00 USD | 10,730.00 USD | 22,650.00 USD |
| `7D` | `0.1802` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 23,530.00 USD |
| `1D` | `0.1803` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 7,340.00 USD | 29,410.00 USD | 10,840.00 USD |
| `7D` | `0.1805` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1806` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 9,910.00 USD | 5,710.00 USD | 11,030.00 USD |
| `7D` | `0.1808` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 8,870.00 USD | 16,960.00 USD | 1,080.00 USD |
| `7D` | `0.1811` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 13,200.00 USD |
| `1D` | `0.1812` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 18,980.00 USD | 36,890.00 USD | 9,500.00 USD |
| `7D` | `0.1814` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 60,000.00 USD |
| `1D` | `0.1815` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 7,310.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `0.1817` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 20,080.00 USD |
| `1D` | `0.1818` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 5,350.00 USD |
| `7D` | `0.1820` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 42,210.00 USD | 54,880.00 USD | 38,610.00 USD |
| `1D` | `0.1821` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 13,320.00 USD | 6,430.00 USD |
| `7D` | `0.1823` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 62,540.00 USD | 13,300.00 USD | 105,730.00 USD |
| `1D` | `0.1824` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 7,970.00 USD | 5,910.00 USD | 3,960.00 USD |
| `7D` | `0.1826` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 90,200.00 USD | 9,890.00 USD | 66,950.00 USD |
| `1D` | `0.1827` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 5,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1829` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 20,880.00 USD | 28,120.00 USD | 51,250.00 USD |
| `1D` | `0.1830` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,420.00 USD |
| `7D` | `0.1832` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 94,870.00 USD | 27,790.00 USD | 50,530.00 USD |
| `1D` | `0.1833` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 2,670.00 USD | 716.83 USD | 0.00 USD |
| `7D` | `0.1835` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 111,430.00 USD | 46,260.00 USD | 52,650.00 USD |
| `1D` | `0.1837` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD |
| `7D` | `0.1838` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 83,000.00 USD | 64,170.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 56,160.00 USD | 57,660.00 USD | 45,300.00 USD |
| `7D` | `0.1844` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 48,920.00 USD | 3,900.00 USD | 72,920.00 USD |
| `7D` | `0.1847` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 77,110.00 USD | 77,020.00 USD | 103,160.00 USD |
| `7D` | `0.1853` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 62,090.00 USD | 9,590.00 USD | 146,560.00 USD |
| `7D` | `0.1856` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 31,410.00 USD | 21,030.00 USD | 87,320.00 USD |
| `7D` | `0.1859` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 47,740.00 USD | 6,920.00 USD | 77,460.00 USD |
| `7D` | `0.1862` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 60,020.00 USD | 13,950.00 USD | 37,650.00 USD |
| `7D` | `0.1865` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 22,320.00 USD | 18,650.00 USD | 40,190.00 USD |
| `7D` | `0.1868` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 88,110.00 USD | 31,750.00 USD | 24,730.00 USD |
| `7D` | `0.1871` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 83,830.00 USD | 27,560.00 USD | 34,980.00 USD |
| `7D` | `0.1874` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 41,180.00 USD | 43,720.00 USD | 51,010.00 USD |
| `7D` | `0.1877` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 27,840.00 USD | 22,370.00 USD | 17,920.00 USD |
| `7D` | `0.1880` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 36,800.00 USD | 14,700.00 USD | 8,130.00 USD |
| `7D` | `0.1883` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 14,000.00 USD | 3,530.00 USD | 9,740.00 USD |
| `7D` | `0.1886` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 9,250.00 USD | 31,900.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `189.57M` | Total OI Tokens: `1,146,219,618.1 ARB`
  * 1h OI Change: `+2.77%` | 4h OI Change: `+6.36%` | 24h OI Change: `-15.30%`
  * Exchange Breakdown: Binance=`42.95M` | Bybit=`26.71M` | OKX=`14.70M` | Hyperliquid=`13.34M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.09K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0042%` | **USDT OKX** | `0.0017%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0014%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `-0.0097%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `57.69%` | `42.31%` | `1.36` | 1,660,000.00 USD |
| `15M` | `Binance` | `53.95%` | `46.05%` | `1.17` | 590,720.00 USD |
| `15M` | `OKX` | `60.32%` | `39.68%` | `1.52` | 205,710.00 USD |
| `15M` | `Bybit` | `72.3%` | `27.7%` | `2.61` | 285,160.00 USD |
| `15M` | `KuCoin` | `51.56%` | `48.44%` | `1.06` | 97,520.00 USD |
| `15M` | `Gate` | `17.31%` | `82.69%` | `0.21` | 30,020.00 USD |
| `15M` | `Bitget` | `76.14%` | `23.86%` | `3.19` | 32,220.00 USD |
| `15M` | `BingX` | `53.7%` | `46.3%` | `1.16` | 52,550.00 USD |
| `15M` | `MEXC` | `53.19%` | `46.81%` | `1.14` | 46,950.00 USD |
| `15M` | `Bitunix` | `51.66%` | `48.34%` | `1.07` | 13,130.00 USD |
| `15M` | `Hyperliquid` | `72.67%` | `27.33%` | `2.66` | 9,110.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.45%` | `44.55%` | `1.24` | 275,570.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.31 USD |
| `15M` | `WhiteBIT` | `43.85%` | `56.15%` | `0.78` | 20,200.00 USD |
| `15M` | `HTX` | `1.07%` | `98.93%` | `0.01` | 195.76 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 95.38 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `55.69%` | `44.31%` | `1.26` | 3,660.00 USD |
| `15M` | `Whale Positions` | `53.95%` | `46.05%` | `1.17` | 590,720.00 USD |
| `15M` | `Global Accounts` | `57.69%` | `42.31%` | `1.36` | 1,660,000.00 USD |
| `1H` | `ARB` | `51.67%` | `48.33%` | `1.07` | 5,460,000.00 USD |
| `1H` | `Binance` | `59.47%` | `40.53%` | `1.47` | 1,900,000.00 USD |
| `1H` | `OKX` | `53.38%` | `46.62%` | `1.15` | 626,080.00 USD |
| `1H` | `Bybit` | `61.72%` | `38.28%` | `1.61` | 572,310.00 USD |
| `1H` | `KuCoin` | `50.31%` | `49.69%` | `1.01` | 270,010.00 USD |
| `1H` | `Gate` | `24.97%` | `75.03%` | `0.33` | 48,430.00 USD |
| `1H` | `Bitget` | `66.29%` | `33.71%` | `1.97` | 71,030.00 USD |
| `1H` | `BingX` | `14.86%` | `85.14%` | `0.17` | 592,240.00 USD |
| `1H` | `MEXC` | `36.1%` | `63.9%` | `0.56` | 199,730.00 USD |
| `1H` | `Bitunix` | `76.97%` | `23.03%` | `3.34` | 91,740.00 USD |
| `1H` | `Hyperliquid` | `87.81%` | `12.19%` | `7.20` | 42,730.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.42%` | `50.58%` | `0.98` | 963,020.00 USD |
| `1H` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.30 USD |
| `1H` | `WhiteBIT` | `76.97%` | `23.03%` | `3.34` | 52,980.00 USD |
| `1H` | `HTX` | `41.6%` | `58.4%` | `0.71` | 1,030.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `100%` | `0%` | `1.00` | 116.75 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `73.99%` | `26.01%` | `2.84` | 40,160.00 USD |
| `1H` | `Whale Positions` | `59.47%` | `40.53%` | `1.47` | 1,900,000.00 USD |
| `1H` | `Global Accounts` | `51.67%` | `48.33%` | `1.07` | 5,460,000.00 USD |
| `4H` | `ARB` | `48.81%` | `51.19%` | `0.95` | 89,330,000.00 USD |
| `4H` | `Binance` | `50.05%` | `49.95%` | `1.00` | 32,670,000.00 USD |
| `4H` | `OKX` | `51.62%` | `48.38%` | `1.07` | 20,940,000.00 USD |
| `4H` | `Bybit` | `51.7%` | `48.3%` | `1.07` | 7,270,000.00 USD |
| `4H` | `KuCoin` | `50.94%` | `49.06%` | `1.04` | 2,620,000.00 USD |
| `4H` | `Gate` | `48.21%` | `51.79%` | `0.93` | 1,970,000.00 USD |
| `4H` | `Bitget` | `53.19%` | `46.81%` | `1.14` | 2,340,000.00 USD |
| `4H` | `BingX` | `21.59%` | `78.41%` | `0.28` | 2,880,000.00 USD |
| `4H` | `MEXC` | `57.32%` | `42.68%` | `1.34` | 1,130,000.00 USD |
| `4H` | `Bitunix` | `48.35%` | `51.65%` | `0.94` | 2,830,000.00 USD |
| `4H` | `Hyperliquid` | `39.58%` | `60.42%` | `0.66` | 714,920.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.49%` | `51.51%` | `0.94` | 12,150,000.00 USD |
| `4H` | `Crypto.com` | `79.26%` | `20.74%` | `3.82` | 1,410.00 USD |
| `4H` | `WhiteBIT` | `9%` | `91%` | `0.10` | 1,450,000.00 USD |
| `4H` | `HTX` | `42.12%` | `57.88%` | `0.73` | 74,280.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.37%` | `24.63%` | `3.06` | 143,190.00 USD |
| `4H` | `Aster` | `45.95%` | `54.05%` | `0.85` | 103,100.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.22%` | `50.78%` | `0.97` | 50,360.00 USD |
| `4H` | `Whale Positions` | `50.05%` | `49.95%` | `1.00` | 32,670,000.00 USD |
| `4H` | `Global Accounts` | `48.81%` | `51.19%` | `0.95` | 89,330,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1567` | `0.1555` | 659,096.24 USD | 362,345.04 USD | 296,751.20 USD | 65,593.84 USD | `+9.95%` | `17B / 13S` |
| `5:00 UTC` | `0.1568` | `0.1562` | `0.1568` | `0.1570` | `0.1554` | 510,482.89 USD | 331,670.18 USD | 178,812.71 USD | 152,857.47 USD | `+29.94%` | `56B / 25S` |
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1581` | `0.1581` | `0.1581` | `0.1585` | `0.1579` | 820,818.50 USD | 467,570.37 USD | 353,248.12 USD | 114,322.25 USD | `+13.93%` | `9B / 5S` |
| `0:00 UTC` | `0.1580` | `0.1582` | `0.1580` | `0.1590` | `0.1577` | 855,410.94 USD | 513,960.14 USD | 341,450.80 USD | 172,509.34 USD | `+20.17%` | `35B / 24S` |
| `5:00 UTC` | `0.1601` | `0.1598` | `0.1601` | `0.1608` | `0.1587` | 1,430,991.81 USD | 878,187.62 USD | 552,804.19 USD | 325,383.42 USD | `+22.74%` | `24B / 14S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1625` | `0.1603` | 1,684,179.28 USD | 761,022.88 USD | 923,156.41 USD | -162,133.53 USD | `-9.63%` | `12B / 13S` |
| `5:00 UTC` | `0.1637` | `0.1631` | `0.1637` | `0.1639` | `0.1618` | 1,849,966.09 USD | 605,282.83 USD | 1,244,683.26 USD | -639,400.43 USD | `-34.56%` | `9B / 30S` |
| `0:00 UTC` | `0.1655` | `0.1648` | `0.1655` | `0.1660` | `0.1635` | 1,718,232.82 USD | 746,856.42 USD | 971,376.40 USD | -224,519.98 USD | `-13.07%` | `15B / 23S` |
| `5:00 UTC` | `0.1654` | `0.1653` | `0.1654` | `0.1656` | `0.1649` | 354,251.21 USD | 114,812.73 USD | 239,438.48 USD | -124,625.75 USD | `-35.18%` | `5B / 26S` |

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
| `5m` | -33,960.00 USD | -247,750.00 USD | **`DISTRIBUTION`** |
| `15m` | 276.85 USD | -812,460.00 USD | **`DISTRIBUTION`** |
| `30m` | 30,790.00 USD | -2,000,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 136,030.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -92,370.00 USD | -963,180.00 USD | **`DISTRIBUTION`** |
| `4h` | -22,260.00 USD | 17,610.00 USD | **`DISTRIBUTION`** |
| `6h` | -323,240.00 USD | -459,830.00 USD | **`DISTRIBUTION`** |
| `8h` | 54,910.00 USD | -5,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,930,000.00 USD | -5,650,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,060,000.00 USD | -10,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,500,000.00 USD | -37,410,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,650,000.00 USD | -163,400,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-33.96K` | 15m=`+276.85` | 1h=`+136.03K` | 24h=`-2.06M`
* Futures Capital Netflows: 5m=`-247.75K` | 15m=`-812.46K` | 1h=`-1.42M` | 24h=`-10.37M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
