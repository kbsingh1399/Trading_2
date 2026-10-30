# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1535` | `0.1537` | `0.1526` | `0.1537` | `1,550,175` | 237,307.45 USD | 30,428.47 USD | `+12.82%` | -7,748,975.66 USD | `+0.31` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1537` | `0.1537` | `0.1524` | `0.1525` | `1,548,379` | 236,506.73 USD | 15,408.15 USD | `+6.51%` | -7,733,567.51 USD | `+0.28` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1525` | `0.1530` | `0.1524` | `0.1527` | `647,598` | 98,919.21 USD | -6,200.69 USD | `-6.27%` | -7,739,768.19 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1545` | `0.1546` | `0.1528` | `0.1534` | `8,160,997` | 1,252,838.62 USD | -246,321.42 USD | `-19.66%` | -7,615,881.66 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.1534` | `0.1545` | `0.1520` | `0.1535` | `9,432,942` | 1,447,365.29 USD | -163,522.47 USD | `-11.30%` | -7,779,404.13 USD | `-0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1535` | `0.1537` | `0.1524` | `0.1527` | `3,745,694` | 572,663.54 USD | 39,702.80 USD | `+6.93%` | -7,739,701.32 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1544` | `0.1559` | `0.1527` | `0.1542` | `37,030,008` | 5,719,656.09 USD | 161,930.05 USD | `+2.83%` | -6,603,839.78 USD | `+0.54` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1542` | `0.1555` | `0.1471` | `0.1555` | `122,723,994` | 18,580,533.07 USD | -801,003.43 USD | `-4.31%` | -7,404,843.21 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1555` | `0.1558` | `0.1520` | `0.1527` | `30,742,069` | 4,722,730.62 USD | -334,924.98 USD | `-7.09%` | -7,739,768.19 USD | `+0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1558` | `0.1471` | `0.1526` | `153,429,193` | 23,297,631.63 USD | -1,135,325.45 USD | `-4.87%` | -8,635,459.50 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,340,323.74 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,578,452.08 USD | `-1.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1558` | `0.1471` | `0.1526` | `153,429,193` | 23,297,631.63 USD | -1,135,325.45 USD | `-4.87%` | -8,635,459.50 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

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
| `Live` | `Long Liquidation` | `0.0365` | 515.81 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,880.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 562.95 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 397.83 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 970.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 269.69 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 176.68 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 194,570.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 11,100.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 1,660.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 2,080.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 743.33 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,190.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 1,720.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 7,110.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 143.87 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 10,150.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,260.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 331.44 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 70,470.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 14,050.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 1,050.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 1,890.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 190.02 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 514.04 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 4,780.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 17,040.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 7,550.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 14,330.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 535.45 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 9,870.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 2,960.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 11,640.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 1,850.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 1,700.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 23,980.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 1,090.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,490.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 129,250.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 774.43 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,360.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 707.42 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 2,520.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 10,050.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 1,270.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 5,420.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 27,460.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 8,570.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 18,510.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 35,660.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,060.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 4,850.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 3,860.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,710.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,780.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 4,010.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 3,670.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 13,480.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 50,870.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,280,000.00 USD | 3,280,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,250,000.00 USD | 3,250,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 3,200,000.00 USD | 3,200,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 583.12 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1348` | 3,170,000.00 USD | 3,170,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 3,110,000.00 USD | 3,110,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,920.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 3,070,000.00 USD | 3,070,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 3,030,000.00 USD | 3,030,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,990,000.00 USD | 2,990,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 16,680.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,970,000.00 USD | 2,970,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1370` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,950,000.00 USD | 2,950,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1373` | 2,710,000.00 USD | 2,710,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,750.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1376` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1379` | 2,700,000.00 USD | 2,700,000.00 USD | 2,250.00 USD | 821.64 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,950,000.00 USD | 2,950,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1382` | 2,690,000.00 USD | 2,690,000.00 USD | 10,310.00 USD | 9,440.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,930,000.00 USD | 2,930,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1385` | 2,640,000.00 USD | 2,640,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 8,610.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1388` | 2,560,000.00 USD | 2,560,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,890,000.00 USD | 2,890,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 2,540,000.00 USD | 2,540,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 6,340.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1397` | 2,450,000.00 USD | 2,450,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,780,000.00 USD | 2,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,760,000.00 USD | 2,760,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 885.87 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1412` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 5,130.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 2,430,000.00 USD | 2,430,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 524,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 2,420,000.00 USD | 2,420,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 53,570.00 USD | 482,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,730,000.00 USD | 2,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 2,390,000.00 USD | 2,390,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,690,000.00 USD | 2,690,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,670,000.00 USD | 2,670,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 16,220.00 USD | 428,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1451` | 2,370,000.00 USD | 2,370,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,950.00 USD | 412,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 38,590.00 USD | 319,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,630,000.00 USD | 2,630,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 2,360,000.00 USD | 2,360,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 2,340,000.00 USD | 2,340,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,610,000.00 USD | 2,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 2,250,000.00 USD | 2,250,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 98,050.00 USD | 280,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1476` | 2,580,000.00 USD | 2,580,000.00 USD | 68,180.00 USD | 20,180.00 USD | 81,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1478` | 2,210,000.00 USD | 2,210,000.00 USD | 129,340.00 USD | 11,890.00 USD | 136,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 2,410,000.00 USD | 2,410,000.00 USD | 74,500.00 USD | 43,810.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 1,930,000.00 USD | 1,930,000.00 USD | 60,660.00 USD | 14,570.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1484` | 1,850,000.00 USD | 1,850,000.00 USD | 45,680.00 USD | 4,230.00 USD | 185,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 2,240,000.00 USD | 2,240,000.00 USD | 47,020.00 USD | 16,640.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 9,200.00 USD | 182,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 1,610,000.00 USD | 1,610,000.00 USD | 8,170.00 USD | 4,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1488` | 1,970,000.00 USD | 1,970,000.00 USD | 73,140.00 USD | 10,470.00 USD | 25,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1490` | 1,590,000.00 USD | 1,590,000.00 USD | 38,650.00 USD | 9,450.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 1,860,000.00 USD | 1,860,000.00 USD | 40,320.00 USD | 21,590.00 USD | 92,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 1,540,000.00 USD | 1,540,000.00 USD | 14,230.00 USD | 3,520.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 7,770.00 USD | 173,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1496` | 1,510,000.00 USD | 1,510,000.00 USD | 14,390.00 USD | 5,270.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1496` | 1,710,000.00 USD | 1,710,000.00 USD | 34,650.00 USD | 18,690.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 1,490,000.00 USD | 1,490,000.00 USD | 2,670.00 USD | 0.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1500` | 1,640,000.00 USD | 1,640,000.00 USD | 60,500.00 USD | 9,610.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1502` | 1,480,000.00 USD | 1,480,000.00 USD | 3,610.00 USD | 13,270.00 USD | 130,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 1,550,000.00 USD | 1,550,000.00 USD | 20,410.00 USD | 19,520.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 1,340,000.00 USD | 1,340,000.00 USD | 54,760.00 USD | 23,120.00 USD | 7,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1505` | 159,210.00 USD | 165,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1508` | 1,250,000.00 USD | 1,250,000.00 USD | 200,020.00 USD | 16,950.00 USD | 259,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 1,460,000.00 USD | 1,460,000.00 USD | 200,530.00 USD | 16,820.00 USD | 256,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 774,760.00 USD | 774,760.00 USD | 122,160.00 USD | 4,360.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1512` | 988,210.00 USD | 988,210.00 USD | 86,820.00 USD | 13,310.00 USD | 59,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1514` | 645,740.00 USD | 645,740.00 USD | 25,970.00 USD | 1,730.00 USD | 232,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 6,540.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,470,000.00 USD | 3,470,000.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,440,000.00 USD | 4,440,000.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 37,090.00 USD | 11,530.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1615` | 4,950.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1616` | 2,070,000.00 USD | 2,070,000.00 USD | 17,630.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 5,030,000.00 USD | 5,030,000.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 2,200,000.00 USD | 2,200,000.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1622` | 2,330,000.00 USD | 2,330,000.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 2,440,000.00 USD | 2,440,000.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 3,720.00 USD | 8,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1628` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,600,000.00 USD | 5,600,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1631` | 2,650,000.00 USD | 2,650,000.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 2,680,000.00 USD | 2,680,000.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 7,430.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 7,000.00 USD | 23,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1646` | 2,800,000.00 USD | 2,800,000.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1648` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 7,370.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1656` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 31,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1658` | 2,870,000.00 USD | 2,870,000.00 USD | 9,730.00 USD | 47,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 5,860,000.00 USD | 5,860,000.00 USD | 79,170.00 USD | 11,020.00 USD | 51,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 2,940,000.00 USD | 2,940,000.00 USD | 8,220.00 USD | 11,150.00 USD | 50,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1664` | 3,100,000.00 USD | 3,100,000.00 USD | 66,370.00 USD | 14,550.00 USD | 80,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 6,110,000.00 USD | 6,110,000.00 USD | 104,470.00 USD | 71,120.00 USD | 80,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1665` | 6,270.00 USD | 29,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1667` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 5,340.00 USD | 41,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1668` | 6,300,000.00 USD | 6,300,000.00 USD | 42,580.00 USD | 52,290.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 6,490,000.00 USD | 6,490,000.00 USD | 135,250.00 USD | 62,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 3,240,000.00 USD | 3,240,000.00 USD | 66,630.00 USD | 2,010.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 508.23 USD | 29,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1676` | 3,260,000.00 USD | 3,260,000.00 USD | 22,100.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1676` | 6,720,000.00 USD | 6,720,000.00 USD | 84,020.00 USD | 141,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 3,270,000.00 USD | 3,270,000.00 USD | 6,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1680` | 6,940,000.00 USD | 6,940,000.00 USD | 121,860.00 USD | 80,270.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1682` | 3,450,000.00 USD | 3,450,000.00 USD | 154,780.00 USD | 4,560.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 7,010,000.00 USD | 7,010,000.00 USD | 60,960.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 3,510,000.00 USD | 3,510,000.00 USD | 20,370.00 USD | 29,790.00 USD | 13,450.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.1705` | 110.74 USD | 30,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1706` | 4,110,000.00 USD | 4,110,000.00 USD | 38,860.00 USD | 9,590.00 USD | 13,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 25,490.00 USD | 87,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 4,200,000.00 USD | 4,200,000.00 USD | 21,630.00 USD | 62,270.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1712` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 15,040.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 4,270,000.00 USD | 4,270,000.00 USD | 9,570.00 USD | 27,880.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 4,300,000.00 USD | 4,300,000.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 8,220,000.00 USD | 8,220,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 2,410.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1730` | 4,550,000.00 USD | 4,550,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 8,710,000.00 USD | 8,710,000.00 USD | 476,430.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 4,570,000.00 USD | 4,570,000.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 2,970.00 USD | 32,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1736` | 4,590,000.00 USD | 4,590,000.00 USD | 14,970.00 USD | 9,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 4,620,000.00 USD | 4,620,000.00 USD | 18,610.00 USD | 2,310.00 USD | 12,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1740` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 83,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1742` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 1,600.00 USD | 11,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 8,810,000.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 4,660,000.00 USD | 4,660,000.00 USD | 8,530.00 USD | 2,460.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1745` | 758.99 USD | 33,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1765` | 748.62 USD | 34,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1766` | 5,430,000.00 USD | 5,430,000.00 USD | 15,830.00 USD | 20,220.00 USD | 62,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 10,850,000.00 USD | 10,850,000.00 USD | 191,690.00 USD | 147,360.00 USD | 31,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 5,600,000.00 USD | 5,600,000.00 USD | 40,920.00 USD | 78,870.00 USD | 44,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1772` | 5,620,000.00 USD | 5,620,000.00 USD | 22,380.00 USD | 5,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 11,120,000.00 USD | 11,120,000.00 USD | 98,390.00 USD | 153,480.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1776` | 11,370,000.00 USD | 11,370,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,620,000.00 USD | 11,620,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,850,000.00 USD | 11,850,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 34,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1788` | 12,020,000.00 USD | 12,020,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 12,250,000.00 USD | 12,250,000.00 USD | 182,810.00 USD | 46,960.00 USD | 3,940.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.1845` | 777.21 USD | 35,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1848` | 14,820,000.00 USD | 14,820,000.00 USD | 35,280.00 USD | 69,910.00 USD | 41,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1852` | 15,270,000.00 USD | 15,270,000.00 USD | 168,270.00 USD | 28,290.00 USD | 251,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1856` | 15,510,000.00 USD | 15,510,000.00 USD | 100,160.00 USD | 21,030.00 USD | 120,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1860` | 15,750,000.00 USD | 15,750,000.00 USD | 64,600.00 USD | 48,330.00 USD | 127,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1864` | 15,910,000.00 USD | 15,910,000.00 USD | 48,260.00 USD | 44,140.00 USD | 61,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1868` | 16,140,000.00 USD | 16,140,000.00 USD | 133,990.00 USD | 38,100.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1872` | 16,410,000.00 USD | 16,410,000.00 USD | 138,560.00 USD | 67,770.00 USD | 68,190.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.1915` | 4,590.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1916` | 17,140,000.00 USD | 17,140,000.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,170,000.00 USD | 17,170,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,190,000.00 USD | 17,190,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,190,000.00 USD | 17,190,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 40,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,210,000.00 USD | 17,210,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,220,000.00 USD | 17,220,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,240,000.00 USD | 17,240,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 1,710.00 USD | 42,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 53,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 198.08 USD | 54,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 54,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 69,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 111,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 25,880.00 USD | 137,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 224,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 229.15 USD | 225,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 225,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 25,700.00 USD | 251,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 36,260.00 USD | 287,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 303,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 303,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2385` | 47,700.00 USD | 351,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 361.66 USD | 351,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 352,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 352,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 352,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 356,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 385,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 438,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 438,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 438,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,510.00 USD | 452,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 452,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 27,890.00 USD | 480,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2755` | 313,200.00 USD | 793,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 794,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2815` | 2,530.00 USD | 796,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 253.85 USD | 796,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 797,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 464.84 USD | 797,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 1,040.00 USD | 798,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 2,280.00 USD | 800,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0355` | 1,810,000.00 USD | 0.00 USD | 4,280.00 USD | `-77.16%` | `120,460,900,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,810,000.00 USD | 0.00 USD | 1,490.00 USD | `-75.23%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,810,000.00 USD | 0.00 USD | 3,760.00 USD | `-73.30%` | `90,632,000,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,800,000.00 USD | 0.00 USD | 278.62 USD | `-72.65%` | `6,555,800,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,800,000.00 USD | 0.00 USD | 529.67 USD | `-68.79%` | `10,921,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,800,000.00 USD | 0.00 USD | 109.52 USD | `-68.15%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,800,000.00 USD | 0.00 USD | 289.43 USD | `-66.22%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,800,000.00 USD | 0.00 USD | 1,430.00 USD | `-65.58%` | `26,643,700,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,800,000.00 USD | 0.00 USD | 2,270.00 USD | `-64.93%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0555` | 1,800,000.00 USD | 0.00 USD | 195,160.00 USD | `-64.29%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,600,000.00 USD | 0.00 USD | 15,650.00 USD | `-63.65%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,590,000.00 USD | 0.00 USD | 203.46 USD | `-62.36%` | `3,477,900,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,590,000.00 USD | 0.00 USD | 719.53 USD | `-61.72%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,590,000.00 USD | 0.00 USD | 1,120.00 USD | `-61.07%` | `18,534,500,000,000.00` |
| `Live` | `Long` | `0.0615` | 1,590,000.00 USD | 0.00 USD | 6,150.00 USD | `-60.43%` | `100,000,000,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,580,000.00 USD | 0.00 USD | 1,170.00 USD | `-59.79%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,580,000.00 USD | 0.00 USD | 595.64 USD | `-57.21%` | `8,957,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 99,790.00 USD | `-56.57%` | `1,478,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,480,000.00 USD | 0.00 USD | 313.22 USD | `-55.93%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,480,000.00 USD | 0.00 USD | 4,300.00 USD | `-55.28%` | `61,891,800,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,470,000.00 USD | 0.00 USD | 5,390.00 USD | `-54.64%` | `76,392,300,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,470,000.00 USD | 0.00 USD | 5,840.00 USD | `-54.00%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,460,000.00 USD | 0.00 USD | 4,820.00 USD | `-53.35%` | `66,539,100,000,000.01` |
| `Live` | `Long` | `0.0735` | 1,460,000.00 USD | 0.00 USD | 7,420.00 USD | `-52.71%` | `100,991,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,450,000.00 USD | 0.00 USD | 226.17 USD | `-52.07%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,450,000.00 USD | 0.00 USD | 15,140.00 USD | `-50.78%` | `197,916,400,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,440,000.00 USD | 0.00 USD | 8,340.00 USD | `-49.49%` | `106,220,900,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,430,000.00 USD | 0.00 USD | 4,630.00 USD | `-48.85%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,420,000.00 USD | 0.00 USD | 13,940.00 USD | `-46.92%` | `168,979,700,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,410,000.00 USD | 0.00 USD | 112.78 USD | `-46.27%` | `1,350,600,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,410,000.00 USD | 0.00 USD | 883.64 USD | `-45.63%` | `10,457,300,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,410,000.00 USD | 0.00 USD | 1,990.00 USD | `-44.99%` | `23,219,100,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,410,000.00 USD | 0.00 USD | 19,460.00 USD | `-44.34%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,390,000.00 USD | 0.00 USD | 73,680.00 USD | `-43.70%` | `842,071,000,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,310,000.00 USD | 0.00 USD | 514.04 USD | `-43.06%` | `5,808,400,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,310,000.00 USD | 0.00 USD | 113.80 USD | `-41.13%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,310,000.00 USD | 0.00 USD | 2,220.00 USD | `-40.48%` | `24,033,900,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,310,000.00 USD | 0.00 USD | 814.24 USD | `-39.84%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,310,000.00 USD | 0.00 USD | 1,760.00 USD | `-39.20%` | `18,595,300,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,310,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.91%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,310,000.00 USD | 0.00 USD | 9,310.00 USD | `-37.27%` | `95,522,700,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,300,000.00 USD | 0.00 USD | 2,810.00 USD | `-36.62%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,290,000.00 USD | 0.00 USD | 7,670.00 USD | `-35.98%` | `77,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,290,000.00 USD | 0.00 USD | 3,260.00 USD | `-35.34%` | `32,393,300,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,280,000.00 USD | 0.00 USD | 14,220.00 USD | `-34.05%` | `138,768,400,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,270,000.00 USD | 0.00 USD | 1,580.00 USD | `-33.41%` | `15,220,000,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,270,000.00 USD | 0.00 USD | 6,230.00 USD | `-32.76%` | `59,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,260,000.00 USD | 0.00 USD | 14,270.00 USD | `-32.12%` | `135,244,600,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,250,000.00 USD | 0.00 USD | 4,210.00 USD | `-31.48%` | `39,491,300,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,240,000.00 USD | 0.00 USD | 8,870.00 USD | `-30.83%` | `82,527,400,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,230,000.00 USD | 0.00 USD | 10,940.00 USD | `-30.19%` | `100,844,900,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,220,000.00 USD | 0.00 USD | 9,570.00 USD | `-29.55%` | `87,419,000,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,210,000.00 USD | 0.00 USD | 14,000.00 USD | `-28.90%` | `126,702,100,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,200,000.00 USD | 0.00 USD | 425.50 USD | `-28.26%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,200,000.00 USD | 0.00 USD | 3,660.00 USD | `-27.62%` | `32,557,400,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,190,000.00 USD | 0.00 USD | 1,300.00 USD | `-26.97%` | `11,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,190,000.00 USD | 0.00 USD | 8,950.00 USD | `-26.33%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,180,000.00 USD | 0.00 USD | 2,560.00 USD | `-25.69%` | `22,153,700,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,180,000.00 USD | 0.00 USD | 471.49 USD | `-25.04%` | `4,047,100,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,180,000.00 USD | 0.00 USD | 6,120.00 USD | `-24.40%` | `52,087,700,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,170,000.00 USD | 0.00 USD | 150,220.00 USD | `-23.75%` | `1,267,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,020,000.00 USD | 0.00 USD | 3,500.00 USD | `-23.11%` | `29,283,400,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,020,000.00 USD | 0.00 USD | 897.50 USD | `-21.82%` | `7,386,800,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,020,000.00 USD | 0.00 USD | 17,890.00 USD | `-21.18%` | `146,077,300,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,000,000.00 USD | 0.00 USD | 34,560.00 USD | `-20.54%` | `279,831,800,000,000.00` |
| `Live` | `Long` | `0.1245` | 967,860.00 USD | 0.00 USD | 7,500.00 USD | `-19.89%` | `60,262,700,000,000.00` |
| `Live` | `Long` | `0.1255` | 960,360.00 USD | 0.00 USD | 5,130.00 USD | `-19.25%` | `40,848,800,000,000.00` |
| `Live` | `Long` | `0.1265` | 955,240.00 USD | 0.00 USD | 15,110.00 USD | `-18.61%` | `119,436,400,000,000.00` |
| `Live` | `Long` | `0.1285` | 940,130.00 USD | 0.00 USD | 11,500.00 USD | `-17.32%` | `89,517,400,000,000.00` |
| `Live` | `Long` | `0.1295` | 928,620.00 USD | 0.00 USD | 6,290.00 USD | `-16.68%` | `48,593,700,000,000.00` |
| `Live` | `Long` | `0.1305` | 922,330.00 USD | 0.00 USD | 18,440.00 USD | `-16.03%` | `141,318,100,000,000.00` |
| `Live` | `Long` | `0.1315` | 903,890.00 USD | 0.00 USD | 4,380.00 USD | `-15.39%` | `33,301,600,000,000.00` |
| `Live` | `Long` | `0.1325` | 899,510.00 USD | 0.00 USD | 18,060.00 USD | `-14.75%` | `136,288,799,999,999.98` |
| `Live` | `Long` | `0.1335` | 881,450.00 USD | 0.00 USD | 54,720.00 USD | `-14.10%` | `409,897,300,000,000.00` |
| `Live` | `Long` | `0.1345` | 826,730.00 USD | 0.00 USD | 583.12 USD | `-13.46%` | `4,335,500,000,000.00` |
| `Live` | `Long` | `0.1355` | 826,150.00 USD | 0.00 USD | 12,930.00 USD | `-12.82%` | `95,428,600,000,000.00` |
| `Live` | `Long` | `0.1365` | 813,220.00 USD | 0.00 USD | 1,690.00 USD | `-12.17%` | `12,379,800,000,000.00` |
| `Live` | `Long` | `0.1375` | 811,530.00 USD | 0.00 USD | 14,170.00 USD | `-11.53%` | `103,066,200,000,000.00` |
| `Live` | `Long` | `0.1385` | 797,350.00 USD | 0.00 USD | 4,030.00 USD | `-10.89%` | `29,084,300,000,000.00` |
| `Live` | `Long` | `0.1395` | 793,330.00 USD | 0.00 USD | 29,080.00 USD | `-10.24%` | `208,433,000,000,000.00` |
| `Live` | `Long` | `0.1405` | 764,250.00 USD | 0.00 USD | 1,610.00 USD | `-9.60%` | `11,433,300,000,000.00` |
| `Live` | `Long` | `0.1415` | 762,640.00 USD | 0.00 USD | 26,150.00 USD | `-8.96%` | `184,815,300,000,000.00` |
| `Live` | `Long` | `0.1425` | 736,490.00 USD | 0.00 USD | 484,730.00 USD | `-8.31%` | `3,401,615,000,000,000.00` |
| `Live` | `Long` | `0.1435` | 251,760.00 USD | 0.00 USD | 19,500.00 USD | `-7.67%` | `135,886,299,999,999.98` |
| `Live` | `Long` | `0.1445` | 232,260.00 USD | 0.00 USD | 36,910.00 USD | `-7.03%` | `255,458,500,000,000.00` |
| `Live` | `Long` | `0.1455` | 195,350.00 USD | 0.00 USD | 85,060.00 USD | `-6.38%` | `584,609,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 110,290.00 USD | 0.00 USD | 27,920.00 USD | `-5.74%` | `190,575,800,000,000.00` |
| `Live` | `Long` | `0.1475` | 82,370.00 USD | 0.00 USD | 80,080.00 USD | `-5.10%` | `542,919,600,000,000.00` |
| `Live` | `Long` | `0.1485` | 2,290.00 USD | 0.00 USD | 2,290.00 USD | `-4.45%` | `15,410,500,000,000.00` |
| `Live` | `Short` | `0.1555` | 2,430.00 USD | 2,430.00 USD | 0.00 USD | `+0.05%` | `15,646,000,000,000.00` |
| `Live` | `Short` | `0.1605` | 5,500.00 USD | 3,070.00 USD | 0.00 USD | `+3.27%` | `19,137,200,000,000.00` |
| `Live` | `Short` | `0.1615` | 9,640.00 USD | 4,130.00 USD | 0.00 USD | `+3.91%` | `25,583,400,000,000.00` |
| `Live` | `Short` | `0.1625` | 10,520.00 USD | 887.09 USD | 0.00 USD | `+4.56%` | `5,459,000,000,000.00` |
| `Live` | `Short` | `0.1635` | 13,820.00 USD | 3,300.00 USD | 0.00 USD | `+5.20%` | `20,189,500,000,000.00` |
| `Live` | `Short` | `0.1645` | 13,940.00 USD | 118.90 USD | 0.00 USD | `+5.84%` | `722,800,000,000.00` |
| `Live` | `Short` | `0.1685` | 16,350.00 USD | 2,400.00 USD | 0.00 USD | `+8.42%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1715` | 17,830.00 USD | 1,480.00 USD | 0.00 USD | `+10.35%` | `8,642,500,000,000.00` |
| `Live` | `Short` | `0.1725` | 18,630.00 USD | 797.95 USD | 0.00 USD | `+10.99%` | `4,625,800,000,000.00` |
| `Live` | `Short` | `0.1785` | 18,770.00 USD | 138.82 USD | 0.00 USD | `+14.85%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1795` | 22,360.00 USD | 3,590.00 USD | 0.00 USD | `+15.49%` | `20,000,000,000,000.00` |
| `Live` | `Short` | `0.1875` | 22,950.00 USD | 591.24 USD | 0.00 USD | `+20.64%` | `3,153,300,000,000.00` |
| `Live` | `Short` | `0.1925` | 25,760.00 USD | 2,820.00 USD | 0.00 USD | `+23.86%` | `14,639,700,000,000.00` |
| `Live` | `Short` | `0.1945` | 26,390.00 USD | 623.68 USD | 0.00 USD | `+25.14%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 26,890.00 USD | 501.79 USD | 0.00 USD | `+27.08%` | `2,540,700,000,000.00` |
| `Live` | `Short` | `0.2055` | 38,480.00 USD | 11,590.00 USD | 0.00 USD | `+32.22%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 38,680.00 USD | 198.08 USD | 0.00 USD | `+34.15%` | `950,000,000,000.00` |
| `Live` | `Short` | `0.2095` | 38,840.00 USD | 164.23 USD | 0.00 USD | `+34.80%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2115` | 39,040.00 USD | 190.90 USD | 0.00 USD | `+36.08%` | `902,600,000,000.00` |
| `Live` | `Short` | `0.2135` | 54,730.00 USD | 15,690.00 USD | 0.00 USD | `+37.37%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 96,060.00 USD | 41,330.00 USD | 0.00 USD | `+38.66%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 122,160.00 USD | 26,090.00 USD | 0.00 USD | `+39.94%` | `119,969,800,000,000.00` |
| `Live` | `Short` | `0.2195` | 209,960.00 USD | 87,800.00 USD | 0.00 USD | `+41.23%` | `400,000,000,000,000.00` |
| `Live` | `Short` | `0.2235` | 210,070.00 USD | 114.52 USD | 0.00 USD | `+43.80%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 210,230.00 USD | 154.78 USD | 0.00 USD | `+45.09%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2285` | 235,130.00 USD | 24,910.00 USD | 0.00 USD | `+47.02%` | `108,995,000,000,000.00` |
| `Live` | `Short` | `0.2295` | 241,950.00 USD | 6,820.00 USD | 0.00 USD | `+47.66%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2355` | 257,880.00 USD | 15,930.00 USD | 0.00 USD | `+51.52%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 257,980.00 USD | 102.62 USD | 0.00 USD | `+52.81%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 258,780.00 USD | 796.25 USD | 0.00 USD | `+56.03%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 259,010.00 USD | 231.03 USD | 0.00 USD | `+57.32%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2525` | 309,510.00 USD | 50,500.00 USD | 0.00 USD | `+62.46%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 310,060.00 USD | 546.54 USD | 0.00 USD | `+63.75%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 313,920.00 USD | 3,870.00 USD | 0.00 USD | `+65.04%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 342,830.00 USD | 28,910.00 USD | 0.00 USD | `+65.68%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 395,450.00 USD | 52,620.00 USD | 0.00 USD | `+66.32%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 395,610.00 USD | 154.94 USD | 0.00 USD | `+68.25%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2635` | 395,810.00 USD | 201.21 USD | 0.00 USD | `+69.54%` | `763,600,000,000.00` |
| `Live` | `Short` | `0.2685` | 396,030.00 USD | 226.51 USD | 0.00 USD | `+72.76%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 409,550.00 USD | 13,510.00 USD | 0.00 USD | `+74.69%` | `49,773,600,000,000.00` |
| `Live` | `Short` | `0.2725` | 409,760.00 USD | 214.21 USD | 0.00 USD | `+75.33%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 437,650.00 USD | 27,890.00 USD | 0.00 USD | `+76.62%` | `101,607,700,000,000.00` |
| `Live` | `Short` | `0.2795` | 438,140.00 USD | 482.84 USD | 0.00 USD | `+79.84%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2815` | 748,350.00 USD | 310,210.00 USD | 0.00 USD | `+81.12%` | `1,101,995,500,000,000.00` |
| `Live` | `Short` | `0.2855` | 748,570.00 USD | 224.40 USD | 0.00 USD | `+83.70%` | `786,000,000,000.00` |
| `Live` | `Short` | `0.2915` | 748,760.00 USD | 187.26 USD | 0.00 USD | `+87.56%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 749,220.00 USD | 464.84 USD | 0.00 USD | `+88.20%` | `1,589,200,000,000.00` |
| `Live` | `Short` | `0.2955` | 749,490.00 USD | 264.59 USD | 0.00 USD | `+90.13%` | `895,400,000,000.00` |
| `Live` | `Short` | `0.2985` | 749,720.00 USD | 234.62 USD | 0.00 USD | `+92.06%` | `786,000,000,000.00` |
| `Live` | `Short` | `0.3065` | 752,060.00 USD | 2,330.00 USD | 0.00 USD | `+97.21%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.3075` | 758,350.00 USD | 6,290.00 USD | 0.00 USD | `+97.85%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 758,710.00 USD | 363.72 USD | 0.00 USD | `+98.49%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 770,640.00 USD | 11,930.00 USD | 0.00 USD | `+99.78%` | `38,407,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 564,300.00 USD | 0.00 USD | 355.00 USD | `-77.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 563,940.00 USD | 0.00 USD | 297.50 USD | `-72.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 563,640.00 USD | 0.00 USD | 353.50 USD | `-67.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 563,290.00 USD | 0.00 USD | 4,310.00 USD | `-64.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 558,980.00 USD | 0.00 USD | 475.11 USD | `-59.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 558,500.00 USD | 0.00 USD | 131.16 USD | `-57.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 558,370.00 USD | 0.00 USD | 881.45 USD | `-57.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 557,490.00 USD | 0.00 USD | 1,070.00 USD | `-56.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 556,410.00 USD | 0.00 USD | 1,400.00 USD | `-55.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 555,020.00 USD | 0.00 USD | 1,010.00 USD | `-55.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 554,010.00 USD | 0.00 USD | 4,100.00 USD | `-54.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 549,900.00 USD | 0.00 USD | 529.04 USD | `-54.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 549,380.00 USD | 0.00 USD | 2,390.00 USD | `-53.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 546,990.00 USD | 0.00 USD | 757.39 USD | `-51.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 546,230.00 USD | 0.00 USD | 1,490.00 USD | `-49.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 544,740.00 USD | 0.00 USD | 277.37 USD | `-44.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 544,470.00 USD | 0.00 USD | 262.50 USD | `-43.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 544,200.00 USD | 0.00 USD | 795.57 USD | `-43.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 543,410.00 USD | 0.00 USD | 181.00 USD | `-41.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 543,230.00 USD | 0.00 USD | 3,810.00 USD | `-35.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 539,410.00 USD | 0.00 USD | 1,550.00 USD | `-34.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 537,870.00 USD | 0.00 USD | 116.07 USD | `-30.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 537,750.00 USD | 0.00 USD | 19,070.00 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 518,680.00 USD | 0.00 USD | 577.22 USD | `-28.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 518,100.00 USD | 0.00 USD | 343.50 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 517,760.00 USD | 0.00 USD | 26,280.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 491,480.00 USD | 0.00 USD | 105.75 USD | `-24.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 491,370.00 USD | 0.00 USD | 21,540.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 469,830.00 USD | 0.00 USD | 83,620.00 USD | `-21.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 386,200.00 USD | 0.00 USD | 487.10 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 385,720.00 USD | 0.00 USD | 14,940.00 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 370,780.00 USD | 0.00 USD | 2,670.00 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 368,110.00 USD | 0.00 USD | 473.27 USD | `-17.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 367,640.00 USD | 0.00 USD | 203,210.00 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 164,430.00 USD | 0.00 USD | 2,800.00 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 161,630.00 USD | 0.00 USD | 1,590.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 160,040.00 USD | 0.00 USD | 6,000.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 154,040.00 USD | 0.00 USD | 3,350.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 150,680.00 USD | 0.00 USD | 502.28 USD | `-13.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 150,180.00 USD | 0.00 USD | 162.60 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 150,020.00 USD | 0.00 USD | 700.86 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 149,320.00 USD | 0.00 USD | 13,710.00 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 135,610.00 USD | 0.00 USD | 108.57 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 135,500.00 USD | 0.00 USD | 3,520.00 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 131,980.00 USD | 0.00 USD | 127.35 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 131,850.00 USD | 0.00 USD | 24,850.00 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 107,000.00 USD | 0.00 USD | 1,300.00 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 105,700.00 USD | 0.00 USD | 26,220.00 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 79,480.00 USD | 0.00 USD | 29,020.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 50,450.00 USD | 0.00 USD | 14,830.00 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 35,620.00 USD | 0.00 USD | 10,110.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 25,510.00 USD | 0.00 USD | 2,340.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 23,170.00 USD | 0.00 USD | 1,400.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 21,770.00 USD | 0.00 USD | 8,300.00 USD | `-3.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 13,470.00 USD | 0.00 USD | 5,510.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 7,960.00 USD | 0.00 USD | 4,890.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 3,070.00 USD | 0.00 USD | 175.79 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 2,900.00 USD | 0.00 USD | 2,900.00 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1555` | 21,460.00 USD | 21,460.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 22,840.00 USD | 1,370.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 23,390.00 USD | 554.07 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 27,190.00 USD | 3,800.00 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 27,320.00 USD | 124.14 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 28,540.00 USD | 1,220.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 29,050.00 USD | 514.57 USD | 0.00 USD | `+3.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 29,300.00 USD | 249.16 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 30,340.00 USD | 1,040.00 USD | 0.00 USD | `+5.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 34,800.00 USD | 4,450.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 39,110.00 USD | 4,320.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 89,320.00 USD | 50,210.00 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 89,910.00 USD | 589.50 USD | 0.00 USD | `+7.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 91,060.00 USD | 1,150.00 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 91,380.00 USD | 317.95 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 91,940.00 USD | 564.90 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 93,740.00 USD | 1,800.00 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 94,020.00 USD | 272.96 USD | 0.00 USD | `+10.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 102,850.00 USD | 8,840.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 103,070.00 USD | 219.54 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 104,430.00 USD | 1,350.00 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 105,080.00 USD | 657.66 USD | 0.00 USD | `+13.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 105,420.00 USD | 336.40 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 106,320.00 USD | 898.02 USD | 0.00 USD | `+14.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 132,710.00 USD | 26,390.00 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 144,250.00 USD | 11,540.00 USD | 0.00 USD | `+16.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 154,490.00 USD | 10,240.00 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 155,350.00 USD | 864.12 USD | 0.00 USD | `+17.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 157,880.00 USD | 2,520.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 158,150.00 USD | 276.75 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 158,280.00 USD | 128.68 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 161,650.00 USD | 3,370.00 USD | 0.00 USD | `+20.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 165,360.00 USD | 3,700.00 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 165,600.00 USD | 245.50 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 166,260.00 USD | 660.73 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 166,960.00 USD | 697.34 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 167,180.00 USD | 222.24 USD | 0.00 USD | `+23.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 196,310.00 USD | 29,130.00 USD | 0.00 USD | `+23.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 203,380.00 USD | 7,070.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 203,570.00 USD | 194.50 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 203,710.00 USD | 137.77 USD | 0.00 USD | `+25.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 203,840.00 USD | 133.19 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 207,600.00 USD | 3,750.00 USD | 0.00 USD | `+27.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 208,090.00 USD | 492.19 USD | 0.00 USD | `+28.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 230,990.00 USD | 22,900.00 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 231,550.00 USD | 560.96 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 252,890.00 USD | 21,340.00 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 253,080.00 USD | 182.72 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 338,970.00 USD | 85,900.00 USD | 0.00 USD | `+31.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 340,440.00 USD | 1,470.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 340,610.00 USD | 174.20 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 342,690.00 USD | 2,080.00 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 342,940.00 USD | 252.51 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 345,310.00 USD | 2,370.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 345,430.00 USD | 126.50 USD | 0.00 USD | `+36.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 345,630.00 USD | 190.80 USD | 0.00 USD | `+36.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 345,990.00 USD | 361.76 USD | 0.00 USD | `+38.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 346,350.00 USD | 365.12 USD | 0.00 USD | `+39.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 352,630.00 USD | 6,280.00 USD | 0.00 USD | `+40.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 353,000.00 USD | 368.47 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 375,490.00 USD | 22,490.00 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 375,820.00 USD | 333.91 USD | 0.00 USD | `+43.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 379,800.00 USD | 3,980.00 USD | 0.00 USD | `+43.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 380,180.00 USD | 378.55 USD | 0.00 USD | `+45.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 380,560.00 USD | 380.23 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 380,740.00 USD | 185.87 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 384,580.00 USD | 3,840.00 USD | 0.00 USD | `+47.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 429,230.00 USD | 44,650.00 USD | 0.00 USD | `+48.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 433,490.00 USD | 4,260.00 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 435,010.00 USD | 1,520.00 USD | 0.00 USD | `+50.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 456,230.00 USD | 21,230.00 USD | 0.00 USD | `+52.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 458,760.00 USD | 2,530.00 USD | 0.00 USD | `+53.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 458,960.00 USD | 195.67 USD | 0.00 USD | `+54.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 478,680.00 USD | 19,720.00 USD | 0.00 USD | `+54.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 487,980.00 USD | 9,300.00 USD | 0.00 USD | `+55.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 489,730.00 USD | 1,750.00 USD | 0.00 USD | `+57.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 508,490.00 USD | 18,750.00 USD | 0.00 USD | `+58.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 509,040.00 USD | 551.23 USD | 0.00 USD | `+59.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 509,430.00 USD | 397.90 USD | 0.00 USD | `+60.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 513,770.00 USD | 4,330.00 USD | 0.00 USD | `+61.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 514,090.00 USD | 320.66 USD | 0.00 USD | `+61.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 529,970.00 USD | 15,880.00 USD | 0.00 USD | `+63.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 531,970.00 USD | 2,000.00 USD | 0.00 USD | `+63.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 534,520.00 USD | 2,550.00 USD | 0.00 USD | `+64.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 546,250.00 USD | 11,730.00 USD | 0.00 USD | `+65.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 551,410.00 USD | 5,160.00 USD | 0.00 USD | `+65.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 568,280.00 USD | 16,870.00 USD | 0.00 USD | `+66.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 595,070.00 USD | 26,790.00 USD | 0.00 USD | `+67.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 595,340.00 USD | 272.88 USD | 0.00 USD | `+74.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 595,460.00 USD | 114.99 USD | 0.00 USD | `+77.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 595,850.00 USD | 394.01 USD | 0.00 USD | `+77.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 596,230.00 USD | 375.53 USD | 0.00 USD | `+80.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 598,360.00 USD | 2,130.00 USD | 0.00 USD | `+83.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 598,940.00 USD | 579.27 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 600,690.00 USD | 1,750.00 USD | 0.00 USD | `+86.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 600,790.00 USD | 101.21 USD | 0.00 USD | `+90.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 601,050.00 USD | 262.73 USD | 0.00 USD | `+90.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 602,490.00 USD | 1,440.00 USD | 0.00 USD | `+91.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 607,920.00 USD | 5,430.00 USD | 0.00 USD | `+93.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 613,350.00 USD | 5,430.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 613,640.00 USD | 289.61 USD | 0.00 USD | `+96.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 614,130.00 USD | 487.09 USD | 0.00 USD | `+97.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 620,700.00 USD | 6,570.00 USD | 0.00 USD | `+99.14%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `177.22M` | Total OI Tokens: `1,157,505,218.9 ARB`
  * 1h OI Change: `-1.94%` | 4h OI Change: `-5.76%` | 24h OI Change: `-18.86%`
  * Exchange Breakdown: Binance=`39.87M` | Bybit=`24.79M` | OKX=`13.57M` | Hyperliquid=`12.32M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.68K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0049%` | **USDT OKX** | `-0.0039%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0042%` |
| **USDT MEXC** | `-0.0037%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0093%` | **USDT Bitget** | `-0.0121%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `49.48%` | `50.52%` | `0.98` | 1,820,000.00 USD |
| `15M` | `Binance` | `52.66%` | `47.34%` | `1.11` | 675,010.00 USD |
| `15M` | `OKX` | `55.54%` | `44.46%` | `1.25` | 226,300.00 USD |
| `15M` | `Bybit` | `26.7%` | `73.3%` | `0.36` | 134,860.00 USD |
| `15M` | `KuCoin` | `42.19%` | `57.81%` | `0.73` | 130,400.00 USD |
| `15M` | `Gate` | `54.82%` | `45.18%` | `1.21` | 27,760.00 USD |
| `15M` | `Bitget` | `44.14%` | `55.86%` | `0.79` | 41,180.00 USD |
| `15M` | `BingX` | `50.48%` | `49.52%` | `1.02` | 114,150.00 USD |
| `15M` | `MEXC` | `39.54%` | `60.46%` | `0.65` | 68,840.00 USD |
| `15M` | `Bitunix` | `46.74%` | `53.26%` | `0.88` | 39,520.00 USD |
| `15M` | `Hyperliquid` | `29.39%` | `70.61%` | `0.42` | 20,480.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.72%` | `52.28%` | `0.91` | 268,880.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 53,670.00 USD |
| `15M` | `HTX` | `32.98%` | `67.02%` | `0.49` | 565.94 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `15.33%` | `84.67%` | `0.18` | 14,870.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 889.33 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `52.66%` | `47.34%` | `1.11` | 675,010.00 USD |
| `15M` | `Global Accounts` | `49.48%` | `50.52%` | `0.98` | 1,820,000.00 USD |
| `1H` | `ARB` | `48.21%` | `51.79%` | `0.93` | 23,710,000.00 USD |
| `1H` | `Binance` | `51.62%` | `48.38%` | `1.07` | 9,390,000.00 USD |
| `1H` | `OKX` | `48.31%` | `51.69%` | `0.93` | 1,260,000.00 USD |
| `1H` | `Bybit` | `49.05%` | `50.95%` | `0.96` | 1,680,000.00 USD |
| `1H` | `KuCoin` | `35.47%` | `64.53%` | `0.55` | 588,410.00 USD |
| `1H` | `Gate` | `40.09%` | `59.91%` | `0.67` | 619,770.00 USD |
| `1H` | `Bitget` | `55.87%` | `44.13%` | `1.27` | 632,340.00 USD |
| `1H` | `BingX` | `39.12%` | `60.88%` | `0.64` | 2,940,000.00 USD |
| `1H` | `MEXC` | `52.84%` | `47.16%` | `1.12` | 962,930.00 USD |
| `1H` | `Bitunix` | `36.72%` | `63.28%` | `0.58` | 546,340.00 USD |
| `1H` | `Hyperliquid` | `62.79%` | `37.21%` | `1.69` | 475,450.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.74%` | `51.26%` | `0.95` | 4,120,000.00 USD |
| `1H` | `Crypto.com` | `1.78%` | `98.22%` | `0.02` | 3,910.00 USD |
| `1H` | `WhiteBIT` | `34.79%` | `65.21%` | `0.53` | 196,440.00 USD |
| `1H` | `HTX` | `61.25%` | `38.75%` | `1.58` | 6,040.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.5%` | `59.5%` | `0.68` | 171,370.00 USD |
| `1H` | `Aster` | `26.01%` | `73.99%` | `0.35` | 36,110.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `28.86%` | `71.14%` | `0.41` | 81,890.00 USD |
| `1H` | `Whale Positions` | `51.62%` | `48.38%` | `1.07` | 9,390,000.00 USD |
| `1H` | `Global Accounts` | `48.21%` | `51.79%` | `0.93` | 23,710,000.00 USD |
| `4H` | `ARB` | `51.51%` | `48.49%` | `1.06` | 78,970,000.00 USD |
| `4H` | `Binance` | `52.22%` | `47.78%` | `1.09` | 28,240,000.00 USD |
| `4H` | `OKX` | `50.6%` | `49.4%` | `1.02` | 8,340,000.00 USD |
| `4H` | `Bybit` | `46.72%` | `53.28%` | `0.88` | 8,450,000.00 USD |
| `4H` | `KuCoin` | `46.11%` | `53.89%` | `0.86` | 3,000,000.00 USD |
| `4H` | `Gate` | `56.39%` | `43.61%` | `1.29` | 6,120,000.00 USD |
| `4H` | `Bitget` | `42.75%` | `57.25%` | `0.75` | 2,900,000.00 USD |
| `4H` | `BingX` | `38.68%` | `61.32%` | `0.63` | 3,300,000.00 USD |
| `4H` | `MEXC` | `47.62%` | `52.38%` | `0.91` | 4,870,000.00 USD |
| `4H` | `Bitunix` | `50.48%` | `49.52%` | `1.02` | 1,810,000.00 USD |
| `4H` | `Hyperliquid` | `57.15%` | `42.85%` | `1.33` | 2,150,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.68%` | `50.32%` | `0.99` | 6,280,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `94.13%` | `5.87%` | `16.04` | 2,540,000.00 USD |
| `4H` | `HTX` | `46.71%` | `53.29%` | `0.88` | 74,310.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.19%` | `53.81%` | `0.86` | 802,300.00 USD |
| `4H` | `Aster` | `38.83%` | `61.17%` | `0.63` | 103,240.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `52.22%` | `47.78%` | `1.09` | 28,240,000.00 USD |
| `4H` | `Global Accounts` | `51.51%` | `48.49%` | `1.06` | 78,970,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1550` | `0.1551` | `0.1550` | `0.1559` | `0.1547` | 1,273,091.41 USD | 679,769.26 USD | 593,322.15 USD | 86,447.11 USD | `+6.79%` | `15B / 31S` |
| `5:00 UTC` | `0.1550` | `0.1546` | `0.1550` | `0.1552` | `0.1538` | 1,428,021.10 USD | 808,975.04 USD | 619,046.06 USD | 189,928.98 USD | `+13.30%` | `17B / 10S` |
| `0:00 UTC` | `0.1525` | `0.1532` | `0.1525` | `0.1544` | `0.1522` | 2,110,848.48 USD | 1,098,398.51 USD | 1,012,449.97 USD | 85,948.54 USD | `+4.07%` | `6B / 10S` |
| `5:00 UTC` | `0.1507` | `0.1503` | `0.1507` | `0.1530` | `0.1471` | 10,277,659.34 USD | 4,448,495.39 USD | 5,829,163.95 USD | -1,380,668.57 USD | `-13.43%` | `4B / 24S` |
| `0:00 UTC` | `0.1498` | `0.1510` | `0.1498` | `0.1532` | `0.1492` | 3,257,292.15 USD | 1,571,991.63 USD | 1,685,300.52 USD | -113,308.89 USD | `-3.48%` | `23B / 32S` |
| `5:00 UTC` | `0.1550` | `0.1544` | `0.1550` | `0.1556` | `0.1526` | 2,934,484.43 USD | 1,770,871.27 USD | 1,163,613.16 USD | 607,258.11 USD | `+20.69%` | `21B / 14S` |
| `0:00 UTC` | `0.1552` | `0.1542` | `0.1552` | `0.1557` | `0.1528` | 1,449,793.31 USD | 742,538.14 USD | 707,255.18 USD | 35,282.96 USD | `+2.43%` | `14B / 29S` |
| `5:00 UTC` | `0.1544` | `0.1535` | `0.1544` | `0.1546` | `0.1528` | 1,252,838.62 USD | 503,258.60 USD | 749,580.02 USD | -246,321.42 USD | `-19.66%` | `11B / 39S` |
| `0:00 UTC` | `0.1540` | `0.1534` | `0.1540` | `0.1545` | `0.1520` | 1,447,365.29 USD | 641,921.41 USD | 805,443.88 USD | -163,522.47 USD | `-11.30%` | `6B / 8S` |
| `5:00 UTC` | `0.1525` | `0.1529` | `0.1525` | `0.1537` | `0.1524` | 461,580.78 USD | 254,963.21 USD | 206,617.57 USD | 48,345.64 USD | `+10.47%` | `28B / 22S` |

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
| `5m` | 16,830.00 USD | 45,220.00 USD | **`ACCUMULATION`** |
| `15m` | 30,400.00 USD | -52,080.00 USD | **`DISTRIBUTION`** |
| `30m` | -128,360.00 USD | 62,690.00 USD | **`DISTRIBUTION`** |
| `1h` | -139,830.00 USD | -288,480.00 USD | **`DISTRIBUTION`** |
| `2h` | -417,640.00 USD | -1,200,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -97,760.00 USD | -240,760.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,050,000.00 USD | -5,880,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,070,000.00 USD | -7,180,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,050,000.00 USD | -7,860,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,400,000.00 USD | -8,870,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,750,000.00 USD | -36,840,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,980,000.00 USD | -164,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.83K` | 15m=`+30.40K` | 1h=`-139.83K` | 24h=`-2.40M`
* Futures Capital Netflows: 5m=`+45.22K` | 15m=`-52.08K` | 1h=`-288.48K` | 24h=`-8.87M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
