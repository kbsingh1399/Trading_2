# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 09:25:13 IST` (`2026-10-30 03:55:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1575` | `0.1584` | `0.1573` | `0.1583` | `2,540,718` | 401,097.86 USD | 57,031.97 USD | `+14.22%` | -8,077,692.56 USD | `+0.46` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.1583` | `0.1585` | `0.1576` | `0.1581` | `3,155,688` | 498,650.77 USD | -105,469.93 USD | `-21.15%` | -8,183,162.48 USD | `-2.21` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.1582` | `0.1584` | `0.1580` | `0.1583` | `1,705,692` | 269,873.63 USD | 58,686.59 USD | `+21.75%` | -8,124,475.89 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1556` | `0.1570` | `0.1553` | `0.1568` | `3,268,360` | 510,482.89 USD | 152,857.47 USD | `+29.94%` | -8,154,818.07 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1568` | `0.1585` | `0.1566` | `0.1581` | `7,768,422` | 1,225,850.60 USD | -80,576.74 USD | `-6.57%` | -8,235,394.81 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1582` | `0.1584` | `0.1580` | `0.1583` | `1,705,692` | 269,873.63 USD | 58,686.59 USD | `+21.75%` | -8,176,708.22 USD | `+0.24` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1555` | `0.1558` | `0.1520` | `0.1533` | `31,981,907` | 4,912,629.10 USD | -386,533.95 USD | `-7.87%` | -8,687,671.43 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1533` | `0.1563` | `0.1526` | `0.1560` | `24,694,709` | 3,828,145.62 USD | 314,402.05 USD | `+8.21%` | -8,373,269.38 USD | `+0.72` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1560` | `0.1585` | `0.1553` | `0.1583` | `16,961,053` | 2,664,883.46 USD | 196,723.61 USD | `+7.38%` | -8,176,545.77 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1584` | `196,388,242` | 29,990,400.32 USD | -677,014.87 USD | `-2.26%` | -8,177,148.92 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1631` | `0.1697` | `0.1630` | `0.1679` | `68,848,429` | 11,449,693.18 USD | -430,993.81 USD | `-3.76%` | -1,340,323.74 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1679` | `0.1749` | `0.1674` | `0.1745` | `114,906,320` | 19,692,415.49 USD | -1,238,128.34 USD | `-6.29%` | -2,578,452.08 USD | `-1.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -3,775,910.08 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -7,500,134.05 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1584` | `196,388,242` | 29,990,400.32 USD | -677,014.87 USD | `-2.26%` | -8,177,148.92 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1723` | 8,870.25 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 8.87K USD at 0.1723 USD [API] | `2026-10-28 23:21:23` |
| `ANNOUNCEMENT` | `INFO` | `0.1717` | 5,737.95 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 5.74K USD at 0.1717 USD [API] | `2026-10-28 23:48:04` |
| `ANNOUNCEMENT` | `INFO` | `0.1717` | 5,790.16 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 5.79K USD at 0.1717 USD [API] | `2026-10-28 23:50:01` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 7,886.04 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 7.89K USD at 0.1813 USD [API] | `2026-10-17 16:52:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 99.34 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.10K USD at 0.1813 USD [API] | `2026-10-17 16:52:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 9,999.98 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 10.00K USD at 0.1813 USD [API] | `2026-10-17 16:52:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 2,495.96 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 2.50K USD at 0.1813 USD [API] | `2026-10-17 16:52:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1813` | 6,511.66 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 6.51K USD at 0.1813 USD [API] | `2026-10-17 16:52:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1721` | 7,449.32 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 7.45K USD at 0.1721 USD [API] | `2026-10-29 00:31:44` |
| `ANNOUNCEMENT` | `INFO` | `0.1709` | 7,729.41 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 7.73K USD at 0.1709 USD [API] | `2026-10-29 01:05:08` |


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
| `Live` | `Long Liquidation` | `0.0345` | 908.42 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 798.75 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0395` | 129.92 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0405` | 1,080.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0435` | 32,330.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 551.51 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0555` | 195,160.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 4,680.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 743.33 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 1,130.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 6,810.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 417.15 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 3,180.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 102,500.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 6,140.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 7,810.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 15,030.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 154.19 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 14,460.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 4,980.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 627.22 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 72,110.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 162.28 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 589.50 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 198.90 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 4,130.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 3,510.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 535.45 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 145.24 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 2,810.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 8,840.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,600.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 6,330.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 8,320.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 15,300.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 16,380.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 10,460.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 105.42 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,580.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 1,540.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 9,240.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,450.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 122,890.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 6,320.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 27,110.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 25,780.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 39,440.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,400.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 348.01 USD | 999,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 29,740.00 USD | 998,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,710.00 USD | 969,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 18,980.00 USD | 967,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,130.00 USD | 948,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 16,660.00 USD | 946,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 4,380.00 USD | 929,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,810.00 USD | 925,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 52,860.00 USD | 920,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1336` | 3,280,000.00 USD | 3,280,000.00 USD | 3,580.00 USD | 5,990.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 3,250,000.00 USD | 3,250,000.00 USD | 9,160.00 USD | 7,730.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1344` | 3,200,000.00 USD | 3,200,000.00 USD | 6,410.00 USD | 5,790.00 USD | 19,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 42,940.00 USD | 867,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1348` | 3,170,000.00 USD | 3,170,000.00 USD | 31,170.00 USD | 7,150.00 USD | 23,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 3,110,000.00 USD | 3,110,000.00 USD | 11,390.00 USD | 6,290.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,540.00 USD | 824,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1356` | 3,070,000.00 USD | 3,070,000.00 USD | 16,150.00 USD | 12,180.00 USD | 9,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 3,030,000.00 USD | 3,030,000.00 USD | 25,240.00 USD | 8,630.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 2,990,000.00 USD | 2,990,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 1,690.00 USD | 821,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1368` | 2,970,000.00 USD | 2,970,000.00 USD | 4,500.00 USD | 7,610.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1370` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,740.00 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 2,950,000.00 USD | 2,950,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1373` | 2,710,000.00 USD | 2,710,000.00 USD | 5,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 21,990.00 USD | 819,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1376` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,730.00 USD | 536.58 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1379` | 2,700,000.00 USD | 2,700,000.00 USD | 2,250.00 USD | 821.64 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1380` | 2,950,000.00 USD | 2,950,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1382` | 2,690,000.00 USD | 2,690,000.00 USD | 10,310.00 USD | 9,440.00 USD | 29,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 2,930,000.00 USD | 2,930,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1385` | 2,640,000.00 USD | 2,640,000.00 USD | 31,240.00 USD | 0.00 USD | 55,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 13,380.00 USD | 797,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1388` | 2,560,000.00 USD | 2,560,000.00 USD | 12,440.00 USD | 1,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1388` | 2,890,000.00 USD | 2,890,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1391` | 2,540,000.00 USD | 2,540,000.00 USD | 15,160.00 USD | 1,440.00 USD | 71,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1392` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1394` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 6,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 5,960.00 USD | 784,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1397` | 2,450,000.00 USD | 2,450,000.00 USD | 12,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1400` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 2,780,000.00 USD | 2,780,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1404` | 2,760,000.00 USD | 2,760,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 885.87 USD | 778,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1412` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 2,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1415` | 34,710.00 USD | 777,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1416` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1421` | 2,430,000.00 USD | 2,430,000.00 USD | 4,030.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 498,880.00 USD | 742,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1432` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1433` | 2,420,000.00 USD | 2,420,000.00 USD | 3,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 20,420.00 USD | 243,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1436` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1436` | 2,730,000.00 USD | 2,730,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1439` | 2,390,000.00 USD | 2,390,000.00 USD | 17,680.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1440` | 2,690,000.00 USD | 2,690,000.00 USD | 13,180.00 USD | 5,260.00 USD | 3,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1442` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1444` | 2,670,000.00 USD | 2,670,000.00 USD | 3,450.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 223,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1451` | 2,370,000.00 USD | 2,370,000.00 USD | 2,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1452` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 5,660.00 USD | 14,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 94,810.00 USD | 213,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1456` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1460` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,430.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1464` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 35,240.00 USD | 118,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1466` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 2,630,000.00 USD | 2,630,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 2,360,000.00 USD | 2,360,000.00 USD | 12,090.00 USD | 2,700.00 USD | 6,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1472` | 2,340,000.00 USD | 2,340,000.00 USD | 6,430.00 USD | 14,550.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 2,610,000.00 USD | 2,610,000.00 USD | 19,180.00 USD | 0.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 2,250,000.00 USD | 2,250,000.00 USD | 33,920.00 USD | 8,290.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 81,380.00 USD | 83,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1605` | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1607` | 1,760,000.00 USD | 1,760,000.00 USD | 12,980.00 USD | 0.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1608` | 3,470,000.00 USD | 3,470,000.00 USD | 208,080.00 USD | 240,680.00 USD | 329,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1610` | 1,900,000.00 USD | 1,900,000.00 USD | 34,860.00 USD | 0.00 USD | 106,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1612` | 4,440,000.00 USD | 4,440,000.00 USD | 353,120.00 USD | 328,050.00 USD | 287,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1613` | 2,050,000.00 USD | 2,050,000.00 USD | 37,090.00 USD | 11,530.00 USD | 97,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1615` | 3,970.00 USD | 7,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1616` | 2,070,000.00 USD | 2,070,000.00 USD | 17,630.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 5,030,000.00 USD | 5,030,000.00 USD | 293,210.00 USD | 131,180.00 USD | 165,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 2,200,000.00 USD | 2,200,000.00 USD | 91,300.00 USD | 41,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1620` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 196,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1622` | 2,330,000.00 USD | 2,330,000.00 USD | 76,010.00 USD | 54,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1624` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 193,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 2,440,000.00 USD | 2,440,000.00 USD | 54,920.00 USD | 48,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1625` | 2,670.00 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1628` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 5,600,000.00 USD | 5,600,000.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1631` | 2,650,000.00 USD | 2,650,000.00 USD | 88,400.00 USD | 23,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1634` | 2,680,000.00 USD | 2,680,000.00 USD | 10,020.00 USD | 10,690.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,930.00 USD | 12,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1636` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 13,670.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1637` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 22,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1640` | 2,720,000.00 USD | 2,720,000.00 USD | 9,110.00 USD | 13,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1640` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 29,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1643` | 2,780,000.00 USD | 2,780,000.00 USD | 10,070.00 USD | 35,000.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1644` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 8,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1645` | 232.18 USD | 12,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1715` | 1,480.00 USD | 13,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1716` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 42,020.00 USD | 15,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1718` | 4,300,000.00 USD | 4,300,000.00 USD | 12,630.00 USD | 10,110.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 4,450,000.00 USD | 4,450,000.00 USD | 107,900.00 USD | 16,860.00 USD | 30,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1724` | 4,520,000.00 USD | 4,520,000.00 USD | 21,930.00 USD | 0.00 USD | 48,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 8,220,000.00 USD | 8,220,000.00 USD | 118,060.00 USD | 0.00 USD | 208,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 2,460.00 USD | 16,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1745` | 1,770.00 USD | 17,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.1775` | 316.07 USD | 18,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1776` | 11,370,000.00 USD | 11,370,000.00 USD | 186,770.00 USD | 59,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 11,620,000.00 USD | 11,620,000.00 USD | 52,730.00 USD | 46,410.00 USD | 157,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 11,850,000.00 USD | 11,850,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 18,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Short Liquidation` | `0.1916` | 17,140,000.00 USD | 17,140,000.00 USD | 7,460.00 USD | 5,300.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1920` | 17,150,000.00 USD | 17,150,000.00 USD | 0.00 USD | 5,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1924` | 17,170,000.00 USD | 17,170,000.00 USD | 12,420.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1925` | 543.50 USD | 18,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1928` | 17,190,000.00 USD | 17,190,000.00 USD | 11,600.00 USD | 7,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1944` | 17,190,000.00 USD | 17,190,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1945` | 623.68 USD | 19,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1952` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1956` | 17,210,000.00 USD | 17,210,000.00 USD | 4,860.00 USD | 2,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1960` | 17,220,000.00 USD | 17,220,000.00 USD | 5,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1964` | 17,240,000.00 USD | 17,240,000.00 USD | 6,470.00 USD | 2,700.00 USD | 10,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 19,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 31,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 386.27 USD | 31,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 3,230.00 USD | 34,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 50,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 91,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 113,920.00 USD | 206,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 206,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 206,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,820.00 USD | 213,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2315` | 24,350.00 USD | 237,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 1,200.00 USD | 238,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 254,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 254,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 255,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2445` | 231.03 USD | 255,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2505` | 50,100.00 USD | 305,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 306,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 310,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 28,910.00 USD | 339,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 52,620.00 USD | 391,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 392,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 392,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 405,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 405,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 417,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 417,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2885` | 5,810.00 USD | 423,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 423,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 424,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 294,020.00 USD | 718,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 8,630.00 USD | 727,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 727,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3095` | 132.90 USD | 727,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 739,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 495.44 USD | 740,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0345` | 1,870,000.00 USD | 0.00 USD | 908.42 USD | `-77.89%` | `26,331,000,000,000.00` |
| `Live` | `Long` | `0.0355` | 1,870,000.00 USD | 0.00 USD | 798.75 USD | `-77.25%` | `22,500,000,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,870,000.00 USD | 0.00 USD | 1,490.00 USD | `-75.32%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0395` | 1,870,000.00 USD | 0.00 USD | 129.92 USD | `-74.68%` | `3,289,200,000,000.00` |
| `Live` | `Long` | `0.0405` | 1,870,000.00 USD | 0.00 USD | 1,080.00 USD | `-74.04%` | `26,643,700,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,870,000.00 USD | 0.00 USD | 110.22 USD | `-73.40%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,870,000.00 USD | 0.00 USD | 170.00 USD | `-72.76%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0435` | 1,870,000.00 USD | 0.00 USD | 32,330.00 USD | `-72.12%` | `743,202,800,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,840,000.00 USD | 0.00 USD | 109.52 USD | `-68.27%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,840,000.00 USD | 0.00 USD | 551.51 USD | `-67.63%` | `10,921,000,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,840,000.00 USD | 0.00 USD | 289.43 USD | `-66.35%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,840,000.00 USD | 0.00 USD | 2,270.00 USD | `-65.07%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0555` | 1,830,000.00 USD | 0.00 USD | 195,160.00 USD | `-64.43%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,640,000.00 USD | 0.00 USD | 15,650.00 USD | `-63.79%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,620,000.00 USD | 0.00 USD | 4,680.00 USD | `-62.50%` | `79,923,000,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,620,000.00 USD | 0.00 USD | 743.33 USD | `-61.86%` | `12,493,000,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,620,000.00 USD | 0.00 USD | 1,130.00 USD | `-61.22%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,620,000.00 USD | 0.00 USD | 6,810.00 USD | `-59.94%` | `108,957,000,000,000.00` |
| `Live` | `Long` | `0.0645` | 1,610,000.00 USD | 0.00 USD | 417.15 USD | `-58.66%` | `6,467,400,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,610,000.00 USD | 0.00 USD | 3,180.00 USD | `-57.38%` | `47,846,600,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,610,000.00 USD | 0.00 USD | 102,500.00 USD | `-56.74%` | `1,518,522,500,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,500,000.00 USD | 0.00 USD | 6,140.00 USD | `-56.10%` | `89,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,500,000.00 USD | 0.00 USD | 976.14 USD | `-55.45%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,500,000.00 USD | 0.00 USD | 2,970.00 USD | `-54.81%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,490,000.00 USD | 0.00 USD | 5,840.00 USD | `-54.17%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,490,000.00 USD | 0.00 USD | 111.58 USD | `-53.53%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,490,000.00 USD | 0.00 USD | 2,440.00 USD | `-52.89%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,490,000.00 USD | 0.00 USD | 7,810.00 USD | `-52.25%` | `104,866,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,480,000.00 USD | 0.00 USD | 15,030.00 USD | `-50.97%` | `196,419,200,000,000.00` |
| `Live` | `Long` | `0.0775` | 1,460,000.00 USD | 0.00 USD | 154.19 USD | `-50.33%` | `1,989,600,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,460,000.00 USD | 0.00 USD | 4,630.00 USD | `-49.04%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,460,000.00 USD | 0.00 USD | 14,460.00 USD | `-47.12%` | `175,233,400,000,000.00` |
| `Live` | `Long` | `0.0835` | 1,440,000.00 USD | 0.00 USD | 4,980.00 USD | `-46.48%` | `59,604,600,000,000.00` |
| `Live` | `Long` | `0.0845` | 1,440,000.00 USD | 0.00 USD | 627.22 USD | `-45.84%` | `7,422,700,000,000.00` |
| `Live` | `Long` | `0.0855` | 1,440,000.00 USD | 0.00 USD | 72,110.00 USD | `-45.20%` | `843,421,600,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,370,000.00 USD | 0.00 USD | 19,460.00 USD | `-44.56%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,350,000.00 USD | 0.00 USD | 162.28 USD | `-43.92%` | `1,854,600,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,350,000.00 USD | 0.00 USD | 589.50 USD | `-43.28%` | `6,661,000,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,350,000.00 USD | 0.00 USD | 198.90 USD | `-42.64%` | `2,222,400,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,350,000.00 USD | 0.00 USD | 113.80 USD | `-41.35%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,350,000.00 USD | 0.00 USD | 4,130.00 USD | `-40.71%` | `44,668,100,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,340,000.00 USD | 0.00 USD | 3,510.00 USD | `-40.07%` | `37,530,200,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,340,000.00 USD | 0.00 USD | 1,510.00 USD | `-39.43%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0955` | 1,340,000.00 USD | 0.00 USD | 535.45 USD | `-38.79%` | `5,606,800,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,340,000.00 USD | 0.00 USD | 1,600.00 USD | `-38.15%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,330,000.00 USD | 0.00 USD | 145.24 USD | `-37.51%` | `1,489,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,330,000.00 USD | 0.00 USD | 2,810.00 USD | `-36.87%` | `28,516,700,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,330,000.00 USD | 0.00 USD | 8,840.00 USD | `-36.23%` | `88,805,800,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,320,000.00 USD | 0.00 USD | 2,600.00 USD | `-35.59%` | `25,906,300,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,320,000.00 USD | 0.00 USD | 6,330.00 USD | `-33.66%` | `61,115,700,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,310,000.00 USD | 0.00 USD | 8,320.00 USD | `-33.02%` | `79,663,200,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,310,000.00 USD | 0.00 USD | 15,300.00 USD | `-32.38%` | `145,015,100,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,290,000.00 USD | 0.00 USD | 16,380.00 USD | `-31.74%` | `153,824,500,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,270,000.00 USD | 0.00 USD | 10,460.00 USD | `-31.10%` | `97,275,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,260,000.00 USD | 0.00 USD | 11,210.00 USD | `-30.46%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1095` | 1,250,000.00 USD | 0.00 USD | 105.42 USD | `-29.82%` | `962,700,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,250,000.00 USD | 0.00 USD | 14,580.00 USD | `-29.18%` | `131,917,100,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,240,000.00 USD | 0.00 USD | 425.50 USD | `-28.53%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,240,000.00 USD | 0.00 USD | 1,540.00 USD | `-27.25%` | `13,599,500,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,240,000.00 USD | 0.00 USD | 9,240.00 USD | `-26.61%` | `80,672,600,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,230,000.00 USD | 0.00 USD | 1,450.00 USD | `-25.97%` | `12,552,800,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,220,000.00 USD | 0.00 USD | 122,890.00 USD | `-25.33%` | `1,054,886,800,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,100,000.00 USD | 0.00 USD | 6,320.00 USD | `-24.69%` | `53,762,800,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,100,000.00 USD | 0.00 USD | 27,110.00 USD | `-24.05%` | `228,753,800,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,070,000.00 USD | 0.00 USD | 1,830.00 USD | `-23.41%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,070,000.00 USD | 0.00 USD | 303.75 USD | `-22.13%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,070,000.00 USD | 0.00 USD | 25,780.00 USD | `-21.48%` | `210,482,400,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,040,000.00 USD | 0.00 USD | 39,440.00 USD | `-20.84%` | `319,346,000,000,000.00` |
| `Live` | `Long` | `0.1245` | 1,000,000.00 USD | 0.00 USD | 1,400.00 USD | `-20.20%` | `11,249,300,000,000.00` |
| `Live` | `Long` | `0.1255` | 999,240.00 USD | 0.00 USD | 348.01 USD | `-19.56%` | `2,773,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 998,900.00 USD | 0.00 USD | 29,740.00 USD | `-18.92%` | `235,089,900,000,000.00` |
| `Live` | `Long` | `0.1275` | 969,160.00 USD | 0.00 USD | 1,710.00 USD | `-18.28%` | `13,445,900,000,000.00` |
| `Live` | `Long` | `0.1285` | 967,440.00 USD | 0.00 USD | 18,980.00 USD | `-17.64%` | `147,679,200,000,000.00` |
| `Live` | `Long` | `0.1295` | 948,470.00 USD | 0.00 USD | 2,130.00 USD | `-17.00%` | `16,434,900,000,000.00` |
| `Live` | `Long` | `0.1305` | 946,340.00 USD | 0.00 USD | 16,660.00 USD | `-16.36%` | `127,649,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 929,680.00 USD | 0.00 USD | 4,380.00 USD | `-15.72%` | `33,301,600,000,000.00` |
| `Live` | `Long` | `0.1325` | 925,300.00 USD | 0.00 USD | 4,810.00 USD | `-15.07%` | `36,288,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 920,490.00 USD | 0.00 USD | 52,860.00 USD | `-14.43%` | `395,985,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 867,630.00 USD | 0.00 USD | 42,940.00 USD | `-13.79%` | `319,238,900,000,000.00` |
| `Live` | `Long` | `0.1355` | 824,690.00 USD | 0.00 USD | 3,540.00 USD | `-13.15%` | `26,114,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 821,150.00 USD | 0.00 USD | 1,690.00 USD | `-12.51%` | `12,379,800,000,000.00` |
| `Live` | `Long` | `0.1375` | 819,460.00 USD | 0.00 USD | 21,990.00 USD | `-11.87%` | `159,957,000,000,000.00` |
| `Live` | `Long` | `0.1385` | 797,470.00 USD | 0.00 USD | 13,380.00 USD | `-11.23%` | `96,623,700,000,000.00` |
| `Live` | `Long` | `0.1395` | 784,080.00 USD | 0.00 USD | 5,960.00 USD | `-10.59%` | `42,721,100,000,000.00` |
| `Live` | `Long` | `0.1405` | 778,120.00 USD | 0.00 USD | 885.87 USD | `-9.95%` | `6,305,100,000,000.00` |
| `Live` | `Long` | `0.1415` | 777,240.00 USD | 0.00 USD | 34,710.00 USD | `-9.31%` | `245,314,400,000,000.00` |
| `Live` | `Long` | `0.1425` | 742,530.00 USD | 0.00 USD | 498,880.00 USD | `-8.67%` | `3,500,889,200,000,000.00` |
| `Live` | `Long` | `0.1435` | 243,650.00 USD | 0.00 USD | 20,420.00 USD | `-8.02%` | `142,306,900,000,000.00` |
| `Live` | `Long` | `0.1445` | 223,230.00 USD | 0.00 USD | 9,510.00 USD | `-7.38%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 213,720.00 USD | 0.00 USD | 94,810.00 USD | `-6.74%` | `651,639,300,000,000.00` |
| `Live` | `Long` | `0.1465` | 118,900.00 USD | 0.00 USD | 35,240.00 USD | `-6.10%` | `240,525,800,000,000.00` |
| `Live` | `Long` | `0.1475` | 83,660.00 USD | 0.00 USD | 81,380.00 USD | `-5.46%` | `551,703,100,000,000.00` |
| `Live` | `Long` | `0.1485` | 2,290.00 USD | 0.00 USD | 2,290.00 USD | `-4.82%` | `15,410,500,000,000.00` |
| `Live` | `Short` | `0.1605` | 3,450.00 USD | 3,450.00 USD | 0.00 USD | `+2.87%` | `21,465,300,000,000.00` |
| `Live` | `Short` | `0.1615` | 7,410.00 USD | 3,970.00 USD | 0.00 USD | `+3.51%` | `24,552,400,000,000.00` |
| `Live` | `Short` | `0.1625` | 10,080.00 USD | 2,670.00 USD | 0.00 USD | `+4.15%` | `16,407,900,000,000.00` |
| `Live` | `Short` | `0.1635` | 12,010.00 USD | 1,930.00 USD | 0.00 USD | `+4.79%` | `11,828,700,000,000.00` |
| `Live` | `Short` | `0.1645` | 12,240.00 USD | 232.18 USD | 0.00 USD | `+5.44%` | `1,411,400,000,000.00` |
| `Live` | `Short` | `0.1715` | 13,730.00 USD | 1,480.00 USD | 0.00 USD | `+9.92%` | `8,642,500,000,000.00` |
| `Live` | `Short` | `0.1725` | 16,190.00 USD | 2,460.00 USD | 0.00 USD | `+10.56%` | `14,263,600,000,000.00` |
| `Live` | `Short` | `0.1745` | 17,960.00 USD | 1,770.00 USD | 0.00 USD | `+11.84%` | `10,149,600,000,000.00` |
| `Live` | `Short` | `0.1775` | 18,270.00 USD | 316.07 USD | 0.00 USD | `+13.77%` | `1,780,700,000,000.00` |
| `Live` | `Short` | `0.1785` | 18,410.00 USD | 138.82 USD | 0.00 USD | `+14.41%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1925` | 18,960.00 USD | 543.50 USD | 0.00 USD | `+23.38%` | `2,823,400,000,000.00` |
| `Live` | `Short` | `0.1945` | 19,580.00 USD | 623.68 USD | 0.00 USD | `+24.66%` | `3,206,600,000,000.00` |
| `Live` | `Short` | `0.1975` | 19,730.00 USD | 150.10 USD | 0.00 USD | `+26.59%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 31,320.00 USD | 11,590.00 USD | 0.00 USD | `+31.71%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2085` | 31,710.00 USD | 386.27 USD | 0.00 USD | `+33.64%` | `1,852,600,000,000.00` |
| `Live` | `Short` | `0.2095` | 34,940.00 USD | 3,230.00 USD | 0.00 USD | `+34.28%` | `15,423,600,000,000.00` |
| `Live` | `Short` | `0.2135` | 50,630.00 USD | 15,690.00 USD | 0.00 USD | `+36.84%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 91,970.00 USD | 41,330.00 USD | 0.00 USD | `+38.12%` | `191,801,700,000,000.00` |
| `Live` | `Short` | `0.2175` | 92,180.00 USD | 213.22 USD | 0.00 USD | `+39.41%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 206,100.00 USD | 113,920.00 USD | 0.00 USD | `+40.69%` | `518,989,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 206,210.00 USD | 114.52 USD | 0.00 USD | `+43.25%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 206,370.00 USD | 154.78 USD | 0.00 USD | `+44.53%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 213,190.00 USD | 6,820.00 USD | 0.00 USD | `+47.10%` | `29,727,000,000,000.00` |
| `Live` | `Short` | `0.2315` | 237,540.00 USD | 24,350.00 USD | 0.00 USD | `+48.38%` | `105,188,200,000,000.00` |
| `Live` | `Short` | `0.2325` | 238,740.00 USD | 1,200.00 USD | 0.00 USD | `+49.02%` | `5,179,300,000,000.00` |
| `Live` | `Short` | `0.2355` | 254,670.00 USD | 15,930.00 USD | 0.00 USD | `+50.94%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 254,780.00 USD | 102.62 USD | 0.00 USD | `+52.22%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2425` | 255,570.00 USD | 796.25 USD | 0.00 USD | `+55.43%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2445` | 255,800.00 USD | 231.03 USD | 0.00 USD | `+56.71%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2505` | 305,900.00 USD | 50,100.00 USD | 0.00 USD | `+60.56%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2545` | 306,450.00 USD | 546.54 USD | 0.00 USD | `+63.12%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 310,320.00 USD | 3,870.00 USD | 0.00 USD | `+64.40%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 339,230.00 USD | 28,910.00 USD | 0.00 USD | `+65.04%` | `112,272,400,000,000.00` |
| `Live` | `Short` | `0.2585` | 391,840.00 USD | 52,620.00 USD | 0.00 USD | `+65.68%` | `203,548,800,000,000.00` |
| `Live` | `Short` | `0.2615` | 392,000.00 USD | 154.94 USD | 0.00 USD | `+67.61%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 392,220.00 USD | 226.51 USD | 0.00 USD | `+72.09%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2715` | 405,470.00 USD | 13,240.00 USD | 0.00 USD | `+74.02%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 405,680.00 USD | 214.21 USD | 0.00 USD | `+74.66%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 417,280.00 USD | 11,600.00 USD | 0.00 USD | `+75.94%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 417,760.00 USD | 482.84 USD | 0.00 USD | `+79.14%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2885` | 423,580.00 USD | 5,810.00 USD | 0.00 USD | `+84.91%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.2915` | 423,760.00 USD | 187.26 USD | 0.00 USD | `+86.84%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 424,560.00 USD | 794.52 USD | 0.00 USD | `+87.48%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2935` | 718,570.00 USD | 294,020.00 USD | 0.00 USD | `+88.12%` | `1,001,756,400,000,000.00` |
| `Live` | `Short` | `0.3075` | 727,200.00 USD | 8,630.00 USD | 0.00 USD | `+97.09%` | `28,068,500,000,000.00` |
| `Live` | `Short` | `0.3085` | 727,570.00 USD | 363.72 USD | 0.00 USD | `+97.73%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3095` | 727,700.00 USD | 132.90 USD | 0.00 USD | `+98.37%` | `429,400,000,000.00` |
| `Live` | `Short` | `0.3105` | 739,630.00 USD | 11,930.00 USD | 0.00 USD | `+99.01%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3115` | 740,120.00 USD | 495.44 USD | 0.00 USD | `+99.65%` | `1,590,500,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 702,860.00 USD | 0.00 USD | 355.00 USD | `-77.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 702,510.00 USD | 0.00 USD | 297.50 USD | `-72.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 702,210.00 USD | 0.00 USD | 353.50 USD | `-67.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 701,860.00 USD | 0.00 USD | 276.53 USD | `-65.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 701,580.00 USD | 0.00 USD | 4,310.00 USD | `-64.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 697,270.00 USD | 0.00 USD | 475.11 USD | `-59.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 696,790.00 USD | 0.00 USD | 131.16 USD | `-58.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 696,660.00 USD | 0.00 USD | 881.45 USD | `-57.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 695,780.00 USD | 0.00 USD | 1,070.00 USD | `-56.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 694,710.00 USD | 0.00 USD | 1,050.00 USD | `-56.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 693,660.00 USD | 0.00 USD | 1,010.00 USD | `-55.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 692,650.00 USD | 0.00 USD | 4,100.00 USD | `-54.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 688,540.00 USD | 0.00 USD | 529.04 USD | `-54.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 688,020.00 USD | 0.00 USD | 2,390.00 USD | `-53.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 685,630.00 USD | 0.00 USD | 757.39 USD | `-51.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 684,870.00 USD | 0.00 USD | 1,490.00 USD | `-49.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 683,380.00 USD | 0.00 USD | 277.37 USD | `-44.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 683,110.00 USD | 0.00 USD | 262.50 USD | `-43.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 682,840.00 USD | 0.00 USD | 795.57 USD | `-43.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 682,050.00 USD | 0.00 USD | 181.00 USD | `-41.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 681,870.00 USD | 0.00 USD | 3,810.00 USD | `-35.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 678,050.00 USD | 0.00 USD | 1,550.00 USD | `-34.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 676,510.00 USD | 0.00 USD | 116.07 USD | `-31.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 676,390.00 USD | 0.00 USD | 19,070.00 USD | `-30.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 657,320.00 USD | 0.00 USD | 577.22 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 656,740.00 USD | 0.00 USD | 343.50 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 656,400.00 USD | 0.00 USD | 26,280.00 USD | `-25.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1175` | 630,120.00 USD | 0.00 USD | 105.75 USD | `-24.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 630,010.00 USD | 0.00 USD | 24,280.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 605,730.00 USD | 0.00 USD | 83,620.00 USD | `-22.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 522,100.00 USD | 0.00 USD | 487.10 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 521,620.00 USD | 0.00 USD | 14,940.00 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 506,680.00 USD | 0.00 USD | 129,320.00 USD | `-19.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 377,360.00 USD | 0.00 USD | 2,670.00 USD | `-18.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 374,690.00 USD | 0.00 USD | 473.27 USD | `-18.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 374,220.00 USD | 0.00 USD | 203,210.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 171,010.00 USD | 0.00 USD | 2,800.00 USD | `-16.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 168,210.00 USD | 0.00 USD | 1,590.00 USD | `-15.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 166,620.00 USD | 0.00 USD | 6,000.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 160,610.00 USD | 0.00 USD | 3,350.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 157,260.00 USD | 0.00 USD | 502.28 USD | `-13.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 156,760.00 USD | 0.00 USD | 162.60 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 156,600.00 USD | 0.00 USD | 700.86 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 155,900.00 USD | 0.00 USD | 13,710.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 142,190.00 USD | 0.00 USD | 108.57 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 142,080.00 USD | 0.00 USD | 3,520.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 138,550.00 USD | 0.00 USD | 127.35 USD | `-9.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 138,430.00 USD | 0.00 USD | 24,850.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 113,580.00 USD | 0.00 USD | 1,300.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 112,280.00 USD | 0.00 USD | 26,220.00 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 86,050.00 USD | 0.00 USD | 46,480.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 39,570.00 USD | 0.00 USD | 14,830.00 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 24,740.00 USD | 0.00 USD | 10,110.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 14,630.00 USD | 0.00 USD | 3,610.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 11,020.00 USD | 0.00 USD | 2,390.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 8,630.00 USD | 0.00 USD | 3,010.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 5,620.00 USD | 0.00 USD | 192.48 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 5,430.00 USD | 0.00 USD | 4,890.00 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 540.18 USD | 0.00 USD | 175.79 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 364.39 USD | 0.00 USD | 197.87 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 166.52 USD | 0.00 USD | 166.52 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1565` | 10,100.00 USD | 10,100.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1575` | 10,660.00 USD | 554.07 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1585` | 12,010.00 USD | 1,350.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1595` | 14,870.00 USD | 2,860.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1605` | 16,490.00 USD | 1,620.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1615` | 17,000.00 USD | 514.57 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 18,360.00 USD | 1,360.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 19,400.00 USD | 1,040.00 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 82,130.00 USD | 62,730.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 85,320.00 USD | 3,190.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 135,530.00 USD | 50,210.00 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 136,120.00 USD | 589.50 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 137,270.00 USD | 1,150.00 USD | 0.00 USD | `+8.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 137,590.00 USD | 317.95 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 138,150.00 USD | 564.90 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 139,950.00 USD | 1,800.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 140,520.00 USD | 571.13 USD | 0.00 USD | `+10.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 149,360.00 USD | 8,840.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 149,580.00 USD | 219.54 USD | 0.00 USD | `+11.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 150,930.00 USD | 1,350.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 151,620.00 USD | 683.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 151,950.00 USD | 336.40 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 154,420.00 USD | 2,470.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 180,810.00 USD | 26,390.00 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 192,350.00 USD | 11,540.00 USD | 0.00 USD | `+15.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 202,590.00 USD | 10,240.00 USD | 0.00 USD | `+16.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 203,450.00 USD | 864.12 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 205,980.00 USD | 2,520.00 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 206,250.00 USD | 276.75 USD | 0.00 USD | `+18.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 206,380.00 USD | 128.68 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 209,750.00 USD | 3,370.00 USD | 0.00 USD | `+19.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 213,460.00 USD | 3,700.00 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 213,700.00 USD | 245.50 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 214,360.00 USD | 660.73 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 215,060.00 USD | 697.34 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 215,280.00 USD | 222.24 USD | 0.00 USD | `+22.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 244,410.00 USD | 29,130.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 251,480.00 USD | 7,070.00 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 251,670.00 USD | 194.50 USD | 0.00 USD | `+24.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 251,810.00 USD | 137.77 USD | 0.00 USD | `+25.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 251,950.00 USD | 133.19 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 255,700.00 USD | 3,750.00 USD | 0.00 USD | `+27.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 256,190.00 USD | 492.19 USD | 0.00 USD | `+27.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 278,940.00 USD | 22,750.00 USD | 0.00 USD | `+28.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 279,500.00 USD | 560.96 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 300,840.00 USD | 21,340.00 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 386,740.00 USD | 85,900.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 388,200.00 USD | 1,470.00 USD | 0.00 USD | `+31.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 388,380.00 USD | 174.20 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 390,450.00 USD | 2,080.00 USD | 0.00 USD | `+33.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 390,710.00 USD | 252.51 USD | 0.00 USD | `+34.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 393,070.00 USD | 2,370.00 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 393,200.00 USD | 126.50 USD | 0.00 USD | `+35.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 393,560.00 USD | 356.72 USD | 0.00 USD | `+36.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 393,920.00 USD | 361.76 USD | 0.00 USD | `+38.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 394,280.00 USD | 365.12 USD | 0.00 USD | `+39.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 400,560.00 USD | 6,280.00 USD | 0.00 USD | `+40.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 400,930.00 USD | 368.47 USD | 0.00 USD | `+40.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 423,420.00 USD | 22,490.00 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 423,760.00 USD | 333.91 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 427,730.00 USD | 3,980.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 428,110.00 USD | 378.55 USD | 0.00 USD | `+44.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 428,490.00 USD | 380.23 USD | 0.00 USD | `+45.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 428,680.00 USD | 185.87 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 432,510.00 USD | 3,840.00 USD | 0.00 USD | `+46.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 477,160.00 USD | 44,650.00 USD | 0.00 USD | `+47.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 481,420.00 USD | 4,260.00 USD | 0.00 USD | `+49.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 482,940.00 USD | 1,520.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 504,160.00 USD | 21,230.00 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 506,690.00 USD | 2,530.00 USD | 0.00 USD | `+52.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 506,890.00 USD | 195.67 USD | 0.00 USD | `+53.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 526,610.00 USD | 19,720.00 USD | 0.00 USD | `+54.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 535,910.00 USD | 9,300.00 USD | 0.00 USD | `+54.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 537,820.00 USD | 1,910.00 USD | 0.00 USD | `+57.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 556,570.00 USD | 18,750.00 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 557,130.00 USD | 551.23 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 557,520.00 USD | 397.90 USD | 0.00 USD | `+59.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 561,860.00 USD | 4,330.00 USD | 0.00 USD | `+60.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 562,180.00 USD | 320.66 USD | 0.00 USD | `+61.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 578,060.00 USD | 15,880.00 USD | 0.00 USD | `+62.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 580,060.00 USD | 2,000.00 USD | 0.00 USD | `+63.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 582,610.00 USD | 2,550.00 USD | 0.00 USD | `+63.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 594,340.00 USD | 11,730.00 USD | 0.00 USD | `+64.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 599,500.00 USD | 5,160.00 USD | 0.00 USD | `+65.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 616,370.00 USD | 16,870.00 USD | 0.00 USD | `+66.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 643,160.00 USD | 26,790.00 USD | 0.00 USD | `+66.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 643,430.00 USD | 272.88 USD | 0.00 USD | `+73.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 643,550.00 USD | 114.99 USD | 0.00 USD | `+76.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 643,940.00 USD | 394.01 USD | 0.00 USD | `+77.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 644,310.00 USD | 375.53 USD | 0.00 USD | `+79.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 646,450.00 USD | 2,130.00 USD | 0.00 USD | `+82.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 647,030.00 USD | 579.27 USD | 0.00 USD | `+83.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 648,780.00 USD | 1,750.00 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 648,880.00 USD | 101.21 USD | 0.00 USD | `+89.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 649,140.00 USD | 262.73 USD | 0.00 USD | `+90.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 650,580.00 USD | 1,440.00 USD | 0.00 USD | `+90.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 656,010.00 USD | 5,430.00 USD | 0.00 USD | `+92.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 661,440.00 USD | 5,430.00 USD | 0.00 USD | `+93.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 661,730.00 USD | 289.61 USD | 0.00 USD | `+95.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 662,220.00 USD | 487.09 USD | 0.00 USD | `+96.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 668,790.00 USD | 6,570.00 USD | 0.00 USD | `+98.37%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `182.48M` | Total OI Tokens: `1,154,786,686.2 ARB`
  * 1h OI Change: `+1.46%` | 4h OI Change: `-1.87%` | 24h OI Change: `-16.10%`
  * Exchange Breakdown: Binance=`41.22M` | Bybit=`25.61M` | OKX=`13.92M` | Hyperliquid=`12.67M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.28K` | Last 24h: `-1.51K` | Last 3d: `12.63K` | Last 7d: `45.15K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0064%` | **USDT OKX** | `0.0005%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0004%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `-0.0115%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `43.70%` | `56.30%` | `0.78` | 1,650,000.00 USD |
| `15M` | `Binance` | `56.05%` | `43.95%` | `1.28` | 535,070.00 USD |
| `15M` | `OKX` | `54.2%` | `45.8%` | `1.18` | 127,330.00 USD |
| `15M` | `Bybit` | `54.29%` | `45.71%` | `1.19` | 101,090.00 USD |
| `15M` | `KuCoin` | `48.77%` | `51.23%` | `0.95` | 47,460.00 USD |
| `15M` | `Gate` | `94.04%` | `5.96%` | `15.78` | 33,320.00 USD |
| `15M` | `Bitget` | `51.34%` | `48.66%` | `1.06` | 13,810.00 USD |
| `15M` | `BingX` | `4.93%` | `95.07%` | `0.05` | 377,040.00 USD |
| `15M` | `MEXC` | `49.88%` | `50.12%` | `1.00` | 107,960.00 USD |
| `15M` | `Bitunix` | `50.58%` | `49.42%` | `1.02` | 11,660.00 USD |
| `15M` | `Hyperliquid` | `90.12%` | `9.88%` | `9.12` | 5,130.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.27%` | `48.73%` | `1.05` | 275,760.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.10 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 8,940.00 USD |
| `15M` | `HTX` | `99.88%` | `0.12%` | `832.33` | 216.20 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 89.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0.32%` | `99.68%` | `0.00` | 312.28 USD |
| `15M` | `Whale Positions` | `56.05%` | `43.95%` | `1.28` | 535,070.00 USD |
| `15M` | `Global Accounts` | `43.70%` | `56.30%` | `0.78` | 1,650,000.00 USD |
| `1H` | `ARB` | `55.19%` | `44.81%` | `1.23` | 8,410,000.00 USD |
| `1H` | `Binance` | `53.86%` | `46.14%` | `1.17` | 3,660,000.00 USD |
| `1H` | `OKX` | `58.17%` | `41.83%` | `1.39` | 1,530,000.00 USD |
| `1H` | `Bybit` | `58.48%` | `41.52%` | `1.41` | 865,840.00 USD |
| `1H` | `KuCoin` | `45.37%` | `54.63%` | `0.83` | 88,950.00 USD |
| `1H` | `Gate` | `52.53%` | `47.47%` | `1.11` | 142,950.00 USD |
| `1H` | `Bitget` | `53.91%` | `46.09%` | `1.17` | 519,590.00 USD |
| `1H` | `BingX` | `49.5%` | `50.5%` | `0.98` | 310,800.00 USD |
| `1H` | `MEXC` | `58.26%` | `41.74%` | `1.40` | 445,640.00 USD |
| `1H` | `Bitunix` | `48.85%` | `51.15%` | `0.96` | 279,000.00 USD |
| `1H` | `Hyperliquid` | `64.99%` | `35.01%` | `1.86` | 160,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.24%` | `50.76%` | `0.97` | 287,920.00 USD |
| `1H` | `Crypto.com` | `35.57%` | `64.43%` | `0.55` | 3,210.00 USD |
| `1H` | `WhiteBIT` | `74.51%` | `25.49%` | `2.92` | 98,320.00 USD |
| `1H` | `HTX` | `91.53%` | `8.47%` | `10.81` | 4,050.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.3%` | `99.7%` | `0.00` | 310.79 USD |
| `1H` | `Aster` | `70.4%` | `29.6%` | `2.38` | 3,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `14.2%` | `85.8%` | `0.17` | 7,790.00 USD |
| `1H` | `Whale Positions` | `53.86%` | `46.14%` | `1.17` | 3,660,000.00 USD |
| `1H` | `Global Accounts` | `55.19%` | `44.81%` | `1.23` | 8,410,000.00 USD |
| `4H` | `ARB` | `49.60%` | `50.40%` | `0.98` | 44,240,000.00 USD |
| `4H` | `Binance` | `49.17%` | `50.83%` | `0.97` | 15,240,000.00 USD |
| `4H` | `OKX` | `52.74%` | `47.26%` | `1.12` | 4,880,000.00 USD |
| `4H` | `Bybit` | `51.31%` | `48.69%` | `1.05` | 7,000,000.00 USD |
| `4H` | `KuCoin` | `45.92%` | `54.08%` | `0.85` | 1,280,000.00 USD |
| `4H` | `Gate` | `49.6%` | `50.4%` | `0.98` | 848,120.00 USD |
| `4H` | `Bitget` | `52.17%` | `47.83%` | `1.09` | 1,470,000.00 USD |
| `4H` | `BingX` | `35.67%` | `64.33%` | `0.55` | 3,730,000.00 USD |
| `4H` | `MEXC` | `48.62%` | `51.38%` | `0.95` | 1,870,000.00 USD |
| `4H` | `Bitunix` | `46.98%` | `53.02%` | `0.89` | 467,370.00 USD |
| `4H` | `Hyperliquid` | `46.56%` | `53.44%` | `0.87` | 680,970.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.25%` | `51.75%` | `0.93` | 6,380,000.00 USD |
| `4H` | `Crypto.com` | `43.95%` | `56.05%` | `0.78` | 14,840.00 USD |
| `4H` | `WhiteBIT` | `80.6%` | `19.4%` | `4.15` | 187,640.00 USD |
| `4H` | `HTX` | `52.68%` | `47.32%` | `1.11` | 33,290.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.43%` | `51.57%` | `0.94` | 97,740.00 USD |
| `4H` | `Aster` | `21.85%` | `78.15%` | `0.28` | 6,370.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `32.62%` | `67.38%` | `0.48` | 55,620.00 USD |
| `4H` | `Whale Positions` | `49.17%` | `50.83%` | `0.97` | 15,240,000.00 USD |
| `4H` | `Global Accounts` | `49.60%` | `50.40%` | `0.98` | 44,240,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1540` | `0.1534` | `0.1540` | `0.1545` | `0.1520` | 1,447,365.29 USD | 641,921.41 USD | 805,443.88 USD | -163,522.47 USD | `-11.30%` | `6B / 8S` |
| `5:00 UTC` | `0.1525` | `0.1530` | `0.1525` | `0.1537` | `0.1524` | 762,631.88 USD | 375,329.43 USD | 387,302.45 USD | -11,973.03 USD | `-1.57%` | `23B / 18S` |
| `0:00 UTC` | `0.1532` | `0.1537` | `0.1532` | `0.1552` | `0.1526` | 1,309,674.64 USD | 684,814.53 USD | 624,860.11 USD | 59,954.42 USD | `+4.58%` | `19B / 16S` |
| `5:00 UTC` | `0.1552` | `0.1554` | `0.1552` | `0.1563` | `0.1546` | 1,015,146.23 USD | 599,871.34 USD | 415,274.89 USD | 184,596.46 USD | `+18.18%` | `40B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1563` | `0.1557` | 778,824.29 USD | 403,907.68 USD | 374,916.61 USD | 28,991.07 USD | `+3.72%` | `13B / 12S` |
| `5:00 UTC` | `0.1560` | `0.1557` | `0.1560` | `0.1561` | `0.1552` | 724,500.45 USD | 382,680.28 USD | 341,820.18 USD | 40,860.10 USD | `+5.64%` | `10B / 13S` |
| `0:00 UTC` | `0.1560` | `0.1561` | `0.1560` | `0.1567` | `0.1555` | 659,096.24 USD | 362,345.04 USD | 296,751.20 USD | 65,593.84 USD | `+9.95%` | `17B / 13S` |
| `5:00 UTC` | `0.1568` | `0.1562` | `0.1568` | `0.1570` | `0.1554` | 510,482.89 USD | 331,670.18 USD | 178,812.71 USD | 152,857.47 USD | `+29.94%` | `56B / 25S` |
| `0:00 UTC` | `0.1575` | `0.1578` | `0.1575` | `0.1585` | `0.1566` | 1,225,850.60 USD | 572,636.93 USD | 653,213.67 USD | -80,576.74 USD | `-6.57%` | `41B / 29S` |
| `5:00 UTC` | `0.1582` | `0.1582` | `0.1582` | `0.1583` | `0.1580` | 76,442.51 USD | 33,801.46 USD | 42,641.05 USD | -8,839.59 USD | `-11.56%` | `1B / 5S` |

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
| `5m` | 49,930.00 USD | 36,020.00 USD | **`ACCUMULATION`** |
| `15m` | 56,640.00 USD | -39,660.00 USD | **`ACCUMULATION`** |
| `30m` | 65,410.00 USD | 237,700.00 USD | **`ACCUMULATION`** |
| `1h` | 44,580.00 USD | 668,350.00 USD | **`ACCUMULATION`** |
| `2h` | 161,940.00 USD | 1,470,000.00 USD | **`ACCUMULATION`** |
| `4h` | -209,740.00 USD | 425,290.00 USD | **`ACCUMULATION`** |
| `6h` | -117,630.00 USD | 981,490.00 USD | **`ACCUMULATION`** |
| `8h` | -1,830,000.00 USD | -3,950,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,010,000.00 USD | -6,410,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,100,000.00 USD | -8,510,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,690,000.00 USD | -36,620,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,220,000.00 USD | -162,600,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+49.93K` | 15m=`+56.64K` | 1h=`+44.58K` | 24h=`-2.10M`
* Futures Capital Netflows: 5m=`+36.02K` | 15m=`-39.66K` | 1h=`+668.35K` | 24h=`-8.51M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
